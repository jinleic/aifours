# Named six-span together branch: a common-fibre spectral and parity obstruction

**Status: author candidate, conditional necessary invariants and excluded subfamilies; the whole together branch is NOT proved impossible.** The quantified object is one original balanced Boolean function on `F_2^9`, with its actual nonzero selected support XOR `T`, Walsh cap 28, `m=116`, original rank-two quadratic/eight-zero residual, labelled small-fibre counts `(0,4,8)`, `G3=1` meaning 23 spatial `U3` zeros, and the explicitly local `H_loc=0`: no `U1=0` block has an `|U0|=4` peak. Restrict to the affine-six-span branch in which both `|g|=4` blocks occur in the same odd row. All conclusions below refer to the SAME actual pairfunction, common coordinates and four fibres, for BOTH retained frequency matchings, every admitted sign/offset, and every transported original-balance frequency. They do not cover the split branch, other `m=116` classes, `m=114`, or global NL242.

The branch geometry and the atom/caller boundary are imported conditionally from the complete literal bodies S1–S5, especially S2 lines 7–32, S3 lines 5–33 and S4 lines 37–153. In particular, the f244 weight-four/even-syndrome atom boundary and its named original residual are not separately source-authenticated here; links in the packet were not followed. Local `H_loc` is exactly the definition above, not an identification with an undisplayed historical class. No fixture, independent choice of rows, or arbitrary local inverse is asserted to be an original caller.

## 1. One actual shell and the two matchings

Write the common 64-block coordinate as `(y,z) in Y x Z`, with `Y=Z=F_2^3`, and `z=(j,t')` with `j in F_2` and `t' in F_2^2`. Put

`x=U0`, `a=U1/3`, `g=U2`, `h=U3`, and `4u=x+3a chi_1+g chi_2+h chi_3`.

The four normalized small `g` frequencies are `A={0,e1,e2,e3}` in `Y*`, all with coefficient `+4`; put `xi=e1+e2+e3`, embedded in `(Y x Z)*` with zero `Z*` component. The four odd `y` rows are `e1,e2,e3,xi`; let `y_F` denote the full-block row, and `I={0} union (odd rows minus {y_F})`. The four occupied `a`-planes are indexed by `i in I`, with `y_0=0`. Their exact forms are

`P_0={z:n(z)=0}`, `P_i={z:m_i(z)=beta_i}` for `i!=0`,

where `n(j,t')=j`, `beta_0=0`, the full blocks are `(0,t0)` and `(1,t1)` in row `y_F`, `D=(1,t0+t1)`, and the four normals are precisely

`{m_i:i in I}={m in Z*:m(D)=1}`, with `m_0=n`.

Thus each `P_i` is an actual affine two-plane, with direction `W_i=ker m_i`; the signs of `a` on each are restricted characters. On the E row `g=3 1_{P_0}-2`. On each occupied odd row `g=epsilon_y(3 1_{P_i}-2)`; on `y_F`, `g=epsilon_y(6 1_F-2)`, where `F` is its two full points. On the other three rows `g=0`. The four actual `epsilon_y` have product `-1`. The two actual `a` peaks on each plane have frequency pair `{theta_i,theta_i+m_i}`; these four pairs partition all eight `Z*` frequencies. Equivalently, on `C=D^perp`, the pair map is `v -> n+Lv+b`, with `L` one of the TWO order-three elements of `GL(2,2)` and `b=(I+L)v_0` fixed by the actual E pair. No extra matching or arbitrary independent phase rows are allowed.

The same local inverse gives `|S|=16`, `S=supp a=union_i ({y_i} x P_i)`, with `x,h,g,a` all odd on `S`, `x,h,g,a` even off `S`, and on `S`

`x,h,g,a in {+1,-1}` and `h=-a g x`.                                                   (1)

The physical census off `S` is four `D0` sites `(g,x,h)=(+/-2,+/-2,0)`, eighteen `D3` sites `(+/-2,0,+/-2)`, two full `g` sites `(+/-4,0,0)`, six `Z2` sites `(0,+/-2,+/-2)`, one `Z4` site `(0,0,+/-4)`, and seventeen zero sites. Consequently `sum x^2=56`, `sum h^2=128`; the six `Z2` sites lie among the THREE nonzero even `y` rows, since the E and odd rows have nonzero `g` everywhere. This is a statement about the same `u`, not separately realizable spectra.

