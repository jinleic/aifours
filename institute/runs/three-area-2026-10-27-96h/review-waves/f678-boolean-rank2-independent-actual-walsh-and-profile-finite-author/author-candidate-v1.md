# Independent physical Boolean rank-two finite author: exact construction, profiles, and unrun source

**Status: AUTHOR WRITTEN DERIVATION + PREPARED FINITE SOURCE; CHILD SCIENTIFIC EXECUTION NOT RUN.** This is a fresh finite-source-author contribution on the actual normalized five-span physical interface, not an independent review or a parent disposition. The displayed expected values below follow from the written derivations; they are **not** claimed as output from the prepared program. The program, all 64 transports, all 1,136 profile cases, and all negative controls remain unexecuted until a separately authorized parent source read and one-shot run. No old checker, held episode or consumer, sibling proof/code, linked source, external-model CLI, installation, network, scientific execution, test, build, lint or formatter was used. The parent must not infer a run or PASS from this document.

## 1. Frozen inputs and actual target

The only scientific bodies read were the entire ordered 353-line `literal-packet-v1.md`, SHA-256 `14d3eddd712c29ac7deccae411204f3decf65bc7d72d821ee72c0f30bf0c8229`: the new **unadopted** f664 author body, followed by its four already-frozen original scientific interfaces. They are imports with their recorded scopes, not an acceptance of f664. The fourth original interface is six-span; it is not a hypothesis for this five-span construction. No packet links were followed. The rank-two actual zero-flat/caller interface, actual four-fibre/XOR criterion, bent graph/phase normalization, and original balance transport are retained at their stated scopes. The frozen manifest is SHA-256 `25ef7afc00d28f2035182a15ba1555757a1296c6e01c81abc9284606b646b8c2`; the freeze receipt is `62e9329d901a66b380b0b1ad1714d18f07d78cc6e992bc2f7269aa73c2ae6a6a`.

The target is ONE common ternary array on `F2^6 x F2^2`, its four physical fibres, the U0 cap at **all** 64 frequencies and its specifically transported original balance, then the same array's U3 and the same support's complementary V, followed by restoration of the original caller. This document constructs a genuine physical **non-witness**, with an explicit cap violation; it does not replace the actual caller by separately selected spectra, a free balance frequency, or a six-span input.

## 2. Conventions and exact physical construction

Write `c=(ell,h,j,b)`, with `j=(j0,j1)` and `b=(b0,b1)`. Encode the physical six-bit coordinate by

```
c = ell + 2*h + 4*(j0 + 2*j1) + 16*(b0 + 2*b1),
e = 2, beta = 16, gamma = 32, b1-frequency = 32.
```

Dot products are ordinary bit parity; `chi_k(c)=(-1)^(k dot c)`. For `z=(j,b)`, take

```
f(z) = j0*j1,
r(z) = j0*b0 + j1*b1,
q(z) = 1 + b0*b1,              rho(b) = (-1)^q(b),
S = {(1,f(j),j,b): j,b in F2^2}.
```

All additions in the exponents are in F2. On the graph let `a=(-1)^r`, and let `a=0` elsewhere. Set `g=4` for `ell=b=j=0` and either h; set `g=-2` for `ell=b=0,j!=0`; set `g=rho(b)*(-2+3*1_S)` for `ell=1`; and set `g=0` otherwise. Thus the two 4-blocks are F, the six remaining blocks in their E row and 16 graph mates are D, and the 24 `ell=0,b!=0` blocks are Z.

Define the 64-entry `x0` exactly as follows, and zero elsewhere:

* on S, it is `-1` at `(j,b)=(0,1)` and at `(j,b)=(1,0),(2,0),(3,0)`; on the other 12 graph points it is `+1`;
* on the four graph mates `(1,1+f(j),j,0)` it is `-2`;
* for `j=0,1,2` on `(0,0,j,2)` it is `+2`, and on `(0,0,j,3)` it is `-2`.

Here 1,2,3 in j or b mean their two-bit encodings, not physical c. The actual six Z2 rows, in physical order `(beta,gamma,beta+gamma)`, are **(0,3,3)**.

