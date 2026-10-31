# F547 — WRITTEN review

## Verdict

**overall_correctness: correct — within the expressly stated scope.**

**FATAL: 0 · MAJOR: 0 · MINOR: 0** candidate-mathematics findings.

**explanation:** The supplied body supports the coprime-dilation lemma, anchor divisibility, restricted two-adic exclusion, quotient-fiber obstruction analysis, and unique decodability of the eight literal words. The border consequences are valid only conditional on the displayed Restivo–Salemi–Sportelli import; neither that import’s original proof nor the separate pure-letter-order fact was independently established here. Neither unrestricted anchored nonexistence nor nonexistence of a finite maximal completion follows.

**confidence: 0.98.**

This is a completed written assessment, not a parent adoption or an independent FINITE-gate certificate.

## 1. Frozen input and actual read coverage

The sole mathematical input was **S1**, the author-candidate body stored at:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f497-shor-cyclic-tiling-two-prime-powers-actual-anchor-frontier/review-v1.md`

Parent-supplied pins:

- **Manifest:** `3d823865683232f18b43b1b3adf57447db0b239da3af9cecdfbe1e5d48d875e1`
- **Freeze receipt:** `274cad7c6110ff84a3c75605258dbe4a55d2896cd78bec0eccb4fa0e750638e9`
- **Literal packet:** `937e29274c9ee12b42f99bc635e424ba7a65663b421ace4d2a95c60423c1b2fe`
- **S1:** `ec0cdf85c4da552b1ccd80982c79a5234512161124e2d476cb06da82c470bb86`

These are attributed to the supplied manifest, receipt, and parent live-metadata record—not to child-native hash execution.

Before opening the mathematical packet, I completed the manifest, freeze receipt, dispatch receipt, parent live-metadata supply, and all twelve listed status-only controls, then delivered a direct administrative pre-body ACK to Main. I subsequently read the complete packet in ordered raw windows **1–20, 21–40, …, 501–520, 521–522**, including the final `S1|520` sentence, before mathematical reconstruction. No packet elision remained.

An administrative correction was delivered separately: the ACK’s transcribed endpoint counts for the live-metadata and dispatch files were not established counts and must not be reused. Their actual completed read windows and displayed endings were specified in the correction. This did not change the pre-body read order.

All quarantined episodes and their consumers were treated as **status-only/NONINPUT**. No excluded links, author code, sibling review, external mathematical source, or held scientific payload was followed. No scientific execution or new private selected instance was used. No working-tree file was written; this is the full return for parent materialization.

## 2. Coprime dilation — SUPPORTED

**Anchors: S1 LF 83–139.**

The proof correctly retains image multiplicities until injectivity has been established.

For prime \(\ell\nmid |A|\), directness gives \(A(X)B(X)=J(X)\) in the integral group ring. Reduction modulo \(\ell\) yields

\[
A(X^\ell)B(X)
=A(X)^\ell B(X)
=A(X)^{\ell-1}J(X)
=|A|^{\ell-1}J(X)
=J(X).
\]

The integral coefficient

\[
c_x=\#\{(a,b)\in A\times B:\ell a+b=x\}
\]

is nonnegative and congruent to one modulo \(\ell\), hence at least one. Its total over the \(n\) residues is \(|A||B|=n\), forcing every coefficient to equal one.

This also proves injectivity of multiplication by \(\ell\) on \(A\): coincident images of two distinct elements, combined with any element of the nonempty factor \(B\), would give a coefficient at least two. Successive prime dilations therefore preserve both cardinality and directness for every positive \(k\) coprime to \(|A|\).

There is no hidden requirement that \(k\) be a unit modulo \(n\), and no invalid replacement of a multiplicity-bearing image by an unweighted set.

## 3. Universal anchor divisibility — SUPPORTED

**Anchors: S1 LF 60–79 and 143–195.**

Every contradiction uses actual supplied anchors and a dilation justified by the cardinality whose divisibility is being proved.

| Supposed failure | Admissible dilation | Collision from the supplied anchors |
|---|---|---|
| \(2\nmid |P|\) | \(P\mapsto2P\) | \(2\cdot3+1=2\cdot0+7\) |
| \(2\nmid |Q|\) | \(Q\mapsto8Q\) | \(8+8\cdot0=0+8\cdot1\) |
| \(3\nmid |Q|\) | \(Q\mapsto3Q\) | \(3+3\cdot0=0+3\cdot1\) |
| \(5\nmid |Q|\) | \(Q\mapsto5Q\) | \(8+5\cdot0=3+5\cdot1\) |
| \(11\nmid |Q|\) | \(Q\mapsto11Q\) | \(11+11\cdot0=0+11\cdot1\) |

The relevant original anchors are distinct modulo \(n\), since \(n>14\); the dilation lemma preserves the needed distinction within the dilated factor.

Consequently,

\[
2\mid |P|,\qquad330\mid |Q|,\qquad660\mid n
\]

are supported without restrictions on odd-factor overlap or multiplicity. The exclusion of all odd head cardinalities is correspondingly uniform.

## 4. Whole-odd-factor exclusion and consequences — SUPPORTED

**Anchors: S1 LF 199–296.**

For the theorem’s assumed \(n=4m\), with \(m\) odd and \(3\nmid |P|\), the congruence

\[
2k\equiv3\pmod m
\]

has an odd positive representative: invertibility of two gives the residue class, and adding odd \(m\) changes parity.

The coprimality argument accounts for all prime divisors of \(|P|\):

- \(2\nmid k\) by construction.
- Any odd \(r\mid |P|\) divides \(m\).
- If also \(r\mid k\), the congruence forces \(r\mid3\), contrary to \(3\nmid |P|\).

Thus Lemma 1 applies. Moreover,

\[
m\mid2k-3
\quad\Longrightarrow\quad
4m\mid8k-12,
\]

so the actual anchors give

\[
k\cdot8+1\equiv k\cdot0+13\pmod n.
\]

The two tail entries are distinct, and the head images are distinct by the dilation lemma. This is a directness contradiction.

The equivalent necessary condition

\[
3\mid |P|\quad\text{or}\quad8\mid n
\]

also uses Proposition 2’s prior \(v_2(n)\ge2\); it does not silently omit a lower two-adic case.

Therefore the following consequences are supported:

- No anchored tiling has \(|P|=2u,\ |Q|=2w\), with \(u,w\) odd and \(3\nmid u\).
- The proof permits shared odd primes and arbitrary multiplicities.
- In particular, for \(p\in\{5,11\}\) and \(j\ge2\), head size \(2p^j\) requires \(v_2(|Q|)\ge2\).
- Every anchored tiling satisfies at least one of
  \[
  2^3\cdot3\cdot5\cdot11\mid n,
  \qquad
  2^2\cdot3^2\cdot5\cdot11\mid n.
  \]

These are exclusions and necessary conditions, not existence statements.

## 5. Quotient-fiber calculation and local barrier — SUPPORTED at the stated scope

**Anchors: S1 LF 300–383.**

For

\[
|P|=2^ap^j,\qquad
|Q|=2^bp^tR,\qquad
n=2^{a+b}p^{j+t}R,
\]

the specified \(\gcd(R,2p)=1\) implies \(\gcd(R,|P|)=1\). Dilation by \(R\) is therefore valid. Since \(RP\) lies in \(R\mathbb Z_n\), restriction to each residue class modulo \(R\) gives a direct fiber tiling

\[
A\oplus B_r=\mathbb Z_{2^{a+b}p^{j+t}},
\qquad
|A|=2^ap^j,\quad |B_r|=2^bp^t.
\]

If \(B_r\) lies in one coset of \(L=p^2H\), then, for each target coset of \(L\), precisely one corresponding coset of \(A\) can contribute. Counting its ordered representations gives

\[
|A\cap(\text{corresponding coset})|
=\frac{|L|}{|B_r|}
=2^ap^{j-2}.
\]

For \(j=1\), this is not an integer because \(p\) is odd. For \(j\ge2\), that specific contradiction disappears. The text correctly distinguishes loss of the counting contradiction from feasibility of an anchored tiling.

The supplied symbolic local construction also checks:

- Quotient and remainder modulo \(p^j\) prove \(A_p\oplus B_p=\mathbb Z_{p^v}\).
- The even residues plus \(\{0,1\}\) prove the two-primary direct tiling.
- CRT applies because the two component orders are coprime.
- The second factor is constant modulo \(p^2\), has both parities, and shares \(p\) with the first factor because \(v-j\ge1\).

Crucially, the first factor is entirely even under the CRT identification and therefore omits the actual head anchor \(3\). **It is not an anchored witness.** Its use is limited to demonstrating that the displayed local counting configuration is possible without the full anchors.

The stated unpaid step—an anchored replacement for the every-fiber nonconstancy argument, or a different anchored contradiction—remains unpaid.

## 6. Eight-word unique decodability — SUPPORTED

**Anchors: S1 LF 387–423.**

The reviewed code is exactly

\[
X=\{b,a^3b,a^8b,a^{11}b,ba,ba^7,ba^{13},ba^{14}\}.
\]

The word \(b\) occurs only once in this set; its occurrence in both exponent descriptions does not create an initial empty residual.

### Complete first residual set

Distinct words beginning with \(a\) are not prefix-comparable: their first \(b\) occurs at different positions. They are not prefix-comparable with words beginning with \(b\). Thus all proper-prefix comparisons between distinct codewords occur among the \(ba^q\) words.

The actual exponent-pair differences are:

| Exponent pair | Positive difference |
|---|---:|
| \(0,1\) | \(1\) |
| \(0,7\) | \(7\) |
| \(0,13\) | \(13\) |
| \(0,14\) | \(14\) |
| \(1,7\) | \(6\) |
| \(1,13\) | \(12\) |
| \(1,14\) | \(13\) |
| \(7,13\) | \(6\) |
| \(7,14\) | \(7\) |
| \(13,14\) | \(1\) |

Hence the complete initial residual set is

\[
R_1=\{a,a^6,a^7,a^{12},a^{13},a^{14}\}.
\]

### Complete second residual set

A residual \(a^d\) cannot compare with a word beginning with \(b\). Against \(a^pb\), comparison is possible precisely when \(d<p\), leaving \(a^{p-d}b\); equality \(d=p\) does not occur.

All such comparisons are:

| \(d\) | Admissible supplied \(p\) | Resulting residuals |
|---:|---|---|
| \(1\) | \(3,8,11\) | \(a^2b,a^7b,a^{10}b\) |
| \(6\) | \(8,11\) | \(a^2b,a^5b\) |
| \(7\) | \(8,11\) | \(ab,a^4b\) |
| \(12,13,14\) | none | none |

Thus

\[
R_2=\{ab,a^2b,a^4b,a^5b,a^7b,a^{10}b\}.
\]

Every member starts with \(a\), excluding comparisons with all \(ba^q\) words. Its exponent belongs to \(\{1,2,4,5,7,10\}\), disjoint from \(\{3,8,11\}\); comparison with each \(a^pb\) therefore fails where the earlier \(b\) meets an \(a\). Consequently \(R_3=\varnothing\), with no empty residual at any stage.

An equality between two distinct finite codeword concatenations would, after cancelling their common initial codewords, generate a chain of these residual comparisons terminating at the empty word. The exhaustive chain above makes that impossible. Unique decodability follows without an omitted prefix case.

## 7. Border bridge — SUPPORTED only as a conditional implication

**Anchors: S1 LF 425–469.**

The required external import is exactly the displayed theorem: a finite maximal code containing \(b\) and \(a^n\) has the ordered border pair

\[
P_M=\{i\ge0:\exists s\ge1,\ a^ib^s\in M\},
\qquad
Q_M=\{j\ge0:\exists s\ge1,\ b^sa^j\in M\}
\]

forming a factorization of size \(n\). Its factorization conclusion is the import needed to enter the direct cyclic-tiling scope.

Under that import, the actual words supply the borders in the correct direction:

- \(b,a^3b,a^8b,a^{11}b\) supply \(0,3,8,11\in P_M\), with \(s=1\).
- \(b,ba,ba^7,ba^{13},ba^{14}\) supply \(0,1,7,13,14\in Q_M\), with \(s=1\).

The factorization’s cardinality relation gives

\[
n=|P_M||Q_M|\ge4\cdot5=20>14.
\]

Thus the cyclic results apply, yielding the stated divisibility and restricted higher-power exclusions.

**Not independently established in this review:**

- The original RSS proof.
- Public-source authenticity or equivalence of the quoted formulation to the original theorem.
- The separate pure-letter-order fact needed to remove the explicit \(a^n\in M\) assumption.
- Identification of these eight words with every condition of an unsupplied printed problem.

Those limitations are explicit in S1. Unique decodability plus the conditional restrictions does **not** prove that \(X\) lacks a finite maximal completion.

## 8. Remaining allocations and assurance boundary

**Anchors: S1 LF 471–520.**

The listed residual parameters correctly express what these results do not settle:

- For \(p=3\): \(j\ge2\), \(a,b,t\ge1\), \(55\mid R\), and \(\gcd(R,6)=1\).
- For \(p=5\): the analogous conditions with \(33\mid R\), \(\gcd(R,10)=1\), and \(a+b\ge3\).
- For \(p=11\): the analogous conditions with \(15\mid R\), \(\gcd(R,22)=1\), and \(a+b\ge3\).

In every case,

\[
|P|=2^ap^j,\qquad |Q|=2^bp^tR,
\]

with all original anchors and directness still required. Shared \(p\)-factors are preserved through \(t\ge1\). These lists are supported **as residual obligations relative to this body**, not as a globally audited frontier or an assertion of feasibility.

### Final disposition

- **SUPPORTED:** the self-contained cyclic results, the limited local-barrier construction, the complete eight-word cancellation proof, and the explicitly conditional border consequences.
- **INCONCLUSIVE / NOT ESTABLISHED:** the external theorem’s original proof and source authentication, a global historical-frontier audit, existence in the listed residual allocations, unrestricted anchored nonexistence, and unrestricted finite-completion nonexistence.
- **REFUTED claims:** none.
- **Scientific execution:** NOT_RUN.
- **Assurance:** same-harness written review only; no human, kernel/formal, independent-model-family, novelty, or original-target closure credit.