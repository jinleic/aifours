# f535 — No globally distinct six-dimensional complement to the two-antipodal-pair four-sector support

**GENERAL AUTHOR CANDIDATE — UNREVIEWED.**

## 1. Result and original-target status

I obtain a **whole-complement obstruction**, without assuming covariance of the vectors.

> **Theorem.** On the sixty cells
> \[
> H=\{(r,c)\in\mathbb Z_{10}^{\,2}:c-r\in\{2,3,4,7,8,9\}\},
> \]
> there do not exist sixty pairwise nonparallel unit vectors in \(\mathbb C^6\) such that every restricted row, column and cyclic symbol class \(r+c\) is an orthonormal basis.

The proof establishes a stronger compatibility statement before using nonparallelness:

> Any complex-vector solution of those thirty ONB equations, even if repeated rays are allowed, necessarily places every vector in one of three common, mutually orthogonal two-dimensional subspaces.

Global nonparallelness then gives an immediate contradiction.

Consequently, the forty-ray subsystem on
\[
S=\{0,1,5,6\}
\]
cannot have the requested orthogonal sixty-ray complement. This does **not** contradict the standalone forty-ray construction. It excludes completing that particular four-dimensional sector to the original hundred-ray array.

The obstruction transports to the entire ten-support affine orbit of \(S\). It is **not an unrestricted hundred-ray no-go**.

## 2. Input, chronology and execution boundary

Before scientific derivation, I completed:

1. The manifest, freeze receipt and supplied parent metadata.
2. All twelve permission/status controls, through their endings.
3. A direct pre-body ACK to Main.
4. The complete literal packet, LF 1–363, in consecutive raw windows of at most twenty LF, through its ending.

The permitted scientific source coverage was exactly:

- **S1:** f496 author body, LF 1–332.
- **S2:** the binary-sector/cyclic-support disposition, LF 1–29.

The f496 optional checker was excluded and was not read. Links to other scientific sources in these inputs were not followed. Held episodes and their consumers remained status-only NONINPUT.

An initial nonraw preview of administrative metadata preceded its complete exact raw reread; all required administrative reads were complete before the ACK and scientific packet reading.

The following are **parent-supplied bindings**, not hashes independently computed by me:

- Manifest SHA-256: `092ec267b5909ace70853d182901046b6090ba2f4c9b05031fbc5967957b4b6e`.
- Receipt SHA-256: `b4e126c378c2924fa32cdf5b45b467b9e56839092c9cdb6ae3bf41778cd6839f`.
- Packet SHA-256: `89a3321892378e5daf6556b59e0211e2e1a66947c60a35cfd269faa2b601da51`.

The supplied `2026-10-30T12:45:20-0700 PDT` clock observation belongs to Main. I made no native start-clock claim.

**Scientific execution: NOTRUN.** No executable calculation, solver, checker, public-source search or external-model call was performed. No scientific code or argv is proposed as evidence. The result below is an exact written argument, not an inferred execution result.

This response supplies the complete candidate body for Main’s materialization. No successful filesystem materialization or file-write refusal is claimed.

## 3. The exact sixty-cell problem

Use Chinese-remainder coordinates
\[
r\longleftrightarrow(a,u)=(r\bmod5,r\bmod2),\qquad
c\longleftrightarrow(b,v)=(c\bmod5,c\bmod2).
\]
The inverse is
\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2).
\]

The complementary support is precisely
\[
b-a\in D:=\{2,3,4\}\pmod5.
\]

For each \(a\in\mathbb Z_5\), \(d\in D\), and \(u,v\in\mathbb Z_2\), suppose that a vector
\[
q_{a,d}^{uv}\in\mathbb C^6
\]
is assigned to the cell
\[
r=\operatorname{crt}(a,u),\qquad
c=\operatorname{crt}(a+d,v).
\]

These are exactly \(5\cdot3\cdot4=60\) cells.

The required contexts are:

- **Row \((a,u)\):**
  \[
  \{q_{a,d}^{uv}:d\in D,\ v\in\mathbb Z_2\}.
  \]
- **Column \((b,v)\):**
  \[
  \{q_{b-d,d}^{uv}:d\in D,\ u\in\mathbb Z_2\}.
  \]
