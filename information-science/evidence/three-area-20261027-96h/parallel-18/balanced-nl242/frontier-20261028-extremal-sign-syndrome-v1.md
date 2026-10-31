# info-6 frontier: an extremal sign-syndrome obstruction

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:38:10-0700**. **UNREVIEWED AUTHOR CANDIDATE**. The written Fourier argument below uses the unreviewed three-orbit classification in `frontier-20261028-fullrank-extremal-phase-v1.md` and a complete same-owner 3×512 phase computation. It is neither parent-adopted nor independently reviewed, and does not settle existence, unrestricted exclusion, book-source status, or novelty.

## Statement and consequences

Let f:F₂⁹→F₂ be balanced with `T=⊕{x:f(x)=1}≠0`, `max|W_f|≤28`, and full-rank even-half polar B. On the odd frequency half put `k=W_f/4`, `P=1_{|k|∈{1,7}}`, and `n_j=#{|k|=j}` for j=1,3,5,7. At the full-rank boundary `wt(P)=210`, necessarily

    n₁+n₃ is odd and at least 9.                                  (1)

The actual ten-zero formal count vector in `frontier-20261028-tenzero-common-placement-v1.md` has `n₁=2,n₃=5`, hence cannot be realized by **any** placement of its spectrum if this candidate and its dependencies hold. This is stronger than observing that its one displayed placement fails correlations, but remains a single count-vector exclusion, not an exclusion of all ten-zero f.

Combining (1) with the rank-eight odd-energy identity and `wt(1−P)≥46` also gives the unreviewed support floor m≥80 in the pinned support-floor packet: at m=78 the only two possibilities have `(n₁,n₃)=(0,3)` or `(1,0)`, both forbidden. At m=80 and `wt(P)=210`, the energy identity gives `n₃+3n₁=11`; (1) therefore implies `n₁≤1` and `n₃≥8`. The previously formal m=80 vector has n₁=2 and is excluded by this sharper condition; this does not exclude m=80 itself.

## Baseline and exact syndrome

Use the pinned polynomial identities: the odd quadratic `Q=1_{k≡3 mod 4}` has polar B, and h=1−P has degree≤4 with quartic Pfaffian of B. The pinned phase paper proves that every full-rank h of weight 46 is equivalent, under an affine symplectic change of the eight coordinates, to one of three explicit slice representatives. Such a frequency relabelling preserves both histogram and divisibility of inverse character sums.

At any odd frequency, its residue modulo 8 is determined by Q and h:

    r=(1+6Q+4h) mod 8 ∈{1,3,5,7}.

Each admissible signed value is `k=r−8b` for a bit b. Choose the deterministic baseline

    b₀=1_{r∈{1,3}},    k₀=r−8b₀.                                (2)

Thus k₀ equals −7,−5,+5,+7 on the four r-classes 1,3,5,7 respectively. Let `δ=b−b₀`. Exactly the entries with |k|=1 or 3 differ from this baseline, so δ has `D=n₁+n₃` nonzero entries, each ±1.

For each of the three h representatives and all 512 Q phases with the fixed polar, the finite checker verifies an exact modular identity for all 256 inverse-character indices y:

    8 divides K₀(y),     K₀(y)/8 ≡ A(−1)^{<p,y>} (mod 16),       (3)

where `K₀=Walsh(k₀)`, `A∈{−5,+5}`, and the representative-dependent p is as follows. For each representative 256 Q phases have A=−5 and 256 have A=+5.

| h slice pattern | p, as an 8-bit mask | Q phases | y indices each |
|---|---:|---:|---:|
| (8,8,8,22) | 255 | 512 | 256 |
| (8,8,14,16) | 143 | 512 | 256 |
| (10,12,12,12) | 0 | 512 | 256 |

The table is an explicit finite calculation; the reason these three representatives cover the all-variable case is the written orbit proof in the pinned phase paper. No solver UNSAT result is used.

## Fourier contradiction

For an actual f, the inverse of the odd-half Walsh spectrum satisfies

    Walsh(k)(y)=128v(y),  with v(y)∈{−1,0,1}.                    (4)

Since `k=k₀−8δ`, (3) and (4) force

    Walsh(δ)(y) ≡ A(−1)^{<p,y>} (mod 16) for all y.             (5)

Each of the D nonzero δ entries is ±1, so every Walsh(δ)(y) has the parity of D and absolute value at most D. The right side of (5) is odd, making D odd. If D≤7, every odd residue modulo 16 has a unique representative in [−7,7], so (5) gives exact equality `Walsh(δ)(y)=A(−1)^{<p,y>}` for all y. Inverting the 256-point Walsh transform yields `δ=A·1_{p}`, impossible because δ has entries only −1, 0 or 1 and |A|=5. D=8 is already excluded by parity. Hence D is odd and at least 9, proving (1) conditional on the three-orbit proof and finite table. ∎

## Positive near miss and limits

For each explicit representative the checker also takes one Q phase and deliberately sets `δ=A·1_p`, producing `k′=k₀−8A·1_p`. All 256 inverse sums of k′ are then divisible by 128, as (3) predicts, but the single modified coefficient has magnitude at least 33, violating the permitted peak bound `|k|≤7`. A mutation applying the same change at `p⊕1` fails the divisibility test. This is a positive control for the modular obstruction with the sign/peak bound relaxed; k′ is not a Boolean spectrum and is not an existence witness.

The result constrains only the extremal `wt(P)=210` rank-eight branch. Other peak/unit weights, other histograms, rank-six/rank-four cases, all target construction and the unrestricted witness-or-exclusion question remain unresolved. The finite table and the inherited orbit argument require disjoint review.

## Pins

| File in this directory | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-extremal-sign-syndrome-check.py` | `aacaf9e79c9d01325fb0c6f7310c96e5085a70040f91c1a620cc84d502db7f2f` | 63 |
| `frontier-20261028-extremal-sign-syndrome-check-result.json` | `8d80d4f6b53ec7e2ffd39d8357602944e80f67c2f8a1445b568648f8180cd287` | 60 |
| `frontier-20261028-fullrank-extremal-phase-v1.md` | `e12b3a32a3f7f19b9dea35615bbf4c8fbd6ba970d1491ca33f3fc8f4bacc6fd4` | 100 |
| `frontier-20261028-fullrank-support-floor-v1.md` | `5df3df9277c71ed31ba0ae8969666306dae73ce16c2488cffb4b31125729e2bd` | 75 |
| `frontier-20261028-tenzero-common-placement-v1.md` | `4b587b60028d1344386fccde7db565fb7a6e4a990f715307f60f2e555fcf267f` | 47 |

**END.**
