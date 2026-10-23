# K62-M13-SCOPE-v1: scope note for the written slice on the (1,3)/(3,1) orientations of the K6.2* residue

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:54:30-0700. Frozen **before** any derivation of the slice.
- **Author:** Sun63Successor. Written mathematics only. The HOLD (`RUN/review/runtime-guard-admission-HOLD-v1.json`
  6c1d8440…) is in force, and no computation is planned or allowed. RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Instruction (parent IRC, after receiving `K62-CAP-DT-erratum-v1.md` 996f924c…):** start ONE written slice on the
  marked (1,3)/(3,1) orientation sub-cases of K6.2*, labelled CONDITIONAL on the CAP/DT verdict, citing exact statement
  scopes. Freeze a scope note before deriving. Checkpoints at most 1800 s apart. No computation. No claim about full
  K6.2* or Sun(7).

## 1. The sub-case
- **Class.** K6.2* with e_d >= 4, e* = 2 (the accepted frontier after K62-E3, verdict `RUN/review/sun7-K62E3-parent-verdict-v1.md`
  sha256 576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f).
- **Orientation (O13).** The joint d-i* entry is (alpha_(d i*), alpha*_(d i*)) = (1, 3), or (3, 1).
- **Consequences of the class.** By accepted K62-E3 Lemma 1, an entry 3 at d-i* occurs only if the 3-marker t lies in
  O, so f* = 1 and f_t >= 2. The 5-marker p may be anywhere admissible.
- **Reduction.** (3,1) reduces to (1,3) by INV (a) with E6 (accepted). The inverted configuration is again K6.2*, with the
  same indices and markers, and alpha and alpha* exchanged. **The slice works in (1,3)**; every result transfers to
  (3,1) with alpha and alpha* swapped.

## 2. Imports and exact scopes
**Accepted** (used only at these scopes):
- R0, the K6.2* class definition, P0/P1, old README section 0 L0.1 with Lagrange.
- E1; LFC (a)-(d) and INV (a)-(b) with E6 (verdict sha256 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18).
- rules-k7-v1 L1 (T3) and VFC (V1)-(V4) with the count (verdict 73a25ba6…).
- K62-E3 with errata v1-v2 (verdict 576969dd…): Lemma 1 including its gcd computation at d (gcd 9 only for (t, i*)
  when x = 3); Lemma 2 and C2 sub-claim (a) (O-O entries in {1, 2, 4} in both families); Lemma 3 in its proof form for
  every non-empty Q contained in O (Z10; orientation-free); steps 1-3; Corollaries (C1), (C2) in the orientation
  alpha_(d i*) = 1.
- K62-SH and K62-DG through both mandatory errata (verdict `RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md` sha256
  cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda, CORRECTNESS_ACCEPTED_SCOPED_PARTIAL):
  - SH-1, SH-2 and SH (i)-(iii); in particular **SH (ii)**: with alpha*_(d i*) = 3, every c in O minus {t} has
    alpha*_(i* c) in {2, 3, 4}, or alpha*_(i* c) = 5 with h_d >= 1.
  - **DG-1**, which does not require alpha_(d i*) = 1.
  - DG-2, DG-3 (G3 form), DG-4.
  - **Theorem DG** for the alpha*-family when alpha_(d i*) = 1, with its four-subset hypothesis and orientation explicit.

**Candidates pending the CAP/DT repair review** (`RUN/review/sun7-K62-CAP-DT-repair-review-freeze-v1.json` sha256
78cd1f690611bdceb102299655bc7896788b069eefb0276e3d9b1b8032dd9084). Every use is labelled **CONDITIONAL ON CAP/DT VERDICT**:
- CAP-62 (C1), (C2) and Lemma RC (`K62-CAP-DT-erratum-v1.md` item CD3);
- DT-A Lemma CI and Corollary CI';
- DT-B and DT-C lemmas.

## 3. Planned targets (to be derived; any of them may fail and will then be reported as failed)
- **Part A (accepted imports only): the second family at d.** In (1,3), study the inverted configuration's fibres at d,
  where alpha*_(d i*) = 3. Targets:
  - every fibre has at most three O-pieces, and at most four pieces, four only with both t and i*;
  - the three counting facts behind DG-2 hold for these fibres, so DG-2 and **Theorem DG hold for the alpha-family in
    (1,3)** (DG-1 applied to the inverted configuration);
  - **C2 for alpha**: n_4(alpha) >= 2 n_1(alpha) + 2;
  - the analogue of K62-E3 (C1) and step 4 for T_alpha;
  - the joint edge-class budget of DT-C C1, re-derived from C2 in both families.
- **Part B (accepted imports only, except where labelled): the i*-rows.** For a family x put
  K_x := {c in O : x_(i* c) in {1, 2}}. Targets:
  - |K_x| != 4 for both families, in any orientation (LFC certificates at i*);
  - in (1,3), |K_alpha*| != 5 (via SH (ii));
  - CONDITIONAL ON CAP/DT VERDICT: |K_alpha| != 5 (via (RC-i*), using f* = 1).
- **Part C (CONDITIONAL ON CAP/DT VERDICT): second-family granularity at unmarked O-vertices.** Targets:
  - a chain lemma giving gcd(n_v, T_alpha*(V minus {v})) | 6 at every unmarked v in O (the (C1) of CAP fails in
    general for alpha* here, since alpha*_(d i*) = 3);
  - hence the 5/6 bound for the alpha-rows, and CI/CI' for the alpha*-family, at unmarked O-vertices.
- **Part D (if reached; labelled as its premises require).** The row facts (R3)/(R4) of DT-B at unmarked O-vertices
  whose neighbours include the marked t (and p), and a precise description of what remains of (1,3).

## 4. Non-goals and boundaries
- No exclusion of K6.2* or of the (1,3) sub-case is promised; no claim about full K6.2* or Sun(7).
- No enumeration of U62; no computation; no K7 work.
- No novelty, Lean or human-review claim.
- Results of this slice are candidates until the parent reviews them.

## 5. Files and process
- **New files** go only in `k62-followon/`, by exclusive creates with versioned names: `K62-M13-A-v1.md`,
  `K62-M13-B-v1.md`, `K62-M13-C-v1.md` (and D if reached).
- Each frozen part is sent to the parent with path, SHA and exact scope.
- Checkpoints at most 1800 s apart, timestamps from `/bin/date`.
- **Provenance.** Planned direct Sun instances: Sun(2), Sun(3), Sun(4), through LFC (c). The computer-assisted Sun(5)
  and Sun(6) remain in the import closure through the accepted LFC package and the class reduction.
