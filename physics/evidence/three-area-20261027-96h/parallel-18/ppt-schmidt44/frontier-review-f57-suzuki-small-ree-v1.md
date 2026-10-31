# f57 — Suzuki and small-Ree simple-family coset arguments

Reviewer **PhysicsPPT44-2**. Actual native clock observed immediately before creation: **Wed Oct 28 17:53:10 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT STATED IMPORTS AND SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** For `Sz(2^(2m+1))`, m≥1, the candidate proves Sun6/7/8 conditional on local Sun5 and the cited Suzuki order/maximal-subgroup statements. For small `²G₂(3^(2m+1))`, m≥1, it proves Sun8 conditional on local Sun7 and the cited Ree structure statements. The **maximal-subgroup classifications and Sun5/Sun7 proofs are not rederived** in this review. This is same-harness written/source checking plus bounded exact calculations, not an independent-family, human, formal/kernel, novelty, priority or all-simple-group acceptance.

## 1. Inputs and actual source reads

I read the complete assignment, both candidates and both stated parent verdicts in the required order:

- Assignment `f57-suzuki-small-ree-simple-families/assignment-v1.json`: SHA256 `13424926cb5894a52b7e211bc868dd24eff3f2c9d63b3461df1d36e3a8b3571f`.
- Suzuki candidate, 74 LF: SHA256 `0ff73b77b1abc66e642747d4e42c9a0cdc7f4ac385a31cde55b673d201d27818`.
- Small-Ree candidate, 78 LF: SHA256 `2db80cfabb54771aabc84faf69191047f47fbf90bc5be7ba891845b3ee47dd65`.
- Sun5/6 parent verdict, 31 LF: SHA256 `63baa72b107e0f809c26a5057f10b6fd31f8ae2f09cffb527873bec11a8107ee`.
- Later Sun7 composition parent verdict, 63 LF: SHA256 `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`.

