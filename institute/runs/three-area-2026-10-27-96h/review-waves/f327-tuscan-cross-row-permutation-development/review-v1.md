# f327 — Cross-row closing-permutation parity compatibility

**Status: UNREVIEWED AUTHOR CANDIDATE.** This is a written necessary-condition proof, not peer acceptance or a T2(11) witness/no-go.

## 1. Result and exact imports

Let \(S\) be the eleven symbols of an arbitrary actual linear T2(11), with rows indexed by their first symbols \(c\). Let:

- \(E(c)\) be the last symbol of row \(c\);
- \(\rho(a,b)\) be the unique row containing the directed adjacency \(a\to b\);
- \(\pi_c\) be the adopted closing permutation on \(S\setminus\{c,E(c)\}\).

Then the eleven closing permutations satisfy the joint compatibility equation
\[
\boxed{\prod_{c\in S}\operatorname{sgn}(\pi_c)=\operatorname{sgn}(E).}
\tag{CP}
\]

Thus the parity of the number of odd closing permutations is determined by the endpoint permutation. This links **all eleven cross-row permutations to an actual row-position incidence**, beyond the supplied missing-arc degree and event-count equations.

The same argument proves, for every actual T1(\(n\)), \(n\ge2\),
\[
\prod_c\operatorname{sgn}(\pi_c)
=
(-1)^{n(n+1)/2}\operatorname{sgn}(E),
\tag{GCP}
\]
where \(\pi_c\) is defined by the same closing adjacency-row correspondence. T2 is needed for the adopted interpretation of its fixed points and derangements, not for this parity identity.

**Imports:** S1 LF5,9,11,16 supply adjacency exhaustion, the row indexing, endpoint permutation, and closing correspondence. S3 LF8 supplies the first/last-column permutation laws. S2 LF7–17,28–30 and S3 LF15–17 retain their exact count/boundary limitations. No linked source, earlier review, diagnostic, unreviewed inequality, or excluded episode is used. The general sign identity needed below is proved here.

## 2. Proof

### A. Encode the actual rows as a Latin incidence square

Put \(X=S\cup\{\infty\}\). For each actual row \(r\), adjoin \(\infty\) and take the directed cyclic ordering
\[
\infty\longrightarrow r
\longrightarrow \text{the actual intervening row positions}
\longrightarrow E(r)\longrightarrow\infty .
\]

This only encodes the existing row. It does **not** assert that its circular distance-two completion is Tuscan.

For distinct \(x,y\in X\), let \(H(x,y)\) be the label of the unique augmented row containing \(x\to y\). Set \(H(x,x)=\infty\).

This is well-defined:

- Original adjacencies exhaust the distinct ordered pairs of \(S\) exactly once.
- The arc \(\infty\to c\) occurs precisely in row \(c\).
- The arc \(a\to\infty\) occurs precisely in row
  \(\lambda(a)=E^{-1}(a)\).

Define maps on \(X\) by
\[
\sigma_a(b)=H(a,b),\qquad \tau_c(b)=H(b,c).
\]
Every \(\sigma_a\) and \(\tau_c\) is a permutation.

Indeed, for \(a\in S\), the original outgoing adjacencies from \(a\) occupy every row except \(\lambda(a)\); the new target \(\infty\) supplies that row, and the diagonal supplies \(\infty\). Dually, incoming adjacencies to \(c\in S\) occupy every row except \(c\); the source \(\infty\) supplies row \(c\), and the diagonal supplies \(\infty\).

Moreover,
\[
\sigma_\infty=\mathrm{id}_X,\qquad
\tau_\infty=E^{-1}\text{ extended to fix }\infty .
\tag{1}
\]
Consequently \(H\) is a Latin square on \(X\).

For each symbol \(r\in X\), let \(h_r(x)\) be the unique \(y\) such that \(H(x,y)=r\). For \(r\in S\), \(h_r\) is precisely the augmented actual-row cycle. Hence
\[
\operatorname{sgn}(h_r)=(-1)^{11}\quad(r\in S),
\qquad h_\infty=\mathrm{id}_X.
\tag{2}
\]

This is the load-bearing actual-position input: each symbol class is **one Hamilton cycle**, not merely arcs satisfying prescribed degrees.

### B. Recover the closing permutations inside this square

Fix an arbitrary \(c\in S\) and put \(a=E(c)\). Define
\[
\Phi_c=\tau_c^{-1}\circ\sigma_a.
\]

Since \(a\ne c\), the definitions give
\[
\Phi_c(\infty)=\infty,\qquad
\Phi_c(a)=c,\qquad
\Phi_c(c)=a.
\tag{3}
\]

For the first equality, \(H(a,\infty)=c=H(\infty,c)\). The second uses the diagonal entries \(H(a,a)=H(c,c)=\infty\). The third uses the same incidence \(H(a,c)\) on both sides.

On \(K_c=S\setminus\{a,c\}\), \(\Phi_c\) is exactly \(\pi_c\): it sends \(b\) to the unique \(x\) satisfying
\[
\rho(a,b)=\rho(x,c).
\]
Thus \(\Phi_c\) consists of \(\pi_c\), the transposition \((a\,c)\), and the fixed point \(\infty\). Therefore
\[
-\operatorname{sgn}(\pi_c)
=
\operatorname{sgn}(\sigma_{E(c)})
\operatorname{sgn}(\tau_c).
\tag{4}
\]

Multiplying over \(c\in S\), using that \(E\) permutes \(S\), and then including the factors from (1), yields
\[
\left(\prod_{a\in X}\operatorname{sgn}(\sigma_a)\right)
\left(\prod_{c\in X}\operatorname{sgn}(\tau_c)\right)
=
(-1)^{11}\operatorname{sgn}(E)
\prod_{c\in S}\operatorname{sgn}(\pi_c).
\tag{5}
\]

