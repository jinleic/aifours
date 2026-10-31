# Actual Boolean five-span rank-two cross-fibre restrictions: independent written reconstruction

**Status: new author proof candidate, not an adopted verdict.** For the named actual five-span caller, assume the four D0 blocks occupy four different `ell=1` radical cosets, all U0 coefficients satisfy their cap, and the *specified transported original balance* holds. I reconstruct the radical and U0 profile arguments and derive the same-object D0/Z2, sign and graph-U3 restrictions below. With J=1 and all U3 caps added, all four restriction counts of the actual magnitude-four U3 frequencies are odd. A completely specified 256-entry physical inverse shows that the row-census restriction is not a consequence of the local counts, residue/divisibility, J and carried zero alone. **Neither this necessary-condition theorem nor that countercontrol supplies a common capped U0/U3 solution, complementary V, or original Boolean caller.**

## 1. Exact imported interface and the actual object

The input is the complete f677 frozen `literal-packet-v1.md` (parent freeze SHA-256 `14d3eddd712c29ac7deccae411204f3decf65bc7d72d821ee72c0f30bf0c8229`): its outer S1 is the complete, **unadopted** f664 author candidate, SHA-256 `4ba235c01fbab59e0829c5b6a38283a56ea7b0454ab95cac661c592130bb655f`; outer S2 contains the four complete original-interface bodies in the prior frozen packet, SHA-256 `c58ebaac67be54400b3bdb71cfefa24928913b7d5f5d66c3a05c97c68fb5ae23`. The mathematical inputs I use are the original-interface S1 rank-two zero direction/transported-balance statement, S2 common physical counts/divisibility/J/complement interface, and S3 common graph/phase normalization. These are imports at their stated scopes, not newly certified original-book equivalences. Original-interface S4 concerns six-span and is **not** a hypothesis for the five-span proof. No linked source was followed. I saw the f664 theorem statements, proof and countercontrol before deriving this reconstruction, so this is neither a blind discovery nor an independent-family check.

All variables below are over `F2` unless identified otherwise. Let `c=(ell,h,j,b)` with `ell,h` bits and `j,b` two-bit vectors; let `e=(0,1,0,0)` toggle h. For the same normalized five-span physical object set

\[
 S=\{(1,f(j,b),j,b):j,b\in F_2^2\},\quad q(b)=1+b_0b_1,\quad \rho_b=(-1)^{q(b)}.
\]

The quadratic graph f has polar rank two, while `f+q`, `r`, and `r+f` are bent. The physical `a` equals `(-1)^r` on S and zero off S. The physical g equals 4 at the two full blocks `F={(0,h,0,0):h=0,1}`, equals -2 on the six other `ell=0,b=0` blocks, equals `rho_b(-2+3 1_S)` at `ell=1`, and is zero on the 24 blocks `ell=0,b!=0`. Consequently g is `rho_b` on S and `-2 rho_b` on its 16 graph mates. The 22 D blocks are those 16 mates and the six nonfull E-row blocks; the 24 Z blocks have `ell=0,b!=0`.

For the *same* ternary `u(c,w)`, `w in F2^2`, let `chi1,chi2` be the independent two-bit characters and `chi3=chi1 chi2`:

\[
 u(c,w)=\frac{x(c)+3a(c)\chi_1(w)+g(c)\chi_2(w)+y(c)\chi_3(w)}4,
 \qquad x=U_0,\quad y=U_3. \tag{1}
\]

On S, `x=±1` and `y=-agx`; on F, `(x,y)=(0,0)`; the D blocks comprise four D0 with `(x,y)=(±2,0)` and eighteen D3 with `(0,±2)`; the Z blocks comprise six Z2 with `(±2,±2)`, one Z4 with `(0,±4)` and seventeen Z0 with `(0,0)`. Thus `sum x^2=56`, `sum y^2=128`, and `u` has support 116. Let P be the negative-x graph points, W the ten D0/Z2 points supporting x, N the negative-x points in W, and `X_A` the XOR of a finite set A. The imported rank-two criterion, with the signs of this actual x, is the equivalence

