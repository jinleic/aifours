# A genuinely non-ME three-ray negative geometry: complete complex Gram interface and uniform structured PT obstruction

Actual `/bin/date` before writing: **Sun Oct 25 12:30:42 PDT 2026**. PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; cross-domain reconstruction and parent disposition pending.** Analytic branch of the SAMEoriginal P44primary, not a new registered problem or a reset of the live full16Droute. No scientific eval/interpreter/arithmetic program, enumeration, solver, replay or compile. Source/clock/hashmetadataonly; HOLD and v9/v10/v11remainbinding. Checkpoint013's older cadence deviation remains disclosed.

The source/Gram interface was frozen in `checkpoint-022-nonME-complement-source-and-Gram-interface-v1.json`, SHA-256 `41e86e04fe5058d90c04297c9aac4479d0b774e57e41bc38833cb0e494769c02`. Informal written leads before that checkpoint are disclosed, not called preregistered or independently supplied. This manuscript settles the ENTIREnew family, not isolated lambda controls on the old fixedQ.

## 1. New normalized negative rays and proof of genuine escape

Let Phi_U=vec(U)/2 for the normalized I,Z,X,ZX Weyl rays, Z=diag(1,i,-1,-i). Set

```
phi=alpha Phi_I+beta Phi_Z,
|alpha|^2+|beta|^2=1,
Q_phi=P(phi)+P(Phi_X)+P(Phi_ZX),
W_lambda=lambda I16-Q_phi, lambda>=0.                   (1)
```

The three rays are orthonormal: phiis a unit vector in the old Q0plane and the other two are the orthogonal shifted Q1rays. Thus Q_phiis a rank3projection and W_lambdahas THREEnegative eigenvalues for0<=lambda<1. This is outside the literal one/two-negative witness families.

Write the diagonal coefficients of phias

```
v_r=(alpha+beta i^r)/2, a_r=|v_r|^2.                     (2)
```

For alphabeta!=0the ray is NONmaximally-entangled: the four a_rcannot all equal1/4. In fact the partial trace is

```
Tr_B Q_phi=I4/2+diag(a_0,a_1,a_2,a_3),                   (3)
```

which is nonuniform. ANYpositive conic sum of normalized ME4projectors has partial trace equal to its total weight timesI4/4. Since TrQ_phi=3, (3)proves Q_phicannot be ANYsuch MEconic sum for alphabeta!=0, not merely that a displayed decomposition has too few terms. The supported arbitrary<=3ME-conic-term theorem is therefore inapplicable to these genuine interior cases. The endpoints alpha0orbeta0are MEoverlaps with that older theorem, included for boundary completeness and not counted as new.

