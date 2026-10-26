# RQLS10 — consolidated asymmetric nine-to-ten continuation

Owner PhysicsRQLS10-2. Actual clock observed before this consolidation: `Sun Oct 25 12:47:07 PDT 2026`.

**WRITTEN CANDIDATE only.** No scientific eval/interpreter/program, arithmetic enumeration, solver, symbolic program or replay was used. The literal field products, permutations and Fourier arguments below are WRITTEN, not machine-certified. V9/v10/v11 and HOLD remain binding. No acceptance, novelty or full-target conclusion is inferred from a source hash or an auxiliary lower-order construction.

## 1. Original target and retained boundaries

The original target remains an actual order10 array with all30 prescribed row/column/resolution ONBs and ALL100 projective rays distinct. There is no such point or curve in this manuscript. It is a consolidated new-component continuation, not a declaration that a boundary, a parameter count or a restricted no-go completes the problem.

Retain unchanged:

- `global-onb-actual-seed-normal-obstruction-v2.md`,341LF, SHA256 `e7dd4776278c8363d5a5f9366aba5b1116f689e636da48e2cf0ba11629138326`: actual cyclic7+3 seed and local nonlinear claims, the latter under their separate frozen review. No <=13/46 promotion to global nonexistence.
- `global-onb-cyclic-isotypic-core-v3.md`,209LF, SHA256 `114e935c407cedbee3afaea9d6ab64a5a05485435c481b11ed420924cee5ac38`: exact finite-amplitude7+3 representation, required isotypic type,72-ray/NINE-context boundary, general core equations and monomial-core obstruction. Its remaining21 ordinary contexts are not silently passed here.
- The old RT/all-P/236/52 gates remain unaccepted. No part of this continuation uses their computations or purports to settle their missing quantifiers.

The new component below instead starts with a different explicitly proved order10 CLASSICAL RESOLUTION and an actual28-cell partial configuration. Every already assigned pair sharing ANY prescribed context is orthogonal. It is not connected to a classical order10 seed by assumption; a classical mate for this particular resolution is not needed for a positive quantum construction and is not asserted. A future actual100-ray root would solve the existential target, while a negative for a symmetry subclass would not.

## 2. Literal finite-field auxiliary input, derived in writing

Use F9=F3[alpha]/(alpha^2+1), label t=x+y*alpha by x+3y. Put omega=exp(2*pi*i/3), Tr(x+y*alpha)=2x, and

    chi_i(t)=omega^Tr(i*t).

The nonzero squares are S={1,2,alpha,2alpha}. Define

    a0=2+alpha, b0=2-alpha,
    theta(0)=0,
    theta(t)=a0*t for t in S,
    theta(t)=b0*t for t in F9 minus (S union {0}).       (1)

The literal label lists, in input order0,...,8, are

    theta:       (0,5,7,8,3,2,4,1,6),
    theta-id:    (0,4,8,5,2,6,7,3,1),
    theta-2id:   (0,3,6,2,7,4,1,8,5).                 (2)

These were obtained by written multiplication using alpha^2=2; each list contains every label once. There is also a structural verification: the slopes of theta and theta-id are respectively 2+/-alpha and1+/-alpha, both nonsquare pairs; those of theta-2id are +/-alpha, a square pair. Equal quadratic character of the two nonzero slopes makes each piecewise map a permutation.

Define ACTUAL unit vectors in C9 by

    Q_(i,j)=(1/3) sum_(t in F9) chi_i(theta(t))*chi_j(t)|t>.
                                                               (3)

The usual character orthogonality proves every row is an ONB. Permutation of theta proves every column is an ONB. The two sets of transversals j=i+c and j=2i+c are ONBs because theta+id and theta+2id are permutations by(2), with signs interpreted in characteristic3. Their intersections have size one since the two slopes differ by1.

All81 rays in(3) are distinct, and this assertion has a direct proof rather than a selected table: a global-phase equality has phase1 from t=0, so chi_u(theta(t))*chi_v(t)=1 for every t. On S, nondegeneracy of the trace pairing gives u*a0+v=0, since S contains the F3-basis1,alpha. On the nonsquares the same argument gives u*b0+v=0; the points1+alpha and1-alpha are an F3-basis there. Since a0-b0=2alpha!=0, u=v=0. The construction is a lower-order INPUT, not an order10 witness or a claimed new existence theorem. No novelty clearance is attached to this standard character/orthomorphism framework instance.

## 3. An actual order10 resolution, independent of a classical mate

Let X=F9 disjoint-union{infinity}. Define the classical array M by

    M(r,c)=-r-c when r!=c,
    M(r,r)=infinity,
    M(r,infinity)=r,
    M(infinity,c)=c,
    M(infinity,infinity)=infinity.                    (4)

