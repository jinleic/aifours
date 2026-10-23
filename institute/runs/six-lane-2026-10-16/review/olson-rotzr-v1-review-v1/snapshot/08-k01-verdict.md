# Olson rotation: KETA, PAIR1 and ROT-K01 — parent verdict v1

Recorded at 2026-10-18T13:56:36-07:00.

**CORRECTNESS-ACCEPTED with the mandatory overlay below.** For every prime p ≥ 5, the uniform sufficient condition is **o_F ≤ p−1 and F−o_F ≥ 2p−4**: it gives INV* for length-(4p−2) avoiders and an increasing-order identity 2p-subword for length-(4p−1) words over D_(2p). This extends the earlier ZX-SC uniform range, not unrestricted ordered Olson. No novelty, Lean or human-review claim.

## Texts and hostile reviews

- Candidate [ROT-K01 v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-K01-v1.md), SHA256 `b3ecdb4e09d2eae964322b96e0cddb3c48c91bcea258bebbd4324d16c59eb378`. Its new sequence “Lemma K1” is called **PAIR1** in this verdict, to distinguish the accepted one-block Proposition K1. Frozen text is unchanged.
- [Codex](olson-rotation-k01-v1-codex-v1.note.md), SHA256 `0ff55cc391350437c52372c14ae8b41b671ba5fb8d52b0e838fd34d18e38777b`: KETA and sequence lemma ACCEPT; three word conclusions ACCEPT-WITH-FIXES; 0 FATAL/MAJOR, 2 MINOR. All eight snapshot hashes matched.
- [Claude](olson-rotation-k01-v1-claude-v1.note.md), SHA256 `a6e868afe7abe7482340d23e5ec079c6b1d9d94f59e9a1135dfc5c92ba345564`: KETA ACCEPT, other four claims ACCEPT-WITH-FIXES; 0 FATAL/MAJOR, 10 MINOR. It did not inspect hashes. Its “subsumes unreviewed K0” comparison is INCONCLUSIVE and is not used here.
- Accepted imports: [SC0/ZX-SC verdict](olson-zxsc-parent-verdict-v1.md), [ZX/S1(c) verdict and overlay](olson-zx-s1c-parent-verdict-v1.md), [general index-one source statement](olson-index-one-primary-statement-parent-v1.md). Actual heavy-weight definitions were supplied from [SHgen v3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-SHgen-v3.md), SHA256 `fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e`.

## Exact statements

1. **KETA.** For η ≥ 1 heavy rotation occurrences, absolute weights a_j ≥ 3, E = Σ(a_j−1), and a_max = max a_j, we have η+a_max ≤ E+2. Thus E ≤ k−1 and k ≤ p−1 imply SHgen(K): k ≤ 2p−η−a_max−1. If η=0, no maximum is defined or needed; E=0 already gives the light-rotation conclusion.
2. **PAIR1.** Let p ≥ 5 be prime, 1 ≤ k ≤ p−1 integer, and Y a sequence of 2p+2−k odd elements of C_(2p), every zero-sum subsequence having length at most 2. There is a generator g with every signed odd coefficient satisfying |b_g(y)| ≤ k−1, cost_g(Y) ≤ k−1, E ≤ k−2 and N ≤ 1. At k=1 the premise is impossible; it does not assert a negative cost for an existing sequence.
3. **ROT-K01.** For a length-(4p−2) avoider, if **some** admissible normal form has 2 ≤ k ≤ p−1 and κ̂ ∈ {0,1}, its original rotations lie in one nonzero pair {ρ_c,ρ_−c}. The k=1 case uses the separately accepted one-block Proposition K1, not PAIR1.
4. **INV*-K01.** Every length-(4p−2) avoider with o_F ≤ p−1 and F−o_F ≥ 2p−4 satisfies INV*.
5. **OLSON-K01.** Every length-(4p−1) word over D_(2p) satisfying those same inequalities has an identity 2p-subword in increasing original index order.

Here F counts reflections and o_F counts odd maximal cyclic constant reflection blocks. Rotation ρ_x maps to Y(x)=(1,x) in C_2×C_p. For g=Y(c), c≠0, b_g(Y(x)) is the unique odd representative with |b|≤p−2 for x≠0; b_g(Y(0))=p. E=Σ(|b|−1), N counts negative coefficients, and cost=E+N. These agree with the accepted ZX and SHgen definitions.

## Independent parent derivation

The parent read the candidate, checked SHgen's actual definitions, and independently derived the following before accepting the reviews.

**KETA.** Choose a maximal heavy occurrence. All remaining η−1 heavy weights contribute at least 2 to E, so E ≥ a_max−1+2(η−1) ≥ a_max+η−2. Hence 2p−η−a_max−1 ≥ 2p−E−3 ≥ 2p−k−2 ≥ k. The η=0 branch is handled separately.

**PAIR1.** Zero-sums have even length; the hypothesis permits only inverse pairs of distinct occurrences. Two disjoint pairs would give a prohibited length-four zero-sum. If there is no pair, Y is zero-sum-free of length R≥p+3. SC0 gives total positive odd weight W≤2p−1, excess≤k−3 and coefficients≤k−2. This branch is impossible for k≤2.

If a pair {u,v} exists and neither endpoint deletion is zero-sum-free, choose pairs {v,x} and {u,y}. The no-disjoint-pairs property forces x=y, hence u=v=x is the unique order-two element. Deleting u,v leaves a zero-sum-free sequence of length 2p−k≥p+1 containing the third order-two occurrence: a further pair would be disjoint from {u,v}. Under SC0 this remaining order-two term has coefficient p, forcing total weight at least p+(2p−k−1)≥2p, impossible. Therefore one deletion Y_0=Y−{u} is zero-sum-free.

