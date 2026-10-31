# info-6: one consolidated necessary-condition theorem for balanced nine-variable peak ≤28

Owner **InfoBalancedNL242-2-2**, original info-6 slot. Native `/bin/date` observed immediately before writing: **2026-10-27T17:26:00-0700 PDT**. **CONSOLIDATED AUTHOR UNION, UNREVIEWED AS A UNION AND NOT ADOPTED.** The parent-adopted premises below retain only their exact earlier same-harness written-support scope and mandatory corrections. All other clauses are author claims for one prospective full-scope disjoint review, not individually adopted results. Earlier w43b, w68, w74, w81 and w91 review activity is identified where relevant; it is not blanket union acceptance or a clean-cognition certificate.

## 1. One theorem, one actual object, all alternatives

Let f:F₂⁹→{0,1} be **any actual** balanced Boolean function with |W_f(a)|≤28 for every a, s(x)=(−1)^{f(x)}, k(a)=W_f(a)/4, and T=⊕_{f(x)=1}x. Let K=T^⊥, H={a:a·T=1}, S={a:|k(a)|=7}, n=|S|, and N_j=#{a:|k(a)|=j}; for odd j write n_j=N_j. Every assertion below concerns this **same f and same full 512-entry array**. The theorem is conditional: no such f is asserted to exist. All ranks, weights and the original `(24,24,2)` alternative remain included.

### 1A. Previously adopted base, cited without re-derivation

1. **Exact caller and mod-4 coupling [P1].** k is integer, k(0)=0, |k|≤7, and Σ_a k(a)k(a+b)=2¹⁴·1_{b=0} for every b. Conversely those full integer equations, zero frequency and bound recover an actual balanced Boolean function. There is one symmetric F₂-bilinear form 𝔅 with 𝔅(a,a)=a·T and k(a+b)−k(a)−k(b)≡2𝔅(a,b) (mod 4); k(a) mod 2=a·T.
2. **Peak and energy [P2].** T≠0; H has 256 odd coefficients and K has 256 even coefficients; n=n₇≥92. For every direction the two frequency-half square energies have the parent-stated divisibility, and Σ_{a∈H}k(a)²≥8576. The coupled-count correction [Ecount] is mandatory: use the actual complementary count, not an independent upper bound.
3. **Peak phase and one cube [P3].** On H, Q(a)=(k(a)−1)/2 mod 2 is a quadratic phase with polar 𝔅 restricted to K; a peak sign is −(−1)^{Q(a)}. S contains an affine peak 3-flat, and every such 3-flat has sign product +1.
4. **Saturated flats [P4, Ew44].** Any full |W|=28 affine frequency d-flat has d≤5. Its sign pattern is either an affine character, or has four oriented local coefficients of magnitude 14 on an affine quotient 2-flat with sign product −1; the first alternative has one oriented local coefficient of magnitude 28. The polar radical on the flat direction is respectively the whole direction or has dimension d−2. For d=5 only the four-label case is possible. The adopted constant-magnitude odd-divisor bounds also apply at their stated exact scope. The w44 orientation character and normalization corrections [Ew44] are mandatory.

### 1B. Further common-spectrum necessary conditions [AUTHOR UNION]

5. **Full histogram and signs.** For this f,

       Σ_a k(a)^4 ≡0 (mod 256),     Σ_a k(a)^4≥532480,
       N₂+N₆+5N₃+7N₅+6N₇≡0 (mod 16),
       n₇−n₁ ≥ 2⌈(272+2n₃)/6⌉ ≥92,       92≤n₇≤234.             (2)

For every x∈V, each of {a:k(a)χ_a(x)>0} and {a:k(a)χ_a(x)<0} contains at least 165 points. For every b≠0, among unordered nonzero-support pairs {a,a+b}, at least three have positive product and at least three negative if b·T=0; at least five of each sign if b·T=1.

6. **Peak-flat supersaturation.** If G counts all affine peak 3-flats, then

       21G ≥ 8 binom(n,2)−255·127,       G≥53.                    (3)

Some peak belongs to at least five peak 3-flats with distinct directions, and at least six of their weight-8 sign-check incidence vectors are linearly independent. If S lies in an affine 7-flat, it contains at least

       ⌈[binom(n,2)−4064]_+/15⌉ ≥9

