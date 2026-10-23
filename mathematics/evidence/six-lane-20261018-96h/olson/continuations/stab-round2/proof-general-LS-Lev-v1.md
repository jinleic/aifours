# General-parameter LS from a few-sums core and a bounded shortest-long witness, v1

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T09:22:40-0700. Status: CANDIDATE_UNVERIFIED, CONDITIONAL on the exact
external Lev2022 Theorem2 statement below. Scope frozen first in GENERAL-LS-Lev-scope-v1.md
5daf9b391dba6c78e75928e1688839978d0fd479a68f86ea0595679f2ea5947e. No computation, model call, novelty or Lean claim.
The parent lead b11e3908... was a suggestion, NOT a premise. No pending BASE2 normalization/closure claim is imported.

## 0. Exact statement, definitions, imports and range checks

CONDITIONAL THEOREM G-LS. Let p>=7 be prime and kappa an integer satisfying
 floor(2p/3)+1<=kappa<=p-2.
For every sequence Y of odd elements of C_(2p), if |Y|>=p+2kappa+1 and Y has no zero-sum occurrence subsequence of length in
[2kappa+2,2p], then every zero-sum occurrence subsequence of Y has length<=2kappa.
This is LS(p,kappa) on the displayed interval, relative to the declared imports. It is not LS+, STAB, INV* or ordered Olson.

Put e:=p-kappa and h:=e-1. Thus e>=2 and 3e<=p-1, equivalently p>3e. Write (ZP_kappa) for the excluded-length condition and
(S1_kappa) for the conclusion. Zero-sums of odd elements have even length, so under (ZP_kappa) a zero-sum failing (S1_kappa)
has length>=2p+2; call it long. All submultisets below are occurrence submultisets, not value sets. An odd generator has order2p.

NEW EXTERNAL IMPORT, NOT PARENT-ACCEPTED: V. F. Lev, Zero-sum-free sequences with few subsequence sums, arXiv2110.01081v3,
01 Jun2022, Section1 Theorem2, https://arxiv.org/html/2110.01081v3#Thmtheorem2. Local normalized statement record
source-Lev-2110.01081v3-statement-v1.md c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d, lines10-28:
a zero-sum-free sequence alpha of length n in an abelian group with |Sigma_inc(alpha)|<2n can be ordered as(x_i a), with
integers1=x_1<=...<=x_n, x_(j+1)<=sum_(i<=j)x_i (NO '+1'), and
 Sigma_inc(alpha)={0,a,...,Sa}, S=sum x_i<ord(a) if a has finite order.
Sigma_inc includes the empty sum0. This theorem has NO half-order length hypothesis. Its statement was read from the primary
version-pinned source; its proof was NOT replayed. The local hash binds the transcription, not remote HTML bytes. Every new
consequence here is conditional on the exact theorem and its application being admitted independently.

ACCEPTED INTERNAL IMPORTS (original scopes were read, not extrapolated from BASE2):
A. RED: proof-SLZ-EXT-v2.md 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751, lines12-31,96-101, through overlay
 proof-SLZ-EXT-v2-erratum-1.md 907b3d06dd2ac93686ea4f49cf812dfd41f80f9abdefa6fd2d4398821c234daa. Authority:
 review/olson-KPS-SLZ-parent-verdict-v1.md 23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612, item4.
 RED applies to0<=kappa<=p-2. Its endpoint qualification for kappa=0 is irrelevant here (kappa>=5); its shrink step is through
 PROP, not an assertion that failure of(S1) is hereditary. It reduces an all-length LS counterexample to exactly p+2kappa+1.
B. CF(a), DGM-p, LS-threshold dichotomy and AP: authority review/olson-CFXT-ROW-LSII-parent-verdict-v1.md
 ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0, items1,5,6,8. Sources:
 proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f, lines8-33;
 proof-ROW-v1.md a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d, lines29-37,55-66;
 proof-LS-caseII-v2.md 3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43, lines30-31 for AP.
 Mandatory overlays: erratum-1-CF-XT-ROW-range.md 767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7,
 E1/E3/E4; erratum-2-prereq-consolidated.md fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5, especially R5/R6.
 CF(a) permits integer0<=kappa<=p-1 and any odd generator. DGM-p permits(p-3)/2<=kappa<=p-1; our lower bound exceeds(p-3)/2.
 The LS-threshold dichotomy has EXACTLY our kappa interval. It uses g=g0 of DGM-p, not an arbitrary large generator.
 AP: an(N+1)-term AP of nonzero difference in an arc of size<=2N, N>=1,3N<p, has difference+-1; corrected R6 governs.
