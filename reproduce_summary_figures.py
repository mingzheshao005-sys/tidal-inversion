from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
FIG=OUT/'Figures';FIG.mkdir(exist_ok=True)
DATA=OUT/'Numerical_data'
SD=.0016200408022456227;MU=.03675593947939972
def read(name):
    with (DATA/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
models=read('model_error_metrics.csv')
direction=read('direction_cases_25.csv')
approx=read('response_approximation_cases_25.csv')
names={'MLP':'MLP','global_PINN':'Global PINN','depth_weight_control':'Depth weighted'}
colors=['#0072B2','#D55E00','#009E73']; methods=list(names)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','pdf.fonttype':42})
def save(fig,num):
    for ext in ['png','pdf','svg']:fig.savefig(FIG/f'Figure_{num}.{ext}',dpi=400,bbox_inches='tight')
    plt.close(fig)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.6),layout='constrained')
for j,m in enumerate(methods):
    rr=[r for r in models if r['method']==m]
    ax[0].plot([1,2,3],[100*float(r['global_test_stage_RMSE_m']) for r in rr],'-o',color=colors[j],label=names[m],markersize=4)
    ax[1].plot([1,2,3],[float(r['posterior_mean_shift_refSD']) for r in rr],'-o',color=colors[j],markersize=4)
ax[0].set(ylabel='Water-level test RMSE (cm)',title='(a) State prediction');ax[1].set(ylabel='Signed mean shift / reference SD',title='(b) Posterior displacement');ax[1].axhline(0,color='grey',lw=.6)
for a in ax:a.set(xticks=[1,2,3],xticklabels=['Seed 1','Seed 2','Seed 3'])
ax[0].legend(fontsize=7);save(fig,2)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9),layout='constrained')
for j,dr in enumerate(['parallel','orthogonal_1','orthogonal_2','orthogonal_3']):
    rr=[r for r in direction if r['direction']==dr]
    for sign,marker in [(-1,'o'),(1,'x')]:
        z=[r for r in rr if int(r['sign'])==sign]
        label=('Parallel' if j==0 else f'Orthogonal {j}')+(' / negative' if sign==-1 else ' / positive')
        x=[1000*float(r['observation_rmse_m']) for r in z];y=[float(r['mean_shift_zero_refSD']) for r in z]
        ax[0].plot(x,y,marker=marker,color=['#0072B2','#D55E00','#009E73','#CC79A7'][j],lw=.7,label=label)
        ax[1].plot(x,np.abs(y),marker=marker,color=['#0072B2','#D55E00','#009E73','#CC79A7'][j],lw=.7)
ax[0].set(ylabel='Signed mean shift / reference SD',title='(a) Direction and sign');ax[1].set(ylabel='Absolute mean shift / reference SD',yscale='log',title='(b) Magnitude separation')
for a in ax:a.set(xlabel='Artificial error RMSE (mm)',xticks=[1,2.5,5])
fig.legend(*ax[0].get_legend_handles_labels(),loc='outside lower center',ncol=4,fontsize=6.7);save(fig,4)
rr=approx[1:];fig,ax=plt.subplots(2,1,figsize=(7.2,4.4),sharex=True,layout='constrained');idx=np.arange(24)
for key,label,marker,color in [('nonlinear_shift_refSD','Cached response','o',colors[0]),('linear_shift_refSD','Affine in n','x',colors[1]),('squared_shift_refSD','Affine in n squared','+',colors[2])]:ax[0].plot(idx,[float(r[key]) for r in rr],marker,ms=4,label=label,color=color)
ax[0].set(ylabel='Signed shift / reference SD',title='(a) Mean displacement');ax[0].legend(fontsize=7,ncol=3)
for key,label,marker,color in [('D_mu','Cached minus affine n','o',colors[0]),('D_K','Cached minus affine n squared','x',colors[1])]:ax[1].plot(idx,[float(r[key]) for r in rr],marker,ms=4,label=label,color=color)
ax[1].set(ylabel='Residual shift / reference SD',title='(b) Residual displacement');ax[1].axhline(0,color='grey',lw=.6);ax[1].legend(fontsize=7)
labels=[]
for r in rr:
    dr=r['direction']; dr='P' if dr=='parallel' else 'O'+dr[-1]
    labels.append(f"{dr} {float(r['observation_rmse_m'])*1000:g}{'+' if int(r['sign'])>0 else '−'}")
ax[1].set_xticks(idx,labels,rotation=65,ha='right',fontsize=6)
ax[1].set_xlabel('P: parallel; O1–O3: orthogonal; number: RMSE in mm; sign: perturbation')
save(fig,5)
print("Three summary figures reproduced from stored numerical arrays.")
