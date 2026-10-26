# v32-E — written review of joint-boundary and two-positive-gap identities

Reviewer InfoBalancedNL242-2, info-6; author MathShor. Actual pre-return observation: `Sun Oct 25 04:48:42 PDT 2026`.

## 1. Exact binding and verdict

- Manifest `peer-review-wave-eighteen-v32.json`, v32-E: SHA-256 `7c2f7e7679040669e9e97fb71da76e7e1eb846cb5af28f35afe55d593e504708`.
- Literal packet `peer-review-wave-v32-shor-joint-two-gap-sources-v1.md`: SHA-256 `be0cd9bec8a246213a595730006cf8efa36798f465da211ad40ea0574d07ef32`.
- Sole author source `proof-HETEROGENEOUS-JOINT-BOUNDARY-TWO-GAP-v1.md`, LF1–214: SHA-256 `6532a032aed9e19eef70927c98f07c470d29b2e6d241eef34c7ac16adfde511f`.

All hashes were freshly observed with metadata-only shasum. The packet receipt's exact rendering entry was read. Every source line was read through the223-line literal packet, with additional raw reads of long LF3,5,15,41,47,62,78,86,96,102,128,131,140,142,161–171,200,202,204,210,212,214. References below are author-source LF, not packet wrapper LF.

Exposure ACK: `peer-review-shor-joint-two-gap-ack-v1.json`. Previous v30-D review was already returned. The reviewer knows the author's earlier PR/HG packet and written-roots overlay from that review. This is a reciprocal same-harness supplied-proof review; the author is assigned the reviewer's four-stream packet in v32-F. It is not blind, cross-model, human, formal or novelty acceptance.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the reconstructed subsystem scope.** The joint-delay count matrix, all five parsing cases, single zero-gap bridge resolvent and their exact coefficientwise equivalence are reconstructed below. The accepted GP interface and previously reconstructed pure-run classification are explicit imports. No unrestricted Shor completion/noncompletion conclusion follows.

Parent erratum v7 was reread. This review used strictly written reasoning plus metadata/source tools: no scientific arithmetic interpreter, eval, enumeration program, symbolic program, certificate replay or solver; no GO exists.

## 2. Joint pure-run matrix and boundary orientation

For LF21–54, rows index the actual initial delay e and columns the actual final delay d. Optional start, any number of a^n, optional end gives L_e R_d/Delta. A singleton isolated word contributes H_ed. The only empty parse is e=d=0 with zero powers and both optional endpoints empty; subtracting its1 yields J0. Thus P_00=z^n/Delta and every P entry is the indicated nonempty count series.

Summing over initial or final endpoint recovers exactly F_d or G_e. This is an actual joint distribution of labelled parses, not a free coupling of two fixed marginals.

For LF56–62, the first run's final delay is d and the next run's initial delay is e, so T_g must have row d and column e. The test d+e<=g is necessary and sufficient; exactly g−d−e codeword copies of b fill the surplus. Another pure-b word would already contradict UD because b is a codeword.

Therefore the matrix products in the source use the correct final-to-initial contraction, not a hidden transpose.

## 3. Actual bridge matrices and endpoint attachments

The matrices W_g and W_(g,h) in LF66–78 count actual raw words with exactly one or two positive internal b-gaps. Every monomial retains the number of a's on each side of each internal gap. The matrix indices retain the actual outer b-delays; different words are still different labels. Words with further positive gaps cannot contribute to these cores.

For LF80–94, consider a bridge with initial delay e and final delay d:

- With no prefix its external initial delay remains e, the identity-matrix option.
- A nonempty prefix can precede it inside one adjacent a-run only if both the prefix's final delay and e are0. The matrix entry of PZ is precisely P_(external,0) times the indicator e=0.
- Dually, ZP attaches a nonempty suffix only when d and the suffix's initial delay are0.

Thus A=I+PZ and B=I+ZP have exactly the source's orientation, including the wholly empty prefix/suffix cases. C_g=A W_g B counts parses whose sole crossing word bridges that gap, with arbitrary legal external pure attachments. The disjoint no-crossing contribution is P T_g P. Endpoint summation consequently reproduces the earlier HG_g identity.

## 4. The bridge-to-bridge resolvent is exactly ONE geometric factor

At LF96–102 the first bridge ends inside the middle adjacent a-run and the second bridge starts later in that same run. If either touching b-delay were positive, their internal zero-gap join would be impossible. Hence both touching bridge indices must be0.

If no pure word lies between them the transition is Z. If a nonempty pure-run parse lies between them it must have initial and final delay0, giving ZP(y)Z. J0 supplies P_00=y^n/(1-y^n), so

    Z+ZP(y)Z=Z/(1-y^n).

This includes the zero-intervening-word case once and every positive a^n-chain once. It does not count the middle run itself as empty: each bridge already contains a positive middle a-segment, so their concatenated middle contribution has positive length even when the chain is absent.

A product of independently attached first-bridge suffix and second-bridge prefix would split the same a^n-chain at an arbitrary cut and overcount it. The single factor in J4 is therefore essential, and its source placement between W_g and W_h is correct.

## 5. All five cases of J5 are disjoint and exhaustive

Fix g,h>0 and positive run lengths. A raw ordered parse can have at most one word crossing each fixed gap. Classify by whether the first gap and second gap are crossed and, if both are crossed, whether it is the same word:

1. **Neither:** each run has a nonempty pure-run parse. The two independent actual joins give `P(x)T_gP(y)T_hP(z)`.
2. **First only:** the whole two-run first-gap contribution is C_g, including all its legal pure prefix/middle suffix data. Its final delay joins the third pure run through T_h, giving `C_g T_h P(z)`.
3. **Second only:** the reversed third term `P(x)T_g C_h` follows identically.
4. **Both, distinct words:** the first and second bridges contain nonoverlapping ordered pieces of the middle a-run. Their remaining middle material is exactly one possibly empty a^n-chain. Only the outer first/third runs have optional pure attachments. This gives `A(x)W_g(x,y)[Z/Delta(y)]W_h(y,z)B(z)`.
5. **Both, the same word:** the word contains the complete middle run and both positive gaps. Only outer prefix/suffix attachments remain, giving `A(x)W_(g,h)(x,y,z)B(z)`.

The crossing status makes cases1–3 distinct; cases4 and5 differ by the number of crossing words. A word with at least three internal positive b-gaps cannot fit the three-run core, regardless of how many such longer words the hypothetical finite M contains. These facts prove both exhaustiveness and absence of double counting. No independence of middle-run endpoint marginals was assumed.

## 6. Subsystem iff, denominator clearing and the residual

Each entry of J5 records a labelled parse with its two actual external delays. Summing all endpoints gives its total count. Therefore the coefficient of x^p y^q z^r is exactly one for every p,q,r>0 iff J6 holds. This is necessity and sufficiency for the **stated three-run free-end parsing subsystem**, conditional on the GP interface; it is not global all-list UD or factor completeness.

Denominators are as claimed at LF142:

- P has at most one Delta denominator in its own run variable.
- The one-bridge terms have one outer attachment denominator in each bridge variable and one denominator for the remaining pure run.
- The two-distinct-bridge term has the single middle Delta from J4 and only the two outer attachment denominators.
- The one-both-gaps word has only the two outer denominators.

Thus multiplication by Delta(x)Delta(y)Delta(z), all with constant1, loses no formal-series condition and gives a finite polynomial identity. Finiteness is for the actual finite endpoint/word data, not an imposed run-length cutoff.

For LF146–171, Lower is the nonnegative count series of the first four disjoint cases. Def=target−1^T Lower 1 therefore has the following exact meaning:

- A negative coefficient at a positive core means at least two lower parses already exist. Adding further words cannot remove those parses; via GP no completion of that data can be UD.
- If Def is nonzero, setting W_(g,h)=0 cannot satisfy the identity. A putative completion must realize Def by actual three-run words with those precise gaps and outer attachments. A word with more gaps cannot fit the missing core. A negative Def, of course, is impossible even with such an addition; this is consistent with the first bullet, not a promise that every nonzero Def is fillable.

Substituting Abar=Delta(x)A and Bbar=Delta(z)B into J8 gives J9 directly: the middle factor Delta(y) remains because one word spanning both gaps admits no separate middle pure-run attachment. Nonnegative arbitrary polynomial filling is not enough; one needs the exact actual-word matrix and its prescribed attachments.

## 7. Non-Shor control — reconstructed at its claimed coefficient

The v30-D review reconstructed K0's UD directly: its only proper-prefix residual is `aba`, which has no further prefix relation with a K0 word. Its pure-run and every one-gap identity were also reconstructed there. The present review does not replace that control by a Shor candidate.

For K0, LF184–198 gives only P_00=z²/Delta and P_02=z/Delta, with W_1 entries x³y at(0,0) and xy at(1,0). These follow directly from aa,abb,aaaba,baba. There is no W_2 or three-run word.

At gaps(2,1) and coefficient xyz:

- All-singleton parses must use abb at each a-run. The first boundary permits2, but the second requires at least2 and has only1.
- A first-gap bridge is absent because W_2=0.
- A second-gap bridge aaaba uses too many middle a's; baba is length-compatible but its initial delay1 after the first abb requires the first gap at least2+1=3, not2.
- The distinct-bridges term again contains W_2 and vanishes, and the same-word term is absent.

So Lower's coefficient is0 and the target coefficient is1. Adding the actual word abbaba contributes xyz to W_(2,1) at(0,0); the identity components of A,B supply exactly that missing coefficient without a pure attachment. The other control word abaaba has run lengths1,2,1 and gaps(1,1), as stated. Neither observation asserts that arbitrary defects are filled by these two words or that an analogous Shor addition is globally compatible.

## 8. NOT_RECONSTRUCTED and nonclaims

- **Original GP theorem and its complete acceptance chain:** named import, not re-proved from its original source. No generic residue-to-raw-word realization converse is imported.
- **M0's full UD/factor-completeness proof:** named import, not re-proved here; only the explicit K0 coefficient and proposed actual bridge were needed for this review.
- **A coherent actual Shor solution of J5–J9 for all g,h, arbitrary-many-run analogues, all-list UD and global factor completeness:** NOT_RECONSTRUCTED / NOT_PROVED. The author explicitly leaves them open at LF210–214.
- **Any claim that an arbitrary choice of nonnegative polynomial matrices corresponds to a single raw code:** not supplied and not accepted. The theorem uses actual labelled word data throughout.
- **Executable, finite-certificate, process-exit, formal, human, cross-model or novelty acceptance:** not performed or inferred. There was no computation to replay in this strictly written packet.

No source repair is requested at this precise written subsystem scope. All outputs are in the reviewer's owned root; frozen author/shared sources remain unchanged.
