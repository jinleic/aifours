# Conditional exclusion of the balanced quadratic type (polar rank4, weight128)

**Status:** new candidate written proof and finite classification, awaiting its own fresh independent proof review; not Lean-verified or human peer reviewed. Its imported zero-set/magnitude and next-residue lemmas received the parent's separate Opus5.5 hostile verdict **CORRECT-WITH-FIXES**, with no mathematical error (`inputs/parent-candidate-review.json`). The application below is explicitly conditional on those reviewed lemmas with the errata incorporated here. This is not an acceptance verdict for the present new exclusion. Known Walsh residue, quadratic-normal-form and canonical-sign tools are prior art; no priority or new-general-method claim is made.

The conclusion excludes one *quadratic residue type*, not all balanced nine-variable functions. No truth table is constructed. The other seven types in the reviewed `SHARPER.md` are outside this assignment.

## 1. Explicit hypotheses and coordinate conventions

All vector spaces below are over `F_2`. Truth/frequency inputs are integers0..255 with bit coordinates `a_i=(a>>i)&1`. Character transforms are unnormalized:

`hat p(x)=sum_a p(a)(-1)^(a.x)`.

The candidate lemmas, when applied to a balanced peak<=28 target in type(4,128), give an integer function `p` on eight-dimensional `s-perp` and a quadratic `D` satisfying:

- **H1:** `D(0)=0`, `wt(D)=128`, and its polar matrix has rank4.
- **H2:** the zero set `Z={p=0}` is a **linear three-flat**. On `D=0` outside `Z`, `|p|=2`; on `D=1`, `|p|=3`. In particular `Z` is contained in `D=0`.
- **H3:** `hat p` takes values in `{0,+64,-64}`. The argument below uses only its magnitude bound64, while the next-bit lemma uses its stronger divisibility.
- **H4:** for `E=(p-D)/2 mod2`, the quartic coefficients are the principal4-coordinate Pfaffians of the polar matrix of `D`, and `deg E<=4`.

The source of linearity in H2 is **balance**, not affine normalization: the reviewed candidate first obtains an affine three-flat from its zero-moment identities, then uses the original Walsh zero at the origin to make it linear. We cite that derivation with the review errata below; the new finite audit does not replace the imported proof.

For the precise map to the original spectrum, use the split `V=ker(v)` with `v.s=1`, coset origin `s`, and basis map `B:F_2^8->V`. For a nine-variable frequency `a in s-perp`, put `b=B^T a`. This restriction map is bijective: its kernel in the nine-space is `span(v)`, and `v` does not lie in `s-perp`. Then `R(b)=eta(b)W_f(a)`, where `R=K_g-K_h`, `epsilon_g=(-1)^((wt(g)+1)/2)`, and `eta(b)=epsilon_g*(-1)^(b.supportXOR(g))`. The equal half-support XORs and `epsilon_h=-epsilon_g` give this identity. The neighboring identity, if used, is `S(b)=eta(b)W_f(a+v)` with this **specific split normal v**, not an arbitrary vector of dot product one with `s`. Only the `R` identity is used here. Set `p(b)=R(b)/8`; H2 then corresponds to magnitudes0/16/24 of the original restricted spectrum. No off-`s-perp` histogram totals are used in the new contradiction.

### Dependency ledger for the conditional application

The complete imported chain is explicit:

1. The reviewed canonical-sign tools give `hat K_g,hat K_h in {+/-256}`, hence `hat p in {0,+/-64}`. This is the source of H3, not an assumed Boolean realization of a profile.
2. The candidate's zero-set identities give even zero count, zero support XOR and second-moment matrix equal to the6-coordinate Pfaffian cofactor of the polar matrix. In rank4 that matrix is zero. The candidate uses this to obtain at least8 nonempty zeros, exclude10 zeros, and identify an8-point zero set as an affine three-flat.
3. The candidate's exact slack identity, quadratic-correlation bound and congruences give `z+2(a+c)<=16` and its listed seven triples, then exclude all but `z=8,c=0,a in {2,4}`. Here `c` counts `|p|=1`; **c=0 is essential** for `|p|=3` on every `D=1` point. This is the source of the exact magnitude pattern in H2, not merely its three histogram totals.
4. Balance puts the origin in that affine zero-flat, giving the linearity required in H2.
5. Fourier divisibility yields the next-bit degree bound and the fixed Pfaffian quartic in H4. The E-extension and character-alignment steps below depend on the full quartic statement, not just `deg E<=4`.

