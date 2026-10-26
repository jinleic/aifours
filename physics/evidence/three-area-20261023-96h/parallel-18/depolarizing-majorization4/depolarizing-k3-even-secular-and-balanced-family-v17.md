# Actual k3 continuation v17 — exact even-sector secular equation, the balanced even family, and k4-based sufficient conditions

Actual `/bin/date` before drafting: **Sun Oct 25 23:20:07 PDT 2026** (checkpoint068). Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT ACCEPTED, NOT A GLOBAL CLOSURE.** Strict WRITTEN exact algebra; no interpreter/eval/program/CAS/enumeration/solver/CLI/nested agent/GO. HOLD, own root, October27 cutoff11:05:38/deadline12:35:38 unchanged; all process findings (including checkpoint062's own cadence lapse) retained. Zhang attribution (`source-audit-v2-zhang-prior-claim.md`) remains binding. Named imports: v16 Lemma E and Kraus-sixteen form (author candidate, same owner), the parent-supported global k4 theorem (`depol-original-global-k4-parent-v1.md`), X3<=4I.

## 1. A general k4-based sufficient condition

For any pure psi and rank-three Pi, adding any unit vector orthogonal to Pi gives a rank-four projector, so the supported global bound Tr(Pi4 X3)<=7 yields K3(X3)<=7-lambda4(X3). **Hence U3(3) holds whenever lambda4(X3)>=1**, and every U3(3) violator has lambda4(X3)<1.

For even-parity psi (X3=X_e+X_o, v16), the same argument with Pi4 spanned by the top two even and top two odd, or one even and three odd, eigenvectors gives

    lambda1(X_e)+K2(X_o)<=7-max(lambda2(X_e),lambda3(X_o)),

so Lemma E (hence U3(3)) holds whenever lambda2(X_e)>=1 or lambda3(X_o)>=1.

## 2. Exact even-sector spectrum

For even psi, X_e=sum_i D_i(rho)=2rho+(1/2)sum_i Z_i rho Z_i has entries psi_x conj(psi_y)(4-d(x,y)), i.e. X_e=rho o K with K=4J-Dist on the eight even strings. Distances are0,2,4, so K=2I+2J-2P_ant, with P_ant the global-flip pairing x<->xbar. The nonzero spectrum of rho o K equals that of diag(sqrt p) K diag(sqrt p), p_x=|psi_x|^2, which is

    2[ s s^T + sum_k m_k vhat_k vhat_k^T ],   s=sqrt(p) (unit),

with antipodal pairs k=(x,xbar), m_k=p_x+p_xbar, d_k=p_x-p_xbar, vhat_k=(sqrt(p_x),-sqrt(p_xbar))/sqrt(m_k), and the complementary unit vectors uhat_k=(sqrt(p_xbar),sqrt(p_x))/sqrt(m_k) carrying eigenvalue0 of the second term. Since s.vhat_k=d_k/sqrt(m_k) and (s.vhat_k)^2+(s.uhat_k)^2=m_k, the rank-one secular equation 1=s^T(lambda-M0)^{-1}s becomes, for lambda above max m_k,

    lambda = 1 + sum_k d_k^2/(lambda-m_k).                    (SEC)

**Proposition SEC.** lambda1(X_e)=2 lambda*, lambda* the largest root of (SEC). Controls: product (one pair, d=m=1): lambda*=2; a|0000>+b|1111>: lambda*=1+|a^2-b^2|; the v16 four-cycle family: lambda*=[(1+G)+sqrt(5G^2-2G+1)]/2, i.e. lambda1(X_e)=1+G+sqrt(5G^2-2G+1)=2G+w+sqrt(4G^2+w^2), matching v16 exactly.

## 3. Balanced even family

**Theorem BE.** If Z^(tensor4)psi=psi and |psi_x|=|psi_xbar| for every string x, then K3(X3(psi))<=6.

Proof. All d_k=0, so (SEC) gives lambda*=1 (if some m_k=1 the second term has eigenvalue m_k=1 on vhat_k orthogonal to s, and lambda1=1 directly). Thus lambda1(X_e)=2 and, by Lemma E, the only nontrivial rank-three trace is at most 2+K2(X_o)<=2+TrX_o=6.

Consequently the ORIGINAL k3 comparison holds at every physical p (v13 §5) for every balanced even state, its local-unitary images and their convex hull. Examples: GHZ (K3=4.5), any even state whose amplitudes on each antipodal pair have equal modulus with arbitrary phases.

## 4. Exact remaining target for general even states

Lemma E is equivalent to bottom6(X_o)>=2(lambda*-1)=2 sum_k d_k^2/(lambda*-m_k): the odd (hopping) sector must be at least as spread as the classical antipodal imbalance forces. Phases enter only X_o. Not proved here; the product saturates it (bottom6=2, lambda*=2).

## 5. Scope

New: the k4-based sufficient conditions, Proposition SEC and Theorem BE. Not claimed: general even states, global U3(3), the original k3 quartic in general, a counterexample, or any formal/kernel/human/family/executable/novelty acceptance. Parkable increment, not a park.
