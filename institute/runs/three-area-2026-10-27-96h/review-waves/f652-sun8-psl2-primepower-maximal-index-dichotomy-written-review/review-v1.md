# F652 — Full written review

**Reviewer:** ReviewF652PSL2Indices  
**Candidate:** S1, `author-candidate-v1.md`, complete LF1–114  
**Result:** **SUPPORTED at the stated classification-conditional scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

This is a written review, not a parent disposition. The complete review is returned here for parent materialization; no repository write or on-disk `review-v1.md` is claimed.

## 1. Read-order and evidence boundary

Before reading the mathematical packet, I read the complete manifest, freeze receipt, parent metadata supply, actual dispatch receipt, and all 15 status-only controls through their endings. I then sent the required direct **PREBODY ACK** to `agent://Main`.

I subsequently read the entire literal packet, LF1–295, in successive ordered RAW windows of at most 20 LF, including every source ending, **before derivation**. No displayed packet window contained an elision requiring recovery.

The reviewed bindings are those recorded by the supplied parent metadata:

| Input | Coverage | SHA-256 |
|---|---|---|
| Manifest | Complete | `8bb07118d6b465de246b347bc0b2a9b228f579c6a6d4520a71731a021d2d5687` |
| Freeze receipt | Complete | `31dce189eadebad1864f2dcdf286ed4c5c35b1f94762e34bc945b24ef9efd016` |
| Literal packet | LF1–295 | `b5ac82b4cf112cf1f1f0ef9208fe6aab9f2b8a9559bf6da4b2b91d503ba71aea` |
| S1 candidate | LF1–114 | `0014cdf55c7574eca98a8dbbbab036cd6bd56359aa7c96585156f347e08889e2` |
| S2 chronology addendum | LF1–3 | `5db6d8eec5be473760995dd37997d1fcb4d28c4dda8e57674bad9e1ca0b61349` |
| S3 classification excerpts | LF1–75 | `2e60f1c0a3c7a52e1e7d52d67c3d2fce802bd6ccb1fa58309737cb2d8d1c86d9` |
| S4 sparse-quotient bridge disposition | LF1–24 | `58992864735e124aabf00654f27b83ac59fc9f279f2848f9d81c1fcd8ae451f3` |
| S5 normal-extension fibre disposition | LF1–27 | `ee60510ba57ab8ef6459daca9f9127d2270d69c197b82879220ce33708054b71` |
| S6 extension-consolidation disposition | LF1–22 | `8ac1842d6284a329d1eba3652d1795ad2d95b7eb23ea9d88efc4f3a093a16236` |
| S7 non-Helly necessity disposition | LF1–28 | `35094e248fcd01c6ec963b2992711572c297d7eb479295cb3c41a46df4e61b5c` |

These are **parent-supplied hash observations**, not independently recomputed child hashes.

No links, siblings, prior reviewer bodies, old author code, or held payloads were followed. All held episodes and **all** proof, method, selection, planning, verification, confidence, and reporting consumers remained NONINPUT. The historical execution reports embedded in S4 and S7 were not replayed or used as scientific verification.

**Child scientific execution: NOT RUN.** No program, CAS, interpreter, solver, enumeration, test, build, lint, or formatter was run. No new selected mathematical case was introduced.

## 2. Exact imports and supported scope

### Classification import

The non-elementary premise is the maximal-subgroup classification attributed to **Dickson, in Giudici, Theorems 2.1–2.2**, as represented in S3 and used in S1 LF21–30. This review does not independently prove that classification or claim a fresh reading of the linked originals.

The relevant corrected conditions are:

- For even \(q\), maximal subgroups have the Borel, two dihedral, or prime-degree subfield forms. The actual even subfield condition is **\(q_0>2\)**, as explicitly rendered in S3 LF53–55. Allowing \(q_0=2\) in the candidate’s necessary-divisibility list is a harmless enlargement.
- For odd \(q\), the split dihedral entry requires \(q\ge13\); the nonsplit entry excludes **\(q=7,9\)**, as explicitly rendered in S3 LF39 and LF44.
- Odd-characteristic subfields are \(\mathrm{PSL}_2(q_0)\) for odd prime extension degree, and \(\mathrm{PGL}_2(q_0)\) for quadratic extension degree.
- Exceptional \(A_4,S_4\) maximal entries require prime \(q\). A nonprime-\(q\) maximal \(A_5\) can occur only for \(q=p^2\), with \(p\equiv\pm3\pmod {10}\), together with the stated \(q\)-congruence.

