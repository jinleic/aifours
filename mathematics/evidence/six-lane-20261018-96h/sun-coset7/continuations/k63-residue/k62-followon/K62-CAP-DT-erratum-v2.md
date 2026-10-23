# K62-CAP-DT-erratum-v2: the consolidated MINOR fixes from both repair reviews

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T08:25:01-0700.
- **Overlays, frozen unchanged:** `K62-CAP-DT-erratum-v1.md`, sha256 996f924c731f0bfb1bf2a336d50d6ac0be50e55fb4ce134fa4b3cec2a1e2466d; and the DT-B parenthetical named in V10,
  `K62-DT-B-v1.md`, sha256 51960d44d60fa50901a3201143410f935750852d1ccd4c6e116f81a9c601604f.
- **Responds to:** Codex repair review `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-repair-codex-v1.prompt.stdout.txt`, sha256 ea2292637a09e66fa0108107766b126a3955eb4312ebc71c9df708d221575c97,
  ACCEPT_REPAIRS_WITH_FIXES, 0 FATAL / 0 MAJOR / 2 MINOR; Claude repair review `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-repair-claude-v1.prompt.note.md`,
  sha256 816ceaf719a0b93364c480fe0df8bfa5a6ab49af2243984845415cd328ed4497, 0 FATAL / 0 MAJOR / 9 MINOR, plus its uncounted pairing editorial.
- **Rules:** one overlay, exact Old/New; each Old block was checked to occur exactly once in its frozen target. V1-V9 and
  V11-V14 replace only text in the first overlay; V10 replaces only the stale base-DT-B parenthetical. Every other first-
  overlay correction remains in force. No statement is strengthened and no new mathematical proof is added. V12/V14
  align captions and explanations with the requested citation/LOSSY repairs, not extra changes. All candidates remain
  candidates until the parent verdict. No computation.

## Disposition
| Review finding | Items |
|---|---|
| Codex M1 / Claude W1 | V3 |
| Codex M1 / Claude W2 | V8, V14 |
| Codex M2 / Claude G1 | V2 |
| Claude R1 | V4-V6 |
| Claude R2 | V7 |
| Claude S1/S2 | V9 |
| Claude G2 | V10 |
| Claude G3(a) | V1 |
| Claude G3(b) | V11-V12 |
| Claude pairing editorial | V13 |

## V1: Claude G3(a): include DG-4 without extending its scope.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
- In `K62-DT-A-v1.md` (heading of section 3), `K62-DT-B-v1.md` (Labels bullet; headings of sections 3 and 4) and
  `K62-DT-C-v1.md` (Labels bullet; heading of C3), "CONDITIONAL ON DG" reads: "depends on Theorem DG, accepted by verdict
  `RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md` (sha256 cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda) as
  CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, with DG's orientation (the family x needs x'_(d i*) = 1) and four-subset hypothesis
  explicit". DT-A gets the same change as explicit text in CD8.
```

**New:**
```text
- In `K62-DT-A-v1.md` (heading of section 3), `K62-DT-B-v1.md` (Labels bullet; headings of sections 3 and 4) and
  `K62-DT-C-v1.md` (Labels bullet; heading of C3), "CONDITIONAL ON DG" reads: "depends on Theorem DG and, in B4's other
  branch, Lemma DG-4, at the scope of `RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md` (sha256
  cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda), CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, read through
  K62-DG-erratum-v1 e435430c… and K62-SH-DG-erratum-v1 755edc21…. Theorem DG for the family x requires x'_(d i*) = 1;
  its (a)/(b) keep the capped-four-subset hypothesis. DG-4 concerns an unmarked added vertex and raw depths, with the
  family swap via INV (a)/E6 in G (both distinguished entries 1)". DT-A gets the Theorem DG status change explicitly in CD8.
```

## V2: Codex M2 / Claude G1: both missed citation strings quoted verbatim.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
- In DT-A, DT-B and DT-C, "the 5/6 row bounds of K62-CAP (C)", "the O-row bounds of K62-CAP (C)" and "(K62-CAP (C))" used
  as a row bound read "Lemma RC (item CD3) with (C1) for the opposite family". "The 11/12 bound" reads "(RC-i*)", which
  needs f* = 1.
```

