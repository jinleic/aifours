# Four-distinct-D0 all-anchor obstruction: original-input reconstruction

**NONBLIND GENERAL-AUTHOR WRITTEN CANDIDATE, NOT ADOPTED.** I reconstruct the entire signed-array Theorem A of packet S2 below, with no even-multiplicity restriction and without sampling. The actual-caller deduction is reconstructed at the explicit conditional imports in §5. In particular, the source packet does not display a definition of the separate local `H_local=0` condition. It also does not exhibit in adopted S4/S5 the general off-graph `g` site values from which S2's residue calculation is asserted; §6 states exactly the needed normalization and its provenance. These are import/coverage boundaries, not an asserted counterexample to the actual caller. Parent review and disposition are separate.

## 1. Complete array statement and notation

Let `I=B=F_2^2`, and let characters of `I` and `B` be indexed by the corresponding duals. Use the standard coordinates to regard `Q(v_0,v_1)=(v_1,v_0)` as a covector. All sums of binary vectors, covectors, and binary exponents below are modulo 2. Let `F:I -> F_2` have odd total sum, let arbitrary anchors `b_i in B`, covectors `k_i in B*`, and signs `sigma_i in {+1,-1}` satisfy

    v = sum_i b_i,       sum_i k_i = Qv.                         (1)

Define `g_i(b)=sigma_i (-1)^{k_i(b)}`. A **single** real array `Y` on `(ell,h,i,b) in F_2 x F_2 x I x B` is required to have:

* `Y(1,F_i,i,b)=g_i(b)`, and on the opposite-h mate plane it is zero at the actual anchor `b_i` and equals `2 d_{i,b}` at all other b, where every `d_{i,b}` is one fixed sign;
* for each i, the two values at `(ell=0,b=0)` are either both zero or both in `{+2,-2}`; at `(ell=0,b!=0)` there are exactly six magnitude-2 sites, a different unique magnitude-4 site, and zeros otherwise; the six sites are distributed as two distinct b sites in each of exactly three physical `(h,i)` cells;
* `sum Y^2=128` and all 64 unnormalized full Walsh coefficients `W` lie in `4+8Z`.

**Claim A.** At least one `|W|>12`. Every variable and sign above is quantified universally. In particular no assumption that the anchor map is affine, that the covectors have even multiplicities, or that different frequencies can choose different arrays is made.

The graph/mate energy is `16+12*4=64`; the six magnitude-2 sites and unique magnitude-4 site contribute 40 more. Thus the first bullet at `ell=0,b=0` and the total energy force exactly three of the four i-rows there to be nonzero. This observation is not used to impose their signs. The all-zero array is already excluded by its 16 graph signs; zero anchors, zero covectors, either sign of the magnitude-4 site, and zero partial transforms are all allowed wherever the stated hypotheses permit them.

## 2. Residue parity and equality forcing

For `s in F_2`, `alpha in B*`, and `beta in I*`, put

    A_l(s,alpha,beta) = sum_{h,i,b} Y(l,h,i,b)
                                      (-1)^{s h + beta(i) + alpha(b)}.

The two full coefficients over this triple are `A_0+A_1` and `A_0-A_1`; their simultaneous caps are equivalent, for real `A_0,A_1`, to `|A_0|+|A_1| <= 12`. Let `n` be the actual number of negative `d` signs, and `m_alpha=#{i:k_i=alpha}`. The graph part of `A_1` is a sum of `m_alpha` terms `+/-4`, hence is `4m_alpha` modulo 8. The 12 mate terms are `+/-2`. Their product of signs is `(-1)^{n+s+alpha(v)}`: indeed the total h exponent is `3 sum_i(1+F_i)=1`, the total i label is `3 sum_i i=0`, and `sum_i sum_{b!=b_i} b=sum_i b_i=v`. A sum of 12 signs multiplied by 2 is 4 times its number of negative signs modulo 8. Consequently

    A_1/4 = n+s+m_alpha+alpha(v)  (mod 2).                       (2)

This also proves that `A_1` is divisible by 4. Let `O={alpha:m_alpha odd}` and `tau_alpha=m_alpha+alpha(v)`. Its size is even and `sum_{alpha in O} alpha=Qv` by (1). If `v=0`, the only even-cardinality subsets with XOR zero are the empty set and the entire four-point dual; hence `tau_alpha` is respectively 0 or 1 for every alpha. If `v!=0`, the XOR is nonzero, so `O={a,a+Qv}`. Since `(Qv)(v)=0`, these two distinct covectors form one entire level set of `alpha -> alpha(v)`. On that level the multiplicity parity is 1, on the other level it is 0, so again `tau_alpha=tau` is independent of alpha. Both choices of level and every multiplicity pattern are included; no selected anchor origin has been used.

