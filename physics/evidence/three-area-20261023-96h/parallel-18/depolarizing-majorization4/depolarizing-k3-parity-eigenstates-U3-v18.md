# Actual k3 continuation v18 — U3 at rank three for EVERY parity eigenstate (and all their local-unitary images)

Actual `/bin/date` before this body: **Sun Oct 25 23:28:15 PDT 2026**. Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE THEOREM, NOT ACCEPTED, NOT A GLOBAL CLOSURE.** Strict WRITTEN exact algebra; no interpreter/eval/program/CAS/enumeration/solver/CLI/nested agent/GO. HOLD, own root, October27 cutoff11:05:38/deadline12:35:38 unchanged; all process findings (including checkpoint062's own cadence lapse) retained. Zhang attribution (`source-audit-v2-zhang-prior-claim.md`) and unclear priority remain binding; no novelty claim.

Imports: the full operator bound Z<=4I (v9 eq.(6), parent-supported through `depol-original-global-k4-parent-v1.md`); elementary Ky Fan subadditivity, Cauchy interlacing, rank-one secular equations. This packet supersedes the open status of v16 Lemma E and v17 §4 (those files are unchanged; their stated open target is now proved here).

## 1. Statement

**Theorem PAR.** Let psi be a pure four-qubit state with Z^(tensor4)psi=+-psi. Then K3(X3(psi))<=6. The same holds for every state (U1 tensor U2 tensor U3 tensor U4)psi, i.e. every eigenvector of some product operator (n1.sigma) tensor...tensor (n4.sigma), and for every density in the convex hull of such states.

Consequently (v13 §5: Tr Pi rho<=1, Tr Pi X1<=10, Tr Pi X2<=12, exact expansion and reflection) the ORIGINAL k3 comparison Tr Pi D_p^(tensor4)(rho)<=K3(D_p^(tensor4)(|0000><0000|)) holds for all these densities, every complex rank-three Pi and every physical 0<=p<=4/3.

Odd states reduce to even ones by the local unitary X_1, and X3 is LU-covariant; so assume Z^(tensor4)psi=psi below.

## 2. Parity splitting (Kraus-sixteen form)

Tr_i(Y) tensor I_i=D_i(Y)+X_i D_i(Y) X_i with D_i the Z-dephasing at site i. Hence X3=X_e+X_o, X_e=sum_i D_i(rho) (even block), X_o=sum_i X_i D_i(rho) X_i=(1/2)sum_i(X_i rho X_i+Y_i rho Y_i) (odd block). TrX_e=TrX_o=4, and X_o<=Z/2<=2I. The best rank-three trace is max over j of K_j(X_e)+K_(3-j)(X_o); the cases j=3,2,0 are at most 4, 4+2, 4. So it suffices to prove

    lambda1(X_e)+K2(X_o)<=6.                                   (E)

## 3. Even block: lambda1(X_e)<=2(1+m_max)

X_e=2rho+(1/2)sum_i Z_i rho Z_i has entries psi_x conj(psi_y)(4-d(x,y)). On the eight even strings distances are0,2,4 and d=4 exactly for the global flip xbar, so 4J-Dist=2I+2J-2P_ant. With p_x=|psi_x|^2 and the diagonal unitary of phases, X_e is unitarily similar to

    2H,  H=s s^T+sum_k m_k vhat_k vhat_k^T,

s=sqrt(p) (unit), antipodal pairs k=(x,xbar), m_k=p_x+p_xbar (sum m_k=1), d_k=p_x-p_xbar, vhat_k=(sqrt(p_x),-sqrt(p_xbar))/sqrt(m_k); the complementary pair vectors uhat_k have eigenvalue0 under the second term. Let lambda=lambda1(H) and m_max=max m_k. If lambda<=m_max we are done. Otherwise lambda-M0 is invertible, the top eigenvector has s^T x!=0, and 1=s^T(lambda-M0)^{-1}s; with (s.vhat_k)^2=d_k^2/m_k and (s.uhat_k)^2=m_k-d_k^2/m_k this is exactly

    lambda=1+sum_k d_k^2/(lambda-m_k).                         (SEC)

phi(t)=1+sum_k d_k^2/(t-m_k)-t is strictly decreasing on (m_max,infinity) with phi(lambda)=0. At t0=1+m_max every denominator is >=1, so

    phi(t0)<=sum_k d_k^2-m_max<=sum_k m_k^2-m_max<=m_max sum_k m_k-m_max=0.

Hence lambda<=1+m_max and lambda1(X_e)<=2+2m_max.

## 4. Odd block: K2(X_o)<=4-2m_max

Choose an antipodal pair (x,xbar) of maximal mass and apply the local unitary prod_(i: x_i=1)X_i (an even number of flips, preserving parity, LU-covariant for X3): WLOG it is (0000,1111). Write psi=a|0000>+sum_e c_e|s_e>+f|1111> over the six weight-two strings, m_max=|a|^2+|f|^2, S=sum|c_e|^2=1-m_max. The odd vectors are

    u_i=sigma_-^i psi=a e_i+sum_(l!=i) c_([4]\{i,l}) c_l,
    t_i=sigma_+^i psi=sum_(j!=i) c_(ij) e_j+f c_i,

(e_j weight-one strings, c_l the weight-three string missing l), and X_o=sum_i(|u_i><u_i|+|t_i><t_i|)=Xi Xi^dagger+Theta Theta^dagger with Xi=[aI;Atilde], Theta=[A;fI] (A_ji=c_ij, Atilde_li=c_([4]\{i,l}), zero diagonals). Then Xi^dagger Xi=|a|^2 I+Atilde^dagger Atilde and Theta^dagger Theta=A^dagger A+|f|^2 I, with Tr(Atilde^dagger Atilde)=Tr(A^dagger A)=2S. By Ky Fan subadditivity and K2<=trace for PSD matrices,

    K2(X_o)<=2|a|^2+2S+2|f|^2+2S=2m_max+4(1-m_max)=4-2m_max.

## 5. Conclusion and controls

(E) follows: lambda1(X_e)+K2(X_o)<=2+2m_max+4-2m_max=6. This proves Theorem PAR.

Controls (exact): product: m_max=1, lambda1(X_e)=4, K2(X_o)=2 (both bounds tight). a|0000>+b|1111>: lambda1(X_e)=2+2|a^2-b^2|<=4, K2(X_o)=1+|a^2-b^2|<=2. Four-cycle family (v16): lambda1(X_e)=1+G+sqrt(5G^2-2G+1)<=2+2max(G,w/2) and K2(X_o)=2-G+sqrt(4G-3G^2), consistent with K3=3+sqrt(4G^2+w^2)+sqrt(G^2+4Gw)<=6. GHZ: 2+1=3.

Scope: the set of parity eigenstates up to local unitaries is a proper (22-real-dimensional) subset of all pure states. It contains the W state itself (but NOT the general vacuum-plus-single-excitation class of v12, which mixes parities), GHZ, every Dicke state, the whole paired-parity span (v12), the cluster state (LU-equivalent to (|0000>+|0011>+|1100>-|1111>)/2) and the four-cycle family (v16). **Arbitrary states without such a product-Pauli eigen-symmetry remain OPEN** for original k3; no global U3(3), quartic closure, counterexample or formal/kernel/human/family/executable/novelty acceptance is claimed. Parkable increment, not a park.