Neither second-column nor penultimate-column multiplicities enter this equation.

### C. Prove the Latin sign identity

For any Latin square \(H\) of order \(N\),
\[
\left(\prod_a\operatorname{sgn}(\sigma_a)\right)
\left(\prod_c\operatorname{sgn}(\tau_c)\right)
\left(\prod_r\operatorname{sgn}(h_r)\right)
=
(-1)^{N(N-1)/2}.
\tag{6}
\]

To prove this, define permutations of \(X\times X\):
\[
\begin{aligned}
A(x,y)&=(x,H(x,y)),\\
B(x,y)&=(H(x,y),y),\\
D(x,z)&=(h_z(x),z),\\
T(x,y)&=(y,x).
\end{aligned}
\]
Their signs are respectively the row-sign product, column-sign product, symbol-sign product, and \((-1)^{N(N-1)/2}\). By definition of \(h_z\),
\[
D\circ A=T\circ B.
\]
Taking signs proves (6). This argument is universal; no square or permutation instance has been selected for testing.

### D. Obtain the compatibility equation

Here \(N=12\), so the right side of (6) is \(+1\), since \(N(N-1)/2=66\) is even. Equation (2) gives
\[
\prod_{r\in X}\operatorname{sgn}(h_r)=(-1)^{11\cdot11}=-1.
\]

Substituting this and (5) into (6), the two minus factors cancel:
\[
\operatorname{sgn}(E)\prod_{c\in S}\operatorname{sgn}(\pi_c)=1.
\]
This proves **(CP)**.

For general \(n\), the row/column product is
\[
(-1)^n\operatorname{sgn}(E)\prod_c\operatorname{sgn}(\pi_c),
\]
and the symbol-sign product is \((-1)^{n^2}=(-1)^n\). Their cancellation in (6) gives **(GCP)**. This is written symbolic reasoning, not an experimental check.

## 3. Boundary, orientation, and residual obligations

**Every required boundary branch remains live.** The proof works when both relevant boundary columns are permutations, when a full source exists, when a full target exists, and in mixed branches with either or both defects. It assumes neither \(\alpha_9\equiv1\) nor \(\alpha_1\equiv1\). The endpoint permutation \(E\) is not either of those columns.

All actual adjacencies retain their source-to-target orientation. Rows remain separately indexed. The coordinate swap \(T\) is solely a universal device in the sign proof; it does not reverse or identify actual rows.

No hypothetical missing-pair graph is treated as realizable. Actual row positions enter through the Hamilton-cycle fact in (2).

In the \(M=C\) branch, the imported result says that every \(\pi_c\) is a derangement. Those derangements must additionally satisfy **(CP)** jointly with the actual endpoint permutation. Outside that branch, the identical parity equation holds regardless of which closing permutations have fixed points.

This is a derived compatibility equation absent from the supplied count-and-degree interface. It is **not** a claim of axiomatic independence from all supplied structural facts or of literature novelty.

No exclusion of a count profile, conditional permutation-\(M\) cycle type, full-source/full-target branch, or mixed branch is established. No witness, nonexistence theorem, one-boundary-forces-the-other implication, or sufficiency result is claimed. **T2(11) remains OPEN.**

There is no unpaid premise for the displayed necessary condition beyond the explicit actual-array/T1 imports. To turn it into an exclusion would require additional, unpaid information about the possible joint signs of \(E\) and the \(\pi_c\).

## 4. Claim ledger

- **C1 — SUPPORTED at author-written-proof scope:** the joint closing-permutation compatibility equation **(CP)**, with the complete derivation above.
- **C2 — SUPPORTED at author-written-proof scope:** the argument preserves directed, separately indexed rows and requires no permutation assumption on either relevant boundary column.
- **C3 — INCONCLUSIVE:** whether this identity, together with further actual-array information, excludes a branch or assists a construction.

No source claim is declared REFUTED. No FATAL/MAJOR/MINOR mathematical source finding is submitted: this is an author candidate, not an independently graded review. No human, independent-family, formal/kernel, or priority/novelty verification occurred.

# Reviewer-prefixed process record — for parent materialization

- **Pre-body delivery:** A direct administrative ACK was successfully delivered to `agent://Main` after reading the complete manifest LF1–90, freeze receipt LF1–60, and all five status-only controls, including endings. No mathematical packet read or derivation preceded that ACK.
- **Bindings:** Live metadata hashing matched the requested manifest SHA `34fd97dc3228456778fc87f57117c8324a5b60013654a8706719d8ae537fc159` and receipt SHA `f4bc6dae9f7a5b0486a78243124352097712a4d2ec570ec8736e3f96ef39c7e1`.
- **Body coverage:** The complete 71-LF packet was read raw in windows 1–20, 21–40, 41–60, and 61–71 before derivation. All endings were visible; no unresolved elision remained. Its live SHA matched `38a2d907ae266385cb2838488ed608fa7d5d8f5eafae9bf2d29f663b81c8a78d`.
- **Exclusions:** Held records were used only as status controls. Their links were not followed.
- **Execution:** No scientific code, CAS, solver, enumeration, replay, selected mathematical instance, private optional sanity test, external-model CLI, paid/heavy run, build, lint, test, or formatter was used. Metadata commands were `/bin/date` and `shasum`.
- **Native observations:** `2026-10-30T14:47:23Z`; `2026-10-30T14:49:58Z`; final handoff checkpoint `2026-10-30T14:52:44Z`.
- **Publication chronology:** The direct ACK succeeded. Later, the attempted wave `review-v1.md` write was refused by the tool’s path restriction. That failure is not a scientific disqualification or successful publication. No bypass was attempted; the complete mathematical candidate and process text are delivered here.