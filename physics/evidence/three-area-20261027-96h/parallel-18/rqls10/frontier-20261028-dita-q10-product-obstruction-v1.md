# Every tenth-root 2×5 Diţă Fourier product fails maximal 1-resolvability

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED**, with independently exact finite-lemma and one-example original-vector checks. Native `/bin/date` before writing: **Wed Oct 28 18:28:37 PDT 2026**. An independent full mathematical review is requested. This is a new all-L, NONuniform family obstruction; it is not an unrestricted QLS10 no-go or a novelty claim.

## 1. Statement, including every physical row permutation

Put `zeta=exp(2*pi*i/10)`, `omega=zeta^2`, and write subscripts t,b∈F5 and a,h∈{0,1}. For arbitrary `delta_t` belonging to a single coset of the tenth roots, let

`K_((a,t),(h,b))=(-1)^(a h) delta_t^h omega^(t b)`.

This is the 10×10 Diţă block Hadamard `[[F5,D F5],[F5,-D F5]]`; D may have ANY fifth- or tenth-root relative phases. Allow arbitrary Hadamard row and column permutations, arbitrary Hadamard row/column unit phases, and an arbitrary common unitary and cell phases on the physical vectors. Let the physical coordinate index `tau` be an arbitrary ordering of the TEN pairs (a,t). The associated product array is

`psi_(r,(h,b))(tau)=zeta^(r tau) K_((a(tau),t(tau)),(h,b))/sqrt(10)`.

**Claim:** if this array admits an orthogonal transversal, it has a repeated ray. Equivalently, NO maximal-cardinality member of the family is 1-resolvable, for ANY incidence L. Row/column ONBs follow immediately from K Hadamard and the Fourier factor; no uniform-overlap hypothesis is used. This family includes many non-Fourier-equivalent K and goes beyond the earlier separable-Fourier/row-permutation obstruction. The theorem does not cover arbitrary complex Diţă phases, other phase orders, all BH(10,10), arbitrary Hadamards, or general QLS10.

Row phase gauges are common coordinate unitaries, column phases are cell phases, and column permutations merely relabel physical columns. A common factor of all delta_t is absorbed into the h=1 column phases. Thus WLOG every delta_t is a tenth root. Crucially, the ordering `tau -> (a,t)` is still ARBITRARY throughout; we do NOT assume a parity-aligned coordinate ordering.

## 2. Two elementary exact lemmas

**L1: odd sums of tenth roots.** A sum of one or three tenth roots cannot vanish. A sum of five tenth roots vanishes iff they are the five distinct roots in one coset of the fifth roots. To see this, use `zeta=-omega^3` and collect any signed sum of fifth roots into integer coefficients n0,...,n4. The only rational relation is a common coefficient times `1+X+X²+X³+X⁴`; in particular all ni are equal. For an odd number k in {1,3,5}, their signed sum is odd, has magnitude at most k, and must be divisible by5. Thus k=5 and the signed count is ±5, forcing all terms to have the same sign and all five residues exactly once.

**L2: complete maps of F5.** If `f:F5->F5` and both `f(x)` and `f(x)+s x` are permutations for nonzero s, then f is affine. Proof: represent f uniquely by a polynomial of degree at most4. Since f is a permutation, `sum_x f(x)=0`, giving its x^4 coefficient zero. Since both maps are permutations, the difference of their square sums, together with `sum_x x²=0`, gives `2s sum_x x f(x)=0`, so the x^3 coefficient is zero. Thus f has degree at most2. A genuine quadratic over the odd field F5 is not injective, since x and `-a1/a2-x` have the same value; hence f is affine.

Consequently a non-affine g:F5->F5 has AT MOST ONE shift d for which `g(t)+d t` is a permutation. Also, if a permutation q has a missing nonzero secant slope s, then q is affine: `q(x)-s x` is a permutation and L2 applies.

