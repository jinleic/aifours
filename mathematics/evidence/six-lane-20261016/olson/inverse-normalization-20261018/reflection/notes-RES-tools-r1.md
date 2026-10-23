# Tools for the residual RES_<(p): RPT, SHIFT, CON, FW-G, EVEN, and the refined residual (RED+)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T03:32:55-0700.  Status [W], UNREVIEWED.  Builds on
proof-K0star-r1.md (99a8f2e0...9488) and proof-RED-r1.md (fa6c5054...bb3); notation as there.  None of this closes RES_<(p).

## 1. Exact and dominated moves

**Lemma RPT (reflection-pair transfer).**  Moving one pair sigma_y sigma_y out of a block of length >= 3 into any other block
sigma_y'^l' (as sigma_y' sigma_y', keeping both blocks nonempty) leaves every GR0 (GRX) condition unchanged: F, every block parity,
Phi, delta, C_max = F - delta, E+-, tau are unchanged (block lengths enter GR0 only through F and parities).  So an all-odd word is
determined, for avoidance, by the cyclic sequence of (run contents, block values) and H; in particular WLOG every block but one
is a single letter.  (GRX is parent-accepted for every representation.)  []
**Lemma SHIFT.**  In an all-odd G-avoider, let t be an empty run and P a proper pattern with t notin P, exactly one of t - 1,
t + 1 in P, and P u {t} proper.  Then u_P and u_P + u_t both avoid I(P) (mod p).  Consequently, if A(P) := Z_p \ I(P) and
||c|| denotes the distance of c to 0 in Z_p, then |I(P)| <= p - 1 - ||u_t||.
Proof.  P u {t} has the same m (t lengthens the interval of P that contains its neighbour), beta = 0 (all-odd) and the same
D (d_t = 0), so I(P u {t}) = I(P) (Lemma H0); avoidance of P u {t} gives u_P + u_t notin I(P).  A(P) is a set of p - |I(P)|
cyclically consecutive residues containing two residues that differ by u_t, so p - |I(P)| >= ||u_t|| + 1.  []
(Example of use: for an interval P = {t+1, ..., j} with E+(P), E-(P) in [2 kappa - 1, 2p - 2], |I(P)| >= R/2, so
||u_t|| <= (k - 2 kappa - 2)/2; if moreover k <= 2 kappa + 3 this contradicts u_t != 0.)
**Lemma CON (contraction at theta = 2x).**  Let t be an empty run between SINGLE-letter blocks sigma_u, sigma_v with u - v = 2x
(mod p), x in {1, -1}, and suppose the run R_(t-1) (or R_(t+1)) contains a letter rho_x.  Delete sigma_u, sigma_v and insert two
letters rho_x into that run (R_(t-1), R_t, R_(t+1) merge).  If w avoids, so does the result: it has the same length, kappa, H,
two blocks and one empty run fewer, R + 2, and B unchanged when x = 1.
Proof.  Inside a run the order of rotations is irrelevant (GRX depends on run multisets only), so let R_(t-1) end with rho_x.
X := rho_x sigma_u sigma_v is contiguous; Y := rho_x rho_x rho_x.  Spec(Y) = {(0,1), (1, rho_x), (2, rho_2x), (3, rho_3x)} and
Spec(X) contains (1, rho_x), (2, sigma_u sigma_v) = (2, rho_(u-v)) = (2, rho_2x) and (3, rho_x sigma_u sigma_v) = (3, rho_3x).
Lemma SPEC.  (Right-hand version: X := sigma_u sigma_v rho_x.)  []
(Only theta = +-2 works: a one-reflection-pair segment sigma_u sigma_v next to rotations is dominated by rotations only if the pair
product rho_(u-v) equals the product of two available rotations.)
**Lemma FW-G (full window from p + 1 boundaries; proof-RUNS.md L23-32 re-checked).**  In any G-word, a pattern P with
m(P) = (p + 1)/2 and E+(P), E-(P) >= p - 1 has a full window, so the word is solvable.  (h(P) = H - beta(P) >= 0 is all that is
used.)  []
**Lemma EVEN.**  Any word of length 4p - 2 over D_(2p) (arbitrary letters) all of whose maximal cyclic reflection runs have even
length is solvable.  Proof: Lemma G of proof-T0.md (its size bound needs only length <= 4p - 1): cut at the start of a rotation
run, tile every reflection run by ff units (depth 1, any values) and the R (even) rotations by nests r_(2i-1)[...]r_(2i); total
depth F/2 + R/2 = 2p - 1.  If R = 0 this is Lemma AR.  []  In an all-odd G-avoider some maximal reflection run therefore
contains an odd number of constant blocks.

## 2. Refined residual

**Theorem RED+.**  Under the hypotheses of Theorem RED: REFL(p) holds iff no word of RES_<^+(p) avoids, where RES_<^+(p) is the
set of words of RES_<(p) with kappa >= 2 such that, after Lemma RPT, no empty run t with u_t = 1 has a letter rho_1 in an adjacent
run.  Necessary conditions for an avoider in RES_<^+(p) include those of proof-RED-r1.md Sec. 6, Lemma SHIFT for every empty
run, and Lemma EVEN.
Proof.  Choose an avoider w in RES_<(p) of minimal (kappa, g, k) (lexicographic).  If CON with x = 1 applies at some empty run
(after RPT, which needs a third block: k >= kappa + 2 >= 4), the result w2 avoids with the same kappa and B, g - 1 empty runs.
If g(w2) = 0, w2 is an RGR avoider with B < kappa, impossible by (I1), (I2).  Otherwise run the process of Theorem RED on w2: every
exit is contradictory and the terminal state is an avoider in RES_<(p) whose (kappa, g, k) is at most that of w2, which is
smaller than that of w.  Contradiction with minimality.  []

## 3. Failed route recorded (finite aid, plan-E6.md frozen 03:30:57)

out/e6_interval_probe.json (code/e6_interval_probe.py): cyclic-interval patterns plus the zero pattern do NOT certify RES_<
words.  One seeded random run datum per stratum (p, kappa, B, k): p = 7: 170 strata, 101 with interval-feasible value
assignments (up to 51,394 per run datum in the kappa = 6, H = 0 slices); p = 11 (k <= 16): 272 strata, 66 interval-feasible.
5,971 interval-feasible assignments decided by raw DP: all solvable (0 candidate counterexamples; a miss is UNKNOWN).  Positive
control: for the sharpness run datum at length 4p - 3 (p = 7, 11) the same pipeline finds its unique interval-feasible
assignment and the DP confirms it avoids.  So any proof of REFL-RES(p) must use patterns with m >= 2 (the analogue of the
integrality arguments of Theorem M / NMH for RGR words).
