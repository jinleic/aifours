# BASE2 written review package v1: LS(17,12), LS(23,16), L1 and B2-1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T07:57:42-0700.  Status: CANDIDATE_UNVERIFIED, written mathematics only.
Requested by Main after receiving proof-LS-BASE2-cells-v2.md.  No model review is launched by this worker.  This package does not
change that proof.  Both claimed LS cells lie outside the accepted LS-lin band: (17,12) has e=5 and 6e-10=20>17; (23,16) has e=7 and
6e-10=32>23.  They are not BASE1 cells (both primes are 2 mod 3).  If correct they are new LS cells relative to the recorded
acceptance ledger, not a literature-wide novelty or priority claim.  No LS+, STAB, INV* or ordered-Olson claim.

## 1. Frozen candidate and statements copied verbatim
Candidate: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-BASE2-cells-v2.md`,
SHA256 `fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306`, lines 1-118 (whole file).  v1 is superseded and not a governing text.
Scope: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/BASE2-scope-v1.md`,
SHA256 `59eae7d2187f91c1f49a557b43ed849fe35981850e9cbaf4b17996b240828839`, lines 1-28 (whole file).

The full LS statements below are copied VERBATIM from scope lines 9-10; their proof headings are candidate lines 63 and 81:
```text
(S1) LS(17, 12): every odd Y over C_34 with no zero-sum of length in [26, 34] and |Y| >= 42 has no zero-sum of length >= 36.
(S2) LS(23, 16): every odd Y over C_46 with no zero-sum of length in [34, 46] and |Y| >= 56 has no zero-sum of length >= 48.
```
```text
## 3. Theorem B2-17: LS(17, 12)
## 4. Theorem B2-23: LS(23, 16)
```
L1 (candidate line 29, VERBATIM; setting is candidate lines 20-28):
```text
Lemma L1 (the shortest long zero-sum has length 2p + 2).  There is W* <= U with sigma(W*) = -1 (mod p) and |W*| >= delta0 + 2.
```
B2-1 (candidate heading line 34, VERBATIM; setting is candidate lines 20-28, specialized to delta0=1):
```text
## 2. Lemma B2-1: at every BASE2 cell, delta0 = 1 is impossible
```
The defining BASE2 line is copied VERBATIM from candidate line 20:
```text
BASE2 cell: p = 6m - 1 prime (m >= 3: p = 17, 23, 29, 41, ...), kappa = (2p + 2)/3 = 4m = floor(2p/3) + 1, e := p - kappa = 2m - 1,
```
Thus L1 and B2-1 are claims about threshold LS counterexamples in case (I), with g=g0 and the CF data in the stated setting;
B2-1 does not assert anything about a sequence outside that setting.  S3 (the full BASE2 family) is expressly NOT proved.

## 2. Authority records (full paths, whole-file SHA256, exact ranges)
All line numbers here and in the JSON are one-based and inclusive.  Hashes bind whole source files, not just the excerpts.

| ID | Acceptance authority / import record | SHA256 | Lines used |
|---|---|---|---|
| V-pre | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-CFXT-ROW-LSII-parent-verdict-v1.md` | `ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0` | 5, 16-25: CF, DGM-p, threshold dichotomy and governing overlays |
| V-delta | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-STAB-delta-parent-verdict-v1.md` | `ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5` | 7-16: new-range hypotheses, LS-II', I-small/AP'; 21, 39-40: accepted LS+2 proof and index-one boundary |
| V-red | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-KPS-SLZ-parent-verdict-v1.md` | `23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612` | 11, 16-18: RED at its literal source/overlay scope |
| V-slz3 | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SLZ3-parent-verdict-v1.md` | `2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24` | 5-7, 15-17: shortest-long bound, parity at first p=2 mod3 cell, not an ambient-Y bound |
| V-index | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-index-one-primary-statement-parent-v1.md` | `e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6` | 5-17, 24: author-statement import, exact length threshold and basis definition, proof not replayed |
| V-chain | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LSplus-chain-parent-verdict-v1.md` | `4005007f4e073386236016b62949cba925cb5cde12ba13c24ce27b2a2c351b55` | 29, 32, 36: accepted general use of LS+2 greedy step, with governing C4 overlay below |

