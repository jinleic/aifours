# Hostile mathematical referee: exact-radius, uniform-density spiral Delone sets

Today: 2026-10-14. Read only inside `/Users/jinleic/jinleic-workspace/ai4s/phys-spiral-delone-uniform-density/`. Do not delegate further, write/edit files, execute code, install packages, contact anyone, access credentials or browse unrelated material. Your available tools are read-only file tools. Do not run code/verify.py because it writes results. Final report only; the caller captures it.

## Task

Independently verify or refute the complete theorem in RESULTS.md. This is a candidate answer to an explicit primary-source question, not merely a local lemma. Novelty/history is a SEPARATE obligation being researched independently; do not infer priority from correctness or from a search miss.

The physics-book bridge is packing/phyllotaxis, not a full elastic cone-energy theorem. The exact source is Adiceam–Tsokanos, Higher Dimensional Spiral Delone Sets, arXiv:2010.06428v3 (30 Mar 2021), §6 pp22-23. Pinned PDF and images are in source/. On rendered p23 it states: “It is not clear to the authors whether a spiral Delone set with asymptotic density r = V_n^{-1} can exists in any dimension n >= 3.” On p22 density means the limit for EVERY bounded Jordan-measurable X, not just centered balls. The symbols are V_n^{-1}, not V_(n-1). Definitions pp1-4 allow arbitrary spherical sequences; no bounded consecutive step or orbit is required.

## Read set

- review/input/RESULTS.md: frozen complete written proof to audit.
- review/input/verify.py and review/input/verification.json: frozen generator/checker and observed results. These are NOT a proof by sampling.
- source/primary-evidence.json; source/open-question-page-22.png and source/open-question-page-23.png; source/adiceam-tsokanos-v3.pdf if the definitions need checking.
- README.md is only introductory context. STATUS.md may be completed concurrently; its absence is not a proof defect.

## Proposed construction and crucial steps

For every fixed integer n>=2, enumerate ALL nonzero integer vectors z_k in Z^n by increasing Euclidean norm, with lexicographic ties. Define c=V_n^(1/n), u_k=z_k/|z_k|, s_k=k^(1/n)u_k. Nonprimitive vectors are INCLUDED. Claim: exact radii, effective construction, uniform all-pair separation, ambient covering, all-Jordan-region density 1/V_n, angular cap uniform distribution.

1. Ball count: N0(R)=#(Z^n intersect closed B_R)=V_n R^n+O(R^alpha), alpha=n(n-1)/(n+1), for ALL real R>=2. Proof uses Fourier convention exp(-2pi i x.xi), ball transform R^(n/2)|xi|^(-n/2) J_(n/2)(2pi R|xi|), fixed-order Bessel bound O(x^-1/2), and compact smooth nonnegative mollifier supported in B_1. Sandwich 1_(B_(R-eps))*phi_eps <= 1_(B_R) <= 1_(B_(R+eps))*phi_eps. Apply absolutely convergent Poisson summation to smooth functions, and sum nonzero frequencies using O(j^(n-1)) points in unit-width lattice annuli. Error <=C[R^(n-1) eps + R^((n-1)/2) eps^(-(n-1)/2)]. Choose eps=R^(-(n-1)/(n+1)). Beware: no assertion that a very thin discrete shell count equals its volume is allowed. The continuous volume term, not that shortcut, yields the first error.
For n=3 the proof also gives the elementary exact transform [sin(2pi Rq)-2pi Rq cos(2pi Rq)]/(2pi^2 q^3), hence the required O(R/q^2) decay without general Bessel asymptotics.

2. Ties: for r=|z_k|, N_<(r)+1<=k<=N(r), excluding the origin. The same discrepancy estimate applies to strict count by taking a real-radius left limit. Thus |k-V_n r^n|=O(r^alpha) uniformly through all ties; tie multiplicity is O(r^alpha). Difference of n-th powers gives |k^(1/n)-cr|<=|k-V_n r^n|/(cr)^(n-1)=O(r^-beta), beta=(n-1)/(n+1)>0. A leading volume asymptotic alone would NOT suffice.

3. Separation including finite/cross pairs: choose K such that displacement delta_k<=c/4 for k>=K. Tail pairs have distance>=c/2 by lattice separation. Let A=(K-1)^(1/n) (A=0 if K=1), choose L>=max(K,2) with L^(1/n)>A+1. Prefix i<K and j>=L are >1 apart by reverse triangle inequality. Remaining finite pairs below L have positive distance from their distinct exact radii, with a lower bound L^(1/n)-(L-1)^(1/n)>0. Therefore a global positive separation constant exists.

4. Covering: D=sup delta_k<infinity. Round x/c to Z^n; distance<=c sqrt(n)/2. If the rounded vector is zero, use e1 at extra cost<=c. Match that nonzero lattice vector to s_k, yielding cover bound c(sqrt(n)/2+1)+D.

5. EVERY bounded Jordan set: scaled lattice cZ^n has density 1/c^n=1/V_n by box/Riemann-sum counts. Remove origin (one point). Cover compact null boundary of X by finitely many open boxes with sum of volumes<epsilon; their union contains a fixed h-neighborhood of boundary. For large R, D/R<h. If matching lattice and spiral points disagree on membership in RX, the lattice point/R lies in that boundary cover. Lattice box counts bound normalized difference by epsilon/V_n; let epsilon->0. Check this for nonconvex/disconnected/nonclosed X too.

6. Angular UD: cone X_C={r u:0<r<=1,u in a spherical cap C} is Jordan, has volume V_n sigma(C)/sigma(S). With R=N^(1/n), its spiral count is exactly the first-N angular-cap count. Alternative direct lattice-sector proof differs from a completed ball only by the subleading tie count.

7. Effective generator: enumerate integer cube [-M,M]^n, retain 0<|z|^2<=M^2, sort by (|z|^2,z_1,...,z_n); increase integer M until enough points. No omitted smaller-norm vector can lie outside that cube. Exact integer keys avoid rounded norm ties. Each output point is computable algebraically.

## Observed finite controls

The script exited 0 with five PASS groups on its first run. Exact independent cube-sort and recursive sum-of-squares enumerators agreed in dimensions 2,3,4. It includes origin, nonprimitive-vector and partial-tie boundaries; arbitrary-dimension exponent identities; an exact 3D Fourier identity; and negative controls for an insufficient leading asymptotic and constant direction with correct radii. The 3D sample uses 57776 points (lattice radius24), finite minimum separation 1.3558211108940448, sampled covering radius 1.3777041273639627 on 35937 grid queries. These are EMPIRICAL, NOT global certified constants. Some small-scale box-density observations oscillate around the limiting density and are not claimed monotone. All raw summaries are retained in the frozen JSON.

## Required report

Return a mathematical verdict correct / correct-with-fixes / incorrect, numbered findings by severity with precise proof locations and concrete fixes/counterexamples. Check ALL quantifiers: every real radius, every tied shell rank, every pair including finite prefix, every ambient point, every bounded Jordan set, every cap, every fixed n>=2. Check Fourier constants and exponent balance, admissibility of the source definition, and whether the algorithm genuinely enumerates all nonzero lattice vectors. Distinguish accepted standard analytic identities from new bridges; do not elevate sampled behavior to proof. State exactly whether any unresolved lemma remains for the source's n>=3 existence question. No novelty certification is requested from this math-only review. Do not invent defects merely to be critical.
