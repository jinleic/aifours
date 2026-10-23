This is partial progress. All results proved below are rigorous; the final coverage assertion for arbitrary words in Res remains unproved.

1. Polynomial duality, including selections with point zero.

For a block B, let S(B) denote the points (val(T),|T|/2) of its nonempty selections having even size and an even number of reflections. A nonempty selection with point zero is retained in S(B). It already supplies the witness 1-[0]=0, with the two terms indexed by different selections.

For every integer D≥1, B admits a witness in J^D with empty-selection coefficient 1 if and only if every polynomial g(v,h) of total degree less than D that vanishes on S(B) also satisfies g(0,0)=0.

Indeed, the coefficient of s^i t^j in [v,h] is binom(v,i)binom(h,j), for 0≤i,j<p. Membership in J^D requires the coefficients with i+j<D to vanish. Finite-dimensional linear duality gives the assertion for the span of these binomial functions. This span is exactly the space of polynomial functions representable with total degree less than D: binomial and monomial bases are triangular, and exponents at least p can be reduced using v^p=v and h^p=h without increasing degree. This argument also applies when D>p.

We use two consequences. First, the triangular level criterion in proof-T0.md remains valid for D=p as well: if level h contains at least D+1-h distinct values for every integer h=1,...,D, with coordinates reduced modulo p, then B has depth D. To prove this, a polynomial of degree at most D-1 vanishing on the options is successively divisible by h-1,...,h-D. These D height residues are distinct, including when D=p.

Second, for a six-letter block with admissible whole selection, either of the following suffices for depth 3: at least three values at height 1 and two at height 2, or at least two values at height 1 and three at height 2. For the second version, divide a vanishing quadratic first by h-2 and then by h-1; the height-3 point kills the remaining constant. These arguments work at p=3, where height 3 is zero.

2. Exact four-letter criteria.

Write C=a-b and S=x+z. For each mixed four-letter block containing two rotations and two reflections, the height-1 values are C and S. If C≠S, an affine polynomial vanishing on both height-1 points is a multiple of h-1, and the whole-selection point at height 2 forces that multiple to be zero.

If C=S, the two nonempty option points are (C,1) and (V,2). Fullness is equivalent to V=2C: otherwise the line through these two points avoids the origin and is a separating polynomial.

The whole-selection values are C-S for FRRF, x+C-z for RFRF, C-x+z for FRFR, and S+C for RFFR. Substitution gives precisely the criteria in proved_lemmas. The shapes RRRR, FFFF, RRFF and FFRR are concatenations of two same-type pairs and are always full.

Every three-letter block is full to depth 1: choose any two letters of the same type and use 1-[(their product value,1)].

3. Exact criterion for a constant-rotation bracket, at every allowed length.

Let U=σ_a ρ_x^n σ_b, put C=a-b, m=floor(n/2), and assume 0≤m≤p-1. Its desired depth is D=m+1. An admissible selection either uses neither endpoint and 2j rotations, or both endpoints and 2j rotations. Consequently the nonempty option set is

  (2xh,h),                 1≤h≤m,
  (C-2x(h-1),h),           1≤h≤m+1.

This is the same set for n=2m and n=2m+1. The case m=0 is immediate.

Suppose first that x≠0. Let g have degree at most m and vanish on these points. The second family consists of m+1 distinct points on the line

  L(v,h)=v+2xh-(C+2x)=0.

The restriction of g to this line has degree at most m and m+1 roots, so L divides g. If C=-2x, this line passes through the origin and g(0,0)=0 immediately.

Otherwise write g=Lq, with degree(q)≤m-1. On the first line v=2xh, the factor L equals 4xh-(C+2x). Unless

  j=(C+2x)/(4x)

belongs to {1,...,m}, the restriction q(2xh,h) has m roots and degree at most m-1. Hence q(0,0)=0 and U is full.

