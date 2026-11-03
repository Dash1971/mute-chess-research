# Mute Chess research

Readable studies, visual explanations and the evidence behind Mute Chess's design decisions.

## Brilliant moves: History Rule with a material-recovery guard

![The refined History Rule on the reviewed development corpus.](studies/brilliant-moves/figures/history-recovery-replay.png)

**[Read: Adopt the Mute History Rule—with a material-recovery guard →](studies/brilliant-moves/REPORT.md)**

We recommend the **Mute History Rule with a narrow material-recovery guard**. In the 1,048-move development replay it retains **all 400 previously matched Chess.com Brilliants** and removes exactly two extra awards; **22 extras and 113 misses remain**. The guard was designed using these positions and labels: **it has no new unseen validation yet**.

The preserved independent 200-move test of the **unrefined** History Rule recognized 78/100 Brilliants with 5 extra awards, 86.5% agreement and 94.0% sample badge precision. The refined 78/3 result on that same subset is retrospective reuse, **not a revised untouched test score**. The full corpus covers 545 games; comparison models and original evidence remain inspectable.

Two native-board illustrations show why ordinary hxg6/hxg5 recoveries are now withheld while all 400 previously matched awards remain. This does not guarantee that no future Brilliant will be lost. **Adoption is recommended, not claimed deployed. Native SF19 and variable browser budgets remain unvalidated. Mobile Maia stays unchanged.**

[Exact rules](studies/brilliant-moves/README.md) · [Methods and evidence roles](studies/brilliant-moves/METHODS.md) · [Refinement outcomes](studies/brilliant-moves/data/history-recovery-results.json) · [Original move-level evidence](studies/brilliant-moves/moves.csv) · [Earlier 618-move report](https://github.com/Dash1971/mute-chess-research/blob/c6969d1/studies/brilliant-moves/REPORT.md)

## Elo seeding: giving human-like opponents useful starting ratings

![From reference ratings through measured games to a varied opponent pool.](studies/elo-seeding/bot-rating-establishment-2026-10-31/figures/reader-cover.png)

**[Read the illustrated Elo report →](studies/elo-seeding/REPORT.md)** · **[How the 10,000-opponent catalog is assigned →](studies/elo-seeding/CATALOG-METHOD.md)**

Two historical studies contain **3,449 rated games**, reference-policy establishment and the method behind the initial catalog. Maia's conditioning input is distinct from a measured playing rating. New identities reuse estimates for matching measured policies; Glicko-2 then updates their ratings through play.

The complete study directories were copied byte for byte from [mobile-maia-research at 140e2eb](https://github.com/Dash1971/mobile-maia-research/tree/140e2eb411923930fb0d5950b92abf6f3c0166dd). Reader copies adapt links for this repository. [Transfer provenance](SOURCE-PROVENANCE.json) records every archived source blob and SHA-256 digest. Their deployment descriptions describe the original study date, not a fresh audit of the live service.

## Evidence and attribution

Each study separates observations, interpretations and recommendations. Public game records, source pins, limitations and reproduction material accompany the reports. No authenticated session data or raw cookie-bearing response metadata is published.

The original [AGPL-3.0-only license](LICENSE) is retained for the copied research. Third-party code and visual evidence retain their own attribution and licensing; see the brilliant study's [reference notes](studies/brilliant-moves/reference/README.md). Reports and preparation used OpenAI Codex assistance. This repository is independent of Chess.com, Lichess and En Croissant.

## Archived studies

The [feasibility study](studies/brilliant-moves-pilot-2026-11-03/REPORT.md), [tactical reference positions](studies/brilliant-moves-followup-2026-11-03/README.md) and [development-reference release](studies/brilliant-moves-2026-11-03/REPORT.md) remain available with their original denominators. Use the unified report above for the complete current comparison.
