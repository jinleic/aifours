# Sun8 and three-index exclusion for six exceptional simple-group families: E8, twisted E6, E7, E6, F4 and triality

Native clock observed before writing: **2026-10-28T18:43:50-0700 PDT** (last `/bin/date` observation recorded by the parent exact-check cell; this file was written after it). Same-harness written support only; not formal/kernel, human, configured-family, executable or novelty acceptance. Prospective authority: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Inputs actually read by Main

Candidate bodies are in `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`; hashes are those pinned in `review-waves/f75-exceptional-simple-families-review/manifest-v1.json` (SHA-256 `e304684162fcf5f8b39ec94796673bf1e7f71db06a34a1192a9825f06536f715`).

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| E8 locator erratum (JSON) | `8f2d8491caf0bf92af12b2eb2608205d7f181db83e198ad3318071f2dfb7128b` | 10 | complete, before freeze |
| E8 candidate | `e4ca53aa65035bbca70b0a84a52055fd1e938d3d48176e8eed72aff7961f4d87` | 116 | complete raw read before freeze |
| twisted-E6 beta sign qualification (JSON) | `bab095074a9f0aa1ae41cbc32e48dad957887e2900717f8552ffaa731330542a` | 10 | complete, before freeze |
| twisted-E6 candidate | `940037b4b32bf8da41c636c344377d0d57f99609ec17dd359ca56304e13e5574` | 88 | complete raw read after the return, before this disposition |
| E7 candidate | `4403532d00653c182e2b3120186fcfc6a1f173e250ba4da7b0889251d4e69716` | 68 | same |
| E6 candidate | `37d8d288a4e217d10f6811aec5022bfce3574f1e0cae83fe44a47fa85cf44a4d` | 57 | same |
| F4 candidate | `64494b4c744c90c26b886765c621b60761b8c6e300e77c4dea931111e68b379e` | 52 | same |
| triality candidate | `77f9daa875be02fa92454de0ac9c35e46f369fb6343e13f3014981aa5395fc65` | 23 | same |
| Review return `review-waves/f75-exceptional-simple-families-review/review-v1.md` (230 LF) | `93007ad15eefc088891d732d23f6eca12a195f273feb3c8d8e42dc62f48381f1` | 230 | complete, after return |

Reviewer verdict **FATAL 0 / MAJOR 0 / MINOR 1** at the stated conditional scopes; the published classifications and their Magma computations were not reproduced by anyone in this run.

## Adopted statements, each conditional on its named external inputs

Common imports: Baumeister-Burness-Guralnick-Tong-Viet 2024 (arXiv:2307.13976v2) Theorem 2/Table C rows and Propositions 7.3, 7.5-7.8, 7.10 at G=T; the displayed group orders and simplicity; Zsigmondy as stated in that source's section 2.1; for E7(3), E6(4) and even-characteristic F4 additionally Craven's corrected F4/E6 tables (arXiv:2103.04869v4, Theorem 1.1, Tables 1, 2, 8, 9), Craven's E7 Corollary 1.2 with Tables 1.1 and 4.1 (arXiv:2201.07081v2), and the ATLAS orders of J3, PSL2(19) and 2F4(2)'. The common caller (section 4 of the return) is written: for r>7 dividing |G| and G simple, at most one of three pairwise-gcd<=7 proper indices is divisible by r, each other subgroup contains a Sylow r-subgroup and lies in a maximal overgroup, and either a unique overgroup or a common index divisor D>7 of every maximal overgroup gives the contradiction; eight actual disjoint cosets cannot involve G itself.

