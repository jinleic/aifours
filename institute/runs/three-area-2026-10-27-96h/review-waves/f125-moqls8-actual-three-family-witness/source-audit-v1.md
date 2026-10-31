<!-- Persisted verbatim by the parent at 2026-10-28T20:17:05-0700 PDT from read-only scout output agent://MOQLSSourceDefinitionAudit (paged :raw ranges, no truncation footer). The scout could not write files and did not recompute pins; the parent recomputed manifest input pins at freeze time. -->

# f125 source audit v1

## 1. Summary

- Ball–Simoens defines \(M(n)\) using **nonclassical sets**, not sets in which every member must be nonclassical. **One genuinely nonclassical member suffices.**
- Its pinned Table 2 gives **\(2\le M(8)\le5\)**. The upper bound comes from **Theorem 5**, \(M(n)\le n-3\).
- **Corollary 7 does not apply at \(q=8\)**: \(q-1=7\) has no proper positive divisor other than the expressly excluded \(1\).
- **Theorem 4 does not establish nonclassical \(3\)-MOQLS(8)**. Its triple-existence clause requires \(n\ge16\). The directly checked relevant references likewise do not supply that order-eight conclusion through the statements identified below.
- **Conditional only:** independently verified ordinary \(3\)-MOQLS(8), with at least one genuinely nonclassical member, would establish \(M(8)\ge3\) under this source’s definition. Combined with the source’s upper bound, that would give \(3\le M(8)\le5\), improving the **lower endpoint of the pinned table**, not establishing current novelty.
- The direct unversioned arXiv listing identifies **v2, revised 27 July 2026**, as its latest listed version. **Current literature-wide status remains unknown.**
- Three families **do not close the registered four-family alternative**.

## 2. Inputs and evidence boundaries

Let:

```text
R = /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h
F = R/review-waves/f125-moqls8-actual-three-family-witness
S = R/public-sources/ballsimoens-2607.12933v2.html
```

Read `F/manifest-v1.json`, `F/parent-inputs-v1/physical-definition-v1.md`, the registered four-family definitions, and relevant exact raw ranges of `S`.

| Input | Declared SHA-256 | Declared bytes / LF | This audit |
|---|---|---:|---|
| `F/manifest-v1.json` | `bc1753bab7dc9efa691a13ab8fa03be2b403172c00b837d503d04a745f74f9f0` | Not supplied in assignment | Read; SHA not recomputed |
| `F/parent-inputs-v1/physical-definition-v1.md` | `3df4d2bec7f566a66508110176e8217c15e38025323b6f19444e70e435c01fff` | 2,115 / 11 | Read; pins not recomputed |
| `F/parent-inputs-v1/witness.json` | `a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413` | 8,040 / 891 | Witness vectors not read or checked |
| `R/written-releases/physics-4-four-family-definitions-v1.md` | `ebfd79fe2fba3aab2d4b61b29688e66199718ff789a3a922c8bc2e38277bdfee` | 1,583 / 9 | Read; pins not recomputed |
| `S` | `f2ef2a3f2493585ce22e022eca571f9c5e2268fd166f6599f3820afdf1b6d5ad` | 274,893 / 1,315 | Relevant source ranges read; pins not recomputed |

Additional public reads were direct arXiv reads of cited papers, identified below. Their displayed versions are recorded; they are **not additional hash-verified frozen inputs**.

No author checker/producer, solver, catalog, held research result, repository test suite, external model, or paid API was used as evidence. No `web_search` was used.

Quotations below preserve wording; mathematical typesetting and whitespace are normalized from the HTML.

## 3. Source definitions and physical-definition correspondence

### 3.1 Quantum Latin squares

