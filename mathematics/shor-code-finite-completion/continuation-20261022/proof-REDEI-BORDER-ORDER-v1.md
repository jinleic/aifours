# Shor completion: a sourced Rédei route to the order restriction

Before-creation clock observed: **2026-10-22T22:47:17-0700**. Draft reasoning started earlier; this is not an exact creation instant. Status: **CANDIDATE written consequence of an explicitly imported literature theorem**. No new priority, full finite-completion solution, formal verification or two-family acceptance is claimed.

## 1. Exact result and what changes

Let M be a hypothetical finite uniquely decipherable complete code over {a,b} containing the exact 16-word Shor code in `../source/problem.zh.txt`. Let a^n be its unique pure a-power codeword. At the inherited completion-to-factorization and 8-divisibility interfaces below, and the precise Rédei lemma stated in section 2, the written conclusion is:

> Write n=1320m. Then m has at least **two distinct odd prime divisors**. In particular n≥19800.

This is a necessary condition, not a construction, a sufficient condition, a proof that 19800 is attainable, or an all-order noncompletion result. It excludes all n=1320·2^a·r^b with a,b≥0 and r an odd prime, including b=0, for every choice of those parameters. The nonnegative-exponent family is a symbolic consequence, not a finite search or enumeration.

The old dossier gave n≥19800 conditionally on an unauthenticated transcription of Szabó2006 Theorem7. This manuscript supplies another argument using an actually opened, precisely stated lemma in Cordero2023. It does **not** authenticate the 2006 article or independently prove the imported Rédei theorem. No claim is made that this lower bound or its application is new; it may reproduce the very argument behind Szabó's result.

## 2. Exactly declared inputs and source boundary

### Rédei input (R2)

For a normalized direct factorization P⊕Q=Z_n, if the cardinality |P| involves at most two distinct primes, at least one of the generated subgroups ⟨P⟩,⟨Q⟩ is proper in Z_n. Equivalently, if both factors generate Z_n, then |P| has at least three distinct prime divisors. The same applies to |Q| by exchanging the factors.

This is the literal content of **Cordero, _Factorizations of Cyclic Groups and Bayonet Codes_, arXiv2301.13566v1, Lemma5.2**. The lemma writes |P|=p^αq^β with α,β≥0, so it includes one-prime and trivial cardinalities. Its exact HTML MathML was opened and checked, not inferred from a search summary or a PDF's lost inequality glyph. It explicitly attributes the lemma to Szabó–Sands, _Factoring Groups into Subsets_ (2009), Theorem5.5.

- Primary statement: https://arxiv.org/html/2301.13566v1#S5.Thmtheorem2
- Author-hosted primary representation, printed p.17: https://www.normalesup.org/~cordero/Publications/Factorizations_and_Bayonet_Codes.pdf
- Retained text: `../sources/cordero2023.txt` LF815–817; whole SHA256 `c2cc3649b9b9ad36a3b563b2a9c88fca7bc07406e43263cb44f43afa75e57f86`.

**Trust boundary:** R2 is a theorem-level external import whose precise statement was authenticated. Its original monograph proof was not read or independently replayed. The PDF extraction drops some ≠ symbols; the HTML MathML explicitly contains `\left\langle P\right\rangle\neq\mathbb{Z}_n` and `\left\langle Q\right\rangle\neq\mathbb{Z}_n`. This is not proof verification of R2, nor authentication of Szabó2006 Theorem7.

### Completion data (B) and 8-divisibility (U8)

The existing written proof `../proof.md` (whole SHA256 `fe22a69786a237e144c6e4f06c08bee9f8dcd3ac6cbd365b4fab054debf312e6`) supplies:

- Section3, B1: a unique a^n∈M with n>0.
- Section3, B2–B4: actual residue sets R={r mod n : b^s a^r∈M for some s≥1}, L={l mod n : a^l b^t∈M for some t≥1}, with a bijection R×L→Z_n, (r,l)↦r+l, and
  R⊇{0,1,7,13,14}, L⊇{0,3,8,11}. In particular |R||L|=n and both contain0.
- Sections4–6: the all-t tiling/one-sided unit-multiplier written argument proves 8|n. The present paper imports that complete written result, not its finite sanity tests or the arithmetic-only Lean roots as a code-theoretic proof.

The current manuscript does not need stable-set, Hajós, triangle, completion-converse or Szabó2006 assumptions. It does not assume that any arithmetic order admits a factorization or a code. Section3 below is stated directly for the displayed cyclic-factorization data, independently of code realization; the completion corollary then invokes B and U8 at their recorded written-proof boundary.

## 3. Complete factorization argument

### Lemma M0: multiplier preservation, including multiplicities

Let G be a finite abelian group, and let F,B:G→Z_{≥0} have convolution F*B identically1. If a positive integer d is coprime to the total mass |B|=Σ_g B(g), the pushforward B^(d)(g)=Σ_{dh=g}B(h) also has F*B^(d) identically1.

