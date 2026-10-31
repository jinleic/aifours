# F8 AFFINE five-net — ENTIRE4+1^4 and5+1^3 strata excluded

**PhysicsMOQLS8-2. NEW WRITTEN AUTHOR CANDIDATE**, not independently/parent/formally/executably/novelty accepted. Actual returned precreation clock bound **2026-10-26T06:48:19-0700 PDT**. This is NEW scope; no older474LF/598LF freeze is expanded or credited retroactively.

## 1. Exact theorem and independent conditional-source boundary

Let N be ANY FIVE classes of the affine plane AG(2,F8), acting on its64 actual points. Q assigns arbitrary complex C8 units, ONB on EVERY actual N-line. Then neither of the following ENTIRE intrinsic component strata is possible:

- ONE irreducible dimension4 component and FOUR fixed singleton rays;
- ONE irreducible dimension5 component and THREE fixed singleton rays.

No selected choice of five slopes, real/phase ansatz, contiguous coordinates or particular fixed-ray positions is imposed. All original64 cells and actual line incidence remain. This is a theorem at the explicitly AFFINE-F8 interface. It does NOT silently identify every actual order8 five-net with this interface.

Sections2–6 prove it by a new elementary direction lemma and exact Fourier rank of ACTUAL restricted line incidence. The specialized quantum input for the4 case is the complete preceding LOCAL8 theorem; for5 it is only the ordinary general ONB span2r-1. A SEPARATE conditional route from arbitrary nets to this affine interface is documented in §7 with two explicit UNRECONSTRUCTED published finite-classification imports. Neither import is needed for §§2–6. No missing Shrikhande hypothesis is supplied by a citation.

## 2. Every eight-point five-net common transversal is an affine line — elementary proof

Let X be eight distinct points in AG(2,F8) meeting every line of each of the FIVE given classes once. A direction determined by two X-points cannot be one of those five classes. The affine plane has NINE directions, so X determines at most FOUR.

Suppose X is noncollinear. If any affine line contains t>=2 X-points, an X-point outside that line sees them in t DISTINCT directions, none equal to that line's own determined direction. Hence X determines at least t+1 directions, so t<=3. Through each X-point the seven other points lie in at most four directions, with at most two in each. Thus EXACTLY three of these directions have two other points and the fourth has one. Every X-point lies on exactly THREE trisecants and ONE bisecant.

There are8*3/3=8 trisecants. In a single direction there can be at most TWO trisecants, because they are disjoint and X has eight points. Four directions and eight trisecants therefore force EXACTLY TWO parallel trisecants in EACH direction; the two remaining points form its bisecant. In particular choose any two parallel trisecants, identify their lines as y0,y1, and their three-element x-coordinate sets as A,B. Put h=y1-y0≠0. For every a∈A, the three slopes encoded by dx/dy from(a,y0) to B are

    h^(-1)(B-a).

They are distinct and exhaust the SAME three directions other than the trisecant direction. Therefore B-a is the same three-element set for EVERY a∈A. Choosing distinct a,a' gives B+(a-a')=B. But a-a' is a nonzero translation of order TWO in characteristic2; its orbits all have size2, so no three-element set is invariant. Contradiction.

Thus X is collinear and, having eight points, is one COMPLETE affine line, in a direction outside N. This proof covers ALL point sets, not merely additive/linearized permutations. No external Rédei direction theorem, Möbius–Kantor classification or finite enumeration is an import.

## 3. Actual fixed rays make the component a union of parallel lines

A fixed singleton Q-ray occurs exactly eight times and exactly once on EVERY N-line, so its cells form a common transversal. Section2 makes each such cell set an affine line in a missing direction. Distinct fixed rays occupy disjoint cells. Two affine lines of different directions intersect, so ALL fixed-ray lines are parallel.

Choose global affine coordinates(t,s) with that missing class given by t=constant. The selected nontrivial component therefore occupies

    C=T x F8,       |T|=r,

