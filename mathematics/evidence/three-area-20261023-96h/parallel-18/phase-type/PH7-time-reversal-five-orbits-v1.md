# PH7 at8/9: Markovian time reversal and five complete shared-block representatives

Actual returned `/bin/date` before this freeze: **Sun Oct 25 04:29:39 PDT 2026**. MathResearch96h, math-1. Written-only primary work AFTER completing v30-B. No scientific interpreter/eval, arithmetic program, enumeration, replay or solver. Metadata clocks/source reads only. New packet; pinned predecessors untouched.

## 1. Exact advance and explicit limits

The preceding conic-fiber representation left nine integer degree allocations. A materially different representation—PH time reversal with its ACTUAL positive occupation measure—identifies complete cases in pairs without deleting backwards feedback or assuming a free exit. This reduces the unrestricted8/9 existence question to FIVE representative degree allocations, only THREE of which can contain a nonreal hidden pair.

This is a genuine equivalence, not a search miss or a restriction to real hidden roots. It does NOT decide whether any representative fiber is feasible; the minimum remains{7,8}. It does not extend the candidate exact7 interval beyond its cubic endpoint.

Named written imports:

- B6, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`: all PH orders≤6 excluded for z>1/2.
- Dominator form, `PH7-dominator-normal-form-v1.md`, SHA256 `5e259982c3fe8f762acc0546080aa87afec405e0cbc34b00afc460f01b39f846`.
- Shared identities and complete nine-row allocation table, `PH7-dominator-shared-block-identities-v1.md`, SHA256 `941ea246ba96e00e820021733b0d716e79cc103807a86f97ee5b31dfabf5b969`.

The positive occupation/time-reversal argument is reconstructed below rather than cited as a new discovery. Novelty remains UNCLEAR; this is an unreviewed WRITTEN candidate.

## 2. Why the occupation vector is strictly positive here

Suppose an ACTUAL PH7 pair(alpha,T) realizes the target at8/9. All states are reachable from supp(alpha): otherwise remove the unreachable states, retaining the literal PH row/exit ties on the reachable block, to obtain the same law with at most6 states, contrary to B6.

Define the column

`xi=(-T^T)^(-1) alpha^T = integral_0^infinity exp(T^T t)alpha^T dt`.

T is Hurwitz Metzler, so the integral exists and is nonnegative. Reachability makes every coordinate strictly positive: a positive path from an initial phase gives a strictly positive semigroup entry and hence a positive integral. Thus every diagonal entry of V=diag(xi) is positive. There is no unsupported assumption of a full-support initial row.

Since omega=-T1,

`xi^T omega=alpha(-T)^(-1)omega=alpha1=1`.

## 3. Literal reversed PH pair

Define

`T_rev=V^(-1)T^T V`,

`alpha_rev=omega^T V`,

`omega_rev=V^(-1)alpha^T`.

All off-diagonal entries of T_rev are nonnegative. It is Hurwitz by similarity to T^T. Its actual row sums are

`T_rev1=V^(-1)T^T xi=-V^(-1)alpha^T=-omega_rev≤0`.

The reversed initial row is nonnegative and sums to `omega^T xi=1`. Thus this is a literal PH7 pair, not a transpose with an independently assigned exit vector. Moreover

`alpha_rev(sI-T_rev)^(-1)omega_rev`

`=omega^T(sI-T^T)^(-1)alpha^T`

`=alpha(sI-T)^(-1)omega`.

The distribution, all reduced poles and the hidden quadratic Q are exactly unchanged. Reversal is invertible at the existence level, and applying it twice returns an equivalent original pair.

## 4. All actual common blocks and boundary ties under reversal

Write the imported original form as

```
T=[ A     b       0
    r^T  -lambda  t^T
    D     f       F ],
