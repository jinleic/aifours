# Four-distinct-D0 same-object obstruction: all anchor parities and all four characters

**NONBLIND GENERAL-AUTHOR WRITTEN CANDIDATE; NOT ADOPTED.** At the exact rank-two actual-caller imports and four-distinct-D0 subfamily stated below, I derive a contradiction from one physical `x,y`, `J=1`, all 64 U0 caps, the carried zero at the specified `t`, and all 64 U3 caps. The proof covers all four graph covectors simultaneously, including actual nonaffine D0-anchor arrays, not a sample or separate choices by frequency. The result is stronger than the even-multiplicity lemma, conditional on the explicitly stated three-cell actual-location conclusion. It requires a full independent reconstruction and a parent disposition. It says nothing about D0 allocations outside this subfamily, `V`, or original-caller/global completion. No execution was used.

## A. A self-contained signed-array theorem

All arithmetic in arguments of characters is over `F_2`. Let `I=B=F_2^2`, with dual `B*`; put `Q(v_0,v_1)=(v_1,v_0)`. Let `F:I->F_2` have odd total sum. For each of the four `i`, take an **actual** anchor `b_i in B`, a covector `kappa_i in B*`, and a sign `sigma_i`. Set

`v = sum_i b_i`, `g_i(b)=sigma_i (-1)^{kappa_i(b)}`,

and impose the single relation

`sum_i kappa_i = Q v`.                                                    (A1)

On the 64 coordinates `(ell,h,i,b)`, let one real array `Y` have the following values, all simultaneously:

1. On `ell=1`, `Y(1,F_i,i,b)=g_i(b)`, and on the mate plane `Y(1,1+F_i,i,b_i)=0` while `Y(1,1+F_i,i,b)=2 d_{i,b}` for `b!=b_i`, with one fixed sign `d_{i,b}` at each of the 12 sites.
2. On `ell=0,b=0`, for each fixed `i`, the two h-values are either both zero or both signs times 2. On `ell=0,b!=0` there are exactly six values of magnitude 2, one value of magnitude 4 at another site, and zeros elsewhere. The six magnitude-2 sites occupy **exactly three** distinct cells `(h,i)`, two sites per cell; their two b-coordinates in a cell are distinct. These are properties of one array, not separately chosen cells for different transforms.
3. `sum Y^2=128`, and all 64 unnormalized Walsh coefficients belong to `4+8Z`.

**Theorem.** Under 1–3 and (A1), not all 64 Walsh coefficients have absolute value at most 12. The theorem quantifies over *all* four covectors and arbitrary `b_i`, signs, the one magnitude-4 location, and `F` of odd parity. It does not assume affine anchors, an independently chosen sign per frequency, or an `H_local` condition.

### A.1. The anchor-dependent parity is nevertheless constant in alpha

Let `n` be the number of negative mate signs `d`, and for `alpha in B*` let `m_alpha` be the number of `i` with `kappa_i=alpha`. Define

`A_l(s,alpha,beta) = sum_{h,i,b} Y(l,h,i,b) (-1)^{s h+beta(i)+alpha(b)}`,

for `s in F_2`, `beta in I*`. The two full coefficients at the corresponding two ell-frequencies are `A_0+A_1` and `A_0-A_1`; consequently their two caps are equivalent to `|A_0|+|A_1|<=12`.

The graph contribution to `A_1` is `4 sum_{i:kappa_i=alpha} sigma_i (-1)^{s F_i+beta(i)}`, congruent to `4 m_alpha` modulo 8. For the 12 mate terms the product of their character signs is

`(-1)^{n+s+alpha(v)}`:

indeed `sum_i 3(1+F_i)=1`, `sum_i 3 i=0`, and `sum_i sum_{b!=b_i} b=sum_i b_i=v`. Thus the mate contribution is `4(n+s+alpha(v)) (mod 8)`, and

`A_1/4 = n+s+m_alpha+alpha(v) (mod 2)`.                                  (A2)