Items2–5 belong to the separately reviewed candidate report. We incorporate its coordinate errata by applying the moment/next-bit lemmas **directly after** a linear change of variables, whose hypotheses are invariant, rather than assuming an unproved Pfaffian-cofactor covariance law. The moment and next-bit identities are pruning identities, not standalone obstructions: the moment result holds whenever the canonical difference has peak<=24, and the next-bit result holds for every odd pair. Their force here comes from the additional exact balanced magnitude pattern and the projection contradiction. The candidate's unarchived “300 controls” are not used: `inputs/parent-candidate-audit.json` records the parent's independently archived601 controls. If these reviewed dependencies hold, the new conclusion is precisely: **no balanced nine-variable peak-at-most28 function has residue type(rank4,weight128)**. The seven other listed types remain `(2,192),(4,160),(6,112),(6,128),(6,144),(8,120),(8,136)`.

## 2. Why the stated quadratic normal form is WLOG by a linear map

A rank4 alternating polar form admits two symplectic pairs and a four-dimensional radical. Weight128 means that the restriction of `D` to the radical is a nonzero linear functional: if it vanished, its quadratic sign bias would have magnitude64 and its weight would be96 or160 instead.

Choose a radical vector `e_z` with `D(e_z)=1`, and choose `k_0,k_1,k_2` spanning the kernel of `D` in the radical. Choose a symplectic basis for the other four directions. If a chosen symplectic basis vector has `D(e_i)=1`, replace it by `e_i+e_z`. The polar pairings do not change, while its value of `D` becomes zero. Since `D(0)=0`, this gives a **linear**, not merely affine, coordinate change to

`a=(u_0,u_1,u_2,u_3,z,k_0,k_1,k_2)`,

`q(u)=u_0u_1+u_2u_3`, `D=q(u)+z`.

A linear frequency change preserves the origin, linear zero-flats, all pointwise magnitudes and the multiset of transform magnitudes. H4 can be applied in these new coordinates, giving

`E=F_4+P_3`, `F_4=u_0u_1u_2u_3`, `deg P_3<=3`,

because the only nonzero principal4-coordinate Pfaffian in this normal form is the one on the four `u` coordinates.

Let `R=rad(B)=span(e_z,k_0,k_1,k_2)` and `K=R intersect D^-1(0)=span(k_0,k_1,k_2)`.

## 3. Complete zero-three-flat geometry and its stabilizer

On `D=0`, the fifth coordinate is `z=q(u)`. Project away `z` to

`Y=U_4 direct_sum K_3`, with coordinates `(u,k)`.

Projection is injective on `D=0`. The image `L` of a linear zero-three-flat is a three-dimensional linear subspace of `Y`. Its graph lifts linearly exactly when `q|L` is linear, equivalently when the polar form of `q` vanishes on `L`. If

`tau=dim(L intersect K_3)=dim(Z intersect rad(B))`,

then its projection to the symplectic four-space has dimension `3-tau` and is isotropic. Hence `tau` is1,2 or3.

For completeness, these are exactly three orbits under the **linear stabilizer of D**. It suffices to use the subgroup

`(u,z,k) -> (M u, z+q(Mu)+q(u), N k+F u)`,

where `M` is symplectic on `U_4`, `N` is invertible on `K_3`, and `F:U_4->K_3` is arbitrary linear. The middle correction is linear because `M` preserves the polar form. Symplectic maps are transitive on isotropic subspaces of each dimension; `GL(K_3)` is transitive on its `tau`-subspaces; and `F` removes the graph map into `K_3/T`. Thus this subgroup is transitive at each `tau`. Conversely every stabilizer of `D` preserves its polar radical and the kernel of `D` on that radical, so `tau` cannot change. Representatives are

- `tau1`: `Z_1=span(u_0,u_2,k_0)`;
- `tau2`: `Z_2=span(u_0,k_0,k_1)`;
- `tau3`: `Z_3=span(k_0,k_1,k_2)`.

In bit-index notation their bases are respectively `(1,4,32)`, `(1,32,64)`, `(32,64,128)`.

The exact counts are obtained by choosing the intersection `T`, the isotropic projection `S` and its graph map:

`tau1:7*15*16=1680`, `tau2:7*15*2=210`, `tau3:1`.

