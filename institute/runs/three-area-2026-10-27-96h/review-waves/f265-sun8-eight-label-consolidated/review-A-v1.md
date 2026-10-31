# f265 / Review A — universal normal-extension lemmas and finite residual

## Verdict and scope

**WRITTEN SUPPORT in Obligation A, with one MINOR correction to the description of the global residual. FATAL: 0; MAJOR: 0; MINOR: 1.** No defect was found in the universal index formula, the actual left-coset fiber formula, the finite-core preservation claims, quotient inheritance of the original two bounds, either rough-direction argument, or the minimality argument for every proper nontrivial normal cut. The first alternative at candidate LF290–294 describes the normal-extension problem, not by itself the entire unrestricted Sun8 proof obligation: finite nonabelian simple groups remain a separate base case. This is a residual-scope defect, not a disproof of an algebraic lemma.

This is my written reconstruction of the assigned A claims. Reading all 356 LF of the common manuscript is not a whole-manuscript acceptance of the separate B/C/D obligations. I reconstruct the prime-multiplicity and localization facts only insofar as Section 7 invokes them. No sibling review has been consulted or inherited.

Native `/bin/date` observations returned by the tool:

- With the initial manifest verification: **Thu Oct 29 16:07:32 PDT 2026**.
- After complete input display and before composing this review: **Thu Oct 29 16:21:24 PDT 2026**.

These are observations, not inferred creation timestamps. This report is prospective; it changes no source, earlier verdict, historical process finding, or parent disposition.

## 1. Per-claim dispositions

All candidate LF references below are to input 8 in the coverage receipt.

| Claim / location | Disposition | Basis and boundary |
| --- | --- | --- |
| Arbitrary-group identity `n_i=a_i b_i`, including finite indices but possibly infinite sets, LF37–52 | **SUPPORTED** | The two index towers and the explicit left-coset bijection in §3.1 require only normality of N and finite index of U_i. |
| Quotient images are actual left cosets; common-fiber right translation uses the conjugated subgroups `t K_i t^{-1}`, LF41–42,54–61 | **SUPPORTED** | §3.2 establishes the set identity, the subgroup index, and preservation of disjointness with one common translation. No normality of U_i is used. |
| Simultaneous intersection for pairwise-coprime subgroup indices, including repeated labels and unit indices, LF63–72 | **SUPPORTED** | §3.3 proves surjectivity of a finite coset-set injection by index divisibility. |
| Product gcd divisibility, intersecting-image bound, and impossibility of both factor gcds being 1, LF48–52,74–82 | **SUPPORTED** | §3.4 derives these directly from the preceding lemmas. No assertion that a_i and b_i of one label are coprime is needed. |
| Finite-core construction preserves all n_i, all a_i and b_i, all subset intersections of the actual original and projected cosets, LF84–91 | **SUPPORTED** | §4 supplies the quotient maps and full-inverse-image equalities. Fixed-fiber intersection data also pass through the corresponding surjection. |
| Both original factor hypotheses `B_7(N)<=7` and `B_7(Q)<=7` survive the finite reduction, LF92–93,211–215 | **SUPPORTED** | Both reduced factors are actual quotients. Pullback preserves nonempty disjoint left cosets and their indices; §4. No bound is replaced by `<=2`. |
| Candidate restatement and reconstruction of the pinned rough-quotient theorem, LF141–149 | **SUPPORTED** | Its quantified interface agrees with input 7 LF3 and its written proof LF11–15. §5.1 independently proves it for all T>=2, r>=1. The 210 premise is not interchangeable with the weaker clique-localization premise. |
| Kernel-side rough transfer used in the finite residual, LF280–285 | **SUPPORTED** | §5.2 independently proves the dual transfer. For finite N, order coprime to 210 supplies precisely the needed rough indices. The pinned parent is quotient-side support; the dual is not merely attributed to it. |
| Any arbitrary-group failure produces a finite failure, and there is a least finite counterexample order, LF267–272 | **SUPPORTED** | §6 uses the original-subgroup cores alone. It needs no initially supplied normal cut. |
| Every proper nontrivial normal cut of a least-order nonsimple finite counterexample has two Sun8 factors, LF274–285 | **SUPPORTED** | Both orders are strictly smaller; §6. The factors have the original bound 7, not a strengthened bound. Both orders must separately have a prime divisor at most 7. |
| Section 7 applications of localization and the 5/7 multiplicity bound, LF276–279 | **SUPPORTED at this stated necessary-condition scope** | The written dependency reconstructions in §7 give the invoked conclusions; they do not prove realization or exclusion of a bad family. |
| LF290–294 as a complete global residual | **CONDITIONAL** | Correct as the normal-extension residual. As a route to unrestricted Sun8 it also needs the finite-simple base case; see finding A-M1. |
| A general finite-simple exclusion, or unrestricted Sun8 | **INCONCLUSIVE / NOT PROVED** | LF271–272 correctly refuse a simple-group exclusion. The normal-cut arguments do not settle the nonabelian simple case. |
| Existence or impossibility of an actual eight-coset bad family | **INCONCLUSIVE / NOT PROVED** | Neither the necessary conditions nor this review construct one or exclude all of them. |
| Author exposure, historical independence, priority, novelty, formal or human verification | **INCONCLUSIVE** | The bounded exposure report is status-only. Mathematical support is not a provenance certificate; §9. |

