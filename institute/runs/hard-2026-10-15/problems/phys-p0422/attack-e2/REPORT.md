# Random 4-SAT and 5-SAT: continued bounded attempt

**Outcome: solved for the frozen numerical contract. Novelty is unknown.**

The written proof and exact rational arithmetic certificates establish:

| k | rational density a_k | frozen benchmark |
|---|---|---|
|4|249/25 = 9.96|10.23|
|5|1057/50 = 21.14|21.33|

For each row, the probability of satisfiability with floor(a_k n) independent
clauses tends to zero as n tends to infinity. Each clause uses a uniformly
chosen set of k distinct variables and independent fair forbidden signs.
Adding clauses gives the conclusion at every larger density. No existence
of a limiting threshold is assumed.

This resolves the requested numerical pair. It is partial progress on the
book's broader Challenge 5: no lower bounds, exact thresholds, other
transition points, or general validated population-dynamics method follow.

## Verification level and attribution

The analytical bridge is a written proof in `notes/PROOF.md`, rechecked
line by line in this continuation. It is not formally verified or externally
refereed. The supplied referee feedback reports no mathematical gap and asks
for attribution, expectation-order, and control fixes; it is supplied review
data, not an independently authenticated publication.

The integer-cost, y-reweighted energetic interpolation is due to Vorobyev
(2026), whose staged preprint treats k=3. This proof re-derives that method
and extends its comparison to general k. The degree-k nonnegative remainder
is credited to Lelarge–Oulamara (2018), following the staged preprint's
condition-(4)/equation-(30) attribution. No independent discovery is claimed.

`code/independent_check.py` retains its historical filename. It is an
algorithmically distinct implementation of the same Psi_T formula, written
by the same producer as `code/certify.py` in the prior attempt. It imports
neither the producer nor its output. Its different product enumeration,
exponential enclosure, grid, and logarithm series cross-check arithmetic;
agreement does not independently establish the formula or analytical bridge.

## What this continuation changed

The existing proof, trials, and certificate package were continued rather
than replaced. The two exact calculations reproduced both claimed margins.
A fresh audit retained the threshold statement and made these corrections:

- Credited Vorobyev's integer-cost comparison and the Lelarge–Oulamara remainder.
- Restated (E) with old rows fixed:
  E_new[W_C^h]=<B_h^k>_h,
  E_new[W_S^h]=<B_h>_h C_h^(k-1), and E_new[W_D^h]=C_h^k.
- Made explicit that (A) holds for every n>=1; the distinct-variable
  model transfer requires n>=k.
- Replaced the finite audit's vacuous control with a sign mutation inside
  `check_system`. A valid witness first passes; reversing the d_y correction
  then gives a rigorously positive lower bound and fails the same comparison
  assertion used by the ordinary audit.
- Relabeled the old noninteger and signed-odd-domain examples as
  illustrative counterexamples, not checker controls.
- Recorded the finite audit's fixed rate law and t=exp(-y)=1/2.
- Added delivery-limit copying and replay of every nonempty ledger command.

There were no new trial searches or optional extensions to other k. No
network, outside-directory reads, delegation, installation, commit, or
external contact was used.

## Proof and numerical premises

For a finite rational warning law rho in [0,1), let Q be the product of k-1
independent warnings, lambda=k alpha/2, and define

    nu_i = E(1-Q)^i,
    M_i = exp(lambda(nu_i-1)),
    mu_j = sum_{i=0}^j (-1)^i binom(j,i) M_i,
    d_infinity = E log(1-R_1...R_k),
    Psi_T = -sum_{j=1}^T mu_j^2/j - (k-1)alpha d_infinity.

The proof gives, at every finite y>0 and n>=1,

    -(y/n) E[min violations in the repeated-variable
              Poisson(alpha n) model] <= Psi_T + T exp(-y).

Its load-bearing steps are the exact insertion identity for integer unit
costs, independent replicas of the tilted old activations, and

    B^k-k B C^(k-1)+(k-1)C^k
      = (B-C)^2 sum_{ell=0}^{k-2}(ell+1)B^(k-2-ell)C^ell >= 0.

The replica quantities B and C lie in [0,1], so the sign holds for odd k=5.
Finite Pascal induction and Poisson thinning replace clauses by independent
one-variable sites. Marked-Poisson generating functions give exact site
moments, with no unaccounted degree tail. The site-log truncation has the
required upper-bound sign; its finite-y error is at most T exp(-y).
No population-dynamics convergence or infinite-y exchange is assumed.

For T=128 and y=20, the explicit trial laws are:

| k | R support numerators over 10000 | mass numerators over 10000 |
|---|---|---|
|4|1745, 7707, 4454|2946, 3363, 3691|
|5|5391, 3691, 7344|1009, 6190, 2801|

Both arithmetic implementations certify these outward enclosures:

| k | enclosure of Psi_128 | epsilon with Psi_128 <= -epsilon |
|---|---|---|
|4|[-0.001462618250731676, -0.001462618250731675]|1/1000|
|5|[-0.000462941572738438, -0.000462941572738437]|1/2500|

They also prove 128 exp(-20) < 0.000000263828 <= epsilon/2.
The staged floating-point probes only selected trials; their output is
not a premise of any certified inequality.

## Model transfers and probability conclusion

The preceding inequality gives expected minimum energy at least c0 n in
the repeated-variable Poisson model, where c0=epsilon/(2y).
Coupling to floor(alpha n) clauses loses at most sqrt(alpha n)+1.
Resampling clauses whose variable tuples repeat loses at most
alpha binom(k,2) in expectation and yields exactly the requested independent
distinct-variable, fair-sign ensemble. Its expected minimum therefore is at
least

    c0 n - sqrt(alpha n) - 1 - alpha binom(k,2).

