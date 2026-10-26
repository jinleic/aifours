# CURRENT P44 CONSOLIDATION v13 — PART11/11: exact v-pivot slices and the current map of the ORIGINAL compression chart

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 22:20:56 PDT 2026**. Exact WRITTEN mathematics only, with no scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## V0. Scope and union rule

NEW claims C30.1–C30.3 continue Part10 on the SAME original chart R_x (Part10 H1.1, Part6 Y1.2). They add exact SN<=2 slices in v-dominant directions, which Part10's u-pivot could not reach. A self-audit of every Part10 identity found no correction needed; this is not an acceptance. **Original P44 remains UNMET.** The literal original input (1,1,1,1) remains OUTSIDE every proved region and its Schmidt number is UNKNOWN.

The complete current union is ALL ELEVEN parts and endings:
- the ten parts bound in `checkpoint-084-complete-current-v12-ten-part-manifest-h-absorption-v1.json` (SHA256 6567da14ee4110878911331c1e59bef8d8dace1e86ed6425ee86b2ca6fe24d9e);
- THIS part;
- all mandatory overlays named in cp082/cp084.

Process records cp083 (cadence miss + exactness MAJOR) and cp085 (NEW later decimal-heuristic exactness occurrence, ZERO credit) are permanent. No approximate scouting is a premise here; every displayed inequality is exact. Parts 9–11 are LATER UNREVIEWED; frozen v10/v111 is unchanged and nothing is inherited.

## V1. C30.1 — Theorem D: the slice x=(u,v,0,0)

Fix real r in (0,1). For zeta=e^(i theta), theta uniform, use the single circle family

```
psi_zeta = a + sqrt(r) zeta b - sqrt(r) conj(zeta) c + lambda(zeta) h_x,
lambda(zeta) = 1/( -sqrt(r) v conj(zeta) - u(1-r) ).                       (V1.1)
```

**Rank.** Rows are [1+lambda u, beta+lambda v, 0, 0], [gamma,1,beta,0], [0,-gamma,1,0], 0, with beta=sqrt(r)zeta and gamma=-sqrt(r)conj(zeta). Then row0=p row1+q row2, with p=(1+lambda u)/gamma and q=-p beta. The middle coordinate is EXACTLY lambda(v gamma-u(1+beta gamma))=1, and beta gamma=-r. This is Part10 F2 with w=z=0, so the rank is exactly two whenever the denominator is nonzero.

**Moments.** Assume sqrt(r)|v|>(1-r)|u|. Then

`lambda = -(zeta/(sqrt(r) v)) sum_(n>=0) (-u(1-r)/(sqrt(r) v))^n zeta^n`

converges absolutely on the circle and contains only POSITIVE powers. Hence:
- E[lambda]=0.
- E|lambda|^2 = 1/( r|v|^2-(1-r)^2|u|^2 ) by Parseval.
- a-b, a-c, b-c (E[zeta^2]) and c-h (only powers <=-2) cross-moments vanish.
- The single surviving cross is the ALLOWED b-h cross E[beta conj(lambda)] = sqrt(r) conj(c_0) = -1/conj(v), with c_0=-1/(sqrt(r)v).
- E|beta|^2=E|gamma|^2=r, E|alpha|^2=1, and kappa=0 since z=0.

**Theorem D.** If sqrt(r)|v|>(1-r)|u| and

`(1-r)(3 - 1/(r|v|^2-(1-r)^2|u|^2)) >= 1/|v|^2`,                            (V1.2)

then R_x is SN<=2. Proof: the residual is

`(1-r)P(c) + 3[P(d_x)+P(e)+P(f)+P(g)+P(j)]`

plus the {b,h_x} block with coefficient matrix [[1-r, 1/conj(v)], [1/v, 3-E|lambda|^2]]. (V1.2) makes that block PSD (its diagonals are then positive). Every vector of span{b,h_x} has Alice support in {0,1}, so the block is a sum of SR<=2 projectors. The integral of SR2 projectors lies in the closed SN<=2 cone. QED.

Exact examples:
- (1,2,0,0), r=1/2: r|v|^2-(1-r)^2|u|^2=2-1/4=7/4, and (1/2)(3-4/7)=17/14>=1/4.
- Ray (s,s,0,0), r=1/2: SN2 for s^2>=2.
- Same ray, r=3/5: r|v|^2-(1-r)^2|u|^2=(11/25)s^2, and the condition is 6/5-10/(11s^2)>=1/s^2, i.e. s^2>=35/22.

