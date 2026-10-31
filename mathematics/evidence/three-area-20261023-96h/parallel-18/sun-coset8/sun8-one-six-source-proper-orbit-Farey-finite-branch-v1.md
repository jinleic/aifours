# Sun P7 — ONE six-source bounds its entire simple-group branch, with no two-orbit hypothesis on the other source

Owner **MathSun8-2**. Actual preceding `/bin/date`: **Mon Oct 26 08:28:22 PDT 2026**. **NEW STANDALONE WRITTEN CANDIDATE, not reviewed/adopted.** Every new finite-group, actual-fibre, representation, variance and packing step is proved below. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/GO or huge-power evaluation.

## 0. Three complete exact statements

**A. Generic proper-orbit dimension bound.** Let G be finite, M ACTUAL of index7t. Let R,H be ACTUAL subgroups of indices7r,7u with gcd(r,u)=1 and gcd(t,ru)=1, and suppose ACTUAL nonempty LEFT cosets of R,H are disjoint. Suppose R has EXACTLY TWO orbits6t+t on Omega=G/M. Let H have ANY actual nonempty proper invariant set T of size ell*t, ell an integer1..6; no two-orbit, multiplicity, density or quotient ansatz is imposed on H. Then the unique nontrivial irreducible W shared by C[Omega] and C[G/R] has

    d=dim W<=216 if ell1 or6,
    d<=720 if ell2,3,4 or5.

In particular d<=720 with EVERY other-source representation structure, including the genuine two-component5+1+1 case left outside the stronger single-isotypic source theorems.

**B. ANY actual normalizer alpha6 branch.** In ANY direct P7 family of EIGHT disjoint original LEFT cosets with FULL indices7r_l/private r_l pairwise coprime, select U_i and N=N_G(U_i). If ONE original neighbour has normalizer coefficient alpha6, there is another actual proper-orbit neighbour satisfying A; indeed at least FOUR of the other six neighbours do. Thus its actual nontrivial W has d<=720. This requires no private7-free vertex, minimum-SUM, minimum group order, restriction on a starting nonabelian Q=N/U_i, or absence of a second alpha6.

**C. Explicit finite simple-group/ALL-index bound.** If that G is finite NONABELIAN SIMPLE, W is faithful and

    |G| < 109^1036800,
    7r_l < 109^1036800 for EVERY original l,
    7s < 109^1036800 where[G:N]=7s.

This covers the ENTIRE alpha6-PRESENT normalizer branch in finite simple direct-P7 groups, not merely the mixed5+2/private2/3/5 branch. It is not a bound on an alpha6-ABSENT example, a nonsimple/infinite G, or all general Sun8 configurations. No finite search or emptiness certificate is supplied.

These statements need ONLY ordinary finite-group index/coset facts, finite unitary decomposition/Schur, elementary positive matrices, exact finite rational-grid inequalities and Euclidean volume scaling. No F7/NC7, Sun3/Sun4/R4, Jordan/CFSG, group/subgroup catalogue, old source verdict or opaque research lemma is a correctness premise of THIS standalone proof. The separate least-GROUP-ORDER simple reduction is needed only if one uses C inside that earlier existence route; it is not re-authenticated here.

## 1. ALL conjugate intersections, not just one original position

Original disjointness implies RH!=G. Private coprimality and index divisibility give

    [G:R cap H]=7ru*delta, 1<=delta<=6.

The upper bound comes from the product formula; delta7 would mean RH=G and force every left-coset pair to meet.

For EVERY g the SAME upper bound holds:

    [G:R cap gHg^(-1)]=7ru*delta_g, 1<=delta_g<=6.     (1)

If one such product were all G, R's orbit through gH on G/H would have FULL size7u and cover that entire coset set. R would be transitive, hence its orbit through H also full, contradicting RH!=G. This supplies the ALL-conjugate step rather than silently transplanting one intersection factor.

