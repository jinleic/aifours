# SCW review package: second cut window p = 4kappa-3 (kappa >= 4), lower-half terminal cell excluded, v1

Owner OlsonSecondCutWindow. Frozen after /bin/date 2026-10-20T02:16:22-0700. CANDIDATE_UNVERIFIED written proof. Outcome: the
FULL frozen target is PROVED; there is no failing lemma. (kappa,p) = (4,13) and (5,17) are written out. LABELLED PARTIAL of
ordered Olson. The parent owns both-family reviews and verdicts. No novelty/priority/first/human-review/Lean claim, no other
cell, no full ordered Olson. Owner throttle: single deliverable; the slot parks after the closing checkpoint.

## 1. Frozen texts (DIR = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window)
- DIR/proof-SCW-v1.md, SHA256 6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650, LF lines 1-386 (38,656 bytes).
- DIR/SCW-scope-v1.md, SHA256 99707df43b6a577e479444d80459b123461b55d03c827389ccac445f54e7258d, 95 LF lines (9,625 bytes), frozen
  after /bin/date 2026-10-20T02:00:53-0700 BEFORE written derivation (pre-freeze reading and unwritten preliminary window/route
  checks disclosed there). Authority RUN/control/written-olson-second-cut-window-transition-v1.json, SHA256
  baf55df8a92cbe40e0f469ac8a21a0d541f529abe053c94450afe5b3e959ab40.
- DIR/checkpoints/checkpoint-001.md, SHA256 1da34a2543d35bdde07008b7cb3633430a24d08039d8fd01238afedd57316945 (02:09:06); a closing
  checkpoint-002.md follows this package.
Claim (full existential NF/word antecedent: SOME admissible NF, arbitrary extra-pair placement, genuine empty-run rule; no o_F,
nonempty-run, rotation-pair or reflection-rigidity hypothesis):
- THEOREM SCW: for every integer kappa >= 4 such that p = 4kappa-3 is prime ((4,13), (5,17), (8,29), (10,37), ...), no
  length-(4p-2) word over D_(2p) avoiding an identity 2p-subword in increasing original index order has an admissible NF with
  terminal k = p+1 and kappa_hat = kappa.
Intermediate, at p = 4kappa-3, kappa >= 4 only: Lemma 1 (W_kappa = [2,R-2], W_(kappa+1) = [0,R-4]); Lemma 2 (frame: direct
zero-sum bound, SC0 via Y'z, (S') at (p-1,kappa-1)); Lemma 3 (E <= 2kappa-3+n-, m1 >= 5kappa/2, u1 >= |b|+4); Lemma 4
(density, signed sums); Lemma 5 (2Pi0+nu0-2p >= 2kappa-1+E/2 >= 7); Lemma 6 (small zero-sums); Lemma 7 (realisation:
m = kappa two-signed full; m = kappa+1 full when both signs have >= 3 letters, otherwise at most two values lost at one end);
Lemma 8 (B* <= 2p; common window I* = [Pi0-2, 2p+2-nu0]; m = kappa sub-windows [Pi0, 2p-nu0] and, two-signed,
[Pi0+1, 2p-1-nu0]); Lemmas 9-10 (additivity, complements); Lemma 11 ((F1)-(F6): theta, empty-run fact, connectivity with
G = 2kappa-3, constant, link to kappa-sets, new pair P1 = {0,3,...,3kappa-3}, P2 = {1,4,...,3kappa-2} u {3kappa} giving f0 = 0,
total); Sec. 5 (top kappa of each alternating set of 2kappa-1 runs; exceptional sets; cases (alpha)-(gamma); B* <= R-1 < R).

