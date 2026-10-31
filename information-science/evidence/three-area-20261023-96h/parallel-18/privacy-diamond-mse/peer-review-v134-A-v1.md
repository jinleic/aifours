# Peer review v134-A: Sun8 direct P7, rank-free bound, bounded global existence, and every simple projective unitary model

Reviewer: InfoResearch96h-2 (info-1 owner, privacy diamond MSE). This is a cross-domain, same-harness, WRITTEN review.
Author: MathSun8-2.
Last actual `/bin/date` observed before this write: `Mon Oct 26 10:24:06 PDT 2026`.

**Level.** This is a hand reconstruction of supplied written proofs. It is not formal or kernel verification, not cross-vendor or human review, and not novelty or priority clearance. It is NOT blind; see §6. No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver, replay, CLI or nested agent was used. Every identity below was checked by hand in exact symbols, fractions or integer products; none was machine-checked. No numeric, state, control or boundary instance, magnitude or decimal probe was introduced. B was never evaluated.

## 0. Chain, coverage and verdict summary

**Chain**

| Step | Record | SHA-256 | Clock |
|---|---|---|---|
| 1 | Pre-ACK held checkpoint110 | `44c21dc36ea96c306784b84217d4a90810af18be08f96cde831615c4b61108bc` | — |
| 2 | Opaque ACK `peer-review-v134-A-opaque-ack-v1.json` | `8e223ff4c321719c0969ecbbd1e4f41d6d088634bf3a45b72191aa762f51f3ce` | prewrite 10:09:05 |
| 3 | Main's explicit full-body release `peer-review-v134-A-explicit-body-release-v1.json` | `e1f92aeddb5ec55953fefbd1037f1c9e72e6e0971712fdef6fc1bcbae4034bc0` | 10:11:18 |
| 4 | Manifest `peer-review-wave-eighteen-v134.json` | `07bfe300f499dc112e162691f5f8c1a432ad5838c08232eb7946cf1e228a3b93` | — |
| 5 | Receipt | `ae754f50849c4da203669814b13f2c9817a458abfef54de01bb3752b32a0820c` | — |
| 6 | Mid-review checkpoint111 | `ca9f6da9f08c90c57a4ad7841dd8624a62f1b36c33219209cebd53bfb170864b` | 10:14:11 |

- Before the ACK, the intake was read in this order: v9 first, then v10, v11, HOLD, then the envelope (`6934db98...d6fb`).
- After the release, I read the manifest entry including `post_ack_entire_scope`.

**Coverage.** Every literal part was read through its END:

| Part | SHA-256 | LF | Sources |
|---|---|---|---|
| part1 | `71ff0c2e...78c6` | 916 | S1–S26 |
| part2 | `ea7327ad...a4a1` | 1002 | S27–S65 |
| part3 | `c334c8f4...9c4b` | 737 | S66–S74 |
| part4 | `5052e7c1...8850` | 268 | S75–S77 |

- Total: 2923 LF.
- The S1/v9 and S2/v10 overlays were read first.
- The four proof bodies were read complete:
  - S72: 178/178 LF
  - S73: 88/88 LF
  - S74: 225/225 LF
  - S75: 149/149 LF
- The raw request S76 (25/25 LF) and the parent context S77 (76/76 LF) were also read complete, each through its final line.
- At 10:23:23 I re-hashed all six live source files. Each SHA matches its packet header (§8).

**Verdicts.** I found 0 FATAL, 0 MAJOR and 0 MINOR mathematical findings in any gate. Each gate's two separate verdicts follow.

| Gate | Mathematics | Dependency / application / trust |
|---|---|---|
| A: whole 178 | WRITTEN_SUPPORTED | SUPPORTED at named ordinary background |
| B: whole 178+88 | WRITTEN_SUPPORTED | SUPPORTED at the stated existence ceiling |
| C: whole 225+149+178 | WRITTEN_SUPPORTED | SUPPORTED at the explicit nonabelian-simple model hypothesis |
| D: whole four-body application | WRITTEN_SUPPORTED as a conditional composition | SUPPORTED with all stated nonclaims |

