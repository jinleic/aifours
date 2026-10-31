# F894 author candidate: composite original gcd — prime-power/cyclotomic projections of the original weighted fibres, lift rigidity, and the exclusions g=18,20,21,22,25,26,27

**Status.** Prospective GENERAL AUTHOR written candidate under owner addendum 2. Not a parent disposition, independent review, family/human/formal acceptance, novelty or priority claim. Every statement concerns ONE actual ordered direct tiling and ONE actual two-point direct factor of its ORIGINAL head. No such tiling or factor is asserted to exist; the anchors alone do not force the factor; no unrestricted anchored nonexistence or maximal-code statement follows. No code was prepared or executed.

## 0. Quantifiers and normalization (as in S5 §1, S6 §1, S7 §1)

Let `n>14`, `P,Q⊂Z_n` with every residue having exactly one ordered representation `p+q`, and
`A0={0,3,8,11}⊆P`, `S={0,1,7,13,14}⊆Q`. Assume in addition an actual direct factorization `P={u,u+d}⊕C_0`, `d≢0 (mod n)`, and `g=gcd(d,n)` in the original `Z_n`.

Absorb `u` and, if needed, replace `(d,C)` by `(−d,C+d)`, so that `P={0,d}⊕C`, `0∈C`; `P,Q,g` are unchanged. With `T=C⊕Q`: `1_T(x)+1_T(x−d)=1`, hence `2g|n`, `d/g` odd, `d≡g (mod 2g)`, `T` is the full inverse image of a selector `V⊂Z_m`, `m=2g` (exactly one of `r,r+g` in `V`), and with ORIGINAL multiplicities `c_i=#{c∈C: c≡i mod m}`, `q_j=#{q∈Q: q≡j mod m}`, `L=n/m`:

(W) `Σ_i c_i q_{s−i} = L·1_V(s)` for every `s∈Z_m`.

Consequences used throughout (all from (W) with nonnegative integer weights): `c_0>0`; `q_s>0` for `s∈S`; `S⊂V`; `c_i>0 ⇒ i+S⊂V`; `q_j>0 ⇒ j+supp(c)⊂V`; each anchor `a∈{3,8,11}` has a positive `c` at `a+ε_a g` for some `ε_a∈{0,1}` (its actual `C` representative; `ε_a` is attached to the single physical factor). For a set `D` of forced positive `c`-residues put `A(V)=⋂_{s∈S}(V−s)` and `B(V,D)=⋂_{i∈D}(V−i)`; then `supp c⊆A(V)`, `supp q⊆B(V,D)` (necessary supersets, never a quotient tiling). If `s∈V` and `I_s={(i,j)∈A(V)×B(V,D): i+j≡s}`, then `L=Σ_{(i,j)∈I_s} c_iq_j` exactly, every term nonnegative.

## 1. General lemmas (all composite g)

**Lemma 1 (cyclotomic vanishing on divisors of g).** For every divisor `e>1` of `g` and a primitive `e`-th root `ζ`, `c(ζ)q(ζ)=0`, where `c(X)=Σ c_iX^i`, `q(X)=Σ q_jX^j`. Equivalently `C(ζ)=0` or `Q(ζ)=0` for the original mask polynomials (since `e|m`, `C(ζ)=c(ζ)`, `Q(ζ)=q(ζ)`).

*Proof.* (W) is `c(X)q(X)≡L·V(X) mod X^m−1`. Because `V⊔(V+g)=Z_m`, `V(X)(1+X^g)≡Σ_{x∈Z_m}X^x`. At `ζ` (`e|m`, `e>1`) the right side is `0`; as `e|g`, `ζ^g=1`, so `2V(ζ)=0`. Hence `c(ζ)q(ζ)=L·V(ζ)=0`. Since `c,q` have integer coefficients, `c(ζ)=0` for one primitive `e`-th root iff for all of them (Galois conjugation); so "`C` (or `Q`) vanishes at order `e`" is well defined and used below in that sense. ∎

**Lemma 2 (prime-power fibre criterion, multiplicities retained).** Let `p^k` divide `m` and let `w` be any integer weight on `Z_m`; put `W(r)=Σ_{x≡r (p^k)} w_x` on `Z_{p^k}`. Then `w(ζ_{p^k})=0` iff `W(r)=W(r+p^{k−1})` for all `r`, i.e. `W` is constant on every fibre `{r+jp^{k−1}: 0≤j<p}` of `Z_{p^k}→Z_{p^{k−1}}`.

*Proof.* `w(ζ)=Σ_r W(r)ζ^r`, a polynomial `F` of degree `<p^k`. The minimal polynomial of `ζ` over `Q` is `Φ_{p^k}(X)=Σ_{j<p}X^{jp^{k−1}}` (irreducible: `Φ_{p^k}(X+1)` is Eisenstein at `p`), of degree `p^{k−1}(p−1)`. So `F(ζ)=0` iff `F=Φ_{p^k}H` with `deg H<p^{k−1}`; the coefficient of `X^{r+jp^{k−1}}` (`r<p^{k−1}`) in `Φ_{p^k}H` is exactly `h_r`, independent of `j`. Conversely a fibre-constant `F` has this form. ∎

For `k=1` this is the prime-profile statement of S5 Theorem A / S6 Theorem 1.

