# Actual k3 continuation v32 — a global ENERGY-angle inequality for the SAME actual b,d,R,C

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 08:55:11 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN universal compatibility lemma, NOT a full original-k3 proof or physical counterexample.** Exact ALL-variable conventional written proof under prospective parentv51; no new chosen state/control/numeric/boundary/limit/magnitude probe, decimal gloss, scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO. All old findings/withdrawals remain. This is an actual common-projector ENERGY coupling, not an unrelated norm or restricted input family.

## 1. Prior boundary and precise new statement

The complete earlier `depolarizing-actual-pair-compatibility-consolidated-v2.md` §6.1, LF230–256, was read: its existing bound is

    delta-C <=[sqrt((1-d)(b-3d))+sqrt(6d)]^2,

using the GLOBAL norm A<=6I and the original Pi decomposition of psi. The new inequality below uses instead the ACTUAL two-ray projector tilt relative to psi and the FULL operator interval `0<=A<=3I+3rho`. It is a complementary sharper operator-angle constraint, not a claim that the older coupling was absent or that every parameter regime is uniformly improved. The old source/parent assurance remains; no duplicate is counted as a new mechanism discovery.

For EVERY pure four-qubit rho=|psi><psi| and EVERY complex rank-three orthogonal projector Pi, define

    d=1-<psi|Pi|psi>,
    b=12-TrPi X2(rho),
    R=sum_i t_i^2, delta=4-R,
    C=|<psi|Theta psi>|^2, tau=delta-C,
    B=b-3d.

Then0<=d<=1,0<=tau<=4,B>=0 and

    B >=[sqrt((1-d)tau)-sqrt(d(3-tau/2))]_+^2.           (ANGLE)

Here[x]_+=max(x,0). Equivalently, with the POSITIVE-PART guard retained,

    [(1-d/2)tau-b]_+^2
              <=4d(3-tau/2)(b-3d).                     (POLY)

This is a necessary inequality for EVERY ACTUAL pure state/projector pair in the ORIGINAL quartic, with the SAME b,d,R,C. It is not a sufficiency/realizability theorem for free scalar tuples, nor a proof of that quartic. At d0 it gives b>=delta-C; d1 and all zero cases are included without normalizing zero vectors.

## 2. The full ENERGY operator, including positivity and its actual input expectation

Let

    A=3I-X2(rho)+3rho.

The standard pure/full-spin-flip ENERGY identity is

    A=(1/2)sum_(weight(P)=2) P tilde(rho) P >=0.

It can be checked WITHOUT a scientific program: the generating polynomial for conjugation by all weight-two Pauli strings is `(1+3x)^(4-w)(1-x)^w` on a weight-w Pauli coefficient. After global spin flip and the factor1/2 its FIVE multipliers are27,-9,-1,3,3 for w0..4. They equal those of3Tr(Y)I-X2(Y)+3Y. Full spin flip is a positive unitary-TOTAL-transpose map, not a partial-transpose assumption. Thus this is the ACTUAL full positive ENERGY Gram, not only separate positive compressions.

Since X2(rho)>=0 as a sum of positive erased marginals,

    0<=A<=3I+3rho.                                     (INTERVAL)

At the SAME original projector,

    TrPi A=9-(12-b)+3(1-d)=b-3d=B>=0.

For the pure input, the actual pair-purity identity gives `sum_(i<j)Tr(rho_ij^2)=2+R+C`; equivalently this follows from pure complementary marginal spectra/Pauli orthogonality and the global-spin-flip sector identity A2=2+R+4C. Hence

    <psi|A|psi>=3-(2+R+C)+3=4-R-C=tau.

This identity already occurs in the frozen ENERGY source; it is an INPUT expectation, not the later withdrawn output-purity/noise/Rayleigh scout. No selected moment/noise value or consuming inference from that branch is used or repaired. INTERVAL gives0<=tau<=6; the physical definition delta<=4,C>=0 sharpens it to tau<=4. All square roots below therefore have nonnegative arguments.

## 3. A complete ALL-variable two-ray operator lemma

First take0<d<1. Set

    xi=Pi psi/sqrt(1-d)
       =sqrt(1-d)psi+sqrt(d)eta,
    eta perpendicular psi, ||eta||=1.

Then Pi=P+|xi><xi| with P a positive rank-two projection orthogonal to psi and eta. A>=0 gives `B=TrPi A>=<xi|A|xi>`. Put D=<eta|A|eta>, w=<eta|A|psi>. Compressing BOTH sides of INTERVAL to span(psi,eta) gives

    [[tau,conj(w)],[w,D]]>=0,
    [[6-tau,-conj(w)],[-w,3-D]]>=0.

