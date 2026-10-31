# Independent written review: both unrestricted Pandya orbit families

Observed native clock immediately before this review write: `2026-10-28T18:23:40-0700 PDT`. This is a pre-write observation, not a completion time. Reviewer: `AMEFullOrbitProofReview`, a same-harness reviewer; no author or peer was consulted before the verdict. This review is not a parent disposition.

## Verdict and findings

**Source:** the pinned table's 36 ordered cells, including the two signed terms or the single √2 term, match the selected public Table 1 MathML alttext; both P and P′ match all six public Eq. (6) quartets. The source artifact contains only the specified HTML excerpts, not a whole-page byte hash. Separately written exact checks establish the color/Pauli, Gram, parity, support-mask and algebra facts stated below. See the evidence and limitations; no author checker was imported.

**Complex and mathematical verdict:** I reconstructed the argument for all complex local invertible maps and arbitrary unit phases on **either** specified parity face. Subject to the explicitly listed source/computational assumptions, I found **FATAL 0, MAJOR 0, MINOR 1**. The mathematical inference to support minimum 60 in each of these particular complete GL(6,C)^4 orbits is supported by the reconstruction below. This is not a parent adoption, cross-model or human review, formal/kernel verification, or a novelty determination.

**m1 — make two implicit coherences explicit (nonblocking exposition).** Base §§4, 6–7 should explicitly say (a) *the very same* globally chosen `φ_i` gives `η_i = conjugate(φ_i,H)/sqrt(h_i)` on every pair, rather than allowing independent pairwise choices of conjugation, and (b) U being unitary excludes **zero**, not merely rank-one, two-covector contractions, including mixed covectors. The first follows from equality for the same four-party product vector on every oriented cut; the second from `||U(a⊗b)||=||a|| ||b||`. Neither requires changing the claim. The derivation below incorporates both points.

## Frozen scope and evidence

All manifest inputs were read completely in the stated order. SHA-256 and actual size/LF, checked before the exact structural run:

| Input | SHA-256 | Bytes; LF |
|---|---|---|
| `manifest-v1.json` | `58bc6ef69b3bba96616a5a96e19b64d685590380482d537f749c617df0e0661a` | manifest |
| `frontier-20261028-pandya-table-v1.txt` | `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38` | 523; 38 |
| `frontier-20261028-unrestricted-orbit-60-barrier-v1.md` | `d21c734fa2830bf20e7330e118f03d3e1367f1794815c82162075c7df6dac251` | 15939; 146 |
| `frontier-20261028-two-face-unrestricted-orbit-60-v1.md` | `8af3381ec64c50d7e9f17e485e1c91093be35fa9057ad2829de66474e41af5cf` | 6683; 44 |

