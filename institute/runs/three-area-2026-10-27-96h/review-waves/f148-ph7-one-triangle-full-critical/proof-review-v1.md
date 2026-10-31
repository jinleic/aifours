# f148 proof review: PH7 at z=8/9, one directed triangle, no 2-/4-cycle

Native clock observed before writing: **2026-10-28T21:44:24-0700 PDT** (2026-10-29T04:44:24Z). Same-harness independent scientific review (manifest `manifest-v1.json`, SHA-256 `a30381bbdf9a0a8722122243450e9ee608f7f197948ecef30ee333fb38496f8f`, 3674 bytes). Reviewer wrote only `proof-review-v1.md`, `proof-review-v1-exact-controls.py`, `proof-review-v1-exact-controls-log.txt` and `proof-review-v1-exact-controls-log-run1-reviewer-expectation-bug.txt` in this directory. No author checker or replay was imported or executed; the author certificate JSON was opened as data only. No author contact, web search, external model, Git, deletion or publication.

## Scoped verdict

**0 FATAL / 0 MAJOR / 1 MINOR** for the written argument at the frozen scope, **conditional on the imported positivity certificate** (dependency C below). The reconstructed theorem is:

> **Theorem (scope).** Let `G` be a real 7×7 Metzler matrix that is irreducible with spectral bound `s(G)=0`. Let `Γ` be its digraph (arc `i→j`, `i≠j`, iff `g_ij>0`). If `Γ` has no directed 2-cycle, exactly one directed 3-cycle and no directed 4-cycle — arcs and cycles of length ≥5 arbitrary, overlapping or not — then `D(y)=y[(y+1)²+8/9]²` does not divide `χ_G(y)=det(yI−G)`.
>
> **PH consequence (under import I).** No phase-type representation of `H` with at most seven states at `z=b²/(a−c)²=8/9` has a generator graph in this class.

Load-bearing dependencies, each named at its use:

* **I** — import disposition `math-1-ph7-global-irreducibility-eight-edges-parent-v1.md` (SHA-256 `42ae3d99…281`): any ≤7-state PH representation at `z>1/2` has exactly seven states, strongly connected generator graph, characteristic polynomial containing `−c` and `−a±ib` with at least multiplicities 1 and 2, and spectral bound **at most** `−c` (so, after `G=(T+cI)/d`, at most 0). Used only for the PH consequence.
* **C** — strict positivity of the four five-rate polynomials `b0, b1, b3, 4b1b3−3b2²` on `(0,∞)^5`. **Imported, not established here.** Source: the separate certificate audit `certificate-review-v1.md` in this directory (SHA-256 observed `17dad81ecd56c97595770fc1ecffc75de9728ada250d74d3ae176e2ec9e220c5`), which reports 0/0/0 after an own-engine replay of all 2311 leaves (its receipts `certificate-exact-check-v1.py` `290f72c0…598`, `certificate-results-v1.json` `80b6b702…327`, `certificate-cubic-coefficients-v1.json` `04f2afb2…052`, hashes observed, engine not executed by me). This review independently derived the four polynomials from first principles and found **identical canonical digests, term counts and individual degrees** to the author certificate records, parsed the complete cover structure, and spot-checked 12 leaves with its own exact de Casteljau; those are consistency checks, **not** a universality proof from samples.
* **E** — ordinary mathematics: Perron–Frobenius for irreducible Metzler matrices (the spectral bound is a simple real eigenvalue with a strictly positive eigenvector), the permutation/cycle-family expansion of a determinant, Cramer's rule, the cubic Bernstein basis, and 2×2 positive definiteness.

What this review is not: not a human, independent-family, formal/kernel or novelty verification; not a global PH7 exclusion; not an adoption of any graph-edge classification or of the manuscript's section-1 cross-source corollary (12 of 14 eight-edge shapes), which depends on separately frozen sources outside this manifest.

## Frozen inputs (all verified before reading, in manifest order)

