# AME(4,6), N=50 and t=22: same-support flat phases and the integer-kernel criterion

**Status and scope.** This is a fresh, nonblind, same-harness GENERAL AUTHOR reconstruction, not a reviewed or adopted theorem. For one fixed local orthonormal product basis and one common complex tensor, the argument below proves a conditional exact reduction of the `N=50, t=22` branch to actual word-incidence conditions and an integer left-kernel parity condition. It also characterizes all permitted moduli for a fixed incidence support. It does **not** produce a 50-word support or phase witness, prove that any proposed physical incidence exists, exclude this branch, establish any global minimum or bound, or claim novelty, priority, independent model-family, human, kernel, or parent verification. The first unresolved step is the physical-support decision stated in Section 6.

## 1. The actual common object and its 21 squares

Let the four local alphabets each be a fixed six-element set. Let `psi` be a normalized complex AME(4,6) state in one product basis, and set `U=6 psi`. Across each of the three balanced `2|2` cuts the `36 x 36` flattening of `U` is unitary, since the corresponding two-party reduced density matrix is `I_36/36`. Let `N=50`, let `P` be its 22 entries of modulus one, and let `E` be its other 28 nonzero entries. These are **one pair of sets of actual four-coordinate words** with one coefficient per word, used unchanged in all six pair projections and all three cuts.

An entry of modulus one exhausts both its unitary row and its unitary column. Consequently two `P` words cannot have the same value in any physical pair, and no `E` word can share any physical pair value with a `P` word. In any one cut, removing the 22 occupied `P` rows and 22 occupied `P` columns leaves a `14 x 14` unitary whose entries are exactly the 28 entries from `E`. There are no zero residual rows or columns, and no residual row or column has one nonzero: a singleton in a unitary has modulus one and would belong to `P`. Thus all residual row and column degrees are at least two and, because their total is 28, exactly two.

A finite simple bipartite 2-regular graph is a disjoint union of even cycles. A cycle of length greater than four contains two distinct rows sharing exactly one column; their unitary inner product is then one nonzero complex term, a contradiction. Each component is therefore a complete `K_2,2`. There are exactly seven such components per cut and hence **21 cut-indexed squares** in total. Distinct cuts are not deduplicated, even if some of their four-word sets coincide.

Equivalently, in **every** physical pair projection, the `P` values are 22 distinct singletons, the `E` values are 14 distinct values each with exactly two `E` extensions, and these two sets of values are disjoint and cover all 36 pair values. Define `M_ij(w)` as the other `E` word with the same `ij` pair value. It is a fixed-point-free involution on the same 28 words. For complementary pairs `ij|kl`, the two matching involutions commute on each actual square and are different: their common two pair values would otherwise identify the entire word. This is a consequence of physical incidence, not permission to choose six unrelated abstract matchings.

## 2. Arbitrary complex moduli and the flat representative

Write `U_w=sqrt(p_w) z_w` for `w in E`, where `0<p_w<1` and `|z_w|=1`. Every actual `E` pair line has two entries and has squared norm one, so

`p_w + p_{M_ij(w)} = 1` for every physical pair `ij` and every `w in E`.  (1)

Consider one actual square in any cut, with distinct corners ordered as `[[a,b],[c,d]]`. Its row and column squared norms imply `p_a=p_d`, `p_b=p_c`, and `p_a+p_b=1`. All four moduli are nonzero. Its two rows are orthogonal if and only if

`z_a conjugate(z_c) + z_b conjugate(z_d) = 0`,

which, on multiplication by `z_c z_d`, is exactly

`z_a z_d + z_b z_c = 0`.  (2)

The common positive factor `sqrt(p_a p_b)` was cancelled. Equation (2) is a statement about **unit phases**, not a general claim that the unnormalized products `U_a U_d` and `-U_b U_c` are equal: their moduli are `p_a` and `p_b`, which need not agree. Conversely, the displayed norm equations and (2) make the two rows orthonormal; the square is then a unitary `2 x 2` block, including its column conditions.

