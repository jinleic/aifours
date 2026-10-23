# Review package: standalone LS candidate on the full NEW kappa interval, v1

Owner OlsonSTABSuccessor. Frozen after /bin/date 2026-10-19T09:27:16-0700. CANDIDATE_UNVERIFIED, CONDITIONAL on a declared
statement-level external theorem. No computation or model launch. Parent owns reviews/verdicts. No pending narrower proof is a premise.

## 1. Review exactly this candidate

WHOLE proof: proof-general-LS-Lev-v1.md, SHA256
bc4f4c7035353bf904a202bd41811684a76cb5e9401905a2860e20222fec06dc, lines1-206 (16,255 bytes).
Frozen scope: GENERAL-LS-Lev-scope-v1.md5daf9b391dba6c78e75928e1688839978d0fd479a68f86ea0595679f2ea5947e.
Statement, copied from the proof:

CONDITIONAL THEOREM G-LS. Let p>=7 be prime and kappa an integer satisfying
 floor(2p/3)+1<=kappa<=p-2.
For every sequence Y of odd elements of C_(2p), if |Y|>=p+2kappa+1 and Y has no zero-sum occurrence subsequence of length in
[2kappa+2,2p], then every zero-sum occurrence subsequence of Y has length<=2kappa.
This is LS(p,kappa) on the displayed interval, relative to the declared imports. It is not LS+, STAB, INV* or ordered Olson.

The new proof separately re-proves the general few-sums application, pinning, Z0 localization, both first-crossing bounds and
signed-lift contradiction. It proves a NEW shortest-long witness with variable j, not BASE2's j=1 lemma. The parent suggestion
b11e3908... is NOT evidence or a premise. Pending BASE2/NORM/PIN/P1-P3 proof bodies are not imported, upgraded or evaluated by analogy.

## 2. Original definition and endpoint accounting -- do NOT label this unrestricted LS

ORIGINAL definition: evidence/LS-scope-v1.md80ae8041118d68f4c1417a67a2891ceaceeba181a375b29dfd73820957cfddfa, lines9-15.
Verbatim lines10-12:
LS(p, kappa): p >= 5 prime, 0 <= kappa <= p - 2 integer; every sequence Y of odd elements of C_(2p) with |Y| >= p + 2kappa + 1
satisfying (ZP_kappa) (no zero-sum of length in [2kappa + 2, 2p]) satisfies (S1_kappa) (no zero-sum of length > 2kappa,
equivalently none of length >= 2p + 2).

The same scope's lines13-15 distinguish the new interval floor(2p/3)+1<=kappa<=p-2 from the S1-sharp interval. Put
kappa0:=floor(2p/3), exactly as in proof-LS-caseII-v2.md line13 and delta verdict line9. Coverage accounting, NOT a new assembly claim:

| Parameter block | Status relative to G-LS |
| --- | --- |
| p>=7, kappa0+1<=kappa<=p-2 | Exact proposed G-LS domain. p>3e with e=p-kappa>=2. New candidate, not accepted. |
| p>=5,0<=kappa<=kappa0 (intersect original kappa<=p-2) | OUTSIDE G-LS. Already accepted by length-free S1-sharp, verdictbd4a0a60... lines5-9; no G-LS premise needed. This includes the boundary kappa=kappa0 and all original-domain cells p=5 (0<=kappa<=3). |
| p>=7,kappa=p-2 (e=2) | Inside G-LS but ALREADY accepted LS-small, delta verdictac8ead13... item2. New proof disposes it by empty case-(I) d-range before using Lev. LS+2 here is separate accepted context, not imported. |
| Existing e=3/e=4, LS-lin, BASE1 and two accepted BASE2 cells | Overlap the new candidate's domain but are NOT proof premises or induction bases. This packet does not re-review their proof bodies. |
| kappa=p-1 or larger | OUTSIDE both original LS definition and G-LS. No extension is asserted; accepted endpoint bounds/classification statements elsewhere retain their own scopes. |
| p=2 or3 | OUTSIDE the original p>=5 definition and G-LS. |

No combined all-domain LS corollary or word-level transfer is proposed in this packet. Parent may later evaluate such an assembly
separately; it must not be inferred as an extra reviewed theorem here.

## 3. Governing source manifest and trust classes

Use ONLY review-excerpts-general-LS-Lev-v2.json for embedding: it is a list of {path,sha256,start,end} with WHOLE-file SHA256 and
inclusive line ranges. v2 adds the original LS definition and low-range acceptance context requested by the parent. v1 was a frozen
intermediate manifest before that request; preserve it as history, do not use it as the governing prompt list.
Selected text:26 ranges from22 files,68,914 raw bytes before package/manifest. No rendered ellipses should replace source text.
All source paths are absolute in the manifest. Abbreviations below:
 OWN=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/
 EVID=/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/
 RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/

