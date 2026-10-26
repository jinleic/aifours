# v30-D — written reconstruction of heterogeneous pure runs, one gap and endpoint escape

Reviewer InfoBalancedNL242-2, info-6; author MathShor. Actual clock before this return: `Sun Oct 25 04:26:22 PDT 2026`.

## 1. Binding, exposure and verdict

Assignment: `peer-review-wave-eighteen-v30.json`, v30-D, SHA-256 `99da25ec26aa7b7f35050105d206016ccd68dd6eb14b2cabb0b2f1b54d671154`. Literal packet SHA-256 `a8d6e6234b4983815d7194bfc3177237b9b380861bb1a91233a73264319ef051`; its provenance receipt reports source pins and literal rendering equality. Reviewer independently observed all three source hashes using metadata-only shasum.

Notation for source references:

- **A:** `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-v1.md`, SHA-256 `38328e19b46a88f524b7af2b51654b9d6bf8e7dcf62cba1bdfdd5ce2350cba7f`, LF1–433.
- **B:** `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-ADDENDUM-1-WRITTEN-ROOTS.md`, SHA-256 `ae9567bb6363eafbcbaaaf78346cc6f03ce9117a157266354e7c8185adc515f0`, LF1–169.
- **C:** `parent-HOLD-correction-disclosure-v1.json`, SHA-256 `85521395b7ad128b9b4d6340ae2d13496423f9491f23d26fa406d9150349214c`, LF1–29.

Coverage: read every line of all three sources through the650-line literal packet. Long source/disclosure lines were additionally read raw, including A7,176,219,290,352,354,419,421,431,433; B5,43,51,91,156,167,169; C5–7,13–28. Exposure ACK is `peer-review-shor-heterogeneous-written-roots-ack-v1.json`. This is reciprocal, same-harness, supplied-proof cross-domain review: MathShor is concurrently reviewing my NL242 packet. It is not blind, independent-model, human, formal or novelty review.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the written scopes reconstructed below, conditional on the explicitly retained GP interface and classical cyclotomic facts.** No full Shor-completion result is accepted. No finite computational-certificate credit is given. B and C are mandatory overlays, not optional supplements.

Only written reasoning and metadata clocks/hashes/source reads were used in this review. No scientific eval/interpreter, enumeration program, symbolic calculation program, certificate replay, solver or GO occurred.

## 2. Pure-run theorem and lifted deficits — RECONSTRUCTED

### 2.1 Parsing and PR

A38–80 correctly distinguishes actual word labels/delays from endpoint exponents. A zero internal b-gap permits a join only when both touching delays are zero. Therefore a parse containing several a-containing words must be an optional positive-leading start, then powers of the unique pure word a^n, then an optional positive-trailing end. An isolated word cannot join another a-containing word at gap zero. The empty run contributes once through the two empty endpoints. This gives precisely

    LR/(1-z^n)+H=1/(1-z),

and hence PR: `LR+(1-z^n)H=S_n`.

The uniqueness of the pure power follows directly from UD: two distinct powers of a have a common multiple and give two different codeword lists. Existence and the free-end parsing interface use the named accepted GP theorem (A23), not a new residue-to-raw-code realization converse. Different words of a fixed type and a-length already give two singleton free-end parses, so their delays cannot create duplicate endpoint terms.

**Scope:** PR is iff for this pure-run subsystem, not global UD/completeness of arbitrary added crossing words. Actual positive leading/trailing delays remain attached to each word; they do not affect a zero-gap join but are retained in the later profiles.

### 2.2 Cyclic factorization and LIFT

A84–112 is valid over the cyclic quotient. Coefficient nonnegativity makes each residue coefficient of LR exactly1. Hence each residue has one actual exponent pair, neither endpoint set repeats a residue, and the product of endpoint cardinalities is n. Because both contain0, residue0 has actual representative0 and no other, so h_0=0.

For residue k represented by actual sum k+nh_k,

    (z^k-z^(k+nh_k))/(1-z^n)
      =z^k+z^(k+n)+...+z^(k+n(h_k-1)).

Different residues do not overlap. This proves the unique H in LIFT, with coefficients0/1 and no constant term. Conversely substitution proves PR for any such actual endpoint sets and their forced H. Assigning arbitrary positive delays does not change the pure-run count; it does not establish any positive-gap equation. No cutoff or assumption that endpoint representatives are below n enters this reconstruction.

## 3. One-positive-gap identity with heterogeneous delays — RECONSTRUCTED

For A116–139, ending with delay0 means no end or isolated word, so the nonempty series is L/Delta−1. A positive final delay d arises either from an actual end of delay d after the L/Delta prefix, or from one isolated word with that final delay. These are disjoint. The initial-delay formulas are the exact reversed statement. Summing over the delay index recovers the nonempty pure-run series z/(1-z) by PR.

