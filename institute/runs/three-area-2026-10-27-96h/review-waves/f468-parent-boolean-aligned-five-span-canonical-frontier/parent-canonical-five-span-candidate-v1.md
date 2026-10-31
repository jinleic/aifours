# Parent GENERAL-AUTHOR candidate: canonical five-span Boolean graph and local ternary lifts

**Status:** Fresh parent-authored candidate, with parent finite execution; NOT independently reviewed or adopted. The five-span normalized necessity is imported from the separately adopted actual m116 dichotomy, not assumed for all residual branches. The canonical pair classification and local lifts below are new, at the stated scope. They do not establish the original actual balanced NL242 caller, any U/V complement, or a global target result.

## 1. Frozen actual-caller import and normalization

Use the shared actual object and hypotheses in [the adopted dichotomy](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-actual-m116-a2-xor-alignment-and-five-six-span-dichotomy-parent-v1.md): \(u:R\times Q\to\{-1,0,1\}\), \(R=\mathbb F_2^6\), \(Q=\mathbb F_2^2\), \(U_s(c)=\sum_wu(c,w)\chi_s(w)\), \(a=U_1/3\), \(g=U_2\), \(|S|=16\), \(S=\operatorname{supp}a\), \(|\widehat a|=4\), and \(|\widehat g|=4\) on the named four-element set \(A\) and 12 elsewhere. Restrict to the five-span branch, not the six-span branches. The inherited normalization uses an invertible linear coordinate change, translation and a common character/global-sign modulation of the actual \(u\); it preserves the two-fibre hypotheses used here but need not preserve the original balance condition.

Write \(c=(h,d)\), \(h,d\in\mathbb F_2^3\). In the inherited normalization \(A=\{0,1,2,4\}\) in the dual \(d\)-coordinate, all four small signs are positive, \(E=\{d=0\}\), \(B=\{d=1,2,4,7\}\), \(S\subset B\), and each of the four \(B\)-cosets contains four \(S\)-points. Here integers denote the corresponding three-bit vectors. The two full \(|g|=4\) blocks lie in \(E\); a translation and \(GL(3,2)\) change on \(h\) alone send them to \(h=0,1\), while leaving all \(d\)-frequencies and their small signs unchanged. Thus

\[
g(h,0)=\begin{cases}4&h=0,1,\\-2&\text{otherwise},\end{cases}\qquad
g(h,d_b)=\rho_b(-2+3\mathbf 1_S(h,d_b)),
\]
where \((d_0,d_1,d_2,d_3)=(1,2,4,7)\), \(\rho=(-1,-1,-1,+1)\), and \(g=0\) elsewhere. This follows from the imported saturated five-coset signs, not an independent choice of \(g\).

## 2. Every support slice is an exact transversal

Let \(G_d(y)=\sum_h g(h,d)(-1)^{y\cdot h}\). For nonzero \(y\) with \(y\cdot1=0\), the full-block pair gives \(G_0(y)=12\). Every one of the eight full coefficients \(\widehat g(y,z)\) has magnitude 12. Their average over \(z\) is 12, so all are +12 and inverse Fourier transform gives \(G_d(y)=0\) for every \(d\ne0\).

For \(d=d_b\), the constant term in \(g\) has zero nontrivial \(h\)-transform, so all three nonzero transforms on \(1^\perp\) of \(\mathbf 1_{S\cap\{d_b\}}\) vanish. Fourier inversion on \(\mathbb F_2^3/\langle1\rangle\), combined with the inherited cardinality four, says that every pair \(\{2j,2j+1\}\), \(j\in\mathbb F_2^2\), contains exactly one support point. Hence a single 16-bit truth function \(f(j,b)\) parametrizes the entire support:

\[
S=\{(2j+f(j,b),d_b):j,b\in\mathbb F_2^2\}.
\]
This is a necessity for every normalized actual five-span caller, not a choice of four unrelated slices.

## 3. Exact two-fibre Fourier equivalences

Write \(b=(b_0,b_1)\), \(d_b=1+3b_0+5b_1\) in binary-vector XOR, and \(q(b)=1+b_0b_1\). Then \(\rho_b=(-1)^{q(b)}\). For \(y\cdot1=1\), write \(y=1+2v\), \(v\in\mathbb F_2^2\). The \(E\) contribution vanishes, and the actual full transform equals

\[
\widehat g(y,z)=3(-1)^{z\cdot1}\sum_{j,b}(-1)^{f(j,b)+q(b)+v\cdot j+w(z)\cdot b},
\quad w(z)=(z\cdot3,z\cdot5).
\]
As \(z\) ranges over \(\mathbb F_2^3\), \(w(z)\) covers every two-bit frequency. At \(y=0\), the predetermined values give the four +4 small coefficients and four -12 coefficients. At nonzero \(y\perp1\), the preceding saturation gives all +12. Therefore the **entire** actual \(g\)-spectrum has its required \(4/12\) magnitudes if and only if the four-variable Boolean function \(f+q\) is bent: all sixteen unnormalized Walsh coefficients have magnitude four.

For \(a\), write \(a(2j+f(j,b),d_b)=(-1)^{r(j,b)}\). The eight \(h\)-frequency rows split by \(y\cdot1\). Even rows are the four-variable Walsh transform of \(r\); odd rows are that of \(r+f\), each multiplied by a character sign. Hence