\[
 \widehat x\in8\mathbb Z\text{ at all 64 frequencies}\quad\Longleftrightarrow\quad
 |P|\text{ even},\quad |P|/2+|N|\text{ odd},\quad X_P=X_W. \tag{C}
\]

The normalized balance frequency `t` throughout is the *specified image of original DC under the common normalization*, not a newly chosen zero. The source's actual rank-two zero-flat implication says that the cap `|x-hat|<=8`, divisibility, and `x-hat(t)=0` force the eight zeros to be `t+L^perp`, with L defined below. It does not itself pay any U3 or V condition.

## 2. Radical geometry, with the load-bearing calculation

Let `B_f(z,z')=f(z+z')+f(z)+f(z')+f(0)` and `K=rad(B_f)`. Since the polar rank is two in four variables, `dim K=2`. For `k in K`, `d_f(k)=f(z+k)+f(z)` is independent of z and linear in k. Put

\[
 L=\{(0,h,k):h\in F_2,\ k\in K\},\qquad
 H=\{(0,d_f(k),k):k\in K\}.
\]

Then `L=H+<e>`, with H a two-space. We prove that the projection `K -> F2_b^2` is an isomorphism and that `(r+q)` has nondegenerate polar restriction to K. Choose a basis `u,v,k1,k2`, with `k1,k2` a basis of K and `B_f(u,v)=1`. For any four-dimensional alternating form A in this basis,

\[
 \operatorname{Pf}(A)=A_{uv}A_{k_1k_2}+A_{uk_1}A_{vk_2}+A_{uk_2}A_{vk_1}.
\]

A four-variable quadratic is bent exactly when its polar is nonsingular: squaring its Walsh transform and summing over differences leaves only radical shifts; a trivial radical gives squared magnitude 16, whereas a nontrivial radical cannot give that value at every frequency. Thus its polar Pfaffian is 1. Addition of `B_f` changes only the uv entry by 1, and hence changes the Pfaffian by `A(k1,k2)`. Since `f+q` is bent while `B_f` has rank two, `B_q(k1,k2)=1`. But `B_q(k1,k2)` is precisely the determinant of the two b-projections. Hence they form a b-basis and `K -> F2_b^2` is bijective. Since both r and `r+f` are bent, their Pfaffians are both 1, giving `B_r(k1,k2)=0`; therefore `B_(r+q)(k1,k2)=1`. This proves both assertions, including all affine terms because they do not change the polars.

Each `ell=1` L-coset contains one affine graph H-plane of four S points and its e-translate of four D mates. Each `ell=0` H-cell contains exactly one E-row point with b=0 and three Z points with the three distinct nonzero b-values. Let `lambda in L*` vanish on H and take value 1 on e.

## 3. The seven U0 profile columns, reconstructed at the needed scope

Take any linear complement M of L in `F2^6`. Extend covectors on L and M by zero on the other summand. For `m in M`, `eta in L*`, set

\[
 Z_m(\eta)=\frac14\sum_{v\in L}x(m+v)(-1)^{t\cdot(m+v)+\eta(v)}. \tag{2}
\]

Assume the actual physical x and the divisibility in (C). Then the U0 cap and the specified balance hold **if and only if**

* `Z_m(0)=0` for every m;
* every `Z_m(eta)` is an integer; and
* each of the seven nonzero-eta columns either has exactly one entry `±2`, or has exactly four entries `±1` on an affine two-plane of M with product of their four signs `-1`; all other entries vanish.

For the forward implication, the imported zero-flat statement and inversion on M give `Z_m(0)=0`. The odd support of x inside each L-coset is empty or a four-point affine H-plane. For each eta, the intersection of that plane with `eta=1` has cardinality 0, 2, or 4; consequently subtracting the eta=0 sum changes the numerator in (2) by a multiple of 4, so every Z is integral. Fourier inversion on the complement gives, for `q0 in M*`,

\[
 \widehat x(t+\bar\eta+\bar q_0)=4\sum_m Z_m(\eta)(-1)^{q_0(m)}. \tag{3}
\]

