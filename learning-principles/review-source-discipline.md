# Review Source Discipline

The system is only useful if it preserves the user's actual thought process.

## Rule

Do not reconstruct the user's during-game reasoning from the board, the engine, or hindsight.

If the user did not report a thought, write:

```text
Not captured.
```

Then ask a targeted follow-up if the missing thought matters.

## Allowed Buckets

User-reported memory:

- what the user says they saw
- what the user says they missed
- what the user says they calculated
- what the user says they felt

Post-game interpretation:

- what the user now thinks after the game but before engine
- what the move appears to have done on the board

Engine interpretation:

- what Stockfish prefers
- eval changes
- human translation of engine lines

Post-engine-added critical moment:

- a moment the no-engine pass missed
- must be labeled as discovered after engine review
- must not be inserted into the no-engine critical moment list

Codex inference:

- any reconstruction not explicitly reported by the user

Codex inference must be labeled and should be used sparingly.

## Failure Mode

Bad:

```text
My reasoning during the game: I challenged White's queenside counterplay.
```

This is bad if the user did not actually report that thought.

Good:

```text
My reasoning during the game: not captured.

Post-game interpretation: the move functioned as queenside counterplay, but that was not reported as the user's conscious intention.
```
