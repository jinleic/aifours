# Handoff: phys-p0422 continuation bundle (hash-pinned, compact)

This is the load-bearing subset of `physics/evidence/hard-continuation-20261015/`, copied unchanged.
Every file's sha256 is in `MANIFEST.sha256`. The full research record, including scratch, exploration
logs and the MMZ PDF, stays in the parent directory. `formal/` belongs to a separate lane and is not
included here.

## Claim

For k = 4, alpha >= 3973/400 = 9.9325, and for k = 5, alpha >= 8447/400 = 21.1175: a random k-CNF on n
variables with floor(alpha n) independent clauses, each on k distinct uniform variables with fair
signs, is unsatisfiable with probability tending to 1. The exact rates and cutoffs are in
`certificates/constants.json`.

Status levels:
* certificate: rigorous outward-rounded enclosures by two package implementations, which agree to 20
  decimals; the parent checker passes; and
* full proof: the written analytic bridge `notes/PROOF.md`. It is not formally verified or peer reviewed; and
* formalized subset: none in this bundle.

No new method is claimed (Franz–Leone, Lelarge–Oulamara, Vorobyev, Achlioptas–Menchaca-Méndez). The only
possible novelty is the explicit constants, and priority is unresolved.

## Input pins

* `certificates/trials.json`: sha256 `1cdc03c232078cac29906c0156bfdf7658b40fbe80fe1d0577dbcfc87000913e`.
  This equals the `input_sha256` in the parent receipt
  `institute/review/continuation-20261015/sat-independent-improved-bounds.json`, which has sha256
  `8509a0ecac8e62284a318a76fed61d56fe1941f4e04d3f14c5f250a07373d281`. The parent checker
  `sat_independent_certificate.py` has sha256 `2bf5c8525f852aeb435dab82416b2ab90840b2b8d710ffab3473ac87dc72b1f3`.
* The epoch-2 checkers are used read-only from
  `institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2/code/`: `certify.py` sha256
  `173708e7…f2477` and `independent_check.py` sha256 `81f53814…0b4`.
* Python 3.14.3, standard library only, for the certifiers, constants, finite audit and replay.
  numpy and mpmath are needed only for `code/control_lowdensity.py` and `code/explore_moments.py`.

## Commands (run from this directory)

    python3 code/certify_a.py --trials certificates/trials.json        # exit 0; ~1.3 s
    python3 code/certify_b.py --trials certificates/trials.json        # exit 0; ~27 s
    python3 code/transfer_constants.py                                 # exit 0
    python3 code/finite_audit.py                                       # exit 0; ~22 s
    python3 code/finite_audit.py --break-comparison                    # exit 1 (mutation control)
    python3 code/replay.py --with-epoch2                               # exit 0; ~7 min; writes logs/replay.json
    python3 code/control_lowdensity.py --T 256 --starts 3 --cases k5,k4,k2 --out controls/lowdensity-rerun.json   # exit 0; ~5.5 min

`replay.py` checks every expectation: headline certificates, A/B agreement, the k = 2 and k = 3 reference
rows, eight same-law negative controls with rigorous positive lower bounds, five tamper controls, the transfer
constants, the finite audit with its mutation, and the epoch-2 checkers on the T = 128 rows. The
recorded run is in `logs/replay.json` (41 commands, all expectations met, 413.7 s). A byte copy of this
bundle, replayed in `../scratch/handoff-replay-copy/`, also met all 41 expectations in 412.0 s.

## FRONTIER

PROOF-OBLIGATION. The numerical certificates sit within ~1e-4 (k = 4) and ~2.4e-4 (k = 5) of this
functional's numerically estimated floor (9.932389, 21.117262). The next claim-changing work is formal
or human verification of the analytic bridge and priority closure, not further law tuning.
