# F895 author candidate: anchored heads without a two-point direct factor — cyclotomic allocation, factor signatures, and the exact residual

**Status.** Prospective GENERAL AUTHOR written candidate under owner addendum 2. Not a parent disposition, not an independent review, not family/human/formal acceptance, no novelty or priority claim. All statements concern actual original objects. No anchored tiling is constructed, and no global anchored nonexistence or finite-maximal-code-completion claim is made. No code was prepared or executed.

## 0. Summary of results (all proved below unless marked IMPORT)

For an actual anchored tiling `P⊕Q=Z_n` (`n>14`, `A={0,3,8,11}⊆P`, `S={0,1,7,13,14}⊆Q`), write `k=v_2(n)`, `n=2^k m'` with `m'` odd.

* **Thm 1 (exact cyclotomic criterion with multiplicities).** `P⊕Q=Z_n` iff `|P||Q|=n` and, for every divisor `m>1` of `n`, the multiplicity-retaining projection `P_m` or `Q_m` vanishes at a primitive `m`th root. The prime powers dividing `n` are split **exactly** (each lies in exactly one of `S_P,S_Q`), and `|P|=∏_{p^α∈S_P}p`, `|Q|=∏_{p^α∈S_Q}p` (a written T1-type partition proof is given).
* **Thm 2 (anchor-forced data).** `4|n`, `330|n`; the literal spectra are `𝒟(n)={1,6,12}∪{gcd(n,7),gcd(n,13),gcd(n,14)}` (forbidden head-difference gcds) and `ℰ(n)={3,5,11,2^{min(k,3)}}` (forbidden tail-difference gcds). The adopted two-adic allocation becomes: `S_P` contains `a≥1` powers of 2 and `S_Q` contains `k−a≥1`; `S_Q` contains a power of each of `3,5,11`; if `k=2`, then `S_P∩{2,4}` is a single element and `S_P` contains a power of 3 (hence `v_3(n)≥2`).
* **Thm 3 (two-point factor signature).** If `P={u,u+d}⊕C_0`, `g=gcd(n,d)`, then `Φ_m | P` for **every** `m|n` with `m|2g`, `v_2(m)=v_2(g)+1`; in particular `v_2(g)+1∈α(P):={α:2^α∈S_P}`. At `k=2`: `Φ_2|P` forces every factor gcd odd; `Φ_4|P` forces `v_2(g)=1` for every factor.
* **Thm 4 (reduction at the top two-adic layer).** `P` has the two-point factor `{0,n/2}` **iff** `Φ_{2^k s} | P` for every `s|m'`, iff `P` has a period of even order. Hence an actual **factorless** head has some `s|m'` with `Φ_{2^k s}∤P` and therefore `Φ_{2^k s}|Q`; if moreover `2^k∈S_P`, then `s>1`.
* **Prop 5 (the n/2 factor).** For every actual anchored tiling with `k=2` and `7∤n`, `P` has no period of even order and no factor `{0,n/2}`. For `k≥3` or `7|n`, every anchor/mate original-gcd test for `d=n/2` passes (exact values `3,5,11,2^{min(k,·)}` displayed), so this case stays in the residual.
* **Cor 6 (progression tails, conditional on S4 at its scope).** No anchored tiling (with or without a head factor) has the S4 progression-shaped tail.
* **Cor 7 (literal eight-word code).** The UD calculation `R1={a,a⁶,a⁷,a¹²,a¹³,a¹⁴}`, `R2={ab,a²b,a⁴b,a⁵b,a⁷b,a¹⁰b}`, `R3=∅` is freshly re-derived; all results above apply to `P_M` only under the unverified conditional RSS bridge.
* **Residual 8.** The explicit remaining class: anchored tilings whose head has no two-point direct factor, satisfying (R1)–(R7) of §8. No reduction of this class to the factor case is proved; Thm 4 is the exact boundary of the reduction available here.

## 1. Quantifiers, objects and the meaning of "factorless"

Throughout, `n>14` is an integer, `P,Q⊆Z_n` are nonempty, and `P⊕Q=Z_n` means every residue has **exactly one ordered** representation `p+q` (`p∈P`, `q∈Q`). Assume the literal anchors `A={0,3,8,11}⊆P` and `S={0,1,7,13,14}⊆Q`. Masks are `P(X)=Σ_{p∈P}X^p` with representatives in `[0,n)`, and `J(X)=Σ_{x∈Z_n}X^x`. For `m|n`, the **multiplicity-retaining projection** is `P_m(X)=Σ_{t∈Z_m}N_P^m(t)X^t`, where `N_P^m(t)=|{p∈P: p≡t (mod m)}|`; then `P(X)≡P_m(X) (mod X^m−1)` and `P(ζ)=P_m(ζ)` for every `ζ` with `ζ^m=1`. No projected set is ever treated as an unweighted quotient tiling.

