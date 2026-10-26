# P24 matched primary-source comparison v1

## 1. Status decision and review boundary

Owner: PhysicsResearch96h. This is the parent's bounded cross-domain source/status assignment, not a transfer of P24 ownership. The observed preparation clock was `2026-10-23T14:32:52-07:00` from `/bin/date -Iseconds`; it is not an estimate of an earlier record's creation time.

**Finding: an exact, publicly registered prior claim covers BOTH P24 and its P33 reserve.** Alper Ferudun's *Open Sets of Linear Systems with n = mp That Are Not Stabilizable by Static Output Feedback: New Cases of a Problem of Eremenko*, version 1.0, dated 3 October 2026, explicitly claims the same ordinary-open-family negative conclusion for `(m,p)=(2,4)/(4,2), n=8`, and for `(3,3), n=9`. The paper also supplies the same real-basepoint-free/possibly-complex-degenerate robustness bridge and a complex-curve/Hermitian-rank mechanism. This is not just a paper omitting some pole configurations.

Primary record: <https://eulersolve.org/papers/amr-036-0044/>.

Primary manuscript: <https://eulersolve.org/papers/amr-036-0044/paper.pdf>.

DOI: <https://doi.org/10.5281/zenodo.23127063>.

The public manuscript and its own verification report are **unrefereed and AI-assisted**. I did not run its certificates, reconstruct its entire proof, authenticate its numerical or exact-program outputs, or accept its claimed theorems. A matched public claim is sufficient to defeat an unqualified assertion that this case is unclaimed or that our candidate newly resolves it; it is not sufficient to label the case mathematically settled.

The earlier mathematical bridge review of our packet remains a written check at its stated boundary. This source collision does not itself find a mathematical defect in that packet. The operative additional status is **PRIOR-CLAIM COLLISION; NOVELTY/PRIORITY NOT CLEARED**, not a retrospective clean novelty pass and not acceptance of the external proof.

## 2. Exact local comparison pin

Local author packet, read in full for the earlier bridge review and used again for this comparison:

`/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-SOF24-rational-inner-candidate-v1.md`

Current SHA256 observed with `shasum -a 256`:

`267d717cd735537ff8c29a3c73a17ed7fb1f7939c85788a8cbd60374f74ab8a0`.

Our earlier reconstruction is `peer-review-P24-stabilization-bridge-v1.md` in this slot, SHA256 `70d5380397341f0f2ee94339bbfc8376adafa0573157de96f2153694c37dca80`. Its 0F/0M/0m written mathematical return did not certify novelty, source priority, formal verification, or the external paper.

## 3. Dates: manuscript labels versus actual registry metadata

The following are separately observed source fields, not inferred elapsed times:

| Object | Actual retrieved fields | What these do and do not establish |
|---|---|---|
| EulerSolve primary page and `metadata.json` | Manuscript date, first public online release, modification date: `2026-10-03`; version `1.0`; status `unrefereed preprint`; DOI `10.5281/zenodo.23127063` | Publisher/author assertions of release/version/status. They are not peer review. |
| DataCite DOI API | `created`, `registered`, and `updated` all `2026-10-03T20:38:13.000Z`; `Issued` date `2026-10-03`; version `1.0`; type `Preprint`; exact matching title, author, abstract and cases | Independently returned registry metadata predates this 23 October round. This is stronger than relying only on a date typeset in a PDF. It does not prove the mathematics or by itself audit every historical byte of the manuscript. |
| Current Eremenko problem PDF | Header `October 3, 2026` | Actual current author-file date, not evidence that the underlying problem was first posed in 2026 or that no later public claim exists. |
| Current AIM 319 inventory | `OPEN`, `Last checked: 2026-09-17`; identifies Eremenko's underlying formulation as 20 October 2010 | Its explicit search cutoff precedes the registered 3 October claim. It cannot override that later matched claim. |

Metadata URLs actually read:

- <https://eulersolve.org/papers/amr-036-0044/metadata.json>
- <https://api.datacite.org/dois/10.5281/zenodo.23127063>

