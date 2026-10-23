DISPOSITION: ACCEPT-WITH-FIXES

## FATAL

none

## MAJOR

none

## MINOR

1. **The continuous-gap sentence omits the zero-weight exception.**  
   `inverse-run-count/mixdef-high/c6/proof-SEEDGstar-r1.md:44` assigns the far-side gap \((E-|d|+4)/2\) without restricting it to \(d\ne0\). At \(d=0\), **both** gaps are \((E+3)/2\).

   Hand substitution: \((p,k,\kappa,B,E,\Delta_0,d)=(11,14,4,1,2,6,0)\) gives \(L_A=L_B=11/2\), original targets \(3\), and gaps \(5/2\), whereas the printed far-side expression gives \(3\). Correct the sentence using the three-case table below. The lower bound \(3/2\), integer relaxation, and certification proof survive.

2. **The driver JSON does not record the CPU/file-size limits.**  
   `inverse-run-count/mixdef-high/c6/proof-SEEDGstar-r1.md:137–138` explicitly attributes those limits to `out/review_revision_runs.json`; that JSON, at `inverse-run-count/mixdef-high/c6/out/review_revision_runs.json:1–70`, contains no limit fields. The related wording at `inverse-run-count/mixdef-high/c6/proof-SEEDG-cls-r1.md:107–108` should make the same distinction.

   Correct statement: **the hashed driver configures CPU limits of 1,800/1,860 seconds and a 128 MiB file-size limit; the JSON records job arguments, times, statuses, exit codes, disk observations, and peak child RSS.** The configured limits are visible at `inverse-run-count/mixdef-high/c6/review_revision_runs.py:9–11`.

3. **The retained status line misidentifies the old checker’s arithmetic.**  
   `inverse-run-count/mixdef-high/c6/proof-SEEDGstar-r1.md:12–13` attributes “exact integer arithmetic” to `seedXstar2.py`, whose bounds use floating division and `math.ceil` at `inverse-run-count/mixdef-high/c6/seedXstar2.py:23–27`. The appended qualification at `inverse-run-count/mixdef-high/c6/proof-SEEDGstar-r1.md:126–128` correctly distinguishes the implementations.

   Correct the status line to say **exact finite-range computations using exactly represented integer/half-integer floating values in the historical checker; doubled-integer arithmetic in `seedXstar3.py`.** This is a description defect, not a failure of the reported \(p\le31\) computations.

**Residual severity counts: FATAL 0; MAJOR 0; MINOR 3.**

Review date: **2026-10-17 PDT**. The manifest was read before the proofs. All six target SHA-256 values matched the supplied pins using `shasum -a 256`. No mathematical program, claimant code, replay, solver, or compiler was executed; no network, writes, or delegation was used.

Below, `c6/` means the pinned directory `inverse-run-count/mixdef-high/c6/`; `out/` means its pinned `out/` directory. All cited numbers are `nl -ba` LF numbers.

**A. Finding map**

The four notes contain no other FATAL findings; their only MAJOR finding is SC-M1, mapped below.

