# Mute Chess research

Readable studies, visual explanations and the evidence behind Mute Chess's design decisions.

## Brilliant moves: a Chess.com-like experience with open rules

![Mute Chess and En Croissant compared on the studied examples.](studies/brilliant-moves/figures/history-recovery-replay.png)

**[Read: Making Brilliant badges feel at home on Mute Chess →](studies/brilliant-moves/REPORT.md)**

The **Mute History Rule** is our closest-matching tested heuristic, but the merge is on hold. Across **1,248 studied moves from 654 games**, it recognizes **478 of 613 Chess.com Brilliants**, compared with En Croissant’s 166. Overall agreement is **86.4% versus 63.4%**. Mute also gives more extra awards: **35 of 635 comparison moves versus 10**. The report explains the tradeoff through quiet sacrifices, repeated offers and ordinary material recovery.

**Fresh-game testing found 78/100 Brilliants and 13/100 extra awards, versus En Croissant’s 27 and 1. That false-award rate is too high: hold the merge and keep the PR in draft.** The material guard changed no fresh decisions; its generalization is unproven. Mobile Maia keeps its existing En Croissant-based classifier.

[Exact rules](studies/brilliant-moves/README.md) · [Methods and validation](studies/brilliant-moves/METHODS.md) · [Move-level evidence](studies/brilliant-moves/data/combined-history-moves.csv)

## Elo seeding: giving human-like opponents useful starting ratings

![From reference ratings through measured games to a varied opponent pool.](studies/elo-seeding/bot-rating-establishment-2026-10-31/figures/reader-cover.png)

**[Read the illustrated Elo report →](studies/elo-seeding/REPORT.md)** · **[How the 10,000-opponent catalog is assigned →](studies/elo-seeding/CATALOG-METHOD.md)**

Two historical studies contain **3,449 rated games**, reference-policy establishment and the method behind the initial catalog. Maia's conditioning input is distinct from a measured playing rating. New identities reuse estimates for matching measured policies; Glicko-2 then updates their ratings through play.

The complete study directories were copied byte for byte from [mobile-maia-research at 140e2eb](https://github.com/Dash1971/mobile-maia-research/tree/140e2eb411923930fb0d5950b92abf6f3c0166dd). Reader copies adapt links for this repository. [Transfer provenance](SOURCE-PROVENANCE.json) records every archived source blob and SHA-256 digest. Their deployment descriptions describe the original study date, not a fresh audit of the live service.

## Evidence and attribution

Each study separates observations, interpretations and recommendations. Public game records, source pins, limitations and reproduction material accompany the reports. No authenticated session data or raw cookie-bearing response metadata is published.

The original [AGPL-3.0-only license](LICENSE) is retained for the copied research. Third-party code and visual evidence retain their own attribution and licensing; see the brilliant study's [reference notes](studies/brilliant-moves/reference/README.md). Reports and preparation used OpenAI Codex assistance. This repository is independent of Chess.com, Lichess and En Croissant.
