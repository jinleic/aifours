# Same-object Boolean U3: a uniform sign obstruction and physical reconstruction

**NONBLIND GENERAL-AUTHOR CANDIDATE; UNADOPTED.** On the particular physical `f, phase, x` specified in S1, the 24-sign/18-site common-`y` system has **no solution** with `J=1` and all 64 `U3` caps. The proof below is written, uniform in all 24 signs and all Z4 sites/signs, and in fact excludes a larger explicitly stated class of partial arrays. It is not a finite exhaustion, and has not received parent review or a separate disposition. It says nothing by itself about other actual `x`, graph/phase choices, or D0 allocations. The original Boolean target is **not proved or refuted**.

The full S1 reconstruction exposed two concrete errors in its unadopted example: three of the seven displayed profile rows have both graph signs reversed, and its stated graph `w=0` nonzero counts by `b` are wrong and do not sum to its claimed total. Correct rows and counts are below. The corrections preserve the stated profile types and the total 9 graph nonzeros, but they are mathematical corrections, not an old-gate clearance.

## 1. Inputs and the actual caller

Only the four complete bodies in the ordered frozen packet were scientific inputs: S1, the unadopted f689 body, SHA-256 `69ada1decb9bdf5835dc0b438647a114f1872932c52327cc2cbed5d6b7192a29`; S2, the adopted four-distinct-D0 necessary location theorem, `fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a`; S3, the adopted actual seven-profile and cross-fibre conditions, `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`; and S4, the finite quotient receipt, `ffa3595b81ed738f766a771f2d0540f49e8b0c4f31e565af872c9e2b72d84659`. S4's actual U0 illustration is a different graph construction; its y, J, U3, V and original caller were not tested. It is not verification of S1's example. These are frozen source pins and parent-reported source bindings, not my own direct source-file hashes.

Write `c=(ell,h,j,b)`, with `j,b in F2^2`, and let `e` toggle h. The physical graph is `S={(1,f(z),z)}` for `z=(j,b)`, with `a=1_S (-1)^phase` and `g=U2`: `g=rho_b=(-1)^(1+b0*b1)` on S, `-2 rho_b` at graph mates, 4 on the two F blocks, -2 on the other six E-row blocks, and 0 on the 24 Z blocks. The one actual inverse is

`u(c,w)=[x(c)+3a(c)chi1(w)+g(c)chi2(w)+y(c)chi3(w)]/4`,

and its graph condition is **the same** `y=-agx`. The local forms are graph `(x,y)=(+/-1,-agx)`, F `(0,0)`, D0 `(+/-2,0)`, D3 `(0,+/-2)`, Z2 `(+/-2,+/-2)`, Z4 `(0,+/-4)` and Z0 `(0,0)`. In the named m116/local-`H_local=0` caller, there are 4 D0, 18 D3, 6 Z2, 1 Z4 and 17 Z0, with `sum x^2=56`, `sum y^2=128`, and 23 spatial y zeros. `H_local` is not the radical plane H used below.

The covector `t` is the specified image of original DC under the actual common gauge. The imposed balance is `xhat(t)=0`; t is neither selected after choosing x nor the original selected nonzero T. S2/S3 remain conditional on their stated actual physical, divisibility, zero-flat, original-source and collateral-atom imports. I do not assert equivalence with an unexamined printed source.

## 2. Location and signed criterion reconstructed

Let `K=rad(B_f)`, `d_f(k)=f(z+k)+f(z)`, `H={(0,d_f(k),k):k in K}`, `L=H direct-sum <e>`, and `lambda|H=0`, `lambda(e)=1`. The nondegeneracy of the polar form of `f+q`, with rank-two `B_f` and `q=1+b0*b1`, gives `B_q|K` nondegenerate: in a symplectic complement to K the Pfaffian of `B_f+B_q` is `B_q(k1,k2)`, since `B_q` itself has rank two. Hence projection `K -> F2_b^2` is an isomorphism. Each ell=0 H-cell has one E-row point and three Z points. Fix a complement M of L; `M_0={ell=0}` is a two-plane and `M_1={ell=1}` its affine coset. Extend L-covectors by zero on M.

