# Strict radial-cost equality: every optimal law is a staircase mixture

**AUTHOR CANDIDATE — WRITTEN with one exact rational total-variation check; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 17:56:50 PDT 2026`.

## 1. Original full-law class and exact equality structure

Fix EVERY finite epsilon>0 and `b=e^(-epsilon)`. Let F_epsilon contain ALL Borel probability laws on R^2 obeying `mu(A)<=b^(-1)mu(A+h)` for EVERY Borel A and EVERY h in the full CLOSED unit l1 diamond D. Let `r(x)=||x||_1`.

Let `phi:[0,infinity)->[0,infinity)` be Borel, finite and STRICTLY increasing, and suppose at least one law in F_epsilon has finite E phi(r). Define the actual full-law infimum `V_phi`. For `0<=gamma<=1` let Q_gamma be the normalized centered D-staircase `q_gamma(x) proportional to b^(min{k>=0:r(x)<=gamma+k})`, with Q_0=Q_1 as laws. Let Gamma_phi be the set of scalar offsets minimizing E_Q_gamma phi(r).

**Equality-lifting candidate:** at the named per-cost input below, the complete full-law optimizer set is EXACTLY

    argmin_(mu in F_epsilon) E_mu phi(r)
       = { integral Q_gamma lambda(dgamma) : lambda probability supported on Gamma_phi }.   (1)

Both sides are probability LAWS, with gamma endpoints identified when they give the same law. Every optimal original law is centered radial nonincreasing; a different nonradial optimizer cannot hide behind an existence-only radialization theorem. Conversely every measurable probability mixture on the scalar minimizing offsets is genuinely private and optimal. If all minimizing scalar offsets describe the same staircase law, the full-law optimizer is unique.

**Targeted consequences:** for phi(r)=r and phi(r)=r^2, the two scalar minimizers gamma_1 and gamma_2 are separately unique and satisfy `0<gamma_1<gamma_2<1` for every finite epsilon. Thus BOTH all-Borel optimizer laws are unique and different. Every globally first-moment-optimal law has strictly larger registered squared-Euclidean cost than an actual full-D-private competitor. This pays the nonradial squared-l1 optimizer-uniqueness gap left explicit in the earlier v253 record, and extends the preceding universal source-selector counterexample to ALL mean-optimal laws rather than just one.

For any distinct offsets `0<g1<g2<1`, this note also proves the exact positive distance

    TV(Q_g1,Q_g2) = [(g2-g1)(g1+g2+2m)/(1-b)] [1/D(g2)-b/D(g1)],      (2)

where `m=b/(1-b)`, `D(g)=g^2+2mg+m+2m^2`. Equation (2), with g1=gamma_1,g2=gamma_2, gives an explicit LAW-level separation, not just different formula parameters.

The general phi lemma is restricted to the same planar D model; it is a needed equality bridge for its two matching costs, not a claim about nonadditive mechanisms or all norms/dimensions. No Euclidean all-law optimum, new source priority or novelty is claimed.

## 2. Named input and exact dependency ceiling

The research input for (1) is the previously parent-WRITTEN_SUPPORTED complete alternative per-cost matching-norm proof:

`institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, §I; underlying `privacy-MDA26-norm-monotone-cost-direct-reconstruction-v1.md`, SHA `54cc4fd54fa74bad4c74d857ca7bca028cb0772bffe7771933857ebce52f164a`, especially §§2–6. It supplies the full-law bounded density and privacy-preserving equimeasurable rearrangement, amplitude-phase mixture, level-radius gap, actual all-phase parallelization toward the cost crossing, finite/infinite signed-sum control and attainment of SOME scalar staircase. The strict equality and arbitrary-optimizer conclusions below are additional derivations, not asserted as printed MDA or PMLR theorems.

The TWO cost-specific scalar root uniqueness/order claims are taken from my own still-UNREVIEWED `frontier-20261028-universal-pmlr-selector-separation-v1.md`, SHA `4c92d56867a959298836063d0045634cd61a0efb8f3175fcb701c4ac4a722fc6`, §§3–5. Its explicit P_m(gamma_1)<0 proof and positive J gap are an input to the targeted consequences, not automatically parent accepted. The general structural identity (1) and the exact TV formula (2) do NOT use those scalar claims. LAW642, v241 and v253 are not premises of this note.