For **every** prescribed carried frequency `t` in the 64-element dual space define `x_t(c)=chi_t(c)*x0(c)`. Then, on the **same** c, first define y by

* `y=-a*g*x_t` on S;
* `y=0` on F and the four D0 blocks, `y=+2` on the other 18 D blocks;
* `y=x_t` on the six Z2 blocks, `y=+4` at `(0,0,3,2)`, and `y=0` on the other Z blocks.

Form all 256 entries, for `w=(w0,w1)`, by

```
u_t(c,w) = [x_t(c) + 3*a(c)*(-1)^w0 + g(c)*(-1)^w1
             + y(c)*(-1)^(w0+w1)] / 4.
```

If `J = #{c : u_t(c,0)!=0} mod 2` is even, negate y at the single Z2 block `(0,0,0,2)` and form the inverse again; otherwise do nothing. This gives a completely specified y and u for each t, with no independently chosen U0/U3 spectra. At that block `|x_t|=|y|=2` and `y=x_t` before the toggle, so the toggle changes `u_t(c,0)` from `x_t/2` to zero and flips J, without changing any support count or x. It leaves all four entries ternary. On a graph block write `s=a*chi_1`, `v=g*chi_2`; the inverse is `(3s+v+x_t*(1-sv))/4`, directly ternary for `s,v,x_t in {+1,-1}`. The D and Z formulas have the displayed allowed forms. Consequently, for every t the exact physical block census is

```
S=16, F=2, D0=4, D3=18, Z2=6, Z4=1, Z0=17;
support(u_t)=116, sum x_t^2=56, sum y^2=128,
#{c:y(c)=0}=23, J=1.
```

For example, support is `16*3 + 2*4 + 22*2 + 6*2 + 4 = 116`. The specified gauge transport here is the character modulation of x; y and u are rebuilt from the physical rules and J toggle. It would be incorrect to assert that the entire `u_t` is merely `chi_t*u_0` while keeping a and g fixed. The true original t is not identified by these 64 conditional cases.

## 3. Independent F2 geometry, bentness, and full Walsh facts

The polar radical of f is exactly `K={(j,b):j=0}`, encoded in z as `{0,4,8,12}`. Its b projection is a bijection. Its derivative on K is zero, so in physical coordinates

```
H = {0,16,32,48},
L = H + <e> = {0,2,16,18,32,34,48,50},
L^perp = {0,1,4,5,8,9,12,13}.
```

Every ell=0 H-cell has one `b=0` E point and one point in each of the three nonzero b rows. The four D0 points are `[3,7,11,13]` and have four distinct L-cosets, indexed by the four j values.

The three required bent assertions follow without an appeal to a table: in the Walsh transforms of r and `r+f`, sum over b first. The b sum is zero unless the j value equals the b-frequency, when it is 4 in magnitude. For `f+q=1+j0*j1+b0*b1`, the two two-bit transforms factor and each has magnitude 2. All three 16-entry spectra thus have magnitude 4. The graph a is physical on all 64 c: its transform at h-frequency 0 or 1 is respectively a transform of r or `r+f`, with a harmless ell sign, so all 64 values have magnitude 4.

For g, let `(A,H0,J,B)` denote the four dual coordinates corresponding to `(ell,h,j,b)`. Its E-row contribution is 0 for `H0=1`, is -4 for `H0=J=0`, and is +12 for `H0=0,J!=0`. The ell=1 contribution is `-4*(-1)^A*W_rho(B)` for `H0=J=0`, zero for `H0=0,J!=0`, and `3*(-1)^A*W_(f+q)(J,B)` for `H0=1`. Since `W_rho(B)=+/-2` and `f+q` is bent, g has exactly four **+4** coefficients and 60 coefficients of magnitude 12. These are full 64-frequency claims, not separate spectra installed by hand.

Let P be the graph points with negative x0, W the ten non-graph magnitude-two x0 points, and N the negative points in W. Their actual encoded sets are

```
P = {5,9,15,17},
W = {3,7,11,13,32,36,40,48,52,56},
N = {3,7,11,13,48,52,56}.
```

