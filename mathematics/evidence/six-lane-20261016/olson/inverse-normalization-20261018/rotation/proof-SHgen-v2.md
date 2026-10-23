# Theorem SHgen: heavy rotations of any odd weight in an all-odd constant-block word of length 4p-2, v2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:12:10-07:00.  Status [W], UNREVIEWED.
Supersedes proof-SHgen-v1.md (kept unchanged).  v1 Sec. 3 case (iii) contains a FALSE side sentence ("Either form
contradicts (F2)": the cruder chain recorded there does not); the v1 theorem itself is still implied by v2.
Changes: sharper case analysis in Lemma FLEXa giving the single side condition (K); v1's hypothesis (L) is derived;
rho_0 is allowed as a heavy of weight p.  For heavies +-3c, (H) and (K) are the hypotheses of Theorem SHm
(proof-SHm-v1.md) without its eta <= p-3, so v2 subsumes SHm-v1.
Imports (accepted scopes): GRX (notes-GRX-v1.md, any cyclic constant-block representation) and Proposition K1
[R/olson-rotation-lowodd-parent-verdict-v2.md, 0853f4ac...ba29]; from the RUNS assembly v4 [R/olson-runs-parent-verdict-v1.md,
82adbddd...9237]: Corollary B'(b); the C1 lemma composition; Theorem KBH (kappaB-high/proof-KBH.md L10-14); Theorem KB
(inverse-parity/proof-PAR-Kplus-partial-r2.md L238-273), UNCAPPED implication only, no (D0); KB's capped case is shown
impossible inside Lemma Ua; Davenport-alpha (olson/proof-dihedral-partial.md Sec. 4, erratum m4 pinned at
R/olson-runs-parent-verdict-v1.md L57: N <= 4p-1, F >= 2, frame at a gap outside I) in the instance (V) below; the
trivial cut.  KB and KBH are applied only to genuine RGR words of length 4p-2.

## 0. Setting

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1).  w is a cyclic word R_1 S_1 ... R_k S_k of
length 4p-2 (p >= 5 prime) with F, R >= 1 and k >= 2 blocks S_i = sigma_(y_i)^(l_i), every l_i ODD and every run R_i
NONEMPTY.  (Lemma PM* delivers this form, with the same length and rotation multiset, from any avoider whose maximal
cyclic reflection runs are constant and k >= 2 of them odd; k = 1 is Proposition K1.)
H := sum_i (l_i - 1)/2, kappa := p - 1 - H; so F = 2H + k and R = 2p + 2kappa - k.
GRX in this form: for z in {+1,-1}^k let Phi be the number of cyclic sign changes, C_max = 2H + Phi and
T(z) = sum_(z_i = +) theta_i.  w has an identity 2p-subword iff for some z there is a sub-multiset Q of the rotations
with |Q| = m even, 2kappa + 2 - Phi <= m <= 2p - Phi, m <= R, whose effective value sum equals T(z) (a rotation of run
i has effective value z_i times its value).  [GRX with C = 2p - m and delta = k - Phi.]
(ZP) (z = all +, T = 0): an avoider has no sub-multiset of rotations of even size in [2kappa+2, 2p] with value sum 0.
(V) Davenport-alpha with I = every second interior gap of every block (|I| = H, pairwise non-adjacent, F >= 2): an
avoider has R + H <= 3p-2, i.e. kappa <= k-1.  An avoider has kappa >= 0 (if H >= p, z = all + and m = 0 qualify).

Weights.  Fix c != 0.  rho_c and rho_-c are LIGHT; every other rotation rho_x is HEAVY with signed weight b_x: the odd
integer with x = b_x c (mod p) and |b_x| <= p-2 if x != 0 (the odd integers in [-(p-2), p-2] are distinct mod p and
miss only 0), and b_0 := p.  eta := number of heavies; a_j := |b| of heavy j; a_max := max_j a_j;
E := sum_j (a_j - 1).

## 1. Statement

**Theorem SHgen.**  In the setting of Sec. 0, if eta >= 1 and
  (H) 2H >= E,
  (K) k <= 2p - eta - a_max - 1,
