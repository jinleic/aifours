# Raw b-gap realization and the first cross-layer compatibility obstruction

Observed before creation: **2026-10-23T14:45:48-0700 PDT**. Owner MathShor, math-5. **CANDIDATE written bridge / four-a layer restriction**, not a completion, noncompletion, new n-bound, formal proof or novelty claim. No scientific executable was run or created.

This continues the ONE raw-tail selector obligation. It does not replace the Shor target by an automaton problem and call the encoding solved. The bridge below is exact for finite raw M containing b; its immediate scientific use is an actual compatibility restriction between the forced two-/three-a layers and a complete description of which four-a cores must be supplied. All higher-layer simultaneous compatibility and existence remain open.

## 1. Exact b-padding gap-parse bridge

Let M be a finite set of nonempty words, containing b and no other pure-b word. Each word w containing a has a unique representation

    w=b^(alpha_w) a b^(g_1(w)) a ... b^(g_(k-1)(w)) a b^(beta_w),
    k=|w|_a≥1,

with all exponents nonnegative. Call (g_1(w),…,g_(k-1)(w)) its internal gap list. Distinct raw words remain distinct labelled objects even if some of these lists coincide.

A **free-end parse** of an arbitrary finite list (g_1,…,g_(q-1)) of nonnegative gaps partitions its q a-positions into consecutive nonempty blocks, each labelled by a word w∈M with exactly that block's number of a's. The gaps inside a block must match w's internal gaps exactly. At a boundary between words u and v the actual gap must satisfy

    g≥beta_u+alpha_v.                                   (P)

There is no initial or final delay restriction: arbitrary outside b-padding is permitted. The surplus g-beta_u-alpha_v is the uniquely determined number of intervening b codewords.

**Theorem GP.** M is UD and complete in the book's factor sense if and only if **every finite nonnegative gap list, including the empty list, has exactly one labelled free-end parse**.

### Forward proof

Let D be the maximum raw word length. Completeness embeds b^(2D) U b^(2D) into a product for the a-core U=a b^(g_1)a…b^(g_(q-1))a. Every codeword containing one of these a's lies wholly within the padded factor, because each outside b-margin is longer than a codeword. Its a-positions therefore partition the q displayed positions; all other codewords are b. Reading this product gives a free-end parse, proving existence.

If two distinct parses existed, choose common leading/trailing b-padding at least both first-word alpha delays and both last-word beta delays. Each parse gives a product of raw M-words for that SAME padded word. Internal b surplus is filled by b, and the outside surplus by b as well. Different parses have different sequences of a-containing codewords or different a-block boundaries; their actual M lists are distinct. This contradicts UD. Thus the parse is unique.

### Converse proof

Two raw M-factorizations of a word with a's induce free-end parses of the same internal gap list. Uniqueness makes their a-containing word sequence and boundaries identical. Every remaining b-count at a boundary and the two ends is then determined, so the lists coincide. A word with no a has only its unique list of b's. Hence M is UD.

For completeness, take any binary word. If it contains a, choose the unique free-end parse of its a-core and add enough outside b's to meet the two end delays, retaining the word's original leading/trailing b's inside that padding. The resulting padded word belongs to M*, so the original word is a factor. Pure-b words already lie in M*. This is exactly the book quantifier. QED.

No cancellation of M* or realization of residues is used. The theorem refers to actual raw word delays and every actual gap list.

## 2. The all-order criterion has finite witness certificates, not a bounded test cutoff

For a fixed finite M, let B be at least every internal gap value and every beta_u+alpha_v. Replace a gap g>B by one symbol infinity; keep 0,…,B individually. Every internal equality and boundary test (P) depends only on this finite alphabet

    Gamma={0,…,B,infinity}.

Build a finite labelled automaton whose states are (w,j), 1≤j≤|w|_a. Start states are (w,1), final states (w,|w|_a).

- An internal transition (w,j)→(w,j+1) has the one label g_j(w).
- At the final state of u, a boundary transition to (v,1) is allowed on every gap label satisfying (P); infinity always satisfies the inequality.

