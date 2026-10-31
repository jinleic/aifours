# f33 — review of global-regular-band semigroup separation

**Verdict: NO_SUBSTANTIVE_DEFECT at the stated conditional scope.** For every nonempty regular weakly \(E\)-unitary semigroup whose idempotents form a global regular band, the author's algebraic argument proves the claimed actual-syntactic-quotient and canonical separation **conditional on SZ87**, whose published statement matches the hypothesis but whose proof is **NOT_RECONSTRUCTED** here. It includes all original-class monoids. This is same-harness written review plus one exact finite example, not a formal/kernel, independent-model, human, full-source, novelty or unrestricted original-target result.

Actual native prewrite observation: **Wed Oct 28 17:26:22 PDT 2026**, not an inferred completion or delivery clock.

## Bound source and registered definitions

- Assignment `institute/runs/three-area-2026-10-27-96h/review-waves/f33-semigroup-global-regular-band/assignment-v1.json`, SHA256 `bbd0f5d13b56fb66a983b3e850c7045d175df0e0c2e3ef56115d5cf3fc1937c0`.
- Candidate `mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-20261028-global-regular-band-separation-v1.md`, SHA256 `78fa8d588d1a7f44df9733baf95f14116145a4f77a5b1117e7f8383551009a82`, read all 114 LF through the ending.
- Registered weak-order and syntactic definitions: `semigroup-syntactic-idempotent-pure-CS-quotient-v2-elementary.md` SHA256 `93f216ee1a14cf9d4c9aca0de9d807efff3bbd39471d233a040423eb1ebfa968`, LF13–78. The book defines \(e\le a\) by actual idempotents \(f,g\) with \(e=fa=ag\); \(\tau\) tests idempotence in all \(S^1\) two-sided contexts.
- Registered physical multiplication and free-band presentation: `semigroup-syntactic-actor-universal-canonical-host-v1.md` SHA256 `788c2e31dbecc8ab8266abe08e94aae2ffd247eb7e2a0a7619d03fe899da24f4`, LF13–28 and LF136–171. I use these as named definitions, not as a blanket adoption of the old manuscript's all-host or actor-existence conclusions. The registered variety \(V\) consists of bands with regular-band local corners.
- The separate registered printed math-4 transcription `book-literal-math-4-v1.md` SHA256 `8627f8902cc9b89254997ede7f161225568ff77d25e6f33abe787e4520aeee2f`, LF35–100, and its erratum SHA256 `a9fa4669837ecd2bdca20017627f16adb13603bb0925276a0bbb501a72ee9c66` were read for the target and wording. Its five disputed Chinese function-word occurrences are unchanged in the erratum; I did **not** independently inspect the book images. The printed Question 1 asks for a seminormal-band/by-completely-simple product; the present review uses the registered explicit group-special-case physical convention, not a proof of equivalence of every product convention.
- I have prior semigroup/cross-domain project context and make no claim of blinding, first exposure, full cognition census or independence from all historical context. None of the historically held results is accepted as a premise and no old process outcome is retrospectively cured. No author contact or external model call was made.

## External import: exact statement matched, proof NOT_RECONSTRUCTED

