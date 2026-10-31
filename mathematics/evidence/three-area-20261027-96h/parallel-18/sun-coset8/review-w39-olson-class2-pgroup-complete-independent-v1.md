# w39 — Complete standalone class-at-most-two p-group ordered-selector review

Actual native `/bin/date` before this NEW body: **Tue Oct 27 15:49:05 PDT 2026**.
Reviewer **MathSun8-2**, math-6. Author **MathOlson-2-2**, math-2.
**Same-harness WRITTEN review**, serial and non-blind; not formal/kernel, human/configured-family, executable or novelty verification.

## 1. Exact verdict, quantified theorem and coverage

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.** The complete standalone A6 proof is reconstructed below for EVERY prime p, EVERY finite p-group G with `[G,G]⊆Z(G)`, ANY exponent, and EVERY ACTUAL ordered word of length `2|G|−1`. Its number A of exactly-|G| increasing-index identity selectors is `1 modulo p`. No mathematical FATAL, MAJOR, MINOR or unpaid load-bearing proof is identified at this proper group-class scope.

Every cyclic-decomposition, normal-coordinate, carry/sign, conditional-integer-division, digit-degree, full-budget, zero-count and selector-multiplicity step is paid from this supplied source. No earlier A5 source/verdict, stopped review assessment or chosen prime/group/order/word is input. Characteristic two and the trivial/empty/repeated-value cases are proved as universally quantified cases, not tested examples.

The original supplied target is for ALL finite groups and exact original-order selections (S1 LF38). This proper p-group/class-two theorem is not WLOG for mixed-prime or higher-class groups and does NOT close unrestricted Olson or the old prime-dihedral residual. Source/priority/literature and stronger verification remain separate.

S0 was read completely FIRST, followed by the complete frozen manifest (SHA256 `92adde39f9a39e6507193a6ffb9e77c3b5a7c65296e8626514f20c26751faa00`). The actual15:44:31 pre-body exposure ACK was WRITTEN before any packet access or mathematical review reasoning:

`review-w39-olson-class2-pgroup-complete-independent-prebody-ack-v1.json`, SHA256 `9fe419e2ac91bb997926f7afe446849f25bdf4891d22fc175c6405cce69a580b`,21LF/5237B.

ALL429LF/37653B of the sole packet were read raw in returned windows1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–429, including every long line and true ending. Packet SHA256 `268ceb3e9cfd5e9bd964d4716ed7794d96a6c97262675ed34fa2036573cfb294` matched the dispatch before opening.

| Source | Complete supplied LF | SHA256 |
|---|---:|---|
| S1 original ordered-problem definition/control packet | 42 | `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788` |
| S2 standalone carry-correct A6 proof | 282 | `c4641b356ea4f2e9fd2630ed3a4e50707252fdfaded3da970e3210807f054799` |
| S3 w30 process STOP | 13 | `a45074daba5880c36be60e7310edccb3a3ea18fa98cf0c4c3ed0fedc4a863186` |
| S4 w33 process STOP | 13 | `7220b27010b3d5bc0d15a1f3f8f40f91e108a6eb9f5d376fd29fcc521b6837ab` |
| S5 w35 process STOP | 17 | `0d7cfcde96c922184c3ad89938deb46271c4aa07e81fae535886ccd72bd6a6c0` |
| S6 w38 process STOP | 17 | `0292fc4ce079db82b3461ecda4972123eee6e86655609618ce422810405250a4` |
| S7 own Sun selected-index STOP | 17 | `18961a1e608b5ac5ecc141e129ff5f65bbc745aa916edf2faf5b7842abd27531` |

S3–S7 are process boundaries ONLY. Their failed-review outcomes and partial assessments are NOT a mathematical input, repair target or confidence guide. None of their selected values/outcomes was recovered. No author contact or other source was used.

## 2. Elementary finite-abelian cyclic decomposition: Lemma B

**Claim:** every finite abelian p-group is a direct product of cyclic p-power groups, with the trivial group an empty product (S2 LF30–48).

**Reconstruction.** In additive notation choose an element a of maximal order p^e in a nontrivial finite abelian A. Lagrange/cyclic coset cardinality makes every element order a p-power dividing this maximum, so p^e annihilates A. Start `chi:<a>→C_(p^e)`, a↦1.

Suppose chi is defined on H containing a. For b outside H, its coset in A/H has order p^r with `1≤r≤e`. Put `h0=p^r b∈H`; it is annihilated by `p^(e−r)`. Its image under chi has the same annihilation, hence is a multiple of p^r in the actual cyclic target. Choose y with `p^r y=chi(h0)`. This is integer cyclic arithmetic, not division by a nonunit in F_p.