**Definition.** `P` has a *two-point direct factor* if there are `u`, `d≢0 (mod n)` and `C_0⊆Z_n` with `P={u,u+d}⊕C_0` (the `2|C_0|` sums distinct and equal to `P`). `P` is *factorless* if no such `u,d,C_0` exist. Translating by `u` does not change any statement below (`X^u` is a unit at roots of unity), so we may take `u=0`. The order-two case `2d≡0`, i.e. `d=n/2`, is included.

Write `k=v_2(n)`, `n=2^k m'` with `m'` odd. For a set `E`, `Σ_n(E)={gcd(n,x−y): x,y∈E, x≠y}` (original gcds, never projected ones).

## 2. Theorem 1: exact cyclotomic criterion and the prime-power partition

**Theorem 1.** Let `P,Q⊆Z_n` be nonempty.

(a) `P⊕Q=Z_n` iff `|P||Q|=n` and for every divisor `m>1` of `n`, `Φ_m | P_m` or `Φ_m | Q_m` (equivalently `P(ζ_m)=0` or `Q(ζ_m)=0` for one, hence every, primitive `m`th root `ζ_m`).

(b) If `P⊕Q=Z_n`, put `S_P={p^α | n: p prime, α≥1, Φ_{p^α}|P_{p^α}}` and `S_Q` likewise. Then `S_P∩S_Q=∅`, `S_P∪S_Q` is the set of all prime powers `>1` dividing `n`, and
\[
|P|=\prod_{p^\alpha\in S_P}p,\qquad |Q|=\prod_{p^\alpha\in S_Q}p .
\]
Non-prime-power `m` may have `Φ_m` dividing both projections; no exclusivity is claimed for them.

(c) (Prime-power mask condition with multiplicities.) For `p^α|n`, `Φ_{p^α}|P_{p^α}` iff for every `r mod p^{α−1}` the `p` counts `N_P^{p^α}(r+jp^{α−1})`, `j=0,…,p−1`, are equal. In particular `Φ_{p^α}|P_{p^α}` implies `p | |P|`.

**Proof.** (a) Directness is the identity `P(X)Q(X)≡J(X) (mod X^n−1)`, since the coefficient of `X^x` on the left is the number of ordered representations of `x`. Two polynomials are congruent modulo `X^n−1` iff they agree at all `n`th roots of unity (distinct roots). At `ζ=1` the identity reads `|P||Q|=n`; at `ζ≠1` of order `m|n`, `J(ζ)=0`, so it reads `P(ζ)Q(ζ)=0`. As `Φ_m` is irreducible over `Q` (the minimal polynomial of `ζ_m`) and `P_m,Q_m∈Z[X]`, `P(ζ_m)=0` iff `Φ_m|P_m`, and then `P` vanishes at all primitive `m`th roots. Both directions follow.

(c) Write `P_{p^α}(X)=Σ_{r=0}^{p^{α−1}−1}X^r F_r(X^{p^{α−1}})` with `F_r(Y)=Σ_{j=0}^{p−1}N_P^{p^α}(r+jp^{α−1})Y^j`. Put `ω=ζ^{p^{α−1}}`, a primitive `p`th root. Since `[Q(ζ):Q(ω)]=p^{α−1}`, the elements `1,ζ,…,ζ^{p^{α−1}−1}` are linearly independent over `Q(ω)`; so `P(ζ)=0` iff `F_r(ω)=0` for all `r`, iff `Φ_p=1+Y+⋯+Y^{p−1}` divides each `F_r` (degree `≤p−1`), iff each `F_r` has equal coefficients. Summing equal counts, `|P|=Σ_r pN_r` is divisible by `p`.

(b) By (a) every prime power `s|n`, `s>1`, lies in `S_P∪S_Q`. For `s∈S_P`, `Φ_s` divides `P_s`, and `P(X)−P_s(X)` is a multiple of `X^s−1`, which `Φ_s` divides; so `Φ_s | P(X)` in `Z[X]`. The `Φ_s` (`s∈S_P`) are distinct monic irreducibles, hence `∏_{s∈S_P}Φ_s(X)` divides `P(X)` in `Q[X]`, and, the divisor being monic, in `Z[X]`. Evaluating at `1` and using `Φ_{p^α}(1)=p` gives `∏_{s∈S_P}Φ_s(1) | |P|`. Likewise for `Q`. Since `n=∏_{s pp | n}Φ_s(1)` (product over all prime powers `s>1` dividing `n`),
\[
n=\prod_{s\in S_P\cup S_Q}\Phi_s(1)\le\prod_{s\in S_P}\Phi_s(1)\prod_{s\in S_Q}\Phi_s(1)\le |P||Q|=n,
\]
where the first inequality counts an overlap twice (each factor `≥2`) and the second uses divisibility of positive integers. Equality throughout forces `S_P∩S_Q=∅` and both divisibilities to be equalities. ∎

