# The low-privacy TV repair has a genuine b^(3/2) correction

**AUTHOR CANDIDATE — WRITTEN with explicitly scoped exact rational checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:30:36 PDT 2026`.

## 1. Written source-independent claim

Let Q be the product of the two symmetric 1D half-offset epsilon-private staircases, `b=e^(-epsilon)`, and let `T_*(b)` be its nearest TV distance to ALL original FULL closed-D pure-epsilon-private 2D Borel laws. There exist absolute constants and sufficiently small b such that

    2b-16b^(3/2)-O(b^2 |log b|) <= T_*(b)
       <= 2b-4b^(3/2)+O(b^(7/4)).                                       (1)

In particular `2b-T_*(b)=Theta(b^(3/2))`. The actual private upper law is a diamond-shell staircase with a CLIPPED SQUARE core; the finite explicit lower is rederived below. This is sharper than a mere `2b+O(b^(3/2))` statement. It does NOT determine the exact b^(3/2) coefficient, finite-b nearest law, novelty or any original J optimizer.

## 2. Explicit true-private clipped-square law

Let `S=[-1/2,1/2]^2` and for 0<t<1/2 define

    K_t=S intersect {||x||_1<=1-t}.

Its area is `A=1-2t^2`. For k>=0 the exact Minkowski area is

    |K_t+kD|=A+(4-4t)k+2k^2.                                             (2)

Indeed the four shortened axis edges contribute `4(1-2t)` to the D-mixed perimeter, and the four diagonal clipping edges contribute 4t. The actual full-D-private shell density `p_t=b^(min{k:x in K_t+kD})/Z_t` therefore has

    Z_t=A+(6-4t)m+4m^2,   m=b/(1-b).                                    (3)

Inside S, points of K_t have shell index 0 and the clipped corners shell index 1. Thus

    P_t(S)=[A+b(1-A)]/Z_t,
    Q(S)=[(1-b)/(1+b)]^2.                                                 (4)

## 3. TV upper and a real negative b^(3/2) term

Choose `t=(1-b^(1/4))sqrt(b)`. Then t<=sqrt(b), and direct expansion gives `Q`'s core density q0 times Z_t equal to `1+4b^(5/4)+O(b^(3/2))>1`. Hence q>=p_t everywhere on S for all small b. Outside S, the positive part `(q-p_t)_+` has total mass O(b^2), uniformly for t<=sqrt(b):

* On Q's one-coordinate first-shell strips inside K_t+D, both densities are b times `1+O(b)`.
* The parts of those strips outside K_t+D have total area at most 4t^2, contributing O(bt^2)=O(b^2).
* Q's remaining outside mass has at least two geometric index units and is O(b^2).

For the second bullet, on the right strip write x1=1/2+a and x2=sign(x2)(1/2-u). If u<t, a core point can be chosen at inward horizontal distance t-u, so exclusion from K_t+D requires a>1-(t-u); integrating u from 0 to t over the eight strip ends gives total area at most 4t^2.

Therefore

    TV(Q,P_t) <=Q(S)-P_t(S)+O(b^2)
              =2b-4bt+O(b^2)
              =2b-4b^(3/2)+O(b^(7/4)).                                  (5)

All O constants are absolute in the stated choice; P_t is a genuine private law.

## 4. Re-derived lower at the same correction scale

For any full-D-private mu with T=TV(mu,Q), q0=`[(1-b)/(1+b)]^2`, and any 0<delta<1, let K_delta be the four triangles outside S with corner coordinates a,c>0 and a+c<1-delta. Its area is `2(1-delta)^2` and Q density there is b^2 q0. For y in a triangle, its exact unit-D overlap with S is a corner triangle C_y of area `(1-a-c)^2/2`. Pointwise privacy plus the TV definition gives

    f_mu(y)>=b[q0-2T/(1-a-c)^2].

Integrating four quadrants and rearranging yields

    T >= 2b(1-b)q0(1-delta)^2 /
           [1+8b(1/delta+log(delta)-1)].                                 (6)

At delta=2sqrt(b), expansion gives the lower side of (1), with the stated `O(b^2 |log b|)` error. Comparing with the actual upper (5) proves the Theta conclusion.

## 5. Actual checks and limitations

The Python eval kernel used `fractions.Fraction` at b=1/10000,t=9/1000 and b=1/10^8,t=99/10^6 to check (3)–(4), the sign `q0 Z_t>1`, and the order of the core-deficit remainder. It did NOT integrate the full TV or verify the asymptotic proof. All geometric/variational claims are WRITTEN source-independent arguments, not formal or independent review, novelty or parent acceptance. Review should examine mixed perimeter (2), strip-exclusion area, the use of signed TV on S, and uniform remainder estimates.
