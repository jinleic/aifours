# Independent hostile review: UPAR5-C / UPAR5-T (proof-UPAR5-v1.md LF1–201)

**Method and scope.** Everything here was done by hand. I used no tools, code, computation, enumeration, network or delegation.

- I did not verify any SHA256, byte count, timestamp, chronology or exclusive-write claim. Source identity is taken from the supplied headers.
- I read both parts in order. Part-1's operative scope governs: the parent JSON LF1–189 and the exposure ack LF1–87. Part-2's UPAR4 scope LF1–79 is historical only.
- The three diagnostics were checked but never used as a cutoff.

## Verdict

**0 FATAL / 0 MAJOR / 6 MINOR new.** All six minors are FIX-level: notation, wording, citation or manifest.

- I re-derived every new deduction and found no discrepancy.
- **UPAR5-C: PASS.**
- **UPAR5-T: PASS**, at the declared import scope.
- No inequality, branch, diagnostic outcome or residual test needs to change.
- **Inherited:** the UPAR4 pre-freeze PROCESS MAJOR is permanent and uncured. UPAR5 carries it correctly, and this review does not cure it.

## 1. Re-derivations

### 1.1 Common data, parity, Room (LF28–77)

**Parameters and windows**
- h=κ+d and p=2κ+2d−1 give R=4κ+2d−2, and ℓ_m+M_m=δ+2.
- The lower window is low=Π0+2−y−2p. With Π0=e+R−ν this becomes e−2d+2−ν−y.
- ID: Θ(all)=B*−2ν−2p=e−2ν−2d.

**Endpoint types**
- ℓ_r=A0+2 and M_(r+1)=P0+2.
- In Q_r and P_(r+1) the opposite window entry is ≤δ−R<0.
- So x=ℓ_r−q, resp. x=M_(r+1)−q′. Hence sQ and sP are exactly the upper-endpoint slacks (≥0), with z≤A0 and zP≤P0.

**Range and sizes**
- r≤κ−d−1 gives b≤κ−2d−2 and A0≥2d+2.
- x0=h−r−1=(κ+2d−b)/2−1, using κ≡b (mod 2). y0=x0+1.

**Tail costs** (θ≤−1 on X∪Y)
- D_i≥0 by Lemma 1, and D_i is even because θ_i≡|L_i|.
- l_i≤D_i+1 in general, and l_i≤D_i when θ_i≤−2.

**Parity**
- e is even.
- From l=a−q+2β we get q≡a+l. With ν≡a and A0=2κ−2r even:
  - sQ ≡ −a−(a+l(Q))−l(Q) ≡ 0.

**Room**
- A0−B0=κ−3b+4d−2+e.
- κ−3b≥e+ν+E≥0 in the weak/weak case (WW), and κ−3b≥2d+2e in the strong-I/weak-Q case (SW).
- Therefore 0≤sQ≤Λ≤B0<A0.

### 1.2 Defect and Ω (LF54–61)

**Letter partition**
- A^c∖L(K) splits into the w letters in Q and the rest in X∪Y.
- A∖L(Q) splits into the wA letters in K and the rest in X∪Y.
- With zP=α′(K)+wA and z=α(Q)+w, this gives:
  - l(X)+l(Y)=zP+z−2W
  - β(X)+β(Y)=zP−W

**Defect identity**
- Sum the three pieces and set the total equal to e−2ν−2d (ID used inside the computation):
  - Θ(K)=P0−ν−zP−sP
  - Θ(Q)=A0−ν−z−sQ
  - Θ(X∪Y)=l(X)+l(Y)−2(κ+2d−b−1)−D_X−D_Y
- The result is exactly F−e=2W+sP+sQ+D_X+D_Y.
- The "≥2" is the literal R3 gap from UPAR3-Z, not a consequence of the identity.

**Ω**
- Ω=Γ+2(Λ−sQ)=Γ+2(sP+D_X+D_Y), and Ω is even.

### 1.3 Accepted bounds, re-checked from the pasted text

**Order**
- Θ(K)=Θ(I)+θ_u≤A0−ν−z0−1, or −2 when θ_u≤t_r(S)≤−2.
- Comparing with Θ(K)=P0−ν−zP−sP gives zP+sP≥z0+2b−2d+1, or +2 when I is strong.

