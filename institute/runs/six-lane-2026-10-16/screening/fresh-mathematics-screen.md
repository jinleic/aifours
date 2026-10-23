# Fresh mathematics replacement screen — 2026-10-16 PT

Source: read-only scout `FreshMathScreen` (completed after 29m59s). This preserves its selection report as screening evidence. It ran nothing; hand calculations marked by the scout as its own are unreviewed.

## Ranked targets

### T1. Minimal squared coefficient of variation of ME(3)

- **Target.** Prove that inf SCV over order-3 matrix-exponential probability laws is the conjectured numerical value v₃≈0.200902, or give an exact nonnegative ME(3) density below it.
- **Book link.** Related to 位相型分布的最小表示, book p.544 / PDF p.560; not the book's literal question.
- **Open statements reported.** Horváth–Sáfár–Telek–Zámbó, <https://math.bme.hu/~safaro/cikkek/osafarepew.pdf>, p.1: "While there is a long standing conjecture that for the first non-trivial order, which is order 3, the cv cannot be less than 0.200902 but the proof of this conjecture is still missing." Also p.2 and arXiv:1901.08627 p.3; arXiv:2609.14612 abstract signals active numerical work.
- **Baseline.** v₃ known numerically; PH(3) minimum 1/3; single repeated real pole solved in arXiv:2608.29143.
- **Missing obligation.** Global lower bound over every pole configuration under semi-infinite nonnegativity, especially complex pair left of the real pole and distinct real poles.
- **Proposed method.** Extreme-ray reduction, compactified parameters, interval branch-and-bound and Krawczyk certification.
- **Risk.** Moderate prior-art risk; book/forward citations not fully checked; 2026 activity.

### T2. Commault–Mocanu Conjecture 1

- **Target.** For 0<c<a, b>0 and f̃(s)=c(a²+b²)/((s+c)((s+a)²+b²)), let n* = min{n : b ≤ (a−c)cot(π/n)}. Prove an order-n* PH representation always exists, or certify a counterexample.
- **Book link.** Smallest complex-pole case of the minimal PH-representation question in 位相型分布的最小表示.
- **Open statements reported.** Commault & Mocanu, Int. J. Control 76 (2003), copy <https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf>, PDF p.13: "Conjecture 1: There exists a representation of order n_min for such a distribution." Mocanu (1999) reportedly gives n_min+1. O'Cinneide's April 2017 lecture slide 55 lists it among conjectures; arXiv:2409.12673v2 p.2 describes minimal PH representation as far from solved.
- **Baseline.** n=3 solved by Commault–Chemla 1996 condition b ≤ (a−c)/√3; order n*+1 always achievable according to the cited source.
- **Scout lead, unreviewed.** Explicit four-state representation at boundary b=a−c using a cycle with exits from two states.
- **Proposed method.** Circulant forward/backward rates with Doob h-transforms; reduce positivity to trigonometric inequalities.
- **First obligation.** Prior-art screen of He–Zhang 2005, Mocanu 1999, Commault–Mocanu 2002 and Benvenuti's 2022 survey before freezing.

### T3. Finite order of ⟨a,b | a³=1, bab³=aba⟩

- Reported source: Rokicki, Math Stack Exchange 4942596 (2024-07-06) and Pestov's Monoid Zoo Open Question 1. Known finite quotients reach order 86,184; Todd–Coxeter exceeded 256GB and Knuth–Bendix ran two weeks without finishing.
- Proposed route: finite-index kernels, Reidemeister–Schreier, abelian invariants, L2-quotients.
- Risk: non-paper primary sources; possibly very large finite group; GAP installation and memory.

## Rejected or deferred

| Lead | Scout reason |
|---|---|
| O'Cinneide's PH density lower-bound conjecture | Probably true and likely only partial in bounded work |
| Rota classification lists | Research programme |
| Finite basis for four-element semirings | Claimed classified by 2609.39700 and 2609.32152 |
| Atiyah–Sutcliffe four points | Claimed by Svrtan; convex case by Bou Khuzam |
| Regular n-gon extension complexity | Heavily searched and active |
| Unpublished one-relation word-problem list | Not public; active groups |
| Hot spots on non-smooth domains | Conditional on unverified smooth-domain proof; double-eigenvalue route unbounded |
| Bin packing, k-server, TSP, spline and NMF questions | Flagships or not bounded |

## Parent disposition

T2 is the leading mathematics replacement because it is the smallest exact case of the book's minimal-representation problem and has a decisive symbolic verifier. It is not frozen until the named prior-art screen is complete. T1 is second. T3 is a fallback because its primary attestation is non-paper and computationally risky.
