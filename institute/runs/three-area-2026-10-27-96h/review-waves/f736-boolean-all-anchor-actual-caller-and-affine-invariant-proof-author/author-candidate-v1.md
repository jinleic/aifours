# All-anchor partial-Parseval obstruction and the actual-caller bridge

**Status: nonblind GENERAL AUTHOR written reconstruction, not a disposition.** The signed-array theorem in §2 is proved below for arbitrary actual anchor arrays, including nonaffine ones, and all four possible graph covectors. Section 3 gives a conditional consumer for one and the same physical object and the specifically supplied balance frequency. It explicitly exposes both the adopted-location imports and the physical F/E spectrum import; it does not establish the separately named `H_local=0` condition or its definition. No finite program was run or prepared. Parent review and disposition are separate.

## 1. Statement of the pure-array theorem

All indices and characters below are over F₂. Let `I=B=F₂²`, identify `B*` with F₂² in the displayed basis, and define `Q(v0,v1)=(v1,v0)`. Let `F:I→F₂` have XOR of its four values equal to 1. For each `i` let `b_i∈B`, `κ_i∈B*`, `σ_i∈{±1}`, set `v=⊕_i b_i`, and write `g_i(b)=σ_i(-1)^{κ_i(b)}`. Assume only the anchor/covector relation

    ⊕_i κ_i = Qv.                                                (1)

One real array `Y` on all 64 sites `(ell,h,i,b)` has, simultaneously:

* `Y(1,F(i),i,b)=g_i(b)`; `Y(1,F(i)+1,i,b_i)=0`; and `Y(1,F(i)+1,i,b)=2 d_{i,b}` for `b≠b_i`, with twelve fixed signs `d_{i,b}`.
* At `ell=0,b=0`, for each i the two h-values are either both zero or both in `{−2,+2}`. At `ell=0,b≠0` there are six magnitude-2 sites, one different magnitude-4 site, and zeros otherwise. The six magnitude-2 sites occupy exactly three distinct `(h,i)` cells, two distinct b-sites in each.
* `ΣY²=128`, and every unnormalized 64-point Walsh coefficient lies in `4+8Z`.

**Claim.** These conditions preclude all 64 Walsh magnitudes being at most 12. The quantifiers include every `F` of odd parity, every anchor array (not only affine ones), every ordered four-tuple of κ satisfying (1), all signs and every allowed magnitude-4 site. The constraints apply to a single array; no frequency-dependent selection is allowed. No local-H premise is used in this theorem.

## 2. Written proof of the pure-array claim

For `s∈F₂`, `α∈B*`, `β∈I*`, set

    A_l(s,α,β) = Σ_{h,i,b} Y(l,h,i,b)(−1)^{s h+β(i)+α(b)}.

The two full coefficients at this triple are `A_0+A_1` and `A_0−A_1`. Their two bounds are equivalent to `|A_0|+|A_1|≤12`. Let `n∈F₂` be the parity of the number of negative mate signs and let `m_α=#{i:κ_i=α}`. The graph contributes `4m_α (mod 8)` to `A_1`. Among the twelve mate terms the product of signs, including their characters, is `(-1)^{n+s+α(v)}`: the sums of `3(F(i)+1)`, `3i`, and of the three non-anchor b's over each row are respectively 1, 0, and v. Since the twelve signed terms each have magnitude 2, their sum is `4(n+s+α(v)) (mod 8)`. Consequently

    A_1/4 ≡ n+s+m_α+α(v)  (mod 2).                              (2)

Here `A_1` is a multiple of 4. Because both full coefficients are 4 modulo 8, `A_0` is also a multiple of 4 and `A_0/4`, `A_1/4` have opposite parity.

The parity `τ_α=m_α+α(v)` is in fact independent of α. For a four-point Boolean function, even XOR of its values is exactly affineness. Thus `p(α)=m_α mod 2` has the form `τ+α(w)`, since `⊕_α p(α)=4 mod 2=0`. Directly summing `α p(α)` over the four α gives `Qw`. But this same sum is `⊕_i κ_i=Qv`; hence `w=v` and `τ_α=τ`. This derivation uses (1), not an affine-anchor change of variables.

Assume all caps. Put `s_0=n+τ`, `s_1=s_0+1`. On slice `s_0`, (2) gives `A_1∈{0,±8}`; on slice `s_1`, it gives `A_1∈{±4,±12}`. Full Parseval gives `Σ_ξ W(ξ)²=64·128`. The capped `4+8Z` coefficients have magnitude 4 or 12, so exactly eight of the 64 have magnitude 4.

