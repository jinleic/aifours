# f9 — ordered Olson dihedral prefix potentials and mixed-prime bridge

Reviewer **MathShor-2 / math-5**, disjoint scientific review for author **MathOlson-2-2 / math-2**.
Native `/bin/date` observed before writing: **Wed Oct 28 17:18:32 PDT 2026**.

## 1. Exact verdict, sources and review level

**NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE: 0 FATAL / 0 MAJOR / 0 MINOR.** Both candidate proofs, all claimed directions/boundaries, the support-only sharpness construction, the original-order mixed-prime caller and the actual three-reflection exchange counterfamily are reconstructed below. These are **not** an all-dihedral or all-finite-group proof, original avoiding word, novelty clearance, formal/kernel proof, human review or configured-independent-model acceptance.

| Candidate | Complete source / native SHA256 | Decision |
|---|---|---|
| A: `frontier-20261028-dihedral-prefix-potential-selector-v1.md` |153 LF /10762 B; `efcd3a5cc20e9be07e8a6740acdf32dc89fee753e88a9c1ca93aee25c7ac9d11` | Actual fixed-I chronological identity, both sufficient conditions, support-only sharpness and all-prime alternating example supported |
| B: `frontier-20261028-mixed-prime-ordered-bridge-v1.md` |243 LF /20580 B; `fd6114b218efd2ea89ddf02e01d19a9063f4f20ba31865b4676f75519d70aff4` | Collision iff/counterfamily, exact sharp elementary-kernel threshold, prime-quotient and mixed-prime bridge, and conditional greedy word class supported |

The f9 assignment was read FIRST; both candidate files were read ENTIRELY through their endings. Native source hashes matched dispatch. The registered `mathematics/olson-ordered-egz/source/problem.zh.txt` was also read: the requested selector has exactly |G| DISTINCT indices in increasing ORIGINAL order within an actual word of length2|G|−1. The partial-group-class results below retain that distinction.
The earlier w42 parent disposition `math-2-short-kernel-mixed-prime-transport-parent-v1.md` was read completely; native SHA256 **c7ee97b515bb0898f8f386cef300ff4ce23bf64e47e0ea0c663dd37a8948e3a5** matches B. Its generic actual-packet transport is prior same-harness written support; B's explicit elementary-kernel specialization is reconstructed independently here, not claimed to be a novel generic lemma.
I have bounded earlier Olson/privacy/review contacts; this is not a blind or lifetime noninfluence certification. No author contact, nested agent, external-model/API call, secret, deletion, Git push, publication or infrastructure mutation. The historical process records remain historical, not retroactively converted to mathematical acceptance.

## 2. A — exact original-order two-reflection formula

Let p be ANY odd prime, and write rotations/reflections as `(x,0)=r^x`, `(y,1)=r^y s`, with product `(x,e)(y,f)=(x+(-1)^e y,e+f mod2)`. An actual word has `2p−2<=R<=3p−2` rotations, total length4p−1 and at least p+1 reflections. Fix ANY actual set I of 2p−2 distinct rotation positions; unchosen rotations do not contribute. Put `S=sum_I x_a` and for each reflection position i put `z_i=y_i+2 sum_(a in I,a<i)x_a`.

For arbitrary distinct reflection positions i<j, call A,B,C the sums of the SELECTED rotations before i, strictly between i,j, and after j. The actual chronological product is

    r^A (r^yi s) r^B (r^yj s) r^C
      = r^(A+yi−B−yj+C)
      = r^(S+zi−zj).

Thus the selected 2p original indices have product1 **iff** `z_j−z_i=S`. This is an exact iff, not merely a necessary sum; it covers zero x, repeated reflections, empty segments and every rotation-set placement. The original word order is not changed.

If S=0, p+1 actual reflection occurrences and p residues give an ordered equal-potential pair by pigeonhole. If S!=0 and the potential support is all F_p, the map `v->v+S` is one directed p-cycle. Failure of every desired ordered pair would place every occurrence at v+S strictly before every occurrence at v, for every v. Since every vertex occurs, cycling these strict precedence relations is impossible. Therefore the stated two conditions each give an actual exact-2p selector. Full support is sufficient, not necessary; nothing establishes that one of these conditions holds for every word or every I.

## 3. A — support-only sharpness and actual family

Fix ANY nonzero delta and ANY nonempty proper T subset F_p. Removing at least one vertex from the directed delta-cycle leaves a disjoint union of directed paths (isolated vertices included). List its vertices in reverse topological order, grouping any chosen positive multiplicities of each vertex. Then no earlier v is followed by v+delta, although the support is exactly T. Repetitions can make F at least p+1 and fit an original count-band word.

