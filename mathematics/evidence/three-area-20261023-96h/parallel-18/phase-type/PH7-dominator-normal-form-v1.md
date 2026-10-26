# PH7 relative-degree-five dominator normal form — candidate v1

Clock actually observed before creation: **2026-10-24T03:48:10-07:00**. Owner MathResearch96h, math-1. Written graph/matrix reasoning only; no scientific program, arithmetic code, solver, import, compile, test, enumeration, native launch, model CLI or nested agent.

The initial Newton-family construction idea did not produce an admissible PH7 pair. The dominator observation and preliminary block/factorization exploration arose during that hand attack and were disclosed to the parent before this freeze. This is not a preregistered-discovery claim. As requested, this packet freezes the complete graph proof and literal block form **before any new common-block numerator or characteristic-factorization claim**. Such identities are not asserted here.

## 1. Literal statement and scope

Let (alpha,T) be an actual seven-state PH representation, with T real Hurwitz Metzler, T1<=0, alpha>=0, alpha1=1 and literal exit omega=-T1>=0. Suppose its transform has relative degree exactly five:

    alpha(sI-T)^(-1)omega=K/s^5+O(s^-6), K>0.

This includes the frozen H_(1,2) at z=b^2/(a-c)^2=8/9, but the following graph statement does not assume its particular poles.

**Candidate dominator theorem.** There is a phase o outside both I=supp(alpha) and E=supp(omega) that every positive I-to-E directed path visits. After a simultaneous permutation, the actual PH pair has the form

    T=[ A     b       0
        r^T  -lambda  t^T
        D     f       F ],
    alpha=(alpha_R,0,0), omega=(0,0,omega_S),     (NF)

where R,o,S partition all seven phases, R,S are nonempty and |R|+|S|=6. All displayed cross blocks b,r,t,D,f are entrywise nonnegative. A,F are the actual principal subgenerators, not independently chosen matrices, and the exact row-sum ties are

    A1+b=0,
    r^T1+t^T1=lambda,
    D1+f+F1=-omega_S.                           (RS)

No irreducibility, uniform-rate, hidden-real-pole, companion or independently chosen path-weight assumption is imposed. The backwards block D is retained and may be nonzero.

This is a topology-unrestricted **normalization**, not PH7 impossibility, a construction at z=8/9, or a minimum8 theorem. Its correctness and novelty remain separate; status is AUTHOR-WRITTEN CANDIDATE pending actual reconstruction.

## 2. Exact positive path length from the same PH pair

The large-s expansion gives

    alpha T^j omega=0 for j=0,1,2,3,
    alpha T^4 omega=K>0.

Choose Lambda>=max_i(-T_ii) and B=T+Lambda I>=0. The binomial expansion has the same four initial zeros and fourth positive coefficient. Every term of alpha B^j omega is a nonnegative walk weight. Hence there is no positive initial-to-exit walk of fewer than four edges, and one of length four exists.

Deleting any repeated-vertex segment of a shortest positive walk would produce a shorter positive walk, including deletion of a self-loop. Thus a shortest path has four off-diagonal transition edges and five distinct states. The j=0 zero makes I and E disjoint; both are nonempty. The directed graph below uses only positive off-diagonal T entries, not generator diagonals.

An I-to-E path can be truncated at its first E and then at the last I preceding it. The resulting segment still has at least four edges and has no internal I or E vertices. It therefore uses at least **three distinct nonboundary phases**.

## 3. Complete two-path/one-cut argument

Here is the finite augmenting-path argument rather than an unproved appeal to a graph classification.

Build a directed capacitated network with a supersource joined to every I vertex and every E vertex joined to a supersink. Give those arcs and all original transition arcs capacity8. Split each nonboundary phase v into v_in->v_out with capacity1. Boundary phases may either remain unsplit or have split capacity8. Capacities here are only a graph proof device; they do not replace any transition rates.

Send one unit along an existing source-to-sink path. If its residual network has no augmenting source-to-sink path, let U be the residual-reachable set from the source. Every original arc from U to its complement is saturated, and every original arc entering U has zero flow (otherwise its positive reverse residual arc would extend U). Flow conservation therefore makes this cut have capacity exactly1. All original/boundary arcs have capacity8, so the cut consists of one nonboundary split arc. The corresponding phase is a separator of every I-to-E path.

If no such one-phase separator exists, the residual network instead has an augmenting path. All residual capacities are integers, so augment by one unit. Decompose the resulting integral value2 flow into two source-to-sink paths and discard any circulation cycles. The capacity1 nonboundary split arcs ensure that these two paths have disjoint nonboundary internal phases. Truncate each at first E/last preceding I as in Section2; this preserves that disjointness. Each uses at least three nonboundary phases, requiring at least six in total.

But there are only

    7-|I|-|E|<=5

nonboundary phases. This is impossible. Therefore the one-phase separator exists. Call it o. It is neither initial nor an exit phase by construction. Any walk avoiding o would contain a path avoiding o, so the conclusion is also a true first-hitting dominator statement, not merely a statement about a selected shortest path.

No automated graph enumeration or external classification theorem is used. The proof's only flow steps are the explicit integral augment/cut and path-decomposition facts above.

## 4. Derive the actual block form and row constraints

Delete o from the positive transition graph. Define R to be **all** phases reachable from I without visiting o. Let S be the remaining phases other than o. Then:

- I is contained in R.
- No E phase is in R, otherwise there would be an I-to-E path avoiding o; hence E is contained in S.
- R and S are nonempty.
- There is no positive edge R->S: its endpoint would also be reachable from I without o.

Permuting into R,o,S order gives the zero upper-right block of(NF). All other off-diagonal blocks retain their actual nonnegative transition entries, including arbitrary backwards D:S->R and returns f:S->o. No other zero pattern is inferred.

Since omega vanishes on R and o, the literal identity omega=-T1 gives all three equations(RS). In particular b=-A1 is **not** a free exit column. Alpha_R is nonnegative and sums to1. The last exit omega_S is also not free: it is the stated negative row sum, tied to D and f.

A and F are Hurwitz. One elementary proof for any principal block of a Hurwitz Metzler T is to put h=-T^(-1)1>0, obtained from the nonnegative semigroup integral. For a principal index set U,

    T_U h_U=-1_U-T_(U,Uc)h_Uc<0.

Positive diagonal similarity therefore makes every row sum of T_U strictly negative, so its Gershgorin right endpoints are strictly negative. This proves principal stability without assuming those blocks decouple dynamically.

Every actual positive simple initial-to-exit path first stays in R, then visits o, then stays in S. The first assertion follows from the definition of R. For the last assertion, if a post-o simple path entered R and then reached E without visiting o again, concatenating a pre-o I-to-that-R path would give an I-to-E walk avoiding o, contradicting the separator. Thus no such post-o return into R is possible on a simple path. Actual stochastic trajectories may return through D and revisit o; those feedback transitions remain in T and are not deleted.

This completes the normal-form proof. It asserts no subsequent numerator or characteristic identity.

## 5. Actual accepted PH7 anchor passes the normal form

Use the actual C7 anchor at z=31/49, not a free spectral list. Its source is `proof-seven-state-complex-hidden-extension-v1.md`, SHA256 `023ac8611a66263233288838eaf3dcd3ac0013111a5be93fb5974e7f47e39667`.

Put eta=d/7, lambda=a+eta, D0=lambda^2+12eta lambda+44eta^2, and

    f4=1616eta^4, f5=13184eta^5,
    f6=8192eta^6, f7=360448eta^7.

The actual T has diagonal-lambda, superdiagonal lambda and last row

    (f7/lambda^6,f6/lambda^5,f5/lambda^4,
     f4/lambda^3,0,0,-lambda).

Its initial support is states1,2,3, with alpha=(44eta^2,12eta lambda,lambda^2,0,...)/D0; its only exit is state7, with omega_7=K D0/lambda^6.

Every positive initial-to-exit path visits state4. Removing4 leaves R={1,2,3}, S={5,6,7}. Let J3 denote the three-state matrix with diagonal-lambda and superdiagonal lambda. The actual blocks are

    A=F=J3, b=(0,0,lambda)^T,
    r=0, t=(lambda,0,0)^T,
    D_(last,:)=(f7/lambda^6,f6/lambda^5,f5/lambda^4),
    f=(0,0,f4/lambda^3)^T,

with the other rows of D zero. These are literally entries of the accepted T. All(RS) ties hold, including the last row with its actual exit. Crucially **D and f are positive here**. A supposed normal form that discarded these feedback terms would fail this accepted control.

Its shortest path begins at initial state3 and goes3->4->5->6->7. The same dominator is nonboundary, and the proof does not falsely exclude this genuine PH7 or assume its hidden pair is real.

## 6. Actual accepted PH8 anchor is not excluded

At z=8/9 the accepted C8 anchor has eta=d/3, lambda=a+eta and hidden cubic `Y^3+8Y^2+26Y+28`. Its actual T has diagonal-lambda, superdiagonal lambda, and last row

    (f8/lambda^7,f7/lambda^6,f6/lambda^5,
     f5/lambda^4,f4/lambda^3,0,0,-lambda),

where f4=3eta^4,f5=684eta^5,f6=214eta^6,f7=2124eta^7,f8=9072eta^8. Its initial support is1,2,3,4 and sole exit is8. These are the literal supported source `proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`.

It also has an internal dominator, phase5. Removing5 gives R={1,2,3,4}, S={6,7,8}; the first positive initial-to-exit path is4->5->6->7->8. Its backwards D and return f are again retained. This does not contradict the seven-state theorem: having a dominator is a necessary normalization, **not an obstruction to PH existence**, and here |R|+|S|=7 rather than6. Its hidden polynomial has degree3, not the seven-state hidden degree2.

Thus both actual controls admit the claimed graph structure; PH8 is not incorrectly asserted to avoid it or to be excluded by it.

## 7. Status and next exact obligation

This is a complete candidate proof of an unrestricted internal-dominator normal form for the actual seven-state relative-degree-five pair. It uses the same alpha,T,omega throughout, with exit/row ties and feedback retained. No new holding-rate threshold or allowed-order chart is substituted for the minimum-order target.

At z=8/9 the full question remains whether any such actual pair exists; the known upper8 and lower7 therefore still leave minimum in{7,8}. Neither a PH7 pair nor its impossibility is supplied here.

A separate subsequent packet must derive any common-block numerator/characteristic identities from(NF), rather than treating them as part of this already frozen proof or choosing independent W,V,U. That derivation and eventual feasibility/exclusion must retain D, f, the row-sum constraints and all hidden-root types. The generic trace-only failed route and the supported rate-gap constraint remain valid controls, not sufficient obstructions. All prior verification and timestamp overlays remain operative; no novelty or formal acceptance is implied.