All eight coefficients on every nonzero eta-column are `±8`: divisibility and the cap permit only 0 or `±8`, Parseval with energy 56 gives exactly eight zeroes, and the imported zero-flat already accounts for them. Parseval on M gives `sum_m Z_m(eta)^2=4`. Integrality gives either one `±2` or four `±1`. Four points of the three-space M are either an affine plane or affinely independent. In the latter case every four-sign assignment extends to an affine character, violating the bound on the transform in (3). On a plane the sign assignment extends to a character exactly when the four-sign product is +1; product -1 instead gives character sums of magnitude 2. This proves the stated alternatives. Conversely, those alternatives and (3) make all nonzero-column coefficients `±8`, while the eta=0 column is zero and includes t. Thus this is an exact replacement of the U0 cap/balance at the stated physical/divisibility scope, not an independent U3 or full-caller construction.

## 4. One D0 in each graph L-coset

Assume the four actual D0 points `D_i`, `i=1,...,4`, lie in the four distinct `ell=1` L-cosets. All four `ell=0` E-row D blocks are consequently D3 or F. Define weighted values `X(c)=(-1)^{t dot c} x(c)` and `epsilon_i=X(D_i)/2`.

**Claim A.** The six Z2 points form three opposite-weighted-sign pairs, one pair in each of three `ell=0` H-cells. Their three pair differences are the three distinct nonzero vectors of H. Therefore each nonzero physical b-row contains exactly two Z2 points and the XOR of all six Z2 points is zero.

**Proof.** The zero-eta equation on the ith graph L-coset says the four graph signs X sum to `-2 epsilon_i`. They are therefore a 3-to-1 sign pattern. Since the graph and D mate lie in opposite lambda-levels, the lambda-column entry from this coset has magnitude one. Its four graph-coset entries already contribute squared norm 4, so every `ell=0` lambda entry is zero. Together with the zero-eta equation, this makes the X-sum separately zero in each of its two H-cells. In `ell=0`, the only nonzero x-values are the six Z2 values; each H-cell has just three possible Z points, so its selected number is even, hence 0 or 2, with opposite weighted signs. There are exactly three occupied cells.

Fix any nonzero `alpha in H*` and choose an extension `eta in L*`. In each graph cell the Walsh coefficient of a 3-to-1 four-sign pattern at alpha has magnitude 2; the single D0 term also has magnitude 2. Thus the eta and eta+lambda entries together contribute exactly 1 to the sum of their squared column norms in that graph L-coset. The four graph cosets contribute 4, while the two full norms total 8. On an `ell=0` occupied cell, its pair contributes to a normalized coefficient with magnitude 1 precisely when alpha is nonzero on the pair difference, and otherwise contributes 0. Combining the two H-cells of an L-coset in the two columns doubles the sum of their separate squared contributions. Hence exactly two of the three pair differences are nonzero under each nonzero alpha. In a two-space each nonzero covector has a distinct nonzero kernel vector, forcing the multiset of the three differences to contain each nonzero H direction once.

The b-projection is an isomorphism. Within an H-cell its Z points have the three nonzero b-labels; the difference of a selected pair is its omitted third b-label. Since the three differences have distinct nonzero b-projections, each nonzero b-label is omitted once and selected twice. Also the XOR of all six points is the sum of the three distinct nonzero H vectors, which is zero. QED.

**Claim B.** `product_i epsilon_i=+1`, and `(C)` consequently gives `X_P=X_{D_1,D_2,D_3,D_4}`.

**Proof.** The lambda-column support is exactly the four `ell=1` cosets. Their M-representatives form the affine plane `ell=1`, so the seven-profile theorem gives product of their four signs `-1`. Extend lambda by zero on M. The ith entry is `-epsilon_i (-1)^{lambda(D_i)}`, so its four-sign product is `product_i epsilon_i` times `(-1)^{lambda(X_D)}` for `X_D=sum_i D_i`.

To determine the latter factor rather than assume it, choose representatives `z_st=z0+s u+t' v+k_st`, where `s,t' in F2`, `k_st in K`, and `u,v` project to a basis of `F2^4/K`. For rank two, `B_f(u,v)=1`. Each D point has h-coordinate `f(z_st)+1`. Their XOR lies in L and has z-coordinate `sum k_st`; lambda on L is `h+d_f(k)`. Therefore