**Lemma 3 (anchor-translate compatibility for g≥18).** Let `g≥18`, `a_x=x+ε_x g` (`x∈{3,8,11}`), `a_0=0`. The four translates `a+S` contain an antipodal pair iff for some pair `x≠y` in `{0,3,8,11}` with `ε_x=ε_y` (where `ε_0=0`) there are `s,s'∈S` with `(x+s)−(y+s')=±g`. With `Δ={0,±1,±6,±7,±12,±13,±14}` (all differences of `S`) this reduces exactly to `|x−y−δ|=g` for some `δ∈Δ`, giving the complete list:

| g | forced by antipodal compatibility |
|---|---|
| 18 | `ε_11=1` (`0+7`, `11+14` antipodal); `ε_3≠ε_8` (`8+13`, `3+0`) |
| 20, 21, 22 | `ε_8=1` (`0+1`,`8+13` / `0`,`8+13` / `0`,`8+14`); `ε_3≠ε_11` (`3+1`,`11+13` / `3`,`11+13` / `3`,`11+14`) |
| 23, 24, 25 | `ε_11=1` (`1`,`11+13` / `0`,`11+13` / `0`,`11+14`) |
| 19 | `ε_3≠ε_8` (prime; already excluded by S5 Theorem A) |
| ≥26 | no constraint |

*Proof.* Two residues `x+εg+s`, `y+ε'g+s'` are antipodal iff their difference is `≡g (mod 2g)`. If `ε≠ε'` this says `x−y−(s'−s)≡0 (mod 2g)`, impossible since `x−y∈{±3,±5,±8,±11}`, `s'−s∈Δ` and `|x−y−(s'−s)|≤25<36≤2g` with `{3,5,8,11}∩{0,1,6,7,12,13,14}=∅`. If `ε=ε'` it says `x−y−(s'−s)≡g (mod 2g)`, and as `|x−y−δ|≤25<3g` this is `x−y−δ=±g`. Enumerating `x−y∈{3,5,8,11}` (and negatives) against `δ∈Δ`: `3−δ` has `|·|≤17`; `5−δ∈{18,19}` only for `δ=−13,−14`; `8−δ∈{20,21,22}` only for `δ=−12,−13,−14`; `11−δ∈{18,23,24,25}` only for `δ=−7,−12,−13,−14`. Within one translate no antipode occurs because `|δ|≤14<g`. ∎

**Lemma 4 (support saturation; extends S5 Theorem A to every g≥2).** Neither `supp c` nor `supp q` meets every antipodal class `{r,r+g}` of `Z_m`. Consequently there is no divisor-closed equidistribution of one factor: it is impossible that `C(ζ_e)=0` for all `e|g, e>1` (then the `C`-profile mod `g` is constant and positive), and likewise for `Q`.

*Proof.* `supp c⊆V` (as `q_0>0`) and `supp q⊆V` (as `c_0>0`). If `supp c` meets every class, `supp c=V`; with `q_1>0`, `V+1⊆V`, so `V+1=V` and `V=Z_m`, contradicting `|V|=g`. If `supp q=V`, then every `i∈supp c` satisfies `V+i=V`, so `i∈H=Stab(V)`, a subgroup with `g∉H` (because `V+g=Z_m∖V`). For `x∈Z_m`, `g∈⟨x⟩` iff `gcd(x,m)|g` iff `v_2(x)≤v_2(g)`. If `g` is even, `a_3∈{3,3+g}` is odd, so `g∈⟨a_3⟩⊆H`: contradiction. If `g` is odd, `a_3=3`, `a_8=8+g`, `a_11=11` are odd and impossible, so `a_3=3+g`, `a_8=8`, `a_11=11+g∈H`; then `H⊇⟨8,3+g⟩=⟨gcd(8,3+g,2g)⟩=⟨2⟩`, so `V` is a union of parity classes, while `0,1∈V`: `V=Z_m`, contradiction. If all `e|g, e>1` annihilate `C`, then `Σ_{e|g}`-orthogonality makes the `C`-profile mod `g` constant, positive because `c_0>0`, so `supp c` meets every class. ∎

Lemma 4 recovers S5 Theorem A (`g` prime: Lemma 1 gives one factor annihilated at the only nontrivial divisor). For composite `g` it only says the annihilation pattern on divisors of `g` is genuinely mixed; it does not by itself exclude any composite value.

## 2. Theorem E: the original gcd g=18 is impossible

**Theorem E.** Under §0 hypotheses, `g≠18`. With S5 Theorem A, S7 (g=15,16) and the S2/S6 small-gcd scope (conditional imports, §6), every remaining actual factor has composite `g≥20`.

*Proof.* `m=36`, antipode `r↔r+18`. By Lemma 3, `c_29>0` and exactly one of the two cases below holds.

**Case A: `ε_3=0, ε_8=1`; forced `D={0,3,26,29}`.** Translates: `0+S={0,1,7,13,14}`, `3+S={3,4,10,16,17}`, `26+S={3,4,26,27,33}`, `29+S={0,6,7,29,30}`. Union
`F_A={0,1,3,4,6,7,10,13,14,16,17,26,27,29,30,33}` — sixteen residues in sixteen distinct classes mod 18; the free pairs are `{2,20}`, `{5,23}`. The residues certainly outside `V` are the antipodes `{8,9,11,12,15,18,19,21,22,24,25,28,31,32,34,35}`.

Complete supersets (test `i+1,i+7,i+13,i+14∈V`; `j+3,j+26,j+29∈V`):
`A(V)={0,3,26,29}∪{13 if 20∈V}∪{16 if 23∈V}`;
`B(V,D)={0,1,4,7,10,13,14}∪{17,27 if 20∈V}∪{23,33 if 23∈V}∪{20,30 if 20,23∈V}`.

