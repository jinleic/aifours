# A joint interlacing bound for the y¹ coefficient

**New written lemma candidate, not a new variant of the frozen 0.83 packet.** It does not change any frozen source or assert a sharper exclusion. MathResearch96h-2 / math-1. Native clock observed before writing: **Thu Oct 29 09:18:17 PDT 2026**. Status WRITTEN with the two explicit identities below exact-checked in the owner kernel (SymPy rational polynomials); not a formal proof, independent review or parent adoption. The later numerical discussion is diagnostic only.

## 1. Setup and imports

Use the geometric-symmetrization cover identity and its coefficient extraction (adopted f159/f160 context). Let 𝒜=-S be positive definite, with eigenvalues `0<v1<=...<=v7`. Extra cycles have nonnegative weights omega and at least three vertices. Put `Wj=sum_{|C|=j} omega_C`; for a cycle C write `𝒜_{V-C}` for the complementary principal submatrix. With elementary sums e_k of the seven eigenvalues, and the target characteristic polynomial `y((y+1)²+z)²(y²+py+q)`, write

    W3 = E4,
    E3 = a1+W4,       a1 = sum_{|C|=3} omega_C tr(𝒜_{V-C}),
    E2 = a2+b1+W5,    a2 = sum_{|C|=3} omega_C e2(𝒜_{V-C}), b1 = sum_{|C|=4} omega_C tr(𝒜_{V-C}),
    E1 = a3+b2+c1+W6-P33,

where `a3=sum_{|C|=3} omega_C e3(𝒜_{V-C})`, `b2=sum_{|C|=4} omega_C e2(𝒜_{V-C})`, `c1=sum_{|C|=5} omega_C tr(𝒜_{V-C})`, and P33 is the sum of products over unordered vertex-disjoint pairs of extra 3-cycles. Thus `0<=P33<=W3²/2`. Here

    p=e1-4, q=e2-4e1+10-2z,
    E1=e6-(1+z)²q,
    E2=e5-[(1+z)²p+(4+4z)q],
    E3=e4-[(1+z)²+(4+4z)p+(6+2z)q],
    K=E3-W3*(v1+v2+v3+v4)>=W4>=0.

The coefficient formulas follow from the written cover expansion: at y¹ the only pair contribution is two 3-cycles; at y² no pair contributes. K>=W4 is Ky Fan/interlacing. These are cited at their adopted scopes, not independently re-reviewed here.

## 2. Coupling the trace and second elementary function

Let `s=v1+v2`. For any 3-by-3 principal submatrix 𝒜_U, let its ordered positive eigenvalues be nu1<=nu2<=nu3. Interlacing gives `nu_i>=v_i`, i=1,2,3. Consider

    F(t1,t2,t3)=e2(t1,t2,t3)-s*(t1+t2+t3).

On the full rectangular region `t_i>=v_i`, each partial derivative is nonnegative:

    partial_i F = sum_{j!=i} t_j - s >= sum_{j!=i} v_j-s >= 0.

For i=3 the last lower bound is zero; for i=1,2 it is nonnegative because v3>=v2>=v1. Integrating one coordinate at a time from (v1,v2,v3) to nu therefore yields

    e2(𝒜_U)-s*tr(𝒜_U) >= F(v1,v2,v3) = v1*v2-s² =: B_joint < 0.       (J)

This is a joint inequality for the SAME submatrix; replacing e2 by its lower bound and trace independently by its upper bound loses this coupling.

Equivalently, for `delta_i=nu_i-v_i>=0`, the exact polynomial identity

    F(v+delta)-F(v) = (v3-v1)*delta1+(v3-v2)*delta2+delta1*delta2+delta1*delta3+delta2*delta3

is a sum of nonnegative terms. This identity and `F(v1,v2,v3)=v1*v2-s²` were expanded exactly in the owner kernel using symbolic rational polynomial arithmetic; both residuals were zero.

Multiplying by the nonnegative cycle weights gives `b2-s*b1>=W4*B_joint`. As B_joint<0 and W4<=K,

    b2-s*b1 >= K*B_joint.

