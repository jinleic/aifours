# CONFERENCE-GLUING symmetry addendum v1 — arbitrary phases in the natural cyclic survivor

Observed before creation: **2026-10-23T14:37:27-07:00**. PhysicsRQLS10. Read with `candidate-CONFERENCE-GLUING-v1.md` (SHA256 `15da67c0b9241ac6b5f4128305f023d5efe82e53728fcde2829189e235516995`). Immutable additional candidate, not an edit or retroactive claim about that manuscript.

**CANDIDATE WRITTEN PARTIAL.** The earlier full-matrix mod7 test was inconclusive for cyclic10's zero matching `rho` of cycle type `1+2+2+2+2`. This addendum closes the **symmetry-preserving conference-seed** subcase while allowing **every complex compatibility phase**, without enumerating relative permutations or discretizing phases. No unrestricted cyclic10/H0/QLS10 impossibility is claimed.

## 1. Retained precise setup

Use C, C'=PCP^T, rho, and the fixed coefficient matrix

    M_(i,t)=conjugate(C_(t,i)) C'_(t,rho(i))

from the main manuscript. A genuine phase gluing requires `M delta=0` with all |delta_t|=1. C and C' are the specified Et-Taoui order9 cores; the relative permutation P is arbitrary subject to the additional explicit hypothesis below. All diagonal phases in the actual third basis remain arbitrary and need not respect a symmetry.

**Additional unphased-core hypothesis S:** rho is a simultaneous automorphism of C and C', meaning

    C_(rho(t),rho(i))=C_(t,i),
    C'_(rho(t),rho(i))=C'_(t,i)

for every t,i. This is a property of the stripped conference cores only. It does **not** assume any global covariance of the QLS vectors or any invariance of delta.

Then M commutes with the permutation action of rho: substituting rho(i),rho(t) in its definition and using both displayed identities gives

    M_(rho(i),rho(t))=M_(i,t).

## 2. The invariant-subspace mod7 test

Let F_rho be the coordinate space of vectors constant on each cycle of rho. Both M and its reduction `N=J-I-P_rho+Fix(rho)` preserve F_rho. The cycle-indicator basis is defined over Z, so the restricted M matrix has coefficients in the same ring `Z[1/2,i sqrt7]`. Reduction of that restricted matrix is exactly the restriction of N in the cycle-indicator basis; no averaging denominator is introduced in this reduction.

### Lemma FIX

Let f be the number of fixed points of rho. If f is nonzero modulo7, the restriction of N to F_rho is invertible over F7.

**Proof.** Let x be constant on cycles and set `S=sum_t x_t` in F7. For a fixed point a,

    (Nx)_a=S-x_a.

For any coordinate i on a nontrivial cycle, `x_(rho(i))=x_i`, so

    (Nx)_i=S-2x_i.

Thus Nx=0 forces x_a=S on fixed points and x_i=S/2 on the other coordinates. Summing all nine coordinates yields

    S=fS+(9-f)S/2,
    0=(7+f)S/2=fS/2  in F7.

If f is nonzero modulo7, S=0 and then every coordinate vanishes. The restricted operator is square, so it is invertible. QED.

As in the main manuscript, a nonzero reduced determinant implies a nonzero determinant over C. Therefore, under the lemma's hypothesis,

    ker(M) intersection F_rho={0}.                         (F)

## 3. Why arbitrary, non-invariant phase vectors are still excluded

### Theorem CGLUE-SYM

Under the retained setup and S, if rho has at least one fixed point and its number f of fixed points is not divisible by7, **no unimodular complex phase vector delta can satisfy M delta=0**.

**Proof.** Let L be the finite order of rho and average any putative complex kernel vector over its permutation action:

    delta_bar=(1/L) sum_(k=0)^(L-1) P_rho^k delta.

M commutes with P_rho by S, so M delta_bar=0. The average belongs to F_rho, hence is zero by (F). At a fixed coordinate a, averaging leaves the coordinate unchanged: `delta_bar_a=delta_a`. Therefore delta_a=0 at every fixed point. This contradicts |delta_a|=1.

Averaging here is over C, where 1/L exists. The mod7 determinant argument was applied separately to a cycle-indicator basis, so it does not require L to be invertible modulo7. No number-field assumption was placed on delta. QED.

This proves an obstruction even when M itself is singular: kernel vectors may survive in nontrivial rho-eigenspaces, but their fixed-point coordinates must vanish. Such vectors cannot be compatibility phases. This is not promoting a singular reduction to a no-go without a bridge; the bridge is the explicit invariant-subspace and averaging argument.

## 4. Actual cyclic10 conference-seed consequence

Cyclic10's zero-matching permutation has one fixed point and four2-cycles, so f=1. Identify those nine labels with GF(9) so rho is `t→-t`, whose fixed point is0. For the explicit conference core,

    C_(-t,-i)=C_(t,i)

because chi(-1)=1. The same holds for any relative core C'=PCP^T for which rho remains an automorphism. In particular it holds for **every P commuting with rho**, not merely P=id or a field-linear relabeling.

Consequently all those cyclic-inversion conference gluings are impossible under **arbitrary independent diagonal compatibility phases** D,E. They need not be roots of unity and they need not be invariant under rho. The additional local symmetry is only in the unphased seed cores, not in the sought physical array.

There are surviving relative permutations P for which the second unphased core does not preserve rho; this addendum does not classify or exclude them. A full arbitrary-P statement would require a new argument about their actual coefficient matrices and unimodular kernels. The other conference classes and all nonuniform 100-ray arrays also remain untouched.

## 5. Outcome and exact boundary

The phase-gluing route now has two genuine complex obstructions:

1. The main manuscript excludes all relative permutations/phases for odd-cycle zero matchings with a fixed point, including the complete diagonal-prolongation seed.
2. This addendum excludes the natural cyclic-inversion seed whenever the two stripped cores share that inversion, **without** requiring the compatibility phases to share it.

Neither is a general conference9 classification, H0-wide no-go or full 1-RQLS(10) theorem. No scientific execution or enumeration was used. The arguments are complete author-written candidates requiring separate reconstruction and parent review at pinned bytes. Novelty remains uncertified; no old global F9/AGL symmetry exclusion is imported or relabeled as this local phase argument.
