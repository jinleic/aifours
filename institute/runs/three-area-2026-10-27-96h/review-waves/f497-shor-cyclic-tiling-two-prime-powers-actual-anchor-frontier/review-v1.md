# F497 — author-candidate-v1.md

## Status and exact scope

**AUTHOR CANDIDATE — written proofs below; not independently reviewed or adopted.**

This return establishes a uniform exclusion beyond the frozen first-odd-exponent result:

> **There is no anchored direct tiling with**
> \[
> |P|=2u,\qquad |Q|=2w,\qquad u,w\ \text{odd},\qquad 3\nmid u.
> \]
> The odd factors of \(u,w\), their multiplicities, and their overlap are otherwise unrestricted.

In particular, for \(p\in\{5,11\}\) and **every \(j\ge2\)**, this excludes
\[
|P|=2p^j,\qquad v_2(|Q|)=1.
\]
The conclusion does not assume that \(p\) is absent from \(Q\); the actual anchors force \(p\mid |Q|\).

The return also proves the necessary conditions
\[
2\mid |P|,\qquad 330\mid |Q|,\qquad
3\mid |P|\ \text{or}\ 8\mid n,
\]
and gives an explicit uniquely-decodable eight-word code corresponding to the frozen anchors, with a precisely conditional Restivo–Salemi–Sportelli connection.

**The unrestricted higher-prime-power target remains NOT_PROVED.** No anchored counterexample is supplied. The new exclusion is a specified whole-odd-factor family with a restricted two-adic allocation, not closure of all allocations.

**Scientific executable status: NOT_RUN.** No scientific program, solver, build, test, or interpreter calculation was executed. All mathematical work below is written algebra or finite word cancellation.

## 1. Inputs, permissions, and chronology

