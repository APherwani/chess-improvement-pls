# SCOREBOARD.md

## Rating

Starting rapid rating: 1710
Current rapid rating: 1717
Goal: 1850
Peak during this system: 1717

## Pre-System Context

All-time high: 1731
Recent tilt low: 1593
Current recovery: 1717
Distance from all-time high: 14 rating points
Recovery from recent low: 124 rating points

Last 251 games:

- Wins: 126
- Draws: 17
- Losses: 108
- Score: 134.5/251, about 53.6%

Context caveat:

Most of the losses in this sample may be tilt-contaminated from the previous downswing.

Pre-system volume clustering evidence:

| Date | Games Played | Result Pattern | Rating Movement | Lesson |
|---|---:|---|---|---|
| 2026-05-13 to 2026-05-14 | 6 | L / L / L / L / L / L | about -48 if about 8 points per game | Loss cascades can cross days. Stop rules need to interrupt streak repair, not just single-session volume. |
| 2026-05-22 | 13 | 8W / 0D / 5L | 1633 -> 1649, +16 | Even a winning day became excessive volume. The process risk was not worth 13 rapid games. |
| 2026-05-24 | 4 | W / D / L / L | 1679 -> 1662, -17 | Session started fine, then losses clustered at the end. |
| 2026-05-25 | 4 | W / L / L / L | 1670 -> 1647, -23 | First game was a win; continuing turned the day into a losing streak. |

Last 50 games:

- Rating moved from 1625 to 1717
- Net change: +92
- Average change: +1.84 rating points per game
- Wins: 29
- Draws: 3
- Losses: 18
- Score: 30.5/50, 61.0%

Defensive stability target:

Start tracking whether some losses can be converted into draws. The goal is not passive play; it is to keep defending when worse, reduce tilt losses, and make opponents prove the conversion.

Pre-system loss termination baseline:

Source: user-provided chess.com stats screenshot.

| Lost By | Share | Process Note |
|---|---:|---|
| Resignation | 68.3% | Main actionable signal: do not resign early. |
| Abandonment | 17.1% | Treat as a hard process failure. |
| Checkmate | 14.6% | Low checkmate share may mean many games end before the opponent has to prove conversion. |

Opening baseline:

Aggregate pre-system opening results are recorded in [OPENING_INCIDENTS.md](/Users/arjun/dev/chess-improvement-pls/OPENING_INCIDENTS.md). Early watchlist: Scotch Game and Philidor Defense, with small-sample caveats.

## Volume

Games played: 2
Games fully reviewed: 2
Five-game reviews completed:
Monthly reviews completed:

## Quality Metrics

Average severe misses per game: 0.5 S4/S5 after 2 games
S4/S5 misses per 5 games: 1 after 2 games
Recurring gaps promoted: 0
Gaps repaired:
Opening incidents: 1
Endgame incidents: 0
Games lost from better or equal positions: 0
Games saved from worse positions: 1
Losses converted to draws: 1
Early resignations avoided: 1
Winning positions converted: 1 tactical win by mate after opponent blunder

## Process Metrics

No-engine reviews completed: 2
Critical moments identified before engine: 13
Engine moves translated into human explanations: 10
Next-day plans completed: 2
Repair drills created from own games:

## Running Table

| Date | Game ID | Rating Before | Rating After | Result | Fully Reviewed? | S4/S5 Misses | Focus Kept? |
|---|---|---:|---:|---|---|---:|---|
| 2026-06-04 local / 2026-06-05 UTC | G001 | | 1717 | 0-1 | yes | 0 | partial |
| 2026-06-05 local / 2026-06-06 UTC | G002 | | 1717 | 1/2-1/2 | yes | 1 | partial |

## Noisy Engine Review Estimates

Use these only as loose context. Do not treat them as proof of playing strength.

| Game ID | White Estimate | Black Estimate | User Caveat |
|---|---:|---:|---|
| G001 | 1650 | 1800 | Short game; White blundered mate in one. Opening good, middlegame only okay. |
