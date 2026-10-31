# Shor raw completion — signed polynomial certificate sufficiency, fully reconstructed

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 05:35:38 PDT 2026** (earlier observation bound). WRITTEN/unreviewed. Exact symbolic variables, fractions and integer products only. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

This strengthens the POSITIVE direction of `shor-raw-signed-factor-top-layer-and-gap-balance-v1.md` (SHA2569dadb66e…ee14b). That packet cautiously used I5 for both directions. The sufficiency direction is now completely proved below from elementary formal-series support and finite-word counting. Only the converse existence of signed factors for EVERY finite complete code retains the named external I5 boundary. No actual certificate is exhibited.

Source read: Berstel–Reutenauer, *Noncommutative Rational Series With Applications*, author-hosted2010draft, Chapter11 Lemmas2.2–2.3/Theorem2.4 and Theorem2.7/proof, pp191–195 in the printed pagination, at http://www-igm.univ-mlv.fr/~perrin/Livres/RationalSeries9April2010.pdf . The raw argument below supplies every operative step and explicitly corrects the text-extraction loss of a not-equal sign in the ambiguity argument. The much longer Chapter11§4 NECESSITY proof is NOT_RECONSTRUCTED here.

## 1. Complete literal theorem

Let P,S be FINITE polynomials in Z<a,b> and suppose

    F=1+P(a+b−1)S

has nonnegative integer coefficients and zero empty-word coefficient. Then:

1. every coefficient of F is0 or1;
2. M=supp(F) is a FINITE RAW UD code;
3. EVERY binary word is a factor of M*.

Thus if F additionally contains every literal Shor word, M is an ACTUAL finite completion. There is NO remaining PR/isolated-word/delay/STAB realization obligation after an actual such finite pair is supplied and its coefficient conditions proved. No degree, b-count, a-gap, cardinality, n, symmetry or numerical margin bound is imposed.

P,S need not be nonnegative. This is not the positive-factorization conjecture, not a statement about a residue code and not a finite-state span being renamed raw stabilization.

## 2. Signed formal support gives actual factor-completeness BEFORE UD is known

The empty coefficient condition gives P(empty)S(empty)=1, so both factors are invertible in the formal noncommutative series ring. F is proper, so F*=sum_(k>=0)F^k is a well-defined formal series with NONNEGATIVE coefficients. The identity is

    1−F=P(1−a−b)S.

Inverting and multiplying on the correct sides gives

    (1−a−b)^(-1)=S F* P.                                (SUPPORT)

The series on the left has coefficient1 at EVERY binary word. A nonzero coefficient of a product implies at least one nonzero product term in its coefficient sum; possible signed cancellations do not change that implication. Thus for every word w there are x in supp(S), y in supp(P) and m in supp(F*) with w=x m y. Since F is nonnegative and proper, supp(F*)=M*: a middle coefficient is positive exactly when some finite list of support words concatenates to it. No UD assumption is used here.

Let d exceed BOTH maximum lengths of support words of P and S. For ANY desired raw word v, apply SUPPORT to a^d v a^d. The selected x,y have lengths below d, so removing them from the two ends leaves a middle word m that STILL contains the ENTIRE v as a factor. Hence v is a factor of M*. M is therefore factor-complete. This is literal padding in the free monoid, not cancellation of a^n inside an arbitrary submonoid.

## 3. Elementary Bernoulli mass facts, including non-UD languages

Fix symbolic0<t<1 and let mu(a)=t,mu(b)=1−t, extended multiplicatively to words. For a language L, mu(L) is the nonnegative sum of its word weights. Every fixed word length contributes total mass1, so mu({a,b}*) is infinite. Countable subadditivity and mu(XY)<=mu(X)mu(Y) hold even for ambiguous products.

### 3.1 A FINITE complete language has mass at least1

Let C be a finite nonempty language without the empty word, and suppose every word is a factor of C*. Its finite maximum word length L gives a finite-cover identity

    {a,b}* = R C* T union E,

with R,T finite collections of proper suffixes/prefixes of C and E a finite set of words contained entirely inside one codeword. This is only a cover; it need not be disjoint or uniquely parsed. It follows by cutting an occurrence of a desired word at the first/last full C-word boundary. Completeness gives the forward inclusion; the reverse inclusion is automatic.