*Row 2.* If `2∈V`: candidates `(i,2−i)` are `(0,2)`, `(3,35)`, `(26,12)`, `(29,9)`, `(16,22)` (and `13∉A` since `20∉V`). `2∉B` (`2+26=28∉V`); `35,12,9,22∉V`. So `I_2=∅` and (W) gives `0=L`, impossible. Hence `20∈V`.
*Row 5.* If `5∈V`: `(0,5)`: `5∉B` (`5+3=8∉V`); `(3,2)`: `2∉V`; `(26,15)`, `(29,12)`, `(13,28)`: `15,12,28∉V`; `16∉A` as `23∉V`. So `I_5=∅`, impossible. Hence `23∈V`.

Thus `V=F_A∪{20,23}`, `A(V)={0,3,13,16,26,29}`, `B={0,1,4,7,10,13,14,17,20,23,27,30,33}`.

Row 1: `1−i` for `i∈A(V)` is `1,34,24,21,11,8`; only `1∈V`. So **`L=c_0q_1`**.
Row 7: `I_7={(0,7),(3,4),(13,30),(16,27),(26,17),(29,14)}`, so `L≥c_0q_7+c_29q_14>c_0q_7` (`c_29,q_14>0`). Hence **`q_7<q_1`**.

*Prime-power projection at 9 (multiplicities retained).* `supp c⊆A(V)` has residues mod 9 `{0,3,4,7,8,2}` (from `0,3,13,16,26,29`). On the fibre `{0,3,6}` the `C`-masses are `(c_0,c_3,0)`; by Lemma 2, `C(ζ_9)=0` would force `c_0=0`. So `C(ζ_9)≠0`, and Lemma 1 (`9|18`) gives `Q(ζ_9)=0`. The `Q`-masses on the fibre `{1,4,7}` are, from `supp q⊆B`: residue 1: `q_1+q_10` (`19,28∉V`); residue 4: `q_4+q_13` (`22,31∉V`); residue 7: `q_7` (`16∉B` since `16+3=19∉V`; `25,34∉V`). Lemma 2: **`q_1+q_10=q_4+q_13=q_7`**, so `q_7≥q_1`, contradicting `q_7<q_1`.

**Case B: `ε_3=1, ε_8=0`; forced `D={0,8,21,29}`.** Translates `0+S`, `29+S={0,6,7,29,30}`, `8+S={8,9,15,21,22}`, `21+S={21,22,28,34,35}`; union
`F_B={0,1,6,7,8,9,13,14,15,21,22,28,29,30,34,35}` (sixteen classes), free pairs `{2,20}`, `{5,23}`; certainly outside `V`: `{3,4,10,11,12,16,17,18,19,24,25,26,27,31,32,33}`.

Supersets: `A(V)={0,8,21,29}∪{1 if 2∈V}∪{7 if 20∈V}∪{22 if 23∈V}∪{28 if 5∈V}`;
`B(V,D)={0,1,7,13,14,21,22,28,29}∪{15 if 23∈V}∪{35 if 20∈V}∪{20 if 20,5∈V}∪{30 if 2,23∈V}`.
Uniformly in all four free choices:
* Row 9 (`9∈F_B`): `9−i` over all possible `i∈{0,8,21,29,1,7,22,28}` is `9,1,24,16,8,2,23,17`; `9,24,16,17∉V`, `8∉B` (`8+8=16∉V`), `2∉B` (`2+8=10∉V`), `23∉B` (`23+8=31∉V`). So **`L=c_8q_1`**.
* Row 34 (`34∈F_B`): `34−i` is `34,26,13,5,33,27,12,6`; `26,33,27,12∉V`, `34∉B` (`34+21=55≡19∉V`), `5∉B` (`5+21=26∉V`), `6∉B` (`6+21=27∉V`). So **`L=c_21q_13`**.
* Row 21 (`21∈F_B`) contains `(8,13)` and `(21,0)`: `L≥c_8q_13+c_21q_0>c_8q_13`, so with `L=c_21q_13`, **`c_21>c_8`**.
* Row 22 (`22∈F_B`) contains `(8,14)` and `(21,1)`: `L≥c_21q_1+c_8q_14>c_21q_1`, so with `L=c_8q_1`, **`c_8>c_21`**.
Contradiction. Both cases fail; `g=18` is impossible. ∎

(Case B needs no cyclotomic input; Case A is the first place where a non-prime prime-power projection of the original count profile — `Φ_9` on the `Q` profile, multiplicities kept — is decisive.)

## 3. Theorem F: the original gcd g=20 is impossible

**Theorem F.** Under §0 hypotheses, `g≠20`.

*Proof.* `m=40`, antipode `r↔r+20`. Lemma 3: `ε_8=1` (`c_28>0`) and `ε_3≠ε_11`.

**Case I: `D={0,3,28,31}`.** Translates `{0,1,7,13,14}`, `{3,4,10,16,17}`, `28+S={1,2,28,29,35}`, `31+S={4,5,31,32,38}`; union
`F={0,1,2,3,4,5,7,10,13,14,16,17,28,29,31,32,35,38}` (eighteen classes mod 20), free pairs `{6,26}`, `{19,39}`; certainly outside `V`: `{8,9,11,12,15,18,20,21,22,23,24,25,27,30,33,34,36,37}`. Testing every residue, `A(V)={0,3,28,31}` in all four free choices (`5` needs `12`, `6` needs `20`, `19` needs `20`, `26` needs `27`, `38` needs `11`, `39` needs `12`).
* Row 6 (if `6∈V`): `6−i` for `i∈A(V)` is `6,3,18,15`; `6∉B` (`6+3=9∉V`), `3∉B` (`3+31=34∉V`), `18,15∉V`: empty. So `26∈V`.
* Row 39 (if `39∈V`): `39,36,11,8`; `39∉B` (`39+28≡27∉V`), others `∉V`: empty. So `19∈V`.

