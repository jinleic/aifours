# w34 Olson class-two p-group carry/zero-count theorem — full standalone review

Reviewer **InfoResearch96h-2**, info-1. Author **MathOlson-2-2**, math-2. Actual native prewrite clock: **Tue Oct 27 15:34:48 PDT 2026**; first duty observation **15:30:58 PDT**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE. 0 FATAL / 0 MAJOR / 0 MINOR.** The supplied standalone proof supports `A≡1 (mod p)` for EVERY prime, EVERY finite class-at-most-two p-group and EVERY original-order word of length `2|G|-1`, counting EXACTLY `|G|` increasing-index identity selections. This is a proper-GROUP-CLASS theorem, not the unrestricted all-finite-group problem or a novelty finding.

## 1. Mandatory pre-body ACK, complete raw coverage and exclusions

S0 was read completely FIRST (31LF, pin `a7161aa016f59552d9ee823cd2e4205df74ef2308e6ad25c4ed18322d78e580b`), then the ENTIRE manifest (38LF/3685B, pin `5ce28537d01a79e5891f1cf93ab8ca6bc8e7aaa6bc47359ab6ce046c35e58cae`). BEFORE ANY packet body or mathematical reasoning, I wrote the required actual-clock pre-body ACK at **15:31:21**:

`review-w34-olson-class2-pgroup-zero-count-prebody-ack-v1.json`, SHA256 `88334e22f92c9ec8a25c48c1f5242fa7eec23945ee237ec5dc3e577c3e232cf5`, 29LF/4198B.

The sole part was then live-pin-matched and read **COMPLETELY in RAW windows of at most60LF**:1–60,61–120,121–180,181–240,241–300,301–349. Every source ending and the historical stop ending was included. No long-line elision occurred in those returned raw windows.

Packet: `packet-part-1-v1.md`, SHA256 `aa037c66c2c2d25a80ef408c4b7ca58cf9a1d78e5649327f7a4d6f51067cb701`, 349LF/28346B. It contains ALL:

- **S1 target/controls:**42LF, `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788`.
- **S2 STANDALONE A6:**282LF, `c4641b356ea4f2e9fd2630ed3a4e50707252fdfaded3da970e3210807f054799`.
- **S3 HISTORICAL separate A5 review stop:**13LF, `a45074daba5880c36be60e7310edccb3a3ea18fa98cf0c4c3ed0fedc4a863186`.

References below are these OUTER S-line labels. No A5 mathematical body, old Olson source/review/park/checkpoint, Dimitrov/Mohar source, held formula/guide, selected control/outcome or author contact was opened. Author private provenance/ACK chronology beyond the supplied literals is not independently certified. S3 is a PROCESS boundary only: w30's selected-control episode/partial assessment and every consumer are HELD/ZERO, not evidence for or against this A6 mathematics. This is a separately frozen review, not resuming, curing or inheriting w30. No values or private reasoning from that event are present or reconstructed here.

**Prior contact/exposure:** as stated in the pre-body ACK, this continuing owner has inherited cross-domain group/coset/ordered-word review exposure; the exact older author/reciprocal-contact census is not established and no old history was retrieved. No math-2 author body was reviewed in this new window before this duty. I do not claim blindness, independent configured-family review, unaffected cognition or absence of older material contact. No old verdict or A5 theorem is a premise below. The proof checks are universally symbolic; NO selected prime, group, order or word example was tested, even privately. The exhaustive characteristic-two/parity branch required by the theorem is not a selected sanity experiment.

**Actual pre-return protocol update, 15:36:41 PDT:** Main's additional reminder says three related review attempts reported prohibited selected sanity checks and were stopped; it supplies NO values or mathematical conclusions. I have performed no selected prime/group/order/particular-word sanity substitution in this duty. The characteristic-two reasoning below is the fully quantified required case, not a tested group/word. No stopped review's values or assessment are used or reconstructed. Main also reminds that my own phase-type mixed-packet STOP and ALL ZERO consumers persist; that is binding, not repaired or rehabilitated here. No phase-type result/body/verdict is a proof premise of the standalone A6 reconstruction. This action report is not a global private-cognition/noninfluence census.

