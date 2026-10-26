# Shor common mates — exact carry cocycle, reset control, and a bounded-potential obstruction

Owner MathShor / MathShor-2. Actual `/bin/date` before writing: **Sun Oct 25 15:49:00 PDT 2026**. WRITTEN CANDIDATE, unreviewed. No scientific interpreter/program/arithmetic execution/enumeration/replay/solver/CLI/nested agent/new GO. This is an all-order mathematical control on a new representation, NOT an answer to the original Shor question.

The bounded v94-B review was ACTUALLY returned to Main at the observed15:33:52 clock before this primary work resumed. Its337-LF output has SHA256 `f9981ff7f373d0b64b63a45aa6bd0dc1be7a602f383bb22c2fe3bc9d03d5151f`. This primary packet is not part of that review and cannot change its verdict.

## 0. Exact interface and scope

Assume ONE cyclic direct tile A at order n has complements B,D2,D3 with

    I={0,3,8,11} subset A,
    J0={0,1,7,13,14} subset B,
    J2={0,2,4,6} subset D2,
    J3={0,1,2} subset D3.

Choose canonical representatives in{0,...,n−1}. The literal seeds are distinct; the earlier common-mate interface gives n>=1320, but the new proof uses only the distinct displayed seeds and n>14. Set a=|A|,b=|B|=|D2|=|D3|,ab=n.

This hypothesis is NECESSARY for any original finite raw UD factor-complete superset of C. Its existence is not established. Under this hypothesis define the EXISTENCE-normal-form row code

    D_0=B, D_3=D_8=D2, D_11=D3,
    D_i=B for every other i in A,
    Y=union_(i in A) ({i} x D_i).

The actual original one-b set of a hypothetical completion is NOT assumed equal to Y. Replacing it by this normal form has NOT been proved to preserve finite completability.

Named local interface: `shor-common-complement-uniform-trades-consolidated-v1.md`,255LF,SHA256 `1697ed1a7d7051d9c5a63e2531abb539e7af96e12a41046c8e862adc51b7ca83`, itself WRITTEN/unreviewed. Its §§1–2 derive the common-mate necessity and the all-t border decoder, and distinguish raw UD from completeness. The new finite-algebra and carry claims below are proved directly. No H*, known-construction exhaustiveness, literature classification or execution receipt is an input.

## 1. Exact deterministic labelled carry system

For EVERY state i in A and EVERY input r in Z_n, the direct tiling D_i+A gives a UNIQUE pair

    j_i(r) in D_i, F_r(i) in A,
    j_i(r)+F_r(i) = r + n c_i(r),       c_i(r) in{0,1}.       (1)

All quantities in (1) are actual canonical integers, not formal independent phases. The carry is only0 or1 because both summands lie between0 and n−1. Thus each r acts as a deterministic map F_r:A->A with an output label j_i(r) and an exact nonnegative carry c_i(r).

A path with inputs r1,...,rt has states i_s=F_(r_s)(i_(s−1)) and total carry

    K_t=sum_(s=1)^t c_(i_(s−1))(r_s).                       (2)

This state/carry system describes CYCLIC one-b decoding. It does not insert raw bridges, cancel a^n inside words, or claim an actual raw parsing at a short gap whose canonical carry is1.

## 2. A finite closed residue algebra is automatic

For any row-label function f:A->{B,D2,D3}, let

    Y_f=union_(i in A) ({i}x f(i)).

Every such set has n pairs. Every mate f(i) complements the SAME A. Hence the successive border decoder gives a bijection B x Y_f^t x A -> Z_n^(t+1) for every t; more generally it gives a bijection for ANY heterogeneous sequence Y_f1,...,Y_ft, by using the appropriate mate at each step.

Define the usual interior-residue composition purely as a relation:

    Y_f circle_r Y_g
      ={(i,l): exists j,k with(i,j)inY_f,(k,l)inY_g,j+k=r modn}.

For each fixed i there is exactly one (j,k)in f(i)xA with j+k=r. Consequently

    Y_f circle_r Y_g
      = union_(i in A) ({i}x g(F_r^f(i))).                  (3)