The publisher metadata reports PDF SHA256 `9c811e1584896c3869998a96386488d3c69bbb2b4df3f022dff091f9ef4a8394`, source archive SHA256 `7e6504cae570eff2a764d5329ac36681cdedddf53b9681a9855aa1723ae07ac9`, and verification-report SHA256 `29ed7cc8a387cc225cc1e94295cf0f8b04b32b0422900a6838a941c30b91211c`. These are **publisher-reported pins**, not locally recomputed download hashes. No external witness or program was executed.

## 4. Full relevant prior-claim assumptions and quantifiers

Ferudun uses **p inputs, m outputs**, with

- `A in R^(n x n)`, `B in R^(n x p)`, `C in R^(m x n)`;
- arbitrary real **constant** feedback `K in R^(p x m)`;
- closed-loop matrix `A+BKC`;
- continuous-time Hurwitz stability, with all eigenvalues having strictly negative real part;
- ordinary Euclidean topology on the entire space `S_(m,p,n)` of real triples, not only a polynomial-curve ansatz or a gain-bounded subset.

For P24 this is `n=8`, `p=4`, `m=2`, hence ordinary plant space `R^112`. Transposition supplies the reversed port pair. A negative conclusion means there exists a **nonempty open subset U** such that for **every** triple in U and **every** real constant gain K, `A+BKC` is not Hurwitz. It does not mean all plants fail: a Hurwitz A with K=0 is always a positive plant.

### Theorem 1.1, exact scope

For each of the **particular integer polynomial matrices displayed in its Section 3** for `(m,p)=(2,4),(2,5),(3,3)`, the manuscript claims that there is no real `p x (m+p)` matrix L of rank p satisfying

`det[V(z); L] = c z^(mp)`

for **any real c, including c=0**. It consequently claims nonempty ordinary open unstabilizable subsets for `(2,4),(4,2),(2,5),(5,2),(3,3)` at `n=mp`.

This is a statement about the displayed matrices, not about every polynomial V. Section 3 says the exclusion is proved by a positive-definite combination of Plucker relations on the lower-coefficient kernel. The `(3,3)` integer matrix is printed; the 45 certificate multipliers are in the source package rather than all printed in the PDF. Remark 3.2 additionally reports coprime maximal minors, maximal degree n, and complex nondegeneracy. These are external exact-computation claims that I did not replay.

**P33 reserve:** `(3,3), n=9` is directly and explicitly covered by Theorem 1.1, not merely suggested by an infinite-family analogy. Its ordinary plant space is `R^135`. It is therefore not a collision-free fallback from P24.

### Theorem 1.2, exact scope

For **every even integer p >= 2**, with `n=2p`, the manuscript claims nonempty ordinary open unstabilizable subsets of **both** `S_(2,p,n)` and `S_(p,2,n)`. Thus P24 is covered a second way by p=4. The argument uses complex polynomial curves regarded as real curves and dimension estimates; it is not conditional on running a numerical search successfully.

For context, Theorem 1.3 similarly claims the two port orders `(4,p)` for every even p >=2 at `n=4p`. Neither these theorems nor the local packet answer the full all-pairs classification. The external paper itself keeps other even-degree cases open and labels its full parity classification as a question, not a theorem.

## 5. Classical primary sources: what was actually read

### 5.1 Current author problem and AIM inventory

- Eremenko current primary PDF, all five extracted pages: <https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf>.
- Current AIM 319 inventory, complete record: <https://raw.githubusercontent.com/MColbrook/AIM/main/problems/319-generic-static-output-feedback-stabilization.md>.

Eremenko asks which m,p have generically stabilizable real systems at `n=mp`. He distinguishes even-even **failure of arbitrary pole placement** from the known `(2,2)` **open nonstabilizable family**. His Byrnes-Anderson geometric criterion concerns the pure-power fibre for nondegenerate polynomial systems. The current literal `(2,2)` displayed sign issue is also discussed in Ferudun Remark 3.3; our earlier correction is not, by itself, a new source finding relative to that public claim.

