# f4 review: Shor prefix-layer obstruction and 2-adic strengthening

Reviewer **InfoRecursiveMDS18-2**, info-4; author **MathShor-2**, math-5. Native observation before evidence pinning: **Wed Oct 28 17:19:56 PDT 2026**. Same-harness disjoint-owner review, not an independent-model, human, formal/kernel or novelty gate.

**Verdict: SUPPORTED AT THE STATED CONDITIONAL / ALL-ORDER SCOPES, WITH ONE MINOR DEFINITION CLARIFICATION. FATAL0 / MAJOR0 / MINOR1.** The clarification and its complete derivation are in §4. The claims are necessary conditions on a hypothetical SAME finite UD factor-complete extension, the separately stated non-UD obstruction family, and the cyclic-tiling iff. They are not a finite completion or a universal noncompletion proof.

## 1. Assignment, inputs and source familiarity

- Assignment `review-waves/f4-shor-prefix-layer/assignment-v1.json`, SHA256 `5a9c7d3fefac19980c3f87ad9ce46d97812f775fce774f4902dd4441fec170bf`,27LF/3127B, read FIRST.
- **A:** entire `frontier-20261028-prefix-layer-obstruction-v1.md`, SHA256 `ef0d973f52ece5365613a8280475e240992ab53d47bca55dd13ea62f573ab0dc`,177LF/14562B, raw1–177 through ending.
- **B:** entire `frontier-20261028-2adic-prefix-strengthening-v1.md`, SHA256 `d77fd47e36166d51b22ffb6d1ff977e60549116e20068c79f26e8f30ba5b6e44`,77LF/6489B, raw1–77 through ending.
- Registered original-object definition: `mathematics/shor-code-finite-completion/README.md` LF5–14, whole SHA256 `f4d65d104e828681c21955ad1c47526acd18aa1a8858e11d1ef272dba9371bbd`; and the locally retained printed-page image `mathematics/shor-code-finite-completion/source/page-081.png`, SHA256 `6699efc93adb5c0c151f0057d571f194c89e75a59f6090d3cb652de87a3079e0`, directly viewed for the displayed original code/question. These match the candidate's printed 16-word source spelling. No source-current-status or priority conclusion follows from that match.

I previously performed a source-only B5 transcription/comparison-related duty and saw fixed-text math-5 ledger summaries. Parent later imposed a B5 hold; those previous returns/consumers are NOT evidence for this review. The later owner instruction authorizes fresh source inspection prospectively, not retroactive certification of B5 or use of held outcomes as premises. All arguments below are reconstructed directly from the candidate statements and source definition. No author contact, nested agent or external model was used. Prior exposure is disclosed; no blindness or independent-cognition claim.

The candidate labels its finite experiments separately. I did NOT run or import its checkers as evidence. My independently written bounded checks are reported in §9 and are not substitutes for the all-order proofs.

## 2. Literal scope and two-boundary mechanism

The registered problem asks for a finite uniquely decipherable (UD), factor-complete extension of the literal binary code

`S=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2}`.

A binary code D is UD if distinct finite ordered lists of its atoms do not concatenate to the same word; factor-complete means every finite binary word occurs as a contiguous factor of a word in D*. A one-b atom has the form `a^i b a^j`. A and B use the SAME hypothetical finite D throughout; repeated residues do not mean free selection of unrelated D's.

**A LF28–43 reconstructed.** Given an actual pure-a atom a^n, two one-b atoms with the same pair of endpoint residues can be padded at their two outer boundaries with nonnegative powers of that actual atom until their raw words agree. Distinct atoms would then give distinct parses, contradicting UD.

For two actual ordered lists of one-b atoms, equality of the first-prefix, each internal suffix-plus-next-prefix, and the final-suffix residues permits independent nonnegative a^n padding at all those boundaries. Choosing the larger of each pair of congruent a-run lengths yields the SAME raw binary word. Different atom lists give an actual UD violation. The same argument works for any finite number of one-b atoms, not just two.

For length-two lists, a repeated residue key has common first prefix and common second suffix. If the lists differ, their first-tail difference and second-head difference are a common nonzero element of Δrow and Δcol, with orientation chosen consistently; conversely such a common difference creates two different ordered length-two lists with the same key. Unique endpoint pairs prevent a zero-difference hidden duplicate. Thus the difference-set criterion is correct at its stated residue-key scope, not a full UD criterion.

## 3. Unique pure-a atom and the n≥26 necessary bound

**A LF47–73 reconstructed.** Since D is finite, let L be its largest atom length. If no atom were pure-a, every atom would contain b, so an all-a run in a word of D* can meet at most the suffix of one atom and prefix of the next; its length is bounded. Factor-completeness demands arbitrarily long all-a factors, a contradiction. Two DISTINCT pure-a atoms commute; taking sufficiently many copies of each produces two distinct D-atom lists for the same all-a word, contradicting UD. Hence exactly one a^n exists.

