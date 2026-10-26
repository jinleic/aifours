# Two replacement proposals for info-1

Observed clock: **2026-10-23T14:43:32-0700** (`/bin/date`, copied verbatim). This is a **selection proposal, not an activated target or scientific result**. Parent binding remains required; the October 27 deadline and all no-execution/no-contact boundaries are unchanged.

## 1. Operative retirement and collision check

P24, P33, and the printed-sign correction are **PRIOR-CLAIM** in Alper Ferudun's October 3, 2026 unrefereed preprint, DOI [10.5281/zenodo.23127063](https://doi.org/10.5281/zenodo.23127063). The actual canonical paper, metadata and relevant statements were read. The independent written P24 construction and reviews are preserved, not mathematically refuted, not novel by default, and not a parent-certified finite witness. No verifier version has been run; no execution GO is sought for that retired target.

Detailed source disposition: [source-comparison-Ferudun-20261003-v1.md](source-comparison-Ferudun-20261003-v1.md), SHA-256 `0c7d9379bc44bfe9f56df0e26c1937c2fcc305b812d5b34b1ac2796064589512`.

Both proposals below differ from every other active problem in [the authoritative eighteen-slot roster](../../../../../institute/runs/three-area-2026-10-23-96h/eighteen-problem-roster-v1.md). The actual roster was read; its observed SHA-256 is `f79c594ad016c06321beb07993707ef4a21a9892bea54193280bb96c083cbefc`. In particular neither is robust-SPR7, stochastic-H-infinity preview, recursive MDS18, guessing-number R-minus, or balanced NL242. P34 has the same broad SOF classification as retired P24 but a **different expressly unclaimed dimension pair**; the privacy proposal is a genuinely different book article and problem.

## 2. Proposal A: P34, ordinary twelve-state generic SOF stabilization

### Exact statement and desired delta

Let

- `A in R^(12 x 12)`, `B in R^(12 x 4)`, `C in R^(3 x 12)`;
- `S = {(A,B,C): exists K in R^(4 x 3), A+BKC is Hurwitz}`.

**Is S dense in the full ordinary Euclidean space of triples?** A negative answer must exhibit a **nonempty ordinary open family** of triples outside S; one exceptional plant, inaccessible state, missing non-Hurwitz spectrum, gain restriction, or generic failure of arbitrary pole assignment is insufficient. An affirmative answer must prove this density with unrestricted real constant K. Inputs/outputs are explicitly bound here because two source conventions interchange their names.

A successful negative construction would settle the `(m,p)=(3,4)`, `n=12` case (three outputs, four inputs) of the current classification question. It is not another example in the already claimed `(2,p)` or `(4,p)`-with-even-p families: swapping `(3,4)` gives `(4,3)`, whose other port count is odd. The Grassmannian degree is even, `d(3,4)=462`; the known odd-degree sufficient criterion therefore does not settle it.

### Book provenance, baseline and current open evidence

Book: *10000 Selected Problems in Sciences: Information Science*, Science Press, 2011, ISBN 978-7-03-031911-1; Chen Benmei, *Disturbance Decoupling Problem with Static Output Feedback*, printed **631–632**, PDF **652–653**. The stable variant requires `A+BKC1` Hurwitz. Setting disturbance and controlled-output channels to zero makes decoupling automatic and retains SOF stabilization. **The article does not literally state P34**: P34 is this exact generic-dimensional subquestion of its stable synthesis obligation. Earlier extracted text and actually opened page are immutable at `../../sources/book-sof-631-632.txt` and `../../sources/book-sof-0652.png`.

Primary/current status:

1. [Ferudun, canonical October 3 preprint](https://eulersolve.org/papers/amr-036-0044/paper.pdf?v=9c811e158489), **Table 1, Problem 6.1, and final scope/priority paragraph**: explicitly leaves all smaller-port-three cases except `(3,3)` open; hence `(3,4)` is expressly outside Theorems 1.1–1.3. The actual theorem and open-case text, not the abstract alone, were read. Its declared PDF hash is `9c811e1584896c3869998a96386488d3c69bbb2b4df3f022dff091f9ef4a8394` (publisher-declared, not a new local rehash).
2. [Eremenko maintained primary note](https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf), October 3, 2026 displayed version, and [Byrnes–Anderson manuscript in NASA CR-166441](https://ntrs.nasa.gov/api/citations/19830010078/downloads/19830010078.pdf), printed 113–115: original critical-dimension question and precise nondegenerate-plant criterion. Already read in this lane; source route and imported theorem boundaries remain recorded in the immutable selection-v2.
3. [Public AIM problem 319](https://raw.githubusercontent.com/MColbrook/AIM/main/problems/319-generic-static-output-feedback-stabilization.md), actually read, last checked September 17, 2026: full classification open and critical equality distinguished from individual-plant decision/hardness. This dated inventory is **superseded by Ferudun on his listed pairs**, not used to reopen those pairs.

### First residual action and exact missing ingredient

One possible new certificate target is a real **3-by-7 polynomial row matrix of total minor degree twelve**, preferably balanced row degrees `(4,4,4)`, whose determinant against **every** constant real rank-four complement cannot be `z^12` after permitted calibration. This is a new Grassmannian/three-row geometry, not rotating P24's fixed complex structure, retuning its Hermitian kernel, or appending a hidden mode. A genuine attack must first decide whether a candidate real-fibre representation can exclude every real decomposable four-vector, including all chart boundaries. The exact missing ingredient is that global real-fibre exclusion (or a new theorem proving it impossible for the chosen representation).

Acceptance for a negative result additionally requires degree/leading-coefficient binding, ordinary controllable/observable twelve-state realization, exclusion of **all** Hurwitz closed-loop polynomials, and an ordinary open-neighborhood argument. If a current primary claim covers `(3,4)`, or the proposed representation only embeds a retired port pair with an invariant hidden mode, record the closure/obstruction and return to the alternative before new science. This is not authorization to start the representation now.

## 3. Proposal B: planar mixed-geometry optimal additive differential privacy

### Exact statement and desired delta

For every epsilon > 0 let `M(epsilon)` consist of **all Borel probability measures mu on R^2** satisfying

`mu(E) <= exp(epsilon) mu(E+h)`

for every Borel E and every real h with `|h1|+|h2| <= 1`. The mechanism is query-output-independent additive noise, with the **full diamond** as its prescribed sensitivity set. Define

`V(epsilon) = inf_{mu in M(epsilon)} integral (x1^2+x2^2) dmu(x)`.

Let `b=exp(-epsilon)`. The traditional correlated diamond staircase has density `f_gamma(x)`, for gamma in `[0,1]`, proportional to

- `b^k` when `||x||_1 in [k,k+gamma)`;
- `b^(k+1)` when `||x||_1 in [k+gamma,k+1)`;

for integers k >= 0, with normalization included. Endpoint parameters are interpreted by the same normalized almost-everywhere density.

**Does `V(epsilon) = min_{gamma in [0,1]} E_{f_gamma}[X1^2+X2^2]` hold for every epsilon > 0?** A resolution may prove this for all epsilon or refute it by one explicit admissible measure at one exact positive epsilon with cost strictly below **the optimized entire staircase family**, not merely below Laplace noise or one sampled gamma. The broader exact V remains open if only the conjecture is refuted. No assumption of independent coordinates, radiality, smoothness or density is added to the feasible set.

### Book provenance and primary open question

Book: same Information Science volume; Yang Xiaochun and Yu Ge, **Privacy Protection for Sensitive Data**, printed **583–586**, PDF **604–607**. Source-only extraction was performed and the actual p.583 image opened. The article explicitly poses the security/information-loss/usability tradeoff and, at printed p.585, asks how to measure released-data usefulness and balance it against protection. **It does not literally formulate differential privacy or this exact planar optimization**; this is a precise modern subquestion of the printed tradeoff, not a full-book solution claim.

Local source: [book-privacy-583-586.txt](source-excerpts/book-privacy-583-586.txt), SHA-256 `014581a2312b2e68d6bab236a8be8f4f84e77f1f78d7fdf13baac1257f0806d0`; [actually opened first page](source-excerpts/book-privacy-0604.png). Article authors are visible at the end of the extraction. The source volume routed hash remains `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db` (not rehashed here).

[Quan Geng and Pramod Viswanath, *The Optimal Mechanism in Differential Privacy: Multidimensional Setting*, arXiv:1312.0655v1](https://arxiv.org/html/1312.0655), Section III's final paragraph, **literally conjectures optimality in d=2 for `L(x)=||x||_2^2` under its l1-sensitivity model**, and says the layer-averaging lemma does not work because this cost is not a function of the l1 norm alone. This exact paragraph, model and preceding theorem were actually read.

### Required comparison with later resolutions

- [Geng–Kairouz–Oh–Viswanath 2015 journal paper](https://pramodv.ece.illinois.edu/pubs/GKOV.pdf), DOI `10.1109/JSTSP.2015.2425831`: the actual printed p.1179 image was opened. Equation (9) uses l1 sensitivity; equation (10) and **Theorem 1 use the l1 loss itself**, not Euclidean squared loss. Its broad abstract is not taken as a proof of the mixed-cost conjecture. Local PDF hash: `f07bc5861e5dc8c48efbd0d5a3685339497e044db571c829aaeb82b9d7de4d7d`.
- [Kulesza–Suresh–Wang, AISTATS 2025](https://proceedings.mlr.press/v258/kulesza25a.html), actual paper Sections 1–3 and Definitions 3/5/Theorems 1/2: proves the optimal mechanism when sensitivity and theoretical loss use **the same K norm**. Other error metrics are discussed empirically; no mixed-cost optimality theorem was found in the read theorem interface. Its [public implementation README](https://github.com/google-research/google-research/tree/master/general_staircase_mechanism) was actually read; it claims implementation/experiments for that paper, not a new theorem for the present mixed model.
- [Melbourne–Diaz–Asoodeh, January 21, 2026, arXiv:2601.14597](https://arxiv.org/html/2601.14597): actual additive-model constraints and **Assumption 1** read. It requires `Phi(x)=varphi(||x||)` for the **same norm** as the sensitivity geometry. The target cost fails this: `(1,0)` and `(1/2,1/2)` have equal l1 norm but costs `1` and `1/2`. Selecting the Euclidean norm instead changes the sensitivity set and is not this problem. Thus the arbitrary-dimension, same-norm conjecture is already settled and **is not proposed**. This hypothesis mismatch is not by itself proof that no other source settles the mixed problem.
- [Amorino–Gloter, arXiv:2603.27572](https://arxiv.org/abs/2603.27572), actual abstract, concerns local-DP Fisher information, not this additive global-DP MSE optimization. [Hillebrand et al., 2026 TPDP preprint](https://tpdp.journalprivacyconfidentiality.org/2026/pdfs/hillebrand.pdf), actual abstract, introduction and model, concerns integer-valued discrete-Laplace postprocessing and unbiased estimation; that discrete adjacency is not the present full continuous diamond.

Current screening verdict: **a literal historical primary conjecture with a precise uncovered interface in the later read theorems; current openness not globally certified**. The parent should not call it novel, accepted, or settled on this source screen alone.

### First residual action, acceptance and redirect

If bound, the first written action is to reconstruct the complete optimized staircase cost and examine **non-homothetic noise-density superlevel sets**, with full translation-DP control rather than a sampled finite grid. A potential new ingredient is to let successive level sets expand by the sensitivity diamond while the initial set is not itself a diamond. The missing ingredient is a rigorous admissibility-and-cost comparison against **all** gamma, or an exact dual inequality excluding every such improvement. This is not another same-norm staircase reformulation or small extra enumeration.

A counterexample must specify its entire probability law including all tails, normalization and every-shift privacy proof, and give an exact strict cost bound against the global staircase-family minimum. A positive answer must give an all-law lower bound and attainment. Formal verification and novelty would remain separate gates. If a later primary theorem covers the exact full-diamond/squared-Euclidean interface, preserve that source and redirect to P34 only after parent binding; do not silently substitute Euclidean sensitivity or discrete adjacency.

## 4. Mandatory cross-corpus screen and access limits

- **EulerSolve:** the actual full [papers listing](https://eulersolve.org/papers/) was searched for privacy, staircase, stabilization and pole placement. The relevant SOF claim is AMR-036-0044, directly read as above. No privacy/staircase match was returned. This is a listing-level screen, not a proof that no unindexed theorem exists.
- **openai/math:** both the retained current-remote catalog `../../sources/openai-math-CONTENTS-20261023.md` (SHA-256 `cc7c0b8a1cdedd845a777e77cf682657308503daf8346c1349e06e9259d063c2`) and local `/Users/jinleic/jinleic-workspace/math/CONTENTS.md` (SHA-256 `c492802b53fb4c4161e45fc678bb67bd526add72ca2635493a367ff7fb860bf9`) were searched for privacy, staircase, generic stabilizability, static output feedback and pole placement. Only unrelated representation-theoretic/lattice staircase matches appeared. This is **catalog screening**, not a read of every paper or a formal non-overlap certificate.
- **Public repositories/claims:** the current AIM primary problem route and Google Research implementation route above were opened. Targeted current and GitHub-indexed queries for each exact interface found no additional matched resolution; search summaries were not promoted to theorem evidence. In particular summaries that blur same-norm and mixed-norm privacy were rejected in favor of the actual Assumption 1.
- Direct Zenodo access to Ferudun returned an access barrier, but its canonical EulerSolve paper and DataCite DOI registry supplied the actual statement/date. No external contact or credential change was attempted. No source/test/verification code was run.

## 5. Recommendation to parent

**Prefer Proposal B if the book-to-modern-scoped-question link is accepted**: it supplies a literal precise primary conjecture and a materially different geometric ingredient, and does not extend the retired P24 method or occupy a sibling's problem. Keep P34 as the source-supported alternative. Either choice needs a new parent binding and immutable exact selection before substantive attack. No new target is activated by this document.
