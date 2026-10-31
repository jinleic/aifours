# Addendum 5 — full original-order selectors for every finite prime-exponent class-two group

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 15:19:16 PDT 2026**.
**NEW complete WRITTEN positive group-class candidate. NOT reviewed/adopted, formal/kernel checked or novelty-cleared.**

## 1. Current authority, exact inputs and scope honesty

This is continued work inside the SAME frozen math-2 S1 definition-first release, under Main's standing direction to continue admissible all-variable steps after the priority review.
Only the COMPLETE current S1/S2 packet SHA256 `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788`, read after the actual14:46:50 pre-body ACK, and elementary group/finite-vector-space/polynomial/finite-field facts are inputs.
ALL load-bearing specialized arguments, including the polynomial zero-count lemma and the exact-cardinality digit device, are proved below.
No old Olson proof/candidate/review, held formula, degree/point-mass result, provider, Dimitrov/Mohar source, private selection/confidence guide or scientific computation is an input.
Prior polynomial/group exposure remains disclosed; no blind, clean-cognition or independently unaffected derivation claim.
This packet does not rely on the earlier unadopted addenda as a correctness premise.

The theorem is for an EXACT proper class of original groups, not an ansatz asserted WLOG. It includes nonabelian groups but does NOT cover arbitrary finite groups or the odd-prime dihedral intermediate route.
It may be a known classical consequence of polynomial methods; no novelty, priority or current-literature claim is made.

## 2. Full original-object theorem

**Theorem A.** Let p be ANY prime. Let G be ANY finite group of exponent dividing p with `[G,G]⊆Z(G)` (nilpotency class at most2).
Let n=|G|. For EVERY ACTUAL word

`a_1,…,a_(2n−1)` in G,

there exist ORIGINAL indices `i_1<…<i_n` such that

`a_(i_1)…a_(i_n)=1`.

Moreover, for every nontrivial such G, the number A of n-element index subsets with product1 IN ORIGINAL ORDER satisfies

`A ≡ 1 (mod p)`.

The selections use distinct actual occurrences, not distinct values; arbitrary repeats and identity entries are allowed.
The original all-finite-group problem is NOT claimed solved. This theorem proves its full2n−1/n statement only for the stated group class.

## 3. Actual normal coordinates, with original multiplication retained

First suppose p is odd. Both Z=Z(G) and G/Z are abelian groups of exponent dividing p; viewed additively they are finite vector spaces over F_p.
For Z, scalar multiplication is ordinary powering by a residue modulo p. For G/Z the same construction is well-defined because the quotient is abelian and exponent divides p.
Choose ANY bases: z_1,…,z_c for Z, and a quotient basis with ANY actual lifts h_1,…,h_d∈G.
Then

`|G|=p^(d+c)`. Put `m=d+c`, so `n=p^m`.

Every actual group element has a UNIQUE normal expression

`h_1^(x_1)…h_d^(x_d) z_1^(y_1)…z_c^(y_c)`,

with x∈F_p^d, y∈F_p^c.
Existence follows by matching its quotient coordinates and then its remaining central element. Uniqueness follows first in G/Z and then in the chosen central basis.
This is a coordinate theorem for EVERY group in the stated class, not a chosen multiplication table or special presentation.

Use commutator convention `[u,v]=u^-1 v^-1 u v`.
All commutators are central. Define ACTUAL coefficients κ_(ij,l) by

`[h_i,h_j]=product_l z_l^(κ_(ij,l))`.

The swap identity `uv=vu[u,v]`, with central commutators, gives by induction
`h_i^a h_j^b=h_j^b h_i^a [h_i,h_j]^(ab)`.
Because each h_i has exponent dividing p, combining equal-basis powers introduces NO extra central carry when their exponents are reduced modulo p.
Thus multiplying two normal-coordinate elements gives EXACTLY

`(x,y)(x',y')=(x+x', y+y'+Φ(x,x'))`,

where the ACTUAL bilinear map is

`Φ_l(x,x')=sum_(i>j) κ_(ij,l) x_i x'_j`.

Indeed each right-factor h_j power moves left past precisely the higher-index left-factor h_i powers; those swaps give the stated ordered bilinear contribution. All z_l are central.
No arbitrary bilinear map is assumed realizable, and no physical word is replaced by free coefficient data: Φ is derived from the given ACTUAL G and its chosen lifts.

Write the ACTUAL input letter a_v as coordinates (α_v,β_v).
For ANY selected index set S, with indicator z_v∈{0,1}, induction using this multiplication law gives its ORIGINAL-order product coordinates

`X_S = sum_v α_v z_v`,

`Y_S = sum_v β_v z_v + sum_(u<v) Φ(α_u,α_v) z_u z_v`.

The strict u<v is the ORIGINAL occurrence order. This formula does not permit reordering the selected letters; it explicitly pays the noncommutative multiplication through its actual central term.
The product is identity IFF EVERY displayed coordinate is zero, by uniqueness of normal form.

