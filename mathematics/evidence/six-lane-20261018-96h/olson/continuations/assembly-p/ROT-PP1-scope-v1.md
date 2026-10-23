# Frozen scope: rotation half at terminal k = p+1, 0 <= kappa^ <= p-2 (Target 2, "ROT-PP1"), v1

Owner OlsonAssemblyP. Frozen after /bin/date 2026-10-19T11:57:04-0700, BEFORE any written derivation for Target 2.
Authority: Main's assignment to OlsonAssemblyP (2026-10-19), Target 2, started after Target 1 was delivered
(proof-ASSEMBLY-P-v2.md 059033b0...cfb5, reported to Main). Status of every statement below: CANDIDATE_UNVERIFIED target, NOT a
proof and NOT a verdict. Written research only (no computation, enumeration, solver, test, build or model CLI). Reflection
rigidity is NOT touched beyond o_F <= p.

## Setting (accepted definitions only)
p >= 7 prime; w an avoider of length 4p-2 over D_(2p); w^ an admissible normal form (accepted NF, existential reading, ZX
overlay 2) with terminal k = p+1 odd blocks S_i = sigma_(y_i)^(l_i), runs R_i (empty runs allowed; every empty run separates
blocks of different values); H^ = (F-k)/2, kappa^ = p-1-H^, so R = p-1+2kappa^ and the rotation sequence Y has
|Y| = p+2kappa^-1 (two below the LS length threshold). GRX (accepted, every cyclic constant-block representation, every sign
pattern) and CT / RS(b) / Cauchy-Davenport as accepted are the intended tools. Pending ROT-SING+ (k = p+1, kappa^ = p-1) is
not a premise.

## Full target (may not be reached)
ROT-PP1: for p >= 7 prime, if SOME admissible normal form of an avoider w of length 4p-2 has terminal k = p+1 and
0 <= kappa^ <= p-2, then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0.

## Candidate pieces to attempt, in this order (each is claimed ONLY if its written proof is completed)
(a) Proposition VAC: an admissible normal form of an avoider never has terminal k >= p+1 together with kappa^ = 0
    (so ROT-PP1 holds vacuously at kappa^ = 0).
(b) Lemma P (pairing) and Lemma U (dominant pair), k = p+1, (p-1)/2 <= kappa^ <= p-2: for every sign pattern with m sign-change
    pairs, 1 <= m <= p-kappa^, the signed rotation multiset has one value of multiplicity >= R-p+2 = 2kappa^+1; there is a
    nonzero a such that all such dominant values lie in {a, -a}; hence all but at most p-2 rotation letters lie in {rho_a,
    rho_-a}. (A structural statement, not rigidity.)
(c) Theorem ROT-PP1-TOP: kappa^ = p-2 at k = p+1 => one nonzero rotation pair (the cell where the sequence statement fails).
(d) Sequence map at |Y| = p+2kappa-1 (no new theorem beyond length comparisons with accepted results): (ZP_kappa) => (S1_kappa)
    holds for kappa <= floor(2p/3) (S1-sharp) and in the accepted LS+ band / BASE1+ cells with e = p-kappa >= 3; it FAILS at
    kappa = p-2 (accepted E2/E3 families of length 3p-5) and at kappa = p-1 (an explicit sequence to be verified in writing);
    it is undecided on U(p).
(e) Obstruction note for every part of 0 <= kappa^ <= p-2 not covered by (a)-(c): exact blocking hypothesis, failed arguments
    with their exact obstruction, and the smallest missing lemma(s), including the word-level replacement for the
    ROT-KP+/ROT-FB(b) step at k = p+1 (complement length p-1 at t = kappa^; SHgen-E would need REFL at o_F(u°) = p+1).

## Deliverables
A proof file for whatever of (a)-(c) is completed (with interface table), a separate obstruction note for (d)-(e), a review
package and an excerpt manifest (<= 100 KB total), checkpoints, and an IRC report to Main. If (c) is not completed, it is
recorded as a failed attempt with the exact point of failure; no partial statement is silently substituted.

## Not claimed
ROT-PP1 in full unless (c) and the remaining range are actually proved; reflection rigidity beyond o_F <= p; INV*; any word-level
assembly at o_F >= p+1; acceptance of ROT-SING+, ONE-SHORT-LS or ROT-SING; p = 5; novelty or priority; Lean; human review.
