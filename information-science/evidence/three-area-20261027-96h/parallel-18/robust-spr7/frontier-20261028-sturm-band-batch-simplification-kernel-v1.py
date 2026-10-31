# Round each independently found rational numerator to a shorter exact vector,
# keeping it only if all four half-line Bernstein proofs remain strictly valid.
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
steps={1:1,2:5,3:3,4:2,5:7,6:2,7:1,8:4,9:1,10:2,11:4,12:3,13:2,14:4,15:3,16:5,17:4,18:5,19:2,20:4,21:3,22:3,23:1,24:4,25:5,26:2,27:1,28:3,29:2}
def rnd(z,D):return Q((2*z.numerator*D+z.denominator)//(2*z.denominator),D)
records=[]
for case,step in steps.items():
 bn='frontier-20261028-sturm-band-strict-certificate-case-%02d-v1.json'%case;rn='frontier-20261028-sturm-band-multi-box-%02d-step-%02d-v1.json'%(case,step)
 br=(root/bn).read_bytes();rr=(root/rn).read_bytes();box=json.loads(br);result=json.loads(rr)
 if result['status']!='COMMON_NUMERATOR_PROVED' or result['source_box_sha256']!=sha256(br).hexdigest():raise ValueError('SOURCE')
 lo=list(map(Q,box['lower']));hi=list(map(Q,box['upper']));cs=corners(lo,hi);large=list(map(Q,result['b']));chosen=None
 for k in range(1,14):
  D=10**k;b=[rnd(v,D) for v in large]
  if not all(v>0 for v in b):continue
  proofs=[]
  for a in cs:
   proof=sign_halfline(pair(a,b));proofs.append(proof)
   if proof['status']!='STRICT_POSITIVITY':break
  if len(proofs)==4 and all(p['status']=='STRICT_POSITIVITY' for p in proofs):chosen=(D,b,proofs);break
 if chosen is None:raise ValueError('ROUNDING_NO_EXACT_PROOF')
 D,b,proofs=chosen;mins=[min(Q(v) for leaf in p['leaves'] for v in leaf['coefficients']) for p in proofs]
 records.append({'case':case,'box':bn,'box_sha256':sha256(br).hexdigest(),'source_result':rn,'source_result_sha256':sha256(rr).hexdigest(),'rounding_denominator':D,'b':list(map(str,b)),'frequency_leaves':[[[leaf['left'],leaf['right']] for leaf in p['leaves']] for p in proofs],'compactified_minimum':str(min(mins))})
 print('simplified box',case,'denominator',D,'leaves',[len(p['leaves']) for p in proofs])
out={'scope':'29 specifically enumerated independent coefficient boxes, not arbitrary boxes','cases':records}
path=root/'frontier-20261028-sturm-band-batch-simple-frozen-v1.json';text=json.dumps(out,indent=2,sort_keys=True)+'\n';path.write_text(text)
print('29-box frozen sha256',sha256(text.encode()).hexdigest())
