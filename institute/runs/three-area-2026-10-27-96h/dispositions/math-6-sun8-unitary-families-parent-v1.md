# Sun8 for unitary families: odd prime-power dimension, even dimension and the five small-support endpoints

Native clock observed before writing: **2026-10-28T18:43:50-0700 PDT** (last `/bin/date` observation recorded by the parent exact-check cell; this file was written after it). Same-harness written support only; not formal/kernel, human, configured-family, executable or novelty acceptance. Prospective authority: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Inputs actually read by Main

| Input | SHA-256 | Read |
|---|---|---|
| Review manifest `review-waves/f74-unitary-family-source-review/manifest-v1.json` | `972b4cb761a5352a28db76e303a9ef450be2b71d5e28239e6886ea71d7c37f43` | complete, at freeze |
| PSU3 q=4 source qualification `frontier-20261028-psu3-q4-source-qualification-v1.json` | `cd1de7418b5c790d122eaed5360bda5aa3fff034c4f7b0f3a229131dd07d5d35` | complete, before freeze |
| Odd candidate `frontier-20261028-unitary-odd-primepower-dimension-v1.md` | `252cdb33e748fc6d2cceec477df9fac8b4b3a15855bb91d25bfe6f17fa0b6424` | complete raw read before freeze |
| Even candidate `frontier-20261028-unitary-even-dimension-v1.md` | `b397a601924663a029619737146087d985ff23d47851618d53e9f3dcac038f85` | complete raw read before freeze |
| PSU3 candidate `frontier-20261028-psu3-all-fields-v1.md` | `c32a27c4e2c71cf76e3b129d37513dba9680da34cf4186a35d1d70126b7b8e7b` | complete, before the earlier f65 review; adopted in [the PSU3 disposition](math-6-sun8-psu3-all-fields-parent-v1.md) |
| Review return `review-waves/f74-unitary-family-source-review/review-v1.md` (190 LF) | `2bc52d4fd947f7b28e0ad264524e0a98a121ad0c017ef24bdee6d11559dd6274` | complete, after return |

Candidate bodies are in `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`. Reviewer verdict **F=0 / M=1 / m=1**: the MAJOR is a source-interface discrepancy, not a defect found inside any adopted range.

## Adopted statements, each at its exact conditional scope

`Sun_8(X)`: every eight pairwise-disjoint actual left cosets of finite-index subgroups of X have a pair of original indices with gcd >= 8. All statements import, without reproof: the Baumeister-Burness-Guralnick-Tong-Viet 2024 Theorem 2/Table B unique-Sylow-overgroup rows at G=T, the unitary order/simplicity formulas, and Zsigmondy's theorem as stated in that source. The actual-coset caller (at most one index divisible by r>7; every other subgroup contains a Sylow r-subgroup, lies in a conjugate of the unique maximal overgroup M, so [G:M]>=8 divides its original index) is written and was reconstructed by the reviewer and by Main.

1. **Odd n=t^a>=5, t an odd prime, q=p^f with f>=2:** Sun8(PSU_n(q)). Primitive prime r with ord_r(p)=2nf exists (no Zsigmondy exception), r>=2nf+1>2n+1, beta(n,-1) holds for every odd prime k|f, r survives the projective denominator.
2. **Same odd n, f=1 with 2n+1 composite,** and **same odd n, f=1 with some primitive prime r of p^{2n}-1 satisfying r>2n+1 or r^2 | p^n+1:** Sun8(PSU_n(p)). The second statement is existential exactly as displayed; the complementary prime-field cases are not asserted.
3. **PSU5(2):** Sun8 by the written small-support count on |PSU5(2)|=2^10*3^5*5*11 (11-adic bound), not by any generic row and not by the source's Magma treatment.
4. **Even n>=4, f>=2:** Sun8(PSU_n(q)) via a primitive prime with ord_r(p)=2(n-1)f, beta(n-1,-1), f>1.
5. **Even n>=6, f=1 with 2n-1 composite:** Sun8(PSU_n(p)).
6. **Even n>=4, f=1, (n,p) != (6,2), with some primitive prime r of p^{2n-2}-1 such that r>7 and (r != 2n-1 or r^2 | p^{n-1}+1):** Sun8(PSU_n(p)). Existential as displayed; complement not asserted.
7. **PSU4(2), PSU4(3):** Sun8 by the written small-support counts on 2^6*3^4*5 and 2^7*3^6*5*7.

PSU3(q), q>=3, remains adopted under the earlier disposition; the f74 return re-reconstructed it and carries the q=4 source-method qualification (the source handles q in {3,4,5} by Magma; the candidate's q=3,5 arguments are independent, q=4 uses the imported statement).

## Carried findings (mandatory with any use of these statements)

- **S1 (MAJOR, source interface, confined to unused branches).** The literal Table B generic even row would, with the square-residue alternative, appear to give uniqueness for U6(2), r=11 and the odd row for U5(2), r=11, whereas Proposition 6.4 names U4(2), U4(3), U5(2), U6(2) as separately treated and reports uniqueness among them only for U5(2) with the L2(11) type. Neither adopted statement uses a generic row or the square-residue branch on those four socles; U6(2) is explicitly excluded and the other three are paid by order/support counts. Do not extrapolate the printed generic rows to those four groups.
- **S2 (MINOR, transcription).** The odd candidate presents a sufficient subset of the Table B f-alternatives (omits the f>1 branch, writes `>` for `!=`); in the primitive setting r>=2n+1 the two are equivalent and no adopted application loses a hypothesis.
- The source's q=4 PSU3 case and its four small unitary socles rest on Magma computations that were not reproduced.

## Parent exact checks

Receipt `review-waves/f74-unitary-family-source-review/parent-unitary-exact-checks-v1.json`, SHA-256 `d41e397f0f2b3030cd530f97024c0dc8a8783e16f5762604d61782b4c31bcdd8` (standard-library arithmetic in the parent eval kernel; clocks inside the receipt):

- The five endpoint orders 6048, 126000, 25920, 3265920, 13685760 were reproduced from the formula, and the reviewer's divisor max-clique overapproximations (42,4), (113,5), (64,4), (217,5), (258,5) were reproduced by an independent Bron-Kerbosch search over all divisors >=8 with edges exactly at gcd in 2..7.
- 7^3+1=2^3*43 with ord_43(7)=6; 2^10-1=3*11*31 with ord_11(2)=10, ord_31(2)=5 and 11^2 not dividing 33; 3^6-1=2^3*7*13 with ord_7(3)=6 and ord_13(3)=3, so (4,3) has only the primitive prime 7.
- Eleven least-primitive-prime controls: all f>=2 cases and the odd f=1 cases (5,3)->61 and (7,2)->43 pass beta, divisibility and the threshold. The least primitive primes of (10,3)->19=2n-1 and (5,7)->11=2n+1 do not pass the threshold; both cases are nevertheless decided by a larger primitive prime, since 3^9+1=4*7*19*37 with ord_37(3)=18 and 7^5+1=8*11*191 with ord_191(7)=10. The adopted f=1 statements are existential over primitive primes, exactly as written.

## Not established

Unrestricted Sun8; U6(2) and the other excluded prime-field cases; the source classification proofs, the Zsigmondy proof and the unitary order/simplicity proofs; the S1 editorial resolution; any human, formal/kernel, independent-model or publication acceptance; novelty or priority. Earlier Sun-lane quarantines and historical records keep their recorded statuses and are not premises here.
