# F474 — Complete WRITTEN review of the unconditional overlap budget

## 1. Verdict and exact scope

**SUPPORTED at the frozen unconditional scope.**

For an actual T2(11), consisting of the same eleven permutation rows with all 110 directed linear adjacency events distinct and all 99 original directed linear distance-two events distinct, the candidate proves that every six-symbol set \(B\) satisfies
\[
\boxed{11N_6(B)+5N_5(B)+6N_1(B)\le 36-\mu_B.}
\]

The individual-row lower bounds
\[
f(1),\ldots,f(6)=(6,0,0,0,5,11)
\]
are correct and individually sharp. Both stated unconditional multiplicity consequences follow.

**Findings within this scope: 0 FATAL / 0 MAJOR / 0 MINOR.**

This return does **not** review or adopt the separate conditional joint-cut theorems in S1 Sections 5–9. It does not establish \(M=C\), an actual T2(11) witness, unrestricted nonexistence, or attainability of equality in the joint array inequality.

## 2. Input, read-order, and method record

I completely read the manifest, freeze receipt, parent dispatch record, parent live-metadata supply, and all ten declared controls before sending the administrative pre-body ACK. The controls were status-only inputs; no linked held mathematical episode or consumer was opened or used.

After that ACK, I read the entire literal packet in increasing, exact raw windows of at most twenty physical lines: packet lines 1–701, including both source endings. This covers:

- **S1:** displayed source labels 1–670, including the final statement of remaining obligations.
- **S2:** source labels 1–29, including its verification and scope limitations.

The parent-supplied metadata identifies:

| Artifact | SHA256 |
|---|---|
| Manifest | `c6f30efe67ef5c9192463b549bd3b261154b018021d30ce2e1880004cb8f9b94` |
| Freeze receipt | `0894599b41fbfc4416e4a03f3c81432197a82383fe2a16b126e41606c3470d31` |
| Literal packet | `5d4847c632fdb5123d4ca183a610b7830081ce5ea17a56fe2f59d268aff2c015` |
| S1 author candidate | `f803b813a4fd0bc97244e8b2806a8df28f5366de8b52944901260a38aeaee21d` |
| S2 adopted disposition | `2dea1377df9a8a8e42b2380f05b9748bacd96f8fe59c092ec6d904139eeaa78d` |

The supplied counts are manifest 6,404 bytes/107 LF, receipt 1,843 bytes/47 LF, packet 35,214 bytes/701 LF, S1 25,831 bytes/669 LF, and S2 4,603 bytes/29 LF. For S1, my coverage is through displayed logical source label 670; I did not independently count its newline characters.

These live pin/count observations and the clock **2026-10-30T12:05:56-0700 PDT** are **parent-attributed**, not my native execution, start, or completion observations. I did not independently execute hashing or packet byte-equality checks.

All mathematical checking below was written reconstruction using formal parameters and the six expressly prescribed instances in S1’s sharpness table. Those six instances are six cuts of the **same prescribed permutation row**, not six independently constructed array rows. No additional selected instance, private diagnostic, scientific executable, interpreter, CAS, solver, enumeration, replay, author code, sibling return, or new external source was used.

Repository materialization was not attempted under the read-only role. This is the complete review body for parent materialization.

## 3. Exact imports and claim dispositions

The mathematical inputs used are the actual-row definition and the finite-singleton identity stated in S1 lines 134–214 and S2 lines 7–11. I reconstruct that identity below rather than treating prior review or finite-run reports as a substitute for proof.

| Claim | Author locations | Disposition |
|---|---|---|
| Finite singleton accounting and \(W_B=36-\mu_B\) | S1 134–214; S2 7–11 | **SUPPORTED** |
| Individual-row lower bounds \(f=(6,0,0,0,5,11)\) | S1 220–255 | **SUPPORTED** |
| Individual sharpness of all six entries | S1 259–278 | **SUPPORTED** |
| Sum over the same eleven actual rows | S1 280–288 | **SUPPORTED** |
| Tripled-support intersection restriction | S1 23, 290 | **SUPPORTED** |
| Doubled-support exceptional-row bound | S1 24, 292–298 | **SUPPORTED** |
| Conditional \(M=C\) joint-cut conclusions | S1 302–602 | **Outside this review’s mathematical scope** |
| Actual T2(11) existence or unrestricted nonexistence | S1 656–670 | **INCONCLUSIVE; neither is established or claimed** |

No theorem from either public paper mentioned in S1 is imported. Their links were not followed. The historical finite-check descriptions in S2 were read as part of the complete source, but were not executed or counted as this reviewer’s independent finite gate.

## 4. Written reconstruction

### 4.1 Actual linear events and finite singleton accounting

Let \(A\subseteq S\), with \(|A|=b\). Color \(A\) black and its complement white, and append one white vertex \(\infty\) to an actual row:
\[
h_r=(\infty,r_1,\ldots,r_{11}).
\]

For the original linear row, let:

- \(q\) be its number of black runs;
- \(s\) be its number of singleton black runs, including boundary runs;
- \(\tau\) be its number of internal singleton white runs;
- \(d\) count its original black-to-black distance-two events.

A black run of length \(\ell\) contributes
\[
\max(\ell-2,0)=\ell-2+\mathbf 1_{\ell=1}
\]
distance-two events lying inside that run. The remaining black-to-black distance-two events cross exactly one internal singleton white run. Therefore
\[
d=b-2q+s+\tau.
\]

On the augmented cycle, the finite black singletons are precisely the singleton black runs counted by \(s\). This remains true at the original row boundaries because their added neighbor is white \(\infty\). The finite white singletons are precisely the internal singleton white runs counted by \(\tau\). A boundary white vertex cannot become a singleton because it has white \(\infty\) as a neighbor. Hence
\[
w_A(r)=s+\tau.
\]

This justifies the finite-versus-infinity distinction used by the candidate.

For one row, the number of black-to-black adjacency events is \(b-q\). Across all eleven rows, distinctness of the 110 adjacency events exhausts all possible directed adjacency pairs. Consequently,
\[
\sum_r q=11b-b(b-1)=b(12-b).
\]

Original distance-two injectivity, with \(M\) the missing set of ordered distinct pairs, gives
\[
\sum_r d=b(b-1)-\mu_A.
\]

Summing the row identity thus yields
\[
b(b-1)-\mu_A
=11b-2b(12-b)+W_A,
\]
and therefore
\[
\boxed{W_A=b(12-b)-\mu_A.}
\]

In particular, for \(b=6\),
\[
\boxed{W_B=36-\mu_B.}
\]

Every distance-two event used in this derivation is an original linear event \(r_i\to r_{i+2}\), \(1\le i\le9\). No uniqueness condition on augmented wrap events has entered.

For completeness, the actual augmented Hamilton interpretation is also justified by adjacency exhaustion: each finite symbol has ten outgoing and ten incoming original adjacency pairs, so it appears last exactly once and first exactly once among its eleven row occurrences. The added arcs to and from \(\infty\) are therefore exhausted exactly once. Nothing here requires \(M=C\).

### 4.2 Individual-row lower bounds

Fix an actual permutation row \(r\), put
\[
D=O(r)=\{r_1,r_3,r_5,r_7,r_9,r_{11}\},
\]
and fix a six-symbol \(B\subseteq S\). Write \(t=|B\cap D|\).

The augmented cycle alternates across \(D\mid X\setminus D\). Initially all twelve vertices, and thus all eleven finite vertices, are singletons.

Because \(B,D\) are both six-element subsets of an eleven-element set,
\[
1\le t\le6.
\]

**Case \(t=6\).** Then \(B=D\), so
\[
w_B(r)=11.
\]

**Case \(t=5\).** The \(B\)-coloring differs from the \(D\)-coloring at exactly two finite vertices. A vertex’s singleton status depends only on its own color and its two cycle neighbors. Only the two changed vertices and their neighbors can lose singleton status. Their union has at most six vertices, hence at most six finite vertices. Thus
\[
w_B(r)\ge11-6=5.
\]

Overlapping neighborhoods or neighborhoods containing \(\infty\) can only improve this lower bound; no separation assumption is needed.

**Case \(t=1\).** Let \(u\) be the unique element of \(B\cap D\). Here \(B\cup D=S\). The coloring by \(X\setminus B\) differs from the coloring by \(D\) at exactly
\[
\{\infty,u\}.
\]

Complementing all colors preserves singleton status, so it suffices to compare these two colorings. The union of the two changed closed neighborhoods has at most six vertices and contains \(\infty\). It therefore contains at most five finite vertices. At least
\[
11-5=6
\]
finite singletons remain.

This is a comparison of colorings only. It does not treat a set containing \(\infty\) as an original odd-position support.

**Cases \(t=2,3,4\).** Nonnegativity gives
\[
w_B(r)\ge0.
\]

Together these prove
\[
\boxed{w_B(r)\ge f(t),\qquad
f=(6,0,0,0,5,11).}
\]

### 4.3 Direct checks of all six prescribed sharpness instances

Use exactly the author’s prescribed row
\[
r=(1,2,\ldots,11),\qquad
P=\{1,3,5,7,9,11\}.
\]

The following counts use the actual augmented cycle \((\infty,1,\ldots,11)\), with white \(\infty\). The two singleton columns contain only finite vertices.

| Prescribed \(B\) | \(|B\cap P|\) | Black singleton vertices | White singleton vertices | Is \(\infty\) singleton? | \(w_B(r)\) |
|---|---:|---|---|---|---:|
| \(\{2,4,5,6,8,10\}\) | 1 | \(\{2,8,10\}\) | \(\{3,7,9\}\) | No | 6 |
| \(\{2,3,4,8,9,10\}\) | 2 | None | None | No | 0 |
| \(\{1,2,5,6,9,10\}\) | 3 | None | None | No | 0 |
| \(\{1,2,3,7,8,9\}\) | 4 | None | None | No | 0 |
| \(\{1,3,7,8,9,11\}\) | 5 | \(\{1,3,11\}\) | \(\{2,10\}\) | Yes | 5 |
| \(P\) | 6 | \(P\) | \(\{2,4,6,8,10\}\) | Yes | 11 |

