# F868 author candidate: actual-factor prime fibres, original gcd spectra, and the small-gcd boundary

**Status.** This is a prospective GENERAL AUTHOR written candidate, not a parent disposition, independent review, formal verification, or a claim of novelty. All tilings and factors below are the actual original objects. The main conclusions are: the prime-fibre dichotomy and exclusion of every prime original gcd; an independently written exclusion of all original gcds at most 17; and an exact spectrum-separation characterization for a complete cyclic direct tiling. The last result yields sign-aware necessary tests and infinite composite-gcd exclusion families. None says that an actual head factor exists or that all anchored tilings are impossible.

## 1. Actual objects and exact weighted projection

Let `n>14`, and let nonempty subsets `P,Q` of `Z_n` satisfy

\[
P\oplus Q=\mathbb Z_n,\quad A=\{0,3,8,11\}\subseteq P,\quad S=\{0,1,7,13,14\}\subseteq Q,
\]

where `⊕` means every element has exactly one **ordered** representation. In addition, assume as a separate hypothesis an actual direct factorization of the original head

\[
P=\{u,u+d_0\}\oplus C_0,\qquad d_0\not\equiv0\pmod n.
\]

Absorb `u` into `C_0`. The unique representation of the actual element `0` either puts `0` in that factor, or puts `-d_0` in it. In the latter case replace the difference by `-d_0` and translate the factor by `d_0`. Thus, without changing `P,Q` or the gcd, fix an orientation

\[
P=\{0,d\}\oplus C,\quad 0\in C,\quad g=\gcd(n,d)=\gcd(n,d_0).
\tag{1}
\]

Here and throughout a gcd with a residue means the gcd with any integer representative. There is no assertion that either orientation is the one originally specified by `d_0`.

Associativity and uniqueness make `T=C⊕Q` an actual subset and give

\[
1_T(x)+1_T(x-d)=1\quad(x\in\mathbb Z_n).
\]

Each cycle of addition by `d` has length `n/g`; alternating around it shows `n/g` is even. Consequently `2g|n`, `d/g` is odd, and `gcd(2d,n)=2g`. Alternation also makes `T` invariant under `2d`, so it is the full inverse image of a selector `V⊂Z_{2g}`: `|V|=g`, and exactly one of `s,s+g` belongs to `V` for every `s mod g`. Put `L=n/(2g)`. For the **original element counts**

\[
c_i=|\{c\in C:c\equiv i\pmod{2g}\}|,\qquad
q_j=|\{q\in Q:q\equiv j\pmod{2g}\}|,
\]

counting the uniquely represented original elements in each full fibre yields

\[
\sum_{i\in\mathbb Z_{2g}}c_iq_{s-i}=L\,1_V(s)\quad(s\in\mathbb Z_{2g}).\tag{2}
\]

In particular `c_0>0`; the projections of all five tail anchors lie in `V`; if `c_i>0` then `i+S⊂V`; and if `q_j>0` then `j+supp(c)⊂V`. An anchor `a∈A` has its actual representative in `C` at residue `a` or `a−g` modulo `2g`, since `d≡g mod 2g`. If these two choices are equal as *original* elements, that would contradict `d≠0`; equality modulo a smaller quotient alone is not a collision. The anchors do not themselves imply the direct factorization (1).

## 2. Prime-divisor weighted fibres and all prime gcds

**Theorem 1.** For every prime `p|g`, at least one of the two original-element count functions

\[
r\mapsto |\{c\in C:c\equiv r\pmod p\}|,\qquad
r\mapsto |\{q\in Q:q\equiv r\pmod p\}|
\]

is a positive constant on `Z_p`. The choice may depend on `p`. Moreover `g` is not prime.

**Proof.** Put `α_r=c_r+c_{r+g}` and `β_r=q_r+q_{r+g}` for `r mod g`. Summing (2) over the two residues above each `r` gives `α*β=L` on `Z_g`, because `V` is a selector. Further summing over fibres of `Z_g→Z_p` gives

\[
F_p*G_p=Lg/p\quad\text{on }\mathbb Z_p,\tag{3}
\]

where `F_p,G_p` are precisely the stated original-element profiles. This projection does not assert that either support is a quotient tile. At a primitive `p`th root `ζ`, the profile polynomials `F(X),G(X)` of degree at most `p−1` satisfy `F(ζ)G(ζ)=0`. The minimal polynomial is `Φ_p=1+X+⋯+X^{p−1}`: `Φ_p(X+1)` is Eisenstein at `p`. Thus one polynomial is a scalar multiple of `Φ_p`, and all its coefficients are equal. Its total is a positive original cardinality, so that common value is positive. This includes `p=2`.