If j belongs to that set, the polynomial

  g(v,h)=L(v,h) product_{1≤k≤m, k≠j}(h-k)

has degree m, vanishes on every nonempty option, and has nonzero value at the origin. Indeed C+2x=4xj≠0, and all the indices k are nonzero modulo p. Thus U is non-full exactly when C=(4j-2)x for some 1≤j≤m.

For x=0 and C=0, restrict g to v=0 and use the m+1 heights 1,...,m+1. For x=0 and C≠0, restriction to v=C first forces v-C to divide g; restriction to the m points (0,h), 1≤h≤m, then forces g(0,0)=0. Therefore x=0 is always full.

In particular, for four identical rotations the exceptional differences are C=2x and C=6x, with x≠0. The p=7 formulation in DATA.md involving 4x in {2C,3C} does not carry over unchanged to p=11; the all-prime formula is {2x,6x}.

4. Four arbitrary rotations between two reflections.

Consider U=σ_a ρ_x1 ρ_x2 ρ_x3 ρ_x4 σ_b. Put C=a-b, X={x1,x2,x3,x4}, A=Σ_2(X), and S=x1+x2+x3+x4. The option levels are

  L1=A union {C},
  L2={S} union (C-A),
  L3={C-S}.

If |A|≥3, the triangular criterion proves depth 3. If X is nonconstant and |A|≤2, then X must be x,x,x,y with x≠y. To see this, four distinct values give three distinct pair sums by fixing one value; three distinct values with one repeated give 2x,x+y,x+z; and a two-plus-two multiset gives 2x,x+y,2y, which are distinct in odd characteristic.

For X=x,x,x,y, A={2x,x+y}. If C is outside this set, the level criterion again applies. If C belongs to it, height 1 has two values; whenever height 2 has at least three values, the reversed six-letter criterion applies.

It remains to inspect when height 2 has at most two values. For C=2x, height 2 is {3x+y,0,x-y}. Since x-y≠0, this happens only when y=-x or y=-3x. For C=x+y, height 2 is {3x+y,y-x,0}; it happens only when x=0 or y=-3x.

The cases y=-x,C=2x and x=0,C=y give a rectangle at heights 1 and 2 with value coordinates 0 and a nonzero δ, followed by the height-3 point of value 0. A quadratic vanishing on that rectangle has the form

  λv(v-δ)+μ(h-1)(h-2).

The height-3 point forces μ=0, so the polynomial vanishes at the origin.

For y=-3x,C=2x, the relevant points are

  (2x,1), (-2x,1), (0,2), (4x,2), (2x,3).

For every quadratic Q one has the polynomial identity

  Q(0,0)=2Q(2x,1)+Q(-2x,1)-2Q(0,2)-Q(4x,2)+Q(2x,3).

It is verified on the six monomials 1,v,h,v²,vh,h². Thus vanishing on the options implies Q(0,0)=0. The case y=-3x,C=x+y=-2x uses the same identity with x replaced by -x.

This proves fullness for every nonconstant X, at every odd prime. Constant X is covered by Section 3 with m=2, giving exactly the two stated exceptional differences.

5. Universal six-letter tiles with four reflections.

Consider the three shapes FRRFFF, FRFFRF and FFFRRF. Label their reflections in order y1,y2,y3,y4. All rotations lie in the gaps between reflections 1 and 2 or between reflections 3 and 4. Let u and v be the sums of rotation values in those two gaps, respectively, and put S=u+v. Define

  d_ij=yi-yj,
  A=d_12+d_34,
  q_ij=sum of rotation values strictly between reflections i and j.

The option levels are

  L1={d_ij:i<j} union {S},
  L2={A} union {d_ij+S-2q_ij:i<j},
  L3={A-S}.

Let g be a quadratic vanishing on all options.

Suppose |L1|≥3. Then g=(h-1)(αv+βh+γ). If |L2|≥2, the height-2 points force α=0 and 2β+γ=0; the height-3 point gives 3β+γ=0. Thus g(0,0)=0.