Assume all 64 caps. Set `s_0=n+tau` and `s_1=s_0+1`. Because `A_1` is a multiple of 4 and both `A_0 +/- A_1` are 4 mod 8, `A_0` is also a multiple of 4, with `A_0/4` and `A_1/4` of opposite parity. At `s_0`, `A_1` is 0 or +/-8; at `s_1`, it is +/-4 or +/-12. These lists include the zero and cap-boundary cases.

Full Parseval gives `sum W^2=64*128`; with `W in {+/-4,+/-12}`, exactly eight full coefficients have magnitude 4. Let `E` count the 16 triples at `s_0` with `|A_1|=8`, and let `O_count` count the 16 at `s_1` with `|A_1|=4`. Each E triple has `|A_0|=4` and contributes one small full coefficient. Each O_count triple has `A_0 in {0,+/-8}` and contributes at least one; the corresponding full-frequency pairs are disjoint. Therefore

    E+O_count <= 8.                                             (3)

Five-bit Parseval on the ell=1 half, whose energy is 64, gives

    4E + O_count + 9(16-O_count) = 32*64/16 = 128,
    O_count = 2+E/2,  and hence E <= 4.                           (4)

Now set `C=sum_{i,b!=b_i} g_i(b)d_{i,b}`. Transforming h first, then applying the 16-point Parseval identity over `(i,b)`, gives for either s

    sum_{alpha,beta} (A_1(s,alpha,beta)/4)^2
        = 64 + 4(-1)^s C.                                       (5)

At `s_0` the left side is `4E`, hence `E=16+(-1)^{s_0}C >= 4`, since C is a sum of twelve signs. Thus E=4 and O_count=4. Equality in the sign bound is pointwise: for all twelve sites of this **one** array,

    d_{i,b} = -(-1)^{s_0} g_i(b)       (b!=b_i).               (6)

This is forced simultaneously, not selected separately for each transform.

## 3. Every repeated covector is impossible

At `s_1=s_0+1`, the h-transform of a graph/mate row is `(-1)^{s_1 F_i}g_i(b)` at the anchor and three times this at every other b. Put `w_i=sigma_i(-1)^{s_1 F_i}`. The b- and i-transform is therefore

    A_1(s_1,alpha,beta) = sum_i (-1)^{beta(i)} w_i
        [12*1_{alpha=k_i} - 2*(-1)^{(k_i+alpha)(b_i)}].        (7)

If any alpha occurs exactly twice, the two active brackets equal 10. Their two distinct i-labels allow a beta which makes their signed `w_i` agree, and the other two brackets have absolute value 2. The resulting magnitude is at least `20-4=16`. This covers both multiplicity shapes 2+2 and 2+1+1. If some alpha occurs three times, the differences between three distinct points of `F_2^2` are independent; a beta makes all three active signs agree, and the fourth term has magnitude 2. Thus the magnitude is at least `30-2=28`. If it occurs four times, all brackets are 10; the four-point Parseval identity for the four signs `w_i` implies that some beta has `|sum_i w_i(-1)^{beta(i)}|>=2`, yielding magnitude at least 20. All these violate the necessary `|A_1|<=12`. The zero value of alpha and negative signs require no separate exception.

The remaining four covectors are distinct, hence comprise the entire dual and XOR to zero. Equation (1), with Q invertible, forces `v=0`. A function from the four points of `F_2^2` to `F_2^2` is affine iff the XOR of its four values is zero: choose its value and the two coordinate differences at 0, and the fourth value is then fixed. Thus the actual anchor map is affine. This is a **consequence** of all caps; no nonaffine anchor was aligned in deriving it. Here every `m_alpha=1`, so `tau=1`, `s_0=n+1`, and `s_1=n`.

## 4. Rank-one inversion and the three-cell contradiction

Only now apply the globally invertible affine map `b'=b+b_i`, with ell, h and i unchanged. Because the row-anchor function is affine, this is one affine transformation of the whole six-bit space. It maps the very same array and all frequencies together, preserves the physical h-mate vector, and maps each original `(i,b)` pair and its two h-sites to the same new `(i,b')`. The number n of negative mate signs is unchanged. Write the transported row character as `sigma_i'(-1)^{k_i(b')}`. Multiplying (6) over all 12 mate sites in these coordinates gives

    (-1)^n = product_i sigma_i',