*Remark (what "with multiplicities" means here).* (c) is a condition on the original-element counts `N_P^{p^α}`, not on a support set; e.g. `Φ_4|P_4` says `N(0)=N(2)` and `N(1)=N(3)` for the counts of actual head elements modulo 4. For non-prime-power `m`, `Φ_m|P_m` is the exact vanishing identity `Σ_t N_P^m(t)ζ_m^t=0`, which is not replaced by any positivity or fibre-decomposition claim.

## 3. Theorem 2: anchor-forced spectra and the cyclotomic form of the two-adic allocation

**Lemma 2.0 (admissible dilation; packet-displayed written lemma, restated).** If `U⊕W=Z_n` and `t>0` with `gcd(t,|U|)=1`, then `t` is injective on `U` and `tU⊕W=Z_n`. *Proof (as displayed in S5 §4/S6 §4.1/S8 §4, re-checked):* for a prime `ℓ∤|U|`, in `F_ℓ[Z_n]`, `U(X^ℓ)W(X)=U(X)^ℓW(X)=U(X)^{ℓ−1}J=|U|^{ℓ−1}J=J`; the integer ordered-sum coefficients of `U(X^ℓ)W(X)`, counted with multiplicity before passing to an image set, are nonnegative, `≡1 (mod ℓ)` and total `n`, so all equal `1`; iterate over the prime factors of `t`. Every unit modulo `n` is admissible for either factor.

**Lemma 2.1 (spectrum separation; packet-displayed S6 Theorem 2 / S5 Theorem C, restated).** If `U⊕W=Z_n` then `Σ_n(U)∩Σ_n(W)=∅`. *Proof:* if `gcd(n,x−y)=gcd(n,s−r)` with `x≠y` in `U`, `r≠s` in `W`, a unit `v` with `v(x−y)≡s−r` exists (prime-power-wise unit ratio, then CRT); then `vU⊕W` is direct by Lemma 2.0, but `(vx,r)` and `(vy,s)` have the same sum.

**Theorem 2.** For every actual anchored tiling:

1. `2 | |P|`, `2 | |Q|`, `330 | |Q|`; hence `4|n`, `660|n`, `k≥2`.
2. `Σ_n(P)∩𝒟(n)=∅` and `Σ_n(Q)∩ℰ(n)=∅`, where exactly
\[
\mathcal D(n)=\{1,6,12\}\cup\{\gcd(n,7),\gcd(n,13),\gcd(n,14)\},\quad \gcd(n,14)=\begin{cases}14&7|n\\2&7\nmid n\end{cases},\qquad
\mathcal E(n)=\{3,5,11,2^{\min(k,3)}\}.
\]
3. Let `a=|S_P∩{2,4,…,2^k}|`. Then `|P|_2=2^a`, `|Q|_2=2^{k−a}`, and `1≤a≤k−1`. `S_Q` contains at least one power of each of `3,5,11`. For every prime `p∤|P|`, all powers of `p` dividing `n` lie in `S_Q`.
4. (Adopted two-adic allocation, re-derived.) `3 | |P|` or `8|n`. Consequently, if `k=2` then `a=1`, `S_P∩{2,4}` is a single element, `S_P` contains a power of `3`, `S_Q` contains a different power of `3`, so `v_3(n)≥2` and `1980|n`; if `k≥3`, `1320|n`.
5. `P≠A`; hence `|P|≥6`, and `|P|` is even.

**Proof.** (1) Collisions (Lemma 2.0): if `|P|` were odd, `2P⊕Q` would contain `2·3+1=2·0+7`; if `gcd(t,|Q|)=1` for `t=8,3,5,11`, then `P⊕tQ` would contain respectively `8+8·0=0+8·1`, `3+3·0=0+3·1`, `8+5·0=3+5·1`, `11+11·0=0+11·1`. All displayed pairs are distinct ordered pairs since the anchors are distinct residues (`n>14`). Then `n=|P||Q|` is divisible by `2·330`.

(2) `Σ_n(Q)⊇{gcd(n,s): s∈{1,6,7,12,13,14}}` (positive differences of `S`) and `Σ_n(P)⊇{gcd(n,s): s∈{3,5,8,11}}` (positive differences of `A`); apply Lemma 2.1. Evaluate with `4|n`, `3|n`, `5|n`, `11|n`: `gcd(n,6)=6`, `gcd(n,12)=12`, `gcd(n,3)=3`, `gcd(n,5)=5`, `gcd(n,11)=11`, `gcd(n,8)=2^{min(k,3)}`, and `gcd(n,14)=2·gcd(n/2,7)`, which is `14` or `2`.

(3) By Theorem 1(b), `|P|_2=2^a`, `|Q|_2=2^{k−a}`; (1) gives `a≥1` and `k−a≥1`. Since `3,5,11 | |Q|` and `|Q|=∏_{S_Q}p`, `S_Q` contains a power of each. If `p∤|P|`, Theorem 1(c) forbids every `p^α∈S_P`, so Theorem 1(b) puts it in `S_Q`.

