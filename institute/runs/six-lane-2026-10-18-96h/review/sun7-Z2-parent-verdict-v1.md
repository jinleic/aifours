# Sun k7: a 2-marker with no 3-marker is excluded

Recorded at 2026-10-19T01:00:07-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Theorem K7-Z2 excludes every class-K7 configuration with a vertex of 2-valuation at least 2 and no vertex of 3-valuation at least 2. A 5-marker may occur at the centre or elsewhere; all excess valuations are unbounded. The conclusion holds for arbitrary groups with finite-index subgroups through the accepted finite-core quotient.

This is not Sun(7). Combined with K7-M0 and K7-M1, the remaining K7 configurations have both a 2-marker and a 3-marker, or have no 2-marker with the 3- and 5-markers on different vertices. K6.2* and marked K6.3 remain separately open.

## Frozen text and reviews

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-Z2-v1.md), SHA256 `cda7573de2401c220493d55e37fdc09b3292590522fc0258ba9a5ca6e27ecbe7`.
- [Mandatory erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-Z2-erratum-v1.md), SHA256 `3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9`.
- [Codex review](sun7-z2-codex-v1.prompt.stdout.txt): ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 1 MINOR; observed model gpt-6.1-sol.
- [Claude review](sun7-z2-claude-v1.prompt.note.md): ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 10 MINOR; observed model claude-opus-5-5.

The parent read the candidate, both reports and the erratum completely. Neither report establishes novelty or human peer review.

## Independent parent derivation

At the 2-marked centre z, all neighbour cofactors are odd and 3-free, and at most one carries a 5-marker. LFC depends on neighbour labels, not the apex's own cofactor. Thus ROW-U applies directly when all neighbours are unmarked; otherwise the explicitly stated ROW-1-deg transfer applies. The threes are excluded by adding a weight on the 5-marked neighbour to the five-neighbour value 5. An all-five row is excluded by applying LFC to the inverse row of ones. Both alpha rows at z therefore lie in {1,2,4}, contain at most one 1, and have at least three 4s. INV makes the two sets of 4-neighbours complementary triples F and F*.

For a cross pair a in F*, b in F, the triangle has values (s,4,x), with s in {1,2}. Direct evaluation of the accepted T bounds gives tau_min = lcm(4,x/gcd(x,r_z)) and tau_max = min(sx,4 min(s,x),s min(4,x)). Values x=1,3 are impossible. A possible x=5 forces inverse x*=1, also impossible. Hence (x,x*) is one of (2,2),(2,4),(4,2). If s=1, x=4. For surviving values, tau_min=4; F7 gives X_a subset X_b exactly in the needed cases xs<=4. The inverse containment has the reversed roles, with no apex error.

The true VFC vector is q=alpha*. On tight centre edges alpha+alpha*=6, D_v=Y_v by equality of finite measures. Since neighbour cofactors are odd and 3-free, the VFC local gcds reduce to those of the values 1,2,4. Two light indices and one heavy index cannot share a right coset by Sun(3); a local index labelled 1 is coprime to every other and must stand alone by Sun(2). Their total union avoids U_z and has measure strictly below 1.

The possible ones in the two centre rows give four exhaustive types. If both exist, CROSS forces (4,4), impossible. If exactly one exists, F7 and tightness place its nonempty D-set inside a heavy D-set despite coprime local indices, impossible; inversion handles the other orientation. If no ones exist, every light vertex having an incident cross-2 edge has a D-set disjoint from every other light D-set. At most one remaining light vertex would make three sets of measure 1/3 pairwise disjoint, contradicting the strict union bound. Thus both orientations have an out vertex; their crossing edge is 4 in both alpha matrices, again impossible.

## Findings and verification boundary

Erratum G1–G10 disposes all findings: the accepted M1 overlay is cited; the marked-apex transfer and its weights are explicit; the inverse involution is stated; R0/LFC/VFC/F7 imports are complete; inherited row arguments correctly retain Sun(t) for t<=6 (only the additional LIGHT applications use Sun(2)/Sun(3)); triangle notation and tau=4 scope are fixed; odd neighbour cofactors and right-coset intersections are stated; inversion of T2 is explicit; probe remarks remain bounded observations.

The proof is written and uses no computed leaf census, LP optimum or exploratory search as a premise. It inherits the accepted Sun(5)/Sun(6) imports and the general T/VFC/F7 rules. No Lean, human review, novelty clearance or full-target gate is claimed.