For **the actual** `X(c)=(-1)^t(c)x(c)`, let `Z_m(eta)=1/4 sum_(v in L) X(m+v)(-1)^eta(v)`. The S3 import, at its exact scope, characterizes the common x condition: zero column, integral entries, and, for each nonzero eta, either one `+/-2` or four `+/-1` on an affine two-flat with product -1. The quotient identity `xhat(t+eta+mu)=4 sum_m Z_m(eta)(-1)^mu(m)` also proves the profile-to-cap and divisibility direction; the seven columns are not independent choices.

Assume the four actual D0 blocks lie one in each graph L-coset. For D0 `D_i`, graph mate `G_i=D_i+e`, and `epsilon_i=X(D_i)/2`, the zero column forces a unique `delta_i in H` with

`X(G_i+h)=epsilon_i(2*1_(h=delta_i)-1)`.

Thus `Z_(m_i)(lambda)=epsilon_i (-1)^lambda(D_i)`, with the **plus** sign. Its four graph entries consume the column energy, so every ell=0 H-cell has zero weighted x sum. Exactly six Z2 points consequently give three occupied cells, each an opposite-weighted pair. For nonzero `alpha in H*`, write `eta_s=bar_alpha+s lambda`; then

`Z_(m_i)(eta_s)=epsilon_i (-1)^eta_s(G_i) [(-1)^alpha(delta_i)+(-1)^s]/2`.

A Z pair contributes to the two extensions iff alpha is nonzero on its difference, and then contributes two units in their combined squared norm. The graph contributes four units in total and the two columns have combined norm eight. Thus exactly two pair directions are active for every nonzero alpha. The three directions are the three distinct nonzero elements of H; their XOR is zero, as is the XOR of all six Z2 points, and their actual nonzero-b row counts are `(2,2,2)`.

The four D0 z-coordinates represent all four K-cosets. Taking a symplectic complement `u,v` of K, their sum `X_D=sum_i D_i` is in L and `lambda(X_D)=sum_(s,t) f(su+tv)=1`: radical terms cancel against `d_f(sum k_i)`. The odd-product lambda profile now gives `product_i epsilon_i=+1`.

There are only two occupied-cell patterns. If `a_d in M_0` denotes the L-coset of direction d:

* **1+1+1.** The four deltas have each H-value once, and form an affine bijection `delta:M_1 -> H` with linear part `A:M_0 -> H`. The profile support flats force `A(a_d+a_d')=d+d'` for every distinct nonzero d,d'. All six nonzero-H-restriction columns are four-entry columns.
* **2+1.** If d1,d2 lie in the two H-cells over a and `d3=d1+d2` lies over `b!=a`, then delta is affine onto a line parallel to d3, has kernel `<a+b>`, and takes each line value twice. For the unique nonzero `alpha0` active on d1,d2, one extension is a single `+/-2` and the other has four graph entries; the other four columns each have two graph and two Z entries. The singleton is not a four-point flat.

The location conditions are not by themselves sufficient. Choose one actual point `z_d` in each pair, let `xi_d=X(z_d)/2`, and for alpha's two active directions d,d' suppose their cells have distinct L-cosets. If `alpha(delta_i)=alpha(delta_i')=s`, their exact flat and sign equations are

`m_i+m_i'=a_d+a_d'`,

`epsilon_i epsilon_i' xi_d xi_d' (-1)^eta_s(G_i+G_i'+z_d+z_d')=-1`.  (2.1)

Changing the chosen endpoint changes both xi and its character, so (2.1) is endpoint-independent. In 1+1+1, the affine relation supplies the flat equation and all six sign equations in (2.1) are required. In 2+1, writing `X_D=sum D_i`, the odd four-graph column and the singleton respectively require

`alpha0(delta_i)=1+bar_alpha0(X_D)` for all i,                         (2.2)

`xi_1 xi_2 (-1)^[bar_alpha0(z_1+z_2)+bar_alpha0(X_D)]=+1`;          (2.3)

the four remaining columns require (2.1). Indeed the graph-column sign product is `(-1)^[bar_alpha0(X_D)+s]`, while the two same-coset contributions add precisely at the singleton extension in (2.3). Conversely, the zero column, `product epsilon=+1`, the appropriate affine location relation, and these literal sign equations produce all seven required profiles. This reconstructs S1's **same-physical-x** signed iff under the stated physical counts and one-D0-per-coset assumption; it does not construct a common y.

