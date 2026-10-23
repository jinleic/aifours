# T1 result: certified positive coherent information of an explicit 2000-qubit state at p = 1/5

Status: CANDIDATE (computed rigorous enclosure). Pending: Codex hostile review (`codex-review-M2000-p1_5.*`),
parent independent reproduction. Do not cite as accepted until both close.

## Statement (computer-assisted)

Channel `N_p(ρ) = (1−p)ρ + (p/3)(XρX+YρY+ZρZ)` (total-error convention; per-Pauli `p/3`). Let
`a_0, a_1 ∈ R^{301}` be the binary64 vectors in `evidence/cert/witness_g3_M2000_p1_5.json` (`a_0` supported on
`k ≡ 0`, `a_1` on `k ≡ 1 (mod 3)`), `φ_i = Σ_k a_i[k] |D^{2000}_k⟩ / ‖a_i‖` (Dicke states of 2000 qubits) and
`ρ⋆ = ½|φ0⟩⟨φ0| + ½|φ1⟩⟨φ1|`. Then

    1.1288547919e−8  ≤  I_c(ρ⋆, N_{1/5}^{⊗2000})  ≤  1.1436444146e−8      (bits)

and therefore `Q(N_p) ≥ 5.64e−12 > 0` for all `0 ≤ p ≤ 1/5` (monotonicity, PROOFS §0; LSD).

Matched prior art: certified 0.194868 (arXiv:2608.15870v2, exact-rational, M = 45); claimed 0.2029161
(arXiv:2609.39747v2, float Ic ≈ 1e−12 for the M → ∞ Gaussian limit, no finite witness). Delta: +0.005132 over
the certified record; −0.0029 vs the non-rigorous asymptotic claim.

## Dependencies

1. PROOFS.md §1 (sector decomposition; independently re-derived, cross-checked by brute force and by KG's
   certified state R), §2 (Schwinger steps), §3 (double-double error model incl. underflow), §4 (truncation,
   tails), §5 (Ostrowski + Gershgorin entropy enclosures); PROOFS_v2.md A1 (normalization/weights exposition).
2. Imported theorems listed at the top of PROOFS.md.
3. Software: CPython 3.13.9, numpy 2.5.4 (IEEE binary64, no FMA in dd.py), python-flint 0.9.0 (Arb balls).

## Replay

```
cd physics/evidence/six-lane-20261016/depolarizing/evidence/cert/code_snapshot_M2000_p1_5
for r in 1236:1344 1346:1454 1456:1564 1566:1674; do
  OMP_NUM_THREADS=1 ../../../env/bin/python cert.py ../witness_g3_M2000_p1_5.json \
     --out /tmp/replay_${r/:/_}.json --ptail 1e-13 --sectors $r &
done; wait
../../../env/bin/python combine.py ../witness_g3_M2000_p1_5.json /tmp/replay_*.json.sectors.jsonl --ptail 1e-13 --out /tmp/total.json
```
(4 workers, ~30 min on Apple M3 Ultra; peak ~0.7 GB RSS per worker.)

## Controls

- Brute force (2^M dims) M = 4, 6, 7: 15/15 enclosures contain the exact value (`evidence/test_cert_small_v2.log`).
- External: KG's state R (payload SHA-256 9a94606d…) inside both KG certified intervals.
- Independent float64 implementation (`code/finite.py`): 1.1412e−8 at M = 2000, inside the enclosure.
- Same-state sign control: p = 201/1000 negative certificate (run started 20:04 PDT; see LOG.md).
