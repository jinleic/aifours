# Generic three-super-soliton degree obstruction

**Target:** the paired supersymmetric family proposed by Wang–Tang–Liang2018,

    (D_t+D_x^n)F·G=0,       S_y(D_t+D_x^n)F·G=0,

for all integers n≥4, with even F,G and `D_theta=partial_theta+theta partial_y`.
The paper explicitly proposes checking three-super-soliton existence (§4,
p. 040203-9); the primary quotes and the 2026 classification comparison are in STATUS.md.

**Book bridge:** Lou–Li's chapter 关于得到高维可积模型的一个新猜想 in
《10000个科学难题·物理学卷》, pp. 350–351. It proposes lifting a low-dimensional
Hirota system using an extra-dimensional or supersymmetric operator. The unedited
Chinese source excerpt is `source/problem.zh.txt`.

## Exact result and limits

**SOLVED (negative answer) for the selected Hietarinta-type generic interpretation
of the proposed three-super-soliton test:** for every integer n≥4 there is no generic
family combining independent F–F–G body seeds in the square-free exponential-body
class fixed in RESULTS.md §1.2, even after arbitrary nilpotent supertau dressings.
The source does not specify this ansatz or quantifier. Literal mere existence is
insufficient: G=1 and linear superpositions give restricted solutions for every n.
This generic all-pattern failure does not exclude isolated or restricted families
(including odd-n `b_i=±a_i` sectors), other body ansätze, Lax pairs or generalized
symmetries. The broad book chapter and the authors' symmetry hypothesis are not
fully solved.

**Evidence:** Certification. **Novelty:** bounded source/citation screen found no
settling source for this exact paired all-n question; no first-result claim or
exhaustive historical clearance. The 2018 explicit hypothesis is not being inferred
from a search miss. FRONTIER state: DELIVERY-READY for the scoped proof after its
recorded replay/referee disposition; NOVELTY-UNCLEAR for priority.

## Why the proof works

Project away the fermionic **parameters** while retaining the external superspace
coordinate theta. For even supertau functions this gives ordinary f,g, and

    pi_zeta(S_y P F·G)=theta D_y P f·g.

Thus both bosonic equations are necessary. A fully written exact F–F–G compatibility
obstruction is nonzero for every n≥4: finitely many exact integer signs plus a uniform
inequality for the infinite tail. Nilpotent corrections cannot cancel this body
obstruction. Setting theta=0 as well would lose the second equation; the replay
includes that invalid-projection negative control.

## One-command reproduction

From this directory:

    /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B code/replay.py

The replay independently reconstructs n=4/n=5 rational negative witnesses by
Euler/binomial differentiation, checks n=2/n=3 bodies and common-fermion boundary
lifts, verifies exterior-algebra signs and parameter projection, and records the
finite certificate and exact tail bound in `results/replay.json`.
It does not import any earlier project's engine. Finite controls do not replace the
universal written proof. No Lean/kernel verification is claimed.

## File map

- `STATUS.md`: explicit primary-open hypothesis, exact selected criterion, current
  single-tau-vs-paired classification comparison, forward-citation table and limits.
- `RESULTS.md`: Grassmann/seed definitions, projection theorem, general-n obstruction,
  exact scope, evidence ledger and independent-review dispositions.
- `source/`: original book excerpt; pinned 2018 paper and 2026 preprint/texts; `pins.json`.
- `code/replay.py`: independent exterior algebra and direct-differentiation replay.
- `results/`: observed replay output and verification receipts.
- `review/`: self-contained referee prompt, untouched response and metadata.

All earlier physics folders remain unchanged. This selection is not a relabeling of
the earlier cubic all-N certification as a newly solved open problem.

## Verification and referee outcome

The changed-path replay passed. Exact body witnesses have
`R211=-56064/5423` at n=4 and `R211=-313600/1573` at n=5. The n=2/n=3 full body
residuals and restricted common-fermion lifts vanish. Projection controls,
15 unprojected sign-sensitive off-shell controls, the finite integer certificate
and the all-degree tail inequality all passed.

The configured other-vendor referee, `claude-opus-5-5` at max effort, returned
**correct** for Theorem4.1, with no remaining mathematical step and no fatal/major
finding. Minor scope, citation-screen and control clarifications are addressed
in RESULTS.md §7. The untouched output and pinned snapshot remain in `review/`.
The reviewer did not execute code or certify originality; the exact replay was run
by this worker. Source indexes disagree (2018 citers: OpenAlex0, OpenCitations0,
SemanticScholar1), and that limitation is retained rather than hidden.