\[
 \lambda(X_D)=\sum_{s,t'}f(z_{st})+d_f\!\left(\sum_{s,t'}k_{st}\right)
 =\sum_{s,t'} f(z_0+s u+t'v)=B_f(u,v)=1.
\]

Here `d_f` is linear and removes each radical displacement. Thus `(-1)^{lambda(X_D)}=-1` and the column product `-1` forces `product epsilon_i=+1`. Claim A gives zero XOR for the six Z2 points; with `W={D_i} union Z2`, criterion (C) gives `X_P=X_W=X_D`. QED.

**Claim C.** On each actual graph H-plane, the same physical `y=-agx` is a signed affine H-character.

**Proof.** The weighted graph x-signs are 3-to-1, so as a Boolean exponent on the two-dimensional H-plane they have nonzero alternating quadratic polar. Removing the character `(-1)^{t dot c}` does not change that polar. On S, `ag=(-1)^{r+q}`, whose polar restricted to K is the same unique nonzero alternating form by Section 2. The product `-agx` therefore has zero polar and is a signed affine character on that plane. QED.

Claims A–C are necessary for the entire quantified four-distinct-D0 subfamily. In particular any other nonzero-b row census is excluded uniformly in f, r, actual signs, and transported t. They make no assertion for other D0 allocations and do not prove that the remaining choices satisfy the full U0/U3 system.

## 5. Odd restriction counts of the actual U3 small frequencies

Keep all hypotheses of Section 4 and now additionally assume actual J=1 and all 64 U3 caps `|y-hat|<=12`. The imported same-column congruence gives `y-hat=4 mod 8`. Its values are consequently `±4,±12`. Since `sum y^2=128`, Parseval gives exactly eight frequencies in

\[
 B=\{\xi:|\widehat y(\xi)|=4\},\qquad
 n_\alpha=|\{\xi\in B:\xi|_H=\alpha\}|\quad(\alpha\in H^*). \tag{4}
\]

Indeed `64*128=16|B|+144(64-|B|)`, so `|B|=8`. We prove each `n_alpha` odd.

For each nonzero `v in H`, let `A_y(v)=sum_c y(c)y(c+v)`. The graph contribution is `4 sum_i (-1)^{kappa_i(v)}`, with `kappa_i` the actual character slope from Claim C. It is divisible by 8 because there are four terms. Translation by v preserves S and its complement; all off-S y-values are even, and their points pair under translation by v, so the off-S contribution is also divisible by 8. Fourier inversion, using squared values 16 on B and 144 elsewhere, gives

\[
 A_y(v)=-2\sum_{\xi\in B}(-1)^{\xi(v)}\qquad (0\ne v\in H). \tag{5}
\]

Write `N_v=|{xi in B:xi(v)=1}|`. Since `|B|=8`, divisibility of (5) by 8 says `N_v` is even. The three nonzero v give even sums over each of the three pairs of nonzero H-characters; these force the three nonzero `n_alpha` to have a common parity, and the even total 8 forces the zero-restriction count to have that parity too.

To fix the parity, sum `A_y(v)` for the three nonzero v modulo 16. Each graph H-plane contributes `12` if its slope is zero and `-4` otherwise, so all four graph planes together contribute 0 modulo 16. Off S, each unordered pair of points in the same H-cell occurs once among these shifts, counted in both orders. Its contribution `2 y(c)y(c')` is 8 modulo 16 precisely when both absolute y-values are 2; any zero or magnitude-four entry contributes 0 modulo 16. Each of the four graph-mate H-cells has three D3 magnitude-two entries, for `4*binom(3,2)=12` pairs. In `ell=0`, each of the three occupied Z2 cells has two such Z2 entries and at most one magnitude-two E-row entry, giving `binom(2,2)=1` or `binom(3,2)=3` pairs. Unoccupied cells have at most one magnitude-two E entry; Z4 is a multiple of four. The total number of off-S contributing pairs is therefore odd, and

\[
 \sum_{0\ne v\in H} A_y(v)\equiv8\pmod {16}. \tag{6}
\]