Let E count triples `(s_0,α,β)` with `|A_1|=8`, and O count triples `(s_1,α,β)` with `|A_1|=4`. At an E triple the other parity and the pair cap force `|A_0|=4`, hence one of its two full coefficients has magnitude 4. At an O triple, `A_0=0` or `±8`, so at least one of its two full coefficients has magnitude 4. Different triples give disjoint frequency pairs. Therefore

    E+O ≤ 8.                                                       (3)

The ell=1 energy is `16+12·4=64`. Five-bit Parseval, divided by 16, gives

    4E + O + 9(16−O) = 32·64/16 = 128,
    O = 2+E/2.                                                     (4)

Equations (3)–(4) imply `E≤4`. On the other hand, with

    C = Σ_{i,b≠b_i} g_i(b)d_{i,b},

transform first in h and then apply Parseval in `(i,b)`. The graph/mate cross term gives, for either s,

    Σ_{α,β}(A_1(s,α,β)/4)² = 64+4(−1)^s C.                       (5)

At `s=s_0` the left side is `4E`, so `E=16+(−1)^{s_0}C≥4`. Equality holds, and since C is a sum of twelve signs it forces, at every actual mate site,

    d_{i,b}=−(−1)^{s_0}g_i(b).                                   (6)

It also gives `E=4` and `O=4`. At the opposite h-frequency `s_1`, put `w_i=σ_i(−1)^{s_1F(i)}`. The actual h-transformed row is `w_i(-1)^{κ_i(b)}(3−2·1_{b=b_i})`; therefore

    A_1(s_1,α,β) = Σ_i (−1)^{β(i)}w_i
                      [12·1_{α=κ_i}−2(−1)^{(κ_i+α)(b_i)}].       (7)

If some κ occurs twice, choose β so its two active `w_i(-1)^{β(i)}` signs agree; this is possible for two distinct i. The two active brackets are 10 and the other two terms have total magnitude at most 4, so `|A_1|≥16`. If a κ occurs three times, the two differences among those three distinct points of I are independent, so some β aligns the three active signs and `|A_1|≥30−2=28`. If all four κ are equal, every bracket is 10; four-point Parseval ensures some β has a signed row sum of magnitude at least 2, giving `|A_1|≥20`. Each alternative violates the necessary `|A_1|≤12`. Thus all four κ are distinct.

Their XOR is zero. Equation (1) and invertibility of Q give `v=0`; consequently the actual anchor map is affine, because a two-bit-valued function on I is affine precisely when the XOR of its four values is zero. This conclusion is *derived after* applying the simultaneous caps. In particular, nonaffine actual anchor arrays were included up to this point and are ruled out by the repeated-κ argument, rather than silently aligned.

Now, and only now, set `b'=b+b_i`. This is an invertible affine change of the full coordinates preserving `ell,h,i`, the physical h-mate vector, all full-spectrum caps and residues, and the common array. It merely permutes the twelve d signs, so n is unchanged. Denote the transported graph scalars by `σ'_i`. Since every κ is now unique, `τ=1`, `s_0=n+1`, `s_1=n`. Multiply (6) over all twelve nonzero b' sites. The product of each character over the three nonzero elements of B is +1, so

    ∏_i σ'_i = (−1)^n,
    ∏_i w'_i = ∏_i [σ'_i(−1)^{nF(i)}] = +1.                      (8)

Every four-sign function with product +1 is a constant sign times a unique character `(-1)^{β_0(i)}`. With `i(α)` the unique row with `κ_i=α`, (7) reduces to

    A_1(n,α,β)=12 w'_{i(α)}(−1)^{β(i(α))}
               −2 Σ_i w'_i(−1)^{β(i)}.                           (9)

For every α the magnitude is 4 at `β_0` and 12 at the other three β. The paired full caps therefore force

    A_0(n,α,β)=0  for every α and every β≠β_0.                    (10)

Define `B_i(b')=Y'(0,0,i,b')+(−1)^nY'(0,1,i,b')`. Inverting the b' transform in (10), and then the i transform, gives

    B_i(b')=(−1)^{β_0(i)}B_0(b')  for all i,b'.                   (11)

The six magnitude-2 sites outside physical b=0 occupy only three `(h,i)` cells and thus at most three i-rows. Choose one i-row with no such site. In that row every `B_i(b')` is 0 or has magnitude 4: at shifted physical b=0 it is the sum/difference of two zero or two magnitude-2 entries, and at other b it is zero except possibly for the unique magnitude-4 site. Equation (11) implies this same `0 or 4` magnitude restriction for every row at every b'.

