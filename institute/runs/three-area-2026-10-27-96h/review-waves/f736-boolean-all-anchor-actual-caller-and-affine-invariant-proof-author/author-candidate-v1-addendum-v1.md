# Additive source-foundation reconstruction: general g and explicit local H

**Prospective supplement, not a retroactive change to the original f736 return.** The original candidate's separate general F/E-table import and unverified-definition qualification accurately reflected the original frozen packet. After the later supplement, I reconstruct the general g table and its residue at the named normalized-caller scope, and identify the precise local H condition. The earlier file remains unchanged. The new source supports removing the **additional independent F/E-table import** from the earlier conditional consumer *when the named general normalization below is imported*: it does not remove the actual `H_local=0` hypothesis of the adopted location theorem, establish a printed-original-source equivalence, or assert that every putative caller satisfies the named imports without proof. Parent disposition remains separate.

## 1. The normalized g table is general at its exact import

Supplement S2 is the complete parent disposition for the named actual m=116, five-span, common two-fibre normalization. It supplies, for every caller at that normalization, physical coordinates `c=(h,d)`, `h=(h0,j)∈F₂×F₂²`, `d=(d0,d1,d2)∈F₂³`, a fixed support graph S, and

    g(h,0)=4 if h=(h0,0) with h0∈F₂;  g(h,0)=−2 otherwise;
    g(h,d_b)=ρ_b[−2+3·1_S(h,d_b)],   d_b=1+3b0+5b1;
    g=0 at the remaining 24 blocks,
    ρ_b=(−1)^{1+b0b1}.

Here the integers in the d-labels denote binary vectors and addition is XOR. This is not restricted to the explicit illustrative f and R. The normalization's own full named actual-caller hypotheses remain imports; the normalization is not itself an original balanced caller or a license to choose a new balance zero.

Set `ell=d0+d1+d2` and `b=(d1,d2)`. The map `d↦(ell,b)` is invertible. Its `ell=0,b=0` point is exactly d=0; its four `ell=1` points are exactly the d_b's in b-order, because `d_b=1+3b0+5b1`. The other three `ell=0` b-values correspond to the remaining 24 zero-g blocks. The full-block direction toggles h0, so use `h=h0` and retain j as the two-bit index. Supplement S2 makes the support a graph

    S={(ell,h,j,b): ell=1, h=f(j,b)}.

Consequently the **same** normalized g has the coordinate formula

    g(0,h,j,0)=4 if j=0, and −2 if j≠0;
    g(0,h,j,b)=0 if b≠0;
    g(1,f(j,b),j,b)=(-1)^{q(b)},
    g(1,f(j,b)+1,j,b)=−2(-1)^{q(b)},
    q(b)=1+b0b1.                                                  (1)

This proves the general F/E pattern used in §3.2 of my earlier candidate directly from the newly supplied named normalization. The signs and both h-entries belong to one physical g. If an otherwise admissible coordinate description translates the exceptional j-origin, the corresponding character phase must be carried; no such translation is needed in (1).

The earlier radical coordinates `z=(i,0)+k(b)`, `h'=h+d_f(b)` leave the physical b-coordinate unchanged. Since the radical lift and its derivative are linear, `k(0)=0` and `d_f(0)=0`; at b=0, `j=i` and `h'=h`. Thus (1)'s ell=0 physical table remains exactly the same in those coordinates. This observation does not identify the local invariant H below with the radical-lift plane, which is a different object.

## 2. General Fourier residue from the recovered table

Use the **unmodulated** common physical arrays, one phase R, and original normalized physical j,b coordinates. Write a full Fourier frequency as `(nu,s,beta,alpha)`, with characters `(-1)^{nu ell+s h+beta(j)+alpha(b)}`. Formula (1) gives the ell=0 term

    Σ_h (-1)^{s h}[4−2Σ_{j≠0}(-1)^{beta(j)}]
      = 1_{s=0}[12−16·1_{beta=0}].                              (2)

The ell=1 graph plus mate term is

    (−1)^nu [1−2(−1)^s] W_{q+s f}(beta,alpha).                   (3)

For s=0, q depends only on b; its two-bit Walsh coefficients have magnitude 2, and the j-sum is 0 or 4. Hence (3) is divisible by 8, while (2) is 4 modulo 8. For s=1, (2) vanishes and `f+q` is bent at this same named general normalization, so (3) is ±12. In both cases

    ghat(nu,s,beta,alpha) ≡ 4 (mod 8)  at all 64 frequencies.      (4)

