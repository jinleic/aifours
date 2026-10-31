# RQLS10 v88 — Dense column planes are pairwise isoclinic; trace overflow excludes d=2 with three long trails and pins d=2 with two long trails

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 19:03:44 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written unitary-modulus/projection-trace/counting arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Lemma TD: the four column planes at a dense vertex are pairwise interior-isoclinic

Let D be dense, with row ONBs e_1..e_4, f_1..f_4, transition W_ij = <e_i,f_j> and planes A_i = span(e_i,f_i). By v77's complete modulus table, |W_ij| = |W_ji| for all i,j, with weights a,b,c>0, a^2+b^2+c^2=1, and complementary index pairs carry equal weights. For i not equal to j and any unit z = alpha e_i + beta f_i in A_i,

    <z,A_j z> = |<e_j,z>|^2 + |<f_j,z>|^2 = |beta|^2 |W_ji|^2 + |alpha|^2 |W_ij|^2 = |W_ij|^2.

A positive operator on the two-dimensional A_i with constant expectation is scalar, so

    A_i A_j A_i = lambda_ij A_i,   lambda_ij = |W_ij|^2 in (0,1),
    lambda_ij = lambda_ji,   sum over j not i of lambda_ij = 1,
    lambda_12 = lambda_34,  lambda_13 = lambda_24,  lambda_14 = lambda_23.

The row-norm identity uses W_ii = 0. By the complete equal-angle CS form, also

    (I-A_i) A_j (I-A_i) = (1-lambda_ij)(I-A_i).

These are exact written identities from the v77 table, not computations.

TRACE IDENTITY. For any full-resolution class T, an ONB of E4, and every j: sum over t in T of <t,A_j t> = tr A_j = 2. A cell in A_j contributes 1, a cell in I-A_j contributes 0, a cell in A_k (k not j) contributes lambda_kj, and a cell in I-A_k contributes 1-lambda_kj.

## 2. Theorem: d=2 with three long trails is IMPOSSIBLE

By v87, d=2 with m=3 forces three long trails tau_k : D -> s_k -> D' (k=1,2,3), one direct trail tau_4 : D - D', and a three-circuit on the sparse vertices. Each D-missing class consists of one D'-cell w' and three D-side cells z_1,z_2,z_3, with z_k in A_k at s_k. The D-side cells of tau_k at s_k lie in column s_k-D'. Distinct columns therefore force w' into the ONLY remaining column at D', the direct column D-D', so w' lies in I-A_4. The trace identity for A_4 gives

    lambda_14 + lambda_24 + lambda_34 + 0 = 1   but must equal 2.

Contradiction. Hence d=2 with m=3 is impossible, and by v87 d=2 requires m in {1,2}.

## 3. Theorem: exact structure of d=2 with two long trails

For m=2, v87 gives two-circuits C_1 on {s_i,s_j} and C_2 on {s_i,s_k}, long trails tau_1 through s_j and tau_2 through s_k, and direct trails tau_3,tau_4. Each D-missing class contains exactly one D-side cell z_1 in A_1 at s_j and one z_2 in A_2 at s_k.

* NO D-missing class contains a D'-cell. A D'-cell w' cannot share the columns of z_1,z_2, so w' lies in I-A_l with l in {3,4}. The A_l trace then forces the fourth cell u to satisfy <u,A_l u> = 2-(lambda_1l+lambda_2l) = 1+lambda_(l',l) > 1, where l' is the other direct index. That is impossible.
* Hence the two D-missing classes also miss D'. By v87 they are therefore EXACTLY the two D'-missing classes. Each has the form

      M = {z_1, y_1 at s_j in distinct rows; z_2, y_2 at s_k in distinct rows},

  with y_k a D'-side cell of tau_k in I-A_k. The trace identities hold automatically, by the complement compressions of section1.
* U = span(z_1,y_1) is A_1-invariant, and its orthogonal complement span(z_2,y_2) is A_2-invariant. Since A_1,A_2 are interior-isoclinic, in their tensor identification U = K_1 tensor w for one unit w. Consequently

      S_(s_j) = span(a+ tensor w, a- tensor w-perp),   S_(s_k) = span(b+ tensor w-perp, b- tensor w),

  up to exchanging S with its complement. Both are PRODUCT-reflection forms, with P_(tau_1)=A_1 = |a+><a+| tensor I and A_2 = |b+><b+| tensor I. The second D-missing class uses the complementary rows and spans the same pair {U,U-perp}.
* The other EIGHT classes each contain exactly one D-cell, one D'-cell and two circuit cells: all sixteen dense cells and all sixteen circuit cells. By GLX, their circuit parts are {C_1+,C_1-}, {C_2+,C_2-} or {C_1 at s_j, C_2 at s_k}. A circuit cell at s_j forbids tau_1's dense columns in its class, and one at s_k forbids tau_2's.

Existence or exclusion of this exact d=2,m=2 configuration remains OPEN; m=1 also remains OPEN.

## 4. General overflow corollary

Let D be dense and T a class containing cells in A_k for every k in a set K not containing j, plus one cell in I-A_j, with r further cells. Then those r cells have total A_j-expectation 2 - sum over K of lambda_kj. If K is the full complement of j, this total is 1 with r=0: impossible. If |K|=2, it is 1+lambda > 1 with r=1: impossible. This is the mechanism of sections 2-3 and applies to any d.

## 5. Exact frontier and imports

New paid results: Lemma TD; the trace identity; d=2,m=3 IMPOSSIBLE; the exact d=2,m=2 structure; and the general overflow corollary. The v76-graph frontier is now: all-sparse residuals (BARBELL, THETA(1,1,3) three cases, THETA(1,2,2), C5); d=2 with m in {1,2}, where m=2 has the pinned structure; d=3 with two long trails; d=4 with complementary long trails; and d=5. Other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: ENTIRE v76/v77 graph, local frames and modulus table; v78 complete CS form; v80 oriented-plane bound; v85 D1/trails; v86 GLX; v87 DX/TL and the d=2 slot structures; and the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity, chosen frame or global tensor WLOG. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S88, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor and the v30 dangling-reference defect. Frozen Mainv17/S72/input map/proofs/live151 stay immutable.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
