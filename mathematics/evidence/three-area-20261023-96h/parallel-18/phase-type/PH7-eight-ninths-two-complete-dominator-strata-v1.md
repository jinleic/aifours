# PH7 at8/9: two complete actual dominator representatives, with arbitrary feedback

Actual `/bin/date` returned BEFORE this manuscript: **Sun Oct 25 21:17:43 PDT 2026**. MathResearch96h-2, math-1. AUTHOR-WRITTEN CANDIDATE; new independent whole-body reconstruction NOT PERFORMED. No scientific interpreter, calculator, eval kernel, symbolic/numerical program, enumeration, solver, replay, native experiment, model CLI or nested agent was used for this manuscript. No scientific machine checks are claimed.

## 1. What is proved conditionally, and what is not

Fix c,d>0, a=c+d, b²=8d²/9,

    D5(s)=(s+c)((s+a)²+b²)², K=D5(0)>0.

Retain the original problem: an ACTUAL seven-state phase-type pair must have alpha>=0, alpha1=1, T Hurwitz Metzler, omega=-T1>=0 and

    alpha(sI-T)^(-1)omega=K/D5(s).

At the named B6/normal-form/shared-identity imports below, existence of ANY such pair is equivalent to existence in the union of just TWO complete actual representatives:

    A: m=5,n=1, delta_R=3,delta_S=1, deg N_R=2,deg N_S=0;
    B: m=3,n=3, delta_R=2,delta_S=2, deg N_R=1,deg N_S=1.

These are complete unrestricted matrix classes, NOT selected holding-rate families. All actual principal blocks, input and exit vectors, backward D, middle returns r/f and PH row identities remain. No holding equality, upper/lower rate rectangle, hidden-root localization, selected path weights, companion form or quotient-positive cone is inserted.

A nonreal hidden quadratic can occur ONLY in A. A also includes real hidden quadratics. B has two real negative hidden roots, with equality/multiplicity allowed. Nothing here asserts every real-hidden representation belongs only to B, or that A and B are disjoint.

The new step beyond the earlier nine-allocation/five-reversal-representative interface is a complete actual cut-movement and prefix-separator proof. It reduces a topology-unrestricted feasibility problem, not its answer. There is NO PH7 witness at8/9, NO full8/9 empty-intersection certificate, and NO promotion of the minimum beyond{7,8}.

## 2. Named imports and source/proof chronology

Named load-bearing written imports, not reconstructed here as their original entire lower-bound proofs:

1. B6, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`: orders<=6 excluded at z>1/2. It supplies the no-unreachable-state consequence below. This manuscript does not re-prove B6 or turn it into a formal result.
2. Actual dominator form, `PH7-dominator-normal-form-v1.md`, SHA256 `5e259982c3fe8f762acc0546080aa87afec405e0cbc34b00afc460f01b39f846`,132LF/11415B: relative degree5 gives an internal dominator and the actual common block form, with all feedback and row ties. Complete132LF body including ending was actually reread before this manuscript.
3. Shared identities/nine allocations, `PH7-dominator-shared-block-identities-v1.md`, SHA256 `941ea246ba96e00e820021733b0d716e79cc103807a86f97ee5b31dfabf5b969`,227LF/13893B. Complete227LF body including ending was actually reread before this manuscript. Its same-matrix elimination, boundary-numerator positivity and degree identities are retained, not silently promoted.

The older unreviewed reversal candidate is `PH7-time-reversal-five-orbits-v1.md`, SHA256 `6e539a6887c6d54f97658dad9536a738991f8df2e951f89ef58bbe8aa7d28dc4`, ACTUAL154LF/7887B. Its complete154LF body and ending were actually reread. Sections4-5 below reproduce its occupation, physical reversal and numerator scaling rather than treating an old verdict as a correctness proof. The new cut movement/prefix separator is not claimed to have been proved in that older paper.

**Additive checkpoint qualification.** Checkpoint055 mistakenly described that older source as190LF:190 was a requested read-range endpoint, NOT a measured body count. That count is withdrawn in `checkpoint-055-time-reversal-LF-inventory-addendum-v1.json`; the actual metadata was observed later as154LF. No extra36LF receive coverage credit, and metadata chronology is not backdated.

**Additional logical refinement to checkpoint055.** After time reversal, a valid actual shared-block partition need not be the canonical set reachable from the new input before the center. Therefore the checkpoint's blanket phrase about a new canonical reachable partition for the constant-side move is TOO STRONG and withdrawn. Section6 uses a literal permutation with a proved zero upper-right block; it does NOT need canonical reachability. In the asymmetric linear/linear argument, a canonical reachable set is selected explicitly only where needed. This closes that checkpoint proof gap without altering a source or assuming unreachable phases away.

All prior owner exactness/cadence/opaque/documentary findings, mandatory v9/v10/v11/HOLD and later parent process overlays remain. In particular the fourth private numeric scout and every inference consuming it remain UNADMITTED/ZERO credit. This proof uses fresh symbolic graph counts, occupation identities and literal matrix algebra, NOT that scout or a reconstructed numeric campaign. No clean-thought, blind-review, continuous-runtime or exhaustive-census claim is made.

## 3. Literal actual interface, not free factors

The imported form, after an actual permutation, is

    T=[ A     b       0
        r^T  -lambda  t^T
        D     f       F ],
    alpha=(alpha_R,0,0), omega=(0,0,omega_S)^T,
    m=dim A>=1,n=dim F>=1,m+n=6.                       (1)

A,F are actual Hurwitz Metzler principal blocks. Every cross block displayed is nonnegative. The PH constraints are

    alpha_R>=0,alpha_R1=1;
    b=-A1>=0;
    lambda=r^T1+t^T1>0;
    omega_S=-D1-f-F1>=0.                              (2)

Write

    a_R=det(sI-A), a_S=det(sI-F),
    U=adj(sI-A)b, V^T=t^T adj(sI-F),
    N_R=alpha_R U, N_S=V^T omega_S.

The actual characteristic and numerator identities are

    P7=(s+lambda)a_R a_S-a_S r^T U-a_R V^T f-V^T D U,
    alpha adj(sI-T)omega=N_R N_S.                      (3)

They come from THAT SAME T and its physical exit. For the target,

    P7=D5 Q2, N_R N_S=K Q2, Q2 monic Hurwitz degree2.   (4)

Both actual N factors have positive leading and constant coefficients, and nonnegative coefficients throughout. In particular N_R(0)=a_R(0); this factor cannot be freely scaled without the input/row constraints.

Let delta_R be the shortest positive I-to-center path and delta_S the shortest center-to-E path, where I=supp(alpha),E=supp(omega). They satisfy

    delta_R+delta_S=4,
    deg N_R=m-delta_R, deg N_S=n-delta_S,
    1<=delta_R<=m,1<=delta_S<=n.                     (5)

The upper-right zero block and the separator imply that a simple center-to-E path cannot enter R: once in R it must revisit the center before entering S. Thus all its post-center vertices are in S. An I-to-center segment similarly lies in R until its endpoint. This remains true for a valid noncanonical shared partition.

The full integer table, with no topology or rate enumeration, is

|m|n|delta_R|delta_S|deg N_R|deg N_S|
|---:|---:|---:|---:|---:|---:|
|1|5|1|3|0|2|
|2|4|1|3|1|1|
|2|4|2|2|0|2|
|3|3|1|3|2|0|
|3|3|2|2|1|1|
|3|3|3|1|0|2|
|4|2|2|2|2|0|
|4|2|3|1|1|1|
|5|1|3|1|2|0|

The transformations below act on ACTUAL pairs, not on this table alone. No new numeric testing of any row is claimed.

## 4. Actual PH time reversal: all boundary and positivity identities

Any actual target PH7 is initial-reachable in all seven states. Otherwise its reachable block is a smaller PH representation of the same distribution, contradicting named B6. Define the occupation column

    xi=(-T^T)^(-1)alpha^T
      =integral_0^infinity exp(T^T u)alpha^T du.

Hurwitz Metzler T makes the integral finite/nonnegative; reachability and a positive path from some initial phase make every xi_i strictly positive. Let V=diag(xi). Then

    T_rev=V^(-1)T^T V,
    alpha_rev=omega^T V,
    omega_rev=V^(-1)alpha^T.                          (6)

T_rev is Metzler/Hurwitz and

    T_rev1=V^(-1)T^T xi=-V^(-1)alpha^T=-omega_rev.

Also alpha_rev1=omega^T xi=alpha(-T)^(-1)omega=alpha1=1. Hence this is an ACTUAL PH pair with its own literal exit, not an arbitrary transpose. Its transfer equals

    omega^T(sI-T^T)^(-1)alpha^T
      =alpha(sI-T)^(-1)omega.

Its characteristic polynomial and full hidden Q2 are unchanged. Positivity of diagonal scaling means the transition graph is exactly reversed. Original I and E exchange as positive supports, and any internal dominator stays an internal dominator in reversed path order.

The elementary semigroup integral and finite directed flow facts used here are ordinary classical imports. They are not machine/kernel verification. The model-specific normalization and graph consequences are proved explicitly in this manuscript.

## 5. Every actual block and actual numerator under reversal

Partition xi=(xi_R,xi_o,xi_S), V_R=diag(xi_R),V_S=diag(xi_S). Reorder (6) as old S,old center,old R. Then

    A_rev=V_S^(-1)F^T V_S,
    b_rev=xi_o V_S^(-1)t,
    r_rev^T=xi_o^(-1)f^T V_S,
    t_rev^T=xi_o^(-1)b^T V_R,
    D_rev=V_R^(-1)D^T V_S,
    f_rev=xi_o V_R^(-1)r,
    F_rev=V_R^(-1)A^T V_R.                           (7)

The new input and exit blocks are omega_S^T V_S and V_R^(-1)alpha_R^T. The three block equations T^T xi=-alpha^T imply EXACTLY

    A_rev1+b_rev=0,
    r_rev^T1+t_rev^T1=lambda,
    D_rev1+f_rev+F_rev1=-omega_(S,rev).

All feedback entries survive with positive scaling. The upper-right block is still zero, being the transpose of the original zero block. This is a valid actual partition even if it is not canonical reachable-set partition.

Adjugate similarity/transposition gives

    a_(R,rev)=a_S, a_(S,rev)=a_R,
    N_(R,rev)=xi_o N_S,
    N_(S,rev)=N_R/xi_o.                             (8)

For example the first is

    omega_S^T V_S [V_S^(-1)adj(sI-F^T)V_S]
       [xi_o V_S^(-1)t]
      =xi_o omega_S^T adj(sI-F^T)t=xi_o N_S.

Thus the product and degrees exchange with their actual scales. Dimensions and delta lengths exchange as well, because reversed positive boundary paths are the original positive paths in reverse. No localization Q2|a_R or Q2|a_S follows.

The nine rows therefore have five representatives: A=(5,1;3,1;2,0), U=(4,2;3,1;1,1), C=(4,2;2,2;2,0), D=(3,3;1,3;2,0), B=(3,3;2,2;1,1). Only U remains asymmetric after the constant-side argument next.

## 6. Constant post-numerator: move to the actual pre-exit dominator

Consider ANY actual valid form(1) with deg N_S=0. Then n=delta_S by(5). A simple center-to-E path has at least n edges and at most n vertices after the center, so its length is EXACTLY n and it visits EVERY S vertex. Choose one such positive path and label it

    o -> s1 -> ... -> sn,

where sn is an exit. There can be no other exit s_j with j<n: stopping there gives a shorter positive center-to-E path. Thus E={sn}. There can be no forward skip o->s_j for j>1 or s_i->s_j for j>i+1: follow the displayed prefix and suffix to obtain a shorter positive center-to-E path. All backward edges within S and all D/f feedback remain allowed.

Every simple center-to-E path therefore visits every S vertex. In particular, if n>=2 then v=s_(n-1) is an ACTUAL global internal dominator. Its only later forward state is sn. Permute the ACTUAL phases as

    R_new=(all phases except v,sn), center=v, S_new={sn}.

This is a valid actual shared form with m_new=5,n_new=1. Indeed no R_new->sn edge exists: original R->S was zero; o and all earlier S vertices cannot skip forward to sn by the previous paragraph. The only forward edge into sn is the actual v->sn, which is positive. The new center is neither initial nor an exit. No original entry, including every backward feedback, is removed.

**No canonical-reachability assumption is needed.** Some of the five new upstream phases may be reachable from the new input only after feedback through v/sn. They remain in the actual A5 block. The absence of an edge into sn, the literal PH row equations and all seven phases are preserved anyway. This is precisely why a free reselected canonical partition was NOT assumed after reversal.

The positive original shortest I-to-E path reaches v after3 edges and then sn after1. Conversely an earlier I-to-v path would yield an I-to-E path shorter than4 by following v->sn. Thus delta_R,new=3,delta_S,new=1, and the degrees are2+0. This is representative A. For n=1 the original form is already A by(5).

Consequently ALL degree2+0 representatives C,D,A reduce to A. A degree0+2 representative first undergoes actual reversal(6)-(8), then this actual constant-post move. No hidden-root type, asymmetric holding or physical input/exit case is lost.

## 7. The sole remaining asymmetric linear/linear row has another actual prefix separator

Take U: m=4,n=2,delta_R=3,delta_S=1,degrees1+1. The partition need not be canonical. Consider the finite positive graph on its four R phases plus o. It contains I in R, and every I-to-o path has at least3 edges. Every I-to-E path first reaches o; before first reaching o it cannot leave R, because R->S is zero.

There is an internal separator v in R\I on EVERY I-to-o path. Here is the full counting proof, including multiple initial phases.

Add a supersource joined to every I vertex and let o be the sink. Give all transition/source/boundary arcs capacity8. Split every R\I vertex with a capacity1 internal arc, while I vertices and o remain uncuttable with capacity8. An existing positive I-to-o path gives an integral unit flow. If its residual network has no augmenting path, the residual-reachable cut has capacity1; every capacity8 edge is excluded from such a cut, so the cut is one R\I split arc. That vertex is the required v.

If there is an augmenting path, augment by one and decompose the integral value2 flow into two source-to-o paths, discarding circulation cycles. They have disjoint R\I vertices. Trim each path to its LAST I vertex. Its remaining length is still at least3, because delta_R=3, and it has no other I internally. It therefore uses at least TWO R\I vertices. The two paths need at least FOUR different R\I vertices, whereas

    |R\I|=4-|I|<=3.

Contradiction. Shared or different initial endpoints do not help; no single-initial assumption was used. Thus v exists. Since all I-to-E paths must first reach o and their prefix passes v, v is also an ACTUAL global I-to-E dominator.

This proof does not discard any backward/cross feedback. It concerns first-hitting paths in the actual prefix graph, not a replacement generator. A walk avoiding v would contain a path avoiding v, so the separator is a true first-hitting condition.

## 8. Exact two-slack accounting after selecting that separator

NOW choose a canonical reachable set, but only at this explicitly selected v:

    R'=all phases reachable from I without visiting v,
    m'=|R'|, d=shortest positive I-to-v length.

Because v separates I from old o, neither old o nor either old S phase is in R'. Thus R' is a subset of old R\{v}. Let L=old R\(R' union{v}); then |L|=3-m'.

A simple v-to-old-o path cannot enter R'. Otherwise take its suffix from the first such R' state to old o, which avoids v, and prepend an I-to-that-state path avoiding v. This would be an I-to-old-o walk avoiding v, impossible. Hence that simple path uses only L and old o after v. Conversely a shortest I-to-v path lies in R' before v. The two shortest segments concatenate without shared states, so

    d+delta_(v,o)=delta_(I,o)=3.

Since v is neither initial nor old o, d is1 or2. At most |L|+1=4-m' vertices are available after v on the v-to-o path. Therefore

    m'>=d,
    4-m'>=3-d,
    e:=m'-d is either0 or1.                         (9)

These are exact vertex slacks of the actual graph, not rate inequalities. Equivalently the two nonnegative slacks of the old prefix add to its single extra vertex:

    (m'-d)+[(4-m')-(3-d)]=1.

The new cut at v has delta_R'=d and delta_S'=4-d: its post path must reach old o, then an exit in old S, and the disjoint shortest segments achieve that total. Its numerator degrees are e and2-e.

There are only the following cases, all handled physically:

### 8.1 e=0

The new cut has constant PRE numerator, degrees0+2. Its actual reversed pair has constant POST numerator. Section6 gives A, retaining all seven actual phases and every normalization tie.

### 8.2 e=1,d=2

Then m'=3,n'=3 and delta_R'=delta_S'=2. This is B directly, with actual linear/linear numerator factors. No further change or root assumption is made.

### 8.3 e=1,d=1

Then m'=2 and |L|=1. Write L={s}. The shortest v-to-old-o distance is2 and only the two post-v vertices s,old o are available. Thus v->s->old o is positive, and EVERY simple v-to-old-o path visits s. No v->old-o edge can exist, because its length1 would violate the actual distance2. Therefore s is another actual global dominator.

Move the center ONE actual edge from v to s. Its prefix is exactly R' union{v}, of size3: those phases are reachable from I without s, while old o and old S require s, and the only remaining old R phase is s itself. The I-to-s distance is2 and the s-to-E distance is2. Thus this is B. This argument does not set any of the surviving backwards feedback entries to zero; they are merely reclassified in the new actual blocks.

Sections8.1-8.3 exhaust(9). Therefore U always reduces to A or B.

## 9. Full iff and every actual coefficient/normalization obligation

The nine-row table is exhaustive at the named imports. Actual reversal reduces it to five representatives. Section6 sends the three constant-post representatives to A. Sections7-8 send the asymmetric linear/linear representative to A or B. The balanced representative is B already. Every step is either a literal permutation/reblocking of an actual T or its actual positive-occupation PH reversal, with no deleted phase or independently chosen exit.

Consequently original PH7 existence implies existence in A or B. Conversely each A/B actual solution of(1)-(4) is a literal actual PH7 solution: its T is Metzler with its stated negative row-sum exit; alpha is a probability row; the full characteristic D5Q2 is Hurwitz; and the full actual numerator KQ2 gives the target after cancellation. Thus the implication is an IFF, not only a necessary screen.

For clarity A can be written without any upstream ansatz as

    T=[ A5    b       0
        r^T  -lambda  t
        D     f       -v ],
    b=-A5 1, lambda=r^T1+t,
    omega=(0,0,v-D1-f)^T,
    alpha=(alpha_A,0,0), alpha_A1=1.

A5 is an ARBITRARY actual Hurwitz Metzler5x5 principal block. All r,D,f are nonnegative, t>0 and omega_7=v-D1-f>0. The actual shortest input-to-center distance is3. With a=det(sI-A5),U=adj(sI-A5)b and omega_7 as stated, the ENTIRE same-matrix equations are

    (s+lambda)a(s)(s+v)-(s+v)r^T U-a(s)t f-t D U
      =D5(s)Q2(s),
    t omega_7 alpha_A U=K Q2(s).                    (10)

No scalar coefficient may be redistributed independently of U,A5,b,alpha_A,r,D,f. The actual alpha_A U has degree2, and its value at0 is a(0). Q2 may be real or nonreal and need NOT divide a(s).

For B use arbitrary actual A3,F3 and ALL blocks in(1)-(2), with both shortest boundary distances2. Both actual N factors are linear with strictly positive leading/constant coefficients. Their product is KQ2, so Q2 has two real negative roots; repeated roots are included. Equations(3)-(4) in their entirety, not merely positivity of two free linear polynomials, are still required. Multiple actual initial and exit phases are allowed wherever these distance/row identities permit them. No assertion of unique middle path, fixed unequal holdings, regular source or restricted feedback graph is made.

## 10. Assurance and exact next unresolved mathematics

This is a complete conditional AUTHOR-WRITTEN topology reduction, not scientific execution, formal/Lean/kernel acceptance, configured-family/cross-vendor/human review, priority or novelty clearance. All named imports retain their existing written assurance boundaries; the fresh combined reduction needs its own complete independent written gate. Older gate returns are not silently transferred to it.

The full8/9 problem is now: produce an ACTUAL solution of(10) in arbitrary A5, or of the balanced arbitrary A3/F3 system, OR prove both entire actual classes empty. The new reduction does not itself settle either class. Every arbitrary holding, principal topology, genuine input/exit normalization, hidden-root type and backward feedback remains in at least one surviving class. In particular a proof about a selected5state cycle/chain, uniform holdings or a trace cone alone would NOT settle A.

The separate actual rational band through7/9 and its strict algebraic continuation remain fresh candidates with their own pending full gate; no ordering against an older unevaluated algebraic endpoint is inferred here. The full endpoint8/9 remains NOT_PROVED and the original minimum{7,8} is unchanged. No new launch permission, round completion, deadline extension or park-as-completion is inferred from this manuscript.