Hence `V=F∪{19,26}` and `B(V,D)={0,1,4,7,10,13,14,16,26,28,38}`. Complete rows:
* row 0: `{(0,0)}` (`37,12,9∉V`) ⇒ `L=c_0q_0`; row 3: `{(3,0)}` (`3∉B`, `15,12∉V`) ⇒ `L=c_3q_0`; so **`c_3=c_0`**;
* row 2: `{(28,14)}` (`2∉B`, `39,11∉V`) ⇒ `L=c_28q_14`; row 5: `{(31,14)}` (`5,2,17∉B`) ⇒ `L=c_31q_14`; so **`c_31=c_28`**;
* row 14: `{(0,14),(28,26)}` (`11,23∉V`) ⇒ `c_0q_14+c_28q_26=c_28q_14`, so **`c_0≤c_28`**;
* row 13: `{(0,13),(3,10)}` (`25,22∉V`) and row 1: `{(0,1),(3,38),(28,13),(31,10)}`. Equating both to `L` and using `c_3=c_0`, `c_31=c_28`:
  `(c_0−c_28)(q_13+q_10)=c_0(q_1+q_38)>0`, so **`c_0>c_28`**. Contradiction.

**Case II: `D={0,11,23,28}`.** Translates `{0,1,7,13,14}`, `{11,12,18,24,25}`, `{23,24,30,36,37}`, `{1,2,28,29,35}`; union
`F={0,1,2,7,11,12,13,14,18,23,24,25,28,29,30,35,36,37}`, free pairs `{6,26}`, `{19,39}`; outside `V`: `{3,4,5,8,9,10,15,16,17,20,21,22,27,31,32,33,34,38}`.
Supersets: `A(V)={0,11,23,28}∪{12 if 19,26∈V}∪{39 if 6,39∈V}`; `B(V,D)={0,1,2,7,12,13,14,24,30}∪{18,35 if 6∈V}∪{19,36 if 19∈V}`.
If `26,39∈V`, row 26 has candidates `26,15,3,38` only (`26∉B` as `26+23≡9∉V`): empty. Three subcases remain.
* `(6,19)`: complete singleton rows 11 `{(11,0)}`, 28 `{(28,0)}`, 14 `{(0,14)}`, 37 `{(23,14)}` give `c_11=c_28`, `c_0=c_23`. Row 0 `{(0,0),(28,12)}` gives `c_0≤c_28`; row 2 `{(0,2),(23,19),(28,14)}` gives `c_28≤c_0`. So `c_0=c_11=c_23=c_28=:γ` and row 0 forces `q_12=0`. Rows 12 `{(0,12),(11,1),(28,24)}` and 24 `{(0,24),(11,13),(23,1),(28,36)}` then give `q_12=q_13+q_36`, so `q_13=0`, contradicting the tail anchor `13`.
* `(6,39)`: row 39 is `{(39,0)}` (`39,28,11∉B`, `16∉V`), so `L=c_39q_0` and `c_39>0`. Row 28 `{(28,0)}` gives `L=c_28q_0`; row 0 `{(0,0),(28,12),(39,1)}` gives `L>c_0q_0`, so `c_0<c_28`. Row 14 `{(0,14)}` gives `L=c_0q_14`; row 2 `{(0,2),(28,14)}` (`31,19,3∉V`) gives `c_28≤c_0`. Contradiction.
* `(26,19)`: rows 11 `{(11,0)}`, 37 `{(23,14)}` and 26 `{(12,14)}` (`26∉B`, `15,3,38∉V`) give `L=c_11q_0=c_23q_14=c_12q_14`, so `c_12=c_23>0`. Row 12 `{(0,12),(11,1),(28,24),(12,0)}` gives `L>c_12q_0`, i.e. `c_11>c_12`; row 25 `{(11,14),(23,2),(12,13)}` gives `L>c_11q_14`, i.e. `c_11<c_23=c_12`. Contradiction.

All cases fail. ∎

## 4. Two further projection lemmas

**Lemma 5 (one residue per class modulo a prime).** Let `e=qf|m` with `q` prime, `q∤f`, let `w≥0` be an integer weight on `Z_m` and `W(r)=Σ_{x≡r (e)}w_x` on `Z_e`. Suppose every class `b mod q` contains at most one `r∈Z_e` with `W(r)>0`, and `W≠0`. If `w(ζ_e)=0`, then `supp W` has exactly `q` elements, one in each class mod `q`, all congruent modulo `f`, and `W` is constant on it. (For `f=1`: `Φ_q|w` forces `W` constant on `q` residues, one per class.)

*Proof.* Choose `s,t` with `qs+ft≡1 (mod e)`; `θ=ζ_e^{qs}` is a primitive `f`-th and `ψ=ζ_e^{ft}` a primitive `q`-th root, and `ζ_e^r=θ^rψ^r`. So `w(ζ_e)=Σ_{b∈Z_q}ψ^bβ_b`, `β_b=Σ_{r≡b (q)}W(r)θ^r∈Q(θ)`. Since `[Q(ζ_e):Q(θ)]=q−1`, the only `Q(θ)`-relation among `1,ψ,…,ψ^{q−1}` is their sum; hence all `β_b` are equal. Each `β_b` is `0` or a single term `W(r_b)θ^{r_b}`. If one is `0` all are and `W=0`; otherwise equal moduli give equal `W(r_b)` and equal arguments give `θ^{r_b}` equal, i.e. `r_b≡r_{b'} (mod f)`. ∎