This is realizable by actual group letters and an actual fixed I: choose any 2p−2 rotation exponents summing to delta and place them in any prescribed selected-rotation positions. For each reflection use the ACTUAL selected-rotation prefix P_i and set `y_i=z_i−2P_i`; any unselected rotations are irrelevant to I. Thus every nonempty proper support can fail the exact oriented-pair criterion, even size p−1. This proves the advertised **support-only guarantee is sharp for this fixed-I/two-reflection method**. It does not assert absence of another I or an original selector.

The all-prime alternating construction also checks out: F=2p,R=2p−1, selected first2p−2 rotations all exponent1, so S=−2!=0; with reflected exponents as supplied, z_j=j mod p. Positions j=0 and j=p−2 have the required oriented difference. Counts, alternating endpoints and the exact2p selector work for every odd p, including p=3. This is one uniformly specified word family, not all alternating words.

## 4. B — direct three-reflection exchange counterfamily

For the actual semidirect product `F_p^d ⋊_(−1) C_2`, ordered reflection pairs from distinct v,w,u yield `(v−w,0),(v−u,0),(w−u,0)`. The first can equal the middle only if w=u; the middle equals the last only if v=w. The remaining equality is exactly `v+u=2w`. Under distinctness, this is the ONLY possible collision, and gives exactly two distinct pair products.

For every odd p,d>=1, any x and nonzero a give distinct v=x,w=x+a,u=x+2a, hence the equality and two actual different pair products. Appending identity occurrences to reach the registered length preserves that local counterexample and supplies a separate easy original selector; it is **not** an original avoiding word. It refutes only the proposed local assertion that three distinct reflection values must give three distinct ordered pair-products.

## 5. B — complete elementary-kernel short-selector proof and sharpness

Let p be ANY prime, d>=1, `m=p^d`, `D=d(p−1)`, and an arbitrary actual V=F_p^d word have length L=m+D. First, for polynomials f_j in L field variables with total degree sum<L, the common-zero count is divisible by p: `prod_j(1−f_j^(p−1))` is its field-valued indicator and has total degree<L(p−1). In every monomial at least one variable has exponent <p−1; summing that variable over F_p gives0, including exponent0 and p=2. Therefore the whole indicator sum is0 mod p.

Set `z_i=t_i^(p−1)` and impose the d elementary-symmetric equations `sigma_(p^j)(z)=0` for j=0,...,d−1 plus d vector-coordinate equations `sum_i (x_i)_r z_i=0`. For a support of size w, the symmetric coefficient is `binom(w,p^j) mod p`, the j-th base-p digit of w by `(1+T)^w=prod_j(1+T^(p^j))^(w_j)`. Thus the first equations force m|w. Since `(1+(p−1))^d>=1+d(p−1)`, D<=m−1 and `L<=2m−1`, so w is0 or EXACTLY m. The vector equations say that SAME actual support sums to zero.

After substituting z_i, the sum of equation degrees is at most `(m−1)+D=L−1`. The empty support contributes exactly one field assignment. Each actual zero-sum m-subset contributes `(p−1)^m` nonzero-coordinate assignments. Therefore

    0 == 1+A(p−1)^m == 1−A (mod p).

For odd p, m is odd; for p=2, 1=−1 in the field. Thus A==1 mod p and is positive. This pays BOTH field-to-actual-support and actual-support-to-field directions, including repeated vector values and the characteristic-two boundary.

Sharpness is an actual full family: `m−1` zero occurrences followed by p−1 occurrences of each standard basis vector. A zero-sum subset must use each basis vector a multiple of p times; only0 is possible because fewer than p are present. Only m−1 zero positions remain, so no exact-m selector exists at length m+D−1. This proves the claimed one-position-shortening failure, not a nonabelian avoidance theorem.

## 6. B — ordered quotient transport, arithmetic and word-dependent branch

For prime q, the cyclic EGZ result is also paid by the displayed polynomial argument: in a word of length2q−1 impose `sum z_i=0` and `sum a_i z_i=0`. Degree sum2(q−1)<2q−1, and the first equation restricts support to0 or q. The same zero-count/assignment calculation gives a q-element zero-sum set. The quotient is abelian, so retaining those positions in increasing order is legal; q=2 is included.

For ANY G with normal K≅C_p^d, quotient C_q, m=p^d and `(2q−1)D<=m−1`, the chunk budget is exactly

    (m+D)(2q−1) <= 2qm−1 = 2|G|−1.

Partition an arbitrary ORIGINAL word's initial required segment into m+D consecutive chunks. In each, choose q ACTUAL increasing positions with quotient product1. Each resulting product lies in the SAME normal K. Lemma §5 selects exactly m of these kernel products whose product is identity. Their chunks are chronologically separated, so their union is exactly mq=|G| distinct original indices, and the original-order G-product is the kernel product. No crossing/interleaving reordering, extension splitting, action assumption, semidirect presentation or group-exponent shortcut is used. The statement is only the displayed sufficient condition; its failure is not a counterexample.