\[
|\widehat a|\equiv4\quad\Longleftrightarrow\quad r\text{ and }r+f\text{ are both bent.}
\]
The same \(f\) and \(r\) occur throughout, so this is a common-phase condition, not independent spectra.

## 4. Exact finite classification, parent-observed

The parent froze the [prospective plan](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f468-parent-boolean-aligned-five-span-canonical-frontier/prospective-author-plan-v1.json) before the full [source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f468-parent-boolean-aligned-five-span-canonical-frontier/canonical-five-span-graph-assay-v1.py) and [GO](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f468-parent-boolean-aligned-five-span-canonical-frontier/parent-canonical-graph-assay-go-v1.json). The one-shot parent execution and exact stdout/stderr are bound by the [run receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f468-parent-boolean-aligned-five-span-canonical-frontier/parent-canonical-graph-assay-v1-receipt.json); exit 0, elapsed 2.53 seconds, empty stderr. The program has no filesystem/network/child-process science input.

It exhausts all 65,536 truth functions \(f\), computes every actual 64-position \(g\)-transform, and checks the bent-offset equivalence against the independent 16-position transform. It enumerates all 896 four-variable bent functions and all 802,816 ordered bent-phase pairs. For all surviving graphs the ANF has degree at most two, and its alternating quadratic polar form has rank two or four. The observed exact census is:

| Canonical graph property | Count |
|---|---:|
| All 16-bit graph supports | 65,536 |
| Required \(g\) spectrum, equivalently \(f+q\) bent | 896 |
| Of those admitting at least one common flat \(a\) phase | 896 |
| Rank-two \(f\) polar form | 512 |
| Rank-four \(f\) polar form | 384 |
| Allowed \(r\) phases for each surviving \(f\) | 384 |

Thus there are exactly 344,064 canonical \((f,r)\) pairs at this two-fibre level. For one deliberately chosen non-bent \(f\), the program independently tests every one of the 65,536 candidate phases by a full 64-position \(a\)-transform and confirms the same 384 phases. Four intended controls alter a full block, a \(B\)-sign, a shared phase, or the required bent offset; all were rejected in the actual run. The exact source and output, not these prose counts alone, are the finite evidence. The parent both authored and executed it; it is not an independent checker or a kernel proof.

The finite ANF census proves each surviving \(f\) is quadratic and non-affine at this canonical, exhaustive finite scope. Consequently its graph spans dimension exactly five: it lies in the known affine five-flat \(B\), and an affine four-flat graph would make \(f\) affine. These facts exclude all other graph shapes within the normalized five-span branch, not the six-span branch.

## 5. Each pair has an actual ternary local lift with 116 nonzeros

This is a new written construction, not a run output or an original global witness. On each support point choose one \(w_0\) satisfying \(\chi_1(w_0)\chi_2(w_0)=-g/a\), set \(u(w)=a\chi_1(w)\) for \(w\ne w_0\), and set \(u(w_0)=0\). Then the block has support three and gives \(U_1=3a\), \(U_2=g\). Exactly two choices of \(w_0\) exist.

On the two full \(E\)-blocks set \(u=(g/4)\chi_2\). On each of the other 22 nonzero \(g\)-blocks off \(S\), choose one \(w\) from each \(\chi_1\chi_2\)-sign class and set \(u=(g/2)\chi_2\) on those two points and zero elsewhere. These give \(U_1=0,U_2=g\). The support count is \(16\cdot3+2\cdot4+22\cdot2=100\).

On any eight of the 24 \(g=0\), \(a=0\) blocks, add two equal nonzero signs at \(w\) and \(w+(1,1)\); both \(U_1\) and \(U_2\) remain zero. This adds 16 nonzeros, giving an actual ternary \(u\) with support 116 and the prescribed complete \(U_1,U_2\) spectra. The other 16 zero blocks remain zero. All off-\(S\) blocks of support two have \(|U_0|\le2\), and the full blocks are \(\pm\chi_2\), with \(U_0=0\); thus the adopted **local** \(H\), the number of \(U_1=0\) blocks with a single \(|U_0|=4\) peak, is zero. These objects are called **local lifts**, not actual original-target callers: no global \(U_0,U_3\) Walsh spectrum, original balance, full rank/eight-zero/T constraints, complementary \(V\), or odd-fibre cap is proved.

## 6. Remaining obligations and provenance

The local-lift construction and classification need independent written checking, plus a separately authored finite physical-block replay. The planned and actual finite assay precede this manuscript; parent reasoning about the transversal/bent equivalence was already recorded in the frozen plan before execution, so this is not a blinded derivation. The local-lift extension was developed after the assay and was not tested by that assay. No source-body from a quarantined episode or consumer was used. All old f439/f444/f448 and other held episodes remain HELD/ZERO/NONINPUT.

Remaining for the actual named five-span caller: simultaneous \(U_0,U_3\) requirements, original balance, named rank/eight-zero and \(T\ne0\), all remaining four-fibre conditions, a common physical complementary 140-support \(V\), and its global odd Walsh caps. The two six-span classes, other m116/m114 callers, and the full balanced NL242 question remain open. No source equivalence, novelty, independent-family/human/kernel acceptance, or full exclusion is claimed.
