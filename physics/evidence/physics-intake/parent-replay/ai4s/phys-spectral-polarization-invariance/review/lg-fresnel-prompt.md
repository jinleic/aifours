# Hostile referee: approved restricted-Fresnel necessity/sufficiency theorem

Today is 2026-10-14. The user approved choosing a precise subproblem of the book's broad spectrum/polarization-invariance question. Review the new C8 theorem in RESULTS.md, not a claim to have solved all sources or Maxwell propagation. No scientific priority is claimed.

## Permissions

Read only files inside `/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/`. Do not read workspace instructions, secrets or files outside this folder. Do not delegate, edit/write files, install anything, run account actions, or launch long computation. Do not run any verification script, because scripts write their result files. Small standalone write-free mathematical calculations are allowed. You may make at most six primary-source web checks for the exact prior-art class. Final report only; the caller captures it.

## Read set

- RESULTS.md C8: complete proposed theorem and proof; C2: already independently reviewed two-mode channel classification used as a lemma; C6: retained physical counterexample to indiscriminate all-probe necessity.
- code/lg_fresnel_classification.py and results/lg-fresnel-classification.json: current exact computations and physical propagation checks.
- STATUS.md and README.md: scope/novelty context. They are being updated with the new scoped result; missing final review dispositions are not a mathematical finding.
- Prior referee reports, only if useful: review/codex-review.md and review/fresnel-bridge-review.md. Do not let prior agreement substitute for checking C8 independently.

## Exact proposed scope

Fix any k>0, waist scale a>0, integer m>=1. On the source plane, with R=r/a and M=m+1,

psi_0,epsilon = R^m exp(-R^2/2) exp(i epsilon m theta)/(a sqrt(pi m!));
psi_1,epsilon = (M-R^2) psi_0,epsilon/sqrt(M), epsilon=+1,-1.

These are four orthonormal scalar LG spatial modes, radial n=0,1 and azimuthal +/-m. The source covariance is Gamma_+ direct-sum Gamma_-, each an arbitrary PSD 4x4 radial/polarization matrix, with NO covariance between azimuthal sectors. Rotation here means spatial-coordinate rotation with fixed polarization labels, not combined Maxwell spin/space rotation.

Question: characterize ALL nonzero such covariances with one local two-component spectral degree P_star in [0,1], at every illuminated point for every forward full-plane scalar Fresnel distance z>=0.

## Proposed bridge and classification

Let t=z/(k a^2), Q=1+i t. Fresnel propagation gives common radial amplitudes for +/-m:
q0 = R^m exp[-R^2/(2Q)]/(a sqrt(pi m!) Q^M),
q1/q0 = [M |Q|^2-R^2]/[sqrt(M) Q^2].
The formula is proved by the radial paraxial PDE and a Gaussian-parameter derivative, not assumed from a fit.

For K=Gamma_++Gamma_-, Phi_K(X)=sum_bc X_bc K_bc, the actual local coherency matrix is Phi_K(q q*), where q=(q0,q1). Angular factors cancel because cross-sector covariance is absent.

Crucial correction to an initially suggested route: forward responses w=q1/q0 are NOT dense in CP^1. Their closure misses the lower half-plane outside radius sqrt(M), in this phase convention. However they contain the entire open UPPER half-plane: for w=rho exp(i phi), 0<phi<pi, choose t=cot(phi/2), R^2=(1+t^2)(M+sqrt(M)rho). Then w is attained at finite z and r>0.

Let T=Phi_K*(I), with T_bc=tr K_cb. Nonzero PSD K implies nonzero PSD T. In the chart f=(1,w), trace vanishes only on ker T, hence at most one chart direction; r=0 is dark independently. The constant-degree condition clears to the real polynomial
F(u,v)=(1-P_star^2)[tr Phi_K(f f*)]^2 - 4 det Phi_K(f f*), f=(1,u+i v),
of degree <=4. It vanishes on the attained upper half-plane except possibly one dark point, hence identically. Homogeneity and polynomial continuity cover f0=0, the projective direction not physically attained at finite radius. PSD guarantees zero matrix at zero trace; P is never assigned at a dark point. Thus Fresnel invariance is equivalent to the all-RADIAL-probe property of SUM K, not all-four-spatial-probe invariance of the original source.

