# PH7: physical budgets, double poles and one actual mean

Parent observation before writing: **2026-10-27T07:27:59-0700 PDT**. Four v212 gates are **WRITTEN_SUPPORTED at the ordinary input boundaries below**. They give an exact reformulation, not a seven-state witness, universal infeasibility proof or new minimum-order bound. Original PH7 feasibility at the stated ratio remains unresolved.

## Mandatory correction to v1

This complete successor supersedes the mathematical text of [parent v1](PH7-v212-physical-budget-double-pole-one-mean-entire-parent-v1.md), SHA-256 `bd5e0ae9954c19c05a68974b486c9f8af102d8aadaeaea4749eb990237993f53`. Parent v1 was emitted from a JavaScript template with unescaped mathematical backslashes: delimiters and commands were lost and `\t` became a tab. Its formulas are malformed; **do not use v1 alone as a mathematical statement**. Frozen v1 is unchanged. The correct formulas and decisions are restated below, using inline code to avoid that serialization error. The parent observed this defect after writing v1; it is not attributed to the author or either reviewer.

## Scope and evidence

Fix `c,d > 0`, `a = c+d`, `b > 0`, `b^2 = 8d^2/9`, `G(s) = ((s+a)^2+b^2)^2`, `D5(s) = (s+c)G(s)` and `K = D5(0)`. A physical candidate is a real seven-state Hurwitz Metzler matrix `T`, a probability row `alpha`, and the literal exit `omega = -T 1 >= 0`. Its transfer is `H = N/P`, where `P = det(sI-T)` and `N = alpha adj(sI-T) omega`. All statements keep the same actual matrix and its row/input/exit ties.

Main read, in separately returned raw calls through every ending, the complete 266-LF global A-or-B proof, 174-LF balanced-B fibre proof, 232-LF new source and both complete reviews (374 and 269 LF). The four over-768-character lines in the 266-LF source and the two in review B were reread individually. All five live hashes matched their frozen or returned pins before v1. The first four reads of the new source were incorrectly issued in one parallel batch; [parent finding v221](parent-v212-PH-parallel-source-read-finding-v221.json) records that process MAJOR. Main subsequently reread the entire new source sequentially before v1; this does not cure the event or certify private noninfluence.

| Input | LF | SHA-256 |
|---|---:|---|
| [Global A-or-B proof](../../../mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-standalone-global-ordered-A-or-balanced-B-equivalence-v1.md) | 266 | `3815c4d699735797090dbd974f522828363c02931b604d8f36af438f00d7ffc6` |
| [Balanced-B fibre proof](../../../mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-balanced-B-four-simplex-fiber-v1.md) | 174 | `13827911709d55d9d0bc77fe90f3f68272c9b207e99556ced0521339faafd877` |
| [New budget/mean proof](../../../mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-all-topology-budget-double-pole-and-one-mean-iff-v1.md) | 232 | `aa904382dd20a90431f1c2d67edaaa614c94d7dbaeca0139443ee3253f1c7f86` |
| [Review A — MathShor-2](../../../mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/peer-review-v212-A-v1.md) | 374 | `c309fe7acd99bf7c6691276234a17885f47134e263964484accad67885aa5ba0` |
| [Review B — PhysicsRQLS10-2](../../../physics/evidence/three-area-20261023-96h/parallel-18/rqls10/peer-review-v212-B-v1.md) | 269 | `e4933635e56727990c3883e0f21ec1c1b603467c364861ac295b6f3091ae79e8` |

The [21-LF author request](../../../mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-all-topology-budget-double-pole-one-mean-entire672-gate-request-v1.json) defines the four gates; [v212](peer-review-wave-eighteen-v212.json) and its [packet receipt](peer-review-wave-eighteen-v212-packet-receipt-v1.json) bind the supplied scope. Earlier parent dispositions are context at their own cuts, not substitutes for the operative bodies.

## Decisions

