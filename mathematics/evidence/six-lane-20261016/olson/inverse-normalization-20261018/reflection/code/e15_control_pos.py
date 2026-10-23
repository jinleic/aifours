# Positive control for the E15/E15b/E15c census code (first run informally in the eval transcript at ~10:3x PDT; not
# pre-registered).  The length-(4p-3) word sigma_0 rho_1^(2p-3) sigma_2^(2p-1) (kappa = 0, B = 0, one genuine empty run) is
# known to avoid (c2/invstar results: sharpness family).  The census search must find its u-assignment as a full avoider, and
# an independent subsequence DP on the actual word must agree.  The H0 windows are length-agnostic (GR0).
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e15_two_avoiders as E15

def mul(a, b, p):
    (ta, x), (tb, y) = a, b
    if ta == 'r' and tb == 'r': return ('r', (x + y) % p)
    if ta == 'r' and tb == 's': return ('s', (x + y) % p)
    if ta == 's' and tb == 'r': return ('s', (x - y) % p)
    return ('r', (x - y) % p)

def has_identity(word, p):
    reach = {(0, ('r', 0))}
    for g in word:
        new = set(reach)
        for (L, pr) in reach:
            if L < 2 * p:
                new.add((L + 1, mul(pr, g, p)))
        reach = new
    return (2 * p, ('r', 0)) in reach

out = {"controls": []}
for p in (5, 7, 11):
    r = [2 * p - 3, 0]; kap = 0
    W = E15.windows(p, kap, sum(r), 2)
    found = E15.search(p, kap, r, W, {"nodes": 0})
    full = [u for u in found if E15.full_avoid(p, kap, r, u, W) is None]
    word = [('s', 0)] + [('r', 1)] * (2 * p - 3) + [('s', 2)] * (2 * p - 1)
    out["controls"].append({"p": p, "r": r, "two_avoiders": found, "full_avoiders": full,
                            "dp_word_has_identity_2p_subword": has_identity(word, p), "word_length": len(word)})
print(json.dumps(out))
with open(sys.argv[1], "x") as f:
    json.dump(out, f, indent=1)
