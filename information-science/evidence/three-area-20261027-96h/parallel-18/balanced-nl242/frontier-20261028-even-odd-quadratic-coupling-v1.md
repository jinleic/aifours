# info-6 frontier: coupled quadratic ranks on the two Walsh half-spaces

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T18:46:16-0700 PDT**. This is an **UNREVIEWED AUTHOR CANDIDATE**; the executable placement below is a formal non-witness. No unrestricted exclusion, realization or novelty claim is made.

## Necessary two-half count constraint

For any balanced f:F₂⁹→{0,1} with `max|W_f|≤28`, let `k=W_f/4`, let T be the XOR of the one-support, and K=T^⊥. As proved in `frontier-20261028-even-half-four-zero-obstruction-v1.md`, SHA-256 `7344078fb115eb47f9d5e3c731a63d16567cb09d23af4868810c5d45ef38f8c4`, 59 LF, T≠0 and `q(x)=k(x)/2 mod 2` is quadratic on the eight-dimensional K. Choose any a₀∉K and define `Q(x)=(k(a₀+x)−1)/2 mod 2` on K. Write

    z = #{x∈K:q(x)=0} = #{a:W(a)=0} + #{a:|W(a)|=16},
    w = #{x∈K:Q(x)=1}.

Then q and Q have the **same alternating polar form**. Therefore their weights must obey this table; it is a necessary condition, not a sufficiency claim:

| z | Allowed w |
|---:|---|
| 64 or 192 | 64, 128, 192 |
| 96 or 160 | 96, 128, 160 |
| 112 or 144 | 112, 128, 144 |
| 120 or 136 | 120, 136 |
| 128 | 0, 64, 96, 112, 128, 144, 160, 192, 256 |
| 256 | 0, 128, 256 |

In particular, a four-zero target can have `#{|W|=16}` only in `{60,92,108,116,124,132,140,156,188,252}`, before considering the w restriction. This refines, rather than replaces, the ≥60 bound. Neither bound excludes every four-zero target.

## Proof

The exact mod-4 Boolean caller gives vanishing third additive differences of k. For u,v∈K, the difference between the polar numerator for Q and that for q is

    Δₐ₀ Δᵤ Δᵥ k(0) ≡ 0 (mod 4).

Each polar numerator is even, so division by two modulo two gives identical polars. Equivalently, Q+q is affine on K. This uses all coordinates of one actual spectrum and does not assert that arbitrary matched marginal counts are realizable.

For a quadratic Boolean polynomial on eight variables, its alternating polar form has even rank 2r. An elementary symplectic change of basis expresses its quadratic part as `Σ_{i=1}^r x_i y_i`, with an arbitrary linear term on those coordinates and on the `8−2r` radical coordinates. Summing `(−1)^q` over radical coordinates gives zero if their linear term is nonzero; otherwise each pair contributes ±2 and the sum has magnitude `2^(8−r)`. In full rank 8 there is no radical, so the sum cannot be zero. Thus a quadratic of rank 2,4,6,8 has zero/one weights `128±64`, `128±32`, `128±16`, or `128±8`, respectively, with 128 also possible when the radical is nontrivial. Rank zero gives weights 0,128,256. Since q(0)=0, z cannot be zero. Combining the possibilities at the **same** polar rank gives precisely the displayed table; z=128 can come from ranks 0,2,4,6, and z=256 only from rank zero. ∎

## Explicit barrier beyond these conditions

A different four-zero histogram satisfying the new table exists as a **formal count model**: z=144, F=140, w=144, and 200 peak-28 coefficients. All 257 dual coefficients are nonnegative integers, with D₂₅₄=47 and D₂₅₅=1; a separate recurrence implementation checked the forward and inverse Krawtchouk transforms. The histogram is not a code or Boolean witness.

An explicit assignment of this model to all 512 frequencies goes further. On K=F₂⁸ choose

    q(x)=x₀x₁+x₂x₃+x₄x₅,       Q(x)=q(x)+1,

so q has 144 zeros and Q has 144 ones, with common polar rank six. The four Walsh-zero positions are `{0,64,128,192}`; the other 140 q-zero positions have |k|=4. The odd-half `|k|∈{1,7}` indicator is the complement of an affine 5-flat, so has degree three. The assignment obeys the **global** `k(a)≡2q(a mod 256)+3(a>>8) (mod 4)` identity, not merely odd-half sign parity; both zero and |k|=4 frequency sets have XOR zero. An independent checker also enumerated all 777,240 affine 5-flats for the indicator's parity.

This explicit k nevertheless fails the actual Boolean caller: **507** inverse-transform entries are not ±128, and **508** nonzero-shift autocorrelations are nonzero. Other adopted energy, multiscale and exchange constraints were not all checked. Hence it only demonstrates coexistence of the explicitly listed conditions, and does not refute the preceding theorem or solve the original target.

## Finite controls and pins

The separate coupled-rank checker exhausted 32,768 pairs of quadratics/affine shifts in dimension four and 2,097,152 such pairs in dimension five, checked even polar ranks and the weight formula, and checked the explicit eight-variable (z,w)=(144,144) pair. These controls do not substitute for the written rank proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-coupled-rank-check.py` | `896c671efff4daa1619e34af0cf76fe9f87870fce42997065d4af6fa4fc93638` | 65 |
| `frontier-20261028-coupled-rank-check-result.json` | `3144798ce9e418b80207fb350c3dde22c27b2b5ba7ac432d1724820595ef95c9` | 24 |
| `frontier-20261028-four-zero-coupled-rank.py` | `fc8dafd7b23957e083adb0d66e19313bab266ec8ce6fc0419408cced2f476c52` | 54 |
| `frontier-20261028-four-zero-coupled-rank-result.json` | `0a4ebd458300628a6962b6038b91172ddf5aa27dbc2c2075a9702b165bc07406` | 285 |
| `frontier-20261028-four-zero-coupled-rank-check.json` | `73fcfde99c24cf918cab236dde8d1b3d2947482e8a847d7e778428339de7bb4a` | 19 |
| `frontier-20261028-four-zero-coupled-placement.py` | `026a275ce11a15a678ac966451e58cf2672c120922e6081c659d116b81adcab8` | 64 |
| `frontier-20261028-four-zero-coupled-placement-result.json` | `ba99cc035f8cc8bbbcb9edfc99d9068263e93bdb93dfa9e368b2219f1e223c0f` | 674 |
| `frontier-20261028-four-zero-coupled-check.py` | `f7acda3d956e0da966dbc99ae133bcf77bf1e72100b7920bbd2b40dc396a35b2` | 75 |
| `frontier-20261028-four-zero-coupled-check-result.json` | `f8dbfd120196adbf7a97cf930fa43e972c7edbdd245b87f0052e7206386eef4a` | 18 |

The four-zero actual-function problem, and the original witness-or-unrestricted-exclusion gap, remain open in this work. **END.**
