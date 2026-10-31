# f325 — Minimal projector-span rigidity for complex tight frames

**UNREVIEWED AUTHOR CANDIDATE — not peer acceptance.**

**Result:** The proposed universal rigidity statement is true. Its proof gives the conditional necessary bound
\[
8\le \operatorname{rank}H\le21
\]
for every actual connected rank-seven C7 phase lift, while preserving \(\operatorname{rank}D\le20\). It supplies neither a C7 witness nor a C7 exclusion.

Own-wave writes of `review-v1.md` and reviewer-prefixed process records were refused by the tool transport. The complete scientific return and process account follow for parent materialization; no alternate writing route was attempted.

## 1. Universal theorem

Let \(W\) be a complex Hilbert space of arbitrary finite dimension \(d\ge1\). Let \((u_x)_{x\in X}\) be a finite family of unit vectors satisfying a positive weighted tight-frame identity
\[
\sum_{x\in X}w_xP_x=aI_W,
\qquad
w_x>0,\quad a>0,\quad
P_x=|u_x\rangle\langle u_x|.
\]
Ordinary unit-norm tight frames have \(w_x=1\). Arbitrary nonzero tight-frame vectors fit this formulation after normalization, with their squared norms as weights.

Write
\[
r=\dim\operatorname{span}\{P_x:x\in X\}.
\]
The real span in \(\operatorname{Herm}(W)\) and complex span in \(\operatorname{End}_{\mathbb C}(W)\) have the same dimension: a complex relation separates into real and imaginary Hermitian parts, and taking adjoints shows that both parts vanish.

Then:

1. \(r\ge d\).
2. \(r=d\) **if and only if** all frame directions lie in exactly \(d\) mutually orthogonal rays.
3. If \(d>1\) and the nonorthogonality graph of the frame is connected, then
   \[
   r\ge d+1.
   \]

These statements quantify over every \(d\) and every frame satisfying the hypotheses. No concrete dimension, ray family, graph, matrix or auxiliary-parameter instance is used in their proof.

### Proof

The tight-frame identity implies that the vectors span \(W\) and that \(I_W\) belongs to their projector span.

Extract an arbitrary vector-space basis \(v_1,\ldots,v_d\) from the unit frame vectors, and put
\[
E_j=|v_j\rangle\langle v_j|.
\]
This is a basis extraction within an arbitrary universally quantified family, not a selected example.

Let \(z_1,\ldots,z_d\) be its inner-product dual basis:
\[
\langle v_i,z_j\rangle=\delta_{ij},
\]
using the convention that the inner product is linear in its second argument.

The \(E_j\) are linearly independent. Indeed, applying a relation
\[
\sum_jc_jE_j=0
\]
to \(z_k\) gives \(c_kv_k=0\), so \(c_k=0\) for every \(k\). Consequently,
\[
r\ge d.
\]

Now suppose \(r=d\). The \(E_j\) form a basis of the entire projector span. Since \(I_W\) belongs to that span, there are scalars \(a_j\) with
\[
I_W=\sum_ja_jE_j.
\]
Apply this equality to \(z_k\):
\[
z_k=a_kv_k.
\]
Taking the inner product with \(v_k\), and using \(\|v_k\|=1\), yields
\[
1=\langle v_k,z_k\rangle=a_k.
\]
Thus \(z_k=v_k\) for every \(k\). The dual-basis identities therefore give
\[
\langle v_i,v_j\rangle=\delta_{ij}.
\]
The extracted basis is orthonormal.

For any frame index \(x\), write
\[
P_x=\sum_jb_jE_j.
\]
Because the \(E_j\) are mutually orthogonal projections, the identity \(P_x^2=P_x\) becomes
\[
\sum_j(b_j^2-b_j)E_j=0.
\]
Linear independence forces \(b_j^2=b_j\), so every \(b_j\) is either \(0\) or \(1\). Since \(\operatorname{tr}P_x=1\), exactly one coefficient is \(1\). Hence
\[
P_x=E_j
\]
for exactly one \(j\). Every frame direction lies on one of the \(d\) orthogonal basis rays, and every ray occurs because the extracted basis came from the frame.

