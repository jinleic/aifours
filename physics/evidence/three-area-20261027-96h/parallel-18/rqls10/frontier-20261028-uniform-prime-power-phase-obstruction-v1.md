# Uniform QLS(10): no prime-power root-of-unity phase alphabet

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` before writing: **Wed Oct 28 17:42:09 PDT 2026**. This theorem covers EVERY resolution L and EVERY prime-power alphabet, but only the PHYSICAL uniform-overlap M_* branch with the explicitly stated phase restriction. It does NOT rule out arbitrary complex phases, composite-order alphabets with at least two distinct primes, nonuniform QLS, or the original unrestricted QLS10 target. No novelty claim.

## 1. Exact statement

Let n=10 and let an actual 1-resolvable QLS have the uniform physical overlaps: distinct cells in a common row, column or transversal are orthogonal, and every other pair has squared inner-product modulus1/8. Fix ANY reference row as coordinate ONB. Suppose there are cell phases lambda_x, common coordinate phases d_j, and a single primitive q-th root of unity zeta with q=p^e for some prime p and e>=1, such that EVERY nonzero coordinate of EVERY nonreference vector has the form

`(lambda_x d_j / sqrt(8)) * zeta^(k_(j,x))`.

Then **no such array exists**, for ANY prime p, ANY positive exponent e, ANY integer exponents k, ANY cell/coordinate phase gauges, and ANY Latin resolution L. The degenerate one-phase alphabet q=1 is also impossible. This includes all fixed real/Butson prime-power phase alphabets, but it is not WLOG for all complex phases.

The key number-theoretic lemma is independent of Latin squares:

> For any prime-power q=p^e and any seven q-th roots of unity eta_1,...,eta_7, `|eta_1+...+eta_7|² != 8`.

The proof includes the apparently exceptional p=41; it is not merely a modular necessary condition.

## 2. Exact seven-overlap caller for EVERY L

The separately delivered all-L support proof `frontier-20261028-uniform-phase-obstructions-v1.md`, SHA256 **11ae022040c391e2d4151446a6a88e47ab5feefcb27e5d38815d85e54c4dd945**, is rederived here at its needed scope. A nonreference cell x has exactly two zeros in the reference row basis: the reference cells in x's column and transversal, which are distinct. All eight other coordinates have modulus1/sqrt(8).

Let those zero coordinates be {i,j}, with x in column i and the transversal through reference-row e_j. In the transversal through e_i, discard the cells in columns i and j; the remaining8 cells have zero sets {i,k} with k!=i,j. At most one is in x's row, and none is in x's column or transversal. Hence at least7 of them share NO block with x, and each such pair has exactly7 common nonzero coordinates. (The symmetric column-j argument supplies at least7 additional partners, but one suffices here.) This holds for every nonreference x and EVERY L.

For such a nonsharing pair x,y, the actual uniform condition requires

`|<psi_x,psi_y>|²=1/8`.

Coordinate phases cancel and the cell phases give a common unit prefactor. The seven surviving products are q-th roots of unity, so this equality is exactly `|sum_(h=1)^7 eta_h|²=8`. Thus the lemma in §3 excludes the hypothesized array. No selected vector or finite-search outcome is needed in this caller.

## 3. Complete prime-power root lemma, INCLUDING p=41

Let zeta be a primitive q=p^e-th root, write each eta_j=zeta^(a_j), and let `c_d` be the number of ORDERED index pairs (i,j) with `a_i-a_j=d mod q`. The coefficient vector c_d consists of nonnegative integers with `sum_d c_d=49`. If the squared-magnitude equation held, the integer polynomial

`F(X)=(c_0-8)+sum_(d=1)^(q-1)c_d X^d`

would satisfy `F(zeta)=0` and `F(1)=49-8=41`.

The cyclotomic polynomial

`Phi_q(X)=sum_(j=0)^(p-1) X^(j p^(e-1))`

is monic and irreducible over Q. For completeness, `Phi_q(1+X)` is Eisenstein at p: modulo p its only nonzero coefficient is the leading one, while its constant term is p, not divisible by p². Thus `Phi_q` divides F over Q, and monic long division gives an INTEGER quotient. Evaluating at1 yields `p | F(1)=41`. Therefore p must equal41.

Now take q=41^e and h=41^(e−1). Since `deg F<q` and `Phi_q=1+X^h+...+X^(40h)`, the quotient has degree<h. Hence for EACH residue r=0,...,h−1, the41 coefficients of F at `r+jh` are one common INTEGER `b_r`. For r!=0 all are counts c_d>=0; for r=0 use j=1 to see `b_0=c_h>=0` (h<q). Moreover `sum_r b_r=F(1)/41=1`.

`c_0=sum_v multiplicity(v)^2` for the seven exponents, so c_0 is ODD and at least7. Since `b_0=c_0-8` is both nonnegative and odd, it is at least1. The sum1 and nonnegativity force `b_0=1` and every other b_r=0. Thus `c_0=9`, and every NONZERO difference count c_d is either0 or1.

But `c_0=7+2 sum_v binom(multiplicity(v),2)=9` means exactly ONE pair of equal exponents and at least one other distinct exponent. The difference between that doubled exponent and a distinct exponent occurs for at least TWO ordered index pairs, so some nonzero c_d>=2, contradiction. This rules out **all** powers of41, not just q=41. For q=1 all seven phases agree and the squared sum is49, not8. QED.

The proof's use of cyclotomic irreducibility and integer polynomial division is explicit; no numerical root approximation, selected L or exhaustive q enumeration is invoked. The resulting absence of a seven-term overlap is an exact local arithmetic obstruction, which §2 connects to the original SAME-array uniform branch.

## 4. Exact experiments and composite-order boundary

`frontier-20261028-cyclotomic-seven-sums-v1.py`, SHA256 **5de9c6b46203f2e34a544d654ec7807563ba89161cf87b422169a5614fc12347**, constructs cyclotomic polynomials by exact integer division and exhaustively checks multisets of seven q-th roots for the SINGLE overlap equation. Result `frontier-20261028-cyclotomic-seven-sums-result-v1.json`, SHA256 **d1c8c364c4d06a98e6c022d4a422ca2e8ffbf587c44f717cf7debf7401a74695**. Actual output:

```text
q 2:    8 multisets, 0 solutions
q 3:   36 multisets, 0 solutions
q 4:  120 multisets, 0 solutions
q 5:  330 multisets, 0 solutions
q 6:  792 multisets, 0 solutions
q 7: 1716 multisets, 0 solutions
q 8: 3432 multisets, 0 solutions
q 9: 6435 multisets, 0 solutions
q 10: 11440 multisets, 0 solutions
q 12: 31824 multisets, 192 solutions
q 15: 116280 multisets, 60 solutions
```

These finite computations check only one necessary inner-product equation; they do not establish the all-prime-power theorem or a full quantum array. In particular the composite-order situation CANNOT be ruled out by the same one-pair argument: for q=12,

`1+1+i+i+(1+zeta_3+zeta_3²)=2+2i`,

which has squared modulus8. In q=12 exponents this is the exact seven-term multiset `(0,0,0,3,3,4,8)`; the integer cyclotomic checker verified it. It is not an actual full M_* array.

The earlier GF(9) two-phase conference obstruction is separate: its phase ratio is `(-3+i sqrt(7))/4`, whose sum with its inverse is the nonintegral rational −3/2, so it is not a root of unity. A single complex 9×9 conference block in that alphabet nevertheless exists and was independently checked exactly in the earlier report. Neither result implies arbitrary complex phase impossibility.

## 5. Remaining scientific gap

The root lemma and physical-support caller give an all-L obstruction for a very broad discrete phase class. They do NOT show that a hypothetical uniform lift must have prime-power phases, and the exact q=12/q=15 one-pair solutions are evidence against overgeneralizing this arithmetic step. A valid next step would enforce multiple SAME-array row/column/transversal phase cycles for composite-order or genuinely non-root phases, or find a physical nonuniform 100-ray array. No such full witness or unrestricted obstruction is supplied here.

The theorem, cyclotomic irreducibility argument, exact original-object caller and code require independent review; historical held outputs are not premises. No external model/paid API, secret, deletion, publication or infrastructure action. The original 10×10/100-ray target remains OPEN.

**END — all prime-power phase alphabets excluded in the physical uniform branch; no global QLS10 no-go.**
