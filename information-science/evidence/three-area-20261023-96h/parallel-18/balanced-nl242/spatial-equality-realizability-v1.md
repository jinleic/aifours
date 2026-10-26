# Spatial equality obstruction: no genuine full-rank L=8 canonical pair

Observed before creation: **2026-10-23T15:49:00-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN PROOF**; a new complete spatial argument requiring its own actual reconstruction and parent disposition. No scientific executable, solver, enumeration, arithmetic interpreter or formal kernel ran.

## 1. Literal result and exact checked baseline

**Theorem E (candidate).** Let K_g,K_h be genuine canonical Walsh spectra of two odd-weight Boolean functions on V=F_2^8, with `|K_g|+|K_h|<=28` pointwise. Put S=K_g+K_h, R=K_g-K_h, and `D=(R/8 mod2)`. If the polar form of D is nonsingular, then

`#{y:|S(y)| in {4,12}} !=8`.

This excludes the entire **full-polar-rank, exactly-eight-defect stratum**, not merely the previously rejected count profile. It does not exclude either complete full-rank residue type, any lower-rank type, or balanced242 existence. Combined with the earlier separately gated L>=8 chain it would give L>=9 in the two full-rank types; the present proof does not independently accept or re-prove that earlier chain.

The one checked new input is the parent's operative written disposition

`institute/runs/three-area-2026-10-23-96h/nl242-joint-profile-parent-v1.md`,

observed SHA256 `585e5e2b934e3bc3953cd33c83078fab7ba73320f2b9946dc3c0e216ada7ba85`.

It supports the signed-eight-point bound and exact equality tables, and the necessary boundary **m=224 for a genuine full-rank L=8 pair**. Its source is `joint-profile-realizability-v1.md`, SHA256 `5bbe53363d8a485d3cd9b4f3840d8691433e8cd1aef414eb9902b86f0ea32822`, read with erratum `28fad30f9393ba907c8ef24f002d0990221aa958eb9a0e87502c19e4168fbd47` and actual peer reconstruction `a389df9df8ab1858fd59e3770d0c0ea2f7817ebf39d2cbf0599532699c3eb9a7`.

This import is in-harness written checking, not formal/human/priority acceptance. The new spatial proof below is NOT covered by that acceptance. It uses no additional scalar-feasibility claim or old solver output.

## 2. Necessary S-interface and a legal normalization group

Write H for the unnormalized256-point transform, `chi=(-1)^D`, and `Q=(H chi)/16`, a sign function because D has full polar rank8. A genuine canonical pair supplies

`H S in {0,±512}`, `S=4+8D mod16`, `|S|<=28`.

Consequently `T=chi S in {-28,-12,4,20}`. Define the eight-point defect set

`A={y:T(y)=-12 or4}`,

and delta=chi on T=-12, delta=-chi on T=4, and0 elsewhere. For y in A set `r(y)=chi(y)delta(y)`, so

`T(y)=-4-8r(y)` on A; `T(y) in {-28,20}` off A.          (1)

Let `b=phi(H delta)`, where phi selects0,±1 modulo3. The checked joint boundary gives `wt(b)=224`.

The following operations preserve every S-interface hypothesis just stated, the full polar rank, L=8 and wt(b)=224:

1. invertible affine changes of the frequency variable;
2. for an affine Boolean ell, `S'=(-1)^ell S`, `D'=D+ell`, `delta'=(-1)^ell delta`.

For operation2, the congruence becomes S'=4+8D' mod16, `chi' S'=chi S`, and the Fourier alphabet is shifted/permuted and possibly globally signed. H delta is likewise shifted/signed, so wt(phi(H delta)) is unchanged. The polar form is unchanged by adding ell.

We do **not** assert that the normalized S has a newly constructed canonical Boolean pair R. Instead we prove impossibility in this larger necessary S-class with the retained m=224 hypothesis. Its affine/sign invariance therefore legitimately permits the normal forms below. No truth-table half is fixed or silently changed in the target.

## 3. A common geometric decomposition

The exact mod3 lift gives `B=(H S)/512=phi(Q-H delta)`. If b=phi(H delta), its three residue cases give

`B=Q(1-(3/2)b^2)+(1/2)b`.

