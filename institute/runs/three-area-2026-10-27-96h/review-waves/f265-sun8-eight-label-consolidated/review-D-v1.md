**File-delivery blocker:** `functions.write` rejected the assigned filesystem path; it accepts only `local://` scratch files and `xd://` devices. The device inventory contains only Gmail/Slack operations, and this assignment prohibits shell editing and creating another file. **No review file was created or source modified.** The completed review below is ready for the parent’s authorized file writer. It supersedes the unpublished, rejected draft: the cosmetic notation suggestion is **not** a defect.

# f265 review D — conditional finite-image-nilpotent specialization

## Verdict

**SUPPORTED at the explicitly conditional, necessary-representation scope.**

**FATAL 0 / MAJOR 0 / MINOR 0.**

Under the original hypotheses \(B_7(N)\le7\), \(B_7(Q)\le7\), and the **additional** assumption that every finite quotient of \(N\) and of \(Q=G/N\) is nilpotent, candidate Section 6 correctly obtains its small-factor quotient incidence representation and corresponding actual disjoint kernel slices.

The high-coordinate choices are simultaneous for all active labels, not chosen separately for pairs. The transferred kernel sets are genuine **left cosets of conjugated subgroups**, with the claimed indices. No abelian-factor, split-extension, finite-original-\(G\), or original-subgroup-normality assumption is required. No independent local gluing step or upgrade to \(B_7\le2\) occurs.

This is same-harness written reconstruction only, not acceptance of unrestricted Sun8, novelty, provenance, human verification, or formal verification.

## Clock and scope

Native `/bin/date` observed after every declared input had been displayed and before the initial composition:

**Thu Oct 29 16:09:50 PDT 2026**

Native `/bin/date` before this corrected final composition:

**Thu Oct 29 16:22:27 PDT 2026**

Neither timestamp is backdated.

The whole candidate was read. Mathematical dispositions here cover Section 6, **LF209–264**, its shared Section 1 prerequisites, **LF37–93**, and the framing and limitations relevant to this slice. The remaining obligations of Sections 2–5 and 7 are not adjudicated here; no sibling review output was read.

## Shared prerequisites independently reconstructed

### 1. Actual subgroup indices — SUPPORTED

Candidate **LF37–50**.

Let \(C_i=g_iU_i\), \(K_i=U_i\cap N\), \(V_i=\pi(U_i)\), and \(A_i=\pi(g_i)V_i\). Normality of \(N\) makes \(NU_i\) a subgroup, and
\[
[G:U_i]=[G:NU_i][NU_i:U_i].
\]
The quotient correspondence gives \([G:NU_i]=[Q:V_i]=a_i\). The left-coset-set bijection
\[
N/K_i\longrightarrow NU_i/U_i,\qquad nK_i\longmapsto nU_i
\]
gives the second index \(b_i\). Thus \(n_i=a_ib_i\), with both factor indices finite. This does not assert that \(N\), \(K_i\), or \(A_i\) is finite.

### 2. One common lift gives actual left kernel cosets — SUPPORTED

Candidate **LF54–61**, extended to any simultaneously active label set.

If \(q\in\bigcap_{i\in S}A_i\), choose **one** lift \(t\) and, for each \(i\in S\), \(x_i\in C_i\cap Nt\). Since \(C_i=x_iU_i\) and \(Nt=x_iN\),
\[
C_i\cap Nt=x_iK_i.
\]
Therefore
\[
(C_i\cap Nt)t^{-1}
=(x_it^{-1})(tK_it^{-1}).
\]
Here \(x_it^{-1}\in N\), \(tK_it^{-1}\le N\), and its index in \(N\) equals \(b_i\). The translated cosets are pairwise disjoint because the original \(C_i\) are disjoint.

The subgroup is the **conjugate** \(tK_it^{-1}\), not necessarily \(K_i\). No normality of \(U_i\) or extension section is used.

### 3. Disjoint finite-index cosets cannot have coprime indices — SUPPORTED

Candidate **LF63–72**.

For subgroups \(H_i\le X\) of pairwise-coprime finite indices \(d_i\), the natural map
\[
X/\bigcap_iH_i\longrightarrow\prod_iX/H_i
\]
is injective. Hence the intersection index is finite and at most \(\prod_i d_i\). Each \(d_i\) divides that intersection index, so their product divides it. Equality follows, making the map surjective. Every prescribed tuple of left cosets therefore has a common point.

In particular, disjoint finite-index left cosets have index gcd at least two. Together with the bad-family hypothesis, every original pair has gcd in \(\{2,3,4,5,6,7\}\).

### 4. Finite-core reduction preserves the needed actual data — SUPPORTED

Candidate **LF84–93**.