full peak 4-flats; otherwise S affinely spans H. Products of signs on every full peak 3- or 4-flat are +1. The ≥53 argument is the author claim associated with w43b, not a parent adoption merely because that review returned.

7. **Every fully peak 5-flat has a local defect pattern.** For each E=a₀+J with dim J=5 and |W|=28 throughout, let U=J^⊥. Among the 32 affine U-cosets exactly four, whose labels form an affine 2-flat, have a local affine slope a₀|_U at distance one from f; each has one differing truth bit and 7 or 9 ones. The other 28 have distance 8 from either affine constant and an even number of ones. The four coherently oriented nonzero local coefficients have product-sign −1. This is a frequency-5-flat condition on source **4-flats**, distinct from and not derived from the excluded truth-5-flat occupancy file.

8. **All odd signs from one magnitude profile.** For an arbitrary a₀∈H and h∈K define

       q(h)=1_{|k(h)|∈{2,6}},    m(h)=|k(a₀+h)|,
       ρ(m)=(−1)^{(m−1)/2},     ε(h)=sgn k(a₀+h).

There is one affine binary function c+L(h) such that ε(h)=ρ(m(h))(−1)^{q(h)+c+L(h)} for every h. Conditional on a fixed full magnitude profile, its 256 odd signs obey exactly 247 independent phase-skeleton equations and have at most 512 patterns. If the profile is realized by an actual f, all 512 patterns are realized by translations and output complementation, each by exactly two translation/complement parameter pairs; no even-sign or full-function uniqueness follows.

For every b∈K\{0}, label each unordered odd pair {h,h+b} by λ_b=ρ(m(h))ρ(m(h+b))(−1)^{q(h)+q(h+b)} and let A_b^τ be the complete class with λ_b=τ∈{±1}. Necessarily, for both classes and every b,

       Σ_{{h,h+b}∈A_b^τ} [m(h)+m(h+b)]² ≤ 2¹⁴.                (4)

A change of the arbitrary origin can swap the two labels, not their conjunction. This is a magnitude-only obstruction, not sufficiency for an actual spectrum.

9. **Global polar radical.** Let R₀=rad(𝔅|_K), r=dim R₀, and e_b=|S∩(S+b)|/2. Every nonzero b∈R₀ has e_b≤83. Consequently n≥212 implies R₀={0}. For the peak occupancies p_i of all N=2^{8−r} affine R₀-cosets of H,

       Σ_i binom(p_i,2)≤83(2^r−1),
       n²/N−n≤166(2^r−1).                                      (5)

Both radical alternatives remain open.

10. **Every balanced two-bit exchange.** For every f(x)=1, f(y)=0, d=x+y≠0, the exchange f^{x,y} preserves the peak bound iff

       sgn W_f(a)=−χ_a(x) for every a∈S with a·d=1.             (6)

Let S_d={a∈S:a·d=1}; let X_d be the solution set of these sign equations. It is nonempty iff Π_{a∈R}[−sgn W_f(a)]=1 for every R⊆S_d with ⊕_{a∈R}a=0; when nonempty dim X_d=9−dim span(S_d). An actual neighbor additionally requires f(x)=1 and f(x+d)=0. Let R_* be the span of the one-dimensional radicals of **all** non-affine-sign peak 3-flats, or zero if there are none. Every preserving exchange has d∈R_*^⊥. If deg(f) counts all such distinct two-bit neighbors, then

       deg(f) ≤ [2^{8−dim R_*}Σ_{a∉R_*}k(a)²−Σ_{a∈H}k(a)²]/64. (7)

In particular R_*=K would imply isolation; it is not asserted. For d∉{0,T}, if |S_d|>64 then X_d is empty or a two-point affine set of direction T+d. If |S_d|>96 and X_d is nonempty, 𝔅 vanishes on K∩d^⊥ and factors as (u·d)L(v)+(v·d)L(u) for some linear L on K. No active direction or exchange is asserted to exist.

