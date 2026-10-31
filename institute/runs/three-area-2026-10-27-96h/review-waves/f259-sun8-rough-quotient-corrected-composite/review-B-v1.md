# f259 corrected rough-quotient composite — slice B review

**Reviewer:** ReviewF259RoughExamples, same harness. **Native clock observed before writing:** 2026-10-29T15:30:50-0700 PDT. **Scope:** corrected m3, m4 and m5; the example quantifiers and the precisely supplied f151/f242/f243 interfaces. This is not a review of the universal transfer proof, m1/m2 as such, provenance, novelty, or any historical disposition.

## Verdict and dependency table

Within the assigned examples and comparisons I found **0 FATAL / 0 MAJOR / 0 MINOR**. The following `F/M/m/I` counts distinguish supported claims from `INCONCLUSIVE` stand-alone conclusions. A zero is a finding count, not a claim of human, independent-family, formal, kernel or novelty verification.

| Claim reviewed | F/M/m/I | Disposition |
|---|---:|---|
| m3: every extension `1 -> (Q,+) x C7 -> G -> F_p^2 -> 1` splits, **for every prime p>7 and every such abstract extension** | 0/0/0/0 | Written argument below supports the stated universal split claim; this is not a split hypothesis for the transfer theorem. |
| m4: conditional nonabelian quotient family, and the specific `p=23,q=11` rough quotient | 0/0/0/0 | Supported with the exact prime and action arithmetic below. The general family is conditional on primes satisfying `q | p-1`; the explicit pair is a witness, not a claim about how many pairs exist. |
| m4: the displayed `C23 semidirect C121` extension is central over `C11` and nonsplit | 0/0/0/0 | Supported by an explicit quotient map and all eleven relevant lift powers below. This is one particular example, not a universal nonsplitting claim. |
| m4: `B_7(C11)<=1`, and the resulting application of the transfer theorem at r=1 | 0/0/0/1 | The kernel predicate and the example's quotient hypotheses are supported. The **universal transfer theorem itself was outside this slice**, so its r=1 conclusion is conditional on that theorem; `I` is not a finding of a counterexample. |
| m5: rational/C7 kernel predicates and f242 `J_7`/r+s comparison | 0/0/0/0 | Supported for the stated kernel and `F_p^2`, conditional on the literal f242 bridge supplied in the disposition. It does not exclude other applications or arguments. |
| m5: f243 global Helly-premise comparison | 0/0/0/0 | The explicit affine triangle refutes the stated global premise, not Sun8 or a low-gcd original configuration. |
| m5: f151 comparison | 0/0/0/0 | Its four displayed criteria do not directly apply to the specified infinite G; the finite-group domain and `mu=7` qualifications are stated separately below. |
| Candidate's general arbitrary-kernel transfer theorem, and use of it to draw example conclusions | 0/0/0/1 | **INCONCLUSIVE in this slice:** the proof of the universal theorem is not adjudicated here. All example applications below are explicitly conditional on it. |

The f151/f242/f243 dispositions are used **only as the exact comparison statements supplied**, not as independently re-proved source bodies. In particular, no earlier f254 review, other reviewer result, author program or claimed PASS is a premise. The later erratum was not an input to the historical reviews; this review does not transfer its content into them.

## m3 — every extension in the rational/C7 family splits

Write `D=(Q,+)` and `N=D x C7`. An additive homomorphism `D -> C7` is zero since D is divisible; a homomorphism `C7 -> D` is zero since D has no torsion. An endomorphism of D is multiplication by its rational value at 1. Therefore

`Aut(N) = Q^* x Aut(C7)`, with `Aut(C7)` of order 6.

The only finite-order elements of `Q^*` are `1,-1`; hence this automorphism group has no element of order p for p>7. Because N is abelian, conjugation gives a well-defined homomorphism `G/N = F_p^2 -> Aut(N)`. Its image has exponent dividing p, so it is trivial. Thus **N is central** in every extension under this exact hypothesis.

Multiplication by p is bijective on both D and C7, and N has no p-torsion. Choose lifts x,y of a basis of `F_p^2`. Their pth powers lie in N. Multiply x and y by central pth roots of the inverses of those powers, obtaining `x^p=y^p=1`. The commutator `[x,y]` lies in central N, so `[x,y]^p=[x^p,y]=1`; p-torsion-freeness gives `[x,y]=1`. The commuting adjusted lifts generate a copy of `F_p^2`: their images form a basis, so the generated subgroup intersects N trivially. This is a section. Since N is central, the extension is in fact equivalent to the direct product with the given kernel and quotient.

