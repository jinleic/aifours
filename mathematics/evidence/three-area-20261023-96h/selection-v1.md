# Mathematics selection v1: repeated-pole phase-type representations

Before-creation clock observed: **2026-10-23T12:47:50-07:00**. Owner: `MathResearch96h`. All writes are confined to this lane. This freeze follows source reading and exploratory symbolic reasoning, not a blind preregistration: the exploratory reasoning already suggested the trace/companion route below. No scientific program, parameter loop, solver, compilation, Lean run or model CLI has been executed. Scientific execution has no GO.

## 1. Book question and scope hierarchy

The source is *10000 Selected Problems in Sciences: Mathematics*, Science Press 2009, ISBN 978-7-03-024267-9, article **Minimal Representation of Phase-Type Distribution**, Qiming He and Hanqin Zhang, printed pp.544–545 / PDF pp.560–561. The page offset is +16. The source PDF identity recorded by `books/README.md` is `3c69cf2c023a37fdb9e2c7e8ccbe9b163e067884f257003c9df64ac62d092901`; this lane has not rehashed the whole PDF. Direct `pdftotext -layout -f 560 -l 561` extraction is preserved in `book-phase-type-pp544-545.txt`.

The **full book question** is: given a continuous-time PH distribution, find an equivalent PH representation with the fewest transient states. The book explicitly calls this a decades-old open problem (p.544, final paragraph). No claim below solves this general problem.

A representation of order N means a real N-by-N Hurwitz Metzler matrix T with T1 <= 0 and a nonnegative row alpha with alpha1 = 1, giving the Laplace transform alpha(sI-T)^(-1)(-T1). The absorbing state is not counted in N.

For a > c > 0 and b > 0 put d = a-c, beta = b/d, and

    H_{r,q}(s) = c^r (a^2+b^2)^q /
                 [(s+c)^r ((s+a)^2+b^2)^q],  r,q positive integers.

This is initially a normalized rational function, NOT automatically a PH distribution for every parameter. Its reduced denominator has degree r+2q; therefore every PH representation, if one exists, has at least r+2q states.

**Broad primary research target:** determine the minimum PH order, or non-PH status, of H_{1,2} for every a > c > 0, b > 0. Repeated nonreal poles make this distinct from the old three-simple-pole problem.

**First complete bounded obligation (P1):** for every r,q >= 1 and a > c > 0, b > 0, prove or refute that H_{r,q} admits a PH representation of algebraic degree r+2q exactly when

    beta <= 1 / sqrt(2 ceil(q/r)+1).

**Next obligation within the same primary target (P2):** settle the exact minimum order of H_{1,2} on 0 < beta <= 1/sqrt(2), with endpoints included. The proposed candidate is order 5 on beta <= 1/sqrt(5), and order 6 on 1/sqrt(5) < beta <= 1/sqrt(2). A complete proof must provide actual PH parameters or an exact formula constructing them, not just an admissible spectrum. For beta > 1/sqrt(2), neither non-PH status nor a six-state impossibility is presumed.

P1/P2 are explicit subproblems of the book question, not a claim that their formulas are presently literature-certified open.

## 2. Three exact candidates compared

