# F818 — a uniform actual common-slice parity lemma and the entire two-E obstruction

**Status: nonblind same-harness GENERAL AUTHOR written candidate; not independently checked or parent-adopted.** This is one conditional argument about the named actual rank-two, five-span, m116 same-object interface. Its common-slice lemma treats every even E-row D0 count and every graph D0 distribution at once. Its no-go treats the entire two-E case, including both graph occupancy types `2` and `1+1` and both E allocations `2` and `1+1`. It neither establishes original-source identity nor automatically promotes any union, full caller, all five-span, V, NL242, novelty, human, independent-family or kernel claim. The same-object imports below are load-bearing.

## 1. Named physical interface and statement

Work throughout with **one** actual `f/R, a, g, u, x=U0, y=U3`, the physical inverse, local `H_loc=0` and the named count/phase/general-g bridges in the frozen packet. Coordinates are `(ell,h,i,b)`, with `ell,h in F_2` and `i,b in F_2^2`. In graph row `i`, the four graph sites are `(1,F_i,i,b)` and their physical same-`b` mates are `(1,1+F_i,i,b)`, with `sum_i F_i=1` in `F_2`. The two full sites are `(0,h,0,0)`; six E-row sites have `ell=0`, nonzero `i`, and `b=0`; Z sites have `ell=0`, `b!=0`.

There are four actual D0 sites in the 16 graph mates and six E-row sites. Put `d=d_E` for the E count and `k_i` for the graph-mate count in row `i`; hence `sum_i k_i=4-d`. The graph signs have magnitude one in X and Y. At graph D0 mates X has magnitude two and Y is zero; at all other graph mates X is zero and Y has magnitude two. At ell zero there is a unique physical Z4 of `|Y|=4`; each other Z has `|Y|=0 or 2`. Its opposite-h mate at the same `(i,b)` is a different Z, since `b!=0`. These are physical statements, not choices of independent arrays.

Use the **specified** carried original-DC character `t`, not a newly selected character, and let `X=(-1)^t x`, `Y=(-1)^t y`. Assume `xhat(t)=0`, the complete all-U0 divisibilities/caps and the seven simultaneous nonzero same-X quotient profiles. Explicitly, with

`Z_(ell,i)(s,alpha) = (1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`,

all eight `Z_(ell,i)(0,0)` vanish and every other column is either one `+/-2` or four `+/-1` supported on one affine two-flat of `(ell,i)`, with sign product `-1`. The proof below uses only the resulting graph-side parity, but does not replace the physical profile import by arbitrary local data.

The actual phase bridge says that on graph row `i`, `Y` is `X` times a row sign and `(-1)^(q(b)+lambda_i(b))`, where `q(b)=b_1 b_2` and the four actual two-bit covectors `lambda_i` have XOR zero. This is the same graph phase arising from `Y=-agX`, not a freely selected Fourier phase. Retain J=1/general-g residue: all 64 full Walsh coefficients of this same Y are `4 mod 8`; also `sum Y^2=128` and all 64 absolute values are at most 12. In particular the transported Y remains the same physical modulation of y.

**Claims under these imports.**

1. For *arbitrary* `d` and `k_i` obeying `sum_i k_i=4-d`, the negative-graph-position XOR identity in Section 2 is necessary. If `d` is even, one fixed bit `c`, depending on the actual object, satisfies

   `A_1(s,alpha,beta) = 4(c+s) (mod 8)`

   for every `s`, every b-frequency `alpha` and every row-frequency `beta`. Thus the two entire s-slices have opposite parity in `A_1/4`; there is no exclusion of `alpha=0`. The cases `d=0,2,4` and all their graph occupancies are included, including four odd graph rows.
2. If additionally `d=2`, these conditions are mutually inconsistent. No choice of the graph `2` versus `1+1` partition, E `2` versus `1+1` allocation, actual signs, permitted profile/λ alternative, or admitted odd F changes the conclusion.

