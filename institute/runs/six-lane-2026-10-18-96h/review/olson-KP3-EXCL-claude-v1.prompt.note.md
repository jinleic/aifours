# KP3-EXCL v1: independent hostile review

**Boundary.** This review is reasoning only, on the pasted text. I used no tools, files, computation or delegation. I did not recompute any SHA256, byte or line metadata, so the review covers the text as pasted. I did not take any `[RE-DERIVED]`/`[NEW]` label, package summary or UH excerpt on trust; I re-derived every step below myself. All claims, including my observations, remain **CANDIDATE_UNVERIFIED**, and the parent owns the verdict. `L###` is a physical line of `…/terminal-pplus1-kp3-exclusion/proof-KP3-EXCL-v1.md`; `pkg L##` is a line of the review package.

## Verdict

**FATAL 0 · MAJOR 0 · MINOR 2**, plus editorial items that I did not count.

The proof of the stronger word-form assertion (L19–21) holds. So does KP3-EXCL at the full existential NF antecedent, which follows from it. Both are relative to these interfaces at their literal scopes:
- NF, Sec. 0 output only
- GRX, if-direction
- RS(b)
- classical Cauchy–Davenport

The proof uses no CT, UH, KP2, PP1, Lev, S(p) or inverse-sumset premise. It makes no multiset-only, other-cell or whole-upper-half inference. Neither MINOR affects correctness.

## Claim-by-claim

**§0–1 Setup**

- **C0, word form ⇒ theorem (L14–22): OK.**
  - An admissible NF u is an avoider (PM*, original→reduced) with p+1 odd blocks, Σh_i=2 and the empty-run rule.
  - This covers *every* admissible NF, as ZX-2 requires.
  - The word form itself never uses NF.
- **C1, parameters and SR3 (L38–50): OK.**
  - F=(p+1)+4 and R=3p−7.
  - Since all l_i are odd, δ_GRX=#{f_i=0}=p+1−Φ, so C_max=Φ+4. This holds whether the two extra pairs share a block or not.
  - SR3 is exactly the set of even n in [2p−2m−4, 2p−2m]∩[0,R]. The binding condition is 2p≤3p−7, i.e. p≥7.
  - T(z_P)=Σ_{i∈P}τ_i follows from Σθ_i=0.
  - GRX is invariant under z↦−z, so z_P with z_1=−1 is legitimate.

**§2 Dominant class**

- **C2, Lemma M (L55–59): OK.** If a pair were equal, the list would contain q+1 consecutive copies, which exceeds the cap.
- **C3, Lemma P (L61–66): OK.**
  - n=max(p−1, 2p−4−2m) is even, lies in the SR3 window for 1≤m≤(p+1)/2, and is ≤2p−6.
  - If μ≤2p−6, Lemma M applies with N=R and q=p−1, since 2p−2≤3p−7.
  - The filler count n−p+1 lies in [0, p−5].
  - RS(b) with K=p−1 on the p−1 nonzero swap differences gives all p residues.
- **C4, Lemma U (L68–73): OK.**
  - 2(2p−5)>3p−7, so each z has a unique dominant value and the class is common to all z.
  - The class {0} is excluded by the arc of runs j+1..j′ between two equal-valued blocks. It has m=1 and T=0, and n=2p−6 is admissible.
- **C5 (L75–81): OK.**
  - A≤2p−1 comes from the all-plus pattern with C=0, n=2p≤R.
  - A′≤p−3 comes from C=4, n=2p−4.
  - φ_a=A−d and φ_{−a}=A′+d.
  - λ=p−2−b and Λ−λ=p−3+δ.

**§3 The m=3 window**

- **C6, MW3 and (W3) (L85–98): OK.**
  - w0≤p−2<p−1≤K≤φ, so every J⊆W is usable and G_s is not truncated.
  - R−K∈{2p−6, 2p−8, 2p−10}, which is exactly the m=3 window.
  - The translates are spaced by 2s and 4s, both nonzero because s≠0.
  - Cauchy–Davenport then forces w0+q≤p−1.
  - If φ≥p+3, then q=3 and φ≥2p−3.
  - φ=p+2 can occur only at p=7, and there it gives w0+q=2p−7≥p, a contradiction.
  - The gap is p+1+δ. Complementation preserves m=3 and swaps the low/high type.

**§4 Super-heavy run, light sets, empty runs**

- **C7, toggle path (L102–105): OK.** I checked it for general N≥8 and explicitly at N=8: {6,7,0},{2},{4} → … → {1},{3},{5,6,7}.
- **C8, the run h (L106–108): OK.** A low→high step that removes a run needs β_i≥p+1+δ, but β_i≤A′≤p−3. The traversal direction does not matter.
- **C9, light sets and the range of c (L110–115): OK.**
  - A high set P′ that avoids h gives 0≥3+2δ, which is impossible.
  - If λ≤−1, then A′≥p.
  - So c∈{1,…,5} is exhaustive, b=p−1−c≥1, and λ=c−1, consistent with erratum 8f1ea491.