| Input | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `dispositions/math-1-ph7-global-irreducibility-eight-edges-parent-v1.md` | `42ae3d996ffb7f46cc5ad72a0d18f3eae665290f8d7901e994ac7776a6b4d281` | 6427 | 31 |
| `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md` | `2e30b352597880b78bfc59baa3adead91e4d4f0f1717a8cf7f684cee0a92decc` | 7612 | 102 |
| `frontier-20261028-ph7-one-triangle-full-critical-check.py` (read/hash only) | `dd323a51986972808cdcc209bbc2df58b81214072c2ec760480546c04996a6d3` | 4147 | 77 |
| `frontier-20261028-ph7-one-triangle-full-critical-certificate.json` | `d1195a6f0099d105eb34e5a6acbeb1fec3d81c333658af7a3c8b2ea5ac79f2c9` | 51575 | 2377 |
| `frontier-20261028-ph7-one-triangle-full-critical-integer-replay.py` (read/hash only) | `7c20fce389e2b87f4e4df3d9ac31f33bb62b40e8fcd19cb3e53f982fc13b7536` | 5483 | 128 |

All text bodies were read completely; the certificate's four records were parsed in full (metadata, digests, degrees, term counts, every leaf path).

## Reconstructed proof

Notation: `u_i=−g_ii>0` escape rates; triangle `1→2→3→1` with rates `u1,u2,u3` and arc product `w=g12 g23 g31`; `u4,u5` any two of the four outside vertices, `O=u4+u5`; `v1,v2` the remaining two, `t=v1+v2`, `r=v1v2`; `s_k=e_k(u1,…,u5)`.

**Step 0 — PH caller bridge (MINOR M1).** Import I gives spectral bound of `T` at most `−c`. Since `−c` is a pole of `H(s)=α(sI−T)^{-1}t`, it is an eigenvalue of `T`; the spectral bound of a Metzler matrix is its largest real eigenvalue, hence equals `−c` exactly, and is simple by irreducibility. Therefore `G=(T+cI)/d` is irreducible Metzler with `s(G)=0`, and `D | χ_G` (roots `0`, `−1±i√(8/9)` with multiplicities ≥1, ≥2 by I). The manuscript states "spectral bound 0" as given; the import literally gives "at most 0", so this one-line bridge is needed and is supplied here. The spectral theorem itself needs no bridge.

**Step 1 — Perron normalization and `θ`.** Let `v>0` be the right Perron vector, `Gv=0`, and `G'=Δ^{-1}GΔ`, `Δ=diag(v)`. Then `G'` has the same diagonal, the same digraph, the same cycle arc-products (telescoping `v_j/v_i`) and the same `χ`; and `G'𝟙=Δ^{-1}Gv=0`, i.e. zero row sums. Hence `u_i=Σ_{j≠i}g'_ij>0` (each row has an out-arc by irreducibility, `n=7≥2`), so **all seven diagonal rates are positive** without assumption. Each triangle arc is at most its row sum: `g'_12≤u1`, `g'_23≤u2`, `g'_31≤u3`, giving `w=θu1u2u3` with `0<θ≤1`. In fact `θ<1`: `θ=1` forces rows 1–3 to have no other out-arcs, so `{1,2,3}` would be closed, contradicting strong connectivity. The manuscript's `(0,1]` is a harmless superset; the certificate covers `[0,1]`.

**Step 2 — Actual characteristic coefficients.** With `M=yI−G'`, the permutation expansion of `det M` groups each permutation into fixed points and disjoint cycles: a fixed point `i` contributes `(y+u_i)`; a directed cycle `C` of length `L` contributes sign `(−1)^{L−1}` times `∏(−g')=(−1)^L w_C`, i.e. `−w_C`. Thus

`χ(y)=Σ_F ∏_{C∈F}(−w_C) ∏_{i∉V(F)}(y+u_i)`, sum over families `F` of pairwise vertex-disjoint simple directed cycles (`F=∅` included).

In the class every cycle has length 3 (exactly one) or ≥5; two disjoint cycles need ≥8>7 vertices. So the only families are `∅` (degree 7), `{Δ}` (degree 4) and single long cycles (degree ≤2). Therefore

`[y^6]=e1(u)`, `[y^5]=e2(u)`, `[y^4]=e3(u)−w`, `[y^3]=e4(u)−w·e1(u outside Δ)=e4−w(O+t)`.