**Every direction is eventually covered.** For each ratio rho=|u|/|v| choose r in (0,1) with sqrt(r)/(1-r)>rho. Then the regime holds and E|lambda|^2 and 1/|v|^2 tend to 0 as |v| grows. Every nonzero-v direction of this slice is therefore SN<=2 at all sufficiently large norms. The v=0 axis is the old core0 mechanism; u=0 is the old middle-core checkpoint003 mechanism. Points such as (1,2,0,0) are new against the Part6 ball and Part10 Theorem C.

## V2. C30.2 — Theorem D': the slice x=(0,v,0,z)

Same family with u=w=0 and the j-coefficient from Part10 (H2.2):

```
beta=sqrt(r)zeta, gamma=-sqrt(r)conj(zeta),
lambda=-zeta/(sqrt(r) v), kappa=-z conj(zeta)/(sqrt(r) v).                    (V2.1)
```

**Rank, checked directly.** h_x=v|01>+z|03>. The rows are:
- row0 = [1, zeta(r-1)/sqrt(r), 0, -z zeta/(sqrt(r) v)];
- row1 = [-sqrt(r) conj(zeta), 1, sqrt(r) zeta, 0];
- row2 = [0, sqrt(r) conj(zeta), 1, -z conj(zeta)/(sqrt(r) v)].

With p=-zeta/sqrt(r) and q=zeta^2, row0=p row1+q row2 holds in all four coordinates. So the rank is exactly two.

**Moments.** beta, gamma, lambda and kappa are pure first-degree phases, so all means vanish. Forbidden crosses vanish: b-c, c-h and b-j all average zeta^(+-2), and j-h averages conj(zeta)^2. The allowed crosses are:
- b-h: E[beta conj(lambda)] = -1/conj(v), with Alice support {0,1};
- c-j: E[gamma conj(kappa)] = conj(z)/conj(v), with Alice support {1,2}.

The costs are E|beta|^2=E|gamma|^2=r, E|lambda|^2=1/(r|v|^2) and E|kappa|^2=|z|^2/(r|v|^2).

**Theorem D'.** If

```
(1-r)(3-1/(r|v|^2)) >= 1/|v|^2,
(1-r)(3-|z|^2/(r|v|^2)) >= |z|^2/|v|^2,                                       (V2.2)
```

then R_(0,v,0,z) is SN<=2. Both 2x2 residual blocks are PSD and live on Alice-rank-two spans. With r=1/2 the conditions reduce to |v|^2>=4/3 and |v|^2>=(4/3)|z|^2.

Example: x=(0,2,0,1). Part6's projective criterion requires 4+1<=2, which fails. Theorem D' holds since 4>=4/3. This point is new.

## V3. C30.3 — exact map of the original chart after Parts 6, 10, 11

**Proved SN<=2 regions** (each by an explicit operator certificate):
- Part6 ball normx^2<=2 and its projective-kernel image;
- old generic region, and the core0, middle-core and auxiliary axes;
- Part10 Theorem A slice (u,0,w,0);
- Part10 Theorem C u-dominant region (bounded z), and its involution image (w-dominant region);
- Theorem D slice (u,v,0,0), covering every v!=0 direction at large norm;
- Theorem D' slice (0,v,0,z).

**OPEN, with no SN<=2 certificate and no SN3 evidence:**
- directions where u, v and w are all comparable;
- v-dominant points with both u,z!=0 or w!=0.

In those directions every v-pivot member found here carries the same leading kappa-mean -zu/v^2 and lambda-mean -w/v^2. Cancelling them requires a different mechanism. The literal input (1,1,1,1) lies in this open core. It fails:
- Theorem D/D' (w,z!=0);
- Theorem C (m_L<0);
- (H5.1) (negative margin).

Part10 H6 showed explicit cheap SR2 completions there (a+j-h) and excluded only one restricted witness form. Whether some R_x in the open core has Schmidt number three is UNKNOWN. **Such a point would solve P44 positively. No such claim is made.**

## V4. Imports and the original gap

Ordinary imports: finite complex rank/PSD algebra, absolutely convergent Laurent series with Fourier orthogonality and Parseval, closedness of the SN<=2 cone, and the already-written Part6 chart/PPT image. No numerical value, sample, decimal heuristic, program output, old N4/solver result or unreviewed table is a premise. Examples use exact rational comparisons.

**Original physics-3/P44 remains UNMET:** no explicit rational 4x4 PPT state with a universal complex-SR<=2 strict negative separator, and no unrestricted all-4x4-PPT SN<=2 theorem. These are author-WRITTEN candidates pending fresh complete reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty/SOTA acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v13 PART11/11.**
