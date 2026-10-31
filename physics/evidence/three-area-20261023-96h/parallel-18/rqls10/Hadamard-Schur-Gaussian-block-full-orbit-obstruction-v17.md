# RQLS10 v17 — corrected Gaussian-block matrices and an ENTIRE all-monomial-orbit obstruction

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 06:33:20 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact field/unitary/character/graph reasoning only; no interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no private decimal/approximate scouting or discarded-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

MANDATORY predecessor qualification: `global-Hadamard-Schur-v14-model-erratum-e1.md`,39LF,SHA256 `f93806b235e24011b6c7b408cf83d5e5b0a8ba826a8b897c875a3bbcda3ed879`, withdraws v14's printed non-Hadamard MODEL and its alleged actual Butson-orbit application. That mathematical MAJOR remains. The present source specifies DIFFERENT, correctly constructed matrices and gives a NEW uniform proof; it is outside all earlier freezes and cannot repair their chronology.

Original unrestricted maximal1-RQLS10 remains UNKNOWN. This closes an entire exact Hadamard construction family under ALL row/column permutations and arbitrary unit phases, not all Hadamards or the unrestricted1-RQLS problem.

## 1. Full family and theorem

Let zeta=exp(2*pi*i/5), r=sqrt5. Let q,l be ARBITRARY elements of F5 satisfying

    q!=0, l!=0, l-q!=0.

Put

    theta=Legendre(q) in{+1,-1},
    sigma=Legendre((l-q)/q) in{+1,-1}, delta=-sigma,
    R0=1/(4q), R1=-1/(4(l-q)).

Index rows T_i,B_k and columns(0,j),(1,j), all i,k,j in F5. Define the unit-entry matrix

    H_(T_i),(0,j)=zeta^(i*j),
    H_(T_i),(1,j)=zeta^(l*i^2+i*j),
    H_(B_k),(0,j)=zeta^(R0*(j-k)^2),
    H_(B_k),(1,j)=delta*zeta^(R1*(j-k)^2).           (H)

**Theorem.** EVERY H in this family is Hadamard, but NO matrix monomial-equivalent to H has a Fourier-Schur Hadamard companion. This includes ALL row permutations, ALL column permutations and arbitrary unit row/column phases. No member can solve the Hadamard master of v14, even before maximal noncollision is imposed.

The family is the complete displayed diagonal-quadratic McNulty-Weigert block family with F=F5, K=D_q F5,L=D_l F5. No assertion that it exhausts all McNulty-Weigert choices, all BH(10,5), all BH(10,10) or arbitrary order10 Hadamards is made. No catalogue equivalence/classification is a proof premise.

## 2. Actual Hadamard property and exact cross sums

Use normalized F5 and D_a=diag(zeta^(a*j^2)). The unitary block matrix

    W=(1/sqrt2)*[[F5,D_l F5],
                [(D_q F5)^dagger F5,-(D_q F5)^dagger D_l F5]]

has orthogonal row blocks by direct multiplication. Completing the exact5-term quadratic Gauss sum gives

    [(D_q F5)^dagger F5]_(k,j)
       =(theta/r)*zeta^((j-k)^2/(4q)),
    -[(D_q F5)^dagger D_l F5]_(k,j)
       =-(sigma*theta/r)*zeta^(-(j-k)^2/(4(l-q))).

Multiplying each bottom row by theta is a unit phase and gives precisely H/sqrt10. Thus H*H^dagger=10I with unit entries. This derives the signs AND the quadratic exponents, not just their Legendre classes.

For a top-bottom row pair(T_i,B_k), the exponent differences ignoring the explicit delta in the second block are

    L0(j)=i*j-R0*(j-k)^2,
    L1(j)=l*i^2+i*j-R1*(j-k)^2,
    p=q*i^2+i*k.

The EXACT completed squares are

    L0(j)-p=-(j-k-2q*i)^2/(4q),
    L1(j)-p=(j-k+2(l-q)*i)^2/(4(l-q)).              (SQ)