This is a universal result for the **specific** kernel/quotient family, not a statement about arbitrary kernels or quotients. In particular, the candidate's general theorem is not restricted to split extensions; the separate m4 witness below is nonsplit. Conversely, the existence of that witness does not make any extension in the rational/C7 family nonsplit.

For the kernel predicate used by m5, if H has finite index d in N, then `D/(D cap H)` has order at most d, and D has no proper finite-index subgroup: multiplication by any positive integer is surjective. Hence H contains D. The finite-index cosets are the pullbacks of the seven singleton cosets or the whole coset in C7. There are seven disjoint index-7 cosets and no eight disjoint nonempty cosets. Thus the exact predicates are `B_7(N)<=7` and **not** `B_7(N)<=6`; no undefined numerical `B_7(N)=7` is needed.

## m4 — explicit nonabelian, nonsplit application

For primes p,q>7 with `q | p-1`, `F_p^*` has order p-1; by Cauchy's theorem it has an element of order q. Its multiplication action gives the nonabelian quotient `C_p semidirect C_q` of order pq. Every finite quotient has order dividing pq, so it is 7-rough. This argument is for every pair satisfying the stated hypotheses, not an assertion that every pair of primes does so.

For the explicit pair, 23 and 11 are prime, `11 | 22`, and `2^11=2048=23*89+1`. Since 2 is not 1 mod 23 and 11 is prime, it has exact order 11 in `F_23^*`. Let

* `G=C23 semidirect_2 C121`, with elements `(a,b)` and multiplication `(a,b)(c,d)=(a+2^b c, b+d)` modulo 23 and 121;
* `Q=C23 semidirect_2 C11`; and
* `pi(a,b)=(a,b mod 11)`.

The map is a homomorphism because `2^11=1 mod 23`, and is onto. Its kernel is exactly `N={(0,11k): k mod 11} = <y^11>`, of order 11. It is central because `2^11=1` and the C121 coordinate is abelian. The quotient is nonabelian because conjugation by `(0,1)` sends `(1,0)` to `(2,0)`.

Every lift of the particular quotient element `(0,1)` is **exactly** `(0,1+11k)` for `k=0,...,10`. Its eleventh power is `(0,11+121k)=(0,11)`, which is not the identity modulo 121. A section would send this order-11 quotient element to an element whose eleventh power is the identity, impossible. Thus this extension is genuinely nonsplit. The quotient has order `23*11=253`, coprime to 210.

For `N=C11`, a pair of disjoint nonempty cosets cannot contain the whole-group coset; both must have index 11, hence gcd 11>7. So `B_7(N)<=1`. The written transfer conclusion for this example at r=1 is **conditional on the separate universal theorem**; no inference that all arbitrary extensions split or are nonsplit is made.

## m5 — exact limited comparison interfaces

* **f242.** Every subgroup of the additive vector space `F_p^2` is a vector subspace. Proper-subgroup indices are p or p², so any two proper labels, including repeated labels, have gcd at least p>7. Hence `J_7(F_p^2)<=1`; `J_7(F_p^2)<=0` fails because a proper subgroup exists. With the stated f242 bridge and the actual kernel predicate above, the direct substitution `r=7,s=1` yields `B_7(G)<=8`: it addresses nine disjoint cosets, whereas Sun8 requires the bound `B_7(G)<=7` for eight. This is a statement about that **single direct substitution**, not proof that no alternative f242 application or proof yields Sun8. The bridge itself is taken only from the scoped f242 disposition.
* **f243.** In `F_p^2`, the cosets `x=0`, `y=0`, `x+y=1` each have index p. Their pairwise intersections are `(0,0)`, `(0,1)`, `(1,0)` as appropriate, and the total intersection is empty. Thus the global 3-Helly premise of the stated f243 sufficient theorem fails; the finite-clique Helly premise also fails. The pairwise index gcd is p>7, so the triangle is **not** an original low-gcd counterconfiguration. No inference about other f243 methods is made, and the separately supplied f243 cyclic-CRT correction remains in force.
* **f151.** The displayed `G=D x C7 x F_p^2` is infinite, while the four f151 criteria are stated for **finite** groups. Independently, every finite-index subgroup of G contains D, and the resulting finite quotient `C7 x F_p^2` has order `7p²`; every finite proper index divides that order and is at least 7. Projection onto C7 supplies index 7. Therefore `mu(G)=7`, and the finite quotient also has minimum proper-subgroup index 7. All four displayed f151 sufficient criteria require `mu>=8` or `mu>=13`; those hypotheses also fail. The missing finiteness is a domain qualification, not a claimed mathematical defect in the narrow comparison. Neither observation rules out a different method or claims novelty.