## 4. Elementary finite-field zero-count lemma, proved here

**Lemma B.** For polynomials f_1,…,f_r over F_p in L variables, if

`sum_j deg(f_j) < L`,

the INTEGER number of their common zeros in F_p^L is divisible by p.
A zero polynomial may be omitted; it does not increase the degree bound.

**Proof.** For any nonzero a∈F_p, multiplication by a permutes F_p^×. Multiplying its nonzero elements and cancelling proves `a^(p−1)=1`; thus t^(p−1) is0 for t=0 and1 otherwise.
The polynomial

`H(t)=product_j (1−f_j(t)^(p−1))`

is therefore the indicator, in F_p, of simultaneous vanishing.
Its total degree is strictly less than L(p−1).
Every monomial in H consequently has SOME variable with exponent e satisfying0≤e<p−1.
If e=0, summing that variable contributes p=0 in F_p.
If0<e<p−1, the polynomial X^e−1 has at most e roots, so some nonzero a has a^e≠1. Scaling the field summation variable by a shows `sum_t t^e=a^e sum_t t^e`, hence that sum is0.
Thus every monomial's complete field sum is0, and so is the complete sum of H.
That sum is the common-zero count reduced modulo p. ∎

Only the elementary polynomial root bound was used; it follows by repeated linear-factor division. No cyclic multiplicative-group theorem, external Chevalley–Warning proof, interpreter, enumeration or zero-count computation is imported.
The finite sums in this proof are symbolic universal identities, not an executable traversal of a finite field.

## 5. Exact cardinality n, not just cardinality modulo p

For the moment assume n=p^m with m≥1 and let L=2n−1, the ORIGINAL input length.
For each input occurrence v introduce a field variable t_v and the Boolean-valued expression

`z_v=t_v^(p−1)`.

For j=0,…,m−1 define the polynomial

`D_j(t)=σ_(p^j)(z_1,…,z_L)`,

where σ_q is the elementary symmetric polynomial of degree q. Its degree as a polynomial in t is at most `(p−1)p^j`.
This is a universally defined polynomial, not a generated/enumerated object.

At a field assignment, let S={v:t_v≠0} and let w=|S| as an INTEGER.
Then

`D_j(t)=binomial(w,p^j) mod p`.

To see exactly what these equations impose, write the base-p digits of w as w_i.
In F_p[T], the binomial theorem and Frobenius give

`(1+T)^w = product_i (1+T^(p^i))^(w_i)`.

The coefficient of T^(p^j) in this product is w_j: all lower-digit factors have total degree at most p^j−1; higher-digit factors cannot contribute; and the j-th factor contributes its linear term exactly once.
Therefore `binomial(w,p^j)≡w_j (mod p)`.

Consequently ALL D_j=0, j<m, holds IFF the lower m digits of w vanish, IFF n divides w.
Since0≤w≤L=2n−1, this means

`w=0 OR w=n`,

with NO other cardinality allowed.
This is the essential actual-cardinality coupling. A single equation w≡0 mod p would NOT suffice, and is NOT substituted here.
The total degree cost of all digit equations is bounded by

`sum_(j=0..m−1) (p−1)p^j = p^m−1 = n−1`.

## 6. Odd p, all groups with m≥2: full polynomial system and strict degree bound

Use the ACTUAL coordinates from §3 and substitute z_v=t_v^(p−1).
Impose all digit equations D_j=0 from §5, all d coordinates of X_S=0, and all c coordinates of Y_S=0.
Each quotient coordinate polynomial has degree at most p−1; each central coordinate polynomial degree at most2(p−1).
The sum of degrees of the WHOLE system is therefore at most

`(n−1)+(d+2c)(p−1) ≤ (n−1)+2m(p−1)`.

For EVERY odd prime p and EVERY m≥2,

`2m(p−1) < p^m = n`.

Here is a symbolic proof, not a spot check. At m=2,
`p²−4(p−1)=(p−2)²>0`.
If the inequality holds at m, multiplying its right side by p gives a strict bound larger than2(m+1)(p−1), since pm≥m+1 for p≥3,m≥2.
Induction proves it for all m≥2.

Hence the degree sum is STRICTLY LESS than

`(n−1)+n=2n−1=L`.

LemmaB applies: the total number C of common zeros is divisible by p.
By §5, every common zero has support size0 or n.
By §3, at support size n the coordinate equations hold IFF its ACTUAL original-order group product is1.
Thus there are NO formal unrealizable support solutions or reordered products in this counting argument.

## 7. Zero count to ACTUAL original selectors and the count congruence

There is exactly ONE empty-support assignment: all t_v=0. It satisfies the complete system.
For each actual n-element original index subset S with product1, there are EXACTLY `(p−1)^n` field assignments giving that support, independently choosing each of its nonzero t_v.
The equations depend only on z, so either all these assignments satisfy them or none do.
Consequently the INTEGER common-zero count is exactly