Set \(R=\bigcap_i\operatorname{core}_G(U_i)\). It is normal of finite index and lies in every \(U_i\), so \(\bar G=G/R\) is finite and each \(C_i\) is the full inverse image of its image. Disjointness and the indices \(n_i\) survive.

Moreover, \(\pi(R)\le V_i\), so every \(A_i\) is the full inverse image of its image under \(Q\to Q/\pi(R)=\bar Q\). All \(a_i\) and **every subset-intersection nonemptiness question** survive.

For the kernel data,
\[
NR\cap U_i=(N\cap U_i)R=K_iR.
\]
Also \(N\cap K_iR=K_i\), since \(N\cap R\le K_i\). Thus
\[
[\bar N:\bar K_i]=[N:K_i]=b_i.
\]
Finally,
\[
\bar N\cong N/(N\cap R),\qquad \bar Q\cong Q/\pi(R),
\]
so these are genuine finite quotients of the original factors.

### 5. Factor bounds pass to quotients — SUPPORTED

Candidate **LF92–93**.

Pulling back disjoint left cosets from a quotient produces disjoint left cosets of preimage subgroups, with unchanged indices. Hence \(B_T(X)\le r\) implies the same bound for every quotient of \(X\).

## Per-claim dispositions for Section 6

### D1. Nilpotency of the finite factors — CONDITIONAL, with condition explicit

Candidate **LF211–220**.

The extra hypothesis concerns **every finite quotient of \(N\) and every finite quotient of \(Q\)**. The groups \(\bar N,\bar Q\) above are such finite quotients, so they are nilpotent. No nilpotency of \(\bar G\) follows or is needed.

The proof would need only nilpotency of these particular two finite images, but the stronger stated hypothesis is sufficient and is not a hidden assumption.

### D2. Primary splitting of groups, subgroups, and left cosets — SUPPORTED

Candidate **LF218–225**.

Write a finite nilpotent group as \(X=\prod_pX_p\), its direct product of Sylow subgroups. For \(h=(h_p)\in H\le X\), choose an integer exponent that is \(1\) modulo \(|X_p|\) and \(0\) modulo each other Sylow-factor order. Its power of \(h\) extracts \(h_p\) inside \(H\). Consequently,
\[
H=\prod_p(H\cap X_p),\qquad
xH=\prod_p x_p(H\cap X_p).
\]
These statements do not require the Sylow factors to be abelian: different direct factors commute, and the power operation is on a single element.

Indices split accordingly. In particular, with
\[
V_{i,p}=\bar V_i\cap Q_p,\qquad K_{i,p}=\bar K_i\cap N_p,
\]
the local indices are the corresponding prime-power parts of \(a_i,b_i\).

### D3. High-prime uniqueness — SUPPORTED

Candidate **LF227–229**.

For \(p>7\), two labels with \(p\mid n_i,n_j\) would have original gcd at least \(p>7\). Thus at most one label \(i_p\) has \(p\mid n_{i_p}\).

Since \(a_i,b_i\mid n_i\), a proper \(V_{i,p}\) or proper \(K_{i,p}\) is possible only for that label. In particular, if both a proper quotient component and proper kernel component occur at the same high prime, they belong to the same original label. Repeated labels or repeated original subgroups do not invalidate this argument.

### D4. The entire quotient intersection hypergraph survives — SUPPORTED

Candidate **LF230–234**, using the finite-core preservation above.

For every label subset \(J\),
\[
\bigcap_{i\in J}\bar A_i
=
\left(\bigcap_{i\in J}A_i^{\rm small}\right)
\times
\prod_{p>7}\left(\bigcap_{i\in J}A_{i,p}\right).
\]
At each high prime, the intersection on the right is either the full factor or its one constrained coset. It is always nonempty. Thus the full intersection is nonempty exactly when its small-factor intersection is nonempty.

This works for every subset, not only pairs. The finite-core step transfers the same equivalence back to the original quotient images.

### D5. High-coordinate selection is simultaneous for all active labels — SUPPORTED

Candidate **LF236–240**.

Fix \(q_{\rm small}\) and let
\[
S=\{i:q_{\rm small}\in A_i^{\rm small}\}.
\]
For each \(p>7\), choose \(q_p\) in the unique constrained quotient coset if its label belongs to \(S\); otherwise choose any point of \(Q_p\). For every \(i\in S\), every high-coordinate constraint for that label is then satisfied. The resulting single
\[
q=(q_{\rm small},(q_p)_{p>7})
\]
belongs to all \(\bar A_i\), \(i\in S\), at once.

There is no per-pair choice here. Constraints at different high primes are independent coordinates, and at any one coordinate there is at most one constrained label. Labels outside \(S\) cannot become active because their small-coordinate condition fails.