Where each hypothesis is used: *no 2-cycle* removes the only other degree-5 family and — because a 2-cycle's term `−w₂∏_{5 others}(y+u_i)` also feeds `y^4` and `y^3` — is needed for all three lower equations (control B.7 shows one added 2-cycle shifts `y^5,y^4,y^3` by exactly `−w₂e_{0,1,2}(others)`); *exactly one 3-cycle* fixes the single `−w` at `y^4` and `−w e1(out)` at `y^3` (a second triangle shifts both, B.7); *no 4-cycle* removes the only other degree-3 family (B.7). Long cycles, overlaps and extra arcs only touch degrees ≤2 and are unrestricted. The `y^2,y^1,y^0` identities are deliberately unused; an impossibility proof needs only necessary conditions.

**Step 3 — Reduction to five rates plus `(t,r)`.** `e_k(u1..u5,v1,v2)=s_k+t s_{k−1}+r s_{k−2}` (A.0, symbolic). `D` is real monic of degree 5 and divides the real monic `χ`, so `χ=D·Q` with `Q=y²+py+q` real — no sign of `q`, no numerator identity and no assumption on the hidden roots (coincidence with roots of `D` allowed). With `D=y^5+4y^4+(70/9)y^3+(68/9)y^2+(289/81)y` (A.2), coefficient matching gives exactly the manuscript's `p=s1+t−4`, `q=s2+ts1+r−4p−70/9`, and `E4=E3=0` as displayed in (EQ) (A.3). Both are affine in `(t,r)` (A.4) with closed forms derived by hand and confirmed symbolically (A.5):

```
a00 = s2 − 4 s1 + 74/9            a01 = s1 − 4
a10 = s3 − w − (70/9) s1 + 212/9  a11 = s2 − 70/9
c0  = s3 − 4 s2 + (74/9) s1 − 28/3 − w
c1  = s4 − w O − (70/9) s2 + (212/9) s1 − 1007/27
```

`den=a00a11−a01a10`, `tn=−c0a11+a01c1`, `rn=−a00c1+c0a10` satisfy the Cramer identities `a00tn+a01rn=−c0den`, `a10tn+a11rn=−c1den` (A.6). Their `θ`-degrees are 1, 1, 2, so `N=−19683(tn²−4rn·den)` is a cubic in `θ`, free of `t,r` (A.6); `19683=3^9` is the smallest power of 3 making all four Bernstein coefficients integers (with `3^8` they are not; A.7 info line).

**Step 4 — Bernstein identity and the 2×2 criterion.** With `b_k=Σ_{j≤k} C(k,j)/C(3,j)·n_j` from the power coefficients `n_j`, the identity `N=b0(1−θ)³+3b1θ(1−θ)²+3b2θ²(1−θ)+b3θ³` holds as a polynomial identity (A.7), with `b0=N(0)`, `b3=N(1)`. Writing `N=b0(1−θ)³+θ·B(θ)`, `B(θ)=3b1(1−θ)²+3b2θ(1−θ)+b3θ²` is the quadratic form of `S=[[3b1,3b2/2],[3b2/2,b3]]` on the vector `(1−θ,θ)`, and `det S=(3/4)(4b1b3−3b2²)` (A.7). Under C, `3b1>0` and `det S>0`, so `S` is positive definite and `B(θ)>0` for every real `θ` (the vector `(1−θ,θ)` is never zero). For `θ∈[0,1]`, `b0(1−θ)³≥0` and `θB(θ)≥0` with at least one strict, so `N(θ)>0` on all of `[0,1]`; at the endpoints `N(0)=b0>0`, `N(1)=b3>0`. The sign of `b2` is not needed (control C.6 positive case); the criterion is not vacuous (C.6 negative case: `(1,1,−2,1)` has `b0,b1,b3>0` yet `N(1/2)<0`). `b3>0` is implied by `b1>0` and `4b1b3>3b2²≥0`; the certificate's separate `b3` record is redundant but harmless.

**Step 5 — Case analysis and conclusion.** Fix the hypothetical matrix: positive `u1..u5`, `θ∈(0,1)`, real `t,r` with `E4=E3=0`.
* `den≠0` (either sign): Cramer forces `t=tn/den`, `r=rn/den`, and `t²−4r=(tn²−4rn·den)/den²=−N/(19683den²)<0` by C. But `t²−4r=(v1−v2)²≥0` for the actual real rates `v1,v2`. Contradiction. (Only `den²>0` is used; in all 160 sampled points `den>0`, but the sign is irrelevant.)
* `den=0`: by definition `N=−19683tn²≤0`, contradicting `N>0`. So under C, `den=0` cannot occur at any positive rates and `θ∈[0,1]` — the zero-denominator case is vacuous rather than merely handled; no division is performed.
* Endpoints: `θ=0` (no triangle weight; not attained) and `θ=1` (excluded by irreducibility) are nonetheless covered by `b0>0`, `b3>0`.
* Hidden roots: never constrained; the argument uses only that `Q` is real.

