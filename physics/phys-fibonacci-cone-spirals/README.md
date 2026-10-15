# Fibonacci spirals on cones

Snapshot: 2026-10-14 (America/Los_Angeles).

Cao Zexian's problem in *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. 541–543, asks whether the consecutive-Fibonacci counter-rotating spiral patterns observed in stressed Ag-core/silica-shell microstructures minimize elastic energy, and whether changing the size of identical disks packed toward a cone apex alternates the pattern's chirality. The source gives experimental motivation but no constitutive energy, boundary conditions, or mathematical definition of the admissible Fibonacci class. Global equilibrium, densest packing, and growth-selected metastable patterns are different questions.

## Verdict

**PARTIAL overall; COUNTEREXAMPLE for the precise fixed-golden-angle packing claim below.**

**FRONTIER_METHOD: DELIVERY-READY for the scoped certificates; NOVELTY-UNCLEAR as a research contribution.** The original elastic-energy question and unrestricted sequential-growth chirality question remain open here, not fully solved. Known commensurate triangular cone crystals and classical phyllotaxis mathematics are the baseline, not discoveries of this project.

### Precise formulations addressed

1. **C1-Finite:** On the intrinsic cone obtained from a sector of angle `pi/3` by identifying its edges (half-angle `asin(1/6)`), constrain 183 centers to slant radii `10 <= r <= 20`. Maximize their minimum geodesic separation. The equal-area golden-angle placement
   `r_i^2 = 100 + 150*i/91`, `theta_i = 2*pi*i*(3-sqrt(5))/2`, `i=0,...,182`, is **not** a maximizer. A triangular-lattice quotient has minimum distance exactly 1; the golden placement has a pair with squared distance strictly below `77/100`. Unit-diameter disks in the former fit in the same frustum `9.5 <= r <= 20.5`. This is an apex-independent, finite certified comparison, not a certificate of the unrestricted optimum.
2. **C1-Bulk:** For `r_n=c*sqrt(n)` and that fixed golden divergence on a cone of sector angle `2*pi*beta`, any packing of equal embedded intrinsic disks centered on every point after any finite initial deletion has asymptotic density at most `pi/(2*sqrt(5))`. At `beta=1/6`, a triangular-lattice quotient, with all centers of slant radius at most 1 omitted, attains the global upper-asymptotic-density optimum `pi/(2*sqrt(3))`. The fixed-golden-angle ansatz therefore loses in the bulk too. The theorem does **not** exclude all deformed configurations whose contact graph happens to have Fibonacci counts.
3. **C2-Reduced:** In a specified local linearized golden-spiral model, the two shortest *Fibonacci-offset* families change consecutively and the handedness of the larger-count family alternates at explicitly derived thresholds. In an achiral energy model, reflection instead makes opposite-handed minima degenerate at every disk size. Neither fact proves size-driven alternation for the book's physical growth process.

## Reproduction

From this folder, run:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/reproduce.py
```

This regenerates a 183-center witness, verifies it with an independent integer-coordinate implementation and rational bounds, then runs separately labeled 80-digit empirical controls. The certificate-only replay is:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py
```

Python 3.13.9 was exercised. The certificate is standard-library-only. Diagnostics use the existing shared `mpmath` installation; its version is recorded in `results/diagnostics.json`. No packages are installed. One core is used; no random search, paid compute, or remote mutation occurs.

## File map

- `source/problem.zh.txt`: unedited supplied source excerpt.
- `source/literature-evidence.json`: short primary-source scope anchors and the matching source-excerpt SHA-256.
- `STATUS.md`: primary-source status, comparable baseline, and unresolved model assumptions.
- `RESULTS.md`: complete arguments, claim/evidence/novelty ledger, actual verification, and independent-review dispositions.
- `code/generate_witness.py`: fixed triangular-lattice orbit construction.
- `code/verify.py`: independent Cartesian-lift verifier, rational golden-pair bound, negative controls, and exact algebra controls.
- `code/diagnostics.py`: independent polar-coordinate and local-branch empirical checks.
- `code/reproduce.py`: one-command reproduction.
- `results/lattice-witness.json`, `results/certificate.json`, `results/diagnostics.json`: small replayable outputs.
- `review/`: hostile-referee prompt, response, and invocation evidence.

The independent Codex referee returned **correct-with-fixes**. Its closed-disk embedding correction, upper-density definition, and empirical sample-reporting clarification were all applied; dispositions are in RESULTS.md. No priority claim or full physical solution was endorsed.

## Research decision

A global basin-hopping search cannot strengthen the existing strict counterexample to the fixed ansatz; finding the unrestricted finite optimum is unnecessary to disprove it. The highest-value next action is to specify the actual Ag/silica elastic functional and growth constraints, then compare a relaxed Fibonacci-contact state against a seam-bearing crystal at the experimental cone angle. Without those assumptions, answering the broader book question from generic Riesz optimization would substitute a different physical problem.

## Approved scoped target: sharp tail density (2026-10-14)

After explicit approval to choose precise subproblems, the proposed continuation was the sharp tail separation of every constant-divergence Fermat spiral, not the physical elastic problem. **Screening verdict: ALREADY-SOLVED mathematical mechanism; Certification of its cone-tail transfer, not a new open-problem solution.** The newly located 2024 packing/Lagrange theorem already gives the density law `pi*mu(alpha)/2`, and the golden limiting distance appears in 2012 phyllotaxis work. See STATUS.md §6 and RESULTS.md §9.

For every fixed `0<beta<=1`, `c>0`, and real divergence `alpha`,
`d_tail^2=2*pi*beta*c^2*liminf_(q->infinity) q*||q*alpha||`.
The supremum of equal-disk densities obtainable by deleting a finite prefix is exactly `pi*mu(alpha)/2`, with value zero for rational `alpha` and for `mu(alpha)=0`. Its maximum over divergences is the known `pi/(2*sqrt(5))`; therefore changing a constant divergence cannot close the triangular-density gap. Supremum is not necessarily attainment: at the golden divergence the endpoint diameter fails on every tail. This screened item no longer occupies an active “still-open” selection slot.

Exact addendum controls (no enlarged convergence table):

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify_tail.py --write
```

They certify the rational Cauchy-equality example, the rational-offset zero-tail control, and sufficient rational rounding bounds for all even golden indices `k>=10`; the universal theorem remains the written proof, with its separate referee report.
