# K63-RES-erratum-v2: consolidated disposition of the two CLI reviews (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:58:32-0700.
- **Overlays (all frozen, unchanged):** `K63-RES-v1.md` sha256 1542a551f6d9787784a2434d18a5aa7275f673b23aab4901a384518206f67515;
  `K63-RES-erratum-v1.md` sha256 e70a5518a74ee4230d442a1b81d562d65b683ab6fcb904ff306792ea0ac3b49b.
- **Responds to:** `RUN/review/sun7-K63RES-codex-v1.prompt.stdout.txt` (ACCEPT all five, 0/0/1: M1) and
  `RUN/review/sun7-K63RES-claude-v1.prompt.note.md` (CORRECT all five, 0/0/9: m1-m9), relayed by the parent, which
  asked for exactly one consolidated overlay. RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- Every item below is a citation, wording or scope repair. No theorem, lemma statement, case or weight changes.

## X1 (Claude m1, m2; Codex M1): the product formula; TG removed from the premises
- In section 0, delete the premise bullet "TG (parent verdict ... general computational form ...)". TG is not used.
- Replace the premise "L0.3 identity and range (`K7-LFC-INV-erratum-v1.md` E1)" by two items:
  (i) **old README section 1, L0.1**: |XY| = |X||Y| / |X cap Y| for subgroups X, Y of a finite group, hence
  mu(XY) = [G : X cap Y] / ([G : X][G : Y]); with **Lagrange**, [G : X cap Y] is a common multiple of [G : X] and
  [G : Y], so mu(XY) >= 1 / gcd([G : X], [G : Y]);
  (ii) `K7-LFC-INV-erratum-v1.md` E1 **only** for the range 1 <= alpha <= g - 1 of disjoint cosets.
- Every use of "the L0.3 formula" for a product with a multiple intersection or an arbitrary subgroup H (section 1:
  mu(V_e W_m) = T_(m+1)/(n_e T_m) and the final display; section 2 (b): mu(W*U_v) = mu(U_vW*)) cites (i). The
  pairwise measure mu(V_eV_j) = beta_ej / g_ej is (i) with X = V_e, Y = V_j.

## X2 (Claude m3): the VFC import
Section 2 (a) uses VFC (V1)-(V4) and the VFC-count argument of rules-k7-v1 section 2 (sha256
77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee), accepted in the written parent verdict
`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md`
(sha256 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35; "Fibre construction and counts"). This is the
citation added to section 0. *Alternative proof of (a), not needed:* (a) is (b) applied to the inverted configuration
(INV (a) with E6 keeps the labelled index tuple and the choice of v; its conjugate family is a conjugate of U, with
beta = alpha <= g - 1 by E1; its LFC labels are n_j alpha*_vj / g_vj).

## X3 (Claude m4): one letter for two objects
In section 0 (hypothesis (B)), section 1 and section 2, the subgroup family is renamed **Phi = (Phi_j)**; V keeps
meaning the vertex set. "FG for V = U" reads "FG for Phi = U", and so on.

## X4 (Claude m5): the normalisation in section 2
Replace the opening sentence of section 2 by: "Left-translate every coset by g_v^-1, so that g_v = 1. This replaces
each g_j by g_v^-1 g_j and therefore conjugates the family U* (and W*) by g_v^-1; indices, alpha, alpha*,
disjointness and hypothesis (B) are unchanged, so FG applies to the conjugated family. The contradiction step in (b)
uses g_v = 1 (U_v = g_vU_v)."

## X5 (Claude m6): case (1b)
Replace "(z is incompatible with every five)" and the corresponding sentence of erratum v1 R1 ("Effect") by: "h_d >= 1
makes every C-vertex unmarked, so type(z) = x_z in {1, 2, 3, 4} and type(f) = 5 for every five f; gcd(x_z, 5) = 1, so
z is incompatible with every five (this includes z a three)." The appeal to (F3) in (1b) is withdrawn; (F3) is used
only where k5 = 0.

## X6 (Claude m7, with Codex's direct check): the restricted star remark
- Section 0, "Not used: K63-CLIQUE" reads "Not used **for Theorem K63-RES**: K63-CLIQUE ...".
- Section 6, "Star question", is re-justified without CLIQUE's proof steps: inside the section 0 residue, with v in O
  and h_v = 0, the star hypothesis alpha_vc = alpha*_vc = 3 (c in C minus {v}) is excluded by Theorem K63-RES; directly,
  INV (b) gives an orientation x with x_vd = 1, and that row is Row Lemma case (2) with x_* = 3 (all five C-entries 3,
  all six pairwise label gcds exactly 3, y = 1/3 feasible, val = 17/3 > 5). The sentence "steps (ii)-(v) use only v's
  row; so the withdrawn star statement is valid for such v" and its route through CLIQUE steps (ii)-(v) are withdrawn.
  Erratum v1 R2 (scope: the section 0 residue only) stays.

## X7 (Claude m8): CLIQUE is not a sub-case of the residue
Section 5, "The accepted K63-CLIQUE is the special case of the residue with the full all-3 clique and is not used
here" reads: "The accepted K63-CLIQUE is stated for all of K6.3; its overlap with the residue is the instance k3 = 4,
x_* = 3 of Row Lemma case (2). It is not used here."

## X8 (Claude m9): Sun instances and the import boundary
Section 0, "Sun(t), t <= 6, only inside LFC (c) and VFC (V3)" is made explicit. Load-bearing instances (all inside
U_v, through LFC (c) / VFC (V3)):
- **Sun(2)**: an incompatible pair never shares a fibre (every case);
- **Sun(3)**: three pieces with pairwise gcd 2 (the triple {z1, z2, i*} in case (4b); triples with two twos in the
  standard weights);
- **Sun(4)**: four pieces with pairwise gcd 3 (the gcd-3 cliques of cases (2), (3), (4));
- **Sun(6)**: six pieces with pairwise gcd 5 (case (1c) with x_* = 5; without it the bound would cap val at 5).
Sun(5) is not used. **Import boundary:** Sun(5) and Sun(6) are accepted imports that are themselves computer-assisted
and model-reviewed (`RUN/review/sun7-lfc-inv-parent-verdict-v1.md`, sha256
8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18, "Finding dispositions and remaining limits"). "No
computation is a premise" holds for the arguments of K63-RES itself, not for its whole import closure, since Sun(6)
is load-bearing in case (1c).

## Unchanged
Lemma FG, Corollary 5/6, the Row Lemma (all cases and weights), Theorem K63-RES and its scope, and erratum v1 R1-R2
(as amended by X5, X6). The parent's independent explicit-weight control (`RUN/review/k63-row-controls-v1/`) is a
navigation aid, not a premise. No novelty, priority, Lean or human-review claim.
