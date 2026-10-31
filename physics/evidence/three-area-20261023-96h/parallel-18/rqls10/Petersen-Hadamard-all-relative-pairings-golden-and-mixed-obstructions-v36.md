# RQLS10 v36 — ALL relative column permutations: mixed pairs have ten untransversalizable cells; golden/golden pairs have NO quantum transversal AT ALL

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW successor: **Mon Oct 26 09:25:52 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite field/polynomial/congruence/permutation proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

## 1. The ACTUAL formerly open coordinate-pairing gap is addressed

v35 deliberately excluded only the SAME-coordinate two-central-Hadamard construction and did NOT call arbitrary relative column permutations WLOG. Here ALL such pairings are treated, without enumerating a permutation or assuming covariance after re-pairing.

Let epsilon_a(s) be the literal Petersen-duad relation exponent0,+1,-1 defined inv35, with its UNIQUE zero at s=a. Let r=(-1+i*sqrt15)/4; v35 proves r is not a root of unity and its primitive irreducible polynomial is

    m(x)=2x^2+x+2.

The four exact central Hadamards are the two CONFERENCE matrices C_+- with entries(+-i)^epsilon and the two GOLDEN matrices G_+- with entries r^(+-epsilon). Allow arbitrary independent row/column phases/permutations on each Hadamard. Row phases/permutations only rephase/relabel array cells; column phases act as a common coordinate unitary. After one common coordinate permutation, ALL nontrivial remaining freedom is ONE ARBITRARY relative permutation pi of the ten coordinates.

The original target is an ACTUAL100-ray maximal1-RQLS10, not just row/column Hadamard products. The following theorems cover EVERY pi and all sign choices:

- CONFERENCE/GOLDEN mixed pairs still give100 distinct rays, but ten matched cells lie on NO quantum transversal; no full resolution exists.
- GOLDEN/GOLDEN pairs admit NO quantum transversal whatsoever, whether their rays are all distinct or not. Thus no full resolution exists.

Only CONFERENCE/CONFERENCE pairs with nontrivial relative permutations remain OPEN within this entire monomial-pair family. Those pairs were NOT excluded inv35's same-coordinate equal/conjugate argument, and are not smuggled into the present conclusions.

## 2. Mixed categories: the ten exceptional cells simply MOVE with pi

After harmless sign choices a mixed array has literal vectors

    q_(a,b)(s)=r^(sigma*epsilon_a(pi(s)))
                 *i^(tau*epsilon_b(s))/sqrt10,
    sigma,tau in{+1,-1}.                         (MIX)

Rows/columns are ONBs for EVERY pi by the two independent exact Hadamard matrices. The100 projective rays are distinct by v35's coordinate-ratio/root-of-unity proof: a relative permutation only moves the two special coordinates pi^-1(a),pi^-1(c) at which different golden rows have opposite ODD exponent differences. They still cannot have constant exponent difference or match a fourth-root row ratio. This is the complete same proof with the actual permuted coordinates retained.

For EACH a put b=pi^-1(a). Take any other cell(c,d) with c!=a and d!=b, the required cross-row/cross-column position for a transversal through(a,b). In their inner product, the conference factors are REAL signs at every coordinate EXCEPTb,d, where they are opposite multiples of i. Thus, in the exact field decomposition

    Q(r,i)=Q(r) directsum iQ(r),

the i-component is, up to a nonzero sign,

    r^Delta_d-r^Delta_b,
    Delta_s=sigma*[epsilon_c(pi(s))-epsilon_a(pi(s))].

At s=b, pi(b)=a, so Delta_b=sigma*epsilon_c(a) is ODD(+1or-1). At s=d, pi(d)!=a. If pi(d)=c, Delta_d=-Delta_b; otherwise pi(d) differs from both a,c, and Delta_d is EVEN(0,+2,-2). Thus Delta_d!=Delta_b in EVERY allowed crosscell case. Non-root-of-unity r and i notinQ(r) force the inner product NONZERO.

Hence all ten cells(a,pi^-1(a)) have ONLY their row/column orthogonality neighbors and lie on NO quantum transversal. This closes the entire mixed-category relative-pairing freedom, not just a selected permutation or covariant resolution. Exchanging the two category orders is array transposition plus complex conjugation and a common coordinate permutation, so it is also covered.

## 3. Golden/golden: a necessary mod3 parity condition for ANY orthogonal pair

The literal two-golden array is

    q_(a,b)(s)=r^[sigma*epsilon_a(pi(s))+tau*epsilon_b(s)]/sqrt10,
    sigma,tau in{+1,-1}.                         (GG)

This includes both equal and opposite golden signs; the sign from conjugating the second Hadamard is absorbed in tau. Every row/column is an ONB, independently of whether a particular pi yields100 distinct rays.