All 64 unnormalized transforms obey `hat x in {0,+/-8}` with exactly eight zeros, `hat a=4 sigma` with `sigma in {+/-1}`, `hat g=4 kappa` with `kappa in {+/-1,+/-3}`, and `hat h=4 rho` with `rho in {+/-1,+/-3}`. The set `A={|kappa|=1}` has four elements and `H={|rho|=1}` has eight; their remaining coefficients have magnitude three in these normalizations. Let `t` be the SPECIFIC transform of the original DC under the entire common affine/modulation normalization. Original balance is the exact condition `hat x(t)=0`, not the existence of some subsequently selected zero.

## 2. New common x/h plane-profile and support obstruction

**Claim 1.** The eight zeros of `hat x` are `t+L^perp` for a UNIQUE three-dimensional spatial subspace `L <= Y x Z`. For `X(c)=(-1)^(t.c)x(c)` and every coset `C=c+L`,

`sum_{l in L} X(c+l)=0`, hence `|S intersect C|` is even.                           (2)

Moreover, for each character `e in L*`, define, using an arbitrary representative `c` of each coset,

`X_e(C)=sum_{l in L} X(c+l)(-1)^{e(l)}`,
`H_e(C)=sum_{l in L} (-1)^{t.(c+l)}h(c+l)(-1)^{e(l)}`.

Changing representative can change a sign, not any displayed square. Set

`k_e=|{r in H+t : r|_L=e}|`, so `0<=k_e<=8` and `sum_e k_e=8`.

On these SAME eight cosets, simultaneously,

`X_0(C)=0` for every C;  `sum_C X_e(C)^2=64` for each nonzero e;                 (3)
`sum_C H_e(C)^2=144-16 k_e` for every e.                                          (4)

Every `X_e(C)` and `H_e(C)` is even. Equivalently, their halves have squared sums `16` in (3) and `36-4k_e` in (4). The autocorrelation of the actual `x` is also

`sum_c x(c)x(c+v)=64 1_{v=0}-8(-1)^{t.v}1_L(v)` for EVERY `v`.                   (5)

**Proof.** Put `zeta=hat x/8` on the 64-frequency space. Then `zeta in {0,+/-1}`, its zero set `Z_x` has size eight, and `hat zeta=8x`. On every affine codimension-two frequency flat, the sum of `zeta` is one quarter of four values of `hat zeta`, hence is even. The flat has 16 elements, so `1_{Z_x}` has even sum there too. These flat indicators span the Boolean monomials of degree at most two. Therefore, writing the algebraic normal form of `1_{Z_x}`, any maximal monomial of degree at least four would pair nontrivially with its complementary monomial of degree at most two, a contradiction: `deg 1_{Z_x}<=3`.

For completeness, the minimum-weight/equality fact used now has this direct induction proof. A nonzero degree-at-most-`r` Boolean function in `n` variables has weight at least `2^(n-r)`; at equality its support is an affine codimension-`r` flat. Split `f=f0+x_n g`. If `g=0`, use induction on `f0`. If `g!=0`, `wt(f)>=wt(g)>=2^(n-r)`. At equality, induction makes `supp g` an affine codimension-`r-1` flat, and `f0` vanishes off it. In affine coordinates `g` is the product of its `r-1` defining affine factors; the degree bound forces `f0=g h` with `h` affine on that flat. Thus `supp f` is cut out by those factors and one further affine equation. The usual constant/full-space boundary cases start the induction. Applying it at `(n,r)=(6,3)` gives an affine three-flat. Since the actual `t` is a zero, it is `t+L^perp` for unique `L`.

After the common modulation by `t`, every Fourier coefficient of `X` on `L^perp` is zero; Fourier inversion on the quotient gives the first part of (2). Reducing it mod two gives the second because `x` is odd exactly on `S`. Fourier Parseval on each coset of `L^perp` gives (3) and (4): the eight entries in a nonzero `L*`-frequency class of `hat X` have squares 64, while the eight entries of `hat h` have squares 16 at `k_e` positions and 144 at the others. The zero coset has `X_0=0`. The `H_e` are even because `h` and `x` have the same pointwise parity and the `X_0` sums vanish mod two; all `X_e` are even for the same reason. Finally (5) is inverse Fourier transform of `|hat x|^2=64(1-1_{t+L^perp})`. No spectral sign is freely reassigned in this argument. QED.