The malformed Giudici PDF extractions are not interpreted as equalities. The modern HTML excerpt also preserves the \(A_4\) noncongruence in S3 LF68; that congruence is not needed by this candidate, which uses only the prime-\(q\) restriction.

The interleaved almost-simple-group table in S3 LF16 is **not** a list of additional maximal subgroups of the socle and is not imported.

### Earlier scoped statements

- **S4 LF3–5:** definitions and the \(B_7(N)\le5,\ J_7(Q)\le2\) bridge.
- **S5 LF7–13:** actual-fibre indices, common-representative transport, and necessary capacity constraints.
- **S6 LF7–9:** index multiplication, actual left-coset orientation, and finite-core preservation. No held B/C obligation is imported.
- **S7 LF7 and LF15:** meeting quotient images give genuine disjoint kernel slices and hence noncoprime kernel indices.

The operative elementary arguments are reconstructed below; historical review verdicts or machine-control outcomes are not substitutes for them.

### Supported conclusion

Conditional on the classification import:

1. Every \(\mathrm{PSL}_2(p^f)\), \(f\ge2\), satisfies the original eight-actual-left-coset assertion \(B_7\le7\).
2. For \(q\notin\{4,9\}\), the stronger repeated-proper-label assertion \(J_7\le2\) holds.
3. The cases \(q=4,9\) are proved using actual coset packing, not finite \(J_7\) bounds.
4. The stated normal-extension theorem requires \(B_7(N)\le5\).
5. Under only \(B_7(N)\le7\) and \(J_7(Q)\le2\), the \(6+2\) structure is **necessary only**.

## 3. Per-claim dispositions

“SUPPORTED” below is conditional on the named classification wherever that classification is used.

| Claim and source anchor | Disposition | F/M/m |
|---|---|---|
| Definitions distinguish repeated subgroup labels from disjoint actual cosets; coprime-index and density lemmas, S1 LF9–17 | **SUPPORTED** | None |
| Every proper subgroup index is a multiple of a containing maximal index, S1 LF23–30 | **SUPPORTED** | None |
| Correct even/odd maximal-list consequences and \(q=9\) exclusions, S1 LF25–28; S3 LF9–73 | **SUPPORTED, conditional** | None |
| \(q=8\): indices \(9,36,28\), and overincluded \(84\), S1 LF43 | **SUPPORTED** | None |
| Even \(q=2^f,\ f\ge4\): divisibility by \(q+1\) or \(8\), including all prime-degree subfields, S1 LF43 | **SUPPORTED** | None |
| Odd \(f\ge3\): divisibility by \(q+1\) or \(p^2\), including \(p=3\) and odd-prime subfield degree, S1 LF45 | **SUPPORTED** | None |
| Odd \(f=2,\ p\ge5\): divisibility by \((q+1)/2\) or \(p^2\), including the \(A_5\) and \(p=5\) conditions, S1 LF47 | **SUPPORTED** | None |
| Every displayed \(A,B\) exceeds \(7\); cases exhaust nonexceptional \(f\ge2\), S1 LF34–47 | **SUPPORTED** | None |
| Repeated proper labels give \(J_7\le2\), hence \(B_7\le2\), S1 LF49 | **SUPPORTED** | None |
| Perfectness and small-index exclusions, S1 LF55–59 | **SUPPORTED** | None |
| \(q=4\) index coverage and actual packing in both cases, S1 LF65–72 | **SUPPORTED** | None |
| \(q=4\): \(B_7\le7\), but no finite \(J_7\), S1 LF74 | **SUPPORTED** | None |
| \(q=9\): maximal indices \(6,10,15\); every index-6 subgroup is maximal \(A_5\), S1 LF78 | **SUPPORTED, conditional** | None |
| At most three low-gcd labels of index greater than \(6\), S1 LF80 | **SUPPORTED** | None |
| Self-normalization and same-class 2-transitivity, S1 LF84 | **SUPPORTED** | None |
| Nonconjugate index-6 subgroups force every cross-class pair of cosets to meet, S1 LF86 | **SUPPORTED** | None |
| Transporter representation and row/column classification, S1 LF88 | **SUPPORTED** | None |
| Five-coset complement is a genuine left coset; contained cosets become actual kernel cosets, S1 LF90 | **SUPPORTED** | None |
| \(q=9\): \(B_7\le7\), but no finite \(J_7\), S1 LF92 | **SUPPORTED** | None |
| Conditional normal extension with kernel bound \(5\), S1 LF98 | **SUPPORTED** | None |
| Exactly six full images and two disjoint proper images under the stated bad-family assumptions, S1 LF100–102 | **SUPPORTED, necessary only** | None |
| Kernel pair restrictions and complete displayed \((d,e)\) possibilities, S1 LF104 | **SUPPORTED, necessary only** | None |
| Remaining normal-cut, other-simple-group, and unrestricted-group exclusions, S1 LF106 | **SUPPORTED as scope limitations** | None |
| Author’s historical read order, external-access chronology, and execution history, S1 LF5,110–114; S2 LF3 | **INCONCLUSIVE as independently verified history**; not proof premises | No candidate defect inferred |
| Existence or impossibility of an actual original-bound \(6+2\) family; unrestricted Sun8; novelty | **INCONCLUSIVE / NOT PROVED** | Outside the claimed result |