Thus `|P|=4`, `|N|=7`, and `XOR(P)=XOR(W)=18=e+beta`; the imported rank-two criterion C holds. Independently, `hat(1_S)` is divisible by 8: when the h-frequency is zero it is 0 or 16; otherwise the sum over b vanishes unless the b-frequency is zero, in which case it is four times a two-bit bent transform, hence `+/-8`. Expanding character signs modulo four in `x0=1_S-2*1_P+2*1_W-4*1_N` gives

```
hat(x0)(xi) = 2*(10-|P|)-4*|N| + 4*(xi dot (XOR(P)+XOR(W)))  (mod 8),
```

so every coefficient is divisible by 8. On each ell=1 L-coset, the graph signs sum to 2 and the one D0 contributes -2. On each ell=0 coset the only nonzeros are opposite Z2 pairs. Therefore the sum on every L-coset is zero and `hat(x0)` vanishes on the displayed `L^perp`.

At b1-frequency 32, the four ell=1 j-slices each contribute -4, while every ell=0 Z2 pair cancels. Therefore **`hat(x0)(32)=-16`**, an explicit failure of the required U0 cap 8. For each specified t, the exact transform identity `hat(x_t)(xi)=hat(x0)(xi+t)` gives divisibility by 8, zero on `t+L^perp`, balance at precisely t, and the carried spike `hat(x_t)(t+32)=-16`. The actual Z2 row census remains `(0,3,3)` under all these sign transports.

The constructed y has a signed-character restriction to each of the four actual graph H-planes even for this non-witness. For each fixed j, the four x0 graph signs have product -1; multiplying by `chi_t` does not change that product. The four graph values of `a*g=(-1)^(r+q)` also have product -1, because r restricts linearly in b and q has the single quadratic term `b0*b1`. Hence the four signs of `y=-a*g*x_t` have product +1, equivalent on F2^2 to a signed affine character. This is the **same** y and same physical graph, not a separately selected character.

Finally, modulo 8, the physical inverse at w=0 yields at every c-frequency

```
hat(x_t) + 3*hat(a) + hat(g) + hat(y) = 4*J.
```

The right-hand side uses parity because signs in a character are indistinguishable modulo 2. Both `3*hat(a)` and `hat(g)` are 4 modulo 8, `hat(x_t)` is 0 modulo 8, and the actual toggle makes J=1. Thus `hat(y)=4 (mod 8)` at all 64 frequencies. This is a residue, **not** the U3 amplitude cap.

## 4. Seven U0 profiles and the complete 1,136-vector classification

Choose `M={<ell,j>}` and `L=<h,b>` as the eight physical L-coset representatives and the above L. For each `eta in L*`, let

```
Z_m(eta) = (1/4) sum_(v in L) x(m+v)*chi_t(m+v)*(-1)^eta(v).
```

Walsh inversion on M is the exact same-array identity

```
hat(x)(t + eta_bar + q_bar) = 4 * sum_(m in M) Z_m(eta)*(-1)^q(m).
```

For a zero-flat actual x, `Z_m(0)=0`. These Z are integers: the difference of an eta sum and the zero sum is minus twice the signed sum on an eta half-space; its odd support in any L-coset is empty or an affine H-plane, and its intersection with that half-space has even cardinality. Under the imported actual rank-two zero-flat conclusion **and** the U0 cap plus energy 56, all 56 other Walsh values have absolute value 8. Thus every one of the seven nonzero eta profiles has eight Walsh magnitudes 2 and energy 4. Conversely, zero eta plus seven such profiles, with the exact displayed transform, gives the full cap and the carried zero. This is conditional on the stated actual-interface hypotheses; it is not a construction of an x satisfying them.

The entire integer energy-four universe is explicitly

```
{ vectors with one entry +2 or -2 }                            (8*2 = 16)
union
{ vectors supported on I, |I|=4, each supported entry +/-1 }   (C(8,4)*16 = 1120).
```

