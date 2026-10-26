# Optimal planar private noise: exact screened scalar systems and an attaining law

Observed clock before creation: **2026-10-24T06:42:00-0700**.

## 0. Result, composition status, and limits

This is ONE consolidated manuscript for the same fixed-sensitivity problem. It composes the parent-supported all-law equality **V=W1** with the separately parent-supported calibration of the ENTIRE canonical one-core class. No frozen source, review or parent note is rewritten.

**Assurance:** scoped same-harness supplied-proof mathematics, at the existing **WRITTEN_SUPPORTED** levels of its components. This consolidation is an additive composition and explicit presentation, not a new blind, external-model, human, formal/kernel, numerical or executable verification. Its integration read is separate from those earlier component checks. The actual slice-C primary audit has now been read in full raw before this first frozen consolidated snapshot; its bounded source boundary is recorded below. Full-result priority remains **UNESTABLISHED / NOVELTY_UNCLEAR**.

For every finite ε>0, the original optimum is exactly the unique admissible solution of the screened scalar systems in Section2. Section3 gives a normalized density attaining that value under EVERY shift in the full closed sensitivity diamond. No unknown measure, curve, compact outer minimum or multilevel support vector remains to optimize in this final characterization.

There is still a scalar root to determine. The result is NOT an elementary inverse formula, an executed numerical root or a sampled mechanism. No uniqueness of ALL original nonsymmetric/noncanonical optimizers is asserted. This is a modern mathematical subproblem of the broad printed privacy-utility article, not a solution of that entire book article.

## 1. Original all-law problem and scalar constants

Let

```
D={h in R²: |h1|+|h2|<=1},
b=exp(-ε),    0<b<1.
```

Minimize squared-Euclidean error over ALL Borel probability laws:

```
V(ε)=inf_mu ∫ |z|² dmu(z),
mu(E)<=b^(-1)mu(E+h)
for EVERY Borel E and EVERY h in the full CLOSED D.
```

No density, symmetry, convexity, coordinate independence, attained peak or shell representation is imposed on this original class. Those properties needed for the selected attaining representative are derived in the proof chain. The laws are query-output-independent additive noise distributions; “all-law” does not mean all data-dependent or nonadditive DP channels.

Set

```
m=b/(1-b),
T1=m,
T2=m+2m²,
T3=m+6m²+6m³,
T4=m+14m²+36m³+24m⁴,
v=T2-m²=m+m²,
lambdaP=T4/(3T2)=4m²+4m+1/3,
C0=T3/3-m*T2/2.
```

Equivalently Tj=E G^j for P(G=k)=(1-b)b^k, k≥0. All constants are finite and m,v,T2 are strictly positive. The interval T2<lambda<lambdaP below is a screening condition inherited from the complete calibration, not a new envelope claim.

For t≥0 define the explicit shifted-moment polynomials

```
M1(t)=m+2t,
M2(t)=T2+4tm+4t²,
M3(t)=T3+6tT2+12t²m+8t³,
M4(t)=T4+8tT3+24t²T2+32t³m+16t⁴.
```

Thus Mj(t)=E(G+2t)^j. Define

```
H_D(t,lambda)=(2/3)M4(t)-2lambda*M2(t).
```

## 2. Exact evaluation prescription: one globally valid screened branch

Exactly ONE valid parameter pair is obtained across branches D and R below, counting their common transition as the same core. Existence and global screening follow from the entire-class calibration, not from choosing an arbitrary stationary root.

This is a mathematical root prescription only. No polynomial, transcendental equation, integral or optimizer was executed in this round for this result.

### D. Full-diamond branch

Find a real root t of the fixed polynomial equation

```
2 M3(t) M2(t)-M4(t) M1(t)=0.
```

Define

```
lambda_D(t)=(2/3)M3(t)/M1(t).
```

Retain the root ONLY when ALL screens hold:

```
0<t<1/2,
T2<lambda_D(t)<lambdaP,
lambda_D(t)>=4t²+4mt+T2.
```

If there is such a root, set lambda=lambda_D(t). It is the unique valid solution across both branches. The attaining core is the full diamond S=2tD.

The polynomial is explicit through the four printed Mj; M1>0. The stationarity formula and polynomial jointly imply H_D=0. The final inequality is the full-upper-clip condition, not an optional numerical check.

### R. Rounded branch

For a scalar d define

