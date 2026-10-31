# F873 author candidate: exact p=7 selector classes and unrun actual-word corroborator

## Status and exact scope

**Author candidate; not a finite-run result or parent disposition.** The new standalone standard-library source `actual-selector-offset-p7-v1.py` is **UNRUN**. The parent supplied its administrative SHA256 `6e060cc38d2a059739b1fd1e3247b41cba5d0dc9e7064e5c8327fc55d7857a20` (23,898 bytes, 581 LF), without executing it or granting a GO. Parent full-source reading and a separate named one-shot GO are prerequisites to any execution. No checker PASS, numerical program output, independent review, human or formal acceptance, priority, publication, or theorem outside the scope below is claimed.

The complete finite mathematical domain is p=7, actual original linear words in `D_14 = F_7 ⋊ {0,1}`, with `(x,e)(y,f)=(x+(-1)^e y,e+f mod 2)`, exactly 19 reflection occurrences, at least eight rotation occurrences, and at most one actual rotation in each original cyclic reflection gap. The cyclic reflection projection has one run of nine equal exponents and ten singleton runs, and its true rich-window count H is at most three. A selected identity subsequence has length 14 in **original occurrence order**. A rotation of exponent zero is an actual occurrence, not absence. The implementation enumerates **all increment patterns** in this domain after the harmless common-label normalization below. It does **not** enumerate all assignments of physical rotation gaps and exponents: actual-word/offset/DP corroboration is restricted to the three deterministic eight-rotation scenarios for each recorded representative and to the author witness. No primes other than 7 are tested.

The p=7 refinement in §2 is written reasoning, pending independent checking. The numeric enumeration totals in §3 are independently derived here, not presented as program output. They are also hard-coded as checks in the unrun source. Neither the numeric totals nor the presence of a complete verifier is an executed finite corroboration.

## 1. Actual closure, true H, and the phase geometry

Let the nine run occurrences be `A_1,...,A_9`, with common exponent `a`, and the ten outside occurrences be `b_1,...,b_10`. Set `x_0=a`, `x_i=b_i` for `1<=i<=10`, and `x_11=a`; put `d_i=x_i-x_(i-1)` in `F_7`. Exactly this run type is equivalent to

`d_1,...,d_11 != 0`, `sum_i d_i=0`.

Indeed each of the ten singleton adjacencies and the two boundary adjacencies is unequal, and conversely these inequalities leave exactly the eight equal edges within the nine-run. Nonadjacent labels may coincide. A triple centered at `b_i` has difference set `{-d_i,-d_i-d_(i+1),-d_(i+1)}` and is rich if and only if `d_i != d_(i+1)`. All triples centered inside or at either end of the nine-run have a repeated adjacent label. Therefore

`H = #{i in {1,...,10}: d_i != d_(i+1)}`.

There is **no** extra comparison of `d_11` with `d_1`: the physical intervening run is nine equal reflections. For H=h, the unique increment presentation has h change positions among `{1,...,10}`, h+1 positive segment lengths summing to 11, nonzero adjacent-distinct segment values, and the actual closure equation `sum length_j*value_j=0`. No cyclic quotient of the 11 increment positions is taken. A common change of every reflection label to `x-a` preserves the exponent of every even-reflection subsequence: the alternating coefficients of the common shift sum to zero. Thus normalization `a=0` retains the identity question while the checker still constructs actual words and physical gaps.

For phase `j=1,2,3`, omit the **occurrence** `A_j`, cut immediately after it and form six chronological triples from the remaining reflections. Exactly two triples are constant. A rich center `b_i` belongs to phase `j ≡ i+1 (mod 3)`, so `r_1+r_2+r_3=H`. The checker independently reconstructs the 19 cyclic reflection labels, the true cyclic rich windows, all three actual block partitions and their phase counts. In particular, a same-residue collision is precisely `max_j r_j>=2`. The gap after the omitted occurrence and the gap before it remain two different physical gaps.

## 2. Sharp p=7 direction classification for the restricted triple family