There are no other integer partitions of 4 as a sum of eight squares. Every singleton has all Walsh magnitudes 2. For a four-support I in `F2^3`, the four positions form an affine two-flat exactly when their XOR is 0. A nonflat has four affinely independent points, so an affine sign character can match any assigned signs and produces a magnitude-4 Walsh coefficient. A flat has eight affine-character sign patterns, exactly those with sign product +1, which likewise produce a magnitude-4 coefficient. The other eight patterns have sign product -1; multiplication by any restricted character preserves that product, so their four signed terms sum to `+/-2` at every frequency. There are seven 2-dimensional linear subspaces and two cosets each, hence 14 affine two-flats.

Accordingly the **derived**, not empirically reported, census is

```
all energy-four integer vectors: 1136 = 16 + 1120;
accepted: 16 singletons + 14*8 odd-product flat signings = 128;
rejected: 1008.
```

This gives every case by an exact generator and an if-and-only-if predicate. The prepared source additionally emits a separate JSONL record containing the vector, all eight Walsh coefficients, support category and acceptance for **each** of the 1,136 cases. It checks the direct transform against an independent butterfly transform. Until a parent actually runs it, those 1,136 records do not exist as observed evidence.

## 5. Conditional cross-fibre and mod-16 implications; not an assay of the non-witness

The following is written reasoning at the original stated premises, not a new finite-run result. For a general admissible rank-two f, let K be its polar radical. Bentness of `f+q`, and the rank-two polars of f and q, imply by the four-dimensional alternating Pfaffian identity that `B_q|K` is nondegenerate; hence `K -> b` is an isomorphism. Bentness of r and `r+f` similarly gives `B_r|K=0`, so `B_(r+q)|K` is nondegenerate. Thus `a*g` restricts to a bent sign function on each graph H-plane.

Suppose, separately from the constructed non-witness, that the four D0 points lie in distinct ell=1 L-cosets **and the actual x has the full U0 cap and its carried balance**. In each such coset the weighted four graph signs sum to `+/-2` because the unique D0 cancels them; hence they are a three-to-one pattern. Let lambda vanish on H and equal 1 on e. The four ell=1 values of `Z(lambda)` are each `+/-1`, and the profile energy is exactly 4; all ell=0 lambda entries must therefore vanish. Together with the zero eta profile, this forces the weighted x sum to vanish in each ell=0 H-cell. Each has at most three Z points, so six nonzero Z2 points form three opposite-signed pairs.

For nonzero `alpha in H*`, use its two extensions `eta` and `eta+lambda`. Across each ell=1 coset the squared contributions of those two profiles sum to 1: the graph alpha coefficient and the single D0 contribution each have magnitude 2 and add/cancel. The four ell=1 cosets use four units of the two profiles' total energy eight. An occupied ell=0 H-cell contributes two units exactly when alpha is nonzero on its pair difference. Thus exactly two of the three pair differences are nonorthogonal to every nonzero alpha. In a two-space the three differences must be the three distinct nonzero vectors. The K-to-b bijection then forces **two Z2 points in each nonzero physical b row**. This is a necessary condition only; it is not existence or a full-branch exclusion. The constructed actual `(0,3,3)` case is consistent with the condition because its cap demonstrably fails.

For the same hypothetical capped physical x, its weighted graph signs are three-to-one, so x is bent on each graph H-plane. The bent `a*g` has the same unique nonzero alternating polar there; consequently the actual `y=-a*g*x` is a signed affine character on every one of those same four planes. If in addition the **same y** obeys J=1 and all 64 U3 caps, Parseval and the residue give exactly eight magnitude-four frequencies B and magnitude 12 elsewhere. If `n_alpha` counts B restricted to each `alpha in H*`, then every `n_alpha` is odd, hence the unordered multiplicities are `(5,1,1,1)` or `(3,3,1,1)`. For completeness, the conditional mod-16 derivation is:

* For nonzero `v in H`, `A_y(v)=sum_c y(c)y(c+v) = -2*sum_(xi in B)(-1)^(xi dot v)`. Graph-character contributions are multiples of 8; off S, pairing even y-values also gives multiples of 8. This forces all four n-alpha to have the same parity.
* Summing `A_y(v)` over the three nonzero v gives a graph contribution divisible by 16. Off S, only unordered pairs of magnitude-two entries matter modulo 16. The four D-mate cells contribute `4*C(3,2)=12` such pairs. The three occupied Z2 cells contribute an odd number each; other cells contribute none. Thus the total is 8 modulo 16.
* The Fourier formula for the same sum is `16-8*n_0`, so `n_0` and then all four n-alpha are odd.

