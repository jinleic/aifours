DISPOSITION: ACCEPT-WITH-FIXES

The core seeded argument passes. I found one repairable scope gap and two minor errors. All five files match the manifest, including the target SHA-256.

All “G” line references below mean `proof-SEEDG-r1.md`.

- **FATAL: none.**
- **MAJOR — missing prime restriction in the large-\(B\) corollary.** [G:237–239](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-r1.md:237) should explicitly assume **\(p\ge11\)**. Imported SEED-B assumes this, RA2 assumes \(p\ge11\), and RA3(a) assumes \(p\ge13\). On the printed parameter domain, \(p=7\) permits \((k_B,B)=(2,2),(1,3)\), both with \(k=R=11,\kappa=4\). They fall outside the corollary’s listed remainder but are not covered by those cited results. Add \(p\ge11\), or supply a separate small-prime argument. This concerns coverage; these parameter tuples are **not group counterexamples**. The main SEED-G theorem can retain \(p\ge5\).
- **MINOR — false size assertion.** [G:156–158](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-r1.md:156) says \(k\ge12\). The stated setting gives **\(k\ge7\)**, since \(\kappa\ge2\) and \(k\ge2\kappa+3\). For example, the printed constraints permit \((p,k,\kappa,B,E)=(5,7,2,1,0)\). Replace the parenthesis accordingly. The path’s ends are nonadjacent already for \(k\ge5\), so the construction survives.
- **MINOR — off-by-one equivalence.** At [G:126](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDG-r1.md:126),
  \[
  \left\lfloor\frac{d_u+B}{2}\right\rfloor+1<d_u+1-k_B
  \quad\Longleftrightarrow\quad d_u>2k_B+B,
  \]
  rather than \(d_u>2k_B+B-1\). For \(k_B=1,B=2,d_u=4\), both compared terms equal \(4\). This example fits \(p=17,k=18,\kappa=3,E=4\), including the relevant branch condition. The downstream bound \(\lambda(\{u\})\ge k_B+B+1\) remains valid.

The substantive proof checks pass:

- **C+ is used within the required hypotheses.** Its [proof, lines 52–88](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-parent-inputs-v1/inverse-run-count/mixdef-high/c6/c5-fixes/proof-Cplus-r2.md:52) needs from the lifts precisely integrality, \(\sum x_t=p\), and every proper-pattern lower bound. The singleton bound in branch (A-ii) is included. SEED-G supplies these, without asserting or importing (H). The additional bound \(d_t\le E+1\le p-3\) is available.
- **Canonical lifts, actual arcs, and no wrap are sound.** G:37–45 establishes uniqueness: the singleton interval contains at most \(p\) integers. GS takes differences of representatives from the two actual pattern arcs, then intersects with the canonical interval. Its generic calculation uses arbitrary integer \(d_t\), covering multi-letter aligned runs, pairs with \(d_t=0\), and long anti runs. NW correctly incorporates excess through \(\Delta_0=p-\kappa-E/2\).
- **SCW-G handles arbitrary weights.** Every \(3\times3\) term pairing in both extension inequalities, for both signs of \(d\) and for \(d=0\), satisfies its stated target using (2.1) and \(|d|\le E+1\). No singleton-only assumption enters. The two-run lower step correctly switches to canonical lower bounds when \(2\Delta_0\ge A+4\). After the minor equivalence correction above, that argument remains valid. The pin gives \(1\le X_{[k]}\le2p-1\), hence \(X_{[k]}=p\).
- **SA/PA configurations exist for every target run.** Deleting \(t\) and its neighbours handles cyclic wrap. The interval counts give the stated ceilings; selected blocks are separated, \(t\) is isolated from them, and the block counts are \(m,m+1\). The budgets \(y\le m+E-e_t\), respectively \(2m+E-e_t\), justify the generic-arc inequalities for every permitted run type.
- **RA2/RA3 arithmetic is correct at their stated primes.** RA2 gives aligned seed \([0,0]\) and anti seed \([-1,-1]\), inside the canonical ranges, so \(\sum x_t=-2\not\equiv0\pmod p\). RA3 gives \([0,1]\) and \([-1,0]\) in both cases. The integer rounding handles the exceptional availability checks at \(p=11\) and \(p=13\).

Fresh checks using independently written arithmetic—not claimant code—found no failures in 386,412 weighted extension configurations, 11,484 two-run cases, 148,288 cyclic constructions, 390,532 generic-arc checks, and the RA formulas through \(p=257\). These support the written arguments; they do not replace them.

The exact accepted scope is conditional SEED-G for \(p\ge5\), SA/PA within their stated regions and C+ count condition, and RA2/RA3 at their explicitly stated prime bounds. Universal quality-seed existence remains unproved.

For \(p\ge11\), the six old Claim E′ exceptions actually acquire written uniform exclusions here: SA witnesses \(m=4,5,7\) cover \((11;4,2),(13;5,3),(17;7,4)\); PA witnesses \(m=4,4,5\) cover \((11;5,2),(13;6,2),(13;7,2)\). Thus the remaining all-single-letter candidates with \(B\ge2\), relative to these uniform results, lie among large-\(B\), \(B\ge4\) classes outside SA/PA, plus \((11;5,3)\). Excess words outside the applicable seed/count conditions remain unresolved by this argument.

The census totals and external IND* receipts are not independently certified here. No full RUNS/PAR/Olson conclusion follows, and no relaxed-window solution is treated as a group counterexample.