1. **E8(q), every q:** Sun8, via r with ord_r(q)=30, alpha(30,1) and `r>61 or |R|>r` (f=1 from F(p)=Phi30(p)>31*61 for p>=3 and F(2)=331; f=2 from ord_r(p)=60 and F(p^2)>=80581; f>=3 from ord_r(p)=30f). The separate r=61 source branch is not used. Carry the **locator erratum**: the E8 proof is Proposition 7.10, not 7.8.
2. **2E6(q), every q:** Sun8, via r with ord_r(q)=18 and the `f>1`, `r>19`, `|R|>r` or (p=2: nonsquare mod 5) alternatives. Carry the **sign discrepancy**: Table C prints beta(9,1) while Proposition 7.7 prints beta(9,-1); for every f>=2 prime chosen (ord_r(p)=18f) both signs hold, and for f=1 both are vacuous; the reviewer's exact example (p,f,r)=(2,5,19) shows the two printed hypotheses genuinely differ and neither is silently identified.
3. **E7(q), every q:** no three proper subgroup indices with pairwise gcd<=7 (hence no eight-coset Sun8 counterconfiguration and no direct P7 counterconfiguration). For q=3 the Sylow 37-overgroups are not unique; the common divisor D=3^27 of both tabulated overgroup types (rank type of order 4|2E6(3)|, almost-simple PSL2(37)) pays the claim.
4. **E6(q), every q:** same three-index exclusion. For q=4 the overgroups of a Sylow 19-subgroup are bounded by the rank type PSL3(64).3 and almost-simple J3 or PSL2(19) socles with outer order 2 allowed; every index is divisible by D=2^54. The q=4 PSL2(19) ordinary row and novelty row are kept distinct and not conflated.
5. **F4(q):** odd q via a unique overgroup using only `r>13 or |R|>r`, which appears in both printed field-alternative formulations; even q via D=q^12 dividing every maximal-overgroup index extracted from the corrected simple-group tables (3D4(q).3, 2F4(q) when f odd, subfield exclusion by the order of 2 modulo r, PSL4(3).2 at q=2 and PSL2(27) at q=8). Carry the **F4 discrepancy**: Proposition 7.5 prints `f not in {1,3}` where Table C prints `f != 3`; neither branch is used.
6. **3D4(q), every q:** three-index exclusion via the unique overgroup under the proposition's subfield condition, checked for every prime k|f.

Carry **m1**: the F4 candidate cites Maroti-Tamburini Bellani Table 9 for the 2F4(q) order while including q=2, but that table prints q=2^(2k+1), k>=1; the q=2 endpoint 35,942,400=2^12*3^3*5^2*13 is supported by the ATLAS 2F4(2)=2F4(2)'.2 page instead.

## Parent exact checks

Receipt `review-waves/f75-exceptional-simple-families-review/parent-exceptional-exact-checks-v1.json`, SHA-256 `1bfdfbe5588193c2f076cbed2e734f477a6b38f8025597338f2cdd840e660ced` (standard-library arithmetic, clocks inside):

- All five polynomial identities ((x^3-1)A=x^9-1, (x^3+1)B=x^9+1, (x^2+1)C=x^6+1, Phi2*Phi6*Phi10*F=x^15+1, (x^2-x+1)(x^2+x+1)C=x^8+x^4+1) verified by integer coefficient convolution; endpoints F(2)=331, F(4)=61*1321, A(2)=73, B(2)=3*19, B(3)=19*37, B(4)=37*109, B(5)=3*5167, C(2)=13, C(3)=73.
- E8 primes: ord_331(2)=30, ord_61(2)=ord_1321(2)=60. Twisted-E6 sign example: ord_19(2)=ord_19(32)=18 with 2^9 = -1 mod 19; 2 is a nonsquare mod 5.
- E7(3): ord_37(3)=18, 3^9 = -1 mod 37, v3(|E7(3)|)=63, v37=1, v3(4|2E6(3)|)=36, |PSL2(37)|=25308 with v3=2; both orders divide |E7(3)|; index 3-valuations 27 and 61.
- E6(4): ord_19(4)=9, v2(|E6(4)|)=72, v19=1, |PSL3(64).3|=281405183754240 with v2=18, |J3|=2^7*3^5*5*17*19, |PSL2(19)|=3420; all three divide |E6(4)|; the minimum index 2-valuation with an outer factor 2 allowed is 54.
- F4 even q=2,4,8: v2(|F4(q)|)=24,48,72 against 2-parts 12f of 3*|3D4(q)| and |2F4(q)| (q=2,8), all dividing |F4(q)|; |2F4(2)|=35942400=2^12*3^3*5^2*13; |PSL4(3).2|=12130560 divides |F4(2)| with index 2-valuation 16. F4 discrepancy example: ord_13(41)=12, v13(C(41))=v13(|F4(41)|)=1 and 3*|3D4(2)| divides |F4(41)| with 13-free quotient.
- Sixteen least-primitive-prime controls (ord_r(p)=mf, ord_r(p^f)=m) for m in {30,18,9,12}. The receipt field `all_k_half_test` records only whether p^(mf/k) != -1 for every prime k|f; it is false exactly in the f=2 cases where p^(mf/2) = -1 mod r, which is the alpha-type condition holding, not a failure of any source hypothesis; the actual alpha/beta conditions at their correct exponents were checked by the reviewer and in the candidates.

## Not established

The source classifications and their Magma computations; the editorial resolution of the twisted-E6 sign and F4 field-alternative discrepancies; unrestricted Sun8, all finite simple direct-P7 factors, or any normal-extension statement; any human, formal/kernel, independent-model or publication acceptance; novelty or priority. The earlier Sun7-to-P7 normal-section results remain separately recorded and are not inputs here.
