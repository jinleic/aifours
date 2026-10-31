# Shor completion: an extremal-row certificate forces at least three new-head atoms when 16 divides the order

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:05:16 PDT 2026**.
**Computer-assisted ALL-ORDER necessary theorem, with two separately written exact transfer checkers. Not yet peer-reviewed or formalized; no original completion/noncompletion or novelty claim.**

## 1. New actual-completion conclusion

Let D be ANY finite UD factor-complete extension of the literal16-word Shor code. Let a^n be its actual unique pure-a atom, B its SAME one-b layer, and N_out the number of B-atoms with prefix residue outside the original `{0,3,8,11}`.

**Theorem. If 16 divides n, then N_out>=3.** The earlier elementary result gave only N_out>=2 for this case. Together with the earlier 2-adic/odd-order inequalities, every hypothetical completion satisfies

    n odd:                  N_out>=3;
    v_2(n)=1:               N_out>=2;
    v_2(n)=2:               N_out>=4;
    v_2(n)=3:               N_out>=8;
    v_2(n)>=4:              N_out>=3.

These are necessary restrictions for ONE actual D; they do not show its one-b layer exists or exclude any whole family of orders. The new v_2>=4 step uses the flagged finite-state certificate below; other cases are the previous written results.

## 2. The precise extremal-row lemma

Write n=16m with m>=3 and let J be ANY subset of Z_n containing the literal old row0 tails

    Y={0,1,7,13,14}

such that `J×A -> Z_n, (j,a)->j+a` is injective for `A={0,3,8,11}`. The elementary old-word argument already gives `|J|<=n/4−1`.

**Lemma. If |J|=n/4−1, then every optional tail**

    14+16k,  1<=k<=m−2                                   (3)

**lies in J.** The omitted endpoint k=0 is the original mandatory tail14. The later congruent residue n−2 is NOT in(3).

The all-order proof uses a finite exact max-plus certificate, not an inference from a sample. For n=48,64,...,144 it computes the entire cyclic optimization directly; for n>=160 it proves period16 by an exact equality of ALL120 augmented states plus induction (§3). In each case, imposing omission of ANY one of the positions(3) decreases the best possible row size from n/4−1 to n/4−2. No claim is made that all rows or all B-atoms simultaneously attain their separate optima.

## 3. Exact flagged-transfer certificate and infinite continuation

The row condition is equivalent to selecting a binary n-cycle with forbidden cyclic distances3,5,8,11. Row0's original anchors0,1,7 force ALL other positions among0..10 to be0: each has one of these distances from one of the three anchors. Anchors13,14 are then forced at their actual indices. State consists of the last11 bits and one flag `bad`, initially0. The flag changes to1 exactly when a position `14+16k`, k>=1, is passed with bit0. For a linear prefix, store at each `(state,bad)` the maximum number of selected positions among all legal prefixes. The transfer tries bit0 and bit1, vetoes bit1 when any last-bit distance is in `{3,5,8,11}`, obeys the fixed anchors, and takes a max over identical successor states. This is exact by induction on prefix length; no other earlier bit can conflict with the next bit.

Let F_t be this WHOLE score vector after the first t positions. After the fixed anchors, the flag/bit transition depends on position only modulo16. The two separately implemented integer checkers compare all reachable keys and scores and both returned the exact120-state identity

    F_145 = F_129 + 4.                                     (4)

The two times have the same phase modulo16. The max-plus transfer commutes with adding a constant to every finite score. Because its transitions repeat every16 positions, applying any subsequent finite transition sequence to both sides proves

    F_(t+16)=F_t+4  for EVERY t>=129.                       (5)

For a cyclic n=16m, the OPTIONAL positions(3) end at n−18. Process the prefix through that position, i.e. t=n−17, with flagging on; process the final17 positions with flagging OFF. This is essential: the residue n−2 is NOT an optional tail. In the final17 positions, veto a selected bit exactly when it creates a cyclic distance3,5,8 or11 to one of the fixed first11 bits. There are no other wrap interactions: two indices both at least11 apart from the start have wrap distance>=12. The final17-position map depends only on relative offset and n mod16=0, not on n itself.