If any physical b≠0 magnitude-2 site lacked another magnitude-2 site at the same i,b and opposite h, its opposite entry would be 0 or ±4. Its h-sum would then have magnitude 2 or 6, contradicting (11). Thus every such site is paired across h at the same i,b. Every occupied `(h,i)` cell has its opposite-h cell occupied too; the occupied cells occur in pairs. This contradicts the stipulated number three and proves the pure-array theorem. All h-pairing here is of the same transported array; the coordinate shift depends only on i and so does not change which two sites are physical mates.

## 3. Actual normalization and the conditional consumer

The following are imports, not conclusions manufactured by choosing frequencies separately. Take the same physical m=116 five-span inverse and rank-two quadratic f, `q(b)=1+b0b1`, a common Boolean phase R with R and R+f bent, and bent f+q. On the graph `S={(1,f(z),z)}` the same arrays obey `a=(-1)^R`, `g=(-1)^q`, `y=−agx`; on the graph mates `g=−2(-1)^q`. The U0 coefficients of the same x are divisible by 8, obey all 64 caps ≤8, and vanish at the **specified original-DC transport t**. Use the actual four-D0 subfamily with one actual D0 per graph L-coset, all the physical local forms/counts and the S4/S5 named local-H import. The following calculation also makes explicit the F/E form used in S2's residue argument:

    g(0,h,j,b)=0 for b≠0;
    g(0,h,j,0)=4 for one fixed j=j_F, and −2 for the other three j,

independently of h. A translation of the j origin can make `j_F=0`. The literal packet displays this F/E g table for S3's canonical physical example and uses its Fourier consequence in S2's general argument; S4/S5 summarize the actual normalization and counts but do not independently spell out this entire table. Accordingly the general F/E table, or equivalently its spectrum used below, is an **explicit physical-normalization import** of this consumer, not a separately established identity of the printed original caller. This qualification is additional to, not a replacement for, the unverified `H_local=0` boundary. The pure-array theorem does not need either import.

### 3.1 Radical lift and intrinsic graph characters

Let `K=rad(B_f)`. The projection `K→B`, `k↦b(k)`, is an isomorphism. One way to see injectivity from the named inputs is that if a nonzero radical vector has b=0, then the derivatives of both f and q in that direction are constant, contradicting bentness of f+q (all nonzero derivatives of a bent function are balanced). Both spaces have dimension two. Let k(b) be its unique inverse lift. The physical radical lift is

    H(b)=(ell=0, h=d(b), z=k(b)),
    d(b)=f(z+k(b))+f(z),

where d is linear and independent of z. Write `z=(i,0)+k(b)` and `h'=h+d(b)`. These are one invertible linear coordinate change, not a change of physical f or an independently chosen object. Then

    f((i,0)+k(b)) = F(i)+d(b),  F(i)=f(i,0),
    graph: h'=F(i),    ⊕_i F(i)=1.

The complement to K has nondegenerate rank-two polarization; equivalently the coefficient of `i0 i1` in F is 1, so its four values have odd XOR.

Set `R_i(b)=R((i,0)+k(b))` and `V_i(α)=Σ_b(-1)^{R_i(b)+α(b)}`. Bentness of R makes all four i-Walsh transforms of the vector `V(α)` have magnitude 4, hence `Σ_i V_i(α)²=16`. Bentness of R+f, evaluated at the *shifted* b-covector `α+d`, makes all four i-Walsh transforms of `((-1)^{F(i)}V_i(α))_i` also have magnitude 4. A two-bit Boolean row has either one Walsh value ±4 and three zeros, or four Walsh values ±2. If any row were nonaffine, then at every α its contribution has magnitude 2; the energy 16 forbids any ±4 contribution and forces all four entries to have magnitude 2. The flat i-transform of four signs requires their product to be −1; multiplying by the odd-parity F signs reverses that product, contradicting the other flat transform. Thus every `R_i` is affine. The same energy identity shows each α occurs exactly once as its row-linear part `λ_i`; every bijection of the four points of F₂² is affine, so `i→λ_i` is affine.

Use the physical actual D0 anchor b_i, its actual graph mate in the same i-row, and the actual exceptional displacement Δ_i from that mate. S4 gives the necessary affine map `i→Δ_i` in *both* its 1+1+1 and 2+1 location alternatives, as well as the three physical `ell=0` H-cells carrying two Z2 sites each. These conclusions are conditional on S4's actual imports and do not give a signed-location iff. Put `γ_i=b_i+Δ_i` and use `X(c)=(-1)^{t(c)}x(c)`. S4 supplies the one weighted graph pattern

    X(1,F(i),i,b)=ε_i(2·1_{b=γ_i}−1).