| Gate | Mathematical result | Dependency/application boundary |
|---|---|---|
| **J1: contacts and one mean** | Suppose the actual numerator is `N = K Q`, where `Q = s^2+p s+q` with `p,q > 0`, and the actual trace is `-tr(T) = c+4a+p`. The target `H = K/D5` holds iff `P(-a+i b) = P'(-a+i b) = 0` and the **actual** mean equals `mu_star = 1/c + 4a/(a^2+b^2)`. | WRITTEN_SUPPORTED with all printed physical, numerator and trace antecedents. Root coincidences, repeated or nonreal hidden roots, and singular principal blocks at the complex pole remain allowed. Contacts alone do not imply the target. |
| **J2: ordered A** | At fixed admissible actual upstream data and ordered holdings, the entire feedback set is the nonnegative weighted simplex `v sum_i r_i + sum_i E_i = lambda v - k`, with `E=tD` and `k=K/L0`. A negative budget excludes target feedback; zero budget is retained. | WRITTEN_SUPPORTED: each budget point restores physical rows with `t >= k/v > 0`, exit `k/t`, actual numerator `KQ`, and pre-target Hurwitz stability. Conversely every actual ordered-A target supplies such data. |
| **J3: balanced B** | At fixed full physical outer data, the complete feedback domain is a product of four budget simplices, retaining all fifteen feedback coordinates; its polynomial image is the stated Minkowski sum. | WRITTEN_SUPPORTED: four separate budgets, the exact common-matrix numerator/constant and actual pre-target Hurwitz property are required. No essential-channel or freely chosen hidden-factor substitution. |
| **J4: global interval** | For the **same** fixed admissible A or B outer data and holdings, the double-contact set `Z` is compact convex or empty. Its affine discrepancy image is empty or a compact interval, and the target is feasible at these data iff the interval contains zero. | WRITTEN_SUPPORTED using the complete global A-or-B reduction and both physical fibre constructions. Two contact points bracket zero only within the **same** outer data and budget; different outer matrices do not suffice. |

Both reviews report zero new mathematical fatal, major or minor findings at these cuts. They are supplied-source, same-harness reviews; one reviewer has prior PH contact and the other has a disclosed reciprocal author/reviewer relationship. Neither review is blind or configured-family, human, formal, kernel, executable, cross-vendor or novelty verification.

## Parent hand checks

1. Row ties give `N(0)=P(0)` by the adjugate identity. For Metzler `T` with `T 1 <= 0`, Gershgorin discs meet the imaginary axis only at zero; `P(0)>0` excludes it, establishing stability for budget candidates without assuming the target.
2. The two complex double-contact equations imply `G` divides `P`. Monicity, the actual trace and `P(0)=Kq` force `P/G = (s+c)Q + kappa s`. Differentiating the actual transfer at zero gives `mu - mu_star = kappa/(c q)`; no positive-Laplace-integral inequality at the complex pole is used.
3. For ordered A, `R=lambda v-k` and the budget imply `t=lambda-sum_i r_i >= k/v > 0`, `v-D 1=k/t>0` and `P(0)=Kq`. Division by `t` is therefore justified at every budget point, including zero budgets.
4. For balanced B, `h=-F 1-omega`, `r0=lambda-t^T 1`, and `v0^T=t^T(-F)^(-1)` give `r0+v0^T h=lambda-gamma`, so `P(0)=a_R(0)a_S(0) gamma=Kq>0` for every separately budgeted point.
5. With fixed `P(0)` and `N`, the mean error and characteristic coefficients are affine in the stated feedback coordinates, not in arbitrary restored matrix entries. A compact convex contact set has an interval image with attained endpoints; no cross-outer interpolation is used.

Named ordinary inputs include finite graph augmentation/flow decomposition, determinant and adjugate algebra, Gershgorin and Metzler semigroup/resolvent positivity, irreducible Perron asymptotics, real symmetric spectral/compact-extremum facts and finite-dimensional convex separation. Their specialized applications appear in the supplied proofs; their general foundations are not independently formalized here.

## Exact residual and permanent limits

**NR-NEXT-CONTACT-ZERO remains unproved:** obtain admissible complete ordered-A or balanced-B outer data with an actual zero-discrepancy contact point (or two genuine same-outer contact points bracketing zero), **or** prove that every allowed contact set is empty or omits zero. Neither source nor review provides either. The historical upper-eight input was not newly verified here, so the contextual `{7,8}` minimum range retains that separate dependency.

The [v218 chronology qualification](v212-ABC-E-checkpoint-read-chronology-qualification-v218.json) records that Main read requested reviewer whole checkpoints after, not before, the original v212-A/B releases; the frozen v212 contract explicitly required complete ACK reads before release. The author's disclosed 33m08 cadence finding, both reviewers' prior contacts and all older read-order, source, process and ZERO-credit findings remain. [v221](parent-v212-PH-parallel-source-read-finding-v221.json) records the later parent parallel-read MAJOR. Correct later reconstruction does not repair any history. The 141-LF renewal, 177/170 moment/I-O, 189-LF real-algebra bodies and unrelated results are not new correctness inputs to this gate.

No scientific interpreter, calculator, CAS, numerical selection, program, enumeration, solver, replay or new GO was used for this disposition. HOLD, N4 UNKNOWN with historical child exit unestablished, auxiliary214 STOP, the same eighteen owners, science cutoff **2026-10-27T11:05:38-07:00** and delivery deadline **12:35:38-07:00** remain unchanged. This is not round closeout.