Hence `D∤χ` for every matrix in the class, and under I no ≤7-state PH representation at `z=8/9` has such a graph. □

The pointwise identity `t²−4r=−N/(19683den²)` and the equality of the symbolic `E4,E3` with the actual `y^4,y^3` coefficient defects of `χ` against `D·Q` were confirmed on exact rational 7×7 generators drawn from the class (Part B).

## Independent controls actually executed

Script `proof-review-v1-exact-controls.py` (reviewer-written, standard library only, exact `Fraction` arithmetic; SHA-256 `477b154385ffdb8e3ccd1fb504a79bcff835dce07202236ecf943e2cd11fddbf`, 37088 bytes). Accepted run: start `2026-10-29T04:41:18Z`, end `2026-10-29T04:43:14Z`, monotonic 115.8 s, Python 3.14.3 arm64, **194 PASS / 0 FAIL**, log `proof-review-v1-exact-controls-log.txt` SHA-256 `1c3671ba4460cd669dfb398b8b3a206cb14d666fb354ac0b43acde1ebd4d0244`.

Run history, preserved: run 1 (script SHA-256 `d620e9c4…b71`, start `04:37:56Z`, 82.99 s, log `…-log-run1-reviewer-expectation-bug.txt` SHA-256 `dbbfb2f5…04a`) failed exactly one line, `B.7/2cycle`, because the reviewer's expected delta omitted the added 2-cycle's fixed-point product on `y^4,y^3`; the expectation was generalized to `−w_C e_{7−L−d}(outside C)` and everything else was byte-identical in effect. This was a reviewer-control bug, not an author defect; it is the reason the no-2-cycle hypothesis is recorded above as load-bearing for all three lower equations.