where r4 or5. Every given N-class is transverse to the fixed-ray class, so it can be written

    b=s-mt,        m in M, |M|5.

M is an arbitrary five-element subset of F8. Its complement S=F8\M has size3. Put U=F8\T, of size8-r. This is a single GLOBAL coordinate change of the actual net/board, not independent frames at cells. Each actual N-line contains r component entries, an ONB of its actual r-space V.

## 4. Exact Fourier rank of ACTUAL line incidence and projector range

Let B be the8r-by40 incidence matrix of C against ALL given N-lines. Let H be the REAL Gram matrix of the actual V-projectors, of rank b. Actual frame sums give H1=8*1 and HB=J. Hence the(b-1)-dimensional tracezero part of Range(H) is in ker(B*), exactly as in the earlier actual-incidence proof. Thus

    b<=1+dim ker(B*).                                  (RANGE)

We compute the latter dimension symbolically, not via a matrix interpreter. For a∈F8 put

    chi_a(z)=(-1)^(Tr(az)),      Tr(z)=z+z^2+z^4 in F2.

The trace pairing is nondegenerate: Tr(1)=1, and for a≠0 choose z=a^(-1). Character orthogonality follows by pairing a sum with a translation of trace1. Thus the eight-by-eight Walsh character matrix F is unitary after the exact normalization1/sqrt(8).

Apply the invertible character transform to the actual s coordinate and the line-label b in each class. At frequency a0 the incidence block has rank1. At each nonzero a it has the rank of

    V_a=[chi_a(mt)]_(t∈T,m∈M),

a restriction of the full Walsh matrix to T rows and aM character columns. Let W_a be its complementary submatrix, with U rows and aS columns. The exact complementary-rank identity for a unitary matrix gives

    rank V_a = r+5-8+rank W_a =r-3+rank W_a.

For clarity, this identity is not assumed from determinants of square minors. A vector supported on the five retained character columns is in ker V_a iff its transform is supported on U. Those transforms form the kernel of the inverse matrix restricted to missing character columns aS and U, of dimension |U|-rank W_a. Therefore5-rank V_a=8-r-rank W_a, proving the displayed identity for these RECTANGULAR blocks.

It follows that the ACTUAL incidence nullity is

    dim ker(B*)=(r-1)+sum_(a≠0)(3-rank W_a).            (NULL)

All seven nonzero frequencies and the constant sector are retained. No arbitrary projector has replaced H's range or a Fourier support slogan replaced a rank calculation.

## 5. Four-space stratum: nullity<=6, so local span<=7, contradiction

Here |U|4. Write S={s0,s0+p,s0+q}, with p,q independent over F2. After multiplying rows by nonzero signs, the three columns of W_a are

    1, chi_(ap), chi_(aq),

restricted to U. The map

    z -> (Tr(apz),Tr(aqz))

has rank2 over F2 and fibers of size2. Its image on U has at least TWO of its four patterns. The corresponding four possible Walsh rows are(1,1,1),(1,-1,1),(1,1,-1),(1,-1,-1); ANY three are linearly independent over the reals, by subtracting the first row or their exact3-by3 determinant. Therefore rank W_a is2 iff U has exactly two image patterns, and3 otherwise.

Two full two-point fibers form an affine plane (a coset of a two-dimensional additive subspace) H0 in F8. Thus if U is NOT an affine plane, rank W_a3 for every nonzero a. If U is an affine plane with direction H, rank W_a2 exactly when the one-dimensional kernel K_a of the trace map lies in H.

Let D=span_F2(p,q), a two-dimensional subspace, and let H-perp=span_F2(u), u≠0, under the trace pairing. Since K_a=(aD)-perp, the condition K_a⊆H is equivalent to u∈aD, or

    a=u/d for some d∈D\{0}.

There are EXACTLY THREE distinct such nonzero a. Hence in ALL cases the sum in NULL is at most3; constant-sector contribution is3. Thus

    dim ker(B*)<=6,       b4<=7.

