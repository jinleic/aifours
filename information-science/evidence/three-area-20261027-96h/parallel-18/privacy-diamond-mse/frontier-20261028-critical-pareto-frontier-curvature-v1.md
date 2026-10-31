# Complete finite-coordinate critical Pareto frontier and exact curvature

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:14:43 PDT 2026`.

## 1. Target and exact scope

Import the unreviewed all-law mixed-degree candidate `frontier-20261028-mean-euclidean-critical-crossover-v1.md`, SHA-256 `7de42660b59814a1802d2fdeec3ca0c0a6d69c845beaa1d9f3c083fd3cbbc53d`. Its peak-floor proof and its all-nearopt moment identities are REQUIRED here; the present note does not turn that candidate into an accepted theorem.

For b=e^(-epsilon)->0 set s=b^(1/4). Let J=E|X|_2^2 and L=E||X||_1 for the original full-D-private Borel laws. Consider all FINITE pairs `(u,v)` that arise as actual limits

    J/s^2 ->u,      L/s ->v.                                             (1)

Pareto order means componentwise <=, with at least one strict inequality. This note describes the complete Pareto-efficient subset of those limiting pairs. It does NOT claim an exact finite-epsilon frontier or a novelty result.

Define T_theta for theta>=0 by the unique root

    integral [T_theta-|z|_2^2-theta||z||_1]_+ dz=2/3,
    K_theta={|z|_2^2+theta||z||_1<=T_theta},
    A_theta=|K_theta|,    V_theta=T'_theta.                              (2)

The entire finite-coordinate efficient frontier is precisely

    (u_theta,v_theta)=(T_theta-theta T'_theta, T'_theta),  theta>=0.      (3)

Its v-coordinate decreases strictly from `v0=8R0/(3pi)` to 0, where `R0=(4/(3pi))^(1/4)`; the limit v=0 is NOT a finite-coordinate attainable point. Every point (3) is realized by actual full-D private shell laws. Any finite-coordinate attainable point off (3) is dominated by an actual point of (3).

## 2. Smoothness and strict concavity of the threshold

Put `c_theta(z)=|z|^2+theta||z||_1` and `G(T,theta)=integral(T-c_theta)_+`. Equation (2) gives `G_T=A_theta>0`. Its radial boundary in each quadrant is smooth with positive radial derivative, and axis intersections are a finite null set. Differentiation under the integral and the implicit function theorem therefore give

    T'_theta = [integral_(K_theta)||z||_1 dz]/A_theta >0.                 (4)

For finite theta>=0, a second differentiation along the moving boundary gives

    T''_theta = -(1/A_theta) integral_(partial K_theta)
                       [||z||_1-T'_theta]^2/|grad c_theta(z)| dS.         (5)

At theta=0 interpret this as the right derivative. This is STRICTLY negative: the l1 norm is not constant on the boundary of K_theta. Indeed, equality of its axis and diagonal l1 radii would give the same l1 norm but two different positive squared Euclidean norms, contradicting the shared level `c_theta=T_theta`. Thus T is strictly increasing and strictly concave, and V_theta strictly decreases.

The earlier candidate establishes the separate iterated limit `T_theta/theta^(2/3)->1` as theta->infinity. Concavity bounds T'_theta between secant slopes on `[theta/h,theta]` and `[theta,h theta]` for any h>1. Taking theta->infinity then h->1 yields

    T'_theta ~ (2/3)theta^(-1/3),
    u_theta=T_theta-theta T'_theta ~ (1/3)theta^(2/3).                  (6)

Hence v_theta->0 and `u_theta v_theta^2->4/27`. These are ITERATED theta limits of the critical frontier, not a claim about arbitrary joint theta(b)->infinity; the latter has its own separately pinned candidate.

## 3. Why this is the COMPLETE limiting efficient set

For ANY feasible sequence with finite limiting pair (u,v), scalarization by each fixed theta>=0 and the imported all-law leading lower bound imply

    u+theta v >= T_theta.                                                (7)

The imported explicit actual shell law with core sK_theta achieves the leading mixed value. Its all-nearopt component formulas give `L/s->T'_theta` and `J/s^2->T_theta-theta T'_theta`. Thus EVERY point (3) is actually realized, including theta=0.

No finite-coordinate feasible limit has v=0. To see this directly, let M be the essential density peak. The all-event full-D condition implies the translated bM density floor; integrating |x|^2 on the translate gives `J >= (2/3)b M`. Thus the scaled density of X/s has cap `s^2 M <= (3/2)J/s^2`. If J/s^2<=U<infinity, the l1 bathtub for a probability density with that cap yields

    L/s >= 2/[3 sqrt(3U)] >0.                                            (8)

For any 0<v<=v0 there is a UNIQUE theta>=0 with T'_theta=v, by strict monotonicity and (6). Equation (7) gives `u>=T_theta-theta v=u_theta`. The realizable frontier point with the SAME v therefore dominates all points with a larger u. If v>v0, (7) with theta=0 gives u>=u0; the realizable endpoint (u0,v0) dominates it. Each point (3) is itself efficient: its unique supporting positive weight makes any strict componentwise improvement violate (7); the theta=0 endpoint is protected by taking theta->0 in (7). This proves completeness for exactly the finite limit set (1).

## 4. Exact local target-end curvature

At theta=0, `K_0=R0 B2`, `T0=R0^2=2/sqrt(3pi)`, and

    v0=T'_0=8R0/(3pi).

On the boundary, `||z||_1=R0 a(phi)`, `a=|cos phi|+|sin phi|`, and `dS/|grad c_0|=dphi/2`. The exact integrals are

    integral_0^(2pi) a dphi=8,   integral_0^(2pi) a^2 dphi=2pi+4.

Substitution in (5) gives

    T''_0 = -k,   k=1+2/pi-128/(9pi^2)>0.                              (9)

Positivity follows from the nonzero variance integral (5), not from a floating computation. Thus near the original squared-Euclidean endpoint,

    v_theta=v0-k theta+o(theta),
    u_theta=u0+(k/2)theta^2+o(theta^2),
    u-u0=(v0-v)^2/(2k)+o((v0-v)^2)                                  (10)

along the efficient frontier. More generally `du/dv=-theta` and `d^2u/dv^2=-1/T''_theta>0`, so this frontier is strictly convex as a graph over 0<v<v0. This yields the local cost of improving mean error while preserving the actual full-D privacy model, not a claim about a finite-b optimizer family.

## 5. What was actually checked

An attempted import of SymPy in the Python eval kernel failed with `ModuleNotFoundError`; it was not installed or used. A subsequent bounded check used `fractions.Fraction` for the rational coefficient 128/9 and `math.pi` only as a FLOAT diagnostic, obtaining `k≈0.19560738278766654`. It is not an interval bound. The exact formula, strict sign, all-law inequalities and Pareto statements are written arguments conditional on 7de42660; they were not kernel/formally proved, independently reviewed, cross-vendor reviewed or parent-adopted. No source-equivalence, priority, global non-equivalence or publication claim is made.
