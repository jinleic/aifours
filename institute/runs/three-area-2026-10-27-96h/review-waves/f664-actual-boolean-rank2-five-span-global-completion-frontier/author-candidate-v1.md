# Actual five-span rank-two completion: exact U0 profiles and a cross-fibre subfamily obstruction

**Author result; not independently reviewed or parent-adopted.** For the actual normalized five-span branch, I give an exact seven-profile characterization of the entire capped, carried-balanced U0 spectrum. In the subfamily where the four physical D0 blocks occupy the four distinct radical cosets, I prove global constraints on the actual six Z2 blocks, their signs, the common U3 graph values, and the eight small U3 frequencies. In particular, the Z2 population in each of the three physical nonzero b-rows must be exactly two. This excludes every physical configuration in this subfamily with a different row census, for every permitted phase and every specifically transported balance t. A concrete common physical u below shows that this exclusion is not merely the local count, divisibility, J, or prescribed-zero condition.

**Not proved:** existence or nonexistence of a full U0/U3/V completion, even in this subfamily; the remainder of the rank-two branch; a balanced original nine-variable caller; or global NL242. No novelty, source-equivalence, independent-family, human, or formal/kernel acceptance is asserted. The proof is conditional on the four frozen source interfaces and their stated actual-caller normalizations, not on any held science.

## 1. Same physical object and input boundary

The only scientific inputs are the complete four original-input bodies S1–S4 in `literal-packet-v1.md` (parent-supplied packet SHA-256 `c58ebaac67be54400b3bdb71cfefa24928913b7d5f5d66c3a05c97c68fb5ae23`); S4 is a separate six-span source and is **not** used as a five-span hypothesis. In particular, S1 supplies the actual rank-two zero-flat direction and its all-shift equivalence, S2 supplies the actual common four-fibre counts, divisibility criterion and complementary interface, and S3 supplies the actual common graph/phase normalization. These are imports with their own recorded scopes, not newly independently checked here. No link in the packet was followed.

Use `c=(ell,h,j,b)` with `ell,h` bits and `j,b` in F2^2. This is the same physical basis as S1. For an explicit identification with S3, let `d_00=1, d_10=2, d_01=4, d_11=7` in F2^3 and set `d=ell*d_00 + b_0*(d_00+d_10) + b_1*(d_00+d_01)`. Thus `d=0` is exactly `ell=0,b=0`, while `ell=1` gives the four actual B-cosets. The full-block direction `e` toggles h. Write `z=(j,b)`, and

\[
S=\{(1,f(z),z):z\in\mathbb F_2^4\},\quad q(b)=1+b_0b_1,
\quad \rho_b=(-1)^{q(b)}.
\]

Here f is quadratic with polar rank two; `f+q`, r and `r+f` are bent. The actual arrays are `a=1_S(-1)^r`, and g is 4 on the two full blocks `F={(0,h,0,0):h in F2}`, −2 on the other six blocks of `ell=0,b=0`, `rho_b(-2+3*1_S)` on `ell=1`, and zero on the remaining 24 blocks. Thus the 22 D blocks are the six nonfull blocks in that E row and the 16 graph mates `S+e`; the 24 Z blocks are `ell=0,b!=0`. On the **same** ternary u,

\[
u(c,w)=\frac{x(c)+3a(c)\chi_1(w)+g(c)\chi_2(w)+y(c)\chi_3(w)}4,
\quad \chi_3=\chi_1\chi_2,\quad x=U_0,\ y=U_3.
\]

The physical forms and counts are: graph blocks `(x,y)=(±1,−agx)`; F blocks `(0,0)`; four D0 `(±2,0)` and 18 D3 `(0,±2)`; six Z2 `(±2,±2)`, one Z4 `(0,±4)` and 17 Z0 `(0,0)`. Signs are physical signs of this same inverse; no independent spectra are substituted. Let P be the negative-x graph points, W the ten D0/Z2 x-support points, and N the negative-x points in W. S2's actual rank-two divisibility criterion is

\[
|P|\text{ even},\qquad |P|/2+|N|\text{ odd},\qquad X_P=X_W.\tag{C}
\]

The transformed balance t below is the **specified image of original DC**, not a freely chosen zero. The original selected nonzero T, original gauge, rank/eight-zero and other actual-caller requirements remain part of the unpaid full caller.

## 2. Radical geometry forced by the original bent conditions

