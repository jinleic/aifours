# q4-span bridge: exact reduction, a three-mate frame inequality and a ray-star lemma

**WRITTEN AUTHOR PACKET, PhysicsMOQLS8-2; not reviewed, not adopted.** Clock observed before writing: Thu Oct 29 08:26:24 PDT 2026. This packet registers one disjoint bridge toward the original unrestricted four-family alternative and supplies two self-contained tools for it. It proves **no** exclusion of any four-family stratum, no classicality, no witness, no numerical M(8), and nothing about A10/A11. Every load-bearing step is proved here except the explicitly named *adopted* prior-round gates, which are used only as stated in their parent disposition.

## 0. Definitions and adopted inputs

An ordinary QLS of order 8 is an 8×8 array of unit vectors of C^8 whose rows and columns are orthonormal bases (ONBs). Q,X1,X2,X3 form a four-MOQLS(8) when every pair's 64 same-cell tensor products form an ONB of C^8⊗C^8; equivalently, for distinct members M,N and distinct cells y,z, `<M_y,M_z><N_y,N_z>=0`. Phases and separate unitaries are irrelevant; rays mean unit vectors up to phase. A *component* of a member is a connected component of its non-orthogonality graph on cells; its rays span W_C of dimension r, every row and column meets it in r cells whose rays are an ONB of W_C (a *line basis*), and r=1 components are exactly the fixed (complete) rays. S_C is the real span of the rank-one projectors of C, b=dim S_C. A member's span a is the sum of b over its components.