Full source hashes and ranges are in the manifest and proof Section0; this import table pins what each accepted interface is used for.
The old sources' historical CANDIDATE headers are superseded ONLY by their specifically cited parent verdict plus mandatory overlays.
Model reviews alone are not acceptance authorities.

| Interface | Exact source/ranges in governing manifest | Acceptance authority and full domain used |
| --- | --- | --- |
| Original LS definition (context) | EVID/LS-scope-v1.md9-15,80ae8041... | Original definition p>=5,0<=kappa<=p-2; NOT proof of LS. |
| Low-kappa S1-sharp (context only) | RUN/olson-s1sharp-parent-verdict-v1.md5-19,bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41 | p>=5,0<=kappa<=kappa0. No use in new general core, no word-level conclusion imported. |
| RED | EVID/proof-SLZ-EXT-v2.md12-31,91-101; erratum9-25 | RUN/olson-KPS-SLZ-parent-verdict-v1.md7-18,23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612 item4. Original0<=kappa<=p-2; our kappa>=5. |
| CF(a), nonzero mu coordinates | OWN/proof-CF-XT-v1.md8-33 + erratum-1 E1 (7-11) | RUN/olson-CFXT-ROW-LSII-parent-verdict-v1.md1-28,ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 item1. Original integer0<=kappa<=p-1, p>=5, any odd generator. |
| DGM-p | OWN/proof-ROW-v1.md10-37 + erratum-1 E4 | Same authority item5. Original(p-3)/2<=kappa<=p-1; new kappa interval is contained. Gives unique dominant GENERATOR g0. |
| LS-threshold dichotomy | OWN/proof-ROW-v1.md55-66 + erratum-1 E3/E4 (17-30) | Same authority item6. Original EXACT kappa0+1<=kappa<=p-2; use threshold length and g0, not LS+ dichotomy. |
| LS-II' without H' | OWN/proof-LS-caseII-v2.md12-19,39-59 (Steps1-4), addendum-1.md1-26; delta erratum14-35 | RUN/olson-STAB-delta-parent-verdict-v1.md7-16,ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 item1. Full p>=7,kappa0+1<=kappa<=p-2; neither H' nor SH assumed. |
| AP | OWN/proof-LS-caseII-v2.md30-31; prereq erratum32-50 (R5/R6 included) | ca6e4ca7 item8. N>=1,3N<p, arc<=2N. R6 proof, NOT v2's obsolete proof lines32-37. |
| AP' | OWN/proof-LS-caseI-smalldelta-v1.md30-31; erratum-1-delta-APprime.md1-21; delta erratum38-45 | ac8ead13 item2. N>=1,3N+2<p, arc<=2N+1. Corrected D1, NOT old proof. No separate I-small length hypothesis is imported into this lemma. |
| SLZ3 (shortest-only) | EVID/proof-SLZ3-v1.md10-30 + WHOLE57-line erratum | RUN/olson-SLZ3-parent-verdict-v1.md1-17,2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24. Original p>=5,kappa0+1<=kappa<=p-1; bounds only shortest long |T|, not |Y|. |
| Lev Theorem2 (NEW, unaccepted external import) | OWN/source-Lev-2110.01081v3-statement-v1.md1-34,c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d | Primary https://arxiv.org/html/2110.01081v3#Thmtheorem2, displayed01Jun2022. Statement read; external proof NOT replayed, local normalized record NOT a remote byte hash. |

Parent-accepted interfaces retain their transitive classical/index-one/FB/S1-sharp dependencies at their actual scopes. This review
need not reconstruct those accepted proofs, but MUST check that the new application stays in their original domains. No body of a
new narrower pending candidate is an accepted interface. The new proof is independent of their status.

## 4. New argument map and exact endpoints for hostile review

Review every step below in the WHOLE proof, not merely this map. The proposed theorem is not established by this package's existence.

A. RED/DGM/dichotomy/LS-II' give a threshold Y, g0 of order2p, M=2p-d,1<=d<=e-2, |U|=p-2e+1+d. If e=2 the d-interval is EMPTY,
so no N=0 AP' call or zero-free-core definition is made. For e>=3, |U|+2h=p-1+d<2p establishes F* ONLY when rho<=h.

