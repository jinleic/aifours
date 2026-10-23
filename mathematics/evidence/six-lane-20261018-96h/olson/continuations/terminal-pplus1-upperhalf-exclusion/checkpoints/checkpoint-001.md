# Checkpoint 001: UH-EXCL (terminal k = p+1, (p-1)/2 <= kappa^ <= p-3), derivation in progress

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T13:18:36-0700. Scope frozen 13:08:38: UH-EXCL-scope-v1.md, sha256
6ff7fec519944d57c3162f45e1b19403b12a8bea19647634dc86ba20e03d15e9 (4490 bytes). No candidate file written yet.

- Worked so far (written in my notes only, to be frozen in the candidate): with e := p - kappa^ in [3, (p+1)/2], H^ = e-1,
  R = 3p-1-2e: (SR) n even in [max(0, 2kappa+2-2m), min(2p-2m, R)]; pairing (Lemma M/P) gives a dominant signed value of
  multiplicity >= 2kappa+1 for every non-constant pattern exactly because kappa >= (p-1)/2 (2(p-1) <= R and n <= 2kappa);
  dominant class {a,-a}, a != 0, delta <= p-2; all-plus gives A' <= kappa, A <= 2p-1; window (W) e(P) <= lambda = p-2-b or
  e(P) >= Lambda = 2kappa+1-A', gap Lambda - lambda = p-2e+3+delta. Exact route inequalities: heavy single run by first
  passage needs b + delta >= 2e-4; two disjoint high sets are impossible iff delta >= e-2 (else A' >= p-2e+3+delta is
  consistent with A' <= kappa).
- New partial observation: in the +-a case the window of a low arc is an interval [kappa - E_-, U] in x = T/(2a) units, so the
  allowed region is the integer interval [-(e-1-mu(P)), kappa-1-E_-(P)]; when it is nonnegative (mu = e-1, i.e. E_- <= p+1-2e)
  arc sums lift additively. This excludes the pure cell (all rotations equal, kappa^ = (p-1)/2) by a run-budget count; the
  general +-a case still has negative allowed parts where lifts can wrap.
- Parent notices read: RPdelta (not needed) and ASSEMBLY-P acceptance (o_F <= p only; not used, target has no o_F hypothesis).
- Blocker: no whole-interval argument yet for e >= 3 when b + delta < 2e-4 or delta <= e-3 (multiple high sets) or when lifts
  wrap. Next bounded action (<= 30 min): try to close the +-a case with arc lifts plus the light-set structure, then decide
  between a whole-interval proof and an exact sub-range proof plus obstruction note.
