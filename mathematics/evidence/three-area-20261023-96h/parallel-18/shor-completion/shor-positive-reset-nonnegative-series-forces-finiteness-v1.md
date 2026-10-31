# Shor positive reset route — coefficientwise nonnegativity FORCES finite termination

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 06:42:07 PDT 2026** (earlier observation bound). WRITTEN/unreviewed. Conventional symbolic proofs from existing inputs only; no invented parameter/control trial, withdrawn Taylor guidance, scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

This is a substantive strengthening of the positive reset-certificate packet, SHA256 `50ad08443b5d170cdb9c902d8cd907de4d92684e2b2e3bb46d03b259a8014048`. The earlier packet required finite M explicitly and conservatively retained termination as an additional obligation if M was defined by rational inversion. The theorem below shows that for FINITE positive R,T,H, proving coefficientwise nonnegativity of that inverse already forces termination. Earlier bytes remain unchanged; no actual positive inverse for the Shor data is supplied.

## 1. Literal finite boundary data, with the middle series NOT presumed finite

Let R,T,H be FINITE characteristic polynomials over{a,b}, with R(empty)=T(empty)=1 and H(empty)=0. Put K=1−a−b and DEFINE the formal rational series

    X=1−T(1−K H)^(-1)K R.                               (INV)

The inverse exists formally because KH has zero constant term. X has zero constant term automatically. Suppose every coefficient of X is NONNEGATIVE. No upper degree, word-length, b-count, arity, delay, order or support-finiteness assumption is made about X.

**Theorem.** X is necessarily a FINITE0/1 characteristic polynomial of a RAW UD factor-complete code. Consequently, finding finite R,T,H for which INV is coefficientwise nonnegative and contains the literal C would already settle the ORIGINAL positive Shor question, with no separate finite-termination or raw PR/STAB realization obligation.

## 2. Positive RESET first gives characteristic coefficients and UD

Rearranging INV in the formal ring gives

    (1−X)^(-1)=R^(-1) K^(-1)(1−K H)T^(-1),

hence

    K^(-1)=R(1−X)^(-1)T+H.                              (RESET)

All coefficients on the right are nonnegative because X is proper and nonnegative. R,T each contain the empty word. Thus every coefficient of(1−X)^(-1) is at most1. In particular X itself has coefficients0 or1, and two distinct lists of support words cannot concatenate to the same raw word. Let M=supp(X); M is RAW UD, at this point possibly infinite.

The finite outer supports and H imply factor-completeness just as before: pad any desired w by a^d on both sides for d greater than their maximum lengths. The padded word is too long to be an H-word; RESET gives an R/M*/T decomposition whose middle contains ALL of w. Thus the only issue left at this stage is whether M can be infinite. The next section rules that out.

## 3. Finite positive outer data leave NO possible positive real pole

Use a SINGLE length variable z to evaluate both a and b at z. Write finite nonnegative polynomials r(z),t(z),h(z) for R,T,H, and f(z) for X. INV gives the exact rational function

    f(z)=1−(1−2z)r(z)t(z)/[1−(1−2z)h(z)].               (LEN)

Because X has0/1 coefficients, [z^N]f is the number of its support words of length N and lies between0 and2^N. Therefore the series for f converges for every0<=z<1/2. In particular no positive pole of its reduced rational function occurs below1/2.

At z=1/2 the displayed denominator equals1. For EVERY real z>1/2 it equals

    1+(2z−1)h(z)>0,

using ONLY nonnegativity and finiteness of h. The numerator is polynomial as well. Hence f has NO positive real pole ANYWHERE.

### Elementary rational positive-pole lemma, reconstructed

A nonpolynomial rational function analytic at0 with nonnegative Taylor coefficients MUST have a positive real pole. Indeed choose a pole z0 of smallest modulus rho>0 and multiplicity pi. For0<=s<1, coefficient nonnegativity gives

    |f(s z0)| <= f(s rho).

The pole at z0 makes `(1−s)^pi |f(s z0)|` tend to a strictly positive finite limit. If rho were not a pole, f(s rho) would stay bounded and the same product on the right would tend to0, contradiction. Thus rho is a positive pole. This elementary argument is the operative part of Berstel–Reutenauer Chapter8 Lemma1.2, read in the author-hosted2010draft; the full stronger pole/root-of-unity classification is NOT used.

Applying the lemma to LEN contradicts the absence of positive real poles unless f is a POLYNOMIAL.

Since its coefficients count actual support words and are nonnegative, polynomial f means X has no word above its finite maximum degree. Thus M is FINITE. Sections2–3 prove the theorem without signed-factor necessity, PF, a sampling bound or a conjectural cancellation rule. ∎

## 4. Exact degree/count identity for a nonempty isolate language

Suppose H is nonempty, and let d_R,d_T,d_H be the maximum WORD LENGTHS in the three finite languages, with c_R,c_T,c_H the respective numbers of maximum-length words. They are positive integers. A nonnegative inverse X with nonempty proper M has maximum codeword length

    L=d_R+d_T−d_H >=1,                                 (DEG)

and its number of length-L codewords is

    c_M=c_R c_T/c_H.                                   (COUNT)

*Proof.* In LEN the denominator has degree d_H+1 with positive leading coefficient2c_H. The nonconstant product in the numerator has degree d_R+d_T+1 and leading coefficient−2c_R c_T. Since1−f is polynomial and nonconstant, exact rational cancellation makes its degree the difference d_R+d_T−d_H, with leading coefficient−c_R c_T/c_H. Subtracting from1 gives DEG and COUNT. A degree difference0 or negative would make f constant; X has zero constant and a nonempty support, so that cannot occur. ∎

This is a necessary FULL actual-length identity, not a selected small-word ansatz. In particular c_H divides c_R c_T. If H is empty, the separate formula is L=d_R+d_T+1. The preceding marker packet proves H cannot be empty for any Shor completion; that argument uses the sixteen fixed one-b words, not a new numeric/control trial.

## 5. Updated exact original feasibility problem

The positive direction can now be phrased using ONLY FINITE positive R,T,H:

- they have the stated empty-word coefficients;
- the formal inverse INV has NONNEGATIVE coefficients at EVERY raw word;
- every literal word of C has coefficient at least1 in INV.

The theorem then supplies characteristic coefficients, RAW UD, ALL-word factor-completeness AND finite support automatically. Conversely every actual finite completion supplies such finite boundary data by the raw marker theorem. Thus this is a self-contained necessary-and-sufficient representation of the ORIGINAL problem, independent of I3/I4/I5.

The remaining obstruction is genuinely **coefficientwise nonnegativity of a noncommutative rational inverse**, not a separate polynomial-termination hypothesis. Nonnegativity of only its scalar evaluations, total-length coefficients or selected finitely many coefficients is NOT enough. No data R,T,H satisfying the Shor inclusion and that whole noncommutative condition are supplied; no all-data impossibility theorem is proved.

This strengthens the prior representation rather than reasserting a small period. All orders, arities, b-counts, raw gaps and delays remain unbounded. H* remains FALSE/WITHDRAWN; no commutative-prefix/factorization conjecture or residue stabilization is assumed. Original Shor completion is **NOT_PROVED** in either direction.

Own permanent v109-A exactness MAJOR and NEW v34 written-scope MAJOR/all earlier histories remain uncured. Entire withdrawn Taylor/control packet is ZERO-credit/nonpremise and is neither repeated nor repaired here. No source/shared/frozen edit, git/deletion/publication, new scientific GO, formal/kernel/human/configured-family/executable/novelty acceptance or early final park. Same original cutoff and deadline.