For c=c0/2 the proof supplies these sufficient cutoffs and bounds:

| k | c0 | c | sufficient N0 | P[SAT], n>=N0 |
|---|---|---|---|---|
|4|1/40000|1/80000|254976000000|<= exp(-n/31872000000)|
|5|1/100000|1/200000|3382400000000|<= exp(-n/422800000000)|

Replacing one clause changes the minimum by at most one, so the bounded
difference lower-tail inequality proves these exponential SAT bounds.
The coarse cutoffs serve the asymptotic theorem; they are not finite-size
predictions.

## Falsification and limits of finite checks

The finite audit enumerates all tables H:{0,1}^n->{0,1,2} for n=1,2,
four specified old-site systems, and k=3,4,5. At the one rate law
rho=(delta_(1/4)+delta_(3/4))/2 and t=1/2, all 1,080 local comparisons
and 1,203,048 clause-insertion checks pass. This verifies only that finite
range, not the universal proof.

The new `--break-comparison` control passes the valid input
n=1, H=(0,1), k=5, old sites (0,0,1/3),(0,1,2/3), then changes the
correction's sign inside the same checking function. The interval lower
bound becomes strictly positive, and the ordinary upper<=0 assertion rejects
it. The replay checks the failure message as well as the nonzero exit.

Other invalid trial witnesses are rejected: zero-warning laws have Psi=0,
and the same nonzero laws at densities 7.9 and 18.7 fail the required negative
margin. The examples H=(0,1/2), penalty=(1,0), and B=-3,C=1,k=5 show why
noninteger costs and signed replica quantities cannot be silently admitted;
their deliberate false assertions are illustrations only.

The staged k=3 trial at 4.268 is reproduced as a functional inequality, not
as verification of the preprint's theorem or claimed Lean development.
The two target densities exceed the supplied cavity estimates 9.931 and
21.117; this is a sanity check, not a proof premise.

## Baseline and literature limitations

Before changing the proof or arithmetic, this continuation rechecked the
staged Achlioptas–Peres text and ran `code/baseline.py`. Its introduction
and Table 10 report 10.23 and 21.33 and cite Dubois–Boufkhad (1997) and
Kirousis et al. (1998). The original papers are absent from this directory.
The supplied reader's ensemble description is not used to silently identify
the requested distinct-variable model.

`notes/BASELINE.md` instead derives the classical one-flip criterion
directly on that model:

    (1-2^-k)^a [2-exp(-ka/(2^k-1))] = 1.

Exact exponential and logarithm enclosures put its positive roots in
(10.22,10.23) and (21.32,21.33). Thus the displayed benchmarks are upper
roundings. The certified densities are below both reconstructed classical
values and the frozen numerical targets.

Achlioptas–Menchaca-Mendez (2012), Lelarge–Oulamara (2018), and their citing
works are not staged. A current literature check is unavailable under the
no-network/no-external-read rule. Nothing here asserts that no later work
already established these or stronger bounds. Novelty remains unknown.

## Deliverables, replay, and remaining work

- `notes/PROOF.md`: complete written comparison, finite-y estimate,
  ensemble transfers, concentration, and arithmetic enclosure lemmas.
- `notes/AUDIT.md`: analytic assumptions, attribution, and control audit.
- `notes/BASELINE.md`: source limitations and classical criterion derivation.
- `certificates/trials.json` and `certificates/results.json`: rational
  witnesses and exact moment/functional enclosures.
- `code/`: deterministic computations using Python's standard library.
- `claims.json`: six claims, atomically published and schema checked.
- `logs/`: numerical evidence, finite checks, rejected controls, and
  delivery-copy replay records.

Run `python3 code/replay.py` for the numerical and finite-audit package.
Run `python3 code/delivery_replay.py` to make a filtered local snapshot
and test every ledger verify/check/control command there with the specified
300-second per-command and 1,800-second aggregate limits. All command
executions use Python, with no locally built executable.

No analytic bridge is left as a conditional premise of the frozen pair.
The remaining verification limitation is that the analytical proof is a
written, manually audited argument, not a kernel-checked or externally
refereed theorem. Current literature novelty and the broader book challenge
remain unresolved. The best next step is independent mathematical review
or formalization of the proof, before further trial optimization.

Continuation start: **2026-10-15 21:23:56 UTC**.
Deliverable target: **2026-10-16 00:17:56 UTC** (174 minutes).
Hard stop: **2026-10-16 00:48:56 UTC** (205 minutes).
Full continuation replay: **all checks passed in 54.20 seconds**, including
the expected checker rejections, both domain illustrations, and schema
validation. The filtered delivery copy included every claim-evidence file:
**57 files, 3,304,166 bytes**, with no size/count-limit loss. Its **12 nonempty
claim commands plus schema validation all passed in 56.50 seconds**; the
longest command took 22.11 seconds, within the 300-second individual and
1,800-second aggregate limits. Correct controls exited 1; verify/check
commands exited 0. Details and exact copied-file hashes are in
`logs/delivery-replay.json` and `logs/delivery-commands/`.

Completed **2026-10-15 21:34:56 UTC**, about 11 minutes after continuation
start and before the deliverable deadline. Stopping because the frozen
numerical pair and the justified referee fixes are complete. No automatic
continuation or outside review has been scheduled.