**New:**
```text
- In DT-A, DT-B and DT-C, every CAP citation used for a row bound reads "Lemma RC, case (RC-O), with (C1) for the
  opposite family", or "(RC-i*), with f* = 1", as appropriate. This explicitly includes DT-B Labels' "the 5/6 row bounds
  of `K62-CAP-v1.md` (C)" and DT-C Labels' "5/6 bound of `K62-CAP-v1.md`", as well as "the 5/6 row bounds of K62-CAP (C)",
  "the O-row bounds of K62-CAP (C)" and "(K62-CAP (C))" when used as row-bound citations. The VFC union-bound use of (C1)
  for the family's own x (bounding the x'-row) in CI is not redirected.
```

## V3: Codex M1 / Claude W1: falsity only for S_x; N(O) equivalence holds by integrality but is withdrawn as unneeded.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
After the review freeze, my IRC answer to the parent's question Q2 claimed two things. First, that DG's bound
"S <= 19/16 - 2/n_d" is *equivalent*, on the 1/32 grid, to the pattern-level predicate "S < 19/16" (S <= 37/32), so that
"nothing is lost". Second, the same for "N(O)/n_d < 1/8" in place of "N(O) <= n_d/8 - 1/2". **Both claims are false and are
withdrawn**; the withdrawal was first recorded in `checkpoint-013-v1.md` (sha256 9c6102199c6327427ffe38ebbb964e07f318f7e78fb3d73d2143de6f4dc44112). The grid argument absorbs 2/n_d only when 2/n_d <= 1/32, i.e. n_d >= 64. Counterexamples to
equivalence:
- at n_d = 16, DG gives S <= 17/16, while S < 19/16 admits 18/16 (for example eight terms 1/8 and two terms 1/16);
- at n_d = 32, DG gives S <= 36/32, while the grid test admits 37/32.
The correct statement is CD4 (D3)-(D4): pattern-level predicates are safe necessary weakenings and are lossy in general.
No equivalence for n_d >= 64 is claimed here. My Q1 answer stands and is item CD2.
```

**New:**
```text
After the review freeze, my IRC answer to the parent's question Q2 claimed two things. First, that DG's bound
"S <= 19/16 - 2/n_d" is equivalent, on the 1/32 grid, to "S < 19/16" (S <= 37/32), so "nothing is lost". Second, the same
for "N(O)/n_d < 1/8" in place of "N(O) <= n_d/8 - 1/2". **The first claim is false**, as the counterexamples below show.
**The second holds by integrality**, but it is withdrawn as unneeded, and no rule relies on it: N(O) and n_d/8 are integers,
so N(O) <= n_d/8 - 1/2 iff N(O) <= n_d/8 - 1 iff N(O)/n_d < 1/8. This does not make N(O)/n_d a function of pi. The earlier
withdrawal in checkpoint-013-v1.md (9c610219…) incorrectly called the second claim false; that wording is superseded here.
Both claims of a needed lossless pattern-level replacement are withdrawn.
Counterexamples to the first equivalence:
- at n_d = 16, DG gives S <= 17/16, while S < 19/16 admits 18/16 (eight terms 1/8 and two terms 1/16);
- at n_d = 32, DG gives S <= 36/32, while the grid test admits 37/32.
Strict replacements are used only as LOSSY necessary consequences; no source equivalence is asserted or used. Some
replacements are strictly weaker, as in these two S_x examples. No equivalence for n_d >= 64 is claimed or needed here.
My Q1 answer stands and is item CD2.
```

## V4: Claude R1: rule imports are restricted to the two frozen cases.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
- (RC-O) if v in O is unmarked and **x'_(d i*) = 1**, (C1) applied to x' gives the bound 5/6;
- (RC-i*) if v = i* and f* = 1, (C2) applied to x' gives the bound 11/12.
```

