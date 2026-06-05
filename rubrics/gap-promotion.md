# Gap Promotion Rubric

A miss becomes a gap only if it repeats or is severe enough.

Promote a miss to [GAP_LOG.md](/Users/arjun/dev/chess-improvement-pls/GAP_LOG.md) if:

1. The same pattern appears in 3 games.
2. It causes 2 serious eval swings.
3. It directly causes a loss from an equal or better position.
4. It reveals a missing chess concept you cannot explain.

## Good Gap

```text
Missing backward defensive moves.
```

Evidence:

- Game 012: missed Nd2, defending f3 and rerouting to c4.
- Game 017: missed Be1, defending g3 while keeping rook active.
- Game 019: missed Kh1, stepping out of tactics before attacking.

Repair:

```text
Before committing in tense positions, ask:
"Is there a quiet move that defends the threat and improves my worst piece?"
```

## Weak Gap

```text
I blundered once.
```

This should stay in MISS_LOG.md unless it repeats or is severe enough to shape future behavior.