Public source: [Pandya arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673v1#S2.T1) and [Eq. (6)](https://arxiv.org/html/2610.16673v1#S4.E6). I read the displayed table and equation, then captured the raw HTML line ranges 290–356 and 592–625 as `public-source-excerpts-v1.json`, SHA-256 `7e0a6b5b23e7af5d1a6fe0ff78a0493b1983326acf03abf6ba1e616c55dfdd19`. Those are selected textual ranges, excluding each last line delimiter; they are **not** a hash of the complete HTTP response. `source-checker-v1.py`, SHA-256 `9a1f8b687fab23f565d3533ecd7453d43ffe88a73932d575feccc920323a6c5d`, parsed the public MathML alttext and compared all 36 ordered cells to the pinned table. It compared P from the table with Eq. (6)'s first three quartets and the extension's ordered P′ list with its last three quartets. Intended-failure controls changed the sign of 0012 and P′ tuple 0353→0354 and were rejected for the respective source mismatches. `source-receipt-v1.json`, SHA-256 `8aa83896652de638abd56362f59b474744784a4229475a51ab73aecf6923feea`, records native pre-write clock `2026-10-28T18:21:53-0700 PDT`.

The independent standard-library `checker-v1.py`, SHA-256 `51e09c93c2499c43295b3443ef26c418f03529feacf25684eacb9ca22b9f65ab`, reads the hashed inputs, not the author's certificate code. Its `receipt-v1.json`, SHA-256 `0696642a6e626f6b1c3961e691aea66259cee32ceff632db9a5e065d09bcf7aa`, records native pre-write clock `2026-10-28T18:19:39-0700 PDT`. It checked all six signed-Pauli block families, the even/odd tuples, each 12×12 monomial support, and both integer row and column E Gram matrices (2592 entries per cut, 7776 total). It enumerated all 15^4 nonempty support masks **for each parity**, finding exactly the claimed 17; checked the seven propagation steps, the 16-vertex/72-edge connectivity graph for each parity, all four invertible anticommuting Pauli triples and the Bloch conjugation signs. Deleted-P, flipped-E-sign and three-hit-mask controls failed for the intended reasons. These finite exact checks validate finite premises, not a proof over C by sampling.

## 1. Fixed tensor, both parity faces, and all-cut isometry

Write H=span{|1>,|2>} and K=span{|0>,|3>,|4>,|5>} for every party, and use the four party-dependent physical-K→color bijections from the pinned base proof. They map P to the 12 even permutations and the public P′ to the 12 odd permutations of 0,1,2,3. The 48 E coefficients have exactly two H indices. For any active H pair i,j and color g on both spectators, the 2×2 active coefficient matrix `Q_ij,g` is one of ±I, ±X, ±Z, ±J, with each type appearing once. Here `J=ZX=[[0,1],[-1,0]]`; transposition only changes its sign. There are no other H-counts.

For either S=P or S=P′ and any twelve real phases, set

`T = (sum_(x in E) ε_x |x> + sqrt(2) sum_(x in S) exp(i θ_x)|x>)/sqrt(72)`.

Every displayed coefficient is nonzero, so the initial support is 48+12=60 and the squared norm is `(48+2·12)/72=1`. In any 2|2 flattening F of the unnormalized tensor, the 12 P/P′ entries occupy precisely the K,K **unequal-color** rows and columns, one per row and column; the remaining 24 rows and columns support E only. The exact E Gram checks give `E E†=2 I` on that sector. Thus the P/P′ sector is a disjoint √2-times unitary monomial for **every** independent phase choice, and `F F†=2 I_36` for all three cuts. The reverse orientation has flattening `F^T`, also unitary after scaling. Hence `U=F/sqrt(2)=6 T_flat` is unitary in either orientation. Each 2-party reduction of normalized T is I/36, so every specified source tensor is AME; this statement is not transferred to general nonunitary orbit outputs.

## 2. Rank one implies one coherent product saturator on all cuts

Fix a cut CB|AD and nonzero covectors `λ_C, μ_B`. Normalize both in the Euclidean norm; use their coefficient columns without additional conjugation for contraction. If the resulting AD matrix has rank one, `w=U(λ_C⊗μ_B)` is a rank-one 6×6 matrix of norm 1. Factor it as `φ_A⊗φ_D` with **both** local factors normalized, absorbing the phase, and set `φ_C=conjugate(λ_C)`, `φ_B=conjugate(μ_B)`. Then `φ=⊗_i φ_i` is one normalized product vector and

`<φ,T> = (φ_A⊗φ_D)† U (conjugate(φ_C)⊗conjugate(φ_B))/6 = 1/6`

up to an irrelevant global phase. The unnormalized tensor contraction has norm √2, the normalized-T contraction has norm 1/6, and the U output has norm 1. The input product on any cut is the product of **conjugates** of those same φ factors.

For any other oriented cut ij|kl, with kl on the output side, the scalar `6<φ,T> = (φ_k⊗φ_l)† U_kl|ij (conjugate(φ_i)⊗conjugate(φ_j))` has modulus 1. Both arguments of the inner product are unit vectors. Equality in Cauchy–Schwarz therefore gives a phase `ω_ij` such that

`U_kl|ij (conjugate(φ_i)⊗conjugate(φ_j)) = ω_ij (φ_k⊗φ_l)`.

Consequently, every contraction by the corresponding covectors `conjugate(φ_i),conjugate(φ_j)` has rank one. No pairwise re-selection of φ or its conjugations is permissible or needed. Moreover U's injectivity means a contraction by any two nonzero covectors is never zero, irrespective of whether either covector is pure or mixed.

## 3. Pure-sector rank bounds and consequence for a saturator

Let a C covector be pure H. For B covector `u=(u_H,u_K)`, the AD matrix has H/K blocks `[[0,X],[Y,Z]]`. If `u_K≠0`, any nonzero spectator-color coordinate selects a nonzero column of X and nonzero row of Y: each is an invertible Pauli applied to the nonzero C spinor, multiplied by the same nonzero K coordinate. A minor using the zero HH corner equals `-XY≠0`, even if `u_H` makes Z nonzero. If `u_K=0`, only Z remains, diagonal in four matched spectator colors, with entries `u_H^T Q_g λ_C`. At least two are nonzero: if three vanished, their three nonzero `Q_g λ_C` would all lie in the one-dimensional kernel of `u_H^T`. After inverting one Q, the other two give a common nonzero eigenvector of two invertible anticommuting matrices, impossible over C. Thus every nonzero B contraction has rank ≥2.

Now let C be pure K, `t≠0`. If `u_H≠0`, pick g with `t_g≠0`. The A-H/D-K and A-K/D-H blocks have nonzero entries at the D-K column g and A-K row g, respectively. The A-K/D-K entry at `(g,g)` is zero: neither even nor odd P uses a repeated color, and E has the wrong number of H indices. The resulting minor `[[F_ab,X],[Y,0]]` is `-XY≠0`; F is allowed to be nonzero and u may be mixed.

If B is also pure K, the AD matrix is block diagonal. Its HH block is `sum_g t_g u_g Q_g`. Linear independence of the four signed Pauli types gives vanishing HH block iff `t_g u_g=0` for each g. The KK block has one, and only one, term per unequal C,B color pair, at distinct output positions, with a nonzero unit phase; it vanishes exactly when all `t_g u_h=0` for g≠h. In that zero-KK case nonzero t,u must be the same singleton, and the HH block is an invertible nonzero scalar times Q_g, hence rank 2. Otherwise a rank-one matrix must have zero HH block. For any fixed g in supp(t), every such B covector is in `{u_H=0,u_g=0}`, a three-dimensional subspace. Thus across any B basis: all six ranks are nonzero, at most three are 1, and their sum is ≥9.

If a rank-one contraction has C mixed, the saturator above has φ_C mixed. Every φ_i participates in a rank-one contraction with every other: no φ_i can be pure H by the first bound, and if any φ_i were pure K, the second bound would force **all** other φ_j pure K, contradicting mixed φ_C. Hence mixed rank one would imply that the same φ has all four H and K projections nonzero. We rule that out next.

## 4. Nonnegative probability cases, including zeros

Let `h_i=||φ_i,H||²>0` and `p_i(g)=|φ_i,K,g|²≥0`, with `h_i+sum_g p_i(g)=1`; each support `S_i={g:p_i(g)>0}` is nonempty. Take any source parity tuple `(g_0,g_1,g_2,g_3)` and set `x_i=p_i(g_i)`. In the product equality on any cut, a distinct-color output has exactly one input from the monomial P/P′ sector, modulus 1, and no E contribution. Therefore, for every bipartition,

`x_i x_j = x_k x_l`.                                                   (A)

For four nonnegative x, the three equations imply either all four are positive and equal, or at most one is positive. For example, two or three positives make some pairing product positive and another zero; with four positives, dividing the equalities forces all four equal. Thus no parity tuple meets exactly two or three S_i.

The only admissible nonempty masks are (i) four copies of one singleton, (ii) four distinct singletons making a tuple in the chosen parity class, or (iii) all four colors at every party. A written propagation independent of enumeration is as follows. If no two parties contain different colors, all supports are the same singleton. Otherwise 2-transitivity of the parity class supplies a tuple through two different supported colors, and (A) forces its other two colors into their supports. For the even class, simultaneously relabel positions and colors to make that tuple `(0,1,2,3)`. If an extra color occurs, simultaneously relabel further so party 0 also has color 1. The seven even tuples

`(1,3,2,0), (1,2,0,3), (3,2,1,0), (3,1,0,2), (2,3,0,1), (2,0,1,3), (2,1,3,0)`

successively have at least two known supported entries and force the rest; their pre-step counts are `2,2,2,3,2,3,3`, ending with all supports full. With no extra entry one has the distinct-singleton case. Interchanging two positions takes odd permutations to even permutations, preserving the mask rule and equality of spectator colors, so the same classification holds on P′.

For any output HH pair i,j, only the matched K,K input products at colors g contribute. The four `Q_ij,g` are Hilbert–Schmidt orthogonal, `tr(Q_g† Q_h)=2 δ_gh`; each normalized U coefficient is `Q_g/sqrt(2)`. Taking the squared Frobenius norm of that HH output gives

`h_i h_j = (1/2) sum_(g,h) conjugate(a_g) a_h tr(Q_g† Q_h) = sum_g p_k(g) p_l(g)`,   (B)

where `a_g=conjugate(φ_k,g) conjugate(φ_l,g)` and `{i,j,k,l}` are distinct. The coefficient is exactly **1**, not 1/2, after the Pauli norm 2 is included.

If all four supports are distinct singletons in one source tuple, the right-hand side of (B) is zero, contrary to `h_i h_j>0`. If all four supports are the same singleton g, (B) yields `h_i h_j=p_k(g)p_l(g)`. But the matched `(g,g)` output receives only the HH input via `Q_ij,g/sqrt(2)` and Cauchy–Schwarz gives `p_k(g)p_l(g)≤h_i h_j/2`, also impossible. Thus every S_i is full.

With full support (A) makes all four probabilities on each parity tuple equal. Any two entries from distinct parties and distinct colors occur in a tuple of either parity; their 16-vertex co-occurrence graph is connected (indeed, any remaining pair can be joined through an entry of a third party and a third color). All sixteen probabilities are one p>0. Then (B) gives `h_i h_j=4p²` for all pairs; positivity forces each `h_i=2p`. Normalization `h_i+4p=1` gives `p=1/6`, `h_i=1/3` for each party.

## 5. Same global spinors and the Bloch contradiction

For every pair i,j choose **once**, from the global φ of §2,

`η_i = conjugate(φ_i,H)/sqrt(h_i)`, a normalized two-component spinor.

In the opposite pair k,l, the equal-color output `(g,g)` comes only from the input HH block `Q_ij,g/sqrt(2)`; no P/P′ term has equal colors. Consequently,

`p_k(g)p_l(g) = (h_i h_j/2) |η_i^T Q_ij,g η_j|²`.

Substituting the values above yields `|η_i^T Q η_j|²=1/2` for every pair i≠j and each Q in I,X,Z,J, irrespective of their color-dependent order, signs, or transpose. These are the **same four η_i for all six pairs**; the cut-dependent phase cancels in modulus.

For each i let r_i be the real unit Bloch vector of `η_i η_i†=(I+r_i·σ)/2`. Since `η_i^T Q η_j = <conjugate(η_i), Qη_j>`, conjugation sends `(r_x,r_y,r_z)` to `(r_x,-r_y,r_z)`. The corresponding Pauli density identity gives

`2|η_i^T Qη_j|² - 1 = H_Q · (r_ix r_jx, -r_iy r_jy, r_iz r_jz)`,

where the rows for Q=I,X,Z,J are respectively `+++`, `+--`, `--+`, `-+-`. The row-sign matrix satisfies `H^T H=4I`. Thus all three coordinate products `r_ia r_ja` vanish for each distinct pair and each axis a. The supports of four nonzero vectors r_i would be four pairwise disjoint nonempty subsets of the three coordinate axes, impossible. This excludes every all-mixed saturator, and hence every mixed-C rank-one contraction over C. Together with §3 and nonzero contractions, every non-pure-K C covector has rank ≥2 against every nonzero B covector.

## 6. Arbitrary local bases and the exact minimum

For arbitrary `V_i∈GL(6,C)`, fix C,B. Their six output-coordinate covectors form bases of the corresponding dual spaces. At most four of the six C covectors lie in the four-dimensional pure-K subspace. For each such C covector, the six B-slice ranks sum to at least 9; for every other C covector the sum is at least 12. If k≤4 are pure K, the 36 slice ranks sum to at least `9k+12(6-k)=72-3k≥60`. The V_A and V_D maps are invertible and preserve the rank of each AD matrix; each matrix has at least rank many nonzero entries, and different CB slices are disjoint. Hence the transformed tensor has support ≥60. The identity maps leave exactly 60 nonzero entries, so the minimum in **each** of the two specified arbitrary-phase complete GL(6,C)^4 orbits is exactly 60. LU maps are a subcase and also attain 60 at the source.

## 7. Remaining assumptions and excluded claims

The conclusions rely on the pinned table and extension bytes, faithful public HTML MathML alttext for the selected source passages, correctness of the explicitly retained source/structural checkers and execution environment, the displayed phase normalization and standard finite-dimensional complex linear/Hilbert-space algebra, and invertibility of all four local maps. The finite claims can be replayed from the hashed inputs, excerpts, and programs; the numerical/finite-mask runs do not establish the universal complex implication by themselves. No author's finite-field search, earlier one-restricted-case review, cross-harness review, uninspected literature classification, or external model was assumed.

This review does **not** prove a support lower bound for every AME(4,6) state, address states outside these explicitly parameterized families and their orbits, establish orbit inequivalence or classification, determine the global support minimum, establish priority/novelty, provide human or proof-assistant certification, or confer parent adoption. The companion finite/source review and parent integration remain separate obligations; this review reports only its own reconstruction and exact checks.
