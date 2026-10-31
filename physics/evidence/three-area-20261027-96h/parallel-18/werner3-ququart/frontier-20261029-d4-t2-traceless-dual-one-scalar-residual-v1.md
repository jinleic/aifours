# A single-scalar residual for every original T2 test projector

**Status: WRITTEN, UNREVIEWED.** Conditional only on the traceless rank≤2 dual theorem in `frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md` (SHA-256 b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5), this packet reduces the full original T2 statement to **one real scalar inequality for each rank-two test projector**. The scalar inequality is **not proved**. No 2+2-reducing theorem, Schur-block kernel classification, selected numerical/physical q, code, external source or held/ZERO input is needed.

## 1. Full source, rank-two projector and trace functional

Let `P=ΨΨ†` be any rank-two orthogonal projector on `C4⊗C4`. On the 30-complex-dimensional Hilbert space

`S=sl4(C)⊕sl4(C)`, `||(A,B)||²=||A||_F²+||B||_F²`,

define `X=A⊗I4+I4⊗B`, the linear map `T_P(A,B)=XΨ`, and

`M_P=2I−T_P†T_P`, `ℓ_P(A,B)=Tr(XP)`.

The quadratic form of `M_P` is precisely `2L−Tr(PX†X)`. By the Ky Fan variational principle, **unrestricted original T2 holds iff `M_P⪰0` for every rank-two `P`**. The Gram operator `T_P†T_P` depends only on `P`, not the chosen `Ψ`.

Let `P_A=Tr_B P`, `P_B=Tr_A P` and

`h_P=((P_A)_0,(P_B)_0)`, `(P_A)_0=P_A−(Tr P_A/4)I4`.

Both partial traces have trace two, so `ℓ_P(w)=⟨h_P,w⟩` in the source Frobenius inner product and `h_P=0` exactly when `P_A=P_B=I4/2`.

## 2. Positive hyperplane and automatic range condition

The named dual theorem says `||Φ(R)||²≤2||R||²` whenever `rank R≤2` and `Tr R=0`. If `w=(A,B)∈ker ℓ_P`, then `R=XP` meets both hypotheses and

`Tr(PX†X)=⟨Φ(R),w⟩ ≤ √2 ||R||·||w||`.

Since `||R||²=Tr(PX†X)`, this gives `⟨w,M_Pw⟩≥0`. Hence **`M_P` is PSD on `ker ℓ_P`**. In particular it has at most one negative eigenvalue: any two-dimensional negative-definite subspace would intersect the codimension-at-most-one hyperplane nontrivially.

If `h_P=0`, the hyperplane is the entire source and `M_P⪰0` immediately. Otherwise set `e=h_P/||h_P||`, `H_P=ker ℓ_P`, `K_P=Π_H M_P|_H`, `b_P=Π_H M_P e`, `c_P=⟨e,M_Pe⟩`. Then `K_P⪰0` on the 29-dimensional hyperplane.

**The singular range condition is automatic.** If `w∈ker K_P`, then its quadratic form vanishes, so for `R=XP` one has `Tr R=0` and

`2||w||²=||R||²=⟨w,Φ(R)⟩≤||w||·||Φ(R)||≤√2||w||·||R||=2||w||²`.

Equality throughout Cauchy–Schwarz forces `Φ(R)=2w`, including the zero vector. Since `T_P†T_P w=Φ(XP)=Φ(R)`, this gives **`M_Pw=0` on the full source**, not just its compression. Consequently `ker K_P⊆ker b_P†`, equivalently `b_P∈range K_P`.

## 3. The one unpaid scalar

Define the real scalar

`δ(P)=c_P−b_P† K_P⁺ b_P`,  (3.1)

where `K_P⁺` is the Moore–Penrose inverse. The range condition just proved makes the following exact completion of the square valid for `x∈H_P`, `z∈C`:

`⟨x+ze,M_P(x+ze)⟩`

`= ||K_P^(1/2)(x+zK_P⁺b_P)||² + |z|² δ(P)`.

Therefore, for `h_P≠0`,

`M_P⪰0  ⇔  δ(P)≥0`.  (3.2)

Equivalently `δ(P)=min_{x∈ker ℓ_P}⟨e+x,M_P(e+x)⟩`; the minimum exists even when `K_P` is singular. Thus the **exact remaining universal original-T2 obligation** in this reduction is

**`δ(P)≥0` for every rank-two `P` with `h_P≠0`.**  (3.3)

This is not proved here. It is one scalar per projector but still quantifies over the full rank-two Grassmannian; it is not a finite enumeration, a narrowed source, a claim of tractability or a counterexample. If (3.3) fails, `M_P` has exactly one negative mode. If `P` has maximally mixed local marginals `P_A=P_B=I4/2`, (3.3) is vacuous because `M_P` is already PSD.

## 4. An explicit, still-insufficient trace penalty

For any source `w` and `P`, put `t=Tr(XP)` and

`R0=(X−(t/2)I16)P`.

It has rank at most two and trace zero. Since `Tr P=2`,

`||R0||_F²=Tr(PX†X)−|t|²/2`,

`Tr(R0†X)=Tr(PX†X)−|t|²/2=||R0||_F²`.

The traceless dual theorem therefore gives `||R0||²≤2L`, including the zero case. Equivalently,

`2L−Tr(PX†X) ≥ −|Tr(XP)|²/2`,

or as an operator inequality,

`M_P+(1/2)|h_P⟩⟨h_P| ⪰ 0`.  (4.1)

This proves the **single possible negative mode is controlled by the trace functional**, and in particular `δ(P)≥−||h_P||²/2`. The penalty in (4.1) is not automatically zero: removing it is exactly the unpaid scalar problem. No boundary-continuity argument, numerical sampling, or inference that `δ(P)≥0` is made.

## 5. Boundaries

The only scientific input beyond elementary linear algebra is the explicitly pinned UNREVIEWED tracezero dual theorem. This packet does not imply a proof of unrestricted T2/T3/Z2/q3, f274 `η>2L`, a physical counterexample, source correctness, execution, Lean/kernel, stronger-family/human review or novelty. It is independent of the earlier 14+8 reduction and its kernel packets; those remain separately unreviewed. The range/equality argument and the global scalar equivalence require disjoint written review.
