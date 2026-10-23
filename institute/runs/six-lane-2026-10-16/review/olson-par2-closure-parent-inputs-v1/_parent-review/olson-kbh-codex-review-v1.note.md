VERDICT: ACCEPT-WITH-FIXES

No fatal or major defect found in HW, KBH, or the conditional reduction of RUNS to MIX_DEF. One minor scope correction is needed in a cited auxiliary statement. All 12 pinned files match their manifest hashes.

1. **Minor finding: the parity file’s general Lemma H omits possible constant-pattern hits at \(\pm p\).**  
   [proof-PAR-K0.md, lines 18–33](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-parity__proof-PAR-K0.md:18) replaces the empty/full-pattern constraints by \(\min(A,B)\le\kappa\). Without a preliminary bound on \(A,B\), that replacement is false.

   For \(p=5\), take \(w=\rho_1^{10}\sigma_0^8\). Then \(k=1\), \(H=4\), \(\kappa=B=0\), and there are no proper patterns. Lemma H’s stated conditions hold, but the ten rotations form an identity subword. The actual empty-pattern half-window is \([-5,-1]\), which contains residue \(0\).

   **Fix:** include \(A,B\le2p-1\) in that equivalence, or retain the exact empty/full-pattern modular conditions. This does **not** invalidate HW, which checks every pattern, or the requested corollary: avoiders automatically satisfy these bounds, and odd-segment merging preserves \(A,B\).

2. **Lemma HW is exact, including the direction KBH uses.**  
   The definitions in [the run-count README, lines 24–35](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__README.md:24) give
   \[
   m=\tfrac12\sum_j f_j,\qquad
   h=\sum_j\left\lfloor\frac{\ell_j-f_j}{2}\right\rfloor=H-\beta.
   \]
   An even boundary reflection run loses one available pair; an odd boundary run loses none. Consequently,
   \[
   C_{\max}
   =\sum_j\left(f_j+2\left\lfloor\frac{\ell_j-f_j}{2}\right\rfloor\right)
   =2m+2h.
   \]
   \(E^+\) counts the available effectively positive rotations; \(E^-=R-E^+\).

   Substitution into GR’s endpoints gives exactly
   \[
   \left\lceil L/2\right\rceil=-g_P(E^-),\qquad
   \left\lfloor U/2\right\rfloor=g_P(E^+).
   \]
   Thus dividing the attainable even integers by two produces precisely \(I(P)\), including empty intervals and negative endpoints.

   WAS gives \(\tau(z_P)=\sum_P(y_{i-1}-y_i)=2\phi(P)\). Since \(p\) is odd, cancellation of \(2\) modulo \(p\) is valid. Every zero-sum \(\phi\) arises by recursively choosing \(y_i=y_{i-1}-2\phi_i\).

   At \(P=\varnothing,[k]\), the boundary definition gives **\(m=0\)**, \(h=H\), and \(\phi(P)=0\); \(E^+,E^-\) are respectively \(B,A\) and \(A,B\). Counting the full cycle as one block would be wrong, but HW’s explicit definition avoids that error.

   **Therefore, \(\phi(P)\in I(P)\pmod p\) for even one pattern fully justifies an identity \(2p\)-subword.** No converse or inherited condition is needed for KBH’s use.