Every orbit of R cap gHg^(-1) on Omega has length a multiple of t/gcd(t,delta_g): a length a gives7t|7ru*delta_g*a, and gcd(t,ru)=1.

Let T_R be R's UNIQUE small orbit of size t. For ANY a,b in G, aT_R cap bT is invariant under aRa^(-1) cap bHb^(-1). Therefore

    z_(a,b)=|aT_R cap bT|/t
      belongs to F6={k/g:0<=k<=g,1<=g<=6}.            (GRID)

Every entry lies in[0,1] since T_R has size t. This is an ACTUAL finite union of stabilizer orbits, not a formal fraction chosen as a model. The conclusion applies to ALL original incidence columns.

## 2. One multiplicity-one module and an arbitrary positive other covariance

Define actual G-equivariant0/1 incidence matrices I_R,I_H on the SAME rows Omega and columns G/R,G/H by membership in translated T_R,T. Their column weights are t,ell*t; their row weights are r,ell*u by transitivity/counting.

Equivariant maps C[G/R]->X=C[Omega] have dimension equal to R's orbit count TWO. Finite unitary irreducible decomposition leaves constants once and precisely ONE common nontrivial W, multiplicity ONE in BOTH modules. The incidence columns are nonconstant, so their image is constants plus W. Schur/constant eigenvalue/trace give

    I_R I_R^*=(r/7)J+(6tr/d)E_W.                    (2)

The constant eigenvalue is tr and total trace7tr, so the nontrivial trace is6tr. This is a complete elementary representation argument, not a classification of R or G.

For I_H impose NO analogous image/rank/multiplicity assertion. Its Gram has constant eigenvalue ell²*t*u and total trace7ell*t*u. Thus its nonconstant positive part has trace ell(7-ell)*t*u. Because W occurs only once in the FULL X, the G-equivariant positive I_H I_H^* acts on W by a scalar lambda>=0, and

    d*lambda<=ell(7-ell)*t*u.                        (3)

All its OTHER irreducibles/isotypic multiplicities remain. No claim that I_H's image equals constants plus W is made.

## 3. Full cross moments and the exact universal variance ceiling

Normalize Z=I_R^* I_H/t and average over ALL(7r)(7u) entries. Counting row products gives

    mean Z=ell/7=:mu.

Using (2), positivity, and (3),

    ||I_R^*I_H||_F²
      =tr[(I_R I_R^*)(I_H I_H^*)]
      =ell²*t²*r*u+6tr*lambda
      <=[ell²+6ell(7-ell)/d]*t²*r*u.

Consequently

    Var(Z)<=6ell(7-ell)/(49d).                       (VAR-UP)

These are exact finite matrix identities and an inequality on the arbitrary other covariance, not a SAME-covariance assumption. In particular they cover BOTH nonzero projections in a three-orbit source. If lambda were0, GRID's positive variance below would contradict the zero nonconstant variance; sharing W is a consequence, not an assumed omitted bridge.

## 4. ALL six rational-grid cases, with a full gap proof

Every entry Z lies in GRID, while its mean ell/7 is NOT in F6. The required adjacent-grid gaps are

    ell1: mean1/7 between0 and1/6;
    ell2: mean2/7 between1/4 and1/3;
    ell3: mean3/7 between2/5 and1/2.

There is no allowed fraction strictly inside any indicated interval. Here is a uniform elementary proof: if a/b<c/d have bc-ad=1 and k/g is strictly between them, then bk-ag>=1 and cg-dk>=1; multiplying the former by d and the latter by b and adding gives g>=b+d. Each displayed endpoint pair has determinant1 and denominator sum7. Thus no denominator<=6 lies between them. Endpoint0 is0/1.

For entries z outside(a,b), (z-a)(z-b)>=0. At a fixed mean mu this yields

    Var(Z)>= (mu-a)(b-mu).