**Finite status of this mod-16 premise: NOT TESTED.** Although the explicitly constructed non-witness does satisfy the separately checked written graph-character property, it has the U0 coefficient -16 and therefore fails the required cap. It cannot be used to assert or falsify the conditional n-alpha conclusion. The prepared source explicitly emits `NOT_TESTED` rather than pretending a capped case has been found. Both allowed patterns remain open.

## 6. Full prepared source, intended controls, and exact unpaid gates

The complete standalone standard-library source is the new sibling file [`independent-boolean-physical-profile-v1.py`](independent-boolean-physical-profile-v1.py), SHA-256 `4ee2939d220fecce13afe08a65de3b8e6c2513507ea8ae64ab679fe2bf1dc460` (hash observed after creation). It takes no arguments, inputs or file paths; performs no network, subprocess or filesystem writes; emits JSONL only; and needs a Python interpreter with integer `bit_count` support. It has a 45-second cooperative monotonic deadline and sticky SIGTERM/SIGINT stop latch; parent external supervision at 55 seconds remains separate. Blocking stdout or interpreter startup is not a claimed hard in-process time limit. The source emits all a/g/x0 data, all 256 entries of u and full 64-entry x/y Walsh spectra for each of the 64 t values; both Walsh implementations are compared. It independently recomputes the polar radical, H, L, K projection, four D0 cosets, bent spectra, C sets/counts, block census, row counts, graph-character restrictions, and exact profile transform. It emits the individual 1,136 vectors, then a summary derived by enumeration if all checks finish.

The named reason-specific negative controls are `wrong-normalization`, `free-balance-instead-of-specified-t`, `independent-u`, `graph-y-relation`, `odd-J`, `U3-residue`, `actual-U0-cap`, `six-span-is-not-five-span`, and `false-witness-scope-guard`. They deliberately corrupt an inverse, require the wrong frequency, replace the common u, flip a graph y value, toggle to even J, use its wrong residue, challenge the actual -16 cap, or exercise explicit scope tags. They are implementation/scope guard controls, **not** mathematical counterexamples to a theorem. The six-span tag is not a six-span scientific instance. The final witness guard deliberately cannot certify a positive caller: it refuses the actual uncapped example and has no implementation purporting to prove V or original caller restoration.

The exact remaining scientific obligations are: construct or rule out an actual common x satisfying all seven profiles, actual restrictions and specified t; then satisfy all 64 U3 caps and the same-case character/projection constraints on its physical y; then find a V with odd negative parity on the very same 140 zero positions and all 256 odd-half caps; finally restore and verify original gauge, balance, selected nonzero T, Boolean/rank/eight-zero and remaining original caller conditions. The presented sample pays none of these full-caller obligations and cannot close the rank-two five-span branch, any six-span branch, the original book target, or global NL242. No novelty, historical source equivalence, external-family, human or kernel acceptance is claimed.

## 7. Chronology and assurance

Before opening the scientific packet I read the complete f678 manifest, freeze, prepared live metadata, actual dispatch, and every listed status/permission control through its ending; I independently matched the three manifest/freeze/packet hashes quoted above and directly sent PREBODYACK to Main. I then read the entire packet in increasing raw slices of at most 20 LF; a mistyped 101–120 filename was immediately recovered with the correct raw range before continuing. All held episodes and all their consumers, expressly including f513/f586/f653/f654/f659/f660/f662, remain NONINPUT. This records actual source access, not an unobservable clean-cognition certificate.

I derived the formulas and authored the source only after packet completion. A native clock observation after the source was prepared was `2026-10-30T16:02:23-0700 PDT`; it is not a private start or completion timestamp. The source hash above is an administrative byte pin, not an execution. The child did not run the source, a mathematical calculation, CAS, solver, test, build, lint, formatter, external model, or linked source. Parent full-source reading, a separate GO and one bounded run, independent written reconstruction, original caller verification, and any broader adoption remain unpaid. No observed output is fabricated here.
