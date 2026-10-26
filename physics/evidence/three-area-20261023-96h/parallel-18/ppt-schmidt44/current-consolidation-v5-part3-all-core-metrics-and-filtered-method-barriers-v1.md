# CURRENT P44 CONSOLIDATION v5 — PART3/3: all core metrics, ALL local filters, and the fullD diagonal-filter boundary

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 18:22:38 PDT 2026**. Exact WRITTEN mathematics only, not machine/kernel verified. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 unchanged.

## V0. Complete THREE-part current union and additive status

The complete v5 is the union of ALL of the following literal bodies, as pinned in its author manifest:

1. Entire frozen v3,723LF54000bytes, SHA256 `041471cfd6990fd764563366bc1c9e5273afe278356c8199e0ce1118a9a02fc3`: C1–C10, all original proofs/context/gap.
2. Entire frozen v4 Part2,394LF27845bytes, SHA256 `a9b780b56dec585aca58723a43fc464d3cd23926e261940f91a13e321a9c0cab`: C11–C14, weighted PPT constructor, operator SN2 certificates and the first whole-method barriers.
3. Entire THIS new Part3: full C16/C17 proofs, with C15's intermediate restricted metric result included as a special case of the stronger new proof.

Every LF/ending of ALL THREE is required for an entire-current v5 gate. Older headers/end labels remain immutable historical bytes, not pretended original v5 labels. Part3 alone is not the entire current source. Existing v2/v3/v4 frozen assignments retain their exact scopes; no review is restarted/backdated and no old verdict transfers to the broader new quantifiers.

**NEW C16 proves a bound for EVERY complex Alice core metric and a method miss under ALL local filters for THIS constructor/witness mechanism. This is NOT an unrestricted all4x4 PPT no-go.** NEW C17 proves the fixed full16D Weyl witness route misses the same actual PPT constructor under ALL diagonal local filters, not arbitrary non-diagonal rotations or allPPT states. Neither proves general constructor SN<=2 or generic compressed-witness decomposability.

All mandatory v9/v10/v11/HOLD and later overlay `RUN/later-resumption-and-opaque-findings-v6.md`, SHA256 `b482c4c6ea08d7549d7a551df0eb38c513dc332e8128c22e3e7a6a3b1e4b26ca`, remain. My separate ACK-order MAJOR, checkpoint049 private written-exactness MAJOR, older cadence/admission/N4/old21 findings remain permanent. No clean-order/cognition/runtime census or process cure by a later correct identity. All new mathematics here is author-WRITTEN pending fresh complete reconstruction.

## V1. Exact matrix domain and the current core

Use the natural complex vec convention and unnormalized projectors. On3x3 let

```
G0=I3,
G1=B=E01+E12,
G2=L=E10-E21,
a=vecG0=00+11+22,b=vecB=01+12,c=vecL=10-21,
C=P(a)+P(b)+P(c).                                       (V1.1)
```

The other fixed4x4 constructor rays, for ANY complex x in C4, are

```
d_x=02+|3>tensorx,e=20+33,
f=30,g=32,j=23,h_x=|0>tensorx.                            (V1.2)
```

Each of these SIX remaining rays has SR<=2. The previous weighted constructor had core C. Here we also allow arbitrary nonnegative core weights

`C_(u,v,w)=uP(a)+vP(b)+wP(c)`.

The full operator is a positive conic sum of those three core rays and the six named remaining rays. We claim method barriers only for this explicitly specified construction, not every positive4x4 operator.

C itself is not being called a PPT/SN3 solution. Its matrix pencil has determinant

`det(zI+vB+wL)=z^3`.

Its support has no rank2 vector with a nonzero a coefficient; the range criterion thus gives SN(C)=3, but it is NPT (the partial-transpose expectation at02-20 is negative). The core's genuine3-dimensional NPT entanglement does not imply that any of its PPT extensions preserves SN3. None of the new method barriers says otherwise.

## V2. C16's central theorem: ALL Alice metrics have normalized core norm<=2

### V2.1 Exact Bob transpose and the three-vector Gram

Let R be ANY invertible complex3x3 Alice core filter, P=R*R>0 and

`E(P)=sum_(i=0)^2 Gi* P Gi>0`.