It is another member of the SAME row-label family. The entire residue closure is finite, of size at most3^a, regardless of which compositions or input residues are used. The bound is finite for each hypothetical witness, not uniform in unknown n.

This is a PROOF of exact closure, not a finite search. It also explains why finite closure of residue types cannot by itself be announced as raw STAB: it is already automatic here, while the raw M0 below remains incomplete.

## 3. Every A-input is a genuine reset with ZERO carry

Every mate contains0. Therefore, for any r in A and ANY i in A, the decomposition of r is exactly

    j_i(r)=0, F_r(i)=r, c_i(r)=0.                          (4)

Uniqueness follows from the actual direct tiling f(i)+A. In particular the input0 resets all states to0, and input3 resets all states to3. These are not eventual or sampled resets: they hold at ONE step on the entire state space.

Thus an abstract synchronizing word exists automatically. A claimed implication from abstract synchronization to original finite raw completion would need an additional theorem that is not supplied by (3) or (4).

## 4. The forced short input1 has carry1 at row3

First1 is NOT in A: otherwise the distinct pairs(0,1)and(1,0)in A x B both represent1. Also1 is NOT in D2: otherwise the distinct pairs(0,4)and(3,1)in A x D2 both represent4.

At row3 the mate is D2. An integer nonwrapped representation of the input1 would have to be(0,1)or(1,0). Both are impossible by the preceding exclusions. The unique CYCLIC representation must therefore satisfy

    j_3(1)+F_1(3)=n+1,
    c_3(1)=1.                                             (5)

The same is true at row8. This conclusion holds for EVERY unknown n,A,B,D2,D3 satisfying the gate; no unknown tail support is omitted.

By contrast at state0, D_0=B and the actual pair1inB,0inA gives

    F_1(0)=0, c_0(1)=0.                                   (6)

Let k=F_1(3), whose value is unknown and need not be classified. Input3 resets k to3 with carry0 by (4). Consequently the TWO-input path

    3 --input1,cost1--> k --input3,cost0--> 3              (7)

is an ACTUAL cycle in this residue/carry system. Repeating(1,3) m times returns to3 and has total carry exactly m for EVERY m>=1.

This is an unbounded family with all unknown states retained, not an inconsequential bounded enumeration or a claimed raw-code nontermination certificate.

## 5. No bounded telescoping potential, even with input-only surcharges

### 5.1 State-potential obstruction

There do NOT exist real-valued functions phi:A->R and psi:Z_n->R such that

    c_i(r)=phi(i)-phi(F_r(i))+psi(r)                        (8)

for EVERY state/input pair. This is stronger than excluding an integer potential or a pure coboundary.

Proof. At the0 self-loop of input1, (6) forces psi(1)=0. At the3 self-loop of input3, (4) forces psi(3)=0. Sum (8) along cycle(7). The phi terms telescope and its input surcharges sum0, whereas the actual left side is1. Contradiction.

Thus state-dependent offsets plus independent input-dependent offsets cannot remove the raw carry discrepancy in this canonical row-normal model.

### 5.2 ANY bounded history extension still fails as a telescoping correction

The same obstruction persists if the state is enlarged arbitrarily, provided:

- every original input path is still available from a lift of its starting state;
- lifted edges preserve the original carry and input;
- a proposed correcting potential Phi is UNIFORMLY bounded on lifted states;
- the correction still has the form carry=Phi(before)-Phi(after)+psi(input).

The lift need not even be finite. A finite-state lift would in particular have bounded Phi.

For the path consisting of m input1's from original state0, the total actual carry is0. Telescoping gives0=bounded endpoint difference+m psi(1); letting m be arbitrary forces psi(1)=0. Repeating input3 from state3 likewise forces psi(3)=0. But the lifted path(1,3)^m from3 has actual carry m, which would equal a uniformly bounded endpoint difference+m[psi(1)+psi(3)]. This is impossible for arbitrary m.

This rules out a PARTICULAR bounded-correction proof strategy on the ENTIRE transition system. It does not rule out new raw multi-b bridges, history-dependent nonseparable edge costs, or a genuinely different realization.

## 6. Exact carry count and an invariant moment check

