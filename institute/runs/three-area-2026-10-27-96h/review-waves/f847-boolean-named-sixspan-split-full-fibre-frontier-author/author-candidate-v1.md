# Named m116 six-span split: a common four-fibre zero-flat and mixed-amplitude obstruction

**Status: prospective written AUTHOR CANDIDATE, conditional on the named original-object and normalization imports.** This gives new, simultaneously imposed restrictions on the same actual `x=U0`, `a=U1/3`, `g=U2`, `y=U3`, not an exclusion of the entire split branch. Every statement below is uniform in all admitted labelled placements and signs. Failure of any displayed necessary test excludes that placement and its specified signs as an actual caller. No example below is asserted to be an original caller. Parent disposition and independent review are separate.

## 1. Quantifiers, original object, and exact import boundary

Let `F:F2^9 -> F2` be **any one** balanced original Boolean function in the named f263/f244 residual of S1--S4: original Walsh cap 28; its actual support XOR `T != 0`; `m=116`; rank-two even quotient quadratic with six-dimensional radical, `q|R=0`, and eight original even Walsh zeros; labelled nonzero-fibre small counts `(0,4,8)`; `G3=1`, meaning 23 `U3` zero blocks; and **local** `H=0`, meaning no `U1=0` block has a single `|U0|=4` peak. The original f244 atom/class boundary, common normalization and the identification of this local H with the intended named residual are conditional imports; the bodies behind links in S1--S5 were not supplied and are not treated as newly proved or authenticated here. In particular no equality with an unspecified historical H class is claimed.

Use S4's actual pair functions on the same 256 points: `u=(s(y)+s(y+T))/2`, `v=(s(y)-s(y+T))/2`, with `s=(-1)^F`, `u^2+v^2=1`, `uv=0`, `sum u=0`, `sum u^2=116`, `sum v^2=140`. The four `U_s` are partial Walsh transforms of this **one** `u` in the same 64 blocks, with inverse

`4u(c,w)=x(c)+3 a(c) chi_1(w)+g(c) chi_2(w)+y(c) chi_3(w)`.

Take only the six-span branch in which the two full `|g|=4` blocks are in **different** odd rows. Import the split-branch necessity of S2 and the original-caller bridge of S1/S3. All of the original rank, atom, cross-fibre, sign, original selected-XOR and complementary-`v` requirements remain in force. In particular the all-translation atom intersection and sign-mismatch requirements of S4 are not replaced by the tests below. The other six-span branch, five-span source correspondence beyond the stated imports, other m116/m114 classes, and global NL242 remain open.

A common normalization is allowed, but it can move original balance. Write its **specified** transported original-balance frequency as `t in (F2^6)*`; the actual requirement is `xhat(t)=0`. It is not permissible to choose a convenient zero after the fact. All signs, `a,g,x,y`, the spatial support and `t` move together under the same normalization. Hats below are unnormalized 64-point Walsh transforms. Every frequency, subspace and placement is over `F2`; all actual physical values are real integers and signs are Boolean. No complex-existence claim is needed or made.

## 2. Explicit all-placement split geometry, including matched peaks and signs

Write `c=(Y,j,p)` with `Y in F2^3`, `j in F2`, `p in F2^2`. The E row is `Y=000`, its `a` support is `j=0`, and the four B rows are

`Y_1=100, Y_2=010, Y_3=001, Y_4=111`.

Choose **arbitrarily** two distinct B-row labels `A,B` for the full blocks; `C,D` are the remaining two. The following notation ranges over every placement, not a selected fixture. Choose nonzero `lambda in (F2^2)*` and its unique nonzero kernel vector `v`. For `i=A,B`, choose `j_i in F2` and `p_i,t_i in F2^2`, and put

`F_i={(j_i,p_i)}`, `S_i={(1+j_i,t_i),(1+j_i,t_i+v)}`.

For `i=C,D`, choose `t_{i0},t_{i1}` and distinct nonzero `d_{i0},d_{i1}` with `d_{i0}+d_{i1}=v`, and put

`F_i=empty`, `S_i={(0,t_{i0}),(0,t_{i0}+d_{i0}),(1,t_{i1}),(1,t_{i1}+d_{i1})}`.

Thus both full-bearing lines have direction `v`; both free rows are genuinely nonplanar and have spatial XOR `v`. This also follows from S2's common `a`-transform hyperplane: a two-point row has Fourier support on the affine hyperplane whose normal is its line direction. Let `S_E={(0,p):p in F2^2}`, and `S={(000,z):z in S_E} union union_i {(Y_i,z):z in S_i}`. The two actual full points form `F={(Y_A,j_A,p_A),(Y_B,j_B,p_B)}`.

