# f175 review v1: odd-prime T1 symbol asymmetry, orbit freeness and normalized counts

- Reviewer: `ReviewF175TuscanOrbit` (same-harness task subagent).
- Wave: `f175-tuscan-odd-prime-orbit-asymmetry`. Manifest `manifest-v1.json`, SHA-256 `a8dec6fcd51e1580cfb7cc69eabf0cab9700762c0955eaa698a0f14ecf500ce0` (2,797 B, 30 LF). Candidate author `InfoRecursiveMDS18-2`.
- Native `/bin/date` observed immediately before writing this file: **2026-10-29T08:09:43-0700 PDT**.
- Assurance class: a same-harness written reconstruction plus bounded, reviewer-authored finite diagnostics. This is **not** human acceptance, independent-model-family acceptance, formal/kernel acceptance, or novelty/priority acceptance. It is not parent adoption either.

## 0. Verdict at the frozen scope

Both candidate statements are **correct as stated for every odd prime p** under exact linear directed-adjacency definitions. Section 3 reconstructs every load-bearing step independently.

| Severity | Count | Items |
|---|---|---|
| FATAL | 0 | none |
| MAJOR | 0 | none |
| MINOR | 1 | MINOR-1: T2(p) is never defined explicitly in either input (validity unaffected) |
| INCONCLUSIVE (in scope) | 0 | none |
| Not adjudicated (outside frozen scope) | 3 groups | In1 LF17 literature/source boundary; In1 LF19 p=11 nonvacuity files; In2 LF14 SAT model and run status (section 4) |

**Empty set versus existence.** Every divisibility statement is a cardinality identity for a finite set that may be empty. The complete controls in section 6 find T1(3) = T1(5) = ∅, so at p = 3 and p = 5 the statements hold only with the value 0. At p = 7 a bounded sample exhibits actual T1(7) arrays. Nothing in this review asserts or excludes the existence of any T2(p), and in particular of T2(11).

## 1. Source order, integrity and process record

1. At 2026-10-29T14:26:33Z (`/bin/date -u`) the manifest's SHA-256, byte count and LF count were verified against the task pin. The manifest was then read completely (30 LF).
2. At 2026-10-29T14:27:55Z both inputs were verified against the manifest:
   - input 1, `frontier-20261028-odd-prime-symbol-asymmetry-v1.md`: SHA-256 `afb2640251506ec1f9dc02a2411e227a7e0740423cdcf36cc7b3ea0c5c28bf3f`, 4,283 B, 19 LF;
   - input 2, `frontier-20261028-odd-prime-orbit-divisibility-v1.md`: SHA-256 `e1b7d77bf78c752911666da1013db005a57a5cb829438fe28d083fab2ccd1e82`, 3,110 B, 14 LF.

   Each was then read completely in the declared order (input 1 LF 1–19, then input 2 LF 1–14) before any mathematical interpretation.
3. A parent capacity pause was acknowledged at 2026-10-29T14:44:18Z. No file had been created at that point; the return was status-only.
4. On resume, the parent record `parent-capacity-resume-v1.json` (SHA-256 `5cb68de2162bd4f600d071092f907eb73e550d174b4b3ce3469a94d464ca9a8b`, 1,450 B, 15 LF) was read as process metadata, not as a scientific input. At 2026-10-29T07:57:05-0700 PDT the manifest and both inputs were re-hashed as a drift check; all three were unchanged.
5. No other source was opened. That excludes every file cited inside the inputs: the Tuscan-k PDF, the Ollis paper, `frontier-20261028-three-row-fast-run-01*.json`, `frontier-20261028-tuscan-sat-canonical-v1.py` and its run JSON. It also excludes author code, web search, external models/APIs, Git and held/ZERO material. Parent STATUS-ONLY safety notices about f161/f162 were received; none of the affected material was accessed.
6. Controls: one reviewer-authored standard-library script. It was syntax-checked with `ast.parse` only (no control logic executed), then executed exactly once (run-01) through a reviewer-authored runner with exclusive outputs (section 6).

## 2. Exact definitions used

The alphabet is Σ = {0,…,p−1}, with p ≥ 2. A *row* is a permutation x = (x_0,…,x_{p−1}) of Σ, written left to right. An *ordered array* is a sequence A = (A_0,…,A_{p−1}) of rows, and its *row set* is R(A) = {A_0,…,A_{p−1}}.