For the physical negative graph set P and the ten D0/Z2 points W, the actual XOR follows as well: in each graph cell the negative-x XOR is `G_i+delta_i+k_t`, where the common `k_t` is the nonzero kernel element of `t|H` if that restriction is nonzero and otherwise 0. Four copies cancel, so `XOR(P)=X_D+sum_i delta_i=X_D=XOR(W)` in both patterns. This XOR does not by itself replace the other divisibility or profile conditions.

## 3. The particular actual x: corrected seven profiles

Write `0=(0,0), p=(1,0), q=(0,1), r=(1,1)` and use `R` for the phase, avoiding confusion with the vector r. Take

`f(j,b)=j0*j1`, `R(j,b)=j0*b0+j1*b1`.

The polar rank of f is 2, `f+1+b0*b1` is a direct sum of two nondegenerate binary quadratics, and R and R+f are bent: summing their Walsh transforms over b fixes j and leaves magnitude 4. Here H is the b-plane, `M=(ell,j)`, `G_j=(1,f_j,j,0)`, and `D_j=(1,1+f_j,j,0)`.

Define `x_*` by `x_*(1,f_j,j,b)=2*1_(b=j)-1`, `x_*(D_j)=2`, and the only six Z2 values

| j | h | b | x_* |
|---|---:|---|---:|
| p | 1 | q | +2 |
| p | 1 | r | -2 |
| q | 1 | p | -2 |
| q | 1 | r | +2 |
| r | 0 | p | +2 |
| r | 0 | q | -2 |

All other values vanish. The three pairs have directions p,q,r respectively, with `a_d=d`, `delta_j=j`, and all `epsilon_j=+1`. For the **given** t, use `x_t(c)=(-1)^t(c)x_*(c)`; the profile transform untwists it back to x_*.

In this table `p+` means the entry at j=p is +1, and entries not listed vanish. These are the **correct actual signed entries**:

| eta | ell=0 entries | ell=1 entries |
|---|---|---|
| lambda | none | 0-, p-, q-, r+ |
| b0 | p+, r- | 0+, q+ |
| b0+lambda | p-, r- | p-, r+ |
| b1 | q-, r+ | 0+, p+ |
| b1+lambda | q+, r+ | q-, r+ |
| b0+b1 | p-, q+ | 0+, r+ |
| b0+b1+lambda | p+, q- | p-, q- |

S1 instead prints `p+,r-`, `q+,r-`, and `p+,q+` in the three graph-side lambda-shifted rows respectively. For example, at eta=`b0+lambda`, ell=1, j=p, the graph sum weighted by b0 is -2 and the D0 contribution weighted by h is -2, so the entry is `(-2-2)/4=-1`, not +1. This is the first such displayed-row failure. The other two corrected signs follow from the same formula in section 2.

Each corrected row has product -1. The lambda support is the full ell=1 plane; in each other row, the XOR of the two ell=0 j positions equals the XOR of its two ell=1 j positions, so the four M-points form a flat. The zero column vanishes, since each graph sum -2 cancels its D0 +2 and each Z2 pair cancels. A four-sign odd-product pattern on an affine binary two-flat has all four internal Walsh magnitudes 2. Hence all 64 `xhat_t` values lie in `{0,+8,-8}`, the eight zeros are precisely `t+L^perp`, and the specified `xhat_t(t)=0` and all U0 divisibility hold. This is one x, not independently chosen profiles.

## 4. Physical y, parity J and arbitrary t

Define `y_*` on this same x: use `-agx_*` on S, zero on F and D0, +2 on the 18 D3 and 6 Z2 blocks, +4 at `(ell,h,j,b)=(0,0,0,p)`, and zero on the other Z sites. For every specified t, put `y_t=(-1)^t y_*`. The fixed a and g are **not** modulated. Nevertheless `y_t=-agx_t` on S, and on every other physical block the allowed local pair form is unchanged by sign modulation, so the four-point inverse remains ternary. Each graph block has 3 nonzeros, F has 4, D0/D3/Z2 have 2, Z4 has 4 and Z0 has 0. Thus support is `16*3+2*4+4*2+18*2+6*2+4=116`, with x/y energies 56/128 and 23 spatial y zeros. This does **not** say that the whole `u_t` is the character modulation of `u_*`; its fixed `3a` and g terms generally prevent that.

