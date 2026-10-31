# f143 review v1 — alternating degrees n≥14 from Nagura and Jordan (four-index gcd≥9)

**Kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (manifest `manifest-v1.json`, SHA256 `419d36d74be87d0ea1132b669f5fbbe8a58307fae1e1fd218642983618e16fc2`, 4217 bytes, verified at 2026-10-29T03:54:09Z).
**Reviewer:** a same-harness Claude instance (slot assigned by Main). This is NOT human review, NOT an independent model family, NOT Lean/kernel/formal verification, NOT a novelty/priority search.
**Clock receipts (UTC, `/bin/date -u`):** manifest hash 03:54:09Z; input hash/byte/LF verification 03:54:19Z; PDF rasterised 03:54:41Z; final control run 04:09:51Z–04:09:58Z; review write began after 04:10:51Z (observed clock immediately before this write; the file mtime is an upper bound).

## 1. Verdict (scoped)

**PASS at the assigned scope, conditional on two unreplayed public source statements. FATAL 0, MAJOR 0, MINOR 1, INCONCLUSIVE 0.**

Statement reviewed (candidate status line): *for every integer n≥14, among any four proper subgroups of A_n (repetition allowed) some pair of indices has gcd ≥ 9; hence the eight-coset (Sun8) and nine-coset index conclusions hold for A_n, n≥14.*

The written argument is correct as a mathematical proof **given** (i) Nagura 1952, Theorem, case n=5: for real x≥25 there is a prime p with x<p<6x/5; and (ii) Jordan's theorem as restated in Jones arXiv:1209.5169v1 Theorem 1.1: a primitive finite permutation group of degree n containing a cycle of prime length fixing at least three points contains A_n. **Neither source proof was replayed, reconstructed or reviewed here**; only their exact public statements were read (Section 3). Everything else in the candidate (prime supply, Sylow/cycle structure, block argument, orbit/binomial divisibility, gcd collisions, exceptional n=14/16, final count, coset implications) was re-derived by me by hand (Section 4) and the finite arithmetic was re-run by my own code with receipts (Section 5).

The single MINOR is a citation/justification gap, not a mathematical error: the strict **lower** endpoint of the Nagura interval is load-bearing (Section 6), the candidate's endpoint discussion covers only the upper endpoint, and the frozen "exact observed wording" is the informal page-177 sentence ("between x and 6x/5"). The formal Theorem on page 180 of the pinned PDF (visually inspected by me) is strict on both sides, which closes the gap at the source level.

Nonclaims (binding): nothing here is an all-simple-group or global Sun8 result; nothing restores the withdrawn all-degree seven-index assertion (false for A_7 per the mandatory overlays, replayed in control C9); no P7 source-definition equivalence; no n≤13 statement; no adoption, publication, novelty or formal-verification claim; same-harness only.

## 2. Inputs read, in manifest order, with verification

All six declared inputs were hashed/counted before being opened; every SHA256, byte count and LF count matched the manifest (receipt 2026-10-29T03:54:19Z):

