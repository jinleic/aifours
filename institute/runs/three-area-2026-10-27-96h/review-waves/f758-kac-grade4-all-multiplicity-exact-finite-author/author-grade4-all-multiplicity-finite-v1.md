# Grade-four complete-multiplicity ordered-tensor finite preparation

**STATUS FIRST — NOT TESTED / NOT RUN.** This is a nonblind same-harness GENERAL AUTHOR written reconstruction and one proposed standard-library finite source, not an executed calculation or a parent disposition. No scientific program, compile, test, build, formatter, linter, solver, external-model CLI, installation, Git operation, deletion, heavy job, or network call was run by this author. The source, every proposed assertion, and all mutation controls are untested. The parent must independently read the **entire** source through its ending, disposition it, and issue a **separate** bounded GO before considering a run; the cooperative source deadline is 40 seconds and any external bound must be at most 55 seconds. A source file, expected table, or prior sample receipt is not a passing execution.

**Explicit coverage.** The written grade-four character/whole-first-relation reconstruction below is conditional on the named actual-source and whole-Serre bridge for every full complex Cartan realization, for r=3 and every integer s≥4. The proposed finite executable targets **only (r,s)=(3,4),(3,5)**. It is designed to enumerate all 13 possible lowest positions and all free grade-four weights, to generate the whole 81-dimensional first-seed relation in ordered tensors, and to construct the full simultaneous F1/F2 lowest kernel and the actual F3 map for **each** of the seven listed remaining types at **both** points. There is no claimed output, map rank, control detection, radical equality, parameter interpolation, or verified runtime here. Parameters r=1,2, equal arms, s≤r, all higher grades, and the global problem are outside this finite assay. The parent remains responsible for execution safety, independent review, and actual disposition.

## Prepared source and precise interface

`independent-grade4-all-multiplicity-finite-v1.py` — SHA-256 `0898124f38607f17d8b1eb4c798e9d049279ab82a6e852fe2ef3467a4609689f`, 19,037 bytes. It was created directly in its complete final bytes with exclusive creation; it was not copied, edited afterward, imported, compiled, or run. The SHA was also observed by `shasum` on the created file. The program reads no files or inputs, has no network/subprocess/delete operation, and emits only JSON on stdout. A prospective invocation is `python3 -B independent-grade4-all-multiplicity-finite-v1.py`; this is **not** a GO. A full output could be large because actual sparse tensor bases are intentionally retained. Allocation/peak RSS and wall time have not been observed or independently bounded here; parent resource admission and supervision are separate.

The source makes a degree-three and degree-four Lyndon basis from genuine ordered associative-tensor concatenation; a word such as `xabc` denotes a tensor word, not a product of 3×3 matrices. It separately forms Witt characters from the eight individual letter weights, compares every weight with the Lyndon count, and extracts the 13 lowest multiplicities with the Weyl denominator. For r=3 the source closes the single degree-four seed under **all** E1,E2 translates weight by weight, tests its full expected character and the F1,F2 stability of its span, and emits its full basis. It checks that the actual F3 kills every relation basis vector for both fixed s values. It then forms the quotient weight by weight, computes simultaneous kernels of the **entire** induced F1,F2 maps, keeps every basis vector rather than one preferred copy, applies the actual ordered-tensor F3 derivation to each, and expresses each image in a complete ordered-tensor grade-three target basis. Its JSON is intended to include relation bases, quotient bases, lowest tensors and coordinates, F3 columns, and image ranks. These descriptions are source-design statements, **not observed results**.

The proposed explicit negative controls are: (1) reverse the actual Cartan delta in F3 and compare the full tensor F3([x,b]) at (3,4), with expected correct coefficient 6 and mutant coefficient 2; (2) omit all translates of the first seed and detect the missing genuine E2(seed) relation in weight (1,1); (3) at a genuinely constructed lowest space with at least two independent F3-image directions, retain only one lowest basis vector and require a smaller image rank. If no such direction pair is constructed, or any check fails, the source is designed to report FAILURE rather than invent a detection. Deadline or signal is designed to report INCOMPLETE with previously completed stages; an interrupted type is not appended as complete. None of these controls has been exercised. A parent must verify both the source logic and the intended reasons for actual mutation detection; a failure, timeout or partial JSON is not a pass.

## Written character reconstruction and whole relation