## 3. Explicit geometric exclusions on the actual zero flat

Let `d=dim(L intersect Z)`, where `Z` denotes `{0} x Z`, and `P=pi_Y(L)`. The following are NECESSARY for each actual object, including every offset, physical sign and either actual matching:

* `d=0`: `L` is the graph of a unique linear `J:Y->Z`; necessarily
  `sum_{i in I} [beta_i+m_i(J y_i)]=0` in `F_2`.                             (6)
* `d=1`: write `L intersect Z=<w>` with `w!=0`; `P` is a two-plane in `Y`.
  * If `w=D`, then `y_F in P`.                                                (7)
  * If `w!=D`, exactly two of the four `m_i` satisfy `m_i(w)=1`. If their row labels are `y_i,y_j`, then `y_i+y_j in P`.                              (8)
* `d=2` or `d=3`: the parity assertion (2) imposes no further restriction on `L` alone; the full signed equalities (2)–(5), physical census, and all other conditions remain mandatory.

**Proof.** For a support plane `P_i`, its intersection with an `L`-coset is empty or has size `2^{dim(W_i intersect L)}`. Thus only planes with `W_i intersect L=0` contribute to the parity in (2).

When `d=0`, identify `(Y x Z)/L` with `Z` by `(y,z)->z+Jy`. All four planes contribute and their images are `m_i(z)=beta_i+m_i(Jy_i)`. The `F_2`-sum of their four indicator functions is `sum_i [beta_i+m_i(Jy_i)] + (sum_i m_i)(z)`. The four normals form the affine plane `{m:m(D)=1}`, so their XOR is zero. Equation (6) follows, and is exactly the parity condition in this case.

When `d=1`, an `m_i` contributes iff `m_i(w)=1`. Its image in the quotient is the inverse image of the single class `y_i+P` in `Y/P`: indeed `W_i+<w>=Z`. If `w=D`, all four contribute. Their parity vanishes iff their four row labels have XOR in `P`. The XOR of `0` and the three non-full odd labels is `y_F`, proving (7). If `w!=D`, evaluation at `w` is nonconstant on `{m:m(D)=1}`, so exactly two contribute; their image hyperplanes coincide exactly when `y_i+y_j in P`, proving (8). If `d>=2`, `dim((L intersect Z) intersect W_i)>=1` for every i, so every intersection multiplicity is even. QED.

These exclude genuine entire geometric subfamilies, not just a numerical example. For instance, for ANY admitted together-branch shell choose a two-plane `P` not containing the actual nonzero `y_F` and take `L=P x <D>`. This is a legitimate three-space with `L intersect Z=<D>` but violates (7); hence no same-physical-`u` completion can have zero flat `t+L^perp`, irrespective of phases, signs, matching or `t`. This is a formal choice of a putative zero-flat direction, NOT a constructed caller or a claim that every other choice is attainable.

## 4. New six-site common-fibre convolution invariant

Define the actual signed six-site function

`w(c)=[x(c)h(c)+a(c)g(c)]/4`.                                                   (9)

By (1) and the complete local census, `w` is zero outside the actual six `Z2` blocks and takes `+1` or `-1` on each of them. Thus its support is exactly six sites in the three nonzero even `y` rows. This uses one common `u`; an arbitrary independent `x`/`h` assignment cannot be substituted.

For every 64-frequency `r` define, with all sums in `F_2^6`,

`B(r)=sum_s [ sigma(s) kappa(r+s) + 2 zeta(s) rho(r+s) ]`.                     (10)

Then the following simultaneous, signed, 64-frequency conditions are necessary:

`B(r)=16 hat w(r)`, so `B(r) in {-96,-64,-32,0,32,64,96}`;                    (11)
`sum_r B(r)^2=98304`;                                                         (12)
`B(r+xi)=B(r)` for every `r`, and `sum_{alpha in Y*} B(alpha,eta)=0` for every `eta in Z*`;  (13)
`B(r)/32 = 3+N_-(w)+(XOR_{c in supp w} c).r (mod 2)`.                         (14)

In (14), `N_-(w)` counts its negative sites; the physical XOR vector has even `y` parity. Equivalently the inverse 64-Walsh transform of `B` is exactly `1024 w`: precisely six `+/-1024` values at the actual `Z2` sites and zero at all other 58. This is stronger than testing the `x` and `h` caps, or the `a` and `g` shell, separately.

