# G001 Engine Lines

Engine: Stockfish 18, official Apple Silicon binary.

Interface: python-chess.

Search: 5 seconds per selected position, MultiPV 3, except final mate confirmation from a shorter pass.

Scores are from White's point of view.

## 12...a5

Position after 12.a4:

```text
rn3rk1/p1q2pbp/1pp1pnp1/2Pp4/PP1P4/4PN2/2Q1BPPP/R1B2RK1 b - - 0 12
```

Played: 12...a5

Top lines:

1. +0.49 12...bxc5 13.bxc5 Nbd7
2. +0.51 12...Nbd7
3. +0.59 12...Rc8

Eval after played move: +1.12

Human explanation:

12...a5 is not the concrete losing mistake from this game, but it is an early structural warning. It challenges b4, but it also means Black must stay alert to White's b-pawn. In the game, Black later had a clear chance to solve that pawn problem with 14...axb4.

Lesson:

After playing a move like ...a5, keep tracking the pawn it challenged. Do not switch into routine development while that pawn can still advance.

## 13...bxc5

Position after 13.Ba3:

```text
rn3rk1/2q2pbp/1pp1pnp1/p1Pp4/PP1P4/B3PN2/2Q1BPPP/R4RK1 b - - 1 13
```

Played: 13...bxc5

Top lines:

1. +0.26 13...axb4 14.cxb6 Qxb6
2. +0.51 13...bxc5 14.bxc5 Nbd7
3. +1.13 13...Rc8

Eval after played move: +0.39

Human explanation:

The suspected 13...bxc5 was not the main blunder. After White chose 13.Ba3, Black's played capture is close to acceptable. The engine's preferred 13...axb4 directly removes the advanced b-pawn before it can become the supported passer, and after cxb6 Qxb6 Black has at least eliminated the scariest queenside pawn.

Lesson:

Your post-game suspicion was directionally good, but the concrete miss came after White recaptured on c5. Black still had a chance to solve the b-pawn problem with ...axb4.

## 14...Nbd7

Position after 14.dxc5:

```text
rn3rk1/2q2pbp/2p1pnp1/p1Pp4/PP6/B3PN2/2Q1BPPP/R4RK1 b - - 0 14
```

Played: 14...Nbd7

Top lines:

1. -0.28 14...axb4 15.Bxb4 Na6
2. +0.61 14...Na6 15.b5
3. +1.04 14...Ne4 15.b5

Eval after played move: +1.82

Human explanation:

This is the concrete engine-confirmed miss. The biggest problem in the position is White's b-pawn: b4-b5 is coming, and if Black lets it happen, the pawn can become the main feature of the game. 14...Nbd7 develops a piece, but it does not address the pawn threat. 14...axb4 removes the problem while it is still removable.

Lesson:

When there are many pieces on the board, do not let piece activity distract from the most urgent pawn move. Before developing a piece, ask whether there is a pawn threat that will become permanent next move.

## 16...e4

Position after 16.b5:

```text
r4rk1/2qn1pbp/2p2np1/pPPpp3/P7/B3PN2/2Q1BPPP/2R2RK1 b - - 0 16
```

Played: 16...e4

Top lines:

1. +1.71 16...Rfe8
2. +1.83 16...h5
3. +1.96 16...Rfd8

Eval after played move: +2.18

Human explanation:

By this point White is already better because Black missed the chance to remove the b-pawn on move 14. 16...e4 creates kingside space and practical chances, but it does not solve the b-pawn. The engine prefers slower moves that improve coordination or defensive readiness before trying to race.

Lesson:

When the opponent's passed pawn is about to become dangerous, check whether your active counterplay actually changes that race or just changes the subject.

## 20...Neg4

Position after 20.Qb3:

```text
rqr3k1/5pbp/1Pp2np1/p1Ppn3/P2Np3/1Q2P3/1B2BPPP/2R2RK1 b - - 6 20
```

Played: 20...Neg4

Top lines:

1. +1.94 20...Re8
2. +2.25 20...Rf8
3. +2.30 20...Qb7

Eval after played move: +2.91

Human explanation:

20...Neg4 is a practical attacking try, and it creates the exact Qh2 motif that wins after White's h3. But objectively it appears to worsen Black's position because White has defensive resources and the queenside passer remains extremely strong. This was a successful swindle pattern, not proof that the attack was sound.

Lesson:

Do not let a later opponent blunder retroactively validate a speculative attack.

## 21...Qh2#

Position after 21.h3:

```text
rqr3k1/5pbp/1Pp2np1/p1Pp4/P2Np1n1/1Q2P2P/1B2BPP1/2R2RK1 b - - 0 21
```

Played: 21...Qh2#

Engine confirms mate in 1.

Human explanation:

White's h-pawn moved off h2 and opened the b8-h2 diagonal. The queen reaches h2, the king cannot capture because the knight on g4 guards h2, and White has no escape.

Lesson:

This was a tactical success: you saw and used the queen-knight mating pattern.