These are IMPORTS at accepted scopes; reviewers need not re-audit the earlier proof bodies.  Source statements and required
overlays are supplied below to prevent accepting an unstated stronger interface.  The author-statement record V-index is the
only external index theorem used; neither its original proof nor any additional inaccessible Zeng-Yuan/Savchev-Chen result is
silently assumed.  Cauchy-Davenport lies transitively in accepted DGM-p/ROW; no new application is hidden in the candidate.

## 3. Import table: each source, scope, overlay, and use in the candidate
| Import | Source path and SHA256 | Literal source ranges / governing overlay | Authority | Candidate use |
|---|---|---|---|---|
| CF notation and CF(a); CF(b) only where I-small uses it | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-CF-XT-v1.md`; `aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f` | 8-37; E1 and R4 below | V-pre line 17 | 21-28 (F*, F'); L1 31-32 uses the coefficient identity directly; I-small is imported at 64-65,84 |
| CF scope E1; ROW rho-condition repair E3; exact threshold scope E4 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-CF-XT-ROW-range.md`; `767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7` | 7-11,17-30 | V-pre line 5 | mandatory on CF/ROW imports; no use of the unscoped length-(3kappa+2) dichotomy |
| CF(b)/longness R4; AP prerequisite R6; threshold-context R13 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-2-prereq-consolidated.md`; `fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5` | 32-35 R4; 39-50 R6; 92-94 R13 | V-pre lines 5,14,17,22,24 | R4 in the I-small import; R6 is internal to accepted LS-II', not a fresh AP use in the new proof |
| DGM-p | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-ROW-v1.md`; `a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d` | 29-37 (definitions at10-14; RS proof16-27 supplied as context) | V-pre line21 | 21-23: g=g0 is a generator at every threshold BASE2 cell |
| LS-threshold dichotomy, case (I) | same `proof-ROW-v1.md`, same SHA | 55-66 through E3/E4 above and V-pre exact scope | V-pre line22 | 23-28: delta0<=e-2, r=p-2e+1+delta0; case (II) then excluded by LS-II' |
| LS-II' (without H') | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-caseII-v2-addendum-1.md`; `c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718` | 6-8,24-26; corrected statement at delta erratum21-26 | V-delta line15 | 23: all threshold candidates are in case(I). Import is unconditional w.r.t. H', not free of declared imports |
| Proposition I-small | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-caseI-smalldelta-v1.md`; `2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1` | 11-29; statement12-13; AP' statement30-31; delta overlay38-49 | V-delta line16 | 64-65: p17,delta0=1,2, 20<=18+2delta0; 84: p23,delta0=2,28=24+4 |
| Corrected AP' (D1), not the old source proof | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-delta-APprime.md`; `e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461` | 7-17 D1; pointer18-21; source statement30-31 above | V-delta lines11,16 | 73: n=3,p17; 88-90: n=5 or4,p23 (checks below) |
| Delta corrections/authority | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-2-delta-consolidated.md`; `16cc18235f4353605ebd55753de4304bcf80e5b2c18b42f6fa0c68117795cc27` | 14-49: authority,D1,LS-II' and I-small corrections;69-80: LS+2 dependency/positive appended coefficient | V-delta line11 | all imported interfaces read through their mandatory corrections |
| Greedy integer subset-sum step | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LSplus-e2-v1.md`; `2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1` | 48-54, specifically51-54 (C), read with C4 below | V-delta line21; V-chain lines29,32,36 | 71,85-86: all x-sums0..S' exist once S'<2|U'|; size bound |W'_s|>=s-E' |
| Explicit general greedy hypotheses (C4) | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-lsplus-chain-consolidated-v3.md`; `f1573d6c8b1ac00afe3ce438ff5ebca64cce1e4c2682aaf3ef01e18831a608c0` | 55-65 | V-chain lines29,32,36 | supplies the previously accepted parameterized application of (C), not an import of RED(B) at an out-of-range p |
| RED threshold equivalence | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-SLZ-EXT-v2.md`; `2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751` | 10-15 definitions;28-31 RED;91-101 proof, with overlay below | V-red lines11,16-18 | set up threshold Y at21 and final conclusions79,109; applies as kappa<=p-2 |
| RED overlay | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-SLZ-EXT-v2-erratum-1.md`; `907b3d06dd2ac93686ea4f49cf812dfd41f80f9abdefa6fd2d4398821c234daa` | 14-25: endpoint kappa0 clause, occurrence shrink/non-hereditary S1 repair | V-red lines16-18 | keeps the threshold equivalence at its literal scope, no deletion argument assumes failure of S1 is hereditary |
| SLZ3 (accepted statement; no proof replay here) | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SLZ3-parent-verdict-v1.md`; `2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24` | 5-7,15-17 | V-slz3 (same file) | 29-32 only: |T|<=3kappa+1=2p+3, evenness gives |T|=2p+2, not |Y| bound |
| Index one (external classical statement) | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-index-one-primary-statement-parent-v1.md`; `e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6` | 5-17,24 | V-index; reaffirmed V-delta40 | 68-71:p17 at length>=10;85-86:p23 at length>=13, minimality checked (below) |

The LS-II' excerpt contains its corrected statement/effect, not a partial replay of its earlier proof; it is an accepted import.
The original AP' proof in I-small is deliberately not excerpted past its statement (line31); D1 governs in its place.  Extra
mentioned imports in accepted proof bodies (such as S1-sharp) are not new uses in BASE2.  Scope's atomic-decomposition sentence
was a proposed fallback only; the candidate does not use it or an inaccessible two-atom theorem.

## 4. Complete location map for non-elementary steps and for the new counts
The line references below point to the frozen candidate (fd6e64e5...), not to proof substitutes.

| Candidate lines | Step / import | Literal hypothesis check supplied / to check |
|---|---|---|
| 20-28 | RED, DGM-p, threshold dichotomy, LS-II', CF(a) | p=6m-1 prime,m>=3; kappa=4m=kappa0+1<=p-2; thr=14m; g=g0; 1<=delta0<=2m-3; r=2m+2+delta0. If rho<=2m-2 then r+2rho<=r+4m-4<=2p. (F') comes from occurrence-disjoint W' and Z0. |
| 29-32 | The ONLY direct use of SLZ3 | shortest T is nonempty, zero-sum, even; ZP forces >=2p+2; SLZ3 upper range contains kappa=kappa0+1<=p-1 and yields <=2p+3. Thus equality 2p+2. All mu/c coefficients refer to g, which is a generator. |
| 34-61 | Lemma B2-1 (new; no index one/AP') | Prefix sums distinct by zero-sum-freeness; complement symmetry A=sigma-A includes empty/full subsets; disjointness/merging of the two forbidden arcs; proper-subset interval J; pair/triple wrap alternatives and extension of the two triples are the load-bearing new argument. |
| 64-65 | Proposition I-small at p17 | delta0=1 or2; 4e=20<=18+2delta0; literal proposition scope satisfied. |
| 68-71 | Index one and greedy at p17 | U' nonempty/zero-sum-free, |U'|=9 or11; appended -sigma(U') nonzero; minimality via complement; length>=10=floor(17/2)+2; appended positive coefficient>=1 makes S'<=16; 2|U'|>=18>S'. |
| 72-74 | AP' at p17 | Four distinct points in arc of size<=7=2*3+1; n=3>=1, 3n+2=11<17; a^(-1)!=0. Exclude 1,2 via s1; -2 via s4=9<=S'. |
| 75-78 | p17 residual delta0=3 | |Z0|=0 or2; a=-1; pair residue nu in1..8 gives a forbidden1..4; empty Z0 plus L1 forces x-sum s*=1 and insufficient occurrences. |
| 82-84 | I-small at p23 | delta0=1 by B2-1; delta0=2 by literal inequality4e=28=24+2*2; delta0=3..5 remains. |
| 85-86 | Index one and greedy at p23, delta'>=2 ONLY | U' is zero-sum-free/nonempty, |U'|=10+delta'>=12; U'(-sigma(U')) minimal by same complement argument as68-70; length>=13=floor(23/2)+2; S'<=22<24<=2|U'|. No index one is used when delta'=1. |
| 87-91 | AP' at p23 | delta'=2,3: six points s1..s6, n=5, arc<=10<=11=2n+1, 3n+2=17<23. delta'=4,5: five points s2..s6, n=4, arc<=8<=9=2n+1, 3n+2=14<23. Distinct points, nonzero difference. Inverse -2 excluded by s6=11<=S'; inverse -1 gives S'<=16. |
| 92-100 | p23, delta'>=2, new signed Z0 count | |Z0|<=3, all signed residues are+1 or-1..-4; q<=1 positives from(F*); signed total in[-12,1] and zero mod23, hence exactly0. L1 gives a signed difference in[-28,1] congruent-1, so only-1 or-24; both excluded by size and balance. |
| 101-108 | p23, delta'=1, new modular counting | |U'|=11,|Z0|=delta0-1 in2..4; complement symmetry gives A' subset {0} union[7,22], |A'|>=12. Single z and the occurrence complement Z0-{z} exclude two arcs. The explicit residue-removal table below must be independently checked. |
| 79,109 | RED conclusions | No threshold candidate survives; invoke the already accepted threshold equivalence to reach every |Y|>=42 or>=56, not merely threshold sequences. |

The p23 delta'=1 count at candidate lines105-108 uses the union of `[2-zeta,6-zeta]` and `[1+zeta,6+zeta]` mod23 intersected
with `[7,22]` (16 residues).  The source's counts, written in increasing zeta order for checking, are:

| zeta | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|
| Removed from [7,22] | 11 | 11 | 11 | 9 | 7 | 6 | 8 | 10 | 11 | 11 |

Each removes at least6, leaving at most10 in the tail, plus the element0, contradicting |A'|>=12.  zeta in2..6 or17..22 is ruled
out because0 is in A'.  Hence every element of nonempty Z0 would have residue1, while |Z0| in{2,3,4}: not a zero-sum mod23.
This is a short written count inside the proof, not an unrecorded finite search or computational premise.

## 5. Reviewer focus and requested verdict format
Please treat the candidate as untrusted and use accepted imports only at their literal scopes.  Independently verify:
1. L1: full CF generator/coefficient identity, occurrence counts, parity, and that SLZ3 bounds the shortest T only.
2. B2-1(a): cardinal |A|>=|U|+1 from distinct prefix sums, complement symmetry with empty/full subsets, exact arc endpoints and
   the disjoint versus merged cases.  In particular, check that the endpoints lead to B in[2m+3,4m] without an implicit rectification.
3. B2-1(c)-(f): proper-subset quantifiers, pair/triple sums including both possible wraps, t>=4 exclusion, exactly the two triples
   at B=4m, and all further elements forced/excluded.  Check five occurrences of2m are available when used.
4. The index-one calls (n=p, not2p) and all three AP' calls, including the delta'=4,5 shift from s1..s6 to s2..s6.  Do not invoke
   the index-one theorem at p23,delta'=1, where its length hypothesis is not met.
5. p23,delta'>=2: the signed total of Z0 versus the CF nonnegative integer sum, the q<=1 positive bound, and the two possible
   lifts -1/-24 in L1.  Congruence is not equality unless the signed range forces the lift.
6. p23,delta'=1: both forbidden arcs are derived using occurrence-disjoint W' and Z0, the inequalities use delta0<=5, and the
   residue count above is correct.  It is a different argument from applying index one at a short length.
7. Completeness of delta0 cases at both cells; exact general scope of B2-1; Section5's S3 residual is planning context, not a
   classification theorem about the whole remaining family.  No claim for LS+, STAB or an actual dihedral avoider.

Return a verdict for each of (S1), (S2), L1 and B2-1 with FATAL/MAJOR/MINOR counts, exact location and minimal repair of any issue,
and the exact import scope used.  A verdict for a restricted lemma must not be promoted to full LS or a word-level conclusion.

## 6. Verbatim excerpt manifest and size
`review-excerpts-BASE2-v1.json` is a list of `{path, sha256, start, end}` entries: whole-file SHA256, one-based INCLUSIVE line ranges.
It includes the whole candidate and the frozen scope (not v1), the authority records above, every used source statement and the
mandatory overlays; it supplies accepted imports, not a request to replay their earlier proofs.  26 excerpt entries from20 source
files select65,315 raw UTF-8 bytes (measured from the pinned file bytes; prompt headers/package text extra).  This package plus the
excerpts and JSON metadata is comfortably below120KB.  Embed the raw selected lines verbatim, not the read-tool rendering (which
may add context lines or ellipses).  Mathematical derivation remains written only; the byte/hash measurement is packaging metadata.
