DISPOSITION: ACCEPT-WITH-FIXES

FATAL: none.

MAJOR:

- **M1 — The closing scope claim exceeds the receipt.** [c6/proof-SEEDGstar.md:82](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:82) identifies COUNT as the remaining obstacle, but [out/seedXstar2_mode0.txt:8](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/out/seedXstar2_mode0.txt:8) records one OPENE class failing the seed test. Replace that sentence with: **“Among the 378 OPENE classes remaining in the reported range, 377 pass the seed/certification tests but fail C+’s stated class sufficient condition; one further class fails the seed/certification test.”** Failure of the class sufficient condition also does not establish failure of C+’s per-word condition.

MINOR:

- **m1 — Incorrect minimum argument in SCW-G*.** [c6/proof-SEEDGstar.md:42](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:42) says the certification sum is at least *each* of the nine displayed bounds. The corrected argument is
  \[
  \min_i U_i+\min_j T_j=\min_{i,j}(U_i+T_j)
  \ge \min_{i,j}B_{ij}=L_A(d),
  \]
  and similarly for \(L_B\). Integrality then gives the ceiling. For an arithmetic counterexample to the written sentence, take
  \[
  (p,k,\kappa,B,E,\Delta_0)=(11,14,4,1,2,6),\quad
  d=1,\ y'=2,\ m=m'=1.
  \]
  Then \(\operatorname{lam}(2,1)+\operatorname{lamc}(3,1)=7\), while the displayed \(U_1+T_1\) lower bound is \(10\). The corrected minimum argument preserves the conclusion.

- **m2 — CF′ retains the incorrect \(k\ge12\) parenthetical.** [c6/proof-SEEDG-cls.md:35](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-cls.md:35) should use the reason supplied at [c6/proof-SEEDG-r2.md:186](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-r2.md:186): the path endpoints are \(t+2,t-2\), with cyclic distance \(\min(4,k-4)\ge2\), since \(k\ge7\). For example, the setting permits \((p,k,\kappa,B)=(5,7,2,1)\). The configuration counts remain valid.

- **m3 — `bounds()` is exact for the receipts, but its unrestricted implementation can be too permissive.** [c6/seedXstar2.py:23](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/seedXstar2.py:23) uses floating division followed by `math.ceil`. All relevant integers and half-integers are exactly represented for \(p\le31\). Beyond that range, take the legal arithmetic parameters
  \[
  p=2^{61}-1,\quad \Delta_0=2^{60}+200,\quad
  \kappa=p-\Delta_0,\quad k=p+\kappa,\quad B=d=1,\ E=0.
  \]
  Exact \((\lceil L_A\rceil,\lceil L_B\rceil)\) is
  \((2^{59}+101,\,2^{59}+102)\); the floating expressions return
  \((2^{59}+128,\,2^{59}+128)\). This weakens the endpoint checks by 27 and 26 units. Compute the eight **doubled integer expressions**, then use `(minimum + 1) // 2`. This defect does not invalidate the reported finite computations.

- **m4 — T1’s abbreviated task hash has a suffix typo.** [manifest.json:7](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/manifest.json:7) and the actual bytes give
  `476e9a2871cc81352b7bcbb84c31f9c29606f76cb330d18556330578385f5b22`,
  ending `f5b22`, whereas the request says `2b22`. This disposition concerns the named, manifest-pinned copy.

All 26 manifest digests match. T2’s verified digest is `5a5038e4b22c9a00e95c11f5157357b65ab2cbb3311d241b5478dbcb4e8602ba`. No pinned Python was imported or executed.

The remaining proof and code checks support the conditional results as follows.

**SEED-G*.** The eight expressions in each definition are exactly the minima of the nine displayed lower bounds, with the stated duplicate entries. The individual term bounds at [c6/proof-SEEDG-r2.md:122](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-r2.md:122) and [129](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-r2.md:129) hold throughout the stated arithmetic domain. They use (2.1), (F1), the setting identities, \(1\le m'\le m\le m'+1\), and the floor inequality; they do not require (QS).

For \(s=2\), the extension inequalities are exactly (P2): \(D_Q=d_s+d_t\), and \(m(Q)=1\) for cyclically adjacent runs and \(2\) otherwise. Both extension orders give the same two inequalities. One run satisfying (PIN) suffices: its canonical lower bound and P0 give the lower total bound \(1\), while (PIN) gives the upper bound \(2p-1\).

Lemma QQ is correct **for seeds as defined**, including \(a_t\ge\lambda(\{t\})\). That lower bound is essential in the imported two-run proof. The base proof establishes (P2) for every actual pair and (PIN) for every run. Theorem SEED-G* then combines correctly with C0+. Its empty-intersection alternative concerns actual configuration seeds, so it does not mistake an empty quality window for an exclusion. These conclusions concern [c6/proof-SEEDGstar.md:35–54](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:35).

