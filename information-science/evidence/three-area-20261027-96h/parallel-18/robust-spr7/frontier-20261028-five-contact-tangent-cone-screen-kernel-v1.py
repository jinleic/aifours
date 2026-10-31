# Exact Gordan-type screening of the FIVE contact tangent equations for the
# bounded 436 rational designs. No finite feasible result is a full SPR proof.
from fractions import Fraction as Q
from math import lcm
def parity(a,t):
    return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
screen={'tested':0,'positive_at_1e-12':0,'margin_inconclusive':0,'face_obstructions':[],'pivot_caps':0}
for idx,design in enumerate(five_design):
    lo,hi,center,vertices,contacts=five_box(design);tangent=[]
    for ci,t in contacts:
        a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
        D=[ep*(-t)**(k//2) if k%2==0 else t*op*(-t)**((k-1)//2) for k in range(8)]
        for sign in (1,-1):tangent.append([sign*v for v in D])
    eps=Q(1,10**12);vectors=[[Q(int(k==j))-eps for k in range(8)] for j in range(8)]+tangent
    scale=lcm(*(v.denominator for row in vectors for v in row));M=[[int(scale*row[k]) for row in vectors] for k in range(8)]
    sol=exact_minimax(M,pivot_cap=600);screen['tested']+=1
    if sol['status']!='CERTIFIED_OPTIMUM':screen['pivot_caps']+=1;continue
    if sol['optimum']==0:
        b=sol['dual']
        if any(v<eps for v in b) or any(sum(row[k]*b[k] for k in range(8))!=0 for row in tangent):raise ValueError('TANGENT_REPLAY')
        screen['positive_at_1e-12']+=1;continue
    if sol['optimum']>0:raise ValueError('TANGENT_PAIR')
    tscale=lcm(*(v.denominator for row in tangent for v in row));TM=[[int(tscale*row[k]) for row in tangent] for k in range(8)]
    found=False
    for k in range(8):
        result=face_probe(TM,k,pivot_cap=1000)
        if result['status']=='NEGATIVE_FACE_WITNESS':
            vec=[sum(result['weights'][i]*tangent[i][j] for i in range(len(tangent))) for j in range(8)]
            if not all(v<=0 for v in vec) or not any(v<0 for v in vec):raise ValueError('FACE_REPLAY')
            screen['face_obstructions'].append({'index':idx,'design':[str(x) for x in design[:8]],'vector':[str(v) for v in vec],
             'weights':[str(v) for v in result['weights']]});found=True;break
    if not found:screen['margin_inconclusive']+=1
    if found:break
print('five-contact tangent-cone bounded screen:',screen)
