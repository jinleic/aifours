# Census/composition candidate v1 — every support48 officer/hole/excess configuration

Actual returned `/bin/date` before creation: **Sun Oct 25 07:13:01 PDT 2026**. PhysicsAME46-2, physics-6. **WRITTEN complete scalar census and composition candidate at explicitly named existing exclusions. Fresh independent reconstruction/parent disposition of THIS global case assembly is not performed.** No scientific interpreter/eval, arithmetic/symbolic program, enumeration, certificate replay, solver, simulation, native scientific job, external-model CLI or nested agent was used. Metadata clocks/hashes and source reads only. Parent errata v7–v8 and HOLD remain binding. Every earlier pinned artifact stays unchanged.

## 1. Exact result and an important identity correction

The census is for arbitrary-complex normalized AME(4,6), every product orthonormal basis, with EXACT support s=48. It does NOT assume e0, closed2x2 components, equal original moduli or a common support-minimizing basis.

The correct universal identity in EVERY pair direction is

    s=t+2h+e,   h=36-t,   e=s-(72-t).

The shorter equality `s=t+2h` holds ONLY when e=0. It cannot be imposed on every support48 stratum. Conversely e is NOT a separately selectable parameter for different cuts: all six pair directions have the SAME global t,h,e, derived from the SAME actual support and coefficients. Sections2–4 prove these facts and state the full global feasibility predicate.

At s48 the necessary nonnegative scalar relations give exactly THIRTEEN triples. Matrix-capacity and universal written obstructions reduce them to five. Removing the newly closed t24/h12/e0 point leaves exactly FOUR positive-excess candidates. All four already have an explicit historical CORRECTNESS-ACCEPTED exclusion at their exact parameters, read in this task. Therefore the current census residual at those named imports is EMPTY.

This is a NEW global parameter-composition candidate, not an independent rerun of the historical finite certificates or an already accepted numerical lower49 declaration. It identifies no genuinely open positive-excess parameter to attack again. A fresh composition gate is required before changing a numerical frontier.

## 2. Intrinsic officers and the exact per-pair-direction equations

Put A=6psi. Define the GLOBAL sets

    T={x:|A_x|=1},   t=|T|,
    N=supp(A) minus T,   n=|N|=s-t.

For each two-party set P of coordinates and its complement Pc, the36x36 flattening M_P has

    rho_P=M_P M_P^dagger/36,
    rho_Pc=(M_P^dagger M_P)^T/36.

All six marginals give both products I36 in the three complementary cuts. In particular every pair-value line has squared A-norm1.

An entry of modulus1 exhausts EVERY pair line through that tensor position. Distinct officers cannot share a pair-value line. A singleton pair line has coefficient of modulus1, so is necessarily an officer. Thus the officer set is INTRINSIC to the coefficient tensor; there are not six different officer counts chosen by flattening.

For EACH of the six P and each of its36 pair values ell:

- Officer line: exactly ONE T point and ZERO N points; coefficient squared modulus1.
- Hole line: ZERO T points and k_(P,ell)>=2 N points; their positive squared moduli sum to1.
- No pair line is empty.

The projection of T to every P is injective, of cardinality t. Hence every P has EXACTLY

    h_P=36-t=h

hole lines, not merely at most h. Every N position belongs to exactly one P line, so

    sum_(ell in H_P) k_(P,ell)=n,
    e_P:=sum_(ell in H_P)(k_(P,ell)-2)=n-2h.

The right side contains only global quantities. Consequently

    e_P=e for ALL six P,
    n=2h+e,
    s=t+n=t+2h+e=72-t+e.

The row excess and column excess of one complementary cut each equal e. Adding those two budgets gives2e; it does NOT define a different global excess. Adding the budgets of all six directions gives6e, likewise not a new e. Individual degree profiles may differ across directions, but their sums cannot.

The SAME coefficients also imply the mass equations

    sum_(x in N)|A_x|^2=h,
    sum_(x in N on a hole line)|A_x|^2=1.

Thus n positive coefficients share total mass h. At e>0 their mean squared modulus is `h/(2h+e)<1/2`; one cannot simply apply the e0 equalization/2x2 phase theorem to them.