The [publisher/Crossref abstract of M. B. Szendrei, *E-unitary regular semigroups* (1987), DOI 10.1017/S0308210500018229](https://doi.org/10.1017/S0308210500018229) explicitly states that every E-unitary regular semigroup with regular band of idempotents \(E\) embeds in a semidirect product of a band \(B\) by a group, with \(B\in\operatorname{var}(E)\). The abstract imposes no finiteness or identity condition. The author's [2019 survey, §5.1](https://arxiv.org/html/1909.05280v1#S5.SS1), identifies E-unitary orthodox semigroups via the unitary idempotent subset and records the regular-band embedding theorem. Its regular-band equation \(axya=axaya\) is the candidate's equation with renamed variables. The [same survey, §5.2](https://arxiv.org/html/1909.05280v1#S5.SS2), gives the Pastijn multiplication and states that its group-actor case is the ordinary band-by-group semidirect product.

I verified these **source statements only**. The original SZ87 proof was not read or reconstructed; this theorem remains an explicit **NR-SZ87 import**, not a newly established theorem here. The abstract and survey do not establish a modern exhaustive priority review. The later thesis mentioned by the author was not read and is not an additional premise of this review.

## Independent reconstruction of the internal argument

### 1. Weak \(E\)-unitarity implies the required unitary idempotent subset

Let \(E=E(S)\) be closed under multiplication. If \(b^3=b^2\), put \(d=b^2\); then \(d^2=d\) and \(d=db=bd\). The book's order uses the two actual idempotent witnesses \(d,d\), so weak \(E\)-unitarity forces \(b\in E\).

If \(ab\in E\), associativity gives \((ba)^3=b(ab)^2a=b(ab)a=(ba)^2\), and the previous observation gives \(ba\in E\). The reverse implication swaps \(a,b\). Now if \(e\in E\) and \(ea\in E\), cyclic idempotence gives \(ae\in E\); global closure of \(E\) makes \(z=(ae)(ea)=aea\) idempotent. Since \(z=(ae)a=a(ea)\), the two actual witnesses are \(ae,ea\in E\), so \(z\le a\) and weak \(E\)-unitarity forces \(a\in E\). The right-unitary implication follows symmetrically. Thus \(E\) is a two-sided unitary subset. Regularity plus its closure is exactly the orthodox condition used in the survey. No global natural-order compatibility, cancellation, finiteness or source identity is assumed.

### 2. The pure group coordinate has exactly the actual syntactic kernel

Apply SZ87 **conditionally** after the preceding hypothesis match. Write the injective homomorphism as \(\iota(s)=(b_s,\rho(s))\in B\rtimes G\), with \((b,g)(c,h)=(b\alpha_g(c),gh)\). In a band-by-group product, \((b,g)\) is idempotent iff \(g=1\): a group idempotent is 1, and \((b,1)^2=(b^2,1)=(b,1)\). Injectivity of \(\iota\) therefore gives
\[
\rho(s)=1\quad\Longleftrightarrow\quad s\in E(S).\tag{P}
\]
For each \(s\), regularity gives a mutual inverse \(s'\in S\), hence \(\rho(s')=\rho(s)^{-1}\). The nonempty image \(H=\rho(S)\) contains 1 and all inverses, so is a subgroup even if \(S\) is not a monoid.

If \(\rho(s)=\rho(t)\), every actual context \(x,y\in S^1\), including an absent factor interpreted as group identity, gives the same group image for \(xsy\) and \(xty\). By (P), they are simultaneously idempotent; hence \(s\,\tau\,t\). Conversely, if \(s\,\tau\,t\), use the **actual** left context \(s'\) and absent right context: \(s's\in E\), so \(s't\in E\); (P) implies \(\rho(s')\rho(t)=1\), hence \(\rho(s)=\rho(t)\). Therefore
\[
\tau=\ker(\rho\!:S\to H),\qquad j:S/\tau\xrightarrow{\cong}H,\quad j(q(s))=\rho(s).
\]
The kernel identity is independently valid whenever such an idempotent-pure group map exists; **its existence for the candidate's full class depends on SZ87**. In particular, this does not assume that the syntactic quotient is a group for every locally-r-orthodox source outside the stated global-band subclass.

### 3. Actual canonical presentation and equivariant witness

Since \(E\) satisfies the global regular-band identity, every band in \(\operatorname{var}(E)\) satisfies it; each of its local corners is an actual subband, so \(B\in V\). Identify \(C=S/\tau\) with the group \(H\) through \(j\) and restrict the genuine \(G\)-action to \(H\).

The registered physical product \(P(B,C)\), when the completely-simple actor is a group, has a single row and column and normalized sandwich entry 1. The registered mixed relation specializes to
\[
X_{u,s}X_{u q(s),t}=X_{u,st},\qquad u\in C,\ s,t\in S.
\]
The shift \(X_{u,s}\mapsto X_{vu,s}\) preserves every such relation and all \(V\)-identities; inverse shift gives actual automorphisms. Define on **all** generators
\[
h(X_{u,s})=\alpha_{j(u)}(b_s).
\]
The band coordinate of \(\iota(st)=\iota(s)\iota(t)\) is \(b_{st}=b_s\alpha_{\rho(s)}(b_t)\), whence
\[
h(X_{u,s})h(X_{u q(s),t})
=\alpha_{j(u)}(b_s\alpha_{\rho(s)}(b_t))
=\alpha_{j(u)}(b_{st})=h(X_{u,st}).
\]
Because the target \(B\) obeys every defining \(V\)-identity, this assignment factors through the **entire** presented band and is equivariant under every shift. For \(\beta(s)=[X_{1,s}]\), it gives \(h(\beta(s))=b_s\).

