# P44 v26 — PART26: ALL PPT completions, exact CP charge, and the one-Alice-level Schmidt border lemma

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 06:25:34 PDT 2026**. AUTHOR-WRITTEN, LATER UNREVIEWED. All identities are exact WRITTEN complex linear algebra at finite-dimensional PSD/Schur-complement facts, not scientific interpreter or machine checks. Original HOLD, exclusive root/eighteen/cutoff/deadline remain.

## T0. Why this is the SAME original problem, not an assumed CP-zero shortcut

Part25, SHA256 **e87a72a9e1319269b960924a52e3a9b270175d0a4b0977008bd171798faa3929**, gives the exact global K2 criterion for normalized W00=I and decomposition W=U+tilde(chi), U=T^dagger T, T=[I,K], K=[V1^dagger,V2^dagger,V3^dagger]. Its all-complex-two-plane positivity requirement remains mandatory; it is not replaced by any condition in this part.

The CP-kernel/PPT-target direction was ALREADY held before v118 worker receipt and saved in checkpoint120. The exact ALL-completion/charge equations and Schmidt-border proof supplied below are prospective development after the ACTUAL v118 return and separate whole-primary ACK **5315c8e48b34da02fd7240e576b90547ec6781ac876c183dc75758a8194d3057** was written and SENT before reasoning/source work. They are NOT backdated into checkpoint120 or called blind/private-clean evidence.

An indecomposable chi does NOT guarantee that adding U preserves indecomposability. Conversely a negative PPT pair for W need NOT have zero CP cost. The main representation T1–T2 includes EVERY PSD/PPT pair, with its actual nonnegative CP charge; the zero-charge graph in T3 is explicitly a SUFFICIENT subroute, NOT an exhaustive target ansatz.

P44 remains UNMET: no actual globally complex-SR<=2-positive indecomposable W/PPT-negative pair, and no all-state SN<=2 theorem, is delivered. The aim is to expose exactly which finite-dimensional charge/compatibility inequalities any original counterexample must satisfy, rather than assuming them away.

## T1. ALL PSD completions of the lower3x4 block, including singular blocks

Write a Hermitian4x4 bipartite operator in Alice0 versus Alice1,2,3 blocks as

    rho=[[A,B],[B^dagger,sigma]],

where A is4x4, B is4x12 and sigma is12x12. Moore–Penrose inverses are denoted by +. The exact PSD completion criterion is

    sigma>=0,
    range(B^dagger) subset range(sigma),
    H:=A-B sigma^+ B^dagger>=0.                       (PSD-COMP)

*Proof of necessity.* If v∈ker sigma, positivity of rho on (u,tv) for arbitrary complex t forces Bv=0. This gives the range condition. Completing the square with sigma^+ then gives H>=0. *Sufficiency* is the factorization

    rho=[[B sigma^+],[I12]] sigma [[sigma^+ B^dagger,I12]]
         +[[H,0],[0,0]],                              (FACTOR)

using B=B sigma^+ sigma and sigma sigma^+ B^dagger=B^dagger. Thus the singular case is included exactly, not discarded as a full-rank genericity assumption. ∎

For Part25's K define C=B+K sigma. Its adjoint also has range in range sigma. Conversely, ANY sigma>=0, C with that range condition, and H>=0 determine a PSD rho by

    B=C-K sigma,
    A=H+(C-K sigma)sigma^+(C^dagger-sigma K^dagger).   (ALL-RHO)

This parameterization is exhaustive in both directions; sigma=0 is permitted and then B=C=0. No state has been excluded by a CP-kernel restriction.

## T2. Exact CP charge for EVERY completion and the original negative-pair condition

Since U=T^dagger T, cyclicity of trace gives

    Tr(U rho)=Tr(T rho T^dagger)
       =Tr(A+B K^dagger+K B^dagger+K sigma K^dagger).

Use (PSD-COMP) and C=B+K sigma. The range conditions make the mixed terms exact, giving the MATRIX identity

    T rho T^dagger=H+C sigma^+ C^dagger>=0.            (CHARGE)

Consequently

    Tr(W rho)=Tr(chi sigma)+Tr(H)+Tr(C sigma^+ C^dagger). (PAIR)

This is an equality for ALL PSD completions, not merely a lower bound or a claim that a CP perturbation costs nothing.

Bob partial transpose acts on EACH4x4 block. Let B=[B1,B2,B3] and sigma=[sigmaij]_(i,j=1)^3. Define

    D=sigma^Gamma=[sigmaij^T],
    mathcalT(B)=[B1^T,B2^T,B3^T].

