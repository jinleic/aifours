# f139 review — projection-only four-block selector: F=3p−2, p distinct-label odd projection runs, actual factor σ_cρ_uσ_cρ_v ⇒ a 2p original-order identity subsequence (arbitrary u,v)

- Review id: `f139-olson-projection-fourblock-selector`
- Kind: INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (not human, not independent-model-family, not formal/kernel, not novelty/priority clearance)
- Observed native clock before composing this file: `2026-10-29T03:52:18Z` = `Wed Oct 28 20:52:18 PDT 2026` (`/bin/date`; the post-write hash of this file is in `reviewer-receipt-v1.json`)
- Authority: `contract-addendum-2-frontier-first-owner-direction-v1.json` (as named by the manifest; not re-read here)
- Manifest: `manifest-v1.json`, SHA-256 `8e1cffa98cecedccca4194318f96b5e03c44d606825b9e0f7b1b967bd54aaf91`, 3582 bytes — live `shasum` at `2026-10-29T03:34:14Z` matched the assignment hash before anything else was opened.
- Author: MathOlson-2-2 (slot math-2). No author contact. No web search, no external model, no paid API, no Git, no deletion, no publication, no infrastructure action. The author's checker was read but **never executed or imported**.

## 1. Inputs read, in declared order, with live verification

All hashes/byte counts/LF counts were recomputed with `shasum -a 256`, `wc -c`, `tr -cd '\n' | wc -c` at `2026-10-29T03:34:25Z`, before reading. Every file was read completely with `:raw` (exact bytes, no context lines).

| # | Role | File | SHA-256 | bytes | LF | Verified |
|---|------|------|---------|-------|----|----------|
| 1 | MANDATORY fatal actual-block correction (read first) | `ordered-olson/frontier-20261028-olson-actual-block-fatal-correction-v1.json` | `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e` | 9278 | 92 | yes, first and complete |
| 2 | registered ordered-word definitions | `written-releases/math-2-ordered-word-definitions-v1.md` | `010ef028f750f718df327102ec92e1803289169b512d361bf66ed2e28145c9fc` | 1275 | 16 | yes |
| 3 | candidate | `ordered-olson/frontier-20261028-olson-projection-fourblock-selector-v1.md` | `eedd10defe0b7cc0d8a349fc4d8937c7ecc67b1c032c4eec4722a506143a4075` | 6220 | 53 | yes, complete |
| 4 | author checker (hash/read only) | `ordered-olson/frontier-20261028-olson-projection-fourblock-checker.py` | `230ccb2ed473f3e91b9248c7d0c289552049a5a690907e8ffbefd11ab578b60b` | 3893 | 87 | yes, read only, never run |
| 5 | author result | `ordered-olson/frontier-20261028-olson-projection-fourblock-check-results.json` | `c57e831e006beeede91e09560d8a90735ccf5303111b72951fa46054c8b244bc` | 448 | 16 | yes |

The manifest's 8-hex `expected` prefixes (`e11fd873`, `eedd10de`, `230ccb2e`, `c57e831e`) match. The candidate's quoted SHA for input 1 (L5) and for its own checker/result (L47–49) match inputs 1, 4, 5.

**What the FATAL correction binds here (input 1, applied before the candidate).** It establishes that *actual* constant reflection blocks (where an occupied rotation gap between equal reflection exponents splits a block) are a different object from *projection runs* (rotation-deleted maximal constant runs), that the historical actual o_F/e_F/H symbols must not be attached to projection runs, that the whole f111 adoption and its lift/profile/floor consumers are WITHDRAWN/HELD with nothing transferred (including its "former 0F review or standalone lemma fragment"), and that "the direct ordered-four lemma may only proceed as a separate NEW disjoint review". This review is such a new disjoint review at projection-only scope; it reads nothing from the held inventory, and §6 below audits that the candidate makes no actual-block claim and that nothing here flows back to f111.

