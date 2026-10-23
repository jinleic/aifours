# inverse-parity: Lemma PAR(p) for inherited RGR avoiders of length 4p-2

Owner: worker OlsonParity (six-lane run, lane `olson`; deadline 2026-10-18 18:31:43 PDT).
Writes only inside this directory.  Parent integrates.  No git, no deletion.
Host clock read just before freezing Sec. 1-3: 2026-10-17T02:42:31-07:00.

## 0. Target (verbatim from ../proof-INV-reduction.md Sec. 2)

w an inherited avoider in RGR_{4p-2}(p), p prime >= 5, with k <= p rotation runs:
then all 2k maximal cyclic runs of w are odd.  Inherited (../proof-INV-reduction.md
Sec. 1): (E) R <= 3p-2; (P) F + sum_i floor(r_i/2) <= 3p-2; (V) R + H <= 3p-2 with
H = sum_j floor(l_j/2); (Pairs) H <= p-1; (D0) a_i, b_i <= p-1.

## 1. Frozen representation (exact; derived only from Lemma GR / Lemma WAS)

Word (x = 1): cyclic runs R_1 S_1 ... R_k S_k, R_i = a_i letters rho_1 and b_i letters
rho_{-1} (r_i = a_i + b_i >= 1), S_j = sigma_{y_j}^{l_j}; S_j lies between R_j and
R_{j+1} (indices mod k).  A = sum a_i, B = sum b_i, R = A + B, F = sum l_j, F + R = 4p-2.
o_F, o_R = numbers of odd reflection / rotation runs; e_F = k - o_F, e_R = k - o_R.

Half values.  eta_j := 2^{-1} y_j in Z_p.  For P subset [k], u_P := 2^{-1} sum_{i in P}
theta_i (theta_i = y_{i-1} - y_i), additive on disjoint unions, u_{[k]} = 0.  For the
cyclic interval P = (a, b] := {a+1, ..., b}: u_P = eta_a - eta_b.

Half windows.  Lemma WAS (../repr-WAS.md, reviewed): avoid iff 2u_P notin Ach(z_P)
mod p for all P.  Ach is the set of even integers in [lo, hi]; dividing by 2,
avoid iff u_P notin I(P) := Z cap [lo/2, hi/2] (mod p) for all P, where with
c := C_max/2 and Phi(P) = number of cyclic boundaries of P,
  I(P) = [ max(-(p - Phi/2), p - c - E-, -floor(E-/2)),
           min(  p - Phi/2,  E+ + c - p,  floor(E+/2)) ],
E+ = A_P + B_{P^c}, E- = B_P + A_{P^c} (E+ + E- = R).  (hi/2: s1/2 = p - Phi/2,
(2E+ - s0)/2 = E+ + c - p, floor(E+/2); lo/2 rounded up likewise.)

Key parameters.  H = (F - o_F)/2.  kappa := p - 1 - H = (R + o_F - 2p)/2 (integer since
F + R even and F = o_F mod 2).
* P = empty (or [k]): c = H = p - 1 - kappa, I(empty) contains 0 iff min(A, B) >= kappa + 1.
  So avoid => min(A, B) <= kappa ("zero condition").
* P = (a, b] proper cyclic interval: Phi = 2, c_P = H + 1 - e_P = p - kappa - e_P with
  e_P := [l_a even] + [l_b even] (the two boundary reflection runs S_a, S_b), so
  U_P := min(p-1, E+_P - kappa - e_P, floor(E+_P/2)),
  L_P := max(-(p-1), kappa + e_P - E-_P, -floor(E-_P/2)),
  I(P) = [L_P, U_P];  allowed arc J(P) := Z_p \ I(P) = [U_P + 1, L_P + p - 1] (mod p).
  Complement: U_{P^c} = -L_P, L_{P^c} = -U_P.

Inherited conditions in these parameters (F = 4p - 2 - R):
  (Pairs) <=> R + o_F >= 2p <=> kappa >= 0;   (V) <=> R - o_F <= 2p - 2 <=> kappa <= o_F - 1;
  (P) <=> R + o_R >= 2p;   (E) implied by (V) and o_F <= k <= p;   (D0) as stated.

## 2. Attack protocol (frozen)

A. Proof route ("lap" argument): lift u_{{i}} into J({i}); show the lifts of a
   solution go once around Z_p (sum exactly p) and every proper interval sum lies in
   its own arc J(P) without wrap; the avoidance system then becomes a difference-
   constraint system on prefix sums S_0 = 0, S_k = p, S_b - S_a in [U_{(a,b]} + 1,
   L_{(a,b]} + p - 1]; prove it infeasible for every violator by explicit negative
   cycles (chains of interval lower bounds against p).  Full windows and the zero
   condition are value-independent certificates handled first.
B. Computation (aid only; never a proof for other p): python scripts here,
   (B1) control: half-window formulas vs ../code/gr_window.py ach on random run data;
   (B2) p = 5 (all k <= 5) and p = 7 (k <= 7) inherited PAR violators: record which
        certificates (zero, full window, lap-linear infeasibility with the
        one-lap hypotheses verified) cover them, and the shape of negative cycles;
   (B3) p = 11, 13: structured families suggested by the proof attempts.
   Every claimed counterexample must be re-checked by the raw ordered-product DP
   ../code/was_verify.py dp_has on the explicit word before any report.
Resource caps: <= 2 CPU, <= 4 GiB, chunks <= 30 min, host-clock labels.

## 3. Results (appended 2026-10-17T05:55 PDT; Sec. 1-2 unchanged)

Deviation from protocol A (recorded, not a change of target): the interval-only "lap" route
is insufficient (notes-checkpoint.md F1: p = 11 run datum with 18 interval-feasible theta,
all killed only by 2-bracket patterns), so the proofs use general patterns (lambda formula
for every pattern, Lemma H of proof-PAR-K0.md) and the block-chain Lemma BC.
Files:
* proof-PAR-K0.md: Lemma H, Lemma BC, Theorem K0 (PAR for kappa = 0, all p).
* proof-PAR-Kplus-partial.md: Lemma OR (odd-segment reduction), Theorems K1, K1'
  (kappa = 1), Lemma IP, Proposition S1' + Lemma A1' (B = 0, k <= p), Theorem KB
  (B = kappa, o_F <= p), precise open statement (Sec. 4) and failed approaches (Sec. 5).
* notes-checkpoint.md: dated checkpoints with every numerical control and its scope.
* par_windows.py (window formulas, enumeration), bestpart.cpp (best set partition +
  block-chain check for one run datum); session code for the controls is described in the
  checkpoints (no long-running jobs; all runs were <= 25 min, 1 CPU).
Net status: PAR(p) for all primes p >= 5 is reduced to MIX_DEF(p) restricted to o_F <= p
(all-odd-reflection RGR words of length 4p-2 with 1 <= B < kappa, B <= A); MIX_DEF is
OPEN and is being attacked for all k by OlsonRunCount (../inverse-run-count/mixdef/).
No counterexample: every candidate found by search was killed (raw DP on the p = 11 example).

Correction (2026-10-17T07:39 PDT, from the Codex review relayed by Main): in Sec. 1 the line
"I(empty) contains 0 iff min(A, B) >= kappa + 1" is correct for the integer 0 only; as a
residue condition the empty/full window also contains +-p when A >= 2p or B >= 2p
(counterexample to the unqualified equivalence: p = 5, rho_1^10 sigma_0^8).  The implication
"avoid => min(A, B) <= kappa" stays true (avoiders have A, B <= 2p - 1).  Lemma H in
proof-PAR-K0.md now states the exact condition and the equivalence under A, B <= 2p - 1.
