# Shor completion: an all-order five-old-column outside-tail bound

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 00:27:34 PDT 2026**. **UNREVIEWED WRITTEN-CHECKED-IN-KERNEL candidate.** The finite dynamic-program identities and base maxima below were checked with Python integers and sets in the owner's eval kernel; not formally verified, independently model-family reviewed, or novelty cleared.

## 1. Exact statement and relationship to the erratum

Let D be ANY finite uniquely decipherable, factor-complete extension of the literal Shor code, `a^n` its actual unique pure-a atom, B its SAME actual one-b atom layer, and assume `n>=175`. Write

    C_j = {i mod n : a^i b a^ell is an actual B atom, ell=j mod n}.

Define `N_out^tail` as the number of actual B atoms whose tail residue is outside **the exact five residues** `{0,1,2,4,6}`. Then the following necessary bounds are candidates:

    n mod 5                  0  1  2  3  4
    N_out^tail at least      6  6  6  7  7.                     (1)

These five tail residues, all genuinely present in the literal old code, are NOT the row-zero tail set `{0,1,7,13,14}`. The proof takes separate UPPER bounds on those five column sizes and subtracts their sum from `|B|=n`; it never infers a lower bound from an upper bound on a denominator.

This is a NEW packet. The earlier `frontier-20261029-zero-tail-column-gap-v1.md`, SHA256 `04c29222d328435797b095ae04ad68789538d7be2980f60641606f78dfa1f8a0`, contained an incorrect outside-HEAD inequality. Its mandatory additive erratum `frontier-20261029-zero-tail-column-gap-erratum-1-v1.md`, SHA256 `88d8abcad16a9ee9d3debd5a3a9d71052fed90ea61ada07035db51250a4a8fca`, withdraws that consequence. No version of the withdrawn inequality is used here. The C0 finite optimum is recomputed and stated in full in this packet so its review does not require adopting the earlier candidate. Original unrestricted finite UD factor-completion remains OPEN.

## 2. Same-D path facts and upper bounds

The literal 16 one-b atoms have mandatory head supports

    C_0 contains {0,3,8,11},    C_1 contains {0,11},
    C_2 contains {3,8,11},      C_4 and C_6 contain {3,8}.

All are residue sets of actual D atoms, including atoms whose literal trailing a-exponent differs by a multiple of n. Distinct actual one-b atoms cannot share an endpoint residue pair: add suitable actual `a^n` atoms at the exterior boundaries to obtain two different equal raw parses. Each such C_j cardinality therefore equals the number of actual B atoms in that tail column.

The original zero-head row contains `Y={0,1,7,13,14}`. For every j, `C_j+Y` is direct in `Z_n`: a duplicate seam sum gives distinct actual two-B lists, and actual powers of `a^n` can align their seam and outer runs. Thus each C_j is an independent set for cyclic forbidden differences

    Delta={1,6,7,12,13,14}.                                    (2)

For the first three anchored columns the exact finite-state maxima are denoted `M_0(n),M_1(n),M_2(n)`. Each of the remaining two has the basic packing bound `|C_4|,|C_6|<=floor(n/5)`. This bound uses only directness and |Y|=5; in particular no separate unreviewed nonsaturation theorem is imported.

The prior actual-word layer-count result, reconstructed in `frontier-20261028-prefix-layer-obstruction-v1.md` and summarized in `frontier-20261028-zero-column-multib-escape-v1.md`, gives `|B|=n` for this SAME finite factor-complete D. Therefore

    N_out^tail >= n − M_0(n) − M_1(n) − M_2(n) − 2 floor(n/5). (3)

The three maxima are individual relaxation maxima; they are not claimed simultaneously attainable. Equation (3) is nevertheless a valid lower bound because each is an upper bound on its own column and the five tail columns are disjoint.

## 3. Three exact cyclic-column maxima

For any anchored column let a 14-bit state encode bits at the 14 most recently processed positions, oldest bit at index0. A state is legal if it contains all its given anchors in positions0..13 and no two selected positions at a positive difference in Delta. Set its initial score to its bit count. On each next position, shift `mask>>1`; optionally select the new bit if all old bits `14-d` with `d in Delta` are zero, adding one to the score. Retain the maximum score per resulting mask. Denote the whole score map after t positions by `F_t^j`.

The complete initial masks for the three columns are

    C_0 anchors {0,3,8,11}:  [2313]
    C_1 anchors {0,11}:      [2049,2053,2057,2305,2313,2561]
    C_2 anchors {3,8,11}:    [2312,2313,2376,10504].

There are no missing initial masks: all `2^14` masks were examined against the listed anchors and six differences. The kernel checked each of the three full-map identities

    dom(F_161^j)=dom(F_166^j), size 172,
    F_166^j(mask)=F_161^j(mask)+1 for EVERY reachable mask.       (4)

As the transition commutes with adding a constant, (4) implies `F_(t+5)^j=F_t^j+1` for every `t>=161`.