### D6. Projected kernel slices are actual disjoint left cosets with the correct indices — SUPPORTED

Candidate **LF240–247**.

For the one \(q\) above, choose one lift \(t\in\bar G\). The shared fiber lemma gives disjoint actual left cosets
\[
D_i=y_i(t\bar K_it^{-1})\subseteq\bar N,\qquad i\in S.
\]
Each Sylow subgroup \(N_p\) is characteristic in the nilpotent group \(\bar N\). Since \(\bar N\triangleleft\bar G\), conjugation by \(t\) preserves each \(N_p\), and hence \(N_{\rm small}\).

Writing \(K_i^{\rm small}=\bar K_i\cap N_{\rm small}\), the small projection is
\[
D_i^{\rm small}
=
y_i^{\rm small}\bigl(tK_i^{\rm small}t^{-1}\bigr).
\]
It is therefore an actual **left coset** of a subgroup of \(N_{\rm small}\), with index
\[
[N_{\rm small}:tK_i^{\rm small}t^{-1}]
=[N_{\rm small}:K_i^{\rm small}]
=b_i^{\rm small}.
\]

For two labels in \(S\), their high kernel components intersect at each high prime because at least one is the full factor. Their whole high-factor projections therefore intersect. If their small projections also intersected, the product decomposition would give a point in \(D_i\cap D_j\), contradicting original disjointness. Hence the small projections remain pairwise disjoint.

This argument correctly retains the conjugated subgroups; it does not identify them with unconjugated \(K_i^{\rm small}\).

### D7. Small indices and gcd transfer — SUPPORTED

Candidate **LF249–252**, equation (6.1).

Primary splitting gives
\[
a_i^{\rm small}=\prod_{p\le7}p^{v_p(a_i)},\qquad
b_i^{\rm small}=\prod_{p\le7}p^{v_p(b_i)}.
\]
Therefore \(m_i=a_i^{\rm small}b_i^{\rm small}\) is exactly the part of \(n_i=a_ib_i\) supported on primes at most seven.

Since every original pairwise gcd is already in \(\{2,3,4,5,6,7\}\), removing high-prime factors does not change it:
\[
\gcd(m_i,m_j)=\gcd(n_i,n_j).
\]
This also implies \(m_i>1\).

For the transferred kernel cosets specifically,
\[
\gcd(b_i^{\rm small},b_j^{\rm small})
\mid\gcd(m_i,m_j)\le7.
\]
For the quotient small cosets the analogous divisibility holds with \(a_i^{\rm small}\).

### D8. Original factor bounds and their two consequences — SUPPORTED

Candidate **LF254–257**.

The small factors are quotient groups of \(\bar N,\bar Q\), which are quotients of \(N,Q\). Thus both inherit **\(B_7\le7\)**.

If all eight labels were active at some \(q_{\rm small}\), D5–D6 would give eight disjoint actual kernel small cosets, whose pairwise index gcds are at most seven by D7. This contradicts \(B_7(N_{\rm small})\le7\).

If all eight quotient small cosets were pairwise disjoint, their pairwise index gcds would likewise be at most seven, contradicting \(B_7(Q_{\rm small})\le7\).

Neither conclusion requires \(B_7\le2\). As the manuscript’s later discussion also recognizes, the corresponding two exclusions in the full factors already follow from the original bounds without nilpotency. The extra hypothesis supplies the **small-factor representation**, not a stronger graph-theoretic conclusion.

### D9. No independent local gluing or separate small extension — SUPPORTED as a limitation

Candidate **LF259–264**, consistent with **LF307–316**.

The choices of full quotient point, lift, representatives, and conjugated kernel subgroups remain tied to the same actual extension and original cosets. No step combines independently chosen data at different \(q_{\rm small}\), identifies the resulting conjugates across fibers, or constructs a new extension with kernel \(N_{\rm small}\) and quotient \(Q_{\rm small}\).

The candidate expressly disclaims arbitrary local gluing and separate small-extension realization. Section 6 is therefore only a necessary incidence representation, not a sufficient condition or a small-group reduction of the unrestricted problem.

## Hidden-assumption audit

| Potential hidden assumption | Conclusion |
|---|---|
| Abelian \(N,Q\) or abelian Sylow factors | Not used; component extraction and coset products work in nonabelian direct factors. |
| Split extension | Not used; lifts are arbitrary, not a homomorphic section. |
| Finite original \(G\) | Not used; the exact finite-core quotient supplies the finite groups. |
| Normal original \(U_i\) | Not used; the common lift produces the required conjugated kernel subgroups. |
| Distinct original subgroups | Not used; labels may repeat. |
| Nilpotent \(\bar G\) | Not used; only \(\bar N,\bar Q\) are assumed nilpotent. |
| Stronger factor bound \(B_7\le2\) | Not used. |
| Independent realizability/gluing of local slices | Neither used nor claimed. |

