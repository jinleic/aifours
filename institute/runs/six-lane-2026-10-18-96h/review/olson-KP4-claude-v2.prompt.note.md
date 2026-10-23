# KP4 hostile mathematical review

**How I read the texts.**
- `proof-KP4-v1.md` is read with author erratum-1 applied. E1 replaces lines 206–207. E2 replaces the heading at line 80.
- `obstruction-KP4-p7-v1.md` is read with the parent erratum v1 governing lines 58–60 (F1) and 61–63 (F2).
- Inputs are used only at their literal scopes: NF, GRX (if direction), RS(b) and Cauchy-Davenport (CD). UH-A is used only inside the obstruction note.
- I re-derived everything by hand from the quoted texts. I used no tools, opened no files and ran no computation. I took no hash, byte count or label as evidence.

All files are in `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/terminal-pplus1-kp4-exclusion/`.

## Verdicts (recommendations; the parent owns acceptance)

| Claim | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| (A) Theorem KP4-A, every prime p≥11, word form | Correct at the full antecedent | 0 | 0 | 0 |
| (B) Prop. KP4-7P, p=7, all rotation letters equal | Correct with E1 | 0 | 0 | 1 |
| (C) Lemma KP4-7N, p=7 necessary conditions | Correct as necessary conditions | 0 | 0 | 1 |
| (D) Lemma PR, Lemma B1, R7, F1–F4 | Accept with wording fixes. PR is correct; B1 is correct on the R7 range; R7 is open and not claimed; F1–F4 arithmetic is correct | 0 | 0 | 5 |
| Erratum-1 self-description | Accept with fix | 0 | 0 | 1 |
| **Total** | | **0** | **0** | **8** |

## 1. Re-derivation of claim (A), proof §§1–6

### SR4 (§1)

- With k=N=p+1 and κ̂=p−4: H=3, F=p+7, R=3p−9.
- All l_i are odd, so l_i≢f_i exactly when f_i=0. Hence δ_GRX=N−Φ and C_max=Φ+6.
- This is the same for the three possible H=3 distributions (one 7; 5+3; 3+3+3). Nothing else about block lengths or block positions is used anywhere in the proof.
- Admissible lengths are n=2p−2j with j∈{m,…,m+3}.
  - n≤R is automatic for p≥9.
  - n≥0 holds because j≤(p+7)/2≤p.
- Φ(z_P)=2m(P).
- T(z_P)=Σ_{i∈P} τ_i, using Σθ_i=0.
- τ_e≠0 on every empty run, by the empty-run rule.

### §2: pairing, dominant class, ordinary window

- **Lemma M** holds: the capped total is ≥2q in both branches, and pairing x_i with x_{i+q} never pairs equal values.
- **Lemma P** holds.
  - n=max(p−1, 2p−6−2m) is admissible: it is j=(p+1)/2∈[m,m+3] in the first case and j=m+3 in the second.
  - Lemma M needs 2(p−1)≤3p−9, i.e. p≥7.
  - Fillers needed: max(0, p−5−2m)≤p−7, which the unpaired letters supply.
  - RS(b) with K=p−1 on the p−1 nonzero swaps gives all p residues.
- **Lemma U** holds.
  - 2(2p−7)>3p−9 for p>5, so the dominant class is common to all non-constant patterns.
  - The class {0} is excluded: two of the p+1 block values coincide, the arc between them has T=0, and n=2p−8 is j=4 at m=1.
- A′≤p−4, using m=0, j=3.
- A≤2p−1, using m=0, j=0, which needs p≥9.
- Under z_P the signed counts are A−d(P) and A′+d(P). The ordinary window (W) has gap 4p−14−(R−δ)=p−5+δ.

### §3: Lemma MW, all four lengths at m=e=4

- The omission counts are K=R−n=p−9+2j.
- The proof holds: the q translates Ks are distinct because 𝒦 spans at most 6<p and s≠0; RS(b) is applied with K=w0; CD combines them.
- **m=2** (all K≤2p−7 needs p≥8):
  - w0=p−2 gives 𝒦={p−1, p+1};
  - w0=p−3 gives 𝒦={p−3, p−1, p+1};
  - both give w0+q=p, so φ≥2p−5.