- **D1 events** are the pairs (A_r[j], A_r[j+1]) for 0 ≤ j ≤ p−2. The reading is linear, with no wrap-around. A ∈ T1(p) iff the p(p−1) D1 events are pairwise distinct.
- **D2 events** are the pairs (A_r[j], A_r[j+2]) for 0 ≤ j ≤ p−3. A ∈ T2(p) iff A ∈ T1(p) and the p(p−2) D2 events are pairwise distinct. This is the standard linear Tuscan-2 reading; see MINOR-1.
- **Symbol action.** g ∈ Sym(Σ) acts entrywise on rows: g(x) = (g(x_0),…,g(x_{p−1})). The symbol-automorphism group is G(A) = {g : g(R(A)) = R(A)}. Rows may be reordered, but there is no column permutation, reversal or symbol-dependent change.
- **Product action.** (g, π) ∈ S_p × S_p acts by ((g,π)·A)_i = g(A_{π^{−1}(i)}).
- **Normalized arrays.** A is normalized iff A_0 = ι := (0,1,…,p−1) and A_r[0] = r for every r.

## 3. Written reconstruction (all odd primes)

**Lemma 0.** If A ∈ T1(p), every ordered pair (a,b) with a ≠ b occurs as a D1 event exactly once.

*Proof.* Rows are injective, so each D1 event has two distinct coordinates. The p(p−1) events are pairwise distinct, and there are exactly p(p−1) ordered pairs of distinct symbols. ∎

**Lemma 1.** If A ∈ T1(p) with p ≥ 2, its rows are pairwise distinct, so |R(A)| = p.

*Proof.* If A_r = A_s with r ≠ s, the event (A_r[0], A_r[1]) occurs in both rows. ∎

**Lemma 2.** Let (g,π) ∈ S_p × S_p.
- The D1 events of (g,π)·A are the images of those of A under (a,b) ↦ (g(a), g(b)), with multiplicity, and likewise for D2 events. Hence T1(p) and T2(p) are invariant.
- The formula defines a left action: ((g₁,π₁)·((g₂,π₂)·A))_i = g₁g₂(A_{π₂^{−1}π₁^{−1}(i)}) = ((g₁g₂, π₁π₂)·A)_i.
- R((g,π)·A) = g(R(A)). ∎

**Lemma 3 (free on rows).** Let A ∈ T1(p). Then G(A) acts on R(A), and only the identity fixes a row. Hence every G(A)-orbit on R(A) has |G(A)| elements, and |G(A)| divides p.

*Proof.* If g(A_r) = A_r, then g(A_r[j]) = A_r[j] for all j. Since A_r is onto Σ, g = id. By orbit–stabilizer, every orbit has |G(A)| elements, and the orbits partition the p-element set R(A) (Lemma 1). ∎

**Theorem A.** If p is an odd prime and A ∈ T1(p), then G(A) = {id}.

*Proof.* Suppose not. By Lemma 3 and primality, |G(A)| = p, so G(A) = ⟨g⟩ with g of order p.
1. *g is a single p-cycle.* The cycle lengths of g are at most p and have least common multiple p, so each is 1 or p. They are not all 1, and a p-cycle exhausts Σ. So g = (s, g(s), …, g^{p−1}(s)).
2. *Reduction to translation.* Let φ: Σ → Z_p be defined by φ(g^k(s)) = k. Replace A by (φ, id)·A. It is still T1 by Lemma 2, and its group is φG(A)φ^{−1}. We may therefore assume Σ = Z_p and that τ: k ↦ k+1 lies in G(A).
3. *The rows are translates.* By Lemma 3, ⟨τ⟩ acts freely on the p rows, so R(A) is a single orbit: R(A) = {x + k : k ∈ Z_p} for some row x, where x + k = (x_0+k, …, x_{p−1}+k).
4. *The differences are distinct.* Put d_i = x_{i+1} − x_i for 0 ≤ i ≤ p−2; each d_i ≠ 0. Suppose d_i = d_j with i < j, and put t = x_j − x_i, which is nonzero. Position i of row x + t carries (x_i + t, x_{i+1} + t) = (x_j, x_j + d_j) = (x_j, x_{j+1}). That is also the event at position j of row x. The rows x and x + t differ because t ≠ 0, so a D1 event repeats, contradicting T1. Hence d_0,…,d_{p−2} are p−1 distinct elements of the (p−1)-element set Z_p∖{0}, i.e. all of it.
5. *Endpoint contradiction.* Therefore Σ_i d_i = 1 + 2 + ⋯ + (p−1) = p·(p−1)/2 ≡ 0 (mod p), since (p−1)/2 is an integer for odd p. Telescoping gives Σ_i d_i = x_{p−1} − x_0. So x_{p−1} = x_0 although p−1 ≠ 0, contradicting the injectivity of x. ∎

