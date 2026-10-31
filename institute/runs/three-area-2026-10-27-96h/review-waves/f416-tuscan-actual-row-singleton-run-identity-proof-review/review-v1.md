# F416 WRITTEN review: actual-row singleton budget and parity-support multiplicity

**Intended materialization:** `review-waves/f416-tuscan-actual-row-singleton-run-identity-proof-review/review-v1.md`

**Result:** **0 FATAL / 0 MAJOR / 0 MINOR findings.** The exact singleton-run identity, uniform odd-order multiplicity bound, T2(11) branch exclusions, and stated conditional three-row boundary are supported by the written argument.

**Acceptance boundary:** This is one same-harness independent written reconstruction. It is not finite verification, formal verification, novelty clearance, unrestricted T2(11) resolution, or parent adoption. The candidate remains **UNREVIEWED for integration until parent disposition**.

## 1. Input, read-order, and execution record

Before mathematical packet reads, I read:

- The complete manifest, LF 1–102.
- The complete freeze receipt, LF 1–60.
- The dispatch receipt and complete parent live-metadata supply.
- All seven manifest-listed status-only controls through their endings.

I then sent the required administrative pre-body ACK to `agent://Main`; delivery was confirmed before opening the mathematical packet.

I read the complete literal packet, packet LF 1–597, in ordered raw windows of at most 20 LF, including every source ending:

| Packet source | Complete coverage | Supplied SHA256 |
|---|---:|---|
| S1, author candidate | Logical lines 1–548; metadata reports 547 LF | `b56de28c6218849e9200689115b0da20bcbf43d6c786a12ae2d06603ef804d85` |
| S2, adjacency-row/closing-pair disposition | 1–22 | `72d608050ac1f115057fc89e2135ce700db38681636081f3f9b6ab7d90b935c5` |
| S3, actual-T1 closing-parity disposition | 1–25 | `1cfc3b41f42ba9fa118ae1f12790f350f8399876b460c0454db5e04618fe5368` |

The manifest and receipt pins are those supplied in the assignment and parent metadata:

- Manifest: `356818f6c55f43dd4e0232cc3ed75fb80cb31b7b36089690f0f94c677d3e8500`.
- Receipt: `d78f860ee6cbd38952de03bb3dde8a10905afd9b0bc20484f76e3d95347ae1d6`.
- Packet: `8e03c103cd6512431e9d99140e704202f5c9b28ff73f4006c6629869c8108147`.

These are **parent-supplied metadata**, not independently executed reviewer hashes. No native reviewer clock or duration is claimed.

No scientific executable, CAS, interpreter, solver, enumeration, replay, test, build, linter, formatter, or external-model CLI was run. No new selected mathematical instance was introduced. The empty/full subset boundaries, the assigned \(m=2\) boundary, and the assigned \(n=11\) specialization are addressed below by written reasoning.

No author code, sibling mathematical return, linked prior reviewer body, or held scientific payload was opened. An administrative process listing exposed job names/status only, not mathematical outcomes. Status controls were not used as mathematical premises.

Repository writing is barred by the active read-only role. This response supplies the complete review body for parent materialization; no filesystem-write bypass was attempted.

## 2. Exact scope and imports

The caller is an **actual** T2\((n)\):

- \(S\) is an \(n\)-element symbol set.
- There are exactly \(n\) rows, each a permutation of \(S\).
- Directed distance-one events are distinct.
- Directed distance-two events are distinct, counted only at linear positions \(i\to i+2\), \(1\le i\le n-2\).

The budget theorem is quantified over every \(n\ge3\), every such array, and every \(B\subseteq S\), including \(B=\varnothing\) and \(B=S\).

The odd-order theorem is quantified over every integer \(m\ge2\), \(n=2m-1\), every actual T2\((n)\), and every \(m\)-element subset \(B\subseteq S\).

Only the actual-row adjacency and augmentation interfaces from S2 LF 5, 9, 16 and S3 LF 15 are relevant imports. They are reconstructed below. The closing-permutation derangement theorem, product-sign identity, earlier review counts, and historical computational statements are not load-bearing premises here.

No orthogonal-Latin-square assumption, circular Tuscan condition, endpoint cycle-type restriction, second/penultimate-column permutation assumption, or universal equality \(M=C\) is imported.

## 3. Independent written reconstruction

### 3.1 Actual rows, adjacency exhaustion, and Hamilton cycles

**SUPPORTED — S1 LF 81–125.**