| Review item | Status | Repair location and adequacy |
|---|---|---|
| **SC-M1 = SL-m14:** COUNT-only scope overclaim | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:112–118` preserves the one seed failure, distinguishes 377 class-condition failures from per-word failures, and confines the observation to the historical finite test. Mathematically adequate. |
| **SC-m1 = SL-m2:** minimum comparison | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:62–66` uses the minimum over term sums followed by integrality. Correct. |
| **SC-m2 = SL-m6:** erroneous \(k\ge12\) wrap reason | **ADDRESSED** | `c6/proof-SEEDG-cls-r1.md:34–40` proves properness and uses cyclic distance \(\min(4,k-4)\ge2\), with \(k\ge7\). Correct. |
| **SC-m3:** floating unrestricted `bounds()` | **ADDRESSED** mathematically | `c6/proof-SEEDGstar-r1.md:126–128,160–162`; `c6/seedXstar3.py:15–24` uses exact doubled expressions. Historical limitations are disclosed. MINOR-3 above is the remaining status-line wording. |
| **SC-m4:** task hash abbreviation typo | **NOT-A-LANE-ITEM** | It concerned the earlier review request. The full current pins match; `c6/proof-SEEDGstar-r1.md:5` uses the correct suffix `f5b22`. |
| **SC LF 129 = SL-m7:** stale r1 citations | **ADDRESSED** | `c6/proof-SEEDG-cls-r1.md:10,29,65,73` cites base r2. The configuration argument handles actual emptiness itself and imports no withdrawn empty-window inference. |
| **SC LF 145:** missing c4 label dependencies | **PARTIAL** | `c6/proof-SEEDGstar-r1.md:131–133` discloses the limitation; new headers, e.g. `out/revision_star3mode0.txt:1`, record c4 hashes. Their source bytes remain absent, so the label partition cannot be independently reconstructed from this snapshot. Endpoint criteria do not depend on those labels. |
| **SL-m1:** ill-formed per-run alternative | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:81–86` states a global actual-empty alternative before quantifying the nonempty seeds and P2. Correct. |
| **SL-m3:** facts-used list | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:26–29` supplies the block-count relations and floor inequality, and separates derivation from the later run-weight comparison. Correct. |
| **SL-m4:** LF proof completeness | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:30–42` supplies both positive vectors, the zero vector, reflection, and the discarded-term comparison. All are correct. MINOR-1 concerns the subsequent gap sentence. |
| **SL-m5:** redundant PIN | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:60–69,95–96,122,129` removes the premise and proves it for every canonical-contained seed. Correct. |
| **SL-m8:** allowed profiles versus code | **ADDRESSED** | `c6/proof-SEEDG-cls-r1.md:44–52` matches `c6/seedX3.py:33–53`, including the forced anti excess when \(a^*=1\). Actual triples are retained; unrealizable extras are conservative. |
| **SL-m9:** “class for class” evidence | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:119–120,142–144` distinguishes historical aggregate counts from new per-class records. The new record equality is independently checkable by text normalization and checksums. |
| **SL-m10:** QQ on conservative formal pairs | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:71–79` covers equal weights, excess-compatible formal pairs, and both block counts. The branch bounds suffice; see B5. |
| **SL-m11:** RA2 identification | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:114–115` and `c6/proof-SEEDG-cls-r1.md:84–85` correctly limit what aggregate receipts identify. New records additionally identify both classes as RA2; see C. |
| **SL-m12:** sensitivity and diagnostics | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:130,145–159` supplies requested one-unit tightening, diagnostics, stronger declared ablations, and a nonvacuous P2 fixture. The prose correctly avoids calling insensitive OPENE tests sensitive. |
| **SL-m13:** source provenance | **ADDRESSED** for new receipts | `c6/proof-SEEDGstar-r1.md:131–140`; `c6/proof-SEEDG-cls-r1.md:97–108`; `c6/seedX3.py:109–117`; `c6/seedXstar3.py:65–73`. New headers record source hashes; historical provenance is not retroactively reconstructed. Missing c4 bytes remain the separate SC-LF-145 limitation. |

SL-m15’s **seven** presentation items are covered individually:

| Sub-item | Status | Location and assessment |
|---|---|---|
| X/X* totals labelled [W+F] | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:112–114`. |
| OPEN0 column counts all passing classes | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:110–112`. |
| Misspelled star proof filename in code | **ADDRESSED** in replacement | `c6/seedXstar3.py:2` names `proof-SEEDGstar-r1.md`; replacement is declared at `c6/proof-SEEDGstar-r1.md:7–8,126`. Frozen code remains historical. |
| Code’s stale base citations | **ADDRESSED** in replacements | `c6/seedX3.py:17` cites r2; `c6/seedXstar3.py:2` points to the repaired proof, whose base import is explicit at `c6/proof-SEEDGstar-r1.md:14`. |
| E=0 documentation | **ADDRESSED** | `c6/seedX3.py:7,80`; documented at `c6/proof-SEEDG-cls-r1.md:97`. |
| CF′ properness and S1 total | **ADDRESSED** | `c6/proof-SEEDG-cls-r1.md:34–40`. Both arguments are valid. |
| Unsupported generic-seed endpoint-attainment gloss | **ADDRESSED** | `c6/proof-SEEDG-cls-r1.md:87–91` removes the universal inference. |

