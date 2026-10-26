# Cyclic separator characters: a uniform arc selector and an exact type-only boundary

Actual returned clock before creation: **Sun Oct 25 11:20:06 PDT 2026**. Owner MathOlson-2-2, math-2. **ONE consolidated AUTHOR-WRITTEN CANDIDATE successor; fresh reconstruction and parent disposition NOT PERFORMED.** Written field/graph/word reasoning only. No scientific interpreter/eval, arithmetic program, symbolic computation, enumeration, replay or solver. No value of the earlier positive p7 word is computed.

## 0. Current primary and source boundary

This continues the SAME frozen102319 original-primary assignment after the actual203-LF v79-A temporary review was returned. Own primary was safely frozen before that interruption; parent explicitly requested continuation on the full residual rather than parking at the delivery of a candidate.

The preceding230-LF `consolidated-FULL-CYCLE-STATUS-AND-PARITY-SELECTORS-v1.md`, SHA256 `06239c35cf6fd33f9063291fbbcdf9bd26fb16b069ff6f8cc7ef901409bed626`, is an AUTHOR-WRITTEN candidate awaiting its fresh gate, not silently accepted. This successor re-derives its needed full-cycle/character core below rather than importing an unreturned verdict. Its additional result is a genuinely new CYCLIC ARC selector and the complete boundary of the formal-zero-character method, not another calculation of an isolated pair value.

The new finding/cadence record is `primary-102319-cyclic-separator-checkpoint-v1.json`, SHA256 `e9753ed8b21b6511b878c479211dbf4796089682a9906e194def04d13cbd33d8`, observed11:16:57. The original primary ACK at10:26:38, named actual indicator/GRAD/HESS/run interfaces and v9/v10/v11/HOLD remain operative. The later source/clock corrections are additive, not backdated. No prior pinned file is changed.

## 1. ENTIRE word class and notation

For EVERY prime p>=7, use the actual group

    D_(2p)={(v,e):v in F_p,e in {+1,-1}},
    (v,e)(v',e')=(v+e*v',ee'),
    rho_x=(x,+1), sigma_y=(y,-1).

Retain all original words of EXACT counts

    R=p+2, F=3p-3, N=4p-1,

with nonzero rotations and actual cyclic reflection gaps of size0 or1, EVERY retained literal old caller/GRX/certificate/deletion failure, simultaneous actual GRAD/HESS, actual gamma/x sum and NONNULL continuants of EVERY maximal ACTUAL reflection RUN. No field-alphabet, root, covariance or shortened-word assumption is added.

Write

    h=(p-1)/2, F=6h, R=2h+3.

Let I be the occupied gap indices on the actual F-colour cycle. At occupied j let x_j!=0 be the actual rotation, and put x_j=0 only as a coefficient convention at an EMPTY gap. With actual reflection values y_j, cyclically put

    beta_j=y_(j-1)-y_j, gamma_j=beta_j-x_j,
    sum beta_j=0, sum gamma_j=-sum x_j.                   (ACTUAL)

Define the FORMAL monomer-dimer polynomial on the full colour cycle C_F by

    P_C(a;t)=sum_(matchings M) t^|M| product_(uncovered j)a_j,
    Phi(a)=coeff_(t^(2h))P_C(a;t).

It is multiaffine of degree2h=p-1 and bihomogeneous of degree h in each parity class of cycle vertices. This auxiliary cycle is NOT the old possible-switch graph or a physical one-endpoint packet family.

The original goal remains exactly2p actual positions in increasing ORIGINAL order for every word of the full class. The uniform sufficient selectors below apply to ambient actual words even without the old failures. The entire remaining actual complement, with every failure retained, is stated in §8.

## 2. Full-cycle character core, with normalization re-derived

At an actual initial rotation gap r, fix colour u_r=0 and select reflection j iff adjacent colours differ. For formal statuses z of all actual rotations, the supported original-order formulas are

    V=C+sum_j alpha_j u_j,
    alpha_j=beta_j-2x_j z_j, C=sum x_j z_j,
    Z=k+S(u), k=sum_(j in I)z_j,
    S(u)=sum_j(u_j+u_(j+1)-2u_j*u_(j+1)).

Let H^(r)(z) be the signed sum of(1-V^(p-1))(1-Z^(p-1)) over the F-1 free colours.