Define `chi'(h+j b)=chi(h)+j y`. If two expressions agree, j−j'=p^r t by the coset order, and h−h'=−t h0. The image difference is `−t chi(h0)+p^r t y=0`. Thus chi' is well-defined, additive and extends chi. Each step strictly grows its finite domain; iteration reaches A.

At the end chi(a)=1, and every x splits as `chi(x)a+(x−chi(x)a)` with the second summand in ker chi. The first summand is well-defined modulo p^e, and `<a>∩ker chi=0`. Therefore `A=<a>⊕ker chi`; the kernel is strictly smaller. Finite induction proves the whole decomposition. No structure/classification theorem or choice of a test group is imported.

**Mathematics/dependency verdict:** reconstructed in full. Maximum order, the image-divisibility step and extension well-definedness are all paid; no missing homomorphism-extension premise.

## 3. ACTUAL central normal coordinates and order-sensitive commutator sign

Apply Lemma B to the actual center Z(G) and actual abelian quotient G/Z(G); both are finite abelian p-groups because the commutator subgroup is central. Write their nontrivial cyclic orders as `q_i=p^(a_i)` and `r_j=p^(e_j)`; empty lists are permitted. Choose actual quotient lifts h_i and actual center generators z_j. Put `Q=product_i q_i`, `R=product_j r_j`, so `n=|G|=QR=p^m`, `m=sum a_i+sum e_j` (S2 LF52–66).

Every group element has exactly one expression

`h1^alpha1 ... hd^alphad z1^beta1 ... zc^betac`,

with the source's integer representative ranges. Quotient uniqueness fixes the alpha coordinates, and the unique remaining central element fixes beta. This is an ACTUAL normal form, not a freely realizable coordinate ansatz.

The actual powers `h_i^(q_i)` are central but need not be1. Record `h_i^(q_i)=product_j z_j^(theta_ij)` and `[h_i,h_l]=product_j z_j^(kappa_il,j)` with nonnegative residue representatives. Commutator convention is `[x,y]=x^(-1)y^(-1)xy`, so `xy=yx[x,y]`. Centrality gives by induction

`h_i^u h_l^v=h_l^v h_i^u [h_i,h_l]^(uv)`.

In the actual input word, an earlier source occurrence u and a later one v have a basis inversion exactly when i>l. Moving the later h_l power left across the earlier h_i power contributes the POSITIVE commutator in this displayed convention. Thus for Boolean support z the ORIGINAL increasing-order product is exactly

`h1^(S1)...hd^(Sd) z1^(T1)...zc^(Tc)`,
`S_i=sum_v alpha_vi z_v`,
`T_j=sum_v beta_vj z_v+sum_(u<v)sum_(i>l) kappa_il,j alpha_ui alpha_vl z_u z_v`.

All pair crossings are paid. Because they are central, subsequent collecting does not change a crossing's value. Powers are kept UNREDUCED until the final identity test; no exponent-p assumption is made. Residue changes add multiples of the actual central order and do not change the group element. Coefficients are nonnegative integers, including zeros, which is important for the digit lemma.

The product is identity IFF all q_i divide S_i and, ONLY THEN, each r_j divides

`U_j=T_j+sum_i theta_ij(S_i/q_i)`.

The quotient conditions are necessary by actual quotient normal form. Under them each `h_i^(S_i)=(h_i^(q_i))^(S_i/q_i)` is central, giving exactly these carries; central-coordinate uniqueness proves sufficiency. No hidden half-commutator/BCH convention, negative-coordinate choice or missing carry occurs (S2 LF68–105).

**Mathematics/dependency verdict:** reconstructed for every actual class-at-most-two p-group, every original word and support, including arbitrary exponent and repeated/identity letters. The u<v terms preserve the original occurrence order, not merely a freely reordered multiset product.

## 4. Conditional integer division is removed with the SAME guards

Let `q=max_i q_i=p^a` when quotient factors exist; if none, set q=1,a=0. Each q/q_i is an integer because all q_i are p-powers. Define the actual integer polynomial

`F_j=q T_j+sum_i theta_ij(q/q_i)S_i`.

UNDER q_i|S_i it equals q U_j. Hence the identity test is exactly

`q_i|S_i for all i`, AND `q r_j|F_j for all j`.

