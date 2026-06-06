# MISS_LOG.md

Raw misses live here. Do not promote every miss into a gap. A miss becomes a gap only when it repeats or is severe enough.

## Miss Categories

- Tactical oversight
- Calculation error
- Candidate move failure
- Threat blindness
- Defensive resource missed
- Quiet move missed
- Exchange evaluation error
- King safety misevaluation
- Pawn break missed
- Bad piece or worst piece ignored
- Opening trap
- Opening drift
- Endgame technique
- Conversion failure
- Time management
- Emotional or tilt decision
- Planless move
- Overpressing
- Premature simplification
- Refusal to simplify

## Severity

Use [rubrics/severity-scale.md](/Users/arjun/dev/chess-improvement-pls/rubrics/severity-scale.md).

## Entries

### Miss 2026-06-06-01

Game: G002
Move: 29.Nf5
Position/FEN: 4rr1k/p1p3p1/8/7p/3P3q/2P1N2P/PP2R1Q1/4R1K1 w - - 2 29
Category: Calculation error / opponent resource missed / conversion failure
Severity: S4
My move: 29.Nf5
Best or better move: 29.Qg6, 29.Rf1, or 29.Rd1
Eval swing: about +5.5 to +1.4
Time spent: about 25.6 seconds, from PGN clock

What I saw:

User-reported: I thought I had calculated the tactics. ...Rxe2 did not work because Qxf7#, and ...Rxf5 did not work because Rxe8+.

What I missed:

...Qxe1!!.

Why my move was tempting:

I felt 100% winning, Black's queen looked passive, and I believed my material advantage meant the tactics should work.

Human explanation of better move:

The better moves preserve the winning position without allowing the queen capture on e1. The key failure was not checking all opponent captures before playing the forcing-looking knight move.

Root cause:

- calculation
- candidate move failure
- emotional
- time usage
- conversion

Repair idea:

When I feel completely winning and want to play a forcing move, I must check all queen captures before moving.

Promote to GAP_LOG? no

### Miss 2026-06-05-01

Game: G001
Move: 14...Nbd7
Position/FEN: rn3rk1/2q2pbp/2p1pnp1/p1Pp4/PP6/B3PN2/2Q1BPPP/R4RK1 b - - 0 14
Category: Threat blindness / candidate move failure / pawn-structure evaluation / board vision
Severity: S3
My move: 14...Nbd7
Best or better move: 14...axb4
Eval swing: about +2.1 toward White compared with 14...axb4
Time spent: not recorded; user-reported that White's fast play pulled me into their pace

What I saw:

User-reported after engine review: I tried to activate my knight.

What I missed:

I did not see or recognize that White's b-pawn was threatening b4-b5, which would become the major problem of the game.

Why my move was tempting:

User-reported after engine review: I was trying to activate a knight.

Post-game board interpretation:

14...Nbd7 is a normal-looking developing move, but the board's most urgent problem was a pawn, not a piece. With many pieces on the board, the b-pawn threat was visually easy to underweight.

Human explanation of better move:

14...axb4 removes the b-pawn before b4-b5 can happen. The lesson is not just "calculate better"; it is to notice when the opponent's obvious pawn move matters more than my piece activation.

Root cause:

- board vision
- threat recognition
- time usage
- opening knowledge
- strategic model

Repair idea:

Next time I want to activate a piece in a crowded position, I should first ask whether an opponent pawn move is about to change the whole structure.

Promote to GAP_LOG? no

### Miss YYYY-MM-DD-01

Game:
Move:
Position/FEN:
Category:
Severity:
My move:
Best or better move:
Eval swing:
Time spent:

What I saw:

What I missed:

Why my move was tempting:

Human explanation of better move:

Root cause:

- calculation
- evaluation
- pattern recognition
- time usage
- emotional
- opening knowledge
- endgame knowledge
- strategic model

Repair idea:

Next time I see ___, I should check ___.

Promote to GAP_LOG? no