This proves the same-support flat-representative assertion in both directions. An actual tensor provides phases satisfying (2) on all 21 cut-indexed squares. Retain those phases and replace **every** `E` modulus by `1/sqrt(2)`; retain or independently choose any unit phase at each `P` word. Each `E` square is a unitary complex Hadamard block and each `P` position is an isolated unitary singleton in **every** cut. The three flattenings of this one new `U` are therefore unitary simultaneously. Its squared norm is `22+28/2=36`; dividing by six gives a normalized state, with each two-party reduced density `I_36/36` and hence all smaller marginals maximally mixed. Its support is the identical `P union E`, and the number of unit-modulus coefficients remains exactly 22. Conversely a flat tensor is one of the arbitrary-modulus tensors. No separate choice of phases, support, or local basis is made for different cuts.

There is a slightly fuller characterization for a fixed physical `P,E` satisfying Section 1's incidence conditions. Form a graph on `E`, joining two distinct words whenever they share at least one physical pair value. Equation (1) holds along every edge. On each connected bipartite component one may choose any `p in (0,1)` on one color class and `1-p` on the other; an odd cycle instead forces the entire component to `p=1/2`. Conversely, any such independent component choices satisfy all line norms. Together with a single phase assignment satisfying all (2), they make all square blocks unitary, so these are precisely the possible squared-modulus assignments. This characterization does not assert that any bipartite or nonbipartite component occurs in a physically admissible 28-word support.

## 3. The common 21-by-28 phase system

For fixed actual sets `P,E` with the above incidence properties, order the 28 words once. For **each cut-indexed square**, make one row of an integer matrix `A` by putting `+1` at its diagonal corners `a,d`, `-1` at its off-diagonal corners `b,c`, and zero elsewhere. Thus `A` has 21 rows and 28 columns, with each row having exactly two `+1` and two `-1` entries. Write `z_w=exp(2 pi i theta_w)`, where `theta_w` belongs to `R/Z`. Equation (2) is exactly

`A theta = (1/2) 1_21` in `(R/Z)^21`.  (3)

Exchanging the two rows or the two columns of a square negates its matrix row. Since `-1/2 = 1/2` in `R/Z`, this does not change the phase condition; transposition preserves the two diagonal signs. Reordering words and squares merely permutes columns and rows. Every physical cut-square still contributes its own equation, including repeated four-word sets whose physical corner arrangements may differ.

## 4. Exact integer parity iff, with Smith-normal-form sufficiency

For this actual matrix `A`, (3) has a complex phase solution **if and only if**

`for every y in Z^21 with A^T y = 0, the integer sum_j y_j is even`.  (4)

*Necessity.* Multiply (3) by any integral left-kernel vector `y^T`. The left side is zero in `R/Z`; the right is `(sum_j y_j)/2`. Hence the sum must be even. In particular, one explicit odd-sum vector with the **exact integer equality** `A^T y=0` would be a complete obstruction for this fixed physical support.

*Sufficiency.* Choose unimodular integral matrices `V` and `W` such that `D=V A W` is in Smith normal form. Let its nonzero diagonal entries be `d_1,...,d_r`; all rows below row `r` are zero. The torus transformations induced by `V,W` are invertible. With `theta=W phi`, equation (3) becomes `D phi=(1/2)V 1_21` modulo one. For each `i<=r`, multiplication by the nonzero integer `d_i` is surjective on `R/Z`; explicitly one may choose `phi_i=(V 1_21)_i/(2 d_i)`. The other coordinates of `phi` may be chosen zero. The remaining equations hold exactly when `(V 1_21)_i` is even for every `i>r`.

