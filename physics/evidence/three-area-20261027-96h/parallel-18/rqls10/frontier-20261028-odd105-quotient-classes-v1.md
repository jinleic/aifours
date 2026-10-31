# Odd-q quotient classes force three residual transversal patterns

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the finite sanity check: **Wed Oct 28 20:40:22 PDT 2026**. This is a new necessary structural restriction for the still-open odd-multiple-of-105 Fourier-product frontier; it is NOT a no-go for that frontier and does not address general QLS10. It imports [Lam–Leung Cor.3.4 and Thm.4.8](https://arxiv.org/pdf/math/9511209v1) and the universal q5 no-transversal certificate SHA **44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678**.

## 1. Statement

Let q be odd with 5|q, let K∈BH(10,q), and write G=mu_q/mu_5. Define two K columns equivalent when the G-valued entrywise quotient takes at most TWO values. If the actual Fourier-product QLS of K has an orthogonal transversal, then:

1. This is an equivalence relation. Every equivalence class has EVEN size, because the required five/five half-coordinate zero graph matches columns only inside these classes.
2. K is NOT phase-gauge equivalent to BH(10,5), by the imported q5 no-transversal result. Consequently no column class can have size6 or larger.
3. The ONLY remaining class-size partitions are `4+4+2`, `4+2+2+2`, `2+2+2+2+2`.
4. Every size4 column class determines a 5/5 row partition, and the corresponding row quotient equivalence relation has exactly those two five-element classes. If two column classes have size4, their 5/5 row partitions agree up to complement.

The earlier odd-root theorem excludes q with 105∤q. Thus this restriction is useful only for remaining odd q divisible105, and no example of a matrix satisfying the restrictions or of a transversal is asserted.

## 2. Low/high quotient profiles and matching

For odd q, the imported low-weight root-sum result says each ten-term zero sum splits into regular prime polygons, and its only possible forms are `5+5` and `3+7`. For `5+5`, its G quotient values are either one value ten times or two values five times each; call this LOW. In a `3+7` sum, the order3 and order7 subgroups inject into G and intersect trivially. Their two rotated cosets meet in at most one value. Thus the quotient has 9 or10 distinct values, each of multiplicity at most2; call this HIGH.

For any three columns a,b,c, if a/b and b/c are LOW, then a/c takes at most four quotient values. Orthogonality of a,c says that profile is either LOW (at most2 values) or HIGH (at least9), so it is LOW. Symmetry and reflexivity are immediate. Thus LOW is an equivalence relation on columns and, separately, on rows.

An orthogonal transversal yields the usual five/five coordinate half E and a perfect matching of the ten K columns on zero E-half sums. An odd-q zero sum of five roots is necessarily one regular5-gon, so the five terms in any edge all have one G quotient value. A HIGH profile has multiplicity at most2 and cannot supply an edge. Every edge is inside one LOW class, hence every class must be even.

## 3. One LOW class implies BH(10,5) gauge

We prove this for columns; the row statement follows by transpose. Dephase the first row and first column in G. Every nonconstant column is nonidentity on a five-set S avoiding row0. Since any two columns are LOW, their nonconstant supports are identical: if different, all four Venn regions occur and quotient values `1,a,b^(-1),ab^(-1)` have at least three distinct elements in the odd-order group G (the detailed argument is in `frontier-20261028-odd-root-hadamard-reduction-v1.md` SHA **5b14644b2f59f7a108372b3296e65772041b90412b9e95330a4596200989697d**).

If there is no nonconstant column, dephasing has made K mu5-valued. Otherwise group columns by their value delta on S; at least two groups occur. For columns in different delta groups, their quotient terms lie in two distinct G cosets on S and S-complement, so the LOW decomposition is one zero pentagon in each half. Write the row-S blocks as A_i. Their column spaces are pairwise orthogonal, while `sum_i A_i A_i†=10 I_5`. Therefore `A_i A_i†=10 P_i` and

`5 * |group_i| = Tr(A_i A_i†) = 10 * rank(A_i)`.

Every group size is even; in particular there are at most five groups. A row quotient between S and its complement therefore takes at most five values, hence must be LOW. It has at least two values and so has exactly two, each appearing five times, contradicting the even group sizes. Thus the nonconstant case is impossible. One LOW column class forces BH10,5 gauge.

## 4. A LOW column class of size at least six forces BH(10,5) gauge

Take a class C of size m>=6. Dephase relative to one of its columns and its first row. As above, any nonconstant members share one five-set S; group by their delta value on S. If there are no nonconstant members, every row quotient repeats one value at least six times, so is LOW. All rows are in one LOW class, and §3 applied to the transpose gives BH10,5 gauge.

Otherwise, groups with distinct deltas have mutually orthogonal nonzero column spans in BOTH five-row halves S and S-complement, because each such column pair is a LOW two-coset zero sum. Therefore the number t of delta groups is at most5. Two rows in the SAME half have an equal quotient at all m columns in C, hence their quotient profile is LOW. For rows in OPPOSITE halves, the m entries from C have t distinct quotient values. If `m-t>=2`, the full ten-column quotient has at most eight distinct values and is LOW.

For m>=7, `t<=5` gives `m-t>=2`. For m=6 the only remaining possibility is t=5, consisting of one two-column group and four singleton groups. In EACH five-row half the five nonzero mutually orthogonal group spans then all have dimension1. The two columns of the two-column group are therefore proportional on both halves. Their proportionality constants are q-th roots alpha and beta; global column orthogonality forces `5*alpha+5*beta=0`, i.e. `alpha=-beta`, impossible for odd q. Thus t<=4 also when m=6, and all row quotients are LOW. Applying §3 to the transpose proves the claim.

Hence a transversal, which cannot occur in the BH10,5 gauge class by the named base certificate, requires every LOW column class to have even size at most4. The three partitions in §1 follow.

## 5. Size-four support pins the row classes

Let a size4 column class be given. If its quotient profiles are all constant relative to its reference, every row-pair quotient repeats a value at least4 times and is LOW, giving one row class and BH10,5 gauge. In the remaining non-gauge case the class has a common five-set S of nonconstant support. Any two rows both in S, or both in the complement, repeat a quotient value four times across the class and therefore are LOW. These two five-sets each belong to a row equivalence class. If ANY cross pair were LOW, transitivity would merge all rows and §3 would force BH10,5 gauge. Thus exactly two row classes occur, S and its complement. Any other size4 column class gives the same two classes.

## 6. Check and limitations

`frontier-20261028-odd105-quotient-check-v1.py` SHA **59ac96edf2cbaab52ef357fa1f0081cd48cf3b2dacb10205c22246cbca7520ef** checked all441 choices of 3- and7-cosets in G=Z21: all have9 distinct quotient values and maximum multiplicity2; it also listed every even partition of10. This finite check corroborates only q=105's quotient example and the partition arithmetic, NOT the all-q proof. The all-q arguments above are written and require independent review of the imported root theorem, grouping, symmetries and physical half-matching caller. There is no conclusion for these three residual partitions or arbitrary phases.