Applying H yields

`S=F+C`,

`C=H b=H phi(H delta)`,

`F=32chi-3H(Q b^2)=2H(Q G)`, `G=1-(3/2)b^2`.            (2)

Let `L=u_0+K` be the affine span of A, dimension d. The correction C is supported inside L. In coordinates on K, with v=delta restricted to L,

`C(u_0+y)=2^(8-d) J_d(v)(y)`, `J_d(v)=H_d phi(H_d v)`.    (3)

Indeed H delta is a sign character times a lift of H_d v; phi is odd, and summing over the complementary dual directions gives exactly this factor and support.

Because b^2 ignores that sign character, G depends only on the restriction of a frequency to K. Its character expansion is supported on K. In (2), each such character translates H Q=16chi, so **F/chi is constant on every coset of**

`R_0=K-perp_B`,

where B is the polar form of D. A fiber has2^(8-d) points. Outside L, C=0 and S=F, so any fiber meeting the outside has |F|<=28 everywhere. If `R_0` is not contained in K, every fiber meets the outside. The same conclusion follows by size whenever a fiber is larger than L.

These are actual common-coordinate constraints, not histogram inequalities.

## 4. Exhaustive equality cases inherited from the checked support theorem

Eight distinct points have affine dimension3..7. At m=224:

- d=3 or4: all signs are covered by the arguments in §5 below; no extra sign classification is assumed;
- d=5: the two-dimensional even relation code has nonzero weight triple(4,4,8), with the two weight-four relation signs opposite;
- d=6: its unique nonzero even relation has weight8 and negative sign;
- d=7: impossible already, since the checked formula gives m=170.

The d=5/6 assertions are exactly the equality entries of the parent's checked relation-code tables, not an exhaustive native search.

## 5. Low affine dimensions3 and4

### 5.1 Dimension3

Here L has8 points and every F fiber has32 points, so |F|<=28 everywhere. Every point of L is a defect, giving |S|<=12 and hence |C|<=40. Equation (3) gives C=32J_3(v), so |J_3(v)|<=1 at all8 points.

But the local ternary support has `224/32=7` points, so Parseval gives

`sum J_3(v)^2=8*7=56`,

contradicting the upper bound8. Thus d=3 is impossible.

### 5.2 Dimension4, not Lagrangian

If `K!=K-perp_B`, all fibers meet outside L, so |F|<=28 everywhere. Put J=J_4(v). Its local ternary support has14 points. Every J value is therefore even, and J=v modulo3 because H_4^2=16I.

At the eight defects, |C|<=12+28=40 gives |J|<=2, so the only even value congruent to v=±1 is J=-2v. Off A in L, |C|<=56 gives |J|<=3, so the only even multiple of3 is0. Thus `sum J^2=8*4=32`, while Parseval requires `16*14=224`. Contradiction.

### 5.3 Dimension4, Lagrangian

Now R_0=K and F/chi is one constant c on L. D restricts affinely to L. Gauge locally by that affine character: set r=chi*delta on L. Equivariance of J_4 under affine sign characters, obtained by shifting/signing its two H transforms and using oddness of phi, gives

`T=c+16J_4(r)` on L.

The local ternary support still has14 points, so J_4(r) has common even parity. At defects equation(1) gives `c+16J_4(r)=-4-8r`. Since T=4 mod16, write c=4+16h. Then `J_4(r)=-h-(1+r)/2` on A. Opposite r signs would give adjacent parities, impossible. Thus r=sigma*1_A with one sign sigma.

Let `J_0=J_4(1_A)`, with common value j on A. Off A the two permitted T values imply `J_0-j in {-1,2}`; common parity eliminates-1. Hence `J_0=(j+2)1-2*1_A`.

At the zero transform frequency, H_4 1_A=8 and phi(8)=-1. Transforming that identity gives `-16=16(j+2)-16`, so j=-2. Thus J_0=-2*1_A and `sum J_0^2=32`, again contradicting Parseval16*14=224. This handles every Lagrangian sign case.

## 6. Dimension5: an affine plane and a bent-sign plane

The equality relation code has two disjoint four-point relations P_1,P_2 whose union is A. Each is an affine plane. Their combined affine span has dimension5, the maximum2+2+1, so their two direction spaces are disjoint and their offset is outside their sum.

