# Heuristic expected-count derivations for symmetric DM7 models — v1 (2026-10-19T01:17:34-0700, ContinueCFR21)

Status: HEURISTIC ONLY. Used to ORDER models and size budgets, never as evidence of existence or non-existence.

## Model of randomness
Choose a G-invariant column configuration uniformly (orbit representatives free), treat each pair-orbit difference list as
uniform subject to (i) automatic relations: a list that is +/- balanced by an element acting by -1 on that pair has sum 0
and its 0-entries are forced by fixed columns; (ii) conditioning on the rows being bijections (pairs with the zero row),
after which every other pair list of two bijective rows has sum 0 automatically (factor n) and, when the two entries of a
column come from distinct columns of a bijective row inside one orbit, its entries are automatically nonzero.
P(list of n entries is a permutation) = n!/n^n; for a +/- balanced list with (n-1)/2 classes: ((n-1)/2)!/((n-1)/2)^((n-1)/2)
(times (n-1)/n per entry when nonzero-ness is not automatic).

## Calibration points
* Old-lane exhaustive count (one program): Z21 six-row DMs invariant under a pure 5-cycle with a fixed zero row: 96
  labelled solutions (2 classes). Prediction: 22.27 (configs) - 8.06 (rows) - 2 x 6.31 (other pair orbits, sum and
  nonzero corrections) = log10 1.58 -> ~38. Observed/predicted ~2.5.
* Old-lane exhaustion: Z21 seven-row model g06-type <(4,(123)(456))> (fixed row): prediction ~0.4 labelled; observed 0.
* DM35 (Sym2026 Ex.3) exists in z35_m1_gauged; prediction ~50 labelled solutions.

## Z39 seven-row models (row 6 or 0 = zero row)
| model | configs (log10) | pair-orbit factors (log10) | E (labelled) |
|---|---|---|---|
| pure involution (12)(34)(56), gauge fixed col = 0 (z39_m1_gauged) | 21.91 + 2x62.05 - 2x1.59 (gauge) | -7.21 (swapped, auto nonzero) - 2x(15.74 + 7.21 + 2x14.15) - 2x14.15 | ~6e4 |
| <(16,pi)> (z39_g3), f3 = 0 / 3 / 6 fixed columns | 108.1 / 108.9 / 108.4 | 2x(-15.74) rows, 5x(-14.15) | ~7e5 / 5e6 / 2e6 |
| <(16,pi),(1,(03)(14)(25))> gauged (z39_z6p_gauged), m2 = 1 | 52.6 | -15.74 - 2x14.15 - 7.21 | ~25 |
| <(16,pi),(-1,id)> (z39_g6), m2 = 1 / 4 | 52.6 / 51.9 | 7 x (-7.42) incl. nonzero factor | ~5 / ~1 |
| six-row anchor model z39_g6six, m2 = 1 | 52.6 | 5 x (-7.42) | ~3e15 |
| unrestricted DM7 (zero row, columns unordered) | 326 | 6x(-15.74) - 15x14.15 | ~2e19 labelled (~5e4 classes after row/unit/translation symmetries) |

Reading: Z39 is far above the Z21 threshold (unrestricted ~1e-2 labelled at n = 21 by the same model). The open
question is search effort, not expected existence; the heuristic has no validated error bars beyond the two calibration
points and must not be cited as evidence.