For the same `Y=(-1)^t y`, the physical equation gives `Y=−agX` on the graph. The two quadratic terms in `(-1)^{b0b1}` and in the exceptional-point sign cancel. Expanding

    1_{b=γ}=(1+b0+γ0)(1+b1+γ1)   in F₂

gives an affine graph row with linear covector

    κ_i=λ_i+(1,1)+Qγ_i.                                           (12)

All other row dependence is an actual scalar sign σ_i. Since both λ and Δ are affine, their four-value XORs vanish. Summing (12) gives precisely `⊕κ_i=Q(⊕b_i)`, i.e. (1), without an affine-anchor assumption. The actual graph mates are four zeros at the b_i and twelve ±2 values at the other b. On `ell=0,b=0` the two values in a row are both zero or both ±2. Off that physical b, the actual six Z2 sites lie in the three distinct H-cells just named, together with a distinct Z4 site and zeros. In `(h',i,b)` those H-cells are exactly the three cells of the pure-array claim. The local physical count gives `ΣY²=16+12·4+6·4+6·4+16=128`.

### 3.2 The residue and the *specific* carried t

It remains to derive residues from the same inverse rather than assert them. In original physical `(j,b)` coordinates, write a full frequency as `(ν,s,β,α)`. Since R and R+f are bent,

    ahat(ν,s,β,α)=(-1)^ν · W_{R+s f}(β,α) ≡ 4 (mod 8).

The graph plus graph-mate contribution to ghat is

    (−1)^ν [1−2(−1)^s] · W_{q+s f}(β,α).                         (13)

For s=0, q depends only on b and its two-bit Walsh coefficients are ±2. Hence (13) is 0 or ±8. The imported F/E form gives the `ell=0` contribution `12(-1)^{β(j_F)}−16·1_{β=0}`, always 4 modulo 8. For s=1 that ell=0 contribution vanishes, while bentness of f+q makes (13) ±12, again 4 modulo 8. Therefore `ghat≡4 (mod 8)` at every physical frequency, and `3 ahat+ghat≡0 (mod 8)`.

At w=0 the *unmodulated physical inverse* is `4u=x+3a+g+y`. Because u is ternary, its signed Fourier sum is congruent modulo 2 to the number of its nonzero entries. Thus, for `J=#{c:u(c,0)≠0} mod 2`,

    yhat(ξ)≡4J  (mod 8)  for every ξ,                             (14)

using the actual U0 divisibility `xhat≡0`. This derivation does **not** say the entire inverse or a,g were multiplied by `(-1)^t`. For the actual specified t only, multiplying both x and y by its character translates their spectra: `Xhat(ξ)=xhat(ξ+t)`, `Yhat(ξ)=yhat(ξ+t)`. The same X has the stipulated zero at 0 because `xhat(t)=0`, and the same Y has residue 4 mod 8 if J=1. The residue, all U3 caps, graph relation and all site counts refer to that one X,Y. The pure-array theorem then excludes simultaneous J=1 and all 64 U3 caps ≤12 within these explicit actual-caller imports and this one-per-L-coset four-D0 subfamily.

This is a written conditional implication, not an assertion that any original caller exists, that S4's assumptions are automatic, or that the separately named `H_local=0` definition has been inspected. In particular, the packet does not by itself establish that the additional F/E table above follows from S4/S5's summaries or from the printed original problem; the implication may instead import the derived property `ghat≡4 (mod 8)` explicitly. S2 is an unadopted candidate, not independent evidence of its own source identity.

## 4. Full affine alignment, mate direction and invariant

Every two-bit-valued anchor array can be written uniquely

    b_i=B i+c+vF(i),     v=⊕_i b_i,

because `1,i0,i1,F(i)` is a basis of all four-point Boolean functions. The full-space affine shear

    b' = b+B i+c+v(h'+1),      ell,h',i unchanged                 (15)

is invertible. At every D0 anchor `(h',b)=(F(i)+1,b_i)` it gives b'=0. But its paired graph mate has b'=v, and the physical mate direction e is sent to `(Δh',Δb')=(1,v)`. Hence the unqualified assertion that a nonaffine array cannot be aligned by **any** affine map is false; the narrower assertion that `b'=b+b_i` with h' fixed is nonaffine when v≠0 is correct. The shear does not restore the old same-b mate interface. In the proof above the e-preserving alignment is used only *after* the cap assumptions imply v=0.

There is a full ambient-affine invariant for the precise standard form. In the radical coordinates `D_i=(1,F(i)+1,i,b_i)`, so

    ⊕_i D_i = e+H(v),       (⊕_i D_i)+e=H(v).                    (16)