- **m=3** (needs p≥10): w0=p−2, p−3, p−4 give w0+q=p+1, p+1, p. Hence φ≥2p−4.
- **m=4**, covering lengths 2p−8 through 2p−14 (K=p−1 through p+5):
  - if φ≥p+5 then q=4, so w0≤p−5;
  - otherwise 2p−7≤φ≤p+4, which forces (p,φ)=(11,15): there 𝒦={10,12,14}, w0=9, and 12≥11 excludes it;
  - hence φ≥2p−4.
- The strong gap is 4p−8−(R−δ)=p+1+δ. Complements swap low and high: d(P^c)=A−A′−d(P).

### §4: toggle path, super-heavy run, light sets, empty runs

- **Toggle path.** At N=12 the path is: add 11, 10, 9, 8; remove 0; add 1; remove 2; add 3; remove 4; add 5; remove 6; add 7.
  - Every intermediate set is one long interval plus three of {1},{1,2},{2},{3},{3,4},{4},{5},{5,6},{6}, separated by unselected runs. So m=4 throughout.
  - The same holds for every N≥12.
- **Super-heavy run.** Some step crosses the gap p+1+δ. A removal step would need β_i−α_i≥p+1+δ, impossible since β_i≤A′≤p−4. So some run h is added with d_h≥p+1+δ.
- **Light sets.**
  - A high set avoiding h would give A≥(p+1+δ)+(2p−7−A′), while A=3p−9−δ−A′. Together these give 0≥3+2δ, a contradiction.
  - λ≥0, since otherwise every one of the p singletons ≠h is low with d_i≤−1, giving A′≥p.
- **Exhaustive range for A.** A=2p−8+c with c∈{1,…,7}, b=p−1−c, λ=c−1.
- **Empty runs.** p=|E|+|Q|+N_B and N_B≤b, so |E|+|Q|≥c+1. Also |Q|≤d(Q)≤c−1. Hence |E|≥2.
- **Strong bounds.** The strong-high floors are 2p−5−A′≥p−1≥10>6≥c−1. So:
  - L2: d≤c−3 on m=2 sets avoiding h;
  - L34: d≤c−4 on m∈{3,4} sets avoiding h.

### §5: subset-sum interface

- |G|≥b+1, so |M|≤c and 0∉M.
- When the negative side lies inside E, every letter keeps its value. A selection has sum 2a(−j+Σ_J ω).
- |J|≤b≤p−2≤2p−12≤n (p≥10), so the only restriction is |J|≥r=8−c−2j.
- The free and (N1) tables are correct. The j-ranges are correct: all-plus 0–3; one empty 1–4; two empties 1–4 (adjacent) or 2–5 (not adjacent); three empties m…m+3.

### §6: cases c=1..7 (all checked)

| c | Forced by all-plus and one empty run | Closing contradiction |
|---|---|---|
| 1 | t=−3, M={1} | A pair at j=4 (m=1 or 2) puts −2 in M |
| 2 | 3∈M; t=−1; M={2,3} | A pair at j=3 puts 1 in M |
| 3 | M={1,2,3}; every pair forces t=−1 | L34 gives independence ≤2, so \|S\|=4 in two shapes; L2 gives Q=∅; three empties at j=3 put 0 in M |
| 4 | t∈{±1}, common to all empties | t=1: pair at j=4 puts 6 in M. t=−1: pair at j=2 puts 0 in M |
| 5 | [1,3]⊆M; t=1 (M=[1,5]) or t=−1 | Only (1,−1) pairs survive, so \|E\|=2 and \|Q\|=4 one-letter runs; L2 (≤2) and L34 (≤1) fail on every component shape |
| 6 | t∈{1,2} | Only adjacent (1,1) pairs survive; no triangle, so \|E\|=2 and \|Q\|=5; L2 (≤3) and L34 (≤2) fail |
| 7 | Step 1: t≤3 | Step 2: adjacent s≤3, non-adjacent s=2. Step 3: M=[1,7], \|E\|≤3, \|E\|=3 only consecutive. Step 4: \|Q\|∈{5,6}; L2/L34 fail, with e2 supplying the third interval |

### Smallest primes

