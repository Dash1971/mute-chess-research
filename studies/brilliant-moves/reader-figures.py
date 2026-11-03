#!/usr/bin/env python3
"""Two study-specific panels from the completed frozen test; no fitting/searches."""
from pathlib import Path
import hashlib,json,sys,os
os.environ.setdefault('MPLCONFIGDIR','/private/tmp/mute-research-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'data/test-results.json'
COLORS={'moss':'#668478','light':'#C7CFBA','gold':'#D9B25F','ink':'#172723','pale':'#EDF1EA','muted':'#496357'}

def render(names,filename,heading,footer,retrospective=False):
    source=ROOT/'data/history-recovery-results.json' if retrospective else SOURCE
    d=json.loads(source.read_text())
    if retrospective:
        rows=json.loads((ROOT/'moves.json').read_text());ec={'TP':0,'FN':0,'FP':0,'TN':0}
        for row in rows:
            assert isinstance(row['ec_direct_award'],bool) and isinstance(row['is_brilliant'],bool)
            ec[('TP' if row['ec_direct_award'] else 'FN') if row['is_brilliant'] else ('FP' if row['ec_direct_award'] else 'TN')]+=1
        assert len(rows)==1048 and len(d['rows'])==1048 and d['removed_true']==0 and d['removed_false']==2
        d={'overall':{'refined':d['refined_retrospective_counts'],'ec_direct':ec}}
    else:assert d['total_moves']==200 and d['games']==106
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
    fig,axes=plt.subplots(1,2,figsize=(15.8,5.5),dpi=110,sharey=True)
    fig.patch.set_facecolor('white')
    fig.suptitle(heading,x=.035,y=.965,ha='left',fontsize=21,color=COLORS['ink'],weight='bold')
    fig.text(.035,.885,'1,048 reviewed moves · 545 games · retrospective refinement replay' if retrospective else '200 moves · 106 games · 100 observed Brilliant + 100 explicitly non-Brilliant',fontsize=12,color=COLORS['muted'])
    audit=[]
    for ax,kind,title,color in zip(axes,['positive','negative'],['Brilliants recognized','Extra awards on comparison moves'],[COLORS['moss'],COLORS['gold']]):
        for i,(key,label) in enumerate(names):
            m=d['overall'][key];n=m['TP']+m['FN'] if kind=='positive' else m['FP']+m['TN'];value=m['TP'] if kind=='positive' else m['FP'];assert n==(513 if kind=='positive' else 535) if retrospective else n==100
            ax.barh(i,n,color=COLORS['pale'],height=.48,zorder=1)
            ax.barh(i,value,color=color,height=.48,zorder=2,edgecolor=COLORS['ink'] if kind=='negative' else color,linewidth=.7)
            text_x=value+(.6 if retrospective and kind=='negative' else 5 if retrospective else .22 if kind=='negative' else 2);ax.text(text_x,i,f'{value} / {n}',va='center',color=COLORS['ink'],fontsize=13,weight='bold')
            audit.append({'classifier':key,'panel':kind,'count':value,'denominator':n})
        ax.set_title(title,loc='left',pad=24,fontsize=15,color=COLORS['ink'],weight='bold')
        ax.set_xlim(0,(30 if kind=='negative' else 513) if retrospective else (10 if kind=='negative' else 100));ax.set_ylim(len(names)-.35,-.65)
        ticks=([0,10,20,30] if kind=='negative' else [0,100,200,300,400,513]) if retrospective else ([0,2,4,6,8,10] if kind=='negative' else [0,25,50,75,100])
        ax.set_xticks(ticks,labels=[str(x) for x in ticks])
        ax.set_xlabel(('Extra awards out of 535 comparison moves' if kind=='negative' else 'Recognized out of 513 Brilliant moves') if retrospective else ('Extra awards out of 100 comparison moves' if kind=='negative' else 'Recognized out of 100 Brilliant moves'),labelpad=10,color=COLORS['muted'])
        ax.set_yticks(range(len(names)),labels=[label for _,label in names]);ax.tick_params(axis='both',length=0,labelcolor=COLORS['ink'],pad=10)
        ax.grid(axis='x',color='#DBE3DB',linewidth=.7,zorder=0);ax.set_axisbelow(True)
        for spine in ax.spines.values():spine.set_visible(False)
    axes[1].tick_params(labelleft=False)
    fig.text(.98,.835,'Different scales: left 0–513, right 0–30.' if retrospective else 'Panels use different scales: left 0–100, right 0–10.',ha='right',fontsize=10,color=COLORS['muted'])
    fig.text(.035,.065,footer,fontsize=12,color=COLORS['ink'],weight='bold')
    fig.text(.035,.023,'Guard designed using these labels. No independent validation of the refinement; no deployment-precision claim.' if retrospective else 'Balanced, challenging sample. These rates do not establish ordinary-game badge frequency or deployment precision.',fontsize=10,color=COLORS['muted'])
    fig.subplots_adjust(left=.18,right=.98,top=.73,bottom=.22,wspace=.28)
    out=ROOT/'figures';out.mkdir(exist_ok=True)
    for ext in ('png','svg'):fig.savefig(out/f'{filename}.{ext}',facecolor='white',dpi=110)
    plt.close(fig)
    (out/f'{filename}-audit.json').write_text(json.dumps({'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'plotted_counts':audit,'native_colors':COLORS},indent=2)+'\n')

if __name__=='__main__':
    render([('S','Unrefined History Rule'),('ec_direct','En Croissant')],'history-vs-ec','Unrefined History Rule: historical independent test','78% recognized · 5 extra awards / 100 controls · 94.0% sample badge precision · 86.5% overall agreement')
    render([('forest','Mute selective model'),('S','Unrefined history rule'),('ec_direct','En Croissant')],'fresh-test-results','Matching Chess.com’s Brilliant badges','Selective model: 55% recognized · 1 extra / 100 controls · 98.2% sample precision · 77% agreement')

    render([('refined','Refined History Rule'),('ec_direct','En Croissant')],'history-recovery-replay','History Rule with material guard: development replay','400 matched Brilliants · 22 extra awards · 2 ordinary recoveries rejected · 0 previously matched awards lost',True)