Fix any phase and any actual eligible pair Q of distinct rotations: protect the interiors of `min(r,2)` rich triples, forbid the at-most-one unsafe interior gap in a nonconstant triple, and select at most one interior rotation per triple. At most five physical gaps are forbidden. At least three of the eight or more actual rotations survive, and a pair with the stated block condition exists. In a nonconstant nonrich triple, the usable two-value local set is a translate of `{0,d}` for its nonzero direction class `±d`; this remains true with a safe selected interior rotation. Protected rich triples retain their actual three-value difference sets. Constant blocks contribute at least one actual value, possibly two. These statements do not invent any free rotation offset.

For each eligible Q, first choose one actual value from each constant block. With these values fixed, the following classification is **necessary and sufficient for that fixed-value restricted sumset to be all of F_7**, not merely a sufficient direction test. Allowing both constant values can enlarge the union, so a failure in the list is not an avoiding-word assertion.

* `r>=2`: the fixed-value sumset is all seven residues.
* `r=0`: four nonrich directions occur. If all four are one sign-class `±d`, the sumset has exactly five elements. If exactly three are `±d` and the fourth is `±2d`, it has exactly six. In all other direction patterns it has all seven.
* `r=1`: three nonrich directions and the rich three-set `T` occur. If all directions are `±d` and `T={t,t+d,t+2d}`, the sumset has exactly six elements. Otherwise it has all seven.

Proof. For nonempty subsets of `F_7`, repeated `|A+B|>=min(7,|A|+|B|-1)` applies; S1 includes its finite-grid interpolation proof. Briefly, if `N=min(6,|A|+|B|-2)` and the sumset had at most N elements, the product over an N-element containing set would vanish on a suitable grid although its relevant top coefficient is a nonzero binomial coefficient of degree below 7. Two distinct sign-classes give four sums of their two pairs. When `r>=2`, two three-sets and the remaining nonconstant pairs contribute at least `1+2+2+1+1=7` in the Cauchy--Davenport size accounting. When `r=0`, two disjoint unequal-class pairs yield `4+4-1=7`; such pairs exist unless one class has at least three of the four entries. Four common directions give `{0,1,2,3,4}d`. For a 3+1 split, after translation/orientation the three common pairs give `{0,1,2,3}d`; adding the remaining pair gives six residues for `±2d` and seven for the only other nonzero sign-class, `±3d`. When `r=1`, two unequal directions give four elements, and the remaining pair and T force `4+1+2=7`. With a common direction, a consecutive T plus three pairs is a six-point interval; a nonconsecutive T has at least two components in the d-cycle, so `|T+{0,d}|>=5`, and the remaining two pairs force seven.

For `u,v != 0`, `u != v`, and `T={-u,-v,-u-v}`, the condition that T is a three-term progression of step `±d` is exactly

`(u=2v and d=±v) or (v=2u and d=±u) or (v=-u and d=±u)`.

This follows by testing each of the three possible midpoints. It is checked in the proposed source for every generated rich triple and each of the three sign-class representatives `d=1,2,3`.

### Actual-offset identities

For a bad phase and eligible actual rotation pair Q, orient each usable nonrich pair as `{b_i,b_i+d}`; in the 3+1 exceptional case orient the one outlier as `{b_e,b_e+2d}`. If `r=1`, orient the protected rich set as `{b_T,b_T+d,b_T+2d}`. Let `B(Q)` be the sumset of the actual boundary-gap rotation exponents, all these bases, and **all actual** values supplied by the two constant blocks. Then the complete restricted-family support is exactly

* `B(Q)+{0,1,2,3,4}d` in the uniform `r=0` case; zero is absent iff `B(Q)⊆{d,2d}`;
* `B(Q)+{0,1,2,3,4,5}d` in either the `r=0` ±2d-outlier case or the `r=1` uniform/progression case; zero is absent iff `B(Q)⊆{d}`.

