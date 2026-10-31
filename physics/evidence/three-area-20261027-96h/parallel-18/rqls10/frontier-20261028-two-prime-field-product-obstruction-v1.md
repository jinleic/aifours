# A uniform field obstruction for Fourier-product QLS of order 2p

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:04:18 PDT 2026**. This generalizes the order10 argument `frontier-20261028-no5-field-product-no-transversal-v1.md` SHA **69849d0dad81748b50771dea667176fb3818aa54fb728268340d2fbff064fc36**; it is not an unrestricted QLS no-go or a novelty claim.

## Theorem

Let p>=3 be prime. Let F⊆C be conjugation-stable and suppose `Phi_p(x)=1+x+...+x^(p-1)` is irreducible over F. Let K be any `2p×2p` complex Hadamard with entries in F. For the Fourier-product QLS

`psi_(r,c)(t)=zeta_(2p)^(r t) K_(t,c)/sqrt(2p)`,

no THREE pairwise orthogonal cells can occupy three distinct physical rows of the same parity and three distinct columns. In particular this QLS has no orthogonal transversal, including when rays repeat.

The standard coprime-conductor cyclotomic disjointness theorem implies the condition for `F=Q(zeta_q)` whenever p∤q. Consequently NO `BH(2p,q)` Fourier-product QLS has a transversal when p∤q.

## Proof

For orthogonal cells in distinct same-parity physical rows r,s and distinct columns c,d, put `Delta=s-r=2k mod 2p`, with k nonzero mod p. Set `z_t=conj(K_(t,c)) K_(t,d)∈F` and `w_u=z_u+z_(u+p)`, u=0,...,p−1. K-column orthogonality yields `sum_u w_u=0`, while physical orthogonality yields `sum_u zeta_p^(k u) w_u=0`. The p powers in the latter equation are a permutation of the p-th roots and their only F-linear relation is the all-ones relation, by irreducibility of Phi_p. Thus every w_u is equal, and its sum is zero: `z_(u+p)=-z_u` for every u.

Equivalently, with `h_c(u)=K_(u+p,c)/K_(u,c)`, one has `h_d(u)=-h_c(u)` for every u. Three orthogonal cells in distinct same-parity rows and columns c1,c2,c3 would imply `h_c2=h_c3=-h_c1` and `h_c3=-h_c2`, impossible because all entries of K have modulus1. Each transversal uses p>=3 same-parity rows, proving the corollary.

## Scope

This is a written field/linear-algebra proof with the named cyclotomic-disjointness import. It does not require a classification of BH matrices and imposes no maximality assumption. It does not cover p|q, reducible Phi_p, even composite p, or non-Fourier products. Independent review is required.
