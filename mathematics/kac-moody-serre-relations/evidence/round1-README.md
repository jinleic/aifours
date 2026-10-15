# Defining relations of nonsymmetrizable Kac–Moody algebras

**The full book conjecture remains unsolved in this dossier.** The work below gives a proved infinite boundary family, an exact graded comparison algorithm, and bounded rational computations; none is substituted for the universal goal. No novelty claim is made for consequences of established symmetrizable theory.

## Source

- **Book:** 《10000个科学难题·数学卷》 (*10000 Selected Problems in Sciences: Mathematics*), Science Press, 2009.
- **Problem:** 非可对称化的卡茨–穆迪 (Kac-Moody) 代数的定义关系问题 — *Problem on Defining Relations of Non-symmetrizable Kac-Moody Algebras*.
- **Author:** 苏育才 (Yucai Su), University of Science and Technology of China.
- **Printed pp.226–227; PDF pp.242–243.** Exact excerpt: [`sources/book-excerpt.txt`](sources/book-excerpt.txt).
- Extraction command from the workspace root:

  ```sh
  pdftotext -layout -f 242 -l 243 "/Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf" ai4s/kac-moody-serre-relations/sources/book-excerpt.txt
  ```

This target replaced the scope-ambiguous inverse-optimization intake and the subsequently superseded Seymour intake. Their evidence was preserved, not deleted; the shared index is parent-owned.

## Problem

The goal is **Conjecture 1 for every generalized Cartan matrix**, not merely finding some defining presentation, not a quantum-specialization question, not a positive-characteristic group simplicity question, and not a finite-height computation.

Starting from the preliminary contragredient Lie algebra with Chevalley/Cartan relations, there are two quotients: the explicit Serre quotient S(A), and the quotient g(A) by the unique maximal ideal meeting the Cartan subalgebra trivially. The conjecture asserts that these coincide for every A. They are known to coincide for symmetrizable A. Some sources call S(A) itself “the Kac–Moody algebra”; this dossier always distinguishes the two constructions.

## Status as of 2026-10-14

### (a) Verbatim book statement and faithful translation

> 猜想 1 对任意广义 Cartan 矩阵 A, Serre 关系是 Kac-Moody 代数 g(A) 的定义关系.

**English:** “Conjecture 1. For every generalized Cartan matrix A, the Serre relations are defining relations of the Kac–Moody algebra g(A).” Here g(A) is the book's maximal-Cartan-disjoint-ideal quotient, defined immediately before the conjecture; “Serre relations” includes its displayed Chevalley/Cartan relations (1) and the positive/negative relations (2). See excerpt lines 12–34.

### (b) Dated primary status evidence and current search boundary

**Current label: uncertified-open.** The exact question is explicitly reported open in dated primary literature, and a search through 2026-10-14 found no resolution. A negative search is **not a proof of current openness**.

