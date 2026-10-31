# f304 written review v1

## Verdict and scope

**Overall correctness: incorrect as written.** The fiber-measure theorem, corollaries, rough-kernel transfer, and conditional prime-lift density degeneration are **SUPPORTED**. One **MAJOR** overstatement remains: the lift does not preserve all point-multiplicity data, and its active-set collection is the downward closure of the old collection, not an established unchanged collection; this does not invalidate the exact density identity or the conditional absence of a uniform positive density lower bound.

**Finding count:** 0 FATAL / 1 MAJOR / 0 MINOR.  
**Confidence:** 0.98.

This is a same-harness written review, not independent-family, formal, human, novelty, or unrestricted Sun8 acceptance.

## Process and source binding

The administrative PRE-BODY ACK was sent after the manifest, freeze receipt, and all three manifest-listed status-only controls were read, and before any mathematical packet read. Actual `/bin/date` observations were:

- `2026-10-30T06:42:21-0700 PDT`
- `2026-10-30T06:45:16-0700 PDT`, after the complete packet read
- `2026-10-30T06:46:31-0700 PDT`, after reconstruction

No checkpoint interval approached 30 minutes.

Live metadata SHA256 checks matched:

- **Manifest:** `630bebaedc1914b10d934c253f2248257a952703887a19745f77a510a8f7bbc3`
- **Freeze receipt:** `32561bfa63e7ee15ce8ff15aa823635224f2e0a9daa9dd17c2f9fd94262aedc2`
- **Literal packet:** `f57fac1afb02de1f45c95aa8d833d4df0793ed725878e4aa3a94f014af813cc1`
- **S1**, `frontier-20261030-fiber-measure-additive-correction-v1.txt`: `346d50517d64d4aeeb6be17ac8e391e0900e4c2638051325215dcb175e17a9a3`; all source LF 1–152 read first.
- **S2**, `frontier-20261030-fiber-measure-incidence-bridge-v1.txt`: `a6c9841d4d089ff4da3122d4bbd4a4629fb0dbda653ed6a2991f501faced6b6a`; all source LF 1–204 read second.

The complete literal packet, physical LF 1–358 including both source endings, was read raw in nonoverlapping windows of at most 20 LF. There were no returned elisions. All source citations below refer to source LF, not packet LF.

S1 and S2 reside under:

`/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`

The three status controls were used administratively only. No excluded link, held payload, prior review body, failed-provider transcript/progress, author code, scientific executable, interpreter, CAS, solver, enumeration, replay, selected group/prime/state, or voluntary numerical example was used. One unsolicited separate-wave administrative ACK was delivered; it contained no mathematical packet and supplied no mathematical premise.

No external-model CLI, configuration, or account change was made. The f265/f259 labels and source-order references in the packet were not independent imported premises: all operative algebra is reconstructed below from the complete supplied bodies and elementary group/index/counting arguments.

## Finding F1 — MAJOR

**Title:** Restrict incidence preservation to the nerve and maximum multiplicity

**Priority:** 2  
**Confidence:** 0.99  
**File path:** `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261030-fiber-measure-additive-correction-v1.txt`  
**Line start:** 102  
**Line end:** 104  
**Related reuse:** LF 125–128

