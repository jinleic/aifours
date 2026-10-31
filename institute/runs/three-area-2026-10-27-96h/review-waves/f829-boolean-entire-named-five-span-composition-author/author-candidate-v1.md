# Entire named five-span obstruction: same-object graph-rank composition

**Status: GENERAL AUTHOR candidate; conditional on the named source theorems below, not a parent disposition.** For every original Boolean object satisfying the exact named residual and its specified source imports in §1, its actual 16-point support cannot have affine span five. Consequently, **if such an original object exists**, it has affine span six and satisfies exactly one of the two six-span occupancy alternatives in §7. The conclusion is necessary, not an existence theorem and not an exclusion of the named residual in its entirety. In particular it is not an NL242 theorem.

The new composition is the audit in §§2–6: the two graph-polar ranks concern the *same* normalized physical pairfunction; the rank-four obstruction and the later whole-rank-two obstruction apply to that object, including its specifically transported original DC zero. The full rank-two no-go is an explicitly named **conditional import** from S4, not a proof body reproduced by this packet. The rank-four argument and the interface calculations are reconstructed here. No independent construction of spectra, alternative `u`, eight-halfblock recipe, complementary witness, or replacement balance frequency is used.

## 1. Quantifiers and original-object boundary

Work over `F_2`. For **every** original Boolean function `F:F_2^9→F_2` in the following explicitly named caller, put `s=(-1)^F`, `S_F={x:F(x)=1}`, `T=⊕_{x∈S_F}x`, `W(a)=Σ_x s(x)(-1)^{a·x}`, and `k(a)=W(a)/4`. Require the original balance `|S_F|=256`, the original Walsh bound `|W|≤28`, and the selected **actual** `T≠0`; `T` is not a free parameter chosen after normalization. The f263/f244 named residual is imported at precisely the scope displayed in S9: on `K=T^⊥`, the quadratic `q_K(a)=k(a)/2 mod 2` has alternating polar rank two, radical `𝓡` of dimension six, `q_K|𝓡=0` and exactly 64 quadratic-zero positions; the original Walsh spectrum has eight zeros, all in `𝓡`. Choose an allowed complement `P`, so `K=𝓡⊕P`; label its nonzero elements `1,2,3=1+2` with the numbers of `|k|=2` atoms `(e1,e2,e3)=(0,4,8)`. Retain the named `m=116`, `G3=1`, and the **explicit local** condition

`H_loc = #{c : U1(c)=0 and U0(c) has a single |U0|=4 peak}=0`.

Here the named G3 source import includes `#{c:U3(c)=0}=23`; the eight-atom weight-four/even-syndrome relation and the other original-atom facts needed by S8 remain at S9's expressly named f244 import boundary. No definition of an undisplayed historical H class or proof that it is identical to `H_loc` is supplied. Nor is equivalence with an original printed source asserted.

Choose `a0·T=1`, `V=a0^⊥`, and form the **actual** pairfunctions, for `y∈V`,

`u(y)=(s(y)+s(y+T))/2`, `v(y)=(s(y)-s(y+T))/2`.

Thus `u,v∈{0,±1}`, `u²+v²=1`, `uv=0`, `Σu=0`, `Σu²=116`, `Σv²=140`. S9 gives `Walsh_V(u)(a)=2k(a)` and `Walsh_V(v)(a)=2k(a0+a)`; both come from this one `F`. Identify `V=𝓡*⊕P*`, write `(c,w)` with `c∈𝓡*≅F_2^6`, `w∈P*≅F_2^2`, and let

`U_j(c)=Σ_w u(c,w)(-1)^{j·w}`, `a=U1/3`, `g=U2`, `x=U0`, `y=U3`.

For the same 64 `c` and the same `u`, the inverse is

`u(c,w)=[x(c)+3a(c)χ1(w)+g(c)χ2(w)+y(c)χ3(w)]/4`.  (1)

