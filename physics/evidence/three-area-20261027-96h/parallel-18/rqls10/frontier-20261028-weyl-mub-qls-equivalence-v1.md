# A circulant 1-RQLS(10) is equivalent to one vector unbiased to a Weyl MUB triple

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: **Wed Oct 28 18:49:25 PDT 2026**. This is an exact, restricted construction/reduction with a substantial consequence if the required vector exists. No such vector or 1-RQLS witness has been found; the claim is NOT an equivalence for all 1-RQLSs.

## 1. Main equivalence and original-vector construction

Let `zeta=exp(2*pi*i/10)`, `xi=exp(2*pi*i/20)`, `Z|t>=zeta^t|t>`, `X|t>=|t+1 mod10>`, and `D|t>=xi^(t²)|t>`. Let F be the normalized Fourier matrix with entries `zeta^(t b)/sqrt(10)`. Consider the three eigenbases

`B_Z=I`, `B_X=F`, `B_ZX=D F`.

They are mutually unbiased (§2). The following are equivalent for a unit vector phi:

1. phi is unbiased to EVERY vector of these three bases;
2. the 100 actual unit vectors `psi_(r,c)=Z^r X^c phi` have row/column ONBs and the diagonal `psi_(c,c)` is an ONB.

Whenever these hold, all 100 rays are automatically DISTINCT (§4), and shifting the diagonal by r gives ten disjoint transversal ONBs. Thus ANY exact phi satisfying (1) would solve the ORIGINAL 100-ray 1-resolvable QLS10 problem, with explicit vectors and resolution. Its ten translates `{X^c phi}` would also form a FOURTH MUB for this fixed triple (§3).

Conversely, the equivalence concerns this precise **Weyl orbit with the diagonal transversal**. An arbitrary QLS10, or even a Weyl orbit with a non-diagonal transversal, is not asserted to have this form.

## 2. The three bases and cyclic correlations

Because `xi^((t+10)²)=xi^(t²)`, D is well defined modulo10. A direct computation gives

`D X D† = xi^(-1) Z X`.                                         (1)

Thus DF diagonalizes ZX (up to an irrelevant common eigenvalue). I diagonalizes Z and F diagonalizes X. I,F and DF are all flat relative to I. F and DF are mutually unbiased as well: the chirp `d_t=xi^(t²)` has cyclic autocorrelation

`sum_t conjugate(d_t) d_(t+k)=xi^(k²) sum_t zeta^(k t)=0` for k!=0.

Consequently every discrete Fourier transform coefficient of d has modulus sqrt(10), so every entry of `F† D F` has modulus 1/sqrt(10).

For a unitary W with ten distinct eigenvalues in a cyclic progression, the orbit `{W^j phi:j=0,...,9}` is an ONB iff all nontrivial moments `<phi,W^k phi>` vanish, iff the ten eigenbasis probabilities of phi are all1/10. Apply this to Z, X, and ZX. The diagonal orbit `Z^c X^c phi` differs from `(ZX)^c phi` by a cell phase only. This proves the equivalence in §1. If one diagonal is an ONB, its ten common-unitary Z shifts partition the grid into ten ONB transversals.

## 3. A fourth MUB follows, not just one unbiased vector

Under (1), the translates `X^c phi` are an ONB. Each translation X^c permutes each of the three Weyl eigenbases up to phases: conjugating Z or ZX by X changes it only by a scalar, and X commutes with itself. Thus every `X^c phi` is also unbiased to each basis in the triple. They form an entire FOURTH MUB. Conversely, a circulant fourth MUB of this form includes phi unbiased to the triple.

This is a useful difficulty warning, not an imported no-go theorem: Prat Colomer et al. report numerical evidence suggesting at most three MUBs in dimension10, not a proof: https://arxiv.org/abs/2203.09429. We do not infer that a fourth cannot exist and do not claim current novelty or complete status from that numerical abstract.

## 4. Why all 100 Weyl-orbit rays are distinct

Assume (1), and suppose two orbit vectors were parallel. Cancelling them would make phi an eigenvector of a nontrivial Weyl displacement `W=Z^m X^k`, `(m,k)!=(0,0)` mod10.

