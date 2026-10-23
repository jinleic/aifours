# Handoff state for the INV(p) stage (ordered Olson, dihedral D_{2p}, RGR words)

Lane root: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/
Written by MathOlson after host clock 2026-10-17T02:20:58-07:00.  Read in this order:

1. proof-GR.md          Lemma GR (exact iff-criterion for RGR words, any length N);
                        reviewed (Claude max); parent raw-DP replay PASS.
2. repr-WAS.md          Lemma WAS: avoid iff sum_{i in P} theta_i notin W(P) for every
                        zone set P (theta_i = y_{i-1} - y_i); Sec. 4 results (finite-exact,
                        code-fidelity review TIMED OUT, not accepted); Sec. 5 review fix.
3. proof-DR.md          Theorem DR / Corollary DR' (reviewed correct): INV(p) => all
                        RGR words of length 4p-1 solvable; INV*(p) + INV(p) => ordered
                        Olson for D_{2p}.
4. repr-INV.md          frozen INV representation (bracket/mark coordinates; value
                        V = sum_{i in P} beta_i + sum_i (mu_i^+ - mu_i^-), beta_i = theta_i - d_i).
5. proof-INV-reduction.md  Theorem DR-Res (reviewed: correct with minor fixes, applied;
                        review/claude-DRRes/receipt.json) (only inherited avoiders matter: (E),(P),
                        (V),(Pairs),(D0)); the two open lemmas PAR(p) [k <= p => all
                        runs odd] and RUNS(p) [k <= p]; certificate data (Sec. 3, 3.1).

Exact open target: prove PAR(p) and RUNS(p) for every prime p >= 5 (or refute one
with an explicit word verified by raw DP).  Then Theorem DR-Res closes ordered Olson
for all RGR words; full D_{2p} additionally needs INV*(p) (open; true at p = 5).

What the data says (aids only, never hypotheses):
* PAR is certified at p = 5, 7 by single-bracket patterns (P = empty or a cyclic
  interval of rotation runs); elementary brackets alone are not enough; "joint"
  certificates (no single full window) are forced-difference contradictions among
  reflection values.
* RUNS needs more brackets (p = 5: up to 3 for k = 2p-1, the fully alternating
  words, whose windows are explicit step-2 sets, proof-INV-reduction.md 3.1).
* Extremal avoiders at 4p-2 (p = 5, 7): all runs odd, constant rotation runs, all
  brackets = rho_{+-1}, k <= p, unique theta; exact counts repr-WAS.md 4.3.

Tools: code/was_search.cpp (WAS solver; fam=m keeps patterns with <= m brackets),
code/inv_classify.cpp (zero/full/joint/none certificate classes for inherited words;
fam=-1 elementary brackets; env INV_RUNS=1 for k > p), code/was_verify.py (raw DP,
canonical keys, dump comparison), code/gr_window.py (Ach), code/inv_brackets.py.
Rules carried over: no git, no deletion, lane-only writes, <= 4 CPU workers, <= 30 min
uncheckpointed compute, host-clock labels, Claude opus-5-5 max = cross-vendor review
for the current OpenAI parent, timeouts are not verdicts.