Extend these formulas algebraically to ALL F Boolean colours. Actual sum beta=0 gives sum alpha=-2C; hence complementing every colour sends V to -V and fixes Z. The Fermat indicator is unchanged because p-1 is even. Its sign weight is unchanged because F=6h is even. Complementation pairs the u_r=0 and u_r=1 halves, so the full signed sum is2H^(r).

Set c_j=1-2u_j. The coordinate constant cancels EXACTLY:

    V=-(1/2)sum alpha_j c_j,
    Z=(1/2)[F+2k-sum c_j c_(j+1)].

The full signed sum has weight product c_j. Its c-degree is at most3(p-1)=F. A monomial can survive only when every exponent is odd; at total degree<=F this means the ONE full squarefree monomial. Only the highest coordinate/size product contributes. Its p-1 monomers and p-1 dimers have factor((p-1)!)^2=1 by Wilson pairing; half and minus factors disappear to even(p-1) powers. Thus its coefficient is exactly Phi(beta-2xz). Since2^F=1 in F_p,

    H^(r)(z)=(1/2)Phi(beta-2xz).                         (CYCLE)

This is an ordinary polynomial identity and uses the ACTUAL cyclic sum, not a free Hessian assignment. The full-F degree boundary is legitimate; the invalid reduced(F-1)-degree shortcut is not used. Mixed terms remain.

With epsilon=1-2z at the R occupied gaps,

    H=(1/2)Phi(gamma+x epsilon)
      =(1/2)sum_(S subset I)J_S epsilon_S,
    J_S=x_S partial_S Phi(gamma), x_S=product_(i in S)x_i.  (1)

No Boolean reduction or missing factorial is hidden: Phi is multiaffine and each occupied gap is distinct.

Under hypothetical absence of identity2p, H on EVEN rotation selections is the point mass at the empty selection. No odd-subset indicator is assumed zero. Sign-character orthogonality gives

    1=2^(R-1)*(J_S+J_(I minus S))/2,
    J_S+J_(I minus S)=1/2 for EVERY S subset I.           (AJ)

Here2^(R-1)=2^(p+1)=4. Any failure of(AJ) is a genuine identity2p existence criterion on the ORIGINAL word. The low orders give VALUE, GRAD and HESS; satisfying the whole signed-indicator pattern is still not sufficient for avoidance, because identity contributions can cancel modulo p.

## 3. EXACT formal-zero criterion for ANY character derivative

For a nonempty S subset I, list its vertices in cyclic order. Let kappa(S) be HALF the number of changes of parity along this cyclic list. Thus kappa=0 if S is monochromatic, and if both parities occur it is the number of cyclic blocks of either colour. All quantities in this section are ordinary INTEGERS, not ordered field residues.

Deleting S splits C_F into paths. Between consecutive deleted indices with cyclic gap distance d, the remaining path has d-1 vertices. That path is odd exactly when the two deleted indices have the SAME parity. The number of odd path components is therefore

    |S|-2kappa(S).

The matching number of the remaining path forest is consequently

    nu(C_F minus S)
      =[F-|S|-(|S|-2kappa(S))]/2
      =3h-|S|+kappa(S).                                 (MATCH)

On the other hand

    partial_S Phi=coeff_(t^(2h))P_(C_F minus S).

**Lemma FZ.** This derivative is IDENTICALLY zero as a polynomial in the remaining formal gamma variables IF AND ONLY IF

    |S|-kappa(S)>h.                                     (FZ)

**Proof.** If the matching number is<2h, no matching term of the required size exists. Conversely a matching of size2h exists whenever the matching number is>=2h: take that many edges from a maximum matching. Its unmatched vertices determine a monomial. On the remaining forest, deleting those monomer vertices leaves disjoint even paths, each with a UNIQUE perfect matching forced from an endpoint. Hence that monomial has coefficient EXACTLY1, not a multiplicity that might cancel modulo p. Thus the derivative is not the zero polynomial. Combine with(MATCH). QED.

The same reasoning shows Phi itself is nonzero; its2h monomers break the original cycle into paths. Hence a subset and its complement can BOTH have formally zero derivatives only when both are nonempty. Formal nonzero does NOT mean nonzero at a particular actual gamma; this distinction is retained below.

## 4. A new CYCLIC ARC selector in the surviving parity range

The earlier direct bidegree selector cases are:

- BOTH occupied parity counts>=h+1; or
- ONE occupied parity count>=2h+2=p+1.

