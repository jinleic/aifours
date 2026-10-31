# P44 prerequisite addendum2 — exact state-specific positive-reconstruction classification

Owner **PhysicsPPT44-2**, physics-3. Actual native `/bin/date` immediately BEFORE this NEW immutable write: **Tue Oct 27 15:15:34 PDT 2026**. **WRITTEN, UNREVIEWED**, no mathematical identity machine-checked.

The assigned w15-math-4-add3 review was completed and actually returned before this continuation. Main's standing15:08:03 direction leaves the existing S1 release in force for the next genuinely admitted all-variable step. This proof stays inside that definition-side scope; it does NOT enter the accepted-stopped nonunitary-filter/marginal-balancing branch or open a source.

## 1. What is genuinely stronger than addendum1

Current author inputs are the COMPLETE new-round derivation v1 (`7d00196376108da34c416b8e80f815adfc337d01cb24191f8ad40f6a47d8cdc4`,208LF) and addendum1 (`02beb05df29588703aa46ced25d103ea6ec1aefcbf042c61f6f3df1c1d2d29bf`,111LF), with their stated S2/elementary premises. These are AUTHOR-WRITTEN UNREVIEWED premises, not parent adoptions or independent reviews. No old proof/guide or JL construction is input.

Addendum1 excluded a FIXED positive linear-map resolution of the identity. It expressly did NOT settle recovery of one actual rho with coefficients and rotations chosen from that rho. The present theorem closes exactly that loophole for the SAME complement/noise/unitary/input-transpose family and gives a FULL forward-and-converse classification of its recoverable original objects.

**Result:** a nonzero original PPT rho can lie in the closed positive cone of its own allowed complement/noise orbit ONLY IF it is a product with a completely mixed local factor. Conversely EVERY such product lies in that cone. This is an exact method-classification theorem, NOT a new classification of PPT Schmidt numbers or an original P44 answer.

## 2. Actual map family, including state-dependent choices

Let A=C^a,B=C^b, with arbitrary a,b>=3; the original case is a=b=4. Keep

    D_A(X)=I_A tensor Tr_A X,   D_B(X)=Tr_B X tensor I_B,
    D_0(X)=Tr(X)I_AB,           R_A=D_A-id, R_B=D_B-id.

T is ANY finite word of local-unitary conjugations and Gamma_A/Gamma_B. L is ANY local-unitary output conjugation. Generators are

    F=L R_A^p R_B^q T,       p,q>=0, p+q>=1,
    N=L D T,                D in {D_A,D_B,D_0}.             (2.1)

For an ACTUAL fixed PPT rho, define K(rho) as the closure of the cone of all finite nonnegative sums of F(rho) and N(rho). Coefficients, exponent choices, unitary rotations and input-transpose words may ALL depend on rho, without any continuity/linearity requirement on that choice rule. The resulting Y is simply a member of the indicated cone at that rho.

Each generator actually produces a positive C2 output for PPT inputs, by the complete earlier rank-two congruence proof and its PPT preservation. All finite positive sums and their limits are therefore actual positive outputs; no unrelated ambient source is substituted. The cone notation here refers to a DEFINED generating family and norm closure, not an algorithm, solver or enumeration.

No arbitrary output partial transpose after the final C2-producing block is added. Its SN2-preserving property has not been proved. No nonunitary local congruence, inverse marginal, balancing/scaling or chosen physical test state is included.

## 3. Full actual-object projections

Write s=Tr rho. On the ENTIRE Hermitian operator space let

    P00(X)=Tr(X)/(ab) I_AB,
    U(X)=(Tr_B X-Tr(X)/a I_A) tensor I_B/b,
    V(X)=I_A/a tensor (Tr_A X-Tr(X)/b I_B),
    C(X)=X-P00(X)-U(X)-V(X).                              (3.1)

These are exactly the identity, Alice-local-traceless, Bob-local-traceless and doubly-traceless projections. In particular both partial traces of C(X) vanish. This decomposition does not change X or assert any physical state can be replaced by a projected component.

