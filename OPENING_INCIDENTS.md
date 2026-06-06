# OPENING_INCIDENTS.md

This repo does not optimize for memorizing openings.

Opening study is allowed only when triggered by game evidence.

## Trigger Rules

Log an opening incident only if:

- I fell into a trap.
- I was clearly worse by move 10 to 12.
- I reached the same structure repeatedly with no plan.
- I spent too much time because I did not know the setup.
- I misunderstood a common pawn break or piece placement.
- My safe move created a long-term passive position.

## Allowed Outputs

- one-line trap note
- typical piece-placement note
- pawn-break note
- danger-square note
- minimal move-order correction
- model middlegame plan

## Disallowed Outputs

- long memorized variations without game evidence
- engine-only opening lines I cannot explain
- repertoire expansion as procrastination

## Aggregate Opening Baseline

Source: user-provided chess.com opening statistics before this system.

Caveat: these samples are small and may be tilt-contaminated. Use them as review triggers, not as instructions to memorize openings in bulk.

| Opening | Moves | Games | Win % | Draw % | Loss % | Implied Record |
|---|---|---:|---:|---:|---:|---|
| Philidor Defense | 1. e4 e5 2. Nf3 d6 | 7 | 42.9% | 0% | 57.1% | 3W / 0D / 4L |
| Scotch Game | 1. e4 e5 2. Nf3 Nc6 3. d4 | 6 | 16.7% | 0% | 83.3% | 1W / 0D / 5L |
| Sicilian Defense | 1. e4 c5 | 6 | 33.4% | 33.3% | 33.3% | 2W / 2D / 2L |
| Scandinavian Defense | 1. e4 d5 | 5 | 60% | 0% | 40% | 3W / 0D / 2L |
| Caro-Kann Defense | 1. e4 c6 | 4 | 100% | 0% | 0% | 4W / 0D / 0L |
| Italian Game | 1. e4 e5 2. Nf3 Nc6 3. Bc4 | 4 | 100% | 0% | 0% | 4W / 0D / 0L |
| Owen's Defense | 1. e4 b6 | 3 | 33.3% | 0% | 66.7% | 1W / 0D / 2L |
| Petrov's Defense | 1. e4 e5 2. Nf3 Nf6 | 3 | 100% | 0% | 0% | 3W / 0D / 0L |
| Ruy Lopez Opening | 1. e4 e5 2. Nf3 Nc6 3. Bb5 | 3 | 33.3% | 0% | 66.7% | 1W / 0D / 2L |
| Reti Opening | 1. Nf3 | 2 | 50% | 0% | 50% | 1W / 0D / 1L |

## Baseline Watchlist

- Scotch Game is the clearest statistical concern: 1W / 0D / 5L over 6 games.
- Philidor Defense is worth watching: 3W / 0D / 4L over 7 games.
- Owen's Defense and Ruy Lopez show poor results, but only over 3 games each.
- Caro-Kann, Italian, and Petrov results are strong but too small to over-credit.

Policy: do not study any of these abstractly. If a future reviewed game reaches one of the weak-result openings and the opening affects the game, create a focused opening incident with one minimal repair.

## Incidents

### Opening Incident 2026-06-05-01

Game: G001
Color: Black
Opening: D04, Colle System structure
Move where problem began: 14...Nbd7
My move: 14...Nbd7
Better move: 14...axb4
Reason:

After 14.dxc5, White's b-pawn was threatening b4-b5 and could become the central problem. I did not see or recognize this threat and tried to activate my knight with 14...Nbd7 instead. Engine review showed that 14...axb4 would have solved the pawn problem.

Was this:

- trap? no
- bad move order? possibly
- lack of plan? yes
- tactical oversight? no
- unfamiliar pawn structure? yes
- passive but playable choice? no, normal-looking development while missing the pawn threat

One-sentence repair:

Next time in this structure, I should identify White's b4-b5 threat before developing pieces.

Minimal line to remember:

```text
1. d4 d5 2. Nf3 c6 3. e3 Nf6 4. Be2 g6 5. Nbd2 Bg7
6. O-O O-O 7. c4 Bg4 8. Qc2 Bxf3 9. Nxf3 e6
10. c5 b6 11. b4 Qc7 12. a4 a5 13. Ba3 bxc5 14. dxc5
```

Structure note:

At this moment, do not auto-develop with ...Nbd7. Check whether ...axb4 removes the biggest pawn problem before White plays b5.

### Opening Incident YYYY-MM-DD-01

Game:
Color:
Opening:
Move where problem began:
My move:
Better move:
Reason:

Was this:

- trap?
- bad move order?
- lack of plan?
- tactical oversight?
- unfamiliar pawn structure?
- passive but playable choice?

One-sentence repair:

Next time in this structure, I should ___.

Minimal line to remember:

```text

```
