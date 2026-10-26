# Shor completion — exact common-complement gate and uniform trade obstructions

Owner MathShor / MathShor-2. Last actual `/bin/date` before composing: `Sun Oct 25 15:10:59 PDT 2026` (an earlier-observation bound, not an invented creation instant).

**WRITTEN CANDIDATE, unreviewed.** This is ONE consolidated partial primary packet from the SAME102319 continuation. It does not solve the original problem. It consolidates the new common-mate representation and all-order uniform restrictions so they can be reviewed in one body. Consolidation itself is not new science. No frozen predecessor is edited.

## 0. Original target, exact result and trust

The code is LITERALLY

    C = b{1,a,a^7,a^13,a^14}
        union {a^3,a^8}b{1,a^2,a^4,a^6}
        union a^11 b{1,a,a^2}.

The target is a FINITE raw M containing C, concatenation-injective on EVERY finite codeword list, with EVERY binary word a factor of some M-product. There is no upper bound on word lengths, b-counts, delays, pure-a order or bridge arity.

**Uniform partial theorem.** Every hypothetical full completion supplies ONE unknown cyclic tile A with THREE unknown complements B,D2,D3 containing respectively

    I={0,3,8,11} subset A,
    J0={0,1,7,13,14} subset B,
    J2={0,2,4,6} subset D2,
    J3={0,1,2} subset D3.

Existence of these common complements is EXACTLY equivalent to the relevant one-b all-t border EXISTENCE gate, at the same n,A,B (§2). For EVERY such common-mate witness, at ANY order,

    |D2 minus B|=|B minus D2| >= 7,
    |D3 minus B|=|B minus D3| >= 3,
    |D3 minus D2|=|D2 minus D3| >= 3.

If the first trade has exactly7 points on each side, then Phi_n divides the integer mask A(z). This primitive-spectrum zero is NOT a period and is not excluded. The first two mates can be chosen to have CONNECTED actual trade graphs containing the mandatory configurations in §8; all unknown vertices/chords/wraps remain.

**What is NOT supplied:** no A,B,D2,D3 witness, no finite PR-saturated raw extension, no uniform obstruction for all larger trades, no raw STAB termination theorem. Full Shor target: **NOT_PROVED in either direction**.

**Inputs.** The actual long-run border extraction, the nonnegative group-ring multiplier lemma, and the finite-code Bernoulli identity are earlier WRITTEN interfaces. Their short derivations are recalled in §1; they are not new order improvements. Classical facts used without reproving the general theory are finite Fourier inversion, cyclotomic degree/irreducibility over coprime cyclotomic fields, elementary finite-group/field algebra and unit-circle geometry. No Szabo/Redei classification, Cordero realization converse or H* is a premise. H* as formalized remains WITHDRAWN by the exact countercontrol. No old computation is credited.

## 1. Existing necessary interfaces, with scope retained

### 1.1 Long raw runs give the border tilings

A finite complete UD M containing b has a unique pure-a word a^n: a sufficiently long pure a-run in an M-product must contain a whole codeword, while two different pure-a powers would commute and violate UD.

Let A be the residue set of END a-lengths in words a^s b^d (plus0 through b), B the START a-lengths in b^e a^r (plus0), and Y the residue pairs of actual one-b words a^i b a^j. For arbitrary t>=0, padding

    b^D a^E0 b a^E1 b ... b a^Et b^D

with D and all E_i greater than the maximum codeword length forces each internal b into one actual one-b codeword. Every other internal word is a^n; the outer mixed words give B/A endpoints. Completeness gives surjectivity of

    B x Y^t x A -> Z_n^(t+1),
    (r,(i1,j1),...,(it,jt),s)
       -> (r+i1,j1+i2,...,jt+s).                  (BT)

Two different residue tuples can be padded to the SAME long b/a runs using b and a^n codewords; they give different actual lists, so UD gives injectivity. It also gives raw-to-residue injectivity. Thus A+B is direct, |A||B|=|Y|=n, and the literal seeds are distinct. In particular n>=20 and all displayed exponents0..14 are canonical representatives. This is the existing written raw-to-border proof, not a converse.

### 1.2 Multiplier fact (including nonunit pushforwards)

If finite nonnegative counting functions U,V on a finite abelian group satisfy U*V=1, then the pushforward T_d U under x->dx still tiles with V whenever gcd(d,|U|)=1. For a prime p not dividing |U|, work in the commutative F_p group ring. Frobenius gives T_p U=U^{*p}, while

    (T_p U)*V=U^{*(p-1)}*1=|U|^(p-1)*1=1 modp.

The integer coefficients are nonnegative and1 modulo p, hence at least1. Their total is the group size, so all are exactly1. Iterate over prime factors of d. Multiplicities are kept; injectivity of multiplication was not assumed.

