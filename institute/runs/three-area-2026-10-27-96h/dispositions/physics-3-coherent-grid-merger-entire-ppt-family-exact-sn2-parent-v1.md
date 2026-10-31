# Coherent merger of 4×5 grid extensions: the entire PPT output family has Schmidt number two

**Disposition: same-harness written support plus independently authored exact finite physical-matrix corroboration, parent-run once.** This closes a SPECIFIC physically meaningful attempt to obtain a 4×4 PPT/SN3 state by coherently merging two extension coordinates of the specified 4×5 grid family. Every PPT output of this family has **Schmidt number exactly two**, including arbitrary complex merging coefficients and the exact PPT boundary. It is NOT an unrestricted 4×4 PPT/SN3 no-go, a 4×4 SN3 witness or an exhaustive classification of filters.

## Exact physical family and PPT region

Write [x]=|x><x| and

A=|00>+|11>+|22>, B=|01>+|12>, D=|10>−|21>, F_v=|02>+v|33>, E_u=|20>+u|33>.

For s,r>0 and arbitrary complex u,v, the ACTUAL 16×16 PSD operator is

R=[A]+[B]+[D]+s[F_v]+r[E_u]+s|v|²[03]+r|u|²[23]+r[30]+s[32],

with Z=Tr R=7+2(s+r)+2(s|v|²+r|u|²)>0. It is the Bob-filter output of the explicitly specified 4×5 positive grid-extension operator Q_sr: K fixes Bob0,1,2 and maps old3→u|3>,old4→v|3>. Scaling by 1/sqrt(max(1,|u|²+|v|²)) makes K a physical contraction without changing normalized output. This is a COHERENT merger retaining the original core, not an arbitrary 5→4 filter or a spectator extension.

The actual Bob partial transpose is PSD exactly when the central block on(02,11,20),

M=[[s,1,1],[1,1,−1],[1,−1,r]],

is PSD. Its Schur complement is [[s−1,2],[2,r−1]], hence

**R is PPT iff s>1,r>1,(s−1)(r−1)≥4.**

Equality is included. All remaining disjoint blocks are positive and retain the correct complex conjugates. On this region sr≥9. Both normalized local supports have rank4 iff (u,v)≠(0,0); at u=v=0 Alice/Bob ranks are4/3. Every parameter point remains a legitimate normalized PSD state even when its partial transpose is not PSD.

## Explicit complex rank-two upper bound and entanglement lower bound

A root-average family of physical coefficient matrices has C2=z^−1 C1 and C3=alpha w C0+alpha z w C1, so every vector has complex Schmidt rank≤2. Averaging over distinct characters of C4×C3 gives a positive twelve-vector decomposition of the core and F_v extension; reflecting by a physical swap/sign map gives the analogous E_u identity. The three cases v=0, v≠0 with |v|≤r|u|, and |v|>r|u| exhaust all complex coefficients. Their residual filler coefficients are nonnegative on the exact PPT region, including equality/zero endpoints; the comparison is |v|²≤r²|u|², not r|u|². Every output therefore has SN≤2.

Its actual local 3×3 compression has range matrices [[a,b,c],[d,a,b],[e,−d,a]]. A rank-one element has minors a²−bd=a²+bd=0, so a=0 over C. In any positive separable decomposition every product vector lies in that range, forcing a zero 00 entry; the actual compression has 00 entry one. Thus the compression and R are entangled, establishing **SN(R/Z)=2** for the whole PPT family. Every valid Hermitian detector nonnegative on ALL COMPLEX rank≤2 vectors has nonnegative expectation on these actual outputs; a finite sample alone cannot certify that universal detector property.

The physical 4×5 parent Q_sr is itself PPT in the same region and has **SN exactly3**. Its actual range matrix Y is displayed in the [author source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f490-ppt44-actual-sn3-boundary-or-global-certificate-frontier/review-v1.md); all five specified 3×3 minors g1,…,g5 vanish for every rank≤2 range vector. The exact identity

\[a(g_5-g_3-g_4)-\tfrac12(cg_1+eg_2)=a^4\]

forces a=0; positivity/range then contradicts Q's nonzero 00 entry. Its explicit positive projector decomposition has ranks at most3, proving the upper bound. The same family thus exhibits a real physical SN3→SN2 drop under this specific coherent merger, not the conjectured SN3 preservation.