No reviewed mathematical claim is REFUTED.

## 4. Reconstruction of the maximal-index dichotomy

### 4.1 Passing from maximal subgroups to every proper subgroup

For a proper subgroup \(U<T\), choose a maximal overgroup \(M\). Since \(T\) is finite,

\[
[T:U]=[T:M][M:U].
\]

Thus divisibility of each possible maximal index by \(A\) or \(B\) transfers to **every** proper subgroup index. No assumption that the supplied subgroup is itself maximal is made.

### 4.2 Even characteristic

The maximal-index possibilities used are

\[
q+1,\qquad \frac q2(q+1),\qquad
\frac q2(q-1),\qquad
\frac q{q_0}\frac{q^2-1}{q_0^2-1}.
\]

For \(q=8\), these are \(9,36,28\), and the deliberately overincluded subfield index \(84\). Here \(36\) is divisible by \(9\), and \(84\) by \(28\). Therefore \(A=9,B=28\) works.

For \(q=2^f,\ f\ge4\):

- The Borel and split-dihedral indices are divisible by \(q+1\).
- The nonsplit-dihedral index has 2-adic valuation \(f-1\ge3\), so is divisible by \(8\).
- If \(q=q_0^2\), the subfield index simplifies to \(q_0(q+1)\).
- If \(q=q_0^r\), with \(r\) an odd prime and \(q_0=2^d\), the ratio \((q^2-1)/(q_0^2-1)\) is odd. The index has 2-adic valuation \((r-1)d\). Subject to \(rd\ge4\), this is at least \(4\): either \(r\ge5\), or \(r=3,d\ge2\).

This covers every prime-degree subfield entry, including the quadratic one separately. Consequently \(A=q+1,B=8\) works.

### 4.3 Odd characteristic, \(f\ge3\)

Take \(A=q+1,B=p^2\).

The Borel index equals \(q+1\). Each dihedral order is prime to \(p\), so its index contains \(p^f\).

For an odd-prime-degree subfield \(q=q_0^r\), \(q_0=p^d\), the maximal index has \(p\)-adic valuation

\[
f-d=(r-1)d\ge2.
\]

This remains valid when the extension-degree prime equals the characteristic; no coprimality between \(r\) and \(p\) was used.

For a quadratic subfield, \(f=2d\). Since \(f\ge3\), necessarily \(d\ge2\), and the \(\mathrm{PGL}_2(q_0)\) index has \(p\)-adic valuation \(d\). The factor \(2\) in the odd-characteristic order formula does not affect this valuation.

The classification excludes \(A_4,S_4,A_5\) maximal entries for \(f\ge3\). In particular, \(p=3\) causes no missing exceptional entry and gives \(p^2=9>7\).

### 4.4 Odd characteristic, \(f=2,\ p\ge5\)

Take \(A=(q+1)/2,B=p^2\).

The Borel index is \(2A\), and the quadratic-subfield index is \(pA\). Dihedral indices contain \(p^2\).

A maximal \(A_5\) requires \(p\equiv\pm3\pmod {10}\). This excludes \(p=5\). For the remaining primes \(p\ge7\), \(p\nmid60\), so an \(A_5\) index retains the full \(p^2\) factor of \(|T|\). The prime-only \(A_4,S_4\) cases do not occur here.

