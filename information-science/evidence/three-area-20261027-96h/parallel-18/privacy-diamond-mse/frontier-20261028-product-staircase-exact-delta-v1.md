# Exact approximate-privacy defect of 1D-staircase products

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:10:22 PDT 2026`.

## 1. Source-independent exact finite privacy profile

Fix any epsilon>0, `b=e^(-epsilon)`, `m=b/(1-b)` and gamma in (0,1]. Let nu_gamma be the ACTUAL symmetric 1D staircase with density proportional to `b^(max(0,ceil(|x|-gamma)))`, and let `Q=nu_gamma tensor nu_gamma`. Define its exact privacy-defect function for the ORIGINAL closed l1-unit diamond D:

    delta_Q(epsilon)=sup_(h in D) sup_(Borel A)[Q(A)-e^epsilon Q(A+h)].   (1)

The written exact formula is

    delta_Q(epsilon)=(1-b) [min(1/2,2gamma)+m/2]^2
                           /[4(gamma+m)^2].                               (2)

The supremum is attained by shifts with `|h1|=|h2|=1/2`; the maximizing event is the product of the two 1D likelihood-ratio b^(-1) regions. Thus Q is exactly `(epsilon,delta_Q)`-private with respect to full D, but is NOT pure epsilon-private. Here delta is a privacy defect, not a statement about scientific approximation or a source theorem.

For EVERY actual pure-epsilon full-D-private Borel law mu, this gives the stronger-than-one-jump TV separation

    TV(mu,Q) >= [b/(1+b)]delta_Q(epsilon)
       = b(1-b)/(1+b) [min(1/2,2gamma)+m/2]^2/[4(gamma+m)^2].           (3)

Both (2) and (3) are source-independent finite-epsilon claims for ANY gamma; no optimizer interpretation is assumed.

## 2. One-dimensional maximum-likelihood regions

The 1D normalization is `Z1=2(gamma+m)`. For a positive shift h in [0,1], 1D privacy makes `p(x)/p(x+h)` one of b^(-1),1,b. Let a(h) be the P-mass of the ratio-b^(-1) region. On the positive axis, each boundary gamma+n, n>=1, contributes length h at density proportional to b^n. At the first boundary gamma, the central high-density contribution has total length `min(h,2gamma)`, including the possible piece crossing 0. Therefore

    a(h)=[min(h,2gamma)+m h]/[2(gamma+m)].                               (4)

For negative shifts symmetry gives the same a(|h|). At gamma=1 or h=1, endpoint overlaps are null and the formula remains valid.

## 3. Product hockey-stick divergence and exact maximizer

For any h in D, each |h_i|<=1. The product density likelihood ratio is at most b^(-2). It exceeds the allowed b^(-1) EXACTLY where BOTH coordinate ratios equal b^(-1); there the shifted product density equals b^2 times the original. The Neyman–Pearson positive-part identity therefore gives

    sup_A[Q(A)-b^(-1)Q(A+h)]
       =(1-b)a(|h1|)a(|h2|).                                             (5)

The function a is nonnegative, increasing and concave. For |h1|+|h2|<=1, AM–GM and concavity bound their product by `a(1/2)^2`; equality holds at equal half shifts. Substitution gives (2).

If mu is pure-epsilon private, its corresponding signed difference is <=0. For any A,h, comparing the two measures bounds the difference by `(1+b^(-1))TV(mu,Q)`. Taking the maximizing A,h and rearranging proves (3).

## 4. Exact original-marginal instance and asymptotic scale

If the unreviewed 1D optimizer candidate `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`, is valid, then at epsilon=ln 2 the individually squared-optimal 1D gamma is `3^(1/3)-1>1/4`. Formula (2) becomes

    delta_Q(ln 2)=1/[8*3^(2/3)],
    TV(mu,Q)>=1/[24*3^(2/3)]>1/50.                                      (6)

The last strict rational comparison follows from `(25/12)^3>9`. The 1D-optimum interpretation is conditional on cde9, while (2)–(3) require no research import.

As epsilon->0, if gamma->1/2 (in particular for every 1D mixed-cost-optimal gamma from cde9, uniformly in arbitrary nonnegative kappa), (2)–(3) yield the following. For the uniform selector assertion, its strictly increasing mixed cubic has its root between the pure-mean and pure-squared roots, which tend to 1/2.

    delta_Q(epsilon)~epsilon/16,
    inf_(mu pure full-D private) TV(mu,Q) >=(epsilon/32)[1+o(1)].         (7)

This epsilon/32 obstruction is stronger than the epsilon^3/32 lower bound obtained by considering only the first staircase jump in the earlier unreviewed 8f4c candidate. It remains compatible with qualitative TV convergence to product Laplace, whose rate is also O(epsilon).

## 5. Status

Equations (1)–(7) are written exact probability/geometry arguments, not formal or independently reviewed proofs. The high-privacy optimal-gamma interpretation names its unreviewed 1D input explicitly; no novelty, source equivalence or parent acceptance is claimed. Suggested review: the first-boundary central crossing in (4), product likelihood-ratio cases, and the AM–GM maximization over all shifts.