Under the first family, F_j is divisible by q, so its lower a base-p digits are automatically zero. It is enough to impose digits a through a+e_j−1; this omission would not be valid on arbitrary unrelated supports, but the first family remains present throughout. Integer division of S_i is never applied to an arbitrary field variable.

Every quadratic coefficient in F_j is a multiple of q. Its linear coefficients need no such divisibility. If q=1, d=0, G is abelian and there are NO quadratic terms. Changing theta residues does not invalidate the guarded criterion: on q_i|S_i the corresponding change in F_j is a multiple of q r_j. All guards and actual central data are retained (S2 LF109–124).

**Mathematics/dependency verdict:** reconstructed; integer/cyclic arithmetic, not cancellation of a power of p inside F_p. No relaxation of the original identity conditions.

## 5. Boolean integer digit polynomial: value AND degree

For the actual nonnegative integer activation polynomial `H(z)=sum_A c_A z_A`, define

`P_H(T,z)=product_A [1+z_A((1+T)^(c_A)−1)]` over F_p,

omitting zero coefficients. On a Boolean support each z_A is0 or1, so this is exactly `(1+T)^(H(z))`. Thus coefficient extraction can be evaluated after Boolean substitution without a formal integer lift of arbitrary field values (S2 LF128–145).

For any nonnegative integer w with base-p digits w_b, Frobenius gives

`(1+T)^w=product_b (1+T^(p^b))^(w_b)` in F_p[T].

For coefficient T^(p^l), higher factors cannot contribute. Even taking every lower digit yields degree at most `sum_(b<l)(p−1)p^b=p^l−1`. Thus the only contribution uses one T^(p^l) from the l-th factor and constants elsewhere, with coefficient w_l. Consequently `Delta_l(H)=coeff_(T^(p^l))P_H` evaluates to precisely the l-th INTEGER digit mod p. No upper bound on H relative to |G| is required.

For the degree estimate, if positive c_A is divisible by p^b, every positive T-degree of `(1+T)^(c_A)−1` is at least p^b by the same Frobenius identity. In a product term contributing to T^w, activated factors have total T-degree w and z-degree at most the sum of their |A|. Whenever each |A| is at most that factor's minimum positive T-degree, the z-degree is therefore ≤w. This is an ordinary polynomial-degree bound; Boolean squarefree reduction is NOT needed. Repeated z variables or cancellation cannot increase it.

For S_i all activations are linear, giving `deg_z Delta_l(S_i)≤p^l`. For F_j a quadratic activation has coefficient divisible by q, so its positive T-degree is at least q. If quotient factors exist then q≥p≥2, so its activation degree2 is at most q. If q=1 there are no quadratic activations. Linear activations are always paid by minimum T-degree≥1. Thus in EVERY case

`deg_z Delta_(a+l)(F_j)≤p^(a+l)=q p^l`.

No particular coefficient, support, group order or characteristic is substituted to test this estimate. Zero coefficients/polynomials are harmless; term aggregation preserves nonnegativity and q divisibility (S2 LF149–168).

**Mathematics/dependency verdict:** both digit identity and sharp degree control reconstructed. This is the load-bearing carry improvement, not an assumed generic quadratic digit estimate or an imported finite-field theorem.

## 6. Complete field system and BOTH actual-object directions

Let L=2n−1 and take field variables t_v for ALL actual word positions. Put `z_v=t_v^(p−1)`. The ordinary Fermat identity follows because multiplication by a nonzero scalar permutes the nonzero field elements and their nonzero product cancels. Thus z_v is exactly0 or1. Its canonical integer value counts membership in the support.

Impose:

1. Delta_l(w)=0 for l=0,...,m−1, where integer `w=sum_v z_v`;
2. Delta_l(S_i)=0 for l=0,...,a_i−1 for every quotient coordinate;
3. Delta_(a+l)(F_j)=0 for l=0,...,e_j−1 for every central coordinate.

The first family is exactly n|w, and `0≤w≤2n−1` makes w either0 or n. The second family is exactly q_i|S_i. Given it, the missing lower-a digits of F_j vanish automatically, so the third is exactly q r_j|F_j and hence the actual central carry condition. Therefore a field solution has empty support OR EXACTLY n positions whose ACTUAL ORIGINAL-order product is identity.

Conversely, every such original n-index identity selector satisfies these integer digit conditions, and every independent nonzero choice of the t_v on its support gives the same Boolean activations and equations. Empty support gives exactly the all-zero field point. Repeated element VALUES do not merge positions; independent position labels are retained. This proves equivalence and exact multiplicity, not just a necessary coordinate condition (S2 LF172–186 and LF249–257).

