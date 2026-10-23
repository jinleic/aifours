"""Exact two-flip search, all output-linear shifts at once, integer bitsets.

For a two-point flip set S={x,y}, only initially saturated coefficients
|W_g(a)|=28 can violate the bound 28.  At such a coefficient both flipped
signs must oppose sign(W_g(a)) to violate it.  We encode these opposing
positions by bitsets B_x; legality is B_x & B_y == 0.

A Walsh zero can arise only from |W_g(a)|=4, with both flipped signs
aligned to W_g(a).  Corresponding bitsets C_x give C_x & C_y != 0.
Thus this enumerates every even-distance <=2 candidate with a Walsh zero.
Odd-distance candidates have odd weight and Walsh coefficients 2 mod 4,
so cannot have a zero.  The seed itself has no zero.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from seeds import SEEDS, decode, fwht


def search(bits, bound=28, positions=None):
    if positions is None:
        positions=list(range(512))
    w = fwht(bits)
    assert max(map(abs,w)) <= bound
    high = [a for a in range(512) if abs(w[a]) == bound]
    low = [a for a in range(512) if abs(w[a]) == 4]
    bmask, cmask = [], []
    for x in range(512):
        bm = cm = 0
        for k,a in enumerate(high):
            c = 1 - 2*(bits[x] ^ (bin(a & x).count("1") & 1))
            if c*w[a] < 0:
                bm |= 1 << k
        for k,a in enumerate(low):
            c = 1 - 2*(bits[x] ^ (bin(a & x).count("1") & 1))
            if c*w[a] > 0:
                cm |= 1 << k
        bmask.append(bm)
        cmask.append(cm)
    legal_pairs, balanced_pairs = [], []
    for i,x in enumerate(positions):
        for y in positions[i+1:]:
            if bmask[x] & bmask[y]:
                continue
            legal_pairs.append([x,y])
            zeros = cmask[x] & cmask[y]
            if zeros:
                balanced_pairs.append({"flips":[x,y], "zero_indices":[a for k,a in enumerate(low) if (zeros>>k)&1]})
    return {
        "weight":sum(bits), "W0":w[0], "original_minimum_balancing_distance":abs(w[0])//2,
        "minimum_over_linear_shifts":min(map(abs,w))//2,
        "max_abs_walsh":max(map(abs,w)), "zero_count":w.count(0),
        "absolute_spectrum_histogram":{str(k):v for k,v in sorted(Counter(map(abs,w)).items())},
        "linear_shift_indices_with_minimum_distance_2":low,
        "pairs_examined":len(positions)*(len(positions)-1)//2,
        "pairs_preserving_bound":legal_pairs,
        "pairs_preserving_bound_and_giving_a_zero":balanced_pairs,
        "walsh":w,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results/radius2.json")
    parser.add_argument("--compare", action="store_true")
    args=parser.parse_args()
    out={"bit_order":"f(x), x=0,...,511; x_i=(x>>i)&1; hex MSB first", "radius":2, "bound":28, "seeds":{}}
    for name,hx in SEEDS.items():
        bits=decode(hx)
        rec=search(bits)
        rec.update({"hex":hx,"sha256_ascii_bits":hashlib.sha256(''.join(map(str,bits)).encode()).hexdigest()})
        out["seeds"][name]=rec
        print(name, "hist",rec["absolute_spectrum_histogram"],"legal",len(rec["pairs_preserving_bound"]),"balanced",len(rec["pairs_preserving_bound_and_giving_a_zero"]))
    path=Path(args.output)
    if args.compare:
        assert json.loads(path.read_text()) == out
    else:
        path.write_text(json.dumps(out,indent=2)+'\n')


if __name__=="__main__":
    main()
