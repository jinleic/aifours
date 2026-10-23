# aifours — AI-assisted attacks on open problems

Research dossiers on precisely stated problems from three volumes of 《10000个科学难题》
(10000 Selected Problems in Sciences, Science Press). The work started on 2026-10-14 in
`/Users/jinleic/jinleic-workspace/ai4s` and moved here the same day
([relocation record](maintenance/relocation-2026-10-14/README.md)).

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

`origin` is `https://github.com/jinleic/aifours` (public). This research round creates no commits or pushes.
`.gitignore` keeps all PDFs local: the source books and downloaded papers are third-party
documents. The tree still contains rendered book pages and extracted paper text under
`*/sources/` and `*/source/`; review them before the first push.
