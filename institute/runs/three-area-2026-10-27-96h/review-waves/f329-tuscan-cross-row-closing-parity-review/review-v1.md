# f329 — Written review of f327 closing-permutation parity

## Verdict and scope

**SUPPORTED at same-harness written-review scope. No FATAL, MAJOR or MINOR mathematical defect found.**

For an arbitrary actual \(T1(n)\), \(n\ge2\), with rows indexed by first symbol \(c\), endpoint permutation \(E\), and closing permutation \(\pi_c\) on \(S\setminus\{c,E(c)\}\), the necessary identity is
\[
\boxed{\prod_{c\in S}\operatorname{sgn}(\pi_c)
=(-1)^{n(n+1)/2}\operatorname{sgn}(E).}
\]

At \(n=11\), the exponent is \(66\), giving
\[
\boxed{\prod_{c\in S}\operatorname{sgn}(\pi_c)=\operatorname{sgn}(E).}
\]

This supports only the stated necessary compatibility condition. **No \(T2(11)\) boundary/profile branch is excluded.** No existence, nonexistence, sufficiency, axiomatic-independence or novelty conclusion is established.

**Publication status:** both attempted own-wave writes were refused by the tool’s filesystem-path restriction. The administrative pre-body ACK was successfully delivered directly to `agent://Main` before packet reads. This complete review is the direct-return fallback for parent materialization; no filesystem publication or bypass is claimed.

## Frozen inputs and source notation

The labels below refer to the **f329 packet**:

| Source | Complete assigned coverage |
|---|---|
| S1 — f327 AUTHOR candidate | LF1–199 |
| S2 — adopted adjacency/closing disposition | LF1–22 |
| S3 — adopted distance-two count/boundary disposition | LF1–30 |
| S4 — adopted sign/boundary disposition | LF1–17 |

The author’s earlier input numbering in S1 LF30 is not the numbering of this review packet.

Live metadata SHA-256 checks matched:

- Manifest: `2caf68ebb48cc32ce57ea644c46000eaff8707a507e4d3bc7d61e78f734080aa`
- Freeze receipt: `5296b95620c5dad0f5a29c223de982f942ff107a89531abd695531fc78f06009`
- Literal packet: `e1bd9e7474cdcda26842a47c3b20a1a8d96ac41b82ee2b5df08c0805bb481327`
- S1: `1f6cd32010cc799690ef10c9483a48af046f112e78c532450ff945b570e7d2e0`
- S2: `72d608050ac1f115057fc89e2135ce700db38681636081f3f9b6ab7d90b935c5`
- S3: `0b050abc36ad9146a5b8ff2081047d7d34fd5a9c2ec31617cb47ddce875dc377`
- S4: `f8926010da34cb4460fd4b172e74a310b1629311499c7a3ceccb7c08c5464f82`

All six status-control hashes also matched their manifest pins. Status controls, historical examples and diagnostic accounts are not mathematical premises. No excluded link was followed.

## 1. Assumptions and endpoint laws

Assume only:

1. \(S\) is a set of size \(n\ge2\).
2. There are \(n\) separately retained, directed linear rows, each a permutation of \(S\).
3. Their adjacency events are pairwise distinct.

No distance-two injectivity, symmetry, missing-pair graph hypothesis or second/penultimate-column permutation hypothesis is imposed.

There are \(n(n-1)\) adjacency slots and precisely \(n(n-1)\) possible ordered pairs of distinct symbols. The slots therefore exhaust those pairs, giving the well-defined \(\rho(a,b)\) of S2 LF9,16.

For a symbol \(u\), let \(f(u)\) be its first-column multiplicity. It has \(n-f(u)\) incoming adjacency events, whose sources are distinct and belong to the \(n-1\) other symbols. Hence \(f(u)\ge1\). Because \(\sum_u f(u)=n\), every \(f(u)=1\).

The outgoing-adjacency argument likewise shows that every last-column multiplicity is one. Consequently rows are uniquely indexed by their first symbols \(c\), and their last symbols define a permutation \(E\). Since \(n\ge2\), each row has different first and last symbols, so
\[
E(c)\ne c.
\]
Write \(\lambda=E^{-1}\).

This establishes the endpoint inputs for general \(T1\) directly, rather than silently extending a \(T2\) boundary assertion. It is consistent with the imported first/last-column law in S4 LF8.

## 2. Augmented incidence square and all bijections

Put
\[
X=S\cup\{\infty\},\qquad N=n+1.
\]

Encode each actual row \(r\) by its successor cycle beginning at \(\infty\), traversing that existing row from first symbol \(r\) to last symbol \(E(r)\), and returning to \(\infty\). This does **not** assert any circular distance-two Tuscan property.

