# Sharp asymptotic TV repair within the entire radial class

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:14:23 PDT 2026`.

## 1. Source-independent radial optimum

Let Q_gamma be the product of two 1D epsilon-private symmetric staircases with ANY gamma=gamma(epsilon) in [0,1]. Q_gamma is an auxiliary product, not in general 2D full-D private. Let Rad be ALL 2D laws with a density of the form rho(||x||_1), with no privacy restriction on rho. As epsilon->0, uniformly in gamma,

    inf_(P in Rad) TV(Q_gamma,P)=epsilon/8+O(epsilon^2).                 (1)

The same asymptotic holds when the infimum is restricted to ACTUAL full-D pure-epsilon-private radial laws. The upper law is the explicit full-D-private diamond staircase with `eta=2gamma-1/2 (mod 1)` from the preceding construction; the lower bound in §2 applies to the WHOLE radial-density class, not only to staircases or private laws.

This does NOT prove epsilon/8 is the optimum over all nonradial private laws. The separately pinned unreviewed privacy-defect lower remains epsilon/32 for gamma->1/2.

## 2. Angular-median lower bound without assuming radial privacy

Use the actual product Laplace Lambda_epsilon as a positive reference, with radial variable r=||x||_1. In each quadrant, fix r and parameterize x1 in [0,r], x2=r-x1; the Jacobian is 1. Under Lambda_epsilon the conditional x1 is uniform on [0,r], and r has density `epsilon^2 r e^(-epsilon r)`.

Outside the coordinate core pieces x1<gamma or x2<gamma, set

    theta_i={x_i-gamma},   phi={r-2gamma}={theta_1+theta_2}.

Uniformly in gamma and x,

    dQ_gamma/dLambda_epsilon
      =1+epsilon(theta_1+theta_2-1)+O(epsilon^2).                         (2)

As x1 ranges over [0,r], the theta_1 phase is uniform up to a discrepancy O(1/r), and the two coordinate cores have total conditional length at most 2. For fixed phi, the sum S=theta_1+theta_2 is phi on a phase set of length phi and 1+phi on one of length 1-phi. Thus the two leading values of `S-1` are `phi-1` and `phi`, with respective weights phi and 1-phi.

For ANY radial comparator density rho(r), its ratio to the reference is a SINGLE constant along this level set. The L1 distance from two points a<b with weights p,1-p to any constant is at least `min(p,1-p)(b-a)`. Applying this angular median inequality, ignoring the central pieces and accounting for O(1/r) phase discrepancy and the O(epsilon^2) ratio error, yields for r>=2

    average_angle |dQ_gamma/dLambda_epsilon-rho(r)/lambda(r)|
       >= epsilon min(phi,1-phi) - O(epsilon/r+epsilon^2).                (3)

This bound is uniform even if rho(r)/lambda(r) is arbitrarily large. Since `E_Lambda[1/r]=epsilon`, and periodization of `epsilon^2 r e^(-epsilon r)` gives phi uniform to O(epsilon), integrate (3) and divide by 2:

    TV(Q_gamma,P) >= (epsilon/2) integral_0^1 min(phi,1-phi)dphi
                       -O(epsilon^2)
                     =epsilon/8-O(epsilon^2).                            (4)

The discarded region r<2 has Lambda mass O(epsilon^2) and cannot invalidate this nonnegative lower bound. For the matching upper take the actual full-D-private radial staircase P_eta with `eta=2gamma-1/2 (mod 1)`. Its density/reference first-order phase is `{theta_1+theta_2+1/2}-1/2`. Thus the product-minus-radial first-order phase is `floor(theta_1+theta_2+1/2)-1`. Under the independent uniform limiting phases this has absolute value 1 with total probability 1/4, and 0 otherwise. The finite phase-periodization error is O(epsilon), while all central regions have reference mass O(epsilon) and ratio error O(epsilon); therefore `TV(Q_gamma,P_eta)=epsilon/8+O(epsilon^2)`. This directly proves (1) and the private-radial assertion.

## 3. Separately conditional comparison with the actual cost optimizers

Let gamma_1D,J and gamma_1D,L be the exact scalar optimal offsets from unreviewed `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`. Let eta_2D,J and eta_2D,L be the actual full-D squared-Euclidean and first-norm optimal staircase offsets on the small-epsilon diamond branch, conditional on parent v253 SHA `a32085f921269874b24821146d7af820451ac48b844288887805c75042e7e71d`, parent MDA SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, and unreviewed `frontier-20261028-high-privacy-selector-tradeoff-v1.md`, SHA-256 `aa45831697246a418364e72eedc4345e11afb1a988076ac730a204c8fd9617b7`. Those inputs give `gamma_1D,*=1/2+O(epsilon)` and `eta_2D,*=g+O(epsilon)`, `g=(3+sqrt(3))/6`.

Using the explicit phase formula of unreviewed `frontier-20261028-radial-repair-tv-asymptotic-v1.md`, SHA-256 `b139fd3cac818da2ea2539923efa5f4a2f66458d7e287a625412b4b16843ea1f`, their distance satisfies

    TV(Q_(gamma_1D,*),P_(eta_2D,*))
      = [1/8+sqrt(3)/18]epsilon+O(epsilon^2),                             (5)

for either * in {J,L}. Indeed `c={2gamma_1D-eta_2D}=1-g+O(epsilon)` and the phase expectation there is `1/4+sqrt(3)/9`. Equation (5) is explicitly conditional on the named optimizer/phase inputs, not a freestanding source claim.

## 4. Status

The whole-radial lower argument and (1) are written source-independent geometry plus an explicit true private upper law; no 2D optimizer theorem is imported for (1). The optional actual-optimizer comparison (5) has the named unreviewed/parent dependencies. No numerical, formal, independent review, novelty, full-class nearest-TV solution or parent acceptance is claimed. Suggested review: angular coordinate Jacobian, unconditional median bound with unrestricted rho, periodization uniform in gamma and endpoint errors.