Let x,a,b,c,d,e,f,g have respective horizontal degrees
`(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)` and set
`H=(1+X)(1+Y)(1+XY)`. The characteristic-zero free-Lie/PBW character identity gives
`C4=(H(X,Y)^4-H(X²,Y²)^2)/4` and `C3=(H(X,Y)^3-H(X³,Y³))/3`. In particular, with out-of-range binomial coefficients zero, the coefficient of X^aY^b in C4 is

```
( sum_k C(4,k) C(4,a-k) C(4,b-k)
 - 1_{2|a,2|b} sum_k C(2,k) C(2,a/2-k) C(2,b/2-k) ) / 4.
```

The lowest labels at (a,b) are `(p,q)=(4-2a+b,4+a-2b)`. In the dominant region the multiplicity is the coefficient of `(1-X)(1-Y)(1-XY) C4`; explicitly it is `c[a,b]-c[a-1,b]-c[a,b-1]+c[a-2,b-1]+c[a-1,b-2]-c[a-2,b-2]`. Solving the two dominance inequalities in nonnegative integers yields exactly the 13 rows below. The following are the **written expected values** and assertions to be independently assessed, not outputs of this unrun source:

| (a,b) | (p,q) | free copies | quotient copies, r=3, s≥4 |
|---|---|---:|---:|
| (0,0) | (4,4) | 0 | 0 |
| (0,1) | (5,2) | 1 | 1 |
| (0,2) | (6,0) | 0 | 0 |
| (1,0) | (2,5) | 1 | 0 |
| (1,1) | (3,3) | 3 | 3 |
| (1,2) | (4,1) | 4 | 4 |
| (2,0) | (0,6) | 0 | 0 |
| (2,1) | (1,4) | 4 | 4 |
| (2,2) | (2,2) | 7 | 7 |
| (2,3) | (3,0) | 6 | 6 |
| (3,2) | (0,3) | 6 | 6 |
| (3,3) | (1,1) | 8 | 8 |
| (4,4) | (0,0) | 1 | 1 |

For the whole relation, the first seed can be taken as `[x,[x,[x,a]]]`; it is nonzero in the tensor embedding since `xxxa` occurs with coefficient 1. F1 and F2 annihilate it by the displayed letter action table, and its labels are (2,5). In the finite-dimensional semisimple Levi module, the cyclic module generated by this one nonzero lowest vector is one irreducible copy, even in the presence of equivalent copies elsewhere; its dimension is `(2+1)(5+1)(2+5+2)/2=81`. At r=3 its grade is four; for every s≥4 the second seed has grade s+1≥5, and outer brackets cannot remain in grade four. At the **imported whole positive/negative Serre-ideal bridge**, this identifies the entire grade-four relation with that cyclic module, not just its seed or a single selected weight. Consequently the free and quotient dimensions are 1008 and 927. The source is designed to verify the 81 relation directions in ordered tensors rather than merely use this dimension; it has not yet done so.

The seven remaining lowest positions are `(1,2),(2,1),(2,2),(2,3),(3,2),(3,3),(4,4)`, with expected complete multiplicities `4,4,7,6,6,8,1`. Existence of these quotient copies does not imply membership in the Cartan-disjoint radical. Conversely, absence of the two types (6,0) and (0,6) here is a grade-four character assertion, not a general higher-grade claim. No F3 rank, kernel dimension, or injectivity for these seven spaces is asserted without an actual separately authorized run and review. Even a nonzero simultaneous F1/F2/F3 kernel would require a separate ideal-closure/radical analysis.

## Imports, actual corrections and source coverage

The actual quotient interface is imported from S6: the ordinary free Lie algebra on the eight-dimensional Levi module, the full complex Cartan including singular-realization extra directions, and the **whole** positive/negative Serre-ideal bridge with all cyclic seed modules and possible overlaps. S7 supplies the displayed eight-letter Levi table and actual F3 letter-delta identities; the classical characteristic-zero free-Lie tensor embedding, finite-dimensional sl3 semisimplicity, and Weyl character identity are also imports. S4/S5 supply the separate entire-grade-three radical scope if it is later used; it is **not** assumed that a finite F3 matrix proves radical membership or that any F3 rank follows merely from a character. S2 is an unadopted nonblind candidate, not a proof black box; S3 is the separately scoped parent disposition, whose uniform exact-kernel/seven-type refinement remains unadopted there. S8 is an earlier finite sampled receipt, not a universal parameter proof or an execution of this source.