- **Symbol \((s,w)\):**
  \[
  \{q_{3(s-d),d}^{u,w-u}:d\in D,\ u\in\mathbb Z_2\},
  \]
  because
  \[
  a+b=2a+d=s\pmod5,\qquad u+v=w\pmod2.
  \]

Each displayed context has six vectors. The formulas quantify over all ten rows, all ten columns and all ten symbols.

Write
\[
p_{a,d}^{uv}=q_{a,d}^{uv}(q_{a,d}^{uv})^\dagger.
\]
Under the hypothetical ONB conditions these are rank-one orthogonal projections.

## 4. Every four-cell CRT block is orthonormal

Fix \(a,d\). The four vectors
\[
q_{a,d}^{00},\quad q_{a,d}^{01},\quad
q_{a,d}^{10},\quad q_{a,d}^{11}
\]
are mutually orthogonal:

- Equal \(u\), different \(v\): they share a row.
- Equal \(v\), different \(u\): they share a column.
- Different \(u\) and different \(v\): they have the same \(u+v\pmod2\), and the same \(a+b\pmod5\), so they share a cyclic symbol class.

Therefore
\[
F_{a,d}:=\sum_{u,v\in\mathbb Z_2}p_{a,d}^{uv}
\]
is a rank-four orthogonal projection.

Its missing subspace is represented by
\[
E_{a,d}:=I_6-F_{a,d},
\]
a rank-two orthogonal projection.

These missing-space projections are actual operators derived from the hypothetical physical vectors. They are not incidence selectors.

## 5. All context equations constrain the missing spaces

Adding the two row equations with first coordinate \(a\) gives
\[
\sum_{d\in D}F_{a,d}=2I_6.
\]
Hence
\[
\boxed{\sum_{d\in D}E_{a,d}=I_6.}\tag{R}
\]

Adding the two column equations with first coordinate \(b\) gives
\[
\boxed{\sum_{d\in D}E_{b-d,d}=I_6.}\tag{C}
\]

Adding the two symbol equations with first coordinate \(s\) gives
\[
\boxed{\sum_{d\in D}E_{3(s-d),d}=I_6.}\tag{L}
\]

All indices in this section are modulo five.

Define
\[
A_a=E_{a,2},\qquad B_a=E_{a,3},\qquad C_a=E_{a,4}.
\]
Reindexing (R), (C) and (L), respectively, yields, for every \(a\),
\[
A_a+B_a+C_a=I_6,\tag{1}
\]
\[
A_{a+1}+B_a+C_{a-1}=I_6,\tag{2}
\]
\[
A_{a+3}+B_a+C_{a-3}=I_6.\tag{3}
\]

For (2), take \(b=a+3\). For (3), take \(s=2a+3\).

No vector symmetry or covariance has been imposed.

## 6. Rigidity: the missing spaces are independent of \(a\)

Subtracting (1) from (2) gives
\[
A_{a+1}-A_a=C_a-C_{a-1}.
\]
Equivalently,
\[
C_a-A_{a+1}=C_{a-1}-A_a.
\]
Thus there is a single operator \(K\), independent of \(a\), such that
\[
C_a=A_{a+1}+K.\tag{4}
\]

Subtracting (1) from (3), and substituting (4), gives
\[
A_{a+3}-A_a
=C_a-C_{a-3}
=A_{a+1}-A_{a-2}.
\]
Since \(a-2=a+3\pmod5\),
\[
\boxed{2A_{a+3}=A_a+A_{a+1}.}\tag{5}
\]

We now use the projection property, not merely linear incidence equations.

### Projection-average lemma

If \(P,Q\) and \((P+Q)/2\) are orthogonal projections, then \(P=Q\).

Indeed, expanding the square of \((P+Q)/2\) gives
\[
PQ+QP=P+Q,
\]
and therefore
\[
(P-Q)^2=P+Q-PQ-QP=0.
\]
Because \(P-Q\) is Hermitian, this implies \(P-Q=0\).

Apply the lemma to (5). All the \(A_a\) are orthogonal projections, so
\[
A_a=A_{a+1}
\]
for every \(a\). Hence \(A_a\) is constant. Equation (4) makes \(C_a\) constant, and (1) makes \(B_a\) constant.

