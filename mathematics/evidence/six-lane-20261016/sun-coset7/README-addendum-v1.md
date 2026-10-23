# sun-coset7 README addendum v1: engine freeze and Prop 4.5 citation (written before any run)

The freeze record (host clock) is in `evidence/addendum-v1.sha256`. `README.md` (2a6d6d6e…3fd1) stays frozen and unchanged.

## 1. Parent rulings received (13:35 PDT IRC)

- **Prop 4.5** may be used only as stated and proved in the accepted k5 record, with exact lines cited and hypotheses restated at each use.
- **M-S Lemma 4.6** is not an accepted import; K5.3 stays open unless derived or certified.
- **GO, exploratory only, never a premise until reviewed:** Stage A (X1 plus controls, self-budget ≤ 5 min) and then Stage B (K5.2\* and KII, self-budget ≤ 45 min), only after reporting A. Stages C and D are not authorised.

## 2. Exact citation for the single Prop 4.5 use (README Lemma R1c)

- **Source:** `mathematics/evidence/six-lane-20261016/sun-coset5/proof-v4.md`, sha256 3d17efcc034cca643515e581fa4667515086d0844a58b951e2641080d6c94516, bound by the accepted verdict `R/sun-coset5-parent-verdict-v1.md` (2cf02436…5301).
- **Statement (proof-v4.md line 67):** "Let r_1, …, r_4 be pairwise coprime with r_1 odd. Then no group has subgroups with indices [G:U_1] = 2r_1 and [G:U_i] = 4r_i (i = 2, 3, 4) and pairwise disjoint cosets g_iU_i." Proof: proof-v4.md lines 69–101 (§2 (a)–(g)).
- **Use (README Lemma R1c), hypotheses restated:** the four cosets of i, d_1, d_2, d_3 are pairwise disjoint (subfamily of a CE); their indices are 2r_1 with r_1 = n_i/2 odd (e_i = 1), and 4r_{t+1} with r_{t+1} = n_{d_t}/4 (e_{d_t} ≥ 2 by R1b); r_1, …, r_4 are pairwise coprime (shown in R1c from P0–P1). No further hypothesis is used: the statement allows any group and any subgroups.

## 3. Engine freeze (before any run)

| file | sha256 | frozen |
|---|---|---|
| `code/core7_engine_v1.py` | e7b4f039ba02c9e8ab5c39579c0d21d3ce4e1d3aba13ec2813129eda67a4288d | 13:34:29 PDT (chmod a-w) |

**What it implements** (rules-k7-v1; exploratory per the GO):
- T with general γ and ℓ;
- K on partial assignments (deletion) and at leaves;
- VFC-LP on stars with at least 3 assigned neighbours (partial or complete, by deletion), exact duals, every admissible q;
- P and RPLP at leaves (exact or Farkas duals; float search, exact verification);
- leaf orbits deduplicated under the full stabiliser of the profile tuple (exact lexicographic canonical form over every stabiliser permutation);
- no FH rule.

**Self-limits (no external timeouts):**
- each universe run checks elapsed time against its own budget at every node and inside long loops;
- it reads statvfs at start and at least every 20 s, and stops itself cleanly, reporting UNKNOWN, if free space < 12.0e9 B;
- universes outside the current GO are refused by the program itself.

**Planned command lines** (one process at a time; TMPDIR inside the lane):
- **Stage A:** `python3 code/core7_engine_v1.py X1 evidence/stageA-X1 120`, `… MSP45 evidence/stageA-MSP45 20`, `… CORE5 evidence/stageA-CORE5 90`, `… CONTROLS evidence/stageA-CONTROLS 60` (total budget 290 s ≤ 300 s).
- **Stage B (only after the A report):** `… K52 evidence/stageB-K52 900`, then `… KII evidence/stageB-KII <remaining of 2700 s>`.

**Readiness check before each stage:** statvfs free ≥ 12.2e9 + 16 MiB = 12,216,777,216 B, recorded in the stage receipt.
