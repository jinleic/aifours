# The algebraic PH7 endpoint is first-order stationary against ALL seven-state graph edges

**EXACT ALGEBRAIC CANDIDATE; independent review and parent adoption pending.** MathResearch96h-2. This is a topology-unrestricted one-sided TANGENT result at one known endpoint, not a local maximum, global spectral bound, 8/9 exclusion or existence theorem. Its endpoint is the separate exact v4 construction `frontier-20261028-ph7-two-cycle-endpoint-v4.md` SHA256 `4f63347198b12ce6dfefb5c7c94adf95fcc262234d29ce055e6f789bff27e191`, with mandatory correction `frontier-20261028-ph7-two-cycle-endpoint-v4-erratum-v1.md` SHA256 `b5526a1556a61786c5cc382e924087a318b31b6640b35d30a41fe9d3fe22cc30`.

## 1. Precise first-order theorem

Let `(U,V,z_*)` be the unique exact algebraic triple in v4's rational box, isolated by its rational contraction. Set `a=D1/U^4`, where D1 is v4's exact coefficient `[y^2]R`. The positive-diagonal Perron normalization of the endpoint's raw matrix has exactly these off-diagonal transition rates (all unlisted off-diagonal rates are zero):

    1->2, 2->3, 3->4, 4->5: each U;
    5->1: a;       5->6: U-a;
    6->7: V;       7->1: V.                       (G*)

Diagonal entries are minus row sums. These eight edges are strictly positive. Its characteristic polynomial is `D_(z_*)(y) Q_*(y)` for `D_z=y[(y+1)^2+z]^2`.

Consider ANY one-sided differentiable family of seven-by-seven row generators `G(t)`, t>=0, whose 42 off-diagonal rates are nonnegative, with `G(0)=G*`, and ANY differentiable z(t) with z(0)=z_*, such that the characteristic polynomial of every G(t) is divisible by `D_(z(t))`. In particular this hypothesis includes every smooth spectral continuation of a PH7 solution after positive Perron normalization; it does not require or assume the actual PH numerator condition.

For each absent directed edge e let `r'_e(0+)` be its right derivative. Then

    z'(0+) <= -(1/100) sum_(e absent in G*) r'_e(0+) <= 0.  (MAIN)

The stronger equality is `z'(0+)=-sum_absent mu_e r'_e(0+)`, with explicitly defined algebraic `mu_e>1/100`; every active edge has coefficient exactly0. Thus opening ANY of the 34 absent edges at first order forces a strictly negative first-order frequency change; active-edge changes alone have zero first-order change.

This is a necessary tangent condition only. A path with all absent-edge derivatives0 may still improve at second or higher order, and disconnected remote feasible components are unconstrained. The theorem does NOT claim local maximality or solve 8/9.

## 2. Why(G*) is exactly the v4 endpoint

At v4's endpoint, the raw matrix has diagonal `(-U,-U,-U,-U,-U,-V,-V)`, unit superdiagonal, positive feedback D1 from state5 to1 and D3 from7 to1, and its other two feedbacks vanish. Its determinant contains the factor y, so at y=0

    D3=V^2(U^5-D1).

Strict D3,V>0 implies `U^5-D1>0`. A positive zero-eigenvector is

    h=(1,U,U^2,U^3,U^4,U^5-D1,V(U^5-D1)).

The similarity `diag(h)^(-1) G_raw diag(h)` is precisely(G*), with `a=D1/U^4` and `U-a>0`. The exact v4 determinant and sign proof, not a rounded fit, supplies these identities.

## 3. A literal four-coefficient dual for all 42 transitions

Use 1-based indices. For any row generator write

    P(y)=det(yI-G)=y^7+c6 y^6+c5 y^5+...+c1 y,
    p=c6-4,     q=c5-4p-(6+2z).