Consequently there are fixed rank-two projections
\[
E_2,\ E_3,\ E_4
\]
such that
\[
\boxed{E_{a,d}=E_d\quad\text{for every }a,d.}\tag{6}
\]
They satisfy
\[
E_2+E_3+E_4=I_6.
\]

Projections summing to the identity are mutually orthogonal. For completeness, if \(x\in\operatorname{ran}E_i\), then
\[
\|x\|^2
=\sum_j\langle x,E_jx\rangle
=\|x\|^2+\sum_{j\ne i}\|E_jx\|^2,
\]
so \(E_jx=0\) for \(j\ne i\).

We have therefore obtained a common orthogonal decomposition
\[
\mathbb C^6=H_2\oplus H_3\oplus H_4,
\qquad H_d=\operatorname{ran}E_d,\qquad \dim H_d=2.
\]

It remains essential to prove that the individual vectors respect this decomposition. Constancy of the missing spaces alone would not establish that.

## 7. A three-partition commutation lemma

Let
\[
E_1+E_2+E_3=I,\qquad R_1+R_2+R_3=I
\]
be orthogonal projection partitions, and suppose
\[
R_iE_i=0\qquad(i=1,2,3).
\]
Then every \(R_i\) commutes with every \(E_j\).

To prove this, consider an off-diagonal block \(E_jR_iE_k\), where \(j\ne k\).

- If \(i=j\), it vanishes because \(E_iR_i=0\).
- If \(i=k\), it vanishes because \(R_iE_i=0\).
- Otherwise \(i,j,k\) are the three different indices, and
  \[
  E_jR_iE_k
  =E_j(I-R_j-R_k)E_k=0.
  \]

Thus \(R_i\) is block diagonal with respect to the \(E\)-partition and commutes with every \(E_j\).

This lemma is dimension-independent and makes no assumption about real coordinates.

## 8. Every physical ray lies in a common two-dimensional sector

For a fixed row \((a,u)\), define its three two-plane projections
\[
\mathsf R_{a,d,u}
=p_{a,d}^{u0}+p_{a,d}^{u1},
\qquad d\in D.
\]
The row ONB condition gives an orthogonal partition
\[
\sum_{d\in D}\mathsf R_{a,d,u}=I_6.
\]
Moreover,
\[
\mathsf R_{a,d,u}E_d=0,
\]
because its range lies in the four-cell block \(F_{a,d}=I_6-E_d\).

The three-partition lemma therefore implies that every \(\mathsf R_{a,d,u}\) commutes with every \(E_j\).

For a fixed column \((b,v)\), the same argument applies to
\[
\mathsf C_{b,d,v}
=p_{b-d,d}^{0v}+p_{b-d,d}^{1v}.
\]
These three column planes also form an orthogonal partition of \(I_6\), and each is orthogonal to the correspondingly indexed \(E_d\). Thus every \(\mathsf C_{b,d,v}\) commutes with every \(E_j\).

Inside the four-cell block \((a,d)\), its four rank-one projections are mutually orthogonal. Consequently,
\[
\boxed{
p_{a,d}^{uv}
=
\mathsf R_{a,d,u}\,
\mathsf C_{a+d,d,v}.
}\tag{7}
\]
Both factors commute with every \(E_j\), so \(p_{a,d}^{uv}\) does too.

A rank-one projection commuting with an orthogonal projection partition must be supported in exactly one member of that partition. Explicitly, each \(E_j\) preserves its one-dimensional range and acts on it as either zero or identity; their sum is identity.

Therefore every one of the sixty hypothetical rays lies wholly in one of
\[
H_2,\ H_3,\ H_4.
\]

This completes the promised uniform complex compatibility theorem.

## 9. The forced two-dimensional sectors contradict global distinctness

Every row is an ONB of \(\mathbb C^6\), and every vector in it lies in one of the three orthogonal two-dimensional sectors. Hence each row contains exactly two rays from each sector. The same statement holds for every column.

Choose any cell ray \(q\), and let its sector be \(H_j\).