Each inclusion is for that particular actual Q. The two physical end gaps are separate boundary occurrences; a selected nonzero rotation inside a constant triple gives actual alternatives `{y,-y}`, not an invented cancellation. These are exact statements for the restricted family and necessary conditions for avoidance, not sufficient conditions for avoidance by the whole original word. The proposed actual-word checks compare the explicitly built full restricted support and the `B(Q)` formula for each eligible Q in the listed representative scenarios.

For unrestricted selection of one omitted reflection within a triple `(a,b,c)`, including two actual rotations in its two internal gaps if present, the chronological local values are

`{ b-c+u-v, a-c-u-v, a-b-u+v }`,

where a missing rotation has numerical exponent zero but is not counted as a selected occurrence. A boundary selected rotation has plus sign because each complete triple contributes two reflections. The proposed source multiplies the actual local occurrences independently of this formula and checks equality; it reconstructs any zero-sum local path into actual original-order occurrences. The global DP separately counts **all** length-14 identity subsequences, not only this triple family.

## 3. Written enumeration totals, independent of execution

For `h=0,1,2,3`, the number of segment-length/value templates before closure is respectively `6`, `10*6*5=300`, `45*6*5^2=6,750`, and `120*6*5^3=90,000`: total `97,056`. The closure-valid counts claimed by this written derivation are

| Actual H | Closed increment sequences, with the nine-run anchored and a=0 |
|---:|---:|
| 0 | 0 |
| 1 | 48 |
| 2 | 972 |
| 3 | 12,744 |
| **Total** | **13,764** |

Derivation. H=0 would give `11d=4d=0` with `d!=0`, impossible. For H=1, the change position k gives `k u+(11-k)v=0`. Positions k=4,7 force a forbidden zero slope; the other eight positions each admit six nonzero u and a unique distinct nonzero v, giving 48.

For H=2 or 3, count closure first with all h+1 slopes nonzero, then exclude equality of adjacent slopes by inclusion-exclusion. For k nonzero coefficients, the number of nonzero assignments solving their zero sum is `T_k=(6^k+6(-1)^k)/7`; equivalently `T_1=0` and `T_k=6^(k-1)-T_(k-1)`. Thus `T_2=6`, `T_3=30`, `T_4=186`. A coefficient 0 mod 7 contributes a free factor 6. There is at most one zero coefficient because the segment lengths are positive and total 11. The all-equal slope case never closes because `11≡4`.

For three segments, there are 45 length compositions, nine having one length 7: the all-nonzero-slope closure count is `45*30+9*6=1,404`. Each of the two adjacent-equality events has `45*6-9*6=216` solutions in aggregate: the nine exceptions are where one of the two merged coefficients is 0 mod 7. Their intersection is empty, so `1,404-2*216=972`.

For four segments, there are 120 length compositions, 12 having one length 7; the all-nonzero-slope closure count is `120*186-12*6=22,248`. Across the three single adjacent-equality events, a merged three-coefficient system has one zero coefficient in 72 composition/event incidences: 24 per edge, of which 18 have the merged segment length 7 and six have an unmerged length 7. Their aggregate is `3*120*30+72*6=11,232`. Across pairs of equality events, the two-coefficient system has a zero coefficient in 72 incidences: 18 for each adjacent-edge pair and 36 for the two disjoint edges. Their aggregate is `3*120*6-72*6=1,728`. The triple intersection is empty. Hence `22,248-11,232+1,728=12,744`. These counts distinguish anchored increment sequences, not rotation-equivalence classes of entire words.

## 4. Actual witness and proposed verification

The packet's explicit witness has increments `(4,1,1,1,2,2,2,2,2,2,2)`, whose sum is 21, and outside reflection labels `(4,5,6,0,2,4,6,1,3,5)`. The only true changes are at i=1 and i=4, both in phase 2. Put an actual zero-exponent rotation after each `A_1,...,A_8`. The selected reflections are `(A_3,A_4),(A_6,A_7),(A_9,b_2),(b_3,b_5),(b_6,b_8),(b_9,b_10)`, together with rotations after `A_3,A_6`. Their original-order exponent is `0+0+2+4+3+5=14=0` mod 7 and the reflection parity is even. This is a written actual 14-occurrence identity selection; it is not a run receipt.

