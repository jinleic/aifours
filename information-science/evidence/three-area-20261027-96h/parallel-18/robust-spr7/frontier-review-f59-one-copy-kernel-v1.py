# Independent exact f59 replay in Python Eval. Imports no author checker code.
# Requires the independently loaded f26 and f39 review kernels for their pinned
# closure point; all certificate rows and their 11-bit masks are parsed here.
from pathlib import Path as f59_Path
from fractions import Fraction as f59_Fraction
from hashlib import sha256 as f59_sha256
from collections import Counter as f59_Counter
from copy import deepcopy as f59_copy
import json as f59_json

f59_root=f59_Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus')
f59_cert_bytes=(f59_root/'frontier-20261028-branch1-farkas-cut-result.json').read_bytes()
f59_point_bytes=(f59_root/'frontier-20261028-source-closure-primal-frozen.json').read_bytes()
if f59_sha256(f59_cert_bytes).hexdigest()!='ae9d207260ef0855f84c9ab3ab6f7d62128562db5ad051a0337bf9ccac6e6498':raise ValueError('CERTIFICATE_HASH')
if f59_sha256(f59_point_bytes).hexdigest()!='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec':raise ValueError('POINT_HASH')
f59_cert=f59_json.loads(f59_cert_bytes)
f59_point=f59_json.loads(f59_point_bytes)
if f59_cert['base_point_sha256']!='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec':raise ValueError('CERTIFICATE_POINT_BINDING')
if f59_cert['symbols']!=list('abcdefghij')+["b'0"]:raise ValueError('SYMBOL_ORDER')
f59_h={0:f59_Fraction(0)}
for item in f59_point['primal_values']:
    mask=f26_mask([s.replace("'",'’') for s in item['entropy_variables']])
    if not mask or mask in f59_h:raise ValueError('DUPLICATE_ENTROPY')
    f59_h[mask]=f59_Fraction(item['value'])
if len(f59_h)!=4398:raise ValueError('POINT_COORDINATES')
f59_expected={579:-1,706:-1,728:-1,729:-1,730:2,731:1,733:1,737:-1,739:3,746:-1,762:1,763:-1,764:-1,835:1,962:-1,965:-1,966:1,975:1,976:-1,978:1,980:1,982:-1,991:-1,1000:-1,1002:1,1003:-1,1004:1,1010:-1,1011:1,1013:-1,1014:1,1017:5,1019:-4,1020:1,1021:-1,1022:-1}
if len(f59_expected)!=36:raise ValueError('EXPECTED_COUNT')
f59_Y=1023^(2|4); f59_old=2; f59_fresh=1024
f59_ci={f59_Y:-1, f59_Y|f59_fresh:1, 1023:1, 2047:-1}

def f59_terms(raw):
    d={}
    for mask,c in raw:
        if type(mask)!=int or type(c)!=int or not (0<mask<2048) or mask in d or c not in (-1,1):raise ValueError('TERMS_FORMAT')
        d[mask]=c
    return d

def f59_is_copy(d):
    if d==f59_ci or d=={k:-v for k,v in f59_ci.items()}:return True
    if len(d)!=2 or sorted(d.values())!=[-1,1]:return False
    x=next(k for k,v in d.items() if v==1); y=next(k for k,v in d.items() if v==-1)
    for old,new in ((x,y),(y,x)):
        if old & f59_old and not old & f59_fresh and new & f59_fresh and not new & f59_old:
            context=old^f59_old
            if not (context & ~f59_Y) and new == context|f59_fresh:return True
    return False

def f59_validate(rows):
    if len(rows)!=48:raise ValueError('ROW_COUNT')
    vector=f59_Counter(); kinds=f59_Counter(); seen=set()
    for row in rows:
        idx=row['row_index']
        if idx in seen:raise ValueError('DUPLICATE_ROW')
        seen.add(idx)
        weight=f59_Fraction(row['weight'])
        if not weight:raise ValueError('ZERO_WEIGHT')
        terms=f59_terms(row['terms'])
        meta=row['metadata']; equality=row['equality']
        if not equality:
            if weight<0:raise ValueError('NEGATIVE_CMI_WEIGHT')
            if meta.get('kind')!='CMI':raise ValueError('CMI_METADATA')
            i,j,z=meta['i'],meta['j'],meta['z']
            if type(i)!=int or type(j)!=int or type(z)!=int or not (0<=i<j<=10) or not (0<=z<2048):raise ValueError('CMI_INDICES')
            x,y=1<<i,1<<j
            if z&(x|y):raise ValueError('CMI_CONDITION')
            expected={z|x:1,z|y:1,z|x|y:-1}
            if z:expected[z]=-1
            if terms!=expected:raise ValueError('CMI_TERMS')
            kinds['CMI']+=1
        else:
            if meta.get('kind')!='copy_equality' or not f59_is_copy(terms):raise ValueError('COPY_EQUALITY')
            kinds['copy_independence' if len(terms)==4 else 'copy_marginal']+=1
        for mask,coef in terms.items():vector[mask]+=weight*coef
    result={k:v for k,v in vector.items() if v}
    if any(k&1024 for k in result):raise ValueError('AUXILIARY_CANCELLATION')
    if result!={k:f59_Fraction(276*v) for k,v in f59_expected.items()}:raise ValueError('BASE_VECTOR')
    return kinds,result

f59_rows=f59_cert['exact_separator']['selected_rows']
f59_kinds,f59_sum=f59_validate(f59_rows)
f59_text_vector={int(mask):f59_Fraction(coef) for mask,coef in f59_cert['exact_separator']['original_entropy_coefficients']}
if f59_sum!=f59_text_vector:raise ValueError('SERIALIZED_VECTOR')
f59_L=sum((f59_h[m]*c for m,c in f59_expected.items()),f59_Fraction(0))
if f59_L!=f59_Fraction(-1,276):raise ValueError('POINT_VALUE')

f59_controls=[]
def f59_expect(label,expected,mutator):
    rows=f59_copy(f59_rows);mutator(rows)
    try:f59_validate(rows)
    except ValueError as error:
        if str(error)!=expected:raise ValueError('CONTROL_WRONG_REASON:'+label+':'+str(error))
        f59_controls.append((label,str(error)));return
    raise ValueError('CONTROL_ACCEPTED:'+label)
f59_first_cmi=next(i for i,x in enumerate(f59_rows) if not x['equality'])
f59_first_copy=next(i for i,x in enumerate(f59_rows) if x['equality'] and len(x['terms'])==2)
f59_expect('negative_cmi','NEGATIVE_CMI_WEIGHT',lambda r:r[f59_first_cmi].update(weight='-276'))
def f59_bad_cmi(r): r[f59_first_cmi]['terms'][0][1]*=-1
f59_expect('corrupted_cmi','CMI_TERMS',f59_bad_cmi)
def f59_bad_copy(r): r[f59_first_copy]['terms'][0][0]^=4
f59_expect('corrupted_copy_marginal','COPY_EQUALITY',f59_bad_copy)
f59_expect('remove_row','ROW_COUNT',lambda r:r.pop())
print('f59 exact replay:',{'row_counts':dict(f59_kinds),'base_coefficient_count':len(f59_sum),'auxiliary_coefficient_count':sum(bool(m&1024) for m in f59_sum),'point_L':str(f59_L),'weighted_point':str(276*f59_L),'controls':f59_controls})
