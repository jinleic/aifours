# Hostile referee: all-N mixed-parity Hirota construction

Today is 2026-10-14 PT. Read ONLY user files under `/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-mixed-parity/`. Do not delegate; do not create/change files; do not install; do not fetch private data or use the web. Do not read sibling files, workspace instructions, credentials, or configuration. The caller saves your final answer. You may extract the pinned PDFs to stdout. Avoid running code/verify.py unchanged: it imports an out-of-scope sibling and writes a report. Small exact in-memory calculations on this folder's code are welcome, with bytecode disabled. No large search or test-suite run is needed.

Assignment: determine whether the complete written proof in RESULTS.md genuinely establishes the following theorem for every N, not merely for the exact samples:

P=Dt+c1 Dx+c2 Dx^2+c3 Dx^3, c2 != 0. For every finite N and every F/G type pattern, construct F,G with constant terms 1 and arbitrary independent active amplitudes A_i. Generic F seeds have w_i=-p(k_i), G seeds w_i=p(-k_i); transverse l_i are independent of k_i. Prove P F.G=0 and Dy P F.G=0. Include c3=0. The DxP reduction uses l_i=k_i followed by y=0. No general Lax/full-book integrability or novelty is claimed.

Read README.md, STATUS.md, RESULTS.md, code/tau_formula.py, code/verify.py, and results/verification.json (the latter is finite control data only). Source/manifest.json pins accessible Li-Lou/Hietarinta primary papers and Peng metadata. Peng's full text remains unavailable, so originality is explicitly unverified. The original user approved a precise subproblem; this is a second parity branch of the SAME book chapter, not another unrelated book problem.

Critical proof structure to attack:
1. Universal bordered-Pfaffian lemma: with H_X=r1 wedge r0, H_s=r3 wedge r0-2r2 wedge r1, rj_X=rj+1 and rj_s=rj+3, (Dx^3-Ds) Pf(H).[r0,v]_H=0 for v independent of X,s. Check rank-two update signs, singular H, and the four-border Jacobi identity.
2. Block construction K=[[A,I],[-I,-B]], L=K+q wedge a, r0=q+a, Fhat=sigma Pf(L), Ghat=sigma(Pf(L)+[r0,a-b]_L). Check both bilinear equations, especially the independently necessary transverse identity Ghat_y=-sigma[r0,b_y]_L from J=K+(q+a) wedge b. Do not assume the sibling's former conjecture; all derivations are included here.
3. Pfaffian minor-sum/Schur dictionary, odd dummy index LAST, no division by a seed amplitude. Typed Fhat has only charge 0,+1; typed Ghat only 0,-1.
4. For c3 != 0 set delta=c2/(3c3), p0(r)=c3*r^3+(c1-3c3*delta^2)r, r_i=k_i+epsilon_i delta. Add auxiliary F index r0=delta,l0=0, amplitude u. Scale active F amplitudes by u, G amplitudes by u^-1 A_i lambda*k_i/(lambda*k_i-1), lambda=3c3/(2c2). Since Fhat=F0+u Fplus and Ghat=G0+u^-1 Gminus, the u^1 coefficient of EACH bilinear identity is uniquely Fplus.G0. Does that really license the projected pair?
5. Set physical F=e^-theta0 Fplus, G=G0. Check operator shifts, time signs, both dispersions, seed normalization, and that the auxiliary zero transverse mode is allowed by the actual matrix lemma rather than by the generic seed test.
6. For every selected full index set T, its type counts obey m=n or m=n+1. The total lambda power is choose(m,2)+choose(n,2)-mn+n=(m-n)(m-n-1)/2=0. Does the resulting explicit Q_ij/Pfaffian formula remain regular at lambda=0 and prove the QUADRATIC branch for all N by rational specialization? Check that no hidden divergent phase/background or denominator invalidates this step.
7. Genericity: every type pattern, independent amplitudes and transverse waves, all formal coefficient equations, not just ones with no doubled exponential. Check the unique recursive-ansatz identification and edge cases N=0,1, all-F/all-G, zero amplitudes, tau zeros, and stated denominator exclusions.

The scientific program observed: 444 exact rational cases through N=7, all type patterns through N=5, agreement with shared recursion and all residuals zero; 12 separate polynomial-differentiation cases; symbolic pair, gauge, and cardinality identities; two negative controls. These are controls, NOT the all-N proof. The newly added zero-soliton vacuum check will be included in final smoke; do not count it as previously exercised.

Return English, concise but substantive:
- verdict CORRECT / CORRECT-WITH-FIXES / GAP / FALSE;
- numbered real findings with severity, file/line evidence, and a concrete correction or counterexample;
- exact mathematical steps independently checked, computations actually performed;
- every remaining unproved step within the stated theorem, if any;
- whether SOLVED (precise written theorem), Certification, and NOVELTY-UNCLEAR are honest labels.
Do not confuse a written/model-reviewed proof with a Lean kernel proof. Do not give a new research plan or generic praise. The folder is frozen for this review.