**New:**
```text
- (RC-O) if v in O is unmarked and **x'_(d i*) = 1**, (C1) applied to x' gives the bound 5/6;
- (RC-i*) if v = i* and f* = 1, (C2) applied to x' gives the bound 11/12.
*Rule-import scope:* Rules import Lemma RC only through (RC-O) and (RC-i*). Elsewhere its slack
1/gcd(n_v, T_x'(V minus {v})) is not a pattern quantity, and (D3) yields only sum_j y_j x_vj/g_vj < 1, i.e. LFC (d), not a
new numerical pattern bound. The general light-fibre calculation is proof context, not an additional black-box pattern
rule.
```

## V5: Claude R1: D2 does not admit all of general RC as a rule.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
- (D2) it reads only pi and the quantities of (B), together with the bounds of (C) and Lemma RC;
```

**New:**
```text
- (D2) it reads only pi and the quantities of (B), together with the bounds of (C) and only (RC-O)/(RC-i*) of Lemma RC;
```

## V6: Claude R1: intersection indices are included among non-pattern slacks.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
  an inequality X <= c - epsilon(Gamma) with epsilon(Gamma) > 0 depending on n_v, n_d, the w's or absolute counts yields
```

**New:**
```text
  an inequality X <= c - epsilon(Gamma) with epsilon(Gamma) > 0 depending on n_v, n_d, intersection indices T, the w's or absolute counts yields
```

## V7: Claude R2: exact RC provenance.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
Both enter through LFC (c) or (V3). Lemma RC is LFC (a)-(d) plus index arithmetic. Its allowed-set notion is LFC (c),
which is proved via Sun(|T|) for |T| <= 6. Sun(4) enters only through accepted K62-E3 (Lemma 1, step 2).
```

**New:**
```text
Both enter through LFC (c) or (V3). Lemma RC uses LFC (a)-(c), superseding (d), plus L0.1 with Lagrange and
INV (a)-(b) with E6. Its allowed-set notion is LFC (c), proved via Sun(|T|) for |T| <= 6. Sun(4) enters only through accepted
K62-E3 (Lemma 1, step 2).
```

## V8: Codex M1 / Claude W2: operational LOSSY discipline, not universal non-equivalence.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
**Strict weakenings are lossy; they are not equivalent to their sources.**
```

**New:**
```text
**Strict weakenings are labelled LOSSY and used only as necessary consequences. No rule or consumer may use one as an
equivalence; some are strictly weaker than their source (Theorem DG (a) at n_d in {16,32}).**
```

## V9: Claude S1/S2: CI' explicit, lie among, CAP (D3)-(D4) forms.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
Inside G, the patterns not excluded by Parts A-B are the G-patterns in U62 that satisfy, in both families, (R3), (R4),
B1-B5 and the accepted K62-E3 (Lemma 2, C2), K62-SH/DG (DG with its explicit orientation and four-subset hypothesis) and
L1 constraints; Part C adds C1-C3. This describes what remains; it is not a characterization of realizable patterns and
```

**New:**
```text
Inside G, the patterns not excluded by Parts A-B lie among the G-patterns in U62 that satisfy, in both families, (R3),
(R4), CI' (both families, every O-vertex), B1-B5 and the accepted K62-E3 (Lemma 2, C2), K62-SH/DG (DG with its explicit
orientation and four-subset hypothesis; in their CAP (D3)-(D4) forms) and L1 constraints; Part C adds C1-C3. This describes
what remains; it is not a characterization of realizable patterns and
```

## V10: Claude G2: replace stale parenthetical through both mandatory errata.
*Target:* `K62-DT-B-v1.md`.

**Old:**
```text
(`K62-DG-v1.md` a4bfc41e… + erratum e435430c…, under dual review)
```

**New:**
```text
(`K62-DG-v1.md` a4bfc41e… read through `K62-DG-erratum-v1.md` e435430c… and
  `K62-SH-DG-erratum-v1.md` 755edc21…, accepted at the scope of parent verdict cae455c3…)
```

## V11: Claude G3(b): use L1 plus INV at its imported scopes.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
With tau a multiple of lcm(x's) and tau <= (product of the two smallest values) (Lemma DG-3 in its form of
K62-SH-DG-erratum-v1 G3, accepted; its elementary proof (L0.1, Lagrange, Z11 (a)) applies verbatim to either family;
"admissible" below means allowed by these two constraints and makes no realizability claim):
```