## 3. Shared cut graphs, local excesses and actual quantum feasibility

### 3.1 Three cuts, not independent supports

After individually ordering officer rows/columns first in a given cut P|Pc, M_P consists of t isolated unit-modulus entries and one h-by-h N block U_P. That block is unitary in BOTH products and contains ALL n N entries. Its row and column labels are the actual hole pair values H_P,H_Pc. Its bipartite support graph is SIMPLE: a row-pair/column-pair label specifies ONE physical tensor position.

Therefore

    n<=h^2                                                   (CAP)

in every cut. Its n edges have row degrees k_(P,ell) and column degrees k_(Pc,ell), each at least2, with both excess totals equal e. A row-support intersection of exactly one column would give a single nonzero inner-product term and is forbidden; the corresponding column statement is also required.

The three U_P are NOT unrelated matrices: their entries are the SAME physical A_x at the SAME N positions, reshaped in three ways. A choice of separately feasible degree graphs or independently assigned rectangles does not establish a tensor.

### 3.2 Unit components and exact excess budgets

Each connected non-officer component has q row vertices and q column vertices. Indeed its row vectors are orthonormal in its column space, giving rows<=columns; the column argument gives the reverse. Its restricted matrix is unitary and all other entries in those rows/columns vanish.

If it has m nonzero entries, define delta=m-2q>=0. For each cut,

    sum_components q=h,
    sum_components m=n,
    sum_components delta=e.

A component with delta0 has every row of degree2. Any row meeting a two-entry row must share BOTH its columns by orthogonality; connectedness then forces a closed2x2 block. Conversely a non-officer2x2 component has all four entries and delta0.

Delta1 is impossible. If a component had one row of degree3 and all others degree2, every two-entry row connected to that row lies within its three-column support; a disjoint two-entry pair would form a separate component. Hence the component has exactly three columns/rows. The other two row supports are equal two-subsets (they cannot overlap in exactly one column). The third column is a singleton of modulus1, forcing its row to be an isolated officer, contradiction. This is the universal L42 Lemma7 argument, not an e0-only fact.

Thus e1 is impossible in ANY cut and ANY state. Positive component excesses are at least2. For e>0, however, larger square unitary components are permitted in principle; closed2x2 structure for the ENTIRE N block must not be inferred.

### 3.3 Coordinate slices retain a common local excess, too

For a local value a at party i, let t_(i,a) be its officer count and d_(i,a)=6-t_(i,a). Positive deficits are at least2, sum_a d_(i,a)=h, and d_(i,a)<=v_j for every other party j. An inactive value has no N coefficient.

For a positive-deficit value define

    n_(i,a)=#{x in N:x_i=a},
    epsilon_(i,a)=n_(i,a)-2d_(i,a)>=0.

For EACH partner j, the d_(i,a) officer-free partner lines partition that slice, so

    epsilon_(i,a)=sum_(b in D_j^(i,a))(k_(ij,(a,b))-2).

This same slice excess is therefore shared by ALL THREE partner directions. Moreover

    sum_a epsilon_(i,a)=e for EVERY party i,
    sum_(x in N:x_i=a)|A_x|^2=d_(i,a).

Only at e0 do all these local epsilons vanish and all slice cardinalities equal2d. For positive excess a slice may have EXTRA N sites. None is discarded by the census.

### 3.4 Exact feasibility predicate, not a degree relaxation

A candidate triple(t,h,e) is quantum-feasible precisely if there exist ONE disjoint pair of literal sets T,N in{0,...,5}^4, with cardinalities t and n, and ONE complex coefficient tensor A, satisfying:

1. |A_x|=1 on T,0<|A_x|<1 on N, and zero elsewhere.
2. The three actual reshapes12|34,13|24,14|23 satisfy BOTH `M M^dagger=I36` and `M^dagger M=I36`.
3. h=36-t and e=n-2h, with the degree/mass/slice counts derived above from these SAME sets and coefficients.

