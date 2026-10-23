# FC19 scope v1 (frozen before any new derivation)

Owner: OlsonThirdCutWindow, same throttled math2 slot, after the parked FC717 delivery.
Freeze time: 2026-10-20T10:04:27-0700 (`/bin/date`, taken immediately before this exclusive creation).
Directory: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells

## 1. Authority and target

Authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-fc-p19-cells-transition-v1.json,
SHA256 9c04963a8d484c774812fe549a8552004bdf2a0bce57e584c80b627de708e094, 49 LF lines, 3641 bytes (read LF1-49).

Target (authority LF6, literal): BOTH remaining p=19 terminal k=20 cells, (kappa,p)=(7,19) and (8,19), with
kappa_hat=kappa, under the full existential NF/word antecedent: a length-74 avoider over D_38 without an identity
38-subword, SOME admissible NF, arbitrary extra reflection pairs and the genuine empty-run rule.
Deliverable, SEPARATELY for each of the two cells: either a written proof that the full cell is excluded, or the
exact first unproved lemma together with a checkable surviving residual. No silent reduction to one cell, to a
subfamily of frames, or to a restricted NF placement. If one cell closes and the other does not, both outcomes are
reported separately.

## 2. Premises permitted (exact scopes only)

- UMR, now ACCEPTED_SCOPED_PARTIAL: verdict /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md
  (SHA256 a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772, 38 LF lines, 6188 bytes); proof
  /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md
  (SHA256 c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9); errata v1
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md
  (SHA256 b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f) and v2
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v2.md
  (SHA256 2a5f142ef136b04c15304137a4ba19946d0fee115ce18e8660817cd25bc902a2, 9 LF lines, 1813 bytes).
  Usable: UMR-F, literal Lemmas 0-20 and the conditional UB reduction, each at its exact stated scope as fixed by the
  verdict and both errata. Lemma FC of UMR is NOT proved and is not used. No universal saturation, characterisation
  or necessary obstruction for RES is used. Any statement beyond a literal accepted statement is re-proved here.
- FC717 (/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-7-17/proof-FC717-v1.md,
  SHA256 e2c74806fc5f1986b298d490b121676eff7dce5f90f014311d3d8c099800b945): NOT accepted. Method inspiration only.
  No FC717 lemma is a premise, and no (7,17) constant is substituted for p=19. Every new count is re-derived here.
- Frontier context only: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FQW-parent-verdict-v1.md
  (SHA256 a9388a49e227b3bf418e2250b515860a33f880dba816b5318a834faa5da9e566), LF9; not a premise.
- Primitive inputs (NF, GRX, SC0, FB, balfull, (S1), LOWER and FCW errata) are used only through UMR as accepted.

## 3. Untrusted parent route hint

The authority (LF40) records a parent observation that, at these p=19 cells, the symmetric real-valued balancing
level lies between adjacent integer m-levels. This is an untrusted hint. It was NOT checked before this freeze, in
writing or mentally, and it is not a premise. If used as a route, it is first derived post-freeze.

## 4. Prior exposure (complete disclosure)

- I authored TCW, P7L, FQW (all parent-accepted), UMR (proof c403bfba..., now ACCEPTED_SCOPED_PARTIAL) and FC717
  (proof e2c74806..., not accepted). I know the full UMR text, its Sec. 6 cell constants and its RES/UB analysis,
  including that the selected UB certificates fail at (7,19) and (8,19) and that Lemma FC is UMR's first failing
  lemma there. During UMR authorship I made unwritten attempts at the open cells (RES reasoning, window counting)
  that did not close; none is relied on, and nothing from them is assumed correct.
- FC717 method, known in full: at (7,17) the central level m=5 has ell=M; one uses the two-sided five-subset
  window on the two alternating nine-run sets, sorts the top five runs, splits into types G/P/Q by
  min(q,q') and closes by empty-run counting, a sparse lemma and the total identity. I have NOT worked out how
  any part of this transfers to p=19 (level choice, subset sizes, window offsets); no p=19 arithmetic was done.
- Pre-freeze reading for this assignment: the authority LF1-49 only. Pre-freeze machine steps: `/bin/date`,
  `shasum -a 256` and `wc -c -l` of the authority, verdict, erratum v2, erratum v1, UMR proof, FC717 proof and FQW
  verdict (all hashes match the authority); mkdir of the directory and checkpoints/. Verdict and erratum v2 were
  hashed but not read before this freeze.

## 5. Plan (open; no result presumed)

Post-freeze: read the UMR verdict, erratum v2 and the UMR ranges needed at p=19; derive the exact cell constants for
each cell from the accepted UMR text; test level windows at the central levels, including a combination of
adjacent levels, for each cell. Either close each full cell or stop at its first unproved lemma and state a
checkable residual (explicit integer data plus the exact conditions it must satisfy).

## 6. Rules and non-claims

Written mathematics only, in English, by hand. Files are created exclusively with Python open(path,'x') and are
never edited, overwritten, moved or deleted; corrections go into new erratum files. Checkpoints in checkpoints/ at
most 1800 s apart (target 1200 s) and around substantial subcases. Allowed machine steps only: `/bin/date`,
`shasum -a 256`, byte/LF counts, reading files, mkdir, exclusive creation of drafted text. No assertion
statements, scripts or computation over mathematical objects, enumeration, tests, solvers, Lean, model CLIs,
network, /tmp, nested agents, deletion, commit or push. One review packet of at most 100 KB, then park.
Non-claims: no other cell, kappa, prime or k; no full p=19 or full ordered Olson; no priority, novelty, "first",
human-referee, Lean or runtime claim; no review or acceptance is claimed by this worker.