The AIM record carefully distinguishes the same two tasks, but its September search predates the October paper. Its later plant-dependent pole-placement/LQR/decision-complexity references are not evidence that the exact critical P24 open-family question has no public answer. The inventory is a routing/status source, not a priority certificate.

### 5.2 Original Byrnes-Anderson

Published reference: C. I. Byrnes and B. D. O. Anderson, *Output Feedback and Generic Stabilizability*, SIAM J. Control Optim. 22(3), 362-380 (1984), <https://doi.org/10.1137/0322024>.

Lawful accessible primary manuscript route: NASA CR-166441, <https://ntrs.nasa.gov/api/citations/19830010078/downloads/19830010078.pdf>. NASA record <https://ntrs.nasa.gov/citations/19830010078> identifies the containing report, *Algebraic geometric methods for the stabilizability and reliability of multivariable and of multimode systems*, publication February 1983. This is an earlier submitted manuscript of the paper, not a claim to have fetched the final journal typesetting.

Actually read in the retained primary extraction: the relevant manuscript statements at printed pp113-115, its closed-image/compactification discussion, and the Section4 complex-linear nondegeneracy definition at printed pp132-133. I also directly opened the retained p113 page image, avoiding reliance on its poor inequality OCR.

- Theorem1 gives the generic-stabilizability/deadbeat-pure-power equivalence in the regime including `mp=n`, with its **nondegenerate-system** hypothesis.
- Theorem3 states a nonempty open nonstabilizable family for `(2,2), n=4`.
- **Example3 explicitly leaves `(2,4), n=8` to be analyzed.** Thus the original does not already provide the exact P24 negative theorem.
- The definition uses independent **complex linear** functionals. A real-basepoint-free but complex-degenerate curve cannot simply be substituted into the universal nondegenerate theorem without an additional argument.

The SIAM publisher route returned HTTP403 earlier. The actual link on Anderson's public bibliography was located, <https://users.cecs.anu.edu.au/~briandoa/pubs/hidden/R211AN317.pdf>, but returned HTTP502 in this audit. No access restriction was bypassed. The available NASA manuscript and actual page image supply the stated original-interface read scope; I do not claim a full final-journal proof audit.

### 5.3 Fixed rectangular case before the new claim

Rosenthal-Sottile, *Some Remarks on Real and Complex Output Feedback*, arXiv `math/9702218`, later Systems & Control Letters33 (1998), 73-80: <https://arxiv.org/pdf/math/9702218>. Actually read the primary statement framework, Theorem2.3, Example2.4 and its selected target polynomial, and Conjecture2.5; the complete extracted paper was available.

Example2.4 has `(m,p)=(4,2), n=8` and an ordinary-open **nonsurjectivity** conclusion. Its omitted polynomial is

`(s+8)(s+6)(s+4)(s+2)(s-1)(s-2)(s-3)(s-4)`.

This polynomial has both positive and negative real roots. Omitting it is not exclusion of every Hurwitz polynomial. Its fourteen nonreal inverse-fibre calculations are the source's evidence, not calculations replayed here.

Eremenko-Gabrielov, *Counterexamples to Pole Placement by Static Output Feedback*, author preprint dated 6 November2001, published Linear Algebra Appl.351-352 (2002), 211-218: <https://www.math.purdue.edu/~eremenko/dvi/polep33.pdf>. Actual primary abstract, Theorem1 and its system/omitted-configuration construction were read. It proves real pole-placement nonsurjectivity when `n=mp`, `min(m,p)=2`, `max(m,p)` even, with a whole neighborhood of some pole configuration omitted. It does not state an open family omitting every stable configuration.

Eremenko-Gabrielov, *Pole Placement by Static Output Feedback for Generic Linear Systems*, SIAM J. Control Optim.41(1) (2002), 303-312: <https://www.math.purdue.edu/~eremenko/dvi/polep72.pdf>. Actual primary introduction, even-even theorem and explicit separately open stabilization question were read. For both m,p even and `n=mp`, it proves generic nonsurjectivity/open pole omissions. In the preprint formulation the reference omitted polynomial is `s(s^2+1)^(mp/2-1)` (a projective degree-n divisor, including infinity). That is not the pure power `s^n`, and the paper separately asks whether the generic even-even critical system is stabilizable.