* **A (symbolic, ring `ℚ[u0..u4,θ,t,r]`)**: A.0 elementary-symmetric split; A.2 `D` from `z=8/9`; A.3 `p,q,E4,E3` from first principles equal (EQ); A.4 affinity; A.5 all six closed forms; A.6 Cramer identities, `θ`-degrees `(1,1,2)`, `N` cubic and free of `t,r`, side identity `den−a11²=(s1−4)(−4a11−a10)`; A.7 (BERN), `b0=N(0)`, `b3=N(1)`, integrality, `det S=(3/4)G`, `N=b0(1−θ)³+θB`; A.8 term counts `1753,1753,1717,31422`, symmetry in `(u1,u2,u3)` and `(u4,u5)`; A.9 intended-failure digest controls (`z=1`; dropping the `−wt` term) both change the digests. Reviewer digests: `b0 7c1ebd08…f69e`, `b1 88dcb154…24c7`, `b3 35f6c146…072e`, `G e6231a6a…0d07` — identical to the certificate records — and `b2 638eb1e3…6079` (1747 terms), not pinned by the author but identical to the value the separate certificate audit reports.
* **B (exact rational matrices)**: six seeded strongly connected class graphs (8–11 arcs; cycle-length histograms containing 5-, 6- and 7-cycles, e.g. `{3:1,5:1,6:2,7:1}`), each with a row generator and a non-generator Metzler matrix: Faddeev–LeVerrier `χ` == full cycle-family expansion == direct determinant at a random point; `y^6..y^3` == `e1, e2, e3−w, e4−w(O+t)`; `χ(0)=0` and `θ=w/(u1u2u3)∈(0,1)` for generators (e.g. `33/83`, `53/131`); symbolic `E4,E3` at the matrix point == actual coefficient defects; `t²−4r=−N/(19683den²)` at the point; `D∤χ`. Negative controls (graph#1 + one arc): added 2-cycle shifts `y^5,y^4,y^3` by `(−609/4, −65453/8, −2110417/14)` = `−w₂e_{0,1,2}`; added 4-cycle shifts `y^3` by `−11760=−w₄`; added second triangle shifts `y^4,y^3` by `(−9204, −3624842/7)=−w′(1, e1(out))`; all three exactly as predicted.
* **C (exact points)**: 40 random rate tuples × `θ∈{0,1,random,random}`: pointwise `den,tn,rn,N`, Cramer solution satisfies (EQ), `t²−4r` identity, Bernstein identity, endpoints; observed `den>0` in 160/160, no `den`-root in `[0,1]` for any tuple, `N>0` and `(b0,b1,b3,G)>0` in 160/160; extreme sweep of 1071 points over rates `10^{-6}…10^{6}` (all seven equal-rate diagonals included) × `θ∈{0,1/2,1}`: `N>0` throughout. **These samples are not universality evidence; universality is dependency C.** Cubic negative/positive controls and the bracket-positivity grid as described in Step 4.
* **D (certificate data parse)**: SHA/bytes/LF; metadata (`z=8/9`, `θ∈[0,1]`, `u=x/(1−x)`, split axis = depth mod 5, identity string = (BERN)); per record: digest/terms/degrees equal reviewer values; 657/567/522/565 leaves (2311), binary, distinct, prefix-free, Kraft sum 1, every internal node has both children (complete cover of `[0,1]^5`), minimum depth 5 (each axis split ≥1), every leaf box has an open-cube corner and side lengths ≤1/2.
* **E (bounded spot check, sample only)**: first/middle/last leaf of each record with the reviewer's own exact Bernstein root array `a_β/∏C(d_i,β_i)` (the compactification maps monomials to the Bernstein basis) and exact midpoint de Casteljau: all 12 leaves have nonnegative coefficients and strictly positive open-cube corners, corner coefficient equals the compactified value; the root arrays contain 781/781/771/14741 negative entries (subdivision genuinely needed); negating the `b0` constant term makes the first `b0` leaf fail.

Open-boundary inference (checked as written mathematics, not just data): for `x∈(0,1)^5` in a closed leaf box, choose per coordinate the box endpoint equal to `x_i` when `x_i` sits on it (that endpoint is then globally interior), else any globally interior endpoint (exists since every side is ≤1/2); the resulting corner is open-cube, its coefficient is `>0`, its tensor basis weight at `x` is `>0`, and all other coefficients are `≥0`; hence strict positivity holds on shared faces as well as box interiors, and transfers to `(0,∞)^5` through the positive factor `∏(1−x_i)^{d_i}`.

## Findings

* **MINOR M1 (presentational, PH caller).** The manuscript takes "spectral bound 0 after shift/scale" from the import, whose text gives only "at most" `−c`/`0`. The equality — needed for the Perron-vector diagonal similarity to a zero-row-sum generator, hence for `θ≤1` — follows from `−c` being a pole and so an eigenvalue of `T` (Step 0). Supplying this sentence closes the gap; nothing else changes.

Observations (not defects, not adopted as results):
* O1. Irreducibility gives `θ<1` strictly; `(0,1]` and the `[0,1]` certificate domain are supersets. `θ=0` corresponds to no triangle at all; the same equations with `w=0` would make `b0>0` alone bear on girth-≥5 graphs — **not claimed by the author, not reviewed, not adopted here**; it would need its own frozen scope.
* O2. Under C, `N>0` forces `rn·den>0`, so `den=0` is vacuous; the manuscript's separate den=0 sentence is correct and complete.
* O3. The author's "two independent integer implementations" are both author-written in one harness and the replay consumes the certificate's leaf lists; the manuscript itself qualifies this. The present review and the separate certificate audit add two further same-harness implementations, which is still not human, cross-family, formal or novelty verification.
* O4. Section 1, paragraph 3 (12 of 14 eight-edge theta shapes excluded) rests on separately frozen sources not in this manifest; it is outside this review's scope and is not adopted.

## Boundaries

Established at scope: the written argument from (actual coefficients) → (five rates, `t,r`) → (cubic `N`) → (Bernstein/PD) → (contradiction) is exact and complete, with dependencies I, C, E as named. Not established here: dependency C itself (imported from the certificate audit), any graph with a 2-cycle, several triangles or a 4-cycle, PH7 existence or minimum order at `8/9`, any edge-count classification, and novelty/priority.
