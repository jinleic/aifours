# f886 author candidate v1 — together six-span branch: zero-flat directions, six-site convolution, atom slices

**Status: AUTHOR CANDIDATE (written, conditional on the named imports). Parent disposition is separate.** Author: `AuthorF886BoolTogether`, prospective GENERAL AUTHOR under owner addendum 2. No code was prepared or executed. Nothing here is a whole-branch exclusion, a realization, an NL242 statement, or family/human/formal acceptance.

## 0. Result summary

Quantified object (exactly as in f846 S2 L3, imported): one original balanced Boolean `F` on `F_2^9` in the named f263/f244 residual (actual nonzero selected XOR `T`, Walsh cap 28, `m=116`, polar rank two/eight zeros, labelled fibre counts `(0,4,8)`, `G3=1` read as 23 spatial `U3` zeros, explicit local `H_loc=0`), restricted to the six-span branch with both full `g` blocks in one odd row ("together"), for BOTH retained frequency matchings, every admitted sign/offset, and the SPECIFIC transported balance frequency `t`.

| f846 item | f886 outcome |
|---|---|
| Claim 1: zeros of `x^` form `t+L^perp`, unique 3-dim `L`; (2)–(5) | Reconstructed independently; correct. New remark R1: (2)–(5) are invariant under replacing `t` by any zero of `x^`, so they encode only `t ∈ Z_x`. |
| §3 direction cases (6), (7), (8), `d>=2` | Reconstructed for every `d∈{0,1,2,3}` and both `w=D`, `w!=D`; correct. New: exact census of the 1395 three-dimensional `L`: 704 directions are excluded by parity, 691 survive parity (table in §4.5). R3: the mod-8 refinement of (3) adds no further exclusion. |
| §4 six-site `w=(xh+ag)/4`, (9)–(14), S1 erratum | Reconstructed with every Fourier factor; correct; S1 erratum is right (`hat B=1024w`, normalized inverse `16w`). (13) is shown equivalent to "w vanishes on the five rows `0,e1,e2,e3,xi`". |
| §5 atom-slice items 1–3 | Items 1–3 reconstructed; correct as stated (“before imposing … rank …”). **New (conditional on the imported affine rank six of `H`):** profiles `(4,2,2)` and `(3,3,1,1)` are EXCLUDED, and each surviving profile carries an explicit spanning condition (Theorem 5). Placement of the relation plane `P` in the survivors (Theorem 6) also uses the f244 weight-four import. |
| §6 (15), complement tally, (16), caller | Reconstructed; correct. |

Findings against f846 (S1+S2): **0 FATAL, 0 MAJOR**. MINOR/notation: (n1) the letter `L` denotes both the order-three `GL(2,2)` element (§1) and the zero-flat subspace (§2–3); below the former is renamed `Lambda`. (n2) the original §4 sentence calling `1024w` the "inverse" transform — already corrected by the S1 erratum; no further action. No f846 displayed claim is refuted.

## 1. Imports (all conditional) and notation

Only the literal packet bodies S1–S7 were used. Every import below is a named conditional input, not re-authenticated here.

- **I1 (S6 §1–2).** Original caller: `k=W/4`, `k(a)≡a·T`, `K=T^perp`, pair functions `u,v` on `V=a0^perp`, unnormalized `Walsh_V(u)=2k`, `Walsh_V(v)(a)=2k(a0+a)`, full caller `sum_a k(a)k(a+b)=2^14 1_{b=0}`, local system `U_s`, `16U_s=3Walsh_R(sigma_s)-2t_s`, `k∈{0,±4}` on `R`, `k∈{±2,±6}` on nonzero fibres. Uses f244's `T!=0` and rank-two scope.
- **I2 (S6 §3, S7).** Local block shapes, energies 56/144/136/128, and with `H_loc=d=0`: `a=4,b=6,c=18,o=17` pair counts, two `|U2|=4` and one `|U3|=4` peak. The 23 count uses f244's `20+3G3` at `G3=1`. **The f244 body is missing from the packet; everything depending on it stays conditional.**
- **I3 (S6 §4–6).** For the eight `U3` atoms: affine rank six (from the odd count 23), the f244 weight-four/even-syndrome relation (`P` plane of sign product `+1` plus four points, six differences independent), equal XOR and sign product with the four `U2` atoms, `|(A2+t)∩A3|<=2` for every `t`, and the all-translation sign-mismatch conditions.
- **I4 (S5).** Nonzero `XOR(A)`, the five/six-span dichotomy and branch table; together branch counts `(4;0,4,4,4)/(0;2,0,0,0)`.
- **I5 (S4).** Five-span exclusion (only six-span survives) and the common-normalization bridge: the original DC is carried to ONE specific `t` with `x^(t)=0`.
- **I6 (S3).** Together-branch shell: E-row plane `j=0`, odd-row planes with normals `{m: m(D)=1}`, forced signs with product `-1`, E pair, and exactly two matchings.
- **I7 (S2 §1).** f846's normal form, which packages I4–I6.

