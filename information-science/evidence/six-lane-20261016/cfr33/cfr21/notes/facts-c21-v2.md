# Facts c21-v2: the Frobenius single-orbit family (worker InfoCFR27Lift; written 2026-10-17 19:05 PDT, before the assay)

## D1 Reduction for one regular column orbit of the untwisted Frobenius group [written derivation; calibrated by
## code/frob21_orbit_c21v1.c selftest and by full direct checks of every passing vector]
Rows of the DM are indexed by Z_7. For mu in Z_21^* with mu^3 = 1 (mu in {1, 4, 16}) let
G_mu = { g_{s,t} = (mu^t, pi_{s,t}) : s in Z_7, t in Z_3 }, pi_{s,t}(x) = 2^t x + s (2 has order 3 mod 7).
Composition (mu^t1, pi_{s1,t1}) (mu^t2, pi_{s2,t2}) = (mu^(t1+t2), pi_{2^t1 s2 + s1, t1+t2}), so G_mu is a group of order 21
(the Frobenius group C7 x| C3). Action on columns (as everywhere in this lane): (g c)_x = mu_g c_{pi_g^-1(x)}, columns
modulo constants; pi_{s,t}^-1(x) = 2^-t (x - s) with 2^-1 = 4, 2^-2 = 2 (mod 7).
Single orbit: the columns are g v (g in G_mu) for one base column v in Z_21^7; WLOG v_0 = 0.
For rows a != b, d = b - a: the 21 differences (g_{s,t} v)_a - (g_{s,t} v)_b = mu^t (v_y - v_{y + 2^-t d}) with
y = 2^-t (a - s); for fixed t, y runs over Z_7 as s does. Hence the pair (a, b) is good iff
T(d) := { mu^t (v_y - v_{y + 2^-t d}) : t in Z_3, y in Z_7 } has 21 distinct elements.
T(2d) = mu T(d) (substitute t = t' + 1; exponents mod 3 since mu^3 = 1 and 2^3 = 1 mod 7) and T(-d) = -T(d) (substitute
y = y' - 2^-t d). The orbits of <2, -1> on Z_7 \ {0} are all of it, so the column set is a (Z_21, 7; 1)-DM iff
T(1) = { v_y - v_{y+1} } u { mu (v_y - v_{y+4}) } u { mu^2 (v_y - v_{y+2}) } (y in Z_7) has 21 distinct elements.
Then the 21 columns are pairwise distinct (their (0,1)-differences are), so the orbit is regular.
The scout lead "{v[j+1]-v[j]} u {4(v[j+4]-v[j])} u {16(v[j+2]-v[j])} enumerates Z_21" is -T(1) for mu = 4, i.e. the same
condition (negation is a bijection). For mu = 16: T(1) = {v_y - v_{y+1}} u {16(v_y - v_{y+4})} u {4(v_y - v_{y+2})}.
Relation to the enumerated classes (specs/groups-v1/n21-k7-ord2to84.jsonl): g49 = <(1, x+1), (4, 2x)> is G_4 in the
same labelling; g50 = <(1, x+1), (4, 4x)> = <(1, x+1), (16, 2x)> = G_16 ((4, 4x)^2 = (16, 16x) = (16, 2x)); g36 is the
mu = 1 Frobenius group in another row labelling (every transitive C7 x| C3 in S_7 normalises its Sylow 7-subgroup and is
the index-2 subgroup of that AGL(1,7), hence all are conjugate). The xc runs on g49, g50, g36 (all orbit structures,
modes zero and nozero) therefore contain the single-orbit family as the case "one option covers every item".
Expected size [HEURISTIC only]: 21^6 candidate v per mu, each passing with probability ~21!/21^21 ~ 8.8e-9 if T(1) behaved
randomly, i.e. ~0.75 passing v per mu (passing v come in families of at least 21, one per column of a DM).

Time correction (appended 2026-10-17 19:03:51 PDT): the header time "19:05 PDT" was typed before reading the clock; the file was written just before 19:03:42 PDT (clock read immediately after). See notes/deviations-c21.log C21-D2.

## P1 The per-row model K = <8> admits at most one f-row [written proof, 2026-10-17 19:06:37 PDT]
Let f be an <8>-equivariant normalised orthomorphism of Z_21 (f(8x) = 8 f(x), f and f - id bijective). Fix(8) = 3Z_21,
and an <8>-equivariant bijection maps fixed points to fixed points, so f(3Z_21) = 3Z_21 and f maps the 14 elements
x not in 3Z_21 among themselves; the same holds for f - id. For x not in 3Z_21 write f(x) = e x (mod 3) with e in {1, 2}
(f(x) is a unit mod 3); f(8x) = 8 f(x) = 2 e x = e (8x) (mod 3), so e is constant on the orbit {x, 8x}. If e = 1 then
(f - id)(x) = 0 (mod 3) lies in 3Z_21, impossible because f - id maps non-multiples of 3 to non-multiples of 3. Hence
f(x) = -x (mod 3) for every x not in 3Z_21. For two such maps f, g and x not in 3Z_21: (f - g)(x) = 0 (mod 3), so f - g
maps the 14 non-multiples of 3 into 3Z_21 and is not a bijection. Therefore no two f-rows of a <8>-model normal form
can coexist: the model is empty for every k >= 4 (in particular for CFR(6,21)). This agrees with bin/keq_clique_c21v1
(runs/B1/keq-n21-kk7-K8-reps-first.out: 2,527 maps, 108 R1-orbit representatives, L2 empty for every one of them).


## G2 Fixed-row pure permutations (worker-written proof, recorded 2026-10-17 19:19:26 PDT; NOT used as an unreviewed search cut)
Suppose a (Z_n,k;1)-DM column set is invariant under s=(1,pi), pi!=id and pi fixes row r. Normalise every column at
row r. Choose a moved row a. The map C -> c_a is bijective (difference from row r), so s(C)=C iff
c_a=c_(pi^-1(a)): this equation occurs in exactly one column by the DM property on the distinct rows a,pi^-1(a).
Thus s fixes exactly one column D. The same reasoning applies to every nonidentity power of pi, and its unique
fixed column must be D, which was already s-fixed. Hence no other column has an orbit of proper length dividing
m=ord(pi): all n-1 other columns have orbit length m. Necessarily m divides n-1.
For n21 the pure row-permutation models g01 (order3, cycle3.3.1) and g02 (order6, cycle6.1) fail this necessary
condition. This uses multiplier EXACTLY1; it does not exclude the g06 multiplier4 order3 model. Positive controls:
P21's pure5-cycle divides20, Sage55's pure6-cycle divides54, and the n13 pure6-cycle divides12.
The production g01 zero result is instead checked by the independently enumerated option sizes plus arithmetic
reachability; g01 nozero has an uncovered item; g02 was already exhausted by the orbit solver.
