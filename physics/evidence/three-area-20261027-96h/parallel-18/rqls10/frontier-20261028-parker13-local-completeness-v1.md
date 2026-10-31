# Parker 13-ray array: exact local completeness of its embedded-unitary family

**NEW AUTHOR CANDIDATE — written proof plus exact finite-field and rational checks; unreviewed.** Actual native `/bin/date` before writing: **Wed Oct 28 17:22:11 PDT 2026**. This is an obstruction in an OPEN NEIGHBORHOOD of ONE fixed labelled order-10 resolution, not an all-L, global, or unrestricted QLS10 no-go. No novelty, formal/kernel, independent-model or mathematical adoption is claimed.

## 1. Statement and actual object

The independently verified actual 10×10 C10 array in `frontier-20261028-parker-13ray-result-v1.json`, SHA256 **0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5**, uses the published Parker 1959 order-10 orthogonal array (source PDF SHA **d00efa7a8e6966af64d4bb4ea7d0accdd33e8e174218b5c54879ca4f3e2f9090**), with original Parker row as color and its other three coordinates as row, column and transversal label. Its 3×3 embedded subarray consists of the nine four-coordinate tuples whose entries all lie in {7,8,9}. Outside that subarray the vector is the standard color basis vector; inside, the three standard basis rays are transformed by

`Q=(1/3)[[1,-2,-2],[-2,1,-2],[-2,-2,1]]=I-(2/3)J`.

`Q^TQ=I`. Every one of the30 required blocks meets the small subarray either in zero cells or in the three distinct embedded colors; hence applying Q on that entire local 3-space preserves every original ONB. The exact integer verifier `frontier-20261028-partial-qls-exact-check-v1.py` SHA **40f201ed11f598afada8091ac59b7fe5865b7d75acd5bf5764b4024550a4ed47** independently checked 100 unit vectors, all30 ONBs and the10 disjoint transversal labels. It counted EXACTLY13 projective ray classes and387 parallel unordered cell pairs. This is an actual 1-resolvable QLS(10), but **not maximal**.

Replace Q by any U in U(3), applied ONLY to those nine cells. The same block argument makes a genuine same-L QLS(10). Around Q, all its three transformed basis rays differ from all ten exterior standard rays, so this family has exactly13 rays. Its equivalence classes modulo a global U(10) and cell phases have local real dimension4.

**Candidate local-completeness theorem.** There is a neighborhood of this particular Q array such that EVERY exact labelled unit-vector array with the SAME30 row/column/transversal ONB constraints is, after one global unitary and per-cell phases, a member of the above embedded U(3) family. Therefore every such nearby array has13 rays and there is no maximal-cardinality array in that neighborhood.

This is a precise local obstruction. The radius is not computed; no claim is made about other incidences, distant components, singular solutions outside the neighborhood or unrestricted order10.

## 2. Exact linearization and independently checked rank

The array is real, so write an arbitrary infinitesimal perturbation at cell x as `delta_x=a_x+i b_x` with real vectors a_x,b_x. The linearized original constraints are:

- norms: `v_x·a_x=0` for every cell x;
- for every unordered x,y in each original block, real part `v_y·a_x+v_x·a_y=0` and imaginary part `v_x·b_y-v_y·b_x=0`.

Thus there are1000 real variables in each sector,100 norm rows and1350 within-block pairs, with NO relaxation to an abstract scalar Gram matrix. The exact generator `frontier-20261028-tangent-matrix-v1.py` SHA **3ac0f54ae7df9ff157f75a67dc960e2b194ff20864b070803426bdae3b52db39** wrote the original ungauged integer systems. The first attempted v1 matrix header had an incorrect column count and was rejected with `invalid sparse entry`; the corrected v2 filenames and this chronology are preserved in the earlier interim record `frontier-20261028-parker13-tangent-frontier-v1.md` SHA **f4d26f020e9db259d45824d05e9ec06e47f4529a124423ec34ca5b14aac87c68**. The following ranks use ONLY corrected v2 matrices.

Gauge the first ONB to the standard reference basis by a common unitary, and align the phase of each of the other90 vectors with its own reference vector. At the linear level add zero variation for all100 real and100 imaginary first-row coordinates, and `v_x·b_x=0` on the other90 cells. There remains a two-real-dimensional diagonal-unitary freedom on the embedded3-space; at cell(7,7), whose numerator vector is `(0,...,0,1,-2,-2)`, additionally impose `b_(7,7;7)=b_(7,7;8)=0`.

Exact generated matrices:

- real gauge:1550×1000, `frontier-20261028-parker13-tangent-real-gauge-v1.txt`, SHA **6c544d04942f27e957b655ca5576de3fb476934a766a5571bdbe1ecca1bf283e**;
- imaginary gauge:1542×1000, `frontier-20261028-parker13-tangent-imag-gauge-v1.txt`, SHA **ceb2b3e2dddcac7673abd7dc1813373dde1c326589d60d5210507df4719ce3ba**.

The gauge writer `frontier-20261028-gauge-tangent-v1.py` SHA **b0f9474230c59d35ae6c27b1ada74f3b88e69d0e01c3eee25f3381a17934b08f** builds them. An independently written row-by-row assembly audit `frontier-20261028-tangent-assembly-audit-v1.py` SHA **68703f267ffd30dcfc1fc52dc9b894760c8ed2ce5043383b9d213e861b6908be** rederived every original norm/orthogonality/gauge row directly from the actual vector/label certificate. Actual output:

```text
real independent assembly audit: PASS 1550 rows x 1000 columns
imag independent assembly audit: PASS 1542 rows x 1000 columns
PASS every original norm/30-block orthogonality derivative and stated gauge row
```

Exact elimination modulo the prime65521 was run in TWO independently implemented ways: C++ dense elimination `frontier-20261028-modnull-v1.cpp` SHA **d0e578d5153b31a8579a3fba74d199fca91a659bd21843b9ec31bb3236f1fcbc**, and Python sparse-dictionary elimination `frontier-20261028-sparse-modrank-v1.py` SHA **d71202329a1a580edcdf0b68c036bb802d9c22c0b99178bda6112768e72c38f2**. Both output:

```text
real gauge: prime 65521 rank 997 nullity 3
imag gauge: prime 65521 rank 999 nullity 1
```

The Python checker also independently tests primality by integer trial division to sqrt(p). A rank over F_p is a LOWER bound on rank over Q/R, so it gives gauge-nullity AT MOST3 real and AT MOST1 imaginary. It does NOT by itself prove a matching lower bound.

For that lower bound the modular bases were rationally reconstructed and checked over EXACT Q against EVERY gauge row by `frontier-20261028-rational-null-check-v1.py` SHA **2a6d0aa7ce060473be86496bd4f0ff6768328d340cb196c44110f062416d66e3**. The complete rational vectors are:

- real3: `frontier-20261028-parker13-null-real-rational-v1.json`, SHA **15ae8810b81d05e758c36c91d29a0191f2a5e3f3400079a02183e5b1b6c96370**;
- imaginary1: `frontier-20261028-parker13-null-imag-rational-v1.json`, SHA **03dc09102322701ce990b1b344b4339515423d115841f739711945850b95fb5c**.

A second checker `frontier-20261028-tangent-direct-check-v1.py`, SHA **0d6a9f9e206a28acfe3a1248994d55bbdea84b163fbb102608e6fd529d3b8f54**, never reads the generated matrices. It checks those four vectors directly against the actual original norms,30 block inner-product derivatives and gauges. All pass exactly; the three real free coordinates989,998,999 form the identity, and the imaginary vector has free coordinate989 equal1. Hence the four are independent. Consequently the characteristic-zero gauge-fixed tangent dimension is **EXACTLY4**, with real3 and imaginary1, not merely modular evidence. These vectors are infinitesimal; exact nonlinear local completeness is justified separately below.

## 3. Why the gauge removes every global/phase orbit direction

At the reference, the first row consists of the ten unrotated standard rays. If a global skew-Hermitian infinitesimal K plus per-cell phase variations has zero first-row variation, K must be diagonal imaginary after choosing the first-row phase changes. The per-cell phase conditions for the remaining cells eliminate their own scalar phases relative to the reference. On the seven one-dimensional standard color directions, the remaining global diagonal phases act trivially on rays. On the embedded3-space let their imaginary parameters be t7,t8,t9.

At the rotated cell(7,7), whose three coordinates are all nonzero, the phase-aligned variation has component proportional to `t_j - sum_k |v_k|^2 t_k`. Setting its imaginary components7 and8 to zero forces t7=t8=the weighted average; since the third weight is nonzero, also t9 equals it. The common scalar acts trivially on all three rays. Thus the two extra gauge conditions kill precisely the residual nontrivial global diagonal orbit and the gauge slice has no nonzero global-unitary/per-cell-phase tangent.