| C0WB review item | Status | Repair location and adequacy |
|---|---|---|
| **CL-m1:** per-word SA**/PA** and actual-empty alternative | **ADDRESSED** | `c6/proof-C0WB-r1.md:97–103` retains per-word (i)/(ii+), distinguishes sufficient class conditions, and retains actual emptiness. Correct. |
| **CC F3/empty-order requirements; CL-m2(a–c):** brackets, endpoints, certification premises, “proof of” citation | **ADDRESSED** | `c6/proof-C0WB-r1.md:88–96` explicitly brackets F3, dispatches actual emptiness before endpoints, names QS*/P2, explains automatic PIN, and invokes the proof stopped before C0+. Correct. The same distinction appears at `:34–36`. |
| **CC-3 = CL-m3:** profile-indexed endpoints and X** quantifier | **ADDRESSED** | `c6/proof-C0WB-r1.md:104–112` excludes guaranteed-empty profiles before endpoint use and uses \(a_\pi(d)\). Monotone transfer and the vacuous case are sound. |
| **CC-1; CL-m4(a):** false “exactly” converse | **ADDRESSED** | `c6/proof-C0WB-r1.md:82–84,144–148` claims only a sufficient family. Correct. |
| **CC-2; CL-m4(c):** unconditional exclusion of \(n_{\rm ev,al}=E\) | **ADDRESSED** | `c6/proof-C0WB-r1.md:82–83` states the necessary inequality instead. Correct. |
| **CL-m4(b):** confusing count-clause failure with \(2k_B>p\) | **ADDRESSED** | `c6/proof-C0WB-r1.md:83–84,145–146` expressly restricts the assertion to violation through the \(n_{\rm ev,al}\) clause. |
| **CC-4; CL-m5:** census ranges, [W+F], bookkeeping, zero Case-B replay | **ADDRESSED** | `c6/proof-C0WB-r1.md:114–148,153–157` supplies the lower prime bounds, labels finite instantiations correctly, separates mutation samples, and disclaims empirical Case-B validation. Its correction that MUT1 contains **no C0B replay** is supported by the receipt; CL’s 420-vector MUT1 assertion was inaccurate. |
| **CC-5; CL-m6(a–c):** path, source review qualifier, import list | **ADDRESSED** | `c6/proof-C0WB-r1.md:15–23` corrects the path, distinguishes the broader source findings from Lemma W, and lists cls and the repaired imports. It does not give clean acceptance to the frozen originals. |
| **CL-i1; CC LF 186–191:** imported minimum repair | **ADDRESSED** | `c6/proof-SEEDGstar-r1.md:62–66`; imported through `c6/proof-C0WB-r1.md:17–19,90–96`. |
| **CL-i2; CC LF 192:** imported wrap repair | **ADDRESSED** | `c6/proof-SEEDG-cls-r1.md:34–40`; import at `c6/proof-C0WB-r1.md:18`. |
| **CL-i3; CC LF 192:** historical floating bounds | **ADDRESSED** within stated scope | `c6/proof-C0WB-r1.md:155–157` confines old use to \(p\le31\) and directs future work to doubled integers. |
| **CL-i4; CC LF 192:** imported scope MAJOR | **NOT-A-LANE-ITEM for T3**; **ADDRESSED in T1** | T3 does not inherit it: `c6/proof-C0WB-r1.md:130–133` retains the seed failure. T1’s correction is at `c6/proof-SEEDGstar-r1.md:116–118`. |

**B. Mathematical adequacy by hand**

1. **The certification minimum is now literal and correct.**  
   Base `c6/proof-SEEDG-r2.md:52–53,117–125` gives
   \[
   \operatorname{lam}(y',m')+\operatorname{lamc}(y,m)
   =\min_iU_i+\min_jT_j
   =\min_{i,j}(U_i+T_j).
   \]
   If \(U_i+T_j\ge B_{ij}\) individually, this is at least \(\min B_{ij}=L_A(d)\). The sum is integral, hence at least \(\lceil L_A(d)\rceil\ge1-a_t\). The B-side uses \(\min V_i+\min S_j\) identically. Thus `c6/proof-SEEDGstar-r1.md:62–66` repairs the argument, not merely its phrasing.

