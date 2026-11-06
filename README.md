# Mute Chess research

Readable studies, visual explanations and the evidence behind Mute Chess's design decisions.

## Brilliant moves: more genuine ideas, fewer undeserved badges

![New Selective recognizes more Brilliants and gives fewer wrong awards on 1,000 fresh-account games.](studies/brilliant-moves/figures/selective-update-2026-11-06.png)

**[Read: Making Brilliant badges feel at home on Mute Chess →](studies/brilliant-moves/REPORT.md#november-6-2026-addendum-more-brilliants-fewer-wrong-badges)**

Our November 6 recommendation is **New Selective with PR285’s complete-window confirmation fix**. In 1,000 fresh-account games, it recognized **774 of 1,234 reference Brilliants** and gave **38 wrong awards among 30,423 non-Brilliant moves**. Compared with the older model using the same fix, that is **49 more genuine Brilliants and 20 fewer wrong badges**, about a 34% reduction in wrong awards.

We trained the updated forest on more labeled examples and improved its tree settings, then froze it before this test. Your browser runs the decision trees locally alongside Stockfish and the basic chess checks. It does not use a neural network or remote classification call, and it does not learn during play. **The new recommendation is not yet deployed.**

The report preserves the earlier En Croissant comparison and adds the new SF19 Fast results separately. The fresh test covers one account’s gallery-represented games; it does not establish accuracy for every player. Our next priority is more coverage while keeping wrong awards low.

[Reader addendum](studies/brilliant-moves/REPORT.md#november-6-2026-addendum-more-brilliants-fewer-wrong-badges) · [Methods and limits](studies/brilliant-moves/METHODS.md#november-6-2026-update-frozen-forest-and-fresh-account) · [Result counts](studies/brilliant-moves/data/selective-update-2026-11-06.json)

## Elo seeding: giving human-like opponents useful starting ratings

![From reference ratings through measured games to a varied opponent pool.](studies/elo-seeding/bot-rating-establishment-2026-10-31/figures/reader-cover.png)

**[Read the illustrated Elo report →](studies/elo-seeding/REPORT.md)** · **[How the 10,000-opponent catalog is assigned →](studies/elo-seeding/CATALOG-METHOD.md)**

Two historical studies contain **3,449 rated games**, reference-policy establishment and the method behind the initial catalog. Maia's conditioning input is distinct from a measured playing rating. New identities reuse estimates for matching measured policies; Glicko-2 then updates their ratings through play.

The complete study directories were copied byte for byte from [mobile-maia-research at 140e2eb](https://github.com/Dash1971/mobile-maia-research/tree/140e2eb411923930fb0d5950b92abf6f3c0166dd). Reader copies adapt links for this repository. [Transfer provenance](SOURCE-PROVENANCE.json) records every archived source blob and SHA-256 digest. Their deployment descriptions describe the original study date, not a fresh audit of the live service.

## Evidence and attribution

Each study separates observations, interpretations and recommendations. Public game records, source pins, limitations and reproduction material accompany the reports. No authenticated session data or raw cookie-bearing response metadata is published.

The original [AGPL-3.0-only license](LICENSE) is retained for the copied research. Third-party code and visual evidence retain their own attribution and licensing; see the brilliant study's [reference notes](studies/brilliant-moves/reference/README.md). Reports and preparation used OpenAI Codex assistance. This repository is independent of Chess.com, Lichess and En Croissant.