(4) Suppose `k=2`, `n=4μ` with `μ` odd, and `3∤|P|`. Choose a positive odd `t` with `2t≡3 (mod μ)` (possible as `2` is invertible modulo odd `μ`; add `μ` if needed for oddness). Any odd prime `p` dividing both `t` and `|P|` divides `μ` (because `|P| | 4μ`), hence divides `2t−3`, hence `p=3`, excluded; and `t` is odd. So `gcd(t,|P|)=1`, while `8t−12=4(2t−3)≡0 (mod 4μ)`. In `tP⊕Q` (Lemma 2.0) the distinct ordered pairs `(8t,1)` and `(0,13)` give `8t+1≡13≡0+13`, a contradiction. Thus `k=2` forces `3 | |P|`; by (3) `a=1`. By Theorem 1(b) a power of 3 lies in `S_P` and, since `3 | |Q|`, another power of 3 lies in `S_Q`, so `v_3(n)≥2` and `4·9·5·11=1980 | n`. If `k≥3`, `8·3·5·11=1320 | n`.

(5) If `P=A={0,3}⊕{0,8}`, normalize `d=3`, `C={0,8}`, `g=gcd(n,3)=3`. As in S6 §2 (explicit `p=3` boundary), `T=C⊕Q` satisfies `1_T(x)+1_T(x−3)=1`, so `6|n` and `T` is the full preimage of a selector `V⊂Z_6`. The tail anchors project to `{0,1,2}⊆V`, so `V={0,1,2}`; the actual element `8∈C` gives `8+1≡3 (mod 6)` in the image of `T`, but `3∉V`. Contradiction. So `P⊋A`, and with (1) `|P|≥6`. ∎

*Interpretation.* Item 2 is the complete list of **literal** spectrum constraints; the full Lemma 2.1 also uses all of `Σ_n(P)` and `Σ_n(Q)`, which are unknown beyond the anchors. Item 4 is the S3 statement re-derived in written form; it is used below only in the stated cyclotomic translation.

## 4. Theorem 3: the cyclotomic signature of an actual two-point factor

For a divisor `g` of `n` with `2g|n` put
\[
M(g)=\{m: m|n,\ m|2g,\ v_2(m)=v_2(g)+1\}.
\]

**Lemma 3.0.** For `d∈Z_n` with `g=gcd(n,d)` and `ζ` of order `m|n`: `ζ^d=−1` iff `m∈M(g)` (when `2g∤n`, never).

*Proof.* `ζ^d=−1` iff `m|2d` and `m∤d`. For `m|n`, `m|2d` iff `m|gcd(n,2d)`, and `m|d` iff `m|g`. If `2g|n` then `gcd(n,2d)=2g` (as `d/g` is coprime to `n/g`, and `n/g` even forces `d/g` odd); if `2g∤n` then `gcd(n,2d)=g` and no `m` qualifies. Finally `m|2g`, `m∤g` iff `m|2g` and `v_2(m)=v_2(2g)`. ∎

**Theorem 3.** Let `P={u,u+d}⊕C_0` be an actual two-point direct factor of an actual anchored head, `g=gcd(n,d)`. Then `2g|n` and
\[
\Phi_m\mid P_m\quad\text{for every } m\in M(g);\qquad\text{in particular}\quad 2^{v_2(g)+1}\in S_P,\ \ v_2(g)+1\in\alpha(P):=\{\alpha:2^\alpha\in S_P\}.
\]
Consequently `2^{v_2(g)+1}∉S_Q` (Theorem 1(b)). If `k=2` and `S_P∩{2,4}={2}`, every two-point factor has odd `g`; if `S_P∩{2,4}={4}`, every two-point factor has `v_2(g)=1`.

**Proof.** `2g|n` is the alternation argument displayed in S5 §1/S6 §1/S7 §1/S8 §1, re-checked: with `u` absorbed and `P={0,d}⊕C`, the actual set `T=C⊕Q` is direct and `{0,d}⊕T=Z_n`, so `1_T(x)+1_T(x−d)=1`; along a cycle of `x↦x+d` (length `n/g`) membership alternates, so `n/g` is even. For the cyclotomic claim, the mask identity `P(X)≡X^u(1+X^d)C_0(X)` modulo `X^n−1` gives `P(ζ)=ζ^u(1+ζ^d)C_0(ζ)=0` whenever `ζ^d=−1`, i.e. (Lemma 3.0) whenever `ord ζ∈M(g)`; by Theorem 1(a)'s Galois remark this is `Φ_m|P_m` for each `m∈M(g)`. The number `2^{v_2(g)+1}` divides `2g`, hence `n`, and has valuation `v_2(2g)`, so it lies in `M(g)`. The `k=2` clauses: `2g|n` gives `v_2(g)≤1`, and `v_2(g)+1` must be the unique element of `α(P)` (Theorem 2(4)). ∎