- **Documentary item.** The S76 JSON syntax MINOR is the parent's v63 classification. I confirmed it independently (§5). It is not a mathematical finding.
- **Presentation remark.** One non-blocking remark on S75 §5 carries no severity (§3.4).
- **Process.** All process disclosures are in §6.

## 1. Gate A — S72 entire 178 LF: three-source constituent bound and same-G simple order bound

**Setting.** Take three pairwise-disjoint nonempty LEFT cosets `xM, yR, zH` in a finite group G. Their indices are `7t, 7r, 7u`, with t, r, u pairwise coprime positive integers.

**1.1 Pair lemma.** Let A and B be subgroups with indices `7a, 7b` and `gcd(a,b)=1`.
- `[G:A∩B]` is a multiple of `lcm(7a,7b)=7ab`; write it as `7abδ`.
- `|AB|/|G| = [G:A∩B]/([G:A][G:B]) = δ/7`, so `δ<=7`.
- If `δ=7`, then `AB=G`. Since `B^-1=B`, every pair of left cosets `xA, yB` meets: `x^-1y ∈ AB^-1`.
- Disjointness therefore forces `δ<=6`.

**1.2 Every conjugate pair.** Fix any g. The R-orbit of gH in G/H has stabilizer `R∩gHg^-1`.
- Its index is a multiple of `7r` and of `7u`, hence of `7ru`. Write it as `7ruδ_g`.
- The orbit size is `uδ_g`.
- An orbit of size `7u` would make R transitive, i.e. `RH=G`. That contradicts the disjoint pair `yR, zH`. So `δ_g<=6` for EVERY g, which is stronger than the base-pair statement.
- Likewise `T_R=R·M` and `T_H=H·M` in `Ω=G/M` have sizes `kt` and `ℓt`, with `1<=k,ℓ<=6`.

