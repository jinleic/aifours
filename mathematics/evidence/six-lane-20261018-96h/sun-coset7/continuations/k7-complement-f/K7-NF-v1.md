# K7-NF-v1: class K7 outside F has no configuration — exact marker-placement partition matched to accepted literal scopes [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T16:10:40-0700, immediately before this exclusive write.
- **Author:** SunM13MixedFibres; single author; written mathematics only. No scientific computation, enumeration,
  solver, test, Lean, model call or nested agent. **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Frozen scope:** `K7-NF-SCOPE-v1.md` (this directory), sha256 2469a967b81d15ade6a11a981678c831b12b60d4e12404733fef8f7d943b351c,
  frozen before any derivation in this directory (its section 3 discloses the pre-freeze case sketch). **Outcome against
  it: the primary target Theorem K7-NF is proved in writing (section 3); the fallback is not used.**
- **Nature of the result.** Theorem K7-NF is an ASSEMBLY: an exact elementary partition of K7 \ F (section 2) whose
  eight blocks are each matched, hypothesis by hypothesis, to the LITERAL statement of an accepted theorem (section 1).
  No accepted subfamily is re-proved, and none of them is claimed here as new mathematics. The only new items are the
  elementary Lemmas SHAPE, MK and PART, the literal matching, and the separately named navigation Corollary K7-REM.
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`; S := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`;
  O16 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`; R16 := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.

## 0. Setting and definitions
A **configuration** is a group G with finite-index subgroups U_1, ..., U_7 and elements g_1, ..., g_7 such that the left
cosets g_iU_i are pairwise disjoint; n_i := [G : U_i]. Following O16/README.md (lines 33-35), write
n_i = 2^(e_i) 3^(f_i) 5^(h_i) w_i with gcd(w_i, 30) = 1 (the README writes g_i for the 5-exponent; the accepted written
verdict's overlay A-1 renames it h_i). **Class K7** is the README class of line 91: "a <= 1, C = V, all 21 pairs gcd 6".

**Lemma SHAPE.** Seven positive integers n_1, ..., n_7 have all 21 pairwise gcds equal to 6 if and only if
n_i = 6 r_i with r_1, ..., r_7 pairwise coprime. (Then a <= 1 and C = V hold automatically.)
*Proof.* If every pairwise gcd is 6, then 6 | n_i for each i; writing n_i = 6 r_i, gcd(n_i, n_j) = 6 gcd(r_i, r_j) = 6
forces gcd(r_i, r_j) = 1. Conversely gcd(6 r_i, 6 r_j) = 6 gcd(r_i, r_j) = 6. If all n_i are divisible by 6, then
C = A_2 cap A_3 = V; and 5 divides at most one r_i, hence at most one n_i, so a = |A_5| <= 1. QED

Write r_i = m_i w_i with m_i the {2,3,5}-part of r_i ("marker product"; S/K7-LFC-INV-v1.md lines 10-11) and
gcd(w_i, 30) = 1. Vertex i is **unmarked** iff m_i = 1, i.e. n_i = 6 w_i; M := {i : m_i != 1} is the marked set.
Since n_i = 6 r_i: e_i = 1 + v2(r_i), f_i = 1 + v3(r_i), h_i = v5(r_i). Hence vertex i is a
- **2-marker** iff 2 | m_i iff e_i >= 2; **3-marker** iff 3 | m_i iff f_i >= 2; **5-marker** iff 5 | m_i iff h_i >= 1.
Put Z := {i : 2 | m_i}, T := {i : 3 | m_i}, P := {i : 5 | m_i}. For i in M, m_i = 2^(v2 r_i) 3^(v3 r_i) 5^(v5 r_i); the
exponents of the present primes are actual and unbounded (no capping anywhere in this file).

**Lemma MK (each marker is unique).** In class K7, |Z|, |T|, |P| <= 1, M = Z cup T cup P, and every vertex outside M is
unmarked. *Proof.* If a prime q in {2, 3, 5} divided r_i and r_j with i != j, it would divide gcd(r_i, r_j) = 1 (Lemma
SHAPE). M = Z cup T cup P because m_i is the {2,3,5}-part of r_i. (This re-derives, in K7, README P1 (ii)-(iii), lines 48-49.) QED

**F** := the K7 configurations with |Z| = |T| = 1 and Z != T (a 2-marker z and a 3-marker t, z != t), as in the parent
transition `RUN/control/six-slot-written-resumption-20261019-1603-v1.json` (ac09b465…f0f8). By Lemma MK, a K7
configuration lies OUTSIDE F iff Z is empty, or T is empty, or Z = T is a singleton.

## 1. Interface table: accepted statements used, read literally with their mandatory overlays
Line numbers refer to the exact files and sha256 values listed; every pinned file was hashed by me against its verdict pin.
| tag | literal statement used (file:lines) | mandatory overlays (statement effect) | accepting verdict (sha256; lines) | exact scope in section-0 notation |
|---|---|---|---|---|
| R0, CE, P0, P1, class K7 | O16/README.md (2a6d6d6e…3fd1) lines 27-29 (R0), 33-35 (CE), 37-50 (P0, P1), 91 (K7 row) | written-verdict overlay A-1 (5-exponent named h_i; that verdict's line 46) | R16/sun-coset7-written-parent-verdict-v1.md (73a25ba6…9f35) lines 16-23, 46 | definitions only |
| **K7-M0** | S/K7-LFC-INV-v1.md (45be9162…726c) lines 113-114: "There is no finite group G with seven pairwise disjoint left cosets g_iU_i whose indices are n_i = 6 w_i with w_i pairwise coprime and coprime to 30. (By R0 the same holds for arbitrary G with finite-index U_i.)" | S/K7-LFC-INV-erratum-v1.md (7af9acf0…75bd5): no statement change (lines 10, 82-85) | RUN/review/sun7-lfc-inv-parent-verdict-v1.md (8621e744…cca18) line 21 (item 4), line 23 (item 6, arbitrary groups) | M empty |
| **K7-M1** | S/K7-M1-v1.md (6e9b2d09…5d63) lines 56-57: "There is no K7 configuration (in any group with finite-index subgroups, by R0) with exactly one marked vertex z whose markers lie in {3, 5} (e_z = 1)." | S/K7-M1-erratum-v1.md (4094b537…c510) F2, lines 19-22: m_z = 3^A 5^B, A, B >= 0, A + B > 0, actual unbounded exponents; no statement change (line 8) | RUN/review/sun7-M1-parent-verdict-v1.md (7121ceed…ed84) line 5 | M = {x}, 2 does not divide m_x |
| **K7-Z2** | S/K7-Z2-v1.md (cda7573d…cbe7) lines 20-24: "Hypothesis H: some vertex z has e_z >= 2 (so m_z = 2^eps 5^(h_z), eps = e_z - 1 >= 1, h_z >= 0) and **no vertex has f >= 2**. [...] **Theorem K7-Z2 [NEW].** No K7 configuration satisfies H. (By R0, in any group with finite-index subgroups.)" | S/K7-Z2-erratum-v1.md (3aa30555…e456f9): statements and scope unchanged (line 8); G1 makes its ROW-1 import accepted (lines 12-16) | RUN/review/sun7-Z2-parent-verdict-v1.md (0f6b9aa3…19c) line 5 ("A 5-marker may occur at the centre or elsewhere") | Z = {z}, T empty, P arbitrary |
| **K7-35** | S/K7-35-v1.md (5624d978…fc5a) lines 13-18: "Hypothesis H35: no vertex has e >= 2; one vertex t has f_t >= 2 (m_t = 3^A, A >= 1) and a different vertex p has h_p >= 1 (m_p = 5^B, B >= 1); W := V \ {t, p} (five unmarked vertices). [...] **Theorem K7-35 [NEW].** No K7 configuration satisfies H35 (any group, by R0)." | S/K7-35-erratum-v1.md (b13e1cf2…6e32) K1 and S/K7-35-erratum-v2.md (93f99707…0d44) K2-K4: proof repairs, "Theorem K7-35 is unchanged" (v2 line 25) | RUN/review/sun7-K63DE-K735-parent-verdict-v1.md (1a1c6390…3919) lines 11, 13 | Z empty, T = {t}, P = {p}, p != t |
| **K7-U1** | S/continuations/k7-k62-residue/K7-U1-v1.md (d4e6cdc9…1965) lines 30-32 (hypothesis U1: "exactly one vertex z is marked, with m_z = 2^E 3^A 5^B, E, A, B >= 0 not all 0 (actual, unbounded exponents)") and line 158: "No K7 configuration (in any group with finite-index subgroups, by R0) has exactly one marked vertex." | K7-U1-erratum-v1.md (a795c5b7…99d5) E-1 lines 14-16 (|M| = 1 mandatory; a separate 5-marked vertex is outside), lines 103-104 (theorem unchanged) | RUN/review/sun7-U1-parent-verdict-v1.md (44dfbe85…5c86) lines 5-8 | M = {x}, any m_x != 1 |
| **Z23-P5** | S/continuations/k7-k62-residue/K7-Z23-P5-v1.md (63255032…8e04) lines 10-20: indices n_z = 6*2^E*3^A*w_z, n_p = 6*5^B*w_p, n_u = 6*w_u (u in W, |W| = 5), E, A, B >= 1, w_i pairwise coprime and coprime to 30; "**Theorem Z23-P5.** No finite group with seven pairwise disjoint left cosets of subgroups has these indices. By R0 (the common finite-core quotient), the same holds in arbitrary groups with finite-index subgroups." | K7-Z23-P5-erratum-v1.md (737e82a3…823d) lines 8-9: exact statement and scope unchanged | RUN/review/sun7-Z23P5-parent-verdict-v1.md (7179e564…6f8d) line 5 | Z = T = {z}, P = {p}, p != z |
| (a1) closure — Corollary K7-REM only | — | the R2 verdict's mandatory overlays (its lines 19-31) | RUN/review/sun7-K7-R2-parent-verdict-v1.md (9b0f7df5…926d) lines 5, 9 | (a1) as defined at its line 9 |
Not used anywhere: the A2X units of `S/continuations/k7-a2-closure` (candidates), K62-FULL (accepted only for class K6.2*,
irrelevant to K7), M13X, MK, R2MIX, M3R, TX/ZA/ZB, the conditional K7 family closure map, D23/RICH/A1/TC/CELL statements,
FH, Sun(7), and every pending candidate. No accepted theorem's proof is repeated.

## 2. Lemma PART (exact partition of K7 \ F)
Every K7 configuration outside F lies in exactly one of the following eight blocks (z, t, p denote the elements of
Z, T, P when nonempty; E, A, B >= 1 are the actual exponents v2 r_z, v3 r_t (or v3 r_z), v5 r_p (or v5 of the 5-marked
vertex), unbounded):
| block | Z, T, P | marked set and marker products |
|---|---|---|
| B1 | Z = T = P = empty | M empty |
| B2 | Z = T = empty, P = {p} | M = {p}, m_p = 5^B |
| B3 | Z = empty, T = {t}, P = empty | M = {t}, m_t = 3^A |
| B4 | Z = empty, T = P = {t} | M = {t}, m_t = 3^A 5^B |
| B5 | Z = empty, T = {t}, P = {p}, p != t | M = {t, p}, m_t = 3^A, m_p = 5^B |
| B6 | Z = {z}, T = empty, P in {empty, {z}, {p} with p != z} | M = {z}, m_z = 2^E 5^(B') with B' >= 0; or M = {z, p}, m_z = 2^E, m_p = 5^B |
| B7 | Z = T = {z}, P contained in {z} | M = {z}, m_z = 2^E 3^A 5^(B') with B' >= 0 |
| B8 | Z = T = {z}, P = {p}, p != z | M = {z, p}, m_z = 2^E 3^A, m_p = 5^B |
*Proof.* By Lemma MK, each of Z, T, P has at most one element, so for a configuration outside F exactly one of the four
mutually exclusive cases holds: (Z, T) = (empty, empty), (empty, {t}), ({z}, empty), or Z = T = {z}. [The fifth possibility,
Z = {z}, T = {t}, z != t, is F.] Within each case P is empty or a singleton, and a singleton P either coincides with an
already marked vertex or not; these sub-cases are listed, are mutually exclusive and exhaust the possibilities:
(empty, empty): P empty (B1) or P = {p} (B2). (empty, {t}): P empty (B3), P = {t} (B4), P = {p}, p != t (B5).
({z}, empty): all three P-possibilities (B6). Z = T = {z}: P empty or P = {z} (B7), P = {p}, p != z (B8).
In each block M = Z cup T cup P (Lemma MK); a marked vertex's marker product is the product of the prime powers of the
primes placed on it (by the definitions of Z, T, P), and every other vertex is unmarked. This gives the displayed products.
QED

## 3. Theorem K7-NF
**Theorem K7-NF [CANDIDATE_UNVERIFIED; assembly of accepted theorems].** No group with finite-index subgroups contains a
configuration of class K7 outside F. Equivalently: every K7 configuration, in any group, has a 2-marker z and a 3-marker t
with z != t. This holds for every admissible 5-marker placement and all exponents and w-cofactors.

*Proof.* Let a K7 configuration outside F be given (any group). By Lemma PART it lies in exactly one block; in each block
the literal hypothesis of the cited accepted theorem holds, so that theorem (stated for arbitrary groups with
finite-index subgroups) gives a contradiction.
- **B1 -> K7-M0.** All m_i = 1, so n_i = 6 w_i with the w_i = r_i pairwise coprime (Lemma SHAPE) and coprime to 30: the
  literal index hypothesis of K7-M0 (LFC-INV lines 113-114).
- **B2 -> K7-M1.** Exactly one marked vertex p; its markers lie in {3, 5} (m_p = 5^B) and e_p = 1 (2 does not divide
  r_p): K7-M1 with A = 0, B >= 1, which the overlay F2 (lines 19-22) explicitly allows.
- **B3 -> K7-M1** with A >= 1, B = 0 (M = {t}, e_t = 1).
- **B4 -> K7-M1** with A, B >= 1 (M = {t}, e_t = 1).
- **B5 -> K7-35.** No vertex has e >= 2 (Z empty); t has f_t = 1 + A >= 2 and m_t = 3^A (2 and 5 do not divide r_t, since
  Z is empty and P = {p} with p != t); the different vertex p has h_p = B >= 1 and m_p = 5^B (Z empty, T = {t}); the five
  vertices of W = V \ {t, p} are unmarked (Lemma MK). This is H35 verbatim (K7-35 lines 13-14).
- **B6 -> K7-Z2.** z has e_z = 1 + E >= 2 and no vertex has f >= 2 (T empty): hypothesis H verbatim (Z2 lines 20-21).
  H restricts neither P nor h_z: its own consequence clause (lines 21-22) lists m_z = 2^eps 5^(h_z) with h_z >= 0 and at
  most one further marked vertex p != z with m_p = 5^(h_p); the accepting verdict (line 5) states "A 5-marker may occur
  at the centre or elsewhere". So all three P-placements of B6 are covered.
- **B7 -> K7-U1.** Exactly one marked vertex z with m_z = 2^E 3^A 5^(B'), E, A >= 1, B' >= 0: inside hypothesis U1
  (E, A, B >= 0 not all 0; U1 lines 30-32), with |M| = 1 as the erratum E-1 requires.
- **B8 -> Z23-P5.** n_z = 6 * 2^E * 3^A * w_z (5 does not divide r_z, since P = {p} with p != z), n_p = 6 * 5^B * w_p
  (2 and 3 do not divide r_p, since Z = T = {z}), and the five other indices are 6 w_u (Lemma MK); E, A, B >= 1; the w's
  are pairwise coprime and coprime to 30. This is the literal index tuple of Z23-P5 (lines 10-15).
Every block leads to a contradiction, so K7 \ F has no configuration. Each cited statement is already for arbitrary
groups (each via the accepted R0 / finite-core quotient, which preserves indices: README lines 27-29; LFC/INV verdict
line 23), and membership in a block depends only on the labelled index tuple; no separate lift is needed. QED

*Remarks (no further premise).* (1) U1 alone also covers B2-B4 (|M| = 1); M1 is cited there because it is the earlier
accepted statement with exactly that scope. (2) No block needs two accepted theorems, and no accepted theorem is applied
outside its literal hypothesis: K7-35 is NOT used for B4 (3 and 5 on ONE vertex), U1 is NOT used for B8 (|M| = 2), Z2 is
NOT used for B7 or B8 (they have a 3-marker), M1 is NOT used for B6 or B7 (they have a 2-marker). (3) The theorem is
consistent with the frontier sentences of the accepted U1 and Z23-P5 verdicts (U1 verdict lines 24-28; Z23-P5 verdict
line 13), which state the same conclusion informally; those sentences are not used as premises.

## 4. Corollary K7-REM (navigation; accepted results only)
Define, inside F (z the 2-marker, t the 3-marker, z != t):
- **(a1)** (as defined in the accepted R2 verdict, line 9): r_z = 2^E 5^(Bz) w_z, r_t = 3^A 5^(Bt) w_t, E, A >= 1,
  Bz, Bt >= 0, Bz Bt = 0, and the five other vertices unmarked (5-marker absent, on z or on t);
- **(a2)**: a third vertex p not in {z, t} has r_p = 5^B w_p, B >= 1, with r_z = 2^E w_z, r_t = 3^A w_t and the four other
  vertices unmarked (the (a2) setting of `RUN/control/mathematics-slot-transition-sun-20261019-1325-v1.json`, 4b617b81…2697).
**Lemma.** F = (a1) disjoint-union (a2). *Proof.* In F, P is empty, {z}, {t}, or {p} with p not in {z, t} (Lemma MK). The
first three give exactly the (a1) shape (Bz Bt = 0 because |P| <= 1; the other five vertices are unmarked by Lemma MK);
the last gives exactly the (a2) shape. They are disjoint (|M| = 2 versus |M| = 3). QED
**Corollary K7-REM.** By Theorem K7-NF and the accepted (a1) closure (R2 verdict line 5: "(a1) contains no actual
disjoint-coset configuration, in any group"), every K7 configuration in any group lies in (a2). Equivalently, class K7
minus (a2) has no configuration, by accepted results plus Theorem K7-NF.
**Boundary.** (a2) remains OPEN: the A2X units are candidates under review and are NOT used. K7-REM is not an exclusion of
K7 or of Sun(7).

## 5. Scope, provenance and verification boundary
- **Claimed (CANDIDATE_UNVERIFIED, written, single author):** Lemmas SHAPE, MK, PART (elementary), Theorem K7-NF
  (assembly) and Corollary K7-REM (navigation). The accepted theorems K7-M0, K7-M1, K7-Z2, K7-35, K7-U1, Z23-P5 and the
  (a1) closure are cited at their literal scopes, not re-proved, and not counted as new progress.
- **Sun provenance.** No Sun instance is used in this file. Through the cited accepted theorems the transitive closure
  includes Sun(2)-Sun(4) and the locally accepted, computer-assisted Sun(5) (R16/sun-coset5-parent-verdict-v1.md,
  2cf02436…5301) and Sun(6) (R16/sun-coset6-parent-gate-verdict-v1.md, efe1d849…1e29). No Sun(7).
- **Not claimed:** exclusion of (a2), of class K7, of any other README class, or Sun(7); novelty, priority, significance,
  Lean or human review. No computation of any kind was run.
- **Requested checks:** (1) Lemma PART: exhaustiveness and disjointness of the eight blocks, in particular the three
  P-placements of B6 and the two of B7/B8; (2) each block against the quoted literal hypothesis, including the actual-
  exponent overlays (M1 F2; U1 E-1) and that Z2's hypothesis allows h_z >= 1 and a separate p; (3) that K7-35's
  "m_t = 3^A" holds in B5 (5 does not divide r_t because P = {p} with p != t); (4) that each cited statement is for
  arbitrary groups; (5) the (a1)/(a2) split of F in Corollary K7-REM against the R2 verdict's line 9 definition.
- **Omission controls (thought experiments).** Dropping B4 would leave "3 and 5 on one vertex, no 2" uncovered (K7-35
  needs distinct vertices); dropping the P = {z} option of B6 would leave "2 and 5 on z, no 3"; dropping B8 would leave
  the shared 2/3 vertex with a separate 5 (U1 needs |M| = 1). Each is covered by the cited block.
