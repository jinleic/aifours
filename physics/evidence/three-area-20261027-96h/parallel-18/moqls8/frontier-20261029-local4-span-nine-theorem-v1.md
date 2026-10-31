# Every intrinsic four-dimensional component in a four-MOQLS(8) has projector span at least 9

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE, PhysicsMOQLS8-2; not reviewed, not adopted.** Clock observed before writing: Thu Oct 29 08:53:33 PDT 2026. This raises the adopted prior-round bound LOCAL4>=8 to **LOCAL4>=9**, by a proof that also re-excludes every span <=7. It is one of the two local targets of the registered q4-span bridge (packet 0cd4294a…). It does **not** exclude q4, any q-stratum, or any four-family; it is not formal, executable, independent-family or novelty acceptance. A10/A11 stay open.

## 0. Setting and the only imported fact

An ordinary QLS of order 8 is an 8×8 array of unit vectors of C^8 whose rows and columns are orthonormal bases (ONBs). Q,X1,X2,X3 form a four-MOQLS(8) when, for any two members M,N and distinct cells y,z, `<M_y,M_z><N_y,N_z>=0` (equivalently, each pair's 64 same-cell products form an ONB of C^8⊗C^8). Rays are unit vectors up to phase. A *component* C of Q is a connected component of Q's non-orthogonality graph on cells; its rays span W=W_C (dimension r) and every row and every column of the board meets C in r cells whose rays form an ONB of W — these r-sets are the *lines* of C and their ONBs the *line bases*. Rays of different components are orthogonal. C is *intrinsic C4* if r=4 (it is then connected, hence irreducible). S is the real span of the projectors P_y=|Q_y><Q_y|, y in C; b=dim S. A ray is *nonfixed* if it lies in a component with r>=2; for an actual ray v, m(v) is its number of cells.

**Imported (adopted prior-round Gate 1, GAP3, parent disposition SHA256 2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4):** every nonfixed ray of every member of a four-MOQLS(8) has m<=3. Nothing else is imported; Lemmas A–F are proved here.

For a unit a in W put c_y(a)=|<a,Q_y>|^2; a ray is *a-active* if c>0 and *a-mixed* if 0<c<1. For y in C, 𝒪 denotes the ordered pairs (y,z) of distinct cells of C not in a common row or column with Q_y orthogonal to Q_z.

## 1. Lemma A (three-mate frame inequality)

For every unit a in W, each mate X satisfies `sum_{y in C} c_y P^X_y = I_8` (apply `<a|.|a>` to the first factor of `sum_y P^Q_y ⊗ P^X_y = I⊗I`; cells outside C have c=0). With M_X the 8×|C| matrix of columns sqrt(c_y)X_y, `M_X M_X* = I_8`, so `Gamma_X=M_X* M_X`, `Gamma_X(y,z)=sqrt(c_y c_z)<X_y,X_z>`, is an orthogonal projection and

    sum_{z != y} |Gamma_X(y,z)|^2 = c_y - c_y^2 .                                  (A1)

Gamma_X(y,z)=0 (z!=y) unless (y,z) in 𝒪 (row/column ONBs of X; Q–X product orthogonality), and for different mates X,Y, Gamma_X(y,z)Gamma_Y(y,z)=0 (X–Y product orthogonality). Writing w^X_yz=|<X_y,X_z>|^2 (so w^X w^Y=0 off the diagonal and sum over mates <=1), summing (A1) over the three mates gives for c_y>0:

    sum over z with (y,z) in 𝒪 of c_z >= 3(1-c_y).                                  (TMFI)

**Lemma B (forced partner).** Let a be unit, w an actual a-mixed ray at a cell y, and w' a ray with |<a,w'>|^2=1-c_y such that (i) w' is the only a-active ray orthogonal to w and (ii) every line through w contains w'. Then m(w')>=5; hence this is impossible for nonfixed w'. *Proof.* By (TMFI) at y, at least three w'-cells lie off y's row and column; by (ii) w' also lies in y's row and in y's column. ∎ A sufficient condition for (ii): every ray orthogonal to w other than w' lies in a fixed 2-dimensional subspace (the other three rays of a line through w are orthonormal and orthogonal to w).

## 2. Lemma C (two-vector frame identity)

Summing (A1) over y for one mate X: `sum_{(y,z) in 𝒪} w^X_yz c_y c_z = 8 - sum_y c_y^2` for unit a (sum_y c_y=8 because each row's C-cells are an ONB of W). Homogenized, both sides are Hermitian forms evaluated at a⊗a. Since such a form vanishing on all a⊗a vanishes on Sym^2(W),

    sum_{(y,z) in 𝒪} w^X_yz |sigma_yz><sigma_yz| = 8·I_{Sym^2 W} - sum_y |Q_y⊗Q_y><Q_y⊗Q_y|,    sigma_yz = (Q_y⊗Q_z+Q_z⊗Q_y)/2.

Evaluating at (a⊗b+b⊗a)/sqrt2 for orthonormal a,b in W, and halving the ordered sum:

    sum over unordered pairs {y,z} in 𝒪 of w^X_yz |<a,Q_y><b,Q_z>+<b,Q_y><a,Q_z>|^2 = 8 - 2 sum_y |<a,Q_y>|^2 |<b,Q_y>|^2.     (C1)

**Corollary C2 (separated vectors).** If no ray of C is active for both a and b, the right side is 8 and every pair contributing has one cell a-active and the other b-active. Summing (C1) over the three mates, whose weights are disjoint and at most 1:

    sum over pairs (y,z) in 𝒪 with y a-active, z b-active, of c_y(a) c_z(b) >= 24.

## 3. Lemma D (ray-star lemma)

For an actual ray u of C let sigma_u = dim span_R{P_v : v ray of C, v orthogonal to u}. The map Z -> P_u Z P_(u-perp) on S has kernel S ∩ BD_u (block-diagonal for Cu ⊕ u-perp), which contains P_u and the star span (which annihilates u); write its image as {u chi* : chi in L_u}, L_u a real subspace of u-perp. Then **dim_R L_u <= b-1-sigma_u**, and for every u-active ray v with representative chosen so that v*u>0, P_(u-perp)v lies in L_u.

(i) L_u is not contained in a complex line. (ii) If dim_R L_u=2 then Im<.,.> vanishes on L_u (L_u is *Lagrangian*). *Proof.* Some u-mixed ray exists, otherwise u is orthogonal to all other rays and C would be one-dimensional. (i) If L_u ⊆ Cw, all u-active rays lie in span(u,w); for a mixed v=alpha u+beta w its partner v' is the only u-active ray orthogonal to v, |<u,v'>|^2=1-|<u,v>|^2, and every other ray orthogonal to v is orthogonal to u and w, i.e. lies in the 2-dimensional u-perp ∩ w-perp. Lemma B (a=u) contradicts GAP3. (ii) If Im<.,.> is nonzero on the real 2-plane L_u it is nondegenerate; for orthogonal u-active v=alpha u+lambda, v'=alpha'u+lambda' (alpha,alpha'>0), `<lambda,lambda'>=-alpha alpha'` is real, so lambda' is a real multiple of lambda and v' lies in span(u,lambda). Then the in-plane partner of v is the only u-active ray orthogonal to v, other rays orthogonal to v lie in u-perp ∩ lambda-perp (dimension 2), and Lemma B contradicts GAP3. ∎ Hence dim L_u >= 2 and sigma_u <= b-3.

## 4. Lemma E (pair partitions, C4 with b<=8)

Let E={e1,e2,e3,e4} be any line basis of an intrinsic C4, B=span(e1,e2), P=span(e3,e4) (any relabeling), V_E the elements of S with zero E-diagonal (dimension b-4), X={P_B Z P_P : Z in V_E}. **Then dim X>=3; consequently dim(V_E ∩ (Off_B ⊕ Off_P)) <= b-7.** Here a ray v is *mixing* if v_B,v_P are both nonzero; then v_B v_P* lies in X. A mixing ray exists (else the B-rays and P-rays would be mutually orthogonal and C disconnected).

If dim X<=2, the rank-one part of X is one of: (R0) inside one real or complex line through b p* (b in B, p in P unit) — all mixing rays lie in span(b,p); (R1) all of X with a common B-factor b — mixing rays have B-part ∝ b; (R1') common P-factor p; (R2) exactly two real directions b1p1*, b2p2* with b1∦b2, p1∦p2 — mixing rays lie in Q1∪Q2, Qk=span(bk,pk). (If dim X=1, X=R·M with M of rank 1, or of rank 2 and then no mixing ray. If dim X=2, Re det and Im det are real binary quadratic forms on X: both identically zero gives a real 2-plane of rank<=1 matrices, hence (R1)/(R1'); otherwise there are at most two rank-one directions; zero is impossible, one is (R0), two with b1∥b2 or p1∥p2 would make the whole pencil rank one.) Each case contradicts Lemma B:

* (R0),(R1): a = unit vector of B orthogonal to b. All a-active rays lie in B. Some ray w of B other than the rays a,b exists (if {e1,e2}={a,b}, the actual ray a would otherwise be orthogonal to every other ray). Rays orthogonal to w other than its B-partner lie in P (a mixing ray x has B-part ∝ b with <w,b>≠0).
* (R1'): symmetric with a ⊥ p in P; one of e3,e4 or another P-ray is mixed; the residual space is B.
* (R2), b1⊥b2: if Q2 carries a mixing ray take a=b2 (else a=b1 by symmetry). a-active rays lie in B ∪ Q2, two planes through a whose a-orthogonal directions b1,p2 are orthogonal, so for a mixed w in Q2 the only a-active ray orthogonal to w is its partner; every other ray orthogonal to w lies in span(b1, p2-perp) (B-rays: ∝b1; P-rays: ∝p2-perp; Q1-rays: orthogonal to w only if b-part 0, or all of Q1=span(b1,p2-perp) when p1⊥p2).
* (R2), b1 not ⊥ b2: a = unit of B orthogonal to b1. For a ray w of B with w ∉ {b1, b1-perp, b2-perp}, the only a-active ray orthogonal to w is its B-partner (a Q2-ray γb2+δp2 is orthogonal to w only if γ=0), and rays orthogonal to w lie in P otherwise. Among the orthonormal actual e1,e2 at most the pair {b1,b1-perp} is excluded; in that case use a'=b2-perp and w=b1 symmetrically.

In every case Lemma B contradicts GAP3, so dim X>=3. ∎

## 5. Lemma F (no Lagrangian ray, C4 with b<=8)

Suppose dim L_u=2 for a ray u; by Lemma D it is Lagrangian. Put Xi=R u ⊕ L_u (a real 3-space on which <.,.> is real), Pi=span_C L_u (complex dimension 2), and π a unit vector of W orthogonal to u and Pi. Every u-active ray, normalized, lies in Xi, so is orthogonal to π. A line not through u has total u-weight 1 and so contains 2 or 3 u-active rays, mutually Euclidean-orthogonal in Xi:

* two: x,x' with real parts in L_u; if those were independent the other two rays would lie in Cπ, impossible; so x,x' are an ONB of span(u,λ) (λ in L_u) and the other two rays s,s' are an ONB of u-perp ∩ λ-perp = span(μ,π), μ ∈ L_u ⊥ λ (type II-2);
* three: a real orthonormal frame of Xi, and the fourth ray is π, which is then actual (type II-3).

Applying Lemma E (b<=8) to a II-2 line basis {x,x',s,s'} with B=span(x,x'), P=span(s,s'): the projector P_u lies in S and has a nonzero (x,x') coherence, using the single allowed dimension of Off_B⊕Off_P; so **span(μ,π) contains no actual ray besides s,s'**.

*If π is actual*, it is an actual ray of span(μ,π) for every II-2 line, hence lies in every II-2 and II-3 line; every row then contains u or π, so 8<=m(u)+m(π)<=6 by GAP3 (π, non-orthogonal to some ray of C, is nonfixed).

*If π is not actual*, there are no II-3 lines. No ray is active for both u and π, so Corollary C2 gives Φ = sum over (y,z) in 𝒪, y u-active, z π-active, of c_y(u)c_z(π) >= 24. For a u-cell y, every π-active ray is orthogonal to u and each of y's two lines carries π-weight 1, so its contribution is exactly 6. For a mixed u-active y with ray x ∈ span(u,λ), a π-active ray orthogonal to x is orthogonal to λ, so lies in span(μ,π) and is s or s'; both of y's lines are II-2 lines of the same plane and contain s and s'; by GAP3 at most one further cell of each remains, so the contribution is at most c(s)+c(s')=1 times c_y(u). Since the u-weights of the mixed u-active cells sum to 8-m(u), Φ <= 6m(u)+8-m(u) <= 23 < 24. ∎

## 6. Theorem LOCAL4>=9

**Every intrinsic C4 component of every member of every ordinary four-MOQLS(8) has b>=9.**

*Proof.* Suppose b<=8. By Lemma F every ray u has dim L_u>=3, so sigma_u<=4 (Lemma D). At a cell y with ray u, the other rays of y's row and of y's column are two ONBs of the 3-space u-perp; their transition is connected, split 2+1, or equal.

* Connected: their diagonal algebras give sigma_u>=5. Impossible.
* Split: they share a ray g and the 2-plane P=u-perp ∩ g-perp, with different ONBs there; their projectors span RP_g ⊕ (a 3-space of Herm(P)), so sigma_u=4 and every ray orthogonal to u is g or lies in P. The same rays show sigma_g=4 with star {u} ∪ (rays of P). Hence every line through u contains g and every line through g contains u. With a=(u+g)/sqrt2 the only a-active ray orthogonal to u is g, |<a,g>|^2=1-|<a,u>|^2, and Lemma B gives m(g)>=5, contradicting GAP3.
* Equal at every cell: then each column through a row's cells carries that row's four rays, and each row ray recurs in three further cells, m>=4, contradicting GAP3. ∎

The argument re-proves the adopted b>=8 independently and uses only GAP3 from earlier work. Lemmas A–D hold for components of every dimension.

## 7. Consequence for the q4-span bridge and exact remaining gap

With LOCAL4>=9, a C4-type nonclassical member has span a=4+b>=13. Under the adopted bounds (C5>=10, C6>=12, C7>=13, C8>=15, 4+4>=18 now) and the adopted all-four-nonclassical budget (spans sum <=53), the q4 residual is exactly the type multisets in which at least three members have span 13 — C4-type with b=9 or C5-type with b=10 — and the fourth has span <=14. **q4 is not excluded.** The remaining local targets are LOCAL4>=10 (exclude b=9) and LOCAL5>=11 (exclude b=10). Families with a classical member, A10 (GB15/18, three literal UNKNOWNs) and A11 are unchanged. Required review: Lemma A's projection/disjointness, Lemma C's polarization and the separation step, Lemma D(ii), every case of Lemma E, the II-2/II-3 typing and both branches of Lemma F, and the three cell types of the Theorem.
