# Premise ledger and mathematical bridge

Only the staged files in this directory were read. In particular the source for
Thas–Zagier below is a reader conversion, not its original PDF. The contract's
account of later work is background data; this visit cannot conduct a new
literature or novelty search. Novelty is unknown.

1. **Kantor (1987), imported, classification-dependent.** A non-Desarguesian
   finite flag-transitive projective plane of order n has n even,
   p=n²+n+1 prime, and the Frobenius/sharply flag-transitive alternative.
   Thas–Zagier Section 1 presents this as an amalgam of earlier results and
   explains the reduction using Kantor and the classification of finite simple
   groups. We do not independently prove that classification or the reduction.
2. **Thas–Zagier (2008), imported identification.** Proposition 2.1 and Theorem
   2.4 identify the remaining plane with the development of the additive
   difference set D=(F_p^*)^n=mu_(n+1), if it exists. The n=2,8 cases are
   classical; no other Desarguesian case is flag-regular in this way (Section 2,
   using earlier literature). Thus eliminating these D for n>8 addresses the
   intended geometric conjecture, rather than the defective printed graph form.
3. **Feit (1990), only the valid conditions, imported via Thas–Zagier.** For
   a putative non-Desarguesian plane, 8 divides n, and every positive divisor
   d of n satisfies d^(n+1)=1 (mod p). The divisor condition is quoted in
   Thas–Zagier Section 1, and 8|n in its appendix. The purported exclusion of
   powers of two and Ott's purported prime-power-order theorem are explicitly
   NOT used: the staged paper says their proofs have errors.
4. **Derived congruence, proved here.** The identity n³−1=(n−1)p gives
   n³=1 (mod p). For n>1 we have 1<n<p and n≠1 (mod p), so n has multiplicative
   order exactly 3. Applying the valid divisor condition to d=n gives
   3|(n+1). Combining n=2 (mod 3) with 8|n gives n=8 (mod 24).
5. **Base-two condition, stated by Thas–Zagier; elementary argument included.**
   If D is a planar difference set, there is exactly one x with x,x+1 in D.
   Inversion maps any such x to x^(-1), since (x+1)/x belongs to D too.
   Uniqueness forces x=x^(-1), so x=±1 in the odd-prime field. The value −1
   cannot occur, because x+1 would be zero. Hence x=1 and 2 belongs to D,
   i.e. 2^(n+1)=1 (mod p). This is only necessary, as n=24,90,512 illustrate.
6. **Published baseline, imported computational result.** Thas–Zagier's
   appendix lists the seven even base-two solutions below 5×10^9 and reports
   no new solutions on n=8 (mod 24) up to 2×10^11. This visit reproduces the
   former FULL interval in C before production; it does not rerun the entire
   latter baseline. Its below-2×10^11 exclusion is imported when combining
   the ranges.

## Exactly what the scan can establish

For every n in a completed arithmetic-class block, either a proper divisor
1<q<p of p is exhibited by the sieve algorithm, or the exact base-two power
is computed. A proper divisor proves p is composite. A residue other than 1
excludes a necessary condition without any primality assumption on p.
Any residue-1 candidate without a proper factor is a **survivor**; it cannot
be eliminated by probable-primality. It needs an explicit proper factor,
a failure of a valid divisor congruence, or another exact argument. An
unresolved survivor prevents exclusion of an interval containing it.

Only n=8 (mod 24) are scanned in the main range, justified by items 1–4.
All n outside that class are excluded analytically under the imported premises.
Combining an unbroken main-range scan [2×10^11,N) with item 6 would therefore
give the conditional computational bound: no non-Desarguesian flag-transitive
plane has order less than N. This does not prove the all-orders conjecture.

## Printed Cayley-graph defects, kept separate from the target

For the dihedral group of order 2p, edges from reflections cross between the
rotation subgroup and its other coset. Both parts have p vertices; degree
n+1<p leaves nonadjacent vertices in opposite parts. Every path between
opposite parts has odd length, so such a pair cannot be at distance 2 or less.
The printed diameter-two assertion is thus inconsistent with these definitions.
Also, allowing an arbitrary set of n+1 reflections does not supply the claimed
equivalence with **non-Desarguesian** flag-transitive planes: the standard Singer
construction for a classical plane gives a cyclic planar difference set and a
dihedral Cayley realization of its incidence graph, of diameter 3. The contract
points to Li (2005) for this. We have not read that paper in this visit and do
not use its graph wording as a premise for the computation.

## Arithmetic scope and Montgomery justification

The scanner accepts 2≤n<2^60, hence odd p=n²+n+1<2^121<2^127.
For R=2^128 and 0≤a,b<p, t=ab is retained as a FULL 256-bit product.
Let m=(t mod R)(−p^(-1)) mod R. Then t+mp is divisible by R and
0≤(t+mp)/R<p+p²/R<2p<R. A single subtraction therefore produces
the correct Montgomery product in [0,p). The sum of the high halves plus
the low-half carry cannot overflow 128 bits under these bounds. Within this
Montgomery reduction, only the multiplication used to find m is intentionally
truncated modulo R; Newton inversion separately works modulo R throughout.
The four 64×64 products used for a full product are widened before multiplying.
The sum of three middle 64-bit contributions fits 66 bits.

Seven Newton iterations starting with the inverse modulo 2 compute p^(-1)
modulo 2^128. Unsigned (−p) mod p equals (R−p) mod p=R mod p, the
Montgomery representation of 1. Squaring and conditional doubling implement
binary exponentiation; p<2^127 also makes doubling safe. Audit records convert
back using a final Montgomery multiplication by ordinary 1, so the stored
value is the COMPLETE ordinary residue, not a pass/fail flag.

This arithmetic argument explains the algorithm. It does not assert that
compiler output or the entire production execution has been independently
certified. Python integer checks certify only the explicitly recorded subsets.
