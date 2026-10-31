# f328 — Review of weighted tight-frame projector-span rigidity

**Overall correctness: correct within the frozen scope.** The universal theorem is **SUPPORTED** by the reconstruction below. Its application to the declared actual connected C7 interface is **SUPPORTED CONDITIONALLY**; it establishes neither physical existence nor nonexistence.

**Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

**Confidence: 0.98**, restricted to this same-harness written algebraic review. No automatic theorem acceptance, human, independent-family, formal/kernel, or novelty assurance is conferred.

Own-wave ACK, process-record, and review writes were **refused** by the tool transport. The required pre-body direct message to `agent://Main` returned **Delivered**. This complete return is provided for parent materialization; no writing workaround was attempted.

## 1. Frozen scope and complete reading

Live metadata checks matched:

- Manifest SHA256: `71bdd8bd05a91b28f9176d26c16ab0dc06160d6c16f3579c3ac2a13f6f8d1e98`
- Freeze receipt SHA256: `8288aa0f77a0f7a501d7cd460588780e4a405f78984a199bd2f783dd20697893`
- Literal packet SHA256: `fd8206e30e9c746652678be19df31c4153ea46cd93e4e87160bd71cc763951c2`
- All four scientific source hashes and all seven status-control hashes.

Current packet labels:

| Label | Source | Complete coverage |
|---|---|---|
| S1 | f325 author candidate, `f325-c7-projector-span-clean-development/review-v1.md` | Logical lines 1–226; 225 LF, without a terminal LF |
| S2 | `physics-4-c7-projector-gram-slice-and-affine-anisotropy-parent-v1.md` | LF 1–19 |
| S3 | `parent-c7-schur-square-space-and-rank-correction-v1.md` | LF 1–9 |
| S4 | `frontier-20261029-C7-net-Gram-phase-lift-affine-anisotropy-v1.md` | LF 1–179 |

S1’s internal source references retain its original f325 numbering: original S1 = current S2; original S2 = current S3; original S3 = current S4. All citations below use **current f328 labels**. This mapping is not a mathematical finding.

The entire 435-LF packet was read raw, in order, in windows:

1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–380, 381–400, 401–420, 421–435.

Every ending was read. No returned elision required recovery. Mathematical derivation began only after completing the packet.

## 2. Universal weighted tight-frame theorem — SUPPORTED

### Assumptions and inner-product convention

Let \(W\) be an arbitrary finite-dimensional complex Hilbert space, with \(d=\dim W\ge1\). Let \(X\) be finite, each \(u_x\) unit, and
\[
P_x=|u_x\rangle\langle u_x|,
\qquad
\sum_{x\in X}w_xP_x=aI_W,
\qquad w_x>0,\quad a>0.
\]

The inner product is conjugate-linear in its first argument and linear in its second. Thus
\[
P_xz=u_x\langle u_x,z\rangle.
\]

No equal-weight, distinct-ray, real-vector, or real-phase assumption is added. These are exactly the declared hypotheses and convention in **S1 LF15–28,45–55**.

The tight identity gives:

1. \(I_W\) belongs to the projector span.
2. The vectors span \(W\): if \(z\) is orthogonal to every \(u_x\), then the left side annihilates \(z\), hence \(az=0\), so \(z=0\).

These are precisely the preliminary properties consumed by the proof (**S1 LF43,102**).

### Real versus complex projector span

Suppose
\[
\sum_x(\alpha_x+i\beta_x)P_x=0,
\qquad \alpha_x,\beta_x\in\mathbb R.
\]
Taking adjoints gives the same relation with \(i\) replaced by \(-i\). Adding and subtracting therefore gives
\[
\sum_x\alpha_xP_x=0,
\qquad
\sum_x\beta_xP_x=0.
\]

A real-independent family of these Hermitian projectors is consequently complex-independent. Hence
\[
\dim_{\mathbb R}\operatorname{span}_{\mathbb R}\{P_x\}
=
\dim_{\mathbb C}\operatorname{span}_{\mathbb C}\{P_x\}
=:r.
\]

This establishes **S1 LF28**. It does not treat \(\operatorname{Herm}(W)\) as a complex vector space.

### Basis-projector independence and \(r\ge d\)

Extract an arbitrary basis \(v_1,\ldots,v_d\) from the spanning unit frame. Let its inner-product dual be \(z_1,\ldots,z_d\), characterized by
\[
\langle v_i,z_j\rangle=\delta_{ij},
\]
and set \(E_j=|v_j\rangle\langle v_j|\).

