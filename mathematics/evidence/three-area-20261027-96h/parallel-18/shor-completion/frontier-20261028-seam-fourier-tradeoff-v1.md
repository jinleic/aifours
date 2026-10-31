# Shor completion: prime-modulus head/tail balance and a new-prefix tradeoff

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:48:48 PDT 2026**.
**All-order written necessary condition; exact finite algebra checks. Not a complete code, a universal no-go, formal proof or novelty clearance.**

## 1. Exact same-object theorem

Let D be ANY finite UD factor-complete extension of the literal 16-word Shor code S, let its unique pure-a atom be a^n, let B be its ACTUAL one-b layer, and let N_out count B-atoms whose initial a-run modulo n is not in the original head set

    A={0,3,8,11}.

For each divisor d of n, let `R_a^(d)` and `C_a^(d)` count the SAME B-atoms whose head and tail exponents, respectively, are congruent to a modulo d. No independent head/tail profile or alternative completion is selected.

**Prime dichotomy.** For every prime p dividing n, either

    R_0^(p)=...=R_(p−1)^(p)=n/p,

or

    C_0^(p)=...=C_(p−1)^(p)=n/p.                         (P)

If the HEAD alternative holds, every atom in the `p−|A mod p|` residue classes not represented by A has a genuinely new head residue. Therefore

    N_out >= (p−|A mod p|) n/p.

Equivalently, if the actual N_out is LESS than that threshold, the TAIL alternative in(P) is forced. In particular:

| Prime dividing n | Old classes A mod p | Either this many outside-head atoms, OR tails exactly balanced mod p |
|---:|---|---:|
|3|{0,2}|n/3|
|5|{0,1,3}|2n/5|
|7|{0,1,3,4}|3n/7|
|11|{0,3,8}|8n/11|
|p>=13|four distinct classes|(p−4)n/p|

**Binary refinement.** For d=4 or8 dividing n, if N_out<n/2 then the actual suffix counts satisfy

    C_a^(d)=C_(a+d/2)^(d),  a=0,...,d/2−1.              (B)

The strict inequality is essential: when N_out=n/2 the head alternative may hold. Conditions(P)/(B) are necessary for every original completion, not sufficient for UD or completeness.

As a concrete conditional caller, if the actual order were1320 and `N_out<440`, then the SAME suffix distribution would be balanced modulo3,5 and11, and would obey both the order4 and order8 paired-class identities. In particular each mod11 tail class contains120 one-b atoms. This does NOT claim order1320, N_out<440 or an actual completion exists; n=1320 is not inferred as a divisor of all orders.

## 2. Exact actual path conservation implies cyclic convolution

