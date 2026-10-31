# f28 — independent review of the all-parameter level-four rectangle

Reviewer **MathSemigroup-2**, math-4; author **MathKacMoody-2**, math-3. Assignment SHA `69b5340839ff6f711fb7a7b24a52c9ecf4b866ca9ec77e8100fd494f6f5946ad`. Actual native prewrite observation **Wed Oct 28 17:28:38 PDT 2026**.

## 1. Verdict: exact scope and imports

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR**, with the explicit mathematical imports and computer-assisted limits below.

For every r,s∈Z_{>=1}, every allowed **full complex Cartan realization** of `A=[[2,-1,-1],[-1,2,-1],[-r,-s,2]]`, and each nonzero positive multidegree α=(a,b,n) with 0<=a,b<=2 and 0<=n<=4, the candidate's exact source/target certificates and first-defect argument support `J_α=τ_α`. At n=4 its stated reached-target intersection equality follows from actual quotient-kernel vanishing. This is the finite horizontal rectangle for every parameter and every full realization; it is **not** all horizontal degrees at level four, the global conjecture or arbitrary GCMs.

This is **computer-assisted written support**, conditional on the named parent structural/freeness inputs and PBW. The independently written exact checker below rebuilt all192 degree/class source and target calculations and compared all516 rational determinant-grid evaluations; the interpolation, positivity, mirror and first-defect arguments remain mathematical reasoning, not a machine proof of unrestricted parameters. Same-harness review is not external-model/human/formal/kernel or novelty acceptance.

## 2. Complete sources and exact prior dispositions

I read the full156LF candidate, SHA `887573ecc0adb16706d97674e7f7aa57a1880ae42b7db72330cb16f5272f3abb`, and its full193LF analytic chain predecessor, SHA `d3cf1666c9b7eac84bc052da6af932c3199c878faaca717dcb987ac85109ec67`. I previously reconstructed that predecessor in `frontier-review-f13-kacmoody-horizontal-chain-v1.md`, SHA `e09d6db77b22709092ac7ff079ff7eec49a0e61dadd424648ed4368509f2efd2`, with a separate tensor-word exact check. It is an author candidate plus that review, not a parent disposition or a claim of independent-model review.

The registered100LF family packet SHA `8b811cbc88e55b5b48bebef299f356bf10c808968c967ab2ed4aca1065cc03a6` was read completely in f13; its actual full-Cartan definitions, not book-image authentication, are the family premise. The following two parent statements are **imports**, not re-adjudicated by this numerical certificate:

- **I1:** `math-3-full-cartan-radical-serre-containment-and-first-defect-parent-v1.md`, SHA `08217c89602bbed5bb05447144addfb1978037ad3e4c2e57271d88b794d98be9`: full-Cartan root grading and triangular/mixed-sign support, full positive/negative Serre-ideal splitting, J⊆τ and root-zero defect zero; the exact first-defect interface. This review relies on those stated conclusions and does not claim newly re-reading all their underlying author/reviewer bodies.
- **I2:** `math-3-preliminary-free-lie-and-serre-transport-parent-v1.md`, SHA `f08daf3e2259a563a426e8982be78a36094bb58e4d56f587b2b51f14fa8df46d`: the actual positive preliminary algebra is the free Lie algebra on e1,e2,e3, and the full positive Serre ideal transports to the free-Lie seed ideal with actual lowering targets. Its named PBW theorem/associative embedding is not proved or kernel-checked here. Mandatory `math-3-positive-freeness-pbw-transcription-addendum-v1.json` SHA `21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247` says the released statement is a normalized transcription/paraphrase, **not** a byte-verbatim primary-source quotation.

These parent dispositions and qualification were read completely in f13. Their assumed truth is necessary for identifying the rebuilt tensor-word matrices with the full original Serre quotient. No historical held output or prior selected type is used as a premise. The author chain proof is reconstructed in the prior review and summarized in §6 below; it is not silently elevated to a parent-adopted theorem.

