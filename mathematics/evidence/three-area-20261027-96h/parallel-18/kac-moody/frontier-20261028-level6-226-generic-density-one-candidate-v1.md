# Generic irreducibility gives a density-one level-six type125 candidate

**MathKacMoody-2 / math-3.** Native observation before this additive write: **Wed Oct 28 19:50:07 PDT 2026**. New exact-computation + named quantitative-Hilbert-irreducibility argument, entirely UNREVIEWED; not parent adoption, formal/kernel, human, independent-model, priority or novelty acceptance.

## 1. Exact asymptotic claim and its boundaries

For `r,s>=6`, let `S=G_C/J` be the original Serre quotient for ANY allowed FULL complex Cartan realization C of A(r,s), and let `P_(2,2,6)=ker f1 intersect ker f2` in that actual degree. At the named UNREVIEWED full-Cartan/free-Levi/PBW and full 34×34 determinant inputs in the previously replayed strip candidate `frontier-20261028-level6-226-gap41-strip-candidate-v1.md`, SHA `a9d70a2b7da3b93056999cff6771997593e78d2d4cc12a3ac46a33d094f75f40`, plus the exact finite-field certificate and the NAMED classical quantitative Hilbert irreducibility theorem below, the candidate is:

> For all but `O(sqrt(N) log N)` integers r in `[6,N]`, the ENTIRE original D3 map `P_(2,2,6) -> S_(2,2,5)` is injective for **every** integer `s>=6`. Consequently the set of proven-injective parameter pairs has natural density 1 in expanding squares `6<=r,s<=N`, with at most `O(N^(3/2) log N)` pairs not certified by this argument.

The implicit constant depends on the explicit polynomial below and is NOT made effective here. Exceptional r rows may be infinite, and their maps may still be injective. This is NOT a proof of every r,s>=6, a finite-box bound, another level-six type, F6/B6, arbitrary-GCM/all-level Serre, a non-Serre witness, global novelty or priority. The previous >99.4%-density finite-modulus subset remains a separate **constructive** result; this density-one theorem has a stronger explicitly named classical theorem import and is not a finite residue-table claim.

## 2. The exact 21-degree polynomial

With `x=r-6,y=s-6`, the previously independently replayed actual 34×34 source determinant `P(x,y)` factors exactly as

\[
P(x,y)=393216\,(x+5)^4(y+5)^7(2x+2y+19)^2 R(x,y).\tag{1}
\]

Here `R` is the explicit **253-term integer polynomial** in the pinned certificate below, of total degree21 and degree21 in y, whose leading y coefficient is the nonzero CONSTANT

\[
[y^{21}]R=2107392.\tag{2}
\]

All three displayed nonconstant factors are strictly positive for x,y>=0. The previous independent integer convolution established the factors through the intermediate 341-term Q; the new independently authored plain-integer replay checks the additional identity `Q=(x+5)^4 R` coefficient-by-coefficient, including all341 Q coefficients, and verifies (2). Hence `R(x,y) != 0` implies the actual full-size D3 minor is nonzero; no determinant positivity or full-map nullity outside that implication is assumed.

## 3. Exact finite-field and generic irreducibility proof

Reduce `R(0,Y)` modulo61 and divide by its leading coefficient `2107392 ≡ 25 (mod 61)`. The resulting monic degree21 polynomial `F in F_61[Y]` has coefficients LOW-to-HIGH

    1,20,58,51,8,13,4,26,7,46,44,4,12,36,45,15,31,39,55,32,43,1.

The complete exact Rabin irreducibility certificate verifies

\[
Y^{61^{21}}\equiv Y\pmod F,
\quad \gcd(F,Y^{61^7}-Y)=1,
\quad \gcd(F,Y^{61^3}-Y)=1.\tag{3}
\]

The certificate includes explicit Bézout polynomials for both gcds. The two prime divisors of 21 are 3 and 7, so the standard finite-field irreducibility criterion makes F irreducible over F61. Its degree is preserved because 25 is nonzero mod61; Gauss' lemma therefore makes `R(0,Y)` irreducible over Q.

