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

### Miss 2026-06-05-01

Game: G001
Move: 12...a5
Position/FEN: rn3rk1/p1q2pbp/1pp1pnp1/2Pp4/PP1P4/4PN2/2Q1BPPP/R1B2RK1 b - - 0 12
Category: Candidate move failure / opening drift / pawn-structure evaluation
Severity: S2
My move: 12...a5
Best or better move: 12...bxc5, 12...Nbd7, or 12...Rc8
Eval swing: about +0.6 toward White compared with the engine's preferred options
Time spent: not recorded; user-reported that White's fast play pulled me into their pace

What I saw:

User-reported: I thought 12...a5 was fine. The specific during-game intention behind ...a5 was not captured.

What I missed:

I did not fully price White's natural b5-b6 plan and the supported passed pawn that could follow.

Why my move was tempting:

Not captured as a during-game thought.

Post-game board interpretation:

...a5 challenges White's queenside expansion and looks active, which may explain why it is easy to play automatically. That is interpretation, not recorded memory.

Human explanation of better move:

The better options either clarify the c5 tension or continue development without immediately giving White such a clean queenside lever. The main issue was not that ...a5 is always bad; it was that I played it without consciously naming White's pawn break and passed-pawn route.

Root cause:

- evaluation
- time usage
- opening knowledge
- strategic model

Repair idea:

Next time I consider a flank pawn move that changes a pawn-majority structure, I should ask what pawn break and passed pawn I am allowing.

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
