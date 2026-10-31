# A genuine κ=1, e_F=2 REF-failure family with a mixed selector

Owner **MathOlson-2-2**, original math-2. Native `/bin/date` immediately before writing: **Wed Oct 28 19:25:54 PDT 2026**. This is a **WRITTEN all-prime family candidate**, with independent finite checks in §7. It has not received a disjoint scientific review, formal proof, novelty or global-adoption verdict.

## 1. The actual original word and exact scope

Let p be any prime `p>=11`, a∈F_p nonzero, `Z=σ_0=s`, `A=σ_a=r^a s`, `B=σ_(−a)=r^(−a)s`, `T_j=σ_(ja)` for `1<=j<=p−1`, and `ρ=r^a`. Write `L=2p−7`. Construct the actual original-order word

`W = [L copies Z] · ρ · A · A · Z · B · B · Z · ρ · T_1 · ρ · T_2 · ρ · ... · T_(p−1) · ρ`.

Every bracket denotes named occurrence repetition, not a group-power simplification. The word has exactly F=3p−2 reflections, R=p+1 nonzero rotations, and length4p−1. Every cyclic reflection gap has at most one rotation, including the final ρ gap from `T_(p−1)` back to the first Z.

**Theorem.** For every p>=11 and a!=0, this actual word has all of the following:

1. Its cyclic constant-reflection-run profile is `o_F=p+2`, `e_F=2`, `H=p−2`, `κ=1`.
2. Its literal raw possible-switch graph has matching number `ν_M=(p+5)/2<=p−3`.
3. It is genuinely **REF-failing**: no reflection-only identity subsequence has length2p. Its exact reflection-only `2p` product support is all nonzero rotation exponents.
4. Nevertheless it has the explicit original-order mixed identity selector of §5.

Thus the count/zero-free/singleton-gap/low-raw-matching/REF-failure base class is genuinely NONEMPTY at the FIRST remaining odd-run boundary `κ=1,e_F=2`, for every p>=11, and this entire exhibited family is SOLVED by a separate actual selector. The other historical OLD/SEL/IPGEN/GS/DS3 caller failures are NOT checked. In particular, this paper does NOT assert the family belongs to the complete L_RES set, does NOT give an L_RES counterexample, and does NOT close the remaining universal branch.

## 2. Actual runs and raw graph

The cyclic reflection-only runs, in order, are

`Z^L, A^2, Z, B^2, Z, T_1, T_2, ..., T_(p−1)`.

Consecutive run exponents differ, including the cyclic boundary `T_(p−1)=B` to the first Z. There are three odd Z runs plus p−1 singleton T runs, so `o_F=p+2`; the A² and B² runs give `e_F=2`. Also

`H=sum floor(ell/2)=(p−4)+1+1=p−2`, hence `κ=p−1−H=1`.

Use the literal raw graph: adjacent cyclic reflection occurrences are joined when their exponents differ OR their actual gap is occupied by a rotation. Every ρ above lies in a gap whose endpoint exponents already differ; no rotation is inserted inside a constant run. Its nontrivial components are exactly three paths:

* a path on2 vertices from the LAST long-run Z to the first A;
* a path on3 vertices from the second A through the first singleton Z to the first B;
* a path on p+2 vertices from the second B through the second singleton Z, all p−1 T reflections and cyclically to the FIRST long-run Z.

The remaining `L−2=2p−9` Z vertices are isolates. The actual graph has p+4 edges and

`ν_M=1+1+floor((p+2)/2)=(p+5)/2<=p−3` exactly when p>=11.

The occupied-gap placement is essential: no hidden edge inside an even or odd constant run is added. No GS/DS3 equivalence beyond this literal graph calculation is imported.

## 3. Reduce every REF-only selection to an active-run parity pattern

Suppose 2p actual reflections are selected, with ALL rotations skipped. Cancel adjacent selected equal reflections inside each original constant run. Let

* z∈{0,1,2,3} be the number of active odd Z runs;
* y∈{0,1,2} be the number of active even runs among A² and B²;
* t be the number of active singleton tail reflections `T_(j_1),...,T_(j_t)`, with `1<=j_1<...<j_t<=p−1`.

Before cancellation, an odd run can contribute at most its even-pair capacity plus1 when active; an even run contributes at most its full even capacity, but loses at least1 when active. The total equal-pair capacity is H=p−2. Therefore a 2p selection forces

`t+z−y >=4`, i.e. `t>=4+y−z`.  (1)

The active prefix (the three Z runs and two even runs) has length h=z+y. Since the full selected reflection count is even,

`t≡h (mod 2)`.  (2)

The selected tail is a strictly increasing list of integer labels. If `t=2s`, its alternating exponent, normalized by a, is `−D` where

`s<=D=sum_(v=1)^s (j_(2v)−j_(2v−1))<=p−s−1`.  (3)

If `t=2s+1`, its normalized alternating exponent is `S`, where

`s+1<=S=j_1+sum_(v=1)^s(j_(2v+1)−j_(2v))<=p−s−1`.  (4)

The upper bounds follow by writing each sum as the last selected index minus disjoint complementary positive gaps. They are ordinary INTEGER inequalities before reducing modulo p.