There are \(n(n-1)\) directed adjacency slots and exactly \(n(n-1)\) ordered distinct symbol pairs. Distinctness therefore implies exhaustion.

For each symbol \(x\), its \(n-1\) outgoing adjacency events occupy \(n-1\) rows. Since \(x\) appears once in each of the \(n\) rows, precisely one row ends at \(x\). The incoming argument similarly gives precisely one row starting at \(x\).

Thus rows can be indexed by first symbol \(c\), and their last symbols define a permutation \(E(c)\). Since a permutation row has different first and last symbols for \(n\ge2\), \(E(c)\ne c\).

Adjoining the same \(\infty\) to every existing row gives the directed cycle
\[
\infty\to r_{c,1}\to\cdots\to r_{c,n}\to\infty.
\]
It is one Hamilton cycle, not a disconnected cycle cover. Finite-to-finite edges are exhausted adjacency events; edges leaving and entering \(\infty\) are exhausted by the first- and last-column permutations. Hence these cycles partition the complete directed graph on \(S\cup\{\infty\}\) without loops.

The distance-two condition remains a condition on the original linear rows. It does **not** include
\[
\infty\to r_{c,2},\qquad
r_{c,n-1}\to\infty,\qquad
E(c)\to c.
\]
No later count requires uniqueness of those augmented events.

### 3.2 Per-row singleton identity, including boundaries

**SUPPORTED — S1 LF 133–179.**

Fix \(B\subseteq S\), \(|B|=b\). Use the manuscript’s definitions \(q_B,s_B,t_B,d_B\), with black singleton boundary runs included in \(s_B\), but white boundary runs excluded from \(t_B\).

An original distance-two event with both endpoints in \(B\) has exactly one of two forms:

1. Three black entries within one black run.
2. A white singleton between two black entries.

A black run of length \(\ell\ge1\) contributes
\[
\max(\ell-2,0)=\ell-2+\mathbf1_{\ell=1}
\]
events of the first kind. Summing over black runs gives \(b-2q_B+s_B\). The second kind contributes exactly \(t_B\). Consequently,
\[
d_B(r)=b-2q_B(r)+s_B(r)+t_B(r).
\]

The distinction between internal and boundary white singletons is necessary and correctly maintained: a white entry at a linear endpoint cannot be the middle of an original distance-two event.

For \(B=\varnothing\), the black-run sum is empty and every term in the identity is zero. For \(B=S\), the unique black run has length \(n\ge3\), so the identity gives \(d_B=n-2\), as required.

### 3.3 Total black-run count

**SUPPORTED — S1 LF 181–196.**

In a row, black-to-black adjacency events number \(b-q_B(r)\). Across all rows, adjacency exhaustion gives exactly \(b(b-1)\) such events. Therefore
\[
nb-\sum_rq_B(r)=b(b-1),
\]
and hence
\[
\sum_rq_B(r)=b(n-b+1).
\]

This uses actual T1 adjacency exhaustion only. It requires neither distance-two injectivity nor any boundary-column permutation beyond what adjacency exhaustion already implies.

### 3.4 Exact singleton-run budget

**SUPPORTED — S1 LF 198–237.**

Let \(M\) be the missing ordered **distinct** distance-two pairs and
\[
\mu_B=|M\cap(B\times B)|.
\]
Summing the per-row identity and substituting the black-run total gives
\[
\sum_rd_B(r)
=nb-2b(n-b+1)+W_B
=b(2b-n-2)+W_B.
\]

Distance-two injectivity means that the realized pairs internal to \(B\) number exactly
\[
b(b-1)-\mu_B.
\]
Equating these expressions yields
\[
\boxed{W_B=b(n+1-b)-\mu_B},
\qquad
\boxed{W_B\le b(n+1-b)}.
\]

No diagonal pairs have been counted: the relevant universe has \(b(b-1)\), not \(b^2\), pairs.

The full-subset boundary is consistent. For \(B=S\), \(W_B=0\), while the \(n(n-2)\) distinct distance-two events leave exactly
\[
n(n-1)-n(n-2)=n
\]
missing pairs. Thus the right-hand side is \(n-\mu_S=0\). The empty-subset boundary is also zero on both sides.

### 3.5 Hamiltonian singleton interpretation

**SUPPORTED — S1 LF 241–273.**

Color \(\infty\) white. Every finite black singleton run, including a boundary singleton, has white neighbors in the augmented cycle. Every finite white vertex with two black cycle neighbors is an internal white singleton in the original row.

