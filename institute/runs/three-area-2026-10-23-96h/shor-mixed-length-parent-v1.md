# Shor: mixed-length growth, homogeneous no-go and UD seeds — parent disposition

Actual clock observation preceding this record: **2026-10-23T16:22:15-07:00 PDT** (`/bin/date` at the corrected GO launch; this record written immediately after the complete parent reads). Written checking and source/metadata only.

## Decision

**SUPPORTED at the in-harness written-check level:**

1. **Forced growth (every finite UD complete extension):** the unique two-a word `W=b^r a^2 b^t` forces an actual four-a word `Q=b^α a^2 b^{r+t−1} a^2 b^β` with `α≥r OR β≥t`, hence `|Q|≥|W|+1+min(r,t)≥|W|+2` (strengthened to `+2+min(r,t)` when r,t≥2, via the additional C-collisions `β≥1`/`α≥1`). This is a mixed-length compatibility requirement on EVERY completion.
2. **Homogeneous no-go:** there is **no UD COMPLETE extension of C of the form C∪T_N for any positive N** (both W and Q would have length N, contradicting the strict growth). Consequently **every composition-respecting mass-saturated Bernoulli selector is non-UD** — the entire homogeneous constructive route is retired, not merely its displayed bad control. Wording discipline (D1, accepted): arbitrary C∪T_N supersets CAN be UD while incomplete (e.g. C∪{baab}); the no-go is specifically about UD-and-factor-complete extensions, and the universal non-UD statement covers exactly the Kraft-1 selector family.
3. **UD seeds:** the 20-word set (C plus baab, baaba, baabaa, aaabab) is UD over ALL finite lists via the closed residual invariant; adding `a^n` for every n≥26 preserves UD uniformly (overlap S∩(n−S) cannot cycle to an ambiguity). Both are **incomplete**: Kraft `15811/16384+2^(−n)<1` and the explicit missing factor `b^30 a^5 b^30` (no partition of the central 5-a run by A/W/P at zero internal gap, and no other word can meet it).

**Not established:** any mixed-length completion, unrestricted noncompletion, a new pure-a order bound (the n≥26 threshold is a seed-construction parameter, not a completion bound), novelty. The unrestricted Shor target remains open: supply an actual finite mixed-length M with UD/completeness certificate, or an all-order obstruction.

## Evidence and parent reads

- Complete152-line no-go body `proof-MIXED-LENGTH-GROWTH-AND-HOMOGENEOUS-NO-GO-v1.md`, SHA256 `ad958ace…94dd` — fully parent-read (seven-partition forcing, six-a ambiguity identities with exact gap arithmetic, both C-collisions, homogeneous contradiction).
- Seeds `construction-MIXED-LENGTH-UD-SEED-v1.md` (`c45ef598…`) and `construction-MIXED-LENGTH-UD-SEED-pure-power-addendum-v1.md` (`9205b212…`; wave-v9's third basename had my suffix-order slip, resolved by hash binding): pinned and exhaustively reconstructed by the actual reviewer; parent read the review's complete residual-invariant reconstruction (initial coverage, closure, all ≤4-a gap lists, Kraft arithmetic, missing-factor argument) rather than the seed bodies line-by-line — disclosed coverage level.
- Actual complete153-line review `physics/evidence/three-area-20261023-96h/parallel-18/ame46-support/peer-review-Shor-mixed-length-nogo-and-seeds-v1.md`, SHA256 `e8e4ce8601967a24351b794cfc3f2d2ef948eef167dfe45b047795bdd4336f92`: **0F/0M/0m on all three sources**, plus D1.
- Consumed boundary: `shor-raw-structure-parent-v1.md` (44cd9950) interfaces only.

## Parent hand checks

- The seven proper partitions of the core `a^2 b^{g} a^2` all fail for the stated delay reasons (1+2+1: middle gap g>0 vs W's gap 0; 2+2: needs gap v, actual v−1; 3+1/1+3: V_g's range and trailing boundary / U_g's range g≥r). Padding forcing then yields the actual codeword Q.
- The six-a identity: both displayed lists concatenate to `b^r a^2 b^g a^2 b^g a^2 b^t` with first-list gap `t+(r−1−α)+α=g` and second-list gap `β+(t−1−β)+r=g`; all exponents nonnegative exactly when α≤r−1 and β≤t−1, giving the disjunction by UD contradiction. The two C-collisions use `t+(r−2)+1=g` and `1+(t−2)+r=g` with nonnegative padding at the stated r/t ranges.
- Homogeneous: C's a-counts are {0,1,3,5,7,8,9,10,11,12,13,14} — no 2, no 4 — so W,Q∈T_N and |W|=|Q|=N contradicts |Q|≥|W|+2. The Bernoulli implication uses the reviewed UD+Kraft1⇒completeness implication.
- Seeds: B∩I=∅ and S∩I=∅ keep every residual inside the invariant; the a^26 absence (max run 25, crossing at most one boundary) and the b^30-margin argument for the central 5-a run reconstruct as written.

## Next obligation

The math-5 owner continues the ONE existence-changing input: an actual finite mixed-length M with an epsilon-free residual/Kraft or GP certificate, or an all-order obstruction. Extending the frozen seeds is a sufficient-only branch — permitted as one consolidated packet per seed, not incremental word additions. Homogeneous attempts are closed. Each new packet gets its own actual reconstruction; no execution. Deadline unchanged.
