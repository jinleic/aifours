# Rank-four collision slice: the private-three subgroup has a quartic V4/D8 action

MathSun8 / math-6. Actual preceding clock: **Sun Oct 25 04:13:33 PDT 2026** (`/bin/date`). **NEW WRITTEN candidate, written-only continuation after the HOLD correction.** No eval, arithmetic interpreter, enumeration, solver or replay was used for this note. Read with `resumption-hold-correction-addendum-v1.md`; prior scientific calculations remain preserved and are not retroactively admitted.

## 1. Exact boundary and improvement

This is an additive successor to `simultaneous-index-two-character-bound-v1.md`, SHA `a87846a5ecaeaa37427a0c13f6cf51276b2418429aab1b671acf8cdfa17ab9dd`. That NEW theorem is still a candidate needing separate reconstruction. Its written normalizer/fibre/character statements are the explicit hypotheses here; its finite parity checks are NOT used as proof premises or certification.

Use its notation for an actual minimum-sum P7 witness: U is the even-private vertex, N=N_G(U), Q=N/U, and E≤Q is elementary abelian of rank four. Assume every nonidentity element of E has a genuine collision, as minimum-sum requires. The predecessor's written rank-four analysis leaves exactly one beta=1 support X_e∩E, with private3|r_e and affine codimension two; no beta=2 slice support; and three or four beta=3 supports whose global sign characters restrict to rank three on E.

The new consequence is genuinely about the WHOLE quotient Q, not merely a finite necessary pattern on E:

> **Quartic-action theorem.** Let H_e≤Q be the subgroup of the actual quotient coset X_e. Then [Q:H_e]=4. There is an actual normal subgroup M of Q with [Q:M]=[M:H_e]=2 and H_e normal in M. The faithful coset action Q/core_Q(H_e) is V4 or D8; C4 and all odd-degree5/7 alternatives are excluded. Moreover M is the kernel of a precisely constrained odd combination of the beta=3 collision characters. In the four-C case that combination is a single distinguished C character, so the entire e support is globally disjoint from that C support.

This does NOT exclude either V4 or D8, supply eight original cosets, or repair any collision while preserving all sources. It sharpens the exact rank-four residual.

## 2. The full character map forces index four

Let chi:Q→F2^3 be the map given by three independent PRESENT beta=3 characters. Their restrictions to E are independent, so chi is onto and E∩ker chi is a line. Let z be its nonidentity point. All C supports miss z. The only remaining E support is X_e∩E, so z∈X_e. In particular X_e=zH_e and chi(z)=0.

Write c=[Q:H_e]. The predecessor's actual factorization gives c*beta_e≤7. Here beta_e=1 and the E intersection has index four, so c≥4. Also c divides |Q|, which divides r_i; private coprimality and3|r_e imply3∤|Q|. Therefore c is one of4,5,7.

If c were odd, the index of chi(H_e) in F2^3 would divide both c and8 and hence be one. Thus X_e would project onto ALL of F2^3. A point of X_e with all three chosen C characters equal to1 would be an ACTUAL quotient point shared by e and three C neighbours. Their genuine U-fibre pieces would give four disjoint cosets with all pairwise index gcds at most3, contradicting the classical Sun4 input. Hence c is not odd, and c=4.

This excludes the index5/7 possibilities by the full actual quotient map, not by extrapolating the finite E control.

## 3. An actual two-by-two normal chain

Put K=ker chi. The subgroup E∩H_e has rank two. Since z∈X_e and X_e avoids1, z∉H_e; therefore E∩H_e has trivial intersection with E∩K=<z>. Its image under chi has dimension two. Consequently chi(H_e) has dimension at least two. It cannot be all of F2^3, by the same four-collision contradiction, so it is EXACTLY a plane S.

Because X_e=zH_e and chi(z)=0, chi(X_e)=S as well. Set

    M=chi^-1(S)=K H_e.

Then M is normal of index two in Q. Since [Q:H_e]=4, [M:H_e]=2, so H_e is normal in M. Also z∈M\H_e and

    X_e=zH_e=M\H_e.