Then the exact PPT requirement in addition to (ALL-RHO) is

    [[A^T,mathcalT(B)],
     [mathcalT(B)^dagger,D]]>=0.                      (PPT-COMP)

Do NOT replace mathcalT(B) by the ordinary transpose of the4x12 row; its dimensions and block action differ. The display preserves all complex entries/conjugations. In particular sigma itself must be PPT, since D is a principal submatrix of rho^Gamma.

For any W satisfying Part25's ALL-plane K2 criterion, an original strict PPT-negative pair exists IFF there are sigma,C,H satisfying (ALL-RHO), (PPT-COMP), and

    -Tr(chi sigma)>Tr(H)+Tr(C sigma^+ C^dagger)>=0.    (STRICT)

This is an exact interface to the ORIGINAL indecomposability problem, not an assertion that such data exist. If STRICT holds, rho≠0 and Tr rho>0; dividing by Tr rho gives an eligible normalized PPT state with the same strict sign. Conversely every negative PPT state provides these data by T1, so the charge criterion does not lose pairs. If sigma=0, the right-hand terms leave Tr(W rho)=Tr(A)>=0, so any genuine negative pair has sigma≠0.

In finite dimensions DEC is the dual PPT cone. Thus (STRICT) plus global K2 positivity proves the actual desired counterexample; proving no such data exist for ALL global Part25 data would prove the opposite original theorem. No such existence/exclusion is supplied here.

## T3. The CP-zero kernel graph: EXACT criterion, expressly not exhaustive

Because both H and C sigma^+ C^dagger are PSD, CHARGE has trace0 IFF BOTH vanish. With range(C^dagger) subset range sigma, `C sigma^+ C^dagger=0` forces C=0: its quadratic form is the squared norm of sigma^(+1/2) C^dagger, whose restriction to range sigma is injective. Hence

    Tr(U rho)=0 iff H=0,C=0,
    iff rho=L sigma L^dagger, L=[[-K],[I12]].          (ZERO-CHARGE)

Equivalently range rho⊂ker T; the graph form follows also because T L=0 and the lower block of L is identity. This covers every PSD state annihilating the rank-four CP peel.

For this graph, define the4x12 block row N with

    Nj=sum_(i=1)^3 sigmaij^T conjugate(Vi),
    A0=K sigma K^dagger.

Indeed B=-K sigma has block j `-sum_i Vi^dagger sigmaij`, whose transpose is -Nj. The PPT matrix is EXACTLY

    [[A0^T,-N],[-N^dagger,D]].                        (GRAPH-PPT)

Its singular Schur criterion is

    D>=0,
    range(N^dagger) subset range(D),
    A0^T-N D^+ N^dagger>=0.                          (GRAPH-SCHUR)

The same proof as T1 gives necessity and sufficiency. In particular merely choosing a PPT sigma does NOT guarantee its graph lift is PPT; the range and residual inequalities are substantive. No transposition-through-product error or unsupported CP-kernel assumption remains.

If (GRAPH-SCHUR) and `Tr(chi sigma)<0` could be established for actual data with ALL-plane positivity, they would give a sufficient exact P44 certificate, because the entire CP charge vanishes. Failure of this OPTIONAL route would NOT rule out positive-charge pairs in T2 or settle P44.

## T4. One-Alice-level Schmidt border lemma — a genuine restriction on ALL candidate states

**Lemma T4 (WRITTEN, no PPT hypothesis).** For ANY PSD completion rho of a nonzero3x4 block sigma,

    SN(sigma)<=SN(rho)<=SN(sigma)+1,                  (BORDER)

where unnormalized positive operators have Schmidt number defined by finite positive sums of pure projectors. If sigma=0, rho is supported on Alice0 and is separable. In particular, if sigma is SEPARABLE, EVERY PSD completion rho has Schmidt number<=2, independently of PPT or of its CP charge.

*Proof.* Compression by the Alice projection onto levels1,2,3 cannot increase Schmidt rank of any pure vector; applying it termwise gives the lower inequality. For the upper one use FACTOR. Choose a finite pure decomposition `sigma=sum_l |w_l><w_l|` with Schmidt rank(w_l)<=s=SN(sigma). Let `M=[[B sigma^+],[I12]]`. For w_l, the three lower Bob rows span a space of dimension at most s; M only adds ONE arbitrary Bob row at Alice0. Hence rank(Mw_l)<=s+1. The residual `|0><0| tensor H` is a positive sum of product projectors. FACTOR gives a decomposition of rho with ranks<=s+1. Every w_l lies in range sigma because its kernel annihilates every positive summand, so no singular-domain issue occurs. ∎

