# Shor completion: an exact five-period gap for the actual zero-tail column

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 00:25:13 PDT 2026**. **UNREVIEWED WRITTEN-CHECKED-IN-KERNEL candidate:** the finite max-plus vector identities and base cases below were checked using Python integer and set operations in the owner's eval kernel. They are not a formal proof, an independent-family review, a novelty claim, or an original-problem solution.

## 1. Actual-code statement and exact bound

Let D be ANY finite uniquely decipherable, factor-complete extension of the literal 16-word Shor code. Let `a^n` be its actual unique pure-a atom and B its SAME actual one-b layer. Define

    I_0 = {i mod n : a^i b a^j is an actual B atom, j=0 mod n},
    c_0 = |I_0|.

The literal old atoms give `A={0,3,8,11} subset I_0` and old row-zero tails `Y={0,1,7,13,14}`. No literal tail exponent is required to equal zero: a positive multiple of n also represents tail residue 0. Assume `n>=175`. Then the isolated necessary packing problem has the exact maximum

    c_0 <= M(n) = floor((n−12)/5).                              (1)

The maximum in (1) is exact for the isolated `I_0+Y` packing relaxation, not a claim that an extremal column extends to a complete code or to an actual layer. In particular if 5 divides n then `c_0<=n/5−3`, whereas the separate global nonsaturation candidate only yields `c_0<=n/5−1`.

Every finite complete D has `|B|=n` by the prior actual-word path argument, explicitly reconstructed in `frontier-20261028-prefix-layer-obstruction-v1.md` and summarized in `frontier-20261028-zero-column-multib-escape-v1.md`; this is a named premise, not a claim that a necessary packing constructs D. Let N_out count actual one-b atoms whose HEAD residue is outside A. For each actual head h, the row J_h packs directly with I_0: equal `j+i` seam sums for distinct `(j,i)` give distinct two-B lists whose actual `a^n` padding yields the same raw word. Thus `|J_h|<=floor(n/c_0)`. Summing over the four old heads gives

    N_out >= n − 4 floor(n/c_0) >= n − 4 floor(n/M(n)).        (2)

The second inequality uses `c_0<=M(n)` and `c_0>=4`; its right side may be weak or negative for some n, in which case the trivial nonnegativity bound remains available. It is a conditional necessary consequence for the same actual D, not a claim that any n is feasible. The original finite UD factor-completion problem remains OPEN.

## 2. Direct column packing and finite initial state

For any two actual heads `i,i' in I_0` and actual old tails `y,y' in Y`, two different pairs with equal seam sum `i+y=i'+y' mod n` would create equal raw two-atom parses using actual old row-zero atoms, actual tail-zero-residue atoms, and appropriate nonnegative powers of actual `a^n` at word boundaries. UD rules this out. Therefore `I_0+Y` is direct.

The positive differences among Y are exactly

    Delta={1,6,7,12,13,14}.

For n>=29, a set `I subset Z_n` contains A and packs directly with Y if and only if no two of its elements have cyclic difference in `±Delta`. The forward direction is the equality of two Y differences; conversely a packing collision has a nonzero Y difference from this list. Thus (1) is an exact maximum for an anchored independent set in this fixed-distance circulant graph.

Among the first 14 positions 0,...,13, the anchors 0,3,8,11 force all other bits to zero: each is at a forbidden distance from an anchor. The unique admissible 14-bit initial mask is

    sum_(a in A) 2^a = 2313,     initial score = 4.              (3)

This is a direct finite check over the 14 named positions, not an assumption that a later selected configuration exists.

## 3. Exact max-plus transfer and all-order periodicity

Represent an admissible length-14 bit history by a mask in `[0,2^14)` whose bit i is the selection at the i-th oldest position. At each new position t, try 0 and 1. For 0, replace the mask by `mask>>1`. For 1, require that every bit `14-d` for `d in Delta` is zero, replace the mask by `(mask>>1)|(1<<13)`, and add 1 to the score. For every successor mask keep the maximum score; unreachable masks are absent. Let `F_t` be the entire map from reachable masks to maximum scores after positions `0,...,t−1`, starting from (3). This dynamic program is exact by induction: every compatible prefix chooses one next bit, and compatibility with the future depends only on the previous 14 bits.

The exact kernel check found, as full map identities including identical reachable keys,

    |dom(F_161)|=|dom(F_166)|=172,    F_166(mask)=F_161(mask)+1
                                      for EVERY reachable mask.  (4)

