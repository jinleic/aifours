# info-5 prerequisite: exact finite-law to actual-word coupling

Owner InfoGuessingRminus-2. Actual native clock immediately before writing: **Tue Oct 27 14:52:17 PDT 2026**.

**AUTHOR-WRITTEN, UNREVIEWED.** Narrow prospective definition-first work only, not original-problem completion, source/book equivalence certification, novelty, computation or a general STOP158 lift. All historical HELD/ZERO consumers remain noninputs.

## 1. Release, actual inputs, exposure and source boundary

- Pre-body ACK: `narrow-prebody-exposure-ack-v1.json`, sha256 `466a28cda7a03ba39d41d0b1faf37db836af8b6d1b4c34d078b9f6b37e83b829`, written after the actual 14:47:08 clock and BEFORE the packet/definitions were opened.
- S1 controls: 19 LF, `03468965e9b86dd2229e78c02d1809c5eb07340221870b243a856f8c9d73dcfd`.
- Release: `c4baca3667b38d215fecacef4b3f580a540d1e4998e32cd9d9d2a7b738e643c8`.
- Complete 35-LF packet: `94cb769fb505c25ec272976de680d8f0331071dc60322c43d7d1ecb340378232`; complete equality receipt `33164e951f041a20b8b588a1bb680d8b1b7ecb2933670961d68db53699fb28df`.
- The 9-LF S2 definitions admit **Baber–Christofides–Dang–Riis–Vaughan, Graph Guessing Games and non-Shannon Information Inequalities, arXiv:1410.8349v2**, limited to the game/guessing definitions, R/R-minus definition and figure, and R-minus bound statements. [Admitted reader](https://arxiv.org/html/1410.8349v2).
- Retained raw HTML pin, live-matched: `3a270e579f080067717d90e25b6e59d29615a543ff30b1abfb9b5e2fae31337d`; pin metadata names v2. The live reader and retained raw bytes are distinct transports; no byte-equality claim between them, PDF, book or a publisher version is made.
- No old proof/review/park/checkpoint/DAG or bibliography source was opened. No Riis 2007 or Christofides–Markstrom source was fetched. Prior authorship and old exposure persist; unaffected cognition or fresh-independent derivation is NOT certified.

### Source-read overshoot disclosure

The initial URL reader request `:1-170` returned introductory examples and the short Lemma 3.1 proof at its boundary in addition to definitions. A subsequent locator grep on the admitted retained HTML (pattern containing R variants and bound strings) displayed adjacent proof fragments and unrelated R-variant statements. Those extra fragments were not followed or recovered from their truncated displays and are not premises below. The locator line was stopped; subsequent source reads were restricted to the specific definition paragraphs, Fig. 1 and Theorem 6.2/bound statements. This is an observable display-scope overshoot, not a clean-access assertion; Main must assess its boundary. No historical held or ZERO body was opened. The proof below uses only the game definitions and the elementary facts it proves/names.

## 2. Literal public definitions and exact object

References use section/paragraph/figure labels from the admitted HTML. Quoted prose is verbatim; mathematical transcription is separately marked.

### 2.1 Observation, alphabet, sampling, strategies

**Section 2, S2.p4:** undirected graphs are treated as digraphs with both directions of every undirected edge. Thus each player sees its undirected neighbours, not an orientation chosen by this packet.

**Section 2, S2.p6:**
> "They may discuss and agree upon a strategy using this information before the game begins, but no communication between players is allowed after the game starts."

The displayed alphabet is `A_s = {0,1,...,s-1}`.

**Section 2, S2.p7:**
> "uniformly and independently at random."
> "do not have access to their own values"
> "each player is given a list of the players in its in-neighbourhood with their corresponding values."
> "If all players guess correctly they will all win, but if just one player guesses incorrectly they will all lose."

**Section 2, S2.p9:**
> "The winning probability of the mixed strategy is the average of the winning probabilities of the pure strategies weighted according to the probabilities that they are chosen."

The paper then restricts to pure strategies; this is justified by the elementary average <= maximum inequality.

**Section 2, S2.p10:** the displayed full-domain strategy is
`f_v : A_s^{|Gamma^-(v)|} -> A_s`.
No domain restriction to a selected support or only frequently seen inputs is part of the physical strategy.

**Section 2, S2.p11:** the displayed definition is
`gn(G,s) = |V(G)| + log_s(max_F P[Win(G,s,F)])`.
We use s >= 2 so the logarithm is defined. For a pure strategy, let W_F be its actual simultaneous fixed-word set. The source's independent uniform sampling implies
`P[Win] = |W_F|/s^{|V|}` and hence `gn(G,s)=log_s(max_F |W_F|)`.
This last equality is a direct definition consequence, not an imported code theorem.

**Section 3, S3.p1:**
> "we will instead concentrate our efforts on evaluating the asymptotic guessing number"
> "define to be the limit"

The displayed limit is `gn(G)=lim_{s->infinity} gn(G,s)`. Lemma 3 below proves the needed limit/supremum relation directly, without using the accidentally displayed source lemma.

### 2.2 R-minus

**Section 6, S6.p1 and Figure 1:**
> "the graph R given in Figure 1, and the graph R^- which is identical to R but with the undirected edge between vertices 9 and 10 removed."

Figure caption:
> "Figure 1: The undirected graph R."

The [admitted figure](https://arxiv.org/html/1410.8349v2/RGraph.png) was actually displayed. Vertices are labelled 1,...,10. The following is a **visual transcription**, not a verbatim adjacency list printed by the paper and not a machine certificate:

- N(1) = {2,3,4,5,6,7}
- N(2) = {1,3,7,9,10}
- N(3) = {1,2,4,8,9}
- N(4) = {1,3,5,8,10}
- N(5) = {1,4,6,9,10}
- N(6) = {1,5,7,8,9}
- N(7) = {1,2,6,8,10}
- N(8) = {3,4,6,7,9,10}
- N(9) = {2,3,5,6,8}
- N(10) = {2,4,5,7,8}

There are 26 undirected edges, 3–4 is present and 9–10 absent. The horizontal line through vertex 5 gives 4–5 and 5–6, not an additional 4–6 edge. All proofs below hold for EVERY finite loopless digraph, so they do not depend on this visual transcription being separately source-certified. Its exact identification is still required for any R-minus-specific inequality.

### 2.3 Bounds and provenance ceiling

Theorem 6.2 prints the Shannon, Zhang–Yeung, DFZ and Ingleton bounds for R-minus. Section 6, equation S6.Ex34, explicitly displays
`20/3 <= gn(R^-) <= 59767/8929`.
Its proofs/computer searches were not audited here. The permitted safe final-status record separately carries the later interval `20/3..1847/276`. This primary-source excerpt does **not** recertify the latter upper endpoint; it is retained as inherited status, not attributed to a theorem that was not read.

No verbatim Chinese-book/source-equivalence claim or worldwide current-status check is made.

## 3. Definitions for the coupling theorem

Let G have a finite vertex set V and the exact in-neighbourhood N(v) at each vertex. Let X=(X_v) be ANY joint law on a finite product of alphabets; zero-probability symbols may be dropped. Write S=supp(X), and use natural-log entropy H.

The original FD condition is
`H(X_v | X_N(v)) = 0` for EVERY v.
For a finite law this is equivalent to the exact support condition:
`x,y in S and x_N(v)=y_N(v) => x_v=y_v`.
Indeed each observed neighbour value of positive probability has a point-mass conditional law iff that condition holds. Empty neighbourhoods are allowed and then X_v is constant.

Set `h=max_v H(X_v)` and `H=H(X_V)`. If h=0, every coordinate and the joint law are deterministic, so H=0. Such laws carry no positive gain and need not be divided by h.

## 4. Lemma 1 — support decoders with all physical inputs

For EVERY nonempty finite S subset [q]^V satisfying the support FDs, there are full-domain decoders on [q] whose winning set contains S. On each neighbour tuple appearing in S, define the unique prescribed output; on every other tuple choose a fixed alphabet element. This is unambiguous by FD consistency, covers the ENTIRE physical domain, and every s in S wins.

Conversely every actual winning set is FD-consistent, because its two words with the same observed neighbour tuple must have the same decoder output.

Containment, not equality of W and S, is what is proved. Extra winning words do not hurt the lower-bound caller. For an upper bound we will use the uniform law on the actual W, not on a support proposed to be a subset of W.

This elementary lemma alone is an encoding, NOT the result of this packet. The following lemma pays the nonuniform-law/alphabet cost that the encoding alone leaves missing.

## 5. Lemma 2 — exact FD-preserving type-class coupling

For ANY finite FD law P with h>0 there is a sequence of genuine common alphabet sizes q_n >= 2 and full-domain original-graph strategies with at least M_n winning words such that

`(log M_n)/n -> H`,
`(log q_n)/n -> h`.

No field, linearity, quasigroup closure, distributional independence of the X_v, or graph-class restriction is assumed.

### 5.1 Rational empirical laws without changing the FD support

Index the d points of S. For every positive integer n choose integer counts k_s >= 0 summing to n so that P_n(s)=k_s/n -> P(s), retaining no point outside S. Such counts exist by rounding the first d-1 counts down and assigning the remainder to the last point; the errors are bounded independently of n. For d=1 the construction is the single constant row. This is an all-n construction, not evaluation of a selected type or numerical probe.

For any subset A of vertices, let k_{A,a}=sum_{s:s_A=a} k_s and let T_A be the sequences of length n over the A-tuples with these exact counts. Put T=T_V. Then

`M_n=|T|=n! / product_s k_s!`,
`Q_{A,n}=|T_A|=n! / product_a k_{A,a}!`,

with 0!=1.

The projection of T onto A is exactly T_A: take any member of T and permute its n positions. The permutation orbit of its A-projection is all of T_A; the same permutation preserves T. The fibres of this projection have equal size by that transitive action. Thus the uniform law on T has UNIFORM projections on every T_A. This statement includes empty A (one empty sequence), zero counts and coincident symbols.

### 5.2 Exact FDs, without a closure-preservation assumption

View an element of T as a tuple of vertex-columns of length n. If two such tuples have identical N(v)-columns, their entries agree on N(v) at each position. Both rows at that position belong to S, so the original support FD makes the v-entries equal. Hence the v-columns agree.

Thus T obeys EVERY original FD exactly, before taking any limit. This is not an assertion that arbitrary independent multiplication, arbitrary set closure or a lossy projection preserves FDs.

For each v, inject the entire marginal type alphabet T_{v} into a common alphabet of size
`q_n=max(2, max_v Q_{v,n})`.
Use these vertex-dependent injections to label the columns. Injectivity retains all observed-column equalities and therefore all FDs. Lemma 1 completes the partial prescriptions to full-domain original decoders on this common alphabet. There are at least M_n winning words.

### 5.3 Elementary factorial estimates and entropy limits

For k>=1, integral comparison for the increasing function log gives
`k log k-k <= log(k!) <= k log k-k+log(k+1)+1`.
The lower bound also follows from the integral from 1 to k; zero counts have zero error under 0 log 0=0. Consequently

`log M_n >= n H(P_n) - d[log(n+1)+1]`.

Also `log M_n <= nH(P_n)`: the probability of that type under iid P_n equals `M_n product_s P_n(s)^{k_s} <= 1`.
Apply the same two inequalities to each marginal type; its number of symbols is fixed and finite. Since t log t is continuous at zero, H(P_n)->H(P), and every marginal entropy converges. The errors divided by n vanish, so

`log M_n/n -> H(P)`,
`log Q_{v,n}/n -> H(P_v)`,
`log q_n/n -> h`.

In particular q_n tends to infinity when h>0. Every decoder system above exists at a finite n; the limit is used only to prove that its cardinality ratio eventually exceeds any strictly smaller threshold.

## 6. Lemma 3 — no missing fixed-alphabet/asymptotic implication

Let K be the actual winning-word count of a strategy on an alphabet of size q>=2. For EVERY larger alphabet size s, take t=floor(log_q s), inject [q]^t into [s] separately at each vertex, and play the original q-strategy componentwise on valid inputs. Arbitrary invalid inputs receive a fixed output. All K^t product words win.

Therefore
`gn(G,s) >= t log K / log s`.
As s tends to infinity, t/log_q s tends to 1, so
`liminf_s gn(G,s) >= log_q K`.
Taking the maximum over strategies at each q and then the supremum over q gives
`liminf_s gn(G,s) >= sup_q gn(G,q)`.
The reverse inequality for limsup follows because every term is <= that supremum. All values lie between 0 and |V|. Thus the limit exists and
`gn(G)=sup_{q>=2} gn(G,q)`.

No source blowup theorem or excluded old construction is a premise of this argument; its only construction is the explicitly proved componentwise strategy on a full alphabet.

## 7. The homogeneous all-law / actual-word criterion

For EVERY finite loopless digraph G and EVERY real c>=0, the following are equivalent:

1. Every strategy at every finite common alphabet q>=2 satisfies `|W| <= q^c`.
2. Every finite joint law satisfying EVERY original neighbour FD satisfies
   `H(X_V) <= c max_v H(X_v)`.

**2=>1.** If W is empty, the count bound is immediate. Otherwise put the uniform law on the actual W. It satisfies all FDs, H(X_V)=log|W| and max_v H(X_v)<=log q. With c>=0 the desired bound follows.

**1=>2.** If h=0, both sides are zero. Otherwise Lemma 2 gives `M_n <= |W_n| <= q_n^c`; divide logs by n and take limits to get H<=ch.

Equivalently, with the deterministic laws omitted from the ratio,
`gn(G)=sup_{finite FD laws, h>0} H(X_V)/max_v H(X_v)`.
The empty-ratio case (a graph admitting only deterministic FD laws) gives zero. The equality also follows directly from the two implications and Lemma 3.

This is not a claim that Shannon-submodular set functions are entropic laws. No unconstructed entropy vector, no marginal entropy-cap relaxation at a FIXED alphabet and no remembered Phi criterion is promoted to an actual strategy.

### Exact original R-minus callers

- **Strict lower:** ANY admissible finite original-R-minus FD law with `H(X_V) > (20/3) max_v H(X_v)` yields, by Lemma 2, a finite common alphabet and actual full-domain decoders with `M_n^3 > q_n^20`, hence `|W_n|^3 > q_n^20`. Conversely any such actual strict-gain W yields that strict entropy inequality on its uniform law, since max marginal entropy <= log q.
- **Strict upper:** an all-finite-original-FD-law inequality H<=ch with a rational c<1847/276 gives the required universal word-count upper bound by 2=>1. Conversely a universal word-count bound at c forces that all-law entropy inequality by 1=>2.

These callers retain the exact original graph and all nonlinear/composite finite alphabets. They are existential conversion criteria, not an exhibited negative law, a code witness or an improved upper bound.

## 8. Finite blocklength sufficient condition (no evaluation or execution)

Let P be rational on d positive support points, denominator D, and let `Delta=H(P)-c h>0`. For EVERY n divisible by D, use its exact type P (no approximation). Then

`log M_n >= nH(P)-d[log(n+1)+1]`,
`Q_{v,n} <= exp(nH(P_v))`.

If `nh >= log 2` and `nDelta > d[log(n+1)+1]`, then q_n<=exp(nh) and `log M_n > c log q_n`. This gives a finite decoder witness strictly above c.

One all-variable sufficient size bound is
`n > (2d/Delta)^2`, `nh >= log 2`, `D divides n`.
Indeed for real x>=1, the derivative of `sqrt(x)-log(x+1)` is `(sqrt(x)-1)^2/[2sqrt(x)(x+1)] >= 0`, and its value at x=1 is positive by integral comparison for log. Hence log(n+1)+1 <= 2sqrt(n). Every sufficiently large multiple of D satisfies the displayed sufficient conditions.

A strict finite-law witness can be made rational first: approximate its probabilities on the SAME FD support. Entropy continuity preserves the strict inequality H-ch>0. This rational approximation preserves FDs because it changes only the probabilities on a fixed FD-consistent support, not the support constraint itself.

No n, P, entropy gap or decoder table is numerically chosen or evaluated here. No claim of an executable witness accompanies the existence proof.

## 9. What this pays, and what remains exactly unpaid

**Paid at author-written scope:** a complete nonuniform-finite-law to exact finite actual-word construction with controlled alphabet cost; every original FD survives exactly. It repairs the genuinely missing implication that marginal entropy normalization, by itself, does not put an arbitrary law directly on a fixed q-symbol alphabet. The proof uses type classes to pay that cost rather than asserting it away. It also supplies the converse uniform-winning-law caller and a finite-blocklength sufficient condition.

**Not paid:** no original R-minus finite law with strict entropy gain is supplied; no universal all-law inequality improving the inherited upper bound is supplied. The inherited interval remains unchanged. The precise old Phi definition/sign-to-gain claim was not provided and remains NR; this packet neither imports nor repairs it. No T300 finite/executable/triple gate, held review verdict or book/primary-source matching gate is discharged.

**Ordinary facts used:** finite support/conditional-entropy equivalence, entropy upper bound by log cardinality, entropy continuity, finite multinomial counting, elementary integral comparison and one-variable limits/calculus. Specialized type projection, exact FD preservation, common-alphabet injection and full-domain completion were proved above. No external research theorem, asymptotic equipartition theorem or scientific computation was imported.

**Next admitted obligation:** use the now-explicit all-law/word caller to identify a genuinely useful unrestricted entropy inequality or a finite strict-gain law, without using any old architecture/field/operator or excluded guide. If no source-separated candidate can be established, report that precise missing entropy inequality rather than restating another proper-class barrier. The source-display overshoot above is separately awaiting Main's assessment.

Same eighteen owners, exclusive new root and deadline `2026-10-31T21:23:27.000Z`. This is not stronger verification or a claim of scientific novelty.
