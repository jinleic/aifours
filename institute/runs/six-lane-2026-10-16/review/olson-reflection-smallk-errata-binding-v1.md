# Olson small-k errata binding v1 (B0S-r4, MXG-r3)

Parent at 2026-10-18T05:55:34-07:00. Errata binding only. The [small-k verdict](olson-reflection-smallk-parent-verdict-v1.md) (`b71fcaf4…13b8`) continues to rest on the reviewed texts B0S-r3 (`95851b9c3231ec665341145d779ec9eb11da71c5a5ed772f88cb2222595de1ee`) and MXG-r2 (`f2235ed9964e92ca7554678bfae612b7eebb2760eb1b086e487b2e04688aae2f`).

The parent read the full diffs to the worker errata
- [proof-B0S-r4.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-B0S-r4.md) (`d76a179d86692bd59e291b9738c7ab66ca009726fa9cb407372f2e1f3eebb89c`) and
- [proof-MXG-r3.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-MXG-r3.md) (`07baf046ac3e0e1fdb85294b284c76f06a818e7d371c4c1d4355775720cc7f87`).

Each change is labelled with the review finding it answers, and a fix map is appended (B0S §9, MXG §11).

- **Statements:** neither accepted theorem changed scope. B0S now says explicitly that the common rotation letter is ρ_x with x ≠ 0 (Claude B0S MINOR-1). The x = 0 remark is outside the theorem. MXG adds a sentence that its corollary does not give REFL(p), because k ≥ p+1 remains open.
- **Pins:** B0S corrects the printed GRX hash suffix to `…620b1a30`. The full GRX hash is `afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30`; the earlier `…0a30` suffix was a misprint.
- **New justification text** (unreviewed, written at the reviewers' request):
  - the direct derivation of the used H0 instance from GRX;
  - the properness of P = Z ∪ W in Case II;
  - the explicit κ = 1 remark and parity sharpenings in B0S;
  - the no-double-edge sentence in SPLIT, the window-formula range A, B ≤ 2p−1, and the Lemma S hypothesis list in MXG.
  The parent did not independently re-derive these additions. They are recorded as errata deltas, not as newly accepted mathematics.
- **Finite aids** listed in MXG §11 keep their status: not premises.
