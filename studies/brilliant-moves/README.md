# Brilliant moves: study and evidence

**[Read the illustrated report →](REPORT.md)** · [Exact methods](METHODS.md) · [Reproduce the rules](reference/README.md)

The benchmark contains **618 moves from 299 games**, with 309 observed Chess.com Brilliants and 309 explicitly non-Brilliant moves. The headline compares direct En Croissant annotation with Mute's confirmation-aware material-guard candidate on identical engine evidence. The methods also report the more generous Mute comparator and independently reserved games.

| Evidence | Contents |
| --- | --- |
| [moves.csv](moves.csv) / [moves.json](moves.json) | Labels, game/move identity, source links, positions, ratings and every classifier outcome |
| [SUMMARY.json](SUMMARY.json) | Combined, fixed-policy prospective, reserved-game and account results; label/position audits |
| [primary-moves.json](primary-moves.json) | Primary selected labels and observation keys |
| [observations-export.json](observations-export.json) | 963 active primary and secondary gallery/review observations, with capture times and coach-text completeness |
| [corpus.sqlite3](corpus.sqlite3) | Publication-filtered games, positions and 992 observation records (including superseded metadata) |
| [selected-games.pgn](selected-games.pgn) / [provenance](public-pgn-provenance.json) | All 299 primary games, with source and content hashes |
| [analysis-baseline.json](analysis-baseline.json) | 1,775 saved baseline position windows, scores and material inputs |
| [comparison-v2.json](comparison-v2.json) / [comparison-v3.json](comparison-v3.json) | Actual pinned-rule replay, provisional versus confirmed awards and gate diagnostics |
| [analysis-stronger.json](analysis-stronger.json) / [sensitivity summary](sensitivity-summary.json) | 178 stronger windows for 60 frozen targeted disagreements; distinct from baseline totals |
| [Stronger v2 replay](comparison-v2-stronger.json) / [v3 replay](comparison-v3-stronger.json) | Standalone stronger decisions and independent confirmation of baseline decisions |
| [Selection plan](PLAN.json), [cohort freeze](COHORT-FREEZE.json), [candidate freeze](FINAL-CANDIDATE-FREEZE.json), [manifest](manifest.json) | Sampling, prospective assignment, source/session provenance and validation boundaries |
| [reference/](reference/README.md) | Pinned source copies, hashes, source credits and licenses |
| [Publication manifest](PUBLICATION-MANIFEST.json) | SHA-256 for each published study artifact |

`source_cohort` and `original_split` preserve provenance. Use the final `split` and the validation hygiene in `SUMMARY.json` for current results. Prospective and reserved results are subsets of the 618 moves, not additional cases. Secondary captures do not add benchmark cases; absent gallery membership is never a negative label. Supplemental visual reference combinations are excluded from benchmark totals.
