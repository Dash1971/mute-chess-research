"""One fixed report figure from published fresh-account counts; no fitting."""
import json
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', '/private/tmp/mute-research-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT/'data/selective-update-2026-11-06.json').read_text())
KEYS = ['production', 'pr285', 'selective']
LABELS = ['Existing production', 'Older model + context fix', 'Updated Mute Selective']
INK, MOSS, GOLD, PALE = '#172723', '#668478', '#D9B25F', '#EDF1EA'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'svg.fonttype': 'none'})
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2), dpi=130)
fig.suptitle('More genuine Brilliants. Fewer wrong badges.', x=.03, y=.97,
             ha='left', color=INK, fontsize=21, weight='bold')
fig.text(.03, .88, '1,000 fresh-account games · Witty_Alien · same SF19 Fast analysis', color=INK)
for ax, field, title, limit, color, denominator in zip(axes, ['TP', 'FP'],
        ['Brilliants recognized — higher is better', 'Wrong awards — lower is better'],
        [1234, 70], [MOSS, GOLD], [1234, 30423]):
    values = [DATA['metrics'][key][field] for key in KEYS]
    ax.barh(range(3), values, color=[color, color, INK], height=.52)
    for i, value in enumerate(values):
        ax.text(value + limit*.015, i, f'{value:,}', va='center', color=INK, weight='bold', fontsize=14)
    ax.set_yticks(range(3), labels=LABELS if field == 'TP' else ['', '', ''])
    ax.set_ylim(2.7, -.7)
    ax.set_xlim(0, limit)
    ax.set_title(title, loc='left', fontsize=13, color=INK, pad=16)
    ax.set_xlabel(f'Out of {denominator:,} '+('reference Brilliants' if field == 'TP' else 'non-Brilliant moves'), color=INK)
    ax.tick_params(length=0, labelcolor=INK)
    ax.grid(axis='x', color=PALE)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
fig.text(.03, .09, 'With the same complete confirmation: 49 more genuine awards, 20 fewer wrong awards.',
         color=INK, weight='bold', fontsize=13)
fig.text(.03, .025, 'Panels use different scales. One account, gallery-represented games; see Methods for labels and limits.',
         color=INK, fontsize=10)
fig.subplots_adjust(left=.21, right=.98, top=.71, bottom=.25, wspace=.22)
for ext in ['png', 'svg']:
    fig.savefig(ROOT/f'figures/selective-update-2026-11-06.{ext}', facecolor='white')
plt.close(fig)
