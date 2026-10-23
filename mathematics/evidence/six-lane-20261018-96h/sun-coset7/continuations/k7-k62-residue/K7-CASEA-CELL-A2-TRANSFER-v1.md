# K7-CASEA-CELL-A2-TRANSFER: named-claim transfer of K7-CASEA-K23 and K7-CELL to (a2-no5) (conditional)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:43:44-0700.
- **Owner:** Sun7K62Successor. Dependency-use audit only; no new mathematics beyond the audit; no computation.
- **Status:** CONDITIONAL on: Theorem K7-A2-BRIDGE and Corollary K7-A2-TRANSFER of `K7-A2-FIVE-v1.md`
  (93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc) as amended by `K7-A1-A2-delta-erratum-v1.md`
  (0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e); `K7-CASEA-K23-v1.md`
  (f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3); `K7-CELL-v1.md`
  (d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae) with `K7-CELL-erratum-v1.md`
  (56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132). No closure claim.

## Statement

**Corollary K7-CC-A2 (conditional).** In (a2-no5), with W := W' cup {p}, T, T* as in Theorem K7-A2-BRIDGE, the following
named claims hold, with RICH replaced by Theorem K7-A2-BRIDGE and A1-STRUCT/K7-TC/K7-TC-A22 replaced by their
transferred versions (Corollary K7-A2-TRANSFER): from K7-CASEA-K23 - the rigid-row list (R), Lemmas K3, K2, CL, S, the
exclusions (S-a)-(S-f), Theorem K7-CASEA-K23 and Proposition K7-CASEB-T; from K7-CELL - Lemmas EQ, SUB, IN, CELL and
Theorems K7-CELL-A, K7-CELL-B. Not transferred: navigation remarks and the conditional chain of K7-CELL section 7 as a
claim.

## Dependency-use audit (what each step reads, and why it holds in (a2-no5))

| step | (a1) fact read | (a2-no5) replacement |
|---|---|---|
| rows (R), twin rule, triangle rule | label gcds = entry gcds; ell's odd | (B2): p's labels / local indices are entry * 5^B w_p, and no other label has a factor 5 (no entry 5; r_z, r_t prime to 5); ell_p = 5^B w_p is odd |
| Lemma K3, Lemma EQ, Theorem K7-CASEA-K23 count | Lemma FG-V at a W-apex | FG-V for the actual subgroups of C via G0 + FG-a2 (a) (apex in W') or (b) (apex p) (A2.17 (iv)) |
| Lemma CL | Corollary L (both orientations) | transferred Corollary L (A2.17; Sun(5) direct as recorded there) |
| Lemma S, (S-a)-(S-f) | graph structure on the five vertices of W; K2, K3, CL, INV, LFC (d) at t | the same five-vertex combinatorics; LFC (d) at t with labels via (B2) |
| Lemma EQ | odd parts of local indices pairwise coprime | odd parts are distinct w's, 5^B w_p for p, 3^A w_t for t, 3 w_z for z: pairwise coprime |
| Lemma SUB, Lemma IN | subgroup algebra; LFC (a)-(c) at the apex; n_j = 6 r_j | unchanged (group-theoretic; n_p = 6 5^B w_p, n_p/3 = 2 5^B w_p) |
| Lemma CELL | piece indices n_v/3 = 2 r_v; N_z has prime factors in {2,3} cup primes(r_z) | for v = p the piece index is 2 5^B w_p; r_z = 2^E w_z and r_t = 3^A w_t carry no 5, so every gcd with a p-piece is 2 |
| Theorem K7-CELL-A final step | alpha_zv = 3 (T = W) | the same (Case A of (a2-no5) has T = W) |
| Theorem K7-CELL-B integrality | N_z = n_z m^H_z / 9 | n_z = 6 2^E w_z: m^H_z = 3 and N_z = 2^(E+1) w_z |
| Case A / Case B split | TZ (iii), CASEB | Theorem K7-A2-BRIDGE (TZ) and transferred CASEB |

Every step above uses only facts in (B1)-(B7) of Theorem K7-A2-BRIDGE (as amended), Corollary 5/6-a2 / FG-a2, and
statements of the four source files; no (a1)-only fact outside this table was found. Direct Sun instances: Sun(2),
Sun(3) (and Sun(5) inside the transferred Corollary L). Conditional chain (not a claim): together with K7-CELL section 7,
these would leave no (a2-no5) configuration; (a2-zt5) is not covered.
