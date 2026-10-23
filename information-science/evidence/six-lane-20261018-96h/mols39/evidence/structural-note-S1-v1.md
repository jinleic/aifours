# Structural note S1 — symmetries of known cyclic difference matrices near n = 39 (2026-10-19T02:24:47-0700, ContinueCFR21)

Data (frozen stdlib probes; exact computations on pinned matrices): a1 (anchor), a2 (DM35, DM55 untwisted),
tw1-dm35-anchor-v1 (stdout d81f33fa…) and tw2-dm55-v1 (868d2fe1…) = full TWISTED automorphism groups
{(mu, pi, tau) : (s.c)_x = mu c_(pi^-1 x) + tau_x maps the column set onto itself}.

| matrix | rows | twisted group order | content |
|---|---|---|---|
| DM35 (Sym2026 Ex.3) | 7 | 4 | (1,(12)(34)(56)); (-1, id, tau); (-1,(12)(34)(56), tau') |
| Sage DM_55_7_1 | 7 | 12 | untwisted <(1, 6-cycle on rows 0..5), (-1, id)>, contains (-1,(03)(14)(25)) |
| Sage DM_39_6_1 (anchor) | 6 | 6 | untwisted G6 = <(16,(012)(345)), (-1,id)> |
| Sage DM_33_6_1 | 6 | 5 | <(4, 5-cycle)> (multiplier of order 5) |
| Sage DM_51_6_1 | 6 | 10 | <(1, 5-cycle), (-1, id)> |
| Sage DM_21_6_1 | 6 | 5 | <(1, 5-cycle)> |

Observation O1 (exact, from the data): in DM35 the column sums D_1+D_2, D_3+D_4, D_5+D_6 are constant (9, 22, 8 mod 35)
while D_0 = 0; equivalently the twisted element (-1, (12)(34)(56), tau') fixes every column. DM55 likewise contains the
untwisted element (-1, (03)(14)(25)) with the fixed zero row 6, which fixes every column (for a swapped pair the column
permutation is conjugate to multiplication by -mu = 1), so D_3 = -D_0, D_4 = -D_1, D_5 = -D_2 there.
Consequence (by Lemma L3 / Theorem A, accepted scoped partial): for 3 | n and 9 ∤ n (n = 21, 33, 39, 51, ...) no DM
with >= 4 rows has three rows with constant column sum mod 3; a zero row together with a pair D_b = c - D_a is such a
triple. Hence the "paired negation" structure shared by the two known nearby seven-row cyclic DMs (35, 55) cannot occur
for n = 39. This is an exact restriction of mechanisms, not a nonexistence statement for DM7(39).
Remark: Sym2026 Thm 5 lists 2-SOLSSOM(v) possible exceptions {15,21,33,39,45,51,65,87,123,135}; all but 65 are divisible
by 3. Whether the construction of their ref. [120, Thm 4.1] needs exactly the column-fixing involution is UNREAD
(ref. [120] not accessed) — no claim.
Consequence for this lane: models must avoid (-1, swap) elements; the untwisted pure involution model z39_m1 (mu = 1)
remains allowed but lacks DM35's extra column-fixing symmetry, so DM35 is a calibration of the encoder/solver on the
mu = 1 involution only, not proof that the same full mechanism exists at 39. For odd n the twisted versions of our order-2
and order-3 model elements are coboundaries (involutions: 2 invertible; the order-3 rows form induced modules and the
fixed row is the normalised zero row), so twisted variants add no new models here.