*Comment.* Theorem 3 converts every actual factor into a **mandatory head divisor set** `M(g)`; by Theorem 1(a) the complementary requirement on `Q` is untouched (for `m∈M(g)` non-prime-power, `Q` may also vanish). The weighted fibre equation of S5/S6/S7 is a finer consequence of the same factor; it is not available when `P` is factorless.

## 5. Theorem 4: the exact top-layer reduction to the two-point-factor case

**Theorem 4.** For an actual anchored tiling the following are equivalent:

(i) `P` has the two-point direct factor `{0,n/2}`;

(ii) `P+n/2=P`;

(iii) `P+t=P` for some `t∈Z_n` of even order;

(iv) `Φ_{2^k s}|P_{2^k s}` for every divisor `s` of `m'`.

Hence every actual **factorless** head satisfies: there is `s_*|m'` with `Φ_{2^k s_*}∤P_{2^k s_*}`, and therefore `Φ_{2^k s_*}|Q_{2^k s_*}` (Theorem 1(a)). If `2^k∈S_P`, then necessarily `s_*>1` (for `s_*=1` would contradict `Φ_{2^k}|P`); if `2^k∈S_Q`, `s_*=1` is allowed.

**Proof.** (i)⇒(ii): `P=C⊔(C+n/2)` and `(C+n/2)+n/2=C`. (ii)⇒(i): `P` is a union of pairs `{x,x+n/2}`; let `C` contain one element of each pair; the `2|C|` sums `c, c+n/2` are distinct and exhaust `P`. (ii)⇒(iii): `t=n/2` has order 2. (iii)⇒(ii): if `t` has even order `e`, then `(e/2)t` has order `2`, so equals `n/2`, and `P+(e/2)t=P` by iteration. (ii)⇔(iv): `P+n/2=P` iff `(1−X^{n/2})P(X)≡0 (mod X^n−1)` iff `(1−ζ^{n/2})P(ζ)=0` for all `ζ^n=1`. For `ζ` of order `m|n`, `ζ^{n/2}=1` iff `m|n/2` iff `v_2(m)<k`; otherwise `ζ^{n/2}=−1`. So the condition is exactly `P(ζ_m)=0` for all `m|n` with `v_2(m)=k`, i.e. `m=2^k s`, `s|m'`, which is (iv) by Theorem 1(a)'s Galois remark. The final assertions are the contrapositive together with Theorem 1(a),(b). ∎

*Status of the reduction.* Theorem 4 is a genuine reduction in one direction only: a head whose entire top two-adic cyclotomic layer `{Φ_{2^k s}: s|m'}` divides `P` is **not** factorless; it has the actual factor `{0,n/2}` with `g=n/2`, so it belongs to the two-point-factor case of S1/S2/S5–S8 at their scopes, and Proposition 5 gives its exact anchor/mate test. For a lower layer, i.e. a candidate `d` with `2g|n` and `v_2(g)+1<k`, vanishing of `P` on all of `M(g)` is necessary (Theorem 3) but is **not** proved sufficient for a factor `{0,d}`: a factor additionally requires the combinatorial matching `P=C⊔(C+d)` with `C` a `0/1` set, and divisibility of the mask by the cyclotomic factors of `1+X^d` at the relevant orders does not supply such a `C`. No reduction of lower layers is claimed.

## 6. Proposition 5: the order-two factor `{0,n/2}` and its exact anchor/mate test

**Proposition 5.** Let `P⊕Q=Z_n` be an actual anchored tiling (so `k≥2`, `330|n`, Theorem 2). Suppose `P+n/2=P`. Then for all `a,b∈A` the actual elements `a+n/2` and `b` of `P` satisfy
\[
\gcd\bigl(n,\,a-b+\tfrac n2\bigr)=\begin{cases}
n/2,& a=b,\\
c,& a-b=\pm c,\ c\in\{3,5,11\},\\
2^{\min(k,\,v_2(8\pm n/2))}\in\{2\ (k=2),\ 4\ (k=3),\ 16\ (k=4),\ 8\ (k\ge5)\},& a-b=\pm8 .
\end{cases}
\]
Consequently: **if `k=2` and `7∤n`, no actual anchored head has a period of even order, has the factor `{0,n/2}`, or contains the entire layer `{Φ_{4s}:s|m'}`**; by Theorem 4 there is then `s_*|m'` with `Φ_{4s_*}|Q_{4s_*}` and `Φ_{4s_*}∤P_{4s_*}` for **every** anchored tiling in this class (with or without other head factors). If `k≥3`, or `k=2` and `7|n`, every value above lies outside `𝒟(n)`, so the literal anchor/mate test does not exclude `{0,n/2}`; that subcase remains in the two-point-factor residual (with `g=n/2`, composite and `≥330`, consistent with the S1/S2 imports).

**Proof.** The anchor differences are `a−b∈{0,±3,±5,±8,±11}`. Put `x=a−b+n/2`. Since `k≥2`, `n/2` is even. For an odd prime `p|n`, `p|n/2`, so `x≡a−b (mod p)`.

