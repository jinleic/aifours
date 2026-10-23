# Olson: exchange lemma ZX and S1(c), parent verdict v1

Recorded at 2026-10-18T12:13:33-07:00.

**CORRECTNESS-ACCEPTED as written partial theorems, with the mandatory overlay below.** Every prime p ≥ 5 is covered at the stated hypotheses. No unrestricted INV*(p), ordered Olson for D_(2p), or all-groups ordered Olson theorem follows. No breakthrough-gate or novelty claim; no Lean check.

## Text of record

- [ZX v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-ZX-v1.md), SHA256 `ad2460b251b54e93611a7f632349671ce0727cb2a1a812da6ca48d84d1b6815b`.
- [S1(c) addendum v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-ZX-addendum-S1c-v1.md), SHA256 `7ce7102c3db86c09e6662b353e542e56f104a097442440ebc9ea5e22c012b0b6`.
- [Dependency/statement note](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/notes-ZX-deps-v1.md), SHA256 `f98eb3ebe65cdb36419d002c1eecbb430dd96406993df280f88c9d0a9ba92b33`.
- Read all three through this verdict's overlay. Original files and the [ZS v2 verdict](olson-zs-v2-parent-verdict-v1.md) remain unchanged. The combined acceptance here discharges the addendum's dependency on acceptance of ZX.

## Exact accepted statements

An avoider has no identity 2p-subword in increasing original index order. For a word w, F counts reflections, o=o_F counts odd blocks in the **maximal cyclic constant reflection-block decomposition**, and κ(w)=p−1−(F−o)/2. INV* means all rotations lie in one nonzero pair {ρ_c,ρ_−c} and every maximal cyclic reflection run is constant.

1. **ZX.** Let k,κ be integers, k≥1, 3k≤2p+1 and 0≤κ≤k−1. If Y is a sequence of 2p+2κ−k odd elements of Z_(2p) and every zero-sum subsequence has length ≤2κ, choose a **longest** zero-sum Z and a value g of maximum multiplicity in Y−Z. Then g is a generator and cost_g(Y)≤e=k−1−2κ+|Z|≤k−1. Every signed odd coefficient b_g satisfies |b_g|≤k; positive terms of Z equal g; E+N=cost_g(Y).
2. **S1(a), S1(b), S1(c), and S1+.** For integer κ≥0, let (ZP) exclude zero-sums of lengths [2κ+2,2p], and let (S1) bound every zero-sum length by 2κ. Part (a) gives (S1) when κ≤(p−1)/2. Part (c) also gives it at κ=(p+1)/2. Thus **(ZP) implies (S1) for all integers 0≤κ≤(p+1)/2**. Separately, under 6κ≤4p+2, failure of (S1) supplies two disjoint minimal zero-sums P,P′ of lengths in [2p−2κ+2,2κ] with |P|+|P′|≥2p+2. Part (b) describes an obstruction to (S1), not a counterexample to ROT/INV*/Olson.
3. **Terminal ROT-ZX.** For any length-(4p−2) avoider, it suffices that **some** normal form produced by the accepted process has k=1, or has 3k≤2p+1 and (S1) for its rotation sequence at κ̂=p−1−(F−k)/2. Then the original rotations lie in one nonzero pair. In particular, **κ̂≤(p+1)/2** suffices in the second branch. No uniqueness of normal form is assumed. To infer INV* for the original word from this terminal criterion, retain the extra condition o_F(w)≤p.
4. **Uniform ROT/INV*-ZX+.** Every length-(4p−2) avoider satisfies INV* if

   **3o≤2p+1 and [o≤(p+3)/2 or F≥o+p−3].**

5. **Uniform OLSON-ZX+.** Every length-(4p−1) word satisfying that same uniform condition has an identity 2p-subword in increasing index order.

Together with the separately accepted p=5,o=4 finite case, the unconditional-on-F union is **o_F≤max(4,(p+3)/2)**. For p≥7, 3(p+3)/2≤2p+1; the p=5,o=4 extension comes only from the [finite foundation and lift](olson-p5-few-lift-parent-verdict-v1.md).

