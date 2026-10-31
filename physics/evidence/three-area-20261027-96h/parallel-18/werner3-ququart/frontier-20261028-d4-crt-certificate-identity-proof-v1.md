# Exact d=4 certificate identity by a separately audited CRT height bound

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: **Wed Oct 28 17:42:24 PDT 2026**. This adds a second exact global-arithmetic route to the pinned corrected certificate; it is not a new theorem/priority claim, a Lean proof, independent human/model-family review or parent adoption.

## 1. Exact result

For the pinned d4 three-copy corrected rational certificate, all **4675** orbit-sum residuals are exactly zero. The modular checker recomputed every residual for **424 distinct primes**, all yielding zero. Its explicit integer residual bound B has **6745 bits**, while the product P of those primes has **6761 bits** and satisfies the actual exact comparison `P>2B`. Thus this is an exact rational-zero inference, **not** an assertion that agreement modulo a few primes is a proof.

The checker uses a new NumPy-int64 modular aggregation backend, no author `ep3core.py`/`verify_perd.py`, and no FLINT arbitrary-precision matrix multiplication for the global residuals. It shares the previously independently written literal local-map and orbit generators, and the same public data; it is not independent of every software or coding assumption. The earlier exact FLINT-integer global checker, author replay, saved-data PSD check and finite local commutant witness are separate companion evidence.

- CRT checker `frontier-20261028-d4-modular-crt-identity-proof.py`, SHA256 `57fb9da48e142b0288b723402111e2121fae69dbc2be6fa2c61a86bb5fb41086`.
- Full receipt with exact D, B, prime list and P: `frontier-20261028-d4-modular-crt-identity-proof-results.json`, SHA256 `f93866ea9171a6dd8b1ecd4ca78fbeb5afe86167aebdc02c701a721da9705d3b`.
- Separately recomputed height/modulus audit `frontier-20261028-d4-crt-height-bound-audit.py`, SHA256 `b7e7df74d12783bf905c132d8766048d8a1c7b1562f738f8c7edab91bf8c7d84`; result SHA256 `1c08e90c8c7aafe291bd82a60b23c8bbea6375bfe12d6c699d7cb7e3d76b5dfc`.
- Actual CRT runtime **115.062s**, one process/single BLAS threads; separate bound audit **4.692s**. Both reported PASS.

The input source archive SHA256 is `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`; corrected data SHA256 is `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`. The exact original operator is q3 for arbitrary complex rank<=2 C on `(C^4)^tensor3`, with unnormalized traces and coefficients1,−1/2,1/4,−1/8. No physical domain or normalization was substituted.

## 2. Exact integer scaling

Let D be the positive least common multiple of the denominators of all1237 corrected rational multipliers Z_t, all329 corrected equality coefficients lambda_e, and the objective denominator `2^3(2*4^3)^4=2^31`. D has **6645 bits**. Define integer matrices `Z'_t=D Z_t` and integer coefficients `lambda'_e=D lambda_e`.

For a family f and source orbit o, let

`R_(f,o)=D [c(o)−Σ_t Tr(Z_t K_t†M_t(o)K_t)−Σ_e lambda_e E_e(o)]`.

All local maps, compression matrices and word traces are integer-valued after this scaling. Hence every R is an integer. The orbit partition is independently regenerated from the actual letter stabilizers, site permutations and inversion; counts are1142,2391,1142. The 424-prime run computes each of these integers modulo every listed prime, after confirming each prime is coprime to D.

## 3. A concrete upper bound on EVERY integer residual

For a type t let k_t be its number of Gram rows, r_t its multiplier dimension, and n_t the product of its four local compression dimensions. Let

`Zmax=max_(t,a,b)|D(Z_t)_(a,b)|`,
`Lmax=max_e |D lambda_e|`.

Using the pinned data and every independently rebuilt local map, the checker uses:

- `Wmax=771160`, the maximum absolute integer congruence entry;
- `Amax=256`, the maximum absolute site/auxiliary Gram local-map entry;
- `Emax=24`, the maximum absolute local equality-map entry;
- `Cblock=Σ_t k_t² r_t² n_t²=278530617`;
- `Ceq=Σ_e(number of signed parts of equality e)=433`;
- `Cobj=1438646272`, a bound on the absolute objective numerator of ONE word.