I then read Héthelyi–Horváth–Petényi's [Suzuki paper](https://arxiv.org/html/1404.1523v1), §2, Theorem 3.1 and Theorem 4.1; Pierro's [small-Ree paper](https://arxiv.org/html/1410.8702v2), §§2.1–2.2 and the q=27 remark in §4.18; the explicit Ree order in [Alavi–Daneshkhah–Mosaed](https://arxiv.org/html/1606.00049v1); and the disclosed competing order/action statements in [Busch et al.](https://arxiv.org/html/2510.06479v1), §§2.2–2.3. These source statements are checked below at their actual stated scopes. The 2014 papers attribute their subgroup information to earlier classification sources; I did **not** rederive those classifications or read their original proofs. The competing 2025 source was inspected as HTML, not independently checked against its PDF.

I have earlier Sun-coset familiarity and reviewed other Sun transfers in this run; this is not a blind or clean-cognition review. The local candidate implications are rederived below, without treating historical quarantined outcomes or either author's program output as proof. No author contact or nested agent was used. The prior-art/novelty investigation is separate and no exclusion is called new on this evidence.

## 2. The imported statements and chronology

The Sun5 parent verdict states the arbitrary-group five-disjoint-left-coset theorem at its named written composition, Sun3/Sun4 and other dependency/erratum boundaries. Its contemporaneous statement that full Sun7 was then unaccepted predates the later Sun7 verdict. The later verdict explicitly states the arbitrary-group seven-disjoint-left-coset theorem at its own full written-composition and erratum/ledger boundaries. I read those verdicts, **not their entire transitive proof DAGs**. They are statement-level conditional imports here, not human, kernel or priority certification. In fact the two candidate theorems need only `Sun5(G)` or `Sun7(G)` for the particular family member, respectively.

## 3. Actual-coset parity and p-free-index lemmas

Let n_i be indices of the same actual pairwise-disjoint cosets; an index-one coset is all G, so in any collection of at least two such cosets every subgroup is proper.

### 3.1 Suzuki parity lemma

Let G be finite, 3∤|G|, and satisfy Sun5(G). Assume every actual proper odd-index subgroup has index divisible by D≥8. Suppose k∈{6,7,8} actual disjoint cosets have all pair gcds<k. Then each gcd is at most 7. If five indices were even, Sun5 applied to those **same five cosets** would force a pair gcd≥5. Since each index divides |G|, the gcd is even and not divisible by 3. The only positive even possibilities ≤7 are 2 and 4, contradiction. At most four indices are even. Since k≥6, at least two indices are odd; both proper odd-index subgroups have indices divisible by D, so their pair gcd is at least D≥8≥k, contradiction. Thus Sun6, Sun7 and Sun8 follow. No normality or covering premise is needed.

### 3.2 Ree p-free-index lemma

For p∈{2,3,5}, suppose G is finite and satisfies Sun7(G), and every actual proper subgroup of p-free index has index divisible by D≥8. If eight actual disjoint cosets had all pair gcds≤7 and seven indices were divisible by p, Sun7 applied to those seven would give a gcd≥7. It is also ≤7 and divisible by p, impossible: the only possibility at the bound would be 7, which is not divisible by p. Thus at most six indices contain p; at least two are p-free, proper, and both divisible by D, forcing a gcd≥8. This proves Sun8(G). The p=7 case is not included and would not follow from this argument.

## 4. Suzuki source list, all 2-parts and small-field boundary

For `q=2^(2m+1)`, m≥1, q≥8. The cited source §2 states

`|Sz(q)|=q²(q²+1)(q−1)`.

Both q²+1 and q−1 are odd, so the group 2-part is q². Theorem 3.1 gives `N_G(F)` order `q²(q−1)`, a dihedral group of order `2(q−1)`, the two cyclic Hall orders `q±2^(m+1)+1` and normalizer orders four times those values, and subfield groups `Sz(s)` for odd powers s≥8 with q=s^t. Theorem 4.1 lists the conjugacy representatives of maximal subgroups as those normalizers and **maximal proper subfield** groups. Thus the cited list is a source statement about all maximal types, not something inferred from the q=8 calculation.

The comparison of 2-parts is uniform:

| Source-stated type | Order | Exact 2-part |
| --- | --- | --- |
| `N_G(F)` | `q²(q−1)` | q² |
| dihedral `N_G(H)` | `2(q−1)` | 2 |
| each Hall normalizer | `4(q±2^(m+1)+1)` | 4, since the bracket is odd |
| proper subfield `Sz(s)` | `s²(s²+1)(s−1)` | s²<q² |

Any actual H<G of odd index has the full group 2-part q². A Sylow-2 subgroup of H is therefore a Sylow-2 subgroup of G, and H is contained in some maximal proper M. The complete cited list excludes every type except `N_G(F)`, since q²≥64>4. Therefore `[G:H]=[G:M][M:H]` is divisible by `[G:N_G(F)]=q²+1`, irrespective of which conjugate M contains H.

Also q=2^(odd)≡−1 mod 3, so q−1≡1 and q²+1≡2 mod 3; 3∤|G|. With D=q²+1≥65, §3.1 proves Sun6/7/8 conditional on Sun5(G) and the cited structure. At the boundary q=8, q²=64 and D=65, and there is no proper source-listed subfield `Sz(s)` with s≥8. The exceptional order-20 `Sz(2)` is not silently included as a simple family member.

## 5. Small-Ree source list, all 3-parts and q=27

For `q=3^(2m+1)`, m≥1, q≥27. Pierro §2.1 gives Hall orders `(q−1)/2`, `(q+1)/4`, `q−√(3q)+1`, `q+√(3q)+1` and the product formula for |G|. Because the last two factors multiply to `q²−q+1`, the source formula is

`|G|=q³(q³+1)(q−1)`.

The same explicit order appears in [Alavi–Daneshkhah–Mosaed](https://arxiv.org/html/1606.00049v1). Since q³+1≡1 and q−1≡−1 modulo 3, the group 3-part is q³. Pierro §2.2 gives the exhaustive maximal-subgroup types attributed to Levchuk–Nuzhin and Kleidman: maximal subfield, parabolic, involution centralizer, four-group normalizer, and the two Hall normalizers. The needed exact order/3-part comparison is:

| Source-stated type | Order | Exact 3-part |
| --- | --- | --- |
| parabolic `q^(1+1+1):(q−1)` | `q³(q−1)` | q³ |
| involution centralizer `2×PSL₂(q)` | `q(q²−1)` | q |
| four-group normalizer | `6(q+1)` | 3 |
| each Hall normalizer | `6(q±√(3q)+1)` | 3 |
| proper subfield `²G₂(q₀)` | `q₀³(q₀³+1)(q₀−1)` | q₀³<q³ |

For the centralizer, `|PSL₂(q)|=q(q²−1)/2` for odd q. For the four-group normalizer, Pierro's `D_(q+1)/2` has order `(q+1)/2` in the source's convention: its cyclic Hall subgroup has order `(q+1)/4` and index two. Thus `(2²×D):3` has order `4·((q+1)/2)·3=6(q+1)`. Since q and √(3q)=3^(m+1) are multiples of 3, the two Hall brackets are 1 modulo 3, and q+1 is 1 modulo 3.

The maximal subfield list is `R(q^(1/p))` for prime field-extension degree p; it may include `q₀=3`. That exceptional group is not simple, but the source identifies `R(3)≅PΓL₂(8)`; its order is 1512 and its 3-part is 27=q₀³. This is strictly below the full q³ 3-part for every q≥27. For q=27 specifically, the cited §2 is scoped to q>3, includes this subfield type, and §4.18 explicitly discusses the R(27) subgroup lattice. The paper's separate Möbius-function theorem's displayed n>3 scope is not substituted for the §2 maximal-list statement.

A proper H of 3-free index has full Sylow-3 order q³. It lies in a maximal proper M; by the cited exhaustive list and the strict comparisons above only a parabolic can contain that full 3-part. Consequently `[G:H]` is divisible by the index `q³+1` of its particular containing parabolic. With D=q³+1≥19684, §3.2 gives Sun8(G) conditional on Sun7(G) and the source structure. The exceptional `²G₂(3)` itself is not asserted simple or included in the m≥1 theorem; large Ree groups are not covered.

## 6. Competing 2025 order statement

The [2025 HTML source](https://arxiv.org/html/2510.06479v1) literally displays `q³(q+1)(q−1)` in §2.2, while describing the Sylow-3 normalizer of order q³(q−1) and a unital of q³+1 points on the natural Sylow-3 action. Those action/normalizer statements yield `q³(q³+1)(q−1)` by orbit–stabilizer, in agreement with Pierro's factorization and the 2016 explicit formula. The shorter displayed expression is therefore inconsistent **as returned by this HTML source**. I did not inspect its PDF or silently infer the authors' intended correction. The candidates do not use the shorter expression.

## 7. Independently executed bounded checks

### 7.1. Arithmetic, including proper and exceptional subfields

I independently wrote `frontier-20261028-review-f57-group-arithmetic.py`, SHA256 `3ca29fd0bca1e42ff73132eef15c2f258c3e96cd53e322f16425b7f51893fadb`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f57-group-arithmetic.py`.

For odd exponents n=3,5,7,9,15, the exact-integer program checks each displayed order divides the stated group order, the full p-part comparison, the torus factorization, the parabolic index, and **all** proper subfield powers allowed by the field exponent. This deliberately includes some nonmaximal proper subfields, a conservative order-comparison superset, not a claim they are maximal. Actual boundary outputs:

```text
Suzuki q=8:  |G|=29120; [G:B]=65; 2-parts B=64, dihedral=2, both Hall normalizers=4.
Suzuki q=512: [G:B]=262145; 2-parts B=262144, subfield Sz(8)=64.
Ree q=27: |G|=10073444472; [G:P]=19684; 3-parts P=19683,
          involution centralizer=27, four-group/Hall normalizers=3, subfield R(3)=27.
Ree q=19683: [G:P]=7625597484988; 3-parts P=7625597484987,
             subfield R(27)=19683, subfield R(3)=27.
```

All assertions in the five Suzuki and five Ree instances passed. The program's initial output called every proper subfield order a “maximal” order; that misleading output label was corrected to explicitly include all proper subfields and the bounded check rerun. The arithmetic was unchanged. Neither version proves maximal-list completeness, the group constructions, Sun5 or Sun7.

### 7.2. Independent Sz(8) matrix model

I separately wrote `frontier-20261028-review-f57-suzuki8-independent.py`, SHA256 `5fe56243f54684e674f06ba96fc1f8a3db4829a6f22bfc660e58fbcaec58822f`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f57-suzuki8-independent.py`.

This is a separate implementation using the source's matrices over F₂[x]/(x³+x+1), a 30,000-element cap and exact integer/bit arithmetic. It constructs the matrix group, all S(a,b) root matrices, verifies their closure and inclusion, constructs the root conjugacy orbit, and verifies a diagonal normalizer candidate by orbit–stabilizer. Observed:

```text
generators=5; generated group order=29120; root subgroup=64;
root conjugacy orbit=65; normalizer by orbit-stabilizer=448;
explicit F·H candidate size=448.
```

This independently reproduces the author's q=8 numerical interface, using the same published matrix definition, but does not enumerate all its subgroups or certify the all-q maximal classification. Both calculations are bounded exact code checks, not formal/human or cross-family reviews.

## 8. Disposition by claim

| Claim | Exact disposition |
| --- | --- |
| Suzuki candidate LF18–31, local parity lemma | NO_SUBSTANTIVE_DEFECT, finite G, 3∤|G|, Sun5(G), D≥8 odd-index condition |
| Suzuki LF33–54, all odd-index subgroups and Sun6/7/8 | NO_SUBSTANTIVE_DEFECT conditional on the complete source-stated classification and Sun5(G), m≥1 |
| Ree LF17–31, local p-free-index lemma | NO_SUBSTANTIVE_DEFECT for p∈{2,3,5}, D≥8 and Sun7(G) |
| Ree LF33–52, all 3-free subgroups and Sun8 | NO_SUBSTANTIVE_DEFECT conditional on the complete source-stated classification and Sun7(G), m≥1 |
| Small-field/subfield and competing-order qualifications | NO_SUBSTANTIVE_DEFECT at the source scopes above; classification proof and competing PDF remain NR |

No classification proof, Sun5/Sun7 proof closure, full scientific history or literature novelty has been independently reconstructed. No claim about all simple groups, all Ree types, an arbitrary-group Sun8 proof, or a new family exclusion is made. Parent must itself read the operative source and review bodies before any disposition. Historical process and quarantine findings remain historical, not retrospectively certified by this review.
