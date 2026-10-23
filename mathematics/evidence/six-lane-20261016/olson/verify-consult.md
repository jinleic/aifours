# Lane verification of the Codex consult (review/codex-consult-residual)

Lane MathOlson.  Started after host clock 2026-10-16T21:54:28-07:00.  The consult
(gpt-6.1-sol max; same-vendor relative to the current parent) is UNVERIFIED until
the hostile review recorded at the end.  Definitions are the lane's (proof-T0.md):

* Opt(B) for a block B (consecutive positions): points (val T, |T|/2 mod p) of the
  nonempty selections T in B with an even number of reflections and |T| even.
* depth(B) = max d such that theta = [0] + sum_{s in Opt(B)} c_s [s] lies in J^d
  (equivalently, by duality: every polynomial of total degree < d vanishing on
  Opt(B) vanishes at the origin; a nonempty selection with point 0 gives depth oo).
* A *tiling* partitions the cyclic word into arcs (top-level blocks; any internal
  structure); it proves an identity 2p-subword when sum depth >= 2p-1 (Lemma G).

## 1. The obstruction family (all primes p >= 5) -- lane rederivation

w_p = sigma_0^{p-2} rho_1^{p-2} sigma_1^{p-2} rho_1^{p-2} sigma_2^4 rho_1^3,
length 4p-1, F = 2p, R = 2p-1.

**1a. w_p lies in Res** (residual-class.md).  Gap brackets
beta_t = y_{t-1} - y_t - (sum of gap): rotation gaps (p-2, beta 1), (p-2, beta 1),
(3, beta -1); every empty gap has beta 0.
* E fails: R = 2p-1 < 3p-1.
* P fails: F + sum floor(a_i/2) = 2p + (p-3) + 1 = 3p-2.
* Davenport-alpha fails: nonempty gaps have weight 1 - n_t < 0, so the best I uses
  empty gaps only, at most (p-3)/2 + (p-3)/2 + 2 = p-1 of them; R + p-1 = 3p-2.
* Doubling fails: all rotations equal 1, so sum K = |K|.  j = 0 needs p rotations
  in one gap (max p-2).  Two nonempty M-gaps already hold >= p+1 rotations > p.
  One M-gap of length p-2: |K| = 2-2j forces j = 1, K empty, value beta = 1 != 0.
  M-gap of length 3 only: |K| = p-2j-3 is even in [0, p-5], value -1+|K| != 0.
  Only empty M-gaps: value |K| = p-2j in (0, p), nonzero.
* Lemma A fails for every Phi: rotations of one run share a signed value, so the
  multiplicity a of +1 is a subset sum of {p-2, p-2, 3} and b = 2p-1-a; always
  min(a,b) <= p-2, and min(k,a)+min(k,b)-k+1 <= min(a,b)+1 <= p-1 < p.
* Not rigid (three reflection values).  R' fails: a template keeping rotation
  value 1 keeps one reflection value, which occurs at most max(p-2, 4) <= p-1
  times (sigma_2 has 4 copies, more than p-2 at p = 5), so >= p+1 > p-3
  deletions; dropping the rotation value deletes 2p-1 letters.  [review fix]
* T0 fails: reflection runs p-2, p-2 (odd), 4 (even): o_F = 2.

**1b. Direct solution.**  All p-2 letters sigma_0, the first sigma_1, the second
rotation run (p-2 letters) and the final rho_1^3, in increasing order:
sigma_0^{p-2} sigma_1 rho_1^{p+1} = sigma_0 sigma_1 rho_{p+1} = rho_{-1} rho_{p+1}
= rho_p = 1, size (p-2)+1+(p-2)+3 = 2p.

