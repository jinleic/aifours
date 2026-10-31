# Actual k3 continuation v33 — TWO further GLOBAL common-projector angle constraints for M and spin flip

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 09:02:27 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN compatibility addendum, NOT global closure or an eligible counterexample.** Exact ALL-variable conventional proof from correct frozen full operators, under prospectivev51. No newly chosen state/control/numeric/boundary/limit/magnitude trial, decimal annotation, scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO. Every prior finding/quarantine/withdrawal remains. Same18/HOLD/OWNroot/cutoff/deadline, active original research not a park.

## 1. Literal ORIGINAL coordinates and THREE coupled positive traces

For EVERY pure four-qubit rho=|psi><psi| and EVERY complex rank-three orthogonal Pi use the SAME actual

    a=10-TrPi X1, b=12-TrPi X2, c=TrPi X3-6,
    d=1-<psi|Pi|psi>, delta=4-R,
    C=|<psi|Theta psi>|^2, zeta=TrPi tilde(rho).

The correct full operators, already present in oldv8, are

    A=3I-X2+3rho>=0,
    D=X1-X3, 0<=D<=2(I-rho),
    M=A+tilde(rho)=4I-X1-X3+4rho, 0<=M<=4I.

**M is NOT4I-Z.** Its actual relations are `Z+D+M=4I` and `<psi|M|psi>=delta`. Retaining this distinction matters for the new inequality. All operators and cross terms belong to the SAME actual input; no sum of unrelated positive compressions is used.

Their actual projector traces satisfy

    B=TrPi A=b-3d>=0,
    m=TrPi M=B+zeta=a-c-4d>=0,
    c=a-b-d-zeta, zeta>=0.                             (JOINT)

These identities are old frozen actual-map facts, not new discoveries. The NEW statements below apply a full all-variable angle lemma to them and to the ACTUAL pure spin-flipped state.

## 2. Correctness of the full positive contraction M, without an extra TC assumption

The ENERGY Gram proof of A>=0 is explicitly recalled in fullv32: half the sum of weight-two Pauli conjugations of tilde(rho), with actual multipliers27,-9,-1,3,3. Thus M=A+tilde(rho)>=0.

For clarity the other used operator inputs can also be derived directly. A two-qubit six-local-Pauli Gram has blocksI+iK1,T;T^T,I+iK2 with real antisymmetric K1,K2 and real T. After conjugation by diag(I3,iI3), it isI+iK with real antisymmetric K; its complex conjugate is2I minus that Gram and is PSD. Hence each pair Gram<=2I. Partition the four qubits into two pairs. Positivity and block Cauchy give the full twelve-Pauli Gram<=4I, and therefore its physical Kraus operator Z<=4I, since they have the same nonzero spectrum.

The Pauli-weight identity `Z-tildeZ=L` and antisymmetry of the spin-flip bilinear JS_mu give tildeZ psi=0. Thus0<=tildeZ<=4Q, Q=I-rho. Consequently

    D=2Q-tildeZ/2, 0<=D<=2Q,
    X1>=X3>=2rho.

The full-spin-flip inclusion/exclusion identity `tilde(rho)=I-X1+X2-X3+rho` gives the printed expression for M. Since X1+X3>=4rho, it implies M<=4I. Pure one-qubit Schmidt duality gives X1 psi=X3 psi=(2I+L/2)psi and therefore

    Mpsi=4psi-Lpsi=delta psi-v, v=QLpsi,
    <psi|M|psi>=delta.

These are conventional full complex Pauli/PSD proofs, not partial-transpose positivity, TC strengthening, numerical calibration or authentication of every old proof DAG. They reproduce correct OLDv8 facts only as explicit premises, not extra new-progress counts.

## 3. An ALL-variable positive-contraction/projector angle lemma

Let0<=T<=hI on any finite-dimensional complex Hilbert space, h>0, unit psi, tau=<psi|T|psi>∈[0,h], and an ACTUAL orthogonal projector Pi with d=1-<psi|Pi|psi>. Put m=TrPi T. Then

    m>=[sqrt((1-d)tau)-sqrt(d(h-tau))]_+^2,            (GENERAL)
    [tau-m-hd]_+^2<=4d(h-tau)m.                       (GENERAL-P)

Proof for0<d<1: write the actual normalized xi=Pi psi/sqrt(1-d)=sqrt(1-d)psi+sqrt d eta, eta perpendicular psi. Since T>=0, m>=<xi|T|xi>. Let D0=<eta|T|eta>, w=<eta|T|psi>. Positivity of BOTH T and hI-T gives

    0<=D0<=h,
    |w|^2<=min(tau D0,(h-tau)(h-D0)).

