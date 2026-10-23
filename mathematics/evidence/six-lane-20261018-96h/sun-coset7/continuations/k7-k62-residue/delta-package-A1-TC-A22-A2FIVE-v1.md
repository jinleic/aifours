# Delta package for dual review: (a1) residue narrowing and (a2) five-entry reduction (Sun7K62Successor)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:34:23-0700.
- **Purpose:** the single delta-package list requested by the parent after the RICH/D23P verdict. Manifest only; no new
  mathematics, no computation. All four candidates are frozen byte-identical in
  `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/`.
- **Accepted base (discharges the former RICH condition):** `RUN/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` (sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0): `K7-D23-RICH-v1.md` (ba32d282...f2bb3) + erratum-1
  (8261831b...0ba69, R-1 mandatory) + consolidated erratum `K7-D23RICH-D23P-erratum-v1.md` (55cb66ca...4d428), and
  `K7-D23P-v1.md` (89739dc2...37880) + the consolidated erratum. RICH's FG7 is accepted in chain form (a)/(b).
- Other accepted imports referred to below: LFC (a)-(d), INV (a)-(b), errata E1/E2/E6/E7/E8 (verdict 8621e744...ca18, item 6
  = R0 for alpha*); L0.1, L0.3, L1 (T, tau_min/tau_max), VFC (V1)-(V4) (written verdict 73a25ba6...3f9d / rules-k7-v1
  77b9afec...cee); D23-MIX (verdict d3453de1...e37db). Transitive closure of all four files reaches the computer-assisted
  Sun(5)/Sun(6) records (2cf02436...5301, efe1d849...1e29) through these packages.

## Review order and items

| # | file | sha256 | bytes | written |
|---|---|---|---|---|
| 1 | `K7-A1-STRUCT-v1.md` | c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf | 15594 | 05:42:53 |
| 2 | `K7-TC-v1.md` | cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117 | 11375 | 06:04:04 |
| 3 | `K7-TC-A22-v1.md` | 9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41 | 4945 | 06:07:57 |
| 4 | `K7-A2-FIVE-v1.md` | 93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc | 17424 | 06:33:35 |

### 1. K7-A1-STRUCT-v1 (setting (a1))
- **Claims:** section 1 Corollary W3 (W3 = W3* = empty); section 2 Lemma E3 (no W-t entry 3); section 3 Lemma PFG-t (i)-(ii)
  with Corollary L (allowed t-rows; at least two t-entries 4 when Gamma^x is connected); section 4 Lemma B; section 5
  Theorem K7-CASEB. Section 6 (patterns Q_B, Pc5') and section 7 are an obstruction/navigation record, **not claims**.
- **Accepted imports:** RICH: G0; FG7 chain form (a) (PFG-t (i) uses k <= x_ej for an earlier tree-neighbour j);
  Corollary 5/6 (val <= 5 at u in W, both orientations); NO5; Lemma R3 (rows with a W-three are S1-S4); TZ; LZ; Theorem
  K7-D23-RICH. D23-MIX; LFC; INV; E8 standard weights; L1 (T); VFC (V1)-(V4); R0.
- **Co-packaged imports:** none.
- **Direct Sun instances:** Sun(2)-Sun(4) through LFC (c)/VFC (V3), and **Sun(5)** exactly in the two/four-class rule "no
  5-set" used in Corollary L (cases 44441, 44444).

### 2. K7-TC-v1 (setting (a1))
- **Claims:** Lemma TC (cross-apex transfer, both orientations); rigid rows R1, R3, R4, R5 with their forced containments,
  and the exclusion of ({1,4,4,4} | c | 1); Theorem K7-TC-B (Case B: alpha*_v1v2 = 2 and alpha* = 2 on T*); Proposition
  TC-P (pattern Pc5' impossible). Section 5 (pattern Q_B') and section 6 are navigation, **not claims**.
- **Accepted imports:** RICH Corollary 5/6 with its equality clause and FG7 (for C^alpha and C^alpha*; the "union <= 5/6"
  steps); LFC; INV (a)-(b); VFC (V1), (V3), (V4); L1 (T); R0.
- **Co-packaged imports:** A1-STRUCT section 0 (triangle evaluation, two/four classes), Corollary W3, Lemma E3, Lemma B,
  Theorem K7-CASEB.
- **Direct Sun instances:** Sun(2)-Sun(4).

### 3. K7-TC-A22-v1 (setting (a1))
- **Claims:** Theorem K7-TC-A22: in Case A (T = T* = W) there is no configuration in which every W-vertex has exactly two
  alpha-fours and two alpha*-fours. Section 4 (remaining Case A) is navigation, **not a claim**.
- **Accepted imports:** RICH NO5, Corollary 5/6, FG7; LFC; INV; VFC (V1), (V3), (V4); R0.
- **Co-packaged imports:** A1-STRUCT section 0 (triangle rule (1, a, b) passes only for a = b), Corollary W3, Lemma E3,
  Lemma PFG-t with Corollary L; K7-TC Lemma TC and row R1.
- **Direct Sun instances:** Sun(2)-Sun(4).

### 4. K7-A2-FIVE-v1 (setting (a2))
- **Claims:** Lemma F (F1)-(F7) (the only possible five is z-t, in one orientation, with z-row (3,3,3,3 | p 3 | t 5));
  Lemma FG-a2 with Corollary 5/6-a2; Lemma D23-a2 (without a z-t five the z-row is 3-type relative to W' cup p);
  Proposition K7-A2-ZT5 ((S1)-(S5), including E >= 2); Theorem K7-A2-BRIDGE (in (a2-no5) all RICH conclusions hold with
  W = W' cup p; in particular no (a2-no5) configuration has T* subset W3 or T subset W3*).
- **Accepted imports:** D23P (both z-rows (b')); RICH (G0, the FG7 chain proof and the Corollary 5/6 proof re-run, and
  for the bridge every RICH statement and proof); LFC; INV; E1/E2/E6/E7/E8; L0.1; L0.3; L1; VFC; R0.
- **Conditional part:** Corollary K7-A2-TRANSFER only, on items 1-3 of this package.
- **Direct Sun instances:** Sun(2)-Sun(4).

## Suggested reviewer focus
- Item 1: the triangle table of section 0, the two/four-class allowed sets, every Corollary L weight and the z-compatibility
  claims, Lemma B's weights, the CASEB position argument.
- Item 2: the value-5 weights and forced containments of R1/R3/R4/R5, the transfer orientation (C^alpha* in section 3,
  C^alpha in section 4), and the three measure counts (11/12, 11/12, >= 1).
- Item 3: the twin rule on the 5-cycle, the e = 1 version of R1, the 5-cycle neighbour lemma, the count of section 2.
- Item 4: every weight vector of Lemma F and D23-a2, the third-marked-vertex gcd in FG-a2 (a), the inverse step in the
  last branch of (F6), the light-fibre count of (S5), and (B1)-(B7) against the text of RICH.

## Status
All four are unreviewed single-author candidates. The (a1) residue (Case A with a vertex of four-degree type
(3,1)/(1,3)/(2,1)/(1,2); Case B containing Q_B'), (a2-zt5) beyond (S1)-(S5), the (a1)-type residue inside (a2-no5),
K6.2* and full Sun(7) remain OPEN. No novelty, Lean or human-review claim.