Therefore

    0<=D<=3,
    |w|^2<=min(tau D,(6-tau)(3-D)).                     (TWO-PSD)

The complex phase is retained: `Re w>=-|w|` is a one-sided adversarial bound, not a claim that the actual cross term vanishes or can be independently chosen physically.

The two upper bounds for |w|^2 cross at `D_*=3-tau/2`. For0<=D<=D_*, the lower quadratic is

    <xi|A|xi>
       >=[sqrt((1-d)tau)-sqrt(dD)]^2.

Minimizing this scalar expression on the ENTIRE interval gives0 if its zero occurs beforeD_*, and otherwise its endpoint value. Thus it is bounded below by the right side of ANGLE. ForD>=D_*, TWO-PSD instead gives

    <xi|A|xi>
       >=(1-d)tau+dD
                     -2sqrt(d(1-d)(6-tau)(3-D)).

This expression is NONDECREASING in D: its affine D term increases and its subtracted nonnegative square root decreases. Its minimum on this second interval is atD_*, the SAME boundary value already considered. No derivative division atD3, no generic strictness, selected parameter trial or omitted phase case is needed. The minimization is an exact theorem for ALL d,tau,D in their displayed domains, not an exploratory boundary/limit viability check.

Combining the two intervals and B>=<xi|A|xi> proves ANGLE. At d0, Pi contains psi and B>=tau directly. At d1 the right side is0, covered by B>=0; no xi is defined from a zero vector. The tau0 endpoint similarly gives0 directly. Degenerate/singular2x2 matrices are allowed throughout.

## 4. Exact polynomial form and its sign boundary

Let `H=d(3-tau/2)>=0`. ANGLE is equivalent to

    sqrt((1-d)tau)<=sqrt B+sqrt H.

Indeed if the first square root is<=sqrtH the assertion is automatic; otherwise subtract and square the nonnegative sides. Squaring the displayed inequality, using B+H=b-d tau/2, gives

    (1-d/2)tau-b <=2sqrt(d(3-tau/2)(b-3d)).

When the left side is nonpositive it is automatic; when positive, reversible squaring gives POLY. Retaining the positive part is REQUIRED—one must not square a negative left side and manufacture an extra necessary constraint. No division by d,1-d,tau,B or an ENERGY eigenvalue is used, so all zero and rank-deficient endpoints remain.

## 5. What is newly constrained in the ORIGINAL residual

At the named original scalar interface, a=10-TrPi X1>=0, c=TrPi X3-6 and the literal common-projector q(u)=d-cu+bu^2+au^3 remains the true problem. ANGLE/POLY now constrains its ACTUAL b,d using the SAME state's tau=delta-C, in addition to the original B=b-3d>=0 and the earlier v2 inequality. It cannot be obtained by setting unrelated moment coordinates independently, and it does not depend on a parity/Schmidt/product-overlap assumption.

It may be combined with the ACTUAL v6 off-face c/V bound, the actual spin-flip cross vectors, v21's original critical-system equations and other genuine state/projector identities. But no proof that these necessary conditions alone force q>=0, no free-tuple feasibility claim, no global output coefficient bound and no actual channel failure is supplied. The first missing step remains a uniform common-pair transfer to the full quartic/nonautomatic branch, not positivity of this isolated2x2 interval.

This packet is independent of unreviewed v20-v30 conclusions: its operative substantive interface is the correctly normalized full ENERGY identity and pure input pair-purity identity, both explicitly recalled/proved at the displayed Pauli/Schmidt facts. Its ordinary PSD/Cauchy/two-ray/positive-part facts are named finite-dimensional mathematics, not formal libraries. Newv30's INPUT-unrestricted small-noise interval andv27's direct BISEP theorem remain separately gated candidates; they do not accept this coupling or receive automatic adoption from it.

All original arbitrary-state/every-physical-noise quantifiers remain active; no positive cutoff replaces the task. No known-false FULL four-copy certificate is revived, and v23's repetition of oldv8 receives ZERO new-progress credit. F3falsefinal/ENTIREv22withdrawal and parentv35/v41, PRIMARY073434/v44 and REVIEWv125format/v47 findings, all older cadence/privateapproxZERO/pause/inventory/orientation/readorder/freeze/clock/admission/source/priority boundaries remain permanent. Exact new proofs do not cure history or certify unaffected private provenance. Same18/HOLD/OWNroot/oldpinnedimmutable/Oct27cutoff11:05:38/deadline12:35:38PDT; no scientificGO/probe/replay/CLI/nestedagent/frozenedit/earlypark/roundcloseout/strongerformal/human/family/executable/novelty acceptance.