Set `tau_alpha=m_alpha+alpha(v) (mod 2)`. It is actually the **same** `tau` for every one of the four `alpha`. To see this, let `O={alpha:m_alpha odd}`. Its cardinality is even and `sum_{alpha in O} alpha=Qv` by (A1). If `v=0`, this forces `O` either empty or all four, so `tau` is respectively 0 or 1. If `v!=0`, `Qv!=0` and `O` has exactly two elements `a,a+Qv`: the empty set and the four-element set both have zero XOR. Since `(Qv)(v)=v_1 v_0+v_0 v_1=0`, both members have the same value on `v`. They therefore form one full two-element level set of `alpha(v)`, and `tau_alpha` is constant, either 0 or 1. No anchor alignment has been made.

### A.2. Full and partial Parseval force every mate sign

Assume for contradiction that all 64 U3 caps hold. Put `s_0=n+tau` and `s_1=s_0+1`. On the 16 `(alpha,beta)` at `s_0`, (A2) and the cap give `A_1 in {0,+8,-8}`. On the 16 at `s_1`, they give `A_1 in {+4,-4,+12,-12}`. At every triple, `A_0/4` and `A_1/4` have opposite parity because both `A_0+A_1` and `A_0-A_1` are 4 modulo 8.

Full Parseval gives `sum W^2=64*128`. Every capped `W` is `+/-4` or `+/-12`, so exactly eight of the 64 have magnitude 4. Let `E` count `s_0` triples with `|A_1|=8`, and `O` count `s_1` triples with `|A_1|=4`. Each such triple contributes at least one distinct magnitude-4 full coefficient: at an E triple `|A_0|=4`; at an O triple `A_0=0 or +/-8`. Therefore `E+O<=8`.

The ell=1 energy is `16+12*4=64`. Its five-bit Parseval identity gives

`4E + O + 9(16-O) = 32*64/16 = 128`, hence `O=2+E/2` and `E<=4`.

Now put `C=sum_{i,b!=b_i} g_i(b)d_{i,b}`. Taking the h transform first and applying Parseval over `(i,b)` yields

`sum_{alpha,beta} (A_1(s,alpha,beta)/4)^2 = 64+4(-1)^s C`.

At `s=s_0` its left side is `4E`, so `E=16+(-1)^{s_0} C>=4`, because C is a sum of 12 signs. Equality forces `E=4`, `O=4`, and, at **all 12 actual mate sites**,

`d_{i,b} = -(-1)^{s_0} g_i(b)` for `b!=b_i`.                             (A3)

At the other slice `s=s_1`, the h-transformed row is `(-1)^{s_1 F_i} g_i(b)[3-2*1_{b=b_i}]`; hence, with `w_i=sigma_i(-1)^{s_1 F_i}`,

`A_1(s_1,alpha,beta) = sum_i (-1)^{beta(i)} w_i [12*1_{alpha=kappa_i} - 2*(-1)^{(kappa_i+alpha)(b_i)}]`.  (A4)

This formula uses the same signs at every alpha and beta, including nonaffine anchors.

### A.3. Any repeated kappa is impossible

If some alpha has multiplicity two, choose beta so its two active signed `w_i` agree. This is possible because their two i-labels are distinct. Their contribution has magnitude 20; the other two terms have magnitude at most 2 each, so `|A_1|>=16`. For multiplicity three, the two independent differences between three distinct points of `I` let one choose beta making all three active signs agree, giving `|A_1|>=30-2=28`. For multiplicity four, every bracket in (A4) is 10, and four-point Parseval guarantees a beta with the signed sum of the four `w_i` of magnitude at least 2; hence `|A_1|>=20`. Every case violates `|A_1|<=12`, a necessary consequence of the *pair* of full caps.

Thus the four `kappa_i` must be distinct. In particular their XOR is zero. Equation (A1) and invertibility of Q then give `v=0`. A function on `F_2^2` is affine iff the XOR of its four values is zero, so the actual anchor map `i->b_i` is affine. Moreover every `m_alpha=1`, hence `tau=1`. This is a conclusion of the all-cap hypothesis, not an initial affine-alignment assumption.

### A.4. Distinct kappa and the same ell=0 array also contradict the caps

Only now use the invertible affine change `b'=b+b_i`, which is legal because the actual `b_i` have just been proved affine. It preserves `h,i`, the h-mate direction and the physical distinction of sites; it transports all 64 frequencies together. Write `g_i'(b')=sigma_i'(-1)^{kappa_i(b')}`. It merely permutes the 12 mate signs, so their negative count remains n. Since `tau=1`, `s_0=n+1` and `s_1=n`. Multiplying the 12 equalities (A3) in the aligned coordinates gives