```
P(d)=(4/3)d³+2md²+m²d,
t(d)=[P(d)-C0]/v,
lambda(d)=2t(d)²+2d²+2m(t(d)+d)+T2,
c(d)=t(d)-d.
```

Retain ONLY

```
0<d<1/2,
t(d)>d,
T2<lambda(d)<lambdaP.
```

For these parameters put a=lambda-v, w=2t and define the following elementary functions, with t=t(d), lambda=lambda(d), c=c(d):

```
J3(a,c)=[c*sqrt(a-c²)*(5a-2c²)
          +3a²*arcsin(c/sqrt(a))]/8,

Rint=-(2/3)J3(a,c)+(ma-m³/3)c-c⁴/3+lambda*c²/2,

Uint=[w³/3+mw²+(T2-lambda)w]c
     +[-w²-2mw+2lambda-T2]c²/2
     +(2/3)(w+m)c³-(2/3)c⁴,

H_R(t,lambda)=H_D(t,lambda)+8(Rint-Uint).
```

Solve the SINGLE scalar equation

```
H_R(t(d),lambda(d))=0
```

under every displayed screen. If branch D has no valid root, exactly one such rounded root exists. Set t=t(d) and lambda=lambda(d).

All square roots and the principal arcsin are well defined: a-c²=(t+d+m)²>0, a>0, and0<c/sqrt(a)<1. The rounded screen excludes c=0; that transition is already covered by D and is not a second optimum. No unfiltered stationary solution is declared optimal.

### The value

For the valid branch and parameter pair,

```
V(ε)=lambda.
```

This holds for EVERY finite ε>0, not merely a low-privacy limit or a list of parameter values.

## 3. The actual attaining probability law

### 3.1 Core and profile

The same compact convex core can be described uniformly as

```
S={z in R²:
     |z|_1<=2t,
     |z|²+2m*|z|_infinity+T2<=lambda }.
```

In branch D the curved constraint is inactive on the diamond. In branch R the first-octant cap is

```
F(y)=sqrt(a-y²)-m,    0<=y<=c,
F(y)=2t-y,           c<=y<=t,
a=lambda-v,  c=t-d.
```

In branch D simply F(y)=2t-y on[0,t]. The profile is continuous, nonincreasing and1-Lipschitz, with F(t)=t and t≤F≤2t-y. Its terminal facet width is d∈(0,1/2), taking d=t in branch D. Convexity of this optimal core is DERIVED by the entire-class minimization, not assumed in the original all-law problem.

### 3.2 Closed level index, including all boundaries

Let

```
n_S(z)=min{k>=0:z in S+kD}.
```

It is finite everywhere. An explicit equivalent version uses X=max(|z1|,|z2|), Y=min(|z1|,|z2|):

```
n_S(z)=max(0,ceil(X-F(Y)))       when0<=Y<=t,
n_S(z)=ceil(X+Y-2t)             whenY>t.
```

The formulas match at Y=t. Ceilings assign exact integer boundaries to the earlier CLOSED level. Isolated boundary choices do not create atoms; the law below is a Lebesgue density.

### 3.3 Exact positive finite normalizer

In both branches,

```
Z=8∫_0^t(F(y)-y)dy+8tm+2T2.
```

For the diamond this evaluates to

```
Z_D=8t²+8tm+2T2=2M2(t).
```

For the rounded branch define

```
J1(a,c)=[c*sqrt(a-c²)+a*arcsin(c/sqrt(a))]/2,
I_area=t²+J1(a,c)-(m+2t)c+c²/2.
```

Then

```
Z_R=8I_area+8tm+2T2.
```

This presentation introduces no new optimizing step: J1 is the elementary antiderivative of sqrt(a-y²) on[0,c], and splitting the profile integral at c gives exactly I_area. It agrees with the diamond expression when c=0. Since F≥t and t>0, the core area is at least4t² and Z>0.

Define the probability density

```
p_ε(z)=b^(n_S(z))/Z.
```

No shell's mass is assigned independently. Its mass follows from this actual normalization; every tail is included.

### 3.4 Full privacy and actual optimum cost

For EVERY z and EVERY h∈D,

```
S+n_S(z)D+h ⊂ S+(n_S(z)+1)D,
```

so n_S(z+h)≤n_S(z)+1. Applying the same argument with-h gives the reverse index inequality. Therefore p_ε(z)≤b^(-1)p_ε(z+h) pointwise, including corners and closed boundaries. Integration proves the original inequality for every Borel event, not just sampled shifts or noise regions.

