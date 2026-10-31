# Shor completion: two distinct cyclotomic spectral constraints and an exact order-32 exclusion

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:53:55 PDT 2026**.
**All-order written necessary conditions, with independently executed finite checks; not a full completion/no-go or a novelty claim.**

## 1. Original-object conclusions

Let D be ANY finite UD factor-complete extension of the actual Shor code, a^n its unique pure-a atom, and B its SAME actual one-b layer. Write `R_i`/`C_j` for the counts of B-atoms by initial/final a-run residue modulo n. Thus `sum R=sum C=n`, and the independently reconstructed SAME-layer conservation gives `C*R=n` at every cyclic seam.

**Theorem A.** Neither R nor C can have any cyclic period d<=15. Equivalently, if a divisor d of n is at most15, each of R and C has a nonzero Fourier coefficient at some character whose order does NOT divide d. In fact, for every such d there are TWO DISTINCT divisors `t_R,t_C` of n, neither dividing d, such that

    Phi_(t_R) divides R(X),   Phi_(t_R) does NOT divide C(X),
    Phi_(t_C) divides C(X),   Phi_(t_C) does NOT divide R(X).

The conclusion refers to the actual integer marginal polynomials of the SAME B. The distinct divisor labels may depend on d; the theorem does not assert a particular prime or factorization.

**Corollaries.** No prime n is possible. For any prime p<=13, n=p² is impossible. These are separately derived elementary necessary exclusions, not new records against the prior stronger order restriction.

**Theorem B.** A finite UD factor-complete Shor extension with pure-a order n=32 is impossible already at the two-path SEAM-CONSERVATION level. This holds even though `S union {a^32}` is itself UD, and even though a 32-pair layer satisfying all two-boundary uniqueness constraints exists. The exclusion is a self-contained analytic explanation of that finite case, not a substitute for the original all-n question. Two earlier SMT searches timed out; neither timeout is the proof.

The original n=32 exclusion is weaker than the existing recorded baseline for possible completion orders. The value here is the two-sided actual-marginal mechanism and a fully checked separation of pair uniqueness from seam conservation, not a claim of new best order bounds or priority.

## 2. Old atoms force both marginals to be nonperiodic below16

The 16 old words give these lower bounds on actual residue counts, with all positions below n because n>=26 by the elementary raw-ambiguity argument in the predecessor:

    heads:  R_0>=5, R_3>=4, R_8>=4, R_11>=3;
    tails:  C_0>=4, C_1>=2, C_2>=3, C_4>=2,
            C_6>=2, C_7>=1, C_13>=1, C_14>=1.

If a nonnegative integer n-vector v of total n is d-periodic for d|n, one period has sum d. If specified positions i require `v_i>=w_i`, their PERIODIC lower bound is the sum over residues modulo d of the largest w_i in that residue. For the actual head and tail anchors this gives:

| d |1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| head lower per period |5|9|9|9|12|16|16|9|16|16|13|16|16|16|16|
| tail lower per period |4|6|9|10|12|11|13|15|15|15|15|14|14|15|16|

EVERY entry exceeds its column d. Therefore neither actual marginal can be d-periodic for any divisor d<=15. These are actual one-b multiplicities, not independently chosen hypothetical marginal values.

## 3. From nonperiodicity to distinct cyclotomic factors

Let `R(X)=sum_(i=0..n−1)R_i X^i`, and similarly C. Seam conservation gives

    R(zeta)C(zeta)=0

at EVERY nontrivial n-th root of unity zeta. For any d|n, a cyclic vector is d-periodic iff all its Fourier coefficients at characters whose order does not divide d vanish: shift by d multiplies each Fourier character by zeta^d, and Fourier inversion gives the converse.

Since R is not d-periodic, there is a character of order t_C not dividing d at which R is nonzero; seam conservation forces C to vanish. Since C is not d-periodic, there is an order t_R not dividing d at which C is nonzero and R vanishes. Both divide n and exceed1. As R,C have INTEGER coefficients, vanishing at one primitive t-th root is equivalent to divisibility by the irreducible cyclotomic polynomial Phi_t. If t_R=t_C, R would have to be both zero and nonzero on primitive roots of the same irreducible polynomial, impossible. The two divisors are therefore distinct, proving Theorem A.

A consequence often useful for bookkeeping is: the least period of either actual marginal is at least16. Also the least common multiple of the orders of the nontrivial cyclotomic factors of EACH marginal is at least16; otherwise conservation would force the opposite marginal to be periodic with a divisor at most15. These are LCM statements: they do NOT assert that one individual factor has order>=16 or that any specified prime occurs.