**Conclusion from the classical sources read:** the 1998 and 2002 omissions must not be promoted to a stabilization theorem. The robust pure-power-to-stabilization architecture is classical; obtaining a suitable new real empty pure-power fibre is the consequential extra ingredient. Our local target-level conclusion is not just the already-known arbitrary-pole omission, but Ferudun's later claim explicitly supplies that extra ingredient for the very same P24 and P33 cases.

## 6. Mechanism comparison with the pinned local packet

### 6.1 The robustness bridge is already explicitly present

Ferudun Definition2.2 defines (NS) as

`U(V) intersect D = {0}`,

where U annihilates all minor-coefficient rows below degree n and D is the real decomposable cone. Equivalently no real rank-p L gives `c z^n`, **including the zero polynomial**.

Proposition2.3 assumes only a real `m x (m+p)` polynomial V whose entries have degree <=p and property(NS). It concludes a nonempty ordinary open unstabilizable set for both port orders. Its full five-step bridge was read:

1. Compactness of the unit decomposable cone and elementary root-coefficient bounds give a neighborhood of coefficient maps with neither a real zero image nor an image polynomial with all n roots in a sufficiently small disk.
2. **The identical Cayley map** `z=epsilon(s+1)/(s-1)` converts that disk exclusion to Hurwitz exclusion. Degree drop contributes a root at `s=1`, outside the stable half-plane, so roots at infinity are not ignored.
3. A constant real GL column transformation preserves the decomposable cone and root exclusions.
4. The whole ordinary plant's determinant coefficients depend continuously on `(A,B,C)`, via its expansion in the gain minors. Thus the open coefficient-map condition pulls back to an open set in the **entire ordinary plant space**.
5. Normalize the leading row block to `[I_m | 0]`, write `[D,N]` with monic degree-p D and strictly lower degree N, and use the **same first-column observable block companion**, `B=col(N_(p-1),...,N_0)`, `C=[I_m,0,...,0]`. The closed-loop identity is `det(sI-A-BKC)=det(D-NK)`. Transposition gives the other port order.

Remark2.4 explicitly says this proposition requires **neither coprime minors nor complex nondegeneracy**, because(NS) already excludes real c=0. It explicitly identifies the same Mobius-transformation and compactness ideas in Byrnes-Anderson. Therefore allowing a deliberately complex-degenerate but real-basepoint-free base curve is not an unmentioned loophole or, relative to this prior paper, a new general bridge.

Our packet's PBH/minimality, explicit coprime normal form, finite gain chart and continuous fraction reconstruction are useful detailed checks of its chosen implementation. The external proposition's ordinary-plant coefficient-map proof already establishes the target open-neighborhood conclusion without needing those particular details. A more explicit realization argument is not a new dimension case.

### 6.2 The Hermitian mechanism is also a direct match

In Section4, the prior paper regards a complex polynomial row `v` of length `b+1`, degree <=`2b`, as a real two-row curve. Its Proposition4.4 defines

`K_v = {H Hermitian : v H v* in R z^(4b)}`

and states that the real curve has(NS) **iff K_v contains no nonzero matrix of rank <=2**. This is precisely the low-rank Hermitian exclusion behind the local packet's J-splitting/real-simple-bivector argument.

For b=2, Example4.5(b) explicitly gives

`v=(i z, 1+i z^4, 1+z^2+i z^3)`

and a Hermitian H0 with `v H0 v*=2z^8`, `K_v=R H0`, and rank H0=3. Its verification report explicitly records signature `(2,1)` and determinant `-20`. The PDF text conversion loses some minus signs in this display; this audit does not use an OCR sign as an independently verified certificate. What matters for the mechanism comparison is the explicitly claimed full-rank Hermitian line and exact `(2,4)` example. The computations establishing that example were not replayed.