| # | file (root `…/parallel-18/sun-coset8/`) | SHA256 (match) | bytes | LF |
|---|---|---|---|---|
| 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf…33d793` ✓ | 6883 | 56 |
| 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149c…018d04` ✓ | 3056 | 11 |
| 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4…748218` ✓ | 3164 | 10 |
| 4 | `frontier-20261028-nagura-primary-source-v1.json` | `91d6e9f2…3cf9e48` ✓ | 2507 | 24 |
| 5 | `frontier-20261028-nagura-1952-public-source.pdf` | `a8396acd…2938f4` ✓ | 291519 | (binary; LF declared null) |
| 6 | `frontier-20261028-alternating-nagura-jordan-v1.md` (candidate) | `521a823b…738d6a` ✓ | 7999 | 71 |

Every text input was read completely (`:raw` full-line ranges). The three mandatory overlays were read before the candidate and their corrections are preserved here:
- Overlay 1 (f116/f81 arithmetic): the corrected `≥` intermediates and `>7` conclusions stand; nothing in the present candidate quotes either corrected comparison.
- Overlay 2 (seven-index FATAL): the unqualified assertion "every A_n excludes seven proper-subgroup indices with pairwise gcd 7" is FALSE — seven copies of A_6 in A_7 have index 7. The small-degree table and dependent small-degree reasoning of the older all-degree candidate are withdrawn. Its n≥14 argument was declared source-conditional and unreviewed; the present candidate is a self-contained rewrite of that n≥14 argument and is what this review assesses.
- Overlay 3 (P7-cardinality): "eight-coset direct-P7 configuration" is withdrawn as a definition; the seven-index assertion and an eight-disjoint-coset assertion are kept separate. I keep them separate (Section 7).

No frozen input was modified. Author code was neither imported nor executed; the only author data parsed by my script is the markdown prime table (after an in-script hash recheck), compared against my own literal transcription.

## 3. Primary-source inspections (statements only; proofs not replayed)

**Nagura PDF.** SHA256 `a8396acdbe057ba920f610ab3a95a1aa0a7f5dd13512b9f9293a4fc0ad2938f4`, 291519 bytes (match). `pdfinfo`: 5 pages, 516×729 pt, producer e.Typist v.11.0, RC4-encrypted (print/copy allowed). Pages rasterised with `pdftoppm -r 150` and read as images.
- **Page 177 (first page), visually read.** Header "No. 4.] … 177"; title "44. On The Interval Containing At Least One Prime Number."; "By Jitsuro NAGURA."; "(Comm. by Z. SUETUNA, M.J.A., April 12, 1952.)". Opening paragraph, observed: "Bertrand-Tschebyschef's theorem (1852) is well-known for the interval between x and 2x where x>1, within which at least one prime number exists; this paper, however, enables us to reduce it up to between x and 6x/5 where x ≧ 25." This matches the frozen `exact_observed_wording` (the frozen text writes ≥ for the typeset ≧). Raster saved as `reviewer-f143-nagura-p177-150dpi.png` (SHA256 `7b7bc026cad6206f455835ae77d3872a7f9fa03438e090ee84c67bb11de088bb`, 150709 bytes).
- **Page 180, visually read (beyond the manifest's minimum, within the named source).** Formal statement: "**Theorem.** There exists at least one prime number p such as: a_n ≤ x < p < (1 + 1/n) x (n = 1, 2, 3, 4, 5; a_n = 2, 8, 9, 24, 25, resp.)". For n=5 this is exactly **25 ≤ x < p < 6x/5**, strict at both ends. Raster saved as `reviewer-f143-nagura-p180-150dpi.png` (SHA256 `e9899f3ac9c091cd4499aaee4fb216bec44a1932268b8c8b5b835ca112e72092`, 153697 bytes).
- Journal/DOI in the frozen metadata (Proc. Japan Acad. 28(4) 177–181, DOI 10.3792/pja/1195570997) are consistent with the page headers ("[Vol. 28," / "No. 4.]"); the DOI itself was not resolved online (not required by scope).

**Jones, arXiv:1209.5169v1** (direct read of `https://arxiv.org/abs/1209.5169` and `https://arxiv.org/html/1209.5169v1`, no web search). Title "Primitive permutation groups containing a cycle", Gareth A. Jones, submitted 24 Sep 2012, journal ref. Bull. Aust. Math. Soc. 89 (2014) 159–165. **Theorem 1.1, verbatim:** "Let G be a primitive permutation group of finite degree n, containing a cycle of prime length fixing at least three points. Then G ≥ A_n." This matches the frozen `jordan_import`. Jones presents it as "the following theorem of Jordan (see [7, Theorem 3.3E] or [22, Theorem 13.9])" — i.e. Dixon–Mortimer and Wielandt — and does **not** prove it in the paper (Section 2 proves only Theorem 1.2, which the candidate does not use). The candidate's "statement read, proof not replayed" is accurate; the proof lives in the cited textbooks and was not replayed by me either.

