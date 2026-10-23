# 901 bounded cycle 1 (plan recorded 2026-10-16, before any run of this cycle; limit 2 h, <= 3 search CPUs)

## Why not "involution + a few unpaired general blocks"
Classes of Z_901 = Z_17 x Z_53 split into 8 K classes [(a,0)], 26 pure classes [(0,y)] and 416 mixed classes.
Under mu = 52 a block is "structured" (stable) only if it contains >= 2 of the 34 fixed (K or pure) classes, so at
most 17 blocks are stable and at least 28 blocks contain no fixed class. Allowing unpaired general blocks (the
321/681 device) does not change this count: every block with a fixed class uses one of only 34 fixed classes, so at
least 11 blocks are all-mixed in ANY family, and blocks with exactly one fixed class are themselves unstructured.
The device fixed a parity defect for 321/681; 901 has no parity defect, its difficulty is the size (>= 14 pairs) of
the unstructured part. Scope: this is a counting remark about the mu-representation, not an impossibility result.

## New representation: partial order-13 symmetry with a 6-block defect
nu = (1 mod 17, g mod 53), g of order 13. Exact facts (to be machine-checked by the code):
- no block is nu-stable (fixed points of x -> nu x + t form a coset of {(a,0)}, size 17; Z_17 has 8 < 10 classes);
- so nu cannot be a multiplier (45 is not a multiple of 13), but a family may contain 3 nu-orbits of blocks
  (39 blocks) plus a defect D of 6 blocks;
- the 8 K classes are nu-fixed, so D must cover all of them; the other 52 classes of D are 4 complete nu-orbits of
  classes (the 39 orbit blocks cover 30 complete class orbits).
Stage 1 (exhaustive, finite): for every choice T of 4 of the 34 non-K class orbits, enumerate all blocks with
all 10 classes in K u T and decide exactly whether 6 of them partition K u T. Output: number of T with a defect.
If none: the representation is impossible (exact scoped result). Stage 2 (if defects exist): the remaining 30
orbits by 3 base blocks (randomized B1, B2, exhaustive B3), in-program full difference check, strict certificate.
Producer: new file code/defect13.c (forked, pinned by SHA before the run). Checkpoint: stage 1 writes progress every
2000 T; every run <= 30 min.

## Result of stage 1 (run 2026-10-16 23:54:37-23:55:32 PDT, `./bin/defect13 1 0 runs/v901/defect13/stage1`)
Producer `code/defect13.c` SHA-256 177db5e8f64d85e0e2bc02f35122d88a8e33f850d00dc33c09ac0fa1357f6aac (pinned copy
`evidence/v901/defect13/defect13.pinned.c`), binary 658a97cc5a581a883329b3179ad81869801cb4c5633aed60d1d9954a69f97625.
g = 10; class orbits: 8 K singletons + 34 orbits of size 13 (as predicted). All C(34,4) = 46376 choices of T scanned;
rows per T mean 230.15, max 29406 (row cap 200000 never reached); every exact cover search ran to exhaustion.
No 6-block defect exists for any T. Scoped exact result (one implementation, not independently re-verified): there
is no (901,5,1)-CDF made of three orbits of 13 blocks under the order-13 subgroup {(1, h)} plus 6 further blocks.
(Every order-13 element of Z_901^* lies in that subgroup.) Larger defects are not excluded.

## Cycle 1b (recorded before run): 2 nu-orbits + a 19-block mu-structured defect
Counting (exact): a defect of 19 blocks covers K + 14 class orbits; mu-closure of the defect forces both pure orbits
and 6 mu-pairs of mixed nu-orbits (p + 2j = 14 with p even; p = 0 fails by parity), e.g. 13 T1 + 4 T1' + one free
pair {B, mu B}; the bulk is 2 base blocks whose nu-orbits cover the other 20 mixed orbits. Producer: new file
`code/nu13mu.c` (pinned by SHA before its first run). Random choice of the 6 mu-pairs and of the free pair, exact
cover by T1/T1' rows of everything else in the defect, then randomized B1 + exhaustive B2 for the bulk.

## Outcome (2026-10-17 00:00 PDT)
- 901 was found by the pre-existing cycle-0 run of the frozen mu-route producer (`cdf_mq4`, seed 41, r = 11),
  .sol written 23:57:41 PDT, attempt 21 of that run; certificate `certificates/cdf_901.txt` (06bd6ae8...).
- Cycle 1b (`code/nu13mu.c` sha c9958fee..., binary eb6d1a82..., pinned under `evidence/v901/nu13mu/`), seeds 1 and 2,
  started 23:58:18 PDT and stopped at about 23:59:55 after the find: about 2050 configurations each, stage S failed at
  the root (1 node, an uncoverable item) every time, so the bulk stage was never reached. Not analysed further; no
  claim about that representation beyond these counts.