Apply the already proved C2 after trace-support whitening Psi(X)=Phi_K(T^-1/2 X T^-1/2). The permitted maps are exactly:
A: replacement tr(X) C, C PSD trace1 degree P_star, trace rank1 or2;
B: trace rank2, P_star U X U* + (1-P_star) tr(X)I/2, 0<=P_star<=1;
C: trace rank2, P_star U X^T U* + (1-P_star) tr(X)I/2, 0<=P_star<=1/3.
The source is then ANY PSD split Gamma_+=L, Gamma_-=K-L with 0<=L<=K. Zero K is excluded as the all-dark source.

C6 is included: K=diag(1,1/2) tensor diag(3/4,1/4), yet the full four-spatial-mode trace support is four. Neither sector individually must have the sum's constant degree.

ABCD corollary: the same condition is equivalent to invariance under every centered lossless polarization-independent isotropic real ABCD system (AD-BC=1). Its Collins kernel depends on cos(theta-theta'), so +/-m receive identical radial transfer. The classified SUM map therefore gives sufficiency for any resulting radial q. Necessity follows because forward Fresnel systems are included. B=0 is scalar magnification/phase. No claim for astigmatic systems, arbitrary rotationally invariant but chiral kernels, cross-sector source correlations, random averaging, other radial indices, or Maxwell fields.

## Observed checks, not a proof by sampling

The new script exited 0 with five PASS groups. It checks arbitrary-integer-m symbolic radial PDE and normalization identities, upper-half-plane inverse identities, seven exact PSD sector/sum families including p=0,1 and transpose p=1/3, nontrivial complex trace whitening, a physical dark direction (m=3,t=1,R^2=12,w=i) with J=0, and a noninvariant diagonal sum with polynomial -16(u^2+v^2). Independent physical sector-covariance FFT2 versus the analytic sum-block prediction passed at 42 cases (m=1,3; z=1.5,4,8; seven sources), maximum matrix discrepancy 3.34e-16, degree discrepancy 1.78e-13 at the declared intensity floor. Independent Hankel-Fresnel quadrature versus analytic radial amplitudes differs by at most 4.49e-14 at its fixed samples. These are empirical consistency checks; the universal necessity relies on the polynomial/open-set proof.

## Prior-art leads

- Martínez-Herrero et al. (2022), vectorial pseudo-Schell sources, https://oa.upm.es/87042/1/9906481.pdf, DOI 10.1016/j.optlastec.2022.108079: retained angular matrix gives propagation-invariant nonuniform polarization patterns; not assumed to classify arbitrary PSD four-LG-mode covariances.
- Yajun Li (2015), Laguerre-Gaussian functions and generalized formulation of electromagnetic Gaussian Schell-model sources, DOI 10.1364/JOSAA.32.000877; publisher abstract https://opg.optica.org/services/open_md.cfm?uri=josaa-32-5-877. LG-correlated GSM is not automatically the same as a four-coherent-mode covariance truncation.
- Pampaloni and Enderlein, arXiv:physics/0410021, standard differential-operator/Gouy-phase derivation of LG beams.
- Standard Bloch-channel geometry in Ruskai/Szarek/Werner arXiv:quant-ph/0101003. Do not claim the channel lemma or Gouy phase is new.

## Required final response

Give separate mathematical verdict (correct / correct-with-fixes / incorrect) and novelty verdict. Number findings by severity, citing the exact issue and correction. Check the all-m propagation ratio, actual reachable set and its closure, zero source/rank1/dark cases, PSD contraction conventions, trace whitening, sum versus individual sectors, completeness of the PSD split parameterization, and the isotropic ABCD corollary including B=0. Inspect whether the numerical source actually exercises arbitrary within-sector correlations rather than only diagonal examples. Look for a real counterexample, but do not manufacture concerns or mistake the stronger SUM-radial property for the earlier refuted global property. End with the strongest defensible theorem statement and any unresolved proof obligation.
