DISPOSITION: ACCEPT-WITH-FIXES

The mathematical argument survives this static audit, conditional on the computational trust assumptions stated below. I found no missing case in K1, its two corollaries, or section 8. This does not independently certify the unpinned computational runs.

**FATAL**

none.

**MAJOR**

1. **The claimed drat-trim control outcomes lack receipts.** `review/K1-THEOREM.r1.md:70` and `review/K1-THEOREM.r1.md:71` assert two observed verification results, but `manifest.json:458` records that neither output receipt exists. Moreover, `env/drat-trim/ctl_unsat.drat:1` contains `0`: an empty-clause proof line, not an empty proof file. The pinned SAT formula, `env/drat-trim/ctl_sat.cnf:1`, is satisfiable; the pinned UNSAT formula, `env/drat-trim/ctl_unsat.cnf:1`, contains opposing unit clauses. **Corrected statement:** the control inputs are available and have the intended satisfiability statuses; their reported verifier outcomes remain unverified. Supply receipts or withdraw the outcome assertions. This does not itself refute the production proofs.

2. **The additional phase-elimination and minimality claims are unsupported here.** `review/K1-THEOREM.r1.md:110` asserts 315 relations and 97 independent contradictions; `review/K1-THEOREM.r1.md:111` asserts minimum cardinality seven. The cited exploration code is unpinned (`manifest.json:440`), and the pinned certificate checks only the displayed seven-relation contradiction (`code/k1_phase_cert.py:47`). **Corrected statement:** a seven-relation contradiction exists. Establishing the other counts and minimum cardinality requires additional evidence; none is needed for K1.

**MINOR**

1. **Two printed hash suffixes are wrong.** At `review/K1-THEOREM.r1.md:64`, replace `e61ab812…3c7e` with `e61ab812…e113`; the full digest is recorded at `manifest.json:228` and matches my rehash. At `README.md:7`, replace `a39911fd…ff3a2` with `a39911fd…a3ff2`, according to `manifest.json:339`. The latter target is unpinned, so this confirmation is against the manifest’s recorded digest.

2. **The table citation confuses sets and lists.** `review/K1-THEOREM.r1.md:57` calls Tables 5–6 reduced-list tables. They count reduced **sets**; Tables 7–8 count lists (`sources/1406.3681v2.layout.txt:721`, `sources/1406.3681v2.layout.txt:736`). **Correction:** cite Tables 7–8, or explicitly invoke Theorem 3.1: for \(k=2\), the factor \((k-1)!\) is one, so the numerical totals coincide (`sources/1406.3681v2.layout.txt:361`).

3. **The minimum computes the key, not \(|par|\).** The wording at `review/K1-THEOREM.r1.md:44` is inaccurate. `code/net_canon.c:72` counts distinct normalized keys; `code/net_canon.c:74` obtains \(|par|=846720/\text{distinct}\). **Correction:** distinguish the lexicographically minimal canonical key from this quotient.

4. **Solver versions are not tied to the recorded runs.** `review/K1-THEOREM.r1.md:64` and `review/K1-THEOREM.r1.md:65` name versions without run-specific receipts. `manifest.json:459` establishes only what was installed later. **Correction:** describe the recorded commands as using `cadical` and `kissat`, with run-time versions unverified.

5. **References and historical assertions exceed the pinned evidence.** `README.md:23`, `code/k1_sat.py:8`, `code/k1_sat.py:15`, `code/k1_encB.py:4`, and `code/pattern_check.py:2` reference absent `review/LEMMAS.md` (`manifest.json:457`). Redirect these references to the actual arguments. The killed-classification history at `review/K1-THEOREM.r1.md:59` and the retired run’s reported violations at `review/K1-THEOREM.r1.md:128` have no pinned run receipts; label them unverified history. The mathematical observation that the unshifted \(f\) is not a permutation is independently correct.

The following addresses the requested checks explicitly.

**(a) Reformulation and equivalence.**  
`review/K1-THEOREM.r1.md:8`–20 agrees with the definitions at `sources/2607.12933v2.layout.txt:90`–116.

A single QLS has at least seven rays because any row is an ONB. Exactly seven rays means every entry belongs, up to phase, to that row’s ONB. Thus non-classicality is equivalent to having more than seven rays.