The ACTUAL Bob marginal of `C_R=(R tensorI)C(R* tensorI)` is `D_R=E(P)^T`. Indeed the Bob marginal of P(vec(RGi)) is `Gi^T P^T barGi`. Thus there is no real-only or transposed-metric substitution.

The Bob-normalized operator is

`Ctilde_R=(I tensorD_R^-1/2)C_R(I tensorD_R^-1/2)`.

Its three generating coefficient matrices are `R Gi D_R^-T/2`; hence its nonzero eigenvalues are those of the Hermitian PSD3x3 Gram

`H_ij(P)=Tr(Gi* P Gj E(P)^-1)`, `TrH=3`.                 (V2.1)

It suffices to prove for EVERY complex unit coefficient vector z that

`Tr(A0*P A0 E(P)^-1)<=2`, `A0=sum zi Gi`.                 (V2.2)

This is an exact norm statement for every complex P, not selected parameter points or diagonal metrics.

### V2.2 Full complex coefficient reduction using an actual SU2 symmetry

Reorder the3-dimensional coordinates as endpoints(0,2), middle1. For u in C2 set

`N(u)=[0_2,u;u^T J2,0]`, `J2=[0 1;-1 0]`.

B,L are N(u) for the orthonormal endpoint basis u=e0,-e2. If S in SU2 and U=S directsum1, then

`U N(u)U*=N(Su)`

because `S^T J2 S=J2`, while U I U*=I. Thus simultaneous local U tensorbarU fixes C EXACTLY and conjugates the two Kraus matrices B,L by a unitary coefficient transformation. This is a proved symmetry, not arbitrary state averaging.

A global phase makes z0 nonnegative real. SU2 acts transitively on the complex unit sphere of the two remaining coefficients, so after this actual simultaneous conjugation one may take

`A0=a I+b B`, a,b>=0, a^2+b^2=1.                         (V2.3)

P is conjugated by the same U and remains completely arbitrary. The Kraus sum E(P) and the trace in (V2.2) transform covariantly. No general Alice metric was diagonalized or discarded.

If a=0, A0 has rank<=2. Complete its coefficient vector to an orthonormal Kraus basis. E(P)>=A0*P A0, so the PSD contraction `E^-1/2 A0*P A0 E^-1/2` has rank<=2 and trace<=2. This proves that whole boundary without an inverse of A0.

### V2.3 Invertible A0: exact reduction to a positive3x3 S

For a>0 put tau=b/a>=0 and u_tau=1+tau^2. Take the unitary Kraus completion

`A1=-b I+a B`, `A2=L`.

Let `Li=Ai A0^-1`. Since B^3=0,

```
L1=-tau I+u_tau B-tau u_tau B^2,
L2=sqrt(u_tau) L(I-tau B+tau^2 B^2).                     (V2.4)
```

The order is important: Ai=Li A0, so

`E=A0*[P+L1*P L1+L2*P L2]A0`.

With `Mi=P^1/2 Li P^-1/2` and `S=M1*M1+M2*M2>=0`, exact cyclic trace cancellation gives

`Tr(A0*P A0 E^-1)=Tr(I+S)^-1`.                           (V2.5)

This includes arbitrary complex P and is not a scalar or commuting-metric approximation.

### V2.4 Explicit exterior-square matrices and the invariant product trace

Use ordered basis01,02,12 on the exterior square. Direct2x2 minors of (V2.4) give

```
wedge2 L1=[tau^2   -tau u_tau    u_tau]
          [0        tau^2      -tau u_tau]
          [0          0         tau^2],

wedge2 L2=u_tau[0  0    0]
                 [0  0    0]
                 [-1 tau  0].                           (V2.6)
```

The product's diagonal entries are `-u_tau^2,-tau^2 u_tau^2,0`, so

`Tr[(wedge2 L1)(wedge2 L2)]=-u_tau^3`.                    (V2.7)

Similarity by wedge2(P^1/2) preserves this product trace for M1,M2. No Frobenius norm is incorrectly called similarity invariant; only this cyclic trace is invariant.

Let e2 denote the second elementary symmetric function. For PSD A,B,

`e2(A+B)-e2(A)-e2(B)=TrA TrB-Tr(AB)>=0`.

This follows from B<=TrB I. The singular-value/exterior-minor identity gives

`e2(Mi*Mi)=norm(wedge2 Mi)_F^2`.

Therefore, by ordinary Frobenius Cauchy–Schwarz (the wedges need NOT be PSD),