The existing same-X theorem that `d` must be even is a separate imported result (packet S2), not something needed to prove the XOR identity for an arbitrary `d`. The proposed named full union is not asserted here.

## 2. Global negative-location XOR, with every k_i allowed

All additions of positions are XORs in `F_2^2`. Write `S_i(b)=X(1,F_i,i,b)` and let `e_i(b)` be `+1` or `-1` at a D0 mate and zero elsewhere, so that the mate X value is `2e_i(b)`. Define

`P_i = XOR_{b:S_i(b)=-1} b`,   `B_i = XOR_{b:e_i(b)!=0} b`,   `B = sum_i B_i`.

The zero-flat equation is `sum_b S_i(b)+2 sum_b e_i(b)=0` in each graph row. For nonzero `alpha`, the sum of the graph-half entries of the actual `(s,alpha)=(0,alpha)` profile is even: a singleton `+/-2` contributes zero modulo two; a four-`+/-1` affine two-flat intersects the graph half `ell=1` in 0, 2, or 4 points. **It is the number of odd-valued graph entries that is even**, not necessarily the number of all nonzero graph entries: a graph singleton `+/-2` is permitted.

For each row subtract its zero-flat equation before dividing by four. Since `{b:alpha(b)=1}` has two points,

`Z_(1,i)(0,alpha) = -(1/2) sum_{alpha(b)=1} S_i(b) - sum_{alpha(b)=1} e_i(b)`.

Modulo two the first term is `1+alpha(P_i)` and the second is `alpha(B_i)`. Summing over the four rows, the four constants cancel; graph-half profile parity therefore gives

`alpha(sum_i P_i+B)=0` for every nonzero `alpha`, hence **`sum_i P_i=B`**.  (2.1)

The rowzero/profile proof did not assume `d=0`, any equality of row offsets, a graph character type, the signs of the mates, or any particular E allocation. It includes singleton columns and every `k_i` from 0 through 4.

Let `p_i` be the number of negative graph signs. Rowzero gives `4-2p_i+2 sum_b e_i(b)=0`; hence `p_i=2+sum_b e_i(b)` and `p_i = k_i (mod 2)`. Thus the number `r` of odd-k rows has parity `sum_i k_i=4-d`. In the even-d case used next, `r` and `4-r` are both even.

## 3. Even and odd graph phases and the row-covector identity

Use fixed two-bit coordinates; `J(a_1,a_2)=(a_2,a_1)` identifies a covector with a vector, and conversely. It obeys `q(u+v)=q(u)+q(v)+u(Jv)` when the coordinates are interpreted in the natural dual pairing.

* If `k_i` is even, `p_i` is 0, 2 or 4. Every such four-sign row is a signed character `S_i(b)=sigma_i(-1)^xi_i(b)`, with `xi_i=0` allowed. Its negative-position XOR is `P_i=J xi_i`. For `xi_i!=0` the two negative positions form an affine line with direction `J xi_i`; for the constant rows the XOR is zero. The actual phase makes the Y graph row `G_i(b)=tau_i(-1)^(q(b)+theta_i(b))`, where `theta_i=lambda_i+xi_i`.
* If `k_i` is odd, `p_i` is 1 or 3. There is a unique exceptional position `gamma_i` and a sign `sigma_i` with `S_i(b)=sigma_i(2 1_[b=gamma_i]-1)`. In either sign choice `P_i=gamma_i`, since the XOR of all four b-points is zero. The two-bit identity `2 1_[b=gamma]-1 = sign * (-1)^(q(b)+((1,1)+J gamma)(b))` shows that the graph Y row is the signed affine character with covector `kappa_i=lambda_i+(1,1)+J gamma_i`. Additive sign constants are absorbed into the actual row sign; no assumption that all graph Y rows are affine is made.

For even `d`, summing these covectors, using `sum_i lambda_i=0`, the even number of odd rows, and (2.1), yields

`sum_{i even-k} theta_i + sum_{i odd-k} kappa_i = J B`.  (3.1)

