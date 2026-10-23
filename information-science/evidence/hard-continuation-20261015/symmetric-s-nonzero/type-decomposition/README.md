# Balanced 3-DSBF: exact support-type decomposition checkpoint

**Outcome: all three requested exact branches remain UNKNOWN.** No balanced NL242 witness and no new negative theorem were obtained. This checkpoint closes this computational route for now; it does not exclude any of the three types or any unrestricted balanced function.

The parent fixed-half result and the earlier symmetric-search files/manifests are unchanged. All files of this new assignment are confined to this directory.

## Exact structural question

For nine-bit inputs with `x_i=(x>>i)&1`, the actual generators are rotation left by3 and reversal of all9 coordinates. Their104 input orbits give104 independent Boolean truth values. Applying the actual linear generator matrices to all512 possible support vectors derives

`Fix(R) intersect Fix(J) = {0,146,365,511}`.

The zero-support type is already impossible for a balanced peak<=28 function by the elementary quadratic-residue/Parseval argument recalled in `PROOF.md`; no covering-radius preprint theorem is assumed. Thus every balanced 3-DSBF target belongs to one of the three nonzero branches.

Each branch imposes **all** of:

- exact weight256, not merely even weight;
- its fixed support XOR `s`, not merely `s!=0`;
- `|W_f(a)|<=24` when `a.s=0`, and `<=28` otherwise;
- harmless output-complement normalization `f(0)=0`.

The tightened bands are equivalent to peak<=28 under these conditions, because balance gives `W_f(a)=4(a.s) mod8`. Exactly256 full-spectrum coefficients lie in each band. The frequency-orbit band counts are:

| Type | Orbit cap24 | Orbit cap28 | Exact variables/assertions |
|---|---:|---:|---|
| 146 | 52 | 52 | 104 /219 |
| 365 | 60 | 44 | 104 /219 |
| 511 | 52 | 52 | 104 /219 |

These are genuinely stronger balanced questions than the preceding all-weight/nonzero-XOR circuit. No same-heuristic run was used.

## Single bounded visits: actual outcomes

The three native weighted-pseudo-Boolean questions were each given **one600s visit**, run concurrently with process-local Z3 parallelism disabled and a1100MiB Z3 memory guard per process. No automatic refill or retry was installed.

| Fixed support type | Solver status | Elapsed seconds | Reason | Certified exclusion |
|---|---|---:|---|---|
| 146 | UNKNOWN | 600.489 | timeout | No |
| 365 | UNKNOWN | 600.028 | timeout | No |
| 511 | UNKNOWN | 600.028 | timeout | No |

Thus the target branch counts are **0 positively resolved,3 UNKNOWN,0 unattempted,0 excluded**. Solver-only UNSAT would also require a complete independently checked certificate before counting as an exclusion; none was returned. No candidate truth table triggered a positive witness claim.

Each `results/s<S>-run.json` records the input hashes, actual elapsed time, Z3 version, native status, timeout reason, exact scope and configured guards. The exact source/commands and final replay receipt are in `result.json`.

## Recorded equivalence, without skipping a requested branch

An explicit commuting linear shear exchanges types146 and511:

`M(x)=x XOR (365 if parity(x&146) else0)`.

It is an involution commuting with both actual group generators. Its transpose maps frequencies by

`M^T(a)=a XOR (146 if parity(a&365) else0)`.

For `g=f composed with M`, support changes by `s(g)=M s(f)` and the Walsh spectrum is permuted by `W_g(a)=W_f(M^T a)`. It preserves balance, normalization and the24/28 bands. The exact104-variable and104-frequency permutations, all10816 character-matrix correspondences, and a full512-bit transported control are recorded in `inputs/type-equivalence.json`.

The independent checker constructs the matrix differently, checks all262144 character pairings, and maps the **actual parsed SMT** Walsh constraints, balance equality, support equations and normalization between branches. This gives the recorded groups `{146,511}` and `{365}`; it is not a proof that365 is inequivalent under every possible transformation. All three requested solver visits were retained, so this observation does not hide an unattempted branch or justify another retry. Equivalence is not an exclusion or a novelty claim.

## Genuine positive and discriminating controls