If mu(C)<1, then mu(C*)<=sum_(k>=0)mu(C)^k<infinity, even without UD. The displayed finite cover would make the mass of ALL words finite, contradiction. Therefore mu(C)>=1.

### 3.2 A FINITE complete language of mass1 is UD

Let C be finite complete and mu(C)=1. For EVERY positive integer m, C^m is again complete: embed a desired word in some C-product and append enough C-words to make the number of factors a multiple of m. Applying3.1 to C^m gives mu(C^m)>=1. Subadditivity over the C-tuples gives mu(C^m)<=mu(C)^m=1. Thus equality holds.

Suppose C had two distinct finite parses of the SAME word. Cancel their common initial C-words AS LISTS. Both remaining lists are nonempty, and their first C-words differ: one remaining list cannot be empty because all C-words are nonempty. Call the remaining lists U and V, of lengths r and s, with equal raw concatenation w. The lists UV and VU have the same number r+s of C-words, the same raw concatenation ww, and DIFFERENT first C-words. Hence one word in C^(r+s) has at least two tuple preimages of positive weight.

Consequently mu(C^(r+s)) is STRICTLY LESS than the sum of the weights of all(r+s)-tuples, namely mu(C)^(r+s)=1. This contradicts equality above. Therefore C is RAW UD. Different word lengths and heterogeneous delays were never restricted.

## 4. Nonnegative INTEGER coefficients force characteristic coefficients

Evaluate the finite signed identity at the formal Bernoulli weights. Since t+(1−t)−1=0,

    mu(F)=1.

Let M=supp(F). Coefficients of F are positive integers on M, so mu(M)<=mu(F)=1. Section2 proves M complete, so3.1 gives mu(M)>=1. Thus equality holds. If any coefficient of F exceeded1, its strictly positive word weight would make mu(F)>mu(M), impossible. Therefore F is a0/1 characteristic polynomial.

Now3.2 applies to finite complete M of mass1 and proves UD. This establishes every assertion of§1 without assuming Reutenauer's converse, a factorization conjecture, prior kernel computation or a selected raw completion protocol.

The nonempty support needed in§3 follows automatically: if F=0 then P(a+b−1)S=−1, impossible for finite nonzero polynomial factors, since the top homogeneous degree of the left product is deg(P)+1+deg(S)>0 in the free algebra. Equivalently SUPPORT with finite outer supports cannot cover words of arbitrary length if M*={empty}.

## 5. Exact updated trust boundary and remaining science

**Positive direction, now self-contained:** an ACTUAL finite signed pair P,S with F>=0, no empty coefficient and literal C inclusion directly certifies finite RAW UD factor-completeness by§§2–4. Nonnegativity is an ALL-word coefficient condition for the finite F, not an empirical test or a request for execution. No such pair has been found.

**Negative direction:** to transfer an all-pairs obstruction to EVERY hypothetical finite completion, the existence of finite signed factors still uses named I5 (Reutenauer's converse). Its published statement has been read; its full noncommutative-factorization proof, including weak-algorithm/inertia/Gauss/minimal-ideal antecedents, is NOT_RECONSTRUCTED here. The sufficiency result above is not a claim those missing proofs were read or accepted.

The elementary TOP/PEN/BAL constraints, forced NEG14, all-degree one-sided obstruction and positive-orthant/top-sign theorem remain exact raw restrictions at their algebraic hypotheses. They are NOT a proof that the remaining two-sided signed factors fail or that a finite repair cascade terminates. The genuine next step is a Shor-specific contradiction covering ALL finite two-sided signed factors, or an actual finite pair meeting every coefficient condition.

No residue closure, canonical first-return graph, positive rational potential, near-unit Kraft limit, boundary-dimension stabilization, H* (FALSE/WITHDRAWN), commutative-prefix/factorization conjecture or finite-depth miss substitutes for that missing step. All original word lengths/arities/b-counts/delays/orders remain unbounded. Original Shor completion is **NOT_PROVED** in either direction.

Own permanent v109-A exactness MAJOR/all earlier process findings remain. No source/shared/frozen edit, git/deletion/publication, scientific GO or stronger formal/kernel/human/configured-family/executable/novelty acceptance. Original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 unchanged; no early final park.
