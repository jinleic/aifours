"""Planted solvable and broken data controls for the complete searches."""
import argparse
import json
from pathlib import Path
import subprocess
from radius2 import search


def planted():
    # Balanced semibent f=x0+x1*x2+x3*x4+x5*x6+x7*x8, NL=240.
    f=[((x>>0)&1)^(((x>>1)&1)&((x>>2)&1))^(((x>>3)&1)&((x>>4)&1))^(((x>>5)&1)&((x>>6)&1))^(((x>>7)&1)&((x>>8)&1)) for x in range(512)]
    zeros=[i for i,b in enumerate(f) if not b]
    points=zeros[:2]
    g=f.copy()
    for x in points:
        g[x]^=1
    candidates=list(range(8))
    for x in points:
        if x not in candidates:
            candidates.append(x)
    candidates.sort()
    rec=search(g,bound=36,positions=candidates)
    observed={tuple(t['flips']):t['zero_indices'] for t in rec['pairs_preserving_bound_and_giving_a_zero']}
    assert tuple(points) in observed
    # Separate direct-sum test of every candidate in this planted variant.
    expected={}
    wg=[sum((-1)**(g[t]+(bin(a&t).count('1')%2)) for t in range(512)) for a in range(512)]
    for i,x in enumerate(candidates):
        for y in candidates[i+1:]:
            h=g.copy()
            h[x]^=1
            h[y]^=1
            w=[sum((-1)**(h[t]+(bin(a&t).count('1')%2)) for t in range(512)) for a in range(512)]
            new_zeros=[a for a,v in enumerate(w) if v==0 and abs(wg[a])==4]
            if max(map(abs,w))<=36 and new_zeros:
                expected[(x,y)]=new_zeros
    assert expected==observed
    print('PASS planted radius-two control; known balanced pair',points,'all candidate pairs checked',rec['pairs_examined'])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=('planted','make-broken','reject-broken2','reject-broken4'))
    args=p.parse_args()
    if args.mode=='planted':
        planted()
    elif args.mode=='make-broken':
        for radius in (2,4):
            data=json.loads(Path('results/radius%d.json'%radius).read_text())
            if radius==2:
                data['seeds']['dsbf40']['walsh'][0]+=4
            else:
                data['seeds']['dsbf40']['four_sets_preserving_bound'].pop()
            Path('results/radius%d-broken.json'%radius).write_text(json.dumps(data,indent=2)+'\n')
    else:
        radius=int(args.mode[-1])
        raise SystemExit(subprocess.call(['python3','code/check_radius%d.py'%radius,'results/radius%d-broken.json'%radius]))


if __name__=='__main__':
    main()
