# f262 slice A — independent written review

Native `/bin/date` observed before creation: `2026-10-29T15:41:14-0700 PDT`.

**Disposition, on the exact conditional mathematical claims below: FATAL 0 / MAJOR 0 / MINOR 0.** The specified universal arguments are supported by the reconstruction below; the finite controls are checks, not their proof. The existence or exclusion of a triangle satisfying the T=7 factor-bound/fiber conditions is **INCONCLUSIVE**. This is a same-harness review, not independent-family, human, formal/kernel, priority/novelty verification or parent adoption.

## Frozen inputs and exposure

Manifest `manifest-v1.json`: SHA-256 `fa7c1dc175cab440eda3e3fc2ce70f2c6f4107c52cc97d6c996cf795076affca`, verified before reading it. Before any source-body read, every input below matched its listed whole-file SHA-256, byte count and LF count. All had a trailing LF and zero CR bytes. I displayed each complete file in listed order in raw windows of at most 15 LF lines, including both candidate endings, before undertaking mathematics.

| Order / role | Complete LF | Bytes | SHA-256 |
|---|---:|---:|---|
| Alternating overlay 1 | 1–56 | 6883 | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` |
| Alternating overlay 2 | 1–11 | 3056 | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` |
| Alternating overlay 3 | 1–10 | 3164 | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` |
| f243 CRT correction | 1–12 | 2329 | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` |
| f253 gcd correction | 1–25 | 2825 | `c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3` |
| **Target A**, `frontier-20261029-nonhelly-slice-capacity-obstruction-v1.txt` | 1–174 | 9144 | `5365b7b6b7713ff4b500b8186ed556615d1f45de7920545be100711bad3adc7e` |
| Target B, `frontier-20261029-six-coset-nonabelian-nonhelly-v1.txt` | 1–170 | 8822 | `bba2c656d770e13d37d576dcca9fc25366080c1cfff2d1704115658f5fc5c6d7` |

Target B was required to be read, but is **not a premise** for this review. No linked body, author checker or PASS, prior review, sibling conclusion, held/f161/f162/selected prime-2/3 payload, external model/API, or Git was consulted. The listed overlays retain their corrections and historical boundaries; none is used to import an unproved theorem. Claims concerning the author's previous work or exposure are not independently certified by this review.

## Per-claim verdicts

| Target A claim | Verdict | Reason / exact scope |
|---|---|---|
| LF 13–43: slice lemma for actual left cosets, arbitrary Q, no normality or requirement that the other two cosets meet | **SUPPORTED; F0/M0/m0** | Sections 1–2 below reconstruct every intersection, index and pairwise gcd, including `d=s` and `d=1`. |
| LF 45–52: `h_j` divides `a_j` if `V_1` is normal and hence the stated weaker inequality | **SUPPORTED; F0/M0/m0** | Product subgroup and coset-index argument below; an S3 counterexample shows the divisibility cannot simply be used without normality. |
| LF 56–76: quotient/kernel index factorization, actual conjugated fibers, and intersecting-pair bound (3) | **SUPPORTED; F0/M0/m0** | Section 3 proves these for finite-index subgroups even when G, N or Q is infinite. |
| LF 78–85: pairwise-coprime finite-index cosets have a common point; a non-Helly triangle has a nonunit quotient-index gcd | **SUPPORTED; F0/M0/m0** | Section 4 proves the full simultaneous intersection claim, not merely pairwise intersection. |
| LF 88–110: under `B_T(Q)<=2`, the three restrictions and slice inequalities, including index-2 elimination | **SUPPORTED; F0/M0/m0** | Section 5 proves each case and retains the original low-gcd and pairwise-intersection assumptions. |
| LF 112–120: six original low-gcd cosets and **both** factor bounds `B_T<=2` imply the stated non-Helly triangle restrictions | **SUPPORTED; F0/M0/m0** | Section 6 separately reconstructs Ramsey, inherited quotient gcds and the common-fiber contradiction. |
| LF 121–144: the consequence is necessary, not existence, exclusion, the original factor-Sun8 result, or unrestricted Sun8 | **SUPPORTED; F0/M0/m0** | The strictly stronger factor hypotheses are indispensable to the displayed proof. The exact T=7 existence/exclusion gap remains open here. |
| LF 127–134 and 145–174: other unreviewed packet/status/provenance assertions | **INCONCLUSIVE** | Not a mathematical input; no linked sources or prior reviews were opened, and no historical hold is cleared. |
| Existence or impossibility of the T=7 necessary triangle with actual original disjoint fibers and both factor bounds | **INCONCLUSIVE** | Neither the displayed numerical restrictions nor these finite checks settle realizability or exclusion. |