Only the required ACK and this requested review output are written for this duty. No scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/test, external source/modelCLI/nested agent, author contact, Git or deletion was used. Same-harness written review is not formal/kernel, executable, human, novelty or parent adoption.

## 2. Exact original caller and gate decisions

S1's literal ordered target requires increasing ACTUAL indices, not a permutation of the selected letters. S2 assumes `G` finite of p-power order and `[G,G] subset Z(G)`; no exponent-p condition, no fixed prime and no special word pattern is added. Its claim includes abelian/trivial groups, repeated/identity letters and all exponent/carry degeneracies. The original all-finite-group problem remains outside this proper class.

| Gate | S2 locations | Decision |
|---|---|---|
| Cyclic decomposition without a classification import | LF26–48 | SUPPORTED |
| Actual normal form, original-order commutators and central power carries | LF50–124 | SUPPORTED |
| Integer digit polynomials and actual q-divisibility degree estimate | LF126–168 | SUPPORTED |
| Exact support/cardinality/identity IFF and full degree budget | LF170–218 | SUPPORTED |
| Elementary field zero count and exact selector congruence | LF220–245 | SUPPORTED |
| Both actual-object directions and all stated boundaries | LF247–282 | SUPPORTED; no unrestricted/novelty upgrade |

## 3. Cyclic decomposition: checking every extension and splitting step

For a nontrivial finite abelian p-group A, choose an element a of maximal order `p^e`. Since all element orders are p-powers, this maximum annihilates every element of A. Start the character on `<a>` by `chi(a)=1` in the additive cyclic group of order `p^e`.

If its current domain H is not all A, choose b outside. The coset b+H has order `p^r`, with `1<=r<=e`. Put `h0=p^r b`. Then `p^(e-r)h0=0`, so its character value is annihilated by `p^(e-r)` in the cyclic target, which means it is divisible by `p^r`. Thus a y solving `p^r y=chi(h0)` exists.

Define `chi'(h+j b)=chi(h)+j y`. If two expressions agree, their j-difference is `p^r t` and the compensating H-difference is `-t h0`. Their proposed character values differ by `-t chi(h0)+p^r t y=0`. This verifies ALL relations, including any finite-order relation of b, not merely a chosen representative. The extended domain strictly increases; finiteness completes the extension to A.

The resulting chi is onto, and every x splits as `chi(x)a+(x-chi(x)a)`, the second part in the kernel. Intersection with `<a>` is zero because chi restricts to the canonical cyclic isomorphism there. This is a direct sum with a smaller kernel; induction proves the asserted cyclic decomposition. The trivial group is the empty-product base. Only the ordinary cyclic-subgroup/coset order divisibility is needed, as stated by the author.

## 4. Normal form and exact original-order multiplication, with ALL carries

Let `Z=Z(G)`. It is abelian and G/Z is abelian by the class-two hypothesis. Both are finite p-groups by elementary quotient/subgroup cardinality. Apply §3 to obtain ACTUAL decompositions with nontrivial factor orders `q_i=p^(a_i)` and `r_j=p^(e_j)`. Let `Q=product q_i`, `R=product r_j`, so `|G|=QR=p^m`, `m=sum a_i+sum e_j`.

Choose actual lifts h_i of the quotient generators and actual central generators z_j. Quotient coordinates determine each alpha_i uniquely modulo q_i; after subtracting the chosen lifted product the remaining element lies in Z with unique central coordinates modulo r_j. This proves the stated unique normal form. It does NOT claim the h_i have order q_i in G.

Indeed `h_i^(q_i)` is central, with actual coefficients theta_(ij), and `[h_i,h_l]` is central, with actual kappa_(il,j). These are read from the given group, not freely prescribed realizable data. Nonnegative representatives modulo r_j are legitimate; changing such representatives changes only a multiple of a central generator's order.