For \(x\ne y\), define \(H(x,y)\) as the unique augmented-row label containing \(x\to y\), and set \(H(x,x)=\infty\). The off-diagonal cases are exhaustive:

\[
\begin{aligned}
H(a,b)&=\rho(a,b) &&(a,b\in S,\ a\ne b),\\
H(\infty,c)&=c &&(c\in S),\\
H(a,\infty)&=\lambda(a) &&(a\in S).
\end{aligned}
\]

Define
\[
\sigma_a(b)=H(a,b),\qquad \tau_c(b)=H(b,c).
\]

For finite \(a\), its original outgoing adjacencies occur in exactly the rows
\[
S\setminus\{\lambda(a)\}.
\]
Every row except the unique row ending at \(a\) contributes one such adjacency. Target \(\infty\) supplies label \(\lambda(a)\), and diagonal target \(a\) supplies label \(\infty\). Thus \(\sigma_a:X\to X\) is bijective.

Dually, incoming original adjacencies to finite \(c\) occur in exactly the rows \(S\setminus\{c\}\). Source \(\infty\) supplies label \(c\), and source \(c\) supplies label \(\infty\). Thus \(\tau_c:X\to X\) is bijective.

The exceptional-coordinate maps are exactly
\[
\sigma_\infty=\mathrm{id}_X,
\qquad
\tau_\infty=\widehat{E^{-1}},
\]
where the hat means extension fixing \(\infty\). Therefore \(H\) is Latin.

For each \(r\in X\), let \(h_r(x)\) be the unique \(y\) with \(H(x,y)=r\). Latin row uniqueness defines this map; Latin column uniqueness makes it a permutation. For finite \(r\), its arcs are precisely those of the **single augmented actual row** \(r\), so it is one cycle of length \(N\), not an arbitrary cycle cover. For \(r=\infty\), it is the identity. Hence
\[
\operatorname{sgn}(h_r)=(-1)^{N-1}=(-1)^n
\quad(r\in S),
\qquad
\operatorname{sgn}(h_\infty)=1.
\]
The symbol-sign product is therefore
\[
Q:=\prod_{r\in X}\operatorname{sgn}(h_r)=(-1)^{n^2}.
\]

This verifies S1 LF36–77, including both infinity maps. The one-Hamilton-cycle statement is the load-bearing actual-position input; degree information alone would not establish it.

## 3. Closing map, orientation and inverse sign

Fix arbitrary \(c\in S\), put \(a=E(c)\), and use right-to-left composition. Define
\[
\Phi_c=\tau_c^{-1}\circ\sigma_a.
\]

The endpoint identities give
\[
\begin{aligned}
\Phi_c(\infty)&=\infty
&&\text{because }H(a,\infty)=c=H(\infty,c),\\
\Phi_c(a)&=c
&&\text{because }H(a,a)=\infty=H(c,c),\\
\Phi_c(c)&=a
&&\text{because }\sigma_a(c)=H(a,c)=\tau_c(a).
\end{aligned}
\]

As \(a\ne c\) and \(\Phi_c\) is bijective,
\[
K_c=S\setminus\{a,c\}
\]
is invariant. On this set its defining equation is
\[
\rho(a,b)=\rho(\Phi_c(b),c).
\]

For \(a=E(c)\), both
\[
\rho(a,\cdot):S\setminus\{a\}\longrightarrow S\setminus\{c\}
\]
and
\[
\rho(\cdot,c):S\setminus\{c\}\longrightarrow S\setminus\{c\}
\]
are bijections onto the same row-label set. Their adopted correspondence sends \(c\) to \(a\), and restricts to \(\pi_c\) on \(K_c\). Thus
\[
\Phi_c|_{K_c}=\pi_c,
\]
in the source-to-target orientation of S2 LF11,16, **not its inverse**.

The disjoint decomposition of \(\Phi_c\) consists of \(\pi_c\), the transposition interchanging \(a,c\), and fixed \(\infty\). Consequently
\[
\begin{aligned}
-\operatorname{sgn}(\pi_c)
&=\operatorname{sgn}(\Phi_c)\\
&=\operatorname{sgn}(\tau_c^{-1})
  \operatorname{sgn}(\sigma_{E(c)})\\
&=\operatorname{sgn}(\tau_c)
  \operatorname{sgn}(\sigma_{E(c)}).
\end{aligned}
\]

The inverse contributes no extra minus:
\[
\operatorname{sgn}(g^{-1})=\operatorname{sgn}(g)
\]
for every permutation \(g\).

Let
\[
P=\prod_{c\in S}\operatorname{sgn}(\pi_c),\quad
R=\prod_{a\in X}\operatorname{sgn}(\sigma_a),\quad
C=\prod_{c\in X}\operatorname{sgn}(\tau_c).
\]
Multiplication over \(c\), reindexing the \(\sigma\)-factors by the genuine permutation \(E\), gives
\[
RC=(-1)^n P\,\operatorname{sgn}(\widehat{E^{-1}})
   =(-1)^n\operatorname{sgn}(E)P.
\]

