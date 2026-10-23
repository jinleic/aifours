# Desk hand check of the second-family foundations (written before the Claude note was read)

Author: OlsonFoundationDesk (Claude-family sub-agent, anthropic/claude-opus-5-5).  Written while the commissioned audit was running,
host clock after 2026-10-18T01:43 PDT, from the byte-identical snapshot (snapshot-manifest.json).  This is a desk derivation, NOT
an acceptance and NOT independent of the commissioned reviewer's vendor (same model family).  File:L = 1-based index in
text.split('\n') of the snapshot copy.

## 1. GR -> WAS -> HW (both directions)

* GR product formula (olson/proof-GR.md L38-49).  Cut the cyclic word before R_1 (allowed: UV = 1 iff VU = U^{-1}(UV)U = 1,
  proof-theoremP.md L14-15).  For a selection with C reflections, put z_i = (-1)^{#selected reflections in S_1..S_(i-1)}; every
  rotation of R_i gets sign z_i; the j-th selected letter of S_i gets z_i(-1)^(j-1), so S_i contributes z_i y_i [c_i odd].
  z_(i+1) = z_i(-1)^(c_i); for i = k this closes the cycle exactly when C is even, which an identity product forces (sign
  component (-1)^C).  So c_i = f_i (mod 2), V = sum z_i n_i + sum_(f_i = 1) z_i y_i, and (z_i - z_(i+1))/2 = z_i [f_i = 1] gives
  sum_(f_i=1) z_i y_i = 2^(-1) sum_i z_i (y_i - y_(i-1)), y_0 := y_k.  Hence V = t - tau(z), t = A+ - A-.
* Realisable C (L51-53): each c_i ranges over {f_i, f_i + 2, ..., l_i - [l_i != f_i mod 2]}; the sumset is every even number in
  [Phi, C_max], C_max = F - delta, and F = Phi + delta (mod 2) makes C_max even.
* Elimination (L54-57): with A+- = (2p - C +- t)/2 the constraints are 0 <= A+ <= E+, 0 <= A- <= E-, Phi <= C <= C_max.  All six
  bounds on C are even (t is even because A+ + A- = 2p - C is even).  Pairwise: Phi <= 2p - |t| iff |t| <= s1; 2p + t - 2E+ <= C_max
  iff t <= 2E+ - s0; 2p - t - 2E- <= C_max iff t >= s0 - 2E-; 2p + t - 2E+ <= 2p - |t| iff t <= E+ (t >= 0; automatic for t < 0);
  2p - t - 2E- <= 2p - |t| iff t >= -E- (t <= 0; automatic otherwise); Phi <= C_max always.  So the realisable t are exactly Ach(z).
* Directions.  Completeness (every identity 2p-subword gives z, an admissible (c, rotations) and t in Ach(z) with t = tau(z) mod p)
  is the reading above; realisability (every admissible data point is a selection of size C + A+ + A- = 2p with product rho_(t-tau))
  uses the global sign z -> -z (Ach -> -Ach, tau -> -tau) when z_1 = -1.  GR is an iff for every length N = F + R with F, R >= 1.
* WAS (repr-WAS.md L16-22): sum_i z_i theta_i = 2 sum_P theta because sum theta = 0, so tau(z_P) = sum_(i in P) theta_i.
* HW (README L29-36): per run, f = 0 contributes 2 floor(l/2) and f = 1 contributes l - [l even] = 1 + 2 floor((l - 1)/2); so
  C_max = 2m + 2h, h = H - #{f_j = 1, l_j even}.  s1 = 2p - 2m and s0 = 2p - 2m - 2h are even, so floor(U/2) =
  min(p - m, E+ + m + h - p, floor(E+/2)) = g_P(E+) and ceil(L/2) = -g_P(E-) for E+- of either parity; 2 is a unit mod p.
  P = empty / [k] (m = 0, h = H) are included; I(P^c) = -I(P).  k = 1: f_1 = 0, tau = 0.
* Which direction is used where: "one window hit => solvable" (direct certificates) = GR realisability; "avoider => every window
  avoided" = contrapositive of the same; the transfers OR and M0 additionally need "every window avoided => avoider" = GR
  completeness, applied to the reduced word.  Both directions are proved.

## 2. Lemma H (proof-PAR-K0.md L18-44)

For proper Q: m >= 1, Phi = 2m, delta = beta + o_F - (2m - beta), C_max = 2H + 2m - 2beta, h = H - beta = p - 1 - kappa - beta,
E+(Q) = D_Q + B, E-(Q) = E+(Q^c).  Then E+ + m + h - p = D_Q + B - kappa + m - beta - 1, so g_Q(E+) = lambda(Q) - 1 and
-g_Q(E-) = 1 - lambda(Q^c): I(Q) = [1 - lambda(Q^c), lambda(Q) - 1].  Empty pattern: E+ = B, E- = A, h = H gives I(empty) as at
L22-23 and u = 0; P = [k] gives -I(empty).  The 07:39 correction (L23-31): upper end min(p, B - kappa - 1, floor(B/2)) <= p - 1 and
lower end >= -(p - 1) when A, B <= 2p - 1, so the only multiple of p available is 0, which lies in I(empty) iff both minima are
>= 0 iff A, B >= kappa + 1 (also correct for kappa < 0: then 0 is in I(empty) and the word has p reflection pairs).  The quoted
counterexample to the uncorrected form: p = 5, rho_1^10 sigma_0^8: A = 10, B = 0, H = 4, kappa = 0 = B, min(A, B) <= kappa holds,
yet I(empty) = [-min(5, 9, 5), min(5, -1, 0)] = [-5, -1] contains -5 = 0 mod 5 (the subword rho_1^10).  Avoiders have A, B <= 2p - 1
(rho_(+-1)^(2p) = 1); OR keeps A, B; M0 lowers both.

## 3. OR and M0 transfers

OR (proof-PAR-Kplus-partial-r2.md L24-35): a pattern of w~ is a union of segments of w; its boundary runs are odd in both words, so
beta = 0 and m, D_Q + B, kappa (hence lambda and the window) agree; u telescopes over each segment to the y-difference of the two
odd runs, which w~ keeps; the empty condition depends on A, B, kappa only.  w~ is RGR of length 4p - 2 with the same F, R >= 1.
M0 (proof-RUNS.md L402-414): for every P (including empty) E+-' = E+- - 1, h' = h + 1 (beta unchanged), so g' <= g and every window
shrinks; phi is unchanged; R' = R - 2 >= 1 (r_t >= 3), F' = F + 2.  Both transfers: w avoids => (H/HW, necessity on w) all windows
of w avoided => all windows of the reduced word avoided => (H/HW, sufficiency on the reduced word) it avoids.  The v4 wording at
L53-56 and Fact T L87-97 describes this correctly.

## 4. Upstream imports of DR-Res/DR (general words)

* EGZ (proof-dihedral-partial.md L27-28): from 3p - 1 rotations take p with zero sum (classical EGZ, 2p - 1 suffice), then p more
  from the remaining 2p - 1; rotations commute, so the 2p letters in increasing order multiply to rho_0.  Classical import.
* Gap Theorem P (proof-theoremP.md): requires F >= 1 (L17) and N <= 4p - 1 (L27); F = 1 is vacuous (1 + floor((N - 1)/2) <= 2p <
  3p - 1).  The parametrisation, injectivity (u_1 = 0), even size, sign c_t = (-1)^(u_t), V = sum_(t>=2) beta_t u_t + sum x_pi m_pi,
  Z of degree 2, deg Q <= 3(p - 1) < M = F - 1 + sum floor(n_t/2), the Boolean-box cancellation and "even, divisible by p, in
  [1, 4p - 1] => 2p" all check.
* Per-rotation marked formulation (proof-dihedral-partial.md L19-25): same computation with x_r m_r - x_r u_t per rotation gives
  V = sum_(t in Minus) beta_t + sum_(marked) x_r; the fixed gap (u = 0) must be chosen outside the Minus set (always possible below).
* Doubling (L33-59): |U| = 2j + n_M + |K| = p and value(U) = sum_M beta + sum_K x = 0; the V-family has F - 2j - 1 colours and
  R - (p - 2j) marks, M = N - p - 1 = 3p - 2 for N = 4p - 1; U's reflections sit between frozen Plus gaps, U's rotations are fixed
  unselected; the box lemma (deg <= 3p - 3 < 3p - 2) gives a nonempty V with value 0 and size in {p, 2p} (size <= 3p - 1); the
  union with U is the selection with Minus(V) u M-gaps and marks(V) u K, value 0, size 2p, even reflection count.  Implicit:
  2j + 1 <= F (distinct gaps).  j = 0: U = K, p rotations of one gap with zero sum.
* Davenport-alpha (L61-73): needs F >= 2 (stated), I pairwise non-adjacent (stated) and N <= 4p - 1 (used at L70, "below 4p", NOT
  stated in the lemma; the context L125 and DR-Res L35 supply N = 4p - 1).  With the word cut so that a gap outside I is first (one
  exists: |I| <= floor(F/2) < F), each chosen bracket f_(t-1) f_t with gap t's rotations unselected is rho_(y_(t-1) - y_t) and is
  preceded by an even number of selected reflections, so (size, value) is additive.  D(Z_(2p) + Z_p) = p + 2p - 1 = 3p - 1
  (rank-2 formula, p | 2p; classical import).  A zero-sum item subset gives size = 0 mod 2p, 1 <= size <= N < 4p, so 2p.

## 5. DR-Res and DR

(E) EGZ; (P) gap Theorem P with n_t = r_i for the gap containing R_i and 0 for interior reflection gaps; (V) Davenport-alpha with
I = every second interior gap of each S_j (floor(l_j/2) gaps, separated within a run by one gap and across runs by a rotation gap),
|I| = H, R + H items; (Pairs) p disjoint adjacent pairs sigma_y sigma_y (cut the cyclic word at a run boundary first; at most one
pair could straddle the cut and it still multiplies to 1 around an identity middle); (D0) Doubling j = 0.  An in-run deletion
lowers R or F by one and does not increase any floor(r_i/2), floor(l_j/2), a_i, b_i; it keeps all 2k runs nonempty and constant,
so w' is in RGR_(4p-2)(p) with the same k and F, R >= 1, and every 2p-subword of w' is one of w in the same index order.  Theorem DR
L32-40 then needs exactly: k <= p for one deletion (RUNS), and all runs odd for the deletions from X and Y (PAR).  Corollary D of
v4 (L202-203) supplies INV_Res for inherited avoiders with F, R >= 1, which is what DR-Res uses.  INV*(p) is used only in DR'
(proof-DR.md L47-58), whose (a), (b) are correct; nothing in the packet derives RGR membership for an arbitrary avoider.

## 6. Points the desk would raise (before reading the reviewer)

1. MINOR: Davenport-alpha (proof-dihedral-partial.md L61-70) omits the hypothesis N <= 4p - 1 used at L70; DR-Res L35 supplies it.
2. MINOR: Davenport-alpha's "any subset of items is a valid selection" (L65-66) tacitly fixes a gap outside I as the first gap.
3. NIT: DR-Res (Pairs) (proof-INV-reduction.md L24-25) tacitly cuts the cyclic word at a run boundary.
4. NIT: proof-theoremP.md L3-6 still says "NOT yet independently reviewed" although review/codex-theoremP (verdict correct, input
   sha 58a85ebe..., identical to the pinned file) exists.
5. No circularity (gap Theorem P is a standalone Chevalley-Warning argument; PAR's Theorem P is used only through INV_Res) and no
   finite premise (proof-PAR-K0.md L45-46, proof-GR.md Sec. 5, repr-WAS.md Sec. 4, proof-INV-reduction.md Sec. 3, proof-DR.md
   L60-67 and the [C] labels are aids).
