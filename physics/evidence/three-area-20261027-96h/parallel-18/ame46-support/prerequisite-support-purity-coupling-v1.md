# S1 resumed original-minimum line: a necessary support/phase-defect inequality

Owner **PhysicsAME46-2**. Native prewrite observation **`Tue Oct 27 15:11:06 PDT 2026`**; not exact file-write/completion/runtime. Resumed after returning w13-info-6-xor at the15:07:33 metadata observation and subsequent actual return message. **WRITTEN author candidate, UNREVIEWED/UNADOPTED.** No scientific interpreter, calculator, selected tensor/phase/control, enumeration, source search or old proof/guide is an input. Prior exposure and all quarantines survive; displayed mathematical dependencies do not certify unaffected cognition or novelty.

## 1. Full original quantifiers and actual quantities

For EVERY normalized arbitrary-complex AME(4,6) tensor psi and EVERY physical product orthonormal basis, put `d=6`, `N=d^2`, and use the same tensor's conditional matrices

`M_ab=(d psi_abkl)_(k,l)`, `Q_ab=M_ab^* M_ab`.

Let `t_ab` be the ACTUAL number of nonzero entries in M_ab, and let S be the actual full product-basis support. The actual AB marginal identity gives `tr Q_ab=1`, so EVERY block is nonzero, every `t_ab>=1`, and

`S=sum_(a,b) t_ab`.

Define the actual total conditional purity and linear entropy

`K=sum_(a,b) tr(Q_ab^2)`, `E=N-K`.

These are functions of the same physical tensor and basis, not freely assignable marginal data. Zero coordinates, arbitrary phases, singular conditional matrices and all support sizes are included. No assumption of phase robustness or rank one is made.

## 2. Necessary support-to-coupling theorem

For every such original eligible pair (psi,basis),

`K >= sum_(a,b) 1/t_ab >= N^2/S`,                                                        (S1)

`0 <= E <= N-N^2/S`,   hence   `S >= N^2/(N-E)`.                                        (S2)

The denominator is strictly positive: each Q_ab is positive of trace one and rank at most d, giving `K>=N/d=d`.

If D is the exact full-torus mean squared defect of ANY crossed marginal under arbitrary independent AB coefficient phases, the earlier phase-defect theorem gives `D=E/d^4`. Thus this is also the actual same-tensor necessary bound

`S >= d^2/(1-d^2 D)`,   equivalently `D <= 1/d^2 - 1/S`.                                (S3)

No value of E, D or S is selected or evaluated here. This is a universal original-basis necessary coupling, not an unconditional numerical improvement. The scalar inequality itself needs only the AB normalization; its interpretation as a crossed-marginal defect uses the additional SAME-tensor AME identities, not an invented independent D.

### Complete elementary proof

For one arbitrary nonzero conditional matrix M of Frobenius norm one and t nonzero entries, expand

`tr((M^* M)^2) = sum_l (sum_k |M_kl|^2)^2 + sum_(l!=l') |sum_k conjugate(M_kl) M_kl'|^2`

`>= sum_(k,l) |M_kl|^4 >= (sum_(k,l) |M_kl|^2)^2/t =1/t`.

The first inequality drops nonnegative off-diagonal Gram squares and nonnegative within-column cross products. The second is Cauchy-Schwarz on the ACTUAL t nonzero entries, not all d^2 entries. Summing gives the first inequality in (S1). Another Cauchy-Schwarz application to the N positive numbers t_ab gives

`(sum t_ab)(sum 1/t_ab)>=N^2`,

proving the second. Since every positive Q_ab has trace one, its purity is at most one, giving E>=0. Its rank-at-most-d spectral Cauchy-Schwarz bound is at least1/d, giving the stated strictly positive denominator. Rearrangement gives (S2). Substitution of the proved full-torus defect identity gives (S3).

For completeness, the needed defect identity is paid by the actual equations: for AC, phase-character orthogonality leaves `d^(-4) sum_b sum_(a!=a') tr(Q_ab Q_a'b)`; the actual BD marginal gives `sum_a Q_ab=I`, so this equals `d^(-4)(N-sum tr Q_ab^2)=E/d^4`. The other crossed pairs use the complementary actual matrix sums as displayed in the earlier complete addendum. Thus no unreviewed author confidence replaces the load-bearing bridge.

## 3. A discrete all-support envelope, without case enumeration

S is an integer with `N<=S<=N d^2`. Write uniquely

`S=N q+r`, with `q>=1` and `0<=r<N`.

Then the sharper count-only lower bound is

