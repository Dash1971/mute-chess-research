# Mute Chess research

Readable studies, visual explanations and the evidence behind Mute Chess's design decisions.

## Brilliant moves: making good chess feel rewarding

![A small pilot compares En Croissant and Mute with observed Chess.com labels.](studies/brilliant-moves-pilot-2026-11-03/figures/rule-comparison.png)

**[Read the illustrated brilliant-moves pilot →](studies/brilliant-moves-pilot-2026-11-03/REPORT.md)**

On November 3, 2026 we captured 20 gallery brilliants and 20 separate, explicitly reviewed controls across five Chess.com accounts. The 40 moves came from 19 games. Current Game Review displays confirmed 19 brilliants and 21 non-brilliants: one historical gallery entry now displayed Best.

With fixed local engine evidence, Mute's existing v2 rules awarded **17/19** of those current brilliants, versus **6/19** for the pinned En Croissant rules. Mute also awarded **1/21** sampled non-brilliants; En Croissant awarded **0/21**. These are selected pilot counts, not population accuracy estimates.

Mute v2 rewards near-best, sound, legally capturable piece offers. It credits material already won, rejects an evaluated safe alternative worth at least +6 pawns, and requires corroborating engine evidence. The report explains the [exact rules and score mapping](studies/brilliant-moves-pilot-2026-11-03/REPORT.md#the-rules-we-actually-compared), the mismatches and the limitations. Chess.com's complete formula remains unpublished. This pilot changed no application rules; Mobile Maia was left unchanged.

**[Follow-up: the pawn-winning false positive →](studies/brilliant-moves-followup-2026-11-03/README.md)** Current Chess.com review calls the reported Ndxe5 **Excellent**. Two simple material filters reject it, but also remove four confirmed pilot brilliants. A closely related GothamChess pawn-winning combination illustrates why we recommend a focused second sample before changing the classifier.

## Elo seeding: giving human-like opponents useful starting ratings

![From reference ratings through measured games to a varied opponent pool.](studies/elo-seeding/bot-rating-establishment-2026-10-31/figures/reader-cover.png)

**[Read the illustrated Elo report →](studies/elo-seeding/REPORT.md)** · **[How the 10,000-opponent catalog is assigned →](studies/elo-seeding/CATALOG-METHOD.md)**

Two historical studies contain **3,449 rated games**, reference-policy establishment and the method behind the initial catalog. Maia's conditioning input is distinct from a measured playing rating. New identities reuse estimates for matching measured policies; Glicko-2 then updates their ratings through play.

The complete study directories were copied byte for byte from [mobile-maia-research at 140e2eb](https://github.com/Dash1971/mobile-maia-research/tree/140e2eb411923930fb0d5950b92abf6f3c0166dd). Reader copies adapt links for this repository. [Transfer provenance](SOURCE-PROVENANCE.json) records every archived source blob and SHA-256 digest. Their deployment descriptions describe the original study date, not a fresh audit of the live service.

## Evidence and attribution

Each study separates observations, interpretations and recommendations. Public game records, source pins, limitations and reproduction material accompany the reports. No authenticated session data or raw cookie-bearing response metadata is published.

The original [AGPL-3.0-only license](LICENSE) is retained for the copied research. Third-party code and visual evidence retain their own attribution and licensing; see the brilliant study's [reference notes](studies/brilliant-moves-pilot-2026-11-03/reference/README.md). Reports and preparation used OpenAI Codex assistance. This repository is independent of Chess.com, Lichess and En Croissant.
