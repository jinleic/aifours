# Shor completion: exact b-run border factorization and a six-head reduction

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:31:31 PDT 2026**.
**All-order written necessary conditions plus a bounded exact-cover experiment; not a full completion/noncompletion or novelty claim.**

## 1. Same-code border factorization

Let D be ANY finite UD factor-complete extension of the literal Shor code, and a^n its unique actual pure-a atom. The literal old code includes b, the four words a^i b for

    A={0,3,8,11},

and the five words b a^j for

    Y={0,1,7,13,14}.

Define residue sets from ACTUAL D-atoms, permitting multiple consecutive b's:

    P={i mod n : a^i b^k in D for some k>=1},
    Q={j mod n : b^l a^j in D for some l>=1}.              (1)

Then A⊆P, Y⊆Q and **P+Q is a direct tiling of Z_n**: every residue has exactly one representation p+q. In particular

    n=|P||Q|,  |P|>=5,  |Q|>=6.                           (2)

These P/Q are NOT merely the zero-tail/zero-head subsets of the one-b layer: atoms with several consecutive b's must be included. No array of residues is substituted for actual D words.

The general border-factorization theorem is a classical prior result, e.g. Restivo–Salemi–Sportelli as stated in [Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*, Theorem1.1](https://arxiv.org/html/2301.13566v1). Sections2–3 independently reconstruct exactly the finite/complete/b-contained case used here; this is not a new attribution or a priority claim.

## 2. Directness from exact raw word equalities

Take two representations of the same residue, using actual representatives

    u_t=a^(i_t) b^(k_t) in D,  v_t=b^(l_t) a^(j_t) in D,  t=1,2,
    i_1+j_1 == i_2+j_2 (mod n).

Choose L>=l_1,l_2, K>=k_1,k_2, and a POSITIVE common G at least each `i_t+j_t` in their common residue modulo n. Then the following are two actual D-word lists for the SAME raw word `b^L a^G b^K`:

    b^(L−l_t), v_t, (a^n)^((G−i_t−j_t)/n), u_t, b^(K−k_t),

where powers of b denote repeated copies of the ACTUAL b atom. Every count is nonnegative.

If u_t starts with no a's, it is a pure b-word and UD forces u_t=b; otherwise it starts with a and ends with b. If v_t ends with no a's, UD forces v_t=b; otherwise it starts with b and ends with a. These two non-b word types are distinct and occur on opposite sides of the positive central a-run. Hence equality of the two actual atom lists forces the SAME chosen v and u, and therefore the same Q/P residue pair. UD rules out two distinct representations. This proves directness without treating a multib atom as a one-b atom.

## 3. Coverage from guarded factors, and the old-anchor lower bounds

Let L be the maximum D-atom length. For ANY gamma modulo n choose g>L in that residue class and consider the raw factor `b^L a^g b^L`. Factor-completeness embeds it in some D-word concatenation.

The atom containing the LAST b of the left guard cannot reach beyond that guard on the left, nor can it cross the longer-than-L middle a-gap to a right b. It is therefore an ACTUAL `b^l a^j` atom. Similarly the atom containing the FIRST b of the right guard is an ACTUAL `a^i b^k` atom. All codewords between these two are pure-a, hence a^n. Consequently `g==j+i mod n`, so every gamma lies in Q+P. Together with directness, P+Q tiles and |P||Q|=n.

The old-head set A and old-tail set Y already rule out either border remaining at its bare anchor size. If P=A, any direct complement Q containing Y would have to cover6, but each of its only possible Q-elements `6,3,−2,−5` collides with existing0 or1 via

    6+3=1+8;  3+0=0+3;  −2+3=1+0;  −5+8=0+3.

If Q=Y, any direct complement P containing A would have to cover2, but each of its only possible P-elements `2,1,−5,−11,−12` collides with an existing head:

    2+1=3+0; 1+0=0+1; −5+13=8+0;
    −11+14=3+0; −12+13=0+1.

All inequalities are valid modulo every feasible n>=26. Hence `|P|>=5, |Q|>=6`. These are necessary border sizes, not existence of the tiling or of D.

## 4. Any prime divisor appearing on only one side forces balance

For a prime p dividing n, the tiling identity at a primitive p-th root gives `P(zeta)Q(zeta)=0`, using the 0/1 characteristic polynomials of the actual residue SETS. If p does not divide |Q|, then Q(zeta) cannot vanish: otherwise Phi_p divides the integral polynomial Q and evaluation at1 would give p||Q|. Thus P(zeta)=0, so P has equal counts in every residue class modulo p. Conversely, if p does not divide |P|, Q is uniform modulo p. Standard Phi_p irreducibility is the only named algebraic fact here; no selected factorization or real relaxation is used.

Therefore, when v_p(n)=1, the prime p lies on exactly one of the two cardinalities and the corresponding border is uniform modulo p. Old anchor multiplicities supply explicit minimum sizes. For example:

- If v_5(n)=1 and p=5 divides |P|, the heads3 and8 are in the same mod5 class; P needs at least2 elements in EACH class, so |P|>=10.
- If v_11(n)=1 and p=11 divides |P|, heads0 and11 share a class; |P|>=22.
- If v_3(n)=1 and p=3 divides |Q|, tails1,7,13 share a class; |Q|>=9.
- If v_7(n)=1 and p=7 divides |Q|, tails0,7,14 share a class; |Q|>=21.
- If v_13(n)=1 and p=13 divides |Q|, at least two old tails share a class; |Q|>=26.

These are quantified alternatives about the SAME direct P/Q factorization. They do not establish the stronger historical n-divisibility result or select which side receives any prime.

## 5. Exhaustive parametrization of the six-head branch in a stated valuation range

Assume **only in this section** that `|P|=6`, `v_3(n)=1`, and `v_2(n)` is2 or3. Then |Q|=n/6 is coprime to3, so §4 forces P uniform mod3. A has two residues0 and two residues2 modulo3. Its exactly two new heads must BOTH be1 modulo3.

For each 2-power order2,4,...,2^v2(n), at least one of P,Q vanishes at a primitive root. Each corresponding cyclotomic polynomial evaluates to2 at1. The total2-adic valuation of `|P||Q|=n` shows that EXACTLY one of these factors belongs to P. It cannot be Phi_4: A has two heads0 mod4 and two heads3 mod4, so paired balance would require two NEW heads in EACH of classes2 and1, four in total. It cannot be Phi_8 for the same reason, now requiring two new heads in EACH of classes4 and7. Hence Phi_2|P and P has three even and three odd elements. The old A already has two even and two odd heads, so the two new heads have opposite parity.

Combining the mod3 and parity facts, any SUCH P is exactly

    P=A union {u,v},   {u mod6,v mod6}={1,4}.              (3)

This is an exact, global parametrization only for the stated valuation branch; it is not claimed for v_2(n)>=4, v_3(n)!=1, or |P| other than6.

## 6. Actual bounded search and honest frontier

The standalone exact-cover search `frontier-20261028-six-head-border-search.py` enumerates all P in(3), rejects overlap of the mandatory five Q-translates, and recursively covers the full n-cycle by disjoint P-translates, with honest node/time caps. A returned tiling is directly rechecked. This is a finite BORDER search, not a full code/UD/completeness solver.

Actual command/result:

    python3 -B frontier-20261028-six-head-border-search.py 660 20 5000
    tested_pairs=12100; anchor_collisions=1284; fully_exhausted=10816;
    capped=0; DFS nodes=135407; status=EXHAUSTED; no factorization.

Thus the exact program found NO size-six P/Q border factorization at n=660 within the mathematically proved valuation/size parametrization. This does not improve the previously recorded stronger actual-order floor, and the program has not yet received an independent complete-source review or proof certificate.

At n=1320 the bounded60-second run visited15836 of48400 parametrized P-pairs:1886 had anchor collisions,13949 were fully exhausted, ONE was node/time-capped; status **INCOMPLETE**, no factorization found in that incomplete scan. This is NOT an n=1320 exclusion, and no identity of the capped case was saved by v1. The indexable v2 search is intended to continue the remaining cases; its later outputs are not asserted by this packet.

Native source pins at Wed Oct28 18:31:31 PDT:

| File | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-six-head-border-search.py` | 6a30cc85559191d9b7a4a48379cdbb356c32f1371f09789abb6236551e055d00 |86 /3333 |
| `frontier-20261028-six-head-border-search-v2.py` | 48e8bfa966470d834c20850ae9294c57a2a1de54fa5ab909047d22a56b97ef7d |81 /3450 |

## 7. Original gap and source/assurance limits

Even a genuine P/Q direct factorization is a NECESSARY border condition only; it supplies neither the full n-element one-b layer nor all-list UD, multib compatibility or factor-completeness. Conversely failure of the |P|=6 branch does not exclude all possible border sizes. A completion-or-unrestricted-no-go remains unsolved.

The classical border theorem is explicitly prior, and the current exact source read is not an exhaustive novelty or world-status search. Prior historical process records remain historical, not a proof of or against these deductions. No peer, human, formal/kernel or independent-model-family gate has been passed.

**END OF BORDER-FACTORIZATION AND SIX-HEAD REDUCTION.**