3. **Every substantive KBH step checks out.**

   - **Segments, windows, ZS:** [lines 39–60](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__kappaB-high__proof-KBH.md:39). Segments partition the rotation runs into nonempty cyclic intervals, including when \(k>o\). A union of \(1,\ldots,o-1\) consecutive segments has exactly two odd boundaries, hence \(m=1,\beta=0,h=H\). Substituting \(E^+=D_Q+B\) and \(H=p-1-B\) gives the stated \(U_Q,L_Q\), even for negative \(D_Q\). ZS uses \(p+1\) prefix residues correctly. Its collision interval contains at most \(p\) segments and misses at least one nonempty segment because \(o\ge p+1\).

   - **Step 0:** [lines 64–71](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__kappaB-high__proof-KBH.md:64). The identities \(F=o+2H\), \(R=2p-o+2B\), \(D=2p-o\) are correct. From \(p+1\le o\le k\le2p-1\), one gets \(1\le D\le p-1\). Also \(R\ge k\ge o\) implies \(B\ge o-p\ge1\). The \(A\ge2p\) cut is valid.

   - **Step 1:** [lines 73–81](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__kappaB-high__proof-KBH.md:73). Both coordinate transformations are exact. In particular, the ceiling in `lo` and floor in `hi` remain correct for negative arguments. The monotonicity and Lipschitz assertions hold on the integer domain used here.

   - **Step 2a:** [lines 83–88](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__kappaB-high__proof-KBH.md:83). Induction establishes every lower constraint. For negative \(d_G\), monotonicity makes every extension bracket nonpositive; for \(d_G=0\), it is likewise nonpositive. Thus these cases give \(\theta_j=0\), and \(0\le\theta_j\le P_G\) holds throughout.

   - **Step 2b:** [lines 89–102](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__kappaB-high__proof-KBH.md:89). A positive greedy increment supplies a tight interval. Recursing into indices \(\le i_r\) makes the intervals disjoint and covers every positive increment. Each tight interval has \(D_Q\ge B+1\). The single-interval bounds are valid. With at least two intervals, each \(D_Q\le2p-2-B\), so the linear cap cannot exceed the half term, and
     \[
     \sum_r\operatorname{lo}(D_{Q_r})
     \le\frac{A-r(B-1)}2
     \le\frac{D-B+2}2
     \le D.
     \]
     No endpoint or rounding error found.

   - **Step 2c and conclusion:** [lines 103–108](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__kappaB-high__proof-KBH.md:103). From \(\theta(Q)\le\min(D,P_Q)\) and \(N_Q\le B\le p-1\), all three upper bounds follow, including the floored bound by integrality. ZS then applies. **No inherited inequality or per-run cap is used.**

4. **The RUNS bookkeeping is complete as a conditional reduction using the cited [W] results.**

   Normalisation swaps \(A,B\) while preserving every inherited condition. The empty-pattern zero certificate excludes \(B>\kappa\). For a remaining inherited avoider with \(k\ge p+1\):

   | Case | Applicable result |
   |---|---|
   | \(B=0,\ \kappa\ge1\) | [Corollary B0](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__proof-RUNS.md:377) |
   | \(B=\kappa=0\) | [K0 extension](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__proof-RUNS.md:383): \(R\ge k>p\), \(o=2p-R<p\), hence an even reflection run exists; inherited (P), (V) are available |
   | \(B=\kappa\ge1,\ o\le p\) | [Theorem KB](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-parity__proof-PAR-Kplus-partial.md:214); inherited (V) and the capped case’s (D0) are available |
   | \(B=\kappa\ge1,\ o\ge p+1\) | KBH |
   | \(1\le B<\kappa\) | Odd-segment reduction gives the stated [MIX_DEF](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-parent-inputs-v1/inverse-run-count__proof-RUNS.md:490) instance |

   Merging can reduce \(k\) below \(p+1\) and lose inherited conditions; MIX_DEF explicitly permits any \(k\) and requires no inherited conditions. There is no gap at \(\kappa=B=1\): KB and KBH already cover both ranges of \(o\), independently of the cited K1′ extension.

5. **Independent in-memory verification passed.**

   At \(p=5,7,11\), my own HW implementation agreed with raw ordered-product DP on **729 words**, checking **83,830 patterns**, including six explicit avoider controls. The KBH replay passed on **540 random words**, **6,200 windows**, and **269,375 subintervals**, including negative/zero segment totals, mixed rotation runs, \(k>o\), and 27 decompositions with at least two tight intervals. Three additional words violating (D0) also passed. Explicit identity witnesses were reconstructed and their ordered products checked.

Only pinned inputs were read; no live-lane files were opened or files modified.