**Count**
- Start from 2r−3l(J)≤Θ(J)=A0−ν−q−s_J.
- Use 2r−A0=2b, l=a−q+2β and ν=a+η. This gives a≥b+2q−3β+(η+s_J)/2.
- For a weak I: β(I)=z0−a+β′(I) and β′(I)≤wA, so z0≥2a+b−3wA.

**Pred**
- QQ-1 with ID: e≤κ−3b−ν−E.
- QQ-mixed with ID: z0+z≤(κ−b)/2−d−e.
- UPAR2 L3(a), using n≥b: κ≥3b+2d+2e.

**Cap**
- If a≤δ+1, then c=⌈(a+1)/2⌉≤κ−d+1, so level d+c is central and proper.
- The bound is ≤d+c−1≤d+a/2.

### 1.4 Positive-integer-gain selection (LF81–88)

**Integrality**
- gain_i=β_i−D_i/2 is an integer, and k=sQ/2 is a nonnegative integer.

**Choosing V**
- Failure-A is equivalent to Σ_Y gain>k.
- The positive-gain runs sum to ≥Σ_Y gain>k. So the family of positive-gain subsets with sum >k is finite and nonempty.
- Take V inclusion-minimal and set t=|V|≥1.

**Size bound**
- Suppose t≥k+2. Any k+1 members, each with gain ≥1, form a proper subset with sum ≥k+1>k, contradicting minimality.
- Hence 1≤t≤k+1.

**Gain-cost**
- Each member has β_i≥D_i/2+1, so l(V)≥D_V/2+t.
- Therefore Θ(V)=l(V)−2t−D_V≥−D_V/2−t.
- Empty Y runs have gain −D_i/2≤0, so they are never selected.

### 1.5 Centrality, Needed, P-small, ℓ-entry (LF90–106)

**Centrality**
- Minimality gives t≤k+1, and Room gives sQ<A0. Together r+t≤κ+1≤h−1, using d≥2.
- U=Q∪V⊂S′ has 1≤|U|≤h−1, so m(U)=r+t is central (UMR 252–253). Hence (Win) applies.

**Needed**
- ν+2+Θ(U)≥A0−z−sQ−D_V/2−t+2.
- Using D_V≤D_Y≤Λ−sQ and t≤sQ/2+1, this is ≥Ω/2+1.
- Ω>0 and even gives Needed ≥2>ε.

**P-small**
- M_(r+t)=κ+b+2t−2d, and q(U)=z+β(V)−β′(V)≤z+t+D_V.
- So M−R+q ≤ −3κ+b−4d+2+3t+z+B0.
- Substituting t≤A0/2+1, z≤A0 and B0=2b−4d+2−e gives ≤ −A0/2−8d+7−e ≤ −9d+6−e < 0.

**ℓ-entry**
- Only ℓ_(r+t)−q(U)=A0+2−2t−q(U) can reach Needed.
- Insert the exact Θ(Q). This gives Θ(V)+2t+β(V)−β′(V)≤sQ.
- That is equivalent to 2β(V)−D_V≤sQ, i.e. gain(V)≤k, which contradicts the choice of V.
- If ℓ−q also fell short, (Win) is violated outright.

**Result**
- **(A) 2β(Y)≤sQ+D_Y**, with sQ paid **once**.

### 1.6 Global Ω (LF110–133)

**Both weak (WW)**
- a+η≤κ−3b−e, combined with Q-Count, gives 2z≤κ−4b−e+3w−(3η+sQ)/2.
- Hence Ω≥κ+4d−2+2e+2wA−w+3η/2−3sQ/2.
- Using sQ≤B0−2W: Ω≥κ−3b+10d−5+7e/2+5wA+2w+3η/2≥15.

**Strong I, weak Q (SW)**
- z0≥a−β′(I)≥a−wA.
- Pred gives a+z−wA≤b+τMix/2−e.
- Combined with Q-Count: sQ≤τMix−2e−6z+6w+2wA−η.
- This yields Ω≥2b+8d−2+5e+10(z−w)−2wA+2η.
- α(Q)=z−w≥β′(K)=wA, because L(K)∩L(Q)=∅. So Ω≥2b+8d−2+5e+8wA+2η>0.
- τMix cancels. Even b≥2d−1 from the inherited interval suffices.

