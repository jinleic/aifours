# PH7 chain obstruction on the entire explicit half-line z >= 389/500

**MathResearch96h-2 / math-1. NEW written candidate with exact symbolic/rational checks, not yet independently reviewed.** Actual native observation before writing: **Wed Oct28 17:12:46 PDT2026**. This is an additive strengthening of `frontier-20261028-ph7-three-chain-critical-obstruction.md` (SHA256 `d231c72575c414d0891269e536100c05388896cfd8ce8a4325b50de07a37e817`), whose bytes are unchanged. It excludes ONE explicitly defined PH7 construction family, not arbitrary PH7 representations.

## 1. Exact theorem and the physical quantifiers

Use the SAME earlier-supported `3+1+3` chain family, its actual input/exit and positive diagonal normalization described in the predecessor §2 and in the earlier literal source `PH7-u-deformation-actual-family-v1.md` (SHA256 `9f9b048bd4113b5008bdebf56f1e5d903e06e0b6ffe1f8eed78dbcd7ebb1a01e`). Here u>0 is its arbitrary upstream raw rate, the downstream raw rate is1 after normalizing d=1, and z is the actual squared pole ratio.

**Theorem.** For EVERY real `u>0`, EVERY `z>=389/500` and EVERY positive physical c, this EXACT chain's same-matrix coefficient equations cannot give a PH7 via a positive diagonal normalization with a nonnegative initial row. More precisely, whenever its literal initial coefficient `C>=0`, its last-to-center off-diagonal feedback must satisfy `phi<0`. The singular degree-four matching case `L=0` has no solution either. Every possible zero of the other input/feedback coefficients is retained; no q-Hurwitz, equal-physical-holding or selected-u assumption is needed.

Since `7/9<389/500<8/9`, the parent-supported strict continuation beyond7/9 remains consistent but the SAME free-u family cannot reach the explicit interval `[389/500,8/9]`. In particular the earlier actual family endpoint z_star from the parent must satisfy `7/9<z_star<389/500`, assuming its stated supported construction; that is a chart-specific upper bound, not a new bound on the true PH7 endpoint. The theorem also covers z>8/9 for this one family, independently of whether those parameters lie in the ultimate PH existence region.

## 2. Exact coefficient identities and the singular matching case

For general z, the published family's SIX-rate symmetric coefficients are

    a=3u+3,
    b=3u^2+9u+3,
    c3=u^3+9u^2+9u+1,
    e4=3u^3+9u^2+3u,
    h0=b+4a-a^2-6.

Again these local coefficient names a,b are NOT the original dimensional pole names. The full degree-four and degree-five actual characteristic matching gives

    L p=N,
    q=(a-4)p+h0-2z,
    w=p+4-a,
    C=q-up+u^2,
    phi=e4+c3*w-[(6+2z)q+(4+4z)p+(1+z)^2],
    L=3u^2-3u+1-2z,
    N=8u^3-9u^2+3u-4z.

All appear in ONE actual matrix; the original input row has raw first coordinate C and the last-to-center raw off-diagonal entry is phi. Positive diagonal similarity preserves their signs. In particular C>=0 and phi>=0 are NECESSARY, not freely chosen polynomial coefficients.

When L!=0, exact algebra gives

    C L=(u^2+4z)(u-1)^2+2z(2z-1).                 (C-id)

For z>1/2 the right side is strictly positive for EVERY real u. Thus C>=0 forces L>0. For0<u<=1,

    L=3u(u-1)+1-2z<0,

so any physical point also has u>1. No hidden quadratic q>0 premise is used here.

When L=0, matching requires N=0. Solving the L equation for z and substituting gives the exact identity

    N=(u-1)(8u^2-7u+2)     when 2z=3u^2-3u+1.

Under z>1/2 and u>0, L=0 implies u>1; both factors displayed are strictly positive. Hence N!=0 and the coefficient matching equation has NO solution p. This treats the entire singular boundary, rather than merely excluding division by zero.

## 3. A universal monotonicity identity for the feedback numerator

Define the polynomial `P(u,z)=-L phi` by clearing L using the exact matching equations. Direct symbolic expansion gives

    P=u^6-3u^5+3u^4-u^3
       +(6u^4-26u^3+30u^2-12u+2)z
       +(15u^2-27u+9)z^2+6z^3.                   (P-id)

For u=1+t, z>=1/2, differentiate at fixed u and write

    partial_z P(1+t,z)
      =t^2(6t^2-2t+1)
       +(30z-13)t^2+(6z-6)t+(18z^2-6z).          (D-id)

The first term is nonnegative for all real t, because `6t^2-2t+1>0`. For the remaining quadratic in t, its leading coefficient is positive (`30z-13>=2`). Its discriminant is strictly negative: put z=1/2+h, h>=0, and EXACT expansion gives

    -disc=2160h^3+1548h^2+312h+3>0.

Therefore the second quadratic is strictly positive for every real t, and

    partial_z P(u,z)>0 for EVERY real u and EVERY z>=1/2.   (MONO)

In particular, for u>=1 and z>=389/500, P(u,z)>=P(u,389/500). This is an all-variable inequality, not an observed monotonic trend from a finite solver run.

## 4. One exact base polynomial and a finite rational positivity certificate

At `z0=389/500`,

    P(u,z0)=[62500000u^6-187500000u^5+479250000u^4
             -1326750000u^3+2026203750u^2
             -1604916750u+614313857]/62500000.     (BASE)

For each k=0,...,7 consider the complete interval

    [1+k/16, 1+(k+1)/16].