**Mathematics/dependency verdict:** reconstructed in both directions, with unchanged occurrence count, order, group elements and power carries. No quotient packet flattening, independently chosen central array or unproved actual-word bridge is used.

## 7. Whole degree budget, ANY exponent and characteristic two

Substitution z_v=t_v^(p−1) multiplies degree upper bounds by p−1. The cardinality equations cost at most

`sum_(l=0)^(m−1)(p−1)p^l=p^m−1=n−1`.

The quotient equations cost at most `sum_i(q_i−1)`. The central equations cost at most `q sum_j(r_j−1)`, because only the a-shifted e_j digits are imposed. For positive integer factor lists,

`sum_i(q_i−1)≤product_i q_i−1=Q−1`,
`sum_j(r_j−1)≤R−1`;

the remaining expansion terms in `product(1+(factor−1))` are nonnegative. Empty lists give zero on both sides. Also q≤Q, including q=Q=1 in the empty quotient case. Hence the entire group-coordinate cost is at most

`(Q−1)+q(R−1)≤(Q−1)+Q(R−1)=QR−1=n−1`.

Adding the cardinality equations gives `sum deg f_r≤2n−2<2n−1=L`. This proof treats arbitrary actual cyclic orders, including unequal exponents and central power carries. It divides by neither p nor2 and never discards the characteristic-two case. A quadratic term is paid because q≥2 whenever one can occur, which is valid for EVERY prime. Zero equations may be omitted; they neither alter the solution set nor increase the cost (S2 LF190–218).

**Mathematics/dependency verdict:** complete budget reconstructed, with the strict inequality on the WHOLE system rather than separate block budgets or a selected boundary check.

## 8. Zero-count lemma, proved here rather than imported

For ANY system f_r in L variables over F_p with `sum deg f_r<L`, the polynomial

`I(t)=product_r(1−f_r(t)^(p−1))`

is its common-zero indicator and has total degree `<L(p−1)`. In EVERY monomial some variable exponent e is `<p−1`. If e=0, the complete sum in that variable is p=0 in F_p. If `0<e<p−1`, the polynomial X^e−1 has at most e roots, so it does not vanish on all nonzero scalars. Existence of a scalar u with u^e≠1 follows universally from that root bound. Multiplicative reindexing of the COMPLETE power sum then gives `sum_x x^e=u^e sum_x x^e`, hence that sum is zero.

This is a formal all-field proof: no prime, scalar u, group, order or word is assigned/evaluated as a sanity input. The existential u is used only to prove the universal power-sum identity from the elementary root bound. Factoring a monomial's complete sum by variables makes it zero, so the sum of I is zero. Thus the integer common-zero count C is divisible by p.

In characteristic two the same degree argument ensures some exponent e<1, necessarily0; the e=0 branch already proves the needed cancellation without the other branch. This is a proof for ALL characteristic-two systems under the stated inequality, not a small-group substitution. Empty equation families and zero equations obey the same indicator proof; L is positive (S2 LF222–231).

**Mathematics/dependency verdict:** reconstructed with only Frobenius/Fermat, elementary root bound and finite algebraic summation. No Chevalley–Warning theorem, external zero-count source, group algebra/Jennings import or executed enumeration is required.

## 9. Exact selector congruence and all degenerate cases

By §6 there is exactly ONE empty-support common zero. Every actual original n-index identity selector has EXACTLY `(p−1)^n` field realizations, choosing each nonzero t coordinate independently. No other common zero exists. Therefore the integer count satisfies

`C=1+A(p−1)^n`.

For odd p, n=p^m is odd, so `(p−1)^n≡−1 mod p`. In characteristic two,1=−1, so the same congruence holds for every n. The zero-count lemma therefore gives `0≡1−A`, hence `A≡1 mod p`, and A≥1 because A is a nonnegative integer. This proves the stated exact-count strengthening and the original-order existence result for the ENTIRE claimed class, not merely a positive source-count estimate.

For the trivial group, n=1, every word of the required length has its sole entry identity and its unique one-index selector gives A=1. This is the universally forced theorem subcase; no hand-picked nontrivial group or word is being tested. Equivalently all cyclic coordinate/cardinality equation lists are empty and the same one-variable indicator count is p. Empty quotient or center lists elsewhere use the already stated product conventions; the proof never invents a group realizing arbitrary coefficients. Vanishing commutators, repeated/identity letters and zero alpha,beta,theta,kappa coefficients were retained throughout. In an abelian group d=0 and the entire quadratic carry part is absent; arbitrary central exponent remains covered.