**Case A: at least one of m,k is odd.** Up to a phase, W^5 is one of `Z^5`, `X^5`, or `Z^5 X^5` (the latter is a phase times `(ZX)^5`). Being an eigenvector of W makes the corresponding expectation have modulus1. But unbiasedness to the respective Z, X or ZX eigenbasis makes that nontrivial fifth moment ZERO. Contradiction.

**Case B: m,k both even.** Identify `Z10` with `Z2×Z5` via `t=5a+6b mod10`. Then W is `I_2 tensor W5` up to a scalar, where W5 is a NONTRIVIAL order-five Weyl displacement. Its five eigenvalues are distinct: a nonzero diagonal power has five distinct phases, while any nonzero shift power is a single 5-cycle with five distinct eigenvalues. Therefore any W eigenvector is a product `u_2 tensor v_5`.

Under the same CRT relabelling the three bases factor into the qubit Z, X and Y bases times 5-dimensional bases. Explicitly, if `omega=exp(2*pi*i/5)`,

`F10 = F2 tensor F5^(3)` up to coordinate labels, where `F5^(3)_(b,d)=omega^(3bd)/sqrt(5)`,
`D10 = diag(1,i) tensor diag(omega^(4b²))`.

If a product vector is unbiased to each product basis, summing the ten equal joint probabilities over the five-dimensional outcomes makes its qubit factor unbiased to all three qubit Z, X and Y bases. No pure qubit has that property: Z-unbiased implies `(1,exp(i theta))/sqrt(2)`, X-unbiased then gives cos(theta)=0, and Y-unbiased gives sin(theta)=0. Contradiction.

All nontrivial stabilizers are therefore excluded. This establishes 100 DISTINCT actual rays, rather than merely a nonuniform Gram or an unverified genericity assertion.

Exact integer `frontier-20261028-weyl-mub-crt-check-v1.py`, SHA **cc8e84d4c52c080058f97c6fd83b8e5e687f8facddbad58d5e2326b99ebe830f**, verifies the 100 Fourier CRT exponent identities, ten chirp identities, and the partition of the99 nonzero Weyl labels into75 odd-parity and24 nonzero even-parity labels. The algebraic MUB and eigenspace reasoning above is written mathematics, not a consequence of this finite arithmetic check alone.

## 5. Equivalent circulant Hadamard pair, and actual search status

Let `f_t=sqrt(10)*phi_t` be unit phases, and H the circulant normalized matrix `H_(t,c)=f_(t-c)/sqrt(10)`. From (1), H is Hadamard, `J=H∘F_unnormalized` is Hadamard, and the character quotient tests of the prior exact caller all pass automatically by §4. Indeed

`zeta^(t c)=d_t d_c conjugate(d_(t-c))`,

so `J=D C(f*conjugate(d)) D`; its unitarity is exactly unbiasedness to DF. This connects the current reduction to the arbitrary-H/H∘F caller without assuming every candidate H is circulant.

A bounded continuous search over only circulant phases (`frontier-20261028-circulant-hadamard-pair-search-v1.py` SHA **7e379f31c12ddcb11b319b861dc9086187305b25af149c94064b6112a59ffb12**) used 200 deterministic restarts, each at most4000 Adam steps. Result JSON SHA **ff510e39871644cd6591acdf246ae155702d3bf9ab903c0bbee850c16aaff065** records best loss approximately **2.44991083220506**, worst errors approximately **0.17067723** in both matrices. No candidate satisfied the 1e-10 threshold. A separate 30-second q10-circulant Z3 search returned **UNKNOWN timeout**, record SHA **fd7e97e760b71767501ac44c1a623d7de6be01d2a358d84cb6cb70743055cab0**. Neither failure is a no-go, a global lower bound, or evidence that the needed phi cannot exist.

## 6. Remaining gap

A single exact common unbiased vector for this fixed MUB triple would finish the original target and produce a fourth MUB; no such vector has been delivered. More general noncirculant product H, different transversals, nonproduct QLSs, and general 100-ray 1-RQLSs remain outside this equivalence. Independent review and novelty clearance are pending.