If |L2|=1, every d_ij+S-2q_ij equals A. Additivity of d_ij and q_ij across i<j<k gives A=S. It follows that d_12=2u and d_34=2v, whence A=2S. Therefore A=S=0. The height-2 and height-3 points both have value zero, forcing β=γ=0 and again g(0,0)=0.

Now suppose |L1|≤2. The forward-difference set {d_ij} contains zero: otherwise the four reflection values are distinct, and y1-y2,y1-y3,y1-y4 are three distinct differences. If its only value is zero, all four reflections have the same value. For S=0 the points (0,1),(0,2),(0,3) force g(0,0)=0. For S≠0, L1 contains 0,S and L2 contains 0,S,-S; the reversed level criterion applies.

The remaining possibility is {d_ij}={0,δ}, δ≠0. The reflection values must be two consecutive constant blocks a^j b^{4-j}, where j is 1,2 or 3 and a-b=δ. Indeed every yi is y1 or y1-δ, and a return to y1 after y1-δ would introduce the forbidden difference -δ. Also S belongs to {0,δ}.

Put B=v-u. Direct substitution gives the following height-2 sets:

  j=1: {δ, δ+B, δ-S, S, -B};
  j=2: {0, B, δ+B, δ-S, δ+S, δ-B, -B};
  j=3: {δ, B, δ-S, S, δ-B}.

If a displayed set has at least three values, the reversed level criterion applies. Otherwise, for j=1 or 3 the set is exactly {0,δ}, and the height-3 value δ-S also belongs to {0,δ}. For j=2,S=0, the same conclusion holds, with height-3 value zero. The case j=2,S=δ necessarily has at least three height-2 values: otherwise its values would be only 0,2δ; the simultaneous presence of B,-B forces B=0, after which δ+B supplies a third value.

Thus every remaining case contains the rectangle with values 0,δ at heights 1,2 and a height-3 point whose value is 0 or δ. The rectangle representation from Section 4 forces g(0,0)=0. Polynomial duality proves all three universal fullness statements.

6. Closure and global gluing.

Suppose a unit U has witness θ in J^d. Insert consecutive letters g,g^{-1} anywhere. For each selection contributing to θ, select either neither inserted letter or both. Their product is the identity regardless of the preceding sign, so the value is unchanged and half-size increases by one. Assigning opposite coefficients to these two choices realizes

  θ_new=θ(1-[(0,1)]) in J^{d+1}.

The empty-selection coefficient remains 1. This proves the insertion lemma for arbitrary lengths.

Removing equal-valued adjacent reflection pairs from an inner F^{2a} run, until one pair remains, reduces FRF^{2a}RF to the universal tile FRFFRF. Reinsertion proves the stated longer fullness criterion. In particular it proves FRσ_y^{2a}RF full for every a≥1, all endpoint and rotation values, and every odd prime.

Likewise F^{2a+1}R²F^{2b+1}, a+b≥1, is a concatenation of reflection pairs and one FRRFFF or FFFRRF tile. Therefore it is universally full, with no restriction on the values in its reflection runs.

For gluing, choose one full odd block O and disjoint full even blocks B_i. Cut the cyclic word at O. Assume every remaining string of free reflections has even length, and pair each such string. Treat all B_i and these reflection pairs as already constructed even units. The number of free rotations is even. Pair them in order; between two consecutively paired free rotations are only already constructed even units, so the rotation-nesting construction from T0 gives another full unit. The resulting top-level units cover every position, with total depth

  (|O|-1)/2 + (4p-1-|O|)/2 = 2p-1.

Their product lies in J^{2p-1}=0. Its identity coefficient has empty contribution 1, so some nonempty expanded selection has point zero. Its positive even size is below 4p and divisible by 2p, hence exactly 2p. This is the supplied Lemma G argument.

7. A uniform eight-letter degeneracy and the longer-block interpolation problem.