There are1891 zero-three-flats in total. The finite producer also enumerates **all97155** linear three-subspaces of `F_2^8`; an independent checker enumerates the11811 three-subspaces of `F_2^7` and uses the graph criterion. Explicit8x8 stabilizer matrices map every listed flat to its representative. No orbit assertion is assumed merely from matching counts.

If a matrix `A` maps an original zero-flat to a representative, normalize the function as `p'=p composed with A^-1`. Its zero set is then `A Z`, and `hat p'(x)=hat p(A^T x)`. This specifies the direction of the coordinate map. The quartic class is preserved: the `u` block is `M u`, so `F_4(Mu)+F_4(u)` has degree at most3 (the top coefficient is `det M=1`). Therefore `F_4+RM(3,8)` is preserved as well.

## 4. The exact E-extension criterion excludes tau1

On `D=0`, H2 gives `E=0` on `Z` and `E=1` elsewhere. Thus after projection to `Y`,

`E|D=0 = 1+1_L`.

Write a cubic in eight variables uniquely as `A_3(Y)+z B_2(Y)`, with degrees at most3 and2. Substituting `z=q(u)` gives

`E|D=0 = F_4 + A_3(Y)+q B_2(Y)`.

The lower-degree part is freely adjustable through `A_3`. At degree4 the possible correction is the exterior product `q wedge beta`, for a quadratic2-form `beta` on `Y`. Decomposing by the number of `K` variables shows that the wedge map has rank

`1 + 12 + 3 = 16`:

- `Lambda^2 U -> Lambda^4 U` has rank1;
- `U tensor K -> Lambda^3 U tensor K` has rank12;
- `Lambda^2 K -> Lambda^2 U tensor Lambda^2 K` has rank3.

For `Z_1`, the top term of `1_L` is `u_1u_3k_1k_2`. Terms with these two `K` variables in `q wedge beta` can only be scalar multiples of `(u_0u_1+u_2u_3)k_1k_2`, not `u_1u_3k_1k_2`. Hence no E-extension exists for `tau1`.

For `Z_2`, its top term is `u_1u_2u_3k_2`, which is obtained by using `beta=u_1k_2+u_0u_1` to correct the base quartic. For `Z_3`, the top term is the base `F_4` itself. The cubic remainder is always adjustable. Thus **exactly211 flats pass this necessary E-extension condition**: all210 of `tau2` and the unique `tau3` flat. This is an intermediate residue compatibility result, not211 Boolean functions.

## 5. All extensions have an explicit13-bit description

On `Y` there are64 degree-at-most-three monomials. The preceding wedge rank16 therefore gives

`rank(RM(3,8)|D=0)=64+16=80`.

Its kernel has dimension `93-80=13`. More explicitly define the13-dimensional quadratic space

`B = span{1,u_0,u_1,u_2,u_3,k_0,k_1,k_2,u_0u_2,u_0u_3,u_1u_2,u_1u_3,q}`.

Then the kernel is exactly `{D*b:b in B}`. To see completeness, a cubic vanishing on `D=0` is `A_3+z B_2` with `A_3=q B_2`. Its degree can stay at most3 exactly when the quadratic part of `B_2` belongs to the5-dimensional kernel of `q wedge beta` inside `Lambda^2 U`. Cross `U-K` terms and `K-K` terms have injective wedge maps and cannot occur. The affine8-dimensional part of `B_2` is free. Multiplication by `D` is injective here, since evaluating on `D=1` recovers `B_2` at every `Y` point.

Choose particular extensions

`E_3=1+product_(i=0..3)(1+u_i)`,

`I_2=(1+u_1)(1+u_2)(1+u_3)(1+k_2)`,

`E_2=1+I_2+D*(u_1k_2+u_0u_1)`.

Their quartic part is exactly `F_4`; their restrictions to `D=0` have the required zero-flats. For `tau2` or `tau3`, **all** possible E are therefore

`E=E_tau+D*b`, `b in B`.

There are8192 extensions at either representative. The finite audit checks completeness by an independent rank computation and verifies every extension's common-character property below. This is a reduction of a necessary residue representation, not an enumeration of Boolean truth tables.

## 6. Character alignment and the strict projection-energy contradiction

Let `K_tau=Z_tau intersect rad(B)`, of dimension2 or3. The particular `E_tau` is independent of the coordinates in `K_tau`. Every `b in B` depends on all `K` coordinates only through an affine linear form with **constant** coefficients; it has no `u-k` or `k-k` quadratic term. Since `D=1` is invariant under these radical translations, there is one fixed character `chi:K_tau->F_2` such that