- **C10, at least two empty runs (L116–118): OK.** The case Q+=∅ is covered by λ≥0.
- **C11, (L3) (L118–119): OK.** W3-high implies W-high, which is impossible for a set avoiding h, so d(P)≤c−3.

**§5–6 Subset sums and cases c=1..4**

- **C12 (L123–136): OK.**
  - RS(b) with K=b gives |G|≥b+1, and b+1≤p−1, so |M|≤c and 0∉M.
  - The n=A+1 uses rely only on nonempty J.
  - The distinction between G and G_nonempty is respected.
- **C13, c=1 (L140–143): OK.** Optional shortcut: the all-plus pattern at j=2 has n=A+1 and forces 2∈M. That already contradicts M={1} using a single empty run.
- **C14–C16, c=2, 3, 4 (L145–157): OK.** The forced sets are {1,2}, {1,2} and {1,2,3,4}, and the pair steps force 0, 0 and 5 respectively. Window details are in the table below.

**§7 Case c=5**

- **C17, part (a) (L168–173): OK.**
  - For 3≤t≤p−4, M is exactly {1,2}⊔I_t.
  - Its components are bounded by {0,3} and by {t, t+4}, with t+4≤p.
  - So I_t is the only 3-interval in M, and its start is unique because p>3.
  - An adjacent pair forces t=0; a non-adjacent pair forces t=−1. Both are impossible.
- **C18, part (b) (L175–177): OK.** t+s∈{3,4}, so both pair windows contain 6. 6∉{0,…,5} mod p for p≥7.
- **C19, part (c) (L179–183): OK.** A non-adjacent pair forces {1,…,6}⊆M. C_N is triangle-free, so the empties are exactly two and adjacent.

**§8 Final contradiction**

- **C20 (L187–190): OK.** There are at least (p−2)−(p−6)=4 pure-a runs, and d(Q)≤4 forces |Q|=4 with α_i=1.
- **C21, cycle lemma (L192–204): true, but two steps are asserted without argument (MINOR-1).**
  - The independence number Σ⌈s_i/2⌉ leaves only the shapes (4) and (2,2).
  - In the 4-path case, E={x,y} would close a 6-cycle.
  - I verified the 2+2 constructions, including the other gap of size N−6≥2.
- **C22 (L206–209): OK.** P⊆Q∪E avoids h and has m=3, and d(P)=|P∩Q|≥3>2=c−3.

## Requested checks

**p=7 boundary.**

- **Sizes:** N=8, F=12, and R=14=2p, so A≤13 is a genuine constraint.
- **SR3 windows:**
  - m=0: {14, 12, 10}
  - m=1: {12, 10, 8}
  - m=2: {10, 8, 6}
  - m=3: {8, 6, 4}
- **Lemma P:** uses n=8, 6, 6, 6 for m=1..4; the m=4 window is {6, 4, 2}.
- **Lemma M:** q=6, 12≤14, μ≤8, and 2 letters stay unpaired.
- **Lemma U:** the dominant multiplicity is ≥9, and the U arc uses n=8.
- **MW3, φ≥10:** K∈{6, 8, 10} (n=8, 6, 4) gives w0≤3 and φ≥11.
- **MW3, φ=9:** w0=5 and K∈{6, 8}, so w0+q=7=p. The equality case is covered.
- **Section 4:** A=8+c and b=6−c. At c=5: b=1, |M|≤5, λ=4, and the L3 bound is 2.
- **Section 5:** the smallest n used is 6≥b.
- **Section 8:** there are 5 nonempty runs outside h, at most 1 holds the deviant, and |Q|=4.
- **Cycle lemma on 8 vertices:** the path case needs N≠6, and in the 2+2 case the other gap has 2 vertices.
- **Unused observation:** at c=5, G={0,ω} and M={1,…,5} force ω=−1, so the sole deviant is ρ_{−a}.

**Filler windows.** Write n=2p−2j. A length is free iff j≥(6−c)/2. The lower bound n≥b always holds, because the smallest n used is 2p−8≥p−2≥b.

| c | A | b | free j | n=A+1 at | non-free uses |
|---|---|---|---|---|---|
| 1 | 2p−5 | p−2 | ≥3 | j=2 | single empty, j=2 |
| 2 | 2p−4 | p−3 | ≥2 | none (A+1 odd) | none |
| 3 | 2p−3 | p−4 | ≥2 | j=1 | all-plus j=1; single empty j=1 |
| 4 | 2p−2 | p−5 | ≥1 | none (A+1 odd) | none |
| 5 | 2p−1 | p−6 | ≥1 | j=0 (unused) | none |