**Proof.** For a prime ℓ∤|B|, work in F_ℓ[G]. Write W=Σ_g e_g. From FB=W and WB=|B|W, Frobenius gives

    F B^(ℓ) = F B^ℓ = W B^(ℓ−1) = |B|^(ℓ−1)W = W.

Thus every coefficient of the corresponding integer convolution is nonnegative and congruent to1 moduloℓ, hence at least1. The coefficient sum is still |F||B|=|G|, so all |G| coefficients equal1. Pushforward preserves |B|; iterating over the prime factors of d proves the claim. This is the standard group-ring multiplier argument, not a novelty claim. QED.

### Lemma M1: 330 divides |R|

Suppose R⊕L=Z_n with R containing0,1 and L containing0,3,8,11. Here n>1; for the eventual completion application, U8 and n>0 ensure n≥8, and B also gives n≥20. Thus the two R-coordinates0,1 are distinct.

Applying M0 to B=1_R, F=1_L, each displayed equality is a collision between distinct actual pairs if the multiplier is coprime to |R|:

| Multiplier on R | First pair (r,l) | Second pair | Equal integer images | Forced prime divisor of |R| |
|---|---|---|---|---|
|8|(0,8)|(1,0)|8|2|
|3|(0,3)|(1,0)|3|3|
|5|(0,8)|(1,3)|8|5|
|11|(0,11)|(1,0)|11|11|

For example, if 2∤|R|, d=8 is coprime to |R|, so M0 would give unique representation after multiplying R by8, contradicted by the first row. The other three rows use prime multipliers. Distinctness does not depend on the L coordinates because the R coordinates differ. Reducing the equalities modulo n preserves the collisions. Consequently 2·3·5·11=330 divides |R|. QED.

### Lemma M2: both factor cardinalities have at least three prime divisors

The factorization is normalized since 0∈R∩L. Since 1∈R, ⟨R⟩=Z_n. Since 3,8∈L and 3·3−8=1 as an integer identity, the subgroup generated by L contains1; hence ⟨L⟩=Z_n. R2 applied with P=L,Q=R now excludes a cardinality |L| involving zero, one or two distinct primes. Thus there exist three pairwise distinct primes p_1,p_2,p_3 dividing |L|. Applying R2 with factors exchanged also gives the corresponding statement for |R|; M1 already forces four distinct primes there.

No assumption says these primes are disjoint from2,3,5,11. All overlap is allowed. QED, relative to R2.

### Theorem O: the quotient must contain two distinct odd primes

Assume the factorization data in M1 and also 8|n. Write |R|=330a and |L|=b with positive integers a,b. Then

    n=330ab,       q:=n/330=ab.

M2 implies that q, a multiple of b, has at least three distinct prime divisors. Because 330=2·165 and 8|n, we have 4|165q; as gcd(4,165)=1, it follows that4|q. Put q=4m. Hence n=1320m.

At least two of q's three distinct prime divisors are odd, say r and s. Since they do not divide4, both divide m. They are distinct; thus rs|m. Distinct odd primes have product at least3·5=15, and m>0, so

    m≥15,                 n≥1320·15=19800.

This is a written all-order argument; it uses no parameter enumeration or scientific program. It also proves the structural restriction on m, not merely the numerical bound. QED, relative to R2.

## 4. Application to the exact book code

For any hypothetical finite completion of the exact Shor16 code, B supplies the normalized factorization and the required actual inclusions; U8 supplies8|n. Therefore TheoremO applies to its unique a-power order. All code-theoretic inputs are necessary consequences, not sufficient realization conditions. None of the argument establishes that a hypothetical M exists.

This replaces dependence on the **unverified 2006 transcription** for this consequence with a precise authenticated **2023 theorem statement** plus the existing written bridge/U8 proofs. It does not replace every literature theorem by a new proof, nor certify the monograph's argument. Without R2, this manuscript retains only the inherited1320-divisibility boundary. Without B/U8, TheoremO is a theorem about its explicit factorization premises, not about arbitrary codes.

## 5. Verification, novelty and remaining problem

Parent symbolic checks: normalizedness uses actual0 on both sides; generation uses explicit1 and3·3−8; all four multiplier collisions use actual included residues; prime overlap is never forbidden; divisibility is proved from |R| and |L| before cancellation; 4|q is derived from8|n, not from an illicit cancellation of330. The lower-bound arithmetic does not use a finite-case list. The arithmetic example m=15/n=19800 is only the minimum permitted by these inequalities, **not a factorization or completion witness**.

No scientific code/Lean/solver/model CLI was executed. The original required independent-model gate remains unperformed/blocked; this paper is a candidate written derivation, not an accepted replacement verdict. External source proof and novelty checks remain separate.

The original question remains open in this work: produce a finite UD complete extension containing C, or prove no such extension exists for every admissible n. A direct cyclic factorization would still not realize a finite completion. New source-relative order restrictions do not solve that all-order gap.

Process history: audit-worker inventory was delivered/ACKed before this manuscript was drafted; parent pre-ACK route reasoning is nevertheless permanently recorded in checkpoint237. No clean planning-order/compliance claim is made. The old eight forbidden scientific outputs remain excluded and are not used here.