This elementary border argument is not claimed novel or a general map-preservation theorem. It uses only the specific addition of ONE Alice output row, not an assertion that the arbitrary linear M is a local operation.

**Necessary consequence for the ORIGINAL P44 counterexample:** an eligible rho with SN>=3 must have an ENTANGLED3x4 principal compression for EVERY Alice three-dimensional hyperplane. If even ONE such compression were separable, change the Alice basis to that hyperplane and apply BORDER, proving SN(rho)<=2. For PPT rho each such compression is also PPT. Thus a negative pair in T2 requires a genuinely PPT-entangled sigma, not a separable identity-block target. This is a necessary condition, not a classification of all3x4 PPT states or a claim they have a particular Schmidt number.

The graph case is especially transparent: a product lower vector `alpha tensor u` is sent by L to rows `(-sum Vi^dagger alpha_i u,alpha1u,alpha2u,alpha3u)`, whose complex row span has dimension<=2. Therefore a separable sigma can NEVER produce a negative target against a globally K2-positive W, even if the graph lift is PPT. This avoids mistaking mere existence of a zero-charge PPT completion for an entangled negative certificate.

## T5. Exact symbolic control: identity lower block and a trace-zero commutator

As a WRITTEN control of the graph PPT formula, take the symbolic identity operator sigma=I3 tensor I4, without any parameter trial. Then D=I12, Nj=conjugate(Vj), and

    A0^T-N N^dagger
      =sum_i (Vi^dagger Vi-Vi Vi^dagger)^T.            (COMM)

This matrix is Hermitian and has trace0, by cyclicity of trace. It is PSD IFF it is0. Hence this graph is PPT IFF

    sum_i Vi^dagger Vi=sum_i Vi Vi^dagger.

For example the equality is automatic when every Vi is normal, but normality is not claimed necessary termwise: only the displayed sum is necessary and sufficient here. No commutation between distinct Vi is inferred.

Even when this yields a PPT graph, BORDER proves its SN<=2 because sigma is separable. Also `Tr(chi sigma)=Tr chi>=0`, since each diagonal product expectation is nonnegative for the positive chi. Thus this exact control CANNOT be a P44 counterexample. It checks the orientation/trace terms and identifies why the simplest CP-zero target is mathematically incapable of providing the desired sign; it is not an inconsequential solver enumeration or a false all-target no-go.

## T6. What has advanced and what is still exactly missing

Part25 replaces a local/selected family by global ALL-complex-plane positivity. This part now includes ALL PPT targets with their exact nonnegative CP penalty, rather than trusting the indecomposability of chi to survive CP addition. It also proves that every possible SN>=3 target must have PPT-entangled codimension-one Alice compressions; a separable lower target is excluded for ALL PSD completions, not only the zero-charge graph.

Still NOT_PROVED:

- `PAIR-GLOBAL`: no actual complex chi,Vi satisfying EVERY Part25 B_F>=0 and (STRICT) with a PPT completion.
- `PAIR-DEC`: no theorem that all such global witness/target data have nonnegative PAIR.
- `GRAPH-ENTANGLED`: no actual PPT-entangled sigma satisfying GRAPH-SCHUR with negative chi expectation and global ALL-plane positivity. This is only an optional sufficient subroute; its absence is not an original no-go.

The exact future task is to handle a genuinely PPT-entangled3x4 compression while respecting BOTH global plane positivity and its unavoidable CP charge/PPT completion, or prove their joint incompatibility. No numeric tuple, parameter sweep, solver/accountant/certificate run, source theorem imported by title or old normalized-N4 outcome is supplied.

All previous24parts/addenda, Part25 and every held Delta/conditional-norm/CPtarget/Laurent/chart/range/Bell/code/PV/DOC lead remain. All own cp049/063/081/083/085/089, oldcp013/admission and parent histories persist; N4 UNKNOWN/incomplete/exit-unestablished, old21 NOT_RECONSTRUCTED, C19–C27 FOUR minors and normalized N4 ZERO new-method credit. No clean-history/private-cognition/runtime/cadence or novelty/current-status assurance. Written correct new algebra cures no prior process finding.

Exact WRITTEN/source/metadata only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/build/test/nestedagent/newGO, no approximate/decimal/numeric scouts or withdrawn-output guidance. No pinned file edited. No formal/kernel/executable/configured-family/human/novelty/parent acceptance or publication claim. Same original eighteen, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**. This is an incremental active primary packet, NOT an early final park or round closeout. **P44 remains UNMET.**

**END OF COMPLETE v26 PART26.**
