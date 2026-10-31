# Shor raw completion — signed noncommutative factors, pure top b-layer and exact penultimate gap balance

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 05:08:58 PDT 2026** (earlier observation bound only). WRITTEN/unreviewed. Exact symbols, fractions and integer products; no scientific interpreter, calculator, eval, CAS, program, enumeration, solver, replay, CLI, nested agent or new GO.

This is a NEW representation of the ORIGINAL finite RAW UD factor-completion question, not another modulus/period filter. It retains arbitrary added word lengths, b-counts and heterogeneous a-gaps. It supplies two elementary signed-factor constraints at the last two b-layers. It does NOT settle existence or nonexistence.

The v113-A review actually RETURNED before the separate primary ACK and the newer whole-primary checkpoint34, SHA256 `3ac2c48a6c1999be3b949e34155fa277f13b5b43c31a008c90b679faea1d7def`, which was SENT to Main before this new work. Earlier publisher-preview exposure and all prior leads are disclosed there. No review result is a Shor premise.

## 1. One named published interface, NOT the positive-factorization conjecture

**Named import I5 (Reutenauer signed factorization).** De Felice's survey *Some conjectures on codes*, arXiv1611.04580v1, Theorem2.1, states the following result and attributes it to Reutenauer, *Non commutative factorization of variable-length codes*, J. Pure Appl. Algebra36(1985),167–186:

- If finite P,S in Z<a,b> give F=1+P(a+b−1)S with F nonnegative and coefficient of the empty word zero, then F is the characteristic polynomial of a finite maximal code.
- Conversely every finite maximal code has such a pair of INTEGER, possibly SIGNED, polynomial factors.

The survey theorem statement and its attribution were read at https://arxiv.org/html/1611.04580v1 . The original proof is **NOT_RECONSTRUCTED** here. All equivalence statements using this result are CONDITIONAL on I5. P,S are NOT assumed nonnegative. Requiring them nonnegative would substitute the factorization conjecture and lose the unrestricted problem; that is explicitly forbidden here.

The conditional representation below is distinct from the earlier direct finite-code/SP/Kraft protocol, which did not use I5. Neither accepts the other from a hash.

## 2. Exact unrestricted signed-factor feasibility system

Let C be the literal16-word Shor code. The ORIGINAL question is equivalent, conditional on I5, to the existence of a positive integer n and FINITE P,S in Z<a,b> such that:

1. `P(0,b)=S(0,b)=1`;
2. `P(a,0) S(a,0)=1+a+...+a^(n−1)`;
3. `F:=1+P(a+b−1)S` has NONNEGATIVE coefficients at EVERY word;
4. `(F,c)>=1` for EVERY literal c in C.

No degree, b-count, number of monomials, coefficient magnitudes, a-gaps, n or delay bound is imposed. The infinitely indexed nonnegativity condition is a finite coefficient condition for EACH actually given finite pair P,S; it is not an executed test or a uniform decision bound.

### Necessity

For a finite raw complete UD M, there is exactly ONE pure-a word a^n. If there were none, finite maximum word length L would bound every a-run in M* by2L, contradicting factor-completeness. Two different pure-a codewords violate UD by taking their appropriate positive powers. Since b belongs to C, no b^k with k>=2 can be another codeword, so the pure-b characteristic part is exactly b.

Finite UD gives its Bernoulli sum f<=1: for fixed positive letter probabilities summing to1, UD and a length bound L give f^k<=kL+1 by summing the probabilities of distinct words in M^k by length. Exponential growth would contradict this if f>1. Completeness forces f=1: every factor of M* is a bounded suffix, followed by M*, followed by a bounded prefix, up to finitely many short exceptions. If f<1 that finite cover would have finite total Bernoulli mass, whereas all words have infinite total mass (one at each length). Consequently M is maximal: any larger UD set would have Bernoulli sum>1.

