VERDICT: REJECT

All five SHA-256 hashes match. Rejection concerns the claimed lifting obstruction in DOB(p); W-ALL and Theorem C survive review.

Paths below are relative to `inverse-run-count/mixdef-high/c3/`.

| File | Verdict |
|---|---|
| `proof-WALL.md` | ACCEPT |
| `proof-C-r1.md` | ACCEPT |
| `proof-NOBCplus.md` | REJECT as written; NOBC+ and NOLIFT themselves are correct |
| `proof-W4-r2.md` | ACCEPT current mathematics; revision diff unchecked |
| `proof-NOLP-r2.md` | ACCEPT current mathematics; revision diff unchecked |

**MAJOR — `proof-NOBCplus.md:54`, `:56`, `:61`: DOB does not obstruct every singleton-extension lifting argument.**

Failure to certify anti pairs prevents (H), but does not prevent certifying larger patterns or proving a contradiction using Lemma L. There is a concrete counterexample to the claimed methodological obstruction: **W(19,8)**, explicitly included in DOB(19).

Here \(k=28\), \(\rho=5/7\), \(\sigma=2/7\), and
\[
\rho(p+kB)-\sigma=19<20.
\]
Thus the Lemma BC obstruction holds. Nevertheless:

- Every aligned pair is certified. Every anti triple is certified by adjoining the anti singleton to an aligned pair: condition (A) is at least \(1\), and (B) at least \(22\ge20\).
- The CW induction then certifies every pattern of size \(3,\ldots,9\): its potentially tight inequality becomes \(19+3+y\ge24\), with \(y\ge2\).
- \(P=\{0,2,4\}\) and \(P^c\) are certified. Build \(P^c\) by adjoining aligned runs in order \(1,3,5,6,\ldots,27\); the minimum left sides of (A) and (B) are respectively \(1\) and \(24\). Since \(\lambda(P)=-4\), \(\lambda(P^c)=14\), Lemma L pins \(\sum x_t=19\).

These certified constraints already contradict avoidance. Put \(c_t=d_t-x_t\); then \(\sum c_t=7\), and singleton bounds give \(c_t\le7\). WALL’s defect argument applies except for two cases:

- \(Z=\{0\}\): all outside \(c_t=0\). Adding two isolated aligned runs gives a certified anti triple with \(c(Q)=7>\gamma(Q)=5\).
- \(Z=\{0,a\}\): \(7\le c(Z)\le14\). The 26 outside aligned coordinates are nonpositive and sum to \(7-c(Z)\ge-7\); hence at least 19 are zero. Choose one adjacent to neither member of \(Z\). The resulting certified anti triple has \(c(Q)\ge7>\gamma(Q)\), since \(\gamma(Q)\le6\).

Thus a singleton-extension/Lemma L argument **does exclude W(19,8)**.

**Concrete fix:** retain DOB’s definition but describe only “no Lemma BC certificate and failure of (H),” deleting the universal lifting obstruction and “open core” claims. Alternatively impose \(3kB>p+6\), which invokes NOLIFT(b), and update the listed ranges. Correct the corresponding claims in `README.md:227` and `:262`.

**What is established**

- **W-ALL:** exactly the stated range
  \[
  p\ge5\text{ prime},\qquad
  1\le kB\le\min\!\left(p-4,\left\lfloor\frac{p+4}{3}\right\rfloor\right).
  \]
  Family parameters, both lambda formulas, special values, CW boundary cases, and the pin are correct. Kill patterns have respectively \(kB\), at most \(kB\), and at most \(kB+1\) runs. The larger interval used for pinning is separately certified by CW(b).
- **Theorem C:** NMH words with \(R\le2p-3\), hypothesis (H), and the stated disjunction on even aligned runs. Conditions (M), (Fl), (P) exactly characterize \(X_Q<\lambda(Q)\). Both cases work without strengthening (H). Corollary S retains (H).
- **NOBC+ / NOLIFT:** their stated quantitative obstruction lemmas hold; their combination does not justify the broader DOB conclusion.
- **Visible revisions:** `proof-W4-r2.md:66` correctly excludes the two zero positions from the third-run choice. `proof-NOLP-r2.md:51` correctly restricts its conclusion to the specified lifted constraint system.

**What is imported/unchecked**

Corrected Lemma H and the BC Claim are imported; the upstream reductions are not re-refereed. The original W4/NOLP files and earlier review note are absent, so “exactly two fixes and nothing else substantive” cannot be confirmed.

Independent in-memory checks found no failures in 1,266,196 CW step types, 224,713 interval steps through \(p=199\), and 13,478 sampled Theorem C replays. These do not validate the original censuses or establish RUNS(p), INV, or ordered Olson.