**New:**
```text
With tau a multiple of lcm(x's) and tau <= (product of the two smallest values) (rules-k7-v1 L1 for the configuration
whose alpha-matrix is x; for x = alpha* apply L1 to the inverted configuration, INV (a) with E6; these are the imports of
DT-A section 1; "admissible" below means allowed by these constraints and makes no realizability claim):
```

## V12: Claude G3(b): align CD9 caption/explanation with V11 only.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
## CD9: DT-A section 1: citation of the tau bound (DG-3 in its G3 form); "admissible"
*File:* `K62-DT-A-v1.md`. *Disposes:* Claude m7 (second and third clauses); Codex DT-A section 1 remark.
*Why:* Cites the tau bound in its accepted G3 form. The apex identity stays cited as L1 (T3) of rules-k7-v1 earlier in section 1, one of the two citations Claude m7 allows.
```

**New:**
```text
## CD9: DT-A section 1: citation of the tau bound (L1 plus INV); "admissible"
*File:* `K62-DT-A-v1.md`. *Disposes:* Claude m7 (second and third clauses); Codex DT-A section 1 remark.
*Why:* Cites rules-k7-v1 L1 for the original or inverted configuration (INV (a)/E6), already in DT-A's import list. The apex identity stays cited as L1 (T3).
```

## V13: Claude Editorial: reorder the pairing, no algebra change.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
*Proof.* K62-E3 C2 for alpha* (orientation alpha_(d i*) = 1) and for alpha (alpha*_(d i*) = 1): n_4(alpha) >= 2 n_1(alpha) + 2 and
n_4(alpha*) >= 2 n_1(alpha*) + 2, i.e. N41 + N42 >= 2(N14 + N11 + N12) + 2 and N14 + N24 >= 2(N41 + N11 + N21) + 2. Adding:
```

**New:**
```text
*Proof.* K62-E3 C2 for alpha (orientation alpha*_(d i*) = 1) and for alpha* (alpha_(d i*) = 1): n_4(alpha) >= 2 n_1(alpha) + 2 and
n_4(alpha*) >= 2 n_1(alpha*) + 2, i.e. N41 + N42 >= 2(N14 + N11 + N12) + 2 and N14 + N24 >= 2(N41 + N11 + N21) + 2. Adding:
```

## V14: Claude W2: align CD4 caption/explanation with V8 only.
*Target:* `K62-CAP-DT-erratum-v1.md`.

**Old:**
```text
## CD4: CAP (D): rule discipline; strict weakenings are lossy; quantifiers
*File:* `K62-CAP-v1.md`. *Disposes:* Claude m4; Codex "DG correction at pattern level" and CAP D quantifiers; parent's correction of my Q2 IRC claim (with W1).
*Why:* Makes explicit which predicates count as rules: side conditions decidable from pi; only slack-free normalized inequalities or strict necessary weakenings; rounding only onto lattices determined by pi. Records that strict weakenings are lossy, not equivalences. The transfer implication is unchanged.
```

**New:**
```text
## CD4: CAP (D): rule discipline; strict replacements labelled LOSSY; quantifiers
*File:* `K62-CAP-v1.md`. *Disposes:* Claude m4; Codex "DG correction at pattern level" and CAP D quantifiers; parent's correction of my Q2 IRC claim (with W1).
*Why:* Makes explicit which predicates count as rules: side conditions decidable from pi; only slack-free normalized inequalities or strict necessary weakenings; rounding only onto lattices determined by pi. Strict replacements are used only as LOSSY necessary consequences, with no equivalence used; some are strictly weaker. The transfer implication is unchanged.
```

## Boundary
The scoped partial claims of CAP/DT are unchanged. Nothing here supplies universal coverage or excludes the remaining
G-patterns, marked sub-cases, (1,3)/(3,1), full K6.2* or Sun(7). Computer-assisted Sun(5)/(6) provenance remains in the import
closure. No new computation, novelty, Lean or human-review claim.