11. **Odd-divisor flat obstruction.** For any Boolean function on F₂⁹, odd m≥1, and every affine frequency d-flat with d≤8, if all its Walsh coefficients are divisible by m, then either they are all zero or 2m≤2^{9−d}. For d=9 and m>1, a common divisor m is impossible. In particular every frequency flat of dimension ≥6 containing a |W|=28 coefficient also contains a nonzero coefficient not divisible by 7, hence not a peak. This variable-magnitude statement is an author generalization, not part of P4's constant-magnitude adoption.

12. **Equivalent code and all dual indices.** Original existence is equivalent to an actual binary [256,9] code with 256 distinct nonzero generator columns and **every** nonzero word weight in [121,135]. For any such code let A_t count words of weight 128+t, −7≤t≤7, let D_j count dual words of weight j, and define

       K_j(w)=Σ_i(−1)^i binom(w,i)binom(256−w,j−i).

Every original witness gives, simultaneously for all 0≤j≤256,

       ΣA_t=511,  ΣtA_t=128,  Σt²A_t=16384,
       Σ_{t odd}A_t=256,  Σ_{t even}A_t=255,
       A_{−7}+A_7≥92,  512D_j=binom(256,j)+ΣA_tK_j(128+t),
       D₁=D₂=D₂₅₆=0,  5296≤D₃≤5594,  30≤D₂₅₄≤71,
       0≤D₂₅₅≤11,
       (A₃−A₋₃)+5(A₅−A₋₅)+14(A₇−A₋₇)≡0 (mod 8).             (8)

For arbitrary integer A_t, the divisibility of **all** 257 dual numerators by 512 is equivalent to just the 15 simultaneous coefficient congruences

       Σ_{t=−7}^7 A_t(1−z)^{7+t}(1+z)^{7−t}
          +(1−z²)^7+256z(1−z²)^6 ≡0  (mod 512),                 (9)

in degrees 0,…,14. This equivalence handles divisibility only; all D_j≥0 and actual code/Boolean realization remain separate. W81 reconstructed the source claims 0F/0M/0m; it did not establish method noninfluence or parent-adopt the new union clauses.

## 2. Proof of author-union clauses; adopted base is cited, not re-derived

### 2A. Histogram, signs and shifts

The cited parent [P2] gives odd energy E_H≥8576 and divisibility by 128. Since the odd counts sum to 256, E_H=6400+24(n₇−n₁)−16n₃; hence 3(n₇−n₁)−2n₃ is a multiple of 16 at least 272. In particular n₇−n₁ is even, proving the gap in (2).

For the upper bound let C=H\S, c=|C|. By P4 no affine 6-flat in H is entirely peaks, so C meets every affine 6-flat. Every affine hyperplane of H therefore meets C in a spanning set of at least eight points on each side. With t=c−16≥0, every nontrivial character sum of 1_C has magnitude at most t. If r(v)=#{(x,y)∈C²:x+y=v}, then r(0)=c, all other r(v) are even, and Σ_v r(v)²≥3c²−2c. Orthogonality and Parseval give

       256(3c²−2c) ≤ c⁴+t²(256c−c²).

Substitution c=16+t reduces this to 3t³+48t²−80t−1280≥0. For 0≤t≤5, t³≤5t²≤25t, making the left side at most 235t−1280<0. Thus c≥22 and n≤234. This is additive-combinatorics Fourier analysis of the peak **set**, not a transform of the stopped frequency sectors.

For global fourth moments, put C_f(b)=Σ_x s(x)s(x+b) and J(b)=C_f(b)/8. The cited parent full count identity makes J integral; Σ_bJ(b)=0 and J(0)=64. Whole-array character orthogonality gives Σ k⁴=128Σ J². Because ΣJ²≡ΣJ=0 mod 2, the fourth moment is divisible by 256; because Σ_{b≠0}J(b)²≥|Σ_{b≠0}J(b)|=64, it is at least 128(4096+64). Reduction modulo 256 using the parent odd count 256 gives the histogram congruence in (2).