Independent exact recheck `frontier-20261028-dita-finite-lemmas-v1.py`, SHA **9122fdeffc9f0bd2fec249895f71ee9644b63669dd9e1fbe287afb33b42efd17**, enumerated 10, 220, 2002 root multisets of lengths1,3,5; zero counts were 0,0,2 respectively. It also exhausts all3125 functions F5->F5 and checks the two-good-shifts consequence. The written proofs above, not enumeration alone, justify both lemmas.

## 3. An arbitrary transversal forces one even coordinate per t

Suppose T is any orthogonal transversal, and E is the set of the five K rows assigned to EVEN physical coordinates tau. Pair the transversal cells in physical rows r and r+5. Since a transversal uses all ten columns exactly once, these five pairs form a perfect matching on K-column labels. K-column orthogonality gives sum_E+sum_O=0, while opposite-row vector orthogonality gives sum_E-sum_O=0; hence each matched pair is orthogonal on E.

For each t let x_t,y_t be the indicators that `(0,t),(1,t)` belong to E. If the two K columns have the SAME h, their distinct b values differ by some nonzero d, and their half inner product is

`sum_t (x_t+y_t) omega^(d t)`.

It vanishes iff all five coefficients `x_t+y_t` are equal. Their sum is5, so every coefficient is1. Thus a same-h half edge exists only when E chooses exactly ONE of `(0,t),(1,t)` for every t.

For DIFFERENT h, the half inner product is, up to a nonzero common column phase,

`sum_t (x_t-y_t) delta_t omega^(d t)`.

The number of nonzero summands is odd, because `sum_t(x_t+y_t)=5`; it is 1,3 or5. By L1, vanishing is impossible with1 or3 terms. Five terms occur iff E again selects exactly one row for every t. Therefore, if this one-per-t condition fails, the half graph has NO edges and cannot have T's required perfect matching.

From now on assume one-per-t. Write `a_e(t)` for the source a on the even coordinate associated with t, and define

`epsilon_t=(-1)^a_e(t) delta_t`.

Each t occurs once on an even and once on an odd physical coordinate, with opposite source a labels. Hence for EVERY physical coordinate tau,

`(-1)^(tau+a(tau)) delta_(t(tau)) = epsilon_(t(tau))`.            (2)

## 4. The transversal's two h groups use opposite physical row parities

Let R_h be the set of five physical row indices used by T in columns with that h. For each t, let tau_e and tau_o denote its even and odd physical coordinates. An ONB's sum of rank-one projectors is I. The `(tau_e,tau_o)` off-diagonal entry gives, because the two source a labels are opposite and t is equal,

`sum_(r in R_0) zeta^(r Delta) - sum_(r in R_1) zeta^(r Delta)=0`,

where `Delta=tau_e-tau_o` is odd. R_0 and R_1 partition Z10, so the two sums are both zero. If `Delta=5 mod10`, either sum is a sum of five signs and cannot vanish. Otherwise Delta is coprime to10; by L1 the five roots in either sum all lie in one fifth-root coset. Since Delta is odd, the five r values have the same parity. They are distinct, so **R_0 is one entire parity class and R_1 is the other**.

It follows that in T every opposite-row pair is CROSS-h. Let its h=0 and h=1 column labels be b and b+d. Their half orthogonality gives

`sum_t epsilon_t omega^(d t)=0`.                                    (3)

All epsilon_t are tenth roots. By L1, for some tenth-root lambda and some function g:F5->F5 we have

`epsilon_t=lambda omega^g(t)`, with `g(t)+d t` a permutation.        (4)

If g is affine, say `g(t)=k t+c`, equation (2) yields, for EVERY r,b,

`psi_(r+5,(1,b)) = lambda omega^c psi_(r,(0,b+k))`.

Thus the array has repeated rays. We may therefore suppose g NON-affine. By L2, equation (3) can hold for at most ONE shift, call it d0. Hence every opposite-row pair in T connects `(0,b)` to `(1,b+d0)`.

## 5. The h=0 row assignment must be affine

Enumerate T's h=0 cells by b∈F5. Because R_0 is an entire parity class, uniquely write their physical rows as

