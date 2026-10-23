# Scope note F39 — seven-row difference matrices over the Frobenius group of order 39 (2026-10-19T06:39:37-0700, ContinueCFR21)

Status: written only (parent IRC 2026-10-19 ~06:3x; no execution, runtime HOLD in force). Every lemma below is a
worker proof marked CANDIDATE (unreviewed). Heuristics are labelled [HEURISTIC]. Nothing here constructs or excludes a
difference matrix, and nothing bears on the existence of six MOLS(39) beyond the stated sufficiency (Lemma F0).
Two corrections to the worker's IRC summary of about 06:2x are recorded in section 7.

## 0. Setting
G = F39 = Z_13 x|_omega Z_3: elements (n, a) with n in Z_13 and a in Z_3, product (n1, a1)(n2, a2) = (n1 + omega^a1 n2,
a1 + a2), with omega = 3 (omega^3 = 27 = 1 mod 13, omega != 1). Inverse (n, a)^-1 = (-omega^-a n, -a). N = {(n, 0)} is
the unique Sylow 13-subgroup, normal; phi : G -> G/N = Z_3, (n, a) -> a. Standard Sylow facts: the groups of order 39
are Z_39 and this group (omega = 9 gives an isomorphic group), so F39 is the only non-abelian group of order 39.
Its abelianisation is G/G' = G/N = Z_3 (G' = N because t (n,0) t^-1 (n,0)^-1 = ((omega - 1) n, 0) covers N).
Definition. A (G, k; 1)-difference matrix (DM) is a k x 39 array D with entries in G such that for all rows x != y the
39 elements D_x(c) D_y(c)^-1 (c over the columns C) are exactly the elements of G. The gauge: right-multiplying a
whole column by h in G (c -> c h) preserves every D_x D_y^-1, so columns are taken modulo right translation; distinct
columns of a DM stay distinct modulo the gauge (else d_01 would repeat a value).

## Lemma F0 (CANDIDATE; standard construction written out). A (G, k; 1)-DM gives an OA(k+1, |G|) of index 1, hence
## k - 1 MOLS of order |G|. In particular a (F39, 7; 1)-DM gives six MOLS(39).
Proof. Runs (c, g) in C x G. Factors f_inf(c, g) = c and f_x(c, g) = D_x(c) g (x = 0..k-1). For (f_inf, f_x) and a
target (c0, u): g = D_x(c0)^-1 u is unique. For (f_x, f_y) and a target (u, v): D_x(c) g = u and D_y(c) g = v force
D_x(c) D_y(c)^-1 = u v^-1, which determines c (DM property), and then g = D_x(c)^-1 u. So every pair of factors takes
every pair of values exactly once. An OA(k+1, n) of strength 2 and index 1 gives k+1-2 MOLS of order n. QED

## Lemma F1 (CANDIDATE; transfer of Theorem A through G -> Z_3)
Let D be a (F39, k; 1)-DM and a_x(c) = phi(D_x(c)) in F_3. Then for x != y, a_x - a_y takes every value of F_3 exactly
13 times, and the conclusions of Theorem A hold for the array a: if k >= 4, no nonzero sum-zero mod-3 character of
support <= 5 is constant on the columns; for k = 7 the mod-3 affine rank of a is 5 or 6 (Corollary A1 shapes apply).
Proof. phi is a homomorphism onto an abelian group, so phi(D_x D_y^-1) = a_x - a_y; as D_x D_y^-1 runs over G once and
every fibre of phi has 13 elements, a_x - a_y is balanced. Theorem A (text /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21/evidence/theoremA-mod3-rank-v1.md, sha256 10e9b724b40b2a6d1f81827cf82f4cabf7d1e14d8b113cbe9fa15291ac969094, with errata
7f92e7c3... and 83679b8e...; parent verdict /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/cfr21-theoremA-parent-verdict-v1.md, sha256 937b980ec415df8294751911c8fff57cd88881b7ade0ac270e8b6d19675bf509,
CORRECTNESS_ACCEPTED_SCOPED_PARTIAL) is proved in Steps 0-3 using only (i) this balance for every pair of rows and (ii)
that the number of columns, 39, is divisible by 3 but not by 9. Both hold, so its proof applies verbatim. QED
In particular Lemma L3 (support 3) holds for F39 DMs with k >= 4; it is used in F4 and F5.

