# All-phase 2×5 Diţă Fourier products: transversals force repeated rays

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED**; full independent mathematical review is required. Native `/bin/date` before writing: **Wed Oct 28 18:31:37 PDT 2026**. This strengthens the pinned tenth-root-only candidate `frontier-20261028-dita-q10-product-obstruction-v1.md` SHA **0d753f43ad147fba27d8c2608e8b385aba4a6029f724156ffa60bf55a570130c**; that file remains unchanged. The argument below is self-contained and uses NO phase quantization. It is not an unrestricted QLS10 no-go or a novelty claim.

## 1. Exact scope

Let `zeta=exp(2*pi*i/10)`, `omega=zeta²`, and take ARBITRARY complex phases `delta_t` of modulus1, t∈F5. Define the order-10 Diţă Hadamard

`K_((a,t),(h,b)) = (-1)^(a h) delta_t^h omega^(t b)`,  a,h∈{0,1}, t,b∈F5.

Thus `K=[[F5,D F5],[F5,-D F5]]`, for arbitrary unitary diagonal D, including generic non-root phases. Put the TEN source rows `(a,t)` in an ARBITRARY order indexed by physical coordinates tau∈Z10, and form ACTUAL vectors

`psi_(r,(h,b))(tau) = zeta^(r tau) K_((a(tau),t(tau)),(h,b))/sqrt(10)`.

Row and column gauges/permutations of K, physical row/column relabellings, common unitary and cell phases are allowed. **Claim:** if this product array has ANY orthogonal transversal, at least two of its 100 cells determine the same ray. In particular NO maximal-cardinality member is 1-resolvable, for ANY resolution incidence L. K and the Fourier factor give all20 QLS row/column ONBs. No uniform overlap assumption or root-of-unity restriction on D is used.

Row phases are common coordinate unitaries, K-column phases are cell phases, and K-column permutations relabel physical columns; absorb these before the proof. The physical source row ordering tau->(a,t) stays completely arbitrary. The claim covers this continuous Diţă family only, not all complex Hadamards, all QLSs, or more general independent F5-row permutations in the two Diţă blocks.

## 2. Elementary lemmas

**A. Five tenth roots.** A sum of five tenth roots vanishes iff they are the five distinct roots in a single coset of the fifth roots. Proof: `zeta=-omega³`. Collect the five signed fifth-root terms into integer coefficients; their only rational relation is `1+X+X²+X³+X⁴`. The sum of the five signed coefficients is odd, divisible by5 and has magnitude at most5, so all terms have the same sign and all residues occur once.

**B. F5 complete maps.** If f:F5->F5 and both f(x) and `f(x)+s x` are permutations for nonzero s, then f is affine. Represent f uniquely by a polynomial of degree <=4. Since f is a permutation, `sum_x f(x)=0` forces its x⁴ coefficient to vanish. Comparing the square sums of the two permutations and using `sum_x x²=0` forces `sum_x x f(x)=0`, hence its x³ coefficient vanishes. A genuine quadratic is noninjective in odd characteristic, so f is affine. Thus any permutation with a missing nonzero secant slope is affine.

**C. Two shifts cannot mix in a permutation.** If a permutation `pi:F5->F5` has each `pi(b)-b` in `{d0,d1}`, then pi is one constant shift. Indeed, if d0!=d1, take A={b:pi(b)=b+d0}. Collision avoidance implies A is invariant under the nonzero translation d0-d1; its orbit is all F5, so A is empty or all of F5.

**D. Unit-modulus sequences have no two-point Fourier support.** If `epsilon_t` all have modulus1 and their F5 Fourier transform has at most two nonzero frequencies, it has exactly one and `epsilon_t=lambda omega^(k t)`. For support2, inverse Fourier expansion is `epsilon_t=A omega^(k t)+B omega^(l t)` with A,B!=0 and k!=l. In `|epsilon_t|²`, the nonzero Fourier coefficient A*conjugate(B) at k-l cannot vanish, contradicting constant modulus. Consequently a non-character unit sequence has at most TWO vanishing Fourier coefficients.