No algebraic identity in the assigned A slice is REFUTED. The conditional residual row is not an accepted universal extension-closure theorem.

## 2. Finding A-M1 — state the finite-simple base case in the global residual

**Severity: MINOR. Location: candidate LF290–294 (in particular LF290–293).**

The alternative beginning “The UNSOLVED remainder is exact: prove” asks for exclusion of eight-coset configurations in extensions whose two factors already satisfy Sun8. Proving that statement excludes a *nonsimple* minimal finite counterexample, but it does not exclude a *simple* minimal counterexample: the latter has no proper nontrivial normal cut, while the degenerate cuts assume the target on G itself. LF271–272 explicitly leave that simple possibility open. Thus the first alternative is not an exhaustive global proof obligation as written, although it is the correct remaining normal-extension obligation. Qualify the sentence as the **normal-extension residual**, and state that a proof of unrestricted Sun8 by this route additionally needs Sun8 for every finite simple group. No source edit is made here. The correction leaves the finite-core, fiber, and minimal-normal-cut arguments unchanged.

A precise positive-proof route is the conjunction of (i) the finite-simple base theorem and (ii) extension closure at the original bound 7. If both were established, induction on finite group order, followed by the finite-core lemma, would give the unrestricted result. Neither missing component is established in this packet.

## 3. Independent reconstruction of the universal lemmas

### 3.1 Index formula and actual quotient cosets

Fix an arbitrary group G, a normal subgroup N, the surjection pi to Q=G/N, and a finite-index subgroup U. Put K=U intersect N and V=pi(U). The full inverse image of V is NU=UN, a subgroup. The correspondence between left cosets of NU in G and left cosets of V in Q gives `[G:NU]=[Q:V]`.

The map from the set of left K-cosets in N to the set of left U-cosets in NU sending `nK` to `nU` is well-defined, onto, and one-to-one: equality on either side says that the quotient of the two representatives lies in U intersect N. Consequently `[NU:U]=[N:K]`. The index tower is finite because `[G:U]` is finite, and yields

`[G:U]=[Q:V][N:K]`.

For any g, the image of gU is exactly the actual left coset `pi(g)V`. None of these arguments says that N, K, Q, or that image coset is a finite set. Applied label by label, this proves LF41–46 and complies with the finite-index correction in input 5 LF34–45.

### 3.2 Fiber orientation and the single translation

Let q lie in the images of some labels, choose one lift t with pi(t)=q, and choose `x_i` in `C_i intersect Nt` for each such label. Since x_i belongs to C_i, we have `C_i=x_i U_i`; since x_i maps to q, the fiber is `Nt=x_i N`. Thus

`C_i intersect Nt = x_i (U_i intersect N) = x_i K_i`.

Right multiplication by the *same* t inverse gives

`(C_i intersect Nt)t^{-1} = (x_i t^{-1})(t K_i t^{-1})`.