Notation (S2 §1). `c=(y,z)∈Y×Z`, `Y=Z=F_2^3`, `z=(j,t')`. `x=U0`, `a=U1/3`, `g=U2`, `h=U3`, `4u=x+3a chi1+g chi2+h chi3`. Transforms are unnormalized on 64 points: `f^(r)=sum_c f(c)(-1)^{r.c}`, so `f^^=64f` and `(fg)^(r)=(1/64)sum_s f^(s)g^(r+s)`. Spectra: `x^=8zeta`, `zeta∈{0,±1}`; `a^=4sigma`; `g^=4kappa`, `kappa∈{±1,±3}`, `A={|kappa|=1}={0,e1,e2,e3}` with `kappa=+1` there; `h^=4rho`, `rho∈{±1,±3}`, `H={|rho|=1}`, `|H|=8`. `xi=e1+e2+e3∈Y*` (zero `Z*` part). Odd rows `e1,e2,e3,xi`; `y_F` = full-block row; `I={0}∪(odd rows \ {y_F})`; plane on row `y_i` is `P_i={z: m_i(z)=beta_i}`, `m_0=n` (`n(j,t')=j`), `beta_0=0`, `{m_i}={m∈Z*: m(D)=1}`, `D=(1,t0+t1)`, `W_i=ker m_i`. The order-three matching element of `GL(2,2)` is written `Lambda` (f846's §1 `L`).

The counts `|A|=4`, `|H|=8`, eight zeros of `x^` follow from the caps plus Parseval: `sum x^^2=64·56` with `|x^|∈{0,8}` gives 56 nonzero values; `sum h^^2=64·128=16N+144(64-N)` gives `N=8`; `sum g^^2=64·136` gives `N=4`.

## 2. One common physical object: block lemma, census, and `w`

"Common physical mate" is used in both senses the scope allows, and both are enforced. (i) `x=U0` and `h=U3` are partial transforms of the SAME four-point blocks of ONE `u`; Lemma 1 and the census tie them site by site. (ii) `D=(1,t0+t1)` is the actual difference of the two full-block points `(0,t0)`, `(1,t1)` in row `y_F`. It fixes the normals `{m: m(D)=1}` and is common to both matchings and every direction case. The split `w=D` / `w!=D` in §4 is relative to this actual `D`.

**Lemma 1 (support block).** On each of the 16 blocks with `U1=±3`: `x,a,g,h∈{±1}` and `h=-agx` (f846 (1)).

*Proof.* Such a block has exactly three nonzero ternary entries (I2), so one `z*∈P*` has `u(c,z*)=0`. Evaluate the block inverse there: `0=4u(c,z*)=x+3a chi1(z*)+g chi2(z*)+h chi3(z*)`. Since all of `x,g,h` are odd with modulus at most 1 (I2), they are `±1`, and `3a chi1(z*)` equals minus a sum of three signs; this forces `|sum|=3`, so `x=g chi2(z*)=h chi3(z*)=-a chi1(z*)`. With `chi1 chi2 chi3=1` (the three nonzero `s` sum to zero), `-agx=-(-x chi1)(x chi2)x=x chi1 chi2=x chi3=h`. QED.

**Census (I2 with `H_loc=0`).** Off `S` (`U1=0`), each block is all-zero, one `±4`, or two `±2` entries in slots `(0,2)`, `(0,3)` or `(2,3)`. The counts are: `D0=(g,x,h)=(±2,±2,0)`: 4; `D3=(±2,0,±2)`: 18; full `g=(±4,0,0)`: 2; `Z2=(0,±2,±2)`: 6; `Z4=(0,0,±4)`: 1; zero: 17. Total `16+4+18+2+6+1+17=64`. Energies: `x`: `16+4·4+6·4=56`; `h`: `16+18·4+6·4+16=128`; `g`: `16+4·4+18·4+2·16=136`. All match I1/I2.

**Row location.** By I6/I7, `g` is nonzero at every site of row `0` (`3·1_{P_0}-2∈{1,-2}`), of every occupied odd row (`±(3·1_{P_i}-2)`) and of `y_F` (`±(6·1_F-2)`), and `g=0` on the three nonzero even rows. The 40 sites with `g!=0` are exactly `S(16)+D0(4)+D3(18)+full(2)`. Hence the 24 sites of the three nonzero even rows are exactly `Z2∪Z4∪zero`, and `D0`, `D3` lie in rows `0`, odd.

**Lemma 2 (six-site function).** `w=(xh+ag)/4` is `±1` on the six `Z2` sites and `0` elsewhere; `supp w` lies in the three nonzero even rows.

*Proof.* On `S`, `xh+ag=x(-agx)+ag=0` by Lemma 1 (`x^2=1`). On `D0` `h=a=0`; on `D3`, full and `Z4` sites `x=a=0`; zero sites vanish. On `Z2`, `a=0` and `xh=(±2)(±2)=±4`. QED. This uses ONE common `u`; independently assigned `x`, `h` arrays are not covered.

## 3. The zero flat of `x^` and the coset identities

**Lemma 3 (degree).** Let `Z_x={r: x^(r)=0}`, `|Z_x|=8`. Then `deg 1_{Z_x}<=3`.

*Proof.* `zeta^=x^^/8=8x`. For an affine codimension-two flat `F=r0+M` (`|M|=16`), `1_F(s)=(1/4)sum_{c∈M^perp}(-1)^{c.(s+r0)}`, so `sum_{s∈F}zeta(s)=(1/4)sum_{c∈M^perp}(-1)^{c.r0}·8x(c)=2·(integer)`, even. As `zeta≡1_{Z_x^c} (mod 2)` and `|F|=16`, `|F∩Z_x|` is even. Indicators of codimension-two flats span all Boolean functions of degree `<=2` (`x_i x_j` is one; `x_i` and `1` are sums of two and four). If the ANF of `1_{Z_x}` had a maximal monomial `x_U`, `|U|>=4`, then `sum_s 1_{Z_x}(s)x_{U^c}(s)` is the sum over the subcube `{s_{U^c}=1}`, which equals mod 2 the sum of ANF coefficients of monomials containing `U`, i.e. `1` by maximality — contradicting orthogonality to degree `<=2` (`|U^c|<=2`). QED.

**Lemma 4 (minimum weight with equality).** A nonzero Boolean function of degree `<=r` in `n` variables has weight `>=2^{n-r}`, with equality iff its support is an affine flat of codimension `r`. (f846's induction is complete as written: if `f=f0+x_n g` with `g=0`, induct on `f0`; else `wt f=wt f0+wt(f0+g)>=wt g>=2^{n-r}`; at equality `supp g` is a codimension-`(r-1)` flat `G`, `supp f0` and `supp(f0+g)` partition `G`, so `f0=g·h|_G` with `deg h<=1` by the degree bound in coordinates where `G={y_1=...=y_{r-1}=1}`; thus `supp f={y∈G: h(y)+x_n=1}`. Bases `r=0` and `r=n` are immediate.) Applied at `(6,3)`: `Z_x` is an affine three-flat. Since `t∈Z_x` (I5), `Z_x=t+M` for a unique 3-dim `M`; put `L=M^perp`, a unique 3-dim spatial subspace with `Z_x=t+L^perp`.

**Theorem 1 (f846 Claim 1).** With `X(c)=(-1)^{t.c}x(c)`, `Hm(c)=(-1)^{t.c}h(c)`, for every coset `C=c+L` and every character `e∈L*` (extended to any `r_e` with `r_e|_L=e`), `X_e(C)=sum_{l∈L}X(c+l)(-1)^{e(l)}`, `H_e(C)` likewise, and `k_e=#{r∈H+t: r|_L=e}`:

- (2) `X_0(C)=0`, hence `|S∩C|` even;
- (3) `sum_C X_e(C)^2=64` for `e!=0`;
- (4) `sum_C H_e(C)^2=144-16k_e` for every `e`, `sum_e k_e=8`;
- all `X_e(C)`, `H_e(C)` even;
- (5) `sum_c x(c)x(c+v)=64·1_{v=0}-8(-1)^{t.v}1_L(v)` for every `v`.

*Proof.* `X^(r)=x^(r+t)`, so `X^` vanishes on `L^perp`. For fixed `e`, the function `C ↦ (-1)^{r_e.c}X_e(C)=sum_{l}X(c+l)(-1)^{r_e.(c+l)}` on the 8-element quotient `(Y×Z)/L` has quotient-Fourier coefficients `X^(r_e+s)`, `s∈L^perp`. Quotient inversion: at `e=0` all coefficients vanish, giving (2); quotient Parseval: `sum_C X_e(C)^2=(1/8)sum_{s∈L^perp}x^(r_e+s+t)^2`. For `e!=0`, `r_e+s+t∉t+L^perp`, all eight squares are 64: total 64, (3). For `Hm`, `Hm^(r)=h^(r+t)`; on the class `r_e+L^perp` exactly `k_e` points have `h^^2=16` and `8-k_e` have 144: `(16k_e+144(8-k_e))/8=144-16k_e`, (4). Parity: `x` is odd exactly on `S` (`±1`) and even off `S`; the same holds for `h` (I2). So `X_e(C)≡H_e(C)≡X_0(C)=0 (mod 2)`; mod 2 reduction of (2) gives `|S∩C|` even. (5): `sum_c x(c)x(c+v)=(1/64)sum_r x^(r)^2(-1)^{r.v}=sum_r(-1)^{r.v}-sum_{r∈t+L^perp}(-1)^{r.v}`. QED. Changing a coset representative multiplies `X_e(C)`, `H_e(C)` by `(-1)^{e(l0)}`; squares are unchanged. Consistency: (5) at `v=0` gives `56`, the census energy; summing (3) over the seven `e!=0` gives `448=8·56-0`, the quotient Parseval total.

**Remark R1 (what `t` contributes).** If `t'=t+s0` with `s0∈L^perp`, then `(-1)^{s0.c}` is constant on each `L`-coset, so `X'`, `Hm'` differ from `X`, `Hm` by one sign per coset; and `k'_e=k_e` because `s0|_L=0`. Hence (2)–(5) hold verbatim for EVERY zero of `x^` and encode about `t` only that `t∈Z_x`. Which zero is the original DC matters elsewhere (restoring balance, (16), the 58-pair count), never through (2)–(5). This supports f846's warning that a subsequently selected zero is not original balance.

**Remark R2 (bounds on `k_e`).** By I3, `H` has affine rank six and its unique nontrivial affine relation is the four-point plane relation. A class `r_e+L^perp` is an affine three-flat; any `k` points of `H` in it have affine rank `<=3`, while `k` points of `H` have rank `k-1`, or `k-2` if they contain the relation plane. Hence `k_e<=4`, or `k_e=5` only if `r_e+L^perp⊇P+t` (`P` the relation plane). Thus `sum_C H_e(C)^2>=64` in (4). (Conditional on I3.)

## 4. Zero-flat directions: every case of `d=dim(L∩Z)`

Write `L_Z={z: (0,z)∈L}`, so `d=dim L_Z`, and `P=pi_Y(L)`, `dim P=3-d`. Let `Q=(Y×Z)/L` (8 cosets). For `i∈I` let `Pi_i={y_i}×P_i`, so `S=⊔_i Pi_i`.

**Lemma 5 (plane–coset intersection).** For every coset `C`, `Pi_i∩C` is empty or a coset of `{0}×(W_i∩L_Z)`; so `|Pi_i∩C|∈{0,2^{delta_i}}`, `delta_i=dim(W_i∩L_Z)`. If `delta_i=0`, `Pi_i` maps injectively onto a 4-element subset `Im_i⊂Q`. Hence the parity part of (2) is equivalent to `sum_{i:delta_i=0}1_{Im_i}≡0 (mod 2)` on `Q`.

*Proof.* Two points of `Pi_i` differ by `(0,delta)`, `delta∈W_i`; they are congruent mod `L` iff `delta∈L_Z`. QED.

**Theorem 2 (directions).** For the actual shell (I6/I7), every admitted sign/offset, both matchings, and any zero of `x^` in place of `t`:

- **`d=0`.** `L={(y,Jy)}` for a unique linear `J:Y->Z`, and parity holds iff
  `sum_{i∈I}[beta_i+m_i(Jy_i)]=0`, i.e. `sum_{i!=0}[beta_i+m_i(Jy_i)]=0` (f846 (6)).
- **`d=1`, `L_Z=<w>`, `w=D`.** All four planes contribute; parity holds iff `y_F∈P` (f846 (7)).
- **`d=1`, `w!=D`.** Exactly two indices `i!=j` have `m_i(w)=1`; parity holds iff `y_i+y_j∈P` (f846 (8)); if one of them is `i=0`, this reads `y_j∈P`.
- **`d=2,3`.** Parity holds automatically; `d=3` means `L=Z` (cosets are the rows).

*Proof.* `d=0`: `pi_Y|_L` is injective, hence bijective, so `L` is the graph of `J`. The linear map `(y,z) ↦ z+Jy` is onto `Z` with kernel `L`, identifying `Q` with `Z`; `Im_i={z': m_i(z')=gamma_i}`, `gamma_i=beta_i+m_i(Jy_i)`, and `1_{m=gamma}=1+gamma+m(·)` mod 2. Summing the four: `4+sum gamma_i+(sum m_i)(·)`. The four normals are the coset `m_0+D^perp`, an affine plane, so `sum m_i=0`; parity holds everywhere iff `sum gamma_i=0`. For `i=0`, `y_0=0`, `beta_0=0`, so that term is zero.
`d=1`: `delta_i=0` iff `w∉W_i` iff `m_i(w)=1`. The map `Q->Y/P` (2 classes) is well defined because `pi_Y(L)=P`, with 4-element fibres; `Im_i` lies in the fibre over `y_i+P` and has 4 elements, so it equals that fibre. With `phi` the nonzero functional on `Y` vanishing on `P`, `1_{fibre(y_i+P)}=1+phi(y_i)+phi(·)`. If `w=D`, all four `m_i(D)=1`, so the sum is `phi(sum_{i∈I}y_i)`; since the four odd rows sum to zero, `sum_{i∈I}y_i=0+(three non-full odd rows)=y_F`; parity iff `phi(y_F)=0` iff `y_F∈P`. If `w!=D`: on `m_0+D^perp`, `m(w)=m_0(w)+c(w)` and `c ↦ c(w)` is a nonzero functional on `D^perp` because `w∉<D>=(D^perp)^perp`; so exactly two `m_i(w)=1`, and parity iff the two fibres coincide, iff `y_i+y_j∈P` (the rows are distinct, so `y_i+y_j!=0`).
`d>=2`: `dim(W_i∩L_Z)>=2+d-3>=1` for every `i`. QED.

**Independence of the remaining data.** (6)–(8) involve only `y_i`, `m_i`, `beta_i`, the actual full-block difference `D`, and `y_F`. They do not involve the matching `Lambda` or its offset `b`, the `a`-peak signs, the `epsilon_y`, or which zero of `x^` is `t` (Remark R1). Hence they hold for BOTH matchings and every sign/offset; the full signed (2)–(5) remain additional conditions in every case.

**Structure when (7) holds (`d=1`, `w=D`).** `P` is a 2-dim subspace containing the odd row `y_F`, so it is not inside the even-weight subspace and contains exactly two odd rows, `y_F` and one `y_k∈I`. Then `I∩P={0,y_k}` and every one of the 8 cosets meets `S` in exactly two points (rows `0`,`y_k` over the class `P`; the other two non-full odd rows over the other class). With (2), `sum_{S∩C}X∈{0,±2}` must be cancelled by `±2` values on `(D0∪Z2)∩C`; in particular every coset whose two `S` points have equal `X` sign contains a `D0` or `Z2` site, and the number of such cosets is even (`|D0∪Z2|=10`).

**Remark R3 (a refinement that adds nothing; useful negative).** For `e!=0`, `X_0(C)=0` gives `X_e(C)/2=-sum_{l∉ker e}X(c+l)≡|S∩(c+(L\ker e))| (mod 2)`. Odd squares are `≡1 (mod 8)` and even squares are `≡0 (mod 4)`. So (3) (`sum_C(X_e(C)/2)^2=16`) forces `#{C: X_e(C)/2 odd}≡0 (mod 4)`. Equivalently, with `K'=ker e`, the number of `K'`-cosets with odd `|S∩·|` is `≡0 (mod 8)`. This holds for EVERY 2-dim `K'⊂F_2^6` by the plane structure alone, so it excludes no direction. *Proof.* Let `K'_Z={z: (0,z)∈K'}`. The parity of `|S∩·|` on `F_2^6/K'` is `sum_{i: W_i∩K'_Z=0}1_{Im'_i}`. There are three cases.

- `dim K'_Z=2`: no plane contributes, since `W_i∩K'_Z!=0`.
- `K'_Z=<u'>`: then `pi_Y(K')=<p'>`. Each contributing `Im'_i` is the whole 4-element fibre over `y_i+<p'>` in `Y/<p'>`. There are four contributions if `u'=D` and two otherwise. Either way the number of classes hit an odd number of times is even, so the weight is `4·(even)`.
- `K'_Z=0`: `K'` is a graph over a 2-plane `P'⊂Y`. With `Phi(y,z)=(y+P',z+J~y)`, where `J~` extends the graph map, the quotient becomes `(Y/P')×Z` and `Im'_i={y_i+P'}×{m_i=gamma_i}`. On each class the parity is affine, with linear part `sum_{i in class}m_i`. Since `sum_{i∈I}m_i=0`, the two classes have equal linear parts. If that common part is zero, each class has weight 0 or 8; otherwise each has weight 4. Either way the total is `≡0 (mod 8)`.

QED.

**f846's example re-verified.** For a 2-plane `P∌y_F` (4 of the 7 planes of `Y`), `L=P×<D>` has `L_Z=<D>`, `pi_Y(L)=P`, and violates (7). It is a formal direction exclusion, not a constructed caller.

**4.5 Exact census of directions (formal; not attainability).** `Y×Z=F_2^6` has `[6 choose 3]_2=63·31·15/(7·3·1)=1395` three-dimensional subspaces: `d=0`: `2^9=512` graphs; `d=1`: for each of 7 `w`, each of 7 planes `P`, the graphs of the 16 linear maps `P->Z/<w>`: `7·7·16=784`; `d=2`: 7 choices of `L_Z`, 14 lines of `F_2^4` off `Z/L_Z`: 98; `d=3`: 1. Sum `1395`.

| case | count | parity-admissible | excluded |
|---|---|---|---|
| `d=0` | 512 | 256 | 256 |
| `d=1`, `w=D` | 112 | 48 (`P∋y_F`: 3 of 7 planes) | 64 |
| `d=1`, `w!=D` (6 values) | 672 | 288 (`P∋y_i+y_j`: 3 of 7) | 384 |
| `d=2` | 98 | 98 | 0 |
| `d=3` | 1 | 1 | 0 |
| total | 1395 | 691 | 704 |

For `d=0`, (6) is an affine condition on `J∈Hom(Y,Z)` whose linear part `J ↦ sum_{i!=0}m_i(Jy_i)` is nonzero: the three non-full odd rows are linearly independent (the only relation among the four odd rows is their total sum), so `J` can send one of them to a `z` with `m_i(z)=1` and the others to `0`. Hence exactly half. These counts use the shell only; they exclude whole direction subfamilies for every completion, but say nothing about which admissible `L` is attained.

## 5. The six-site convolution identity

**Theorem 3.** For every `r∈F_2^6`, with `B(r)=sum_s[sigma(s)kappa(r+s)+2zeta(s)rho(r+s)]` (sums in `F_2^6`, `sigma` from the actual matching):

- (11) `B=16w^`, so `B(r)∈{0,±32,±64,±96}`;
- (12) `sum_r B(r)^2=98304`;
- (13) `B(r+xi)=B(r)` for all `r`, and `sum_{alpha∈Y*}B(alpha,eta)=0` for all `eta∈Z*`; jointly (13) is EQUIVALENT to `w=0` on the five rows `0,e1,e2,e3,xi`;
- (14) `B(r)/32≡3+N_-(w)+X_w.r (mod 2)`, `X_w=XOR(supp w)`, with `xi.X_w=0`;
- (S1 erratum) unnormalized `B^=1024w`; normalized inverse `(1/64)B^=16w`.

*Proof.* Product rule: `(xh)^(r)=(1/64)sum_s 8zeta(s)·4rho(r+s)=(1/2)sum_s zeta(s)rho(r+s)` and `(ag)^(r)=(1/64)sum_s 4sigma(s)·4kappa(r+s)=(1/4)sum_s sigma(s)kappa(r+s)`; so `(xh+ag)^=B/4`. By Lemma 2, `xh+ag=4w`, hence `4w^=B/4`, `B=16w^`. `w^(r)` is a sum of six signs, an even integer in `[-6,6]`: (11). Parseval: `sum_r w^(r)^2=64·6=384`, so `sum B^2=256·384=98304`: (12). For (13): `w^(r+xi)=sum_c w(c)(-1)^{r.c}(-1)^{xi.y}`, equal to `w^(r)` for all `r` iff `w` vanishes where `xi.y=1` (Fourier uniqueness), i.e. on the four odd rows; `sum_alpha B(alpha,eta)=16·8·sum_z w(0,z)(-1)^{eta.z}`, zero for all `eta` iff `w(0,·)=0`. Lemma 2 gives both. For (14), with `w=(-1)^{eps_c}` on its support, `w^(r)=sum_c(1-2[eps_c⊕r.c])=6-2#{c: eps_c⊕r.c=1}`, so `w^(r)/2≡3+sum_c(eps_c+r.c)=3+N_-+r.X_w (mod 2)`; `xi.X_w=sum_c xi.y_c=0` since each support row is even. Finally `B^(c)=16sum_r w^(r)(-1)^{r.c}=16·64·w(c)`. QED.

**Remarks.** (i) All of (11)–(14) follow from the single identity `B=16w^` plus Lemma 2; conversely the full content of §4 of f846 is: the 64-vector `B` computed from ONE object's `sigma,kappa,zeta,rho` has `B^=1024w` with `w=±1` on exactly six sites of the three nonzero even rows and `0` elsewhere. (ii) On those six (`Z2`) sites `w=sgn(x)sgn(h)` because `x,h=±2` there. (iii) Parity pattern: `B/32` is odd exactly on the affine hyperplane `{r: r.X_w≡N_-}` if `X_w!=0`; if `X_w=0` it is odd everywhere when `N_-` is even and nowhere when `N_-` is odd. Also `sum_r(B/32)^2=96`. (iv) `B(0)=16(6-2N_-)` and `sum_r B(r)=1024w(0)=0`. (v) `B` depends on the matching through `sigma`; the identity is required for the actual matching of the object. It is not implied by the separate `x`/`h` caps or the `a`/`g` shell.

## 6. Original eight-atom set `H`: slice occupancy

**Transport of the I3 facts.** The common normalization acts on all four fibres' frequency spaces by the same affine bijection (plus independent global signs of individual fibres). Translating an even-size set by `lambda` adds `|set|·lambda=0` to its XOR; a linear map carries XORs linearly. Hence `XOR(A2)=XOR(A3)` becomes `XOR H=XOR A=0+e1+e2+e3=xi`. A spatial modulation multiplies the sign products over `A` and over `H` by `(-1)^{XOR(A).tau}` and `(-1)^{XOR(H).tau}`, equal factors; a global sign of `g` or of `h` alone changes the product over 4 or 8 atoms by `+1`. So `prod_H sgn rho=prod_A sgn kappa=+1`. Affine rank six, the unique four-point relation `P` with sign product `+1`, and `|(A+lambda)∩H|<=2` for every `lambda∈F_2^6` are carried verbatim (images of all translates are all translates). All conditional on I3 (and its f244 part).

For `eta∈Z*` let `H_eta={alpha∈Y*: (alpha,eta)∈H}`, `n_eta=|H_eta|`, and `pi: F_2^6->Z*` the projection. The translates `alpha0+A` (as subsets of `Y*`) are exactly the closed neighbourhoods `N[alpha0]` in the cube graph on `F_2^3`; since `(alpha0,eta)+A⊂Y*×{eta}`, the bound reads: every closed neighbourhood contains at most two points of each `H_eta`.

**Theorem 4 (f846 §5 items 1–3, reconstructed).**
1. `n_eta<=4`; a 3-slice lies in an affine plane with normal in `{110,101,011}`; a 4-slice is such an entire plane, with XOR zero.
2. The number of odd `n_eta` is `0`, `4` or `8`; for `4` the odd labels form an affine plane; for `8`, `H` is a graph `alpha=phi(eta)` with `XOR_eta phi(eta)=xi`, i.e. every coordinate of `phi` has cubic ANF coefficient `1`.
3. The occupancy multisets allowed by 1–2 and `XOR H=xi` are exactly `(2,2,2,2)`, `(4,2,2)`, `(4,1,1,1,1)`, `(2,2,1,1,1,1)`, `(3,2,1,1,1)`, `(3,3,1,1)`, `1^8`; in `(4,2,2)` the two 2-slices have XORs summing to `xi`.

*Proof.* A face with normal `100` (similarly `010`, `001`) is a 4-cycle of the cube; any three of its points contain a vertex adjacent to the other two, so lie in one closed neighbourhood. A plane with normal `111` is the even or odd weight class; each of its four 3-subsets is the neighbour set of the unique opposite-parity vertex adjacent to all three. So each of these four normals splits `F_2^3` into two planes, each holding `<=2` points of `H_eta`: `n_eta<=4`. Three distinct points span a unique affine plane, whose normal must then be `110`, `101` or `011`. For `n_eta=4`, each forbidden normal splits the four points 2+2, so all three coordinates of their XOR vanish; four distinct points with zero XOR form an affine plane, again with normal in `{110,101,011}`.
The `Z*` part of `XOR H=xi` is `XOR{eta: n_eta odd}=0`. The number of odd `n_eta` is even since `sum n_eta=8`. Two distinct labels never XOR to zero; six cannot either, because the XOR of all eight labels of `F_2^3` is zero, so six labels XOR to the XOR of the two missing ones. Four distinct labels XOR to zero iff they form an affine plane. Eight odd values summing to 8 are all `1`; the XOR of all values of a Boolean function is its top ANF coefficient.
Partitions of 8 into parts `<=4` number 15: `44, 431, 422, 4211, 41111, 332, 3311, 3221, 32111, 311111, 2222, 22211, 221111, 2111111, 1^8`. Keeping odd-part counts `0,4,8` leaves `44, 422, 41111, 3311, 32111, 2222, 221111, 1^8`. `44` dies: both 4-slices have zero `Y*`-XOR, but the `Y*` part of `XOR H` is `xi!=0`. In `422` the 4-slice contributes zero, so the two 2-slice XORs sum to `xi`. QED. No error found in f846 items 1–3.

**Theorem 5 (NEW: spanning; conditional on the imported affine rank six and `XOR H=xi`).** The occupied labels `O={eta: n_eta>0}=pi(H)` affinely span `Z*`. Consequently:

- `(4,2,2)` is EXCLUDED (three labels always lie in an affine plane);
- `(3,3,1,1)` is EXCLUDED (its four labels are all odd, hence an affine plane by Theorem 4.2);
- `(2,2,2,2)`: the four labels are affinely independent;
- `(4,1,1,1,1)`: the label of the 4-slice lies off the affine plane of the four singleton labels;
- `(3,2,1,1,1)`: the label of the 2-slice lies off the affine plane of the four odd labels;
- `(2,2,1,1,1,1)`: at least one 2-slice label lies off the affine plane of the four singleton labels;
- `1^8`: no new condition.

*Proof.* Affine rank six means the affine span of `H` is `F_2^6`; `pi` is linear and onto, so `aff(pi(H))=pi(aff H)=Z*`. A set contained in an affine plane of `Z*` does not span it. QED.

Exactly five profiles survive: `(2,2,2,2)`, `(4,1,1,1,1)`, `(2,2,1,1,1,1)`, `(3,2,1,1,1)`, `1^8`, each with the stated spanning condition. This strengthens f846's list, which was explicitly "before imposing the remaining sign, rank, convolution and balance restrictions"; it is not an error in f846.

**Theorem 6 (NEW: placement of the relation plane; conditional on I3 including the f244 weight-four relation).** Write `H={a+v: v∈{0,p,q,p+q,b1,b2,b3,b4}}` with `p,q,b1,...,b4` independent (I3). Then:

- (a) `b1+b2+b3+b4=xi`, so `pi(b1)+...+pi(b4)=0`.
- (b) The only four points of `H` with zero sum are `P`; since 8 points of affine rank 6 have a one-dimensional space of affine relations, this relation is unique. Hence every 4-slice equals `P`: in `(4,1,1,1,1)` the 4-slice is `P` (normal in `{110,101,011}`, `rho`-sign product `+1`) and the four `a+b_i` are the singletons, with `pi(b_i)` four distinct nonzero vectors forming an affine plane off `0` (relative to `a`).
- (c) `pi(P)` is the image of a 2-dim space under a linear map, so `P` meets the slices as `4`, `2+2` or `1+1+1+1`. In `(2,2,2,2)` it is exactly `2+2`: the four nonzero within-slice differences lie in `ker pi` (dimension 3), so the union of some two, three or four 2-slices has zero sum; three would be a six-point affine relation, contradicting the uniqueness in (b); four would give `XOR H=0!=xi`; so two 2-slices form a weight-four relation, which is `P`. In `(3,2,1,1,1)`, `P` is either two points in each of the 3-slice and the 2-slice, or four singletons of `pi(P)`; in `(2,2,1,1,1,1)` it is either the union of the two 2-slices or spread over four slices; in `1^8` it is spread over an affine plane of labels, and the four `b`-points over the parallel plane.

*Proof.* (a) `XOR H=4a+(0+p+q+(p+q))+sum b_i=sum b_i`. (b) A zero-sum 4-subset of `{0,p,q,p+q,b_i}` must cancel every `b_i` coordinate in the basis, so it avoids all `b_i`. A 4-slice is an affine plane (Theorem 4.1), so its four points have zero sum. (c) As displayed; for `1^8`, `pi(P)` has four labels forming an affine plane, and the four `b`-labels are its complement, the parallel plane. QED.

**Link to the zero flat (Theorem 1 with `d=3`).** If `L=Z`, then `r|_L` is the `Z*` part of `r`, so `k_e=n_{e+eta_t}` (`eta_t` the `Z*` part of `t`). Then (4) reads `sum_y H_e(y)^2=144-16n_{e+eta_t}` with `n_eta<=4`. So the `d=3` coset energies are tied to the surviving slice profiles of Theorem 5. For `d<3`, only Remark R2's bound `k_e<=5` is claimed.

## 7. Original caps, residue, complement and source imports

**ALL-64 caps (I1).** From `sum_c U_s(c)(-1)^{r.c}=2k(r,s)`: `x^=2k(r,0)∈{0,±8}` (`k∈{0,±4}` on `R`); `a^=2k(r,1)/3=±4` (fibre 1 has no small atoms, so `|k(r,1)|=6` everywhere); `g^=2k(r,2)`, `h^=2k(r,3)∈{±4,±12}`. Common affine changes of `c` and common modulations permute and re-sign these values, so the magnitude statements are normalization-invariant. They are separate from, and not implied by, (11)–(15).

**(15) `J=1` residue.** For every `r` and internal point `b∈P*`, `[x^+3chi1(b)a^+chi2(b)g^+chi3(b)h^](r)/4` is the 64-point transform at `r` of the slice `u(·,b)`, hence an integer; its terms are `≡0,4,4,4 (mod 8)` (`3a^=±12`, `g^=4kappa`, `h^=4rho` with `kappa,rho` odd), total `≡4`, so it is odd. Equivalently each of the four slices `u(·,b)` has odd support (a transform is `≡|supp| mod 2`), consistent with `116=` a sum of four odd numbers. (15) does not see which zero of `x^` is the balance frequency.

**Complement half (I1).** On the odd half `Walsh_V(v)(a)=2k(a0+a)` with `k(a0+a)` odd and `|W|<=28`, so `Walsh_V(v)∈{±2,±6,±10,±14}`. With counts `N2,N6,N10,N14` (sum 256) and Parseval `4N2+36N6+100N10+196N14=256·140=35840`, subtracting `100·256` and dividing by 32 gives `3(N14-N2)-2N6=320`; mod 3, `N6≡2`; so `N6>=2` and `N14=N2+(320+2N6)/3>=108`, with equality iff `(N2,N6,N10,N14)=(0,2,146,108)`. A tally, not a signed spectrum or existence statement.

**(16) XOR.** For `y∈V`: `u=-1` puts both `y,y+T` in `{f=1}` (contributing `T`); `u=1` puts neither; `u=0,v=1` puts `y+T`; `u=0,v=-1` puts `y`. Since `sum u=0` and `|supp u|=116` hold in ORIGINAL coordinates, there are 58 negative pairs, and `XOR_{f=1}x=58T+XOR_{u=0}y+#{v=1}T`. Because `V⊕<T>=F_2^9`, `=T` iff `XOR_{u=0}y=0` and `#{v=1}` is odd. This uses the original DC, i.e. the specific transported `t`, not an arbitrary zero (contrast Remark R1). The full caller `sum_a k(a)k(a+b)=2^14 1_{b=0}` for all 512 `b` remains a separate requirement.

**Sign-mismatch transport (I3).** S6 gives `W2≡W3 (mod 8)` and `W_s≡0 (mod 4)`; hence also `W2≡-W3 (mod 8)`, so `sum_r d_lambda(r)≡0 (mod 4)` and `XOR_{d_lambda!=0}r=0` hold whatever independent global signs `g` and `h` carry. Under a common frequency translation the sum is unchanged and the XOR moves by `|supp d_lambda|·tau=0` (`|supp d_lambda|≡sum d_lambda≡0 mod 2`). So the conditions in the `kappa,rho` normalization are a valid transport, conditional on I3.

**Reading aid (inference).** f846's packet labels differ from f886's. By LF counts in f846's declaration (S2 L148) and the cited content, `[INFERENCE]` f846-S1=f886-S4 (27 LF), f846-S2=f886-S3 (46), f846-S3=f886-S5 (37), f846-S4=f886-S6 (162; e.g. "S4 lines 107–113" is the atom shape at f886-S6 L107–113), f846-S5=f886-S7 (13). No unlisted body was opened to confirm this.

## 8. Findings, limits and the unpaid frontier

**Against f846 (S1+S2): 0 FATAL, 0 MAJOR.** Notation-only: (n1) the symbol `L` is used both for the order-three `GL(2,2)` matching element and for the zero-flat subspace; (n2) the original §4 "inverse" wording is already corrected by S1, and the correction is right. No displayed f846 identity, case or exclusion is refuted. f846's slice list is not wrong: it was explicitly pre-rank; Theorems 5–6 add the rank restriction.

**New necessary conditions in this candidate (all conditional on I1–I7):**
- R1: (2)–(5) are invariant under replacing `t` by any zero of `x^`.
- R2: `k_e<=5`, and `k_e=5` only for the class containing `P+t`.
- R3 (negative): the mod-8 refinement of (3) is automatically satisfied by the four support planes for every 2-dim `K'`. So the `S`-parity content of (2)–(3) yields no direction exclusion beyond (6)–(8); further exclusions need the signs, the `h` data (4), or (5).
- §4.5: exact direction census; 704 of the 1395 directions are excluded by parity, 691 survive; `d=1`, `w=D` survivors meet `S` in exactly two points per coset.
- (13) is equivalent to `w` vanishing on the five rows `0,e1,e2,e3,xi`; parity pattern of `B/32`.
- Theorem 5: slice profiles `(4,2,2)` and `(3,3,1,1)` excluded; spanning conditions on the five survivors.
- Theorem 6: the relation plane `P` is the 4-slice in `(4,1,1,1,1)`, the union of two 2-slices in `(2,2,2,2)`, and is split `4`, `2+2` or `1+1+1+1` in general.
- `d=3`: `k_e=n_{e+eta_t}`.

**Limits.** These are necessary conditions on one actual object. Nothing here constructs, or excludes, any completion. In particular this candidate makes no claim about: the whole together branch; the split branch; other `m=116` classes; `m=114`; global NL242; any historical H-class or source identity; novelty or priority. The f244 body is missing from the packet. Every use of `T!=0`, the rank-two scope, `20+3G3`, and the weight-four/even-syndrome relation is therefore a named conditional import (I1–I3). No finite enumeration was executed. The counts in §4.5 and §6 are written counting arguments.

**Unpaid frontier (first open step).** Decide feasibility of one actual system. Fix a shell and either matching, and take a parity-admissible `L` (one of 691 per shell) with `t∈t+L^perp`. Seek ONE physical `(x,h)` with the census (Lemma 1/2), the signed (2)–(5), `B=16w^`, a surviving slice profile with the Theorem 5/6 placements, the intersection and sign-mismatch conditions, the ALL-64 caps and (15). Then require a complement `v` on the 140 zeros with all 256 caps, (16) after restoring original coordinates, and the full 512-shift caller. No solution or contradiction is claimed.

## 9. Read, provenance and method declaration

- **Administrative, before any body.** Read completely and raw: manifest-v1, freeze-receipt-v1, final-pre-dispatch-binding-v1, parent-live-metadata-supply-v1, actual-dispatch-receipt-v1 (present at first look), and all 22 `controls_before_body` (status/permissions only). Created `prebody-ack-v1.md` (exclusive new file; clock `2026-10-31T03:01:53Z`). Then sent a direct prebody ACK to `agent://Main`, which returned "Delivered to Main.". Both preceded any mathematical body read or reasoning.
- **Body.** Read `literal-packet-part-01-v1.md` completely and in order. Raw windows: LF `1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-160, 161-180, 181-200, 201-220, 221-240, 241-260, 261-280, 281-300, 301-320, 321-340, 341-360, 361-380, 381-400, 401-420, 421-440, 441-460, 461-470`. That is 24 windows, each `<=20` LF. An administrative byte count gives a largest window of 7080 bytes (`<30000`). The ending was observed: packet L470 = S7 L13, terminal. No clipping was observed, so no recovery was needed. Coverage: S1 1–7, S2 1–148, S3 1–46, S4 1–27, S5 1–37, S6 1–162, S7 1–13, with all packet headers.
- **Not used.** No linked or unlisted body, held episode or held consumer, sibling output, old code, network, external model, solver, test, compilation, scientific execution, child agent or subprocess for science. Hashes are the parent-supplied values; none was recomputed.
- **Administrative shell use (disclosed).** `ls -la` and `wc -c -l` on the wave directory before the ACK; `date` for clocks; one `awk` byte count of the 20-line packet windows. None is scientific.
- **Method notes.** Written GENERAL AUTHOR reasoning only; no verifier was requested or prepared, so there is no prepared-code hash. Private reasoning used general enumerations (partitions of 8, subspace counts). While orienting Lemma 1, it also briefly used one illustrative concrete ternary block. That example was dropped for the general proof and nothing depends on it; fresh examples are permitted to a GENERAL AUTHOR under addendum 2 and the scope restoration.
- **Process note.** The harness discarded one earlier response attempt of mine for output length; per the harness notice, none of its planned tool calls ran. I have no view of its content, and no file or message came from it.
- This is an author candidate; parent disposition and any independent check are separate.