## 3. Equality forces the SAME original law to be radially decreasing

Let mu be any original minimizing law. The named per-cost source supplies an absolutely continuous bounded density p and a fully private centered radial nonincreasing rearrangement p-sharp with equal superlevel-set volumes and no larger phi-cost. Let `A_s={p>s}` and let `B_s=R_s D` be the centered diamond with the same finite area. For every s for which the relevant moments are finite,

    integral_(A_s) phi(r) - integral_(B_s) phi(r)
       = integral_(A_s minus B_s)[phi(r)-phi(R_s)]
         + integral_(B_s minus A_s)[phi(R_s)-phi(r)].                   (3)

Both integrands are nonnegative. If the symmetric difference has positive area, at least one is STRICTLY positive on a positive-area set: phi is strictly increasing and an l1 sphere has Lebesgue area zero. Layer cake and Tonelli apply to the nonnegative finite-cost integrals. Since p is already globally optimal and p-sharp remains feasible, their costs are equal, making (3) zero for a.e. s. Therefore their superlevel sets agree a.e. for a.e. s, and another layer-cake integral gives `p=p-sharp` a.e.

Thus EVERY minimizing original law, not merely some rearranged representative, is centered radial nonincreasing. Strictness would fail for a cost with a plateau, so (1) is not asserted for merely nondecreasing phi.

## 4. Equality forces each optimal amplitude phase to be a minimizing staircase

For the actual p=p-sharp, let M=esssup p and use the source's normalized geometric amplitude phases

    u_a(x)=b^(min{k>=0:p(x)>a b^k}),
    q_a=u_a/Z_a,          a in [bM,M).

The source supplies a jointly measurable mixture with weights `Z_a da/(1-b)` summing to 1, and each q_a is itself genuinely full-D private. Its cost average equals the finite optimum. Because EVERY phase costs at least V_phi, almost every positive-weight phase has cost exactly V_phi.

For an optimal phase, its centered level radii R_i are finite, R_0>0 and `R_(i+1)>=R_i+1`. Put

    B(R)=2R^2,     A_phi(R)=integral_(r<=R) phi(r) dx,
    H_v(R)=A_phi(R)-v B(R),        v=V_phi.

Since every feasible density is positive a.e. and phi is finite/strictly increasing, v lies strictly between phi's essential extremal values. At its unique crossing r0, H_v is STRICTLY decreasing before r0 and STRICTLY increasing after r0: its signed radial increment is the integral of `4r[phi(r)-v]` and the factor has a strict sign away from r0. This remains true if phi jumps over v; no differentiability or a false equality-at-the-jump assumption is required.

The cited source constructs one t>0 such that every `t+i` lies between R_i and r0 and proves absolute convergence of both signed weighted level sums. It gives a genuinely feasible staircase Q_t with `J_phi(Q_t)<=v`. Since v is the full-law minimum, equality holds. Every term of the comparison is nonnegative and has a positive geometric weight; strict monotonicity of H_v implies every equality term forces `R_i=t+i`. Thus the actual phase law is Q_t.

If t>1, the source's exact identity

    u_(t-1)=b u_t+(1-b)1_((t-1)D)

expresses Q_(t-1) as a nontrivial mixture of Q_t and the inner-ball uniform law. Q_t is itself a positive mixture of uniform laws on `(t+i)D`. Coupling uniform radii by scaling the same D-uniform point and using STRICT increase of phi shows the inner-ball uniform has strictly smaller phi-cost, so `J_phi(Q_(t-1))<J_phi(Q_t)=v`, a contradiction. Therefore t belongs to (0,1].

The radius `t=R_0(a)` is a measurable function of phase amplitude: it is determined by the area of `{p>a}`, whose value is monotone measurable in a. Pushing the phase probability weights forward gives a probability lambda supported on Gamma_phi, and the original minimizing law is `integral Q_gamma lambda(dgamma)`. Source continuity of the scalar finite-cost function makes Gamma_phi measurable/closed; endpoint identification does not change laws.