`E(a+k)+E(a)=chi(k)` for every `a with D(a)=1`, every `k in K_tau`.

On `D=1`, H2 gives only `p=+3,-3`, and the definition of E gives exactly

`p=-3*(-1)^E`.

Therefore `p(a+k)=(-1)^chi(k) p(a)` on all128 points of `D=1`.

Project the entire function `p` to this translation character:

`P_chi p(a)=2^-tau sum_(k in K_tau) (-1)^chi(k) p(a+k)`.

It agrees with `p` on `D=1`; hence its ordinary squared norm is at least

`sum_a (P_chi p(a))^2 >=128*9=1152`.

Its character transform equals `hat p(x)` on the affine dual slice `x|K_tau=chi` and is zero elsewhere. That slice has `2^(8-tau)` points. H3 and Parseval therefore give

`sum_a (P_chi p(a))^2 <= 2^(8-tau)*64^2/256 = 2^(12-tau)`.

This is1024 for `tau2` and512 for `tau3`, both strictly less than1152. Contradiction.

**This is not the invalid transfer of the three-variable fiber parity argument to two variables.** The crucial extra input for `tau2` is the complete13-bit E-extension description: it forces one *fixed* character on the two-dimensional radical intersection. Without that restriction, bent two-variable sign tables and four odd fiber parities would indeed remain possible.

Sections4 and6 exhaust the three zero-flat geometries. Thus no `p` can satisfy H1–H4. **Conditional on the candidate report supplying H1–H4 for a balanced type(4,128) target, that entire balanced quadratic residue type is excluded.** This conclusion is not global balanced nonexistence and does not exclude any of the other seven residue types.

## 7. What was attempted but did not give an extra exclusion

Before finding the projection argument, a next-bit carry test was implemented for the two compatible representatives. Writing the allowed integer values exactly as `p=D+2E-4F`, `F` is fixed as `1+E` on `D=1` and zero on `Z`; its other120 bits are sign choices. The parity moments implied by `hat p=0 mod64` have rank79 on those120 positions. All8192 E extensions at each representative pass the14 left-nullspace consistency conditions, leaving41 free F parities. This test alone excludes **no** extra E. It was not followed by unrestricted sign SAT or another old search. The projection proof above supersedes the need to enumerate those signs.

## Appendix A. Independent alternative tau3 fiber proof

This appendix records the parent's distinct fiber route explicitly, although Section6 already handles `tau3` through the stronger E information.

**Balanced residue lemma.** For a balanced Boolean function on `n>=4` variables, write `m_i=sum_(x in support)x_i`, `m_ij=sum x_i x_j`. For nonzero frequency `a`, `W(a)=-2^n+4N_a`, where `N_a` counts support points with `a.x=1`. Expanding parity as `sum y_i-2sum y_i y_j+4...` gives

`W(a)=-2^n+4sum_i m_i a_i-8sum_(i<j)m_ij a_i a_j mod16`.

At `a=0`, balance gives `W(0)=0`. In particular `W/4 mod2=a.s`. On a frequency hyperplane where `a.s=0`, coordinates can be chosen so the corresponding `m_i` are even; dividing by8 then gives a quadratic mod2. This derivation is valid for the six-variable fibers here. LXW Proposition1 is the eight-variable instance, not a theorem imported for all arities.

For `tau3`, use a linear frequency change sending `Z` to the three `k` coordinates. Its dual input split gives eight six-variable fibers `f_lambda`, labeled by `lambda in F_2^3`. Walsh zeros on all of `Z` invert to `W_(f_lambda)(0)=0`, so every fiber has weight32. The global support vector annihilates `Z`, so it has a nonzero six-dimensional projection `s'`. Write `H={v:v.s'=0}`, a five-space. The restricted quadratic descends to `q=u_0u_1+u_2u_3+z` on H.

At `v=0`, all fiber Walsh values are zero; handle this point separately. At nonzero `v in q^-1(0)`, all eight full Walsh values have magnitude16. Inverting in the three `k` coordinates gives `H_lambda(v)=2*Walsh(epsilon_v)(lambda)`, with an eight-entry sign table. For any three-variable sign table, `Walsh/2 mod2` is constant over all eight frequencies. Thus the balanced residue lemma makes the fiber support sums differ only in `span(s')`, since `q^-1(0) minus {0}` spans H.

