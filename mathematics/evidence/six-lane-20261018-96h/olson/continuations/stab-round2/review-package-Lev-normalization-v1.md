# Standalone dual-review package: Lev 2022 Theorem 2 application and BASE2 multiplier pinning, v1

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T09:05:37-0700. Candidate mathematics only; no model call or scientific
computation. This packet is SEPARATE from the S3lowdefect P1/P2/P3 packet. It neither imports nor re-reviews P1/P2/P3. Its conclusion
is normalization and multiplier pinning, NOT a full LS theorem. The Z0/closure obligation is outside this review packet.

## 1. Frozen texts and the new external trust boundary
Whole candidate: proof-S3-Lev-normalization-v1.md
SHA256 83a67e6a8135b40f84794476b3b8e75abaaf45f2e19f0b42a03a4caf65ae9694, lines1-81.
Checked-primary statement record: source-Lev-2110.01081v3-statement-v1.md
SHA256 c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d, lines1-34.
Frozen application scope: S3-Lev-application-scope-v1.md
SHA256 1450aa85c6dfca9504201b499296b0154b3f9c8539de52fbd8aadd242f03c206, lines1-28. Only NORM/PIN are under review here; its ZCLASS/ASSEMBLY
paragraphs are goals, not imported proof steps.

Lev source: Vsevolod F. Lev, Zero-sum-free sequences with few subsequence sums, arXiv2110.01081v3, displayed date01 Jun2022:
https://arxiv.org/html/2110.01081v3#Thmtheorem2.
The worker read Section1's zero-sum-free and INCLUSIVE Sigma definitions plus the exact Theorem2 statement directly, not from
the scout paraphrase. Source record is a typography-normalized local transcription, not a byte snapshot of remote HTML; its
SHA binds that record only. The external theorem's proof is NOT reproduced, formally verified or replayed. It is NOT yet a
parent-accepted correctness import. Reviewers may take exactly the following public theorem as a declared external black box,
and must verify every application hypothesis. Parent independently owns import admission/source confirmation.

Exact mathematical transcription of Theorem2 (as recorded, NO extra '+1'):
A zero-sum-free sequence alpha=(a_1,...,a_n) over an abelian group with |Sigma_inc(alpha)|<2n can be suitably reordered as
(x_i a), with integers1=x_1<=...<=x_n, x_(j+1)<=x_1+...+x_j. All subsequence sums INCLUDING0 are
{0,a,...,Sa}, S=sum_i x_i, and S<ord(a) if a has finite order. There is NO length>group-order/2 hypothesis.
Do not substitute Theorem1 printed above it (the older half-order theorem, with a different '+1' inequality).

## 2. Exact new statements
Setting: p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h=2m-2. Threshold odd Y with |Y|=14m,(ZP_4m),a long zero-sum. Accepted reductions
give g=g0,1<=d=2p-v_g(Y)<=h-1, U of nonzero CF mu-residues, |U|=2m+2+d,
 (F*) rho(W)<=h => |W|+2rho(W)<=d-1.
Z0<=U ANY inclusion-maximal mod-p zero-sum,k=|Z0|<=d-1; U'=U-Z0 is zero-sum-free,delta'=d-k>=1,
n:=|U'|=2m+2+delta', and
 (F') rho(W')<=h => |W'|+2rho(W')<=delta'-1.
No lower-delta or lower-kappa LS theorem is assumed.

NORM (candidate34-48): t:=max(1,floor(delta'/2)),1<=t<=h. A:=Sigma_inc(U') avoids[t,h], so
 |A|<=p-(h-t+1)=4m+t<4m+4+2delta'=2n.
Conditional on exactly Lev Theorem2, U'=(x_i a),1=x_1<=...<=x_n,x_(j+1)<=sum_(i<=j)x_i,
S:=sum x_i<p, a!=0, ord(a)=p, and all integer coefficient sums0..S occur among occurrence sub-multisets of U'.
The generator conclusion a!=0 follows because x_1=1 and mu_1=a is an actual nonzero U' term; prime order then gives ord(a)=p.

PIN (candidate50-73): in that exact setting a=-1, n<=S<=4m and E:=S-n<=h-delta', with
 mu_u=-x_u(mod p), x_u>=1,
and full coefficient interval0..S. This is a multiplier pinned relative to the original CF mu-residues, not a translation of U'.

These claims address EVERY delta', including the short cores below p/2. They do not by themselves control Z0 or exclude an L1
witness. In particular this review must not certify S3, all BASE2 LS, general LS, LS+, STAB or ordered Olson from NORM/PIN alone.

## 3. Primary applicability checks to audit (strict inequalities and empty-sum convention)
- U' is nonempty (n>=2m+3>=9) and zero-sum-free by maximality of Z0. The ambient group is additive C_p, hence abelian.
- t..h does not contain0. Any representing W' of a residue there is nonempty, so |W'|+2rho>=1+2t>delta'-1. Check separately
  delta'=1,t=1; even delta'=2q,t=q; odd delta'=2q+1>=3,t=q. Thus precisely h-t+1 NONZERO residues are absent from A, while0 is counted.
- Subtracting that many from p=6m-1 gives4m+t, not4m+t-1. The strict inequality4m+t<2n holds using t<=delta' and delta'>=1.
- Lev's finite-order conclusion gives S<ord(a). As x1=1, a is nonzero and has order p; no generator/positive-coefficient sum
  conclusion is silently imported from the old index-one theorem.
- The theorem supplies the FULL inclusive coefficient interval, not merely a small positive coefficient sum. No separate
  greedy theorem or SC2007 length hypothesis is used.

## 4. Every AP/AP' hypothesis (new PIN proof)
Let b=a^(-1) in C_p, nonzero. The progression rho*b (rho=t,...,h) must lie in I=[S+1,p-1] of size
 l=p-1-S<=p-1-n=4m-4-delta'.
A representative s<=S would give an actual coefficient-sum subsequence of residue rho; s=0 is impossible since rho,b!=0.
If I were empty the nonempty progression could not lie in it; otherwise it is a usual arc. Distinctness holds since the number
of consecutive rho values is<p and b!=0.

| Branch | Progression / AP parameter N | Arc bound | Required strict modular inequality | Pinning checks |
|---|---|---|---|---|
| delta'>=2 | t=floor(delta'/2),rho=t..h,N=h-t; N+1 points | delta'>=2t => l<=4m-4-2t=2N | 3N=6m-6-3t<p=6m-1; N>=1 because t<=m-2 and h=2m-2 | Accepted AP gives b=+-1; b=1 puts rho=t at t<=h<n<=S, outside I; hence b=-1 |
| delta'=1 | t=1,rho=1..h,N=h-1=2m-3; N+1 points | l<=4m-5=2N+1 | N>=1;3N+2=6m-7<p | Accepted AP' gives b=+-1,+-2; +1,+2 use rho1; -2 gives rhoh point p-2h=2m+3=n<=S (2h<p); hence b=-1 |

