# INV reduction: what Theorem DR actually needs, and the exact open lemmas

Lane MathOlson (INV cycle; repr-INV.md frozen 2026-10-17T01:56:00-07:00).  Written
proof [W] for Sec. 1; Sec. 2-3 are precise statements with finite-exact evidence
only.  Not yet hostile-reviewed.

## 1. Theorem DR-Res (strengthening of Theorem DR)

Definitions as in proof-DR.md; lengths and runs cyclic; x normalised to 1.
For an RGR word u of length N with F, R >= 1 let
  H(u) = sum_j floor(l_j/2) (reflection pairs), a_i, b_i the rotation counts.
Call u *inherited* if
  (E) R <= 3p-2;  (P) F + sum_i floor(r_i/2) <= 3p-2;  (V) R + H <= 3p-2;
  (Pairs) H <= p-1;  (D0) a_i, b_i <= p-1 for every rotation run i.
INV_Res(p): every inherited avoider in RGR_{4p-2}(p) has all runs odd and k <= p.

**Theorem DR-Res.**  INV_Res(p) implies that every word in RGR_{4p-1}(p) has an
identity 2p-subword.
Proof.  Let w in RGR_{4p-1}(p) be an avoider.  As in proof-DR.md, F, R >= 1
(else EGZ or sigma_y^{2p}) and F >= 2 (if F = 1 then R = 4p-2 >= 3p-1, EGZ).
w satisfies (E) [EGZ], (P) [Theorem P], (V) [Davenport-alpha, F >= 2], (Pairs)
[p same-letter pairs sigma_y sigma_y taken from constant reflection runs, each pair
adjacent in the selection, give an identity 2p-subword], (D0) [Doubling Lemma,
j = 0: p equal rotations rho_{+-1} in one gap sum to 0].  Each of these
quantities is monotone non-increasing under deleting a letter inside a run, so
every in-run deletion w' of w is an inherited avoider in RGR_{4p-2}(p) with the
same k.  The rest of the proof of Theorem DR (two-long-runs contradiction, the
long run X with |X| = 4p-2k >= 2p, sigma_y^{2p} or Doubling) uses INV only on such
w'.  []

## 2. The two open lemmas (exact statements)

Let w' be an inherited avoider in RGR_{4p-2}(p).
**Lemma PAR(p)** (parity): if k <= p then all 2k runs of w' are odd.
**Lemma RUNS(p)** (run count): k <= p.
INV_Res(p) = PAR(p) + RUNS(p), so PAR(p) + RUNS(p) imply ordered Olson for all RGR
words of length 4p-1 (Theorem DR-Res).  [RUNS is used before PAR: if k > p no
parity statement is needed.]

## 3. Finite-exact evidence and the certificate structure (aids, not proofs)

code/inv_classify.cpp (derived from was_search.cpp; T0 filter removed because it is
not inherited) classifies inherited RGR words of length 4p-2 that VIOLATE parity
by how patterns with Phi <= 2 (empty + single brackets = cyclic intervals) certify
them: zero (0 in W(empty): reflection pairs + rho_1 rho_{-1} pairs), full (a single
bracket window with >= p residues), joint (no single certificate, but no theta
avoids all Phi <= 2 windows: an interval-avoidance system on the reflection values
is infeasible), none (Phi <= 2 does not certify).
p = 5 (complete, k <= 9): k <= 6: none = 0 with Phi <= 2; k = 7, 8: none = 2037,
512 with Phi <= 2 and none = 0 with Phi <= 4.  Joint cases occur already for
k <= p (p = 5: 640 at k = 4, 1984 at k = 5), in all three violation types (even
reflection run only, even rotation run only, both), e.g. even rotation run only:
a = (0,0,0,0,0), b = (1,1,1,2,2), l = (1,1,1,1,7).
Consequences for a proof: PAR cannot be proved by single-window inequalities
alone (joint cases); RUNS needs patterns with more brackets (k > p cases are
uncertified by Phi <= 2 at p = 5).

### 3.1 Results added after host clock 2026-10-17T02:19:08-07:00 (finite-exact aids)

code/inv_classify.cpp (sha256 recorded in Sec. 4), inherited words at N = 4p-2:
* PAR, p = 7 (complete, all inherited parity violators, k <= 13): with Phi <= 2
  patterns (empty + all cyclic intervals) "none" = 0 for every k <= 7 = p; joint
  cases occur (k = 4..7: 7,168 / 112,606 / 627,757 / 1,450,264).  With Phi <= 2,
  "none" first appears at k = 8 > p (3,188).  So PAR(5) and PAR(7) hold and are
  certified by single brackets; PAR(p) is a single-bracket statement at p = 5, 7.
* Elementary brackets only (P = empty, single rotation runs, complements) do NOT
  suffice for PAR at p = 5 (k = 4: 60, k = 5: 710 uncertified): longer intervals
  are needed.
* RUNS, p = 5 (INV_RUNS mode: every inherited word with k > p, any parities):
  Phi <= 2 leaves k = 7, 8, 9 uncertified; Phi <= 4 leaves only k = 9 = 2p-1 (8 run
  data); Phi <= 6 certifies all.  k = 2p-1 at length 4p-2 means EVERY run is a
  single letter: the fully alternating words rho_{e_1} sigma_{y_1} ... rho_{e_{2p-1}}
  sigma_{y_{2p-1}}.  For them (exact, from Lemma GR): C = Phi(P) exactly, all but
  Phi(P) - 1 rotations are selected, and the achievable t form an arithmetic
  progression with difference 4: t = D(z) + 2(Phi - 1) - 4q, D(z) = sum_i e_i z_i,
  q in [max(0, Phi-1-E-), min(Phi-1, E+)]; the condition is t = sum_{i in P} theta_i.
RUNS(5), RUNS(7) hold (INV(5), INV(7) complete, repr-WAS.md Sec. 4).

## 4. Status and next steps (precise)

Proved (written, Sec. 1): Theorem DR-Res.  Open for general p: PAR(p), RUNS(p).
Most promising next lemmas: (a) PAR via the interval-avoidance system on
reflection values (single brackets suffice at p = 5, 7; joint certificates are
forced-difference contradictions: windows of size p-1 force y_a - y_b, and the
forced values are not additive when a run is even); (b) RUNS, starting with the
fully alternating words (k = 2p-1, all runs single letters), where the windows are
explicit step-4 progressions.