Therefore

    sum_j zeta^L0(j)=theta*r*zeta^p,
    sum_j zeta^L1(j)=sigma*theta*r*zeta^p.

Since delta=-sigma, the full two-block row inner product vanishes, as the block proof requires. These formulas explicitly show why v14's mismatched fourth exponent could not give orthogonality.

## 3. The necessary zero-graph criterion under ALL monomial changes

For any Hadamard H, a Fourier-Schur companion H' entrywise*F10 forces, on the five physical row pairs j,j+5,

    [H'*diag((-1)^k)*H'^dagger]_(j,j+5)=0.

Thus its simple off-diagonal zero graph has a perfect matching. Row permutations/phases relabel this zero graph or multiply edges by nonzero phases; column phases cancel, and arbitrary column permutations turn diag((-1)^k) into EVERY balanced5-plus/5-minus sign diagonal J.

It is enough to prove: for EVERY such J, H*J*H^dagger has no zero-graph perfect matching. This argument is completely supplied here; it does not use v14's invalid MODEL or its old cross-phase calculation.

Changing J to -J preserves zeros. Thus its plus columns can always be written

    (0,j), j in A; and (1,j), j NOT in B,
    |A|=|B|=a<=2.                                  (SPLIT)

This is an ALL-balanced-split parameterization, not a selection of tested subsets. For a distinct pair of rows, since their full inner product is zero, the J-twisted product vanishes iff the sum over plus columns vanishes.

We use the elementary cyclotomic coefficient rule: if integer n_0,...,n_4 satisfy sum n_t*zeta^t=0, then all n_t are equal, because1+x+x^2+x^3+x^4 is the minimal polynomial. In particular sum n_t is divisible by5. When its coefficient sum is0, the coefficient vector itself is zero. No code or character-table enumeration is needed.

## 4. The sign-minus case delta=-1: NO cross zero edge for ANY balanced split

Here sigma=+1. The plus-column top-bottom sum is

    sum_A zeta^L0(j)+sum_B zeta^L1(j)
       -sum_(all j) zeta^L1(j).                    (MINUS)

For a=1 or2, the integer coefficient sum of this expression is2a-5, which is NOT divisible by5. Hence it cannot vanish by the cyclotomic rule. For a=0 it is minus the NONZERO Gauss sum theta*r*zeta^p. Thus the zero graph has NO T/B cross edges for EVERY balanced J.

Each row half has ODD size5. Any matching covering all10 vertices would need an edge between the halves, impossible. This closes the entire delta=-1 family under all monomial equivalences, without restricting its within-half edges or a column ordering.

## 5. The sign-plus case delta=+1: at mostFOUR cross edges

Now sigma=-1. The top-bottom plus-column condition is

    sum_A zeta^L0(j)-sum_B zeta^L1(j)
       =theta*r*zeta^p.                            (PLUS)

For a=0 it is impossible; for a=1 its left modulus is at most2, while r>2. These cases again have no cross zero edge and fail perfect matching.

At a=2 use the EXACT coefficient identity

    r=zeta+zeta^-1-zeta^2-zeta^-2.

After dividing by zeta^p, both sides of PLUS have integer coefficient sum0. The cyclotomic rule forces EXACT coefficient equality. Since both sides have exactly two positive and two negative unit terms, no cancellation/repetition can be hidden: the two L0-p phases must be precisely the two exponents in the Legendre-theta class, and the two L1-p phases the two exponents in the opposite class.

By SQ, the first coefficient A0=-1/(4q) has Legendre symbol theta, while A1=1/(4(l-q)) has Legendre symbol-theta. Each phase pair is therefore{A0,-A0} or{A1,-A1}. Equivalently their two offsets squared must be{1,4}.

For a two-element set S={s,t}, there are EXACTLY TWO centers h with

    {(s-h)^2,(t-h)^2}={1,4}:
    C(S)={4s+2t,2s+4t}.                            (CENTERS)