Now suppose `g=p` is prime. If the `C` profile is constant, it has a representative in every class modulo `p`. Since `q_0>0`, `supp(c)⊂V`; since `V` contains exactly one element from each antipodal pair, these representatives force `supp(c)=V`. But `q_1>0` then gives `V+1⊂V`, hence `V+1=V`, impossible for a nonempty proper subset of the cyclic group `Z_{2p}`.

If the `Q` profile is constant, the same argument using `c_0>0` gives `supp(q)=V`. Choose an anchor `a` coprime to `p`: use `a=3` for `p≠3` and `a=8` for `p=3`. Its actual positive `C` residue `i` is congruent to `a` modulo `p`; hence `gcd(i,2p)` is 1 or 2. From `i+V⊂V` obtain `i+V=V`. In the first case translation by `i` generates all `Z_{2p}`, forcing `V` to be the whole group. In the second it generates the even subgroup, so `V` is a union of parity classes; because `0,1∈V`, both classes occur, again forcing the whole group. Both contradict `|V|=p`. This proves the theorem. ∎

**Explicit `p=2,3` boundaries.** At `g=2`, the tail anchors `0,14` project to antipodes `0,2 mod 4`, already contradicting the selector; so do `1,7`. At `g=3`, the projected tail is exactly `{0,1,2} mod 6`, hence is all of `V`. Its only translation stabilizer is zero, so every positive `c_i` has `i=0 mod 6`; but the anchor `8` requires a positive residue `2` or `5`. These direct checks agree with the prime argument, rather than treating either small prime as an exception.

## 3. Independent weighted exclusion through gcd 17

The following supplements, rather than imports, the packet's prior small-gcd disposition: the written support and coefficient arguments below derive the needed cases directly from (2). In each support list, omissions are forbidden by `i+S⊂V` or by `j+F⊂V` for the displayed forced set `F`; positive coefficients and all omitted nonnegative terms retain their original multiplicities.

First, `g=1,4,6,12,14` are impossible because a tail-anchor difference is an odd multiple of `g`: respectively use differences `1,12,6,12,14`. Such a pair would occupy both members of a selector pair. Prime `g≤17` is already excluded by Theorem 1.

### 3.1. The three cases `g=8,9,10`

* `g=8`, modulo 16. The anchor `3` cannot use `c_11`, since `11+13=8` is opposite `0`; hence `c_3>0`. The forced union `S∪(3+S)` is exactly
  \[V=\{0,1,3,4,7,10,13,14\},\]
  one member of each pair. Directly checking `i+S⊂V` and `j+{0,3}⊂V` yields
  \[\operatorname{supp}c=\{0,3\},\quad
  \operatorname{supp}q\subseteq\{0,1,4,7,10,13,14\}.\]
  The complete rows at `3,14` give `L=c_3q_0=c_0q_14`; the rows at `0,1` give `L≥c_0q_0+c_3q_13` and `L≥c_3q_14+c_0q_1`. Since `q_13,q_1>0`, the first comparison forces `c_3>c_0` and the second forces `c_0>c_3`.

* `g=9`, modulo 18. Anchor `3` forces `c_12>0`, because `3+13=16` is opposite tail anchor `7`. Anchor `8` forces `c_17>0`, because `8+1=9` is opposite `0`. But `12+14=8` and `17+0=17` are antipodes, impossible.

* `g=10`, modulo 20. Since `3` is opposite tail anchor `13`, anchor `3` forces `c_13>0`. Anchor `8` forces `c_8>0`, because `18+13=11` is opposite tail anchor `1`. The resulting forced union is
  \[V=\{0,1,2,6,7,8,9,13,14,15\}.\]
  Anchor `11` forces `c_1>0` because `11∉V`. Testing the selector gives
  \[\operatorname{supp}c\subseteq\{0,1,7,8,13,14\},\quad
  \operatorname{supp}q\subseteq\{0,1,7,13,14\}.\]
  The complete rows at `6,9` give `L=c_13q_13=c_8q_1`. At rows `1,14`, respectively, `L≥c_8q_13+c_0q_1` and `L≥c_13q_1+c_0q_14`. The first forces `c_13>c_8`, the second `c_8>c_13`.