Actual packet corrections were retained: S1 replaces S2's mistaken phrase about needing the separately imported all-grade boundary with the grade-four absence statement **without** needing that separate boundary in this grade; S5 clarifies that “grade≥4” meant unpaid **entire** grades, not absence of every previously adopted component, and specifies the actual grade-three multiplicity-space injectivity scope. Neither correction is a new parent adoption. No additional source correction is claimed in this report; if a defect is discovered, preserve these bytes and use a new additive correction/new complete exclusive source.

After actual dispatch and before body access, the manifest, freeze receipt, final pre-dispatch binding, prepared metadata, actual dispatch receipt and all **22/22** listed status/permission controls were read through their endings. A direct PREBODY ACK was sent to Main with the exact single-part/1,789-LF/8-body counts. The one packet was read in serial RAW calls of ≤20 LF through LF1–1789; an early presentation repeat was made to display a clipped long line in full before continuing. No packet comparison or mathematical research preceded the full ending. The packet contains the following complete frozen bodies; paths are as given in the manifest, and SHA values below are the frozen whole-body pins, not a claim of fresh author rehash of all original bodies:

| Source | Coverage | Frozen SHA-256 | Role |
|---|---|---|---|
| S1 | LF1–5 | `0c24a0e70f9e42f3fbd19a7aa909c34d81268f8e946bc7bcc1d12d7513eee8e8` | f739 additive wording correction |
| S2 | LF1–216 | `dc486169629008e88b650f1807c313873b5e29889cf811eb9a9becec45e176df` | unadopted complete f739 character/kernel candidate |
| S3 | LF1–33 | `34f2fd44c33d2c481c8ea112f636e4692812559f393c1ff5ede5ef1b89ab3ce0` | scoped parent grade-four disposition |
| S4 | LF1–37 | `b703063027085eb004407d51a9a55941c2fbf02d5f3ccf851ab502a1af7f500d` | entire-grade-three radical disposition |
| S5 | LF1–5 | `9648a8ab70aa62355e52e5c7cc8ad5ebb584876bc1d5ad7e3b883b40f78799e5` | grade/lowest-map correction |
| S6 | LF1–27 | `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e` | actual free-source/whole-Serre bridge |
| S7 | LF1–314 | `f856b62e2f8261ff0c272ccff33431cdbd014aa4ef7a6f27aca6f445c288ab5e` | actual Levi/F3 reconstruction |
| S8 | LF1–1118 | `757d91d52730335c56bd6941ac6da45d43890c28fcf35a42834b444e222ec674` | earlier finite sample receipt |

Observed administrative pins: manifest `d9a7b1b3a0417471fe0fc33758c33401ead4b25e11021cfd36958da7872180f5`; freeze `c332359c378ded40edb815fe68515253bfdd2054a9645aaf761f05a57bee0a29`; final binding `9c898ae709399bde4b38c686ef45d0fd4243a3ad2b643b35d2dfca03ca9268a2`; prepared metadata `694eecbca6c7948b7fb923bf4d9d9a2f67db6ea4f1c290cbbbc17898e5e9e73f`; actual dispatch `c8d114686b6d9182aa391c24330912cd9bdc50c363131200e54e44bd3be30c02`; packet `88168fea366ac8b9b6663ccc92c8f863f908a9e3d59871261747b2fce3e9c6cb`. Controls were used only for permission/status. No outgoing linked source, old code, unspecified sibling proof, held history or held episode and no proof/method/selection/planning/verification/reporting/confidence/downstream consumer of any genuinely held episode was used. This access account is not a certificate about unobservable cognition.

## Remaining frontier and assurance boundary

Parent whole-source reading, scientific admission, a separate ≤55-second GO, actual intended-reason controls, captured JSON and independent disposition are all outstanding. The source's full-map design is unrun and could contain errors or time out; completion of its mathematical coverage is not yet an observed finite result. Even a successful two-point finite result would not establish all s, all r, the entire grade-four radical or global J=τ, the original-source identity, priority/novelty, human review, independent-model-family review, or a formal/kernel proof. An actual whole-multiplicity map, its rank, the ideal-stability argument and any subsequent radical conclusion are distinct obligations.
