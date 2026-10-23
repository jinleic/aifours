# Fresh information-science replacement screen — 2026-10-16 PT

Source: read-only scout `FreshInfoScreen` (completed after 33m28s). It ran no searches, solvers or model calls and wrote no files. Not finding a resolution is not proof of openness; likelihood estimates are inference.

| Rank | Target | Book link | Decisive certificate | Crowding |
|---|---|---|---|---|
| 1 | Exact asymptotic guessing number gn(R⁻), sibling gn(R^L) > 27/4 | 网络中的信息流最大化 pp.423–424; 网络信息论 pp.417–419; related network-coding question, not book wording | Exact rational upper-bound certificate giving 20/3, or code with \|S\|³ > s²⁰ | Low–moderate |
| 2 | Perfect versus linear secret sharing with five participants | 视觉密码方案的最优化问题 pp.409–410; related secret-sharing question | One perfect scheme outside the linear region | Moderate–high |
| 3 | Generic static-output-feedback stabilizability at n=mp, smallest cases (2,4), (3,3) | 静态输出反馈下的干扰解耦 pp.631–632; 关联系统分散控制 pp.661–663 | Non-degenerate rational V with empty real fibre for one case, certified exactly | High (AIM #319) |

## A. gn(R⁻)

- Baber–Christofides–Dang–Riis–Vaughan, <https://arxiv.org/pdf/1410.8349> v2, §8 p.23: "It would also be interesting to determine the exact value of gn(R−) as R− according to our calculations is the only undirected graph on at most 10 vertices whose guessing number remains undetermined." §6 p.15 asks whether non-linear strategies beat 20/3 or entropy inequalities reduce the upper bound to 20/3.
- Gürpınar, Kybernetika 60(5) (2024), §5.2: "For both of these graphs, the asymptotic guessing numbers remain unknown."
- Reported bounds: R⁻ lower/Ingleton 20/3; upper Shannon 114/17, Zhang–Yeung 1212/181, DFZ 59767/8929, Gürpınar 1847/276. R^L: 27/4 ≤ gn ≤ 359/53.
- Proposed attack [INFERENCE]: conditional Ingleton inequalities whose hypotheses are forced by exact functional dependencies, exact symmetry-reduced dual; non-abelian group-characterizable strategies for lower bounds. Possible quick kill: forced hypotheses may be Shannon-implied.
- Required checks: exact graph from the primary figure, replay Shannon/Ingleton/Gürpınar controls, exact decoding check for any code.

## B. Perfect versus linear secret sharing

- Khazaei ePrint 2026/1646 abstract: "Under statistical security, we show that the answer is five participants; under perfect security, the corresponding threshold remains unknown." It also states "One dual pair remains open."
- Reported baseline: 157 connected five-participant access structures; 17 exceptional; statistical beats linear on 15 of 17; Γ₃₀ statistical ratio in [14/9,1.6502), linear optimum 5/3.
- Required first step: full PDF, numbering, open dual pair and any perfect lower bound for Γ₃₀.
- High prior-art and scooping risk: two-month-old question in an active paper series.

## C. Generic SOF stabilizability at n=mp

- Eremenko note dated 2026-10-03, <https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf>, p.2: "Question. For which m and p the generic system with n = mp is stabilizable?"
- Eremenko–Gabrielov SIAM J. Control Optim. 41 (2002): stabilizable if n<mp or n=mp and m+p odd. AIM #319 lists open status, last checked 2026-09-17, and a discrepancy between versions on mixed-parity cases.
- Reported missing object: non-degenerate V in Q(2,6) or Q(3,6) such that the fixed polynomial equation has no real L; Byrnes–Anderson criterion then gives a nonempty open set for that one (m,p).
- One case is a partial answer to a full classification; high crowding.

## Screened out by the scout

- Tu–Deng: claimed proved in August 2026 (2608.14821, 2608.05187).
- Howard policy iteration: exponential lower bound posted (2609.40147); older Hansen–Zwick conjecture disproved (1407.4293).
- openai/math claims: Courtade–Kumar/Hellinger, Unique Games, mean-payoff and stochastic games.
- AIM-crowded: C₇ Shannon capacity, deletion channel, relay/two-way channels, fix-free codes, Cusick–Li–Stănică, Helleseth, Costas, Golomb–Welch.
- Lower value: Kurz table entries, Higman–Sims guessing number, five-element ideal secret-sharing characterization.

## Parent disposition

No information replacement is frozen yet. The SOF stabilization question has a single exact witness format and current primary attestation, but must be checked against Eremenko's exact Byrnes–Anderson reduction and AIM version discrepancy. gn(R⁻) is a lower-crowding alternative with a hard 13-year history.