For d=2, cancellation of p−1>0 gives `p>=4q−3`. The q=2,p>=5 class, including equality at p=5, is correctly included. In the named inversion-action semidirect family, `[V,C_2]=V` because2 is invertible for odd p, so the lower central series cannot reach1: this supports its nonnilpotent illustration. No independent nonsplit example or novelty assertion is inferred.
The coarser rank condition is also sufficient: binomial expansion gives

    p^d−1 >= d(p−1)+binom(d,2)(p−1)^2,

and `(d−1)(p−1)>=4(q−1)` makes the second term at least `2d(q−1)(p−1)`, yielding the exact bridge inequality. It is not asserted necessary.

For an arbitrary index-two extension and an ACTUAL quotient word, the proposed greedy blocks are disjoint chronological blocks of length2 or3, each containing an actual equal-symbol quotient pair. If a,b count the two block sizes, t=a+b and tail r, then `4k−1=2a+3b+r=3t−a+r`; hence `t>=k+D` iff `a>=3D−k+1+r`. Under Short(K,D), choosing k packet products preserves chronological G-order. The alternating quotient type has every same-symbol pair spanning at least3 positions, and the successive first/third picks attain floor((4k−1)/3) disjoint separated pairs. This shows the stated separated-packet limitation, not failure of arbitrary selectors or all dihedral words.

## 7. Independent exact checks, replay and actual boundaries

New reviewer-owned standalone checker `frontier-review-f9-olson-check.py`, SHA256 **c98ae945b2a122d79deb99edc7995c5b63d50c32e2a3b7684f5ac94f6cb686c5**,199 LF /8512 B, imports NO author program/data. Actual execution:

    python3 -B frontier-review-f9-olson-check.py

Observed output, exact integer arithmetic:

- For p=3, **459270** original-length words with four arbitrarily chosen rotations, four reflections and three unchosen identity rotations, spanning ALL 8-position interleavings and ALL chosen-rotation/potential assignments; **2755620** actual reflection-pair group products matched the formula, and all **289170** sufficient-condition words had a selector. This is one bounded count band, not all p/words.
- For p=3,5,7, **888** nonempty proper-support/nonzero-delta cases passed the explicit reverse-cycle ordering construction with enough reflection occurrences. It tests the sharpness construction, not global avoiding words.
- Independently enumerated ALL elementary-kernel words at `(p,d)=(2,1),(2,2),(3,1)`: respectively **8,4096,243** words, each satisfying the selector-count congruence. The p=3,d=2 sharpness word's **220** size-9 subsets had zero zero-sum selectors; this is a finite check in addition to the written all-p proof.
- Direct ordered reflection products reproduced **504/72** and **13800/600** distinct-triple/collision counts for `(p,d)=(3,2),(5,2)`.
- A separate seed2026102803 generated **24** actual group-order50, original-length99 words under three involution actions. Chronological quotient chunks plus an independently implemented exact kernel subset-sum dynamic program supplied and directly multiplied 50-index selectors for every word. All **48** duplicate/out-of-range index controls were rejected. These inputs are not the author's corpus or a proof for arbitrary groups.

I also separately re-ran the AUTHORS' read-only checkers against their saved, natively hash-matched result files; this is receipt replay, NOT the independent checker above. The dihedral checker returned `PASS_BOUNDED_REPLAY_AND_DIRECT_PRODUCTS`, 1440 random words /60480 reflection pairs /700 promised /718 additional /18 representatives /3 alternating instances, with all three named mutations rejected. The mixed-prime checker returned `PASS_BOUNDED_CHECKS`,30 actual group cases /2 triple domains /220 kernel subsets, with its four named mutation controls rejected. Their saved-input hashes matched the candidates. No checked finite sample is promoted to the universal proof.

## 8. Prior-source and remaining target limits

I read the cited public [Qu preprint, arXiv:2610.26122v1](https://arxiv.org/html/2610.26122v1): its abstract/introduction define product-one sequences by allowing a reordering; its Lemma2.2(i) states the abelian threshold `E(C_p^d)=p^d+d(p−1)`. In the abelian kernel, reordering does not change the sum, so it is reasonable PRIOR context for §5. The preprint's nonabelian bound is NOT an original-order theorem and is not imported into §6. This source check does not establish whole-literature priority, peer acceptance, current openness or novelty.

Both results remain proper/conditional scopes: B's mixed-prime sufficient class is a consequence of the already-supported general transport plus reconstructed elementary inputs; A's support sharpness is only for fixed I and two reflections. Neither pays the remaining all-word dihedral residual, arbitrary finite groups, all-mixed-prime extensions when the budget fails, or the original ordered conjecture. No historical HELD outcome becomes a premise merely from this review. Author programs, my finite checker and this written reasoning are not formal proof or an independent-model-family/human referee.

**FINAL: 0 FATAL / 0 MAJOR / 0 MINOR at exact candidate scopes.**

**END OF COMPLETE f9 SCIENTIFIC REVIEW.**
