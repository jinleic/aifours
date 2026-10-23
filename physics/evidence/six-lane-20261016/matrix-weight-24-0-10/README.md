# Replacement target (phys-2 slot): integral matrix weights for a hypothetical `[[24,0,10]]_2`

Six-lane run 2026-10-16. Switched here from `../noncws-code/` (unrestricted `((7,3,3))_2`, recorded OPEN /
NEEDS-NEW-REPRESENTATION) on parent instruction. Frozen by parent: `institute/runs/six-lane-2026-10-16/screening/fresh-physics-screen.md` rank 1.

## 1. Frozen target

**AMH Open Problem 1** (Anglès Munné–Huber, arXiv:2603.19901v1 §3.3, p. 8; pinned `sources/rational-sdp-2603.19901.pdf`,
sha256 `6e8783…53b1`): for the hypothetical `[[24,0,10]]_2` stabilizer code with putative weight distribution Eq. (38)
`(A10,…,A24) = (18216, 156492, 1147608, 3736557, 6248088, 4399164, 1038312, 32778)`, provide integers
`λ^{t,p}_{i,j}` satisfying Eq. (31) plus pure (32), self-dual (33), additive (34: `x ≥ 0`, `λ ∈ Z`) and Type II (35)
constraints (`n=24, K=1, δ=10`) — or prove that none exist.

- A positive table answers the stated feasibility question only; it does **not** imply the code exists.
- Nonexistence of integer tables satisfying *necessary* conditions would exclude the code; such a claim needs an
  exact certificate, an independent derivation and the controls below (high bug risk).

## 2. Status and baseline (2026-10-16)

- Underlying code: open (Rains–Sloane survey math/0208001; Grassl table lists `8 <= d <= 10` for `n=24,k=0`; a
  `(24,2^24,10)` additive self-dual code must be even). No resolution found in a dated search; not proof of openness.
- Eq. (38) independently re-derived: it is the unique Gleason polynomial in `C[x^2+3y^2, y^2(x^2-y^2)^2]` with
  `A0=1, A2=A4=A6=A8=0` (sympy, exact); it sums to `2^24`.
- AMH machinery reproduced in the predecessor lane: GST06 blocks brute-force verified (n<=3); AMH exclusions of
  ((8,9,3)) and pure ((6,2,3)) reproduced numerically.

## 3. Representation and protocol (frozen before the n=24 runs)

For a stabilizer state, `Γ_ab = 1` iff both Pauli labels are in the stabilizer group, so `λ^{t,p}_{i,j}` is the
S3-symmetrized **pair (genus-2) weight distribution** of the additive self-dual code: coordinate types
`00, 0x, x0, xx, xy` with `n_x0=i−t, n_0x=j−t, n_xx=p, n_xy=t−p`. Additional necessary linear conditions not in
AMH's list but valid for every additive self-dual code: genus-2 MacWilliams self-duality
`Σ_τ f(τ) K(τ→τ') = 2^{48} f(τ')` (`K` from the brute-force-verified 5×5 symmetrized transform `T`, `T^2=16I`),
S3 symmetry, and support only on pairs with `wt u, wt v, wt(u+v) ∈ {0,10,12,…,24}`.

Protocol: (1) solve the genus-2 linear system exactly (modular elimination → exact rational reconstruction);
(2) if a solution family exists, search it for nonnegative integer points and check every AMH constraint, with exact
block positivity; (3) if no admissible point exists, produce an exact certificate and review hostilely.
Controls (all run): AMH Example 6 `[[5,1,3]]` matrix weights reproduced exactly; hexacode and dodecacode
(graph state of circulant C12(1,3,6), weights `1+396y^6+1485y^8+1980y^10+234y^12`) pair counts satisfy genus-2
MacWilliams exactly, mutations detected; in the linear system the hexacode solution is unique and equals the actual
counts, the dodecacode lies in a 1-dimensional solution family.

## 4. Results