For n prime, d=1 has only one nontrivial divisor, contradicting the distinct-divisor conclusion. For n=p² with p<=13, d=p has only the divisor p² outside d. Thus neither type can occur. n<26 is independently excluded by the raw old-word ambiguities; these corollaries do not claim novelty beyond existing stronger order restrictions.

## 4. Why n=32 fails even with the correct path conservation

Let n=32 and let zeta be a primitive32nd root. Conservation forces R(zeta)=0 OR C(zeta)=0. Since `Phi_32(X)=X^16+1`, the respective integer coefficient vector is16-periodic.

### Case 1: R is16-periodic

The first16 head counts sum16. The four old lower bounds already sum16, so they are exactly

    (R_0,R_3,R_8,R_11)=(5,4,4,3),  all other first-half counts0.

Write `P(X)=5+4X^3+4X^8+3X^11`; then `R(X)=(1+X^16)P(X)`. Its remainders modulo the four nontrivial 2-power cyclotomics up to16 are

    mod Phi_2: 2;
    mod Phi_4: 9−7X;
    mod Phi_8: 9+7X^3;
    mod Phi_16: 1+X^3.

All are nonzero of degree below the respective irreducible cyclotomic degree. Thus R is nonzero at EVERY nontrivial 16th root. Conservation forces C to vanish at all of them. Fourier inversion says the16 grouped counts `C_j+C_(j+16)` are each `32/16=2`, but the old words already give C_0>=4. Contradiction.

### Case 2: C is16-periodic

The first16 tail counts sum16 and the eight old lower bounds in §2 sum16, fixing

    Q(X)=4+2X+3X²+2X⁴+2X⁶+X⁷+X¹³+X¹⁴,
    C(X)=(1+X^16)Q(X).

The remainders of Q modulo Phi_2,Phi_4,Phi_8,Phi_16 are, respectively,

    8;  2X;  2+X−X³;
    4+2X+3X²+2X⁴−X⁵+X⁶+X⁷.

Each is nonzero. Thus C is nonzero at every nontrivial16th root and conservation forces grouped head counts `R_i+R_(i+16)` all equal2. This contradicts R_0>=5. The two cases exhaust the primitive32 root dichotomy, proving Theorem B.

This is a proof by actual one-b path conservation and old-word multiplicities. It does not claim the 32-pair two-boundary model itself is UD: the separately pinned `frontier-20261028-full-size-two-boundary-failure-v1.md` explicitly supplies its THREE-word ambiguity and shows its seam0 has44, not32, paths.

## 5. Actual finite checks and exact limits

- `python3 -B frontier-20261028-spectral-period-check.py` recomputed every table entry d=1..15 and each listed cyclotomic remainder using exact integers. A uniform16-count positive control had zero remainder at all four nontrivial 2-power factors.
- `python3 -B frontier-20261028-order32-spectral-check.py` used a small linear Z3 model for each fixed 16-periodic template plus exact seam convolution. With the required old opposite-marginal anchor, both branches returned `unsat`; after removing that anchor, both returned `sat`, and each returned positive-control profile was directly rechecked. This is a finite solver cross-check, NOT a separately certified UNSAT proof; the full proof is §4.
- Earlier full two-boundary+conservation n=32 searches returned **UNKNOWN** at20s and30s. The present analytic proof does not retroactively change those observed solver outputs or report them as UNSAT.

Native checker pins at Wed Oct28 17:53:55 PDT:

| File | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-spectral-period-check.py` | 5a8a3a89e797fc738c4823f34decb0264c98dcc139e314cb2a0b44f0db02142c |42 /1523 |
| `frontier-20261028-order32-spectral-check.py` | c88f2ebfa3415d71abc883c17a4dfe42e7e17b69b34255efba1e1d01de9841db |32 /1285 |

## 6. Remaining target and provenance

These restrictions apply to every actual finite completion but do not provide a completion, contradict all n, establish which cyclotomic factors actually occur, or replace full multi-b/list/factor-completeness obligations. The exact original Shor completion question remains open at this packet's scope. Prior archived findings remain historical and are not converted into accepted science by a clock change; the only imported caller is the separately reconstructed actual path conservation. Standard cyclotomic irreducibility and finite Fourier inversion are named elementary facts; no novelty, formal/kernel, human or independent-model acceptance is claimed.

**END OF SPECTRAL-PERIOD OBSTRUCTION CANDIDATE.**