- **Most explicit modern statement opened:** Robert Theodore Williams Jr., *Commutator Formulas in Groups of Kac-Moody Type*, thesis, August 2022, DOI [10.18130/t9v1-vz61](https://doi.org/10.18130/t9v1-vz61), printed p.49 / PDF p.55, after Definition 6.1.5: “They coincide in (at least) the case that A is a symmetrizable matrix … but it is not known if they always coincide or if there is a GCM A for which they do not.” The preceding text explicitly identifies the two quotients. Full PDF opened and saved as `sources/williams-thesis-2022.pdf`; text lines 2079–2098.
- **Later fresh discussion:** Timothée Marquis, [arXiv:2309.02508](https://arxiv.org/abs/2309.02508), September 5, 2023, §6.2 “Open questions”, p.11: for characteristic zero and A not necessarily symmetrizable, the group GK-simplicity question is equivalent to proving the Gabber–Kac theorem for A. The notes use the Serre-defined algebra and state that theorem only for symmetrizable A. This is the equivalent open formulation, not a positive-characteristic counterexample.
- **Latest posting found with an explicit conjectural statement:** Guy Rousseau, [arXiv:2508.08728](https://arxiv.org/abs/2508.08728), posted August 12, 2025, §6.5, PDF p.54: “En caractéristique 0, g_k est GK-simple dans le cas symétrisable (et même conjecturalement dans tous les cas).” Translation: in characteristic zero, g_k is GK-simple in the symmetrizable case, and conjecturally in all cases. **Important date caveat:** the PDF itself is dated May 12, 2015 and is a repost of the 2016 article [DOI 10.24033/bsmf.2724](https://doi.org/10.24033/bsmf.2724), with an erratum. This is not presented as a new 2025 assessment.
- **Published supporting context:** Marquis, *Ann. Inst. Fourier* 69(6) (2019), [DOI 10.5802/aif.3301](https://doi.org/10.5802/aif.3301), p.2523, calls the characteristic-zero nonsymmetrizable Lie problem “completely open.” Gorelik–Hinich–Serganova (2024), [DOI 10.5802/art.13](https://doi.org/10.5802/art.13), distinguishes the exact two constructions in §1.1.3 and leaves the indefinite nonsymmetrizable case outside its equality theorem. Its broader root-superalgebra question is not silently identified with every quantifier of the book conjecture.

Search evidence: [`evidence/status-search-20261014.json`](evidence/status-search-20261014.json), with separate access limits and a citing-work audit in the source ledger. Parent reported no matching family for this topic in the local `openai/math` clone `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, the remote listing on 2026-10-14, or the Sra arXiv:2608.29595 screen. This negative corpus screen is recorded as parent-reported evidence, not as a mathematical openness certificate.

### (c) Fully formal target and fixed experiment model

For every n>=1 and every integer matrix A with a_ii=2, a_ij<=0 for i!=j, and a_ij=0 iff a_ji=0, let ell=rank A. Over **C**, take the book's full realization: a rank-n matrix C with 2n-ell rows whose first n rows are A, independent Cartan generators h_1,...,h_(2n-ell), and

    [e_i,f_j]=delta_ij h_i,  [h_p,h_q]=0,
    [h_p,e_i]=c_pi e_i,     [h_p,f_i]=-c_pi f_i.

Let tau be the maximal ideal of this preliminary algebra with tau intersect h=0. Let J be the ideal generated by (ad e_i)^(1-a_ij)e_j and (ad f_i)^(1-a_ij)f_j for all i!=j. **The full target is J=tau for every such A and full realization.** The extra Cartan directions cannot be discarded when A is singular.

Computations use the positive free Lie algebra over Q, root-lattice multidegrees, total height, the fixed alphabet e_1<e_2<e_3 and standard Lyndon bracketing by the longest proper Lyndon suffix. D_i=[f_i,.] uses **row i** of A and D_i e_j=-delta_ij h_i. K_ei=0 is a separate boundary condition. The recurrence depends only on the rows A, and its interpretation is valid for every full realization; no arbitrary completion of a singular A is substituted for the Cartan-disjoint condition. Characteristic-zero extension Q→C preserves these finite dimensions. Prime-field runs are diagnostic and are never labeled characteristic-zero counterexamples.

Fixed inputs, written before computation: [`work/matrices.json`](work/matrices.json). The deeper height-12 scope was recorded in [`evidence/height12-scope.json`](evidence/height12-scope.json) before that run.

## State of the art

1. **Symmetrizable case:** Gabber–Kac is established. Every rank-two GCM is symmetrizable, and so is a GCM whose underlying graph is a forest, by consistent diagonal ratios along edges. Nonsymmetrizability first requires an unbalanced cycle; rank three is the smallest possible rank. These observations are not new nonsymmetrizable cases of the conjecture.
2. **No all-height nonsymmetrizable case established by the opened literature:** the source audit found no proof for a nonsymmetrizable matrix over C and no characteristic-zero counterexample. This is a bounded search finding, not a theorem that no such paper exists. Hyperbolic classification, low rank, and restrictions on a_ij a_ji alone must not be promoted to a Gabber–Kac result.
3. **Marquis's group counterexamples have the wrong characteristic for this problem:** [arXiv:1509.01976](https://arxiv.org/abs/1509.01976), published 2019, gives non-GK-simple group examples over finite fields. Its characteristic-zero Lie theorem remains conditional on symmetrizability. In §2.7 the example involving sl_m(k) and p dividing m is likewise not over C.
4. **Kumar's geometry does not settle this conjecture:** Heckenberger–Kolb, [arXiv:math/0605460](https://arxiv.org/abs/math/0605460), [DOI 10.1007/s00031-007-0059-2](https://doi.org/10.1007/s00031-007-0059-2), Theorem 3.2, cites exactness of Kumar's BGG complex ending in the maximal integrable quotient V(mu). The same page states that simplicity of V(mu) is unknown for arbitrary Kac–Moody algebras. Exactness is not a proof that V(mu) is the simple module. The book calls the representation conjecture closely related; no unverified two-way equivalence is used here.
5. **Quantum and super cases are not replacements:** [arXiv:1303.5994](https://arxiv.org/abs/1303.5994) is by **Xin Fang**, not Berenstein–Greenstein. Its defining Nichols ideals and failed specializations do not refute the classical Serre conjecture. Gorelik–Hinich–Serganova's gl(1|1), sl(n|n), sq(n) and other superalgebra exceptions have parity hypotheses absent from the book's ordinary Lie algebra problem.

Primary snapshots and hashes are in `sources/` and [`evidence/source-downloads.json`](evidence/source-downloads.json). Failed HTML responses are identified as unusable, not counted as read papers.

## Attack

### Exact algorithm and proof of its meaning

[`proof.md`](proof.md) proves, without assuming the conjecture, that the positive maximal ideal is obtained recursively by

    K_ei=0,
    K_alpha={x in L_alpha : D_i x in K_(alpha-ei) for all i}.

It also proves the exact Serre-ideal recurrence from the original generators plus [e_i,I_(alpha-ei)]. Thus dim L_alpha/I_alpha and dim L_alpha/K_alpha are genuinely different constructions being compared, not two labels for one quotient. The code does not use a symmetrizable root-multiplicity formula for a nonsymmetrizable input.

The producer, [`work/graded_lie.py`](work/graded_lie.py), uses recursive bracket lowering. The separate checker, [`work/check_certificate.py`](work/check_certificate.py), imports no producer code and computes lowering by an independently derived associative-word deletion formula, followed by independently reconstructed coordinates. It regenerates exact Serre spans and checks injectivity on their quotients, which proves I=K inductively; a nonzero-defect certificate is explicitly refused rather than mislabeled an equality pass. The height, matrix set, and entries are bound to an external requested scope and fixed specification. Six negative controls test field, missing degree, changed dimension, omitted matrix, altered matrix, and height. A finite-field rank match alone is not the accepted evidence; the exact-Q certificate and independent checker are the acceptance path.

### Proved infinite boundary family

**If deleting one index i leaves a symmetrizable principal GCM, then I_alpha=K_alpha in every degree with alpha_i=1.** The proof constructs a symmetrizable comparison matrix preserving the entire coefficient-one Serre slice and every complementary lowering, then uses its nondegenerate opposite-root pairing. It does not assume the full nonsymmetrizable algebra has an invariant symmetric form.

For rank three this excludes **every** degree with a zero or one coordinate, at all heights. The structural proof alone gives equality through height five and leaves (2,2,2) as the first candidate. The separate symbolic certificate below excludes that candidate uniformly as well, proving equality through height six for every rank-three GCM. An independently derived all-(m,1,1) calculation and the full coefficient-one proof are preserved in [`evidence/descent-audit.md`](evidence/descent-audit.md). These are bounded or boundary results; novelty has not been established.

A first extra relation must also be annihilated by every lowering. Integrable sl2 theory then gives the necessary condition A alpha<=0. This directs the remaining attack to interior imaginary degrees, not already-excluded boundary degrees.

### Bounded exact computations

The three genuinely nonsymmetrizable input matrices are

    A_one   = [[2,-1,-1],[-1,2,-1],[-2,-1,2]],
    A_cycle = [[2,-1,-2],[-2,2,-1],[-1,-2,2]],
    A_large = [[2,-2,-2],[-3,2,-2],[-2,-3,2]].

Their absolute directed cycle products are respectively 2 vs 1, 1 vs 8, and 8 vs 18, excluding a diagonal symmetrizer.

The exact-Q computations and independent scope-bound checks passed: **no discrepancy in any positive multidegree through height 10** for all three matrices and the A3 / affine-A2 controls (258 nonzero free-Lie degrees per matrix; 1,290 checked matrix-degree records), and through height 12 for A_one (421 degree records). All other positive degrees in those ranges have zero free-Lie dimension. Each check rejected all six negative controls. These are bounded results, not the full theorem.

| Matrix | dim at (2,2,2), both quotients | dim at (3,3,3), both quotients |
|---|---:|---:|
| A_one | 3 | 8 |
| A_cycle | 5 | 31 |
| A_large | 14 | 148 |
| affine-A2 control | 2 | 2 |

The free-Lie dimensions at those degrees are 14 and 186. The samples include interior weights in A alpha<=0, so the computation is not just rechecking the boundary theorem. Evidence: [`evidence/interior-root-samples.json`](evidence/interior-root-samples.json), [`height-10 independent PASS`](evidence/rational-height10/independent-check.json), and [`height-12 independent PASS`](evidence/rational-height12/independent-check.json), with full certificates and source/scope hashes. The two earlier unbound checker runs were cancelled without acceptance; they are not counted.

### Uniform symbolic interior theorem and failed routes

**Every rank-three GCM has I_alpha=K_alpha through total height six.** After the coefficient-one theorem, only (2,2,2) remained. For strictly negative off-diagonals, partition their six magnitudes into 1 versus 2+x, x>=0. This creates 64 cells covering arbitrarily large entries. Through componentwise degree (2,2,2), Serre ideal spaces depend only on the cell, while each lowering matrix is affine in its free parameters.

The producer found positive-coefficient maximal-minor certificates in 58 cells; the first chosen minor was inconclusive in six. **The six failures were not dropped.** Exact simultaneous index permutations map every cell to one of 16 successful representatives, and degree (2,2,2) is permutation-invariant. The independent checker reconstructed all representative matrices, verified the full determinant identities by fraction-free Bareiss elimination in FLINT, checked positivity including the constant term, and verified complete 64-cell coverage. Matrices with a zero off-diagonal pair are symmetrizable in rank three and are handled separately.

The complete logical bridge is [`proof.md` §9](proof.md), with [`all-cell independent PASS`](evidence/symbolic-222/all-cells-independent-check.json) and [`permutation coverage`](evidence/symbolic-222/permutation-cover.json). For the largest representative, a 14-by-14 minor has 3,699 positive terms, constant 286654464, and total degree 14. These are exact polynomial identities, not evaluations at finitely many matrices. The first rank-three degrees not excluded **uniformly** now have height at least seven. No all-height nonsymmetrizable case or novelty claim follows.

The initial SymPy reporting exception is preserved in `evidence/symbolic-222-first-attempt.json`. The direct all-cell checker correctly rejected mask 1 before symmetry coverage was supplied; its stricter predecessor is preserved as `evidence/check_interior_cells-direct.py`. The final proof changes the argument by a verified symmetry reduction, not by weakening the required parameter coverage.

No all-height reduction of interior degrees was found. The standard invariant-form route cannot simply be applied to the original nonsymmetrizable A. Even the coefficient-one comparison breaks at coefficient two: altered i-row Serre relations and i-lowerings can then matter. Finite exact agreement, modular agreement, and the known symmetrizable theorem do not close that gap.

### Reproduction

From this directory, the core computations need only Python 3.14.3 and the standard library, one process each:

```sh
python3 work/compute.py --height 10 --prime 1000003 --output evidence/modp-height10
python3 work/compute.py --height 10 --output evidence/rational-height10
python3 work/check_certificate.py evidence/rational-height10/certificate.json.gz --height 10 --matrices A3_control affine_A2_control one_asymmetric_edge oriented_double_cycle larger_asymmetric_cycle --output evidence/rational-height10/independent-check.json --negative-controls
python3 work/compute.py --height 12 --prime 1000003 --matrices one_asymmetric_edge --output evidence/modp-height12
python3 work/compute.py --height 12 --matrices one_asymmetric_edge --output evidence/rational-height12
python3 work/check_certificate.py evidence/rational-height12/certificate.json.gz --height 12 --matrices one_asymmetric_edge --output evidence/rational-height12/independent-check.json --negative-controls
```

The separate symbolic experiment uses an isolated uv environment, not a global installation:

```sh
env UV_CACHE_DIR=/tmp/kac-serre-uv-cache OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 uv run --no-project --with sympy==1.14.0 --with python-flint==0.9.0 python work/interior_minor.py --mask 0 --output evidence/symbolic-222
env UV_CACHE_DIR=/tmp/kac-serre-uv-cache OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 uv run --no-project --with sympy==1.14.0 --with python-flint==0.9.0 python work/run_interior_cells.py --output evidence/symbolic-222 --seconds-per-cell 180
env UV_CACHE_DIR=/tmp/kac-serre-uv-cache uv run --no-project --with python-flint==0.9.0 python work/check_interior_cells.py evidence/symbolic-222 --output evidence/symbolic-222/all-cells-independent-check.json
```

The last command alone verifies the provided polynomial certificates and complete permutation cover; the two preceding commands regenerate the producer outputs. The supplied `permutation-cover.json` is itself a checked certificate, not an assumed classification.

No more than four computation processes were run concurrently. No system package installation, live infrastructure change, or Git publication occurred. Finite certificates are compressed to keep the target small.

## Claims

| Claim | Status | Evidence path |
|---|---|---|
| The descent recurrence computes the actual positive maximal Cartan-disjoint ideal | PROVED | `proof.md` §§2–3; `evidence/descent-audit.md` §§2–4 |
| Original relations plus generator brackets compute the whole positive Serre ideal | PROVED | `proof.md` §4 |
| Symmetrizable-deletion / coefficient-one equality in all degrees | PROVED | `proof.md` §7; `evidence/descent-audit.md` §10 |
| Every rank-three GCM has equality at all degrees with a zero/one coordinate, hence through height five | PROVED | `proof.md` §7 corollary |
| A first rank-three defect must have every coordinate >=2 and A alpha<=0 | PROVED | `proof.md` §§7–8 |
| Every rank-three GCM has equality through height six, via 16 exact polynomial certificates covering all 64 cells | COMPUTED+VERIFIED | `proof.md` §9; `evidence/symbolic-222/all-cells-independent-check.json` |
| Three nonsymmetrizable matrices and two controls agree in every positive degree through height ten | COMPUTED+VERIFIED | `evidence/rational-height10/independent-check.json` |
| A_one agrees in every positive degree through height twelve | COMPUTED+VERIFIED | `evidence/rational-height12/independent-check.json` |
| All-height equality for the three nonsymmetrizable matrices | OPEN | No all-height argument is supplied |
| Full book conjecture for every nonsymmetrizable GCM | OPEN | Dated primary status evidence above; no proof or counterexample here |

The finite and polynomial-certificate claims are backed by completed independent checks, not producer logs alone. The written proofs and exact algebraic checks are not Lean/kernel formalizations, and the universal book conjecture remains open here.

## Independent review

A read-only mathematical subagent independently audited the lowering/ideal recurrences, obtained explicit low-degree formulas, and audited the infinite coefficient-one proof. Its complete reasoning is in [`evidence/descent-audit.md`](evidence/descent-audit.md); it ran no computations.

Three focused Codex CLI reviews used the registry's **gpt-6.1-sol / max**, confirmed by runtime headers, with read-only sandbox, ephemeral execution, target-only read prompts, and no further delegation or test execution. Round 1 was **READY-WITH-FIXES**: the mathematics was accepted, but experiment scope needed external binding. That issue was fixed and mutation-checked. Round 2 was **READY** for the revised independent checker. Round 3 was **READY** for the complete uniform height-six theorem and exact polynomial/permutation certificates. Verbatim outputs: [`proof-review.md`](evidence/proof-review.md), [`checker-review.md`](evidence/checker-review.md), [`symbolic-review.md`](evidence/symbolic-review.md). Commands, prompts and hashes are preserved alongside them; [`review-resolution.md`](evidence/review-resolution.md) resolves every finding and records timing/trust limits. All three reviews explicitly distinguish the partial results from the unsolved full goal.

## Next steps

The full goal remains J=tau for every GCM. The precise next analytic step is to control the **interior** lowest-weight vectors, where the symmetrizable comparison no longer intertwines the missing lowering. For A_one, the necessary conditions alpha_i>=2 and A_one alpha<=0 leave only **(4,4,5)** at height 13 after the bounded height-12 computation; at height 14 they leave only (4,4,6). This is a candidate for investigation, not a claimed defect. See [`evidence/next-interior-degrees.json`](evidence/next-interior-degrees.json).

A useful route is to decompose these levels under the symmetrizable rank-two Levi and analyze the remaining f_i coupling on its lowest-weight vectors, rather than infer a global theorem from longer numerical searches. Any proposed all-height argument must explain why no first extra relation can appear at an arbitrarily large interior degree. If a candidate defect is found, supply its exact rational Lie polynomial and independently certify its nonmembership in the Serre ideal and every required descent. The present equality checker deliberately refuses nonzero-defect certificates; its PASS must not be misreported as validation of a counterexample.