Its length L=2p+1−k≥p+2 and SC0 excess W−L≤k−2. The surviving partner v cannot be the order-two value, whose coefficient p would force W≥3p−k≥2p. Let v=ag. If a≥3, let h count nonunit terms and m=L−h count unit terms. Excess gives a≤k+1−2h, hence m−a≥2p−2k+h≥3. Thus a distinct copies of g in Y_0 together with deleted u=−ag give a zero-sum of length a+1≥4. Contradiction. So v=g and u=−g. All other positive coefficients are ≤k−1≤p−2; E=W−L≤k−2, N=1 and cost≤k−1. At k=1 this branch is impossible (negative excess bound); at k=2 it gives exactly g^(2p−1)(−g).

**ROT-K01.** GRX gives (ZP), and integer-domain S1+ gives (S1) at κ̂=0,1. For κ̂=0, Y is zero-sum-free of length 2p−k≥p+1; SC0 directly gives E≤k−1, N=0 and positive coefficients≤k, hence≤p−2 by oddness. For κ̂=1, PAIR1 applies. In both cases g=Y(c) with c≠0 and all weights are precisely SHgen's. If E=0, rotation rigidity already holds. Otherwise η≥1, SHgen(H) follows from 2H=2p−2−2κ̂≥2p−4≥k−1≥E, and KETA gives (K). SHgen or SHgen-E then contradicts avoidance. All expansions preserve k, block values and genuine empty runs; each base expansion has length 4p−2, rotations in the same nonzero pair and o_F=k≤p−1≤p, supplying the required restricted REFL caller.

**Uniform conclusions.** For k≥2, parity gives integral κ̂ and GRX gives κ̂≥0. Normal form gives k≤o_F≤p−1 and κ̂=κ(w)−(o_F−k)/2≤1; thus κ̂∈{0,1}. Handle k=1 by the one-block proposition. Apply restricted REFL to the original word with o_F≤p−1. In the ordered deletion ledger, Case1 uses o_F≤p−1≤2p−3 and framed equal pairs; Case2 gives (o−1,F−1); Case3 gives (o or o−2,F). These preserve both inequalities, so each shorter avoider meets INV*-K01. The accepted RGR-LONG case argument completes the increasing-order conclusion.

## Boundary and coverage

New examples outside the old ZX-SC uniform range: p=7, o_F=6, F≥16; p=11, o_F=9 or10, F≥o_F+18; p=13, o_F=11 or12, F≥o_F+22. At p=5, o_F=4 was already covered by the separate finite result. No existence of avoiders at these parameters is asserted. The κ̂=0 branch is derived here independently; the unreviewed K0 file is not a premise.

**Excluded sequence boundary k=p.** SC0 already covers a zero-free Y_0 of length p+1. What fails is the involution-triple exclusion: deleting its two endpoints leaves length p and only the weight lower bound 2p−1. For any odd generator g, Y=(pg)^3 g^(p−1) has length p+2 and only length-two nonempty zero-sums: in C_2×C_p, a selected positive-g count i∈[0,p−1] must be 0 modulo p, and then the involution count must be even. Its coefficient p exceeds k−1. This refutes the proposed sequence bound at k=p, **not** ordered Olson. For κ̂=0, (pg)g^(p−1) is zero-sum-free of length p and contains the zero rotation under Y(x); the SC0-based word argument does not extend. No general classification of this boundary is adopted from diagnostic reviewer remarks.

A parent in-memory occurrence-count check at p=5,7,11,13 confirms only zero-sum length2 for the excluded involution family and for the admitted sharp family g^(p+1)((p−2)g)(−g) at k=p−1. The latter has E=p−3, N=1, cost=p−2 and m−a=3. These finite checks are aids, not proof premises.

## Mandatory overlay / all findings disposed

- **m1 / Codex2:** replace the incorrect SC0-at-length-p+1 explanation with the actual excluded involution-triple obstruction above. No word counterexample is claimed.
- **m2 / Codex1:** call the new sequence lemma **PAIR1**; all imported/k=1 citations mean the accepted one-block Proposition K1, including c≠0.
- **m3:** spell out vacuous small-k branches; no negative cost is realized.
- **m4:** κ̂ is integral, and κ̂≥0 follows from GRX for k≥2.
- **m5:** handle η=0 directly and supply the explicit SHgen-E caller discharge above, using [ZS v2 overlay V3](olson-zs-v2-parent-verdict-v1.md).
- **m6:** examples are outside earlier uniform ranges, not outside every existential normal-form route. The new band is empty at p=5 after the finite p5 result is included.
- **m7:** κ̂=0 is independently re-derived; no comparison with the unsupplied K0 file is needed. The method here is SC0 plus the inverse-pair graph, not the ZX exchange argument.
- **m8:** this route covers no κ̂≥2 and no k≥p; other accepted sufficient conditions remain available. Residual claims quantify over all admissible normal forms, not one chosen form.
- **m9:** use the explicit Y, b_g, E, N and cost definitions above.
- **m10:** cite the accepted deletion ledger, retaining o≤p−1≤2p−3 and the shorter-word caller conditions.

## Verification limit

Written proof relative to SC0 and its classical index-one theorem, S1+, GRX, normal form/PM*/DAV/one-block K1, SHgen/SHgen-E, restricted REFL, RGR-LONG and the ordered deletion ledger. Their previously accepted scopes are not enlarged. Both CLI families audited the new argument; parent derivation supplies the independent integration check. No finite search, K0 draft, unreviewed diagnostic classification, Lean kernel or human review is used as a premise. Unrestricted targets remain open.