## Lemma F2 (CANDIDATE; twisted-difference form)
Write D_x(c) = (n_x(c), a_x(c)). Then D_x(c) D_y(c)^-1 = (n_x(c) - omega^(a_x(c) - a_y(c)) n_y(c), a_x(c) - a_y(c)).
Hence D is a DM iff for every pair x != y: (i) a_x - a_y is balanced, and (ii) for each delta in Z_3, on the 13 columns
F_xy(delta) = {c : a_x(c) - a_y(c) = delta} the map c -> n_x(c) - omega^delta n_y(c) is a bijection onto Z_13.
Proof. (n_x, a_x)(-omega^-a_y n_y, -a_y) = (n_x - omega^(a_x - a_y) n_y, a_x - a_y), using the product rule; the pair
map c -> D_x D_y^-1 is a bijection onto G iff its Z_3 part is balanced and on each Z_3-fibre the Z_13 part is a
bijection. QED
Remark F2a (exact, elementary). Only phi is a homomorphism; G has no homomorphism onto Z_13 (G^ab = Z_3). So the
CRT split used for Z_39 (mod-13 skeleton, GF(3) lift, structural notes S4/R1) has no analogue: here the "skeleton" is
the Z_3 image a (fibres of size 13) and the "lift" n must satisfy condition (ii) on fibres of size 13.
Remark F2b (exact). For a list M of 13 elements of F_13: M is a permutation of F_13 iff the power sums
p_j(M) = sum m^j vanish for 1 <= j <= 11 and p_12(M) = -1. (Newton's identities determine e_1..e_12 from p_1..p_12
because j! is a unit mod 13 for j <= 12; then prod (X - m) = X^13 - X - e for a constant e; all m are roots, and
t^13 = t on F_13 forces e = 0. Without p_12 the constant list (13 copies of one value) also has p_1..p_11 = 0.)
Only p_1 is linear: sum over F_xy(delta) of (n_x - omega^delta n_y) = 0. So the GF(3) device of S4 (linear fibre
sums plus one nonzero functional per fibre, which is exact for fibres of size 3) has no counterpart: for fibres of size
13 the exact condition has degree 12. For k = 7 the linear relaxation has 3*21 = 63 equations against 7*39 = 273
unknowns n_x(c) (before gauge), so it carries little information.

## Lemma F3 (CANDIDATE; automorphisms act trivially on G/N)
Every automorphism theta of G maps N onto N and induces the identity on G/N. Consequently, for every symmetry
(theta, pi, (g_x)) of a DM (see section F4), the induced map on the mod-3 image is a -> (a_(pi^-1 x) + phi(g_x))_x:
row permutation plus row constants, with multiplier +1 only (over Z_39 the mod-3 multiplier can be -1).
Proof. N is the unique Sylow 13-subgroup, so theta(N) = N and theta(n, 0) = (u n, 0) for a unit u of Z_13. Let
t = (0, 1) and theta(t) = (m, b). Conjugation: t (n, 0) t^-1 = (omega n, 0) and (m, b)(x, 0)(m, b)^-1 = (omega^b x, 0).
Applying theta to the first identity: (omega^b u n, 0) = (u omega n, 0) for all n, so omega^b = omega and b = 1
(omega has order 3). Thus theta(t) is in tN and theta induces the identity on G/N = <tN>. QED
(Every pair (u, m) with u in Z_13^* and m in Z_13 gives an automorphism theta_(u,m)(n, a) = (u n + m [a]_omega, a),
[a]_omega = 1 + omega + ... + omega^(a-1); |Aut(G)| = 156. The inner ones are exactly those with u in <omega>; those with
u = 1 are conjugations by elements of N.)