The listed positive within-row suffix differences are exactly `D={1,2,4,6,7,12,13,14}`; the positive head differences in suffix column0 are exactly `E={3,5,8,11}`. If n divides d+e for d∈D,e∈E, choose actual source atoms with p−q=d and v−w=e. The two displayed actual lists have first internal a-lengths p+v and q+w+(d+e), respectively, so inserting `(d+e)/n` copies of a^n on the indicated side makes the SAME word. The lists differ in their first one-b atoms. This pays the actual UD caller, not merely a residue inequality.

The explicit four rows of D+E cover4,…,25 except8. For each n in1,…,25 either n occurs in this set, or n is one of the separately covered divisors1,2,3,8 of a listed sum. Thus n≥26 for every hypothetical D. No stronger historical FACT or order-divisibility premise is imported.

## 4. Exactly n one-b atoms: proof and MINOR M1

**A LF75 — M1 (MINOR, missing definition).** The symbol `J_gamma` is used in the claimed ordinary matrix products and sum but is not defined in the candidate body. Its intended seam matrix is recoverable uniquely from the immediately stated internal residue: for suffix residue j and next-prefix residue i, define

`(J_gamma)_(j,i)=1` iff `j+i≡gamma (mod n)`, and0 otherwise.

This is a permutation matrix indexed by suffix/prefix residues and `Σ_gamma J_gamma` is the all-one matrix. Include this definition in any use or erratum. This is an exposition/import precision issue; the corrected proof below establishes the advertised count without assuming the missing definition as an opaque theorem.

Let W be the n×n zero-one endpoint-incidence matrix of the SAME one-b atoms, whose entries are binary by the padding argument. With the explicit J_gamma, `W J_gamma1 W ... J_gamma W` counts actual ordered B-lists with the prescribed internal residue word and prescribed outer residues. Each entry is0 or1: if two different lists contributed, the all-boundaries padding argument in §2 would contradict UD.

There are finitely many such zero-one matrices. Choose one P with maximum K total entries; W itself occurs, so K≥|B|. For every seam gamma, `P J_gamma P` is another actual-list product, so has at most K entries. Summing over gamma gives total K² because the sum of seam matrices is all-one. Thus K²≤nK; since S supplies one-b atoms, K>0 and |B|≤K≤n.

For the opposite inequality, let m≥1 and prescribe arbitrary m−1 internal residues. Choose a word with m displayed b's, inter-b a-runs longer than2L with those residues, and end guards of L a's. Factor-completeness places it inside an actual D* word. No atom of length≤L containing a displayed b can reach outside the guarded factor or contain a second displayed b. Thus each displayed b belongs to its own actual one-b atom, and atoms between successive ones contain no b and are copies of the unique a^n. Each of the n^(m−1) residue words is therefore achieved by an actual length-m B-list. A B-list determines one residue word, so `|B|^m≥n^(m−1)` for ALL m. If |B|<n this inequality fails for sufficiently large m. Hence **|B|=n**. No hypothetical atom with multiple b's is declared absent from D.

## 5. Packing holes and forced outside-prefix atoms

**A LF81–115 reconstructed.** All four original atoms `a^v b` with v∈A are in D and have suffix0. For any actual prefix-residue row i, two unequal pairs `(j,v),(j',v')∈J_i×A` with the same sum would give different length-two atom lists with equal endpoint/internal residues; §2 makes an actual ambiguity. Thus J_i+A is a DIRECT packing and `4|J_i|≤n`.

The four tabulated target/anchor cases at A LF103–105 are valid as integer equalities; they remain valid modulo EVERY n≥26, and the proposed tail differs from its anchor modulo n. Hence row0 misses6 and19, while row11 misses6 and7. The respective target pairs remain distinct at all n≥26. This gives

`|J_0|,|J_11|≤floor((n−2)/4)`, `|J_3|,|J_8|≤floor(n/4)`.

The four original prefixes are distinct at that range. Since exactly n ACTUAL one-b atoms lie in the row partition, subtraction yields at least2 outside A when n is even and at least3 when n is odd. The integer floors have been kept before the even/odd simplification. This pays Theorem A uniformly for every hypothetical finite D, not existence of any such D.

## 6. Three-boundary rectangle and exact 400-pair statement

**A LF119–150 reconstructed.** For a new one-b atom c with head residue i∈Δ and tail residue s∈T, select actual same-row tails p,q with `i≡p−q`, and actual j∈Y0,v,w∈A with `s≡j+v−w`. The two actual three-one-b lists printed in A LF130–131 have the same outside runs and internal lengths congruent at BOTH boundaries. Padding each side independently by actual a^n atoms makes their raw words equal. For n≥26, all negative Δ residues are at least12, while the old prefixes are at most11; its positive residues also miss A. Thus c is not an old atom and the lists are distinct. The result forbids c in ANY UD extension containing S,a^n, regardless of factor-completeness.

For n≥37, the sixteen signed Δ values are distinct modulo n. The stated T has33 integer offsets with range −11 through25, so they are also distinct modulo every n≥37. The eight old suffix values belong to T, leaving25 new suffix residues; hence Δ×(T\J_old) has exactly400 pairs.

