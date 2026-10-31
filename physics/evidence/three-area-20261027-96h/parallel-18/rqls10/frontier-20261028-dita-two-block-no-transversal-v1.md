# No transversal in arbitrary-phase, independently permuted 2×5 Diţă products

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Independent full review required. Native `/bin/date` before writing: **Wed Oct 28 18:34:45 PDT 2026**. This is a stronger and shorter successor to the pinned all-phase maximality obstruction `frontier-20261028-dita-all-phase-product-obstruction-v1.md` SHA **8e1292f778a322fdcb6fd5214d0291ed5232b7b5848943f4caaf0b806b4c4162**; the earlier file stays unchanged. The result is restricted to an explicit Fourier–Diţă family and does NOT settle unrestricted 1-resolvable QLS10.

## 1. The exact all-phase theorem

Let `zeta=exp(2*pi*i/10)` and `omega=zeta²`. Let `mu:F5->F5` be ANY permutation and `delta_t` ANY unit complex numbers. Define the 10×10 Hadamard

`K_((a,t),(0,b))=omega^(t b)`,
`K_((a,t),(1,b))=(-1)^a delta_t omega^(mu(t) b)`,

with a∈{0,1}, t,b∈F5. Choose an ARBITRARY ordering `tau -> (a(tau),t(tau))` of its ten source rows, and form actual physical vectors

`psi_(r,(h,b))(tau)=zeta^(r tau) K_((a(tau),t(tau)),(h,b))/sqrt(10)`.

**Claim:** for EVERY mu, EVERY delta, and EVERY physical source-row ordering, this QLS has NO orthogonal transversal at all. In particular it has no 1-resolution, even if rays are repeated; NO maximum-cardinality premise is needed. Arbitrary K row/column phases or permutations, physical row/column relabelling, common unitary and cell phases are included: row gauges are coordinate unitaries, column gauges are cell phases, column permutations are relabellings, and source-row permutations are already quantified by the arbitrary ordering. Do not infer invariance under a fixed Fourier-coordinate permutation: its effect is handled by the full ordering quantifier.

K is Hadamard directly: each 5×5 block has Fourier-orthogonal rows and columns, and the two a halves cancel for different h; the physical Fourier factor makes each physical column an ONB, while each physical row is K's row ONB. We explicitly allow the two 5×5 blocks to have DIFFERENT row permutations via mu.

## 2. Optional named classification import

The self-contained theorem above needs NO outside classification. Separately, **conditional on** Haagerup's order-five classification — every complex 5×5 Hadamard is equivalent to F5 via monomial row and column transformations — it covers the FULL block construction `[[A,B],[A,-B]]` for arbitrary 5×5 complex Hadamards A,B, arbitrary phases and physical row ordering. Normalize A to F5 using the SAME row monomial in both a halves and an h=0 column monomial; the transformed B is still Hadamard and can be written `D P_mu F5 Q` using the named classification, with Q absorbed by an h=1 column operation. These operations become the allowed gauges/relabelings plus an arbitrary source ordering.

The named imported statement is attributed to U. Haagerup, “Orthogonal maximal abelian *-subalgebras of the n×n matrices and cyclic n-roots,” in *Operator Algebras and Quantum Field Theory* (1997), pp. 296–322. A recent public preprint explicitly states the order-five Fourier classification and cites Haagerup: https://arxiv.org/html/2608.18053 (Introduction; ref. [18]). Its claimed order-six classification is NOT used. The original Haagerup proof was not independently reconstructed here; reviewers should verify the import before adopting the arbitrary-A,B corollary. The explicit theorem in §1 stands without it.

## 3. A finite-field lemma

**Lemma.** If `f:F5->F5` and both `f(x)` and `f(x)+s x` are permutations for nonzero s, then f is affine. Consequently a permutation with a missing nonzero secant slope is affine.