## 4. Independent reconstruction of the argument (by hand)

Notation: n≥14; r a prime with n/2 < r ≤ n−3 and r>8; t = n−r, so 3 ≤ t < n/2 < r.

**(a) Prime supply.** n=14..49: the 36-entry table (checked, C1). n≥50: m=⌊n/2⌋≥25; Nagura gives a prime r with m<r<6m/5. Then r≥m+1>n/2 for both parities (n even: m=n/2; n odd: m=(n−1)/2), and t = n−r ≥ 2m−r > 2m−6m/5 = 4m/5 ≥ 20, so t≥21≥3; r>m≥25>8; t<n/2<r. Only the named Nagura statement is used. ✓ (bounded numeric consistency in C2.)

**(b) Sylow and cycle structure.** r ≤ n < 2r and r² > n give v_r(n!)=1; r odd so v_r(|A_n|)=1. An element of order r in S_n has cycle type with all parts in {1,r} and, since 2r>n, exactly one r-part: it is an r-cycle, even because r is odd. So a Sylow r-subgroup of A_n is generated by an r-cycle. If r ∤ [A_n:H] then H contains a Sylow r-subgroup, hence an r-cycle c (Sylow). ✓ (C6.)

**(c) Transitive ⇒ primitive ⇒ not proper.** Suppose H transitive with a nontrivial block system of k blocks of size b, kb=n, 1<b<n. Then k ≤ n/2 < r and b ≤ n/2 < r. The permutation induced by c on the k blocks has order dividing r and lies in S_k with k<r, so it is trivial: c fixes every block setwise. The r moved points of c form one ⟨c⟩-orbit, hence lie inside the block of any one of them, of size b<r — contradiction. So transitive H is primitive; c is a prime-length cycle fixing t≥3 points; Jones Thm 1.1 gives H ≥ A_n, contradicting properness. Hence **every r-free proper subgroup is intransitive.** ✓ (C7 confirms b,k<r for all divisors in the table range.)

**(d) Orbit and binomial divisor.** Let O be the H-orbit containing the moved points of c (they lie in one orbit, being one ⟨c⟩-orbit); |O|≥r>n/2, and O is the unique H-orbit of size >n/2. Put u = n−|O|; intransitivity gives u≥1, and u ≤ n−r = t < n/2. H ≤ Stab_{A_n}(O) = Stab_{A_n}(U), U the complement, |U|=u. Since n−u ≥ r ≥ 11 ≥ 2 the S_n-stabiliser S_U×S_{Ū} contains a transposition, so S_n = A_n·Stab_{S_n}(U) and the A_n-orbit of U is all u-subsets: [A_n:Stab_{A_n}(U)] = C(n,u). Therefore **C(n,u) | [A_n:H] with 1≤u≤t.** ✓ (C8: BFS orbit sizes equal C(n,u) at n=14, u≤3 and n=16, u≤5.)