These are actual-data maxima/counts, recomputed independently by the separate height audit. To justify the formula, a word contribution of one type is a sum over at most k_t² row pairs, r_t² multiplier indices and n_t² paired compression indices. Each summand has magnitude at most `Zmax*Wmax²*Amax^4`. Thus the sum over all types is bounded per word by

`Cblock*Zmax*Wmax²*Amax^4`.

Each lambda coordinate contributes at most its number of signed equality parts times `Lmax*Emax^4`, giving the per-word equality bound `Ceq*Lmax*Emax^4`. The objective is bounded by `Cobj*(D/2^31)` in the same integer scaling. Any orbit has at most `24^4=331776` words. Therefore the single conservative bound

`B=24^4 * [Cblock*Zmax*Wmax²*Amax^4
            +Ceq*Lmax*Emax^4+Cobj*(D/2^31)]`

satisfies `|R_(f,o)|<=B` for EVERY family and orbit. It need not be sharp. The separate audit reread the exact archive/corrected data, rebuilt every used map maximum, recalculated D and B with Python integers, and matched the receipt's complete decimal values exactly.

## 4. Distinct primes, safe modular arithmetic and exact conclusion

The receipt lists every prime, the exact product P and the exact bound B. The separate audit verified all **424** moduli are distinct, prime by trial division, and do not divide D; recomputed P exactly; and checked `P>2B`. The CRT program reports zero nonzero-residue primes and explicitly records the first-prime residual counts0/0/0.

For each modular contraction, values are reduced modulo p before matrix multiplication. The code checks the contraction-axis and multiplier-rank bounds against signed int64 overflow. Here p<=65521, multiplier rank<=40, so `40*(p−1)^2<2^63`; every orbit accumulation is bounded by `331776*(p−1)<2^63`. The program also checks each mode's actual axis width. All additions/multiplications in the modular backend are exact within those bounds; no floating-point reduction or approximate tolerance is used.

For any fixed residual integer R, all tested residues are zero, so P divides R. Since `|R|<=B<P/2`, necessarily R=0. This applies to all4675 residuals. The separately pinned exact FLINT-integer implementation independently reported the same zero identity on the same corrected rational bytes; this CRT proof uses a distinct modular arithmetic contraction but shares our literal-map/orbit generators and Python/numpy runtime.

## 5. Fault control and retained proof boundaries

At the first prime, an in-memory +1 change to one aab equality coefficient produced **1142 nonzero family31 and2391 nonzero family22** residuals; the original corrected-data bytes were restored and never rewritten. The receipt labels this an intentional fault control, not a physical counterexample. Other independently run single/coupled block, trace-subset and PSD controls are documented in `frontier-20261028-d4-certificate-verification-addendum-v1.md`, SHA256 `176eac7dcf96c9819c5d73488787b18a201be0a0b5a46061b26ac83f67a14340`.

The global identity is only one premise. The independent saved-data Schur check established all1237 corrected multipliers positive definite, and the actual local block/equality validity and full physical lift are reconstructed in `frontier-20261028-d4-certificate-bridge-and-independent-identity-v1.md` (`cc9a354a16b9d3abf6ac1ef8ff6fcc6e2041a88d435216b9d9b326a85f348a66`). The only needed local `U(2)`/`U(4)` four-replica source spans have an independently replayed finite-rank witness in `frontier-20261028-d4-four-replica-commutant-finite-rank-proof-v1.md` (`49df4f874bf8c4a4da60d61f1b76d9b8028e2acfca5fe6d8c2b378a324501a23`), with subsequent standard-library-only replay; these facts together give the stated computer-assisted d4 proof candidate, conditional on code/runtime and written-argument correctness.

The separate height audit validates the bound and prime-product inference; it **trusts the per-prime residue run** and shares literal-map helpers. These are not independent model families, a Lean kernel, human verification or parent adoption. The paper already made the full-target claim; no new priority or all-d>=9 validation is asserted. Historical held outcomes remain unvalidated and are not premises.