| Candidate | Exact statement and provenance | Baseline and missing ingredient | Decision |
|---|---|---|---|
| **Fresh primary: repeated-pole PH** | P1/P2 above; book pp.544–545. The immediately preceding round worked on Olson/Shor, and the earlier PH result treated only H_{1,1}. | Liu–Yao–Zhang, arXiv:2409.12673v2 (15 Feb 2025), gives a general nonconvex iff criterion for algebraic-degree representations, not an explicit order formula for this family. Laffey–Smigoc's spectral theorem, precisely stated in Ellard–Smigoc 2017 Theorem1.2, supplies nonnegative companion realizations under first/second moment conditions. Missing: a transfer-preserving PH construction, handling pole multiplicity and Frobenius blocks, and a matched novelty comparison. | **Select.** All-parameter inequalities and compact exact constructions can change a checkable mathematical claim without scientific execution. The likely value is a specialist corollary, not an established major result. |
| **Kac–Moody reserve** | For every r,s >= 1, A(r,s)=[[2,-1,-1],[-1,2,-1],[-r,-s,2]], prove J_alpha=tau_alpha for every positive multidegree with alpha_3 <= 4. Book Yucai Su, pp.226–227 / PDF242–243, full question: Serre relations define the maximal Cartan-disjoint quotient for every GCM over C. | Dossier presently gives alpha_3 <= 3 for all r,s; alpha_3 <= 4 only for r,s >= 4 by an exact checker whose last HMZ review was unfinished. Uniform rank-three height8 coverage is incomplete. Missing: all small-row parameter regimes and a written or fully coverage-bound proof, without treating old checker output as a general theorem. Marquis 2023 §6.2 explicitly retains the nonsymmetrizable Gabber–Kac question. | **Reserve only.** Genuine headroom, but a larger representation-theory/checker dependency surface than PH. No second simultaneous target. |
| **Olson lower-band continuation** | Every word of length4p-1 over D_(2p), p an odd prime >= 7, with exactly R=p+1 ROTATIONS has an original-index-order identity product on2p selected terms. Full book question: the analogous assertion for every group of order n and every length2n-1 word; Sun Zhiwei, p.142 / PDF158. | Read the closed v17 report WITH its mandatory operative erratum and the Oct22 EVENING continuation. The insertion family sigma_0^(2p-1)sigma_1...sigma_(p-1) plus arbitrary p+1 rotations is already covered by an unpromoted candidate. Full R=p+1 remains unproved. Missing: solve the actual signed mixed-selection equation for every remaining word, not relaxed parameters or a one-short word. | **Do not select now.** A materially new structural ingredient is not yet identified. No duplicate credit for the covered insertion family. |

Shor's n=1320m condition with at least two distinct odd prime factors of m is excluded from selection: the Oct22 continuation identifies it as a restatement of the old conditional restriction. Sun7 remains internally written-accepted; Sun8 is not inferred. No completed design/code case is being reproduced.

## 3. Dated primary reading and trust boundaries