All constants exceed \(7\): \(9,28,8\) do so directly; \(q+1>7\) in its assigned cases; \(p^2\ge9\); and \((p^2+1)/2\ge13\) for \(p\ge5\).

The rows cover every \(f\ge2\) except exactly \(q=4,9\).

### 4.5 Repeated labels

Assign each proper subgroup index to one of its valid divisibility classes. Among three labels, two share a class, and their gcd is at least its divisor \(A\) or \(B\), hence exceeds \(7\).

This argument explicitly allows repeated subgroups and repeated indices. It proves \(J_7\le2\), not merely a statement about selected actual cosets or quotient shadows.

## 5. Reconstruction of the exceptional actual-coset arguments

### 5.1 Elementary exclusions

The unipotent identities in S1 LF55 generate \(\mathrm{SL}_2(q)\). A nonzero \(t\) with \(t^2\ne1\) exists for \(q\ge4\), and conjugation by \(\operatorname{diag}(t,t^{-1})\) gives the displayed upper-unipotent commutator identity. The corresponding lower identity gives perfectness of \(\mathrm{SL}_2(q)\), hence of its projective quotient.

A proper subgroup of index \(2,3,4\) would give a nontrivial permutation image in the solvable group \(S_4\), impossible for a perfect group.

The stated \(A_5\) commutator argument likewise gives perfectness: inversion of a 3-cycle by the specified even permutation makes that 3-cycle a commutator, and 3-cycles generate \(A_5\).

### 5.2 \(q=4\)

The order is \(60\). Lagrange and perfectness leave the overinclusive proper-index list

\[
5,6,10,12,15,20,30,60.
\]

If index \(5\) occurs, actual disjointness and the coprime-index lemma force all other indices to be divisible by \(5\). There is at most one label among \(10,20,30,60\), and at most one of index \(15\). Five index-5 cosets fill the group; otherwise there are at most four of them and two additional cosets.

If index \(5\) does not occur, indices greater than \(6\) contribute at most three labels: one from \(10,20,30,60\), one of index \(12\), and one of index \(15\). Six index-6 cosets fill the group; at most four give at most seven total members. For five index-6 cosets and three further members, the further indices must be \(12,15\), and \(10\) or \(20\), because \(30,60\) violate a pairwise gcd bound. Their density is at least

\[
\frac1{12}+\frac1{15}+\frac1{20}=\frac15>\frac16,
\]

exceeding the remaining space.

Thus eight disjoint low-gcd actual cosets cannot exist. This is a packing proof, not a label-only argument. The genuine index-5 point stabilizer separately defeats every finite \(J_7\) bound by repetition.

### 5.3 \(q=9\): index coverage

The corrected maximal list gives indices \(6,10,15\). An index-6 subgroup must itself be a maximal \(A_5\).

Among low-gcd labels of index greater than \(6\), there is at most one divisible by \(10\), and at most one divisible by \(15\). Every remaining index is \(6m\), not divisible by \(5\), and its subgroup lies in an index-6 \(A_5\). Hence \(m>1\), \(m\mid60\), and \(5\nmid m\). The possibilities are \(2,3,4,6,12\); perfectness excludes the first three. The resulting original indices \(36,72\) allow at most one further label. This proves the bound of three, including repetitions.

### 5.4 \(q=9\): genuine transporter packing

For an index-6 subgroup \(H\), maximality makes \(N_X(H)\) either \(H\) or \(X\). The latter would make \(H\) normal with a nontrivial solvable quotient of order \(6\), contradicting perfectness. Therefore \(N_X(H)=H\).

In the six-point action on \(X/H\), \(H\) fixes exactly one point. Every other orbit has size at least \(5\), since \(A_5\) has no subgroup of index \(2,3,4\). The remaining five points form one orbit, establishing 2-transitivity without importing simplicity or an identification with \(A_6\).

For nonconjugate index-6 subgroups \(H,K\), the action of \(H\) on \(X/K\) has no fixed point. Its six points therefore form one orbit. Thus \(HK=X\), which implies that **every** left \(H\)-coset meets **every** left \(K\)-coset. Disjoint index-6 cosets must consequently come from one conjugacy class.

Within that class every actual left coset is a transporter

