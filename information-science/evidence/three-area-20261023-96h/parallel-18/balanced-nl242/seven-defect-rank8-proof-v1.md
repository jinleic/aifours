# Seven defects are impossible at full polar rank

Observed before creation: **2026-10-23T14:37:47-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN PROOF**, not independently reconstructed, executed, formally checked or novelty-cleared.

This completes the next written obligation requested by the parent: together with the earlier pinned small-defect proofs it gives **a>=8 for both surviving full-rank types (8,120) and (8,136)**. Neither type is excluded in full. This is a consequence of the same mod3 Fourier-rigidity mechanism, not another independent contribution count.

## 1. Common identities and exact scope

Let `V=F_2^8`, H its unnormalized256-point transform, `chi=(-1)^D`, and D a quadratic with nonsingular polar form B. The canonical sum S satisfies

`H S in {0,±512}`, `S=4+8D mod16`, `|S|<=28`.

Put `T=chi S in {-28,-12,4,20}`. Let `A={T=-12 or4}` and define delta=chi on T=-12, delta=-chi on T=4, and0 elsewhere. Thus `supp(delta)=A` and

`S=-chi+delta mod3`.

With `Q=W_D/16 in {±1}`, `H Q=16chi`, the mod3 signed lift gives

`b=(H S)/512=phi(Q-H delta)`, `S=2H b`,

where phi selects0,±1 modulo3. This fixes the entire signed transform, not a histogram.

For `A={u_1,...,u_k}`, with signs epsilon_i=delta(u_i), write `u_I=sum_{i in I}u_i`, `epsilon_I=product_{i in I}epsilon_i`. The sine addition identity gives the exact decomposition

`S=F+C`,                                                   (1)

`F(y)=(-1)^k2^(5-k) sum_{|I| even}(-3)^(|I|/2)epsilon_I chi(y+u_I)`,

`C(y)=(-1)^(k+1)2^(9-k) sum_{|I| odd}(-3)^((|I|-1)/2)epsilon_I 1_{y=u_I}`.

These formulas are proved in the earlier full-rank manuscript, SHA256 `f6f1dc1f16d322025307cb748fa973522d8fe55af2503c2e98f1aa7fff744aa3`; a second form, proved in the six-defect manuscript, SHA256 `02a13eaf53b991b068d15ea6e24285bd025a5e626baecc3e8dbac6bf547139fd`, is

`C=H phi(H delta)`.                                        (2)

Let `L=u_0+K` be the affine span of A, dimension d. Every odd-subset sum lies in L, so C is supported there. Every even-subset sum lies in K, and quadratic polarization shows that F/chi is constant on every coset of `K-perp_B`, of dimension8-d. Outside L, S=F and |F| is20 or28.

If a fiber meets the outside of L, its F magnitude is consequently<=28 everywhere. If `K-perp_B` is not contained in K, every fiber meets the outside. This remains true by cardinality for d<=3.

In coordinates on K, with `r(v)=delta(u_0+v)`, equation (2) reads

`C(u_0+v)=2^(8-d) J_d(r)(v)`, `J_d(r)=H_d phi(H_d r)`.      (3)

No executable calculation or classification is used below.

We assume |A|=7 and exhaust its possible affine dimensions3,4,5,6.

## 2. Affine dimension3

Every F fiber has32 points, while L has8, so |F|<=28 everywhere. At defects |S|<=12, giving |C|<=40; at other points |C|<=56. Equation (3) makes C a multiple of32, hence |C|<=32 everywhere.

Let `z=phi(H_3 r) in {0,±1}`. Then all entries of H_3 z are0,±1. Parseval gives `8 sum z^2=sum(H_3 z)^2<=8`, so z has support at most1. It cannot have support0 because H_3 is invertible modulo3 and r is nonzero. With support1, H_3 z is nonzero modulo3 everywhere, whereas

`H_3 z=H_3^2 r=8r mod3`.

This would force r to have support8, not7. Contradiction.

## 3. Affine dimension4, not Lagrangian

Suppose `K!=K-perp_B`. All F fibers meet the outside, so |F|<=28 everywhere. Put `J=J_4(r)` and `z=phi(H_4 r)`, with `m=wt(z)`.