The inherited literal collisions force330||B| and2||A|:

- multipliers8,3,5,11 on B use8+0=0+8, 3+0=0+3, 8+0=3+5, 11+0=0+11;
- multiplier2 on A uses2*3+1=2*0+7.

Thus660|n and n>=1320 (the latter is an inequality from |A|>=4, |B|>=330). The stronger inherited full-code1320 divisibility and conditional19800 threshold are not newly derived or needed below.

### 1.3 A period gives a genuine quotient tiling

If A+H=A for a subgroup H, projection is injective on ANY complement B: b-b' in H would give a+b=(a+b-b')+b'. Counting and covering then give Abar+Bbar=Z_n/H directly. For the periods60,660 used below, the quotient seeds remain distinct because those moduli exceed14; the multiplier argument would force |Bbar|>=330 and |Abar|>=4, impossible at either modulus.

For an arbitrary smaller quotient one must bootstrap distinctness rather than assume it. The separate periodic-descent proof does that without dropping660Z minus1320Z orders. No raw word/delay/STAB quotient is implied.

## 2. Exact three-complement equivalence, at the SAME n,A,B

Fix a direct A+B=Z_n with I subset A and J0 subset B. The following are equivalent:

1. There is Y containing ALL16 C pairs such that BxYxA -> Z_n^2 is bijective.
2. The SAME A has complements D2,D3 containing J2,J3.
3. There is SOME Ytilde containing ALL16 C pairs with BT bijective for EVERY t>=0, at the same n,A,B.

**1=>2.** For k in Z_n define a counting function

    D_k(j)=#{(r,(i,j)) in BxY : r+i=k}.

The t1 bijection says D_k*1_A=1. Since0 in A, D_k(j)<=1, so it is a SET, not an unaccounted multiset. Its size is n/|A|=|B|, and D_k+A is direct. With r=0, the C row at i=k contributes all its right exponents. Hence J2 subset D_3 and J3 subset D_11. These give the two mates, with no independence assumption.

**2=>3.** For every i in A choose

    D_0=B, D_3=D_8=D2, D_11=D3,
    D_i=B at all other i,
    Ytilde=union_(i in A) ({i}xD_i).

It has n points and includes all C pairs. Given an arbitrary output(x0,...,xt), B+A uniquely determines r,i1; D_(i1)+A uniquely determines j1,i2; continue, and D_(it)+A uniquely determines jt,s. This is a complete successive decoder at EVERY length t. For t0 use B+A. Finally3=>1 is t1.

This is an EXISTENCE normal form. It does NOT replace the original actual Y inside a raw M while preserving its other words.

### What a gate witness would deliver, and what it would not

A positive common-mate witness would explicitly construct the FINITE RAW UD set

    M0={a^n} union {a^i b a^j : (i,j) in Ytilde, 0<=i,j<n}.

UD follows from BT: equal products have the same b-count and give equal residue outputs with outer markers0, so their Ytilde sequences agree; the numbers of a^n words between them are then fixed by actual run lengths.

But M0 could NOT be complete. The finite complete-UD Bernoulli identity would force

    1=x^n+(1-x) sum_Ytilde x^(i+j),
    sum_Ytilde x^(i+j)=1+x+...+x^(n-1).

The right side has15 terms in degrees0..14 while C contributes16 such terms on the left, with nonnegative coefficients. Contradiction. The Bernoulli identity is the earlier elementary Kraft/divergent-mass argument, not a new conjectural positivity statement.

Nor is M0 automatically PR-saturated: a cyclic factorization can wrap, requiring the isolated-word lift H in LR+(1-z^n)H=S_n. This construction has not realized H, actual delays or higher bridge words. No residue-to-raw completeness converse is asserted.

## 3. Exact forced trade signs

In any complement of A, two values differing by3,5,8 or11 are forbidden, because those are differences inside I. Literal collisions give:

    B excludes2,4,6:
       3+7=8+2; 3+1=0+4; 8+6=0+14.
    D2 excludes1,7,13,14:
       0+4=3+1; 3+7=8+2;
       0+13=11+2; 0+14=8+6.
    D3 excludes4,6,7,13:
       0+4=3+1; 3+6=8+1;
       3+7=8+2; 0+13=11+2.

Therefore B minus D2 contains1,7,13,14, while D2 minus B contains2,4,6. The other two trades have B minus D3 containing7,13, D3 minus B containing2; and D2 minus D3 containing4,6, D3 minus D2 containing1. Equal cardinalities imply all trade sides balance.

## 4. The two small trades: each must have at least3 points

### Unit-circle lemma

Two pairs of complex unit numbers with the same sum either agree as unordered pairs or have common sum0. For a nonzero midpoint the chord of the unit circle is unique; the zero-sum case is antipodal. Hence

    zeta^p+zeta^u=zeta^r+zeta^s