The homogeneous transfer T commutes with adding 1 to every finite score, so applying T repeatedly to (4) proves `F_(t+5)=F_t+1` as whole maps for **every** `t>=161`. This is written induction from an exact finite identity, not a numerical-trend extrapolation.

For a cyclic set of length n>=175, process the first `n−14` bits with F. For positions `n−14,...,n−1`, apply the same transfer but veto selecting t if its circular distance to any of the four anchors in A lies in Delta. This veto covers all wraparound interactions: the first 14 positions are uniquely known from (3), and if both positions are at least14, their wrapping distance is at least15. As n changes by5, the last-14-position veto depends only on each position's distance from n and is identical. Therefore the same terminal 14-step max-plus map, which also commutes with a constant score shift, proves

    M(n+5)=M(n)+1   for EVERY n>=175.                           (5)

The exact base outcomes, including independently directly checked literal independent-set controls, are

    n                175  176  177  178  179
    M(n)              32   32   33   33   33
    n−5M(n)           15   16   12   13   14.

For compact reproducibility, let `T={29,34,39,...,159}`. The following base witnesses have the displayed sizes, contain A and have no forbidden cyclic pair:

    n=175,176: A union {19} union T;
    n=177:     A union {19,169} union T;
    n=178:     A union {19,170} union T;
    n=179:     A union {19,164} union T.

The terminal dynamic program is the upper-bound computation; these witnesses show the five base maxima are achieved for the **packing relaxation**. Together with (5), the maxima agree with `floor((n−12)/5)` for every n>=175, proving (1) contingent on review of the finite identity and base computation.

## 4. Reproducible exact kernel check

The following self-contained pseudocode specifies the integer computation that was actually executed; it does not invoke an external solver or float arithmetic. `D` is the set Delta. States and score values are integer; `-infinity` is implemented by a missing dictionary key.

```python
from itertools import combinations
D = {1,6,7,12,13,14}
A = (0,3,8,11)
initial = sum(1 << a for a in A)
F = {initial: 4}
Fby = {14: F.copy()}
for t in range(14, 401):
    G = {}
    for mask, value in F.items():
        skip = mask >> 1
        G[skip] = max(G.get(skip, -10**9), value)
        if all(not (mask >> (14-d) & 1) for d in D):
            take = skip | (1 << 13)
            G[take] = max(G.get(take, -10**9), value+1)
    F = G
    Fby[t+1] = F.copy()
assert set(Fby[161]) == set(Fby[166])
assert len(Fby[161]) == 172
assert all(Fby[166][s] == Fby[161][s]+1 for s in Fby[161])

def cyclic_max(n):
    f = Fby[n-14].copy()
    for t in range(n-14, n):
        g = {}
        for mask, value in f.items():
            skip = mask >> 1
            g[skip] = max(g.get(skip, -10**9), value)
            ok = all(not (mask >> (14-d) & 1) for d in D)
            ok = ok and all(min((t-a) % n, (a-t) % n) not in D for a in A)
            if ok:
                take = skip | (1 << 13)
                g[take] = max(g.get(take, -10**9), value+1)
        f = g
    return max(f.values())
assert [cyclic_max(n) for n in range(175,180)] == [32,32,33,33,33]
```

The kernel also verified (4) and the direct pairwise cyclic compatibility of all five displayed witnesses, and checked `M(n+5)=M(n)+1` on n=175,...,195 as a diagnostic. The all-n proof is the transfer commutation in §3, not those 21 bounded examples. There is no separate replay program or independent model-family review yet.

## 5. Limits and review request

The isolated maximum (1) concerns the **zero-tail column anchored by the literal four old heads**, not every column. The quantitative outside-head conclusion (2) additionally imports the actual-layer conservation `|B|=n` and direct row-to-zero-column packing. The old Y differences are used as actual atoms of the same D. No finite positive control is a complete code. No n<175 is covered by (1). Neither (1) nor (2) settles any order or the original all-order completion problem.

A disjoint reviewer should check unique initialization, all 172 state scores and equality (4), cyclic wrap veto for n>=175, the five base maxima/witnesses, all-order induction, and the actual-word quantifiers for (2). No independent review, formal verification or novelty assessment is asserted.

**END OF ZERO-TAIL COLUMN GAP CANDIDATE.**
