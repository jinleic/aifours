# An infinite Paley-prime family has a rook orthogonality graph

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:55:02 PDT 2026**. This strengthens the elementary p=7 result `frontier-20261028-bjorck7-rook-graph-analytic-v1.md` SHA **7012b808b5b1648632cf5b6d1a8c29129ca23f3fc3417bc47e4adc0ffb971d2c** to every prime p congruent to 3 mod4 with p>=7. It is NOT a universal even-order no-go.

## Theorem

Let `p=4k-1` be prime, k>=2, let chi be the quadratic character of F_p, and choose a primitive pth root zeta. Set

`g = sum_(x != 0) chi(x) zeta^x`,  `a = [-(2k-1)+g]/(2k)`.

Let `K_p(t,c)=a` if `t-c` is a quadratic nonresidue and `1` otherwise. Then K_p is complex Hadamard. For EVERY permutation of its source rows, its cyclic-Fourier-product QLS has orthogonality graph exactly the p×p rook graph: two distinct cells are orthogonal if and only if they share a physical row or a physical column.

For EVERY positive m coprime to p and every local source-row permutation pi, the CRT-aligned order `p m` cyclic Fourier product based on `(pi K_p) tensor F_m` has NO orthogonal transversal, even if rays repeat. For even m this gives non-Butson examples in infinitely many even dimensions. The same tensor-incidence proof works with ANY classical Latin QLS of order m for p not dividing m, independently of CRT. Arbitrary source permutations mixing the two tensor factors are not covered.

## Paley matrix and character facts

Since p=3 mod4, `chi(-1)=-1`. The standard Gauss-sum identities, included here for clarity, are `conjugate(g)=-g`, `g conjugate(g)=p`, and `sigma_h(g)=chi(h)g` for nonzero h; hence `g²=-p`. For example, the norm identity follows by setting x=h y in the double sum and using `sum_(y != 0) zeta^((h-1)y)=p-1` at h=1 and -1 otherwise. Therefore `|a|=1` and `a+conjugate(a)=-(2k-1)/k=-2+1/k`. In particular a is not a root of unity: its rational trace is not an integer.

The nonresidue set B0 has `2k-1` elements. Any two distinct translates intersect in exactly k-1 elements. One direct derivation writes `1_B0(x)=[1-chi(x)-delta_(x,0)]/2`, uses `sum_x chi(x)chi(x+h)=-1` for h!=0, and observes `chi(h)+chi(-h)=0`. The character sum itself follows by counting solutions to `y²=x(x+h)`: the change `(2x+h-2y)(2x+h+2y)=h²` gives p-1 solutions, so the sum is -1.

Consequently, for any two distinct K columns their entrywise ratio has a on k positions, conjugate(a) on k positions, and 1 on `p-2k=2k-1` positions. Their column inner product is `(2k-1)+k(a+conjugate(a))=0`; unimodularity gives K_p K_p* = pI. The ratio multiset is preserved by arbitrary source-row permutations.

## No off-axis orthogonal pair: Fourier-convolution argument

Suppose two cells in different physical rows and different columns were orthogonal. The nonzero row difference multiplies source positions by a unit mod p, so it suffices to consider two disjoint k-subsets A,B of F_p indicating where the relevant column ratio is a and conjugate(a). Let `S_A(h)=sum_(x in A) zeta^(h x)` and similarly S_B. Since the sum of all p roots is zero, the off-axis Gram equation becomes

`S_A(1)=conjugate(a) S_B(1)`.                                      (1)

Apply every cyclotomic Galois automorphism `zeta -> zeta^h`. With `S_A(0)=S_B(0)=k`, (1) yields `S_A(h)=f(h) S_B(h)` for all h, where

`f(0)=1`, `f(h)=conjugate(a)` for chi(h)=1, and `f(h)=a` for chi(h)=-1.

Let `h_f(x)=(1/p) sum_h f(h) zeta^(-h x)`. The Gauss identities give explicitly

`h_f(0)=-(k-1)/k`, and `h_f(x)=[1-chi(x)]/(2k)` for x!=0.       (2)

Fourier inversion of the product identity therefore says, for every x in F_p,

`k 1_A(x) = #{b in B : chi(x-b)=-1} - (k-1) 1_B(x)`.             (3)

Here chi(0)=0. Since A and B are disjoint, at each x in B the left side is zero. Equation (3) forces ALL k-1 directed differences `x-b` for b in B\{x} to be nonresidues. This is impossible for k>=2: for any distinct x,b in B, `chi(x-b)=-chi(b-x)`. Thus no off-axis Gram can vanish. On-axis Gram zeroes follow from Hadamard/Fourier orthogonality, proving the rook graph and showing that its only p-cell orthogonal bases are its p rows and p columns.

## Tensor argument and scope

For `gcd(m,p)=1`, CRT identifies F_(pm) with F_p tensor F_m up to harmless coordinate relabelings. A hypothetical transversal partitions by the m mutually orthogonal classical F_m-factor rays into m local p-cell ONB cliques. Every clique is a local row or local column. Let R_i and C_j count the two types and R,C be their totals. Each local row must be used m times, so `p R_i+C=m=R+C`, hence p divides R. Similarly p divides C. But R+C=m, contradicting gcd(m,p)=1.

Every K_p has a nonroot 2×2 cross-ratio a, so K_p tensor F_m is outside all finite Butson monomial classes. Also Q(sqrt(-p)) is a subfield of Q(zeta_p), so the earlier irreducible-Phi_p field theorem does not cover this construction. There are infinitely many p=3 mod4 (an elementary Euclid argument using `4 product(p_i)-1` suffices), and taking any even coprime m yields infinitely many even dimensions.

`frontier-20261028-paley-rook-p7-p11-control-v1.py` SHA **85389a3a32e97dd934b27acb6580ddb006798d6d10fff92271e750e0f6b98653**, result SHA **e0320e6f4fcb9e29b520054aa0ca806775ca338d86a78392dc47dad1d22f20f9**, independently checks g², the difference-set counts and all disjoint (A,B) equations for p=7 (210 pairs) and p=11 (9240 pairs) in Z[zeta_p]; these are controls, not the all-p proof.

The Gauss identities, difference-set calculation, Fourier inversion signs, row-permutation normalization and CRT caller need independent full review. No arbitrary even Fourier T is constructed or excluded, and unrestricted 1RQLS10 remains open in this work.
