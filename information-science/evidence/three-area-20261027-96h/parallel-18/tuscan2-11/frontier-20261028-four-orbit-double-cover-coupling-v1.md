# Two surviving four-orbit patterns force an exact doubled difference cover

Owner **InfoRecursiveMDS18-2**, info-4. Actual native clock before writing: **Wed Oct 28 22:25:22 PDT 2026**.

**NEW author-WRITTEN candidate, unreviewed.** This sharpens two ENTIRE residual patterns, with every base permutation row, shift subset and endpoint free. It is not an exclusion or a search of selected arrays. No scientific execution or external source is used. Input: `frontier-20261028-orbit-multiplicity-gcd-and-singleton-v1.md`, SHA `8a68232f98c5a9b54979b3e266169a86bce1f0896e3846a9bee8feffa1fe1512`, in particular the exact actual-row counts sum_i m_i k_i(e)=11 and sum_e k_i(e)=10. No certificate outcome is an input.

For every base row R_i let Δ_i=last(R_i)−first(R_i) modulo 11, a NONZERO residue. It equals sum_e e·k_i(e).

## 1. Multiplicities (5,4,1,1)

Write a_e,b_e,c_e,d_e for the adjacent-difference counts of the four base rows, ordered as the multiplicities. They satisfy

5a_e+4b_e+c_e+d_e=11,   sum_e a_e=sum_e b_e=sum_e c_e=sum_e d_e=10.

The source packing bound gives 0≤a_e≤2 and 0≤b_e≤2. If a_e+b_e≥3, the least possible 5a_e+4b_e is 13, impossible. Hence a_e+b_e≤2 for every one of the ten nonzero differences. Their total is 20, so equality holds for every e. Substitution yields

**a_e+b_e=2,   c_e+d_e=3−a_e      for EVERY nonzero e.**     (1)

Thus R_1 and R_2 together use every nonzero difference exactly twice. A difference doubled in R_1 is absent in R_2, and vice versa; the single occurrences agree. Neither row can use every difference once, so both missing and doubled differences occur, in equal nonzero numbers. Telescoping (1) gives the original-row endpoint coupling

**Δ_2=−Δ_1,   Δ_3+Δ_4=−Δ_1.**                              (2)

No assertion that R_2 is a reversed/translated R_1 follows: (1) describes their difference MULTISETS, not their symbol order.

## 2. Multiplicities (4,3,3,1)

Now write a_e,b_e,c_e,d_e in that order, giving

4a_e+3b_e+3c_e+d_e=11,   sum_e a_e=sum_e b_e=sum_e c_e=sum_e d_e=10.

Here 0≤a_e≤2. Modulo 3, d_e≡2−a_e, and 2−a_e belongs to {0,1,2}, so d_e≥2−a_e. But sum_e(2−a_e)=10=sum_e d_e. Equality must hold term by term. Therefore

**a_e+d_e=2,   b_e+c_e=3−a_e      for EVERY nonzero e.**     (3)

R_1 and the singleton base row R_4 together use every nonzero difference exactly twice; their doubled/missing differences are complementary. The endpoint consequences are

**Δ_4=−Δ_1,   Δ_2+Δ_3=−Δ_1.**                              (4)

## 3. Remaining original gap

Equations (1)–(4) are necessary for EVERY actual T1(11), hence T2(11), with the indicated orbit multiplicities under ANY 11-cycle. They couple whole free base rows and endpoints rather than choosing a particular row or checking only separate marginals. They do not construct those rows, impose the full T2 condition, or exclude the two patterns. The third four-orbit residual (5,3,2,1), and arrays occupying five or more orbits, remain unresolved. The unrestricted T2(11) target remains **OPEN**; no support-9, formal/kernel, novelty or adoption claim.