Separate square-wise unitaries and entry phases straighten each classical member into \(|L(i,j)\rangle\), preserving every tensor-product orthogonality. Independent row or column permutations are unnecessary. Two resulting classical squares are orthogonal precisely when their ordered symbol pairs are distinct, giving two MOLS and a 4-net. The proof of C1 correctly handles equal and unequal symbols.

Permuting the four parallel classes need not be a permitted isotopy of the original triple. Nevertheless, it preserves the ONB-assignment problem and its ray count. Choosing any two classes as rows and columns reconstructs the required triple. Therefore one representative per net-isomorphism class suffices.

**(b) Frame lemma and F1–F4.**  
The necessary conditions at `review/K1-THEOREM.r1.md:23`–39 are sound.

If two of the three meeting points on \(\ell_0\) coincided, two lines from different classes would share both that point and the off-frame point, violating the net axioms. Points on \(\ell_0\) have their prescribed singleton supports. Lines through frame points are included in the conditions.

For F3/F4, put the seven line vectors in the **rows** of a unitary matrix. Coordinate \(k\) is then column \(k\). A uniquely covered column has its sole coefficient of modulus one; the corresponding row’s other coefficients vanish. This proves exactly the stated direction of F4. All singleton supports in this frame imply classicality.

**(c) Encoders, enumeration, and model lists.**  
I found neither extra restrictions nor omitted parts of frame + F1–F4 in the production encodings.

- A computes the stated frame and \(A(p)\) at `code/k1_sat.py:43`–59. Its auxiliary clauses at `code/k1_sat.py:77`–79 enforce the full equivalence \(o_k\leftrightarrow(x_{pk}\land x_{qk})\); line 81 excludes exactly one shared coordinate. Lines 84–92 implement coverage and F4, including an empty clause when coverage is impossible. The driver explicitly disables both optional families at `code/k1_certify.py:52`.
- B uses the same frame and allowed coordinates at `code/k1_encB.py:37`–49, enumerates **all nonempty subsets** at lines 53–56, and enforces exactly one choice at lines 58–62. Lines 65–75 implement F2–F4, including empty coverage clauses.

A’s blocking clause at `code/k1_certify.py:62` excludes exactly one complete support-bit assignment, regardless of auxiliary variables. B’s clause at `code/k1_encB.py:104` excludes exactly one support tuple **provided** the parsed model contains exactly one selected option for every point.

Consequently, UNSAT of base plus these blocks proves that every base support solution is listed. Calling the lists *exactly* the model sets additionally requires their listed members to be valid models. The assumptions are:

1. Correct, complete SAT-model output and parsing—particularly B’s complete one-hot selections.
2. Sound drat-trim verification and an authentic success report.
3. Identity of the checked CNF with the intended encoder output plus exactly the listed blocks, using the pinned class data.
4. Faithful execution of the recorded drivers and summaries.

Both drivers handle carriage returns and compare complete stripped status lines, requiring `s VERIFIED` and excluding `s NOT VERIFIED` (`code/k1_certify.py:69`, `code/k1_encB.py:112`). They do not independently validate SAT assignments or require drat-trim exit code zero. The summaries contain synthesized statuses, not raw verifier receipts. Under sound verifier-status semantics, the parsing logic is adequate.

Reading the actual model arrays confirms equality after decoding:

- Class 5: A’s order corresponds to slopes \(3,6,4,5\); B’s to \(6,3,4,5\), with singleton support \(\{y-mx\}\). See `evidence/k1A/summary.json:103` and `evidence/k1B/summaryB.json:69`.
- Class 6: both contain the weight-4 pattern and singleton slopes \(2,4,5,6\), in different orders. See `evidence/k1A/summary.json:340` and `evidence/k1B/summaryB.json:300`.
- I checked all off-frame entries of the weight-4 model against \(A(p)\), rather than relying on its reported weight set. They agree.

The control discrepancy is MAJOR finding 1.

**(d) Class completeness and trust base.**  
The counting argument at `review/K1-THEOREM.r1.md:41`–60 is valid under its computational premises.