`C = 1 + A(p−1)^n`,

where A counts the ACTUAL desired original-order n-subsets.
For odd p, n=p^m is odd, so `(p−1)^n≡−1 (mod p)`.
LemmaB's C≡0 therefore gives

`A≡1 (mod p)`.

In particular A≥1: a true n-element ORIGINAL-order identity selector exists.
This proves BOTH the existence assertion and the stated count congruence in the odd-p,m≥2 case.
The noncommutative pair terms in §3 were kept throughout; they were not discarded because a quotient product vanished.

## 8. All remaining cases, including characteristic2 and the trivial group

**Trivial G, n=1.** Its only actual letter is identity and the required single-occurrence selection is immediate. No field construction is needed.

**Odd p, m=1.** A nontrivial group of order p and exponent dividing p is cyclic: any nonidentity element has order exactly p and fills the group.
There is one ACTUAL additive coordinate over F_p, and the selected product coordinate is LINEAR in the z_v, not quadratic.
The degree cost is therefore

`(n−1)+(p−1)=2p−2 < 2p−1=L`.

The SAME digit equations, LemmaB and support-count proof yield A≡1 mod p and the required original selector. No m≥2 inequality is misapplied.

**p=2, every nontrivial case.** Exponent dividing2 forces G abelian: `ab=(ab)^-1=b^-1a^-1=ba`.
Hence G is a finite F_2-vector space of some dimension m≥1 and n=2^m.
Its actual selected product has m LINEAR Boolean coordinate equations; the total degree cost is

`(n−1)+m < 2n−1=L`,

because m<2^m for every m≥1. This follows from the base1<2 and induction `m+1≤2m<2^(m+1)`.
LemmaB again gives C≡0 mod2. Each n-support assignment has `(p−1)^n=1` realization, so C=1+A and A≡1 mod2.
The full original selector follows.

These cases exhaust every prime, every finite group in the stated class and every possible order. The nonabelian part is necessarily in the odd-prime case, but no nonabelian group is replaced by an abelian model in that proof.

## 9. Forward and converse actual-object caller

**From a field zero to the original object:** digit equations force support size0 or EXACTLY n; nonempty support has increasing actual occurrence indices; the ACTUAL normal-form multiplication equations force its product in THAT order to be identity. This supplies the original selector, not a polynomial witness alone.

**From an original selector to field zeros:** for any n-index original-order identity selector, every choice of nonzero t_v on those indices and zeros elsewhere satisfies ALL digit and ACTUAL group coordinate equations. This proves the exact count formula, not merely one inclusion.

**Why existence follows:** the empty assignment is only one zero. If no actual selector existed, C would be1, contradicting LemmaB's divisibility. Repeats, identity letters, vanished coordinates, degenerate commutator coefficients and zero-dimensional quotient/central coordinate blocks are all permitted; omitting zero polynomials only lowers the degree cost.
No particular basis, field tuple, group example, numerical state, boundary sample or selected word was evaluated to test viability.

## 10. Exact scientific change, imports and nonclaims

This candidate proves the FULL original2n−1/n ordered assertion for EVERY finite group of prime exponent and nilpotency class at most2, including every ACTUAL word and every original occurrence pattern. It is not a proper word ansatz treated as WLOG.
The additional mod-p count statement is also at that full group-class/word scope.
It is a round-level positive GROUP-CLASS theorem candidate, not merely another obstruction or encoding.
It may already be known; no novelty or publishability is inferred from this derivation.

It does NOT cover groups of composite exponent, arbitrary nilpotency class, arbitrary solvable or arbitrary finite groups. In particular an odd-prime dihedral group is not silently inserted into this prime-exponent class, and the old prime-dihedral intermediate actual-word gap is not declared closed.
The original all-finite-group question remains unresolved beyond the explicitly proved class.
No source/priority/openness authentication beyond the supplied literal is claimed.

Ordinary inputs explicitly used: finite abelian exponent-p groups as F_p-vector spaces and basis existence; group quotients and central commutator swaps; elementary finite-field arithmetic; the polynomial root bound; binomial/Frobenius identities; ordinary integer base-p expansion, counting and induction. Every specialized bridge, the zero-count lemma and the exact-cardinality consequence are proved inline.
No source-original Chevalley–Warning, Jennings/group-algebra theorem, old polynomial proof, unreplayed computation or external paper is named as a correctness premise.

All earlier candidates remain immutable. This needs a NEW full-source mathematics AND dependency/application review and Main's complete source/actual-return reads before any adoption.
Prior exposure is not erased. Every STOP/HOLD/ZERO outside S1, all nine held formulas/consumers, v214-A/threshold/v227 restrictions, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and prior process findings persist.
No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or timer/heartbeat loop.
This is WRITTEN/same-harness, not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/new exclusive append-only root/actual20min substantive cadence and honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE PRIME-EXPONENT CLASS-TWO SELECTOR PROOF.**