Consider U=σ_0 ρ_1^4 σ_{-6}^3 and write z=value/2. Choosing an even number of reflections uses either no initial reflection and zero or two final reflections, or the initial reflection and one or three final reflections. Therefore the nonempty option columns are exactly

  z=0: h=1;
  z=1: h=1,2,3,4;
  z=2: h=2,3;
  z=3: h=1,2,

with coordinates interpreted modulo p. The cubic

  q(z,h)=(z-1)(z²-(2h+1)z-(h-1)(h-8))

vanishes on these columns. At z=0 its required value is zero because h=1; at z=1 it vanishes identically; at z=2 it is -(h-2)(h-3); and at z=3 it is -2(h-1)(h-2). But q(0,0)=8≠0 for every odd prime. Section 1 therefore proves non-fullness to depth 4 for every odd prime, including p=3. Thus an additional equal reflection pair need not repair a longer degenerate rotation bracket.

There is a precise interpolation model for a natural unbounded family of proposed repair units. Let

  U=σ_a^{2u+1} ρ_x^n σ_b^{2v+1},
  m=floor(n/2), A=u+v, C=a-b.

Its nonempty options are the union of the following indexed grids:

  S_plus={(2jx,j+t): 0≤j≤m, 0≤t≤A}, omitting the empty index (j,t)=(0,0);
  S_minus={(C-2jx,j+1+t): 0≤j≤m, 0≤t≤A}.

The first grid comes from even reflection counts in both runs; the second comes from odd counts in both runs. Every listed index is realizable. The desired depth is m+A+1. Consequently fullness is exactly the assertion that no polynomial of degree at most m+A separates the origin from these two grids. Section 3 solves A=0. The cubic certificate above shows genuine failure already at m=2,A=1. I do not classify these grids for general parameters.

8. An explicit family in Res, for all primes p≥5.

Define

  w_p=σ_0^{p-2} ρ_1^{p-2} σ_1^{p-2} ρ_1^{p-2} σ_2^4 ρ_1^3.

Its length is 4p-1. It has F=2p, R=2p-1, reflection-run lengths p-2,p-2,4, and rotation-run lengths p-2,p-2,3. In particular o_F=2 and k_O=3.

Condition E fails. The left sides of P and of the empty-gap Davenport-alpha bound are both 3p-2. More precisely, for Davenport-alpha every nonempty rotation gap has negative weight 1-n_t, so an optimal independent set uses only empty gaps. The maximum number of such pairwise nonadjacent gaps is

  floor((p-2)/2)+floor((p-2)/2)+floor(4/2)=p-1.

Thus the maximum item count is R+p-1=3p-2, and the full Davenport-alpha condition fails.

For Doubling, the three nonempty gaps have (length,beta) equal to (p-2,1),(p-2,1),(3,-1). All empty gaps have beta zero, and every rotation value is 1. For j=0 a gap contains fewer than p rotations. For j≥1, two nonempty M-gaps already contain at least p+1 rotations, so they are impossible. If there is one M-gap of length p-2, the required size of K is 2-2j, forcing j=1 and K empty; its beta is 1, so the equation fails. If the only nonempty M-gap has length 3, the required size is k=p-2j-3, an even integer with 0≤k≤p-5; its beta is -1, so the equation would require k=1 modulo p, impossible. If every M-gap is empty, k=p-2j lies strictly between 0 and p whenever feasible, so beta+k is nonzero. Hence no Doubling stretch exists.

For Lemma A, fix any even reflection set Phi. All rotations in a given maximal rotation run have one common signed value, either 1 or -1. Thus the multiplicity a of signed value 1 is a subset sum of p-2,p-2,3, and b=2p-1-a. In every case min(a,b)≤p-2. For every k≥1,

  min(k,a)+min(k,b)-k+1 ≤ min(a,b)+1 ≤ p-1.

Therefore Lemma A fails for every Phi.

