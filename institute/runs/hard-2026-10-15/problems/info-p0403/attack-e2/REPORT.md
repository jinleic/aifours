# Balanced nine-variable nonlinearity: bounded continuation

**Outcome: partial. The headline question is unresolved.** No balanced
NL242 witness or global nonexistence proof was found. The verified
results below have restricted scope. Novelty is unknown.

Started 2026-10-15 21:23:54 UTC. Deliverables due by 23:44:54 UTC
(minute 141); hard stop 2026-10-16 00:09:54 UTC (minute 166).
Updated: 2026-10-15T22:11:33.208310+00:00.

## Contract and baseline recheck

The target remains a 512-bit table of weight 256 with every Walsh
magnitude <=28. All tables use x=0,...,511 and x_i=(x>>i)&1. Printed hex
is decoded left to right, MSB first within each nibble. Indexed bits,
ASCII-bit SHA-256 hashes, and complete spectra are stored for attainers.

The delivered 2026 manuscript, Section 6, explicitly leaves balanced
attainment of 242 open. The 2024 full text is not staged, so that
reported citation cannot be independently rechecked here. The supplied
Section 3.1 and Section 4 tables were reconstructed from the delivered
Kavut--Yucel text and directly checked. No claimed unrestricted upper
bound from an unrefereed preprint is assumed. No online literature or
novelty search was possible.

## What was recovered and what was withdrawn

The old report and claims are in `historical/` as data. The recovery
archive and all 77 members were hash-checked before 64 missing files
were restored; see `results/recovery-audit.json`. The literature excerpt,
radius-two/four files, flat outcomes, and two-coset results are now
inside the delivery.

The three old radius-six LRAT proofs are unavailable and are not used.
A new exact hypergraph enumeration replaces that claim. Eleven old
quarter-class proofs remain unavailable; the twelve-class assertion and
the corresponding restrictions on all four quarter domains are
withdrawn. Exactly one preserved 128-point class and a recovered
64-point class are retained with their full certificates. No missing
artifact, old producer-written audit, timeout, or solver-only verdict
supports a current negative claim.

## Self-contained elementary bounds

`degree-bound-proof.md` proves that the global balanced maximum is
either 240 or 242, without the unrestricted covering-radius preprint.
The proof uses a quadratic residue of W/8 when support XOR is zero and
a separate W/4 parity argument when support XOR is nonzero. The latter
case is essential for the global upper bound.

The exact maximum among balanced degree-at-most-seven functions is 240.
The explicit quadratic x0+x1*x2+x3*x4+x5*x6+x7*x8 attains it and passes
both FWHT and direct-character checks. Any target must have degree
exactly eight and nonzero support XOR. The stronger negative control
keeps the balanced truth table and its hash intact but corrupts one
recorded Walsh coefficient; the checker must reject the spectrum.

## Complete neighborhoods around five inequivalent explicit seeds

| Seed | Weight | W(0) | Original forced balancing distance | Minimum over linear shifts | Absolute autocorrelation indicator |
|---|---:|---:|---:|---:|---:|
| dsbf40 | 250 | 12 | 6 | 2 | 40 |
| dsbf32 | 250 | 12 | 6 | 2 | 32 |
| rsbf56 | 242 | 28 | 14 | 2 | 56 |
| perm104-ac48 | 270 | -28 | 14 | 2 | 48 |
| perm74-ac64 | 246 | 20 | 10 | 2 | 64 |

All have NL242 and no Walsh zero. Distinct autocorrelation indicators
prove that the five tables are pairwise not extended-affine equivalent;
identical absolute Walsh histograms of the first three do not imply
equivalence. The extra tables are defined in `code/extra_seeds.py`.

For every seed, no modification within distance six followed by any
linear output addition is a balanced target. This all-shifts scope is
non-vacuous, even when a small ball at the original origin is vacuous.
Adding a linear output balances exactly when some Walsh coefficient is
zero, while preserving nonlinearity.

All 130816 pairs and all 22238720 triples per seed were independently
exhausted. No pair preserves bound 28. The original three seeds have
195 radius-four admissible triples and 45 legal fours each, none with
a zero; the extra two have none. The distance-two count is computed,
not hard-coded.

