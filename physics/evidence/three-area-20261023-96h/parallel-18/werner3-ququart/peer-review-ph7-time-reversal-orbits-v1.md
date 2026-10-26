# v32-D — written reconstruction of PH7 time reversal and all five allocation orbits

Observed `/bin/date` before this review: **Sun Oct 25 04:49:41 PDT 2026**. Reviewer PhysicsResearch96h-2; author MathResearch96h. **0 FATAL / 0 MAJOR / 0 MINOR at the explicit written/import scope below.** This is not an8/9 feasibility verdict, novelty clearance or automatic parent acceptance.

## 1. Binding, exposure and complete coverage

The completed prior v30-A review was returned before this assignment. No v31 review is pending for this owner. The present exposure ACK is `peer-review-ph7-time-reversal-orbits-ack-v1.json`, written before the packet body was read. It discloses the prior PH7 band/conic reconstruction; this is supplied-proof review, not blind review.

Read the exact v32-D entry in RUN/`peer-review-wave-eighteen-v32.json`, SHA256 `7c2f7e7679040669e9e97fb71da76e7e1eb846cb5af28f35afe55d593e504708`; read parent erratum v7 and the complete packet receipt SHA256 `ef9ce1e16eeb1a8f9653b9167b909190591bc22e8f5bee4c658b508d9bd13cc1`.

Read the ENTIRE literal packet RUN/`peer-review-wave-v32-ph7-time-reversal-orbits-sources-v1.md`, LF1-163, SHA256 `5d484098a7319ef54fc6c07cf66acc660674432f66e23800e8e869c5535ebefd`, including original source LF1-154. Explicit RAW rereads of long packet lines152,154,156,162 were also made. No unread truncation or partial source body is treated as reconstructed.

The actual source `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-time-reversal-five-orbits-v1.md` hashes to its frozen SHA256 `6e539a6887c6d54f97658dad9536a738991f8df2e951f89ef58bbe8aa7d28dc4`. References below use its ORIGINAL source LFs. RUN is `institute/runs/three-area-2026-10-23-96h/`.

For the complete predecessor allocation comparison, additionally read ORIGINAL LF108-147 of `PH7-dominator-shared-block-identities-v1.md`; its actual SHA256 matches the declared import `941ea246ba96e00e820021733b0d716e79cc103807a86f97ee5b31dfabf5b969`. This is an explicitly limited additional source range, not a claim of a new complete read/review of that227-line predecessor.

**Execution:** strictly written reasoning/source reconstruction. No scientific eval/interpreter/arithmetic program/enumeration/symbolic program/certificate replay/solver, no nested agent or model CLI, no GO. Only metadata clocks/hashes and literal source reads. No author's or reviewer's unadmitted earlier arithmetic is a premise; all v7 qualifications remain binding. No author/shared or pinned source bytes were changed.

## 2. Strict positivity of the occupation vector — source LF21-31

Let S be the states reachable from the support of alpha using positive off-diagonal entries of T. If a row in S had a positive transition to a state outside S, that state would be reachable, contradiction. Thus after permutation the reachable block has no outgoing entries to the unreachable block. Restricting to it preserves alpha's mass1, the exact exits `omega_S=-T_SS 1`, and the entire transfer. The principal block is Hurwitz Metzler. If any state were unreachable, this would give the target with at most6 PH states, forbidden by the named B6 import.

Hence all7 states are reachable, without requiring that alpha itself have full support. The shifted nonnegative power series for exp(Tt) shows that a positive path from an initial state to state j makes `(alpha exp(Tt))_j` positive for positive t. Integrating gives

```
xi=(-T^T)^(-1)alpha^T>0.
```

Transience guarantees convergence. Zeros of alpha do not cause zero coordinates of xi once reachability is proved. Also

```
xi^T omega=alpha(-T)^(-1)(-T1)=alpha1=1.
```

This reconstructs the exact normalization used later; no arbitrary diagonal weighting is substituted for the actual occupation vector.

## 3. Actual reversed PH pair, transience, zeros and involution — LF35-55