| Prime | Uniform coverage without an extra F condition | Additional uniform coverage |
|---:|---|---|
| 5 | o≤4, using the separate finite foundation at o=4 | None asserted here |
| 7 | o≤5 | None asserted here |
| 11 | o≤7 | None asserted here |
| 13 | o≤8 | o=9, F≥19 |
| 17 | o≤10 | o=11, F≥25 |
| 19 | o≤11 | o∈{12,13}, F≥o+16 |

These are sufficient classes, not a claim that avoiders realizing the new parameters exist. At p=7 and 11, “every avoider” always means every avoider **within the displayed o range** (or meeting the existential terminal criterion), never every dihedral avoider.

## Hostile reviews

| Claim packet | Codex gpt-6.1-sol | Claude claude-opus-5-5 |
|---|---|---|
| ZX | [Review](olson-rotation-zx-v1-codex-v1.note.md), `08bbf21922e8ef13c8dd2006b74a3bc63e13d8f1bbf65777901401c297ce2156`; 0 FATAL/MAJOR, 2 MINOR | [Review](olson-rotation-zx-v1-claude-v1.note.md), `2a8584f535d40f3754dfe5b0996b8681daaf876952d2c60886609f06ab474de2`; 0 FATAL/MAJOR, 11 MINOR |
| S1(c) and consequences | [Review](olson-rotation-zx-s1c-v1-codex-v1.note.md), `c40d2d8ae737dd3de581fa081b3d641285a2aaf83d17405fb2a59be2795fc54c`; ACCEPT, 0 findings under integer κ | [Review](olson-rotation-zx-s1c-v1-claude-v1.note.md), `370e410af4ea072b3fb6805e6cf6742bc8c7d4bfa37a66e42a120cf2af5b3c35`; S1(c) ACCEPT, consequences ACCEPT-WITH-FIXES, 0 FATAL/MAJOR, 8 MINOR |

Codex hash-checked the snapshots. Claude had no tools and audited the inlined written arguments. Both checked all mathematical implications; their agreement is not formal verification.

## Mandatory overlay and finding disposition

1. **Integer domain** (ZX Codex 1; S1(c) M1): S1(a)/(b) and S1+ explicitly require κ∈Z_≥0. Without this they are false: p=5, κ=1/2, Y=1·9 in Z_10 satisfies (ZP) but violates (S1). All word-derived κ are integral since F≡k mod2.
2. **Existential normal form** (ZX Codex 2; Claude m1; addendum M7): replace “its/whose normal form” by “some normal form produced by the process.” Any residual statement must quantify over all admissible normal forms. Higher κ̂ alone is not failure: actual (S1), or another form, may suffice.
3. **k=1 and nonzero pair** (m2,m3; M3,M4): handle k=1 by K1 first, including c≠0. Use DAV's κ̂≤k−1 only for k≥2. For that case κ̂≥0 follows independently from GRX: H≥p would supply an all-plus identity selection with zero rotations.
4. **SHgen-E** (m4): expansions preserve k and the required block/empty-run representation. Every base word has length4p−2, rotations in one nonzero pair and o_F=k≤(2p+1)/3≤p. This is the explicit caller discharge; cite the generalized [ZS v2 overlay V3](olson-zs-v2-parent-verdict-v1.md), not only the earlier half-range bound.
5. **Definitions and dependencies** (m5,m10,m11; M2,M5): use the definitions above. The sequence proof is complete modulo classical D(C_n)=n and imported MULT(ii),(iii); MULT(i) is not needed by ZX. The theorem consequences additionally import GRX, PM*, K1, normal form/DAV, SHgen/SHgen-E, restricted REFL-few-odd, RGR-LONG and the OLSON-FEW case structure. The supplied REFL r5 statement/interface is read at its accepted scope through the [REFL parent verdict](olson-refl-fewodd-parent-verdict-v1.md), rather than treating stale r4 line references as new evidence.
6. **S1(b)** (m6): “apart from (G′)” precedes the sequence hypothesis discussion. Its two-piece obstruction is stated under 6κ≤4p+2; conversely P·P′ violates (S1) since κ<p under that bound. S1(b) is not a premise of the ROT/INV*/OLSON consequences.
7. **S1(c) notation/parity** (M2): s(T) in the addendum is a group sum, distinct from ZX's integer coefficient sum. Sequences use distinct occurrences. An even length >p+1 is at least p+3; an even length <p+3 is at most p+1. These are the parity steps used in its minimality argument.
8. **Ordered deletion** (M6): Case1 needs o≤2p−3, which follows from 3o≤2p+1. Case2 removes a reflection only from an odd block of length≥3, giving (o−1,F−1); Case3 removes distinct rotation occurrences separately, giving (o or o−2,F). Neither operation lowers F−o. No even-block deletion is invoked.
9. **Scope/existence** (m7,m8,m9; M7,M8): no existence of new-range avoiders is claimed; the type-II sequence already has its rotations in one pair, so it adds no ROT coverage. The ZS obstruction bears only on (k,κ)=(p,p−1); no group realization or ordered-Olson counterexample is supplied, and nothing is claimed at other pairs. The original all-groups ordered Olson target remains open.