## 1. Actual LEFT slices and every gcd

Let `Q` be any group, `T>=2`, `s>=1`, `B_T(Q)<=s`, and let `A_i=x_i V_i` with each `V_i` finite-index. Suppose `A_1` meets `A_2` and `A_3` and their triple intersection is empty; there is no need to assume `A_2` meets `A_3`. Choose `w_j` in `A_1∩A_j`. Since `w_j` is a common point of two **left** cosets, `A_1=w_j V_1` and `A_j=w_j V_j`, so exactly

`D_j=A_1∩A_j=w_j (V_1∩V_j)`.

The two nonempty `D_j` are disjoint, since any shared point would be in the triple intersection. Write `d=[Q:V_1]` and `h_j=[V_1:V_1∩V_j]`. The intersection has finite index: the natural map of `Q/(V_1∩V_j)` into `(Q/V_1)×(Q/V_j)` is injective. Index multiplication then gives `[Q:V_1∩V_j]=d h_j`; this does not assume either subgroup normal.

There are exactly `d-1` other left cosets of `V_1`, and these are disjoint from `A_1` and one another. Together with `D_2,D_3`, they form `d+1` actual pairwise-disjoint left cosets. Between two complementary cosets the index gcd is `d`; between a complement and either slice it is also `d`; and between the two slices it is `d gcd(h_2,h_3)`. Statements involving a nonexistent pair are vacuous when `d-1<2`. Because `d` divides the slice-pair gcd, if `d gcd(h_2,h_3)<=T` **every** pair in the family has index gcd at most T. When `d>=s`, the family contains `s+1` members, contradicting `B_T(Q)<=s`. Thus

`d gcd(h_2,h_3)>T`.

This includes the boundary `d=s`, where there are exactly `s+1` members; the proof must not require `d>s`. It also handles `d=1,s=1` with no complement cosets. The construction only needs finitely many cosets of `V_1`, not a finite group Q.

The condition cannot simply be dropped: in `S3`, take `T=7,s=6`, `V_1=<r>` of order 3, `A_1=V_1`, `V_2=V_3={e}`, `A_2={e}`, and `A_3={r}`. The predicate `B_7(S3)<=6` holds because seven nonempty disjoint subsets of a six-element group are impossible. Here `d=2<s`, `h_2=h_3=3`, and `d gcd(h_2,h_3)=6<=7`. This example is for the lemma, which does **not** require `A_2∩A_3` to be nonempty.

## 2. Normality is specific to the divisibility step

If `V_1` is normal, `V_1V_j` is a subgroup. The map from the `V_1∩V_j` left-coset set in `V_1` to the `V_j` left-coset set in `V_1V_j` is a bijection. Hence

`a_j=[Q:V_j]=[Q:V_1V_j] [V_1:V_1∩V_j]=[Q:V_1V_j] h_j`.

Thus `h_j|a_j` and `gcd(h_2,h_3)|gcd(a_2,a_3)`, so the strict slice inequality implies `d gcd(a_2,a_3)>T`. No normality was used to obtain the slice inequality itself. Conversely, in `S3` let `V_1` and `V_2` be two different order-2 subgroups. Then `h_2=2` and `a_2=3`, so `h_2` does **not** divide `a_2`. Normality is a sufficient condition for this step, not an asserted necessary condition in every special case.

## 3. Original cosets, common fibers, and inequality (3)