**Mathematics/dependency verdict:** exact selector multiplicity, sign and both support directions reconstructed. There is no odd-prime-only conclusion, false zero denominator, unstated reordering or suppressed arbitrary-exponent case (S2 LF233–257).

## 10. Per-claim verdict and precise original limits

| Claimed interface/result | Mathematics | Dependency/application/trust |
|---|---|---|
| Lemma B cyclic decomposition | Reconstructed, including the homomorphism extension and splitting | Elementary cyclic/order arithmetic, finite induction; no structure classification imported |
| Actual central normal form | Reconstructed and unique | Actual Z and G/Z, not arbitrary realizable data |
| All ordered commutator signs | Reconstructed | Convention `[x,y]=x^(-1)y^(-1)xy` gives the stated positive i>l,u<v term |
| Power carries and conditional division | Reconstructed in BOTH directions | Integer guards stay present; no exponent-p substitution or field division |
| Digit coefficient identity | Reconstructed for every nonnegative integer activation sum | Frobenius/base-p coefficients, no size truncation or computed field table |
| Sharp digit-degree helper | Reconstructed | Actual quadratic q-divisibility pays degree2; q=1 has no quadratic terms |
| Entire field-system actual-word equivalence | Reconstructed | Exactly empty or n actual increasing positions; no relaxed source or lost carry |
| Whole degree budget | Reconstructed for every prime/exponent | Strict total bound <L; empty/zero cases retained |
| Common-zero divisibility | Reconstructed | Complete elementary proof, no external Chevalley–Warning/Jennings input |
| Count A≡1 mod p and proper-class existence | Reconstructed | Exact1+A(p−1)^n, characteristic-two/trivial/repeated cases paid |

**Overall mathematical verdict:** NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE. There is no load-bearing NAMED_NOT_RECONSTRUCTED item in this standalone proof at its explicitly elementary foundations. The proof may be known; no novelty/current-literature/open-status certification is asserted.

**Unpaid original scope:** mixed-prime groups, higher nilpotency class and unrestricted finite groups are not covered. The proper class is NOT a WLOG model; the original all-finite-group ordered Olson problem and old prime-dihedral actual-word residual remain unresolved by this packet. No avoiding word, unrestricted obstruction, source priority or stronger gate is established. The supplied book excerpt has its recorded transcription provenance; page images were not freshly reauthenticated by this reviewer.

## 11. Separate process history and exclusions

This is a NEW separately frozen full A6 assessment, not continuation/repair of w30/w33/w35/w38. S3/S4 preserve the two separate A5 selected-control STOPs; S5/S6 preserve the two separate A6 STOPs. Their private values/outcomes, partial assessments and ALL verdict/confidence/method/source consumers remain HELD/ZERO. Their reading facts are not mathematical reviews. The source's other returned-review status references are not proof premises or a cure of these events. No old A5 body or review result is used to skip a current carry/digit/caller proof.

My ACK specifically retained the old mandatory-v10 Olson mixed-formula display, group/PBW/Kac/Tuscan and other contacts; it did not pretend blind or classify an unknown historical v44-B title by guess. No new material same-A6 contact was recognized from the supplied proof. S7 binds my own Sun selected-index PROCESS MAJOR and ENTIRE post-v3 prime2/3 continuation/ALL consumersZERO. That source/method line is not restarted or used here, even though this proof universally quantifies primes. All other author/reviewer/parent STOP/HOLD/ZERO/exposure/cadence findings persist. No counterfactual clean cognition, source independence or exhaustive-history certification follows from this fresh source reconstruction.

No scientific interpreter/calculator/Eval/CAS/program/enumeration/test/typechecker/solver/replay, selected group/prime/exponent/order/word/control/boundary probe, nested task/modelCLI/paidAPI/newGO, old protected-body lookup, author/external contact, Git/delete/publication/infrastructure action, timer/poll/heartbeat was performed. Universal theorem cases and polynomial coefficient identities above are proofs, not sampled diagnostics. Machine tools were only metadata hash/LF/native clocks; no identity was machine-checked. N4 UNKNOWN with historical child exit unestablished, auxiliary214 STOP and HOLDv2 remain.

Main must itself read the COMPLETE source and this return before adoption. This RETURN is full-scope same-harness WRITTEN support for the proper-class theorem, not formal/kernel, human/configured-family, executable or novelty verification, original Sun/Olson completion, permission to reopen stopped work, final park or round closeout.
