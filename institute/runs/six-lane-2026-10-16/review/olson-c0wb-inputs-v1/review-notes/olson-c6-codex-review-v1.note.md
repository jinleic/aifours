DISPOSITION: ACCEPT-WITH-FIXES

No substantive gap found in SEED-B, the C+ weakening, or the revised SEED proof. One minor rounding correction is needed.

- **MINOR — exact gain needs an integer bound.** [SEEDB:240–241](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:240) compares the real upper bound \((\delta-B-3)/2\) with the plain bound and claims an exact gain of \(\lfloor B/2\rfloor+1\). For \((p,k_B,B)=(17,5,4)\), those bounds are \(5/2\) and \(5\): their difference is \(5/2\), not \(3\). The actual integer seed cap is \(2\), so the intended gain is correct. Replace the quoted cap by
  \[
  \left\lfloor\frac{\delta-B-3}{2}\right\rfloor.
  \]
  This changes no lemma, theorem hypothesis, or proof step.

The substantive checks passed as follows.

**SEED-B: arbitrary placements and seeds.** The argument at [SEEDB:48–96](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:48) works for every run \(t\), including anti runs and runs adjacent to anti blocks. After deleting \(t\) and its neighbours, the remaining path has at least \(n-3\) aligned runs in at most \(B+1\) aligned intervals. Different intervals have an unselected anti run between them; the path endpoints are separated around the cycle by the deleted segment. Thus neither adjacency across intervals nor cyclic adjacency invalidates the configuration.

The available counts are at least \((n-3)/2\) isolated singles and \((n-B-4)/3\) separated aligned pairs. The displayed bounds on \(m\) imply both availability inequalities. Because both neighbours of \(t\) remain excluded, \(Q+t\) is proper and has exactly \(m+1\) blocks. All four generic arc values in (1.1) follow under the stated branch conditions.

Canonical lift uniqueness also holds: the singleton intervals contain respectively
\[
p-\lceil\delta/2\rceil-1,\qquad p-\lceil\delta/2\rceil
\]
integers, both fewer than \(p\). The strict inequalities in IS(d) exclude every nonzero multiple of \(p\) from \(x_t-z\).

**SL, SCW-B, and the pin.** I checked all 36 displayed term-sum bounds, including both removal kinds \(m'=m,m-1\) and both signs of \(d_t\). Writing \(h=\delta-B\ge4\), every sum is at least \((h+2)/2\), while every required seed target is at most \((h+1)/2\). The argument therefore accommodates anti-only blocks and blocks touching anti runs. See [SEEDB:103–142](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:103).

The two-run fallback is valid: failure of the canonical lower-bound tests gives respectively \(p\le3k_B-7,3k_B-5,3k_B-3\), which imply the common inequality needed for the seeded alternative. The anti-singleton complement is always one cyclic block, regardless of anti placement. Its bounds put the total lift in \([1,2p-1]\); congruence then forces \(X_{[k]}=p\). See [SEEDB:143–158](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:143).

**C0 and imports: hypotheses match; no circularity.** Here \(R_{\rm rot}=k\), excess is zero, \(\kappa=k_B+B\), \(A=p+k_B\), and \(n_{\rm ev,al}=0\). Region R gives \(k_B+B\le p-4\), hence both the rotation-total bound and \(k\ge2k_B+2B+3\) required by the imported setting. Theorem C case (i) uses the lifted constraints and their sum after their construction; it does not independently reuse (H). Thus [C0:162–173](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:162) legitimately finishes the argument. Neither IND* nor a computation is needed.

**Claim E and small primes.** The contradiction \(4p<75\) at [SEEDB:177–186](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:177) is correct. The same inequalities restrict the possible exceptional \(B\)’s; substitution gives exactly:

| \(p\) | Classes in R failing (E), listed as \((k_B,B)\) |
|---|---|
| 11 | \((4,2),(5,2)\) |
| 13 | \((6,2),(7,2),(5,3)\) |
| 17 | \((7,4)\) |

All four priority classes satisfy the singles branch. No boundary-case failure was found.

**Proposition AB.** [SEEDB:219–228](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDB-r2.md:219) correctly excludes every possible last plain-extension step, including removal of an interior run. Its necessary condition is \(f+e\le4\), yielding precisely the stated odd/even \(k_B\) thresholds. The universal result is a sufficient obstruction; the converse for the T1 classes remains explicitly a finite census claim.

**C+ C4: accepted.** At [Cplus-r2:59–87](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6-parent-inputs-v1/inverse-run-count/mixdef-high/c6/c5-fixes/proof-Cplus-r2.md:59),
\[
\Delta=k_B-c(Z)-m(Z)\in\mathbb Z.
\]
Consequently,
\[
|X_o|\ge2\Delta+\tfrac12\quad\Longrightarrow\quad |X_o|\ge2\Delta+1.
\]
The path blocks then supply at least \(\lceil|X_o|/2\rceil\ge\Delta+1\) independent runs. The remaining construction is unchanged. The revised bound with “\(-1\)” is justified universally. The diff contains no other change to the theorem’s mathematical argument.

**SEED-r3: no change to the proved result.** Comparison with r2 confirms unchanged theorem hypotheses, seed construction, certification inequalities, pin, and contradiction argument. S1–S4/S9/S10 revise explanations, references, scope bookkeeping, and receipt wording. The S10 parity statement also follows directly from \(\delta+3-w\ge2\lceil\delta/2\rceil\).

The scope is exact **as coverage of R∩(E)**. For \(p\ge19\), after the reviewed \(B=1\) closure, the potential residual lies among excess words and all-single-letter classes with \(B\ge2\) and \(2B+k_B\ge p-1\). At \(11,13,17\), retain the six listed exceptions unless separately invoking their asserted IND* coverage. That proof and its receipts are absent from this snapshot, so their closure is not certified here. This is not an exhaustive classification of globally open classes.

All ten manifest hashes match. The universal conclusions above rest on the written arguments. No relaxed-window solution is treated as a group counterexample.