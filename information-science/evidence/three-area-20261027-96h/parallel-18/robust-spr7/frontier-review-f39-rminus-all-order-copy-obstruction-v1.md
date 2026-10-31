# f39 — all-order R-minus partial-copy relaxation review

Reviewer **InfoSPR7-2**, author **InfoGuessingRminus-2**. Actual `/bin/date` observation immediately before writing: **Wed Oct 28 17:43:40 PDT 2026**. Full-scope assignment SHA256 `bf185921563babb8a9c3a11e63a03c9c6913bcea9ff36b292841d8c759909b3b`. The predecessor was read in full, SHA `76d83e14a011baaa2de3a17d8f6d8a28474094bf8a8a4bd5829f14bb5c40230b`; the full addendum was read, SHA `13f21942f6f2ddc8af3f0750b03d366b2c5f950364132e91d8bda461ab667679`.

## Verdict and material correction

**FATAL 0 / MAJOR 1 / MINOR 0.** The all-order family proof and the exact **partial-coordinate** optima at `1847/276` are reconstructed, with the source-graph/extraction and same-harness limits stated below. The new known-coordinate monotonicity obstruction changes the addendum's source-extension status materially; it does **not** invalidate its stated partial-core witness or prove the registered original guessing number.

**MAJOR M1 — addendum line 28, now superseded by exact evidence.** It says whether the specified 4,397 coordinates extend to the remaining source Shannon rows is unestablished. The parent subsequently supplied an author finding; I independently checked the frozen point, SHA `97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec`. In the publisher's actual branch with all original variables plus `d'1,e'1,g'2`, put

`S={a,b,c,d,e,g,h}`.

The two **already fixed** coordinates are `H(S)=871/138` and `H(S union {d'1})=0`. Therefore `H(d'1|S)=-871/138`, violating Shannon monotonicity. Every full extension of *these specified coordinates* would retain this negative quantity, so **none satisfies the full branch Shannon cone**. This does not assert that the same original ten-variable projection has no *different* assignment of auxiliary copy coordinates, nor that full-copy constraints plus the F-family cannot improve the bound. The addendum's 66,731 separately evaluable elemental rows can all pass while a non-elemental Shannon consequence using the already specified endpoint coordinates fails. The 280,954 count is a count of individually unevaluable elemental row occurrences, not a guarantee that their joint completion is possible.

A more explicit contradiction uses the other branch variables in order `f,i,j,e'1,g'2`. Let `R=d'1` and begin with conditioning set S. The Shannon chain identity is

`H(R|S) = I(R;f|S)+I(R;i|S f)+I(R;j|S f i)`
`             + I(R;e'1|S f i j)+I(R;g'2|S f i j e'1)`
`             + H(R|S f i j e'1 g'2)`.

These six terms are elemental source-branch inequalities. Direct exact evaluation of the last three fixed-coordinate terms gives `1/6`, `0`, `35/92`; the first three individually use missing coordinates. Since the left side is `-871/138`, **every** assignment of those missing coordinates forces the first three terms to sum to `-631/92`, so at least one is `<= -631/276`. This strengthens the status from “not proved extendible” to **proved nonextendible as specified**; it is not a claim about a differently chosen auxiliary extension. Parent cited author checker `frontier-20261028-extension-known-monotonicity.py` SHA `e73c1c10192d8359258612c4424938db1d5468d4a8b9d4601e09fa220339be0b`; the values and chain here were independently computed without importing it.

## What was reconstructed

### A. The all-order inequality itself

For arbitrary finite random-variable tuples A,B,C,D,Z, write `a=I(A;B|C,Z)`, `Delta=I(A;B|Z)-I(A;B|D,Z)-I(C;D|Z)`, and `d=I(A;C|B,Z)+I(B;C|A,Z)`. The claimed family is `F_n=(n+1)a-n Delta+n(n+1)d/2 >=0` for every integer n>=1. The proof works for overlapping tuples too; the computational claim below is restricted to disjoint blocks of the ten original vertices.

Condition on each value of Z. Given A,B, draw C and `R_1,...,R_(n+1)` i.i.d. with the conditional law of C, with the new copies independent of `(C,D)` given A,B; finite zero-probability conditioning events can be assigned arbitrary kernels. Let S_j and h be as in the candidate. Direct entropy-chain expansion gives `a_(j+1)=a_j-B_j+d_j`; conditional independence gives `B_j=I(R_(j+1);A,B|S_j)>=0`, while `d_j=I(R_(j+1);B|A,S_j)+I(R_(j+1);A|B,S_j)>=0` and `d-d_j=I(R_(j+1);S_j|A)+I(R_(j+1);S_j|B)>=0`. Conditional exchangeability yields `I(S_k;A,B|C)=sum_(j=1)^k B_j`.

I also independently checked the entropy coefficient cancellation in the candidate's E_k formula: before using copy independence, `E_k - [I(A;B|S_k,D)+I(S_k;D|A)+I(S_k;D|B)+I(C;D|S_k)+I(S_k;A,B|C,D)]` equals exactly `-I(S_k;D|A,B)-I(S_k;D|A,B,C)`. Both terms vanish by the construction. The five displayed terms are nonnegative. Telescoping then gives the candidate's sum-of-nonnegative-terms representation for F_n. This is an ordinary finite entropy proof, not a numerical test or novelty claim.

If any original A or B block is empty, the surviving expression is a nonnegative sum of original-variable CMIs; if C is empty it is `I(A;B|Z)+n I(A;B|D,Z)`; if D is empty, Delta=0. These are implied by the original Shannon rows, so excluding empty A–D from the finite scan loses no disjoint-block cases. Z may be empty and was included in the scan.

### B. Exact independent finite checks

The source constraints were regenerated in the reviewer Python Eval kernel from the independent f26 parser and source-copy definitions, **not** by importing either author checker/producer. All point coordinates were converted exactly to signed integers at scale 25,944; duplicate or missing original masks, nonintegral scale, negative stored coordinates, and wrong objective were rejected. Both first and second 2,558-coordinate witnesses and the 4,397-coordinate witness have objective exactly `1847/276`.

For **each of all three points**, my check evaluated all 1,920 published certificate rows at their printed directions, all 11,520 original elemental CMIs, ten original full-conditional entropy rows, ten graph FDs, ten singleton caps and both generators' 2,046 original-subset symmetry equalities. All passed. I independently evaluated the predecessor's two named prior cuts: F_4=`0`, F_3=`1/69`. The author's precise 15,374-row builder was not itself rebuilt or rerun; the just-enumerated direct constraints and those two cuts are the independently checked coverage.

For the *first* point, the exact A,B,C,D,Z masks `(2,512,32,12,401)` give `a=11/276`, `Delta=1/23`, `d=0`, so `F_n=(11-n)/276` and `F_12=-1/276`. This point is a nonentropic relaxation object, not a counterexample to the entropy inequality.

For the *second*, sparse all-order point, I independently regenerated all five source-copy steps: 493 of 2,181 equality forms were evaluable and 15 nonzero. In particular `H(d)-H(d'1)=1`. The three source branches had respectively `11802,12997,14522` evaluable elemental rows with `28,301,384` negative. Thus this frozen sparse point is not a full-source primal; no claim is made about a different copy extension of its original projection.

For the **4,397-coordinate closure point**, I independently regenerated all 2,181 copy equalities: all are evaluable and zero. I separately enumerated all three source branches' elemental rows, retaining duplicate row occurrences across branches:

| Branch | All elemental occurrences | Evaluable | Negative evaluable | Unevaluable |
|---|---:|---:|---:|---:|
| originals + `b'0` | 28,171 | 14,526 | 0 | 13,645 |
| originals + `d'1,e'1,g'2` | 159,757 | 20,148 | 0 | 139,609 |
| originals + `f'3,g'3,h'4` | 159,757 | 32,057 | 0 | 127,700 |
| **Total** | **347,685** | **66,731** | **0** | **280,954** |

A row was counted evaluable only when every entropy coordinate it uses was present, with H(empty)=0; unknown coordinates were not filled with zero. M1 above shows why those facts do not imply extension feasibility.

### C. All disjoint substitutions, all integer orders

For the two all-order points, an independently written vectorized integer scan in the **Python Eval kernel** inspected every one of `6^10=60,466,176` assignments of each original vertex to unused/A/B/C/D/Z, then kept A,B,C,D nonempty and A-mask<B-mask. It checked exactly **13,729,980** substitutions per point, consistent with the candidate's inclusion–exclusion formula and the A/B symmetry. Entropy values and all operations were integer, with no float arithmetic. The maximum original scaled entropy was 173,618; a conservative bound on every intermediate was `1,339,758,130,153,652,472 < 2^63`, so the NumPy signed-int64 calculations cannot overflow under the stated scan.

For each substitution, let `c=a-Delta` and `d` be the scaled integer sums. Since `F_n=a+n c+n(n+1)d/2`, if d=0 the scan requires c>=0 and checks n=1. If d>0 it checks the first integer n>=1 for which `F_(n+1)-F_n=c+(n+1)d>=0`, namely `max(1,ceil(-c/d)-1)`; discrete convexity makes that a global minimizer over all positive integers, including a two-minimizer tie. Each point passed every substitution, with minimum **twice-scaled** slack 0; 1,338,634 substitutions per point had d=0. The largest actual minimizing n was 22. The candidate's 23 is the largest *adjacent candidate* in its different vertex-based implementation; there is no discrepancy. This is an all-n proof via the exact quadratic criterion, not a scan truncated at n=22.

The exact core identity and coefficient directions were independently replayed in f26 using source SHA `b6bd12e460b8cdc142208e11d7fb188126bf280d109e7689a2c0e49f5dfa8f5d`. Thus, relative to the pinned source text and graph, the 1,920 rows give the upper bound 1847/276 on the core, while each checked all-order point attains it in its **specifically named partial-coordinate system**. The stronger point additionally satisfies all 2,181 supplied copy forms and the 66,731 individually evaluable branch inequalities. Consequently adding the specified all-n disjoint-block F-family to that partial system cannot reduce its optimum. M1 prevents extending that conclusion to the full source Shannon/copy LP.

## Reproducibility and assurance

- Exact independent source-check kernel: `frontier-review-f39-source-constraints-kernel-v1.py`, SHA `abf8bc28bc5592f3cfacf091d1218435e507b4bb55b39eae1a9248762bdc71dd`; it uses the previously loaded independent f26 definitions and imports no author code.
- Exact all-order scan kernel: `frontier-review-f39-all-order-kernel-v1.py`, SHA `0bfaf62c332e184fff825847ac3cd2f2287e1d7f6d148eed2a3dd45f83b089e2`. It likewise executes only within the reviewer's Eval kernel; the two point arrays and integer overflow guard are explicit.
- Receipt `frontier-review-f39-replay-v1.json`, SHA `202eac2fca12e2d12d9921ab8db1d16cd9129067b2eaf385c7f5b725ce78defe`, binds observed results. First/sparse/closure point hashes are respectively `55599041a5a2e73e69d0c70718bc9b049cbbd8e00f3983c5aa42ee86226e88e0`, `af431478fdad330f5f79fa416bdcaf1c56a56fb30ed4855fc65b50d1cac50545`, and `97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec`.

The existing f26 review inspected the article graph, copied protocol, source-text extraction and exact 1,920-row upper identity; full PDF glyph-by-glyph verification and documentary archive provenance remain conditional. This f39 work shares those source bytes and the same harness; no independent human, cross-model, formal-kernel or novelty acceptance is claimed. No native scientific subprocess, external model, nested agent, Git action, deletion or publication was used. The true guessing number, any new original bound, and the possibility of a *different* auxiliary source extension remain open.

**END OF REVIEW.**
