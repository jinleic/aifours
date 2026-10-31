# The rank-two dual master reduction of the full original T2 obligation

**Status: WRITTEN, ONE consolidated owner candidate, UNREVIEWED.** This is the single consolidated advance authorized by the parent ruling of 2026-10-30 (read complete; ACK `frontier-20261030-ruling-read-ack-v1.json`). It reduces the entire original traceless-pair T2 statement to ONE dimension-uniform inequality on rank-two bipartite operators, proves that reduction exactly, adds two new written facts (the nonnegative trace bracket and the vanishing-mixed-Gram paid region), and names the precise remaining core with a structural obstruction. It does not re-prove pinned regions; they are cited by hash. Inputs are elementary: Ky Fan/Frobenius duality, SVD, the pinned rank-one local-swap identity. **Exclusions honored:** the quarantined unsaved cross-term episode and all consumers are HELD/ZERO/NONINPUT and are not reconstructed, used or salvaged; the false f198 lemma is not used; no numerical instance, physical q, execution, external source, stronger-family/human/formal review or novelty claim is made.

## 1. Master theorem: full original T2 is one rank-two inequality

For traceless `A,B∈M4(C)`, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, the following are equivalent:

**(T2)** `σ1(X)²+σ2(X)²≤2L` for all traceless `A,B`.

**(Q)** For every `R` on `C4⊗C4` with `rank R≤2`:

`q(R) := ||Tr_B R||_F² + ||Tr_A R||_F² − |Tr R|²/2 ≤ 2||R||_F²`.  (1.1)

*Proof.* Ky Fan gives `√S2(X)=max{|Tr(R†X)| : ||R||_F=1, rank R≤2}`. For any such `R`, `Tr(R†(A⊗I4))=⟨Tr_B R,A⟩_F` and `Tr(R†(I4⊗B))=⟨Tr_A R,B⟩_F`. Since `A,B` are traceless, only the traceless parts `(Tr_B R)_0=Tr_B R−(Tr R/4)I4` and `(Tr_A R)_0` pair with them. For fixed `R`, the maximum of `|⟨(Tr_B R)_0,A⟩+⟨(Tr_A R)_0,B⟩|` over `||A||²+||B||²≤L` equals `√L·√(||(Tr_B R)_0||²+||(Tr_A R)_0||²)`. Therefore (T2) holds for a pair iff `||(Tr_B R)_0||²+||(Tr_A R)_0||²≤2||R||²` for its maximizing R; conversely, if some R violated (1.1), choosing traceless `A,B` parallel to the two projections with `L=1` and scaling gives a T2-failing pair. Finally `||(G)_0||²=||G||²−|Tr G|²/4` for 4×4 `G` and `Tr(Tr_B R)=Tr(Tr_A R)=Tr R`, so the left side equals `q(R)`. ∎

**Uniformity remark.** The same q-shape governs every local support size: by the pinned support equivalences (`...2x3...` SHA 4bb8a5de…, `...general-support...` checkpoint 2310), for supports `(m,n)`, `mn≥2`, `m,n≤4`, the corresponding statement is equivalent to (1.1) for all rank≤2 `R∈M(C^m⊗C^n)`: the optimal scalar-complement weight `w_t=4mn/(2(m+n)−mn)` satisfies `2/w_t−1/m−1/n=−1/2` identically, so the partial-trace projections and the trace penalty combine to the same `q`. Thus one dimension-uniform inequality on rank-two bipartite operators carries the whole support hierarchy; the `(m,n)`-dependence lies only in the equivalence proofs, not in the inequality.

## 2. Exact residual identity for rank-two R

Let `rank R=2` with thin SVD `R=s1|u1⟩⟨v1|+s2|u2⟩⟨v2|`, `s1≥s2>0`, `{u1,u2}`, `{v1,v2}` orthonormal. Define

`a_i=Tr_B|u_i⟩⟨v_i|`, `b_i=Tr_A|u_i⟩⟨v_i|`, `c_i=⟨v_i,u_i⟩` (so `Tr R=s1c1+s2c2=:γ`),

`p_i=⟨u_i⊗v_i,(P_-^A⊗P_-^B)(u_i⊗v_i)⟩≥0`,

`C12=⟨a1,a2⟩_F+⟨b1,b2⟩_F` (mixed partial-trace Gram).