The normalization count is
\[
24\cdot49\cdot720=846720:
\]
ordered parallel classes, an origin, and an ordering of the six remaining points on its row line. `code/net_canon.c:47` orders both squares’ first rows; line 48 orders the first square’s first column. These are precisely EW’s reduced-list conditions (`sources/1406.3681v2.layout.txt:185`).

Every reduced list in the species arises from such a normalization. The autoparatopism group acts freely on **normalization frames**: fixing their ordered classes and ordered row-line points fixes all lines of two other classes, hence all points. Thus each key has \(|par|\) preimages. The full paratopy action on lists is not free; its stabilizer is \(\operatorname{par}(M)\).

The 78-byte key omits only prescribed entries (`code/net_canon.c:52`). Equality of minimum keys therefore yields an actual paratopy, making the minimum a complete invariant. The seven printed keys in `evidence/nets7_classes.json:1` are distinct.

By hand, the orbit sizes sum to
\[
6720+141120+141120+35280+17640=341880,
\qquad 341880+360+240=342480.
\]
All seven divisions by the printed group orders also check. EW Theorem 3.2 gives exactly this coefficient (`sources/1406.3681v2.layout.txt:382`). Disjoint species contributions exhausting the published total establish completeness; random discovery alone would not.

The maximal flags agree with EW’s five maximal species (`sources/1406.3681v2.layout.txt:708`). Their transversal-count multiset \(0,1,2,4,4\) agrees with Table 9 (`sources/1406.3681v2.layout.txt:868`). The two affine classes extend using remaining directions.

For validity spot-checks, class 0 has symbols \(x+y\) and \(f(x)+y\), with both \(f\) and \(f-x=(0,1,3,5,2,6,4)\) permutations. For classes 1–4 I checked first rows, first columns, and the seven second-square symbols on the first square’s symbol-0 line. These passed; I did not exhaustively validate those four arrays. Classes 5 and 6 match \((x,y,y-x,y-2x)\) and \((x,y,y-x,y-3x)\). Their direction sets are respectively harmonic and equianharmonic: \(2\) is harmonic, while \(3^2-3+1=0\pmod7\).

The exact remaining trust base includes the published EW enumeration, validity of the input nets, and faithful production of the stored keys/counts by an executable corresponding to `code/net_canon.c`. Neither that binary nor the class-file generator is pinned. Source inspection establishes the algorithm’s logic, not that it produced the JSON. The generator becomes dispensable once the explicit arrays and canonical computations are independently validated.

**(e) Phase cycle.**  
The arithmetic at `review/K1-THEOREM.r1.md:89`–105 checks by hand. Against `evidence/nets7_classes.json:1`:

| Point | Four labels | \(A(p)\) |
|---|---|---|
| 26 | \((3,5,2,3)\) | \(\{0,1,4,6\}\) |
| 28 | \((4,0,3,2)\) | \(\{1,4,5,6\}\) |
| 29 | \((4,1,4,3)\) | \(\{0,2,5,6\}\) |
| 33 | \((4,5,1,0)\) | \(\{2,3,4,6\}\) |
| 34 | \((4,6,2,1)\) | \(\{0,3,4,5\}\) |

Frame points are \((0,j,j,j)\). Off-frame, the excluded coordinates are \(y,y-x,y-3x\), so their complement is \(y-x\{2,4,5,6\}\).

The seven pairs have common classes \(0,0,0,0,1,2,3\), respectively, and overlaps
\[
56,\ 46,\ 45,\ 05,\ 46,\ 04,\ 06.
\]
Each pair shares exactly one net line.

For nonzero coefficients, cancellation of the two inner-product terms gives the displayed phase relation with right side \(\pi\), modulo \(2\pi\). All four coefficients are nonzero because the supports equal \(A(p)\).

Writing \(D_p(a,b)=\arg c_{pb}-\arg c_{pa}\), the signed left-hand side groups into
\[
\begin{aligned}
&D_{28}(5,6)-D_{28}(4,6)+D_{28}(4,5)\\
&-D_{34}(4,5)+D_{34}(0,5)-D_{34}(0,4)\\
&-D_{29}(5,6)-D_{29}(0,5)+D_{29}(0,6)\\
&+D_{26}(4,6)+D_{26}(0,4)-D_{26}(0,6),
\end{aligned}
\]
with the \(D_{33}\) terms cancelling. Every displayed group is zero. The signed right-hand side is
\[
(1-1+1-1+1+1-1)\pi=\pi.
\]
The word derivation at lines 103–105 also works: the two \(\pi\) contributions in each intermediate identity cancel modulo \(2\pi\).