Each path is precisely a free-end parse, with no epsilon transition or silent reordering. Thus GP requires exactly one accepting path for every word of Gamma*. This is still an all-order property; checking a finite number of gap lengths without a proof is insufficient.

An exact finite **certificate** is available if a candidate M is actually supplied. Let A_c be the integer transition matrix for each c∈Gamma, I the row indicator of starts and F the column indicator of finals. The acceptance count is I A_(c1)…A_(cl) F. Put

    B_c=diag(A_c,1),       lambda=(I,-1),       nu=(F,1)^T,

where nu denotes the stacked column (F;1). A rational matrix V, vectors z and rational matrices T_c satisfying

    nu=V z,       B_c V=V T_c for every c,       lambda V=0       (Q)

prove that every count is exactly1, by induction on words. Conversely, if every count is1, the rational span of all B_word nu is an invariant subspace annihilated by lambda; it has dimension at most one more than the automaton state count and admits a finite rational basis giving (Q).

This is an optional finite witness language for the raw positive answer, not a produced witness, a new algorithm solving unbounded completion, or authorization to build a runtime framework. It is not necessary to execute it for any argument below.

## 3. Specialization to the forced Shor layers

Use the exact raw conclusions in `proof-RAW-TWO-THREE-A-LAYERS-v1.md` (pin recorded separately):

    A=ba                  (alpha_A=1,beta_A=0),
    W=b^r a^2 b^t         (r,t≥1),
    P=a^3b                (alpha_P=0,beta_P=1),
    U_s=b^(alpha_s) a b^s a^2 b^(beta_s),   1≤s<r,
    V_s=b^(gamma_s) a^2 b^s a b^(delta_s),  1≤s≤t.

These are ALL words with at most three a's, apart from b. In particular

    beta_s≥1;     alpha_1≥1 when r≥2;     gamma_s≥1 for s≥2.

GP gives a second direct view of that earlier core classification: gap0 cannot be parsed as A,A because their boundary threshold is1, forcing W. For two-gap cores (s,0), s≥1, A,W is possible precisely when s≥r; the missing s=1,…,r-1 force the U_s. For (0,s), s≥1, W,A is possible precisely when s≥t+1; the missing s=1,…,t force the V_s. The (0,0) core is P. Positive-positive pairs are already parsed by three A's. This corroborates the core list without relying on a finite parameter sample or a second arithmetic program.

## 4. A genuine cross-layer compatibility inequality

For every 1≤a<r and 1≤c≤t consider the four-a core with gaps

    (a,0,c),  namely a b^a a^2 b^c a.

The following are two distinct possible parses using only already-forced three-a words:

- U_a followed by A, allowed exactly when c≥beta_a+1;
- A followed by V_c, allowed exactly when a≥gamma_c.

If both inequalities held, padding the two ends would give distinct actual factorizations of the same word. Therefore every hypothetical finite completion satisfies

    NOT (beta_a<c AND gamma_c≤a),                       (C4)

or equivalently

    beta_a≥c  OR  gamma_c>a,
    for every 1≤a<r, 1≤c≤t.

This relates independent outer-delay choices from opposite three-a families. It is not implied merely by their raw a-counts, their total lengths, a permissible pure-a order, or the Bernoulli identities. A fourth-a codeword cannot repair a failure of (C4): the two existing lower-layer parses would already violate UD.

The condition is correctly restricted to these ranges; no U_a outside a<r or V_c outside c≤t is introduced.

## 5. Complete forced four-a core table

A four-a core is specified by three actual gaps (g_1,g_2,g_3). A proper parse using only lower layers has a composition of4 from {1,2,3}:

    1+1+1+1,  2+1+1,  1+2+1,  1+1+2,  2+2,  3+1,  1+3.

These seven cases exhaust all proper partitions. Applying their actual boundary thresholds gives the table below. Every variable a,b,c in the table is POSITIVE. Assume the necessary existing constraints including (C4); if any lower-layer parses overlap, M is already impossible.