In the first case choose S as all occupied vertices of one parity; in the second choose h+1 vertices from the overlarge parity. Both its derivative and its complement's derivative vanish. Equation(AJ) would require0=1/2, so the original word has identity2p. Their complement has minority count a and majority count b with

    2<=a<=h, b=2h+3-a.                                  (COUNTS)

Let A be the actual minority occupied vertices and B the majority occupied vertices. There are a open cyclic arcs between consecutive A vertices. Count only ACTUAL occupied B vertices on each arc; empty gap vertices are not silently identified with rotations. Put

    ell=h+2-a>=2.

**Theorem ARC (new uniform actual-word selector).** If ANY one of these arcs contains at least ell majority occupied gaps, the original word has an exact2p identity in original order, for EVERY actual choice of reflection and nonzero rotation values.

**Proof.** Choose ell of those actual B vertices as U and put S=A union U. In its cyclic subsequence, all A vertices form one block and all selected U vertices one block: selected B vertices occur in only that ONE A-to-A arc. Thus kappa(S)=1 and

    |S|-kappa(S)=a+ell-1=h+1>h.

By FZ, partial_S Phi is identically zero. The complement consists ONLY of the b-ell=h+1 remaining B vertices, so it is monochromatic with size h+1 and its derivative is identically zero too. Actual x products do not change zero. Equation(AJ) contradicts0=1/2. This proves an actual identity2p exists. QED.

No raw possible-switch matching, invented same-gap anchor or shorter-word witness is used. The character subset is not itself asserted to be the selected2p word; it witnesses failure of the ORIGINAL indicator's necessary equation.

## 5. COMPLETE boundary of this particular value-independent mechanism

The following is not an avoiding-word classification. It classifies EXACTLY when a type pattern admits a character S for which BOTH formal derivative polynomials in(AJ) vanish.

If both derivatives vanish, FZ gives

    |S|-kappa(S)>=h+1,
    R-|S|-kappa(I minus S)>=h+1.

Since R=2h+3, this forces

    kappa(S)+kappa(I minus S)<=1.                        (2)

If both kappas are0, both subsets are monochromatic. Outside the already listed concentrated/monochromatic case, they are exactly the two full occupied parity classes, and their required sizes give the balanced case.

Otherwise one subset is mixed with kappa1 and its complement monochromatic. In(COUNTS) the monochromatic complement cannot be minority, since its size would be<=a<=h and FZ would fail. Thus the mixed subset contains ALL A and u selected B vertices. The two FZ conditions become

    a+u-1>=h+1,
    b-u>=h+1.

They force the SINGLE integer value u=h+2-a=ell. Kappa1 then says those u selected B vertices all lie in ONE arc between consecutive A vertices. Such a subset exists exactly when the corresponding actual arc has at least ell B vertices.

Therefore the balanced case, concentrated case and ARC case are the COMPLETE classification of the two-FORMAL-zero-character method. If none occurs, that method cannot force0+0 by structural matching deficiency alone. Actual gamma evaluation may still violate(AJ), and no broader no-go for polynomial or word selectors is proved.

This completeness proof uses no endpoint/graph enumeration program and does not assume that arbitrary nonzero derivative values, Hessians or old caller failures are realized.

## 6. Uniform pigeonhole consequences and a calibrated whole-band corollary

The a arcs distribute all b=2h+3-a majority occupied vertices. If every arc had at most ell-1=h+1-a, then

    b<=a(h+1-a).

The exact difference is

    b-a(h+1-a)=3-(a-2)(h-a).                             (3)

Consequently ARC is FORCED for EVERY actual cyclic order in(COUNTS) whenever

    (a-2)(h-a)<=2.                                      (PH)

This is a growing all-prime sufficient condition, not a checked finite range or a chosen word example. In particular the entire minority-count a=2 and a=h classes are solved, with arbitrary actual values and old data.

Any hypothetical all-prime remainder must therefore satisfy

    (a-2)(h-a)>=3,
    EVERY A-to-A arc has <=h+1-a occupied B vertices.      (ARC-RES)

If the product is EXACTLY3, equality holds in the capacity sum, so EVERY such arc saturates that upper bound. This is a necessary incidence pattern, not rotation-value covariance or a realized residual word.

### Candidate whole R=p+2 band at p=7 and p=11

If h<=5, then for every2<=a<=h, writing u=a-2>=0,v=h-a>=0 gives u+v=h-2<=3. Thus4uv<=(u+v)^2<=9, and the INTEGER product uv<=2. Condition(PH) always applies.