## 3. Independent exact implementation and actual outputs

A new reviewer-owned tensor-word/seed/quotient engine `frontier-review-f28-independent-determinants-v1.py`, SHA `535e58e04b7d40c86127d0956d8dabe0875e3ff6d67b8d4d6c1515638b0112af`, reads pinned certificate JSON and **imports neither author producer nor author replay**. It uses only Python standard-library integers and `fractions.Fraction`; it independently generates all right-nested simple brackets and all six Serre-seed descendants, forms exact Gauss–Jordan quotient spaces and applies full tensor-word lowering.

First I independently checked the SHA pins, sign/constant and16-class coverage of all192 records and replayed representatives including zero source, 214 fixed/one-/two-variable classes, 224 fixed/two-variable classes and predecessor degrees. Actual corrected run at **Wed Oct 28 17:27:09 PDT 2026**, exit0, reported14 exact determinant evaluations and:

```text
PASS SHA pins and exact sign/constant/16-class coverage for all 192 degree-class records
ZERO source (2, 1, 4) 1 1 source_dim= 15
PASS (2, 1, 4) class= (1, 3) source= 1 minor= 1 exact_determinants= 1
PASS (2, 1, 4) class= (2, '>=4') source= 5 minor= 5 exact_determinants= 2
PASS (2, 1, 4) class= ('>=4', '>=4') source= 10 minor= 10 exact_determinants= 4
PASS (2, 2, 4) class= (1, 2) source= 3 minor= 2 exact_determinants= 1
PASS (2, 2, 4) class= ('>=4', '>=4') source= 25 minor= 7 exact_determinants= 4
PASS (2, 0, 3) class= (3, 1) source= 1 minor= 1 exact_determinants= 1
PASS (2, 2, 3) class= (1, 1) source= 1 minor= 1 exact_determinants= 1
PASS independent nested-word/seed/target exact representative replay; determinants=14
```

The **first** reviewer checker run at17:26:52 failed immediately because I mistyped one expected SHA digit in my own source. Native `shasum` showed the candidate's actual pin was correct; I fixed that checker-only transcription and reran. No author source/certificate was changed, and the failed run is not reported as a pass.

I then wrote `frontier-review-f28-all-cases-v1.py`, SHA `c26590366e91c345e100a34c39c31123699d36593894ffd00abeaeed21033ca8`, which pins and imports **my own** above engine, not either author implementation. Actual command

```text
/opt/homebrew/bin/python3 -B mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f28-all-cases-v1.py
```

started at **Wed Oct 28 17:28:04 PDT 2026**, timeout180s, exited0 in **16.05s**. Its output was:

```text
PASS degree=(2, 1, 4) classes=16 determinants=172
PASS degree=(2, 2, 4) classes=16 determinants=110
PASS degree=(2, 0, 1) classes=16 determinants=0
PASS degree=(2, 0, 2) classes=16 determinants=0
PASS degree=(2, 0, 3) classes=16 determinants=15
PASS degree=(2, 0, 4) classes=16 determinants=10
PASS degree=(2, 1, 1) classes=16 determinants=25
PASS degree=(2, 1, 2) classes=16 determinants=47
PASS degree=(2, 1, 3) classes=16 determinants=90
PASS degree=(2, 2, 1) classes=16 determinants=0
PASS degree=(2, 2, 2) classes=16 determinants=0
PASS degree=(2, 2, 3) classes=16 determinants=47
PASS ALL independent exact replays: 192 classes; 516 rational determinant grid evaluations
```

The new all-cases driver reconstructs missing source-complement labels itself for zero-horizontal-kernel records, checks full source/ideal/target span inclusion, all required ideal-lowering stability directions, actual complement independence and coverage, horizontal kernel rank and complete advertised basis, all selected pivot rows, each interpolation-grid determinant and the exact one-sign/nonzero-constant coefficient condition. It reads the two **alternate** 224 minors in the two classes where the initial producer reported mixed signs. Original producer certificates/replays are not modified, and the failed author replay described in the candidate remains historical.