**1c. Theorem (obstruction).**  For p >= 5, no tiling of w_p whose top-level blocks
all have length < p reaches total depth 2p-1.
Proof.  (i) For a block of length L < 2p every nonempty option has height
h in {1, ..., floor(L/2)} (distinct nonzero residues), so
g = prod_{j=1}^{floor(L/2)} (h-j) separates the origin: depth <= floor(L/2).
(ii) If L is even and the block has an odd number of reflections, the whole block
is not admissible, heights are <= L/2 - 1, and depth <= L/2 - 1.
(iii) With q odd-length blocks (q >= 1 odd, total length odd),
sum depth <= (4p-1-q)/2, so 2p-1 forces q = 1 and every block at its bound;
by (ii) every even block has an even number of reflections, and since w_p has 2p
reflections so does the odd block.
(iv) The run M = sigma_1^{p-2} is flanked by rotation runs of length p-2.  A block
(cyclic arc) containing a letter of M and a reflection outside M contains a whole
flanking rotation run plus a reflection at each end: length >= p.  So every block
of length < p meeting M has all its reflections in M, an even number each; summing,
|M| = p-2 would be even.  Contradiction.  []
Consequence: no catalogue of TOP-LEVEL blocks of length bounded independently of
p gives full tilings for all of Res.  Tilings that nest bounded units inside long
top-level blocks (e.g. rotation nests spanning p or more letters) are NOT covered
by this theorem.  This does NOT contradict the target theorem (1b).  [review fix]

## 2. Load-bearing lemmas of the consult (status in this lane)

* Constant-rotation bracket sigma_a rho_x^n sigma_b, m = floor(n/2) <= p-1:
  full (depth m+1) iff x = 0 or C = a-b is not in {(4j-2)x : 1 <= j <= m}.
  Lane check of the consult's derivation (Sec. 3): the bracketed options lie on
  the line L: v + 2xh - (C+2x) = 0 (m+1 points) so L | g; then q = g/L vanishes on
  the line v = 2xh at the m heights except j = (C+2x)/(4x); the separator
  L * prod_{k != j}(h-k) has g(0,0) = -(C+2x) prod(-k) != 0 when j in [1,m].
  Derivation accepted by the lane.  Edge case m = p-1 (review fix): the
  consult's proof covers it unchanged; the second-family heights 1..p are distinct
  residues including 0, the separator vanishes at (C+2x, 0) because that point
  lies on L; for x != 0 the bracket is then non-full iff C != -2x, and C = -2x
  gives a direct identity 2p-subword.  Relevance: by residual-class.md (c6) a
  constant rotation run in a word of Res has <= p-1 letters, so m <= (p-1)/2.
* Four-letter criteria (frrf: C = S != 0; rfrf: C = S and z != 0; frfr: C = S and
  x != 0; rrrr, ffff, rrff, ffrr, rffr always full): agrees with the lane's own
  earlier derivation (two height-1 points C, S and the height-2 whole selection).
  Computation: classification exhaustive (up to translation/scaling) at p = 5, 7,
  11; the "always full" shapes exhaustive at p <= 7 and 3000 random samples at
  p = 11.  [review fix]
* Insertion lemma (theta -> theta(1 - [(0,1)]) when g g^{-1} is inserted) and the
  gluing lemma (T0 tiling around certified full blocks): short proofs, accepted.
* Four arbitrary rotations (Sec. 4), six-letter universal shapes (Sec. 5), the
  uniform eight-letter degeneracy (Sec. 7, cubic certificate): exact small-prime
  computations below; the all-p case analyses are the consult's and are part of
  the hostile review.
## 3. Exact computations (code/verify_consult.py; evidence/consult_verification.json,
## evidence/consult_verification.p13.json; finished by host 21:59:31 PDT)

Block depths are computed exactly from the full option set (all 2^L selections)
with the duality rank test (code/tiling.depth_at_least); the tiling maximum is
over every cyclic cut and every partition into arcs of length <= Lb.

| p | in Res (all tools false; Lemma A max bound) | direct solution (size, product, DP) | max depth, blocks < p | target 2p-1 | blocks <= p | counter: first rotation run p-3 | counter: middle run even |
|---|---|---|---|---|---|---|---|
| 5 | yes (4 < 5) | 10, identity, yes | 7 | 9 | 8 (9 once blocks <= 6) | 8 | 7 |
| 7 | yes (6 < 7) | 14, identity, yes | 12 | 13 | 12 (12 with blocks <= 9) | 11 | 12 |
| 11 | yes (10 < 11) | 22, identity, yes | 20 | 21 | 20 | 21 | 21 |
| 13 | yes (12 < 13) | 26, identity, yes | 24 | 25 | 25 | 25 | 25 |

