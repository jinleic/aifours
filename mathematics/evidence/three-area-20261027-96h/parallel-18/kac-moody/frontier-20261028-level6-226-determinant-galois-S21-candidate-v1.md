# The degree-21 determinant factor has generic Galois group S21 — exact candidate

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:56:25 PDT 2026**. New exact finite-field/group-theoretic candidate, UNREVIEWED; not parent/formal/kernel, independent-model/human, novelty or priority acceptance. Its role is to sharpen the polynomial interface used in the separate density-one candidate; it does not by itself prove every Serre map.

## 1. Exact statement and source boundary

Let `R(X,Y)` be the explicit 253-term integer factor of the actual level-six `(2,2,6)` determinant in `frontier-20261028-level6-226-generic-density-one-candidate-v1.md`, 61LF SHA `8a4ac80a3131f3ddcdc8568da32a5fafe10dea1bda823f7bc52100a640d41d38`. It has degree21 in Y and constant leading coefficient `c=2107392`. Let

\[
f(X,Y)=R(X,Y)/c\in\mathbb Q[X][Y].
\]

At the exact pinned integer/finite-field and named classical Frobenius/specialization inputs below, the candidate is

\[
\operatorname{Gal}(f(0,Y)/\mathbb Q)\cong S_{21},\qquad
\operatorname{Gal}(f(X,Y)/\mathbb Q(X))\cong S_{21}.
\]

Both are groups of permutations of the 21 roots, not claims about a Galois group of the entire Kac–Moody algebra. The determinant/source, full Cartan, ideal and PBW conditions of the prior paper remain required for applying this polynomial to the original map. The quantitative Hilbert irreducibility theorem in that paper then has the concrete generic group S21; its existing density-one conclusion and stated classical-import boundary are not strengthened to every parameter pair.

## 2. Three independently checked Frobenius cycle patterns

All primes below are prime, do not divide c, and the indicated monic reductions have distinct irreducible factors. The finite-field coefficient arrays and exact Frobenius/Bézout data are pinned below.

|prime|factor degrees of monic f(0,Y) mod p|cycle type supplied by Dedekind|
|---:|---|---|
|61|21|a 21-cycle|
|467|1,20|a 20-cycle fixing one point|
|59|2,19|a disjoint 2-cycle and 19-cycle|

At p61 the complete Rabin test `Y^(61^21)=Y mod F`, plus the Bézout gcd1 tests for exponents `61^7` and `61^3`, was independently replayed in the prior density-one paper. For p59, the new source verifies exact product and coprimality of a degree2 factor and a degree19 factor; their irreducibility follows from their complete respective Rabin/Frobenius and Bézout tests. For p467 it similarly verifies a degree1 factor and an irreducible degree20 factor, with the degree20 prime-divisor checks at powers4 and10. The pairwise Bézout identities establish squarefreeness. Thus these are exact cycle-pattern certificates, not a heuristic modular factor table.

The factors in ascending coefficient order are:

    p59 degree2:  [18,33,1]
    p59 degree19: [56,50,17,40,15,13,53,52,20,17,11,22,50,56,55,25,11,4,54,1]
    p467 degree1:  [262,1]
    p467 degree20: [182,289,24,355,102,149,306,127,149,100,80,249,418,318,448,356,290,92,46,28,1]

The p61 21-term-degree monic polynomial and its two explicit Bézout certificates are in the prior generic-irreducibility data; no factor is assumed irreducible just from its displayed degree.

## 3. Exact group-theoretic proof, with the correct integral polynomial

Because f(0,Y) is monic rational, we may apply the standard monic-integer theorem without assuming its rational coefficients are algebraic integers. Define

\[
g(Z)=c^{20}R(0,Z/c)\in\mathbb Z[Z].
\]

It is monic of degree21 and has the SAME splitting field over Q as f(0,Y). Since each of 59,61,467 is coprime to c, scaling `Z=cY` is invertible modulo p and preserves the factor degrees and squarefreeness verified above. The named Dedekind/Frobenius factorization-cycle theorem therefore supplies elements of its Galois group with the three listed cycle types. A precise public statement is [Keith Conrad, *Galois Groups over Q and Factorizations mod p*, Theorem 1](https://kconrad.math.uconn.edu/blurbs/gradnumthy/galois-Q-factor-mod-p.pdf); that theorem is a named classical input, not newly proved or locally byte-pinned here.

The 21-cycle makes the specialized Galois group transitive. A 20-cycle fixing one point lies in that point stabilizer and is transitive on the other20 points, so the group is **2-transitive**. Raising the `(2)(19)` element to the 19th power gives a transposition. By 2-transitivity, conjugation supplies every transposition; they generate S21. Thus the specialized group is exactly S21.

The generic polynomial f is monic and irreducible over Q(X), as proved in the earlier mod61/monic-specialization candidate. Its discriminant does not vanish at X=0 because its p61 reduction is squarefree. The standard good-specialization theorem embeds the specialized Galois group in the generic Galois group, up to conjugacy; see [Zywina, *Hilbert's irreducibility theorem and the larger sieve*, §1.1](https://pi.math.cornell.edu/~zywina/papers/Quantitative-HIT.pdf). Since the subgroup is already S21 and the generic group is a subgroup of S21, the generic group is S21. This is a named classical specialization import; no external theorem proof or source bytes were independently pinned here.

## 4. Exact certificates and limits

|Owner-root artifact|LF|SHA-256|
|---|---:|---|
|`frontier-20261028-level6-226-galois-cycle-certificate.py`|66|`53070a9ccb2e877e346609b9a854fed6df1bca001e8194f74c2b235afcd5dd14`|
|`frontier-20261028-level6-226-galois-cycle-certificate-v1.json`|423|`c4b1dd6e83344cf03d19eb29a915ed51c1f81d20a31d9f7aa4c436fd8a1be884`|
|`frontier-20261028-level6-226-galois-cycle-independent-replay.py`|49|`9cc892caf1e02bcf40d54a0f10b4376d88aa24bb3b31d8f219a17330616f277a`|
|`frontier-20261028-level6-226-galois-cycle-independent-replay-v1.json`|22|`a507a2aa845d87a17da0e42338d27b7f24984c570f79f3b5c718de02a58f3c68`|
|prior full integer/Rabin61 replay `frontier-20261028-level6-226-generic-irreducibility-independent-replay-v1.json`|14|`177815daf9f790e91dc2677388c425ef3e4026db91533bfc404839342381fc1c`|

The producer returned `PASS p59 irreducible factor degrees2+19 and p467 degrees1+20, all Rabin/Bezout/product identities` at **19:55:20 PDT**. The separate replay used plain integer finite-field multiplication, polynomial division, modular powering and Bézout identities and returned PASS at **19:55:43 PDT 2026-10-28**. It independently checks the finite-field arithmetic, not Dedekind's theorem, group-theoretic deduction, generic specialization or an actual Serre proof. All current and prior mathematical/source/code steps need full independent review before adoption.

The p61 specialization and generic-density-one result are preexisting within this current work; this S21 identification is a new candidate property of its selected determinant factor, not evidence of a full-quadrant map, F6/B6, arbitrary-GCM/all-level theorem, novelty or priority. Prior incidental older cone-status methodological exposure and all ZERO/STOP/HOLD/process qualifications remain unchanged.

**END — exact S21 candidate for the specified degree-21 determinant factor, review pending.**
