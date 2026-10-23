# K7-Z2-erratum-v1: import/wording overlay on K7-Z2-v1 (no theorem change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T00:55:58-0700.
- **Overlays:** `K7-Z2-v1.md`, sha256 cda7573de2401c220493d55e37fdc09b3292590522fc0258ba9a5ca6e27ecbe7 (frozen, unchanged).
- **Responds to:** Claude `RUN/review/sun7-z2-claude-v1.prompt.note.md` (sha256 1b671509fd615469abee89158310c457dd2162275c045e94820f44025c0f8368; ACCEPT-WITH-FIXES, 0/0/10
  MINOR) and Codex `RUN/review/sun7-z2-codex-v1.prompt.stdout.txt` (sha256 80a999f9ab332e8edec075e8b49c5f65e52b87a2b481d1175293a7949f373033; ACCEPT-WITH-FIXES, 0/0/1 MINOR).
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Status:** overlay only; Lemma Z-ROW, Lemma CROSS, Lemma LIGHT and Theorem K7-Z2 keep their statements and scope.

## G1 (Claude 1): ROW-1 is now an accepted import with its mandatory erratum

Replace every citation "K7-M1-v1.md Lemma ROW-1 (CANDIDATE, under review)" by: **Lemma ROW-1 of `K7-M1-v1.md` (sha256
6e9b2d09...5d63) read with its mandatory erratum `K7-M1-erratum-v1.md` (sha256 4094b537...c510), accepted by
`RUN/review/sun7-M1-parent-verdict-v1.md` (sha256 7121ceeedc1f1b0de8d9642c8f5c2aed052d9f2e83140afee33ffcd2f71ced84)**, in particular F2 (actual exponents; here m_p = 5^(h_p)
with A = 0, B = h_p >= 1, and only [5 | m_p] enters a gcd), F3 (ROW-U-deg, used by ROW-1 (c)) and F5 (the corrected
feasibility sentence of ROW-1 (b), last case). In section 7 read "K7-M1 (accepted with mandatory erratum)".

## G2 (Claude 2, Codex): ROW-1 used at the marked centre z — explicit transfer

ROW-1 is stated at an unmarked apex v in a configuration with one marked vertex. Section 2 uses its *proof* at the marked
apex z under the following transfer hypothesis **ROW-1-deg at z**: g_zj = 6 for all six neighbours; five neighbour labels
have the form w_u alpha_zu with w's pairwise coprime and coprime to 30; the sixth label has the form m w alpha with m odd
and {3,5}-smooth (here m = m_p = 5^(h_p)); and LFC (d) holds at z. ROW-1's proof uses exactly these facts (it never uses
the apex's own index). Renaming: ROW-1's apex v becomes z, ROW-1's marked neighbour z becomes p. When there is no p,
ROW-U applies directly (its statement allows a marked apex).

## G3 (Claude 3): explicit weights in the k3 kill of section 2

In section 2, case "some unmarked alpha_zu = 3": by ROW-1 (b), k3 >= 3, no unmarked entry is 4 or 5, alpha_zp in {1,2}.
Weights: y = 1/3 on the unmarked threes, y = 1 on the remaining unmarked ones, y = 1/2 on the remaining unmarked twos;
these five contribute exactly 5. Then: if alpha_zp = 1, put y_p = 1: lambda_p = 5^(h_p) w_p is coprime to every other
label (k5 = 0 and the unmarked entries lie in {1,2,3}), so p lies only in {p}; if alpha_zp = 2, put y_p = 1/2: every
allowed set through p is {p} or {p, two} (any triple through p has all gcds equal to 2, and p shares no prime with ones
or threes). Either way the value is 6, contradicting LFC (d). Hence k3 = 0.

## G4 (Claude 4): the inverted application

