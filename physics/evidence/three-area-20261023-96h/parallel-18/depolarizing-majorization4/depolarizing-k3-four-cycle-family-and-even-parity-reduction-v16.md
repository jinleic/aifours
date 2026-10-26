# Actual k3 continuation v16 — the exact four-cycle family and an exact even-parity reduction

Actual `/bin/date` before drafting: **Sun Oct 25 23:06:56 PDT 2026** (checkpoint066). Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT ACCEPTED, NOT A GLOBAL CLOSURE.** Strict WRITTEN exact algebra; no interpreter/eval/program/CAS/enumeration/solver/CLI/nested agent/GO. HOLD, own root, October27 cutoff11:05:38/deadline12:35:38 unchanged; checkpoint062's own cadence lapse and all earlier findings retained. Zhang attribution (`source-audit-v2-zhang-prior-claim.md`) and unclear priority remain binding.

## 1. The Kraus-sixteen form (any state)

For one qubit, Tr_i(Y) tensor I_i=sum_(b,c) E_cb Y E_cb^dagger with E_cb=|c><b|_i. Hence for EVERY pure psi

    X3(psi)=sum_i sum_(b,c) |E^i_cb psi><E^i_cb psi| = sum_i [D_i(rho)+D_i(X_i rho X_i)],

where D_i is the Z-dephasing (pinching) at site i. E_00,E_11 keep Hamming weight; E_10=sigma_-, E_01=sigma_+ change it by one.

## 2. Even-parity reduction (exact)

Let Z^(tensor4)psi=psi. Then the eight weight-keeping vectors are even and the eight weight-changing vectors are odd, so X3=X_e+X_o with

    X_e=sum_(i,b)|Pi_i^b psi><Pi_i^b psi|,  X_o=sum_i(|sigma_-^i psi><.|+|sigma_+^i psi><.|),

TrX_e=TrX_o=4. The Gram of X_e is the CLASSICAL pair-marginal matrix Prob(x_i=b,x_j=c) of p(x)=|psi_x|^2. Since X3<=4I and X_o=(1/2)sum_i(|X_i psi><.|+|Y_i psi><.|)<=Z/2<=2I, every rank-three trace is at most max(K3(X_e),K2(X_e)+lambda1(X_o),lambda1(X_e)+K2(X_o),K3(X_o)), and the first, second and fourth are <=4,4+2,4. Therefore:

**Lemma E.** For even-parity states, U3(3) is EQUIVALENT to lambda1(X_e)+K2(X_o)<=6.

Both separate bounds lambda1(X_e)<=2+sqrt(R) (bordered form of the Gram [[2,z^T],[z,T/2]], T the ZZ-correlation matrix, lambda1(T)<=4) and K2(X_o)<=4-R/2 (principal xy-block of Gamma and supported CLIP) are tight at products but their sum 6+sqrt(R)-R/2 is not; a joint inequality is NOT proved here.

## 3. The four-cycle family: exact spectrum and U3(3) for all G

Let psi=a|0000>+b(|1100>+|1010>+|0101>+|0011>), a^2=G, 4b^2=w, G+w=1 (edges12,13,24,34 of the cycle1-2-4-3). This is the weight-two direction with the smallest product second-order margin (v14 F1: Q=-3n2+2top2(B-DiagB)=-1, B-DiagB=2t^2 P3 for A=t(P1+P2)).

Using §1 with the dihedral symmetry of the cycle: for each site i, Pi_i^0 psi=a|0>+b(sum of the two edges at the opposite vertex), Pi_i^1 psi=b(sum of the two edges at i), sigma_-^i psi=a e_i+b(c_j+c_k) (j,k the cycle neighbours of i, c_j the weight-three string missing j), sigma_+^i psi=b(e_j+e_k).

Even block, basis (|0>, four edge strings): [[4a^2,2ab 1^T],[2ab 1,4b^2 I+2b^2 Adj(C4)]] (edge-adjacency of C4 is again C4, eigenvalues2,0,0,-2). The all-ones edge vector couples to |0>: [[4G,2sqrt(Gw)],[2sqrt(Gw),2w]], eigenvalues 2G+w+-sqrt(4G^2+w^2); the rest gives w,w,0.

Odd block, basis (e_i, c_i): [[a^2 I+b^2 N,ab Adj],[ab Adj,b^2 N]] with N=2I+2Opp (common-neighbour matrix; Opp swaps opposite vertices). Cycle Fourier modes k=0,1,2,3 give Adj=2,0,-2,0 and N=4,0,4,0: blocks [[G+w,+-sqrt(Gw)],[+-sqrt(Gw),w]] for k=0,2 with eigenvalues mu+-=(G+2w)/2+-(1/2)sqrt(G^2+4Gw), and [[G,0],[0,0]] for k=1,3. Trace check: (4G+2w)+2w+2(G+2w)+2G=8(G+w)=8.

Ordering: sqrt(G^2+4Gw)>=G gives mu+>=G+w=1, while every remaining eigenvalue G, w, mu-, lambda-<=2G+w-2G=w is <=1. Also sqrt(4G^2+w^2)>=w gives lambda+>=2(G+w)=2, and sqrt(G^2+4Gw)<=G+2w gives mu+<=G+2w<=2. Hence the top three are lambda+ and mu+ twice:

    K3=3+sqrt(4G^2+w^2)+sqrt(G^2+4Gw)=3+sqrt(4-8w+5w^2)+sqrt(1+2w-3w^2).

**Proposition C4.** K3<=6 for every w in[0,1], with equality only at w=0. Proof: the claim is sqrt(4-8w+5w^2)<=3-sqrt(1+2w-3w^2). Squaring (both sides nonnegative) reduces it to 3sqrt(1+2w-3w^2)<=3+5w-4w^2 (right side>=3 on[0,1] since 5w-4w^2>=w>=0); squaring again, the difference is 4w(3+7w-10w^2+4w^3), and 3+7w-10w^2+4w^3>0 on[0,1] (its derivative vanishes at w=1/2 where the value is9/2, and the endpoint values are3 and4). Near w=0, K3=6-w-(7/4)w^2+O(w^3), consistent with Q=-1.

Consequently the four-cycle family, its local-unitary images and their convex hull satisfy U3(3) and hence the ORIGINAL k3 comparison at every physical p (v13 §5 coefficient bounds). This family is not in the paired-parity span, the symmetric sector or the W class.

## 4. Scope

New: the Kraus-sixteen/dephasing form, Lemma E (an exact reduction for even-parity states, unproved there), and Proposition C4 (a complete one-parameter family). Not claimed: U3(3) for all even states, global U3(3), the original k3 quartic in general, a counterexample, or formal/kernel/human/family/executable/novelty acceptance. Parkable increment, not a park.