C. LS-II' (WITHOUT H'): proof-LS-caseII-v2-addendum-1.md c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718,
 lines6-8,10-26, with Steps1-4 of proof-LS-caseII-v2.md and mandatory corrected AP(R6). Read through
 erratum-2-delta-consolidated.md 16cc18235f4353605ebd55753de4304bcf80e5b2c18b42f6fa0c68117795cc27, D-1.
 Authority review/olson-STAB-delta-parent-verdict-v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5,
 item1 with its full-range definition on line9. It excludes case(II) at every parameter in THIS theorem; no induction or SH assumed.
D. AP': proof-LS-caseI-smalldelta-v1.md 2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1, lines30-31,
 through erratum-1-delta-APprime.md e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461, D1, and delta erratum D-2.
 Authority ac8ead13... item2. If N>=1,3N+2<p and an(N+1)-term nonzero-difference AP lies in an arc of size<=2N+1, its
 difference is in{1,-1,2,-2}. No I-small length condition is attached to this standalone AP' lemma; only its displayed hypotheses.
E. SLZ3: proof-SLZ3-v1.md 0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c, lines10-18, through
 proof-SLZ3-v1-erratum-1.md 483d9d1b70a895215a68654d329b73d8d8ab5221382fda290a933a937f5dda59. Authority
 review/olson-SLZ3-parent-verdict-v1.md 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24, line5.
 Its range floor(2p/3)+1<=kappa<=p-1 contains ours. It bounds ONLY a shortest long |T| by3kappa+1, never |Y|.
 These accepted results retain their declared transitive classical/index-one imports; those proofs are not replayed here.
No pending normalization, BASE2 closure, P1/P2/P3, LS-lin or separate index-one/greedy theorem is a premise of the new argument.

## 1. Threshold reduction and the e=2 boundary

Suppose the theorem fails. RED supplies a counterexample Y of exactly
 |Y|=p+2kappa+1=3p-2e+1,
with(ZP_kappa) and a long zero-sum. By DGM-p there is a unique dominant generator g=g0 with M:=v_g(Y)>=2kappa+3 and at most
p-2 other occurrences. In CF coordinates let d:=2p-M, remove the M copies of g, and associate to every remaining odd term c g
(c odd in[3,2p-1]) the nonzero residue mu:=(c-1)/2 in[1,p-1]. Let U be this occurrence multiset of mu-values and let rho(W) be
the least residue modp of its NONNEGATIVE INTEGER mu-sum. Since M>=2p would itself violate(ZP_kappa), d>=1.
The threshold dichotomy and LS-II' leave only case(I), hence
 1<=d<=e-2=h-1, r:=|U|=p-2e+1+d.
If e=2 this integer d-range is empty: contradiction, proving the e=2 cells WITHOUT Lev or an AP' call with N=0. For the rest
assume e>=3; thus h>=2. Every W<=U with rho(W)<=h has
 |W|+2rho(W)<=r+2h=p-1+d<2p,
since d<=e-2<p. CF(a) therefore gives
 (F*) rho(W)<=h => |W|+2rho(W)<=d-1.                              (1)
Indeed a value>=d would fall into the forbidden CF interval[d,2p]. The upper bound is used ONLY under rho(W)<=h.

Choose any inclusion-maximal zero-sum occurrence submultiset Z0<=U (possibly empty). Put k:=|Z0|. Applying(1) to Z0 gives
k<=d-1. Maximality makes U':=U-Z0 zero-sum-free, since a nonempty zero-sum in U' could be adjoined to Z0. Set
 delta':=d-k, n:=|U'|=p-2e+1+delta', 1<=delta'<=d<=e-2.