The exclusion of k5 = 5 uses LFC (d) for the inverted configuration (whose alpha-matrix is alpha*); the conclusion for
alpha* in Lemma Z-ROW uses the same argument for the inverted configuration, whose own inverted configuration is the
original one (INV (a): alpha** = alpha). When there is no p, ROW-U applies to alpha* by INV (a) with erratum E6 (same
labelled index tuple, hence the same markers).

## G5 (Claude 5): complete import list

Add: **R0** (README section 1; theorem statement), **LFC (a), (c), (d)** by name, **Sun(2)** (erratum E2; used via (V3)
in LIGHT (L2)), **E6**, and the note that **L1 (T1)-(T3) and (F7) are applied to the inverted configuration as well**
(Lemma CROSS for alpha*, T1 inverted step, T2).

## G6 (Claude 6, Codex): Sun dependencies

Replace "Sun(t) inside U_z only with t <= 3 (through V3)" by: **"Sun(t), t <= 6, inside U_z and inside the conjugate
g_z U_z g_z^-1 only through the imported LFC / ROW-U / ROW-1 arguments of section 2; the additional applications of
section 5 through (V3) use only Sun(2) and Sun(3)."**

## G7 (Claude 7): CROSS notation and the alpha*-orientation

In Lemma CROSS write x_ab := alpha_ab (not x, which collides with L1's vertex letters), s_a := alpha_za, s*_b := alpha*_zb,
and 5^(h_p) for the 5-part of a marked neighbour. In the alpha*-triangle the labels are (alpha*_za, alpha*_zb, alpha*_ab)
= (4, s*_b, x*_ab): the small entry sits at b, not at a. The table transfers because both edge-at-z terms ignore odd ell
(s / gcd(s, ell) = s and 4 / gcd(4, ell) = 4) and tau_max is symmetric under a <-> b. (C3) is restated: **for
x_ab in {2, 4} (i.e. after (C1))**, tau_min(z, a, b) = 4, hence F7 gives X_a subset X_b whenever x_ab s_a <= 4; for
x_ab = 3 one has tau_min = 12 and for x_ab = 5 tau_min in {20, 4}, cases already removed by (C1).

## G8 (Claude 8): LIGHT gcd identity and the disjointness step

In Lemma LIGHT: the (V3) local index is d_v = q_v n_v / 6 = alpha*_zv r_v (= lambda*_v), with r_v = m_v w_v. Its gcd
reduction gcd(d_v, d_v') = gcd(alpha*_zv, alpha*_zv') uses two facts: alpha*_zv in {1,2,4} (Lemma Z-ROW) and **r_v odd for
every v != z** (only z carries the 2-marker; the possible p carries only 5). Each D_v and each intersection of D's is
left U_z-invariant, hence a union of right cosets U_z y; so a non-empty intersection D_b cap D_b' contains a right coset
R subset D_b, and if D_b subset D_a then R subset D_a and {a, b, b'} subset S_R, contradicting (L1). In T1, if at most one
element of F is out, every pair from F contains an in element, so the three light sets are pairwise disjoint.

## G9 (Claude 9): T2 by inversion, spelled out

For the inverted configuration: F_inv = F*, F*_inv = F, s_inv = s*, s*_inv = s; the vertex a0 (with alpha_za0 = 1) plays
the role of b0; Lemmas Z-ROW, CROSS and LIGHT hold for it (same z, same markers, alpha** = alpha). Type T2 of the original
is type T3 of the inverted configuration, whose proof gives X*_b subset X*_a0, D*_a0 subset D*_b, and the coprime label
of a0 (alpha_za0 = 1) contradicts (L2).

## G10 (Claude 10): probe remark

The status-line remark on probe v10 is restricted to the **examined range** of capped profile tuples (items examined by
that exploratory run); it is not a premise and not a claim.

## Remarks recorded (no change)

Claude's mutation controls (alpha = 4, alpha* = 2 on F* x F dies only in the inverted step; a 3-marker on z would admit
(s, x) = (2, 3) and break (C1)) are consistent with the stated scope; the theorem's no-3-marker hypothesis is
load-bearing.