**(e) Collisions at threshold 8 (indices d_1..d_4 of proper subgroups, pairwise gcd ≤ 8 assumed, contradiction sought).**
- Two r-divisible indices have gcd ≥ r ≥ 11 > 8 → at most one r-divisible index.
- Each r-free index d has C(n,u) | d with 1≤u≤t. Same type u twice: gcd ≥ C(n,u) ≥ n ≥ 14 > 8 (this is also what handles repeated subgroups). ✓
- Two types 3≤i<j<n/2: the identity C(n,i)·C(n−i,j−i) = C(n,j)·C(j,i) (verified symbolically: both equal n!/(i!(j−i)!(n−j)!)) gives, with g=gcd(C(n,i),C(n,j)) and A=C(n,i), (A/g) | C(j,i) because A/g and C(n,j)/g are coprime. Hence g ≥ A/C(j,i) = ∏_{h=0}^{i−1}(n−h)/(j−h) ≥ (n/j)^i > 2^i ≥ 8 (each factor ≥ n/j because n≥j; n/j>2 because j<n/2). So g ≥ 9. → at most one r-free index with u≥3. ✓ (C3: exact gcd ≥ 9 for all 14≤n≤400, 3≤i≤j<n/2, minimum 44 at (22,3,7); identity, divisibility and product bound verified exactly for n≤80.)
- Types 1 and 2: gcd(n, n(n−1)/2) = n (n odd) or n/2 (n even): >8 for n≥15 except n=16 (=8); =7 at n=14. → for n≥15, n≠16, at most one r-free index with u∈{1,2}. ✓ (C3.)
- Ordinary degrees (n≥15, n≠16): r-free ≤ 1+1 = 2; plus ≤1 r-divisible: **≤3 indices, so four are impossible.** ✓
- n=14 (r=11, t=3): factors 14, 91, 364; gcd(14,91)=7 (compatible), gcd(14,364)=14, gcd(91,364)=91. Types available {1,2,3}, same type collides, 3 collides with both 1 and 2 → r-free ≤ 2 → total ≤ 3. ✓ (C5.)
- n=16 (r=11, t=5): factors 16,120,560,1820,4368; gcd(16,120)=8 (compatible); gcd(120,·)=40,20,24 for u=3,4,5 so no u≥3 coexists with u=2; two u≥3 collide by (e); hence any three r-free indices would need types {1,2,u≥3}, impossible → r-free ≤ 2 → total ≤ 3. ✓ (C5. Note gcd(16,1820)=4, so u=1 and u=4 *can* coexist — not displayed by the candidate, but its stated logic only needs "no u≥3 with u=2", which holds.) The u≤t restriction is **load-bearing** here: without it, u=6 (C(16,6)=8008, gcd 8 with both 16 and 120) would give a compatible triple {1,2,6}; but C(16,6) is 11-divisible, consistent with u=6 being unreachable for an 11-free index. (C4 info line.)

**(f) Conclusion.** For every n≥14, any four proper subgroups (with repetition) have a pair of indices with gcd ≥ 9. ✓

## 5. Independent controls (receipts)

Script: `reviewer-f143-controls-v1.py` (reviewer-authored, pure Python 3.14.3 stdlib, exact integers/Fractions; no author code imported), SHA256 `ee178a3ccc70c5773caeaf65f5fc714371e196b3e8cbe9f4992cb5fa12da4c72`, 21021 bytes.
Log: `reviewer-f143-controls-v1.log`, SHA256 `125910f316e922bc65c7370abf6c302929f9ec7c6c16598065414c99da56f050`, 7950 bytes. Run 2026-10-29T04:09:51Z → 04:09:58Z, exit 0, **failures: 0**.