## Lemma F4 (CANDIDATE; row-fixing symmetries)
A symmetry is s = (theta, pi, (g_x)) with theta in Aut(G), pi in Sym(rows), g_x in G, acting on columns modulo the gauge
by (s.c)_(pi x) = g_(pi x) theta(c_x); it is a symmetry of D if it maps the column set onto itself.
Statement. Let D be a (F39, k; 1)-DM with k >= 4 and s a symmetry with pi = id. Then either s acts trivially on the
columns, or k <= 5 and s is (after the normalisation below) a pure left translation of the rows by elements
q_x in N whose classes in N / <omega> (the classes {0} and the four cosets of <omega> in Z_13^*) are pairwise
distinct; such an s has order 13 and fixes no column. In particular, for k >= 6 (so for k = 7) every row-fixing
symmetry acts trivially.
Correction: the worker's IRC summary said "for k >= 4". As stated without the exception this is unproven. The
threshold proved here is k >= 6, and for k = 4, 5 the exception above remains.
Proof. For rows x != y let d_xy(c) = c_x c_y^-1 (gauge-invariant; a bijection C -> G) and A_xy(w) = g_x theta(w) g_y^-1.
Then d_xy(s.c) = A_xy(d_xy(c)), so s on C is conjugate to the permutation A_xy of G, for every pair; in particular all
A_xy have the cycle type of s, and d_xy maps the fixed columns of s onto Fix(A_xy).
(1) All phi(g_x) are equal. By F3, phi(A_xy(w)) = phi(w) + tau_x - tau_y with tau_x = phi(g_x). If tau_x != tau_y,
every cycle of A_xy visits the three cosets of N cyclically, so all cycle lengths of s are multiples of 3. Since k >= 4,
two rows share a value of tau; for that pair A_xy maps each coset (13 elements) to itself, so its cycles partition 13,
which is not a multiple of 3. Hence no pair has tau_x != tau_y.
(2) Normalisation. With h in G, phi(h) = tau, the same column map is given by (conj_h o theta, g_x h^-1) (right-multiply
every column by h^-1), and now every g_x lies in N; write g_x = (p_x, 0) and theta = theta_(u,m).
On the coset of a, A_xy(n, a) = (u n + p_x + m [a]_omega - omega^a p_y, a): an affine map with slope u.
(3) Case u != 1: each coset contains exactly one fixed point, so |Fix(A_xy)| = 3 with one element in each coset. The
3 fixed columns F therefore satisfy: a_x - a_y takes all three values on F, for every pair. The 3 x k array
(a_x(c)) for c in F is a (Z_3, k; 1)-DM, impossible for k >= 4 (it would give k - 1 >= 3 MOLS of order 3).
(4) Case u = 1: theta = conjugation by some n0 in N, and after the gauge c -> c n0 the map is a pure translation
c_x -> q_x c_x with q_x = g_x n0 in N. On the coset of a, A_xy translates by t_a = q_x - omega^a q_y. Let
f(x, y) = #{a : t_a = 0}, so |Fix(s)| = 13 f(x, y), which is the same for all pairs. f = 3 iff q_x = q_y = 0; f = 1 iff
q_x, q_y are nonzero with q_x / q_y in <omega>; otherwise f = 0.
 - f = 3 for all pairs: all q_x = 0 and s is trivial.
 - f = 1 for all pairs: q_x = omega^(b_x) q with q != 0, and Fix(A_xy) is the coset of b_x - b_y. With a'_x = a_x - b_x,
   the 13 fixed columns are exactly those where a'_x - a'_y = 0, the same set F for every pair. For three rows x, y, z,
   put f1 = a'_y - a'_x and f2 = a'_z - a'_x: both vanish exactly on F, f1 - f2 vanishes exactly on F, so off F
   {f1, f2} = {1, 2} and f1 + f2 = 0 there, and also on F. Hence a'_x + a'_y + a'_z is constant: the support-3
   character e_x + e_y + e_z is constant on a, contradicting L3 (F1, k >= 4).
 - f = 0 for all pairs: the q_x lie in pairwise distinct classes of {0} and the four cosets of <omega> in Z_13^*, so
   k <= 5; s has order 13 and no fixed column. This is the stated exception. QED

## Lemma F5 (CANDIDATE; faithfulness on columns)
For a (F39, k; 1)-DM with k >= 4, a symmetry that fixes every column (modulo the gauge) acts trivially. (Over Z_39 the
analogue, structural note S5, needed k odd; here no parity condition is needed because of F3.)
Proof. If s.c = c h_c for every column c, then c_(pi x) h_c = g_(pi x) theta(c_x); applying phi and F3:
a_(pi x)(c) - a_x(c) = tau_(pi x) - phi(h_c) for all x. For rows x, z the character e_(pi x) - e_x - e_(pi z) + e_z is
constant on a. If pi != id, take x with z = pi x != x. If pi z = x, the character is -(e_z - e_x) != 0 of support 2:
a_x - a_z would be constant, but it is balanced. Otherwise x, z, pi z are distinct and the character is
-(e_x + e_z + e_(pi z)), of support 3: contradicts L3 (k >= 4). So pi = id. Then d_xy(c) = g_x theta(d_xy(c)) g_y^-1
for all c, and since d_xy is onto, w = g_x theta(w) g_y^-1 for all w in G. At w = e this gives g_x = g_y =: g, hence
theta = conjugation by g^-1, and (s.c)_x = c_x g: s acts trivially. QED

