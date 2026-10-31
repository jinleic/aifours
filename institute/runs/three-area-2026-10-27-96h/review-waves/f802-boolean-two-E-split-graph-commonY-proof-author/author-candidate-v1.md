# F802 — mixed affine/bent graph-Y parity and the physical Z4 obstruction

**Status:** fresh, nonblind, same-harness GENERAL AUTHOR written reconstruction. This is a conditional proof candidate, not parent adoption or a human, independent-model-family, kernel, original-source-identity, or novelty determination. Packet S1 already states a proof of this same branch; this return reconstructs its load-bearing mixed-row argument and all the modulo-8 factors rather than claiming discovery or a blind review. No scientific executable, solver, test, compiler, external CLI, network, or old code was run or read; no new executable source is supplied.

## 1. Exact scope and imports

Work with one actual normalized rank-two five-span object at the packet's local-H/count interface. It supplies the same physical `f/R, a, g, u, x=U0, y=U3`, physical inverse and **specified** original-DC-transported character `t`, with `xhat(t)=0`. Let `X(c)=(-1)^t(c)x(c)` and `Y(c)=(-1)^t(c)y(c)` only for analysis. Modulate both arrays by that same given character; do not select a convenient zero or change the actual phase. Translation of a Walsh spectrum by `t` preserves the imported caps and the common-Y residue condition.

The following are necessary inputs at exactly the packet's named interface; the proof below does **not** derive the physical inverse, general graph phase, original normalization or residue bridge from first principles.

* Write positions as `(ell,h,i,v)` with `ell,h in F2` and row and fibre coordinates `i,v in F2^2`. In row `i`, the graph is `ell=1,h=F_i` and its physical mate at the **same** `v` is `h=1+F_i`; `sum_i F_i=1` in `F2`. There are four D0 in the 16 graph mates and six non-full E sites at `ell=0,v=0`, six Z2, one Z4, 17 Z0 and 18 D3. In the branch considered, exactly two D0 are E sites and exactly one is a graph mate in each of two different graph rows. Consequently the other 14 graph mates are D3. Both possible actual E occupancy shapes, `2` and `1+1`, are covered.
* On the graph, `X=+/-1`. A D0 mate has `X=+/-2`, a D3 mate has `X=0`, and each occupied graph row has one D0. The same-X zero-flat equations and all seven nonzero quotient profiles apply simultaneously:
  `Z_(ell,i)(s,alpha)=(1/4) sum_(h,v) X(ell,h,i,v)(-1)^(s h+alpha(v))`, `Z_(ell,i)(0,0)=0`; each nonzero `(s,alpha)` profile is either one entry `+/-2`, or four entries `+/-1` on one affine two-flat of `(ell,i)` with sign product `-1`.
* On the actual graph `Y=-a g X`. In a common choice of fibre coordinates, its phase has quadratic part `q(v)=v_0 v_1` and row-dependent linear covectors `rho_i` that are the four distinct elements of `(F2^2)*`; hence `sum_i rho_i=0`. Row signs and constants are arbitrary but fixed by the object. This is the actual phase import, not a freely chosen independent graph spectrum.
* The same physical Y has graph magnitude 1, a graph D0 mate value 0, and a graph D3 mate value of magnitude 2. The unique Z4 has `|Y|=4` at a nonzero fibre coordinate `v`; the other h-site at that exact `(i,v)` is another Z site, with magnitude 0 or 2. No bound on either full `ell=0,v=0` site's Y value is assumed.
* All 64 full Walsh coefficients of this Y are `4 mod 8`, with absolute value at most 12, and `sum_c Y(c)^2=128`. These conditions, in particular the J=1/residue bridge, refer to the **same** physical Y, not independently specified paired coefficients.

**Claim under these imports:** the entire `d_E=2`, graph-occupancy `1+1` branch is impossible. This is conditional on the named imports and does not assert the graph-occupancy `2` branch, any other rank or original caller.

## 2. The simultaneous X profiles force the missing-position identity

