# Notes v5: 3-adic structure of the odd model at n = 27 (written 2026-10-17 15:54:29 PDT)

## L1 (mod-q relaxation) [definition + computation]
Reducing an odd CFR(r,27) normal form modulo q in {3, 9} gives, for every pair of DM rows, the half-column profile:
#{a in 1..13 : D(a) = 0 mod q} = (27/q - 1)/2 and #{a : D(a) = +-g mod q} = 27/q for g = 1..(q-1)/2.
`../code/oddmod_relax_cnf.py` encodes this (sequential counters with full equivalences). kissat (relax/): r = 4 and
r = 5 relaxations mod 9 and mod 3 are SAT (r = 5 mod 9: 1.4 s). So no obstruction at the mod-9 level.

## L2 (top-level lifting is overdetermined) [written derivation; heuristic consequence labelled]
Write r_j(a) = rbar_j(a) + 9 e_j(a) (rbar in 0..8, e in Z_3). For a pair (i,j) and half-column a with
rbar_i - rbar_j = 0 the difference is 9(e_i - e_j): need e_i != e_j. Otherwise, with sign sigma and class rho in
{1,2,3,4} (sigma*(rbar_i - rbar_j) = rho + 9 kappa, kappa in {0,-1}), sigma*D = rho + 9 delta with
delta = kappa + sigma (e_i - e_j) mod 3, and the three half-columns of class rho must have distinct delta. Distinct
triples in Z_3 sum to 0, so each (pair, class) gives the LINEAR equation sum delta = 0 (mod 3). With rows 0 and id
fixed and 4 unknown rows: 14 pairs x 4 classes = 56 linear equations over GF(3) in 52 digit unknowns, plus 56
"not all equal" and 14 "!=" conditions. [HEURISTIC] A generic mod-9 pattern therefore lifts with probability about
3^-4 (consistency) x (2/3)^56 x (2/3)^14 ~ 6e-15, which is consistent with the E6 count (~8e5 ordered odd solutions
over ~1e20 mod-9 patterns). For r = 4 the system is 36 x 39 (underdetermined), matching the abundance of odd
CFR(4,27). This explains the r = 4 -> r = 5 cliff but is NOT a nonexistence proof.
