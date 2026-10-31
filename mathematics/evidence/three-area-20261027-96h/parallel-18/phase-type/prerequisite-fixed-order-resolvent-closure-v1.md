# Definition-first minimum-order continuation: unbounded rates, finite resolvent closure and boundary order exclusion

MathResearch96h-2 / math-1. Actual native observation before drafting: **Tue Oct27 15:04:53 PDT2026**. **WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Exact all-variable written proof; no scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/test/typechecker, fitted state or numerical probe.

## 1. Scope, inputs and reproduction qualification

Main has qualified the earlier beta_star boundary calculation as a **definition-first REPRODUCTION of an old baseline**, not a newly discovered existence threshold. The immutable `prerequisite-boundary-reproduction-and-NR-import-addendum-v1.md` carries that correction; the old baseline body was NOT opened. This manuscript claims a complete current proof of an actual fixed-order coupling/closure lemma and its precise non-effective lower-order consequence. Priority/novelty and whether an equivalent classical consequence was already known are NOT asserted.

Inputs: current S1 controls and43LF literal packet (`89fedee56db112d2fc29b1762dc18fbc58092dffabb130e9001e14a853eb5c2c`); complete195LF reproduced density proof (`a763a08228625177d05f98cbc18f0deddba9cdfa609c83eb983e7f5a588d0adb`); elementary finite matrix-exponential/resolvent algebra, finite-dimensional compactness, Jordan block algebra and finite nonnegative-matrix graph arguments SUPPLIED below. No old PH closure theorem, compactness/hidden-factor manuscript, held guide or positive-projection theorem is imported.

Main separately authorizes O'Cinneide(1990, Stochastic Models6:1–57) ONLY as a NAMED_NR statement: a distribution on[0,infinity) with rational LST is PH iff its positive-time density is strictly positive and its LST has a unique pole of maximal real part. It is used ONLY to assert finite PH existence on the positive side after the lower-order proof, not to prove fixed-order closure. No primary proof/version was supplied; precise use and consequence-if-false are stated in §8.

The earlier79LF bounded-rate lemma is contextual progress but NOT a correctness premise: this proof handles UNBOUNDED holding rates directly. Current proof is not a hidden generator-rate bound or an assumption that a singular matrix limit stays Hurwitz.

## 2. General all-topology fixed-order closure statement

Let H_j be transforms of actual finite PH pairs `(alpha_j,T_j)` of dimensions at most a fixed integer n, with arbitrary real Hurwitz Metzler T_j, `omega_j=-T_j1>=0`, and alpha_j probability rows. Holding rates may be unbounded; all topologies, reducibility, boundary supports and canceled modes are allowed.

Assume H_j(s) converges for EVERY positive real s to a function H_0(s) that is a proper probability LST with

    lim_(s down to0) H_0(s)=1,
    lim_(s to infinity) H_0(s)=0.                  (PROPER)

The second condition excludes an instantaneous atom at zero. Then H_0 has an actual PH representation of dimension at most n. The proof reconstructs row/input/exit/stability rather than importing an abstract closure assertion.

For the boundary-order application it would suffice to reconstruct a finite subgenerator with a nonzero strictly positive density. We prove the stronger actual-object restoration to expose every coupling.

## 3. Bounded resolvents survive even when generator entries do not

Pass to a subsequence of constant dimension m<=n and probability rows `alpha_j->alpha`; no scientific sequence is sampled. Fix an ARBITRARY symbolic anchor sigma>0. Write

    R_j(s)=(sI-T_j)^(-1).

Uniformization or the nonnegative substochastic semigroup gives, for ALL real s>0,

    R_j(s)>=0,       R_j(s)1<=1/s.

Thus the matrices R_j(sigma) lie in a compact bounded cube. Pass to one subsequence with `R_j(sigma)->A`. This does not require a single bounded T_j entry.

The ordinary resolvent identity yields

    R_j(s)=R_j(sigma)[I+(s-sigma)R_j(sigma)]^(-1),
    [I+(s-sigma)R_j(sigma)]^(-1)=I-(s-sigma)R_j(s).

For each s>0, the inverse on the right has row norm at most `1+|s-sigma|/s`. Consequently its limiting left matrix `I+(s-sigma)A` is invertible: if bounded inverses of convergent matrices had a singular limit, taking a convergent subsequence of the inverse matrices in finite dimension would give a right inverse for that singular matrix, impossible. Therefore

    R(s)=A[I+(s-sigma)A]^(-1)
         =lim_j R_j(s),
    R(s)>=0,       R(s)1<=1/s.                     (RES)

The SAME subsequence defines R(s) for EVERY s>0; the argument does not choose different physical data at different evaluations. It also gives the resolvent identity and commutation for the family R(s).

