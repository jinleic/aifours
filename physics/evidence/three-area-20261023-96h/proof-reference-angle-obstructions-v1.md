# Reference-angle obstructions: Schmidt rank alone cannot characterize GS(eta)

Before-creation clock last observed: **2026-10-23T13:22:50-07:00**. Status: **CANDIDATE written derivation**, not an independently checked certificate. No scientific program, numeric approximation or new replay was performed. This directly addresses the parent's next-phase reference-ray classification question. The full W4 problem remains unchanged and NOT PROVED.

## 1. Exact question and result

On two ququarts let `Lambda_B=(Tr(.)I-./2)⊗(Tr(.)I-./2)`, and use the same co-Choi convention as the GSd proof. For a nonzero reference eta put

`A_eta=Lambda_B(|eta><eta|)>0`,

`L_i=Lambda_B(|i><eta|)`,

`M_eta(|i><j|)=L_i A_eta^(-1)L_j†`,

`C_B=Jhat(Lambda_B)`, `S_eta=Jhat(M_eta)`.

The symmetric domination question is `-C_B<=S_eta<=C_B`. This is scale-invariant in eta.

**Two explicit candidate obstructions:**

- For `eta3=|00>+|11>+(1/4)|22>` (Schmidt rank three), the fixed vector w defined below satisfies

  `<w,(C_B+S_eta3)w>=-58384/54689<0`.

- For `eta4=|00>+|11>+(1/4)|22>+(1/4)|33>` (Schmidt rank four), the same vector satisfies

  `<w,(C_B+S_eta4)w>=-74/289<0`.

Thus “Schmidt rank at least three”, “odd Schmidt rank”, and “full Schmidt rank” are not sufficient criteria for symmetric GS. In particular the already-proved uniform full-rank Omega_4 and eta4 have the **same Schmidt rank but different answers**. Any exact criterion must depend on the Schmidt coefficients, not only their count.

These are negative co-Choi quadratic forms, **not negative rank-two Werner witnesses**. The coefficient matrix of w has rank four.

## 2. A two-parameter reference family and a fixed test vector

Use the unnormalized reference

`eta=|00>+|11>+t|22>+u|33>`, t,u>=0.

Let

`a=1+t^2+u^2`,

`z=2/a+t^2/(2+u^2)+u^2/(2+t^2)`.

The test vector is

`p2=|0000>+|0011>+|1100>+|1111>`,

`q2=|0000>+|0110>+|1001>+|1111>`,

`w=p2+2q2`.

The four slots group the two-site input and output pairs. Only basis labels zero and one occur in w, but the reference and inverse below retain the two unused levels; they must not be discarded.

The exact claimed evaluation is

**(E)**

`<w,(C_B+S_eta)w>=[36+16z-(32+10z)/a-28/a^2]/(4+z)`.

Sections 3–4 derive it by hand. This gives a necessary GS condition on an actual two-parameter family, not a sufficient full classification.

## 3. The reference inverse and contractions

Write c=(1,1,t,u), `N=2+t^2+u^2`, and `D_(ab)=N-(c_a^2+c_b^2)/2`. Then

`A_eta=D+|eta><eta|/4`.

D is strictly positive for this family. Its entries on |00>,|11> and on the inside off-diagonal states |01>,|10> all equal a. Its entries on |22>,|33> are respectively `2+u^2`, `2+t^2`. Hence

`h=D^(-1)eta`, `<eta,D^(-1)eta>=z`,

`A_eta^(-1)=D^(-1)-|h><h|/(4+z)`.

For i=(a,b) with a,b in {0,1},

`L_ab=delta_(ab)I-(E_ab⊗I+I⊗E_ba)/2+|ab><eta|/4`.

Therefore for c,d in {0,1},

`L_ab†|cd>=delta_(ab)|cd>-(delta_(ac)|bd>+delta_(bd)|ca>)/2+delta_(ac)delta_(bd)eta/4`.

Every quantity needed by w is retained in these formulas. The outside components of eta enter through h and z, not through an illicit two-level truncation.

## 4. The three entries on span{p2,q2}

The co-Choi reversal gives

`S_((i,p),(j,q))=<L_j†p,A_eta^(-1)L_i†q>`.