For every x, the Boolean inverse gives Σ_a k(a)χ_a(x)=±128. The odd coefficients have energy at most 256·49, so even energy is at least 3840; hence Σ|k|≥(2¹⁴−E_even)/7+E_even/6≥2432. The positive and negative modulated masses are each at least (2432−128)/2=1152, so each needs at least ⌈1152/7⌉=165 nonzero terms. For shifts b, energy forces at least 107 nonzero even coefficients, and all 256 odd coefficients are nonzero. If b·T=1 there are at least 107 nonzero unordered b-pairs, with product magnitudes in [2,42]; if b·T=0 there are at least 128, with magnitudes in [1,49]. Full zero-shift autocorrelation balances total absolute positive and negative products. Thus each sign class has at least respectively ⌈107/22⌉=5 or ⌈128/50⌉=3 pairs.

### 2B. Peak-flat counting and source defects

A universal auxiliary lemma is: a subset of F₂⁷ with distinct sums of all unordered distinct pairs has at most 15 points. If it had 16, its 120 pair sums would miss seven nonzero points D. Character orthogonality gives Â(ξ)²=14−2D̂(ξ) for nonzero ξ; parity and first/second moments force D̂-values 7,5,−1 with counts satisfying A₇+A₅+A₋₁=127, 2A₇+A₅=30, 4A₇+3A₅=60. Thus D is exactly the nonzero part of a 3-subspace, and the 16 points form a transversal of its cosets. Writing the transversal as a graph F₂⁴→F₂³, each nonzero input difference has all eight output differences twice; every nonzero output character then has zero nontrivial autocorrelation and transform magnitude 4. Output inversion would give 2N_y=4+Σ_{λ≠0}ε_λ(−1)^{λ·y}, even on the left but odd on the right. Contradiction. This is a universal abstract-set argument, not a selected Boolean object or stopped sector representation.

For every nonzero b∈K let e_b count complete b-pairs in S. In K/⟨b⟩ there are 127 nonzero difference directions. The lemma and collision counting imply the number G_b of pairs (2-direction containing b, peak 3-flat) is at least max{0,8e_b−127}. Every peak 3-flat contributes 21 such pairs and Σ_be_b=binom(n,2), proving (3). From (3), G>n/2 for every n≥92; incidences then give a peak in at least five cubes. Their incidence vectors give ≥53 distinct nonzero valid sign checks, so their span has dimension at least six. P3 supplies each + sign product.

For the conditional 7-flat claim, a 3-flat-free subset of affine F₂⁶ has at most 32 points: quotient complete pairs by any nonzero b, use distinct pair differences in a 5-space, and sum over 63 directions. In an affine 7-space, complete b-pairs form such a 6-space quotient; a 3-flat there lifts to a 4-flat. Repeated application of the 32-point bound supplies at least (e_b−32)_+ different lifted flats. Summing over the 127 directions proves 15G₄≥binom(n,2)−4064. The full-span alternative and 4-flat sign product follow as stated.

For clause 7, cite P4 with Ew44: on a fully peak 5-flat the oriented local coset coefficients are four ±14 on an affine quotient 2-flat and 28 zeros. Each source U-coset has 16 points. The ordinary local Hamming identity converts |C|=14 into distance one to one affine constant at slope a₀|_U, and C=0 into distance eight to both. Since J⊆K but a₀∈H, this local slope is nonzero; its affine functions have eight ones, giving 7 or 9 on each active coset and an even number on an inactive one. No source cell or truth 5-flat is selected.

### 2C. Magnitudes, radical and exchanges

For q,m,ρ as in clause 8, the adopted global mod-4 identity gives (k(a₀+h)−1)/2=q(h)+c+𝔅(a₀,h) mod 2. The identity sgn k=ρ(|k|)(−1)^{(k−1)/2} for every odd allowed value proves the common affine-character law. The vector space of affine binary functions on the eight-dimensional K has dimension 9; its 256 evaluations therefore impose 247 independent phase-skeleton equations. Conversely vanishing all affine 2-flat second differences gives an affine phase, but does not realize an actual spectrum. The translation/complement action multiplies the odd signs by every affine character on K; the linear parameter map F₂¹⁰→Aff(K) is onto with kernel size two.

For (4), within either λ_b class every pair product has one common sign. The full zero autocorrelation at b partitions all 512 coefficients into unordered pairs; the remainder must compensate the class. Applying |uv|≤(u²+v²)/2 to all other pairs and total energy 2¹⁴ gives (4). This argument uses the whole array; no complementary-sector transform is formed.