The representative `x_i t^{-1}` lies in N. Normality of N makes conjugation by t an automorphism of N, so the displayed subgroup has index `[N:K_i]=b_i`. The single right translation is a bijection on the whole fiber and hence preserves every intersection and disjointness statement among these sets. Dropping the conjugation while keeping right translation is not justified for general U_i. Using separate translations for different labels would not preserve disjointness.

There is also a legitimate left-translation description: `t^{-1}(C_i intersect Nt)=(t^{-1}x_i)K_i`. This does not contradict LF61; it is an alternative orientation, not a license to omit the conjugation in the stated right-translation formula.

### 3.3 Simultaneous cosets without normal subgroups

Let H be the intersection of finitely many subgroups H_i of X, with finite indices d_i. The map on left-coset sets `xH -> (xH_i)_i` is well-defined and injective. Therefore `[X:H]` is finite and at most the product of the d_i. By the index tower, each d_i divides `[X:H]`. If the d_i are pairwise coprime, their product divides `[X:H]`; the upper bound forces equality. The injection is then a bijection of finite sets. Every prescribed tuple of actual left cosets consequently has a common representative in X.

No normality of the H_i was used. Index 1 contributes a one-point coset set and causes no exception. Repeated subgroup labels are harmless; if two identical indices are pairwise coprime, that index is 1. In particular, two disjoint finite-index left cosets have subgroup-index gcd at least 2.

### 3.4 Gcd consequences actually used in A

Write `d_A=gcd(a_i,a_j)` and `d_B=gcd(b_i,b_j)`. Their product divides both `a_i b_i` and `a_j b_j`, hence divides `gcd(n_i,n_j)`. This does not require d_A and d_B to be coprime. If the projected cosets meet, §3.2 supplies two disjoint kernel cosets. By §3.3 their index gcd d_B is at least 2. For an original pair with gcd at most T, it follows that `d_A<=floor(T/2)`.

If d_A=1, the projected pair meets by §3.3. If d_B=1, it cannot meet by the preceding fiber argument. Therefore d_A=d_B=1 is impossible for an actual disjoint original pair. The original two-coset result also gives `2<=gcd(n_i,n_j)<=7` in a bad eight-family. These are the only gcd identities needed for the A proofs; I do not assume the separate cross-gcd formula of Section 2 as an input.

## 4. Finite-core preservation, including every subset

For each U_i, let its core be the kernel of the G-action on the finite left-coset set G/U_i. It is a finite-index normal subgroup contained in U_i. Their finite intersection R is normal, finite-index, and contained in every U_i. Write `rho:G->bar G=G/R`, `bar U_i=U_i/R`, and `bar N=NR/R=rho(N)`. Then bar G is finite and

`rho^{-1}(rho(C_i))=C_i`.

This full-inverse-image equality holds before using disjointness. For every subset J of labels, the intersection of its original cosets is the full inverse image of the intersection of their images. Surjectivity of rho preserves emptiness and nonemptiness in both directions. Also `[bar G:bar U_i]=[G:U_i]=n_i`.

The induced map `eta:Q->bar Q=bar G/bar N` has kernel `pi(R)=NR/N`. This kernel is contained in every V_i because R is contained in every U_i. It follows that each A_i is the full inverse image of its image bar A_i, and `[bar Q:bar V_i]=[Q:V_i]=a_i`. Applying the same full-inverse-image argument to every J preserves the *entire* projected intersection hypergraph, not only its pairs or cliques.

The kernel data also agree exactly. If `rho(n)=rho(u)` for n in N and u in U_i, then n lies in U_i because R is contained in U_i. Hence

`rho(N intersect U_i)=bar N intersect bar U_i`.

The kernel of the surjection N to bar N is `L=N intersect R`, contained in every K_i. Its induced coset map gives `[bar N:rho(K_i)]=[N:K_i]=b_i`. Thus the n-, a-, and b-index lists are all unchanged; this also follows by applying the already-proved product formula in bar G after preserving n_i and a_i.

For completeness, fix one original fiber Nt. Its image is the full fiber `bar N rho(t)`, and the restriction of rho to Nt is onto that fiber. The full-inverse-image equality for C_i implies that `C_i intersect Nt` is the full inverse image, within Nt, of `bar C_i intersect bar N rho(t)`. All subset-intersection questions in this fixed fiber therefore survive as well. This is not an assertion that arbitrary independently assigned fibers glue to a new extension.

