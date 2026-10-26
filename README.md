# aifours — AI-assisted attacks on open problems

Research dossiers on precisely stated problems from three volumes of 《10000个科学难题》
(10000 Selected Problems in Sciences, Science Press). The work started on 2026-10-14 in
`/Users/jinleic/jinleic-workspace/ai4s` and moved here the same day
([relocation record](maintenance/relocation-2026-10-14/README.md)).

## Current assessment — 2026-10-26

The work contains complete finite constructions and scoped theorems with substantive verification.
The strongest written continuation is **Sun's disjoint-coset conjecture at k = 7 for arbitrary groups**,
accepted by the internal model-review and parent-composition protocol. It is not a proof for every k,
not kernel-checked or human-peer-reviewed, and priority is unresolved.

Concrete successes include **LKTS(57/87)**, the **six cyclic (v,5,1) difference-family exceptions**,
**four decided BTD instances**, and the sharp two-qutrit **15/16** theorem. The final physics verdict
also accepts **M(7) = 2**, with the recorded computational-provenance limitations. Several finite
constructions have recorded Lean kernel replays; those replays were not repeated for this publication.
Fresh direct checks passed again on 2026-10-26 for all six difference families, RDSQS(52),
mcDSQS(38), BTD(14,28), both CFR(5,27) witnesses, and an exact two-qutrit attaining gate.
Three deliberately corrupted witnesses were rejected. The mcDSQS(38) contribution is its
certified optimal colourings; its underlying SQS was already public. See the
[dated assessment, replay commands and limits](maintenance/publication-2026-10-26/README.md).

The [October 23–27 eighteen-target round](institute/runs/three-area-2026-10-23-96h/README.md)
contains further scoped written theorems and useful barriers, but declares none of its
unrestricted book targets solved and remains active at its latest recorded checkpoint.
Its ordinary written reviews are not Lean/kernel or human review. Mandatory verification
overlays, priority corrections and withdrawals accompany the research, including the refuted
semigroup CG/RU–LU claims. Publication does not promote these claims or close the round.

**Full ordered Olson, MOQLS(8), maximal 1-RQLS(10), PA(19,8,6), CFR(6,21), and six MOLS(39)
remain unresolved here.** Earlier CPCW and L(12,3) results are independent confirmations of prior
public claims. The dated summaries below are historical; the
[October 22 assessment and publication limits](maintenance/publication-2026-10-22/README.md) and
[96-hour closeout report v17](institute/runs/six-lane-2026-10-18-96h/report/continuation-report-2026-10-22-final-v17.md)
give the later status. Public source/code availability does not establish scientific priority or expert acceptance.

## Layout

| Path | Contents |
|---|---|
| [`information-science/`](information-science/README.md) | Information-science volume (2011): 12 dossiers, screening notes and round evidence |
| [`mathematics/`](mathematics/README.md) | Mathematics volume (2009): 11 dossiers, HMZ + Lean rounds and round evidence |
| [`physics/`](physics/README.md) | Physics volume (2009): 13 dossiers, the [reselection index](physics/PHYSICS_RESELECTION.md) and round evidence |
| [`institute/`](institute/README.md) | Bounded research-institute visits: parallel launcher, frozen selections, append-only records, replay and referee evidence |
| [`books/`](books/README.md) | Source volumes: local PDFs, SHA-256 identities and page offsets |
| [`maintenance/`](maintenance/relocation-2026-10-14/README.md) | Relocation map, preservation inventories and receipts |

Each dossier, `<domain>/<slug>/`, owns its book statement, status verdict, sources, proofs, code
and evidence. Domain READMEs only route and summarize; when they disagree with a dossier, the
dossier wins. Round-level selection, screening, parent replays and review dispositions live in
`<domain>/evidence/`.

## Outcomes

