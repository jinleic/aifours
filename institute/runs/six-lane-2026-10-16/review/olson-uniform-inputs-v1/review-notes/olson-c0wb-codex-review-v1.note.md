DISPOSITION: ACCEPT-WITH-FIXES

The target SHA-256 matches `ac52d85fc04ebc29aacd5bffbe923355234af752c5b5e2a52efe8b9a9935de77`. This was a static audit: file reading, checksum inspection, and hand reasoning only. No mathematical code, claimant code, receipt replay, network access, writes, or delegation.

**New-target severity counts: FATAL 0; MAJOR 0; MINOR 5.** Previously reported import repairs are distinguished below.

## FATAL

none

## MAJOR

none

## MINOR

1. **The Case-B obstruction is sufficient, not an “exactly” characterization.**  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:121`

   Under \(k\ge k_B+3B\), the proved implication is
   \[
   n_{\mathrm{ev,al}}>
   2(k-k_B-2B)+n_{\mathrm{pr}}-1
   \quad\Longrightarrow\quad
   n_{\mathrm{ev,al}}>B+n_{\mathrm{an}}-2
   \quad\Longrightarrow\quad
   \text{Case B is impossible}.
   \]
   No converse is proved, and it is false.

   Hand control: take
   \[
   (p,k,\kappa,B,k_B,E)=(11,13,3,1,2,2),
   \]
   with ten aligned singles, two aligned doubles, and one anti single. Then \(n_{\mathrm{ev,al}}=2\), so C+ holds through condition (i), while Case B would require
   \[
   2\le B+n_{\mathrm{an}}-2=0.
   \]
   Replace “exactly those” by **“a sufficient family of words for which Case B cannot occur.”**

2. **The unqualified worst-case remark is too strong.**  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:71`

   Case B gives \(n_{\mathrm{ev,al}}\le B+n_{\mathrm{an}}-2\); it does not generally prohibit \(n_{\mathrm{ev,al}}=E\).

   Hand control: take
   \[
   (p,k,\kappa,B,k_B,E)=(17,21,7,4,3,6).
   \]
   Use six aligned doubles, eleven aligned singles, and four consecutive anti singles. Set \(x=2\) on the doubles, \(x=1\) on the aligned singles, and \(x=(-2,-2,-1,-1)\) on the anti block. Then
   \[
   \sum x=12+11-6=17.
   \]
   The singleton lower bounds for \(d=2,1,-1\) are respectively \(0,-1,-3\), so these lifts satisfy them. The defect set is the anti block, with \(c(Z)=2\), \(m(Z)=1\), hence
   \[
   \Phi(Z)=3=k_B.
   \]
   Thus this is Case-B arithmetic with \(n_{\mathrm{ev,al}}=E=6\).

   Correct statement: **“When \(n_{\mathrm{ev,al}}=E\), Case B requires \(E\le B+n_{\mathrm{an}}-2\); in particular, the count-violating words considered below cannot enter Case B.”**

   These two hand controls concern relaxed lift data, **not solutions of all of (0.2), avoiders, or group counterexamples**.

3. **X**’s literal profile quantifier does not match the receipt checker.**  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:87`

   The text requires the seed-dependent inequality for **every allowed profile and every live weight**. But `inverse-run-count/mixdef-high/c6/seedXX.py:42` discards profiles having a guaranteed empty seed, and `seedXX.py:60` checks the inequality only on the remaining profiles.

   This is a harmless mathematical strengthening of the implementation’s intended implication, but the receipt does not literally certify the stronger hypothesis as printed. Replace the clause by:

   > For every allowed profile **not already excluded by a configuration-derived empty seed at a guaranteed occurring weight**, every live weight \(d\) satisfies  
   > \(\min(k_B-1,d-a_d)\le p-k_B-1\).

   Dispatch those empty-profile cases before using endpoints. The corrected implication follows directly from SEED-G**, and matches `seed_part()`/`finisher()`.

4. **The census descriptions omit their lower prime bound.**  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:92`  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:96`  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:110`

   `inverse-run-count/mixdef-high/c6/seedXX.py:68` starts at \(p=11\). Describe the receipts as covering respectively
   \[
   11\le p\le61,\qquad11\le p\le31,\qquad11\le p\le23.
   \]
   Apply the same qualification to the totals at lines 106–109.

   This does not invalidate the written SA**/PA** implication at \(p=5,7\): there \(E\le p-4\), and evenness gives \(E\le2\), so the old class condition already holds. It does mean the displayed receipts did not census those primes.

