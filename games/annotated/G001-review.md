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

## Source Discipline Note

This review was corrected after the user pointed out that Codex had inferred during-game reasoning from the board. In Phase 2, "My reasoning during the game" and "Line I calculated" should contain only user-reported memory. If a thought was not captured, it is marked as not captured rather than reconstructed.

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

Not recorded. User-reported that White's fast play pulled me into their pace.

Did I ask what my opponent was threatening?

Not explicitly enough. I did not fully ask what White's queenside pawn majority was threatening before committing to the structure.

Note: I accidentally glanced at the eval bar briefly, but turned it off promptly and did not get useful information from it. Treat this review as no-engine.

## Phase 2: Human Critical Moments Before Engine

### Critical Moment 1

Move: 12...a5
Position/FEN: rn3rk1/p1q2pbp/1pp1pnp1/2Pp4/PP1P4/4PN2/2Q1BPPP/R1B2RK1 b - - 0 12
My move: 12...a5
Candidate moves I considered: not clearly remembered; in review, ...bxc5 to clarify the c5 tension looks like the simpler candidate to compare.
Move I would choose now without engine: not definitively chosen. Post-game, the simpler idea to compare was taking on c5 earlier to clear the tension.
Evaluation guess: not provided.
Estimated eval: not provided.

My reasoning during the game:

Not captured. Do not infer this from the board. The user did not explicitly report what 12...a5 was intended to accomplish during the game.

What I missed or was unsure about:

User-reported: I did not fully see that White's b5-b6 plan could become very direct and create a supported passed pawn.

Line I calculated:

Not captured. User-reported that the b5-b6 structure was not really seen or priced before committing.

Post-game interpretation, not during-game memory:

On the board, 12...a5 functioned as a challenge to White's queenside space. The user did not report that as the conscious intention during the game.

### Critical Moment 2

Move: 13...bxc5
Position/FEN: rn3rk1/2q2pbp/1pp1pnp1/p1Pp4/PP1P4/B3PN2/2Q1BPPP/R4RK1 b - - 1 13
My move: 13...bxc5
Candidate moves I considered: not clearly remembered.
Move I would choose now without engine: not definitively chosen. Post-game suspicion was that this was the main mistake, though the earlier 12...a5 commitment also needed checking.
Evaluation guess: not provided.
Estimated eval: not provided.

My reasoning during the game:

Not captured. Do not infer this from the board.

What I missed or was unsure about:

User-reported: I missed that White's very obvious-in-hindsight play was b5-b6, breaking through and creating a supported passed pawn.

Line I calculated:

Not captured. User-reported that the supported passed pawn appeared suddenly and felt scary.

Post-game interpretation, not during-game memory:

The engine later showed that 13...bxc5 was not the main issue. This should not be backfilled as something the user knew during the game.

### Critical Moment 3

Move: 16...e4 after 16.b5
Position/FEN: r4rk1/2qn1pbp/2p2np1/pPPpp3/P7/B3PN2/2Q1BPPP/2R2RK1 b - - 0 16
My move: 16...e4
Candidate moves I considered: not captured beyond the general queen-and-knight counterplay idea.
Move I would choose now without engine: not provided.
Evaluation guess: not provided.
Estimated eval: not provided.

My reasoning during the game:

User-reported: I tried to create counterplay with my knights on White's kingside, coordinating with my queen on b8.

What I missed or was unsure about:

Not captured as a during-game thought. Post-game, the strategic question to check was whether this counterplay compensated for the b6 passer.

Line I calculated:

Not captured beyond the general queen-and-knight counterplay idea.

### Critical Moment 4

Move: 20...Neg4
Position/FEN: rqr3k1/5pbp/1Pp2np1/p1Ppn3/P2Np3/1Q2P3/1B2BPPP/2R2RK1 b - - 6 20
My move: 20...Neg4
Candidate moves I considered: not captured beyond the general queen-and-knight counterplay idea.
Move I would choose now without engine: not provided.
Evaluation guess: not provided.
Estimated eval: not provided.

My reasoning during the game:

User-reported: I was trying to create counterplay with my knights on the kingside and queen on b8. I did not expect White to fall for the mate in one.

What I missed or was unsure about:

Not captured as a during-game thought. Post-game, the thing to check was whether the attack was sound or whether White simply walked into it.

Line I calculated:

User-reported expected line: 21.Bxg4 Nxg4 22.g3, blocking the obvious mate in one, and then 22...h5 with the vague plan of ...h4 to generate kingside counterplay.

### Final Tactical Moment

Move: 21...Qh2#
Position/FEN before move: rqr3k1/5pbp/1Pp2np1/p1Pp4/P2Np1n1/1Q2P2P/1B2BPP1/2R2RK1 b - - 0 21
My move: 21...Qh2#

Human note:

White's h3 opened h2 and allowed the queen to finish the b8-h2 diagonal. This should be logged as a tactical success, but not as the expected outcome of the attack. The user expected White to block the mate and then planned vague kingside counterplay with ...h5 and ...h4.

## Post-Engine Added Critical Moment

This moment was not identified in the no-engine pass. It was added after the user reviewed the engine output.

### Added Moment: 14...Nbd7

Move: 14...Nbd7
Position/FEN: rn3rk1/2q2pbp/2p1pnp1/p1Pp4/PP6/B3PN2/2Q1BPPP/R4RK1 b - - 0 14
My move: 14...Nbd7
Candidate moves I considered: not captured.
Move to remember after engine review: 14...axb4.
Evaluation guess before engine: not provided.
Estimated eval before engine: not provided.

My reasoning during the game:

User-reported after engine review: I did not see or recognize the b4-b5 threat, so I tried to activate my knight.

What I missed or was unsure about:

