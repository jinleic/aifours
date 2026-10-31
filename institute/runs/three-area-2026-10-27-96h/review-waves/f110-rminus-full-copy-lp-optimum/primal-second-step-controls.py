#!/usr/bin/env python3
"""Target both second copies and both two-variable copy marginals.

Imports only the independently authored primal-verify.py, never author code.
"""
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('primal_review_own',ROOT/'primal-verify.py')
v=module_from_spec(spec)
spec.loader.exec_module(v)
sources,_=v.pin_inputs()
_,profiles,_=v.build_profiles(sources)
controls=[]

def check(branch, tag, mask, wanted, wanted_step, wanted_sel=None, wanted_base=None):
    p=profiles[branch-1]; H=p['H'].copy(); H[mask]+=1
    try:
        v.copies(H,p['labels'],branch)
    except v.Reject as exc:
        v.require(exc.code==wanted and exc.detail[0:2]==(branch,wanted_step),
                  'WRONG_CONTROL_REASON',(tag,wanted,wanted_step,exc.code,exc.detail))
        if wanted_sel is not None:
            v.require(exc.detail[2]==wanted_sel,'WRONG_CONTROL_SUBSET',(tag,exc.detail))
        if wanted_base is not None:
            v.require(exc.detail[3]==wanted_base,'WRONG_CONTROL_BASE',(tag,exc.detail))
        controls.append({'branch':branch,'name':tag,'changed_mask':mask,
                         'expected':wanted,'observed':exc.code,'detail':exc.detail})
    else:
        raise v.Reject('CONTROL_ACCEPTED',(branch,tag))

for branch in (2,3):
    p=profiles[branch-1]; labels=p['labels']; first,second=v.copy_specs(branch)
    check(branch,'second_singleton',v.named_mask(second[1],labels),'COPY_MARGINAL',2,1,0)
    check(branch,'second_conditioning_subset',v.named_mask(second[1]+('a',),labels),
          'COPY_MARGINAL',2,1,1)
    check(branch,'second_independence',v.named_mask(second[1]+second[3],labels),
          'COPY_INDEPENDENCE',2)
    check(branch,'first_joint_copy',v.named_mask(first[1],labels),'COPY_MARGINAL',1,3,0)

result={'completed_native_clock':v.clock(),
        'manifest_sha256':v.MANIFEST_HASH,
        'verifier_sha256':sha256((ROOT/'primal-verify.py').read_bytes()).hexdigest(),
        'control_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'controls':controls}
with (ROOT/'primal-second-step-receipt-v1.json').open('x',encoding='utf-8') as f:
    json.dump(result,f,indent=2); f.write('\n')
print(json.dumps(result,indent=2))