For a core a^p b^g a^q with p,q>0:

- Without a crossing word, a left parse of final delay d and a right parse of initial delay e can join exactly when d+e<=g. The leftover b words are forced, so there is no additional multiplicity. This is NB.
- At most one a-containing word can cross the single positive gap. Its internal gap must equal g; words with more internal positive gaps cannot fit this core.
- If its leading delay is positive, a nonempty left prefix cannot join it at a zero a-gap, so that prefix must be empty. If its leading delay is0, the left choice is empty or a pure-run parse of final delay0, giving L/Delta. The trailing statement gives R/Delta or the empty suffix.

These four cases give, before clearing denominators,

    target−NB = (L/Delta_z)(R/Delta_w) B_00
               +(L/Delta_z) B_0+
               +(R/Delta_w) B_+0+B_++.

Multiplication by the two invertible formal series denominators gives exactly HG_g in A166–173, with the target numerator zS_n(z)wS_n(w). Labels in the B-polynomials are counted with their actual positive/zero external-delay classes, not merged across raw words. Thus coefficient comparison is iff for this fixed one-gap subsystem, with arbitrary endpoint delays retained.

The finiteness statement at A178 is also correct: once g permits every pure-run boundary pair, NB already equals the target. Every nonnegative crossing contribution then must be zero. This does not prove consistency among several gaps.

## 4. K0 is genuinely UD but fails multi-gap completeness — RECONSTRUCTED

A184–219 can be checked without importing the full M0 certificate. For

    K0={aa,b,abb,aaaba,baba},

the only proper codeword-prefix relations are aa<aaaba and b<baba; both leave the residual `aba`. That residual is neither a prefix of a K0 word nor has a K0 word as its prefix. The Sardinas–Patterson residual process therefore terminates without an empty residual. This is a direct written UD proof. Kraft is

    1/4+1/2+1/8+1/32+1/16=31/32.

More importantly, the explicit missing core supplies factor-incompleteness independently of a general Kraft equivalence.

The pure data n=2,L=1,R=1+z,H=0 give PR. Their boundary profiles are F_0=z²/Delta, F_2=z/Delta, G_0=(z+z²)/Delta, with no positive initial delay. At g=1, NB's numerator is z²(w+w²); the defect after subtraction is zw(1+w). The bridges aaaba and baba contribute respectively

    (1+w)z³w,
    (1-z²)(1+w)zw,

whose sum is zw(1+w). At every g>=2 all boundary pairs are permitted and no one-gap crossing word is present.

For `a b² a b a`, neither aa nor aaaba fits because there are no adjacent a's. Three singleton abb parses fail at the last gap1. A baba crossing cannot span the first gap2. If it spans the last gap1, joining it to the first abb requires the previous gap to be at least2+1=3, whereas it is2. No other a-containing word exists. Thus the core has no free-end parse. Via GP this establishes incompleteness and proves the claimed failure of any inference from all PR/HG equations to multi-gap coherence.

This is a **non-Shor control**, not a proposed Shor extension. The full M0 completeness proof was not needed or reconstructed here.

## 5. Literal endpoint exclusions and R4 obstruction — RECONSTRUCTED

A232–251 lists actual residual pairs in the sixteen seed words. In particular the perhaps less immediate residual12 is `ba` versus `ba^13`; the residuals2,4,6 use `a^3b`. For i in {0,3,8,11}, a^i b is also an actual seed word. Thus

    (p_s a^s)(a^i b)b^(beta−1)=p_s(a^(i+s)b^beta)

holds as a raw word for every beta>=1. Its two codeword lists differ in their first word. It is a UD contradiction, not a residue collision.

The explicit decompositions at B142–145 cover every listed excluded positive exponent through25. The only survivors are3,8,11,19, plus the empty endpoint0. The seed fixes the first three and GP forbids a second delayed end at the same a-length. Hence the capped-support endpoint polynomial is exactly R4 or R5, as asserted at A259–272. No restriction has been imposed on other codeword types or their lengths.

For R4=(1+z³)(1+z⁸),

    (1+z³)(1−z³+z⁶)=1+z⁹,

which proves DUAL immediately. In any cyclic quotient multiplication of S_n by a polynomial of value1 at1 preserves S_n. Thus the displayed four-term nonnegative indicator sum must equal1. At residue22 it contains u_14 and u_13, both forced by seed starts ba^14 and ba^13. It is at least2, even if some residue indices coincide and are counted with multiplicity. This excludes R4 for every n, not merely a bounded order.

## 6. Direct cyclotomic proof for R5 — RECONSTRUCTED

