# Group B screening (computation and statistics): 11 articles

None of the 11 articles has a book-level question that could be fully settled in about a day, so there is no TARGET. Two articles contain a sub-question that later work has settled: the constraint-satisfaction dichotomy in 约束求解与优化, and the surrogate paradox in 因果推断. The other nine are research programmes, or in one case too hard.

- **Article page ranges.** For six articles the manifest range runs one page into the next article: 合作演化之谜, 几何计算的健壮性问题, 高维数据降维, 约束求解与优化, 网络的建模方法及建模 and 复杂知识表示与推理. The ranges below are the true ones, checked against the title headers.
- **Paths.** Local paths are relative to `/Users/jinleic/jinleic-workspace`.
- **`tractability` for the two solved items.** "HIGH" means the status can be confirmed by citing the published proofs. It does not mean the proof could be reproduced in a day.

```json
[
{
 "title_zh": "因果推断",
 "authors": "耿直（北京大学数学科学学院）",
 "book_pages": [596, 599],
 "pdf_pages": [617, 620],
 "question_zh": "从观察获得的数据中发现多因素之间的因果关系是统计学和人工智能领域长期关注的科学难题。……采用这些准则可能会出现因素A对因素B有正作用，且因素B对因素C也有正作用，而因素A对因素C有负作用的现象，称为替代指标悖论或中间因素悖论",
 "question_en": "Discovering causal relations among many factors from observational data is a long-standing problem in statistics and AI. … The existing surrogate criteria (based on conditional independence, principal stratification or causal graphs) still allow a case where A has a positive effect on B and B a positive effect on C, yet A has a negative effect on C. This is the surrogate (intermediate-variable) paradox.",
 "precision": "FORMALIZABLE",
 "formal_reading": "Only the surrogate-paradox item can be stated formally. The rest of the article (discovering causes from data, choosing confounders and instrumental variables, principal stratification, predicting interventions, learning causal networks) is a research programme. Reading, with the book's A, B, C as treatment T, surrogate S and endpoint Y: T is randomized; an unmeasured U affects both S and Y; the potential outcomes are S_t and Y_ts, and for a strong surrogate Y_ts = Y_s. The paradox is ACE(T→S) > 0 and ACE(S→Y) > 0 while ACE(T→Y) < 0. The task is a criterion stated in terms of what a surrogate study identifies, namely P(S,Y|T=0), P(S|T=1) and ACE(S→Y). (i) When the criterion holds, the paradox is impossible. (ii) The criterion is sharp: when it fails, some data-generating process consistent with those quantities shows the paradox. The faithful scope is binary T, S and Y, matching the book's example of arrhythmia suppression and cardiac arrest.",
 "status": "SOLVED-AFTER-PUBLICATION",
 "status_evidence": [
  {"claim": "The book describes the surrogate paradox and cites Ju & Geng 2010 as ref [7]. It asks for causal scrutiny of surrogate methods but states no precise open problem.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0617/p-0618.png", "quote": "因素A对因素B有正作用，且因素B对因素C也有正作用，而因素A对因素C有负作用的现象", "read_primary": true},
  {"claim": "Before publication: Chen, Geng & Jia (JRSS-B 2007) named the paradox and defined consistent surrogates to avoid it.", "url": "https://doi.org/10.1111/j.1467-9868.2007.00617.x", "quote": "Then we propose two notions for a consistent surrogate and a strictly consistent surrogate to avoid the surrogate paradox.", "read_primary": true},
  {"claim": "Before publication (the book's ref [7]): Ju & Geng gave a sufficient and almost-necessary condition on the causal model, using distributional causal effects.", "url": "https://doi.org/10.1111/j.1467-9868.2009.00729.x", "quote": "for a general distribution without any assumption of parametric models, we give a sufficient condition for a distributionally consistent surrogate and prove that it is almost necessary.", "read_primary": true},
  {"claim": "After publication: VanderWeele (Biometrics 2013) extended the conditions and stated what is necessary for the paradox to occur.", "url": "https://causal.unc.edu/wp-content/uploads/sites/1553/2011/08/Surrogates_Biom.pdf", "quote": "New results are given for consistent surrogates that extend the existing literature on sufficient conditions that ensure the surrogate paradox is not manifest.", "read_primary": true},
  {"claim": "After publication: Yin, Liu, Geng & Luo gave criteria that can be checked from observed data and proved them optimal.", "url": "https://arxiv.org/abs/1607.05454", "quote": "our criteria are optimal in the sense that they are sufficient and \"almost necessary\" to exclude the paradox", "read_primary": true},
  {"claim": "That result covers binary T, S and Y only; the paper leaves continuous and survival endpoints open.", "url": "https://arxiv.org/pdf/1607.05454", "quote": "We also leave the conditions to avoid surrogate paradox for continuous Y and survival outcome for future research topic.", "read_primary": true},
  {"claim": "The result is peer-reviewed: Scand. J. Stat. 47(1):84–103 (2020), DOI 10.1111/sjos.12398 (Crossref record).", "url": "https://api.crossref.org/works?query.bibliographic=Novel+criteria+to+exclude+the+surrogate+paradox+and+their+optimalities&rows=2&select=DOI,title,container-title,volume,issue,page,published-print,author", "quote": "Novel criteria to exclude the surrogate paradox and their optimalities", "read_primary": true}
 ],
 "tractability": "HIGH",
 "tractability_reason": "Settled for the binary reading. Yin et al. derive sharp bounds by linear programming and prove their observed-data criterion optimal. A sufficient and almost-necessary condition on the causal model already existed before publication (Ju–Geng 2010, the book's ref [7]). Re-checking the binary case independently reduces to a finite linear program over response types, plausibly about a day [INFERENCE]. Continuous and survival endpoints remain open, but the book's wording does not ask for them. The article's umbrella question cannot be settled.",
 "recommendation": "SOLVED-ELSEWHERE"
},
{
 "title_zh": "合作演化之谜",
 "authors": "王龙、陈小杰、伏锋（北京大学工学院系统与控制研究中心）",
 "book_pages": [117, 119],
 "pdf_pages": [138, 140],
 "question_zh": "对于强选择(博弈收益很大程度上决定了个体适应度)下动态图上的合作演化研究，尚无严格解析结果，是目前的一个公开难题。……可否提出一般模型，并结合自然选择和种群结构因素，统一合作得以演化的条件？",
 "question_en": "For cooperation on dynamic graphs under strong selection (where payoffs largely determine fitness) there are still no rigorous analytical results; this is an open problem. … Can one build a general model, combining natural selection and population structure, that unifies the conditions under which cooperation evolves?",
 "precision": "FORMALIZABLE",
 "formal_reading": "A finite population of N individuals lives on a time-varying graph G_t. Edges form and break at the same time as strategies update, either depending on strategies (active linking) or by exogenous switching. There are two strategies, C and D, with Prisoner's Dilemma payoffs T>R>P>S (or snowdrift payoffs T>R>S>P). Strategies update by imitation or birth–death, with fitness exp(βπ) or the Fermi rule. Selection is not weak: β is a fixed positive number or β→∞. The required result is a rigorous closed-form or provably exact condition for cooperation to be favoured, such as ρ_C > ρ_D or the stationary share of cooperators. It must hold beyond weak selection and outside limits where linking and strategy updating run on separated time scales. The book names no specific graph dynamics, so this is a family of problems rather than one theorem.",
 "status": "OPEN",
 "status_evidence": [
  {"claim": "The book's statement of the open problem.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0138/p-0139.png", "quote": "下动态图上的合作演化研究，尚无严格解析结果，是目前的一个公开难题", "read_primary": true},
  {"claim": "The statement cites ref [11], a paper on a social-learning tournament that does not address strong selection on dynamic graphs. It is probably mis-cited.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0138/p-0140.png", "quote": "Rendell L, et al. Why copy others? Insights from the social learning strategies tournament.", "read_primary": true},
  {"claim": "Before publication, exact results existed only when linking and strategy updating run on separated time scales. When linking is fast, the dynamics reduce to a well-mixed game with rescaled payoffs; the paper uses a Fermi rule with any β, including β→∞.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2430061", "quote": "This means that strategy evolution proceeds as in a well-mixed population of A and B players (complete graph) engaged in a game specified by the payoff-matrix", "read_primary": true},
  {"claim": "The authors' own 2010 treatment of strong selection on dynamic networks (Wu, Zhou, Fu, Luo, Wang, Traulsen) uses a replicator-equation approximation, not a rigorous result.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2894855", "quote": "the replicator equation is only an approximation of the strategy evolution when the population size is sufficiently large", "read_primary": true},
  {"claim": "After publication, the general theory of strategy evolution on dynamic networks covers weak selection only (2023).", "url": "https://arxiv.org/pdf/2301.11982", "quote": "Our main mathematical result (Equation 3) shows when cooperation will evolve on dynamic networks, under weak selection.", "read_primary": true},
  {"claim": "The same holds for temporal networks in 2024 work co-authored by two of the book's authors (Fu and Wang).", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11286197", "quote": "Throughout this paper, we study the limiting case of weak selection", "read_primary": true},
  {"claim": "Even on static graphs, the question of whether some networks provably promote cooperation under medium or strong selection was open until 2025.", "url": "https://research-explorer.ista.ac.at/download/20857/20860/2025_PNAS_Svoboda.pdf", "quote": "Despite the wide applicability of the model, the only known networks that provably promote cooperation do so only for weak selection.", "read_primary": true},
  {"claim": "Exact strong-selection results exist for special static graphs such as cycles (2017).", "url": "https://arxiv.org/abs/1701.06615", "quote": "We establish exact analytical results for fixation times under strong selection", "read_primary": true},
  {"claim": "On static graphs, some of the basic invasion and fixation questions are computationally hard (2015).", "url": "https://pubmed.ncbi.nlm.nih.gov/26644569", "quote": "We therefore show that some fundamental questions in this area cannot be answered by simple equations (assuming that P is not equal to NP).", "read_primary": false}
 ],
 "tractability": "LOW",
 "tractability_reason": "There is no standard model, so a faithful reading is a programme of theory, not one statement. Strong-selection questions are hard even on static graphs: some are computationally hard, the 'promoter' question stayed open until 2025, and exact results exist only for special graphs such as cycles. Dynamic-network theory up to 2024 covers weak selection only, and pre-2011 exact results cover only the fast-linking limit. Solving one toy model in a day would not settle the book's question.",
 "recommendation": "TOO-HARD"
},
{
 "title_zh": "操控量子世界",
 "authors": "谈自忠、张靖、吴热冰（清华大学信息科学与技术国家实验室）",
 "book_pages": [111, 116],
 "pdf_pages": [132, 137],
 "question_zh": "在这一领域还有很多基本问题有待解决，如关于一般的非线性量子反馈控制理论的描述、关于系统可观性的一般性讨论、观测器的设计、量子反馈控制的鲁棒性等。……退相干抑制问题复杂而丰富多样，目前还远没有得到解决",
 "question_en": "Many basic problems remain: a general theory of nonlinear quantum feedback control, a general treatment of observability, observer design, and robustness of quantum feedback. … Suppressing decoherence is far from solved.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The article's only precise controllability question is controllability of finite-dimensional closed systems, which it says is equivalent to the universality of quantum gates. The article itself says this is basically solved.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0132/p-0134.png", "quote": "经过近十年的研究，这个问题已经基本得到了解决", "read_primary": true},
  {"claim": "This matches the literature: Lie-algebraic controllability criteria for Hamiltonian quantum systems had been collected in an overview by 2003.", "url": "https://arxiv.org/abs/quant-ph/0302121", "quote": "An overview and synthesis of results and criteria for open-loop controllability of Hamiltonian quantum systems obtained using Lie group and Lie algebra techniques is presented.", "read_primary": true},
  {"claim": "The problems the article leaves open are described only qualitatively.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0132/p-0134.png", "quote": "在这一领域还有很多基本问题有待解决", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "This is a research programme: feedback theory, observability, observers, robustness and decoherence. The article poses no precise open controllability or reachability question. Its one precise question, controllability of finite-dimensional closed systems, it declares basically solved. Controllability of open and infinite-dimensional systems is mentioned only qualitatively.",
 "recommendation": "VAGUE"
},
{
 "title_zh": "机器学习之模型选择",
 "authors": "徐雷（香港中文大学计算机科学与工程系）",
 "book_pages": [106, 110],
 "pdf_pages": [127, 131],
 "question_zh": "虽然经过近半世纪的努力，可以认为模型选择仍是未决难题。已有各种方法中，没有哪一个被公认是最好的。……此难题实质上涉及从哲学层面看什么是最好的学习理论。",
 "question_en": "Despite nearly half a century of effort, model selection is still unresolved, and no existing method is accepted as best. At bottom it is a philosophical question of which learning theory is best.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The book says model selection is unresolved and no method is accepted as best.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0127/p-0130.png", "quote": "可以认为模型选择仍是未决难题。已有各种方法中，没有哪一个被公认是最好的", "read_primary": true},
  {"claim": "A theorem published before the book (Yang, Biometrika 2005) gives one formal reason no single criterion is best: a criterion cannot be both consistent and minimax-rate optimal.", "url": "https://dr.lib.iastate.edu/entities/publication/f9c20f30-0573-4e2f-a316-7264f05e7c65", "quote": "for any model selection criterion to be consistent, it must behave suboptimally for estimating the regression function in terms of minimax rate of covergence", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "A philosophical question with no test for being answered; the author argues that his own BYY harmony learning theory is the way out. Narrow formal versions already had answers before publication, such as Yang (2005).",
 "recommendation": "VAGUE"
},
{
 "title_zh": "几何计算的健壮性问题",
 "authors": "高曙明（浙江大学CAD&CG国家重点实验室）、齐建昌（东南大学机械工程学院）",
 "book_pages": [609, 611],
 "pdf_pages": [630, 632],
 "question_zh": "解决几何计算健壮性问题的难点在于如何在计算机浮点计算精度下准确判别在实数计算下所存在的相互关联的几何关系。……但距离完全解决几何计算健壮这一难题还十分遥远。",
 "question_en": "The difficulty is to decide correctly, at floating-point precision, the interrelated geometric relations that hold under exact real arithmetic. Tolerance, interval and exact-arithmetic methods are all far from fully solving robustness; exchanging models between modelling systems is a further open issue.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The book says robustness is far from fully solved; this is an engineering programme.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0630/p-0631.png", "quote": "但距离完全解决几何计算健壮这一难题还十分遥远", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "An engineering programme: criteria for setting tolerances, efficiency of interval methods, validity after model exchange. 'Fully solving robustness' has no test for being answered.",
 "recommendation": "VAGUE"
},
{
 "title_zh": "高维数据降维",
 "authors": "乔立山（南京航空航天大学信息科学与技术学院；聊城大学数学科学学院）、陈松灿、张道强（南京航空航天大学信息科学与技术学院）",
 "book_pages": [593, 595],
 "pdf_pages": [614, 616],
 "question_zh": "但降维问题至今仍未从本质上得以解决。……①内在维数如何估计？②学习模型的参数如何选择？③学习算法的性能如何评价？……难道“维数灾难”本质上无法克服？",
 "question_en": "Dimensionality reduction remains fundamentally unsolved. How should intrinsic dimension be estimated, how should model parameters (neighbourhood size, kernel width) be chosen, and how should performance be evaluated? Is the curse of dimensionality impossible to overcome in principle?",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The book says dimensionality reduction remains fundamentally unsolved; its sub-questions are about methods.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0614/p-0615.png", "quote": "但降维问题至今仍未从本质上得以解决", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "A research programme about methods; the questions of how to estimate, choose and evaluate have no formal criterion for success.",
 "recommendation": "VAGUE"
},
{
 "title_zh": "约束求解与优化",
 "authors": "季晓慧（中国地质大学(北京)信息工程学院）、刘田（北京大学信息科学技术学院）、王怀民（国防科学技术大学计算机学院）",
 "book_pages": [521, 523],
 "pdf_pages": [542, 544],
 "question_zh": "一个重要的研究方向是寻找约束问题的可多项式时间求解的子类，并在此基础上得到约束问题的复杂度分类定理，如二分定理。……在理论上，约束问题可满足性相变与难解性之间的确切关联仍然是一个重要的科学问题。",
 "question_en": "An important direction is to find subclasses of constraint problems solvable in polynomial time and, from them, theorems classifying their complexity, such as a dichotomy theorem (via universal algebra or structural decomposition). … In theory, the exact link between the satisfiability phase transition and hardness remains an important scientific question.",
 "precision": "FORMALIZABLE",
 "formal_reading": "The faithful reading of '复杂度分类定理，如二分定理' is the Feder–Vardi CSP Dichotomy Conjecture. Take any finite constraint language Γ: finitely many relations on a finite domain. CSP(Γ) asks whether an instance built only from relations in Γ has a solution. The conjecture says CSP(Γ) is either in P or NP-complete. In the algebraic form stated by Zhuk, CSP(Γ) is tractable if Γ has a weak near-unanimity polymorphism (in the usual statement, after reducing Γ to its core or idempotent form) and NP-complete otherwise. The article's other items (phase transition versus hardness, choosing and combining algorithms, distributed CSP) cannot be stated as single theorems.",
 "status": "SOLVED-AFTER-PUBLICATION",
 "status_evidence": [
  {"claim": "The book names a complexity classification, such as a dichotomy theorem, as a research direction.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0542/p-0543.png", "quote": "并在此基础上得到约束问题的复杂度分类定理，如二分定理", "read_primary": true},
  {"claim": "Bulatov proved the Feder–Vardi dichotomy (FOCS 2017).", "url": "https://www2.cs.sfu.ca/~abulatov/papers/focs17.pdf", "quote": "For any finite constraint language Γ over a finite set the problem CSP(Γ) is either solvable in polynomial time or is NP-complete.", "read_primary": true},
  {"claim": "Bulatov's arXiv version, March 2017.", "url": "https://arxiv.org/abs/1703.03021", "quote": "In this paper we prove the Dichotomy Conjecture on the complexity of nonuniform constraint satisfaction problems posed by Feder and Vardi.", "read_primary": true},
  {"claim": "Zhuk proved it independently (arXiv, April 2017).", "url": "https://arxiv.org/abs/1704.01914", "quote": "In the paper we present an algorithm that solves Constraint Satisfaction Problem in polynomial time for constraint languages having a weak near unanimity polymorphism, which proves the remaining part of the conjecture.", "read_primary": true},
  {"claim": "Zhuk's proof is published in J. ACM vol. 67, issue 5, pp. 1–78 (online 2020-08-26), per Crossref.", "url": "https://api.crossref.org/works/10.1145/3402029", "quote": "A Proof of the CSP Dichotomy Conjecture", "read_primary": true},
  {"claim": "Caveat: the infinite-domain version (the Bodirsky–Pinsker conjecture) is still called a conjecture in 2026. It falls outside the book's finite-domain framing.", "url": "https://arxiv.org/abs/2602.02302", "quote": "The Bodirsky-Pinsker conjecture asserts a P vs. NP-complete dichotomy for the computational complexity of Constraint Satisfaction Problems (CSPs) of first-order reducts of finitely bounded homogeneous structures.", "read_primary": true},
  {"claim": "For the phase-transition versus hardness item there is only an extraordinary preprint claim by Ke Xu, co-author of the random CSP model RB; it is unverified here and not treated as settled [INFERENCE].", "url": "https://arxiv.org/abs/2302.09512", "quote": "we prove that such examples cannot be solved without exhaustive search, which is stronger than P $\\neq$ NP", "read_primary": true}
 ],
 "tractability": "HIGH",
 "tractability_reason": "Already settled by two independent peer-reviewed proofs, so certifying the status means citing them. Re-proving it is not a one-day task (Zhuk's J. ACM paper runs to 78 pages) and is not needed. The phase-transition versus hardness item is VAGUE.",
 "recommendation": "SOLVED-ELSEWHERE"
},
{
 "title_zh": "网络的建模方法及建模",
 "authors": "高志鹏、邱雪松、孟洛明（北京邮电大学网络与交换技术国家重点实验室）",
 "book_pages": [431, 433],
 "pdf_pages": [452, 454],
 "question_zh": "提出适用于融合和泛在网络的、支持对网络行为感知/预测/控制的网络建模方法，并基于该方法，构建一个普适的、基于精准数学表达的、富语义的网络模型，成为当前和未来一段时期内网络研究领域的重大课题。",
 "question_en": "Develop a method for modelling converged, ubiquitous networks that supports sensing, predicting and controlling network behaviour, and use it to build a universal, mathematically precise and semantically rich network model.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The book poses an open-ended modelling programme.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0452/p-0452.png", "quote": "构建一个普适的、基于精准数学表达的、富语义的网络模型", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "A modelling programme: unified models for heterogeneous networks, ontology-based models covering many properties, and behaviour models borrowed from other disciplines. There is no test for being answered.",
 "recommendation": "VAGUE"
},
{
 "title_zh": "通信网络的免疫自愈问题",
 "authors": "隆克平、彭云峰（电子科技大学光互联网及移动信息网络研究中心）",
 "book_pages": [436, 438],
 "pdf_pages": [457, 459],
 "question_zh": "缺乏对免疫系统的免疫可计算机理、通信网的可免疫机理的交叉深入探究，至今仍未突破局部单点问题方面的简单模拟和概念化探讨的瓶颈。",
 "question_en": "There has been little cross-disciplinary study of how immune mechanisms can be made computable or how communication networks could be made 'immunizable'. Work has not progressed beyond simple simulations and conceptual discussion of local, single-point problems: ant-colony routing, chemotaxis-inspired routing agents, and intrusion detection by negative selection or danger theory.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The book says the field is stuck at simple simulations; this is an engineering programme.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0457/p-0457.png", "quote": "至今仍未突破局部单点问题方面的简单模拟和概念化探讨的瓶颈", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "A bio-inspired engineering programme. Its sub-issues, such as convergence speed of ant-colony optimization and false-alarm rates of negative selection, are empirical.",
 "recommendation": "VAGUE"
},
{
 "title_zh": "复杂知识表示与推理",
 "authors": "刘大有、欧阳丹彤、杨博、王生生、欧阳继红（吉林大学计算机科学与技术学院）、王国胤（重庆邮电大学计算机科学与技术学院）、漆桂林（东南大学计算机科学与工程学院）",
 "book_pages": [590, 592],
 "pdf_pages": [611, 613],
 "question_zh": "如何针对特定逻辑特征给出信念修正的合理公设集，仍是一个理论难题。……但如何在复杂系统中针对不同类型问题选择合适的知识表示与推理方法并进行深度结合是一个理论难题。",
 "question_en": "How to give a reasonable set of belief-revision postulates suited to the features of a specific logic remains a theoretical problem. So does how, in complex systems, to choose suitable knowledge representations and reasoning methods for different kinds of problem and combine them deeply. The article also raises choice of knowledge granularity and the trade-off between expressiveness and efficiency in spatio-temporal reasoning and planning.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The article's most specific item: belief-revision postulates for specific logics.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0611/p-0612.png", "quote": "如何针对特定逻辑特征给出信念修正的合理公设集，仍是一个理论难题", "read_primary": true},
  {"claim": "Answers exist logic by logic. For Horn logic, AGM revision fails and is repaired with an extra postulate and a representation theorem (IJCAI 2011, the same year as the book).", "url": "https://www.ijcai.org/Abstract/11/146", "quote": "It proves to be the case that classical (AGM) belief revision doesn't immediately generalise to the Horn case.", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "'Reasonable postulates' has no test for being answered. Answers exist for individual logics, but the programme as a whole has no single statement that could be settled.",
 "recommendation": "VAGUE"
},
{
 "title_zh": "模式特征的抽取和表达",
 "authors": "丁晓青（清华大学电子工程系）",
 "book_pages": [600, 602],
 "pdf_pages": [621, 623],
 "question_zh": "如何从复杂的、极大数据量的模式样本观测中获取和表达模式分类和识别的模式特征，特别是抽取和表达那些对模式分类密切相关的鉴别特征成为模式识别成功的关键和核心问题。",
 "question_en": "How to extract and represent, from complex and very large pattern observations, the features needed for classification, especially discriminative features, is the key problem of pattern recognition. The article mentions heteroscedastic, non-Gaussian, nonlinear and nearest-neighbour discriminant analysis.",
 "precision": "VAGUE",
 "formal_reading": null,
 "status": "UNKNOWN",
 "status_evidence": [
  {"claim": "The article ends with an open-ended statement that research will continue; it asks no precise question.", "url": "scratch/ai4s-information-science-more-20261014/screen/B-computation-statistics/0621/p-0622.png", "quote": "模式特征抽取和表达的探索还将持续进行", "read_primary": true}
 ],
 "tractability": "LOW",
 "tractability_reason": "A survey of feature-extraction methods. Its only formula, a bound on the Bayes error by H(E|F)/2, is an established result cited from a 1974 paper, not an open question.",
 "recommendation": "VAGUE"
}
]
```