`product_i sigma_i'=(-1)^n`,

because the product of a character over the three nonzero elements of B is 1. Thus, for `w_i'=sigma_i'(-1)^{n F_i}`,

`product_i w_i'=(-1)^n (-1)^{n sum_i F_i}=+1`.

A four-sign pattern has product +1 precisely when it is a constant sign times a character of `I`. Therefore there is a unique `beta_0` such that `w_i'(-1)^{beta_0(i)}` is constant. Equation (A4) simplifies to

`A_1(n,alpha,beta)=12 w'_{i(alpha)}(-1)^{beta(i(alpha))} - 2 sum_i w_i'(-1)^{beta(i)}`,

where `i(alpha)` is the unique row with `kappa_i=alpha`. For **each** of the four alpha, this has magnitude 4 at `beta=beta_0` and magnitude 12 at the other three beta. The same physical pair of caps therefore forces

`A_0(n,alpha,beta)=0` for all four alpha and all `beta!=beta_0`.           (A5)

Let `B_i(b')=Y'(0,0,i,b')+(-1)^n Y'(0,1,i,b')`. Inverting the full b'- and i-Walsh transforms in (A5) gives

`B_i(b')=(-1)^{beta_0(i)} B_0(b')` for every `i,b'`.                    (A6)

The prime means the very same array transported by `b'=b+b_i`. The six magnitude-2 Z sites occupy only three h,i cells, hence at most three i-rows. Pick an i-row with no such site. For every b' its `B_i` is 0 or has magnitude 4: at the shifted physical `b=0` both entries are zero or both are `+/-2`, while at physical `b!=0` its only possible nonzero is the unique `+/-4` site. By (A6), **all** `B_i(b')` must have magnitude 0 or 4.

Suppose a magnitude-2 Z site has no magnitude-2 site in the other h-cell at the same i and the same physical b. The other entry is then 0 or the unique `+/-4` site, so their signed h-sum has magnitude 2 or 6, contradiction. Consequently every such Z site has a magnitude-2 partner at the same i,b and opposite h. Each occupied `(i,h)` cell therefore has its opposite `(i,h+1)` cell occupied as well. The occupied cells must come in pairs, contradicting the stipulated **three** occupied cells. This completes the proof of the theorem.

## B. The actual four-distinct-D0 consumer, explicitly conditional

The named actual imports are those in packet S4/S5: the m116 five-span physical common inverse, rank-two quadratic `f`, `q(b)=1+b_0 b_1`, bent `f+q`, and common bent graph phases `R` and `R+f`; all U0 divisibilities and caps; the specifically carried original-DC balance `t` with `xhat(t)=0`; and the actual four D0, one in each graph L-coset. The adopted location/profile results also have the **explicit local `H_local=0` import** in S4/S5. I do not verify that import here and do not infer it from another condition. The purely array theorem above does not itself use or assert `H_local`.

At those imports, write `K=rad(B_f)` and use its bijective projection to physical b, as in S1/S5. Write the unique radical vector over b as k(b); `d(b)=f(z+k(b))+f(z)` is linear. In the global linear coordinates `z=(i,0)+k(b)`, `h'=h+d(b)`, the graph is `h'=F_i=f(i,0)` with `sum_i F_i=1`. The actual D0 in row i has physical b-coordinate `b_i`; the four graph exceptions have actual coordinates `gamma_i=b_i+Delta_i`. The adopted location theorem S4 gives `i->Delta_i` affine, in both its 1+1+1 and 2+1 alternatives, and gives exactly the three occupied ell=0 H-cells with two Z2 points apiece. No condition on their signs is inferred from location.

The graph phase restriction `R_i(b)=R((i,0)+k(b))` is affine in b, with its four linear covectors `lambda_i` forming a bijection. Here is the needed argument. For each alpha put `V_i=sum_b (-1)^{R_i(b)+alpha(b)}`. Bentness of R gives all four i-Walsh transforms of V magnitude 4; bentness of R+f, using the shifted b-covector `alpha+d`, gives the same for `((-1)^{F_i}V_i)_i`. In particular `sum_i V_i^2=16`. A Boolean function of two bits has either one Walsh value of magnitude 4 and three zeros (affine), or four values of magnitude 2 (nonaffine). If one row were nonaffine, the 16 energy forces all four `V_i=+/-2`; their i-sign product must then be -1 for the first transform to be flat. Multiplication by `(-1)^{F_i}` flips that product, so the second transform cannot be flat. All rows are affine; energy then gives exactly one row per alpha. A bijection of the four points of `F_2^2` is affine, so `i->lambda_i` is affine.

With `X=(-1)^t x` and `Y=(-1)^t y`, the physical graph equation remains `Y=-a g X`. The actual weighted graph pattern is `X=epsilon_i(2*1_{b=gamma_i}-1)`. Multiplying it by the actual graph factors `a=(-1)^R` and `g=(-1)^{1+b_0 b_1}` gives a signed character with

`kappa_i=lambda_i+(1,1)+Q gamma_i`.

Indeed `1_{b=gamma}=(1+b_0+gamma_0)(1+b_1+gamma_1)`, so its quadratic term cancels `b_0 b_1` and leaves linear part `(1,1)+Q gamma`. Summing over the four rows and using affine lambda and Delta yields precisely (A1), with the **actual** `v=sum b_i`. On graph mates, the actual D0 value is 0 and the other three values are signs times 2. On ell=0, the two entries at physical b=0 in each row are both 0 on the F row or both signs times 2 on an E row; outside that b there are the six physical Z2 sites, one Z4 site and zeros. The structural energy is `16+18*4+6*4+16=128`.

It remains to show that `J=1` supplies the 64 residues, rather than assume it. Use the physical inverse `4u(c,0)=x(c)+3a(c)+g(c)+y(c)`. At every frequency, `ahat=+/-4` because R and R+f are bent, and `xhat=0 (mod 8)` by the actual U0 divisibility. To compute g, first use the original physical `(j,b)` coordinates: the graph and mate contributions are `[1-2(-1)^s]` times the Walsh transform of `(-1)^{q+s f}`. For `s=0`, that transform is a multiple of 8 because q depends only on b and its two-bit transform is `+/-2`; the ell=0 F/E contribution is `12-16*1_{beta=0}`, congruent to 4 modulo 8. For `s=1`, the ell=0 contribution vanishes and bentness of `f+q` makes the graph/mate contribution `+/-12`, also 4 modulo 8. Therefore `3 ahat+ghat=0 (mod 8)` at every frequency. Since u is ternary, its signed Walsh sum is congruent modulo 2 to the number of nonzero entries of `u(c,0)`. Thus

`yhat(xi)=4J (mod 8)` for every physical frequency xi.

For the **given** t, not an after-the-fact zero, `Y=(-1)^t y` translates the full spectrum by t and has the same cap and residue. Apply the array theorem to that same `X,Y`. This proves the advertised conditional no-go within the exact four-distinct-D0 subfamily, pending independent review. It does not prove any other D0 allocation impossible or supply a common V.

## C. Full affine-coordinate issue, including h-into-b shears

The statement in S1 that the particular row translation `b->b+b_i` is not affine for nonaffine `b_i` is correct as written; it is **not** a proof that no ambient affine map can make the D0 b-coordinates coincide. Indeed, when `v=sum b_i!=0`, the function `i->b_i+v(1+F_i)` has zero four-value XOR and is affine. Choose its affine interpolation `L i+c` and set

`b'=b+v h'+L i+c`, leaving `ell,h',i` unchanged.

