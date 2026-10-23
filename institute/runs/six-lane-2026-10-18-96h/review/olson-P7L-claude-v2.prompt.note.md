## Result (governing parent erratum and worker erratum 1 applied)

**0 FATAL / 0 MAJOR / 0 new MINOR.** The governing Codex MINOR (proof LF329–332) is confirmed. It does not carry any proof step, and the parent erratum disposes of it correctly. It is not counted again here.

## Claim-wise verdicts

| Claim | LF | Verdict |
|---|---|---|
| Lemma 1 (SR) from NF + GRX | 47–56 | Correct. Φ=2m, δ=8−2m, C_max=2H+2m, T(z)=T(P), n=14−C |
| Lemma 2 windows | 58–61 | Correct, all ten windows |
| Lemma 3 frame (a)–(e) | 63–96 | Correct. Covers t∈{0,1}; label lists at LF90–93 are complete; u1 ≥ 6/9/8 |
| Normalisation, Lemma 4 | 97–111 | Correct. Swapping the two arcs keeps every label, including Z's ±1 |
| Lemmas 5–7 | 120–145 | Correct |
| Lemma 8 (with erratum-1 item 3) | 147–159 | Correct |
| Lemma 9 and lift framework (with erratum-1 item 2) | 161–186 | Correct. Δ∈[M0, 28−ν0−B*] gives Δ=14. Complement interval has length 28−2B*≤12. θ is unique because 2(14−R)=12 or 8 <14. An empty-run θ is even and ≢0 (mod 7) |
| **Theorem P7L-2, cell (2,7)** | 188–267 | **CORRECT and complete relative to the imports below** |
| **Theorem P7L-1, cell (1,7)** | 272–316 | **CORRECT and complete relative to the imports below** |
| Route remarks (M1)–(M3), (R1)–(R3) | 321–342 | Not premises. The N=8 arithmetic in (M1) is correct. (M2) is correct only as amended by the governing erratum |

## Independent checks of the steps the proofs rest on

**Cell (2,7)**
- **Lemma 2.1(i).** A minimal J contains no zero-signed subset. All 10 letters contain Z0, so J is not the full set and |J|≤8, which lies in Win_3. For v=0, use Z0 when m=2 and ∅ when m=3.
- **Lemma 2.1(ii)/(iii), single-signed sets.**
  - The unrealised endpoints are exact: v=0 at m=2 and v=B* at m=3.
  - The two single-signed cases cannot both hold, because R>0.
- **(F2).** Every move takes from a gap of size ≥2, and every intermediate set has m=3. Step (d) carries {x,x+2,x+4} to {x+1,x+3,x+5}.
- **(F3), modified additive constant.**
  - {0,3,6} and {1,4,7} are independent and disjoint.
  - Their union {6,7,0,1}∪{3,4} has m=2, so it lies in Cl but not in Fp.
  - P3={0,1,3,4,6} has m=3, and (P3, P3∪{7}) is a pair in Cl, so f(union)=f0.
  - Lemma 9(b) with M0≥3 then gives f0=2f0, hence f0=0.
- **(F4) and (F5).** Correct.
- **CLAIM, case letters(J_S)≠A.** U′(J_S)≤−1−ν0: a two-signed set has hi≤−1, and an all-negative set with m=2 has hi=−2.
- **CLAIM, case ν0=0.** Both runs of J_S are empty, so each θ is even and nonzero. Θ(J_S)≤0 then forces θ_(2)≤−2.
- **The exception occurs at most once.** If it held for both alternating sets, A would lie in two disjoint letter sets, so A=∅ and ν0=0, which the exception excludes.
- **Conclusion.** B*−2ν0−14 ≤ −5−2ν0, so B*≤9<10≤B*, a contradiction.

