# All even orders: aligned Fourier–Diţă products have no transversal

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:04:32 PDT 2026**. This gives a non-computational all-even-order obstruction for a continuous family, in response to the even-order question. It does NOT prove that every even-order Fourier-product QLS lacks a transversal.

## 1. Theorem

For every integer m>=1, put n=2m, `zeta=exp(2*pi*i/n)` and `omega=zeta²`. For ANY m unit complex numbers delta_t, define the n×n complex Hadamard

`K_((a,t),(0,b)) = omega^(t b)`,
`K_((a,t),(1,b)) = (-1)^a delta_t omega^(t b)`,

where a∈{0,1}, t,b∈Z_m, and the physical Fourier coordinate of `(a,t)` is **aligned** as `tau=a*m+t`. The associated Fourier-product QLS has NO orthogonal transversal, including with repeated rays. Arbitrary column permutations/phases, source-row phases and affine source-coordinate reindexings `tau -> u*tau+v mod n` with gcd(u,n)=1 preserve the conclusion. An affine row permutation of the second m×m Fourier block is also covered, since its multiplier is absorbed into a column relabelling and its offset into column phases.

This is a full continuous `F2⊗Fm` Diţă deformation at every even order, with arbitrary delta. It does NOT allow a completely arbitrary physical source-row ordering, arbitrary m×m Hadamard blocks, or general K.

## 2. A transversal imposes injective effective labels

Suppose a transversal exists. Let `R_h(b)∈Z_(2m)` be the physical row occupied by its cell in column `(h,b)`, h=0,1. The 2m labels R_h(b) are a permutation of Z_(2m).

For distinct b,c in the SAME h group, the delta factors and source-a signs cancel. The exact inner product is proportional to

`(1+(-1)^Delta) * sum_(t=0)^(m-1) zeta^((Delta+2(c-b))*t)`,

where `Delta=R_h(c)-R_h(b)`. If Delta is odd this is automatically zero. If Delta is even, the geometric sum is nonzero exactly when `Delta+2(c-b)=0 mod 2m`. Hence orthogonality of all same-group pairs is equivalent to injectivity of each map

`S_h(b)=R_h(b)+2b mod 2m`.                                      (1)

Indeed equality of two S_h values already forces even Delta.

## 3. A missing Fourier frequency contradicts parity

For a cross-group pair b,c with odd `Delta=R_1(c)-R_0(b)`, orthogonality is exactly

`sum_(t=0)^(m-1) delta_t zeta^((Delta+2(c-b))*t)=0`.              (2)

The exponent `j=Delta+2(c-b)=S_1(c)-S_0(b)` is odd. For odd `j=1+2k`, the m sums in (2) are the m-point DFT of the nonzero vector `(delta_t*zeta^t)_t`. They cannot all vanish. Choose an odd frequency j0 whose sum is nonzero. Then (2) implies

`S_1 ∩ (S_0+j0) = empty`.

Both sets have m distinct elements by (1), so they partition Z_(2m). Summing their elements modulo2m gives

`sum S_0 + sum S_1 = sum_(r=0)^(2m-1) r - m*j0 ≡ m-m = 0`,

because j0 is odd. On the other hand the same sum from their definitions is

`sum_(h,b) S_h(b) = sum_(r=0)^(2m-1) r + 4*sum_(b=0)^(m-1)b ≡ m`,

since the R_h(b) partition all rows and `4*sum b=2m(m-1)`. This contradiction holds for every m, every unit delta, and every possible transversal.

## 4. Boundary

The proof uses only actual Fourier-product inner products, a finite DFT and modular arithmetic; it requires no Hadamard catalog, root-order condition, numerical search or maximality premise. It generalizes the aligned equal-Fourier-block portion of the n8/n10 continuous results, but it does NOT establish a universal even-order no-T theorem. Other source orders, non-Fourier subblocks and arbitrary QLSs remain open. Full written review of the label normalization, DFT and parity sum is required.