The old within-row positive differences D and same-column positive differences E are disjoint as integer sets. Signed equality modulo n≥26 cannot be opposite-sign, since d+e≤25, and cannot be same-sign because D∩E=∅. A new atom whose prefix AND suffix residues are both new changes neither old row-difference nor old column-difference set. Therefore each of the400 additions has unique length-two residue keys while the preceding actual length-three lists violate UD. This conclusion is per addition; it is NOT a claim that these atoms can coexist or that the rectangle exhausts every forbidden atom.

The unpadded literal identity `(ba)(b)(a^3b)=(b)(aba^3)(b)` follows by direct concatenation. It is a valid finite ambiguity against adding `aba^3` to the actual S, not a witness for or solution of the original completion question.

## 7. All-order 2-adic bound and tiling iff

**B LF28–63 reconstructed.** Let d=2^k with k∈{1,2,3} and v2(n)=k. Then n/d is odd. Reducing A={0,3,8,11} modulo d produces two copies each of the residues0 and3 mod d (at d=2 the latter is residue1). For any finite J satisfying the already proved direct packing, each congruence class r mod d receives an EVEN number N_r of distinct elements of J+A, while the entire class has odd size n/d. Thus every class misses at least one element and `4|J|=|J+A|≤n−d`.

Apply that bound to each of the four actual A-prefix rows, use |B|=n and keep the floor:

`N_out≥n−4 floor((n−d)/4)≥d`.

This gives the stated2,4,8 lower bounds for k=1,2,3. It does not force any new atom into the separate forbidden rectangle and makes no claim for another 2-adic class beyond the separately proved general bound.

For the independent cyclic statement, take any n≥12. If A has a direct tiling complement, `n=4|J|`, so 4|n. If 16 did not divide n, its 2-adic valuation would be2 or3, and the bound just proved would contradict full coverage. Conversely, for n=16m, `J={0,2,4,6}+16{0,…,m−1}` works: modulo16, A shifts of {0,2,4,6} cover each even residue once via0,8 and each odd residue once via3,11. Equality of two sums modulo16m first determines the same `(a,y)` modulo16, then the same k modulo m, and the chosen k-range makes k=k'. The construction covers all16m residues uniquely, including m=1. This proves the stated iff for ALL n≥12, not just the experiment range. It does NOT construct an entire one-b layer or complete D.

## 8. Findings and scientific limits

- **M1, MINOR:** A LF75 uses `J_gamma` without defining its entries. Insert the seam definition in §4 above. The proof is fully reconstructable with that clarification.
- **FATAL0 / MAJOR0 / MINOR1.** No mathematical contradiction to A or B was found at their exact stated quantifiers.
- The all-order proofs above, not the bounded computations, support the mathematical disposition. No claim of finite UD completeness, all-order noncompletion, a global counterexample, source novelty or priority is made.
- B's stronger bounds use A's reconstructed |B|=n and SAME-D packing. The modular tiling iff is independently stated for all n≥12 and has its own proof.

## 9. Actual independent bounded checks

I wrote a separate checker from the printed source spelling and the claims, **without importing any author checker**:

`frontier-review-f4-shor-check-v1.py`, SHA256 `139daaa51ea1911d637d06c816760dbe687309a1a65434454de29c659f8cc04e`,189LF/8075B.

Executed command, exit0:

```text
python3 -B frontier-review-f4-shor-check-v1.py frontier-review-f4-shor-check-v1.json 80
```

Actual stdout:

```text
{"elapsed_ms": 381, "exact_cover_status_counts": {"no_by_cardinality": 27, "no_exhausted": 7, "yes": 3}, "explicit_tilings_checked": 4, "max_n": 80, "output": "frontier-review-f4-shor-check-v1.json", "parity_orders_by_v2": {"1": 14, "2": 7, "3": 3}, "rectangle_pair_n_checks": 17600, "row_hole_claims_checked": 220}
```

Result SHA256 `b2fe4ff8ce78538754771aa1ab1e45a149eca56b60e864b595d124e3a2f3dedb`,256LF/4033B. The check rebuilt the original16 atoms, the stated D/E/T sets, all25 small-order divisibility exclusions,220 row-hole cases for n=26..80, and all400 rectangle members at EACH n=37..80 with both two-boundary uniqueness and explicit raw equal-word padding. A separate exact-cover recursion checked the cyclic tiling statement n=12..48 (no search cap hit); four multiples of16 up to80 were also checked against the explicit complement. These are **bounded checks only**, not all-order or formal verification.

## 10. Final review boundary

The two full candidate bodies and their complete all-order load-bearing arguments were reviewed; the only correction is the explicit seam definition. Neither reviewer nor this report contacted the author, assessed any quarantined prior result as a premise, executed an author's checker, proved the original target or established novelty. Parent must assess the exact source, actual return and M1 before any adoption. Current owner direction permits these prospective local checks; historical process/quarantine records remain historical and are not retroactively validated.

**END OF f4 SCIENTIFIC REVIEW.**