The three EXACT lower bounds are1/294,1/588,1/490. Combining with VAR-UP gives, respectively,

    d<= [36/49]*294=216,
    d<= [60/49]*588=720,
    d<= [72/49]*490=720.

For ell4,5,6 apply z->1-z. F6 and variance are unchanged and the means become3/7,2/7,1/7. This exhausts EVERY ell1..6. These are universal finite rational inequalities on ALL original cross entries, not numeric parameter/control trials, a likelihood probe, decimal magnitude annotation or executed enumeration. This proves A.

## 5. Actual normalizer identities and seven-retention for the original eight sources

Now take the direct P7 family and translate ALL eight cosets together so selected U=U_i contains identity. For every original neighbour l, put V_l=U cap U_l. Index arithmetic gives

    [G:V_l]=7r_i r_l beta_l, [U:V_l]=r_l beta_l,
    1<=beta_l<=6.                                    (4)

The exclusion of beta7 is again UU_l=G, incompatible with the original disjoint cosets.

For completeness N=N_G(U) retains7 in its index without any minimum hypothesis. If d0=[G:N] lacked7, it would divide r_i and be coprime to EVERY7r_l. Thus every given neighbour meets N and[N:N cap U_l]=7r_l. Since U normal N, projection into Q=N/U gives quotient index c_l with c_l beta_l=7, hence beta1,c7. Projected neighbour cosets avoid identity. Any overlap in the SAME U-fibre would give two original subgroup cosets of private-coprime indices r_l,r_k, impossible. Seven such disjoint index7 cosets would exhaust finite Q yet avoid identity, contradiction.

Therefore

    [G:N]=7s, q=|Q|, r_i=sq.

With W_l=N cap U_l, H_l=U W_l/U and c_l=[Q:H_l], the ORIGINAL full identities are

    [N:W_l]=r_l alpha_l,
    alpha_l=beta_l c_l<=7,
    [U_l:W_l]=s alpha_l.                             (5)

Coprimality of s and r_l gives the integer alpha. The actual neighbour hits s alpha_l LEFT N-cells. In EVERY common cell its intersection is a left coset of the SAME fixed W_l; its Q support is a coset of the SAME H_l, and in each common U-fibre its pieces have indices r_l beta_l. N need NOT be normal G and G/N is ONLY a coset SET. No independent affine cell arrangements or source changes are used.

## 6. At most TWO transitive neighbours leave an actual proper-orbit source

Assume one original R has alpha_R6. Then beta_R*c_R=6, so both beta_R,c_R divide6. Its actual action on G/N has6s orbit through N and the remaining s orbit: precisely the two-orbit source required in A.

Any OTHER alpha7 neighbour H has beta_H1,c_H7, since beta7 was excluded. It hits ALL7s N-cells. Its quotient index7 and R's index c_R in{1,2,3,6} are coprime, so their Q cosets meet in EVERY shared N-cell. Such shared cells exist because R hits6s.

The actual U-fibre indices there are r_H and beta_R*r_R. If gcd(r_H,beta_R)=1, they are coprime and force an original coset intersection. Therefore EVERY alpha7 neighbour must own a prime2 or3 dividing beta_R. Private pairwise coprimality allows at most ONE owner per prime, hence at most TWO alpha7 sources among the SIX other neighbours.

At least FOUR of those six therefore have alpha in1..6. Choose any one. Its ACTUAL orbit through N has size alpha*s, a nonempty proper invariant set, regardless of its OTHER orbits or irreducible types. The relevant private factors and s are coprime by s|r_i. Apply A with t=s and ell=alpha to obtain d<=720.

This proves B with ALL seven neighbours retained, including hidden ones and the possible selected private7-owner. It needs no initial-character rank, min-SUM, no-second-six theorem, Sun3/Sun4/R4, F7 or group catalogue. The capacity argument is about ACTUAL fixed quotient intersections/fibres, not an index list alone.

## 7. Complete elementary simple-group packing and the explicit branch bound

