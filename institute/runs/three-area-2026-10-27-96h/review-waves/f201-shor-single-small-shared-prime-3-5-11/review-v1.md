# f201 — independent same-harness review: one small shared prime

**Disposition: 0 F / 0 M / 0 m; 3 INCONCLUSIVE evidence categories, not findings against the conditional mathematical argument.** Subject to the expressly adopted Łaba–Londner Corollary 6.2/T2 import specified below, the candidate's anchored-tiling exclusion and its stated order-family and same-code implications are supported over their full stated quantifiers. In particular, the review includes shared primes and does not assume p∤|Q|. The three inconclusive categories are (1) external source verification and truth of the named import, (2) author-checker PASS/counts and historical/process attestations, and (3) unrestricted Shor status, novelty and other out-of-scope claims. No one of these is silently promoted to a premise or a positive verification.

Native clock observed before composing this review: **2026-10-29T13:18:23-0700 PDT**. This is not a file-creation timestamp.

## Frozen inputs, measurements, and actual sequence

The first research artifact opened was this wave's `manifest-v1.json`. Its complete body was displayed in raw windows 1–15 and 16–30. Its measured SHA-256 was `0b681946f60119b5a397ffb793cb8c924c570f147b49b66edb9acb1ff49569f1`, matching the assigned prefix `0b681946f601`; it had 2,697 bytes and 30 LF. Mandatory general memory/skill instruction material was read before the manifest, but no other research artifact was opened or used as evidence.

Before opening either declared input body, I measured **both** files and compared all of SHA-256, bytes and LF with the manifest. Both matched:

| Order | Declared input | Measured SHA-256 | Bytes | LF | Actual complete raw windows displayed |
|---|---|---|---:|---:|---|
| 1 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/math-5-shor-165-powers-two-all-tail-conditional-parent-v1.md` | `059616d47a482b46fa647722646df69482de71d87cfda54ad67c95801667a47a` | 6,184 | 34 | 1–15, 16–30, 31–34 |
| 2 | `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-single-small-shared-prime-v1.md` | `da734f2a29a6681043d2645de269478e781a055d381607bccf4fea62067cd8b0` | 15,400 | 172 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–172 |

The disposition was displayed completely before the candidate, including both final lines and all intervening lines; all candidate lines including its ending were displayed before reconstruction or control design. Its source links and checker were not opened. The sequence thereafter was mathematical reconstruction, creation and execution of the independently written finite-control script, clock observation, and composition of this review. The measured manifest contains only the above two declared inputs.

## Claim-by-claim verdicts

`0` in this table means **0 F / 0 M / 0 m** for that claim under its stated hypotheses, not an unconditional certification of an import. F, M, m mean fatal, major and minor respectively.

| Claim or interface | Verdict | Reason and exact boundary |
|---|---|---|
| R1: 330 divides n | 0 | Independent divisor-exclusion derivation plus the displayed anchor differences; n>14 supplies distinct literal anchor residues. |
| R2: each of 3, 5, 11 divides the cardinality of Q | 0 | Dilation of Q, with injectivity and uniqueness proved below, collides directly with the matching P difference. For the theorem this forces the P-prime p to be shared. |
| Parameterization and arbitrary odd factors | 0 | n=2^K p^v R, v≥2, a+b=K and q₁q₂ divides R; R can include additional odd primes and powers. |
| R3: every odd Q-difference divisible by q₁ or q₂ is divisible by p² | 0 | Both p∤x and p∥x cases yield an admissible dilation and a proper common divisor. No bounded search is used as the proof. |
| Every R-fibre is nonempty and single-parity | 0 | The RP dilation, same-coset count, mixed-parity comparison and the nonintegral translated-subgroup count are valid for all v≥2 and all allowed a,b,R. |
| Corollary 6.2/T2 applies to Q | 0 conditional | The only possibly shared primes are 2 and p. The general two-shared-prime T2 statement is the specifically named adopted import, not a source verified here. |
| C1, C2 and C3; all divisors m of R | 0 conditional | Primitive-root divisibility, evaluation at 1 and T2 give divisibility of Q by Φ_{sm} for one globally fixed s∈{p,p²} and all m dividing R. |
| Identity ∏ Φ_{sm}(X)=Φ_s(X^R) over all m dividing R, residue-basis quotient, and nonconstant fibres | 0 conditional | Coprimality of s and R, monic factorization, and nonzero fibre weights establish all three steps. The coset calculation in fact also proves the nonconstancy without invoking T2; see below. |
| Graph crossing and theorem | 0 conditional | The full q₁/q₂-step graph is connected; only one crossing edge is required. Together with R3 it contradicts fibre nonconstancy for every n>14 and P of cardinality p2^a. |
| n=165p^s2^K order-family caller | 0 | R2 and the separate j=0 argument leave 2≤j≤s. The exclusion j=1 invokes the reviewed theorem. No feasibility of the residual is inferred. |
| Finite UD, factor-complete code-to-tiling caller | 0 | Reconstructed below directly for the same extension D, using its actual atoms; the converse is not claimed. The order-family conclusion remains conditional on the reviewed theorem. |
| Author's checker PASS, numerical counts, and provenance/process attestations | INCONCLUSIVE | Forbidden author code/receipts were not run or used; the separate controls below do not purport to reproduce or authenticate those assertions. |
| Truth and precise external source text of Łaba–Londner/T2 | INCONCLUSIVE as external verification | The disposition expressly names the import and its two-shared-prime scope. Its proof, source body and underlying literature were not read or independently verified. |
| Unrestricted Shor problem, other cardinalities, novelty or SOTA | INCONCLUSIVE / outside scope | No such conclusion follows from this packet and no external search or sibling result was used. |

## Explicit premises and elementary tools

The only deep mathematical premise imported from the pinned disposition is the named **Łaba–Londner arXiv:2106.14042v3, Corollary 6.2 / Coven–Meyerowitz T2**: for a cyclic tiling with at most two modulus primes dividing both factor cardinalities, the factor masks satisfy T2. Applied to Q, T2 says that whenever the cyclotomic factors Φ_{s_i} of Q have prime-power orders s_i at distinct primes, Φ_{∏s_i} also divides Q. The disposition's separate 165·2^t conclusion is not used to extend this theorem to new n. The source text and the theorem's truth are not rechecked here. The named classical results in the disposition are not replaced by linked bodies.

I independently reconstruct the two general finite-cyclic tools needed here. They are not taken on faith from the author's checker or from an unexamined paper.

1. **Dilation.** Let A⊕B=Z_n and let t be positive and coprime to |A|. Write their masks A(X), B(X), and U=1+⋯+X^{n−1} in Z[X]/(X^n−1). For a prime h∤|A|, work modulo h. Frobenius gives A(X^h)≡A(X)^h, while AB=U and AU=|A|U. Therefore

   `A(X^h)B(X) ≡ A(X)^{h−1}U ≡ |A|^{h−1}U ≡ U (mod h)`.

   Every coefficient of the left-hand side counts pairs, is nonnegative, and is congruent to 1 mod h. There are n coefficients and their total is |A||B|=n; each is therefore exactly 1. In particular hA is injective on A and hA⊕B=Z_n. Iterating over the prime factors of t proves the stated dilation, including t not invertible mod n.

2. **Equal-gcd exclusion.** If nonzero differences α∈A−A and β∈B−B have common gcd d<n with n, put m=n/d. Both α/d and β/d are units mod m. Choose an integer t with `t(α/d)≡β/d (mod m)` and also coprime to every prime of n not dividing m; the Chinese remainder theorem permits this, and t is then a unit mod n. Since |A| divides n, gcd(t,|A|)=1. Dilation gives tA⊕B, but tα≡β mod n yields two distinct representations. This contradiction proves `Div_n(A)∩Div_n(B)={n}`. The zero difference accounts for the common value n.

The coset count is also elementary: if A⊆H≤G and A⊕B=G, each coset u+H is tiled by A and B∩(u+H), so its B-count is |H|/|A|. Integer cyclotomic irreducibility, the prime-power evaluation Φ_{ℓ^j}(1)=ℓ, monic polynomial division and elementary modular arithmetic are used explicitly below.

## Reconstruction of the anchored theorem

Let n>14, P⊕Q=Z_n, `{0,3,8,11}⊆P`, `{0,1,7,13,14}⊆Q`, and |P|=p2^a with p∈{3,5,11}. The named anchors are distinct as residues.

### R1 and R2

If n is odd, the P-difference 8 and Q-difference 1 both have gcd 1 with n, contrary to equal-gcd exclusion. If any ℓ∈{3,5,11} is absent from n, the P-difference ℓ—respectively 3−0, 8−3, or 11−0—and the Q-difference 1 have common gcd 1. Thus 330|n.

If ℓ∤|Q| for one of these ℓ, dilation gives P⊕ℓQ. Its P-difference ℓ equals the ℓQ-difference ℓ(1−0). Since 0<ℓ<n, these are nonzero equal differences and give two representations. Hence 3·5·11 divides |Q|. In particular p divides both |P| and |Q|. Write

`n=2^K p^v R`, `|P|=p2^a`, `|Q|=p^(v−1)R2^b`,

where K≥1, v≥2, a,b≥0, a+b=K, R is odd, gcd(R,p)=1, and the other two primes q₁,q₂ from {3,5,11} both divide R. No squarefreeness or restriction on other prime divisors of R is needed.

### R3: every relevant odd difference is divisible by p²

Take an odd integer representative x of a Q-difference with q₁|x or q₂|x, and set g=gcd(x,n). Since n is even, g is odd and g<n.

* If p∤x, choose ℓ∈{q₁,q₂} dividing x. Then ℓ|g, t=g/ℓ is odd and p∤t, hence gcd(t,|P|)=1. The dilation tP⊕Q contains a P-difference tℓ=g and a Q-difference x; each has gcd g with n, contradiction.
* If p|x but p²∤x, then v≥2 gives p∥g. Taking t=g/p is again admissible, and the P-difference p becomes g. Equal-gcd exclusion gives the same contradiction.

Thus p²|x. In both branches the dilation is applied to the original P with its own separately established coprimality; no unproved simultaneous dilation is assumed.

### Fibres, their sizes and parity

For u∈Z_R let Q_u consist of the elements of Q congruent to u mod R. Since gcd(R,|P|)=1, RP⊕Q. The first factor lies in the subgroup RZ_n of size n/R, so every fibre has

`|Q_u|=(n/R)/|P|=p^(v−1)2^b>0`.  (1)

Suppose Q_u contains an even and an odd element. Every opposite-parity pair in that fibre has odd difference divisible by R, hence by q₁; R3 forces the pair to agree mod p². Fixing one element of each parity then makes **all** of Q_u congruent mod p².

Set N=p^v2^K. Identifying the coset u+RZ_n with Z_N gives a tiling `V_u⊕P̄=Z_N`, where `V_u={(q−u)/R:q∈Q_u}` and `P̄=P mod N`. Dilation injectivity implies |P̄|=|P|. If Q_u were constant mod p², invertibility of R mod p² would put V_u in one coset of the subgroup H=p²Z_N. Translate V_u into H and translate the other factor oppositely. The coset count would require

`|H|/|V_u| = [p^(v−2)2^K]/[p^(v−1)2^b] = 2^a/p`

points of the other factor in each H-coset, impossible because p is odd. Hence every Q_u has exactly one parity. The sets E and O of even and odd fibre indices are both nonempty, since 0∈Q_0 and 1∈Q_1 and R>1.

**Additional observation, not a new premise:** the translated-subgroup calculation makes no use of mixed parity once constancy mod p² has been assumed. Thus it actually rules out a constant Q_u for *every* u directly. The separate T2 derivation next is nevertheless checked in full because it is part of the frozen candidate and the requested conditional review. I retain the requested conditional disposition rather than treating this observation as an external certification of a stronger result.

### T2 and the residue-basis quotient

Only 2 and p can divide both factor cardinalities. Therefore the adopted two-shared-prime import gives T2 for Q.

The mask identity `P(X)Q(X)≡1+⋯+X^{n−1} (mod X^n−1)` shows that each of Φ_p and Φ_{p²} divides P or Q. If both divided P, their monic product would divide P in Z[X]; evaluation at 1 would give p²||P|, contradicting |P|=p2^a. Thus choose a **single** s∈{p,p²} such that Φ_s|Q. For every prime ℓ|R and every 1≤j≤v_ℓ(R), the identity similarly assigns Φ_{ℓ^j} to a factor, but it cannot divide P: evaluation at 1 would force ℓ||P|. Hence Φ_{ℓ^j}|Q.

For each m|R, select from Q's prime-power factors s together with exactly the nontrivial prime powers in m. They have pairwise distinct base primes. T2, with Φ_s itself covering m=1, gives `Φ_{sm}|Q`. Since gcd(s,R)=1, a complex root ζ satisfies that ζ^R has order s precisely when ζ has order sm for a unique m|R. Both sides are monic with simple roots, so

`∏_{m|R} Φ_{sm}(X) = Φ_s(X^R)`.  (2)

The factors are distinct irreducibles over Q; their product divides the integer mask Q over Q, and monicity makes the quotient integral.

Using standard representatives 0≤q<n and 0≤u<R, decompose uniquely by exponents mod R:

`Q(X)=Σ_{u=0}^{R−1} X^u F_u(X^R)`,
`F_u(Z)=Σ_{q∈Q_u} Z^((q−u)/R)`.

Decompose the integer quotient by Φ_s(X^R) in the same residue basis. Uniqueness yields Φ_s(Z)|F_u(Z) for **each** u. By (1), F_u has positive weight. If Q_u were constant mod p², then all `(q−u)/R` would be congruent to one d mod p². At a primitive s-th root ζ, because s|p², `F_u(ζ)=|Q_u|ζ^d≠0`, contrary to Φ_s|F_u. Therefore every fibre is nonconstant mod p². This is nonconstancy, not a claim of full p²-equidistribution.

### Connected graph and contradiction

Join u to u+q₁ and to u+q₂ in Z_R. The graph is connected because gcd(q₁,q₂)=1, so their integer combinations generate 1. Along a path from 0∈E to 1∈O, at least one edge joins an even fibre to an odd fibre. If its step is q_i, every difference between its endpoints' elements is odd and divisible by q_i; this remains true when representatives wrap because q_i|R. R3 forces every cross-fibre pair congruent mod p². Both fibres are nonempty, so fixing an element of either makes the other constant mod p², contradicting the preceding step. Only one crossing edge is needed; no connectivity of the graph consisting solely of crossing edges is assumed. This proves the stated no-tiling theorem conditionally as disposed above, including all p-exponents in n, all allocations of 2-powers, and arbitrary additional odd factors.

## Order-family and same-code callers

For n=165p^s2^K with K,s≥1, each of the other two primes occurs exactly once in n. The R2 argument did not use the special shape |P|=p2^a, so it places each of those two primes, and at least one p, in |Q|. Consequently `|P|=p^j2^a` with 0≤j≤s.

The case j=0 is also impossible. Let T=165p^s be the odd part of n. Dilation by T gives TP⊕Q, with TP contained in TZ_n, so the coset u=6 mod T contains Q-elements. Choose one q. It has q≡6 mod 165. If q is odd, q−0 is odd and divisible by 3; if q is even, q−1 is odd and divisible by 5. In either case let ℓ be that divisor and g=gcd(the difference,n). Then g is odd, proper, divisible by ℓ, and t=g/ℓ is odd, hence coprime to |P|=2^a. Dilation by t turns the P-difference ℓ into g, matching the Q-difference's gcd, a contradiction. The theorem eliminates j=1. Therefore any hypothetical tiling satisfies 2≤j≤s; for s=1 there is no such j. Nothing here establishes any residual cardinality's existence or excludes j≥2.

For the code caller, let D be a finite uniquely decipherable, factor-complete extension of the displayed S, with b∈D. Let L bound the lengths of D-atoms. Arbitrarily long all-a factors of D* force an all-a atom: without one, consecutive b-containing atoms bound every all-a run. There is at most one such atom a^n, since two different pure-a atoms would give two distinct atom sequences for a common power. Define P and Q from actual D-atoms `a^i b^k` and `b^ℓ a^j` as in the candidate.

To prove coverage, take, for any residue r mod n, a sufficiently long G≡r mod n and a factor `b^H a^G b^K` of D*, with H,K,G>L. In its D-parsing, the atom containing the last left b is of the form b^ℓa^j and the atom containing the first right b is of the form a^i b^k: the guards are longer than L, and the two border atoms are distinct because G>L. Every atom wholly between them is the unique pure-a atom. Hence G≡i+j mod n.

For directness, suppose two different P,Q residue pairs have i₁+j₁≡i₂+j₂ mod n, and choose actual atoms representing them. Choose M in that common residue class much larger than both i_h+j_h, and H,K larger than all relevant b-exponents. Each pair supplies a D-parsing of `b^H a^M b^K` by left singleton b's, its b^ℓa^j atom, `(M−i−j)/n` copies of a^n, its a^i b^k atom, and right singleton b's. If the j exponents differ, the boundary after the atom containing the last left b differs; otherwise the different i exponents give different boundaries before the atom containing the first right b. These are distinct atom sequences, contradicting unique decipherability. Thus P⊕Q is a same-D tiling. S supplies the four P anchors and five Q anchors. For n>14 the reviewed theorem applies; in particular the specified order-family code impossibilities follow. A cyclic tiling is not asserted sufficient to construct such a code.

## Independently authored finite controls and receipt

Script: `reviewer-f201-exact-controls-v1.py`, in this wave directory only. It was independently written after both complete input reads; it does not load, import, compile or execute any author code. SHA-256 before execution: `0e85caeeeac777da15a97656bb535ceaeb0901e5c53241a10c94747a288440b5`. Command: `python3 -B reviewer-f201-exact-controls-v1.py`, with a 120-second run deadline. `/bin/date` immediately before execution: **2026-10-29T13:17:23-0700 PDT**; immediately after: **2026-10-29T13:17:24-0700 PDT**. Exit code **0**. These are run observations, not inferred file timestamps.

* Exhausted all factor pairs on Z_n for n=6,8,10,12: **3,104 tilings**, **18,176** coprime-to-factor dilation checks, including **5,928** multipliers noninvertible mod n; each tiling also satisfied equal-gcd exclusion. Intended negatives: t=2 shares the factor size in a Z₆ example and destroys uniqueness; `{0,1}+{0,1}` on Z₄ is non-tiling with a shared proper gcd.
* For all odd differences on **36** selected moduli with p=3,5,11; R=q₁q₂, q₁²q₂ or 13q₁q₂; v=2,3; K=1,2, checked **636,912** admissible R3 gcd witnesses. Intended negative: p²|x in the explicit n=990, x=495 example makes every displayed g/ℓ recipe inadmissible. This bounded grid is not the universal proof.
* Checked **675** exact subgroup-to-fibre ratios against 2^a/p, using rational arithmetic. Intended negative: dropping a p from the hypothetical fibre count makes the resulting ratio integral, demonstrating why the actual count matters.
* Checked **6** concrete monic-integer polynomial identities (2), plus **18** positive constant-residue polynomials with nonzero Φ_s remainder. Intended negatives: s=R=3 violates the coprimality needed for (2); the zero polynomial has zero remainder and is excluded by positive fibre weight.
* Built **6** explicit unanchored tilings, two for each p, exercising s=p and s=p². Checked their mask divisibility for every m|R, and **206** fibre divisibility/nonconstancy checks. They are explicitly not anchored examples or code completions. Deleting a term of Φ₃ gives a nonzero remainder, an intended negative for the residue-basis divisibility step.
* Checked connectivity of **9** q₁/q₂-step graphs and all **32,766** nontrivial partitions of Z₁₅ for a crossing edge. For each prime pair, deleting one step family disconnects the corresponding q₁q₂ graph, the intended negative.

The controls do not verify the named import, the universal exponents, or the author-reported PASS/counts. No capped or timed-out run is claimed as an exclusion; this one run completed normally.

## Imports, remaining gap, deviations and review identity

The named LL Corollary 6.2/T2 statement is an expressly adopted conditional input, not externally checked in this review. The exact general dilation and equal-gcd facts used above are supplied by the independent elementary reconstruction rather than by the candidate's references. The same-code border implication is also reconstructed above; it is not borrowed from a linked source. No other disposition body, author script, author PASS, solver outcome, floating search, literature recollection, web source, other model/API, sibling review, held material, or author contact was used as evidence.

The conclusion does not exclude |P| with odd part 3^j, 5^j or 11^j for j≥2, a different shared odd prime, or two or more distinct odd head primes. The j≥2 order-family interval is an unresolved necessary-condition interval, not an existence claim. This review does not decide the unrestricted Shor question or novelty.

**Contract deviations: none.** Same-harness review is not human review, independent-model-family review, formal/kernel verification, or novelty verification.