2. **All LF closed forms and difference-vector entries check.**  
   With \(D=\Delta_0\), \(u\ge1\), \(C=(D+E-u+3)/2\), \(T=(D+E+4)/2\), the doubled differences are exactly
   \[
   2(A_i-C)=
   [D+E+u+1,\ D+u-1,\ u+1,\ D+u-3,\ D+E-u-1,\ 0,\ 0,\ 2\kappa-1],
   \]
   \[
   2(B_i-T)=
   [D+E,\ D+2u-4,\ 0,\ D+2u-2,\ D+E+2u-2,\ 2u-1,\ 2u-1,\ 2\kappa+u-2].
   \]
   At zero the A-vector is exactly
   \[
   [D+E+1,\ D-1,\ 1,\ D-3,\ D+E-1,\ 0,\ 0,\ 2\kappa-1],
   \]
   and B exchanges positions 2 and 4.

   These verify every entry at `c6/proof-SEEDGstar-r1.md:35–40`. For example, the potentially restrictive positive entry \(D+E-u-1\ge D-2\ge1\); at zero \(D-3\ge0\). The remaining signs follow from \(D\ge3,E\ge0,u\le E+1,\kappa\ge2\).

   Substitution \(d\mapsto-d\) exchanges A/B, with positions 2 and 4 exchanged. Consequently,
   \[
   L_A(d)=\frac{D+E+3-\max(d,-1)}2,\qquad
   L_B(d)=\frac{D+E+3+\min(d,1)}2.
   \]
   The discarded linear term exceeds the attained term by
   \[
   \frac{D+E-u-1}{2}\ge\frac{D-2}{2}>0.
   \]
   The stated closed forms and endpoint comparisons are correct.

3. **Continuous gaps require MINOR-1; all integer gains are correct.**  
   The corrected continuous table is
   \[
   \begin{array}{c|cc}
   d&L_A-(D-d)/2&L_B-(D+d)/2\\ \hline
   u>0&(E+3)/2&(E-u+4)/2\\
   0&(E+3)/2&(E+3)/2\\
   -u<0&(E-u+4)/2&(E+3)/2
   \end{array}
   \]
   Every entry is at least \(3/2\).

   For integer endpoints, write \(E=2h\), \(D=2q+\epsilon\), \(\epsilon\in\{0,1\}\). Comparing
   \[
   \left[\left\lceil\frac{d-D}{2}\right\rceil+1,\
   \left\lfloor\frac{d+D}{2}\right\rfloor-1\right]
   \]
   with
   \[
   [\,1-\lceil L_A(d)\rceil,\ \lceil L_B(d)\rceil-1\,]
   \]
   gives exactly
   \[
   \begin{array}{c|cc}
   d&\text{lower-end decrease}&\text{upper-end increase}\\ \hline
   u>0&h+2&J(u)\\
   0&h+2&h+2\\
   -u<0&J(u)&h+2
   \end{array}
   \quad
   J(u)=h+2-\left\lfloor\frac{u-\epsilon}{2}\right\rfloor.
   \]
   For instance, the positive upper difference uses
   \[
   \left\lceil D/2\right\rceil-\left\lfloor(D+u)/2\right\rfloor
   =-\left\lfloor(u-\epsilon)/2\right\rfloor.
   \]
   Negative \(d\) reflects the endpoints. Since \(u\le2h+1\), \(J(u)\ge2\) for either parity, including \(u=E+1\). Thus `c6/proof-SEEDGstar-r1.md:45–51` correctly claims at least two integer units before canonical clipping/P2.

