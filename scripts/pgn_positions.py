#!/usr/bin/env python3
"""Print positions from a PGN with move labels and FENs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import chess.pgn


def move_label(board: chess.Board) -> str:
    if board.turn == chess.WHITE:
        return f"{board.fullmove_number}. White to move"
    return f"{board.fullmove_number}... Black to move"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pgn", type=Path)
    parser.add_argument(
        "--after-ply",
        type=int,
        action="append",
        default=[],
        help="Print only positions after this ply number. May be repeated.",
    )
    args = parser.parse_args()

    with args.pgn.open(encoding="utf-8") as handle:
        game = chess.pgn.read_game(handle)

    if game is None:
        print(f"No game found in {args.pgn}", file=sys.stderr)
        return 1

    requested = set(args.after_ply)
    board = game.board()
    rows = [(0, "start", move_label(board), board.fen())]

    for ply, move in enumerate(game.mainline_moves(), start=1):
        san = board.san(move)
        board.push(move)
        rows.append((ply, san, move_label(board), board.fen()))

    for ply, san, label, fen in rows:
        if requested and ply not in requested:
            continue
        print(f"{ply:>2} | {san:<8} | {label:<20} | {fen}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

