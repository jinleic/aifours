VERDICT: ACCEPT-WITH-FIXES

The argument establishes nonexistence for unrestricted BTDs, including designs with repeated blocks. I found no fatal or major mathematical error. One minor quantifier/notation correction is needed.

The supplied SHA-256 matches. I used independently written, exact-rational checks in `python3 -c`; I did not open the excluded checkers, worker lane, or receipts. All proof line references below refer to [nonexistence-proof.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-15-parent-inputs-v1/nonexistence-proof.md).

**Findings**

- **Fatal:** none.
- **Major:** none.
- **Minor — L82–83:** The determinant formula \(Y_{kk}=\det H[\{a,b,k\}]/15\) should explicitly require \(k\notin\{a,b\}\). Under ordinary set-index notation, \(k=a\) collapses the set to \(\{a,b\}\), making the displayed right-hand side \(1\), whereas \(Y_{aa}=0\). Add “for \(k\notin\{a,b\}\); \(Y_{aa}=Y_{bb}=0\).” The latter equality already follows directly from the definition and is recognized at L86. No subsequent argument depends on the erroneous literal extension.

**Definition and parameters**

The formulation agrees exactly with Rosin’s [BTD definition and target entry, L92–106](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-15-parent-source-screen-v1/rosin-2501.17725v1.layout.txt:92). The instance appears with “?” at L95; the [Table 1 caption, L119–122](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-15-parent-source-screen-v1/rosin-2501.17725v1.layout.txt:119) identifies these as the Handbook’s smallest open instances.

Francel–Hurd’s [definition, L33–50](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-15-parent-source-screen-v1/francel-hurd-2008.layout.txt:33), and [incidence-matrix description, L63–75](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-15-parent-source-screen-v1/francel-hurd-2008.layout.txt:63), confirm that:

- Block cardinality counts multiplicity, hence column sums equal \(K\).
- Pair incidence is the product-weighted row inner product.
- Repeated blocks are permitted. Their displayed example actually has identical incidence columns \(b_1=b_7\). Their [L124–127](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-15-parent-source-screen-v1/francel-hurd-2008.layout.txt:124) separately defines simplicity as having no repeated blocks.

The necessary conditions hold:
\[
R=6+2(2)=10,\qquad VR=12(10)=15(8)=120,
\]
\[
\Lambda(V-1)=6(11)=66
=6(8-1)+2(2)(8-2).
\]
Thus these parameter equations do not already exclude the instance.

**Verification of Steps 1–8**

| Proof location | Independent assessment |
|---|---|
| **Step 1, L17–25** | All identities are correct: \(MM^T=8I+6J\), \(G^2=8G+384J\), \(H^2=40H\), \(H\mathbf1=0\), and \(\operatorname{tr}H=120\). Direct expansion gives \(H^2=1600I-200G+960J=40H\). |
| **Step 2, L28–34** | Symmetry and \(H^2=40H\) imply PSD. Its eigenvalues are \(0,40\), so trace \(120\) gives rank \(3\). The diagonal bound gives \(c_j\le2\); the stated minor consequences follow. |
| **Step 3, L37–39** | Correct: \(n_2=9+n_0\) and \(n_1=24-2n_2\). |
| **Step 4, L42–47** | The row equations give \(\sum t=2,\ \sum t^2=6\). Exhaustive integer enumeration gives exactly the two stated nonzero multisets. Consequently at most four off-diagonal entries equal \(4\). |
| **Step 5, L50–56** | The bound and congruence give precisely \(H_{jk}\in\{-1,4\}\). PSD makes \(H_{jk}=4\) imply equality of the corresponding \(H\)-columns. The equivalence classes and size bound \(5\) follow. |
| **Step 6, L59–71** | Correct inverse and determinant: \(A^{-1}=(I-\frac3{40}J)/8\), \(\det A=80\cdot8^{11}=2^{37}5\). The determinant-lemma factor is exactly \(2^{28}/25\). |
| **Step 7, L74–77** | \(\det(5I_3-J_3)=50\), contradicting the square-minor lemma. Hence exactly two classes, with sizes \(\{5,5\}\) or \(\{5,4\}\). |
| **Step 8, L80–93** | Correct apart from the minor indexing issue above. The Schur complement is PSD; Guttman rank additivity applies legitimately and gives rank \(1\). The moment identity, trace \(40\), zero row sums, and vanishing \(y_k\) on type-2 columns all follow. |