For two distinct-row/distinct-column cells(a,b),(c,d), their inner product times10 is a sum of ten powers r^D_s, with integer exponentsD_s in[-4,4]. Multiplying by r^4 gives a polynomial P in Z[x] with nonnegative integer coefficients, P(1)=10, and P(r)=0 IF those rays are orthogonal.

The primitive irreducible m(x)=2x^2+x+2 then divides P in Z[x], by Gauss's lemma. Consequently

    P(-1) is divisible by m(-1)=3.

Since the shift4 is EVEN,

    P(-1)=10-2N_odd,

where N_odd counts the odd exponentsD_s in the ORIGINAL ten-term inner product. Their parity is independent of sigma,tau. A difference epsilon_c(pi(s))-epsilon_a(pi(s)) is odd exactly at the two coordinates{pi^-1(a),pi^-1(c)}. The other difference is odd exactly at{b,d}. Thus

    N_odd=|{pi^-1(a),pi^-1(c)} symmetric_difference {b,d}|,

which is0,2or4. The corresponding values P(-1)=10,6,2 show that divisibility by3 forces EXACTLY

    N_odd=2,
    |{pi^-1(a),pi^-1(c)} intersect {b,d}|=1.       (PAIR)

This is only a NECESSARY orthogonality condition; no false sufficiency or root cancellation is claimed. Its strength is that a full row-and-column transversal cannot satisfy it for all pairs.

## 4. NO ten-cell row-and-column transversal can satisfy PAIR

A candidate full transversal chooses one column f(a) for each row a, with f a permutation. Reindex rows by x=pi^-1(a), and put

    T(x)=f(pi(x)),

again an arbitrary permutation of the ten coordinate labels. PAIR for every two transversal rays requires, for ALL x!=y,

    |{x,y} intersect {T(x),T(y)}|=1.               (PERM)

There is NO such ten-point permutation.

If T has at leastTWO fixed points, their pair has intersection2, violating PERM. Otherwise T has0or1 fixed point, leaving a T-invariant set of at leastNINE nonfixed points. Choose any x there. At mostTWO other points are its successorT(x) and predecessorT^-1(x). There exists y among the remaining nonfixed points different from both. Neither T(x)=y nor T(y)=x, and neither point is fixed, so

    {x,y} intersect {T(x),T(y)}=empty,

violating PERM. This exhausts every permutation, with no enumeration.

Therefore NO full row-and-column quantum transversal exists in ANY golden/golden relative-pairing array. This is stronger than nonexistence of a full resolution or an A5-covariant resolution. The original full-resolution requirement fails before maximal-cardinality questions.

## 5. Entire monomial-pair scope and EXACT remaining family

The conclusions are stable under independent Hadamard row phases/permutations, arbitrary Hadamard column phases and arbitrary independent column permutations: the latter have been retained as pi throughout. Common unitary/phase/coordinate changes of the resulting array also preserve them. Thus ALL mixed and ALL golden/golden pairs from the four central matrices' independent monomial-equivalence orbits are covered.

For conference/conference, all powers lie in Q(i); the field-separation proof does not apply. Nor does the golden primitive polynomial's m(-1)=3 congruence. At SAMEcoordinate pairing v35's duplicate-ray conclusion holds, but an arbitrary relative pi may change it. This remaining fourth-root family needs a NEW exact argument or an actual full construction. It is explicitly OPEN, not silently covered by the phrase all central Hadamards.

More generally the ENTIRE TypeIV biunitary master outside monomial-Hadamard pairs remains OPEN, as do mixed TypeI,TypeII/III and all arbitrary noncovariant original intrinsic branches. No A5-WLOG, full100-ray1-RQLS witness, unrestrictedno-go, novel family, formal/kernel or configured-family/human/current-openness/novelty claim.

## 6. Full review/import/assurance contract

Review ENTIREv35 for the literal Hadamards, classification,100-ray ratio proof and quadratic-field/non-root-of-unity facts, PLUS ALLsix sections/endings here. Required new claims include genuinely arbitrary relative pi/signs/category orders, moved matched-cell parity in MIX, Gauss-lemma INTEGRAL divisibility and P(-1) congruence, exact symmetric-difference count, ALL candidate transversal permutations and full monomial-equivalence scope. A finite set of permutations, same-coordinate spotcheck or chosen resolution is not the theorem.

The polynomial/congruence/permutation proof is exact WRITTEN reasoning, NOT an executed exhaustive check. No scientific interpreter or private approximate scout was used. Independent finite-witness checker/control/vendor/priority gates remain NOT PERFORMED underHOLD. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38. Primary continues the genuinely remaining conference/conference relative family or full-master geometry, not another permutation of a now-closed golden/mixed construction; no early pending-review park.
