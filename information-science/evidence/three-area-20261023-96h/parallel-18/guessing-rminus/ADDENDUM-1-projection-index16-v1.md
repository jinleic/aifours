# Addendum 1 — every offending six-coordinate projection has index at least 16

Observed immediately before writing: `2026-10-23T14:20:00-0700`.

**Status: CANDIDATE; separate reconstruction pending.** Read with `candidate-coset-barrier-v1.md`, SHA-256 `697c0f332ac9759efed98e92ef926f10d2020ffef77a9f538a34e6af28191004`, and `inputs-v1.json`. No earlier snapshot is changed. No executable group enumeration or arithmetic check was used.

This addendum strengthens the first candidate's order-960 barrier to an effective-group order-**1920** barrier. It supplies a new complete written interval/entropy argument, not a new guessing-number bound.

## 1. Strengthened statement and retained hypotheses

Use exactly the full uniform FD-consistent coset code of the candidate. If Phi<0, then for **every** one of its eight diamond complements Z,

`[G : L_Z] >= 16`, where `L_Z=intersection_{z in Z} H_z`.

Together with the imported minimum Ingleton-violator order 120 this implies

`|G/core_G(intersection_v H_v)| >= 16*120 = 1920`.

Thus effective ambient groups of order **strictly less than 1920** cannot pass the strict aggregate criterion for a 20/3 improvement. No code at 1920 is exhibited; the threshold is not asserted optimal. The corresponding integer inequality is still `[G:K]^3 <= product_v [G:H_v]^2` in the excluded class. The unchanged prime-field PSL/PGL barrier from the candidate holds separately, for all prime sizes.

Imports I1, I2 and the order-120 part of I3 have exactly the same trust status as in the candidate: prior rational coefficient identities and a primary-source computer-assisted finite-group result, not fresh executable or formal verification.

## 2. Preparatory facts

Assume Phi<0 throughout. Candidate §3 gives, for every v,

`sum_{u!=v} I(X_u;X_v) < H(X_v)/2`.                            (2.1)

It also gives pairwise incomparable proper coordinate subgroups. For one fixed complement Z, put L=L_Z and m=[G:L]. Each of the six H_z is a strict intermediate subgroup `L<H_z<G`.

Write `n_z=[G:H_z]`. For any two distinct z,w in Z put `n_zw=[G:H_z intersection H_w]`. The subgroup-index identities give

- n_z is a proper nontrivial divisor of m;
- n_zw divides m and is a multiple of both n_z and n_w;
- `max(n_z,n_w) < n_zw <= n_z*n_w`, with strictness from incomparability;
- `I(X_z;X_w)=log(n_z*n_w/n_zw)`.

The inequality n_zw<=n_z*n_w follows from the injection of the intersection-coset set into the product of the two coset sets. These are exact integer/divisibility statements, not numerical approximations.

There is one more graph-specific restriction:

> Each peripheral H_v, v in {2,3,4,5,6,7,9,10}, is non-normal in G.      (2.2)

Indeed, each peripheral vertex appears in the first pair (U,V) of at least one listed diamond. If H_v were normal in G, its intersection A_v=L_{Z'} intersection H_v would be normal in the conditional group L_{Z'}. The product of A_v and the other first-pair subgroup would be a subgroup, and the corresponding coset variables would have extractable common information equal to their mutual information. This forces their Ingleton expression J>=0, contradicting I2 and Phi<0. This is Mao–Thill–Hassibi's standard Condition 3, also Craven Lemma 2.8(iii), and does not assume that the other three coordinate subgroups are normal.

For completeness, the entropy step in that common-information argument is short. If W is a deterministic function of both A and B with H(W)=I(A;B), then `H(W|C)<=I(A;B|C)` and `H(W|D)<=I(A;B|D)`. Also

`I(W;C) <= I(C;D)+I(W;C|D) <= I(C;D)+H(W|D)`.

Adding H(W|C) gives `I(A;B)<=I(A;B|C)+I(A;B|D)+I(C;D)`, as required.

Every diamond contains exactly one hub (1 or 8) and three peripherals. Therefore its complement Z contains exactly **five peripherals and the other hub**. The five peripheral intermediate subgroups satisfy (2.2); the sixth subgroup may be normal, but remains proper and incomparable with all five.

## 3. Indices at most 7

Candidate §5 already proves that six incomparable strict intermediate subgroups force m>=8. That proof uses only normalizers and the subgroup structures of groups of orders 4 and 6, with the latter elementary alternatives C6 and S3. Thus only m=8,...,15 remain to exclude.

## 4. Index 8

For a peripheral z, n_z cannot be 2 because every index-two subgroup is normal. Therefore n_z=4, and [H_z:L]=2, for all five peripherals.

Since L has index two in H_z, all five H_z normalize L. Put N=N_G(L). If N<G, [N:L] is 1,2 or 4. The group N/L then has order at most 4 and at most three subgroups of order two. It cannot contain these five distinct H_z/L. Hence N=G and L is normal in G.

Now Q=G/L has order 8, and the five peripheral H_z/L would be five distinct **non-normal** subgroups of order two in Q. A group of order 8 has at most four such subgroups:

- if Q is abelian, all subgroups are normal;
- otherwise its center has order 2, since a cyclic quotient by the center would force Q abelian;
- not all six noncentral elements can be involutions, since then every nonidentity element would have order two and Q would be abelian;
- a non-involution and its distinct inverse account for at least two of the six noncentral elements, leaving at most four noncentral involutions;
- an order-two subgroup is normal exactly when its unique nonidentity element is central.

This contradiction excludes m=8. No classification or enumeration of order-eight groups is needed.

## 5. Index 9

Every strict intermediate subgroup has n_z=3 and [H_z:L]=3. For two distinct ones, n_zw is a multiple of 3, divides 9, is larger than 3 and at most 9. Thus n_zw=9, so `H_z intersection H_w=L`.

Consequently the sets H_z minus L are disjoint, each of size 2|L|, inside G minus L of size 8|L|. At most four such groups can exist. Even the five peripherals are impossible. Thus m!=9.

## 6. Indices 10 and 14

Write m=2r with r=5 or r=7. A peripheral subgroup cannot have index two and hence has n_z=r and relative order [H_z:L]=2. Two distinct such groups intersect exactly in L, so for any peripheral pair

`I(X_z;X_w)=log(r/2)`.

For a fixed peripheral z, its other four peripheral companions already contribute

`sum_{w!=z} I(X_z;X_w) >= 4 log(r/2) > (1/2) log r = H(X_z)/2`,

contradicting (2.1). The strict numerical inequality is equivalent to `r^7>2^8`, true for both r>=5; for instance `5^4=625>256` already suffices. No assumption that L is normal is used here.

## 7. Index 12

A peripheral subgroup has n_z in {3,4,6}. Let a,b,c be the numbers of the five peripherals of those respective indices, so a+b+c=5. Divisibility and incomparability give the following exact pairwise informations whenever the corresponding pair exists:

| n_z,n_w | Forced n_zw | I(X_z;X_w) |
|---|---:|---:|
| 3,3 | 6 | log(3/2) |
| 3,4 | 12 | 0 |
| 3,6 | 12 | log(3/2) |
| 4,4 | 12 | log(4/3) |
| 4,6 | 12 | log 2 |
| 6,6 | 12 | log 3 |

For example, a 3,3 pair has n_zw dividing 12, a multiple of 3, strictly greater than 3 and at most 9, hence 6. The other rows follow the same index rules in §2.

First c=0. If both b and c are positive, a vertex of index 4 has a mutual-information term log 2 from an index-6 companion, already equal to half its entropy and violating the strict inequality (2.1). If c>0 and b=0, then a+c=5. If c>=2, an index-6 vertex has a log 3 term, larger than `(1/2)log 6` because 9>6. If c=1, it has four log(3/2) terms, again larger than `(1/2)log 6`, since `3^8=6561 > 6*2^8=1536`. All possibilities c>0 are excluded.

Now a+b=5. If a>=3, an index-3 vertex receives at least `2log(3/2) > (1/2)log3`, since `3^4=81 > 3*2^4=48`. Thus a<=2. If b>=4, an index-4 vertex receives at least `3log(4/3)>log2`, since `4^3=64>2*3^3=54`. Thus b<=3. Necessarily a=2,b=3.

Consider the sixth vertex, the hub in Z. Its index is one of 2,3,4,6.

- If its index is 3, it creates a third index-3 coordinate and the previous contradiction applies to those coordinates.
- If its index is 4, it creates a fourth index-4 coordinate and the previous contradiction applies.
- If its index is 6, each index-4 coordinate has a log 2 term and violates (2.1).
- If its index is 2, it cannot be incomparable with an index-4 coordinate containing L. Their intersection index would have to divide 12, be a multiple of 4, be strictly greater than 4 and be at most 8. No such integer exists.

Thus m!=12.

## 8. Index 15 and the remaining primes

For m=15, every peripheral index is 3 or 5. There is at most one distinct index-3 subgroup containing L: for a 3,3 pair the intersection index would divide 15, be a multiple of 3, exceed 3, and be at most 9, which is impossible.

Hence at least four peripheral coordinates have index 5. A pair of these has n_zw=15 and mutual information log(5/3). For any one of four such coordinates, its other three companions give

`sum I >= 3log(5/3) > (1/2)log5`,

because `5^6=15625 > 5*3^6=3645`. This contradicts (2.1). Thus m!=15.

The remaining m=11,13 are prime and have no strict intermediate subgroup at all. This exhausts 8 through 15 without scientific enumeration. Therefore m>=16 for every diamond complement.

## 9. Group-order consequence and dependency boundary

Section 4 of the original candidate shows that every L_Z itself violates Ingleton, so the imported minimum offender order gives |L_Z|>=120. Multiplying by the newly proved projection index gives |G|>=1920. Quotienting by core_G(K) preserves the code, all FDs and every entropy and repeats this argument, giving the effective-order statement.

The mathematical strengthening is the **five non-normal peripherals plus the sixth hub** obstruction, with the exact mutual-information inequalities. It does not rely on the detailed PGL subgroup classification. Conversely the PGL/PSL theorem is a separate family exclusion, not evidence that all larger group representations fail.

The full R-minus target remains unresolved. Uniform coset constructions with effective groups at least1920, nonuniform coset-supported laws, correlated/restricted products and general nonlinear strategies are not excluded by this addendum.
