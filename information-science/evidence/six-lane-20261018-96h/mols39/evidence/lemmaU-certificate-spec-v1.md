# Certificate specification for Lemma U (exact anchor) — v1 (2026-10-19T06:10:02-0700, ContinueCFR21)

Status: SPECIFICATION ONLY. Nothing has been produced, computed or run under this specification. The global HOLD
applies; producing or checking a certificate needs an item-specific parent GO. Source of the idea: Claude review note
78f13c8806b67c284b202413d93447fb4c60684e329ef9bf503e8dabe8dd14ae, section 7 ("optional strengthening").
Disposition context: erratum 2 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/erratum2-R1-S4-v1.md (sha256 88a4369970414303d6f90af127bb996827c76456cfef2c22cb70ce0c7db8cc84).
Purpose: let a tiny independent checker (stdlib Python, or later Lean) re-verify Lemma U for the exact anchor
without trusting route 1, route 2 or the parent's dense control. It certifies only the finite statement below.

## 1. Statement certified
Anchor D = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/controls-v1/dm39_six_anchor.raw
(sha256 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a): 6 rows x 39 columns, rows and columns
in file order, entries read mod 39. Notation: D'_x = D_x - D_0, beta = D' mod 13, alpha = D' mod 3, fibres
T_xy(t) for 0 <= x < y <= 5 and t in Z_13 (15 * 13 = 195 fibres). W = the gauged unknowns A_x(c) in F_3,
x = 1..5, c = 1..38 (190 unknowns; A_0 = 0 and A_x(0) = 0). E = the 195 fibre-sum equations
sum over c in T_xy(t) of (A_x(c) - A_y(c)) = 0, restricted to W.
Certified claim: the solution space of E in W has dimension exactly 5, and exactly two of its 3^5 = 243 points are
rainbow (every fibre carries 3 distinct differences), namely +-alpha^, where alpha^_x(c) = alpha_x(c) - alpha_x(0).
Lemma U as stated in erratum 2 section C then follows by the two-line argument of erratum 2 B.m11(iv), which is a
human proof and not part of the certificate.

## 2. Fixed conventions (part of the specification)
- Variable index: v(x, c) = (x - 1) * 38 + (c - 1) for x = 1..5, c = 1..38 (0..189).
- Fibre and equation index: pairs (x, y) in lexicographic order (0,1), (0,2), ..., (4,5) as p = 0..14;
  equation index j = 13 p + t. The checker recomputes every fibre from D; the certificate does not list them.
- Field: F_3 with representatives {0, 1, 2}; all arithmetic is exact integer arithmetic mod 3.
- Encoding: one JSON object, UTF-8, keys sorted; certificate digest = sha256 of the file bytes.

## 3. Certificate content
(a) "anchor_sha256": must equal 3c8dbe62...; the checker re-hashes the anchor file it reads.
(b) "basis": 5 vectors b_1..b_5 in F_3^190 (lists of 190 integers).
(c) "free_columns": 5 distinct variable indices f_1..f_5 such that the 5x5 matrix (b_i[f_k]) is the identity.
    This proves the five vectors are linearly independent.
(d) "rank_witness": 185 records (pivot p_i, combination {j: coefficient}), each a sparse F_3 combination of the
    equations. Let R_i = sum_j coef_ij * E_j (a vector in F_3^190). Required: R_i[p_i] = 1, R_i[p_k] = 0 for k != i,
    and the 185 pivots are distinct and disjoint from the free columns. Then the 185 rows R_i are linearly
    independent, so rank(E) >= 185 and dim(solution space) <= 5.
(e) "rainbow_points": two coefficient vectors z+ and z- in F_3^5 whose points sum_i z_i b_i equal alpha^ and -alpha^.
(f) "failures": for each of the other 241 vectors z in F_3^5 (lexicographic order, excluding z+ and z-), one
    equation index j such that, on fibre j, the point sum_i z_i b_i does not carry 3 distinct differences.

## 4. Checker obligations
A checker accepts only if every check passes:
1. Anchor bytes hash to 3c8dbe62...; 6 x 39 integers; D is a (Z_39,6;1)-DM (all 15 row differences are bijections);
   every fibre has exactly 3 columns.
2. Every b_i satisfies all 195 equations (195 x 5 sparse evaluations).
3. Free-column identity check (c).
4. Rank witness (d): recompute each R_i from E and the coefficients, then check the pivot pattern.
   With 2 and 3 this proves that the solution space is exactly span(b_1..b_5) (dimension 5).
5. Rainbow points (e): recompute alpha^ from D and check equality; check every fibre of +-alpha^ directly.
6. Failures (f): exactly 241 entries, covering every z other than z+ and z-, each with a fibre that really fails.
7. Output: one JSON line with "verdict" VALID or INVALID, the failing check, the certificate digest, and the anchor
   digest. Exit 0 only for VALID.
Size estimate: (b) 950 entries, (d) at most 185 x 195 coefficients (sparse in practice), (f) 241 entries; total
<= 1 MB. Cost: well under 1 s in stdlib Python.

## 5. Independence and controls (for a future GO)
- Producer and checker are different programs by different authors. The checker is written from this specification
  alone, without reading the producer, route 1, route 2 or the parent's control.
- Negative controls for the checker, frozen before any run: flip one basis entry (check 2 must fail); permute two
  pivots in the rank witness (check 4 must fail); swap z+ with a non-rainbow z (check 5 or 6 must fail); delete one
  failure entry (check 6 must fail); a wrong anchor hash (check 1 must fail). Each must fail for the intended reason.
- Positive control: the same certificate format for Sage DM21 (n = 21, q = 7; 5 x 20 = 100 gauged unknowns;
  dimension 7 by S4/L1; 2 rainbow points expected). The expected values come from the frozen route-2 L1 record, not
  from the producer.
- A Lean version would encode checks 1-6 as decidable finite computations. It is not planned; whether kernel
  evaluation (decide) is feasible at this size was not assessed.

## 6. Scope
The certificate would establish only the finite statement in section 1 for the exact anchor. It would not change the
status of the free one-row extension or of the beta route (both UNKNOWN), and it says nothing about other DMs,
CFR(6,39) or six MOLS(39).
