# H_{1,2}: all-topology obstruction to a six-state uniform-rate realization

Before-creation clock observed: **2026-10-23T13:51:15-07:00**. Status: **CANDIDATE / NOVELTY_UNCLEAR**, written reasoning only. This is a restricted but topology-universal lower bound within the SAME primary H_{1,2} target. It is stronger than the earlier failure of one fixed companion and does not solve unrestricted six-state feasibility. No scientific program or numerical check was run.

## 1. Exact theorem and distinction from the open unrestricted minimum

Let a>c>0,b>0,d=a-c,beta=b/d and

    H(s)=K/[(s+c)((s+a)^2+b^2)^2], K=c(a^2+b^2)^2.

Call a PH representation **uniform-rate** if every transient diagonal entry is the same -lambda. Off-diagonal topology, positive initial law and exit law are otherwise arbitrary; neither a companion nor a single-cycle shape is assumed.

**Candidate theorem U6.** H has no uniform-rate PH representation of six or fewer states when beta^2>1/2.

Consequently, on the newly constructed interval

    1/2<beta^2<=53/96,

the minimum **uniform-rate** PH order is exactly7: the G7 construction has constant diagonal, while U6 excludes all constant-diagonal six-state topologies and the algebraic-degree bound excludes lower orders. The unrestricted minimum remains6or7, because a nonuniform-diagonal six-state realization has NOT been excluded.

At the endpoint beta^2=1/2, every six-state uniform-rate representation must have

    lambda=a, hidden real pole u=c+2d,

and its off-diagonal graph has no directed2cycle or directed3cycle. The known six-state companion satisfies these necessary equalities and supplies an existence anchor.

## 2. Hidden-pole and trimming facts, stated without an imported minimality assumption

The nonzero constant numerator has reduced degree5. For any six-state representation,

    det(sI-T)=D5(s)(s+u)

with u real and positive by stability. Above beta^2=1/5, the already checked all-topology trace obstruction excludes every representation of five or fewer states. Thus any six-state representation in the region considered here has no unreachable state: deleting one would preserve H and leave at most five states. Every transient PH state can reach a positive exit; otherwise a final nonabsorbing communicating class would have eigenvalue0, contradicting Hurwitz stability.

Therefore the spectral abscissa cannot be a canceled mode to the right of-c. Explicitly, choose a diagonal irreducible block with maximal real eigenvalue rho. Reachability and exit co-reachability make the corresponding factors of alpha exp(Tt0) and exp(Tt0)w positive for every fixed t0>0. Restricting the intervening semigroup to paths remaining in that block and applying its positive Perron eigenvectors gives a lower bound C exp(rho t) on f(t+2t0) for large t. But the exact density of H is asymptotic to a positive constant times exp(-ct). Hence rho<=-c; because-c is a pole/eigenvalue, rho=-c. In particular u>=c.

This argument is independent of the equal-diagonal assumption and handles reducible or unobserved-noncritical modes. It does not assert that every eigenvalue must appear as a pole.

## 3. Zero-diagonal nonnegative matrix and its two walk traces

For a uniform-rate representation put

    C=T+lambda I.

It is an entrywise nonnegative matrix with zero diagonal. The characteristic trace of T gives

    6lambda=c+4a+u.

Set h=lambda-a. Since d=a-c, this is equivalently

    u-c=2d+6h.

The already justified u>=c therefore implies h>=-d/3. The six eigenvalues of C are

    d+h,
    -d-5h,
    h+ib twice, h-ib twice.

These identities keep the hidden real mode and both nonreal algebraic multiplicities; no diagonalizability is required.

Because C is nonnegative, tr(C^2)>=0 and tr(C^3)>=0: they are sums of positive closed-walk weights. Direct expansion gives

    tr(C^2)=2d^2+12dh+30h^2-4b^2,

    tr(C^3)=(d+h)^3-(d+5h)^3+4(h^3-3hb^2)
            =-12h[d^2+6dh+10h^2+b^2].

The bracket is strictly positive for every real h, since

    d^2+6dh+10h^2+b^2
      =10(h+3d/10)^2+d^2/10+b^2>0.

Thus tr(C^3)>=0 forces h<=0. We have now proved

    -d/3<=h<=0.

The trace-square condition yields

    b^2 <= d^2/2+3dh+(15/2)h^2
         =d^2/2+h(3d+(15/2)h).

On that interval, 3d+(15/2)h>=d/2>0 and h<=0, so the added term is nonpositive. Therefore

    b^2<=d^2/2.

This contradicts beta^2>1/2 and proves U6. It is an all-off-diagonal-topology inequality, not a companion coefficient test.

## 4. Endpoint equality and the exact restricted order7 consequence

If b^2=d^2/2, the last inequality is an equality only when h0, since the other factor remains strictly positive. Hence lambda=a and u=c+2d. The displayed trace formulas then give tr(C^2)=tr(C^3)=0.

With zero diagonal and nonnegative off-diagonal entries, tr(C^2)=sum_(i!=j)C_ij C_ji, so no directed2cycle can have positive weights. Likewise tr(C^3) is a sum of nonnegative three-edge closed-walk weights; with no self-loops these are exactly directed3cycles, and none can occur. This is necessary topology information, not an asserted classification of all endpoint graphs.

The separately written-checked G7 parameters have diagonal-lambda at every state, including the last one, and give H on beta^2 in[1/2,53/96]. Above1/2 they are therefore minimal within the uniform-rate class by U6. Their unrestricted order is still only bounded between6 and7. The endpoint1/2 already has the checked uniform-rate PH6 witness, so there is no false endpoint7 claim.

## 5. What this changes for the remaining all-topology problem

The old fixed six-state companion failed above1/2 because one feedback coefficient changed sign. U6 proves that **no six-state equal-holding-rate topology whatsoever** can repair that failure. Any unrestricted six-state exception above1/2 must have genuinely nonuniform diagonal rates, in addition to the irreducibility and one-extra-state layer constraints in the preceding L6 candidate.

The argument uses only trimming/positive Perron asymptotics, characteristic trace identities and nonnegative closed-walk traces, all classical mechanisms. Priority is not cleared, and the theorem must receive an independent written reconstruction before its status changes. It supplies no unrestricted minimum7, no generic minimum-order formula, no formal/kernel proof and no full-book resolution.

The next true obligation is the nonuniform-diagonal six-state class. A large hidden pole, arbitrary backward feedback or the one doubled layer cannot be dismissed by applying this uniform-rate proof after a non-diagonal similarity: a general similarity need not preserve entrywise positivity or equal holding rates.