This is an invertible affine map. It sends every actual D0 anchor to `b'=0`, while sending every paired graph anchor to `b'=v`; the physical h-mate vector becomes `(Delta h',Delta b')=(1,v)`. Thus the desired h-into-b shear exists, but it does **not** put both graph and mate anchors at the same b-coordinate as required by the aligned lemma. Undoing the b-part of the mate direction restores a nonaffine row anchor.

There is also an invariant statement under the **entire** ambient invertible affine group, not only this shear. In the radical coordinates, the XOR of the four actual D0 points is

`sum_i D_i = e+H(v)`,

where `e` is the physical mate vector and `H(v)` is the radical-lift vector with b-projection v. For an arbitrary affine bijection `P(c)=Mc+a`, the four-point XOR transforms to `M(sum_i D_i)` and the physical mate vector to `M e`; the defect `(sum_i D_i)+e=H(v)` therefore transforms to `M H(v)`. A standard form in which all D0 anchors have b=0, their graph mates have the same b=0, and the graph row function has odd parity necessarily has `sum_i D_i=e`. Thus v!=0 cannot be put in **that specific standard aligned form** by any invertible ambient affine map. This does not forbid other useful affine normal forms. The preceding proof does not rely on this invariant as a substitute for the nonaffine calculation.

Exact transport: for `c'=Mc+a`, all physical arrays, including a,g,x,y and u, are pulled back by `P^{-1}`. Their Walsh transforms satisfy `W'(xi')=(-1)^{xi'(a)} W(M^T xi')`; the specified balance frequency becomes `t'=M^{-T}t`, with the corresponding affine modulation phase `t(P^{-1}c')`. Zero, magnitude caps, divisibility by 8, and residue 4 modulo 8 are preserved; the scalar sign from an affine translation cannot change 4 modulo 8. The parity J is unchanged by the common permutation of spatial points at fixed w. This is not a claim that the physical inverse is modulated by t or that a,g can be left untransported under an affine coordinate change.