For b∈R₀\{0}, the polar restriction vanishes, so the odd peak phase derivative in direction b is constant. All e_b peak-pair products therefore have one sign. They contribute magnitude 49e_b and consume energy 98e_b; the remaining pairs can compensate at most (2¹⁴−98e_b)/2. Thus 98e_b≤8192, giving e_b≤83. Since e_b≥n−128, n≥212 forces R₀=0. Summing e_b over nonzero b∈R₀ counts all within-coset peak pairs once and gives (5), with Cauchy for the second inequality.

For an exchange, the Walsh change is exactly 2[χ_a(x)−χ_a(y)]. On active frequencies its magnitude is 4; nonpeak coefficients are multiples of 4 and have magnitude at most 24, so only peaks constrain the bound, proving (6). The X_d consistency criterion is the usual relation criterion for linear binary equations. On every non-affine peak 3-flat, its local polar form has a unique radical by P4; if d pairs nontrivially with that radical, the active peak plane has nonzero polar form and cannot match the affine phase imposed by (6). Thus d annihilates all such radicals. The cited parent count identity m_d=(1/64)Σ_{a·d=1}k(a)² counts unequal truth pairs, and an actual neighbor has d≠0,T by the adopted nonzero-XOR theorem. Summing m_d over R_*^⊥\{0,T} gives (7). If |S_d|>64, its affine span is the full active 7-flat, so X_d has at most two points; if |S_d|>96, an affine/quadratic phase difference vanishing there is identically zero because a nonzero quadratic on seven bits has weight at least 32. Its second differences give the stated polar factorization.

For clause 11, cite P4's corrected all-affine restriction identity: every coherently oriented source-coset sum is an integer C with 2^d C an integer combination of the flat's Walsh values. If all are divisible by odd m, then m|C. For d≤8 each source coset has even size, so nonzero C has |C|≥2m and at most 2^{9−d}. Inversion on the flat ensures a nonzero flat coefficient gives nonzero C. For d=9, singleton sums are ±1, precluding odd m>1.

### 2D. Code constraints and the all-index divisibility reduction

For the exact code direction, translate the support of an actual hypothetical f by an arbitrary point outside it; all magnitudes are preserved and the resulting 256 support points are distinct nonzero generator columns. For every nonzero message a, W(a)=4(w(aᵀG)−128), so the two-sided peak bound gives the full [121,135] window and rank 9. Conversely such an actual generator gives the entire 512-bit Boolean indicator. These are the exact statements reconstructed by w81, not a claimed actual code.

Character orthogonality on the actual generator gives the three moments and every j identity in (8). Complementing j-subsets gives K_{256−j}(w)=(−1)^wK_j(w). With O_r=Σ_{t odd}t^rA_t, the j=255 and 254 identities yield O₁=128D₂₅₅ and O₂=128(128−D₂₅₄). The even-energy ceiling 36·255 and odd ceiling 49·256 yield 30≤D₂₅₄≤71; two parity-class Cauchy inequalities yield 0≤D₂₅₅≤11. The j=3/253 difference gives O₃−O₁ divisible by 192, hence the signed congruence in (8).

For the sharper D₃ bound set M₃=Σt³A_t and P(t)=(7−t)(t+7)², Q(t)=P(−t). Both are nonnegative for |t|≤7, and at least 13 for every even allowed t because P(t)−13=(t+6)(55−t−t²) and |t|≤6. The 255 even words and the three moments give −50998≤M₃≤63542. The exact third-moment identity M₃=2²¹−384D₃ yields 5296≤D₃≤5594.

Finally let B_A(z)=Σ_t A_t(1−z)^{7+t}(1+z)^{7−t}. The generating polynomial of all dual numerators is P_A(z)=(1+z)^{256}+(1−z²)^{121}B_A(z). In (Z/512Z)[[z]], the second factor is a unit and

       (1+z)^{256}(1−z²)^{−121}
         =(1−z²)^7[(1+z)/(1−z)]^{128}
         ≡(1−z²)^7+256z(1−z²)^6.                              (10)