\[
T_{x,y}=\{g\in X:g(x)=y\}.
\]

Two distinct transporters are disjoint exactly when they share a first coordinate or share a second coordinate. Different first and second coordinates give an intersection by 2-transitivity. Three or more pairwise-disjoint transporters must therefore occupy one row or one column.

Five such cosets have complement precisely the missing transporter. A column causes no orientation defect: its missing transporter is still an actual **left** coset of the stabilizer of its first coordinate.

Write this complement \(D=dK\). If another coset \(aU\) is contained in \(dK\), then \(d^{-1}a\in K\) and \(U\le K\). Thus two additional contained cosets, translated by the same \(d^{-1}\), become genuine disjoint left \(K\)-cosets. Their original indices are \(6m,6n\), so the low-gcd condition forces

\[
6\gcd(m,n)\le7,\qquad \gcd(m,n)=1.
\]

The coprime-index lemma forbids their disjointness.

Therefore five index-6 cosets leave room for at most one additional member; six leave none; and at most four index-6 cosets together with at most three others give at most seven. This proves \(B_7(\mathrm{PSL}_2(9))\le7\) using genuine actual cosets. Repeating its index-6 \(A_5\) as a label shows that \(J_7\) is not finite.

## 6. Normal-cut reconstruction and limits

For \(N\triangleleft G\),

\[
n_i=[G:U_i]=a_i b_i,\qquad
a_i=[G/N:\pi(U_i)],\quad
b_i=[N:N\cap U_i].
\]

Over one common fibre \(Nt\), choose an element \(h_it\) of each nonempty slice. Right translation by the **same** \(t^{-1}\) turns that slice into

\[
h_i\bigl(t(U_i\cap N)t^{-1}\bigr),
\]

an actual left \(N\)-coset of index \(b_i\). Common translation preserves disjointness; the subgroup conjugation preserves index.

### Conditional extension

The \(J_7(Q)\le2\) hypothesis permits at most two proper quotient labels in a bad eight-family. At least six image cosets are therefore all of \(Q\), so one fibre contains six disjoint low-gcd \(N\)-cosets. This contradicts **\(B_7(N)\le5\)**.

The argument does not replace that kernel bound by \(7\).

### Necessary \(6+2\) structure

Assume instead \(B_7(N)\le7,\ J_7(Q)\le2\), and an actual bad eight-family.

There are at most two proper images. With zero or one, all eight image cosets have a common quotient point, giving eight bad slices in one fibre. Hence there are exactly two proper images and six full images. The two proper images must be disjoint for the same reason.

Their actual disjointness yields

\[
2\le d=\gcd(a_7,a_8)\le7.
\]

Each of the six full images meets each proper image. Applying the actual-fibre argument separately to those pairs gives

\[
2\le\gcd(b_j,b_7),\gcd(b_j,b_8)\le7.
\]

The fibres used for the two proper images need not coincide.

Finally, for \(e=\gcd(b_7,b_8)\),

\[
de\mid\gcd(n_7,n_8)\le7.
\]

With \(d\ge2\), this gives exactly the displayed alternatives: \(e=1,\ 2\le d\le7\), or \((d,e)=(2,2),(2,3),(3,2)\).

These are **necessary constraints**, not a construction, exclusion, compatibility theorem, or sufficient gluing criterion. They do not establish normal-extension closure under the two original bound-7 assumptions. The \(q=4,9\) quotients cannot be inserted into this argument using \(J_7\le2\), which fails for them.

## 7. Final disposition

The entire candidate has been reconstructed at its advertised conditional scope. No mathematical correction is required before considering that scoped result for parent disposition.

The classification itself remains an explicit external import. Author chronology and historical nonexecution statements are not independently certified by this review. The prospective finite-verifier paragraph supplies no implemented verifier or finite-execution evidence. No result concerning f113 is imported or adjudicated.

No all-group, all-simple-group, unrestricted normal-cut, novelty, human, independent-model-family, or kernel-verification claim follows.

**overall_correctness:** correct

**explanation:** Conditional on the precisely corrected Dickson/Giudici maximal-subgroup classification, the maximal-index dichotomy covers every nonexceptional prime power with \(f\ge2\), including repeated proper labels. Both exceptional cases use valid actual-coset packing arguments, and the normal-cut conclusions remain at the stated conditional-extension and necessary-only scopes.

**confidence:** 0.98