The radius-six hypergraph method enumerates every admissible nonzero-
XOR four anchor, then every five- and six-extension. Every six-set has
such an anchor, so this is complete. The independent implementation
reconstructs direct Walsh characters, reverses coefficient order, uses
different lookup blocks, and extends anchors by pairs instead of the
producer's five-set extension. It directly checks all 512 coefficients
of every resulting six-set.

| Seed group | Saturated-constraint six-candidates per seed | Preserving all 512 bounds | With a Walsh zero |
|---|---:|---:|---:|
| original three | 195 | 120 | 0 |
| extra two | 0 | 0 | 0 |

The small planted six-flip control exhausts all 924 sets on twelve
points at relaxed bound 44 and includes a known balanced NL240 return.
Its initial assumed bound 40 was falsified and corrected to the directly
computed 44 before acceptance. The broken-result control removes a
legal six-set and must fail. See `radius-six-proof.md`,
`seed-and-local-proof.md`, and `extra-seed-proof.md`.

## Exact maxima in specified free coordinate domains

For the original three seeds, arbitrary assignments on the specified
16-point affine four-flat, followed by every linear output addition,
have exact balanced maximum 240. All 65536 assignments per seed were
independently transformed in all 512 coordinates and compared with the
producer's 16-point reduction. Each has 448 bound-preserving tables,
none with a Walsh zero. Outcome binaries and explicit attainers are
included.

For V=span(27,45,195,325) for dsbf40/rsbf56 and
V=span(63,90,139,278) for dsbf32, allow arbitrary assignments on any two
distinct V-cosets. Every one of the 496 pairs per seed is covered by
complete 65536-entry half catalogues and exact bitset intersections of
all 2^32 assignments. An independent audit checks all character-block
identities and every original inequality. The exact balanced maximum
is 240. The count 14353 has pair multiplicity; these overlapping cases
are not distinct-function counts. See `two-coset-proof.md`.

Exactly two larger classes have preserved, independently replayed LRAT
empty-clause certificates and universal encoding audits:

| Seed | Arbitrarily free domain | Free bits | Exact balanced maximum |
|---|---|---:|---:|
| dsbf40 | 5+span(27,45,195,325,1,2) | 64 | 240 |
| dsbf32 | span(63,90,139,278,1,2,4) | 128 | 240 |

All linear output additions are included. Bound-32 planted SAT models
and class-member attainers are checked by direct sums. CNFs and
encoding metadata are losslessly compressed; the 64-point CNF was
regenerated with exactly its preserved proof's original hash. No
sampling is used to establish the circuit correspondence. See
`compact-flat-proof.md`. Other quarter domains remain unproved.

These are coordinate domains with independent free values, not common
rotation-invariant classes. An affine conjugate of the nine-cycle shift
has two fixed inputs and cannot fix 16, 32, 64, or 128 independently
variable inputs pointwise. This screen does not assert novelty.

## A Parseval screen for fixed eight-variable halves

For an odd-weight fixed slice g with spectrum G, any completion h whose
full nine-variable table has all magnitudes <=28 and a Walsh zero must
satisfy

    max|G| <= 26,
    ||G||_1 <= 3570 + max{|G(b)|: |G(b)|<=14}.

The proof uses |G|+|H|<=28, Parseval on H, and the index at which
H=+G or -G. It is given fully in `slice-reduction-proof.md`. A failed
screen excludes every completion and all balancing output shifts; a
passed screen supplies no completion.

All 31744 listed (source,normal) pairs from 124 explicit balanced NL240
sources were independently checked, each with all 256 slice character
sums. The producer instead averages pairs of full nine-variable Walsh
coefficients. Exactly 31492 classes fail a necessary condition and
therefore have exact balanced maximum 240, attained by their source.
Each has 256 freely assigned points. The other 252 classes are
unresolved by the screen. These families overlap and are not claimed
affine-inequivalent. All 31492 exclusions in this corpus fail the simpler
max|G|<=26 condition: their slice maximum is 30. The Parseval l1 bound
adds no exclusions here. The 252 survivors have slice maximum 26.
The independent check also tests a bound-32
planted solvable variant in every listed class. Full indexed sources,
hashes, spectra and case definitions are in `results/slice-screen.json.gz`.

