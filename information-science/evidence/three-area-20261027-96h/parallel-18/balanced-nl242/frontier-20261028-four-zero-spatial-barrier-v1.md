# info-6 frontier: a placed four-zero spectrum satisfying selected spatial filters

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:35:44-0700 PDT**. This is an explicit **formal signed spectrum**, not an actual Boolean function or code and not an NL242 witness. The exact finite checks have not received a disjoint review.

## A stronger specified relaxation remains feasible

Starting with the exact four-zero count vector in `frontier-20261028-four-zero-enumerator-barrier-v1.md`, SHA-256 `6adfa5ecdc131f8ce45ac370e87d36722def54176a35e22b8743a8f150ec2229`, 41 LF, the attached receipt explicitly assigns all 512 signed scaled Walsh values k(a) to frequencies in F₂⁹, taking T=e₈. It satisfies the earlier moments, peak≤28, 129 formal peaks, all 257 nonnegative integral dual coefficients, and the following **selected** spatial constraints:

- Its four zero frequencies form the linear 2-plane `{0,1,2,3}`, and its four |k|=4 frequencies form the affine 2-plane `{4,5,6,7}`. Thus both frequency sets have XOR zero.
- On the odd half `a=e₈+x`, x∈F₂⁸, the signs obey `k(a)≡1+2Q(x) (mod 4)` for the actual quadratic `Q=x₀x₁+x₂x₃+x₄x₅+x₆x₇`. On the even half, all k are even; on the odd half, all k are odd.
- The indicator P of `|k|∈{1,7}` on that odd half has algebraic degree four and even sum on every affine 5-flat. An independently written RREF enumeration checked **all 777,240** such flats (97,155 linear directions, eight cosets apiece). The prescribed counts are |P|=150, |Q|=120 and |P∩Q|=80.

The parity assertion on 5-flats implies degree **at most four**, not degree two: it is the vanishing of the fifth additive derivative. A nearby exploratory file had temporarily imposed degree-two weight restrictions on P and P+Q as optional extra hypotheses; those restrictions are **not necessary conditions**. The explicit correction is pinned below. Q, separately, really is quadratic. No invalid degree-two condition was used in this construction.

These checks do **not** establish every adopted affine-energy, multiscale, sign, exchange, or other necessary condition; their purpose is only to exhibit coexistence of the expressly listed filters. The formal k is very far from a Boolean inverse: the independent direct 512×512 inverse transform has **493** entries with magnitude other than 128, and all 511 nonzero-shift spectral autocorrelations are nonzero. In particular, this specific k cannot be W_f/4 for any Boolean f. The finder writes a truth-table candidate if an exact inverse ever occurs, but none was produced here.

## Pinned evidence

All paths are in this directory; hashes are of actual bytes. The flat checker additionally verifies the sign formula, counts, moment values and a parity-breaking mutation.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-four-zero-spatial-placement.py` | `12a97d4c78aa92eaaba4396beb55bc141433f37716684fe4917683b2f5207251` | 107 |
| `frontier-20261028-four-zero-spatial-placement-result.json` | `9e7c777f5478a124c122323c875de94f6d7a3ee5fbdc9fb4077840c031bf3f39` | 545 |
| `frontier-20261028-four-zero-spatial-check.py` | `5f1cce96f1b87acf46d646a9438747a893f8d9cb3f51e9b78f489379b308972c` | 70 |
| `frontier-20261028-four-zero-spatial-check-result.json` | `99d3f8002794eb56e1ea65f1fdac418a817e671201a0c3696442b56859e48538` | 14 |
| `frontier-20261028-quadratic-scope-correction-v1.json` | `adf59cd97bd7f4f2404b42ffc9c8684d8cf59b9d6cfe07864c4c05707c906b26` | 7 |

The original actual balanced witness-or-unrestricted-exclusion gap remains. **END.**