### 3.2. The case `g=15`

Modulo 30, anchor `3` forces `c_18>0` (`3+13=16` is opposite `1`), anchor `8` forces `c_23>0` (`8+7=15` is opposite `0`), and anchor `11` forces `c_11>0` (`26+7=3` is opposite the forced residue `18`). Along with `c_0>0`, their translates of `S` occupy exactly

\[
F=\{0,1,2,6,7,11,12,13,14,18,19,23,24,25\}.
\]

These occupy fourteen different antipodal pairs; the remaining pair is `{5,20}`. Write `V=F∪{h}`. The support tests `i+S⊂V`, `j+{0,11,18,23}⊂V` give

| `h` | possible `supp(c)` | possible `supp(q)` |
|---|---|---|
| 5 | `{0,5,11,18,23}` | `{0,1,7,12,13,14,19,25}` |
| 20 | `{0,6,11,18,23}` | `{0,1,2,7,13,14,19,25}` |

In either case, the complete coefficient rows at `11,14` and the displayed positive terms in rows `0,25` yield

\[
L=c_{11}q_0=c_0q_{14},\quad
L\ge c_0q_0+c_{23}q_7,\quad
L\ge c_{11}q_{14}+c_{18}q_7.
\]

All displayed forced factors are positive, so these give `c_11>c_0` and `c_0>c_11`.

### 3.3. The case `g=16`

Modulo 32, anchor `3` forces `c_19>0`, since `3+13=16` is opposite `0`. Anchors `8,11` choose among `{8,24}` and `{11,27}`. Both unshifted choices give antipodes `8+1=9` and `11+14=25`; both shifted choices give the same pair in the opposite order. Thus the only cases are `(c_8,c_27)>0` and `(c_24,c_11)>0`. In each case the following forced union contains one member of every antipodal pair and so is all of `V`:

| case | `V` | possible `supp(c)` | possible `supp(q)` |
|---|---|---|---|
| A: `8,27` | `{0,1,2,7,8,9,13,14,15,19,20,21,22,26,27,28}` | `{0,1,7,8,13,14,19,20,26,27}` | `{0,1,7,13,14,20,26}` |
| B: `24,11` | `{0,1,5,6,7,11,12,13,14,18,19,20,24,25,26,31}` | `{0,5,6,11,12,18,19,24,25,31}` | `{0,1,7,13,14,20,26}` |

For A the support tests use forced `C` residues `{0,8,19,27}`. Complete rows at `19,22` and positive terms at `8,1` give

\[
L=c_{19}q_0=c_8q_{14},\quad
L\ge c_8q_0+c_{27}q_{13},\quad
L\ge c_{19}q_{14}+c_0q_1,
\]

which implies both `c_19>c_8` and `c_8>c_19`. For B use forced residues `{0,11,19,24}`. Complete rows at `11,14` and positive terms at `0,25` give

\[
L=c_{11}q_0=c_0q_{14},\quad
L\ge c_0q_0+c_{19}q_{13},\quad
L\ge c_{11}q_{14}+c_{24}q_1,
\]

which implies both `c_11>c_0` and `c_0>c_11`. Thus `g=16` is impossible.

Together with the prime and antipodal cases, this proves, **from the displayed weighted identities and actual factor hypothesis**, that `g≥18` and `g` is composite. This is a structural-subclass result, not an unrestricted anchored nonexistence theorem. The packet's larger author/reviewer/checker bodies for the older small-gcd disposition are not needed as imports for this displayed argument and were not opened.

## 4. Original cyclic difference spectra: exact characterization

For any `E⊂Z_n` define its nonzero original gcd spectrum

\[
\Sigma_n(E)=\{\gcd(n,x-y):x,y\in E,\ x\ne y\}.
\]

It consists of proper divisors of `n`; coinciding residues are deliberately excluded.

### 4.1. Admissible dilation lemma

If `U⊕W=Z_n` and positive `k` is coprime to `|U|`, then multiplication by `k` is injective **on U**, and `kU⊕W=Z_n`, even when `k` is not a unit modulo `n`. To prove this, first take a prime `ℓ∤|U|`. In the integral group ring of `Z_n` let `J=∑_x X^x`. Reducing modulo `ℓ`,

\[
U(X^\ell)W(X)=U(X)^\ell W(X)
=U(X)^{\ell-1}J=|U|^{\ell-1}J=J.
\]

