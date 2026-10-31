# Four-word, two-syndrome counterexample

This is an additive simplification of `frontier-20261028-syndrome-information-counterexample-v1.md` (SHA-256 `e83e762385db49e07737346ac3142ab16a0f410c08e8e4435aa1b27a4a04e70f`). **WRITTEN with exact finite checks; no guessing-number gain is claimed.**

Use the same triangle occurrence order and `q=8` embedding `(bit,0,0)` at every original R-minus vertex. Give equal probability to the four 10-bit words (vertex `v` is bit `v-1`)

```
649  759  697  711
```

Their triangle-parity syndromes are respectively `51,51,53,53`. All six word pairs satisfy all ten original-neighbour FD conditions, so the law has valid full-domain decoders. The syndrome `S` is a fair bit, with `H(S)=1`. For each vertex, the number of 1 bits among the two words with syndrome 51 equals the number among the two words with syndrome 53: these paired counts are `(2,2)` at vertices 1,8,10, `(1,1)` at vertices 2–7, and `(0,0)` at vertex 9. Therefore every `X_v` is independent of `S`, and

\[
H(S)=1,\qquad \sum_v I(X_v;S)=0.
\]

Thus the proposed shortcut `2 sum_v I(X_v;S) >= 3H(S)` fails **even when the syndrome is supported on only two cosets**, and maximally so on this example. The full mixed-syndrome entropy-gap identity retains its nonnegative conditional term and is not contradicted. This law has only four equiprobable support words and gives no improvement of `20/3`.

Checker `frontier-20261028-four-word-syndrome-witness.py` SHA-256 `337482fb74654a9fb9df414f27fc0f906ab8755314aefa45182cff562fa5d262`; receipt SHA-256 `2edca8c5687037e8bb94c140cc0147a79ba1389146f819731c2ca1f0d42c8ed4`. It checks 60 vertex/pair conditions and all stated syndrome-conditioned counts with integer arithmetic. The group-parity cover is pinned in the predecessor packet. No formal proof, cross-model review or novelty clearance was performed.