| Quantity | p=11 | p=13 |
|---|---|---|
| N, R, F | 12, 24, 18 | 14, 30, 20 |
| Lemma P bound φ≥2p−7 | 15 | 19 |
| A′≤, A≤ | 7, 21 | 9, 25 |
| MW2 | w0=9 (q=2), w0=8 (q=3) each sum to 11, so φ≥17 | φ≥21 |
| MW3 | K∈{8,…,14}≤15; w0=9,8,7 fail, so φ≥18 | φ≥22 |
| MW4 | φ=15: sum 12. φ=16: 12. φ=17: 11. So φ≥18 | K≤18≤φ, q=4, so φ≥22 |
| Gap / d_h bound | 12+δ | 14+δ |
| 2p−5−A′ vs c−1 | ≥10 > 6 | ≥12 > 6 |
| 2p−12 ≥ b | 10≥10−c | 14≥12−c |

At p=11, every integer used is at most 10. The one exception, s+5=11≡0 in c=7, is handled in the proof.

## 2. Re-derivation of claims (B) and (C), p=7

### Claim (B): pure rotations

- **Parameters.** N=8, R=12, F=14. SR4 gives:
  - m=0: n∈{8,10,12}
  - m=1: {6,8,10,12}
  - m=2: {4,6,8,10}
  - m=3: {2,4,6,8}
  - m=4: {0,2,4,6}
- **Attained set.** [max(−ν, ν−α), min(ν, 12−α−ν)] is correct.
- **R1–R3:**
  - R1 (arcs, m=1): α=6 at ν=3 gives [−3,3].
  - R2/R3 (m=2 and m=3): α=4 gives [−2,2]∪[0,4]; α=6 gives [−3,3]; α

=8 gives [−2,2]∪[−4,0]. Each union is 7 consecutive integers, so it covers every residue mod 7. The values ν∈{2,3,4} lie in both V_2={2,3,4,5} and V_3={1,2,3,4}.
- **Empty runs.**
  - For α=0 and m=1 the attained set is {3,4,5,6}, so t(e)∈{1,2}.
  - For α=0 and m=2 the attained set is {2,3,4,5}. It contains every possible pair sum {2,3,4}, so no two empty runs are non-adjacent.
  - C_8 has no triangle, so |E|≤2, and |E|=2 only for two adjacent empty runs.
- **Profile completeness:**
  - |E|=0: every r≥1, so r≤5. Distributing the excess 4 over 8 parts gives exactly the 5 listed profiles.
  - |E|=1: r=6 is excluded by R1. Distributing the excess 5 over 7 parts gives 7 partitions; removing (6,1^6) leaves the 6 listed.
  - |E|=2: parts lie in {1,2,3,5}. Parts 4, 6, 8 are excluded by R2 using a non-adjacent empty run. A part of 7 forces an m=2 set holding 8 letters. Distributing the excess 6 with parts in {0,1,2,4} gives the 6 listed.
- **Contradictions.** I checked every listed contradiction.
- **Effect of E1.**
  - The original lines 206–207 named the arc {0,1,2}, which holds 0+5+2=7 letters, so the original text was wrong.
  - E1's arc {7,0,1} holds 1+0+5 or 5+0+1 = 6 letters, which is correct. E1 is needed.

### Claim (C): Lemma KP4-7N

- **(i) Lemmas P and U hold at p=7.**
  - Lemma M applies with q=6=R/2 (2q=12≤12, μ≤6).
  - n=6 is admissible for every m=1..4, and no fillers are needed.
  - Lemma U holds since 14>12; the class {0} is excluded via n=6=2p−8 at m=1.
- **(ii) A′≤3.** Use n=8 at m=0 with four letters a and four letters −a.
- **(iii) Window.** λ=A−7, Λ=7−A′, gap 2+δ.
- **(iv) A≥7.** Suppose A≤6, so λ≤−1.
  - Σd_i=A−A′≥0, so some singleton must be high.
  - Two high singletons would give A≥14−2A′≥8, a contradiction.
  - Otherwise seven singletons are low with d_i≤−1, so A′≥7, a contradiction.
- **(v) MW at p=7 is valid under E2**, since 𝒦 spans at most 6<7.
  - Running through all pairs (m,φ), only (2,8) and (3,8) give w0+q=7≥7; every other pair gives ≤6.
  - This matches F1.

## 3. Re-derivation of claim (D), obstruction note

### UH-A scope

