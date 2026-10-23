# KDM-SCOPE-v1 — short direct written proof attempt for K7 (a2) [target only; no claim]

- **Written:** `/bin/date` read at 2026-10-19T18:13:44-0700, immediately before this exclusive create (directory created empty just before).
  Owner SunM13MixedFibres, slot math-1. First `/bin/date` of this slice: 2026-10-19T18:12:26-0700.
- **Authority:** `RUN/control/written-k7-direct-marker-residual-scope-v1.json`, sha256
  bfaea95f585c1a9e97eea9bd60b981d50acf3883be7f193329b65529e1eb39bb (RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h).
- **Mandatory-first item done before this freeze:** `../sun7-written-import-cutover/CUT-erratum-v1.md`, sha256
  3da79c1c88442dedba09920253336b16b1e1a403f7b3ec33d1255c234948cc40, propagating the parent S56W erratum (b2299b6f…0aae).

## 1. Frozen target
**K7 (a2):** seven pairwise disjoint left cosets of finite-index subgroups of any group with n_i = 6 r_i, r_i pairwise
coprime; distinct vertices z, t, p with r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p (E, A, B >= 1, unbounded); the four other
vertices unmarked (r_u = w_u); all w pairwise coprime and coprime to 30. **Goal:** a SHORT independent written proof that
(a2) is empty, by left-fibre counts plus actual inversion, OR the exact local multiplier/marker obstruction where such an
argument stops. Alternative verification route for the still-unaccepted A2X target; not a new problem.

## 2. Premise discipline
- Allowed: elementary facts, R0, Sun(2) (re-proved), Zhu Sun(3), Sun(4); a restricted fibre count and actual inversion
  re-proved inside. If a Sun(5) or Sun(6) instance is needed it is labelled an explicit pending input (S5W/S6W via S56W with
  H5/H6, all UNREVIEWED), never the old computational theorem.
- Not premises or citations: A2 Units 1-3 or their closure (A2X); old long A2 arguments; the accepted NF and (a1) results
  (not re-proved either); StageB; any engine/certificate/count. Accepted K7-lane lemmas (Lemma F, FG-a2, D23P, S1-S5,
  BRIDGE, TRANSFER, ROW-1/2/U, M0, ...) are NOT cited, because their accepted provenance includes Sun(5)/Sun(6).
- If A2X is accepted while this work is in progress: stop duplicate closure and report only genuinely different value.

## 3. Prior exposure (disclosed)
I authored A2 Units 1-3 (the long A2X proof), K7-NF, SUN7-COMP and the other Sun-lane candidates, and have read the
accepted K7 verdicts (A1/A2 repairs incl. Lemma F, FG-a2, D23-a2, S1-S5, BRIDGE A2.10, TRANSFER; RICH/D23P; D23; R2; M0;
M1; Z2; K7-35; U1; Z23-P5; LFC/INV/ROW-U). I therefore know the old (a2) structure (only z-t can carry a 5, the no5/zt5
split, z-row types, T* sets, CELL). None of it will be cited.
**Pre-freeze sketch:** none written or derived for this route. Planned approach only: at a chosen apex (p, z, t or an
unmarked vertex) the six neighbours carry labels r_j alpha and masses alpha/6; group neighbours by the primes they can
share; find rows that survive a count using Sun(2)-Sun(4) only; then compare with the inverse family (alpha + alpha* <= 6);
record any surviving regime exactly.

## 4. Deliverables and governance
`KDM-v1.md` (proof or exact obstruction with failed routes), `review-package-KDM-v1.md`, `review-excerpts-KDM-v1.json`,
checkpoints <= 1800 s apart (target 1200 s), IRC with paths/SHA256s, park. All files exclusive-create; written-only; no
scientific scripts/assertions/enumeration/numerics; metadata only. CANDIDATE_UNVERIFIED; no acceptance or Sun(7) claim.