Those last rows of `V` are an **integral basis** for the integer left kernel, not just a basis over the reals: if `y^T A=0`, then `lambda^T=y^T V^{-1}` is integral and `lambda^T D=0`; nonzero `d_i` force `lambda_i=0` for `i<=r`. Conversely every last row of `V` is a left-kernel vector. Thus the remaining Smith equations hold exactly under (4). This also gives rational phases, and therefore roots of unity: for the chosen `A`, their orders can be taken to divide `lcm(2|d_1|,...,2|d_r|)`. No Smith form or phase vector for any physical 28-word support has been computed here. Row sign changes leave (4) invariant because changing a coordinate's sign does not change its parity.

## 5. Why an odd dependency only modulo two is different

The quantifier in (4) is over the **integral** kernel, not all vectors in `ker_{F_2}(A^T mod 2)`. A mod-two null vector need not lift to an exact integral null vector with the same odd parity. In fact the stronger mod-two condition has its own interpretation: restricting all phases to signs, `z_w in {+1,-1}`, is equivalent to `theta_w=x_w/2` with `x_w in F_2`; equation (3) then becomes `A x=1_21` over `F_2`. By finite-dimensional linear algebra this sign-only system is soluble exactly when every mod-two left-kernel vector has even coordinate sum. Arbitrary complex phases are not restricted to signs.

For an algebraic illustration only, consider the three formal square-shaped rows

```
   1  1 -1 -1  0  0
   1 -1  0  0  1 -1
   0  0  1 -1 -1  1
```

Their all-ones left vector is odd and null modulo two, but the first two column equations force `y_1=y_2=0` for any exact integral left-kernel vector, and the third then forces `y_3=0`. The torus vector `(1/4,1/4,0,0,1/2,0)` gives right-hand side `(1/2,1/2,1/2)` modulo one. Thus a mod-two odd relation can forbid sign phases while complex phases exist. This is **not** a proposed physical `P,E`, not a 21-square matrix, and not a support-50 or AME witness; no claim is made that these three formal rows arise simultaneously from physical words. Its only role is to show that replacing (4) by the stronger mod-two test is not a valid general algebraic inference.

## 6. Exact frontier and import boundary

Combining the previous sections, the following are equivalent:

1. There exists one normalized complex AME(4,6) tensor in the fixed product basis with `N=50` and `t=22`.
2. There exist actual disjoint word sets `P,E subset [6]^4` with `|P|=22`, `|E|=28`, such that each physical pair has 22 distinct `P` values disjoint from exactly 14 `E` values with two `E` extensions apiece, each of the three actual `E` cut graphs is a union of seven `K_2,2`s, and their common 21-by-28 matrix obeys (4).
3. The same conditions hold and the same support has a representative with all `E` moduli `1/sqrt(2)` and arbitrary unit `P` phases, with one simultaneous solution of (3).

For `1 => 2`, actual unitarity supplies the incidence and (4); for `2 => 3`, Smith form supplies common phases and flat blocks; for `3 => 1`, the three block-unitary flattenings give all AME marginals. The `K_2,2` condition is explicitly retained: two extensions per pair value alone only forces 2-regular cut graphs, not automatically square components without the orthogonality argument. Actual words, common `P,E`, all six physical pairs and all three cuts are essential; abstract, independently realized square systems do not suffice.

**Unresolved, exactly:** construct and independently check actual physical `P,E` satisfying the incidence and even integral-kernel condition, or prove that every actual physical `P,E` satisfying the incidence has an odd-sum integral dependency (or is itself impossible). Nothing above decides either alternative. No unprovided support has been treated as a witness; no matrix for a 28-word candidate has been enumerated or solved. Prior N49 dispositions and the conditional 50-to-60 union in the packet are context only; this proof neither requires nor strengthens their global imports.

## 7. Source, control, and process coverage

After Main's direct finalized-receipt notice and before the body, I read the actual dispatch receipt, complete 213-LF manifest, 199-LF freeze receipt, 181-LF final pre-dispatch binding, 212-LF prepared metadata, and all 22 listed controls through their endings. I then sent Main a direct PREBODY ACK naming the 22 controls and the single 250-LF part. After that ACK, I read part 01 serially RAW in windows `1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-160, 161-180, 181-200, 201-220, 221-240, 241-250`, including complete long lines and the ending, before mathematical research or comparison. No sequencing or presentation deviation is known. The supplied target and manifest made this a nonblind duty; no independent cognition or source-identity certificate is claimed.