implies zeta^(p-r)=1, or zeta^(p-s)=1, or zeta^(s-r)=-1.

### B versus D3

Trade size<=2 would be exactly

    D3 minus B={2,u}, B minus D3={7,13}.

At any nth root where A(zeta)!=0, the annihilator A*(D3-B)=0 gives zeta^2+zeta^u=zeta^7+zeta^13. The unit-circle lemma forces the order to divide5,11 or12, hence660. Thus Fourier inversion makes A periodic by660. Section1.3 gives an impossible quotient tiling at660. Therefore this trade is>=3.

### D2 versus D3

Trade size<=2 would be

    D3 minus D2={1,u}, D2 minus D3={4,6}.

Now the orders divide3,5 or4, hence60. A is periodic by60, again impossible by §1.3. Thus this trade is>=3. These arguments cover EVERY unknown u and EVERY n, not a sampled range.

## 5. The main uniform restriction: B/D2 trade size>=7

Let k=|D2 minus B|=|B minus D2|. Already k>=4. Set

    E=1_D2-1_B,
    Q=z+z^7+z^13+z^14-z^2-z^4-z^6.

If k<=6, then at any root of E the relation Q plus AT MOST2k-7<=5 further signed powers vanishes. These unknown exponents and signs are arbitrary; no new term is discarded.

### 5.1 Any11-bearing root of E has order EXACTLY11

The seven fixed Q terms grouped modulo11 occupy:

    class1: zeta,
    class2: zeta^13-zeta^2,
    class3: zeta^14,
    class4: -zeta^4,
    class6: -zeta^6,
    class7: zeta^7.

There are five singleton classes, one paired class2 and five empty classes0,5,8,9,10.

If11^2 divides the root order d, the extension degree over Q(zeta^11) is11, so every grouped coefficient is0. Five singletons require at least five unknown terms. If that many exist, all are consumed there; the unchanged paired class then forces zeta^11=1, impossible.

If11 divides d once, write d=11m and zeta=alpha*beta, with alpha order11 and beta order m coprime to11. The only relation among the eleven alpha powers over Q(beta) is the all-ones relation, so all grouped coefficients must be equal.

- If a class remains empty, their common value is0. Again the five unknown terms are consumed by the five singletons, leaving beta^13-beta^2=0. Thus beta^11=1 and beta=1, so d=11.
- If no class remains empty, all five unknown terms occupy one each of the five initially empty classes. None alters the known classes. Comparing the three positive singleton coefficients beta,beta^7,beta^14 gives beta^6=beta^13=1, hence beta=1. But the paired class coefficient is then0 while a singleton coefficient is1. Impossible.

This proves the claim for ALL unknown locations/signs. The cyclotomic extension/irreducibility fact is the explicit classical algebra input, not an unread model-specific theorem.

### 5.2 Binary spectral rigidity contradicts tiling

Write n=11^e m, gcd(11,m)=1. Since11||B|, e>=1. A*E=0 means A's nonzero Fourier modes can have either prime-to11 order (dividing m) or EXACT order11. Hence A is periodic modulo11m, and on Z_m x Z_11 its binary indicator has the form

    1_A(u,v)=f(u)+g(v).