*Where each hypothesis is used.* Primality is used only to obtain |G(A)| ∈ {1,p} and to make g a p-cycle. Oddness is used only in p(p−1)/2 ≡ 0. For p = 2 the residue sum is 1 ≢ 0 (mod 2), and the unique T1(2) row set {01, 10} has G = Sym(2) (control S1).

**Theorem B (free action).** Let p be an odd prime and let X be T1(p) or T2(p), as sets of ordered arrays. The action of S_p × S_p on X is free, and every orbit has exactly (p!)² elements. Hence (p!)² divides |X|, including the case |X| = 0.

*Proof.* X is invariant by Lemma 2. Suppose (g,π)·A = A. Then g(R(A)) = R(A) by Lemma 2, so g ∈ G(A) = {id} by Theorem A, which applies because T2 ⊆ T1. Then A_{π^{−1}(i)} = A_i for all i, and since the rows are distinct (Lemma 1), π = id. By orbit–stabilizer every orbit has |S_p × S_p| = (p!)² elements, and X is the disjoint union of its orbits. ∎

**Lemma C (complete adjacency count).** For any p ≥ 2 and A ∈ T1(p), each symbol begins exactly one row and ends exactly one row. In particular r ↦ A_r[0] is a bijection onto Σ.

*Proof.* Fix a symbol s. It occurs once in each row, so p times in all. An occurrence at a position j ≥ 1 is the second coordinate of exactly one D1 event, (A_r[j−1], s), and each D1 event (a, s) arises from exactly one such occurrence. By Lemma 0 there are exactly p−1 events of the form (a, s). So p−1 occurrences of s lie in columns ≥ 1, and exactly one lies in column 0. The argument for the last column is symmetric, using the out-events (s, b). ∎

**Theorem D (normalized representatives).** Let p be an odd prime and X as in Theorem B. Every orbit O ⊆ X contains exactly p normalized arrays. Hence #normalized(X) = p·#orbits ≡ 0 (mod p), and |X| = p!·(p−1)!·#normalized(X). Both counts may be 0.

*Proof.* Fix A ∈ O. For y ∈ R(A), let g_y be the unique symbol permutation with g_y(y) = ι, namely g_y(y_j) = j.
- *Construction.* (g_y, id)·A ∈ X by Lemma 2, so by Lemma C its rows have distinct first symbols. Let ν(A,y) be that array with its rows reordered so that row r begins with r. Then ν(A,y) ∈ O. Its row 0 is ι, because ι begins with 0 and only one row begins with 0. So ν(A,y) is normalized.
- *Every normalized array arises.* Let B ∈ O be normalized, say B = (h,σ)·A. Then R(B) = h(R(A)) contains B_0 = ι, so ι = h(y) for some y ∈ R(A), and h = g_y. By Lemma C the start-ordering of R(B) is unique, so B = ν(A,y).
- *Distinct choices give distinct arrays.* Suppose ν(A,y) = ν(A,y′) with y ≠ y′. Then g_y(R(A)) = g_{y′}(R(A)), so h = g_{y′}^{−1}g_y lies in G(A). But h(y) = g_{y′}^{−1}(ι) = y′ ≠ y, so h ≠ id, contradicting Theorem A.

So O has exactly |R(A)| = p normalized arrays. Combined with Theorem B, |X| = (p!)²·#orbits = ((p!)²/p)·#normalized(X). ∎

*General identity used to read the even-order controls (any p ≥ 2).* The stabilizer of A has order |G(A)|, and the orbit of A contains exactly p/|G(A)| normalized arrays. This is because ν(A,y) = ν(A,y′) iff y′ ∈ G(A)y, and G(A) acts freely on R(A).