## D. Coverage, historical qualification, and assurance

After direct PREBODY ACK, I read the sole packet in ascending serial raw windows of at most 20 LF, all LF 1–621 through the ending, before any research or comparison. It contains complete S1 197 LF (`74a5f0cbec49ecabc63e33bdfdc20937092eb5faaef2616c5874533c0eb5adc3`), S2 3 LF (`96195b75b83e0f2d91f71849238f58808fb31c8803ed1439c67cb5e91587371f`), S3 206 LF (`a3e060e7564d91f0539c7bb9eb7b8603210617680c1e0ec8fb6bc26862210dca`), S4 30 LF (`fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a`), S5 37 LF (`44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`), S6 17 LF (`ba7cc22c99c615a0674d04ea827d90527494cfb0956452d8ad9588a885fd71f0`), S7 42 LF (`c863d8aed5ad610cc4854391f7efe5eb544fab36cd924e0a8a7ced43ff772e30`), and S8 55 LF (`20b2bebb3cd3a0e93772a1160ff87a8b0dcfe3c658d575b7b366630f0a74cb0a`); these source hashes are the supplied bindings, not direct rereads of those source paths. Packet SHA observed `ab1dde98809fd53370935e3e2188de5e83e3432d9ed50624aff68d83b8e3cde9`.

Before ACK I read the complete manifest, freeze receipt, final binding, parent-live metadata, actual dispatch and all **21** listed controls through their endings. Observed metadata SHA256: manifest `ef120d4606b8677bfe1f3e9192d68df16a7194f6ec2d89ee86b95fa526122185`; freeze `ef6e757706b54b6fdf5e673d5167b2c142fc1e73e702cdcd25115dcd4dda849b`; final binding `7056bc30ecc2490959b6a3b961e249abc60407b9309578659538df6a27122a57`; metadata `501ac5c468f6b75fd5733c1b01681885303b3481dcdf933b218a11c9620d2170`; actual dispatch `216a1211cafb85501f606099f96fe1a6ba9c9980c009484386a64b8f24ca81d8`. The native clock observed during work was `2026-10-30T17:01:23-0700 PDT`, not a claim about exact file creation time.

S1/S3 are complete but unadopted and nonblind inputs; their even-kappa results are not used as a black-box premise above. S6 records the f689 explicit-example correction. The historical f710 v1 actually FAILED (193 failed checks); v2 was one corrected bounded run, not all signs or a U3 witness. None of the present theorem depends on treating either run as exhaustive. All held episodes and their proof/method/selection/planning/verification/reporting/confidence/downstream consumers were NONINPUT. No old link, held payload/history, old code, sibling artifact or external source was opened. **CHILD SCIENTIFIC EXECUTION NOT RUN:** no solver, CAS, finite program, test, build, linter, formatter, or scientific calculation tool was run. Metadata hashes and exclusive artifact creation are not scientific verification. No claim of parent acceptance, source identity, novelty, external-model-family, human or kernel/formal verification is made.