**Verdict: CANDIDATE answer to AMH Open Problem 1 (positive), frozen as `frozen-candidate-v1/`.** An explicit table
of nonnegative integers `λ^{t,p}_{i,j}` (`frozen-candidate-v1/lambda_24_0_10.json`, sha256
`15a159af1078468defea70d4394f25d896b51d471ed8f2f59453502357fe73e1`; 1616 nonzero entries, total `2^48`) satisfies
every constraint of AMH Eq. (31)–(35) and Eq. (38) exactly. Labels: **Certification** of a precisely scoped
feasibility statement; it does **not** show that a `[[24,0,10]]_2` code exists. Novelty: answers an explicitly
posed open problem of a 2026 preprint; dated prior-art screens (arXiv v1 only, AMH certificate repository,
EulerSolve listing, openai/math CONTENTS) found no earlier answer; Zenodo API returned 403. Not a priority claim.

| Step | Result | Evidence |
|---|---|---|
| Genus-2 linear system (S3-symmetric, extremal support, genus-1 marginals, full MacWilliams) | 415 orbit unknowns, rank 407 modulo each of 8 primes, consistent; exact rational reconstruction stable from 6 to 8 primes; 9 exact lattice points of affine rank 8 ⇒ solution space is **exactly 8-dimensional** | `evidence/g2_solution_space.json`, `evidence/family_dimension_check.json` |
| Partial MacWilliams (Fourier in one factor, `T1`, `T1 T2 = T`) | adds no rank (still 407): implied on this support | `evidence/g2_system2_n24_p*.json` |
| AMH blocks on the family | 84 of 125 nonzero blocks are exact rank-1 families `c(s)·vv^T` (PSD ⇔ linear inequality); the other 41 have structural kernels and compressed rank ≤ 3, positive definite (float) at the LP center | `evidence/block_structure.json`, `evidence/general_blocks.json` |
| Integral points | integrality lattice index `1.13e14`; with 2-subspace divisibility `2.1e19`; nearest point to the strictly feasible LP center passes all checks | `evidence/int_lattice*.json`, `evidence/candidate_subspace.json` |
| Independent exact verifier | `verify_amh.py` (stdlib, Fractions, exact `Q(√3)` LDL^T): ALL_PASS; parent's separate stdlib checker also passed (parent report `institute/runs/six-lane-2026-10-16/review/matrix-weight-parent-verification-v1.json`) | `frozen-candidate-v1/receipts/amh_check.json` |
| Controls | AMH Ex. 6 reproduced; hexacode & dodecacode pass; n=24 random even groups and n=7 odd-weight groups give PSD blocks; ±1, swap, ×2, delete, spurious entry fail; PSD load-bearing control: an integral nonnegative family point passing all linear gates fails blocks (3,3),(6,6) with exact certificate `B_{10,10} = −15685/163944` | `frozen-candidate-v1/receipts/controls.json`, `frozen-candidate-v1/appendix-psd-control/` |
| Extra (separate) | genus-2 full and partial MacWilliams identities hold for **all 20475 coefficients**, exact by 6-prime evaluation with deterministic height bound `2^145`; 2-subspace divisibility holds | `frozen-candidate-v1/receipts/g2_rigorous_*.jsonl`, MAP.md |

Floating-point SDP/LP solves only located the strictly feasible region; every claim above is re-checked exactly.

Review status: Codex `gpt-6.1-sol` (max, read-only) hostile review **ACCEPT** with only informational findings
(`review/codex-review-output.md`); parent independent full-table checker PASSED; parent confirmed the PSD-only
control. Verifier v1.1 (no float paths) added with v1 preserved; snapshot manifest
`frozen-candidate-v1/MANIFEST.json` (sha256 `3a504093b62c904047e73f783854d2b2d08a8c77e632b85386abe9d4ee156be1`).

## 5. What this does and does not say about the code

Genus-2 pair-enumerator constraints, AMH's degree-3 moment SDP, integrality and 2-subspace divisibility are jointly
satisfiable in an 8-dimensional family; they cannot exclude a `[[24,0,10]]_2` code. Deciding existence would need
genuinely stronger information (e.g. genus-3 enumerators, about `10^10` raw type vectors before reductions, or
higher AMH levels), not attempted here.