With V=diag(xi)>0, define the literal displayed reversed data. Positive diagonal similarity of T^T preserves every off-diagonal nonnegative entry and every zero, and preserves all eigenvalues. Thus T_rev is Hurwitz Metzler. The occupation equation gives

```
T_rev1=V^(-1)T^T xi=-V^(-1)alpha^T=-omega_rev.
```

The initial mass is `omega^T V1=omega^T xi=1`. Both reversed boundaries are nonnegative; zero original exits or initial entries are permitted and are not divided by. Only xi is inverted, and its strict positivity has already been established. This is an actual transient PH pair with its true exit vector, not merely a transpose realization.

For transfer preservation, the resolvent similarity cancels V exactly:

```
alpha_rev(sI-T_rev)^(-1)omega_rev
 =omega^T(sI-T^T)^(-1)alpha^T
 =alpha(sI-T)^(-1)omega.
```

The final equality is transposition of a scalar. The characteristic polynomial is unchanged by transpose/similarity; the reduced target denominator is unchanged by the transfer identity. Therefore the monic hidden quadratic Q is unchanged as well, including multiplicities/coincidences.

One can check the claimed reversibility more sharply without any new hypothesis. The reversed occupation vector is

```
(-T_rev^T)^(-1)alpha_rev^T
 =V(-T)^(-1)omega=V1=xi.
```

Applying the construction twice therefore returns exactly T,alpha,omega before any block permutation. With the source's S,o,R reordering it returns the permutation-equivalent original pair. There is no loss of existence cases in either direction.

## 4. Every common block and all row ties — LF59-104

Before reordering, transpose the original R,o,S block matrix and apply the positive diagonal scalings. Reordering to S,o,R gives

```
[ V_S^-1 F^T V_S      xi_o V_S^-1 t             0
  xi_o^-1 f^T V_S     -lambda                  xi_o^-1 b^T V_R
  V_R^-1 D^T V_S      xi_o V_R^-1 r            V_R^-1 A^T V_R ].
```

These are exactly the SEVEN source block formulas. In particular D is transposed/rescaled and remains backward feedback; r and f exchange; b and t exchange. No zero-feedback assumption is introduced. Principal blocks remain Hurwitz Metzler by the same positive similarity/transpose argument, and their dimensions exchange.

The boundaries after the same reordering are exactly

```
alpha_rev=(omega_S^T V_S,0,0),
omega_rev=(0,0,V_R^-1 alpha_R^T)^T.
```

Writing `T^T xi=-alpha^T` in its THREE actual block rows gives precisely the source equations LF90,92,94. Multiplying them by `V_S^-1`, `xi_o^-1`, `V_R^-1`, respectively, proves all three displayed reversed row ties:

```
A_rev1+b_rev=0,
r_rev^T1+t_rev^T1=lambda,
D_rev1+f_rev+F_rev1=-omega_(S,rev).
```

The middle diagonal rate lambda is unchanged. These are matrix-entry identities, not merely an initial-mass normalization.

The reversed partition need not be the original canonical partition selected by a reachability proof. That does not invalidate its use here: it still has the exact common block zero pattern and boundary support, so initial-to-exit paths must cross the middle state, and the block determinant/transfer identities apply to these ACTUAL entries. No claim that arbitrary principal blocks can now be chosen WLOG is made.

## 5. Actual numerator factors and their scales — LF108-130

For polynomial adjugates, positive similarity gives `adj(sI-V^-1F^TV)=V^-1 adj(sI-F^T)V`, first by the ordinary inverse/determinant identity away from the roots and then by polynomial identity everywhere. Thus

```
N_(R,rev)
 =omega_S^T V_S [V_S^-1 adj(sI-F^T)V_S]
                    [xi_o V_S^-1 t]
 =xi_o t^T adj(sI-F)omega_S
 =xi_o N_S.
```

Similarly

```
N_(S,rev)
 =xi_o^-1 b^T adj(sI-A^T)alpha_R^T
 =N_R/xi_o.
```

