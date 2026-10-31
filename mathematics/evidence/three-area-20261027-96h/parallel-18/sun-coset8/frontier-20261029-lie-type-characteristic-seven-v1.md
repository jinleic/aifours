# Groups of Lie type in characteristic 7: no direct P7 outside PSL2(7)

**Status: WRITTEN, with exact arithmetic in the author's eval kernel; conditional on named published classifications and on the owner's unreviewed Lie-type lemmas; UNREVIEWED.** Let S be a finite simple group of Lie type in characteristic 7, q=7^f, with S≇PSL2(7). The candidate statements are:

1. **Exceptional S** (G2, ³D4, F4, E6, ²E6, E7, E8 over F_q): some prime r>7 has a Sylow r-subgroup contained in a unique maximal subgroup. Hence no three proper subgroups of S have all pairwise index gcds ≤7; in particular Sun8(S) holds and S carries no direct P7 configuration.
2. **Classical S** (PSL_n(q) for n≥2, PSU_n(q) for n≥3, PSp_n(q), PΩ_n(q), PΩ^±_n(q)) with S≠PSL2(7), PSL2(49): S carries no direct P7 configuration.
3. **PSL2(49)** carries no direct P7 configuration.

"Direct P7" is the eight-pairwise-disjoint-left-coset condition, with all 28 index gcds equal to 7, of §3 of `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md` SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`. PSL2(7)≅PSL3(2) has seven disjoint index-7 cosets and is left to the separate, unreviewed Fano candidate `frontier-20261028-gl32-sun8-geometric-v1.md` SHA `d7c18486c27d7f50d792d57c6ed493f4ceb19c4a8df0c2ff041a59e3ff1c4da0`. No unconditional, arbitrary-group, novelty, formal-verification or adoption claim is made. The classical case 2 is a P7 statement only; a Sun8 conclusion there needs the separate Sun7/R8 import of §5.

## 1. Provenance, source order and inputs

Before any affected earlier body, read in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The owner's preview frontier `frontier-20261028-sun-wide-search-preview-frontier-v1.json` SHA `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6` is cited. Its displayed snippets are NONINPUT, and none is used, reconstructed or searched for. No historical hold or earlier review is modified.

Named inputs:

- **(L) Owner's unreviewed Lie-type lemmas.** These are Lemma 1 (every proper overgroup of a Sylow p-subgroup lies in a proper parabolic), Lemma 2 (a cyclotomic value D(S)=Φ_e(q), e≥2, divides every proper parabolic index) and Lemma 3 (Φ_e(q)≡1 mod q and Φ_e(q)≥2) of `frontier-20261029-lie-type-away-from-seven-v1.md` SHA `d2af4a0dfa7cbf3a55274aeb30b5657a593737eef6ffd97d2d38a461ea579736`. That packet is logged by Main as UNREVIEWED.
- **(M) Maslova's classification of the maximal subgroups of odd index in the simple classical groups over fields of odd characteristic.** N. V. Maslova, *Classification of maximal subgroups of odd index in finite simple classical groups: addendum*, Sib. Electron. Math. Rep. 15 (2018) 707–718; arXiv:1710.01563v3. The original PDF is pinned as `frontier-20261029-maslova-1710.01563v3-source.pdf` SHA `108397a5e0db8f4361d629f16c33e08b3810b8bd94a37d38e1fc5aafc9193cac` (204412 bytes); the owner visually read its Theorem items (1)–(23) on pp. 3–4. The theorem rests on Liebeck–Saxl, Kantor, Kleidman–Liebeck and Bray–Holt–Roney-Dougal, hence on CFSG. Its proof is not replayed.
- **(B) Baumeister–Burness–Guralnick–Tong-Viet, Theorem 2(iii) and Table C** (arXiv:2307.13976v2): for an exceptional simple T=G and odd r, the triples with a unique maximal overgroup of a Sylow r-subgroup R. The HTML is pinned as `frontier-20261029-bbgt-2307.13976v2-source.html` SHA `6cf5530f8386133e7208e6e0b77b1b44de78d8546549f2c3faf5144d403f9bfc`. The owner extracted Table C and the definitions α(m,ε): (q^{1/k})^m≢ε (mod r) for every prime k|f with k≠r, and β(m,ε): the same for k∉{2,r}. The proof is CFSG-dependent and not replayed.
- **(Z) Zsigmondy's theorem**, as stated in (B) §2.1: 7^n−1 has a prime divisor r of multiplicative order exactly n modulo r for every n≥3.

## 2. Exceptional groups: unique maximal overgroups

**Lemma U (unique-overgroup observation).** Let r be a prime greater than 7, let R be a Sylow r-subgroup of a finite simple group S with every proper subgroup index at least 8, and suppose R lies in a unique maximal subgroup M. Then among any three proper subgroups two have index gcd greater than 7.

*Proof.* A proper subgroup K of r′-index contains a Sylow r-subgroup R^g. Then K^{g^{-1}} contains R, so it lies in a maximal subgroup containing R, namely M. Hence [S:M]≥8 divides [S:K], and two r′-indices have gcd≥8. Two r-divisible indices have gcd≥r>7. Of three subgroups, two lie in the same class. □

For q=7^f choose r to be a **p-primitive** prime divisor of 7^{ef}−1, i.e. ord_r(7)=ef, which exists by (Z). Then ord_r(q)=e. For each prime k|f, q^{1/k}=7^{f/k} has order ef/gcd(ef,f/k)=ek modulo r. Consequently (q^{1/k})^m≡±1 would force ek|2m. That fails in each row below, since ek>e and m≤e with ε as listed, so every α or β condition holds. The rows of Table C used are, with H the unique maximal overgroup:

| S | r | type of H | condition needed beyond α/β | how it holds for q=7^f |
|---|---|---|---|---|
| G2(q) | r_6 (e=6) | A2^−(q) | p≥5 and (f>3 or r>13, …) | f=1: r=43; f=2: r=181; f≥3: r≡1 mod 6f gives r≥19 |
| ³D4(q) | r_12 (e=12) | q⁴−q²+1 torus normaliser | only (q^{1/k})^6≢−1 for k∉{3,r} | holds by p-primitivity |
| F4(q) | r_8 (e=8) | Ω9(q) | p≥3 and (f>2 or r>17, …) | f=1: r=1201; f=2: r=169553; f≥3 |
| E6(q) | r_9 (e=9) | A2(q³) | f>2 or r>19, … | f=1: r=37 or 1063; f=2: r=117307; f≥3 |
| ²E6(q) | r_18 (e=18) | A2^−(q³) | f>1 or r>19, … | f=1: r=117307; f≥2 |
| E7(q) | r_18 (e=18) | ²E6(q)×(q+1) | f>2 or r>37, … | f=1: r=117307; f=2: r=13841169553; f≥3 |
| E8(q) | r_30 (e=30) | the q⁸+q⁷−q⁵−q⁴−q³+q+1 torus normaliser | r>61, or … | f=1: r=6568801; f=2: r=555915824341; f≥3: r≥30f+1≥91 |

The displayed small primes come from the exact factorizations Φ_6(7)=43, Φ_12(7)=13·181, Φ_8(7)=2·1201, Φ_16(7)=2·17·169553, Φ_9(7)=3·37·1063, Φ_18(7)=117307, Φ_36(7)=13841169553, Φ_30(7)=6568801 and Φ_60(7)=61·555915824341. Primality and multiplicative orders were checked by the author's checker in §6. For E8 the table row uses r_{15(3−ε)/2} with α(30,1); taking r_30 makes α(30,1) automatic.

Every proper subgroup index of these S is at least 8, because |S| does not divide 7!/2. By (B), R lies in a unique maximal subgroup, so Lemma U gives the three-index exclusion. Since all 28 index gcds of a direct P7 configuration equal 7, this proves Statement 1. □

## 3. Classical groups: odd-index reduction

**Lemma O.** Let S be a finite group carrying a direct P7 configuration with subgroups H_1,…,H_8, [S:H_i]=7a_i and pairwise coprime a_i. Then at least six H_i have odd index and v_7([S:H_i])=1.

*Proof.* At most one a_i is even and at most one is divisible by 7. □

**Lemma P.** If S is of Lie type in characteristic 7, at most one H_i lies in a proper parabolic subgroup.

*Proof.* By (L), D(S) divides the index of every subgroup contained in a proper parabolic. Two such H_i would force D(S)|7. But D(S)≡1 (mod q) and D(S)≥2, so D(S)≠1,7. □

**Lemma Q (from (M)).** Let S be classical in characteristic 7 with S≠PSL2(7),PSL2(49). Every maximal subgroup M of odd index that is not a parabolic subgroup satisfies v_7([S:M])≥2.

*Proof.* Go through Maslova's Theorem items with q=7^f. Items (9), (10)(ii), (12), (14), (16), (17), (19) and (21)–(23) require a prime q≡±3 (mod 8), q≡±3,±13 or 5 (mod 40), q≡±11,±19 (mod 40), characteristic 5, q≡5 (mod 8) or q≡3 (mod 8), all impossible for q=7^f. Item (13) occurs only in PSL2(7), and (11) for f=2 only in PSL2(49). Item (2) consists of subspace stabilizers in PSL_n, which are parabolic. In each remaining item the 7-part of |M| is at most the displayed product of 7-parts of its classical factors, times |Sym(k)|_7 for a wreath product on k blocks, and its index valuation is:

- (1) subfield C_S(σ), q=q_0^r with r an odd prime dividing f: fN(1−1/r)≥2N≥2, where N≥1 is the number of positive roots of the type;
- (3) PSU_n or PSp_n, stabilizer of a nondegenerate m-space: f·m(n−m)≥f(n−1)≥2 (unitary, n≥3) and f·m(n−m)/2≥f(n−2)≥2 (symplectic, n≥4, m even);
- (4) PΩ_n, n=2a+1≥7, stabilizer of a nondegenerate 2b-space: f·b(n−2b)≥2;
- (5) PΩ^ε_{2a}, a≥4, stabilizer of a nondegenerate m-space: f(2bc+b+c) with m=2b+1, b+c=a−1≥3, if m is odd; f·2b(a−b)≥6 if m=2b is even;
- (6)(i), (7)(i), (8), (10)(i), decompositions into k≥2 isometric blocks of dimension m≥2: fm²k(k−1)/2−v_7(k!) or fm²k(k−1)/4−v_7(k!), both at least 2;
- (6)(ii), (7)(ii), m=1: fn(n−1)/2−v_7(n!) for n≥3, at least 3. For n=2 in (6)(ii), q≡1 (mod 4) forces f even and the valuation is f≥2;
- (15) D_{q+1} in PSL2(q) with 7<q≡3 (mod 4), so f odd and f≥3: valuation f≥3;
- (18), (20) PSp4(q).2 in PSL4(q) or PSU4(q): valuation 2f≥2.

The exceptional cases are S4<PSL2(7), of index 7 with valuation 1, and PGL2(7)<PSL2(49), of index 175 with valuation 1. □

**Proof of Statement 2.** Suppose S carries a direct P7 configuration. By Lemma O at least six H_i have odd index and v_7=1, and by Lemma P at least five of them lie in no proper parabolic. Such an H_i lies in some maximal subgroup M_i of odd index with v_7([S:M_i])≤1. If v_7([S:M_i])=0, then M_i contains a Sylow 7-subgroup and is parabolic by (L), which is impossible. So M_i is a non-parabolic maximal subgroup of odd index with valuation 1, contradicting Lemma Q. □

**Proof of Statement 3.** |PSL2(49)|=58800 does not divide 2520=7!/2, so the simple group PSL2(49) has no subgroup of index at most 7: a faithful coset action would embed it in A_7. In a direct P7 configuration all cofactors a_i would therefore exceed 1 and be pairwise coprime divisors of |S|/7=8400=2⁴·3·5²·7. That requires eight distinct primes, but only four occur. □

## 4. Boundary of the statements

Statement 1 is unconditional at the scope of (B) and (Z), and requires no Sun7. Statement 2 rests on (M) and the unreviewed (L), and yields only absence of direct P7. Statement 3 is elementary given the order of PSL2(49). PSL2(7) remains outside this packet.

## 5. Optional consequence

With the prior arbitrary-group Sun7 statement at its named written-composition scope, `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md` SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`, and the prior R8 implication, Statement 2 gives Sun8 for the classical groups covered there. The full Sun7 proof DAG is not replayed, and this is not an unconditional statement.

## 6. Finite checks and review obligations

The author's checker `frontier-20261029-char7-arithmetic-check-v1.py` SHA `2a3e85b8286b43dda8bc62a1b407c25081a9d3bab29308a325b524a89c464b27` (4536 bytes) ran in the author's eval kernel on 2026-10-29. It reproduced the nine cyclotomic factorizations above using deterministic Miller–Rabin and a seeded Pollard rho, with every product remultiplied, and identified the p-primitive prime factors by multiplicative order. It confirmed every Table C size condition used for q=7 and q=49, and the four-prime support of |PSL2(49)|/7. These are exact arithmetic checks only.

A disjoint reviewer should verify the reading of Maslova's item list and of BBGT Table C, including the α/β definitions and the reading of the symbols □/⊠, which are not used here because every size condition is met through f or r. They should also check each valuation formula in Lemma Q, the p-primitivity argument for the α/β conditions, and Lemmas O and P. The source classification proofs, the owner's Lie-type lemmas, the Sun7 interface and any priority question remain unreplayed or unreviewed.
