# Independent source-bound review: six exceptional simple-group families

**Native clock observed before writing:** `Wed Oct 28 18:33:58 PDT 2026`. **Verdict:** the six written elementary arguments and their stated family-specific conclusions are supported **conditional on the exact external classification, order, simplicity, and primitive-prime inputs below**. The conclusion is not unconditional acceptance of those inputs. **New findings: FATAL 0 / MAJOR 0 / MINOR 1.** The minor source-citation qualification and the already-disclosed source discrepancies are recorded below. This is a same-harness review, not an independent-model, human, formal, or kernel verification. The full published classification proofs, their underlying classification DAG, and their Magma computations were **not reproduced**. No priority or novelty finding is made.

The scope is exactly the six submitted families and the original-index or three-proper-index statements in the submitted files. It is not a classification of all finite simple groups, an arbitrary-group Sun8 proof, a normal-extension theorem, or a proof of the named classification inputs. In particular, a source-statement check below is not a classification-proof check. No held proof body was used.

## 1. Frozen inputs and review order

I read the manifest, then every LF of each of the following eight complete inputs in the order shown. In particular the locator correction preceded E8 and the sign qualification preceded twisted E6. I independently hashed the actual bytes and checked each hash, byte count, and LF count against the manifest; all eight matched. The basename prefix below is `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`.

| Order | Input basename | Bytes / LF | SHA-256 |
|---:|---|---:|---|
| 1 | `frontier-20261028-e8-source-locator-erratum-v1.json` | 954 / 10 | `8f2d8491caf0bf92af12b2eb2608205d7f181db83e198ad3318071f2dfb7128b` |
| 2 | `frontier-20261028-e8-all-fields-v1.md` | 10911 / 116 | `e4ca53aa65035bbca70b0a84a52055fd1e938d3d48176e8eed72aff7961f4d87` |
| 3 | `frontier-20261028-twisted-e6-beta-source-qualification-v1.json` | 1273 / 10 | `bab095074a9f0aa1ae41cbc32e48dad957887e2900717f8552ffaa731330542a` |
| 4 | `frontier-20261028-twisted-e6-all-fields-v1.md` | 8022 / 88 | `940037b4b32bf8da41c636c344377d0d57f99609ec17dd359ca56304e13e5574` |
| 5 | `frontier-20261028-e7-all-fields-v1.md` | 8770 / 68 | `4403532d00653c182e2b3120186fcfc6a1f173e250ba4da7b0889251d4e69716` |
| 6 | `frontier-20261028-e6-all-fields-v1.md` | 7414 / 57 | `37d8d288a4e217d10f6811aec5022bfce3574f1e0cae83fe44a47fa85cf44a4d` |
| 7 | `frontier-20261028-f4-all-fields-v1.md` | 7652 / 52 | `64494b4c744c90c26b886765c621b60761b8c6e300e77c4dea931111e68b379e` |
| 8 | `frontier-20261028-triality-all-fields-v1.md` | 3089 / 23 | `77f9daa875be02fa92454de0ac9c35e46f369fb6343e13f3014981aa5395fc65` |

Manifest `manifest-v1.json`: 3904 bytes, 60 LF, SHA-256 `e304684162fcf5f8b39ec94796673bf1e7f71db06a34a1192a9825f06536f715`. The hashes bind the reviewed local snapshots, not future modifications or any predecessor/held material.

## 2. Published-source inspection and finding

I directly inspected the published 2024 Theorem 2, its exceptional Table C and Remark 9.2, and the complete statements and relevant proof discussions in Propositions 7.3, 7.5–7.8 and 7.10. I separately inspected Craven's corrected 2025 F4/E6 Theorem 1.1 and its Tables 1, 2, 8 and 9; the E7 2025 Corollary 1.2 and Tables 1.1 and 4.1; the two cited ATLAS order/outer-order pages; and the cited group-order table. For the q=2 Ree endpoint I also inspected the ATLAS Tits-group page. The following are hashes of the raw public bytes retrieved for this review, not hashes of a downloaded local evidence file or assertions that a public server can never change its rendering:

| Source | Raw bytes | SHA-256 |
|---|---:|---|
| [Baumeister–Burness–Guralnick–Tong-Viet v2, 2024](https://arxiv.org/html/2307.13976v2) | 2262535 | `6cf5530f8386133e7208e6e0b77b1b44de78d8546549f2c3faf5144d403f9bfc` |
| [Craven F4/E6 corrected v4, 2025](https://arxiv.org/html/2103.04869v4) | 2629616 | `eb172fd70edb59404dd29691373bd11bd4e3d25559e81cd2feb4666295151fbd` |
| [Craven E7 v2, 2025](https://arxiv.org/html/2201.07081v2) | 2169981 | `cbb349ec5fb7f03b8b28788ab3428a838ed61b22ae19d5830a3f1e8f8d7c3901` |
| [ATLAS J3](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/J3/) | 66686 | `fcf41712f8d7a2c91423f0961b315277fef5e345821952c5b7bb945d3af26abf` |
| [ATLAS L2(19)](https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L219/) | 35431 | `53e4bbd995dea97ef48df8974e85d48eed32060f14593c15f58f0427914a79ee` |
| [Maróti–Tamburini Bellani, Table 9](https://www.renyi.hu/~maroti/centralizer12.pdf) | 230097 | `3ddf12b8c438bdd207d9b77b2cd8eeddd2a28a6f629df4938ba8f95915f15ae3` |
| [ATLAS ²F4(2)′](https://brauer.maths.qmul.ac.uk/Atlas/exc/TF42/) | 29444 | `9ac0a5956c434eced6d4170e7d1fc30f7c6d1338ee44c455e44df88ea6c98d6a` |

**m1 — q=2 Ree source range.** The F4 candidate cites Maróti–Tamburini Bellani Table 9 as a source for its displayed ²F4(q) order while explicitly including the full group at q=2. That table prints the Ree range `q=2^(2k+1), k≥1`, so the table as stated does **not** itself cover k=0. This is a citation-scope issue, not an observed error in the q=2 value: the independently inspected ATLAS page gives `|²F4(2)′|=17,971,200` and explicitly identifies `²F4(2)=²F4(2)′.2`, giving `35,942,400=2^12·3^3·5^2·13`. This equals the candidate's full-group formula at q=2. Carry the ATLAS endpoint qualification rather than attributing that endpoint to the displayed Table 9 range.

The already supplied E8 locator erratum is correct: Proposition **7.10**, not 7.8, is the E8 proof; Proposition 7.8 is E7. This review keeps the original candidate and additive erratum distinct. The sign and F4 table/proposition disagreements in §3 are real source-level discrepancies, material outside the particular selected branches, not newly found errors in these sign-robust/threshold-robust submitted arguments. I do not resolve them by declaring either publication a typo.

## 3. Exact theorem rows, discrepancies, and trust cut

The 2024 Theorem 2 assumes an almost simple G with socle T, an odd prime r, a Sylow r-subgroup R, and G/T an r-group. All six applications set **G=T**, satisfying that quotient condition. Let `r_d` mean `ord_r(q)=d`. Remark 9.2 defines α(m,ε) by `(q^(1/k))^m != ε (mod r)` for every prime `k|f`, `k!=r`; β uses only the odd such k. The used rows and the extra alternatives not used by the candidates are:

| T | Printed Table C and proposition statements at the used primitive degree | Relevance |
|---|---|---|
| E8(q) | `r_30`; α(30,1), and `r>61` or `|R|>r`; Table C also has the separate `|R|=r=61` branch with `f>2`, or `f=2`, `i=15`, `d_p(r)∈{15,30}`. Proposition 7.10 discusses the 31 exotic-local and 61 almost-simple exceptions. | Only the first two threshold alternatives are used. The source's extra 61 branches are not assumed. |
| ²E6(q) | `r_18`; Table C prints **β(9,1)**, while Proposition 7.7's subfield discussion prints **β(9,−1)**. Both print, among the no-extra-overgroup alternatives, `f>1`, `r>19`, `|R|>r`, or `f=1` and p nonsquare mod 5; an f=1 mod-19 alternative is also printed. | Both signs are checked for the actual selected r, so the discrepancy is not silently identified. |
| E7(q) | `r_18`; α(18,1), and `f>2` or `r>37` or `|R|>r` or `(q,r)=(2,19)` among further quadratic branches. Proposition 7.8 gives the relevant 37-socle alternatives. | q=3,r=37 is not represented as unique; it is separately bounded. |
| E6(q) | `r_9`; α(9,1), and `f>2` or `r>19` or `|R|>r`, with additional quadratic branches. Proposition 7.6's possible r=19 almost-simple socles are J3 and L2(19). | q=4,r=19 is separately bounded; no uniqueness is assumed. |
| F4(q), odd q | `r_12`; α(6,−1), and `r>13` or `|R|>r`, with field-degree and mod-7 alternatives. | Only the common threshold/square branches are used. The even case is not taken from this odd-q row. |
| ³D4(q) | `r_12` and `(q^(1/k))^6 != −1` for `k∈π(f)\{3,r}`. | The chosen r meets the stronger condition for every `k|f`. |

**Concrete sign discrepancy.** With p=2, f=5, q=32, r=19, exact modular arithmetic gives `ord_19(2)=ord_19(32)=18` and `2^9≡−1 mod 19`. Thus for k=5 the printed β(9,1) holds but β(9,−1) fails. Both `|²E6(32)|` and `|²E6(2)|` have 19-valuation 1 and the latter order divides the former. This exhibits a genuine difference in the printed hypotheses; the arithmetic does not independently certify any embedding or adjudicate the conflicting source statements. By contrast, every f≥2 prime chosen in the candidate has `ord_r(p)=18f`, so `(p^(9f/k))^2!=1` for every prime k|f: **both** signs hold. For f=1 both β conditions are vacuous.

**Concrete F4 discrepancy.** Proposition 7.5 prints the field alternative `f∉{1,3}`, while Table C prints `f!=3`. They differ at f=1. For q=p=41 and r=13, `ord_13(41)=12`, `C(41)=2,824,081` has `v_13=1`, and `v_13(|F4(41)|)=1`. The order of `³D4(2).3` divides `|F4(41)|` with 13-free quotient; the proposition's discussion specifically names this extra type for the relevant order-13 situation. This demonstrates why neither printed condition should be silently substituted for the other. The candidate uses neither field alternative: it always selects `r>13` or `|R|>r`, appearing in both. The calculation alone is not an independent subgroup construction.

The 2025 F4/E6 source calls its list complete and states that the v4 tables incorporate known corrections; its abstract reports computational algebra and supplemental Magma. The 2025 E7 source gives a partial general classification but its Corollary 1.2 makes characteristic 3 complete at the cited tables. This review imports those exact statements; it neither reruns Magma nor proves the classification, group simplicity/order formulas, or Zsigmondy. The 2024 paper states the needed Zsigmondy theorem in §2.1; our uses have exponents 9f≥27, 12f≥12, 18f≥36/54, or 30f≥90 as applicable, away from its stated exceptions.

## 4. Common original-index caller — PASS at its stated hypotheses

Let G be finite nonabelian simple, r>7 divide |G|, and let R be a Sylow r-subgroup. If `[G:H]` is r-free, then H contains a Sylow r-subgroup; after conjugation it contains R and lies in some maximal proper `M` containing R. The original index, without moving the original coset or requiring the same conjugate M, is divisible by `[G:M]`.

For three **proper** subgroup indices with pairwise gcd≤7, at most one can be divisible by r, so two indices arise this way. If all maximal overgroups of R have a common index divisor D>7, those two original indices have gcd≥D. If R has exactly one such M, simplicity makes the coset action on G/M faithful; an index n≤7 would embed G in S_n, impossible since r divides |G| but not n!, and thus D=`[G:M]`≥8. The proof uses no disjointness for the three-index statement.

For eight actual pairwise-disjoint nonempty cosets, none of their subgroups can be G, since a coset of G is all of G. The same original-index argument therefore applies; the E8 and ²E6 callers explicitly use at least two of the at least seven r-free indices. This establishes the stated Sun8 conclusion conditional on the selected Sylow-overgroup input. It does not prove anything about arbitrary groups or a normal extension.

## 5. Independent polynomial and primitive-order reconstruction

Write

`A=x^6+x^3+1`, `B=x^6−x^3+1`, `C=x^4−x^2+1`,

`F=x^8+x^7−x^5−x^4−x^3+x+1`.

I independently multiplied coefficient arrays over the integers and obtained the exact identities

```
(x^3−1) A = x^9−1;       (x^3+1) B = x^9+1;
(x^2+1) C = x^6+1;       (x+1)(x^2−x+1)(x^4−x^3+x^2−x+1) F = x^15+1;
(x^2−x+1)(x^2+x+1) C = x^8+x^4+1.
```

The universal residue arguments, not the finite controls, justify the following: A and B are odd, and their 3-valuation is at most 1; C is coprime to 6; F is coprime to 30 for every integer x. For A/B, the exceptional 3-residue follows from `x^3≡±1 mod 9` when `x≡±1 mod 3`. For F, reduce x modulo 2, 3, 5. The common-root reduction `A≡3 mod (x^3−1)`, `B≡3 mod (x^3+1)`, and `C≡3 mod (x^2+1)` yields, for primes r>3 dividing A/B and for r dividing C, respective orders **9, 18, 12**. For F, r∤30 and the derivative of `x^15+1` is nonzero at a root, so its displayed factors cannot share that root; the only possible orders 2, 6, 10 are excluded and the order is **30**. Consequently a prime dividing F(x²) has order **60** for x and order 30 for x². These are all-variable deductions, not a claim that arbitrary cyclotomic divisors are automatically primitive.

Independent executed integer controls checked those five coefficient identities and all residues x=0,…,179. Exact endpoint values: `F(2)=331` (prime by trial division), `F(4)=80581=61·1321`, `A(2)=73`, `B(2)=57=3·19`, `B(3)=703=19·37`, `B(4)=4033=37·109`, `C(2)=13`, `C(3)=73`. The strict bounds used in the written proofs are `F(x)>31·61` for x≥3, `B(x)>3·19` for x≥3, `B(x)>3·19·37` for x≥5, `A(x)>3·19` for x≥2, and `C(x)>13` for odd x≥3. Thus, if every allowable small primitive divisor occurred at most once, the indicated product would be too small; a larger prime or a repeated small prime follows. A repeated factor r² divides an actual group-order factor, and the relevant central divisor is at most 3 and coprime to r, so the **actual Sylow r-subgroup** has order >r.

As additional bounded square-branch controls, I independently found these prime x with the exact indicated valuation and primitive order:

| Polynomial | r | x | `v_r` | `ord_r(x)` |
|---|---:|---:|---:|---:|
| F | 31 | 229 | 2 | 30 |
| F | 61 | 1693 | 2 | 30 |
| A | 19 | 389 | 2 | 9 |
| B | 19 | 127 | 2 | 18 |
| B | 37 | 691 | 3 | 18 |
| C | 13 | 19 | 2 | 12 |

These examples exercise the arithmetic alternative; they do not replace the universal inequalities, show that the alternative is necessary for those x, or classify subgroups. Primitive-order checks also gave `(p,f,m,r)=(2,1,9,73),(2,2,9,19),(2,1,12,13),(2,2,12,241),(2,3,12,37),(2,1,18,19),(2,2,18,37),(2,1,30,331),(2,2,30,61)`, with `ord_r(p)=mf` and `ord_r(p^f)=m`. A bounded search below 6000 found no such r for some higher-degree controls; that is only a bounded search result and is not used to challenge Zsigmondy.

## 6. Claim-by-claim family verdicts

### E8(q) — PASS conditional on §3 inputs and the locator erratum

The source order is `q^120 ∏_{d=2,8,12,14,18,20,24,30}(q^d−1)`. For f=1, all r|F(p) have order 30, hence r≡1 mod 30; below or at 61 only 31 and 61 can occur. `F(2)=331`; for p≥3 the strict product bound yields `r>61` or r²|F(p). For f=2, r|F(p²) has `ord_r(p)=60`, so r≡1 mod 60 and the only possible r≤61 is 61; the bound supplies r>61 or 61². In this case `p^30!=1 mod r`, the sole α test. For f≥3 choose `ord_r(p)=30f`; then r>61, `ord_r(q)=30`, and for every k|f, `p^(30f/k)!=1`. The source α and threshold conditions hold in every branch; r survives in q^30−1 in the displayed order. The actual-coset caller in §4 applies. No use of the separate r=61 source exception is needed.

### ²E6(q) — PASS conditional on §3 inputs and both-sign qualification

The source projective order is `q^36(q²−1)(q^5+1)(q^6−1)(q^8−1)(q^9+1)(q^12−1)/gcd(3,q+1)`. For f≥2 choose `ord_r(p)=18f`; then r≥37, `ord_r(q)=18`, r divides q^9+1 and cannot be cancelled by the denominator. Both β signs hold as shown in §3, and the source's f>1 and r>19 alternatives hold. For f=1,p≥3, B(p) and the 3-adic bound yield `r>19` or `r=19` with r² dividing the group order. For p=2, B(2)=3·19 and neither numerical alternative is asserted; 2 is a nonsquare modulo 5, and the distinct source quadratic branch applies. Both β conditions are vacuous for f=1. The source disagreement is preserved rather than resolved, and §4 pays the original-coset conclusion.

### E7(q) — PASS conditional on the stated 2024/2025 classification and order inputs

The displayed projective order has `q^63`, factors at degrees `2,6,8,10,12,14,18`, and denominator `gcd(2,q−1)`. For f≥3, a primitive r for p^(18f) gives α(18,1) and the f>2 branch. For f=2, every prime factor of B(p²) has `ord_r(p)=36`, is ≥37, satisfies `p^18!=1`, and B(p²)≥4033>37 gives `r>37` or 37². For f=1,p≥5, B(p)>3·19·37 gives `r>37` or a square; for p=2 use the source's explicit (2,19) branch. No such uniqueness claim is made for p=3.

For the exceptional q=3, `ord_37(3)=18`, `3^9≡−1`, `3^6≡26`, and `v_37(|E7(3)|)=1`. The 2024 proposition restricts additional types to the ²E6 rank type and an almost-simple L2(37) socle after subfield exclusion. The 2025 characteristic-3 Corollary and Table 4.1 give rank order `4|²E6(3)|`: at q=3, `d=2`, `e′=1`, and the written table's factors produce 4. Table 1.1 gives PSL2(37), two classes because 3 is a square mod 37 (`15²≡3`). Its order is `37(37²−1)/2=25308`. Thus the corrected source actually has both relevant sorts, not a unique-overgroup case. For a fixed R, the r-free index property permits conjugating representatives to contain R; class counts are not themselves counts of subgroups containing R.

Independent exact controls found `v_3(|E7(3)|)=63`, `v_3(4|²E6(3)|)=36`, `v_3(25308)=2`; both displayed orders divide the G order, giving respective index valuations 27 and 61. Hence D=3^27 divides every relevant maximal-overgroup index at the named classification cut, proving the three-proper-index claim by §4. The E7 paper's unresolved other-characteristic cases and its PGL3/PGU3 ambiguity are not turned into a general complete E7 classification here.

### E6(q) — PASS conditional on the stated 2024/2025/ATLAS inputs

The source order is `q^36∏_{d=2,5,6,8,9,12}(q^d−1)/gcd(3,q−1)`. For f≥3, `ord_r(p)=9f` implies `ord_r(q)=9`, r>7 and α(9,1), so the f>2 source branch applies. For f=1, A(p)≥73>3·19 gives `r>19` or r². For f=2,p≥3, any r>3 in B(p) has `ord_r(p)=18`, `ord_r(p²)=9`, and `p^9≡−1`, the α test; B(p)≥703>3·19 gives the numerical branch. The only excluded endpoint is p=2,f=2.

At q=4, r=19 has `ord_19(4)=9`, `2^9≡−1 mod 19`, and `v_19(|E6(4)|)=1`. The 2024 Proposition 7.6 bounds the relevant maximal types by rank `A2(4³)` or almost-simple socles J3 or PSL2(19); Craven corrected Table 9 gives rank shape `PSL3(64).3`. Corrected Table 2 prints an ordinary PSL2(19) row with `p≡±2 mod 5`, `q=p²`, which includes p=2,q=4, **and separately** an explicit q=4 novelty row. One must not conflate these rows or infer that every q=4 embedding of that isomorphism type is a novelty. The argument only needs the safe overgroup-of-socle bound, not a chosen embedding or class count. The ordinary J3 row is also at p=2,q=4.

ATLAS directly gives `|J3|=50,232,960=2^7·3^5·5·17·19`, Out order 2; and `|PSL2(19)|=3420=2²·3²·5·19`, Out order 2. Thus all possible almost-simple extensions have 2-part at most 2^8 and 2^3, respectively. Independent exact computation of `|PSL3(64).3|=281405183754240` gives 2-part 2^18, while `v_2(|E6(4)|)=72`. All three types therefore have index divisible by 2^54. Exact quotient valuations using the listed *simple* J3 and PSL2(19) orders are 65 and 70; allowing full outer factors 2 gives 64 and 69. Each displayed integer order divides the G order, which is an arithmetic check, not proof that each possible extension is a maximal subgroup. D=2^54 proves the stated three-index claim at the imported type-list cut.

### F4(q), odd characteristic — PASS conditional on the common source branches

The source order is `q^24(q²−1)(q^6−1)(q^8−1)(q^12−1)`. For f≥2, `ord_r(p)=12f` implies `ord_r(q)=12`, r>13, and `p^(6f/k)!=−1` for all k|f by squaring. For f=1, C(p) is coprime to 6 and each prime factor has order 12; C(p)≥73>13 gives either r>13 or 13². α(6,−1) is vacuous for f=1. The §3 F4 source discrepancy is avoided, not resolved.

### F4(q), even characteristic — PASS conditional on the corrected full simple-group table and order inputs

For q=2^f choose `ord_r(2)=12f`. Then `ord_r(q)=12`; r=13 for f=1 and r>13 for f≥2. I reconstructed the relevant unmarked **simple-group** inventory from corrected Tables 1 and 8, rather than treating novelty maximals in a graph extension as simple-group maximals:

1. Table 8's two parabolic shapes `[q^15].Sp6(q)×(q−1)` and `[q^20].(SL2(q)×SL3(q)).(q−1)`; Sp8(q); `PΩ8⁺(q).Sym(3)`; and the SL3/SU3 product rows have semisimple factors only from q^d−1 with d in {1,2,3,4,6,8}, plus extension factors 2 or 3. None contains the selected order-12 r. The table's `³D4(q).3` row has two simple-group classes, both of the same order.
2. A field subgroup F4(q0), q=q0^k with prime k|f, cannot contain r: its semisimple exponents are 2,6,8,12 in q0, and divisibility would force `12f | (f/k)d`, impossible for k≥2 and d≤12. This uses the order of **2** modulo r, not merely the order of q.
3. The unmarked `²F4(q)` row is allowed when f is odd; it is retained as a possible r-containing type. The marked `Nov.` rows are for almost-simple groups inducing the graph automorphism and are not assumed maximal in the simple group. At q=2 use the full ²F4(2), not just its derived subgroup.
4. Reading every Table 1 row at p=2 leaves PSL4(3).2₂ at q=2 and PSL2(27) at q=8. The apparent PSL2(17), q=p² row does not apply: p=2 is not in its printed nonsquare residue set modulo 17; its other row explicitly excludes p=2. All other rows exclude p=2 or the relevant field. `|PSL4(3).2₂|=12,130,560`, 2-part 2^8. `|PSL2(27)|=9828=2²·3³·7·13`; at q=8 the chosen r has order 36 mod 2, hence r>13 and cannot divide it.

The explicit imported orders are

```
|³D4(q).3| = 3 q^12(q^8+q^4+1)(q^6−1)(q²−1),
|²F4(q)|   = q^12(q^6+1)(q^4−1)(q^3+1)(q−1).
```

For even q their 2-parts are exactly q^12, whereas `|F4(q)|_2=q^24`. All remaining applicable almost-simple possibilities have 2-part at most q^12. Thus every actual maximal M containing R has index divisible by `q^12=2^(12f)>7`, and §4 applies. This inventory conclusion is conditional on the complete corrected source classification, not an independent enumeration of subgroups.

Independent exact order/divisibility controls gave:

| q | `v₂(|F4(q)|)` | `v₂(|³D4(q).3|)` / index | `v₂(|²F4(q)|)` / index where applicable |
|---:|---:|---:|---:|
| 2 | 24 | 12 / 12 | 12 / 12; order 35,942,400 |
| 4 | 48 | 24 / 24 | not a listed Ree field |
| 8 | 72 | 36 / 36 | 36 / 36; order 264905352699586176614400 |

For q=2, the PSL4(3).2₂ order also divides |F4(2)| and its index has 2-valuation 16. For q=4 and q=8 the listed ³D4.3 orders divide the group order; for q=2 and q=8 the full listed Ree order does as well. Those checks do not prove maximality or replace source Magma.

### ³D4(q) — PASS conditional on the source overgroup statement

The proposition gives `|G|=q^12(q²−1)(q^6−1)(q^8+q^4+1)`. Choose `ord_r(p)=12f`; then `ord_r(q)=12` and r≥13. For **every** prime k|f, `p^(6f/k)!=−1`, since a contrary congruence would force the smaller exponent 12f/k to be divisible by the order 12f. This covers, in particular, the source's required subset excluding k=3,r. Moreover q^6≡−1 and q²≠−1 imply r divides C(q); the exact identity in §5 places C(q) in the last order factor. The published unique-overgroup statement and §4 exclude three proper indices, hence the submitted eight-coset configuration. This covers all prime powers, including q=2, at the same named imports.

## 7. Explicit limitations of the controls and verdict

The independent calculations above used newly written integer arithmetic, coefficient convolution, exact divisibility/valuations, modular orders, and trial division; I did not execute the authors' recorded scripts or rerun their reported checks. All examples are finite controls; the all-field inferences are the written inequalities, order arguments and stated Zsigmondy import. Source rows and p-parts were reconstructed to the stated selected scopes; the existence and exhaustiveness of the listed maximal subgroups remain published classification imports, and their proofs, source Magma, group simplicity, Zsigmondy proof, human review, formal checking, and priority screening remain unreproduced. In particular, the source discrepancies in §3 persist even though both selected uses satisfy the common stronger conditions.
