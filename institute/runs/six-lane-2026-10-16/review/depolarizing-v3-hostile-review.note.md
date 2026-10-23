VERDICT: ACCEPT-WITH-FIXES

This is a reasoning-only review of the pasted PROOFS_v4.md, cert.py, dd.py, combine.py and p1_5_TOTAL.json. I did not have the witness JSON or the sector `.jsonl` records, and I executed nothing. I treated the listed cross-checks and the replay as evidence, not proof. **Acceptance depends on M1 being discharged. If that check fails, the certificate is void.**

## Fatal

None found.

## Major

**M1. The modular-support hypotheses of §4 and F2 are used on the certified path but never checked.**

§4 and F2 require each φ_i to be supported on {x ≡ r_i (mod k)}, with the r_i pairwise distinct.

- `parse_witness` returns `w.get("k"), w.get("residues")` verbatim.
- Nothing in `certify`, `run_sector` or combine.py checks them against `amps`. The only input checks are the 1e−100 floor and `assert M + D < 10 ** 6 and D < 10 ** 4`.

`run_sector` relies on these values twice:
- **Block structure.** `blocks_B = [np.nonzero(xs % k == c)[0] ...]` and `blocks_RB = [...]` discard every cross-block entry of B and RB with zero radius.
- **Flag structure.** The comment `# one flag (PROOFS §4): modular inputs => RB flag block diag(q_i w_i)` assumes tr(Q_D Φ̂(φ_iφ_j†)) = 0 for i ≠ j.

If a single entry of some a_i lies outside its class, or two residues coincide, the code silently computes entropies of the pinched B and RB.
- Pinching can only raise entropy, so the S(B) lower bound becomes invalid.
- The flag term is also wrong.
- Replay reproduces the error bit for bit, and combine.py cannot detect it.

The same gap covers two smaller witness premises:
- **K = max len(a_i) − 1 ≤ M.** If x > M, the first `loss_step_dd` drops those entries while `norms2` still counts them.
- **§3's "d ≤ 10⁴".** This is asserted for D but not for the loss-chain width K+1.

**Fix:** run an exact, index-level check on the witness with sha256 43117f99…7991e2. It should verify:
- supp(a_i) ⊆ the residue class r_i;
- the r_i are pairwise distinct mod k, with k ≥ 2;
- K ≤ M;
- whether the witness is real.

Make it a standalone script whose output records the witness hash, so the existing cert_py_sha256 81d50d… records stay valid. I could not run this check. The description "mod-3 comb" does not replace it. Neither does the parent's float64 agreement, because that implementation may share the block assumption.

## Minor

**m1. Unrounded float addition on the upper-bound path.**
- In `run_sector`, `icu = up(ic_hi) + sum(f[1] for f in fRB)` uses round-to-nearest, and so does the inner `sum`.
- The loss is at most Σ_i h(q_i w_i) ≈ 1e−24 per sector.
- In this run the 1e−12 slack on `afw`/`sw` absorbs it: loss/slack ≈ 2√w/1e−12 ≤ 0.22 for w ≤ 1.2e−26. That coverage is incidental, and the proof does not argue it.
- Only the upper endpoint is affected, not POS.
- Fix: compute it in Arb, as `arb(up(ic_hi)) + Σ arb(f[1]) + arb(afw)`.

**m2. Documentation contradicts the certified code (no math error).**
- **(a) §5 refinement note.** §5 says the lowest-cluster refinement exists only in "code versions after the M=2000 p=1/5 run". But the TOTAL's cert hash 81d50d… is the pasted v3 code, which contains the refinement (`if ci == 0 and kc > 1:`). So this certificate relies on it. I checked the refinement and it is correct. The sentence should say the refinement was used.
- **(b) cert.py header.** It cites `review/PROOFS.md` and `PROOFS_v2 A3`; it should cite v4.
- **(c) dd.py docstring.** It says "cert.py asserts the exponent range at runtime", mentions a "separate float64 magnitude recursion", says "far from overflow/underflow", and gives "64.5 u²". All are false for v3. §3 is the operative model, and the constant is 64u².
- **(d) §3 error formula.** "((1+ε)^L − 1 + max δπ)" omits the cross term. The correct form is (1+ε)^L(1+δπ) − 1. The two `1.01` factors in `relE` already cover the difference.
- **(e) §3 step count.** "≤ 10⁶ steps" does not follow from the guard M + D < 10⁶, since the step count is (M−s_min)+(N−s_min) ≤ 2M. This is immaterial at M = 2000.

**m3. Guards implemented as `assert`.** The checks in `parse_witness` (`sum(qs) == 1`, `q > 0`) and `certify` (`M + D < 10**6`) disappear under `python -O`. They should raise explicit exceptions.