**Corollary (order 11, existence-free).** Since 11 is an odd prime, #normalized T2(11) ≡ 0 (mod 11) and |T2(11)| ≡ 0 (mod (11!)²). Both hold whether or not T2(11) is empty. They give no existence, nonexistence or bound.

## 4. Per-claim verdicts

| Source LF | Claim | Verdict |
|---|---|---|
| In1 LF1–3 | Universal statement: every T1(p), p an odd prime, has a trivial symbol-automorphism group (rows reorderable, in-row order kept). Stated as unconditional, with no existence claim and no Latin or cyclic hypothesis | VERIFIED (Theorem A) |
| In1 LF3 | Every original Tuscan-2(11) witness has this asymmetry | VERIFIED as a universally quantified statement over a possibly empty set (T2 ⊆ T1); no existence content |
| In1 LF7 | Array and automorphism definitions; all p(p−1) ordered pairs are present | VERIFIED (Lemma 0; the definitions match section 2) |
| In1 LF9 | Rows distinct; fixing one row forces the identity; free action; \|G\| divides p; a group of order p is cyclic, generated by a p-cycle; relabel to +1; the rows are translates | VERIFIED (Lemmas 1 and 3; Theorem A) |
| In1 LF11 | Equal differences repeat an event; the differences are exactly the nonzero residues; their sum is ≡ 0 for odd p; telescoping gives the endpoint contradiction | VERIFIED (Theorem A). That the translate t = x_j − x_i is nonzero is left implicit; see NIT |
| In1 LF13 | p = 2 excluded: residue sum 1, and rows 01, 10 have the swap automorphism. No claim about column, reversal or symbol-dependent symmetries; not a characterization or a nonexistence proof | VERIFIED (control S1, n = 2); the scope statement is accurate |
| In1 LF17 | 1990 source definition and page claims; Ollis Roman-2 order 21; Ollis theorem not imported | NOT ADJUDICATED (outside frozen scope: literature/priority; no web access) |
| In1 LF19 | p = 11 T1 nonvacuity via the cited JSON files; 110 distinct D1 events; 91 of 99 D2 events distinct | NOT ADJUDICATED (the files are not manifest inputs, and order 11 is excluded). The closing sentence, that the universal proof uses no finite computation or this example, is VERIFIED. Independent nonvacuity at the odd prime 7 comes from control S3 |
| In2 LF1–3 | Framing: written counting consequences, not existence, census or novelty; cites input 1 by SHA-256 | VERIFIED. The cited hash equals the live hash of input 1 |
| In2 LF5 | The S_p×S_p action on T1(p) or T2(p) is free; orbit size (p!)²; (p!)² divides \|X\|, including 0; no column or reversal quotient | VERIFIED (Theorem B). See MINOR-1 on the implicit T2 definition and invariance |
| In2 LF7 | One row begins with each symbol, by the indegree p−1 count | VERIFIED (Lemma C) |
| In2 LF9–10 | Globally valid canonical shape: relabel a chosen row to 0..p−1, then order rows by first symbol | VERIFIED (the construction in Theorem D) |
| In2 LF12 | The p outputs are distinct; converse; exactly p normalized representatives per orbit; normalized T1 and T2 counts divisible by p | VERIFIED (Theorem D) |
| In2 LF14 | #normalized T2(11) ≡ 0 (mod 11) and #T2(11) ≡ 0 (mod (11!)²); no positivity, bound or enumeration certification | VERIFIED as existence-free consequences (Corollary) |
| In2 LF14 | The SAT model uses exactly the valid normalization; its 45-second run was UNKNOWN; that status is unchanged | NOT ADJUDICATED (external code and run files not opened; SAT excluded). Theorem D establishes only that restricting a search to normalized arrays loses no orbit |

## 5. Findings

- **FATAL:** none.
- **MAJOR:** none.
- **MINOR-1 (definition clarity; validity unaffected).** Neither input states the T2(p) condition explicitly. Input 2 LF5 says only "its T2(p) subset under the same linear directed-event definitions", and input 1 mentions "distance-two events" only in LF19.
  - Theorems B and D need only that the T2 subset is invariant under symbol relabelling and row permutation.
  - That invariance holds for the standard linear Tuscan-2 condition used here (pairwise distinct (x_j, x_{j+2}) events). It also holds for any condition stated as pairwise distinctness of fixed-offset events.
  - Repair: state the D2 condition and its invariance explicitly.