4. **PIN is automatic for every run, and the pin is complete.**  
   Seed containment and P0 give
   \[
   b_a-\lambda(\{a\})
   \le p-\lambda(\{a\}^c)-\lambda(\{a\})\le p-1.
   \]
   After certification of \(\{a\}^c\), the total lies between
   \[
   a_a+\lambda(\{a\}^c)\ge1,\qquad
   b_a+p-\lambda(\{a\})\le2p-1.
   \]
   It is \(0\bmod p\), hence equals \(p\). This validates `c6/proof-SEEDGstar-r1.md:60–69` without a distinguished run or extra PIN premise.

5. **Extended QQ covers the conservative pair domain.**  
   At `c6/proof-SEEDGstar-r1.md:71–79`, the excess budget gives \(d_i\le e(d_i)+1\), so \(y=d_1+d_2\le E+2\). The formal weight domain gives \(y\ge-2\min(B,E+1)\ge-2B\).

   Against base `c6/proof-SEEDG-r2.md:139–151`:

   | Branch | Sufficient replacement condition |
   |---|---|
   | B-side linear term, uniformly over \(m=1,2\) | \(y\ge-2B-E-4\) |
   | A-side \(p-m+1\) term, uniformly over \(m=1,2\) | \(y\ge-2\kappa-E\) |
   | Contradiction in the canonical linear/linear fallback | \(y>-2B-2E-7\) |
   | Other singleton in the heavy branch | \(d_i\ge-B\) |

   All hold. The strict third bound is sufficient; sharpness is unnecessary. The other branches retain the upper bound \(y\le E+2\), the floor estimates, and \(F=\lfloor(A-y)/2\rfloor\ge0\). Neither distinct weights nor co-occurrence in a word is used, so equal weights and both block counts are covered.

   Canonical containment is sufficient. Its **lower** endpoint is genuinely needed for the general QS-to-P2 implication used here; its upper endpoint supports automatic PIN.

   Hand arithmetic showing why the lower bound cannot simply be omitted: take
   \[
   (p,k,\kappa,B,E,D)=(11,13,2,1,0,9),\quad d_1=d_2=1,
   \]
   and uncertified intervals \([-3,-3]\). They satisfy QS, but \(\lambda(1,1)=1\). With \(y=2\), \(\operatorname{lamc}(2,m)=6\) for \(m=1,2\), so P2 requires the lower sum to be at least \(-5\), while it is \(-6\). This concerns formal intervals, not a word or group counterexample. Canonical containment is not claimed necessary for every individual interval pair that happens to satisfy P2.

6. **SEED-G* and X* are well formed without PIN.**  
   `c6/proof-SEEDGstar-r1.md:81–86` discharges an actual configuration-derived empty intersection globally. Otherwise all endpoints exist. At `:90–100`, guaranteed-empty weights discharge profiles; an occurring empty nonguaranteed weight excludes the particular word. For remaining words, actual seed intervals lie inside \(\sigma_\pi(d)\), and QS*/P2 transfer under shrinking. Every actual pair has excess sum at most \(E\). No formal empty quality window is used as an exclusion.

7. **The allowed-profile filter matches the unchanged arithmetic.**  
   The read-only `diff -u seedX2.py seedX3.py` shows no changes to `profiles`, `exact_seed`, or `class_pass` arithmetic.

   | `proof-SEEDG-cls-r1.md` filter | `seedX3.py` implementation |
   |---|---|
   | `:45` parameter ranges | `:36–38` |
   | `:46` \(b^*=0\Rightarrow n_{\rm pr}=B\) | `:39` |
   | `:46` \(b^*\ge1\Rightarrow n_{\rm pr}+b^*\le B\) | `:40–41` |
   | `:47` \(a^*\ge2\) budget with \(e_{\rm an}=(b^*-1)^+\) | `:40,48–51` |
   | `:48` forced \(e_{\rm an}=E-n_{\rm pr}\), zero when \(b^*\le1\), minimum/maximal-run and anti-count checks | `:42–47` |

   The lower bounds at `c6/proof-SEEDG-cls-r1.md:50–52` follow from
   \[
   n_{\rm al}=k-B+e_{\rm an},\qquad
   n_1\ge k-B-E+2e_{\rm an}+n_{\rm pr}+a^*-2.
   \]
   Both grow with anti excess. For \(a^*=1\), anti excess is forced and \(n_1=n_{\rm al}\). The explicit E=0 profile agrees with the filters.

   CF′’s interval counts, integer rounding, separation, and properness at `:29–40` all check. The neighbours of \(t\) remain outside \(Q+t\), and its actual \(m+1\) blocks imply \(2m+2\le k\).