At t=0, direct evaluation of `4u(c,0)=x+3a+g+y` gives graph nonzeros by b as follows:

| b | j with nonzero `u(c,0)` | count |
|---|---|---:|
| 0 | 0 | 1 |
| p | p,r | 2 |
| q | q,r | 2 |
| r | 0,p,q,r | 4 |

Thus there are 9 graph nonzeros. S1's `(3,2,2,0)` is incorrect and even sums to 7, not 9. Off graph there are 2 F, 4 D0, 8 D3, 3 Z2 and 1 Z4 nonzeros, hence `J=27 mod 2=1`.

The arbitrary-t parity follows from the **actual** inverse, not a claim that the whole u is modulated. For the common graph, direct b-summation gives

`ahat(nu,s,beta,alpha)=4(-1)^[nu+s f(alpha)+beta(alpha)]`,

so `3 ahat` is always 4 mod 8. Also `sum_b rho_b(-1)^alpha(b)=-2(-1)^(alpha0 alpha1)`. When s=0, the ell=1 contribution to `ghat` is a multiple of 8 and the ell=0 E-row contribution is 4 mod 8; when s=1, the ell=0 contribution vanishes and the ell=1 one is `+/-12`. Thus `ghat=4 mod 8` at every frequency. For ternary u, the transform of `4u(c,0)` is `4J mod 8`, because signs and Fourier characters do not affect parity. Since every `xhat_t` is divisible by 8,

`yhat_t(xi)=4J mod 8` for every xi.                                   (4.1)

For the reference at t=0 this gives residue 4; `y_t` is a character modulation of y_* alone, so its y spectrum is a translate and also has residue 4. Equation (4.1), with the unchanged a,g and the actual inverse, then gives `J=1` for every specified t. Finally the reference graph y sum is -8, the D3 sum is 36, Z2 sum 12 and Z4 sum 4, so `yhat_t(t)=yhat_*(0)=44`: this J=1 completion fails U3.

## 5. Literal common-y system, with all coefficients

Fix this `x_t`. Untwist any compatible y as `Y(c)=(-1)^t(c)y(c)`. On the graph

`Y(1,f_j,j,b)=g_j(b)=sigma_j (-1)^kappa_j(b)`,

with `sigma_0=+1`, `sigma_p=sigma_q=sigma_r=-1`, `kappa_0=kappa_r=b0+b1`, and `kappa_p=kappa_q=0`. This follows directly from `-agx_*`; it is not a free graph spectrum.

The remaining choices are the **same** 24 signs in every frequency: 12 `d_(j,b)` on graph D3 mates, `j in F2^2, b=p,q,r`; six `e_(j,h)` on ell=0 E-row D3, `j=p,q,r`; six `z_(d,b)` on the Z2 sites in section 3; and a site `(0,h_*,j_*,b_*)` among the 18 Z sites not already Z2 plus a sign `k`. Their untwisted amplitudes are respectively `2d`, `2e`, `2z`, `4k`. There are 18 site choices and two k signs, not 18 independent coordinates of y.

Relative to the reference y, flipping any D3 or Z2 sign toggles exactly one `w=0` nonzero, whereas moving or signing the Z4 changes no total `w=0` count. This remains true after the common t modulation. Therefore `J=1` is exactly

`#{negative d,e,z signs}=0 mod 2`.                                     (5.1)

Let `B_p={q,r}`, `B_q={p,r}`, `B_r={p,q}`, with `h_p=h_q=1`, `h_r=0`. For `s in F2` and `alpha,beta in (F2^2)*`, the two **actual partial transforms of one Y** are

`A1(s,alpha,beta)=sum_j (-1)^beta(j) [4 sigma_j (-1)^(s f_j) 1_(alpha=kappa_j) + 2(-1)^[s(1+f_j)] sum_(b=p,q,r) d_(j,b)(-1)^alpha(b)]`,