**Lemma 6 (unit transport).** For a unit `u` of `Z_m`, `c'_x=c_{u^{−1}x}`, `q'_x=q_{u^{−1}x}` satisfy (W) with `V'=uV`; `V'` is a selector because `u` is odd and so `ug≡g (mod 2g)`. Cyclotomic vanishing orders are preserved. (A bookkeeping automorphism of the projected profiles, not a dilation of the original sets.)

## 5. Theorem G: the original gcd g=21 is impossible

*Proof.* `m=42`, antipode `r↔r+21`. Lemma 3: `ε_8=1` (`c_29>0`) and `ε_3≠ε_11`. In both cases the free antipodal pairs are `{2,23},{5,26},{6,27},{19,40},{20,41}`.

**Case I: `D={0,3,29,32}`.** Translates `0+S`, `3+S={3,4,10,16,17}`, `29+S={0,1,29,30,36}`, `32+S={3,4,32,33,39}`; `F={0,1,3,4,7,10,13,14,16,17,29,30,32,33,36,39}`; certainly outside `V`: `O={8,9,11,12,15,18,21,22,24,25,28,31,34,35,37,38}`. Testing all residues, the only possible `c`-residues are `0,3,29,32` and `6[needs 6,19,20]`, `13[20,26,27]`, `16[23]`, `19[19,20,26]`, `26[26,27,40]`.
* Row 2 (if `2∈V`): `2−i` over these `i` is `2,41,15,12,31,28,18,38,25`; `2∉B` (`2+29≡31∈O`), `41∉B` (`41+29≡28∈O`), the rest lie in `O`. Empty: `23∈V`.
* Row 5 (if `5∈V`): `5,2,18,15,34,31,41,28` (`26` is then absent); `5∉B` (`5+3=8∈O`), `2,41∉B`, rest in `O`. Empty: `26∈V`.
* Row 41 (if `41∈V`): `41,38,12,9,28,25,15,35,22`; `41∉B`, rest in `O`. Empty: `20∈V`.
* Row 40 if `6,40∈V` (so `19,27∉V`): `0→40` needs `27`; `13,26` need `27`; `6,19` need `19`; `3→37`, `29→11`, `32→8`, `16→24` are in `O`. Empty.
So `V=F∪{20,23,26}∪X` with `X∈{{6,19},{27,19},{27,40}}`. Apply Lemma 6 with `u=13` (`13·{0,1,7,13,14}≡{0,13,7,1,14}=S`). Then `13F∪13{20,23,26}=[−4,14]` and `13·6≡−6`, `13·19≡−5`, `13·27≡15`, `13·40≡16`, so `V'=[α,α+20]` is an interval with `α∈{−6,−5,−4}`, and the forced `C` residues become `13D≡{0,−3,−1,−4}`. As `S'=S⊂[0,14]`, `c'_i>0` forces `i∈[α,α+6]`; `q'_j>0` with `c'_{−4},c'_0>0` forces `j∈[α+4,α+20]`. Put `C̃(X)=Σ_{i=0}^6c'_{α+i}X^i`, `Q̃(X)=Σ_{j=0}^{16}q'_{α+4+j}X^j`. Their product has exponents `0..22`, which are distinct modulo 42, so (W) is the exact identity in `Z[X]`:
`C̃(X)Q̃(X)=L·X^{−α−4}(1+X+⋯+X^{20})=L·X^{−α−4}Φ_3Φ_7Φ_21.`
By unique factorization (Gauss), `C̃=aX^{e_1}Π_I`, `Q̃=bX^{e_2}Π_{I'}` with `I⊔I'={Φ_3,Φ_7,Φ_21}` (degrees `2,6,12`). `deg C̃≤6` and `deg Q̃≤16` force `4+e_2≤deg Π_I≤6−e_1`, so `Π_I=Φ_7` and `Q̃=bX^{e_2}Φ_3Φ_21=bX^{e_2}(1+X^7+X^{14})`. Then `supp q'` has three elements, but it contains the five distinct tail residues `S'`. Contradiction.

