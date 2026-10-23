# Erratum 1 to theoremA-mod3-rank-v1.md (sha 10e9b724b40b2a6d1f81827cf82f4cabf7d1e14d8b113cbe9fa15291ac969094)

Frozen 2026-10-18T23:59:47-0700 by ContinueCFR21 after parent reading. The original file is unchanged; this erratum corrects
three statements. The theorem, its proof (Steps 0-3) and Corollaries A1/A2 are unchanged.

E1 (point form, original lines 25-26). Without a normalisation the column points are only defined modulo the common
column offset, so the correct unnormalised point form is
    a_i(c) = g_c + <lambda_i, y_c> + s_i      (g_c in F_3 an arbitrary per-column offset, s_i a per-row offset),
equivalently: first replace a_i by a_i - a_{i_0} (allowed by the invariance paragraph, which shows K and r are
unchanged), and then a_i(c) - a_{i_0}(c) = <lambda_i - lambda_{i_0}, y_c> + s_i'. For chi with sum chi_i = 0 the
offset g_c cancels: chi(c) = <sum_i chi_i lambda_i, y_c> + sum_i chi_i s_i, so K = {chi : sum chi_i = 0,
sum chi_i lambda_i = 0} exactly as stated, and every consequence of the point form (cap, no parallelogram, no 4+1
relation) stands.

E2 (strata wording, original line 76 vs line 67). The 96 P21 DMs have k = 6 rows and mod-3 affine rank 5, which is
FULL rank for six rows (the maximum k - 1 = 5); they do not lie in a seven-row stratum. Corrected sentence: "It does
not exclude the generic seven-row stratum r = 6 (no seven-row DM is known; the 96 known six-row Z_21 DMs are of full
rank 5 for k = 6) and gives no nonexistence."

E3 (shape counts, original line 62 vs line 23). The five support-6/7 shapes tested in part 3 of probe p4 are sorted
coefficient multisets BEFORE the global-sign quotient: (0,1^6), (0,2^6), (0,1^3,2^3), (1^5,2^2), (1^2,2^5).
Up to global sign and row relabelling they are the three shapes listed in Corollary A1 (1^6 ~ 2^6; 1^3 2^3 self-
paired; 1^5 2^2 ~ 1^2 2^5). Both counts are correct under their respective conventions.
