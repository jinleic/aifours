# Untrusted candidate: sharp order for the three-pole all-pole PH family

This is a proof candidate from the read-only screen plus parent hand derivation, not an accepted result. It must be independently derived, falsified and reviewed. No numerical experiment establishes its all-real/all-n claims. Scope is the frozen Commault–Mocanu Conjecture1 special family, not the book's general PH-minimization question.

## Normalize time

Let delta=a−c>0, A=a/delta, C=c/delta=A−1>0 and beta=b/delta>0. Work first at delta=1; recover original time by multiplying the eventual generator by delta. With x=s+A, the target is

    F(s)=K/[(x−1)(x²+beta²)],   K=C(A²+beta²).

The spectral lower bound is imported separately; its applicability to representations with unobservable/unreachable states must be justified.

For n=n_min≥4, beta lies in (cot(pi/(n−1)),cot(pi/n)]. Put phi=arctan(beta), psi=pi−2phi. Then

    2pi/n ≤ psi < 2pi/(n−1).

Let S=2pi−(n−3)psi, so 2psi<S≤3psi. Seek three angles with sumS and n−3 remaining angles equalpsi.

## One scalar intermediate-value problem

Take theta1=t, theta2=theta3=(S−t)/2, t∈[0,S/3], and

    G(t)=sin(t+phi)*sin((S−t)/2+phi)²−sin(phi)³.

Candidate sign argument: G(0)<0 since S>2psi and phi+S/2 lies between pi−phi andpi. G(S/3)≥0 since S≤3psi. For n≥4, S/2≤pi−phi, so a root t∈(0,S/3] puts every theta_i strictly in(0,pi−phi). At the upper spectral boundary use t=S/3. Check these inequalities carefully, including n4 and exact band endpoints.

Set theta4=...=theta_n=psi and m_i=−beta*cot(theta_i). Then m_i<1. Let

    W=product_i(1−m_i)>0,
    Q(x)=product_i(x−m_i),
    q(x)=Q(x)−W.

Since sumtheta_i=2pi and product sin(theta_i+phi)=sin(phi)^n, the candidate identities are q(1)=q(i beta)=q(−i beta)=0. Hence

    P(x)=q(x)/[(x−1)(x²+beta²)]

is a real monic polynomial of degreen−3.

## Positivity of the cancelling numerator

Put m_*=(1−beta²)/2=−beta*cot(psi) and z=x−m_*. The last n−3 diagonal entries equalm_*. With

    h(x)=1/[(1−x)(x²+beta²)],

polynomial division/Taylor expansion gives

    P(x)=z^(n−3)+W*sum_{k=0}^{n−4} h^(k)(m_*)/k! * z^k.

This needs an exact derivation, not a numerical division. Let rho=(1+beta²)/2. The proposed generating-function identity is

    h(m_*+z)=rho^(−3)/[(1−z/rho)(1−2cos(psi)z/rho+(z/rho)²)].

Consequently its kth Taylor coefficient has the sign of

    cos(psi/2)−cos((k+3/2)psi),

with positive denominator2sin(psi/2)sin(psi). For0≤k≤n−4, the angle lies strictly between psi/2 and2pi−psi/2, since(n−2)psi<2pi. Thus all needed coefficients are positive. Verify every power, sign and range.

## A positive cyclic realization

Let M have diagonalm_i, superdiagonal weightsw1=...=w_(n−1)=1 and closing weightw_n=W>0. Its characteristic polynomial isq(x). The vector determined recursively by(1−m_i)u_i=w_i u_(i+1) is positive and has eigenvalue1, so a Metzler/Perron argument gives spectral abscissa1. Thus T0=M−AI is Hurwitz.

For row initialvectore1, the resolvent numerator with exitt has the form

    sum_{j=1}^n t_j*product_{k=j+1}^n(x−m_k)

because all partial forward weights are1. Take t1=t2=0, t3=K, and, forj≥4,

    t_j=K*W*h^(n−j)(m_*)/(n−j)!.

Then e1(xI−M)^(-1)t=K/[(x−1)(x²+beta²)]. Check orientation/cofactors and the n4 case explicitly.

Let v=−T0^(-1)t>0, D=diag(v), T=D^(-1)T0D, alpha=e1D. Then T1=−D^(-1)t≤0, T is Metzler/Hurwitz, and alpha1=F(0)=1. This gives a PH representation of ordern. In fact v1=1, so alpha=e1. Restore originaltime bydelta. All positivity/invertibility and lower-bound details must be proved; a finite sample is not enough.

## Controls to run before trusting it

- Reproduce the known n3 regime and an exact n4 family/polynomial identity.
- Check n4..12 in the interior and at upper band boundaries, including a value arbitrarily close to each lower endpoint: transform identity, all exits nonnegative, row sums, normalization and stability.
- A perturbed exit must alter the target transform. Above-thresholdbeta cannot have an ordern representation by the sector theorem, not because a root-finder fails.
- Boundary t=0 is NOT an admissible matrix: the construction needs a positive interior root except the upper-bound root at S/3.

No correctness, novelty or priority verdict follows from this candidate note.
