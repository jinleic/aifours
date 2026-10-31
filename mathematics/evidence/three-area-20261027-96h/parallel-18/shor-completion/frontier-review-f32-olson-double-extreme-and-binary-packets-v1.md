# f32 — dihedral double-extreme obstruction and exact binary packet class

Reviewer **MathShor-2 / math-5**; author **MathOlson-2-2 / math-2**.
Native `/bin/date` observed before writing: **Wed Oct 28 17:25:45 PDT 2026**.

## 1. Exact verdict, actual sources and review boundary

**NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE: 0 FATAL / 0 MAJOR / 0 MINOR.** The omission hyperplane/count, full-word double-extreme family and interior selector, alternating reflection criterion, exact binary run iff/count, and SAME-actual-word index-two caller are reconstructed below. No unrestricted ordered-Olson proof, original avoiding word, novelty/priority clearance, formal/kernel or human/configured-independent-model review follows.

| Candidate | Complete source and native SHA256 | Decision |
|---|---|---|
| A `frontier-20261028-dihedral-double-extreme-obstruction-v1.md` |104 LF /8804 B; `16d7f27c4d913b6f77267a16a3c7f54672202e170eec898d13db6f9c688b2422` | Exact reflection-only failure count, all-p>=5 two-mode obstruction, p=3 boundary, interior selector and stated proper word class supported |
| B `frontier-20261028-exact-binary-packet-class-v1.md` |135 LF /10367 B; `2e7c1ab87fc0e5027b192140b08e53b668117a491ef8aedd627b433ea053a20e` | Both directions of run classification, exact count including k=1, and conditional original-group selector supported |

The f32 assignment was read FIRST, then both complete candidate files through their endings; native hashes match dispatch. The registered `mathematics/olson-ordered-egz/source/problem.zh.txt` was read: the claim is for every word of length2|G|−1 and exactly |G| DISTINCT increasing original indices. Candidate B invokes O(K) explicitly, not an unordered quotient theorem. My previous f9 review was a same-author nonblind contact; the short-kernel/packet transport and current Dihedral notation have prior familiarity, without a clean-cognition or independent-model claim. No author contact, nested agent, external-model/API call, secret, deletion, push, publication or infrastructure mutation.

## 2. A — omission-exponent linear map and complete count

For ANY odd prime p and ANY ordered N=2p+1 reflections `r^(y_i)s`, let `A_i=(-1)^(i−1)y_i`. Removing occurrence j changes the alternating parity after j, so the original-order product of the remaining2p reflections is `r^E_j` with

    E_j= sum_(i<j) A_i − sum_(i>j) A_i,
    E_(j+1)−E_j=A_j+A_(j+1)=(-1)^(j−1)(y_j−y_(j+1)).

These formulas use actual increasing reflection indices; the omitted reflection's A_j does not contribute. The map `F_p^N -> F_p^N, y->E` has kernel consisting precisely of constant y: all E=0 forces equality of adjacent y by the second identity, and a constant sequence has identity product after every omission. Hence rank N−1.
For each coordinate y_i the coefficient in `sum_j (-1)^(j−1) E_j` vanishes: the alternating prefix before i and suffix after i have the same sum since N is odd. Its image lies in this single nontrivial hyperplane; equal dimension N−1 makes the image the WHOLE hyperplane. Every image point has exactly p preimages, including the zero vector.

All omission products are nonidentity iff every E_j!=0. Set `b_j=(-1)^(j−1)E_j`; this bijects the hyperplane's nonzero-coordinate points with N nonzero field elements summing to zero. If A_N counts such tuples and B_N counts tuples of any one specified nonzero target, scaling makes the latter count independent of the target. Then

    A_N+(p−1)B_N=(p−1)^N,
    A_(N+1)=(p−1)B_N=(p−1)^N−A_N,   A_1=0.

Thus `A_N=((p−1)^N+(p−1)(−1)^N)/p`. Multiplying by p preimages for odd N=2p+1 yields exactly `(p−1)^(2p+1)−(p−1)` actual reflection-exponent words with NO identity omission. It counts only this particular reflection-only mode, not all original full-word avoiding cases.

