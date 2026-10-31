# Universal two-horizontal-node chain: exact level-four lifting and a wider graded Serre equality

Owner **MathKacMoody-2**, original math-3. Actual native `/bin/date` before this NEW write: **Wed Oct 28 17:07:21 PDT 2026**. Precreation observation only.

**SCIENTIFIC CANDIDATE — WRITTEN PROOF PLUS BOUNDED EXACT CHECKS; NOT YET INDEPENDENTLY REVIEWED OR ADOPTED.** The proof below claims a genuine all-parameter graded result, not the full original band. The finite experiments check specific identities and cases, not the unrestricted theorem. No novelty, global Serre, formal/kernel or stronger-family acceptance is claimed.

## 0. Exact new claim and original-object scope

For every pair of positive integers r,s and every allowed FULL complex Cartan realization C of

    A(r,s) = [[2,-1,-1],[-1,2,-1],[-r,-s,2]],

let G_C, the full Serre ideal J, its Cartan-disjoint maximal ideal tau, and the simultaneous actual lowering map Delta be as in the admitted original definitions. Write root degree alpha=(a,b,n), with a,b,n nonnegative integers.

**Theorem A (candidate).** For every n>=1 and EVERY r,s>=1, the simultaneous simple-lowering map on the ACTUAL Serre quotient G_C/J has zero kernel in degree (1,1,n). More strongly:

- if s<n, the single actual f3-lowering is injective in that degree;
- if s>=n and r<n, the single actual f3-lowering is injective;
- if r>=n and s>=n, the pair of actual lowerings (f1,f3) is injective.

Zero-dimensional source cases are included. All targets are the FULL actual root spaces. The proof handles every boundary through these explicit inequalities; it does not assume r=s, avoid a singular realization or select a numerical parameter.

**Corollary B — actual reached-target correction.** At alpha=(1,1,n), and thus in particular at the requested level-four alpha=(1,1,4),

    Delta(G_C,alpha) intersect (direct-sum_i J_(alpha−epsilon_i))
                  =Delta(J_alpha).                       (0.1)

Indeed an actual reached tuple in the target ideal has a preimage x whose Serre-quotient class is annihilated by all three lowerings; Theorem A forces x in J, so **j=x itself** is a common actual ideal correction. This is not separate per-row lifting and does not replace the target intersection by the entire target ideal.

**Corollary C — actual graded ideal equality.** For every nonzero positive root degree (a,b,n) with a,b in{0,1} and n>=0,

    J_(a,b,n)=tau_(a,b,n).                              (0.2)

This holds for ALL r,s/full C at these explicitly restricted horizontal degrees, with NO upper bound on n. It is NOT equality for every degree at level4 or every matrix. The complete predecessor/base/first-defect proof is in Section6; the conclusion is not inferred pointwise from Theorem A alone.

## 1. Current input boundary and proof dependencies

The source family and G_C/J/tau definitions are the literal packet `8b811cbc88e55b5b48bebef299f356bf10c808968c967ab2ed4aca1065cc03a6`. We use ONLY the following independently admitted, exactly scoped interfaces:

1. Parent `08217c89602bbed5bb05447144addfb1978037ad3e4c2e57271d88b794d98be9`: full-realization root grading/triangular support, full positive/negative Serre-ideal splitting, J subset tau and root-zero defect0, and the actual first-defect criterion. This is ordinary same-harness written support, not a source-page authentication.
2. Parent `f08daf3e2259a563a426e8982be78a36094bb58e4d56f587b2b51f14fa8df46d`: the preliminary positive source is the actual free Lie algebra on e1,e2,e3 and the full positive Serre ideal transports to the seed-generated free-Lie ideal. Its PBW theorem is a named classical import. The mandatory source qualification `21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247` says the frozen text is a normalized transcription/paraphrase, NOT a byte-verbatim primary-source quote. This theorem's proof is not newly authenticated here.
3. The defining Chevalley brackets, Jacobi, elementary properties of Lie ideals and the explicitly demonstrated tensor-word leading terms below.

The user's frontier-first direction supersedes the earlier procedural execution ban PROSPECTIVELY. Historical HELD/ZERO outputs are not accepted as correctness premises. This proof does not quote, replay or derive an inference from those bodies; prior exposure is not denied or certified cognitively unaffected. The result was generated and checked anew from the actual definitions/adopted inputs, not from an old type table or review verdict. Original scope remains the whole registered family; this theorem proves only the explicit slice(0.2).

## 2. Entire positive free-Lie source at degree (1,1,n)