| Domain | Status on 2026-10-14 |
|---|---|
| Information science | No previously open broad book problem fully solved. Two precise claims were settled negatively: universal optimizer existence for expected-average POMDPs, and sufficiency of separate IF/GD feasibility tests for nonnegative time–frequency distributions (certified counterexample). Two exact readings were already answered by classical work; the other eight dossiers are partial or open. |
| Mathematics | One candidate full answer: semifilter Questions 2–3, HMZ-accepted, with novelty unresolved. Already settled by prior work: the dendriform trialgebra basis and the studied inverse-optimization case. Refuted: the broad no-moment M-estimator formulation. Artin Question 3 is answered for a fixed deg-lex reading. Kirkman, Kac–Moody, semigroup embedding, Olson and Shor remain open with partial results. Seymour is claimed by the openai/math corpus, not re-verified here. |
| Physics | Five reselection packages are Certification results with uncertified priority. The SO(5) candidate was already solved. The earlier five narrowed proofs did not pass the openness gate. Two first-pass dossiers, cone spirals and small quantum codes, are retained but screened out. |

Labels follow the dossiers. Written proofs are not kernel-checked unless a Lean/Comparator
receipt says so. Model referees are not human peer review, and no novelty is claimed without a
primary-source comparison.

## Difficult-problem visits and continuation (2026-10-15–16)

Batch 01 started at 04:03 PT. Mathematics produced an **unverified** attack: its referee could not
replay the production computation because large logs were omitted from the snapshot. Information
science and physics timed out during 10-minute identification and never reached attack. With owner
approval, all three restarted at 12:02 PT with fresh six-hour ceilings; identification now has 30
minutes, and the previous logs are supplied as hash-checked compressed inputs. Batch 02 and its
same-budget continuation, batch 03 (14:23–17:36 PT), both closed all three as **unverified** after
referee accept-with-fixes. In batch 03 no claim was judged wrong or unsupported. Referees asked only for
wording or control changes, but that still stopped every visit before its novelty stage. Those
are the completed engine visits' verdicts, not a verdict on the later continuation findings below.
No book problem is fully solved. See the [batch outcome ledger](institute/review/hard-2026-10-15-outcomes.md).

| Volume | Selected target | Book pages | Selection and budget |
|---|---|---|---|
| Mathematics | Flag-transitive projective planes: extend the finite exclusion range beyond the published n < 2×10¹¹, with the book's inconsistent graph wording disclosed | 39–40 | [Catalog](mathematics/evidence/mathematics-hard-20261015/catalog.md) |
| Information science | A balanced nine-variable Boolean function with nonlinearity ≥242; local/class exclusions remain partial | 403–405 | [Catalog](information-science/evidence/information-science-hard-20261015/catalog.md) |
| Physics | Certified random 4-SAT/5-SAT upper bounds from the statistical-physics chapter; numerical inequalities require their analytic bridge | 422–427 | [Catalog](physics/evidence/physics-hard-20261015/catalog.md) |

[Run entry](institute/runs/hard-2026-10-15/README.md) ·
[Frozen selection](institute/runs/hard-2026-10-15/selection.json) ·
[Terminal supervisor receipt](institute/runs/hard-2026-10-15/run.json) ·
Batch receipts [01](institute/runs/hard-2026-10-15/batches/01/receipt.json),
[02](institute/runs/hard-2026-10-15/batches/02/receipt.json),
[03](institute/runs/hard-2026-10-15/batches/03/receipt.json).
The generated run records own the completed engine visits' outcomes; later parent research does not rewrite them.

The owner then authorized continued scientifically reasonable research without the previous total
time/token limit. The [continuation ledger](institute/review/continuation-20261015/outcomes.md)
separates its checked findings from the unchanged engine verdicts:

| Problem | Checked continuation result | Evidence |
|---|---|---|
| Flag-transitive planes | Conditional exact finite exclusion extended to **n < 2,582,236,504,064**, including a fresh replay of the old low range | [Package](mathematics/evidence/hard-continuation-20261015/README.md) |
| Balanced nine-variable NL242 | All **252** remaining restricted fixed-half classes closed; universal residue distance **>=112**; the entire **(rank4,weight128)** residue type excluded by a model-reviewed written proof. **Seven types remain.** | [Structural proof](information-science/evidence/hard-continuation-20261015/quadratic-distance/zero-geometry/README.md) |
| Random SAT | Rigorous numerical densities **4.26679 / 9.9325 / 21.1175** for k=3/4/5; separate kernel-checked endpoints **4.26718 / 9.934 / 21.123** | [Numerical certificates](physics/evidence/hard-continuation-20261015/README.md) · [Lean](physics/evidence/hard-continuation-20261015/formal/README.md) |