After eliminating the monic hidden quadratic `y^2+p y+q`, divisibility by D_z is equivalent to the four exact polynomial equalities `F=(F4,F3,F2,F1)=0`:

    F4=c4-[4q+(6+2z)p+4+4z],
    F3=c3-[(6+2z)q+(4+4z)p+(1+z)^2],
    F2=c2-[(4+4z)q+(1+z)^2 p],
    F1=c1-(1+z)^2 q.

For the directed edge i->j, `J_ij` is the four-vector derivative of F when that edge rate increases and the i-th diagonal decreases by the same amount. This uses the ACTUAL seven-by-seven determinant, not an independent spectrum or numerator. Let `J_z` be the derivative of F with respect to z at fixed G. Form the four-by-four matrix

    K = rows (J_12^T, J_51^T, J_67^T, J_z^T),
    L = K^(-1) (0,0,0,1)^T,
    mu_ij=J_ij^T L.                              (DUAL)

The checker proves K invertible at the actual algebraic endpoint and checks, as exact identities/interval statements,

    J_z^T L=1;
    mu_e=0 on all eight edges of(G*);
    mu_e>1/100 on all other 34 off-diagonal edges. (SIGNS)

Indeed, if `D=det K` and `w=adj(K)e4`, then `mu_e=(J_e^T w)/D`. The verifier constructs each J_e from a literal rank-one row perturbation of the full characteristic determinant. It proves `D` lies in `(-30,-20)` on the root box, proves all eight active numerators vanish symbolically, and proves `J_e^T w-D/100<0` for all 34 others; the sign of D then gives(SIGNS).

## 4. Exact enclosure and differentiation

The v4 contraction certificate provides an actual unique zero in the original radius `10^-7` box, with contraction factor q and center residual b satisfying `b/(1-q)<2*10^-9`. Consequently the actual U,V,z_* each differ from centers `1338787907/10^9`, `1042029691/10^9`, `820420441/10^9` by less than `2*10^-9`. Exact centered-polynomial bounds also put a within `10^-6` of `871488314/10^9`. All sign claims in §3 are uniformly certified on this rational four-variable box; there is no floating-root assumption.

Now differentiate `F(G(t),z(t))=0` from the right and multiply by L. Using(SIGNS),

    z'(0+) = - sum_(42 edges) mu_e r'_e(0+)
            = - sum_(34 absent) mu_e r'_e(0+).

Each absent rate is nonnegative and starts at0, so each right derivative is nonnegative. The strict lower bounds on mu give(MAIN). Changes to the eight already positive rates are unrestricted to first order but drop out identically.

## 5. Actual exact checks and scope

Actual invocation:

    python3 frontier-20261028-ph7-all-edge-first-order-check.py
    SymPy 1.14.0 exact all-42-edge tangent dual PASS: 8 zero, 34 >1/100, z-normalized 1

Checker `frontier-20261028-ph7-all-edge-first-order-check.py`, **82LF/4016B**, SHA256 `51254f3a74c8c9623ae5fe335c67a4bbb393705543e0c5b31356301835391042`. Certificate `frontier-20261028-ph7-all-edge-first-order-certificate.json`, **46LF/754B**, SHA256 `efc13dfa7a1cdec7f19e88c2cd5a74565ae71152e5a2e3712f1ae799f5877f6f`.

The checker imports the exact endpoint contraction certificate `frontier-20261028-ph7-two-cycle-interval-certificate.json` SHA256 `2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88`, verifies its residual/factor implications, reconstructs all 42 determinant derivatives and dual expressions symbolically, and applies exact rational centered-monomial bounds over the entire four-variable box. The proof depends on the actual v4 endpoint and its independent general-matrix identity correction, not on its initial floating optimizer. The algebraic/root and interval checks are not a formal proof or external independent review.

This result covers ALL 42 possible directed edges at ONE endpoint, not all generators globally. It imposes no separate numerator, shortest-path, or PH row-exit constraints; those could only further restrict admissible continuations. No stronger gate, novelty, 8/9 decision, or historical process cure is claimed.

END — any differentiable spectral continuation from the explicit algebraic endpoint is nonincreasing at first order, with strictly adverse cost for every newly activated edge.