Here \(\tau_\infty\) really is \(E^{-1}\), not \(E\) as a map; only their signs are equal.

These calculations verify S1 LF81–119 and its general form at LF161–165.

## 4. Universal Latin sign identity on \(X\times X\)

All signs are signs of permutations of the specified finite sets and do not depend on an ordering used to represent them.

Define permutations of \(X\times X\):
\[
\begin{aligned}
A(x,y)&=(x,H(x,y)),\\
B(x,y)&=(H(x,y),y),\\
D(x,z)&=(h_z(x),z),\\
T(x,y)&=(y,x).
\end{aligned}
\]

Their bijectivity and signs follow from their fiber actions:

- \(A\) acts by \(\sigma_x\) on the fiber with first coordinate \(x\), so \(\operatorname{sgn}(A)=R\).
- \(B\) acts by \(\tau_y\) on the fiber with second coordinate \(y\), so \(\operatorname{sgn}(B)=C\).
- \(D\) acts by \(h_z\) on the fiber with second coordinate \(z\), so \(\operatorname{sgn}(D)=Q\).
- \(T\) fixes the diagonal and exchanges the two elements belonging to each unordered pair of distinct coordinates. Thus
  \[
  \operatorname{sgn}(T)=(-1)^{N(N-1)/2}.
  \]

For arbitrary \(x,y\), the defining equation for \(h\) gives
\[
h_{H(x,y)}(x)=y.
\]
Therefore
\[
D\circ A(x,y)=(y,H(x,y))=T\circ B(x,y).
\]

Taking signs yields \(QR=\operatorname{sgn}(T)C\). Multiplying by \(C\), using \(C^2=1\), proves
\[
\boxed{RCQ=(-1)^{N(N-1)/2}.}
\]

This establishes S1 LF123–146 without selecting any particular square or permutation.

## 5. Exponents, lower boundary and \(n=11\)

Substitute
\[
N=n+1,\qquad
RC=(-1)^n\operatorname{sgn}(E)P,\qquad
Q=(-1)^{n^2}
\]
into the universal identity:
\[
(-1)^{n+n^2}\operatorname{sgn}(E)P
=(-1)^{n(n+1)/2}.
\]

Because \(n+n^2=n(n+1)\) is even, the closing-transposition and symbol-cycle contributions cancel. Since \(\operatorname{sgn}(E)^2=1\),
\[
\boxed{P=(-1)^{n(n+1)/2}\operatorname{sgn}(E).}
\]

The exponent is \(n(n+1)/2\), coming from augmented order \(n+1\). There is no residual extra \(n\), and no sign change from taking an inverse.

### Lower boundary

At \(n=2\), \(K_c\) is empty. Its unique empty-set permutation has sign \(+1\); the same disjoint decomposition and all \(X\times X\) maps remain valid. The endpoint map is fixed-point-free on the two-element set, hence has sign \(-1\), while \(n(n+1)/2\) is odd. Thus the displayed identity remains consistent.

This is the forced abstract boundary analysis, not a selected labeled row or permutation.

### Symbolic specialization to \(n=11\)

The proved formula gives
\[
n(n+1)/2=66,
\qquad
\boxed{\prod_{c\in S}\operatorname{sgn}(\pi_c)=\operatorname{sgn}(E).}
\]

Equivalently, if \(o\) denotes the number of odd closing permutations,
\[
(-1)^o=\operatorname{sgn}(E).
\]

Tracking the unsimplified factors gives \(RC=-\operatorname{sgn}(E)P\), \(Q=-1\), and Latin-sign right side \(+1\), confirming the same cancellation directly within the symbolic specialization.

This supports S1 LF13–28,150–165.

## 6. Exact \(T1/T2\) separation and live boundary cases

The parity theorem requires only \(T1\).

For the separate closing/missing-pair interpretation, a fixed point \(b\) of \(\pi_c\) is exactly
\[
\rho(E(c),b)=\rho(b,c).
\]
In a permutation row, those two directed adjacencies are consecutive through the same middle symbol. They therefore give a distance-two occurrence \(E(c)\to c\). Conversely, such a distance-two occurrence supplies the same fixed point.

**This local equivalence already holds under \(T1\)**, as S2 LF9 states. In particular, missing at distance two is equivalent to absence of a fixed point.

What the adopted \(T2\) package additionally supplies is distance-two uniqueness and
\[
|M|=n,
\]
from \(n(n-2)\) distinct directed distance-two events—S2 LF9–11,16 and S3 LF7–13.

