# Two unrestricted local factors: an exact 56-term orbit support floor

Owner **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:54:55 PDT 2026`**; not exact creation/completion/runtime. **WRITTEN proof with two independently structured exact finite-field computations, author candidate; not yet independent scientific review, formal/kernel verification or novelty clearance.**

## 1. Scope and precise statement

Let T be the SPECIFIC real 60-term AME(4,6) tensor from [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1), in its published product basis. The separately transcribed exact coefficient table `frontier-20261028-pandya-table-v1.txt` has SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`; two differently structured local checkers verified its normalization and all SIX physical two-party marginals, as recorded in `frontier-20261028-two-party-orbit-obstruction-v1.md` SHA256 `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`.

At each party set `H=span{|1>,|2>}`, `K=span{|0>,|3>,|4>,|5>}`. Choose ANY two parties as free; apply arbitrary complex GL(6) maps there. At the other two parties apply arbitrary block-diagonal `GL(H)⊕GL(K)` maps. Then the transformed tensor has **at least56** nonzero coefficients in that product basis.

For physical unitaries the state remains AME. Consequently any state in THIS particular LU orbit with support≤55 must have at least THREE local factors whose image of H is not a coordinate 2-plane: if at least two images were coordinate 2-planes, output monomial permutations would bring them back to H and this theorem would apply. This is only a necessary condition in one orbit. It does NOT prove that56 is attainable, that59 is unattainable, or any lower bound for other AME states/global minimum.

## 2. Four disjoint sectors after two parties are fixed

Call the unrestricted parties A,B and the H/K-preserving parties C,D. Their actual output coordinate supports split into the four disjoint C/D sectors `KK, HK, KH, HH`. The source table has only the all-K sector P of12 terms and six sectors E_ij of8 terms where parties i,j lie in H.

- `KK` contains P plus E_AB, exactly20 source terms. Its verified maximum 2|2 flattening rank is20.
- `HH` contains E_CD, exactly8 source terms, with verified 2|2 flattening rank8.
- `HK` contains E_AC+E_BC, exactly16 source terms.
- `KH` contains E_AD+E_BD, exactly16 source terms.

All statements are for the SAME tensor, with the ordered choices of A,B,C,D arbitrary. The first two ranks were independently verified modulo17 (with `sqrt2↦6`), so the corresponding characteristic-zero ranks are at least20 and8. Their actual source term counts give matching upper bounds. Arbitrary invertible local maps preserve each sector's chosen flattening rank; hence the output KK sector has at least20 nonzeros and HH at least8.

The two mixed sectors are harder: ordinary 2|2 flattenings only give12 each. The exact projective certificate below gives14 each, uniformly in ALL complex local transformations, not merely a sampled H basis.

## 3. A 6×6×4 Koszul rank lower bound

Consider the source HK sector. Fix an output H coordinate of party C after its arbitrary invertible 2×2 transformation. Its coefficient tensor, before the other three local maps, is a nonzero contraction

`T_(λ,μ)=λ T_(C=1)+μ T_(C=2) ∈ C^6_A⊗C^6_B⊗C^4_D`,

for some `(λ,μ)≠(0,0)`. Since the row of an invertible 2×2 matrix is nonzero, this covers every possible output H slice. Arbitrary GL(6) maps on A/B and GL(4) on D act invertibly on this same three-tensor, so any valid tensor-rank lower bound survives them.

Define the wedge-one flattening

`F_T: A⊗B* → Λ²A⊗D`,

`v⊗β ↦ sum_(a,b,d) T_abd β(e_b) (e_a∧v)⊗e_d`.

It is a `60×36` matrix. For a rank-one tensor `a⊗b⊗d`, this map has rank at most `dim(A)−1=5`, since `v↦a∧v` has kernel `span(a)`. By subadditivity of matrix rank, a tensor written as r product terms satisfies `rank(F_T)≤5r`. Hence

`rank(F_T)≥31  ⇒  tensor-rank(T)≥ceil(31/5)=7`.

Every nonzero product-basis coefficient is one product term. Therefore if rank≥31 for **every** nonzero `(λ,μ)`, each of C's two output H slices has at least7 coefficients, and the HK sector has at least14. The analogous argument applies to KH. Wedge maps transform equivariantly by invertible factors under GL(A)×GL(B)×GL(D), so the bound survives the actual free-party and K maps.

## 4. Uniform projective rank certificate — not a finite sample argument

For EACH ordered case `(free pair A,B; H party C; K party D)`, form `F(λ,μ)=λF_0+μF_1` directly from the published 16 signed-unit coefficients in that mixed sector. There are 12 such cases: six free pairs times the two H/K orientations of the other parties. All pencil entries are in `Z[λ,μ]`; the `sqrt2` P coefficients do not occur in these mixed sectors.

If the complex matrix F had rank<31 at some projective point `[λ:μ]`, EVERY 31×31 minor would vanish there. The finite certificate selects several actual 31×31 minors `F_j(λ,μ)` and forms TWO homogeneous degree31 integer polynomials:

`f=F_0`,  `g=sum_j w_j F_j`, with explicit integer weights `w_j`.

Its exact 62×62 homogeneous Sylvester determinant/resultant is NONZERO modulo the prime257. The resultant is an integer polynomial in the coefficients of f and g; a nonzero residue implies that integer is nonzero. A nonzero homogeneous resultant implies that f and g have no common zero in complex projective 1-space. Thus F has rank≥31 at EVERY nonzero complex `(λ,μ)`. No enumeration of field points is substituted for this characteristic-zero conclusion.