The original `rank two` is the rank of the polar of `q_K` on the eight-dimensional frequency space. It must **not** be confused with rank two or four of the four-variable graph polar below. The imports S8 (the actual caller's XOR/span dichotomy), S6 (its all-graph normalization), S7 (the same-block four-fibre criterion) and S4 (the whole physical graph-polar-rank-two no-go) are all conditional source theorems, not consequences of independently selected local arrays.

## 2. One common physical census and carried balance

The fibre identities `hat U_j(r)=2k(r,j)` give, on the same arrays,

`Σx²=56`, `Σ(3a)²=144`, `Σg²=136`, `Σy²=128`;

`hat x∈{0,±8}`, `hat(3a)∈{±12}`, `hat g∈{±4,±12}`, `hat y∈{±4,±12}`, with exactly four small coefficients of `hat g` and eight of `hat y`. These statements include all 64 frequencies. There are 16 `U1=±3` blocks, each with three nonzero entries and `|x|=|g|=|y|=1`.

On the remaining 48 actual ternary four-point blocks the only nonempty transform forms have either a single peak of magnitude four or two entries of magnitude two. The named `H_loc=0` rules out the `x` peak. The `g` energy gives two full `g` peaks and 22 blocks with `|g|=2`. On these 22 let `D0` mean `(x,y)=(±2,0)` and `D3` mean `(0,±2)`. Among the 24 blocks with `U1=g=0` let `Z0=(0,0)`, `Z2=(±2,±2)`, `Z4=(0,±4)`.

If `d=#D0`, `p=#Z2`, and `z4=#Z4`, then actual support, actual `x` energy, and the imported 23 `y`-zeros respectively yield

`p+2z4=8`, `d+p=10`, `23=20+3z4`.

For the last equality, the zeros are the two full `g` blocks, `d` D0 blocks and `24-p-z4` Z0 blocks. Therefore

`#D0=4, #D3=18, #Z2=6, #Z4=1, #Z0=17`,  (2)

and the four D0 locations are actual blocks, not freely chosen spectral entries. The resulting `y` energy is `16+18·4+6·4+16=128`. This census is already in S9; it is not an original class-table identification.

On every S point the inverse (1) with `U1=3a` forces

`y=-a g x`.  (3)

Indeed, three values are `aχ1`, one is zero, so the three other fibre values obey this identity. The common signs in (3), including all later Fourier profiles, are therefore fixed by the actual `u`.

A normalization may use a common affine `c` change and common character/global sign, and may permute the four entries within a block in a way already included in the allowed normalization. These operations do **not** generally leave DC at zero. For example, if after summing over `w`, `x_N(c)=ε(-1)^{t·c}x_O(Mc+b)`, with `M` invertible, then

`hat x_N(t)=ε Σ_c x_O(Mc+b)=ε hat x_O(0)=0`.  (4)

Thus `t` is the **specific dual image of the original DC character**, not an arbitrary zero selected after seeing `x_N`; other allowed operations must carry their actual dual action as well. From here on, `f,a,g,x,y,t` always refer to one such common normalization of this one original object. A coordinate/gauge correspondence outside the displayed source imports is not asserted.

## 3. All-graph dichotomy on that same object

Assume for contradiction that this original object's `S=supp(a)` has affine span five. By S8 and the general all-caller normalization in S6, choose common coordinates `c=(h,d)`, `h,d∈F_2^3`, with `ell=d0+d1+d2`, `b=(d1,d2)∈F_2²`, and `h=(h0,j)` with `j∈F_2²`. The two full blocks are `d=0,h=0,1`; the other six `d=0` blocks are E-row D blocks. On the four `ell=1` B-cosets `d_b=(1,2,4,7)`, in their fixed labeling, every pair differing in the primal full-block direction `e` contains exactly one S point. There is a single function `f:F_2^4→F_2` such that

`S={(ell=1,h0=f(j,b),j,b):j,b∈F_2²}`.

With `q_b=1+b0 b1`, `ρ_b=(-1)^{q_b}`, and the *same* phase `r` defined by `a|_S=(-1)^r`, S6 gives the simultaneous necessary equivalences

`f+q_b is bent`, and `r` and `r+f` are both bent.  (5)

These are not three independently chosen spectra. The same general `g` is `4` at the two F blocks, `-2` at the other six E blocks, `ρ_b` on each graph point, `-2ρ_b` at its physical h-mate, and `0` on the other 24 blocks.

Every four-variable bent function is quadratic, with nonsingular alternating polar. Hence `f` is quadratic. Since the polar of `q_b` has rank two, `B_f=0` would make the polar of `f+q_b` singular. An alternating form on four variables has even rank, so the *graph-polar* rank of this very `f` is exactly **2 or 4**. S6 reports 896 labeled canonical graphs: 512 of graph-polar rank 2 and 384 of rank 4, each with 384 compatible common phases. These are labeled necessary-interface counts, not counts of original Boolean functions, equivalence classes or witnesses. Their numerical enumeration is not needed for the dichotomy.

## 4. Rank four is impossible: the actual U0 zero flat

This section reconstructs the S5 argument, including the balance and amplitude hypotheses. All Walsh transforms on `F_2^6` are unnormalized. From (2), `x` is odd exactly on S, `Σx²=56`, and the actual spectral bound and divisibility give `hat x∈{0,±8}` with exactly 56 nonzeros. Put `z=hat x/8∈{0,±1}`. Then `hat z=8x`, so the parity `z mod 2` has Boolean degree at most three. Indeed, each ANF coefficient of degree `d≥4` is an alternating finite difference of `z`; Fourier inversion makes it divisible by `2^(d-3)`, hence even. The zero indicator `1_Z=1+z mod 2` has weight eight and degree at most three.

The minimum-weight Boolean-degree lemma gives `Z=t+K0`, an affine three-flat: a nonzero degree-at-most-d Boolean function in n variables has weight at least `2^(n-d)`, and equality has affine `(n-d)`-flat support. For completeness, induct on `(n,d)` using `p=p0+x_n p1`: if `p1≠0`, `wt(p0)+wt(p0+p1)≥wt(p1)`; equality and the induction hypothesis force either one summand to vanish or the two minimum-support summands to be complementary affine hyperplanes inside the minimum affine support of `p1`. The case `p1=0` is immediate. Include `d=0` and `d=n` as boundary cases. The specific `t` belongs to Z by (4). Set `L=K0^⊥` in the primal space.

Let `B_-={ξ:z(ξ)=-1}`. Exact inversion gives

`x(c)=8δ_0(c)-(-1)^{t·c}1_L(c)-(1/4) hat(1_{B_-})(c)`.  (6)

The quotient is integral because all other terms are integers. Its Boolean parity has degree at most two: in the expansion of `hat(1_{B_-})(c)/4`, each ANF finite difference of degree `j≥3` has the factor `(-2)^j/4`, hence is even; degrees zero and one are integral because the whole function is integral. Reducing (6) modulo two gives

`1_S+1_L` has Boolean degree at most two.  (7)

In the Boolean algebra's associated graded exterior algebra, the cubic term of `1_S=ell(1+h0+f(j,b))` is `ell∧B_f`. A linear three-space L has indicator's cubic term equal to the wedge of its three independent normal forms. By (7), `ell∧B_f` must be a nonzero decomposable three-form. Wedging it with `ell` shows that `ell` belongs to its normal span; quotienting by `ell` makes `B_f` decomposable. Because `B_f` involves only the four independent `(j,b)` coordinates, its rank has not changed in the quotient. A nonzero decomposable alternating two-form has rank two. Thus graph-polar rank four is impossible. Neither y nor v can repair this contradiction.

For graph-polar rank two write `B_f=p∧q` with independent linear forms on `(j,b)`. Equality of the cubic normal spans also fixes

`L=ker ell ∩ ker p ∩ ker q`, `Z=t+L^⊥`.  (8)

Here `e∈L`. This `L` is neither the original two-dimensional quotient P nor the selected original T.

## 5. Rank-two original-caller bridge to S4

Assume now that the very same `f` has graph-polar rank two. Let `H_f=rad(B_f)` in the four `(j,b)` variables. It has dimension two. If `(j,0)∈H_f`, then it also lies in the radical of the polar of `q_b`, hence in the radical of `f+q_b`; the latter is nonsingular by (5). Thus `H_f∩{(j,0)}=0`, and projection of `H_f` to physical b is bijective. Write its elements as `k(b)` and use common linear coordinates

`(j,b)=(i,0)+k(b)`, `h'=h0+d_f(b)`, `d_f(b)=f(k(b))+f(0)`.

Here `k(0)=0`, `d_f(0)=0`, `d_f` is linear because `H_f` is radical, and `f=F(i)+d_f(b)` with `F(i)=f(i,0)`. Consequently the graph is `h'=F(i)`, physical b and the h-mate direction are preserved, and `F` has nondegenerate two-variable polar, hence odd truth-table parity. In these coordinates (8) reads `L={ell=0,i=0}`, with free `(h',b)`.

### Actual common phase

For each `i`, let `r_i(b)` be the restriction of the common graph phase from (5). For fixed `α∈F_2²` set `v_i(α)=Σ_b(-1)^{r_i(b)+α·b}`. Bentness of r gives `Σ_i v_i(α)^2=16`; since each v is even, either one is `±4` and three are zero, or all four are `±2`. In the latter case the four signs must have odd product for all four i-Walsh values to have magnitude four. Multiplication by `(-1)^{F(i)}` reverses that product because F has odd parity, and then the four i-Walsh values are one `±8` and three zero, contradicting bentness of `r+f`. Hence the first alternative holds for every α. Row Parseval now says each `r_i` is an affine character of b, with slope `λ_i`, and the four slopes are distinct. Every permutation of `F_2²` is affine, so the `i↦λ_i` map is an affine bijection and `Σ_i λ_i=0`. This proves the four distinct phase-row covectors on the actual graph; it does not select four unrelated phase rows.

### Actual balance and all seven common-X profiles

The whole `hat x` condition, not merely the zero set, gives from (8)

`A_x(v)=Σ_c x(c)x(c+v)=64δ_0(v)-8(-1)^{t·v}1_L(v)`.  (9)

Indeed its Fourier transform is exactly `64(1-1_{t+L^⊥})`. Define the **auxiliary** arrays `X(c)=(-1)^{t·c}x(c)` and `Y(c)=(-1)^{t·c}y(c)` using this fixed t. This is simultaneous spectral translation, not a new physical ternary inverse with a newly modulated a or g. Equation (3) remains `Y=-agX` on S; all `Y` caps and the common residue are merely permuted. Also `hat X(0)=0` and

`A_X(v)=64δ_0(v)-8 1_L(v)`.

For the eight actual L-cosets indexed by `(ell,i)`, and for every character `η=(s,α)∈L*`, write

`X_{ell,i}^(η)=Σ_{h',b} X(ell,i,h',b)(-1)^{s h'+α·b}`.

Fourier transformation of the *same* autocorrelation in L gives

`Σ_{ell,i} [X_{ell,i}^(η)]² = 0` for `η=0`, and `=64` for **each of the seven** `η≠0`.  (10)

Thus all eight physical coset sums vanish and all seven nonzero profiles hold simultaneously for this one X. There is no frequency-by-frequency choice of profile signs. This proves the profile bridge from the actual amplitude cap, energy and the specific carried zero, rather than assuming seven independently realizable spectra.

### Physical locations, H, residue and phase retained

There are 16 physical graph-mate D blocks plus six E-row D blocks. Consequently, if `d_E` is the number of D0 blocks on E and `k_i` their counts on the four graph rows, then

`d_E∈{0,1,2,3,4}`, `Σ_i k_i=4-d_E`.  (11)

All E-row and graph-mate placements, local signs, the six Z2 and the unique actual Z4 are retained; (11) is not restricted to `d_E=0` or one graph D0 per row.

Let `J` be the parity of the number of nonzero `u(c,0)` in the **actual** Q coordinate. The Fourier transform of `U0+U1+U2+U3=4u(c,0)` gives

`hat x+hat(3a)+hat g+hat y ≡ 4J (mod 8)` at every frequency.

Here `hat x≡0`, `hat(3a)≡hat g≡4`, while the named original third fibre gives `hat y≡4`; hence `J=1` and all 64 actual `hat y` are congruent to four modulo eight. After the fixed t modulation the same is true for `hat Y`. The required cap `|hat y|≤12` is the actual original cap on all 64 positions, not a consequence of the residue.

The general-g residue used in S4 follows directly, without a fixture: at `ell=0,b=0`, `k(0)=d_f(0)=0`, and

`Σ_{h',i} (-1)^{s h'+β·i} g(0,h',i,0) = 1_{s=0}(12-16·1_{β=0})`.  (12)

At `ell=0,b≠0`, `g=0`. This holds for every admitted f and r.

To spell out the phase interface in the even-`d_E` part of S4, let `s_i(b)` be the negative-sign indicator of X on graph row i, `P_i=⊕_{b:s_i(b)=1} b`, and let `B_D` be the b-XOR of the actual D0 blocks (E-row blocks have b=0). The zero profile in (10) gives `|P_i|≡k_i (mod 2)`. Write the ANF of `s_i` as `c_i+u_i·b+(k_i mod 2)b0b1`, and let `Q(v0,v1)=(v1,v0)`. Then

`P_i=Q u_i+(k_i mod 2)(1,1)`.  (13)

By `Y=-agX`, the Y graph row is bent when `k_i` is even and affine when `k_i` is odd; in either case its linear covector, denoted respectively `θ_i` or `κ_i`, is `λ_i+u_i`. The **S4 row-parity lemma**, whose full proof is a named import and which uses all the valid profiles including the singleton cases, supplies `Σ_i P_i=B_D`. As `Σ_i λ_i=0` and `Σ_i k_i=4-d_E` is even,

`Σ_{k_i even} θ_i + Σ_{k_i odd} κ_i = Q B_D`.  (14)

This derives the stated phase relation from the actual signs and the imported lemma; it is not an assertion about arbitrary independent rows. For odd `d_E`, S4 uses its separately imported actual-X support-parity obstruction instead of (14).

### Exact no-go import and its application

S4 states the following whole conditional theorem: **no single** normalized graph-polar-rank-two object can simultaneously have the retained common `f,r,a,g,u,x,y`, physical inverse/count/phase data, `H_loc=0`, all 64 U0 divisibilities and caps, the specific original-DC transport t, the seven same-X profiles, `J=1`, the general-g residue, and all 64 common U3 caps `≤12`. Its union covers `d_E=0,1,2,3,4`: an actual-X support-parity theorem excludes `1,3`; a whole-graph theorem covers all five D0 partitions for `0`; the uniform even-E/two-E argument covers **both** graph allocations `2` and `1+1`, all permitted E placements and signs for `2`; and the common-Y theorem covers both lambda alternatives for `4`. Its no-go is not the narrower one-D0-per-graph-row theorem S10. The full d0, d4, odd-E and uniform-d2 proof bodies, including the detailed location and row-parity lemmas, are not included as separate literal sources here; they remain **load-bearing conditional imports**, with the exact source pins in §8.

Sections 1–5 put every premise of this stated S4 theorem on the **same original object**: original q-rank and named atom scope; actual ternary inverse and census; the same normalized f/r and general g; the original fixed t; all-cap autocorrelation and seven profiles; actual J and y residue; and the actual all-frequency y cap. No V is needed for this necessary contradiction. Assuming S4 at its stated full physical/location/phase scope therefore rules out the rank-two branch as well. This is a conditional composition of the displayed source theorem, not a claim that the omitted S4 proof bodies were independently reread or re-proved here.

## 6. Exact conclusion and negative boundaries

Every original object quantified in §1 which additionally has five-span S produces one and only one graph-polar rank in `{2,4}`. Section 4 excludes rank 4; §5 and the explicitly conditional S4 theorem exclude rank 2. Hence **there is no five-span object in that named, explicitly locally defined original caller, conditional on the specified source theorems and their source/gauge/atom imports**.

This statement does not say every arbitrary object called `rank2`, `m116`, `H=0` or `NL242` enters §1. It does not assert the missing historical H-table identity, the printed-source correspondence, all collateral original-atom identifications, or a new unrestricted global-caller identity. It neither assumes nor exhibits the complementary v. For any attempted positive full caller, v must still be supported on the actual 140-point complement, satisfy its odd-negative-sign parity and **all 256** odd Walsh caps `≤14`, as well as the selected-T reconstruction and every original constraint. A local two-fibre construction or a formal placement is not such a caller. The particular eight-halfblock recipe is not used in this proof; S1/S2 only warn that it cannot be substituted for the actual census.

## 7. Exact necessary residual, if the original caller exists

Apply the S8 dichotomy to that **same** original object and exclude its five-span alternative as above. With E and the four B cosets defined by S8 from its actual `g`, the only remaining alternatives, up to permutation of the four B-cosets, are:

1. `(|S∩E|; |S∩B_1|,...,|S∩B_4|)=(4;0,4,4,4)` and full-`g` block counts `(0;2,0,0,0)`;
2. `(4;2,2,4,4)` and full-`g` block counts `(0;1,1,0,0)`.

In either alternative `affdim(S)=6`, `S∩E` is an affine two-flat, and the full translation-structure group of the actual `σ1` is `{0}`, as stated by S8. These are only **necessary** alternatives, not proved realizable and not excluded here. They retain the original physical common-u, all four fibres, selected T, carried balance, rank/eight-zero, explicit local H and all remaining original/odd-half conditions. Other m116 residual classes, m114 cases, other nonzero-fibre patterns and the global balanced NL242 problem are outside this result. No human, independent-model-family, kernel/formal, novelty, worldwide-priority or publication acceptance is claimed.

## 8. Inputs, conditional imports and process declaration

I read `manifest-v1.json`, `freeze-receipt-v1.json`, `final-pre-dispatch-binding-v1.json`, `parent-live-metadata-supply-v1.json`, `actual-dispatch-receipt-v1.json`, and all 23 listed controls as status/permissions before `prebody-ack-v1.md`. One initial mistyped f660 control path returned not found; the correct manifest path was then read before the acknowledgement. The actual receipt also displayed adjacent task descriptions; these were administrative exposure, not mathematical inputs. There was no packet/body reading or task-specific mathematical reasoning before the acknowledgement. Memory summary and the two relevant protocol skills were read as administrative guidance.

After that acknowledgement, I read the sole literal packet in order, **all packet LF 1–511**, using exact `:raw` windows `1–20,21–40,...,481–500,501–511`; each display was under 30,000 bytes and at most 20 LF, including the final source ending. No display was observed clipped, so no clipping recovery was necessary. The packet reproduces complete S1–S10 source bodies. Their parent-supplied whole-source SHA-256 pins and roles are:

- S1 `9471cda09e4b8e15d9390b0ce4a7b9ddd354fdc6e82ba64283a8302ee4d13c08`, 35 LF, local-lift caveat only.
- S2 `80b1cca43683ef43557495942bcad22832ab5c4d5cdbdecaf1851d70734d6700`, 19 LF, local-lift caveat only.
- S3 `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef`, 13 LF, explicit local H and general-g foundation.
- S4 `16f5d261dd85ece2842fd3726fd534901f0741bd72b01e74c3199a0076b2a790`, 30 LF, **conditional whole graph-polar-rank-two no-go**, including the row-parity lemma and all E counts.
- S5 `888a7385ea1548b584400d1d84a31d6e0d0ad493c89097278e9726ca56939ed4`, 53 LF, rank-four/zero-flat scope, reconstructed in §4.
- S6 `443d0a1a94384e237076cb7974b49845e6fa52edf3ca83f161259e79a369de1e`, 38 LF, actual all-graph and common-phase normalization.
- S7 `fc7169410a6540a6d63ea033720a90207fd49e89e4cc048d9eb208639eb65e5c`, 51 LF, common physical counts, parity and complement boundaries.
- S8 `2aa39512cf0ef6d1194cc8257dfe722cf9a58b62f637baf9056e08355b4423f0`, 37 LF, original-object five/six span dichotomy.
- S9 `117149fa1734b863b21a37197217b4d8f111ac455194d445c25d0bc95d420de1`, 162 LF, original inverse, explicit local H and named f244 atom/import boundary.
- S10 `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928`, 31 LF, actual physical/radical/phase bridge and narrower one-per-row theorem; not substituted for the entire S4 union.

The packet pin supplied by the parent is `6c41f7f44721bcbdb31b609fdd72aea6bc14b6c0821f2c1c025e7e758df50875` (86,456 bytes, 511 LF). I did not independently execute a hash command or re-open the source paths; metadata pins are not a correctness certificate. The separate S4 load-bearing sources not read as bodies include its parent uniform candidate `18c308d0416d44d4811e1485f849272f4098da69545a378776a3206752579baf`, f818 `c7404c129991d62dccac6dae98ca2e86f627fa5272170803d84c414f31b09ff5`, f819 `d0dcb02fb6df99c37dbdecf16fbbdc8a62ba00c146041d082670768326dd3692`, and its three cited E-parity / entire-d0 / entire-d4 dispositions `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2`, `b8f74cc8316ce476cac0de23b82b626b99e1f526a54c1042cebbdd66c8a19c2e`, `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5`. S4's own precise scope and these unprovided proof bodies, not their mere citation, are the conditional import.

All genuine held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT; source links did not authorize following other files. No sibling scientific return, network, external model, scientific code, subprocess, test, compilation, solver, or scientific evaluation was used. No code was prepared, so there is no prepared-code hash. The candidate is a single new write; any correction must be additive. Parent disposition and independent review remain separate.
