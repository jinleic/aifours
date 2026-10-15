You are a hostile referee (robust control / real algebra). Do not delegate, do not browse the web,
do not modify anything. You may read only files under
/Users/jinleic/jinleic-workspace/ai4s/robust-spr-interval-synthesis/ and the PDF
/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/QuinticSPR-English.pdf.

Context: robust SPR synthesis for MONIC real interval polynomial boxes of degree n (see
work/theory.md for notation: t = w^2, E_p, O_p even/odd parts, D_E = floor(n/2), D_O = floor((n-1)/2),
pairing P_{a,b}(t) = E_b E_a + t O_b O_a, corners = four Kharitonov polynomials). A previous review
of Lemmas B, C and Propositions D, E led to the revisions now in work/theory.md.

Referee ONLY these items in work/theory.md, as stated there:
F1. Lemma F (interior reduction): if K's intervals lie strictly inside K_0's (l_i^0 < l_i <= u_i < u_i^0,
    i = 1..n), and a nonzero beta (deg <= n) is nonnegative-paired with the four corners of K_0 on
    [0, inf) and has no zeros on the imaginary axis, then beta is strictly paired with every member of K;
    if K is robustly Hurwitz it has a common SPR numerator of exact degree n.
F2. Corollary G (boundary sandwich): (a) conjecture at order n => every boundary box
    K_0 = c + lambda*(K' - c) (K' stable with positive widths, lambda* the stability radius along the
    ray) has a nonzero closed numerator; (b) if every such K_0 has a closed numerator with no
    imaginary-axis zeros, the conjecture holds at order n.
F3. Lemma H (conditional converse of Lemma B at a critical family; generalizes the quintic manuscript's
    Lemma 4.5 / Prop. 4.6 to any n under the stated extra hypotheses mu_inf = 0, full degrees,
    gcd(E_b, O_b) = 1).
F4. The revised Proposition D (sign conditions; nondegenerate fully-closed class; rank not proved).

For each item: is the proof complete and correct as written? Give the precise line and a concrete
counterexample or missing step if not. In particular check in F1 the strict-interior claim at t = 0 and
for the fixed monic coefficient, the claim that a nonzero linear form nonnegative on a rectangle is
positive at interior points, and the degree-raising step beta + eps s^n (uniformity over the box as
t -> infinity); in F2 that K inside int K' inside int K_0 really holds and that lambda* is finite and > 1;
in F3 the degree bounds, the use of coprimality, and the Q = 0 exclusion.

Output JSON matching the provided schema, one item per F1..F4 (claim, verdict, objection, fix), with
status_scoping_issues, overclaims, and best_next_step.
