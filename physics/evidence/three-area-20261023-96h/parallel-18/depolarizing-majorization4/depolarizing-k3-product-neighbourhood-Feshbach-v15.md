# Actual k3 continuation v15 — an explicit product neighbourhood: U3 at rank three whenever the maximal product overlap is at least 124/125

Actual `/bin/date` before this body: **Sun Oct 25 22:54:15 PDT 2026**. Owner PhysicsDepol4-2 / physics-2. **NEW AUTHOR-WRITTEN CANDIDATE THEOREM, NOT ACCEPTED, NOT A GLOBAL CLOSURE.** Strict WRITTEN exact algebra with hand-evaluated rational bounds; no interpreter/eval/program/CAS/enumeration/solver/CLI/nested agent/GO. HOLD, own root, October27 cutoff11:05:38/deadline12:35:38 unchanged; checkpoint062's own cadence lapse and all earlier findings retained. Zhang's matched clipping attribution (`source-audit-v2-zhang-prior-claim.md`) and unclear priority remain binding. The earlier near-product addendum (`local-product-full-addendum-v1.md`, radius 1-G<=1/900000000, all indices) is NOT used; this is a separate, much larger rank-three neighbourhood.

## 1. Statement

For a pure four-qubit psi let G(psi)=max over product unit vectors phi of |<phi|psi>|^2.

**Theorem NP.** If G(psi)>=124/125 then K3(X3(psi))<=6, with margin K3<=6-(1-G)/40. Hence for every density supported on the convex hull of such pure states, every complex rank-three projector Pi and every physical 0<=p<=4/3,

    Tr Pi D_p^(tensor4)(rho) <= K3(D_p^(tensor4)(|0000><0000|)),

by the universal coefficient bounds Tr Pi rho<=1, Tr Pi X1<=10, Tr Pi X2<=12 and the exact expansion/reflection of v13 §5 (U3 at rank three is exactly the automatic c<=0 branch).

## 2. Normal form

Choose a maximising product vector and apply local unitaries so it is |0>:=|0000>; fix the phase so <0|psi>=sqrt(G)>0. Stationarity of the maximum under the one-site variations |0>_i -> cos(t)|0>_i+e^{ia}sin(t)|1>_i gives Re(e^{-ia}<e_i|psi>)sqrt(G)=0 for all a, so <e_i|psi>=0 for every single excitation e_i. Thus

    psi=sqrt(G)|0>+sqrt(w) eta,  w:=1-G,

with eta a unit vector supported on Hamming weights2,3,4. Let n2,n3,n4 be its weight norms (n2+n3+n4=1), A_il=eta_{il} (complex symmetric, zero diagonal), B=AA^dagger.

Since X3 is linear, X3(rho)=G T+g X1+w X2 with g=sqrt(Gw), T=X3(|0><0|)=4|0><0|+sum|e_i><e_i|, X1=X3(|0><eta|+|eta><0|), X2=X3(|eta><eta|). Split C^16=E4+E1+E0 with E4=C|0>, E1=span(e_i), E0 the eleven weight>=2 strings. Direct computation from Tr_l(|0><eta|)=|0_lbar><eta_{l,0}| shows:

- X1 has only E4-E0 and E1-E0 blocks (and adjoints): <0|X1|x>=(4-|x|)conj(eta_x)=:u_x, <e_i|X1|y>=conj(eta_{y-e_i}) for y containing i, =:W_iy.
- X2 has ZERO E4 row (eta has no weight0/1 amplitudes), E1 block exactly B, and 0<=X2<=4I.

Hence, with Y=X2|_{E1,E0}, Z0=X2|_{E0}, M=gW+wY,

    X3 = [[4G, 0, g u],[0, G I+wB, M],[g u^dagger, M^dagger, w Z0]].

Exact traces: |u|^2=4n2+n3, TrWW^dagger=2n2+n3 (so ||W||^2<=2), TrB=2n2 (so ||B||<=2). Positivity of [[B,Y],[Y^dagger,Z0]] with Z0<=4I gives YY^dagger<=4B.

