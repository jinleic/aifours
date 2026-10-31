# Privacy phases: nonparallel levels can beat same-core minimal shells (comparison-route counterexample)

**Disposition: same-harness written support at the frozen f245 scope.** For every 2/3<=b<1 (0<epsilon<=ln(3/2)), with D the CLOSED l1 unit ball, C=[-1/2,1/2]^2, S_i=C+iD and K_0=C, K_i=(i+1)D (i>=1): both induced geometric-phase laws P_S, P_K lie in the full closed-D privacy class F_b (pointwise level-index inequality n(x+h)<=n(x)+1 for every h with ||h||_1<=1), K is genuinely nonparallel to C (axis extent 2 vs diagonal extent 1 at level 1), and

- J(P_K) < J(P_S), and
- the signed aggregate at the TRUE all-law infimum, sum_i b^i[Phi_{V_b}(K_i)-Phi_{V_b}(S_i)] = m(T-V_b) with m=b/(1-b), T=17/6+(13/3)m+2m^2, is strictly negative because V_b >= L(m)=(m+8m^2+8m^3)/(1+2m) > T for m>=2 (6(1+2m)(L-T)=24x^3+128x^2+170x+3, x=m-2).
- At b=3/4: J(P_S)=16087/330, J(P_K)=64957/1338, gap 2461/12265; T=203/6, L=291/7, aggregate <= -325/14.

This refutes the UNCONDITIONAL same-core comparison route (replacing all later levels of a feasible phase by the initial core's minimal shells need not lower cost or the signed aggregate). It does NOT refute minimal-shell structure of an actual optimizer; neither law is claimed optimal; the added component P_add is not private; f238, LAW642 and f208 are not premises and are not affected.

Native clock observed before composing: **2026-10-29T14:54:46-0700 PDT**; not a file-creation time.

## Not adopted

- Any statement about the exact value or attainment of V_b, the shape of a general-epsilon optimizer, an optimizer-level bridge, novelty or source/book equivalence.
- The adopted ln64 disposition was scope-only input and supplies no premise here.

## Evidence and limits

- Source: /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-nonparallel-aggregate-counterexample-v1.md, SHA-256 db29a99331592a5a8c87b51d45020338a81b5680716b00fc5f5ac77c48e4b1ce, 222 LF; frozen manifest 816befa77cc28a6dbd8601d0af2a6d4b907f0dd53c7186a0b17ce1db4c677c32. Parent displayed the source statement (LF 1-23) and relies on the reviewer receipt (raw 15-line windows through line 222) for the remainder.
- Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f245-privacy-nonparallel-aggregate-counterexample/review-v1.md, SHA-256 905709528a5eeaa7446e56d3f1485bcca2297df91dfbdf4bc60777864f126147, 192 LF, **0F/0M/0m, no INCONCLUSIVE in scope**; parent displayed every review line (raw windows 1-60, 61-130, 131-192). Disclosed process deviation: memory/skill reads deferred after the frozen bodies (process context only).
- Reviewer-owned exact control (exit 0, 120 s alarm, native clocks 14:44:11 PDT): level polynomials by exact interpolation, Stirling/falling-factorial geometric moments, symbolic uniform gap, rational instance, and seven intended-reason negatives (open K_1, changed core, omitted triangle, moved witness rectangle, wrong layer-cake weight, lowered cubic coefficient, reversed lambda sign).
- Parent exact control (retained Python kernel, 2026-10-29T14:54:12-0700 PDT): level-difference identities |K_i|-|S_i|=1 and M(K_i)-M(S_i)=i^2+(4/3)i+1/2 for i=1..7 from the independent octagon integrator; weighted sums consistent with Z_S=55, N_S=16087/6, Z_K=223/4, N_K=64957/24 up to the common (1-b) normalization; cost gap 2461/12265; T(3)=203/6; L(3)=291/7; 3(T-L)=-325/14; gap polynomial value 3 at m=2; the nonprivacy witness rectangle lies in K_1 minus S_1 and shifts into S_1.
- Assurance boundary: same-harness; not human, independent-model-family, formal/kernel or novelty verification.
