# Shor completion: self-contained review packet for the order-2640 even-tail candidate

Owner: MathShor-2, math-5. Native `/bin/date` before drafting: `Wed Oct 28 21:48:42 PDT 2026`.

**Status: UNREVIEWED CONDITIONAL CANDIDATE; WRITTEN plus previously completed exact finite integer checks.** The proposed conclusion is only that a finite uniquely decipherable, factor-complete extension of the literal code below, whose actual pure-`a` atom is `a^2640`, cannot have an even-cardinality actual `b`-run tail border. All border sets throughout belong to the SAME putative code. This is not an adopted no-go, formal proof, human review, independent-model-family review, novelty clearance, an unconditional order-2640 exclusion, or a solution of the original problem. **Odd tail at order 2640, other orders, and the original unrestricted finite-completion problem remain OPEN.** The pending odd-tail theorem is not an input. Earlier even-tail fibre packets are not inputs to this proof.

This packet embeds the reductions and the arguments for every branch. The exact finite results are review claims about the pinned programs and certificate in §10, not substitutes for reading their source or for a disjoint scientific review. No solver timeout is used as an exclusion. The proof requires the explicitly identified classical T2 theorem in §3; it does not claim to prove it.

## 1. Literal problem and actual border

Let `1` denote the empty word and let the original finite set of words be exactly

    S = b{1,a,a^7,a^13,a^14}
        union {a^3,a^8} b {1,a^2,a^4,a^6}
        union a^11 b {1,a,a^2}.

Assume for contradiction that a finite code `D` contains S, concatenation of sequences of atoms of D is injective (unique decipherability, UD), every word over `{a,b}` is a factor of a word in `D*` (factor-complete), the unique actual pure-`a` atom is `a^n` with `n=2640`, and the actual tail border defined below has even cardinality. These are assumptions on D itself, not on a separate extension, auxiliary automaton, one-`b` slice, or chosen hypothetical tiling.

Existence and uniqueness of the pure-`a` atom are not assumed without explanation. Let L be the maximum length of an atom of finite D. Completeness embeds `a^(2L+1)` in a D-factorization. Some atom lies wholly inside this `a`-run, so a positive pure-`a` power is an actual atom. Two distinct pure-`a` atoms `a^u,a^v` would give two distinct atom lists `(a^u,a^v)` and `(a^v,a^u)` with the same word, contrary to UD. Likewise, because the literal code contains the atom `b`, UD forbids any other pure-`b` atom: `(b^k)` and k copies of `(b)` would be different factorizations.

Define residues in `Z_n`, allowing actual border atoms with **any positive number of consecutive b's**:

    P = {i mod n : a^i b^k is an atom of D for some i>=0, k>=1},
    Q = {j mod n : b^ell a^j is an atom of D for some j>=0, ell>=1}.

The old words give

    A = {0,3,8,11} subset P,       Y = {0,1,7,13,14} subset Q.

The needed classical actual-word statement is the Restivo–Salemi–Sportelli border theorem, as stated in Christophe Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1): for a finite maximal code containing `b,a^n`, those actual `b+` borders factor `Z_n` directly. The following elementary reconstruction uses only the explicitly assumed factor-completeness and UD; it avoids silently equating an arbitrary finite completion with a different maximal code.

**Directness.** Choose actual representatives `u_t=a^(i_t)b^(k_t)` and `v_t=b^(ell_t)a^(j_t)` for two representations with `i_1+j_1=i_2+j_2 mod n`. Pick positive G in their common class, larger than both actual `i_t+j_t`, and choose K and H large enough. For each t the actual D-atom list

    (b)^(H-ell_t), v_t, (a^n)^((G-i_t-j_t)/n), u_t, (b)^(K-k_t)

spells `b^H a^G b^K`. The factors `(b)^r` mean r separate `b` atoms. If a border atom has no `a`, it is `b` by the preceding paragraph. Otherwise the left non-`b` border atom starts with b and ends with a; the right non-`b` border atom starts with a and ends with b. The positive central pure-`a` run and this orientation distinguish the actual border atoms, including the cases where one is just b. Thus genuinely distinct residue pairs give distinct atom lists, forbidden by UD.

**Coverage.** Embed `b^L a^g b^L` into a D-factorization for any `g>L` in a chosen class modulo n. The atom containing the last left b begins inside the left guard, and it cannot reach the first right b; hence it is `b^ell a^j`. Similarly the atom containing the first right b is `a^i b^k`. They are distinct, and all atoms between them are pure a and therefore copies of `a^n`. Hence `g=i+j mod n`, giving coverage of every residue. Directness and coverage yield

    P direct-sum Q = Z_2640,     |P||Q|=2640.                       (1)

## 2. Difference classes, screens, and the minimum head count