- At p=7, κ=3 we have (p−1)/2=3≤3≤p−3=4 and H=e−1=3, so the cell lies inside UH-A's literal scope.
- UH-A gives A≥9. A non-constant multiset gives A≤11.
- Hence b∈{1,2,3} and δ=b−A′.

### Lemma PR

- ε(P)=A′+d(P) is correct.
- I recomputed all seven attained intervals:

| (m,ε) | (1,1) | (1,2) | (1,3) | (2,1) | (2,2) | (2,3) | (3,3) |
|---|---|---|---|---|---|---|---|
| Attained | [2,5] | [1,5] | [0,4] | [1,5] | [0,5] | [−1,4] | [−1,4] |

- The Allow sets and the |E| bounds follow correctly.
- Side remark: when δ=0, the bounds A′≤3 and A+A′=12 already give A≥9 without UH-A.

### Lemma B1

- n=12 forces J=B.
- n=10 needs |J|≥b−2.
- n=8 needs |J|≥b−4, so every J is allowed exactly when b≤4 (see finding D-1).
- For b=1: ω∉{1,2,3}, so ω∈{4,5,6}, i.e. x_u/a∈{2,4,−1}. This is correct.

### R7

- The reduction is correct.
- The body disclaims necessity and minimality (lines 7–9 and 74). The section heading conflicts with this (see D-4).

### F1–F4

- **F1 (as amended)** matches the (m,φ) table above.
- **F2 (as amended)** is correct. At p=7, Lemma MW gives no exclusion at m=4, so F1 supplies no strong m=4 window. No impossibility claim remains.
- **F3** arithmetic is correct.
  - Walk along the arcs [1,k]. The walk starts low and ends high, because the complement of a low singleton is high.
  - The crossing run has d_k≥2+δ.
  - All singletons can be low only if A−7≥2+δ.
  - So this argument yields a high singleton exactly when A<9+δ. That gives: A=9 needs δ≥1; A=10 needs δ=2; A=11 never.
- **F4:** |M|≤c=A−6∈{3,4,5} is correct.

## 4. Findings and minimal repairs

**FATAL 0 · MAJOR 0 · MINOR 8.** No finding changes a theorem, lemma, case split or inequality.

**B-1 (MINOR)** — `proof-KP4-v1.md:190–193`
- **Issue.** The text says "each an interval of 7 consecutive integers". For α=4 and α=8, each listed ν gives only 5 integers; only the union over the two ν values has 7 ([−2,4] and [−4,2]). R2 and R3 are unaffected.
- **Repair.** Read: "for each listed α, the union of the listed ν-intervals is 7 consecutive integers: [−3,3], [−2,4], [−4,2]".

**C-1 (MINOR, labels)**
- **Issue.** `:179` labels Lemma KP4-7N "[RE-DERIVED at p=7]", but `:220` lists it as "New". The heading at `:80` labels Lemma MW "[RE-DERIVED for this cell]", but `:219` lists the MW instances as "New". §5 (`:120`) has no label.
- **Repair.** Add one reconciling sentence in a new erratum: "Lemmas M/P/U, the window, Lemma MW and KP4-7N(i)–(iv) are re-derived; the MW2/MW34 instances, 7.2(v), the free/(N1) table of §5, §6 and §7.3 are new for this cell."

**E-1 (MINOR)** — `erratum-1-proof-KP4-v1.md:3–5`
- **Issue.** Erratum-1 calls itself "wording only" with no statement changes. But E2 (`:31`) widens Lemma MW's stated range from p≥11 to p≥7. The widening is mathematically correct and is needed for 7.2(v).
- **Repair.** Read: "E1 is wording; E2 corrects the stated scope of Lemma MW; no proof line changes".

**D-1 (MINOR, import scope)** — `obstruction-KP4-p7-v1.md:50–53`, Lemma B1
- **Issue.** "(n=8, every J allowed)" needs b≤4. The lemma relies silently on the UH-A range b∈{1,2,3}. The conclusion 3∈M would survive at b=5 via (N1), since 3≠0, but the parenthetical would not.
- **Repair.** At `:50`, read: "Let b=12−A∈{1,2,3} (the R7 range of §2, from accepted UH-A)".

