#!/usr/bin/env python3
"""Supplement: directly test the odd-composite nonunit extension, not author code."""
from collections import Counter
from math import gcd
from pathlib import Path
import json
import random
import subprocess
import importlib.util
spec = importlib.util.spec_from_file_location("review_checks", Path(__file__).with_name("independent-exact-check-v1.py"))
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def pair_witness(word, p, i, j):
    # Direct exact signed-rotation subset DP with an actual index witness.
    need = 2*p-2
    layers = [dict() for _ in range(need+1)]
    layers[0][0] = ()
    rotations = [(n, (-x if i < n < j else x) % p)
                 for n, (x, t) in enumerate(word) if not t]
    for n, (pos, value) in enumerate(rotations, 1):
        for k in range(min(n, need), 0, -1):
            for total, inds in layers[k-1].items():
                nxt = (total + value) % p
                if nxt not in layers[k]:
                    layers[k][nxt] = inds + (pos,)
    target = (word[j][0] - word[i][0]) % p
    if target not in layers[need]:
        return None
    return tuple(sorted(layers[need][target] + (i,j)))


def main():
    out = Path(__file__).with_name('composite-supplement-results-v1.json')
    if out.exists():
        raise FileExistsError(out)
    rng = random.Random(0x77C0A1)
    counts = Counter()
    examples = []
    for p in (9, 15):
        for a in range(1,p):
            d = gcd(a,p)
            if d == 1:
                continue
            m = p // d
            assert 3 <= m <= p // 3
            for sample in range(8):
                word = checks.sample_word(rng,p,a,False)
                refs, _, _ = checks.low_edges(word,a,p)
                byclass = {}
                for index, (pos, q) in enumerate(refs):
                    byclass.setdefault(word[pos][0] % d, []).append(index)
                group = next(v for v in byclass.values() if len(v) >= 4)[:4]
                pairs = []
                for x,y in zip(group,group[1:]):
                    delta = refs[y][1]-refs[x][1]
                    if m-p+1 <= delta <= 2*p-m-1:
                        pairs.append((x,y,delta))
                assert pairs
                i,j,delta = pairs[0]
                left,right = refs[i][0], refs[j][0]
                assert (word[right][0]-word[left][0]) % d == 0
                sums, _ = checks.pair_rotation_sums(word,p,left,right,2*p-2)
                expected = sum(1 << t for t in range(0,p,d))
                assert sums == expected
                witness = pair_witness(word,p,left,right)
                checks.check_witness(word,p,witness,2*p,2)
                counts[str(p)] += 1
                if len(examples) < 2:
                    examples.append({'p':p,'a':a,'d':d,'m':m,'word':word,
                                     'chosen_pair_1_based':[left+1,right+1],
                                     'selector_1_based':[x+1 for x in witness]})
    result = {'seed_decimal':0x77C0A1,'samples_by_p':dict(counts),
              'word_encoding':'[exponent modulo p, reflection bit]',
              'examples':examples}
    result['native_clock_before_receipt'] = subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
    with out.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