`r_b = eta + 2 q(b) mod10`, eta∈{0,1},

with q a permutation F5->F5. Define

`S_s = sum_(tau=0)^9 omega^(s tau+t(tau))`, s∈F5.

For b≠c, orthogonality of these two h=0 cells says `S_s=0` for their secant slope `s=(q(c)-q(b))/(c-b)`. This follows by applying the cyclotomic automorphism omega->omega^(c-b). We have `S_0=0`, since each t occurs twice. It is IMPOSSIBLE for all five S_s to vanish: Fourier inversion in s would imply, for each j∈F5,

`sum_(tau congruent j mod5) omega^(t(tau))=0`,

a sum of TWO fifth roots, impossible because -1 is not a fifth root. Thus some nonzero s has `S_s!=0`, and q has this missing slope. L2 therefore implies `q(b)=A b+C` for A∈F5^*.

## 6. Cross-orthogonality contradicts the same-h requirement

T's h=1 cell opposite to `(r_b,0,b)` is `(r_b+5,1,b+d0)`. For any b,c, use (2), (4), and `q(c)-q(b)=A(c-b)`. Cross-orthogonality gives, for every j=c-b∈F5,

`0 = sum_tau omega^[g(t(tau))+d0*t(tau)] * omega^[j*(A*tau+t(tau))]`.  (5)

For each z∈F5, let `N_z` count the physical coordinates with `A*tau+t(tau)=z`. Fourier inversion of (5) says the sum of the fifth-root weights over EACH such fibre is zero. Every vanishing fifth-root sum has length divisible by5, so **every N_z is a multiple of5**.

On the other hand, same-h orthogonality from §5 at slope A says

`0=S_A=sum_z N_z omega^z`.

The only rational relation among the fifth roots forces all N_z equal; their sum is10, so each N_z=2. This contradicts divisibility by5. The non-affine branch therefore has no transversal at all. The affine branch has repeated rays. This proves the stated alternative for ANY resolution and EVERY allowed coordinate ordering.

## 7. Independently checked actual maximal QLS example (not resolvable)

Choose `t(tau)=floor(tau/2)`, `a(tau)=tau mod2`, and `delta_t=omega^f(t)` with `f=(0,1,2,4,3)`. The explicit 100×10 tenth-root exponent array is

`frontier-20261028-dita-maximal-qls-result-v1.json`, SHA **53fff425a977ee9ef7211203c14159cfa9ed30c7ca30fa4ef5e0a32c8f8f326d**;
producer `frontier-20261028-dita-maximal-qls-producer-v1.py`, SHA **dc24b81a218c8c387bbbfea5f301a6c979f0d122a413e72454eef63f096ec968**.

Independent exact original-vector verifier `frontier-20261028-dita-maximal-qls-check-v1.py`, SHA **c532739c6b1c19645dc17f574df315cbbbed5abcb1915db0ecb78af0f0d1c1e3**, checked all100 unit norms, all20 row/column ONBs, and all4950 pairs of cells for distinct rays by tenth-root integer arithmetic. It additionally exhaustively backtracked all row/column assignments for this ONE array and printed

```text
PASS exact 100 unit vectors, all20 row/column ONBs, all4950 ray pairs distinct
transversal_found False complete_backtracking_nodes 161
PASS complete exact original-vector transversal search for this one example only
```

This is an actual maximal-cardinality QLS10 but NOT a 1-resolvable one. Its finite search corroborates only this example; it is not the all-K proof in §§3–6. Exact arithmetic was used, no tolerance.

## 8. Scope and review

This branch is valid under the written hypotheses only and must be independently reviewed; the unreviewed derivation and finite checks are neither formal proof nor independent human/configured-family review. It does not classify all BH(10,10) matrices or Diţă matrices with arbitrary phases, does not supply a 100-ray 1-RQLS, and does not establish an unrestricted no-go. Distinguish this ALL-L restricted nonuniform result from the previously delivered ALL-BH(10,5) Fourier-product result and the separate uniform-Gram results.