## 4. Every feasible active pattern has nonzero exponent

Let P be the normalized alternating exponent of the active prefix, computed BEFORE appending the tail.

* **y=0.** By (1), `t>=1`; P=0. Equations (3)–(4) make the tail exponent nonzero modulo p, regardless of the prefix sign.
* **y=1 and z<=2.** Then `t>=3`. Its tail alternating magnitude lies between2 and p−2; P is ±1. Their sum, with either parity sign, cannot be 0 modulo p.
* **y=1 and z=3.** Then t is even and at least2. Whether the active even run is A or B, the actual active prefix has P=−1. The tail contributes `−D` with `1<=D<=p−2`, so the total `−1−D` has magnitude between2 and p−1.
* **y=2 and z<=1.** Then `t>=5`. Its tail alternating magnitude lies between3 and p−3, while |P|<=2. Their sum cannot be 0 modulo p.
* **y=2 and z=2.** Then t is even and at least4; (3) gives `2<=D<=p−3`. The only possible active prefix exponents are P=0 or P=−2: the zero runs selected are left+middle, left+right, or middle+right. Since the tail contributes −D, the total is −D or −(D+2), whose magnitude lies in `[1,p−1]`.
* **y=2 and z=3.** Then t is odd and at least3. The actual active prefix is `Z,A,Z,B,Z`, whose alternating exponent is 0. The tail has nonzero alternating exponent by (4).

These cases exhaust every feasible actual 2p-reflection selection. Every tail contribution and P above is multiplied by the common nonzero a, so the original reflection-only product is never identity. Conversely, select ALL `2p−5` Z occurrences, both A's, both B's, and any one T_j: the count is2p, the equal pairs cancel, and the product is `Z T_j=r^(−ja)`. As j ranges over1,...,p−1, all nonzero exponents occur. Thus the exact reflection-only product support is `F_p\{0}`.

## 5. Explicit original-order mixed selector

Select the following EXACT actual occurrences:

* all L=2p−7 initial Z reflections;
* the ρ immediately after that long run;
* both A reflections, then the first singleton Z, then both B reflections;
* SKIP the second singleton Z;
* the ρ immediately following that skipped Z and before T_1.

The selected count is `(2p−7)+1+2+1+2+1=2p`. Since L is odd and both A² and B² are actual adjacent identity pairs in the selected word, the ordered product is

`Z · ρ · A² · Z · B² · ρ = Z ρ Z ρ = r^(−a) r^a = 1`.

No other rotation or reflection is selected. This original selector has TWO rotations; it is not a reflection-only witness or an equivalence between different packet endpoints.

## 6. Exact boundaries

The word satisfies the previously stated old odd-run floor `o_F>=p+2` exactly, but the floor itself is NOT used or re-proved here. The family is in the newly identified `κ=1,e_F=2` profile and satisfies the literal lower raw matching and REF failure. We have NOT evaluated the remaining OLD/SEL/IPGEN/GS/DS3 caller failures for it, and therefore do not claim membership in their complete set intersection. The explicit mixed selector rules out its being an ordered-Olson or L_RES counterexample regardless of those statuses.

The general original L_RES bridge for every residual word remains open. This example rules out the easy idea that the entire κ=1,e_F=2 structural/REF base is empty or that REF-only coverage proves it; it does not exclude a stronger argument using the other named callers.

## 7. Actual exact bounded checks

`frontier-20261028-olson-kappa1-e2-family-checker.py`, SHA256 `061afc86548a49a1ac67d227fd484ff83daec8ea1344fd72a27d0ce94d1434c4`, returned `PASS_KAPPA1_E2_REF_FAIL_MIXED_SELECTOR` in `frontier-20261028-olson-kappa1-e2-family-check-results.json`, SHA256 `ba7b4eb83912989d95e85a11e70ad51c265deba6960b9f307cfe800daa9d5764`. At p=11,13,17,19 it independently computed the full reflection-only 2p DP support, actual cyclic raw-graph components and matching, and directly multiplied the exact mixed selector. As an intended negative control, changing the two B exponents to +a made the modified word REF-covered; the original word and its pinned data were not altered.

A separately written checker `frontier-20261028-olson-kappa1-e2-family-audit.py`, SHA256 `71f5d6055c41246967bb5a80e33971ee896b554a821320e123ba27860e7f72a8`, imported no first-checker code and returned `PASS_INDEPENDENT_KAPPA1_E2_PARITY_AUDIT` in `frontier-20261028-olson-kappa1-e2-family-audit-results.json`, SHA256 `10e9de61723821fbd41caf494b0e133ec4e4bef5a226a02b5ec0a73edcfd2724`. For the same primes it traversed the actual path components, checked the exact `o_F,e_F` profile and original mixed product, and checked respectively 14,913; 63,019; 1,042,380; and 4,185,195 feasible active-prefix/tail-subset parity cases. These are finite parity supersets, not exhaustive distinct original index lists or a formal all-prime proof.

A complete disjoint scientific review is requested. No independent-model-family, human, formal/kernel, novelty or full residual verdict follows from these checks.

**END — exact first remaining boundary base family and actual selector.**