then w has an identity 2p-subword.

Expansion.  For a heavy h of weight b (a := |b|, s := sign b) with H >= (a-1)/2, u°(h) is w with h replaced in place by
a copies of rho_(sc) and (a-1)/2 pairs of letters deleted from blocks (every block stays odd and nonempty).  u°(h) is in
the form of Sec. 0 with the same k, block values, block parities and runs; H(u°) = H - (a-1)/2,
kappa(u°) = kappa + (a-1)/2, R(u°) = R + a - 1, F(u°) = F - (a-1) >= k; its heavies are those of w other than h, with
the same weights.

## 2. Lemma Ua (eta = 1: the expanded word is solvable)

If eta = 1, h is the heavy (weight a) and H >= (a-1)/2, then u° := u°(h) or w has an identity 2p-subword.
Proof.  Suppose neither does.  All rotations of u° lie in {rho_c, rho_-c}: u° is an RGR word of length 4p-2 with
F, R >= 1, all blocks odd, runs nonempty and kappa(u°) >= 1.  Replace c by -c if needed so that the majority count A°
of u° is >= its minority count B°.
 - A° >= 2p: the trivial cut (2p equal rotations) solves u°.
 - B° >= kappa(u°) + 1: (rho_c rho_-c)^(kappa(u°)+1) has value sum 0 and size 2kappa(u°) + 2 <= 2p; (ZP) fails for u°.
 - 1 <= B° <= kappa(u°) - 1: Corollary B'(b) solves u°.  B° = 0: the C1 composition solves u°.
 - B° = kappa(u°) >= 1: (V) for u° gives kappa(u°) <= k-1.  If k >= p+1, KBH solves u°.  If k <= p, KB solves u°
   unless its capped case arises.  All blocks are odd, so the OR-segments are the single runs; a capped segment G has
   A°_G - B°_G >= 2p-1, hence A°_G = A° = 2p-1 and B°_G = 0: G holds every majority letter and every other run holds
   only minority letters, kappa(u°) of them in total.
   * If the copies have the minority value, they lie in a run other than G, and the k-1 nonempty runs of w other than
     G contain kappa(u°) - a + 1 rotations of w: k - 1 <= kappa(u°) - a + 1 <= k - a, impossible (a >= 3).
   * If the copies have the majority value, w has 2p-1-a majority lights and kappa(u°) = kappa + (a-1)/2 >= kappa + 1
     minority lights; as kappa <= p - 1 - (a-1)/2 and a <= 2p-3, also 2p-1-a >= kappa + 1.  So
     (rho_c rho_-c)^(kappa+1) violates (ZP) for w (size 2kappa + 2 <= 2p): w is solvable, contrary to assumption.
   So the capped case does not arise and KB solves u°.
Every case contradicts the assumption.  []

## 3. Lemma FLEXa (one expansion; other heavies allowed)