An exact finite balance/support DP constructs real invariant balanced models by changing six input points, in whole orbits, of the published `dsbf40` table, followed when needed by global output complementation. It does not optimize nonlinearity or stand in for the target search.

| Control support type | Weight | Degree | Direct Walsh peak | Exact relaxed bands: even/odd `a.s` |
|---|---:|---:|---:|---|
| 146 | 256 | 8 | 36 | 32 /36 |
| 365 | 256 | 8 | 40 | 40 /36 |
| 511 | 256 | 8 | 40 | 40 /36 |

All219 assertions of each corresponding relaxed SMT question are evaluated on its true104 orbit values. The target questions reject these models only at Walsh inequalities; their balance, fixed type and normalization pass. Their full indexed tables and spectra are retained. Transporting the type146 model through the shear supplies an additional balanced type511 model with peak36; it is stored separately, and the original type511 control remains unchanged.

Wrong-type checks explicitly evaluate each planted model against the other support equations: the number of failed coordinate equations equals the bit weight of the difference of the support vectors. This checks the fixed-type condition specifically, without pretending all the other branch's Walsh caps pass.

Deliberate corruptions change a nonzero-frequency PB weight, a support-type bit, the exact-balance value or a recorded spectral coefficient. Each must be rejected for its specific assertion—not for a missing file. These controls are part of the single final evidence pass.

## Independent question-to-encoding correspondence

`PROOF.md` gives the complete derivation. The independent `code/check.py` imports no producer code or Z3 library. It:

1. reconstructs the group orbits and support fixed space from the actual matrices;
2. reconstructs all512 character rows directly;
3. parses every actual SMT declaration and assertion with its own S-expression parser;
4. expands every weighted literal into a signed linear form and compares it to the direct Walsh coefficients and24/28 cap;
5. checks exact weight256, all9 fixed-support equations, normalization, and absence of extra assertions;
6. checks the planted and any returned positive tables by both512 direct character sums and a separate FWHT;
7. verifies the recorded shear and actual branch-assertion isomorphism.

It therefore does not rely on solvers merely agreeing on one CNF. However, a checked question plus an UNKNOWN solver is still not an infeasibility certificate.

## Replay, pins and portable handoff

From this directory, Python3.10+ standard library suffices:

```sh
python3 code/check.py
```

Expected-to-fail corruptions:

```sh
python3 code/check.py --corrupt-encoding
python3 code/check.py --corrupt-type
python3 code/check.py --corrupt-balance
python3 code/check.py --corrupt-spectrum
```

`code/final_verify.py` runs the final independent pass and records actual return codes, expected assertions, elapsed times and hashes in `result.json`. `results/check.json` contains the detailed audit. The machine-readable seed bundle is `seed-bundle.json.gz`.

The pinned byte-for-byte imported orbit/seed data is `inputs/orbits.json.gz`:

`SHA-256 441e85e5289c34a15bc0caf5387cae77d9039da3a47efdbde9d429d5f7c91cbb`.

All bit tables are indexed `bits[x]=f(x)` for `x=0,...,511`; no implicit permutation is used. The exact matrices, input orbit lists, target/control metadata and actual compressed SMT files are staged. `handoff/` contains only the new load-bearing sources/proof/inputs/receipts with a hash manifest, not old snapshots or an automatic scheduler. Z3 is needed only to repeat the now-stopped exact visits, not for replay. All original and new evidence is preserved; no prior files/manifests are overwritten.

## FRONTIER decision

**STOP-THIS-ROUTE / NEW-MATHEMATICS-REQUIRED.** All three structural visits have reached their single reasonable checkpoint and remain unresolved. The recorded146/511 isomorphism removes no uncertainty and is already part of this checkpoint, not a reason to rerun it. Do not repeat these questions with another seed, identical heuristic or merely a longer timeout.

The precise remaining obligation is a balanced peak<=28 3-DSBF witness, or complete independently checkable exclusion certificates for the support-type questions (one could transport a certificate between the two proved-equivalent types). Such a certificate would still concern only the balanced3-DSBF subclass, not global absence. A further authorized continuation must bring genuinely new mathematics or a materially different proof-producing representation. The book problem remains open.