For a subset R of `Z_n`, let `Delta(R)={gcd(r-r',n): r,r' in R, r!=r'}`. The necessary **Sands divisor-exclusion** statement is `Delta(P) intersect Delta(Q)=empty`; the full equivalence, with `|P||Q|=n`, is in Łaba–Londner, *Combinatorial and harmonic-analytic methods for integer tilings*, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3). Brief reconstruction: if two nonzero differences have the same gcd with n, a unit modulo n maps one difference to the other. Multiplying P by a unit preserves its cyclotomic zeros at all n-th roots, so `uP direct-sum Q` still tiles by the mask identity. The mapped difference then gives a collision. Conversely, a shared gcd necessarily gives such a collision after a unit replacement, which is all that is used here.

At n=2640,

    G_A = Delta(A) = {3,5,8,11};   G_Y = Delta(Y) = {1,2,6,12}.

For a set of forbidden gcd classes F and an anchor set B define the **exact individual screen**

    Screen(B,F) = {x in {0,...,2639}: for all b in B,
                   x=b or gcd(x-b,2640) is not in F}.

Every actual `P` is contained in `Screen(A,G_Y)` and has no pair-difference gcd in `G_Y`; every actual `Q` is contained in `Screen(Y,G_A)` and has no pair-difference gcd in `G_A`. If a partial head set `S0 subset P` is known, set `H=Delta(S0)`; actual Q is contained in `Screen(Y,H)` and has no pair-difference gcd in H. If another head difference g is separately forced, include g in H. These are necessary conditions only; satisfying them does not imply a code or a tiling.

The anchor sets imply `|P|>=7` in this same group, without a computer search. All identities below are in `Z_2640`, and the two P entries in any displayed collision are distinct. Since `A subset P`, only sizes 4,5,6 must be ruled out.

* If `P=A`, covering 6 would require one of Q-elements `6,3,-2,-5`, respectively contradicted by `6+3=1+8`, `3+0=0+3`, `(-2)+3=1+0`, and `(-5)+8=0+3`.
* If `P=A union {U}`, cover `U+4`. Its candidates `U+4,U+1,U-4,U-7,4` would respectively collide through `(U+4)+3=7+U`, `(U+1)+0=1+U`, `(U-4)+11=7+U`, `(U-7)+8=1+U`, and `4+0=1+3`.
* If `P=A union {U,V}`, the same five collisions applied to `U+4` force `U-V+4 in Q`; interchanging U and V forces `V-U+4 in Q`. To cover `U+9`, the five candidates `U+6,U+1,U-2,9,U-V+9` are forbidden by `(U+6)+8=14+U`, `(U+1)+0=1+U`, `(U-2)+3=1+U`, `9+0=1+8`, and `(U-V+9)+3=(U-V+4)+8`. The sixth candidate forces `U+9 in Q`, and symmetrically `V+9 in Q`. Then `(U+9)+V=(V+9)+U` is a directness collision. Thus `|P|>=7`.

If a displayed Q candidate specialized to an already present Q value, the corresponding collision would force equality of two distinct P values; hence specializations are not omitted.

## 3. Exact imported tiling theorems and elementary consequences