For W'<=U' with rho(W')<=h, apply(1) to the occurrence-disjoint union Z0 union W'. Its residue is still rho(W'), so
 (F') rho(W')<=h => |W'|+2rho(W')<=delta'-1.                       (2)
No lower bound on n relative to p/2 is assumed.

## 2. New general-parameter few-sums application

Let t:=max(1,floor(delta'/2)), an integer with1<=t<=h. Every residue in[t,h] is absent from A:=Sigma_inc(U'). For otherwise its
representing W' is nonempty (the residue is nonzero) and
 |W'|+2rho(W')>=1+2t>delta'-1,
against(2). The strict inequality holds for delta'=1; for delta'=2q>=2 its LHS lower bound is2q+1; for delta'=2q+1>=3 it is2q+1.
Consequently, INCLUDING the empty sum0,
 |A|<=p-(h-t+1)=p-e+t<2(p-2e+1+delta')=2n,                        (3)
because the difference between the last expression and p-e+t is
 p-3e+2+2delta'-t>0
using p>3e and t<=delta'. U' is nonempty (n>e+1>=4) and zero-sum-free. Thus the exact external Lev Theorem2 applies, CONDITIONALLY:
there are a nonzero a in C_p and positive integers x_u with mu_u=x_u a, and
 n<=S:=sum_(u in U') x_u<p, Sigma_inc(U')={0,a,...,Sa}.             (4)
The multiplier is nonzero because x_1=1 makes a an actual nonzero term of U', and ord(a)=p because p is prime. Every integer
s in[0,S] is the x-sum of an ACTUAL occurrence submultiset of U': its residue s a occurs by(4), and any representing subset has
an integer coefficient sum between0 and S<p, uniquely equal to s. This proves the needed coefficient-interval existence without
an extra greedy theorem or arbitrary translation.

## 3. Pin the multiplier relative to the ORIGINAL CF coordinates

Write b:=a^(-1) modp. For each rho in[t,h], its least representative rho*b lies in I:=[S+1,p-1]; a representative in[0,S] would
be realized by(4) and contradict the avoidance in(3). The representative cannot be0 because rho,b are nonzero. This also disposes
S=p-1 immediately (I would be empty). We may therefore assume I is a nonempty arc with
 l:=|I|=p-1-S<=p-1-n=2e-2-delta'.
These are h-t+1 DISTINCT consecutive progression points of nonzero difference b; h<p.

If delta'>=2, put t=floor(delta'/2) and N:=h-t. Since delta'<=e-2, we have e>=4 and t<=floor((e-2)/2), so N>=1. Also delta'>=2t,
 l<=2e-2-delta'<=2(e-1-t)=2N, and 3N<=3(e-1)<p.
Accepted AP with its CORRECTED R6 proof yields b in{1,-1}. b=1 puts the rho=t point at t<=h<n<=S, not in I. Hence a=b=-1.

If delta'=1, put t=1 and N:=h-1=e-2>=1. The h=N+1 progression points lie in I, with
 l<=2e-3=2N+1, and 3N+2=3e-4<p.
Accepted AP' with its CORRECTED D1 proof yields b in{1,-1,2,-2}. b=1 or2 puts the rho=1 point at1 or2<=n<=S, outside I. For b=-2,
the rho=h point has least representative p-2h=p-2e+2=n<=S (2h<p), again outside I. Hence a=b=-1.
At the smallest remaining e=3, d=delta'=1, this is exactly the AP' branch N=1 with3N+2=5<p (p>9); no zero-length AP is used.

Now the rho=h point for b=-1 lies at p-h in I, so S<=p-h-1=p-e. We have proved at GENERAL p,e that
 mu_u=-x_u (modp), x_u>=1, n<=S<=p-e, and every integer s in[0,S] is realizable as an x-sum in U'.  (5)
This is a new conditional proof of the needed interface, not a larger-range invocation of the pending BASE2 candidate.

## 4. Localize Z0 and bound the positive part

Set R:=p-S-h. From(5) and S>=n=p-2e+1+delta',
 1<=R<=e-delta'<=e-1=h.                                         (6)
For a term z of Z0 let zeta in[1,p-1] be its original least CF mu-residue. If
 h<=zeta<=S+h,
take s=zeta-h in[0,S] and an occurrence submultiset W'_s<=U' of coefficient sum s, as(5) allows. Then {z} union W'_s has
mu-sum congruent to h. Its weighted size is>=1+2h>d-1, against(1). If1<=zeta<h, the singleton bound in(1) gives1+2zeta<=d-1.
Thus every Z0 term has one of the two types
 POSITIVE: 1<=zeta<=floor((d-2)/2), signed representative z_tilde=zeta;
 NEGATIVE: zeta>=S+h+1, signed representative z_tilde=-nu_z,
           1<=nu_z=p-zeta<=p-S-h-1=R-1.                         (7)
All endpoints are included as displayed; S+h<=p-1. If R=1, the negative interval is empty, so there are NO negatives. If the
positive interval is empty (in particular d<=3), there are no positives. Write Z+,Z- for these disjoint occurrence parts, q:=|Z+|,
P:=sum_(z in Z+) zeta, and N_total:=sum_(z in Z-) nu_z; an empty sum is0.

Claim q+2P<=d-1. Otherwise list positive occurrences in any order and let j0 be the first prefix with w_(j0):=j0+2P_(j0)>=d.
The singleton bound makes j0>=2, and the previous prefix gives2P_(j0-1)<=d-j0. The added term satisfies2zeta_(j0)<=d-2. Hence
 1<=P_(j0)<=(2d-j0-2)/2<=d-2<=h-3<h<p.
There is no wrap; this actual prefix has rho=P_(j0) and weighted size w_(j0)>=d, contradicting(1). If there are no positives the
claim is immediate. Therefore
 q+2P<=d-1, in particular P<=(d-1)/2<h.                           (8)

## 5. Bound the negative part at R=p-S-h

Claim N_total<=R-1. This is automatic if Z- is empty, including R=1. Otherwise, if N_total>=R, the first prefix V of the negative
occurrences whose magnitude N_V reaches R has
 R<=N_V<=2R-2,
because each summand lies in[1,R-1]. Existence of a negative term implies R>=2. Set
 s:=p-N_V-h.
From N_V>=p-S-h we get s<=S. From its upper bound and S>=n,
 s>=p-(2R-2)-h=2S+h-p+2
   >=2(p-2e+1+delta')+(e-1)-p+2=p-3e+3+2delta'>0.                (9)
Thus s in[0,S], so(5) supplies an actual W'_s<=U'. The occurrence-disjoint W:=V union W'_s has signed mu-sum
 -N_V-s=h-p,
so its ORIGINAL least CF residue is h. Then |W|+2rho(W)>=1+2h>d-1, contradicting(1). This proves
 N_total<=R-1.                                                  (10)
This uses the full coefficient interval in(5), not a bound on the size of W'_s and not an unproved transversal assumption.

## 6. NEW general shortest-long witness (not the BASE2-only L1)

Let T be a shortest long zero-sum of the threshold counterexample Y. Under(ZP_kappa), |T|>=2p+2, and its length is EVEN.
Accepted SLZ3 is applicable at our full kappa range and gives |T|<=3kappa+1=3p-3e+1. Therefore write
 |T|=2p+2j, 1<=j<=J:=floor((p-3e+1)/2).                          (11)
The interval for j is nonempty when T exists; p>3e also directly gives J>=1. This is a bound on |T| ONLY.
Write T=g^i W*, where0<=i<=M and W* consists of its actual non-g occurrences, identified with a submultiset of U. If
sigma_int(W*) is their nonnegative integer mu-sum, then the g-coefficient sum of T is
 i+|W*|+2sigma_int(W*)=2p+2j+2sigma_int(W*).
It is divisible by2p because ord(g)=2p. Hence sigma_int(W*)=-j(modp), and
 |W*|=2p+2j-i>=2p+2j-M=d+2j.                                    (12)
No general claim that j=1 has been made. The shortest-only SLZ3 statement, not the pending BASE2 closure or accepted L1, is used.

## 7. The signed lift and the final CF contradiction

Decompose W*=W' disjoint-union Z*, with W'<=U', Z*<=Z0, ell:=|Z*|<=k<=d-1. Let s be the actual integer coefficient sum of W'
under(5), so |W'|<=s<=S, and let zeta_tilde be the sum of the signed representatives in(7) over Z*. By(8),(10),
 -(R-1)<=zeta_tilde<=P,
so the signed difference tau:=zeta_tilde-s satisfies
 -p+h+1=-(R-1)-S<=tau<=P<h<p-1.                                (13)
Its residue is -j from(12). We have1<=j<p and p-j>h: indeed from(11)
 j<=(p-3e+1)/2<p-h=p-e+1.
The only possible lifts of -j in the open interval(-p,p-1) containing(13) are -j and p-j. The latter is>h>P, so necessarily
 tau=-j, i.e. s=zeta_tilde+j.                                   (14)
Now(12), positivity x_u>=1, and ell<=d-1 yield
 d+2j<=|W*|=|W'|+ell<=s+ell=zeta_tilde+j+ell,
 zeta_tilde>=d+j-ell>=j+1>=2.                                   (15)
But zeta_tilde<=P<h. Thus Z* is nonempty and its ORIGINAL least CF residue equals zeta_tilde in[2,h], since the signed sum is
congruent to the nonnegative integer mu-sum. Rearranging(15) gives
 |Z*|+2rho(Z*)=ell+2zeta_tilde>=d+j+zeta_tilde>d-1,
contradicting(1) for the actual occurrence submultiset Z*<=U. This excludes every threshold counterexample. RED then proves
G-LS for all |Y|>=p+2kappa+1. []

## 8. Exact delta and remaining trust boundaries

This is a standalone general-parameter candidate for ALL floor(2p/3)+1<=kappa<=p-2, p>=7 prime, not only the first p=2mod3 cell
or an e-limited band. If reviewed and accepted, it would discharge the remaining LS cells IN THIS interval, relative to the stated
imports. No full ordered-word, LS+, stability/classification or novelty conclusion follows from this file alone.
The e=2 contradiction uses only accepted inputs. The e>=3 proof is conditional on NEW Lev Theorem2; both the imported primary
statement and its new full-range application require parent review. The previously pending BASE2 normalization/closure are neither
premises nor acceptance authorities here. No proof-body replay of Lev or of accepted transitive index-one/FB/S1-sharp imports,
no native/scientific computation, no tests or Lean, and no human review have been claimed. Classical priority remains unassessed.
