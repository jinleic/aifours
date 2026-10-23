# K62-M3R-SCOPE-v1: frozen scope for closing the M3(1,1) residual instances R1 and R2 [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T11:27:50-0700. Frozen **before** the
  written derivation.
- **Owner:** SunK62Regimes; owned path `.../sun-coset7/continuations/k62-regimes/` only; new files only (exclusive
  creates); K62-MK-v1/v2, its scope, package and manifest and every other older file stay immutable. Written research only;
  no compute GO; no model call; no enumeration code.
- **Instruction:** parent IRC (Main) after receiving the MK packet: close the M3(1,1) residual isolated by K62-MK-v2
  (R1- and R2-instances), including every 5-marker placement admissible in M3(1,1). RUN :=
  `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Premise discipline.** K62-MK-v2 (sha256 ab7cfcb6ccebb19465eb6dfc3f96580d58c599a2507aee697604f691ad5abee9) is a PENDING
  candidate: its Theorem M3R is used only as an explicitly labelled conditional premise, and any lemma of it that a new proof
  needs is re-proved. GS is cited only through `RUN/review/sun7-K62-GS-parent-verdict-v1.md` (sha256
  3a01c9e495a9bc6d7fbf8f03cbf981df9aa9a9dc70b8e9273ffe87803c19dfc2) with its erratum `RUN/review/sun7-K62-GS-parent-erratum-v1.md`
  (sha256 9c60e4187748eddaf7997201a3e208dce7a86ba86a349db1359648c4c797616b), at its G scope only (it is not expected to be
  needed). M13 ((1,3)/(3,1)) is neither used nor touched.
- **Disclosure (pre-freeze, unwritten):** (1) at t an R1-instance gives Phi_tPhi_a = Phi_tPhi_b; the subgroup
  W := <Phi_a, Phi_b> then satisfies Phi_tW = Phi_tPhi_a (the rules-k7-v1 L6 argument, to be re-proved), [G : W] = m with
  m | 6 and 2m/3 = [Phi_t : Phi_t cap W] an integer, so m in {3, 6}; a sketch suggests m = 3 dies by Sun(3) inside W (the
  a-, b- and d-pieces in the W-coset outside Phi_tW) and m = 6 forces the a- and b-pieces into two distinct W-cosets avoided by
  the d-piece; (2) 9 | T_y(V minus {t}) appears equivalent to tau_y(d, i*, e) = 3 for some e in O minus {t}. Nothing is
  checked; any of this may fail and will then be preserved with its exact obstruction.

## 1. Setting
M3(1,1) exactly as in K62-MK-v2 section 0: K6.2*, e_d >= 4, e* = 2, the 3-marker on t in O (f_t >= 2, f* = 1),
(alpha_(d i*), alpha*_(d i*)) = (1,1), the 5-marker on d, on i*, on t, on some p in O minus {t}, or absent; all exponents and
w-parts unbounded. R1- and R2-instances as defined there.

## 2. Target statements (fixed now)
- **Theorem R1X:** no configuration of M3(1,1) has an R1-instance.
- **Theorem R2X:** no configuration of M3(1,1) has an R2-instance.
- **Corollary M3E (CONDITIONAL ON K62-MK-v2 Theorem M3R):** M3(1,1) is empty; together with K62-E3 (accepted), the GS
  verdict (G empty) and K62-MK-v2 Theorem M5 (pending, stated as a conditional premise), every K6.2* configuration lies in
  the (1,3)/(3,1) orientations (M13), stated only as a conditional navigation consequence.
- **Fallback (if R1X or R2X is not achieved):** an obstruction note giving, for the open instance type, (a) every necessary
  condition derived in writing, (b) the exact failed branch(es) with their obstruction (for example granularity at t forcing
  18 | gcd), (c) the smallest missing lemma, (d) any sub-case proved unconditionally with its exact defining condition. No
  other claim.

## 3. Tools allowed
- Parent-accepted imports at original scopes: LFC/INV (8621e744…), rules-k7-v1 L1 and VFC (73a25ba6…), K62-E3
  (576969dd…: Lemmas 1-3, C1, C2 with its proof sub-claim (a) under its orientation hypotheses), SH-DG (cae455c3…: SH, DG-1..4,
  Theorem DG), CAP-DT (84061c6f…: C1, C2 at i* with f* = 1, RC-O, RC-i*, CI at unmarked v, apex table), R0, L0.1, Sun(k) for
  k <= 6 in any group (old README section 0; Sun(5)/Sun(6) computer-assisted).
- New elementary group-theoretic arguments proved in the file (for example the L6-type subgroup W and fibre counts over
  W-cosets using Sun(k), k <= 6, inside W only). FH (rules-k7-v1 L5 with seven pieces, least-order frame) is not used.

## 4. Deliverables
`K62-M3R-v1.md` (proof or obstruction note), review package and excerpt manifest (<= 100 KB embedded), all
CANDIDATE_UNVERIFIED; checkpoints <= 1800 s apart with `/bin/date`; paths and SHA256 to the parent. No novelty, priority, Lean
or human-review claim; computer-assisted Sun(5)/Sun(6) remain transitive imports.