I5 now gives signed P,S. Substitute a=0 in F=b. In Z[b], `(b−1)P(0,b)S(0,b)=b−1`, so the two evaluated factors are units with the same sign. Flip BOTH P,S if necessary to obtain condition1. Substituting b=0 and using F=a^n gives condition2. Conditions3–4 are the actual characteristic/inclusion conditions.

### Sufficiency

Condition1 makes the empty coefficient of F zero. I5 makes F a finite code characteristic polynomial, in particular0/1-valued, and condition4 puts C inside it. The signed identity evaluated at formal Bernoulli weights a=t,b=1−t gives total code mass1 for EVERY0<t<1.

For completeness directly, if some nonempty word u of length ell never occurred as a factor of M*, every word in M* would avoid u. Disjoint length-ell blocks show that total probability of length-k words avoiding u is at most `(1−mu(u))^floor(k/ell)`, whose sum over k is finite. But UD and code mass1 give total mass of M* equal to `sum_(j>=0)1= infinity`. Contradiction. Thus M is RAW factor-complete. No residue quotient, finite-state stabilization or PR cancellation is used in this direction.

## 3. Two elementary raw consequences: pure-b normalization and the first layer

Write `P=sum P_i`, `S=sum S_j`, where P_i,S_j contain exactly i,j occurrences of b. All are FINITE signed polynomials. Condition1 implies no positive pure-b monomial occurs in either factor, even with a negative coefficient. Their constant coefficients equal1.

Put P_0=U(a),S_0=V(a). Then UV=1+...+a^(n−1). Ordinary factorization in Z[a] gives U,V as complementary products of the monic cyclotomic factors Phi_d, d|n,d>1, normalized to constant1. Their coefficients may be negative; they are NOT indicator factors A,B and are not silently identified with FACT tilings.

Represent one-b polynomials by commuting bookkeeping variables x,y for the a-runs BEFORE and AFTER that one b. Then the exact ACTUAL one-b characteristic polynomial is

    F_1(x,y)=U(x)V(y)
              +(y−1)P_1(x,y)V(y)
              +(x−1)U(x)S_1(x,y).                       (ONE)

This follows by collecting exactly one occurrence of b in the signed identity. These are RAW exponents, not residues. It retains actual high exponents and signs in P_1,S_1. At x=y=1 it gives F_1(1,1)=U(1)V(1)=n. The Shor monomials must occur, but no single one-b profile is assumed complete.

In particular, every root xi of U and root eta of V gives F_1(xi,eta)=0. This is a necessary complex algebraic vanishing, not a sampled Fourier test or a proof of sign feasibility. ONE alone is not sufficient: all higher b-layers in condition3 remain mandatory.

## 4. NEW exact top-layer purity lemma (independent of I5)

Let P,S be ANY nonzero finite integer polynomials with F=1+P(a+b−1)S a0/1 polynomial. Let p=deg_b P and q=deg_b S. Then D=deg_b F=p+q+1, and

    F_D=P_p b S_q.                                       (TOP)

The lower-b term P(a−1)S cannot cancel this layer. More importantly, there is NO hidden convolution in TOP: a word with D b's splits UNIQUELY at its (p+1)-st b as x b y, with |x|_b=p,|y|_b=q. Hence its coefficient is exactly `(P_p,x)(S_q,y)`.

Choose any nonzero coefficient in each factor. Their product must equal1. Thus each is either1 or−1 with the SAME sign epsilon. Keeping one factor coefficient fixed proves EVERY nonzero coefficient in P_p and S_q is that same epsilon. Consequently:

- P_p and S_q are epsilon times characteristic polynomials of finite raw languages;
- the top b-layer of M is the injective Cartesian product `supp(P_p) b supp(S_q)`;
- its cardinality is exactly the PRODUCT of the two support sizes.

This includes p=0 or q=0. It does not prove all lower layers positive. Flipping only the top layers is not an allowed operation on the original factorization. No b-layer cutoff or finite-witness instance was used.

## 5. NEW exact penultimate gap-balance identity

