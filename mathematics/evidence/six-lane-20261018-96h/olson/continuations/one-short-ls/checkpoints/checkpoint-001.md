# Checkpoint 001 -- ONE-SHORT-LS: scope frozen; written route found; proof text being frozen next

Owner OlsonAssemblyLS. Written after /bin/date 2026-10-19T10:31:08-0700. Slice began 10:17:29 (directory creation).
No computation, enumeration, script, solver, test, build or model CLI. No Python yet in this slice. Writes only here.
Parent IRC after the assembly Codex return (parent erratum 572308b8...; no worker edit) received: target unchanged.

## Actual result so far (all CANDIDATE_UNVERIFIED, nothing frozen as a proof yet)
- Scope frozen 10:17:32: ONE-SHORT-LS-scope-v1.md 2b9cfbcdf66cf43b173aa2f9a43542c906b50e04cbae690a860e3c321dd5b872 (sent to parent).
- Read at original scope: G-LS proof (whole), CF(a)-(c), RS/DGM-p/Theorem U/ROW/dichotomies (+ erratum 1 E1-E5, prereq erratum
  R1-R13), LS-II v2 + addendum (LS-II'), AP' (+ D1), LS+2 with Lemma CT, CTgen, SLZ3; verdicts CFXT-ROW-LSII, STAB-delta,
  LSplus-chain, LSplus-partials, BASE2-cells, SLZ3, general-LS.
- Finding 1 (DGM-p does not apply): DGM-p needs |Y| >= p+2kappa+1. Replacement found: accepted Lemma CT with n = p-2
  (|Y|-n = 2kappa+2) gives at most two values of multiplicity >= p-1; two such values force Y = iota^(2kappa+1) x1^(p-1)
  (no long zero-sum, using p not dividing 2kappa+2); one gives an odd generator g with M >= 2kappa+2, d = 2p-M <= 2e-2,
  r <= p-2. (The p | 2kappa+2 step is exactly where kappa = p-1 fails, matching the excluded endpoint.)
- Finding 2: accepted ROW at K = p-2e gives (I) d <= e-1 or (II) one dominant U-value, others <= e-1.
- Finding 3 (case II): LS-II' re-derived at the new constants; Step 1 now needs AP' (arc 2e-1), giving mu1 in {1,-1,1/2,-1/2};
  1 and 1/2 are forbidden by CF; -1/2 is the involution, killed by an elementary involution-pair lemma (IP: in a (ZP) sequence a
  long zero-sum T has |T| - v_iota(T) >= 2p+1); -1 closes with the old Steps 3-5' (c' <= 2e-3, drop <= 2e-2).
- Finding 4 (case I): the G-LS core goes through with every constant shifted by one (n = p-2e+delta', few-sums margin
  p-3e+2delta'-t >= 2, R <= e-delta'+1, s >= p-3e+2delta'+1). Pinning: delta' >= 2 by AP'; delta' = 1 needs a NEW arc-(2N+2)
  lemma (AP'', proof written: b in {+-1,+-2}, or +-3 when N = 1) and leaves a new branch b = -2 iff S = n, where U' is all
  involutions; IP kills it. e = 2 handled (d = 1). The witness step needs only |T| <= |Y| (SLZ3 not required).

## Exact blocker
None found. Lev 2022 Theorem 2 (statement level) is used in case (I), as in G-LS; e = 2, p >= 10e-13 and BASE1 cells are also
covered without Lev by accepted LS+ cells (LS+ implies one-short LS since 3kappa+1 < p+2kappa).

## Next bounded action
Freeze proof-ONE-SHORT-LS-v1.md (statement, new lemmas IP, DOM, AP'', case II, case I, constant-change table vs G-LS, trust and
cross-coverage), then review package + manifest (<= 100 KB) and report path+SHA256 to the parent.