Every T and L in(2.1) preserves EACH of the four sectors, is orthogonal there for the Hilbert–Schmidt norm and fixes I. This follows from trace cyclicity, transformation of the two partial traces under local conjugation, and entry-permutation invariance of full/partial transpose, as proved on the ENTIRE operator space in addendum1. No particular real/complex matrix is tested.

Put

    r_F=(a-1)^p(b-1)^q.

Every F therefore satisfies the ALL-INPUT identities

    Tr(F(X))=r_F Tr X,
    ||U(F(X))|| = r_F/(a-1)^p * ||U(X)||,
    ||V(F(X))|| = r_F/(b-1)^q * ||V(X)||,
    ||C(F(X))|| = ||C(X)||.                               (3.2)

The signs on the traceless sectors disappear ONLY because a norm is taken; they were not replaced by positive operator identities. The transformations before/after the complement block remain orthogonal even when they do not commute with one another.

For a noise generator, trace multiplier r_N is a,b or ab. Its C output is zero. Relative to that trace multiplier, its U/V norm factors are respectively

    D_A: (0,1),       D_B: (1,0),       D_0: (0,0).         (3.3)

Input/output local-unitary and transpose words leave these exact norm factors unchanged. The norms in(3.2)–(3.3) are mathematical quantities for arbitrary operators, not computed values, finite controls or imported unbalanced-norm estimates.

## 4. State-specific correlation contraction — coefficients need NOT be fixed

Assume rho is nonzero and positive, so s>0. Define

    mu=min(a-1,b-1)>1.

For any finite positive output Y=sum c_F F(rho)+sum d_N N(rho), trace accounting gives

    Tr Y=s(sum c_F r_F+sum d_N r_N),
    Tr Y >= mu*s*sum c_F.

Triangle inequality on the ACTUAL C components, together with(3.2), gives

    ||C(Y)|| <= ||C(rho)|| sum c_F
             <= Tr(Y)/(mu*s) * ||C(rho)||.                (4.1)

There is no assumption that the coefficient selection was independent of rho. No marginal eigenvalue or witness expectation is divided by. Continuity of trace and the finite-dimensional norm passes(4.1) to EVERY Y in K(rho).

If rho itself belongs to K(rho), substitution of the SAME rho into this proved ALL-output inequality gives

    ||C(rho)|| <= ||C(rho)||/mu.

Since mu>1, **C(rho)=0** is necessary. This is not a selected-state viability calculation: the theorem quantifies over every positive rho, every allowed choice rule and every generated output; the displayed equality is its exact original-object caller.

Thus arbitrary rho-dependent positive coefficients and arbitrary rho-dependent local-unitary/input-transpose choices do NOT escape the doubly-traceless obstruction. This is a real strengthening of the fixed-superoperator result.

## 5. Both local deviations cannot survive either

Now suppose C(rho)=0. Let u=||U(rho)|| and v=||V(rho)||. If BOTH are positive, set

    eta=max(1/(a-1),1/(b-1))<1.

For a complement monomial put alpha=(a-1)^(-p), beta=(b-1)^(-q). Nonemptiness p+q>=1 implies

    alpha+beta <= 1+eta.

Indeed if exactly one exponent is zero its corresponding factor is1 and the other is at most eta; if both are positive both are at most eta, whose sum is at most1+eta. This covers ALL exponents, not a selected finite set.

For every finite positive output Y, equations(3.2) and triangle inequality therefore give

    ||U(Y)||/u + ||V(Y)||/v
      <= (1+eta) Tr(Y)/s.                                (5.1)

The optional noise outputs satisfy the same bound because their normalized factors in(3.3) have sum at most1. Again the coefficient/rotation choices may depend arbitrarily on rho. Since u,v are fixed positive quantities in this case, continuity passes the inequality to K(rho).

Taking Y=rho would require 2<=1+eta, impossible. Hence **rho in K(rho) requires U(rho)=0 OR V(rho)=0**, in addition to C(rho)=0. The zero-deviation cases are NOT treated by dividing by zero; they are handled separately next.

## 6. COMPLETE forward and converse classification