Set P_(−1)=S_(−1)=0. Collecting b-degree D−1 gives

    F_(D−1)=P_p(a−1)S_q
             +P_(p−1)bS_q+P_p bS_(q−1).                 (PEN)

Here the first term DOES have a central a-run convolution, unlike TOP. Fix the a-run exponents r_0,...,r_(p+q) of a word with p+q b's, and vary only the central run r_p=k. Let

- T_e be the coefficient of the corresponding p-b prefix ending in a^e in P_p;
- U_f be the coefficient of the corresponding q-b suffix starting in a^f in S_q;
- `h_k=sum_(e+f=k)T_e U_f`, with h_(−1)=0.

By §4, all nonzero T_e and U_f have the SAME epsilon, so h_k is a FINITE nonnegative integer sequence. Let L_k and R_k be the coefficients of the two b-insertion terms in PEN for this fixed context. Each is a SINGLE coefficient product: the inserted b is respectively the p-th or (p+1)-st b. If its index is unavailable, that term is0.

Then the exact coefficient condition is

    m_k=h_(k−1)−h_k+L_k+R_k in {0,1}  for EVERY k>=0.     (BAL)

All sequences have finite support. Summing over k telescopes the entire top-layer difference and yields

    sum_k m_k=sum_k(L_k+R_k).                            (SUM)

If h is nonzero, let k0 be its FIRST nonzero index. Then BAL at k0 forces

    L_(k0)+R_(k0) >= h_(k0) >0.                          (REPAIR)

Thus a nonzero top context MUST receive a same-sign adjacent lower-layer repair at its first central gap. It cannot be made nonnegative by the top P_p(a−1)S_q term alone. This is a raw, coefficient-exact repair requirement for every top context, not a bounded-potential hypothesis about the cyclic one-b automaton.

Neither L nor R is assumed separately nonnegative: their signs and lower-b factorizations are the actual remaining freedom. SUM and REPAIR do not turn them into a code or make a finite signed factorization exist. At the last nonzero h the same equations also retain the positive outgoing difference; no boundary term at infinite gap is discarded.

## 6. What changed, and the exact next unproved step

The previous actual-Y construction explained why a canonical cyclic first-return completion can be infinite and why positive rational potentials/exponential tails do not settle alternate finite history splitting. This packet moves to a DIFFERENT representation: finite signed polynomial factors and EVERY raw coefficient. Conditional on I5, solving conditions1–4 would directly give a finite RAW completion; excluding them for ALL n and ALL finite signed P,S would give non-completion. No separate raw PR/STAB realization theorem would be needed after that exact feasibility problem is solved.

New proved elementary constraints are TOP and BAL/REPAIR, including raw a-gap boundaries. They preserve arbitrary b-counts and unknown signed lower layers. The first genuinely unproved Shor-specific step is: show that the sixteen prescribed coefficients in ONE force an impossible finite cascade of the REPAIR conditions, OR construct finite signed factors whose entire coefficient polynomial is nonnegative. No such cascade theorem or signed factors are supplied. Positivity of P,S, bounded repair depth, or an unexplained termination assertion is NOT a premise.

I5 remains a NAMED UNRECONSTRUCTED external theorem, not a conjecture proved here. Its statement is published and read, but this packet does not call it kernel/formal/human acceptance. The source check for I4 did not obtain its original proof: the publisher book preview supplies front matter/introduction/references, not Theorem5.5; the legitimate open-access Szabo2006 article endpoints returned metadata or access errors. I3/I4 retain their previous scopes.

Own permanent v109-A reviewer exactness MAJOR and all older findings remain. SummaryLF58's two-28-coset claim is separately qualified by additive erratum2; it is not a premise here. H* is FALSE/WITHDRAWN. No factorization conjecture, commutative-prefix conjecture, finite-depth miss, new scientific GO, frozen/source/shared edit, git, deletion or publication. Original cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 unchanged; research continues, not a final park.