8. **C0WB’s theorem and uniform corollaries are adequately repaired.**  
   `c6/proof-C0WB-r1.md:88–112` now has the required F3 grouping, actual-empty discharge, QS*/P2 premises, automatic PIN, and certification-proof citation.

   The quality-seed estimate at `:66–68` gives
   \[
   d_t-a_t\le\frac{d_t+D}{2}-1
   \le\frac{2p-k-1}{2}\le p-k_B-1,
   \]
   using \(D+E=2p-k\), \(d_t\le E+1\), and \(k\ge2k_B+1\). Thus quality seeds make F3’s seed bound automatic.

   SA**/PA** retains the regions, \(b^*\), and \(m\) of base `c6/proof-SEEDG-r2.md:198–231`, including actual emptiness and per-word (i)/(ii+). The class conditions are explicitly sufficient.

   X** uses profile-indexed endpoints only after excluded profiles are dispatched. Since an actual lower endpoint satisfies \(a_t\ge a_\pi(d)\),
   \[
   \min(k_B-1,d-a_t)\le\min(k_B-1,d-a_\pi(d)).
   \]
   If every profile is already excluded, A-profile is vacuously true and no nonexistent endpoint is evaluated. This matches `c6/seedXX.py:39–60`.

9. **The repaired Case-B remarks and replay description are correct.**  
   `c6/proof-C0WB-r1.md:82–84,144–148` now states a one-way obstruction.

   Put \(T=k-k_B-2B\). Under \(k\ge k_B+3B\), \(T\ge B\). Violation through the integer count clause gives
   \[
   n_{\rm ev,al}\ge2T+n_{\rm pr}\ge2B+n_{\rm pr}
   >2B-n_{\rm pr}-2\ge B+n_{\rm an}-2,
   \]
   contradicting the Case-B necessary bound. This proves sufficiency, not a converse.

   `c6/replayW2.py:40–49` explicitly selects \(2k_B\le p\), \(k\ge k_B+3B\), and violation of the \(n_{\rm ev,al}\) clause. Its aspirational Case-B description does not establish Case-B coverage; the revised proof correctly reports that the receipts contain only Case-A kills.

**C. Receipt and provenance audit**

These are static receipt checks, not reproduced experiments.