The S2 normalization fixes `q_1=q_2=q_3=-1`, `q_4=+1` for these labelled `Y_i`; in particular their product is `-1`. Indeed the E-row sum is `-4`, each B-row sum is `-4q_i`, and the four small coefficients at `0,e1,e2,e3` are all `+4`. The **same** `g` is

- `g(000,j,p)=3 1_{j=0}-2`;
- `g(Y_i,j,p)=q_i[-2+3 1_{S_i}(j,p)+6 1_{F_i}(j,p)]`;
- `g=0` on the other three Y rows.

Put `r_i=lambda(p_i)+lambda(t_i)` for `i=A,B`. Necessarily `r_A != r_B`. For either of the other two nonzero covectors `eta`, equivalently `eta(v)=1`, let `delta_i(eta)` for `i=C,D` be the unique level with `eta(d_{i,delta_i})=0`. Both BB equations are required:

`j_A+j_B+delta_C+delta_D=0`,

`eta(p_A+p_B+t_{C,delta_C}+t_{D,delta_D})=0`.

All additions are in `F2`. To see both equations, the full rows' `(J,eta)` transforms equal `6 q_i (-1)^(J j_i+eta(p_i))`; the free rows' transforms equal `6 q_i (-1)^(J delta_i+eta(t_{i,delta_i}))`. The four signed values must have product `-1` for every `J` to give four magnitude-12 Y transforms. For `eta=lambda`, the two full-row active `J` values are `r_A,r_B`, and the free rows vanish, giving the two CC routings. Thus the two equations retain both the j-parity and offset sign of the **one actual g**, not two separately selected shells.

The actual signed `a` is also common. Choose `beta in (F2^2)*`, `rho_E,alpha_A,alpha_B,rho_C,rho_D in {+1,-1}`, and different `epsilon_C,epsilon_D in F2`. On `S_E`, `a=rho_E (-1)^(beta.p)`. On a full-bearing row set `a(Y_i,1+j_i,t_i)=alpha_i` and multiply by `(-1)^(1+beta(v))` at the other line point. On a free row set

`a(Y_i,j,p)=rho_i (-1)^(epsilon_i j+(beta+lambda)(p))` on `S_i`.

It is zero off `S`. The E-row transform peaks are the pair `{(0,beta),(1,beta)}`; the free peaks are the distinct matched endpoints `{(epsilon_C,beta+lambda),(epsilon_D,beta+lambda)}`. The full-bearing transforms both occupy `eta(v)=1+beta(v)`. On that hyperplane, for every `J` and both `eta`, define `A_i(J,eta)=sum_{z in S_i} a(Y_i,z)(-1)^((J,eta).z)`; **all four** have magnitude 2 and must satisfy

`A_A(J,eta) A_B(J,eta) A_C(J,eta) A_D(J,eta) = -16`.  (2.1)

This is the full `a` sign coupling, not a choice of four independent peaks. Equivalently, for full rows `A_i=2 alpha_i (-1)^[J(1+j_i)+eta(t_i)]`; for a free row choose the unique `kappa_i` with `(eta+beta+lambda)(d_{i,kappa_i})=0`, and `A_i=2 rho_i (-1)^[(J+epsilon_i)kappa_i+(eta+beta+lambda)(t_{i,kappa_i})]`. The four equations (2.1), the displayed BB equations, the routing inequality, and every remaining original cross-fibre condition must hold simultaneously. They are imported/derived necessary interfaces, not a construction or completeness claim for the original caller.

## 3. The one common physical completion

Set `D={c:|g(c)|=2}`. It has 22 points. Let `D0 subset D` have exactly four points and `D3=D\D0` have 18. The 24 `g=0` points are precisely the three remaining Y rows; choose **any** six as `Z2`, any one further point as `Z4`, and call the remaining 17 `Z0`. These choices range over **all** physical placements. The ternary inverse and local H force the following table, with all indicated signs in `{+1,-1}`:

| physical site | `x` | `y` |
|---|---:|---:|
| `S` | `epsilon_x` | `-a g epsilon_x` |
| `D0` | `2 epsilon_x` | `0` |
| `D3` | `0` | `2 epsilon_y` |
| `Z2` | `2 epsilon_x` | `2 epsilon_y` |
| `Z4` | `0` | `4 epsilon_y` |
| `F` or `Z0` | `0` | `0` |