Let the two occupied rows be `p,p'` and the two unoccupied rows `r,r'`. The four row labels form `F2^2`, so the same nonzero difference `Delta=p+p'=r+r'` joins both pairs. Write the occupied mate coordinate in row `i` as `z_i`, and its value as `2 epsilon_i`, with `epsilon_i in {+1,-1}`.

Zero-flat gives graph-sign sum `-2 epsilon_i` in an occupied row, hence exactly a 3:1 sign split. Every such four-sign function is uniquely of the form

`X(1,F_i,i,v)=sigma_i (-1)^(q(v)+nu_i(v))`,

with `sigma_i=+/-1` and a covector `nu_i`. On an unoccupied row zero-flat gives a 2:2 split, so the graph signs form `sigma_i(-1)^theta_i(v)` with a **nonzero** covector `theta_i`.

At lambda `(s,alpha)=(1,0)` the graph entries are `-(-1)^F_i epsilon_i` on `p,p'` and zero on `r,r'`. There are two magnitude-one graph entries. Therefore lambda is necessarily a mixed four-entry plane, not an E singleton or graph singleton: its two E-side rows have the same pair difference `Delta` and all four signs multiply to `-1`. This deduction does not eliminate either physical E occupancy shape. It also does not replace the other six columns by independently chosen E arrays.

For all `alpha`, identify two-bit covectors with their coordinate vectors and put `J(a_0,a_1)=(a_1,a_0)`, so `q(alpha+nu)=q(alpha)+q(nu)+alpha(J nu)`. The unnormalized two-bit Walsh transform of `(-1)^(q(v)+nu(v))` is `2(-1)^q(alpha+nu)`. Using the zero-flat relation to fix its overall sign, the occupied row contributes a magnitude-one graph profile entry on exactly the slice

` s_i(alpha) = 1 + q(alpha) + alpha(J nu_i + z_i)`  in `F2`.  (2.1)

An unoccupied row contributes one graph entry on **both** s-slices precisely when `alpha=theta_i`. An affine two-flat intersects the graph half in 0, 2 or 4 points, and a singleton cannot contain one of these magnitude-one graph entries. Hence the number of graph entries on each slice must be even. If `L(alpha)=[alpha=theta_r]+[alpha=theta_r']` as an integer, the exhaustive profile consequences are:

| `L` | relation between occupied slices | graph entry counts across the two slices | required completion |
|---:|---|---|---|
| 0 | `s_p=s_p'` | 2, 0 | the two-graph slice is one mixed plane; the other is an E singleton or E plane |
| 1 | `s_p!=s_p'` | 2, 2 | both slices are mixed planes, each with its actual graph-pair difference |
| 2 | `s_p=s_p'` | 4, 2 | the four-graph slice is the whole graph plane; the other is mixed |

All planes have their required sign product `-1`. In particular the parity of the table is, for every `alpha` including zero,

` s_p(alpha)+s_p'(alpha) = [alpha=theta_r]+[alpha=theta_r']` in `F2`.  (2.2)

The right side is the linear function `alpha(J(theta_r+theta_r'))`: if the two nonzero theta values agree it is zero; if they differ, it is one on precisely those two nonzero covectors and zero on the other two. Comparing (2.1) and (2.2) yields the same-object relation

`z_p+z_p' + J(nu_p+nu_p') = J(theta_r+theta_r')`.  (2.3)

No arbitrary independent mate positions, graph phases, lambda realization, or E profile were inserted into this equation.

## 3. Complete modulo-8 reconstruction, including all 14 actual D3 mates

The physical graph identity makes the two occupied graph-Y rows affine and the other two bent:

`phi_i=rho_i+nu_i` for `i=p,p'`, and `mu_i=rho_i+theta_i` for `i=r,r'`.

Thus an occupied graph-Y row has unnormalized fibre Walsh transform `+/-4 [alpha=phi_i]`, whereas for each unoccupied row there is a fixed sign `tau_i` such that its transform is `2 tau_i(-1)^q(alpha+mu_i)`. The graph Y signs are not selected independently of X; only the signs left free by the common physical object are denoted here.