The only deep imported statement used below is the **Coven–Meyerowitz two-prime T2 theorem**, stated in Łaba–Londner, [arXiv:2106.14042v3, p. 3, Theorem 1.1](https://arxiv.org/pdf/2106.14042v3), and also in [the HTML introduction](https://arxiv.org/html/2106.14042v1). Precisely: let F be a finite integer tile, let `F(X)=sum_(f in F) X^f`, and let `S_F` be the prime powers `p^j` whose cyclotomic polynomials `Phi_(p^j)` divide `F(X)`. If the cardinality `|F|` has at most **two distinct prime divisors**, then for every selection of powers `s_1,...,s_k` in `S_F` of pairwise different underlying primes, `Phi_(s_1 ... s_k)` divides `F(X)`. Here the relevant F is always the actual P with `|P|=12,22,24`; it tiles the integers with complement `Q+2640 Z` by (1). No T2 claim is made for arbitrary tile sizes, for an unproved factorization conjecture, or for a three-shared-prime case.

For completeness, the related Łaba–Londner **Corollary 6.2**, [arXiv:2106.14042v3, p. 26, §6.1](https://arxiv.org/pdf/2106.14042v3), states: if `U direct-sum V=Z_M`, `M=product p_i^(e_i)` with distinct primes, and after ordering the primes each `p_i` for `i>=3` divides at most one of `|U|,|V|` (equivalently at most two primes divide both cardinalities), then **both** U and V satisfy T2. That corollary is a stronger alternative under its stated common-prime hypothesis; the branch deductions here do **not** rely on it. These exact hypotheses matter.

All other prime-balance facts used here follow from (1). Write the integer masks of P,Q with canonical representatives. At every nontrivial root of unity whose order divides 2640, at least one mask vanishes. For prime p occurring once in `2640=2^4*3*5*11`, the factor `Phi_p` belongs to exactly one mask, since `Phi_p(1)=p` and `|P||Q|=2640`. Thus whichever cardinality is divisible by p is uniform modulo p, with `|side|/p` entries in each residue class. Likewise, each of `Phi_2,Phi_4,Phi_8,Phi_16` belongs to exactly one mask: each evaluates to 2 at 1, and the total 2-adic valuation of the product of cardinalities is 4. Consequently P owns exactly `v_2(|P|)` of these four factors and Q owns the others. Divisibility is in `Z[X]`, and reduction modulo `X^m-1` preserves divisibility by every factor of `X^m-1` used below.

Two structural deductions, needed only in the indicated cases, are written out rather than imported as additional theorems.

**(i) P=3·2^a parity, used for 12 and 24.** P is uniform modulo 3, with `2^a` heads per class. Suppose `Phi_2` is not owned by P. Let I be P's a owned two-power indices, all at least 2. T2 with `Phi_3` and the elementary identity

    Phi_(2^s)(X) Phi_(3*2^s)(X) = 1+X^(3*2^(s-1))

imply `R(X^3)` divides P, where `R(T)=product_(s in I)(1+T^(2^(s-1)))`. Write uniquely `P(X)=P_0(X^3)+X P_1(X^3)+X^2 P_2(X^3)`. Free-module decomposition over `Z[X^3]` shows R divides every `P_j(T)`. R is even in T and `R(1)=2^a`, so the sums of even-index and odd-index coefficients of `P_0` are each multiples of `2^a`. Both are positive because old heads 0 and 3 occur, yet their sum is the entire mod-3-class-0 count `2^a`: contradiction. Thus P owns `Phi_2`. T2 supplies `Phi_6`; their product `1+X^3` makes each `P_j(T)` divisible by `1+T`, so every mod-3 class has equal even/odd head counts.

**(ii) P=22 parity, used for 22.** P owns `Phi_11` and has exactly two heads in each mod-11 class. P owns exactly one of the four two-power factors, say `Phi_(2^s)`. T2 adds `Phi_(11*2^s)` and

    Phi_(2^s)(X) Phi_(11*2^s)(X) = 1+X^(11*2^(s-1)).

Folding modulo `11*2^s`, the two heads in each mod-11 class must occur at paired positions differing by `11*2^(s-1)`. The old heads 0 and 11 fill class 0, so their separation 11 forces `s=1`. Thus every mod-11 P class contains one even and one odd head. Q owns `Phi_4,Phi_8,Phi_16`, whose product is `1+X^2+...+X^14`; hence its 16 folded counts are a common integer a in each even class and b in each odd class, with `a+b=15`. Old Q contains 0 and 1, so `a,b>=1`.

## 4. Exhaustive even-tail size sieve

The screened head set has 224 residues; the screened tail set has 658. The explicit pinned certificate partitions ALL 658 tail candidates into 266 nonempty `G_A`-conflict cliques, and its independent checker verifies the partition and every pair within every clique. Therefore `|Q|<=266`. Among the 24 screened P candidates equal to 1 modulo 3 the following eight disjoint `G_Y`-conflict pairs leave capacity at most 16:

    (256,418), (415,253), (916,1078), (1075,913),
    (1576,1738), (1735,1573), (2236,2398), (2395,2233).

For transparent reconstruction, the screen residue-count vectors, listed in increasing residue order, are

    P mod 3:  [100,24,100]                Q mod 3:  [213,232,213]
    P mod 5:  [36,36,12,128,12]          Q mod 5:  [182,98,98,98,182]
    P mod 11: [80,12,12,24,12,12,12,12,24,12,12]
    Q mod 11: [62,50,50,62,64,64,64,50,64,64,64].

By `|P|>=7`, `|P|<=224`, divisibility, and even `|Q|`, the complete raw divisor list is

    8,10,11,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132,165,220.

`P=8` would give `Q=330>266`. `P=11` would be uniform mod 11 with one per class but contains both 0 and 11. `P=60,66,120,132,165` require more than 16 P-elements in mod-3 class 1. `P=110,220` require respectively 22 and 44 heads in every mod-5 class, but screened classes 2 and 4 have only 12 each. Thus the exact remaining even-Q sizes are

    |P| in {10,12,15,20,22,24,30,33,40,44,55,88}.                 (2)

No omitted cardinality is treated as feasible. The clique certificate and verifier are pinned in §10. A deterministic self-contained cover-generation rule is also given there.

## 5. Finite search contract used in the branches

All calculations in §§6–9 use exact integers, gcd, finite combinations and the following necessary relaxation. For a forbidden gcd set F, candidate set C, groups `G_j={x in C:x=m_j residue r_j}` and exact required counts `k_j`, optional mandatory anchors are first selected; their forbidden neighbors are removed and every group quota containing them is decremented. A state consists of the remaining active vertices and all remaining group quotas. At each state:

1. Reject if a quota is negative; delete all active vertices from any group whose remaining quota is zero; reject if a group has fewer active vertices than its remaining quota.
2. If all quotas are zero, return SAT: the selected vertices form a witness for this *relaxed selection*, not necessarily a full border.
3. Otherwise choose any active vertex in a positive-quota group. The include child removes that vertex and all its F-conflicting neighbors and decrements every group containing it. The exclude child removes only that vertex. The state is UNSAT only when both children are UNSAT. Memoization stores only fully exhausted UNSAT states.

Every allowed selection is in exactly one child, so a completed UNSAT search is complete for that finite stated relaxation; each capacity rejection is necessary. When only two quota groups are retained, C is their union and only the specified old anchors lying there are required. Any actual Q restricts to a selection of exactly those group counts, so UNSAT still excludes Q. In the full-fibre cases all residues are retained. The searches do not assume that individual screen membership gives pairwise compatibility, and do enforce all pairwise F-conflicts. Multiple head choices inducing the identical H have identical tail instances; stated frequency counts preserve coverage. Branch-dependent individual-capacity tests are applied before quota search in the order stated, so their categories do not overlap.

The pinned producer and replay programs implement these finite partitions as described below. The replay programs are separately written representations in the same harness; some use the same slack-based branching rule. Their reported counts and check outcomes are **unreviewed evidence**, not an independent-family proof. Positive controls are explicitly relaxations and never evidence that a full border tiling or D exists.

## 6. The four written head obstructions: P=30,33,55,88

**P=30 and P=33.** P is uniform modulo 3. In `Screen(A,G_Y)`, the 24 candidates in class 1 split into

    T = [256,415,916,1075,1576,1735,2236,2395]
    Z = [88,253,418,583,748,913,1078,1243,
         1408,1573,1738,1903,2068,2233,2398,2563].

Every T element is outside mod-5 class 3 and mod-11 class 0; every Z element lies in both. For Z, the exact forbidden-`G_Y` neighbor sets in T are

    88,1408       -> {916,2236}
    583,1903      -> {1075,2395}
    748,2068      -> {256,1576}
    1243,2563     -> {415,1735}
    253,913,1573,2233   -> {415,1075,1735,2395}
    418,1078,1738,2398  -> {256,916,1576,2236}.

For `P=33`, its mod-3 class 1 requires 11 heads, while P is uniform mod 11 with three in class 0 and old 0,11 already occupy two; at most one Z is available. Thus at most `8+1=9` heads.

For `P=30`, its mod-3 class 1 requires 10 heads. P is uniform mod 5 with six in class 3, and old 3,8 already occupy two, so at most four Z can be selected. If t T-elements are selected: for `t<=4` the total is at most eight; for `t>=7` no Z survives; for `t=6` the two omitted T-elements can contain at most one of the four disjoint two-blocker pairs, admitting at most two Z; and for `t=5` three omissions can contain at most one such pair and no four-blocker set, again admitting at most two Z. Every case gives at most eight, contradiction. The pinned integer checker verifies this table and all 256 T-subsets.

**P=55.** P is uniform modulo 5 with 11 elements per class. Screened mod-5 classes 2 and 4 each have 12 candidates. Four disjoint old-tail-conflict pairs are

    (872,459), (2192,1779), (987,344), (2307,1664),

all gcd 1. Choosing 11 in each class omits only two of the 24 candidates, while avoiding these four disjoint pairs requires at least four omissions. Contradiction.

**P=88, Q=30: force head gcds 4,55,240.** P is uniform modulo 11 with eight heads per class.

* If gcd 4 is absent from P, screening additionally against 4 leaves exactly eight candidates in each of mod-11 classes 1 and 4, forcing 155 and 576, whose difference has forbidden gcd 1.
* If gcd 55 is absent, the screen of class 5 has 12 candidates including 456; omitting it leaves four disjoint 55-conflict pairs `(368,423),(1028,1083),(1688,1743),(2348,2403)` among the 11 remaining, so at most seven can be chosen. Thus 456 is forced. Similarly class 2 forces 35 using `(68,123),(728,783),(1388,1443),(2048,2103)`. The pair 456,35 has gcd 1.
* If gcd 240 is absent, the additionally screened classes 2 and 10 have ten candidates each. The five disjoint cross pairs `(35,1176),(68,1748),(123,1803),(783,2463),(816,395)` have gcd in `G_Y union {240}`, so at most 15 of their 20 class candidates can be selected, below the required 16.

Consequently Q must avoid `F=G_A union {4,55,240}`. It is uniform mod 5 with six per class and mod 3 with ten per class. The F-screen contains no `1 mod 3` candidate in mod-5 classes 0,4; in classes 1,2,3 its `1 mod 3` candidates are all odd. These three classes have 18 selected tails in total, exactly ten `1 mod 3`, and therefore exactly eight from the following 16 non-1-mod-3 candidates:

    [33,47,113,231,311,627,707,1287,1367,1947,2027,2343,2423,2541,2607,2621].

Two distinct 1-mod-3 candidates in one `(mod 5,mod 16)` slot have difference gcd exactly 240, so each slot supplies at most one; there are 24 such odd slots. Among all `C(16,8)=12870` seeds, the checker reports 12657 with internal F conflicts, 33 more overfilling a mod-5 class, and 180 more with insufficient individually seed-compatible slots in some class. This last test ignores conflicts among the prospective slot occupants, so it is a relaxation. There are zero remaining seeds. A separate replay enumerates omitted seeds; an 18-element Q-only control works after dropping gcd 240, but is not a full Q or tiling.

## 7. P=40 and the common forced-240 lemma for P=22,44

**P=40, Q=66.** P has eight per mod-5 class, Q has 22 per mod-3 class and six per mod-11 class. Each of 4,16,660,1320 must occur as a P-difference gcd:

* If 4 is absent, the additionally screened P mod-5 classes 2 and 4 each have exactly eight candidates, forcing 872 and 459, with forbidden gcd 1. If 16 is absent, the same count forces 872 and 1779, also gcd 1.
* If 1320 is absent, the 12 additionally screened mod-5 class-4 candidates are covered by the six disjoint 1320-conflict pairs `(264,1584),(344,1664),(459,1779),(539,1859),(924,2244),(1199,2519)`, so at most six can be selected.
* If 660 is absent, the 12 class-4 candidates are two gcd-660 four-cycles `(264,924,1584,2244)` and `(539,1199,1859,2519)`, plus four singletons `{344,1664,459,1779}`. Selecting eight forces all singletons and one of the two opposite pairs from each cycle. In each of the four cases, compatibility with these choices and all old heads leaves exactly `{11,396,1056,1331,1716,2376}` in class 1, below its quota eight.

Hence Q avoids `F=G_A union {4,16,660,1320}`. Its old-tail screen has 457 candidates. The quota search with all five old Q anchors, all three mod-3 quotas 22 and all eleven mod-11 quotas 6 reports UNSAT in 2,983 nodes with 611 quota prunes; the separately written set replay reproduces those numbers using the same slack rule. A literal 66-tail control satisfies the prime balances and old-head gcd restrictions after the four extra forced classes are removed; it is not a factorization. The first P40 producer failed an overly strong equality (it asserted eight where the correctly anchor-filtered count is six) and the first differently ordered replay timed out after 35 seconds; neither is evidence of UNSAT. The corrected v2 sources are the pins in §10.

**Forced 240 lemma, used for P=22 and P=44.** Suppose P contains old A, avoids `G_Y`, and has at least two members in each of mod-11 classes `(2,10,9,7,3)`. If P also avoided gcd 240, then `Screen(A,G_Y union {240})` restricted to those five classes contains exactly 63 candidates. Restrict actual P to any two in each class, choosing old head 3 as one of its class-3 pair. This gives a necessary ten-head quota selection, pairwise avoiding `G_Y union {240}`. The complete include/exclude search of §5 reports UNSAT: bitset producer 5,521 nodes / 1,187 quota prunes, independently written set replay 32,971 nodes / 16,486 quota prunes. The literal control

    [3,35,68,128,183,395,428,515,548,608]

has two heads per named class, contains 3, respects old-head screen and `G_Y` pairwise, and has a gcd-240 pair. It demonstrates that dropping 240 makes this relaxation SAT; it is not a border tiling. Therefore every P satisfying the lemma's hypotheses must use gcd 240. P=22 has exactly two and P=44 exactly four in each mod-11 class, so both satisfy the hypotheses.

## 8. Exhaustive partial-head / tail-quota branches

For every row below, join each partial head choice to old A, discard choices containing a `G_Y`-conflicting pair, and define `H=Delta(partial heads union A)`, additionally adjoining 240 in the P=22 and P=44 rows by §7. Screen all possible tails against **all** old Y and H; then enforce the displayed pairwise H-conflicts and quotas. Counts are numbers of head choices, not numbers of distinct H, unless explicitly marked.

**P=10, Q=264.** P has two per mod-5 class; the old-anchor head screen has 12 each in classes 2 and 4. There are `C(12,2)^2=4356` partial choices: 866 conflict, leaving 3490 choices and 210 distinct H. Q has 88 per mod-3 class and 24 per mod-11 class. Of the 3490, 408 fail mod-3 individual capacity, then 2636 fail mod-11 capacity. The remaining 446 choices induce 64 H. For every H, the relaxed selection with quotas `(mod 3, residue 0, count 88)` and `(mod 11, residue 2, count 24)`, mandatory tails 0,13, is UNSAT. Producer and complement/set replay report maximum 1,297 and 3,441 nodes respectively. The producer checks a 106-tail positive relaxation with the same two quotas and old-head/old-tail restrictions after extra partial-head gcds are omitted.

**P=15, Q=176.** P has five per mod-3 class and three per mod-5 class. Old heads 3,8 already use two places of mod-5 class 3, so among the five selected from the 24 screened mod-3-class-1 candidates at most one lies in that mod-5 class. There are eight outside and 16 inside; the complete raw allocation has `C(8,5)+C(8,4)*16=1176` choices. After `G_Y` pair conflicts, exactly 184 remain, producing 20 H. P is odd, so Q owns all four two-power cyclotomics and has 11 per mod-16 class; Q also has 16 per mod-11 class. Of the 184 head choices, 78 fail an individual mod-16 capacity. The remaining 106 induce nine H, all UNSAT with every mod-16 quota 11, every mod-11 quota 16, all five old tails, and pairwise H-conflicts. The two implementations report maximum 67 and 53 search nodes. A directly checked 176-tail positive relaxation meets these balances and old-anchor gcd restrictions when the extra H are omitted.

**P=20, Q=132.** P has four per mod-5 class; screened classes 2 and 4 each have 12 candidates. All `C(12,4)^2=245025` choices are enumerated: 141425 conflict and 103600 remain, producing 223 H. Q has 44 per mod-3 class and 12 per mod-11 class. Of the 103600, none first fails mod-3 capacity, 97146 fail mod-11 capacity, and the remaining 6454 induce 69 H. Every H is UNSAT in the relaxed two-quota selection `(3,0,44),(11,2,12)` with anchors 0,13. Producer and complement/set replay have maximum 523 nodes and use the same slack rule. A 50-tail positive relaxation meets those two quotas and old-anchor conditions when extra partial-head gcds are omitted. A prior differently ordered replay timed out at 35 seconds, with no verdict; only the pinned v2 completed replay is used.

**P=44, Q=60.** P has four per mod-11 class and uses gcd 240 by §7. Screened classes 1 and 2 each have 12 candidates, so `C(12,4)^2=245025` choices: 141425 conflict, 103600 remain, producing 195 H after adjoining 240. Q has 20 per mod-3 class and 12 per mod-5 class. None of the 103600 first fails mod-3 capacity; 43562 fail mod-5 capacity, leaving 60038 choices inducing 161 H. For every H, the relaxed two-quota selection `(3,0,20),(5,1,12)` with old anchors 0,1 is UNSAT. Maximum search size is 8559 nodes in both same-slack representations. A checked 21-tail positive relaxation meets those quotas and old-anchor restrictions after the extra H are dropped.

**P=24, Q=110.** The T2 parity deduction in §3 makes the eight P-heads in mod-3 class 1 consist of four even and four odd. The old-anchor screen has 12 of each parity there, so the complete partition has `C(12,4)^2=245025` choices: 239696 conflict, 5329 remain and induce 45 H. Q has 22 per mod-5 class and ten per mod-11 class. None first fails mod-5 capacity, 128 fail mod-11 capacity, and the remaining 5201 induce 43 H. Every H is UNSAT for relaxed quotas `(5,0,22),(11,2,10)` with old anchors 0,13. Maximum search size is 863 nodes in both same-slack representations. A checked 26-tail positive relaxation satisfies these quotas and old-anchor restrictions with extra partial-head gcds removed.

## 9. The two T2-dependent high-fibre branches

**P=22, Q=120.** From §3(ii), P has one even and one odd in each mod-11 class; Q has common mod-16 counts a on even classes and b on odd classes with `a+b=15`. The old-anchor Q screen has no residue `4 mod 6`, so every Q-element equal to 1 modulo 3 is odd. Q has exactly 40 in that class; hence `8b>=40`, so `b>=5`. Old tail 0 forces `a>=1`; therefore `1<=a<=10` and `b=15-a`. By §7 P also uses gcd 240.

Screened mod-11 head classes 1 and 2 each have six even and six odd candidates. Choosing one of each in each class gives `6^4=1296` possibilities; 272 have a `G_Y` conflict, leaving 1024 and 37 H after adjoining 240. Of those 1024, 64 fail individual mod-3/mod-5 capacity, then 452 have no `a` in 1..10 compatible with individual mod-16 capacities. The remaining 508 choices produce 24 H and 139 distinct allowed `(H,a)` cases. Every case is UNSAT for all 16 mod-16 quotas (a in even classes, `15-a` in odd classes), the quotas `(3,1,40),(5,1,24)`, all old Y anchors, and all H-pair conflicts. Other prime classes are omitted, so this is a relaxation. Both implementations report maximum 755 nodes using the same slack rule.

Its positive control is deliberately weaker: 120 distinct residues satisfy all mod-16, mod-3, mod-5 balances and all five old anchors only after **all gcd constraints are removed**; the control contains old-head-forbidden gcd differences. It must not be characterized as a SAT witness for the original screen, tiling, or code.

**P=12, Q=220.** From §3(i), every mod-3 P class has two even and two odd heads. In class 1 the old-anchor screen has 12 even and 12 odd candidates, so there are `C(12,2)^2=4356` choices before restrictions. P owns exactly two of the four two-power factors; one is `Phi_2` and the other is `Phi_(2^s)` for exactly one `s in {2,3,4}`. T2 and `Phi_3` give `Phi_(3*2^s)` in P, and their product is `1+X^(3*2^(s-1))`. Applying the mod-3 decomposition in §3, the polynomial of the selected class-1 heads in `u=(x-1)/3` has equal folded counts in residues r and `r+2^(s-1)` modulo `2^s`.

The complete partial-head partition is:

    s    G_Y conflicts    fail high-bit balance    valid choices    distinct H
    2       2592                 1508                   256              6
    3       2592                 1620                   144             10
    4       2592                 1664                   100             35

Q has 44 per mod-5 class and 20 per mod-11 class. The two-quota relaxation `(5,0,44),(11,2,20)` with anchors 0,13 excludes all 256 valid choices at s=2, all 144 at s=3, and 84 of the 100 at s=4. **The other 16 s=4 choices, inducing six H, really survive this relaxation.** For example, the pinned producer explicitly checks this 64-tail witness for `H={3,4,5,8,11,16,20,24,44,80,88,165}`:

    [0,13,50,60,110,120,170,180,211,240,277,290,300,343,350,360,
     410,541,600,607,660,673,720,770,780,830,840,871,890,900,960,
     1003,1010,1020,1070,1130,1201,1260,1267,1320,1333,1370,1380,
     1440,1490,1500,1531,1550,1560,1597,1610,1620,1680,1730,1790,
     1861,1920,1927,1980,2030,2257,2323,2521,2587].

It meets both quotas and the stated H/old-anchor compatibility, but is not claimed to meet the additional mod-8 balances or to tile.

For s=4, Q owns `Phi_4,Phi_8`, with product `1+X^2+X^4+X^6`. Thus its folded mod-8 counts are a on every even class and b on every odd class, `a+b=55`; old tails 0 and 1 give `1<=a<=54`. Across the six genuinely residual H, individual capacities leave 146 `(H,a)` cases. For each, the exact relaxation retains all eight mod-8 quotas, `(5,0,44),(11,2,20)`, all old Y, and pairwise H-conflicts. Both implementations report UNSAT in all 146 cases, maximum 5843 nodes using the same slack criterion. This is what disposes of the residual, not the two-quota test.

Subject to verification of the written reductions, the named T2 import, and the exact finite claims, §§6–9 exhaust (2). This would yield the stated even-Q contradiction, and no stronger conclusion.

## 10. Exact finite evidence, reproducibility, and limitations

All paths below are relative to this packet's owner directory. SHA-256 values pin the exact source bytes and JSON certificate. The stated counts are the outcomes previously recorded for those sources; this packet does not purport to rerun them. The checker processes integer residues only; no floating-point arithmetic, native solver, hidden no-good oracle, or timeout verdict is part of the conclusion. The primary program and separate replay are not a configured-family cross-review. An independent reviewer must check source, exhaustiveness, actual outcomes, and theorem hypotheses before adoption.

| Input / checker | SHA-256 | LF / bytes | Exact reported purpose |
|---|---|---:|---|
| `frontier-20261028-2640-even-tail-cover-v1.json` | `791016f119addb8367e729d803da53e8eb2ea4d1ed393ecbce9bfa830bbff758` | 1 / 3689 | 266-clique partition of all 658 Q-screen points and eight P pairs |
| `frontier-20261028-2640-even-tail-cover-generator.py` | `70fab0f6f5738225c1936976ff79c9cb8a36cf741ab325de69df73a4d2c2bcb8` | 29 / 1398 | deterministic exact clique-cover construction |
| `frontier-20261028-2640-even-tail-cover-check.py` | `bc0881e5aae25837c857bda4b9434c708f0246ed0a9f1fe6159ff4385eddadba` | 38 / 1849 | independent coverage, clique, P matching and divisor sieve |
| `frontier-20261028-seven-head-symbolic-check.py` | `5a99d1a528228ddbb6165dca04e80a4d41ef9f4b7faf1359409d51adcc45027d` | 59 / 2567 | finite symbolic controls for §2; written proof is general |
| `frontier-20261028-three-times-power-two-check.py` | `31c717ad1d93d77a41f171b4a5f75553ee3636ce69b10310e864771a7ca1853c` | 25 / 1007 | finite coefficient controls for §3(i), not T2 verification |
| `frontier-20261028-p22-cyclotomic-check.py` | `5efba57fecd33b121e10f94b815077b7f389b3cb73642be0202ea55c844e3be1` | 19 / 751 | finite identity/separation controls for §3(ii) |
| `frontier-20261028-2640-even-p10-check.py` | `f57009251811683d4d038f42fb8d1cbb486b844444a950dfb993f7f03373ab67` | 69 / 3787 | P10 partition and tail searches |
| `frontier-20261028-2640-even-p10-replay.py` | `76e146cf3ce2efbcf6134f682b78c061dc01dc6df152c5126ba98074d19999a9` | 55 / 2630 | P10 complement/set replay |
| `frontier-20261028-2640-even-p15-check.py` | `2e9b0c5eab4c88138cee387391938fd5b1b5858b4cd9401af25cd7a71a46577e` | 64 / 3970 | P15 partition and tail searches |
| `frontier-20261028-2640-even-p15-replay.py` | `d53c108c091cbbc5040bba855f622e3c984cbf9935e85a50e280ba6a1b2ca6f8` | 54 / 2586 | P15 set replay |
| `frontier-20261028-2640-even-p20-check.py` | `2da9f318c8fbc18e28e896bc9c3b845cfc09f66ecde050858ebfe3889c657e44` | 66 / 3424 | P20 partition and tail searches |
| `frontier-20261028-2640-even-p20-replay-v2.py` | `1952802a81e18f1be08f5ebbf67be42c20af9ef86cff39cb4aef3ba8eed1ebb6` | 56 / 2763 | P20 completed complement/set replay |
| `frontier-20261028-2640-even-forced-240-check.py` | `8529821909feeb14a11638eaff93450e745e62c6651990997292b072a01d359f` | 42 / 2067 | forced-240 head relaxation |
| `frontier-20261028-2640-even-forced-240-replay.py` | `310e484581c16e9e36807a4f425a4f448867b19a10bd805658c534873bce10d4` | 27 / 1427 | independent set-state head replay |
| `frontier-20261028-2640-even-p22-check.py` | `721abc668e2782ff0f335773667389d88538ebe423df1310c776e32762e5a9d4` | 83 / 4473 | P22 parity/fibre partition and tail searches |
| `frontier-20261028-2640-even-p22-replay.py` | `fa573ee9ee2e1916ee6f60f0cf44d52becc5b3e363ff5e764ddba5ed6a16009d` | 60 / 3204 | P22 set replay |
| `frontier-20261028-2640-even-p24-check.py` | `dfd54eee2cfd0fcfdf923836ab92462318a38b38ce5b8b135b13a6dcae8ad998` | 65 / 3363 | P24 partition and tail searches |
| `frontier-20261028-2640-even-p24-replay.py` | `55734a77419fa53035d549a71d1096d31eba0ced0f7ce7dbf2894cd3f1b8c4b8` | 55 / 2721 | P24 complement/set replay |
| `frontier-20261028-2640-even-p30-p33-check.py` | `b1a4c25a860d4ecd14dbd58c3daa4df9de2c90e8a6c3ef45e3e711b59f0ff6c8` | 29 / 1492 | head screens, blocker table and all 256 T-subsets |
| `frontier-20261028-2640-even-p40-check-v2.py` | `66ade09cb0653daf1bd97a686571bc81ed11e34f2552e0f4d209f846c572d463` | 66 / 3865 | corrected P40 forced classes and tail search |
| `frontier-20261028-2640-even-p40-replay-v2.py` | `983e4c73b8d3aa400aab31fd9ab0495b56041580b1a885610641a7a044a1dd32` | 35 / 1689 | P40 completed set replay |
| `frontier-20261028-2640-even-p44-check.py` | `31bee4b66dcd0d0d15f2c1bf8205325054cbaf4dd34bc9e18f50c73d87a5cc40` | 65 / 3306 | P44 partition and tail searches |
| `frontier-20261028-2640-even-p44-replay.py` | `74ada7718954db46d77b0e6c4c628a18c3db3e0e351c9cbf109294f43f99cf67` | 55 / 2701 | P44 complement/set replay |
| `frontier-20261028-2640-even-p55-check.py` | `6669c59a99f3043c33ef3fb8349acb4a0d76deef0ce2fea050d9910009461386` | 14 / 718 | P55 explicit four-pair matching |
| `frontier-20261028-2640-even-p88-check.py` | `4b4967c40f6b7aa57cf66280a9864de130f961c89b89b666fc2a42193c74ad5c` | 53 / 3161 | P88 forced classes and 12870 slot seeds |
| `frontier-20261028-2640-even-p88-replay.py` | `ee25a2398462eab2875cc636e18dc11e68d09f23614f423d6fc657c99d52a798` | 42 / 2166 | P88 head subset and complement-seed replay |
| `frontier-20261028-2640-even-p12-check.py` | `57b056b2cf746c0a230207fb14fc23f6ad8bd423be0a8bc69a5111dab472e536` | 84 / 4679 | P12 allocation partition and residual fibre searches |
| `frontier-20261028-2640-even-p12-replay.py` | `c12f872da277deedddade717a712075f2d7979452f0f4c79908e3eb289841934` | 68 / 3708 | P12 complement/set replay |

The cover certificate can also be regenerated from the following entirely specified finite rule, without using any omitted proof packet. Let sorted Q-screen residues be `q_0,...,q_(N-1)`, and make a graph with an edge iff their difference gcd is in `G_A`. Begin with no cliques and all vertices unused. For each unused vertex i, let `valid_i` be the ordered list of existing cliques all of whose members are its graph neighbors. Choose i maximizing the lexicographic score `(number_of_cliques - len(valid_i), N-1-degree(i), -i)`; this fixes ties uniquely. If `valid_i` is nonempty, add i to a largest valid clique, breaking a size tie by the earliest created clique. Otherwise start a new singleton clique. Remove i from the unused set and continue. The exact reported output is N=658 and 266 cliques; the independently pinned checker verifies the actual certificate directly rather than trusting the generator.

**Review gates:** verify (1) same-D multi-b border directness/coverage and anchor collisions; (2) page-identified T2 hypotheses and the polynomial deductions; (3) that all 21 raw divisors and all 12 survivors are covered; (4) exact code-level search completeness, anchor handling, seed/partial-head coverage, and all pins/counts, including the genuine P12 SAT residual; and (5) no stronger claim than the conditional even-tail result. An unsuccessful or timed-out replay must remain UNKNOWN. Until these gates pass, this entire packet is unreviewed. Odd-Q order 2640 and the unrestricted original question remain OPEN.

**END OF SELF-CONTAINED ORDER-2640 EVEN-TAIL REVIEW PACKET.**
