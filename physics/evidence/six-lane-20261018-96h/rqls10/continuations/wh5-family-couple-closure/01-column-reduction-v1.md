# Exact column reduction for the frozen family-couple closure question (v1)

Recorded after actual `/bin/date`: 2026-10-19T18:32:37-0700. ContinueRQLS10b. Written only, single-author,
unreviewed, not Lean-checked. Scope: 00-scope-freeze-v1.md, SHA-256
fb3caaa56640dd03d3baf9bf8696ba176a798fe45ebbc50f5fedd87f4e498049. This note proves a reduction, NOT closure.
No scripts, enumeration, symbolic/float computation, imports or runtime. All sums below are written mathematical sums.
The later note must dispose of every remaining case before claiming CLOSURE. Maximal 1-RQLS(10) remains OPEN/UNKNOWN.

## 1. Definitions and exact flatness equations
Indices are modulo 5; zeta=exp(2 pi i/5). X e_t=e_(t+1), Z e_t=zeta^t e_t.
f_m(t)=zeta^(mt)/sqrt5; g_m(t)=zeta^(2t^2+mt)/sqrt5. A Hermitian matrix H is flat when all its diagonals in the
three orthonormal bases (e_t), (f_m), (g_m) equal 2/5. Assume its computational diagonal already equals 2/5.
Put phi_a(t)=H_(t+a,t). Character inversion gives:

**Lemma 1.** H is flat iff, for a=1,2,
  sum_t phi_a(t)=0, and sum_t phi_a(t) zeta^(-4at)=0.
Equivalently phi_1 has Fourier support {1,2,3}, phi_2 has Fourier support {1,2,4}.

Proof. 5 f_m^* H f_m = sum_a zeta^(-ma) sum_t phi_a(t). This equals 2 for all m iff each nonzero-a coefficient
vanishes. Likewise 5 g_m^* H g_m = sum_a zeta^(-ma-2a^2) sum_t phi_a(t) zeta^(-4at).
For a=0 both sums give 2. For a replaced by -a, Hermiticity gives phi_(-a)(t)=conj(phi_a(t-a)); its first sum
is the conjugate of the first sum for a, and its weighted sum is a nonzero scalar times the conjugate of the weighted
sum for a. Thus a=1,2 suffice. The second forbidden Fourier frequencies are 4 and 3 respectively. QED.

Let R=diag(zeta^(t^2)) and M=R^* H R. Write q_a(t)=M_(t+a,t). Since
phi_a(t)=zeta^(2at+a^2) q_a(t), Lemma 1 says q_1 has support {-1,0,1} and q_2 has support {-2,0,2}.
Take eta=exp(pi i/5) and z_t=eta zeta^t, so z_t^5=-1. Then
  q_1(t)=u z_t+v+w z_t^(-1)
for arbitrary complex u,v,w. This is an exact three-complex-coefficient representation, not an approximation.
For a diagonal unitary E, R commutes with E. The column of E M E^* is w_t q_1(t),
w_t=e_(t+1) conj(e_t); each w_t is unimodular and product_t w_t=1. Conversely any five such w_t integrate to E,
unique up to a scalar (choose e_0 and recurse). Thus pointwise moduli plus that product are necessary and sufficient
for a prescribed column to come from a diagonal conjugation, provided q_1 never vanishes.

## 2. A symmetry-based phase-retrieval lemma, with proof
Suppose the original flat M has q_1(t)=k(z_t+z_t^(-1))+b with k!=0. Put K=|k|>0.
Let h(t)=u z_t+v+w z_t^(-1) satisfy |h(t)|=|q_1(t)| for all five t.

**Lemma 2.** After multiplication of h by a scalar of modulus one, exactly the following alternatives suffice:
(A) u=w=K and v is one of K b/k or its complex conjugate;
(B) u,w are positive unequal real numbers with u w=K^2, v is real, and
  (u+w)v=2 Re(k conj(b)),
  u^2+w^2+v^2=2K^2+|b|^2.
There is no claim here that every candidate in (B) passes column 2, integrates to a diagonal unitary, or is a projector.

Proof. Expand the Laurent polynomial |u z+v+w/z|^2 on |z|=1. Its coefficient at z^2 is u conj(w), at z is
u conj(v)+v conj(w), and at 1 is |u|^2+|v|^2+|w|^2. Multiplication of the difference from the original modulus-square
by z^2 makes a polynomial of degree at most four. It vanishes at the five distinct z_t, so it is identically zero.
Consequently
  u conj(w)=K^2,
  u conj(v)+v conj(w)=2 Re(k conj(b)),
  |u|^2+|v|^2+|w|^2=2K^2+|b|^2.
The first equality makes u and w nonzero with the same phase. Remove that phase, making both positive real.
The imaginary part of the second equality is (w-u) Im(v)=0.
If u=w, they both equal K. The remaining two equations fix Re(v)=Re(K b/k) and |v|=|b|, hence (A).
If u!=w then v is real and the equations are exactly (B). No factorization theorem is imported. QED.

For the matrices P_tau in the frozen question, write P_tau=R M_tau R^* with M_tau=X_tau X_tau^*+Y_tau Y_tau^*
and X_tau,Y_tau exactly as in the scope-freeze reference. Their displayed coordinates give
  (M_tau)_(-r,-s)=conj((M_tau)_(r,s)).
Therefore q_1(-t-1)=q_1(t). If M_tau satisfies the flatness equations, its coefficient representation has u=w,
hence the form assumed in Lemma 2. The remaining proof must establish the nondegeneracy k!=0 and exclude every
non-original alternative using exact column-2 equations and triangle invariants. Flatness/rank/eigenvector facts
from earlier unreviewed notes are not silently accepted by this reduction.

## 3. Exact remaining obligations
1. Re-prove needed flatness and nondegeneracy facts for M_tau, or expose them as explicit hypotheses.
2. Exclude the conjugate choice in (A), except when it is the same column.
3. Exclude every real unequal-coefficient case (B), with all global phases retained.
4. Enforce product_t w_t=1 in the surviving original-column case and extend by WH/U covariance.
Checkpoint055 stated that a complete argument existed in working form. The derivation was not persisted there;
this reduction alone does not certify that claim. Later delivery must contain the actual proof or explicitly report GAP.