It also cannot be hidden as another scalar<=3MErepresentation with a different scalar shift: Q_ME=Q_phi+(lambda'-lambda)Iwould have rank16if the shift were positive and would not be PSDif negative. A rank<=3positive ray sum therefore forces the shift zero, returning the nonuniform-marginal contradiction.

The fixed four-Weyl scalar theorem also does not transfer merely from Q_phi<=Q. Partial transpose is not positive-order-preserving; their difference is the PT of an entangled rank-one projector and is indefinite. Moreover two-positivity of W_lambda(Q_phi)=W_lambda(Q)+P(phi_perp)does not imply two-positivity of W_lambda(Q). No invalid converse is used.

Generic rank-one PTand MEpair bounds only give `Q_phi^Gamma<=I`, while a principal Gram test forces lambda>=(2+sqrt2)/4<1. Thus the old generic bounds leave a real interval and do NOTimmediately settle this new geometry. The structured proof below is additional information.

## 2. Full-COMPLEX universal rank-two criterion for the actual non-ME ray

Define normalized coefficient matrices

```
V0=(alpha I+beta Z)/2, V1=X/2, V2=ZX/2.
```

For EVERYcomplex rank-two orthogonal projector Pput

```
H_rs(P)=Tr(V_r* P V_s), r,s=0,1,2.                      (4)
```

Then

```
W_lambda is two-block-positive
 iff H(P)<=lambda I3 for EVERYsuch complex P.            (5)
```

Proof. Write any rank-at-most-two C=SZwith S* S=I2, P=S S*. Set v_jr=S*V_r e_jand let V_jcollect these columns. The negative overlaps are h_r=Tr(V_r*C), and h=sum V_j*z_j. The exact squared norm of Z->his lambda_max(sum V_j*V_j)=lambda_max(H). This proves sufficiency. If Hv=gv with unit v and g>lambda, take z_j=V_jv: then ||Z||^2=g,h=gvand expectation g(lambda-g)<0on an actual rank-at-most-two matrix. Every complex plane and lower-rank C is included.

The non-MEdiagonal `H00=sum_r a_r P_rr` generally is NOT1/2and is not replaced by the MEformula. All cross entries involving V0are retained. No real-plane or finite sample is asserted sufficient.

The MEpair V1,V2still gives a necessary principal-block bound. At Pprojecting onto span{e0,e1}, its diagonal entries are1/2and off-diagonal is `(1/4)Tr(X*PZX)=(1+i)/4`. Consequently every universally rank-two-positive W_lambdamust satisfy

```
lambda>=lambda0=(2+sqrt2)/4.                             (6)
```

The variable non-MEentries can only increase the full Gram maximum relative to that principal block; they were not discarded as a positivity certificate.

## 3. The actual normalized amplitude bounds

From(2), for each r,

```
a_r+a_(r+2)=1/2, hence0<=a_r<=1/2.                      (7)
```

For adjacent indices r,smodulo4,

```
a_r+a_s<=1/2+sqrt2/4=lambda0.
```

Indeed the sum is `1/2+(1/2)Re(alpha conjugate(beta)(i^(-r)+i^(-s)))`, and |alpha beta|<=1/2while the two adjacent unit phases sum to modulus sqrt2. Therefore

```
|v_r v_s|^2=a_ra_s<=lambda0^2/4
 =(3+2sqrt2)/32<3/16.                                  (8)
```

The strict last inequality is2sqrt2<3. For opposite indices, (7)gives

```
|v_r v_(r+2)|<=1/4.                                    (9)
```

These are uniform complex amplitude identities, including arbitrary alpha/betaphases and zero components. They are not evaluated on selected examples.

## 4. Exact total-index structure of the partial transpose

Let T_phi=Q_phi^Gamma. The pure diagonal ray contributes a weighted swap, while the shifted MEpair has the known direct action:

```
T_phi|r,s>=v_s conjugate(v_r)|s,r>
       +(1/4)(1+i^(s-r+1))|s+1,r-1>.                   (10)
```

Thus total index tau=r+smodulo4is invariant. The following structure exhausts ALLsixteen basis vectors.

- tau0: highpositions00,22have diagonals a0,a2; lowpositions13,31have zero diagonals and cross coefficient v1conjugate(v3). The shifted-pair term couples00to13and22to31, each with squared modulus1/8.
- tau2: highpositions11,33have diagonals a1,a3; lowpositions20,02have zero diagonals and their opposite-vcross coefficient. The shifted-pair term again supplies a diagonal matching of squared modulus1/8.
- tau1: two disjoint pairs10/01and32/23, with diagonals1/2,0. Their off-diagonal moduli are |v1v0|and|v3v2|.
- tau3: two disjoint pairs03/30and21/12, with diagonals1/2,0. Their off-diagonal moduli are |v0v3|and|v2v1|.

There are no entries outside these structures. The odd-sector shifted term has only its fixed-point diagonals1/2; its other coefficient vanishes. The even-sector pure diagonal ray has only its fixed-point a_rdiagonals and its opposite low/low swap. This follows directly from(10), not from an unadmitted matrix diagonalization.

## 5. Uniform structured bound T_phi<=3I16/4

For an odd-sector2 by2block, `3I/4-T_phi` has diagonals1/4,3/4and squared off-diagonal modulus bounded by(8). Its determinant is at least

```
3/16-(3+2sqrt2)/32=(3-2sqrt2)/32>0.
```

So every odd-sector block is PSD, with no omitted phase branch.

For an even sector, order its two highpositions first, then their matched lowpartners. Its matrix has the form

```
[ diag(a_h,a_h')   K ]
[ K*          [0,c;conj(c),0] ],
```

where K is diagonal, each |K_jj|^2=1/8, each a_h<=1/2, and |c|<=1/4by(9). At3/4the high diagonal of `3I/4-T_phi` is positive definite, each entry at least1/4. Its exact Schur complement has low diagonals

```
3/4-1/[8(3/4-a_h)]>=1/4
```

and off-diagonal-c. Thus both diagonals are nonnegative and their product is at least1/16>=|c|^2. This Schur complement is PSD, so the full even sector is PSD. Its denominators stay at least1/4even when some v_rvanishes; no singular boundary has been hidden.

The four sectors prove the WHOLEoperator inequality

```
Q_phi^Gamma<=3I16/4                                    (11)
```

for EVERYnormalized complex alpha,beta. This is an upper bound, NOTclaimed to be the exact maximum PT-eigenvalue or PPT-overlap threshold.

## 6. Complete scalar-completion obstruction and non-vacuous headroom

Combining the universally necessary(6)with the new structured bound(11),

```
W_lambda^Gamma>= [lambda0-3/4]I16
                =[(sqrt2-1)/4]I16>0.                   (12)
```

Hence EVERYtwo-block-positive scalar completion in this ENTIREone-non-ME-plus-two-MEfamily is completely copositive and detects NO PPTstate. A negative PPTtarget would require lambda<3/4by(11), while actual two-positivity requires the incompatible(6). No invalid attractive PPTcontrol is fabricated after this uniform obstruction is proved.

This is not merely a PSD-only family. RanQ_phiis a subspace of the accepted four-Weyl range, every nonzero vector of which has Schmidt rank>=3. Since Q_phiis an orthogonal projection, compactness of unit SR<=2vectors gives eta_phi=max<psi,Q_phipsi><1. Thus scalar completions with eta_phi<lambda<1are two-block-positive but non-PSD. This is existence-only headroom, not an evaluated etaor a displayed certified lambda. The no-detection theorem is still uniform over ALLvalid lambda.

That nonemptiness paragraph's named range import is Section4of `four-Weyl-rectangle-consolidated-obstruction-v1.md`, SHA-256 `eb1ed1c5aba2bb444a817b48a39ff3d7206c1aacc65421cca7073cffe64a5e02`, at the actual `ppt-four-Weyl-semigroup-two-choice-parent-v1.md` disposition. The uniform Gram/PT obstruction(12)itself does not consume this headroom import.

## 7. Source validity and exact remaining primary step

The source framework remains Hou–Li–Poon–Qi–Sze2015Propositions2.2–2.3for arbitrary negative matrices, with(5)rederived in full. No ME-only formula is extended to V0. The Chruściński–Kossakowski–Sarbicki0908.1846v2spectral sufficient condition cannot be borrowed: in this actual three-negative projection the squared2-Schmidt norms sum to at least1/2+1/2+1/2>1, so its strict<1hypothesis fails. The new proof is the structured weighted-swap/Schur argument above, not that sufficient criterion.

The concrete phi=(PhiI+PhiZ)/sqrt2has a Gaussian-rational projector, Schmidt rank3and nonuniform partial trace. It is a genuine non-MEnegative direction, but its SCALARpositive completion is now closed if this proof is reconstructed. The theorem does NOTexclude non-scalar/anisotropic backgrounds for Q_phi, arbitrary non-MEnegative rays, or arbitrary rank-three negative subspaces.

A precise remaining non-MEbranch is D-Q_phiwith full positive16entry D. Its exact universal condition is the same weighted inverse-Gram construction as before, using the THREEactual normalized matrices V0,V1,V2and all complex rank-two planes. An eligible actual target is the coordinate-asymmetric R(s,t)ofcheckpoint021; for the displayed equal-sum phi+, its Q_phi-overlap is1+s+2t. Actual G_D<=IANDnegative normalized PPTexpectation remain unproved. The original full16DfixedQbranch is also still open; this note does not reset or replace the registered P44target.

No SN3state, unrestricted no-go, SOTA/novelty, formal/kernel, scientific-execution/replay, human/cross-vendor or publication acceptance is claimed. Old accepted scopes, the old21table's unreconstructed status and N4historicalUNKNOWN/exit-unestablished record remain unchanged. Currentprimaryresearchcontinues with the exact remaining anisotropic/coherence interface; no newGO is requested.