For the declared commutator convention `[x,y]=x^-1 y^-1xy`, direct multiplication gives `xy=yx[x,y]`. Centrality then yields `h_i^u h_l^v=h_l^v h_i^u[h_i,h_l]^(uv)` by induction. To collect the actual selected word, a later h_l-power crosses an EARLIER h_i-power exactly when `i>l`; its occurrence labels satisfy `u<v`. Thus the supplied central contribution is precisely

`sum_(u<v) sum_(i>l) kappa_(il,j) alpha_(ui)alpha_(vl) z_u z_v`,

with the sign/order specified by that actual commutator convention. Earlier central coordinates commute and contribute their stated linear sum. No same-letter crossing is added because each input letter's own normal form is already ordered. Keeping the powers h_i unreduced until the final test preserves all power carries.

The quotient coordinates vanish iff `q_i|S_i` for every i. ONLY THEN each `h_i^(S_i)` equals its actual central power `(h_i^(q_i))^(S_i/q_i)`. Identity of the whole product is therefore equivalent to every `r_j` dividing

`U_j=T_j+sum_i theta_(ij)(S_i/q_i)`.

There is no field division or ignored central carry in this integer condition.

Let `q=max q_i=p^a`, or `q=1,a=0` if the quotient list is empty. Multiplying the last condition defines the actual nonnegative-coefficient polynomial

`F_j=q T_j+sum_i theta_(ij)(q/q_i) S_i`.

Given the quotient conditions, `F_j=q U_j`, so `r_j|U_j iff q r_j|F_j`. Those quotient conditions also force the low a digits of F_j to vanish. Thus it is valid to constrain only digits a through `a+e_j-1` of F_j AFTER imposing the quotient digits. No such automatic low-digit assertion is applied to unrelated supports.

Every quadratic coefficient of F_j is divisible by q. If q=1 the quotient is trivial, G is abelian and there is NO quadratic contribution. This exact structural divisibility, rather than a generic degree-two estimate or exponent-p assumption, is the critical later budget input.

## 5. Integer digit helper: why it really encodes arbitrary carries

For an integer activation polynomial `H(z)=sum_A c_A z_A` with nonnegative coefficients, define

`P_H(T,z)=product_A [1+z_A((1+T)^(c_A)-1)]` over F_p.

On a Boolean support each z_A is literally zero or one. The factor is therefore either one or `(1+T)^(c_A)`, proving the EXACT identity `P_H(T,z)=(1+T)^(H(z))` at that support. The integer exponents c_A are retained BEFORE reducing polynomial coefficients modulo p; they are not naively replaced by c_A mod p. This is what keeps higher carries.

For any nonnegative integer w with base-p digits w_b, repeated Frobenius gives

`(1+T)^w=product_b (1+T^(p^b))^(w_b)` in F_p[T].

Frobenius here follows from the ordinary prime binomial identity and iteration. To obtain degree `p^l`, higher-digit factors cannot contribute, and the MAXIMUM total degree of all lower-digit factors is `sum_(b<l)(p-1)p^b=p^l-1`. The only contribution is the linear term of the l-th digit factor, with coefficient w_l. Therefore the author's coefficient polynomial Delta_l(H) evaluates to the l-th INTEGER base-p digit modulo p, regardless of how large H(z) is. No bound by |G| or prime-exponent restriction is used.

### Degree, not merely the digit values

If positive c is divisible by `p^b`, then `(1+T)^c=(1+T^(p^b))^(c/p^b)`, so every positive T-degree in its activated factor is at least `p^b`. In any product term contributing to coefficient T^w, the sum of activated z-degrees is at most w whenever EACH activation degree is no greater than its minimum possible positive T-degree. The claimed degree bound follows term by term; repeated variables or coefficient cancellation cannot increase it. No Boolean/squarefree reduction is silently substituted for ordinary polynomial degree.