## 3. A — actual full-word double-extreme family and interior witness

Fix ANY prime p>=5 and ANY a!=0 in F_p. The explicit word is

    s^(2p−1),  r^a s, r^(2a)s,  (r^a)^(2p−3), r^(2a),

where powers in the display are individually labelled occurrences. It has F=2p+1 and R=2p−2, total4p−1. In the reflection block the signed nonzero contributions are −a and +2a. Removing any zero-labelled reflection, or the final `r^(2a)s`, gives exponent −a; removing `r^a s` gives −2a. Both are nonzero for odd p, so no reflection-only 2p selection works.

For the other extreme, ALL rotations occur AFTER the reflections, with total exponent `(2p−1)a=−a`. The ordered two-reflection potential difference is one of `{0,a,2a}` because the actual reflection exponents are ordered `0,...,0,a,2a`. Identity would require this difference to be −a, absent for p>=5. At p=3, −a=2a and this exclusion fails, exactly as stated. No other type/order of word is claimed to be excluded.

The displayed word is NOT an original conjecture counterexample: select the first p+1 copies of s, then p−2 copies of r^a and the last r^(2a). The count is `(p+1)+(p−1)=2p`, indices are increasing, p+1 is even and the rotation exponent is pa=0. This is a real INTERIOR reflection/rotation selector. The phrase “both extremes fail” concerns only this word and these two specified modes, not every possible selector or every group word.

## 4. A — proper reflection-only sufficient class

For any actual reflection subsequence of length2p+1, p−1 consecutive omission increments equal to the same nonzero delta give p successive distinct E-values, exhausting F_p; one actual omission is therefore identity. In particular, if p consecutive reflections have two alternating distinct exponents, their signed increments are all the same nonzero value, regardless of the parity at which the block begins.

If the full original word has at least2p+1 reflections, retain that consecutive-reflection block and any further reflection occurrences outside it until there are2p+1. The block remains consecutive in that selected reflection order; the omission gives 2p actual increasing original positions. Intervening rotations are simply unselected. This is a sufficient word class, not a claim that every word has such a block.

## 5. B — necessity of the exact run classification

Let an arbitrary binary word have N=4k−1=2M+1, M=2k−1, and contain M equal-letter pairs with disjoint chronological spans. The 2M endpoints leave precisely one position unused. Each inclusive span has length>=2 and their total length is at most N, so either all spans have length2 and the unused point is outside every span, or exactly one span has length3 and its interior is the unique unused point. There is no room for a longer span or two longer spans.

- With all adjacent equal pairs, every run except the run containing the unpaired point is covered by pairs and has even length; the exceptional run is odd.
- A length3 equal-end span is either `aaa` or `aba`. In `aaa`, the entire triple lies in one run and its unused middle leaves exactly one odd run. In `aba`, the middle b is an entire singleton run, the outer a's are endpoints from its neighboring runs and each neighboring run is odd; all other runs are even. These are exactly three odd runs consecutive among ALL runs with middle length1.

The argument includes an unused endpoint outside the paired span range, singleton runs, additional even runs and k=1. No assumption is made about kernel labels.

## 6. B — sufficiency and actual original-group caller

If exactly one run is odd, pair consecutive letters within every run and leave one occurrence in the odd run unused. If there are exactly three consecutive odd runs with singleton middle, pair within all other runs, pair all but the last occurrence of the first odd run and all but the first of the third, and join those two remaining equal outer letters across the singleton. The constructed spans are separated, have equal quotient endpoints, leave exactly one point unused, and number M. This proves the run criterion in BOTH directions.

For an actual G-word with index-two normal K, each equal quotient pair has product1 in G/K, so its actual chronological two-letter product lies in K. The M=2k−1 disjoint separated pairs give an actual K-word. Under the EXPRESS hypothesis O(K), select k increasing packet indices with product1. Their union consists of exactly2k original occurrences, in order; because pair spans do not interleave, the original G-product is exactly that K-product. This is a conditional original-word caller, valid also for k=1; it neither assumes every G has such K nor proves a selector for quotient patterns failing the criterion.