This includes constant even-k graph characters and does not identify distinct rows' covectors or exceptional positions. In particular, four odd rows are included: under the actual total-four-D0 count they can occur only when `d=0` and every `k_i=1`.

## 4. One exact A1/4 parity on each entire slice

For the actual common Y define

`A_ell(s,alpha,beta) = sum_(h,i,b) Y(ell,h,i,b)(-1)^(s h+alpha(b)+beta(i))`.

For even-k graph rows, the two-bit Walsh transform is

`sum_b G_i(b)(-1)^alpha(b) = 2 tau_i (-1)^q(alpha+theta_i)`.

For odd-k graph rows it is zero except at `alpha=kappa_i`, where it is `+/-4`. There are `12+d` actual D3 graph mates; each contributes a signed magnitude-two term, including its actual h, i and b phase. Write `m_alpha` for the number of odd-k rows with `kappa_i=alpha`, and set

`N=(4-r)+(12+d)`,  `v=B+J sum_{i even-k} theta_i`.

The integer `N` is even. The bent graph rows and D3 mates give exactly `N` signed magnitude-two terms. For any even N, if `w` of their signs are negative, half their sign sum has parity `N/2+w`. The odd-k graph rows contribute `m_alpha` modulo two after division by four. Thus `A_1/4` is an integer, and multiplying the actual N signs gives the following exponents:

* The beta exponent is `beta(sum_even i + sum_i (4-k_i)i)=beta(sum_all i)=0`. Here `(4-k_i) mod 2` is one precisely for odd-k rows and `sum_all i=0` in the four-point row plane.
* The s exponent is `s[sum_even F_i + sum_i (4-k_i)(1+F_i)] = s[sum_all F_i+r]=s`.
* The alpha exponent is `alpha(B+J sum_even theta_i)=alpha(v)`. Indeed, the `q(alpha)` terms from bent rows cancel because `4-r` is even, and the XOR of all non-D0 mate b-locations is `B`: all four b-points in each row XOR to zero.

All remaining signs and `q(theta_i)` terms are independent of `s,alpha,beta`. Hence for one actual constant `c_0`,

`A_1(s,alpha,beta)/4 = c_0+s+m_alpha+alpha(v) (mod 2)`.  (4.1)

Equation (3.1) gives the crucial same-object relation

`sum_{i odd-k} kappa_i = J v`.  (4.2)

This derivation uses actual weighted mate signs and graph phase; it does not infer the result from an independent spectrum, an assumed equality of odd offsets, or a parity check restricted to nonzero alpha.

**Parity-function lemma, including four odd rows.** Let `f(alpha)=m_alpha mod 2` on the four covectors. Its support has even cardinality because `r` is even, and the XOR of its support is `sum_odd kappa_i=Jv`, including repeated covectors with their correct multiplicity. There are only three possibilities:

* Empty support or all four covectors: the support XOR is zero, so `v=0`; `f` is constant.
* Two distinct support points `a,a'`: their XOR is `Jv!=0`. They form a two-point affine line. The nonzero linear function `alpha -> alpha(v)` is constant on each coset of its direction, because `(Jv)(v)=0`, and changes between the two cosets. Hence the indicator `f` of this line differs from `alpha(v)` by a constant.

Consequently in every case `m_alpha+alpha(v)=m_0 (mod 2)` for **all** alpha, where `0` is the zero b-frequency. This explicitly includes any four odd rows, including zero, two, or four odd-multiplicity covectors. Substitution in (4.1) proves

`A_1(s,alpha,beta)/4 = c+s (mod 2)` for all `s,alpha,beta`,  (4.3)

with `c=c_0+m_0`. The precise even slice is object-dependent; neither t, c nor the actual Y is changed to choose it. Equivalently `A_1=4(c+s) mod 8`, simultaneously over all 16 `(alpha,beta)` cells of each slice.

## 5. Uniform d=2 energy, eight-small census and Z4 contradiction