This is Latin. In regular row r the removed diagonal value of -r-c is -2r=r; the new border restores exactly r, and infinity replaces that diagonal. The column proof is identical. The infinity row/column contain all F9 values once and infinity once. Hence each symbol fiber is a genuine transversal, defining the required resolution on all100 cells. No existence of an orthogonal classical L for this particular M has been assumed.

Translation by g in F9 acts simultaneously on regular row, column and M labels by +g, fixing infinity. This uses -2g=g. The ordinary triple relation is r+c+m=0; it is symmetric in the three context roles.

Let w be a unit vector orthogonal to C9. On C10=C9 direct-sum Cw let T_r be diagonal with entries chi_r(t) on C9, and fix w. Then T_r T_s=T_(r+s), T_r^3=I. Consider the finite-amplitude family

    q_(r,c)=T_r v_(c-r),
    q_(r,infinity)=T_r a,
    q_(infinity,c)=T_c b,
    q_corner=w.                                      (5)

This F9-translation covariance is an explicit ANSATZ, not a WLOG statement about arbitrary RQLS10. All vectors and phases not fixed below remain genuinely complex; no reality, smallness, conference or common-support assumption is imposed on the core.

## 4. Exact28-cell partial configuration, with ALL its contextual overlaps checked

Set

    v_0=Q_(0,0), a=Q_(1,0), b=Q_(alpha,0).             (6)

The three are mutually orthogonal, since they are distinct entries of a column of(3). Each has every T-character projection of norm1/3. Thus its nine translates form an ONB of C9.

Assign ONLY the27 cells on the ordinary diagonal, the top-right border and bottom-left border, and the corner, using(5),(6). Then:

- infinity row: the nine T_c b plus w are an ONB;
- infinity column: the nine T_r a plus w are an ONB;
- M=infinity: the nine T_r v_0 plus w are an ONB.

Every ordinary row has just the assigned pair T_r v_0,T_r a, which is orthogonal. Every ordinary column has T_c v_0,T_c b, orthogonal. In an ordinary-M fiber m, the assigned pair is T_m a,T_m b, also orthogonal. Thus the assigned28 cells really satisfy ALL pairwise orthogonality requirements that already apply to them; this is stronger than separately listing three unrelated bases.

All28 projective rays are distinct. The27 noncorner rays are the three disjoint Q-orbits with first labels0,1,alpha and arbitrary second label, so the proof in§2 applies. The extra w is orthogonal to C9. This remains a partial configuration, NOT an order10 QLS or a100-ray construction.

The noncollinear choice of first labels0,1,alpha is deliberate. It is not the cyclic triple0,1,2 that supports the failed extra triality symmetry in§7.

## 5. Exact remaining72 cells and all three ordinary unitarities

The eight unknown core vectors are v_d, d in F9 without0, producing the72 unassigned cells through(5). All nine ordinary rows are ONBs iff

    A=[(v_d)_(d in F9), a]

is unitary. All nine ordinary columns are ONBs iff

    B=[(T_-d v_d)_(d in F9), b]

is unitary, since a column c factors out T_c. For an ordinary M-label m, write c=r+d and -r-c=m. In characteristic3 this gives r=m+d. Consequently the remaining ordinary condition is

    C=[(T_d v_d)_(d!=0), a,b]                         (7)

unitary, after factoring T_m. The eight nonzero d enumerate exactly the off-diagonal ordinary cells in that fiber. Border entries are a,b and have NOT been independently selected for each fiber.

Thus A,B,C unitary is NECESSARY AND SUFFICIENT for ALL27 ordinary contexts. Together with§4 this is the complete30-ONB problem for this explicit family. Norms, both borders, the diagonal, all ordinary resolution fibers and all eight core orbits remain present.

For each d!=0, the boundary orthogonalities require

    v_d perpendicular to
      {v0,a,T_d v0,T_d b,T_-d a,T_-d b}.               (8)

These six vectors lie in C9. Thus the allowed subspace is Cw plus their common orthogonal complement in C9, of dimension AT LEAST4 in C10. This is not a license to choose eight independent kernel vectors. The ACTUAL core conditions, for d!=e, are

    <v_d,v_e>=0,
    <v_d,T_(d-e)v_e>=0,
    <v_d,T_(e-d)v_e>=0,                              (9)

with every v_d unit. Since T_(d-e) has eigenvalues1,omega,omega^2, Fourier inversion says that the two vectors' projections are orthogonal in EACH of its three spectral slabs. The zero slab contains w as well as its three C9 coordinates. This exact blockwise form is a possible new representation of the coupled completion, not a proof of feasibility.

Full100 further requires all ELEVEN noncorner9-orbits (v0,a,b and eight v_d) to be projectively free and mutually disjoint, and to avoid w. For the core, affine spanning of its nonzero character support in F3^2 is the exact free-orbit condition. Remaining comparisons can be written |<x,T_g y>|<1 for distinct types and every g in F9; boundary/boundary separation is already proved. A row-only completion, a chosen independent phase or a jet is not substituted for(8),(9) and these inequalities.