**LF, including endpoints.** Put \(\delta=\Delta_0\). On the full stated domain, the linear entry in each displayed two-term minimum is redundant. Thus:

| Weight | \(L_A(d)\) | \(L_B(d)\) |
|---|---:|---:|
| \(d=u\ge1\) | \((\delta+E-u+3)/2\) | \((\delta+E)/2+2\) |
| \(d=0\) | \((\delta+E+3)/2\) | \((\delta+E+3)/2\) |
| \(d=-u\le-1\) | \((\delta+E)/2+2\) | \((\delta+E-u+3)/2\) |

For completeness, in the eight-expression order of [c6/proof-SEEDGstar.md:14](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:14), let \(C=(\delta+E-u+3)/2\), \(T=(\delta+E)/2+2\). For \(d=u>0\), the doubled differences from these proposed minima are
\[
2(A_i-C)=
(\delta+E+u+1,\delta+u-1,u+1,\delta+u-3,
 \delta+E-u-1,0,0,2\kappa-1),
\]
\[
2(B_i-T)=
(\delta+E,\delta+2u-4,0,\delta+2u-2,
 \delta+E+2u-2,2u-1,2u-1,2\kappa+u-2).
\]
Every entry is nonnegative. At zero, the corresponding A vector is
\[
(\delta+E+1,\delta-1,1,\delta-3,\delta+E-1,0,0,2\kappa-1);
\]
the B vector exchanges positions 2 and 4. Negative \(d\) follows by exchanging A/B and those same positions.

The setting facts used are \(\delta\ge3\), \(E\ge0\), \(u\le E+1\), and \(R-\delta-E=2\kappa\), with \(\kappa\ge2\) following from \(1\le B\le\kappa-1\). The lower endpoint \(-\min(B,E+1)\) only truncates this verified domain. Evenness of \(E\) is needed for the integer relaxation formula below; it is unnecessary for these comparisons. A zero-weight run requires a pair, hence \(E\ge2\).

The continuous gaps are exactly
\[
\begin{array}{c|cc}
d&L_A-(\delta-d)/2&L_B-(\delta+d)/2\\ \hline
u>0&(E+3)/2&(E-u+4)/2\\
0&(E+3)/2&(E+3)/2\\
-u<0&(E-u+4)/2&(E+3)/2
\end{array}
\]
and are at least \(3/2\), including \(u=E+1\).

The **exact integer relaxation**, before canonical clipping and the separate P2/PIN restrictions, is as follows. Let \(h=E/2\), \(\epsilon=\delta\bmod2\), and
\[
g(u)=h+2-\left\lfloor\frac{u-\epsilon}{2}\right\rfloor.
\]
The permitted decrease in the lower bound on \(a_t\), and increase in the upper bound on \(b_t\), respectively, are:

- \(d>0:\ (h+2,g(d))\);
- \(d=0:\ (h+2,h+2)\);
- \(d<0:\ (g(-d),h+2)\).

Both relaxations are at least **two integer units**.

**PR, allowed profiles, and CF′.** The bookkeeping and lower bound at [c6/proof-SEEDG-cls.md:12–21](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-cls.md:12) are correct. For \(a^*\ge2\), the strengthened form is
\[
n_1\ge k-B-E+2e_{\rm an}+n_{\rm pr}+a^*-2.
\]
Consequently, taking a lower admissible \(e_{\rm an}\) gives valid lower bounds on both \(n_{\rm al}\) and \(n_1\). For \(a^*=1\), \(e_{\rm an}=E-n_{\rm pr}\) and \(n_1=n_{\rm al}\).

Every actual word supplies an enumerated profile. Its weights lie in the specified set, and \(a^*,-b^*,0\) are guaranteed precisely under the stated conditions. `profiles()` correctly handles \(b^*=0\), residual anti excess when \(a^*=1\), and \(n_{\rm an}\ge1\).

The enumeration can include unrealizable triples. For example,
\[
(p,k,\kappa,B)=(17,21,6,5),\quad
(a^*,b^*,n_{\rm pr})=(1,2,0)
\]
is admitted by the necessary-condition checks, but would require \(e_{\rm an}=4\) in one anti run of maximum length 2. This is **conservative**: it adds obligations and cannot create a false acceptance.

CF′’s two counts follow from integer rounding of the interval bounds:
\[
\sum_i\lceil L_i/2\rceil\ge(n_1-3)/2,\qquad
\sum_i\lfloor(L_i+1)/3\rfloor\ge(2n_1-k-4)/3.
\]
After m2, separation between intervals and across the cyclic wrap is valid. Deleting \(t\) and its neighbours ensures no selected member is adjacent to \(t\). The unions have \(m\) and \(m+1\) blocks; the imposed \(2m+2\le k\) ensures properness.