The reviewer's implementation was written after seeing the reported certificate convention and one author replay's algorithm, so it is a separately implemented same-harness replay, **not blind development**. Both reviewer scripts share my own engine and exact JSON input, and their successful execution is not two independent mathematical proofs or a formal verifier. It nevertheless independently checks every finite certificate class and every advertised interpolation-grid determinant without importing author code.

## 4. Why the rebuilt finite calculations address the actual quotient

Work in the free positive Lie algebra of I2, embedded in tensor words at the named PBW boundary. For each multidegree, every bracket tree is a linear combination of right-nested simple-letter brackets: repeated Jacobi expands `[[x,y],z]=[x,[y,z]]-[y,[x,z]]`. The independent engine enumerates those multiset words and computes their exact span; it does not equate every associative tensor word with a Lie basis.

The ideal generated by a positive seed is spanned by all its iterated adjoints by simple generators, since ad([x,y])=[ad x,ad y]. The checker generates **all six** literal seeds and every multidegree-compatible adjoint word, then reduces their actual tensor expansions in the full source span. The same procedure constructs each of the three actual target seed ideals. I1 supplies the necessary fact that negative Serre descendants do not contribute an extra positive-root ideal. Neither overlaps between descendants nor independence of separate seed families is assumed.

For an associative word `w=e_(j1)...e_(jm)` the scalar positive-word part of `[f_i,w]`, after moving h_i to the right, is

`-Σ_(k:j_k=i)(Σ_(ℓ>k) a_(i,j_ℓ)) e_(j1)...hat(e_jk)...e_(jm)`.

The right-h_i coefficient is the deletion derivation sending e_i to1 and other generators to0. That derivation kills every Lie bracket of length>=2 because the inserted scalar is central. The program checks its actual cancellation on every lowered source/ideal vector. All certificate degrees have positive-height targets; root-zero boundaries are paid separately in §6. Thus no actual Cartan row is dropped in the finite matrix reduction.

The target ideal is a **direct sum** of its three separately generated graded subspaces, encoded by the lowering index. Exact reduction modulo that full target ideal provides the same actual quotient map for all source basis vectors. Each certificate's source complement is checked to be in the full free source, independent modulo the source ideal and exhaustive; zero source is checked by equal exact spans. For central records, the entire f1/f2 quotient kernel dimension is computed, the listed basis is checked independent and killed by both rows, and its size equals the kernel dimension before f3 minors are used. The zero-horizontal-kernel cases are independently recomputed without inventing missing producer complement labels.

The checker also verifies that every source-ideal vector lowers into the corresponding target ideal at the base point and each varying parameter direction. Within a threshold class the target ideal is fixed and lowering is affine in r,s, so these basis/direction checks imply stability throughout that entire class. This is stronger than a free-matrix rank without quotient compatibility.

## 5. Parameter classes, interpolation and all-parameter nonvanishing

At n<=4, a seed with repeated node3 has exponent r+1 or s+1 and fits only if the relevant parameter is1,2 or3. Exponents at nodes1/2 are constant. Hence in each of the16 classes `r,s∈{1,2,3,>=4}` all source and target seed subspaces and the chosen complements are fixed. Set x=r-4 and/or y=s-4 for a variable class. From the explicit lowering formula, f1 and f2 are constant and f3 is affine in x,y. Therefore each fixed k×k determinant is polynomial of degree <=k in **each** variable. In the central case its horizontal kernel is constant throughout the class, since source/target subspaces and f1/f2 are constant; the independent driver checks the full kernel basis before using f3.