Necessity was proved above. Sufficiency is literal: put psi=A/6. Unitarity gives total squared A-norm36, so psi is normalized, and the displayed partial-trace formula gives ALL SIX marginals I36/36. This predicate is not replaced by a scalar census, weighted line norms alone, one-body conditions, one-cut unitarity or independent support graphs.

The finite scalar census below is a COMPLETE list of possible parameters for that exact predicate, not a claim that every listed row satisfies it.

## 4. Freeze the complete s48 scalar census FIRST

Because t officers project injectively into36 pair values,0<=t<=36. The common excess is nonnegative. At s48,

    h=36-t,   e=t-24,   n=48-t=h+12.

Thus24<=t<=36. The complete algebraic candidate list is:

|t officers|h hole lines in EACH pair direction|e COMMON excess|n SAME N sites|Status of the scalar row|
|---:|---:|---:|---:|---|
|24|12|0|24|New complete e0-layer disposition|
|25|11|1|23|Universal delta1 obstruction|
|26|10|2|22|Historical positive-excess exclusion|
|27|9|3|21|Historical positive-excess exclusion|
|28|8|4|20|Historical positive-excess exclusion|
|29|7|5|19|Universal officer-moment obstruction|
|30|6|6|18|Historical positive-excess exclusion|
|31|5|7|17|Universal partner/profile obstruction|
|32|4|8|16|Universal binary four-qubit obstruction|
|33|3|9|15|CAP:15>9|
|34|2|10|14|CAP:14>4|
|35|1|11|13|CAP:13>1|
|36|0|12|12|CAP:12>0; no N row/column exists|

These are THIRTEEN solutions of the nonnegative scalar equations, NOT thirteen alleged actual states. CAP immediately deletes h0,1,2,3, leaving exactly nine rows with h4,...,12. In particular no Tarry import is required to eliminate t36 AT s48: its purported twelve N entries have no possible hole row/column. The t36/s36 classical-officer issue is a different question and is not confused with this census.

This establishes the requested COMPLETE parameter universe before attempting a nearest case. It includes every positive-excess row, not just the already closed t24 point.

## 5. Universal all-excess exclusions among the nine capacity-compatible rows

The following are actual all-excess statements, not uses of an e0-only module theorem. Their written sources were read at the exact scopes cited in Section8.

### 5.1 t25/h11/e1

Section3.2 proves delta1 impossible and e is the sum of component deltas. A nonnegative sum with no delta1 cannot equal1. This excludes the nearest positive-excess row. Its apparent one-degree3/rest-degree2 pattern cannot be a unitary non-officer block. No support-search miss is used.

### 5.2 t31/h5/e7

Positive deficits are at least2 and sum5 on each axis. Each axis therefore has profile{5} or{3,2}, hence active size at most2. Some positive deficit is at least3, but every deficit is bounded by every other active size, at most2. Contradiction. This is L46 Lemma13 for EVERY e; it does not extrapolate a small-support-only case table.

### 5.3 t29/h7/e5

Each axis has at most three positive deficits, so the partner bound makes every deficit at most3. Parts in{2,3} summing7 can only be{3,2,2}; all four active sizes are3.

For officers, actual singleton/pair incidence counts give

    kappa1=6*12-4*7=44,
    kappa2=6*9-6*7=12.

The pointwise nonnegative integer polynomial(c-1)(c-2)/2 has sum

    kappa2-kappa1+t=12-44+29=-3,

impossible. This is the all-e t29 obstruction in L48, not an e0 parity inference.

### 5.4 t32/h4/e8

The deficit profile on an axis is{4} or{2,2}. A{4} value would require at least four active values at every other axis, whereas each has at most two. Hence every axis has{2,2}, and N lies in a2x2x2x2 product cube.

In every pair direction the four hole labels are ALL pairs in its two selected local alphabets. Thus each of the three N blocks is an ACTUAL4x4 unitary matrix, not just a support projection. Here n16 even fills the binary cube, but density alone is not the contradiction.

Restrict psi to that cube and normalize omega=3psi_N. The N A-mass is h4, so omega has norm1. The reshapes of2omega are exactly those three unitary4x4 blocks. Therefore ALL SIX two-qubit marginals are I4/4, contradicting the standard no-AME(4,2) theorem proved in L46 Lemma15 (Pauli weights A1=A2=0,A3=12,A4=3 give negative overlap -1/2 with a positive spin-flipped state). This is L46 Lemma16's EVERY-e scope; it does not assume exact-two hole lines at e8.