**Adjacency windows.**
- All-plus pattern: j∈{0, 1, 2}.
- Single empty run or adjacent pair: j∈{1, 2, 3}.
- Non-adjacent pair: j∈{2, 3, 4}.

The pair lengths used in c=1..4 are j=3, 2, 2, 3. Each lies in both windows, so no adjacency split is needed. In c=5 the adjacent and non-adjacent cases are treated separately, each inside its own window.

**Other requested checks.**
- **ρ_0 among deviants:** ρ_0 has ω=−1/2≠0, so it is a valid RS(b) term. In Lemma P and MW3, signed value 0 is an ordinary value with weight −s≠0.
- **a=0:** it arises only in Lemma U's {0} branch, which is excluded. So 2a is a unit at L123.
- **Extra-pair distribution:** it enters only through C_max=Φ+4.
- **n=A+1 uses:** none of them treats 0 as having a nonempty representation.

## Findings

**MINOR-1: cycle-lemma justification (L197–198, L200–201).** Both steps are true, but the proof asserts them without argument.

- **L200–201.** Replace "Otherwise E occupies precisely a gap of length2" with: "Otherwise both E vertices have a Q-neighbour. Being adjacent and outside Q, they lie in one gap between the pairs. Only a gap's end vertices have Q-neighbours, a one-vertex gap cannot hold E, and the two ends of a gap with ≥3 vertices are non-adjacent. Hence E is an entire gap of exactly two vertices."
- **L197–198.** Add before the 6-cycle conclusion: "Interior path vertices have no non-Q neighbour and each endpoint has exactly one, so the two E vertices attach to different endpoints."

**MINOR-2: import-table scope (L236; pkg L30).**
- **Problem:** the pin "fewodd addendum1 line12" accepts ROT-FEW-E together with SHgen-E. That acceptance records a REFL scope of k≤p, and this cell has k=p+1.
- **Why correctness is unaffected:** the proof uses only the Sec. 0 normal-form output, which does not depend on k. The word form (L19–21) does not use NF at all.
- **Risk:** as written, the row invites a mis-scoped reading.
- **Length preservation:** this comes from ROT-few-E-v4 L37, not from the literal wording of lowodd item 2.
- **Repair, appended to the NF row:** "Only the Sec. 0 output is used: PM* original→reduced, odd blocks, empty-run rule, same length and rotation multiset (ROT-few-E-v4 L37). No SHgen-E/REFL content, recorded for k≤p, is invoked at k=p+1."

**Editorial (not counted).**
- **E1 (L39–40):** "signed contribution depends only on f_i" is undefined. Say instead: "GRX depends only on z and on the even C in [Φ, C_max]."
- **E2 (L35 vs L125):** `t` means both a term count and T(z)/(2a). Rename it at L35.
- **E3 (L93):** note that φ=p+2 occurs only at p=7.
- **E4 (L72):** name the arc as runs j+1..j′; either arc works.
- **E5 (L116):** add "(trivial if Q+=∅, since λ≥0)".
- **E6 (L195):** change "path of length4 vertices" to "a path on four vertices". The components are paths because |Q|<N.
- **E7 (pkg L63):** change "leave every rotation positive" to "signed value equals value".

## Import domains and labels

- **NF:**
  - PM* is used only in the original→reduced direction.
  - K1, DAV and SHgen-E are unused.
  - κ̂ is integral (ZX-1), the NF quantifier is existential (ZX-2), and k≥2 (ZX-3).
- **GRX:** only the "if" direction is used, with the same group law (lowodd M2) and with empty runs allowed.
- **RS(b):** in all three uses K is an integer equal to the number of nonzero terms (p−1, w0 and b). p≥7 is inside ROW's range of p≥5.
- **Cauchy–Davenport:** applied to nonempty sets; the second summand has q≤3 distinct translates.
- **UH excerpts:** not needed.
  - Secs. 2–4 match the UH specialisation at κ=p−3, e=3: 2κ+1=2p−5, p+κ=2p−3, gap p+1+δ.
  - I checked each step without relying on UH.
- **Labels:**
  - Every `[RE-DERIVED]` section is self-contained.
  - The `[NEW]` labels match the scope's pre-freeze disclosure (scope L20–25) and are not novelty claims.
  - I found no label error.

## Not covered

- **Other mathematics:** other terminal cells, the whole upper half, reflection rigidity, INV*, REFL or full ordered Olson, o_F assembly.
- **p=5:** not covered. The proof correctly relies on p≥7 at 2p≤R, φ≥p+2, N≥8, 2p−8≥p−2 and 6∉{0,…,5}.
- **Scope-excluded claims:** multiset-only non-existence, novelty or priority.
- **Verification not done:** Lean or human review, and hash or byte checks.
