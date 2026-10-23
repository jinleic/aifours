# New conditional research lead: extend the Lev argument from BASE2 to the full LS parameter interval

Recorded at 2026-10-19T09:20:00-0700. **CANDIDATE_UNVERIFIED / INFERENCE**, not a parent verdict. This is a new general-parameter derivation, not a restatement of the frozen BASE2 closure. No computation. Every imported scope and bound below needs independent source verification and hostile review.

## Proposed target
Prime p>=7; floor(2p/3)+1<=kappa<=p-2; put e=p-kappa>=2 and h=e-1. Prove LS(p,kappa) for ALL these kappa, sequence level only. Do not claim LS+, STAB, INV* or ordered Olson, and do not call this novel. The previous BASE2 files have a narrower scope and cannot simply be invoked as the general theorem.

## Conditional argument to audit
1. RED, DGM-p, threshold dichotomy and accepted LS-II' should reduce a threshold counterexample of length p+2kappa+1=3p-2e+1 to caseI with dominant g0, M=2p-d, 1<=d<=e-2=h-1, |U|=p-2e+1+d. Verify those imports at the FULL interval. If e=2 the d-range is empty, so no core argument is needed.
2. For every actual occurrence W<=U, F*: rho(W)<=h => |W|+2rho(W)<=d-1. Its CF(a) size hypothesis is |U|+2h=p-1+d<2p. For maximal zero-sum Z0, k=|Z0|<=d-1, delta'=d-k>=1, U'=U-Z0 is zero-free of length n=p-2e+1+delta', with F' RHS delta'-1.
3. Set t=max(1,floor(delta'/2)). F' forbids [t,h], so inclusive |Sigma(U')|<=p-e+t<2n: the difference is p-3e+2+2delta'-t>0 because p>3e. **Lev2022 T2** (statement-level external import, proof not replayed) gives positive coefficients and the full integer coefficient interval 0..S with n<=S<p, relative to a nonzero multiplier a.
4. Pin a=-1, not an arbitrary translation. Arc length l=p-1-S<=2e-2-delta'. For delta'>=2, N=h-t gives N+1 points and l<=2N, 3N<p, hence accepted AP(R6) gives inverse a=+-1 and +1 is impossible. For delta'=1, N=h-1=e-2 (check e>=3), l<=2N+1, 3N+2=3e-4<p; AP'(D1) gives +-1,+-2. +1,+2 are too small; -2 at rho=h has representative p-2h=p-2e+2=n<=S. Therefore a=-1 and S<=p-h-1=p-e.
5. The existing BASE2 ZCLASS/crossing argument should re-prove at general parameters, not be imported outside scope. Put R=p-S-h, so 1<=R<=e-delta'<=h. Localisation gives positives zeta<=floor((d-2)/2) or negatives -nu, nu<=R-1. Positive weighted crossing gives q+2P<=d-1, P<h. If total negative magnitude reaches R, its first crossing N_V in[R,2R-2] yields s=p-N_V-h<=S and
   s>=2S+h-p+2>=p-3e+3+2delta'>0.
   A real core subset with coefficient sum s then makes residue h, forbidden by F*. Thus negative total<=R-1. R=1 has no negatives. Signed witness differences lie in[-p+h+1,P] inside(-p,p-1).
6. **The only BASE2-specific step to replace is L1.** Do not assume the shortest long zero-sum has length2p+2 for general kappa. Use accepted SLZ3 ONLY on a shortest long zero-sum T: under ZP its length is even, 2p+2j with
   1<=j<=floor((3kappa+1-2p)/2)=floor((p-3e+1)/2).
   Writing T=g0^i W* gives rho(W*)=-j and |W*|>=d+2j. This is a NEW generalized witness lemma, to prove directly from ord(g0)=2p and coefficients 2mu+1.
7. For W*=W' disjoint-union Z*, ell=|Z*|<=d-1, core coefficient sum s, signed Z* sum zeta_tilde, tau=zeta_tilde-s lies in[-p+h+1,P]. Since p-j>h>P, the positive lift p-j is excluded and the only possible congruent lift is tau=-j. Therefore
   d+2j<=|W*|<=s+ell=zeta_tilde+j+ell,
   so zeta_tilde>=d+j-ell>=j+1>=2. Also zeta_tilde<=P<h. The actual subset Z* has least residue zeta_tilde and
   ell+2zeta_tilde>=d+j+zeta_tilde>d-1,
   contradicting F*.
8. If every full-range prerequisite and step is correct, RED yields LS(p,kappa) at all permitted lengths and kappa. The general argument must stay separate from the still-unaccepted BASE2/normalization records until reviewed.

## Verification obligations
Check AP/AP' hypotheses including small e and the original domain definitions; DGM/LS-II'/RED at all kappa; SLZ3 range and shortest-only usage; j endpoints, p-j>h, occurrence-level coefficient availability and disjointness; signed versus nonnegative CF sums. Preserve the external Lev proof trust boundary. Correctness, literature priority and general ordered-word closure are separate questions.