Not opened (by design): the AP-characterization candidate the candidate cites in §4 (`…projected-odd-ap-characterization-v1.md`, SHA `3901cf26…`) — the candidate states it does not rely on it, and my verdict does not either; any file in the correction's `affected_candidate_inventory`; any other review wave's Olson material. One non-Olson sibling review header (f132, L1–30) was glanced at for file-format conventions only.

## 2. Definitions fixed for this review

**Original ordered target (input 2, L4 excerpt and the "Original ordered target" paragraph).** For every finite group G of order n and every sequence a_1,…,a_{2n−1} in G there exist indices i_1<⋯<i_n with a_{i_1}⋯a_{i_n}=e (product in that index order). Here G=D_{2p}, n=2p, the sequence has length 4p−1 and the required selection has exactly 2p indices in increasing original order. No restriction of the target is implied; the candidate is a *sufficient condition* for one explicitly described class of sequences.

**Dihedral conventions (mine; the candidate's are equivalent, see 3.1).** p an odd prime. D_{2p}=⟨ρ,σ | ρ^p=σ^2=e, σρσ=ρ^{−1}⟩. Every element is ρ^xσ^e, written (x,e), x∈F_p, e∈{0,1}, with law (x,e)(y,b)=(x+(−1)^e y, e⊕b). A **rotation ρ_u** is (u,0) (u=0 is the identity letter, allowed). A **reflection with label c**, σ_c:=ρ^cσ=(c,1). Two facts used throughout: σ_aσ_b=ρ^{a−b} and σ_cρ_uσ_cρ_v=ρ^{v−u}. (If one instead writes σ_c=σρ^c, all labels are negated; distinctness and "all of F_p" are preserved and the argument goes through with t replaced by −t, so the theorem is convention-independent.)

**Actual word.** W=(a_0,…,a_{N−1}), N=4p−1, with exactly F=3p−2 reflection letters and R=p+1 rotation letters (counts fixed by the candidate's §1). W is a linear sequence; "cyclic" statements treat index N−1 as adjacent to 0.

**Reflection-only projection and projection runs.** Delete every rotation letter; the remaining F labels, in cyclic order, form the projection. A **projection run** is a maximal cyclically-contiguous constant segment of this label sequence; its **label** is the common value; it is **odd/even** by its length. Cyclically adjacent runs have different labels (maximality); non-adjacent runs may share a label. The degenerate single-run case (all F labels equal) is excluded by the hypothesis (p≥3 runs). Projection runs are **not** the FATAL correction's actual blocks: a rotation sitting between two equal-label reflections splits an actual block but is invisible to the projection. The candidate uses only the projection notion (§1: "DELETE rotations only to define its cyclic reflection-only projection"), which is exactly what the correction demands.

**Pair count.** H_π:=Σ_runs⌊ℓ/2⌋=(F−#odd runs)/2.

**Actual four-letter factor ("four-block" in the candidate).** Four cyclically consecutive letters a_s,a_{s+1},a_{s+2},a_{s+3} (indices mod N) equal to σ_c,ρ_u,σ_c,ρ_v. Its two σ_c are adjacent in the projection, hence automatically in one run; the hypothesis requires that run to be odd. The word "block" here means a four-letter factor of the actual word, not an actual constant reflection block (see MINOR-1).

**Hypothesis H(p,W).** (i) counts as above; (ii) exactly p odd projection runs; (iii) their labels are pairwise distinct (equivalently, they are all of F_p); (iv) even runs arbitrary in number, lengths and labels; (v) W contains an actual four-letter factor σ_cρ_uσ_cρ_v whose σ_c lie in an odd run; u,v∈F_p arbitrary. **Claim C(p,W):** there are 2p indices i_1<⋯<i_{2p} with a_{i_1}⋯a_{i_{2p}}=e.

Parity sanity: Σℓ over p odd runs ≡ p ≡ 1 ≡ 3p−2 (mod 2), so (ii) is consistent with F; H_π=(3p−2−p)/2=p−1.

## 3. The claim, reconstructed and checked step by step

### 3.1 Cut and block product
Cut the cyclic word immediately before a_s. In cut order the factor comes first and a_sa_{s+1}a_{s+2}a_{s+3}=σ_cρ_uσ_cρ_v=ρ^cσ·ρ^u·ρ^cσ·ρ^v=ρ^{c−u}σρ^cσρ^v=ρ^{c−u}ρ^{−c}ρ^v=ρ^{v−u}. Matches the candidate (L25). The same value results in the other convention.

### 3.2 Pairs after removing the factor's two reflections
The run R* containing the two σ_c is odd of length ℓ≥3 (it contains two letters and is odd). Removing them leaves ℓ−2≥1, odd. ⌊(ℓ−2)/2⌋=⌊ℓ/2⌋−1, so the available pair count drops from p−1 to exactly p−2 (candidate L27). In cut order R*'s residue appears as a piece of length a immediately after the factor and a piece of length b at the very end, a+b=ℓ−2 odd, so exactly one of a,b is odd and ⌊a/2⌋+⌊b/2⌋=(a+b−1)/2=⌊(ℓ−2)/2⌋ (candidate L31). All other runs are contiguous in cut order because the cut lies inside R*.

### 3.3 Run-piece product (the fact the candidate uses implicitly)
Let the post-factor selected letters be reflections only. The cut-order projection (minus the two factor reflections) is a concatenation of **run-pieces**: R*'s a-piece, then every other run intact, then R*'s b-piece. If k_j letters are selected from piece j (label c_j), the selected product in cut order is ∏_j σ_{c_j}^{k_j}, because within a piece all labels coincide and no letter of another piece lies between two letters of the same piece. Even k_j gives e; odd k_j gives σ_{c_j}. Hence if exactly two pieces have odd k — the earlier with label x, the later with label y — the product is σ_xσ_y=ρ^{x−y}; if none has odd k the product is e. This is precisely why "each chosen equal pair is an identity subproduct in its actual order" (L33) is legitimate: pairs are taken inside pieces, so no representative can sit between the members of a pair (see MINOR-3; the candidate's argument is correct, only the contiguity remark is left implicit).

### 3.4 Directed-difference lemma (candidate §2) — proved
**Statement.** Let x_1,…,x_p be any linear ordering of all elements of F_p and t≠0. Then there are i<j with x_i−x_j=t.
**Proof 1 (the candidate's).** Suppose not. For every x, the element x−t occurs somewhere; if pos(x)<pos(x−t) then with i=pos(x), j=pos(x−t) we get x_i−x_j=t, contradiction; so pos(x−t)<pos(x) for every x. Iterating along x, x−t, x−2t,…, x−pt=x gives pos(x)<pos(x), impossible. ∎
**Proof 2 (one line).** x↦x−t is a bijection of F_p, so Σ_x(pos(x)−pos(x−t))=0; if every term were positive the sum would be positive. ∎
**Remarks.** (a) Primality is **not** used: the same proof works in any finite abelian group for any t≠0, as long as the ordering contains all elements (or at least a full ⟨t⟩-coset). The candidate's sentence "This uses primality only to make nonzero t generate all F_p" (L23) overstates the dependency; harmless (MINOR-2). (b) The "all of F_p" hypothesis is essential: the ordering 1,2,…,p−1 (0 missing) realizes earlier-minus-later residues only in {2,…,p−1}∪{0}, never 1. This is exactly what the distinct-labels premise supplies and what my adversarial controls (§4.5) exercise. (c) The lemma applied to the two representatives' cut order gives an earlier x and later y with x−y=u−v, hence (3.3) product ρ^{u−v} — the candidate's "reflection product has exponent u−v" (L33) is the correct sign.

### 3.5 Assembly and count
Reserve from each odd run the unpaired letter of its odd piece (R* contributes the leftover of whichever of its two pieces is odd). These p representatives have the p distinct labels, i.e. all of F_p, in some cut order. Even runs supply pairs only.
- u=v: select the factor and all p−2 pairs: 4+2(p−2)=2p letters; product ρ^{0}·e=e.
- u≠v: select the factor, two representatives x (earlier), y (later) with x−y=u−v (lemma), and any p−3 of the p−2 pairs (pairs and representatives are disjoint by construction): 4+2+2(p−3)=2p letters; product ρ^{v−u}·ρ^{u−v}=e. p≥3 makes p−3≥0.
Pieces with odd selected count are exactly the two representatives' pieces (u≠v) or none (u=v), so 3.3 applies.
**Return to original order.** Restricted to the selected positions, the original increasing order is a cyclic rotation of the cut order: if g_1⋯g_{2p}=e then g_k⋯g_{2p}g_1⋯g_{k−1}=(g_1⋯g_{k−1})^{−1}(g_1⋯g_{2p})(g_1⋯g_{k−1})=e. The 2p positions are distinct. Hence C(p,W). ∎

### 3.6 Edge cases checked
Factor wrapping the linear end (indices N−2,N−1,0,1 etc.): covered, since everything is cyclic and 3.5's rotation step handles it. R* wrapping the linear end: covered likewise. ℓ−2=1: one piece of length 1 (the representative), the other empty. Even runs sharing a label with a non-adjacent odd run: irrelevant (even runs only supply pairs). u or v equal to 0 (identity letters in the sequence): allowed by the original target and by the proof. R>2 rotations elsewhere, several rotations in one gap, rotations immediately after ρ_v: never selected, irrelevant. The hypothesis clause "lie in the SAME ODD projected run": "same" is automatic (MINOR-6), oddness is the real condition.

**Conclusion of §3.** The written proof is correct at the stated scope; every step reconstructs with no hidden premise beyond the stated hypothesis and elementary dihedral arithmetic.

## 4. Independent exact finite control (reviewer-written; author code never executed)

Files (all in this review directory; hashes recomputed after the run at `2026-10-29T03:50:48Z`):

| File | SHA-256 | bytes |
|------|---------|-------|
| `reviewer-control-v1.py` | `640f244759b544dd200a03f72b4e8b5fd50c500d0e9957af3bd317337c56c3ab` | 28486 |
| `reviewer-control-results-v1.json` | `91712226e6c84e6fb22795d43e523dd50bb51ea0f620654064d8e0700f759d47` | 19503 |
| `reviewer-control-fixtures-v1.json` | `f599bbabd477b895b3caad7dd181b792868154b8b890dfd719db350835c0c492` | 1647650 |
| `reviewer-control-stdout-v1.txt` | `ad1b4241df565955013d1190e48070e9aefeed9a88020276f8a60157150c991e` | 8632 |
| `reviewer-fatal-word-crosscheck-v1.txt` | `ed74c048f073443adadc4eb6a87a8130023140ce7c6dc5d20ed8804d35b928d1` | 1844 |

Run: `python3 reviewer-control-v1.py --results reviewer-control-results-v1.json --fixtures reviewer-control-fixtures-v1.json --per-p 400`, cwd = this directory. `/bin/date` before `2026-10-29T03:49:54Z` (`Wed Oct 28 20:49:54 PDT 2026`), after `2026-10-29T03:50:48Z`; the results file's own `clock_start_utc`/`clock_end_utc` are the same values; `wall_seconds` 53.902; `script_sha256` inside the results equals the file hash above; `fixtures_sha256` inside the results equals the fixtures hash above. Python 3.14.3, macOS 27.0.1 arm64, seed 20261028139. Standard library only. Output files are opened with mode `x` (refuse overwrite). Development iterations ran in `/tmp/f139-scratch` and are not evidence.

Design (structurally my own; I had read the author's checker but no author producer; nothing of the author's is imported, and my producer, premise checker, recipe implementation, DP and mutations were written from §2–§3 above):
- **Group self-test** at each p: the (x,e) law agrees with the faithful permutation representation ρ:i↦i+1, σ:i↦−i on all (2p)² products; relations ρ^p=σ²=e, σρσ=ρ^{−1}; σ_aσ_b=ρ^{a−b} for all a,b; σ_cρ_uσ_cρ_v=ρ^{v−u} for all c,u,v. All true for p∈{3,5,7,11,13}.
- **Producer**: random odd-run lengths (block run ≥3), random permutation of F_p as odd labels, 0–3 even runs (capped at p−2) inserted at random cyclic positions with random labels differing from both neighbours (so even labels may repeat odd labels), one singleton gap ρ_u between two adjacent letters of the block run, ρ_v first in the next gap, the remaining p−1 rotations with random values (0 allowed) in random gaps (several per gap allowed), and a random cyclic offset so factors and runs wrap the linear end. 80% of words have u≠v, 20% u=v.
- **Premise checker** from the word alone (N, letter ranges, F, cyclic runs via rotate-to-boundary + `groupby`, odd count, distinct labels); **all** actual four-letter factors in odd runs are found and each is tested, not only the producer's.
- **Recipe** = §3.5 literally (cut, pieces, pairs inside pieces, representatives, lemma search for x−y=u−v, p−3 or p−2 pairs with a random dropped pair, sort to original order), then **verification by direct multiplication in original order in both representations** (any disagreement would abort).
- **Recipe-independent DP**: does *any* 2p-term increasing subsequence multiply to e (set DP over (count, element)).
- **Verifier sensitivity**: each verified selector is corrupted by replacing one index with a random unselected index; the verifier must usually report non-identity.

### 4.1 Positive random control (hypothesis-satisfying words)

| p | words | u≠v / u=v words | factors tested (t≠0 / t=0) | factors wrapping end | even runs 0/1/2/3 | recipe identity | recipe failures | pairs available = p−2 always | DP identity |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 400 | 320/80 | 528 (407/121) | 148 | 193/207/–/– | 528/528 | 0 | yes | 400/400 |
| 5 | 400 | 320/80 | 557 (444/113) | 97 | 109/84/113/94 | 557/557 | 0 | yes | 400/400 |
| 7 | 400 | 320/80 | 675 (554/121) | 85 | 96/108/101/95 | 675/675 | 0 | yes | 400/400 |
| 11 | 400 | 320/80 | 885 (760/125) | 68 | 100/97/97/106 | 885/885 | 0 | yes | 400/400 |
| 13 | 400 | 320/80 | 970 (848/122) | 46 | 95/95/96/114 | 970/970 | 0 | yes | 400/400 |

Totals: 2000 words, 3615 factors, 3615/3615 recipe selectors multiply to e in original order in both representations; up to 6 distinct factors in one word were each tested. All 2000 words and every selector are pinned in the fixtures file (letters encoded 2x+e).

Verifier sensitivity: 7230 single-index corruptions, 6654 reported non-identity (p=3: 861/1056; 5: 1013/1114; 7: 1256/1350; 11: 1679/1770; 13: 1845/1940). The remainder are corruptions that happen to preserve the product (e.g. swapping a pair member for another same-label letter); the verifier is not a constant function.

### 4.2 Exhaustive control at p=3 (N=11, F=7, R=4)
All 3^7=2187 cyclic label sequences were enumerated; **420** meet (ii)+(iii). With all C(11,4)=330 rotation-position patterns: **138,600** skeletons meet the premise; **16,434** contain at least one factor in an odd run. For every such skeleton, every factor, and every (u,v)∈F_3²: **174,636** recipe cases, **174,636** identity (branches t=0/e0 33,264; t=0/e1 24,948; t≠0/e0 66,528; t≠0/e1 49,896). Since the recipe selects exactly two rotation letters (the factor's), its product is independent of the other rotation values; this is therefore an exhaustive verification of the *construction* at p=3. Independently of the recipe, the DP found a 6-term identity subsequence in **all 1,331,154** words obtained from the 16,434 skeletons by all 3^4 rotation-value assignments (and in all 174,636 others-zero cases and 8,726 random-others samples). So C(3,W) holds for every W satisfying H(3,W).

### 4.3 Mutation control M1 — break distinct labels (random)
One odd run of a produced word is relabelled to another odd run's label while keeping every run boundary (new label ≠ both neighbours), so (ii) and (v) survive and only (iii) breaks. Mutable words: p=3 207/400 (the rest have no boundary-preserving relabel), p=5,7,11,13 400/400. **Rejected by the premise checker with the intended reason `PREMISE_LABELS_NOT_DISTINCT`: 207/207, 400/400, 400/400, 400/400, 400/400; zero other rejections; zero survivals.** Bypassing the premise and running the recipe on the designated factor: at p=3, t≠0 cases 54 `NO_DIRECTED_PAIR` / 106 succeed; p≥5 all t≠0 cases succeeded (with p−1 distinct labels the needed difference is usually still realized). The DP (informational, not part of the claim) still found some 2p identity subsequence in every mutant.

### 4.4 Mutation control M2 — break the run count (random)
A boundary letter of an odd run A (length ≥3) is relabelled to the label of a cyclically adjacent odd run B, neither containing the designated factor: both become even, leaving exactly p−2 odd runs with distinct labels, F unchanged, factor intact — only (ii) breaks (shape asserted in code). Mutable: p=3 122, 5 229, 7 371, 11 400, 13 400. **Rejected with the intended reason `PREMISE_ODD_RUN_COUNT`: 122/122, 229/229, 371/371, 400/400, 400/400; zero other, zero survived.** Recipe bypass on t≠0 factors: p=3 94/94 `NO_DIRECTED_PAIR`; p=5 57 fail / 127 succeed; p=7 14/291; p≥11 all succeed. DP informational: identity subsequence found in every mutant.

### 4.5 Deterministic adversarial families (uniform load-bearing demonstration at every p)
Because random mutants at large p rarely defeat the recipe, I constructed for each p∈{3,5,7,11,13} a word per broken premise on which the recipe **must** fail for the factor value u−v=1, by 3.4(b):
- `labels`: odd runs with cut-order labels 1,2,…,p−1,p−1 (0 missing; the duplicate is separated from its twin by an even run of label 0 and length 2); block run label 1 of length 2p−3; F=(2p−3)+(p−2)+2+1=3p−2. Checker: `PREMISE_LABELS_NOT_DISTINCT` at all five p; recipe bypass `NO_DIRECTED_PAIR` at all five p.
- `runcount`: p−2 odd runs with distinct labels 1,…,p−2 plus one even run (label 0, length 4); F=(2p−3)+(p−3)+4=3p−2. Checker: `PREMISE_ODD_RUN_COUNT` at all five p; recipe bypass `NO_DIRECTED_PAIR` at all five p.
Both words are stored letter-by-letter in the results (`word_letters_(x,e)`); e.g. p=3 `labels`: σ₁ρ₁σ₁ρ₀σ₁σ₂σ₀σ₀σ₂ρ₀ρ₀. The DP still finds some other 6-term identity subsequence there (informational) — the controls show the **recipe's** dependence on the two premises, not that the conclusion fails without them.

### 4.6 Cross-check against the FATAL correction's explicit word (consistency, not transfer)
The correction's all-prime family Z ρ Z ρ Z^{2p−3} ρ (T_1 ρ)…(T_{p−2} ρ) T_{p−1} (Z=σ_0, T_j=σ_j, ρ=ρ_1) was rebuilt from its JSON text for p=7,11,13,17: my checker finds F=3p−2, exactly p odd projection runs with distinct labels, 0 even runs, one factor (σ_0ρ_1σ_0ρ_1, u=v=1) in the odd run — so H(p,W) holds and the candidate's criterion applies; my recipe (t=0) returns an identity selector in both representations at each p, and the correction's own listed 0-based p=11 selector `[0,1,2,3,4,5,6,7,8,9,23,24,25,27,29,31,33,35,37,38,39,41]` (22 indices) independently multiplies to e. This agrees with the correction's statement that "the literal SEL predicate applies" to that word and that it is "neither an Olson nor L_RES counterexample". Nothing about actual o_F/e_F is inferred from this.

### 4.7 What the controls do not show
They are bounded same-harness checks (five primes, 2000 random words, exhaustive only at p=3). They do not establish the universal proof (that is §3's written argument), do not test p≥17 beyond 4.6, do not bear on whether factors (v) or hypotheses (ii)–(iii) occur in any residual class, and are not an external-family, human, formal or novelty verification. They do confirm the author's finite assertion in kind (independent words, independent code) without reusing the author's 500 words.

## 5. Author checker and result — read-only observations (not evidence)
`frontier-20261028-olson-projection-fourblock-checker.py` was read, not run. Its logic is consistent with the claim: same (x,e) law as mine; cyclic runs from the first boundary; premise = p odd runs, declared even count, p distinct odd labels; factor positions cyclically consecutive with form [1,0,1,0] and equal reflection values inside an odd run; target u−v; selector 2p sorted distinct indices containing the factor; rest = 2p−4 reflections in cut order; block product ρ^{−target}, rest product ρ^{target}; active-run parity pattern (none for t=0, exactly two odd runs otherwise); and finally the original-order product of the selector = identity. It imports no producer. The result JSON reports 500 cases with branch sum 225+221+25+29=500, two intended-reason controls (`SELECTOR_INDICES`, `TARGET_METADATA`) and `input_sha256` = `5221e84b…` matching the candidate's stated producer-output hash (L47). Author scope limitation (L47): words had "zero or one EVEN projected run"; the theorem allows arbitrary even runs, which my controls cover with 0–3 even runs (MINOR-5). None of this is treated as verification; §4 is.

## 6. Non-claim and transfer audit
Grep of the candidate for `o_F|e_F|floor|f111|actual block|actual-block|lift|L_RES|residual` returns only negations: L3 "It is NOT a repaired actual-block lift, full L_RES result, independently reviewed theorem, formal proof or novelty claim"; L5 the f111 withdrawal with "no assessment is transferred"; L17 "says nothing about historical occupied-gap o_F/e_F values, any OLD/IPGEN/DS3 caller, or whether (1) exists in all words"; L43 "does not prove that every original residual has p odd projected runs, distinct odd-run values or an actual block (1) … does not establish any OLD/SEL/IPGEN/GS/DS3 failure, L_RES universal implication, counterexample, or novelty"; L51 "No f111, human, cross-family, formal or novelty claim is transferred". The only "floor" (L31) is the arithmetic floor-half-length. **Confirmed: the candidate makes no actual-block count, o_F/e_F, floor, lift, residual-class or f111 claim.** Its premises are stated on projection data (§1 L11) plus one actual four-letter factor, as the correction requires.

Transfer audit of this review: my verdict rests only on §3 (elementary, self-contained) and §4 (my own code). It does not read, cite or rehabilitate any item in the correction's `affected_candidate_inventory`, the withdrawn f111 disposition, its former 0F review, the "standalone ordered-four lemma", any o_F≥p+2 floor, or any REF/lift statement. Nothing in this review may be cited as support for those. The candidate's L36 comparison with "the earlier equal-rotation criterion" is a reference to held material (the correction's inventory, first entry); the sentence compares statements "as stated" and asserts nothing about that criterion's status, so no transfer occurs, but it should say "held/not adopted" explicitly (MINOR-4). Observation 4.6 is a consistency check that the criterion covers the correction's own explicit word; it infers no actual-block data.

## 7. Findings
No FATAL. No MAJOR. The covering lemma (§3.4) holds for every p (and in any finite abelian group); the construction (§3.5) is correct; the finite controls agree exhaustively at p=3 and on 3615 independent factors at p∈{3,5,7,11,13}.

- **MINOR-1 (terminology).** The candidate calls the four-letter factor an "actual four-block"/"four-letter block" (title, L17, L53) while the binding correction reserves "actual block" for occupied-gap-split constant reflection blocks. Recommend "actual four-letter factor" to prevent a reader from attaching o_F/e_F semantics. No mathematical effect.
- **MINOR-2 (dependency overstatement).** L23 "This uses primality only to make nonzero t generate all F_p" — primality is not used by the lemma (3.4(a)); the operative hypothesis is that the representatives exhaust F_p. Suggest "This uses only that the p distinct labels exhaust F_p; no primality is needed."
- **MINOR-3 (implicit step).** L33 "each chosen equal pair is an identity subproduct in its actual order" is true because pairs are taken inside cut-order run-pieces, none of which is interleaved with another piece; make the run-piece product statement (3.3) explicit.
- **MINOR-4 (held reference wording).** L36 "the earlier equal-rotation criterion" should be labelled explicitly as a held, non-adopted item, consistent with L5.
- **MINOR-5 (author-check breadth, informational).** Author words used 0–1 even runs; the theorem allows arbitrary even runs. Covered here with 0–3 even runs; no change to the mathematics.
- **MINOR-6 (redundant hypothesis wording).** "lie in the SAME ODD projected run": the two σ_c are adjacent in the projection, so "same" is automatic; only oddness is a hypothesis.

Documentary notes (not findings): a `__pycache__/` directory was created in this review directory by the importlib-based cross-check in 4.6; under the no-deletion rule it was left in place and may be removed by the parent. The author result's `input_sha256` and the candidate's producer-output hash agree but the producer file itself was not among my inputs and was not opened.

## 8. Verdict
**PASS — correct at the exact projection-only scope stated in the manifest** (0 FATAL, 0 MAJOR, 6 MINOR, none affecting validity):

> For every odd prime p and every D_{2p} word with exactly F=3p−2 reflections and p+1 rotations whose cyclic reflection-only projection has exactly p odd maximal constant runs with pairwise distinct labels (even runs arbitrary), the presence of an actual cyclic four-letter factor σ_cρ_uσ_cρ_v with its two σ_c in an odd run (u,v∈F_p arbitrary, equal or not, zero allowed) implies an original-order identity product over exactly 2p positions.

Dependencies: none beyond the stated hypothesis and the dihedral relations; the directed-difference lemma is proved here (two proofs). Conditional on nothing external.

**Explicit non-claims of this verdict.** It does not assert: that any residual/REF-failing/L_RES class has p odd projection runs, distinct labels, or such a factor; any actual-block count, o_F/e_F/H value, κ profile, p7/p11 floor, raw-graph or lift statement; any OLD/SEL/IPGEN/GS/DS3 behaviour; any AP characterization of the labels; any status for the "earlier equal-rotation criterion" or any held/withdrawn f111 item; counterexample or non-counterexample status for the original Olson ordered problem beyond the stated class; novelty, priority, or publication readiness. Same-harness review: not human, not independent-model-family, not formal/kernel, not novelty clearance.

## 9. Artifacts written (this directory only)
`review-v1.md` (this file), `reviewer-control-v1.py`, `reviewer-control-results-v1.json`, `reviewer-control-fixtures-v1.json`, `reviewer-control-stdout-v1.txt`, `reviewer-fatal-word-crosscheck-v1.txt`, `reviewer-receipt-v1.json` (post-write hashes and clocks). No other path was written; no input was modified (hashes in §1 are to be re-verified by the parent against the same values).