A finite white boundary entry is not a singleton after augmentation, because its neighbor \(\infty\) is also white. The vertex \(\infty\) itself is deliberately excluded from \(W_B\).

Therefore \(s_B+t_B\) is exactly the number of **finite** singleton vertices in the augmented Hamilton cycle. This interpretation is compatible with, but does not enlarge, the original distance-two event set.

The actual single-cycle hypothesis is respected. An arbitrary Latin incidence square with disconnected symbol classes does not automatically supply these linear permutation rows.

### 3.6 Uniform odd-order multiplicity theorem

**SUPPORTED — S1 LF 279–342.**

Let \(n=2m-1\), \(m\ge2\), and \(|B|=m\). A row whose odd-position support is \(B\) has \(m\) singleton black runs and \(m-1\) internal singleton white runs. It contributes exactly \(2m-1\) to \(W_B\).

All other contributions are nonnegative. Hence
\[
(2m-1)k_B\le W_B=m^2-\mu_B,
\]
so
\[
k_B\le\left\lfloor\frac{m^2}{2m-1}\right\rfloor.
\]

For all \(m\ge2\),
\[
\frac m2\le\frac{m^2}{2m-1}<\frac{m+1}{2}.
\]
The upper inequality is equivalent to \(m>1\). If \(m\) is even, this interval lies between the integer \(m/2\) and \(m/2+1/2\). If \(m\) is odd, it lies between \(\lfloor m/2\rfloor+1/2\) and the next integer. Thus
\[
\boxed{\left\lfloor\frac{m^2}{2m-1}\right\rfloor
=\left\lfloor\frac m2\right\rfloor}.
\]

The assigned lower boundary \(m=2\) is included: \(\lfloor4/3\rfloor=1=\lfloor2/2\rfloor\). No existence assertion for that order is needed.

### 3.7 Exact T2(11) exclusions and partition equivalence

**SUPPORTED — S1 LF 346–390.**

For \(n=11\), \(m=6\),
\[
11k_B\le36-\mu_B\le36,
\]
and therefore \(k_B\le3\). Four rows sharing one odd-position support would contribute \(44>36\), so that entire branch is impossible.

Each row has exactly one odd-position support. At most three supports, each with multiplicity at most three, accommodate at most nine rows, not eleven. Thus every actual T2(11) requires at least four distinct odd-position supports.

For any equipartition \(X=A\sqcup B\) with \(\infty\in A\), an actual augmented Hamilton cycle alternates across the partition exactly when cutting it at \(\infty\) gives a row with odd-position support \(B\). Both implications hold because the cycle is the augmentation of that actual row. Consequently, at most three actual row cycles alternate across any fixed \(6+6\) partition.

This is not a conclusion about arbitrary degree-compatible cycle covers or independently chosen abstract incidence data.

### 3.8 Conditional \(M=C\), three-row equality case

**SUPPORTED — S1 LF 394–463.**

Assume additionally \(M=C\), where
\[
C=\{(E(c),c):c\in S\},
\]
and exactly three rows have common support \(B\), \(|B|=6\).

Each such row starts and ends in \(B\), yielding a distinct closing pair in \(B\times B\). Under \(M=C\), these give \(\mu_B\ge3\). Meanwhile the three rows contribute \(33\), so
\[
33\le W_B=36-\mu_B\le33.
\]
Therefore
\[
\mu_B=3,\qquad W_B=33,
\]
and every remaining row contributes zero.

The zero contribution excludes all finite singleton vertices in each remaining augmented cycle. A singleton \(\infty\) would mean that its row also starts and ends in \(B\), producing an additional distinct closing pair in \(B\times B\), contradicting \(\mu_B=3\). Thus **all** monochromatic cyclic runs in those eight cycles have length at least two.

If \(r_i\) counts their black cyclic runs, then
\[
1\le r_i\le3.
\]
The lower bound follows because a single Hamilton cycle contains both colors; the upper bound follows from six black vertices with at least two per run.

There are \(72\) directed cross-partition edges in the augmented complete directed graph. The three alternating cycles use \(36\), leaving \(36\). Each remaining cycle contributes \(2r_i\), giving
\[
\sum_{i=1}^8r_i=18.
\]
This also agrees with the earlier run total: \(\sum_rq_B=36\), and the three alternating rows consume \(18\) black runs.

