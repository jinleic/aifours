# AFFINE q1 r7 — EQUIVALENT operator-valued Fano flags; exact rigidity gap

**PhysicsMOQLS8-2. NEW WRITTEN AUTHOR CANDIDATE REFORMULATION, NOT an exclusion.** Actual precreation clock bound **2026-10-26T07:31:22-0700 PDT**. No independent/parent/formal/executable/novelty acceptance. New exact representation of the surviving problem, not another support count or an old theorem with omitted hypotheses.

## 1. Original stratum and complete scope boundary

N is ANY FIVE classes of AG(2,F8). Q assigns arbitrary complex C8 units, ONB on every given line, and has ONE intrinsic irreducible dimension7 component V plus ONE fixed singleton ray. The fixed ray's eight cells are a common transversal, hence an affine line by the COMPLETE elementary direction proof in148LF `affine-five-net-four-and-five-component-exclusions-v1.md`, SHA256 **a4f5b232d7c0cf824f88a4292024de08486f4f8a3656ca1b015c315def4747dd**.

That direction lemma is the ONLY specialized predecessor needed for this representation. Its Egan–Wanless finite-classification bridge is NOT consumed. No covariance/real-vector/phase/rank ansatz and no assumed quantum-graph automorphism is added. We prove a TWO-WAY equivalence retaining every rank-one/ONB condition. The linear flag constraints alone are not declared a quantum Latin square.

## 2. Canonical affine five-net, retaining the fixed line

Choose the fixed-ray direction as t=constant and place its line at t0. Then V occupies(t,b)∈F8* x F8, with the five given classes initially s-mt=constant, m∈M5. The three missing slopes S3 lie in one affine additive plane gamma+D, where gamma=sum S is its fourth point and D is a two-dimensional F2 subspace. Thus M-gamma is0 plus the OTHER coset of D.

Every such D is the kernel of a unique nonzero trace functional Tr(cz), Tr(z)=z+z^2+z^4, by nondegeneracy. Subtract gamma from slopes and rescale the GLOBAL t coordinate to multiply the new slopes by c. The fixed line stays t0, and we may write

    given M={0} union{m∈F8:Tr(m)=1},
    missing S={d∈F8*:Tr(d)=0}.

This is a global affine coordinate normalization of the original given net, not an assumption that its missing t-lines are ONBs. Set D=kerTr. The given slope0 lines are b=constant. For EACH b the seven V-entries give an ACTUAL ONB; denote their projectors by P_t(b), t∈F8*. Put P_0(b)=0 on V.

For all m∈M and all b the exact physical identities are

    sum_t P_t(b+mt)=I_V,
    every P_t(b) a unit rank-one Hermitian projector.   (ORIGINAL)

The eighth fixed-ray projector outside V is understood on t0. For unit rank-one projectors, a sum of seven equal to I7 is equivalent to the seven vectors being an ONB, so no original line orthogonality is weakened by writing the operator sums.

## 3. ALL nonzero frequencies become the three Fano lines through one point

For a∈F8 define

    A_a(t)=(1/8)sum_b chi_a(b)P_t(b),
    chi_a(b)=(-1)^Tr(ab).

For a0 write S_t=A_0(t); S_0=0. Transforming the actual line sums in b shows that for a≠0, A_a(t) as a function of t has Fourier support only in

    a(D\{0}).

Indeed every m∈M imposes the zero coefficient at frequency am, and those are exactly the five omitted frequencies. Nondegenerate trace-character orthogonality is an exact finite identity, not an executed transform.

The annihilator of aD is the one-dimensional additive subspace{0,1/a}, because D=kerTr. Therefore for EVERY a≠0, putting p=1/a,

    A_a(t+p)=A_a(t),      A_a(p)=A_a(0)=0.

The missing t-frequency0 also gives sum_t A_a(t)=0. The six remaining nonzero t-values are THREE disjoint pairs{t,t+p}; the three corresponding operator values SUM0, since each is counted twice.

View the seven nonzero F8 elements as the points of the Fano plane over F2; its lines are{p,t,p+t}. For each point p, its three incident lines L give operator flags B_(p,L). The complete constraints are

    A_(1/p)(p)=0,
    A_(1/p)(t)=B_(p,L) for t∈L\{p},
    sum_(L containing p) B_(p,L)=0.                  (FLAGS)

Each B is Hermitian and trace0. The THREE pair values are NOT separately assumed positive or rank-one. All SEVEN frequencies/twenty-one flags are retained; the point p and the inverse frequency1/p must not be transposed or replaced by t without proof.

## 4. Exact converse — FLAGS plus physical row constraints give ALL five classes

Conversely choose Hermitian S_t with trace1, sum_t S_t=I7, and flags satisfying FLAGS. Define the actual candidate projectors by

    P_t(b)=S_t+sum_(a≠0)chi_a(b)A_a(t),    t≠0,
    P_0(b)=0.

REQUIRE, for EVERY b, that these seven P_t(b) are unit rank-one Hermitian projectors forming an ONB of V. This is an essential nonlinear condition, not a result of flag counting.

Then ORIGINAL holds for the given slope0. For any other given m, Tr(m)=1. At a≠0, with p=1/a, paired t,t+p terms in the Fourier transform of sum_t P_t(b+mt) have opposite character signs:

    chi_a(m(t+p))=chi_a(mt)*(-1)^Tr(m)=-chi_a(mt).