| id | control | result |
|---|---|---|
| C0 | candidate re-hashed in-script before its table is parsed | SHA/bytes/LF match |
| C1 | 36-degree table: parsed table == my literal transcription (36 entries, every n in 14..49 once); each r prime by trial division, 2r>n, r>8, t≥3, r>t, v_r(n!)=1; table r ∈ independently computed admissible set | all ok. **Negative:** admissible set {prime r: 2r>n, r>8, n−r≥3} is empty for every n≤13 (why the method starts at 14) |
| C2 | Nagura consistency (bounded, not a proof): every integer m∈[25, 2·10⁶] has a prime in (m,6m/5); derived chain for n∈[50, 4·10⁶] gives 2r>n, t≥21, r>t, r>8, v_r(n!)=1 | ok. **Negative:** m<25 with no prime in (m,6m/5): {1,2,3,4,5,7,8,9,13,14,19,23,24}; largest failure m=24, i.e. a_5=25 is sharp |
| C3 | gcd(C(n,i),C(n,j)) ≥ 9 for all 3≤i≤j<n/2, 14≤n≤400 (min 44 at (22,3,7)); identity/divisibility/product bound exact for n≤80; gcd(n,C(n,2)) formula and >8 iff n∉{14,16}; C(n,u)≥364 for u≥3; C(n,u)≥n≥14 for all u (repeats collide) | ok. **Negative:** i<3 collisions ≤8 exist (358 triples for n≤400), e.g. (14,1,2)=7, (16,1,2)=8, (16,1,4)=4; within u≤t, u=2 never collides ≤8 with any u≥3 |
| C4 | max pairwise-compatible u-type set at threshold 8, restricted to u≤t (table r for n≤49; smallest prime >n/2 for 50≤n≤160) | ≤2 for all n; n=14 and n=16 give exactly 2 (e.g. {1,2}). **Negative:** n=7 gives 3 ({1,2,3}: 7,21,35); n=16 without u≤t gives 3 ({1,2,6}) |
| C5 | n=14 and n=16 full gcd matrices | all displayed values confirmed (7;14;91 and 8;40,20,24) |
| C6 | partition enumeration n=14..49: every cycle type of order divisible by r has exactly one r-part; order exactly r ⇔ (r,1^{n−r}); r odd | ok |
| C7 | all nontrivial block sizes/counts satisfy b,k ≤ n/2 < r, n=14..49 | ok |
| C8 | BFS orbit of a u-set under A_n generators has size C(n,u): n=14, u≤3; n=16, u≤5 | ok |
| C9 | **small-n countercontrol, actual groups:** A_7 enumerated (2520 even permutations); four distinct proper subgroups Stab(pt) (order 360), GL(3,2) on the 7 nonzero vectors of F₂³ (order 168, built from invertible matrices, verified ⊂A_7), Stab(2-set) (120), Stab(3-set) (72): indices 7,15,21,35, pairwise gcds {1,7,7,3,5,7}, all ≤7<9 — the four-index statement **fails at n=7**, outside the candidate's scope. Overlay A7 counterexample replayed: the seven sets {g∈A_7: g(i)=1} are left cosets g_i·Stab(i) of index-7 subgroups, pairwise disjoint, partitioning A_7 | ok (same-harness replay; this is not the separately assigned disjoint review of that overlay) |
| C10 | 22 genuine A_14 subgroup indices (set stabilisers, pointwise stabilisers, two wreath products, 11-cycle normaliser, trivial): no 4-subset has all pairwise gcd ≤ 8 (worst max-gcd 91); each index is 11-divisible or a multiple of 14, 91 or 364 | ok (sanity only; the lattice of A_14 is not enumerable here) |

Process disclosure: two earlier runs of my script were killed by me (04:05:49Z run: an over-heavy Fraction loop; 04:07:14Z run: an exponential clique search that also exposed two of **my own** over-broad expectations — "u=2 never collides ≤8 with u≥3" and "max clique ≤2 over u≤(n−1)/2" — both false only at n=16 via u=6>t). Those were reviewer-expectation errors, not candidate errors; the corrected script restricts to the candidate's actual range u≤t and reports the over-broad case as information. Only the final run (exit 0) is the receipt.

## 6. Findings

**MINOR-1 (citation/justification of the strict lower endpoint).** Section 2 of the candidate uses r ≥ m+1 (i.e. r>m strictly) to obtain r>n/2; this is load-bearing (if m is prime and the lower endpoint were inclusive, r=m=n/2 for even n would be allowed, n=2r, and the whole Sylow/cycle argument changes). The candidate's endpoint remark ("if 'between' were taken to allow an upper endpoint, an integral 6x/5 is a multiple of 6 …") is correct — for integer x with 5|x, 6x/5 = 6·(x/5) ≥ 30 is composite — but it addresses only the **upper** endpoint, and the frozen metadata's `exact_observed_wording` is the informal page-177 sentence whose "between" does not by itself fix the lower endpoint. The gap is closed by the source: the formal Theorem on page 180 reads a_n ≤ x < p < (1+1/n)x, strict at both ends (Section 3). Even under an inclusive reading a trivial repair exists (reapply the statement at x=m+1≥26, giving t > 2m−6(m+1)/5 = (4m−6)/5 ≥ 18.8). Recommended for any successor: cite the page-180 Theorem (n=5, a_5=25) as the imported statement and location, and state explicitly that the lower endpoint is used strictly. No mathematical change to the result.