**m4. Float operations treated as exact, all harmless here.**
- **`orth` test.** `orth = ... np.vdot(...) == 0`, in both cert.py and combine.py, is a rounded test, not the "disjoint supports" test §5 states. It has no soundness effect: S(Σq_i|φ_i⟩⟨φ_i|) ≤ H(q) ≤ log r holds for any unit vectors φ_i, so both branches give valid upper bounds. Both equal 1 bit here.
- **`arb_to_dd`.** If `float(arb)` truncates (as far as I recall, python-flint uses `ARF_RND_DOWN`), then |lo| can reach 2u·hi. That breaks §3's premise |x_l| ≤ u·x_h. The mul error bound becomes about 12u², still below 64u², so there is no effect.
- **Complex witnesses.** The 1e−100 floor is applied to |c|, not to the Re/Im parts, so "all inputs ≥ 1e−200" does not follow for complex witnesses. This is irrelevant if the witness is real; the M1 check should confirm that.

## Checked and found sound

- **§0.** D_{η1}∘D_{η2} = D_{η1η2}. For p ≤ 1/5, η_p ≥ 11/15 > 0, so data processing applied tensor-wise gives I_c(ρ*, N_p^{⊗M}) ≥ I_c(ρ*, N_{1/5}^{⊗M}). LSD then gives Q ≥ I_c/M, in bits.
- **§1.**
  - det A_uv = ab·g², by the matrix determinant lemma.
  - q_N = (a^{N+1}−b^{N+1})/η, and Σπ_s = 1 exactly.
  - p_N = m_N·s_{(M−λ,λ)}(a,b), so Σp_N = 1.
  - B and RB share the same p_N, the multiplicity terms cancel, and the purification is valid without orthogonality.
- **§2.**
  - I re-derived the Dicke matrix elements of L and C.
  - The cloner chain holds because P_{n+2}(P_{n+1}⊗I) = P_{n+2}.
  - The Horner recursion is correct, and x−y is conserved.
  - Truncation is exact: the loss chain keeps the full input support, and the add chain is cut at D.
  - Index ranges in `loss_step_dd`, `add_step_dd` and `axpy_dd` are correct.
- **§3.**
  - Error constants: add ≈ 4u², mul ≈ 8u², sqrt/recip ≤ 3.1u². The chain uses at most 6 steps per level, against STEP_OPS = 10.
  - Flush and A_op damage propagate through CP trace-non-increasing maps. Russo–Dye covers the non-Hermitian parts, and flushes only remove nonnegative mass.
  - The (1+1e−6) radius slack covers 1/(1−relE), (1+2⁻⁵²), and the float rounding of `rad`.
- **§4.**
  - T_D is CPTP, and the F4 flag identity holds.
  - In the π-tail bound, the upper bound e ≥ ε is used monotonically, which is valid for e ≤ ½.
  - The Araki–Lieb bounds are correct.
  - AFW is applied correctly: dim R = r, ε = √w ≥ √(w(1−w)), and I_c(pinch) ≤ (1−w)I_c^P + w·log r.
- **§5.**
  - Ostrowski is applied with δ ≥ ‖V*V−I‖₂.
  - Gershgorin component counting survives the outward enlargement, and the ordered components map to sorted eigenvalue indices.
  - The outward division rules and `h_range` are correct.
  - The Ky Fan / Jensen lowest-cluster bound is correct.
- **Rounding helpers.** `lo` and `up` are outward for any faithful arb→double conversion.
- **Aggregation.**
  - The aggregation is done in Arb, as Σp_N·[lo_N, hi_N] ∓ rest·S_hi.
  - combine.py uses the same sector partition as cert.py.
  - JSON floats round-trip exactly.

## What is and is not established

**Established, given M1 and the trust base:** a rigorous two-sided enclosure of I_c for this specific ρ* at p = 1/5 and M = 2000. Positivity therefore holds for all p ≤ 1/5.

**Not established:**
- Anything for p > 1/5. The p = 201/1000 NEG record was not provided. Even if correct, it would only say that this ρ*'s M = 2000 coherent information is negative there, not that Q = 0.
- Optimality of ρ* or of M.
- Any priority claim relative to 2608.15870 or 2609.39747. Both are past my knowledge cutoff and I cannot verify them.
- Correctness from the replay and cross-checks alone. They show reproducibility and implementation consistency only.

## Minimal certified wording

> Let a_0, a_1 be the dyadic Dicke-basis vectors and q the rational weights in the witness with sha256 43117f99…7991e2. Set φ_i = a_i/‖a_i‖ and ρ* = Σ_i q_i|φ_i⟩⟨φ_i| on Sym^2000(C²). Then 1.1373755593447965·10⁻⁸ ≤ I_c(ρ*, N_{1/5}^{⊗2000}) ≤ 1.1432769065159199·10⁻⁸ bits. Hence Q(N_p) ≥ 5.68·10⁻¹² qubits per channel use for every p ∈ [0, 1/5].
>
> This is conditional on:
> - the witness passing the M1 support/residue check;
> - IEEE-754 binary64 round-to-nearest with gradual underflow and no FMA contraction in the numpy build used;
> - correctness of FLINT/Arb and python-flint;
> - the cited theorems (Schur–Weyl, LSD, data processing, Araki–Lieb, Winter's Lemma 2, Ostrowski, Gershgorin, Ky Fan).