Conversely, if the directions lie in \(d\) mutually orthogonal rays, spanning ensures that every ray occurs. Their \(d\) independent rank-one projections then span all the frame projectors, giving \(r=d\).

In the equality case, vertices on the same ray are pairwise nonorthogonal, whereas vertices on different rays are orthogonal. The nonorthogonality graph has exactly \(d\) nonempty connected components. For \(d>1\), it is disconnected. Thus a connected frame cannot have \(r=d\); combining this with \(r\ge d\) proves \(r\ge d+1\). ∎

The proof actually needs only that the vectors span \(W\) and that \(I_W\) lies in their projector span. Tightness supplies both conditions. No assumption of real phases or symmetric tensors is involved.

## 2. Identification with projector-Gram rank

For the family above, define
\[
H_{xy}=\operatorname{tr}(P_xP_y)
      =|\langle u_x,u_y\rangle|^2.
\]
This is the Hilbert–Schmidt Gram matrix of the Hermitian projectors. For every real coefficient vector \(t\),
\[
t^{T}Ht
=
\left\|\sum_xt_xP_x\right\|_{\mathrm{HS}}^2.
\]
Therefore \(\ker H\) is precisely the space of real projector relations, and
\[
\operatorname{rank}H
=
\dim_{\mathbb R}\operatorname{span}_{\mathbb R}\{P_x\}
=
r.
\]

Moreover, taking squared absolute values preserves the zero/nonzero distinction. Thus the off-diagonal nonzero graph of \(H\) is exactly the frame’s nonorthogonality graph.

This is the required consuming-side identification: the theorem concerns projector-span dimension, **not** the rank of the original vector Gram.

## 3. Conditional consequence for an actual C7 phase lift

Use the actual-object interface in **S1 LF7,9,12**, together with the definitions and reconstruction in **S3 LF9–15,58–68,103–115**.

Suppose an actual C7 phase lift \(C\) exists at those hypotheses. Factor \(C\) as the Gram of its unit vectors \(q_x\) in the seven-dimensional component \(W\). On each net line, its seven component vectors form an ONB. Summing over the eight lines of any one net class gives
\[
\sum_x|q_x\rangle\langle q_x|=8I_W.
\]
The nonorthogonality graph is connected by the intrinsicness requirement, not merely by tightness.

The universal theorem therefore applies to this actual family and gives
\[
\operatorname{rank}H\ge8,
\qquad
H=C\circ\overline C.
\]
This is a necessary property of every actual lift satisfying the interface, not a selected rank-seven test instance.

Retaining the independently established net-specific upper bounds from **S2 LF7** gives
\[
\boxed{8\le\operatorname{rank}H\le21},
\qquad
\boxed{\operatorname{rank}D\le20}.
\]

Also, the adopted decomposition is
\[
H=\frac17J+K,\qquad K\mathbf1=0,
\]
with \(K\) supported on \(V\). The rank-one constant-direction summand and \(K\) have orthogonal supports. Consequently,
\[
\operatorname{rank}H=1+\operatorname{rank}K,
\]
so the conditional range sharpens to
\[
\boxed{7\le\operatorname{rank}K\le20}.
\]

Nothing here establishes:

- \(\operatorname{rank}D\le19\);
- an exact rank of \(H\) or \(K\);
- an exact value of \(\operatorname{tr}(K^2)\);
- an exact Frobenius norm of \(D\).

In particular, \(\operatorname{rank}C=7\) is never substituted for \(\operatorname{rank}H=7\). The complex projector ambient space remains \(W\otimes\overline W\), not \(\operatorname{Sym}^2(W)\), consistently with **S2 LF5**.

