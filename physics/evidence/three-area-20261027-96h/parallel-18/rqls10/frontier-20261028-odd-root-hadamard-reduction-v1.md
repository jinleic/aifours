# Odd-root BH(10,q) reduction and an infinite no-transversal filter

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at arithmetic sanity check: **Wed Oct 28 20:34:04 PDT 2026**. This advances the finite q<=17 frontier to infinitely many odd q, under the precise named root-sum import below. It is NOT an unrestricted QLS10 no-go. No claim of novelty is made.

## 1. Results and named imports

**A. Prime-power reduction (self-contained).** For every odd prime p and e>=1, every `BH(2p,p^e)` is equivalent by p^e-root row/column phases to a `BH(2p,p)`. The proof is §§2–3.

**B. Order-ten odd-root reduction.** If q is odd, 5 divides q, and 21 does NOT divide q, every `BH(10,q)` is equivalent by q-root row/column phases to a `BH(10,5)`. If q is odd, 5 does not divide q, and 21 does not divide q, no `BH(10,q)` exists. This part explicitly imports Lam–Leung's classification of minimal low-weight vanishing sums, [On vanishing sums of roots of unity](https://arxiv.org/pdf/math/9511209v1), Cor.3.4 and Thm.4.8.

**C. Physical corollary.** If q is odd and **105 does not divide q**, ANY Fourier-product QLS10 with K∈BH(10,q), arbitrary K row/column gauges/permutations, has NO orthogonal transversal, even with repeated rays. This imports the Lam–Leung low-weight theorem and the independent finite universal BH(10,5) no-transversal candidate `frontier-20261028-all-bh10-5-product-obstruction-v1.md` SHA **44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678**. For q=5^e the reduction itself needs no Lam–Leung import, only that q5 base certificate for the physical conclusion.

Separately, for ANY q with `5 does not divide q` and `6 does not divide q`, the five-term half-sum condition excludes a transversal by the same named low-weight root theorem. This includes even q. It does not cover q divisible6, q even divisible5, or odd q divisible105.

## 2. Odd-quotient two-polygon rigidity lemma

Let p be odd, let H be a `2p×2p` complex Hadamard with entries in a finite odd-order root group containing mu_p, and suppose **every** row and column inner product decomposes into exactly TWO rotated regular p-gons. Then H can be made mu_p-valued by root-group row/column phases.

Pass to the odd-order quotient group G=mu_q/mu_p. For any two rows or columns, their 2p entrywise ratios have either ONE quotient value occurring2p times, or TWO quotient values each occurring p times. Dephase the first row and first column in G to1.

Every nonconstant column now equals a nonidentity value a on a p-set S of rows and 1 outside S; row0 lies outside S. Consider two nonconstant columns with p-sets S,T and values a,b. They cannot be disjoint, since both lie inside the other 2p-1 rows, and if S!=T then all four regions `S∩T`, `S\T`, `T\S` and `(S∪T)^c` are nonempty. Their quotient takes the four values

`1, a, b^(-1), a*b^(-1)`.

At most TWO distinct values are permitted. Since a and b^(-1) are both nonidentity they must coincide, giving b=a^(-1); the last value is a². In an odd-order group, a² is neither1 nor a. Contradiction. Thus all nonconstant columns share the SAME p-row support S.

For a row in S and a row outside S, the row quotient takes the column-dependent values a_c and includes 1 at column0. If any nonconstant column exists, it must take exactly TWO values, each p times. Thus columns split into two p-sets C0,C1 with quotient values1,a!=1.

For any c∈C0,d∈C1, the 2p column-ratio terms split into two DISTINCT mu_p cosets on S and its complement, p terms in each. By the two-polygon hypothesis each half sum is zero. Writing the p×2p submatrix of rows S as `[A B]`, with columns C0,C1, this is `A†B=0`. Hadamard row orthogonality gives

`A A† + B B† = 2p I_p`.

The column spaces of A and B are orthogonal. Hence AA† equals `2p` times the projector onto col(A), so

`p²=Tr(AA†)=2p*rank(A)`,

impossible because p is odd. Therefore no nonconstant quotient column exists: the dephased matrix is mu_p-valued. This proves the lemma. Exact finite sanity checker `frontier-20261028-odd-quotient-support-check-v1.py`, SHA **c3bc5cf49dc8dc1e1ec15d3ea1c7090394e968537432ed0ac282ab063ca85268**, checks the quotient four-value implication for sample odd cyclic groups and the trace contradiction for several odd p; the written proof covers ALL odd p and does not extrapolate from samples.

## 3. Prime-power and general odd root sums

For q=p^e, `Phi_(p^e)(x)=1+x^(p^(e-1))+...+x^((p-1)p^(e-1))`. A vanishing sum of2p q-th roots has, in every residue class mod p^(e-1), the SAME multiplicity at all p positions. The total2p therefore consists of exactly two rotated p-gons. §2 applies and proves A.

For general ODD q, Lam–Leung Cor.3.4 handles at most two prime factors; with at least three odd prime factors, Thm.4.8 says an asymmetric minimal vanishing sum has weight at least

`p1*(p2-1)+p3-p2 >= 3*(5-1)+7-5=14`.

Therefore every vanishing sum of weight<=10 decomposes into regular odd-prime polygons. The only decompositions of 10 into odd primes are `5+5` and `3+7`. If 21 does not divide q, the latter is unavailable. Thus any BH(10,q) column/row inner product is two regular5-gons; if 5 does not divide q no such inner product exists at all, and if 5 divides q §2 with p=5 proves B.

For C, if odd q has 5|q and 105∤q, then 21∤q, so B reduces to the q5 base and its no-transversal proof. If 5∤q, any five-term vanishing sum of odd q-th roots would have to decompose into odd-prime polygons of total weight5, so requires a 5-gon; impossible. For arbitrary (even or odd) q, the only decompositions of weight5 into prime polygons are 5 or 2+3, giving the `5|q OR 6|q` necessary condition for a transversal. The same lower-bound import ensures there is no asymmetric minimal sum of weight5.

## 4. Scope and pending review

These statements provide an infinite root-alphabet obstruction for the SAME actual Fourier-product vectors, without requiring a finite catalog of q>5. They do not exclude odd q divisible105, even q divisible5 or6, arbitrary complex phases, non-Fourier products or the general original QLS10. The odd-quotient lemma, Lam–Leung use and q5 exact base certificate all require independent full review before adoption. The earlier q<=17 report conservatively called q25 unresolved; §1C now excludes it conditionally. No general no-go, target witness, formal proof or novelty clearance is asserted.