Their A_a values are EQUAL by FLAGS, while the special t=p term is0. Thus every nonzero b-frequency cancels. The constant frequency is sum_t S_t=I7. Therefore sum_t P_t(b+mt)=I7 for ALL four other m and EVERY b. Since the seven terms are actual unit rank-one projectors, every such line is an ONB. Adding the fixed eighth axis at t0 gives the original arbitrary-complex line-ONB assignment on the affine FIVE-net.

To obtain exactly the nonclassical r7 stratum one must ALSO require that the nonorthogonality graph of all these actual rays is connected on V. If it splits, the result belongs to a smaller-component/classical stratum instead. Nothing is silently promoted by solving only the linear flag equations.

This proves the TWO-WAY physical equivalence: original affine r7 data yield FLAGS and row rank-one ONBs, and ANY such full flag/row solution yields original affine r7 data, with intrinsic connectedness imposed. The representation does not construct a solution or prove it impossible.

## 5. Exact remaining algebraic question and rank bookkeeping

There are seven S_t, whose sum is I7, and at each of seven p there are three flags with one sum relation. Thus before the nonlinear constraints the projector operators lie in the span of I plus SIX independent means plus FOURTEEN flag directions, at most TWENTY-ONE real operator dimensions. This agrees with the actual incidence ceiling, but no equality or finite-rank realization is asserted.

The remaining task is EXACTLY: prove every physical solution of FLAGS and the eight row7-ONB conditions is globally commuting/reducible, OR construct a noncommuting solution with a connected intrinsic7 ray graph. A numerical/eigenvalue relaxation, arbitrary Fano flag count or matrices failing rank-one positivity is not this problem. Global fixed-ray/multiplicity bounds may be added only through their full named proofs; they are not needed for the equivalence itself.

In particular the means S_t are density operators, but they are NOT proved to be projections or to form a magic-unitary column. The Fourier flags are traceless Hermitian operators, not quantum-permutation generators. A proof that treats those objects as projections has skipped the surviving mathematical gap.

## 6. Positive public rigidity theorem; exact missing applicability bridge

A new bounded source read was made of Simon Schmidt, [*On the quantum symmetry of distance-transitive graphs*, arXiv:1906.06537v1](https://arxiv.org/html/1906.06537v1): reader1–200 and286–312 plus targeted source search, NOT the complete §5 commutativity proof or all transitive imports. The source states Theorem1.5: a cubic distance-transitive graph of order>=10 has no quantum symmetry, and Table1 lists the Heawood graph of order14. Its Definition2.16 requires a SQUARE matrix of projections with BOTH row and column sums identity, plus the graph-adjacency intertwining relations u*epsilon=epsilon*u.

This theorem is a POSITIVE prior result, but it is NOT currently a correctness input. Our seven-by-eight array of rank-one row bases/Fano Fourier flags does NOT YET give a14-by14 Heawood quantum automorphism, or a seven-by-seven Fano incidence magic unitary with the required adjacency relation. Neither the missing column sums nor a suitable representation/map have been derived. The original QLS does give an eight-by-eight projector magic unitary in its original two net-class coordinates, but that fact alone is NOT the required Heawood adjacency representation.

Thus published Fano/Heawood rigidity cannot be invoked to exclude this r7 stratum without a NEW exact applicability proof. Its missing interface is explicitly retained, not hidden under “Fano” terminology. The public theorem's full proof was not reconstructed here; no headline/pin establishes it. The static reader shows a2019v1 header and an additional displayed August24,2026 date; no new publication/priority inference is drawn from that rendering.

## 7. Assurance and original residual

This is a new exact WRITTEN equivalence/barrier, not formal proof, an accepted no-go, executable construction, numerical M(8), A10/A11 or novelty clearance. Affine r7 and irreducible8/no-fixed remain OPEN. The separately written affine4/5/6 exclusions and q2 C3/half-multiplicity results require their own ENTIRE audits; no earlier verdict is transferred to FLAGS. General nonaffine proper-component extension still needs explicit I_EW38/I_EWcompletion NOT_RECONSTRUCTED imports from148LF; full8 is outside the fixed-ray bridge. q3/q4/unrestricted families and A10GB15/18/threeUNKNOWNs/A11/finite-object/family/priority gates remain unchanged.

All Fourier/rank/count/flag identities are exact WRITTEN, not machine-checked. NO scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO/privatefloat/decimal gloss/numeric parameter trial. Metadata date/hash/LF and readonly public sources only. Generic finite Fourier/Fano/operator methods and the stated quantum-graph theorem are PRIOR; specialist theorem priority remains UNCLEARED.

Own currentv112/visiblev105/v107/v109 intake read-order PROCESS MAJOR and older histories remain. HELDv3 false ALL-eight-columns/global-light/staircase-only and rejected connected-commutant<=4 shortcut remain WITHDRAWN/unused. No later correct proof cures history or certifies clean-thought/runtime/trial-free cognition census. Exclusive owner-root new writes, frozen/shared sources unchanged, no git/deletion/publication. Same18/originalprimary/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/cadence<=30min; no early final-park or96-hour closeout. Original remaining written mathematics continues.
