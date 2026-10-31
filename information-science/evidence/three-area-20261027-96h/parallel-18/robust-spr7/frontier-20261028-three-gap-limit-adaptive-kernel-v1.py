# Adaptive physical-row exchange on the rho=1 limit with exact tangent
# equalities. A negative optimum is a candidate strict limiting obstruction;
# any full nonnegative limit witness must also pass strict center replay.
from fractions import Fraction as Q
from math import comb,lcm
from collections import deque

def quotient_by_root(poly,root):
    out=[Q(0)]*(len(poly)-1);out[-1]=poly[-1]
    for j in range(len(out)-2,-1,-1):out[j]=poly[j+1]+root*out[j+1]
    if poly[0]+root*out[0]!=0:raise ValueError('CONTACT_MULTIPLICITY')
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def exact_nonnegative_halfline(poly,maxdepth=32,maxnodes=10000):
    while len(poly)>1 and poly[-1]==0:poly=poly[:-1]
    n=len(poly)-1;beta=[poly[k]/comb(n,k) for k in range(n+1)]
    todo=deque([(Q(0),Q(1),beta,0)]);leaves=[];nodes=0
    while todo:
        left,right,beta,depth=todo.popleft();nodes+=1
        if all(v>=0 for v in beta):leaves.append({'left':str(left),'right':str(right),'coefficients':[str(v) for v in beta]});continue
        for x,v in ((left,beta[0]),(right,beta[-1])):
            if v<0:
                if x==1:return {'status':'NEGATIVE_AT_INFINITY','nodes':nodes}
                return {'status':'NEGATIVE','t':str(x/(1-x)),'nodes':nodes}
        if depth>=maxdepth or nodes>=maxnodes:return {'status':'SUBDIVISION_CAP','nodes':nodes}
        L,R=halfsplit(beta);mid=(left+right)/2;todo.append((left,mid,L,depth+1));todo.append((mid,right,R,depth+1))
    return {'status':'NONNEGATIVE_PROVED','leaves':leaves,'nodes':nodes}

def limit_badpoint(poly,residual,contacts,result):
    t=Q(result['t'])
    if independent_pair_t(limit_cs[0],[Q(0)]*8,Q(0))!=0:raise ValueError('PAIR_CONTROL')
    def pv(z):return sum(poly[j]*z**j for j in range(len(poly)))
    if pv(t)<0:return t
    if t in contacts:
        for k in range(1,61):
            for sign in (-1,1):
                v=t+sign*Q(1,2**k)
                if v>=0 and pv(v)<0:return v
    raise ValueError('NEGATIVE_RESIDUAL_WITHOUT_PAIRING')

limit_adapt_grid=set(limit_grid);limit_adapt_rounds=[]
for iteration in range(6):
    latoms=[]
    for ci,a in enumerate(limit_cs):
        for t in sorted(limit_adapt_grid):
            vector,den=pair_vector_t(a,t);latoms.append({'kind':'physical','corner':ci,'t':t,'vector':[Q(v,den)/(1+t)**7 for v in vector]})
    latoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    latoms.extend(row for row in limit_atoms if row['kind']=='tangent')
    scale=lcm(*(x.denominator for row in latoms for x in row['vector']));C=[[int(scale*row['vector'][k]) for row in latoms] for k in range(8)]
    ls=exact_minimax(C,pivot_cap=2400)
    rec={'iteration':iteration+1,'grid':[str(t) for t in sorted(limit_adapt_grid)],'atoms':len(latoms),'pivots':ls['pivots'],'solver_status':ls['status']}
    if ls['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';limit_adapt_rounds.append(rec);break
    opt=ls['optimum']/scale;rec['margin']=str(opt)
    if opt<0:
        weights=[{'kind':row['kind'],'corner':row['corner'],'t':str(row['t']) if row['t'] is not None else 'infinity','sign':row.get('sign'),'weight':str(ls['lambda'][i])} for i,row in enumerate(latoms) if ls['lambda'][i]>0]
        vec=[sum(ls['lambda'][i]*latoms[i]['vector'][k] for i in range(len(latoms))) for k in range(8)]
        if not all(x<0 for x in vec):raise ValueError('LIMIT_CERT_SIGN')
        rec.update({'status':'STRICT_LIMIT_TANGENT_CERTIFICATE','support':weights,'coefficient_sums':[str(x) for x in vec]});limit_adapt_rounds.append(rec);break
    if opt!=0:raise ValueError('TANGENT_SIGNS')
    dual=ls['dual'];rec['dual']=[str(v) for v in dual]
    contacts={1:[Q(15)],2:[Q(3),Q(65)]};new=set();certs=[]
    for ci,a in enumerate(limit_cs):
        poly=pairing_polynomial(a,dual);residual=poly
        for t in contacts.get(ci,[]):
            residual=quotient_by_root(quotient_by_root(residual,t),t)
        out=exact_nonnegative_halfline(residual);certs.append(out)
        if out['status']=='NEGATIVE':new.add(limit_badpoint(poly,residual,contacts.get(ci,[]),out))
        elif out['status'] not in ('NONNEGATIVE_PROVED',):raise ValueError('BOUNDARY_TEST_UNRESOLVED:'+out['status'])
    rec['boundary_checks']=certs
    if not new:
        proofs=whole_halfline(pairing_polynomial(cx_center,dual),max_depth=45,max_nodes=15000)
        if proofs['status']=='STRICT_POSITIVITY' and 'leaves' in proofs:
            verify_leaves_by_power(pairing_polynomial(cx_center,dual),proofs)
            rec.update({'status':'ONE_NUMERATOR_FOR_ALL_RHO_LT_ONE','center_proof':proofs});limit_adapt_rounds.append(rec);break
        rec['status']='BOUNDARY_NONNEGATIVE_CENTER_STRICT_UNRESOLVED';rec['center_proof']=proofs;limit_adapt_rounds.append(rec);break
    new-=limit_adapt_grid
    if not new:raise ValueError('NO_NEW_PHYSICAL_NODE')
    rec['status']='ADDED_BOUNDARY_NEGATIVE_NODES';rec['new_nodes']=[str(t) for t in sorted(new)];limit_adapt_rounds.append(rec);limit_adapt_grid.update(new)
else:limit_adapt_rounds[-1]['terminal']='SIX_ITERATION_LIMIT'
print('adaptive limit exact outcome:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],'status':r['status'],
 'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in limit_adapt_rounds])
