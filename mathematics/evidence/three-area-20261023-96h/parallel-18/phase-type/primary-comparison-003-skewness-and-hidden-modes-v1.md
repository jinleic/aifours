# Primary comparison 003: classical skewness and hidden-mode boundaries

Clock actually observed before creation: **2026-10-23T15:07:41-07:00**. MathResearch96h, math-1. Source reading and written algebra only; no mathematical execution, model CLI or publication.

## 1. An exact classical identification, not merely a resemblance

The symmetric-eigenvalue part of B6's Lemma M is exactly the classical sharp finite-sample skewness bound. It should not be represented as a new inequality.

For real eigenvalues y_1,...,y_n of a symmetric trace-zero matrix S, write tau_j=sum y_i^j. When tau_2>0, the uncorrected moment skewness of this finite sample is

    g1=(tau_3/n)/(tau_2/n)^(3/2)
       =sqrt(n) tau_3/tau_2^(3/2).

The sharp bound |g1|<=(n-2)/sqrt(n-1) is therefore equivalent, with exactly the same constant, to

    tau_3>=-(n-2)/sqrt(n(n-1)) tau_2^(3/2).

At n=6 this is 4/sqrt(30), precisely B6's load-bearing constant. The one-outlier/equal-other-values equality case is also exactly the Lagrange-multiplier extremum reconstructed in B6 and its peer review. No scientific identity is being inferred from numerical similarity.

### Sources actually reached

- Nicholas J. Cox, *Speaking Stata: The limits of sample skewness and kurtosis*, Stata Journal10(3),2010,pp.482–495. Actual PDF pp.483–485, Section2.1, explicitly states the sharp |g1| bound, defines its convention, attributes it to Wilkins1944 and independently Kirby1974, and describes the equality samples. Read those pages and its actual reference pages493–495: <https://ageconsearch.umn.edu/record/159037/files/sjart_st0204.pdf>.
- J. Ernest Wilkins, *A Note on Skewness and Kurtosis*, Annals of Mathematical Statistics15(3),1944,pp.333–335, DOI <https://doi.org/10.1214/aoms/1177731243>. Crossref's actual DOI metadata and full-text link were read: <https://api.crossref.org/works/10.1214/aoms/1177731243>. The bibliographic abstract reproduced by Mendeley states the same bound: <https://www.mendeley.com/catalogue/d9c79d6a-190b-3fe7-a405-1317b92e4b2d/>.
- The original primary full PDF endpoint supplied by Crossref, <https://projecteuclid.org/download/pdf_1/euclid.aoms/1177731243>, returned an Incapsula interstitial, not the proof. Consequently this record does **not** claim to have authenticated Wilkins's original proof. Cox is an accessible later review, not the1944 original. No login, access change or bypass was attempted.

B6 remains self-contained at this step: its own written derivation and separate reconstruction prove the exact inequality, so the inaccessible original does not become an additional mathematical import. The newly identified provenance only narrows novelty attribution.

## 2. Geometric symmetrization is also an established matrix operation

The matrix B6 calls S, with S_ij=sqrt(X_ij X_ji) off diagonal and S_ii=X_ii, becomes the standard Hadamard geometric symmetrization after adding a scalar tI to make X+tI nonnegative:

    S+tI=(X+tI)^(1/2) circ ((X+tI)^T)^(1/2),

where powers are entrywise. This does not assume X itself entrywise nonnegative.

A primary paper actually read is Katarina Bogdanovic and Aljosa Peperko, arXiv2202.02325v1,2022, *Inequalities and equalities on the joint and generalized spectral and essential spectral radius of the Hadamard geometric mean of bounded sets of positive kernel operators*: <https://arxiv.org/pdf/2202.02325>. Read its introduction/definitions and Section4, *Weighted geometric symmetrizations*, pp.14–16. For a singleton nonnegative matrix set, its S_(1/2) operation is the same geometric symmetrization; the displayed Section4 bounds include the familiar spectral-radius comparison with the original operator.

This primary reading identifies the operation and its existing surrounding theory. It is **not** a claim that that paper prints B6's exact centered cubic-trace lemma or its PH-family consequence. B6's explicit three-vertex walk comparison remains its actual written proof of the needed direction. Priority for that combination or its special-family application has not been established.

## 3. Spectrum realization does not discharge repeated-pole transfer obligations

The additional primary paper actually read is Ricardo L. Soto, Mario Salas and Cristina Manzaneda, *Nonnegative Realization of Complex Spectra*, Electronic Journal of Linear Algebra20,2010,pp.595–609: <https://journals.uwyo.edu/index.php/ela/article/download/793/793/793>. Read the introduction and Theorem2.1 with its proof (pp.595–598), and the following small-matrix realization statements.

Theorem2.1 gives a sufficient nonnegative spectral realization using a partition into realizable sublists and a nonnegative coupling matrix with prescribed spectrum and diagonal. Its output is a matrix with the target algebraic eigenvalue multiset. That statement by itself does not prescribe a PH initial row and exit vector, nor the Jordan-chain/controllability data needed for repeated poles in a transfer. A matrix with a repeated but semisimple nonreal eigenvalue may have a resolvent with only a simple pole at that value.

Accordingly it would be unsound to substitute a spectral realization statement for the literal PH transfer construction in C7 or C8. Their companions, positive h, actual alpha/exit and resolvent cancellation are load-bearing. This is a source-interface distinction, not a claim that the2010 methods cannot be specialized to obtain related or stronger constructions.

## 4. Latest general PH paper's actual scope

The current accessible v2 is Liu–Yao–Zhang, *A Non-convex Optimization Approach of Searching Algebraic Degree Phase-type Representations for General Phase-type Distributions*, arXiv2409.12673v2,15February2025: <https://arxiv.org/html/2409.12673v2>. Its actual abstract and Introduction were reread. They explicitly target an iff for the minimal PH representation to have the **same order as the algebraic degree**, and an alternating-minimization method for that condition. This matches the earlier frozen source comparison; it must not be paraphrased as an already-proved general exact-minimum algorithm for arbitrarily many canceled modes.

The introduction also explicitly distinguishes PH order from algebraic degree and says the general problem remains far from solved. Neither that broad status statement nor this bounded source read certifies the novelty of any present constant or construction.

## 5. Consequence for honest status

- The symmetric skewness inequality is **classical**, with an exact displayed equivalence and known1944 attribution.
- Geometric symmetrization, companion realization, canceled extra modes and positive diagonal normalization are established tools; no new-general-tool claim is made.
- B6's specific unrestricted PH6 elimination retains its actual written-check disposition, not a priority verdict.
- The C7 extension source023ac861... now has an actual complete MathShor peer reconstruction at `../shor-completion/peer-review-PH-seven-state-v1.md`, pin `bb34649e5f3eadb3509f71f9666091007d33f678e2e9cb80f13794509ead3099`, reporting0F/0M/0 substantive minor. Its full231-line body was read. Parent disposition remains a separate gate.
- C8 sourcee110dd1f... remains a separate upper-bound candidate, not exact order8 and not promoted by C7's review.
- No exact prior match to the present PH thresholds has been authenticated in these additional readings. This bounded negative observation is not an exhaustive novelty screen. **NOVELTY_UNCLEAR remains operative**, and all earlier primary/corpus scope limitations survive.