On A, equation (3) and the cap give |J|<=2; on the other nine points of L, |J|<=3. Also

`J=H_4^2 r=16r=r mod3`.

Every entry of J has the common parity m, since it sums m signs.

- If m is even, on A the only even integer of magnitude<=2 congruent to r is -2r. Off A the only even multiple of3 of magnitude<=3 is0. Thus `sum J^2=4*7=28`, impossible because Parseval makes it16m.
- If m is odd, on A the only odd integer of magnitude<=2 congruent to r is r. Off A it is±3. Thus `sum J^2=7+9*9=88`, again not divisible by16.

Contradiction in both cases.

## 4. Affine dimension4, Lagrangian

Now `K=K-perp_B`; F/chi is a single constant c on L, and D restricts affinely there. Gauge

`r(v)=chi(u_0+v)delta(u_0+v)`.

The affine-sign equivariance of J_4, which follows directly from H and the oddness of phi, gives

`T(u_0+v)=c+16J_4(r)(v)`.                                  (4)

At a defect, the sign definition says exactly `T=-4-8r`. Since T=4 mod16, c=4 mod16; write c=4+16h. At defects,

`J_4(r)=-h-(1+r)/2`.

The values corresponding to r=+1 and r=-1 differ by1. But every entry of J_4(r) has a common parity. Hence r has one common sign sigma on all seven support points: `r=sigma 1_A`.

Write `J_0=J_4(1_A)`, whose common value on A is j by (4). The defect equation yields `c=-4-8sigma-16sigma j`. At a point outside A in L, T must be-28 or20, so

`J_0-j in {-1,2}`.

The common parity of J_0 eliminates-1. Therefore

`J_0=j on A`, `J_0=j+2 off A`,

or `J_0=(j+2)1-2 1_A`.

For any nonzero frequency x, let `w=(H_4 1_A)(x)`. Since |A|=7, w is odd and nonzero. Transforming the last displayed identity and using the definition of J_0 gives

`16phi(w)=-2w`.

The left side is0,±16, forcing w to be0,±8, impossible for an odd integer. This rules out every Lagrangian dimension4 case.

## 5. Affine dimension5: the exact collision table

The map from even subsets of seven indices (dimension6) to K (dimension5) has one nonzero kernel relation P, necessarily of size4 or6. Set `e=epsilon_P`.

Every point of L has exactly two odd-subset representations, differing by P. For k=7, equation (1) gives coefficients

`singletons:4`, `triples:-12`, `five-subsets:36`, `seven-subset:-108`.

Pairing the two representations gives the following **absolute correction table**, with exact multiplicities. The distinguished largest point is unique.

| P size | e | On singleton defects | Other points | Unique large point |
|---|---:|---|---|---|
|6|+1| six values40; one value104 | twenty-five values24 | remaining singleton, in A |
|6|-1| six values32; one value112 | ten zeros; fifteen values48 | remaining singleton, in A |
|4|+1| four values8; three values40 | twenty-one values24; three values72; one value120 | XOR of the three points outside P, not in A |
|4|-1| four values16; three values32 | twelve zeros; twelve values48; one value96 | XOR of the three points outside P, not in A |

Here is the complete derivation of the pairings, to avoid importing a computational table.

For |P|=6 and remaining index j:

- singleton i in P pairs with the complementary five-subset of P: `C=4epsilon_i(1+9e)`;
- singleton j pairs with all seven: `C=4epsilon_j(1-27e)`;
- the twenty triples contained in P pair with complementary triples: ten points with coefficient `-12(1+e)`;
- the fifteen triples consisting of j and two P indices pair with j plus the other four P indices: coefficient `-12+36e`.

For |P|=4, write J for its three outside indices. Let l be the number selected from P and h the number from J:

- l=1,h=0 pairs with l=3,h=0: four singleton points, coefficient `4-12e`;
- l=0,h=1 pairs with l=4,h=1: three singleton points, coefficient `4+36e`;
- l=2,h=1 pairs with its complementary P pair: nine points, coefficient `-12(1+e)`;
- l=1,h=2 pairs with l=3,h=2: twelve points, coefficient `-12+36e`;
- l=0,h=3 pairs with all seven: one point, coefficient `-12-108e`;
- l=2,h=3 pairs with its complementary P pair: three points, coefficient `36(1+e)`.