| Claim | Result and pinned evidence |
|---|---|
| Historical counts reproduced | New X3 rows at `out/revision_X3p23.txt:73,209,574,1115,2161` match historical `out/seedX2_mode0.txt:2–6`. New star MODE0 rows at `out/revision_star3mode0.txt:73,209,574,1115,2161,4437,7273` match `out/seedXstar2_mode0.txt:2–8`. |
| New class-wise equality | Both X3 MODE0 and star MODE1 contain 2,154 class records. Removing only X3’s `written` field and star’s diagnostic suffix gives identical normalized SHA-256 `402603f7c5d4e325c091838ba0dd5b5ae11b2f19fba300d46c97f92e48b213d2`. This supports the new class-wise claim at `c6/proof-SEEDGstar-r1.md:142–144`; the old aggregate receipts alone do not. |
| MODE0 failures | `grep -c` confirms 70 QS* failure records. Summary counts are \(4+27+39=70\), at `out/revision_star3mode0.txt:2161,4437,7273`. Code returns at `c6/seedXstar3.py:46–49` before later P2 tests. No conclusion about those unexecuted tests follows. |
| Remaining OPENE record | `out/revision_star3mode0.txt:6802` records \((31;51,24,23)\), profile \((26,28,8,1,\mathrm{false})\), weight \(8\), seed \([8,8]\), required \([-2,7]\). The report at `c6/proof-SEEDGstar-r1.md:145–148` is accurate. |
| MODE3 | `grep -c` confirms 151 QS* failure records. Relative losses are 46 IS, 34 IE, and one OPENE `pass-noC+`; accepted OPENE exclusions do not change. See `out/revision_star3mode3.txt:1115,2161,4437,7273`. The newly lost OPENE class is \((29;47,22,21)\), at `:4006`. |
| Two-unit control | `out/revision_star3tight2.txt:575,1116,2162` gives losses \(16\) IE and \(34\) IS, with no accepted OPENE loss. Its declared mutation is at `:1`, implemented at `c6/star3_tight2.py:10–14`. |
| Four-unit control | `out/revision_star3tight4.txt:74,210,575,1116,2162` gives accepted OPENE losses \(20+35+103+152+320=630\). Other changes agree with `out/review_repair_summary.json:126–168`: W 63, IE 769 accepted plus 48 no-C+, SB 185, IS 201, and OPENE 6 no-C+. The SHIFT4 declaration is explicit at receipt `:1`. |
| Exact-bound controls | `out/star3_exact_controls.txt:1` records 528,214 small-domain weights, the specified huge input, and 15 additional huge bounds. `c6/star3_exact_controls.py:8–27` compares repaired bounds with the compact formula. For the specified input, hand substitution gives \(\lceil L_A\rceil=2^{59}+101\), \(\lceil L_B\rceil=2^{59}+102\). No old checker execution is represented. |
| Driver | `out/review_revision_runs.json:3–69` records four sequential completed exit-0 jobs and RSS 23,035,904 bytes. The source implements sequential waiting at `c6/review_revision_runs.py:14–29`. The limits-recording attribution needs MINOR-2. |

The **P2 negative fixture is valid for its declared purpose**. `out/star3_p2_negative_fixture.json:2–37` supplies canonical-contained QS* boxes for \((11;15,6,1)\). Here \(A=18,k_B=5,E=4\). For the two formal weights \((-1,-1)\) and \(m=2\),
\[
\operatorname{lamc}(-2,2)=10,\qquad
\operatorname{lam}(-2,2)=-5.
\]
Thus P2 requires sum range inside \([-9,5]\), while the injected boxes give \([-10,2]\). The real rejection and P2-only bypass acceptance are recorded at `out/star3_p2_controls.txt:1`; the mutation anchor is at `c6/star3_p2_controls.py:24–29`. This establishes a nonvacuous gate test, not GS realizability or a group counterexample.

The replay bookkeeping is:

| Receipt | C0W vectors | C0B vectors | Recorded outcome |
|---|---:|---:|---|
| `out/replayW_mut0.txt:6` | 1,320 | 360 | All kills; C0B entirely Case A |
| `out/replayW_mut1.txt:6` | 1,440 | **0** | 1,151 broken-M, 289 kills |
| `out/replayW_mut3.txt:6` | 1,440 | 420 | 622 C0W and 19 C0B kills lost |

Consequently, `notes/olson-c0wb-claude-review-v1.note.md:67` was wrong about MUT1’s 420 C0B vectors; `c6/proof-C0WB-r1.md:140–143` corrects it. MUT2 records 840 C0W kills at `out/replayW_mut2.txt:6`, supporting no observed failure, not tightness. Biased receipts `out/replayW2_mut0.txt:7` and `out/replayW2_mut1.txt:7` record 27/29 words and 1,080/1,160 Case-A kills, with zero Case-B instances.

The census statements also reconcile:

- `out/seedXX_R.txt:2–15`: OPENE \(26,225/22/602\), IE \(21,308/0/5,062\), with no unfinished region category, for \(11\le p\le61\).
- `out/seedXX_X.txt:2–8`: OPENE \(2,736+343+19+15+1=3,114\), for \(11\le p\le31\).
- `out/seedXX_A.txt:3–6`: ablation unfinished counts \(56,3,1\), for \(11\le p\le23\).

