# G001 Review

## Game Info

Game ID: G001
Date: 2026-06-04 local / 2026-06-05 UTC in PGN
Time control: 10+0
Color: Black
Opponent rating: 1698
My rating before: 1717
My rating after:
Result: 0-1, Black won by checkmate
Opening: D04, Colle System structure
PGN: games/raw-pgn/G001.pgn
Engine lines: games/engine-lines/G001-engine.md

## Phase 1: Immediate No-Engine Self-Review

Emotional state: fine.
Time trouble? no.

Where did I feel comfortable?

The opening initially felt fine. White was playing very fast, and I felt I had a normal setup even though I do not know much about the Colle System.

Where did I feel confused?

I started feeling uncomfortable around the queenside structure after committing to ...a5 and later realizing White's b-pawn could advance to b5-b6. I had not consciously priced the supported passed pawn.

Where did I feel under pressure?

After White created the supported passed pawn on b6. It looked scary, and I felt I suddenly had to generate counterplay instead of just playing a normal position.

Where did I feel winning?

Only once the queen and knights were coordinating against White's king and White allowed Qh2#.

Where did I feel lost?

Not exactly lost, but uncomfortable once the b6 passer appeared.

What move do I most suspect was bad?

Move 13, ...bxc5, is the main suspect. Move 12, ...a5, may be playable, but I did not understand what kind of position I was choosing.

What position do I want to check with the engine?

The queenside tension around moves 12 and 13: whether ...a5 and then ...bxc5 was strategically sound, or whether I should have clarified the c5 tension earlier.

What was my plan after the opening?

I tried to create counterplay on the kingside with the knights and queen, especially with the queen on b8 pointing toward h2.

What was my opponent's main threat that I noticed?

The supported passed pawn on b6 after b5-b6.

What threat did I possibly miss?

I missed how direct and natural White's queenside pawn majority play was: b5, b6, and a strong bishop supporting the passed pawn.

First critical moment I remember:

The decision around 12...a5 and 13...bxc5, because I walked into a structure where White's queenside play was obvious in hindsight.

How much time did I spend there?

Not recorded, but likely less than the position deserved because White's fast play pulled me into their pace.

Did I ask what my opponent was threatening?

Not explicitly enough. I did not fully ask what White's queenside pawn majority was threatening before committing to the structure.

Note: I accidentally glanced at the eval bar briefly, but turned it off promptly and did not get useful information from it. Treat this review as no-engine.

## Phase 2: Human Critical Moments Before Engine

### Critical Moment 1

Move: 12...a5
Position/FEN: rn3rk1/p1q2pbp/1pp1pnp1/2Pp4/PP1P4/4PN2/2Q1BPPP/R1B2RK1 b - - 0 12
My move: 12...a5
Candidate moves I considered: not clearly remembered; in review, ...bxc5 to clarify the c5 tension looks like the simpler candidate to compare.
Move I would choose now without engine: I would slow down and decide whether ...a5 is a conscious structural commitment or whether I should first resolve the c5 tension.
Evaluation guess: unclear, but probably playable for Black if I understand the queenside consequences.
Estimated eval: roughly equal to slightly uncomfortable for Black in practical terms.

My reasoning during the game:

The move looked natural as queenside counterplay against White's space. I did not treat it as a major commitment.

What I missed or was unsure about:

I did not fully see that White's b5-b6 plan could become very direct, creating a supported passed pawn and giving the bishop on a3/b2 a strong role.

Line I calculated:

Only loosely: ...a5, White continues queenside expansion, and I look for counterplay. I did not deeply calculate the b5-b6 structure.

### Critical Moment 2

Move: 13...bxc5
Position/FEN: rn3rk1/2q2pbp/1pp1pnp1/p1Pp4/PP1P4/B3PN2/2Q1BPPP/R4RK1 b - - 1 13
My move: 13...bxc5
Candidate moves I considered: not clearly remembered.
Move I would choose now without engine: I would compare ...bxc5 with maintaining tension and with earlier simplification plans. The key is not the exact move yet; it is understanding what pawn structure I am allowing.
Evaluation guess: this may be where Black's practical problem begins.
Estimated eval: unclear, but I suspect White may become easier to play.

My reasoning during the game:

I likely treated the capture as normal tension release.

What I missed or was unsure about:

After dxc5, White keeps queenside space and can use b5-b6 to create a dangerous passer. I underestimated how obvious and forcing White's queenside play would become.

Line I calculated:

I did not fully calculate the follow-up b5-b6 and how uncomfortable the supported passer would feel.

### Critical Moment 3

Move: 16...e4 after 16.b5
Position/FEN: r4rk1/2qn1pbp/2p2np1/pPPpp3/P7/B3PN2/2Q1BPPP/2R2RK1 b - - 0 16
My move: 16...e4
Candidate moves I considered: kingside counterplay ideas; not sure whether I seriously considered eliminating the b-pawn.
Move I would choose now without engine: I would first ask whether I can or must stop b6 before starting kingside play.
Evaluation guess: practically scary for Black because White can create a supported passer, but Black may have counterplay.
Estimated eval: unclear.

My reasoning during the game:

I switched to counterplay: if White is getting a queenside passer, I need activity against the king.

What I missed or was unsure about:

I did not know whether allowing b6 was objectively acceptable compensation or just panic-counterplay. This is the main strategic question of the game.

Line I calculated:

White advances b6, my queen retreats to b8, and I try to coordinate queen and knights toward the kingside.

### Critical Moment 4

