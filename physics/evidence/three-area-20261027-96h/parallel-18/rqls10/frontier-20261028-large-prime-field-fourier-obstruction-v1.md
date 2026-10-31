# A large-prime field obstruction for Fourier-product transversals

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:31:34 PDT 2026**. This is an elementary all-variable theorem for infinitely many even orders and a restricted entry field, not an unrestricted even-order no-go.

## Theorem

Let `n=m p`, with p prime and `1<=m<p`. Let F be a conjugation-stable subfield of C for which `Phi_p` is irreducible over F. For ANY complex Hadamard K of order n with entries in F, any source-row permutation, and any column permutation, its ordinary cyclic Fourier-product QLS has no orthogonal transversal. Repeated rays are allowed.

More strongly, no `m+1` cells in distinct columns and distinct physical rows all congruent modulo m can be mutually orthogonal.

## Proof

Write `psi_(r,c)(t)=n^(-1/2) zeta_n^(rt) K_(t,c)`. Take two distinct same-residue physical rows r,s, so `s-r=m k` with k nonzero modulo p. For their distinct columns c,d, their Gram is

`0 = sum_(u=0)^(p-1) A_u zeta_p^(k u)`,

where

`A_u = sum_(j=0)^(m-1) conjugate(K_(u+j p,c)) K_(u+j p,d) in F`.

Since `zeta_p^k` has minimal polynomial `Phi_p=1+x+...+x^(p-1)` over F, all coefficients A_u are equal. K's ordinary column orthogonality gives `sum_u A_u=0`, so every A_u=0. Therefore, for every fixed u, the m-coordinate restrictions of all selected K columns are pairwise orthogonal and nonzero. There are at most m such vectors in C^m. Any transversal has p selected rows in each residue class modulo m and p>m, contradiction. No alphabet, source-order or maximal-ray assumption enters beyond F and K being Hadamard.

## Consequences and precise limits

- For ANY prime p>=3, at the even order n=2p, every Fourier-product K over any such F has no transversal. In particular every `BH(2p,q)` with `p` not dividing q is excluded, because `Q(zeta_q) ∩ Q(zeta_p)=Q` for coprime conductors. More generally this holds at `n=mp` whenever `m<p`.
- For p=5,m=2 this recovers the no-5-field order10 theorem, including the same-parity C² obstruction. It does NOT exclude all non-Butson matrices: a field containing a nontrivial subfield of Q(zeta_p) lies outside the irreducibility hypothesis, as do arbitrary complex entries.
- If coefficients of an affine unit-phase family lie in a conjugation-stable number field F0 with Phi_p irreducible, and the phases are algebraically independent over F0, the conjugation-stable rational function field in those unit phases preserves irreducibility. Thus such a family has no transversal at those generic phases; special algebraically dependent phases need separate treatment. No all-phase inference follows from this generic statement alone.

The written proof and the standard coprime-cyclotomic-field import need independent review. No claim is made about all even Fourier products, n with no prime factor larger than its cofactor, or unrestricted maximal 1RQLS10.