Finally, for any surjection X to Y and subgroup W of Y, pulling back an actual left W-coset gives a nonempty actual left coset of its inverse-image subgroup. Disjointness and `[Y:W]` are unchanged under this pullback. Thus `B_T(X)<=r` implies `B_T(Y)<=r`. Since bar N is a quotient of N and bar Q a quotient of Q, the two **original** bounds `B_7<=7` pass separately to both reduced factors. There is no upgrade to 2 and no assumption that the original U_i are normal.

## 5. The two rough directions and comparison with the pinned parent

For a group X and `M_T` the product of primes at most T, the following conditions are equivalent: every finite quotient of X has order coprime to M_T; every finite-index subgroup of X has index coprime to M_T. One direction applies the subgroup statement to finite-index normal kernels. For the other, if H has finite index, the finite left-coset action gives a finite quotient `X/core_X(H)` whose order is a multiple of `[X:H]`.

### 5.1 Rough quotient, arbitrary kernel

Assume every finite quotient of Q is M_T-rough and `B_T(N)<=r`. If G had r+1 disjoint original cosets with all pair gcds at most T, each a_i would be M_T-rough. Since each `gcd(a_i,a_j)` divides a number at most T, it must be 1: any prime divisor would otherwise be both greater than T and at most T. By §3.3 all projected cosets have a common q. By §3.2 their common fiber produces r+1 disjoint actual kernel cosets with indices b_i and pair gcds at most T, contradicting the kernel bound.

This proves the candidate theorem with the same arbitrary-group, arbitrary-normal-kernel, finite-index, repetitions-allowed interface as input 7 LF3 and LF11–15. The proof assumes neither splitting nor coprimality between a_i and b_i of the same label. At T=7 the modulus is 210. A weaker exclusion of primes 2 and 3 from quotient orders gives the clique conclusion in §7 below, not this whole packing transfer. I have not imported the finite controls or reviewer receipts reported in input 7 LF27.

### 5.2 Rough kernel, arbitrary quotient with a packing bound

Independently, assume every finite quotient of N is M_T-rough and `B_T(Q)<=r`. In a hypothetical bad r+1-family every b_i is M_T-rough, so every pair `gcd(b_i,b_j)` is 1 by the same divisibility and prime argument. If any two projected cosets met, §3.2 would produce disjoint kernel cosets of coprime indices, contradicting §3.3. Therefore all projected cosets are pairwise disjoint. Their actual subgroup indices are a_i, with pair gcds dividing the original gcds and hence at most T. This contradicts the quotient bound.

For the finite residual the candidate needs only the specialization: if finite N has order coprime to 210, every b_i divides that order and is 7-rough, so the argument applies. This is not a conclusion from merely assuming `B_7(N)<=7`; it needs roughness. Nor does the pinned parent itself claim to have proved this dual theorem: its displayed theorem is quotient-side. The dual argument above provides its own support. Statements about earlier dual work or priority remain unverified history.

## 6. Finite minimal-counterexample residual

If unrestricted Sun8 fails in any group, take its eight disjoint offending cosets and quotient by the intersection of their cores. Section 4 gives a finite bad group with exactly the same eight indices. Thus the nonempty set of finite counterexample orders has a minimum. Fix a group G of that least order.

For **every** normal subgroup with `1<N<G`, both `[N:1]` and `[G/N:1]` are strictly smaller than the finite order of G. Failure of Sun8 in either factor would itself be a smaller finite counterexample, so both satisfy the original bound 7. No claim that those two facts imply Sun8(G) has been proved; that is exactly the extension gap. Minimality applies separately at every proper nontrivial normal cut, not only at a selected convenient one.

At such a cut, if the order of Q were coprime to 210, §5.1 and the kernel bound would rule out the original bad family. If the order of N were coprime to 210, §5.2 and the quotient bound would do the same. Consequently each of the two orders has at least one prime divisor at most 7. These are two separate necessary divisibility statements; they do not require a common small prime, an index-2 or index-3 subgroup, or a cyclic quotient of either order.

If G is simple there is no proper nontrivial normal cut. The cuts N=1 and N=G are circular for this purpose: one of the assumed factor bounds is then the target bound on G. Thus the candidate correctly makes no all-simple exclusion at LF271–272, and no unprovided f260/f262 body is available as a base theorem.