Move: 20...Neg4
Position/FEN: rqr3k1/5pbp/1Pp2np1/p1Ppn3/P2Np3/1Q2P3/1B2BPPP/2R2RK1 b - - 6 20
My move: 20...Neg4
Candidate moves I considered: kingside attacking moves with the knights and queen.
Move I would choose now without engine: 20...Neg4 still looks like the practical attacking idea to examine.
Evaluation guess: Black has real threats, but I do not know whether they compensate for the queenside passer.
Estimated eval: unclear.

My reasoning during the game:

The queen on b8 and knight jump to g4 coordinate against h2. This was my practical compensation for the queenside pressure.

What I missed or was unsure about:

I am not sure whether the attack was sound or whether White simply walked into it.

Line I calculated:

After h3, Qh2# is mate.

### Final Tactical Moment

Move: 21...Qh2#
Position/FEN before move: rqr3k1/5pbp/1Pp2np1/p1Pp4/P2Np1n1/1Q2P2P/1B2BPP1/2R2RK1 b - - 0 21
My move: 21...Qh2#

Human note:

White's h3 opened h2 and allowed the queen to finish the b8-h2 diagonal. This should be logged as a tactical success, but engine review still needs to determine whether the attack was sound before White's final mistake.

## Phase 3: Engine Comparison

Engine: Stockfish 18, official Apple Silicon binary.

Engine details: [games/engine-lines/G001-engine.md](/Users/arjun/dev/chess-improvement-pls/games/engine-lines/G001-engine.md)

### Engine Moment 1: 12...a5

Engine preferred moves: 12...bxc5, 12...Nbd7, or 12...Rc8.

Engine eval before my move: about +0.49 to +0.59 with best play.

Engine eval after my move: +1.12.

Eval swing: about +0.6 toward White.

Human explanation:

My suspicion was aimed at the right structure, but the engine points one move earlier than my first guess. 12...a5 was not a tactical blunder, but it committed me to a queenside structure where White's b5-b6 plan became very natural. The problem was not just the move; it was that I played it without consciously pricing the passed-pawn race.

Classification: opening drift, pawn structure, candidate move failure.

Could I realistically have found this in a rapid game? yes.

Thinking habit:

Before a flank pawn move locks or opens a pawn majority, ask: "What is their natural pawn break, and what passed pawn could they create?"

### Engine Moment 2: 13...bxc5

Engine preferred move: 13...axb4.

Engine eval before my move: about +0.26 to +0.51 depending on line.

Engine eval after my move: +0.39.

Eval swing: small; this was not the main mistake.

Human explanation:

My post-game suspicion that 13...bxc5 was the blunder was only partly right. After White played 13.Ba3, 13...bxc5 was playable enough. The cleaner engine idea, 13...axb4, directly removes the advanced b-pawn before it becomes the monster. The larger lesson is that I noticed the right theme but diagnosed it a move late.

Classification: pawn structure, move-order issue.

Could I realistically have found this in a rapid game? yes, if I had asked which White pawn I most needed to stop.

### Engine Moment 3: 16...e4

Engine preferred moves: 16...Rfe8, 16...h5, or 16...Rfd8.

Engine eval before my move: about +1.7 for White.

Engine eval after my move: +2.18.

Eval swing: about +0.4 to +0.5 toward White.

Human explanation:

By move 16, White was already better. 16...e4 gave me attacking dreams, but it did not solve the b-pawn. The engine prefers moves that improve coordination or defensive readiness before trying to race on the kingside.

Classification: strategic model, initiative, defensive resource.

Could I realistically have found this in a rapid game? maybe.

Simpler rule:

When a passed pawn is about to become dangerous, check whether the active move changes the race or only changes the subject.

### Engine Moment 4: 20...Neg4

Engine preferred moves: 20...Re8, 20...Rf8, or 20...Qb7.

Engine eval before my move: about +1.9 for White.

Engine eval after my move: +2.91.

Eval swing: about +1.0 toward White.

Human explanation:

20...Neg4 created a real mating motif, but objectively it looks like a speculative try. It won because White played h3 and allowed Qh2#, not because the attack was fully sound. This is still valuable practical chess, but the lesson should not be "the attack worked"; it should be "I found a tactic after getting strategically worse."

Classification: initiative, tactical resource, practical defense.

Could I realistically have found a more solid move? maybe, but the bigger repair is earlier.

Simpler rule:

Do not let a later opponent blunder retroactively validate the earlier strategic choices.

### Engine Moment 5: 21...Qh2#

Engine confirms mate in 1.

Human explanation:

White's h3 moved the pawn off h2, opened the b8-h2 diagonal, and allowed Qh2#. The knight on g4 covers h2, so the king cannot capture the queen.

Classification: tactical resource.

This was a tactical success.

## Logged Misses

Biggest tactical miss: no major Black tactical miss confirmed; tactical success was finding 21...Qh2#.

Biggest positional or strategic miss: 12...a5 as an unpriced structural commitment that allowed White's natural queenside pawn-majority plan.

Biggest time-usage or decision-process miss: getting pulled into White's fast pace and not stopping at the first queenside structural commitment.

Refined process lesson:

Do not make 2 to 3 automatic moves in a row when there is time on the clock. If the previous move was automatic, force a short stop before the next natural move and ask what obvious reply, pawn break, or structural idea is coming down the pipeline.

## Incidents

Opening incident? yes, see [OPENING_INCIDENTS.md](/Users/arjun/dev/chess-improvement-pls/OPENING_INCIDENTS.md)

Endgame incident? no endgame reached

## Next Game

One focus: Stop automatic move chains at structural moments.

Trigger: I made one automatic-looking move last move and now want to make another natural move.

Question to ask during the next game: What obvious move is coming down the pipeline for my opponent?