```
e2(S)>=norm(wedge2 M1)_F^2+norm(wedge2 M2)_F^2
     >=2|Tr[(wedge2 M1)(wedge2 M2)]|
      =2u_tau^3>=2.                                     (V2.8)
```

For the three nonnegative eigenvalues of S, with elementary functions e1,e2,e3,

`Tr(I+S)^-1=(3+2e1+e2)/(1+e1+e2+e3)<=2`,                 (V2.9)

because the difference between twice the denominator and the numerator is `e2+2e3-1>=0`. All denominators are positive. No numerical roots, samples, floats, interpreter or CAS enter this argument.

Equations (V2.2)–(V2.9) prove the central theorem

`normCtilde_R<=2 for EVERY invertible COMPLEX R`.         (V2.10)

The earlier diagonal/endpoint-block metric C15 is genuinely subsumed by this NEW proof, not retroactively accepted by an old restricted gate. Singular R has core Alice support<=2, which is handled directly by universal two-block-positivity in the application; no singular inverse is taken.

## V3. C16 application: ALL local filters of the weighted constructor miss the inherited family

Let even d>=4, real skew unitary J_d, and

`W_d=2I-P(Omega_d)-2T_J`.

The complete universal two-positivity proof is in current Part2 U6: for any complex Alice2-plane, the skew in-plane m component has inverse cost q/4 and the outside component (2-q)/2, totaling1-q/4<=1. Thus all local compressions/filters of W_d are sound SR2 witnesses. There is no inherited Schmidt LOWER bound or indecomposability assumption.

For clarity, the actual Alice3 Schur interface used here is also stated. With isometry Q3, m=sum|i>barq_i, V=spanJq_i, m=m_V+m_W, the in-V skew singular values are alpha,alpha,0. Put t=alpha^2 in[0,1]. Then

`normm_V^2=2t`, `Hmat Hmat*=(1-t)I+tP_rank1`.

The exact positive peel has V block `4P_antisym-P(m_V)`, off block `-m_V m_W*`, and outside block `[2t/(4-2t)]P(m_W)`. It is PSD by its supported Schur complement; the symmetric zero kernel has no cross. The remaining outside operator is

`Rout=2I-cP(m_W)`, `c=2/(2-t)`.

For ANY Bob filter F and the filtered core C_R, set E=Tr(F D_R F*) and Y=overline(F D_R^1/2), so normY_F^2=E. Pulling m_W=vecHmat back by I tensor(D_R^1/2 F*) gives coefficient matrix Hmat barF (D_R^1/2)^T=Hmat Y EXACTLY. Thus the overlap is `<vec(Hmat Y),Ctilde_R vec(Hmat Y)>`. Its partial trace is I_B, so every rank1 Alice conditional has norm<=1. Combining that fact with (V2.10) gives the ACTUAL overlap bound

```
<m_W,(I tensorF)C_R(I tensorF*)m_W>
 <=[(1-t)2+t]E=(2-t)E.
```

This is the COMPLEX-D_R generalization of current Part2 U6.3: Y=overline(F D_R^1/2), NOT barF D_R^1/2 unless D_R is real. Thus Rout contributes at least `2E-c(2-t)E=0`; the positive peel contributes nonnegative. Endpoints t=0,t=1, zero/rank-deficient Bob F, and all outside dimensions are included.

Now take ANY linear Alice map A:C4->Cd and Bob map Bmap:C4->Cd. The first three Alice columns A3 acting on C either have rank<=2, when the transformed core is already SN<=2, or factor as Q3 R with Q3 isometric and R invertible3x3. The preceding proof applies in the latter case; the core Bob map is arbitrary. EVERY other positive-weight generator d_x,e,f,g,j,h_x remains SR<=2 under A,Bmap, so its W_d expectation is nonnegative.

Consequently, for all complex x, all positive auxiliary weights, all even ambient d>=4 and ALL local maps,

`Tr[W_d (A tensorBmap)R(A* tensorBmap*)]>=0`              (V3.1)

when the core is C. Equivalently no arbitrary nonisometric local compression/filter of the inherited witness can separate ANY such input. This closes the previously proposed nonisometric-Alice/core-metric replacement for THIS mechanism. It does NOT make every compressed W decomposable or classify OTHER PPT states.

### All actual PPT positive core weights are covered too