One elementary all-prime observation sharpens, but does not close, this residual. For a finite cyclic simple group C_p, any disjoint family of at least two nonempty cosets uses only the trivial subgroup, hence singleton cosets of index p. Eight such cosets require p>=8, and then their pair index gcd is p>7; for p<=7 there are not eight. Thus C_p satisfies Sun8 for every prime p. This is a symbolic all-prime argument, not a selected-state control or adoption of another packet. The unresolved simple branch can therefore be confined to finite **nonabelian** simple groups. No general exclusion for those groups is supplied here.

The complete proof-by-minimality residual is: exclude that simple branch, and exclude actual nonsimple least counterexamples at their normal cuts where both factors have Sun8. Establishing extension closure alone removes only the latter branch; this is the qualification recorded as A-M1.

## 7. Dependency reconstructions for the consequences used in Section 7

For localization, take a finite set of pairwise-intersecting projected cosets of an actual bad original family. If their total intersection is empty, §3.3 shows that some pair of a-indices is noncoprime. That pair meets, so §3.4 bounds its gcd by floor(T/2). Intersecting the quotient-subgroup cores gives a finite quotient preserving all these intersections; each a-index divides its order. A prime at most floor(T/2) consequently divides this explicit quotient order. At T=7 the prime is 2 or 3. This is an order-divisibility conclusion only, not the existence of a cyclic prime-order quotient, and not a proof that any such non-Helly clique occurs.

Here is a separate written derivation of the 5/7 claims invoked at LF276–278. Fix p in {5,7} and S the labels with p dividing n_i. For any distinct labels in S, their original gcd is exactly p. By §3.4 their two factor gcds are not both 1; their product divides p. Thus exactly one factor gcd is p and the other 1. Each label carries p on its a-side, b-side, or both; these nonempty subsets of a two-element set pairwise intersect, so they have a common side. There cannot be two labels carrying p on both sides.

If the common side is a, all corresponding b-pairs are coprime, so the projected cosets are pairwise disjoint with a-index gcd p. If the common side is b, all a-pairs are coprime; §3.3 gives a common quotient point and §3.2 gives disjoint kernel cosets with b-index gcd p. With both original factor bounds 7, these arguments rule out |S|=8. Cases |S|<=1 need no pair argument.

Choose a label j outside S. For each i in S, disjointness forces a prime q_i dividing `gcd(n_i,n_j)`. It is one of the three primes in {2,3,5,7} other than p. A repeated q_i for different i would make those two S-indices share p*q_i>7, impossible. Hence |S|<=3. If |S|=3, every outside label has all three remaining primes dividing its index. There are five outside labels; two would then have index gcd divisible by the product of those three primes, which is greater than 7. Thus |S|<=2 for each p. The union of the two S-sets has size at most four, leaving at least four indices coprime to 35. These are necessary constraints, not an existence theorem or an extension-closure proof. No stronger factor bound was used.

## 8. Coverage and process receipt

The manifest was checked **before its body was opened** against SHA-256 `c80d5df02be872ff31b34cfa5ca629d27c84eabffb9d7caf76b375ae2f37c23c`, 6108 bytes, 77 LF. All eight declared inputs were then hash/byte/LF checked, with all values matching, **before any declared input body was opened**. Their initial complete displays occurred in the manifest order, overlays and errata before the candidate. Mathematical reconstruction started only after every declared body, including its actual ending, had been displayed.

Path roots used in the table are exact:

- E = `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`
- W = `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f265-sun8-eight-label-consolidated/`
- P = `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`

Every listed display used `:first-last:raw`; windows below are inclusive actual LF ranges.