**Case II: `D={0,11,24,29}`.** Translates `0+S`, `11+S={11,12,18,24,25}`, `24+S={24,25,31,37,38}`, `29+S={0,1,29,30,36}`; `F={0,1,7,11,12,13,14,18,24,25,29,30,31,36,37,38}`; outside: `O={3,4,8,9,10,15,16,17,21,22,28,32,33,34,35,39}`. Complete candidate lists (conditions in brackets):
`A`: `0,11,24,29`, `5[5,6,19]`, `6[6,19,20]`, `12[19,26]`, `13[20,26,27]`, `23[23]`, `30[2]`, `40[40,41,5]`, `41[41,6]`;
`B`: `0,1,7,13,14,25,31`, `2[2,26]`, `12[23,41]`, `18[5]`, `19[19,6]`, `20[20,2]`, `36[5,23]`, `37[6,19]`, `38[20]`.
* Row 27 (if `27∈V`): the only candidate pair is `(13,14)`, so `20,26∈V`.
* Row 40 (if `40∈V`): the only candidate pair is `(40,0)`, so `41,5∈V`.
Hence exactly three groups: (G1) `27,26,20,19∈V`; (G2) `6,19∈V`, the other three pairs free; (G3) `6,40,41,5∈V`. In every group the `C` support superset has exactly one residue in each class mod 7 — G1: `{0,11,24,29,12,13}∪{23|30}`; G2: `{0,11,24,29}∪{5|12}∪{6|41}∪{30|23}`; G3: `{0,11,24,29,40,41}∪{23|30}` — with residues mod 7 `0,4,3,1` and the remaining three covering `5,6,2`.
* *`Φ_7∤C` in all groups.* By Lemma 5 (`f=1`) `Φ_7|C` would make `c=γ·1_A` on the seven residues. Row 29 is then `γ(q_0+[q_18 if 18∈B]+[q_31 in G3])` (every other `29−i` lies outside `B`), while row 0 contains these same terms (`(0,0)`, `(24,18)`, `(11,31)`) plus `γq_13` from `(29,13)`. Both rows equal `L`, so `q_13=0`: contradiction. Hence by Lemma 1, `Φ_7|Q`.
* G1: `B={0,1,7,13,14,25,31,38}∪{2,20}` has no residue `5 mod 7`; G3: `B={0,1,7,13,14,18,25,31}∪{12,36}` has no residue `2 mod 7`. A profile vanishing at a residue cannot be constant positive, so `Φ_7∤Q`: contradiction.
* G2: the `C` residues are all `≡0,2 (mod 3)`, so the `C` profile mod 3 vanishes at `1` and `Φ_3|Q` (Lemma 1). By Lemma 5 with `e=21,q=7,f=3`: the `C` profile mod 21 has one residue per class mod 7, but `0` and `11` differ mod 3, so `C(ζ_21)≠0` and `Q(ζ_21)=0`. Thus `Q` vanishes at every divisor `3,7,21` of `g`, contradicting Lemma 4.
Both cases fail; `g≠21`. ∎

## 6. Theorem H: the original gcd g=22 is impossible

*Proof.* `m=44`, antipode `r↔r+22`. Lemma 3: `ε_8=1` (`c_30>0`), `ε_3≠ε_11`. Free antipodal pairs in both cases: `{5,27},{6,28},{19,41},{20,42}`.

**Case I: `D={0,3,30,33}`.** Translates `0+S`, `{3,4,10,16,17}`, `30+S={0,30,31,37,43}`, `33+S={2,3,33,34,40}`; `F={0,1,2,3,4,7,10,13,14,16,17,30,31,33,34,37,40,43}`; outside `O={8,9,11,12,15,18,21,22,23,24,25,26,29,32,35,36,38,39}`. Complete candidates: `A`: `0,3,30,33`, `6[6,19,20]`, `27[27,28,41]` (at most six residues); `B`: `0,1,4,7,10,13,14`, `16[5,19]`, `17[6,20]`, `27[27]`, `28[28]`, `30[19]`, `31[20]`, `41[27,41]`, `42[28,42]`.
A constant positive `C` profile mod 11 needs eleven residues, so `Φ_11∤C`, and Lemma 1 gives `Φ_11|Q`. The listed `B` residues mod 11 are single except the pairs `{16,27}`, `{17,28}`, `{30,41}`, `{31,42}`; Lemma 2 (`k=1`) gives
`q_0=q_1=q_4=q_7=q_10=q_13=q_14=q_16+q_27=q_17+q_28=q_30+q_41=q_31+q_42=:κ>0.`
Complete rows: 4 `{(0,4),(3,1)}`; 1 `{(0,1),(3,42)}` (`42` only if `42∈V`); 43 `{(30,13),(33,10)}`; 2 `{(33,13),(30,16)}` (`16` only if `5∈V`). Rows 4 and 1 give `κc_3=c_3q_42`, so `42∈V`, `20∉V`, hence `6∉V` (`6∈V` needs `20` for row 6 to be nonempty: its only candidates are `(33,17)` and `(6,0)`); rows 43 and 2 give `κc_30=c_30q_16`, so `5∈V`, and row 5 (only candidate `(33,16)`) needs `19∈V`. Thus `V=F∪{5,19,28,42}`, `A={0,3,30,33}`, `B={0,1,4,7,10,13,14,16,28,30,42}`. Row 16 is `{(0,16),(3,13),(30,30)}` (`27∉V`), so `L=κ(c_0+c_3)+c_30q_30`; with row 4 (`L=κ(c_0+c_3)`), `q_30=0`. As `41∉V`, the class `8 mod 11` of `Q` has mass `q_30=0≠κ`. Contradiction.

**Case II: `D={0,11,25,30}`.** Translates `0+S`, `{11,12,18,24,25}`, `25+S={25,26,32,38,39}`, `30+S={0,30,31,37,43}`; `F={0,1,7,11,12,13,14,18,24,25,26,30,31,32,37,38,39,43}`; `O={2,3,4,8,9,10,15,16,17,21,22,23,29,33,34,35,36,40}`. Complete candidates: `A`: `0,11,24,25,30,31`, `5[5,6,19]`, `6[6,19,20]`, `12[19]`, `13[20,27]`, `18[19]`, `37[6]`, `42[42,5]`, `43[6]`; `B`: `0,1,7,13,14,26,32`, `19[19,5]`, `20[20,6]`, `38[5,19]`, `39[6,20]`.
* Row 28 (if `28∈V`): `28−i` is `28,17,4,3,42,41,23,16,15,10,30` over the available `i`; `28,42,41,30∉B` (`28+25≡9`, `42+11≡9`, `41+11≡8`, `30+30≡16` lie in `O`), the rest lie in `O`: empty, so `6∈V`. Row 41 (if `41∈V`): empty likewise, so `19∈V`. Row 27: only `(13,14)`, so `27⇒20`. Row 42: only `(42,0)`, so `42⇒5`.
* `(5,42)`: no `A` candidate is `≡6 (mod 11)` and `B` has no residue `6,9 (mod 11)`; `(27,20)`: no `A` candidate `≡5` and `B` misses `5,8`. Neither profile is constant mod 11, contradicting Lemma 1.
* `(5,20)`: `V=F∪{5,6,19,20}`, `A={0,5,6,11,12,18,24,25,30,31,37,43}`, `B={0,1,7,13,14,19,20,26,32,38,39}`. Rows 11 and 14 are complete singletons (`11−i`, `14−i` meet `B` only at `0`, resp. `14`): `L=c_11q_0=c_0q_14`. Row 0 contains `(0,0),(30,14)`: `L>c_0q_0`, so `q_14>q_0`. Row 25 contains `(11,14),(25,0)`: `L>c_11q_14`, so `q_0>q_14`. Contradiction.

