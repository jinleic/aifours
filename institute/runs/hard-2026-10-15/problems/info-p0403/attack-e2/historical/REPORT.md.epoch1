# Balanced nine-variable nonlinearity: bounded research report

**Outcome: partial. The headline existence question remains unresolved.**
No balanced 242 witness or global nonexistence proof was found. All
negative results below have explicitly restricted scope. Novelty is
unknown; none is presented as a new best bound or new construction.

Started 2026-10-15 19:17:11 UTC. Deliverable deadline: 22:41:11 UTC
(minute 204); hard stop: 23:17:11 UTC. Deliverables were finalized at 2026-10-15T20:22:10.541637+00:00, before minute 204.

## Question and baseline

The frozen question asks whether a 512-bit table of weight 256 can have
all Walsh coefficients of magnitude at most 28. Equivalently, it asks
whether balanced nine-variable nonlinearity can exceed 240.

The three staged Kavut–Yücel Section 3 tables were reconstructed from
their printed hex, with f(x) indexed by integers x=0,...,511 and
x_i=(x>>i)&1. Hex is decoded left to right, most significant bit first
within each nibble. Full spectra and SHA-256 hashes of the ASCII bit
strings are in `results/radius2.json`.

| Seed | Weight | W(0) | Forced balancing distance at original origin | Minimum after a linear output shift |
|---|---:|---:|---:|---:|
| dsbf40 | 250 | 12 | 6 | 2 |
| dsbf32 | 250 | 12 | 6 | 2 |
| rsbf56 | 242 | 28 | 14 | 2 |

Each has nonlinearity 242, no Walsh zero, and absolute spectrum histogram
`{4:30,12:46,20:226,28:210}`. Independent direct character sums checked
every coefficient. There are 30 linear shifts at forced distance two
for each seed. Original radii below 6,6,14 are vacuous; the shifted
neighborhoods investigated here are non-vacuous.

The staged 2026 paper's Section 6 explicitly still leaves balanced
attainment of 242 open. Its claimed unrestricted covering radius is not
used as a theorem. The 2024 full text is not staged, so that citation's
baseline could not be independently rechecked here. Only staged research
inputs were used, without network access.

## Verified results

### Elementary bounds and the degree restriction

`degree-bound-proof.md` gives a self-contained argument using integer
Walsh congruences, the minimum weight of a quadratic polynomial, and
Parseval. It proves:

* Every balanced nine-variable function of degree at most seven has
  nonlinearity at most 240, with a degree-two attainer.
* A balanced target reaching 242 must have degree exactly eight and
  nonzero XOR of its support indices.
* The global balanced maximum lies in {240,242}. This is an elementary
  bound, proved without the unrestricted 2026 preprint; it does not
  determine which endpoint is attained.

The attaining quadratic is
`x0+x1*x2+x3*x4+x5*x6+x7*x8`. Its indexed table and complete Walsh
spectrum are in `results/baseline240.json`; the independent direct-sum
checker verifies weight 256 and nonlinearity 240. The written proof,
not that witness check, establishes the universal upper bounds.

### Complete neighborhoods through radius six

No table within Hamming radius six of any staged seed, followed by any
linear output shift, is balanced with nonlinearity at least 242.
Invertible affine changes of input and affine output additions transport
this exclusion. It is a local result, not a global answer.

* Distance two: all 130816 pairs per seed violate the Walsh bound 28.
  The independent checker computes every coefficient for every pair.
* Distance four: all 22238720 triples per seed were examined. Exactly
  195 triples meet the necessary constraints; they yield exactly 45
  bound-preserving four-sets per seed. None creates a Walsh zero.
  A separate NumPy Boolean implementation independently exhausts the
  triples, reconstructs every possible four-set and directly checks all
  surviving spectra.
