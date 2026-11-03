# Making Brilliant badges feel at home on Mute Chess

Chess.com’s Brilliant badge makes a good chess idea feel special. Our goal is to bring that experience to an open chess platform: celebrate sound sacrifices, including quiet ones, with rules that anyone can inspect.

**We recommend adopting the Mute History Rule.** It recognizes substantially more of the studied Chess.com Brilliants than our En Croissant starting point, while checking for repeated offers and ordinary material recovery.

## What we studied

We examined **1,048 labeled moves from 545 games** played by nelsi, hansen, KNVB, GothamChess and Hikaru. Each move has a recorded Chess.com classification, its full game history and engine analysis. We compared our rule with En Croissant on the same positions and analysis.

Chess.com does not publish its complete formula. Its [guidance](https://support.chess.com/en/articles/8572705-how-are-moves-classified-what-is-a-blunder-or-brilliant-etc) describes good piece sacrifices, position conditions and player-strength considerations. We used those published ideas and the observed moves to build an understandable Mute policy.

## The rules we chose

- **Keep the move sound.** Current and previous completed engine checks must both support its quality.
- **Look for a real piece offer.** The offered piece can be somewhere other than the piece that moved.
- **Check the position’s context.** An already-converted position with a safe winning alternative should not receive an automatic sacrifice badge.
- **Remember earlier offers.** A quiet follow-up should not earn another badge merely because the same sacrifice remains available; a new tactical idea can make the difference.
- **Account for ordinary recovery.** Some apparent offers simply recover material elsewhere. A narrow check covers legal defenses before withholding those badges.

## Quiet moves can be Brilliant

![A quiet bishop retreat leaves a rook available.](visuals/outputs/quiet-offer-bg2.gif)

[Hikaru’s 27.Bg2](https://www.chess.com/analysis/game/live/186567991235/review?move=52) retreats a bishop while leaving a rook available. Chess.com and Mute both recognize the idea. The illustrated **...Bxb1 Rxb1** continuation trades a rook for a bishop; these replies are conditional, not claimed forced or played.

## An apparent sacrifice can be an ordinary trade

![After hxg6, a queen check enables recovery on another square.](visuals/outputs/routine-hxg6.gif)

After [18...hxg6](https://www.chess.com/analysis/game/live/171488501692/review?move=35), **Bxc4 Qc5+** lets Black recover the bishop after every legal defense. The animation shows one such continuation. Black trades a knight for a bishop and finishes a pawn ahead. Chess.com calls hxg6 Best, and Mute withholds Brilliant. The [rook-recovery example](visuals/outputs/routine-hxg5.gif) shows a similar distinction.

## How closely do the badges match?

![Mute Chess and En Croissant compared with Chess.com on the studied examples.](figures/history-recovery-replay.png)

| On the studied examples | Mute Chess | En Croissant |
| --- | ---: | ---: |
| Chess.com Brilliants recognized | **400 / 513** | 139 / 513 |
| Extra awards on non-Brilliant moves | **22 / 535** | 9 / 535 |
| Overall agreement | **87.1%** | 63.5% |

Mute recognizes about **2.9 times as many Brilliants**, with more extra awards. That is the explicit tradeoff behind our recommendation: make more worthwhile ideas visible, using documented rules rather than treating every temporary offer as special.

**These results describe the studied examples; fresh-game testing is underway before release.**

Adopt the History Rule for Mute Chess. Keep the [exact algorithm](README.md), [sampling and validation methods](METHODS.md), and move-level evidence open. Mobile Maia keeps its existing En Croissant-based classifier.