For the candidate's boundary statement, take the separate example `G=Q=C7`, `N=1`. Both factors satisfy `B_7<=7`, while Q itself is a finite quotient of order 7 and is not 7-rough. This witnesses that the rough premise is not implied by arbitrary factor Sun8; it is not an eight-coset counterexample.

## Frozen inputs and read coverage

Manifest SHA-256 measured first: `a289243539e3e15200148dbecc14a882030c22704f3f5a7a12924aaa379fb1d2`. Before reading any input body I measured all nine complete files; each matched its declared full SHA-256, byte count and LF count. I then read every input completely in the following manifest order, in raw windows of at most 15 lines each, including each ending. The later erratum preceded all three scope-only dispositions and the unchanged candidate.

| Order / role | Full SHA-256 | Bytes / LF |
|---|---|---:|
| Alternating arithmetic overlay 1 | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 / 56 |
| Alternating fatal overlay 2 | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 / 11 |
| Alternating cardinality overlay 3 | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 / 10 |
| f243 CRT correction | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 / 12 |
| Later five-minor erratum | `d95c7cecf5b39e6d6649f1ca0238acf661f79082be4f8ba3a2ceb9757591244b` | 10485 / 181 |
| f151 disposition, m5 interface only | `2ad5691a705089a6d724b2c9f21c075d76d31ddc471448abaa11240bc8d6637f` | 6429 / 30 |
| f242 disposition, m5 interface only | `58992864735e124aabf00654f27b83ac59fc9f279f2848f9d81c1fcd8ae451f3` | 4426 / 24 |
| f243 disposition, m5 interface only | `0a77a4311d9e6059e4c08542e7553d5f8b2c60a25476dec9995bd87aaa30fc08` | 4192 / 24 |
| Unchanged candidate | `0522bf11ac96d7d688b27d1602cf2d11124c8b05c95c0d3b5023b1ffb5476176` | 7914 / 149 |

No linked source, held/selected prime-2/3 payload, f161/f162, f254 review body/verdict, other review result, external model/API, or Git was used. No historical HOLD, ZERO or provenance status is changed.

## Reviewer-owned bounded controls and limits

After the complete reads and written analysis, I ran only `reviewer-B-control.py`, SHA-256 `08c430a57824fb91b728c12a6709888cee6c7000cb45f2d3be33cb4a05053df4` before and after execution. The native clocks were 2026-10-29T15:30:45-0700 PDT at start and end; monotonic elapsed 0.034512 s, timeout 120 s, actual exit 0. Full stdout/stderr, exact interpreter and timing are in `reviewer-B-control-receipt.json`, SHA-256 `4e569b423c8c0e0ecd2c9a87805e56a959cd38202862bdae6bbd8927224de2ec`.

The controls enumerated C7 cosets, the affine planes and proper subgroups for p=11 and 23, a twisted-coordinate **finite** central model with a 529-element corrected section, and all 2,783 elements of the explicit semidirect example for the quotient/kernel/lift checks. The example has 253 quotient elements, 11 kernel elements and 11 lifts of `(0,1)`, each with eleventh power `(0,11)`; the quotient homomorphism was checked against three generators on each enumerated group element, not by claiming an exhaustive general proof. Intended-reason negatives exercised `B_7(C7)<=6`, `J_7<=0`, loss of p-invertibility (`C49 -> C7`), loss of the automorphism restriction using a **different** kernel, the f151 `mu>=8` threshold, global 3-Helly, a hypothetical splitting lift, and a strict-gcd-threshold mutation. All eight were rejected for their named intended reasons in the receipt.

These finite controls are consistency checks of particular instances and boundary mutations. They do **not** establish the universal rational-kernel splitting theorem, the universal transfer theorem, novelty, formal correctness, or independent-family/human review; those require the written reasoning and separately scoped review.
