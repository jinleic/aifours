# T-MAX: frozen scope (before proof text or probe) -- the t = kappa^ obstruction in the high cells

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:42:06-0700, on parent instruction (IRC after verdict
run review/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee...1bc0): 'in (S') with longest zero-sum of length exactly
2kappa^ and 2kappa^ + k >= 2p, k <= p - 1, freeze a scope first; aim either (i) a word-level contradiction ... or (ii) an
explicit small-p obstruction family showing the rotation-sequence route cannot close it (sequence-level only, clearly
labelled)'.  Terminal k = p (S(p)) and terminal k >= p + 1 stay separate parked boundaries.  Lane:
evidence/disposition-BALfull-ROTZB-v1.md 55138906...16c4 records the accepted inputs.

## Setting (T) (sequence level)
p >= 5 prime; k integer, 2 <= k <= p - 1; kappa integer with 1 <= kappa <= k - 1 (DAV) and 2kappa + k >= 2p (HIGH cell;
forces 3k >= 2p + 2); Y a sequence of R = 2p + 2kappa - k odd elements of C_(2p) whose LONGEST zero-sum subsequence has
length EXACTLY 2kappa.  (Equivalently (ZP_kappa) and (S1_kappa) hold and t = kappa.  (S1_kappa) is automatic from (ZP_kappa)
by S1-sharp when kappa <= floor(2p/3) and is an extra hypothesis otherwise; avoiders whose rotation sequence fails (S1)
are a separate parked case.)  Then for every longest Z: L = |Y - Z| = 2p - k in [p + 1, (4p - 2)/3] and L <= 2t, so
BAL-forall and ROOM do not apply.
Word-level context: Y is the rotation sequence (all-plus pattern) of an admissible normal form w^ with terminal k and
kappa^ = kappa (GRX gives (ZP)); 2H = 2p - 2 - 2kappa.

## Objects and claims distinguished
- For c in Z_p^*: E_c(Y), eta_c(Y), a_max,c(Y) are SHgen's quantities for the weights relative to c (rho_(+-c) light,
  b_0 = p).  These depend on Y and c only, NOT on a choice of Z or of a generator g.
- ROUTE(Y) [existential in c]: some c in Z_p^* has E_c = 0, or E_c <= 2H and eta_c + a_max,c <= 2p - 1 - k (SHgen's (H)
  and (K)).  If ROUTE(Y) holds for the rotation sequence of w^, accepted SHgen/SHgen-E (with restricted REFL,
  o_F <= k <= p - 1) give rotation rigidity for w^.  In (T), KETA's k-free inequality makes (K) follow from E_c <= 2H.
- ROUTE-ALL(T): ROUTE(Y) for every Y in (T).  A proof would close the t = kappa^ part of the high cells (with (S1)).
- OBSTRUCTION (option (ii)): an explicit Y in (T) (exact p, k, kappa) with ROUTE(Y) false.  It is SEQUENCE-LEVEL ONLY: it
  does not assert that an avoider with rotation sequence Y exists; it shows that (ZP) + (S1) + t = kappa (all the sequence
  information the BAL/ROOM/SHgen route uses) cannot close the cell, so any proof there must use word-level data (run
  distribution, block values y_i, arc patterns of GRX).
- Balance is recorded separately (existential and universal over (Z, g)); it is not by itself sufficient in (T).
- Option (i) (word-level contradiction via GRX arc patterns) is attempted only after (ii)'s status is known.

## Planned finite aids (each with a launch plan to the parent and a gated pre-launch PID record; aids, never premises)
- p = 7: exhaustive over all multisets (cells (k, kappa) = (6, 4), (6, 5)); control for the normalized enumeration.
- p = 11, 13 (and 17 if budget allows): complete normalized enumeration Y = Y' Z with g = 1 (ZSTRUCT form, accepted via
  its proof in (S')), every candidate checked by an exact zero-sum-length DP; report every Y in (T) with ROUTE(Y) false, and
  per-cell completeness.  A finite search miss is never offered as a proof or as a 'larger finite range' result.