**Location:** `S:470`, §2.2, `S2.SS2.p1.1`.  
[Primary source §2.2](https://arxiv.org/html/2607.12933v2#S2.SS2)

> “A quantum Latin square of order \(n\) is an \(n\times n\) matrix over \(\mathbb C^n\) such that each row and each column forms an orthonormal basis of \(\mathbb C^n\).”

**Correspondence:** `physical-definition-v1.md:3` requires precisely this at \(n=8\). Its integer-numerator representation is a witness encoding, not a different mathematical definition. Real vectors are permitted instances of complex vectors; indexing \(0,\ldots,7\) rather than \(1,\ldots,8\) is immaterial.

**Not audited:** whether the supplied arrays actually satisfy these conditions.

### 3.2 Orthogonality and MOQLS

**Location:** `S:494-503`, §2.3, `S2.SS3.p1.1`, `S2.Ex3`, `S2.SS3.p1.2`.  
[Primary source §2.3](https://arxiv.org/html/2607.12933v2#S2.SS3)

> “Two quantum Latin squares \((\psi_{ij})_{1\le i,j\le n}\) and \((\phi_{ij})_{1\le i,j\le n}\) are orthogonal if”
>
> \[
> \{\psi_{ij}\otimes\phi_{ij}:i,j\in\{1,\dots,n\}\}
> \]
>
> “is an orthonormal basis of \(\mathbb C^n\otimes\mathbb C^n\).”

The source then defines a \(t\)-member set as quantum Latin squares:

> “such that any two of them are orthogonal.”

**Correspondence:** the pinned physical definition requires all members in the same cell coordinates, and the complete \(64\times64\) tensor-product Gram matrix for every pair. This is the ordinary, separated-array definition in the source—not merely a same-cell support condition or an entangled/generalized Latin arrangement.

**Not audited:** any actual row, column, normalization, or pairwise Gram entry.

### 3.3 Classical individual squares

**Locations:** `S:475,479,483,486-487`, §2.2.

The allowed isotopy operations are:

> “multiplying each entry by a phase factor,”  
> “permuting rows and columns, and”  
> “applying a unitary transformation on all entries.”

Classicality is defined by:

> “A quantum Latin square is classical or not genuinely quantum if, up to isotopy, all entries are contained in \(\{\ket1,\dots,\ket n\}\), a fixed orthonormal basis.”

**Correspondence:** this agrees with one global output orthonormal frame **per member**, allowing per-cell phases.

**[INFERENCE—definition-level]:** if two normalized entries of a member satisfy
\[
0<|\langle u,v\rangle|^2<1,
\]
that member cannot be classical: entries on rays of one orthonormal basis have squared overlaps only \(0\) or \(1\), and the allowed operations preserve these overlap magnitudes. This justifies the acceptance definition’s proposed nonclassicality criterion; it does **not** certify that the witness has such a pair.

### 3.4 Classical sets: exactly one nonclassical member counts

**Locations:** `S:508,512,516,519`, §2.3.

For sets, the source permits:

> “permuting rows and columns, simultaneously among all squares, and”

and:

> “applying, separately to each square, a unitary transformation to all of its entries.”

It defines a classical set by:

> “if, up to isotopy, all entries are contained in \(\{\ket1,\dots,\ket n\}\).”

**[INFERENCE—definition-level]:** a set is classical exactly when every member is individually classical.

- If the whole set is classical, each member is classical.
- Conversely, for individually classical members, choose their separate global unitaries and cell phases to send their respective frames to the fixed basis. Separate row/column permutations are unnecessary for the property “all entries lie on these basis rays,” so the simultaneous-permutation restriction introduces no obstruction.

Thus, **one nonclassical member plus two classical members is a nonclassical three-member set**, provided all three are valid and mutually orthogonal.

The source expressly corroborates this usage:

**Location:** `S:387`, Theorem 6:

> “then there exist \(|M|\) \(\mathrm{MOQLS}(n)\), exactly one of which is non-classical.”

This is not a requirement that all members share one original output frame.

### 3.5 Definition of \(M(n)\)

**Location:** `S:275`, Introduction, `S1.p2.1`.  
[Primary source definition](https://arxiv.org/html/2607.12933v2#S1.p2)

> “we define \(M(n)\) as the largest value of \(t\) such that a non-classical set of \(t\) \(\mathrm{MOQLS}(n)\) exist”

and:

> “If such a set does not exist, we let \(M(n)=0\).”

Therefore \(M(n)\) counts the **size of the set**, not the number of nonclassical members within it.

## 4. Pinned Table 2 and the upper bound at order eight

**Locations:**

- `S:419`: header cell `S1.T2.2.1.8`, containing `8`.
- `S:439`: corresponding value cell `S1.T2.2.2.8`, containing **`2-5`**.
- `S:451`: caption, “New bounds on \(M(n)\) for \(2\le n\le17\).”

[Primary Table 2](https://arxiv.org/html/2607.12933v2#S1.T2)

The entry means:
\[
2\le M(8)\le5.
\]

**Theorem giving the upper endpoint:** Theorem 5, `S:362`, `Thmtheorem5.p1.1`.

> “Suppose \(n\ge3\). A set of \(n-2\) \(\mathrm{MOQLS}(n)\) is classical. Thus, \(M(n)\le n-3\).”

[Theorem 5](https://arxiv.org/html/2607.12933v2#Thmtheorem5)

At \(n=8\), \(8-3=5\). The earlier Theorem 2 (`S:283`) gives only \(M(8)\le6\), so it is **not** the theorem responsible for Table 2’s upper endpoint \(5\).

This audit identifies the source’s theorem and its arithmetic specialization; it does not independently reprove the theorem.

## 5. Corollary 7 at \(q=8\)

**Location:** `S:402`, `Thmtheorem7.p1.1`.  
[Corollary 7](https://arxiv.org/html/2607.12933v2#Thmtheorem7)

> “If \(q\) is a prime power and \(q-1\) has a proper divisor \(d\neq1\), then there exist \(d-1\) \(\mathrm{MOQLS}(q)\), exactly one of which is non-classical.”

**Exact specialization:**

- \(q=8=2^3\) satisfies the prime-power condition.
- \(q-1=7\).
- The positive divisors of \(7\) are \(1,7\).
- \(1\) is explicitly excluded; \(7\) is not proper.

**Conclusion:** Corollary 7 produces **no applicable nonclassical-set existence conclusion at \(q=8\)**. Substituting \(d=7\) would violate a hypothesis. Its non-applicability is **not a nonexistence theorem**.

The construction discussion independently makes the restriction explicit:

**Location:** `S:968`, §4.1:

> “assuming \(q-1\) is not prime”

For Example 15’s proper multiplicative subgroup at \(q=8\), the only possible subgroup order is \(1\); its displayed count \(|H|-1\) of undetermined directions is then \(0\) (`S:964`).

## 6. Do the listed results already establish nonclassical \(3\)-MOQLS(8)?

### 6.1 Ball–Simoens Theorem 4

[Theorem 4](https://arxiv.org/html/2607.12933v2#Thmtheorem4), citing references [2,5,7,14]:

| Clause and exact location | Source statement | Consequence at \(n=8\) |
|---|---|---|
| `S:298` | “There exists a non-classical \(\mathrm{QLS}(n)\) if and only if \(n\ge4\).” | One member exists. |
| `S:302` | “There exists a non-classical set of \(2\) \(\mathrm{MOQLS}(n)\) if and only if \(n\ge7\).” | A nonclassical pair exists. |
| `S:306` | “If \(n\ge16\), then there exists a non-classical set of \(3\) \(\mathrm{MOQLS}(n)\).” | Does not apply at eight. |

The triple clause is sufficient, not an “if and only if.” It neither proves existence nor nonexistence at eight.

### 6.2 Direct checks of the relevant cited references

| Reference | Exact checked statement/location | Order-eight implication |
|---|---|---|
| **[5] Han–Zang–Zhang–Tian**, arXiv:2507.20154v1 | [Theorem 3.8](https://arxiv.org/html/2507.20154v1#S3.Thmtheorem8): “For \(v\ge4\), there exists a non-classical \(3\)-MOQLS(\(v\)), except possibly for \(v\in\{4,5,\dots,15\}\).” Reader evidence: `artifact://50527:502-506`. | Eight is explicitly exceptional. Theorem 3.7 separately supplies a **pair** at eight, not a triple. |
| **[14] Zang–Facchi–Tian**, arXiv:2111.04055v1 | [Theorem 2.23](https://arxiv.org/html/2111.04055v1#S2.Thmtheorem23), clauses 2–3: \(E_2=\{2,3,4,6,8,18,p,2p,6p:p\ge5\text{ prime}\}\); the triple conclusion requires \(d\notin E_2\cup E_3\). Evidence: `artifact://50570:299-312`. | Eight lies in \(E_2\), so the triple clause does not apply. For the prime-power split in clause 1, \(8=2^3\), \(3=1+2\), and the displayed lower bound is only \(2^1-1=1\). |
| **[2] Ball–Simoens**, arXiv:2603.02334v1 | [Theorem 10](https://arxiv.org/html/2603.02334v1#Thmtheorem10): “There are at most \(n-1\) MOQLS of order \(n\). In case of equality, they are classical”. Its §5 discusses the pair-existence exceptions at orders 4–7. Evidence: `artifact://50526:199-208,891-898`. | These are upper-bound/pair-classification statements, not a nonclassical triple construction at eight. |
| **[7] Huang–Li**, arXiv:2606.27758v1 | [Theorem 5.2](https://arxiv.org/html/2606.27758v1#S5.Thmtheorem2): “There exists a non-classical \(2\)-MOQLS(7).” Its preceding construction converts a QLS with \(n\) disjoint transversals into a **pair**. Evidence: `artifact://50528:1103-1118`. | Does not supply a triple at eight. Maximum cardinality of one QLS is not the number of mutually orthogonal QLS. |

**Product-construction check:** Ball–Simoens Theorem 3 (`S:289`) preserves the minimum number of families in its factors. A nontrivial factorization of eight includes an order-two factor. The cited general bound \(t\le n-1\) permits only one family at order two; this route therefore does not produce three families at order eight.

### 6.3 General construction machinery is not an automatic existence result

Ball–Simoens Theorem 6 (`S:371-387`) requires an actual map \(f:R\to R\) that is **not the sum of an additive map and a constant**, plus a set \(M\) satisfying:

\[
x\mapsto f(x)-mx\quad\text{is a permutation for every }m\in M,
\]
\[
m-m'\in R^*\quad(m\ne m').
\]

A suitable order-eight instance with \(|M|\ge3\) would give the desired set. **No such instantiation was established in this audit.** Failure of Corollary 7 does not rule out other uses of Theorem 6.

At \(q=8\), “additive” means \(\mathbb F_2\)-linear; the source makes this explicit in §4.1 (`S:909`). Merely failing to be affine over \(\mathbb F_8\) is not enough to satisfy the theorem’s non-additivity requirement.

### 6.4 Remaining bibliography coverage

Reference [1], [*Group Invariant Quantum Latin Squares*, arXiv:2501.00196v2](https://arxiv.org/html/2501.00196v2), was checked at its abstract/introduction scope. Its stated main result concerns individual group-invariant QLS and group-algebra isomorphisms, not an identified ordinary three-MOQLS(8) existence theorem.

References [3,8,11] are used for finite-field directions; the displayed application gives Corollary 7, while the later optimality statements at `S:971` concern **odd primes**, not \(8\). References [4,12,13] concern classical planes/MOLS or Frobenius-ring background. References [6,9,10] supply applications or foundational definitions in this paper.

Their complete texts and every possible indirect consequence were **not** exhaustively audited. Therefore the defensible conclusion is:

> **The identified source statements and directly checked relevant existence theorems do not already establish nonclassical \(3\)-MOQLS(8). This is not a certificate that no listed reference, combination of known methods, or other publication can imply it.**

## 7. Latest-version metadata versus CURRENT public status

Directly read: [https://arxiv.org/abs/2607.12933](https://arxiv.org/abs/2607.12933), including its raw HTML.

Observed listing:

> “Submitted on 14 Jul 2026 … last revised 27 Jul 2026 (this version, v2)”

Submission history:

- **v1:** `Tue, 14 Jul 2026 16:05:20 UTC`
- **v2:** `Mon, 27 Jul 2026 07:40:44 UTC`

Comments:

> “Correction of Theorem 6”

Exact returned evidence: `artifact://50481:112,128,165-168`.

Thus **v2 is the latest version listed for this arXiv identifier in the response inspected**. This does not establish that its Table 2 is the latest literature-wide bound. No comprehensive newer-publication or forward-citation screen was performed.

**CURRENT public status of the best known lower bound, or prior public existence of a nonclassical three-member set at eight: UNKNOWN in this audit.**

## 8. Registered four-family target

**Location:** `R/written-releases/physics-4-four-family-definitions-v1.md:5`.

The registration quantifies over:

> “EVERY ordinary complex physical tuple of FOUR pairwise mutually orthogonal QLS(8)”

and asks either to prove every member classical or:

> “exhibit an exact physical four-family with AT LEAST ONE genuinely nonclassical member.”

It expressly includes mixed classical/nonclassical combinations.

A three-member witness neither supplies the fourth member nor proves the universal four-member classicality alternative. **Original target closure: not established, even conditionally on a valid triple.**

## 9. Conditional conclusion table

| Axis | Conclusion | Required qualification |
|---|---|---|
| **Physical validity** | **NOT AUDITED** | No witness-vector arithmetic, dimensions, normalizers, row/column Gram matrices, pairwise tensor Gram matrices, or nonclassical overlap were verified. |
| **Source-definition correspondence** | **Matches at the specification level** | Ordinary QLS, same-cell tensor orthogonality, separate member unitaries and cell phases agree. This is not witness acceptance. |
| **Exactly one nonclassical member** | **Counts as a nonclassical set** | All three members must independently satisfy the physical conditions. |
| **Pinned Table 2** | **Reports \(2\le M(8)\le5\)** | Documentary comparison to the inspected local source; cryptographic pin recomputation remains outstanding. |
| **Conditional numerical consequence** | Valid nonclassical three-member set \(\Rightarrow M(8)\ge3\) | Logical implication only; no actual lower-bound promotion from this audit. |
| **Conditional pinned-table improvement** | Lower endpoint \(2\to3\); with Theorem 5, \(3\le M(8)\le5\) | Does not determine \(M(8)\), improve the upper bound, or certify current priority. |
| **Corollary 7 at eight** | **Inapplicable** | No admissible divisor of seven; not evidence of nonexistence. |
| **Theorem 4 / checked references** | **No identified statement already supplies the triple at eight** | Not exhaustive elimination of earlier constructions or indirect consequences. |
| **CURRENT public status** | **UNKNOWN** | Latest version of this one paper is not latest status of the field. |
| **Four-family target** | **NOT CLOSED** | Three is not four. |
| **Novelty/publication clearance** | **NOT ISSUED** | No novelty, priority, human, independent-family, or formal/kernel certification. |

## 10. Explicit unresolved items

1. Actual finite physical validity and genuine nonclassicality of the claimed witness.
2. Independent SHA-256, byte-count, and LF-count verification of the frozen inputs.
3. Current literature-wide best bounds and whether a nonclassical triple at eight was already public elsewhere.
4. Whether the claimed construction is equivalent to, or a routine instance of, existing constructions.
5. Exact \(M(8)\), and either branch of the registered four-family alternative.
6. Persistence of this report as `F/source-audit-v1.md`, which was not performed by this read-only subagent.

**Disposition:** source-definition correspondence supports the stated **conditional** interpretation. Physical acceptance, current-priority assessment, and original-target closure remain separate and ungranted.