Write

    X_k=(ad e3)^k e1,      Y_k=(ad e3)^k e2,
    V_k=[X_k,Y_(n−k)]   (0<=k<=n).                       (2.1)

The actual free-Lie identification is the named PBW-dependent input above. Every Lie word with exactly one e1, exactly one e2 and n copies of e3 is a linear combination of the V_k:

- a Lie word using only e3 is either e3 or0;
- a word with one e1 and otherwise e3 is a scalar multiple of the appropriate X_k, and similarly for e2/Y_k, by induction on its bracket tree;
- a bracket whose two distinguished letters lie in different factors is therefore a multiple of a V_k; if both lie in one factor, the other nonzero factor is e3 and its adjoint distributes over the bracket by Jacobi, preserving the span.

The V_k are linearly independent. Embed the free Lie algebra into the tensor algebra using the PBW-based source identification. With lexicographic order e1<e2<e3, X_k has least associative word e1 e3^k with coefficient (−1)^k; Y_l has least word e2 e3^l with coefficient (−1)^l. The least associative word of V_k is therefore

    e1 e3^k e2 e3^(n−k),

with nonzero coefficient (−1)^n. These leading words are distinct for distinct k. This proves the actual source basis (V_0,...,V_n); no character count or presumed module decomposition is used.

The same argument at n=0 gives V_0=[e1,e2]. With only one horizontal generator, the whole positive degree (1,0,n) is spanned by X_n, and (0,1,n) by Y_n. Each displayed vector is nonzero by its leading tensor word. The pure e3 degree is one-dimensional at n=1 and zero for n>1.

## 3. FULL actual Serre ideal, with no overlap assumption

At degree (1,1,n), every positive Serre seed whose repeated node is1 or2 has at least two occurrences of that node and cannot contribute. The ONLY seeds whose degrees can fit are

    X_(r+1)=(ad e3)^(r+1)e1,
    Y_(s+1)=(ad e3)^(s+1)e2.                            (3.1)

This is the literal ALL-seed bookkeeping at the displayed multidegree, not a selected coefficient evaluation. Negative seeds cannot add a hidden positive component because the admitted full ideal splits into actual positive and negative ideals.

The ideal generated by X_(r+1), in this multidegree, is exactly the span of V_k with k>=r+1. To see both containments: every X_k for k>=r+1 is a positive-ideal descendant, so its bracket with Y_(n−k) lies in that ideal. Conversely, any simple-adjoint descendant reaching degree (1,1,n) uses e2 once and e3 otherwise; before/after that e2, Jacobi distributes every e3 action across the bracket. Every resulting X index remains >=r+1. The corresponding argument for the Y seed gives exactly V_k with n−k>=s+1. It does not require those two generated families to be disjoint; possible overlap is included in their sum.

Therefore the ACTUAL quotient source has basis

    bar V_k,    a<=k<=b,
    a=max(0,n−s),       b=min(n,r),                      (3.2)

with the convention that a>b means the source is0. In particular its dimension is max(0,b−a+1); this is proved by the explicit ideal SPAN and leading-word independence, not by a virtual-character subtraction.

At the f3 target degree (1,1,n−1), write

    U_j=[X_j,Y_(n−1−j)],    0<=j<=n−1.

Its actual Serre quotient basis is similarly

    bar U_j,    a'<=j<=b',
    a'=max(0,n−1−s),    b'=min(n−1,r).                  (3.3)

The source and target ideals in(3.2),(3.3) are the complete ACTUAL ideals at those degrees. No free target has been substituted.

## 4. All-variable f3 and f1 formulas, including signs and boundaries

The defining relations and Jacobi give, for k>=1,

    [f3,X_k]=k(r−k+1)X_(k−1),
    [f3,Y_k]=k(s−k+1)Y_(k−1),                           (4.1)

and the corresponding k=0 brackets vanish. For example, the induction follows from

    [f3,[e3,X_k]]=−[h3,X_k]+[e3,[f3,X_k]],
    [h3,X_k]=(−r+2k)X_k.

These are symbolic identities for the complete variables; the coefficients are NOT inferred from sampled cases. The Y identity is identical with s.

Applying Jacobi to the SAME V_k yields

    [f3,V_k]=k(r−k+1)U_(k−1)
              +(n−k)(s−n+k+1)U_k,                       (4.2)

where out-of-range U_(−1),U_n are omitted. Ideal stability makes this an actual quotient map, and each bar U outside(3.3) is zero.