Assume `d=2`. There are 14 D3 graph mates, so the ell-one spatial energy of the **same Y** is `16+14*4=72`. Let `s_*` be the odd `A_1/4` slice in (4.3); the other is the even slice. At each paired frequency the two full coefficients are `A_0+A_1` and `A_0-A_1`. Their residue `4 mod 8` makes both `A_0/4` and `A_1/4` integers of opposite parity. Their two caps are exactly `|A_0|+|A_1|<=12`.

Each of the 64 full coefficients has magnitude 4 or 12. Parseval and total spatial energy 128 give `16 N_4+144(64-N_4)=64*128`, so **exactly eight** full coefficients have magnitude 4. Each s-slice has 16 `(alpha,beta)` cells. On the even slice `|A_1|` is 0 or 8; on the odd slice it is 4 or 12. Let `n` count the even-slice 8s and `m` the odd-slice 4s. Partial Parseval, divided by 16, gives

`4n + m + 9(16-m) = 32*72/16 = 144`, hence `n=2m`.  (5.1)

The pair-by-pair possibilities, including their small-full-coefficient counts, are:

| `|A_1|` | allowed `|A_0|` | number of magnitude-4 full coefficients |
|---:|---:|---:|
| 12 | 0 | 0 |
| 8 | 4 | 1 |
| 4 | 0 or 8 | 2 or 1 |
| 0 | 4 or 12 | 2 or 0 |

Let `h` count the odd-slice `|A_1|=4` cells having `A_0=0`, and `z` count the even-slice `A_1=0` cells with `|A_0|=4`. Then

`8=n+m+h+2z=3m+h+2z`, with `0<=h<=m`.  (5.2)

Since `3m<=8`, `m=0,1,2`. If `m=0`, the odd-slice A0 is identically zero. If `m=1`, parity in (5.2) forces `h=1`, again giving identically zero. If `m=2`, `h=0` or 2, so at most two odd-slice A0 values are nonzero, each of magnitude 8. Equivalently the complete solutions `(n,m,h,z)` are `(0,0,0,4)`, `(2,1,1,2)`, `(4,2,0,1)`, `(4,2,2,0)`. Thus

`sum_(alpha,beta) |A_0(s_*,alpha,beta)| <= 16`.  (5.3)

Invert the **actual** 16-point Walsh transform in `(i,b)` at this same slice:

`Y(0,0,i,b)+(-1)^s_* Y(0,1,i,b) = (1/16) sum_(alpha,beta) A_0(s_*,alpha,beta)(-1)^(alpha(b)+beta(i))`.

Equation (5.3) bounds its absolute value by 1 at every physical `(i,b)`. At the unique actual Z4, however, `b!=0` and the opposite-h point at the very same `(i,b)` is a different Z of absolute value at most 2. The displayed sum or difference there has absolute value at least `4-2=2`, a contradiction. No bound on either full site is needed.

This proof never branches on the E locations or on λ. Because `sum_i k_i=2`, the only graph occupancies are `2` and `1+1`; because exactly two of the six E sites are chosen, they are in either one E row or two. The universal argument retains every such physical placement and sign, including graph/E singleton and mixed-plane profile alternatives whenever permitted. It is not a claim that all these alternatives are realizable.

## 6. Other even counts and precise frontier

The uniform parity assertion (4.3) itself also covers `d=0` and `d=4`. For illustration of its exact strength, let `n,m,h,z` have the same meanings as above. In general the graph/mate spatial energy is `64+4d`, so partial Parseval gives `n=2m+d-4`, while the eight-small equation remains `8=n+m+h+2z`.

For `d=4`, `n=4+2m` and the small budget gives `m<=1`. If `m=0` the odd-slice A0 is zero; if `m=1`, the count forces `h=1`, again giving zero. Physical Z4 then gives the same contradiction as above. This is a reconstruction under the stated actual imports, consistent with but not a new adoption of packet S5. For `d=0`, the parity/census alone gives `m in {2,3,4}` and `n=2m-4`; it does **not** by itself exclude the branch. The separate d=0 actual obstruction and its additional proof are packet S4, not proved by the census. The even-E result is packet S2. No union of those dispositions with this unadopted new candidate is automatically authorized or asserted.