Allow arbitrary nonnegative core weights u,v,w. In any actual PPT constructor, the PT principal block on12,21 is EXACTLY

`[v u;u w]`.

The other SIX named rays do not alter these populations/coherence. Thus `vw>=u^2`. If u=0 all rays are SR<=2 and the claim is trivial. If u>0 then v,w>0; choose k=(v/w)^(1/4). The local diagonal maps

`S_A=diag(k,1,k^-1)`, `S_B=diag(k^-1,1,k)`

fix a, send b to k b and c to k^-1 c. Therefore

```
C_(u,v,w)=u(S_A tensorS_B)C(S_A* tensorS_B*)
 +(v-u sqrt(v/w))P(b)+(w-u sqrt(w/v))P(c),                (V3.2)
```

with both residual coefficients nonnegative. Applying the ALL-filter theorem to the first term and universal SR2 positivity to the residuals proves (V3.1) for EVERY actual PPT positive-nine-Gram constructor, ALL its positive core/auxiliary weights and ALL further local maps.

This corollary STARTS with an actual PPT constructor. It does not silently assert that a singular filter of an arbitrary NPT tuple inherits the unfiltered principal-block premise. Closed zero-weight cases above are handled without the fourth root of zero divided by zero.

## V4. NEW C17 — direct complex endpoint completion for full16D W_D

Use the current Part1 full16D fixed-Weyl definitions. W_D=D-Q0-Q1 is assumed nonnegative on EVERY complex SR<=2 vector; product tests force d02,d20>=0. No scalar/two-level restriction or sampling.

For ANY diagonal three-level core vector

`v_alpha=alpha0 00+alpha1 11+alpha2 22`,

add only entries p02,q20 with `p q=alpha0alpha2`. The endpoint2x2 coefficient block has rank<=1 and the isolated11 block rank<=1, so the completed matrix has SR<=2. Because Q annihilates BOTH02 and20 and D is product diagonal, its exact W expectation is

`<v_alpha,W_Dv_alpha>+d02|p|^2+d20|q|^2`.

Infimizing only the endpoint moduli proves

`<v_alpha,W_Dv_alpha>+2|alpha0alpha2|sqrt(d02d20)>=0`.      (V4.1)

All phases are retained; a unit square root of the product phase implements the completion. If one low diagonal is0, the infimum is approached by finite reciprocal p,q, and a strictly negative core expectation would yield a finite violating vector. If alpha0alpha2=0, v_alpha already has SR<=2. Thus ALL zero boundaries are covered without division by zero. This is a direct infinite-family two-positivity consequence, not a claim that eight necessary tests become sufficient.

## V5. C17 application: ALL positive weights and ALL diagonal local filters

Take ANY actual PPT positive-nine-Gram constructor, allowing arbitrary nonnegative core weights, and apply arbitrary complex DIAGONAL local filters on Alice and Bob. It remains a positive sum of its filtered rays, and PPT by the actual local congruence. Let v_alpha be the filtered sqrt(u)*a core vector. NONE of the SIX remaining named rays or b,c contains BOTH00 and22, and diagonal filters do not change that fact. Hence the actual state's00/22 coherence is EXACTLY

`rho_(00,22)=alpha0 conjalpha2`.

Write actual populations `P02=rho_(02,02)`, `P20=rho_(20,20)`. The ACTUAL PPT principal block on02,20 gives

`P02 P20>=|alpha0alpha2|^2`.                              (V5.1)

This is not a separately chosen population relaxation.

It remains to justify that the entire noise has W cost at least d02 P02+d20 P20, rather than assuming arbitrary entry deletion preserves rank. Here the EXACT named shapes matter:

- After diagonal filters d_x contains02 plus a single-Alice-row3 product tail. Removing02 leaves SR1; all cross with02 vanish since W_D|02>=d02|02>.
- e contains20 plus33. Removing20 leaves a product; all cross with20 vanish since W_D|20>=d20|20>.
- h_x lies on a single Alice row0. Removing02 leaves a product on that same row.
- b,c,f,g,j have no02/20 component and retain SR<=2.

Thus exact splitting of each named vector's quadratic form gives nonnegative residual costs by universal two-block-positivity, and

`Tr(W_Drho)>=<v_alpha,W_Dv_alpha>+d02 P02+d20 P20`.

The nonnegative AM–GM bound and (V5.1) make the right side at least