`A0(s,alpha,beta)=2 sum_(j=p,q,r) (-1)^beta(j) sum_(h=0,1) e_(j,h)(-1)^(s h)`

`    +2 sum_(d=p,q,r) (-1)^[beta(d)+s h_d] sum_(b in B_d) z_(d,b)(-1)^alpha(b)`

`    +4k (-1)^[beta(j_*)+s h_*+alpha(b_*)]`.                       (5.2)

Their coefficient signs follow directly from the actual graph h=f_j, mate h=1+f_j, and the displayed ell=0 sites. At the actual frequency `t+nu ell*+s h*+beta+alpha`, the same physical y has transform `A0+(-1)^nu A1`. Therefore all 64 caps are **equivalent** to

`|A0(s,alpha,beta)|+|A1(s,alpha,beta)|<=12` for all 32 triples.      (5.3)

Let `n_j` count negative d signs in row j and `n=sum_j n_j`. At `(s,alpha,beta)=(0,0,0)`, `A1=16-4n`, hence `1<=n<=7`. At `(1,0,0)`, `A1=-20+4(n_0+n_p+n_q-n_r)`, hence `2<=n_0+n_p+n_q-n_r<=8`. These S1 bounds are correct necessary conditions, not by themselves the full obstruction.

## 6. Uniform obstruction: no completion of the specified x

The following slightly larger-class statement supplies an analytic proof, with no enumeration and no use of the Z4 location or of the detailed ell=0 signs.

**Lemma.** Let j,b range over `F2^2`, and let `sum_j f_j=1 mod 2`. Suppose an actual real y has ell=1 values `g_j(b)=sigma_j(-1)^kappa_j(b)` on `(h,j,b)=(f_j,j,b)`, zero at each mate `(1+f_j,j,0)`, and `2d_(j,b)` at the other twelve mates, where all `sigma_j,d_(j,b)` are signs. Assume every covector among the four `kappa_j` occurs an even number of times, `sum_c y(c)^2=128`, and all 64 Walsh coefficients are 4 mod 8. Then the 64 caps `|yhat|<=12` cannot all hold, regardless of every ell=0 value.

*Proof.* Denote by A1 the ell=1 partial transforms. Let n be the number of negative d signs. For any fixed s,alpha,beta, the graph part of A1 is 4 times a signed sum over those j with `kappa_j=alpha`; by even multiplicity it is 0 mod 8. The product of the twelve mate characters `(-1)^[beta(j)+alpha(b)+s(1+f_j)]` is `(-1)^s`: beta contributes an even number of negatives, alpha contributes an even number, and `sum_j(1+f_j)` is odd. Thus the twelve d terms have negative-sign parity `n+s`, and

`A1(s,alpha,beta)=4(n+s) mod 8`.                                    (6.1)

With both full coefficients `A0+A1` and `A0-A1` equal to 4 mod 8, A0 and A1 are multiples of 4. If `s=n mod 2`, A1 is 0 mod 8 and A0 is 4 mod 8. If `s=1+n mod 2`, A1 is 4 mod 8 and A0 is 0 mod 8. Under the cap, the former A1 is either 0 or `+/-8`, while the latter is `+/-4` or `+/-12`.

Parseval and the full energy 128 give exactly eight magnitude-4 full coefficients: with 64 coefficients, if k have magnitude 4 and the rest magnitude 12, then `16k+144(64-k)=64*128`, so k=8. Let E be the number of the 16 triples in the first s-slice with `|A1|=8`, and O the number of the 16 triples in the second s-slice with `|A1|=4`. Each of these E+O triples forces at least one distinct magnitude-4 full coefficient: in the E case `|A0|=4`, and in the O case A0 is 0 or `+/-8`. Hence

`E+O<=8`.                                                           (6.2)

The ell=1 energy is `16+12*4=64`, so partial Parseval gives `sum_(s,alpha,beta)(A1/4)^2=32*64/16=128`. Its two slice types give

`4E+O+9(16-O)=128`, hence `O=2+E/2`.                                (6.3)

Consequently E<=4. On the other hand put `C=sum_(j,b!=0) g_j(b)d_(j,b)`. Parseval in j,b for the slice `s=n mod 2` gives

