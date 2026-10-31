# Written review v1 — f114-shor-1320-two-border-sizes

Review kind: INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (same harness; not human, not independent-model-family, not formal/kernel, not novelty clearance).
Native `/bin/date` observed before writing: **Wed Oct 28 19:53:13 PDT 2026** (2026-10-29T02:53:13Z).
Manifest: `manifest-v1.json`, SHA256 `ad3f0ad3e4a7d80afa037fe238e791f267d993ba0c0cbf8945abe72224c30eaf`, 5366 bytes (verified by `shasum -a 256`).
Authority named by the manifest: `contract-addendum-2-frontier-first-owner-direction-v1.json` (frontier-first direction; historical held outcomes are not premises here and no old review is changed).

## 0. Verdict

**No FATAL, no MAJOR defect. MINOR: 3. Observations (non-defects): 3.**

The reviewed claim — *conditional on the existence of a finite UD factor-complete extension D of the literal Shor code whose unique pure-a atom is a^1320, the same-code direct border factorization satisfies (|P|,|Q|) ∈ {(24,55),(44,30)}* — is **correctly derived** from its stated hypotheses. Every general step was reconstructed independently in §2 below, and every finite list, count and certificate the chain relies on was recomputed by reviewer-written code (§4), so none of the finite-list inputs needs to remain conditional. This review does **not** assert that either surviving pair is feasible, does **not** exclude order 1320, and does **not** construct or exclude a completion.

## 1. Source coverage receipt

All twelve manifest inputs were read completely in declared order after verifying full SHA-256, byte and LF counts (`shasum -a 256`, `wc -c`, `wc -l`); every one matched the manifest exactly:

| # | role | SHA256 (full) | bytes | LF | match |
|---|---|---|---|---|---|
| 1 | literal code (math-5 definitions) | 12db546b559de7db391bdc3755b02e391296852b3d188532d8a90dc483686bc9 | 2633 | 40 | yes |
| 2 | six-head border factorization | 56fd2cff931af2da61e2f8a17c513d8af5c3cc8064c9d9ed66c5c361fb3a6051 | 9229 | 114 | yes |
| 3 | divisor-class obstruction | 228757d547c671685c9e2c1b58332b6e8615b15dc9f7db9b49814591dd072b23 | 5532 | 62 | yes |
| 4 | packing witness JSON | eb73d65b4e9d2f79b917e4da2d390cd157388341bb75e5c5049a914cf6ef39cb | 2081 | 1 | yes |
| 5 | packing author checker | 937a789eba003c735dd6e0b72dc7c6967058d9b4417a48d9d9b8a9689567dfc6 | 2027 | 36 | yes |
| 6 | four-border deduction | 3d93c233bc6ea6802a797564edf0c18e21de2215dbf85c70136bad4556399c3e | 6566 | 85 | yes |
| 7 | three-border deduction | 9f2835c4f7e55eb909b342ed96d95f9c543ce7e169d9d0e865a19fc641a9d461 | 4263 | 46 | yes |
| 8 | two-border candidate | 0e2474a0de932d626eac2322fbfe7a627121638f2beac972c45e01938efae946 | 5512 | 54 | yes |
| 9 | author prime-residue control | fd5bb126e37396ec73681954c9e67205ed8c1ffaa4b8e62d8cf454612181068d | 1753 | 32 | yes |
| 10 | author Hall control | 715b325871c8148c1d62647e4925fca1edc23a4a9e71840bd41a6250b59404b6 | 1522 | 33 | yes |
| 11 | author forced-gcd control | 7dcf4ce407c2e13178db3e774d7c4518aca6364687f208011aba49c6ef79a6a3 | 2931 | 53 | yes |
| 12 | author alternative forced-gcd control | f9f237d6c1da97124992aba49fd05b73774f0140fc4e7ebc19bb9ad2dc19d640 | 2030 | 36 | yes |

Author scripts (5, 9–12) were read only; none was executed or imported. The certificate JSON (4) was consumed as data by reviewer code and re-verified from scratch.