The word is not rigid because its reflections have three different values. Corollary R' also fails: a template not containing ρ_1 requires deleting all 2p-1 rotations; a template containing ρ_1 retains reflections of only one value. Each reflection value occurs at most p-1 times, so at least p+1 reflections must be deleted, exceeding p-3. Finally T0 fails because exactly two reflection runs are odd. This verifies every exclusion in the definition of Res.

Nevertheless there is a direct identity 2p-subword. Select all p-2 initial σ_0 letters, one σ_1, all p-2 rotations in the second long rotation run, and the final three rotations. Omit the first rotation run, the other σ_1 letters, and all σ_2 letters. The selected product is

  σ_0^{p-2} σ_1 ρ_1^{p+1}
  = σ_0 σ_1 ρ_1^{p+1}
  = ρ_{-1}ρ_1
  = 1,

and the selected length is (p-2)+1+(p-2)+3=2p.

9. Why bounded short-tile arguments cannot cover Res.

I now prove that w_p has no tiling reaching total depth 2p-1 when every top-level block has length less than p.

For any such block of length L, put d=floor(L/2). Every nonempty admissible selection has height among 1,...,d. The polynomial product_{j=1}^d(h-j), with empty product 1, separates the origin from these options. Hence the block cannot have depth d+1.

If L=2d and the block contains an odd number of reflections, its whole selection is inadmissible. Every admissible selection then has height at most d-1. The polynomial product_{j=1}^{d-1}(h-j) prevents depth d. Consequently every even full block shorter than p contains an even number of reflections.

Let q be the number of odd blocks in a proposed tiling of w_p. The total depth is at most

  sum floor(L_i/2)=(4p-1-q)/2.

Since q is positive and odd, reaching 2p-1 requires q=1 and fullness of every block. All even blocks then contain even reflection counts. Since w_p has 2p reflections, its unique odd block must also contain an even reflection count.

Consider the middle run σ_1^{p-2}. A consecutive cyclic block containing one of its reflections and any reflection from another run has to contain an entire intervening rotation run of length p-2, plus at least one reflection at each end. Such a block has length at least p. Therefore every block shorter than p that meets this middle run contains reflections from no other run. Every block contributes an even number of its reflections, contradicting the odd run length p-2.

This is an all-prime obstruction to full tilings with uniformly bounded unit lengths. It is not an obstruction to the target theorem, since the family has the direct selection in Section 8.

The bracket resonance is also explicit. For p≡3 modulo 4, p≥7, the natural bracket around either long rotation run has n=p-2, C=-1 and m=(p-3)/2. The index j=(p+1)/4 lies in 1,...,m and satisfies C=4j-2 modulo p, so both brackets are non-full. The bracket around the final three rotations has C=2 and m=1, and is also non-full. Thus all three natural rotation-run brackets can fail simultaneously inside Res.

For p≡1 modulo 4, the long bracket of length p is full: the unique residue j solving 4j=1 is (3p+1)/4, outside 1,...,(p-3)/2. Using the last σ_0, the first long rotation run and the first σ_1 as the odd block leaves only even reflection runs, so Section 6 gives a full tiling of this subfamily using an unbounded-length odd unit.

10. Remaining gap and computational checks.

The unresolved issue is global. I have not proved that every remaining word in Res admits disjoint or nested full units pairing its reflection defects, nor that every simultaneous-degeneracy configuration has a direct identity construction. The residual constraints do not supply the missing matching theorem in this argument. The family above proves that a fixed upper bound on unit lengths cannot supply such a theorem by itself. The two-grid model in Section 7 identifies one specific unbounded interpolation problem that remains unsolved here.

Computations were used only as sanity checks. Exact checks at p=3,5 confirmed the three universal six-letter shapes; 746 constant-bracket checks over p=3,5,7,11,13 matched Section 3; and the supplied coverage tests confirmed the residual family at p=5,7. None of these finite checks is used as a proof of an all-prime statement.