# FCW review package: first cut-window boundary p = 4kappa-1 (kappa >= 3), lower-half terminal cell excluded, v1

Owner OlsonUniformSmallKappa. Frozen after /bin/date 2026-10-20T01:38:10-0700. CANDIDATE_UNVERIFIED written proof. Outcome: the FULL frozen
target is proved, with no obstruction; the case (kappa,p) = (3,11) is covered explicitly. LABELLED PARTIAL of ordered Olson.
The parent owns both-family reviews and verdicts. No scientific computation, enumeration, script, assertion, solver, model
CLI, test/build or Lean; all case work by hand. The only machine steps were metadata (/bin/date, whole-file SHA256, LF line
and byte counts) and text drafting; the drafting helper checked that each wording replacement matched exactly once. No
novelty/priority/first/human-review claim, no other cell, no full ordered Olson. Owner throttle: single deliverable; the
slot parks after it.

## 1. Frozen texts (directory /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-first-cut-window-boundary/)
- proof-FCW-v1.md, SHA256 c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf, lines 1-297 (29,526 bytes).
- FCW-scope-v1.md, SHA256 dd0e5d1c7d85070f18f44815a013bb121706511e5bb2d63dd5f39b3ba92c425e, frozen 2026-10-20T01:19:12-0700 BEFORE derivation
  (pre-freeze exposure disclosed, including the parent's untrusted sketch). Authority
  RUN/control/written-olson-first-cut-window-boundary-transition-v1.json, SHA256
  ba6e8038fda856125303c26a85bfac78741ab04186efa98c18f3ebe9071b02d6.
- checkpoints/checkpoint-001.md, SHA256 126ab8421bd2c0d32e6d627f836266533a84df21952452a91888309acc9b6931 (01:31:12); a closing checkpoint-002.md
  follows this package.
Claim (full existential NF/word antecedent: SOME admissible NF, arbitrary extra-pair placement, genuine empty-run rule; no o_F,
nonempty-run, rotation-pair or reflection-rigidity hypothesis):
- THEOREM FCW: for every integer kappa >= 3 such that p = 4kappa-1 is prime, no length-(4p-2) word over D_(2p) avoiding an
  identity 2p-subword in increasing original index order has an admissible NF with terminal k=p+1 and kappa_hat=kappa.
  In particular the whole (3,11) cell is excluded, including the H11-failing branch of the accepted conditional K3-11.
Intermediate, at p = 4kappa-1 only: Lemma W (windows; no m has [0,R]), IF* (frame; direct zero-sum bound), D* (density),
N (lift margin 2Pi0+nu0-2p >= 2kappa-1), Z (two-signed => nonempty zero-sum), U* (common window for every m in
{kappa,kappa+1}, single-signed patterns included), A*, C*, F (theta, connectivity, f0 = 0, total), Sec. 5 (sorting the
top kappa runs: B* <= R-1).

## 2. Manifest and imports
review-excerpts-FCW-v1.json, SHA256 a3225345e84476d296357d64e6055dbfd95ad79e71521b8431969e733a53e143 (4400 bytes): JSON list {path,sha256,start,end}, whole-file
SHA256, inclusive LF ranges, absolute paths; 19 ranges from 19 files; every hash re-checked equal at freeze; raw 72,864
bytes, LF-numbered about 77,163 bytes. Package + manifest + numbered excerpts stay below 100,000 bytes (Sec. 6).
Load-bearing inputs at literal scope: (SR) of PL Sec. 2 (from the GRX if-direction, NF word form), PL IF(a) and the
gamma-normalisation, the explicit SS bijection instantiated through the new D*, the LT argument (re-derived), SC0, and
ZSTRUCT/FB in (S') at (k',kappa') = (p-1,kappa-1) for t >= 1, with the (S1) definition only; K1 verdict and LOWER parent
erratum. NOT used: S1(a), the Setting fact, FB-E, Theorem P, B0S-CJ''', K3-11, PL Lemmas D/U/A/C/THETA (replaced by new
D*/U*/A*/C*/(F1)), PL Secs. 8-9, USK and K3 lemmas, P11R. Context only: USK verdict and parent errata v1/v2, K3 verdict and
erratum, P11R (unreviewed, read after the freeze).

## 3. Transition requirements -> proof location
- Exact boundary p = 4kappa-1, kappa >= 3, full antecedent: Sec. 0, Sec. 5 (which inputs carry the weight).
- Exclusion OR exact first failing lemma: exclusion proved; no failing lemma.
- (3,11) explicitly covered: Sec. 6 (with (5,19) as a second worked case).
- No transfer of USK full-window/rigidity: Lemma W(d) (no full-window family at p=4kappa-1); every frame bound is re-derived
  at p = 4kappa-1; the new Lemma U* replaces fullness; no tight-case rigidity is used.

## 4. Hostile-review focus
A. Lemma W: W_kappa = [2,R] (2p-2kappa = R exactly) and W_(kappa+1) = [0,R-2].
B. IF*: (S') hypotheses at (p-1,kappa-1); s_j <= 2t-2n-+1; E <= 2kappa-1+n-; a_i <= 3kappa-1; m1 >= (5kappa+2)/2.
C. D* at p = 4kappa-1 (s_j, a_max <= m1+1); Lemma N's type split and its margin 2kappa-1+E/2.
D. Lemma Z: the count m1 >= (5kappa-1+b)/2 for an a-label b; the symmetric sign case.
E. Lemma U* (the new step): the realised sets in each of the five type/m cases (two-signed via a minimal representation and Z0;
   all-positive m=kappa: even [2,B*]; m=kappa+1: even [0,B*-2]; all-negative symmetric); the translation to [a,b]; the
   complete residue system a,...,a+2p-2; B* <= 2p-2; containment in [Pi0,2p-nu0]; uniqueness mod 2p.
F. Lemma A* (Delta in (0,4p) from the outer window and Lemma N) and Lemma C* (unique value in [2Pi0,4p-2nu0]).
G. Lemma F at N = 4kappa: Q_i; |d| <= 2p-B* <= 2kappa and uniqueness; gap moves with G = 2kappa-1; P1, P2 separators
   kappa-1 and kappa-2 (kappa >= 3); the link J u {x} in (F4); Q0 and Q0^c.
H. Sec. 5: the three cases of the CLAIM (in particular theta_e nonzero even for empty runs when nu0 = 0); exception in at
   most one alternating set; final B* <= 2p-1-2kappa = R-1.

## 5. Verdict boundary
Judge Theorem FCW and Lemmas W, IF*, D*, N, Z, U*, A*, C*, F at p = 4kappa-1, kappa >= 3, under the full antecedent. Not
claimed: other p (p <= 4kappa-3 or p not of the form 4kappa-1), kappa_hat = 0, p = 7, reflection rigidity, INV*, o_F
assembly, full ordered Olson. Sec. 7 route remarks (M1)-(M2), failed routes (R1)-(R3) and the boundary remark are not
claims. No earlier candidate is promoted by this packet.

## 6. Size
Package 6,044 bytes + manifest 4400 bytes + LF-numbered excerpts about 77,163 bytes = about 87,607 bytes (<= 100,000).
