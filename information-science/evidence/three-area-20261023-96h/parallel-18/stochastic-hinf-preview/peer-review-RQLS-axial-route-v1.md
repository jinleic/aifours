# RQLS10 fixed axial route — actual supplied-proof reconstruction v1

Reviewer **InfoHinfPreview**, retained primary info-3. Assignment: `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v10.json`, own entry only. Author **PhysicsRQLS10**, physics-5. This file is the only new reviewer output. Author files and shared indexes were not edited.

Actual review-start `/bin/date`: **2026-10-24T02:54:15-0700**. Later returned observations used during reconstruction: **03:05:12**, **03:16:01**, **03:20:30**, all on 2026-10-24 at -0700. These are observations, not exact file-creation timestamps. No uninterrupted work since the previous day's central-route review is claimed.

## 1. Verdict, correction history and exact scope

**The unqualified original v1 packet does NOT receive a passing label.** This reconstruction found an actual wrong mixed-matrix coefficient and a separate false local-ring-unit description. They were reported before final disposition, adopted by the author, and repaired in new immutable errata. The original body and its original pin remain part of the history, not a silently corrected source.

- **M1, MAJOR source-coefficient defect, original packet:** `axial-negative-paw-fourth-order-v1.md:32` prints the hub mixed column's fixed entry as `0`. Its actual value is **`-2*d0`**. The assertion that the printed column satisfies regularity was consequently false. This is not a phase convention or merely a reviewer preference. Section 7 below derives the correction directly from the literal core and traces its downstream effects through the full operator blocks.
- **m1, MINOR local-ring terminology defect, original packet:** the same file:47–50 calls `beta_R/L` units. They have valuation exactly one and are nonunits. Their **denominators** are units, and the left/right elementary changes of basis are invertible without dividing by beta.
- The existing **count erratum** in the assigned v1 packet was already mandatory. It correctly distinguishes the entire paw class from the parallel-leaf, heavy-opposite-hub subtype. It is not omitted or replaced by either new erratum.

I have now read and independently reconstructed **both new errata** and both successor overlay manifests on freshly observed matching hashes. **Amended verdict, only for the complete v3 → v2 → v1 packet WITH ALL THREE mandatory errata: 0 FATAL / 0 unresolved MAJOR / 0 unresolved MINOR.** The original finding history is one major and one minor; neither is erased by this amended verdict. This is a supplied-proof written-support verdict at the following exact scope, not parent acceptance.

Let `F9=F3[alpha]/(alpha^2+1)`, label `x+y*alpha` by `x+3y`, put `s=i*sqrt(7)`, and fix the literal first matrix

    C=(J-I+s*Q0)/sqrt(8),     Q0_xy=chi(x-y).

Fix, on those SAME labels,

    rho=(0,2,1,6,7,8,3,4,5),
    H={1,2}, b={3,6}, d={4,7}, e={5,8}.

For EVERY second literal `C'=P*C*P^T` and EVERY arbitrary complex vector delta with all nine `|delta_t|=1`, the necessary zero equation

    M*delta=0,   M_it=conjugate(C_ti)*C'_(t,rho(i))

has no solution. Independent diagonal D/E phases are retained; the outer E phases cannot repair a required zero. The 5040 count is a count of distinct literal second cores, not executed cases, scientific problems or discoveries.

**Not covered:** axial rho being WLOG, every first orientation, every conference9 monomial class, all complex H0 lifts, nonuniform arrays, a 100-ray construction, unrestricted maximal-cardinality 1-RQLS(10) impossibility, novelty/publication significance, a human/formal/cross-vendor verdict, or scientific execution. The primary problem remains UNKNOWN. This is one additional fixed-orientation local obstruction, distinct from the previously reviewed central `rho=-t` route.

## 2. Exposure, complete read coverage, actual pins and primary imports

Prior exposure was disclosed in the startup ACK: I reconstructed the earlier eight-body CENTRAL-route packet; my prior return was `peer-review-RQLS-fixed-route-closure-v1.md`, SHA256 `a59dae775f5d24379863a972e1590e6ff3f69981a823dc7966838f8fac394d59`. That was not a review of the axial packet. No prior verdict, symmetric-block shortcut, blind-review claim or independent-discovery label is transferred here. During this review the author received my two concrete findings and supplied the two numbered repairs. That communication is part of the exposure record.