Compactness of S and geometric decay give finite mass and squared moment. The exact tail calculation yields H_D=0 or H_R=0 precisely as N-lambda Z=0, where N=∫|z|²b^n_S(z)dz. Thus

```
∫p_ε=1,   ∫|z|²p_ε(z)dz=lambda=V(ε).
```

The selected law is D4-symmetric and centered as a consequence of the construction. The original feasible class was not restricted to centered, symmetric, independent-coordinate or density laws. Coordinates of the attaining law need not be independent.

## 4. Connected proof of the composition

### 4.1 Why the original all-law problem reaches a canonical optimizer

The five-body structural/variational packet proves original attainment by tightness and one weakly convergent subsequence, passing every fixed-shift inequality to that same limit. Tonelli derives density/peak facts rather than imposing them. Actual positive amplitude-mixture weights select a geometric global optimum. Essential supports and a genuine normalized simultaneous filling operation give one pointwise-private representative with compact measure-regular closed levels.

Area-preserving Steiner operations in axes and diagonals are actual feasible whole-level competitors. Equality of their nonnegative moment deficits forces exact contractions of the SAME original optimal levels. This produces canonical, possibly nonconvex profiles; no optimizer is silently exchanged between properties. The complete arguments and classical interfaces remain in the pinned source bodies below.

### 4.2 Why the WHOLE original head is one core

The new head-removal proof consumes R7 explicitly. A strict common-cap gap gives an open positive-area set on which raising to the previous geometric height preserves every directed full-D privacy edge and strictly improves the ACTUALLY normalized original cost. Thus every common cap increments exactly by1.

All remaining head freedom is one global offset f, with exact closed index max(0,ceil(x-f(y))). Above t0 it gives an arbitrary AC trajectory g=y-f with1≤g'≤2. The fast-tail potential is calibrated throughout the ENTIRE region g>0,y≥g/2, not only on a selected path. Its derivative is-(b^j/2)K, and the exact all-phase polynomial certificate is K≥m/3>0. Integrating the verification identity compares every such head to the true K0-generated one-core law, with unchanged RAW top rows and its own normalizer.

Original global minimality forces equality in that comparison; strictness gives g'=2 a.e. and hence exactly K_i=K0+iD at all levels. This is a global all-law objective argument, not local stationarity, Pareto minimality or a chosen-core restriction. Therefore V=W1. The proof did not use the W1 stationary systems to obtain the equality.

### 4.3 Why the scalar systems calibrate the ENTIRE one-core minimum

For fixed t, minimizing the signed numerator N-lambda Z over ALL canonical profiles gives the feasible clipped root

```
min(2t-y, max(t,sqrt(max(lambda-v-y²,0))-m)).
```

Coercivity supplies compact attainment over all t≥0. Point-core and lower-flat cases are excluded by exact ratio and moving-clip derivative arguments. Thus the selected optimum has a free arc/upper facet or a full facet; convexity follows afterward. The diamond derivative has at most one relevant positive local minimum, the rounded derivative satisfies

```
H_tt=16[v+(2d+m)(2t+m)]>0,
```

and the regimes glue with the correct endpoint derivatives. This proves global uniqueness at the positive value-zero minimum, not just stationarity. Removing an actual unit-diamond summand excludes d≥1/2, including its separate zero-area point exception.

The branch-D polynomial and branch-R scalar equation in Section2 are exactly those critical equations with their global screens. Their elementary primitives evaluate the remaining integrals. At least one valid branch exists by attained minimization, and there is at most one valid solution across both. The original all-law equality may now be substituted, yielding Section2's V and Section3's attaining law.

The uniqueness used here is the optimum within the ENTIRE canonical one-core class, up to changes leaving its law unchanged. It does not classify every original nonsymmetric, non-geometric or noncanonical optimizer.

## 5. Frozen proof and assurance ledger

This is an additive composition. LF counts and hashes identify snapshots; they are not substitutes for full reads and do not constitute executable verification. Historical candidate/pending labels at source creation remain intact; the parent dispositions are the current assurance overlays.

### Mathematical sources in this owned root