The literal exit/input ties are retained WITHOUT taking a limit of potentially unbounded omega_j:

    H_j(s)=alpha_j R_j(s)(-T_j1)
          =1-s alpha_j R_j(s)1.

Hence the actual limit is

    H_0(s)=1-s alpha R(s)1.                        (H-LIM)

## 4. The limiting positive projection is constructed, not assumed

The bound(RES) makes `sR(s)` uniformly bounded for s>0. Examine the finite Jordan blocks of A. On a nonzero-eigenvalue block, `s A[I+(s-sigma)A]^(-1)` tends to the identity. On a zero-eigenvalue block with nonzero nilpotent N, the corresponding R(s) is the finite polynomial

    N-(s-sigma)N^2+...,

so `sR(s)` would be an unbounded polynomial if that block had size at least2. Fixed similarity changes boundedness only by a fixed factor. Thus zero is semisimple, and

    Pi=lim_(s to infinity) sR(s)

exists. It is the projection onto the nonzero spectral subspace of A along ker A. In particular

    Pi^2=Pi,   Pi>=0,   Pi1<=1,
    Pi R(s)=R(s) Pi=R(s).

This step is finite block algebra plus a proved uniform resolvent bound, not a positivity-based guess of a rank projection. If Pi=0 then R(s)=0 and(H-LIM) gives H_0=1, contradicting(PROPER); hence its rank is positive.

## 5. Every substochastic idempotent has an actual positive state factorization

We prove the finite positive-projection fact needed here. Extend Pi to the stochastic idempotent on m+1 states

    Pi_hat=[ Pi       1-Pi1
              0         1 ].

Its last state is absorbing. Finite directed-graph decomposition separates transient states and closed irreducible classes. Each closed block B is stochastic and idempotent. A real fixed vector of an irreducible stochastic B is constant: at a maximum coordinate, the averaging equation forces all positive-neighbor values to equal that maximum, and irreducibility propagates it to every coordinate. Since the image of an idempotent is its fixed space, B has rank1 and equals `1*pi_C`, for a nonnegative probability row pi_C supported on its class.

The transient block D is idempotent as well. Every transient state has a positive-probability finite path into a closed class; taking a minimum over finitely many chosen graph paths gives some integer L and delta>0 with `D^L1<=(1-delta)1`. Thus D^k tends0. But D^2=D makes every D^k=D, so D=0. No rate/time-scale assumption is hidden in this finite stochastic-matrix argument.

Idempotence then forces every transient row's portion in a closed class to be its total weight times pi_C. Apart from the absorbing last-state class, enumerate the remaining classes only as symbolic indices C=1,...,ell. Let V have their stationary probability rows on the original m coordinates, and U their mixture-weight columns from the original states. These have

    U>=0, V>=0, V1=1, U1<=1,
    VU=I_ell,      Pi=UV.                         (UV)

All properties follow from the displayed closed-class/transient rows; in a class C the U row is its corresponding unit vector. In particular ell=rank Pi<=m. This supplies the full positive factorization; no general nonnegative-factorization theorem is invoked.

## 6. Recovering a finite actual subgenerator and its original couplings

Because A has no nilpotent zero block, it is invertible on range Pi. Thus `C_sigma=VAU` is invertible. Put

    C(s)=V R(s) U,
    Q=sigma I-C_sigma^(-1).

The resolvent identity on range Pi gives

    C(s)^(-1)=C_sigma^(-1)+(s-sigma)I=sI-Q,
    R(s)=U(sI-Q)^(-1)V.

Since U,V and R(s) are nonnegative,

    C(s)>=0,
    C(s)1=V R(s)U1<=V R(s)1<=1/s.

For large symbolic s, finite matrix inversion gives

    (sI-Q)^(-1)=I/s+Q/s^2+O(s^(-3)).

For an off-diagonal entry, nonnegativity for all positive s forces `Q_ij=lim s^2 C_ij(s)>=0`. The row bound forces

    Q1=lim_(s to infinity) s[s C(s)1-1]<=0.

Therefore Q is an actual finite Metzler SUBGENERATOR, although it need not yet be Hurwitz. With `gamma=alpha U>=0`, gamma1<=1, (H-LIM) becomes

    H_0(s)=1-s gamma(sI-Q)^(-1)1.

Its limit at infinity is `1-gamma1`. By(PROPER), gamma1=1. Thus gamma is a probability row, and with the LITERAL exit `eta=-Q1>=0`,

    H_0(s)=gamma(sI-Q)^(-1)eta.                    (ACT)

No independent exit, probability renormalization, negative inverse or different limiting matrix has been introduced.