For f1, the defining relation [f1,e1]=−h1, [f1,e2]=[f1,e3]=0 and row1 of A give

    [f1,V_0]=(n+1)Y_n,
    [f1,V_1]=−Y_n,
    [f1,V_k]=0  for k>=2.                               (4.3)

For completeness: [f1,X_0]=−h1,[f1,X_1]=−e3, and [f1,X_k]=0 for k>=2; every [f1,Y_l]=0. The full h1 action on Y_n is used in the first line. No actual Cartan direction is quotiented away. The analogous f2 formulas are unnecessary for the injectivity argument, but all f2 components remain in Delta and in Corollary B's full target.

## 5. Prove the quotient kernel vanishes for ALL r,s,n

Fix n>=1. If a>b in(3.2), the ACTUAL source is zero and the theorem is immediate. Otherwise take an arbitrary source vector

    x=sum_(k=a..b) c_k bar V_k.

All c_k below are arbitrary complex coefficients of the SAME actual source.

### Case I: s<n

Here a=n−s>=1, and the first ACTUAL f3-target basis vector is bar U_(a−1). Its coefficient in[f3,x] is

    a(r−a+1)c_a.

No bar V_(a−1) source survives to contribute a second term. Since a<=b<=r, the factor is a positive integer and hence nonzero. If[f3,x]=0 then c_a=0. At the next target coordinate U_a, the term involving c_a is already zero and the coefficient of c_(a+1) is (a+1)(r−a), again nonzero because a+1<=b<=r. Continue through k=b. Every required U_(k−1) belongs to the actual target interval(3.3), and every c_k vanishes. Thus **f3 is injective** in this whole case, without dividing by a vanishing coefficient or discarding a target relation.

### Case II: s>=n and r<n

Here a=0 and b=r<n. The ACTUAL target contains U_b. Its coefficient in[f3,x] is

    (n−b)(s−n+b+1)c_b,

because source V_(b+1) is absent. Both factors are strictly positive: n−b>0 and s−n+b+1>=1. Thus c_b=0. Descending through U_(b−1),...,U_0 shows all earlier coefficients vanish; each newly used second factor is also positive. Thus **f3 is injective** here as well.

### Case III: r>=n and s>=n

Here a=0,b=n: no X/Y seed fits either the source degree or the f3 target. Also the f1 target Y_n survives the full ideal because s>=n. If both f1x=0 and f3x=0, equation(4.3) gives

    c_1=(n+1)c_0.                                       (5.1)

The U_0 coefficient of f3x is n(s−n+1)c_0+r c_1. Hence

    [n(s−n+1)+(n+1)r]c_0=0.                            (5.2)

The bracketed integer is strictly positive for n>=1 and r,s>=n. Therefore c_0=c_1=0. For j=1,...,n−1, the U_j coefficient then forces c_(j+1)=0, since (j+1)(r−j)>0. When n=1 this last range is empty, already leaving both coefficients0. Thus **(f1,f3) is injective** in the remaining whole case.

The three cases cover ALL positive r,s,n. They prove Theorem A. Positivity here is a symbolic consequence of the listed integer inequalities, not a sampled determinant or an assumed sign of a norm. No f3 target is restricted to a lowest line, and no parameter value is excluded.

## 6. Pay the entire lower boundary before claiming J=tau

For degree(1,0,n), the actual source is the line X_n. If n>=r+1 the Serre ideal contains it and the quotient is0. If 1<=n<=r, the actual f3 derivative is n(r−n+1)X_(n−1), which is nonzero in its FULL actual target because the first X seed occurs at r+1. If n=0, f1(e1)=−h1; h1 is nonzero modulo J because the admitted ideal has zero Cartan component, [h1,e1]=2e1 and e1 survives the free-source/Serre-seed grading. Thus the simultaneous kernel is0 in ALL these degrees. The analogous statement for(0,1,n) uses Y_n and s, with f2 at n=0.

At(1,1,0), the actual source is the line [e1,e2] and f1 sends it to e2, which is nonzero modulo J. For(0,0,n), the source is0 for n>1 and is e3 for n=1; its f3 derivative is−h3, nonzero by the same defining-bracket/free-generator/zero-Cartan-ideal argument. There is no nonzero positive degree with a,b in{0,1} left untreated.

Let D=tau/J in the FULL realization. The admitted input proves D is a root-graded ideal, D_0=0, and mixed-sign root spaces vanish. The set of nonzero positive degrees with horizontal coordinates at most1 is closed under simple lowerings that stay positive. If any D component in this set were nonzero, choose one of least total height. Every simple lowering would land in a smaller positive component of the SAME set, in D_0=0, or in a zero mixed-sign space. The chosen class would therefore be simultaneously singular. Sections5–6 prove no such class exists. Hence D vanishes at EVERY degree in the set, proving(0.2) for all r,s and all full C.

