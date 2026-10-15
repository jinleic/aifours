# Group A screening: 15 network and signal articles, plus 非均匀采样问题

None of the 16 articles is a fresh TARGET. Two are already settled by prior work:

- **非均匀采样问题:** settled in 1981, before the book. One caveat from my check: the shortcut test in Tucker et al. (2022), their eq. (11) and Cor. 5, is wrong as stated for an arbitrary lattice basis. Two worked counterexamples are in the JSON.
- **无线网络调度:** settled in 2013, but only for the weaker notion of stability. The book asks for the stronger one.

The other 14 are either loose research directions (VAGUE) or well-known open problems (TOO-HARD).

## 1. Per-article JSON

```json
[
{
"title_zh": "网络中的信息流最大化",
"authors": "廖建新、王敬宇（北京邮电大学网络与交换技术国家重点实验室）",
"book_pages": [423, 424],
"pdf_pages": [444, 445],
"question_zh": "但在大规模复杂的网络环境下，如何达到或接近信息流容量的理论上限依然是有待解决且颇具挑战性的疑难问题",
"question_en": "In large-scale complex networks, how to reach or approach the theoretical upper limit of information-flow capacity is still an open and difficult problem.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [
 {"claim": "The article does not ask for multi-source capacity or solvability. In the strongest formal reading (general multi-source network coding), Li proves that deciding exact solvability is undecidable. Solvability here means: some alphabet size q≥2 exists, every message is uniform on q symbols, every edge carries at most q values, and every sink decodes with zero error. Theorem 22 covers arbitrary q; Theorem 23 covers q=c^m for a fixed c. Undecidability extends to multiple-unicast and index coding.", "url": "https://arxiv.org/pdf/2205.11461", "quote": "We resolve three long-standing open problems, namely the (algorithmic) decidability of network coding, the decidability of conditional information inequalities, and the decidability of conditional independence implication among random variables, by showing that these problems are undecidable.", "read_primary": true},
 {"claim": "Li settles exact solvability only. Searching the full text for 'asymptotic', 'capacity' and 'rate region' turned up nothing on the asymptotic capacity region. Whether network-coding capacity is computable is therefore not settled by this paper.", "url": "https://arxiv.org/pdf/2205.11461", "quote": "It was uncertain if network coding is even decidable, that is, if there exists an algorithm that can determine whether a network is solvable (i.e., admits a coding scheme satisfying the decoding constraints)", "read_primary": true},
 {"claim": "Corollary 30: the minimum alphabet size needed to solve a network has no computable upper bound.", "url": "https://arxiv.org/pdf/2205.11461", "quote": "As a result, the minimum alphabet size needed to solve a network can be uncomputably large, i.e., not upper-bounded by any computable function (Corollary 30).", "read_primary": true},
 {"claim": "Published version: IEEE Trans. Inf. Theory 69(6):3493–3510, June 2023, DOI 10.1109/TIT.2023.3247570.", "url": "https://api.crossref.org/works?query.bibliographic=Undecidability+of+Network+Coding+Conditional+Information+Inequalities+Conditional+Independence+Implication&rows=2&select=DOI,title,container-title,issued,volume,issue,page", "quote": "Undecidability of Network Coding, Conditional Information Inequalities, and Conditional Independence Implication", "read_primary": true},
 {"claim": "The article's own technical case, single-source multicast, was settled before publication. The book itself cites Li–Yeung–Cai 2003. A polynomial-time code construction appeared in IEEE TIT 51(6):1973–1982 (2005). I checked only the metadata.", "url": "https://api.crossref.org/works?query.bibliographic=Polynomial+Time+Algorithms+for+Multicast+Network+Code+Construction+Jaggi&rows=1&select=DOI,title,container-title,issued,volume,issue,page,abstract", "quote": "Polynomial Time Algorithms for Multicast Network Code Construction", "read_primary": false}
],
"tractability": "LOW",
"tractability_reason": "This is a research-program sentence, not a checkable claim. Single-source multicast was solved before 2011. In the general multi-source case, exact solvability is undecidable (Li 2023), and the asymptotic capacity has no known computable characterization.",
"recommendation": "VAGUE"
},
{
"title_zh": "互联网的可测性问题",
"authors": "谢高岗、闵应骅（中国科学院计算技术研究所）；孟洛明（北京邮电大学网络与交换技术国家重点实验室）",
"book_pages": [428, 430],
"pdf_pages": [449, 451],
"question_zh": "网络可测性问题包括两个基本问题：网络是否可以全面测量和网络是否可以深入测量。",
"question_en": "Internet measurability has two basic questions: can the network be measured comprehensively (full spatial coverage), and can it be measured in depth (multi-dimensional, multi-granularity metrics)?",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [
 {"claim": "The article never asks the network-tomography question. One sub-reading of 'comprehensive measurement' is: can internal link metrics be identified from end-to-end path measurements? Ma–He–Leung–Swami–Towsley settle exactly this reading under four assumptions: link metrics are additive; they are constant; probing paths are cycle-free paths between monitors; and the routing is controllable.", "url": "https://research.ibm.com/publications/identifiability-of-link-metrics-based-on-end-to-end-path-measurements", "quote": "it is generally impossible to identify all the link metrics by using two monitors", "read_primary": true},
 {"claim": "The paper gives necessary and sufficient topological conditions: for the interior links with 2 monitors, and for all links with 3 or more monitors. The conditions can be tested efficiently. Venues: ACM IMC 2013, pp. 391–404, and IEEE/ACM ToN 22(4):1351–1368 (2014), DOI 10.1109/TNET.2014.2328668.", "url": "https://research.ibm.com/publications/identifiability-of-link-metrics-based-on-end-to-end-path-measurements", "quote": "these conditions naturally extend to a necessary and sufficient condition for identifying all the link metrics using three or more monitors", "read_primary": true},
 {"claim": "The exact conditions are in the authors' proofs report. With 2 monitors: G−l is 2-edge-connected for every interior link l, and G+m1m2 is 3-vertex-connected. With κ≥3 monitors the conditions are stated on an extended graph G_ex, where they become 3-edge-connectivity and 3-vertex-connectivity (Props. II.6–II.7). Algorithm MMP gives the optimal monitor placement. Not covered: fixed routing, non-additive or time-varying metrics, and the article's 'in-depth' half of the question.", "url": "https://arxiv.org/pdf/2012.12190", "quote": "For an arbitrary connected network G, Algorithm MMP generates the optimal monitor placement", "read_primary": true}
],
"tractability": "LOW",
"tractability_reason": "The article treats measurability as something to define statistically, dynamically and locally, and frames it as an infrastructure research program. The one crisp sub-reading (additive-metric identifiability under controllable cycle-free probing) was settled in 2013–2014.",
"recommendation": "VAGUE"
},
{
"title_zh": "网络的基本性质",
"authors": "邱雪松、高志鹏、孟洛明（北京邮电大学网络与交换技术国家重点实验室）",
"book_pages": [434, 435],
"pdf_pages": [455, 456],
"question_zh": "例如，如何为Internet等复杂网络构造可用于指导网络设计和建设的模型；如何全面认识网络运行的动态变化规律；如何认识网络在故障状态下的行为和网络在遭受安全攻击时的行为；如何描述网络的可管理性及其管控模型等。",
"question_en": "How to build models of Internet-like complex networks that can guide network design and construction; understand their dynamics; understand behaviour under faults and attacks; and describe manageability.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "A modelling and behaviour research program with no checkable statement.",
"recommendation": "VAGUE"
},
{
"title_zh": "复杂网络中关键节点集合的确定",
"authors": "苏森、李勇辉、阎冬（北京邮电大学网络技术研究院）",
"book_pages": [439, 441],
"pdf_pages": [460, 462],
"question_zh": "综上所述，在多种约束条件下，以有限的时间在大规模网络中找到一个最优的关键节点集合还是一个需要继续深入研究的问题，效率和准确性是必须着重关注的指标，两者之间需要取得合理平衡。",
"question_en": "Under multiple constraints, finding an optimal key-node set in large networks in limited time still needs research; efficiency and accuracy must be balanced.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [
 {"claim": "The natural formal reading is k-node Maximum Betweenness Centrality (MBC): choose k nodes to maximize group betweenness. Its worst-case complexity was settled before publication. It is NP-hard, and greedy achieves a (1−1/e) approximation. The book itself already reports the NP-completeness via Puzis.", "url": "https://arxiv.org/abs/1008.3503", "quote": "Recently, Dolev et al. (2009) showed that MBC is NP-hard and gave a $(1-1/e)$-approximation using a greedy approach.", "read_primary": true},
 {"claim": "MBC is APX-complete, so it has no PTAS unless P=NP. It is exactly solvable on trees. arXiv posting: August 2010.", "url": "https://arxiv.org/abs/1008.3503", "quote": "Moreover, we prove that MBC is APX-complete and provide an exact polynomial-time algorithm for MBC on tree graphs.", "read_primary": true}
],
"tractability": "LOW",
"tractability_reason": "The exact-optimum reading is negatively settled (NP-hard, APX-complete). What remains is designing heuristics that trade efficiency against accuracy under unspecified constraints.",
"recommendation": "VAGUE"
},
{
"title_zh": "无线网络调度策略的稳定性及分布式实现",
"authors": "关新平、杨博（上海交通大学自动化系）",
"book_pages": [731, 734],
"pdf_pages": [752, 755],
"question_zh": "目前，结果大多集中在假设式(1)中的μ(链路物理带宽，受信道状态影响)为常值。在时变链路速率情况下的基于队列的随机接入算法及其稳定性还未被人们解决。",
"question_en": "Existing results mostly assume the link rate μ in Eq. (1) is constant. Queue-based random-access algorithms, and their stability, under time-varying link rates remain unsolved.",
"precision": "FORMALIZABLE",
"formal_reading": "Model. Links share an interference graph G; feasible schedules σ(t) are the independent sets I(G). Queues follow Q_i(t+1)=max{Q_i(t)−μ_i(t)·1[σ_i(t)=1],0}+A_i(t). Arrivals are ergodic with mean X_i. The rates μ(t) come from an ergodic finite-state channel process with stationary law π, and link i sees its own μ_i(t). Capacity region: Λ={x≥0 : x ≤ Σ_c π_c Σ_{ρ∈I(G)} α_{ρ,c}(c∘ρ)} for some distributions α_{·,c} on I(G). Question. Construct a CSMA-type random-access policy in which each link's access or backoff depends only on its own queue (and own channel state), and prove stability for every X in the interior of Λ. Definition 1 of the book asks for strong stability: limsup_{t→∞}(1/t)Σ_{τ<t}Σ_i E[Q_i(τ)]<∞. The CSMA literature usually proves rate stability (Q(t)/t→0), which is weaker.",
"status": "SOLVED-AFTER-PUBLICATION",
"status_evidence": [
 {"claim": "Yun–Shin–Yi prove throughput optimality for channel-aware CSMA. The ratio of holding to backoff parameters is exponential in the current local capacity. Assumptions: finite-state Markov channels, an arbitrary interference graph, and idealized continuous-time, collision-free carrier sensing.", "url": "https://arxiv.org/pdf/1306.2009", "quote": "They are the first CSMA algorithms in the literature which are proved to be throughput optimal under time-varying channels.", "read_primary": true},
 {"claim": "Their 'throughput optimal' means rate-stable for every λ in the interior of Λ. It is not the book's strong stability.", "url": "https://arxiv.org/pdf/1306.2009", "quote": "In particular, when α = 1, it is called throughput optimal.", "read_primary": true},
 {"claim": "The queue-based variant (Thm 4.2) uses weights max{w(Q_i), √w(Q_max)} with w = log log. It needs the global Q_max or a distributed estimate of it, and its proof is only sketched on top of earlier work by Shah–Shin. The rate-based variant (Thm 4.1) uses only local history.", "url": "https://arxiv.org/pdf/1306.2009", "quote": "We omit further necessary details.", "read_primary": true},
 {"claim": "Published at ACM MobiHoc 2013, DOI 10.1145/2491288.2491303.", "url": "https://api.crossref.org/works?query.bibliographic=CSMA+over+time-varying+channels+optimality+uniqueness+limited+backoff+rate&rows=3&select=DOI,title,container-title,issued,author", "quote": "Proceedings of the fourteenth ACM international symposium on Mobile ad hoc networking and computing", "read_primary": true},
 {"claim": "Jiang–Walrand adaptive CSMA (2008–2010) does not settle the book's question. It assumes fixed unit link capacities and leaves time-varying channels to other work.", "url": "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/Archive/EECS-2009-124.pdf", "quote": "Without loss of generality, assume that each link k has a capacity of 1.", "read_primary": true},
 {"claim": "The 2013 paper confirms that throughput-optimal CSMA before it, including Jiang–Walrand and Rajagopalan–Shah–Shin, assumed static channels.", "url": "https://arxiv.org/pdf/1306.2009", "quote": "However, the recent CSMA algorithms crucially rely on the assumption of static channel conditions.", "read_primary": true}
],
"tractability": "MEDIUM",
"tractability_reason": "The core question is answered in the rate-stable sense, so documenting it is quick. Not located: the book's strong-stability version, and a fully local version that needs no Q_max. Upgrading log-log-weight CSMA from rate stability to finite mean queues is not obviously a one-day proof [INFERENCE].",
"recommendation": "SOLVED-ELSEWHERE"
},
{
"title_zh": "高性能迭代解码问题",
"authors": "邓科（西安交通大学电子与信息工程学院）",
"book_pages": [464, 466],
"pdf_pages": [485, 487],
"question_zh": "现在，人们依然不能定量地描述迭代解码算法的性能，甚至不能给出收敛速度和误码率的公式。……使用Tanner图只能定性地描述解码的过程，定量的分析结果至今尚未出现",
"question_en": "The performance of iterative decoding still cannot be described quantitatively, not even by formulas for convergence speed or bit-error rate; Tanner graphs give only a qualitative description.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [
 {"claim": "Rigorous asymptotic analysis of iterative decoding already existed before the book. Threshold saturation, for example, was proved for spatially coupled LDPC codes on the binary erasure channel (BEC). Closed-form finite-length bit-error-rate and convergence formulas for general turbo and LDPC codes do not exist, so the book's demand is a research program.", "url": "https://arxiv.org/abs/1001.1826", "quote": "Although we prove the connection between the MAP and the BP threshold only for a very specific ensemble and only for the binary erasure channel, empirically a threshold saturation phenomenon occurs for a wide class of ensembles and channels.", "read_primary": true}
],
"tractability": "LOW",
"tractability_reason": "No specific quantity or ensemble is fixed. The book's claim that no quantitative analysis exists is partly outdated (density evolution, EXIT charts).",
"recommendation": "VAGUE"
},
{
"title_zh": "无线通信系统中信道容量的定义和度量",
"authors": "邓科、穆鹏程（西安交通大学电子与信息工程学院）",
"book_pages": [455, 457],
"pdf_pages": [476, 478],
"question_zh": "总之，实际通信系统的信道容量是一个很重要的物理量和指标，然而，已有的科学理论却很难描述和度量它，这使得这一问题自然地成为了一个科学难题。",
"question_en": "The channel capacity of real wireless systems is a key quantity, but existing theory can hardly describe or measure it.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "A definitional and modelling program (multipath, interference, 'spatial spectrum') with no precise target.",
"recommendation": "VAGUE"
},
{
"title_zh": "网络信息论",
"authors": "尹长川、罗涛、乐光新（北京邮电大学信息与通信工程学院）",
"book_pages": [417, 419],
"pdf_pages": [438, 440],
"question_zh": "在由多个通信节点所组成的通信网络中，人们需要回答的一个基本问题是：在任意可能进行通信的成对节点之间能同时实现的最大信息传输速率是多少。",
"question_en": "What maximal rates can be achieved simultaneously between all communicating node pairs, i.e. what is a network's Shannon capacity region? The book names the 3-node relay channel and the 2-user (4-node) interference channel as still unsolved.",
"precision": "FORMALIZABLE",
"formal_reading": "Take a discrete memoryless or Gaussian n-node network p(y_1..y_n|x_1..x_n), with an independent message W_ij for every ordered pair (n(n−1) messages). Nodes encode causally from their past outputs. The task is a computable characterization of the capacity region: the closure of rate tuples (R_ij) achievable with error probability tending to 0. Minimal named cases: the capacity of the 3-node Gaussian relay channel, and the capacity region of the 2-user Gaussian interference channel.",
"status": "OPEN",
"status_evidence": [
 {"claim": "Relay-channel capacity is still open as of September 2026. The paper exhibits a counterexample to a claimed solution posted two days earlier.", "url": "https://arxiv.org/pdf/2609.18727", "quote": "The characterization of the capacity for general relay channels has been one of the open problems in network information theory.", "read_primary": true},
 {"claim": "The refuted claim (Ponniah, arXiv:2609.15709, 14 Sep 2026) says three relaying schemes achieve capacity.", "url": "https://arxiv.org/abs/2609.15709", "quote": "The capacity of the relay channel is characterized by three schemes: decode-forward, coordinated compress-forward, and uncoordinated compress-forward.", "read_primary": true},
 {"claim": "The counterexample: on a binary relay channel, an achievable rate exceeds the claimed capacity formula.", "url": "https://arxiv.org/pdf/2609.18727", "quote": "An achievable scheme exceeds the proposed capacity characterization, thereby disproving the characterization of the capacity for general relay channels.", "read_primary": true},
 {"claim": "For the Gaussian relay channel, only upper bounds are known.", "url": "https://arxiv.org/abs/1606.01374", "quote": "The cut-set bound developed by Cover and El Gamal in 1979 has since remained the best known upper bound on the capacity of the Gaussian relay channel.", "read_primary": true},
 {"claim": "The 2-user Gaussian interference channel was known only to within 1 bit before the book (2007). The exact region is not given.", "url": "https://arxiv.org/abs/cs/0702045", "quote": "The capacity of the two-user Gaussian interference channel has been open for thirty years.", "read_primary": true},
 {"claim": "Nuance: Li 2021 writes a 'single-letter' characterization as a first-order formula. It is not a computable rate formula, so it does not answer the book's 'what is the rate'.", "url": "https://arxiv.org/abs/2108.07324", "quote": "We also construct a single-letter characterization of the capacity region for a general class of multiuser coding settings (including broadcast channel, interference channel and relay channel), using a first-order formula.", "read_primary": true}
],
"tractability": "LOW",
"tractability_reason": "These are famous problems open for decades (relay channel since the 1970s, exact interference-channel region). The only recent activity is a contested 2026 claim and its refutation.",
"recommendation": "TOO-HARD"
},
{
"title_zh": "Shannon信息论中的语义鲁棒性难题",
"authors": "刘健、隆克平（电子科技大学光互联网及移动信息网络研究中心）",
"book_pages": [425, 427],
"pdf_pages": [446, 448],
"question_zh": "因此，如何建立与Shannon信息论相统一的可靠语义信息表达是本科学难题最重要的方面……如何将基于语义的鲁棒性引入到Shannon信息论中是当前研究的科学难题。",
"question_en": "How to build a reliable representation of semantic information that is unified with Shannon theory, and how to bring semantic robustness into Shannon information theory.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "No mathematical object is fixed; this is a conceptual program.",
"recommendation": "VAGUE"
},
{
"title_zh": "光纤通信频谱效率的极限",
"authors": "喻松、顾畹仪（北京邮电大学信息光子学与光通信研究院）",
"book_pages": [420, 422],
"pdf_pages": [441, 443],
"question_zh": "因此，如何建立光纤通信系统完整的Shannon理论模型，预测光纤通信系统的信息容量极限，探求达到此极限的条件，进而指导光纤通信系统进一步提高频谱效率是亟须解决的关键科学理论问题。",
"question_en": "Build a complete Shannon-theoretic model of fiber links, predict their information-capacity limit, and find the conditions that achieve it.",
"precision": "FORMALIZABLE",
"formal_reading": "The question is the capacity per unit bandwidth (bit/s/Hz) of the channel defined by the stochastic nonlinear Schrödinger equation (NLSE), or the Manakov equation for dual polarization. The channel has Kerr nonlinearity, chromatic dispersion and distributed amplified-spontaneous-emission noise over length L, under an average input-power constraint P. It may be posed for a single user over the full band or for one WDM user among others. Sub-questions: how capacity scales as P→∞ (is it bounded or unbounded, and what is its pre-log), and which inputs and receivers achieve it.",
"status": "OPEN",
"status_evidence": [
 {"claim": "The capacity of the nonlinear fiber channel is still unknown; only lower bounds keep improving.", "url": "https://arxiv.org/abs/2112.03796", "quote": "As a result, only little progress has been made so far, while the optimal shaping distribution and the ultimate channel capacity remain unknown.", "read_primary": true},
 {"claim": "Known upper bound: log(1+SNR) for a split-step cascade model of the stochastic NLSE. Defining 'bandwidth' remains subtle.", "url": "https://arxiv.org/abs/1503.07652", "quote": "It is shown that the spectral efficiency of the cascade is at most log(1+SNR), where SNR is the receiver signal-to-noise ratio.", "read_primary": true}
],
"tractability": "LOW",
"tractability_reason": "A flagship open problem in optical information theory; even the model-level question of how bandwidth is defined is unsettled.",
"recommendation": "TOO-HARD"
},
{
"title_zh": "欠冗余传感器网络的故障诊断",
"authors": "陈伟民、胡顺仁、税爱社、章鹏（重庆大学光电工程学院）",
"book_pages": [923, 925],
"pdf_pages": [944, 946],
"question_zh": "因此，解决欠冗余传感器网络的故障诊断，其关键就是从M_S个传感器的输出中再找到n=k+j个包含待测参量的关系式，从而构成M′_S=M_S+n≫M的软冗余条件",
"question_en": "Diagnosing faults in an under-redundant sensor network (M_S=M−j sensors for M parameters) requires mining n=k+j extra measurement relations from the sensor data to create soft redundancy.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "An engineering methodology program (relation mining, thresholds, classifiers); the linear-equation analogy is illustrative only.",
"recommendation": "VAGUE"
},
{
"title_zh": "多层媒质的电磁并矢Green函数",
"authors": "洪伟、周后型、宋喆、胡俊、郑开来（东南大学毫米波国家重点实验室）",
"book_pages": [336, 337],
"pdf_pages": [357, 358],
"question_zh": "但具有通用性的能够同时精确计算水平分布和垂直分布的Green函数快速算法还很不成熟，有待学术界继续深入研究。",
"question_en": "General-purpose fast algorithms that accurately compute layered-media dyadic Green's functions in both horizontal and vertical distributions are still immature.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "Numerical-methods maturity (pole location, complex images) with no crisp success criterion.",
"recommendation": "VAGUE"
},
{
"title_zh": "空谱的描述与定义",
"authors": "穆鹏程、殷勤业（西安交通大学电子与信息工程学院）",
"book_pages": [449, 451],
"pdf_pages": [470, 472],
"question_zh": "要想合理有效地利用空谱，首先应该解决空谱的准确描述和定义问题，而实际上，该问题到目前为止尚未得到很好解决。",
"question_en": "To use the 'spatial spectrum' effectively, one must first describe and define it precisely (position, propagation direction, polarization); this is unresolved.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "It asks for a definition, not a theorem.",
"recommendation": "VAGUE"
},
{
"title_zh": "非均匀样本条件下的协方差矩阵估计问题",
"authors": "廖桂生、李明（西安电子科技大学雷达信号处理国家重点实验室）",
"book_pages": [472, 473],
"pdf_pages": [493, 494],
"question_zh": "是否存在一个线性变换将不同空时分布的所有距离单元数据一致变换为具有相同空时分布的数据样本？／是否可以直接通过非均匀样本实现协方差矩阵的准确估计？",
"question_en": "(1) Is there a linear transform that uniformly maps the data of all range cells, whose space-time distributions differ, to samples with the same space-time distribution? (2) Can the covariance matrix be estimated accurately directly from non-homogeneous samples?",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "[INFERENCE] The questions do not fix what the transform may depend on, and every explicit choice gives a trivial answer. (a) If each cell covariance R_k is known, T_k=R_0^{1/2}R_k^{-1/2} works, but R_k is the very thing to be estimated. (b) A single T with T R_k T^H constant over many generic R_k forces T=0. (c) Q2 is impossible without structural assumptions, because each distinct covariance is seen once. Under structured models it reduces to known estimators. No faithful, nontrivial formalization was found.",
"recommendation": "VAGUE"
},
{
"title_zh": "微波成像的稀疏表示问题",
"authors": "廖桂生、王伟伟（西安电子科技大学雷达信号处理国家重点实验室）",
"book_pages": [470, 471],
"pdf_pages": [491, 492],
"question_zh": "因此，建立一套完整有效的理论体系，以指导寻求不同复杂观测区域的稀疏化表示，是一个具有重要研究意义的科学难题。",
"question_en": "Build a complete theory that guides finding sparse representations of diverse, complex observed scenes for microwave imaging.",
"precision": "VAGUE",
"formal_reading": null,
"status": "UNKNOWN",
"status_evidence": [],
"tractability": "LOW",
"tractability_reason": "A dictionary-design program with no precise target.",
"recommendation": "VAGUE"
},
{
"title_zh": "非均匀采样问题",
"authors": "穆鹏程、殷勤业（西安交通大学电子与信息工程学院）",
"book_pages": [446, 448],
"pdf_pages": [467, 469],
"question_zh": "因此，当想要使用任意阵列进行空域非均匀采样时，该阵列需要满足什么样的条件才能保证不出现空谱混叠仍然是一个难题。",
"question_en": "When an arbitrary array (nonuniform, or conformal) samples space nonuniformly, what conditions guarantee no spatial-spectrum aliasing, i.e. no grating lobes?",
"precision": "FORMALIZABLE",
"formal_reading": "This uses the book's co-array model: isotropic elements with weights, narrowband far-field sources. Sensors sit at p_1..p_L ∈ R^d in half-wavelength units, with steering vector a(ω)=[e^{iπ p_k^T ω}]_k. ω ranges over ℬ: [−1,1] for d=1, the closed unit disk for d=2, the unit sphere for d=3, or a prescribed subset. The array is alias-free, meaning no full-height grating lobe under any nonzero weighting, iff no pair ω1≠ω2 in ℬ has a(ω1)=c·a(ω2). Equivalently, let P=π[(p_k−p_1)^T]_{k≥2} and Λ={ω: Pω∈2πZ^{L−1}}; then no nonzero lattice point of Λ lies in ℬ−ℬ. For the full ℬ_d this says λ1(Λ)>2. Time-domain counterpart: characterize the sets Λ⊂R whose samples stably determine every f in the Paley–Wiener space PW_S of functions band-limited to S. Not covered: direction-dependent element gains g_k(ω), as in conformal arrays.",
"status": "SOLVED-BEFORE-PUBLICATION",
"status_evidence": [
 {"claim": "Godara–Cantoni (JASA 70(2):467–475, 1981) established geometric conditions for unique steering vectors for general arrays. Per Tucker et al., their Thm. 6 is a necessary and sufficient test over the full set of directions of arrival (DoAs).", "url": "https://doi.org/10.1121/1.386790", "quote": "Conditions on array geometry for uniqueness and linear independence of steering vectors are established for linear, planar, and general arrays.", "read_primary": true},
 {"claim": "Tucker et al. confirm that the Godara–Cantoni Thm. 6 test is necessary and sufficient; it is a finite combinatorial search over integer wrapping vectors.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9757818/", "quote": "Godara and Cantoni [1, Thm. 6] provide an alternative necessary and sufficient test for alias-free on the full set of DoAs", "read_primary": true},
 {"claim": "Tucker, Zhao, Ahmad, Potter (IEEE SPL 29:2457–2461, 2022) give a necessary and sufficient condition for arbitrary isotropic arrays and arbitrary DoA subsets (Prop. 3). For the full DoA set it is Cor. 4. I checked both directly against the definition.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9757818/", "quote": "An array is alias-free if and only if the smallest norm of a non-zero lattice point is greater than 2.", "read_primary": true},
 {"claim": "Tucker et al. explicitly assume isotropic elements, so direction-dependent element patterns are not covered. Their pointer for arbitrary per-sensor gains is Kastinen & Kero 2020, a probabilistic meteor-radar study, not a criterion.", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9757818/", "quote": "The signal model in (2) adopted the traditional assumption of isotropic sensor elements; ambiguity analysis with arbitrary complex-valued gain functions per sensor was considered in [39].", "read_primary": true},
 {"claim": "Eq. (11) is asserted for any lattice basis. My hand-checked counterexamples (see tractability_reason) show it is false unless the basis contains a shortest lattice vector [INFERENCE].", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9757818/", "quote": "For any basis V, let C ∈ ℤ^{d×(2^d−1)} with each column given by a d-digit binary representation from 1 to 2^d − 1.", "read_primary": true},
 {"claim": "Time-domain part: Landau 1967 (Acta Math. 117:37–52, DOI 10.1007/BF02395039) proved the necessary density D⁻(Λ) ≥ |S|/2π for stable sampling of PW_S. I read the restatement by Nitzan–Olevskii 2012; Landau's scan had no extractable text.", "url": "https://www.numdam.org/item/10.1016/j.crma.2012.05.003.pdf", "quote": "The necessity part in these results was extended by H. Landau [4] to the general case.", "read_primary": false},
 {"claim": "Ortega-Cerdà–Seip, 'Fourier frames' (Ann. of Math. 155(3):789–806, 2002, DOI 10.2307/3062132, confirmed via Crossref), completely characterize the sampling sequences for Paley–Wiener space with an interval spectrum. The characterization goes through de Branges spaces. This predates the book.", "url": "https://arxiv.org/abs/math/0005092", "quote": "We solve the problem of Duffin and Schaeffer (1952) of characterizing those sequences of real frequencies which generate Fourier frames. Equivalently, we characterize the sampling sequences for the Paley-Wiener space.", "read_primary": true}
],
"tractability": "HIGH",
"tractability_reason": "[INFERENCE, hand-checked arithmetic] Prop. 3 and Cor. 4 are correct, but eq. (11) and Cor. 5 need a reduced basis. (i) Sensors at (0,0), (2/3,−58/9), (0,20/3) give Λ=VZ² with basis v1=(3,0), v2=(2.9,0.3). Eq. (11) returns min(|v2|,|v1|,|v1+v2|)≈2.92>2, i.e. 'alias-free'. Yet v2−v1=(−0.1,0.3)∈Λ, so ω=(−0.05,0.15) and (0.05,−0.15) alias. (ii) The basis (3,0),(30,0.3) has all parallelepiped vertex distances >2, so Cor. 5 says 'alias-free'. Yet (0,0.3)∈Λ. The fix is to reduce the basis first (Gauss in 2-D, Minkowski in 3-D) and test λ1>2. Conformal extension: with real positive gains, alias requires ω1−ω2∈Λ plus proportional gain vectors, so isotropic alias-freeness is sufficient. Elements with zero gain in some directions need the test on each illuminated subarray via Prop. 3. With complex gains the check becomes per instance.",
"recommendation": "SOLVED-ELSEWHERE"
}
]
```

## 2. Ranked shortlist

1. **非均匀采样问题 (PDF 467–469) — SOLVED-ELSEWHERE.** Under the book's isotropic co-array model, Godara–Cantoni (1981) already gave a necessary and sufficient no-grating-lobe test. Tucker et al. (2022) restate it as "the shortest lattice vector has norm > 2" and extend it to any subset of arrival directions. Their eq. (11) and Cor. 5 shortcut needs a reduced lattice basis. Conformal arrays with direction-dependent element gains are not covered.
2. **无线网络调度策略的稳定性及分布式实现 (PDF 752–755) — SOLVED-ELSEWHERE, rate-stable sense only.** Yun–Shin–Yi (arXiv:1306.2009, MobiHoc 2013) prove queue-based and rate-based channel-aware CSMA throughput-optimal under Markov time-varying channels. Jiang–Walrand alone does not settle it, because it assumes fixed unit link capacities. Not covered: the book's strong stability, and a queue-based version that needs no global Q_max. The 2013 queue-based proof is only sketched.
