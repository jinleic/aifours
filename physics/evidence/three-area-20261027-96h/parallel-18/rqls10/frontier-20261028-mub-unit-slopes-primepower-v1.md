# Prime-power phase-ratio obstruction for every invertible Weyl slope

**WRITTEN + EXACT CYCLOTOMIC-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the new check: **Wed Oct 28 19:14:06 PDT 2026**. This extends the slope-one prime-power result `frontier-20261028-mub-primepower-ratio-obstruction-v1.md` SHA **c78bff776a962122ca1370a4acc8ec49d0b723b268194c45330f58e541743968** to all unit slopes; it does NOT close general irrational or composite-phase branches.

## 1. Statement

For any `k in {1,3,7,9}=Z10*`, put `D_k=diag(exp(pi*i*k*t²/10))`. The bases `I10,F10,D_k F10` are mutually unbiased: the chirp autocorrelation vanishes at every nonzero shift because k is invertible mod10. Under CRT they factor into qubit Z, X, ±Y bases and 5D bases I,U,B_q with `q=4k mod5`,

`U_(t,j)=omega^(3tj)/sqrt(5)`, `B_q=diag(omega^(q t²)) U`.

**Claim:** no common unbiased phi has its five CRT Schmidt ratios `b_t/a_t` in a single arbitrary-phase coset of roots of unity of ANY prime-power order. The proof applies ALL k at once after one additional h=2 calculation. Any common phi would construct a 100-distinct-ray Weyl-orbit 1-RQLS with transversal `r=k c` and its row shifts, by the same moment and stabilizer proof as the slope-one Weyl packet; no phi is constructed here.

## 2. Fifth-root reduction and symmetries

The argument in the cited slope-one packet is independent of k: a vanishing sum of FIVE roots in a prime-power coset forces prime5, and the ratios must be a rotated permutation of the five fifth roots. Affine permutations are character ratios and are excluded by the odd-cycle lemma `frontier-20261028-character-ratio-obstruction-v1.md` SHA **ae331153fb2b082ab50382e12531c2766b288e4cc654aacca11b86cdaf4036b8**, which permits arbitrary diagonal D.

For non-affine permutations, the operations `sigma(t)->epsilon*sigma(c t+d)+b` remain valid for EVERY q!=0: use the common monomial unitary `T v_t=omega^(eta t²) v_(c t+d)`, with eta=0 when c²=1 and eta=q when c²=4. It preserves I and permutes B0,Bq. Swapping a,b and changing the global phase of b realize the output sign and translation. The exact orbit census in `frontier-20261028-nonaffine-fifthroot-cert-v1.py` SHA **a568e81fbd5ea800aaa18d9951e102edc37bb74f80a8eb572c649195d648683c** reduces all100 non-affine permutations to sigma0=(0,1,2,4,3). The new checker SHA **b494559d50e6127106c245b13f76c07fc1e7448ff6bcd5205bd614eeff0356f7** verifies 4000 exact basis-symmetry exponents for all q!=0.

A separate coordinate scaling t->2t maps `{I,B0,Bq}` to `{I,B0,B(-q)}`. Thus it suffices to cover q=4 (the old k=1 case) and q=3 (new k=2 mod5 case).

## 3. New q=3 second-gap contradiction

Let sigma=sigma0 and write `y_t=5 P_(t+2,t)`, P=aa†+bb†. As in the slope-one packet, flat B0 and B3 diagonals imply

`sum_t y_t=0`, `sum_t y_t omega^(3t)=0`.

Thus the Fourier support is `{1,3,4}`. The second-gap sigma difference pattern is `(2,3,1,1,3)`, so the squared moduli are

`((3-sqrt5)/2,(3-sqrt5)/2,(3+sqrt5)/2,(3+sqrt5)/2,(3-sqrt5)/2)`.

Put `d_j=(1/5)sum_t |y_t|² omega^(-j t)`. Exact reduction modulo Phi5 gives

`d0=(15-sqrt5)/10 < 2`,
`d1=-(5+sqrt5)/10`, `d2=(5-sqrt5)/10`,
`d1*d2²=-(5-sqrt5)/50 < 0`, `|d1|+|d2|=1`.

With `y_t=c1 omega^t+c3 omega^(3t)+c4 omega^(4t)`, the singleton/double Fourier coefficients are

`d1=c4 conjugate(c3)`,
`d2=c1 conjugate(c4)+c3 conjugate(c1)`.

Write `c3=p exp(i alpha)`, `c4=q0 exp(i beta)`, `c1=r exp(i gamma)`. The negative-real phase of `d1*d2²` forces `|d2|=r|p-q0|`, while `|d1|=p q0`. Therefore

`d0=p²+q0²+r² >= 2(p q0+r|p-q0|)=2(|d1|+|d2|)=2`,

contradicting d0<2. The exact Phi5 identities and the 4000 general-q symmetry checks are independently replayed by `frontier-20261028-mub-slope2-fifthroot-check-v1.py`, SHA **b494559d50e6127106c245b13f76c07fc1e7448ff6bcd5205bd614eeff0356f7**. The q=4 case is the first-gap proof in the cited packet, and q=1,2 follow by the t->2t sign equivalence.

## 4. Scope of all-root strengthening

The ALL-root-of-unity coset obstruction in `frontier-20261028-mub-all-root-ratio-obstruction-v1.md` SHA **3fac11c5e6f334f543de33bf934b89292df03aba18643efd63659e96fbcd8419**, which additionally imports the cited Lam–Leung small root-sum theorem, carries from k=1 to k=9 by the q->-q coordinate scaling: both the rotated-pentagon and continuous pair-plus-triangle P-flatness obstructions are invariant under it, and affine ratios are excluded for any D. For k=3,7 the pair-plus-triangle composite-order case remains OPEN; only the prime-power exclusion is claimed here.

No condition above is assumed WLOG for an arbitrary 1-RQLS10. Full independent review, a real witness or an unrestricted no-go, and novelty assessment remain pending.