## 3. New polynomial necessary inequality

For each four-state complement, separate interlacing bounds still give

    a3-s*a2 >= W3*alpha,
    alpha=e3(v1,v2,v3,v4)-s*e2(v4,v5,v6,v7).

Also `c1>=s*W5`, by the two-state Ky Fan bound. Subtract s times the E2 identity from the E1 identity:

    E1-s*E2 = (a3-s*a2)+(b2-s*b1)+(c1-s*W5)+W6-P33
             >= W3*alpha+K*B_joint-W3²/2.

Thus every realization obeys the polynomial necessary condition

    Y1_joint := E1-s*E2-W3*alpha-K*B_joint+W3²/2 >= 0.                  (YJ)

It strengthens the frozen Lemma 6 inequality: its previous coefficient was

    beta_old=e2(v1,v2,v3)-s*(v5+v6+v7),
    B_joint-beta_old=s*((v5+v6+v7)-(v1+v2+v3))>=0,
    Y1_old-Y1_joint=K*(B_joint-beta_old)>=0.

No negative-weight or unordered-spectral hypothesis is used. The rate ordering and K>=0 are necessary in this comparison.

## 4. Optional stronger nonpolynomial bound

For the four-state complement eigenvalues mu, interlacing places `mu_i in [v_i,v_{i+3}]`, i=1..4. The function `e3(mu)-s*e2(mu)` is multi-affine, so its minimum on this rectangle is the minimum M3 of its sixteen corner values. Replacing alpha by M3 in (YJ) is valid and at least as strong, since `M3>=alpha`. A certificate of negativity using that version must handle the minimum correctly: with W3>=0, `Y1_corner` is the MAXIMUM of sixteen polynomial expressions `E1-sE2-W3*psi_corner-K*B_joint+W3²/2`; showing only one of them negative would be insufficient. No corner certificate is claimed here.

## 5. Exact contact with the adopted v4 construction

The adopted v4 endpoint spectrum is `(V,V,U,U,U,U,U)` with V<U. Its extra-cycle graph has only lengths 5 and 7, so `W3=W4=0`, hence `E4=E3=K=0`. The length-5 complement contains exactly the two V states, so `c1=2V*W5=s*E2`, and `E1-sE2=0`. Therefore both the old and joint y¹ inequalities are EXACTLY TIGHT at that endpoint; this follows from the displayed graph and identities, not the floating optimizer. It does not prove global or local optimality.

The owner kernel additionally expanded `(y+U)^5(y+V)^2-y((y+1)^2+z)^2(y²+py+q)` symbolically, with p,q fixed by its leading coefficients. It checked the identities `W3=[y^4]R`, `E3=[y^3]R`, and `E1-2V*E2=[y]R-2V[y²]R`; these are exactly the three endpoint defining equations. This check confirms contact at the adopted algebraic root, not a maximum assertion.

## 6. Numerical diagnostics, not upper bounds

In the retained owner kernel, SLSQP maximizing z over the sorted-spectral relaxation `{p,q,W3,K,Y2b,Y1_joint,Y0>=0}` from a perturbed v4 spectrum returned z≈0.8204204407841365 with the spectrum `(V,V,U,U,U,U,U)`. A later multistart run (random seed31, 400-second bound) returned 336 feasible local candidates; the largest returned values agreed to nine decimals with the same spectrum. This is numerical evidence only: no global maximum, no validated local optimality, no strict gap and no supremum equality is established. Y0 in this numerical test is a separately derived diagnostic lower bound from the constant coefficient, not a proof premise of Sections 1–5.

The next mathematical gap is an exact infeasibility certificate above the endpoint using this tighter condition, or a rigorously controlled neighborhood plus global complement argument. The frozen f180 review concerns the earlier, weaker inequality and remains unchanged.

END — the joint principal-submatrix inequality (J) yields a strictly sharper polynomial necessary condition; no new excluded ratio is claimed.