## Searches that do not establish exclusions

A deterministic seeded balanced-swap search completed 600000 steps
(seed 20261016, objective scale 100000) in 241.93 seconds. Its best
verified table is balanced NL240, max|W|=32, tail penalty 21. This is
not an improved construction; non-find supplies no negative theorem.

An exact-six SAT run with the degree-eight necessary condition hit a
24 MiB proof cap and returned UNKNOWN. Three 256-free-point completion
instances passing the slice screen hit 16 MiB proof caps in about
6.5 seconds each and also returned UNKNOWN. Partial traces were hashed
and discarded. Those audits and logs do not certify infeasibility.

Four audited surviving-half instances were then searched without proof
output, each with a 600-second cap. A solver-only UNSAT status is
explicitly uncertified; a SAT model would require a balanced full table
checked independently by FWHT and direct sums.

| Completion trial | Current status | Seconds |
|---|---|---:|
| 0 | UNKNOWN | 600.14 |
| 1 | UNKNOWN | 600.04 |
| 2 | UNKNOWN | 600.12 |
| 3 | UNKNOWN | 600.07 |

Two further 180-second variants add the exact odd-slice residue identity
H/2 mod4=-wt(h)+2*a.supportXOR, after normalizing wt(h)=1 mod4 by
complementing the free slice. Such complementation swaps the two full
Walsh halves and preserves bounds and zeros. Every added XOR gate's
truth table and all 256 residue identities of a known bound-32 source
completion were checked. These experimental controls are not an
accepted negative certificate.

| Low-bit variant | Status | Seconds |
|---|---|---:|
| 0 | UNKNOWN | 180.14 |
| 3 | UNKNOWN | 180.15 |

The historical epoch-1 searches and claims are preserved as data and are
not counted as fresh evidence. No experimental full-space timeout is a
global nonexistence proof.

## Packaging, controls, and replay

Every load-bearing artifact is inside this directory and the delivery
caps. No large radius-six LRAT file is required. Preserved CNFs and
metadata are losslessly gzip-compressed; proof files are below 5 MB.
Only the twelve unclaimed UNKNOWN completion CNF/metadata caches were
removed after retaining hashes, source tables, logs and deterministic
regeneration commands in `results/inconclusive-artifact-recipes.json`.
No file cited by `claims.json` was removed. Accepted target CNFs and
proofs remain fully delivered.
All claimed commands start with python3 and require no locally built
executable. No package installation, network, external contact,
delegation, credential access, or git commit was used. Production used
at most four solver/compute threads; all numerical claims use integers.

Claims are rewritten through `claims.json.tmp` followed by rename.
`code/validate_claims.py` checks the staged schema and evidence paths.
Independent check paths import no producing code. Planted controls,
corrupt spectra, altered outcomes, removed legal sets, wrong case
counts, and broken circuit clauses test the checks. Intentional negative
controls must fail for the intended assertion, not for a missing file.

Limited-copy replay: **PASS**. 25 commands, 525.18 aggregate seconds; all successful commands and all deliberately failing controls are recorded in `results/delivery-replay.json`.

## Exact remaining gap and best next step

The global balanced maximum is still either 240 or 242. A resolution
requires a balanced 512-bit table with every Walsh magnitude <=28, or
a complete exclusion of all balanced degree-eight functions. Neither is
provided. A special-case maximum or finite neighborhood exclusion does
not resolve the book question, and no general odd-n claim is made.

The 252 explicit half-classes passing the analytic screen are a concrete
next search input. Better spectral completion methods could enforce
|H(b)|<=28-|G(b)| directly while seeking inverse-transform signs and a
zero. The completed circuit searches should be used only for their
actual certified outcomes. A global proof still needs an argument
beyond these fixed halves and local seed neighborhoods; the unsupported
old assertion about all quarter domains must not be used.
