# F546 — WRITTEN review, full returned body

## Verdict and findings

**The candidate’s mathematical conclusions are SUPPORTED at their stated scopes.**

**FATAL: 0 · MAJOR: 0 · MINOR: 0**

The coprime-dilation proof, actual-anchor divisibility arguments, whole-odd-factor exclusion, higher-\(5\)/\(11\)-power corollaries, quotient-fiber qualification, explicit local barrier construction, and unique-decodability proof reconstruct successfully. The finite-maximal-code consequences remain **conditional on the explicitly stated external import**; that import’s original-source validity is not established by this review.

Neither the unrestricted anchored-tiling target nor the unrestricted finite-completion target is closed.

## 1. Scope, provenance, and read order

Reviewed wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f546-shor-coprime-dilation-and-twoadic-anchor-collision-written-review/`

Frozen identifiers supplied by the receipt and parent metadata:

| Item | SHA-256 |
|---|---|
| Manifest | `b039d4b21936902247d8c82ca982cb0c7696c5bc80204a68f8501905acc7e47f` |
| Freeze receipt | `c42bbf89e8f8b4abf0eedcb48ce492846b6422ae62a6248c3a3b428ba844aef0` |
| Literal packet | `937e29274c9ee12b42f99bc635e424ba7a65663b421ace4d2a95c60423c1b2fe` |
| S1 author body | `ec0cdf85c4da552b1ccd80982c79a5234512161124e2d476cb06da82c470bb86` |

These are **parent-observed metadata**, not independent child-native hash measurements.

Actual order:

1. Read the complete manifest and freeze receipt, the dispatch receipt, the parent metadata supply, and all twelve named status-only control bodies, including their endings.
2. Delivered a direct administrative pre-body ACK to Main through `agent://Main`.
3. Read the entire literal packet in ordered raw windows: LF 1–20, 21–40, continuing without gaps through 501–520, then the final two lines at 521–522.
4. Began mathematical reconstruction only after completing that read.

The packet contains S1 logical lines **1–520**. The recorded source has **519 LF characters**; these are distinct counts, not an omitted final line. All S1 lines, including its final conclusion, were displayed.

Line citations below refer to **S1 logical lines**, not packet offsets. S1 is the author body designated by this manifest, notwithstanding its stored basename `review-v1.md`.

No scientific executable, interpreter, CAS, solver, enumeration, build, test, lint, or formatter was run. No new private mathematical instance was selected. No external source, author code, sibling review, or held scientific payload was followed or consumed. Quarantine controls were used only for status and exclusions.

This body is returned for Main’s materialization; no working-tree file was written.

## 2. Per-claim assessment

| Claim | S1 lines | Assessment |
|---|---:|---|
| Coprime dilation, with multiplicities retained | 81–139 | **SUPPORTED** |
| \(2\mid |P|\) and \(330\mid |Q|\) from actual anchors | 141–195 | **SUPPORTED** |
| No anchored tiling with \(v_2(n)=2\) and \(3\nmid |P|\) | 199–254 | **SUPPORTED** |
| Whole-odd-factor exclusion \(|P|=2u,\ |Q|=2w,\ u,w\) odd, \(3\nmid u\) | 256–265 | **SUPPORTED** |
| All \(j\ge2\), \(p\in\{5,11\}\), \(|P|=2p^j,\ v_2(|Q|)=1\) excluded | 267–281 | **SUPPORTED** |
| Necessary alternative \(1320\mid n\) or \(1980\mid n\) | 283–296 | **SUPPORTED**, necessary only |
| Quotient-fiber count and failure of the old integrality contradiction for \(j\ge2\) | 298–348 | **SUPPORTED** |
| Author-explicit local barrier tiling | 350–383 | **SUPPORTED**, not an anchored witness |
| Unique decodability of the eight displayed words | 385–423 | **SUPPORTED** |
| Displayed RSS theorem as an independently verified external fact | 425–442 | **INCONCLUSIVE** in this review |
| Consequences assuming the displayed factorization import | 444–469 | **SUPPORTED CONDITIONALLY** |
| Remaining parameter lists as obligations not settled by this candidate | 471–508 | **SUPPORTED** at that limited bookkeeping scope |
| Closure of either unrestricted original target | 28, 469, 520 | **NOT ESTABLISHED; not claimed** |

No reviewed mathematical claim was refuted.

## 3. Coprime dilation: complete reconstruction

**Anchor: S1 83–139.**

Let \(A\oplus B=\mathbb Z_n\), with formal sums in the integral group ring. Directness gives

\[
A(X)B(X)=J(X),\qquad J(X)=\sum_{x\in\mathbb Z_n}X^x.
\]

For a prime \(\ell\nmid |A|\), reduction modulo \(\ell\) gives

