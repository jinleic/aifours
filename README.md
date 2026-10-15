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
| [`institute/`](institute/docs/DESIGN.md) | Research-institute explorer: a separate workstream, with its own design and smoke records |
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

## Reproduction

Commands live in each dossier README. They depend on resources that stay in the workspace:

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

`origin` is `https://github.com/jinleic/aifours` (public). Nothing has been committed or pushed.
`.gitignore` keeps all PDFs local: the source books and downloaded papers are third-party
documents. The tree still contains rendered book pages and extracted paper text under
`*/sources/` and `*/source/`; review them before the first push.