1. **Book pp.544–545:** actual local PDF extraction, read in full; definitions, question, authors and references are visible. This is source provenance, not a 2026 openness certificate.
2. **Liu–Yao–Zhang, arXiv:2409.12673v2, 15 Feb2025:** [official HTML](https://arxiv.org/html/2409.12673v2), abstract, Introduction and start of §2 read. The Introduction says the current state is far from solving the minimal PH representation problem. The paper's result is an iff nonconvex feasibility criterion at the algebraic degree; convergence of its numerical method is not a global infeasibility oracle. No numerical algorithm from it is a proof premise here.
3. **Commault–Mocanu 2003**, *International Journal of Control*76:566–580, DOI10.1080/0020717031000114986: [accessible primary PDF](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf). Definitions, positive-realization/PH bridge, spectral Theorem6, Theorem14 and Conjecture1 sections opened. The old internal H_{1,1} off-boundary result is preserved as baseline, not reannounced. PH order counts transient states.
4. **Ellard–Smigoc, arXiv:1702.02650v1, 8 Feb2017:** [official primary HTML](https://arxiv.org/html/1702.02650v1), Theorems1.1/1.2/2.1 and Lemma2.2 read. Theorem1.2 restates Laffey–Smigoc2006: a self-conjugate list (rho,lambda_2,...,lambda_n), rho >= 0, Re(lambda_i) <= 0 for i>=2, is nonnegative-realizable iff s_1>=0 and s_1^2<=n s_2; a realization C+alpha I exists with C nonnegative companion, trace C=0, alpha>=0. This is a named classical theorem-level import unless its proof is separately reconstructed. A realizable spectrum alone is NOT a PH realization of the desired rational function.
5. **Pulungan2011:** [primary survey](https://pulungan.staff.ugm.ac.id/pubs/P-SEAMS-11.pdf), full reader text opened. General minimal order remains open there; Theorem2.2 gives the algebraic-degree lower bound. Its dated survey is not a current full classification.
6. **Marquis2023**, [arXiv:2309.02508v1 §6.2](https://arxiv.org/html/2309.02508v1#S6.SS2), actual open-question paragraph read. It relates characteristic-zero nonsymmetrizable GK-simplicity to extending Gabber–Kac; it does not settle the reserve. Existing Kac–Moody dossier boundaries were read directly.
7. **Olson:** exact transcribed book statement read directly. Current ordered-dihedral baseline is the mandatory closed v17+erratum and Oct22 evening report. A fresh primary proof of Dimitrov's p-group theorem has not been read in this lane and is not an operative premise. This source-access limitation is disclosed rather than treating an unordered modern EGZ paper as the ordered theorem.

**Dated status on 2026-10-23:** full book PH problem has explicit primary open-status evidence through the 2025 source; no later resolution was located in this bounded screen. The exact repeated-pole P1/P2 formulas are **UNCERTIFIED-OPEN / NOVELTY_UNCLEAR**, not certified new questions. A source miss does not establish openness or priority. The 2017 spectral theorem makes a classical-corollary outcome a serious possibility.

## 4. Local and remote openai/math screen

Read local `/Users/jinleic/jinleic-workspace/math/CONTENTS.md` (722 manuscripts /372 families) and the accessible remote main [CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) (719 manuscripts /372 families). Targeted searches of the local inventory and `lean/docs/`, and the remote inventory, for `phase-type`, `phase type`, `PH distribution`, `nonnegative realization`, `positive realization`, `Kac–Moody`, `Kac-Moody`, `Gabber`, `Olson`, and `disjoint coset` found no matching claim. An earlier broader `coset` search hit unrelated abelian-variety text and is not overlap. Remote/local differing counts are recorded, not silently equated.

Scope: title/abstract inventory and local Lean-scope descriptions, not every manuscript/proof body or a full Git history audit. No OAI result is adopted as a premise. No Lean run occurred. These negative screens are not a novelty certificate.

## 5. Attack, verification and redirect conditions

P1 first lemma: a PH representation with exactly r+2q states has no hidden eigenvalues; irreducible Metzler diagonal blocks each require one real Perron eigenvalue, hence exactly r blocks. Distribute q repeated complex pairs across them, then apply trace(M^2) >= (trace M)^2/dimension on each shifted block. For sufficiency, construct each single-real-pole block by a nonnegative companion matrix and explicitly normalize a positive realization into PH form; cascade r blocks without losing the target transfer function.

P2: use an explicit six-state companion with an extra real pole and a nonnegative linear numerator that cancels it. Every cancellation, diagonal scaling, initial probability, exit rate and endpoint must be proved exactly. No numerical fit substitutes for positivity.

Independent route for parent: reconstruct the lower bound from SCC/Perron theory and the five-/six-state upper bound directly from polynomial coefficients and resolvent cofactors. Check a below-threshold, equality and above-threshold symbolic case. For general P1, verify the exact hypotheses of the 2017 import or reconstruct its required companion-coefficient consequence. Written parent/in-harness checking is not Lean acceptance. Any actual computation/replay requires a separate named GO with exact command/input pins/resources/controls; none is requested yet.

Redirect if: (i) a primary source already states the exact repeated-pole criterion/order formula, (ii) the transfer-preserving companion bridge fails, or (iii) after a complete bounded P1/P2 packet the only remaining primary obligation needs a materially new representation. Preserve that result, label its novelty honestly, and seek parent redirection before activating the Kac–Moody reserve. No quota/access gate is a mathematical exhaustion result.
