# Candidate addendum: closed optimal levels and backward plateau coupling

Observed clock before creation: **2026-10-23T16:20:55-0700**. Extends the frozen candidate `proof-coupled-level-tail-saturation-v1.md`, SHA-256 `ae1e05470b233d2e51a3c56f45a58ab97ecd249a5ed479dc33c6d29ae4ea3958`; original bytes are unchanged. **The complete operative mathematical packet needs both bodies and its own actual reconstruction. No inherited verdict. CANDIDATE / NOVELTY_UNCLEAR; no scientific execution or formal verification.**

This stays on the genuine all-law coupled-level obligation. It constructs feasible mass-lowering/filling/raising operations, not a new envelope constant or upper-core family. It does not compute V or claim that the resulting necessary conditions are sufficient.

## 1. Setup and exact additional claims

Use the base candidate's selected genuine unrestricted optimizer

`q=a b^n`, `J=V_b`, `E_k={n<=k}`, `K_k=ess-supp(1_(E_k)dx)`, `R=sqrt(J)`.

The base proves positive-area top plateau, compact K_k, exact support forcing and a.e. filling, and the genuine optimality sandwich

`K_k+D subset K_(k+1) subset (K_k+D) union B_R`.

**Additional claims (candidate):**

1. `K_0 subset B_R`.
2. Every `E_k=K_k` a.e. The same original optimal law therefore has an **upper-semicontinuous** geometric density version

`qhat(x)=a b^min{k:x in K_k}`

whose privacy ratio holds **pointwise for every x and every h in D**. That representative is derived from optimality, not assumed for arbitrary Borel laws.
3. With `K_(-1)=empty`, the backward coupled condition is

`lambda( ((K_(k+1) erosion D) intersect B_R) \ K_k )=0`, for every integer `k>=-1`,

where `K erosion D={x:x+D subset K}`. In particular `lambda(K_0 erosion D)=0`.
4. The base's coarse finite-head bound can be sharpened, as a dependent consequence, to

`L_J=ceil(2sqrt(2J)) <= ceil(4sqrt(2)/epsilon)`.

The cost ball is contained in `K_(L_J)` and all later levels are exactly forced Minkowski tails. This is a structural index bound, not a sampled epsilon threshold or a separate discovery count.

No prefix set is assumed convex, radial or symmetric. A closed level set need not be convex. No level0 single-core equality or finite-dimensional optimization claim follows.

## 2. Top-plateau mass outside the cost ball can really be lowered

Let `U=E_0 intersect {||x||_2^2>J}`. Lower q by the factor b on U and leave it unchanged elsewhere. Before normalization, this changes only index0 to index1.

For every arbitrary fixed h in D, discard the original null sets where the geometric index privacy bound fails. An original neighbor of a level0 point can only have index0 or1. Lowering one endpoint from0 to1 leaves the index difference at most1; if both endpoints are in U, both are lowered. Thus the altered density has full fixed-shift privacy. Its new mass z' is at least b>0 because it is everywhere at least bq.

The exact normalized cost change is

`J_new-J=-(1-b) integral_U (||x||^2-J)q(x)dx / z'`.

If U has positive area, this is strictly negative: q=a>0 on the top plateau and all the weight is above J. Optimality therefore makes U null. The closed cost ball contains E_0 a.e., so taking essential support proves

`K_0 subset B_R`.

This is an admissible finite mass change, not a first-variation sign and not a frozen-height-cap optimization.

## 3. Where holes in essential supports can lie

For k>=1, the base optimality sandwich gives

`K_k subset (K_(k-1)+D) union B_R`.

The base's full a.e. forcing gives `K_(k-1)+D subset E_k` a.e. Hence any hole `K_k\E_k` outside B_R is null. The same assertion for k0 follows from Section2. Removing a countable union of exceptions, **all holes at all levels lie only inside the cost ball**, up to a common null set.

This uses the nonconvex parallel-boundary/a.e.-filling result from the full base manuscript; it must not be replaced by a guessed simultaneous pointwise version of the original density inequalities.

## 4. Simultaneous support filling is a genuine all-level DP competitor

The K_k are nested and obey `K_k+D subset K_(k+1)`. Since K_0 is nonempty, their union is the entire plane: a fixed point c in K_0 has `c+kD subset K_k`, and these translates exhaust R². Thus

`m(x)=min{k>=0:x in K_k}`

is finite everywhere and Borel. Set `qhat(x)=a b^m(x)`.

Exact closed-set forcing gives `m(x+h)<=m(x)+1` for every x and every h in D. Applying -h yields the reverse. Hence qhat has the privacy ratio pointwise for **all** shifts and points, without taking any uncountable intersection of a.e. exceptions.