B. ANY maximal zero-sum Z0 (possibly empty) has k<=d-1; U'=U-Z0 is zero-free, delta'=d-k>=1,n=p-2e+1+delta'. Adjoining the
occurrence-disjoint Z0 gives F'. The inclusive sumset avoids[t,h],t=max(1,floor(delta'/2)); the strict bound is
 |Sigma_inc(U')|<=p-e+t<2n,
with exact positive difference p-3e+2+2delta'-t. The empty sum is counted. Apply Lev only after its hypotheses, using x1=1 to
obtain nonzero multiplier/orderp. All integer coefficients0..S occur: subset coefficients lie in[0,S] with S<p, so residue equality
has a unique integer lift. No unproved independent greedy step or half-order length hypothesis enters.

C. Pinning: I=[S+1,p-1] is forced to contain the h-t+1 progression points rho*b. If empty, contradiction immediately. Otherwise
l<=2e-2-delta'. For delta'>=2: N=h-t>=1,l<=2N,3N<p; corrected AP yields b=+-1, and +1 is excluded by t<n<=S.
For delta'=1: N=e-2>=1,l<=2N+1,3N+2=3e-4<p; corrected AP' yields +-1,+-2. At rho1, +1/+2 lie in[1,S]; at rhoh, -2 lies at
p-2h=n<=S (2h<p), so b=a=-1. At smallest e=3 necessarily d=delta'=1 and N=1, so this branch is legitimate. The rhoh point then
forces S<=p-e. Pinning is in original CF coordinates, never translated.

D. Localization: R=p-S-h satisfies1<=R<=e-delta'<=h. For zeta in[h,S+h], a real core subset of coefficient sum zeta-h makes residueh.
All endpoints h and S+h are forbidden by F*. The remaining Z0 terms are positive1<=zeta<=floor((d-2)/2), or negative -nu with
1<=nu<=R-1. If R=1, NO negatives; if d<=3, NO positives. Actual occurrences from Z0 and U' are disjoint.

E. Positive first crossing: singleton weight1+2zeta<=d-1 forces first j0>=2; previous weight gives2P_(j0-1)<=d-j0, so
1<=P_(j0)<=d-2<=h-3<h. Thus residue equals integer P_(j0), and F* contradicts a crossing>=d. Conclude q+2P<=d-1,P<h.
If positive bounds already force emptiness, there is no prefix to consider. Empty Z0 is allowed throughout.

F. Negative first crossing is at R=p-S-h, NOT p-S. First N_V>=R has R<=N_V<=2R-2. Its corrective core coefficient
 s=p-N_V-h
lies in(0,S], because s>=2S+h-p+2>=p-3e+3+2delta'>0 and s<=S. Its full coefficient interval supplies an ACTUAL subset. Combined
with the negative prefix its signed sum is h-p, hence original CF residueh and forbidden weighted size. Thus total negatives<=R-1.
The R=1/no-negatives case and empty negative part require no crossing argument.

G. NEW witness: choose shortest long T and use ONLY the accepted shortest SLZ3 bound. Its even length is2p+2j, with
1<=j<=floor((p-3e+1)/2). Order(g0)=2p and coefficient identity c=2mu+1 give rho(W*)=-j and |W*|>=d+2j directly. Do not assume j=1,
use BASE2 L1 outside its scope, replace T by Y, or invoke a stronger unaccepted SLZ3 side observation.

H. Write W*=W' union Z*, ell=|Z*|<=d-1. If s is the coefficient sum of W' and zeta_tilde is the signed Z* sum, then
 tau=zeta_tilde-s in[-p+h+1,P] subset(-p,p-1).
From j<=J obtain1<=j<p and p-j>h>P; all other possible lifts are outside the interval. Hence tau=-j. The size bound gives
zeta_tilde>=d+j-ell>=j+1>=2, while zeta_tilde<=P<h. If these bounds are already inconsistent, contradiction is immediate; otherwise
Z* is nonempty and has original least residue zeta_tilde. It violates F* because ell+2zeta_tilde>=d+j+zeta_tilde>d-1.
RED, not a hereditary-failure shortcut, returns the asserted all-length G-LS result.

## 5. Requested verdict boundary

Check mathematical validity of G-LS at EXACT p>=7,kappa0+1..p-2, conditional on the declared external theorem. Report any invalid
import/domain separately from any new algebraic/occurrence-level gap. Identify the source text for any primary-statement mismatch.
In particular inspect strict versus nonstrict few-sums bounds, empty-sum convention, all small-e branches, R=1, occurrence availability,
positive/negative integer representatives versus original nonnegative CF sums, j endpoints and the positive lift p-j.
No new runtime verification, finite-range evidence, novelty, journal/human/Lean clearance, LS+/STAB, original-LS-domain assembly or
ordered-word consequence is part of this review. Lev's external proof is explicitly not replayed. Narrower candidates remain at their
own actual reviewed or unreviewed status until the parent issues separate verdicts.