For S_i all activations are linear, hence `deg_z Delta_l(S_i)<=p^l`. For F_j its linear factors also satisfy this condition, while each quadratic factor has minimum positive T-degree at least q. If q>=2 then its activation degree two is at most q; if q=1 there are no quadratic factors. Thus universally

`deg_z Delta_(a+l)(F_j)<=p^(a+l)=q p^l`.

This includes all central power exponents and the characteristic-two branch without selecting or calculating a sample group. Zero coefficients/factors can be omitted. A constant activation, if one considered the general helper with it, costs z-degree zero and cannot break the bound; the ACTUAL H=w,S_i,F_j used here have no nonzero constant terms.

## 6. Exact common-zero / actual-selector equivalence

Introduce ONLY the L=`2n-1` variables t_v over F_p and put `z_v=t_v^(p-1)`. The stated elementary permutation-of-nonzero-elements proof gives z_v equal to one exactly at nonzero t_v; otherwise it is zero. No independent carry/digit variables are introduced, so there is no extra uncontrolled field-solution multiplicity.

Let w be the INTEGER support size. Cardinality digits0 through `m-1` vanish iff `p^m=n` divides w. Since `0<=w<=2n-1`, this means exactly w=0 or w=n. Quotient digits then give every `q_i|S_i`, and the central high digits, together with the now-automatic low a digits, give `q r_j|F_j`, equivalently every actual central identity condition from §4.

Thus a common zero is precisely the all-zero support OR one actual n-occurrence identity selection. Conversely every such increasing-index identity selection satisfies the complete system and every independent nonzero t-value on its support yields that same Boolean data. Identity/repeated letters and vanished coordinates do not alter this IFF.

For the empty support all the actual integer activation sums vanish, so it is indeed a common zero. It corresponds to EXACTLY one field point: every t_v zero. An empty selection is not mistakenly promoted into the required n-index subsequence; it is separately counted and removed by the congruence argument.

## 7. Complete degree inequality: checking the additional p−1 factor

Substitution `z_v=t_v^(p-1)` multiplies each ordinary degree bound by p-1. Summing the cardinality equation degrees gives

`sum_(l=0)^(m-1)(p-1)p^l=p^m-1=n-1`.

Summing quotient-coordinate degrees gives `sum_i(q_i-1)`. Summing the selected central-digit degrees gives `q sum_j(r_j-1)`; the shift by a is therefore fully paid, not forgotten.

For any positive-integer list, expansion of `product[1+(q_i-1)]` proves `sum_i(q_i-1)<=Q-1`; similarly the central sum is at most R-1. Empty lists obey the same convention. Since `q<=Q` (also `q=Q=1` in the empty quotient case), total GROUP-coordinate degree is at most

`(Q-1)+q(R-1)<=(Q-1)+Q(R-1)=QR-1=n-1`.

Including cardinality gives `sum deg(all equations)<=2n-2<L=2n-1`. This already counts the selector substitution p-1. The NEXT zero-indicator step raises the constraint polynomials to p-1 once more, exactly as required by its lemma; that is not a missing factor in the current inequality.

All q_i,r_j here are actual p-power group-factor orders; the argument is symbolic for all such lists. No small exponent, rank, dimension or selected-order boundary was substituted to validate it.

## 8. Elementary finite-field zero count and exact congruence

Let the current constraint polynomials be f_r. Because `sum deg f_r<L`,

`I(t)=product_r(1-f_r(t)^(p-1))`

is the common-zero indicator and has degree strictly below `L(p-1)`. Each monomial must have SOME variable exponent e<p-1. If e=0, summing over that variable gives p=0 in F_p. For `0<e<p-1`, the polynomial `X^e-1` has at most e roots, so some nonzero scalar u has `u^e!=1`; scaling the COMPLETE field sum by u proves its e-th power sum is zero. This proves that every monomial's complete field sum vanishes, and hence the integer common-zero count C is divisible by p.

