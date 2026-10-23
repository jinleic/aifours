# K62-FG-erratum-v2: attribution and wording overlay matching the accepted K63-RES conventions (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T04:03:19-0700.
- **Overlays (frozen, unchanged):** `SETTING-v1.md` (sha256 3bff4e6618cb6591683f7adcc1fbd52fbd3dd16e306b024be6181c332f42bb8d),
  `K62-FG-v1.md` (sha256 d47e3747ce16ffc21aa818229e79a2028923ec8722aaaae14031e079b4cad083), `K62-FG-erratum-v1.md`
  (sha256 debcb0331cc474f3d5833cd1e5b791ccf209a2f8da7a8414b55685bc6ef05500).
- **Source:** the reviews of K63-RES (Codex M1, Claude m1-m9) and the parent verdict
  `RUN/review/sun7-K63RES-parent-verdict-v1.md` (sha256 5ac595295727218cd86d0888720213972fe0520f64cea8d93a5c50ef18ed7bac),
  whose acceptance of FG / Corollary 5/6 is **at the exact K6.3 setting only**. Nothing in this directory is promoted
  by that verdict; Lemma FG-62 and Corollary 5/6-62 remain candidates with their own proofs.

## Y1: product formula and TG
In `SETTING-v1.md` (import boundary) delete "TG in its general computational form". Every product measure for
arbitrary subgroups (FG-62 step and final bound; Corollary 5/6-62) cites **old README section 1 L0.1**
(|XY| = |X||Y| / |X cap Y|) with **Lagrange** (lcm of the two indices divides [G : X cap Y]). `K7-LFC-INV-erratum-v1.md`
E1 is cited only for the range 1 <= alpha <= g - 1. This supersedes Q2 of erratum v1 (which wrote "L0.3 formula").

## Y2: VFC
VFC (V1)-(V4) and the VFC count (rules-k7-v1 section 2, sha256 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee)
are cited to `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` (sha256
73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35).

## Y3: notation and normalisation
The subgroup family in Lemma FG-62 is renamed **Phi = (Phi_j)** (V is the vertex set). In Corollary 5/6-62, left-
translating by g_v^-1 conjugates U* and W* by g_v^-1; indices, alpha, alpha* and (B) are unchanged, so FG-62 applies
to the conjugated family; the disjointness step on the LFC side uses g_v = 1.

## Y4: Sun instances and import boundary
Load-bearing instances, all inside U_v through LFC (c) / VFC (V3): Sun(2) (incompatible pairs: Lemma OO, the R2 row
lemma); Sun(3) (gcd-2 triples inside the standard weights of the R2 row lemma); Sun(4) (the gcd-3 sets of size <= 3
at d in Lemma D). Sun(5) and Sun(6) are not used in `K62-FG-v1.md`. The section 5 obstruction uses no Sun theorem (its
dual certificate uses only sets that are allowed by definition). Sun(5)/Sun(6) remain computer-assisted accepted
imports of the wider closure (verdict 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18).

Nothing else changes.