The two bounds cross atD0=h-tau. Below it the quadratic is bounded by `(sqrt((1-d)tau)-sqrt(dD0))^2`, whose interval minimum is the right side of GENERAL. Above it, the bound `(1-d)tau+dD0-2sqrt(d(1-d)(h-tau)(h-D0))` is nondecreasing in D0, so its minimum is the same boundary value. This proves GENERAL over the ENTIRE quantified interval, including zero/singular bounds, with no parameter instance or limiting viability probe.

At d0 the projector contains psi and m>=tau; at d1 the right side is0. Thus no zero vector is normalized. GENERAL is equivalent to `sqrt((1-d)tau)<=sqrt m+sqrt(d(h-tau))`. Squaring these nonnegative sides and retaining a positive part before the second square gives GENERAL-P. In particular a NEGATIVE tau-m-hd must NOT be squared into a false necessary constraint.

This is an ordinary positive-contraction angle inequality applied explicitly here. It is not a new method/novelty claim or a statement that arbitrary angle/trace tuples are physically realizable.

## 4. NEW direct a,c,d,delta coupling from the ACTUAL M

Apply GENERAL with T=M,h4,tau=delta and h-tau=R. Using JOINT gives

    a-c-4d
       >=[sqrt((1-d)delta)-sqrt(dR)]_+^2.             (M-ANGLE)

The polynomial guarded form simplifies because its linear d terms cancel:

    [delta-a+c]_+^2
       <=4dR(a-c-4d).                               (M-POLY)

This is a universal necessary relation between the SAME ORIGINAL a,c,d and actual input delta. It supplements, rather than merely repeats, the older linear inequality a-c-4d>=0. It handles R0,delta0,d0,d1 and all complex projector orientations directly. At d0 it gives a-c>=delta; no variance proxy or free scalar energy has been substituted.

The trace m still equals b-3d+zeta. Hence M-POLY cannot be checked by choosing a,c,d independently of b,zeta or the actual state. The full original quartic remains required; satisfying this new inequality is not a sufficient physical witness test or a global proof.

## 5. NEW spin-flip-overlap constraint, with complementary projector boundary

Apply GENERAL to the ACTUAL rank-one positive contraction T=tilde(rho), h1,tauC and m=zeta. Then

    zeta>=[sqrt((1-d)C)-sqrt(d(1-C))]_+^2,
    [C-zeta-d]_+^2<=4d(1-C)zeta.                     (SP-ANGLE)

Applying the same theorem to I-Pi gives additionally

    1-zeta>=[sqrt(dC)-sqrt((1-d)(1-C))]_+^2,
    [C+zeta+d-2]_+^2
         <=4(1-d)(1-C)(1-zeta).                    (SP-COMP)

These use the SAME actual pair of pure states psi,Theta psi and the SAME projector, not a freely chosen spin-flip overlap. In particular at C1 they recover zeta=1-d by both inequalities, with no phase normalization or division. At C0 and all projector endpoints they retain the correct automatic/nonautomatic branches. No source-control state was instantiated to obtain them.

Combining these with M-ANGLE and the whole ENERGY-anglev32 gives three simultaneously necessary lower controls on

    B=b-3d,
    zeta=a-b-d-c,
    B+zeta=a-c-4d,

from the respective actual input expectations tau=delta-C,C,delta. The separate extrema need NOT be simultaneously attainable: the actual full Apsi/Mpsi/tildepsi cross vectors remain coupled. Ignoring that warning would again replace the ORIGINAL state/projector problem by an unjustified scalar relaxation.

## 6. What remains genuinely unproved

New content is M-ANGLE/M-POLY and SP-ANGLE/SP-COMP at ALL actual input/projector parameters, as further global common-projector constraints alongside wholev32. They are neither another selected family theorem nor a closure of the entire original q(u)=d-cu+bu^2+au^3/quartic. A valid full result still needs a uniform derivation of that scalar predicate from ACTUAL joint maps/fibres, or an eligible exact physical state/projector/noise failure. No such conclusion is supplied.

The strict FACE/BRIDGE/NP source route ofv30 gives its separate ALL-input small-noise interval; it does not establish that the scalar constraints above suffice at every intermediate noise. Wholev27BISEP and the activeKoszulv29 route remain separate candidates. The later withdrawn noise-dependent purity/Rayleigh scout, its chosen instance/decimals and ALL consuming guidance remain ZERO and are not a premise or repaired branch here; all used A/M/tilde identities predate it in the actual frozen source.

Every old/new own/parent/peer process record, falseF3/ENTIREv22mathwithdrawal, v23duplicateZERO-new-progress/v41, PRIMARY073434/v44 and REVIEWv125format/v47 qualification remains permanent. Prospectivev51permission is not history/provenance absolution. Same18/HOLD/OWNroot/oldpinnedimmutable/Oct27cutoff11:05:38/deadline12:35:38PDT; no scientificinterpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nestedagent/GO/newparameterprobe/decimal/frozenedit/Git/delete/publication/newslot/model/deadlinereset/strongerformal/kernel/human/family/executable/novelty/earlypark/roundcloseout. Original unrestricted k3 research continues.