- **NIT (no severity).**
  - In1 LF3: "has trivial symbol-permutation automorphism" should read "has trivial symbol-automorphism group".
  - In1 LF11 leaves implicit that the translating element t = x_j − x_i is nonzero, so the two rows differ. This is harmless, because any repeated D1 event violates T1 anyway.
- **INCONCLUSIVE (in scope):** none.

## 6. Bounded controls (run-01, the single receipted run)

**Artifacts.** All files are in this wave directory, reviewer-prefixed and created exclusively.

| File | SHA-256 | Bytes |
|---|---|---|
| `ReviewF175TuscanOrbit-control-v1.py` | `489efa2a9a5860dcdfb533fdaa823eb7865747518d7e79899166934937cf5e8f` | 29,747 |
| `ReviewF175TuscanOrbit-runner-v1.py` | `9f12de585c52ee848103fcf4e83d8c974c7f149faf2e705bb9a133b8bc094573` | 4,010 |
| `ReviewF175TuscanOrbit-control-run-01-receipt.json` | `722855d4ec28a0de840dffa68497dea210d8b074db7652f7ad52f8a44604c583` | 2,769 |
| `ReviewF175TuscanOrbit-control-run-01-results.json` | `ff8e6eee78f4be442276cd30f4451ae1e9ea448379acd4215b0eef17e2945e52` | 90,023 |
| `ReviewF175TuscanOrbit-control-run-01-stdout.txt` | `817fdca76c6a6fed275d501a03daa2a0509fdd5cac38e266f59e6dae3d5202db` | 215 |
| `ReviewF175TuscanOrbit-control-run-01-stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |

**Receipt.**
- Native clock before `2026-10-29T08:04:09-0700 PDT`, after `2026-10-29T08:04:11-0700 PDT`; monotonic wall time 1.848 s.
- Hard limit 60 s; not timed out. **Exit code 0.**
- The control's SHA-256 was identical before and after the run.
- Python 3.14.3, standard library only; seed 20261029.
- Results: 136 recorded expectations, 0 failed, no exceptions, no skipped section.

**Per section (expectations passed / total).**

- **S0, checker and intended-reason negatives (7/7).**
  - (01,10) is accepted as T1.
  - The following are all rejected: duplicate rows; a non-permutation row; five distinct p = 5 rows that all start with 0; the p = 5 translates of 01234 (repeated difference 1, duplicated events 01, 12, 23, 34, 40).
  - The n = 4 translates of 0132 are T1, with G ⊇ ⟨x↦x+1⟩ and |G| = 4.
- **S1, complete orders 2–5 (79/79).** Two independent complete enumerations agree: an exact cover that branches on the most constrained pair, and an increasing-index DFS over disjoint rows. A direct normalized DFS agrees with the normalized arrays of X.
  - **p = 2 (negative boundary).** One row set, {01,10}, so |X| = 2 and G = Sym(2). Every S_2×S_2 stabilizer has order 2, including (swap symbols, swap rows). There is one orbit of size 2 ≠ (2!)² = 4, and |X| mod 4 = 2. Each orbit has one normalized array, not p. So the odd-prime conclusions fail at p = 2 for the intended reason.
  - **p = 3 and p = 5.** T1(p) = ∅ (complete; 3 and 601 exact-cover nodes respectively). The theorem expectations hold only vacuously: |X| = 0 ≡ 0 and #normalized = 0 ≡ 0. **No T1 examples exist at p = 3 or p = 5.**
  - **n = 4 (even, outside scope).** 6 row sets, each with |G| = 4. |X| = 144, forming a single orbit of size 144 = 576/4. Stabilizers have order 4, there is one normalized array per orbit (= n/|G|), and |X| mod 576 = 144.
  - Every array found has distinct starts and ends and satisfies the indegree identity of Lemma C. In every case orbit size × stabilizer order = (n!)², and stabilizer order = |G|.
- **S1b, order 6, even, outside scope (11/11).** Complete over row sets that contain ι; Lemma C is not assumed.
  - There are 736 such row sets, matching the 736 arrays from the direct normalized DFS. The Lemma C identities hold on all of them.
  - |G| distribution: {1: 708, 2: 24, 3: 2, 6: 2}, giving 129 orbits. Normalized arrays per orbit × |G| = 6 in every case.
  - Nontrivial symbol automorphisms occur at even order 6, so the parity/primality hypothesis is genuinely needed.
- **S2, cyclic translates and endpoint sum (27/27).**
  - Number of bases x of Z_n with x_0 = 0 and pairwise distinct consecutive differences, for n = 2…9: 1, 0, 2, 0, 4, 0, 24, 0.
  - For n ≤ 7, over all n! bases, the translate family is T1 iff the differences are distinct.
  - For every such base, x_{n−1} − x_0 equals the residue sum (n/2 for even n).
  - The example translate families at n = 2, 4 and 6 carry the translation automorphism.
  - So the endpoint-sum step is exactly what fails for even n and what excludes odd n, including composite n = 9.
- **S4, residue sums (2/2).** For the 46 primes below 200, 1+⋯+(p−1) ≡ 0 (mod p) for odd p, and ≡ 1 for p = 2.
- **S3, p = 7 bounded sample (10/10).** This is **not** a census, not a count, and not theorem evidence.
  - A seeded randomized exact cover, with no normalization or start-symbol assumption, returned 24 distinct T1(7) arrays in 24 attempts.
  - Each array satisfies all of the following:
    - it is T1, and the Lemma C identities hold;
    - |G| = 1 by brute force over all 5,040 symbol permutations, and the structural method agrees;
    - its orbit contains exactly 7 distinct normalized arrays, with renormalization closure;
    - its S_7×S_7 stabilizer is {(id,id)}, checking g over the brute-forced G and π over all 5,040 row permutations;
    - it is not T2 (20–29 of the 35 D2 events are distinct).
  - Mutation control: swapping two adjacent entries of one row breaks T1.
  - **First actual example** (rows as found): 4016325 / 3102654 / 5346120 / 0362451 / 1423056 / 2150643 / 6041352. A hand check confirms that its 42 D1 events are exactly the 42 ordered pairs.
  - Its least normalized representative: 0123456 / 1406253 / 2130465 / 3264150 / 4316052 / 5420361 / 6351024.
  - All 24 arrays are listed in the results JSON.
  - The heavy exhaustive p = 7 census was not run, and no p = 7 count is claimed.

## 7. Limitations

- **Same-harness only.** This is not human, independent-model-family, formal/kernel or novelty/priority verification, and it implies no parent adoption.
- **What the controls cover.** Acceptance of the all-odd-prime theorem rests on the written proof in section 3. The finite controls are diagnostics for orders ≤ 7 only:
  - complete for p = 2, 3 and 5, and for n = 4;
  - complete for n = 6 over row sets containing the identity row;
  - a bounded sample at p = 7.
- **Excluded work.** No order-11 computation, no T2(11) existence or exclusion, and no SAT/DRAT. The external files cited in In1 LF17/LF19 and In2 LF14 were not opened.
- **Symmetries treated.** Only symbol relabelling and row permutation. Column permutations, reversal and other symmetries are untreated, as the candidates themselves state.
- **Checker risk.** The checkers are reviewer-authored. Agreement across algorithms, brute force and mutation controls reduces checker error but does not exclude it.

## 8. Deviations (all disclosed; none affects section 3)

1. A parent-directed capacity pause interrupted the review after the complete source reads. No file had been created. On resume the manifest and inputs were re-hashed and found unchanged.
2. Before the pause, unreceipted development executions ran in the in-memory kernel: a normalized-enumeration prototype at orders ≤ 7, including a roughly 211-second exhaustive order-7 prototype, and exact-cover timing at orders ≤ 6. The kernel was reset at the pause. Per parent direction these runs are not evidence: none of their outputs is reported or relied on here, and the order-7 prototype was not rerun.
3. The parent process record `parent-capacity-resume-v1.json` in this wave directory was read at resume, after the scientific inputs, as process metadata only.
4. One `ast.parse` syntax check of the two reviewer scripts preceded run-01. It executed no control logic and wrote no files.
