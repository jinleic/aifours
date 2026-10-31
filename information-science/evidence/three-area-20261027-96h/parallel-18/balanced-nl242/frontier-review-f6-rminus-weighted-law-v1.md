# f6 disjoint scientific review — R-minus weighted law and finite-word bridge

Reviewer **InfoBalancedNL242-2-2**, separate info-6 owner; author InfoGuessingRminus-2. Native `/bin/date` observed before this write: **2026-10-28T17:18:56-0700 PDT**; actual review-start observation **17:14:33 PDT**. Assignment was read before the two candidate bodies. No author contact, nested agent, external-model CLI or paid API was used.

## Verdict and exact scope

**0 FATAL / 0 MAJOR / 1 MINOR.** The 88-word FD/decoder construction, rational law, integer entropy inequality, full-domain finite-alphabet type-class caller, and four-word fixed-support counterexample are reconstructed at the exact stated scope. The mathematical strictness certificate was independently verified by **two different exact approaches**. This is same-harness written and local-computation review, not formal/kernel, human, independent-model or novelty acceptance. The lower exponent 649/100 remains strictly below the recorded 20/3 lower bound; no original-target improvement, universal upper bound or global solution follows.

### MINOR M1 — entropy units should be made explicit

In `frontier-20261028-weighted-law-certificate-v1.md` **LF50–55, LF85–93**, J and h are written as H-values, the displayed logarithm is unqualified, and the type estimates use `exp(nJ)` and `exp(nh)`. LF67 and LF93 use natural logarithms, so the intended common nats convention is clear from context, and the argument is correct under it. For unambiguous reuse, insert before LF50: **“Throughout §§2–3, H and unqualified log are measured in natural-log units (nats); the displayed log₂ baseline is stated separately.”** No numerical or mathematical change is needed.

## 1. Inputs, original graph and decoder definition