**1.3 Grid.** For a, b in G, set `A' = aRa^-1 ∩ bHb^-1`.
- Conjugating by `a^-1` and applying 1.2 gives `[G:A'] = 7ruδ'` with `δ'<=6`.
- `aT_R ∩ bT_H` is a union of A'-orbits. An orbit of size w has point stabilizer of index `7ruδ'w`, which is divisible by `7t`.
- Since `gcd(t,ru)=1`, `t | δ'w`. Put `g=gcd(t,δ')`; then `(t/g) | w`.
- Hence each entry `Z = |aT_R∩bT_H|/t` lies in `(1/g)Z` with `g<=6`. The denominator may vary by entry, and no free incidence matrix is substituted.

**1.4 Incidence and centred operators.** `I_R` is well defined on cosets aR because T_R is R-invariant.
- Column sums are `kt`. By G-equivariance and the count `7r·kt = 7t·(row sum)`, row sums are `kr`. Similarly `I_H` has column sums `ℓt` and row sums `ℓu`.
- For `P=I_R I_R*`: `P1 = k^2 tr·1` and `trace P = 7ktr`. Since P is Hermitian with 1 as an eigenvector, P preserves the complement of 1.
- `P_0 = P - k^2 tr E_0` is PSD, G-equivariant and zero on constants, with `trace P_0 = k(7-k)tr`. Q is identical, with `trace Q_0 = ℓ(7-ℓ)tu`.

**1.5 Spectral step.**
- Let λ be the largest eigenvalue of `P_0`. It is positive because `trace P_0 > 0`.
- The λ-eigenspace is G-invariant and lies in the complement of the constants. The constants are the only trivial isotypic part of a transitive permutation module. Hence an irreducible W inside it is nontrivial.
- `λ·dim W <= λ·dim(eigenspace) <= trace P_0`, because all other eigenvalues are nonnegative.
- `trace(P_0Q_0) = trace(Q_0^{1/2}P_0Q_0^{1/2}) <= λ·trace Q_0`.
- No commutation of `P_0` with `Q_0`, no Q-invariance of W, no scalar action and no multiplicity-one assumption is used. Only this W is bounded, not the whole cyclic or orbital module, and S72 says so explicitly.

**1.6 Moments over the SAME uniform 49ru pairs.**
- The sum of the entries of `I_R* I_H` is `(I_R1)·(I_H1) = 7t·kr·ℓu`, so `E Z = kℓ/7`.
- The sum of squares is `trace(PQ) = k^2ℓ^2t^2ru + trace(P_0Q_0)`. The cross terms vanish because `P_0E_0 = 0 = E_0Q_0`.
- Dividing by `49ru·t^2` gives `Var Z <= k(7-k)ℓ(7-ℓ)/(49d) <= 144/(49d)`, using `k(7-k), ℓ(7-ℓ) ∈ {6,10,12}`.

**1.7 Farey lower bound.**
- The neighbour determinants are `1·1-0·6`, `4·1-1·3` and `5·1-2·2`, each equal to 1.
- A rational n/g strictly between `a/b` and `c/d` satisfies `g = d(bn-ag)+b(cg-dn) >= b+d = 7`.
- The inclusions are: `1/7<1/6`; `1/4<2/7<1/3` (as `7<8` and `6<7`); `2/5<3/7<1/2` (as `14<15` and `6<7`).
- The gap products are:
  - `(1/7)(1/42) = 1/294`
  - `(1/28)(1/21) = 1/588`
  - `(1/35)(1/14) = 1/490`
- Reflection `x->1-x` preserves the product for `j=6,5,4`, and integer translation preserves denominators. Here `μ = kℓ/7` is never an integer, because 7 is prime and `k,ℓ<=6`.
- `E[(Z-a)(Z-b)] >= 0` gives `Var Z >= (μ-a)(b-μ) >= 1/588`.
- Hence `d <= 144·588/49 = 144·12 = 1728`.

**1.8 Packing for finite nonabelian simple G.**
- A nontrivial irreducible representation has a proper normal kernel, which is trivial here. Average the inner product to make it unitary.
- **Claim: `δ >= 1/2`.** Let δ be the least operator distance from I over nonidentity elements. Suppose `δ<1/2`, and take A, B to be conjugates of a minimizer.
  - `(ABA^-1B^-1 - I)BA = AB-BA = (A-I)(B-I)-(B-I)(A-I)`, so the norm is at most `2δ^2 < δ`.
  - The commutator is therefore the identity. All conjugates commute, so they generate a nontrivial abelian normal subgroup. That is a contradiction.
  - The normal-closure step is essential, and it is present.
- **Packing.** Distinct elements are separated by at least 1/2 in operator norm, hence in Frobenius norm.
  - The radius-1/4 Frobenius balls are disjoint in real dimension `2d^2`. All of them lie inside the ball of radius `sqrt(d)+1/4`.
  - So `|G| <= (4sqrt(d)+1)^(2d^2)`.
  - `d <= 1728 < 1764 = 42^2` gives a base strictly below 169.
  - `1728^2 = (1700+28)^2 = 2890000+95200+784 = 2985984`, and twice that is `5971968`.
  - Hence `|G| < 169^5971968`, and every subgroup index, in particular all eight unchanged original indices, is below B.

**1.9 S72 §8.** These are the direct eight-source use of any three sources and the all-eight finite-core quotient.
- Indices and disjointness are preserved through full preimages.
- `N_F(U_l/C) = N_G(U_l)/C` holds.
- An abstract nonabelian simple G with a proper finite-index subgroup is finite.
- All are correct. S72 explicitly does not claim an ambient bound for nonsimple or infinite G.

**Gate A verdicts.**
- **Mathematics:** WRITTEN_SUPPORTED, 0F/0M/0m.
- **Dependency/application:** SUPPORTED.
  - Background: the finite-dimensional Hermitian spectral theorem with PSD square roots and trace, unitary averaging, index/orbit/product-set identities, Farey neighbours (proved inline), and operator/Frobenius norms with Euclidean volume scaling.
  - No research import, classification, Jordan theorem or character table.
  - The older 168-LF and 200/142 papers are not premises.
  - The same-G order bound holds ONLY under the explicit finite-nonabelian-simple hypothesis.

## 2. Gate B — whole 178+88: arbitrary original G, bounded actual simple example

**2.1 Finite core.**
- `C = ∩_l Core_G(U_l)` over ALL EIGHT sources is normal of finite index, and C lies in every `U_l`.
- `F = G/C` keeps every index `7r_l` exactly.
- Each original coset is the full preimage of its image, so overlaps lift. No coset or prime power is lost.

**2.2 CRT.**
- The map `G/∩A_j -> Π G/A_j` is injective.
- The index of `∩A_j` is at most `Π a_j`, and it is a multiple of each `a_j`, hence of their product by pairwise coprimality.
- So the map is bijective, and every tuple of left cosets has ONE common point. No normality is used.

**2.3 Section.**
- `[K:U_l] = [K:NU_l][NU_l:U_l]`, and `[NU_l:U_l] = [N:N∩U_l]`. Hence `c_l D_l = 7r_l`.
- For `q ∈ π(g_l)V_l`, set `g_lU_l ∩ xN = y_l(N∩U_l)`. Translated by `x^-1`, this is the left coset `n_l(N∩U_l)` of index `c_l` in N.

**2.4 Uniform regular placement.**
- For regular l, h: `gcd(7r_l,7r_h) = 7`.
- Opposite placements give `gcd(c_l,c_h) = gcd(D_l,D_h) = 1`. CRT in Q then gives a common q, and CRT in N inside that fibre gives an original overlap, a contradiction.
- The seven regular placements are therefore uniform. The two cases TOP and BOTTOM are exhaustive.
- **Distinguished label.** `gcd(7r_e,7r_l) = 7·gcd(r_e,r_l) = 7` even when 7 divides `r_e`. Splitting `r_e`'s higher 7-power is correctly allowed.

**2.5 TOP.**
- All eight `c_l` are pairwise coprime, so every projected overlap would lift, and the projected cosets are disjoint.
- `D_e` must contain 7.
- So Q carries P7 with `D_l = 7s_l`, where `s_l = r_l/c_l` divides `r_l`.

**2.6 BOTTOM.**
- All eight `D_l` are pairwise coprime, so the full CRT gives one q in all eight projected cosets.
- The eight fibre pieces are nonempty and pairwise disjoint left cosets in N.
- `c_e` must contain 7.
- So N carries P7 with `c_l = 7s_l`, where `s_l = r_l/D_l`.

**2.7 Descent.**
- The order strictly decreases, and the `s_l` stay pairwise coprime divisors of the original `r_l`.
- `Z_p` is impossible: p must be 7, and eight disjoint singletons do not fit into seven elements.
- Gate A applied to any three of the eight sources gives `|S| < B`, and all `7s_l <= |S| < B`.
- Calling S a "composition factor" is ordinary normal-series refinement. That label is not load-bearing for the bound.

**Gate B verdicts.**
- **Mathematics:** WRITTEN_SUPPORTED, 0F/0M/0m.
- **Dependency/application:** SUPPORTED at the union 178+88.
- **Exact ceiling.** If direct P7 exists in ANY G, then an actual finite nonabelian simple S with `|S| < B` exists. S is a section of the all-eight finite-core quotient and carries eight actual disjoint cosets of indices `7s_l`, with each `s_l | r_l` and the `s_l` pairwise coprime.
- **Not covered.** Gate B is NOT a bound on `|G|`, `|F|` or the original `r_l`. Old v125 NR-NS coverage is not changed retroactively: S73 supplies the normal-section proof itself.

## 3. Gate C — whole 225+149+178: every nonabelian simple projective SU(n,q), n≥3, every q

**3.1 Dimension three (S74 §§2–5)**

*Matrices and multiplication*
- **u(a,b) preserves h.** The column pairings are: first with third gives 1; middle norm 1; middle with third gives `-ā+ā=0`; third norm `Tr b+N(a)=0`. The determinant is 1.
- **D(t) and w** preserve h and have determinant 1.
- **Multiplication:** `u(a,b)u(c,d) = u(a+c, b+d-āc)`. This preserves the trace constraint because `N(a+c) = N(a)+N(c)+Tr(āc)`.
- **Order and conjugation:** `|U| = q^3`, and `D(t)` conjugates `(a,b)` to `(t̄^2 a/t, N(t)b)`.

*Points, stabilizer, Sylow and Bruhat*
- **Points:** the isotropic points other than infinity are exactly `K(b,a,1)`, giving `q^3+1` points in all.
- **Stabilizer and order:** the full stabilizer is `B = TU`, and `|SU| = q^3(q^2-1)(q^3+1)`.
- **Kernel and Sylow:** the scalar kernel has order dividing `gcd(3,q+1)`. The cofactors are p-free, so U is Sylow.
- **Bruhat:** `G = B ∪ BwB`.

*Rank-one product*
- **Entrywise check:** `u(0,b)v(-b^-1)` equals `[[0,0,b],[0,1,0],[-b^-1,0,1]]`.
- **Third column after the final factor:** `-b^-1·b + 1 = 0`.
- **Identity with D(b)w:** the product equals `D(b)w = diag(b,-1,-1/b)·w`, because `b̄ = -b`. This also holds in characteristic two.

*Overgroups*
- **Generation:** `E = <U,U^->` is normalized by B and contains `n_b`, so it is normal. The explicit simple hypothesis then gives `E = G`.
- **Overgroup step:** for a proper `J ⊇ U` and `g = b_1 n_b b_2 ∈ J \ B`, `<U, gUg^-1> = b_1 E b_1^-1 = G`, a contradiction. Hence `J <= B`.

*Characteristic not seven*
- **Indices:** two p-free indices are both multiples of `q^3+1`, while their gcd is 7.
- **Contradiction:** `q^3+1 >= 9`, so `q^3+1` cannot divide 7.

**3.2 Faithful lower bound (S74 §6, §8.1).**
- **Commutator:** `[P(a,b),P(c,d)] = P(0, c̄^T a - ā^T c)`.
- **Abelian A:** `A = preimage of F_q^m` has order `q^(m+1)` and index `q^m`. It is abelian, since the commutator vanishes on `F_q^m`, and normal, since it contains the commutators.
- **Commutators fill Z:** for x outside A, choose a coordinate with `a_j ∉ F_q`. Then `c_j(a_j-ā_j)` fills the trace-zero line Z.
- **Orbit bound:** a character χ over a nontrivial ψ therefore has stabilizer exactly A, and its orbit has size `q^m`.
- **Block torus:** `D_n(t) = diag(t,S(t),1/t̄)` has determinant 1. It conjugates a to `t̄S(t)a` and b to `N(t)b`.
- **Norm map:** the norm onto `F_q^*` is surjective (kernel at most `q+1` by degree). The scalar action on the `q-1` nontrivial ψ is free, hence transitive.
- **Result:** every faithful complex V has `dim V >= q^(n-2)(q-1)`.
- **Scope check:** the block group is NOT called Sylow for `n>3`.

**3.3 Characteristic seven branches.**

*Inequalities*
- For `f>=2`: `q(q-1) >= 49·48 = 2352 > 1728`.
- For `f=1, n>=5`: `7^3·6 = 2058 > 1728`.

*q=7, n=3*
- The kernel is trivial, since it divides `gcd(3,8)=1`.
- `|G| = 7^3·344·48 = 2^7·3·7^3·43`.
- 43 is prime: none of 2, 3, 5 divides it, and `6^2 < 43 < 7^2`.
- `|G|/7` has four prime owners, so at least four labels have index exactly 7.
- A faithful action on seven points is then impossible, because 43 does not divide `7!`.

*Order formula*
- **Orthonormal basis:** if every self-pairing vanished, then `Tr(α h(w,v)) = 0` for all α would force `h=0`. An orthonormal basis therefore exists.
- **Recursions:** these are what the count gives.
  - `F_j+(q-1)E_j = q^(2j)`
  - `F_(j+1) = F_j+(q^2-1)E_j`
  - `E_(j+1) = (q+1)F_j+(q^2-q-1)E_j`
- **Derivation of the E-recursion:**
  - there are `q+1` last coordinates of norm one, each paired with norm-zero vectors;
  - the last coordinate zero pairs with norm-one vectors;
  - the remaining `(q-2)(q+1)` last coordinates each pair with vectors of a fixed nonzero norm.
- **Closed forms:**
  - `F_j - E_j = (-q)^j`
  - `E_j = q^(j-1)(q^j-(-1)^j)`
  - `|SU(n,q)| = q^(n(n-1)/2) Π_(a=2..n)(q^a-(-1)^a)`

*q=7, n=4*
- `7^6·48·344·2400`, with `2400 = 2^5·3·5^2`, gives `2^12·3^2·5^2·7^6·43`.
- The kernel divides `gcd(4,8)`.
- At least three labels have index 7, a contradiction.

All private-seven powers stay inside the divisor count.

**3.4 All ranks, p≠7 (S75).**

*Sylow subgroup and root matrices*
- **Order of U:** `|U| = q^(n(n-1)/2)` by the recursion `q^(2n-3)`, since `n(n-1)/2 - (n-2)(n-3)/2 = 2n-3`.
- **Sylow:** U is Sylow because the cofactors and the kernel are p-free.
- **Root pairings checked by hand:**
  - `h(e_j+ae_i, f_i-āf_j) = a - a = 0`
  - `h(f_j+ae_i, f_i-āe_j) = -a + a = 0`
  - `h(f_i+be_i, f_i+be_i) = b+b̄ = 0`

*Bruhat by pivot elimination*
- **e-pivot:** the vector is cleared by the `x_(e_i-e_j)`.
- **f-pivot, in four steps:**
  1. The `f_l` with `l>j` are cleared by `x_(e_j-e_l)`, via `f_j -> f_j-āf_l`.
  2. Each `e_i` with `i≠j` is cleared by the `e_i+e_j` groups. Every `f_i` entry is already zero, so nothing is reintroduced.
  3. z is cleared by the 3×3 group.
  4. The remaining `αe_j+δf_j` has `Tr(α/δ) = 0` and is cleared by `x_(2e_j)(-α/δ)`.
- **Induction:** the argument continues through `L^perp/L`. The root groups of the remaining coordinates fix L.

*Overgroups*
- **Reduction to n_wUn_w^-1:** from `g = u t n_w b ∈ H`, undoing only u gives `g_0 ∈ H`, and `g_0Ug_0^-1 = n_wUn_w^-1`. This holds because b normalizes U and `n_w^-1 t n_w ∈ T`.
- **Left descent:** a left descent i gives `U_(-α_i) = n_w U_β n_w^-1 ⊂ H`, with `β = -w^-1(α_i) > 0`. So `n_i ∈ H`.
- **Shortening:** `n_i^-1 g_0 ∈ T n_(s_iw) B` has length one less. Hence every w lies in `W_I`.
- **Case I = all:** this gives a normal E, so `E = G`, using the simple hypothesis exactly once.
- **Case I omits j:** the `W_I` representatives fix `E_j`, so `H <= P_j`.
- **Containment check:** T or `B ⊂ H` is never assumed.

*Parabolic index*
- **Gram matrix:** I used `[[0,0,I_j],[0,J_d,0],[I_j,0,0]]`, i.e. `F_j` in the order dual to `e_1..e_j`.
- **Unipotent block `[[I,Y,B_0],[0,I,X],[0,0,I]]`:** I derived `Y = -X̄^T J_d` and `B_0 + B̄_0^T = -X̄^T J_d X`. These are exactly S75's equations.
- **Levi block:** `diag(A,C,Ā^(-T))`.
- **Counts:**
  - `q^(2dj)` for X;
  - `q` per diagonal entry and `q^2` per off-diagonal pair for `B_0`;
  - total `q^(j(2n-3j))`.
- **Exponent identity:** `n(n-1)/2 - d(d-1)/2 = 2nj-2j^2-j`. Subtracting `j(2n-3j)` and then `j(j-1)` leaves 0.
- **Determinant:** `t/t̄` has kernel `F_q^*`, so its image has `(q^2-1)/(q-1) = q+1` elements. The kernel lies in every stabilizer.
- **Splitting `N_j`:** I checked the even/odd split. For `n=2m` the factors are `a=2r` and `2r-1`; for `n=2m+1` they are `2r` and `2r+1`, with `r = m-j+1..m`.
- **Integrality:** `C_Q(m,j)` is an integer by counting subspaces.
- **Common divisor:** `D = q^(largest odd ≤ n)+1` is the `r=m` factor in both parities, and `D >= q^3+1 > 7`.
- **Consistency:** `n=3, j=1` gives `N_1 = q^3+1`, which matches S74 §3's direct point count.
- **Conclusion:** any two of the at least seven p-free original indices are multiples of D, while their gcd is 7. Contradiction.

*Non-blocking presentation remark*
- **Basis order:** S75 §5 says only "relative to `E_j+K^d+F_j`". Its displayed Levi block and `B_0` equation are exact for `F_j` in the dual order `f_1..f_j`.
- **Witt order:** in the §1 Witt order `f_j..f_1`, both pick up conjugation by the antidiagonal `J_j`.
- **Effect:** counts and indices are unchanged. No severity is assigned.

**Gate C verdicts.**
- **Mathematics:** WRITTEN_SUPPORTED, 0F/0M/0m.
- **Dependency/application:** SUPPORTED at the EXPLICIT hypothesis that the actual projective image is nonabelian simple. Simplicity is never proved or imported for the family. Where the hypothesis fails, the theorem simply does not apply to that parameter.
- **What each body uses:**
  - S75 uses S74 §2 (trace/norm, the 3×3 group, the rank-one product) and §8.2 (the order formula).
  - The p=7 branch uses S72 Theorem A only.
  - Since all nondegenerate Hermitian forms are equivalent (S74 §8.2), the `J_n` model and the Witt model are conjugate. The union therefore covers abstract PSU(n,q), n≥3, every q.
- **Background:** Sylow existence and conjugacy; that a subgroup of full p-part contains a Sylow subgroup; finite abelian character weights; polynomial root counts; ordered-basis `|GL_j|`; and signed-permutation length/descent combinatorics, which is sketched in S75 §4 and is standard.
- **Not used:** Borel–Tits, maximal-subgroup lists, CFSG, character tables, Jordan, Stone–von Neumann, McLaughlin/Parker.
- **No NR is needed.**

## 4. Gate D — whole application and exact nonclaims

**Composition.**
- If direct P7 exists anywhere, Gate B yields an actual simple S with `|S| < B` and eight labelled divisor indices.
- Suppose S were isomorphic to a simple projective SU(n,q), n≥3:
  - **p≠7:** Theorem V excludes even the bare index pattern.
  - **p=7:** Theorem U7 excludes P7, via Gate A's W together with the §8.1 lower bound and the q=7, n=3/4 owner counts.
- The model's simplicity hypothesis is satisfied because S is simple, and P7 is invariant under isomorphism.
- **Mathematics and application:** WRITTEN_SUPPORTED as a conditional family exclusion.

**Nonclaims, all confirmed.**
- No classification of the remaining S.
- No exclusion of other simple models or other coset configurations below B.
- No enumeration, B evaluation, witness, assay or numerical R8.
- No unrestricted Sun8.
- General Sun8→P7 and global Sun7 ancestry are outside the scope.
- The old SL/PSL and Sp/PSp family results are independent and are not premises.
- The arbitrary G and the original `r_l` are not bounded.
- No adoption from clean component returns.

## 5. Raw request S76 and parent context S77

**S76.** I confirm independently that the part-4 object at LF11 lacks its closing `}` before the array close `],` at LF12. This is RAW_UTF8_NOT_VALID_JSON, a documentary MINOR as classified by the parent in v63. It is not a proof defect or source drift. I neither parsed nor repaired the frozen bytes.
- Its stated totals are internally consistent: `178+88+225+149 = 640` LF and `16928+13626+21895+18372 = 70821` B.
- The four proof bodies were reviewed through their direct pins, not through this request.

**S77.** This is read as context only. It is the earlier v129 parent disposition of Parts I/II. Its labels differ from v134: its C corresponds to v134 B, and its B lies inside v134 A. No verdict is transferred. My Gates A and B are independent reconstructions.

## 6. Process disclosures (conspicuous)

**Reviewer–author relationship.** This disclosure is additive and was NOT named in my opaque ACK.
- MathSun8 previously authored the same-harness review of MY privacy all-epsilon E addendum. That review is `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/peer-review-privacy-all-epsilon-E-v1.md`, SHA `0e1064b5721a6ef1ca8fed600447846bee2ebb90dc0e39d2f5f1c42f2b7ccc7c`. Its verdict was 0F/0M/0 substantive MINOR, conditional on D0.
- MathSun8-2 was also assigned to my v93 privacy source gate. I never read any unfinished verdict from that gate.
- This review is therefore reciprocal and non-blind.
- A whole-root search for `sun8`/`sun-coset8`/`MathSun8` found only these privacy-side records. It found no prior review by me of any Sun8 coset or P7 body.
- My ACK's bounded exposure statement listed my own prior reviews but not this relationship. Disclosing it now does not cure that omission, and I do not self-classify it. Main may classify.

**Own permanent categories.** All are retained and kept distinct:
- the first FIVE findings;
- SIXTH: v111-B exactness;
- SEPARATE: cp077 continuation-control failure (v21);
- cp102 primary exactness recurrence;
- v128 reviewer cadence, 09:15:37..09:47:51 (32m14s);
- the post-v60 numeric-instance finding (checkpoint108, `52ab0477...0c97`), plus its documentary prepin correction.

**Quarantines.** cp102 and checkpoint108 guidance stays ZERO and is not repeated. Auxiliary214 remains under strict STOP. The privacy primary stays STOPPED until this ACTUAL RETURN, followed by a NEW whole ACK and an explicit direction.

**This review's conduct.**
- Only metadata operations were used: `/bin/date`, shasum, reads, and writes in my own root.
- Cadence so far: ACK 10:09:05, checkpoint111 10:14:11, this write after 10:24:06.

**Author process items observed.** None is a new finding by me:
- S74 discloses that it was extended and renamed before its first pin.
- S73 §II.7 discloses that the author read the old NS range and the 63-LF text after Part I.
- The author states that no interpreter was used.

## 7. Exact remaining gap

Suppose the union is adopted. The direct-P7 residual is then to exclude or realize ALL finite nonabelian simple eight-source P7 cases below B that are not simple projective unitary models of dimension n≥3 at any q. This review provides none of the following:
- a list, search or certificate;
- any formal, kernel, human, configured-family or novelty status.

## 8. Source bindings (live SHA-256 re-observed at 10:23:23)

| Path | LF | SHA-256 |
|---|---:|---|
| `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/sun8-rank-free-three-source-Gram-Farey-finite-simple-bound-v1.md` | 178 | `76aa8a6fbfd6a2fcf4587ca5bec29e14215bcdfd5ec81dd47f56de9c4ea60e15` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/sun8-rank-free-global-existence-bound-complete-part2-v1.md` | 88 | `b401c139141c451755174f8151942b86916e5677f734715ede48299394716202` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/sun8-unitary-three-all-fields-and-all-dimensions-characteristic-seven-v1.md` | 225 | `573a5029e122da3d845d192f0a2c8a76ff42cd7d5d3354bd3c744e6c4928d06c` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/sun8-unitary-all-ranks-characteristic-not-seven-full-parabolic-proof-v1.md` | 149 | `95f606f08fc16fb7c033929551c6c5b03a728be81360e8d1b398abc5ff45144f` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/sun8-global-existence-and-entire-unitary-complete-packet-v9.json` | 25 | `3e11a9541ea8cf81749035966a6c455a54ca5f66ef99a621d0421684b5066cf5` |
| `institute/runs/three-area-2026-10-23-96h/sun-rank-free-P7-bounded-simple-existence-entire-parent-v1.md` | 76 | `9dbce6f9b7afab2fc0c9e35dbb0034ff47f45c0cb3d8e40ab4c3f739c34ff726` |

Same 18 owners; HOLD in force; science cutoff `2026-10-27T11:05:38-07:00`; delivery deadline 12:35:38. This is not an early park or a round closeout.