**Proof.** At `S`, (1) gives `xh+ag=0`; at `D0`, `D3`, both full-block types and zero sites both products vanish; at each `Z2`, `xh=+/-4` and `ag=0`. This proves (9) and support. The unnormalized product-convolution formula gives

`widehat{xh+ag}(r)=(1/2) sum_s zeta(s)rho(r+s)+(1/4) sum_s sigma(s)kappa(r+s)=B(r)/4`.

Since `xh+ag=4w`, (11) follows. Parseval and `sum w^2=6` give (12). The support has `xi.y=0` and excludes `y=0`: these respectively give the two identities in (13). Finally expand six signed characters modulo four: `hat w(r)/2 = 3+N_-(w)+(XOR supp w).r (mod 2)`, proving (14). QED.

## 5. Original eight-atom overlap: exact slice restrictions on h

The named S4 atom boundary supplies, conditionally and for this same `h`, `XOR H=xi`, equality of the products of the small-atom signs of `g` and `h`, and `|(A+lambda) intersect H|<=2` for EVERY `lambda in F_2^6`. Since the four `g` signs in `A` are normalized positive, the product of `rho` on `H` is `+1`. The original additional atom shape is also retained: `H` has affine rank six and can be written as one four-point affine plane of sign product `+1` plus four other points, with the six indicated differences independent, exactly as S4 lines 107–113. This shape is a conditional import, not newly certified.

For each `eta in Z*`, let `H_eta={alpha in Y*:(alpha,eta) in H}` and `n_eta=|H_eta|`. Then:

1. `n_eta<=4`. If `n_eta=3` or `4`, its points lie in a two-plane whose nonzero normal is one of `110,101,011` (coordinates dual to `e1,e2,e3`). For `n_eta=4` it is the entire such plane. In particular a four-slice has XOR zero.
2. The number of odd `n_eta` is `0`, `4`, or `8`; in the middle case their four distinct `eta` form an affine two-plane. If it is `8`, each slice is a singleton, giving a graph `alpha=phi(eta)` with `XOR_eta phi(eta)=xi`: each coordinate of `phi` has cubic ANF coefficient one.
3. The complete possible occupancy MULTISETS, before imposing the remaining sign, rank, convolution and balance restrictions, are
   `(2,2,2,2)`, `(4,2,2)`, `(4,1,1,1,1)`, `(2,2,1,1,1,1)`, `(3,2,1,1,1)`, `(3,3,1,1)`, or eight `1`s. Zeros are omitted. In `(4,2,2)`, the XORs of the two two-point slices sum to `xi`. No listed profile is claimed realizable.

**Proof.** At fixed `eta`, any three points lying in a plane with normal `100,010,001` or `111` are a translate of three elements of `A`: translate the missing corner of the relevant three-corner subset as needed. The all-translation intersection bound forbids them. Each such normal partitions the cube into two planes, each containing at most two points of `H_eta`, so `n_eta<=4`. A three-set spans a plane, whose normal must therefore be one of the other three nonzero normals. For a four-set, balance on the two planes normal to each coordinate gives XOR zero; four distinct points of `F_2^3` with XOR zero form an affine plane, and its normal cannot be one of the forbidden four.

The `Z*` component of `XOR H=xi` says the XOR of the `eta` with odd `n_eta` is zero. There are an even number of these because `|H|=8`; exactly two cannot XOR to zero, and exactly six cannot either because the XOR of all eight `eta` is zero and the two omitted distinct indices do not XOR to zero. Four distinct indices XOR to zero exactly when they form an affine two-plane. Enumerating the remaining total weight eight gives the displayed profiles, except that two four-slices are excluded by their zero `Y*` XOR, since the `Y*` component of `XOR H` is `xi!=0`. The two two-slices in `(4,2,2)` must consequently XOR to `xi`. The singleton-graph statement follows because the XOR of a Boolean function over all inputs is its full cubic ANF coefficient. QED.

In addition, do not drop the full S4 sign-mismatch conditions: for every `lambda`, with `d_lambda(r)=[sign kappa(r+lambda)-sign rho(r)]/2`, require `sum_r d_lambda(r)=0 (mod 4)` and `XOR_{r:d_lambda(r)!=0} r=0`. Equations (3)–(14), the atom profile, and these constraints all refer to one actual `x,a,g,h`; checking them separately on unrelated arrays is insufficient.

