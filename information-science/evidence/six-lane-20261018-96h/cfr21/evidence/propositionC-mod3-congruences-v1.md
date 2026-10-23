# Proposition C (mod-3 count congruences for ternary projections) — text v1

Author ContinueCFR21; frozen 2026-10-19T00:17:02-0700. WORKER PROOF, unreviewed. Necessary properties only; no CFR(6,21) decision.

Setting. As in Theorem A: D a (Z_n,k;1)-DM with 3 | n, lambda := n/3; a_i = D_i mod 3. Only the balance of every
a_i - a_j (each value lambda times) is used, so everything below holds for any (Z_3,k;lambda) difference matrix.
For a character chi let g_chi(s) := |{c : chi(c) = s}| (s in F_3).

Proposition C. For pairwise distinct rows:
 (C3) triple chi = e_a+e_b+e_c: every g_chi(s) is divisible by 3;
 (C4) pairing chi = e_a+e_b-e_c-e_d: every g_chi(s) is congruent to -lambda (mod 3);
 (C5) chi = e_a+e_b+e_c+e_d-e_e: every g_chi(s) is congruent to lambda (mod 3).
For CFR(6,21) (lambda = 7): triple counts are multiples of 3; each pairing has counts in
{(17,2,2),(14,5,2),(11,8,2),(11,5,5),(8,8,5)} (never balanced); each (4,1)-character has counts all = 1 (mod 3).

Proof (plane counting). For f, g : C -> F_3 put N(u,v) = |{c : (f,g)(c) = (u,v)}|. Expanding in characters of F_3^2
(or by the parent's incidence identity), if f and g are balanced then
 N(u,v) = n/9 + (1/9)[(3 g_{f+g}(u+v) - n) + (3 g_{f-g}(u-v) - n)]  ... (*)
where for any function h, (1/9)·sum over the two nonzero multiples x of h of omega^(-x h(·)) contributions equals
(3 g_h(value) - n)/9. If moreover a third balanced or known line is present it is added in the same way.
 (C3) f = a_b - a_a, g = a_c - a_a: f - g is balanced, so N(u,v) = g_{f+g}(u+v)/3 with f+g = a_a+a_b+a_c; integrality.
 (C4) f = a_a - a_c, g = a_b - a_d (both balanced): f+g = chi1 = e_a+e_b-e_c-e_d, f-g = chi3 = e_a+e_d-e_b-e_c, and
   (*) gives N(u,v) = (g_1(u+v) + g_3(u-v) - lambda)/3. Since (u,v) -> (u+v, u-v) is bijective on F_3^2,
   g_1(s) + g_3(t) = lambda (mod 3) for all s, t; hence g_1 and g_3 are constant mod 3 with residues r_1 + r_3 = lambda.
   The planes <e_a-e_b, e_c-e_d> and <e_a-e_d, e_b-e_c> give r_2 + r_3 = r_1 + r_2 = lambda for the third pairing,
   so r_1 = r_2 = r_3 = r with 2r = lambda, r = -lambda (mod 3).
 (C5) f = a_a+a_b+a_c (counts divisible by 3 by C3, after subtracting a constant multiple of... — used only as a
   known line), g = a_d - a_e (balanced): f+g and f-g are the (4,1)-characters with negative rows e and d, and the
   analogue of (*) with the extra known line f gives g_f(u) + g_{f+g}(u+v) + g_{f-g}(u-v) = 2 lambda (mod 3);
   with g_f = 0 (mod 3) the two residues add to 2 lambda; letting the negative row range over the five rows forces
   one common residue r with 2r = 2 lambda, r = lambda (mod 3). ∎
Relation to Theorem A: a constant pairing or (4,1)-character would have counts (n,0,0), all = 0 (mod 3), contradicting
C4/C5 when 3 ∤ lambda; this re-derives the support-4 and support-5 cases of Theorem A.

Checks: probe p8-z9-types-pairing-v1 (source 9aec7f5d…, stdout 9b81dc4b…): on the 96 P21 DM6 there are 0
violations of C3/C4/C5 over 1920 triples, 4320 pairings and 2880 (4,1)-characters; observed pairing types
(8,8,5), (11,5,5), (11,8,2); (4,1) types (10,7,4), (7,7,7); triple types (9,6,6), (9,9,3), (12,6,3).
Priority: these are J-characteristic-type congruences for 3-level orthogonal arrays of strength 2; likely known in
the nonregular-design literature; no novelty claim.
