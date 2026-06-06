# G003 Engine Lines

Engine: Stockfish 18, official Apple Silicon binary.

Interface: python-chess.

Search: 3 seconds per selected position, MultiPV 3 except the opening tactic check, which used MultiPV 5.

Scores are from White's point of view.

## 9...Nd4 Opportunity

Position after 9.Nh2:

```text
r2qk2r/pp2bppp/2nppn2/2p4b/2B1P3/3P3P/PPPN1PPN/R1B1QRK1 b kq - 3 9
```

Played: 9...d5

Top line:

1. -1.62 9...Nd4

Eval after played move: -0.58

Human explanation:

After White's queen went to e1 and the knight moved to h2, 9...Nd4 created a concrete threat of ...Nxc2, forking the queen on e1 and rook on a1. This is an opening tactical opportunity rather than a broad opening-theory lesson.

Lesson:

When the opponent's queen and rook sit on forkable squares, check whether a knight jump creates a next-move fork.

## 20...dxc3 En Passant

Position after 20.c4:

```text
r3r1k1/2q1bpp1/2p2n1p/2p1N2b/2Pp1P2/pP1P3P/P2Q2PN/R1B2RK1 b - c3 0 20
```

Played: 20...Bd6

Top lines:

1. -2.75 20...dxc3
2. -1.06 20...Bd6
3. -0.42 20...Bg6

Eval after played move: -0.89

Human explanation:

The engine prefers taking en passant. User-reported: I considered this but rejected it because I thought keeping the structure intact restricted White's space and maintained the positional squeeze. This is stronger for the engine, but it looks like a deeper conversion/structure preference rather than the main human lesson from the game.

Lesson:

Logged as an engine preference, not a primary repair focus.

## 39...Re7

Position after 39.g4:

```text
8/1r6/2p2k1p/B1p2pp1/2Ppn1P1/pP1R1K1P/P7/8 b - - 0 39
```

Played: 39...Re7

Top lines:

1. -4.93 39...fxg4+
2. -4.64 39...Ke5
3. -4.19 39...h5

Eval after played move: -2.23

Human explanation:

39...Re7 allowed 40.Bd8, after which the rook became tactically vulnerable and Black had to give up the exchange with 40...Nc3 41.Bxe7+ Kxe7. Black was still winning because the positional and endgame advantages were large, but the conversion became less clean.

Lesson:

When converting a winning endgame, do not put the rook on a square where the bishop can attack it with tempo unless the tactic is fully accounted for.