5. **The Lemma-W citation’s path convention and review qualifier need correction.**  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:10`  
   `inverse-run-count/mixdef-high/c6/proof-C0WB.md:12`

   The printed `../../../inverse-parity/...` path resolves from **c6/**, contrary to “Paths relative to mixdef-high/.” From `mixdef-high/`, use
   `../../inverse-parity/mixdef-low/c2/proof-Rstar-partial-v2.md`.

   Also replace “wording fixes only in Sec. 2.” The pinned Claude note reports six MINOR findings concerning the broader source file; it finds no FATAL/MAJOR issue and validates Lemma W’s Section 2 argument. The stated Codex ACCEPT / Claude ACCEPT-WITH-FIXES statuses themselves are accurate.

**Correctness.** I find no new gap in DF, C0W, C0B, or the whole SA**/PA** count replacement.

For **DF**, integrality gives
\[
x_t\le\left\lfloor\frac{d_t+1}{2}\right\rfloor
\le\left\lfloor\frac{d_t+B}{2}\right\rfloor,
\qquad
x_t\le\frac{E+2}{2}<p.
\]
Thus \(x_t\) lies strictly below the singleton minimum’s first and third terms, forcing \(x_t\ge d_t+1-k_B\). This works for negative, zero, and positive \(d_t\), including \(B=1\), \(k_B=1\), and \(p=5\). The light-run condition \(bh_t\le1\) correctly includes more than the defect condition \(bh_t\le0\).

For **C0W**, DF gives cheap weights in \([1,k_B]\), and
\[
\sum_t(c_t+1)=p+2k_B.
\]
A noncheap run with \(c_t\ge0\) has \(bh_t\ge2\), hence \(d_t\ge2\), so it is aligned and \(c_t+1\le d_t/2\). The aligned \(d\)-mass is \(A-n_{\mathrm{pr}}\le A\le2p-1\), giving \(W(\mathrm{cheap})\ge2k_B+1\).

The heavier alternating classes of the cheap paths form an independent union. In the all-cheap case, deleting \(t_0\) leaves weight at least \(p+k_B\); the path endpoints have cyclic distance two because \(k\ge4\). This handles odd and even cycles without claiming a half-weight independent set on an odd cycle. Here \(p\ge3k_B+1\) implies \(p\ge k_B+2\).

Both prefix operations preserve independence. Positive integer weights give \(|P|\le k_B+1\), and the first crossing gives
\[
k_B+1\le\Phi(P)\le2k_B,\qquad
bh(P)\le |P|\le k_B+1\le B.
\]
Because \(m(P)=|P|\) and \(x_t=bh_t+c_t\),
\[
X_P+m(P)=bh(P)+\Phi(P)\le3k_B+1\le p.
\]
The pattern is nonempty and proper. Consequently every hypothesis of the **high-run** Kill lemma is present, including at equality \(p=3k_B+1\). No interval-chain lifts, low-run Fact F, low-run Lemma K conditions, or \(k\le p\) are imported.

For **C0B Case A**, \(Z\) is nonempty since \(\sum bh=k-2k_B<k\), and proper since \(k-2k_B>0\) by (0.1). Every nonempty current subset has an endpoint available for deletion. The changes \(-c_t\) and \(-c_t-1\) can be positive; monotonicity is unnecessary. At the first crossing below \(p+1\), the predecessor has integer \(\Phi\ge p+1\), while the decrease is at most \(p-k_B\), giving \(\Phi(Q)\ge k_B+1\). Thus \(Q\) is nonempty and proper, and its containment in \(Z\) supplies (Fl) and
\[
X_Q+m(Q)\le c(Q)+m(Q)\le p.
\]

The sources of (A*) are correct. DF supplies \(c_t\le k_B-1\) on defects; a seed supplies \(c_t\le d_t-a_t\). For quality seeds,
\[
d_t-a_t\le\frac{d_t+\Delta_0}{2}-1
\le\frac{2p-k-1}{2}\le p-k_B-1.
\]
The last inequality needs only \(k\ge2k_B+1\), already implied by (0.1). These estimates do not require nonnegative \(c_t\).

For **C0B Case B**, the definitions and total identities give
\[
\Delta=-f(Z)-m(Z)-n_{\mathrm{ev}}/2-\mathrm{sur},
\]
with \(m(Z)\ge1\) and \(\mathrm{sur}\ge0\). Dropping aligned contributions and extending the positive pair/anti contributions yields
\[
n_{\mathrm{ev}}/2\le-f(Z)-1
\le\frac{B+n_{\mathrm{pr}}+n_{\mathrm{an}}+
n_{\mathrm{ev,an}}}{2}-1.
\]
The stated ceiling identity is correct for both parities of \(b\ge1\). Substitution of
\(n_{\mathrm{ev}}=n_{\mathrm{pr}}+n_{\mathrm{ev,an}}+n_{\mathrm{ev,al}}\) gives
\[
n_{\mathrm{ev,al}}\le B+n_{\mathrm{an}}-2,
\qquad
s_0\ge k-k_B-3B+1+n_{\mathrm{pr}}\ge1.
\]
No nonempty anti set is assumed; a negative resulting upper bound simply rules out Case B.

B1+ uses no additional count hypothesis before its final lower bound on \(s_0\). B2+ produces \(\Delta+1\) independent free odd aligned runs, none adjacent to \(Z\); a boundary neighbour of \(Z\) remains outside \(Q\), proving properness. Its (M), (Fl), and (P) estimates use no \(n_{\mathrm{ev,al}}\) assumption. In particular the imported bound \(X_Q+m(Q)\le p-2-B/2<p\) remains available. All required quantities are integral; the accepted \(s_0\ge1/2\) weakening is preserved, while this argument obtains the stronger \(s_0\ge1\).

For **SEED-G****, the precise F3 grouping is
\[
k\ge k_B+3B
\quad\mathbf{AND}\quad
\left[
2k_B\le p\quad\mathbf{OR}\quad
\forall t,\ \min(k_B-1,d_t-a_t)\le p-k_B-1
\right].
\]
Print these brackets explicitly, also in X**. An actual empty configuration-seed intersection excludes the word immediately, before endpoints are used. A merely empty formal quality window does not. Otherwise the original canonical lifts, singleton bounds, certification, (QS*)/(P2)/(PIN), and NMH hypotheses remain intact. F1/F2/F3 replace only the finisher’s count condition.

For the **whole SA**/PA** implication**, the original region inequalities and configuration availability remain unchanged. Their \(m\ge1\) constructions give proper \(Q,Q+t\), including cyclic separation under \(k\ge7\). They establish quality seeds or an actual empty intersection. Therefore the entire enlarged class condition is valid:
\[
C_{\mathrm{class}}
\ \lor\
(B\ge k_B+1\ \land\ 3k_B+1\le p)
\ \lor\
(k\ge k_B+3B).
\]
No narrowing of either seed region is required.

The \(p=7\) classes \((k_B,B)=(2,2),(1,3)\) remain outside both regions; satisfying F3, or F2 as well in the latter case, does not supply their missing seeds. Likewise \((p;k_B,B)=(11;5,3)\) remains outside SA/PA: SA has lower endpoint \(5\) exceeding upper endpoint \(3\), and PA fails \(\Delta_0\ge B+1\). Keep the repaired \(p\ge11\) boundary on the large-B coverage accounting.

All six Claim E-prime classes retain written coverage: respectively SA \(m=4\), PA \(m=4\), PA \(m=4\), PA \(m=5\), SA \(m=5\), and SA \(m=7\), in the order listed in SEEDG-r2:271–272. They already satisfy the old count alternative.

The **import status remains conditional on known repairs**, not clean acceptance of the frozen star/cls wording. At `proof-SEEDGstar.md:42–43`, the correct argument is
\[
\min_iU_i+\min_jT_j
=\min_{i,j}(U_i+T_j)
\ge\min_{i,j}B_{ij}=L_A(d),
\]
followed by integrality, and similarly for \(L_B\). The claim “at least each” remains a pre-existing wording error. The frozen cls:35 parenthetical must use \(k\ge7\) and cyclic distance \(\min(4,k-4)\ge2\), as explicitly repaired by r2. Star:82’s known scope overclaim is not a premise here and is corrected in substance by the target’s retained seed-failing class. The unrestricted floating `bounds()` issue remains outside the finite receipt range; it does not affect the small integer/half-integer calculations reported here. None is counted as a new target finding.

For **X****, after MINOR-3’s quantifier repair, the transfer is sound. Every actual word has an allowed profile. An occurring empty configuration-derived seed excludes it; otherwise its actual seeds are contained in the exact intervals. Shrinking an interval raises its lower endpoint, so
\[
d-a_t\le d-a_d,
\]
and the seed form of (A*) transfers. The other seed, pair, and pin inequalities transfer in the same direction. Class instantiations remain explicitly **computer-assisted [W+F]**.

The displayed rows and totals agree with the pinned receipts by inspection and hand addition:

| Receipt scope | Reconciled totals |
|---|---|
| Region census, \(11\le p\le61\) | OPENE: \(26{,}225/22/602\); IE: \(21{,}308/0/5{,}062\), for C+/F2/F3 |
| Class census, \(11\le p\le31\) | OPENE: \(2{,}736+343+19+15+1=3{,}114\) |
| OPEN0 in that class census | 2 existing RA2 exclusions; 10 seed failures |
| Ablations, \(11\le p\le23\) | 56, 3, and 1 unfinished OPENE classes |

The replay receipts record 1,320 C0W kills and 360 C0B Case-A kills. The biased receipts record \(1{,}080+1{,}160\) further Case-A kills and **zero Case-B instances**. They provide no empirical validation of Case B. The mutation counts also reconcile. These are inspected recorded receipts, not reproduced experiments or premises of the uniform proofs.

**Novelty.** Relative to the pinned base, the contribution is two additional sufficient finishers for words whose seeds and certification are already established. C0W properly credits the low-run construction and supplies its own high-run bounds. External novelty and priority were not checked.

**Significance.** The recorded finite effect is 377 additional seeded OPENE exclusions, giving 3,113 of 3,114 classes for primes \(11\) through \(31\). The stated remaining OPENE class is \((31;51,24,23)\), whose seed test fails. Ten OPEN0 classes remain under these tests; coverage outside the stated finite ranges is not established by the census. No full NMH, MIX_DEF_HIGH, RUNS, PAR, INV, INV*, or ordered-Olson claim follows.

Necessary changes are MINOR-1–5 above, explicit F3 brackets, and explicit handling of actual empty seed intersections before endpoint use. Preserve every original SA/PA region and NMH hypothesis; no region shrink or additional count restriction is needed.

**PARENT-DELTA-FIT: YES-AFTER-FIXES** — for the **whole written SA**/PA** claim**, with the wording repairs above. This is advisory review, not authorization to accept the parent claim.