The parent-declared complete packet-body source pins are:

* S1: `review-waves/f786-ame50-t22-same-complex-tensor-author/author-candidate-v1.md`, LF 1-143, SHA-256 `14c09bbaf27bbf57d77cfd4bba0225c693834a531371ec1c9eb0bc241e01549c`.
* S2: `dispositions/physics-6-conditional-minimum-support-50-to-60-same-tensor-union-parent-v1.md`, LF 1-29, SHA-256 `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0`.
* S3: `dispositions/physics-6-actual-ame49-t28-entire-same-complex-tensor-exclusion-parent-v1.md`, LF 1-29, SHA-256 `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a`.
* S4: `dispositions/physics-6-actual-ame49-t23-through-t27-exclusion-and-t28-frontier-parent-v1.md`, LF 1-31, SHA-256 `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0`.

Here source paths are relative to `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h`. The parent records declare manifest SHA-256 `189e15c992e3eef9d85baf57fc39e52ca936001c843409af3c5a8d06a4273910`, freeze receipt `65dc58bc321b46e9fe641e911d3cd76de55b1b67835bfe5c598c415a835254ca`, final binding `a84baa7b92c60300e0e542e450ca4fba3ea3ce1b72856a5c97ff616680f856c9`, prepared metadata `21e632f4f53c84890d0de5f3235f07a8fb5bfc7caf872548d49dc5fb44a284a8`, and packet part 01 `d3c36d2bf9c1ed8e3eaff5e9f1df74cc81e83b6c7d52779b23ba47ea50f90a86`. These are reported bindings, **not** hashes independently recomputed by this author. The original source paths and transitive links were not opened; the parent receipt, not this return, reports packet roundtrip and persisted-byte checks.

The complete controls, all read for status/permission only, are listed in manifest order below; `W=R/review-waves`, and LF counts are those declared in the manifest:

1. `R/prospective-author-method-scope-restoration-20261030-v1.json` (15).
2. `R/contract-addendum-2-frontier-first-owner-direction-v1.json` (14).
3. `R/parent-L1-selected-diagnostic-release-quarantine-v1.json` (23).
4. `R/parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json` (11).
5. `R/parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json` (9).
6. `R/parent-ame-held-compression-claim-consumer-quarantine-v1.json` (8).
7. `R/parent-held-ph-registration-report-consumer-quarantine-v1.json` (49).
8. `W/f439-depolarizing-ancillary-all-dimensional-repair-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (23).
9. `W/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (16).
10. `W/f448-kac-actual-second-arm-exterior-module-and-character-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (20).
11. `W/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (22).
12. `W/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (22).
13. `W/f586-semigroup-finite-pure-source-free-band-regularity-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (23).
14. `W/f602-olson-deficit-six-protected-triples-independent-actual-word-check/parent-selected-diagnostic-process-major-quarantine-v1.json` (23).
15. `W/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json` (24).
16. `W/f653-sun8-psl2-small-exception-actual-cosets-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
17. `W/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
18. `W/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
19. `W/f660-fresh-original-input-sun8-exceptional-actual-coset-review/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
20. `W/f662-report-v23-werner-core-falsification-documentary-audit/parent-selected-diagnostic-process-major-quarantine-v1.json` (11).
21. `R/parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` (11).
22. `R/parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json` (28).

All genuine held episodes and **every** proof, method, selection, planning, verification, reporting, confidence and downstream consumer remain NONINPUT. No scientific code, solver, test, compile, external CLI, old code, unlisted scientific source, network, Git, installation, or deletion was used. No finite scientific source or support witness was written, and no finite computation was run. The arguments are this author's written reconstruction and require independent scrutiny and parent disposition before any stronger status is attributed.