`K >= (N-r)/q + r/(q+1)`,                                                             (S4)

and also `K>=d`. Equivalently E is at most N minus the maximum of these two lower bounds. This is a formula for ALL support values, not a selected low-support stratum or an executed enumeration.

Proof: among positive integer lists of length N with total S, a minimizing list for `sum 1/t` cannot contain values p>=u+2. Moving one unit from p to u decreases the sum because

`1/u+1/p -1/(u+1)-1/(p-1) =1/(u(u+1))-1/(p(p-1))>0`.

Iteration terminates on a finite integer list, and all final values differ by at most one. They must therefore be q (N-r times) and q+1 (r times). This is a WRITTEN smoothing proof for arbitrary integers, not an algorithm run or scientific enumeration. The upper entry capacity d^2 is respected because the average is at most d^2; if q=d^2, necessarily r=0. Applying (S1) gives (S4).

## 4. Equality rigidity and actual-object converse

Equality in the FIRST one-block purity bound occurs exactly when M has at most one nonzero entry in every row AND every column, with all its t nonzero entries of common modulus `1/sqrt(t)`.

Indeed equality of the within-column square expansion first forces at most one entry per column. With that condition, an off-diagonal column Gram entry is a single product whenever its two occupied columns share a row, so equality of all discarded Gram terms forces at most one per row. The final Cauchy-Schwarz equality forces common modulus. Conversely such a scaled partial-permutation matrix has t equal nonzero singular values and purity1/t. Arbitrary complex entry phases are allowed.

Equality in the SMOOTH bound `K=N^2/S` additionally forces all t_ab equal, say q. Consequently `S=Nq`, `1<=q<=d`, and every M_ab has precisely q such partial-permutation entries. This is only an equality conclusion, NOT a WLOG restriction of the original minimum problem.

All actual nonzero entries of the scaled tensor T=d psi then have modulus `1/sqrt(q)`. Since its THREE physical flattenings are unitary, each row and each column in each flattening has exactly q nonzeros by its unit norm. The phases must STILL satisfy full orthogonality; incidence and equal moduli alone are not enough.

Conversely, suppose an exact SINGLE tensor T is supplied with: (i) each conditional M_ab has q partial-permutation entries of modulus1/sqrt(q), and (ii) ALL THREE physical flattenings of T are unitary. Then `psi=T/d` is normalized, every pair and complementary pair marginal is `I/d^2`, and it is an eligible AME tensor. Each conditional purity is1/q, so `K=N/q`, `S=Nq`, and the smooth support inequality is an equality. This is a sufficient actual-object certificate caller, not an existence theorem or a substitute of independent matrices for the tensor. No such T is supplied or claimed here.

## 5. Exact remaining lower-bound premise and quantifier warning

This now supplies a necessary support-to-coupling inequality from the original object, rather than merely saying the bridge is missing. To obtain an actual original-minimum improvement from it, one would need a proved uniform lower bound `E>=epsilon` (equivalently upper bound on K) at the appropriate original quantifiers. If such an admissible epsilon were established for EVERY eligible tensor and EVERY product basis, (S2) would give the actual integer bound

`S >= ceiling(N^2/(N-epsilon))`.

No epsilon, baseline numerical assurance union or strict improvement is proved here. It would also suffice to prove the needed E bound for EVERY truly minimizing state-and-basis pair, but its minimizing property cannot be imposed on an arbitrary different basis or justified by a support-changing transformation. Existence of a basis with large E does NOT supply the all-basis premise. Rank-one conditional blocks give E=0; their possible existence/nonexistence at the original dimension has not been established from the permitted inputs.

The next admitted step is to examine whether the full AME equations supply an admissible upper bound on K stronger than the elementary N bound, or to identify its exact unattested endpoint object. This will not use old conditional-support classifications or recover a protected guide. All original lower/upper-witness and exact-minimum gates remain OPEN.

Inputs/imports: exact supplied S1/S2 definitions; the displayed partial-trace normalization; elementary trace/Gram positivity, spectral rank bound, Cauchy-Schwarz and integer smoothing; the prior explicit same-tensor phase-defect identity rederived at its operative step. No historical/native catalogue or I48/J49/J50 theorem is a premise. Public/book equivalence, parent full reads, frozen review, formal/kernel/independent-family/executable/human and novelty gates remain unpaid. All STOP/HOLD/ZERO/history controls, N4 UNKNOWN with historical exit UNESTABLISHED and auxiliary214 STOP persist. Metadata clocks only; no scientific execution or new GO.