Thus the private-three support is globally a negative halfspace INSIDE one actual normal index-two subgroup. This is stronger than saying its E slice happens to be an affine codimension-two set.

On the original normalizer, the preimages give an actual chain

    N > pi^-1(M) > U(N∩U_e),

with both displayed indices two; the lower subgroup is normal in the middle. These are overgroups of U and of N∩U_e, NOT proved overgroups of the original U_e in G. No illegal enlargement of the e vertex is inferred.

## 4. The faithful degree-four quotient

Let L=core_Q(H_e). The action on Q/H_e is faithful after dividing by L, transitive of degree four, and has order dividing24. Because3∤|Q|, that image has order four or eight.

The image of E is elementary abelian and transitive on these four cosets: its base orbit has size [E:E∩H_e]=4. A faithful abelian transitive permutation group is regular, since an element fixing one point fixes every point. Hence the E image has order four and is V4. An image of Q of order four must therefore be V4, not C4. An order-eight subgroup of S4 is a Sylow2 subgroup, hence the usual square dihedral group D8 by elementary Sylow conjugacy. No catalogue or CFSG is used.

Therefore

    Q/L ≅ V4 or D8.

In the V4 branch H_e=L is normal in Q and the support can be described by two GLOBAL sign characters. In the D8 branch H_e/L is an order-two point stabilizer, H_e is nonnormal in Q, and M/L is its order-four normalizer. Thus M=N_Q(H_e). There are exactly two Q-conjugates of H_e. These are statements about the actual quotient subgroup, not a proof that either branch extends to P7 in G.

## 5. The odd character relation and the four-C refinement

Choose the three independent present C characters as coordinates a,b,c on F2^3. Write S=ker eta for a nonzero linear form eta on that image. The plane S must avoid the vector111: otherwise X_e would contain a point with all three C collisions. Hence eta(111)=1. Equivalently eta is an ODD sum of the selected three C characters: one of a,b,c,a+b+c. In particular

    M=ker(eta composed with chi).

When there are exactly three C supports, this leaves the single-character or triple-character alternatives, both unexcluded.

When four C supports occur, the predecessor's written character-count classification gives, after choosing a basis, the multiset

    {a,b,c,a+b}.

There are no repetitions in this rank-three/four-member case. The image points with three C negatives are101,011,111. The plane S must avoid all three, so eta must take value1 on each. Writing eta=Aa+Bb+Cc gives A+C=1, B+C=1, A+B+C=1, whence A=B=0 and C=1. Therefore eta=c, the unique displayed C character outside the three-member circuit {a,b,a+b}.

Consequently in the four-C branch the ENTIRE quotient support X_e lies in ker c and is disjoint from that distinguished C support {c=1}, not just from its E restriction. The other three C supports form the rank-two circuit and may still meet X_e with multiplicity two; together with e this is the permitted three-collision threshold, not a contradiction.

All algebra in this section is written manipulation of the indicated equations. No interpreter calculation or finite certificate was launched after the correction.

## 6. Exact first gap after this refinement

The old rank-four necessary control is compatible with the V4 branch: an actual index-four subgroup can have a normal two-by-two chain and the required odd character relation. The D8 branch supplies a second genuine quotient-action alternative, not an automatic obstruction. Neither quotient classification reconstructs the seven other subgroups U_j, their U-fibres, or a source-preserving replacement.

The sharpened remaining task is therefore: eliminate or realize the ACTUAL private-three index-four support X_e=M\H_e with Q/core(H_e) equal to V4 or D8, its specified three/four C characters and all original subgroup/fibre data. Even solving this rank-four slice would leave rank≤3 normalizer quotients and maximal/self-normalizing vertices. No full Sun8/simple-P7 theorem follows.

This successor needs a separate written reconstruction together with its predecessor. It is not covered by the old C2/C3 review, the v28-A RQLS review, a finite parity enumeration, parent acceptance or a formal/kernel gate. Novelty remains UNCLEAR.
