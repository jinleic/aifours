# RUNS(p) for inherited RGR avoiders of length 4p-2 (task OlsonRunCount)

Owner of this directory only: task OlsonRunCount (sub-agent of the six-lane run).
Read-only inputs: ../proof-GR.md (Lemma GR), ../repr-WAS.md (Lemma WAS + Sec. 5),
../proof-INV-reduction.md (Theorem DR-Res, statement of RUNS(p)), ../proof-DR.md.
Host clock read before writing this freeze: 2026-10-17T02:44:47-07:00.

## 1. Target (exact, unchanged from ../proof-INV-reduction.md Sec. 2)

RUNS(p), p prime >= 5: if w' is an RGR word of length N = 4p-2 over D_{2p} with
F, R >= 1 (k rotation runs, k reflection runs, x normalised to 1) which is
*inherited* -- (E) R <= 3p-2; (P) F + sum_i floor(r_i/2) <= 3p-2; (V) R + H <= 3p-2;
(Pairs) H <= p-1; (D0) a_i, b_i <= p-1 -- and has no identity 2p-subword, then k <= p.
Not hypotheses: parity of runs (PAR is a separate lemma and is applied AFTER RUNS
in Theorem DR-Res), unique theta, equal brackets, constant rotation runs.

## 2. Frozen representation (half-window form of Lemma WAS; exact)

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1).
Cyclic runs R_1 S_1 ... R_k S_k; R_i: a_i letters rho_1, b_i letters rho_{-1},
r_i = a_i + b_i; S_j = sigma_{y_j}^{l_j}; F = sum l_j, R = sum r_i, H = sum floor(l_j/2).
Half jumps phi_i := (y_{i-1} - y_i)/2 in Z_p (y_0 := y_k); sum_i phi_i = 0 and every
zero-sum phi arises.  For P subset [k] (zone "+" runs):
  f_j(P) = [exactly one of j, j+1 in P]  (boundary at reflection run S_j),
  m(P) = (sum_j f_j)/2,   h(P) = sum_j floor((l_j - f_j)/2) = H - #{j : f_j = 1, l_j even},
  E+(P) = sum_{i in P} a_i + sum_{i notin P} b_i,   E-(P) = R - E+(P),
  g_P(E) = min(p - m, E + m + h - p, floor(E/2)),
  I(P) = { x in Z : -g_P(E-(P)) <= x <= g_P(E+(P)) }   (possibly empty).
**Lemma HW.**  The word has NO identity 2p-subword iff for every P subset [k]:
  sum_{i in P} phi_i  is not congruent mod p to any element of I(P).
Derivation (from Lemma GR / Lemma WAS, any length N): C_max(P) = F - delta(P)
= 2m + 2h(P) (per run: f = 0 gives 2 floor(l/2), f = 1 gives 1 + 2 floor((l-1)/2));
so s1 = 2p - 2m and s0 = 2p - 2m - 2h are even, Ach(z_P) = 2Z cap [L, U] and
t in Ach <=> t/2 in [ceil(L/2), floor(U/2)] = I(P); t = tau(P) (mod p) <=>
t/2 = tau(P)/2 = sum_P phi_i (mod p) since 2 is invertible.
Complement symmetry: I(P^c) = -I(P), sum_{P^c} phi = -sum_P phi.

## 3. Protocol (bounded; aids only)

Q1 (exact checks of the representation): Lemma HW decision vs a fresh raw
ordered-product DP over D_{2p} on random RGR words (p = 5, 7, 11; lengths 4p-2,
4p-3, 4p-1), with counter-controls (NO instances must exist at 4p-2/4p-3).
Q2 (certificate structure, finite-exact aids): for inherited run data with
k >= p+1 at p = 5, 7 (all), p = 11 (structured families only), record which
explicit pattern families certify infeasibility (full windows with m = (p+1)/2;
zero windows; interval chains; small-bracket families).  Guides a proof; not a proof.
Q3 (refutation): only an explicit word confirmed by the raw DP counts.
Resource caps: <= 2 CPU, <= 4 GiB, chunks <= 30 min, host-clock labels.
Universal statements are claimed only with written proofs (proof-RUNS.md);
finite checks are labelled [F] and never used as hypotheses.

## 4. Status log (host clock)

2026-10-17T05:03 PDT.  Written proofs ([W], unreviewed) in proof-RUNS.md:
Secs. 1-6 (FW, ALT, zero certificate, TL, KW, ND), Secs. 9-10 (S1, Depth Lemma, C0-B),
Sec. 11 (C0-B' for R <= 2p-2 without inherited hypotheses, Lemma A1 for R = 2p-1, trivial
cut A >= 2p, Lemma OR [OlsonParity] rechecked, Corollary B0, kappa = 0 via OlsonParity's
K0 with k <= p shown unnecessary), Sec. 12 (pair removal M0, Corollary MNA).
Consequence: RUNS(p) holds whenever B = 0 after normalisation.  Open: B >= 1.
Finite aids for the open part: inherited p = 5, all splits, B >= 1 and A <= 2p-2: no
avoider for any k (hwsearch_mixa); mixed_test.py / check_M2.py (p = 7, 11): every
interval-feasible phi is killed by the defect set Z, a depth-ordered prefix of Z, or such a
prefix plus 1-2 runs with bh = 1; the C0 depth bound fails for anti-aligned defects (they
reach the singleton bound 2(kappa - B) - 2 - d_t).

2026-10-17T05:33 PDT.  Added: B = 0 statement holds for ALL RGR words of length 4p-2 with
k >= p+1 (no inherited hypothesis; proof-RUNS.md Sec. 11 status); Lemma PM (merge across one
even reflection run); kappa = 1 closed via OlsonParity's K1' (valid for every k, rechecked);
Sec. 13 states the open part MIX_RUNS(p): k >= p+1, 1 <= B <= kappa, now only kappa >= 2,
with evidence and failed approaches.  Files added since 05:03: check_A1.py, check_M2*.py,
mixed_test.py, z3lib.py, z3_step1*.py, z3_B1.py, hwsearch_{c0a,c0b,mixa,mixa1,mixo}.cpp,
fa_minm.cpp, fwminm.cpp, check_C0B_ineq.py.
