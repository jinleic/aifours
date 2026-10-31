# f259 slice A: corrected rough-quotient transfer theorem

**Verdict: written mathematical support for the corrected composite at the exact scope below.** In this slice I find **0 FATAL / 0 MAJOR / 0 MINOR remaining** after applying the new erratum. Original candidate LF67 has a minor finite-set/index wording error, and LF94 has a minor undefined numerical-invariant notation; m1 and m2 respectively repair them. I independently checked these repairs, not the historical f254 reviews. The slice does not review m3–m5, the comparison claims, or author examples other than those needed for m1/m2. This is a same-harness written review, not parent adoption, independent-family or human review, formal/kernel verification, or a novelty/source-priority assessment.

Native `/bin/date` observed before composing this review: **2026-10-29T15:35:34-0700 PDT**; this is not asserted to be its exact creation time.

## Per-claim disposition

`F/M/m` below means fatal/major/minor mathematical or material wording findings **in the corrected composite**, not the independent historical verdicts. PASS is support for precisely the claim and assumptions stated, not a stronger result.

| Claim | Disposition | Boundary |
|---|---|---|
| Finite-quotient/index equivalence, candidate LF13–15 and LF32–41 | PASS, F0/M0/m0 | All groups Q, including infinite Q; left coset action and its core; no normality of the finite-index subgroup. |
| Simultaneous intersection, candidate LF43–57 | PASS, F0/M0/m0 | Every **finite** family of actual left cosets with pairwise-coprime finite subgroup indices; no normality; repeats and index 1 are allowed. |
| Projected indices and kernel index product, LF61–69, as corrected by m1 | PASS, F0/M0/m0 | Original subgroups may be nonnormal; the coset sets themselves can be infinite. Only the three indices are asserted finite. |
| Pairwise-coprime quotient indices from roughness and a bad original family, LF69–73 | PASS, F0/M0/m0 | Uses both the roughness premise and the given bound on each **original** pairwise gcd. |
| One common fibre, right translation, conjugation, and inherited gcd, LF74–83 | PASS, F0/M0/m0 | Actual left cosets, a single chosen fibre and translation for all labels; the conjugated kernel subgroup is needed and stays in N. |
| Full arbitrary-group theorem and the T=7 corollary, LF8–29 | PASS, F0/M0/m0 | For every integer T>=2 and r>=1, every G and N normal in G, subject to the two explicit hypotheses. No split, finite-G, normal-U, Helly, solvability, or coset-cover hypothesis. |
| m1, erratum LF33–45 | PASS, F0/M0/m0 | Original LF67's literal set-finiteness reading is false; the replacement is necessary and sufficient for this proof. |
| m2, erratum LF47–61 | PASS, F0/M0/m0 | For the specified rational-times-C7 kernel, the two predicate assertions are proved; no unintroduced numerical invariant is used. |
| m3/m4/m5 examples and comparative interfaces | INCONCLUSIVE / OUT OF SLICE | All were read in the required packet order, but none is adopted as a premise of this proof or independently judged in this slice. |
| Arbitrary quotient with a small-prime finite quotient; unrestricted Sun8 | INCONCLUSIVE / OUTSIDE THEOREM | The proof's common-fibre argument does not extend merely from factor Sun8; no eight-coset counterexample or resolution is asserted. |

## Independent proof reconstruction

### 1. Exact quotient/index equivalence

Put `M_T=prod_{p prime, p<=T} p`. If every finite-index subgroup of Q has index coprime to `M_T`, the kernel of an onto homomorphism `Q -> F` to a finite group has index `|F|`, which is therefore coprime to `M_T`.

Conversely, take an arbitrary finite-index `V<=Q`, with `a=[Q:V]`. The action by left multiplication on the finite set of left cosets `Q/V` has finite image and kernel `K=core_Q(V)<=V`. Consequently `F=Q/K` is finite, `V/K<=F`, and `a=[F:V/K]` divides `|F|` by finite Lagrange. If every finite quotient order is coprime to `M_T`, so is `a`. The coset-action kernel/core argument does not require Q to be finite or V normal. The trivial quotient and index 1 are included.

### 2. Simultaneous intersection without normality

Let `H_1,...,H_k` be a finite list of finite-index subgroups of an arbitrary X, with `a_i=[X:H_i]` pairwise coprime, and put `H=intersection_i H_i`. The map

`X/H -> product_i X/H_i`, `xH |-> (xH_i)_i`

is well-defined and injective: equality in each component gives `y^-1 x` in every `H_i`. Thus `[X:H] <= product_i a_i`. Since `H<=H_i<=X`, the subgroup-index multiplication law shows that each `a_i` divides `[X:H]`. Pairwise coprimality makes their product divide `[X:H]`; the upper bound forces equality. The injection is therefore onto the finite product. An arbitrary prescribed tuple of actual left cosets consequently has a common representative.