**E. Three unit terms.** If three unit complex numbers sum to zero, they form a rotated equilateral triple; all their pairwise ratios are cube roots of unity. It follows that, for three DISTINCT t values and nonzero unit numbers v_t, the sum `sum_t v_t omega^(d t)` can vanish for AT MOST ONE d∈F5. If it vanished for two d, ratios between two terms at the two shifts would force a nontrivial fifth root to be a cube root, impossible.

For B, exact independent enumeration `frontier-20261028-dita-finite-lemmas-v1.py`, SHA **9122fdeffc9f0bd2fec249895f71ee9644b63669dd9e1fbe287afb33b42efd17**, checks all3125 functions F5->F5. Lemmas C–E are proved analytically here; no numerical phase sampling is used in the theorem.

## 3. Every putative transversal has opposite h-row parities

Assume T is an orthogonal transversal. Let E be the five K rows occupying EVEN physical coordinates. For each t set x_t,y_t∈{0,1} according to whether `(0,t),(1,t)` belong to E. Let k be the count of t with `x_t!=y_t`. Since `sum_t(x_t+y_t)=5`, k is odd, hence k∈{1,3,5}; at least one source t appears once at an even and once at an odd physical coordinate.

Let R_h be the five physical rows used in T's columns with that h. For one of those t, let tau_e,tau_o be its even/odd physical coordinates. Their source a labels differ. Since T is an ONB, its summed projectors give off-diagonal entry zero:

`sum_(r in R_0) zeta^(r Delta) - sum_(r in R_1) zeta^(r Delta)=0`,

where `Delta=tau_e-tau_o` is odd. Because R_0,R_1 partition Z10, each sum is zero. If Delta=5 mod10, this is impossible for five signs. Otherwise Delta is coprime to10, and Lemma A forces all five r values of R_0 to have the same parity. Thus **R_0 is one full parity class, and R_1 the other**. In particular every opposite-row pair r,r+5 in T connects opposite h values.

Let pi(b) be the h=1 b-label paired with the h=0 label b in the opposite physical row. This is a permutation F5->F5.

## 4. The h=0 row assignment is affine, with no phase restriction

Write T's physical row for column `(0,b)` as

`r_b=eta+2 q(b) mod10`, eta∈{0,1},

where q is a permutation of F5. Set

`S_s=sum_(tau=0)^9 omega^(s tau+t(tau))`, s∈F5.

Orthogonality between the h=0 cells indexed by b and c requires `S_s=0` for the secant slope `s=(q(c)-q(b))/(c-b)`: apply the cyclotomic automorphism omega->omega^(c-b). S_0=0 because each t occurs exactly twice.

Not all five S_s can vanish. Otherwise Fourier inversion in s would give for each j∈F5 a vanishing sum of the TWO fifth roots associated with tau=j,j+5, impossible because -1 is not a fifth root. Hence at least one nonzero slope is missing from q; Lemma B implies

`q(b)=A b+C` with A∈F5^*.

This step uses only source rows F5 and is independent of delta.

## 5. Opposite-row column pairs have a constant b shift, unless rays repeat

Pair r with r+5. K-column orthogonality plus physical-vector orthogonality imply that their K columns are orthogonal on E. For opposite h, this half inner product is

`H_d = sum_t (x_t-y_t) delta_t omega^(d t)`, d=pi(b)-b.             (1)

Each transversal pair has H_d=0.

- If k=1, (1) cannot vanish: no T.
- If k=3, Lemma E shows H_d vanishes for at most ONE d. Thus `pi(b)=b+d0` for all b.
- If k=5, E selects one source a for each t. Define `epsilon_t=(x_t-y_t) delta_t`, a unit sequence. Its zero Fourier shifts include every `pi(b)-b`. By Lemma D, if epsilon is not a character, there are at most two such shifts; Lemma C then forces one constant shift d0. If epsilon IS a character, `epsilon_t=lambda omega^(k0 t)`, then the two source rows of each t occupy opposite physical parities and

  `(-1)^(tau+a(tau)) delta_(t(tau))=epsilon_(t(tau))`.

  Consequently for every r,b, `psi_(r+5,(1,b))=lambda psi_(r,(0,b+k0))`; the array has repeated rays.

Therefore, to finish the theorem it is enough to exclude a transversal with a constant opposite-pair shift d0 in the k=3 or k=5 NON-character branches. In fact the next step excludes a constant shift for ANY odd k, without using any phase alphabet.