Let `B_f` be the polar form and `K=rad(B_f)` in the four z coordinates. Then `dim K=2`. Define the linear derivative `d_f(k)=f(z+k)+f(z)`, independent of z for k in K. The physical subspaces are

\[
L=\{(0,h,k):h\in\mathbb F_2,\ k\in K\},\qquad
H=\{(0,d_f(k),k):k\in K\}\subset L.
\]

Thus `L=H+<e>` and `H` is a two-space. Every one of the four ell=1 L-cosets contains an affine H-plane of four graph points and its e-translate of four D blocks. Let `lambda` in `L*` be zero on H and one on e.

The projection `K -> F2^2_b` is an **isomorphism**. Also `(r+q)|_(z+K)` has nondegenerate polar form on K for every z. Proof: choose a basis `(u,v,k1,k2)` with `(k1,k2)` a basis of K and `B_f(u,v)=1`. In dimension four, a quadratic is bent exactly when its alternating polar matrix has Pfaffian one. Since `f+q` is bent and both B_f and B_q have rank two, `Pf(B_f+B_q)=B_q(k1,k2)=1`. But `B_q(k1,k2)` is the determinant of their b-projections, proving the projection is invertible. Similarly, `Pf(B_r)=Pf(B_r+B_f)=1` implies `B_r(k1,k2)=0`; hence `B_(r+q)(k1,k2)=1`. Affine additions do not change these conclusions. In particular, every ell=0 affine H-cell contains exactly one E-row block `b=0` and three Z blocks, one at each nonzero b.

## 3. Exact global U0 spectrum as seven sparse profiles

Choose a linear complement `M` to L in the physical six-space, and identify its eight elements with the L-cosets. Extend each `eta in L*` by zero on M, and each `q0 in M*` by zero on L. For a fixed x and the actual carried frequency t define

\[
Z_m(\eta)=\frac14\sum_{v\in L}x(m+v)(-1)^{t\cdot(m+v)+\eta(v)}.
\tag{1}
\]

**Theorem 1.** Under the actual rank-two graph, physical count/energy and U0-divisibility hypotheses, the full U0 cap `|x-hat|<=8` and the specified balance `x-hat(t)=0` hold **if and only if** all the following are true:

1. `Z_m(0)=0` for all eight m;
2. all `Z_m(eta)` are integers; and
3. for each of the seven nonzero eta, either exactly one `Z_m` is `+2` or `−2` and the rest are zero, **or** exactly four are `+1` or `−1`, their four m form an affine two-flat of M, and the product of their four signs is −1.

This is an exact condition on the **same physical x** and all 64 frequencies; it does not assert that any choices meet it.

*Proof.* In the forward direction S1's actual zero-flat theorem gives the eight zero frequencies exactly `t+L^perp`. Fourier inversion on M gives `Z_m(0)=0`. For any eta, subtract the eta=0 sum inside (1). Modulo four, the difference is twice the parity of the intersection of the hyperplane `eta(v)=1` with the odd support of x. That odd support is either empty or an affine H-plane in each L-coset, and such an intersection has size 0, 2, or 4. Thus all Z are integral. Further,

\[
\widehat x(t+\bar\eta+\bar q_0)=4\sum_{m\in M}Z_m(\eta)(-1)^{q_0(m)}.\tag{2}
\]

At nonzero eta all eight left sides are ±8; Parseval on M yields `sum_m Z_m(eta)^2=4`. Integer solutions are exactly one ±2 or four ±1. Four points in F2^3 are either an affine plane or affinely independent. On four affinely independent points any assigned signs extend to an affine character, producing an absolute sum 4 in (2), which is forbidden. On an affine plane, sign product +1 likewise extends to a character and is forbidden; sign product −1 makes every character sum ±2. Conversely, condition 1 makes all of `t+L^perp` zero; the two alternatives and (2) make every other coefficient ±8, proving both the cap and the original carried balance. QED.

Theorem 1 provides a literal replacement for U0's 64 spectral checks only **after** its actual physical and divisibility hypotheses; it does not replace U3, the odd half, or the original T/rank conditions.

## 4. Four-distinct-D0 subfamily: full physical support obstruction

Assume now that the four D0 points lie in **four different ell=1 L-cosets**, one in each. This is an explicit subfamily, not a claim that all actual rank-two callers have this property. Let `D_i` denote these four points and set `epsilon_i=chi_t(D_i)*x(D_i)/2`.

