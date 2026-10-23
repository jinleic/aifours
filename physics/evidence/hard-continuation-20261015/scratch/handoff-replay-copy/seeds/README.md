# Seed bundle for a possible engine requeue (exploration data, not certificates)

* `exploration-laws.json`: optimized m-atom warning laws (floats) for k = 4, 5 at T = 128, 256, 512 and 1024,
  with the density where each optimized law's `Psi_T` crosses zero. Use these as warm starts.
* `popdyn-quantised-laws.json`: 64-atom quantizations of SP (energetic 1RSB, y = ∞)
  population-dynamics fixed points at k = 4 (alpha = 9.9324) and k = 5 (alpha = 21.12), with their
  `T = 256` crossings. The raw populations are in `../scratch/pop_*.npy`, and their sha256 hashes are
  recorded in the JSON.
* The certified rational laws are `../certificates/trials.json` (sha256 `1cdc03c2…0913e`). Do not edit
  that file: the parent's independent receipt pins its hash.

To continue numerically (not recommended as a claim-changing step, because the certified constants are
within ~1e-4 of this functional's floor):

    python3 code/explore_search.py --k 4 --T 1024 --alpha 9.93239 --init <json with rates/weights> --out <out.json>
    python3 code/explore_popdyn.py --k 5 --alpha 21.1173 --pop 200000 --sweeps 150 --out <pop.npy>

Round any candidate to rationals with an exact mass sum of 1. Certify it with `code/certify_a.py` and
`code/certify_b.py`, and run the same-law controls before promoting it. Do not certify at or below the
cavity tripwires 9.931 or 21.117 without independently ruling out a bug.

Natural extensions, all untested: other k (6, 7) with the same tools, provided the cavity values
of Mertens–Mézard–Zecchina remain tripwires; certifying closer to the floor, which gains at most
about 1.1e-4 for k = 4 and 2.4e-4 for k = 5; and moving to T = 1024, which shifts the floor by only
about 1e-6. None of these changes the frontier. The frontier is the formal or peer verification of the
analytic bridge.