For n>=160, `n−17>=143>=129`, so(5) implies both the best bad=0 and bad=1 final scores increase by4 on n->n+16. Exact n=160 gives good39 and bad38; hence for ALL n=160,176,... the best bad score is n/4−2, strictly below the extremal row bound. The seven smaller applicable orders n=48,64,80,96,112,128,144 were evaluated directly with the SAME cyclic closure and have the same gap. Thus every maximum row contains all tails(3), proving the lemma at its exact branch. The n=32 case has no optional tail and is handled separately below.

## 4. Apply the lemma to ALL hypothetical completions with 16|n

A finite complete D has |B|=n by the raw actual-path argument in `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 **ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc**. Every head row packs with old suffix-zero heads A and has at most n/4 atoms. Original row0 contains Y; row11 contains {0,1,2}. The explicit two-hole certificates in that predecessor give both rows at most n/4−1 atoms.

If N_out were2, the four original rows together would contain exactly n−2 atoms. Their four independent upper bounds sum to n−2, so EACH upper bound must be attained: rows3 and8 have n/4 atoms, and rows0 and11 have n/4−1 atoms. This is an equality consequence on the SAME actual B, not an assumption that independently optimized rows are jointly realizable.

For n>=48, saturated rows3 and8 are uniquely canonical by `frontier-20261028-unique-saturated-old-row-v1.md`, SHA256 **87921649471a5e734199a5d776831f17611b6b39c4bea9d8542e3698fbe46f5f**. The actual three-word ambiguity/displacement theorem `frontier-20261028-canonical-row-displacement-v1.md`, SHA256 **96a9750e100d25b53835f831375266ab38a17cbeff937454305b7bdbca4a4671**, then requires at least ONE optional tail(3) to be missing, because N_out>0. But row0 is extremal and the lemma proves EVERY optional tail present. Contradiction.

For n=32, the saturated rows are again canonical. Their actual three-word difference obstruction permits no new head at all: the only two possible new residues are blocked by the original row0 tails1 and14 (the optional set is empty). This contradicts N_out=2 without using the flagged optimization. Therefore N_out>=3 for every n divisible by16. No claim is made that3 is achievable in a genuine complete code.

## 5. Actual checks, source pins and assurance boundary

Executed after the new sources were complete:

1. `python3 -B frontier-20261028-extremal-anchor-check.py`: an age-TUPLE implementation computed the full120-state F_129/F_145 equality and exact cyclic good/bad maxima for n=48..176 in steps16.
2. `python3 -B frontier-20261028-extremal-anchor-bitmask-check.py`: a separately written BITMASK implementation enumerated the initial masks, recomputed the same whole-vector identity and cyclic maxima for n=48..192. It rejected deliberate score and state-removal mutations for their intended distinct reasons.

Both observed good/bad values `(11,10),(15,14),(19,18),(23,22),(27,26),(31,30),(35,34),(39,38)` at n=48..160, matching `(n/4−1,n/4−2)`. They implement the SAME elementary transfer invariant, not independent-model/cross-vendor or formal verification; §3 explains why the finite checked period extends to all n.

| File | Native SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-extremal-anchor-check.py` | 566c098073b7462f877fbbef6f62c0e47c5e2cfa21f436cf8c9481ed42aad7a4 |74 /2647 |
| `frontier-20261028-extremal-anchor-bitmask-check.py` | 901faac772334d9c097606637b549f64b357535ad5b418670e22202e16f44f58 |77 /2550 |

Pin observation: Wed Oct28 18:05:16 PDT. Mathematical review, independent period-certificate replay and priority/novelty remain outstanding. No historical held outcome is accepted merely through the updated owner direction.

## 6. Remaining original gap

A hypothetical complete D may have three or more new-head atoms, or may lie outside the 16|n branch. Nothing here constructs its one-b layer, proves all-list UD, handles every multi-b atom, proves factor-completeness, or derives a global contradiction. The full Shor completion question remains unresolved.

**END OF COMPUTER-ASSISTED EXTREMAL-ROW NECESSITY.**