**Theorem 2.** If an actual member of this subfamily satisfies the full U0 cap and its specifically carried balance, then:

(a) the six Z2 blocks split into three two-point sets, each contained in one ell=0 affine H-cell; in each pair the two signs of `chi_t*x/2` are opposite;

(b) the three pair differences are precisely the three distinct nonzero vectors of H. Consequently each nonzero physical b-row contains **exactly two** Z2 blocks, and the XOR of all six Z2 points is zero;

(c) `product_i epsilon_i=+1`. In particular, using (C), `X_P=X_{D_1,D_2,D_3,D_4}`;

(d) on each of the four actual graph H-planes, the same physical y is a signed affine character of H.

*Proof.* Balance on each L-coset says the four weighted graph signs sum to `−2 epsilon_i`. Since the graph plane and its mate have opposite lambda values, (1) gives `Z_i(lambda)=±1` on each of the four ell=1 cosets. Theorem 1 gives column squared norm four, so all four ell=0 values `Z_m(lambda)` are zero. Together with `Z_m(0)=0`, this says the weighted x sum vanishes separately in each ell=0 H-cell. All four D0 points are on ell=1, so x on ell=0 is supported only by the six Z2 points. By Section 2, each cell has just three possible Z points; its selected number is therefore even and is 0 or 2. This proves (a) and gives three occupied cells.

For any nonzero `alpha in H*`, choose an extension `eta in L*`. The four weighted graph signs in each ell=1 slice have sum ±2 and hence form a three-to-one sign pattern, so their H-Walsh coefficient at alpha is ±2. The single D0 mate contributes ±2; the two values at eta and `eta+lambda` are therefore one zero and one ±4. Their combined contribution to `sum_m Z_m(eta)^2+sum_m Z_m(eta+lambda)^2` is one per ell=1 coset, total four. The two column norms total eight. On an ell=0 cell, an opposite-sign Z2 pair contributes a normalized coefficient ±1 precisely when alpha is nonzero on that pair's difference; it contributes zero otherwise. Combining the two cells of any L-coset at eta and `eta+lambda` doubles the sum of their individual squares. Hence exactly two of the three pair differences are nonzero under every nonzero alpha. In a two-space this forces one copy of each nonzero direction. Since `K -> b` is an isomorphism, every cell contains the three nonzero b-values once. A pair's b-difference is the third nonzero b-value, so the three different directions imply exactly two Z2 points in each nonzero b-row. Their three pair XORs sum to zero. This proves (b).

For (c), the lambda column has its four nonzero entries on the affine ell=1 plane of M; Theorem 1 requires their product to be −1. Extending lambda by zero on M, those signs are `epsilon_i*(-1)^lambda(D_i)`. The XOR `X_D` of the four D_i lies in L and satisfies `lambda(X_D)=1`: if their z-coordinates represent all four K-cosets, write them as `z00+s*u+t*v+k_st`. Then `sum f(z_st)+d_f(sum z_st)=B_f(u,v)=1`. Thus the lambda factors have product −1, so the epsilons have product +1. The rank-two (C) and the zero Z2 XOR give `X_P=X_D`.

For (d), the zero-sum equation with one D0 makes `chi_t*x` on each four-point graph plane a 3/1 sign pattern. Multiplication by the restricted character chi_t does not change its nonzero quadratic polar, so x itself is bent on each plane. Section 2 says `ag=(-1)^(r+q)` on S is also bent on each corresponding K-plane. Their two quadratic polars are the same unique nonzero alternating form in dimension two. Thus `y=-agx` is a signed affine character there. QED.

The row-census part of (b) excludes **all** physical D0-distinct configurations whose six Z2 points have any row count other than `(2,2,2)`, uniformly over graph f, common phase r, all choices of physical signs, and the actual t. It is a necessary condition, not a claim that the remaining positions or signs work.

## 5. The U0-to-U3 bridge on the same u

Let the hypotheses of Theorem 2 hold, and additionally impose the actual J=1 residue and **all 64** U3 caps. Thus, with the actual U3 energy 128,

\[
B=\{\xi:|\widehat y(\xi)|=4\}\quad\text{has size }8,
\qquad |\widehat y(\xi)|=12\text{ outside }B.
\]

**Theorem 3.** For every `alpha in H*`, the number