* `a=b`: `gcd(n,n/2)=n/2≥330`, while every element of `𝒟(n)` is at most `14`.
* `a−b=±c`, `c∈{3,5,11}`: `x` is odd; an odd prime `p|n` divides `x` iff `p|c`, i.e. `p=c`; and `v_c(gcd(n,x))=1`, because either `v_c(n)=1`, or `v_c(n)≥2` gives `v_c(n/2)≥2` and `v_c(x)=v_c(±c+n/2)=1`. So the gcd is `c`.
* `a−b=±8`: no odd prime of `n` divides `x≡±8`. Two-adically `v_2(n/2)=k−1`: for `k=2,3` it is `<3`, so `v_2(x)=k−1` and the gcd is `2^{k−1}` (`2` resp. `4`); for `k=4`, `x=8(±1+m')` with `m'` odd, so `v_2(x)≥4=k` and the gcd is `16`; for `k≥5`, `v_2(n/2)≥4>3`, so `v_2(x)=3` and the gcd is `8`.

Mate–mate comparisons `(a+n/2)−(b+n/2)=a−b` reproduce the literal head gcds `3,5,11,2^{min(k,3)}`, which are outside `𝒟(n)` (else no tiling exists at all). Since `𝒟(n)⊆{1,2,6,7,12,13,14}` and `2∈𝒟(n)` iff `gcd(n,14)=2` iff `7∤n` (Theorem 2(2)), the only displayed gcd that can meet `𝒟(n)` is `2`, at `k=2`, `7∤n`, from the actual pair `8+n/2, 0∈P`. Lemma 2.1 then contradicts `P+n/2=P`. The remaining assertions follow from Theorem 4 (i)–(iv). ∎

*Two-adic interaction.* If `P` does have the factor `{0,n/2}`, Theorem 3 with `g=n/2` gives `M(n/2)={2^k s: s|m'}` inside `P`'s divisor set; in particular `2^k∈S_P`. At `k=2` this means `S_P∩{2,4}={4}` and `Φ_2|Q_2` (equal numbers of even and odd tail elements). This is a necessary signature of that subcase, not a construction.

## 7. Corollaries for the progression-tail and literal-code interfaces

**Corollary 6 (progression tails; conditional on S4 at its frozen f241 scope).** Let `n=75RD` (`R,D≥1`) and let `Q` be a union of five length-`R`, step-`75` progressions starting in the classes `{0,1,7,13,14} mod 75` (wrap-around allowed), as in S4. Then there is no actual anchored tiling `P⊕Q=Z_n`, whatever the factor structure of `P` (factorless or not). *Proof.* If `R=1`, `|Q|=5`, contradicting `330 | |Q|` (Theorem 2(1)). If `R>1`, S4 excludes every `P` containing `0,3,11`, and `A⊆P` contains them. ∎ The `R>1` half is a **conditional import**: the packet contains only S4's disposition summary, not the f241 proof body; it is not re-derived here. S4 does not use the anchor `8`, so Corollary 6 adds no head-structure information beyond excluding this tail family.

**Corollary 7 (literal eight-word code).** Let `X={b,a³b,a⁸b,a¹¹b,ba,ba⁷,ba¹³,ba¹⁴}` (eight distinct words). By the Sardinas–Patterson test (standard theorem, IMPORT), with `R_1=X^{-1}X∖{ε}` and `R_{i+1}=X^{-1}R_i∪R_i^{-1}X`, `X` is uniquely decodable iff no `R_i` contains `ε`. Fresh written computation:

* `R_1`: the only proper prefix relations inside `X` are among `b,ba,ba⁷,ba¹³,ba¹⁴` (each `a^ib` with `i>0` is a prefix of no other word, and no word is a proper prefix of it). The quotients are `b^{-1}{ba,ba⁷,ba¹³,ba¹⁴}={a,a⁷,a¹³,a¹⁴}`, `(ba)^{-1}{ba⁷,ba¹³,ba¹⁴}={a⁶,a¹²,a¹³}`, `(ba⁷)^{-1}{ba¹³,ba¹⁴}={a⁶,a⁷}`, `(ba¹³)^{-1}ba¹⁴=a`. Hence `R_1={a,a⁶,a⁷,a¹²,a¹³,a¹⁴}`.
* `R_2`: no word of `X` (each contains `b`) is a prefix of a pure power, so `R_1^{-1}X` alone contributes: `a^{-1}{a³b,a⁸b,a¹¹b}={a²b,a⁷b,a¹⁰b}`, `(a⁶)^{-1}{a⁸b,a¹¹b}={a²b,a⁵b}`, `(a⁷)^{-1}{a⁸b,a¹¹b}={ab,a⁴b}`, and `a¹²,a¹³,a¹⁴` are prefixes of no word. Hence `R_2={ab,a²b,a⁴b,a⁵b,a⁷b,a¹⁰b}`.
* `R_3`: a word `a^ib` (`i∈{1,2,4,5,7,10}`) is a prefix of a word of `X`, or has one as a prefix, only if that word is `a^ib` itself, which requires `i∈{0,3,8,11}`. None qualifies, and `b`, `ba^j` are not prefixes of `a^ib` for `i≥1`. Hence `R_3=∅`, all later `R_i=∅`, and `ε` never occurs.