For primes p>=7 with h=(p-1)/2<=5, namely p=7 and11, EVERY ambient zero-free singleton-gap word at the stated counts is therefore covered by balanced, concentrated or ARC selectors. The separately supported TA/identity-relocation caller covers the other actual words of that count, which have an identity rotation or a gap containing at least two rotations.

Hence this is an AUTHOR-WRITTEN candidate proof of the ENTIRE fixed-count band R=p+2,F=3p-3,N=4p-1 for p=7 AND p=11, with ALL values and type patterns, at the named TA/original indicator interface. It is not an interpreter test of the previous p7 word. It is not unrestricted ordered Olson for D14 or D22: the other R bands remain unclosed.

The universal ARC theorem and condition(PH) are the primary unbounded results. These two prime instances are consequences, not a substitution of finite cases for the original all-prime target.

## 7. Full coupled residue still retained, not replaced by type counts

Let Rcur_p be the ENTIRE current actual class: every original old caller/GRX/certificate failure; exact counts/positions; zero-free singleton gaps; actual beta=dy,gamma=beta-x and cyclic sum; supported GRAD/HESS; nonnull ACTUAL run continuants; and the full necessary character system(AJ). For its exact minority-polynomial interface, the core above also re-derives the preceding candidate's factorization rather than assuming a passed gate:

For T subset A, its complement contains all b>h majority vertices, so its derivative vanishes by bihomogeneity. Thus J_T=1/2 and

    Phi(gamma+sum_(i in A)x_i epsilon_i e_i)
           =(1/2)product_(i in A)(1+epsilon_i).

The same applies after any U subset B with |U|<=ell, since the complement still has at least h+1 majority vertices. Hence the mixed minority jets J_(T union U)=1/2 all remain. These are actual Phi section identities; half-status sections are not words or witnesses.

Every actual word already failing(AJ) is solved by the indicator criterion. Among actual all-(AJ) words, the new theorem forces(COUNTS) and(ARC-RES). Thus the ENTIRE exact unbounded remainder retains every actual field/value/run/old-failure condition AND these incidence restrictions. Its possible emptiness or nonemptiness is not asserted.

For p>=13, this work does NOT prove that actual evaluations of the nonzero formal derivatives must contradict(AJ), nor that minority factorization forces an actual run-null condition. It does not exhibit a word satisfying all the retained conditions. Ambient gamma/x integration from the sum is not full-residual realization: every old failure and the actual derivative values still require proof.

**First unproved step:** use the SAME realized gamma/x data, cyclic sum, full complement jets/minority factorization, the restricted majority counts on every minority arc, all nonnull ACTUAL run continuants and EVERY original caller/certificate failure to force a genuine value-dependent coefficient violation or another actual2p selector on the remaining p>=13 class. The formal matching-deficiency classification is complete, but it is only one sufficient mechanism, not a proof that no further selector exists.

## 8. Original order, exact size and assurance

All selectors contradict absence of an actual identity2p using the original even-rotation indicator. If a nonempty even-K indicator point has coordinate0 and size0 mod p, its actual positive even size is below4p and therefore EXACTLY2p. If the empty-K signed sum differs from its empty contribution, a nonempty reflection selection supplies that same exact2p size. No character subset, monomer pattern or polynomial half-point is itself substituted for a selected word.

For original w=AB and a cut BA, the SAME selected named portions satisfy P_B P_A=1; hence P_A P_B=P_B^(-1)(P_B P_A)P_B=1 in original increasing order. No nonidentity occurrence is moved, and no shortened-word witness or reflection-subsequence block count is used.

Fresh hostile reconstruction should check the full-cycle1/2 and(AJ) normalization; the exact ordinary matching-number formula; absence of finite-field coefficient cancellation in a path forest; completeness of kappa(S)+kappa(complement)<=1 cases; the one-arc subset and exact ell size; integer pigeonhole equality/inequalities; the calibrated p7/p11 whole-band union with TA; and preservation of the ENTIRE all-prime residual and original cardinality/order.

No strict difference outside every historical provider or novelty is certified. The all-prime R=p+2 band, other count bands, prime-dihedral and all-finite-group ordered Olson remain open beyond the explicit candidate corollary. No formal/kernel/human/configured-family/executable acceptance, actual residual witness or scientific GO is supplied. All v9/v10/v11/HOLD, original cutoff/deadline and frozen-source histories are unchanged.
