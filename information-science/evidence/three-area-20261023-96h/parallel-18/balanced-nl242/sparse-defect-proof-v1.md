# A mod-three sparse-defect obstruction across all surviving residue types

Observed before creation: **2026-10-23T14:11:38-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN PROOF**: no separate reconstruction, executable check, formal proof or novelty clearance yet. This is an additional necessary condition, not a balanced242 truth table or an unrestricted nonexistence proof.

## Claim and exact delta

Under the canonical odd-half hypotheses below, if the polar rank of `D` is any of `2,4,6,8`, then

`a := #{u: |S(u)| in {4,12}} >= 4`.                         (C)

Consequently, using the already reviewed reduction excluding polar rank zero, **every balanced nine-variable peak-at-most28 target must have at least four Walsh coefficients of magnitude4 or12**. Those coefficients are in the odd sector `s-perp`'s complement, where `s` is its nonzero support XOR.

This applies across all seven surviving residue types, without fixing either half, a zero set, a residue lift or an invariant class. It excludes no entire additional type. In particular a=4 and larger remain unhandled. The proof's contribution in this packet is spatial S-side compatibility, not another scalar histogram. The lower bound and its method have not been cleared against the full literature; do not call it a discovery.

## 1. Canonical setting and trusted boundary

All functions here have domain `V=F_2^8`, size256. Set

`H v(x) = sum_{u in V} v(u) (-1)^(u.x)`, so `H^2=256 I`.

For the two odd halves use their canonical Walsh spectra `K_g,K_h`, each congruent to2 modulo8 and satisfying `H K_g, H K_h in {+256,-256}` pointwise. Put

`S=K_g+K_h`, `R=K_g-K_h`, `p=R/8`,

`D=((K_g^2-4)/32)+((K_h^2-4)/32) mod2`.

The cap `|G|+|H_half|<=28` implies `|S|,|R|<=28`. The elementary canonical residue identity gives

`S = 4+8D (mod16)`, and `D` is quadratic.

Indeed write `K_i=2+8j_i`; then `(K_i^2-4)/32=j_i mod2`, and sum. The canonical-sign lemma and quadratic-residue lemma are proved in the existing `hard-continuation-20261015/proof.md` §§2,4, and attributed there to Wang–Lou–Wang. The new argument imports neither the unreviewed round2 type claims nor the rank4 zero-geometry exclusion, Pfaffian lemmas or finite certificates.

Write `chi_D(u)=(-1)^D(u)` and `T=chi_D S`. The last congruence and the cap give exactly

`T(u) in {-28,-12,4,20}`.                                  (1)

Let `A={u:T(u) in {-12,4}}`, so `|A|=a`. Define the signed defect

- `delta(u)=chi_D(u)` when `T(u)=-12`;
- `delta(u)=-chi_D(u)` when `T(u)=4`;
- `delta(u)=0` otherwise.

Thus `supp(delta)=A` and every nonzero value is ±1. Checking the four symbolic alternatives in (1) yields the exact congruence

`S = -chi_D + delta (mod3)`.                               (2)

There is no probabilistic or approximate reduction here.

## 2. Ternary Fourier rigidity

Since `H K_g,H K_h` are ±256, put `b=(H S)/512`. It takes only `0,+1,-1`. Let `phi:Z -> {0,+1,-1}` be the unique representative of an integer modulo3. Because `512=-1 mod3`, equation (2) determines **the entire signed transform**, not just its support:

`b(x)=phi(W_D(x)-(H delta)(x))`,

`S=2 H b`,                                                (3)

where `W_D=H chi_D`.

For polar rank `2t`, `1<=t<=4`, the quadratic spectrum is supported on an affine `2t`-space `U` and has nonzero magnitude `beta=2^(8-t)`. Since `beta=(-1)^t mod3`, set

`Q=(-1)^t W_D/beta`.

Then `Q in {0,+1,-1}`, `Q=W_D mod3`, and