But the ENTIRE `five-net-global-ray-four-gap-and-local-four-span-eight-addendum-2.md`,181LF, SHA256 **84e0910c58caa62f431c89b6536393978d1175060e4336ed135de770b1174dc7**, proves LOCAL8, b4>=8, for EVERY actual five-net. Its complete173LF and120LF ordinary span/ray/cone predecessors remain the named chain, not a headline certified here. Contradiction excludes the ENTIRE affine4+1^4 stratum. It is not merely the affine-plane choice of U that is excluded; the nonaffine U case has even smaller incidence nullity.

## 6. Five-space stratum: exact nullity7, so local span<=8, contradiction

Now |U|3. Write U={u0,u0+p,u0+q} and S={s0,s0+h,s0+k}, each pair of differences independent over F2. Normalize the first row/column of W_a to1 by signs. The remaining signs are encoded by the binary matrix

    M_a = [[Tr(aph),Tr(apk)],
           [Tr(aqh),Tr(aqk)]].

The normalized real3-by3 determinant is4 times the difference of the two binary cross-products. Hence rank W_a3 iff M_a is invertible over F2; if M_a has rank1 then rank W_a2. Rank0 will occur only at a0, as now proved.

The FOUR field products ph,pk,qh,qk span F8 over F2. To see this, scale p,h to1 and put alpha=q/p,beta=k/h, both outside F2. If1,alpha,beta are independent they already span. Otherwise beta=alpha or1+alpha, and the products also supply alpha^2 modulo alpha. The three1,alpha,alpha^2 are independent because alpha has degree3 in F8. Thus their product span is the full three-space.

There is EXACTLY ONE nonzero binary linear relation among these four products; place its coefficients in a2-by2 matrix K. K cannot have rank1, because such a relation factors as a product of a nonzero F2-combination of p,q with a nonzero combination of h,k, which cannot be zero in a field. Hence K is invertible.

By nondegeneracy of the trace pairing, a->M_a is injective from the three-space F8 into the four-space of binary2-by2 matrices. Its image is exactly the hyperplane

    sum_ij K_ij(M_a)_ij=tr(K^T M_a)=0.

Multiplication by invertible K^T preserves rank and identifies this hyperplane with the tracezero matrices

    [[u,v],[w,u]],        u,v,w in F2.

Such a matrix has determinant u+vw. At u0 exactly v=w1 makes it invertible; at u1 exactly the THREE choices(v,w)≠(1,1) make it invertible. Thus EXACTLY FOUR of the eight matrices have rank2, while the other THREE nonzero matrices have rank1 and the zero matrix has rank0. This is a complete exact binary proof, not an executed enumeration or a parameter test.

Consequently among the seven NONZERO a, rank W_a3 exactly four times and2 exactly three times. NULL gives

    dim ker(B*)=(5-1)+3=7,       b5<=8.

The ordinary finite-ONB span theorem gives b5>=2*5-1=9 for an irreducible5 component, a contradiction. Its complete proof is reproduced in `five-net-qutrit-span-six-and-3plus5-exclusion-addendum-1.md`,120LF, SHA256 **3556699f530c89006bdcf3ec0f70dd9b24d6cb1f58c80c6dd9312bc28a1eae13**, §6: old span is a SUBSPACE of its coordinate-block algebra; every component merger costs span; no number of full mates is a premise. No stronger unproved local5 theorem is consumed. This excludes the ENTIRE affine5+1^3 stratum.

## 7. SEPARATE conditional route for arbitrary nets; explicit unreconstructed inputs