The signs of these coefficients are epsilon_I. Distinct pairs give distinct points because P is the entire kernel. The table follows, with no unlisted point.

### Eliminating the table cases by actual fibers

If all F fibers meet the outside of L, |F|<=28 everywhere. Every row immediately contradicts its unique large C value: at a defect |C|<=12+28=40, and at a nondefect |C|<=56. All distinguished values exceed those bounds.

Thus it remains only that `R=K-perp_B` is a three-space contained in K. Fibers inside L have8 points and a common F magnitude.

- **|P|=6,e=+1.** At the distinguished defect |C|=104, so |F|>=92. At every other point C has magnitude<=40. Any other point in its eight-point fiber therefore has `|S|>=92-40=52>28` (a point outside L would be an even more immediate contradiction).
- **|P|=6,e=-1.** At the distinguished defect |C|=112, so |F|>=100. All other C values have magnitude<=48. Again another fiber point gives |S|>=52.
- **|P|=4,e=+1.** At the distinguished nondefect |C|=120, so |F|>=92. To keep |S|<=28 at every point in its fiber would require |C|>=64 at all8 points. Only four points in the whole table have that magnitude (one120 and three72). Impossible.
- **|P|=4,e=-1.** At the distinguished nondefect |C|=96, so |F|>=68. Its entire fiber would have to lie among the13 points with |C|>=40: the distinguished point and the twelve magnitude48 points. The following geometry proves this impossible.

Normalize the affine plane P to `W={0,e_1,e_2,e_1+e_2}` and the three outside points to e_3,e_4,e_5; this is possible because they span L affinely. The magnitude96 point is

`u_*=e_3+e_4+e_5`,

and the twelve magnitude48 points are

`(W+e_3+e_4) union (W+e_3+e_5) union (W+e_4+e_5)`.

There is no affine three-flat through u_* contained in this13-point set. Indeed its intersection with the W-coset u_*+W would be only u_*, so its three-dimensional direction space must intersect W trivially. Projection to the three-space L/W is then injective and onto; its image has8 quotient labels. But the13-point set has only4 quotient labels (111 and the three weight-two labels). Contradiction.

This eliminates every dimension5 case, including the previously unresolved coisotropic branch.

## 6. Affine dimension6

The seven points are affinely independent. All64 odd-subset sums are distinct. At their all-seven XOR u_*, outside A, the correction in (1) is uniquely±108. Every other C value has magnitude at most36.

At u_* the cap gives |F|>=108-28=80. Its F fiber has `2^(8-6)=4` points. If any fiber point is outside L, there F=S has magnitude>=80, impossible. Otherwise choose any other point of this fiber inside L. It has |C|<=36, and therefore |S|>=80-36=44>28. Contradiction.

This exhausts all affine dimensions of a seven-point support.

## 7. Consequence, review gate and residual cases

Together with the earlier candidate exclusions a<=6, the present written proof gives

`polar rank(D)=8  ==>  #{u:|S(u)| in {4,12}}>=8`.

Under the corrected original-spectrum map, this is exactly L(f)>=8 for either full-rank residue type. Consequently the pending sharp-ceiling corollary improves on those two types from the condition L<=6 to L<=7. The all-type sharp result with L<=3 is unchanged.

The exact unresolved union after these candidates is:

- `(2,192),(4,160),(6,112),(6,128),(6,144)` with L>=4;
- `(8,120),(8,136)` with L>=8.

There is no derived contradiction for that union, so no whole type or unrestricted balanced maximum is closed. At eight defects the odd-subset coefficients and affine-relation kernels change; the unique-large-correction argument above is not automatically available. No claim is made about eight-defect feasibility, let alone a genuine Boolean pair.

The full chain is queued for actual separate reconstruction and parent checking. All science here is written; there has been no enumeration, solver run, Walsh replay, scientific arithmetic program, CLI or new runtime. The finite collision table was derived by exact subset pairing and linear dimension arguments, not by an unadmitted executable check. Correctness, scope, formal verification, novelty and significance remain separate.