because `sum_{b'!=0} b'=0` and the factors `-(-1)^{s_0}` occur 12 times. Put `w_i'=sigma_i'(-1)^{n F_i}`. Since `sum F_i=1`, `product_i w_i'=+1`. For four signs this is equivalent to `w_i'=c(-1)^{beta_0(i)}` for a sign c and a unique `beta_0 in I*`: these are exactly the eight even-parity sign patterns.

Equation (7) now becomes, where `i(alpha)` is the unique row with `k_i=alpha`,

    A_1(n,alpha,beta)
      = 12 w'_{i(alpha)}(-1)^{beta(i(alpha))}
        -2 sum_i w_i'(-1)^{beta(i)}.                            (8)

For every alpha its magnitude is 4 at beta_0 and 12 at each other beta. The same two caps therefore force

    A_0(n,alpha,beta)=0   for all alpha and all beta!=beta_0.   (9)

Define `B_i(b')=Y'(0,0,i,b')+(-1)^n Y'(0,1,i,b')`. Invert first the full B-transform in alpha and then the full I-transform in beta in (9): for every i and b',

    B_i(b')=(-1)^{beta_0(i)} B_0(b').                            (10)

This is a rank-one conclusion about the **same** transported ell=0 array, not a frequencywise choice. The six magnitude-2 sites occupy only three `(h,i)` cells, hence at most three i-rows. Pick a row with no such site. At every physical b=0, its two h entries are both zero or both signs times 2; their signed sum has magnitude 0 or 4. At any other physical b, the row has no magnitude-2 site and at most the one magnitude-4 site, so again the sum has magnitude 0 or 4. The row-dependent shift by `b_i` only relabels b. Thus (10) forces **every** `B_i(b')` to have magnitude 0 or 4.

Take any magnitude-2 site. At the same i and physical b and the opposite h, the other value is either 0, a magnitude-2 value, or the unique magnitude-4 value. If it is 0 or +/-4, the signed h-sum has magnitude 2 or 6, for either sign of every entry. Hence it must be a magnitude-2 site. Thus every occupied `(h,i)` cell has its opposite-h cell occupied as well. The occupied cells are a union of disjoint two-element pairs, contradicting the stipulated **three** occupied physical cells. This also handles a magnitude-4 site opposite a magnitude-2 site and all cancellations. Claim A follows.

## 5. Actual graph-phase bridge, with one carried physical object

The following is conditional on the exact actual imports: the m116 five-span same physical inverse `4u=x+3a chi_1+g chi_2+y chi_3`, ternary u, `chi_3=chi_1 chi_2`, the common rank-two quadratic f, q(b)=`1+b_0 b_1`, bent `f+q`, bent graph phases R and R+f, the fixed physical graph/mate and off-graph local forms and counts, all 64 U0 divisibilities and caps, the specifically carried original-DC balance `xhat(t)=0`, one D0 in each of the four actual graph L-cosets, and the adopted S4/S5 same-x location theorem at its stated `H_local=0` import. Neither the definition nor the validity of that separate local-H premise is reconstructed here.

