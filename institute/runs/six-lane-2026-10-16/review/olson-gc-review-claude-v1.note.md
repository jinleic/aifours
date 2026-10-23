DISPOSITION: ACCEPT-WITH-FIXES

The mathematics of the target is correct as written. All eight findings below are MINOR (wording, scope or path issues). No step of Lemma GEN, Lemma GC or Theorem NMH-iii fails.

## FATAL
none

## MAJOR
none

## MINOR

**m1. P/c6/proof-GC.md:L105 (Remark (3)): the walk bound is loose and contradicts "linear".**
- The stated bound (2m-1)(L-2) is true but is about k^2/2, which does not support "linear".
- Exact count:
  - b(chi0) = (1, 2, ..., 2m-1).
  - chi* has block lengths (2, 1^(2m-3), L-2m, 1), so b* = (2, 3, ..., 2m-1, L-1).
  - b*_j > b_j for every j, so the lowering pass (L83-85) is never used.
  - N = (2m-2) + (L-2m) = L-2 = k-3.
- chi* is simply chi0 with positions 2..L-1 flipped. The walk flips 2m, ..., L-1, then 2m-1, ..., 2, once each.
- Example: p=7, k=11 gives N=8, against the stated bound 5·8 = 40.
- Fix: "The walk has exactly L-2 = k-3 unit moves (each of positions 2..L-1 is recoloured once; the lowering pass is empty); the construction is linear in k."

**m2. P/c6/proof-GC.md:L103-104 (Remark (1)): the list of what is used is incomplete.**
- "Only Delta0 >= 3 ... and k >= 7 are used" omits two inputs the proof needs:
  - Lemma H with beta=0 and the identities (1.1), used in GEN (L51-52);
  - |d_s| <= e_s+1, e_s >= 0, E = sum e_s, and e_t = 1 for a pair, used in (S) and (M) (L90-93).
- Fix: "Within the NMH setting (Lemma H with beta=0, (1.1), |d_s| <= e_s+1 for pure runs and pairs), the only inequalities used are Delta0 >= 3 (via W' >= E+4) and k >= 7; E, kB, B and the run lengths and positions are otherwise arbitrary."

**m3. P/c6/proof-GC.md:L118: path does not resolve to the intended file.**
- Under L5's convention (relative to mixdef-high/), "../proof-MH.md" resolves to inverse-run-count/proof-MH.md.
- The intended file is P/proof-MH.md, Sec. 6 (L171-185).
- The same string is correct only from inside c3/ (P/c3/README.md:L19, P/c3/proof-C-r1.md:L5).
- Fix: "item (iii) of proof-MH.md Sec. 6".

**m4. P/c6/proof-GC.md:L16-17: root-relative path and stale provenance note.**
- "institute/runs/.../olson-c6-uniform-parent-verdict.md" is repository-root-relative, contrary to L5.
- "not re-read by this worker" is stale: P/c6/README.md:L652-655 records that it was read after freezing.
- The import itself is correct, per review-notes/olson-c6-uniform-parent-verdict.md:
  - L11: SEED-G r2;
  - L14: DF/C0W;
  - L17: A0 and C0-all;
  - L21: the alternatives of the count-free corollary.
- Fix: label the path as root-relative, give sha256 e5ac31d9…, and cite these rows.

**m5. P/c6/proof-GC.md:L109-110: ZSI-B needs the R qualifier.**
- "every ZSI-B word" must read "every ZSI-B word with R <= 2p-3".
- ZSI-B has k=p+1 and kB=1, so R = p+1+2B, and NMH permits R > 2p-3.
  - Example: p=11, B=4 gives kappa=5, k=12, D=12, A=16 <= 21, E=8, R=20 > 19.
- Whether (4.1) admits such words is not visible in the packet, so the qualifier is needed.
- L118 ("its ZSI-B part") is already correct.

**m6. P/c6/proof-GC.md:L119-121: "supersedes" is unconditional.**
- "It supersedes" is asserted in a file that is itself unreviewed (L4).
- Fix: "If accepted, Theorem NMH-iii subsumes, as a conclusion only, …".

