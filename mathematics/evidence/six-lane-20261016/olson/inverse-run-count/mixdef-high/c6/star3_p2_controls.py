#!/usr/bin/env python3
"""[F] Targeted nonvacuous P2 regression control, not a seed/avoider claim.
Inject an explicitly UNCERTIFIED interval fixture whose boxes satisfy QS* and canonical containment but fail P2. The real criterion
must reject at P2; an in-memory mutant bypassing only P2 must accept, so this test detects a vacuous P2 implementation.
No production or frozen file is modified.
"""
import json,hashlib
src=open('seedXstar3.py').read();guard="if __name__ == '__main__':\n    main()"
raw=open('out/star3_p2_negative_fixture.json','rb').read();fixture=json.loads(raw);p,k,kap,B=fixture['class']
boxes={int(d):tuple(v) for d,v in fixture['boxes'].items()}
def load(s):
    G={'__name__':'star3_p2test_lib'};exec(compile(s.replace(guard,''),'seedXstar3.py','exec'),G)
    E=2*p-2*k+2*kap;R=k+E;A=R-B;g=kap-B
    for d,(a,b) in boxes.items():
        lo,hi=G['bounds'](p,k,kap,B,d,0)
        L1=min(p,d+1-g,(d+B)//2+1)
        U1=p-min(p,A-kap-d+1,(A-d)//2+1)
        if not (max(lo,L1)<=a<=b<=min(hi,U1)):raise RuntimeError('fixture is not inside QS*/canonical ranges')
    def injected(pp,kk,ka,bb,n1,nal,d,fams):
        if (pp,kk,ka,bb)!=(p,k,kap,B):raise RuntimeError('unexpected class in negative fixture')
        return boxes[d]
    G['NS']['exact_seed']=injected
    return G
real=load(src)['class_report'](p,k,kap,B,0)
if real.get('verdict')!='fail' or real.get('stage')!='P2':raise RuntimeError(('correct criterion did not reject P2',real))
old='if a1+a2<lower or b1+b2>upper:'
if src.count(old)!=1:raise RuntimeError('mutation anchor mismatch')
mut=load(src.replace(old,'if False:'))['class_report'](p,k,kap,B,0)
if mut.get('verdict')!='pass':raise RuntimeError(('P2-bypass mutant did not accept',mut))
print(json.dumps({'fixture_sha256':hashlib.sha256(raw).hexdigest(),'checker_sha256':hashlib.sha256(src.encode()).hexdigest(),
                  'control_sha256':hashlib.sha256(open('star3_p2_controls.py','rb').read()).hexdigest(),
                  'real':real,'P2_bypass_mutant':mut,'claim':'negative criterion test only, no GS or group witness'}),flush=True)
