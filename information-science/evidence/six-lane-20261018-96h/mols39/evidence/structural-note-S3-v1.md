# Structural note S3 — orbit-type coverage of the frozen orbit models (2026-10-19T03:47:34-0700, ContinueCFR21)

Status: worker proofs, UNREVIEWED; scope notes for any future W2 claim. Notation as in S2. Models in
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/models/*_orb.json fix ONE list of orbit types; a SAT/UNSAT result for such a CNF only speaks for that list.

## z39_g6 = <s, z>, s = (16,(012)(345)), z = (-1,id), row 6 the zero row
(a) z fixes all rows and gcd(-2,39) = 1, so by S2 (i) exactly one column is fixed by z: the all-zero column. Hence the
    zero column is present (no gauge needed) and it is the only G-fixed column.
(b) G6 is cyclic of order 6 with unique involution z, so no column has a stabiliser of order 2 or 6 except the zero
    column; nonzero columns lie in orbits of size 2 (stabiliser <s>) or 6. Write c for the number of size-2 orbits.
(c) Columns fixed by s have the form (u,16u,256u,v,16v,256v,0); their (0,1)-differences -15u lie in 3Z39 and must be
    distinct and nonzero (the zero column already uses 0), so 2c <= 12. With 38 = 2c + 6a, c = 1 mod 3, so c in {1,4}.
(d) z39_g6_orb encodes only c = 1 (types zero, fix3 x1, gen x6). The case c = 4 (zero, fix3 x4, gen x5) is NOT covered.
    The same holds for the six-row model z39_g6six_orb (no zero row; the (0,1)-difference argument is unchanged).
## z39_z6p = <s, t>, t = (1,(03)(14)(25))
(e) t-fixed columns have zero (0,3)-difference; with the gauge below the zero column is present, so t fixes no other
    column; G-fixed columns are t- and s-fixed. 39 is odd and all other orbit sizes (2, 6) are even, so there is exactly
    one G-fixed column (u,16u,256u,u,16u,256u,0); the row translation (u',16u',256u',u',16u',256u',0) with u' = -u keeps
    the action untwisted and moves it to the zero column (gauge). Size-2 orbits: pairs {(u,v),(v,u)} of s-fixed columns,
    u != v; as in (c), c in {1,4}. z39_z6p_orb encodes only c = 1.
## z39_g3 = <s>
(f) No involution, so the zero column is not forced. Orbits have size 1 (s-fixed) or 3. The s-fixed columns
    (u,16u,256u,v,16v,256v,0) need pairwise distinct (0,1)-differences -15u, i.e. u distinct mod 13, so f <= 13 fixed
    columns; 39 = f + 3g gives f in {0,3,6,9,12}. z39_g3_f0_orb (f = 0) and z39_g3_f3_orb (f = 3) cover two of the five
    cases; f = 6, 9, 12 are NOT covered.
## z39_m1 / z35_m1 = <(1,(12)(34)(56))>, row 0 the zero row
(g) Fixed columns have zero (1,2)-difference, so at most one; n odd forces exactly one, (0,p,p,q,q,w,w); the row
    translation (0,-p,-p,-q,-q,-w,-w) keeps the action untwisted and makes it the zero column. Types zero + gen x (n-1)/2
    are therefore complete for this group.
Consequence: an UNSAT (or UNKNOWN) for z39_g6_orb / z39_z6p_orb / z39_g3_f* would leave the uncovered orbit types open;
any W2 request must list per-type CNFs or state the restricted scope.