So `X` is uniquely decodable (agreeing with S3). **Conditional bridge only:** if the RSS border theorem (as cited via Cordero in S3; unverified here) applies to a finite maximal code `M⊇X∪{a^n}`, its ordered borders give an actual anchored tiling `P_M⊕Q_M=Z_n`, and Theorems 1–4, Proposition 5 and Corollary 6 apply to it; if `P_M` is factorless it lies in the Residual of §8. No finite maximal completion, nonexistence of one, or printed-problem equivalence is claimed.

## 8. Residual 8: the explicit factorless class

Let `ℛ` be the class of actual anchored tilings `(n,P,Q)` (`n>14`, `A⊆P`, `S⊆Q`, `P⊕Q=Z_n`) whose head `P` is factorless (§1). Every member of `ℛ` satisfies all of the following, each proved above without the factor hypothesis (except (R7), conditional on S4):

* **(R1) Modulus.** `660|n`, `k=v_2(n)≥2`; `k=2⇒1980|n`; `k≥3⇒1320|n`.
* **(R2) Prime-power allocation.** `S_P⊔S_Q` is the set of all prime powers `>1` dividing `n`; `|P|=∏_{S_P}p` is even and `≥6`; `S_P` holds `a∈[1,k−1]` powers of 2; `S_Q` holds a power of each of `3,5,11` and every power of each prime not dividing `|P|`; `k=2⇒` `S_P∩{2,4}` is a singleton and `S_P` holds a power of 3.
* **(R3) Cyclotomic cover.** For every `m|n`, `m>1`: `Φ_m|P_m` or `Φ_m|Q_m`, as exact identities of original-element count polynomials (Theorem 1(a)); prime-power vanishing has the equal-count form of Theorem 1(c).
* **(R4) Spectra.** `Σ_n(P)∩Σ_n(Q)=∅`; in particular `Σ_n(P)∩𝒟(n)=∅` and `Σ_n(Q)∩ℰ(n)=∅` with the exact sets of Theorem 2(2).
* **(R5) Top layer (Theorem 4).** There is `s_*|m'` with `Φ_{2^k s_*}|Q_{2^k s_*}`, `Φ_{2^k s_*}∤P_{2^k s_*}`; `s_*>1` whenever `2^k∈S_P`. `P` has no period of even order.
* **(R6) Where factorlessness is a genuine constraint.** For `d` with `g=gcd(n,d)`: if `2g∤n`, or `2^{v_2(g)+1}∉S_P`, or some `m∈M(g)` has `Φ_m∤P_m`, then `{0,d}` is automatically not a factor (Theorem 3). Factorlessness is a nontrivial combinatorial condition only for the remaining `d` (those with `2g|n` and `P` vanishing on all of `M(g)`). For `d=n/2`, `M(n/2)` is the whole top layer and vanishing on it is also sufficient (Theorem 4), so factorlessness excludes it outright. For every other `d` in this set (including `v_2(g)+1=k`, `g≠n/2`, where `M(g)={2^k s: s | g/2^{k−1}}` is a proper part of the top layer), sufficiency is **not** proved and factorlessness remains an independent matching condition.
* **(R7) Tail shape (conditional on S4).** `Q` is not of the S4 progression-union form (Corollary 6).

The weighted selector equation and all gcd-15/16/prime/small-gcd contradictions of S1/S2/S5–S8 require an actual two-point factor and therefore say nothing about `ℛ`. **No member of `ℛ` is constructed and `ℛ=∅` is not claimed.** The first unpaid step for `ℛ` is either (a) a proof that some `d` in (R6)'s nontrivial set always yields an actual matching `P=C⊔(C+d)` (reducing to the factor case), or (b) an obstruction using the full cover (R3) together with (R4)–(R5), e.g. showing the forced `Φ_{2^k s_*}|Q` is incompatible with the tail anchors and `ℰ(n)`; neither is proved here.

## 9. Illustrative finite arithmetic (ILLUSTRATIVE ONLY)

The following evaluate Proposition 5's formula at two moduli allowed by (R1). They are hand arithmetic, not tilings, witnesses, or evidence that any anchored tiling exists for these `n`.

* `n=1980=4·9·5·11` (`k=2`, `7∤n`): `n/2=990`, `8+990=998=2·499`, `gcd(1980,998)=2=gcd(1980,14)∈𝒟(1980)`. So no anchored head in `Z_1980` is `990`-periodic, and by Theorem 4 some `Φ_{4s}` (`s|495`) divides `Q_{4s}` but not `P_{4s}`.
* `n=1320=8·3·5·11` (`k=3`): `8+660=668=4·167`, `gcd(1320,668)=4∉𝒟(1320)=\{1,6,12,2\}`; the other mate values are `3,5,11,660`. The anchor/mate test passes, so a `660`-periodic anchored head is not excluded here.