Primary sources read directly (no web_search): `https://arxiv.org/html/2411.03854v3` (Kiss–Londner–Matolcsi–Somlai; Theorem 2.1 states Sands' criterion: A⊕B=Z_M iff |A||B|=M and Div*(A)∩Div*(B)={0}; the chain uses only the necessary direction) and `https://arxiv.org/html/2301.13566v1` (Cordero; Theorem 1.1 restates Restivo–Salemi–Sportelli: for a finite maximal code M with b, a^n ∈ M, `({k : a^k b^+ ∈ M}, {k : b^+ a^k ∈ M})` is a factorization of size n; it also cites BPR Prop. 2.5.15 for the unique order of a letter). Both match how the chain uses them.

Not in the manifest and therefore not reviewed: the "graded tradeoff" packets behind the N_out/N_Y remarks, the six-head search programs, and the packing generator.

## 2. Reconstructed proof (reviewer's own derivation)

### 2.0 Hypotheses and immediate consequences
(H1) D is a finite set of words over {a,b}, D is uniquely decipherable (UD), D is complete in the book's sense (every word is a factor of some word of D*), and C ⊆ D where C is the literal 16-word Shor code
`C = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2}`.
(H2) The unique pure-a atom of D is a^n with n = 1320.

Derived (classical, reconstructed): (i) b ∈ D (b ∈ C), hence by UD no b^k with k ≥ 2 is an atom and every b-run factors as b·b·…·b. (ii) A pure-a atom exists: with L = max atom length, a^(2L+1) is a factor of some D*-word; the atom covering the middle letter of that run lies entirely inside the run, so it is a^m for some m. (iii) It is unique: a^m, a^(m') ∈ D with m ≠ m' gives (a^m)^(m') = (a^(m'))^m, two factorizations. So "unique pure-a word a^n" is a theorem under (H1), not an extra assumption; (H2) fixes its exponent.

### 2.1 Border sets and genuine anchors
Define P = {i mod n : a^i b^k ∈ D, k ≥ 1}, Q = {j mod n : b^l a^j ∈ D, l ≥ 1}. From the literal words: b ⇒ 0 ∈ P∩Q; a^3b, a^8b, a^11b ⇒ A = {0,3,8,11} ⊆ P; ba, ba^7, ba^13, ba^14 ⇒ Y = {0,1,7,13,14} ⊆ Q. The other eight words (a^3ba^2, a^3ba^4, a^3ba^6, a^8ba^2, a^8ba^4, a^8ba^6, a^11ba, a^11ba^2) have a's on both sides and contribute to neither set. The anchors are therefore literal same-code atoms (verified by regex extraction from the 16 words generated from the book formula; the 16 words pass a Sardinas–Patterson test).

### 2.2 Directness of P + Q
Let u_t = a^(i_t) b^(k_t) ∈ D, v_t = b^(l_t) a^(j_t) ∈ D (t = 1,2) with i_1+j_1 ≡ i_2+j_2 (mod n). Pick L ≥ l_1,l_2, K ≥ k_1,k_2, and G > 0 with G ≥ i_t+j_t and G ≡ i_t+j_t (mod n). Then for each t,
`b^(L−l_t) · v_t · (a^n)^((G−i_t−j_t)/n) · u_t · b^(K−k_t) = b^L a^G b^K`
is a D-factorization. By UD the two atom sequences coincide. Count the initial run of b-atoms: if v_t = b (forced when j_t = 0, by (i)), that run has length exactly L (the next atom is a^n or u_t with i_t > 0, because G > 0 excludes v_t = u_t = b with no a^n); if v_t ≠ b, it has length L − l_t < L and is followed by v_t. Equal sequences hence force the same case and l_1 = l_2, so v_1 = v_2 and j_1 = j_2. Symmetrically from the right, u_1 = u_2 and i_1 = i_2. So every residue has at most one representation p+q, and in fact every residue of P (resp. Q) is realized by exactly one head (resp. tail) atom of D.

### 2.3 Coverage of P + Q
For any residue γ pick g > L with g ≡ γ (mod n) and embed b^L a^g b^L in some D*-word. The atom containing the last b of the left guard has length ≤ L, so it starts inside the guard and cannot reach the right guard across the a^g gap; hence it is b^l a^j (j ≥ 0; j = 0 forces it to be b). Symmetrically the atom containing the first b of the right guard is a^i b^k. Every atom strictly between lies inside the a-run, hence equals a^n. So g = j + mn + i and γ ∈ Q + P. With 2.2: P ⊕ Q = Z_n and |P||Q| = n.

### 2.4 Anchor consequences valid for all feasible n
Directness of A + Y alone forces n ≥ 26: the twenty integer sums a+y are distinct and lie in [0,25]; for n ≤ 19 pigeonhole, and for n = 20,…,25 the pairs (1,21),(0,21),(0,22),(1,24),(0,24),(0,25) collide (verified for all n ≤ 2640: first feasible n is 26 and none above fails). For every n ≥ 26: residue 6 ∉ A + Y, and each q ∈ 6 − A = {6,3,−2,−5} collides (3+6=8+1, 0+3=3+0, 3−2=0+1, 8−5=3+0), so P ≠ A, |P| ≥ 5; residue 2 ∉ A + Y, and each p ∈ 2 − Y = {2,1,−5,−11,−12} collides (2+1=3+0, 1+0=0+1, −5+13=8+0, −11+14=3+0, −12+13=0+1), so Q ≠ Y, |Q| ≥ 6. The pair-distinctness needs only n ∤ 1,3,5,12,13,14, true for n ≥ 26 (also machine-checked for every n in [26, 2640]).

### 2.5 Prime balance
P(x)Q(x) ≡ 1+x+…+x^(n−1) (mod x^n−1). For a prime p | n and ζ a primitive p-th root of unity, P(ζ)Q(ζ) = 0. If p ∤ |Q| then Q(ζ) ≠ 0 (else Φ_p | Q in Z[x] by monic division, and Q(1) = |Q| would be divisible by Φ_p(1) = p), so Φ_p | P, i.e. P ≡ R(1)·(1+x+…+x^(p−1)) mod (x^p − 1): P is uniform modulo p. If v_p(n) = 1, exactly one of |P|,|Q| is divisible by p and that side is uniform mod p. The anchor multiplicities quoted in input 2 §4 (A mod 5 has class 3 twice ⇒ |P| ≥ 10; A mod 11 has class 0 twice ⇒ |P| ≥ 22; Y mod 3 has class 1 thrice ⇒ |Q| ≥ 9; Y mod 7 has class 0 thrice ⇒ |Q| ≥ 21; Y mod 13 has a doubled class ⇒ |Q| ≥ 26) were recomputed and are correct.

### 2.6 Sands' necessary direction
Let P ⊕ Q = Z_n, d = p−p' ≠ 0, e = q−q' ≠ 0 with gcd(d,n) = gcd(e,n) = g. Write d = g d', e = g e' with d', e' units mod n/g; take u ≡ e'/d' (mod n/g) and, by CRT, u ≢ 0 modulo each prime of n not dividing n/g; then u is a unit mod n and ud ≡ e. For every nontrivial n-th root ζ of order m, P(ζ) = 0 ⇔ Φ_m | P ⇔ P(ζ^u) = 0 (ζ^u is another primitive m-th root; Φ_m irreducible), so (uP)(ζ)Q(ζ) = P(ζ^u)Q(ζ) = 0 whenever P(ζ)Q(ζ) = 0; with |uP||Q| = n this gives uP ⊕ Q = Z_n. But up + q' = up' + q with (up,q') ≠ (up',q) — contradiction. Hence no nonzero P-difference and Q-difference share a gcd class with n. (Brute-force sanity: all 2,412 normalized tilings of Z_n for n ≤ 18 obey this.)

### 2.7 Order 1320: divisor-class screen
1320 = 2^3·3·5·11. G_A = {gcd(a−a',1320)} = {3,5,8,11}; G_Y = {1,2,6,12}; disjoint, as 2.6 requires. By 2.6 every P-residue x must satisfy gcd(x−a,1320) ∉ G_Y for all a ∈ A (x ≠ a) and pairwise within P; dually for Q against G_A. The individually admissible sets are C_P (|C_P| = 112, A ⊆ C_P) and C_Q (|C_Q| = 286, Y ⊆ C_Q). The certificate (input 4, hash verified) contains 16 pairwise-disjoint triangles inside C_P whose three pairs all have gcd-difference in G_Y ⇒ |P| ≤ 112 − 2·16 = 80; and a partition of all 286 C_Q residues into 130 cliques with every within-clique pair in G_A ⇒ |Q| ≤ 130. (The 80-element witness containing A is G_Y-independent, so 80 is sharp for the one-sided screen; it is not a tiling.) Divisors d of 1320 with d ≤ 80 and 1320/d ≤ 130 are exactly {11,12,15,20,22,24,30,33,40,44,55,60,66}. |P| = 11 is impossible: 11 | |P|, 11 ∤ 120, so P is uniform mod 11 with one element per class, but 0,11 ∈ A share class 0. Twelve sizes remain.

### 2.8 Twelve → four
C_P ∩ (1 mod 3) = {88,253,256,415,418,583,748,913,916,1075,1078,1243} (12 residues; A has none in this class). The pairs (88,916),(256,748),(253,415),(583,1075) are disjoint with gcd-differences 12,12,6,12 ∈ G_Y, so at most 8 of the 12 can lie in P (reviewer's exact maximum: 8). If 3 | |P| then P is uniform mod 3 (3 ∤ |Q|), needing |P|/3 in this class: sizes 30,33,60,66 need 10,11,20,22 — excluded. C_P ∩ (2 mod 5) = {132,407,792,872,987,1067} (6 residues; A has none): if 5 | |P| then P needs |P|/5 there: sizes 40,55 need 8,11 — excluded.
|P| = 15: P uniform mod 3 (5 per class) and mod 5 (3 per class). A already has 3,8 ≡ 3 (mod 5), so at most one new head is ≡ 3 (mod 5). Exactly four of the twelve 1-mod-3 candidates are ≢ 3 (mod 5): {256,415,916,1075}; all four must be chosen plus one of the other eight, but 88–916 (12), 253–415 (6), 418–256 (6), 583–1075 (12), 748–256 (12), 913–415 (6), 1078–256 (6), 1243–415 (12) are all G_Y conflicts. Exhaustively, none of the C(12,5) = 792 five-subsets with ≤ 1 element ≡ 3 (mod 5) is G_Y-independent. Excluded.
|P| = 22, |Q| = 60: Q uniform mod 3 (20 per class) and mod 5 (12 per class). No C_Q residue is ≡ 4 (mod 6): for q ≡ 4 (mod 6) the three numbers q−1, q−7, q−13 are odd multiples of 3 differing by 6 and 12, so at most one is divisible by 5 and at most one by 11, leaving one with gcd exactly 3 ∈ G_A (also machine-checked: C_Q mod 6 has classes 0,1,2,3,5 only). Fix r ∈ {1,2,3}. Among C_Q ∩ (r mod 5) exactly 10 residues are ≢ 1 (mod 3), exactly 4 of them odd; four disjoint gcd-5 pairs sit inside the 10 (exact maximum G_A-independent subset: 6). So Q ∩ (r mod 5) has ≥ 6 elements ≡ 1 (mod 3), all odd; at most 4 can share one mod-11 residue (one class mod 330 has 4 representatives), so two of them, o_1 ≢ o_2 (mod 11), exist. Any even Q-element e ≡ r (mod 5), e ≢ 1 (mod 3) has e−o_i odd, ≡ 0 (mod 5), ≢ 0 (mod 3), and ≢ 0 (mod 11) for at least one i, i.e. gcd(e−o_i,1320) = 5 ∈ G_A — forbidden (machine-checked over all such triples). Hence the non-1 part of Q ∩ (r mod 5) lies among the 4 odd candidates, so ≥ 8 elements per class are ≡ 1 (mod 3): ≥ 24 in total, contradicting 20. Excluded.
Remaining: |P| ∈ {12,20,24,44}.

### 2.9 Four → three (Hall)
|P| = 12, |Q| = 110: Q uniform mod 11 (10 per class). Class 0 contains 0 ∈ Y, class 3 contains 14 ∈ Y. L = C_Q ∩ (0 mod 11) \ {0} and R = C_Q ∩ (3 mod 11) \ {14} both have 25 residues; Q must take 9 from each. Since x−y ≡ −3 (mod 11) for x ∈ L, y ∈ R, a conflict means gcd(x−y,1320) ∈ {3,5,8}. Every one of the C(25,9) = 2,042,975 nine-subsets of L has ≥ 18 R-neighbours (minimum 18 attained by exactly 11 subsets), leaving ≤ 7 < 9; independently every one of the C(25,8) = 1,081,575 eight-subsets of R has ≥ 17 L-neighbours (minimum 17, attained 10 times), leaving ≤ 8 < 9. Excluded.

### 2.10 Three → two (gcd class 264 on both sides)
|P| = 20, |Q| = 66. P side: 5 | 20, 5 ∤ 66 ⇒ P uniform mod 5 with 4 per class; A mod 5 = {0,3,3,1} has nothing in classes 2 and 4, so P takes 4 of C_P ∩ (2 mod 5) = {132,407,792,872,987,1067} and 4 of C_P ∩ (4 mod 5) = {264,344,459,539,924,1199}. The perfect matching (132,924),(407,1199),(792,264),(872,344),(987,459),(1067,539) has all differences of gcd 264 (792 = 3·264, 528 = 2·264); 8 endpoints from 6 disjoint pairs select ≥ 2 complete pairs (brute force over all 225 choices: minimum 2). So Div(P) ∋ 264.
Q side, assuming Div(Q) ∌ 264: 11 | 66 ⇒ Q uniform mod 11 (6 per class); 3 | 66 ⇒ 22 elements ≡ 1 (mod 3), all odd (no 4 mod 6). Two 1-mod-3 elements with equal (mod 11, mod 8) differ by a nonzero multiple of 264 = lcm(3,8,11), whose gcd with 1320 is exactly 264 — forbidden; so each of the 44 odd slots has capacity 1 and each mod-11 class holds ≤ 4 ones, hence ≥ 2 non-ones. Classes 1, 2, 7 each contain exactly 10 non-one C_Q residues (the minimum over classes; others have 16 or 22). Any admissible Q therefore contains a seed of two non-ones from each of these classes. Relaxed necessary tests, all errors on the permissive side: (1) discard seeds with a pairwise or anchor gcd-difference in {3,5,8,11,264} — 1,143 of 91,125 survive; (2) count slots containing at least one candidate compatible with the seed — 1,089 seeds open < 22 slots; (3) for the remaining 54, in some class j ∈ {1,2,7} the 2 seed members plus all open slots plus all remaining seed/anchor-compatible non-ones total < 6 — 0 residual. So Div(Q) ∋ 264 too, contradicting 2.6. Excluded.

### 2.11 Conclusion
Under (H1)–(H2): (|P|,|Q|) ∈ {(24,55),(44,30)}. Nothing above shows that either pair admits a direct tiling with the anchors, let alone a full one-b layer, multi-b compatibility, UD or completeness; and failure at 1320 would not be shown by these packets. The deduction does not use the six-head border search (input 2 §5–6, INCOMPLETE at n = 1320): |P| = 6 is excluded at 1320 by |P| ≥ 12 from 2.7 alone.

## 3. Exact assumptions, dependencies and limits

Load-bearing hypotheses: (H1) finiteness, UD, factor-completeness, C ⊆ D; (H2) pure-a order exactly 1320. Load-bearing imports (all reconstructed in §2): existence/uniqueness of the pure-a atom; the RSS border factorization; Φ_p irreducibility and monic division in Z[x]; Sands' necessary direction; CRT. Load-bearing finite facts (all recomputed in §4, so not merely conditional): G_A, G_Y; |C_P| = 112, |C_Q| = 286; the 16-triangle and 130-clique certificate; the 12-, 6-, 6-element class lists; the P15 blocking table; absence of 4 mod 6 in C_Q; the three (10, 4, four-pairs) class facts for Q22; |L| = |R| = 25 and both Hall minima; the six 264-matched pairs; the 10/10/10 non-one lists, 44 slots, and the 91,125/1,143/1,089/54/0 seed counts.

What this review does not cover: feasibility of (24,55) or (44,30); any exclusion of order 1320; any completion construction; the N_out/N_Y "graded tradeoff" statements (divisor note §4, four-border §5, three-border §3 end, two-border §4 end), whose premises live in packets outside the manifest; the six-head search programs; novelty or world-status.

Informational only (not an exclusion attempt): for (24,55), 3 | 24 forces exactly 8 P-elements ≡ 1 (mod 3), and 8 is the exact maximum G_Y-independent size of that 12-element class, so any such P must realize a maximum independent set there; for (44,30), 11 | 44 forces 4 P-elements per mod-11 class while C_P has 40/6/6/12/6/6/6/6/12/6/6 candidates in classes 0..10.

## 4. Independent finite control and receipt

Reviewer artifact `written-control-1320-chain-v1.py` (SHA256 `159eea4a4f58d9328047dcfbb40c5c1ac8c10f0ea97d95be7788da1fead7ca9b`, 23510 bytes, 505 LF), written from scratch; it imports nothing from author scripts and reads only the certificate JSON (hash re-verified in-run). One observed run, bracketed by native `/bin/date`:

    Wed Oct 28 19:50:10 PDT 2026
    python3 -B written-control-1320-chain-v1.py
    {"all_pass": true, "failures": [], "checks": 49, "elapsed_seconds": 3.826}
    Wed Oct 28 19:50:14 PDT 2026

Receipt `written-control-1320-chain-output-v1.json` (SHA256 `b00f7c4b2e0ac5f60eadc68061ddf595494708fe1d3eb833c9087543dc41ced5`, 11584 bytes, 682 LF; Python 3.14.3; in-file clock 19:50:11 → 19:50:14 −0700). Key observed values: 16 words, Sardinas–Patterson UD true; anchors (0,3,8,11)/(0,1,7,13,14); first feasible n = 26 and no failing n in [26,2640] for either anchor-exclusion; 2,412 small tilings, 0 Sands violations; G_A/G_Y as stated; 112/286; triangles/cliques/witness valid, bounds 80/130; 13 divisors → 12 sizes; 1-mod-3 list exact, maximum independent 8; 2-mod-5 and 4-mod-5 lists exact; P15: blocking table valid and all 792 five-subsets rejected; C_Q mod-6 classes {0,1,2,3,5}; for r = 1,2,3: 10 non-ones, 4 odd, exact independent maximum 6, every even non-one conflicts with one of any two mod-11-distinct odd ones; |L| = |R| = 25; forward 2,042,975 subsets, min 18 (×11); reverse 1,081,575 subsets, min 17 (×10); matching gcds all 264, minimum 2 matched pairs; 44 odd slots (8 singletons, 36 triples), same-slot gcd always 264; non-one counts per mod-11 class 22/10/10/22/16/16/16/10/16/16/16; seeds 91,125 / 1,143 / 1,089 / 54 / 0; survivors {24,44}. Reviewer greedy clique covers gave 80 (P) and 132 (Q) — the author's 130 Q-cover is tighter and was verified pair by pair.

Reviewer's own cross-checks of its tools: the Sardinas–Patterson routine returns False on `{aabb,abaaa,b,ba}` and `{a,aa}`, True on `{aaa,ab,aab,bba,ba}` and on Restivo's `{a^5,ab,b,baa}` (one throwaway command, not an artifact).

## 5. Defects

FATAL: 0. MAJOR: 0. MINOR: 3.

- **MINOR-1 (divisor note §1).** "reduces the preceding 17 border-cardinality possibilities to 12" is not reproducible from the manifest inputs. From the explicitly written premises (|P| ≥ 5, |Q| ≥ 6, prime balance with anchor multiplicities) the reviewer recount is 20 sizes {6,8,10,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132,165}; whatever earlier packet produced 17 is not named. Not load-bearing: the 12-list follows directly from 80/130 plus the |P| = 11 balance argument, both verified.
- **MINOR-2 (border note §3).** "valid modulo every feasible n ≥ 26" is asserted without deriving 26. The derivation (directness of A + Y fails for every n ≤ 25 and holds for all n ≥ 26) is one line and was verified; the anchor-exclusion identities hold for every n ≥ 26 since the only distinctness conditions are n ∤ 1,3,5,12,13,14.
- **MINOR-3 (all packets).** Existence and uniqueness of the pure-a atom a^n under (H1) are used ("its unique actual pure-a atom") but never argued in the inputs; it is classical (BPR Prop. 2.5.15 per Cordero) and reconstructed in §2.0. A one-line statement of the import would close the gap.

Observations (not defects): (O1) the n = 1320 six-head scan in input 2 §6 is INCOMPLETE but is not a dependency of the two-border claim (|P| ≥ 12 supersedes |P| = 6); the chain would read more clearly if this non-dependence were stated. (O2) The N_out/N_Y multi-b remarks appended to inputs 3, 6, 7, 8 cite "graded tradeoffs" outside the manifest; they are unverified here and should not be read as covered by this review. (O3) In the relaxed seed test the anchor-compatibility filter under {3,5,8,11,264} is vacuous for the 30 pool residues (none conflicts with Y), so test (1) is effectively pairwise only; this changes nothing because the test is a necessary condition either way.

## 6. Scope statement

Same-harness independent review by a model instance distinct from the author lane; not a human review, not an independent-model-family review, not a formal/kernel verification, not a novelty or world-status search. The classical border theorem (RSS89) and Sands' theorem are prior results credited by the packets; this review confirms their statements from the two primary pages read and their usage, and asserts no priority. The original finite-completion problem for Shor's code remains OPEN; this review neither excludes order 1320 nor constructs any completion.

**END OF WRITTEN REVIEW v1.**