Contracting the four input pairs in {00,01,10,11} yields the following exact quadratic-form entries:

`<p2,S_eta p2>=[z+(16+2z)/a-4/a^2]/(4+z)`,

`<p2,S_eta q2>=[z/2-(4+2z)/a-2/a^2]/(4+z)`,

`<q2,S_eta q2>=[z-(8+z)/a-4/a^2]/(4+z)`.

One reconstruction route is as follows. Put `Omega2=|00>+|11>`. For the p2 diagonal contraction,

`Σ_(b=0)^1 L_bb† Omega2=Omega2+eta/2`.

Its D-inverse norm is `4/a+z/4`, while its h inner product is `2/a+z/2`; the rank-one inverse formula gives the first entry. For the cross contraction, separating equal and unequal input labels gives

`2[-1/(a^2(4+z))]+[4/(a(4+z))]+[z/(2(4+z))]-2/a`,

which simplifies to the second entry. For the q2 diagonal contraction, the D-inverse contribution is `-2/a+z/4` and the subtracted h contribution is

`[4/a^2-z/a+z^2/4]/(4+z)`,

giving the third entry. These expansions use only the displayed L_ab† formula and Kronecker deltas.

The quadratic-form matrix of C_B on p2,q2 is `[[3,-3/2],[-3/2,3]]`. Thus `<w,C_B w>=9`. Adding the first S entry, four times its cross entry and four times its q2 diagonal entry gives

`<w,S_eta w>=[7z-(32+10z)/a-28/a^2]/(4+z)`.

This proves (E).

At t=u=0, (E) gives -2, matching the separate hand obstruction and the earlier exact assay's sign, although its LDL vector was different. No new execution was used to derive this evaluation.

## 5. Exact rank-three angle obstruction

Set u=0 and s=t^2. Then `a=1+s`, `z=2/(1+s)+s/2`. Formula (E) simplifies to

`<w,(C_B+S_eta)w>=2(8s^3+47s^2+75s-12)/[(s+1)(s^2+9s+12)]`.

The denominator is positive for s>=0. The numerator polynomial is strictly increasing there because its derivative is `24s^2+94s+75>0`. It has one positive zero; the witness is negative below that zero. This is an exact threshold for this **particular witness**, not a full GS characterization.

At t=1/4, s=1/16. The cubic numerator before the factor two is `-3649/512`; the denominator is `54689/4096`. Their ratio including the factor two is exactly

`-58384/54689`.

The three nonzero Schmidt coefficients are 1,1,1/4 before normalization, so this is a genuine rank-three reference obstruction, not the old rank-two ray with a zero coefficient renamed.

## 6. Exact full-rank angle obstruction

Set t=u and s=t^2. Here `a=1+2s`, `z=2/(1+2s)+2s/(2+s)`. Formula (E) becomes

`<w,(C_B+S_eta)w>=(2/3)(34s^3+65s^2+36s-3)/[(1+2s)(1+s)^2]`.

Again the denominator is positive and the numerator cubic is strictly increasing on s>=0, with derivative `102s^2+130s+36>0`. At s=1/16 its value before the factor 2/3 is `-999/2048`, while `(1+2s)(1+s)^2=2601/2048`. Consequently the full value is exactly

`-74/289`.

At t=u=1 the reference is the uniform Omega_4, and the same witness has positive value 22/3, consistently with the separate complete GS4 proof. The negative full-rank example and positive uniform full-rank theorem rule out a Schmidt-rank-only classification decisively.

## 7. Limits and next precise obligation

The vector w has coefficient matrix `|Omega2><Omega2|+2F_2` across input:output, with eigenvalues 4,2,2,-2 and hence rank four. It is not an allowed rank-at-most-two Werner coefficient operator. These obstructions therefore do not refute W4 or the reference-ray positivity theorem at any tested eta; they refute only the symmetric co-Choi route at the specified eta.

The parent-requested exact classification must now track Schmidt **angles**. A first complete positive obligation is the embedded rank-three uniform reference `Omega_3` in two ququarts: the old one-encoding assay is positive, but that is not a written proof. The scalar families above give necessary, not sufficient, boundary inequalities and must not be silently promoted to a complete criterion. The fully product theorem, GSd uniform theorem and all source/novelty gates retain their prior labels.
