# v31-A: independent written reconstruction of the two Boolean-box algebra

Reviewer: **InfoHinfPreview-2**, retaining info-3. Author: **MathOlson-2**, math-2. Assignment **v31-A**. Actual startup clock: **Sun Oct 25 04:33:11 PDT 2026**; actual clock observed after reconstruction and before this return: **Sun Oct 25 04:35:43 PDT 2026**, both returned `/bin/date` outputs.

## 1. Verdict at the actual slice

**0 FATAL / 0 MAJOR / 0 MINOR algebraic findings at the frozen scope.** I reconstructed the two distinct Boolean-box arguments, the exact boundary coefficient, the constant-term omissions, and the parity-completed rotation-status polynomial from the raw displayed formulas. No low-band verdict, author diagnostic, finite enumeration or prior acceptance was imported.

**All load-bearing obligations of the assigned algebra slice were reconstructed in writing.** This is a same-harness, different-domain **supplied-proof written reconstruction**, not blind, cross-vendor/different-family, configured dual-family, human, formal/kernel, executable-certificate, novelty or parent acceptance. It is not a unilateral composition of the A/B gates or a parent declaration that the full band is accepted. The separately assigned applicability slice still requires its actual return and parent full read.

The source's mathematical argument is reconstructed below; this headline is not the evidence in place of that argument. Explicit NOT_RECONSTRUCTED/non-claims appear in section9.

## 2. Exact snapshots, coverage, and exposure

All hashes below were freshly observed with metadata-only `shasum -a 256` before reconstruction:

| Item | Actual SHA-256 | Coverage |
|---|---|---|
| `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v31.json` | `73cf8654ddca55870d137b3e447355274c54a733451fa9aa3d1d6a1dc3dcf5d8` | Common contract and exact v31-A entry read first. |
| `institute/runs/three-area-2026-10-23-96h/parent-evidence-erratum-v7.md` | `d5e1911bba6549684c93b2e910fac66eb44c353ae5dea2a8d1555516946e8d05` | Complete LF1–39 read before author body. |
| `institute/runs/three-area-2026-10-23-96h/peer-review-wave-v31-olson-double-box-algebra-sources-part1-v1.md` | `e98f530639efe1df937a80d9769b0970e474ebe074265c8e752998ff1967e33c` | Complete LF1–229; all literal source LF1–220 read. This is the only assigned literal part. |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/proof-FIXED-ROTATION-DOUBLE-BOX-BAND-CLOSURE-v1.md` | `26b39995d5a7816233fd992ef11b6f193d2e4615f5ede2a4a340b4155e32c86f` | Actual original LF1–220 also read directly, in ranges covering LF1–118 and LF119–220. |

The observed literal/source hashes match the exact assignment pins. No reader-truncated line was treated as read; the two complete ranged packet reads and the two original reads displayed their source bodies without a reported long-line truncation. Source line citations below refer to the actual 220-line author original, not the packet's prefixed line positions.

Exposure was frozen first in `peer-review-olson-double-box-algebra-ack-v1.json`: I had seen round summaries of the older critical matching branch, the L_MAX refutation and unresolved L_RES, and the v31 title/scope headline. I had not read this current220-line author body in this run before the ACK. No v31-B reviewer return or parent correctness verdict was read or inherited. I then read the complete supplied proof and independently reconstructed its displayed algebra.

No scientific eval/interpreter, symbolic program, arithmetic program, enumeration, certificate replay, solver, simulation, external-model CLI, nested agent, git operation, deletion or author/shared write was used. The parent v7 withdrawal is binding; the author's six old diagnostics and my own previously disclosed arithmetic have **no verification role here**. Only metadata clocks/hashes, source reads and this owned-root written return were used for this review.

## 3. The signed-box functionals really are different — source LF29–48

For d Boolean variables define

$$\Lambda_d(H)=\sum_{a\in\{0,1\}^d}(-1)^{|a|}H(a).$$

For one ordinary monomial `u^alpha`, the sum factors coordinatewise. A zero exponent gives the factor `1-1=0`; a positive exponent gives the factor `-1`, since only the Boolean value1 contributes. Thus every monomial missing a variable has zero signed sum.

- If total degree is **strictly below d**, every monomial misses a variable. Hence `Lambda_d(H)=0`: B1.
- If total degree is **at most d**, the only possibly surviving monomial is the product of all d variables with each exponent one. Hence `Lambda_d(H)=(-1)^d [u_1...u_d]H`: B2.

These are ordinary polynomial statements over F_p. No Boolean reduction or multilinearity is assumed. In particular a power of one variable does not secretly count as containing a different missing variable. This distinction is used correctly: the first box is at its degree boundary and uses B2; only the second box uses the strict-degree B1 cancellation.

## 4. Raw input polynomials and the actual zero-colour slot — source LF50–107

I checked the displayed local word bridge sufficiently to validate the algebra's inputs, without inheriting the other slice's verdict.

Let `a_t` be the indicator that the actual reflection f_t is selected. The rule is

$$a_t=u_t+u_{t+1}-2u_tu_{t+1}$$

at Boolean points, with `u_1=u_(F+1)=0`. The recurrence is `u_(t+1)=u_t XOR a_t`, so u_t is exactly the selected-reflection prefix parity before gap X_t and before f_t. Returning to the zero boundary makes the reflection count even.

For a rotation in X_t the actual group law contributes `(1-2u_t)*x`. A selected reflection contributes

$$a_t(-1)^{u_t}y_t=(u_{t+1}-u_t)y_t.$$

This equality checks the four Boolean pairs directly as a written case identity; no enumeration program was run. Summing the latter terms telescopes to `sum_(t=2)^F (y_(t-1)-y_t)u_t`. Rotations do not change reflection parity. Therefore the author's affine V_K and quadratic integer size Z_K are exactly

$$V_K=C_K+L_K,$$

$$Z_K=k+2\sum_{t=2}^F u_t-2\sum_{t=2}^{F-1}u_tu_{t+1}.$$

Thus

$$Z_2=-2\sum_{t=2}^{F-1}u_tu_{t+1}$$

is the homogeneous quadratic part and does not depend on K at all. The boundary-zero variables really remove both cyclic-end quadratic terms; they have not been accidentally included.

The chosen **actual** occurrence r0 lies in X1, so its product contribution is constant x0 and its size contribution is constant1. Its u-linear contribution is `-2*x0*u1=0`. Consequently toggling this one occurrence changes C_K and k but changes neither L_K nor Z2. This is an identity of the displayed raw polynomials; it is not an assertion that Q_K or the actual product stays unchanged after the toggle.

Repeated rotation values, repeated gap indices and rotations elsewhere in X1 are allowed. A repeated gap merely adds coefficients of the same u variable; a rotation in X1 contributes no u-linear term. Zero x values similarly remove a coefficient. No injectivity or nonzero determinant is required anywhere below.

## 5. Fermat indicator and the exact top coefficient — source LF109–132

Write `n=p-1` and `M=3n=F-1`. In F_p, Fermat gives `1-a^n=1` when `a=0`, and gives zero otherwise. Therefore

$$Q_K=(1-V_K^n)(1-Z_K^n)$$

is exactly the pointwise indicator of simultaneous `V_K=0` and `Z_K=0 mod p`. The size congruence alone is not yet an integer size assertion; that separate step is reconstructed in section6.

Here `deg_u V_K<=1`, `deg_u Z_K<=2`. The four expanded terms have degree bounds

| Term | Total u degree bound |
|---|---|
| 1 | 0 |
| `-V_K^n` | n |
| `-Z_K^n` | 2n |
| `+V_K^n Z_K^n` | 3n=M |

The target squarefree monomial contains exactly M u variables and has total degree M. Only the last term can supply it.

Inside that product there are n affine-V factors and n quadratic-Z factors. The maximum possible degree is achieved only if **every** V factor supplies its degree-one part L_K and **every** Z factor supplies its degree-two part Z2. Taking even one constant from V loses at least one degree; taking even one constant or linear term from Z also loses at least one. No other factor has excess degree to replace that loss. Consequently

$$[u_2\cdots u_F]Q_K
 =[u_2\cdots u_F]L_K^n Z_2^n.                              \tag{A}
$$

This proves the exact author equality(6) from raw polynomials and accounts for **all** omitted terms, including k and the constant product effect of r0. Cancellation of leading terms over F_p can make a coefficient zero; it cannot create a missing higher-degree contribution or invalidate (A). The identity also holds if L_K happens to vanish identically.

Since p is odd, M is even. B2 therefore gives

$$\Lambda_M(Q_K)=[u_2\cdots u_F]L_K^{p-1}Z_2^{p-1}.         \tag{B}
$$

It would have been false to invoke B1 directly for Q_K at `degree<=M`; the author does not do that. This is the load-bearing boundary distinction in the proposed proof.

## 6. What hypothetical failure forces on the first box — source LF134–149

Assume the cut word has no identity selection of exactly2p. For an even actual K, the selected reflection count is even, so total integer size Z_K is even. The size lies between zero and `N=4p-1`. Among its nonnegative multiples of the odd prime p, the only positive **even** possibility is2p: p and3p are odd, while4p exceeds the entire word length.

The selected product has positive sign coordinate because the reflection count is even. Thus an indicated Boolean point of Q_K is an actual identity2p selection unless its integer size is zero.

- If K is nonempty and even, size is at least2; hence **every** Q_K Boolean value must be0 under the failure hypothesis.
- If K is empty, zero size means no selected reflection. The zero-boundary recurrence forces every `u_t=0`. At `u=0`, both V and Z vanish and `Q_empty=1`. Every other indicated Boolean point would have positive size and therefore give the forbidden identity2p.

It follows that

$$\Lambda_M(Q_K)=0\quad(K\ne\varnothing\text{ even}),\qquad
\Lambda_M(Q_\varnothing)=1.                               \tag{C}
$$

There is exactly one empty-point contribution and its sign is positive. It is not multiplied by an unspecified number of equivalent colourings: fixing u1=0 made the parametrization unique. This step does not require generic rotation/reflection values, a matching bound, or an old residual exclusion.

## 7. Rotation-status box, parity completion and the contradiction — source LF151–190

Keep the named actual r0 aside and label the other p actual rotation occurrences separately. Define the formal affine-in-status polynomial

$$L(z;u)=\sum_{t=2}^F(y_{t-1}-y_t)u_t
          -2\sum_{i=1}^p z_i x_i u_{g(r_i)},$$

and

$$G(z)=[u_2\cdots u_F]L(z;u)^{p-1}Z_2(u)^{p-1}.$$

Every factor of L has status degree at most1 and there are only p-1 such factors; Z2 has status degree0. Hence **total** status degree is at most p-1, not merely degree at most p-1 in each coordinate. Extracting a u coefficient is F_p-linear and cannot increase total z degree. This proves the exact bound needed for the p-variable B1 application.

For each Boolean status vector let A be its subset of the p named actual occurrences. Use K(A)=A for even |A| and K(A)=A union{r0} for odd |A|. Then K(A) is always even, is empty exactly when A is empty, and uses at most the available p+1 distinct occurrence labels. In particular the all-one vector is allowed: p is odd, so the selected K has p+1 occurrences. Equal group values do not identify distinct occurrence labels.

Because r0 has no u-linear contribution,

$$L_{K(A)}(u)=L(1_A;u).$$

The nonlinear parity rule is used **only to select an actual even K at Boolean status points**, after (A) has removed all constant dependence on r0 and k. There is no insertion of a degree-p parity polynomial into G, and no assertion that the full Q_K depends low-degree-polynomially on K(A). This clean separation makes the argument valid.

Combining (B),(C) at those actual K values forces

$$G(0)=1,\qquad G(z)=0\text{ at every other Boolean status point}.$$

But G has degree at most p-1 in p variables. By B1,

$$\sum_{z\in\{0,1\}^p}(-1)^{|z|}G(z)=0.$$

Its displayed point values make the same sum1. Since1 is nonzero in F_p, this is a contradiction.

This is a second, **strictly lower total-degree** Boolean-box argument. It does not reuse the first box with a relabelled variable count. There is no monomial of total degree<=p-1 supported on all p status coordinates, even if individual powers or gap collisions occur. Thus every monomial cancels in the second box exactly as claimed.

## 8. Actual-word scope checks and no hidden algebraic imports — source LF192–220

The contradiction yields some actual even K and actual Boolean u satisfying the indicated conditions with positive integer size. The even-multiple argument gives size **exactly2p as an integer**, not merely the field equality0. The chosen items are named actual rotations and actual reflection-colour changes, all at distinct original positions. No virtual identity rotation, gap insertion or packet endpoint was used.

I also reconstructed the displayed cyclic restoration: if original AB is cut to BA and selected-part products satisfy `P_B P_A=1`, then

$$P_A P_B=P_B^{-1}(P_B P_A)P_B=1.$$

The same occurrence set is restored, not an alternative selector, and the cardinality is unchanged. This local check supports the raw algebra's interpretation; it is not a substitute for the separately commissioned B applicability review or its residual-definition audit.

All prime p>=7 are covered: the proof needs a prime field for the Fermat indicator, odd p for parity/multiple arguments and for M even, and the stated exact counts. No step requires a larger p threshold, a nonzero rotation value, distinct reflection values, unique gaps, or a coefficient determinant to be nonzero. If degeneracy removes a status variable, it only strengthens the strict-degree incompatibility with a nonzero Boolean point mass.

The earlier theoremP source is credited at LF214 but its result is not a mathematical premise: the needed signed-box identities, product formula and degree steps are all proved in this220-line snapshot and reconstructed above. I did not read an old theorem as an imported correctness oracle. EGZ, Lev/S(p), inverse forms, maximum-matching packet lifting, historical computations and author exploratory diagnostics are not consumed by this reconstruction.

The algebra therefore supports the candidate's entire fixed-count band statement **conditional on the literal actual-word hypotheses and independently settled applicability gate**. It does not establish a selector lying inside a maximum-matching packet family. A selection outside that family is compatible with the retained L_MAX refutation.

## 9. NOT_RECONSTRUCTED obligations and non-claims

No load-bearing algebraic equality or cancellation in the assigned source is left NOT_RECONSTRUCTED. The following are explicitly outside this return:

1. **NOT_RECONSTRUCTED: historical residual-definition chain.** I did not re-read `consolidated-lower-band-v1.md`, every OLD/REF/SEL/IPGEN/GS/DS3 caller, or the old L_MAX counterexample. A universal fixed-count actual-word theorem would apply to any genuine subset of that band, but this algebra return does not newly certify all named residual predicates or historical caller bookkeeping.
2. **NOT_RECONSTRUCTED as a separate review gate: v31-B.** I did not read or inherit that review. My local word/parity/cyclic checks are written redundancies, not an assertion that the independent applicability review has returned or passed. Parent composition remains required.
3. **NOT_RECONSTRUCTED/NOT_CLAIMED: packet-only L_RES or L_MAX.** The proof need not place the selector inside a maximum-matching packet family; neither claim follows from this review.
4. **NOT_RECONSTRUCTED/NOT_CLAIMED: other R bands, unrestricted prime-dihedral ordered Olson or all-finite-group book question.** This source has exactly R=p+1 and F=3p-2.
5. **NOT_SUPPLIED: computational extraction algorithm, complexity bound, scientific certificate replay or formal proof.** Finite existence follows from the written contradiction, not from a performed enumeration.
6. **NOT_PERFORMED: novelty/priority clearance, human/cross-vendor/configured-dual-family review and parent acceptance.** Same-harness different-domain reconstruction does not supply these.

**Disposition recommendation:** retain this actual v31-A return as a completed no-defect **written algebra reconstruction at its pinned scope**. Await the disjoint applicability return and parent full read before composing any accepted full-band or identity-selection L_RES statement. Parent errata v1–v7 and the global scientific-launch HOLD remain binding; no computation or new GO is authorized by this recommendation.