Let `N` be normal in any group `G`, `Q=G/N`, and `C_i=g_i U_i` be disjoint actual left cosets with `[G:U_i]=n_i<infinity`. Set `V_i=pi(U_i)`, `A_i=pi(C_i)`, `a_i=[Q:V_i]`, and `b_i=[N:N∩U_i]`. Since `NU_i` is a subgroup, `[G:NU_i]=a_i` and `[NU_i:U_i]=b_i`, whence `n_i=a_i b_i`. All indices are finite: in particular, the left-coset map of `N/(N∩U_i)` into `G/U_i` is injective. Neither G nor N nor Q need be finite.

If `A_i` and `A_j` meet, take a common quotient point `pi(t)` and choose `x_i` and `x_j` in their respective original cosets over it. Because `N` is normal, their common fiber is `Nt=tN=x_i N=x_j N`. For each label,

`(C_i∩Nt)t^{-1}=(x_i t^{-1}) (t(U_i∩N)t^{-1})`,

an actual **left** N-coset, with index `b_i`; conjugation by t is an automorphism of N. The two translated cosets are disjoint. Their indices cannot be coprime: the two-subgroup special case of Section 4 would otherwise force a common point. Thus `gcd(b_i,b_j)>=2`.

Now `gcd(a_i,a_j) gcd(b_i,b_j)` divides both `a_i b_i` and `a_j b_j`, even if the two gcd factors share primes. If the original pair has `gcd(n_i,n_j)<=T`, the product is at most T, so

`gcd(a_i,a_j)<=floor(T/2)`.

This sharper bound applies to **intersecting** images. For an arbitrary pair, including disjoint images, only `gcd(a_i,a_j)|gcd(n_i,n_j)` and hence the upper bound T are inherited. The conjugation cannot be deleted in general; the final S3×C2 control checks a concrete case where the translated fiber subgroup changes.

## 4. Why a nonunit quotient gcd is forced

For finitely many finite-index subgroups `V_i` of any group X, put `H=∩V_i`. The map `X/H -> product_i X/V_i`, `xH -> (xV_i)_i`, is injective. Its domain index is divisible by each `[X:V_i]` by index multiplication and is at most their product. If those indices are pairwise coprime, their lcm is the product, so the two finite cardinalities are equal and the injection is surjective. Every specified tuple of left cosets therefore has a common point.

Consequently, a pairwise-intersecting triple with empty total intersection cannot have all three pairwise index gcds equal to 1. At least one is >1. This does **not** say every pair gcd is >1. For example, in S3 with `r^3=s^2=e, srs=r^{-1}`, the actual cosets `<r>`, `<s>`, and `s<r s r^{-1}>={s,r}` have pairwise intersections `{e}`, `{r}`, `{s}` and empty triple intersection; their indices are `2,3,3` and gcds `1,1,3`. This is only a general coset illustration, not an example satisfying the T=7 strict factor hypothesis.

## 5. The strong-factor triangle proposition

Assume three original cosets are pairwise disjoint, their original-index gcds are all at most T, `B_T(Q)<=2`, and their actual images form a non-Helly triangle. Section 3 gives all three quotient-index gcds at most `floor(T/2)`; Section 4 gives at least one >1.

For any vertex i, `a_i=1` would make `A_i=Q`; the other two images intersect, giving a triple point. If `3<=a_i<=T`, three distinct left cosets of its subgroup have pairwise gcd `a_i<=T`, contradicting `B_T(Q)<=2`. If `a_i=2`, the subgroup has index 2 and is normal. For the two other labels j,k, Section 2 yields `h_j|a_j` and `h_k|a_k`, while the intersecting pair j,k has `gcd(a_j,a_k)<=floor(T/2)`. Thus

`2 gcd(h_j,h_k)<=2 floor(T/2)<=T`.

The slice lemma with `d=s=2` instead says this quantity is >T. Hence all three `a_i>=T+1`. At each vertex the full slice inequality also follows, now with `d=a_i>=2`; no normality is assumed for this general conclusion.