**Cell (1,7)**
- **Lemma 3.1/3.2.** For m∈{2,3}, any J works since |J|≤R=8, so x=y=ν(P) mod 2 even for single-signed P. For m=1 and two-signed P, v=0 comes from Z0. The only exception is m=1 with letters(P)=A, where hi=0.
- **(G2)–(G3).** (G2) reduces every P in G to a singleton without leaving G. In (G3), the sets {0}, {2}, {0,2} with M0≥1 (from q1≤1) give f≡0, so θ_i=U′({i}).
- **(G4) and the final sum.**
  - (G4) gives Θ(all) ≥ −6−2ν0.
  - If ν0≥1, the singleton bounds give Θ(all) ≤ −7−8ν0.
  - If ν0=0, every θ_i≤−1 and every empty-run θ_i≤−2, so Θ(all) ≤ −8.
  - Both cases are contradictions.

**Cases covered**
- t∈{0,1} and every label multiset. B*=14 arises only at κ=2, t=1, E=4, and Lemma 9(a) excludes it.
- Two-signed and single-signed sets.
- Empty runs, which enter only through Lemma 9(e).
- ν0=0 and ν0≥1.
- All rotations equal: no lemma assumes non-constant letters.

## Governing correction (applied)

- **LF331 as printed is unsupported.** For a singleton with letters({i})=A, Lemma 3.2 (LF288) gives only U′({i})≤−ν0, not ≤−1−ν0.
- **The parent qualification matches what the proof uses at LF308–314:**
  - If ν0≥1, at most one run has letters({i})=A, since different runs have disjoint letter sets.
  - If ν0=0, every such run is empty, and each has θ_i ≤ −2.
- **Wording.** At ν0=0 there can be several exceptional runs, so read the erratum's "the exceptional run" as "each exceptional run". LF332's "at most one exceptional unit" then applies only when ν0≥1; at ν0=0 there is none.
- **Consequence.** Only the route summary is affected; neither theorem changes.

## Dependencies

- **P7L-1 uses:** NF Sec. 0 (imported at p=7 as in R7 LF5 and K0T LF5), the GRX if-direction, and SC0 (n=14, length ≥9).
- **P7L-2 uses the same, plus** ZSTRUCT in (S′) at (k′,κ′)=(6,1), only when t=1. (S′) is a setting about sequences only, and every hypothesis holds:
  - R=10 odd terms;
  - (S1) at κ′=1 follows from Lemma 3(b);
  - t=1≤κ′;
  - L=8 ≥ 2p−k′ = p+1;
  - the generator is odd and W≤13.
- **Lemma FB is not needed.** ZSTRUCT alone gives s_j≤2t−1=1, n₋≥1 and S(N)≡n₊ (mod 14), which force n₊=n₋=1 and s₁=1. W≤12 follows from parity.
- **Nothing below range is a premise.** No PL result, Theorem P, or FCW/SCW/USK/K1/K2/K3/R7/TCW lemma is used. The LOWER and FCW errata enter only as conventions (m(P), θ via explicit pairs) and as derivation patterns that the proof redoes.
- **No unresolved load-bearing dependency.** Both theorems hold relative to these imports.

## Process (preserved; not mathematics)

- **Freeze wording.** "Before any derivation" in proof LF5, and the same phrase in scope LF1 and package LF25 and LF70–71, stands only as a preregistration-order qualification.
  - Scope LF77–79 discloses two pre-freeze unwritten observations: "7=4·2−1" and "PL excludes p=7".
  - That falls short of the strict rule in transition LF36.
  - The proof's own exposure paragraph (LF27–30) does not repeat them.
- **Replacements.** Two in-memory replacements were made before the file was created; erratum-1 LF6–9 corrects proof LF379–381.
- **Byte estimates.** The partial-range estimates in package LF43–45 were inherited and not remeasured by the worker. The parent froze the actual bytes and hashes.
- **What I did not check.** I verified no hash, byte count, timestamp or tool provenance.
- **Computation.** None is a premise. This review was done by hand from the pasted text.
- **Priority.** No novelty or priority is claimed, and none was assessed.

## Boundaries

This covers the two cells only. It is not a result for the whole of p=7, for any other κ̂, k or p, or for full ordered Olson. It carries no Lean, human-review or runtime authority and does not approve the research target.
