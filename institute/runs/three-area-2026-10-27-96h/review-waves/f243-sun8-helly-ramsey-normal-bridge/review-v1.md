# f243 — Helly–Ramsey normal-extension bridge: independent written review

Native `/bin/date` observed before drafting this report: **2026-10-29T14:45:17-0700 PDT**. This is an observation before writing, not an asserted file-creation time.

## Disposition and per-claim verdicts

**Scientific finding: 0 FATAL, 0 MAJOR, 1 MINOR.** At the stated hypotheses, the bridge and the obstruction are supported by the independent reconstruction below. The minor concerns an ambiguous/incorrect-as-a-unique-residue sentence in the finite cyclic CRT discussion; it does **not** invalidate the cyclic Helly claim. The author's historical provenance assertions are **INCONCLUSIVE**, separately from the mathematical assessment.

In the table `0F/0M/0m` means that no fatal, major, or minor defect was found in that claim at its displayed scope; it is not an unrestricted acceptance. `m` identifies the minor finding. `INCONCLUSIVE` is used when the assigned record does not establish a claim.

| Target lines and claim | Verdict | Reason and limit |
|---|---|---|
| 8–13: definition of `B_T(X)≤r`, repeatable subgroups and indices, and `Sun8(X) = B_7(X)≤7` | 0F/0M/0m | The definitions quantify over actual nonempty finite-index left cosets. A larger bad family would contain a bad subfamily of every smaller positive size. No global finite maximum is needed. For the finite examples, `B_7≥k` means explicitly that a bad family of size `k` exists. |
| 39–62: index product, inherited gcd divisibility, and actual fibre identity | 0F/0M/0m | The coset-set product formula works without finiteness of `G` or normality of `U_i`; the common representative must conjugate `K_i`. The original cosets' disjointness survives right translation. |
| 23–29, 64–73: all-variable finite-clique-Helly bridge | 0F/0M/0m | A quotient-overlap clique yields actual kernel cosets; an independent set yields actual quotient cosets. Ramsey gives the stated bound, with no assumption that disjoint original cosets project disjointly. |
| 17–21, 75–83: `R(3,3)=6`, Theorem A, and its Sun8 consequence | 0F/0M/0m | The six-vertex argument proves the needed upper bound; the five-cycle and its complement establish equality. Choosing six of eight gives Sun8. The factor bounds are strictly stronger hypotheses than Sun8. |
| 31–35, 85–90: non-Helly triangle necessity | 0F/0M/0m | Every six-label bad family under the two `B_7≤2` assumptions has an intersecting projected triangle and that triangle has no common quotient point. This is a necessary obstruction, not an existence proof for such a family. |
| 93–100: finite and infinite cyclic quotient Helly | **m** | Pairwise generalized-CRT compatibility does give a common point, for all finite families. But “the resulting solution modulo L is well-defined modulo M because L\|M” is ambiguous: interpreted as a uniquely defined residue of `Z/MZ` obtained from a residue of `Z/LZ`, it is false. Correct wording and a counterexample are below. |
| 103–120: `D_{2p}` and `C_{2q}` factor bounds, and comparison with f151's hypotheses | 0F/0M/0m | For every prime `p,q>7`, each finite factor has exact bad-family maximum 2, using the unique index-two subgroup and the partition argument. `μ(G)=2`, so none of the cited `μ≥8` sufficient cases covers the example. |
| 120–124: lower bound 4, upper bound 5 for the product | 0F/0M/0m | The four cosets of `C_p×C_q` have index 4 and witness the lower bound. The upper bound is conditional Theorem A applied to this product; no sharpness of 5 follows. |
| 129–138: `C_7×C_7` projection and factor-Sun8 shortcut | 0F/0M/0m | Seven actual disjoint index-7 cosets all project to the whole quotient. Both factors satisfy Sun8, but the example is not an eight-coset counterexample. |
| 140–149: `F_5^2` non-Helly quotient example | 0F/0M/0m | The three specified actual line cosets are pairwise intersecting with empty triple intersection; distinct kernel layers make the original cosets disjoint. Their original indices are 25, so the example does not exhibit the six-label gcd-7 obstruction. |
| 151–160: graph-only limitation with Sun8 factors | 0F/0M/0m | Even with full quotient Helly, excluding only an eight-clique and eight-independent-set does not exclude an abstract eight-cycle. The candidate does not claim that cycle is realizable by a bad group-coset family. |
| 164–180, 189–190: author's historical input, exposure, clock, and process-status assertions | **INCONCLUSIVE** | They are self-reports in the target; the author transcript, linked bodies, prior findings and external history were not inputs to this review. They are not used as mathematical premises. The target's statement that the prior PROCESS MAJOR remains binding is not erased by this review. |