Primary source newly read, BOUNDED scope: Judith Egan and Ian M. Wanless, *Enumeration of MOLS of small order*, [arXiv:1406.3681v2](https://arxiv.org/html/1406.3681v2), original dated13Oct2014; reader1–200 and870–1100, plus targeted source search. The COMPLETE paper, original catalogue and exhaustive computations have NOT been reconstructed/replayed. The paper's actual §6 distinguishes maximal Table5 from all-sets Table6, and its introduction states blanks in tables mean zero.

The following are POSITIVE published finite-classification imports, NOT ordinary facts proved in §§2–6:

- **I_EW38 (NOT_RECONSTRUCTED here):** all38 species of maximal THREE-MOLS8 have NO common transversal, stated in the actual paragraph immediately after Tables9–13: “each of which has no common transversal.”
- **I_EWcompletion (NOT_RECONSTRUCTED here):** Table5 has order8 maximal sets only at cardinalities1,2,3,7, while Table6 has exactly ONE complete7-MOLS8 paratopy species. Thus every four-MOLS8 extends to seven, whose full9-net is equivalent to the known F8 affine family. This uses the source's exhaustive completeness claim and equivalence conventions, not just a displayed representative.

CONDITIONAL on these TWO imports, any original q1 FOUR-family whose selected Q has a fixed ray cannot have a maximal THREE-classical subfamily: the fixed ray supplies a common transversal, contrary to I_EW38. It therefore extends to FOUR classical MOLS, then by I_EWcompletion to a complete seven-set and the affine plane. Sections2–6 would then exclude ALL original r4+1^4 andr5+1^3 strata, not only their affine subcases.

That is a CONDITIONAL candidate corollary at the UNION of these imports and the fully named local-span chain. No independent finite-catalogue authentication is supplied here; the two imports remain visibly NOT_RECONSTRUCTED. In particular do NOT invoke Ball–Simoens/Shrikhande Theorem9, which needs FIVE classical MOLS, on the original THREE classical members, or infer a fourth mate merely from maximality without the published no-transversal property. This new route is a separate explicit source boundary, not a repair by missing-hypothesis suppression.

## 8. Exact remaining gap and assurance

Unconditionally at the AFFINE source interface, the two named proper-component strata are excluded as WRITTEN author candidates at their local-span inputs. At arbitrary nets their promotion needs the explicit classification union above; NOT_RECONSTRUCTED has not been removed by a URL/table read. The independently new ENTIRE qutrit spectral exclusion124LF is another candidate; if its whole chain is supported, a remaining q1 assignment has one component of dimension4–8 plus fixed axes. With the EXTRA conditional EW bridge and this packet, the proper4/5 cases disappear, leaving6/7/8. This is NOT yet an accepted global q1 theorem.

The affine6/7 cases are NOT killed by the same rank argument: its complementary blocks give only local span ceilings14 and21 respectively, consistent with general lower bounds11 and13. Fully irreducible8 has NO fixed ray and does not even enter the I_EW38 bridge. Maximal THREE-classical nets with no common transversal remain possible hosts for that full8 case. Original q2/q3/q4/unrestricted four-families, exact M(8), A10GB15/18/threeUNKNOWNs/A11/finite-object and priority gates remain OPEN/unperformed.

All proofs are exact WRITTEN, not machine-checked; NO scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO/privatefloat/decimal gloss/numeric parameter trial. Metadata date/hash/LF and readonly public source retrieval only. Standard finite-field/trace-character/unitary rank/integer-sign/ordinary Hermitian facts are exposed above; no native/GB/catalogue is a hidden premise. Generic Fourier/direction/rank methods are PRIOR mathematics and theorem priority/novelty remains UNCLEARED.

A complete ENTIRE-source mathematical AND dependency/application audit is required before any adoption; no older freeze/verdict is transferred. No formal/kernel/human/configured-family/executable/mutation/replay/novelty acceptance or numerical ledger change. Own permanent currentv112/visiblev105/v107/v109 intake read-order PROCESS MAJOR/all older histories and the HELDv3 false ALL-eight-columns/global-light/staircase withdrawal remain; no later proof cures history or establishes clean-thought/runtime/trial-free cognition census.

Exclusive new owner-root writes, immutable pinned/shared sources, no git/deletion/publication. Same18/originalprimary/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/cadence<=30min; no early final-park or96-hour closeout. Original higher-component/unrestricted-family written work continues.
