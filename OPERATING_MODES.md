# OPERATING_MODES.md

Use modes to keep each session focused.

## Game-Day Mode

Purpose: prepare for and play one serious rapid game.

Inputs:

- NEXT_DAY_PLAN.md
- active gap, if any

Output:

- saved PGN
- immediate no-engine review

## No-Engine Review Mode

Purpose: preserve human thought before Stockfish changes the memory.

Inputs:

- PGN
- memory of the game

Output:

- immediate self-review
- 3 to 5 critical moments
- evaluation guesses
- candidate moves considered

## Engine Review Mode

Purpose: compare human judgment with stronger analysis and translate the difference.

Inputs:

- no-engine review
- critical moments
- engine lines

Output:

- human explanations
- raw misses
- unclear engine ideas, if needed

## Five-Game Review Mode

Purpose: detect repeated patterns.

Inputs:

- 5 completed game reviews
- MISS_LOG.md
- SCOREBOARD.md

Output:

- one promoted gap, if evidence supports it
- one repair plan
- one measurable next-cycle focus

## Repair Drill Mode

Purpose: repair a specific gap using positions from your own games.

Inputs:

- promoted gap
- source positions

Output:

- small drill set
- pass/fail criterion
- next-game trigger

## Maintenance Mode

Purpose: keep the system lean.

Allowed:

- archive stale notes
- tighten templates
- update rubrics from experience

Not allowed:

- expanding into a generic chess notebook
- adding repertoire trees without game evidence

