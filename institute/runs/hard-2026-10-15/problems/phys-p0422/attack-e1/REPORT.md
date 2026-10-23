# Random 4-SAT and 5-SAT: bounded research result

**Outcome: solved for the frozen numerical contract. Novelty is unknown.**

For independent clauses with uniformly distinct variable sets and independent
fair signs, the following densities give asymptotic unsatisfiability:

| k | proved rational density a_k | frozen benchmark |
|---|---|---|
|4|249/25 = 9.96|10.23|
|5|1057/50 = 21.14|21.33|

In each case P[SAT with floor(a_k n) clauses] tends to zero. Monotonicity
gives the conclusion at all larger densities, without assuming existence
of a limiting threshold. This resolves the concrete pair in the frozen
contract and remains partial progress on the book's broader Challenge 5:
no lower bounds, exact thresholds, or general validated population-dynamics
framework are established.

Start: **2026-10-15 19:22:43 UTC**. Hard stop: 23:22:43 UTC; deliverable target:
22:46:43 UTC. All work stayed in this directory. There was no network,
delegation, installation, commit, external contact, or proof-assistant claim.

Completed: **2026-10-15 19:39:33 UTC**, about 17 minutes after the start.
The final full replay passed in 54.09 seconds, including all expected failing
controls and schema validation of the six-claim `solved` ledger. The replay
log is `logs/replay.txt`. Stopping early because the frozen pair is established.

## Deliverables and replay

- `notes/PROOF.md`: the complete comparison, finite-y estimate, model
  transfers, concentration argument, and numerical enclosure lemmas.
- `certificates/trials.json`: explicit rational trials; `results.json`:
  exact rational functional and moment enclosures.
- `code/certify.py`: producer using binary intervals and repeated squaring.
- `code/independent_check.py`: separate exact checker using multinomial
  products, decimal intervals, Taylor/reciprocal exponentials, and atanh
  logarithms. It imports neither the producer nor its results.
- `notes/AUDIT.md`: assumption-by-assumption adversarial audit.
- `notes/BASELINE.md`: staged-source limitations and independent reconstruction
  of the classical one-flip criterion on the requested ensemble.
- `claims.json`: atomically rewritten ledger, checked against the schema.
- `logs/`: numerical replay, finite checks, and rejected negative controls.

Run from this directory:

```sh
python3 code/replay.py
```

This sequential standard-library replay checks the certificates, finite sanity
range, baseline equation, explicit theorem constants, all negative controls,
and claim schema. It reports `ALL REPLAY CHECKS PASSED` on success. The
analytical proof is human-readable; finite replay does not verify its universal
quantifiers.

## What worked

The staged recent k=3 preprint suggested comparing integer minimum violation
counts directly. We proved that comparison independently at every k>=2,
without invoking the preprint's theorem or claimed Lean verification.
Adding a unit-cost constraint raises the minimum by one exactly when every
old minimizer violates it. For a clause the two universal quantifiers, over
literal positions and over minimizers, commute. Independent replicas of the
reweighted old activations give nonnegative quantities B,C and the inequality

    B^k-k B C^(k-1)+(k-1)C^k
      = (B-C)^2 sum_{ell=0}^{k-2}(ell+1)B^(k-2-ell)C^ell >= 0.

This covers odd k=5 explicitly. Finite replacement and Poissonization then
compare clauses to independent one-variable sites. Their moments are exact
marked-Poisson generating functions, so there is no unaccounted degree tail.
The resulting universally proved inequality is

    -(y/n) E[min violations in the repeated-variable
              Poisson(alpha n) model] <= Psi_T + T exp(-y).

At T=128 and y=20 the explicit trial laws are:

| k | R support numerators over 10000 | probability numerators over 10000 |
|---|---|---|
|4|1745, 7707, 4454|2946, 3363, 3691|
|5|5391, 3691, 7344|1009, 6190, 2801|

Both exact implementations certify these outward enclosures:

| k | enclosure of Psi_128 | certified epsilon, with Psi_128 <= -epsilon |
|---|---|---|
|4|[-0.001462618250731676, -0.001462618250731675]|1/1000|
|5|[-0.000462941572738438, -0.000462941572738437]|1/2500|

They also certify 128 exp(-20) < 0.000000263828 <= epsilon/2 in each case.
The negative functional values have a complete analytical bridge to the
threshold statement. No fixed point or population-dynamics convergence is
assumed. The staged floating-point probes selected trials only.

## Model transfers and explicit probability bounds

The Poisson model has expected minimum energy at least c0 n, where
c0=epsilon/(2y). Coupling to floor(alpha n) clauses loses at most
sqrt(alpha n)+1. Resampling clauses with repeated indices loses at most
alpha binom(k,2) in expectation and produces exactly the requested independent
distinct-variable, fair-sign model. Thus its expected minimum is at least

    c0 n - sqrt(alpha n) - 1 - alpha binom(k,2).

It is at least c n with c=c0/2 beyond these explicit cutoffs. Replacing one
clause changes the minimum by at most one, giving the probability bounds:

| k | c0 | c | sufficient N0 | P[SAT], every n>=N0 |
|---|---|---|---|---|
|4|1/40000|1/80000|254976000000|<= exp(-n/31872000000)|
|5|1/100000|1/200000|3382400000000|<= exp(-n/422800000000)|

These deliberately coarse cutoffs make the asymptotic proof explicit. They
are not predictions of practical finite-size behavior.

## Falsification, failed extensions, and controls

Exact checks enumerated all H:{0,1}^n->{0,1,2}, n=1,2, four specified old-site
systems, and k=3,4,5. All **1,080 local comparisons** and **1,203,048 insertion
checks** passed. This is exhaustive only for that finite range. The universal
theorem is proved analytically in `notes/PROOF.md`.

Deliberately broken controls fail with exit code 1:

- Zero-warning laws give Psi=0 and are rejected for both k.
- The same nonzero trial laws at densities 7.9 and 18.7 fail certification.
- A noninteger extension of the insertion identity fails at H=(0,1/2),
  penalty=(1,0), whose increment is 1/2. All costs used in the proof are integers.
- A signed extension of the odd-k polynomial fails at B=-3,C=1,k=5, giving
  -224. The actual quantities in the proof are explicitly nonnegative.

The staged k=3 trial at 4.268 is also reproduced as a functional inequality.
The preprint's k=3 theorem and claimed Lean code are not premises here.

## Baseline audit and unavailable checks

The staged Achlioptas–Peres reader reports 10.23 and 21.33, with references
to Dubois–Boufkhad (1997) and Kirousis et al. (1998). Neither original primary
text is present. Achlioptas–Menchaca-Mendez (2012), Lelarge–Oulamara (2018),
and their citing works are also absent. The no-network/no-external-read rule
prevents a current literature check. No new-best or novelty assertion is made.

We independently rederived the classical one-flip criterion on the requested
model and certified its positive roots in (10.22,10.23) for k=4 and
(21.32,21.33) for k=5. The table entries are therefore upper roundings, not
exact novelty baselines. Our densities are below both those reconstructed
classical values and the frozen targets. This does not show that no later
work already established them or stronger results.

The published finite-temperature theorem was not invoked or inferred from
the bibliography. Its exact relation to this direct integer-cost argument
was not needed. The proof gives a controlled partition-moment comparison
as an optional observation, with error y log(2)/beta per variable.

## Remaining gap and best next step

No analytic bridge is assumed for the frozen pair: the written proof supplies
the comparison, finite-y estimate, model transfers, and concentration, while
two independently implemented exact calculations supply its numerical premises.
The proof is not kernel-checked or externally refereed. Current literature
novelty and the broader book challenge remain outside this result.

The best next step is independent mathematical review of `notes/PROOF.md`
and its connection to the cited interpolation literature. Optimizing the
trial laws further is secondary to that review. No automatic continuation
or external contact is scheduled.
