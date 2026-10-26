# Shor16 finite completion: a raw completion-shape core and one exact remaining witness obligation

Observed before this exclusive creation: **2026-10-23T15:13:44-0700 PDT**. Owner MathShor, slot math-5. This is the parent's requested SINGLE consolidation of the pinned source arguments, not a new problem, an independent discovery count, or a reset of the round deadline.

**Status: CANDIDATE consolidation.** The underlying source packets have the actual separate in-harness reconstructions recorded in section10. Those reviews do not automatically review these new consolidated bytes or establish parent acceptance, novelty, formal verification or a full solution. **The book's Question1 remains unresolved.** No finite UD complete extension is supplied, and no all-order noncompletion theorem is proved.

## 1. Exact target and honest delta

For distinct letters a,b, let

    C=b{1,a,a^7,a^13,a^14}
       ∪{a^3,a^8}b{1,a^2,a^4,a^6}
       ∪a^11b{1,a,a^2}.

The literal pairs (i,j) representing a^i b a^j are:

| i | j |
|---|---|
| 0 | 0,1,7,13,14 |
| 3 | 0,2,4,6 |
| 8 | 0,2,4,6 |
| 11 | 0,1,2 |

Question1 on printed pp64–65 asks whether there is a **finite** M⊆{a,b}^+ such that C⊆M, concatenation of every finite list of M-words is injective (UD), and

    for every w∈{a,b}*, some u,v satisfy uwv∈M*.

There is no bound on word lengths, cardinality, topology, symmetry, number of a's or b's, or form of additional words. Question2, general decidability, is different.

The completion-shape delta is one coherent package:

- The exact low-**a-count** raw words of every hypothetical completion are constrained through the two-, three- and four-a layers, with a genuine crossing restriction between their delays. The number of b's is unrestricted; these are NOT low-b/bayonet layers.
- A raw b-gap parse characterizes UD plus the book's factor completeness exactly and admits finite all-order certificates for an actually supplied M.
- Finite literal supersets satisfying ALL Bernoulli Kraft identities already exist for every sufficiently large prescribed length; an explicit selector is ambiguous. Probability normalization is therefore not the missing decodability proof.
- Even the full factor-coprime multiplier closure cannot create a collision using only the known Shor words and known border pieces. That enlarged scan has no such headroom.

These are shape, construction/control and route-limit statements. They are not a stronger pure-a order bound or a finite completion. The single existence-changing positive obligation is **RAW-SELECTOR** in section9.

### Baseline and source boundary

The inherited dossier proves a unique pure-a codeword a^n and actual border/all-t tiling data. Existing results include 1320|n. The October22 Rédei route restates the earlier conditional restriction as n=1320m with at least two distinct odd prime divisors of m, hence n≥19800. **That restatement is baseline, not an additional new condition here.** Its operative erratum remains mandatory.

The original Szabó2006 theorem/proof is still unauthenticated. The alternate Rédei statement is Cordero2023 Lemma5.2, explicitly citing the unread Szabó–Sands monograph proof. Those boundaries matter only where used below; the raw shape, gap criterion and Bernoulli construction are self-contained and do not use them.