**Neither bound** depends on a parameter, prime-class, Γ or budget cutoff.

### 1.7 Orientations, with the Cap domain proved first (LF140–159)

**Strong I**
- X has θ≤θ_u≤t_r(S)≤−2, so β(X)≤l(X)≤D_X.
- Then zP+sP≤W+sP+D_X+(sQ+D_Y)/2≤B0−W.
- Strong Order gives zP+sP≥2b−2d+2=B0+2d+e. Contradiction.

**Weak I**
- Upper bound: zP+sP ≤ x0+B0−W−(sQ+D_Y)/2.
- Lower bound: zP+sP ≥ 2a+3b−2d+1−3wA. Together these give (C1).
- *Cap domain:*
  - Drop −w−(sQ+D_Y)/2≤0 and use 2wA≤B0. This gives a≤(κ+b)/4−5d/2+1−e≤κ/2−3d+1/2−e<δ+1.
  - So Cap is applicable before its use.
- *Empty count:*
  - β′(Y)≤α gives E(Y)≥y0−α−(sQ+D_Y)/2, and all of these empties are negative.
- *Cap applied:*
  - a+2α ≥ κ−b−sQ−D_Y.
- *Q-Count:*
  - 2α ≤ a−b+w−(η+sQ)/2.
- *Final chain:*
  - κ ≤ x0+B0−3b+2d−1+(2wA+D_Y/2)−η/2.
  - Then ≤ (κ+b)/2−5d+2−2e−η/2.
  - Then ≤ κ−6d+1−2e−η/2 < κ. Contradiction.

### 1.8 Cover and scope (LF163–173)

**The chain**
1. Every target NF has a frame (UMR LF111–112; UPAR LF38).
2. On T∖T4, UPAR4-R puts that frame in R4.
   - Q is weak by literal intersection.
   - I weak or strong exhausts the negative thresholds.
   - Both-strong is excluded by R_PAR LF271.
   - Weak-I/strong-Q is excluded by UPAR4 §2, inside the accepted UPAR4-R.
3. §3 gives Ω>0, §2 gives (A), and §4 gives a contradiction.
4. On T4, UPAR4-P applies.

The chain holds at exact scope: terminal k=p+1, SOME admissible NF, increasing-original-index avoidance, every frame, arbitrary extra pairs, and the genuine empty-run rule.

**No hypothesis deletion**
- The R4-specific tests κ>26d−10 and Γ≤0 are carried but never invoked. That is legitimate for a contradiction.
- No Γ>0-scoped UPAR4 statement is used as a premise. This covers Secs. 3–5 and verdict LF7 "whenever Γ>0".
- (A) is re-proved under Ω>0, which is itself proved, not assumed.
- §4 is re-derived from (A).
- Nothing is broadened by deleting hypotheses, and this review promotes no extension.

**Retained generality**
- e may be any even value, η∈[0,e], and labels may be nonunit (β, l and q count occurrences; ν carries the weights).
- B0 is arbitrary and Γ≤0 is allowed.
- There is no e=0, unit, sQ0, small-budget or Γ0 step anywhere.

### 1.9 Diagnostics (checked by hand; not a cutoff)

| (κ,p) | ⌊(p+7)/4⌋ < κ ≤ (p−3)/2 | d | 26d−10 | primality | in T∖T4 (and outside T3, κ>22) |
|---|---|---|---|---|---|
| (43,89) | 24 < 43 ≤ 43 | 2 | 42 | 2,3,5,7∤89; 10²>89 | ✓ |
| (47,97) | 26 < 47 ≤ 47 | 2 | 42 | 2,3,5,7∤97; 10²>97 | ✓ |
| (49,101) | 27 < 49 ≤ 49 | 2 | 42 | 2,3,5,7∤101; 11²>101 | ✓ |

Each cell is excluded as a uniform instance of the unbounded theorem. None is a premise, a feasible tuple, or an upper cutoff.