As supplied by S5, the radical K of the polar form of f projects bijectively to physical b. Let k(b) be its unique lift. In the global linear coordinates `z=(i,0)+k(b)`, `h'=h+d(b)`, the graph is `h'=F_i=f(i,0)`, where `d(b)=f(z+k(b))+f(z)` is linear and `sum_i F_i=1`. The physical h-mate remains a toggle of h' with b fixed. In these coordinates the actual D0 anchor is `(1,1+F_i,i,b_i)` and its actual graph mate has the same b_i. S4 gives the actual graph-exception offsets `Delta_i` as an affine function of the quotient label in both its 1+1+1 and 2+1 alternatives. Its six Z2 sites occupy precisely three actual ell=0 H-cells, hence three `(h',i)` cells in these coordinates. A complement or a choice of representatives does not let one replace the actual anchors or choose t anew.

To derive the needed row phases rather than assume them, write `R_i(b)=R((i,0)+k(b))` and `V_i(alpha)=sum_b (-1)^{R_i(b)+alpha(b)}`. Bentness of R gives four i-Walsh coefficients of `V_i` of magnitude 4, hence `sum_i V_i^2=16`. Bentness of R+f gives the same flatness for `(-1)^{F_i}V_i`, using b-frequency `alpha+d`. A Boolean two-bit row is either affine with one Walsh value +/-4 and three zero, or nonaffine with all four Walsh values +/-2. If any R_i were nonaffine, the energy 16 at each alpha would force all four rows nonaffine. Their four signs would have product -1, since a flat i-transform has its zero-frequency sum +/-2 after division by 2. Multiplication by `(-1)^{F_i}` flips that product, so the second i-transform could not be flat. Thus every R_i is affine, say `R_i(b)=r_i+lambda_i(b)`. The same energy equation forces precisely one row for each lambda; the four lambda_i are a bijection of the two-bit plane and hence form an affine map of i.

For `X=(-1)^t x` and `Y=(-1)^t y`, the actual graph identity is still `Y=-agX`; a and g are not modulated. On a graph row write the same physical weighted signs as `X=epsilon_i(2*1_{b=gamma_i}-1)`, with `gamma_i=b_i+Delta_i`. Using the graph factors `a=(-1)^{R_i(b)}` and `g=(-1)^{1+b_0b_1}`, the product has character covector

    k_i = lambda_i + (1,1) + Q gamma_i.                          (11)

Indeed `1_{b=gamma}=(1+b_0+gamma_0)(1+b_1+gamma_1)` in F_2; its quadratic term cancels that in q, leaving linear part `(1,1)+Q gamma`. The row scalar absorbs epsilon and all constant terms. Since lambda and Delta are affine, their four-value XORs are zero; summing (11) yields exactly (1), with the actual `v=sum_i b_i`.

The actual local forms then give the graph/mate values required in §1, the two zero-or-magnitude-2 ell=0 values at physical b=0, the six Z2 sites in those three H-cells, and one distinct Z4 site. Their energy is `16+12*4+6*4+6*4+16=128`. The fixed linear coordinate change preserves the array, energy, all Walsh magnitudes and residues, and the physical h-mate; applying Claim A is legitimate once the residue premise is established as in §6. The cited U0 caps and the particular balance are used through the adopted location import, not by choosing a different x or t for each frequency.

## 6. Residue bridge and its exact source boundary

The needed general local g normalization, stated explicitly in the **original physical** coordinates `(ell,h,j,b)`, is

    g(1,f(j,b),j,b)   = rho(b),      rho(b)=(-1)^{1+b_0 b_1},
    g(1,1+f(j,b),j,b) = -2 rho(b),
    g(0,h,j,b) = 1_{b=0} [4*1_{j=0}-2*1_{j!=0}].             (12)

Equivalently, one may import precisely the ell=0 Fourier expression below together with the graph/mate expression. Under (12), for frequency `(nu,s,beta,alpha)`, direct summation gives

    ghat = (-1)^nu [1-2(-1)^s] W_{(-1)^{q+s f}}(beta,alpha)
           + 1_{s=0} [12-16*1_{beta=0}].                       (13)

For s=0 the first term is a multiple of 8 because q depends only on b and its two-bit Walsh coefficients are +/-2; the second term is 4 modulo 8. For s=1 the ell=0 term vanishes and bent `f+q` makes the first term +/-12, again 4 modulo 8. Separately the graph support of a and bentness of R and R+f give `ahat=+/-4`, hence `3 ahat+ghat=0 (mod 8)` at **every** frequency. The actual U0 divisibility gives `xhat=0 (mod 8)`. Fourier-transforming the SAME physical inverse at `w=0`, where the three characters equal 1, gives

    4 uhat(xi,0) = xhat(xi)+3 ahat(xi)+ghat(xi)+yhat(xi).

Since u(c,0) is ternary, its signed Walsh sum modulo 2 equals the number of nonzero u(c,0) modulo 2, namely J. Thus `yhat(xi)=4J (mod 8)` for every physical frequency. If `J=1`, all 64 residues are 4 modulo 8. The already specified modulation by t merely translates the full spectrum, so it preserves the cap and residue. Claim A then rules out all U3 caps for that same x and y.

**Exact verification boundary.** S2 line 111 asserts the general graph/mate and ell=0 terms used in (13). S3 line 7 displays (12) for its *particular* f/R physical construction. Adopted S4/S5 identify the actual-caller/local-form imports and their conclusions but, as literally rendered in this packet, do not independently state the general ell=0 g site formula or define `H_local`. I have verified the algebra from (12) to (13) and the J/residue implication; I have **not** established from the displayed S4/S5 text alone that every actual caller has (12). This is an explicit import-display gap, not a proven falsehood of S2 or a license to change g. A parent with an independently authorized full original local-form source must check that implication before treating the residue bridge as established for all actual callers. The pure array Claim A does not depend on this gap or on local H.

## 7. Full affine changes and remaining scope

For arbitrary anchors, write uniquely `b_i=B i+c+v F_i`, since odd F and `1,i_0,i_1` form a basis of the four binary functions. The global affine shear `b''=b+B i+c+v(h'+1)` aligns the D0 b-coordinates at 0, but sends their actual graph mates to b''=v and the physical mate vector from e to e+H(v). In particular, for v!=0 it is **not** the standard aligned form with both D0 and graph mates at the same b. The coordinate-independent defect is `sum_i D_i+e=H(v)`; an affine map `P(c)=Mc+a` sends it to `M H(v)`, so a nonzero defect cannot become zero under an invertible map. The proof of Claim A avoided this issue by aligning only after it had deduced v=0.

Under any actual affine coordinate change, transport all physical arrays by pullback, including a,g,x,y and u, and transport the same mate vector. Then `W'(xi')=(-1)^{xi'(a)}W(M^T xi')`; the carried linear covector becomes `M^{-T}t` with its affine modulation phase. The change of phase cannot alter 4 modulo 8, and the parity J is unchanged by the common spatial permutation. This is not a license to modulate the inverse's fixed a and g by t or to keep an old mate vector after a shear.

The written result is a proposed obstruction only for the stated physical four-distinct-D0 subfamily, conditional on all named imports and the g-normalization boundary above. It does not rule out other D0 allocations, construct V, restore the original caller, prove the original Boolean target, or establish novelty. It does not make parent acceptance, human, external-family or kernel/formal verification claims.

## 8. Actual reading, pins and non-execution

Before the packet body, I read the complete manifest, freeze receipt, final binding, prepared metadata, actual dispatch receipt and all **23** listed controls through their endings, and sent the direct PREBODY ACK. Control 23 is also designated S7: I read it in its required control role before the literal packet, as disclosed in that ACK. After the ACK I read the sole packet serially in raw windows of at most 20 LF, from LF 1 through its ending LF 458, before comparison or research. These are complete packet renderings of S1 LF1–7, S2 LF1–139, S3 LF1–173, S4 LF1–30, S5 LF1–37, S6 LF1–31 and S7 LF1–11. Parent-supplied whole-source hashes, not separately rehashed source paths, are:

    S1 a1eb0a70820eb9105a043fc22da1bcf9830b5daaa852fdcc5e84244d4d50b894
    S2 63cc4fa48e0dececec9a381b32ca75191eec31e22e2cb3fb4907d7275437e890
    S3 a7deb23a7bf26185d8f9b3cb54c0fe79716bcbac739011ec59453f062cdd18d7
    S4 fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a
    S5 44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a
    S6 3e77eebe5c885ae8b53e04b76f3de46594c5cca2e5647086122bf408fa7052b4
    S7 2253ac97d0b148dfc96406235658b5712c47c6014aecf65befe26e8f20d700ab

I directly hashed the assigned packet and metadata after the complete body read. SHA256: packet `dfb064b343667081a530c794969050967e732883c5adbfbf185e899e6d9c2087`; manifest `23871375d258b1aaaebd9f004a903a699e57a2e2221531adb73272284a945faf`; freeze `156ba336fa833c8d563d10cfb2043c8277706f485cd65693b36c8776ae3ff664`; final binding `b1cda5d1f830e6dd1e851ce2da9eee97d731460f8d2ce2d8288dcf076a02b1c3`; prepared metadata `16de2458189f4ac1779427156935e55aea09905341102e93ed7534596f176ddc`; actual dispatch `f7b665653e9f2e957eb7c91f6b7ccd372c836d18928bca0ec45573ad7950725a`. The native clock observed before writing was `2026-10-30T17:13:13-0700 PDT`; this is not an asserted file-creation time.

S2/S3 are nonblind, unadopted inputs; S4/S5 are used only at the adopted conditional location/profile interfaces; S6 is historical scope, not a black-box proof of Claim A; S1/S7 are the explicit physical-mate/alignment corrections. No outgoing source link, held episode or its proof/method/selection/planning/verification/reporting/confidence/downstream consumer, sibling artifact, old source code, or external source was opened. **CHILD SCIENTIFIC EXECUTION NOT RUN:** no solver, scientific program, CAS, test, build, lint, formatter, or finite search was run; no scientific source or run is proposed here. Hashing metadata and the exclusive creation of this written file are not scientific verification. No sampled historical run is used as proof, no source-identity claim is made, and parent independent review/disposition remains pending.