`code/k1_phase_cert.py:23`–60 checks the advertised support equality, collinearity, overlaps, cancellation, and odd parity. Its certificate agrees (`evidence/k1A/phase_cycle_certificate.json:5`–77). It does not establish enumeration completeness or minimum cycle size.

**(f) Section 8.**  
The reduction at `review/K1-THEOREM.r1.md:136`–145 uses Lemma 10 within its printed proof (`sources/2607.12933v2.layout.txt:185`–192).

Two originally orthogonal entries, one supported on a selected two-coordinate set, have either identical or disjoint supports. Applying the same unitary to every entry with that weight-2 support preserves their zero inner products. All other originally zero inner products are preserved as well. Therefore row/column ONBs and tensor orthogonalities with **both** other squares survive simultaneously. Singleton entries, including row 0, are untouched. Successive replacement of another square preserves orthogonality with the already replaced square.

A standard-form square with weight at least two has an additional ray beyond its first-row basis, so it is non-classical. If \(|Q|\le1\), keep a non-classical square unchanged and classicalize the other two, producing forbidden K1. If \(|Q|=2\), classicalize the remaining square; if \(|Q|=3\), no replacement is needed. Every non-classical square of the **resulting** set is heavy. This does not assert heaviness of every square in the original set.

**(g) Pattern controls.**  
`code/pattern_check.py:19`–42 implements the stated evaluator. Its outputs at `evidence/k1A/pattern_controls.json:4`–55 and `evidence/k1A/pattern_controls.json:205`–207 support the reported results.

The seventh-root criterion at `code/pattern_check.py:7` is correct: the multiplicity polynomial has degree at most six, vanishes at a primitive seventh root, and hence is a multiple of \(1+t+\cdots+t^6\). Its coefficient sum is seven, forcing every multiplicity to be one.

Both shifted permutations and directions check by hand. Their off-frame supports are the allowed five-coordinate sets. Of \(42\cdot7=294\) mutations, adding either forbidden coordinate gives 84 rejections; removing an allowed coordinate preserves these necessary conditions. The printed 4×4 example gives \(12\cdot4=48\) rejected mutations. For the weight-4 pattern, adding a forbidden coordinate violates the frame restriction/F2; deleting a supported coordinate creates a singleton overlap with a row mate. Thus all 294 fail.

The 18 model-evaluation records are present. These controls exercise the independent evaluator; they are not direct SAT-encoder control runs (`code/pattern_check.py:138`–155).

**(h) Hashes and unsupported provenance.**  
I rehashed all pinned files listed by the manifest. They match their manifest digests, including the target’s requested SHA-256.

Among the claim’s 12 printed hash references, the ten pinned references other than `k1_certify.py` match: claim lines 42, 44, 63, the summary hash on 64, 65, 66, 107, 109, and both hashes on 118. The sole claim mismatch is the suffix identified above. The drat-trim source hash at claim line 70 matches `manifest.json:269`; its source and binary were unavailable for independent hashing. Their recorded identities do not themselves establish the build relationship.

The README mismatch is confirmed against the manifest as described above. Its other printed hashes agree with the manifest; external targets were not read. Unsupported control outcomes, solver-run versions, exploration/minimality assertions, absent lemmas, and historical run claims are identified in the findings.

**Scope.** I read the pinned claim, README, manifest, six code files, model summaries, certificates, controls, and relevant source passages, using LF-only line numbering. I checked the counting arithmetic, model correspondence, support formula, seven phase relations, reduction, and control arithmetic by hand; only hashing used computation. I ran no interpreter, solver, verifier, compiler, network operation, delegation, or write. I could not verify the unpinned CNFs/proofs, executable provenance, generator execution, or missing receipts, and did not exhaustively validate the four random net arrays. Subject to the explicit computational assumptions above, K1 and its two corollaries follow, as does the section 8 reduction. K2, K3, and therefore \(M(7)\), remain open.