**Notes (not findings).**
- N1. Jones Thm 1.1 is a restatement of Jordan's theorem with its proof referred to Dixon–Mortimer Thm 3.3E / Wielandt Thm 13.9; the candidate's "proof not replayed" should be read as "proof not in the cited paper either". The import remains conditional.
- N2. At n=16 the candidate's displayed gcds are correct; gcd(16,1820)=4 is an additional compatible pair (u=1,u=4) it does not display. Its logic ("no u≥3 coexists with both u=1 and u=2") is complete without it.
- N3. The threshold 14 is where the method first has a prime r>8 with n/2<r≤n−3 (C1); the candidate does not claim sharpness and I make no statement about n≤13 (C9 shows failure at n=7; n=13 is not a counterexample by a prime-degree argument I did not pursue beyond a sketch, and it is out of scope).
- N4. The author's "checked-in-kernel" statements are not independent evidence and were disregarded; all arithmetic here is from my own code.

## 7. Exact implications (precisely stated)

Let T(n) be the proved four-index statement. For pairwise disjoint left cosets a_1H_1,…,a_kH_k of A_n with k≥2, every H_i is proper (a coset of A_n itself meets every coset). Hence for n≥14:
- k=8 (Sun8): any four of H_1..H_8 contain a pair with gcd of indices ≥ 9 ≥ 8. ✓ Implied by T(n); disjointness is used only for properness.
- k=9: same pair has gcd ≥ 9. ✓
- More generally Sun's inequality gcd([G:H_i],[G:H_j]) ≥ k holds in A_n, n≥14, for every 4 ≤ k ≤ 9. Nothing is implied for k≥10 (would need gcd ≥ 10), for k=2,3, for n≤13, for other simple groups, or for any separately defined "direct P7" notion; T(n) does exclude any seven proper-subgroup indices with all pairwise gcd exactly 7 in degrees n≥14, consistent with overlay 3's retained-scope sentence, while the A_7 seven-index counterexample of overlays 2–3 stands untouched (C9).
- Repeated subgroups: T(n) is stated and proved "with repetition" (same-type collision gives gcd ≥ C(n,u) ≥ n ≥ 14; two r-divisible indices give gcd ≥ r ≥ 11), so no distinctness hypothesis is needed for the coset implications.

## 8. Dependencies, scope and artifacts

Dependencies for the PASS: (D1) Nagura 1952 Theorem, n=5 (statement read on the pinned PDF; proof unreplayed); (D2) Jordan/Jones Thm 1.1 (statement read at arXiv; proof unreplayed, located in Dixon–Mortimer/Wielandt). Everything else is self-contained and was re-derived here. Scope is exactly n≥14, A_n, four proper subgroup indices, threshold 9, and the k=4..9 coset consequences; no global Sun8, all-simple, P7-equivalence, novelty, adoption, human or formal-verification claim.

Artifacts written (review directory only; frozen inputs untouched; no Git operations):
- `review-v1.md` (this file; hash reported in the hand-off message, not inside the file)
- `reviewer-f143-controls-v1.py` — SHA256 `ee178a3ccc70c5773caeaf65f5fc714371e196b3e8cbe9f4992cb5fa12da4c72`, 21021 B
- `reviewer-f143-controls-v1.log` — SHA256 `125910f316e922bc65c7370abf6c302929f9ec7c6c16598065414c99da56f050`, 7950 B
- `reviewer-f143-nagura-p177-150dpi.png` — SHA256 `7b7bc026cad6206f455835ae77d3872a7f9fa03438e090ee84c67bb11de088bb`, 150709 B
- `reviewer-f143-nagura-p180-150dpi.png` — SHA256 `e9899f3ac9c091cd4499aaee4fb216bec44a1932268b8c8b5b835ca112e72092`, 153697 B
