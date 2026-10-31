# Parity-quarter tight frames for even cyclic resolutions

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:30:08 PDT 2026**. This is a necessary structure for ANY even cyclic-resolved quantum Latin square, without Fourier or Butson assumptions. It yields a new self-contained n=4 no-go and a symmetric half-orthogonality caller for the Fourier attack; it is not a general even-order no-go.

## 1. Four tight frames

Let n=2m and let `v_(r,c)` be a QLS whose resolution consists of the cyclic diagonals `r-c=l mod n`. Put `P_(r,c)=|v_(r,c)><v_(r,c)|`. For a,b∈{0,1}, define

`A_ab = sum_(r≡a mod2, c≡b mod2) P_(r,c)`.

Each row, each column and each cyclic diagonal is an ONB. Adding the m even rows, m even columns and m even-labeled diagonals gives

`A_00+A_01=m I`, `A_00+A_10=m I`, `A_00+A_11=m I`.

The sum of all n² projectors is n I=2m I. Solving the four equations yields

`A_00=A_01=A_10=A_11=(m/2) I=(n/4) I`.             (1)

Thus each parity quarter is an `m²`-vector unit-norm tight frame for C^n, with frame bound m/2. This holds for ALL n even, any actual unit vectors and any cyclic label square up to global row/column relabelling. It is a necessary condition only: tight frames of the indicated size can exist.

## 2. Self-contained n=2 and n=4 no-go

For n=2, a quarter has one rank-one projector but (1) demands `(1/2)I_2`, impossible.

For n=4, quarter A_00 has exactly four unit vectors and sums to I_4, hence is an ONB. Choose it as the coordinate basis. Each cell in A_01 is orthogonal, in its even row, to the TWO A_00 vectors in that row, so has support at most2. Similarly every cell of A_10 is orthogonal to the TWO A_00 vectors in its even column, and every cell of A_11 is orthogonal to the TWO A_00 vectors in its cyclic diagonal. All16 vectors are therefore globally two-sparse in this basis.

The self-contained two-sparse classicalization proof in `frontier-20261028-even-cyclic-two-support-obstruction-v1.md` SHA **073647ca824ee430313d427f201065124eed745e9849c9bf459d28d76f027741** says no even-order cyclic resolution can have that property. Thus no QLS4 has a cyclic resolution. In particular no order4 Fourier-product QLS has a transversal, by cyclic shift of any one transversal. This is an elementary written proof independent of the previously cited Ball–Simoens n4 classification. For n=6 the published unrestricted no-2-MOQLS6 theorem still applies separately.

## 3. Symmetric half-orthogonality for any Fourier candidate

Let an even-order Fourier product admit a transversal; permute K columns to put it on the diagonal. Then BOTH K and `K∘F_n` are complex Hadamards. Comparing the two orthogonality equations for row t and row t+m gives

`sum_(c even) K_(t,c) conjugate(K_(t+m,c))=0`,
`sum_(c odd)  K_(t,c) conjugate(K_(t+m,c))=0`.

Likewise, comparing column c and column c+m yields zero separately over even and odd coordinate rows. These are simultaneous conditions on the SAME matrix, not independent necessary examples. For n=10 they give ten paired five-term zero sums in each direction, before requiring the other transversal inner products. They follow directly because `zeta_n^(m c)=(-1)^c`, and are valid for arbitrary complex phases, not just roots of unity.

## 4. Open boundary

At n=8, a quarter contains16 vectors in C8 with frame bound2, so (1) no longer forces an ONB or two-sparsity. At n=10 the bound is5/2 for25 vectors in C10. The parity-frame identity does not imply their nonexistence, does not settle general even Fourier-product T, and does not apply to arbitrary noncyclic resolutions. The written frame derivation and the n4 classicalization dependency need independent review.