The positive scale xi_o neither creates nor removes a leading coefficient. Therefore the product KQ is EXACTLY preserved and the two numerator degrees exchange. The principal characteristic polynomials exchange too. This is a true common-matrix equivalence, not a permutation of independently selected positive factors. No implication that Q divides either principal characteristic follows.

## 6. Complete nine-to-five reduction — LF134-148

The predecessor LF110-119 gives

```
m+n=6,
delta_R+delta_S=4,
1<=delta_R<=m, 1<=delta_S<=n,
deg N_R=m-delta_R, deg N_S=n-delta_S.
```

For m=1,2,3,4,5 the allowed delta_R values are respectively `{1}`, `{1,2}`, `{1,2,3}`, `{2,3}`, `{3}`. These give exactly NINE rows, matching all nine literal predecessor rows LF135-143. This small logical case split is written reconstruction, not a scientific enumeration program.

The actual reversal sends

```
(m,n,delta_R,delta_S,deg N_R,deg N_S)
 ->(n,m,delta_S,delta_R,deg N_S,deg N_R).
```

Its complete orbits, with the source's chosen representatives first, are:

| Representative (m,n;delta_R,delta_S;degrees) | Partner |
|---|---|
| (5,1;3,1;2,0) | (1,5;1,3;0,2) |
| (4,2;3,1;1,1) | (2,4;1,3;1,1) |
| (4,2;2,2;2,0) | (2,4;2,2;0,2) |
| (3,3;1,3;2,0) | (3,3;3,1;0,2) |
| (3,3;2,2;1,1) | itself |

This accounts for all9 rows without discarding an allocation. Both shortest lengths exchange because the actual boundary-supported principal paths are reversed; equivalently this follows from dimension exchange and the already reconstructed numerator-degree exchange.

For a degree1 numerator its leading coefficient is positive by its actual shortest-path term. Its constant coefficient is positive: the associated nonnegative principal resolvent transfer has a positive path, and its value at s=0 is positive for a Hurwitz Metzler block. Equivalently both factors have nonnegative values at0 and their product is `KQ(0)>0`. Thus each actual linear factor has a real strictly negative zero. The two1+1 representative rows therefore have two real negative hidden roots. A nonreal pair can only occur in one of the THREE2+0 representatives, on the chosen upstream side.

“Can only occur” is the necessary allowance proved here, NOT proof that every one of those three strata is feasible or contains a nonreal example. Those three rows also retain real-hidden possibilities. Nothing localizes the hidden eigenvectors or makes an Erlang/Jordan principal block universal.

## 7. Exact scope, import boundaries and non-conclusions

**New load-bearing steps NOT_RECONSTRUCTED: NONE.** Strict occupation positivity, all zero-entry/transience issues, involution, all seven actual block formulas, all PH row/exit ties, numerator scales and the complete9-to5 allocation reduction have written derivations above.

**Named imports not re-proved:** topology-unrestricted B6 (`8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`); dominator theorem (`5e259982c3fe8f762acc0546080aa87afec405e0cbc34b00afc460f01b39f846`); shared identities/relative-degree table (`941ea246ba96e00e820021733b0d716e79cc103807a86f97ee5b31dfabf5b969`). The table's actual LF108-147 was read and reconstructed at its relative-degree/common-block boundary. These imports retain their existing written assurance, not formal or independent primary-source authentication.

**Supported at this scope:** unrestricted PH7 existence for the frozen target is equivalent to a feasible actual conic fiber in one of the FIVE representative strata; only THREE allow a nonreal hidden pair. The same-Metzler-block, boundary, feedback and row-tie requirements remain intact.

**NOT supported:** a witness or impossibility at8/9; new upper7 beyond the prior cubic endpoint; a selected principal block WLOG; a universal separator for even one whole free-block stratum; a hidden quadratic substituted for an upper8 hidden cubic; any formal/kernel/human/cross-vendor/novelty or executable-certificate acceptance. The8/9 minimum remains{7,8}. No earlier unadmitted computation was rerun or credited, and the scientific HOLD/deadline remain unchanged.

No mathematical finding requires an author repair in this frozen packet. This0F/0M/0m is only the reconstructed written scope above, not full-target or process/novelty acceptance.