| Source | Exact SHA-256 | Role |
|---|---|---|
| `proof-coupled-level-tail-saturation-v1.md` | `ae1e05470b233d2e51a3c56f45a58ab97ecd249a5ed479dc33c6d29ae4ea3958` | Original all-law optimum, geometric selection, supports, forward sandwich/tails |
| `proof-coupled-level-tail-ADDENDUM-1-closed-levels.md` | `87320046a2396eb936138af7c3eb3122a5e3451140a70171dce73cb270fd5596` | SAME closed representative and actual backward raising |
| `proof-coupled-level-tail-ADDENDUM-2-coordinate-Steiner.md` | `15a4d1eda329a5f8eb22207c8fce9750f906d5f3cba8d290a65bde5426c29007` | Axis contractions, exact coupled feasibility and equality cases |
| `proof-coupled-level-tail-ADDENDUM-3-diagonal-Steiner.md` | `6da3be079457f4558a32d422c04185e01e0f996fccfe6719152da2c53f55ad36` | Diagonal geometry and arbitrary-size nonconvex cap/line polynomials |
| `proof-all-epsilon-finite-parameter-characterization-v1.md` | `9525687c8bfd782d4d907c2f236b1dcc6824c99f301e5594f23fe5e71c786e0e` | Exact original finite-parameter value/selector interface |
| `outer1-entire-one-core-minimum-calibration-v1.md` | `7c615bb1b645c1a77a20354efd7798cd5ff8836b3eb72e0a3223994f076a7a89` | ENTIRE canonical W1 class and screened scalar systems |
| `outer1-global-single-core-sufficiency-candidate-v1.md` | `adb8eb857af3b431168514792a47813c53bdae0b0d60b1ca6ebfe4f79e682bcc` | NEW global full-head comparison proving C and V=W1 |

### Actual reviews and parent compositions

- Original D0 actual return: physics `ame46-support/peer-review-privacy-coupled-D0-v1.md`, SHA `166dab4ce10c6fd624a09ffc666ccf886888a1e9462c04e9e4aa5ee5210c3a2f`; dependent E return: mathematics `sun-coset8/peer-review-privacy-all-epsilon-E-v1.md`, SHA `0e1064b5721a6ef1ca8fed600447846bee2ebb90dc0e39d2f5f1c42f2b7ccc7c`.
- Parent all-epsilon variational composition: `privacy-all-epsilon-variational-parent-v1.md`, SHA `35da3323f7a368543d0b83714856625e104b81ea11df44041b5447b714b0e871`.
- Actual ENTIRE-W1 return: mathematics `shor-completion/peer-review-privacy-entire-one-core-v1.md`, SHA `f7b0d93f15510397886b7d5341aba108286803485063db5bb711d7727a52e7b5`; actual parent privacy section in `wave-v17-partial-parent-dispositions-v1.md`, SHA `208b2a66fd3b012a554e6f93e1af12f8910ef2615ab866b142e31dfc33276450`. That note did NOT itself prove equality.
- Actual new tail-A return: mathematics `shor-completion/peer-review-privacy-OUTER1-tail-calibration-v1.md`, SHA `a9ee4d0e50e1c70aefd0e7d026def81f795caeb697fbccb8ef3ea57c3650f4e8`; actual new all-law-B return: physics `ame46-support/peer-review-privacy-OUTER1-all-law-bridge-v1.md`, SHA `f742f3ebfda9c00db2289b847a1ef2054636f5e34ee6cc3b2b80390aba80ac53`.
- Parent global-equality composition: `privacy-global-equality-parent-v1.md`, SHA `a029ee4e75f85f744c848e4c08c5b8a7729ae65e5a7718355f78cb21f978ee11`. It matched the acyclic B-geometry → A-global-tail → B-raw-normalized splice and supports equality at the stated written level. This manuscript performs the subsequently requested composition with W1; it does not backdate that step into the earlier parent note.

The source parent notes are in `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/`; reviewer roots are under the corresponding domain's `evidence/three-area-20261023-96h/parallel-18/`. No GitHub publication is implied by these local references.

A and B were disjoint deep reconstructions with full shared interface, not two interchangeable full-proof verdicts. Their frozen conditional statuses were true at creation; counterpart bodies and literal exports were read afterward and composed explicitly. No result is promoted from dispatch, an ACK, metadata, a previous W1 check or a source-only review.