The36-remainder table in A315–350 was **not** reconstructed or replayed. It is unnecessary once B is included.

### 6.1 Minimal relation: conductor reduction

For B37–43, if p² divides m, the cyclotomic degree ratio over K=Q(zeta^p) is p. Grouping indexed terms by exponent modulo p in its degree-p basis makes each occupied group's coefficient zero. Minimality forces one occupied class; exponent0 makes it class0, contradicting the simultaneous exponents3 and8. This excludes every square prime divisor, including p=2.

For squarefree m and p>=7 dividing m, the coprime cyclotomic degree over Q(zeta_(m/p)) is p−1. Grouping the five terms by their primitive-p factor produces a polynomial of degree at most p−1, divisible by 1+x+...+x^(p−1). An empty coefficient exists because five terms cannot occupy p>=7 groups. Therefore all coefficients are0. Minimality again forces one group, contradicting gcd(3,8)=1. Thus m divides30, giving exactly the eight orders in B56. These steps retain indexed terms even when powers coincide.

### 6.2 All eight reductions

The reductions in B65–91 reconstruct directly:

- m1 gives5; m2 gives−1.
- m3 gives2+zeta+2zeta²=−zeta.
- m5 leaves zeta³−zeta² after subtracting Phi_5.
- m6 cancels zeta²+zeta⁵ and leaves zeta.
- m10 gives1+zeta−zeta⁴, then2+zeta²−zeta³, a nonzero polynomial of degree3<4.
- m15 uses zeta¹¹=−zeta⁶−zeta and Phi_15 to give zeta⁷−zeta⁶−zeta⁵+2zeta⁴, nonzero of degree7<8.
- m30 has eta=−zeta primitive of order15. Substitution gives1−eta³+eta⁸−eta¹¹−eta⁴; the same order15 relations yield eta⁷+eta⁶−eta⁵−2eta³+2eta, nonzero of degree7<8.

These are written reductions using the named minimal-polynomial property, not trust in the prior evaluated remainder witnesses.

### 6.3 Decomposable relation

A proper zero subset cannot have one or four terms, so any nonminimal relation splits into a pair and a triple. Three unit roots summing to zero form a scaled cube-root triangle, as the modulus argument at B99 shows. For the ten triples, the difference pairs are

    (3,8),(3,11),(3,19),(8,11),(8,19),
    (11,19),(5,8),(5,16),(8,16),(3,11).

All have gcd1 except (8,16). In a gcd1 case the two order-three conditions force m to divide3, so the complementary opposite pair is impossible. The exceptional triple {3,11,19} requires zeta⁸ primitive of order3, whereas its complementary pair {0,8} requires zeta⁸=−1. This is also impossible.

Hence R5 has no root of unity at any order. This establishes the load-bearing identity claim without the prior finite table.

### 6.4 All-order cyclic inverse and restricted threshold

No root of unity makes R5 invertible in Q[z]/(z^n−1) for each n. Since R5*S_n=5*S_n there, the unique solution L is S_n/5, contradicting actual0/1 endpoint coefficients. Combining this with R4 and the raw collisions proves exactly:

    Every finite UD factor-complete extension of the literal C
    contains an actual a^ell b^beta with ell>=26 and beta>=1.

This is the capped-pure-end-support obstruction requested by v30-D. It is **not** an unrestricted completion/noncompletion theorem, a bound on the pure-a order, an iterated critical-gap theorem, or an answer for larger pure-end supports.

## 7. Explicit NOT_RECONSTRUCTED boundaries

1. **The prior arithmetic JSON,36 cyclotomic remainder identities, generated divisors/quotients and all associated execution/resource/exit claims:** NOT_RECONSTRUCTED. They remain unadmitted observations under C and parent v7; no acceptance depends on them.
2. **Full GP theorem and its parent acceptance chain:** NAMED IMPORT, not reproved from its original source here. The exact pure-run/one-gap and endpoint conclusions are conditional on the stated GP interface. No generic residue realization converse is imported.
3. **Full M0 completeness certificate:** NOT_RECONSTRUCTED and not needed; K0's UD and its missing core were reconstructed directly above.
4. **Arbitrary-many-positive-gap existence/uniqueness, an actual global Shor completion M, or all-order elimination of every larger endpoint support:** NOT_PROVED by the author and NOT_RECONSTRUCTED by this review. They remain the mathematical gap, not hidden PASS obligations.
5. **Novelty, configured dual-family/human/formal verification and actual runtime inventory:** NOT_PERFORMED. Reading C establishes disclosure content, not a new process attestation.

No source repair is requested at the reconstructed written scope. The standalone original finite-table argument must never be quoted as reviewed without the mandatory written-roots and admission overlays. Frozen source bytes were not modified; outputs are confined to the reviewer's root.
