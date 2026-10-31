#!/usr/bin/env python3
"""Independent fixed-label P21 4x4 support-size enumeration and mutation."""
import argparse, collections, hashlib, itertools, json, pathlib, subprocess


def h(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def clock(): return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()


def profile_boards():
    p=(4,3,3,2)
    for chosen in itertools.combinations(range(16),12):
        e=sorted((x//4,x%4) for x in chosen)
        if tuple(sum(i==k for i,j in e) for k in range(4))!=p: continue
        if tuple(sum(j==k for i,j in e) for k in range(4))!=p: continue
        yield e


def allowed(vals,degree,strengthened):
    a=vals.count(2); b=vals.count(3)
    if degree==3 and a>1: return False
    if degree==4 and ((a>=2 and b>=1) or (a>=1 and b>=2)): return False
    if degree==4 and strengthened and a==3: return False
    return True


def collect(strengthened):
    p=(4,3,3,2); counts=collections.Counter(); witnesses={}
    for es in profile_boards():
        tag='low_low_present' if (3,3) in es else 'low_low_absent'
        domains=[range(2,min(p[i],p[j])+1) for i,j in es]
        for values in itertools.product(*domains):
            if any(not allowed([values[z] for z,(i,j) in enumerate(es) if i==t],p[t],strengthened) for t in range(4)): continue
            if any(not allowed([values[z] for z,(i,j) in enumerate(es) if j==t],p[t],strengthened) for t in range(4)): continue
            counts[tag]+=1
            witnesses.setdefault(tag,[]).append([[i,j,x] for (i,j),x in zip(es,values)])
    return counts,witnesses


def support2_triples():
    sets=[frozenset(x) for x in itertools.combinations(range(4),2)]
    count=0
    for a,b,c in itertools.product(sets,repeat=3):
        # Distinct orthogonal support-2 rays have identical or disjoint
        # supports, and no three orthogonal vectors fit one 2-plane.
        if any(len(x&y)==1 for x,y in ((a,b),(a,c),(b,c))): continue
        if a==b==c: continue
        count+=1
        assert len({a,b,c})==2
        repeated=next(x for x in (a,b,c) if (a,b,c).count(x)==2)
        other=next(x for x in (a,b,c) if x!=repeated)
        assert not (repeated & other)
    assert count==18
    return count


def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',required=True); args=p.parse_args()
    out=pathlib.Path(args.out)
    if out.exists(): raise SystemExit('refusing overwrite')
    t=clock(); good,gw=collect(True); mutant,mw=collect(False)
    assert good['low_low_absent']==0 and good['low_low_present']==1
    assert mutant['low_low_absent']==0 and mutant['low_low_present']==2
    bad=[w for w in mw['low_low_present'] if w not in gw['low_low_present']]
    assert len(bad)==1
    high_row=[x for i,j,x in bad[0] if i==0]
    assert sorted(high_row)==[2,2,2,4]
    d={'kind':'finite-p21-size-v1','script_sha256':h(__file__),'clock_before':t,
       'fixed_label_counts_after_three_support2_rule':dict(good),
       'valid_ordered_support2_triples_in_4_axes':support2_triples(),
       'mutation_omit_three_support2_rule':{'counts':dict(mutant),'spurious_high_row_sizes':high_row,
          'reason':'two support-2 vectors fill one 2-plane, so a fourth vector orthogonal to them cannot have full 4-axis support',
          'spurious_size_assignment':bad[0]},
       'limits':'support-size necessity only; no vector or mate realization asserted'}
    d['clock_immediately_before_output']=clock()
    with out.open('x',encoding='utf-8') as f: json.dump(d,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'output':str(out),'sha256':h(out),'script_sha256':d['script_sha256'],'clock':d['clock_immediately_before_output']}))


if __name__=='__main__': main()
