# CODEX_PROMPTS.md

Use these prompts when asking Codex to help review games or maintain this repo.

## No-Engine Review Prompt

```text
Help me complete a no-engine self-review for this rapid game. Do not use engine analysis yet.

I will provide the PGN and my memory of the game. Ask only for information needed to preserve what I believed during the game.

Output:
- immediate self-review
- 3 to 5 candidate critical moments
- my likely thought process
- evaluation guesses to check later
```

## Engine Translation Prompt

```text
Now compare my no-engine review with engine analysis.

For each critical moment:
- give the engine preferred move
- give eval before and after my move
- identify the eval swing
- explain the engine move in human terms
- explain why my move was tempting
- classify the lesson
- say whether this was realistically findable in a rapid game
- extract one transferable rule if useful

Do not treat engine moves as self-explanatory.
```

## Miss Logging Prompt

```text
From this reviewed game, log at most:
- 1 biggest tactical miss
- 1 biggest positional or strategic miss
- 1 biggest time-management or decision-process miss

Use MISS_LOG.md format. Promote to GAP_LOG.md only if the evidence threshold is met.
```

## Five-Game Review Prompt

```text
Review these 5 completed games.

Identify:
- most common miss categories
- highest-severity misses
- repeated positions or structures
- opening incidents
- endgame incidents
- time usage pattern
- one promoted gap, if evidence supports it
- one repair plan for the next 5 games

Do not create more than one active repair focus.
```

## Opening Incident Prompt

```text
Check whether this game creates an opening incident.

Only log one if:
- I fell into a trap
- I was clearly worse by move 10 to 12
- I reached a repeated structure with no plan
- I spent too much time because I did not know the setup
- I misunderstood a common pawn break or piece placement
- my safe move created a passive long-term position

If logged, keep the repair minimal.
```