The same normalization gives a graph sign `a=(-1)^R` and both R and R+f bent, hence every `ahat` is ±4 and `3 ahat+ghat≡0 (mod 8)`. With the single physical inverse

    4u(c,w)=x(c)+3a(c)χ1(w)+g(c)χ2(w)+y(c)χ3(w),
    χ3=χ1χ2,

and all `xhat≡0 (mod 8)`, take w=0 and Walsh transform. The ternary entries satisfy `u(c,0)≡1_{u(c,0)≠0} (mod 2)`, so their signed Fourier sum has parity

    J = #{c : u(c,0)≠0} mod 2.

Thus the **same** y obeys `yhat(ξ)≡4J (mod 8)` at every ξ. For the particular carried original-DC frequency t, `X=(-1)^t x` and `Y=(-1)^t y` translate those spectra by t; `Xhat(0)=xhat(t)=0`, and J=1 yields the `4+8Z` residue for Y. The phase R, f, x, y, u and t are not replaced by separately optimized objects. Neither a nor g is modulated in the physical inverse merely because the analysis introduces X and Y.

Therefore, at the named general normalized-caller imports, there is no need to import (1) or (4) a second time as an unestablished example-specific assumption. This is an additive reconstruction against the new supplement; it is not a claim that the original f736 packet had included S2.

## 3. What local H means, and what it does not mean

Supplement S3 gives the explicit definition: `H_local` is the **number of blocks with U1=0 whose four-component local Walsh spectrum has a single |U0|=4 peak**. The condition is `H_local=0`. This H is not the physical radical-lift plane H or the symbol used for that plane's dimension. It also does not silently identify any undisplayed historical class table or source atom.

For a ternary four-point block, the definition has a direct check. If `|U0|=4`, all four ternary entries have the same sign, so the other three local Walsh coefficients vanish and in particular U1=0. Conversely a block counted by H_local has such an |U0|=4 peak. Thus, for a genuinely ternary common inverse,

    H_local=0  iff  no physical block has |x(c)|=4.                (5)

The point is not that a pure y-array or an arbitrary assignment automatically has a ternary inverse. Nor is H_local=0 by itself a U0 or U3 *global* Walsh cap.

### 3.1 Written reconstruction of local types and the census

The available selected S4 excerpt displays the entire local parametrization. Here is the short calculation. At any block with U1=0, local Parseval gives `x²+g²+y²=4 Σ_w u(w)²≤16`. All three coefficients are even: mod 2 every local character is 1, and U1=0. For integral `u=(x+gχ2+yχ3)/4`, the number of coefficients among x,g,y congruent to 2 modulo 4 must be even. Therefore the only possible local spectra are zero; two signed ±2 entries; or one signed ±4 peak. For g=±4 the other entries vanish. For |g|=2 exactly one of x,y is ±2 and the other zero. For g=0 the possible pairs are `(0,0)`, `(±2,±2)`, `(±4,0)`, `(0,±4)`. By (5), H_local=0 removes exactly `(±4,0)`.

On S, U1=3a=±3 forces exactly three nonzero ternary entries, each contributing the same sign to U1. Deleting the single zero entry from the full four-point character table gives `x=±1` and `y=−agx`, as well as the already normalized `g=±1`. On the two full F blocks g=4 forces x=y=0. Thus the complete H_local=0 choices agree with S4:

    D0: (x,y)=(±2,0);     D3: (x,y)=(0,±2);
    Z0: (x,y)=(0,0);      Z2: (x,y)=(±2,±2);
    Z4: (x,y)=(0,±4).

For example, with `g=2δ`, δ=±1, a D0 block has `u=(ε+δχ2)/2`, and a D3 block has `u=χ2(δ+ζχ1)/2`; the Z2 and Z4 inverses are `(ε+ηχ3)/2` and `κχ3`. All entries are ternary. This checks the direct local converse for these types; it does not give global cap compatibility.

Write `d=|D0|`, `p=|Z2|`, `z=|Z4|`, keeping z distinct from the carried balance frequency t. The 16 S blocks have support 3 each, the two F blocks support 4 each, and all 22 D blocks support 2 each. Hence support116 gives

    48+8+44+2p+4z=116,  i.e.  p+2z=8.

The same x has energy `16+4(d+p)=56`, so `d+p=10`. Its companion y has `2+d+(24−p−z)=20+3z` zero blocks. The named zero count 23 yields

    z=1, p=6, d=4; |D3|=18 and |Z0|=17.                         (6)

Conversely the displayed local types with (6) have support116, x-energy56, y-energy128, 23 y-zeros, and H_local=0; a single common inverse realizes their prescribed local signs. This is precisely an explicit local/count converse, not a construction of one object satisfying every spatial or spectral condition in the broader problem.

### 3.2 The two previously displayed x fixtures