* Distance six: exact binary-index CNFs require all 512 bounds and some
  Walsh zero. Every gate, lookup row, character parity, cardinality
  clause and strict-order circuit is independently audited. Separate
  Python LRAT/RUP checking verifies an empty-clause derivation for each
  seed. Backward-trimmed proofs were checked again before bulky
  originals were removed.

Odd distances give odd weight and cannot become balanced by adding a
linear function; distance zero has no Walsh zero. Thus these exact even
cases cover the whole stated radius. See `encoding-proof.md` for the
complete reduction and certificate correspondence.

The radius-six auditor's random full-assignment checks are supplemental
controls only. Completeness instead rests on universal gate/lookup/
character/order/cardinality checks plus full proof replay, not sampling.

### Exact maxima in 16-point and 32-point families

The four-flip survivors lie in a 16-point affine four-flat for each
seed. Allowing arbitrary assignments on all sixteen points, followed
by any linear output shift, gives exact balanced maximum 240. Every
one of the 65536 full table variants per seed was independently
transformed in all 512 coordinates; every recorded outcome was compared
against a separate 16-point transform reduction. There are 448 underlying
tables meeting the bound 28; all have Walsh coefficients 4 mod 8 and
therefore no zero.

The following larger class was also checked. Let V be the linear space
with basis:

| Seed | Basis of V | Core affine coset |
|---|---|---|
| dsbf40 | 27,45,195,325 | 5+V |
| dsbf32 | 63,90,139,278 | 30+V |
| rsbf56 | 27,45,195,325 | 5+V |

Allow arbitrary changes on any two of its 32 parallel V-cosets, leaving
all other points fixed, and then add any linear output. Each pair has
32 free input points. The exact balanced maximum of this restricted
union is 240 for each seed.

All 496 coset pairs per seed were covered. Two complete 65536-entry
half-spectrum catalogues and exact bitset intersections cover all
2^32 assignments in every case. The independent auditor reconstructs
the catalogue by direct sums and checks the full character-block
identity and every original inequality. This is complete finite-set
coverage, not sampled checks of the large assignment range.

Each of the 31 pairs containing the core has 448 bound-preserving
assignments; each of the other 465 pairs has only the original seed.
The auditor checks that every bound-preserving table changes only the
core. None has a Walsh zero. Cases overlap; 14353 is the count with
pair multiplicity, not the number of distinct functions in their union.
Explicit balanced 240 attainers are stored and directly verified.
See `two-coset-proof.md` and the `*-two-cosets*.json` files.

These are coordinate subcubes, not invariant symmetry classes. A common
affine conjugate of the nine-cycle would have to fix every independently
free input point, but such a conjugate has only two fixed inputs. Thus
the whole classes are not merely a common rotation-symmetric class in
different coordinates. No claim of novelty follows from this screen.

### Twelve exact quarter-table maxima

Enlarge V to the following seven-dimensional U. The four cosets of U
partition the input space. In each coset separately, all 128 truth-table
values may be changed, the other 384 remain fixed to the seed, and any
linear output shift is allowed.

| Seed | Basis of U | Canonical coset origins |
|---|---|---|
| dsbf40 | 27,45,195,325,1,2,4 | 0,8,64,72 |
| dsbf32 | 63,90,139,278,1,2,4 | 0,8,16,24 |
| rsbf56 | 27,45,195,325,1,2,4 | 0,8,64,72 |

Each of these twelve classes has exact maximum balanced nonlinearity
240. Each exclusion covers all 2^128 assignments by an independently
audited integer-FWHT Boolean circuit and a checked LRAT certificate.
The circuit includes the mathematically justified degree-eight/support-
XOR necessary condition. The auditor exhausts every local full-adder
identity, checks transform wiring, all 512 character rows, outside
sums, all comparator values, every zero choice and all additional
constraints. This is a universal composition audit, not a sample of
the 2^128 assignments.

For each case, a bound-32 planted SAT control and its full model were
checked. Its two changed points create a Walsh zero. After the stated
linear shift, an explicit balanced table attaining 240 is stored with
bit order, SHA-256 and all 512 coefficients in
`*-control-balanced-attainer.json`. Those tables were independently
verified by direct sums. See `quarter-class-proof.md` and
`results/free128-batch.json`.