For the concrete assigned s=r3,u=v1 member, Tr R=Tr Q=31; both 4×4 output marginals are diag(8,3,8,12)/31. The actual filter K/sqrt2 applied to Q/31 succeeds with probability1/2 and yields R/31. This is an explicit full-local-rank PPT/SN2 state, NOT an SN3 counterexample.

## Primary-source comparison and a localized printed identity error

Parent directly read [Krebs–Gachechiladze, arXiv:2509.07086v1, Theorem5 and Eqs.11–12](https://arxiv.org/html/2509.07086v1). The 4×5 PPT/SN3 parent construction and displayed range are PRIOR published work; no worldwide novelty or priority claim is made. The paper’s displayed immediate post-Eq12 expression is **not** the corrected multiplier above. With the paper's own five displayed g_i and notation a=psi00,b=psi01,c=psi02,d=psi10,e=psi20, direct algebra gives

\[\text{printed LHS}-a^4=a^2ce+2bcde.\]

The parent’s [prospectively recorded exact formal substitution](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/krebs-gachechiladze-2025-eq12-primary-multiplier-parent-check-v1.json) a=b=c=d=e=1 gives g=(0,2,0,−2,0), printed LHS4 versus a⁴1, while the corrected identity gives1. This disproves that displayed expression **as a polynomial identity**, not Theorem5 or its SN3 conclusion: the formal substitution is not a common zero of the g_i, nor a purported state/counterexample. The independently derived corrected identity proves the needed implication when all five minors vanish. Primary source text was inspected; its complete external proof, illustrations, priority history and any later correction were not independently audited here.

## Evidence and finite limits

[Complete original f490 author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f490-ppt44-actual-sn3-boundary-or-global-certificate-frontier/review-v1.md) · [f524 PPT/complex-decomposition review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f524-ppt44-coherent-grid-merger-ppt-and-complex-rank2-decomposition-review/review-v1.md) · [f525 independent parent-SN3/range review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f525-ppt-grid-parent-sn3-and-coherent-merger-exact-sn2-review/review-v1.md) · [f526 independent finite-report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f526-ppt-coherent-grid-merger-independent-exact-physical-finite-check/review-v1.md) · [materialized exact source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f526-ppt-coherent-grid-merger-independent-exact-physical-finite-check/independent-ppt-coherent-merger-physical-exact-v1.py) · [actual parent one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f526-ppt-coherent-grid-merger-independent-exact-physical-finite-check/parent-independent-finite-run-v1-receipt.json). Parent displayed all589 author,369/427 written-review and1009 finite-report/source logical lines, checked the exact source paper equations, parameter coverage, actual filter and both rank/range arguments. Both written reviews report0F/0M/0m for the candidate; their earlier statements that the public printed multiplier was unadjudicated remain historically accurate at their read scopes, and the later parent-only screen is not attributed to them.

After full static source read and GO, parent ran the independent Gaussian-rational/character-polynomial checker ONCE: exit0, empty stderr,0.8613s. It exactly checked EIGHT PPT physical cases (complex and zero coefficients, both decomposition branches, boundary and interior), FIVE physical but non-PPT parameter cases, full operator filter equality, partial transposes and PSD by exact LDL, rank-two root averages and residual positivity, five formal 4×5 range minors and the corrected a⁴ identity, assigned trace/marginals/success probability, and eight intended-reason controls. The false-detector control only rejects a specific invalid detector using a rank≤2 vector; it does NOT prove universal block positivity. The mathematical continuum family rests on the written decomposition, not an inference from eight points.

In producing the parent-only primary-source screen, the GO and exact substitution were completed; a subsequent clock-helper variable shadowing caused receipt creation to fail. Parent restored only the accidentally shadowed child-process binding, reread the source, and wrote the receipt from retained actual results without rerunning the calculation; a retry merely refused GO overwrite before any new calculation. All held episodes AND their consumers remain NONINPUT.

General 5→4 maps mixing core/extension coordinates, other grid/filler families, unrestricted 4×4 PPT/SN3 existence or impossibility, source-wide equivalence, later corrections, novelty, independent-family,human and formal/kernel verification remain unpaid.