## Findings

**None in Obligation D’s mathematical scope.** There is no LF-located mathematical defect to report.

The transition to finite barred groups followed by lighter notation is understandable from **LF212–220** and the preservation lemmas; it does not constitute a defect or merit a MINOR count.

## Provenance and assurance — INCONCLUSIVE

The owner’s exposure report at **LF326–335** is status-only. It cannot certify clean cognition, non-influence, clean provenance, or independence from prior methods. No protected material was opened or compared, and no historical hold is rehabilitated.

All mandatory overlays and errata were read before the candidate. Their references to undeclared sources were not followed. The supplied parent disposition is same-harness support at its own scope, not adoption of this candidate.

The whole candidate was read; claims belonging exclusively to sibling obligations remain unadjudicated here. No sibling report, external source/model, checker, replay, solver, mathematical program, or selected finite-instance control was used.

Process disclosures: initial progress commentary was emitted despite the no-progress instruction. The first attempt to write the report was rejected by the tool and did not create a file. The subsequent tool-device listing was consulted only to seek an authorized output route; it contained no additional mathematical evidence.

## Coverage receipt

Manifest hash checked before opening it:

- SHA-256: **c80d5df02be872ff31b34cfa5ca629d27c84eabffb9d7caf76b375ae2f37c23c**
- **6108 bytes / 77 LF**
- Initially displayed as `1–77:raw`; the manifest is separate from its eight declared input bodies.

All eight declared inputs were SHA-256/byte/LF checked **before any of their bodies were opened**. Every measurement matched. Their complete bodies were then displayed in the listed order, using raw windows no longer than fifteen lines, including their actual endings. No mathematical assessment preceded completion of those input reads.

For rows 1–6 and 8, the path prefix is:

`/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`

For row 7, the prefix is `/Users/jinleic/repos/aifours/`.

| # | Input | Full SHA-256 | Bytes / LF | Raw windows displayed |
|---|---|---|---|---|
| 1 | frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json | 6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793 | 6883 / 56 | 1–15, 16–30, 31–45, 46–60; actual ending LF56 |
| 2 | frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json | bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04 | 3056 / 11 | 1–15; actual ending LF11 |
| 3 | frontier-20261028-alternating-p7-cardinality-addendum-v1.json | 6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218 | 3164 / 10 | 1–15; actual ending LF10 |
| 4 | frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json | 775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e | 2329 / 12 | 1–15; actual ending LF12 |
| 5 | frontier-20261029-f254-review-b-five-minor-additive-erratum-v1.txt | d95c7cecf5b39e6d6649f1ca0238acf661f79082be4f8ba3a2ceb9757591244b | 10485 / 181 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195; actual ending LF181 |
| 6 | frontier-20261029-f253-review-b-gcd-additive-erratum-v1.json | c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3 | 2825 / 25 | 1–15, 16–30; actual ending LF25 |
| 7 | institute/runs/three-area-2026-10-27-96h/dispositions/math-6-sun8-rough-finite-quotient-arbitrary-kernel-transfer-parent-v1.md | 8feffe5bd9917b83469548880431e55e71a81ecb9bd21e8eaf43e946411b286b | 6216 / 28 | 1–15, 16–30; actual ending LF28 |
| 8 | frontier-20261029-eight-label-extension-consolidated-v1.txt | 3b5b1c6b31c74f71ed0dfcb0ec93b2a0aa78f47478559be4fb3a70a86c6ec4e9 | 20185 / 356 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195, 196–210, 211–225, 226–240, 241–255, 256–270, 271–285, 286–300, 301–315, 316–330, 331–345, 346–360; actual ending LF356 |

Candidate **LF196–210** was subsequently reread, again raw, to establish the precise section boundary.

## Explicitly open items

- **Unrestricted Sun8:** unresolved by this review.
- **Finite-simple residual:** not disposed of; no finite-simple exclusion is derived or inherited.
- **Existence or exclusion of eight-coset bad families:** unresolved here, including whether Section 6’s necessary representation can occur under its hypotheses.
- **Realization and local-to-global gluing:** not proved; no separate small extension is constructed.
- **Nonnilpotent finite factor images:** outside this specialization.
- **Novelty and priority:** unassessed.
- **Clean provenance or clean cognition:** inconclusive.
- **Formal/kernel, human, or independent-model-family verification:** not performed.

**Overall correctness:** correct at the scoped conditional necessary-representation level.

**Confidence:** 0.97.