Finally rho=h is included in either branch; b=-1 puts this point at p-h=4m+1>=S+1, so S<=4m. No no-wrap argument outside
the literal accepted AP or AP' range is assumed.

## 5. Import source table (whole-file SHA256, literal excerpts)
All paths in the JSON are absolute. Here OWN=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/,
RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/.

| Import | Path / SHA256 | Exact excerpt / authority |
|---|---|---|
| Lev2 new external statement | OWN/source-Lev-2110.01081v3-statement-v1.md; c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d | whole1-34; direct primary URL above; conditional, not parent-accepted |
| CF(a),DGM-p,dichotomy,AP accepted authority | RUN/olson-CFXT-ROW-LSII-parent-verdict-v1.md; ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 | 5,16-24, items1,5,6,8 |
| LS-II',AP' accepted authority | RUN/olson-STAB-delta-parent-verdict-v1.md; ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 | 7-16 (item1 LS-II', item2 corrected AP') |
| CF definitions and(a) | OWN/proof-CF-XT-v1.md; aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f | 8-33; M<=2p-1,d>=1; mu-values nonzero and(F) |
| CF E1 and threshold/ROW scope corrections | OWN/erratum-1-CF-XT-ROW-range.md; 767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7 | 7-30 |
| AP statement | OWN/proof-LS-caseII-v2.md; 3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43 | 30-31; do NOT use its superseded old proof |
| AP governing proof R6 | OWN/erratum-2-prereq-consolidated.md; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | 39-50 (empty intersection, both overlap terms, inductive lift) |
| AP' statement | OWN/proof-LS-caseI-smalldelta-v1.md; 2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1 | 30-31; no use of I-small theorem |
| AP' governing proof D1 | OWN/erratum-1-delta-APprime.md; e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461 | 7-17 (statement/proof);18-21 pointer |
| Delta overlay authorities | OWN/erratum-2-delta-consolidated.md;16cc18235f4353605ebd55753de4304bcf80e5b2c18b42f6fa0c68117795cc27 | 14-45, especially D-1 threshold,g0 scope and D-2 corrected AP' proof |
| DGM-p / threshold case(I) | OWN/proof-ROW-v1.md; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d | 29-37,60-66, with above accepted overlays |
| LS-II' interface | OWN/proof-LS-caseII-v2-addendum-1.md; c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718 | 6-8,24-26, accepted statement corrected by D-1; no replay requested |
| RED authority (threshold framing only) | RUN/olson-KPS-SLZ-parent-verdict-v1.md;23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612 | 7-18, item4; no new full-LS conclusion in this file |

CF(b)/R4, SLZ3, index-one, general greedy, lowdefect P1/P2/P3, B2-1, and standalone LS(17,12)/LS(23,16) are NOT load-bearing
imports of NORM/PIN. The candidate's setting is the accepted threshold CF setting, not an import of a universal LS claim.

## 6. Reviewer instructions and byte ceiling
Please return separate verdicts for (i) correctness of the local mathematical transcription/application of Lev2 at its declared
external-statement trust level, (ii) NORM including the strict few-sums inequality and ord(a), (iii) PIN at delta'>=2 and delta'=1,
and (iv) exact scope/import boundary. Flag FATAL/MAJOR/MINOR with exact location and minimal fix. In particular check whether
using AP versus AP' at the parity-dependent delta' branches is justified; a weaker multiplier set or an overlooked endpoint
would affect future Z0 arguments. No theorem-body verification of Lev is claimed.
The original primary is public and readable; a model given only an embedded prompt sees the normalized local theorem statement,
not an authenticated remote snapshot. Parent source admission must remain explicit. No statement-level source limitation is
hidden by the local hash.

review-excerpts-Lev-normalization-v1.json has17 ranges from15 local source files, whole-file SHA256 and one-based inclusive
start/end. Raw selected bytes36,496 plus this package/JSON is well under120KB. Embed raw file lines verbatim, not read-tool
renderings. The source/publication metadata checks are not scientific computation. The independent Z0 closure file and S3
lowdefect package are deliberately not embedded or relied upon here.
