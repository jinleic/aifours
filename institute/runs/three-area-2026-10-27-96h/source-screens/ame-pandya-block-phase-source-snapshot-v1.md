# Public primary-source excerpt

Source: https://arxiv.org/html/2610.16673v1
Rendered source lines: 147-196
Purpose: Lemma1 1x1/2x2 moduli and complex-phase separation, not original t24 exclusion
This is a bounded text excerpt, not an assertion about all versions, priority or complete-paper coverage.


An irredundant orthogonal array of index 11 gives an AME state as the uniform superposition of its rows [[26](#bib.bib26)].
With index 22 the phases must also cancel. In each of the three reshapings, the rows and the columns are labeled by the
indices of two complementary pairs of parties, so strength 22 and index 22 mean that every row and every column has exactly two non-zero entries.
Moreover, two rows that share a column share both of their columns, so after permuting rows and columns each reshaping
is a direct sum of 1818 full 2×22\times 2 blocks [[23](#bib.bib23)]: the 1212 blocks of EE (the *EE-blocks*) from the
proof of Proposition [1](#Thmproposition1 "Proposition 1. ‣ II A real AME(4,6) state ‣ Euler’s thirty-six officers need not all be entangled:real AME(4,6), families and classification"), and six *mixed* blocks with two states of PP on one diagonal and two of P′P^{\prime} on the other. Over the three reshapings this gives 3636 EE-blocks and 1818 mixed blocks. A
block-diagonal matrix is unitary if and only if each of its blocks is, and for a 2×22\times 2 block this amounts to
linear equations in the squared moduli and a single linear congruence in the phases: on such a support the AME
conditions linearize. On the support E∪PE\cup P of |ψ⟩\ket{\psi} the six mixed blocks split into 1212 blocks of size 1×11\times 1, and the proof of Proposition [1](#Thmproposition1 "Proposition 1. ‣ II A real AME(4,6) state ‣ Euler’s thirty-six officers need not all be entangled:real AME(4,6), families and classification") is this argument. Allowing both kinds of blocks gives the
following lemma.

###### Lemma 1.

Let |Φ⟩=∑x∈SΦx​|x⟩\ket{\Phi}=\sum_{x\in S}\Phi_{x}\ket{x} with Φx=sx/72​ei​φx\Phi_{x}=\sqrt{s_{x}/72}\\,e^{i\varphi_{x}}, where sx>0s_{x}>0 and φx∈ℝ\varphi_{x}\in\mathbb{R}. In each of the three reshapings UU, URU^{R}, UΓU^{\Gamma} of 6​|Φ⟩6\ket{\Phi}, along 12|3412|34, 13|2413|24 and 14|2314|23, the basis state |x⟩\ket{x} lies in the row labeled by its indices for the first pair of parties and
in the column labeled by those for the second. For x∈Sx\in S in row rr and column cc we write sr​c=sxs_{rc}=s_{x} and φr​c=φx\varphi_{rc}=\varphi_{x}. Suppose that in each reshaping the 3636 rows and the 3636 columns can be partitioned into
sets R1,…,RmR_{1},\dots,R_{m} and C1,…,CmC_{1},\dots,C_{m} with |Rk|=|Ck|∈{1,2}|R_{k}|=|C_{k}|\in\\{1,2\\} such that SS consists exactly of the basis
states in R1×C1,…,Rm×CmR_{1}\times C_{1},\dots,R_{m}\times C_{m}, the *blocks* of SS. Then |Φ⟩\ket{\Phi} is AME if and only if sx=2s_{x}=2 on every 1×11\times 1 block and every 2×22\times 2 block, with rows r,r′r,r^{\prime} and columns c,c′c,c^{\prime}, satisfies

|  | sr​c=sr′​c′,sr​c′=sr′​c,sr​c+sr​c′=2,φr​c−φr​c′−φr′​c+φr′​c′≡π(mod2​π).\begin{gathered}s_{rc}=s_{r^{\prime}c^{\prime}},\quad s_{rc^{\prime}}=s_{r^{\prime}c},\quad s_{rc}+s_{rc^{\prime}}=2,\\\\ \varphi_{rc}-\varphi_{rc^{\prime}}-\varphi_{r^{\prime}c}+\varphi_{r^{\prime}c^{\prime}}\equiv\pi\pmod{2\pi}.\end{gathered} |  | (2) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

In particular, if these moduli equations have a solution with all sx>0s_{x}>0, a real AME state with support SS exists
if and only if the equations tr​c+tr​c′+tr′​c+tr′​c′=1t_{rc}+t_{rc^{\prime}}+t_{r^{\prime}c}+t_{r^{\prime}c^{\prime}}=1, one for each 2×22\times 2 block, have a solution t∈𝔽2St\in\mathbb{F}_{2}^{S}.

###### Proof.

The reduced state of parties 1,21,2 is ρ12=U​U†/36\rho_{12}=UU^{\dagger}/36, and that of parties 3,43,4 is ρ34=U†​U¯/36\rho_{34}=\overline{U^{\dagger}U}/36, and URU^{R} and UΓU^{\Gamma} give ρ13,ρ24\rho_{13},\rho_{24} and ρ14,ρ23\rho_{14},\rho_{23} in
the same way. Hence |Φ⟩\ket{\Phi} is AME, i.e. all six
two-party reductions equal 𝕀/36\mathbb{I}/36 (which includes ⟨Φ|Φ⟩=1\innerproduct{\Phi}{\Phi}=1), if and only if UU, URU^{R} and UΓU^{\Gamma} are unitary.

Fix one reshaping UU and its blocks. The entry of UU in row rr and column cc is sr​c/2​ei​φr​c\sqrt{s_{rc}/2}\\,e^{i\varphi_{rc}} if the basis state there lies in SS, and 00 otherwise. Since the RkR_{k} and the CkC_{k} partition the rows and the
columns and all entries of SS lie in the blocks Rk×CkR_{k}\times C_{k}, ordering the rows as R1,…,RmR_{1},\dots,R_{m} and the columns
as C1,…,CmC_{1},\dots,C_{m} makes UU block diagonal, with diagonal blocks BkB_{k} the submatrices on Rk×CkR_{k}\times C_{k}. So UU is unitary if and only if every BkB_{k} is. A 1×11\times 1 block is unitary if and
only if sx/2=1s_{x}/2=1. A 2×22\times 2 block BB with rows r,r′r,r^{\prime} and columns c,c′c,c^{\prime} is unitary if and only if its rows are
orthonormal:

|  | sr​c+sr​c′=sr′​c+sr′​c′=2,Br​c​B¯r′​c+Br​c′​B¯r′​c′=0.s_{rc}+s_{rc^{\prime}}=s_{r^{\prime}c}+s_{r^{\prime}c^{\prime}}=2,\qquad B_{rc}\bar{B}_{r^{\prime}c}+B_{rc^{\prime}}\bar{B}_{r^{\prime}c^{\prime}}=0. |  |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |

Then B†​B=𝕀B^{\dagger}B=\mathbb{I} as well, so also sr​c+sr′​c=sr​c′+sr′​c′=2s_{rc}+s_{r^{\prime}c}=s_{rc^{\prime}}+s_{r^{\prime}c^{\prime}}=2. These four norm equations are
equivalent to the three moduli equations in ([2](#S3.E2 "In Lemma 1. ‣ III Symmetry and linearization ‣ Euler’s thirty-six officers need not all be entangled:real AME(4,6), families and classification")). Under them, the two terms of the orthogonality
condition have the same modulus sr​c​sr​c′/2>0\sqrt{s_{rc}s_{rc^{\prime}}}/2>0, so their sum vanishes if and only if their phases φr​c−φr′​c\varphi_{rc}-\varphi_{r^{\prime}c} and φr​c′−φr′​c′\varphi_{rc^{\prime}}-\varphi_{r^{\prime}c^{\prime}} differ by π\pi modulo 2​π2\pi, which is the congruence.
Conversely, the moduli equations and the congruence give orthonormal rows. So BB is unitary if and only if
Eq. ([2](#S3.E2 "In Lemma 1. ‣ III Symmetry and linearization ‣ Euler’s thirty-six officers need not all be entangled:real AME(4,6), families and classification")) holds. Exchanging rr with r′r^{\prime}, or cc with c′c^{\prime}, gives an equivalent system, so the
labeling within a block does not matter. Collecting the conditions of all blocks of the three reshapings proves the
first claim.

The moduli equations involve only ss and the congruences only φ\varphi, so any positive solution ss and any
solution φ\varphi together give an AME state with support SS, and every such state arises in this way. It is real
if and only if all φx∈{0,π}\varphi_{x}\in\\{0,\pi\\}. Writing φx=π​tx\varphi_{x}=\pi t_{x} with tx∈{0,1}t_{x}\in\\{0,1\\}, the congruence becomes tr​c−tr​c′−tr′​c+tr′​c′≡1(mod2)t_{rc}-t_{rc^{\prime}}-t_{r^{\prime}c}+t_{r^{\prime}c^{\prime}}\equiv 1\pmod{2}, which is the stated equation over 𝔽2\mathbb{F}_{2}.
∎

## IV Two families through the real state

[351 more lines in URL output. Use :200 to continue]
