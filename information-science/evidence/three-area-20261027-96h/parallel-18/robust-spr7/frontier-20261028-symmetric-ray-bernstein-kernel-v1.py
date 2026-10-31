# Exact symmetric-width ray analysis, executed only in Python Eval.
# Requires exact_minimax search kernel's independent routh_ok/integer_hurwitz.
# No optimizer, numerical root method or author checker is imported.
from fractions import Fraction as Q
from math import comb

def conv_exact(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def pairing_polynomial(a,b):
    raw=[Q(0)]*8
    for j in range(8):
        for k in range(8):
            if (j+k)%2==0:raw[(j+k)//2]+=a[j]*b[k]*((-1)**abs((k-j)//2))
    ae=[a[0],-a[2],a[4],-a[6]];ao=[a[1],-a[3],a[5],-a[7]]
    be=[b[0],-b[2],b[4],-b[6]];bo=[b[1],-b[3],b[5],-b[7]]
    ee=conv_exact(ae,be);oo=conv_exact(ao,bo)
    independent=ee+[Q(0)]
    for k,v in enumerate(oo):independent[k+1]+=v
    if raw!=independent:raise ValueError('PAIRING_EXPANSION_MISMATCH')
    return raw

def halfsplit(beta):
    levels=[beta]
    while len(levels[-1])>1:levels.append([(x+y)/2 for x,y in zip(levels[-1],levels[-1][1:])])
    return [r[0] for r in levels], [r[-1] for r in reversed(levels)]

def whole_halfline(poly,max_depth=32,max_nodes=4000):
    initial=[poly[k]/comb(7,k) for k in range(8)]
    todo=[(Q(0),Q(1),initial,0)];leaves=[];nodes=0
    while todo:
        left,right,beta,depth=todo.pop();nodes+=1
        if beta[0]<=0:
            return {'status':'NONPOSITIVE_AT_DYADIC_X','x':str(left),'value':str(beta[0])}
        if all(z>0 for z in beta):
            leaves.append({'left':str(left),'right':str(right),'coefficients':[str(z) for z in beta]});continue
        if depth>=max_depth or nodes>=max_nodes:return {'status':'SUBDIVISION_CAP','nodes':nodes,'depth':depth}
        bleft,bright=halfsplit(beta);mid=(left+right)/2
        todo.extend([(mid,right,bright,depth+1),(left,mid,bleft,depth+1)])
    return {'status':'STRICT_POSITIVITY','leaves':leaves,'nodes':nodes,'margin':str(min(Q(z) for leaf in leaves for z in leaf['coefficients']))}

ray_base_lo=[Q(x,1000) for x in (4435,10747,23670,40980,10632,13071,1089)]
ray_base_hi=[Q(x,1000) for x in (4586,11496,24364,43182,11217,14315,1147)]
ray_b=[Q(1,1000),Q(883,25),Q(7183,100),Q(16691,100),Q(23757,100),Q(3851,100),Q(3413,100),Q(1)]
ray_factors=[Q(1001,1000),Q(1003,1000),Q(1005,1000),Q(1007,1000),Q(1009,1000)]
ray_report=[]
for r in ray_factors:
    mid=[(x+y)/2 for x,y in zip(ray_base_lo,ray_base_hi)]
    rad=[r*(y-x)/2 for x,y in zip(ray_base_lo,ray_base_hi)]
    lo=[x-y for x,y in zip(mid,rad)];hi=[x+y for x,y in zip(mid,rad)]
    cs=corners(lo,hi)
    rst=[routh_ok(a) for a in cs];dst=[integer_hurwitz(a) for a in cs]
    if rst!=dst:raise ValueError('STABILITY_REPLAY_MISMATCH')
    rec={'factor':str(r),'corner_hurwitz':rst,'lower':[str(x) for x in lo],'upper':[str(x) for x in hi]}
    if all(rst):
        rec['pairing_polynomials']=[[str(z) for z in pairing_polynomial(a,ray_b)] for a in cs]
        rec['whole_halfline']=[whole_halfline([Q(x) for x in poly]) for poly in rec['pairing_polynomials']]
    ray_report.append(rec)
print('symmetric ray exact summary:',[{'factor':r['factor'],'corner_hurwitz':r['corner_hurwitz'],
    'pairing':[{'status':x['status'],'leaves':len(x.get('leaves',[])), 'margin':x.get('margin'), 'x':x.get('x')} for x in r.get('whole_halfline',[])]} for r in ray_report])