## 6. The constant shift contradicts odd source parity

Suppose `pi(b)=b+d0`. The h=1 cell paired opposite to `(r_b,0,b)` is `(r_b+5,1,b+d0)`. For all b,c, cross-orthogonality and q(b)=A b+C give

`0 = sum_tau w_tau omega^[j*(A*tau+t(tau))]` for ALL j=c-b∈F5,     (2)

where the unit complex weights are

`w_tau=(-1)^(tau+a(tau)) delta_(t(tau)) omega^[d0*t(tau)]`.

For each z∈F5 let F_z consist of physical coordinates with `A*tau+t(tau)=z`. Fourier inversion of (2) gives `sum_(tau in F_z) w_tau=0` for every z. Same-h orthogonality at slope A gives `sum_z |F_z| omega^z=0`; the unique rational relation among fifth roots forces every `|F_z|=2` since the total is10. Each F_z is therefore a PAIR of coordinates whose weights are exact negatives. In particular the whole multiset of ten weights is invariant under negation.

For a given t, its two physical source rows have opposite a. If both source rows lie on the SAME physical parity, their two weights are already an opposite pair. If they lie on OPPOSITE physical parities, their two weights are EQUAL. There are k of the latter t values, and k is odd. Removing the already-balanced opposite pairs from the negation-invariant total leaves two copies of each of k nonzero unit weights in a negation-invariant multiset. Dividing all multiplicities by2 would make an odd-size multiset of nonzero complex numbers invariant under w->-w, which is impossible because this involution has no fixed points. Contradiction.

Thus the non-character branches admit NO transversal; the only remaining character case has repeated rays. This proves the claim under the stated family hypotheses. All equalities are exact; no analytic tolerance or numerical solver supplies a proof step.

## 7. Actual maximal-Qls example outside tenth-root Diţă phases

The stronger all-phase argument covers cases where the half sum has THREE terms, impossible in the previous q10-only proof. For an explicit exact example let the even/odd source rows respectively be

```text
E: (0,0) (0,1) (0,2) (0,3) (1,3)
O: (1,0) (1,1) (1,2) (0,4) (1,4)
```

Interleave E and O in physical coordinate order. Let delta exponents relative to `xi=exp(2*pi*i/30)` be `(0,10,20,1,2)`. Thus the first three are the cube roots, not one tenth-root coset; the E cross-half sum vanishes exactly for shift d=0, with k=3. Independent exact `frontier-20261028-dita-q30-half-check-v1.py`, SHA **d81af56b833ebae6f41b1b6ae07963a90a62753e3a245b006ceae7115fc66c98**, confirms that unique shift by integer reduction modulo Phi30.

The 100 original vectors are recorded as exact xi exponents in `frontier-20261028-dita-q30-maximal-result-v1.json`, SHA **8110bc343c564cdc0e15c7cc4f5bb4ab5c3c77431eacb9655a054a2bfb54eeca**, produced by `frontier-20261028-dita-q30-maximal-producer-v1.py`, SHA **7d78de7cca0869063e197ac30ccea25d2dfad0ccaf3c2b7efd870a5a3848c796**. Independent original-vector checker `frontier-20261028-dita-q30-maximal-check-v1.py`, SHA **ebdd58a0d6be16cea05e9ea1d62c93140440b34c57b95d2be8c82a8501c70753**, independently derives Phi30 from cyclotomic divisibility and reports:

```text
Phi30 ascending [1, 1, 0, -1, -1, -1, 0, 1, 1]
PASS exact original vectors: 100 norms, 20 ONBs, 4950 distinct ray pairs
transversal_found False complete_backtracking_nodes 11
PASS complete original-vector transversal census for this example only
```

It is an actual maximal-cardinality QLS10 with no transversal, NOT a 1-resolvable witness. These finite checks corroborate this ONE example and do not replace §§2–6.

## 8. Remaining original gap

The full continuous four-relative-phase Diţă K family is covered, including arbitrary row permutations, but other Hadamards K, independent row permutations of the two F5 blocks, nonproduct QLSs and all other resolution geometries remain open. The main problem remains either an exact 100-ray 1-RQLS10 or a truly unrestricted impossibility result. Written author proof plus exact sample checking is not a formal proof, external review, human review, or novelty clearance.