For both the original fixed x and the separately sheared x' in the original f736 packet, the actual displayed local values are graph ±1, D0/Z2 values ±2 and zero elsewhere; multiplying by the given `(-1)^t` changes signs but not magnitudes. In each source's stated ternary inverse, no |U0|=4 block occurs. Equation (5) therefore gives `H_local=0` for those two specific physical constructions for every carried t. This is a **new written identification** from the newly supplied definition; it is not a claim that historical f710/f719/f727 finite checks explicitly measured H_local. Neither displayed y satisfies the all-U3 caps merely because H_local=0, and no V or full caller is obtained.

## 4. Consequence and exact remaining boundary

Subject to independent checking of my original all-anchor signed-array proof and the adopted S4 actual-location import, the physical implication in that proof can now cite the general recovered normalization (1)–(4), rather than requiring an extra F/E pattern assumed only from the example. The local-H premise is now **identified**, and it is directly checked for the two displayed local x fixtures; it is not a general proof that an arbitrary caller has H_local=0. The consumer remains restricted to the SAME physical f,R,x,y, the actual specifically carried t, J=1 and the one-D0-per-graph-L-coset subfamily, with all required U0 and U3 caps/divisibilities. It does not assume an unproved signed-location iff, cover other D0 allocations, construct V, restore original T, establish source identity or close NL242.

No claim in this addendum retroactively changes the exposure, proof status or tested scope of the prior return or historical finite runs. A direct parent read, independent review and separate disposition are required.

## 5. Exact supplement coverage and process

I first completed and returned the original f736 458-LF packet reconstruction. For this new supplement I read the complete manifest, freeze receipt, final binding, prepared metadata, actual dispatch and all **22** controls through their endings, then sent a direct SUPPLEMENT PREBODY ACK to Main. Controls were used only for status/permissions. After that ACK I read the only part in strictly ascending serial raw windows of at most 20 LF, all 219 LF through its ending, before using its mathematical content. Source coverage and parent-bound SHA-256 values:

| ID | Actual supplement coverage | Source binding | Selected-range SHA-256, if partial |
|---|---|---|---|
| S1 | complete LF 1–13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` | — |
| S2 | complete LF 1–38 | `443d0a1a94384e237076cb7974b49845e6fa52edf3ca83f161259e79a369de1e` | — |
| S3 | only LF 39–80 of f483 | `a87070e93236c417f0b6d9c04ad6d9ebefd90342f6ce9a6e87a54d4e5d3dca36` | `bb5c8ce088d9f0c67999079ad6abf4a69c040ebffb757888cd69bdfcdb2e9de2` |
| S4 | only LF 191–243 of that same f483 | `a87070e93236c417f0b6d9c04ad6d9ebefd90342f6ce9a6e87a54d4e5d3dca36` | `4a7f7267c1605decc029d3694d46d20f18e07017d3cb52e427629986d0fd11e8` |
| S5 | complete LF 1–51 | `fc7169410a6540a6d63ea033720a90207fd49e89e4cc048d9eb208639eb65e5c` | — |

I did **not** read the omitted f483 body, follow outgoing links, open a held history, inspect old code or read unspecified sibling outputs. Source SHA values and selected hashes above are parent-supplied bindings, not child rehashes of the source paths. My direct metadata hashes: manifest `952e56e2484d3074e5e6630cae29fdece4b37550c817fd6b6f298e127c27be18`; freeze `c1a578e9e4f5878231d1570fb62376be5ca636efadb8f7c0467112cdc9b21aaf`; final binding `d0874361b1da9e53de0a5eab32b6c49d8fb950c743cd5454b96c9f597bb29542`; prepared metadata `ce00ebb8ba62129d56f0e50b6e4afe8458865cfa8143435abfde00dfffa877dc`; actual dispatch `75527bc6da2f81f6681b68bede1864b30ad3dae992ec0dd7eb5d04b572d94957`; packet `52831db2b5af020c8b38bc50e2d8662b8f6b11e293d5c4bd8255d62bcc16d8ff`.

The f483 local-only prebody-ACK transport fault is disclosed in S1/S5 and not rewritten; no conclusion about compliance is backdated. All genuine held episodes and ALL proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. **CHILD SCIENTIFIC EXECUTION NOT RUN:** no solver, CAS, finite program, test, build, linter, formatter or scientific calculation tool. This is nonblind same-harness written reconstruction, not human, external-family, kernel, original-source-identity, novelty or parent acceptance. Metadata hashing and this exclusive create are not scientific verification. Native clock observed during work: `2026-10-30T17:17:34-0700 PDT`, not a creation timestamp.