In particular `y=-ag x` on **the same** S, and the six `Z2` sign products are not arbitrary frequency-by-frequency. Conversely this table makes every individual four-point inverse ternary, but it does **not** supply the missing global Walsh, original-rank, atom, balance, T or complementary-v conditions. It gives energies `sum x^2=56`, `sum y^2=128`, `sum g^2=136` and the stated counts; none of these is a global witness.

For the actual caller, simultaneously and at every one of 64 frequencies,

`xhat in {0,+8,-8}`, `yhat in {+4,-4,+12,-12}`.  (3.1)

Define from these same physical `x,y`, not as separate choices,

`z_x(omega)=xhat(omega)/8 in {0,+1,-1}`,
`w_y(omega)=yhat(omega)/4 in {+1,-1,+3,-3}`.

Parseval gives `|Z|=8` for `Z={omega:z_x(omega)=0}` and `|M|=8` for `M={omega:|w_y(omega)|=1}`. In particular `t in Z`.

## 4. New uniform zero-flat, coset balances and matched-y restriction

**Proposition.** Under Sections 1--3, `Z` is an affine three-flat. Since it contains the specified `t`, there is a unique three-dimensional spatial subspace `L` such that

`Z=t+L^perp`.  (4.1)

For **every** coset `C` of this same `L`,

`sum_{c in C} (-1)^(t.c) x(c)=0`.  (4.2)

Consequently each `|S intersect C|` is even, and, with the physical signs of Section 3,

`sum_{S intersect C} (-1)^(t.c) epsilon_x(c) + 2 sum_{(D0 union Z2) intersect C} (-1)^(t.c) epsilon_x(c)=0`.  (4.3)

For example, if `C` misses S, it must contain an even number of `D0 union Z2` sites; the complete signed equality (4.3) is stronger. These are exclusions for every candidate `L`, every physical placement and every actual transported `t`.

Now define, on the eight cosets `Q=F2^6/L`, the **same-y** integer

`h(C)=(1/2) sum_{c in C} (-1)^(t.c) y(c)`.

It is integral because (4.2) gives an even number of S sites in each C and `x,y` have the same parity pointwise. Let `k=|M intersect Z|`, so `0<=k<=8`. For every `mu in L^perp`, with characters of Q written `(-1)^(mu.C)`,

`sum_C h(C)(-1)^(mu.C) = yhat(t+mu)/2 in {+2,-2,+6,-6}`;  (4.4)

exactly `k` of these eight values have magnitude 2. In particular

`sum_C h(C)^2 = 36-4k`,  and  `sum_C h(C)(-1)^(mu.C) = 2 (mod 4)` for every `mu`.  (4.5)

The same physical `h` can be read without independently assigning a spectrum: because of (4.2), it is also `sum_{c in C} (-1)^(t.c)(x(c)+y(c))/2`. Thus its site contributions are `epsilon_x` on `{c in S:ag=-1}`, zero on the other S sites, `epsilon_x` on D0, `epsilon_y` on D3, `epsilon_x+epsilon_y` on Z2, `2 epsilon_y` on Z4, and zero on F or Z0, all multiplied by the displayed balance character. This retains the actual `a/g` signs and both members of each `Z2` pair.

**Sharp endpoint profiles.** If `k=8`, the eight coset values of h are exactly either (i) one `+2` or `-2`, all others zero, or (ii) four values `+1` or `-1` on an affine two-plane of Q, with sign product `-1`, and all others zero. If `k=0`, the only profiles are the same two forms multiplied by 3: one `+6` or `-6`, or four values `+3` or `-3` on an affine two-plane with sign product `-1`. Conversely these profiles have precisely the indicated eight restricted-transform magnitudes. For `1<=k<=7` the complete necessary conditions are (4.4)--(4.5); no endpoint rule is silently extended to them.

**Proof of (4.1)--(4.5).** Since `xhat=8 z_x`, Walsh inversion gives `Walsh(z_x)(c)=8x(c)`. For any product of at most two coordinate bits of a frequency, its sum weighted by `z_x` is even: expand each bit as `(1-chi)/2` and use divisibility by 8. The indicator `q=1_Z` is `1+z_x mod 2`, so its inner product over F2 with every monomial of degree at most 2 vanishes. By the Boolean Möbius coefficient formula, every algebraic-normal-form coefficient of q of degree at least 4 vanishes. Thus `deg q<=3` and `wt(q)=8`.