| Actual gap pattern | A new four-a word with this internal core is forced exactly when |
|---|---|
| (a,b,c) | Never: four A's already parse it. |
| (0,b,c) | 1≤b≤t and 1≤c≤delta_b. |
| (a,0,c) | NONE of: (a≥r and c≥t+1); (1≤a<r and c≥beta_a+1); (1≤c≤t and a≥gamma_c). |
| (a,b,0) | 1≤b<r and 1≤a<alpha_b. |
| (0,0,c) | c=1 and gamma_1≥1. |
| (0,b,0) | 1≤b<r+t, except b<r with alpha_b=0. |
| (a,0,0) | Never: A,P already parse it. |
| (0,0,0) | Never: A,P already parse it. |

For each forced core there is exactly one actual raw M-word with some outer b-delays. No four-a word with any other core may appear, since it would coexist with an existing proper parse and create ambiguity.

### Exhaustive derivation of the table

With no zero gap, four A's work because every boundary threshold is1.

For (0,b,c), a first W followed by two A's works exactly when b≥t+1 (c is already positive). If b≤t, the only remaining possible first triple is V_b, and V_b,A works exactly when c≥delta_b+1. The complement is row2.

For (a,0,c), the only proper possibilities are A,W,A, U_a,A and A,V_c, with exactly the three conditions displayed in row3. The first applies only in the northeast threshold quadrant, and the latter two can overlap only in the rectangle tested by (C4).

For (a,b,0), the last W after two A's works when b≥r. Otherwise A,U_b works exactly when a≥alpha_b. This yields row4.

For (0,0,c), P,A works if c≥2. A,V_c requires gamma_c=0 and c≤t. The known gamma_c≥1 for c≥2 prevents that from overlapping P,A. At c=1 it works precisely when gamma_1=0. Hence the only missing case is row5.

For (0,b,0), W,W works if b≥r+t. A,U_b works if b<r and alpha_b=0. V_b,A cannot work because its last boundary would require 0≥delta_b+1. This yields row6; the two existing possibilities have disjoint b-ranges.

Finally A,P works for every (a,0,0), including a=0, since beta_A+alpha_P=0. This proves the last two rows.

Whenever a table row has no proper parse, GP's universality forces a single four-a codeword with that core. Whenever a proper parse exists, GP's uniqueness forbids such a codeword. Two raw words with the same core are also forbidden by the padding argument. This proves the exact table, not only a list of necessary examples.

The forced set is finite. For example, the (a,0,c) row is contained in

    a≤max(r-1,max_c gamma_c-1),
    c≤max(t,max_a beta_a),

with absent maxima omitted. Its three proper-parse tails exclude everything beyond this rectangle. The other rows have displayed finite ranges.

## 6. Consequence for the sufficient homogeneous n-tail selector

Inside the Bernoulli-tail ansatz alone, every newly forced four-a word must have length n, because the literal Shor C has no four-a word. For each forced triple g its remaining outer delays therefore satisfy

    alpha_g+beta_g=n-4-(g_1+g_2+g_3).                   (T4)

Thus any forced triple whose gap sum exceeds n-4 immediately rejects that particular lower-layer choice. A failure of (C4) rejects it even sooner, independently of all fourth-layer choices. These are actual raw UD/length restrictions, not scalar mass checks.

This is still only a sufficient construction family. Rejecting all its parameters would not prove the unrestricted book question negative; no reduction of arbitrary completions to homogeneous tails has been proved or assumed. Conversely, an actual finite M satisfying GP, or the finite certificate (Q), would already be a full positive witness and would not need a general n-cbc realization theorem.

## 7. Exact remaining obligation and calibration

The single existence-changing obligation remains: construct one finite raw M containing the exact C with UD plus completeness (equivalently a valid raw residual/Kraft certificate, or GP/Q), or prove that **every** such finite raw realization is impossible. The homogeneous-tail selector is a concrete sufficient route only. The low-a layers, crossing test and forced fourth layer constrain it but do not finish it; its infinitely many further gap-list requirements cannot be dismissed by finitely many examples.

The gap criterion is an exact representation/verification bridge, not itself a solution or novelty claim. The new application supplied in this packet is the explicit raw cross-layer inequality and forced four-a table, whose correctness, prior art, significance and parent/peer written acceptance remain separate. All proofs are written, at actual-word and finite-state level. No unattested source theorem, original Szabó proof, cyclic factorization converse, or scientific execution is a premise.