On the other hand, (5) gives exactly `16-8 n_0`, since a frequency with zero H-restriction contributes 3 to the character sum over nonzero v, and any other restriction contributes -1. Thus `n_0` is odd. All four counts share its parity and sum to 8, so, up to their order, they are `(5,1,1,1)` or `(3,3,1,1)`. These are necessary projection counts of the **actual** common y spectrum, not a sufficiency claim or a construction of either spectrum.

## 6. A complete hand-derived physical countercontrol, not a witness

This example is written algebra, not an executed experiment. Set

\[
 f(j,b)=j_0j_1,\qquad r(j,b)=j_0b_0+j_1b_1,\qquad
 \beta=(1,0),\quad \gamma=(0,1),\quad \delta=\beta+\gamma.
\]

Then `K` is the b-plane, `d_f=0`, and H is the b-plane lifted at h=0. The required three bent facts hold: in the Walsh sums for r and `r+f`, the sum over b forces one j and contributes 4; `f+q=1+j0j1+b0b1` factors into two two-bit quadratic Walsh sums of magnitude 2.

For each of the four j choose `D_j=(1,1+f(j),j,0)` and set `x_0(D_j)=-2`. On the graph set x0 negative at exactly

\[
 P=\{(1,f(0),0,\beta)\}\ \cup\
 \{(1,f(j),j,0):j\in\{\beta,\gamma,\delta\}\},
\]

and set x0=+1 at the other twelve graph points. For each `j in {0,beta,gamma}`, set

\[
 x_0(0,0,j,\gamma)=+2,\qquad x_0(0,0,j,\delta)=-2,
\]

and set x0=0 on every other block. Thus the six Z2 positions have b-row census `(0,3,3)` in the order `(beta,gamma,delta)`. The four D0 occupy the four different j-indexed graph L-cosets. Directly, `|P|=4`, `|N|=4+3=7`, `X_P=e+beta`, and `X_W=e+beta`: the D0 XOR is e, while the three Z2 pair differences sum to beta. Hence (C) makes every x0 coefficient divisible by 8.

This divisibility can also be seen without invoking (C). For this f, summing over b in the graph transform gives either zero, 16, or `±8`; for any set A, `widehat(1_A)(xi)=|A|-2(xi dot X_A) mod 4`. Substituting `x0=1_S-2 1_P+2 1_W-4 1_N`, the constant term is `-2*4+2*10-4*7=-16`, and the remaining mod-8 term vanishes because `X_P=X_W`.

Every L-coset sum is zero: at each ell=1 j-slice, the graph signs sum 2 and its D0 contributes -2; the three occupied ell=0 slices have opposite Z2 values. Consequently `x0-hat` vanishes on `L^perp`. At the b1 frequency, the four graph values in any j-slice contribute -2 and its D0 contributes -2, whereas each Z2 pair cancels. Hence

\[
 \widehat{x_0}(b_1)=4(-4)=-16. \tag{7}
\]

For the caller's *given* t, set `x_t(c)=(-1)^{t dot c}x_0(c)`. This merely translates the entire x-spectrum: all coefficients remain divisible by 8, `x_t-hat(t)=0`, and `x_t-hat(t+b1)=-16`. It does not choose a different balance frequency or cure the U0-cap failure.

It remains to specify a single actual 256-entry ternary inverse, not merely an x-array. Use the above f,r,a,g and x=x_t in (1). Put `y=-agx` on S, y=0 on F and the four D0, y=+2 on all eighteen D3, initially `y=x_t` on all six Z2 points, y=+4 at the Z block `(0,0,delta,gamma)`, and y=0 on the remaining seventeen Z points. If the resulting `J=|{c:u(c,0)!=0}| mod 2` is even, negate y at `(0,0,0,gamma)`; otherwise make no change. At that Z2 point a=g=0 and initially y=x, so `u(c,0)=x/2!=0`; after the negation it is zero. The single toggle flips J and changes neither x nor any block type/count or energy. Thus J=1 and the imported same-column identity gives the U3 residue `4 mod 8`, not a U3 amplitude bound.