The dual vectors are not assumed to be frame vectors or to be orthonormal. For any relation
\[
\sum_jc_jE_j=0,
\]
application to \(z_k\) gives
\[
c_kv_k=0,
\]
because \(E_jz_k=\delta_{jk}v_j\). Every \(v_k\ne0\), so every \(c_k=0\).

Thus the \(d\) extracted projectors are independent, proving
\[
r\ge d.
\]

This reconstructs **S1 LF45–63** with the declared convention and without assuming orthogonality during basis extraction.

### Equality rigidity

Suppose \(r=d\). The \(E_j\) then span the whole projector space, including \(I_W\). Write
\[
I_W=\sum_ja_jE_j.
\]
Applying this equality to \(z_k\) gives
\[
z_k=a_kv_k.
\]
Since the second inner-product argument is linear and \(v_k\) is unit,
\[
1=\langle v_k,z_k\rangle
=a_k\langle v_k,v_k\rangle
=a_k.
\]
Therefore \(z_k=v_k\), and the dual identities imply
\[
\langle v_i,v_j\rangle=\delta_{ij}.
\]

The extracted basis is orthonormal, as claimed in **S1 LF66–82**.

For any frame index \(x\), expand
\[
P_x=\sum_jb_jE_j.
\]
The orthogonal-projector identities and \(P_x^2=P_x\) imply
\[
\sum_j(b_j^2-b_j)E_j=0.
\]
Independence forces \(b_j^2=b_j\), so each coefficient is \(0\) or \(1\), even if the initial expansion was over \(\mathbb C\). Since \(\operatorname{tr}P_x=1\), exactly one coefficient is \(1\). Thus \(P_x\) equals one of the \(E_j\).

All \(d\) rays occur because the extracted basis came from the frame. Conversely, if all frame directions lie on exactly \(d\) mutually orthogonal rays, their \(d\) independent rank-one projectors span every \(P_x\), so \(r=d\).

This proves the complete iff in **S1 LF66–98**.

### Connectedness and boundary cases

In the equality case, vertices belonging to the same ray form a nonempty clique, while vertices on different rays have no edges. The nonorthogonality graph has exactly \(d\) nonempty connected components.

Therefore, for \(d>1\), connectedness excludes \(r=d\). Since \(r\) is integral,
\[
r\ge d+1.
\]
This verifies **S1 LF100**.

The boundaries are consistent:

- **\(d=1\):** all unit vectors determine the sole ray, \(r=1\), and the nonempty graph is connected. This is why the stronger connectedness conclusion explicitly requires \(d>1\).
- **Repeated vectors or different phases on a ray:** allowed throughout.
- **Empty family:** impossible under the declared hypotheses, since tracing the tight identity gives \(\sum_xw_x=ad>0\).
- **Zero vectors:** are not unit vectors and cannot be normalized into this family.
- **Unnormalized nonzero tight-frame vectors:** normalize them and use their squared norms as positive weights, exactly as stated in **S1 LF22**.
- **\(d=0\), zero-weight, or nonpositive-tightness variants:** are not silently imported into the theorem.

## 3. Projector-Gram consumer and complex ambient space — SUPPORTED

Define
\[
H_{xy}=\operatorname{tr}(P_xP_y)
=|\langle u_x,u_y\rangle|^2.
\]
For any complex coefficient vector \(c\),
\[
c^*Hc
=
\left\|\sum_xc_xP_x\right\|_{\mathrm{HS}}^2.
\]
Consequently, \(\ker H\) is precisely the complex projector-relation space, and
\[
\operatorname{rank}H=r.
\]

Since \(H\) is real, its real and complex ranks coincide. This also equals the dimension of the real Hermitian projector span. Thus the real-coefficient argument in **S1 LF106–124** is valid and has the required complex-rank interpretation.

Moreover,
\[
H_{xy}\ne0
\quad\Longleftrightarrow\quad
\langle u_x,u_y\rangle\ne0.
\]
The consuming projector Gram therefore preserves the nonorthogonality graph exactly (**S1 LF126–128**).

This does **not** identify \(H\) with the vector Gram \(C\). Vectorized projectors lie in
\[
W\otimes\overline W,
\]
whose complex dimension is \(d^2\), not generally in \(\operatorname{Sym}^2(W)\). The generic ambient bound is \(r\le d^2\). The correction in **S3 LF5** and distinction in **S1 LF175** are correct.

## 4. Exact conditional physical C7 interface — SUPPORTED

The physical premise is the one in **S2 LF7,12** and **S4 LF9–15,103–115**:

- Four ordinary MOQLS(8), \(Q,L_1,L_2,L_3\).
- The three mates are classical in their independently chosen output ONBs.
- These give an actual five-net on 64 cells: five classes, eight lines per class, eight cells per line, with different-class lines meeting once.
- \(Q\) has an intrinsic seven-dimensional nonorthogonality component \(W\) and a one-dimensional orthogonal complement.
- The fixed-ray cells form a transversal \(T\) of size eight, meeting each of the forty lines once.
- \(X\) consists of the other 56 cells.

These assumptions are not replaced by scalar-Gram feasibility.

For a given such net and transversal, the exact phase certificate is a complex Hermitian matrix \(C\) on \(X\) satisfying:

1. \(C\succeq0\), \(\operatorname{rank}C=7\), and \(C_{xx}=1\).
2. \(C_{xy}=0\) for distinct net-collinear cells.
3. Its off-diagonal nonzero graph is connected.

Factor \(C=F^*F\), with columns \(q_x\) in a seven-dimensional \(W\). Unit diagonal gives 56 unit vectors. Every line contains seven \(X\)-cells, whose vectors are mutually orthogonal by condition 2; they therefore form a \(W\)-ONB.

The eight lines in any one class partition \(X\). Summing their resolutions of the identity gives
\[
\sum_{x\in X}|q_x\rangle\langle q_x|=8I_W.
\]
Thus this is an actual unit-norm tight frame. Also,
\[
C^2=F^*(FF^*)F=8C,
\qquad
H=C\circ\overline C.
\]

Connectivity is separately supplied by intrinsicness; it is **not** inferred from tightness. It passes unchanged from \(C\) to \(H\). The universal theorem therefore gives
\[
\operatorname{rank}H\ge8
\]
for this entire conditional class (**S1 LF134–146**).

### Converse physical routing

The converse in **S4 LF109** also reconstructs correctly:

- Adjoin one unit vector \(f\in W^\perp\) at every \(T\)-cell.
- Every net line becomes an eight-vector \(Q\)-ONB.
- Choose two classes as rows and columns, and the other three as classical mate-symbol classes.
- Net intersections give the Latin conditions and the classical-mate pair-product ONBs.
- For \(Q\) paired with a classical mate, different symbols are orthogonal in the mate factor, while each fixed-symbol line carries a \(Q\)-ONB. This gives the required 64-vector product ONB.
- Connectedness makes \(X\) one intrinsic component, orthogonal to the fixed-ray component.

Hence this is an iff at the **declared five-net/three-classical-mates interface**, not an assertion for unrestricted quantum mates. No matrix satisfying the certificate conditions is constructed here.

## 5. Net-specific upper bounds — SUPPORTED

The incidence-kernel dimension can be reconstructed directly from the all-net identities in **S4 LF19–43**.

Let \(N\) be the actual 64-cell collinearity adjacency. Its degree is \(35\). A collinear pair has six additional points on its common line and \(4\cdot3\) cross-class intersections, hence 18 common neighbors. A noncollinear pair has \(5\cdot4=20\). Thus
\[
N^2=15I-2N+20J.
\]

Block \(N\) by \(T,X\):
\[
N=
\begin{pmatrix}
0&M^T\\
M&A
\end{pmatrix}.
\]
Transversality gives
\[
M\mathbf1=5\mathbf1,\qquad A\mathbf1=30\mathbf1,
\]
and the block identities give
\[
M^TM=15I+20J,
\qquad
AM=-2M+20J.
\]

The first identity makes \(M\) full column rank eight. Its image consists of the constant direction and a seven-dimensional \(-2\)-eigenspace of \(A\). On the 48-dimensional orthogonal complement of \(\operatorname{im}M\), the \(X\)-\(X\) block gives
\[
A^2+2A-15I=0,
\]
with roots \(3,-5\). If their multiplicities are \(m,n\), then
\[
m+n=48,\qquad
0=\operatorname{tr}A=30-14+3m-5n.
\]
Hence \(m=28,n=20\), recovering **S4 LF33** by universally valid net counting, not by selecting a net.

Let \(B\) be the 56-by-40 component-cell/line incidence matrix. Then
\[
BB^T=5I+A.
\]
Therefore
\[
V=\ker B^T
\]
is exactly the \(-5\)-eigenspace, with \(\dim V=20\). Let \(\Pi\) be its orthogonal projection.

For the actual projector Gram, every component line resolves \(I_W\), so
\[
HB=J,\qquad H\mathbf1=8\mathbf1
\]
(**S4 LF58–62**). Define
\[
K=H-\frac17J.
\]
Each column of \(B\) contains seven ones, giving \((J/7)B=J\), hence \(KB=0\). Symmetry then gives \(\operatorname{range}K\subseteq V\). The constant direction belongs to \(\operatorname{im}B\), so \(K\mathbf1=0\).