The book images/transcription and exact pair record were read. [Cordero2019](https://www.normalesup.org/~cordero/Publications/A_Note_with_Computer_Exploration_on_the_Triangle_Conjecture.pdf) explicitly states the exact Shor inclusion question was unknown. [Cordero2023v1](https://arxiv.org/html/2301.13566v1), immediately after Definition1.5, leaves general n-cbc finite-maximal realization unknown. The bounded current literature and local/remote openai/math screens authenticated no full resolution. **UNCERTIFIED-OPEN is the screen status, not proof of continuing openness or novelty.** The inspected [Dai2026v2 classification](https://arxiv.org/html/2601.07135v2) requires order(pqr)^2 and equal cardinalities pqr, with three distinct primes; it does not directly classify orders already divisible by2,3,5,11. No unproved quotient reduction imports it here.

## 2. Mass equality and actual b-padding: the unrestricted raw interfaces

Let M be any hypothetical finite UD complete extension and D its maximum word length. For 0<x<1 put

    mu_x(w)=x^(|w|_a)(1-x)^(|w|_b),
    f(x)=Σ_(w∈M)mu_x(w).

Distinct lists of q codewords give distinct words of lengths q,…,qD. All binary words of each fixed length have total mu_x-mass1, hence f(x)^q≤qD-q+1 and f(x)≤1.

If f(x)<1, UD gives Σ_(z∈M*)mu_x(z)=1/(1-f(x))<∞. Factor completeness embeds every word w in some product; trimming whole codewords outside its occurrence gives z=u w v∈M* with |u|,|v|≤D-1. For each z and pair of end lengths there is at most one middle w. With c=min(x,1-x)>0,

    mu_x(w)≤c^(-2D+2)mu_x(z).

Summing over at most D^2 end-length pairs would make the mass of all binary words finite, contradicting mass1 at every length. Therefore

    Σ_(w∈M)x^(|w|_a)(1-x)^(|w|_b)=1                 (MASS)

for every positive parameter. Finiteness makes this a polynomial identity, so coefficient comparison at0 is legitimate.

Two actual padding facts will be used repeatedly:

**Core injectivity.** If U starts and ends in a, two distinct raw words b^i U b^j and b^(i') U b^(j') cannot both lie in M. Pad both outer b-runs to common maxima using the codeword b. This would give two different lists with the same concatenation. This is not cancellation inside M*.

**Small-core forcing.** Completeness embeds b^(2D) U b^(2D) in a product. Every codeword meeting an a of U lies wholly inside that factor because its length is≤D. Thus U's a-positions are partitioned by actual a-containing codewords. If no proper partition using smaller-a words is possible, one raw codeword with exactly the internal core U is forced. Its outer b-delays are nonnegative; core injectivity makes it unique.

## 3. The ENTIRE two-/three-a layer of every completion

The only pure-b word is b, since b^k for k≠1 would conflict with k copies of b. If A_j(y) sums y^(b-count) over raw words with j a's and N_j=A_j(1), (MASS) says

    1=(1-x)+Σ_(j≥1)x^j A_j(1-x).

Its x coefficient gives N_1=1, so the literal ba is the only one-a word. The b and ba terms sum to1-x^2; the x^2 coefficient then gives N_2=1.

The adjacent core a^2 cannot split into two ba words: the second a would need b immediately before it. Thus its unique two-a word has form

    W=b^r a^2 b^t.

Both delays are positive. If r=t=0, the literal a^8b factors as(a^2)^4 b. If r=0,t≥1,

    (ba)(a^2b^t)=(b)(a^3b)(b)^(t-1).

If t=0,r≥1,

    (b^r a^2)(a^11b)=(b)^(r-1)(ba^13)(b).

Each is an actual ambiguity using literal C-words. Hence r,t≥1. Since A_2(y)=y^(r+t), the x^3 coefficient of (MASS) gives N_3=r+t.

For1≤s<r, the core a b^s a^2 cannot be covered by ba followed by W, whose leading delay would need s≥r; no other proper partition can cover its adjacent last pair. It forces one word U_s. For1≤s≤t, the core a^2 b^s a cannot be covered by W then ba, whose boundary needs s≥t+1; it forces one V_s. The literal a^3b occupies the all-adjacent core. Thus exactly r+t distinct words are forced, exhausting N_3:

    a^3b,
    U_s=b^(alpha_s) a b^s a^2 b^(beta_s),   1≤s<r,
    V_s=b^(gamma_s) a^2 b^s a b^(delta_s),  1≤s≤t.       (LAYERS)

There are NO other three-a words, including none with three separated a's. All displayed delays are nonnegative, subject to the following exact Shor collisions:

    beta_s≥1                     for every1≤s<r;
    alpha_1≥1                    if r≥2;
    gamma_s≥1                    for2≤s≤t.             (DELAY)

Indeed beta_s=0 gives

    (b)(U_s)(a^11b)
      =(b)^(alpha_s)(ba)(b)^(s-1)(ba^13)(b).

If alpha_1=0,

    (ba^7)(U_1)=(b)(a^8ba^2)(b)^(beta_1).

If gamma_s=0 and s≥2,

    (ba)(V_s)=(b)(a^3b)(b)^(s-2)(ba)(b)^(delta_s).

No negative exponent is used. In particular the last argument does NOT assert gamma_1≥1 for arbitrary mixed-length completions. Empty U ranges remain allowed.

## 4. An exact all-order raw gap-parse realization criterion

This section applies to every finite raw M containing b and no other pure-b word, without presupposing UD or completeness. Write each a-containing word uniquely as

    w=b^(alpha_w) a b^(g_1(w)) a ... b^(g_(k-1)(w)) a b^(beta_w),
    k=|w|_a≥1.

A **free-end parse** of a finite nonnegative gap list(g_1,…,g_(q-1)) partitions its q a-positions into consecutive nonempty blocks labelled by actual M-words. Inside a block the gaps must equal that word's internal gaps. Between consecutive words u,v the actual gap must satisfy

    g≥beta_u+alpha_v.                                (BOUNDARY)

There is no end restriction because outside b-padding is free. Surplus b's at a boundary have the uniquely determined count g-beta_u-alpha_v. The empty gap list means ONE a-position, not zero a's.

**Gap theorem GP.** M is UD and factor-complete if and only if every finite nonnegative gap list has exactly one labelled free-end parse.

Forward, padded completeness with the2D margins supplies a parse. Two different parses can be padded to common outer b-lengths meeting both end delays. They then give genuinely distinct lists for the same raw word, violating UD. Conversely two actual M-factorizations induce parses of the same internal gaps; unique parsing fixes the a-containing word sequence and boundaries, then all intervening and outer b-counts. Pure-b products are unique. A parse for any a-core can be padded enough to meet its end delays, yielding a product containing any prescribed original word. These arguments prove both UD and precisely the book's factor-completeness quantifier, including zero gaps.

### Finite exact certificates, not a sampled gap cutoff

For a fixed finite candidate, choose B dominating all internal gap values and all thresholds beta_u+alpha_v. Gaps>B can be replaced by infinity: they never satisfy an internal equality and always satisfy a boundary inequality. Thus use the finite alphabet Gamma={0,…,B,infinity}.

States(w,j),1≤j≤|w|_a retain the actual raw word label. Initial states are(w,1); final states(w,|w|_a). Internal transitions follow that word's exact next gap. At a final state of u, a transition to(v,1) is allowed on every label satisfying(BOUNDARY). Paths consume one gap each and are exactly labelled parses; there are no epsilon transitions.

Let A_c be the integer transition matrix, I the initial row and F the final column. The all-order acceptance condition is

    I A_(c1)...A_(cq) F=1 for EVERY word of Gamma*.     (GP-COUNT)

A finite rational certificate uses B_c=diag(A_c,1), lambda=(I,-1), nu=(F;1), and rational V,z,T_c satisfying

    nu=Vz,       B_c V=V T_c for everyc,       lambda V=0.  (Q)

These identities put every B_word nu in a lambda-annihilated invariant subspace, proving(GP-COUNT). Conversely if all counts equal1, the rational span of the integer vectors B_word nu is finite-dimensional, invariant and annihilated by lambda, giving such a rational basis certificate. This is an exact witness language ONLY when actual finite M and its certificate are supplied. No such Shor instance is supplied here; finite point/gap tests would not prove it.

## 5. Genuine interaction and the complete forced four-a core table

Use A=ba with end delays(1,0), W with(r,t), P=a^3b with(0,1), and the U_s,V_s from(LAYERS). For1≤i<r and1≤k≤t, the core with gaps(i,0,k) admits two distinct lower-layer parses if both

    k≥beta_i+1,       i≥gamma_k:

one is U_i,A and the other A,V_k. Padding would create an actual ambiguity. Therefore EVERY completion satisfies

    beta_i≥k  OR  gamma_k>i,
    for every1≤i<r,1≤k≤t.                            (CROSS)

An additional four-a word cannot repair a failure: the two lower-layer factorizations already exist. This is a relation between opposite layer delays, not merely another count or permissible order.

The proper partitions of four a's are exactly

    1+1+1+1,2+1+1,1+2+1,1+1+2,2+2,3+1,1+3.

Applying(BOUNDARY) to all seven gives the following COMPLETE table. Every i,j,k in this table is POSITIVE. A row with no proper parse forces exactly one new raw word of that internal core; any proper parse forbids a raw four-a codeword of the same core. Actual lower-layer uniqueness, including(CROSS), is required—not presumed solved for higher layers.

| Gap pattern | No proper parse / exactly when a new four-a word is forced |
|---|---|
| (i,j,k) | Never; four A's parse it. |
| (0,j,k) | 1≤j≤t and1≤k≤delta_j. |
| (i,0,k) | None of: i≥r and k≥t+1; i<r and k≥beta_i+1; k≤t and i≥gamma_k. |
| (i,j,0) | 1≤j<r and1≤i<alpha_j. |
| (0,0,k) | k=1 and gamma_1≥1. |
| (0,j,0) | 1≤j<r+t, except j<r with alpha_j=0. |
| (i,0,0) | Never; A,P already parse it. |
| (0,0,0) | Never; A,P already parse it. |

For completeness, the partition derivation is short. For(0,j,k), W,A,A works if j≥t+1; otherwise V_j,A works iff k≥delta_j+1. For(i,0,k), only A,W,A; U_i,A; A,V_k are possible, with exactly the three tests shown. Their only cross-overlap is the rectangle prohibited by(CROSS). For(i,j,0), A,A,W works when j≥r; otherwise A,U_j works iff i≥alpha_j.

For(0,0,k), P,A works when k≥2. A,V_k requires gamma_k=0; (DELAY) excludes that for k≥2, while at k=1 it works iff gamma_1=0. For(0,j,0), W,W works if j≥r+t, A,U_j if j<r and alpha_j=0, and V_j,A is impossible because its last boundary would require0≥delta_j+1. Finally A,P permits all(i,0,0), including i=0. The all-positive case has the four-A parse. These exhaust every proper partition.

The forced core set is finite. In the middle row, any missing(i,0,k) has

    i≤max(r-1,max gamma_j-1),
    k≤max(t,max beta_j),

with absent maxima omitted; the northeast A,W,A region and the two U/V tails exclude everything beyond that rectangle. Other rows have explicit finite ranges. For each forced core the remaining outer b-delays are still unknown; this table is not a complete M.

## 6. Finite raw supersets already satisfy ALL Bernoulli mass constraints

This is a construction/control theorem, not a UD completion. For EVERY integer n≥246002, finite literal supersets C∪T_n exist with every extra word of length n, unique pure-a word a^n, exactly n one-b words, and

    Σ_(w∈C∪T_n)x^(|w|_a)(1-x)^(|w|_b)=1 for everyx∈[0,1]. (B)

An explicit selector below is ambiguous. Therefore these properties do not settle the raw existence question.

From the literal C rows,

    A(x)=Σ_C x^(i+j)
        =1+x+x^3+x^5+2x^7+x^8+x^9+x^10+x^11
          +2x^12+2x^13+2x^14.

Direct multiplication gives

    1-(1-x)A(x)=x^2 H(x),
    H(x)=1-x+x^2-x^3+x^4-2x^5+x^6-x^10+2x^13
        =(1-x)(1+x^2+x^4-x^5)+x^10(2x^3-1).            (H)

On[0,4/5], H≥1-x-x^10≥1/5-(4/5)^10>9/100. On[4/5,1], H≥(4/5)^10·3/125>3/1250>1/500. The inequalities1/10<(4/5)^10<11/100 follow from4^10=1048576 and5^10=9765625. Also H(1)=1 and H'(1)=14.

Write H=Σ_(j=0)^13 h_j x^j. For d≥13, homogenize:

    H_d(X,Y)=Σ_j h_j X^j(X+Y)^(d-j)
             =Σ_(k=0)^d g_(d,k) X^kY^(d-k),
    g_(d,k)=Σ_j h_j binom(d-j,k-j).

The coefficients are integers. Normalize using

    g_(d,k)/binom(d,k)=Σ_j h_j (k)_j/(d)_j.

The ratio is the all-in-a-k-subset probability for j draws without replacement; (k/d)^j is its with-replacement version. Conditioning on distinct draws gives the former law, so their difference is at most the collision probability, bounded by binom(j,2)/d. Thus, including k<j,

    |g_(d,k)/binom(d,k)-H(k/d)|
       ≤[Σ_j |h_j|binom(j,2)]/d
       =(1+3+6+20+15+45+156)/d=246/d.

At d≥246000 every normalized coefficient is≥1/500-1/1000=1/1000, so every g_(d,k) is positive.

Put n=d+2 and G_n=X^2H_d. Homogenizing(H) gives the literal identity

    G_n(X,Y)+Σ_s [x^s]A(x) X^sY(X+Y)^(n-s-1)=(X+Y)^n. (HC)

The second term is coefficientwise nonnegative. Hence each integer coefficient G_(n,k) lies between0 and binom(n,k), the exact number of available length-n words with k a's. Choose G_(n,k) distinct words independently in each composition. They form an actual finite SET T_n, not a multiset or signed formal language. Since n>15 it is disjoint from C. Substitution X=x,Y=1-x proves(B), including the endpoints.

The pure-a coefficient is g_(d,d)=H(1)=1. The one-b coefficient is

    g_(d,d-1)=dH(1)-H'(1)=n-16;

adding the sixteen literal Shor words gives exactly n one-b words. No residue tiling or UD claim follows.

The coefficient at a-count2 is exactly1. Choose that tail word to be

    W_n=(ba)(ba)b^(n-4).

Choose all other composition classes by their first required number of lexicographic words. This defines a finite family without claiming any exponential list was generated. Its single-word list[W_n] and the list[ba,ba,b,…,b] with n-4 copies of b give an explicit ambiguity. **This selector is non-UD for every n in the range.** It does not show that every different selector is ambiguous.

The number246002 is a coarse sufficient positivity threshold for this raw-set construction. It is NOT a necessary order lower bound, an improvement on19800, or an assertion of attainability as a code.

## 7. Exact endpoint shape INSIDE the homogeneous-tail route only

Suppose, as a sufficient construction ansatz, M=C∪T_n is UD complete and every extra word has length n, n≥5. Since C has no two-a word and only one three-a word a^3b, (LAYERS) implies

    r+t=n-2,
    alpha_s+beta_s=n-3-s,
    gamma_s+delta_s=n-3-s.                            (TAIL)

All forced four-a words must be extra, and their core gaps g impose

    outer-left+outer-right=n-4-(g_1+g_2+g_3).           (T4)

The interaction forces the following precise shape:

    r≥3, t≥1;
    gamma_s≥1 for ALL1≤s≤t;
    alpha_s≥1 for1≤s≤r-2;
    alpha_(r-1)=0, beta_(r-1)=t.                      (END)

First r=1 would give t=n-3≥2 and gamma_t+delta_t=0, contradicting(DELAY). Thus r≥2 and each V_s has total outer delay at least r-1≥1. If gamma_s=0, take the positive last gap delta_s. Row(0,s,delta_s) of the four-a table forces a new core of length4+s+delta_s=n+1, impossible in a length-n tail and absent from C. Hence every gamma_s≥1.

At s=t, gamma_t≤r-1 by(TAIL). Apply(CROSS) at i=r-1,k=t to obtain beta_(r-1)≥t; its total outer-delay budget equals t. Thus alpha_(r-1)=0,beta_(r-1)=t. If r=2 this contradicts alpha_1≥1, so r≥3.

Finally if alpha_s=0 for s≤r-2, then beta_s=r+t-1-s≥t+1. The core(s,0,beta_s) has none of the three proper parses in its row and length n+1, again impossible. This proves(END).

Consequently EXACTLY ONE EXTRA three-a word starts with a:

    U_(r-1)=a b^(r-1) a^2 b^t.

The fixed short a^3b is not included in that count. These endpoint conclusions are NOT transferred to general mixed-length completions. Rejecting every homogeneous-tail selector, if eventually achieved, would still not settle the unrestricted book question negatively.

## 8. Why the known-word multiplier route is saturated

This separate route-limit statement uses the inherited completion-to-border interface. Let its actual residue sets be R,L and its one-b set Y. The dossier supplies

    |R||L|=|Y|=n, R⊇R0={0,1,7,13,14}, L⊇L0={0,3,8,11},

and the all-t bijections R×Y^t×L→Z_n^(t+1), with coordinates(r+i1,j1+i2,…,jt+l). It also supplies330||R|,2||L| and1320|n, where330||R| here means330 divides the cardinality |R|, not exact divisibility. The declared Rédei input gives an odd prime divisor of |L|. These are existing interfaces, not new conclusions of this consolidation.

For clarity, the purely combinatorial separator is stronger than the needed multiplier subclass. Let n be any multiple of1320 and let each position use

    Z_k={(u_k i,v_k j) mod n:(i,j)∈C},
    u_k odd, 8u_k≠0 mod n, gcd(v_k,330)=1.

Define T⊆Z_n by residues not divisible by5,11 or8, and with every3-divisible member even. Then0∉T and T=-T. The exact positive left differences of C are D0={3,5,8,11}; the within-row right differences are S0={1,2,4,6,7,12,13,14}. R0 differences are a subset of S0 and L0 differences are D0.

Every ±v_kS0 belongs to T and is nonzero. Every ±u_kD0 is nonzero and outside T:3u_k is odd and3-divisible,5u_k and11u_k fail the respective exclusion, and8u_k fails the8-exclusion. Odd d∈{3,5,11} cannot give0 modulo8; the8-case is the explicit guard. Thus each Z_k has sixteen distinct points.

An edge of the difference graph is formed by DISTINCT points of ONE transform, with source u(i-i') and target v(j'-j). A source0 edge has equal original rows and enters T; every nonzero source is outside T. No T vertex has an outgoing edge, even in the superposition over all allowed transforms. Hence there is no nonempty path0→0.

More strongly, R0×Z_1×…×Z_t×L0 maps INJECTIVELY to Z_n^(t+1) for every t. Equality at the first coordinate equates a difference in T from R0 with a transformed row difference outside T, forcing both0. The first original rows therefore agree, so their right difference is0 or in T. At the next coordinate it equals another row difference, again forcing both0. Continue inductively; the final coordinate compares a last right difference in T with an L0 difference outside T. All tuples agree. At t=0 the same separator proves injection of R0+L0.

[Cordero2023 Theorem7.2](https://arxiv.org/html/2301.13566v1) permits left multipliers u coprime to |L| and right multipliers v coprime to |R| on a full compatible n-cbc stable family with that border. Its orientation is retained exactly. Even |L| makes u odd; an odd prime p||L| would divide u if n|8u, so8u≠0. The condition330 divides |R| gives gcd(v,330)=1. Thus EVERY permitted factor-coprime transform of the forced sixteen points falls under the separator, including nonunits modulo n.

This proves no collision headroom for this known-word/known-border route at ANY product length. It does not prove surjectivity, a full border, a full n-cbc, a UD union of all transformed sets, or a finite completion. Unknown added words/border elements remain outside this restriction. The inaccessible Szabó proof and original Sands construction are not used to close that gap.

## 9. RAW-SELECTOR: the single remaining positive obligation

**Unrestricted form.** Supply actual finite raw M⊇literalC together with a valid certificate of UD and factor completeness. One sufficient and witness-language-complete option is a finite nonempty residual set S_res such that:

1. Every nonempty proper-prefix residual between distinct M-words lies in S_res.
2. For each r∈S_res,x∈M, whenever r=xv or x=rv, the suffix v lies in S_res.
3. epsilon∉S_res, including the forced rejection when r=x.
4. The exact integer Kraft equality holds for the actual raw length profile:

       Σ_(l=1)^D c_l 2^(D-l)=2^D.

Prefix cancellation of a hypothetical two-list ambiguity would start in S_res and keep a residual there until it became empty, proving UD. At Kraft sum1 the total normalized mass of M* diverges. If a word of length h were a missing factor, avoiding it in each disjoint h-block would bound that total mass by

    Σ_(r=0)^(h-1)Σ_(q≥0)(1-2^(-h))^q=h2^h<∞,

a contradiction. Thus this certificate proves the literal completeness quantifier. Conversely every finite UD complete M has Kraft sum1 by section2 and admits the finite epsilon-free closure of its reachable proper-suffix residuals. No actual M,S_res instance is supplied here.

The GP/Q certificate in section4 is an alternative exact witness language, not an extra scientific problem. A literal M* membership certificate for a^i b a^j with i,j<n also suffices for actual M membership if a^n∈M: exactly one factor can contain b, and all other factors would be a^n, impossible within either short outer a-run.

Residues alone are insufficient. For example

    M0={aa,b,abb,aaaba,baba,abbaba,abaaba}

is UD: it substitutes the complete prefix code{aa,b,aba,abb} into the abstract suffix code{P,B,Y,PX,BX,YX,XX}. Its binary Kraft sum1 makes it complete by the preceding proof. Its pure-a order is2 and canonical C_M0(b) contains(1,1), but aba∉M0*, since no M0-word is a prefix of aba. This is a written positive/negative control, not a Shor witness or an executed test.

**Concrete sufficient route.** For some n in the Bernoulli construction range, choose the required number G_(n,k) of literal length-n words of each composition, respecting(LAYERS),(DELAY),(CROSS), the four-a table and(END), then satisfy ALL remaining residual or gap-parse conditions. A successful actual selector plus certificate proves a finite Shor completion without any general n-cbc converse. No such selector is known here.

The homogeneous-tail route has NOT been proved exhaustive for arbitrary finite extensions. A failed selector, an exhausted finite range, or even an impossibility theorem for that ansatz cannot prove unrestricted noncompletion. A negative answer still needs an obstruction reaching EVERY finite raw extension. The original scientific existence conclusion is therefore unchanged.

## 10. Pinned provenance, actual reviews and limits

Every source pin below was re-observed by a metadata-only shasum call before consolidation. Original snapshots remain immutable. The consolidation assembles these same claims and proofs; it does not upgrade their source trust or their earlier review histories.

| Source in this owned root | SHA256 |
|---|---|
| selection-v1.md | d7ac86b0c69dc96b82361d16c17145593e47b6c3d8dce7c99a539bf34be00ba3 |
| proof-multiplier-saturation-v1.md | 67d8b1fdd87c4010bf1818971b4cd6dbabb5ef054160563d4b1fb36c54a4068a |
| raw-realization-protocol-v1.md | 544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578 |
| proof-BERNOULLI-TAIL-REALIZATION-v1.md | 3918ca67108d0dc98620760209474cc306750110d910dbdb2fd167d7eea48de3 |
| proof-RAW-TWO-THREE-A-LAYERS-v1.md | 0614a8e399f789397cdfaf4c6c6adb3d514f884264f6bc5fbd9e22cd71465ba2 |
| proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md | adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb |
| proof-RAW-TAIL-ENDPOINT-COROLLARY-v1.md | 4dca62723aa4f87aeb078d5fde1899e3c74c0c9dbffdeb4fa3025708404fb75c |

Actual separate supplied-proof reconstructions, all read in full:

| Reviewer and source coverage | Review path, relative to parallel-18 | SHA256 | Actual finding |
|---|---|---|---|
| MathSun8: full multiplier source and declared imports | sun-coset8/peer-review-Shor-multiplier-saturation-v1.md | 680511e7d354f729ccc4596d126c661874c164b8eb628536469ab47bbc55a10f | 0F/0M/0minor at S1–S3 and conditional import scope |
| MathResearch96h: full Bernoulli, residual protocol and selection | phase-type/peer-review-Shor-Bernoulli-realization-v1.md | 22e793f4febf64e1cd187bcaac87204bf7abd08d42a0eef5af79e890a8f2f310 | 0F/0M/0minor; raw construction/control, no UD witness |
| PhysicsAME46: full raw2/3, GP/four-a and endpoint sources plus dependencies | physics/evidence/three-area-20261023-96h/parallel-18/ame46-support/peer-review-Shor-raw-layers-and-parser-v1.md (repository-relative) | fddd213f46bddd5ecda4c6e9e2e8b340522cc67f3329d9d7c1a908ff15a0e073 | 0F/0M/0minor at unrestricted raw and explicitly homogeneous scopes |

Literal target pins are the book transcription642b818093ac231cbc44006dc324d73492c6ad9a9b71c469a327cbb4307a75c8 and raw-instance6eb38f63bfee602369a09b22be26a0c598111f33b8202d44349786903f63ecf4. The inherited dossier proof is fe22a69786a237e144c6e4f06c08bee9f8dcd3ac6cbd365b4fab054debf312e6; the October22 operative erratum is477091ac3590d807c7fab6237742e099ffd50032b80e91242ecd3fdcfcd7aee6; retained Cordero2023 text is c2cc3649b9b9ad36a3b563b2a9c88fca7bc07406e43263cb44f43afa75e57f86. The source-screen record must be read WITH source-screen-pin-erratum-v1.json: one Cordero2019 summary hash there was transcribed incorrectly and explicitly withdrawn; the correct source-specific pin is retained. No result depends on that erroneous summary field.

The three reviewers are different in-harness task agents with supplied proofs and shared steering, not necessarily distinct model families or blind evaluators. No review is human, cross-vendor, formal/kernel or novelty certification. Parent consideration and a fidelity/claim check of these consolidated bytes remain separate. Classical mechanisms include multiplier arguments, Sardinas–Patterson cancellation, weighted counting, homogenized coefficient positivity and finite-state linear representations; their exact target application is NOT priority-cleared.

All work here was written mathematics, source inspection and metadata dates/hashes. No scientific script, word enumeration/generation, solver, compilation, Lean, build/test/formatter, independent-model CLI, nested agent, Git mutation, shared-index change, publication or external contact occurred. Both parent verification/timestamp errata remain operative; ordinary arithmetic or finite observations are not called a proof-assistant kernel. No execution GO is requested.
