# G002 Engine Lines

Engine: Stockfish 18, official Apple Silicon binary.

Interface: python-chess.

Search: 3 seconds per selected position, MultiPV 3.

Scores are from White's point of view.

## 29.Nf5

Position after 28...Qh4:

```text
4rr1k/p1p3p1/8/7p/3P3q/2P1N2P/PP2R1Q1/4R1K1 w - - 2 29
```

Played: 29.Nf5

Top lines:

1. +5.54 29.Qg6
2. +4.36 29.Rf1
3. +4.21 29.Rd1

Eval after played move: +1.40

Human explanation:

29.Nf5 did not immediately lose, but it threw away most of a completely winning advantage. The missed resource was 29...Qxe1!!, which forces trades and makes the game much harder. The calculation checked rook captures, but missed the queen capture.

Lesson:

When winning and playing a forcing-looking move, check every opponent capture by queen, rook, and bishop before trusting the tactic.

## 31.Kf2 Resource

Position after 30...Rxe1+:

```text
5r1k/p1p3p1/8/5N1p/3P4/2P4P/PP4Q1/4r1K1 w - - 0 31
```

Played: 31.Kh2

Top lines:

1. +1.43 31.Kf2
2. -0.01 31.Kh2
3. -7.07 31.Qf1

Eval after played move: +0.00

Human explanation:

31.Kf2 looks wrong because it walks the king toward the center and into the mess, but it is the engine's resource to keep White better. 31.Kh2 felt natural and safe, but it allowed the game to become roughly equal.

Lesson:

After a blunder, do not emotionally dismiss the game. There may still be one strange defensive resource that keeps the advantage or saves the result.

## Move 32 Time-Pressure Phase

Position after 32.Qg6:

```text
7k/p1p3p1/6Q1/5r1p/3P4/2P4P/PP5K/4r3 b - - 1 32
```

Played: 32...Re2+

Top lines:

1. -6.22 32...Rf2+
2. -2.63 32...Ref1
3. -0.30 32...Re2+

Eval after played move: -0.12

Human explanation:

The position was dangerous and tactically unstable. Black had winning chances, but did not choose the strongest continuation. This belongs in the time-pressure bucket rather than becoming a separate primary lesson.

## Move 43 Time-Pressure Phase

Position after 43.Qf1:

```text
7k/p1p3p1/8/7p/2PP4/7P/Pr4r1/5Q1K b - - 2 43
```

Played: 43...Rgf2

Top lines:

1. -7.02 43...Rgf2
2. -2.30 43...Rge2
3. -1.43 43...Rh2+

Eval after played move: -7.61

Human explanation:

By this point White was defending a very dangerous position under severe time pressure. The fact that the game still ended in a draw is a practical defensive success, even though the position had become objectively losing.

Post-engine user note:

At move 43, White's attention was on not blundering from frustration and surviving with very little time. The a-pawn plan was not recognized during the game, and Black may not have recognized it either with under a minute left.

Lesson:

The no-early-resignation rule mattered here: after throwing away the win, continuing to defend still saved half a point.