\[
n_\alpha=|\{\xi\in B:\xi|_H=\alpha\}|
\]

is odd. Consequently, up to order, the four counts are exactly `(5,1,1,1)` or `(3,3,1,1)`. This is a necessary constraint on the **actual U3 small-frequency set**, not a constructed U3 spectrum.

*Proof.* The energy/count statement follows from `64*128=16|B|+144(64-|B|)`. For nonzero `v in H`, the graph contribution to `A_y(v)=sum_c y(c)y(c+v)` is `4 sum_i (-1)^{kappa_i(v)}`, where the four kappa_i are the signed-character slopes from Theorem 2(d); this is a multiple of 8. H preserves S and its complement, and every y-value off S is even; pairing `c` and `c+v` makes the complementary contribution a multiple of 8 too. On the other hand Fourier inversion gives

\[
A_y(v)=-2\sum_{\xi\in B}(-1)^{\xi(v)}\quad(v\ne0).\tag{3}
\]

Writing `N_v=|{xi in B:xi(v)=1}|`, the divisibility by eight and `|B|=8` imply N_v is even for every nonzero v. The three equations and total eight imply all four n_alpha have the same parity.

To determine that parity, sum `A_y(v)` over the three nonzero v of H modulo 16. On each graph H-plane the sum over these shifts is 12 for zero slope and −4 for nonzero slope. Across four planes this is divisible by 16. Off S, an unordered pair of points in one H-cell contributes twice their y-product. Such a contribution is 8 modulo 16 exactly when both absolute y-values are 2; a zero or a magnitude-4 value contributes zero modulo 16. Each ell=1 D-mate cell has three D3 magnitude-two points, yielding `4*binom(3,2)=12` such pairs. On ell=0, each of the three occupied Z2 cells has two Z2 magnitude-two points and at most one E-row magnitude-two point, so contributes `binom(2,2)` or `binom(3,2)`, both odd. Every other cell has at most one magnitude-two E point. Thus the total number of such pairs is odd and

\[
\sum_{0\ne v\in H}A_y(v)\equiv8\pmod{16}.
\]

Equation (3) evaluates this same sum to `16−8 n_0`, because a zero restriction contributes 3 and every nonzero restriction contributes −1 to `sum_{0!=v in H} (-1)^{xi(v)}`. Hence n_0 is odd and, by the already-established common parity, every n_alpha is odd. Four positive odd integers summing to eight have the two stated multisets. QED.

## 6. Explicit physical non-witness showing strictness

This is a hand-derived construction, **not** scientific execution, and it is expressly not a full caller. Take

\[
f=j_0j_1,\quad r=j_0b_0+j_1b_1,\quad \beta=(1,0),\quad \gamma=(0,1).
\]

Then K is the b-plane and H is its lift with h=0. The three required bent facts follow directly: summing first over b gives magnitude 4 for the Walsh transforms of both r and r+f, and the Walsh transform of `f+q=j_0j_1+b_0b_1+1` factors into two two-bit transforms of magnitude 2.

For every j choose D0 at `(1,1+f(j),j,0)` and give it x0=−2. On S give x0=−1 at the four graph points with `(j,b)=(0,beta)` or `(j,b)=(j,0)` for each nonzero j; give x0=+1 on the other twelve graph points. On Z, for each `j in {0,beta,gamma}`, give x0=+2 at `(0,0,j,gamma)` and x0=−2 at `(0,0,j,beta+gamma)`. Set x0=0 everywhere else. These are exactly four D0 and six Z2 blocks, and the latter have b-row counts `(0,3,3)` in the order `(beta,gamma,beta+gamma)`.

Here `|P|=4`, `|N|=7`, and `X_P=X_W=e+beta`; hence (C) gives every x0 Walsh coefficient divisible by eight. Every L-coset has sum zero: on ell=1 its graph signs sum 2 and the D0 is −2, while the three nonempty ell=0 slices contain opposite Z2 pairs. Thus `x0-hat` vanishes on `L^perp`. But at the b1 frequency, each ell=1 j-slice contributes −4 and the Z2 pairs cancel, giving **`x0-hat(b1)=−16`**, so the U0 cap fails. For the actual specified t set `x_t(c)=(-1)^{t dot c}x0(c)`; its local t-weighted sums are still zero, its Walsh coefficients are still divisible by eight, and `x_t-hat(t+b1)=−16`.