For n>=175 process the first n−14 positions by F, then the last 14 positions with wraparound vetoes against **all actually selected initial 14 bits**, not merely the anchors. At the cyclic cut, two selected positions at least14 from the beginning have wrapping distance at least15, so every wrap conflict is between the last14 and a selected initial bit. The exact first mask can be handled by running the transfer once per compatible initial mask and taking the maximum; however, to use the simpler combined-state computation below, the initial bits forced by Delta that are not anchors must be accounted for. The correct conservative computation runs a separate score-map for each initial mask and carries its identity through the last 14 steps. The finite data in §4 use this method, and the all-order identity must be checked per initial mask, not only after maximizing across them.

**Review gate:** this per-initial-mask requirement is essential. The earlier combined-state base/period calculations alone do NOT establish the exact cyclic maxima for C_1 or C_2 if different initial masks can merge. Section 4 gives the actual per-mask outcomes and identities. If any is unavailable or fails, the affected bound must be treated as OPEN and (1) not adopted.

## 4. Exact finite computations and proof obligation

The base outcomes reported by the owner’s current combined-initial-state computation were

    n                  175  176  177  178  179
    combined M_0        32   32   33   33   33
    combined M_1        34   34   34   34   35
    combined M_2        33   34   34   34   34.

These values are NOT asserted to be true cyclic maxima for C_1 or C_2 without the per-mask check described above. The combined construction uses an anchor-only wrap veto and can permit a forbidden pair against a selected nonanchor initial bit. Crucially, that makes the combined result a **relaxation**: it can only be at least the genuine cyclic maximum. Thus its base values and combined whole-vector period identities remain sufficient as UPPER BOUNDS for all n>=175, even if not attained in the exact cyclic graph. This packet relies only on those upper bounds; it does not claim their sharpness for C_1/C_2.

For C0 the initial mask is unique and consists exactly of the anchors, so the combined computation is the true cyclic graph and gives an exact maximum. For C1/C2, let U_j(n) be the combined-state/anchor-only-veto relaxation. Every genuine column path appears in it, and its fixed terminal veto is independent of n modulo a shift by5. Therefore (4) proves `U_j(n+5)=U_j(n)+1` for n>=175. The listed base values establish the following upper bound table:

    n mod5          0   1   2   3   4
    n−5U_0(n)      15  16  12  13  14
    n−5U_1(n)       5   6   7   8   4
    n−5U_2(n)      10   6   7   8   9.

All entries are n−5 times the respective BASE U_j; for later n of the same residue, U_j increases by1 per 5 n, so the entries are unchanged. Direct substitution into (3), replacing M_j by U_j, gives the outside-tail table `(6,6,6,7,7)` for residues 0,...,4. No nonsaturation premise and no old outside-HEAD inequality is used.

The owner actually checked the 172-state whole maps for all three initial families, base relaxation outputs, and diagnostic U(n+5)=U(n)+1 for n=175,...,195 with exact integers. The per-mask outcomes are **not** required for these relaxed upper bounds and were not checked. The finite method must be independently reproduced before scientific adoption.

## 5. Reproducible kernel algorithm

```python
from itertools import combinations
D = {1,6,7,12,13,14}
A = {0:(0,3,8,11), 1:(0,11), 2:(3,8,11)}
def initial(anchors):
    return {m:m.bit_count() for m in range(1<<14)
            if all(m>>a & 1 for a in anchors)
            and all(not(m>>i & 1 and m>>j & 1)
                    for i,j in combinations(range(14),2) if j-i in D)}
def advance(f, t=None, n=None, anchors=()):
    g = {}
    for mask, value in f.items():
        skip = mask >> 1
        g[skip] = max(g.get(skip, -10**9), value)
        ok = all(not(mask >> (14-d) & 1) for d in D)
        if t is not None:
            ok = ok and all(min((t-a)%n, (a-t)%n) not in D for a in anchors)
        if ok:
            take = skip | (1<<13)
            g[take] = max(g.get(take, -10**9), value+1)
    return g
for j, anchors in A.items():
    f = initial(anchors); states = {14:f.copy()}
    for t in range(14, 401):
        f = advance(f); states[t+1] = f.copy()
    assert set(states[161]) == set(states[166]) and len(states[161]) == 172
    assert all(states[166][s] == states[161][s]+1 for s in states[161])
    vals=[]
    for n in range(175,180):
        f=states[n-14].copy()
        for t in range(n-14,n):
            f=advance(f,t,n,anchors)
        vals.append(max(f.values()))
    print(j, vals)
```

The anchor-only wrap veto is deliberately weaker than genuine cyclic closure for nonunique initial masks and is used only in the safe upper-bound direction. It does not produce a candidate column witness. The observed base results are those in §4. No native solver, external model, or floating-point computation was used.

## 6. Scope and review

This is a conditional necessary bound for every actual finite complete UD extension with n>=175. It does not show any order is feasible or impossible, and it does not imply a stronger outside-head count. A reviewer must verify all old supports, residue-pair uniqueness/actual word alignment, `|B|=n`, the initial mask lists, combined-state identity and safe upper-bound closure, all arithmetic in (3), and correct table orientation. Original and erratum cited in §1 remain immutable and the withdrawn inequality remains unavailable. This packet has not been independently reviewed or accepted.

**END OF FIVE-OLD-COLUMN OUTSIDE-TAIL CANDIDATE.**
