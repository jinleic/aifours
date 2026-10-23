#!/usr/bin/env python3
"""Finite parent check of local Boolean support classification and exact source-template actions.
No worker scientific code imported, no CNF generated or solver used. Not a substitute for the written transfer proof.
"""
import hashlib,itertools,json,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
HERE=Path(__file__).resolve().parent
M=Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def admissible(rows,n):
    cols=[sum(((rows[r]>>c)&1)<<r for r in range(n)) for c in range(n)]
    return all(rows) and all(cols) and all((a&b).bit_count()!=1 for a,b in itertools.combinations(rows,2)) and all((a&b).bit_count()!=1 for a,b in itertools.combinations(cols,2))
def permute(p,q):return tuple(p[q[i]] for i in range(8))
def cycle(*groups):
    p=list(range(8))
    for g in groups:
        for a,b in zip(g,g[1:]+g[:1]):p[a]=b
    return tuple(p)
def closure(gens):
    e=tuple(range(8));seen={(e,e)};todo=[(e,e)]
    while todo:
        s,r=todo.pop()
        for sg,rg in gens:
            nxt=(permute(sg,s),permute(rg,r))
            if nxt not in seen:seen.add(nxt);todo.append(nxt)
    return seen

def main():
    t=time.monotonic();result={'at':datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),'script_sha256':sha(Path(__file__)),'claim':'local finite/format checks, NOT fullCNF model verification or n8 theorem'}
    classes={};valid=0;distinguished=0
    for bits in range(512):
        rows=[(bits>>(3*r))&7 for r in range(3)]
        if not admissible(rows,3):continue
        valid+=1;ones=bits.bit_count();classes[str(ones)]=classes.get(str(ones),0)+1
        cols=[sum(((rows[r]>>c)&1)<<r for r in range(3)) for c in range(3)]
        if rows[0].bit_count()>2 or cols[0].bit_count()>2:continue
        distinguished+=1
        assert ones in (3,5,8)
        if ones==3:assert all(x.bit_count()==1 for x in rows+cols)
        if ones==5:
            assert sorted(x.bit_count() for x in rows)==[1,2,2]
            assert sorted(x.bit_count() for x in cols)==[1,2,2]
        if ones==8:assert rows[0]==6 and cols[0]==6
    assert admissible([7,7,7],3) # distinguishes the review's missing unrestrictedK33case
    assert not admissible([3,5,6],3) # no singleton intersection control
    result['all512_3x3']={'admissible':valid,'by_ones':classes,'distinguished_degree_bounded':distinguished,'bounded_classes':[3,5,8],'fullK33_unrestricted_control':True,'intersection1_control':True}
    mf=M/'evidence/n8_one_p4_templates_v1/MANIFEST.json';mp=M/'evidence/gram_dev_v1/GA5L_K5_sb2.map.json'
    man=json.loads(mf.read_bytes());table=json.loads(mp.read_bytes());names=table['vars']
    assert table['meta']['script_sha256']==sha(M/'code/gram_a.py')=='bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a'
    assert table['meta']['cnf_sha256']=='6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b'
    e=tuple(range(8));gens={
      'B1':[(cycle((4,5)),cycle((5,4))),(cycle((5,6)),cycle((4,3))),(cycle((6,7)),cycle((3,2)))],
      'B2':[(cycle((4,5)),e),(cycle((6,7)),cycle((2,3)))],
      'B3':[(cycle((4,5)),e),(cycle((6,7)),e),(cycle((4,6),(5,7)),cycle((2,4),(3,5)))],
      'B5':[(cycle((5,6)),e)]}
    representative={'B1':{4},'B2':{4,6},'B3':{4},'B5':{4,5}}
    out=[]
    for case in man['cases']:
        if not case['id'].startswith('P1-'):continue
        tag=case['id'][3:];S={1:{1,2,3}}
        S.update({i:set(v) for i,v in enumerate(case['supports_row2to7'],2)})
        expected=[]
        for i in range(2,8):
            for c in range(1,8):
                key=json.dumps(['g',1,[0,c],[i,0]])
                v=names[key]
                assert v==49*c+7*i-6
                expected.append(v if c in S[i] else -v)
        assert expected==case['units'] and len(set(expected))==42
        keys=[tuple(int(c in S[i]) for c in range(8)) for i in range(2,8)]
        assert keys==sorted(keys)
        m=sum(len(v) for v in S.values());lower=4-min(3,(49-m-28)//2)
        assert (m,lower)=={'B1':(12,1),'B2':(14,1),'B3':(16,2),'B4':(18,3),'B5':(17,2),'B6':(20,4)}[tag]
        entry={'id':case['id'],'ones':m,'min_other_permutation_columns':lower,'full42_units_bound':True,'rowlex_sorted':True}
        if tag in gens:
            group=closure(gens[tag]);orbits=[];unseen=set(range(4,8))
            for sig,rho in group:
                assert all({sig[c] for c in S[i]}==S[rho[i]] for i in range(1,8))
                assert all(rho[i]==i for i in (0,1,6,7)) and all(sig[i]==i for i in (0,1,2,3))
            while unseen:
                orbit={sig[min(unseen)] for sig,rho in group};unseen-=orbit;orbits.append(sorted(orbit))
            for available in itertools.combinations(range(4,8),lower):
                assert any(sig[a] in representative[tag] for sig,rho in group for a in available)
            entry.update(group_order=len(group),orbits=orbits,representative_squares=sorted(x-2 for x in representative[tag]))
        out.append(entry)
    badsig=cycle((4,5));b5=next(c for c in man['cases'] if c['id']=='P1-B5');S={1:{1,2,3},**{i:set(v) for i,v in enumerate(b5['supports_row2to7'],2)}}
    assert not all({badsig[c] for c in S[i]}==S[i] for i in range(1,8))
    result['template_checks']=out;result['bad_B5_generator_rejected']=True
    counts={}
    for s in (2,3,4,5):
        clauses=[]
        for i in range(2,8):
            for c,d in itertools.combinations(range(1,8),2):
                a=names[json.dumps(['g',s,[0,c],[i,0]])];b=names[json.dumps(['g',s,[0,d],[i,0]])]
                clauses.append(tuple(sorted((-a,-b))))
        assert len(set(clauses))==126 and all(a<0 and b<0 for a,b in clauses)
        counts[str(s)]={'clauses':126,'ordered_bytes_sha256':hashlib.sha256(''.join(f'{a} {b} 0\n' for a,b in clauses).encode()).hexdigest()}
    result.update(mononomial_clause_checks=counts,manifest_sha256=sha(mf),name_map_sha256=sha(mp),status='PASS',seconds=round(time.monotonic()-t,3))
    with (HERE/'RESULT.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result))
if __name__=='__main__':main()