`<v_alpha,W_Dv_alpha>+2|alpha0alpha2|sqrt(d02d20)>=0`        (V5.2)

by (V4.1). No inverse population, missing phase, kernel assumption, finite sample or false arbitrary-SR2-noise deletion is used. This closes the ENTIRE actual PPT constructor, ALL positive core/auxiliary weights, ALL complex x and ALL diagonal Alice/Bob filters against the ENTIRE fixed full16D W_D family.

The theorem does NOT cover arbitrary non-diagonal rotations/maps for W_D, arbitrary non-diagonal positive completions, every PPT state, or general input SN<=2. Essential hypotheses are the pure diagonal3-core, its exact endpoint coherence with no noisy00/22 contribution, and the proved removable-low-entry shapes. General PPT operators can have coherent endpoint-noise cancellations or lack such a Gram decomposition; no unrestricted transfer is licensed.

## V6. Source binding, superseded leads, and the still-open ORIGINAL P44

Historical exact written lead pins:

|Lead|SHA256|Role|
|---|---|---|
|checkpoint058|319370d22652a697bda2a94c4d0268998643d81f4b83780e0e8cb326f96f63e0|Restricted diagonal/endpoint-block metric C15, now included by NEW C16, not an earlier acceptance|
|checkpoint059|c05829488aba44d4e100466914af67fd3d08815e3a5daa4b6bc46a380bb45608|ALL complex metrics/exterior-square/filter theorem lead, not preregistration|
|checkpoint060|4d1dcf10aecd3d2f97e41f58c3568949e5f0a147ca058c77eac4d39effbbe727|All core weights/direct rank2 endpoint completion/all diagonal-filter fullD lead; the known count wording was fixed before first SHA|

All new model-specific calculations are fully given above. Ordinary imports are finite complex linear algebra, supported Schur complements, PSD trace/Gram/rank facts, unitary Kraus changes, exterior-square functoriality and its2x2-minor/singular-value identities, Frobenius Cauchy–Schwarz and nonnegative AM–GM. No quantum classification, old solver output, old21/N4 table, computational enumeration, symbolic program or unreplayed finite certificate is an opaque premise.

The source [Krebs–Gachechiladze2509.07086v1](https://arxiv.org/html/2509.07086v1) was read only through the actual shown1–300LF, including the main4x5 range proof and SupplementA heading, NOT the remaining301–605LF. Its two separate auxiliary columns are not available after a4x4 compression; no range proof is transferred. It is ancestry/status context, not novelty clearance or a correctness import into V2–V5.

Part2's earlier statement that nonisometric Alice metrics remained OPEN was correct at THAT frozen source. NEW C16 now closes the whole metric/local-filter route for THIS core/witness mechanism if independently reconstructed; it does not retroactively edit/read/accept that older source. Likewise Part2 C14's phase-only boundary is extended only by NEW C17's complete endpoint-completion/population proof, not by naming old verdicts. C9/PV-input SN2, C10/LDOI SN2, and C11/C12 actual operator retirements retain their distinct state-versus-method meanings.

**Original physics-3/P44 is still UNMET.** There is NO explicit4x4 PPT state with an actual universally complex-SR2-nonnegative STRICT negative separator and NO unrestricted theorem every4x4 PPT state is SN<=2. All-filter no-go for this named constructor/witness mechanism is NOT an all-state no-go. Generic inherited witness decomposability remains unknown on OTHER PPT geometry; general weighted constructor SN remains unknown outside the actual operator certificates.

Genuine remaining science must change eligible PPT geometry for the inherited class, change the witness mechanism on a potentially non-SN2 input, use a genuinely non-covered non-diagonal rotation/positive background for fullD, or prove an actual all-state theorem. Further x/weight/local-filter retuning of this constructor against the inherited mechanism, or diagonal-filter retuning against fixed fullD, cannot be sold as a live original-point route. No newD/SNR label can revive an actual SN2-retired state.

No formal/kernel/executable/triple/human/configured-family/cross-vendor/novelty/SOTA/publication acceptance or scientific permission follows. The complete v5 requires ALL literal parts/current overlays and a separate future gate; hashes do not replace body reading. No new slot, deadline reset, book-solution count or round closeout. This is not a terminal park; the original round remains active.

**END OF COMPLETE CURRENT v5 PART3/3.**