To prove the congruence, put q=z/(1−z) and expand (1+2q)^{128}; binom(127,k−1) is odd by the binary product Π_{i=0}^6(1+x^{2^i}) modulo 2, so 2^k binom(128,k) is divisible by 512 for k≥3, while the first two nonconstant coefficients are 256 modulo 512. Then q+q²=z/(1−z)²≡z/(1−z²) modulo 2. Thus (9) is equivalent in both directions to every dual numerator being divisible by 512. Positivity and realization are not inferred.

## 3. Full dependency and status table

All SHA-256/LF pins below were observed before this packet. `R` denotes `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/`; `P` denotes `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`. A = exact parent-adopted same-harness written support; U = author-only/unadopted; G = disjoint source gate only. A prior review in flight/returned is not an adoption.

| Key / path | SHA-256 | LF | Status and use |
|---|---|---:|---|
| P1 `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | A: caller and mod-4 |
| `P/info-6-walsh-caller-and-mod4-coupling-parent-coverage-addendum-1.md` | `5f07a05431ed8b33907e63b5d7606d119ed679b95e1bf777b0363bf8cbc88dca` | 9 | A coverage correction |
| P2 `P/info-6-hyperplane-energy-and-92-peak-parent-v1.md` | `89279b361e2d0339d901e2fa7a26195d0ae3d009862a12427292f943dddbdfb6` | 25 | A: energy and ≥92 |
| P3 `P/info-6-odd-half-sign-law-and-forced-peak-3flat-parent-v1.md` | `d1734fa7d22ce34b8c90d2fa65b31490335734220054699b8e9270d423b1e399` | 21 | A: phase/cube |
| P4 `P/info-6-saturated-flat-rigidity-and-odd-divisor-parent-v1.md` | `727e8495c8beeeb9181465e9b8804b61621a4216aca2fa26d41206642e46c4fe` | 25 | A only with Ew44 |
| `R/prerequisite-derivation-v1.md` | `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9` | 87 | A via P1 |
| `R/walsh-support-xor-obstruction-v1.md` | `380655caaa06ea27e4236070ff66e070be63963960efebfabef2e730d2091fc4` | 49 | A T≠0 only with Ecount |
| Ecount `R/walsh-support-xor-coupled-count-erratum-v1.md` | `810e3e55c52288f252b335a776a134752702df33d70d8d689fb009aac127273c` | 30 | Mandatory correction |
| `R/walsh-hyperplane-energy-v1.md` | `6a1000f1c95ef4264e82fba6d229e59393241efaed367ee4d3e5687cec0f88a0` | 49 | A via P2 |
| `R/walsh-peak-multiplicity-v1.md` | `8a64a73bc552f9e71cc04f07159c1f09feab17894d31966c16ebfe80d9fd37b8` | 28 | A via P2/Ecount |
| `R/walsh-odd-half-quadratic-sign-v1.md` | `be6421feeb80f076373e09aaccb4a6ed1401591db892e82fe77c64831aa215e7` | 35 | A via P3; spectral phase only |
| `R/walsh-forced-peak-3flat-v1.md` | `5e56a2b74359a5f36cc8289685d227ff6b3f9248540c009a0e049c7c30e43e45` | 33 | A via P3 |
| `R/walsh-forced-peak-3flat-sign-addendum-v1.md` | `b46d6cc50c83af88d327e3e097b853c9bfb642bbcae9476fc2603aa188ee5cef` | 15 | A via P3 |
| `R/walsh-affine-restriction-coupling-v1.md` | `1c03c02f37f10c5b74e5f81b5c69e56fcf1f02ef02684367e3869856ea84c457` | 43 | A only as used in P4 |
| `R/walsh-saturated-flat-rigidity-v1.md` | `5b26b95d4fb47bfffb5af5d85c8dad38dbbbdd28cd7a271ee0a491703f533f47` | 40 | A via P4/Ew44 |
| `R/walsh-constant-magnitude-odd-divisor-v1.md` | `d0c351677d8bdad6a93c5d6eb93b515e9f92a5bc651934ac60b05b2d45e4abe3` | 37 | A via P4/Ew44 |
| `R/walsh-constant-magnitude-odd-divisor-addendum-v1.md` | `ce0ab2816882784f76a9c46ff3ff15099de309d6366fac97ca398c3b5e57c09e` | 7 | A edge clarification |
| Ew44 `R/w44-orientation-normalization-erratum-v1.md` | `254562c4cfc861f108da6680a38c98e4c3161e7adcf69d3fd68493087c2bef97` | 38 | Mandatory orientation/normalization |
| `R/walsh-fourth-moment-coupling-v1.md` | `643d903d399827d56a91adcb3af4248a20da2c7b94ee81ee4c7f066f30c87210` | 43 | U: global fourth moment |
| `R/walsh-global-signed-shift-cover-v1.md` | `3aa2ba5494044863d2385b7b2474dc1eb90f4d35769eb4a77cc86c4cb7934529` | 39 | U: shift sign counts |
| `R/walsh-all-phase-sign-count-v1.md` | `6d5b6bee2bfe3bd9a322ae96e063a516518e6a96c9b7dd039f1f0340e28ba553` | 38 | U: all-phase support |
| `R/walsh-peak-vs-unit-gap-v1.md` | `08acae3b10cca10217ca2638dc60913cee1c5acdd8b3e7eaf06987fd5b874971` | 31 | U: odd magnitude gap |
| `R/walsh-peak-blocking-upper-bound-v1.md` | `1693f189d0320c5b64909fa99a9066e24968af6abd81ae062169eaeceb8a15d2` | 33 | U: w68 scope ≤235 |
| `R/walsh-peak-blocking-fourth-moment-v1.md` | `590560bf7ee75a415037fa08868d42e1f1f48f25d0fa761e80502964e765404b` | 37 | U: ≤234, not w68 adoption |
| `R/walsh-peak-cube-sidon-bound-v1.md` | `a14b6ff9c24406e7236ac3b2f34f018ee37d573d5d6af11b692a686987dfee32` | 50 | U: ≥53; w43b returned, not adopted |
| `R/walsh-forced-peak-star-v1.md` | `e10cdcfe8148758e9db61edf11a00b78f3aae919c89be2773f1ef1f6cabb3ea6` | 23 | U: five-cube star |
| `R/walsh-independent-peak-cube-checks-v1.md` | `56ad731109d2b942c2dcb71e1cfd39f4805778dc6c343a7a57142133c9726209` | 17 | U: six weight-8 checks |
| `R/walsh-peak-span-fourflat-v1.md` | `34f57db29a2430ce140e2f5a5c290bf09c5b57a1b20e69eaea1c9237a27e0a54` | 30 | U: conditional span alternative |
| `R/walsh-peak-sevenflat-fourflat-count-v1.md` | `99a103cf33a56a0932cb27062f554c173ccd30484ff8db44d9d9a1b8a90f525a` | 31 | U: ≥9 conditional 4-flats |
| `R/walsh-peak-fiveflat-source-defects-v1.md` | `2f201dda95ea266bbfd01d837bb2e129e6a7e64eac43b1aad8f05beb3ac3c9cf` | 25 | U: frequency-5/source-4 defect; Ew44 overlay |
| `R/walsh-all-odd-sign-magnitude-obstruction-v1.md` | `8c5bdb238f66999b9f791c545324bfeca25c654a811551387dfff0c9adaac961` | 50 | U: w74 frozen, no adoption inferred |
| `R/walsh-all-odd-sign-symmetry-v1.md` | `5e9699444d85d78e9f1403794ec4c44f59be5ac9bb2fe39c09e67442e63a3d5d` | 34 | U: symmetry orbit |
| `R/walsh-radical-peak-occupancy-v1.md` | `f2a8685d1178f0bd668254bed47352eff4c57a0bc5d280fa4f787afcfba96103` | 45 | U: global polar radical |
| `R/walsh-odd-divisor-flat-obstruction-v1.md` | `810805e82d758833c9634cce02c0d521d5b6e51d7f536b32febc0d0b65dd9282` | 29 | U: variable magnitudes |
| `R/walsh-universal-exchange-rigidity-v1.md` | `7666453ec08368b66511dbb0afa25df3b4d995354686038c17695a61ad39873d` | 40 | U: w91 frozen |
| `R/walsh-exchange-radical-degree-bound-v1.md` | `0dd1a3c40412acd226237c09ea1e99aa0e2dc480dbf81394b14f5e999e422711` | 32 | U: w91 frozen |
| `R/walsh-dense-active-peak-exchange-v1.md` | `9c693952b1688d63bce823a39b1f0729de9322e1dcc53bda62a3d251fc0aa3a0` | 34 | U: w91 frozen |
| `R/walsh-projective-code-equivalence-v1.md` | `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb` | 50 | G: w81 0F/0M/0m, no method certificate |
| `R/dual-enumerator-symbolic-v1.md` | `7a05f4b954bacaf5ba865fa3559dd0ab5ff4f130f32383d60d9245ded0c92897` | 99 | U: code consequences |
| `R/dual-enumerator-congruence-reduction-v1.md` | `6817ccf924a52f42fe5d860b936f79b021e6dd095efbd1b10c5a8a2facb74dad` | 70 | U: exact 15-congruence reduction |

The explicitly released original definition packet is `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/info-6-full-walsh-packet-v1.md`, SHA-256 `a9931cf5a12f174c232e6ad50fba993e5cd01ee9d4ab13dcfe0bd35dc69d3d37`, 35 LF. The prospective enumerator release is `info-6-post054-dual-enumerator-release-v1.json`, SHA-256 `1f4d8609cfd58ae6d72edd8f1475bcdef218bfbecf8f166880482f844a696cc3`, 43 LF, and its actual pre-body ACK is `R/dual-enumerator-prebody-ack-v1.json`, SHA-256 `9d4776d632f485b2ee3234385ac213d64f8617bfa89fdc64acdd29358fe6584b`, 17 LF. W81's actual source-gate return is `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/review-w81-info-6-projective-code-source-gate-v1.md`, SHA-256 `cd924d090ef17822010b68223af6c5445d068a8a2cc483ff34465723316edef8`, 189 LF; it is G, not a clean-cognition certification.

## 4. Exclusions, process and exact unresolved gap

By Main's explicit ruling, `walsh-truth-fiveflat-occupancy-v1.md`, SHA-256 `7dde761291e42da9adc108d5beaa11c215c8e4d7cfc0f8ab839eca9c969875ed`, 43 LF, is **NOT a union input**: it remains author-written, neither held as false nor reviewed, but prospective selection/method separation from the post054 diagnostic has not been established. The separate `walsh-2adic-moment-hierarchy-v1.md`, SHA-256 `a9c399ae2f63d942337e9c4ba9afcf97c36238bd107578a0563894dd9635dc36`, 60 LF, is not used here because separation of its higher truth-support moment interface from the stopped truth-degree/ANF route is not established; no mathematical falsity or new hold is inferred. Other unlisted author fragments retain their own statuses and are not silently adopted.

Binding parent controls, all observed before this write: S0 `a7161aa016f59552d9ee823cd2e4205df74ef2308e6ad25c4ed18322d78e580b` 31 LF; half-split stop `f188c7e01c9398113f8c3f0a3c0f136d614ddef47372a1f2ca5b3a03681a940b` 15 LF; global-degree stop `7e9d7013e4dca370b379943ab574d98c13339b8f045c53155007479f42905eda` 15 LF; post052 PROCESS MAJOR `11ec4733f13c19ad37ccacdefd2f699031dafc2e0e22a5e0418985cabc80ec02` 18 LF; post054 selected-diagnostic PROCESS MAJOR `b24fc8b338c9eaa958514662734b1068f7b6a168bcdd3e22eda7059f98bbfbb6` 17 LF; unrelated L1 quarantine `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f` 23 LF. Both owner episodes and all their selection/method/confidence/correctness/planning consumers remain HELD/ZERO/NONINPUT, with no salvage. The owner's metadata-poll and delayed-pin documentary MINORs, mandatory count/w44 corrections, HOLDv2, N4 UNKNOWN and auxiliary214 STOP persist. Prior exposure means no clean-cognition assurance.

Nothing here supplies an actual balanced 512-bit witness or an unrestricted contradiction covering all arrays. Numerical constraint-system feasibility, if proved, would still not realize a code or Boolean function. Original NL242 existence, all ranks/weights and `(24,24,2)`, global novelty, book-source equivalence except the separate internal bridge, independent-model review, external human, formal/kernel and executable gates remain OPEN or NOT PERFORMED at their exact scopes. This union is a review packet, not an adoption, new source permission, or a replacement for any frozen earlier file.