After these universal obstructions, the scalar residual is exactly

    C5={(24,12,0),(26,10,2),(27,9,3),(28,8,4),(30,6,6)},

where coordinates are(t,h,e). No other officer/hole/excess point survives this written census filter.

## 6. Diff against the newly closed e0 point: FOUR precise positive-excess configurations

The complete current parent record `ame-t24h12e0-layer-complete-parent-v1.md` excludes exactly(24,12,0), with ALL active alphabet configurations. It is not asserted to settle a positive-excess point by itself.

Subtracting that point from C5 leaves

    R_after_e0={(26,10,2),(27,9,3),(28,8,4),(30,6,6)}.

These are the only candidates one might otherwise try next. Their global invariants are:

|New triple(t,h,e)|Historical notation(t,e)|n|Total squared A-mass on N|Mean squared N coefficient|
|---|---|---:|---:|---:|
|(26,10,2)|(26,2)|22|10|5/11|
|(27,9,3)|(27,3)|21|9|3/7|
|(28,8,4)|(28,4)|20|8|2/5|
|(30,6,6)|(30,6)|18|6|1/3|

For EACH of six pair directions, exactly h hole lines partition these SAME n entries, with degrees `2+delta_ell`, nonnegative integer deltas summing to the displayed e, and each hole-line weight sum1. All three complementary h-by-h unitary graphs and their coordinate-slice budgets must come from one global tensor. The displayed mean is a mass invariant, NOT an equal-modulus hypothesis.

For each cut, positive component excesses partition e into parts at least2, with component rank sums h. Thus e2 has exactly one delta2 component plus possible closed2x2 components; e3 one delta3 component; e4 one delta4 or two delta2 components; e6 the corresponding partitions into parts≥2, still subject to rank/edge-capacity and all shared-position constraints. These are necessary structural invariants, not instantiated feasible supports or assertions that the partitions are sufficient.

The e0 joint-phase/equalization reduction must NOT be applied wholesale to these configurations. They can have higher-degree components and extra local N sites. The historical exclusions below explicitly use the positive-excess necessary support/officer constraints, not the e0-only W/doubled-triangle premise.

## 7. These FOUR configurations are ALREADY correctness-accepted as impossible

The COMPLETE actual historical parent record

    institute/runs/six-lane-2026-10-16/review/
    ame46-s48-e-positive-parent-verdict.md

was read. Its LF5 explicitly states:

> No AME(4,6) state has parameters(t,e)=(30,6),(28,4),(27,3)or(26,2).

These are EXACTLY all four members of R_after_e0 after converting h=36-t. Its LF35 marks the four partial parameter exclusions CORRECTNESS-ACCEPTED. LF20–25 bind all40 normalized profiles, all33 regenerated final CNFs and the historical addition-only RUP replay/controls. LF29 states that the e0-only W/Lemma20 is NOT used. LF23 records zero support witnesses/Y and no phase/modulus-completion filters needed for these four cases.

This is a separately named historical COMPUTER-ASSISTED theorem import, not an author claim extracted from the unfinished lower49 draft, not the proof-free158-profile t24 exploration, and not a new replay. The actual defect in schema r1 and its r2 correction remain recorded. The native trust includes the old reviewed reduction, pinned base generator/Python, drat-trim/compiler/hardware and recorded controls; none is silently erased by this written composition.

The old record's statement that t24 proof mode remained UNKNOWN is historically correct. The current new complete t24 written disposition supplies that missing PARAMETER layer by a different proof, without upgrading the old incomplete run or claiming its158-profile exploration certified.

Therefore

    R_current = R_after_e0 minus historical four-case exclusion
              = EMPTY.

There is NO genuinely uncovered nearest parameter left to attack at these accepted imports. Re-running a closed positive-excess case, or inventing a new e per cut, would not be research progress and is not authorized by HOLD.

