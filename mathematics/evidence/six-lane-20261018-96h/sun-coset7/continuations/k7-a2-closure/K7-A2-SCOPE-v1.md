# K7-A2-SCOPE-v1: frozen scope for the written closure of the K7 subfamily (a2) [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this write: 2026-10-19T13:25:54-0700. Frozen **before** any derivation in this directory
  (directory created empty at 2026-10-19T13:25:29-0700).
- **Owner:** SunM13MixedFibres. Owned path, new files only:
  `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-a2-closure/`.
  Exclusive-create files only; corrections are new versions/errata. Written mathematics only: no scientific computation,
  enumeration, solver, Lean, CLI/model call, nested agent, /tmp, commit or push; hash/byte/range metadata only.
- **Authority:** parent transition `RUN/control/mathematics-slot-transition-sun-20261019-1325-v1.json`, sha256
  4b617b815ae3ae96adc769e86b84e7840fd79612967da605be5e113800092697, and the parent IRC that announced it. RUN :=
  `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`. Not runtime authority.

## 1. Target (fixed now)
**Subfamily (a2) of K7** (O16/README.md class K7: seven pairwise disjoint left cosets, all pairwise index gcds 6, so
n_i = 6 r_i with pairwise coprime r_i): three distinct vertices z, t, p with r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p,
E, A, B >= 1; the four other vertices W' are unmarked (r_u = w_u); all w's pairwise coprime and prime to 30; all exponents and
cofactors unbounded; arbitrary groups via R0.
- **Primary target, Theorem A2X:** (a2) contains no configuration, in any group with finite-index subgroups.
- **Mandatory sub-obligations:** (a) the exact split of (a2) into (a2-no5) (no entry 5 in either matrix) and (a2-zt5)
  (alpha_zt = 5 or alpha*_zt = 5), derived from the accepted Lemma F, with no omitted branch; (b) (a2-zt5) normalized to
  alpha_zt = 5 by the ACTUAL inversion, the other component covered explicitly; (c) every internal case split (orientation
  roles, sizes of the z-row three-sets, Case A/B/mirror or replacements) shown exhaustive, with no four-case omission;
  (d) R0 lift.
- **Deliverable shape:** complete written proof with an exact interface and dependency table, split into at most THREE
  genuinely self-contained review units, each <= 70,000 raw bytes including the accepted input STATEMENTS and mandatory
  overlays it uses, with an acyclic join and no hidden conditional import; reuse of older arguments attributed, not claimed.
- **Fallback (if not closed):** the exact obstruction (failing step, retained arithmetic), every genuinely new necessary
  constraint, any separately NAMED closed sub-branch, and the exact smallest missing bridge; (a2) stated OPEN. Never call
  a conditional or partial statement a closure. Full K7 and Sun(7) are outside the scope.

## 2. Premise discipline (fixed now)
- **Accepted, at their exact verdict scopes and with ALL their mandatory overlays:** RUN/review/sun7-K7-R2-parent-verdict-v1.md
  (9b0f7df5…926d; (a1) closure, vertex-wise CELL at its exact hypotheses, mandatory E1-E29 and ecff R2.1-R2.4);
  RUN/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md (2a7c5b6c…f966; OV v1 then v2; Lemma F, FG-a2, Cor 5/6-a2, D23-a2,
  ZT5 S1-S5, BRIDGE in its A2.10 form, A2-TRANSFER only for its named list); RUN/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md
  (1167bc4f…aec0; D23P: both z-rows of type (b')); RUN/review/sun7-lfc-inv-parent-verdict-v1.md (8621e744…cca18; LFC, INV, R0);
  the written verdict R16/sun-coset7-written-parent-verdict-v1.md (73a25ba6…9f35; L0.1-L0.3, L1, VFC); Sun(2)-Sun(4);
  Sun(5)/Sun(6) computer-assisted, transitive only.
- **Pending, NOT premises:** the family closure map v2 (conditional), TX = K7-CASEA-CELL-A2-TRANSFER-v1.md, ZA/ZB =
  K7-A2-ZT5-A/B-v1.md with errata v1-v4, the R3 parts of K7-R2-R3-consolidated-erratum-v1.md, and anything whose only review
  status is a first-family or repair-only acceptance (R3a/R3b ended NO_VERDICT). Needed steps are re-derived or simplified
  and attributed. K62 Proposition SG is NOT transferred outside K6.2*; any K7 subset-granularity step must be proved from K7
  hypotheses. The accepted (a1) proof and the closed K6.3 are not redone.

## 3. Route (pre-freeze disclosure)
Before this freeze I only read the transition record, the four accepted verdicts and the conditional closure map v2
(sections 1-5); I derived nothing. Planned order: (1) read the accepted (a2) statements (A2-FIVE through OV v1/v2; D23P) and
the accepted (a1) chain interfaces (K23/CELL through E1-E29), then the pending TX/ZA/ZB texts; (2) write the exact
no5/zt5 partition; (3) for (a2-no5), decide whether the accepted A2-TRANSFER list plus a re-derived K23/CELL transfer closes
it; (4) for (a2-zt5), re-derive or replace the pending ZT5-A/B steps; (5) if a step fails, record the obstruction.

## 4. Deliverables
`K7-A2-UNIT-*-v1.md` (at most three self-contained review units <= 70,000 raw bytes each) with an interface/dependency table,
or an obstruction note; review package(s) and JSON excerpt manifest(s) {path, sha256, start, end}; checkpoints
`checkpoint-NNN-v1.md` at most 1800 s apart with `/bin/date`; IRC of paths/SHAs; then park. Every new claim
CANDIDATE_UNVERIFIED; no full K7, Sun(7), novelty, Lean or human-review claim.
