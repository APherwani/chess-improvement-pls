# Engine Translation Rubric

The engine is a comparison tool, not the teacher by itself.

Do not log:

```text
Stockfish says Ne2 was best.
```

Do log:

```text
Ne2 defends c1, clears f4 for the bishop, avoids weakening the kingside pawns, and prepares Nc3 where the knight attacks d5. My h3 solved only the immediate bishop pin, created a hook, and did not improve any piece.
```

## Required Questions

- What threat does the move address?
- What new threat does it create?
- Which piece improves?
- Which weakness does it target?
- What does it prevent?
- Why was my move tempting?
- Why is the engine move more precise?
- What transfers to future games?

## Classification

Classify every useful engine recommendation as one or more:

- tactical resource
- defensive resource
- piece improvement
- king safety
- pawn structure
- square control
- initiative
- endgame conversion
- exchange evaluation
- move-order issue
- prophylaxis

If no classification fits, use:

```text
unclear engine idea
```

