# Actual PPT4×4 outputs: a genuine mixed-filter exterior with exact Schmidt number two

**Disposition: scoped same-harness written support plus independently authored exact finite physical checks.** Recorded UTC 2026-10-31T02:51:47.840Z. Let s,r>1 with (s-1)(r-1)>=4, and define the actual 4×5 positive operator

Q=[00+11+22]+[01+12]+[10-21]+s([02+34]+[32]+[04])+r([20+33]+[23]+[30]),

where [v]=vv†. For arbitrary finite complex w=(alpha,beta,gamma,0)^T let K_w=[I4 | w], R_w=(I⊗K_w)Q(I⊗K_w)†, n=|alpha|²+|beta|²+|gamma|², T=7+4(s+r) and Z=7+2s(1+n)+4r. The physical filter K_w/sqrt(1+n) on Q/T succeeds with p=Z/((1+n)T) in (0,1) and produces R_w/Z.

For EVERY finite alpha,beta,gamma, the actual output is PPT, has both local ranks4, and is entangled. If beta≠0, set a=|alpha|²,x=|gamma|²,y=|beta|², kappa=r/(r+s), eta=s/(r+s),

q=x/s+a/(r+s)+{[1+x+x²+a(1+x)]/s+a(x+a)/r}/y.

If q<=1, including equality, its EXACT Schmidt number is2. More generally this holds whenever the explicit Hermitian M below is positive semidefinite, including singular boundary; q<=1 is sufficient, not necessary for that particular M or for SN2. This strictly extends the previously [adopted ellipsoid and coordinate lines](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-3-actual-core-mixing-ppt-ellipsoid-and-coordinate-lines-exact-sn2-parent-v1.md) to nonempty genuinely mixed beta/gamma exterior regions. It does not prove all finite w are SN2, any SN3 detector, arbitrary fourth filter component, all filters or global PPT44.

## Exact positive rank-two construction
Set A=00+11+22,B=01+12,D=10-21,F=02+3w,H=0w,G=32,P=30,J=20+33. Let C have columns (F,H,G,P), and

t1=(-gamma,1,gamma²,alpha gamma)^T/beta; t2=(0,0,gamma,kappa alpha)^T; t3=(alpha/beta)(1,0,-gamma,-alpha)^T; t4=(0,0,-eta alpha,0)^T; M=diag(s,s,s,r)-sum_j t_j t_j†.

The actual kets X_j=Ct_j obey X1=(alpha/beta)00+01-gamma31 and X3=(alpha/beta)02+alpha31. For all six z with z^6=1, V_z=A+zD+z^-1 X1+z^-2 X2+z^-3 X3+z^-4 X4 has Schmidt rank exactly2: its first and fourth coefficient rows are explicit combinations of its independent second and third rows, as displayed in [F862](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f862-ppt44-exterior-mixed-character-decomposition-proof-author/author-candidate-v1.md). The six character exponents are distinct modulo6; hence mean_z[V_z]=[A]+[D]+sum_j[X_j]. The SAME actual output has the identity

R_w=mean_z[V_z]+[B]+r[J]+r[23]+C M C†.

C's columns are supported only on Alice rows0 and3; if M>=0 its positive square-root columns give finitely many additional Schmidt-rank<=2 kets. Beta≠0 makes C injective, so M>=0 is also equivalent to positivity of THIS particular residual CMC†, not to a necessary SN2 condition for every decomposition. With W=diag(s,s,s,r)^(-1/2)[t1 t2 t3 t4], sum column norms²=q and Cauchy-Schwarz gives M >= (1-q)diag(s,s,s,r). No ket coefficient is incorrectly conjugated; outer products use †.

For alpha=0 and0<=x<s, the SAME residual is PSD iff y >= (1+x)/s + x²/(s-x), including equality. At x>=s it is not PSD for finite y; that says nothing about another decomposition. For0<x<s this test is strictly sharper than q<=1. The beta=0 locus is NOT covered by the dividing construction; prior coordinate-line theorems remain separate.