The left side is interpreted with original multiplicities before passing to an image set. Its `n` integer coefficients are nonnegative, each congruent to 1 modulo `ℓ`, and sum to `|U||W|=n`; therefore each is exactly 1. A collision within the dilated `U` would give some coefficient at least 2, so dilation is injective on `U`. Repeat over prime factors of `k`, keeping the cardinality unchanged. Since `|U||W|=n`, every unit modulo `n` is in particular admissible for either factor.

### 4.2. Unit orbits and spectrum equivalence

For residues `t,s`,

\[
\gcd(n,t)=\gcd(n,s)\quad\Longleftrightarrow\quad
\exists v\in\mathbb Z_n^\times:\ vt\equiv s\pmod n.\tag{4}
\]

The reverse direction is immediate. For the forward direction, at each prime power `p^e||n`, the truncated valuations agree. If both residues vanish modulo `p^e`, take `v=1` there. Otherwise write `t=p^a t'`, `s=p^a s'` with `a<e` and `t',s'` units modulo `p^{e-a}`, and choose `v≡s'(t')^{-1} mod p^{e-a}`; any lift to modulo `p^e` remains a unit. CRT combines these local units into one unit modulo `n`.

**Theorem 2 (exact full-spectrum criterion).** For nonempty `U,W⊂Z_n` with `|U||W|=n`,

\[
U\oplus W=\mathbb Z_n
\quad\Longleftrightarrow\quad
\Sigma_n(U)\cap\Sigma_n(W)=\varnothing.\tag{5}
\]

For necessity, suppose a common gcd occurs in the original differences `x−y` of `U` and `s−r` of `W`, with both pairs distinct. By (4) choose a unit `v` with `v(x−y)=s−r`. The admissible dilation lemma makes `vU⊕W` direct, yet the distinct ordered pairs `(vx,r)` and `(vy,s)` have equal sum, a contradiction. For sufficiency, a collision `u+w=u'+w'` of two distinct ordered pairs necessarily has both coordinates different, and so its two nonzero differences have the same gcd with `n`; disjoint spectra therefore give an injective sum map. Its domain has exactly `n` ordered pairs, hence it covers `Z_n`. ∎

This equivalence uses the **entire actual** spectra, not only anchor differences. For the actual tail, the literal anchor spectrum is

\[
D_Q=\{1,6,7,12,13,14\},\qquad
\mathcal D(n)=\{\gcd(n,s):s\in D_Q\}\subseteq\Sigma_n(Q).\tag{6}
\]

Therefore every original nonzero head difference has gcd outside `𝒟(n)`. Conversely, avoiding `𝒟(n)` alone is only a necessary test, not a proof of a tiling or of full-spectrum separation. The unit/CRT step is performed in the original `Z_n`; no gcd from a quotient is substituted.

## 5. Every actual sign and coincidence boundary

In the normalized factorization (1), each original anchor has a unique factor representation `a=c_a+e_a d`, with `e_a∈{0,1}`. Define `ε_a=1−2e_a`, so its actual mate is

\[
f(a)=a+\varepsilon_a d\in P,\qquad \varepsilon_0=+1.
\]

The map `f` exchanges the two members of each actual direct-factor pair; in particular it is an involution on `P`. For every `a,b∈A` and `i,j∈{0,1}` the exact necessary anchor/mate test is

\[
\gcd\!\left(n,(a-b)+i\varepsilon_a d-j\varepsilon_b d\right)
\notin\mathcal D(n).\tag{7}
\]

When the two compared elements coincide, the gcd in (7) is `n`, and `n∉𝒟(n)` because `n>14`; the test remains valid without pretending that a zero difference is nonzero. Equation (7) includes anchor–anchor, anchor–mate, mate–mate, and the original factor difference `g`. If one wishes to test an unoriented original `d_0`, both choices `d=±d_0` with `ε_0=+1` must be considered: an actual factor must realize **one** of these orientations and one compatible sign vector, not four independently selected CRT signs. If every such vector violates (7), the factor is impossible; existence of a passing vector by itself proves neither a factor nor a tiling.

The exact coincidence rules are as follows. For distinct anchors `a,b`, `f(a)=b` if and only if `f(b)=a`; the physical signs are then opposite, and `d≡±(b−a) mod n`. Distinct anchors cannot have equal mates, because `f` is injective. Thus the four actual anchor pairs are pairwise disjoint or identical. If `m∈{0,1,2}` of these pairs have both endpoints in `A`, the union of all anchors and their actual mates has exactly `8−2m` elements. A coincidence of distinct anchors in a pair requires `g` to divide one of the positive anchor gaps `{3,5,8,11}`; it is not implied merely by that divisibility. The proven `g≥18` therefore makes all eight anchor/mate elements distinct. The order-two boundary `2d=0` is included: then `d=−d` as a residue, but the two endpoints still carry opposite physical factor labels, and `f` remains a fixed-point-free involution.