Proof: the condition implies sum of the two squares is0, whose quadratic equation in h has exactly those two roots. Neither root is s,t, and their offsets are nonzero with different square values. This proves necessity and sufficiency without checking individual S choices.

Thus a cross zero edge(T_i,B_k) requires

    h=k+2q*i in C(A),
    h'=k-2(l-q)*i in C(B).

The map(i,k)->(h,h') is invertible because h-h'=2l*i and l!=0. Each of the two center sets has size2, so there are at mostFOUR such cross zero edges, regardless of their arrangement. We do NOT assert they are all incident to T0; that was specific to v14's invalid MODEL and is not reused.

## 6. At least one row half has NO internal zero edge

For two top rows T_i,T_i', put d=i-i'!=0 and s=i+i'. Their block differences are d*j and d*j+l*d*s. The full second-block sum is0. The plus-column condition and cyclotomic rule imply

    A=B+l*s as SETS.

Therefore an internal top edge is possible only if the nonzero gap of A equals the gap of B, up to sign.

For two bottom rows B_k,B_k', the block differences are

    -2R0*d*j+R0*d*s,
    -2R1*d*j+R1*d*s.

The explicit delta signs cancel in a bottom-bottom product. The same set comparison implies that the gap of A is(R1/R0) times that of B, up to sign. But

    R1/R0=-q/(l-q)

is a NONSQUARE here, because sigma=-1 and -1 is a square in F5. Thus it is not+/-1. The top and bottom necessary gap conditions cannot BOTH hold. At least ONE half therefore has no internal zero edge at all.

That half has five vertices. A perfect matching would need FIVE distinct cross edges to cover it, while Section5 proves there are at mostFOUR. Contradiction. This closes a=2 and hence EVERY balanced sign diagonal in the delta=+1 family too.

Sections4-6 prove the stated theorem for all q,l in the displayed parameter domain and ALL monomial equivalents. This is a full symbolic family proof, not an enumeration of12 parameter choices or a collection of subset tests.

## 7. Concrete corrected models and what is not retroactively repaired

For q=1,l=3, the actual fourth block has exponent3(j-k)^2. The correct matrix is

    T_i=(zeta^(i*j), zeta^(3i^2+i*j))_j,
    B_k=(zeta^(4(j-k)^2), zeta^(3(j-k)^2))_j.

It IS Hadamard by Section2, and its ENTIRE monomial orbit is now excluded by the NEW all-split proof. For q=1,l=2 the fourth block is -zeta^((j-k)^2), and the sign-minus argument closes its entire monomial orbit too. These are transparent examples of the parameter theorem, not evidence from a finite trial.

Neither is the incorrectly printed v14 matrix, whose top coefficient3 was paired with bottom coefficient2. That original source and its MAJOR finding remain immutable. A later valid theorem at the intended construction family does not make the invalid source Hadamard, preserve its erroneous intermediate cross-phase claim or backdate the new proof into an earlier review freeze.

## 8. Original residual and assurance

This closes the entire displayed Gaussian2x2 block construction family as a Hadamard-Schur route, including arbitrary column mixing/permutations that the earlier aligned-block theorem alone did not cover. It does NOT classify all order10 Hadamards, all MUB triples or every McNulty-Weigert input tuple. A general H with both H and H*F10 Hadamard and the exact NONCOLLISION property remains unconstructed and unexcluded. No actual100-ray maximal1-RQLS10 or full impossibility is delivered.

The independent unrestricted sector theorem v15/v16 leaves irreducible10,4/6,5/5 branches, and the asymmetric phase master v13 keeps all rank3/4 fibers. Their scopes and every old import/finding remain separate. No I1 complex-certificate TYPE, NEB exhaustion, novelty/SOTA or finite executable certification is inferred.

Fresh entire source/dependency reconstruction is needed before parent promotion. Exact WRITTEN/source/metadata only; same original18/exclusive root/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and30min substantive actual-clock cadence. Primary research continues on the actual surviving asymmetric/unrestricted branches, not a terminal park for pending gates.