## 10. Imports, standard facts, and limits

* **Proved here in writing (no import):** Theorem 1 (given irreducibility of `Φ_m`), Lemma 3.0, Theorem 3, Theorem 4, Proposition 5, Theorem 2(1),(3),(4),(5), the `R_1,R_2,R_3` computation.
* **Packet-displayed written lemmas, restated and re-checked:** Lemma 2.0 (admissible dilation) and Lemma 2.1 (spectrum separation) from S5 §4, S6 §4, S8 §4; the alternation fact `2g|n` from S5–S8 §1; the `g=3` selector argument from S6 §2.
* **Standard external theorems (IMPORT, not in packet):** irreducibility of cyclotomic polynomials over `Q` (S5/S6 display the prime case only), the resulting degree `[Q(ζ_{p^α}):Q(ζ_p)]=p^{α−1}`, Gauss's lemma for monic divisors, CRT, and the Sardinas–Patterson criterion.
* **Conditional imports at their stated scopes (not re-derived):** S4's `R>1` progression-tail obstruction (Corollary 6 only); the RSS/Cordero border bridge (Corollary 7 only); S1/S2's factor-case conclusions (`g` composite `≥18`, `g≤14` excluded), cited only as context for the factor subcase `g=n/2`, never used in a proof about `ℛ`. The separately named coprime-cardinality CRT-graph route has no proof body here and is not used.
* **Limits.** No anchored tiling, factor, or member of `ℛ` is constructed; no unrestricted anchored nonexistence, no finite-maximal-code completion or non-completion, no printed-source correspondence, novelty, priority, family/human/formal acceptance. Theorem 4 is the only reduction from factorless heads to the factor case proved here, and it is confined to the top two-adic layer. All statements are author work awaiting independent review and parent disposition.

## 11. Read, process and execution declarations

* **Before any body.** I read completely (raw rereads after formatted displays elided JSON entries) the f895 `manifest-v1.json`, `freeze-receipt-v1.json`, `final-pre-dispatch-binding-v1.json`, `parent-live-metadata-supply-v1.json`, and, after Main's direct confirmation that it existed, `actual-dispatch-receipt-v1.json`; then all 22 manifest-listed status-only controls, raw and complete. Controls were status/permission inputs only. I opened no file referenced inside a control or a source link. I wrote `prebody-ack-v1.md` exclusively and delivered a direct PREBODY ACK to Main, both before opening any packet part. All genuine held episodes and all proof/method/planning/selection/verification/reporting/confidence/downstream consumers remained NONINPUT. No skill, memory or other unlisted file was read for this task. No clean-cognition certificate is claimed.
* **Part 1** (`literal-packet-part-01-v1.md`, parent pins 882 LF, 87,886 B, `d98b7b78…56dc`): read in order in raw windows `1–20, 21–40, …, 841–860` (43 windows of exactly 20 LF), then `861–882`. **Process deviation (disclosed):** the window `861–882` had **22 LF**, exceeding the 20-LF maximum by two lines; its display was complete and below 30,000 bytes (the whole S7 body is 13,507 B). I recovered compliance by immediately re-reading `861–880` and `881–882` raw before reading part 2. No display was clipped. This covers rendered S1 `1–20`, S2 `1–51`, S3 `1–31`, S4 `1–20`, S5 `1–278`, S6 `1–280`, S7 `1–172` in order.
* **Part 2** (`literal-packet-part-02-v1.md`, parent pins 633 LF, 41,299 B, `7b15b028…b127`): read in order in raw windows `1–20, 21–40, …, 601–620, 621–633` (31 windows of 20 LF and one of 13 LF), through the ending. No clipping. This covers rendered S8 `1–129` and S9 `1–494` (the UNRUN f870 source, read as text only).
* **Batching.** Windows were issued as ordered batches of two to four read calls per tool block, and their results were consumed in window order; each window is a separate display. While reading I made comprehension-level checks of displayed identities (e.g. the anchor collisions); the derivations of this candidate (§§2–9) were composed only after both parts had been read through their endings.
* **Clock and tools.** Two administrative `/bin/date -u` calls: `2026-10-31T03:27:39Z` (before the ack) and `2026-10-31T03:58:48Z` (before writing this section). One generation of mine was discarded by the harness for exceeding its output limit before any tool call it planned was executed; it had no file or message effect, and this candidate was then written incrementally. No network, external model, scientific code execution, scientific eval, solver, test, build, compilation, child scientific process, Git, deletion or cleanup was used. No verifier was requested or prepared, so there is **no prepared-code hash**. All SHA-256 values above are parent-supplied administrative metadata, not recomputed.
* **Writes.** Only new exclusive files in this wave directory: `prebody-ack-v1.md` and this `author-candidate-v1.md` (the latter written incrementally within this task before delivery; no frozen or earlier-candidate file was edited).