No `H_i` need be normal, and no quotient-group structure on any `X/H_i` is used. Unit indices and repeated labels are legitimate: if the same subgroup occurs at two different positions under the pairwise-coprime hypothesis, its index must be 1. The special case of two disjoint left cosets indeed forces their indices to have nontrivial gcd.

### 3. Factor indices and obtain one real common fibre

Fix `T>=2`, `r>=1`, any group G and `N normal G`. Assume `B_T(N)<=r`, let `Q=G/N` be T-rough-finite, and suppose toward contradiction that `C_i=g_i U_i`, `i=1,...,r+1`, are pairwise-disjoint actual left cosets of finite-index subgroups with every pair of original indices having gcd at most T. Repetition of subgroups is permitted.

Write `pi:G -> Q`, `A_i=pi(C_i)=pi(g_i)pi(U_i)`, `K_i=U_i intersect N`, `a_i=[Q:pi(U_i)]`, `b_i=[N:K_i]`, and `n_i=[G:U_i]`. Because N is normal, `NU_i` is a subgroup, `[G:NU_i]=a_i`, and `nK_i |-> nU_i` is a bijection of **left coset sets** `N/K_i -> NU_i/U_i`. Index multiplication gives `n_i=a_i b_i`. These indices are finite; neither `A_i` nor `K_i` is thereby asserted finite. In particular, `N/K_i` and `NU_i/U_i` here mean coset sets, not necessarily quotient groups. No coprimality between `a_i` and `b_i` is required.

By quotient/index equivalence, every `a_i` is coprime to `M_T`. For `i!=j`, `d=gcd(a_i,a_j)` divides `gcd(n_i,n_j)<=T`. If `d>1`, a prime `p|d` satisfies `p<=d<=T`, contradicting roughness. Hence `gcd(a_i,a_j)=1`. The intersection result applies to all projected left cosets at once, furnishing a common actual point `q in intersection_i A_i`; no quotient Helly assumption is invoked.

Choose **one** `t in G` with `pi(t)=q`. For every i, `q in pi(C_i)` supplies `x_i in C_i intersect Nt`. Since `pi(x_i)=pi(t)`, an element `x_i u`, `u in U_i`, lies in `Nt` exactly when `u in N`. Thus

`C_i intersect Nt = x_i K_i`, and

`(C_i intersect Nt)t^-1 = (x_i t^-1)(t K_i t^-1)`.

Here `x_i t^-1 in N`; normality of N ensures `t K_i t^-1<=N` and conjugation is an automorphism of N, so this is an actual left N-coset of index `b_i`. Intersecting a disjoint family with the same fibre and applying the same right translation preserves pairwise disjointness. Finally `b_i|n_i` gives `gcd(b_i,b_j)|gcd(n_i,n_j)<=T`. The r+1 kernel cosets therefore contradict the exact predicate `B_T(N)<=r`. This proves the transfer.

For `T=7`, `M_T=2*3*5*7=210`, and `B_7(X)<=7` is the eight-coset predicate specified in the candidate. No original label or coset was discarded, and nothing in the proof requires G or Q to be finite, a split extension, abelian groups, normal `U_i`, a coset cover, or a global Helly property.

### 4. m1 and m2, checked independently

**m1.** The replacement of “Each is finite” with “The indices `a_i`, `b_i` and `n_i` are finite, and `n_i=a_i b_i`” is correct. To exhibit the distinction, let `D=(Q,+)`, `G=D x C2 x D`, `N=D x C2 x {0}` and `U=D x {0} x D`. The two U-cosets have index `n=2`; `G/N` and the projected cosets are infinite, as is `K=U intersect N=D x {0} x {0}`. Here `a=1`, `b=2`. This example only addresses the wording: its N does not satisfy `B_7(N)<=1`, so it is not a theorem counterexample.

**m2.** Let `N=D x C7`, `D=(Q,+)`. If `U<=N` has finite index, `U intersect D` has finite index `d` in D. Since D is abelian, `dD<=U intersect D`; divisibility gives `dD=D`, so `D<=U`. Thus U is the inverse image of a subgroup of C7, hence its index is 1 or 7. The whole-group coset cannot coexist disjointly with another nonempty coset, and there are only seven index-7 cosets, so eight disjoint finite-index cosets do not exist: `B_7(N)<=7`. The seven index-7 cosets are pairwise disjoint and every pair of their indices has gcd 7, so `B_7(N)<=6` fails. This establishes the corrected pair of predicate statements without assigning a value to the undefined expression `B_7(N)=7`.

## Exact residual and imports

The roughness assumption is sufficient, not asserted necessary for Sun8. If Q has a finite quotient whose order is divisible by a prime at most T, this theorem does not apply, and its index-equivalence gives some finite-index subgroup whose index has such a prime factor. In the attempted proof, `gcd(a_i,a_j)<=T` can then be nontrivial: pairwise-coprime projected indices, simultaneous intersection, and the one-fibre reduction no longer follow. This is the first unproved step for arbitrary small-prime quotients, not evidence that a counterexample to Sun8 exists.