**Body:** The formula at LF 99–101 gives \(S'(q,x)=S(q)\cap\{i:x_i=0\}\), so the attainable active-set collection is exactly the downward closure of the old collection; equality with the old collection requires an additional downward-closure property not supplied here. Moreover, under the theorem’s own hypothetical-family premise, the normalized average multiplicity changes strictly from \(\sum_i1/a_i\) to \(\sum_i1/(a_ip_i)\), since every \(a_i\) is positive and every \(p_i>1\). Thus “every point-multiplicity datum is preserved” is false if it includes the multiplicity distribution, and “no new [active set] arises” does not follow. Retain preservation of the overlap graph, nonempty subset-intersection pattern, old active-set realizability, and maximum multiplicity; remove the stronger preservation claim and its reuse in the scale-free discussion. The density degeneration theorem does not require the stronger assertion.

## Assumptions and acceptance ceiling

All groups are arbitrary unless explicitly passed to a finite quotient; all subgroup indices used are finite positive integers; cosets are actual nonempty left cosets; \(N\) is normal. Repeated subgroups and index values are allowed.

\(B_7(X)\le7\) is used exactly as defined at S2 LF 25–30: eight disjoint finite-index left cosets force some index gcd at least eight. The kernel capacity conclusion additionally assumes \(B_7(N)\le7\).

The lifting theorem assumes an actual bad eight-family and both factor bounds; that existence premise is not discharged. Primes remain universally quantified, distinct, greater than seven, and outside the finite forbidden divisor set.

No unrestricted Sun8 or extension-closure conclusion is accepted.

## Per-claim reconstruction

### 1. L1 — SUPPORTED

**Source:** S2 LF 35–38.

For \(U\le G\), normality of \(N\) makes \(NU\) a subgroup. The quotient correspondence gives
\[
[G:NU]=[Q:\pi(U)]=a.
\]
The map
\[
n(U\cap N)\longmapsto nU
\]
is a bijection \(N/(U\cap N)\to NU/U\), giving
\[
[NU:U]=b,\qquad [G:U]=ab.
\]

The product
\[
\gcd(a_i,a_j)\gcd(b_i,b_j)
\]
divides both \(a_ib_i\) and \(a_jb_j\), hence their gcd. This argument does not require \(U\) normal, finite \(G\), or distinct subgroup labels.

### 2. L2 — SUPPORTED

**Source:** S2 LF 40–48.

For \(H=\bigcap_iW_i\), the left-coset map
\[
X/H\longrightarrow\prod_iX/W_i
\]
is injective, so \([X:H]\) is finite and at most \(\prod_id_i\). Each \(d_i\) divides \([X:H]\); pairwise coprimality therefore makes their product divide \([X:H]\). Equality of the two finite cardinalities makes the map onto.

Any prescribed tuple of actual left cosets consequently meets. Indices one and repeated whole-group factors cause no exception. In particular, disjoint actual cosets cannot have coprime indices.

### 3. L3 — SUPPORTED

**Source:** S2 LF 50–56.

Each \(\operatorname{core}_X(H_i)\) has finite index, by the action on the finite coset set. Their finite intersection \(M\) is finite-index normal and lies in every \(H_i\).

Each coset \(x_iH_i\) is the full preimage of its image in \(X/M\). Images of disjoint cosets therefore remain disjoint, and
\[
[X/M:H_i/M]=[X:H_i].
\]
Finite counting gives the reciprocal-index sum at most one.

Repeated subgroups present no issue because their actual cosets remain disjoint. An index-one coset fills \(X\) and leaves no room for another nonempty disjoint coset. Infinite \(X\) is handled by the same finite quotient, not by cardinal division. The empty-family bound, if needed, is the empty sum.

### 4. L4 — SUPPORTED

**Source:** S2 LF 58–65.

Fix an arbitrary \(q\) and one common \(t\) over \(q\). For every active label \(l\) and \(x_l\in C_l\cap Nt\), both membership conditions give
\[
C_l\cap Nt=x_l(U_l\cap N)=x_lK_l.
\]
Right multiplication by the same \(t^{-1}\) gives
\[
(C_l\cap Nt)t^{-1}=(x_lt^{-1})(tK_lt^{-1}).
\]

Both factors lie in \(N\); conjugation by \(t\) preserves \(N\) and the subgroup index \(b_l\). Right multiplication is bijective, so disjointness of the original cosets gives simultaneous disjointness of all these actual left \(N\)-cosets.

Using a single \(t\) is essential and is respected. No normality of \(U_l\) is used.

### 5. L5 and Step 0 — SUPPORTED with finite-quotient density

**Sources:** S2 LF 67–72; S1 LF 70–75.

Let
\[
R=\bigcap_i\operatorname{core}_G(U_i),\qquad
\bar G=G/R,\qquad
\bar N=NR/R,\qquad
\bar Q=G/NR=Q/\pi(R).
\]
Then \(\bar N\cong N/(N\cap R)\), and \(\bar Q\) is a quotient of \(Q\).

Because \(R\le U_i\), the original cosets are full inverse images of their \(\bar G\)-images and retain \(n_i\). Because \(\pi(R)\le\pi(U_i)\), the quotient images \(A_i\) are full inverse images of their \(\bar Q\)-images and retain \(a_i\) and every subset-intersection nonemptiness question. Also,
\[
U_i\cap NR=(U_i\cap N)R,
\]
which preserves \(b_i\).

A quotient inherits \(B_7\) by pulling back any hypothetical disjoint coset family, with unchanged indices. Hence both factor bounds pass to \(\bar N\) and \(\bar Q\).

For infinite \(Q\), the density notation must mean **finite-quotient density**, not a ratio of infinite cardinalities. With \(T=\pi(R)\), every \(A_i\) and their finite intersections are \(T\)-saturated; define their density by normalized counting in finite \(Q/T\). This is independent of the chosen admissible finite normal quotient: under a common refinement, numerator and denominator multiply by the same fiber size.

Thus all densities used in the proof are genuinely preserved by finite-core reduction, without an amenability assumption. The resulting finite representative suffices for the conditional existence statement; pulling the cylinders back also gives the corresponding construction over the original group with this same density interpretation.

### 6. T1.1–T1.3 — SUPPORTED

**Source:** S2 LF 74–93.

At each arbitrary \(q\), L4 supplies disjoint left \(N\)-cosets of indices \(b_i\) for exactly the active labels. L3 gives
\[
\sum_{i\in S(q)}\frac1{b_i}\le1.
\]

If at least eight labels are active and \(B_7(N)\le7\), any eight slices have pairwise index gcds dividing the corresponding original gcds, hence at most seven, contradicting the kernel factor bound. Thus
\[
|S(q)|\le7.
\]

Empty active sets, repeated subgroups, and \(b_i=1\) are all covered: a unit-index active slice consumes the whole fiber.

The integration assertion at **S2 LF 95–98** is **SUPPORTED** with the finite-quotient interpretation: integrating the pointwise sum gives
\[
\sum_i\frac1{b_i}\frac1{a_i}=\sum_i\frac1{n_i}.
\]

The “strictly stronger” and “independent” remarks are supported only as comparisons of the numerical inequalities, not as a proved logical separation within the entire bad-family hypothesis class. At that stronger interpretation they are **INCONCLUSIVE** and not used here.

In particular, the equal-index sentence at LF 98–100 supplies no admissible bad-family witness: for any common kernel index \(b\), the pairwise gcd restriction gives \(b\le7\), while eight equal reciprocal terms satisfying the measure bound require \(b\ge8\). No such witness is asserted or instantiated by this review.

### 7. C1–C3 — SUPPORTED at their conditional scopes

**Source:** S2 LF 102–126.

**C1.** If \(b_i=1\), any point shared with another image would contribute \(1+1/b_j>1\) to the fiber sum, so that image is isolated from every other image.

**C2.** Pairwise-coprime \(a_i\) within \(J\) let L2 find one common quotient point for all corresponding image cosets. T1.1 gives
\[
\sum_{i\in J}\frac1{b_i}\le1.
\]
L2 applied to each pair of disjoint slices gives kernel gcd at least two, while L1 bounds it by the original gcd at most seven. The cardinality conclusion \(|J|\le7\) additionally uses \(B_7(N)\le7\), exactly as T1.2 does.

**C3.** Write
\[
d_A=\gcd(a_i,a_j),\quad
d_B=\gcd(b_i,b_j),\quad
g=\gcd(n_i,n_j).
\]
L1 gives \(d_Ad_B\mid g\). If \(d_A=1\), L2 forces image intersection; intersection gives two disjoint slices and thus \(d_B\ge2\), excluding \((d_A,d_B)=(1,1)\).

For intersecting images, \(d_B\ge2\) together with \(d_Ad_B\le g\le7\) gives \(d_A\le3\). For disjoint images, L2 gives \(d_A\ge2\), and divisibility gives \(d_A\le7\). When \(d_A\ge4\), the only possible multiple \(g\) of \(d_A\) not exceeding seven is \(d_A\) itself, forcing \(d_B=1\) and \(g/d_A=1\). The latter equality is not asserted for other cases.

These are necessary pair restrictions, not a sufficiency/existence classification.

### 8. Lemma K — SUPPORTED

**Source:** S1 LF 33–58.

The reconstructed statement is:

> For arbitrary \(X\) satisfying \(B_7(X)\le7\) and finite \(K\) with \(\gcd(|K|,210)=1\), one has \(B_7(X\times K)\le7\).

Abelianity of \(K\) is unnecessary.

Suppose an eight-coset counterfamily existed. With \(M=\{1\}\times K\), L1 gives each index as \(a_lb_l\), where
\[
b_l=[M:W_l\cap M]\mid |K|.
\]

If two projections meet, L4 with one common fiber representative gives disjoint actual \(M\)-cosets of indices \(b_i,b_j\). L2 forces \(\gcd(b_i,b_j)>1\). A prime divisor of that gcd divides \(|K|\) and hence exceeds seven; consequently \(\gcd(b_i,b_j)>7\). But this gcd divides
\[
\gcd(a_ib_i,a_jb_j)\le7,
\]
a contradiction.

Thus all eight projections are disjoint actual \(X\)-cosets, with pairwise index gcds still at most seven, contradicting \(B_7(X)\le7\).

This also handles repeated/unit indices and infinite \(X\). It supplies the exact finite-abelian direct-product transfer needed later, without relying on the unread f259 body.

### 9. Prime lift: actual groups, cosets, indices, and factor bounds — SUPPORTED

**Source:** S1 LF 62–98.

After Step 0, only finitely many prime divisors are forbidden. Infinitely many primes therefore remain above any prescribed bound; the assertion applies to every admissible distinct tuple and uses no selected tuple.

In
\[
G'=G\times\prod_i C_{p_i},
\]
the subgroup \(N'=N\times\{0\}\) is normal and isomorphic to \(N\). Each \(U_i'\) is an actual product subgroup, and
\[
C_i'=C_i\times\{0\}_i\times\prod_{j\ne i}C_{p_j}
\]
is its actual left coset. Disjointness follows already from the \(G\) coordinate.

The index is \(n_ip_i\). Freshness and distinctness give
\[
\gcd(n_ip_i,n_jp_j)=\gcd(n_i,n_j),
\]
so the assumed bad family remains bad. Kernel intersection gives \(b_i\) unchanged; the quotient image subgroup has index \(a_ip_i\).

The first factor bound persists by the isomorphism \(N'\cong N\). The second persists because
\[
Q'=Q\times K,\qquad K=\prod_iC_{p_i},
\]
where \(K\) is finite with order coprime to 210, and Lemma K applies.

No \(B_7(G')\) bound is asserted: the lifted bad family would contradict such a bound.

### 10. Projected incidence and multiplicity — PARTLY SUPPORTED / PARTLY REFUTED

**Sources:** S1 LF 95–105, 125–128.

The displayed image formula is **SUPPORTED**. More generally, for every nonempty label subset \(J\), its image intersection is the old intersection times zero coordinates on \(J\) times unrestricted coordinates off \(J\). Thus all subset-intersection nonemptiness data, in particular the overlap graph and its cliques, are unchanged.

The formula
\[
S'(q,x)=S(q)\cap\{i:x_i=0\}
\]
is **SUPPORTED**. Every old active set is realized by the zero-coordinate fiber, every lifted active set is a subset of an old one, and maximum multiplicity is unchanged.

The asserted preservation of all active sets/all point-multiplicity data is not supported; the distribution-preservation reading is **REFUTED** by the strict first-moment change in F1.

For an arbitrary original active set \(S\) and arbitrary \(T\subseteq S\), the number of coordinate tuples realizing exactly \(T\) is
\[
\prod_{i\in S\setminus T}(p_i-1)\prod_{i\notin S}p_i,
\]
which is positive. This proves the downward-closure description without selecting a group, tuple, or pattern.

Exact active-set equality would require the old collection to be downward closed, an additional unproved condition. Hence the construction establishes invariance of graph/nerve/maximum-based statements, not invariance of every possible multiplicity statement.

### 11. Exact density shrinkage and delta bound — SUPPORTED

**Source:** S1 LF 106–123.

For each distinct pair, the lifted intersection has cardinality
\[
|A_i\cap A_j|\prod_{k\notin\{i,j\}}p_k,
\]
while
\[
|Q'|=|Q|\prod_kp_k.
\]
Its normalized density is therefore exactly the original density divided by \(p_ip_j\). The same identity holds for canonical finite-quotient densities when the original groups are infinite.

Each original pair density is at most one, so summing over the 28 pairs gives total density at most
\[
\frac{28}{\min_{i\ne j}(p_ip_j)}.
\]
For every \(\delta>0\), every admissible tuple with all
\[
p_i>\sqrt{28/\delta}
\]
makes that bound strictly less than \(\delta\). No multiplicity-distribution invariance is needed.

Consequently, **if** the class of bad eight-families under the two factor bounds is nonempty, its total relative quotient-overlap densities have infimum zero. There is then no positive constant \(\delta\), uniform across this class of groups/extensions/families, which lower-bounds that total density.

If the class is empty, such a proposed necessary condition is vacuous. This is not a denial of index-dependent or group-dependent density bounds.

### 12. Withdrawals and nonclaims — SUPPORTED as scope restrictions

**Sources:** S1 LF 13–31, 116–133, 146–152.

The original Theorem 2 at S2 LF 128–180 is withdrawn, not accepted through its index-number relaxation. Its proof of non-implication and its closure language supply no premise to this review. W2 likewise limits Theorem 1 to configurations violating its actual capacity/measure inequalities, not a whole rich-overlap regime.

The corrected conditional density theorem does not establish existence of a bad family, non-implication from a constraint list, a universal scale-free-method no-go, or unrestricted Sun8. It preserves graph/nerve/maximum data but, after F1, cannot claim preservation of all point-multiplicity data. No new conclusion on those larger questions is supplied.

## Disposition

Accept as reconstructed written conditional mathematics:

- L1–L5;
- T1.1–T1.3;
- C1–C3 as necessary constraints, with the stated extra factor assumption where needed;
- Lemma K;
- the actual fresh-prime group/coset construction and both factor bounds;
- unchanged index gcds and kernel indices;
- unchanged intersection nonemptiness and maximum multiplicity; and
- exact conditional density degeneration.

**Require an additive correction to S1 LF 102–104 and 125–128 before adopting the complete corrected packet.** Keep the full-hypothesis strictness/independence interpretation outside the accepted scope.

No unrestricted conjecture, existence, non-implication, blanket scale-free no-go, novelty, or independent-family verdict follows.