## 2. Per-claim results

| # | Claim | LF | Result | Finding |
|---|---|---|---|---|
| 1 | Target/antecedent; C and T statements | 9–26 | PASS | — |
| 2 | Common data, (Win), ID, all-run parity, m=size | 28–39 | PASS | — |
| 3 | R4 symbols, b-range, x0/y0, D_i even, tail bounds, sQ even | 41–52 | PASS | — |
| 4 | Defect identity, Λ, evenness | 54–58 | PASS | — |
| 5 | Γ literal; Ω=Γ+2(sP+D_X+D_Y), even | 59–61 | PASS | — |
| 6 | Order/Count/Pred/Cap at stated hypotheses | 63–72 | PASS / FIX | m4 |
| 7 | Room; 0≤sQ≤Λ≤B0<A0; b≥2d | 74–77 | PASS | — |
| 8 | Integer gain; minimal V; 1≤t≤sQ/2+1; Gain-cost | 81–88 | PASS / FIX | m1, m2 |
| 9 | Q∪V proper/independent/central | 90–91 | PASS | (m2) |
| 10 | Needed ≥Ω/2+1≥2 | 91–95 | PASS | — |
| 11 | P-small <0 | 96–100 | PASS | — |
| 12 | ℓ-entry ⇒ gain(V)≤k ⇒ (A), slack paid once | 101–106 | PASS | m1 |
| 13 | (O-WW) | 110–118 | PASS | — |
| 14 | (O-SW) | 120–133 | PASS | — |
| 15 | §4 framing relative to Γ-conditional UPAR4 | 137–138 | FIX | m3 |
| 16 | Strong-I contradiction | 140–142 | PASS | — |
| 17 | Weak-I contradiction, Cap domain first | 144–159 | PASS | — |
| 18 | UPAR5-C | 23, 163–170 | PASS | — |
| 19 | UPAR5-T | 24–26, 172–173 | PASS (import-conditional) / FIX | m4 |
| 20 | Diagnostics | 174–182 | PASS / FIX | m5 |
| 21 | Source/process/manifest statements | 3–7, 184–201 | PASS / FIX | m6 |

## 3. Findings (all MINOR / FIX; no math change)

- **m1: notation collisions** (LF83, 85, 103; LF84–103).
  - `k:=sQ/2` reuses the symbol of terminal `k=p+1` (LF13, 14, 24, 26, 170).
  - `t:=|V|` shares a letter with the thresholds `t_r` (LF42–43, 70) and with ENV's `t`.
  - Optionally, `(A)` sits next to the set `A`.
  - **Fix:** rename `k→kQ`, add "t=|V| is a selection size, not t_r or ENV t", and optionally relabel `(A)→(Agg)`.
- **m2: Sec. 2 hypotheses** (LF79–81, 90).
  - The lemma is headed "requiring Ω>0". It also uses (Room), at LF90 and through A0≥2d+2 at LF97–100.
  - (Room) rests on the orientation-specific (Pred) at LF66–67 and 76.
  - At LF90, "By (Room), t≤sQ/2+1" is a misattribution. That first inequality comes from minimality (LF85).
  - **Fix:** write "Under the Sec. 1 R4 data (Q weak; I weak or strong; hence Room), assume Ω>0", and attribute t≤sQ/2+1 to LF85.
- **m3: Sec. 4 wording** (LF137).
  - "re-states the conditional implication from the UPAR4 proof" can be read as citing UPAR4 Secs. 4–5 with Γ>0 deleted. Those sections are accepted only "whenever Γ>0" (UPAR4 verdict LF7).
  - LF140–159 in fact re-derive everything from (A) and Γ-free data.
  - **Fix:** "This section RE-DERIVES, as a new UPAR5 candidate step, (A) ⇒ contradiction in each orientation; UPAR4's Γ>0-scoped Secs. 3–5 are not premises."