These items dispose of all findings without weakening any integer-domain theorem. They replace the candidate's UNREVIEWED labels only at the exact scopes above.

## Independent parent derivation

The parent read ZX's full proof and theorem interfaces and the complete S1(c) addendum, then re-derived the following critical steps.

**ZX.** Longest-Z maximality makes Y′ zero-sum-free and gives e∈[0,k−1]. MULT's 3e+2≤2p prerequisite holds. From e′≥2q and L=m+q obtain m≥L−e′/2; every d_j≤e′+1≤m, so subset weights fill [0,W′] and W′≤2p−1. Exchanging U≤Z for a disjoint Q≤Y′ of congruent weight gives |Q|≤|U|. Singleton exchanges force every positive Z term to be g and every negative coefficient −β to satisfy β≤e−e′. If σ=r+2pt with t≥1, the unreduced negative-weight prefix sums must hit I=[2p−m,m], because |I|≥e−e′. The two independent exchanges give 2p≤|Z|<2p, a contradiction. Thus σ=r. A completion of weight2p−r would give 2p≤|Z|+e′≤3(k−1)≤2p−2; hence W′≤2p−1−r and cost=e′+r≤e.

**S1(c).** A shortest long zero-sum T has N≥2p+2. Davenport supplies a proper nonempty zero-sum; minimality applied to it and its complement forces N=2p+2 and forces every proper nonempty zero-sum to have length p+1. EGZ supplies p occurrences T1 of x-sum0, hence group sum(1,0). In M=T−T1, any x-zero-sum V of length≤p must be odd; T1·V is proper and zero-sum, forcing |V|=1 and V=(1,0). Two Davenport applications to M and M with one such occurrence removed give two distinct (1,0) occurrences. Their length2 zero-sum contradicts the required length p+1.

**Consequences.** κ̂=κ(w)−(o−k)/2. In the uniform low-o branch, κ̂≤k−1≤o−1≤(p+1)/2; in the high-F branch, κ̂≤κ(w)≤(p+1)/2. SHgen(H) follows from 2H≥2p−2k≥k−1≥E; (K) follows from η≤E/2, a_max≤E+1 and 5k≤4p−1. Restricted REFL is applied to the original word with o≤p. The two deletion operations preserve the required branch and reduce o; RGR-LONG then supplies the increasing-index identity selection.

**Finite aid only.** [S1c-AID-v1.json](olson-zs-v2-parent-smoke-v1/S1c-AID-v1.json), SHA256 `946ccb8d33ffe5dfcf748a43ccc1bdb509e07abd0bafd619334f7017cad7b376`, records parent evaluation-kernel DFS over all (ZP)-avoiding odd multisets up to lengths20 and26 at p=5,7 and κ=(p+1)/2: 1,491 and24,057 multisets respectively, no (S1) failures. Negative controls at higher κ detect failures. The source was executed in the parent transcript, not pre-frozen as a standalone script; this is not a proof premise. The lane's ongoing ZX finite experiment is likewise unnecessary and cannot extend acceptance beyond the written statements.

## Boundary and deviations

Written mathematics with explicit classical/accepted imports; no Lean, Comparator, independent kernel or human peer review. No priority/novelty assessment is made for these partial results. The lane's [CPU-limit deviation](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/zx-check-v1/DEVIATION-v1.md) remains disclosed; numerical runs are not premises. Earlier UNKNOWNs remain UNKNOWN.