\[
A(X^\ell)B(X)
=A(X)^\ell B(X)
=A(X)^{\ell-1}J(X)
=|A|^{\ell-1}J(X)
=J(X).
\]

Each step is valid:

- Frobenius applies in the commutative group ring over \(\mathbb F_\ell\).
- Every group translation preserves \(J\), so multiplying \(J\) by a formal sum multiplies it by that sum’s augmentation.
- Fermat’s theorem applies because \(\ell\nmid |A|\).

**No step requires \(\ell\nmid n\).** In particular, the argument does not rely on semisimplicity or an invertible dilation of the ambient group.

The integral coefficient before replacing the multiplied list by an image set is

\[
c_x=\#\{(a,b)\in A\times B:\ell a+b=x\pmod n\}.
\]

Thus \(c_x\) is nonnegative and \(c_x\equiv1\pmod\ell\), hence \(c_x\ge1\). Its total is

\[
\sum_x c_x=|A||B|=n.
\]

There are exactly \(n\) coefficients, so all are one. This is the decisive passage from a congruence to exact directness.

If distinct \(a,a'\in A\) had the same multiplied image, adding any fixed \(b\in B\) would contribute two distinct ordered pairs to one coefficient, contradicting \(c_x=1\). Hence dilation is injective on \(A\), and \(\ell A\oplus B=\mathbb Z_n\).

For a general positive \(k\), every prime divisor of \(k\) avoids \(|A|\). Successive prime dilations preserve both directness and cardinality, so the same condition remains applicable at every step. The case \(k=1\) is the identity. Interchanging the factors gives the symmetric result.

The proof therefore establishes precisely the lemma needed later: **coprimality with the dilated factor’s cardinality, not with \(n\).**

## 4. Universal divisibility: actual-anchor collisions

**Anchor: S1 141–195.**

The following are the candidate’s actual ordered-pair collisions; no substitute anchor family is used.

| Supposition | Tiling supplied by dilation | Colliding sums |
|---|---|---|
| \(2\nmid |P|\) | \(2P\oplus Q\) | \(2\cdot3+1=2\cdot0+7\) |
| \(2\nmid |Q|\) | \(P\oplus8Q\) | \(8+8\cdot0=0+8\cdot1\) |
| \(3\nmid |Q|\) | \(P\oplus3Q\) | \(3+3\cdot0=0+3\cdot1\) |
| \(5\nmid |Q|\) | \(P\oplus5Q\) | \(8+5\cdot0=3+5\cdot1\) |
| \(11\nmid |Q|\) | \(P\oplus11Q\) | \(11+11\cdot0=0+11\cdot1\) |

All entries occur in the stipulated anchors

\[
\{0,3,8,11\}\subseteq P,\qquad
\{0,1,7,13,14\}\subseteq Q.
\]

The ordered pairs are distinct. The bound \(n>14\) keeps the displayed distinct anchor residues distinct; the dilation lemma also preserves distinct elements within the dilated factor.

For the second row, odd \(|Q|\) is exactly what makes dilation by \(8\) admissible. For the other rows, the indicated missing prime supplies the relevant coprimality condition.

Consequently,

\[
2\mid |P|,\qquad 2\cdot3\cdot5\cdot11=330\mid |Q|.
\]

It follows that \(660\mid n\), and both factor cardinalities are even.

This reasoning does **not** discard a prime because it divides the other factor or the ambient order. The lemma permits precisely those shared-ambient-factor situations.

## 5. Whole-odd-factor exclusion

**Anchor: S1 199–265.**

Assume

\[
n=4m,\qquad m\text{ odd},\qquad 3\nmid |P|.
\]

Because \(2\) is invertible modulo \(m\), there is a residue class satisfying

\[
2k\equiv3\pmod m.
\]

Adding \(m\) changes parity, so an odd representative exists; adding positive multiples of \(2m\) then makes it positive without altering parity or the congruence.

To prove \(\gcd(k,|P|)=1\):

- The prime \(2\) does not divide \(k\).
- Every odd prime \(r\mid |P|\) divides \(m\), because \(|P|\mid n=4m\).
- If such an \(r\) divided \(k\), reducing the displayed congruence modulo \(r\) would give \(r\mid3\).
- That forces \(r=3\), contrary to \(3\nmid |P|\).

This covers every possible prime divisor of \(|P|\), including arbitrary multiplicities and odd factors shared with \(|Q|\).

Also,

\[
m\mid2k-3
\quad\Longrightarrow\quad
4m\mid4(2k-3)=8k-12.
\]

Thus \(8k\equiv12\pmod n\). The dilation lemma supplies \(kP\oplus Q=\mathbb Z_n\), but the actual anchors give

\[
k\cdot8+1\equiv k\cdot0+13\pmod n.
\]

The \(Q\)-entries \(1\) and \(13\) are distinct, so these are distinct ordered representations. This contradicts directness.

Therefore no anchored tiling has \(v_2(n)=2\) and \(3\nmid |P|\).

The equivalent formulation

\[
3\mid |P|\quad\text{or}\quad8\mid n
\]

correctly uses the earlier result \(4\mid n\): when \(8\nmid n\), the two-adic valuation must be exactly two.

For \(|P|=2u,\ |Q|=2w\) with \(u,w\) odd, \(n=4uw\). If \(3\nmid u\), then \(3\nmid |P|\), giving the stated whole-odd-factor exclusion. There is no hidden restriction on overlap between the prime factors of \(u\) and \(w\).

## 6. Higher-power and necessary-order consequences

**Anchor: S1 267–296.**

For \(p\in\{5,11\}\), the cardinality \(2p^j\) is not divisible by \(3\). Therefore the preceding theorem excludes

\[
|P|=2p^j,\qquad |Q|=2w,\qquad w\text{ odd},
\]

for every stated \(j\ge2\). Additional \(p\)-powers in \(w\) do not affect the argument. Together with \(2\mid |Q|\), the exclusion implies \(v_2(|Q|)\ge2\) for any prospective tiling with that head cardinality.

The necessary-order alternative also follows:

- If \(8\mid n\), combining this with \(660\mid n\) gives
  \[
  2^3\cdot3\cdot5\cdot11=1320\mid n.
  \]
- Otherwise the theorem forces \(3\mid |P|\), while universal tail divisibility already gives \(3\mid |Q|\). Combining \(9\mid n\) with \(660\mid n\) gives
  \[
  2^2\cdot3^2\cdot5\cdot11=1980\mid n.
  \]

Neither branch supplies existence. The candidate explicitly preserves that distinction.

## 7. Quotient-fiber counting and the author-explicit local barrier

**Anchor: S1 298–383.**

For the displayed higher-power family,

\[
|P|=2^ap^j,\qquad |Q|=2^bp^tR,\qquad
n=2^{a+b}p^{j+t}R,
\]

the conditions \(a,b,t\ge1\) and \((165/p)\mid R\) follow from the already proved anchor divisibility. The definition of \(R\) separates all \(2\)- and \(p\)-powers, so \(\gcd(R,|P|)=1\).

Dilation by \(R\) is therefore legitimate. Its first factor lies in \(R\mathbb Z_n\). Restricting the direct tiling to one residue class modulo \(R\), translating that class, and identifying \(R\mathbb Z_n\) with

\[
H=\mathbb Z_{2^{a+b}p^{j+t}}
\]

gives \(A\oplus B_r=H\). Injectivity preserves \(|A|=2^ap^j\), and counting the fiber gives \(|B_r|=2^bp^t\).

If \(B_r\) lies in one coset of \(L=p^2H\), then, for each target coset of \(L\), only one corresponding coset of \(A\) can contribute. Directness and coverage force its number of \(A\)-elements to be

\[
\frac{|L|}{|B_r|}
=\frac{2^{a+b}p^{j+t-2}}{2^bp^t}
=2^ap^{j-2}.
\]

For \(j=1\), this is \(2^a/p\), not an integer because \(p\) is odd. For \(j\ge2\), it is an integer. Thus **this counting obstruction disappears**; it does not prove anchored feasibility.

The local construction is also correct for the author’s entire displayed range:

\[
H'=\mathbb Z_{p^v}\times\mathbb Z_{2^{a+1}},\qquad
v\ge j+1,\quad j\ge2,\quad a\ge1.
\]

The sets \(A_p,B_p\) tile the first coordinate by quotient and remainder upon division by \(p^j\). The sets \(A_2,B_2\) tile the second coordinate by parity. Their Cartesian products therefore tile \(H'\) directly, and CRT identifies this group with a cyclic group because its two coordinate orders are coprime.

Its second factor is constant modulo \(p^2\), contains both parities, and has cardinality \(2p^{v-j}\), so it shares an odd \(p\)-factor with the first factor.

Crucially, its first factor has only even parity and therefore misses the actual head anchor \(3\). The candidate identifies this failure expressly. The construction is **not** an anchored counterexample, an original-target witness, or a substitute for the missing higher-exponent anchored argument.

The stated first unpaid step at S1 383 is accurate.

## 8. Eight-word unique decodability

**Anchor: S1 385–423.**

The reviewed code is exactly

\[
X=\{b,a^3b,a^8b,a^{11}b,ba,ba^7,ba^{13},ba^{14}\}.
\]

The positive left- and right-exponent difference sets are correctly given as

\[
D_P=\{3,5,8,11\},\qquad
D_Q=\{1,6,7,12,13,14\},
\]

and are disjoint.

The only proper-prefix comparisons between distinct initial codewords occur among the words \(ba^q\), including \(b=ba^0\). Their nonempty residuals are exactly \(a^d\) for \(d\in D_Q\).

Such a residual can compare with a codeword only when that codeword is \(a^pb\), \(p\in\{3,8,11\}\), and \(d<p\). The author-explicit transitions are:

- \(p=3\): \(d=1\), leaving \(a^2b\).
- \(p=8\): \(d=1,6,7\), leaving \(a^7b,a^2b,ab\).
- \(p=11\): \(d=1,6,7\), leaving \(a^{10}b,a^5b,a^4b\).

Their union is exactly

\[
\{ab,a^2b,a^4b,a^5b,a^7b,a^{10}b\}.
\]

No \(d=p\) occurs, so this transition does not produce the empty word. Each resulting residual starts with \(a\), excluding comparison with every \(ba^q\), and its left exponent differs from \(3,8,11\), excluding comparison with the remaining codewords at the first \(a/b\) mismatch.

Thus the residual chain terminates without reaching the empty word. Any distinct equal concatenations would produce such a chain after cancelling their common initial codewords. This proves unique decodability of the displayed \(X\).

This check uses only the author’s explicit words and residuals.

## 9. External import and conditional finite-code consequence

**Anchor: S1 425–469.**

The packet supplies a named RSS factorization/border theorem, its formulation, and a secondary-source attribution. It does not supply the original proof. No external source was opened in this review.

Accordingly:

- **Original theorem/source verification: INCONCLUSIVE.**
- **The following conditional implication: SUPPORTED.**

Assume the displayed theorem supplies the stated direct cyclic factorization of size \(n\) for \(P_M,Q_M\). If \(M\) contains the actual displayed words, then taking \(s=1\) in their defining occurrences gives

\[
\{0,3,8,11\}\subseteq P_M,\qquad
\{0,1,7,13,14\}\subseteq Q_M.
\]

The imported factorization supplies \(n=|P_M||Q_M|\), hence \(n\ge4\cdot5=20>14\). The reconstructed cyclic theorems then apply and give

\[
2\mid |P_M|,\qquad330\mid |Q_M|,\qquad
3\mid |P_M|\ \text{or}\ 8\mid n,
\]

including the stated exclusion for heads \(2p^j\), \(p\in\{5,11\}\), with \(v_2(|Q_M|)=1\).

This does not independently establish the RSS import, the additional general pure-letter-order fact, equivalence to an unsupplied printed problem, or nonexistence of a finite maximal completion. The candidate preserves those boundaries.

## 10. Residual scope and assurance ceiling

**Anchor: S1 471–520.**

The remaining one-odd-prime parameter lists are consistent with the proved restrictions:

- For \(p=3\), the new obstruction does not apply because the head already contains \(3\).
- For \(p=5,11\), the new obstruction removes exactly the listed case \(a=b=1\); with \(a,b\ge1\), this is expressed by requiring \(a+b\ge3\).
- Shared \(p\)-powers in the tail remain allowed.
- The original anchors and directness remain required throughout.

The lists are appropriately described as obligations not settled **by the results used in this candidate**, not feasible constructions or a globally audited historical frontier. No comparison with every prior disposition was performed here.

### Supported acceptance boundary

This review supports:

1. Coprime dilation under \(\gcd(k,|A|)=1\), without assuming \(\gcd(k,n)=1\).
2. Universal actual-anchor divisibility \(2\mid |P|\), \(330\mid |Q|\).
3. The exclusion \(v_2(n)=2,\ 3\nmid |P|\), including the stated arbitrary-odd-factor and higher-\(5\)/\(11\)-power families.
4. The necessary order alternative.
5. The quotient-fiber counting qualification and the expressly nonanchored local construction.
6. Unique decodability of the eight literal words.
7. The finite-code consequences **only conditional on the displayed import**.

### Not granted

- FINITE verification or executable/certificate credit.
- Closure of all higher-prime-power or mixed-factor allocations.
- An anchored counterexample or feasibility result.
- Nonexistence of a finite maximal completion.
- Original-source authentication or printed-problem equivalence.
- Novelty, human review, kernel/formal verification, or independent-model-family assurance.
- Independent certification of the author’s historical chronology or execution reports.

**FINITE gate: NOT_PERFORMED.** This is a WRITTEN return only.

**overall_correctness:** correct

**explanation:** The candidate’s self-contained written arguments reconstruct without a defect at their explicitly restricted scopes. Its external-source bridge remains conditional, and neither unrestricted original target is proved.

**confidence:** 0.98