The source enumerates all 97,056 templates, reconstructs every closure-valid actual reflection projection and phase, counts H/rich-phase vectors, signed direction multisets, and phase classifications, and checks the direct finite-field sumsets and rich-progression identities for each. It records deterministic first representatives for every observed rich-phase profile and every observed direction case. For each representative it builds three specified actual eight-rotation gap/exponent arrangements and linear token shifts, checks every pair of the eight rotations in each of the three phases, verifies the restricted offset formula on each eligible pair, and constructs explicit identity subsequences whenever its local full-family support contains zero. Its independent semidirect group DP counts all length-14 identity selections, stratified by selected rotation count, and compares each word with its unshifted cyclic cut. The DP does not assume that every word passes a triple-family test or that every representative must have positive DP count.

The source contains intended-reason controls for zero increment, too many actual changes, closure, the spurious wrap change, wrong rich phase, duplicate physical gap, too few rotations, wrong selection length, wrong group product, swapped noncommutative group order, local rotation sign, dropped boundary offset, unsafe gap, and discarded constant-block choice. A control accepts only its named `CheckFailure`, not an arbitrary exception. These are **prepared controls, not passed controls**. All enumeration checks the monotonic 40-second deadline; a single-process 55-second SIGALRM is a second guard. JSON-line progress is flushed, and a recognized timeout returns `INCOMPLETE_TIMEOUT`, not PASS. A run may time out before complete coverage; partial output would not support full enumeration. The numerical totals, the checker design, and its runtime behavior all remain subject to parent review and a separately authorized run.

## 5. Reads, imports, and limitations

Before mathematical body reading/reasoning, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and **all 22** manifest-listed status-only controls; I wrote `prebody-ack-v1.md` and sent the acknowledgement directly to Main. Initial compact displays of the five administrative records elided lines; I recovered them with complete raw reads before the acknowledgement. I also read the general memory summary, written-math protocol and finite-witness protocol; none was used as a mathematical premise. The memory summary itself reported truncation, irrelevant to the scoped mathematical inputs.

After the acknowledgement I read the sole literal packet, parent-pinned SHA256 `e111ad17a59fd3d0de15c33a45f11fd0a1a7096f6b0f4fcf514afd3bddb18f45`, completely in order in raw windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220 and 221–234, including the ending. Every window was at most 20 LF, each displayed well below 30,000 bytes; no packet clipping was observed and no packet recovery was needed. These windows include all of S1, f849 author candidate LF 1–186, parent-pinned SHA256 `f73071bc6938c20a7f6b2be5f99b76f686b54fb6aef44c34ce0670950e85cfbb`, and S2, parent disposition LF 1–38, parent-pinned SHA256 `e1931d621a04153d8b90bf5cf25220ad8baee57b7758a826e047472cfd143f00`. Pin values are parent metadata, not independently computed hashes by this worker.

S2 links the f603 author body, f638/f639 review bodies, and f640 narrative, source and run receipt. None of those linked bodies was opened; any invocation of their separate proof details, checker behavior or independent dispositions would be a **named conditional import**, not a result established here. This candidate instead uses the literal S1/S2 packet and the written arguments above. All genuine held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. No peer scientific body, linked unlisted source, network, external model, scientific code execution, test, compiler, solver, or child subprocess was used. The output names were absent in the initial owner-only directory listing; the available write tool does not provide an atomic exclusive-create guarantee. No clean-cognition or historical-nonexposure certification is claimed.

The exact remaining obligation is unchanged: a word for which all restricted selector/offset criteria fail may still have an identity selection in another triple family, with a different pair of rotations, or with zero/four/more rotations. Deciding that all actual words in this residual have positive length-14 identity DP, or exhibiting a valid actual word with zero DP, requires additional work. No avoiding word, all-prime result, unrestricted ordered-Olson theorem, original-source correspondence or novelty is claimed here.