After the legal affine coordinate change and affine sign gauge of §2, write the local coordinates of L as `(v,w,t) in F_2^2 x F_2^2 x F_2` and arrange

`P_1={(v,0,0)}`, `delta=1 on P_1`,

`P_2={(0,w,1)}`, `delta=q(w):=(-1)^(w_1 w_2) on P_2`.

Why every sign case is covered: positive product on a four-point plane is an affine sign character; negative product is its nondegenerate quadratic sign times an affine character. The two plane products are opposite by the equality table. An ambient affine sign has independent affine restrictions to these two independent planes, so it removes the unwanted affine parts while preserving the required quadratic term on P_2. The accompanying D+ell operation is essential; no arbitrary sign change of delta alone is used.

Since `H_2 q(beta)=2q(beta)`, the local transform is

`z(alpha,beta,tau)=4*1_(alpha=0)+2s`, `s=(-1)^tau q(beta)`.

Thus its exact mod3 lift is

`phi(z)=-s+(1_(alpha=0)/2)(3s-1)`.

Applying H_5 termwise gives

`J_5(delta)(v,w,t)=-4*1_(w=0,t=0)+(6-16*1_(v=0))q(w)*1_(t=1)`.

Multiplying by the factor8 in (3), this proves the **entire correction in L**:

- on P_1: `C=-32delta`;
- on P_2: `C=-80delta`;
- on t=1,v!=0: `C=48q(w)`;
- at the other points: C=0.

At a P_2 point, equation(1) gives `F/chi=-4+72r`, hence |F|>=68. Every point in its F fiber must have |C|>=40 to keep |S|<=28. The high-correction set is exactly the hyperplane t=1 inside L. Therefore the entire three-dimensional fiber direction R_0 lies in the four-space t=0, namely `U_2 direct-sum W_2`.

By dimension, `R_0 cap W_2` contains a nonzero h. Translating any P_2 point by h stays in P_2 and in the same F fiber. Since F/chi=-4+72r there, r must be invariant under this translation for every w.

But h in K-perp_B annihilates W_2. The derivative of D along h on P_2 is therefore constant in w, whereas the derivative of the bent sign q(w) along any nonzero h is a **nonconstant** linear sign on the two-space. Their product `r=chi*q` cannot be invariant. Contradiction. This closes the whole dimension5 equality family, not a selected profile.

## 7. Dimension6: circuit correction and forced extra defects

### 7.1 Exact circuit normal form and its correction

The equality table has exactly one nonzero even relation, containing all eight points, with negative sign. Their affine span is6. By §2's legal transformations normalize

`A={0,e_1,...,e_6,j}`, `j=e_1+...+e_6`,

`delta(0)=-1`, `delta(e_i)=delta(j)=+1`.

All sign cases have the same negative product and differ from this one by an affine sign character on the affinely spanning eight points; the restriction map has rank7 and its sole constraint is the full eight-point product. This proves the claimed normalization rather than choosing a convenient sign ansatz.

Write L=K=F_2^6 inside V. Let

`zeta(alpha)=-1+sum_i(-1)^alpha_i+(-1)^(sum_i alpha_i)`.

At weights0,1,2,3,4,5,6 this has respectively values6,2,2,-2,-2,-6,-6. Its eight exceptional frequencies are

`E={0,j+e_1,...,j+e_6,j}`,

with sign+ at0 and− at the other seven. Let M=I+J_6, where J_6 is the all-one matrix. Over F_2, M is symmetric and M^2=I, and E=M A. The signed exceptional function is `-delta composed with M`.

Since `phi(zeta)=-zeta/2+3 sign(zeta)*1_E`, it follows by H_6^2=64I that

`J_6(delta)=-32delta-3 zeta(M y)`.

Here the symbol J_6(delta) denotes the transform operation J_d at d=6, not the all-one matrix; M was defined explicitly above to avoid any reliance on it as a group-theoretic operator. Equation(3) multiplies this by4 in V. At A the correction is exactly

`C=-56delta`;                                             (4)