## 3. Haynsworth/Feshbach eigenvalue bounds

Let H22=wZ0 (norm<=4w) and S(mu)=H11+H12(mu-H22)^{-1}H21 for mu>4w. Haynsworth inertia gives #{eig X3>lambda}=#{eig S(lambda)>lambda} for lambda>4w, and S is decreasing in lambda; therefore lambda_k(X3)<=max(mu,lambda_k(S(mu))) for every k and mu>4w. Bound S(mu)<=H11+H12H12^dagger/(mu-4w)=:Stilde(mu).

- k=1 at mu=4G (requires 4G>4w): lambda1(Stilde)>=4G, so lambda1(X3)<=lambda1(Stilde(4G))<=a1+|c1|^2/(a1-lambdamax(E1)), with a1=4G+Gw|u|^2/D1, D1=4G-4w, c1=g u M^dagger/D1, E1=GI+wB+MM^dagger/D1 (bordered top-eigenvalue bound).
- k=2,3 at mu=G (requires G>4w): lambda3(S(G))>=lambda3(H11)>=G, so lambda2+lambda3 of X3 is at most lambda2+lambda3 of Stilde(G)=[[a,c],[c^dagger,E]], a>=4G, E=GI+wB+MM^dagger/DG, c=g u M^dagger/DG, DG=G-4w. Using [[0,c],[c^dagger,0]]>=-[[2,0],[0,c^dagger c/2]] and a-2>=lambdamax(E): K3(Stilde)<=a+K2(E)+|c|^2/2, and lambda1(Stilde)>=a, so lambda2+lambda3<=K2(E)+|c|^2/2.

Hence

    K3(X3)<=6G + w[ G|u|^2/D1 + K2(B) + K2(MM^dagger)/(w DG) ] + |c1|^2/(a1-lambdamax E1) + |c|^2/2.

With MM^dagger<=(1+s)Gw WW^dagger+(1+1/s)w^2 YY^dagger (any s>0), K2(WW^dagger)<=2n2+n3, K2(YY^dagger)<=4K2(B)<=8n2, ||M||^2<=2(1+s)Gw+8(1+1/s)w^2.

## 4. Rational evaluation at w<=1/125, s=1/5 (hand arithmetic)

Coefficient of w in the bracket, maximised at n2=1 (all n3/n4 coefficients are smaller):

- G|u|^2/D1<=4(1-w)/(4(1-2w))<=125/123<1.0163;
- K2(B)<=2;
- (1+s)G K2(WW^dagger)/DG<=2(6/5)/(1-5w)<=(12/5)(25/24)=5/2;
- (1+1/s)w*8/DG<=48w/(1-5w)<=(48/125)(25/24)=2/5.

Sum<5.9163. Remainders: |c|^2/(2w)<=2(12/5+48/125)/(24/25)^2/125=(2*348*625)/(125*125*576)<0.0484; and with D1>=4*123/125>3.93, a1-lambdamax(E1)>=4(124/125)-(1+2/125+0.006)>2.94: |c1|^2/((a1-lambdamax E1)w)<=4*(12/5+48/125)/(125*3.93^2*2.94)<0.0021. Total coefficient<5.9668<6-1/40=5.975, so K3(X3)<=6G+(6-1/40)w=6-w/40. Side conditions hold: 4G>4w, G>4w, a-2>=3.968-2>1.04>=lambdamax(E) (lambdamax(E)<=1+2/125+(2.784/125)/0.96<1.04).

## 5. Controls and scope

At G=1 the bound is the exact product value6. The second-order coefficient of v14 F1 is consistent (exact Q<=0; this rigorous bound gives K3<=6-w/40 throughout w<=1/125). Closed-form controls: |0000>+e|1111> gives K3=6-6e^2+O(e^4); (|00>+e|11>)|00> gives K3=6-3e^2+O(e^3); |0>(|000>+e|111>) gives K3=6-(19/4)e^2+O(e^3).

Not claimed: any state with G<124/125 outside other separately stated regions; global U3(3); a channel counterexample; formal/kernel/human/family/executable/novelty acceptance. This is a parkable increment, not a park.
