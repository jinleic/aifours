# Actual k3 continuation v14 — exact off-face reduction, a two-mode sufficient target, and the product-state second-order coefficient

Actual `/bin/date` before this body: **Sun Oct 25 22:35:09 PDT 2026** (checkpoint063). Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE LEMMAS, NOT ACCEPTED, NOT A CLOSURE.** Strict WRITTEN reasoning; no interpreter/eval/program/CAS/enumeration/solver/CLI/nested agent/GO. HOLD, own root, October27 cutoff11:05:38/deadline12:35:38 unchanged. Process history retained, including the NEW own cadence lapse disclosed in checkpoint062 (due21:58:37, written22:05:49). Zhang's matched clipping attribution (`source-audit-v2-zhang-prior-claim.md`) and unclear priority remain binding.

Named imports (parent-supported, not re-proved here): global CLIP `K2(Gamma)<=8-R` and its margin K2M (`depol-global-CLIP-v6-parent-v1.md`); the full Schur inequality `4I-F>=vv*/delta` and `Zpsi=Lpsi` (v9 §2–3, parent `depol-original-global-k4-parent-v1.md`); universal coefficient bounds and channel expansion (v13 §5).

## 1. Notation

Pure psi, twelve local Paulis S_mu, r_mu=<S_mu>, R=|r|^2, delta=4-R, L=sum r_mu S_mu, V=Var(L). Z=sum_mu|S_mu psi><S_mu psi|=[[R,v*],[v,F]] on C psi + psi-perp, v=QLpsi, ||v||^2=V, X3=2rho+Z/2. N:=4I-F (15x15, PSD). Gamma is the centered12x12 Gram; N has eigenvalues 4-gamma_j and three extra4s.

## 2. Exact equivalence for U3 at rank three (F2)

For a rank-three Pi, write d=1-<psi|Pi|psi>, xi=Pi psi/||Pi psi||, xi=sqrt(1-d)psi+sqrt(d)eta (eta unit, orthogonal to psi), P=Pi-|xi><xi| (rank two, orthogonal to psi and eta). The exact identity is

    12-2Tr(Pi X3)=Tr[Pi(4I-2X3)],   4I-2X3=4I-4rho-Z=[[-R,-v*],[-v,N]].

Thus Tr Pi X3<=6 for all rank-three Pi iff the three smallest eigenvalues of this bordered matrix sum to >=0. Minimising over d the 2x2 form [[-R,-sqrt(a)],[-sqrt(a),n]] (a=|<v|eta>|^2, n=<eta|N|eta>, phases chosen adversarially) gives ((n-R)-sqrt((n+R)^2+4a))/2; the optimal P contributes b_eta, the sum of the two smallest eigenvalues of N compressed to {psi,eta}-perp. Squaring (the right base n-R+2b is >=0 because b>=bottom2(N)>=R by interlacing and supported CLIP) shows:

**F2.** K3(X3(psi))<=6 for EVERY complex rank-three projector iff for every unit eta orthogonal to psi

    |<v|eta>|^2 <= (b_eta-R)(n_eta+b_eta).

## 3. A sufficient scalar two-mode target

Interlacing gives b_eta>=B2:=bottom-two of N=8-K2(Gamma). Schur gives |<v|eta>|^2<=delta*n_eta, and trivially <=V. The right side of F2 increases in b and n, so it suffices that min(V,delta n)<=(B2-R)(n+B2) for all n>=0; the binding point is n=V/delta. Hence:

**Lemma S.** If V(K2(Gamma)-4)<=delta(8-K2(Gamma))(8-R-K2(Gamma)), then U3(3) holds at psi; equivalently K2(Gamma)<=4+x_-, with Y=V/delta,

    x_- = [(4+delta+Y)-sqrt((4+delta+Y)^2-16delta)]/2.

Endpoints: V=0 gives x_-=delta (exactly CLIP). V=R*delta (the Schur/Z^2<=4Z maximum) gives K2(Gamma)<=8-2sqrt(R). The identity V=2delta-delta^2+4C+epsilon gives Y in[2-delta,R]. Exact controls (closed-form Gamma spectra): cos|0000>+sin|1111> (eigenvalues1+t x4,1-t x4,4(1-t^2), t=cos2theta, R=4t^2) satisfies K2<=8-4t since 4t^2-5t+3>0 and 2+2t<=8-4t; (|00>+eps|11>)|00> has K2=4<8-2sqrt(R); |0>GHZ3 and W (R=1) have K2=5<=6.