The independent all-cases program evaluated each selected determinant at the complete `{0,...,k}` grid in each varying variable and compared exactly with every coefficient of the pinned polynomial. Applying the univariate identity principle successively proves the two polynomials equal over all x,y, not just the evaluated grid. It separately checked every nonzero coefficient has the sign of a nonzero constant term. Since x,y>=0, every such polynomial stays nonzero, including x=0 or y=0. This covers all positive integers r,s in the class. The first producer's mixed-sign minors are not used in the two affected central classes; the actual pinned alternate records are checked instead.

Thus the 214 table gives full simultaneous-lowering injectivity at (2,1,4) or an actual zero source. The 224 table gives an injective f3 map on the entire horizontal kernel at (2,2,4), again including zero source. The seven direct predecessors and three central predecessors are verified in the same actual quotient fashion, with all 16 classes each. Finite exact agreement plus the all-parameter polynomial argument—not a sample-only extrapolation—supports these matrix claims subject to I1/I2/PBW.

## 6. Mirror, level-zero boundary and J=τ induction

The analytic chain predecessor, independently reconstructed in my f13 review, proves zero simultaneous lowering kernel for all n>=1 at horizontal degree(1,1), using an explicit V_k source basis, full Serre-seed coordinate spans and the three cases s<n; s>=n,r<n; r,s>=n. It also proves the (1,0,n),(0,1,n), pure-e3 and (1,1,0) boundaries for all n, including the root-zero Cartan targets. This is a written predecessor with I1/I2/PBW, not a finite extrapolation or an unreviewed automatic parent import.

Swapping nodes1 and2 together with r and s takes the 20/21 cases to 02/12. For an arbitrary full realization, simultaneously swap the first two Cartan rows and the first two columns, and swap the first two columns in each extra Cartan row. Rank and the full Cartan space are preserved, the defining and all Serre relations correspond, and swapping back is inverse. Hence actual J,τ,root spaces and lowering targets transport; no identification of two different fixed realizations without this map is assumed.

At n=0, the positive horizontal subalgebra is generated by e1,e2 and `t=[e1,e2]`; the two horizontal Serre relations make `[e1,t]=[e2,t]=0`. Every longer positive bracket therefore vanishes, so the degrees with a=2 or b=2 on this boundary vanish. The chain predecessor supplies the remaining e1,e2,t and root-zero cases. I1 supplies zero mixed-sign spaces and zero root-zero defect.

For `D=τ/J`, any nonzero component in the rectangle has a least positive total height. Its simple lowerings lie in strictly smaller rectangle components, in D_0=0, or in actual mixed-sign zero spaces. It would therefore be a nonzero simultaneous singular class. The chain, verified matrices, mirror and Levi boundary exclude that possibility at every rectangle degree. Hence D=0 there, i.e. `J_α=τ_α`. This is a downward-closed first-defect argument; it does not claim that vanishing of a single isolated kernel alone forces ideal equality.

If an actual x has `Δ(x)` in the full target ideal, its Serre-quotient class is simultaneously singular. At the certified n=4 degrees it is zero, so x∈J_α and the SAME `j=x` gives the reached-target correction. Conversely ideal stability gives the easy inclusion. Unreached abstract target tuples are not asserted reached.

## 7. Limitations and final finding

No FATAL, MAJOR or MINOR defect was found in the candidate's exact mathematical and certificate claims. The all-class replay establishes the finite exact arithmetic under the independently implemented definitions, and the written argument extends it to every parameter in the 16 threshold classes. This remains contingent on I1/I2/PBW and the stated source/Cartan conventions; no fully formal proof checker, external-family/human review, source-wide priority/novelty verification or unrestricted original resolution is claimed.

Degrees outside `a,b<=2` at level4, any other GCM, the old five-source quotient, H13 and global Serre equality remain outside the conclusion. No extra source/author contact, external model, Git push/publication, deletion or infrastructure mutation occurred. Main must read the entire candidate and actual return and independently decide adoption; prior quarantines are not retrospectively promoted by these new checks.