The raw-word proof in `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**, establishes for each hypothetical finite complete D: (i) |B|=n; (ii) every finite one-b endpoint-path matrix is zero-one; and (iii) its number of entries is at most n. It uses actual nonnegative a^n padding and long guarded factor-completeness, not a mere formal factorization.

For every seam gamma, let N_gamma count ACTUAL ordered B-pairs with `tail(first)+head(second)==gamma mod n`. This is the entry sum of a length-two endpoint-path matrix, so N_gamma<=n. Every one of the n² ordered atom pairs has exactly one seam, giving `sum_gamma N_gamma=n²`. There are n seams, hence

    N_gamma=n for EVERY gamma in Z_n.                     (1)

This is the all-variable equality, not the insufficient two-boundary uniqueness alone. If R_i and C_j are actual head/tail multiplicities modulo n, counting the same pairs yields

    sum_(j mod n) C_j R_(gamma−j)=n  for EVERY gamma.      (2)

Both arrays are nonnegative integers and `sum_i R_i=sum_j C_j=n`. This is a NECESSARY convolution of the one shared B, not a claim that arbitrary solutions can be paired into a code.

## 3. Proof of the prime dichotomy

Let p divide n and let zeta be a primitive p-th root. Define actual integer polynomials

    R(X)=sum_(i=0..n−1) R_i X^i,
    C(X)=sum_(j=0..n−1) C_j X^j.

Multiply (2) by zeta^gamma and sum all gamma. Because zeta^n=1 and zeta!=1,

    R(zeta) C(zeta)=n sum_(gamma=0..n−1) zeta^gamma=0.

Thus at least one of these two complex numbers is zero. Grouping actual counts modulo p replaces R by the integer polynomial `R_p(X)=sum_(a=0..p−1) R_a^(p) X^a`, without changing its value at zeta; similarly for C.

`Phi_p(X)=1+X+...+X^(p−1)` is irreducible over Q. For example, `Phi_p(1+X)=((1+X)^p−1)/X` is Eisenstein at p: its leading coefficient is1, every other coefficient is divisible by p, and its constant is p, not p². If R_p(zeta)=0, its degree is at most p−1, so `R_p=t Phi_p` for a rational t. Its integer coefficients give t integer and all p head counts equal. Their sum n makes each n/p. The alternative for C is identical. This proves(P) for EVERY prime divisor, including p=2, with no selected n or root approximation.

If head counts are uniform, each of the p−|A mod p| classes not hit by A contains exactly n/p actual atoms. Their head residues modulo n cannot belong to A, so all are counted by N_out. This proves the tradeoff and every prime-table entry. It requires n divisible by p; no claim about primes not dividing n is made.

## 4. Paired 2-power tail balances

Let d=2^k divide n. For primitive d-th zeta, the same calculation gives R(zeta)C(zeta)=0. Grouping counts modulo d, the irreducible polynomial is

    Phi_d(X)=X^(d/2)+1.

A degree<d polynomial vanishes at zeta iff its coefficients in the paired classes a and a+d/2 are equal, for EVERY a<d/2. Thus either all paired HEAD counts balance or all paired TAIL counts balance; the alternative is one whole distribution, not an independently chosen side for each pair.

For d=4, the old A occupies residue classes0 and3. If heads satisfy `R_0=R_2` and `R_1=R_3`, the two classes1,2 together contain n/2 atoms and neither is an old A head class; thus `N_out>=n/2`. For d=8, A occupies only classes0 and3 in the lower half. Head pair-balance makes the upper four classes contain n/2 atoms, all outside A. Hence `N_out<n/2` forces the corresponding TAIL-pair balance for d=4 and independently for d=8 whenever each divides n. This proves(B) without assuming p2 or p3 order conditions for the original problem.

The exact cyclotomic irreducibility used here is standard and follows directly by applying Eisenstein at2 to `(X+1)^(d/2)+1`. It is an ordinary named algebraic fact, not numerical Fourier evaluation.

## 5. Simultaneity and limits of the balances

At a fixed actual D, (P) holds at EVERY prime divisor, and (B) at each applicable binary divisor, for the SAME head/tail arrays and SAME n. The per-prime alternatives need not choose the same side. The tradeoff yields simultaneous TAIL balances when a common N_out upper hypothesis excludes each head alternative; it does NOT show such an upper hypothesis or an actual D exists.

Even multiple prime marginal balances do NOT by themselves imply full CRT-uniformity. For example, on Z_15 start with all tail counts1 and change the counts at residues0,1 by +1 and at6,10 by −1. Each mod3 class still sums5 and each mod5 class sums3, but the15 individual counts are not all equal. This is only a synthetic histogram showing a logical limit; it is not claimed realizable by a Shor one-b layer or a completion.

The original question still requires one actual full one-b incidence, all-length path uniqueness/conservation, all multi-b atoms and complete Boolean-word factor coverage. No one of the prime balances is a converse. In particular the previously exhibited full-size two-boundary false layer violates (1); its SAT status cannot be used as a solution here.

## 6. Actual exact checks and unresolved bounded search

Executed after writing its source:

    python3 -B frontier-20261028-convolution-dichotomy-check.py

The independent integer-profile checker exhausted all35²=1225 pairs of n=4 nonnegative profiles and all462²=213444 pairs at n=6. It found respectively101 and1751 conserving pairs, and EVERY conserving pair satisfied the applicable prime/order4 folded dichotomies. It also checked a synthetic n=12 rectangular pair layer's144 two-path keys and equal seam counts; a deliberate degree mutation was rejected. That synthetic rectangle is NOT a Shor extension. These checks do not replace the all-prime proof.

`frontier-20261028-convolution-dichotomy-check.py`: SHA256 **283340b472fb76dc5ca9e621c44f57b195cfd14184dee6cd17b68b3b3c539fbc**,78 LF /2616 B, native pin Wed Oct28 17:48:48 PDT.

Two separate n=32 SAT attempts imposing full two-path conservation were also bounded. The direct integer-convolution formulation returned **UNKNOWN (20-second solver timeout)**; an equivalent order-2-power Fourier-disjunction formulation returned **UNKNOWN (30-second solver timeout)**. Neither is SAT, UNSAT, a proof certificate or evidence of global noncompletion. No unobserved solve is implied.

## 7. Original-target and novelty boundaries

This is an all-order head/tail tradeoff for every genuine finite completion, not an original witness or unrestricted no-go. The actual missing bridge is whether the required balances, high outside-head count alternatives and raw all-list/multi-b constraints can coexist for ONE completion. No assumption that the outside layer is small, that prime marginals combine into a joint flat distribution, or that a profile is realized has been supplied.

No historical held output is accepted merely by changed process direction. The named raw one-b argument is independently reproduced in the preceding written candidate; standard cyclotomic irreducibility is explicitly named/proved above. Mathematical review, formal/kernel/human/cross-family verification and novelty remain outstanding.

**END OF SEAM-FOURIER TRADEOFF CANDIDATE.**
