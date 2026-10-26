# Werner upper zero — GLOBAL quantitative compatibility repair by two anchored q matchings

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE, not parent-read/reviewed/adopted.** Actual preceding `/bin/date`: **Sun Oct 25 19:03:44 PDT 2026**, precreation observation only. Same ENTIRE allpositive/fullcomplex p12/q6 E_full target. Exact symbolic/rational WRITTEN reasoning only, NOT checked-in-kernel. No scientific interpreter/eval/calculator/program/CAS, enumeration, solver/replay, test/build, scientific CLI, nested agent or GO. OWN written-exactness/cadence findings and all other HOLD/source/process histories remain; ZERO approximate guidance/verification credit, no blanket clean-history assertion. Original cutoff/deadline unchanged.

## 1. Exact input and reason to retain the actual correction

Use the COMPLETE actual raw completion in v7, SHA256 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`, and the proved global row/anchored-negative-edge identities in v9 `1a41695f8bbde665338e4daca4fdba41713472cdb20d9490ac78add2a277b616`, v10 `8fd87df6cd19dfc1ddd3205ee59ebc090cddb2c962ef337abcf87a2b75350938`, v11 `ed3358376965bd005bc3ef8f76ce13560c2296a81d559eb43fef7995ed3f1485`, at their full named operative union: generic G1-G12, FALSE-G13 correction, ENTIRE raw Gram, physical P4/P10, literal residuals and v24 limited scope. NOT false G13, bare dual lift, unproved P11 or unadmitted arithmetic. New ordinary imports: elementary complex square completion and monotonicity of a minimum when positive terms are dropped.

The equivalent original sign remains the actual anchored at-most3-edge deficit Gram. Stronger standalone Praw/row Phi tests are unproved; they are not necessary for E_full. This packet puts an EXPLICIT quantitative portion of the actual compatible q6 minimum back into that comparison, rather than pretending its centers independent or discarding the entire positive correction.

## 2. All ACTUAL centers and coefficients

Assume ALL ci>0,sum ci^2=1, xi=ci^2,di=1-xi,dij=(di+dj)/2,r=(sum1/di)^(-1). All Z are COMPLEX with Zc=0. Relabel a maximal Schmidt square as x0; no spectrum is excluded. The actual negative edges are confined to the triangle{12,13,23}, while0i edges are positive by v11.

For the six unordered q potentials z_e define the actual coefficients from v7:

```
w_ij=ci*cj*dij,
m_ij=xi*xj*gF_ij>0,
gamma_(i;jt)=xi*xj*xt*dij*dit/(2djt)>0,
beta_(i;jt)=sqrt(2)*di*djt/(dij*dit),
Tij=Zij/(ci*cj),
a_ij=(di*Zij+dj*Zji)/(sqrt(2)*ci*cj*gF_ij).
```

The ENTIRE compatibility correction is

```
C_comp(Z)=min_(ONE common complex symmetric z6) {
 (1/2)sum_(i;j<t;j,t!=i) gamma_(i;jt)
       |z_ij-z_it-beta_(i;jt)(Tij-Tit)|^2
 +(1/2)sum_edges m_ij |z_ij-a_ij|^2 }.                    (MC1)
```

This is the ACTUAL full-raw correction. All shared-edge/commutator terms are in gF/gamma. No boundary inverse is evaluated. Orientation of a row difference may be reversed together with its center inside an absolute square.

## 3. Exact two-node series identity over COMPLEX variables

For positive m,n,gamma and arbitrary complex a,b,d,

```
min_(u,v) (1/2){m|u-a|^2+n|v-b|^2+gamma|u-v-d|^2}
  = |a-b-d|^2/[2(gamma^(-1)+m^(-1)+n^(-1))].             (MC2)