These are scoped contributions, not exact thresholds or a demonstrated breakthrough. The methods
have substantial prior art; priority of the specific results remains unresolved. Written/model-reviewed
proofs are not human peer review or Lean verification. No batch 04 or automatic research scheduler ran.

## Six concurrent research lanes (2026-10-16–18)

The owner authorized a new 48-hour research round with **two problems per domain, six concurrent
slots**, and replacement of concretely blocked or already-solved targets. The
[run entry and frozen contract](institute/runs/six-lane-2026-10-16/README.md) specify the exact
targets, deadline, independent-verification gate and worker ownership.

**Mathematics met that contract's breakthrough gate.** Large sets of Kirkman triple systems of
orders **57 and 87** were constructed explicitly. Each certificate passed three independently written
verifiers, mutation controls and a byte-exact regeneration from a compact seed. Both finite existence
statements also have reviewed Lean 4.34.1 proofs, replayed by a fresh process of the same kernel. Wang's
2026 survey had named these as the only admissible orders below 200 still open, so none now remains
(inheriting that survey's premises). The book's all-orders question remains open; priority is unresolved,
and there is no human peer review. An explicit **RDSQS(52)** and an **mcDSQS(38)**, the two smallest
unknown orders named by Tan–Zhou 2025, also passed independent checks, replay, review and
parent-replayed Lean proofs ([RDSQS verdict](institute/runs/six-lane-2026-10-16/review/rdsqs52-parent-verdict.md),
[mcDSQS verdict](institute/runs/six-lane-2026-10-16/review/mcdsqs38-parent-verdict.md)); the mcDSQS(38)'s
underlying SQS(38) was already in a 2025 public dataset, so its certified colourings are the contribution.
An explicit **gcDCQS(20⁴:0)** then settled the v = 20 component of Tan–Zhou §4(2). With their published
Corollary 2.6 it gives **mcDSQS(5·4ⁿ) for every n ≥ 3**; an explicit mcDSQS(80) is also directly verified.
Certificate A, explicit mcDSQS(80) and χ′(79)=40 are now parent Lean-kernel checked; the family still imports published recursion
([direct verdict](institute/runs/six-lane-2026-10-16/review/gcdcqs20-parent-verdict.md), [Lean verdict](institute/runs/six-lane-2026-10-16/review/gcdcqs20-lean-parent-verdict.md)).
An explicit **gcDCQS(32⁴:0)** then settled the v = 32 component, so both parts of §4(2) are answered. An explicit
**mcDSQS(128)** is directly verified, and with Corollary 2.6 and its imports **mcDSQS(2^{2n+1}) exists for every n ≥ 2**
(not Lean-checked; priority screen bounded with access holes;
[verdict](institute/runs/six-lane-2026-10-16/review/gcdcqs32-parent-verdict.md)).
Both finite objects in **Tan–Zhou §4(3)** are now verified: **gcDCQS(18⁴:2)** and **FDGDD(3,4,5{18})**.
An explicit **mcDSQS(74)** also passes all three checker implementations. With the published Constructions2.1/2.3,
Lemma3.8 and mcDSQS(20), this gives **mcDSQS(18·4^t+2) for every integer t≥1**. Both bridge reviews accept the
argument; higher orders remain an imported written consequence, not explicit certificates or Lean proofs.
Priority is unresolved within the stated access limits ([verdict](institute/runs/six-lane-2026-10-16/review/tz43-parent-verdict.md)).
**Commault–Mocanu's 2003 Conjecture 1 is answered for its stated three-pole family:** for every a>c>0, b>0, the
phase-type distribution with transform c(a²+b²)/[(s+c)((s+a)²+b²)] has minimum PH order exactly
n*=min{n≥3 : b≤(a−c)cot(π/n)}. The proof is a written all-parameter argument: a lower bound for every PH
representation, and an explicit n*-state cycle whose exit coefficients are proved positive. Both CLI hostile
reviews found no FATAL or MAJOR issue, and the parent checked it independently. Mocanu's 1999 thesis already gives
n*+1 for the family and order n on every boundary case, and the cycle-angle mechanism is published, so novelty is
unclear; the general minimal-representation problem in the book remains open
([verdict](institute/runs/six-lane-2026-10-16/review/phase-type-complex3-parent-verdict-v2.md)).

**Information science also met the contract's finite-target gate.** Explicit
cyclic `(v,5,1)` difference families for **v = 321, 501, 621, 681, 801 and 901** passed three
independently written verifiers. These are exactly the six possible exceptions of Abel–Costa–Finizio
2004, still listed in 2026 primary sources; with that published theorem, a cyclic `(v,5,1)` family now
exists for every v ≡ 1 (mod 20) with 21 ≤ v ≤ 1001. Modest specialist significance; the bounded priority audit
located no earlier construction but does not establish "first".
All six finite existence theorems also passed parent fresh Lean-kernel replay; the other orders in
the complete-spectrum corollary still import the published theorem and were not re-verified here.
Complete-claim Claude review: ACCEPT-WITH-FIXES, correctness and Lean semantics accepted; minor
reporting/provenance fixes are documented in the [outcome ledger](institute/runs/six-lane-2026-10-16/outcomes.md).
The slot then proved that **no 2-(88,4,1) design has a point-cyclic resolution**, and then gave
**optimal CPCW codes for all eight frozen cases from the screened Baicheva–Topalova 2026 list**.
The additional listed case (126,6,1) was already known and was excluded. Both results are
Lean-kernel checked by parent replay. Finally, **L(12,3) = 36**: no cyclic binary sequence shorter than 36
covers every 12-bit word within distance 3. This modest computer-assisted table result uses counting,
three independent exhaustive implementations and the published length-36 witness
([verdict](institute/runs/six-lane-2026-10-16/review/cover12-3-parent-verdict.md)). **Priority correction:** both
the CPCW codes and L(12,3) were publicly claimed earlier in Zenodo notes (2026-08-24 and 2026-09-07), so they are
independent confirmations, not gates ([CPCW](institute/runs/six-lane-2026-10-16/review/cpcw-priority-addendum-v1.md),
[L(12,3)](institute/runs/six-lane-2026-10-16/review/cover12-3-priority-addendum-v1.md)). **BTD(12,15;6,2,10;8,6) and
BTD(14,18;7,1,9;7,4) do not exist**, even with repeated blocks; Rosin's 2025 table lists both as open. Connor-type
Gram/determinant arguments give reviewed written proofs, and Lean 4 kernel proofs of the explicit unrestricted
statements passed parent fresh replays ([12,15](institute/runs/six-lane-2026-10-16/review/btd12-15-parent-verdict.md),
[14,18](institute/runs/six-lane-2026-10-16/review/btd14-18-parent-verdict.md)); the method is classical and the
significance modest. **BTD(12,20;4,3,10;6,4) does not exist** either: a reviewed structural reduction of the 1-entries
(tetrads meeting evenly, classified into pair multigraphs or e7/e8 structures) leaves 3073 covering cases, each
excluded by a DRAT proof that the parent re-checked after a byte-identical replay
([12,20](institute/runs/six-lane-2026-10-16/review/btd12-20-parent-verdict.md)); computer-assisted, not Lean.
**BTD(14,28;8,3,14;7,6) exists**: an explicit witness passes three independently written checkers
([14,28](institute/runs/six-lane-2026-10-16/review/btd14-28-parent-verdict.md)). All four Handbook BTDs that
Rosin's 2025 tables still listed as open are now decided. Next, **CFR(5,27) exists**: two explicit 5 × 27 circular
Florentine rectangles (6-row difference matrices over cyclic Z_27) resolve an instance CPro1 lists as open, so
F_c(27) ≥ 5. Three separately authored definition-level checkers accept them, with parent controls, producer
rebuild/replay and CPro1's own predicate as additional evidence; priority screen bounded with access holes; modest significance
([verdict](institute/runs/six-lane-2026-10-16/review/cfr27-parent-verdict.md)).

**Physics met the gate as well.** The Díaz et al. Maximum Hypothesis now has a computer-assisted
proof, so with the pinned preprint's Theorem 1.1, χ(G_{n,5}) = 3 a.a.s. The two-qutrit 2-unitary orbit
is isolated among dual and among T-dual gates, which answers T7 at d = 3. **Every four mutually
orthogonal quantum Latin squares of order 7 are classical**, so 2 ≤ M(7) ≤ 3, which answers the n = 7
instance of Ball–Simoens Problem 16 by a computer-assisted proof with parent-checked UNSAT certificates
([verdict](institute/runs/six-lane-2026-10-16/review/moqls7-parent-verdict.md)). **No set of three such squares of order 7
has exactly one non-classical square** (Theorem K1, computer-assisted, five independent parent routes, both reviews
ACCEPT-WITH-FIXES). So every pandiagonal and every 2-resolvable QLS(7) has cardinality 7, and neither an MCPQLS(7) nor a
maximal-cardinality 2-RQLS(7) exists, settling two order-7 cases listed open in 2026 preprints
([verdict](institute/runs/six-lane-2026-10-16/review/moqls7-k1-parent-verdict.md)); a partial follow-up excludes exactly two
non-classical squares as well (Theorem K2, [verdict](institute/runs/six-lane-2026-10-16/review/moqls7-k2-parent-verdict.md)),
leaving only the all-non-classical case open for M(7). **The maximum entangling power of a
non-2-unitary two-qutrit dual (or T-dual) gate is exactly 15/16**, proving Rather's Conjecture 3.3.2 by a reviewed
written proof with exact algebra and two exact attaining gates
([verdict](institute/runs/six-lane-2026-10-16/review/qutrit-sharp-parent-verdict.md)). **The random 8-regular graph is
a.a.s. 4-chromatic, and the random 12-regular graph is a.a.s. 5-chromatic**, closing KPW's two windows by reviewed
written proofs. Exact-exponent weak duality and complete-graph hypercontractivity give a global quadratic-decay
mechanism; strict loss of the older relaxation is demonstrated at(4,8), not at(5,12). DERIVED-OPEN, priority
unresolved; one shared contribution, now counted under the new-theorem half of the contract clause only, because the
exact-marginal method has an earlier precedent ([attribution addendum](institute/runs/six-lane-2026-10-16/review/physics-priority-addendum-v1.md))
([χ8](institute/runs/six-lane-2026-10-16/review/chi8-parent-verdict.md),
[χ12](institute/runs/six-lane-2026-10-16/review/chi12-parent-verdict.md)). Other scoped results are a
positive answer to AMH Open Problem 1 (moment feasibility only), three-qubit depolarizing-output
majorization for all physical p, and a computer-assisted finite-block depolarizing-capacity
certificate at total-error p=1/5. See the [outcome ledger](institute/runs/six-lane-2026-10-16/outcomes.md).
Prior engine verdicts and continuation findings above remain unchanged.



## Reproduction

Historical dossier commands name the resources below. The shared workspace `scratch/` disappeared during
the 2026-10-15 screen; those Python/Lean caches were not restored and their old receipts are not fresh
reproduction evidence. The current institute run uses `~/.local/state/research-explorer/venv/bin/python`.

- Python environments: `/Users/jinleic/jinleic-workspace/scratch/ai4s-*`. Scratch is machine-local
  and not synchronized.
- Lean toolchains and Comparator caches: `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/`
  and `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/`.
- HMZ wrapper and pairing: `/Users/jinleic/jinleic-workspace/scripts/hmz-run.sh`,
  `/Users/jinleic/jinleic-workspace/scripts/hmz-tiers.json`.
- Delegate-model registry for referee scripts:
  `/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json`.

Logs, prompts, receipts and review outputs are preserved byte-for-byte, so they still cite
`/Users/jinleic/jinleic-workspace/ai4s/...`. Translate those paths with the
[path map](maintenance/relocation-2026-10-14/path-map.json).

## Publication

`origin` is `https://github.com/jinleic/aifours` (public), with default branch `main`. The owner
separately authorized publication on 2026-10-22. The earlier research contracts and their
no-publication records remain historical; that authorization does not change their verdicts.

The public tree keeps research sources, proofs, compact witnesses, manifests and structured review
receipts. `.gitignore` excludes source PDFs, full third-party text copies/rendered pages, environments,
native binaries, raw logs and bulky generated evidence. All newly excluded local files stay on disk.
Some computer-assisted proofs require regenerating or separately obtaining the omitted payloads;
a clone is not a complete immediately replayable evidence bundle. See the
[publication record](maintenance/publication-2026-10-22/README.md) for exact limits and exclusions.
The [October 26 refresh](maintenance/publication-2026-10-26/README.md) records subsequent
verification and the additional source-copy exclusions.