The zero entries can be checked directly from their cyclic runs:

- For intersection two, the black runs are \(2,3,4\) and \(8,9,10\); the white runs are \(5,6,7\) and \(11,\infty,1\).
- For intersection three, the black runs are \(1,2\), \(5,6\), and \(9,10\); the white runs are \(3,4\), \(7,8\), and \(11,\infty\).
- For intersection four, the black runs are \(1,2,3\) and \(7,8,9\); the white runs are \(4,5,6\) and \(10,11,\infty\).

For intersection one, the black run \(4,5,6\) is not singleton; the other black runs are the three listed singleton vertices. The white run \(11,\infty,1\) is not singleton; the other white runs are the three listed finite singleton vertices.

For intersection five, the black run \(7,8,9\) is not singleton, and the white run \(4,5,6\) is not singleton. The remaining finite singleton vertices are exactly those listed. Although \(\infty\) is also a singleton, it is excluded from \(w_B(r)\).

For \(B=P\), the augmented cycle has twelve singletons, but its finite count is eleven.

Thus every lower-bound entry is attained by the prescribed full permutation row with the corresponding prescribed cut. This proves **individual-row sharpness**, not simultaneous compatibility of eleven rows, global equality attainability, or existence of a T2(11).

### 4.4 Summation over the same actual array

Fix one \(B\) throughout the eleven-row array. Let \(N_t(B)\) count those actual rows with \(|B\cap O(r)|=t\). Every row belongs to exactly one of the six classes, so
\[
\sum_{t=1}^{6}N_t(B)=11.
\]

Summing the proved pointwise lower bounds over these same rows gives
\[
W_B
=\sum_r w_B(r)
\ge6N_1(B)+5N_5(B)+11N_6(B).
\]

Using the independently reconstructed identity,
\[
\boxed{11N_6(B)+5N_5(B)+6N_1(B)\le36-\mu_B.}
\]

There is no replacement of actual rows by independent binary words, abstract incidences, or disconnected cycle covers. There is also no interchange of arrays between the pointwise bound and the total budget.

### 4.5 Tripled-support consequence

The inequality first implies \(N_6(B)\le3\), since four such rows alone would contribute \(44>36\).

If three rows have odd support \(B\), there are therefore exactly three. Substituting \(N_6(B)=3\) gives
\[
5N_5(B)+6N_1(B)\le3-\mu_B\le3.
\]
Both counts must be zero. Every other support consequently intersects \(B\) in exactly two, three, or four symbols.

This is unconditional. It does **not** give the conditional zero-singleton saturation conclusion: without \(M=C\), the other eight rows have total finite singleton count \(3-\mu_B\), which is not forced to vanish.

### 4.6 Doubled-support consequence

If exactly two rows have odd support \(B\), then
\[
5N_5(B)+6N_1(B)\le14-\mu_B\le14.
\]
Since
\[
5\bigl(N_5(B)+N_1(B)\bigr)
\le5N_5(B)+6N_1(B),
\]
integrality gives
\[
\boxed{N_5(B)+N_1(B)\le2.}
\]

This counts rows, including multiplicity, across the same entire array. It is not merely a bound on the number of distinct exceptional supports.

## 5. Findings and acceptance boundary

**Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR within the assigned unconditional audit.**

The decisive boundaries are maintained:

- Finite singleton counts exclude \(\infty\).
- The \(t=1\) recoloring uses \(\infty\) explicitly, producing a different finite-loss bound from \(t=5\).
- Only the original 99 linear distance-two events are required to be distinct.
- All row bounds are summed for one fixed \(B\) over the same eleven actual rows.
- Individual-row sharpness is not promoted to array feasibility or sharpness of the global inequality.
- \(M=C\) is not assumed or proved.
- The conditional joint-cut results remain outside this return’s mathematical verdict.
- No original T2(11) target is closed.

The independent finite gate is **NOTRUN by this WRITTEN reviewer**. There is no scientific code or execution argv in this return. No independent-family, human, formal/kernel, exhaustive-literature, novelty, or priority verification is claimed. Parent disposition remains required.

## 6. Overall verdict fields

**Overall correctness:** correct, restricted to the frozen unconditional overlap-budget and individual-row-sharpness scope.

**Explanation:** The finite singleton identity, local recoloring bounds, all six prescribed sharpness instances, and the same-array summation reconstruct without a missing assumption. The tripled- and doubled-support consequences follow directly; conditional joint-cut claims and the unresolved full T2(11) target are not accepted by this review.

**Confidence:** 0.99.