Adopted inputs (parent disposition `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4, same-harness written scope): Gate 1 **GAP3** (every nonfixed ray of every member has at most 3 cells); Gate 2 (no component of dimension 2 or 3); Gates 3/5/7 (b>=2r-1 for every component; b>=8, 10, 12 for r=4, 5, 6); Gate 4 (all four nonclassical: the four member spans sum to at most 53).

## 1. The exact q4 reduction

By Gate 2 a nonclassical member has component type {4,1^4}, {5,1^3}, {6,1^2}, {7,1}, {8} or {4,4}. With the adopted bounds its span is at least 12, 13, 14, 14, 15, 16 respectively. Hence:

* If every intrinsic C4 component of every four-MOQLS(8) has b>=10 and every intrinsic C5 has b>=11, every nonclassical member has a>=14; four of them would need span sum >=56>53, so **q4 would be impossible**.
* With only b(C4)>=9, the q4 residual is exactly the type multisets in which at least three members have span 13 (C4-type with b=9 or C5-type with b=10). With only b(C5)>=11, it is the multisets with at least three C4-type members of span at most 13.

These statements are arithmetic on adopted bounds; the two local improvements are **unproved**. They are the registered targets of this bridge. No overlap-counting conclusion is drawn.

## 2. Three-mate frame inequality (TMFI)

**Lemma 2.1.** Let Q,X1,X2,X3 be a four-MOQLS(8), a a unit vector of C^8, c_y=|<a,Q_y>|^2. For every cell y with c_y>0,

`sum over z in P(y) of c_z >= 3(1-c_y)`, where P(y) is the set of cells z not in the row or column of y with Q_z orthogonal to Q_y and c_z>0.

*Proof.* Apply `<a|.|a>` to the first factor of `sum_y P^Q_y (x) P^Xi_y = I(x)I`: `sum_y c_y P^Xi_y = I_8`. Let M_i be the 8×64 matrix with columns sqrt(c_y) Xi_y. Then M_i M_i* = I_8, so Gamma_i = M_i* M_i, `Gamma_i(y,z)=sqrt(c_y c_z)<Xi_y,Xi_z>`, is an orthogonal projection, and `sum_{z!=y}|Gamma_i(y,z)|^2 = c_y-c_y^2`. For z!=y, Gamma_i(y,z)=0 if y,z share a row or column (Xi lines are ONBs), if <Q_y,Q_z>!=0 (Q–Xi product ONB), or if c_z=0. For i!=j, Gamma_i(y,z)Gamma_j(y,z)=c_y c_z<Xi_y,Xi_z><Xj_y,Xj_z>=0 (Xi–Xj product ONB). Thus each z!=y supports at most one i, with |Gamma_i(y,z)|^2<=c_y c_z, and only z in P(y) can support any. Summing the three identities: `3c_y(1-c_y) <= c_y sum_{z in P(y)} c_z`. Divide by c_y. ∎

GAP3 is not used in Lemma 2.1. The Gram-projection device is old in this project; the inequality is stated here in the generality needed below.

**Corollary 2.2 (closed partner).** Suppose 0<c_y<1, and every a-active ray orthogonal to v=Q_y equals one ray v' with |<a,v'>|^2=1-c_y. Then v' occupies at least three cells off y's row and column. If moreover every line containing v contains v', then v' has at least 5 cells. For a nonfixed v' this contradicts GAP3. This contains the adopted single-plane tested channel lemma as a special case.

## 3. Ray-star lemma

Let C be a component of dimension r>=2 of a member Q of a four-MOQLS(8) and u an actual ray of C. Put `sigma_u = dim span_R {P_v : v ray of C, v orthogonal to u}`. The real-linear map Z -> P_u Z P_(u-perp) on S_C has kernel S_C ∩ BD_u (block-diagonal for u ⊕ u-perp); write its image as {u chi* : chi in L_u} with L_u a real subspace of u-perp. Since S_C ∩ BD_u contains P_u and the star span, which annihilates u, **dim_R L_u <= b-1-sigma_u**.

For a u-active ray v (0<|<u,v>|<1), take the representative with v*u>0. Then `P_u P_v P_(u-perp) = u ((v*u) P_(u-perp) v)*`, so **P_(u-perp) v lies in L_u**.

A mixed u-active ray exists: otherwise u is orthogonal to every other ray of C and C would have dimension 1.

**Lemma 3.1.** (i) L_u is not contained in a complex line; in particular dim_R L_u >= 2. (ii) If dim_R L_u = 2 then Im<chi,chi'>=0 for all chi,chi' in L_u (L_u is Lagrangian), so all u-active rays, so normalized, lie in the real 3-space Xi_u = R u + L_u, on which the Hermitian product is real. Consequently **sigma_u <= b-3** for every actual ray u.

*Proof.* (i) If L_u ⊆ Cw, every u-active ray lies in B=span(u,w). Take a mixed v=alpha u+beta w (alpha,beta nonzero) at cell y and its B-partner v'. In any line through v, a ray x orthogonal to v is u-active (then x ∝ v') or orthogonal to u, whence `<v,x>=conj(beta)<w,x>=0` puts x in u-perp ∩ w-perp of dimension r-2; the other r-1 rays of the line cannot all lie there, so v' is actual and lies in every line through v. Every a=u-active ray orthogonal to v is v', with |<u,v'>|^2=1-|<u,v>|^2. Corollary 2.2 gives at least 5 cells of the nonfixed v', contradicting GAP3. (ii) Let omega=Im<.,.> on the 2-dimensional L_u. If omega is not zero it is nondegenerate. For orthogonal u-active v=alpha u+lambda, v'=alpha' u+lambda' (alpha,alpha'>0, lambda,lambda' in L_u), `0=<v,v'>=alpha alpha'+<lambda,lambda'>` makes <lambda,lambda'> real, so omega(lambda,lambda')=0 and lambda' is a real multiple of lambda: v' lies in span(u,lambda). The closedness argument of (i), with w replaced by lambda, and Corollary 2.2 again contradict GAP3. Hence omega=0. Finally b-1-sigma_u >= dim L_u >= 2. ∎

**Remarks proved here.** (a) If u has m_u>=2 cells, the lines through them carry at least two distinct bases of u-perp: a basis B of u-perp occupying s of u's lines forces each of its three rays to cover those s lines, a cell serving one row and one column only at an off-diagonal position (R_i,K_j), i!=j; with GAP3 this needs `3(s-3) <= |I||J|-|I∩J|`, false for s>=5 and for s=4 unless two rows and two columns with |I∩J|<=1 (impossible when m_u=2). (b) If two line bases through cells of u are connected relative to each other inside u-perp, the adopted premise-free 2r-1 argument in dimension r-1 gives sigma_u >= 2r-3, hence **b >= 2r**, with equality only if sigma_u=2r-3 and L_u is 2-dimensional Lagrangian. This would improve the adopted bounds for C7 (to 14) and C8 (to 16) **only** under that connectedness hypothesis; no unconditional C7/C8 improvement is claimed.

## 4. Consequences for the open local targets, and the exact gap

For the residual cases of §1: in a C4 with b=8 every ray's star has span at most 5 (the minimal span of an irreducible qutrit configuration); in a C4 with b=9, at most 6; in a C5 with b=10, at most 7 (the minimal span of an irreducible 4-dimensional configuration). In each equality configuration every u-active set is real in a 3-space. These are necessary conditions only. I have **not** excluded: (1) C4 configurations where every pair of lines through a common cell is reducible on the complement of the shared ray; (2) the Lagrangian equality configurations (u-active rays real in Xi_u, lines of type u+basis of u-perp, a closed pair in span(u,lambda) plus a basis of u-perp ∩ lambda-perp, or a real orthonormal frame of Xi_u plus a basis of the complement); (3) every b=9 C4 and b=10 C5 case. Therefore LOCAL4>=10 and LOCAL5>=11, and with them the q4 exclusion, remain open.

Not claimed: independent, parent, formal, executable, configured-family or novelty acceptance; any q1/q2/q3/q4 conclusion; the unreviewed axis-surplus-six (under f171), complete-ray-cover, distinct-ray or heavy-cell candidates are not inputs. A10 remains GB15/18 with literal P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 remains open. No heavy or multi-GB execution was performed.