## 6. [HEURISTIC] density comparison (arithmetic only, math.lgamma in the worker's kernel; no probe, no search)
Model: row 0 normalised to e, columns unordered, rows 1..k-1 bijections, and each of the C(k-1, 2) pairs among them
independently "orthogonal" with the probability given by the Eberhard-Manners-Mrazovic asymptotic for complete
mappings (arXiv:2003.01798, Adv. Math. 2022: the number of complete mappings of a group G of order n satisfying the
Hall-Paige condition is (e^-1/2 + o(1)) |G^ab| n!^2 / n^n): per pair P ~ e^-1/2 |G^ab| n!/n^n. Labelled count
E = (n!)^(k-2) P^C(k-1,2). Orbit size of the equivalence group on normalised objects <= n^(k-1) |Aut(G)| k!.
All columns are log10.
| group | n | k | G^ab | Aut | log10 P per pair | labelled | orbit | classes | status |
|---|---|---|---|---|---|---|---|---|---|
| Z21 | 21 | 6 | 21 | 12 | -6.95 | 9.3 | 10.5 | -1.2 | exists (Sage DM_21_6_1) |
| Z21 | 21 | 7 | 21 | 12 | -6.95 | -5.8 | 12.7 | -18.5 | open (CFR(6,21)) |
| Z35 | 35 | 7 | 35 | 24 | -12.70 | 9.6 | 14.3 | -4.8 | exists (Sym2026 Ex.3) |
| Z39 | 39 | 6 | 39 | 24 | -14.37 | 41.6 | 12.2 | 29.4 | exists (anchor) |
| Z39 | 39 | 7 | 39 | 24 | -14.37 | 16.0 | 14.6 | 1.4 | open (target) |
| F39 | 39 | 7 | 3 | 156 | -15.48 | -0.7 | 15.4 | -16.1 | open, not examined |
| F39 | 39 | 6 | 3 | 156 | -15.48 | 30.4 | 13.0 | 17.4 | not examined |
| Z55 | 55 | 7 | 55 | 40 | -21.09 | 49.1 | 15.7 | 33.4 | exists (Sage DM_55_7_1) |
Reading: (a) the model is badly calibrated near the threshold. DM35 (k = 7) exists although the model predicts
10^-4.8 classes, and Sage DM_21_6_1 exists at 10^-1.2. So absolute values can be off by five orders or more, and
structured DMs (large automorphism groups) are exactly what the model misses. (b) The comparison between F39 and Z39 at
the same (n, k) is driven by the abelianisation factor |G^ab| = 3 versus 39 in each of the 15 pair probabilities
(13^15 ~ 10^16.7) and by |Aut| = 156 versus 24 (10^0.8). So F39 is about 10^17.5 times less dense than Z39 in this model
(F39 k = 7: about 10^-16 classes against about 10^1.4 for Z39). Whether the o(1) terms at n = 39 change this is unknown.
Correction: the worker's IRC summary said "the heuristic density is the same order as for Z39". That ignored the |G^ab|
factor and is withdrawn.

## 7. Conclusions and scope
- F0: a (F39, 7; 1)-DM would give six MOLS(39). No source read by this lane reports one, and no lane has searched for
  one. Evans' papers on orthomorphisms of non-abelian groups (Discrete Math. 243 (2002); J. Combin. Des. 15 (2007)) were
  seen only as citations and are UNREAD.
- F1-F5 restrict symmetric models over F39. The mod-3 image obeys Theorem A, and symmetries induce multiplier +1 on
  it. A row-fixing symmetry is trivial for k >= 6. Symmetries act faithfully on columns for k >= 4. So any symmetric
  model must move rows.
- Section 6 [HEURISTIC]: F39 is much less promising than Z39 in the standard random model. Together with F2a/F2b (no
  linear-algebra shortcut for the lift), this lane does not propose an F39 search and requests no GO.
- Nothing here bears on the existence of a (Z_39, 7; 1)-DM, a (F39, 7; 1)-DM or six MOLS(39).
