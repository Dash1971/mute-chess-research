# Mute Selective: algorithm and evidence

**[Read the illustrated report](REPORT.md)** for the research result, approach, comparison with other projects and future research.

Mute Selective uses a small trained decision-tree forest alongside chess checks. It runs locally in the browser as ordinary JavaScript. Its test on unseen games recognized **774 of 1,234 reference Brilliants**, with **38 false awards across 30,423 other moves**.

## Award rule

1. Both completed engine windows must provide sufficient evidence for a sound move.
2. The position must contain a genuine legal piece offer, accounting for immediate material gains.
3. The trained forest scores the position’s chess features. Both window scores must be at least **0.83**.
4. Required checks must complete; unavailable required evidence withholds the badge.

The forest has **128 trees**, using **75 chess features plus missing-value indicators**. Its score is not a calibrated probability. Stockfish provides engine evidence; the model does not train or change while you play.

## Technical reference and downloads

- [Exact feature definitions, hard gates, code and model](https://github.com/Dash1971/open-brilly-finder/blob/main/studies/brilliant-selective-2026-11-06/README.md)
- [Training and evaluation on unseen games](METHODS.md)
- [Results and source counts](data/selective-update-2026-11-06.json)
- [Combined annotated PGN](https://raw.githubusercontent.com/Dash1971/open-brilly-finder/main/studies/brilliant-selective-2026-11-06/data/seven-accounts-last-12-months-chesscom-brilliants.pgn)
- [Complete research evidence](https://github.com/Dash1971/open-brilly-finder/blob/main/docs/RESEARCH-INDEX.md)

The model SHA-256 is `1a7150fbe52f440922d94d3ae2af337383d63f370b52d0379aeee22d581d056c`. Mobile Maia retains its En Croissant classifier. App release information belongs in the [Mute Chess repository](https://github.com/Dash1971/mute-chess).

[Archived specification for earlier models](HISTORICAL-ALGORITHM.md)