- Its row contains one other \(H_j\)-ray, call it \(x\).
- Its column contains one other \(H_j\)-ray, call it \(y\).

Both \(x\) and \(y\) are orthogonal to \(q\). In the two-dimensional space \(H_j\), the orthogonal complement of the line \(\mathbb Cq\) is one-dimensional. Thus
\[
\mathbb Cx=\mathbb Cy.
\]

The cells containing \(x\) and \(y\) are different: the selected row and column intersect only at the original cell containing \(q\), and neither \(x\) nor \(y\) is that cell.

We have obtained parallel rays at distinct cells, contradicting the required global pairwise nonparallelness.

This proves the theorem.

## 10. Consequence for the forty-ray sector and its affine orbit

Suppose a full hundred-ray array had an actual four-dimensional sector on
\[
H_S,\qquad S=\{0,1,5,6\}.
\]
Each full row contains four sector rays forming an ONB of that four-dimensional space. Its other six rays must therefore lie in the common six-dimensional orthogonal complement. The same full context conditions make those sixty rays a solution of the complementary problem treated above.

The theorem excludes that solution.

Thus:

> **No actual orthogonal \(4+6\) realization of the original hundred-ray problem can use the support \(S=\{0,1,5,6\}\) for its four-dimensional sector.**

This conclusion does not require accepting or executing the f496 forty-ray construction. It follows directly from the complementary ONB requirements.

For any unit \(h\in\{1,3,7,9\}\) and any \(t\in\mathbb Z_{10}\), the cell relabeling
\[
(r,c)\longmapsto(hr,hc+t)
\]
permutes rows and columns and sends a symbol \(r+c\) to \(h(r+c)+t\). It sends differences to
\[
c-r\longmapsto h(c-r)+t.
\]
A hypothetical complementary solution for \(hS+t\) would therefore pull back to one for \(S\), which is impossible.

These supports are exactly the ten choices of two antipodal pairs: modulo five they are the two-element subsets of \(\mathbb Z_5\), and translation and multiplication by a nonzero residue transport any such pair to any other.

Accordingly, the new AUTHOR theorem excludes the **entire ten-support two-antipodal-pair orbit as actual \(4+6\) sectors**. It does not claim that the forty-ray subsystems themselves are impossible.

## 11. Exact scope and remaining obligations

### What is supplied

- A written whole-complement no-go for all sixty required cells.
- Explicit handling of all thirty physical ONB contexts.
- A uniform operator compatibility theorem forcing a common \(2+2+2\) decomposition.
- An explicit consuming-side argument showing that **individual rank-one cell projections**, not merely block spans, respect that decomposition.
- A forced parallel pair at distinct cells.
- Transport to the ten-support affine orbit without vector covariance.

### What is not supplied or claimed

- No sixty-vector or hundred-vector witness.
- No executed finite verification.
- No unrestricted hundred-ray no-go.
- No result for the other residual cyclic four-support orbit represented by \(\{0,1,3,4\}\).
- No new resolution of noncirculant supports, other Latin resolutions, the rank-28 \(5+5\) branch or an irreducible ten-dimensional realization.
- No independent-family, human, formal/kernel or novelty assurance.

The sixty-ray obligation is answered **negatively by this AUTHOR proof candidate**; it is not replaced by a necessary incidence condition. Its acceptance remains pending independent checking and parent disposition.

The first unpaid acceptance consumers are the exact implications
\[
\text{thirty ONB equations}
\Longrightarrow
\text{constant }E_{a,d}
\Longrightarrow
[p_{a,d}^{uv},E_j]=0
\Longrightarrow
\text{a repeated ray}.
\]
The proof above supplies each implication explicitly, including the cell/context routing.

The simultaneous forty-ray gates retain their standalone scope. Even acceptance of that forty-ray construction would not establish a hundred-ray solution, and this complementary obstruction does not invalidate the standalone construction.

## 12. Evidence classification

**AUTHOR written theorem/proof:** Sections 3–10.

**Scientific execution:** none; NOTRUN.

**Disjoint reconstruction and parent adoption:** not performed here.

**Original hundred-ray target:** unresolved outside the explicitly excluded sector orbit.

**Novelty:** unaudited.