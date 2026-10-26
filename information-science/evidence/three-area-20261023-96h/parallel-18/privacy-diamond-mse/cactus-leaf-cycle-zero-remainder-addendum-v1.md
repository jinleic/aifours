# Addendum: leaf-cycle zero-remainder and forward-difference domains

Owner: InfoResearch96h-2. Actual observed clock: **Sun Oct 25 08:19:05 PDT 2026**, verbatim /bin/date output. This is additive to the frozen 387-LF replacement-information-primary-screen-v6-cactus-portal-swap-v1.md, SHA-256 9359694947945528ed5bf0b1bd60687468c63bbc8643abf67ccd0b162a7e2cf5. That source is unchanged.

**WRITTEN convention correction. Named imports:** v6 Theorem LC and Lemma LC-B, and run-root cactus-portal-swap-leaf-cycle-parent-v1.md recording the actual v54-B MINOR. Scope remains ONE unadorned leaf cycle, all budgets/portal flags and all original shortest-path ties. No broader cycle/cactus theorem or new verification is claimed.

In LC4, for j>=1 let q=floor(s/j) and rho=s-j*q. Define the residual-gap value PIECEWISE:

```
D_j(s)=j*f_ell(q)                                  if rho=0;
D_j(s)=(j-rho)*f_ell(q)+rho*f_ell(q+1)             if 1<=rho<j.
```

When rho=0 the second term is OMITTED ENTIRELY: f_ell(q+1) is neither referenced nor evaluated. In particular j=1,s=ell-1 uses only f_ell(ell-1), never the out-of-domain f_ell(ell). If rho>0, q+1<=s<=ell-1, so the second branch is within the original f domain.

The case j=0 is handled separately: D_0(0)=0 and D_0(s)=+infinity for s>0. No quotient by zero is formed.

The forward-difference identities LC3 are read only on **0<=r<=ell-2**, so both f_ell(r) and f_ell(r+1) lie in their declared domain. The exchange proof uses only these differences. These conventions preserve the original attainment, profile and polynomial-bound conclusions; they do not extend f outside 0,...,ell-1.

No mathematical interpreter, arithmetic program, enumeration, symbolic package, solver, replay or kernel check was used for this addendum. Parent erratum v9 and the global HOLD remain binding.