**D-2 (MINOR)** — `:43–46` and `:72`
- **Issue.** R7a is framed as "the" missing enumeration. The weight description "may be −1 … or 0" understates the range: w_i=α_i−β_i∈[−A′,A]. The listed forbidden values are necessary conditions and are not shown to suffice.
- **Repair.**
  - At `:72`, read: "one possible completion is the weight-profile enumeration of §3".
  - At `:43`, read: "w_i∈[−A′,A], 0 on empty runs and possibly ≤0 on nonempty runs".

**D-3 (MINOR)** — F3 at `:64–65`, F4 at `:66–67`
- **Issue.** F3 says "forced only if" and F4 says "neither is available". These read as claims about every possible argument. The arithmetic only supports statements about this route, which is the same class of overstatement the parent erratum removed from F1 and F2.
- **Repair.**
  - F3: "the ordinary first-passage argument yields a high single run exactly when A<9+δ, and nothing otherwise".
  - F4: "neither is established at p=7 by the arguments here".

**D-4 (MINOR)** — heading at `:69`, and `proof-KP4-v1.md:223`
- **Issue.** "Smallest remaining claim" and "the smallest missing claim" conflict with `:7–8` and `:74`, which deny any necessity or minimality claim. UH parent erratum v2 item 2 made the same correction.
- **Repair.** Read: "Remaining unfinished target of this route".

**D-5 (MINOR, import scope)** — `:72–73`
- **Issue.** "Proving R7 together with the companion proof would give KP4-EXCL" leaves out UH-A. R7 covers only A∈{9,10,11}, and A∈{7,8} is excluded only by UH-A, which the companion proof does not use.
- **Repair.** Read: "together with Theorem KP4-A, Proposition KP4-7P and accepted UH-A; a KP4-EXCL obtained this way carries UH-A in its import list".

**Nits (not counted; each step remains valid):**
- `proof:199–201`: In profiles (4,2,1^6) and (3,3,1^6), the adjacent case is already an arc holding 6 letters, so R1 applies directly.
- `proof:135–136` (case c=1): all-plus (N1) at j=3 gives 3∈M, which contradicts M={1} directly.
- `proof:105`: after "add 1", only run 0 separates N−1 from {1,2}. m=4 is unaffected.
- `proof:5–6, :173` and `obstruction:13` say "proved". The candidate status in the file headers governs.
- `obstruction:61–62` (as amended): the remaining pure-case clause holds only inside the KP4-7P reductio, so it is vacuous. The replacement text also leaves a comma splice before "At p=7".

## 5. Import scope (kept separate from the mathematics)

- **NF.** Used only for:
  - avoidance, length and rotation multiset being preserved;
  - all blocks odd;
  - the empty-run rule;
  - H, κ̂ and R as functions of F and k.

  Terminal k=p+1 fits the cited text's condition 1≤k≤o. The k≤p restriction in the fewodd addendum applies to SHgen-E and REFL, which are not used.
- **GRX.** Only the "if" direction is used. Maximality of blocks is never used. Every even C in [Φ,Φ+6] is allowed, as GRX states. The sign convention matches M2.
- **RS(b).** Three uses, each with an integer K (p−1, w0, b) and nonzero terms.
- **CD.** Used only for the MW translates.
- **UH-A.** Used only in obstruction §2, and silently in Lemma B1 (D-1) and the completion sentence (D-5). All uses are within its literal scope.
- **Non-premises.** The proof file uses none of: KP3/UH candidates, PP1/KP2 endpoints, CT, Lev, S(p), ASSEMBLY-P, RPδ, UH-A. MW and SH are re-proved in the file, not imported.

## 6. Boundary

- **Supported:**
  - (A) for every prime p≥11;
  - (B) at p=7 when all rotation letters are equal.

  Both hold under the full existential NF antecedent (equivalently the stated word form), with any H=3 distribution and any placement of empty runs. (C), and PR and B1 in (D), are necessary conditions only.
- **Silent restrictions: none found.**
  - From the block data, only C_max=Φ+6 and τ_e≠0 are used.
  - Every empty-run configuration is covered: the independence classification in c=3, the no-triangle argument in c=6, the triple analysis in c=7, and |E|≤2 at p=7.
- **Not supported:**
  - KP4-EXCL at p=7 with a non-constant rotation multiset (R7 remains open);
  - any other (k,κ̂) cell;
  - the whole upper or lower half;
  - multiset-only non-existence;
  - o_F, REFL, INV*, ordered Olson, p=5.
