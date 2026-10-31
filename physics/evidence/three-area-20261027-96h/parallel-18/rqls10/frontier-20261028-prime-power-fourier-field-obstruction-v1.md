# Prime-power Fourier-product transversal field obstruction

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:21:45 PDT 2026**. This is a new all-prime-power dimensional result, partially addressing the even-order question, with no claim for unrestricted complex phases.

## Theorem

Let n=p^a>=2 for any prime p and integer a>=1. Let F be a conjugation-stable subfield of C such that `Phi_n` is irreducible over F. For ANY n×n complex Hadamard K with entries in F, the Fourier-product QLS

`psi_(r,c)(t)=zeta_n^(r t) K_(t,c)/sqrt(n)`

has NO transversal, even with repeated rays. In particular, by standard coprime-conductor cyclotomic disjointness, this excludes every `BH(p^a,q)` Fourier product when p∤q. For even n=2^a it also covers q=2q' with q' odd, since Q(zeta_(2q'))=Q(zeta_q').

## Proof

Set `m=n/p`. Suppose a transversal has column c_r in physical row r, r=0,...,n−1. Consider the cells in adjacent rows r and r+1, whose columns c,d are distinct. For each t, put `z_t=conj(K_(t,c)) K_(t,d)∈F`. Their physical orthogonality is

`P(zeta_n)=0`, where `P(x)=sum_(t=0)^(n-1) z_t x^t ∈ F[x]`.

Because Phi_n is irreducible over F, it divides P. For prime powers,

`Phi_n(x)=1+x^m+x^(2m)+...+x^((p-1)m)`.

Since deg(P)<n and deg(Phi_n)=n−m, the quotient has degree at most m−1. Comparing coefficients therefore yields

`z_(u+jm)=z_u` for every `0<=u<m`, `0<=j<p`.                  (1)

Equivalently, for each u,j the ratio `K_(u+jm,c)/K_(u,c)` is the SAME for columns c and d. Adjacent physical rows form a connected cycle (a path suffices), so applying (1) to every adjacent transversal pair makes that ratio independent of ALL n columns. Thus row u+jm of K is proportional to row u for any j!=0, contradicting the Hadamard row-orthogonality of two nonzero rows. No extra maximality or numerical hypothesis was used.

## Scope and even-order significance

For n=8 this gives a universal no-T result for every K over F with Phi8 irreducible, e.g. every BH(8,q) with q odd or `q=2*(odd)`, including BH(8,6). It does NOT cover arbitrary BH(8,8), general K fields containing the relevant cyclotomic subfields, n not a prime power, or general 1-RQLSs. A complete exact BH(8,8) bitvector/transversal search `frontier-20261028-n8-bh8-transversal-smt-v1.py` SHA **b1a7a4d13dda2d4b5e5e524a7a3b1a53058c607eb0a8eb38f0cea75a3496b5e1** returned UNKNOWN at 120 s; it gives no exclusion or witness. The n=8 general even-Fourier question remains open in this work.

If the entries of K are algebraic and a transversal exists, then its conjugation-stable number field F must contain a nontrivial subfield of Q(zeta_(p^a)), because a proper Galois subgroup of the cyclotomic extension fixes such a field inside F. In particular p ramifies in F. This is a necessary condition only; the odd-n example K=F_n is consistent because its field contains zeta_n. The proof and named standard field facts require independent review.
