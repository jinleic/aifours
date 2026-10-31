# Addendum 1 to the partial row-orbit packet: group actions reduce to the cyclic cases; bounded outcomes

Native `/bin/date` observed before writing: **Wed Oct 28 21:18:18 PDT 2026**. Owner InfoRecursiveMDS18-2, info-4. Additive to `frontier-20261028-partial-row-orbit-obstruction-v1.md` (SHA-256 `8aed9f3768ad4af4594cf1d383615a1cd06743377f7ce8ce44a2d5d7b73bd3e4`), which is unchanged. **WRITTEN** reduction plus bounded UNKNOWN records. Original T2(11) remains **OPEN**.

## 1. Group-orbit symmetry reduces to the twelve open cyclic cases (WRITTEN)

Let H be a group of symbol permutations and suppose a T2(11) contains b ≥ 1 disjoint H-blocks {hR : h ∈ H}, with f = 11 − b|H| ≥ 1 further rows. These are |H| distinct rows, because hR = R forces h = id.

For h ∈ H of order k, each H-block is the union of |H|/k blocks {h^iR'} of ⟨h⟩, one for each coset. So A has **b|H|/k ⟨h⟩-blocks with the same f free rows**, and the cyclic case (cycle type of h, b|H|/k) must be one of the 13 cases that survive parts 1, 3, 4 and 5. Every |H| ≤ 10 is checked below; the (6,3,2) entry relies on the DRAT result.

| \|H\| | f | groups | verdict |
|---|---|---|---|
| 10 | 1 | all | excluded: f = 1 (part 3 for any cyclic subgroup) |
| 9 | 2 | Z_9 | excluded: needs (9,1,1) b=1 |
| 9 | 2 | Z_3² | excluded: needs a 3-element case with b = 3 |
| 8 | 3 | Z_8 | excluded: needs a type with an 8-cycle |
| 8 | 3 | Z_4×Z_2, D_4, Q_8 | excluded: an element of order 4 needs b = 2, but (4,4,·) allows b ≤ 1 and other order-4 types allow b = 0 |
| 8 | 3 | Z_2³ | excluded: every involution needs b = 4, so type (2⁵,1) with one fixed point; Burnside gives (11 + 7)/8 orbits, not an integer |
| 7 | 4 | Z_7 | excluded: (7,1⁴) b=1 |
| 6 | 5 | Z_6 | excluded: an element of order 6 with b = 1 is (6,3,2) (DRAT-verified UNSAT), or a type excluded by part 1 or 4 |
| 6 | 5 | S_3 | reduces to the open cases (3³,1²) b=2 and (2⁵,1) or (2⁴,1³) b=3 |
| 5 | 6 | Z_5 | b=1 is the open (5,5,1) b=1; b=2 has f = 1 |
| 4 | | Z_4 | b=1 is the open (4,4,2,1) or (4,4,1³) b=1 |
| 4 | | Z_2², b=2 | excluded: all three involutions are (2⁵,1) with b=4; Burnside gives (11 + 3)/4, not an integer |
| 4 | | Z_2², b=1 | reduces to open involution cases |
| 2, 3 | | cyclic | these are the cyclic cases themselves |

**Conclusion (WRITTEN, with the DRAT-dependent (6,3,2) step).** A T2(11) with any nontrivial group-orbit partial row symmetry has a cyclic block structure among the 12 open cases:

- (5,5,1) b=1;
- (4,4,2,1) b=1;
- (4,4,1³) b=1;
- (3³,1²) b∈{1,2};
- (2⁵,1) b∈{1,2,3,4};
- (2⁴,1³) b∈{1,2,3}.

## 2. Bounded SAT outcomes since the main packet (all UNKNOWN)

**v2 encoder** (symmetry-broken, `570dde55…ea9c`), 900 s each, seed 1:

| case | record | SHA-256 |
|---|---|---|
| (2⁵,1) b=4 | `frontier-20261028-ps2-2-2-2-2-2-1-b4.json` | `81e75aef…5ae57c` |
| (2⁴,1³) b=3 | `…ps2-2-2-2-2-1-1-1-b3.json` | `a417a0b8…74c0fa` |
| (3³,1²) b=2 | `…ps2-3-3-3-1-1-b2.json` | `711178b0…d8e5e9` |
| (5,5,1) b=1 | `…ps2-5-5-1-b1.json` | `cee2eee9…5ca261` |
| (4,4,2,1) b=1 | `…ps2-4-4-2-1-b1.json` | `31c32b41…368e26` |
| (4,4,1³) b=1 | `…ps2-4-4-1-1-1-b1.json` | `ef9d4536…4ba334` |

Two more v2 runs, (3³,1²) b=1 and (2⁵,1) b=3, were cut by the shell-job limit before Kissat returned. They have CNF files but no record and **no result**.

**v1 encoder**, 1,700 s each:

| case | record | SHA-256 |
|---|---|---|
| (2⁵,1) b=4 | `…partial-sym-2-2-2-2-2-1-b4-long.json` | `458ea1e5…5ddf01f` |
| (2⁵,1) b=3 | `…-b3-long.json` | `4300fb67…e93fdbc` |
| (3³,1²) b=2 | `…partial-sym-3-3-3-1-1-b2-long.json` | `b955d34e…d2a8972` |
| (5,5,1) b=1 | `…partial-sym-5-5-1-b1-long.json` | `a9c3a5c1…ae9ee54` |

**Cube sample.** For (2⁵,1) b=4 the first block's base row prefix was split at depth 2, giving 90 cubes. Runner: `frontier-20261028-structured-cube-runner-v1.py`, `10badcf1…0de25e04`. Cubes 0–7 were all UNKNOWN at 120 s each (`…cubes-ps2-2-2-2-2-2-1-b4-sample-01.jsonl`, `ba3925eb…e59dda12`).

No process remained after the jobs ended (checked by ps at 21:18:08 PDT).

## 3. Assessment

The lemma removes every structured case that is easy for SAT. The 12 that remain resist single runs of up to 28 minutes and depth-2 cubes, so deciding even the strongest of them, (2⁵,1) b=4, is a multi-hour cube-and-conquer task. I have not started one. It needs explicit parent authorization with a CPU-hour bound.