**Certificate checking.** A 31×31 determinant of a linear pencil has degree≤31. For each selected minor, an independent implementation directly evaluated the determinant at **32** distinct field values and compared them to the recorded coefficients; equality at32 points fixes the entire degree≤31 polynomial over F_257. It also checked the homogeneous leading coefficient against the direct `F_1` minor (the infinity point). It recomputed each 62×62 Sylvester determinant and checked it is the nonzero recorded residue. Therefore the recorded resultant is tied to ACTUAL source matrices and minor row/column indices, not just to arbitrary polynomial strings.

The exact independent receipt verifies **12/12** ordered cases and **74** individual minors. Its resultant residues, by free pair and H orientation, are:

| Free parties (zero-based) | H party | K party | Resultant mod257 |
| --- | ---: | ---: | ---: |
| 0,1 | 2 | 3 | 1 |
| 0,1 | 3 | 2 | 1 |
| 0,2 | 1 | 3 | 17 |
| 0,2 | 3 | 1 | 1 |
| 0,3 | 1 | 2 | 128 |
| 0,3 | 2 | 1 | 241 |
| 1,2 | 0 | 3 | 141 |
| 1,2 | 3 | 0 | 251 |
| 1,3 | 0 | 2 | 1 |
| 1,3 | 2 | 0 | 241 |
| 2,3 | 0 | 1 | 53 |
| 2,3 | 1 | 0 | 1 |

For example, the `(A,B;C,D)=(0,1;2,3)` case has five explicit minors, weights `(0,1,1,1,1)` for g, and resultant1. The full row/column indices, 257-coefficient polynomials and weights for every case are in the pinned certificate; no source body is reconstructed from the above summary alone.

## 5. Resulting two-free-party support bound

For each of the two mixed sectors, §3–4 force both output H slices to have at least7 nonzeros, hence sector support≥14. Together with the two pure-sector flattening ranks,

`support(output) ≥ 20 + 14 + 14 + 8 = 56`.

All four sectors are disjoint in the output coordinates of C,D; free-party mixing does not merge those H/K labels. The source identity has support60, so this theorem leaves at most the range56–60 for this restricted orbit and does NOT claim a 56-state exists. It strictly extends the previous exact60 floor when THREE parties preserve H/K: now TWO of the four parties are fully unrestricted, at the cost of a weaker56 lower bound.

## 6. Reproducible artifacts, controls and assurance

| Artifact | SHA256 | Actual scope |
| --- | --- | --- |
| `frontier-20261028-mixed-sector-koszul-minors-v1.py` | `760fb196be6d42c1874146267510b6884b6cbb152d2fb0412fde4b2dddbe822c` | Constructs source Koszul pencils and exact F_257 minor polynomials. |
| `frontier-20261028-mixed-sector-multiminor-v1.py` | `385b476f173b15a15c5f66b16d862ee60d5fb9cb27a13963129a0d6ee149d0df` | First bounded individual/multi-minor selector; certified only6/12, NOT a universal result. |
| `frontier-20261028-mixed-sector-multiminor-v1.json` | `0ac480a8f5c56b2a95114bc428d9f10e48df421f3f0510f347f4668f3b2e5a21` | Preserves the six unresolved cases of that bounded search, not six counterexamples. |
| `frontier-20261028-mixed-sector-multiminor-v2.py` | `0c84533caa5dc065d8add7b04ab7e5e5dee102f0217030e4909ba8b1f7fe43c5` | Seeded pivot shuffles select additional exact minors; no success is inferred from random trials. |
| `frontier-20261028-mixed-sector-multiminor-v2.json` | `7a3dbb611f660e3b7d2582693a3be146cecd42db1147949768bf6a75bb45d88f` | Explicit12-case minors/weights/polynomials and nonzero mod257 homogeneous resultants. |
| `frontier-20261028-mixed-sector-certificate-independent-v1.py` | `ac7be2263be41531c8cf6cc4dc4e492575fb8795c8ded1053b26a55803f97c68` | Separate parser/pencil/field-elimination implementation, NumPy int64 only. |
| `frontier-20261028-mixed-sector-certificate-independent-v1.json` | `25ee9b2959e3c7f6dd2d106c11dc13b48011b958e066e134be01e01a625bc40d` | Replays74 minor polynomials at32 points+∞; all12 resultants and six pure-sector rank pairs; polynomial-coefficient mutation rejected at t=0. |

Both determinant implementations operate modulo257 with bounded integer intermediates; the independent verifier uses NumPy2.4.3 integer arrays, not floating-point arithmetic. A separate resultant calibration gave nonzero residue256 for `(λ^31,μ^31)` and zero for `(λ^31,λ μ^30)`. The first selection strategy's six failures remain honest bounded-search failures; the successful successor adds actual new pivot/minor certificates, not an inference from those failures.

The primary paper reports a 38–60 global support gap, but its classical lower-bound input was not independently reconstructed in this work. No independent scientific referee, formal/kernel verification, worldwide source/novelty conclusion, actual support56 tensor or improved all-AME bound is claimed. A disjoint reviewer should independently reconstruct the resultant lift and check the full certificate before adoption.
