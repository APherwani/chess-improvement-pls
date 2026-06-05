#!/usr/bin/env python3
"""Analyze selected PGN moments with a UCI engine."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import chess
import chess.engine
import chess.pgn


def score_text(score: chess.engine.PovScore) -> str:
    white_score = score.pov(chess.WHITE)
    mate = white_score.mate()
    if mate is not None:
        return f"M{mate}"
    cp = white_score.score()
    if cp is None:
        return "?"
    return f"{cp / 100:+.2f}"


def pv_text(board: chess.Board, pv: list[chess.Move]) -> str:
    line_board = board.copy()
    sans: list[str] = []
    for move in pv:
        sans.append(line_board.san(move))
        line_board.push(move)
    return " ".join(sans)


def load_game(path: Path) -> chess.pgn.Game:
    with path.open(encoding="utf-8") as handle:
        game = chess.pgn.read_game(handle)
    if game is None:
        raise ValueError(f"No game found in {path}")
    return game


def boards_by_ply(game: chess.pgn.Game) -> dict[int, tuple[chess.Board, str | None]]:
    board = game.board()
    positions: dict[int, tuple[chess.Board, str | None]] = {0: (board.copy(), None)}
    for ply, move in enumerate(game.mainline_moves(), start=1):
        san = board.san(move)
        board.push(move)
        positions[ply] = (board.copy(), san)
    return positions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pgn", type=Path)
    parser.add_argument(
        "--before-ply",
        type=int,
        action="append",
        required=True,
        help="Analyze the position after this ply, before the next move. May be repeated.",
    )
    parser.add_argument(
        "--engine",
        default=os.environ.get("STOCKFISH_PATH", "stockfish"),
        help="Path to UCI engine. Defaults to STOCKFISH_PATH or stockfish.",
    )
    parser.add_argument("--time-ms", type=int, default=1000)
    parser.add_argument("--multipv", type=int, default=3)
    args = parser.parse_args()

    game = load_game(args.pgn)
    positions = boards_by_ply(game)
    limit = chess.engine.Limit(time=args.time_ms / 1000)

    with chess.engine.SimpleEngine.popen_uci(args.engine) as engine:
        for before_ply in args.before_ply:
            if before_ply not in positions:
                print(f"Missing ply {before_ply}", file=sys.stderr)
                return 1

            board, previous_san = positions[before_ply]
            next_position = positions.get(before_ply + 1)
            played_san = next_position[1] if next_position else None

            print(f"## After ply {before_ply}: {previous_san}")
            print()
            print(f"FEN: `{board.fen()}`")
            if played_san:
                print(f"Played: `{played_san}`")

            infos = engine.analyse(board, limit, multipv=args.multipv)
            if isinstance(infos, dict):
                infos = [infos]

            print()
            print("Top lines:")
            for index, info in enumerate(infos, start=1):
                pv = info.get("pv", [])
                score = score_text(info["score"])
                line = pv_text(board, pv)
                print(f"{index}. {score} `{line}`")

            if next_position is not None:
                after_board = next_position[0]
                after_info = engine.analyse(after_board, limit)
                print()
                print(f"Eval after played move: {score_text(after_info['score'])}")

            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

