# Mute Chess research

Readable studies, visual explanations and the evidence behind Mute Chess's design decisions.

## Chess.com-style Brilliant moves on an open platform

![Mute Selective recognizes 62.7% of reference Brilliants; 95.3% of its awarded badges match Chess.com.](studies/brilliant-moves/figures/selective-update-2026-11-06.png)

**[Read the illustrated report →](studies/brilliant-moves/REPORT.md)**

Our research produced **Mute Selective**, a small trained model combined with checks for move quality and a real piece offer. It runs locally in the browser. On 1,000 games from an account excluded from training, it recognized **774 of 1,234 Chess.com Brilliants (62.7%)**. Of its 812 awarded badges, **774 matched Chess.com (95.3%)**.

The report explains the approach, its relationship to En Croissant and other open classifiers, the evidence behind the result, and how we plan to recognize more genuine Brilliants while keeping false awards low.

[Methods](studies/brilliant-moves/METHODS.md) · [Algorithm and code](studies/brilliant-moves/README.md) · [Open Brilly Finder](https://github.com/Dash1971/open-brilly-finder) · [Download the annotated games](https://raw.githubusercontent.com/Dash1971/open-brilly-finder/main/studies/brilliant-selective-2026-11-06/data/seven-accounts-last-12-months-chesscom-brilliants.pgn)

## Elo seeding: giving human-like opponents useful starting ratings

![From reference ratings through measured games to a varied opponent pool.](studies/elo-seeding/bot-rating-establishment-2026-10-31/figures/reader-cover.png)

**[Read the illustrated Elo report →](studies/elo-seeding/REPORT.md)** · **[How the 10,000-opponent catalog is assigned →](studies/elo-seeding/CATALOG-METHOD.md)**

Two historical studies contain **3,449 rated games**, reference-policy establishment and the method behind the initial catalog. Maia's conditioning input is distinct from a measured playing rating. New identities reuse estimates for matching measured policies; Glicko-2 then updates their ratings through play.

The complete study directories were copied byte for byte from [mobile-maia-research at 140e2eb](https://github.com/Dash1971/mobile-maia-research/tree/140e2eb411923930fb0d5950b92abf6f3c0166dd). Reader copies adapt links for this repository. [Transfer provenance](SOURCE-PROVENANCE.json) records every archived source blob and SHA-256 digest. Their deployment descriptions describe the original study date, not a fresh audit of the live service.

## Evidence and attribution

Each study separates observations, interpretations and recommendations. Public game records, source pins, limitations and reproduction material accompany the reports. No authenticated session data or raw cookie-bearing response metadata is published.

The original [AGPL-3.0-only license](LICENSE) is retained for the copied research. Third-party code and visual evidence retain their own attribution and licensing; see the brilliant study's [reference notes](studies/brilliant-moves/reference/README.md). Reports and preparation used OpenAI Codex assistance. This repository is independent of Chess.com, Lichess and En Croissant.