```

Proof: put U=u-a,V=v-b and Delta=a-b-d. For fixed W=U-V, minimizing m|U|^2+n|V|^2 gives k|W|^2 with k=mn/(m+n). The remaining minimum of k|W|^2+gamma|W+Delta|^2 is k*gamma/(k+gamma)|Delta|^2 by one complex Hermitian square completion. Restoring1/2 gives(MC2). This is an exact identity, not a network analogy or a matrix replay.

For a tail edge ij and a shared tail endpoint i, set

```
Delta_(i;j)=a_ij-a_i0-beta_(i;j0)(Tij-Ti0),
Lambda_(i;j)=[gamma_(i;j0)^(-1)+m_ij^(-1)+m_i0^(-1)]^(-1)>0. (MC3)
```

These centers are not independently attainable. Their incompatibility is exactly what appears in Delta.

## 4. Two genuine q matchings and a GLOBAL repair bound

The q nodes are{01,02,03,12,13,23}. The following are disjoint-pair matchings of those SAME six nodes using actual row-difference graph edges:

```
Mplus ={(12,01) through row1,
        (23,02) through row2,
        (13,03) through row3},
Mminus={(12,02) through row2,
        (23,03) through row3,
        (13,01) through row1}.
```

For Mplus retain only those THREE graph squares in(MC1), but retain ALL SIX mass squares once each; drop the other nine graph squares, which are nonnegative. The retained objective now genuinely decouples into three two-node problems. Its minimum is exactly(MC2), so

```
C_comp >= C_plus
 =(1/2)[Lambda_(1;2)|Delta_(1;2)|^2
       +Lambda_(2;3)|Delta_(2;3)|^2
       +Lambda_(3;1)|Delta_(3;1)|^2].                    (MC4)
```

The same argument for Mminus gives the reversed three oriented terms. Each is separately a lower bound for the ENTIRE common-vector minimum; neither uses a mass square more than once. Therefore their AVERAGE is also a valid lower bound:

```
C_comp(Z)>=(1/4)sum_(i,j in{1,2,3},i!=j)
                    Lambda_(i;j)|Delta_(i;j)|^2.         (MC5)
```

The factor1/4 is important:1/2 comes from the original objective and the other1/2 from averaging TWO different valid weakenings. They are not added with full weight. No claim of equality with C_comp, simultaneous minimization of the dropped graph centers, or independence of the original q6 values is made.

## 5. Physical mismatch formula, retaining every mixed term

For clarity, multiply a single mismatch by sqrt(2)*ci. Exact substitution yields

```
sqrt(2)*ci*Delta_(i;j)
 = [di*Zij+dj*Zji]/[cj*gF_ij]
  -[di*Zi0+d0*Z0i]/[c0*gF_i0]
  -[2di*dj0/(dij*di0)]*[Zij/cj-Zi0/c0].                 (MC6)
```

Thus the actual repair couples BOTH directed entries of the tail edge and BOTH directed entries of the anchor edge. It is not a square of a selected symmetric/skew part alone. All terms have fixed actual coefficients; small coordinates are positive by scope. No selected test family, vanished anchor entry, independent row center or dropped output-c component is inserted.

The min in(MC1) remains the original one; formulas(MC3)-(MC6) merely give a transparent physical lower bound without a six-dimensional inverse.

## 6. A refined SUFFICIENT comparison, not a completed sign

With the globally positive row N_i and actual edge coefficients kappa from v9-v11, the original full energy obeys

```
E_full(Z)>=P_match(Z):=
 sum_i z_i^dagger N_i z_i
 +sum_edges kappa_ij |sqrt(di/dj)Zij+sqrt(dj/di)Zji|^2
 +(1/4)sum_(i,j in{1,2,3},i!=j)Lambda_(i;j)|Delta_(i;j)|^2. (MC7)
```

P_match retains an ACTUAL portion of the nonnegative full-raw resolvent/compatibility correction. It is less overstrong than dropping all C_comp and more explicit than treating its centers as free. Proving P_match>=0 uniformly would suffice for the original target. It is still UNPROVED. A negative P_match would only reject this matching weakening, not E_full, Z_up or W4. The fully equivalent original anchored Gram remains the task when this bound is too coarse.

NEW GLOBAL WRITTEN progress: exact common-q6 matching lower bounds, the correct averaged factor, and a full physical four-entry mismatch formula. This is a genuine replacement mechanism for the blocked standalone-row route, not another spectrum enumeration or a false-lift revival.

Still NOT_PROVED: uniform P_match/Praw/row Phi signs, full anchored-triangle Gram, generic E_full/Z_up, other three canonical signs and unrestricted W4. No full-target separating spectrum or physical witness. Full source-union reconstruction/parent disposition is required before promotion; no formal/kernel/human/configured-family/executable/triple-witness/novelty acceptance, GO or park. Original cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 unchanged.