For an informative reduced test, put `a∈{3,8,11}`. Because both `d` and `a` are actual head elements,

\[
\gcd(n,a-d)\notin\mathcal D(n).\tag{8}
\]

If `ε_a=+1`, comparison with the additional mate `a+d` also forces `gcd(n,a+d)∉𝒟(n)`; if `ε_a=−1`, comparison of the mate `a−d` with `d` forces `gcd(n,a−2d)∉𝒟(n)`. These statements also handle a coincident comparison via gcd `n`. In particular, for an **unoriented** `d_0`, if both `gcd(n,8+d_0)` and `gcd(n,8−d_0)` lie in `𝒟(n)`, neither possible orientation can satisfy (8). This is the packet's two-sign obstruction; after normalization (8) gives the sharper actual-orientation statement.

If `n=HR` with `gcd(H,R)=1`, CRT gives, with the **same physical sign** in both coordinates,

\[
g=\gcd(H,d_H)\gcd(R,d_R),\quad
\gcd(n,a+\varepsilon d-b)
=\gcd(H,a+\varepsilon d_H-b)\gcd(R,a+\varepsilon d_R-b).
\tag{9}
\]

For the general pair expression in (7), replace `a+εd−b` by the same integer linear combination in each coordinate. Neither a favorable single coordinate nor a separate choice of sign in each coordinate proves a valid original gcd.

A related graph statement requires its own **actual graph hypothesis**: if `P={(h,f(h)):h∈B_0}⊂Z_H×Z_R`, then it has the actual direct factor of difference `(d_H,d_R)` iff some `B⊂B_0` satisfies `B_0=B ⊔ (B+d_H)` and `f(b+d_H)−f(b)=d_R` for every `b∈B`. Forward, project the actual `C` and use injectivity of the graph; backward, lift the displayed `B` into the graph. In particular `d_H=0` is impossible for a nonempty graph factor. The separately named coprime-cardinality route that may establish this graph hypothesis in special numerical families has no proof body in this packet and remains a **conditional import**; it is not used above. Likewise, separately complementing graph shadows does not establish the coupled original tail equations.

## 6. Infinite composite families and cardinality audit

Use `rad_odd(n)` for the product of distinct odd prime divisors of `n`. The following are original-group consequences of (8), safe for either physical orientation because their arithmetic statements hold for both signs:

1. If `g` is odd and `rad_odd(n)|g`, then `d` is odd and every odd prime dividing `n` divides `d`; consequently both `8±d` are coprime to `n`. Since `1∈𝒟(n)`, no actual factor exists.
2. If `v_2(g)=1`, `rad_odd(n)|g`, and `7∤n`, then `v_2(n)≥2`, both `8±d` have exact 2-adic valuation 1, and no odd prime of `n` divides either. Their gcd with `n` is 2, which equals `gcd(n,14)∈𝒟(n)`. More generally, under `v_2(n)≥2`, the displayed literal tail spectrum contains 2 exactly when `3∤n` or `7∤n`; the second alternative suffices here.
3. Let `r∈{7,13}`. If `g` is odd, `r|n`, `r∤g`, `v_r(n)=1`, and every other odd prime of `n` divides `g`, then `gcd(n,8±d)` is either 1 or `r`; both belong to `𝒟(n)`, since `r` is itself a tail anchor.

For an explicit unbounded family in cases 1–2, take

\[
n=2^s3^a5^b11^c,\quad s\ge4,\ a,b,c\ge1,\qquad
g=2^e3^i5^j11^k,
\quad e\in\{0,1\},\quad1\le i\le a,\ 1\le j\le b,\ 1\le k\le c.
\tag{10}
\]

Every such `g` is composite, divides `n`, and satisfies `2g|n`; the residue `d=g` shows that the bare gcd and even-cycle arithmetic is possible. Nevertheless the relevant case 1 or 2 excludes an actual anchored factor of that gcd. Varying the exponents gives unbounded odd and even composite gcds. Similarly, for either `r∈{7,13}`, taking `n=2^s3^a5^b11^c r`, with the same lower bounds on `s,a,b,c`, and `g=3^i5^j11^k` with positive allowed exponents gives an unbounded composite family for case 3. These are exclusions, not examples of actual tilings.