## 6. Original J1, complement, and exact remaining boundary

For every one of the 64 block frequencies and every internal two-bit point `b`, the actual original inverse gives

`[hat x+3 chi_1(b)hat a+chi_2(b)hat g+chi_3(b)hat h]/4` an odd integer.       (15)

Indeed `hat x=0 (mod 8)` while the other three summands are each `4 (mod 8)`. This is the `J=1` residue, not a replacement for any of the ALL-64 spectral caps or the original-caller conditions. In particular (15) does not assert that the normalized DC is balanced: only the specified `hat x(t)=0` is the transported original balance. The original quadratic `q=k/2 mod 2` on `K=T^perp`, its polar rank two, radical and exact fibre/zero conditions, and the original 512-frequency Boolean inverse/correlation must all hold on restoring the original coordinates. They are not implied by the local equations above.

A genuine complementary half `v` must be `+/-1` exactly on the 140 zero positions of this SAME `u`, zero elsewhere, and satisfy all 256 odd-half caps `|hat v|<=14`. Its values have magnitudes `2,6,10,14`; with counts `N2,N6,N10,N14`, Parseval implies

`3(N14-N2)-2N6=320`, `N6=2 (mod 3)`, `N14>=108`.

At equality the unique necessary tally is `(N2,N6,N10,N14)=(0,2,146,108)`. This is not a signed spectrum or existence claim. The actual reconstructed XOR must equal the original selected `T`. In the ORIGINAL decomposition `V=a0^perp`, after restoring balance, the 58 negative `u` pairs give

`XOR_{f=1} x = (XOR_{y:u(y)=0} y) + (58+#{y:v(y)=1} mod 2)T = T`.              (16)

Because `V` and `<T>` are complementary, (16) imposes the zero-support XOR in `V` and odd parity of `#{v=1}`. This must be transported through the actual common coordinate changes; the 58-pair statement cannot be inferred at the normalized unbalanced DC. The original full-caller identity for `k=W/4`, `sum_a k(a)k(a+b)=2^14 1_{b=0}` for every one of the 512 shifts, remains required in addition to complementary support and separate caps.

**Unpaid frontier.** It remains to decide whether ANY one of the two actual matchings, with all shell parameters, actual zero-flat directions surviving (6)–(8), one physical pair `(x,h)` satisfying (1)–(5), (9)–(15), full local census, all original rank/atom/shear conditions and specified `t`, admits an original complementary `v` satisfying (16), all 256 caps and the complete Boolean caller. The first open step is the simultaneous feasibility/exclusion of this explicit system; no such solution or whole-branch contradiction is claimed. These necessary conditions exclude, in particular, the full quantified zero-flat subfamilies violating (6), (7), or (8), and any full common spectrum violating (3)–(5) or (9)–(14). They give no independent-family, human, formal/kernel, priority, novelty or global NL242 acceptance.

## 7. Read, provenance and method declaration

Before any mathematical body read or reasoning, I completely read the wave's manifest, freeze receipt, final binding, live metadata, actual-dispatch receipt, and all 23 listed status-only controls; created `prebody-ack-v1.md` as a new file; and directly delivered the prebody ACK to Main. Status-only material is not a mathematical input. The parent-supplied administrative bindings are not independently recomputed hashes or a cognition certificate.

Thereafter I read `literal-packet-part-01-v1.md` completely and in order in raw windows LF `1-20,21-40,41-60,61-80,81-100,101-120,121-140,141-160,161-180,181-200,201-220,221-240,241-260,261-280,281-300,301-307`, including the terminal line; no window was over 20 LF or 30,000 displayed bytes, and no clipping was observed. This covers the entire rendered bodies S1 `1-27`, S2 `1-46`, S3 `1-37`, S4 `1-162`, S5 `1-13`, with their packet headers and endings. The supplied packet pin is SHA-256 `4e77cd601badd5989e0860ff2b4a21af21aca1d789c53b40f7b9e5dd1d47d2a3`, 49,448 bytes/307 LF; this is parent metadata, not a self-run hash. No linked body, held episode, held consumer, sibling science, external source/model, code, solver, subprocess, scientific execution, test, compilation or independent validation was used. No verifier was prepared, so there is no prepared-code hash. There is no known clipping-recovery or process deviation to report; this author candidate has not received a separate parent disposition.
