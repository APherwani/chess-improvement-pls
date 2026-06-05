# Chess Improvement PLS

This is a repo-backed personal learning system for improving at chess rapid.

Current level: 1710 chess.com rapid.

First goal: 1850 chess.com rapid.

Stretch goal: 2000 if progress and enjoyment remain strong.

The system is not a generic chess-study repo. It is a forensic review system for your own games.

## Core Loop

```text
play one serious rapid game
-> write no-engine self-review
-> identify 3 to 5 critical moments
-> compare with engine
-> translate engine ideas into human explanations
-> log raw misses
-> promote repeated or severe misses into gaps
-> create one repair focus for the next game
```

## Start Here

1. Read [NEXT_DAY_PLAN.md](/Users/arjun/dev/chess-improvement-pls/NEXT_DAY_PLAN.md).
2. Play one serious rapid game.
3. Save the PGN in [games/raw-pgn](/Users/arjun/dev/chess-improvement-pls/games/raw-pgn).
4. Use [templates/game-review-template.md](/Users/arjun/dev/chess-improvement-pls/templates/game-review-template.md).
5. Update [GAME_LOG.md](/Users/arjun/dev/chess-improvement-pls/GAME_LOG.md), [MISS_LOG.md](/Users/arjun/dev/chess-improvement-pls/MISS_LOG.md), and [NEXT_DAY_PLAN.md](/Users/arjun/dev/chess-improvement-pls/NEXT_DAY_PLAN.md).

## Local Tooling

Install review helpers:

```bash
python3 -m pip install -r requirements.txt
```

Print FENs from a saved PGN:

```bash
python3 scripts/pgn_positions.py games/raw-pgn/G001.pgn --after-ply 23
```

Run engine comparison after the no-engine review is complete:

```bash
STOCKFISH_PATH=.local/stockfish/stockfish/stockfish-macos-m1-apple-silicon \
python3 scripts/analyze_moments.py games/raw-pgn/G001.pgn --before-ply 23
```

The local Stockfish binary is intentionally ignored by Git. Download it from the official Stockfish page and place it under `.local/stockfish/`.

## Study Policy

Openings and endgames are studied only when your games create evidence that the knowledge matters.

Allowed:

- opening trap notes from your games
- typical piece placement from repeated structures
- pawn-break notes from recurring middlegames
- endgame model positions from failed conversions or failed holds
- repair drills generated from your own games

Disallowed:

- broad opening memorization
- long engine-only variations you cannot explain
- random puzzle grinding disconnected from misses
- collecting notes to avoid reviewing games

## Main Files

- [PRACTICE_MODEL.md](/Users/arjun/dev/chess-improvement-pls/PRACTICE_MODEL.md): the rules of the training loop
- [TODAY.md](/Users/arjun/dev/chess-improvement-pls/TODAY.md): today's game and review workspace
- [NEXT_DAY_PLAN.md](/Users/arjun/dev/chess-improvement-pls/NEXT_DAY_PLAN.md): one focus for the next serious game
- [GAME_LOG.md](/Users/arjun/dev/chess-improvement-pls/GAME_LOG.md): index of played and reviewed games
- [MISS_LOG.md](/Users/arjun/dev/chess-improvement-pls/MISS_LOG.md): raw misses from individual games
- [GAP_LOG.md](/Users/arjun/dev/chess-improvement-pls/GAP_LOG.md): repeated or severe patterns promoted from misses
- [STYLE_PROFILE.md](/Users/arjun/dev/chess-improvement-pls/STYLE_PROFILE.md): evidence-backed model of you as a player
- [SCOREBOARD.md](/Users/arjun/dev/chess-improvement-pls/SCOREBOARD.md): rating, process, and quality metrics

## Cadence

- Daily: one serious game plus structured review.
- Exception: if the opponent blunders massively and the game ends in under 5 minutes, a second rated game is allowed.
- If you blunder massively, continue and review the game.
- Every 5 games: complete a five-game pattern review.
- Monthly: summarize rating trend, recurring gaps, and repaired weaknesses.