Conversely a probability mixture of actual full-D-private Q_gamma laws is full-D private by Tonelli on EVERY event/shift, and linearity of the nonnegative cost makes it optimal when lambda is supported on Gamma_phi. This proves BOTH inclusions of (1), not just existence of one extremal optimizer.

## 5. Two cost-specific uniqueness and the actual Euclidean gap

For phi=r and phi=r^2 the preceding universal selector candidate proves, by exact quartic/quintic root signs and the identity `P_m(gamma_1)=-v^3(z-1)^3(z+3)/(4x_1)<0`, that each scalar minimizing law is unique and `0<gamma_1<gamma_2<1`. Applying (1) gives

    argmin_(mu in F_epsilon) E r = {Q_gamma1},
    argmin_(mu in F_epsilon) E r^2 = {Q_gamma2}.                         (4)

This is a new equality step beyond an existence-only staircase theorem. It is conditional on the cited alternative per-cost source and the separately unreviewed scalar proof; it is not an independent proof of source printed NR-A/NR-D or of the Euclidean all-law value.

The previous candidate constructs `p0=-P_m(gamma_1)>0`, a positive h and Dmax such that the ACTUAL full-D-private Q_(gamma1+h) satisfies

    J(Q_gamma1)-J(Q_(gamma1+h)) >= p0 h/(3 Dmax^2)>0.

Because EVERY first-moment optimum is now the SAME law, that strict original Euclidean gap applies to EVERY mean-optimal original law, not just one selected optimal staircase. The comparison uses the 2/3 angular relation only for the two actually centered radial laws.

## 6. Exact total variation between two different staircase laws

For `0<g1<g2<1`, let `D_i=D(g_i)` and `Z_i=2D_i`. D(g) is strictly increasing and

    D(0)=b D(1),     D(g1)>b D(g2),     D(g2)>D(g1).

For each k>=0, on the radius interval `(g1+k,g2+k)` the index of q_g1 is k+1 and of q_g2 is k, so q_g2>q_g1. On the complementary radial intervals their indices agree, so q_g2<q_g1. Sphere boundaries have zero area. Therefore the positive part of the density difference gives

    TV(Q_g1,Q_g2)
      = (1/Z2-b/Z1) sum_(k>=0)b^k |{g1+k<r<g2+k}|.

Since diamond-ball area is `2r^2` and the relevant geometric moments sum exactly,

    TV = [(g2-g1)(g1+g2+2m)/(1-b)] [1/D2-b/D1] >0,

which is (2). This is exact for every b in (0,1), not an asymptotic or bound. Taking g1=gamma_1 and g2=gamma_2 gives exact positive law-level source-selector separation even though the individual roots need not have elementary closed forms.

## 7. Actual bounded exact check and limitations

The following local `fractions.Fraction` cell checked the TV formula's elementary arithmetic for ONE synthetic pair of feasible offsets, without claiming either offset is an optimizer:

```python
from fractions import Fraction as F
b=F(1,2);m=b/(1-b);T2=m+2*m*m;g1=F(1,2);g2=F(3,4)
D=lambda g:g*g+2*m*g+T2
tv=(g2-g1)*(g1+g2+2*m)/(1-b)*(1/D(g2)-b/D(g1))
print('b=',b,'gamma1=',g1,'gamma2=',g2,'D1=',D(g1),'D2=',D(g2),'exact_TV=',tv)
print('gamma2_density_dominates_gamma1_on_mismatch_intervals=',D(g1)>b*D(g2))
```

Observed output:

```text
b= 1/2 gamma1= 1/2 gamma2= 3/4 D1= 17/4 D2= 81/16 exact_TV= 715/5508
gamma2_density_dominates_gamma1_on_mismatch_intervals= True
```

The exact infinite-sum derivation in §6 proves (2); the selected arithmetic is only a check. The general strict-phi equality lifting and cost-specific scalar conclusions require a disjoint complete review, especially the source phase/comparison imports, strictness through jumps, amplitude-to-offset measurability and scope of all-law mixture. This write is not parent adoption, independent-model/human/formal/kernel acceptance, global source-match clearance or novelty evidence. Historical held outcomes are not accepted as premises.