This x_t extends to one genuine common physical ternary u with the stated support/energy/zero counts: use the above f,r,a,g, put `y=-ag*x_t` on S, y=0 on F and D0, y=+2 on all D3, initially `y=x_t` on Z2, y=+4 at `(0,0,beta+gamma,gamma)`, and y=0 on Z0. If this initial inverse has even `J=|{c:u(c,0)!=0}| mod 2`, negate y at the Z2 point `(0,0,0,gamma)`; otherwise do nothing. That one change toggles J without changing any counts or x. Each inverse block is ternary: on S, writing `s=a*chi1` and `t'=g*chi2`, it equals `(3s+t'+x_t(1-st'))/4`; on D and Z it is one of the listed actual forms. Therefore support is 116, x energy 56, y energy 128, y has 23 spatial zeros, J=1, and S2 gives the U3 residue 4 modulo 8. The carried x balance is at the prescribed t. Nevertheless the explicit U0 coefficient −16 proves it is **not** a capped even half, and no U3 cap, complementary v, original T/rank certification, or Boolean witness is claimed. This construction also directly exhibits a prohibited row census under Theorem 2.

## 7. Literal unpaid completion and first blocker

The seven-profile condition pays the U0 cap/balance **only** for an actual x obeying the graph and local physical hypotheses. The full residual remains the following same-object existential problem, with no dropped quantifier or freely reselected original balance:

1. Choose an actual rank-two quadratic f and common phase r satisfying all three bent conditions; retain the actual physical F, D and Z blocks, signs, count table, local H=0, original transported t, and (C). Choose x so that all seven profiles of Theorem 1 hold, not just the t-zero or the illustrative example. The unrestricted D0 allocations include cases other than the four-distinct subfamily.
2. On **that same** graph and x, choose y using the physical inverse, including `y=-agx` on S, the actual D3/Z2/Z4 values, J=1 and all 64 `y-hat in {±4,±12}`. In the four-distinct subfamily the b-row census, weighted signs and all four odd projection counts of B proved above are compulsory, but they are not sufficient. The first unproved step is a simultaneous choice (or uniform contradiction) for these seven U0 profiles and all y signs/caps, together with every original rank, atom and cross-fibre restriction at its actual import scope.
3. On the **140 zero positions of this very u**, choose `v=±1`, with an odd number of negative signs, such that all 256 actual odd-half Walsh coefficients satisfy `|v-hat|<=14`. Do not substitute a different support or a numerical tally for signed coefficients.
4. Restore the original common coordinate/gauge map, its specified t and selected nonzero T, the original balance and all remaining original Boolean/rank/eight-zero/selected-T conditions; then use the actual pairwise inverse. Neither a projected x nor the necessary U3 condition supplies this reconstruction.

No instance meeting steps 1–4, and no contradiction covering all their choices, is established here. In particular, Theorem 3 does not rule out either of its two allowed multiplicity patterns. The exact remaining obstruction is the joint signed seven-profile/U3-cap system, followed by the fixed-complement 256-cap system and original-coordinate caller checks.

## 8. Chronology, assurance, and independent gates

Before scientific packet exposure I read the entire f664 manifest, freeze receipt, parent-live metadata supply, actual dispatch receipt and all listed status/permission controls through their endings, then sent the direct PREBODY ACK to Main. I subsequently read the entire 190-LF literal packet in order, in RAW slices of at most 20 LF; no packet link or held payload/consumer was followed. The native clock `2026-10-30T15:32:52-0700 PDT` was observed after that read, `2026-10-30T15:40:42-0700 PDT` during written derivation, and `2026-10-30T15:41:52-0700 PDT` before creation of this candidate. Exact private start/end times are not asserted. Parent-supplied input hashes and historical finite-run descriptions remain attributed to the parent; no new child hash verification is claimed.

All new algebra and the displayed explicit example are written reasoning. CHILD SCIENTIFIC EXECUTION NOTRUN: no code, CAS, solver, experiment, build, lint, test, formatter, or external-model CLI was run; only administrative line counting and native clock commands were used. No computational source or parent GO is proposed here. All earlier held episodes and their consumers remain NONINPUT. This file itself is a new author candidate, not a proof acceptance: independent full-scope mathematical reconstruction and the parent's separately recorded disposition are still required. No unobservable cognitive-isolation certificate is claimed.