The pinned rank-one swap identity gives `||a_i||²+||b_i||²=1+|c_i|²−4p_i`. Substituting into the expansion of `q(R)`:

**`q(R) = ||R||_F² + B − 4(s1²p1+s2²p2) + 2 s1 s2 Re C12`,**  (2.1)

`B := s1²|c1|²+s2²|c2|² − |s1c1+s2c2|²/2`.

**New Lemma (trace bracket).** `B≥0` always, since `|s1c1+s2c2|²≤(s1|c1|+s2|c2|)²≤2(s1²|c1|²+s2²|c2|²)` for real `s_i≥0`. ∎

For `s2=0` (rank one) identity (2.1) recovers the pinned bound `q≤(3/2)||R||²`. **Master scalar reduction:** by (2.1), (Q) for an SVD frame is exactly

`2 s1 s2 Re C12 ≤ s1²+s2² + B − 4(s1²p1+s2²p2)`.  (2.2)

**New paid region (vanishing mixed Gram).** If `C12=0` then `q(R)≤||R||²+B≤2||R||²` by the Lemma and `|c_i|≤1`. Hence every rank-two R whose SVD pieces have orthogonal partial traces in both factors is paid, whatever `p_i`, `γ`, EP status or supports. ∎

## 3. Paid regions of (Q) — consolidated pins

| Region of rank≤2 R | Written proof (all UNREVIEWED unless parent-dispositioned) |
|---|---|
| rank ≤ 1 | swap identity, consolidated v2 `...traceless-dual-strict-chiral-consolidated-v2.md` SHA b96fcf9f… §2 |
| `Tr R=0`, any supports | hollow nuclear decomposition, same packet §3 |
| `range R=range R†` (EP, incl. nonnormal EP) | Hermitian-part split, `...2x3...` SHA 4bb8a5de… §4 (cross-purity sublemma flagged there for review attention) |
| either local support dim ≤ 2 (any other dim) | qubit-side block identity, `...qubit-side-test-projectors-complete-v1.md` SHA ce6a6288… §2 — FIRST QUEUED REVIEW |
| `C12=0` mixed Gram | new, §2 above |
| test-projector-side: separable; PPT; product-basis diagonal; 2+2-reducing pairs; chiral/swap-symmetric pairs | pins 12a2a6f4…; 2961f2d5…; ef80f84a…; bb09c6bf…; b96fcf9f…/a6a3effd… |

## 4. The exact remaining core

By §1–§3, any violation of (Q) — equivalently any original T2 failure — requires a rank-two `R` with **all** of:

1. `Tr R≠0` and `rank R=2` with `s2>0`;
2. `range R≠range R†` (non-EP);
3. `C12≠0`;
4. both local support dimensions ≥3 (hence, in `C4⊗C4`, both ≥3×3).

On the test-projector side (at the unreviewed ce6a scope), any failing rank-two projector must have **both marginal ranks ≥3**; the PPT classification additionally forces NPT at its own unreviewed scope. No member of this core is asserted to exist. Solving (2.2) on the core — or exhibiting a core member violating it — is the entire remaining mathematical content of the original T2 obligation in this reduction.

## 5. Structural obstruction (no configurations selected)

The obvious route to (2.2) — polarize the rank-one bound `||a||²+||b||²≤1+|c|²` into a positive sesquilinear form on pairs `(u,v)` and apply Cauchy–Schwarz to `C12` — is structurally unavailable: in the would-be form, the overlap term `⟨v,u⟩⟨u',v'⟩` is conjugate-linear in `v`, while the partial-trace Gram pieces are linear in `v`. Diagonal nonnegativity of a non-sesquilinear polarization yields no cross-term bound. Consequently any proof of the core must use the frame constraints (orthonormality of `{u_i}`,`{v_i}`, rank-two structure, support dimensions), not single-pair positivity alone. This closes the single-pair-polarization route in a configuration-free way.

## 6. Nonclaims

No proof of the core inequality; no unrestricted T2/T3/Z2/q3; no f274 optimized `η>2L`, physical or quantum-state counterexample; no execution, selected parameter/q, source acceptance, formal/kernel, independent-family/human review, or novelty. Prior packets keep their pins and statuses; this file supersedes nothing and is offered as the second queued review item after ce6a, per the ruling's one-consolidated-advance direction.