Proof: represent f uniquely by a polynomial of degree <=4. Because f is a permutation, `sum_x f(x)=0` in F5, so its x⁴ coefficient vanishes. Comparing the sums of squares of the two permutations and using `sum_x x²=0` gives `sum_x x f(x)=0`, so its x³ coefficient vanishes. A nonconstant quadratic over F5 is noninjective: x and `-a1/a2-x` have the same value. Hence f is affine. For the consequence, a missing slope s means `q(x)-s x` is itself a permutation.

An independently written exact finite recheck `frontier-20261028-dita-finite-lemmas-v1.py`, SHA **9122fdeffc9f0bd2fec249895f71ee9644b63669dd9e1fbe287afb33b42efd17**, enumerates all3125 functions F5->F5 and confirms the two-good-shift implication. The written proof above does not depend on this enumeration.

## 4. A transversal forces each h group to use a full row-parity class

Suppose T is an orthogonal transversal. Let E be the five K rows occupying even physical coordinates, and for each t let x_t,y_t indicate whether its source rows `(0,t),(1,t)` lie in E. The number k of t with x_t!=y_t is ODD because `sum_t(x_t+y_t)=5`; in particular k>=1.

Let R_h be the five physical row indices used by T in columns of type h. Choose one t whose two physical coordinates tau_e,tau_o have opposite parity. Their source a labels are also opposite. As T is an ONB, the `(tau_e,tau_o)` entry of its identity projector expansion is zero, giving

`sum_(r in R_0) zeta^(r Delta) = sum_(r in R_1) zeta^(r Delta)`,

where `Delta=tau_e-tau_o` is odd. Since R_0 and R_1 partition Z10 and Delta!=0 mod10, both sums are zero. If Delta=5, a five-term sum of signs cannot vanish. Otherwise Delta is coprime to10. A vanishing sum of five tenth roots consists of a full coset of fifth roots: write `zeta=-omega³`, use the unique rational relation among the fifth roots and note the sum of five signed coefficients is odd and divisible by5. Hence the five r values of R_0 all have the same parity. They are distinct, so each R_h is a full parity class and the classes are opposite.

Label the row of T's `(0,b)` cell by `r_0(b)` and its `(1,b)` cell by `r_1(b)`. For h=0,1 respectively write

`r_h(b)=eta_h+2 q_h(b) mod10`,

where each `q_h:F5->F5` is a permutation and eta_h fixes the appropriate parity.

## 5. Both row assignments are affine

Write `f_0(t)=t`, `f_1(t)=mu(t)`. Same-h orthogonality cancels both delta_t and (-1)^a and gives, for b!=c,

`sum_tau omega^[(q_h(c)-q_h(b))*tau+(c-b)*f_h(t(tau))]=0`.

Define `S_h(s)=sum_tau omega^[s*tau+f_h(t(tau))]`. Applying the cyclotomic automorphism omega->omega^(c-b), every nonzero secant slope s of q_h has S_h(s)=0. Also S_h(0)=0 because f_h is a permutation and each source t occurs twice.

The five values S_h(s) cannot all be zero. Fourier inversion in s would force, for every j∈F5,

`sum_(tau congruent j mod5) omega^[f_h(t(tau))]=0`,

a sum of TWO fifth roots. Such a sum cannot vanish since -1 is not a fifth root. Therefore some nonzero slope is missing from q_h, and §3 implies

`q_0(b)=A b+C`, `q_1(b)=A1 b+C1`, where A,A1∈F5^*.

Rechoose the affine constants so `r_1(b)=eta_0+5+2 q_1(b)`; this is merely a different parameterization of the opposite parity class. If `pi(b)` labels the h=1 cell in T's opposite physical row `r_0(b)+5`, then

`pi(b)=lambda b+kappa`, where `lambda=A/A1` is nonzero.           (1)

No half-graph or phase-root condition is used.

## 6. The 25 cross inner products force an impossible parity pairing

For every b,c∈F5, the h=0 cell at row r_0(b), label b, is orthogonal to the h=1 cell in the row opposite r_0(c), label pi(c). Put j=c-b and use (1). After multiplying by the harmless factor10, each cross inner product is