## 4. Claim dispositions and remaining gap

| Claim | Disposition | Scope |
|---|---|---|
| Minimum projector-span dimension and equality rigidity | **SUPPORTED** | The universal written proof above establishes \(r\ge d\), with equality exactly for \(d\) orthogonal rays. |
| Connected-frame consequence | **SUPPORTED** | For \(d>1\), connected nonorthogonality implies \(r\ge d+1\). |
| Actual C7 consequence | **SUPPORTED CONDITIONALLY** | Every actual connected C7 lift at the imported interface satisfies \(8\le\operatorname{rank}H\le21\), \(7\le\operatorname{rank}K\le20\), and the unchanged \(\operatorname{rank}D\le20\). |
| C7 existence or nonexistence | **INCONCLUSIVE / NOT CLAIMED** | The rank window supplies neither a witness nor a contradiction. |
| Scalar-to-projector phase lift, exclusion of anisotropic lifts, C8 or q1 closure | **INCONCLUSIVE / NOT CLAIMED** | All original realization, net-orthogonality and intrinsic-connectivity obligations remain. |

**FATAL/MAJOR/MINOR mathematical findings in this bounded derivation:** none identified. This is an author proof candidate, not an independently accepted theorem or a blanket audit of every result in the packet.

The affine difference-set argument and its bounds were read for complete packet coverage but are not premises of this new result. No novelty or priority claim is made.

## 5. Process and exact provenance

### Frozen inputs

Live metadata-only SHA-256 checks matched:

- Manifest: `71fefff4dade5739aa5b2fd328fe1755cf138234e34a55fdb462ceaebc35c43b`
- Freeze receipt: `4d0bdb0a3eb610daa6b133b60fb76eef0771756d5567747d1dfb93fb5d67f9d1`
- Literal packet: `1ff2143e918962b13c9120c2061f8ae5a273b27d7ad921bed7c45e9e75982925`
- All six manifest-pinned status-only controls.
- All three manifest-pinned mathematical source hashes.

Complete mathematical coverage was **S1 LF1–19, S2 LF1–9, S3 LF1–179**. The entire 209-LF literal packet was read raw in windows:
\(1\!-\!20,\ 21\!-\!40,\ 41\!-\!60,\ 61\!-\!80,\ 81\!-\!100,\ 101\!-\!120,\ 121\!-\!140,\ 141\!-\!160,\ 161\!-\!180,\ 181\!-\!200,\ 201\!-\!209\).
The ending was read, with no unrecovered returned elision.

### Actual chronology

- **2026-10-30T14:47:23Z:** initial native checkpoint.
- Complete manifest, freeze receipt and all six controls read; administrative hashes checked.
- **14:47:55Z:** native observation before the PRE-BODY ACK attempt.
- Own-wave `reviewer-prebody-ack-v1.md` write **refused**.
- Immediate fallback administrative ACK to `agent://Main` explicitly returned **Delivered**.
- **Only afterward** were mathematical packet windows opened.
- Complete packet reading preceded mathematical derivation.
- **14:50:27Z:** native substantive checkpoint after the universal derivation and conditional actual-lift consequence.
- **14:51:25Z:** native observation before the scientific return attempt.
- Own-wave `review-v1.md` and `reviewer-process-v1.md` writes also **refused**.

Every active checkpoint interval was below 30 minutes. No refused filesystem write is claimed as a delivered artifact. The refusal is a transport limitation, not scientific disqualification; this full return is provided without bypass.

### Exclusions and verification limits

The f320 process record was used solely for its exclusion status. No held link, f320 failed output/transcript, selected payload or prior returned review body was accessed. No scientific code, CAS, solver, enumeration, replay, optional sanity test or external-model CLI was used. No selected mathematical instance was undertaken.

The memory summary and written-math skill were procedural context only. No clean-cognition certificate, retrospective cure, independent-family review, human verification or formal/kernel acceptance is asserted.