For a fixed partial frequency `(s,alpha,beta)`, define

`A_ell(s,alpha,beta) = sum_(h,i,v) Y(ell,h,i,v)(-1)^(s h+alpha(v)+beta(i))`.

For each graph row set `D_i(v)=Y(1,1+F_i,i,v)/2` and `M_i(alpha)=sum_v D_i(v)(-1)^alpha(v)`. This records the physical same-v mates: `D_i` has four signs in an unoccupied row, and three signs plus a zero exactly at `z_i` in an occupied row. Thus all eight unoccupied-row D3 mates and all six occupied-row D3 mates are included; the two missing terms are the actual D0 mates.

For each unoccupied row, `M_i(alpha)` is even and `M_i(alpha)=M_i(0) mod 4` for every alpha: a nonzero character flips exactly two of its four signs. Since an even integer is congruent to its negative modulo 4, its row weight also cannot change `2M_i mod 8`. Define the fixed bit

`k = (M_r(0)/2 + M_r'(0)/2) mod 2`.

For an occupied row, choose `d_i in {+1,-1}` with `d_i=M_i(0) mod 4`. Then for every alpha

`M_i(alpha) = d_i (-1)^alpha(z_i) mod 4`.  (3.1)

Indeed, a nonzero character flips two fibre positions: if the missing `z_i` is not among them it flips two present signs, while if it is among them it flips one. These change the three-sign sum by 0 or 2 modulo 4 respectively.

Define the **actual weighted** signs

`R_i=tau_i (-1)^(beta(i)+s F_i+q(alpha+mu_i))` for `i=r,r'`,

`T_i=d_i (-1)^(beta(i)+s(1+F_i)+alpha(z_i))` for `i=p,p'`.

The graph affine terms, graph bent terms, unoccupied mate rows and occupied mate rows therefore give the full congruence

`A_1 = 4k + 4([alpha=phi_p]+[alpha=phi_p']) + 2(R_r+R_r') + 2(T_p+T_p')  (mod 8)`.  (3.2)

The four summands in (3.2) are respectively the eight unoccupied-row mates, two occupied graph rows, two unoccupied graph rows, and six occupied-row mates. In particular `A_1` is divisible by 4. For `R,R',T,T' in {+1,-1}`, `(R+R')/2=(1+RR')/2 mod 2`, and similarly for T. Dividing (3.2) by 4 gives

`A_1/4 = k + [alpha=phi_p]+[alpha=phi_p'] + (1+R_r R_r')/2 + (1+T_p T_p')/2  (mod 2)`.  (3.3)

The fractions are ordinary integers before reduction. Set bits `r_0,t_0` by

`(-1)^r_0 = tau_r tau_r' (-1)^(q(mu_r)+q(mu_r'))`,  `(-1)^t_0=d_p d_p'`.

The complete two product exponents, including beta, s, and alpha factors, are

`R_r R_r' = (-1)^[r_0 + beta(Delta) + s(F_r+F_r') + alpha(J(mu_r+mu_r'))]`,

`T_p T_p' = (-1)^[t_0 + beta(Delta) + s(F_p+F_p') + alpha(z_p+z_p')]`.  (3.4)

For a bit `w`, `(1+(-1)^w)/2=1+w mod 2`. Therefore the two `beta(Delta)` terms cancel, while the two s coefficients sum to `sum_i F_i=1`. The function `[alpha=phi_p]+[alpha=phi_p']` is affine in alpha with linear coefficient `J(phi_p+phi_p')`: if the phi coincide it is zero; otherwise its support is the unique two-point affine line through them. Consequently (3.3) becomes

`A_1/4 = c + s + alpha(z_p+z_p'+J(mu_r+mu_r'+phi_p+phi_p'))  (mod 2)`,  (3.5)

where an explicit object-dependent constant is

`c = k + [phi_p=0]+[phi_p'=0]+r_0+t_0  (mod 2)`.