For actual arrays sufficiently near the reference, first align their first ONB exactly by a common unitary, choose the90 cell phases continuously to make each reference inner product positive real, and then use the two residual diagonal phase differences. The derivative of the last two conditions in those differences has rank2 by the argument above; the ordinary implicit function theorem gives the required nearby finite gauge choice. No change of resolution, rank or physical state space is made.

## 4. The embedded U(3) family exhausts the four tangent directions

At Q the U(3) family has real dimension9. Per-cell phases identify right multiplication by a diagonal3-torus; global diagonal phases on the original exterior standard rays identify left multiplication by a diagonal3-torus. Their infinitesimal stabilizer intersection at Q has real dimension1: if `diag(t)Q=Q diag(s)`, all nine entries of Q are nonzero, so all t_i and s_j are equal. The combined left/right torus orbit has dimension5; the local quotient therefore has real dimension `9-5=4`.

These four are genuine variations of ACTUAL arrays, because every U in this family preserves all30 bases exactly. They are nonzero and independent modulo global/cell phases by the stabilizer calculation. The gauge-slice construction in §3 maps them to four independent tangent directions; §2 proves that the entire gauge-fixed tangent space has dimension4. Therefore its full tangent is exactly the tangent of this concrete family. It is not legitimate to infer local completeness from a tangent equality alone; the next paragraph pays that step.

## 5. Full local nonlinear conclusion via the implicit function theorem

Consider the original real-analytic norm and block-inner-product equations together with the gauge conditions of §2. Their derivative at the reference has rank `997+999=1996` in2000 real variables, by the independent modular lower bounds and exact rational nullspace upper bounds. Select1996 independent real equations. The implicit function theorem makes their common zero set, near the reference, a smooth real4-dimensional manifold M. Every fully feasible gauge-fixed array is in M, but the selected equations alone need not globally imply all omitted equations.

The actual embedded-U(3) family, after the local gauge of §3, is a smooth4-dimensional family of FULL solutions contained in M; at the reference its tangent equals T(M). Its local parameter map therefore has invertible derivative into M, and the inverse function theorem gives a neighborhood in M entirely covered by this family. Any exact feasible solution sufficiently near the reference is in M and hence in that family. This proves local completeness; it does NOT claim a global parameterization or use numerical convergence as a proof.

Near Q the three local transformed rays cannot coincide with the exterior standard rays by continuity of their nonzero overlap pattern, and they remain mutually orthogonal. Thus all arrays in the resulting smaller neighborhood have exactly the seven outside-color rays, the three exterior embedded-color rays and three new embedded rays: **13 in total**, not100. The full target remains open elsewhere.

## 6. Complementary switch criterion and remaining work

For any classical reference from orthogonal Latin squares A,L, a pair of colors a,b defines a graph whose edges pair their cells in each of the three partitions. If every pair graph is connected, the earlier written proof `frontier-20261028-classical-rigidity-and-search-v1.md` SHA **3dc1eea8fdb47c04c39dea1d0a8a85122680db29b3d8c3fdea6c7ce05f712f24** proves local classical rigidity up to the same symmetries. Conversely, if some pair graph has at least two components, choose different sufficiently small 2×2 unitary rotations on different components: each block contains either both paired colors in the SAME component or neither, so every basis stays exact. Distinct component rotations give more than n rays arbitrarily near the reference. Hence connectedness of ALL pair graphs is also NECESSARY for local classical rigidity. This is an independently checkable structural criterion, not an assertion that every OLS(10) has connected pair graphs.

The bounded exact component-switch search from the Parker12-ray seed found13 rays after one switch and no further eligible closed pair switch on that seed in its six restarts: code `frontier-20261028-exact-switch-grow-v1.py` SHA **60c7338ed9cde7fd03c42caaf554a3f4215587fae4dc7e1d0634077a18250c81**, result `frontier-20261028-exact-switch-grow-result-v1.json` SHA **2023d098dc9c81b437b698601ed8709161794b7434934f83abc2f4219a6dcb6e**. An independent integer verifier confirmed its separate13-ray result. That finite search is NOT an exhaustive theorem about every possible nonlocal switch and is not the source of the local completeness proof.

Open next: actual maximal-cardinality QLS10 may lie far from these specific reference arrays or use another L. A physically valid100-ray solution needs every original constraint and all4950 nonparallel pairs independently checked with exact/rigorous certification. No such solution or universal obstruction is delivered. Local theorem, field-rank code and gauge/IFT application require independent review before adoption; past held outputs are not premises. The full PH7 f8 disjoint review has already been returned; no external model or source contact was used in this construction.

**END — exact local13-ray family completeness candidate, not global QLS10 resolution.**