User-reported after engine review: the biggest issue was a pawn. With many pieces on the board, I forgot that White's b-pawn was the concrete problem.

Line I calculated:

Not captured.

Post-engine interpretation:

14...Nbd7 develops a piece, but it lets White play b5 and make the b-pawn a major problem. 14...axb4 removes the pawn while it is still removable.

## Phase 3: Engine Comparison

Engine: Stockfish 18, official Apple Silicon binary.

Engine details: [games/engine-lines/G001-engine.md](/Users/arjun/dev/chess-improvement-pls/games/engine-lines/G001-engine.md)

### Engine Moment 1: 12...a5

Engine preferred moves: 12...bxc5, 12...Nbd7, or 12...Rc8.

Engine eval before my move: about +0.49 to +0.59 with best play.

Engine eval after my move: +1.12.

Eval swing: about +0.6 toward White.

Human explanation:

12...a5 was an early structural warning, not the concrete confirmed miss. It challenged White's b-pawn, which meant that pawn had to stay in my attention. The later problem was that I switched into routine piece development with 14...Nbd7 while the b-pawn could still advance.

Classification: opening drift, pawn structure, candidate move failure.

Could I realistically have found this in a rapid game? yes.

Thinking habit:

After a pawn move creates contact with an advanced enemy pawn, keep asking whether that pawn is still the main issue.

### Engine Moment 2: 13...bxc5

Engine preferred move: 13...axb4.

Engine eval before my move: about +0.26 to +0.51 depending on line.

Engine eval after my move: +0.39.

Eval swing: small; this was not the main mistake.

Human explanation:

My post-game suspicion that 13...bxc5 was the blunder was only partly right. After White played 13.Ba3, 13...bxc5 was playable enough. The cleaner engine idea, 13...axb4, directly removes the advanced b-pawn before it becomes the monster. The larger lesson is that I noticed the right theme but diagnosed it a move late.

Classification: pawn structure, move-order issue.

Could I realistically have found this in a rapid game? yes, if I had asked which White pawn I most needed to stop.

### Engine Moment 3: 14...Nbd7

Engine preferred move: 14...axb4.

Engine eval before my move: -0.28 with 14...axb4.

Engine eval after my move: +1.82.

Eval swing: about +2.1 toward White.

Human explanation:

This is the concrete mistake the engine flagged and the user identified after review. I activated a knight with 14...Nbd7 while the biggest problem was White's b-pawn. If Black plays 14...axb4, the b4-b5 threat is removed before it becomes a major migraine.

Classification: threat blindness, candidate move failure, pawn-structure evaluation, board vision.

Could I realistically have found this in a rapid game? yes.

Thinking habit:

Before activating a piece, ask: "Is there a pawn move coming next that changes the whole position?"

### Engine Moment 4: 16...e4

Engine preferred moves: 16...Rfe8, 16...h5, or 16...Rfd8.

Engine eval before my move: about +1.7 for White.

Engine eval after my move: +2.18.

Eval swing: about +0.4 to +0.5 toward White.

Human explanation:

By move 16, White was already better. 16...e4 created attacking chances, but it did not solve the b-pawn. The engine prefers moves that improve coordination or defensive readiness before trying to race on the kingside.

Classification: strategic model, initiative, defensive resource.

Could I realistically have found this in a rapid game? maybe.

Simpler rule:

When a passed pawn is about to become dangerous, check whether the active move changes the race or only changes the subject.

### Engine Moment 5: 20...Neg4

Engine preferred moves: 20...Re8, 20...Rf8, or 20...Qb7.

Engine eval before my move: about +1.9 for White.

Engine eval after my move: +2.91.

Eval swing: about +1.0 toward White.

Human explanation:

20...Neg4 created a real mating motif, but objectively it looks like a speculative try. The user did not expect White to fall for mate in one; the expected line was 21.Bxg4 Nxg4 22.g3, after which Black would try 22...h5 and ...h4 for vague kingside counterplay. The game ended immediately because White played h3 and allowed Qh2#.

Classification: initiative, tactical resource, practical defense.

Could I realistically have found a more solid move? maybe, but the bigger repair is earlier.

Simpler rule:

Do not let a later opponent blunder retroactively validate the earlier strategic choices.

### Engine Moment 6: 21...Qh2#

Engine confirms mate in 1.

Human explanation:

White's h3 moved the pawn off h2, opened the b8-h2 diagonal, and allowed Qh2#. The knight on g4 covers h2, so the king cannot capture the queen.

Classification: tactical resource.

This was a tactical success.

## Logged Misses

Biggest tactical miss: no major Black tactical miss confirmed; tactical success was finding 21...Qh2#.

Biggest positional or strategic miss: 14...Nbd7, activating a knight while missing that White's b4-b5 pawn move was the biggest concrete threat.

Biggest time-usage or decision-process miss: getting pulled into White's fast pace and not stopping before 14...Nbd7 to ask what White's b-pawn was threatening.

Refined process lesson:

Do not make 2 to 3 automatic moves in a row when there is time on the clock. If the previous move was automatic, force a short stop before the next natural move and ask what obvious reply, pawn break, or structural idea is coming down the pipeline. In G001, the missed obvious move was the pawn move b4-b5.

## Incidents

Opening incident? yes, see [OPENING_INCIDENTS.md](/Users/arjun/dev/chess-improvement-pls/OPENING_INCIDENTS.md)

Endgame incident? no endgame reached

## Next Game

One focus: Stop automatic move chains and identify the biggest pawn threat before activating pieces.

Trigger: I want to develop or activate a piece while an opponent pawn can advance and change the structure.

Question to ask during the next game: What pawn move is coming down the pipeline, and does it matter more than my piece activity?