For Step 6, independently simplifying the determinant-lemma matrix gives
\[
I-P^TA^{-1}P=\frac{H[S]}{40},
\]
hence
\[
\det(N)^2=\frac{\det A}{40^3}\det H[S]
=\frac{2^{28}}{25}\det H[S].
\]
An integer that is a rational square is an integer square. Neither invertibility of \(N\) nor simplicity is required.

As an additional check on Step 8, put \(Q=P\Gamma^{-1}P^T\), with \(P=HE\). Then
\[
HQ=QH=Q^2=40Q.
\]
Therefore \(Y^2=40Y\); together with \(\operatorname{tr}Y=40\), this independently confirms PSD and rank \(1\).

**Steps 9–11 and exhaustive enumeration**

**Step 9, L96–100:** Both coordinate multisets are correct. The size-4 class’s extra \(t=1\) **cannot occur on a type-2 column**: its three classmates already supply three \(t=1\) entries, and every member of the other class has \(H_{jk}=-1\), hence \(t=0\). This follows from L54–55 and needs no additional assumption.

**Step 10, L103–108:** I enumerated all **100 labeled \(p\)-arrays** and all **500 choices including the type-0 column’s position**. The diagonal values are
\[
F(-1,-1)=2/3,\quad
F(-6,-1)=F(-1,-6)=32/3,\quad
F(-6,-6)=24.
\]
Thus \((-6,-6)\) was included; it can have \(Y_{kk}=0\) at a type-0 column. The complete set of sums is exactly
\[
\{130/3,\ 140/3,\ 150/3\},
\]
which excludes the required \(120/3\). No type-0 case is missed.

**Step 11, L111–124:** Enumeration produced:

| Filter | Labeled arrays remaining |
|---|---:|
| Required coordinate multiplicities | 900 |
| All \(Y_{kk}\ge0\) | 360 |
| Required \(\sum F_{kk}=44\) | 180 |

Here \((-6,-6)\) has \(Y_{kk}=14-24=-10\), so its exclusion is justified. Every diagonal \(F\)-value at L114–115 is correct. Case I always gives \(142/3\). All 180 remaining arrays are permutations of the stated Case II multiset.

**Rank-one argument, L125–129:** Correct. With
\[
y=\sqrt{10/3}\,(s_1,s_2,s_3,s_4,2s_5,2s_6),
\]
integrality of \(H_{56}\) forces \(s_5=s_6\). Zero sum then forces the first four signs opposite. Independently,
\[
F_{12}=22/3,\qquad H_{12}=22/3+10/3=32/3,
\]
a contradiction.

I checked all **64 signs for each of the 180 arrays: 11,520 assignments**. None satisfies both integrality and zero sum. Integrality alone leaves two assignments per array; their normalized sums are \(+6\) and \(-6\), so the zero-sum condition is essential.

**Finitary variant, L130–137:** Correct independently of the rank-one factorization. The uniquely forced row is
\[
(Y_{51},\ldots,Y_{56})
=\frac13(-20,20,20,20,40,40).
\]
Its sum is \(40\), and entries at every type-2 column vanish. This contradicts \(Y\mathbf1=0\). All displayed \(F\)-values and signs in this variant check out.

After the minor correction at L83, the manuscript proves nonexistence under precisely the stated unrestricted matrix definition. It assumes neither distinct blocks nor a special column order, and consequently also excludes simple BTDs.