For any invertible affine `P(c)=Mc+a`, the four-point XOR becomes `M(⊕D_i)` and the physical mate vector becomes Me; the defect becomes `MH(v)`. It is nonzero when v≠0. In the particular standard form with common D0 b=0, their physical graph mates also b=0, and odd graph F, the corresponding defect is zero. Therefore no ambient affine transformation takes a v≠0 object to *that particular* standard form while carrying the physical mate direction. This invariant does not exclude other normal forms and is not substituted for the all-anchor proof.

Under any such P all physical arrays, including `u,a,g,x,y`, must be pulled back together. The full Walsh transform obeys

    W_{A∘P^{-1}}(ξ') = (−1)^{ξ'(a)} W_A(M^Tξ').

The specified t is carried as `t'=M^{-T}t` with the affine modulation phase `t(P^{-1}c')`; the possible constant phase is retained. Common point permutations preserve J, and the sign in the Walsh formula preserves magnitude, divisibility by 8, and the residue class 4 mod 8. This does not authorize leaving a,g fixed during a coordinate transform or selecting a new balance zero.

## 5. Input coverage, exact limits and provenance

Before body access I read the complete manifest, freeze receipt, final binding, prepared metadata, actual dispatch receipt and all **23** listed controls through their endings, then sent Main a direct PREBODY ACK with that count. Controls were permissions/status only. After the ACK I read the sole packet in strictly ascending serial raw windows of at most 20 LF, all 458 LF through its ending, before mathematical comparison or research. Parent-bound input bodies were all complete, not partial:

| Packet ID | Complete LF | Parent-supplied whole-source SHA-256 | Role |
|---|---:|---|---|
| S1 | 1–7 | `a1eb0a70820eb9105a043fc22da1bcf9830b5daaa852fdcc5e84244d4d50b894` | Parent mate-direction clarification |
| S2 | 1–139 | `63cc4fa48e0dececec9a381b32ca75191eec31e22e2cb3fb4907d7275437e890` | Unadopted f726 all-anchor candidate |
| S3 | 1–173 | `a7deb23a7bf26185d8f9b3cb54c0fe79716bcbac739011ec59453f062cdd18d7` | Unadopted f725 physical illustration and alignment repair |
| S4 | 1–30 | `fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a` | Adopted conditional actual-location import |
| S5 | 1–37 | `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a` | Adopted conditional rank-two profile/import |
| S6 | 1–31 | `3e77eebe5c885ae8b53e04b76f3de46594c5cca2e5647086122bf408fa7052b4` | Prior even-κ larger-class lemma and one fixed-x consumer, not a general distinct-κ premise |
| S7 | 1–11 | `2253ac97d0b148dfc96406235658b5712c47c6014aecf65befe26e8f20d700ab` | Parent f718 nonaffine-alignment correction |

These source hashes are the parent bindings; the source bodies were consumed only through the frozen packet, not reopened or separately rehashed. My direct metadata hashes were manifest `7fa950aa06548fda3fac53260932f81b51f4d5af1cbc344bd6db0b161e7eb306`; freeze `7d4e23c6a4d31371d448f328991d948da2496ff98fa00ad92b4e6797e522cbc1`; final binding `9a76b2c1ca913d379a61fdcffc158dd3beb956c20b96e4d5bf3638ed0d93753d`; prepared metadata `4993d851b1fb193c823283ce236d2ff5c02d8889fcec19ac301d552dea01ad5f`; actual dispatch `6f67e86a1debdb40f7e43330b6e842e3168212728dec8876f6758f7003df50b2`; packet `dfb064b343667081a530c794969050967e732883c5adbfbf185e899e6d9c2087`.

I independently reconstructed the displayed implications; this is not a claim of blindness to S2/S3, or independent-family, human, kernel, original-source-identity, or novelty verification. The known f718 broad affine-alignment error is corrected in §4 without claiming an all-U3 witness; its mate-direction qualification is retained. No additional mathematical fault in S2's pure-array derivation is asserted here. The explicit general F/E spectral assumption above and the absent separate H_local definition are load-bearing consumer boundaries, not proofs of failure of either assumption. No all-D0-allocation conclusion, signed-location iff, common V, original T/V restoration, or global NL242 closure is claimed. All genuine held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers were NONINPUT; no held history, outgoing source link, old code or unspecified sibling artifact was opened. **CHILD SCIENTIFIC EXECUTION NOT RUN:** no solver, CAS, finite program, scientific calculation tool, test, build, linter, or formatter. Metadata hashing and this exclusive-create write are not scientific verification. Native clock observed during work was `2026-10-30T17:12:21-0700 PDT`, not a claim of artifact creation time.
