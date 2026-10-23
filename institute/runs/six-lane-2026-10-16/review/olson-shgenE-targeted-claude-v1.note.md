## DISPOSITION

- **Lemma SHgen-E (SOURCE00:39-60): ACCEPT.**
  - It has no FATAL and no MAJOR findings.
  - Every proof fact it claims about SHgen checks out against SOURCE01's actual text.
  - This discharges the earlier INCONCLUSIVE (SOURCE02:9, 117-121, 154). It also discharges that grade for downstream users, provided they respect n2 below.
- **ROT-FEW-E v3 overall: ACCEPT-WITH-FIXES.**
  - All findings are MINOR wording, interface or citation issues (n1–n6).
  - No proof step needs to change.
  - The file stays conditional on SHgen and REFL(p), as it already says.

## Checks

**(i) The expansion step (SOURCE01:51-55).**
- L51 says h is "replaced in place by a copies of rho_(sc)". So the copies go into h's own run, which is nonempty.
- L52 says "(a-1)/2 pairs of letters deleted from blocks (every block stays odd and nonempty)".
  - Since each block stays odd, each loses an even number of letters.
  - Blocks are constant, so this is the same word as SOURCE00:47-48's "pairs σ_yσ_y inside blocks". The paraphrase is faithful.
- Runs only gain letters. Blocks only lose letters and keep at least one. Therefore:
  - no block vanishes;
  - no two blocks become newly adjacent, so nothing fuses;
  - nothing is inserted into a block, so nothing splits;
  - no block value changes.
- So every empty run survives, still between the same two blocks of different values. This matches L53: "same k, block values, block parities and runs".
- In SOURCE01:78-121 the only word operation is u°. FLEXa's Q′ is a multiset, not a word.
- One wording nit: SOURCE00:51 says the induction step "applies the same expansion to u°". In fact L119 expands the current word, and the descendants arise through the induction hypothesis. The conclusion is still correct.
- Survival is actually needed for only one expansion, the one at η = 1. The induction could equally run over the whole extended class, since the hypothesis covers u° in either branch of SOURCE00:43.

**(ii) FLEXa (SOURCE01:80-113).** I re-derived the whole lemma.
- (down) and (up) preserve the value sum. Their sizes are m°−2r4 and m°+1−a+2r2, both even because a is odd.
- The failure criteria (D1), (D2), (U1), (U2) are correct, and all four combinations close:

  | Combination | Closed by |
  |---|---|
  | (D1)&(U1) | L1 ≥ a+1 |
  | (D1)&(U2) | k ≥ Φ, then (K) |
  | (D2)&(U1) | L1 = 2p+2κ−k−η and Φ ≥ 0, then (K) |
  | (D2)&(U2) | a odd |

- The only inputs are:
  - κ ≥ 0 (SOURCE01:37; this needs only p in-block pairs);
  - R = 2p+2κ−k;
  - Φ ≤ k;
  - Σθ_i = 0 (L89);
  - GRX for u° (L84) and for w (L93-95).
- The data shared at L85-86 depend only on z, the block values and parities, and the single run holding the copies. Part (i) preserves all of these.
- No step uses nonempty runs. GRX for empty-run representations is imported (SOURCE00:17).

**(iii) The base case η = 1.**
- Lemma Ua really cannot be used here:
  - KB and KBH apply only to RGR words (SOURCE01:18);
  - (V) places its frame inside a nonempty run (SOURCE01:36, 66);
  - the capped-case count at SOURCE01:70-71 counts nonempty runs.
- What the replacement needs from u°(h) all holds:
  - every rotation lies in {ρ_c, ρ_−c}, with c ≠ 0 fixed at SOURCE01:39;
  - its length is 4p−2 (SOURCE01:53-54);
  - its given representation is its maximal constant decomposition (constant blocks, nonempty runs separating them, empty runs only between different values), so o_F(u°(h)) = k exactly, and k ≤ o ≤ (2p+4)/5 ≤ p;
  - in the "Otherwise" branch an empty run exists, and it puts two values into one maximal cyclic reflection run.
- So REFL makes u°(h) solvable. Alternatively REFL-few-odd does, via the interface checked at SOURCE02:82-89.
- FLEXa, which needs only that w avoids and satisfies (K), makes u°(h) an avoider. That is a contradiction.
- The replacement is legitimate. It is even stronger than Ua, which gives only "u° or w solvable".

