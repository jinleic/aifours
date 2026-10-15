# 无线网络时变信道随机接入：强稳定性与实现代价

Snapshot: **2026-10-14, America/Los_Angeles**.
Book verdict: **PARTIAL — do not count this chapter as solved**.
FRONTIER: scoped classical derivation / Certification candidate;
**NOVELTY-UNCLEAR**. No Lean kernel verification, publication novelty, practical
implementation claim, or proof that the remaining problem is currently open.

## Outcome first

[Theorem 2 in proof.md](proof.md#3a-continuous-time-markov-channels-without-frozen-channel-assumptions)
is a complete written construction and Foster–Lyapunov derivation for **every
finite interference graph and every strictly admissible load**, with bounded
iid arrivals and **finite-state irreducible continuous-time Markov jump
channels**, whose states may change at any real time and have finite maximal
exit rate. Its guarantee is stronger than the book's strong stability:

\[
 \exists\theta>0:\quad
 \sup_{t\ge0}\mathbb E e^{\theta\|Q(t)\|_2}<\infty,
 \qquad\text{hence}\quad
 \sup_t\mathbb E\sum_iQ_i(t)<\infty.
\]

The algorithm has no central MaxWeight computation and no global queue maximum.
At each local random clock ring, a link uses its own sampled queue, its own
current channel and carrier sensing. **The price is unacceptable for ordinary
hardware:** a shared slot counter, synchronized queue sampling, perfect
instantaneous sensing/switching, continuous exact own-channel CSI with zero-delay
rate adaptation, and rate
\(R_t=e^{(t+1)^2}\) per link, forever. There are
\(ne^{(t+1)^2}\) expected clock rings in slot \(t\). The controller withholds
data for the initial \(\delta_t=1/(t+2)\) fraction, but subsequent switches
have zero additional guard time. Its policy is time-inhomogeneous and stores
one local slot-start queue sample. These are explicit added architecture
assumptions, **not a solution of the book's simple-policy requirement**.
The counter substitutes for global worst-case queue-growth and channel-speed
bounds, and the cost of distributed MaxWeight-quality sampling is exposed,
not eliminated. Time-scale separation is constructed by the clock and the
vanishing window; no comparable-clock/channel-rate guarantee is proved.
Statewise memorylessness and time-homogeneity are different; the book does
not formally define the former, so no impossibility is inferred from wording.

The preceding Theorem 1 separately treats Markov **block-fading**, with control
clocks running only in the shrinking window and one frozen data schedule per
slot. It is not substituted for the continuous-time model. Theorem 2 actually
allows channel jumps during both control and data transmission, and proves the
necessary tracking estimate instead of assuming instantaneous Gibbs sampling.

## 1. Exact book statement and translation

- Book: 《10000个科学难题·信息科学卷》.
- Chapter: **无线网络调度策略的稳定性及分布式实现** / *Stable Scheduling for
  Wireless Networks and Its Distributed Implementation*.
- Authors: **关新平、杨博**, 上海交通大学自动化系.
- Printed pp. **731–734**; PDF pp. **752–755**.
- All four page images were read directly. Preserved images:
  [731](sources/p-0752.png), [732](sources/p-0753.png),
  [733](sources/p-0754.png), [734](sources/p-0755.png).
- [Chinese target passages, mathematical transcription and English translation](sources/problem.zh-en.txt).
  [Original extracted text](sources/text.txt) is preserved but garbled and is
  **not** formula authority.

Printed p. 732 defines strong stability by

\[
 \limsup_{T\to\infty}\frac1T
 \sum_i\sum_{t=0}^{T-1}\mathbb E[Q_i(t)]<\infty. \tag{B2}
\]

Its implementation requirement is:

> “满足镇定队列、资源有效利用的调度算法必须是简单的、分布式的、无记忆的策略。”

Translation: *A scheduling policy that stabilizes queues and efficiently uses
resources must be simple, distributed and memoryless.*

Printed p. 733 states the target:

> “在时变链路速率情况下的基于队列的随机接入算法及其稳定性还未被人们解决。”

Translation: *Queue-based random-access algorithms and their stability under
time-varying link rates have not yet been resolved.*

The book motivates local queue-dependent access probabilities and instantaneous
CSI, while separately listing fast convergence, delayed/inaccurate CSI, and
retransmissions as future directions. None of those separate future directions
is claimed solved here.

## 2. Formal contract and model match

Let \(G=(V,E)\) be an arbitrary finite undirected conflict graph and
\(\mathcal I(G)\) its independent sets. Let \(C(u)\) be an exogenous
irreducible finite-state continuous-time Markov chain, with stationary law
\(\pi\) and capacities \(0\le C_i\le c_*<\infty\). Independent arrival
vectors are iid over integer slots, bounded by \(a_*\), and have unknown
mean \(\lambda\). Arrival-vector coordinates and channel coordinates may
be dependent across links. Initial queues are arbitrary deterministic finite
values. Work is divisible; arrivals are inserted at slot end.

**For every** such model, **for every** \(\lambda\) for which there exist
\(\epsilon>0\) and channel-conditioned schedule distributions
\(\alpha_c\) satisfying

\[
 \sum_c\pi(c)\sum_{\sigma\in\mathcal I(G)}
        \alpha_c(\sigma)c_i\sigma_i\ge\lambda_i+\epsilon
 \quad\text{for every }i,
\]

Theorem 2 proves the uniform exponential moment stated above. The same policy
works without knowing \(\lambda,\epsilon,\pi,\Gamma,n,a_*\), or \(c_*\).
These quantities affect the proof constants only. No graph class, topology
fraction, or load-dependent controller tuning is used.
The entire channel process, arrival sequence and all control randomness are
mutually independent; the initial channel law is arbitrary.

| Item | Book / matched feature | Additional assumption or unresolved issue |
|---|---|---|
| Objective | Exact (B2); result proves a stronger uniform moment bound | Not merely rate stability or recurrence |
| Interference | Arbitrary graph and feasible independent sets | Perfect conflict-edge sensing; no hidden terminal |
| Arrivals | Exogenous queue input | Bounded iid vectors; not implied by long-run means in book |
| Channels | Time-varying rates; local instantaneous CSI | Finite-state exogenous irreducible Markov law; bounded rates |
| Continuous-time jump fading | Theorem 2 permits finite-state jumps at all real times | Continuous exact own-channel CSI and zero-delay rate adaptation; continuously varying capacities are excluded |
| Information | Own queue/channel and local carrier sensing | Shared synchronized slot counter; one sampled queue value |
| Resource use | Every strict load inside ideal service region | Shrinking control overhead; zero per-switch guard time |
| Distributed operation | No queue exchange, global maximum, or central optimizer | Unbounded clock intensity and real-valued probability operations |
| Simplicity | Local update is elementary | Total control work is superexponential in slot index, not low-cost |
| Memorylessness | No historical traffic-rate estimation | Theorem 1 is statewise memoryless at slot boundaries; Theorem 2 stores a local queue sample; both use time, not a time-homogeneous policy |

### Proof structure: no tracking lemma left unstated

1. The frozen heat-bath generator has the independent-set Gibbs law by exact
   detailed balance.
2. In each interval of length \(1/R\), every node rings exactly once and all
   marks force zero with probability
   \(e^{-n}\prod_i(1+e^{q_ic_i})^{-1}\). This is an explicit all-state coupling
   event and supplies a nonasymptotic mixing bound.
3. For finite-state continuous-time Markov jump channels, a preceding window of length
   \(\delta_t\) contains a jump with probability at most
   \(\gamma_*\delta_t\), where \(\gamma_*\) is the finite maximum exit
   rate. On the complement, the conditional coupling estimate applies, even
   from an arbitrary schedule at the window start.
4. Entropy loss, mixing error, channel-jump error and paid control time together
   cause an additive weighted-service loss **uniform in time, not in channel
   speed**. In the proof's notation
   \(K^{\rm ct}\le K+\gamma_*nc_*\max(q_*/2,a_*)\).
   The clock/window constructs separation against both queue growth and every
   fixed finite channel speed, without knowing those bounds.
5. A finite-state Poisson equation gives the Markov-channel service average
   over a fixed proof horizon. The resulting quadratic drift is
   \(\mathbb E\Delta_T L\le K_T-\beta\|Q\|_1\).
6. Bounded increments turn that drift into an exponential Foster inequality
   and a uniform exponential queue moment. This last step prevents a silent
   substitution of rate stability for strong stability.

[Complete proof, all constants and both models](proof.md).

## 3. Dated primary-literature status, 2013–2026 search

The closest result **verified here**, not asserted the latest result in the
entire literature, is Yun–Shin–Yi's 2016 journal article. Targeted searches
included 2013–2026, exact strong-stability phrases and later citations, then
primary sources were opened. Search misses do **not** establish present
openness or novelty. See the [source/status ledger](sources/status.json).

| Primary source | Precisely established / model | Why it is not a verified full match |
|---|---|---|
| Yun, Shin, Yi, [MobiHoc 2013](https://arxiv.org/html/1306.2009), DOI [10.1145/2491288.2491303](https://doi.org/10.1145/2491288.2491303) | Channel-aware exponential CSMA; arbitrary graph; finite-state irreducible continuous-time Markov fading | Declared stability criterion is rate stability, not (B2) |
| Yun, Shin, Yi, [IEEE/ACM ToN 2016](https://yung-web.github.io/home/Publication/Journal/Distributed_Medium_Access_Over_Time-Varying_Channels.pdf), DOI [10.1109/TNET.2015.2503394](https://doi.org/10.1109/TNET.2015.2503394), Thm. 4.2 | Queue-based adaptive CSMA; Bernoulli arrivals; positive discrete channel levels; exact instantaneous sensing | Definition 2.1 still defines throughput using rate stability; queue rule uses \(Q_{\max}\) or its distributed estimate; full proof assigned to supplementary material |
| Li, Eryilmaz, [TWC 2013](https://www.ele.uri.edu/faculty/binli/papers/TWC2013.pdf), DOI [10.1109/TWC.2013.062413.121125](https://doi.org/10.1109/TWC.2013.062413.121125) | Fast-CSMA under fading, chiefly inelastic traffic / virtual queues | Fully connected graph; idealized theorem has zero hitting time; general topology explicitly left for future work |
| Swamy, Ganti, Jagannathan, [NCC 2015](https://arxiv.org/html/1504.07825) | Spatial CSMA with iid Rayleigh fading, statistical CSI, SIR-based average success rates | Different interference and capacity model; not a matched instantaneous-CSI graph theorem |
| Shneer, Stolyar, [2019 version](https://arxiv.org/html/1810.08711v2) | Stochastic stability for a local-priority access protocol | Static unit transmission rates; conservative protocol's region; authors explicitly do not target maximal stability |

The 2016 queue rule, read directly from its
[p. 9 image](sources/yun-shin-yi-2016-page9.png), is
\(r_i=\max\{w(Q_i),\sqrt{w(Q_{\max})}\}\),
\(w(x)=\log\log(x+e)\), with both activation and holding rates scaled using
\(Q_{\max}\). The author notes distributed approximation can replace that
maximum **without changing rate stability**. That sentence is not promoted to
a finite-mean-queue guarantee. A journal's “throughput optimal” label and
simulation plots of average queues do not establish (B2).

**Still unverified:** the mathematical content of the 2016 supplement and an
exhaustive later-citation audit for stronger moment bounds. The official
[Supplemental Items page](https://ieeexplore.ieee.org/document/7373692/media)
was opened in a normal browser and its actual archive link was found. `curl`
received HTTP 418; the browser session was redirected to article HTML, not the
ZIP. See the [access receipt](evidence/supplement-access.json). No sign-in,
access-control bypass or external contact was attempted. Main papers are
preserved locally. An author-index page generated in 2026 is not a new 2026
publication. This proof is not presented as an improvement over a fully
matched strong-stability baseline that has not been ruled out.

## 4. Negative results: exactly what they do and do not refute

1. **A real tracking pitfall.** For one conflict edge with channel states
   \((1,0)\), \((0,1)\) flipping at rate 1, rate-1 heat-bath clocks and
   good/bad activities 9/1, the actual joint stationary useful service is
   **\(37/79\)**. Treating the instantaneous frozen Gibbs law as the joint
   invariant distribution wrongly predicts **\(9/11\)**. The exact six-state
   generator rejects this shortcut. At clock rate 100 the actual value is
   **\(58/73\)**, still not \(9/11\).
2. **A fixed-overhead architecture cannot reach ideal full capacity.** One
   unit link, a fixed 1/4 control fraction, and arrival rate 7/8 force at least
   1/8 queue growth per slot. This is not an impossibility for all distributed
   policies.
3. **The printed mean assumptions are insufficient.** Bounded deterministic
   arrivals 2 for \(k\) slots followed by 0 for \(3k\) slots in cycle \(k\)
   have mean 1/2 against unit service, and are rate-stable, but the exact
   average backlog through cycle \(K\) is **\((2K+7)/12\to\infty\)** even
   for a central work-conserving policy. All arrival moments are bounded;
   temporal regularity is missing. This is **only an assumption-gap example**,
   never counted as a solution of the intended scheduling question.

## 5. Exercised verification and isolated parent replay

The dependency-free checker is [work/check.py](work/check.py). The positive
run completed with **PASS**, in **1.532 s** on this worker:
[evidence/check.json](evidence/check.json).

- Exact rational detailed balance / stationarity on **75** labeled graphs of
  1–4 vertices, covering **599** independent-set states.
- **13,366** all-zero reset maps checked over all update orders and initial
  schedules on those graphs.
- Exact frozen service vectors, exact finite-state Poisson equation and
  strict admissibility witness: each link's comparison mean is 1/3, arrival
  mean 1/4, slack 1/12; proof horizon 11.
- Exact six-state continuous-channel stationary law and rejected false
  product law; fixed-overhead and bounded-burst negative controls.
- **Actual block-fading controller:** 96 independent three-slot trajectories,
  **588,344** uncapped Poisson-clock events; all four Markov transition types
  observed; no conflicts.
- **Actual continuous-channel controller:** 48 independent three-slot
  trajectories, **1,176,192** uncapped clock events, **18 channel jumps during
  control and 28 during data**, no conflicts. This is not a simulation that
  freezes channels or replaces the controller with stationary samples.
- An externally selected mutation, `--tamper reverse-activation`, exited 1
  with the expected stationarity failure:
  [evidence/tamper-reverse-activation.json](evidence/tamper-reverse-activation.json).

The short event-driven traces test implementation semantics, not infinite-time
stability. Later clock rates become impractical to simulate; no long-run
simulation is passed off as the proof. All outputs bind the source/proof/checker
SHA-256 hashes. No build, global workspace audit, package installation or
infrastructure action was run.
The checker was run once after both models and algorithms were complete.
Subsequent referee clarifications made the filtration, mutual independence,
total-variation convention and scope language explicit, without changing the
checker or its mathematical algorithms. Accordingly the checker receipt's
proof hash is the pre-clarification snapshot. Round 2 binds the extended proof
before its final notation/scope clarifications; these post-review edits were
not sent for a third review. The exact snapshot relationship is recorded in
`evidence/final-bindings.json`. No hash mismatch is represented as a fresh replay.

Parent replay writes only the selected output path:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B \
  information-science/wireless-timevarying-strong-stability/work/check.py \
  --output /Users/jinleic/jinleic-workspace/scratch/ai4s-wireless-timevarying-strong-stability/parent-check.json
```

Expected rejected mutation (exit **1**, not a successful theorem check):

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B \
  information-science/wireless-timevarying-strong-stability/work/check.py \
  --tamper reverse-activation \
  --output /Users/jinleic/jinleic-workspace/scratch/ai4s-wireless-timevarying-strong-stability/parent-tamper.json
```

## 6. Exact remaining blocker

No intrinsic impossibility for all local distributed policies is proved here.
Here **autonomous** means counter-free and time-homogeneous, with rates based
only on permitted local state (bounded or state-dependent). Theorem 2 supplies
strong stability only for its counter-driven unbounded-rate controller.
To settle the intended simple-policy problem, remove that architecture while
retaining all graphs, all strict loads and finite expected backlog. One
sufficient mathematical bridge would be a uniform drift such as
\(\mathbb E[\Delta_T L\mid\mathcal F_t]\le K_T-\beta\|Q\|_1\)
for a concrete autonomous local controller in finite-state continuous-time
Markov jump channels, or a different fully justified route to finite queue
moments.
Existing rate-stability statements and unproved mixing/tracking assumptions
are not that bridge. A positive per-switch delay, finite rate cap, stale CSI or
retransmissions change the physical service region and need a newly matched
contract; they cannot be silently grafted onto this theorem.

## 7. Independent hostile mathematical review

Two bounded other-vendor CLI reviews used the configured
**Claude Opus 5.5, maximum effort**, with `--safe-mode --no-chrome --tools ''`
and no permissions, session persistence, stdin, or nested delegation. Complete
proofs and exact input hashes were embedded in saved prompts.

- [Round 1](evidence/claude-review.json): successful result event,
  **ACCEPT_SCOPED** for Theorem 1 only. It independently rederived the
  five-lemma argument and negative examples. Its definition, filtration,
  TV convention, symmetry and scope findings were addressed.
- [Round 2](evidence/claude-review-final.json): successful result event,
  **ACCEPT_SCOPED** for **both Theorems 1 and 2**. It analytically rederived
  the no-jump window conditioning, integrated service bound, continuous-time
  Poisson equation, quadratic drift and exponential-moment step, and found
  no mathematical defect. Minor notation/independence and scope clarifications
  were applied afterward.
- [Every finding and disposition](evidence/referee-dispositions.json);
  [final snapshot bindings](evidence/final-bindings.json).

The referee did not run the checker, inspect the page images, or independently
retrieve the literature. Its acceptance is a classical mathematical review,
not kernel certification, a replay receipt, or a novelty determination. An
overstrong round-1 suggestion that superexponential cost was intrinsically
necessary was **not adopted**; round 2 agreed that rejection was justified.
Both reviews explicitly reject counting this as a solution of the book.