Assigned wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f497-shor-cyclic-tiling-two-prime-powers-actual-anchor-frontier/`

Parent-supplied observations:

- Manifest SHA-256: `5f682b27a6da5acf6f6b8a677c31ea02d7908fab52caa4816bc29356f562f2bb`.
- Freeze-receipt SHA-256: `e53f2465472aba269efdab7369bf45160a8738d0249d34acd7eb379ad6893b01`.
- Literal-packet SHA-256: `536bdd333042d3feb0e6cc48b2a6942fb4e24f913ce83f410525fd66110601f2`.
- S1 disposition SHA-256: `56e32c8ba0e049a6bc913d4859aa21b51c9c70e6505c266e6d589a7e9b449195`.

These hashes and the supplied clock observation are attributed to **Main’s metadata supply**, not to child-native execution.

Actual read/work order:

1. Read the complete 91-LF manifest, 34-LF freeze receipt, all ten status-only controls, and parent metadata supply.
2. Delivered a direct pre-body ACK to Main.
3. Read the literal packet in ordered raw windows LF 1–20 and LF 21–24, including its ending. This displayed the complete 22-LF S1 body.
4. Began the mathematical work only afterward.
5. Public-source searches subsequently located Christophe Cordero’s *Factorizations of Cyclic Groups and Bayonet Codes*. I read its Section 1 statement of Theorem 1.1, surrounding definition, and relevant bibliography. I did **not** obtain or independently verify the original 1989 Restivo–Salemi–Sportelli proof.
6. No held scientific payload or its consumers were opened or used. The quarantine records were read only for status and permissions.

The current runtime forbids working-tree edits and scientific shell execution. This complete body is therefore returned for Main to materialize; no write or execution bypass was attempted.

## 2. Actual cyclic target

Throughout the cyclic argument, assume
\[
P\oplus Q=\mathbb Z_n,\qquad n>14,
\]
with
\[
\{0,3,8,11\}\subseteq P,\qquad
\{0,1,7,13,14\}\subseteq Q.
\]

Here directness means that every residue has **exactly one ordered representation**
\[
x=p+q\pmod n,\qquad (p,q)\in P\times Q.
\]
In particular,
\[
|P||Q|=n.
\]

All collisions below are modulo \(n\). The full anchor requirements remain in force even where a particular necessary-condition proof uses only some anchors.

## 3. Coprime dilation, including multiplicities

### Lemma 1

If \(A\oplus B=\mathbb Z_n\) and \(k\) is a positive integer satisfying
\[
\gcd(k,|A|)=1,
\]
then multiplication by \(k\) is injective on \(A\), and
\[
kA\oplus B=\mathbb Z_n.
\]

No hypothesis \(\gcd(k,n)=1\) is needed.

### Proof

First let \(k=\ell\) be prime with \(\ell\nmid |A|\).

Use the integral group ring \(\mathbb Z[\mathbb Z_n]\), writing the formal sums of the sets as \(A(X),B(X)\), and
\[
J(X)=1+X+\cdots+X^{n-1}.
\]
Directness gives
\[
A(X)B(X)=J(X).
\]

Reduction modulo \(\ell\), Frobenius, and Fermat’s little theorem give
\[
\begin{aligned}
A(X^\ell)B(X)
&=A(X)^\ell B(X)\\
&=A(X)^{\ell-1}J(X)\\
&=|A|^{\ell-1}J(X)\\
&=J(X)
\end{aligned}
\]
in \(\mathbb F_\ell[\mathbb Z_n]\).

For the corresponding integral product, retain the multiplicity of every \(\ell a\); do not first replace it by an unweighted image set. Its coefficient at \(x\) is
\[
c_x=\#\{(a,b)\in A\times B:\ell a+b=x\pmod n\}.
\]
Thus \(c_x\) is a nonnegative integer and
\[
c_x\equiv1\pmod\ell.
\]
Consequently \(c_x\ge1\). Also
\[
\sum_{x\in\mathbb Z_n}c_x=|A||B|=n.
\]
There are \(n\) coefficients, so every coefficient is exactly one.

If two distinct elements of \(A\) had the same multiplied image, adding any fixed element of the nonempty set \(B\) would produce a coefficient at least two. Thus multiplication is injective on \(A\), and the multiplied sets tile directly.

Factor a general positive \(k\) into primes and apply this result successively. Cardinality remains \(|A|\) at every step, so every prime factor of \(k\) remains admissible. ∎

The symmetric statement holds when dilating \(B\).

## 4. Universal anchor divisibility

### Proposition 2

Every tiling in Section 2 satisfies
\[
2\mid |P|,\qquad 2\cdot3\cdot5\cdot11\mid |Q|.
\]

### Proof that \(2\mid |P|\)

If \(|P|\) were odd, Lemma 1 would give
\[
2P\oplus Q=\mathbb Z_n.
\]
But its ordered pairs arising from \(3,0\in P\) and \(1,7\in Q\) give
\[
2\cdot3+1=2\cdot0+7.
\]
The two \(Q\)-entries are distinct modulo \(n\), since \(n>14\). This contradicts directness.

### Proof of the tail divisibility

If \(|Q|\) were odd, dilation of \(Q\) by \(8\) would preserve directness, contradicting
\[
8+8\cdot0=0+8\cdot1.
\]
Hence \(2\mid |Q|\).

If \(3\nmid |Q|\), dilation by \(3\) contradicts
\[
3+3\cdot0=0+3\cdot1.
\]
Hence \(3\mid |Q|\).

If \(5\nmid |Q|\), dilation by \(5\) contradicts
\[
8+5\cdot0=3+5\cdot1.
\]
Hence \(5\mid |Q|\).

If \(11\nmid |Q|\), dilation by \(11\) contradicts
\[
11+11\cdot0=0+11\cdot1.
\]
Hence \(11\mid |Q|\).

All displayed pairs are distinct ordered pairs of the dilated factors. The primes are distinct, proving the assertion. ∎

In particular,
\[
660\mid n,\qquad v_2(|P|)\ge1,\qquad v_2(|Q|)\ge1.
\]

This proposition also excludes **all odd head cardinalities**, without any restriction on their odd prime factors or exponents.

## 5. The new whole-odd-factor exclusion

### Theorem 3

There is no tiling in Section 2 satisfying
\[
v_2(n)=2,\qquad 3\nmid |P|.
\]

Equivalently, every anchored tiling satisfies
\[
3\mid |P|\quad\text{or}\quad8\mid n.
\]

### Proof

Suppose
\[
n=4m,\qquad m\ \text{odd},\qquad 3\nmid |P|.
\]

Choose an integer \(k\) satisfying
\[
2k\equiv3\pmod m
\]
and choose it odd. This is possible because \(2\) is invertible modulo the odd integer \(m\), and adding \(m\) changes parity. A positive odd representative can be chosen.

I claim that
\[
\gcd(k,|P|)=1.
\]

The prime \(2\) does not divide \(k\). Every odd prime \(r\mid |P|\) divides \(m\), since \(|P|\mid n=4m\). If such an \(r\) also divided \(k\), reducing \(2k\equiv3\pmod m\) modulo \(r\) would give \(r\mid3\). That would mean \(r=3\), contrary to \(3\nmid |P|\). The claim follows.

Moreover,
\[
m\mid 2k-3
\]
implies
\[
4m\mid8k-12,
\]
so
\[
8k\equiv12\pmod n.
\]

Lemma 1 therefore gives the direct tiling
\[
kP\oplus Q=\mathbb Z_n.
\]
Its actual anchors yield
\[
k\cdot8+1\equiv k\cdot0+13\pmod n,
\]
a collision between distinct ordered pairs. This is impossible. ∎

The multiplier need not be a unit modulo \(n\). Its admissibility is established by coprimality with \(|P|\), exactly as required by Lemma 1.

### Corollary 4 — arbitrary odd factors

For all odd positive integers \(u,w\), with no restrictions on common prime factors or their multiplicities, an anchored tiling cannot satisfy
\[
|P|=2u,\qquad |Q|=2w,\qquad 3\nmid u.
\]

Indeed, \(n=4uw\) has two-adic valuation two, so Theorem 3 applies.

The actual anchors additionally require \(165\mid w\), but this does not weaken the exclusion: the proof allows those primes to be shared with \(u\).

### Corollary 5 — higher \(5\)- and \(11\)-powers

For every \(p\in\{5,11\}\) and every \(j\ge2\), there is no anchored tiling with
\[
|P|=2p^j,\qquad |Q|=2w,\quad w\ \text{odd}.
\]

Thus a prospective anchored tiling with head \(2p^j\) must have
\[
v_2(|Q|)\ge2.
\]

The odd part of \(|Q|\) is unrestricted by this proof beyond the necessary anchor divisibility. In particular, arbitrary additional \(p\)-powers in \(|Q|\) are allowed in the contradiction.

This is a genuine higher-exponent exclusion, but **only for the stated two-adic allocation**.

### Necessary order consequence

Every anchored tiling must satisfy at least one of
\[
2^3\cdot3\cdot5\cdot11\mid n
\]
or
\[
2^2\cdot3^2\cdot5\cdot11\mid n.
\]

To see this, Proposition 2 already supplies \(2^2\cdot3\cdot5\cdot11\mid n\). If \(8\nmid n\), Theorem 3 gives \(3\mid |P|\), while Proposition 2 gives \(3\mid |Q|\), so \(9\mid n\).

These are necessary conditions, not existence claims.

## 6. Why the frozen fiber nonconstancy step does not automatically extend

Consider the original higher-power family
\[
|P|=2^a p^j,\qquad p\in\{3,5,11\},\qquad j\ge2.
\]
Write
\[
n=2^{a+b}p^{j+t}R,\qquad
|Q|=2^b p^tR,
\]
where
\[
a,b,t\ge1,\qquad \gcd(R,2p)=1,\qquad (165/p)\mid R.
\]

The condition \(t\ge1\) is forced by the actual tail anchors; \(p\) is shared.

Because \(\gcd(R,|P|)=1\), dilation by \(R\) gives
\[
RP\oplus Q=\mathbb Z_n.
\]
The first factor lies in the subgroup \(R\mathbb Z_n\). Restriction to any residue class modulo \(R\), followed by identification of that subgroup with
\[
H=\mathbb Z_{2^{a+b}p^{j+t}},
\]
gives a quotient-fiber tiling
\[
A\oplus B_r=H,
\]
with
\[
|A|=2^a p^j,\qquad |B_r|=2^b p^t.
\]

Suppose \(B_r\) is constant modulo \(p^2\). Its elements then lie in one coset of the index-\(p^2\) subgroup
\[
L=p^2H.
\]
For each coset of \(L\), directness forces the corresponding number of \(A\)-elements to be
\[
\frac{|L|}{|B_r|}
=
\frac{2^{a+b}p^{j+t-2}}{2^b p^t}
=
2^a p^{j-2}.
\]

For \(j=1\), the expression is \(2^a/p\), which is not an integer. That is the frozen nonconstancy contradiction.

For \(j\ge2\), it is an integer. The same counting step no longer gives a contradiction.

### Written local barrier control, not an anchored counterexample

The local counting configuration is realizable in an actual cyclic quotient, including a shared \(p\)-factor and both tail parities.

Let
\[
H'=\mathbb Z_{p^v}\times\mathbb Z_{2^{a+1}},
\qquad v\ge j+1,\quad j\ge2,\quad a\ge1.
\]
Set
\[
A_p=\{0,1,\ldots,p^j-1\},\qquad
B_p=\{p^jh:0\le h<p^{v-j}\},
\]
and
\[
A_2=\{2h:0\le h<2^a\},\qquad B_2=\{0,1\}.
\]
Then
\[
(A_p\times A_2)\oplus(B_p\times B_2)=H'.
\]

The first coordinate is direct by quotient and remainder upon division by \(p^j\); the second is direct by parity. CRT identifies \(H'\) with a cyclic group.

The second factor:

- is constant modulo \(p^2\);
- has both parities;
- has cardinality \(2p^{v-j}\), hence shares \(p\) with the first factor.

This example **does not satisfy the frozen anchors**: its first factor is entirely even, so it misses the head anchor \(3\). It is not an original-target witness and receives no credit as one. Its sole purpose is to show concretely why local fiber integrality and parity alone cannot reproduce the old \(j=1\) contradiction.

**First unpaid step in extending the frozen route:** replace its every-fiber-nonconstant-modulo-\(p^2\) premise with a valid anchored argument for \(j\ge2\), or obtain a different contradiction that uses the undilated head anchors. This return supplies neither for the remaining allocations.

## 7. Actual word code and the conditional border bridge

The eight literal binary words canonically represented by the frozen left/right anchors are
\[
X=\{b,\ a^3b,\ a^8b,\ a^{11}b,\ ba,\ ba^7,\ ba^{13},\ ba^{14}\}.
\]

I do not assert that this list exhausts an unsupplied printed problem statement. The claim here concerns exactly these words and their stated anchor bridge.

### Proposition 6 — \(X\) is uniquely decodable

The nonzero positive differences between the left exponents \(\{0,3,8,11\}\) are
\[
D_P=\{3,5,8,11\},
\]
whereas those between the right exponents \(\{0,1,7,13,14\}\) are
\[
D_Q=\{1,6,7,12,13,14\}.
\]
These sets are disjoint.

Here is the complete finite cancellation argument. The nonempty residuals obtained from proper prefix comparisons between distinct words of \(X\) are initially
\[
\{a^d:d\in D_Q\}.
\]
They arise only from comparisons between words \(ba^q\).

Comparing these residuals with words of \(X\) gives exactly the possible next residuals
\[
\{ab,\ a^2b,\ a^4b,\ a^5b,\ a^7b,\ a^{10}b\}.
\]
Indeed, a comparison is possible only against \(a^pb\), with \(p\in\{3,8,11\}\) and \(d<p\), and leaves \(a^{p-d}b\). No \(d=p\) occurs.

None of those six residuals equals a codeword or has a prefix comparison with a codeword:

- they start with \(a\), excluding every \(ba^q\);
- their left exponents are not \(3,8,11\), so comparison with \(a^3b,a^8b,a^{11}b\) fails at the first position where one word has \(b\).

The next residual set is empty, and the empty word was never obtained. Any ambiguous factorization would generate a chain of such uncancelled suffixes ending at the empty word. No such chain exists. Thus \(X\) is uniquely decodable. ∎

### Precisely named external import

The conditional import is the **Restivo–Salemi–Sportelli factorization/border theorem**, in this formulation:

> If \(M\) is a finite maximal code containing \(b\) and \(a^n\), the ordered pair
> \[
> P_M=\{i\ge0:\exists s\ge1,\ a^ib^s\in M\},
> \]
> \[
> Q_M=\{j\ge0:\exists s\ge1,\ b^sa^j\in M\}
> \]
> is a factorization of size \(n\).

This formulation appears as Theorem 1.1 in [Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*](http://www.normalesup.org/~cordero/Publications/Factorizations_and_Bayonet_Codes.pdf), Section 1. Its bibliography attributes the result to:

Antonio Restivo, Sergio Salemi, and Tecla Sportelli, “Completing codes,” *RAIRO—Theoretical Informatics and Applications* **23**(2), 135–147, 1989.

Cordero also recalls that a finite maximal code has a pure-letter order \(n\) with \(a^n\in M\), citing a separate standard reference. Neither that general fact nor the original RSS proof is independently established here.

### Conditional consequence for actual words

Assume the displayed RSS theorem applies to a finite maximal code \(M\) containing \(X\) and \(a^n\). Then, in the stated order,
\[
\{0,3,8,11\}\subseteq P_M,\qquad
\{0,1,7,13,14\}\subseteq Q_M.
\]
The factorization has \(n=|P_M||Q_M|\ge4\cdot5=20\), so it lies within the cyclic scope \(n>14\).

Consequently,
\[
2\mid |P_M|,\qquad330\mid |Q_M|,
\]
and
\[
3\mid |P_M|\quad\text{or}\quad8\mid n.
\]
In particular, it cannot have
\[
|P_M|=2p^j,\qquad v_2(|Q_M|)=1,
\quad p\in\{5,11\},\ j\ge2.
\]

To apply this to every finite maximal completion without separately assuming \(a^n\in M\), one must additionally supply the pure-letter-order fact. This distinction is not hidden inside the cyclic proof.

Unique decodability of \(X\) is proved above; **nonexistence of a finite maximal completion is not proved**.

## 8. Literal remaining obligations

For the pure one-odd-prime higher-power family, the unresolved parameters **under the results used in this return** are:

- \(p=3\):
  \[
  j\ge2,\quad a,b,t\ge1,\quad
  n=2^{a+b}3^{j+t}R,\quad
  55\mid R,\quad \gcd(R,6)=1.
  \]

- \(p=5\):
  \[
  j\ge2,\quad a,b,t\ge1,\quad a+b\ge3,
  \]
  \[
  n=2^{a+b}5^{j+t}R,\quad
  33\mid R,\quad \gcd(R,10)=1.
  \]

- \(p=11\):
  \[
  j\ge2,\quad a,b,t\ge1,\quad a+b\ge3,
  \]
  \[
  n=2^{a+b}11^{j+t}R,\quad
  15\mid R,\quad \gcd(R,22)=1.
  \]

In each case,
\[
|P|=2^ap^j,\qquad |Q|=2^bp^tR,
\]
and all original anchors and literal directness remain required.

These parameter sets are **not asserted feasible**. They are not a globally audited frontier against every historical disposition; they identify what this candidate does not settle.

For arbitrary mixed odd factors in the head, the new exclusion is exactly the family of Corollary 4, together with the universal exclusion of odd head cardinality. No broader mixed-factor closure is claimed.

## 9. Execution, verification, and assurance ceiling

- **Scientific machine execution:** NOT_RUN.
- **Executable source/results:** none; no scientific program was attempted or used.
- **Written checks supplied:** full group-ring coefficient argument; all anchor collisions; the CRT multiplier argument; the quotient-fiber cardinality calculation; the symbolic local barrier tiling; complete word-residual cancellation.
- **Original RSS source verification:** not performed. The code bridge remains conditional on the explicitly stated import.
- **Independent disjoint review and parent disposition:** not yet performed.
- **Novelty:** not assessed or claimed.
- **Human, kernel/formal, independent-model-family, or global Shor-completion credit:** none.

**Final result:** a complete written candidate excluding arbitrary odd-factor heads and tails with exactly one factor of two each when \(3\nmid |P|\), thereby covering higher \(5\)- and \(11\)-power heads in that allocation. The unrestricted higher-power anchored problem and the unrestricted finite-completion problem remain unproved.