**Ranked shortlist** (no TARGET in this group):

1. **约束求解与优化 (SOLVED-ELSEWHERE)** — The dichotomy theorem the article names as a goal is the Feder–Vardi conjecture. Bulatov and Zhuk proved it independently in 2017 (FOCS 2017; Zhuk in J. ACM 67(5), 2020). This is the article's only precise item and it is cleanly settled. The infinite-domain version is still a conjecture, but it lies outside the book's framing.
2. **因果推断 (SOLVED-ELSEWHERE, sub-question only)** — For binary treatment, surrogate and endpoint, Yin–Liu–Geng–Luo (Scand. J. Stat. 2020; the article's author is a co-author) give criteria that are checkable from data and proven optimal for ruling out the surrogate paradox. This builds on Ju–Geng 2010 (the book's ref [7]) and VanderWeele 2013. Two caveats: the article's umbrella question is a research programme, and continuous or survival endpoints remain open.

On the two articles named in the focus:
- **合作演化之谜** has no precise statement about fixation probabilities or a cooperation condition on graphs. Its strong-selection, dynamic-graph problem can be formalized, but is too hard; theory on dynamic networks still covers only weak selection.
- **操控量子世界** poses no open controllability or reachability question. Its one precise question, controllability of finite-dimensional closed systems, is declared solved by the article itself.