Let w avoid and satisfy (K), and let h be a heavy of weight b, a := |b|, with H >= (a-1)/2.  Then u° := u°(h) has no
identity 2p-subword.
Proof.  As w avoids, kappa >= 0, so R >= 2p - k >= eta + a_max + 1 by (K); the number of lights is
L1 := R - eta >= a_max + 1 >= a + 1.
Suppose u° has an identity 2p-subword; GRX gives a pattern z and a sub-multiset Q of u°'s rotations (size m° even,
effective value sum T(z)).  u° and w share k, the block parities, Phi(z), T(z) and the run of every rotation other
than h and its copies; C_max(u°) = C_max(w) - (a-1).  With s0 := 2kappa + 2 - Phi and s1 := 2p - Phi (w's size bounds
for z), m° lies in [s0 + a - 1, s1]; put d := m° - s0 >= a - 1 and e := s1 - m° >= 0.  Replacing z by -z if needed
(Phi and C_max are unchanged; T(z) and all effective values change sign because sum_i theta_i = 0) the copies have
effective value +c, so h has effective value a times c (for x = 0: a = p and pc = 0).  X-lights / Y-lights are the
lights of w of effective value +c / -c, n and M their numbers (n + M = L1).  Q uses i copies (0 <= i <= a), v_X X-lights,
v_Y Y-lights and a set S of other heavies (|S| <= eta - 1); u_X := n - v_X, u_Y := M - v_Y; m° = i + v_X + v_Y + |S|.
A sub-multiset Q' of w's rotations with the same effective value sum (counted as an integer multiple of c, which
preserves it mod p) and an even size in [s0, s1] gives an identity 2p-subword of w by GRX with the pattern z: a
contradiction.  We construct Q' (all sizes below are even, since every weight is odd).
 i = 0: Q' = Q.   i = a: replace the a copies by h (size m° - (a-1) >= s0).
 1 <= i <= a-1:
 (down) drop the i copies, add r3 unused X-lights, drop r4 used Y-lights, r3 + r4 = i: value unchanged, size
        m° - 2r4 <= s1.  Possible iff some r4 with max(0, i - u_X) <= r4 <= min(i, v_Y) has 2r4 <= d.
 (up)   replace the i copies by h, drop r1 used X-lights, add r2 unused Y-lights, r1 + r2 = a - i: value unchanged,
        size m° + 1 - a + 2r2 >= s0.  Possible iff some r2 with max(0, a - i - v_X) <= r2 <= min(a - i, u_Y) has
        1 - a + 2r2 <= e.
 (down) fails iff (D1) u_X + v_Y <= i - 1, or (D2) i - u_X >= 1 and 2(i - u_X) > d.
 (up) fails iff (U1) v_X + u_Y <= a - i - 1, or (U2) a - i - v_X >= 1 and a + 1 - 2i - 2v_X > e.
 (D1)&(U1): L1 = (u_X + v_X) + (u_Y + v_Y) <= a - 2 < L1.  Impossible.
 (D1)&(U2): e = s1 - m° < a + 1 - 2i - 2v_X gives s1 <= a - i - v_X + v_Y + |S|; with v_Y <= i - 1 - u_X and
            |S| <= eta - 1, s1 <= a + eta - 2.  So k >= Phi = 2p - s1 >= 2p - a - eta + 2, contradicting (K).
 (D2)&(U1): d < 2(i - u_X) gives v_Y <= s0 + i - 2u_X - v_X - |S| - 1; with u_Y <= a - i - 1 - v_X,
            L1 = u_X + v_X + u_Y + v_Y <= s0 + a - 2 - u_X - v_X - |S| <= 2kappa + a - Phi.  As
            L1 = 2p + 2kappa - k - eta, k >= 2p - eta - a + Phi >= 2p - eta - a, contradicting (K).
 (D2)&(U2): 2(i - u_X) > d >= a - 1 gives i >= (a+1)/2 (a odd); a + 1 - 2i > e >= 0 gives i <= (a-1)/2.  Impossible.
So (down) or (up) succeeds.  []

## 4. Proof of Theorem SHgen

Suppose w avoids; (H) gives H >= (a-1)/2 for every heavy.  Induction on eta.
eta = 1: Lemma Ua makes u°(h) solvable (w avoids); Lemma FLEXa forbids it.
eta >= 2: pick a heavy h of weight a.  u° := u°(h) is in the form of Sec. 0 with eta - 1 >= 1 heavies,
2H(u°) = 2H - (a-1) >= E - (a-1) = E(u°), a_max(u°) <= a_max and k <= 2p - eta - a_max - 1 <= 2p - (eta-1) - a_max(u°) - 1.
By induction u° is solvable; Lemma FLEXa forbids it.  []

## 5. Scope and non-claims

Covered: every word in the form of Sec. 0 (constant odd blocks, nonempty runs, length 4p-2, p >= 5) whose heavies
relative to some c != 0 satisfy (H) and (K); any kappa; rho_0 allowed (weight p).  For a single heavy +-3c,
Theorem SH3+- (proof-SH3-v4.md) needs no condition on k.
Not covered: 2H < E; k > 2p - eta - a_max - 1; non-constant reflection runs; words for which no c gives (H) and (K).
This is not ROT(p), INV*(p) or ordered Olson; no novelty claim.
