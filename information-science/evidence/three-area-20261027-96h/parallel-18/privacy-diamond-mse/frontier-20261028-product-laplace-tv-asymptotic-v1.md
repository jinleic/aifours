# High-privacy distance of the 1D-staircase product to the private class

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:11:57 PDT 2026`.

## 1. Exact law comparison and original privacy distance

Let nu_gamma be the actual 1D symmetric epsilon-private staircase with gamma in [0,1], Q_gamma=nu_gamma tensor nu_gamma, and let Lambda_epsilon be the ACTUAL full-D-private product Laplace `(epsilon^2/4)e^(-epsilon||x||_1)`. As epsilon->0, uniformly for ANY gamma=gamma(epsilon) in [0,1], the source-independent written claim is

    TV(Q_gamma,Lambda_epsilon)=epsilon/6+O(epsilon^2).                    (1)

The product Q_gamma itself is generally NOT full-D pure-epsilon private; it is a comparator, not an asserted mechanism. Consequently its distance to the actual full-D-private class is at most the right side of (1).

If gamma->1/2, the separately pinned unreviewed exact privacy-defect candidate `frontier-20261028-product-staircase-exact-delta-v1.md`, SHA-256 `1f6b748298e994bed0392b1e9cfc15d4cd80f02920942b464d7ecbc1c39265eb`, gives the matching ORDER lower bound

    (epsilon/32)[1+o(1)] <= inf_(mu full-D epsilon-private)TV(mu,Q_gamma)
                            <=epsilon/6+O(epsilon^2).                     (2)

The lower coefficient is not claimed optimal. Under the separately unreviewed exact 1D optimizer result cde9, gamma->1/2 holds uniformly for arbitrary nonnegative mixed-cost weights. Thus (2) says the individually optimal marginal product is at a strictly linear-in-epsilon TV distance from the full-D-private class at high privacy, despite sharing the same limiting product-Laplace law.

## 2. Uniform expansion of each coordinate ratio

Put b=e^(-epsilon), m=b/(1-b). The exact 1D staircase normalizer is `2(gamma+m)`, and for r=|x| and `n=max(0,ceil(r-gamma))`,

    nu_gamma(x)/lambda_1(x) = A_1 e^(epsilon(r-n)),
    A_1=1/[epsilon(gamma+m)], lambda_1(x)=(epsilon/2)e^(-epsilon|x|).

Uniformly in gamma, `log A_1=(1/2-gamma)epsilon+O(epsilon^2)`. For r>=gamma put `v=ceil(r-gamma)-(r-gamma)` in [0,1). Then

    nu_gamma(x)/lambda_1(x)=1+epsilon(1/2-v)+O(epsilon^2),               (3)

uniformly in gamma and v. The central region r<gamma has Lambda_1 probability O(epsilon) and ratio difference O(epsilon), so contributes only O(epsilon^2) to L1.

## 3. Independent fractional shell phases

Under lambda_1, r=|X| has exponential density `w(r)=epsilon e^(-epsilon r)`. Comparing point samples with unit-interval integrals gives a periodization error at most `integral_0^infinity|w'(r)|dr=epsilon`, plus the omitted central O(epsilon) mass. Thus v is uniform on [0,1] up to O(epsilon), uniformly in gamma. For two independent coordinates their two phases are independent under Lambda_epsilon.

Away from either central region, (3) gives

    dQ_gamma/dLambda_epsilon -1
       =epsilon[(1/2-v_1)+(1/2-v_2)]+O(epsilon^2).                      (4)

The set where a coordinate is central has Lambda_epsilon mass O(epsilon), and there the density-ratio error is still O(epsilon), so it contributes O(epsilon^2). If W1,W2 are independent Uniform[-1/2,1/2], their sum has density `1-|w|` on [-1,1], hence `E|W1+W2|=1/3`. Taking one half of the L1 difference in (4) proves (1).

## 4. Status

Equations (1), (3)–(4) are written from the actual laws and elementary phase averaging, with no named research input. The lower side of (2) explicitly depends on the unreviewed 1f6b exact-defect theorem and the 1D-optimal interpretation separately depends on cde9. No numerical, formal, independent review, novelty or parent acceptance is claimed. Suggested review: uniform phase periodization, two central-region errors, and the coefficient E|W1+W2|/2=1/6.