By the four distinct physical row covectors, `sum_i rho_i=0`. Substituting the definitions of mu and phi and applying (2.3), the alpha coefficient in (3.5) is

`z_p+z_p' + J(theta_r+theta_r'+nu_p+nu_p') = 0`.

Thus, **uniformly for all alpha and beta of this one object**, and with no choice of t,

`A_1(s,alpha,beta)/4 = c+s  (mod 2)`.  (3.6)

In particular the s-slices have opposite parity. Let `s_*` denote the actual odd slice, determined by the given Y. This is where the simultaneous X profiles, actual missing-mate positions, distinct physical phase covectors, and odd F table are all essential.

## 4. Exact energy and eight-small allocation

The physical ell-one Y energy is `16*1^2+14*2^2=72`. Partial Parseval gives `sum_(s,alpha,beta) A_1^2=32*72`. By (3.6), the cap and divisibility, on the even slice `|A_1|` is 0 or 8, while on the odd slice it is 4 or 12. There are 16 partial frequencies per slice. Let `n` count even-slice 8s and `m` count odd-slice 4s. Dividing Parseval by 16 yields

`4n + m + 9(16-m) = 144`, hence `n=2m`.  (4.1)

The full coefficients at each partial frequency are `A_0+A_1` and `A_0-A_1`; their two caps are equivalent to `|A_0|+|A_1|<=12`. Since `A_1` is divisible by 4 and each full coefficient is 4 modulo 8, `A_0` is also divisible by 4 and `A_0/4,A_1/4` have opposite parity. Every full coefficient therefore has absolute value 4 or 12. Full Parseval and energy 128 imply exactly eight magnitude-4 coefficients: `16N_4+144(64-N_4)=64*128`, so `N_4=8`.

The **actual paired** possibilities, including their exact small-coefficient contributions, are:

| `|A_1|` | permitted `|A_0|` | number of the pair of magnitude 4 |
|---:|---|---:|
| 8 | 4 | 1 |
| 4 | 0 or 8 | 2 if 0, otherwise 1 |
| 12 | 0 | 0 |
| 0 | 4 or 12 | 2 if 4, otherwise 0 |

Let `h` count odd-slice `|A_1|=4` pairs with `A_0=0`, and let `q_4` count even-slice `A_1=0` pairs with `|A_0|=4`. Then the exact eight-small count is

`8=n+m+h+2q_4=3m+h+2q_4`, with `0<=h<=m`.  (4.2)

Since `n+m<=8`, `m<=2`. The complete resulting allocation is

| `m` | `n` | `h` | `q_4` | odd-slice nonzero `A_0` count |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 4 | 0 |
| 1 | 2 | 1 | 2 | 0 |
| 2 | 4 | 0 | 1 | 2 |
| 2 | 4 | 2 | 0 | 0 |

No other possibility satisfies (4.1)–(4.2). Therefore over the **entire same actual odd slice** `s_*`, at most two `A_0` values are nonzero, and each nonzero value has magnitude exactly 8. This slice conclusion is strictly stronger than selecting a convenient entry or invoking only the arithmetic census.

## 5. Inversion at the actual Z4

For every physical `(i,v)`, invert the 16-point Walsh transform in `(alpha,beta)` on the one fixed s-slice:

`Y(0,0,i,v)+(-1)^s_* Y(0,1,i,v) = (1/16) sum_(alpha,beta) A_0(s_*,alpha,beta)(-1)^(alpha(v)+beta(i))`.

The right side has absolute value at most `2*8/16=1`. At the unique actual Z4 its fibre coordinate is nonzero, so the opposite-h point at the **same** `(i,v)` is another Z site, not an E site or one of the two full sites. That other site has magnitude 0 or 2. The reverse triangle inequality therefore makes the same left side have magnitude at least `4-2=2`, for either value of `s_*`. This contradiction proves the conditional claim.

The proof never assumes that the full sites have small Y, replaces the opposite point by a virtual site, constructs an independent spectrum, restricts the physical E occupancy shape, or changes the carried t. Its only mathematical dependencies are the explicit common-object, profile, phase, count and J1/U3 imports in Section 1.

