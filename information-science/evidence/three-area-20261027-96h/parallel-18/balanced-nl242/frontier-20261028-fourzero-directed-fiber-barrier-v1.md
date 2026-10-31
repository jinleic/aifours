# info-6 frontier: all three surviving radical-phase types pass a coarse directed-fiber relaxation

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T21:25:38-0700 PDT**. This is a finite **formal multiset** result, not a labeled Walsh spectrum, a Boolean code/function, an actual witness, or a novelty claim. It is unreviewed; the written predecessor `frontier-20261028-fourzero-unequal-radical-phases-v1.md` proves only that the two phases must differ.

## Exact scope

The zero plane R has four coordinates labeled 0,1,2,3. A fiber record is an ordered tuple `(k₀,k₁,k₂,k₃)` together with a multiplicity. The model has one all-zero radical fiber and 127 other fibers; it checks the indicated mod-8 even phase λ, the odd-Q radical phase ρ, all signed magnitude counts and moments, all 257 nonnegative integral dual coefficients, the applicable rank/phase count filters, and all three **radical-direction** autocorrelations

    R(d)=2 Σ_fibers Σ_{i<i⊕d} k_i k_{i⊕d}=0,    d=1,2,3.                  (1)

The models do **not** assign the fibers to individual quotient frequencies, construct a single quadratic q/Q or the forced quartic P, check autocorrelations outside R, or produce a ±128 inverse. Thus (1) checks only three of the 511 nonzero frequency shifts. A satisfying tuple multiset is a relaxation certificate, not evidence that a four-zero target exists.

## Three explicit formal multisets

Each row below is separately recorded with all nonzero tuple multiplicities; zero direction is implicit. For nonzero λ use λ(r)=r₁. A ρ bit equal to one is the same functional; bit two is independent.

| λ | ρ | q-zero count z | odd Q weight | even residue-3 count | odd peak/unit count | peak count | R(1),R(2),R(3) |
|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | bit 1 | 144 | 128 | 56 | 160 | 160 | 0,0,0 |
| bit 1 | 0 | 112 | 144 | 72 | 160 | 159 | 0,0,0 |
| bit 1 | bit 2 | 144 | 128 | 56 | 176 | 166 | 0,0,0 |

Thus the listed scalar constraints plus exact autocorrelation **on the radical alone** do not eliminate any of the three phase types left by λ≠ρ. This observation does not address the other 508 nonzero shifts or the missing common geometry. The equal-phase case is already analytically excluded by the predecessor, not accepted or inferred from a solver status.

A separate direct checker reconstructs each 512-entry multiset from the tuples, adds the all-zero fiber, verifies every local λ/ρ relation, the moments and all three autocorrelations, and rejects a changed autocorrelation. A second scalar checker verifies the listed count implications, while the independently written Krawtchouk recurrence checker confirms all 257 dual coefficients forward and backward. These are same-owner computational checks, not a disjoint review.

## Pinned evidence

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-four-zero-directed-fibers.py` | `8917acf4631c4b3740388af38f49c5ba05745fe977507c49aba81abb9891a179` | 92 |
| `frontier-20261028-directed-fibers-check.py` | `e04a5fde8aa65bc2bba1a107c88ef18fd96c13c7f2cf62a8d407703a20739c41` | 58 |
| `frontier-20261028-directed-scalar-check.py` | `53f5900f76be230cc4f2665d9917a64b344fb3d33271185b437892c5936c4ae1` | 43 |
| `frontier-20261028-directed-scalar-check-result.json` | `f04fa0c3dac7897e6c843a9f3729718c43acd177280d56d0b5e2b258eeaf4f8b` | 41 |
| `frontier-20261028-four-zero-directed-01.json` | `cd43ed480e7ea59c4c7d8403495efc32cb20858d6ee40d1370c61e554d8f7c71` | 399 |
| `frontier-20261028-four-zero-directed-01-check.json` | `91f235be2a82829b65c55f6cd6e3b71f828530e44fe6335dff88bb8915705334` | 25 |
| `frontier-20261028-four-zero-directed-01-dual.json` | `7941a21aee30f818ac12daaa98db1a7491ea365fd636fe48d706a226cecee379` | 19 |
| `frontier-20261028-four-zero-directed-10.json` | `0557b2b6fc27994c3169b5387f9243c29e54b420e9c9c7dc3eab15a56bb9338c` | 516 |
| `frontier-20261028-four-zero-directed-10-check.json` | `1c9c8035fe161400ba3af0ce3c9baf0d9a6941a292d286506001cacffa218f83` | 25 |
| `frontier-20261028-four-zero-directed-10-dual.json` | `2008329bb49d6d6c1da7bae9ab6b8394f24337ba9a1ad96363033c98f556f2ad` | 19 |
| `frontier-20261028-four-zero-directed-11independent.json` | `c4c4bfa01c9456b3dd9d0473b2b00da7a20e28b5941c96abde718e54b9c61750` | 396 |
| `frontier-20261028-four-zero-directed-11independent-check.json` | `360c3cd48591e4f42513411c543de4cabfe22bdb624acc1fa659b4fd653ef80b` | 24 |
| `frontier-20261028-four-zero-directed-11independent-dual.json` | `cb52cb4008864efc9f0957fc0b2466e3c213d7dd49b2583d882c8f44179421f7` | 19 |

No original-target witness or unrestricted exclusion follows. **END.**