For a sharp warning about dropping the roughness assumption from the **general r theorem**, take `T=7`, `r=1`, `N=1`, and `G=Q=C7`. `B_7(N)<=1` is vacuous, but two distinct singleton G-cosets have indices 7 and gcd 7, so `B_7(G)<=1` fails. This is **not** an eight-coset counterexample: C7 has only seven elements, and `B_7(C7)<=7` holds. Thus factor Sun8 alone does not establish quotient roughness, nor does this transfer resolve the remaining mixed-index normal-extension problem.

The proof imports only elementary group axioms and elementary standard results: finite coset actions and their kernels, the first isomorphism theorem, multiplicativity of subgroup indices (including coset-set bijections for nonnormal subgroups), finite Lagrange, elementary gcd/prime arithmetic, and divisibility of `(Q,+)` for m2. It uses no classification, Helly theorem, extension splitting, previous f254 verdict, author code/control result, linked source, f161/f162, held/selected prime-2/3 material, or another reviewer as a mathematical premise. The three parent dispositions were read only as scope-limited comparison inputs and are not theorem premises. Mandatory overlays and the CRT erratum were read before the later erratum and candidate; none enlarges the theorem's hypotheses or conclusion. The old f254 reviews did not receive this later erratum as input; no contrary or retrospective claim is made.

## Frozen inputs and ordered complete reads

The manifest full SHA-256 was verified as `a289243539e3e15200148dbecc14a882030c22704f3f5a7a12924aaa379fb1d2` before opening it. **Before reading any input body**, each of the following nine files was measured against the manifest for full SHA-256, bytes, and LF; all matched, and every file ended in LF. Then every input was read completely in manifest order, including its ending, in raw windows of at most 15 lines. The paths are the full paths pinned in the manifest; row labels below are not substitutes for them.

| # | Manifest role | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| 1 | alternating arithmetic overlay | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 2 | repeated-unit fatal overlay | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 3 | cardinality overlay | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 4 | CRT correction | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 | 12 |
| 5 | later f254 additive erratum | `d95c7cecf5b39e6d6649f1ca0238acf661f79082be4f8ba3a2ceb9757591244b` | 10485 | 181 |
| 6 | f151 comparison scope only | `2ad5691a705089a6d724b2c9f21c075d76d31ddc471448abaa11240bc8d6637f` | 6429 | 30 |
| 7 | f242 comparison scope only | `58992864735e124aabf00654f27b83ac59fc9f279f2848f9d81c1fcd8ae451f3` | 4426 | 24 |
| 8 | f243 comparison scope only | `0a77a4311d9e6059e4c08542e7553d5f8b2c60a25476dec9995bd87aaa30fc08` | 4192 | 24 |
| 9 | unchanged candidate | `0522bf11ac96d7d688b27d1602cf2d11124c8b05c95c0d3b5023b1ffb5476176` | 7914 | 149 |

## Reviewer-owned bounded controls

After all nine complete reads and the written analysis, I ran only my own [`reviewer-A-controls.py`](reviewer-A-controls.py), SHA-256 `608524707225575773965e21dabbd317604b78d82936c9deebd7e76d199e06de`, under a 120-second tool timeout. Native clocks were `2026-10-29T15:34:09-0700 PDT` to `2026-10-29T15:34:10-0700 PDT`; the script measured 0.045539 monotonic seconds. Its real Python exit was 0: the shell's `&&` chain reached the observed END clock only after Python returned zero. The retained [control receipt](reviewer-A-control-receipt.json) has SHA-256 `f822f6b725a9c920d7acb223b9a4c44dde84428d5b7edf69ab802daef2b2b16e`.

The independently generated finite controls enumerated all six S3 subgroups and 12 subgroups of `S3 x C5`. They checked 57 pairwise-coprime subgroup-index tuples, including 42 with a nonnormal subgroup and 17 with repeated unit indices; 12 index-factorization cases; 1,080 fibre identities, including 540 with nonnormal original subgroups; and 630 common-fibre/disjointness checks. For `T=2`, the enumerated `S3` bad-coset graph had seven pairs and no triples, and `S3 x C5` had 77 pairs and no triples; 70 pairs used a nontrivial quotient index. These finite checks corroborate specific orientations and instances, not the arbitrary-group theorem.

Intended-reason negatives: omitting conjugation failed in 360 fibre cases; placing the conjugated subgroup on the wrong side failed in 360; two distinct cosets of a repeated index-2 subgroup gave a missing common tuple; the `N=1, G=C7, T=7, r=1` example falsified transfer with roughness dropped; three `F_11^2` lines met pairwise but not jointly despite the quotient being 7-rough; and `C5 x C5` showed quotient and kernel factors of a single index may both equal 5. No finite control is offered as formal proof, an eight-coset counterexample, or independent-family/human verification.