The **RA2 subtype is now identifiable**. Passing OPEN0 records are
\[
(29;55,26,2),\qquad(31;59,28,2)
\]
at `out/revision_star3mode0.txt:4413,7247`. Both have \(B=2\), \(k_B=p-5\), \(k=2p-3\), exactly base RA2 at `c6/proof-SEEDG-r2.md:244`. Therefore T3’s RA2 statement at `c6/proof-C0WB-r1.md:132–133` is supported. T1/T2’s statements about what the **aggregate receipt alone** identifies are also true; there is no contradiction.

The inspected replacement-source, control, fixture, driver, and review-note hashes match their corresponding pinned headers/summary entries. New headers record c4 hashes, but absent c4 source bytes still prevent independent reconstruction of labels. Historical receipts remain unhashed at execution time; new hashes do not repair that retrospectively.

**D. Changes beyond the declared repairs**

No substantive theorem change in the three supplied diffs falls outside the review findings or the r1 headers’ repair lists.

The additional two-/four-unit controls, injected P2 fixture, exact-bound controls, and per-class receipts extend the evidence requested by SL-m12/SL-m13 and SC-m3; they introduce no alternative valid theorem mode. Their descriptions are correct subject to MINOR-2. The \(p=5,7\) region remark at `c6/proof-C0WB-r1.md:153–157` is correct: even \(E\le p-4\) implies \(E\le2\), hence condition (i).

The new zero-weight gap error is a prose regression beyond the correct LF formulas. The floating/integer attribution is retained wording that conflicts with the new implementation distinction. Neither changes the certified implications.

**DF/C0W/C0B are byte-unchanged:** original `c6/proof-C0WB.md:27–69` equals repaired `c6/proof-C0WB-r1.md:39–81`. Both extracted blocks have SHA-256
`7e673e8b3282a9db6e6361e77f3d269b8f34ed59a90bfb277a658ec226f7e995`.
The supplied diff also shows the proof ending unchanged at `diffs/diff-C0WB-r0-r1.txt:49–57`.

The imports at `c6/proof-C0WB-r1.md:17–19` are the revised star/cls candidates. Their earlier originals’ ACCEPT-WITH-FIXES dispositions do not certify the revised bytes. This audit checks the relevant repairs; it supplies advisory mathematical assessment, not owner acceptance.

**Correctness.** The repaired minimum argument, LF formulas, integer relaxation, automatic PIN, extended QQ, profile filters, and C0WB theorem/corollary quantifiers are mathematically adequate. The three residual findings require small textual corrections.

**Novelty.** Relative to the supplied originals, the revisions complete and clarify existing conditional arguments and improve evidence attribution. External novelty and priority were not checked.

**Significance.** These repairs support the stated conditional routes and reported finite class instantiations. They do not add a general seed-existence theorem or turn census counts into a uniform result.

DELTA-VERDICT T1 proof-SEEDGstar-r1.md: DELTA-ACCEPT-WITH-NOTES
DELTA-VERDICT T2 proof-SEEDG-cls-r1.md: DELTA-ACCEPT-WITH-NOTES
DELTA-VERDICT T3 proof-C0WB-r1.md: DELTA-ACCEPT

The exact scope after these repairs is:

- **[W] written:** LF with the corrected zero-gap sentence; SCW-G*, extended QQ, conditional SEED-G*, PR/CF′; DF, C0W under its stated conditions, C0B under its stated defect bound; SEED-G** under actual emptiness or the seed hypotheses plus F1/F2/F3; unchanged-region per-word SA**/PA**; the sufficient implications underlying X/X*/X**.
- **[W+F] computer-assisted:** reported X/X* finite class applications for primes \(11\) through \(31\); X** applications excluding every word of 3,113 reported OPENE classes in that range; SA**/PA** region-class applications for primes \(11\) through \(61\). These computations were statically inspected, not replayed here.
- **[F] aids only:** class counts, label partitions, receipt summaries, mutations, and replay statistics. Missing c4 bytes limit independent reconstruction of the label partition.
- **Open under these tests:** \((31;51,24,23)\); ten OPEN0 seed-failing classes; the stated \(p=7\) and \((11;k_B,B)=(11;5,3)\) gaps outside SA/PA; general seed/certification existence outside the written regions and verified finite classes. No full NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, or ordered-Olson result is claimed or authorized.