# Methods and evidence

[Reader report](REPORT.md) · [Algorithm](README.md)

## Data and training

The public collection contains **7,019 games and 8,298 Brilliant annotations** from nelsi, hansen, KNVB, GothamChess, Hikaru, MagnusCarlsen and Witty_Alien. Source galleries are matched to legal moves in official PGNs, preserving full history and clocks. Captured categories remain attached; uncaptured Witty_Alien categories are marked uncategorized.

Mute Selective was trained on **6,293 labeled moves** covering Brilliant examples and ordinary tactics. Whole-game and identical-position groups were kept together during development comparisons. The selected model has 128 trees and a 0.83 per-window cutoff, fixed before the independent-account test.

<a id="november-6-2026-update-frozen-forest-and-fresh-account"></a>

## Test on unseen games

We evaluated **1,000 Witty_Alien games** outside training and model selection. Only that account’s moves are scored. Primary scoring excludes one previously seen positive position, leaving **1,234 reference Brilliants and 30,423 other moves**.

Labels come from the complete captured Brilliant gallery: listed moves are positive, and other own moves within represented games use the gallery-negative convention. Missing PGN annotations alone are not negative evidence. Of 1,235 positive source labels before exclusion, 496 have exact rendered-board/arrow checks and 739 have gallery-link, UUID/ply, mover and legal-PGN identity checks. The latter are not independently board-verified.

The replay uses the native **Stockfish 19 small-network WASM engine**, one thread, 16 MB hash, default Fast depth 12 / 500 ms. Additional confirmation targets depth 14 / 500 ms under the existing six-position allowance per game. Full history and both players’ moves participate in review scheduling; opponents are not scored. These are automated native replays, not browser UI reviews of every game.

| Outcome | Moves |
| --- | ---: |
| Brilliant correctly recognized | 774 |
| Reference Brilliant missed | 460 |
| Other move incorrectly awarded Brilliant | 38 |
| Other move correctly left without Brilliant | 30,385 |

Recognition is **774 / 1,234 = 62.7%**. Badge precision is **774 / 812 = 95.3%**. False-positive rate among other moves is **38 / 30,423 = 0.125%**. These are different measures; the large number of ordinary moves makes overall agreement an unhelpful headline.

## Scope and reproducibility

This is one established player’s gallery-represented games. It does not establish performance for all ratings, games without gallery entries, every device, or every engine/review setting. The model and cutoff stayed fixed throughout evaluation. Detailed sampling decisions, original source grades, exclusions and complete results are retained in [the full methods](https://github.com/Dash1971/open-brilly-finder/blob/main/studies/brilliant-selective-2026-11-06/METHODS.md).

- [Published result record](data/selective-update-2026-11-06.json)
- [Exact model, implementation and reproduction commands](https://github.com/Dash1971/open-brilly-finder/blob/main/studies/brilliant-selective-2026-11-06/README.md)
- [Complete scientific archive](https://github.com/Dash1971/open-brilly-finder/blob/main/studies/brilliant-selective-2026-11-06/SOURCE-MANIFEST.json)
- [Peer comparisons and their separate evaluation settings](https://github.com/Dash1971/open-brilly-finder/blob/main/studies/brilliant-selective-2026-11-06/COMPARISONS.md)

The [archived methods](HISTORICAL-METHODS.md) preserve earlier studies’ test conditions and evidence. Their results are not pooled into the independent-account headline.