**m7. P/c6/proof-GC.md:L121-123: the [I] assembly omits the reductions.**
- The sentence makes acceptance of c2/proof-C2.md and of this file conditions, but not acceptance of the reductions.
- MIX_DEF_HIGH(p) also needs the reductions that P/README.md:L18-23 cites as [W]: Lemma OR, Lemma M0, Theorem ALT, Corollary B0/C0-B'/A1, and the trivial cut.
- Fix: "if c2/proof-C2.md (Theorem FW+), this file and the reductions cited in README.md Sec. 1 are accepted, NMH(p) and MIX_DEF_HIGH(p) would follow."

**m8. P/c6/proof-GC.md:L113-115: "empty seed intersection" misnames the object.**
- The logic is right, but an empty interval is not a seed (P/c6/proof-SEEDG-r2.md:L74 requires a_t <= b_t), and here a single configuration yields the empty interval.
- Fix: "the bounds x_t ∈ [lambda({t}),U({t})] (canonical lift) and x_t ∈ [s_lo,s_hi] (proof of GS (a), from the actual Q) are inconsistent".
- This is exactly the accepted alternative (a): review-notes/olson-c6-uniform-parent-verdict.md:L21, "empty intersection of bounds obtained from actual configurations".

*Non-target note (not counted):* P/c6/README.md:L622 and L638 read "the path [k]-2026-10-18T00:00:05-0700" and "[k]-2026-10-18T00:07:19-0700". The intended text "[k]-{t}" was overwritten by a timestamp substitution.

## Q1 — Lemma GEN is exact; no failing tuple exists