- Assignment `review-waves/f6-rminus-weighted-law/assignment-v1.json`, SHA-256 `7ea8483509232a9160990f7a8f31207f458ec59f99ee159f16838efc7f990cd0`, 27 LF, read first.
- Weighted candidate `frontier-20261028-weighted-law-certificate-v1.md`, SHA-256 `d223232b8978a18bba5542fcdcdd133cbbc7f321ac057f8278850674b37d2f96`, 116 LF, read completely in raw windows 1–58 and 59–116.
- Fixed-support counterexample `frontier-20261028-fd-bridge-counterexample-v1.md`, SHA-256 `170be249faad78e9438338a2f36330d6e1a55217b2749d3e7be698a536bb1d17`, 89 LF, read completely in raw windows 1–45 and 46–89.
- Registered source transcription `guessing-rminus/prerequisite-derivation-v1.md`, SHA-256 `779ce3f2223e5c4ec7372f22a5f6d3b226ab8e8a919a459cb007e2c7885b1b18`, 230 LF; relevant original game/FD and graph passages, including LF61–82, read. The separately registered definition file has SHA-256 `711ad49d2775284e06ed5074e7f2c9fdb7e9a3215ee9f5e372d817226265b1bb`, 9 LF.
- Primary [Baber–Christofides–Dang–Riis–Vaughan arXiv:1410.8349v2](https://arxiv.org/html/1410.8349v2): retained HTML SHA-256 `3a270e579f080067717d90e25b6e59d29615a543ff30b1abfb9b5e2fae31337d`, 2,019 LF; inspected the game-definition text and the R-minus description. The [R figure](https://arxiv.org/html/1410.8349v2/RGraph.png) was displayed and visually compared; the edge list remains a **visual transcription**, not a machine-readable adjacency table printed by the source. No image-byte hash or all-literature/source-novelty certification is claimed.

The original game gives each player exactly its graph neighbours' values and requires a total decoder. The source defines R-minus by removing edge 9–10 from the depicted R. The two candidate graph descriptions independently parse to the **same** registered undirected ten-vertex adjacency list; the checker confirms symmetry, 26 edges, edge 3–4, and no 9–10 edge. This reconstructs the requested claim **for that registered/visually checked transcription**; it is not a certificate of every pixel or an imported historical result.

For a finite support S, the FD at v is exactly: two S-words agreeing on all v-neighbours agree at v. Therefore the candidate lookup is well-defined on all tuples occurring in S; default zero elsewhere makes each decoder total. The independent checker enumerated the full 1,024 binary inputs and found the 88-word and four-word lookup systems have **exactly 88 and 4 winners**, respectively, matching the listed supports. It also injected a one-vertex disagreement and rejected it specifically as `FD conflict at vertex 1`; a zero weight was rejected for the intended positive-weight violation.

## 2. Weighted law: exact finite arithmetic, not an optimizer estimate

Independently parsed 88 distinct 10-bit words and 88 positive integer weights summing to 6,000. Their weighted one-counts are exactly

    [3530,2474,3526,2475,2474,2468,2469,3529,2476,3523].

The closest count to 3,000 is 3523 at vertex 10, so binary-entropy symmetry/monotonicity makes h=H(X₁₀) the maximum marginal entropy. Let J be joint entropy in **nats**, a=3523, b=2477, N=6000. Direct expansion gives

    N(100J−649h)=649a ln a+649b ln b−549N ln N−100Σ_i w_i ln w_i
                 =ln(L/R),
    L=a^{649a}b^{649b},  R=N^{549N}∏_i w_i^{100w_i}.

I independently verified L>2^4448R by both:

1. **Rigorous fixed-point logarithm bounds:** set G=ln L−ln R−4448 ln2. For z/2^k∈[1,2), expand ln(z/2^k)=2Σ_{j≥0}u^{2j+1}/(2j+1), u=(z−2^k)/(z+2^k), and use the exact rational tail bound 2u^{2m+1}/[(2m+1)(1−u²)]. With m=80 and integer floor/ceiling arithmetic at scale 2^192, the observed lower bound for 2^192G is `882972985692603514930727617498280132211991562712225288028` > 0. The receipt records the upper bound as well.
2. **Independently constructed exact big integers:** grouped identical weights, built L and R from the candidate lists, compared `L >= (R << 4448)`, and obtained PASS. Their bit lengths were **45,064,415** and **45,059,967**; independently computed big-endian SHA-256 values `374d171ebe554c2a5642a6e17db862178beb90184b90a4f4b071ee4cd18208d2` and `d9308256ac9011363dede4f9954aef45170d5b5ba2d5af4181d6a12a25f84957` match the separately pinned author receipt. Both calculations use the local Python integer implementation; no independent hardware/vendor assumption is claimed.

Thus 100J>649h. Uniformly on the same 88 actual winners, independent counting yields one-counts `[48,40,48,40,44,44,40,48,44,48]`; a marginal has probability 1/2, so its ratio is ln88/ln2. The exact integer comparison `2^649 > 88^100` passed, proving that ratio is below 649/100. The reported search's floating approximation is not used.

## 3. Finite common-alphabet construction

For t=100, n=600000 and row multiplicities c_i=100w_i, every c_i is positive and Σc_i=n. The integer M is the multinomial type-class cardinality; each vertex's binary columns have one-count 100a_v. Binomial unimodality and the independently checked marginal counts identify Q=binom(600000,247700) as the largest column alphabet. Inject each column type into [Q]. On **every** neighbour-label tuple, unrank valid neighbour columns, apply the already checked binary decoder rowwise, rank a valid target column, and return a fixed symbol for invalid inputs or wrong output type. Thus the decoder is total on the original neighbourhood, and every type-class row sequence is a winning Q-ary word. The ten labelled columns recover every row sequence, so there are at least M distinct winners.

The entropy bounds are valid for this integer type, not merely asymptotic. Under p_i=c_i/n>0, a type different from c has some count above and another below expectation; moving one count from the former to the latter multiplies its probability by `(k_i/c_i)(c_j/(k_j+1))>1`. Hence the exact type is most probable among at most (n+1)^88 types, yielding M≥exp(nJ)/(n+1)^88. A fixed binary type probability is ≤1, giving Q≤exp(nh). The independently executed exact-integer test verifies `2^444800 > 600001^8800`; together with ln(L/R)>4448 ln2 and n=100·6000 it gives M^100>Q^649. No huge type class, Q-ary domain or proposed word set was enumerated.

## 4. Four-word fixed-support obstruction

For the four listed supports, the independent checker formed words `[3,5,8,16]`, verified every original-neighbour FD and all 1,024 default-zero decoder inputs, and found exactly those four winners. Uniformly, the maximum marginal is ln2 and the joint entropy ln4, ratio 2. With weights `(2,2,1,1)/6`, the one-counts are `[4,2,2,1,1,0,0,0,0,0]`, so the maximum is h(2/3) and the joint entropy is h(2/3)+ln2. Since 3³<2⁵, h(2/3)=ln3−(2/3)ln2<ln2, making the ratio strictly greater than 2. This falsifies only the stated **same-support** uniformization implication; it does not deny type-class approximation on enlarged supports.

Independently computed with exact factorial/binomial arithmetic: M=662585823900, q=735471 and M−q²=121668232059>0 for multiplicities (8,8,4,4). The same full-domain rowwise decoder/injection argument constructs an actual finite q-ary strategy with at least M winners; it does not claim exactly M total winners or improve 20/3.

## 5. Executed evidence and remaining limitations

All reviewer files below are in `information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/`; hashes were taken from actual bytes.

| Reviewer artifact | SHA-256 | LF | Role |
|---|---|---:|---|
| `frontier-20261028-review-f6-check.py` | `5655ed6f99fb41ed35787b27a48641dbff81824dfb767f88058038d6c8d759c4` | 283 | Independent graph, FD, full decoders, rational-log interval and exact small/type tests |
| `frontier-20261028-review-f6-check-result.json` | `18ba4a377e9ba6f4e42c2b238e71504f7d5254ae6322f2e920565e613249905e` | 155 | Executed receipt and intended-reason FD/weight controls |
| `frontier-20261028-review-f6-bigint.py` | `bc590e53a6d7028bc7f69c089c0c09b41ec75a36d48de411cb2dd93dada2b3ed` | 54 | Independent grouped exact-power reconstruction |
| `frontier-20261028-review-f6-bigint-result.json` | `7444f1ca964c16c05193f2ae50b42a6f8bae9e9a140f50765d038f235eb53619` | 9 | Executed bit lengths, hashes and exact comparison |

Both were executed with `/opt/homebrew/bin/python3 -B` and the pinned candidate paths. The first parser attempt failed on the candidate's two-column graph layout (`invalid literal ... '2:'`); the parser was corrected to recognize all ten numbered row delimiters, and the successful run is the evidence above. The exact bigint run completed in 43.22 s. The author's `frontier-20261028-weighted-fd-certificate-result.json`, SHA-256 `5efe17b8065bba5d1203beebc3b0e5fffbaf707e8bcef8f97b61f7a141a8b047`, 89 LF, was used **only after** independent construction for comparison of its recorded bit lengths and byte hashes, not as independent evidence or code.

Reviewer's prior unrelated info-6 work and historical process findings remain disclosed; no blind or method-noninfluence certification is claimed. No historical quarantined mathematical claim was used as a premise. The public graph's exact image-to-list correspondence remains a visually checked transcription, and no complete independent figure-decoding or current SOTA/novelty survey was performed. No author-facing correction was made; M1 is a wording-only recommendation for Main's disposition. **END.**
