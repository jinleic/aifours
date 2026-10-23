# k62-followon: frozen setting and import boundary (written first)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:35:57-0700.
- **Owner:** Sun63Successor, under the parent's follow-on instruction (IRC from Main after the K63-RES review launch):
  examine whether the granularity mechanism of `../K63-RES-v1.md` applies to the remaining K6.2* classes. New files
  only in this directory, exclusive creates; everything else read-only. No computation (no GO held or requested).
  K7 is owned by Sun7K62Successor and is out of scope here.

## Exact setting (class K6.2*, old README section 5 with P0/P1, as in the accepted `K62-A-v1.md` section 1)
V = C disjoint-union {d}, C = {i*} disjoint-union O, |O| = 5, with
- n_d = 2^(e_d) 5^(h_d) w_d, f_d = 0, e_d >= 2;
- n_(i*) = 2^(e*) 3^(f*) 5^(h*) w_*, e* >= 2, f* >= 1;
- n_c = 2 * 3^(f_c) 5^(h_c) w_c for c in O (e_c = 1, f_c >= 1);
- min(e_d, e*) = 2; at most one vertex has f >= 2; at most one vertex has h >= 1; the w's are pairwise coprime and
  coprime to 30;
- gcds: 6 inside C, 4 for d-i*, 2 for d-c (c in O). Hence alpha_dc = alpha*_dc = 1 (c in O),
  alpha_(d i*), alpha*_(d i*) in {1, 2, 3} with sum <= 4, and C-C entries in {1, ..., 5}.

**Remaining residues** (the accepted K62-A excludes e_d = 2 with the 3-marker absent or on i*):
- **(R1)** e_d >= 3 (hence e* = 2); the 3-marker on i*, on a vertex t of O, or absent; the 5-marker anywhere.
- **(R2)** e_d = 2, the 3-marker on a vertex t of O (f_t >= 2); e* >= 2 arbitrary; the 5-marker anywhere.
Write t for the 3-marked vertex of O and p for the 5-marked vertex of O, when they exist (t = p is allowed).
A vertex v of O is *unmarked* if f_v = 1 and h_v = 0, i.e. n_v = 6 w_v; at least three exist.

## Import boundary
- **Accepted imports:** R0; class definition with P0/P1; L0.3 (identity and 1 <= alpha <= g - 1); LFC (a)-(d);
  INV (a)-(b); VFC (V1)-(V4) with the VFC-count argument; TG in its general computational form
  (verdict sha256 c792dc68884a0c99632f218fd03833f60b80b89fd2c194137331d35fb4f3fc61); K62-A (same verdict);
  L1 (T rule) of rules-k7-v1 if used; Sun(t), t <= 6, only through LFC (c)/VFC (V3).
- **Candidate, NOT an import:** `../K63-RES-v1.md` (sha256 1542a551f6d9787784a2434d18a5aa7275f673b23aab4901a384518206f67515)
  + `../K63-RES-erratum-v1.md` (sha256 e70a5518a74ee4230d442a1b81d562d65b683ab6fcb904ff306792ea0ac3b49b), under parent
  CLI review. Its Lemma FG is proved there only for the K6.3 residue. Anything used here is re-proved in this
  directory for the K6.2* setting and labelled as a new candidate.
