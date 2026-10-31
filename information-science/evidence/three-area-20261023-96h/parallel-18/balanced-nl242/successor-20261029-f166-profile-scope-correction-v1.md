# f166 additive correction: remove the hidden residue and withdraw low-rank completeness

Owner: InfoBalancedNL242-2-2. Native clock observed before this write: **2026-10-29T09:22:12-0700**.

**Status: AUTHOR CORRECTION / UNREVIEWED REPAIRED SCOPE.** This is one additive correction to successor-round f166 and its profile-dependent consumers. It makes no new exclusion, witness, completeness, novelty or acceptance claim. All frozen sources remain unchanged.

**Storage boundary.** This file is stored in this worker's explicitly permitted Oct-23 owner root. Its subject is the Oct-27 successor material named below; it does not reopen the closed Oct-23 round or alter that round's final status. No new scientific computation was run for this correction. The reviewer-reported census and counterprofile were read from existing f166 evidence, not rerun.

Path abbreviations:
- `R` = `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/`.
- `F` = `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f166-walsh-rank-two-coset-exclusion/`.
- `P` = `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

## 1. Accepted defect and immediate withdrawals

Main reported f166 as FATAL 0 / MAJOR 1 / MINOR 3. I accept M1 and all three minor corrections.

The alleged complete rank-two roster of 17 unsigned profiles in three `(D,m)` pairs and complete rank-four roster of 50 profiles in ten pairs are **withdrawn as necessary complete rosters**. The resulting unconditional rank-two exclusion, exclusion of m=114/116 by omission, and every claim that the stated rank-four survivors exhaust the target are withdrawn as well. These claims are UNADOPTED, not repaired by relabelling the omitted cases as infeasible.

The failure is present in the source, not merely in prose: `R/frontier-20261028-lowrank-valid-profile-check.py`, LF24, contains

`if m%2 or m>mmax or m<0 or m%3!=(1-D)%3:continue`

Thus the generator imposed `m≡1−D (mod 3)` while the paper LF28 expressly said this spurious relation was not used. LF39–42 then asserted the narrowed counts/extrema. That receipt is **INCOMPLETE/NONINPUT for exhaustive profile coverage**. Its filename containing “valid” carries no authority.

The valid energy residue is only `m≡n₃=D−n₁ (mod 3)`, from `Σ_odd k²=64(256−m)`. The deficit identity `8(m−60)=6n₁+5n₃+3n₅` supplies the same relation, not a second independent restriction. This correction does not try to justify the hidden residue.

## 2. Corrected census: attributed to the f166 reviewer

The following is transcribed from `F/rv-f166-controls-v1-result.json`, key `C_profile_enumeration`, and `F/review-v1.md`, LF109–144. These are **coarse unsigned magnitude profiles under the stated scalar constraints**, not labelled spectra or actual Boolean functions. D lower bounds remain inherited from author-only sparse-sign inputs that f166 did not review. Main's disposition is still required.

| Rank | Old claimed profiles / pairs | Reviewer reconstruction | Reviewer n₇ range | Reviewer Z upper bound |
|---|---:|---:|---|---:|
| 2 | 17 / 3 | 91 / 15 | 99–124 | 40 |
| 4 | 50 / 10 | 121 / 25 | 123–146 | 40 |

Literal coarse pair roster at rank two:

| D | m |
|---:|---|
| 12 | 114, 116, 118, 120, 122 |
| 16 | 116, 118, 120, 122 |
| 20 | 118, 120, 122 |
| 24 | 120, 122 |
| 28 | 122 |

Literal coarse pair roster at rank four:

| D | m |
|---:|---|
| 8 | 104, 106, 108, 110, 112 |
| 10 | 106, 108, 110, 112 |
| 12 | 106, 108, 110, 112 |
| 14 | 108, 110, 112 |
| 16 | 108, 110, 112 |
| 18 | 110, 112 |
| 20 | 110, 112 |
| 22 | 112 |
| 24 | 112 |

The explicit counterprofile is `(D,m,S,n₁,n₃,n₅,n₇)=(12,114,−4,12,0,120,124)`. The reviewer records all stated scalar checks as true, with odd energy `9088=64·142` and the collective identity `384=448−64`. It is outside the old roster. It is **not** a witness or a claim of frequency placement.

The reviewer also reproduces the old rosters exactly after restoring the disclaimed residue. That is evidence of the enumeration error, not permission to use the residue.

## 3. Repaired rank-two theorem and complete statement of the uncovered domain

Replace the title/conclusion “rank two is impossible” in any use of the frozen coset paper by this restricted statement:

> Under the target hypotheses, rank two, q-zero count z=64, the caller congruence `E₂+2n₃≡0 (mod 4)`, and Z≥8, the frozen coset proof, with the three textual repairs in §4 below, excludes **m∈{118,120,122}**. The argument depends on `(m,Z)` and not on the defective complete D/m roster. This is a repaired conditional author scope, not a parent adoption.

The z=64 reduction and sparse-sign D bounds retain their separate original review/acceptance status. They are not newly adopted here. The Z≥8 premise is available at the f131/f152 rank≤4 scope; the invalid cubic-divisor-eight claim is not used or revived.

The untreated rank-two scalar domain is:
- `(D,m)=(12,114)`: `Z∈{8,12,16,20,24,28,32,36,40}` and `E₂=20−Z/2`.
- `(D,m)=(12,116)` or `(16,116)`: `Z∈{8,12,16,20,24,28,32}` and `E₂=16−Z/2`.
- For each row retain every nonnegative odd-magnitude profile meeting the stated energy/collective equations and caller congruence, and every nonnegative even triple `(e₁,e₂,e₃)` of even integers with sum E₂, subject to the genuine local lemmas. No omitted triple is declared impossible by this correction.

The first unresolved step is to exclude these domains using additional valid arguments or to realize an actual target. They are not settled by the old case analysis.

**Non-vacuous residual.** The reviewer gives `(m,Z,e-pattern)=(116,16,(0,4,4))` with feasible geometric relaxation counts `A₁=16`, `C₂=C₃=4`, `D₁=18`, `G₂=G₃=2`, `O=18`, `H=0`, and `|F₂∩F₃|=2`. In this regime the old argument gives the even value `2+2H`, not the contradictory odd value `1+2H`. These are relaxation counts only: no signs, full Boolean inverse, or 511 correlation equations have been established.

No complete rank-two exclusion remains claimed. “Rank zero excluded” in the separate collective candidate does not remove rank two and does not imply that only ranks 4/6/8 remain.

## 4. Additive repairs for all three f166 MINOR findings

These instructions qualify, rather than edit, `R/frontier-20261028-rank2-coset-exclusion-v1.md`.

**m1 — LF115 (independent hyperplane normals at m=118, Z=12).** The class count is `E_class=4−2κ≥0`, so `κ≤2`. State this before using `2B+4H=6κ−22<0`. The inequality is not valid for κ=4 without the class-count restriction. This repairs the argument at its original m/Z scope only.

**m2 — LF129 (the two e=4 histograms in the `(2,2,4)` case).** Replace the stated reason “fail the U₃ energy or ΣWt=256” by the following joint incompatibilities:
- Histogram `(0,64,0)` does satisfy the s=3 local equations, with `N=(0,40,24,0,0)`. In combination with the s=1,2 class/quadrant counts it gives `B+F=24`, whereas those counts require `B+F=12`.
- Histogram `(48,0,16)` likewise satisfies its s=3 local equations in a family. The combined class equations give `D₁+D₂=κ+B+2H+6`, whereas the s=3 N₂ count gives `D₁+D₂≤3+κ`; nonnegativity contradicts these two statements.

Thus the rejection uses the other slices, U₀ energy and quadrant counts, not a false one-slice energy claim.

**m3 — LF68 (L1).** Only the sums `Σ_c U_j(c)²`, for j=0,1,2,3, are congruent to the number of odd-weight ternary blocks modulo 4. This statement must not be applied to `ΣW(σ)²`, `Σt²` or `ΣW(σ)t` in equation (3). Comparing `ΣU₀²=64−Z` with `ΣU_s²=144−2e_s` yields `2e_s≡Z (mod 4)`. Together with Z≡0 (mod 4), each e_s is even as claimed.

All local lemmas remain at the reviewer's stated conditional scope; this correction does not extend them to the missing m-values by analogy.

## 5. Rank-four consumers: no two-profile or five-profile residual claim

`R/frontier-20261029-rank4-m112-and-profiles-v1.md`, LF10 and LF68–82, used the incomplete ten-pair list. Its claims that “five survive” or that rank four is open **only** in those five pairs are withdrawn. The later informal reduction to only `(14,110)` and `(20,110)` after the fixed-profile searches is likewise withdrawn. The 25-pair coarse roster in §2, not the old ten-pair roster, is the coverage baseline.

Scope separation:
- The conditional m=112 theorem and E=0 block lemmas may be assessed as explicitly quantified fixed-scope claims under z=96, S₄ and their other stated premises. They do not get acceptance from this correction. In particular, the old three D/m pairs at m=112 were not an exhaustive enumeration of that level.
- The odd mod-3 identity and exclusions stated at a fixed `(D,m,S)` are not disproved solely by M1. Their models, normalization, controls and written soundness still require review. They cannot exhaust the unlisted pairs by omission.
- The receipts for `(16,108)`, `(10,108)` and `(8,110)` record only those specific odd-half model searches. Their zero-survivor counts do not imply that rank four, or its |Z|=8 case, is excluded.
- All prior rank-two zero/parity/cubic-residue/D20-plane/shared-cubic tables that imported the three-pair list lose any claim of **global coverage** or global extrema derived from that list. This includes `rank2-zero-divisibility`, `rank2-parity-profile`, `rank2-corrected-parity`, `rank2-cubic-residue`, `rank2-Z8-plane` and `rank2-shared-cubic-barrier` files with the `frontier-20261028-` prefix. Independent local identities keep only their separately justified scopes; earlier withdrawals remain binding.

The original profile checker and JSON, coset checker and JSON, and all consumers are preserved. No success assertion was weakened in code to manufacture a passing check; no checker was rerun.

## 6. Actual dependence disclosure for f183, six-zero, and eight-zero work

**f183 / four-zero, SHA 9227c8fd…cfb.** Its imported structure is f131/f152: rank six and Z=R in the four-zero case, (E8), unequal phases and the translate ρ=0. Its new proof uses the support-moment derivative identity, odd fibre law, class geometry and weighted block energies. It does **not** use the low-rank P1 list or the complete rank-two exclusion. M1 is therefore not itself a disproof of f183. f183 remains frozen, under review and unadopted until Main dispositions it.

**Six-zero, SHA ded2b06d…ae9c.** The separate `|Z|≠6` theorem uses f131/f152, the degree bound (Deg), coset parity (P), and the rank≤4 lower-zero bound. It does **not** use the low-rank P1 list or the alleged rank-two closure. Its combined phrase `|Z|≥8` additionally needs the separate four-zero result, so that composed conclusion remains conditional on f183. The packet stays UNREVIEWED/queued; no variant is issued here.

**Eight-zero computation and private planning.** The C++ enumeration explicitly iterates all zero-XOR eight-sets containing 0, separately for B normal-form ranks 4/6/8, under the full f131 coset-parity necessary condition. This enumerator and its recorded counts do not filter on P1 or D/m. They remain only unreviewed finite necessary-condition evidence, not full Booleanity or an |Z|=8 exclusion.

However, I **did** use the incomplete P1 list privately to plan the rank-four |Z|=8 residual, including treating the old remaining rank-four pairs as exhaustive. That selection/planning and every assertion of global coverage based on it are withdrawn. The later rank-six count-level LP feasibility explorations were explicitly restricted models, not complete-rank claims; they supply no adoption or global exclusion. No profile-based narrowing is carried forward into an eight-zero packet. The parent's instruction to keep that work as one packet remains binding.

The accepted scopes of f131/f152 are not changed by this correction. All historical STOP/HOLD/ZERO/NONINPUT boundaries remain in force.

## 7. Exact source pins and evidence boundary

The following SHA-256 and LF counts were observed by metadata-only hashing/counting before this write. The mathematical census is attributed to the existing reviewer record; it was not re-executed.

| Source under R unless F noted | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 |
| `frontier-20261028-lowrank-valid-profile-check.py` | `77c82174412580278940cb12610bf828f275881d88caad9c82ad9e556edcbb2b` | 98 |
| `frontier-20261028-lowrank-valid-profile-check-result.json` | `71e34280dae3f7843b00ea6ccf948ca53b6fc791997c578779aba319e5910fe6` | 691 |
| `frontier-20261028-rank2-coset-exclusion-v1.md` | `95aecd59e7d1be76731d9cf710f47fd838c82fc749e69d480cc5795b31ecac6f` | 161 |
| `frontier-20261029-rank4-E0-structure-v1.md` | `25b054cdf6eae80fc02771d65206b8c4ea0d89d3ad7442d7af6c4ad4be139797` | 81 |
| `frontier-20261029-rank4-m112-and-profiles-v1.md` | `770c221a8a527f68797a93cb0b0093be1d3f924d3ac506ee5e824c984f2c463e` | 92 |
| `frontier-20261029-fourzero-block-energy-exclusion-v1.md` | `9227c8fd98f7679543a4e780fbd8dc827e097c1783ebead73d1565a678400cfb` | 127 |
| `frontier-20261029-sixzero-exclusion-v1.md` | `ded2b06dee27914c401406a86adf45b78d1cc03a7157e29d541cfe8daab8ae9c` | 71 |
| `frontier-20261029-eightzero-parity-exhaust.cpp` | `d024a5edfb7eafee4b534b3aa8e649d4d0d0a4200b94b5f3886a1acdad01bb1a` | 98 |
| `F/review-v1.md` | `6a3c21c516cefc232aba709fe7bab0a97893a318c29faf2e551f31a04a9dac50` | 284 |
| `F/rv-f166-controls-v1-result.json` | `8bfe045271de0a6c53509e13898b9663aa9acfd5b989d0f3660715b9b5537ded` | 1644 |

Review coverage used for this correction: reviewer LF109–144 and LF197–225, reviewer result key `C_profile_enumeration`, the profile generator LF1–98, original profile/coset/rank-four scope statements and local proof lines, and f183/six-zero/eight-zero dependency declarations. This is not a claim of a fresh full re-audit of every candidate or review line.

**End state.** The coverage error and all three textual minor errors are corrected additively; missing rank-two m=114/116, broader rank-four cases, |Z|≥8, and the original witness-or-unrestricted-exclusion target remain OPEN. No build, lint, test, formatter, solver, scientific run, nested agent, model CLI, Git, deletion or publication was performed for this correction.