Since \(H\succeq0\), and \(J/7\) removes precisely its constant-direction eigenvalue eight, \(K\succeq0\) on the orthogonal complement (**S4 LF64–68**).

The summands \(J/7\) and \(K\) have orthogonal supports. Consequently,
\[
\operatorname{rank}H=1+\operatorname{rank}K\le21.
\]
For
\[
D=K-\frac{12}{5}\Pi,
\]
both terms are \(V\)-supported, so
\[
\operatorname{rank}D\le20.
\]

No trace-zero-to-rank-drop inference is used. In particular, \(\operatorname{tr}D=0\) does not establish \(\operatorname{rank}D\le19\). This verifies **S3 LF7** and its consumption in **S1 LF148–175**.

Combining the upper and lower bounds gives exactly
\[
\boxed{8\le\operatorname{rank}H\le21},
\qquad
\boxed{7\le\operatorname{rank}K\le20},
\qquad
\boxed{\operatorname{rank}D\le20}.
\]

No exact rank or norm follows from these intervals.

## 6. Per-claim dispositions

| Claim | Disposition | Source and scope |
|---|---|---|
| Real and complex projector spans have equal dimension | **SUPPORTED** | S1 LF28; Hermitian-adjoint argument above |
| Arbitrary extracted basis projectors are independent; \(r\ge d\) | **SUPPORTED** | S1 LF43–63; dual convention checked |
| \(r=d\) iff exactly \(d\) orthogonal rays | **SUPPORTED** | S1 LF66–98 |
| Connected nonorthogonality implies \(r\ge d+1\) for \(d>1\) | **SUPPORTED** | S1 LF100; \(d=1\) boundary retained |
| Projector-Gram rank equals projector-span dimension and preserves the graph | **SUPPORTED** | S1 LF106–128 |
| Actual 56-vector factorization, line ONBs, tightness, intrinsic connectivity, and physical iff | **SUPPORTED CONDITIONALLY** | S2 LF7,12; S4 LF9–15,103–115; stated net/three-classical-mates interface |
| \(\dim V=20\), \(\operatorname{rank}H=1+\operatorname{rank}K\le21\), \(\operatorname{rank}D\le20\) | **SUPPORTED CONDITIONALLY** | S4 LF19–43,58–74; S3 LF7 |
| Actual connected C7 rank window and \(K\) lower bound | **SUPPORTED CONDITIONALLY** | S1 LF140–165 |
| C7 existence/nonexistence, scalar-to-projector realization, anisotropic-lift exclusion, C8, or q1 closure | **INCONCLUSIVE / NOT CLAIMED** | S1 LF168–185 |
| Exact ranks/norms, \(\operatorname{rank}D\le19\), novelty, or priority | **INCONCLUSIVE / NOT CLAIMED** | S1 LF168–175,189; S3 LF5–9 |

No audited theorem claim is **REFUTED**.

The affine difference-set/isotropy subsection was read completely for packet coverage, but is not a premise of this result and receives no fresh blanket acceptance from this review. An isotropic scalar point is not a phase lift.

The unresolved physical step remains constructing the required single complex rank-seven PSD phase Gram with every net zero and intrinsic connectivity, or proving no such Gram can exist across the declared class. Neither is supplied here.

## 7. Actual process chronology and exclusions

Native `/bin/date` checkpoints:

- **2026-10-30T14:54:59Z:** initial observation.
- **14:55:50Z:** before PRE-BODY ACK.
- **15:00:38Z:** substantive reconstruction checkpoint.
- **15:02:06Z:** completed review, before return-write attempts.

Every observed active interval was below 30 minutes.

The complete manifest, freeze receipt, and seven status-only controls were read before scientific packet access. The own-wave ACK write was refused; its immediate direct-message fallback returned **Delivered**. Only afterward were the packet windows opened. Own-wave `reviewer-process-v1.md` and `review-v1.md` writes were subsequently refused as well. No refused write is claimed as a persisted artifact, and no administrative transport refusal is treated as scientific disqualification.

No selected mathematical instance, scientific code/CAS/interpreter/solver/enumeration/replay/sanity probe, external-model CLI, build, lint, test, or formatter was used. No f320 transcript/selected payload, author code, excluded link, held scientific payload, or sibling review was accessed. Status controls supplied exclusions only; memory and skills supplied procedural context only.

This return is a bounded same-harness written review—not a clean-cognition certificate, retrospective cure, independent-family review, human verification, formal/kernel acceptance, or novelty assurance.