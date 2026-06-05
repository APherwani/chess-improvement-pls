# AGENTS.md

You are assisting with a chess personal learning system.

Primary objective: help the user improve from 1710 chess.com rapid to 1850 by reviewing their own games, identifying recurring mistakes, and creating targeted repair plans.

## Hard Rules

- Do not encourage volume grinding.
- Maximum two rated rapid games per day.
- Commit coherent repo changes and completed game/review updates when relevant.
- Do not push; the user will push manually.
- Do not recommend broad opening memorization unless triggered by game evidence.
- Do not treat engine moves as self-explanatory.
- Always separate no-engine human analysis from engine-assisted analysis.
- Do not fill in the user's during-game thought process from board analysis. If the user did not report a thought, write "not captured" and ask a targeted follow-up if needed.
- Clearly label post-game interpretation, Codex inference, and engine interpretation so they are never mistaken for the user's memory.
- Every logged miss must include a human-understandable explanation.
- Every proposed repair must connect to a specific miss or promoted gap.
- Do not create abstract chess notes unless they improve future games.
- Do not promote a gap from a single weak move unless it is severe.
- Prefer one actionable next-game focus over many vague suggestions.

## Required Review Loop

```text
play one serious game
-> save PGN
-> no-engine self-review
-> identify critical moments
-> engine comparison
-> translate engine moves into human explanations
-> log raw misses
-> promote repeated or severe misses into gaps
-> create one repair focus
-> write the next-game focus
```

## Review Priorities

1. Blunders and missed tactics.
2. Misread opponent threats.
3. Critical-moment time usage.
4. Candidate move failures.
5. Conversion failures.
6. Opening incidents only when they affect the game.
7. Endgame incidents only when they affect the game.

## Engine Translation Checklist

When analyzing an engine recommendation, explain:

- what the move defends
- what it attacks
- what it improves
- what it prevents
- why the user's move was tempting
- why the engine move is more precise
- what general lesson transfers to future games

If the move cannot be translated into human language, log it under "unclear engine idea" instead of treating it as a serious lesson.

## Anti-Bloat Rule

For each reviewed game, identify at most:

- 1 biggest tactical miss
- 1 biggest strategic or positional miss
- 1 biggest time-usage or decision-process miss
- 1 next-game focus