The polynomial root bound is the elementary repeated-linear-factor bound, not an imported Chevalley–Warning theorem. When p=2 only the e=0 killing case is needed; there is no unprovided intermediate exponent. Zero equations may be omitted, and an empty equation family gives the same constant-indicator argument for L>0. This is an exact universal proof of a finite sum identity, not an executed enumeration or selected-prime check.

By §6 there is one zero-support solution, and each actual n-index identity selector has EXACTLY `(p-1)^n` field realizations. Thus the source's exact count, not merely an inequality, is

`C=1+A(p-1)^n`.

For odd p, n=p^m is odd, so the last power is congruent to -1. For characteristic two it is one, also -1 in that field. Therefore C≡0 gives `A≡1 (mod p)` and A is nonzero. This is the exhaustive parity/characteristic branch required by the theorem; no concrete prime/group/order was selected.

For n=1 the group is trivial, the one input letter is its identity and the single index is the unique required selector. Alternatively m=0 and both coordinate lists are empty, so the one field variable has no constraints, C=p, and the same count yields A=1. All empty/zero boundaries are paid with no false denominator or missing equation.

## 9. Actual-order and group-class caller, with the separate historical STOP

The field support maps to its increasing ORIGINAL indices. Its product is tested using the same S_i,T_j,F_j, whose strict `u<v` sum retains all order-sensitive commutators and whose theta terms retain central power carries. Sorting the h_i BASIS powers in that algebraic computation is not reordering the selected original letters. The reverse direction counts every original-order selector with its exact `(p-1)^n` multiplicity. Thus neither an unordered-product theorem nor a quotient-only selector was substituted for the book target.

This establishes the full original `2n-1`/n conclusion for the stated entire class-at-most-two p-groups, any exponent. It does not provide a WLOG reduction for mixed-prime or higher-class groups, resolve the old odd-prime dihedral residual, exhibit a global avoiding word or settle the unrestricted all-finite-group conjecture. The source explicitly maintains those limits and makes no novelty/priority claim.

The separate S3 w30 process record remains binding: that A5 review stopped with its partial assessment/selected episode and consumers HELD/ZERO. No w30 outcome, A5 mathematical body or earlier prime-exponent verdict was used here. A6's cyclic structure, carries, digit bounds, cardinality helper and zero count are all supplied and reconstructed above, so it is genuinely reviewed as a standalone new scope. This review neither clears w30 nor authenticates historical mathematical noninfluence.

## 10. Final separate decisions and assurance ceiling

- Lemma B cyclic decomposition: SUPPORTED with all extension/well-definedness/splitting cases.
- Actual central normal form/original-order collection: SUPPORTED, including arbitrary powers, central carries and actual-coefficient compatibility.
- Integer digit polynomials and degree control: SUPPORTED without generic-quadratic or squarefree-degree shortcuts.
- Exact support0/n and identity equivalence: SUPPORTED in BOTH actual-object directions.
- Whole degree budget and elementary zero-count lemma: SUPPORTED for ALL primes/exponents, with the p-1 factors and empty cases checked explicitly.
- Selector count `A≡1 mod p`: SUPPORTED at the full proper-group-class scope; unrestricted original problem remains OPEN.

**0 FATAL / 0 MAJOR / 0 MINOR for the complete frozen standalone A6 theorem and its application scope.** Named ordinary inputs are only elementary group/cyclic arithmetic, finite induction, binomial/Frobenius identities, integer digits, polynomial root bound and finite counting; specialized required results are proved in the packet and reconstructed here. No group classification, advanced group algebra/Jennings or external finite-field zero-count theorem is implicitly assumed.

All original STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit unestablished and auxiliary214 STOP remain. This return is same-harness written review, not a private-provenance certificate, formal/kernel/executable/human/configured-family review, novelty/priority clearance, parent adoption or original full-target completion.

**END COMPLETE w34 REVIEW — required pre-body ACK preceded all packet/reasoning; sole part read in <=60LF raw windows, all source endings included; no author contact or other source.**