Suppose G is finite NONABELIAN SIMPLE. Nontrivial W has normal kernel not G, hence is FAITHFUL. Average an inner product to put it in U(d). Let delta be the minimum nonidentity operator distance from I. If delta<1/2, every pair u,v of conjugates of a minimizer has

    ||[u,v]-I||_op=||uv-vu||_op
      <=2||u-I||_op||v-I||_op=2delta²<delta.

Minimality makes ALL those commutators identity; their conjugates generate a nontrivial ABELIAN normal subgroup, contradicting nonabelian simplicity. Thus delta>=1/2. Distinct group matrices are Frobenius-separated by at least1/2. Their open balls of radius1/4 in real dimension2d² are disjoint and lie in the ball of radius sqrt(d)+1/4, because unitary centers have Frobenius norm sqrt(d). Volume scaling gives

    |G| <= (4sqrt(d)+1)^(2d²).

This proof is elementary and FULLY supplied; no Jordan or finite-linear-group classification is a named extra input.

Since d<=720<27² and2*720²=1036800,

    |G| < 109^1036800=:B.

EVERY original index7r_l and the ACTUAL normalizer index7s are at most|G|, so they are all STRICTLY below B. No huge power is evaluated, no finite object/group/coset enumeration is executed or authorized, and no branch-emptiness certificate is supplied. This proves C. For nonsimple G, faithfulness or the abelian-normal contradiction need not hold, so no bound on its entire order is inferred.

## 8. Direct infinite transfer and exact original residual

The representation/dimension statement transfers to ANY original group carrying the direct P7 family: first divide by the common finite-index normal core of all eight U_l. It lies in every U_l and N. All cosets are full preimages, all indices/intersections/disjointness are preserved, and normalizers are preserved EXACTLY because a conjugate of U/core equals U/core iff its full preimage is U. Thus N/core is the actual normalizer of U/core, with the SAME q,s and alpha. Apply the finite proof there. This does NOT bound an infinite G or authenticate the separate reduction from a general Sun8 configuration to direct P7.

At the named least-GROUP-ORDER finite direct-P7 reduction, G is nonabelian simple, so the ENTIRE alpha6-PRESENT branch is now proposed finite with the explicit bound above. The alpha6-ABSENT branch at EVERY vertex remains UNBOUNDED by this theorem. No argument forces an alpha6 source to exist or shows that every group below the bound is impossible. Thus original arbitrary-group Sun8 remains NOT_PROVED.

The prior sharper20/160 mixed-source bounds, actual Q1/2/4 normalizer structure and S5 single-isotypic extensions retain THEIR extra hypotheses and stronger conclusions. The present theorem includes genuine three-orbit/two-component other sources for the dimension/size bound only; it does NOT give them the old private2/3/5 owner pattern, q<=4 or canonical seven-block quotient. Actual small-Q fibre transport, other alpha values, private-composite/odd/maximal/self-normalizing legal enlargement, remaining group families/extensions/infinite ancestry and all original private powers/s/outert/hidden-neighbour gaps remain. No globalSun7/R8/t-bound for ALL cases, witness, novelty/SOTA/priority or stronger acceptance follows.

All mathematics is exact WRITTEN after actual v123 RETURN and the separate WHOLE primary ACK WRITTEN+SENT before prospective source/proof. OWN057/047/078/COUNT/M1/v26/v31 TWO late/v33 and every received finding remain permanent; ENTIRE withdrawn trial/guidance has ZERO credit and is not repeated/replayed/back-converted. No new numeric parameter/control trial, decimal magnitude scout, scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO, dead-kernel restart, author/shared/frozen edit, git, deletion or publication. Same18/exclusiveOWN/HOLD/original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/substantive<=30min checkpoints; no formal/human/family/kernel/executable/triple/priority/novelty gate, new owner/deadline, cognition/runtime census, early final park or round closeout. Original research continues.
