# Exact reduction R1 — the mod-13 ("beta-index-3") extension route for the anchor (2026-10-19T04:28:46-0700, ContinueCFR21)

Status: worker proof, UNREVIEWED; one computational input (Lemma U below) is a single-producer exact computation
(S4a); an independently authored second route is being prepared. No search was run for this note.
Context: parent message of 2026-10-19 ~04:2x proposing to extend only beta = D mod 13 of the anchor by a seventh
beta-row (each old-new difference taking every residue of Z_13 exactly 3 times) and to solve the mod-3 lift for all
seven rows afresh, as a route strictly wider than the fixed-anchor extension.

## Setting
D = exact anchor (Sage DM_39_6_1, raw sha256 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a), rows 0..5, columns C (|C| = 39).
Z_39 = Z_3 x Z_13 (CRT); for a function X : C -> Z_39 write X = (X mod 3, X mod 13).
Normalise at row 0: D'_x = D_x - D_0, beta_x = D'_x mod 13, alpha_x = D'_x mod 3 (x = 0..5; beta_0 = alpha_0 = 0).
V(beta) and "rainbow" as in structural-note-S4-v1.md (49926433...): A in F_3^(rows x C) with A_0 = 0 is a lift of beta iff
for every pair x < y and t in Z_13 the fibre T_xy(t) = {c : beta_x(c) - beta_y(c) = t} (3 columns) carries 3 distinct
values of A_x - A_y; then CRT(A, beta) is a (Z_39,6;1)-DM, and every 6-row DM with skeleton beta arises so.

## Lemma U (computational; S4a, probe code/probe_mod3_lift_v1.py 53583125..., run S4a-six-row-3n, stdout
## sha256 recorded in S4): for the anchor's beta, dim V(beta) = 10, the fibre-functional map F on V has rank 5,
## so ker F = the 5-dimensional space of row constants, and exactly 2 of the 3^5 classes of V / ker F are rainbow.
Hence the rainbow lifts are exactly {eps * alpha + e : eps = ±1, e a row-constant vector} (486 lifts).
(alpha itself is rainbow, so is -alpha; they are different classes since alpha is not constant.)

## Proposition R1
Let D* be any (Z_39,7;1)-DM with rows 0..6 whose rows 0..5 reduce mod 13 (after normalising at row 0 and some
labelling of its columns by C) to beta. Put mu = 1 if eps = 1 and mu = 14 if eps = -1 (14 = -1 mod 3, 14 = 1 mod 13).
Then f := mu^(-1) (D*_6 - D*_0 + g) for a suitable column function g with g = 0 mod 13 satisfies: [D; f] is a
(Z_39,7;1)-DM. Conversely every one-row extension [D; f] is an instance of the beta route (beta_6 = f mod 13).
Proof. Normalise D* at its row 0: D*'_x = D*_x - D*_0 (still a DM). Its rows 0..5 are a 6-row DM with skeleton beta,
so by Lemma U their mod-3 part is eps*alpha + e for one sign eps and constants e_x (x = 1..5). Multiplication by the
unit mu^(-1) (mu^(-1) = mu) maps rows 0..5 to (alpha + eps*e, beta) mod (3,13), i.e. to D' + r with r_x in 13Z_39
constant on each row, and keeps the DM property. Adding a constant to a whole row does not change whether
c -> X_x(c) - Y(c) is a bijection, so [D' ; mu^(-1) D*'_6] is a DM, and [D; mu^(-1) D*'_6 + D_0] is a DM because the
column translation by D_0 (added to every row) preserves all differences. Take g accordingly. ∎
## Consequences
1. For this anchor the beta route is NOT wider than the fixed-anchor one-row extension in free mode: it is the same
   question up to the equivalences (unit 14, row constants, column translations). Its status is that of v1 T2 / v2 T6:
   UNKNOWN (incomplete at the 270-282 s budgets). The equivariant G6/C3 (two producers) and C2 (one producer)
   COMPLETE negatives are unaffected and are special cases.
2. The beta-first search order (decide beta_6 in Z_13^39 by a demand exact cover: 78 items (x,t) with demand 3,
   39 column items, 39*13 = 507 options; then solve the mod-3 lift of row 6) explores a strictly looser relaxation
   of the joint Z_39 exact cover used by v2 free0 (items (x,v), v in Z_39, demand 1). [HEURISTIC, not evidence:
   ~13^39 * (39!/(6^13 13^39))^6 ~ 1 beta-solutions expected, but ~1e23 capacity-feasible partial assignments at depth
   26; joint-cover pruning is much stronger.] So for this anchor a beta-first engine is not expected to be a faster
   engine for the same question; only a stdlib option-statistics probe could quantify this.
3. Where the beta route is genuinely wider: skeletons whose 6-row lift space has more than one rainbow sign-class
   (S4: Singer-type (57,8;1) and its 7-row restriction have 4 rainbow classes = 2 sign pairs). For the anchor
   (and, by S4, Sage DM21/DM33/DM51 and P21: exactly 2 classes) it is not.
4. Positive-control route if a beta engine were ever built: Singer-type DM over Z_57 (mod-19 skeleton, index 3),
   delete one or two rows, re-find the deleted beta-row(s) and re-lift — controls for the engine only, not target
   evidence.
Scope: exact anchor only; no statement about other DM6(39), CFR(6,39) or six MOLS(39).