Both cases fail; `g≠22`. ∎

## 7. Lift rigidity and the forbidden-difference lemma

**Lemma 7 (lift rigidity).** (i) If `u,w∈V` and `u≡w (mod g)`, then `u=w` in `Z_{2g}`. (ii) Hence if `x∈supp c`, `s∈S`, and `y∈supp c` (or any `y∈V`) satisfies `y≡x+s (mod g)`, then `y=x+s`; likewise if `y∈supp q`, `a∈supp c` and `z∈V` with `z≡y+a (mod g)`, then `z=y+a`. (iii) If `g=s+s'−s''` with `s,s',s''∈S`, then no `x,y∈supp c` satisfy `y≡x+s (mod g)`.

*Proof.* (i) `V` is a selector. (ii) `x+s∈V` because `c_xq_s>0`; apply (i). (iii) By (ii) `y=x+s`; then `y+s'∈V` and `x+s''∈V` differ by `s+s'−s''=g`, an antipodal pair. ∎

For `18≤g≤28` the representations are `20=7+13−0=7+14−1`, `21=7+14−0`, `25=13+13−1`, `26=13+13−0=13+14−1=14+13−1`, `27=13+14−0=14+13−0=14+14−1`, `28=14+14−0` (and prime `19`); so the forbidden `C`-differences mod `g` include `13` for `g=25`; `13,14` for `g=26,27`; `14` for `g=28`.

## 8. Theorems I–K: the original gcds g=25, 26, 27 are impossible

**Theorem I (`g=25`).** By Lemma 1 at `e=25`, `Φ_25|Q` or `Φ_25|C`. If `Φ_25|Q`, Lemma 2 makes the `Q` profile mod 25 constant on the classes mod 5; `S≡{0,1,2,3,4} (mod 5)`, so every residue mod 25 carries `Q` mass and `supp q` meets every antipodal class of `Z_50`, contradicting Lemma 4. If `Φ_25|C`, the fibre `{3,8,13,18,23}` of the anchor residue `a_3≡3` has constant positive mass, so some `y∈supp c` has `y≡13 (mod 25)`; with `0∈supp c` this contradicts Lemma 7(iii) (`25=13+13−1`). ∎

**Theorem J (`g=26`).** `m=52`; forbidden `C`-differences mod 26: `13,14`.
1. `Φ_13∤C`. Otherwise every class mod 13 carries `C` mass; as difference 13 is forbidden, `supp c mod 26` is `{r+13θ(r): 0≤r≤12}` with `θ(0)=0`. Consecutive classes differ by `1+13(θ(r+1)−θ(r))`, which must avoid `14`, so `θ≡0`; but then `12` and `0` satisfy `0≡12+14 (mod 26)`, forbidden.
2. `Φ_26∤C`. The `C` profile mod 26 has at most one residue per class mod 13 (difference 13 forbidden). By Lemma 5 (`e=26,q=13,f=2`), vanishing at `ζ_26` would force thirteen residues all of one parity, hence all even (they contain `0`); but `a_3≡3 (mod 26)` is odd.
3. By Lemma 1, `Q` vanishes at `ζ_13` and `ζ_26`. Then the Fourier transform of the `Q` profile on `Z_26` is supported on the characters of order `1,2`, so the profile is constant on each parity class; `q_0,q_1>0` make it positive everywhere, so `supp q` meets every antipodal class: Lemma 4 contradiction. ∎

**Theorem K (`g=27`).** `m=54`, antipode `x↔x+27`; write `a_3=3+27ε_3`, `a_8=8+27ε_8`, `a_11=11+27ε_11` (Lemma 3 gives no constraint).
1. `Φ_27∤C`: otherwise (Lemma 2) the `C` profile mod 27 is constant on fibres `{r,r+9,r+18}`, so residues `12` (fibre of `a_3`) and `26` (fibre of `a_8`) carry mass; `26≡12+14`, forbidden by Lemma 7(iii) (`27=14+13−0`). Hence `Φ_27|Q`: the `Q` profile mod 27 is constant on the fibres `{0,9,18},{1,10,19},{7,16,25},{4,13,22},{5,14,23}`, all positive; each such residue `r` has a unique lift `ℓ(r)∈V`.
2. Lemma 7(ii) from exact tail elements: `1+a_3`, `1+a_8`, `13+a_3`, `14+a_8`, `14+a_11` give `ℓ(4)=4+27ε_3`, `ℓ(9)=9+27ε_8`, `ℓ(16)=16+27ε_3`, `ℓ(22)=22+27ε_8`, `ℓ(25)=25+27ε_11`.
3. `ℓ(22)+a_8≡30∈V` and `a_3∈V` are both `≡3 (mod 27)`, so `a_3=30`, `ε_3=1`. `ℓ(25)+a_11≡36∈V` and `ℓ(9)∈V` are `≡9`, so `ε_8=1`. `ℓ(16)+a_11=27(1+ε_3+ε_11)∈V` and `0∈V` are `≡0`, so `ε_11=0`. Thus `a_3=30`, `a_8=35`, `a_11=11`.
4. Residue 5 carries `Q` mass (fibre of `14`). If `ℓ(5)=5`, then `5+a_8=40∈V` is antipodal to `13∈V`; if `ℓ(5)=32`, then `32+a_3≡8∈V` is antipodal to `a_8=35∈V`. Contradiction. ∎