To restore Hurwitz stability if necessary, retain the set S of states reachable from supp(gamma) by positive off-diagonal Q paths. This set is forward-closed and contains the whole initial support. A reachable closed class with no exit would be entered with positive probability, making eventual absorption probability strictly less than1, contrary to `H_0(0)=1`. Hence every state of S has a path to an exit. Uniformize Q_S at any symbolic positive rate at least its holdings. Finitely many paths give a common positive absorption probability within some finite number of discrete steps. Its substochastic transition matrix consequently has a strictly contracting power and spectral radius<1, so Q_S is Hurwitz.

Deleting ONLY the unreachable complement leaves gamma_S a probability row and the actual exit `-Q_S1=eta_S`; transfer(ACT) is unchanged. This constructs an actual PH representation of order `|S|<=ell<=m<=n`, proving the full closure theorem. This is a theorem about proper limiting distributions, not permission to delete phases from the original critical seven-state classification without its antecedents.

## 7. Consequence for the ORIGINAL minimum-order function near beta_star

Use the EXACT literal family and the REPRODUCED threshold r_star from the195LF input. Fix arbitrary symbolic c,b>0. Vary `d=r b`, `a=c+r b`. At r=r_star, the continuous density has its positive-time zero and so is not finite PH, by the directly proved all-topology strict-density lemma.

For EVERY fixed integer N>=1 there exists epsilon_N(c,b)>0 such that

    r_star<r<r_star+epsilon_N(c,b)
      => NO actual PH representation of order<=N.  (LOW)

Otherwise a contradiction sequence r_j down to r_star with order<=N would have rational transforms converging at ALL positive s to H_(r_star); its properness and strict propriety are explicit from the literal H. The closure theorem would make that boundary transform PH of order<=N, contradicting its interior density zero. UNBOUNDED rates are now covered, unlike the79LF predecessor.

Thus (LOW) is a topology-unrestricted exact lower-order exclusion on a positive-width parameter band, stated NON-EFFECTIVELY. In beta coordinates the band is

    1/(r_star+epsilon_N(c,b)) < beta < beta_star.

There is no computed epsilon or explicit numerical lower endpoint. The width is proved positive by the contradiction argument, not defined by assuming the desired order bound. In particular N=7 gives some such band with no PH of order<=7; it is NOT a proof at `beta^2=8/9`, and it is not an upper-order-eight construction.

## 8. Exact use of the named NR import and consequence-if-false

For EVERY `r>r_star`, the reproduced density calculation gives a strictly positive normalized continuous density. The literal H is rational and strictly proper; its unique pole of maximal real part is the SIMPLE REAL pole -c, since a>c and b>0 put the repeated conjugate pair strictly left, with no numerator cancellation. Thus all hypotheses of the statement-level O'Cinneide import supplied by Main are verified for this family, with no atom at zero.

At that **NAMED_NR** import, the minimum order m_PH(r) is finite for r>r_star. Combining with(LOW) gives the precise whole-function consequence

    m_PH(r) tends to infinity as r decreases to r_star from above,

in the quantified sense that EVERY finite N is eventually exceeded on the stated positive-width band. This is a non-effective lower-bound result, not an explicit finite minimum, numeric band, critical7/8 decision or novelty claim.

If the authorized characterization statement is false, incomplete or model-mismatched, the assertion of finite PH existence on the positive side and hence the finite-valued-minimum interpretation are not established. **The exclusion(LOW), closure proof and boundary non-PH contradiction do NOT depend on that import.** They remain exact written all-object lower-order statements at the supplied literal definition.

## 9. Limitations, inputs and current acceptance boundary

All current density/boundary statements retain the reproduction label. This new complete closure proof uses no old baseline, PH-closure theorem or held/unpublished method input. Its positive factorization, singular limit, actual probability/exit and Hurwitz restoration were proved inline. Prior exposure is not denied and no private-cognition/noninfluence certificate is claimed. Full mathematics AND dependency/application review must read this COMPLETE body plus the complete195LF input and current controls/literals/additive reproduction/NR qualification; pins or a terminal-case check do not suffice.

No actual new seven-state realization, explicit new finite upper order, computable epsilon, exact min8 at8/9, rational negative identity, book-image equivalence, primary O'Cinneide proof, independent source novelty/priority or stronger verification is delivered. The missing effective-band/critical-generator input is not supplied by a qualitative closure theorem. Same18/exclusiveNEWroot/scientificHOLD/N4UNKNOWN historical child exit unestablished/aux214STOP/alloldSTOP-ZERO-findings/v260consumers permanent; no scientific execution/modelCLI/nestedagent/newGO/selected numeric-state-control-boundary-decimal probe/Git-delete-contact-infrastructure action. Research deadline2026-10-31T21:23:27.000Z and truthful substantive cadence remain; no heartbeat/timer/poll/earlypark or continuous-service assertion.

**END — full unrestricted-rate fixed-order closure and non-effective all-topology near-boundary order exclusion; critical8/9 remains OPEN.**