## 6. Why the natural symmetric branch was actually replaced

A tempting alternative is b=Q_(2,0), so that, with D_f=diag(omega^f(t)) on C9 and D_f w=w,

    f(t)=Tr(theta(t)),
    a=D_f v0, b=D_f^2 v0.

For the literal theta(1), direct field algebra gives

    f(x,y)=x+y+x^2*y.                                (10)

The geometric cyclic permutation (r,c,m)->(c,m,r) of the symmetric triple relation preserves d=c-r. Its new first coordinate is r+d. Imposing covariance under the SAME quantum D_f would therefore require

    D_f v_d proportional to T_d v_d.                 (11)

This is an EXTRA symmetry assumption, not a consequence of the original constraints. The following theorem proves that this whole tempting branch cannot supply100, so the active boundary(6) does not repeat it.

## 7. Exact triality-subclass obstruction, including every eigenphase

**Theorem.** For the literal f(10), the family satisfying(11) cannot have100 distinct projective rays, regardless of the other six core vectors and all their complex phases.

**Proof.** The proportionality eigenphase is omega^s for s in F3. On C9 the support must lie in a level set

    f(x,y)-A*x-B*y=s,

where A*x+B*y=Tr(d*t) is the actual linear form associated to d. The corner w may occur only when s=0, since both operators fix it.

Look at the two NONZERO offsets with B=0 and A=1 or2. Put p=1-A, so p=0 or2. Their allowed C9 support is

    S_(p,s)={(0,s),(1,2s+p),(2,2s+2p)}.               (12)

If s=0 it is the line y=p*x through0. Even adding w adds only another copy of character0. The translated projective orbit then has at most3 rays, so a100-ray point cannot use this case.

For s!=0, w is excluded. On the three points(12), f=(1-p)x+s takes each F3 value once. Orthogonality to v0 and a imposes two independent scalar sums, leaving ONE line whose coefficients are proportional to omega^[2(1-p)x], x=0,1,2. In particular every one of those three coefficients is nonzero. No independent phase changes this support.

The supports for p=0,s and p=2,t meet in EXACTLY one point for every s,t in{1,2}. If s=t it is their x=0 point. If s!=t, their x=0 points differ and equality at nonzero x reduces to x=s-t, giving exactly one of x=1,2. Hence the two required core rays have a nonzero inner product: a single common coordinate with nonzero coefficients cannot cancel. But they belong to the same ordinary-row basis A. Contradiction.

Both possible nonzero eigenphases, the zero eigenphase, arbitrary other core data and all complex phases were included. This proves ONLY the stated D_f-triality no-go. It does not prove that every triality implementation, every translation family, every M, or unrestricted RQLS10 is impossible.

## 8. Actual replacement, provenance and exact remaining gap

The active construction uses b=Q_(alpha,0), not Q_(2,0), and imposes NO D_f-triality. Its first labels0,1,alpha are not one affine F3 line. Thus the eigenspace restriction(11) and the forced-three-point obstruction are not silently transferred to the asymmetric problem. Its remaining step is exactly the eight complex vectors satisfying(8),(9), all three unitarities, and all100-ray inequalities. Those equations are still unsolved.

Relevant public inputs were inspected at their literal scopes:

- `https://arxiv.org/html/2608.29201v2` gives the exact maximal1-RQLS target and retains10 among17 possible exceptions; the relevant complete-mapping and singular-product hypotheses do not simply yield10.
- `https://arxiv.org/html/2609.29070v1`, especially its cyclotomic orthomorphism discussion, supplies the known framework for the AUXILIARY field9 character construction; it is not an accepted order10 construction or novelty clearance.
- `https://arxiv.org/html/2603.02334v1` distinguishes product orthogonal QLS from entangled-officer/AME constructions. The latter cannot substitute for a classical-resolution solution here.

No complete reading/reconstruction of all those papers' omitted sections, appendix or computational ancestry is claimed from these scoped source reads. The local literal input(1),(2) and the arguments needed here have been written explicitly instead of citing a hash as their proof.

**First real gap:** an ACTUAL common asymmetric root for the eight-core problem(7)–(9), with all projective distinctions. The28 partial rays are genuine but are not100, the lower-order81-ray object is an input not the target, and the symmetric no-go does not eliminate the asymmetric core. The primary remains ACTIVE at this finite-amplitude gap, not parked or declared solved.

The12:34:49 checkpoint records the over30-minute explicitly named checkpoint interval additively, with no backdating. All pinned predecessors, reviews, ACKs and parent records are unchanged. No scientific execution, new GO, formal/kernel/configured-family/human/novelty acceptance, numerical promotion, publication or deadline reset occurred.