## 9. Combined statement, conditional imports and exact remaining boundary

**Proved here from §0 alone (no imported body):** Lemmas 1–7 and the exclusions `g≠18,20,21,22,25,26,27` (Theorems E–K). Lemma 4 is an all-`g` statement: the annihilation pattern of `C,Q` on the divisors `e>1` of `g` can never be one-sided.

**Combined statement (conditional imports at their stated scopes).** If one additionally imports S5 Theorem A / S6 Theorem 1 (every prime `g` excluded; both bodies are in the packet and Lemma 4 above re-derives it), S7/S8 (`g=15,16`, bodies in the packet) and the S2/S6 small-gcd scope (`g≤14`; S6 §3 displays a reconstruction, S2's own fourteen-case support/checker bodies are not in the packet), then every remaining actual two-point direct factor has **composite `g≥24`, `g∉{25,26,27}`**, the first open values being `24,28,30,32,33,34,35,36,…`, in addition to the S5/S6 spectrum families (gcd tests (6)–(8), not re-proved here).

**Exact residual system for each remaining `g`.** After §0 normalization, a remaining `g` survives only if there are a selector `V⊂Z_{2g}`, a sign vector `(ε_3,ε_8,ε_11)` obeying Lemma 3 (for `g=23,24,25`: `ε_11=1`; for `g≥26`: none), and nonnegative integers `c_i` on `A(V)`, `q_j` on `B(V,D)` with `c_0,c_{a+ε_ag},q_s>0` (`s∈S`) satisfying (W) on every row (all incidences, occupied and unoccupied), and for every `e|g, e>1` the alternative `c(ζ_e)=0` or `q(ζ_e)=0`, with Lemma 2/5 making each prime/prime-power alternative an explicit linear fibre system and Lemma 4 forbidding one-sided annihilation. This system is finite for each fixed `g` (2^g selectors at most) and independent of `n` except through the positive integer `L`. It is a necessary system, not a tiling construction; the original difference-spectrum tests of S5/S6 remain separate necessary conditions on `n,d`.

**Not established.** The listed values `24,28,30` and every composite `g≥32` remain open here; for `g≥26` Lemma 3 imposes nothing, Lemma 7(iii) applies only up to `g=28`, and the hand case analysis grows with the number of free antipodal pairs. No statement is made about heads without a two-point direct factor, about existence of any anchored tiling, the RSS/pure-letter bridge, printed-source correspondence, finite maximal completion, novelty or priority. The anchors alone do not force the factor.

## 10. Read, process and execution declarations

* Before any packet body or task mathematics I read completely the f894 manifest, freeze receipt, final pre-dispatch binding, parent-live-metadata supply, `actual-dispatch-receipt-v1.json` (one long line recovered raw) and all 22 listed status-only controls (raw, windows of at most 20 LF, endings included). I wrote `prebody-ack-v1.md` and sent a direct PREBODY ACK to Main (delivered) before opening any packet part. Controls were used for status/permissions only; all genuine held episodes and all their consumers remained NONINPUT. No cognition certificate is claimed.
* Part 01 (stated 87,886 B, 882 LF) was then read serially in raw windows `1–20, 21–40, …, 841–860` (every window exactly 20 LF) and `861–882`. **Process deviation:** that last request spanned 22 LF, two over the 20-LF cap (display complete, far below 30,000 bytes, no clipping); I immediately re-read it as `861–880` and `881–882`. Part 02 (stated 41,299 B, 633 LF) was read only after part 01, in raw windows `1–20, …, 601–620, 621–633`. No display was clipped; no long line needed recovery. This covers S1 1–20, S2 1–51, S3 1–31, S4 1–20, S5 1–278, S6 1–280, S7 1–172 (part 01) and S8 1–129, S9 1–494 (part 02). No link in any source was followed and no unlisted file was opened. Hashes are the parent-supplied pins (part01 `d98b7b78…56dc`, part02 `7b15b028…b127`, S1–S9 as in the manifest), not recomputed here.
* No network, external model, code preparation, code execution, scientific eval, test, compilation, solver or child subprocess was used; S9 was read as text only and not run. There is no prepared-code hash. All support lists, incidences and cyclotomic arguments above are handwritten author mathematics needing disjoint checking and parent disposition. The selected numerical cases (`g=18,20,21,22,25,26,27`, the unit `13 mod 42`, and the case splits they generate) are named by, or arise inside, the frozen research statement.
* The 20-LF window cap was applied to the packet parts and the 22 controls. The five administrative JSON files were read in larger raw displays (each a complete file or block below 30,000 bytes, after an initial formatted display that elided entries); these are status files, not mathematical inputs.
* This file was composed incrementally (several appends to the same new file) within this single undelivered authoring episode; no frozen, delivered or previously written candidate was edited.
