# Critical PH7: imbalanced triangles cannot all share one edge

**NEW ALL-TOPOLOGY WRITTEN APPLICATION; conditional on the separately frozen exact triangle-imbalance capacity theorem, independent peer review pending.** MathResearch96h-2. Together with `frontier-20261028-ph7-shared-hub-triangle-budget-v1.md`, this proves that exactly TWO imbalanced triangles of a critical PH7 realization must be **vertex-disjoint**. It does not rule out more triangles or settle 8/9.

## 1. Statement

At z=8/9 no actual PH representation with at most seven states can have all of its imbalanced triangle vertex triples containing the SAME pair of vertices. Balanced triangles, 2-cycles, 4-cycles, arbitrary long cycles and arbitrary edge counts are allowed.

Combined with the separately frozen disjoint-petal/shared-hub theorem and the critical triangle-capacity theorem, this implies:

> If a critical PH7 realization has exactly two imbalanced triangle triples, the two triples are vertex-disjoint.

The reason the common-edge case is new is that the two triangles' outgoing-neighbor sets OVERLAP at the shared edge; the simpler disjoint-petal row budget does not apply.

## 2. Exact shared-edge hitting inequality for one triple

Normalize the irreducible Metzler matrix to a row generator by positive Perron similarity. For a triple `{h,k,x}`, write `P_ij=G_ij/u_i` with `u_i=-G_ii>0`, and abbreviate

    a=P_hk, b=P_kh, c=P_hx, d=P_kx, e=P_xh, f=P_xk,
    R=sqrt(a d e c b f),
    D=1-ab-df-ce-2R,
    W=a d e+c b f-2R.

The two triangle-orientation products differ by `u_h u_k u_x W`; the proper symmetric geometric-mean principal determinant is `u_h u_k u_x D`. Row sums give

    a,c>=0, a+c<=1; b,d>=0, b+d<=1; e,f>=0, e+f<=1.

Irreducibility on all seven states gives `1-ab>0`: equality would make the h,k pair closed. We prove the exact bound

    W/D <= (c+a d)/(1-a b).                          (HIT)

The denominator on the left is strictly positive because the proper symmetric principal block is positive definite. Multiplying through, the difference is

    (c+ad)D-(1-ab)W
      = K(e,f)+2(1-ab-ad-c)R,                        (I)

where K is affine in e,f. The R coefficient is nonnegative since `a(b+d)+c<=a+c<=1`. It remains to check K at the three vertices of the simplex `e,f>=0,e+f<=1`:

    K(0,0)=(1-ab)(ad+c)>=0,
    K(1,0)=c(1-ab-ad-c)>=0,
    K(0,1)=a d(1-ab-d)+c[(1-b-d)-ab(1-b)].

The last expression is affine in c on `[0,1-a]`. Its values at the two endpoints are

    K(0,1)|_(c=0)=ad(1-ab-d)>=0,
    K(0,1)|_(c=1-a)=(1-b-d)[(1-a)(1-ab)+ad]>=0.

All signs use only the three row-sum constraints. Thus K>=0, establishing(HIT). No floating or spectral assumption beyond positivity of the proper principal determinant is needed.

## 3. Summing distinct third vertices on the common edge

For each imbalanced triple `C_x={h,k,x}`, inequality(HIT) says

    w_Cx/det(M_Cx) <= [P_hx+P_hk P_kx]/[1-P_hk P_kh].

The third vertices x are distinct. Since `sum_(x != h,k)P_hx<=1-P_hk` and `sum_(x != h,k)P_kx<=1-P_kh`, the right-hand sides sum to at most1. Interlacing gives `det(M_Cx)<=lambda5 lambda6 lambda7`, so the total imbalance W obeys

    W <= lambda5 lambda6 lambda7.

This contradicts the strict opposite critical inequality in `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md`, SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409`. Thus the common-edge configuration is impossible. Combined with the separate shared-hub disjoint-petal theorem, two imbalanced triples that intersect either in one vertex or in an edge are both impossible; exactly two must be vertex-disjoint. □

## Review boundary

A reviewer should independently verify(I), its affine extreme-point argument, proper-principal positivity, the hitting budget summed across arbitrary third vertices, and the full capacity-theorem dependency. This is written mathematics only; no numerical or machine proof is claimed. It does not rule out three or more imbalanced triples with no common edge, two vertex-disjoint triples, 8/9 feasibility, or PH order8. No novelty, stronger-gate acceptance, or historic process repair is asserted.

END — exactly two imbalanced critical triangle triples must be vertex-disjoint.