- **m4: citation precision** (LF63–72; LF172–173).
  - The per-step sources are only inherited via UPAR4 erratum-v2 item 5.
  - "frame existence from accepted UMR" has no LF.
  - **Fix:** add the following, all physically present in part 2:
    - Order/Count: UPAR4 LF56–61 plus erratum 1.
    - Pred: UPAR LF146–155 and UPAR2 LF110–123.
    - Cap: UPAR LF102–107.
    - Lemma 1: UPAR LF66–69.
    - Floor: UPAR LF71–72.
    - Types: UPAR LF73–78.
    - Gap: UPAR3 verdict LF9.
    - Frame existence: UMR LF111–112 and UPAR LF38.
    - m=size: UMR LF252–253.
- **m5: diagnostic attribution** (LF176–180).
  - The table says "excluded by UPAR5-C". C only says no frame induces R4.
  - Excluding the cell needs UPAR4-R + C + frame existence, which is UPAR5-T.
  - **Fix:** "excluded by UPAR5-T (cell ∈ T∖T4)".
- **m6: manifest enumeration** (LF186–197).
  - Sec. 6 omits the physically supplied UPAR3 primary LF69–74 and part-1's UPAR4 cp-03 LF1–25.
  - LF197 refers to an "ordered manifest" that is not present in the supplied text. Only per-block headers are present.
  - As rendered to me, part 1 has 7 file blocks and part 2 has 23 files / 38 range blocks.
  - **Fix:** a numbered erratum giving the exact ordered block list, or a statement that the headers are the manifest.
  - No used premise was found missing.

## 4. Import and unprovided-source boundary

**Imported at declared scope and not re-proved transitively:**
- UMR-F, including windows (Lemmas 2/7/8), parity and empties (Lemma 10), ID (Lemmas 13/14) and frame existence.
- UPAR-R / R_PAR, including LJ: Q chains, unique P exit, θ_u≤−1, at least one −1, and the r-interval.
- UPAR Lemma 1, Lemma 2 and QQ.
- UPAR2-R, including P+ removal by its Lemma 1, and UPAR2 Lemmas 2/3.
- UPAR3-P/Z/R, i.e. T3 and F−e≥2.
- UPAR4-P (T4), and UPAR4-R including UPAR4 §2.

I spot-checked these from the pasted text and found no discrepancy: UPAR Lemma 1/2/QQ, UPAR2 Lemma 2/3, UPAR4 §1 Order/Count/Strong-count, UPAR4 §2, and UPAR4 (G-WW)/(G-SW)→T4. These spot-checks do not upgrade them; they remain imports.

**Unprovided, so not credited as read:**
- UPAR primary outside LF35–107/146–155/216–275.
- UPAR2 primary outside LF95–123/194–224. This includes the Lemma 1 double-cap, Lemmas 4–6 and (Z).
- UPAR3 primary outside LF69–74, i.e. the proofs of UPAR3-P/Z/R.
- UMR primary outside its 12 ranges. This includes the proofs of UMR-F, Lemmas 0–13 and Lemmas 15–20.
- UFC primary outside LF23–27/200–225.
- All disposition and review-freeze JSONs, reviewer outputs and parent written checks.
- recorded-deviations-addendum-v7, and the UMR/UFC scopes and packages.
- UPAR5's own checkpoints, manifest file and receipts, and any parent notification of the second part (scope LF182).

None of these is a premise of a new UPAR5 deduction except through accepted statements whose literal text is present.

## 5. Process carry-forward

- **The UPAR4 pre-freeze PROCESS MAJOR is permanent and uncured** (UPAR4-scope LF56–64; UPAR4 verdict LF13). UPAR5 carries it correctly at LF6–7 and 186–187, and in the ack at LF39–43.
- **Exposure overlaps the §2 route family.** cp-03's unpromoted one-run-charge/q* lead (cp-03 LF16–19) and the Claude O1/O2 leads are in the same family as §2. Both are disclosed (ack LF47–53; proof LF187–189).
  - "Re-derived-after-exposure" is the correct label.
  - There is no independence, preregistration or priority claim.
- **No new process departure is evidenced in the packet.** Second-part notification and checkpoint cadence are not evidenced, so I have not assessed them.

This review covers written mathematical correctness only. It makes no Lean/kernel, human, novelty/priority, runtime, other-terminal-k or full ordered Olson claim, and it is not an acceptance. The parent alone decides.