This minimal-height step is essential. Zero singular kernel at a single isolated alpha, without its predecessor boundary, would NOT alone imply J_alpha=tau_alpha.

## 7. Bounded exact verification actually exercised

The local scientific experiment and checker are NEW files under the exclusive root:

- `frontier-20261028-lift-exact.py`, SHA256 `3511d07fdab20523935f704a45603e9349827eb5f3b14cfa3ec8b8a307173477`. It constructs free-Lie Lyndon brackets in the tensor algebra, generates ALL six Serre seeds and all simple-adjoint descendants inside a bounded multidegree, and computes the actual simultaneous three-row source/target/intersection ranks over `fractions.Fraction`. For every derivative it checks cancellation of the right-Cartan term in the tensor-word formula. Its underlying Lyndon enumeration is an experiment, NOT an input to the all-n proof above.
- `frontier-20261028-lift-114-rs1to4.json`, SHA256 `6d228bf04f93f27a155284996b41b2193cb26a85fb4b71cfffec19329f2a429d`: actual exact experiment at degree(1,1,4), r,s in{1,2,3,4}. All16 tested quotient-kernel and reached-lifting obstruction dimensions were0. In the r=s=1 case the unreduced kernel and ideal-kernel dimensions were both1, illustrating why a FREE kernel need not be0; this is a computed observation, not a sampled proof of all parameters.
- `frontier-20261028-chain-check.py`, SHA256 `dbcf8bd3906211230e5c16325d6a3c3473e0964303139c7c9a3ea8e71e57f709`, and its output `frontier-20261028-chain-check-results-v1.json`, SHA256 `6277cfd2e3be216423013ed2014dbc124278b76764545217b7de1bfb6d864d5e`: actual bounded run reported **PASS, 144 exact cases**, n=1,...,4 and r,s=1,...,6. It checks the direct bracket source basis against the engine's Lyndon basis, the ALL-seed generated source/f3-target ideals against(3.2)–(3.3), every f1/f2/f3 formula for every source basis vector, and both computed actual quotient-kernel and reached-lift obstruction dimensions. Assertions use exact integer/rational arithmetic; no floating point or finite-field rank is used.

The chain checker imports the same exact engine for bracket and elimination operations: it is an independently specified set of formulas and comparisons, **not an independent implementation or external review**. These144 cases do NOT verify unbounded r,s,n, Cartan-ideal generalities or the written proof mechanically. The proof above, including all boundary cases, is the candidate justification for the universal quantifiers.

Observed actual commands were `python3 frontier-20261028-lift-exact.py --a 1 --b 1 --max-r 4 --max-s 4 --output frontier-20261028-lift-114-rs1to4.json` and `python3 frontier-20261028-chain-check.py`; each exited successfully. An earlier environment check found system Python lacked `sympy`; the experiment uses only the standard library and does not install a dependency. No user-reported failure was rerun or hidden.

## 8. Exact remaining problem and verification boundary

The original target is NOT closed. At level4 the result pays exactly the degrees with a,b in{0,1}, including(1,1,4), for every r,s/full C. Other horizontal multidegrees—including the remaining unclosed primitive types and their FULL source/target ideals—are not decided by this argument. The five-source invariant 3→5 quotient and its earlier parameter scope are not relabeled as solved. H13/old19, arbitrary matrices, global/all-level Serre outside(0.2), scientific novelty and the full original conjecture remain unproved.

The separate actual reached-target obligation persists outside the proved slice. In particular the proven injectivity does not say all abstract target-ideal tuples are reached, nor does it treat coherently chosen seed rows as the whole target. The named PBW import and all full-Cartan/ideal-splitting boundaries must be carried into any review. Main must read this COMPLETE proof, code/certificates as applicable and actual peer returns before adoption; source identity, finite-case agreement or this author's confidence is not acceptance.

Scientific work/selected exact checks are permitted PROSPECTIVELY by the supplied frontier-first owner direction; no old quarantined output is credited as proof. No external-model CLI/paid API, publication, Git push, deletion, infrastructure mutation or secret access. Existing frozen files are unchanged. No clean-cognition, independent implementation, formal/kernel/human/configured-family or continuous-service claim is made.

**END OF ALL-PARAMETER CHAIN-SLICE CANDIDATE — FULL ORIGINAL TARGET REMAINS OPEN.**