## 6. Open cases and evidence boundaries

Packet S6 separately records the even-`d_E` exclusion of 1 and 3 and the common-U3 census at its own named scope; packet S7 separately records a conditional `d_E=4` obstruction at its stated interface. Those dispositions are not established anew by this return. In particular, this candidate does not resolve `d_E=2` with both graph D0 in one row, the still-unpaid `d_E=0` graph occupancy branches, V signs, global rank-two/five-span or NL242, an original selected-T/rank/eight-zero caller, or a physical witness. The prior separately scoped one-D0-per-graph-row result must not be widened to other `d_E=0` shapes. S2–S5's omitted E-singleton cases remain important for other occupancies; no singleton is silently discarded here, because lambda in this branch actually has two magnitude-one graph entries.

S8 and S9 are prior parent finite-run receipts with only their expressly stated finite scopes. They are neither a new execution by this author nor finite verification of this mixed-row proof. Parent must independently check the present mathematical argument and its precise imports before any disposition. There is no automatic adoption, family/human/kernel check, source-identity determination, or novelty conclusion.

## 7. Packet and control coverage

After Main's direct actual-receipt notice, I read this wave's actual dispatch, complete manifest, freeze receipt, final pre-dispatch binding, prepared metadata, and all 22 manifest-listed status/permission controls through their endings. The controls were used for status and permissions only: prospective author method and owner direction; parent L1, privacy, core-Gram, AME and PH quarantine controls; f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660 and f662 status controls; parent remaining-d0 E-row omission and pre-run f746/f749 correction controls. All genuinely held episodes **and all consumers** remained NONINPUT. I sent Main the direct PREBODY ACK naming these controls and ordered part count before opening the body. Then I read the only packet part serially RAW, windows `1–20, 21–40, ..., 881–900, 901–907`, through its complete ending and long lines, before mathematical comparison or work. No packet body or mathematics preceded the ACK. No global cognition/separation certificate is claimed.

Parent-supplied administrative pins: manifest `d9faf36052dd91d289e47beb426edf88e8e7661ac3b35c97741e304bfef6c811`; freeze receipt `ab41bb12b9b95ada7a138d2dda13f65eb9f9d65b724afd57eb3cc47aa1f06591`; final binding `3140a344f1e9970b73f9dfa4377c3bc1478d1d2bc06ce6ddef9a0956a628a149`; prepared metadata `c9de4dd5998f9b8f0b0c34a1cd21f4f1a0ae0b13e2db094bb43bcc0589fc311e`; packet part 01, 907 LF, `cb27c6e8096055247d931057fb778465a7f7a354dcd009c723c649f44d230de9`. These are supplied metadata, not an independently run hash check or correctness certification. The complete source bodies rendered in the part, with their manifest-supplied pins, are:

| ID | Body | LF | SHA-256 |
|---|---|---:|---|
| S1 | f788 `author-candidate-v1.md` | 179 | `1c51df762a1878cae342b32b4a34fead49ca39c2813bdab41ba3e7a9ed3b737d` |
| S2 | f748 omitted-lambda-gap record | 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S3 | f753 quotient-census erratum | 9 | `90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606` |
| S4 | f753 `author-candidate-v1.md` | 121 | `e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8` |
| S5 | f754 author addendum 1 | 15 | `4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114` |
| S6 | parent E-row parity/lambda/common-U3 disposition | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S7 | parent entire four-E-row common-Y disposition | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S8 | f755 local-profile/U3 finite receipt | 256 | `d3cdcca328bf4c902c214ddbb9b5d42fccb41f56406147681c3baf2880f5aaf1` |
| S9 | f778 one-shot finite receipt | 182 | `72ce3e26ffc187528890a9d0a808066ceb13b5d6fb9040644cf82f60b9871d08` |
| S10 | recovered local-H/general-g foundation | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |

No linked outgoing source, old code, sibling return or unlisted scientific source was opened. All mathematical work above is written reconstruction, not an executed scientific calculation.