Because `E_k subset K_k` a.e. at every level, qhat>=q a.e. If qhat is strictly larger, the point lies in some hole `K_k\E_k`; Section3 confines that addition to B_R a.e. Also qhat<=a. The added density `rho=qhat-q` is therefore nonnegative, bounded and supported in B_R up to a null set. It has finite mass and finite moment. Its total new mass is

`z=1+integral rho`,

and the probability density qhat/z is genuinely feasible. Its exact cost difference is

`J(qhat/z)-J = integral_(B_R) (||x||^2-J)rho(x)dx / z <=0`.

If rho had positive mass, the inequality would be strict, because the circle `||x||²=J` has area0. That contradicts original optimality. Thus rho=0 a.e., z=1, and **qhat=q a.e.** Every hole is then null: at a hole of level k, qhat is at least `a b^k` while q is at most `a b^(k+1)`, so a positive-area hole would give positive added mass.

It follows that qhat's exact superlevel sets at the geometric heights are K_k. All positive superlevel sets are closed (indeed compact), so qhat is upper-semicontinuous and vanishes at infinity. It is a positive probability density with the same law and cost as the selected optimizer, and its full-DP ratio is pointwise. This is an existence/representation statement for an optimizer, not a regularity hypothesis imposed on the original all-law class or a claim about every feasible density.

## 5. A real raising operation supplies the backward coupled obstacle

Use this closed-level pointwise-private representative and set K_(-1)=empty. For any integer k>=-1 define the target height `h_k=a b^k` and

`U= ( (K_(k+1) erosion D) intersect B_R ) \ K_k`.

For k=-1 the target is a/b and the next set is K_0. On U, the old density is strictly below h_k. For every x in U and every h in D, its neighbor x+h lies in K_(k+1), so the old neighbor density is at least

`a b^(k+1)=b h_k`.

Raise the density on U to h_k and leave it unchanged elsewhere. Check every directed pair: if the endpoint was raised, its new height is controlled by the old b-height floor at every neighbor; if the endpoint was not raised, the old inequality remains valid because the other density only increased. The same argument in the reverse direction proves full pointwise privacy of the altered unnormalized density.

The addition has finite mass and moment because U lies in B_R and h_k is finite for each fixed k, including -1. After normalization, the exact cost change is

`J_new-J = integral_U (||x||²-J)(h_k-qhat(x))dx / (1+integral_U(h_k-qhat))`.

If U has positive area, the numerator is strictly negative. The density addition is positive there, and the cost is strictly below J except on the null circle. This would improve the genuine original optimizer. Therefore U is null, proving the backward condition in Section1.

For k=-1, `K_0 erosion D subset K_0` because0 is in D; Section2 puts K_0 inside B_R. Consequently `lambda(K_0 erosion D)=0`. Raising above the old maximum is allowed here: a was a property of the chosen optimizer, not a constraint on the original feasible class. Normalization and full pairwise privacy were checked explicitly.

The forward and backward obstacle inclusions are only **necessary conditions**. In particular they must not be silently converted into an equality recursion defining an optimal head, or treated as a matching all-law dual.

## 6. Dependent finite-tail bound from the top-plateau location

Choose any c in the nonempty K_0. Section2 gives ||c||_2<=R. For every y in B_R,

`||y-c||_1 <= sqrt2(||y||_2+||c||_2) <=2sqrt2 R`.

Thus with `L_J=ceil(2sqrt(2J))`, the closed ball is contained in `c+L_J D`, hence in `K_(L_J)` by exact iterated forcing. Since J<=4/epsilon² from the feasible Laplace law,

`L_J<=ceil(4sqrt2/epsilon)`.

The base sandwich then forces exact minimal Minkowski tails at all k>=L_J, just as in the base proof. This replaces only a coarse bound in a dependent consequence; it does not change the base theorem's truth or supply the unknown head shapes. No numerical level search or program is being proposed, and the bound is not claimed sharp.

## 7. Exact remaining finite-V problem

The optimizer may now be represented by closed compact levels, the cost-ball forward/backward necessary conditions, and an eventually forced tail. The finite head is still an **arbitrary coupled collection of compact sets**, not a supplied formula. Its optimal geometry and a matching all-law value/dual remain unproved. Neither convexity nor symmetry nor single-core minimal tails from level0 follows merely from these results.

All standard closure, support and elementary mass-variation devices are tools, not separately counted discoveries. The possible scientific content is this exact coupled optimal-law regularization/obstacle structure in the matched model; priority remains **NOVELTY_UNCLEAR**. The original mechanism ancestry and source-interface qualifications, including the2011/2013 prior class, remain mandatory. No source is edited and no scientific execution or formal proof is claimed.