## 2. Manifest and imports
DIR/review-excerpts-SCW-v1.json, SHA256 5713213bf48179d66883d055aac5d236ecd99786d15dd5c7d05cc716784843a5 (4,624 bytes): JSON list of
{path,sha256,start,end}, absolute paths, whole-file SHA256, inclusive LF ranges; 20 ranges from 19 files (PL pinned twice:
40-50 and 61-106); includes the proof, the scope and the transition; every hash re-checked equal at freeze. Raw excerpt bytes
80,783; LF-numbered about 83,992.
Load-bearing inputs at literal scope: (SR) of PL Sec. 2 (GRX if-direction, NF word form) with the LOWER parent erratum's m(P);
PL IF(a), the gamma-normalisation and the explicit SS bijection (instantiated through the new Lemma 4(a)); the LT argument
(re-derived); SC0 (read through Y'z, written out in Lemma 2(c)); ZSTRUCT and FB in (S') at (k',kappa') = (p-1,kappa-1) for
t >= 1, with the (S1) definition only; K1 verdict. NOT used: S1(a), the Setting fact, FB-E, Theorem P, B0S-CJ''', K3-11, PL
Lemmas D/U/A/C/THETA and PL Secs. 7-9, every USK/K3/FCW lemma, P11R. Context only: USK verdict and errata v1/v2, K3 verdict
and erratum (excerpted). Untrusted context, NOT excerpted (not premises; pinned in proof Sec. 8): FCW proof
c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf and FCW manifest
a3225345e84476d296357d64e6055dbfd95ad79e71521b8431969e733a53e143.

## 3. Transition requirements -> proof location
- Exact family p = 4kappa-3, kappa >= 4, full antecedent: Sec. 0; Sec. 5 ("Which inputs carry the weight").
- Complete proof OR exact first failing lemma: complete proof; no failing lemma, so no partial ranges are needed.
- Re-derived at p = 4kappa-3: windows (Lemma 1), frame (Lemmas 2-3), density (Lemma 4), lift margin (Lemma 5), common-window/
  representative lemma (Lemmas 6-8), additivity (Lemma 9), complements (Lemma 10), theta framework and connectivity
  (Lemma 11), final count (Sec. 5). (kappa,p) = (4,13) and (5,17): Sec. 6.
- Parent's untrusted exposure (window losses vs FCW slack): answered in Sec. 7 (M1)-(M2): the losses occur only for
  m = kappa+1 patterns with at most two letters of one sign (Lemma 7(d),(e)), widen the common window by 2 at each end, and
  fit inside the margins of Lemma 9 (2kappa-1 > 6), Lemma 10 (B* > p+4) and (F1) (4kappa+4 < 2p); the final count is per
  alternating set of 2kappa-1 runs and gives B* <= R-2, +1 per exceptional set.
- Optional general-delta item: Sec. 7 (M3), explicitly NOT CLAIMED (where the argument stops for delta >= 4).
- Interface table and not-claimed list: Sec. 8.

## 4. Hostile-review focus
A. Lemma 1: 2p-2kappa = R-2 and 2p-2kappa-2 = R-4 at p = 4kappa-3.
B. Lemma 2: SC0 via the minimal zero-sum Y'z (length L+1 >= p+2; ord(g) = 2p; W <= 2p-1); (S') hypotheses at (p-1,kappa-1);
   s_j <= 2kappa-3.
C. Lemma 3: (iii) and (iv) arithmetic; [K] u1 >= |b_l|+4 (kappa >= 4 used for a-labels).
D. Lemma 5: type split; margin >= 2kappa-1+E/2 >= 7.
E. Lemma 7: minimal representations; (a) J != all letters; (c) the u1-2 count; (d) J inside Pos(P) via the u1-4 count, then
   q = 2, 1, 0 (the smaller replacement sets of size <= R-4); (e) via P^c.
F. Lemma 8: the realised intervals and parities in cases (A), (B), (C); b-a >= B*-4; B* <= 2p; every sub-window inside I*;
   uniqueness (length 2p+4-B* < 2p, p odd).
G. Lemmas 9-10: Delta in [1, 4p+6-B*] with Delta = 0 (mod 2p); the complement interval of length 4p+8-2B* < 2p.
H. Lemma 11: Q_i and Q_i u {i} at N = 4kappa-2 (2kappa-3 and 2kappa-4 separators); |d| <= 2kappa+2; empty runs give nonzero
   even theta; gap moves (sum 3kappa-3, G = 2kappa-3); (F4) pigeonhole (3kappa-2 runs in kappa gaps); (F5) P1, P2, P1 u P2
   (kappa-3 >= 1 wrap separators, kappa >= 4); (F6) Q0, Q0^c.
I. Sec. 5: CLAIM (i)/(ii) (two-signed; exceptional; nu0 = 0 all positive / all negative); combination: none, one, or both
   exceptional, the latter split into (alpha) impossible (nu0 = 0), (beta) impossible (Lemma 5 vs B* <= 2p), (gamma) empty
   runs give B* <= 4kappa-2.

## 5. Verdict boundary
Judge Theorem SCW and Lemmas 1-11 at p = 4kappa-3, kappa >= 4, under the full antecedent. NOT claimed: any p not of the form
4kappa-3 (p = 4kappa-1 is the separate unaccepted FCW candidate); any general-delta statement; kappa_hat = 0; p = 7; other
middle-range cells; reflection rigidity; INV*; o_F assembly; full ordered Olson; any multiset-only statement outside the
antecedent. Sec. 7 remarks (M1)-(M3) and routes (R1)-(R4) are not claims. No earlier candidate is promoted by this packet.

## 6. Process disclosure
Machine steps, all metadata or file creation: /bin/date for every timestamp; shasum -a 256 for input and output hashes;
wc -l/-c for LF and byte counts; reading files; mkdir for DIR and DIR/checkpoints; exclusive file creation with Python
open(path,'x') writing already-drafted text (scope, checkpoints, proof, manifest, this package); the proof text was drafted
as a Python string, with one wording replacement guarded by a check that it matched exactly once, and one date
placeholder filled in the same way (this package's two size fields too); Python sha256 and byte length over the pinned LF ranges, used only to re-check hashes
and to count excerpt bytes. No scientific computation, enumeration, assertion about mathematical content, solver, test,
Lean, model CLI, nested agent, /tmp, network, commit or push. After the freeze, only already-listed inputs were re-read
(for LF line numbers). Mathematics: all by hand.

## 7. Size
Package 8,466 bytes + manifest 4,624 bytes + LF-numbered excerpts about 83,992 bytes = about 97,082 bytes (<= 100,000).