This follows from the Fourier expansion: there are no mixed modes. A real sum f(u)+g(v) taking only0/1 on the whole Cartesian product has one component constant. If f(u)-f(u') is nonzero, it is a fixed difference+1 or-1 of two binary values for every v, forcing g constant; otherwise f is constant.

- If g is constant, A depends only modulo m, so11^e||A|. Together with11||B| this contradicts n=|A||B| and v_11(n)=e.
- If f is constant, A depends only modulo11. With s occupied residues, |A|=(n/11)s and |B|=11/s<=11, contradicting330||B|.

Thus k<=6 is impossible. This proves k>=7 uniformly at EVERY order with ALL additional signed terms included.

## 6. First surviving size7: primitive spectrum must vanish

Assume k=7. Then E=S-Q, where S has four unknown positive and three unknown negative terms, and all fourteen support locations are distinct modulo n. We prove Phi_n|A.

Suppose E vanished at a primitive nth root zeta. Recall11|n and n>=1320. If11^2|n, all mod11 class coefficients vanish. If11 divides n once and a class is empty, they also all vanish. In either case:

1. The five singletons consume at least five unknown terms.
2. The paired class2 cannot have zero unknowns (zeta^11=1), or only one (|zeta^11-1|=1 would force zeta^11 of order6 and n=66).
3. Therefore exactly five unknowns pair with the singletons and two with class2. The four signed unit terms in class2 sum0 and split into opposite pairs. The two known terms do not cancel each other, so each pairs with an unknown.
4. All seven known terms therefore pair with unknowns. Opposite-sign cancellation at primitive order would require identical exponents modulo n, forbidden by the distinct support. Same-sign cancellation requires an antipodal shift. In Q-S, four known positive terms would require four unknown positive terms, but there are only three. Contradiction.

The remaining case has11 exactly dividing n and no class empty. Five unknowns fill the initially empty classes, leaving at most two to alter the five singleton classes. At least three known singleton coefficients are untouched. Writing zeta=alpha*beta as before, equality of these coefficients forces beta^(2(a-b))=beta^(2(a-c))=1 for three distinct a,b,c in{1,4,6,7,14}. The gcd of such pair differences is1,2 or3 (only{1,4,7} gives3 and{4,6,14} gives2). Thus the order m of beta divides2,4 or6, so n<=66, impossible.

Hence E is nonzero at every primitive nth root. Since A*E=0, A vanishes there: Phi_n divides A(z).

**Do not infer a period:** the remaining Fourier orders can be incomparable and have least common multiple n. This k7/Phi_n-divisible case is genuinely unexcluded; all k>=8 cases are also live.

## 7. Exact method controls, not correctness premises of the core theorem

The separate frozen method notes prove further restrictions, but NONE is needed for §§0–6/8:

- Q has no root of unity, so the exact translated-mask7-trade E=(z^h-1)Q would force A+h=A and the literal collision (3+h)+1=0+(h+4). It cannot be an actual tiling trade.
- A general positive-filter density bound excludes E=U*(z^u-Q) with U>=0 and U(1)<=16. That proof uses an additional explicit local root lemma. It is not a theorem that arbitrary trades have such a factorization.

All these optional source notes remain unreviewed and separate; they cannot silently shrink the residual to their favorable architectures. Formal masks with seven or more unknown terms DO admit arbitrarily large conductors before actual tiling/positivity is enforced.

## 8. Connected actual trade normal form, with unknown chords retained

For ANY two complements B,D of A let P=D minus B, N=B minus D. Cancellation of common tiles gives equal unions of disjoint translates A+P=A+N. Each residue in the common region defines one edge between its unique P and N labels; parallel edges are different residues. This is a finite |A|-regular bipartite graph. Each component has equal P/N vertex counts. Swapping a component's P set back to its N set preserves a genuine direct complement.

For B/D2 the fixed points form the mandatory connected path

    N13 -- P2 -- N7 -- P4 -- N1 -- P6 -- N14.

Its actual edge residues are13,10,7/15,4/12,9,14/17 respectively. All come from A0, and the literal collisions in §3 put each vertex on the required trade side.

Choose D2 to minimize |D2 minus B| among all mates containing J2. Any component outside that path can be undone without losing0,2,4,6, contradicting minimality. Thus the WHOLE minimal D2 trade is connected, with at least seven vertices per side. Similarly a minimal D3 trade is connected around N7--P2--N13 and has at least three per side. These choices can be made independently relative to B, with the SAME A.

Unknown additions cannot be deleted from this representation. The entire A-A avoids the nonzero differences +/-{1,2,4,6,7,12,13,14}, the union of the three mate-seed difference sets. Among the seven fixed B/D2 vertices the only additional possible adjacency types are P4--N13 (difference9) and P4--N14 (difference10). Those unknown-endpoint chords are NOT ruled out. Extra multiplicities, arbitrary other vertices and cyclic wraps also remain.

No simultaneous minimality/connectedness of the third D2/D3 graph is assumed. A joint exchange theorem would require its own proof.

## 9. Exact remaining gap, not a solved or narrowed substitute

The full original question remains NOT_PROVED. The unexcluded common-gate cases include

- nonuniform connected seven-point trades with Phi_n|A;
- all larger trades with arbitrary additional positive/negative terms;
- all possible unknown endpoint tiles/mates, unbounded orders and cyclic lifting behavior.

A uniform contradiction for ALL these cases would exclude every finite completion. No such contradiction is proved. A positive common-mate witness would give only the UD/incomplete M0 of §2; actual isolated-word PR lifts, heterogeneous delays, every higher-gap class and eventual raw STAB/GP termination would still be necessary.

No independent proof of world-wide openness or novelty is implied by dated source reports. No H*, exhaustive-known-construction classification, homogeneous seed ansatz, finite-depth miss, residue-to-raw cancellation or boundary-dimension stabilization is used as the missing all-order step.

All displayed finite identities were checked in WRITING only. No scientific interpreter, arithmetic script, symbolic program, enumeration, replay, solver, build/lint/test, nested agent, external model CLI, shared edit, publication or new GO occurred. This is not formal/kernel, configured-family, human, executable, priority or novelty acceptance. The original October27 cutoff/deadline remain unchanged and this packet does not close the96-hour round.