Reading: the obstruction (blocks < p never reach 2p-1) holds at p = 5, 7, 11, 13.
Intended-reason counter-controls: at p = 11, 13 breaking either ingredient of the
proof (isolation of the odd middle run by rotation runs of length p-2, or its odd
length) restores a short-block full tiling; at p = 5, 7 the variants are still
obstructed (blocks < p are too short there), so those two rows are not evidence
for the intended reason.  Positive controls: p = 13 (= 1 mod 4) reaches 25 with
blocks <= p, matching the consult's length-p odd bracket; p = 5 reaches 9 once
blocks <= 6 are allowed; p = 7 (= 3 mod 4) stays at 12 even with blocks <= 9,
consistent with the consult's resonance claim for p = 3 mod 4.

Lemma checks (0 mismatches everywhere): four-letter criteria, all values up to
translation/scaling, p = 5, 7, 11; constant brackets n <= min(2p-2, 12), x in
{0,1}, all C: 80/168/264 cases at p = 5/7/11; four arbitrary rotations: 350/1470/
1640 cases at p = 5/7/11 (p = 11 a 15% sample); six-letter FRRFFF, FFFRRF, FRFFRF:
exhaustive at p = 5 (15625 each), 4000 random at p = 7, 11, none non-full;
sigma_0 rho_1^4 sigma_{-6}^3 has depth 3 (< 4) at p = 3, 5, 7, 11, 13; insertion
lemma: 0 violations in 300 random insertions at each of p = 5, 7, 11.


Provenance (review fix): the p = 13 row, the positive controls (p = 5 blocks <= 6,
7, 8 -> 9; p = 7 blocks <= 9 -> 12) and the eight-letter depths (3 at p = 3, 5, 7,
11, 13) are regenerated by code/verify_consult_extra.py into
evidence/consult_verification.extra.json (sha256 0804006e...1f74; driver sha256
62eb8cbd...3683; verify_consult.py b8d45e4b...118c; tiling.py fb3621c9...a285;
coverage_all.py f52a419b...6e39; run finished by host
2026-10-16T22:18:43-07:00).

Parity-preserving isolation control (reviewer's suggestion; only isolation is
broken, F = 2p kept): sigma_0^{p-2} rho_1^{p-3} sigma_1^{p-2} rho_1^{p-2} sigma_2^4
rho_1^4, blocks < p: p = 13 reaches 25 = 2p-1 (obstruction disappears);
p = 7 -> 12 < 13 and p = 11 -> 20 < 21 remain obstructed, as predicted by the
constant-bracket criterion: the shortened-side bracket sigma_0 rho_1^{p-3} sigma_1
(C = -1, m = (p-3)/2) is non-full iff -1 = 4j-2 for some j <= m, i.e. j = (p+1)/4
for p = 3 mod 4 (p = 7: j = 2 <= 2; p = 11: j = 3 <= 4), and full at p = 13.
The earlier short_first_rot variant changed F to 2p+1, so it tested isolation and
parity together, not isolation alone.  [review fix]

## 4. Representation change (review accepted Section 1: obstruction correct)

Stop extending a bounded catalogue of short units.  Two explicit routes remain:
(a) units growing with p: whole-run brackets sigma_a^{2u+1} rho_x^n sigma_b^{2v+1}
    (consult Sec. 7 two-grid interpolation problem; A = 0 solved by Sec. 3) and
    nests around them, with an exact fullness criterion as a function of
    (n, u, v, C, x) and the run multiset;
(b) a separate structural argument for words whose reflection runs are all
    constant (GR words), e.g. the Theorem R integer/IVT argument with per-run
    shifts eta_i = (y_i - y_{i-1})/2.

## 5. Hostile review (cross-vendor relative to the current OpenAI parent)

Claude claude-opus-5-5, effort max, read-only (Read/Glob/Grep on ./input only);
review/claude-consult-verify/receipt.json, 2026-10-17T05:00:03Z-05:18:08Z.
Verdicts: obstruction (Sec. 1c + consult Sec. 9) CORRECT; membership of w_p in Res
CORRECT WITH MINOR FIXES (R' count, applied); constant-rotation bracket criterion
CORRECT (edge case m = p-1 recorded, applied); four-letter criteria CORRECT;
insertion and gluing lemmas CORRECT.  Required wording/provenance fixes (R' count,
edge case, counter-control interpretation, provenance driver, four-letter sampling
scope, restricting the consequence to bounded TOP-LEVEL blocks) are applied above.
Not reviewed here: the consult's all-p case analyses for four arbitrary rotations
(Sec. 4), the six-letter shapes (Sec. 5) and the cubic certificate (Sec. 7); these
stay consult claims with exact small-prime confirmation only.