The same dilation lemma independently checks the numerical cardinality restrictions. If `|P|` were odd, the admissible head dilation by 2 would collide via `2·3+1=2·0+7`. If `|Q|` were odd, the admissible tail dilation by 8 would collide via `8+8·0=0+8·1`. If respectively 3, 5 or 11 failed to divide `|Q|`, tail dilation by that prime would give the collisions

\[
3+3\cdot0=0+3\cdot1,\quad
8+5\cdot0=3+5\cdot1,\quad
11+11\cdot0=0+11\cdot1.
\]

The displayed original anchors are distinct since `n>14`. Thus `2||P|` in the sense `2` **divides** `|P|` (not exact 2-adic valuation), and `330||Q|` in the same divisibility sense. Also `|P||Q|=n`. Under the actual factor hypothesis proved above, `g≥18`; the four anchor residues modulo `g` are distinct, so their original `C` representatives are distinct and `|C|≥4`, `|P|≥8`. If additionally `|P|=8`, those four representatives exhaust `C`, and `P` is exactly the union of their four actual pairs.

For (10), the **hypothetical** allocation `|P|=8`, `|Q|=n/8` is numerically compatible with the divisibility requirements: `n/8=2^{s-3}3^a5^b11^c` is a multiple of 330. The case-3 family has the same property. The phrase in S1 suggesting a 'necessary allocation |P|=8' must not be read as proving that every head has cardinality 8: what is necessary here is only `|P|≥8`; equality is an optional allocation. Numerical compatibility is not an actual-factor or tiling construction.

## 7. Limits and complete process declaration

* The actual original-head direct-factor assumption is essential to the weighted argument. No factor is inferred from the anchors, a replacement tile, a quotient shadow, an unrestricted hypothetical tiling, or the conditional graph import. Heads without such a factor and actual factors with remaining composite `g≥18` outside the spectrum exclusions remain unclosed. The first unpaid step is an actual-factor/coupled-tail construction or a further obstruction, not a proposed factorization of an anchor subset.
* The packet's small-gcd author/reviewer/checker source bodies and the separately named graph-source proof body are not present as complete underlying bodies; they were not opened via links. The former are not required by §3's displayed reconstruction. The graph-producing route, the RSS/pure-letter bridge and printed-problem correspondence remain named conditional imports/outside scope. No global theorem, human/family/kernel acceptance, publication priority or novelty is claimed.
* Before packet access or mathematical reasoning, I read the complete manifest, freeze receipt, final binding, live metadata supply, actual dispatch receipt, and all 22 listed status-only controls. The first formatted administrative displays elided entries or a long line; complete raw rereads recovered them before the prebody acknowledgement. I wrote `prebody-ack-v1.md` and directly delivered the acknowledgement to Main before opening the packet. Status-only controls were not mathematical inputs; all genuine held episodes and every proof/method/planning/selection/verification/reporting/confidence/downstream consumer remained NONINPUT. No unobservable-cognition certificate is claimed.
* I then read the single literal packet part completely, in order, raw windows `1–20`, `21–40`, `41–60`, `61–80`, `81–100`, `101–120`, `121–140`, `141–160`, `161–180`, `181–200`, `201–220`, `221–240`, `241–260`, `261–280`, `281–300`, `301–320`, `321–340`, `341–360`, `361–374`, including its ending. Each displayed window was under 30,000 bytes and at most 20 LF; none was clipped, so no packet clipping recovery was needed. This covers the complete rendered S1 `1–278`, S2 `1–51`, S3 `1–31`; no linked body was opened. Parent-supplied pins, not independently recomputed here: packet `e4903ba0b42848ed92da00d02dfa00a3be19177f88cf158941def095850d35c5`; S1 `91f2b1a4d4326feeff89cf6ec6541c1437989a08ea84d60e359a8ba546e16e14`; S2 `45e8f43ab00178a600fd733276bc540164260cf97127c73106a1dc541c8838ad`; S3 `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`.
* No network, external model, scientific code execution, child subprocess, solver, test, compilation, scientific eval, or code preparation was used. There is no prepared-code hash or execution result. Apart from the recovered initial administrative display elisions, no process deviation is known. The displayed written mathematics remains author work awaiting separate review and parent disposition.
