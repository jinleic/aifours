# Exact f39 replay in Python Eval, after loading the independent f26 kernel source.
# No author checker or producer code imported. No scientific subprocess is launched.
from pathlib import Path as f39_Path
from fractions import Fraction as f39_Fraction
from collections import Counter as f39_Counter
from itertools import combinations as f39_combinations
from hashlib import sha256 as f39_sha256
import json as f39_json

f39_root=f39_Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus')
f39_scale=25944
f39_spec=[('closure','frontier-20261028-source-closure-primal-frozen.json','97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec',4397),
          ('sparse','frontier-20261028-all-order-primal-frozen.json','af431478fdad330f5f79fa416bdcaf1c56a56fb30ed4855fc65b50d1cac50545',2558),
          ('first','frontier-20261028-exact-primal-family-scan-result.json','55599041a5a2e73e69d0c70718bc9b049cbbd8e00f3983c5aa42ee86226e88e0',2558)]

def f39_load(filename,digest,expected):
    raw=(f39_root/filename).read_bytes()
    if f39_sha256(raw).hexdigest()!=digest: raise ValueError('INPUT_HASH')
    payload=f39_json.loads(raw)
    entries=payload['primal_values']
    if len(entries)!=expected: raise ValueError('COORDINATE_COUNT')
    out={0:0}
    for item in entries:
        mask=f26_mask([x.replace("'",'’') for x in item['entropy_variables']])
        val=f39_Fraction(item['value'])*f39_scale
        if not mask or mask in out or val.denominator!=1 or val<0: raise ValueError('COORDINATE')
        out[mask]=val.numerator
    if not all(k in out for k in range(1024)): raise ValueError('MISSING_ORIGINAL_COORDINATE')
    if out[1023] != f39_Fraction(1847,276)*f39_scale: raise ValueError('OBJECTIVE')
    return out
f39_P={label:f39_load(name,digest,count) for label,name,digest,count in f39_spec}

def f39_CMI(h,A,B,Z): return h[A|Z]+h[B|Z]-h[A|B|Z]-h[Z]
def f39_all_core(h):
    categories=f39_Counter()
    for vec,rel,rhs,coef,lineno in f26_rows_checked:
        try: value=sum(coeff*h[mask] for mask,coeff in vec.items())
        except KeyError as e: raise ValueError('MISSING_CORE:'+str(e))
        limit=rhs*f39_scale
        if (rel=='>=' and value<limit) or (rel=='<=' and value>limit) or (rel=='=' and value!=limit):
            raise ValueError('BAD_CORE:'+str(lineno))
        categories[rel]+=1
    for i in range(10):
        if not 0 <= h[1<<i] <= f39_scale: raise ValueError('CAP')
        v=i+1; N=f26_adj[v]
        if h[N|1<<i]!=h[N]: raise ValueError('FD')
        if h[1023]-h[1023^(1<<i)]<0: raise ValueError('ORIGINAL_CONDITIONAL_ENTROPY')
    n=0
    for i,j in f39_combinations(range(10),2):
        bi,bj=1<<i,1<<j
        rest=1023^(bi|bj); sub=rest
        while True:
            if f39_CMI(h,bi,bj,sub)<0: raise ValueError('ORIGINAL_CMI')
            n+=1
            if sub==0:break
            sub=(sub-1)&rest
    if n!=11520: raise ValueError('ORIGINAL_COUNT')
    for p in (f26_sigma,f26_tau):
        for mask in range(1,1024):
            if h[mask]!=h[f26_image(mask,p)]:raise ValueError('SYMMETRY')
    return dict(categories),n

def f39_submasks(mask):
    s=mask
    while True:
        yield s
        if s==0:break
        s=(s-1)&mask

def f39_copy_counts(h):
    total=missing=nonzero=0
    for old,new,base,previous in f26_steps:
        B=f26_mask(base)
        for chosen in range(1,1<<len(old)):
            om=nm=0
            for k in range(len(old)):
                if chosen&(1<<k):om|=f26_bits[old[k]];nm|=f26_bits[new[k]]
            for context in f39_submasks(B):
                masks=(context|om,context|nm)
                total+=1
                if any(m not in h for m in masks):missing+=1
                elif h[masks[0]]!=h[masks[1]]:nonzero+=1
    for vec in f26_cis:
        total+=1
        if any(m not in h for m in vec):missing+=1
        elif sum(c*h[m] for m,c in vec.items())!=0:nonzero+=1
    return {'total':total,'evaluable':total-missing,'missing':missing,'nonzero':nonzero}

def f39_branch_counts(h,aux):
    bits=[1<<i for i in range(10)]+[f26_bits[x] for x in aux]
    allmask=0
    for bit in bits:allmask |= bit
    total=available=negative=0
    for bit in bits:
        keys=(allmask,allmask^bit);total+=1
        if all(k in h for k in keys):
            available+=1
            if h[keys[0]]-h[keys[1]]<0:negative+=1
    for x,y in f39_combinations(bits,2):
        rest=allmask^(x|y)
        for sub in f39_submasks(rest):
            keys=(sub|x,sub|y,sub|x|y,sub);total+=1
            if all(k in h for k in keys):
                available+=1
                if h[keys[0]]+h[keys[1]]-h[keys[2]]-h[keys[3]]<0:negative+=1
    return {'total':total,'evaluable':available,'negative':negative,'unevaluable':total-available}

f39_core={label:f39_all_core(f39_P[label]) for label in ('closure','sparse','first')}
f39_copy={label:f39_copy_counts(f39_P[label]) for label in ('closure','sparse')}
f39_branches={label:[f39_branch_counts(f39_P[label],aux) for aux in [("b’0",),("d’1","e’1","g’2"),("f’3","g’3","h’4")]] for label in ('closure','sparse')}

# First point's named substitution is checked directly, in scaled exact integers.
f39_h=f39_P['first']; f39_A,f39_B,f39_C,f39_D,f39_Z=2,512,32,12,401
f39_a=f39_CMI(f39_h,f39_A,f39_B,f39_C|f39_Z)
f39_delta=f39_CMI(f39_h,f39_A,f39_B,f39_Z)-f39_CMI(f39_h,f39_A,f39_B,f39_D|f39_Z)-f39_CMI(f39_h,f39_C,f39_D,f39_Z)
f39_d=f39_CMI(f39_h,f39_A,f39_C,f39_B|f39_Z)+f39_CMI(f39_h,f39_B,f39_C,f39_A|f39_Z)
f39_fn12=13*f39_a-12*f39_delta+78*f39_d
f39_first_values=[str(f39_Fraction(x,f39_scale)) for x in (f39_a,f39_delta,f39_d,f39_fn12)]
if f39_first_values != ['11/276','1/23','0','-1/276']: raise ValueError('FIRST_F12')
print('f39 constraint replay:',{'core':f39_core,'copy':f39_copy,'branches':f39_branches,'first_substitution_a_delta_d_F12':f39_first_values})