Thus **complex curves as real curves, a three-dimensional Hermitian form of signature(2,1), rank<=2 exclusion, and a complex-degenerate but real-basepoint-free base are already present together in the matched prior claim**.

### 6.3 What may actually differ in our construction

Our packet's particular rational-inner pair on the circle gives a degree-four row with a **null** Hermitian relation `v B v*=0` for a full-rank form B of signature(2,1). It separately proves that `z^8` is outside the whole linear minor image. Consequently its K_v is the full-rank line `R B`, a direct special case of the already-stated Proposition4.4 criterion.

There is a genuine algebraic distinction from the printed prior Example4.5(b): that example has `v H0 v*=2z^8`, whereas our row has `v B v*=0` and excludes `z^8` already at the linear-image level. Our separator and its explicit rational disk radius are a potentially cleaner or more quantitative certificate for this selected row. I did not find the local rational-inner coefficients printed in the relevant prior-paper sections read.

That does **not** justify a novelty claim for the new row, for a new method, or for the target theorem. Establishing whether the exact null-curve/linear-image specialization or its radius is itself known requires a further matched construction-level literature check. At present the defensible possible delta is **another explicit construction/certificate and expanded written reconstruction**, not a new P24/P33 dimension case, not a new degenerate-to-ordinary-open bridge, and not the full generic-stabilization classification.

## 7. Public AI/corpus overlap and negative-search limits

- **EulerSolve AMR-036-0044 is an actual exact matched public AI-assisted claim**, not an inference from a neighboring topic. The primary page, manuscript, metadata, DOI registry record and public verification report were read. Its `COMPLETE_SCOPED_PROOF` metadata is the publisher's claim, not our verdict. Verification report: <https://eulersolve.org/papers/amr-036-0044/verification_report.md>.
- Current `openai/math` inventory was freshly read: <https://raw.githubusercontent.com/openai/math/main/CONTENTS.md>, header **719 manuscripts /372 result families**. Full backing text was searched for `output.feedback`, `generic.stabili`, `pole.placement`, `rational.inner`, `Byrnes`, `Eremenko`: no matches. This is an inventory/abstract screen, not a proof-body or Lean audit of all manuscripts, and it does not cancel the EulerSolve collision.
- The public Ulam archive <https://www.ulam.ai/archive>, retained from this day's source screen, was searched in its full returned title/abstract data for the corresponding output-feedback, pole-placement and author terms. No matched control result was found; broad `stabili` hits were unrelated geometric/MHD topics. The external paper itself identifies the separate UnsolvedMath dataset record `AMR-036-0044`; I did not independently retrieve that record's current row or rely on its status label as proof.
- Additional exact-case and rational-inner/Hermitian searches did not produce another authenticated matching primary result beyond the papers listed above. Search engines returned unrelated descriptor-system, time-delay, plant-dependent rank and Hermite-stability papers; their snippets are not substitutes for the critical real-static-feedback theorem. A search miss is not proof of priority.

## 8. Consequences and completed scope

1. Maintain the parent's HOLD on P24 scientific execution and novel-resolution framing. This report supplies an actual primary collision; no external witness needs to be executed merely to recognize that collision.
2. Do not redirect to P33 as if it were absent from the new claim: `(3,3), n=9` is explicitly in its Theorem1.1.
3. Preserve our frozen candidate and mathematical review unchanged, with this source-status overlay. A valid independent construction remains useful evidence even if its intended target case was publicly claimed earlier.
4. If the parent commissions a separate audit of Ferudun's proof, distinguish written theorem reconstruction, exact finite certificate replay, numerical evidence and formal proof. None of those extra acceptances occurred in this source assignment.
5. Full all-pairs generic stabilization remains outside both the local P24 theorem and the external paper's scoped claims. No complete-book solution or publication-ready novelty is certified here.

Only this report was written for the bounded source task. All source reading was public or read-only retained evidence; commands were metadata clock/hash operations only. No scientific program, verifier, external model, witness replay, author-file edit or shared-index edit occurred. The worker returns to its own W4 angular obligation after delivering this report.