There is no unresolved internal step claimed in the conditional d=2 argument; independent reconstruction must still inspect each calculation and the exact import boundary. The first step needed for anything stronger is a separately gated demonstration that the named physical/local-H/count, carried-t, phase, profiles, residue and caps all apply to the *same* object at the proposed broader caller, together with a separately frozen union audit where appropriate. Original-source/printed identity, V, original selected-T/rank/eight-zero caller, other ranks or five-span branches, NL242, a positive witness, novelty, human review, cross-family review and kernel certification remain open or outside this return. S9 is a reported earlier local necessary-only run, not a finite verification of this uniform claim.

## 7. Input coverage and process

Before any body, I read the complete actual dispatch receipt (26 LF), manifest (273 LF), freeze receipt (254 LF), final binding (211 LF), live metadata supply (267 LF), and all 22 manifest-listed controls. Controls were used only for status and permissions; every genuine held episode and **all** proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. Administrative-file internal ordering was not mandated. I sent Main the direct PREBODY ACK naming the controls and the ordered 726-LF part, with no packet body or mathematical research/comparison before the ACK. Only thereafter I read the single part in strictly serial RAW windows 1–20, 21–40, ..., 701–720, 721–726 through its ending, including long lines, before researching this candidate. No unlisted scientific source, outgoing link, old code, sibling scientific return or held history was opened. The administrative/source pins below are **parent-supplied**, not independently rehashed, and are byte identifiers rather than correctness or clean-cognition certificates.

The entire rendered source set, in packet order, was:

| ID | Complete body, run-root-relative | LF | Parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `parent-boolean-even-E-common-slice-and-two-E-uniform-candidate-v1.md` | 25 | `18c308d0416d44d4811e1485f849272f4098da69545a378776a3206752579baf` |
| S2 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md` | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S3 | `parent-recovered-local-H-definition-and-general-g-foundation-v1.md` | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |
| S4 | `dispositions/info-6-entire-all-graph-D0-obstruction-and-two-E-residual-parent-v1.md` | 29 | `b8f74cc8316ce476cac0de23b82b626b99e1f526a54c1042cebbdd66c8a19c2e` |
| S5 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md` | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S6 | `dispositions/info-6-two-E-split-graph-D0-entire-common-y-obstruction-parent-v1.md` | 17 | `6d0e6e3bc961fed11d047928a0f32b10c8011debe5642fbe2a12971cfc22d062` |
| S7 | `review-waves/f789-boolean-two-E-one-double-graph-author/author-candidate-v1.md` | 200 | `db6343f98e598ffbe8c480175bbef6d3aeaac4f1b69766c360e5841121679dd5` |
| S8 | `review-waves/f788-boolean-two-E-one-plus-one-graph-author/author-candidate-v1.md` | 179 | `1c51df762a1878cae342b32b4a34fead49ca39c2813bdab41ba3e7a9ed3b737d` |
| S9 | `review-waves/f803-boolean-two-E-split-graph-finite-source-author/parent-split-v2-run-v1-receipt.json` | 142 | `9dfe7696d76b3b46f91bf8b4bbda9fd21540bb546320bb9364e7d09bab03dbb3` |

The sole packet's parent-supplied pin is `dda72dbf247a007ac66964ecb62625c370fc62d9aa16f10b7fb6483335450d3c`, 726 LF; the manifest pin is `c9deeb2be0313ff6d743fe16d3028ecddb737c0554fe703dfd42900e36b688e7`. The parent freeze and final binding report full-source roundtrip and matching bindings, respectively; this author has not independently recomputed them.

**NOT TESTED:** no child scientific execution, test, solver, compiler, CAS, external CLI, network, Git, install or deletion. No new source was assigned or supplied. The candidate requires a complete parent read and separate mathematical scrutiny; no test pass or adoption is implied.