Consequently, with integer \(u_j=\#\{i:r_i=j\}\),
\[
u_1+u_2+u_3=8,\qquad u_1+2u_2+3u_3=18
\]
is equivalent to
\[
\boxed{u_3=u_1+2,\qquad u_2=6-2u_1,\qquad 0\le u_1\le3}.
\]
The manuscript correctly does not claim these necessary conditions are sufficient or contradictory.

### 3.9 Three common supports without \(M=C\)

**SUPPORTED — S1 LF 465–473.**

Without \(M=C\), the same three alternating rows give only
\[
0\le\mu_B\le3,\qquad
\sum_{\text{other eight rows}}(s_B+t_B)=3-\mu_B.
\]
There is then no justification for treating their closing pairs as missing pairs. The stronger zero-singleton conclusion is correctly confined to the additional \(M=C\) branch.

## 4. Public-source attribution and novelty boundary

**SUPPORTED at the manuscript’s bounded attribution scope — S1 LF 519–533.**

I inspected the cited [Technion publication record](https://cris.technion.ac.il/en/publications/tuscan-k-squares/). It confirms the Etzion–Golomb–Taylor authorship, 1989 journal citation, and abstract statements concerning computer-found Tuscan-2 squares and nine questions. The polygonal-path and circular-array statements have additional hypotheses; they do not establish unrestricted T2(11) nonexistence.

I also inspected the cited [Rosin arXiv v1 primary text](https://arxiv.org/html/2505.23881v1):

- Its header confirms the title, author, version, and 29 May 2025 date.
- Table 2 includes Tuscan-2 Square.
- Table 6 defines exactly the \(n\)-row permutation-array target used here: adjacency pairs exactly once and distance-two pairs at most once.
- The reported successful Handbook problem types and accompanying results discussion do not report an open Tuscan-2 instance solved in that study.

These observations support the manuscript’s limited statements about those sources. They do **not** establish complete current T2(11) status.

**INCONCLUSIVE:** novelty, priority, independence from every known Tuscan invariant, and full-literature comparison. I did not read the complete 1989 paper. The author’s historical HTTP 403 and research chronology remain reported history, not independently verified reviewer events. None is needed for the proof.

## 5. Claim dispositions and remaining obligations

| Claim | Disposition |
|---|---|
| Per-row identity \(d_B=b-2q_B+s_B+t_B\), including boundaries | **SUPPORTED** |
| Actual-T1 total \(\sum q_B=b(n-b+1)\) | **SUPPORTED** |
| Actual-T2 equality \(W_B=b(n+1-b)-\mu_B\) for every subset | **SUPPORTED** |
| Uniform odd-order bound \(k_B\le\lfloor m/2\rfloor\), \(m\ge2\) | **SUPPORTED** |
| T2(11) exclusion of support multiplicity at least four | **SUPPORTED** |
| T2(11) requirement of at least four distinct supports | **SUPPORTED** |
| Equivalent bound for actual Hamilton cycles across a fixed equipartition | **SUPPORTED** |
| Conditional \(M=C,\ k_B=3\) equality and remaining run-count constraints | **SUPPORTED** |
| Broader \(k_B=3\) residual without \(M=C\) | **SUPPORTED** |
| Exclusion of the three-row branch | **INCONCLUSIVE — not proved or claimed** |
| Universal \(M=C\) | **INCONCLUSIVE — not proved or assumed** |
| Unrestricted actual T2(11) existence/nonexistence | **INCONCLUSIVE — unresolved by this candidate** |
| Finite canonical checks, formal verification, novelty | **Not performed / not established by this WRITTEN gate** |

The original target still requires either an actual eleven-row witness with independently verified 110 adjacency and 99 distance-two events, or a proof excluding every remaining actual-row configuration. The present argument does neither.

**Scientific code status:** No code is required for this written proof reconstruction; no checker was authored or run. Finite canonical checking remains a separate verification gate, not an implied result of this review.

## 6. Findings and verdict

**Findings:** None. **0F / 0M / 0m.**

**Overall correctness: correct.**

The frozen manuscript supports its exact universally quantified singleton budget and support-multiplicity exclusions, with the three-row equality analysis correctly restricted to \(M=C\). It does not resolve unrestricted T2(11), exclude the remaining three-row branch, establish novelty, or authorize adoption before parent disposition.

**Confidence: 0.98** for this written mathematical correctness assessment; no additional assurance is asserted for unobserved execution, chronology, finite verification, or novelty.