For T=7, the resulting quotient indices are all at least 8, their pairwise gcds are at most 3, and at least one gcd is 2 or 3. These are necessary conditions only. For the separate thresholds T=2 or T=3 the restrictions themselves do prove nonexistence of such a triangle under the stated hypotheses: every pair gcd is at most 1, contradicting Section 4. No analogous T=7 exclusion follows from that argument. The numerical tuple `(8,10,21)` obeys the three displayed T=7 index restrictions, but it is **only arithmetic**; it does not supply a group, cosets, fiber disjointness, the h-values, or either factor bound.

## 6. Six-label Ramsey and the original Sun8 boundary

Assume six actual original cosets are disjoint with all original-index gcds <=T, and **both** `B_T(Q)<=2` and `B_T(N)<=2`. Give the six labels an edge when their actual quotient images intersect. There can be no independent triple: three pairwise-disjoint quotient cosets would have all pairwise quotient-index gcds <=T because each `a_i|n_i`, contradicting the quotient bound.

There is therefore an overlap triangle. Indeed, from one vertex, at least three of the other five are all neighbors or all nonneighbors. In the neighbor case at least one pair among those three is adjacent, or they would be an independent triple; in the nonneighbor case all three must be pairwise adjacent, or the original vertex and a nonadjacent pair would be an independent triple. Either case supplies the triangle.

If its three quotient cosets had a common point, Section 3 would give three disjoint actual N-cosets in that fiber. Their indices `b_i` divide the respective `n_i`, so all their pairwise gcds are <=T, contradicting `B_T(N)<=2`. The overlap triangle is thus non-Helly, and Section 5 applies. This does not prove the six-original-coset configuration exists or fails to exist.

For T=7 the original factor Sun8 hypothesis is `B_7(Q)<=7` and `B_7(N)<=7`, **not** `<=2`: the former only governs families of eight, whereas this argument uses three at both steps. As a self-contained separation, `Q=C2×C2` has `B_7(Q)=4`: four singleton cosets have index 4 and pairwise gcd 4, and five disjoint nonempty cosets cannot fit into four elements. Hence `B_7(Q)<=7` holds but `B_7(Q)<=2` fails. This reviewer-derived illustration is not Target B and does not provide a six-label original-family witness.

## 7. Reviewer-owned exact controls, final stage only

`reviewer-A-controls-v1.py` SHA-256 `93f95370370f3baf57f824a93e91e0130c9fc39745971cfc7fb8a6f1ce4d4634`; receipt `reviewer-A-control-receipt-v1.json` SHA-256 `57d2c0993c15f417674c4e669d3bd2afecd83401cbd999820ca9fb4192559ef5`; stdout SHA-256 `67ed17fa26548aae53617dfd3449708798758663adf1f9b76fd20e6de595541a`. Native clocks before/after: `2026-10-29T15:40:29-0700 PDT` / `2026-10-29T15:40:29-0700 PDT`; monotonic elapsed `0.085312 s`, timeout 120 s, real exit `0`, empty stderr, `CONTROLS_OK`.

The independent finite checks enumerate all 18 actual S3 cosets: 632 qualifying slice triples, all left orientations and all family gcds, with a realized `d=s=2` boundary; the intended negative without `d>=s` is `T=7,s=6,d=1,h=(3,3)`, slice gcd 3. The same control finds `h=2` not dividing `a=3` for nonnormal S3 subgroups, and a non-Helly `3,2,3` triple with only one nonunit pair gcd. It checks all 16 subgroups and 74 cosets of S3×C2, 112 nonempty fibers and 1,616 disjoint common-fiber pairs, including a negative where omitting conjugation changes the fiber; 1,586 qualifying low-gcd pairs satisfy the required bound. The arithmetic check covers 4,189 qualifying small quadruples, including shared-prime factors. The independently enumerated V4 control has exact `B_7=4` and an actual pairwise-overlapping non-Helly triangle; it is not an original-factor-`<=2` witness. Finally all 32,768 six-vertex graphs satisfy the Ramsey dichotomy, whereas 12 of 1,024 five-vertex graphs have neither kind of triangle. These finite results do not prove arbitrary-group claims or settle the T=7 existence gap.