The inverse is ternary in every block. On S, writing `s=a chi1` and `t'=g chi2`, both `±1`, equation (1) becomes `(3s+t'+x(1-s t'))/4`: if `s=t'` it equals s, and otherwise it equals `(s+x)/2`. Thus each graph block has three nonzeros. On F the inverse is `chi2`; every D block has two nonzeros; Z2 has two, Z4 has four, and Z0 has none. Hence the exact support count is `16*3+2*4+22*2+6*2+4=116`; `sum x^2=56`, `sum y^2=128`, and y has `2+4+17=23` spatial zeros. Its row census contradicts Claim A because (7) violates the U0 cap; this is a physical countercontrol to weakening the hypotheses, **not** a contradiction to Claim A and **not** a common capped even half.

## 7. Exact unpaid original-caller obligations

1. The complete rank-two source branch includes *all* ways to allocate the four D0 blocks, including repeated graph L-cosets and E-row D0. Section 4 does not address those. For every surviving actual common `(f,r)`, physical signs and prescribed t, either construct or rule out x satisfying the seven U0 profile columns in Section 3 together with every original physical/rank/atom requirement. Necessary conditions alone do not supply this x.
2. On that **same** x and same graph/phase choose the actual y dictated by (1), including the D3/Z2/Z4 signs and J=1, and establish all 64 `|y-hat|<=12`. In the four-distinct subfamily Claims A–C and the four odd counts are compulsory, but neither allowed count pattern has been constructed or excluded. The first unpaid joint step is a common seven-profile U0/U3 completion or a uniform contradiction covering the relevant choices.
3. Let `C_u={(c,w):u(c,w)=0}` be the **actual** 140-point complement of such an even half. Choose signs `sigma(c,w) in {±1}` on this fixed set, with an odd number of negative signs, and check all 256 signed inequalities, one for every `(xi,omega) in F2^6 x F2^2`:

\[
 \left|\sum_{(c,w)\in C_u}\sigma(c,w)(-1)^{\xi\cdot c+\omega\cdot w}\right|\le14. \tag{8}
\]

The parity condition is not the cap. When all even-half Walsh coefficients are divisible by 4, the support XOR of u, and hence of `C_u`, is zero: compare the transform at each linear character to DC modulo 4, using `u mod 2=1_{supp u}`. Therefore the actual complementary transform is `2 mod 4` exactly when the number of negative signs is odd; (8) remains 256 separate amplitude constraints on the same complement, not an unsigned tally or a freely chosen support.
4. Restore the original common gauge/coordinate map, original DC via its specified t, selected nonzero T, original rank/eight-zero/atom/cross-fibre hypotheses, and all remaining original Boolean conditions. Only then use the original pairwise inverse `s(z)=u(z)+v(z)`, `s(z+T)=u(z)-v(z)` on disjoint support. No original caller, global five-span no-go, six-span conclusion, or NL242 closure follows from this candidate.

## 8. Chronology and assurance

Before packet-body exposure I read the complete assigned manifest, freeze, parent-prepared metadata, actual dispatch, and every listed status control through its ending; the live manifest and freeze hashes matched their assigned pins. I sent Main a direct PREBODYACK before scientific packet reading. I then read the complete frozen packet in order in raw slices of at most 20 LF, including its final LF353; no packet link, held payload, held history or held consumer was followed. The native clock after packet reading was `2026-10-30T15:58:49-0700 PDT`; a further native clock observed during written derivation was `2026-10-30T15:59:41-0700 PDT`. Administrative line counting, two hash checks and native clocks are not scientific execution. Source hashes other than the two directly checked assigned pins are attributed to the parent freeze/metadata rather than independently rehashed here.

All proofs and the explicit countercontrol in this file are written derivations; CHILD SCIENTIFIC EXECUTION NOTRUN. No program, CAS, solver, mathematical experiment, build, lint, test, formatter, external-model CLI, sibling proof/code, or external source was used. All held episodes and **all** consumers—including f513/f586/f653/f654/f659/f660/f662—remain NONINPUT. There is no claim of unobservable cognitive isolation. This author body requires a separate full-scope independent mathematical check and parent disposition; it is not human, cross-model-family, formal/kernel, novelty, original-source-equivalence, or original-target-closure certification.