| Input path | Observed complete SHA-256 | Bytes / LF | Raw windows displayed |
| --- | --- | --- | --- |
| W`manifest-v1.json` | `c80d5df02be872ff31b34cfa5ca629d27c84eabffb9d7caf76b375ae2f37c23c` | 6108 / 77 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–77 |
| 1. E`frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 / 56 | 1–15; 16–30; 31–45; 46–56 |
| 2. E`frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 / 11 | 1–11 |
| 3. E`frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 / 10 | 1–10 |
| 4. E`frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json` | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 / 12 | 1–12 |
| 5. E`frontier-20261029-f254-review-b-five-minor-additive-erratum-v1.txt` | `d95c7cecf5b39e6d6649f1ca0238acf661f79082be4f8ba3a2ceb9757591244b` | 10485 / 181 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–90; 91–105; 106–120; 121–135; 136–150; 151–165; **166–181 (16-line deviation)**; supplemental 167–181, then 166–166 |
| 6. E`frontier-20261029-f253-review-b-gcd-additive-erratum-v1.json` | `c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3` | 2825 / 25 | 1–15; 16–25 |
| 7. P`math-6-sun8-rough-finite-quotient-arbitrary-kernel-transfer-parent-v1.md` | `8feffe5bd9917b83469548880431e55e71a81ecb9bd21e8eaf43e946411b286b` | 6216 / 28 | 1–15; 16–28 |
| 8. E`frontier-20261029-eight-label-extension-consolidated-v1.txt` | `3b5b1c6b31c74f71ed0dfcb0ec93b2a0aa78f47478559be4fb3a70a86c6ec4e9` | 20185 / 356 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–90; 91–105; 106–120; 121–135; 136–150; 151–165; 166–180; 181–195; 196–210; 211–225; 226–240; 241–255; 256–270; 271–285; 286–300; 301–315; 316–330; 331–345; 346–356 |

**Nonconformance disclosure:** input 5 was initially fully displayed, but its last window was 16 LF rather than the required maximum 15. The supplemental 15-line and 1-line reads recover a compliant-size cover; they occurred after the candidate had been read and do not retroactively make the initial sequence strictly compliant. No lines or endings were omitted. I therefore do **not** certify unqualified compliance with the raw-window gate. Earlier progress narration also departed from the no-progress-updates instruction. These are procedural deviations, separate from the mathematical finding count.

After all declared evidence bodies had been read, I also read the mandatory instruction-only memory summary, the written-math and independent-snapshot review skills, and the tool-device inventory. They supplied no mathematical evidence. No additional evidence body or linked historical source was opened. No external model was invoked. No git, mathematical program, test, selected-state/selected-index control, archive, checker, replay, solver, deletion, publication, paid action, or live infrastructure action was performed. Hashing, byte/LF counting, native clock observations, and final report emission are administrative actions, not mathematical verification.

**Output-transport limitation:** the requested `write` call was made with this exact assigned destination and the complete report, but the tool refused filesystem paths: it supports only `xd://` devices and `local://` scratch. It created no file. To avoid a second scratch artifact, the report was emitted directly to the sole assigned path by a shell text pipeline after checking that the target did not exist or name a symlink. Thus literal successful use of `write` could not be achieved with the available tool. No other file was written or edited.

## 9. What remains open and what this review does not certify

- **Unrestricted Sun8:** open here. Necessary conditions do not exclude all actual bad eight-families.
- **Finite-simple case:** no all-finite-simple theorem is established or adopted. The all-prime cyclic observation in §6 leaves the nonabelian simple branch unresolved.
- **Nonsimple case / extension closure:** both factors of each proper normal cut in a minimal counterexample have the original Sun8 bound, but transferring those two bounds across arbitrary extensions is not proved. Roughness settles only the specified subcases.
- **Eight-coset bad families:** neither existence nor universal exclusion follows. A quotient intersection graph, a non-Helly clique, or separate local fiber assignments is not a realization theorem.
- **Other manuscript slices:** this A report is not acceptance of the separate cross-gcd, saturated-case, or nilpotent-incidence obligations beyond the explicit dependencies reconstructed above.
- **Novelty and provenance:** inconclusive. The owner exposure self-report at LF326–335 is bounded status information, not clean cognition, historical independence, source equivalence, or rehabilitation of any HOLD/STOP/ZERO episode. I did not open protected, held, selected-prime, f161/f162, or sibling-review bodies to compare methods.
- **Assurance:** this is same-harness written reasoning only. No human review, independent-model-family review, Lean/formal-kernel proof, executable mathematical verification, or parent acceptance is certified by this file. Reported executions in the pinned parent remain reports of other executions, not executions performed or independently replayed here.