**Corollaries X and X*.** The hull construction at [c6/proof-SEEDG-cls.md:44–48](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-cls.md:44) is sound. For each family/m, an available configuration has some weight in the stated full range. Its seed lies in that range’s hull. Intersecting those hulls with the canonical interval therefore retains the canonical lift of an avoider.

Checking no-wrap for every candidate \(y\) is sufficient. Including unattainable \(y\)’s can enlarge a hull or discard a useful family; both effects are conservative.

An empty sigma excludes a word when that weight occurs. A guaranteed empty weight can therefore discharge a whole profile; an empty non-guaranteed weight cannot. Both implementations respect that distinction. Otherwise endpoint tests transfer to the contained actual seeds. Every actual pair has excess sum at most \(E\), and its block count is among the two tested values. Testing PIN for every live weight supplies the required pin.

C+’s class condition implies the per-word condition because
\(n_{\rm ev,al}\le e_{\rm al}\le E\) and \(n_{\rm pr}\ge0\).

T2’s r1 citation does not introduce a substantive misuse: its own proof uses configuration-derived sigma emptiness, and its RA guards use the corrected prime ranges. Updating its references at [c6/proof-SEEDG-cls.md:6](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-cls.md:6) to r2 would remove the stale wording and CF ambiguity.

The functions carrying the computer-assisted claims are:

| File | Functions and responsibilities |
|---|---|
| [c6/seedX2.py:21](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/seedX2.py:21) | `classes`, `profiles`, `exact_seed`, `class_pass`; `cdiv` supplies exact ceilings. |
| [c6/seedX2.py:97](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/seedX2.py:97) | `region_SA`, `region_PA`, and `main`’s `written` flag supply the coverage breakdown. |
| [c6/seedXstar2.py:19](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/seedXstar2.py:19) | `bounds`, `class_pass`, and `main`, using `seedX2`’s profile and seed functions. |

`classes()` covers the stated arithmetic class domain. `exact_seed()` matches all four families, their \(E-e_d\) ranges, m bounds, properness cutoff, per-y no-wrap tests, hulls, and canonical intersection. The `max(E-et,0)` clamp is inactive for actual candidate weights. The cache key contains all profile-dependent inputs to the seed computation.

`class_pass()` implements X’s alternatives correctly. The star pair loops include equal weights and both block counts, including combinations that need not coexist; this strengthens the test conservatively. Requiring PIN for every live weight is also conservative. Apart from m3 outside the reported range, I found no implementation accepting a weaker hypothesis than its written counterpart.

The SA region matches r2. PA’s additional upper bound is redundant beside its tighter upper bound. The `written` flag matches SA/PA with C+ and the guarded RA2/RA3 cases.

[c6/map6.py:22–28](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/map6.py:22) executes **unpinned** `c4/ind_star3.py` and `c4/ind_star_ex.py`. Those dependencies supply the W/SB/IS/OPEN0/IE/OPENE labels used for counts. They do not supply the X/X* seed acceptance tests. Their absence prevents an independent reproduction of that label partition from this bundle.

**Receipts and scope.** Every displayed row and total agrees with the pinned receipts. For primes **11 through 31**:

| OPENE total | SA/PA | Additional X | Additional X* | X* seed pass, no C+ | X* seed fail |
|---:|---:|---:|---:|---:|---:|
| 3,114 | 1,793 | 756 | 187 | 377 | 1 |

X alone has the stated 207 `pass-noC+` and 358 failures. All control totals reconcile. Star MODE 1 matches X MODE 0 after aggregating the `written` split; its acceptance set is a subset, so equal counts establish equality within these runs. Star MODE 2 adds the stated one IS failure at \(p=19\), and six IS plus three IE failures at \(p=23\), with no OPENE change.

Self-written arithmetic checks additionally covered 31,878 LF parameter tuples and 386,412 domain tuples for the eighteen term bounds at \(p=5,7,11,13\). These are verification aids alongside the algebra above.

After the fixes, **[W]** supports LF, SCW-G*, QQ, conditional SEED-G*, PR, CF′, and the written implications underlying X/X*. Their reported class instantiations remain **[W+F], computer-assisted**. The coverage tables are correctly presented as **[F] aids**.

Novelty is supported here only relative to the supplied SEED-G base: weaker seed windows are separated from explicit two-run and pin obligations. External novelty has not been assessed.

The finite significance is 187 additional OPENE exclusions beyond X in the reported range. There remain 378 OPENE classes under these tests and ten OPEN0 classes after the two existing RA2 exclusions. No full NMH, MIX_DEF_HIGH, RUNS, PAR, INV, INV*, or ordered-Olson result follows.