Changing arbitrary values on multiple quarter domains simultaneously
is not covered. Their partition does not turn these special cases into
a universal exclusion.

## Unsuccessful searches and limitations

* Three binary-index radius-eight variants for dsbf40 ran with 180-second
  caps: all output shifts, the additional necessary degree-eight
  condition, and a fixed original zero origin. All were UNKNOWN.
* A signed-FWHT search with 256 free points stopped at its 120 MiB proof
  size cap, with no decision. This is UNKNOWN, not an exclusion.
* A full-space signed-FWHT search ran for 180 seconds and was UNKNOWN.
  It used support-XOR normalization and a quadratic spectral-bit
  reduction. A planted balanced NL240 control passed, but the extra
  global reduction has not been accepted as an independently audited
  negative result. No claim depends on it.
* Four deterministic balanced-swap searches completed 2900000 total
  steps, with fixed random seeds and different spectral objectives.
  None reached penalty zero. The smallest reported tail penalty is a
  search metric; it is not an improved nonlinearity result. The best
  verified balanced nonlinearity remains the baseline 240.

Detailed progress and final counts are in `logs/` and
`results/heuristic*-summary.json`. Timed-out partial proof traces were
discarded after preserving their hashes, sizes and logs; they are not
certificates. Global and half-table UNKNOWN outcomes prove nothing
about absence of a witness.

Implementation issues were corrected before the accepted checks:
Python 3.9 lacks `int.bit_count`; the Python z3 module is absent although
command-line solvers exist; a planted radius-two control originally
compared pre-existing zeros with newly created zeros and was corrected
to compare the explicitly intended property. Shell here-doc temporary
files, bytecode cache writes, resource-limit hooks and process-status inspection were blocked
by the sandbox; scripts and owned-process wall/file-size caps replaced
those mechanisms. Syntax was checked in memory without creating an
external bytecode cache. The full-space solver retained its own 180-second
limit and its completed UNKNOWN log. No unsupported solver verdict was
turned into a claim.

Observed peak disk use was about 924 MiB, below 1 GB. The full-space
solver reported peak resident memory about 607 MiB. All research
artifacts remain in this directory. No packages were installed, no
network or external contact was used, and no locally compiled binary
is required. Every nonempty claim replay/check/control command starts
with python3 and uses preserved certificates or exact computations.

## Controls and replay

Accepted positive controls include the small relaxed radius-two case,
the fixed six-point bound-32 case, and all twelve planted quarter-class
models. Intentional corruptions of Walsh data, a four-set list, a lookup
literal with an updated checksum, a proof hint, a case count, a circuit
gate, and truth-table entries are rejected by independent checkers.
The negative control commands are supposed to exit nonzero.

`claims.json` is written via `claims.json.tmp` followed by rename.
`code/validate_claims.py` validates all features of the staged schema,
evidence paths and replay command restrictions. `code/final_verify.py`
runs every listed verify, check and negative-control command, recording
the actual exit statuses. Pure mathematical upper bounds are justified
by the written proof; their witness checks verify the lower bounds.

Final command replay: **PASS**. See `results/final-verification.json`.

## Remaining gap and best next step

The global balanced maximum is still either 240 or 242. A positive
answer requires a degree-eight table with weight 256 and all 512 Walsh
magnitudes at most 28; none is provided here. A negative answer requires
a proof covering the full space; none is provided here.

A target must escape the certified affine seed neighborhoods and the
specified coset-supported families. In particular, after any linear
output shift, it must differ from each seed in more than one of that
seed's four certified quarter domains. These restrictions can filter a
future construction or search, but do not cover all degree-eight
functions. The useful next step is a new degree-eight construction or
a substantially stronger full-space search/proof method; the global
and half-table time/size limits here remain inconclusive.