The canonical map \(\kappa_q(s)=(\beta(s),q(s))\) is a homomorphism by the displayed mixed relation at \(u=1\). If \(\kappa_q(s)=\kappa_q(t)\), then \(q(s)=q(t)\) gives \(\rho(s)=\rho(t)\), and applying \(h\) to \(\beta(s)=\beta(t)\) gives \(b_s=b_t\). Hence \(\iota(s)=\iota(t)\), and injectivity of \(\iota\) yields \(s=t\). This is a faithful actual \(V\)-band/group host over the **same source-defined quotient**, for all source elements, including both R- and L-idempotent pairs. Indeed all source idempotents have \(q(e)=1\), so the band coordinates themselves separate distinct idempotents in this subclass. No finite-alphabet restriction or hidden independent choice of q is used.

### 4. Original monoids and boundaries

If an original-class source has an identity 1, then \(1S1=S\). Its locally-r-orthodox hypothesis at that **actual** idempotent says \(S\) is orthodox and \(E(S)\) is a regular band, so the reviewed conditional theorem applies. It also applies to nonunital sources that have the global hypothesis. It does not claim every locally-r-orthodox source has globally regular \(E(S)\), or that the remaining subclass is nonempty.

A regular band is seminormal because every local corner is regular; a group is completely simple. The original printed target therefore follows on this subclass under the registered group-special-case product convention and SZ87. The direct host and same-q canonical statement are proved above at that boundary; there is no claim that the registered canonical formulation and the printed target are equivalent for the whole original class, or that Question 2 is solved.

## Independent finite check

Own, independently written `frontier-review-f33-semigroup-nonmonoid-check-v1.py`, SHA256 `9bf4c7ec8ddb4d45004ba101b69403aa6f90b2b1e14881e84d922b3fad02a752`, 81 LF/3608 bytes; no author checker imported. Ran from repository root:

```
python3 -B physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-review-f33-semigroup-nonmonoid-check-v1.py
```

Exit0. This constructs \(S=B\rtimes C_2\) with the **nonunital** 2×2 rectangular band \(B\), and the nontrivial automorphism that flips both row and column. The 8-element source has no identity, four idempotents and a two-element actor. It checked all 512 associativity triples, regularity, idempotent closure, regular-band identity, both-sided unitary \(E\), and the book's weak-order witnesses. For all 64 ordered element pairs and 81 formal-or-actual contexts each, the computed syntactic relation was exactly equality of group coordinates (32 ordered related pairs). It independently counted four ordered distinct same-q R-idempotent pairs and four L-idempotent pairs; the actual \((b,q)\) host is faithful. It checked all 128 group-position/source-product generator relations and 32 shift-equivariance instances. This is one constructed model, not a construction of all \(B_q\), not a proof of SZ87, and not an exhaustive semigroup search.

## Findings and nonclaims

- Candidate LF11–18, LF29–35: **NO_SUBSTANTIVE_DEFECT** in the global-band and weak-to-strong-E-unitary argument, and monoid inclusion.
- LF39–58: **NO_SUBSTANTIVE_DEFECT conditional on an actual pure group map** for \(\tau=\ker\rho\); the applicability of the group-model existence is **NR-SZ87**.
- LF60–93: **NO_SUBSTANTIVE_DEFECT conditional on SZ87** in the all-generator equivariant witness, canonical faithfulness and both same-q R/L separations; the group-special-case target convention is explicit.
- LF95–114: the author's own 10-element checker and its negative control were not independently read or replayed; the independent 8-element check above is separate. No inference is made about the general non-global-E residual, Question 2, full literature or novelty.

The published abstract/survey are statement-level source matches, not a reconstruction of the 1987 proof. Parent adoption, unrestricted all-source embedding, all-host obstruction, configured cross-family review, human review, formal verification and novelty remain outside this result.