Represent BASE on it in the Bernstein degree-6 basis. ALL seven coefficients on EACH interval are strictly positive. Their exact minimum on each interval, in order k=0,...,7, is

    27208441993941/32768000000000,
    332782156669/512000000000,
    15478323400941/32768000000000,
    2439759321/8000000000,
    5219194922941/32768000000000,
    26265477669/512000000000,
    69564559941/32768000000000,
    467999551/2048000000000.

A polynomial with positive Bernstein coefficients is strictly positive on the entire closed interval, since the basis functions are nonnegative and sum to1. The full exact coefficient lists, not just these minima, are in the certificate JSON identified below.

For the remaining half-line write u=3/2+t, t>=0. Exact expansion is

    P(3/2+t,z0)
      =1202491/31250000+(179139/125000)t+(377469/25000)t^2
        +(1239/50)t^3+(9459/500)t^4+6t^5+t^6>0.  (TAIL)

Thus BASE is positive for ALL u>=1. By(MONO), P(u,z)>0 for all u>=1,z>=z0. Any physical input C>=0 forces u>1 and L>0 by(C-id); hence

    phi=-P/L<0,

contradicting the physical off-diagonal sign. Together with the singular case, this proves the stated whole-half-line theorem.

## 5. Exact verification actually performed

Executed once after completing the checker:

    python3 frontier-20261028-chain-global-band-check.py
    sympy 1.14.0 all exact identity/sign assertions PASS
    Bernstein min 467999551/2048000000000
    positive tail coefficients
      1202491/31250000,179139/125000,377469/25000,1239/50,9459/500,6,1

The checker uses SymPy 1.14.0 for exact polynomial identities over Q and Python `fractions.Fraction` for all Bernstein and shifted-power coefficients. It verifies(C-id), the L=0 substitution, (P-id), (D-id), the negative-discriminant identity, ALL eight complete Bernstein coefficient lists and every tail coefficient. No floating-point/root/optimizer conclusion is needed for the theorem.

- Checker `frontier-20261028-chain-global-band-check.py`: **71LF/3420B**, SHA256 `ebe509b08c6feae787c4ebe02b24df232eeb580f53e7f263936e4e6a12c0b019`.
- Exact coefficient certificate `frontier-20261028-chain-global-band-certificate.json`: **111LF/3931B**, SHA256 `d25c862dcae45727c21e2ee3ba499bb45eed7e7175db3f53693ce35116098706`.

This is an exercised exact-algebra check, not Lean/kernel, external independent review, source priority or verification of ALL PH7 topologies. Reviewer should independently reconstruct the published-family coefficient matching, positive-similarity caller and the interval/tail certificate rather than accepting the script output by itself.

## 6. Genuinely broader families attempted, but not claimed excluded

I then actually explored three increasingly broader same-matrix families at the original `z=8/9`; these bounded searches are exploratory and DO NOT prove infeasibility:

1. `frontier-20261028-ph7-nonuniform-search.py` varies all six upstream/downstream chain rates; deterministic seeded vectorized search,512 population/1800 generations, reported best minimum physical coefficient `-0.3297307967964258`; no exact witness. Script SHA256 `50ebf35efdfd44f4d9b8debff8961213cefebcbbadcff69668db731d6a7d1608`; result JSON `1a75e1845e4177d891f71da7058a9b009c9530ae7e5720bd354bc14bb6fb01c3`.
2. `frontier-20261028-ph7-balanced-search.py` uses balanced linear/linear actual numerator factors, six independent chain rates and nine actual feedback variables. Twenty-four bounded SciPy least-squares starts returned best normalized coefficient residual `0.01185817810778078`; no exact rational witness. Script `ed750d8d4e4dd4071255068e438ff6cda8be81a3dfedb387f644172104d7939b`; JSON `58f00043338aacc302211008c132d9d358fac6f3e41648f0bd2122f583ae4583`.
3. `frontier-20261028-ph7-balanced-cyclic-search.py` further permits nontriangular 3x3 principal blocks with positive feedback arcs. Eight bounded starts returned best normalized residual `0.007847866007328678`; no exact witness. Script `d60219c6722d58a1f19a86a75480c6ef7e7ce755049f74dbb15fdeb51877a6da`; JSON `43b6c96e5a5f4dab9d15522dee837bf46ce2e5404f70915a60991d77fceed149`.

SciPy 1.17.1 and SymPy 1.14.0 were installed from cached wheels into the owner-local `frontier-20261028-localdeps` directory; no global environment was changed. Each search explicitly contains an exact-rational determinant/actual numerator/row/Metzler/Hurwitz verifier for a numerical candidate, but no numerical fit met its threshold, so **that witness-verification path was not exercised**. All stated decimal residuals are algorithmic observations, not proofs, uniform margins, PH counterexamples or acceptance.

## 7. What remains

The exact theorem rules out a wide, explicit ratio band only for the particular earlier `3+1+3` chain with its literal single-column feedback pattern, actual beta/gamma and positive diagonal normalization. It does NOT prove that every allowed A/B representation has that pattern, that no nontriangular/cyclic seven-state generator exists, or that the universal target is infeasible. The original8/9 minimum remains `{7,8}` at its separately retained upper/lower inputs. No global PH7/no-PH7 or full-function conclusion follows.

Prior held/quarantined outputs remain historical/unvalidated and were not used as accepted premises. Earlier source and process claims keep their actual scope; the present exact check does not cure any process finding or prove novelty. No scientific theory is promoted solely from an optimizer miss. Same exclusive owner root; no push/deletion/publication/secrets/unsolicited external model or infrastructure mutation. New science window ends2026-10-31T21:23:27Z.

**END — exact u-uniform exclusion for this supported construction on z>=389/500, not an unrestricted PH7 exclusion.**
