# S3 low-defect core written review package v1: P1/P2/P3, not universal LS

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T08:42:52-0700. Status: CANDIDATE_UNVERIFIED.
Directory: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/.
No review launched by this worker; no scientific computation. Scope is the existing BASE2 LS slice, not a new problem slot.

## 1. Exact candidate, scope and status reconciliation
Whole candidate: proof-S3-lowdefect-core-v1.md, SHA256 3847ade3f32e9d9edd11a7cbbd246b68b1a63c8e16beda796250d7c9d64c662a, lines1-85.
Frozen scope: S3-core-scope-v1.md, SHA256 08b1c8622b5da66872868402b08fb3b78d6993002463fc84620970c43202962a, lines1-23.
The candidate's historical 'candidate L1', 'conditional on L1' and 'BASE2 ... NOT an accepted import' labels predate the new parent
verdict. Read them now alongside run review/olson-BASE2-cells-parent-verdict-v1.md,
SHA256 9df92bdafcb73cff034695ece0c5234fd3cb1bb29821ab30182b30b88fdab553, lines7-14: L1 and B2-1 are accepted ONLY for threshold BASE2
counterexamples with CF data w.r.t. dominant g0, and the isolated Sublemma(a) has explicit elementary hypotheses. This discharges
L1 where the S3 candidate meets that setting. It does NOT accept P1/P2/P3: those are the new claims being reviewed. No assumption
of LS(17,12), LS(23,16), full BASE2 LS, LS+, STAB or the three-occurrence transversal enters this proof.
The accepted BASE2 source is proof-LS-BASE2-cells-v2.md fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306 (lines19-61 supplied for comparison), through
erratum-1-BASE2-consolidated-v1.md 05749bc842c94cc628d05383d301551d62255adede75c5f1876295180afd780b (whole file supplied). The new standalone packing
statement P1 is re-proved, not imported from the restricted B2-1 verdict.