For completeness, the minimum-weight fact used here is elementary: a nonzero Boolean polynomial of degree at most r in n variables has weight at least `2^(n-r)`; equality forces its support to be an affine `(n-r)`-flat. Induct by writing `f=h+x_n g`. If `g=0`, use the induction hypothesis and take a cylinder. Otherwise `wt(f)>=wt(g)>=2^(n-r)`; equality forces g to be a minimum word and the supports of `h` and `h+g` to partition its affine support. Outside that support h vanishes; after affine coordinates on it, the degree bound makes its restriction affine, so the resulting support is an affine graph. The standard r=0 and r=n bases are immediate. With n=6,r=3, q's eight points are an affine 3-flat, and `t in Z` gives (4.1).

For (4.2), Fourier inversion on the quotient by L says that vanishing `xhat(t+mu)` for all `mu in L^perp` is equivalent to all eight twisted coset sums vanishing. The table gives (4.3). Fourier inversion on Q gives (4.4); Parseval on Q gives (4.5), since the eight squared `yhat` values on Z comprise k copies of 16 and `8-k` copies of 144.

For the endpoint profiles, first let every transform in (4.4) have magnitude 2. Parseval gives `sum h^2=4`. An integer vector of that norm has either one entry `+/-2`, or four entries `+/-1`. In the latter case the four occupied cosets must XOR to zero, because all eight transforms are 2 modulo 4; hence they form an affine two-plane. Their sign product is `-1`, again from the transform at zero modulo 4. Conversely the Walsh transform of an odd-sign four-point plane has magnitude 2 at every character. When the eight magnitudes instead all equal 6, inversion gives `h(C)=(3/4) sum_mu epsilon_mu (-1)^(mu.C)`. Integrality forces every h(C) to be divisible by 3, so divide by 3 and apply the preceding classification. This proves both boundaries.

## 5. New global mixed-amplitude identities, all 64 shifts

Define `H(c)=a(c)g(c)` on S and zero elsewhere; this is already the actual pointwise product because a vanishes outside S. Define the **single physical** signed six-site function `zeta(c)=epsilon_x(c)epsilon_y(c)` on Z2 and zero elsewhere. The table implies, pointwise,

`x y = -H+4 zeta`,
`x^2=1_S+4 1_{D0}+4 1_{Z2}`,
`y^2=1_S+4 1_{D3}+4 1_{Z2}+16 1_{Z4}`.  (5.1)

Therefore for **every** `d in (F2^6)*`, including `d=0`, all of the following must hold with the **same** z_x, w_y, placements and six signs:

`sum_omega z_x(omega) w_y(omega+d) = -2 Hhat(d)+8 zetahat(d)`,  (5.2)

`sum_omega z_x(omega) z_x(omega+d) = (1_S)^hat(d)+4 (1_{D0})^hat(d)+4 (1_{Z2})^hat(d)`,  (5.3)

`sum_omega w_y(omega) w_y(omega+d) = 4(1_S)^hat(d)+16(1_{D3})^hat(d)+16(1_{Z2})^hat(d)+64(-1)^(d.Z4)`.  (5.4)

Here `d.Z4` denotes evaluation at its unique point. The factors follow from `Walsh(fg)(d)=1/64 sum_omega fhat(omega) ghat(omega+d)`: `8*4/64=1/2`, `8*8/64=1`, and `4*4/64=1/4`. At `d=0`, (5.3)--(5.4) recover 56 and 512 respectively; no nonzero shifts are discarded.

Since zeta consists of **exactly six** signed points, `zetahat(d)` is an even integer between -6 and 6. Consequently, setting `C(d)=sum_omega z_x(omega) w_y(omega+d)`,

`C(d)+2 Hhat(d) in {-48,-32,-16,0,16,32,48}` for every d.  (5.5)

Equivalently `C(d)=-2 Hhat(d) (mod 16)` and `|C(d)+2 Hhat(d)|<=48`, together with the stronger requirement in (5.2) that **one common six-site signed zeta** realizes all 64 corrections. Explicitly,

`Hhat(d)=sum_{z in S_E} a(000,z)(-1)^((d_j,d_p).z) + sum_i q_i (-1)^(d_Y.Y_i) sum_{z in S_i} a(Y_i,z)(-1)^((d_j,d_p).z)`.

Thus the residue is tied to the actual signed g/a geometry of Section 2, while z_x and w_y come from the same physical x/y and include the designated balance zero and all magnitudes. These equations are not two separate energy spectra.