alpha=(alpha_R,0,0), omega=(0,0,omega_S)^T.
```

Split xi=(xi_R,xi_o,xi_S), with V_R=diag(xi_R), V_S=diag(xi_S). Reorder the reversed pair as old S,o,R. Then its blocks are EXACTLY

```
A_rev = V_S^(-1) F^T V_S,
b_rev = xi_o V_S^(-1) t,
r_rev^T = xi_o^(-1) f^T V_S,
t_rev^T = xi_o^(-1) b^T V_R,
D_rev = V_R^(-1) D^T V_S,
f_rev = xi_o V_R^(-1) r,
F_rev = V_R^(-1) A^T V_R.
```

Its boundaries are

`alpha_(R,rev)=omega_S^T V_S`,

`omega_(S,rev)=V_R^(-1)alpha_R^T`.

Every nonzero feedback is retained with a positive scaling. D is transposed and rescaled, not discarded. r and f trade roles; b and t trade roles. The principal blocks remain Hurwitz Metzler, with their dimensions exchanged.

The occupation equations T^T xi=-alpha^T give, block by block,

`F^T xi_S+t xi_o=0`,

`b^T xi_R-lambda xi_o+f^T xi_S=0`,

`A^T xi_R+r xi_o+D^T xi_S=-alpha_R^T`.

They imply all THREE exact reversed PH ties:

`A_rev1+b_rev=0`,

`r_rev^T1+t_rev^T1=lambda`,

`D_rev1+f_rev+F_rev1=-omega_(S,rev)`.

No row-sum condition has been replaced by a scalar normalization heuristic. The reversed block partition is a valid shared-block form, even if one does not reselect the canonical reachable set used in the original dominator proof.

## 5. Actual numerator factors exchange, with their true scales

Let original principal characteristics be a_R,a_S and actual boundary numerators

`N_R=alpha_R adj(sI-A)b`,

`N_S=t^T adj(sI-F)omega_S`.

Similarity and transpose identities for the adjugate give

`a_(R,rev)=a_S`, `a_(S,rev)=a_R`,

`N_(R,rev)=xi_o N_S`,

`N_(S,rev)=N_R/xi_o`.

For instance the first numerator becomes

`omega_S^T V_S [V_S^(-1)adj(sI-F^T)V_S]`

`*[xi_o V_S^(-1)t]`

`=xi_o omega_S^T adj(sI-F^T)t=xi_o N_S`.

The second is its analogous transpose calculation. Thus their product remains KQ and their degrees exchange EXACTLY; one has not merely exchanged two independently chosen positive scalar factors. The hidden eigenvalues still need not lie in either principal block.

## 6. Five complete representatives

The complete predecessor table has total numerator degree2. Pair every row with the actual time-reversed row. One may choose the following FIVE representatives, with the shortest pre/post edge lengths retained:

|m|n|delta_R|delta_S|deg N_R|deg N_S|
|---:|---:|---:|---:|---:|---:|
|5|1|3|1|2|0|
|4|2|3|1|1|1|
|4|2|2|2|2|0|
|3|3|1|3|2|0|
|3|3|2|2|1|1|

The paired missing rows are respectively (1,5;0,2), (2,4;1,1), (2,4;0,2), and (3,3;0,2), where the last two displayed entries denote numerator degrees. The balanced3+3/1+1 row is self-dual. This pairs the entire old nine-row table; no degree allocation is silently dropped.

The two1+1 rows have two negative REAL hidden roots because both actual linear numerators have positive coefficients. Therefore a nonreal hidden quadratic can occur only in the THREE2+0 representatives, upstream in each chosen orientation. Both real and nonreal roots remain allowed in those three rows. This is not a claim that every real-hidden case is1+1, nor a claim that Q divides the upstream principal characteristic.

At the conic-fiber interface, unrestricted existence is therefore equivalent to a nonempty admissible fiber in at least one of these five representative strata. A universal exclusion need cover these five only, but must still range over ALL their actual principal matrices, boundaries and feedback entries. A single Erlang/Jordan-rate slice is not made universal by the reduction.

## 7. Exact remaining gap and evidence boundary

No new scientific program or arithmetic check supports this packet; it is written matrix/transposition algebra with the explicit positive occupation normalization. Its new contribution is the complete reversal-equivariant reduction, not another holding-rate increment or sampled empty slice. It requires independent written reconstruction at the named B6/normal-form/shared-table imports.

The first unresolved8/9 step is now: find actual outer data giving a feasible conic fiber in ONE of these five representatives, or prove a uniform separator across ALL five. Neither is proved here. The candidate band through zeta and earlier slice certificate retain the mandatory resumption-arithmetic authorization addendum; no historical computation is rerun or given retroactive GO. The frozen deadline and global scientific HOLD remain unchanged.