**(iv) Inheritance by u°.**
- SOURCE01:119-120 gives (H), (K), η−1 heavies and a_max(u°) ≤ a_max. (H) at each level gives H ≥ (a−1)/2, so the expansion exists.
- SOURCE01:53-55 gives the rest:
  - length 4p−2;
  - the same k, all blocks odd;
  - F(u°) ≥ k ≥ 2 and R(u°) = R+a−1 ≥ 1;
  - the same c and the same weights.
- The empty-run clause holds by (i).
- The only Sec. 0 item that needs nonempty runs is (V), and only Ua uses it.
- In the actual use (SOURCE00:67-71), w^ meets every clause:
  - R ≥ η ≥ 1;
  - c ≠ 0 from Step 4;
  - (H) and (K) from Step 5 (SOURCE03:144-146), using (F) 2p ≥ 5k−4, which follows from 5k ≤ 5o ≤ 2p+4.

**The m6 repair (SOURCE00:27-31).**
- The parity rule is right:
  - an odd+odd fusion lowers the odd count by 2;
  - an odd+even or even+even fusion leaves it unchanged;
  - PM* merges keep the count (SOURCE01:25-27).
- There is no cascade. Across empty runs, the fused block's outer neighbours already differed from its value.
- k ≤ o and k ≡ o (mod 2) both hold, and the A|E1|E2 example is correct.
- The diff hunk headers (SOURCE00:129, 144, 157) match the body.
- Only the header, Sec. 0 and the Sec. 1 proof changed. The statement lines L41-42 are context lines.

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR**

- **n1, SOURCE00:28-29.** "It is odd exactly when one of them is odd" can be read as "at least one". That reading is false: two odd blocks fuse into an even block, which is exactly the case where the count drops by 2.
  *Repair:* "odd exactly when exactly one of them is odd".

- **n2, SOURCE00:42, 59-60, 71-72 (REFL interface).**
  - The proof uses REFL only on words of length 4p−2 with all rotations in one nonzero pair, with o_F = k (for u°(h)) or o_F = o (for w).
  - In SHgen-E's generality, (K) at η = 1 allows k ≤ 2p−a−2 ≤ 2p−5, which exceeds p for p ≥ 7. So REFL-few-odd (o_F ≤ p) does not cover the lemma as stated.
  - It does cover every actual call: k ≤ (2p+4)/5 here, and k ≤ (2p+1)/3 in KAPPA01.
  - *Repair:* in SHgen-E, write "assume REFL(p) for words with o_F ≤ k", or add the hypothesis k ≤ p and cite REFL-few-odd. Add the same note to the theorem's last sentence.

- **n3, SOURCE00:44-45.** "whose proof text is that of v2" is literally false. v3 rewords SOURCE01:68, 87 and 95-96 (fix map at SOURCE01:135-139).
  *Repair:* write "whose proof steps are those of v2". Also, L13, L20 and L41 cite SHgen-v2 (8fde88c0) while Sec. 1 cites v3 line numbers (fcbd5a97). Cite v3 throughout, noting that v2 was accepted.

- **n4, SOURCE00:19, 68.** Both cite ROT-few-v3, but v4 (SOURCE03, abd3973c, wording errata only) is current. Also, L19 imports only Sec. 1-5, while L68-70 use Sec. 6 Steps 1-5.
  *Repair:* cite v4, Sec. 1-6.

- **n5, SOURCE00:12.** "v2 itself is unreviewed" contradicts L8 ("Codex round C accepted v2"). Separately, the fix map's "SOURCE02:…" labels (L118, L120) are numbered relative to the earlier review's packet.
  *Repair:* update the status sentence, and cite by file:line instead.

- **n6, SOURCE00:57.** The list of Ua's nonempty-run uses omits the RGR restriction and (V) (SOURCE01:18, 36, 66), and also the count at SOURCE01:70-71. This is harmless, because Ua is replaced whole.
  *Repair:* complete the list.

## Audited versus imported

**Audited here**
- All of SOURCE00, including the v2→v3 diff and its hunk headers.
- SOURCE01:20-121: the expansion, Ua's uses of nonempty runs, every FLEXa case, and Sec. 4.
- SOURCE03 Steps 1-5 (L129-146), at the level of their (F)-inequalities.

**Imported, not re-checked**
- GRX for empty-run representations, PM*, K1, DAV/Davenport-alpha, and EGZ.
- REFL(p) and REFL-few-odd. Their text is not in this packet; the interface follows SOURCE02:82-89.
- ROT-few Sec. 1-5. v3 was accepted, and v4 changes only wording.