## 7. B — exact closed pattern count

For general odd N=2M+1, a binary word is determined by its first bit and ordered positive run lengths.

**One odd run.** If there are e even runs, its placement has e+1 choices. Write its length 2c+1 and the others 2b_i with b_i>=1. The equation is `c+sum b_i=M`, so after removing one from each b_i there are `binom(M,e)` compositions. Including the first bit gives

    2 sum_(e=0..M) (e+1) binom(M,e)=(M+2)2^M.

**Three odd runs.** Their consecutive block has e+1 placements among e even runs, the middle has length1 and the outer lengths are 2c+1,2d+1. The equation `c+d+sum b_i=M−1` gives `binom(M,e+1)` possibilities. Including the first bit gives

    2 sum_(e=0..M−1) (e+1) binom(M,e+1)=M 2^M.

The two cases have different odd-run counts, hence are disjoint. Total `(2M+2)2^M`, with M=2k−1, is `4k*2^(2k−1)`. Dividing by `2^(4k−1)` gives `k/2^(2k−2)`. This is an EXACT count of binary quotient patterns, not a probability of failure, a nonabelian-group-word count or an avoiding-word count.

## 8. Independent exact checks and author-receipt replay

Reviewer-owned `frontier-review-f32-olson-check.py`, SHA256 **915acf2c63a1baee61385806d063027efc0f856bb5440cca2e78d746e0ed6fcf**,167 LF /6375 B, imports NO author source or data. Actual command:

    python3 -B frontier-review-f32-olson-check.py

Observed exact results:

- Independent finite-field row reduction of the omission map had rank N−1 and verified the alternating hyperplane for p=3,5,7,11,13; independent target-sum dynamic programming matched the formula. Exhaustive p=3 enumeration examined2187 reflection words and found126 with no identity omission.
- Direct group multiplication tested the ACTUAL double-extreme family for EVERY nonzero a at p=3,5,7,11,13. All reflection-only counts were zero; all-rotation/two-reflection successes were5 for p=3 and0 for p>=5; every displayed interior selector multiplied to identity.
- A separately implemented disjoint-span dynamic program was compared with the run criterion on ALL8,128,2048,32768 binary words for k=1,2,3,4 respectively. Saturation counts were8,64,384,2048, exactly the closed formula.
- With independent seed2026102804, an actual `C_k x C_2` group lift of EVERY classified pattern was constructed for k=1,2,3: respectively8,64,384 actual words. The checker built separated pairs, selected k actual kernel packet products, and verified the original 2k-index group product. k=4's pattern classification was exhaustive but no group lifts were checked there.

The AUTHORS' read-only checkers were separately replayed on their natively hash-matched saved data; this is receipt replay, NOT the independent checker above. The reflection checker returned `PASS_BOUNDED_OMISSION_RECOUNT`,12187 sequences, input SHA `5ed093a09bec37a41965b70eede8cb3e33c748adfbc82765d3fb464e46066516`. The full-word checker returned `PASS_INDEPENDENT_FULL_WORD_CHECK`, valid interior selectors and the p=3 count5 versus0 for p=5,7,11,13, input SHA `72ac419b2fe750d29d22494354a22cb8f167e09463683b71a97a2a3cb7489eb4`. Author sample counts for p=5/7 are not exhaustive. Neither replay nor reviewer finite checks prove the arbitrary-parameter results by themselves.

## 9. Original residual and final decision

The hyperplane result counts failure only of the reflection-only omit-one construction. The concrete full word defeats two EXTREME selection modes yet has an actual interior identity selector; it is not an avoiding word. The binary theorem is an exact separated-pair certificate under O(K); nonqualifying patterns may still have ordinary ordered selectors. No arbitrary-n/non-index-two theorem, global no-go, original all-finite-group resolution or novelty follows.

**FINAL: NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** Same-harness scientific review with the exact finite checks above; no formal/kernel, configured-family/human or priority acceptance. Historical held outcomes are not accepted premises and prior process records are not retroactively cured.

**END OF COMPLETE f32 SCIENTIFIC REVIEW.**
