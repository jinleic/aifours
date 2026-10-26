# Addendum 3: the band closure for u < 1 (with the numerator conditions), every z ≥ 4/5

Actual `/bin/date` before this addendum: **Sun Oct 25 23:08:48 PDT 2026**. The base file and Addenda 1–2 are not edited. All steps are exact hand algebra; no machine was used.

## 1. Expansion point and cone

Take 0 < u < 1. Set x = y + u, delta' = 1 − u ∈ (0, 1), P' = p − 2u and Q' = u² − pu + q = Q(−u).

The generators (y+u)^alpha (y+1)^beta become x^alpha (x+delta')^beta. This is the same set as in the base file, with the roles of the two factors swapped:

- the pure powers are x^alpha with alpha ≤ 3;
- the spilling factor is (x+delta')^beta.

So the cone characterization of the base file §3 carries over with the expansion taken in x = y + u:

    L5' = R5',
    L4' = R4' − 2delta' R5',
    L3' = R3' − delta' R4' + delta'^2 R5',

together with R2', R1', R0' ≥ 0. Two spot checks: x³(x+delta')² gives (L5', L4', L3') = (1, 0, 0), and x²(x+delta')³ gives (1, delta', delta'^2).

The numerator conditions of the family are exactly P' ≥ 0 and Q' ≥ 0. They are b2 and b1 in the base file §2. They also give w = P' + delta' > 0.

## 2. Coefficients

Write D_z(x−u) = (x−u)((x+delta')² + z)², and let E5..E0 be the coefficients of that quintic in x:

- E5 = 1
- E4 = 5delta' − 1
- E3 = 10delta'² − 4delta' + 2z
- E2 = 10delta'³ − 6delta'² + 6delta' z − 2z
- E1 = (delta'² + z)(5delta'² − 4delta' + z)
- E0 = −(1−delta')(delta'²+z)²

The trace gives w − u = P' − 1 + 2delta'. Hand expansion then yields:

    R5' = P'(1 − 2delta') + delta' − delta'^2 − 2z − Q',
    R4' − 2delta' R5' = P'(−3delta'^2 + 2delta' − 2z) + Q'(1 − 3delta')
                        + delta'^2 − delta'^3 − 2delta' z + 2z.

At delta' = 0 both reduce to the base file's delta = 0 expressions.

## 3. Infeasibility for every z ≥ 4/5

Throughout, use the elementary bounds delta' − delta'^2 ≤ 1/4 and 2delta' − 3delta'^2 ≤ 1/3.

**(a) delta' ≥ 1/2.** Here 1 − 2delta' ≤ 0 and P' ≥ 0, so L5' ≥ 0 forces

    Q' ≤ delta' − delta'^2 − 2z ≤ 1/4 − 2z < 0,

which contradicts Q' ≥ 0.

**(b) 0 < delta' < 1/3.**

- L5' ≥ 0 together with Q' ≥ 0 forces P' ≥ P'_low := (2z − delta' + delta'^2)/(1 − 2delta').
- L4' ≥ 0 bounds Q' from below; combining that bound with L5' ≥ 0 gives
  P'(−3delta'^2 + 3delta' + 2z − 1) ≤ delta'(1−delta')(1−2delta') + 4delta' z.
  The bracket is positive because z > 1/2. Call the resulting upper bound P'_45.

The two bounds clash, P'_45 < P'_low, because

    [delta'(1−delta')(1−2delta') + 4delta' z](1−2delta') ≤ (1+4z)/8
       < (2z − 1/4)(2z − 1) ≤ (2z − delta' + delta'^2)(−3delta'^2 + 3delta' + 2z − 1).

The left inequality uses delta'(1−2delta') ≤ 1/8. The middle one holds because (2z − 1/4)(2z − 1) − (1+4z)/8 = 4z² − 3z + 1/8. That expression is increasing for z > 3/8 and equals 57/200 > 0 at z = 4/5.

**(c) delta' = 1/3.** L4' ≥ 0 reads P'(1/3 − 2z) + 2/27 + 4z/3 ≥ 0, so P' ≤ (2/27 + 4z/3)/(2z − 1/3). Meanwhile P'_low = 6z − 2/3. For z ≥ 4/5 the difference (6z − 2/3)(2z − 1/3) − (2/27 + 4z/3) is positive (at 4/5 it is 3.6 or more), so the two bounds are incompatible.

**(d) 1/3 < delta' < 1/2.** Now L4' has Q'-coefficient (1 − 3delta') < 0. With Q' ≥ 0, L4' ≥ 0 needs

    P'(2z + 3delta'^2 − 2delta') ≤ delta'^2 − delta'^3 − 2delta' z + 2z.

Compare with P' ≥ P'_low:

    (delta'^2 − delta'^3 − 2delta' z + 2z)(1 − 2delta') ≤ (1/4 + 2z)/3
       < (2z − 1/4)(2z − 1/3) ≤ (2z − delta' + delta'^2)(2z + 3delta'^2 − 2delta').

The middle inequality holds at z = 4/5 (0.617 against 1.71 to two decimals), and the gap only grows as z increases. So the bounds are incompatible here too.

All delta' ∈ (0, 1) are covered. **Hence for every z ≥ 4/5 and every 0 < u < 1, the family has no PH7.** Together with Addendum 1 (u > 1) and the base file (u = 1 requires z ≤ 1/2): for every z ≥ 4/5, NO u > 0 admits a PH7 in the band-holding chain family (u,u,u,w,1,1,1) with initial states {1,2,3}, exit 7 and arbitrary through-mid cycles.

## 4. Scope

Still RESTRICTED. Not covered:

- holdings that vary inside a block, or a downstream holding other than 1;
- cycles that avoid the middle state;
- other topologies, and Case II.

The unrestricted 8/9 question remains open: minimum {7,8}. HOLD, root, cutoff and deadline are unchanged.