- Actual source-only C return: information-science `robust-spr7/source-audit-privacy-OUTER1-global-v1.md`, SHA `1b6340532f1bdaac3d07d686671fd9e740da0f7df7f13547dacff366b1c68322`; all233 substantive lines were read raw, including the final continuation. It supplies no mathematical FATAL/MAJOR/MINOR verdict.
- Actual parent source qualification: `privacy-equality-slice-C-addendum-v1.md`, SHA `6da174fe3bed55acdec40691eb498db9a0f02d74b0c76fc91501cd5bed0d85e1`; its complete17-line body was read. It retains V=W1 at WRITTEN_SUPPORTED and novelty at NOVELTY_UNCLEAR.

The first consolidation draft preceded this author's complete C-return read; C was integrated before the first frozen consolidated hash. The source audit's candidate/A+B-pending language is retained as its reviewer's at-creation scope/knowledge disclosure, not used to date or override the actual parent correctness composition. No earlier source read or verdict is retroactively strengthened.

## 6. Provenance, prior work, and remaining assurance

The book provenance is Yang Xiaochun and Yu Ge, *Privacy Protection for Sensitive Data*, printed583-586/PDF604-607 in *10000 Selected Problems in Sciences: Information Science*, Science Press2011, ISBN978-7-03-031911-1. It asks a broad privacy/usefulness/information-loss tradeoff, not this literal modern DP optimization. The exact volume routing, first-page image and four-page text are preserved in the selection/source records. No full-book solution follows here.

The exact historical modern conjecture is [Geng-Viswanath2013, arXiv1312.0655v1](https://arxiv.org/html/1312.0655v1), final paragraph of SectionIII: d=2, squared-Euclidean loss and the SAME full l1-translation privacy model. The conjectured correlated staircase density is homothetic l1-radial. The source-C audit authenticated this literal statement rather than inferring it from a paper title.

An arbitrary canonical one-core S is a BROADER class than that historical f_gamma family. C plus the calibration does not automatically affirm the homothetic restriction; Sections2-3 distinguish the full-diamond and rounded alternatives. The retained strict-comparison packet concerns that narrower assertion and is neither rewritten nor used as a premise here. The2015 journal theorem's visually verified l1 loss is not substituted for the squared-Euclidean objective.

The accepted [EQ-V1 audit](prior-equivalence-audit-v1.md) and source-boundary parent remain binding:

- Both fixed-active selector comparisons are direct PRIOR corollaries of [Amir-Rietzke2025](https://eprints.lancs.ac.uk/id/eprint/229183/1/23292-2_3_.pdf), Theorem1(i)+Lemma1(iii), at the matched lattice/strong-set-order/modularity/derivative hypotheses. No new general monotone-selector principle is claimed.
- Generic attainment is a statement-level prior consequence of [ElSalamouny-Gambs2018](https://arxiv.org/pdf/1805.09571v1), Theorem8. Its arbitrary-X framework EXACTLY includes our class via X=D/2 and ell constant off zero; its particular circularization hypotheses do not thereby apply.
- Shell/Minkowski mechanism ancestry is PRIOR in [SCDF2013](https://openaccess.uoc.edu/handle/10609/152758) and its2011 antecedent. Its sufficient Theorem13 includes the literal condition S0⊂Sf and concentration-order minimality, not multivariate squared-loss exhaustiveness. This manuscript proves its constructed law's privacy directly; it does not assert every canonical core meets that source's extra membership condition.
- Same-norm staircase optimality is not automatically a theorem for our mixed objective. The actual source-only slice-C audit and parent addendum establish a precise bounded non-equivalence boundary for the NEW equality/calibration, not a worldwide absence proof. No exact earlier proof was established among the primary statements read; no worldwide priority, novelty, publication or significance clearance is inferred.

The standing calibrated label is: **an exact variational characterization and global head-removal for one planar mixed-geometry problem, assembled with substantially PRIOR tools**. The further scalar-system evaluation and law description do not turn standard tools into inventions or create an aggregate discovery count.

All parent evidence errata v1-v5, timestamp/verification qualifications and N4 UNKNOWN/resource/unestablished-exit/HOLD remain operative. The author's earlier04:22:29→05:38:30/05:39:07 active-checkpoint deviation remains disclosed in checkpoint020; later mathematics does not repair it. No continuous-activity or fresh-runtime census claim is made.

No scientific program, arithmetic interpreter, CAS, numerical root/integration, solver, tests, proof assistant, native scientific launch, model CLI, nested agent, publication or shared-index edit was performed for this consolidation. Ordinary source/metadata work and written elementary formula composition are all that occurred. There is no new executable GO.