I read the v10 common contract, full own entry, all five mandatory parent overlays/settled-N4 receipt, and ALL complete assigned component bodies. All sixteen original listed input hashes matched their actual bytes. Those original inputs contain 1883 LF including the manifest. All four later repair/overlay files below were also read completely and freshly hashed. The consumed older papers were read in full, but their imported roles here are only the conference/phase interface, general rank8 norm lemma and second-grid catalogue/coverage, NOT the old first-orientation rank conclusions.

All paths in this table are relative to `physics/evidence/three-area-20261023-96h/parallel-18/rqls10/`.

| Actual input | Observed SHA256 |
|---|---|
| axial-complete-route-packet-v1.json | `68ec25b418404be05e6ebdb9f2e65c6f6933bb6268aaac130d9cd6206514d4f7` |
| selection-v2-axial-orientation-v1.md | `76f5edb573d1c584fed6cd196e3e344a7ea30bcd326bd492245e1b83cd3710fd` |
| axial-partial-symmetry-descent-v1.md | `86c589add8fde94840aae94194846305eb14734eadb3875daa8fdd6f3b679e95` |
| axial-leading-class-reduction-v1.md | `bbd578cd37941440d84b6d4c867b726ff6483905ed730dcb07e3eb7da3efda1b` |
| axial-mixed-block-closures-v1.md | `eccc911f66c9b4d5712a06d6027d7383acbf49b11b8a2e639afb68823f2fa24d` |
| axial-negative-axis-triangles-v1.md | `f8d14b81d37a147f167e9ef4ce5af006ac37ec0ef77b5ec9c48450224bb14ebc` |
| axial-negative-paw-fourth-order-v1.md | `a93b22f594d335cfff8c0c5962ba4a522c10db89ec9a1893008c9d0bc7e35536` |
| axial-negative-paw-count-erratum-v1.md | `8e652273bda16a1dfad560b8f0382a166c600d798551881a473b6bc1c4555fbb` |
| axial-negative-paw-residual-closure-v1.md | `ce7b58cd6be1054eb646cd9851777241c58797889c8c40d280ee55fc85855679` |
| axial-complete-route-candidate-v1.md | `8bdca671dc76480fd8b0c2dcd8c8e156d33468a9758456ec9caaa1e7ecebaa97` |
| candidate-CONFERENCE-GLUING-v1.md | `15da67c0b9241ac6b5f4128305f023d5efe82e53728fcde2829189e235516995` |
| candidate-CONFERENCE-GLUING-rank8-v1.md | `2c5f97ecb50a687d5986c8140a9106a127b19b5373fe3efefd6d0e98c9ff8fe9` |
| rook-positive-pairs-closure-v1.md | `aa0c4966efa8009d4e8dcd7afb8c4a0f76498b1c492c93dedf55887babbfe743` |
| rook-three-pairs-closure-v1.md | `3ca0eb7adb0de03cc0a5103fcab4fb11535766811ca5ae7abf7979022d3a86b4` |
| rook-two-pairs-full-closure-v1.md | `71626e32c1d4b5fbc45a7e7ff89bcf65942aa27a940aa2c180d9d3f49871e734` |
| rook-pair-duality-and-coverage-v1.md | `279fd3710fd7128d2f3e255cc65bfaf96ef28a4b22e381ccd0180d70b92b1e4b` |
| axial-negative-paw-coefficient-erratum-v1.md | `3180578116c9e3c6a89b037042d59870cdaf2b59c0a1aafdf25a32bc5432f524` |
| axial-complete-route-packet-v2.json | `1988618289062f58216a8c1a6dff8b370ce8a8f414ed3d08355a89497ccfaf11` |
| axial-negative-paw-local-ring-erratum-v1.md | `694d0d709ea56b45f19fef146d9aed8499f67cf75340713fc8a0e498ea09427b` |
| axial-complete-route-packet-v3.json | `693406928e8261208cd0eccac46f50709a972d72673e5a5c2027063f50cf3c19` |

Fresh public primary-interface reads, not merely author abstracts:

1. Et-Taoui [1409.4282v1](https://arxiv.org/html/1409.4282v1), §2.1 actual character construction and §2.3 Theorem2/Corollary3, including the theorem proof. For q9, k5, the theorem's `c=k-2+(k-1)Re(w^2)` is `3+4*(-3/4)=0`, giving `CC*=8I`. This supplies an explicit core, NOT a classification of every conference9 matrix. The separate real-character identities `Q1=0`, `Q^2=9I-J` agree with the actual rook graph; they are not assumptions about physical phases being real.
2. Zhang–Cao [2608.29201v2](https://arxiv.org/html/2608.29201v2), Introduction's ray/cardinality convention, Definition1.1, Theorem1.3's explicit order10 exception, and Lemma2.2's actual one-resolution forward/converse construction. The full target requires row/column ONBs, one partition into ten ONB transversals, and 100 distinct rays modulo phase. H0's uniform line-disjoint overlap1/8 and the two chosen conference classes are extra route assumptions, not that definition.

No novelty screen or full-paper classification theorem is inferred from these interface reads. The author is not offering a maximal-cardinality witness, so finite-witness execution is neither claimed nor substituted for this written obstruction review.

## 3. Phase bridge, fixed-point descent and genuinely different first orientation

In the H0 local triple, each transition is a conference matrix divided by sqrt8. Normalizing the first transition leaves the other as `D*P*C*P^T*E/sqrt8`. Independent permutations on its two sides must be inverse because its unique zero diagonal is aligned; this does not remove independent D/E phases. Right E factors cancel only from the designated zero equations. Thus delta remains the FULL nine-dimensional complex unit torus.

The axial rho is not a Q0 automorphism: `Q0_(1,4)=+1` whereas `Q0_(rho(1),rho(4))=Q0_(2,7)=-1`. Therefore `P_rho*M` cannot be silently treated as the old symmetric matrix. All four rho pairs are first-rook-positive, unlike central inversion's two. That invariant under literal first-core automorphisms establishes a different fixed orientation; it does not establish inequivalence under every possible conference operation or make the new orientation WLOG.

Put `u=(-3+s)/4`, `v=(-3-s)/4`, so `uv=1`, `u+v=-3/2`, `u-v=s/2`. Coefficients of M lie in `R=Z[1/2,s]`. Under `s->0`, `1/2->4` into F7, both u,v become1. Hence

    N=J-I-P_rho+Fix(rho)

is the reduction for EVERY second P. For `Nz=0`, let S be the coordinate sum. The fixed equation gives `z0=S`; each rho-pair sums to S. Summing yields `S=5S`, so `S=0` in F7 and `z0=0`; the reduced kernel is exactly rho-odd. This reduction acts on coefficients, never on arbitrary unknown phases.

For a projectively K-valued phase vector, `K=Q(s)`, clearing denominators gives nine integral coordinates of equal positive norm `a^2+7b^2=c`. If7 divides c, every a is divisible by7 and division by s stays integral: `(a+bs)/s=b-(a/7)s`. Remove powers of7 until c is nonzero modulo7. Reduction then forces the fixed coordinate's norm to be0 modulo7, contradiction. This excludes projectively K-valued unit vectors in ANY kernel dimension. It does NOT itself exclude unrestricted complex torus points in larger kernels.

If `rank_K M>=8`, rank9 is immediate and rank8 has a one-dimensional K-kernel whose scalar extension is the entire complex kernel. Equal physical moduli would give the forbidden equal K-norm vector, even for transcendental common scalars. This is the correctly scoped rank8 exclusion used below. Every invocation in the axial packet has been rederived at this fixed rho; no old acceptance label is an additional premise.

## 4. Complete second-grid coverage and first-order classification

Source translations normalize p(0)=0 without changing Q1 itself. The rook graph has automorphism group order72, point stabilizer8, so there are `8!/8=5040` literal second cores. Its 105 raw matchings split by rook count as `(8,28,33,28,8)`. The written disjoint-edge count is `C(14,2)-4*C(3,2)-4*C(4,2)=55`; each pair extends in3 ways, giving the second moment165 and the displayed signature counts. Each raw matching contributes48 literal tables.

Only the old SECOND-grid root catalogue is imported. The old central-route solution-preserving complement map need not commute with the axial rho and is NOT used to transfer its old no-go here. For catalogue purposes alone, the literal second set is closed under Q1 negation by a source nonsquare multiplier; all negative families are then actually treated by the new arguments.

The A2⊕A2 pair-root products give all nine shapes listed in the leading-reduction file: triangles plus isolate with magnitudes222 or211, two disjoint unit edges, all-light K4, one-heavy K4, paw, one-heavy diamond, two-heavy K4, weighted K2,2 of2112 pattern, and all-heavy signed K2,2. Pair labels/orientations are retained. I checked the actual parallel and perpendicular diamond endpoint constructions: its heavy edge is incident to a degree2 vertex, NOT the degree3-degree3 edge. That incidence is essential for the new first-H triangle argument.

The new first `A0` is the positive weight2 triangle on b,d,e, with H isolated. Let `L=A0+A1`.

- H-degree3 cases cannot cancel all three old B-triangle edges: the genuine catalogue has at most two heavy edges there. A nonzero principal triangle remains.
- Both K2,2 shapes give an unchanged2 edge between H's neighbours. The matching shape leaves a B-triangle. A degree2-H diamond has a LIGHT edge between its neighbours, hence cannot cancel2.
- A degree2-H paw can avoid its H-triangle only when the opposite edge is heavy-2. The remaining cross determinant is `a*(2+p)-2b`, `a,b,p=±1`; it is a nonzero integer of magnitude at most5, hence nonzero modulo7.
- If H is paw pendant, a heavy cancellation incident to the hub leaves a path4 with nonzero endpoint-weight determinant. Only the heavy-OPPOSITE-hub star **P** remains.
- For H on a second triangle, the only potential four-cycle failure has equal H-incident weights and opposite heavy-2 edge; its triangle product is negative. This is **T1**.
- For H also second isolate, only triangles with at least one heavy-2 cancellation remain, **T0**.

Thus EVERY genuine second core either has leading rank>=3 or belongs to T0/T1/P. No arbitrary signed graph beyond the actual root catalogue is needed, and no leading singularity is promoted to an actual low-rank witness. Nonzero minors modulo7 supply actual rank>=8 by the local even block and the leading odd coefficient.

## 5. Nonsymmetric block algebra and closures of T0/off-axis T1

The actual unnormalized metrics are `G_E=diag(1,2,2,2,2)` and `G_O=2I`. For real symmetric Qj,

    Qj=[Ej Bj; Bj^T*G_E/2 Oj],   Oj=-Dj+Aj.

Here Bj is the Q mixed block, not an operator Schur coefficient. The first data in pair order H,b,d,e are

    D0=I, A0=2*(triangle on b,d,e),
    B0=b0*e_H^T, b0=(0;0,0,2,-2),
    (E0)_pair=I-2*(e_H*e_b^T+e_b*e_H^T).

These follow directly from the literal points, including the sign of each diagonal-pair mean. With `o` denoting entrywise product, the exact gluing expansion is

    M=N+s*M1+s^2*M2,
    M1=(P_rho*Q1-Q0-D1+D0*P_rho)/8,
    M2=(N-Q0 o (P_rho*Q1))/8.

Writing the OPERATOR blocks as `[A B; C D]` gives

    B=s*(B1-B0)/8+s^2*B^(2),
    C=-s*(B1+B0)^T*G_E/16+s^2*C^(2),
    D=-s*(A0+A1)/8+s^2*D^(2).

In particular C is NOT the negative metric transpose of B. I derived the pair curvature formulas by the literal 2×2 sum/difference transform:

    16 D^(2)=E0 o O1-O0 o E1+B0 o C1-C0 o B1,
    16 B^(2)=O0 o C1-E0 o B1-B0 o E1+C0 o O1,
    16 C^(2)=E0 o C1-O0 o B1+B0 o O1-C0 o E1.

The Cj inside these three pair formulas are Qj pair blocks `Bj^T`, not the operator C. Fixed row/column factors are separate; they cannot be treated as norm2 pair coordinates.

The even A0-inverse in the paper is correct. For a Q mixed column h, `h0+2*sum(h_pair)=0`, and

    e0^T*A^(0)^-1*h=-7*h0/8,
    h^T*G_E*A^(0)^-1*h=-h^T*G_E*h/2-7*h0^2/16.

The nonsymmetric Schur matrix consequently has second coefficient

    D^(2)+(B1+B0)^T*G_E*A^(0)^-1*(B1-B0)/128.

All denominators used as local units here are nonzero modulo(s). A first odd minor of rank2 has inverse order s^-1. Restrictions to its exact leading radical determine the next coefficient; later elimination cannot change an earlier nonzero power of s.

### T0 axis: actual higher kernels, not a false rank8 shortcut

For a shared literal y-reflection g, M commutes with g. Its fixed subspace has dimension6, and the reduced restricted kernel is only `span(e1-e2)`, so actual invariant-kernel dimension is at most1. Averaging a hypothetical delta over g preserves the THREE unit coordinates0,1,2, not the moduli of vertical means. A K-line there would have three equal positive norms. Clear all coordinate denominators, divide by s while every constant coefficient is divisible by7, and stop when the reduction is nonzero. Its restricted reduced kernel has nonzero1/2 coordinates and zero0 coordinate, contradicting those three equal norms. The other six averaged coordinates never need unit norm.

Axis same-isolate cores genuinely share this reflection. For `C'=conjugate(C)`, paired rows of M are identical and reduction has rank5, so the actual full rank is5. This four-dimensional complex kernel is excluded by the smaller invariant-space argument, not mislabeled rank8. The shared-reflection count48 follows from centralizer96, four relevant point-stabilizer reflections, divided by8 duplicate representatives.

### T0 positive off-axis and positive P

For heavy leaves i,j and hub k, take the displayed v with leaf coordinates `(1,-3)` or `(3,-1)`. It is an exact leading-radical vector with `B0*v=0`, norm-square10, and `|O1*v|^2=42`. Thus `(B1*v)^T*G_E*(B1*v)/2=48`. Direct v-v curvature is0 from the actual even leaf entries. The feedback is therefore `-48/128=-3/8 mod(s)`, nonzero. This uniformly supplies the eighth actual pivot in both positive families; unused mixed entries and phase freedoms were not fixed.

### Negative off-axis T1

On `u=2e_H-ae_K`, `v=e_i-e_j`, both Q mixed blocks annihilate v. `O1=-O0` on the leading radical makes the scalar feedback difference0 modulo(s); cross feedback with v is0. The remaining form has cross entries `c+z,c-z`, where

    c=-a*v_b/4,   z=-h*(b0_i-b0_j)/8.

I obtained c from the H-b even edge and z from the two explicitly retained skew Hadamard terms. For K=b, c0 and z=±1/2. For K=d/e, c,z are each±1/4 and at least one cross entry survives. Rank at least one in this second form is sufficient for actual rank>=8; symmetry or nonsingularity of the entire second form is not falsely assumed.

### Negative off-axis T0

For k=b, the actual shared x-reflection has fixed-space dimension6 and reduced N-rank4. On its two-dimensional reduced kernel, L has matrix `[0,2(2+a);2+a,0]`, invertible modulo7. The restricted actual matrix is invertible, whereas averaging preserves nonzero coordinate0: contradiction.

For k=d/e, choose i=b and let v=e_i-e_j. The whole odd D kills v on both sides. Both first mixed couplings kill v exactly. The actual pair curvature cancels on v, but the FIXED coordinate gives

    B^(2)*v=(h/2)e0=r,
    v^T*C^(2)=-(h/4)e0^T=l.

Thus the exact v-v Schur entry is `-s^4*l*A(s)^-1*r`, with leading coefficient `-3/32`. Regularity makes its nominal s3 cross coefficients divisible by7=-s²; all cross entries to the two leading odd pivots start at least s4. Their feedback starts at least s7 and cannot cancel this s4 pivot. The pair/fixed factors1/2 and1/4 are independently retained. This closes all T0.

## 6. All96 negative-axis cores and every exceptional prototype

The complete parameterization is `(K,J,sigma modulo simultaneous reversal,epsilon)`, giving `4*3*4*2=96`. The full E/O/B blocks uniquely specify the actual core, not merely its odd graph. The disjoint account is

    24 K=H +36 noncritical signs +24 nonexceptional roles +4 R +8 S.

For the critical signs, `u=e_H+t*e_K`, `v=e_i-e_j`. The second cross coefficient is `(t/4)*(v_b-v_J)`, on both sides. I checked the symmetric even-edge contribution and that the mixed skew support is H-K and restricts to0. Exactly R:(K=b,J=H) and S:(K=d/e,J=b) escape. The literal x/y reflection actions printed in the source give the two R two-element orbits and the two S four-element orbits; these preserve the first C/rho and transport arbitrary phases, not phase symmetry assumptions.

For reproducibility of the literal row checks, the actual first positive-character neighbour sets are

    N0={1,2,3,6}, N1={0,2,4,7}, N2={0,1,5,8},
    N3={0,4,5,6}, N4={1,3,5,7}, N5={2,3,4,8},
    N6={0,3,7,8}, N7={1,4,6,8}, N8={2,5,6,7}.

For a negative core `Q1_xy=-Q0_(p(x),p(y))`, mask t=i,rho(i). At every other entry M is v if both `t in N_i` and `p(t) in N_(p(rho(i)))`, u if neither, and1 otherwise. This direct rule, not the auxiliary paw coefficient table or an executable, regenerated the consumed raw equations.

- **R, p=(0,3,6,1,4,5,2,7,8):** the actual common negation g_n commutes with rho. I reconstructed all five even equations using row representatives0,1,3,4,7, and the complete four-dimensional odd block. The even solution is exactly the displayed `(a=b,c,d0)` times z0. Subtraction gives a=b; the remaining three independent equations give `a=(3+s)z0/8`, `c=(83-7s)z0/112`, `d0=(-5-7s)z0/28`. The odd kernel is `span(1,1,-s/2,0)`, so coordinates7/5 have no odd correction. Their forced squared norm ratio is `(25+343)/784=23/49`. Even/odd ranks4+3 verify actual rank7; no larger complex kernel is ignored.
- **R reversal, p=(0,3,6,2,4,5,1,7,8):** direct even rows0,4,7 give exactly the three displayed equations. Their difference is `(7/2)(a+b)=0`, then c+d0=0 and z0=0. Averaging preserves coordinate0; other mean moduli are irrelevant.
- **S, p=(0,4,7,3,1,5,6,2,8):** p is involutive and commutes with rho. The factor-exchange identity implies `M*P_p=(left permutation)*M`, hence kernel invariance, not a false commutation of M and p. The three anti-invariant raw rows force its anti-kernel0. Actual full kernel vectors are p-even. I regenerated rows0,1,2,3,5 and eliminated their sums to `(19+3s)a+26b=16` and `e0=(381+49s)/364+(7-9s)a/52`. From physical `|a|=|b|=1`, the first gives `Re((19+3s)a)=1/8`. From `|e0|=1`, the second gives a rational value of `Re(beta*a)`, `beta=(-105-943s)/4732`. The two real coefficient vectors have determinant-17602. Thus Re a and sqrt7 Im a are rational, so a lies in K; the raw sums and the nonsingular difference equation put every other normalized coordinate in K. Only AFTER these actual unit constraints is the projective-K descent applied.
- **S reversal, p'=(0,4,7,3,2,5,6,1,8):** source normalization is `q=g_y COMPOSED AFTER p'`, exactly `(0,7,4,6,2,8,3,1,5)`. It is the same core, an involution commuting with rho. I regenerated its five q-even raw equations at rows0,1,2,3,5. Eliminating c,d0 gives the displayed a+b,b,a formulas and finally `-(133+110u)z0/32=0`. The nonreal u makes its coefficient nonzero, forcing the retained fixed coordinate0 to vanish. No unit moduli of averages are required.

All prototype denominators used for ordinary K-linear elimination are nonzero complex numbers; their factors7 are NOT called local-ring units. The reflection coverage makes these literal arguments exhaustive for the twelve exceptional roles. It does not normalize away a first orientation or any unknown phase.

## 7. Negative paw: actual source defect, full downstream trace and corrected fourth-order proof

The parallel-leaf heavy-opposite-hub geometry is the literal one in the source. With i the vertical leaf in the H pair's nonzero column, `a0=h*d0`, `p=-e0*d0`, the entire CORRECT mixed table is

    B1_H: fixed -2e0; pair k -e0, i 2e0, others0;
    B1_k: fixed -2d0; pair H d0, i -d0, j +d0, k0;
    B1_i=B1_j: fixed -2h; pair k h, others0.

### Why M1 is an actual defect and not optional

For A+ below, k=d, `p(4)=6` and `p(7)=5`. In the negative literal Q1, `Q1_(0,4)=-1`, `Q1_(0,7)=+1`. Their odd fixed-row difference is-2. More generally that difference is-2d0. Independently, the hub column's three pair entries sum to d0, so `h_fixed+2sum(h_pair)=0` forces-2d0. The erroneous0 makes that claimed exact column and regularity false. The adopted coefficient erratum fixes precisely this substantive statement; it is not an unexplained waiver because a later scalar happened to agree.

### Exact operator dependency/nondependency

Let eta_a be the first fixed-row pair mean: `eta_H=eta_b=+1`, `eta_d=eta_e=-1`. The hub fixed coefficient changes by-2d0. The OPERATOR mixed blocks therefore change by

    Delta B = [ -s*d0/4+s^2*eta_k*d0/4 ] e0*e_k^T,
    Delta C = [  s*d0/8-s^2*eta_k*d0/8 ] e_k*e0^T.

These follow respectively from `B^(1)=(B1-B0)/8`, `C^(1)=-(B1+B0)^T*G_E/16`, and the actual fixed-row/column curvatures `B^(2)_(0,a)=-eta_a*(B1)_(0,a)/8`, `C^(2)_(a,0)=eta_a*(B1)_(0,a)/16`. They exhibit ALL changed first/second-order mixed entries, with the norm1/norm2 factor distinguished.

A(s) is unchanged: Q1's even means are unchanged and the first fixed row is constant within each rho-pair. D(s) is unchanged because it uses pair blocks only. The corrected right/left radical vectors below have ZERO hub component. Therefore

    (Delta B)*v_R=0,     v_L^T*(Delta C)=0

EXACTLY, not just modulo(s). Their self-Schur entry is consequently unchanged through all orders. Cross couplings to the two leading odd pivots can change, but they still start at s3: corrected mixed blocks are O(s), whereas the corrected radical couplings are O(s2). Feedback through an order-s odd pivot starts at s5. Thus the s4 scalar is genuinely unaffected, for a demonstrated structural reason, not by ignoring the error.

The final sixteen proofs are also independent of this erroneous auxiliary entry: their raw rows were regenerated directly from p and the actual chi rule in section6. Those rows already use the actual nonzero fixed hub difference. No old erroneous table was used to authenticate them.

### Corrected fourth-order reconstruction

Let `v=e_i-e_j`, `c=2+a0`. Both Q mixed blocks kill v, but direct odd curvature does NOT: `D^(2)v=-(1/4)e_k`, on both sides. Its symmetric H-k numerator is `n=-2p` when b=k, otherwise0; its skew numerator is `q=b0_k*d0`. The exact right/left corrections are

    beta_R=4s/[-2p+s(n+q)],
    beta_L=4s/[-2p+s(n-q)],
    v_R=v+beta_R e_H,   v_L^T=v^T+beta_L e_H^T.

They kill D(s) exactly on their respective sides. As the new local-ring erratum correctly states, the denominators are units, beta has valuation1, and the independent changes are elementary unipotent changes with inverse subtraction. Nothing divides by beta. This resolves m1 without pretending beta itself was a unit.

Direct fixed/pair curvature gives

    r=B^(2)v: r0=h*(eta_i-eta_j)/4, r_pair=-(d0/4)e_k,
    l=v^T C^(2)=-(1/2)r^T G_E.

The unchanged pair entries of the HUB column, not its erroneous fixed entry, enter this pair calculation. Leading corrected couplings are

    rhat=r-(p/4)(B1_H-b0),
    lhat=l+(p/8)(B1_H+b0)^T G_E.

Only the unchanged H and leaf columns enter these vectors. With `x=r-(p/4)B1_H`, `y=(p/4)b0`, the actual entries are

    x0=xi=h*(eta_i-eta_j)/4-d0/2,
    x_pair=(d0/2)(e_i-e_k), y0=0, y_pair=(p/4)b0_pair.

Both pair sums vanish and each pair squared norm is1/2. The stated A-inverse yields `x^T G_E A^-1 x=-3xi^2/4-1/2`, `y^T G_E A^-1 y=-1/2`. Its self-adjointness cancels the two cross terms, giving the fourth-order scalar `-3xi^2/8`. Right/left corrected vectors kill D exactly; their cross entries to leading odd pivots start s3, so feedback starts s5 and cannot cancel this s4 certificate. This argument remains nonsymmetric throughout.

Since `xi=d0*[a0*(eta_i-eta_j)-2]/4`, all b=k cases close, as do b=i with a0=-1 and b=j with a0=+1. The surviving conditions are precisely `(b=i,a0=+1)` or `(b=j,a0=-1)`.

### Counts and the mandatory older erratum

The entire paw support has16 raw embeddings/768 literal cores. Only the parallel-leaf heavy-opposite-hub subtype has8/384; it is the `u=r` branch in the actual three-rook geometry, plus its transpose. The other subtype has heavy incident to the hub and was already closed by the leading path4 argument. It is not silently omitted from P.

On the relevant subtype, fixing pendant H and heavy sign-2 leaves48. Equivalently choose k among3, geometric leaf i among2, and three independent pair signs among8:48. The nonzero fourth-order scalar closes32. Each residual alternative has two hubs and four(p,d0) choices, giving8+8=16. The coefficient repair changes neither this genuine geometry nor the xi formula. The source's admitted fifth-order cancellation is NOT reused as a new pivot or an unproved residual closure.

## 8. All four literal sixteen-core residual orbits

The eight raw parallel-leaf matchings form one free orbit of the source point stabilizer8: coordinate signs select r,a, and interchange selects which direction has one rook pair. Thus source-only normalization to the printed `r=a=1,b=2` geometry changes no Q1. Geometric i remains distinct from j. The literal representatives are exactly

    A+ (0,4,3,1,6,2,7,5,8),
    A- (0,3,4,1,6,2,7,5,8),
    B+ (0,4,3,8,6,7,2,5,1),
    B- (0,3,4,8,6,7,2,5,1).

The negative notation is an actual permitted second core: source multiplication by nonsquare1+alpha has tuple `(0,4,8,5,6,1,7,2,3)` and changes Q0's sign. Each tuple therefore also has a positive-Q relabeling form. No nonexistent conference core was manufactured.

I regenerated every raw row consumed in the four proofs from the direct neighbour-set rule, with row coverage A+:1,2,3,6,5,8; A-:those rows plus0; B+:1,2,3,6,5,8; B-:1,2,3,5,7,0,4. The exact eliminations are as follows.

- **A+:** the two row differences force `z7=t`, then `z4=t`, `t=z0`. Writing `S=z3+z5+z6+z8`, the two H rows give `3v*t+u*S=0` and `(u+2)t+S=0`. Their elimination is exactly `-(7/2)(1+u)t=0`. Therefore every kernel vector has fixed coordinate0 zero.
- **A-:** the same differences force z4=z7=t. The two H rows give `X=Y=((1+3s)/4)t`, where X=z3+z6, Y=z5+z8. The coefficient has squared norm4. For actual unit phases, equality in BOTH triangle inequalities forces all four terms to `q*t`, `q=(1+3s)/8`, norm1. The remaining raw rows give `u*z1+z2=(1/2-2q)t` and `v*z1+z2=-(1+u+q/2)t`. Their nonzero u-v difference forces both remaining normalized phases into K. All normalized coordinates are now in K, contradicting the actual fixed-coordinate descent. This is a genuine complex-unit equality argument, not an assumed phase field.
- **B+:** z7=t. With A=z1+z2, X=z3+z6, Y=z5+z8, B=z4, raw rows give `X=-B-(1+u)t-A`, `Y=-B-(1+v)t-uA`, and `(u+1)A=(13/4)t-vB`. The other H row reduces to `(12+23u)t+2(1+6u)B=0`, so `B/t=(-45+7s)/32`. Its squared modulus is `(2025+343)/1024=37/16`, not1.
- **B-:** z7=t, X=A, `Y=-B-uA-(1+v)t`, `A=-(6+7u)t/4`, `B=(v-u)z1+A-vt`. The sum of rows0+4 is `(4u+1)t-7(2+u)z1+(5-3u)A=0`. Consequently `z1/t=-(94+65u)/[56(2+u)]`. For real a,b, `|a+bu|^2=a^2+b^2-(3/2)ab`; the two exact norms are3896 and6272, ratio487/784, not1.

The safe FIRST reflections act by `g_y:(k,p,d0)->(k,-p,-d0)` and `g_x:(d,p,d0)->(e,-p,d0)`. Neither changes the b=i versus b=j branch or its a0. Each of the four representatives has a four-element orbit; the two in each branch are disjoint and cover that branch's eight cases. These are actual permutations preserving first C/rho. They transport unrestricted phases rather than requiring an unknown delta to be reflection invariant. Thus the literal proofs exhaust the16, not just four selected numerical examples.

## 9. Composition and evidence boundary

Leading catalogue exhaustion plus the actual T0/T1/P arguments covers all5040 second literal cores. Every use of rank>=8 is supported by a genuine leading or later local-ring pivot and the general norm theorem. Every surviving lower-rank prototype instead receives an actual whole-kernel, fixed-coordinate or physical-unit-norm argument. A singular leading reduction is never called a phase witness; an auxiliary real Q calculation is never called a reality restriction on delta.

The amended written verdict consumes the COMPLETE corrected chain, including the existing subtype count repair AND the two reviewer-triggered source repairs. It does not label the original wrong coefficient passed, and it does not retroactively claim a review before the repairs were read. Parent integration must retain the original findings and all mandatory overlays.

No scientific source was imported or executed, no syntax/compile/test/checker/enumeration/solver/arithmetic runtime or old assay was run, and no nested agent/model CLI/account change/Git operation occurred in this review. Executed operations were source/file reads, static public-primary reads, cryptographic metadata hashes and actual clocks. All algebra above is written reconstruction, NOT formal/kernel verification or an exercised finite assay. N4's UNKNOWN/absent-process receipt grants no permission to retry anything.

Correctness support is at this explicitly scoped in-harness supplied-proof level. Import trust is the named explicit core and actual ray/transversal definitions. Scope remains fixed first C and axial rho, all second P and arbitrary D/E. Novelty and broader significance remain uncertified. No parent, human, blind, formal or cross-vendor acceptance is implied by this return.