at L outside A it has magnitude24; and outside L it is0. Indeed zeta(M y) has magnitude6 exactly for y in A and magnitude2 elsewhere in L.

At a defect, equations(1),(4) give

`F/chi=-4+48r in {44,-52}`.                                (5)

Thus its entire four-point F fiber must stay in L; any point outside L would have S=F of magnitude>28. Consequently `R_0=K-perp_B` is a two-space contained in K. The restricted polar form on K has radical R_0 and rank4.

### 7.2 Quadratic projections on the actual four K-cosets

Put `q_K(k)=D(k)+D(0)` on K, so q_K(0)=0. Its polar rank is4. For a K-character kappa, let E_kappa be the four-element affine dual slice `{x:x|K=kappa}`. Character expansion gives the exact projection identity

`H(Q*1_Ekappa)(y)/chi(y)=(16/64)W_qK(kappa+B(y,cdot)|K)`.

The nonzero W_qK values have magnitude16. They occur exactly when

`kappa|R_0=q_K|R_0+B(y,cdot)|R_0`.

Hence, using that b vanishes exactly over the eight exceptional local characters E, formula(2) becomes

`F(y)/chi(y)=-16+12 sum sigma_kappa(y)`,                   (6)

where the sum is over the exceptional characters satisfying that restriction and each sigma is±1.

As y runs through V/K, the restriction on R_0 takes every one of its four values once: nonsingularity of B makes the map onto R_0-star surjective, with kernel R_0-perp_B=K. Thus the exceptional eight-point set is partitioned into four fixed slices, with occupancies k_lambda summing8, one slice for each actual K-coset.

On the three K-cosets outside L, C=0 and T=F/chi must be-28 or20. Equation(6) requires the sign sum to be-1 or3, so the corresponding k_lambda are odd. Their sum with the fourth occupancy is8, so the fourth occupancy is odd too. Four positive odd integers summing8 have, up to order, only the patterns

`(5,1,1,1)` or `(3,3,1,1)`.

In particular at least one occupancy-one slice corresponds to a K-coset **outside L**.

### 7.3 One exceptional character creates forty forbidden defects outside L

In that outside coset, equation(6) is `T=-16+12sigma(y)`. To avoid a new defect it would have to have sigma=-1 everywhere, giving T=-28. We show sigma also equals+1.

For its single fixed kappa, as y varies through the64-point K-coset, `kappa+B(y,cdot)|K` ranges over the entire16-point affine Walsh support of q_K, each value four times: the restricted polar map has kernel R_0 of size4 and rank4.

All16 nonzero Walsh coefficients of q_K are±16. Fourier inversion at0 gives their total64 because q_K(0)=0. Their signs therefore have sum4, so exactly ten are positive and six negative. Thus sigma=+1 at forty points of this outside coset, and sigma=-1 at twenty-four.

At those forty points, equation(6) gives T=-4 and therefore |S|=4. They would be additional defects outside L, while A was the entire eight-point support contained in L. Contradiction.

This closes the circuit equality case in actual common coordinates; no scalar occupancy relaxation or assumed simultaneous sign alignment is substituted.

## 8. Conclusion and exact unresolved target

All possible affine dimensions and equality sign cases at m=224 have been excluded: d=3/4 by actual correction size/parity, d=5 by the bent-plane/radical derivative conflict, d=6 by the circuit projection forcing forty new defects, and d=7 by the checked m=170 table. This proves Theorem E subject to a separate actual reconstruction of this new spatial argument.

The proof uses the genuine joint S/R interface to obtain m=224, then proves that no simultaneous spatial S-interface can realize any equality case. It is therefore a new input beyond the accepted single-profile contradiction and beyond boundary-plus-Parseval arithmetic. It is not a list of scalar profiles passed off as Boolean functions.

No entire residue type is closed. Other L values, the five lower-rank types, the unrestricted balanced maximum and an actual balanced242 truth table remain unresolved. Relative to acceptance of the earlier separately gated small-defect family, the residual full-rank branches would move from L>=8 to L>=9; that dependent consequence is not counted as another independent discovery.

Formal verification, human/cross-vendor review and worldwide novelty remain unestablished. No scientific execution has occurred. Parent and an actual separate reconstruction are required at these frozen bytes before any supported label is used.
