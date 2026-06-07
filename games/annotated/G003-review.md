# G003 Review

## Game Info

Game ID: G003
Date: 2026-06-06
Time control: 10+0
Color: Black
Opponent rating: 1723
My rating before: 1717
My rating after: 1725
Result: 0-1, win by resignation
Opening: B50, Sicilian Defense
PGN: games/raw-pgn/G003.pgn
Engine lines: games/engine-lines/G003-engine.md

## Source Discipline Note

In Phase 1 and Phase 2, write only user-reported memory. If a thought was not captured, mark it as not captured.

## Phase 1: Immediate No-Engine Self-Review

Emotional state: not captured yet
Time trouble? not captured yet

Where did I feel comfortable?

User-reported: I was not really ever in trouble in this game.

Where did I feel confused?

Not captured yet.

Where did I feel under pressure?

User-reported: not really ever in trouble, even after going exchange down.

Where did I feel winning?

User-reported: even an exchange down, my positional advantage was dominant enough that it did not end up mattering.

Overall game quality:

User-reported: this was actually a pretty clean game. I got an early advantage and never really let go. The conversion could have been a little cleaner, but it was not bad overall. Accuracy was over 80% in a roughly 50-move game, which counts for something.

Where did I feel lost?

Not captured yet.

What move do I most suspect was bad?

User-reported: 39...Re7 was the big blunder, because it allowed exactly White's next sequence and led to losing the exchange, my rook for White's bishop.

What position do I want to check with the engine?

User-reported: 39...Re7, and whether the conversion after going exchange down could have been cleaner.

What was my plan after the opening?

Not captured yet.

What was my opponent's main threat that I noticed?

Not captured yet.

What threat did I possibly miss?

Not captured yet.

## Phase 2: Human Critical Moments Before Engine

### Critical Moment 1

Move: 39...Re7
Position/FEN: 8/1r6/2p2k1p/B1p2pp1/2Ppn1P1/pP1R1K1P/P7/8 b - - 0 39
My move: 39...Re7
Candidate moves I considered: not captured.
Move I would choose now without engine: not captured.
Evaluation guess: Black still winning or at least positionally dominant after the exchange loss.
Estimated eval: not provided.

My reasoning during the game:

Not captured.

What I missed or was unsure about:

User-reported: 39...Re7 allowed exactly White's next move sequence and led to an exchange loss: my rook for White's bishop.

Line I calculated:

Not captured.

Post-game interpretation:

User-reported: the exchange loss was not enough to lose because Black's positional advantage was still dominant. The conversion could have been cleaner, but the endgame conversion was good enough to win.

User-reported overall: despite the conversion mistake, this was a clean game where I got an early advantage and did not really let go.

## Post-Engine Added Critical Moments

### Added Moment 1

Move: 9...d5 after 9.Nh2
Position/FEN: r2qk2r/pp2bppp/2nppn2/2p4b/2B1P3/3P3P/PPPN1PPN/R1B1QRK1 b kq - 3 9
My move: 9...d5
Engine better move: 9...Nd4

User-reported after engine review:

After White's odd Qe1 setup, I could have played ...Nd4 and threatened to fork the queen on e1 and rook on a1.

What was missed:

The concrete knight-jump tactic. The fork is a next-move threat: ...Nd4 threatens ...Nxc2, where the knight attacks queen and rook.

Human explanation:

This is a useful opening tactical pattern, not a reason to study a big Sicilian line.

### Added Moment 2

Move: 20...Bd6 after 20.c4
Position/FEN: r3r1k1/2q1bpp1/2p2n1p/2p1N2b/2Pp1P2/pP1P3P/P2Q2PN/R1B2RK1 b - c3 0 20
My move: 20...Bd6
Engine better move: 20...dxc3 en passant

User-reported after engine review:

I considered taking en passant, but thought it was weaker because the current structure restricted White's space and applied a positional squeeze. I do not want to focus on this one; it feels like a deeper or more esoteric computer line.

What was missed:

The engine's stronger structural conversion move.

Human explanation:

Logged as an engine preference, not a primary repair focus.

## Phase 3: Engine Comparison

Engine: Stockfish 18, official Apple Silicon binary.

Engine details: [games/engine-lines/G003-engine.md](/Users/arjun/dev/chess-improvement-pls/games/engine-lines/G003-engine.md)

### Engine Moment 1: 9...Nd4 Opportunity

Engine preferred move: 9...Nd4.

Engine eval before my move: about -1.6.

Engine eval after my move: about -0.6.

Eval swing: about 1 point toward White.

Human explanation:

9...Nd4 creates the threat of ...Nxc2, forking the queen on e1 and rook on a1. This is a concrete tactic caused by White's awkward queen/rook geometry.

Could I realistically have found this in a rapid game? yes.

Thinking habit:

When the opponent's queen and rook line up on forkable squares, check knight jumps that create a next-move fork.

### Engine Moment 2: 20...dxc3 En Passant

Engine preferred move: 20...dxc3.

Engine eval before my move: about -2.8.

Engine eval after my move: about -0.9.

Eval swing: about 1.9 points toward White.

Human explanation:

The engine says taking en passant was stronger than preserving the locked structure. User-reported: I considered it and chose the squeeze instead. Since the current structure still produced a dominant position and this looks like a deeper computer preference, this is not the main lesson.

Could I realistically have found this in a rapid game? yes, but it is not the priority repair.

Simpler rule:

When the engine prefers an unintuitive structural capture I considered and rejected, log it but do not overfit unless it repeats.

### Engine Moment 3: 39...Re7

Engine preferred moves: 39...fxg4+, 39...Ke5, or 39...h5.

Engine eval before my move: about -4.9.

Engine eval after my move: about -2.2.

Eval swing: about 2.7 points toward White.

Human explanation:

39...Re7 was the main confirmed conversion mistake. It allowed 40.Bd8, making the rook tactically vulnerable and leading to the exchange loss after 40...Nc3 41.Bxe7+ Kxe7. Black remained winning, but the conversion became much less clean.

Could I realistically have avoided this? yes.

Thinking habit:

In winning endgames, check whether the bishop has a tempo attack on the rook before moving the rook to a new square.

## Logged Misses

Biggest tactical miss:

User-reported candidate: 39...Re7 allowing the exchange loss after 40.Bd8 Nc3 41.Bxe7+ Kxe7.

Biggest positional or strategic miss:

User-reported: conversion could have been cleaner despite the dominant positional advantage.

Biggest time-usage or decision-process miss:

Not captured yet.

## Incidents

Opening incident? no. There was a post-engine opening tactical opportunity with 9...Nd4, but no opening incident requiring repertoire study.

Endgame incident? yes, light conversion review. User-reported that the conversion could have been cleaner, though it was good enough to win.

## Next Game

One focus:

Clean rook safety during conversion.

Trigger:

I am winning an endgame and moving a rook near an active bishop.

Question to ask during the next game:

Does their bishop have a tempo attack on my rook?