At `q(v)=1`, the corresponding formula is `H_lambda(v)=3*Walsh(epsilon_v)(lambda)`. Divisibility of every balanced fiber Walsh coefficient by4 forces epsilon's Boolean sign exponent to have even weight. An even-weight three-variable Boolean function has degree at most2, because its cubic ANF coefficient is its weight parity. Its spectrum is either one entry `+/-8`, or four entries `+/-4` supported on an affine two-flat. The latter would give four odd values of `H_lambda/4` and four even values, contradicting the already constant parity across fibers. Hence only one fiber receives `+/-24`. Since `q^-1(1)` also spans H, all fiber support sums lie in `span(s')`.

Both spanning claims are elementary: `q=0` contains the four `u` basis vectors, and the vector `u_0+u_1+z` supplies the remaining `z` direction; `q=1` contains `z` and each `u_i+z`. Consequently on all H the values `H_lambda/8 mod2` are quadratics `Q_lambda` with `Q_lambda(0)=0`. At `q=0`, the same even-sign-table argument gives either one `+/-16` (all Q-values0) or four `+/-8` supported on an affine two-flat of labels. That label set has XOR zero.

For label bit `i`, the quadratic `P_i(v)=sum_lambda lambda_i Q_lambda(v)` therefore vanishes on `q=0`. The kernel of quadratic evaluation on `q=0` is exactly `{0,q}`: substitution `z=q(u)` gives rank15 from the16 quadratic monomials, since the four cubic terms `q(u)*linear(u)` are independent and the remaining image is `RM(2,4)`. Thus `P_i=c_i q`. At `q=1`, the unique assigned label must consequently be the same `c` at every one of the16 frequencies. That one six-variable fiber would have Walsh energy at least `16*24^2=9216`, greater than its Parseval energy `64^2=4096`. Contradiction.

The final audit checks all256 three-variable sign tables, their even-weight spectra and affine-flat supports, the rank15/kernel assertion by an implementation-independent method, and the exact energy constants. Profiles and residue extensions are never called Boolean functions.

## Appendix B. One to three Walsh zeros force nonlinearity at most240 in nine variables

This separate corollary uses only the reviewed **first zero moments** and the elementary balanced nonzero-support lemma. It does not depend on the new(4,128) exclusion, its13-bit kernel or the three histogram profiles.

Suppose a nine-variable Boolean function `f` has Walsh peak<=28 and a zero at `a0`. Set `F(x)=f(x)+a0.x`. Then `W_F(a)=W_f(a+a0)`, so `F` is balanced and both the peak and the total number of Walsh zeros are unchanged. The elementary degree/quadratic-Parseval argument recalled in the imported `PROOF.md` gives nonzero support XOR `s` for such a balanced target. The congruence `W_F(a)=4(a.s) mod8` shows that all its zeros lie in `s-perp`.

Use the precise split map of Section1. Its zeros correspond bijectively to the zero set of `p=R/8`. The reviewed first-moment identities say that this nonempty zero set has even cardinality and XOR zero. It cannot have two distinct points, since their XOR would be nonzero. It therefore has **at least4** points. Thus every nine-variable peak<=28 function having any Walsh zero has at least4 Walsh zeros.

Consequently a nine-variable function with exactly1,2 or3 Walsh zeros has peak>28. The presence of a Walsh zero itself forces even truth-table weight: from `W_f(a)=512*1_(a=0)-2wt(f)+4I(a)`, a zero gives `wt(f)=0 mod2`. Hence every Walsh coefficient is divisible by4. A peak>28 is therefore at least32, and

`NL(f)=256-max|W_f|/2 <=240`.

This does not claim attainment, and it does not make a statement for seven or eight variables. It does not require an unrestricted covering-radius theorem. The conclusion is conditional on the separately reviewed first-moment lemma in the same explicit sense as the imported assumptions above; the present note has not yet received its fresh proof-review verdict.

**Priority is unresolved.** The parent inspected the abstract of Carlet–Méaux–Broll, [ePrint2026/037, “On those Boolean functions having only one Walsh zero”](https://eprint.iacr.org/2026/037), which constructs examples in seven/eight/nine variables but, in that inspected abstract, makes no nonlinearity claim. The full PDF retrieval returned403 and was not repeated. We have not checked its full text and do not infer that the bound above is novel, answers its open questions, or contradicts those constructions.