Lemma S is a SUFFICIENT target only; it is NOT proved globally. The supported K2M margin delta^2/(24+14delta) is weaker than the ~delta/2 margin needed near products.

## 4. Product-state second-order coefficient (F1)

Closest-product normal form: psi_eps proportional to |0000>+eps*eta with eta orthogonal to |0000> and NO weight-one amplitudes (stationarity of the maximal product overlap). Let n_w be the weight-w norm of eta, A the complex symmetric zero-diagonal matrix A_il=eta_il, B=AA*, tau_i the amplitude of the weight-three string missing i. Exact degenerate perturbation theory (the single-excitation cluster has vanishing first-order block) gives

    lambda1 = 4+eps^2(-3n2-(15/4)n3-4n4)+O(eps^3),
    H_eff = 2B-2Diag(B)+conj(tau)tau^T-(|tau|^2+n4)I,
    K3(X3) = 6+eps^2 Q+O(eps^3),  Q<=2top2(B-DiagB)-3n2-(19/4)n3-6n4.

**Lemma T2.** top2(B-Diag B)<=(3/4)TrB for PSD 4x4 B (convexity reduces to B=vv*; interlacing gives mu2<=-min|v_i|^2<=0; mu1=max_y 2e2(w), w_i=y_i|v_i|, sum w<=1, so mu1<=3/4), strict pointwise. Hence Q<=0, and Q<0 for every nonzero normal eta.

Exact controls: |0000>+eps|1111> gives Q=-6; (|00>+eps|11>)|00> gives Q=-3 (cluster exactly1); |0>(|000>+eps|111>) gives Q=-19/4 (cluster1,c^2,c^2,c^2). SCOPE: a Taylor coefficient along each fixed direction; no neighbourhood theorem and no third-order control.

## 5. Pair-cut Werner–Holevo form (F3)

On a qubit pair in the magic basis D_p tensor D_p=((1-p)(2-p)/2)id+(3/2)p(1-p)W+p^2 Delta, W(X)=(Tr(X)I-X^T)/3, a convex combination for0<=p<=1. X3=2id+3W_A+3W_B; superoperator spectrum8,6,4,4,2,0. If both pair-cut Schmidt bases are magic-real, spec X3={2, s_m^2+s_n^2 twice per pair,0}: full U3 with K3<=4 (a small family).

## 6. Two new open-type regions from Lemma S (written)

Write x=K2(Gamma)-4. Lemma S is the quadratic condition x^2-x(4+delta+Y)+4delta>=0 with roots x_-<=delta<=4<=x_+ (x_-x_+=4delta); CLIP gives x<=delta, so Lemma S holds iff x<=x_-. Since x_+ increases in Y and Y<=R, x_->=x_-(delta,R)=4-2sqrt(R)=2delta/(2+sqrt(R)).

**Corollary R1.** If K2(Gamma(psi))<=4, then K3(X3(psi))<=6 for EVERY complex rank-three projector (x<=0<=x_-).

**Corollary R2 (two nearly pure qubits).** Let e_(1)<=e_(2) be the two smallest impurities e_i=1-t_i^2 and s=e_(1)+e_(2). The supported two-mode placement UP2 (v6 §5: K2(Gamma)<=4+sqrt(6s), parent-supported in `depol-global-CLIP-v6-parent-v1.md`) gives x<=sqrt(6s). Hence U3(3) holds whenever

    6s <= (4-2sqrt(R))^2,  i.e.  s <= (2/3) delta^2/(2+sqrt(R))^2.

Examples: two exactly pure qubits (s=0) with ARBITRARY entangled remaining pair; e=(e,e,1,1) gives the explicit condition 12e<=(4-2sqrt(2-2e))^2, satisfied e.g. for all e<=1/10 (at e=1/10: 1.2<=(4-2sqrt(1.8))^2, and 2sqrt(1.8)<2*1.3417=2.6834, so the right side exceeds1.3166^2>1.73). Mixed states in the convex hull of either region inherit U3(3) by convexity of K3 at fixed projectors; the original k3 comparison then follows at all physical p by the universal coefficient bounds of v13 §5 (U3(3) places every pair in the automatic c<=0 branch).

Near generic product states R2 requires e_(1)+e_(2)<=delta^2/24 approximately, so it does NOT cover a full product neighbourhood; F1 indicates such a neighbourhood is plausible but unproved.

## 7. Remaining gap

Global U3(3), Lemma S's two-mode target, CLIP-prime and the original k3 quartic remain UNPROVED outside the stated families/regions (now including R1/R2); no counterexample. This packet is a parkable increment, not a park.