`0=sum_tau w_tau * omega^[b*(lambda*mu(t(tau))-t(tau))]
                    * omega^[j*(A*tau+lambda*mu(t(tau)))]`,       (2)

where

`w_tau=(-1)^(tau+a(tau)) delta_(t(tau)) omega^[kappa*mu(t(tau))]`.

Every w_tau has modulus1. Since b,j independently range over F5, 2-dimensional Fourier inversion of (2) says that the sum of the w_tau in EACH joint fibre

`U_tau=lambda*mu(t(tau))-t(tau)`,
`V_tau=A*tau+lambda*mu(t(tau))`

is zero. Here `V_tau-U_tau=A*tau+t(tau)`.

The same-h h=0 orthogonality for slope A gives

`0=S_0(A)=sum_tau omega^[A*tau+t(tau)]`.

The only rational relation among the fifth roots implies each of the five values of `A*tau+t(tau)` occurs exactly twice. Thus each of its fibres has TWO coordinates. Its joint (U,V) subfibres have zero weight sum; a singleton subfibre is impossible because its weight is nonzero. Therefore the two coordinates lie in the SAME joint subfibre and their two weights are exact negatives. The entire multiset of ten w_tau is consequently invariant under w->-w.

For any fixed source t, its two source rows have opposite a. If their physical coordinates have the SAME parity, their two weights are opposite and are already negation-balanced. If their physical coordinates have OPPOSITE parity, their two weights are equal, since both a and tau parity flip. The number k of these equal pairs is odd by §4. Removing the already-balanced opposite pairs from the total leaves two copies of each of k nonzero weights in a negation-invariant multiset. Dividing all multiplicities by2 would yield a negation-invariant multiset of ODD cardinality, impossible because w->-w has no nonzero fixed point. Contradiction.

This rules out ANY orthogonal transversal, not only a maximal one. It also includes the previously treated mu=identity and all q10 cases without branching on delta. Every identity and fibre condition uses exact complex orthogonality; no numerical computation or unproved phase classification enters §§3–6.

## 7. Independently checked sample with nonaffine mu

Take `mu=(0,1,2,4,3)` (non-affine), source ordering `(0,0),(1,0),...,(0,4),(1,4)`, and delta exponents `(0,10,20,1,2)` relative to `xi=exp(2*pi*i/30)`. This is outside the earlier same-row-permutation, tenth-root-only scope. Its explicit original 100 vectors are recorded in `frontier-20261028-dita-mu-q30-result-v1.json`, SHA **5f96d3c5e97fae46eae217b134626084b9bd19ccf2bc2349b0d952bd1941733f**, producer `frontier-20261028-dita-mu-q30-producer-v1.py` SHA **8b284af80109a76a614312d909d199b15b663c3660e4f2958334cbebdff05f99**.

Independent original-vector verifier `frontier-20261028-dita-mu-q30-check-v1.py` SHA **44772c35e5e3b43a58eee4790a13d5e9f10f92eadff52998abeb60d35225ce26** uses integer reduction modulo `Phi30`, checks all100 unit norms, all20 row/column ONBs, all4950 ray pairs, and all row/column-compatible orthogonal transversals. Actual output:

```text
PASS 100 norms, all20 ONBs, 4950 distinct ray pairs
transversal_found False complete_backtracking_nodes 81
PASS complete transversal search for this sample only
```

This is a genuine maximal QLS10 but is NOT a resolvable one. The finite example check is corroboration only and is not the all-phase proof or independent peer review.

## 8. Remaining scope

The explicit theorem covers the whole stated continuous/F5-permuted Diţă Fourier-product family, ALL L and arbitrary ray cardinality. The general-A,B block corollary additionally imports the named order-five classification. Other Hadamard K (including the separately treated fifth-root Butson family), other product formulas, and nonproduct QLSs remain outside this theorem. No unrestricted impossibility, formal proof, independently reviewed result, novelty clearance, or target 100-ray 1-RQLS is claimed.