The closing-pair set
\[
C_{\mathrm{cl}}=\{(E(c),c):c\in S\}
\]
has \(n\) distinct nonloop pairs. Under \(T2\), all \(\pi_c\) being derangements is equivalent to \(C_{\mathrm{cl}}\subseteq M\); equal cardinalities then make this equivalent to
\[
M=C_{\mathrm{cl}}.
\]
S1 LF28,175 are valid at this adopted-package scope; the local fixed-point test itself does not require \(T2\).

No part of the parity proof uses \(\alpha_1\) or \(\alpha_{n-2}\). For \(n=11\), it therefore applies in the both-permutation-boundary branch and every still-possible full-source/full-target or mixed branch. It neither asserts those branches are realizable nor excludes them.

It does not replace the repaired rule that \(M\) is a permutation digraph only when **both** relevant boundary columns are permutations—S3 LF17,23,28–30 and S4 LF15–17.

The equation is a necessary compatibility constraint involving actual row-position incidence. No independence from all other structural facts has been proved. Its ability to eliminate a profile, conditional \(M\) cycle type, mixed boundary branch, or \(M=C_{\mathrm{cl}}\) derangement branch remains **INCONCLUSIVE**. No hypothetical missing-pair graph has been assumed realizable.

## 7. Per-claim disposition and findings

| Claim | Disposition | Source LF |
|---|---|---|
| Latin incidence, infinity maps and Hamilton symbol classes | **SUPPORTED** | S1 LF36–77 |
| Closing-map orientation, transposition and sign product | **SUPPORTED** | S1 LF81–119,161–165 |
| Universal Latin sign identity | **SUPPORTED** | S1 LF123–146 |
| General parity identity and author C1/CP at \(n=11\) | **SUPPORTED** | S1 LF13–28,150–165,185 |
| Author C2: directed, separately indexed rows; no second/penultimate-column assumption | **SUPPORTED** | S1 LF169–177,186 |
| \(T2\), \(M=C_{\mathrm{cl}}\), and derangement interpretation | **SUPPORTED at the exact adopted interface scope** | S1 LF175; S2 LF9–11,16 |
| Author C3: branch exclusion or construction consequences | **INCONCLUSIVE** | S1 LF179–187 |

**REFUTED claims:** none within the asserted necessary-condition scope.

**Findings:** FATAL **0**; MAJOR **0**; MINOR **0**. No line-anchored corrective finding is required.

## 8. Reviewer process and publication chronology

Native observations:

- `2026-10-30T14:55:01Z`
- `2026-10-30T14:55:41Z`
- `2026-10-30T14:57:38Z`
- `2026-10-30T14:58:45Z`

These are actual `/bin/date` observations, not inferred event timestamps. The active interval is below thirty minutes.

The complete manifest, freeze receipt and all six status-only controls, including endings, were read before any mathematical packet/source body. At the `14:55:41Z` observation the PRE-BODY ACK was composed. The own-wave `reviewer-prebody-ack-v1.md` write attempt was refused by `functions.write`’s xd/local-only restriction. The administrative ACK was then successfully delivered directly to `agent://Main` **before any mathematical packet read**. No shell write or alternative filesystem bypass was attempted.

After that ACK, the entire ordered 270-LF literal packet was read raw in consecutive windows of at most 20 LF, through its ending. Coverage was S1 LF1–199, S2 LF1–22, S3 LF1–30 and S4 LF1–17. No unresolved elision remained. All mathematical reconstruction above followed completion of that read.

Live hashes matched the supplied source pins. The freeze receipt’s selected-byte-equality assertion was read; it was not independently rerendered.

Exposure was this assignment, mandatory memory/procedural skills, the frozen manifest/receipt, the six status controls, and the literal packet. The author file named `review-v1.md` was read as the explicitly assigned **AUTHOR candidate**, not as an independent review. No sibling review, f320 transcript, author code, held payload or excluded linked source was opened. Historical examples appearing in the required complete imports were not selected, reconstructed, tested or used as premises. The author’s historical process account is not independently recertified by this review.

No scientific code, CAS, interpreter, solver, enumeration, replay, selected concrete mathematical diagnostic, private sanity test, external-model CLI, build, lint, test or formatter was used. Shell commands were metadata-only `/bin/date` and `shasum`.

The attempted own-wave `review-v1.md` publication was also refused. This complete direct return is the fallback for parent materialization. No bypass was attempted.

This is fresh **same-harness written reconstruction**, not human, independent-family, formal/kernel, priority or novelty assurance. No clean-cognition certificate is asserted.

**Overall correctness:** correct, restricted to the candidate’s necessary-condition theorem and stated non-conclusions.

**Explanation:** The augmented incidence square and its closing maps yield the claimed universal sign identity with the stated exponent. \(T2\) contributes the separately scoped missing-pair/count interface; no \(T2(11)\) branch is excluded.

**Confidence:** 0.99.