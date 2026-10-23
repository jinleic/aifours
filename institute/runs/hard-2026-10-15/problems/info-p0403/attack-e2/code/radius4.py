"""Complete four-flip neighborhood search for staged spectra {4,12,20,28}.

Four flips can change a Walsh coefficient by at most 8. Only initial
magnitude 28 needs a constraint; at those positions at most two of the
four flipped signs may oppose the original Walsh sign. Equivalently,
each of the four triples has an empty intersection of opposing masks.
We exhaust all triples and all four-sets formed by admissible triples.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
from seeds import SEEDS,decode,fwht


def search(bits):
    w=fwht(bits)
    assert set(map(abs,w))=={4,12,20,28}
    high=[a for a in range(512) if abs(w[a])==28]
    bad=[]
    for x in range(512):
        mask=0
        for k,a in enumerate(high):
            c=1-2*(bits[x]^(bin(a&x).count('1')%2))
            if c*w[a]<0:
                mask|=1<<k
        bad.append(mask)
    third={}
    legal_pairs_at_distance_two=0
    ntriples=0
    admissible_triples=0
    for x in range(510):
        for y in range(x+1,511):
            common=bad[x]&bad[y]
            if common==0:
                legal_pairs_at_distance_two+=1
            allowed=0
            for z in range(y+1,512):
                ntriples+=1
                intersection=common&bad[z]
                if intersection==0:
                    allowed|=1<<z
                    admissible_triples+=1
            if allowed:
                third[x,y]=allowed
    legal=[]
    balanced=[]
    for (x,y),mask in sorted(third.items()):
        scan=mask
        while scan:
            b=scan&-scan
            z=b.bit_length()-1
            scan-=b
            fourth=scan & third.get((x,z),0) & third.get((y,z),0)
            while fourth:
                bit=fourth&-fourth
                u=bit.bit_length()-1
                fourth-=bit
                flips=[x,y,z,u]
                # Independently calculate exact modified spectrum for each hit.
                wb=[w[a]-2*sum((1-2*(bits[t]^(bin(a&t).count('1')%2))) for t in flips) for a in range(512)]
                assert max(map(abs,wb))<=28
                legal.append(flips)
                zeros=[a for a in range(512) if wb[a]==0]
                if zeros:
                    balanced.append({"flips":flips,"zero_indices":zeros})
    return {"triples_examined":ntriples,"admissible_triples":admissible_triples,
            "pairs_with_admissible_third":len(third),
            "pairs_preserving_bound_at_distance_two":legal_pairs_at_distance_two,
            "four_sets_preserving_bound":legal,
            "four_sets_preserving_bound_and_giving_a_zero":balanced}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',default='results/radius4.json')
    p.add_argument('--compare',action='store_true')
    args=p.parse_args()
    out={"radius":4,"bound":28,"seeds":{}}
    for name,hx in SEEDS.items():
        rec=search(decode(hx))
        out['seeds'][name]=rec
        print(name,rec,flush=True)
    dest=Path(args.output)
    if args.compare:
        assert json.loads(dest.read_text())==out
    else:
        dest.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    main()