`4E=64+4(-1)^n C`, so `E=16+(-1)^n C>=4`,                          (6.4)

because C is a sum of twelve signs. Thus E=4 and equality in (6.4) forces

`d_(j,b)=-(-1)^n g_j(b)` for every j and b!=0.                       (6.5)

Taking products over those twelve sites gives `(-1)^n=product_j sigma_j`: the twelve common factors in (6.5) multiply to +1, while `product_(b!=0) (-1)^kappa_j(b)=1` because `p+q+r=0`.

Now take `s=1+n mod 2`. By (6.5), `(-1)^s d_(j,b)=g_j(b)`. The effective ell=1 h-transform is therefore `g_j(0)` at b=0 and `3g_j(b)` at b!=0. Its b-Walsh transform is

`sigma_j [12*1_(alpha=kappa_j)-2]`.

After the h phase, put `v_j=sigma_j(-1)^(s f_j)`. Their product is `(-1)^n (-1)^s=-1`. The even multiplicity hypothesis means either all four kappa values coincide, or two different values occur twice each. In the first case choose their common alpha; for every beta the four signs `v_j(-1)^beta(j)` have product -1 and sum `+/-2`, so `|A1|=20`. In the second case choose an alpha occurring twice and choose beta so its two active signed v-values agree; this is possible because their two j labels differ. Since the product of all four signed values is -1, the two inactive values then cancel, while the active values contribute `10*(+/-2)`. Again `|A1|=20`. But `max_nu |A0+(-1)^nu A1|>=|A1|`, contradicting the full cap 12. QED.

For the specified x, `f_j=j0*j1` has odd four-point sum, and its forced graph y has the two covectors `0` and `b0+b1` twice each. All compatible local y have the lemma's 12 D3 signs and total energy 128. If also `J=1`, equation (4.1) supplies the residue hypothesis for every t. Thus the lemma excludes **every** assignment of the 24 shared signs and each of the 18 times 2 Z4 choices in (5.1)–(5.3). It is a conditional uniform obstruction for the larger lemma class as stated, but the only displayed physical x to which it is applied here is S1's explicit x. Neither a U3 witness nor an exclusion of all rank-two callers follows.

## 7. Exact remaining boundary and process

For the original four-distinct-D0 subfamily one must still quantify over every actual permitted f and common bent phase, actual D0/Z2 locations and weighted graph signs, and common physical y. The lemma applies only when its aligned D0, odd-f, even-character-multiplicity, energy and residue hypotheses are individually established; it does not cover all such x or the other D0 allocations. S3's odd restriction-count theorem remains only a necessary condition for an actual capped y, not a preassigned spectrum.

Even a different successful common U0/U3 object would still need signs on the **140 actual zero positions of that same u**, odd negative parity, and all 256 odd-half Walsh caps `<=14`; then the original common gauge/coordinate map, specified original-DC transport, selected nonzero T, rank/eight-zero, atom, cross-fibre and pairwise-inverse requirements remain to be restored at their literal import scopes. No source identity, original global Boolean/NL242 closure, novelty, independent-model-family review, human review, kernel proof, or parent acceptance is asserted.

Before the direct PREBODYACK I read manifest, freeze receipt, final binding, prepared parent metadata, actual dispatch and all 21 listed controls through their endings; controls were used for permissions/status only. Live metadata SHA checks matched the three supplied manifest/receipt/binding hashes and the single 358-LF packet hash `a3ae85ebc933c5ae212c154e3a7b13062b6991ba51eb1072aa79282a46d95ac0`. After the ACK I read packet LF 1–358 in ascending serial RAW windows of at most 20 LF, through its ending, before deriving. A native clock observed during this work was `2026-10-30T16:44:03-0700 PDT`, not a claimed file-creation time. All held episodes and all their proof/method/selection/planning/verification/confidence/reporting/downstream consumers were NONINPUT; no outgoing scientific link, sibling proof, old code or held history was followed. **CHILD SCIENTIFIC EXECUTION NOT RUN:** the calculations here are written derivations, not a solver, CAS, scientific program, test, build, linter, formatter or external model. This nonblind author result and both identified corrections require a separate full parent read and disposition.
