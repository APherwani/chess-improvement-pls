# TRANSFERABLE_SKILL_METHOD.md

This repo uses a transferable learning loop:

```text
trace -> miss -> pattern -> gap -> repair -> test
```

## Trace

Chess gives a full behavioral trace:

- moves played
- time spent
- positions reached
- plans noticed
- threats missed
- evaluations guessed
- engine comparison

## Miss

A miss is a concrete failure in one position.

Good miss:

```text
On move 24 I missed Be1, a quiet defensive move that defended g3 while keeping the rook active.
```

Weak miss:

```text
I played badly.
```

## Pattern

A pattern is a repeated kind of miss.

Example:

```text
I search active moves and direct recaptures, but under-search quiet defensive moves that improve coordination.
```

## Gap

A gap is a pattern that has enough evidence to deserve targeted repair.

Do not promote single ordinary mistakes.

## Repair

A repair is a behavior to test in future games.

Good repair:

```text
In tense positions where the opponent has a threat, consider one quiet defensive candidate before choosing an active move.
```

Weak repair:

```text
Study tactics more.
```

## Test

Each repair needs a next-cycle test.

Example:

```text
In the next 5 games, mark every critical position where the opponent has a threat and record whether I considered one quiet defensive candidate.
```

