# Erratum 2 to theoremA-mod3-rank-v1.md (sha 10e9b724b40b2a6d1f81827cf82f4cabf7d1e14d8b113cbe9fa15291ac969094)

Frozen 2026-10-19T00:20:37-0700 by ContinueCFR21. Disposes the two hostile reviews of the exact v1 bytes
(Codex note NEW RUN/review/cfr21-mod3-rank-codex-v1.prompt.stdout.txt: ACCEPT-WITH-FIXES, 0 FATAL;
Claude note NEW RUN/review/cfr21-mod3-rank-claude-v1.prompt.note.md: ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR) together with
erratum 1 (7f92e7c303d928297ab6255c43ee5d7e7b9fe4a38f31f9b18fa65dec73b83e66). No statement of Theorem A, Corollary A1
or Corollary A2 changes; v1 and erratum 1 stay unchanged.

E4 (point form; Codex MAJOR = erratum-1 E1, Claude m1). The correct unnormalised form is
  a_i(c) = h(c) + <lambda_i, y_c> + s_i  with an arbitrary column function h (e.g. h = a_{i0}), the y_c affinely
spanning F_3^r. Then chi(c) = <sum_i chi_i lambda_i, y_c> + const for sum chi_i = 0, hence EXACTLY
  K = {chi : sum chi_i = 0, sum chi_i lambda_i = 0}  (equality, not "isomorphic").
The lambda_i are pairwise distinct (a coincidence lambda_a = lambda_b is the excluded support-2 character e_a - e_b).

E5 (distinct indices; Codex minor a). In the point-form consequences "cap (no three collinear), no parallelogram
lambda_a + lambda_b = lambda_c + lambda_d, no relation lambda_a + lambda_b + lambda_c + lambda_d = lambda_e" the indices
are pairwise distinct (otherwise e.g. lambda_a + lambda_a + lambda_a + lambda_e = lambda_e holds trivially in
characteristic 3).

E6 (machine-check wording; Codex minor b, Claude m6). Replace "(so 3-dim uniformity cannot exclude r = 5)" by
"(i.e. no 3-dimensional certificate of the searched root-mod-<chi> form exists for these shapes; this does not exclude
other arguments)". Moreover the 3-dim search is implied by the 2-dim one: any 2-dim subspace of such a W would already
be a 2-dim witness.

E7 (scope of relations; Claude m3). "Construction in which some <= 5 rows satisfy a mod-3 affine relation" means
precisely: a relation sum_i chi_i a_i(c) = const for all columns with sum_i chi_i = 0 and 1 <= |supp chi| <= 5.
Relations with nonzero coefficient sum are NOT excluded in general (a column offset can create e.g. a_a + a_b = 0).

E8 (CFR coordinates; Claude m4, Codex minor). The rank statement refers to the 7-row DM {0, tau_1, ..., tau_6} where
tau_r = sigma_r^{-1} maps symbols to positions in the CFR row sigma_r (columns indexed by symbols); conversely
subtracting a row turns any (Z_n,7;1)-DM into a zero row plus six bijections forming a CFR. It does not refer to the six
tau-rows alone (there r <= 5, and r >= 4 by Corollary A2) nor to the positional array sigma (not a DM in general).
CFR-coordinate restatement: there is no relation sum_r beta_r tau_r = const (mod 3) with |supp beta| <= 5 and
sum_r beta_r = 0, and none with |supp beta| <= 4 and sum_r beta_r != 0 (the zero row absorbs -sum beta_r);
e.g. tau_a + tau_b = const (mod 3) is impossible.

E9 (rank wording refinement; Claude m2, refines erratum-1 E2). The 96 known DM6 have full rank r = 5. Any 7-row
extension of one of them has K ∩ {chi : chi_new = 0} = 0, so every nonzero chi in K involves the new row; both r = 5
and r = 6 remain open for such extensions, and the generic seven-row stratum r = 6 is untouched.

E10 (priority wording; Claude m5). Replace the Evans sentence by: "Evans (2013, Thm 4) concerns the literal linear rows
{0, x, 2x} and holds whenever 3 is the smallest prime divisor with cyclic Sylow 3-subgroup (including 9 | n); L3 covers
arbitrary rows whose mod-3 images sum to a constant but needs 9 ∤ n. The two results overlap and neither contains the
other." (Claude also notes maximality of {0, x, 2x} for every odd n with 3 | n by a second-moment argument.)
No priority claim is made before the parent's primary screen.

E11 (nits; Claude m6). Corollary A1's shapes read e_a+…+e_f (six distinct rows), e_a+e_b+e_c−e_d−e_e−e_f,
e_a+…+e_e−e_f−e_g. Corollary A1 assumes 3 | n, 9 ∤ n and holds for every such n (not only n = 21). Corollary A2 for
k = 4, 5 follows because support >= 6 > k forces K = 0; for k = 6, r = 4 iff K = <chi> with chi of full support
(mu in {0,3,6}). The Step-3 count gives dim K <= 1 for every 4 <= k <= 7.

Independent confirmations recorded by the reviewers: Codex and Claude re-derived Steps 0-3 by hand; Claude proved the
32,760 seven-cap count and the "exactly one missed direction" property by a counting argument; the parent gave an
incidence proof of Step 1.
