# Primary-source reading and comparison

As of 2026-10-14 (PT). Search results and OpenAlex are **discovery/indexing aids**, not theorem evidence. A failure to find a successor is not proof of openness or novelty. PDFs and extracted texts are in `../../../scratch/ai4s-adaptive-mean-field-game/sources/`; hashes and download receipts are in `../evidence/primary-downloads.json` and `../evidence/access-attempts.json`.

## P1. Li–Zhang, Automatica (2008): known dynamics

Tao Li and Ji-Feng Zhang, “Decentralized tracking-type games for multi-agent systems with coupled ARX models: Asymptotic Nash equilibria,” *Automatica* 44(3), 713–725. DOI [10.1016/j.automatica.2007.07.007](https://doi.org/10.1016/j.automatica.2007.07.007); [author PDF](https://lsc.amss.ac.cn/~jif/paper/%5BJ57%5D.pdf).

**Read:** model and assumptions §2; local/global admissible-control definitions and Theorem 2.1; mean-field construction §3; main stability/mean-estimation/Nash results §4. The proof appendices were not independently reverified line by line.

Model: vector discrete-time `x_i^+=g_i(x_i,t)+u_i+Lambda mean+w_i`, known local functions and known coupling matrix, `rho(Lambda)<1`; no unknown-parameter identification. Independent martingale-difference noises, finite conditional second moments, empirical covariance; target orbit and continuity assumptions enter subsequent results. The original article uses time-independent Phi, unlike the later adaptive article's time-dependent Phi.

The deterministic orbit `f^+=Phi(f)` and cancellation law already appear here, equations (11)–(12). Theorem 4.1 gives vanishing time-averaged mean-estimation squared error as N grows; known-parameter stability and Nash approximation are not new. This is not a solution for unknown A,B,Lambda.

## P2. Li–Zhang, IEEE TAC (2008): continuous time, cost coupling

Tao Li and Ji-Feng Zhang, “Asymptotically Optimal Decentralized Control for Large Population Stochastic Multiagent Systems,” *IEEE TAC* 53(7), 1643–1660. DOI [10.1109/TAC.2008.929370](https://doi.org/10.1109/TAC.2008.929370); [author PDF](https://lsc.amss.ac.cn/~jif/paper/%5BJ65%5D.pdf).

**Read:** abstract; §II model, admissible information and assumptions; §III construction; Theorems 4.1, 5.1–5.2 and optimality discussion. Some PDF mathematical glyphs are absent in extraction; no unviewed formula is used as a numerical citation.

This is a continuous-time Brownian linear system, with known parameter-dependent local dynamics and quadratic costs coupling through the population mean, including a positive control penalty. Compact population parameter support, stabilizability/detectability and existence of a bounded mean-field fixed point are required. It establishes the sample-path asymptotic Nash notions and long-run-L2 uniform stability. Continuous time, absence of the book's unknown dynamical mean-coupling term, and the control penalty are essential differences; mere sampling does not give the book's recursion and next-step tracking objective.

## P3. Li–Zhang, Dynamic Games and Applications (2013): closest result

Tao Li and Ji-Feng Zhang, “Adaptive Mean Field Games for Large Population Coupled ARX Systems with Unknown Coupling Strength,” *DGA* 3, 489–507. Published online 2013-05-29. DOI [10.1007/s13235-013-0084-9](https://doi.org/10.1007/s13235-013-0084-9); [author PDF](https://lsc.amss.ac.cn/~jif/paper/%5BJ93%5D.pdf).

**Read:** complete main text, including §2 assumptions, §3 algorithms, Theorems 1–3 and their proofs, and §6 conclusion. The numerical-example typography is not used as evidence for a simulation. Formula images of journal pp.501 and 503 were separately read: scratch `li-zhang-2013-page-13.png` and `...-15.png`. Their denominator is **1-alpha^2**, not `(1-alpha)^2`.

The crucial explicit limitation on p.490 is: “we assume the local dynamics of each agent is precisely known”. The model (1), p.492, is scalar, has known measurable `g_i`, unit input gain and unknown scalar `|alpha|<1` multiplying the unobserved PSA. It uses exactly the tracking-type cost in the book.

Hypotheses:

* A1: independent agent martingale-difference sequences, uniformly bounded conditional beta-moments for some beta>2, and time-average noise squares tending to a common sigma^2.
* A2: initial states independent of noise, with common finite mean x0.
* A3: the orbit `f(t+1)=Phi(t,f(t)), f(0)=x0` has finite limsup average square.
* A4: `f(T)^2/(1+sum_{t<T} f(t)^2) -> 0`.
* Uniform Lipschitz constant gamma for Phi is additional for the Nash result.
* A5: `f_lower=liminf T^-1 sum f(t)^2 >0` is additional for identification.

Theorem 2 gives, almost surely,

`limsup_T T^-1 sum |mean_N-f|^2 <= sigma^2/[N(1-alpha^2)]`,

uniform long-run-L2 stability, and

`max_i J_i <= sigma^2 + 2 sigma^2(gamma^2+alpha^2)/[N(1-alpha^2)]`.

Theorem 3 gives

`limsup_t |alpha_hat_i(t)-alpha|^2 <= alpha^2 sigma^2/[N(1-alpha^2) f_lower]`.

Thus **all four questions are answered for this explicitly narrower scalar, known-local-dynamics class**, with population-limit identification consistency; Theorem 3 does not assert exact fixed-N time consistency. Remark 4 states that identification consistency is unnecessary for asymptotic Nash optimality.

The conclusion p.505 explicitly leaves “both unknown local and global parameters” for further research. That is decisive evidence that P3 does **not** settle the printed unknown-A, unknown-B, unknown-Lambda problem. This 2013 statement alone does not establish its status in 2026.

## P4. Kizilkale–Caines (2013): unknown local dynamics, no dynamic mean coupling

Arman C. Kizilkale and Peter E. Caines, “Mean Field Stochastic Adaptive Control,” *IEEE TAC* 58(4), 905–920. DOI [10.1109/TAC.2012.2228032](https://doi.org/10.1109/TAC.2012.2228032); [author arXiv preprint 1210.5493](https://arxiv.org/abs/1210.5493), [PDF](https://arxiv.org/pdf/1210.5493).

**Read:** preprint model §II (equations (1)–(2)), A1–A5, adaptive observation definition, projection/dither design, Theorem 2.2, A7–A8 and Theorems 3.2–3.3. This is an author preprint, not a claim to have read every line of the final journal version. The current PDF typesetting bears a later “October 30, 2018 DRAFT” footer although arXiv submission is 2012; the exact fetched bytes are hash-pinned.

Dynamics are `dx_i=(A_i x_i+B_i u_i)dt+Ddw_i`, **without** an unknown `Lambda mean` term. Costs are long-run integrals of tracking error plus `u_i' R u_i`. Unknown local parameters are estimated by RWLS plus diminishing excitation. The population distribution parameter is learned by observing states AND controls of an increasing random subset of other agents, with observed fraction tending to zero. Compact controllable/observable parameter sets, a mean-field contraction, distribution regularity and identifiability are required. Theorem 2.2 gives fixed-agent local-parameter strong consistency, long-run-L2 stability, asymptotic Nash and cost convergence.

Differences are essential: continuous time, dynamical decoupling, control penalty and nonlocal observation for distribution learning. The last requirement conflicts with the example's prohibition on using other agents' states.

## P5. Nourian–Caines–Malhame–Huang (2012): adaptation of the leader's reference

Mojtaba Nourian, Peter E. Caines, Roland P. Malhamé and Minyi Huang, “Mean Field LQG Control in Leader-Follower Stochastic Multi-Agent Systems: Likelihood Ratio Based Adaptation,” *IEEE TAC* 57(11), 2801–2816. DOI [10.1109/TAC.2012.2195797](https://doi.org/10.1109/TAC.2012.2195797); [author PDF](https://people.math.carleton.ca/~mhuang/res/MojTac12.pdf); [institutional record](https://publications.polymtl.ca/14884/).

**Read:** retrieved the author PDF using an ordinary browser User-Agent after reader HTTP403; abstract, §II model/observation structure, §III assumptions, §IV likelihood-ratio estimator and Theorem 4.1, §V control construction and stability, §VI equilibrium formulation. The 16-page PDF is hash-pinned; proof appendix not independently checked.

This is continuous-time LQG with dynamical decoupling and cost coupling. The unknown is the member of a **finite class generating the leaders' reference trajectory**, not both unknown local matrices and unknown dynamical mean coupling. Followers observe a noisy random fraction of leader trajectories. Known own dynamics/parameter distributions, stabilizability/detectability, bounded mean-field solutions, and a finite-hypothesis distinguishability assumption enter. Under these conditions, the reference-model selector locks onto the correct model for sufficiently large observation populations, and the control laws have an asymptotic epsilon-Nash property. This does not answer the book's parameter-identification problem.

## P6. Chen–Li–Qiao, MCRF, online 2024 / issue 2025

Yan Chen, Tao Li and Nan Qiao, “Sampled-data based adaptive mean field games for leader-follower stochastic multi-agent systems,” *Mathematical Control and Related Fields* 15(3), 934–1019 (2025); online 2024-11-19. DOI and [publisher page](https://www.aimsciences.org/article/doi/10.3934/mcrf.2024059).

**Read:** publisher abstract, dates, references, access page and PDF link. **[UNVERIFIED: full hypotheses and proof]**. The linked PDF returned zero bytes in both reader and ordinary HTTP download; the HTML full-text route explicitly requested subscription/login or a $39 purchase. No purchase, login change or contact was attempted. OpenAlex's open-access label conflicts with the observed access route and is not treated as access proof.

The primary abstract explicitly says continuous-time LQG with sampled-data RWLS, leader/follower state aggregation, and asymptotic Nash as the sample step tends to zero. These are enough to exclude a claimed exact equivalence to a fixed-step discrete-time theorem with the printed next-step tracking cost. They are **not** enough to assert what every unknown coupling coefficient in the full paper is; that detail remains unverified.

## P7. Liu–Liu, CCC (2022): later discrete-time lead

Xiang-Yu Liu and Shu-Jun Liu, “Adaptive Mean Field Games for Large Population Discrete-Time Cost-Coupled Linear Quadratic Problems,” CCC 2022, 1293–1300. [DOI 10.23919/CCC55666.2022.9901983](https://doi.org/10.23919/CCC55666.2022.9901983); [IEEE record](https://ieeexplore.ieee.org/document/9901983).

**Read:** DOI metadata and P6's primary reference list. **[UNVERIFIED: full text, equations, precise hypotheses]**. IEEE returned a JavaScript/WAF page; OpenAlex locates no author PDF. Its indexed abstract describes unknown dynamical parameters and their population distribution, random regularization for controllability/observability, a Riccati estimate, stability and asymptotic Nash. That abstract is secondary-index evidence only. The title's cost-coupled wording suggests the Kizilkale–Caines lineage, but cannot itself establish absence of every dynamical mean term. This unresolved full-text comparison prevents claiming exhaustive prior-art clearance.

## Additional bounded follow-up

* [Wang et al., IET 2015, DOI 10.1049/iet-cta.2014.0625](https://doi.org/10.1049/iet-cta.2014.0625): primary abstract read; input-average dynamics, mean consensus and approximate mean information, not an abstract claim of simultaneous unknown local/global identification. Full equations [UNVERIFIED].
* [Wang et al., ICARCV 2014, DOI 10.1109/ICARCV.2014.7064391](https://doi.org/10.1109/ICARCV.2014.7064391): metadata only, [UNVERIFIED] full text.
* [Pavliotis–Zanoni, arXiv:2212.00403](https://arxiv.org/abs/2212.00403): primary abstract read; moments from one particle, polynomial interacting diffusions, infinite-time/infinite-population asymptotic unbiasedness. Not the controlled discrete-time Nash theorem; full comparison for novelty [UNVERIFIED].
* [Liu–Lo, arXiv:2501.11955](https://arxiv.org/abs/2501.11955): primary abstract read; inverse stationary nonlinear-PDE problem, not the book's online discrete-time adaptive control model.
* [Boveiri–Mohajerin Esfahani, arXiv:2608.02256](https://arxiv.org/abs/2608.02256): primary abstract read; high-dimensional discrete-time adaptive control and regret, not a stated theorem for hidden mean-field coupling. Full comparison [UNVERIFIED].
* [Więcek, DOI 10.1007/s13235-024-00570-x](https://link.springer.com/article/10.1007/s13235-024-00570-x): primary abstract and model read; multiple-population discrete-state/stochastic-kernel mean-field approximations with discounted/total rewards and known game kernels. Not this adaptive long-run tracking problem.

## Dated search log and limits

All searches below were performed on 2026-10-14. Exact query families and outcomes are retained in `../evidence/search-log.json`.

1. Searched the two 2008 book citations and retrieved author copies.
2. Retrieved and read the 2013 ARX paper before designing a purported extension; confirmed known local dynamics and the explicit remaining joint-unknown issue.
3. Retrieved the 2013 adaptive-control author preprint and 2012 leader-follower author PDF; checked model and information differences.
4. Searched “discrete-time” + “adaptive mean field” + “unknown”, and unknown-local/unknown-global/ARX variants through the stated date. Located CCC2022 and MCRF2024/2025 rather than a verified exact resolution.
5. Followed P6's primary references and queried OpenAlex citations of P3 (7 indexed results) and CCC2022 (1 indexed result). These are bounded index results, **not a complete citation graph**. Relevant successors are listed above; unrelated stochastic maximum-principle papers were not promoted to model matches.
6. Tried primary publisher/author routes for inaccessible references. P5 succeeded by ordinary public download; P6/P7 remained incomplete. No account or paywall bypass was used.

**Outcome:** no full solution for the book's all-unknown-matrix class was located in the primary texts actually read. This is weaker than “the problem is known open.” No novelty clearance is claimed for the new sparse-pilot certification.