For ANY mate D of A, enumerate the unique canonical decompositions j(r)+k(r)=r+n c_D(r) for all r. Every pair(D,A) occurs once. Therefore

    sum_r c_D(r)
      =[a sum_(j in D)j + b sum_(k in A)k - n(n-1)/2]/n
      = mean(D)+mean(A)-(n-1)/2.                           (9)

This is an INTEGER equal to the actual number of wrapped sums, not a floating average. For two mates D,E, subtraction yields

    b divides sum_(j in D)j - sum_(j in E)j.                (10)

For D2 versus B, the seven fixed signed contributions to the latter difference sum−23; the unrestricted remaining signed exponents must compensate23 modulo b. This is a check on an eventual witness, not an all-order contradiction: those exponents and b remain unknown and unbounded. I do not promote (10) to a fresh global order lower bound.

If a mate has no carries at all, its INTEGER mask product with A is S_n, with no cyclic wrap. For a fixed nonzero integer mask A such an integer complement is unique, since Z[z] has no zero divisors. Distinct D2/B therefore cannot both be carry-free. Equation(5) is a stronger C-specific explicit carry certificate, not just this uniqueness observation.

## 7. Why this still does NOT solve original finite completion

The row code gives the finite RAW UD set

    M0={a^n} union {a^i b a^j:(i,j)inY}.

The all-t border proof gives UD of M0, but NOT factor completeness. The earlier finite-code Bernoulli identity would force, if M0 were complete,

    sum_Y x^(i+j)=1+x+...+x^(n−1).

The sixteen C pairs contribute sixteen terms with degree<=14, whereas the right side has only fifteen such terms, so M0 is necessarily incomplete. No common-mate witness has actually been found; this is an all-witness conditional statement, not a concrete counterexample whose existence has been established.

The new facts coexist exactly as follows: a hypothetical witness supplies a FINITE residue-composition algebra, a ONE-STEP synchronizing reset, and nevertheless an UNBOUNDED positive carry cocycle and an incomplete raw M0. One cannot identify any of these residue properties with the original raw finite STAB/GP target.

A finite completion of the ORIGINAL C might have an actual Y different from this chosen existence normal form. No preservation theorem allows us to replace that Y and its other words by Y_f. Moreover actual multi-b bridge words can change the available raw cuts/costs rather than merely add a bounded state potential to (1). They could in principle repair a repeated residue cycle using a repeatable finite macroblock. No proof of such repair, nor a proof that EVERY repair violates UD/completeness, is supplied.

Accordingly the ORIGINAL remaining gap is unchanged: ALL actual PR-saturated finite raw prefixes, arbitrary endpoint sets/orders/word lengths/b-counts/heterogeneous delays/bridge arities, and eventual raw STAB must be handled. H* remains WITHDRAWN. The k7/Phi_n-divisible and all larger trade cases from the primary packet remain live. This packet blocks a concrete bounded-cocycle shortcut; it is not an arbitrary-delay theorem or a uniform raw noncompletion argument.

## 8. Bounded source refresh, CONTEXT ONLY

After the actual review return I read the abstract/introductory theorem statements of Laba–Londner, *Splitting for Integer Tilings*, author PDF `https://personal.math.ubc.ca/~ilaba/preprints/splitting.pdf`, pp1–4, and Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*, author PDF `https://www.normalesup.org/~cordero/Publications/Factorizations_and_Bayonet_Codes.pdf`, pp1–5. An ar5iv fetch timed out before the successful author-PDF read. I did NOT read either whole paper or reconstruct their full proof DAG in this continuation.

The splitting/T2 theorem has explicit prime-size and lower-divisor tiling hypotheses; it is not a proof of all-order splitting consistency or a replacement for the withdrawn product-plus-universal H*. Cordero distinguishes n-cbc completeness from finite maximal-code completeness and states the latter's ALL-omega cardinality criterion. These are context for why finite residue closure is not the missing raw realization theorem, not correctness premises of §§1–6, a current worldwide openness certificate, or novelty clearance.

All new identities above were checked in WRITING only. No executable, formal/kernel, configured-family, human, independent review, scientific-run admission or priority acceptance is claimed. The original October27 cutoff/deadline and HOLD are unchanged. The round is not closed.