`H Q=(-1)^t 2^t chi_D`, `Q^2=1_U`.                         (4)

Let `R_D=rad(B_D)`, dimension `8-2t`, where `B_D` is the polar form. If `U=x_0+R_D-perp`, character summation gives

`H(Q^2)(y)=2^(2t)(-1)^(x_0.y) 1_{R_D}(y)`.                (5)

This includes balanced quadratics with nonzero radical-linear term: `U` need not pass through0. Modulating `Q^2` by the character at `u` translates this support to `u+R_D`.

**Why this matters:** scalar count profiles do not determine the sign/location of `H S`. Equation (3) does, once the actual signed defect positions and `D` are fixed. No count relaxation can replace that coordinate coupling.

## 3. Exact formulas for at most three defects

Suppose `A={u_1,...,u_k}`, all distinct, with `k<=3`, and write `delta=sum_i epsilon_i 1_{u_i}`, `epsilon_i in {±1}`. In transform coordinates let `d_i(x)=epsilon_i(-1)^(u_i.x)`. Then

`b=phi(Q-sum_i d_i)`.

For `Q in {0,±1}`, `phi(Q)=Q` and `cos(2 pi Q/3)=1-(3/2)Q^2`. For every integer `n`, `phi(n)=(2/sqrt(3))sin(2 pi n/3)`. Multiplying the sine/cosine addition formulas, using `cos(2 pi d_i/3)=-1/2` and `sin(2 pi d_i/3)=(sqrt(3)/2)d_i`, gives the exact rational polynomials

- k=0: `b=Q`;
- k=1: `b=-(Q+(2-3Q^2)d_1)/2`;
- k=2: `b=(Q(1-3d_1d_2)+(2-3Q^2)(d_1+d_2))/4`;
- k=3: `b=(-Q+3Q(d_1d_2+d_1d_3+d_2d_3)-(2-3Q^2)(d_1+d_2+d_3-3d_1d_2d_3))/8`.

These identities are derived algebraically, not inferred from finitely many program evaluations.

Define the exceptional union

`E_k = union_{I subset {1,...,k}, |I| odd} ((sum_{i in I}u_i)+R_D)`.

For k=1,2,3 its size is at most respectively `1,2,4` times `2^(8-2t)`. It contains every defect point. Outside `E_k`, all transforms of the `Q^2` terms vanish by (5), and the transforms of the bare character terms vanish as well. Applying `S=2H b` and (4) gives

- k=1: `S(y)=(-1)^(t+1)2^t chi_D(y)`;
- k=2: `S(y)=(-1)^t2^(t-1)[chi_D(y)-3epsilon_1epsilon_2 chi_D(y+u_1+u_2)]`;
- k=3: `S(y)=(-1)^t2^(t-2)[-chi_D(y)+3 sum_{i<j}epsilon_i epsilon_j chi_D(y+u_i+u_j)]`.

Every such y is outside A, and so must have `|S(y)| in {20,28}`. This necessary condition will contradict the formulas.

## 4. Excluding k=0,1,2

For k=0, equations (3)–(4) make `|S|` constantly `2^(t+1)`, one of4,8,16,32, never20 or28. Thus k=0 is impossible.

For k=1, `E_1` has at most64 points, so its complement is nonempty. On it `|S|=2^t`, never20 or28. Thus k=1 is impossible.

For k=2, `E_2` has at most128 points. On its nonempty complement the second formula gives `|S| in {2^t,2^(t+1)}`, again never20 or28. Thus k=2 is impossible.

## 5. Excluding k=3 at every positive polar rank

The absolute value of the bracket in the k=3 formula is one of `2,4,8,10`: it is a sign with coefficient−1 plus three signs with coefficient3.

### Polar ranks4 and8

For t=2, `|E_3|<=64`; outside it `|S| in {2,4,8,10}`. For t=4, `|E_3|<=4`; outside it `|S| in {8,16,32,40}`. Neither set contains20 or28. Both cases are impossible.