## 8. Exact source/acceptance bindings and actual read coverage

Actual metadata SHA256 pins observed for this task:

1. `ame-t24h12e0-layer-complete-parent-v1.md`: `c05e7ceb3217315f3008b0a8765b12b70dd5eeddb9c664dfa87b20cf93a90180`. Complete30-line body read; LF22 is the whole e0-layer composition, and LF30 explicitly withheld other(t,h,e) cases before THIS census.
2. Historical `ame46-s48-e-positive-parent-verdict.md`: `341a97d445cda29b45da0c9678b9fcc3ddf97c9ceed37408e612f619a47d0cb5`. Complete35-line body read, including all four exact parameters, correctness acceptance and positive-excess qualification.
3. `SUPPORT_LOWER42.r2.md`: `1db90164f6de13cad9211a2e79b3b75c0c604239b5037b44f9a2f072f0bd1418`. Actual LF87–140 read for overlap, square unitary components, delta0/delta1 and all-excess slice facts. Its whole lower42 native evidence is not claimed replayed.
4. `SUPPORT_LOWER46.r2.md`: `fac5242b90554de86cd6bd8e17fb2a6800fbd4a3e71d2e4a99f154d5a216f35b`. Actual LF47–125 read, including all-e partner bound/t31, the COMPLETE no-AME(4,2) proof and all-e t32 reduction. These lemmas' scopes, not only a small-s case table, are used.
5. `SUPPORT_LOWER48.r2.md`: `70daac01707158b2842159dbdc6713afa33e541c51f100a91034fdf4d432f60e`. Actual LF41–108 read for officer counting and the all-e t29 case.
6. Historical `ame46-lower46-parent-verdict.md`: `9527b8710a59d08a22a69d1f93694a49ce93846aff6371c5d5c3617ce9d5a714`. Complete27-line body read; LF7/18 explicitly record accepted written lemmas and their reconstructed scopes. This does not reattest any old native execution.

Historical paths3–5 are under `physics/evidence/six-lane-20261016/ame46-support/review/`; historical parent records are under `institute/runs/six-lane-2026-10-16/review/`; the new e0 composition is under the current three-area run root.

The unclaimed/unfrozen `SUPPORT_LOWER49.r1.DRAFT-unfrozen-not-claimed.md` and its placeholders are NOT mathematical or certificate inputs to this census. Neither are old exploration outputs, summary-only frontier sentences, v8-withdrawn blanket reads or unadmitted eval results.

## 9. New global composition candidate and assurance boundary

The COMPLETE s48 parameter census has no residual under the exact listed exclusions:

- Four h0..3 rows fail the actual h-by-h support capacity.
- Four h4/h5/h7/h11 rows fail universal ALL-excess written obstructions.
- One h12/e0 row is excluded by the new complete layer composition.
- Four h6/h8/h9/h10 rows are excluded by the historical positive-excess theorem.

The counts4+4+1+4 cover all thirteen nonnegative scalar rows. The six pair directions share t,h,e,n, so there is no additional per-cut excess configuration hidden outside this table. Actual graph/phase consistency cannot rescue a row whose necessary parameter class has been excluded.

**Composition candidate:** at precisely these named imported theorems, there is no arbitrary-complex AME(4,6) of support48 in any product orthonormal basis. This is the conclusion of a written CASE ASSEMBLY, not an independent finite-certificate implementation, new scientific run or proof-assistant check.

The requested residual-empty condition has now been established by the census at those imports. Nevertheless this NEW GLOBAL assembly requires its own fresh reconstruction and parent disposition BEFORE reporting a newly accepted numerical lower bound. This owner packet does not unilaterally promote the documented48..60 interval or claim formal/human/cross-vendor/novelty acceptance.

Fresh review should first check the intrinsic/common officer definition, the indispensable +e in the general support relation, CAP, the EVERY-e scope of the four universal obstructions, exact conversion of the historical(t,e) pairs to current(t,h,e), and coverage of ALL13 rows without invoking the abandoned lower49 draft or treating e0 as universal. If those gates agree, the next action is global composition/assurance settlement, not another open positive-excess attack or an unauthorized replay.