## Exact input and reading sequence

1. I opened **only** `manifest-v2.json` first; its initially truncated line 50 was subsequently displayed raw. `manifest-v1.json` was not opened or used. `shasum -a 256` measured v2 as `3ffcfe6f57f8a43fed08931d3cbaaca6a4fae153d18cc8b487cd84f5368c4f8c`, matching the assigned `3ffcfe6f57f8` prefix; `wc -lc` measured 58 LF and 4,590 bytes.
2. Before opening any declared body, one `shasum -a 256` and `wc -lc` command measured **all five inputs**. Every measured SHA-256, byte count and LF count matched v2. The labels below are exact basenames; `D` is `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`, and `E` is `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`.

| Order | Measured input | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| 1 | `D/math-6-sun8-source-free-support-criteria-parent-v1.md` | `2ad5691a705089a6d724b2c9f21c075d76d31ddc471448abaa11240bc8d6637f` | 6429 | 30 |
| 2 | `E/frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 3 | `E/frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 4 | `E/frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 5 | `E/frontier-20261029-helly-ramsey-normal-bridge-v1.txt` | `ba5dae355377f7e63a5426a76177d9bf2a50e9220f5be8a95aea6e28f35cb3e1` | 10994 | 190 |

3. I displayed the complete raw input bodies in manifest order and without reasoning before completion: input 1 at lines `1–15,16–30`; input 2 at `1–15,16–30,31–45,46–56`; input 3 at `1–11`; input 4 at `1–10`; target at `1–15,16–30,31–45,46–60,61–75,76–90,91–105,106–120,121–135,136–150,151–165,166–180,181–190`. Each raw window had at most 15 lines and every last line was displayed. The three overlays preceded the target in their required order.
4. After completing those reads, I read the workspace memory summary and procedural skill instructions. They were not mathematical inputs. No linked source body, held/f161/f162 payload, f184/f188 packet, sibling review, author code, author receipt, external search/model/API, or author contact was used.

**Deviations:** No deviation from the dispatched input order, source scope, or pre-reasoning coverage. The initial metadata-measurement shell call requested a `120000`-second timeout; the tool reported that it clamped this to 3600 seconds, and the command completed. This was not a mathematical control. The separately bounded control below used a 120-second shell deadline and its own 110-second alarm. The memory and skill reads occurred after the source bodies to preserve the manifest-first, measure-first, in-order scientific protocol.

## Independent mathematical reconstruction

### 1. Definitions, indices, and actual fibres

Write `π:G→Q=G/N`, with `N` normal. For a finite-index `U_i≤G`, let `K_i=U_i∩N`, `a_i=[Q:π(U_i)]`, `b_i=[N:K_i]`, and `A_i=π(g_i)π(U_i)`. Since `NU_i` is a subgroup and `π^{-1}(π(U_i))=NU_i`, `[G:NU_i]=a_i`. The coset-set map `nK_i↦nU_i` is a bijection `N/K_i→NU_i/U_i`; this is a bijection of left-coset sets, not an assertion that `K_i` is normal. Consequently `b_i=[NU_i:U_i]` and

`[G:U_i]=[G:NU_i][NU_i:U_i]=a_i b_i`.

These indices are finite even if `G` is infinite. Thus both `gcd(a_i,a_j)` and `gcd(b_i,b_j)` divide `gcd(a_i b_i,a_j b_j)` and are no larger than the original gcd.

For a common quotient point `q∈⋂_{i∈J}A_i`, choose one `t` with `π(t)=q`, and choose `x_i∈g_iU_i∩Nt`. For `y=x_i u`, with `u∈U_i`, we have `y∈Nt` exactly when `π(u)=1`, i.e. `u∈K_i`. Right multiplication by `t^{-1}` therefore gives

`(g_iU_i∩Nt)t^{-1} = (x_i t^{-1})(tK_i t^{-1})`.

Here `x_i t^{-1}∈N`, and `tK_it^{-1}≤N` because `N` is normal; conjugation is an automorphism of `N`, so its index is `b_i`. The displayed set is a genuine **left** coset in `N`. If the original `g_iU_i` are pairwise disjoint, intersections with `Nt` and the same right translation keep them disjoint. Omitting the conjugation is generally wrong. Conversely, when some `A_i` are pairwise disjoint, those `A_i` themselves are actual quotient left cosets of indices `a_i`; their pairwise disjointness was an assumption on the images, not inferred from disjointness in `G`.

### 2. Graph, Ramsey, and the necessary non-Helly triangle

Suppose a finite family of original cosets is pairwise disjoint and all its index gcds are at most `T`. Make its **labels** vertices, putting an edge precisely when the corresponding quotient cosets intersect. Labels remain distinct even if some projected cosets coincide.

Under finite-family quotient coset Helly, a clique of `r+1` has a common point `q`. The fibre construction gives `r+1` disjoint kernel cosets whose index gcds are at most `T`, contradicting `B_T(N)≤r`. An independent set of `s+1` is a collection of disjoint quotient cosets whose index gcds are at most `T`, contradicting `B_T(Q)≤s`. Therefore the graph has neither forbidden monochromatic clique, and ordinary finite Ramsey gives fewer than `R(r+1,s+1)` vertices. This is exactly `B_T(G)≤R(r+1,s+1)-1`. The variables satisfy the target's `T≥2` and positive-integer `r,s` hypotheses.

For six vertices, one vertex has at least three of its five incident edges in the same colour. If any edge between those three neighbours has that colour there is a monochromatic triangle with the chosen vertex; otherwise the three neighbours are a triangle of the other colour. Thus `R(3,3)≤6`. A five-cycle has no triangle and its complement is another five-cycle, so `R(3,3)≥6`. For `r=s=2`, only common intersection of projected triples is needed. The two factor hypotheses and quotient 3-Helly consequently exclude a bad family of six, establishing `B_7(G)≤5`; any bad eight would contain a bad six, proving the stated Sun8 consequence.

Without Helly, the quotient factor bound still excludes an independent triple among six labels. Ramsey then produces an intersecting triple. Were that triple's total intersection nonempty, the common-fibre construction would contradict the kernel factor bound. Therefore this **particular projected triple** has empty total intersection. This localized necessary statement is stronger than merely saying that some triple somewhere in `Q` witnesses failure of 3-Helly; it has its own proof above. It neither constructs a six-label bad family nor establishes the converse implication.

### 3. Cyclic groups and the CRT precision issue

For `Q=Z`, finite-index subgroup cosets are congruence classes `x≡c_i (mod a_i)` with positive `a_i`. For `Q=Z/MZ`, these are the same congruence conditions with each `a_i\mid M`. Two conditions meet iff `gcd(a_i,a_j)\mid(c_i-c_j)`: necessity is immediate, and sufficiency follows from Bézout for the two moduli.

Assume all pairs are compatible. Inductively combine the first conditions into `x≡c (mod L)`, `L=lcm(a_1,…,a_k)`. For the next modulus `a`, pairwise compatibility makes every `gcd(a_i,a)` divide `c-c_{k+1}`. Their lcm is `gcd(L,a)`, as follows prime by prime from `min(max_i v_p(a_i),v_p(a)) = max_i min(v_p(a_i),v_p(a))`. The two-modulus criterion therefore adds the new condition. Induction gives an integer solution for every finite family. In the finite case `L\mid M`; choose any integer solution `c` and take its residue in `Z/MZ`. Each original congruence condition is well-defined on residues modulo `M`, and that residue satisfies all of them. Hence both finite and infinite cyclic groups have the asserted finite-family Helly property.

**Minor finding, target line 100:** the direction of the canonical quotient map is `Z/MZ→Z/LZ` when `L\mid M`, not generally `Z/LZ→Z/MZ`. For `M=6`, `L=2`, the representatives `0` and `2` define the same class modulo 2 but distinct residues modulo 6. There are three solutions modulo 6 to `x≡0 (mod 2)`: `0,2,4`. If the author meant the *congruence predicate or its nonempty inverse-image set* is well-defined modulo `M`, that is correct; if the sentence asserts a unique residue modulo `M`, it is false. Replace it by the explicit choice-of-lift argument above. This issue is local and does not change the theorem.

### 4. Product example for all primes `p,q>7`

Let `N=D_{2p}=⟨r,s:r^p=s^2=1,srs=r^{-1}⟩` of order `2p`, `Q=C_{2q}`, and `G=N×Q`. Then `N×{1}` is normal, `G/(N×{1})≅Q`, and `Q` is cyclic. Both primes are odd. In each factor, Lagrange limits subgroup indices to `1,2,p,2p` or `1,2,q,2q`. Index 1 gives the whole group, so it cannot appear alongside any other nonempty disjoint coset.

In a bad family, at most one index can be divisible by the large prime, because any pair of such indices has gcd at least that prime, which is greater than 7. In `D_{2p}`, an index-two subgroup is the kernel of a surjection to `C_2`; the element `r` of odd prime order must map to the identity, and the only nontrivial such map sends `s` to the nonidentity. Thus the unique index-two subgroup is `⟨r⟩`. In `C_{2q}`, the order-`q` subgroup is uniquely index two. In either group the two distinct cosets of that subgroup partition the whole group. A disjoint family containing both cannot contain any third nonempty coset. If a bad family had three members, at least two of them would have index two, which is impossible by that partition. Thus both factors have `B_7≤2`. Their two index-two cosets are disjoint with gcd 2, so the finite bad-family maximum is exactly 2 in each factor.

Theorem A now yields `B_7(G)≤5` and Sun8. Independently, `H=⟨r⟩×C_q` has order `pq` and index 4 in `G`; its four left cosets partition `G`, and every pair of their indices has gcd 4. Hence a bad family of four exists and `B_7(G)≥4`. This also works when `p=q`; it does not show whether the upper bound 5 is attained. Since `H` is not needed to show the least proper index, note that `⟨r⟩×Q` has index 2, so `μ(G)=2`. The adopted f151 sufficient criteria all require at least `μ≥8`, and do not certify this example. The two disjoint kernel index-two cosets also refute the stronger pairwise-kernel-gcd-`≥8` hypothesis for this kernel.

### 5. Failed shortcuts and remaining gap

* Put `G=C_7×C_7`, kernel the first factor, and take `U={0}×C_7`. The seven cosets `(i,0)+U`, `i∈C_7`, are disjoint, all have index 7, and all project onto `Q=C_7`. The two factors satisfy Sun8 vacuously because neither has eight disjoint nonempty subsets. The fibre over a quotient point contains seven disjoint singleton kernel cosets, so factor Sun8 neither forces projections to be disjoint nor bounds fibre multiplicity by two. This is seven cosets, not a counterexample to an eight-coset implication.
* In `Q=F_5^2`, the affine lines `y=0`, `x=0`, `x+y=1` are left cosets of index-five subgroups. Their pairwise intersections are `(0,0)`, `(1,0)`, `(0,1)`, while their total intersection is empty. In `G=C_5×Q`, put each line on a different first-coordinate layer; the three resulting cosets are disjoint and have index `125/5=25`. Their pairwise gcd 25 is outside the bad-family range. In fact `Q` itself has five disjoint parallel index-five cosets, so `B_7(Q)≤2` fails there. This example proves that arbitrary quotients need not be 3-Helly, not that the theorem's factor hypotheses hold.
* If only `B_7(N)≤7` and `B_7(Q)≤7` are known, even full quotient Helly rules out only an eight-clique and an eight-independent-set in an eight-vertex overlap graph by this argument. An abstract eight-cycle has clique number 2 and independence number 4, so those graph constraints alone do not force a contradiction. It has **not** been shown to arise from actual bad cosets.

**Explicit remaining gap:** Arbitrary quotients need not be 3-Helly, and the factor-Sun8 assumptions are much weaker than the factor bounds 2. An unrestricted extension must control or rule out the remaining non-Helly/incidence patterns by genuine subgroup-index and common-fibre structure, without assuming the missing Helly property or silently replacing `B_7≤7` by `B_7≤2`. No unrestricted Sun8, all-simple-group, or existence/nonexistence result for a six-label obstruction is established here.

## Reviewer-owned exact controls and limits

I wrote `reviewer-exact-controls-v1.py` independently from the stated definitions, using only Python standard-library integer/set arithmetic; it does not import, execute, or read author code or receipts. Its measured SHA-256 is `4692853251e751d10cd82991bb8b43a2a242e3fced6975c2254750eda79abf33`. The native pre-writing clock was observed at `2026-10-29T14:43:29-0700 PDT`. The execution's `/bin/date` observations were **start `2026-10-29T14:44:21-0700 PDT`, end `2026-10-29T14:44:22-0700 PDT`**, with exit code **0**. The 110-second in-script alarm and 120-second shell deadline did not fire; any cap or timeout would have meant UNKNOWN, not exclusion.

* In `D_6×C_2`, it enumerated 16 subgroups and 1,872 nonempty actual fibres over choices of original coset and common representative, checking the index product and the translated conjugated fibre identity. The intended mutation dropping conjugation was rejected specifically as `MISSING_CONJUGATION`.
* It enumerated all labelled graphs on five and six vertices: 12 five-vertex colourings avoid monochromatic triangles and zero six-vertex colourings do. The intended five-vertex false threshold was rejected as `NO_MONOCHROMATIC_TRIANGLE`.
* For `M=1,…,12`, it checked 45,777 four-label finite cyclic congruence families, 2,134 pairwise compatible, against actual global residues. An incompatible congruence pair was rejected as `PAIR_CONFLICT`; attempting the reverse unique class map in `M=6,L=2` was rejected as `NO_UNIQUE_LIFT`. These finite controls do not replace the CRT proof for arbitrary moduli or family sizes.
* For `p=q=11`, it enumerated 14 subgroups/146 subgroup-cosets in `D_22` and 4/36 in `C_22`; each had 23 bad pairs and no bad triple. In `D_22×C_22` it checked the order-121 subgroup and four disjoint index-four cosets covering the order-484 product. These are illustrations, not a proof for arbitrary primes.
* The `C_7×C_7` and `C_5×F_5^2` constructions were checked as finite sets. Targeted shortcut mutations failed for the intended reasons `PROJECTED_OVERLAP`, `FIBRE_EXCEEDS_TWO`, and `NON_HELLY_TRIANGLE`.

## Explicit imports and review boundaries

I use only the target's definitions and assumptions, elementary group/coset counting including Lagrange for the finite example, Bézout and integer gcd/lcm facts, finite Ramsey/pigeonhole reasoning, and elementary facts about finite cyclic and dihedral groups; the needed Ramsey and CRT arguments are reconstructed above. From adopted f151 I use only its expressly displayed **scope**—in particular that the compared sufficient criteria require `μ≥8`—not its linked proofs, review outcomes, or any additional theorem. The three overlays were read as required but no alternating-group result, withdrawn assertion, or other linked body is imported. Author-reported PASS lines, scripts, receipts, solver outputs and sibling reviews are not evidence in this review.

This is a **same-harness** scientific review, not human review, independent-model-family review, formal proof or kernel verification, and not a novelty or priority assessment. Parent disposition and integration remain separate. The report's final SHA-256 is supplied in the reviewer reply, not embedded here.