## 2. Claims and comparison with the accepted BASE2 result
Common setting: p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h=2m-2. A threshold counterexample Y is odd of length14m, has (ZP_4m) and a
zero-sum of length>=2p+2. Accepted RED/DGM-p/LS-II' put it in case(I), with generator g0, d:=delta0=2p-v_g0(Y),1<=d<=2m-3 and
U of size2m+2+d; (F*): rho(W)<=h implies |W|+2rho(W)<=d-1. Z0 is inclusion-maximal mod-p zero-sum, |Z0|<=d-1,
U'=U-Z0 zero-sum-free, delta':=d-|Z0|>=1, |U'|=2m+2+delta', and (F') with delta'.

P1 statement (VERBATIM from candidate26-27; p,m,h fixed by the common setting):
```text
Let S be a sequence over the nonzero residues of Z_p with n:=|S|>=2m+3, and suppose every nonempty occurrence sub-multiset sum
avoids [0,h].  Then no W<=S with sum=-1(mod p) has |W|>=3.
```
P2 statement (candidate heading):
```text
## 2. P2: exclusion of d=delta0=2 (conditional on L1)
```
This means no threshold BASE2 LS counterexample in the common CF setting has d=2. The L1 dependence is now on the newly accepted
restricted L1, not on an unreviewed theorem.
P3 statement (candidate heading and conclusion):
```text
## 3. P3: exclusion of delta'=1 (nonempty Z0 argument is independent of L1)
No nonempty Z0 can occur with delta'=1.  Together with the empty case, delta'=1 is impossible at every BASE2 threshold,
conditional on L1 only for the empty-Z0 case.
```
The final line retains the historical status language of the frozen text; its logical use of L1 is now discharged at the exact
threshold setting by the parent verdict. The proof itself remains unreviewed.

| Claim | Accepted BASE2 scope | New assertion to check | Exact delta if correct |
|---|---|---|---|
| L1 | Shortest-long length2p+2; W* residue-1 and size>=d+2, threshold CF data g0 only | No stronger L1 assertion is made | New candidate may use this accepted interface only in common setting |
| B2-1 versus P1 | B2-1 excludes d=1 in that threshold setting; its internal packing proof has |U|=2m+3 | P1 is standalone and replaces equality with |S|>=2m+3; proof expanded at25-49 | Supplies packing for d=2 with |U|=2m+4; not justified just by changing a theorem label |
| P2 | d=2 excluded by I-small only at m<=4 | Exclude d=2 uniformly, using F* and new P1 plus accepted L1 | Removes d=2 at all BASE2 cells |
| P3 | p23,delta'=1 used a special ten-residue count; B2-1 handles d=1,Z0 empty | Exclude delta'=1 uniformly, including nonempty Z0 with arbitrary d<=2m-3 | Replaces p23-specific count by one interval/cardinality/first-crossing argument |

If all three pass, the potential threshold-counterexample residual is ONLY
  3<=d<=2m-3 and 2<=delta'=d-|Z0|<=d,
with Z0 either empty or of size>=2. This is a necessary residual configuration, NOT an existence theorem and NOT proof that
universal LS holds. In particular at p=29,m=5,delta'=2 lies below the index-one threshold delta'>=m-2=3 and remains untreated.
The candidate's final 'next lever' paragraph at82-85 is planning context, not a fourth theorem.

## 3. Imports (paths, hashes, ranges and acceptance authorities)
Paths below are absolute when given in the JSON; here `OWN/` is exactly
/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/,
`EVID/` is /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/,
and `RUN/` is /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/.

| Interface | Path and whole-file SHA256 | Exact ranges | Acceptance authority / use |
|---|---|---|---|
| BASE2 L1/B2-1, explicit sublemma | RUN/olson-BASE2-cells-parent-verdict-v1.md; 9df92bdafcb73cff034695ece0c5234fd3cb1bb29821ab30182b30b88fdab553 | 7-14,19-25 | L1 used in P2 and empty-Z0 part of P3 only; B2-1 is comparison, not standalone P1 authority |
| Accepted BASE2 source | OWN/proof-LS-BASE2-cells-v2.md; fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306 | 19-61 | L1 lines29-32 and original equality-length packing lines34-61; source read through BASE2 overlay |
| BASE2 governing overlay | OWN/erratum-1-BASE2-consolidated-v1.md; 05749bc842c94cc628d05383d301551d62255adede75c5f1876295180afd780b | whole1-125 | G1: d>=1 from CF(a); B-1/B-2 wrap checks, B-3 restricted scope; Sublemma(a) isolated |
| CF/DGM-p/threshold dichotomy authority | RUN/olson-CFXT-ROW-LSII-parent-verdict-v1.md; ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 | 5,16-25 | CF(a) item1; DGM-p item5; threshold dichotomy item6 |
| LS-II' authority | RUN/olson-STAB-delta-parent-verdict-v1.md; ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 | 7-16 | Item1 excludes case(II), WITHOUT lower-kappa induction H' |
| CF(a)/definitions | OWN/proof-CF-XT-v1.md; aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f | 8-37, especially16-20 | Candidate setting10-17; mu are nonzero; M<=2p-1 gives d>=1. L1's coefficient identity is direct |
| CF E1; ROW E3/E4 | OWN/erratum-1-CF-XT-ROW-range.md; 767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7 | 1-30 | CF integer0<=kappa<=p-1, rho-conditioned ROW repair, threshold scope |
| Longness R4; threshold informational R13 | OWN/erratum-2-prereq-consolidated.md; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | 32-35,92-94 | R4 maintained as boundary, not a direct new CF(b) use; F* derives from CF(a); no SH/AP/TR used |
| DGM-p and threshold cases | OWN/proof-ROW-v1.md; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d | 29-37,60-66 | g0 generator; case(I) d<=e-2; candidate0 is same setting as newly accepted BASE2 |
| LS-II' statement/effect | OWN/proof-LS-caseII-v2-addendum-1.md; c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718 | 6-8,24-26 | Accepted import, not a request to replay its omitted proof |
| LS-II' corrected wording | OWN/erratum-2-delta-consolidated.md; 16cc18235f4353605ebd55753de4304bcf80e5b2c18b42f6fa0c68117795cc27 | 14-36 | D-1: threshold Y, g=g0, no H' needed; declared imports still apply |
| RED authority | RUN/olson-KPS-SLZ-parent-verdict-v1.md; 23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612 | 7-18,especially11,16 | Threshold setup only; no new full-LS conclusion to infer from P1-P3 |
| RED definitions/statement | EVID/proof-SLZ-EXT-v2.md; 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751 | 10-15,28-31 | 0<=kappa<=p-2; present kappa4m satisfies literal range |
| RED mandatory overlay | EVID/proof-SLZ-EXT-v2-erratum-1.md; 907b3d06dd2ac93686ea4f49cf812dfd41f80f9abdefa6fd2d4398821c234daa | 14-25 | No nonhereditary-failure assumption in threshold reduction |
| SLZ3 | RUN/olson-SLZ3-parent-verdict-v1.md; 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24 | whole1-17 | Recalled only for the already accepted L1 parity derivation: bound on shortest T, not on Y |

No index-one theorem, arithmetic-progression lemma, greedy integer lemma, inaccessible shorter-long inverse theorem, or
additional Zeng-Yuan/Savchev-Chen statement is used in P1-P3. The inherited numerical thresholds r and h are essential.

## 4. New proof map and reviewer focus
P1 (candidate25-49):
- Check the change from n=2m+3 to n>=2m+3 is not merely cited from accepted B2-1. In the prefix/symmetry stage |A|>=n+1>=2m+4
  suffices; it gives B>=n>=2m+3, B<=4m. All remaining pair/triple/extension arguments require only n>=9 and that a term exists
  outside the surviving triple. They do not use exact equality n=2m+3.
- Check all subset comparisons are occurrence-level; V and its complement in the sum-1 submultiset are both nonempty when used.
  Integer sums are compared to p and2p; no rectification assumption is allowed.
- B<=3m-1 gives empty J; at3m<=B<=4m-1 a lifted pair gives the triple lower bound18m-1-2B; at B=4m explicitly check residue0 and
  second-wrap residues1/2 are outside J. This is the same accepted argument but must be checked at the standalone scope.
- The only surviving triples are (2m)^3 and (4m-1,4m,4m); check they cannot coexist with the rest of Q, including five available
  copies of2m in the first case. This is a written uniform argument, not a finite search.
P2 (candidate51-54):
- For d=2, a zero-sum of nonzero mu-terms has size>=2, and positive rho has |W|+2rho>=3. Hence F* excludes all nonempty residues0..h.
- |U|=2m+4 meets new P1, whereas accepted B2-1's |U|=2m+3 would not. Accepted L1 gives a sum-1 submultiset of size>=4, contradicting P1.
P3 (candidate56-75):
- Empty Z0: d=1 and accepted B2-1/L1, or P1+L1, give the contradiction only at threshold CF data g0.
- Nonempty Z0 with delta'=1: k=d-1>=2; do NOT assume the existence of an arbitrary disjoint inverse pair. For EACH occurrence z,
  the actual occurrence complement Z0-{z} has size d-2 and residue-z. It is disjoint from W'<=U'. Thus a resulting rho in1..h
  would give |W|+2rho>=(d-2)+2=d, against F*. Every subset-sum value in A' has a representing W', so A' avoids z+[1,h].
- Exact three-region split for z in[1,p-1]: z>=p-h makes the interval contain0 (forbidden because0 in A'); h+1<=z<=p-h-1 makes
  the h-interval nonwrapping and contained in T=[h+1,p-1] of size4m, forcing |A'|<=2m+3<2m+4. Both endpoints must be checked.
- Thus z<=h and singleton F* forces1+2z<=d-1. All actual Z0 terms are positive representatives<=floor((d-2)/2). The last weighted
  prefix w_k=k+2S_k>=3(d-1)>=d crosses d. For the FIRST crossing j>=2, previous w<=d-1 and singleton bound force
  1<=S_j<=(2d-j-2)/2<=d-2<=h-3<h, so rho=S_j with no wrap, yet w_j>=d: contradiction. Check d=3 (singleton interval empty)
  and other small boundaries explicitly.
- P3 is not an application of the p23-specific table; no upper bound d<=5 is used. Its nonempty-Z0 proof uses only F*, F',
  the zero-sum-free core's cardinality and complement symmetry.

Requested review output: verdict for P1/P2/P3 separately, FATAL/MAJOR/MINOR with exact location/minimal fix, accepted imports at
literal scope, and a check of the residual d>=3,delta'>=2. No universal LS, BASE2, LS+ or STAB verdict may be inferred from these
three necessary configuration exclusions. Candidate82-85 is only a proposal for the next lever, not an asserted theorem.

## 5. Excerpt JSON and byte binding
review-excerpts-S3-v1.json contains21 entries selecting17 source files, with whole-file SHA256 and one-based inclusive start/end.
The raw selected source bytes total57,474 (metadata measurement only), plus this package and the JSON: under120KB even with prompt
headers. Embed selected lines verbatim from the files, not a rendered reader preview. The source candidate and earlier scope
are unchanged; the historical L1 status is reconciled by the exact authority comparison above, not by silently broadening it.