**Theorem.** For EVERY PPT rho>=0 on A tensor B with a,b>=3,

    rho in K(rho)
      IFF rho=(I_A/a) tensor rho_B
          OR rho=rho_A tensor(I_B/b).                    (6.1)

This includes rho=0.

**Forward for s>0.** Sections4–5 force C(rho)=0 and at least one local deviation zero. If U(rho)=0, equation(3.1) becomes exactly `rho=(I_A/a) tensor rho_B`. If V(rho)=0 it becomes the other displayed product. No state is replaced by an unrelated model, and the actual marginal is retained.

**Converse.** If `rho=(I_A/a) tensor rho_B`, then D_A(rho)=a rho and R_A(rho)=(a-1)rho. Therefore the ACTUAL positive generator `(1/(a-1))R_A(rho)` is rho itself and lies in the defined cone. The other family uses R_B in exactly the same manner. These are universal exact identities on the full derived families, not test states or scalar probes. For rho=0, K(0) contains0 and both product formulas hold. Degenerate/singular marginal spectra introduce no exception.

The theorem has a genuine forward AND converse actual-object caller and allows ALL state-dependent choices in(2.1). It is not merely a necessary fixed-map spectral condition.

## 7. Additional original coupling: vanishing C is already separable

A useful independent consequence of the same decomposition is that **any positive rho with C(rho)=0 is separable**, whether or not it is recoverable by(2.1).

Let lambda_i and nu_j be the spectra of its ACTUAL positive marginals rho_A,rho_B, in arbitrary local eigenbases. Equation(3.1) makes rho diagonal in their product basis, with coefficients

    lambda_i/b + nu_j/a - s/(ab).

Every such coefficient is nonnegative because rho itself is positive; their sum is s. Thus this is an actual positive product-projector decomposition. All multiplicities, zero eigenvalues and nonunique eigenbases are allowed. No inverse marginal, nonunitary basis transformation, numerical spectrum or old rank-chart theorem is used.

Consequently EVERY possible original negative pair rho,W must have C(rho)!=0: otherwise rho is separable and its expectation against a two-block-positive W cannot be negative. Section4 then shows that its own allowed positive complement/noise orbit cannot reconstruct rho, even with rho-dependent coefficients and rotations. This is an exact coupling/method obstruction, NOT a constructed negative pair or a proof that it exists.

The recoverable states in(6.1) are visibly separable products; this is NOT counted as a new nontrivial PPT Schmidt-number region. The substantive advance is the COMPLETE state-specific reconstruction classification and its exclusion of the old coefficient-dependence loophole. Failure of the method cannot be converted into SN3 evidence: it is only failure of this particular generating cone, which is stricter than the full C2 cone.

## 8. Exact remaining task and boundaries

The fixed-complement construction and its admitted local-unitary/input-transpose/noise enlargement are now classified even at each ACTUAL source state. Repeating those operations or changing their rho-dependent positive weights cannot furnish the missing original all-state proof except at the trivial product families in(6.1).

The original next mathematical need remains a coupling outside THIS generating family, or an actual eligible exact rho,W pair. The accepted-stopped nonunitary-congruence/marginal-balancing branch is NOT resumed; no guide, formula, inverse filter or normalization from it appears here. Main's standing S1 authority permits other genuinely input-clean elementary work, not old-source expansion, but it does not make the absent stronger coupling available by assertion. A frozen review of this COMPLETE three-packet union is now appropriate before any adoption; no favorable review is assumed as proof.

No claim of novelty or absence from the old files is made, and no prohibited old body was opened to investigate it. Only current S2 definitions and the displayed elementary spectral/direct-sum/trace/norm facts are used. All mathematical arguments are WRITTEN; no interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, selected state/control/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/contact/publication/infrastructure mutation occurred.

All history/STOP/HOLD/ZERO, N4 UNKNOWN/historical child exit unestablished, old21 NR and auxiliary214 STOP persist. No formal/kernel/executable/human/configured-family/novelty or original P44 acceptance. Same S1 narrow definition-first scope and successor research deadline2026-10-31T21:23:27.000Z; no new source, blanket restart or window closeout.