**Floor-term conditions (i)-(iv).**
- Source: P/c6/proof-SEEDG-r2.md:L52-53, with beta=0 in inverse-parity/proof-PAR-K0.md:L19, so D_Q+B-kappa+m = y+m-kB.
- "The min equals the floor term" means the floor term is <= both other terms; this gives L41-42.
- Doubled forms at L45 are correct, using floor((y+B)/2) = (y+B-th)/2 and floor((A-y)/2) = (A-y-th')/2.

**Parity elimination: an exact equivalence for both parities.**
- y ≡ B+th (mod 2), so 2m+y and both bounds of (i)/(ii) are ≡ B+th.
- th=1: the bounds are already 2kB+B+1 and 2p-B+1.
- th=0: 2kB+B+1 and 2p-B+1 have the opposite parity. So on integers ≡ B:
  - ">= 2kB+B+2" is equivalent to ">= 2kB+B+1";
  - "<= 2p-B" is equivalent to "<= 2p-B+1".
- The same argument applies to 2m-y ≡ A+th' for (iii)/(iv).

**Centres, half-length and the sum/difference identities.**
- Centres: p+kB+1 and p+kappa+1-A. Half-length: p-kappa.
- a1+a2 = 4m-(2p+kB+kappa+2-A) = 4m-(k+2), because A = p+kB+E/2 = 2p-k+kappa+kB.
- a1-a2 = 2y-(A-kappa+kB) = 2y-D.
- max(|a|,|b|) = (|a+b|+|a-b|)/2, and 2(p-kappa) = E+2Delta0.

**Complement symmetry (1.2).**
- Q^c has m blocks and weight D-y.
- Its two conditions use D-y+B = A-y and A-(D-y) = B+y, so they are literally Q's conditions.

**Domain.**
- The derivation is an identity in all integers y and m, of any sign; th and th' handle negative values.
- Lemma H restricts the meaning to proper Q, where 1 <= m <= k/2.

Boundary checks, written as (p,k,kappa,B,E; m,y):

| tuple | LHS | bound | lam | lamc | generic |
|---|---|---|---|---|---|
| (11,16,5,4,0; 5,-1) | 12 | 12 | min(7,3,**2**) | min(7,13,**7**) tie | yes |
| (11,16,5,4,0; 5,-2), th=th'=0 | 14 | 12 | min(7,2,**2**) | min(7,14,8) = 7 ≠ 8 | no |
| (11,16,5,4,0; 5,9) | 12 | 12 | min(7,13,**7**) | min(7,3,**2**) | yes |
| (11,16,5,4,0; 5,10) | 14 | 12 | min(7,14,8) = 7 ≠ 8 | — | no |
| (11,16,5,4,0; 3,1), c=6 | 12 | 12 | min(9,3,**3**) | min(9,9,**6**) | yes |
| (11,16,5,4,0; 3,0) | 14 | 12 | min(9,2,3) = 2 ≠ 3 | — | no |
| (5,7,2,1,0; 2,0) | 6 | 6 | min(4,1,**1**) | min(4,6,**4**) | yes (ties) |
| (5,7,2,1,0; 2,-1) | 8 | 6 | min(4,0,1) = 0 ≠ 1 | — | no |

## Q2 — The construction is correct

**Choice of m and c.**
- For k = 4j+s: m = j+1 and 4m-(k+2) = 2-s, so c = 2,1,0,1 for s = 0,1,2,3 (k+2 ≡ 2,3,0,1). This matches L67.
- m = 2 at k=7.
- 2m <= L-1: k=7 gives 4 <= 5; k=8 gives 6 <= 6 (tight); for k >= 8, (k+4)/2 <= k-2.

**Path, blocks and properness.**
- r_1 = t+1 and r_L = t-1 are adjacent only if k | 3, so k >= 4 already suffices.
- Every cyclic block of X(chi) or Y(chi) avoids t, so it is a path block; each colour has exactly m blocks.
- Q = X is nonempty and misses t, so it is proper.
- Q+t = [k]-Y contains t and Y is nonempty, so it is proper.
- (Q+t)^c = Y and m(Q+t) = m(Y) = m, so (1.2) and GEN test Q+t with its true block count.
- D_X + D_Y = D-d.

**The two colourings and (3.2).**
- chi0: b = (1,…,2m-1).
- chi*: block lengths (2, 1^(2m-3), L-2m, 1), b* = (2,…,2m-1,L-1); first colour X, last colour Y, m+m blocks. So chi* ∈ C.
- X(chi*) = Y(chi0) ∪ {r_1} − {r_L}. This gives (3.2): v* = D−d−v0 + d_(t+1) − d_(t−1).

**The walk.**
- Since b* > b componentwise, only pass 1 runs:
  - first b_(2m-1) goes from 2m-1 to L-1;
  - then b_(2m-2), …, b_1 each increase by 1.
- Strict monotonicity holds: when b_j is raised, b_(j+1) = b*_(j+1) >= b*_j+1 (or b_(2m) = L), and b_(j-1) = j-1.
- Each move recolours exactly one position in 2..L-1; positions 1 and L never change.
- Every intermediate colouring lies in C with exactly m X-blocks and m Y-blocks. For example, after flipping 2m..j it is X|Y|…|Y|X^(j-2m+2)|Y^(L-j).
- |Δv| = |d_a| with a ∈ {r_2..r_(L-1)}, so a ≠ t.
- The pass-2 argument at L85 is also correct, though unused.

**Isolation is not needed, confirmed.**
- TS (P/c6/proof-SEEDG-r2.md:L71-73) uses only u_(Q+t) = u_Q + u_t and (ARC).
- The proof of GS (b) (L97-99) uses only D_(Q+t) = y+d, never m(Q+t).
- This is essential: every GC configuration contains t+1, because position 1 is always X (t_adjacent = all targets, P/c6/out/gc_controls.txt:L3).

## Q3 — Window, crossing and edge cases

**The window (3.1).**
- |2v−D| <= W' is equivalent to ceil((D−W')/2) <= v <= floor((D+W')/2).
- The Y-condition |D−2d−2v| <= W' gives the same range shifted by −d.
- Their intersection is exactly (3.1).

**Parity (not noted in the target; harmless).**
- D+W' = 2kB+2E+3Delta0−c ≡ Delta0+c ≡ k+k ≡ 0, since Delta0 = k−2kappa and c ≡ 4m−k−2 ≡ k.
- So D ± W' are always even, and the roundings are exact.
- Hence hi−lo+1 = W'−|d|+1, one more than L92 needs.
- (3.3) sharpens to 2lo <= Sigma <= 2hi, i.e. Sigma/2 ∈ [lo,hi]; the two walk endpoints are symmetric about a point of the window.

**Inequalities (S), (M), (3.3) and the crossing.**
- (S): for a pure target, |d_a| <= E−e_t+1 = E+2−|d|; for a pair target, |d_a| <= E. Both are <= W'−|d|, since W'−|d| >= E+4−|d|.
- (M): |d|+|d_(t+1)|+|d_(t−1)| <= E+3 <= W'.
- (3.3) is equivalent to ±(d_(t+1)−d_(t−1)) <= W'−|d|, using 2max(0,∓d) ± d = |d|. This holds for every sign of d.
- Crossing: no step exceeds hi−lo+1, so no step jumps the window, and the endpoints force a crossing.

Edge cases, computed by hand:

| case | parameters | window(s) |
|---|---|---|
| p=5, k=7, c=1 (the only class) | kappa=2, B=1, E=0, D=W'=5 | anti [1,5]; aligned [0,4] |
| p=7, k=8, c=2 | kappa=2, B=1, E=2, Delta0=4, D=W'=8 | pair [0,8]; anti [1,8]; aligned d=3 [0,5] |
| p=7, k=9, c=1 | kappa=3, B=2, E=2, Delta0=3, D=W'=7 | pair [0,7]; anti b=2 [2,7] |
| p=7, k=10, c=0 | kappa=3, B=2, E=0, D=6, W'=8 | anti [0,7]; aligned [−1,6] |

- **p=5:** v0 = d_(t+1)+d_(t+3) ∈ {0,2}, so no move is ever needed (receipt steps_max 0, P/c6/out/gc_controls.txt:L4).
- **A case where the walk is actually needed:** p=7, k=11, kappa=4, B=3, E=0, Delta0=3, so D=5, A=8, m=3, c=1, W'=5.
  - Target t is aligned; d along r_1..r_10 is (−1,+1,−1,+1,−1,+1,+1,+1,+1,+1).
  - Window [0,4]; v0 = −3; Sigma = 5−1−1−1 = 2; vN = 5 > hi, so both endpoints lie outside the window.
  - Flipping positions 6, 7, 8 gives v = −2, −1, 0. Then X = {r1,r3,r5..r8} (3 blocks) and Y = {r2,r4,r9,r10} (3 blocks, D_Y = 4).
  - Direct check:
    - lam(0,3) = min(5,2,2) and lamc(0,3) = min(5,7,5);
    - lam(4,3) = min(5,6,4) and lamc(4,3) = min(5,3,3);
    - Q+t: lam(1,3) = min(5,3,3).
    - All equal their floor terms, so X, Y and Q+t are generic.
  - Seed: s_lo = 3−2 = 1, s_hi = 3−2 = 1, (QS) window [0,1], lambda({t}) = 1, U({t}) = 3. The seed is [1,1].
  - The crossing comes after 3 moves (the receipt's p=7 steps_max is 3); the full walk is N = 8 = k−3.
- **E >= 4, where the bounds are tight:** p=11, k=12, kappa=4, B=1, E=6, Delta0=4, so D=16, W'=12.
  - Target is aligned with d=7; all other runs are single letters. Window [2,7].
  - (S): E+2−|d| = 1 is attained. (M): 7+1+1 = 9 = E+3 is attained.

**Remark (3):** the exact walk length is N = k−3, the second pass is never used, and the stated bound is inconsistent with "linear" (m1).

## Q4 — The invocation is valid

**Genericity and GS (b).**
- GS (b)'s definition of generic (P/c6/proof-SEEDG-r2.md:L93) is identical to the target's at L33.
- GS (b) needs only the L89-90 preamble (Q proper, t ∉ Q, Q+t proper) plus genericity of both Q and Q+t.
- Rechecked:
  - s_lo >= (d+R)/2+1−p = (d−Delta0)/2+1;
  - s_hi <= p−(R−d−2)/2−2 = (d+Delta0)/2−1.

**No-wrap.** The conclusion of NW (L80-81) is verbatim the hypothesis of GS (a) (L91).

**The empty case is the actual-empty alternative, not a (QS)-window test.**
- If w avoids, x_t ∈ [lambda,U] by the canonical lift (L66).
- By NW and TS, x_t ∈ [s_lo,s_hi] (L96-97), computed from the actual Q.
- So an empty interval contradicts avoidance.
- This matches L77-79, L168-171, L175-176 and P/c6/proof-A0-r1.md:L94, L99-100. The (QS) window itself is never tested for emptiness.

**Case split of the Corollary.**
- If any run's interval is empty, case (a) applies.
- Otherwise every interval is a seed satisfying (QS) with a_t >= lambda({t}), so case (b) is met.

**Remaining hypotheses of the Corollary and of Theorem C0-all are met.**
- Canonical lifts: L66-67, via (ARC) and P0.
- SCW-G needs only quality seeds plus a_t >= lambda({t}) (L110, L146, L153).
- The pin step uses P0 and (QS) (L152-156).
- SL: L103-109.
- C0-all (A0-r1:L63-90) splits into three exhaustive cases:
  - (i) B <= g;
  - (ii) B >= g+1 and 3g+1 <= p, which is exactly the accepted scope of C0W (P/c6/proof-C0WB-r2.md:L55);
  - (iii) B >= g+1 and 3g+1 > p.
- No n_ev,al count condition is used (C0+ is not invoked), and no (A*) defect bound is used.

**NMH hypotheses needed by the imports, and where each holds.** All hold under the theorem's hypotheses (an NMH word with R <= 2p−3), and nothing is applied to non-NMH dihedral words.

| hypothesis | source | where it is used |
|---|---|---|
| k >= p+1 | NMH definition (P/README.md:L25) | SEEDG L119; c3 L23 |
| All reflection runs odd, so beta = 0 | NMH definition | GEN, GS, NW, P0, SCW-G, Kill lemma |
| Every run pure or a (1,1)-pair | NMH definition | (S), (M), (0.2'), (2.1), C0-all (3.1)/(B1+) |
| 1 <= B <= kappa−1 | NMH definition | kB, g >= 1; DF L50; the C0-all split |
| B <= A <= 2p−1 | NMH definition / normalisation | Lemma H empty/full (PAR-K0 L23-31); C0W step (2), L60 |
| Delta0 >= 3 (i.e. R <= 2p−3), equivalently (0.1) k >= 2kappa+3 since k = 2kappa+Delta0 | theorem hypothesis | GC; SEEDG L45; A0-r1 L33; C0-all (i)/(iii) |

## Q5 — Scope is right apart from the fixes above

- **Statement.** L109-110 states exactly: all normalized NMH words with R <= 2p−3, for every prime p >= 5. That is item (iii) plus the ZSI-B part (P/proof-MH.md:L179). It needs the qualifier in m5.
- **Disclaimers.** L4-6 and L123-124 correctly disclaim NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* and ordered Olson.
- **Overreach.** Only L119 ("supersedes", m6) and L122 (the reductions in the [I] assembly, m7).
- **Remarks.** (1) is incomplete (m2), (2) is correct, (3) is inconsistent (m1).
- **No computational premise.** The proof (L111-116) cites only GC, GS (b), NW, the proof of GS (a), and the A0-r1 Corollary.
  - Sec. 5 is labelled [F] (L5, L126, L145).
  - The E2 315-row table and all censuses are explicitly unused (L18-19).
  - The A0-r1 chain itself uses no finite result (A0-r1:L27).
- **Paths.** c3/…, c6/…, README.md, c2/proof-C2.md and ../../inverse-parity/proof-PAR-K0.md all resolve. The exceptions are L118 (m3) and L16-17 (m4).

## Counts
FATAL 0 / MAJOR 0 / MINOR 8

**Correctness, novelty, significance.**
- *Correctness:* I re-derived Lemma GEN (exact iff), the GC colouring class, walk and crossing, and the import chain. I found no mathematical gap. Theorem NMH-iii follows from parent-accepted imports, each used within its stated hypotheses. The [F] receipts agree, but I did not rely on them.
- *Novelty:* not assessed, since no search was requested; I make no priority or firstness claim.
- *Significance:* if accepted, this proof settles item (iii) and its ZSI-B part uniformly in p. It replaces the region-by-region and census route with a short structural argument: genericity is a two-term absolute-value condition, and a single-flip sweep crosses the window. Together with c2/proof-C2.md and the README Sec. 1 reductions, once accepted, it would give NMH(p) and MIX_DEF_HIGH(p). It does not by itself give RUNS(p) (whose o_F <= p side runs through the unreviewed Corollary RL) or ordered Olson for D_(2p), which also needs INV*(p).