### Polar rank6

For t=3, at least240 points are outside `E_3`. Their permitted value20 requires the bracket to have absolute value10, so all three ratios

`L_ij(y)=epsilon_i epsilon_j chi_D(y+u_i+u_j)/chi_D(y)`

must equal−1. Put `v=u_1+u_2`, `w=u_1+u_3`; the third shift is `v+w`. Quadratic polarization gives

`L_12(y)L_13(y)L_23(y)=(-1)^B_D(v,w)`.

Thus all three can equal−1 only if `B_D(v,w)=1`. In that case `B_D(y,v)` and `B_D(y,w)` are independent linear forms: evaluate any dependence on v and w to see both coefficients vanish. The conditions on the first two ratios therefore hold at exactly64 points. If `B_D(v,w)=0`, no point qualifies. Neither possibility can cover the required at least240 points. Contradiction.

### Polar rank2

Here `|R_D|=64`. If the four odd-subset sums `u_1,u_2,u_3,u_1+u_2+u_3` do not represent all four distinct cosets of `R_D`, there is a point outside `E_3`. The formula there has absolute value in `{1,2,4,5}`, impossible.

If they represent all four distinct cosets, inspect the full k=3 polynomial. Its `Q` part contributes a function of absolute value at most5 everywhere, by the same bracket bound. Outside the four literal odd-subset-sum points, the transforms of the bare characters vanish. Exactly one `Q^2` term remains, since its four supports are the four distinct radical cosets. By (5) its transform has magnitude4; its coefficient in S is either `3/4` or `-9/4`. Thus `|S|<=5+9=14` at every one of those at least252 points. They are outside A, which requires20 or28. Contradiction.

All four positive polar ranks have now been handled. This proves (C).

## 6. Bridge to the literal nine-variable target

The existing elementary balanced reduction shows that a target has nonzero support XOR s. Choose a normal v with `v.s=1`, split on `ker(v)` using coset origin s and any explicit basis B. Both halves have odd weight. Their support XORs agree and their canonical phases are opposite. The precise corrected map, already recorded in `zero-geometry/PROOF.md` §1, is

`R(b)=eta(b) W_f(a)`, `S(b)=eta(b) W_f(a+v)`,

where `a in s-perp`, `b=B^T a`, and v is **this split's specific normal**, not an arbitrary neighboring vector. Thus `A` corresponds bijectively to every Walsh coefficient in the complementary sector with magnitude4 or12. There are no coefficients of these magnitudes on `s-perp`.

The reviewed `quadratic-distance/SHARPER.md` inequality and `D(0)=0` exclude polar rank zero and leave exactly positive ranks2,4,6,8. Consequently (C) applies to every target, including all seven unexcluded types. The old rank4/weight128 exclusion is not needed to prove this statement.

## 7. Scope, checks and actual stopping point

- **Correctness level:** author-written complete argument, not yet separately reconstructed or accepted. All steps are written; no scientific code or finite point test was executed.
- **Imports:** elementary canonical-spectrum/quadratic-normal-form facts and the reviewed positive-rank reduction only. No use of the unrestricted242 upper-bound preprints, unreviewed round2 claims, old solver statuses or unavailable classification.
- **Scope:** a>=4 is a universal necessary condition, not a truth table, a new residue-type exclusion, or proof of global nonexistence.
- **Novelty/significance:** unclear priority; modest structural filter unless it combines with a further obstruction. Search misses do not clear novelty.
- **Remaining mathematical ingredient:** at four signed defects the interpolation has additional even-subset character terms and can produce20/28 away from its exceptional supports; the small-defect contradiction above does not extend automatically. The complete S-side coordinates from (3), and the still-complementary R realization, must be handled. No claim that a>=4 alone improves the balanced maximum.

The separate modular-saturation protocol freezes an unrestricted constructive/verification criterion. Any executable application requires a source/input-pinned parent GO. This manuscript is immutable; repairs must be numbered addenda or a new version.
