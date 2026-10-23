# KII-W parent erratum v1

Recorded 2026-10-19T17:52:52-0700 (`/bin/date`). Applies to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/kii-written/KII-W-v1.md` SHA256 `b25d4274d09b24b7eaa346d5287af95cee65f99ae4939c4bd32f20eda2eb5c03`; original immutable. Resolves Codex3 MINOR and Claude5 MINOR findings (overlap counted per review, not as eight unique defects). No theorem or weighting changes.

1. SHAPE LF38 begins “For a given pairwise-disjoint coset configuration as in section0, its labelled index tuple has all pairwise gcds<=6 and a=2 iff …”. LF53 says “the given configuration is a CE with a=2”, not that numerical data imply realizability. At LF51 note gcd(r_y,r_c)<=2 is1 because r_y is odd. R0 first reduces arbitrary G to finite G.
2. The Sun(2) justification at LF43–44 is the argument of LF86–88 with U_v replaced by G, finite after R0; it does not depend on SHAPE or KII exclusion.
3. LF95: **six** other vertices, consisting of x,y and four C-neighbours. LF130 and LF167 concern the **four C-entries** Phi_cq, q in C minus{c}; LemmaB's unequal entry must be a C-entry, not the always1 x-entry. LF164/packageLF19 reads “every permitted multiplier assignment”, not “both values of every multiplier”.
4. Fibre counts t_j, distinguished marker t, core N, plain count N, intersection index I_ij and local label I are distinct notation. Use m_j for fibre counts and N_pl for the MainLemma plain count if ambiguity arises.
5. “Compatible” means local-index gcd>=2. M2 sets containing y lie in{x,y}. M4c gives y weight0, so{x,y,i*} weighs at most1; zero-weight additions cannot cure a forbidden subset of positive-weight vertices.