For EVERY admissible s,r, any finite alpha with a<r+s, and any nonzero gamma satisfying x/s+a/(r+s)<1, sufficiently large finite |beta| satisfies q<1 and y/s+x/(s-1)>1. These points have beta gamma≠0 and lie outside the old ellipsoid AND both old coordinate lines; all phases are free. Equality q=1 is included in the theorem, not asserted open. F863 independently gives an explicit q=1 strict-exterior family.

## Physical PPT and exact lower bound
The actual partial transpose of Q is a direct sum of positive scalar and 2×2 blocks and the (11,02,20) block [[1,1,-1],[1,s,1],[-1,1,r]], whose Schur complement is [[s-1,2],[2,r-1]]>=0 by the stated region. For complex K, R_w^Gamma=(I⊗conjugate K)Q^Gamma(I⊗conjugate K)†. The range of R_w has the actual coefficient-matrix form in [F863](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f863-ppt44-exterior-mixed-physical-PPT-and-range-proof-author/author-candidate-v1.md). A product vector in that range has minors m1=u²+bd,m2=ud-be,m3=ue all zero; u²m1-ubm2-b²m3=u^4 forces u=0, hence its physical11 entry vanishes. But (R_w)_(11,11)=1, so no positive separable decomposition exists. The positive rank<=2 decomposition yields exact SN2 wherever M>=0. The original parent Q's historical SN3 assertion is a separate named source import if calling this an SN3-to-SN2 transition; it is not needed to prove the output statement.

An actual exterior anchor s=r=3, (alpha,beta,gamma)=(1,3,1) has q=41/54, old ellipsoid value7/2, n=11,T=31,Z=91 and physical success91/372. Exact complex fixtures include a singular M with q=5/4: failure of the scalar bound is not failure of the stronger M test. Negative M outside this certificate does not prove SN3.

## Evidence and assurance
Parent fully read [F851 191LF author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f851-ppt44-uncovered-mixed-filter-same-state-frontier-author/author-candidate-v1.md), [F862 written reconstruction](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f862-ppt44-exterior-mixed-character-decomposition-proof-author/author-candidate-v1.md), [F863 physical reconstruction](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f863-ppt44-exterior-mixed-physical-PPT-and-range-proof-author/author-candidate-v1.md), [F864 narrative](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f864-ppt44-exterior-mixed-decomposition-exact-finite-author/author-candidate-v1.md) and all654LF of [operative exact v2 source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f864-ppt44-exterior-mixed-decomposition-exact-finite-author/finite-ppt44-mixed-exact-v2.py) before its one GO. F862/F863 are nonblind same-harness GENERAL AUTHORS, not human/independent-family/kernel reviewers. F862's additional general phase-gauge Gram matrix and new beta-axis alternate proof are not separately adopted here.

One [exact v2 parent run](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f864-ppt44-exterior-mixed-decomposition-exact-finite-author/parent-ppt-mixed-v2-run-v1-receipt.json) returned five CASE records and terminal STATUS PASS. It constructed the actual20×20 Q and16×16 R/PT, checked exact complex conjugation, physical traces/local ranks, all15 Hermitian residual principal minors, actual positive residual factorization, each of16 symbolic rank3 minors and96 root-specialized minors per case, exact six-character averages and intended-reason mutants. Cases include q=1, singular M with q=5/4 and nonPSD M with q=2; the latter is NOT an SN3 counterexample. Internal source limit40s; tool-reported duration745ms; numerical exit and separate raw stderr were not exposed and are not inferred. Five fixtures do not prove the universal region; the written proof carries the quantifier. F864v1's missing signal latch/unflushed settlement was ONE pre-run DESIGN MAJOR and v1 was NEVER RUN; the new v2 was wholly reread and separately authorized. All genuine held episodes AND ALL consumers remain NONINPUT. No original-source authentication, novelty, priority or stronger assurance follows.