The mixed congruence is a genuine extra coupling even at the level of formal individual amplitude data: fix arbitrary signless admissible Z, M and t, fix any allowed signs of z_x and w_y, and reverse one w_y sign at a frequency outside Z. Individual spectral magnitudes, their energies, Z, M and the x balance zero do not change, but `C(0)` changes by `2 z_x(omega) w_y(omega)`, which is `+/-2` or `+/-6`, never 0 modulo 16. At most one of the two sign assignments satisfies (5.5) for the same H. This is only a formal non-redundancy argument; neither sign assignment is claimed to have a legal inverse or be an original caller.

An additional consistency check, **already following from the a/g spectra alone**, is worth retaining but is not claimed as new x/y progress: with `N={c in S: a(c)g(c)=-1}`, one has `XOR(N)=XOR(F)`. Indeed `ghat` and `ahat` are both 4 modulo 8 at every frequency, so `(g-a)/2` has Walsh coefficients divisible by 4 and the XOR of its odd support `N union D` is zero. The XOR of S is zero because `ahat` is divisible by 4; the XOR of all five occupied eight-point Y rows is zero, so `XOR(D)=XOR(S)+XOR(F)=XOR(F)`. The common-coset h values in Section 4 have parity `|(N union D) intersect C| mod 2`; the sharper energy, endpoint and mixed-amplitude conditions above are not replaced by this consistency observation.

## 6. Exact remaining step and limits

The resulting necessary system quantifies over every `A,B`, all line/offset/normal placements, the specified common q signs, all matched peak phases and sign choices satisfying Section 2, every 4-of-22 `D0`, every 6-of-24 `Z2` and distinct `Z4`, every physical x/y sign choice, every three-plane L and the **actual** transported t. Sections 4--5 impose all eight same-u coset balances, the full eight-entry matched-y transform and energy, and all 64 mixed and square-correlation equations. Any violation is a written exclusion of that precisely quantified placement. The first remaining step for a whole-branch no-go is to prove that **no** such jointly realizable assignment survives these restrictions together with all 64 full y amplitudes and every original rank/atom/cross-fibre/T requirement. That nonexistence is not proved here. Nor is any surviving assignment proved to exist.

The actual complementary `v` must still occupy exactly the 140 zeros of this same u, satisfy all 256 odd-half Walsh caps, the negative-sign/XOR condition, and reconstruct the original F and selected T. S4's complete 512-shift Boolean caller and the actual original balance are not consequences of this candidate. No full split-branch exclusion, other-branch claim, global NL242 theorem, novelty/priority, family/human/formal/kernel acceptance or source authentication is claimed.

## 7. Read, execution and provenance declaration

Before mathematical-body access I read the complete f847 manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual dispatch receipt and **all 23** listed status-only controls. I wrote `prebody-ack-v1.md` at a path observed absent in this exclusively owned wave directory, then sent the separate direct acknowledgement to Main; both preceded body access. The first ordinary administrative displays collapsed JSON and one dispatch line; each was reread completely in raw form before acknowledgement. Status controls were not mathematical inputs.

After direct delivery I read **all 307 LF**, including the ending, of the sole literal packet part in ordered raw windows `1-20,21-40,...,281-300,301-307`, each at most 20 LF and below 30,000 displayed bytes; no literal-packet clipping was observed. These windows include the complete S1/S2/S3/S4/S5 bodies (27/46/37/162/13 source LF respectively). The supplied part metadata is SHA-256 `4e77cd601badd5989e0860ff2b4a21af21aca1d789c53b40f7b9e5dd1d47d2a3`, 49,448 bytes. Supplied source pins are S1 `f108ac85228bef8faf291e288b6f3caac46d8c7463f423a48f5914836fd74f5a`; S2 `a164bdb842e0c201e94aeb7356e6bba308eea5f5b8ba6d80473bafd6dce832c4`; S3 `2aa39512cf0ef6d1194cc8257dfe722cf9a58b62f637baf9056e08355b4423f0`; S4 `117149fa1734b863b21a37197217b4d8f111ac455194d445c25d0bc95d420de1`; S5 `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef`. These are parent-supplied metadata, not an independently executed hash check. Source links in the packet were not opened. All genuinely held episodes and their proof/method/planning/selection/verification/reporting/confidence/downstream consumers remain NONINPUT. No scientific code, test, compilation, solver, external model, network, child subprocess or finite execution was used; no verifier code was prepared, so no code hash exists. No process deviation is known in this worker's actual sequence; this is not a certificate about unobservable prior cognition.