Set `f(X,Y)=R(X,Y)/2107392`. It is monic of degree21 in Y with coefficients in Q[X]. If f factored into positive Y-degree factors over Q(X), Gauss' lemma over the UFD Q[X] would supply monic factors in Q[X,Y]. Specialization X=0 would preserve their positive Y degrees and factor f(0,Y), contradicting irreducibility. Thus **f is irreducible over Q(X)**. Characteristic0 then makes it separable, so its discriminant is a nonzero polynomial in X and has only finitely many integer zeros. No computation for a selected integer row is used to infer all rows: the monic-specialization argument is essential.

## 4. Explicit named quantitative theorem and density argument

We use the following named classical input: the integral quantitative Hilbert irreducibility theorem, for a fixed monic irreducible separable `f(X,Y) in Q[X,Y]` of degree at least2 in Y, says the number of integer `0<=x<=N` for which `f(x,Y)` is reducible over Q is `O_f(sqrt(N) log N)` (with finitely many discriminant exceptions included). One source stating the stronger Galois-group version is David Zywina, *Hilbert's irreducibility theorem and the larger sieve*, [Theorem 1.2, pages 1–2](https://pi.math.cornell.edu/~zywina/papers/Quantitative-HIT.pdf): specialize its `k=Q,n=1`; transitivity of the generic Galois group then makes equal-specialized-group cases irreducible. That external theorem is a **named imported input**; this paper does not prove it, authenticate its complete transitive source chain, or claim formal verification.

For any x outside the reducible/discriminant exception, `f(x,Y)` is an irreducible degree21 polynomial over Q and therefore has no rational, hence no integer, root y. Thus `R(x,y) != 0` for EVERY integer y, and (1) gives nonzero actual minor for every s>=6. There are only `O(sqrt(N) log N)` uncertified x in `[0,N-6]`, each paired with at most N values of s, so at most `O(N^(3/2) log N)` square pairs are missed. Dividing by the `~N^2` pairs gives density1. This bounds the **complement of a specified sufficient proof condition**, not the number of actual D3 kernels. No existence of a kernel on any exceptional row follows.

## 5. Exact certificate, independent replay, and process

The producer `frontier-20261028-level6-226-generic-irreducibility-certificate.py`, 60LF SHA `08c9052bd0afa77e03dfd788fc812d1fa07de251ca0de4c1460e5be38fdef47e`, records the exact Q→R division, all253 coefficients of R, constant leading coefficient, F61 polynomial, the three Frobenius remainders and both Bézout identities in `frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json`, 1448LF SHA `5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297`.

The separately authored `frontier-20261028-level6-226-generic-irreducibility-independent-replay.py`, 84LF SHA `de5916add76549d24e62a477d3de523d0b6a55f12b6b763e0d26cea3451e607f`, reconstructs `Q=(x+5)^4 R` by plain integer convolution and implements finite-field polynomial multiply/divide/exponentiation from scratch, checking the entire monic specialization, all three Frobenius remainders and both Bézout identities. Its 14LF output `frontier-20261028-level6-226-generic-irreducibility-independent-replay-v1.json`, SHA `177815daf9f790e91dc2677388c425ef3e4026db91533bfc404839342381fc1c`, returned `PASS integer Q factor, degree21 constant leading, F61 Frobenius3/7/21 and both Bezout identities` at **Wed Oct 28 19:49:44 PDT 2026**. This is same-owner exact computation with shared input data, not independent-model/human/formal proof.

The separately replayed source determinant/ideal and the named quantitative theorem are essential gates; a reviewer must reconstruct their exact application, not just the irreducibility header. The Cornell-hosted theorem was read as a public source during this work; its page text is linked above but its remote bytes were not pinned locally, and no external theorem proof was checked. Earlier incidental older cone-status methodological exposure and all ZERO/STOP/HOLD/process findings remain unchanged. No H13/old19, B4/F5, arbitrary-GCM or all-level claim is added.

**END — density-one candidate at explicit exact determinant, Rabin and named quantitative-HIT inputs; independent review pending.**
