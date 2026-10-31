# F590 — Independent WRITTEN review

**Verdict: SUPPORTED at the stated structural scope.**  
**Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The candidate proves the following statement:

> If actual sets satisfy
> \[
> P\oplus Q=\mathbb Z_n,\qquad n>14,
> \]
> with
> \[
> \{0,3,8,11\}\subseteq P,\qquad
> \{0,1,7,13,14\}\subseteq Q,
> \]
> and the actual head admits a direct factorization
> \[
> P=\{u,u+d\}\oplus C
> \]
> with distinct displayed points modulo \(n\), then
> \[
> \gcd(d,n)\ge 15.
> \]

This is **not** unrestricted anchored-tiling nonexistence. Neither the four head anchors nor a pairing of a CRT projection establishes the required actual two-point direct factor.

## 1. Evidence, chronology, and method boundary

### Frozen evidence

- Manifest SHA-256: `6f967df93bb01fd4aaa220be749f28f69d7353d40306bce2d3e66d79b6b98f1c`.
- Freeze-receipt SHA-256: `f35ec6248d565fc2c002d04c5e8131340b4abd2b690d271c545cf9aa5d8150cf`.
- Literal-packet SHA-256, as supplied by the parent: `6270a7c45f80820cae59dabe8c512e091ea9410924e092a749a8361cd4abecbc`.
- **S1:** F569 author candidate, `review-v1.md`, SHA-256 `63a833c5c54b369d072208a0543d15a9b1e4b51e90b4c6b8622cb75a3d333909`, complete logical labels 1–694.
- **S2:** Earlier adopted actual-anchor disposition, SHA-256 `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`, complete labels 1–31.

The live hashes, byte/LF counts, and clock `2026-10-30T13:57:02-0700 PDT` are **parent-supplied observations**, not my own hash execution, native clock observation, or observed start time.

### Actual review sequence

1. Read the complete manifest, freeze receipt, parent-live metadata, and all **12** status-only controls, including their endings.
2. Sent the direct administrative pre-body ACK to Main.
3. Read the entire literal packet in ordered raw windows of at most 20 LF, from packet LF 1 through its ending at LF 727.
4. Began the written reconstruction below only after completing that read.

No scientific program, interpreter, CAS, solver, enumeration, replay, build, test, lint, or formatter was used. No additional selected gcd, parameter instance, trial tiling, or private diagnostic was introduced. The support checks below exhaust the candidate’s explicitly assigned cases and claimed support sets; they are written proof reconstruction, not machine results.

No linked public source, prior reviewer body, sibling result, author code, or held scientific payload was followed. All quarantine controls were used only as status exclusions.

The only earlier mathematical import used for the later CRT discussion is **S2 LF 11**, the adopted coprime-cardinality dilation lemma. The new small-gcd obstruction itself does not require that import.

## 2. Claim dispositions

| Claim | Source labels | Disposition |
|---|---|---|
| Actual-factor reduction, alternating cycles, orientation, and weighted coefficients | S1 69–196 | **SUPPORTED** |
| Immediate exclusions \(g=1,2,4,6,7,12,13,14\) | S1 198–213 | **SUPPORTED** |
| Exclusions \(g=3,5\) | S1 221–265 | **SUPPORTED** |
| Exact support restrictions and weighted contradiction for \(g=8\) | S1 267–337 | **SUPPORTED** |
| Antipodal contradiction for \(g=9\) | S1 339–369 | **SUPPORTED** |
| Exact support restrictions and weighted contradiction for \(g=10\) | S1 371–448 | **SUPPORTED** |
| Exact support restrictions and weighted contradiction for \(g=11\) | S1 450–517 | **SUPPORTED** |
| Uniform conclusion \(\gcd(d,n)\ge15\) for actual two-point direct factors | S1 20–36, 519–539 | **SUPPORTED** |
| CRT graph, fiber cardinalities, original coupled equations, and lifting boundary | S1 541–623; S2 11 | **SUPPORTED at the named family and import scope** |
| Every anchored head has an excluded two-point factor | Explicitly not asserted | **NOT PROVED** |
| Unrestricted anchored nonexistence, feasibility of residual families, or finite-maximal-completion nonexistence | Explicitly excluded | **NOT PROVED by this candidate** |

## 3. Reconstruction of the actual-factor reduction

Absorbing \(u\) into \(C\) gives
\[
P=\{0,d\}\oplus C.
\]
The two actual direct sums imply the actual triple direct sum
\[
\{0,d\}\oplus C\oplus Q=\mathbb Z_n.
\]

In particular, \(C+Q\) has no repeated ordered representations: such a repetition, with the zero element of the two-point factor fixed, would contradict the original directness. Thus
\[
T=C\oplus Q
\]
is an actual subset of \(\mathbb Z_n\), and
\[
\{0,d\}\oplus T=\mathbb Z_n.
\]

Let \(g=\gcd(d,n)\) and \(t=1_T\). Exact directness gives
\[
t(x)+t(x-d)=1.
\]
Applying this at successive points yields
\[
t(x)=t(x-2d).
\]

Every \(d\)-cycle has length \(n/g\). Alternation is impossible around an odd cycle, so \(n/g\) must be even. Consequently \(2g\mid n\). Writing \(d=gh\) and \(n=gm\), with \(\gcd(h,m)=1\) and \(m\) even, makes \(h\) odd and gives
\[
\gcd(2d,n)=g\gcd(2h,m)=2g.
\]

Therefore \(T\) is a union of complete residue classes modulo \(2g\). There is an occupied set \(V\subseteq\mathbb Z_{2g}\) such that
\[
T=\{x:x\bmod 2g\in V\}.
\]
Because \(d\equiv g\pmod{2g}\), the alternating equation becomes
\[
V\sqcup(V+g)=\mathbb Z_{2g}.
\]
Thus \(|V|=g\), and \(V\) contains no antipodal pair.

### Orientation is legitimate and preserves the original head

Since \(0\in P=\{0,d\}\oplus C\), either \(0\in C\) or \(-d\in C\). In the second case,
\[
P=\{0,-d\}\oplus(C+d),
\]
and \(0\in C+d\). This reverses the two-point orientation without changing \(P\), \(Q\), or \(g\). Both orientations project to \(\{0,g\}\) modulo \(2g\).

Hence the candidate may normalize so that \(c_0>0\), where \(c_i\) counts actual elements of \(C\) in residue \(i\). It follows from the actual tail anchors that
\[
S_g=\{0,1,7,13,14\}\bmod 2g\subseteq V.
\]
Every head anchor \(a\in\{0,3,8,11\}\) requires projected \(C\)-residue \(a\) or \(a-g\).

### The coefficient equation preserves all multiplicities

Define
\[
c_i=\#\{c\in C:c\equiv i\pmod{2g}\},\qquad
q_j=\#\{q\in Q:q\equiv j\pmod{2g}\},
\]
and \(L=n/(2g)\).

The number of actual ordered pairs \((c,q)\) whose sum projects to \(s\) is
\[
\sum_i c_iq_{s-i}.
\]
Because \(C\oplus Q=T\) is injective and every occupied residue class of \(T\) contains exactly \(L\) original elements,
\[
\sum_i c_iq_{s-i}=L\,1_V(s).
\]

This is not an unweighted quotient tiling. Neither \(c_i\) nor \(q_j\) is assumed to be a zero-one coefficient. The argument also covers \(L=1\); no strict inequality below requires a larger fiber.

## 4. All fourteen gcd cases

### 4.1 Eight immediate antipodal exclusions

Each row uses two actual tail anchors. Their difference is \(g\) modulo \(2g\), so their projections cannot both belong to \(V\).

| \(g\) | Actual tail difference | Reduction modulo \(2g\) |
|---:|---|---|
| 1 | \(1-0=1\) | \(1\) |
| 2 | \(14-0=14\) | \(2\) |
| 4 | \(13-1=12\) | \(4\) |
| 6 | \(7-1=6\) | \(6\) |
| 7 | \(7-0=7\) | \(7\) |
| 12 | \(13-1=12\) | \(12\) |
| 13 | \(13-0=13\) | \(13\) |
| 14 | \(14-0=14\) | \(14\) |

These exclude exactly \(g=1,2,4,6,7,12,13,14\).

### 4.2 \(g=3\)

Modulo six,
\[
S_3=\{0,1,2\}.
\]
Its cardinality equals \(|V|=3\), so \(V=S_3\).

Every projected \(C\)-residue \(c\) must satisfy \(S_3+c\subseteq S_3\), hence equality. This cyclic interval has trivial translation stabilizer: zero is its unique point whose predecessor lies outside the set, and a stabilizing translation must preserve that point.

Thus \(C\) projects only to zero, and \(P\) projects into \(\{0,3\}\). But the actual head anchor \(8\) projects to \(2\). Contradiction.

### 4.3 \(g=5\)

Modulo ten,
\[
S_5=\{0,1,3,4,7\},
\]
so again \(|S_5|=|V|=5\) forces \(V=S_5\).

A translation stabilizer is a subgroup whose order divides both ten and five. If nontrivial, it therefore has order five, and \(S_5\) would be one parity coset. Its containing both zero and one excludes that possibility.

Consequently \(C\) projects only to zero, and \(P\) projects into \(\{0,5\}\), contrary to the actual anchor \(3\).

### 4.4 \(g=8\): supports and weighted contradiction

Work modulo sixteen with
\[
S=\{0,1,7,13,14\}.
\]
The head anchor \(3\) requires \(C\)-residue \(3\) or \(11\). Residue \(11\) would give \(11+13=8\), antipodal to zero. Hence
\[
c_0,c_3>0.
\]

The forced union is
\[
V=S\cup(S+3)=\{0,1,3,4,7,10,13,14\}.
\]
It contains eight elements and therefore exhausts \(V\).

Since \(q_0>0\), any projected \(C\)-residue must already lie in \(V\). Among those candidates, all residues other than zero and three fail the required inclusion \(S+c\subseteq V\):

| Rejected \(c\) | Actual tail residue used | Sum modulo sixteen outside \(V\) |
|---:|---:|---:|
| 1 | 1 | 2 |
| 4 | 1 | 5 |
| 7 | 1 | 8 |
| 10 | 1 | 11 |
| 13 | 14 | 11 |
| 14 | 1 | 15 |

Both zero and three satisfy the inclusion. Thus the claimed allowable \(C\)-support is exactly \(\{0,3\}\).

Because both occur,
\[
\operatorname{supp}(Q\bmod16)
\subseteq V\cap(V-3)
=\{0,1,4,7,10,13,14\}.
\]
In particular \(q_3=q_{11}=0\). The exact equations at residues \(3,14,0,1\) are
\[
L=c_3q_0,\qquad L=c_0q_{14},
\]
\[
L=c_0q_0+c_3q_{13}>c_0q_0,
\]
\[
L=c_0q_1+c_3q_{14}>c_3q_{14}.
\]

The strict terms are positive because \(c_0,c_3>0\) and the original anchors give \(q_1,q_{13}>0\). The comparison divisors \(q_0,q_{14}\) are also positive actual-anchor multiplicities.

The first and third equations imply \(c_3>c_0\); the second and fourth imply \(c_0>c_3\). Contradiction.

### 4.5 \(g=9\): antipodes from forced head choices

Work modulo eighteen.

- The head anchor \(3\) requires \(C\)-residue \(3\) or \(12\). Residue \(3\) would put \(3+7=10\) opposite the actual tail residue \(1\). Hence \(12\) occurs.
- The head anchor \(8\) requires \(C\)-residue \(8\) or \(17\). Residue \(8\) would put \(8+1=9\) opposite zero. Hence \(17\) occurs.

The actual tail anchors \(14\) and zero then force
\[
12+14=8\pmod{18},\qquad 17+0=17\pmod{18}
\]
into \(V\). They differ by nine. Contradiction.

### 4.6 \(g=10\): supports and weighted contradiction

Work modulo twenty.

The original head anchors force:

- \(3\) or \(13\): reject \(3\), since \(3+7=10\) is opposite zero; therefore \(13\) occurs.
- \(8\) or \(18\): reject \(18\), since \(18+13=11\) is opposite one; therefore \(8\) occurs.
- \(11\) or \(1\): reject \(11\), since \(11+0=11\) is opposite one; therefore \(1\) occurs.

Together with normalization, the mandatory support is
\[
M=\{0,1,8,13\}.
\]
The forced sumset is
\[
V=S+M=\{0,1,2,6,7,8,9,13,14,15\}.
\]
Its ten elements exhaust \(V\).

For \(C\), candidates must lie in \(V\). The four excluded candidates are witnessed as follows:

| Rejected \(c\) | Actual tail residue used | Sum modulo twenty outside \(V\) |
|---:|---:|---:|
| 2 | 1 | 3 |
| 6 | 13 | 19 |
| 9 | 1 | 10 |
| 15 | 1 | 16 |

The remaining candidates satisfy \(S+c\subseteq V\). Hence
\[
\operatorname{supp}(C\bmod20)\subseteq
K=\{0,1,7,8,13,14\}.
\]

For \(Q\), membership requires \(q+M\subseteq V\). All of \(S\) passes because \(S+M=V\). The other candidates in \(V\) fail:

| Rejected \(q\) | Mandatory \(C\)-residue used | Sum modulo twenty outside \(V\) |
|---:|---:|---:|
| 2 | 1 | 3 |
| 6 | 13 | 19 |
| 8 | 8 | 16 |
| 9 | 1 | 10 |
| 15 | 1 | 16 |

Thus the projected \(Q\)-support is exactly \(S\), with every member positive because it is an actual anchor.

Using these supports, residues six and nine have precisely
\[
L=c_{13}q_{13},\qquad L=c_8q_1.
\]

For completeness, the relevant equations at one and fourteen are
\[
L=c_0q_1+c_1q_0+c_7q_{14}+c_8q_{13}+c_{14}q_7
>c_8q_{13},
\]
\[
L=c_0q_{14}+c_1q_{13}+c_7q_7+c_{13}q_1+c_{14}q_0
>c_{13}q_1.
\]
All omitted terms are zero by the established supports. The strict inequalities use \(c_0q_1>0\) and \(c_0q_{14}>0\).

Comparing with the two singleton equations, using \(q_{13},q_1>0\), gives
\[
c_{13}>c_8,\qquad c_8>c_{13}.
\]
Contradiction. In particular, this reconstruction does **not** incorrectly treat \(q_{13}\) as absent.

### 4.7 \(g=11\): supports and weighted contradiction

Work modulo twenty-two.

- The head anchor \(3\) requires \(C\)-residue \(3\) or \(14\). Residue \(3\), using the actual tail zero, is opposite \(14\in S\). Therefore \(14\) occurs.
- The head anchor \(8\) requires \(C\)-residue \(8\) or \(19\). Residue \(19\) would put \(19+14=11\) opposite zero. Therefore \(8\) occurs.

Thus \(c_0,c_8,c_{14}>0\), and
\[
V=S+\{0,8,14\}
=\{0,1,5,6,7,8,9,13,14,15,21\}.
\]
Its eleven elements exhaust \(V\).

The other \(C\)-candidates in \(V\) are all excluded:

| Rejected \(c\) | Actual tail residue used | Sum modulo twenty-two outside \(V\) |
|---:|---:|---:|
| 1 | 1 | 2 |
| 5 | 7 | 12 |
| 6 | 13 | 19 |
| 7 | 13 | 20 |
| 9 | 1 | 10 |
| 13 | 7 | 20 |
| 15 | 1 | 16 |
| 21 | 13 | 12 |

The three mandatory residues do satisfy the required inclusion. Therefore the projected \(C\)-support is exactly \(\{0,8,14\}\).

The allowable \(Q\)-support is
\[
V\cap(V-8)\cap(V-14)
=\{0,1,7,13,14,15,21\}.
\]
The excluded candidates \(5,6,8,9\) fail respectively at sums \(5+14=19\), \(6+14=20\), \(8+8=16\), and \(9+8=17\). Each residue in the displayed allowable set has both required translates in \(V\).

The exact equations at six and eight are
\[
L=c_{14}q_{14},\qquad L=c_8q_0.
\]
At zero and fourteen they are
\[
L=c_0q_0+c_8q_{14}>c_8q_{14},
\]
\[
L=c_0q_{14}+c_{14}q_0>c_{14}q_0.
\]
The actual anchors give \(q_0,q_{14}>0\), and normalization gives \(c_0>0\). Therefore the two comparisons imply
\[
c_{14}>c_8,\qquad c_8>c_{14}.
\]
Contradiction.

### 4.8 Exhaustion and conclusion

The eight immediate cases and the six cases \(3,5,8,9,10,11\) exhaust every positive integer \(g\le14\).

If \(n/g\) is odd, the alternating-cycle argument already rules out the hypothesized factorization. If it is even, the preceding fourteen-case argument applies. Therefore every actual two-point direct factor has
\[
\boxed{\gcd(d,n)\ge15}.
\]

The named differences \(3,5,8,11\) are consequently excluded, since their gcd with \(n\) cannot reach fifteen.

## 5. CRT consumer and exact lifting boundary

This section uses **S2 LF 11**, precisely the adopted statement that, for actual \(A\oplus B=\mathbb Z_n\), a positive multiplier coprime to \(|A|\) acts injectively on \(A\) and preserves the direct factorization with the same actual \(B\). It does not require that multiplier to be a unit modulo \(n\).

For the listed families,
\[
H=2^{a+b}p^{j+t},\qquad n=HR,\qquad
|P|=2^ap^j,\qquad |Q|=2^bp^tR,
\]
with \(p\in\{3,5,11\}\), \(j\ge2\), \(a,b,t\ge1\), and \(\gcd(R,2p)=1\), one has \(\gcd(H,R)=1\).

Choose the CRT multiplier
\[
k\equiv1\pmod H,\qquad k\equiv0\pmod R.
\]
Since \(|P|\mid H\), this has \(\gcd(k,|P|)=1\). In CRT coordinates multiplication by \(k\) sends
\[
(h,r)\longmapsto(h,0).
\]
Its injectivity on actual \(P\) therefore proves that the \(H\)-projection of \(P\) is injective. Thus the original head, not a replacement head, is a graph
\[
P=\{(a,f(a)):a\in A\}.
\]

The dilated head is \(A\times\{0\}\). Accordingly, for the original fibers
\[
Q_r=\{h:(h,r)\in Q\},
\]
the preserved direct tiling gives
\[
A\oplus Q_r=\mathbb Z_H,\qquad
|Q_r|=\frac{H}{|P|}=2^bp^t
\]
for every \(r\).

The original undilated factorization imposes the additional equations
\[
\sum_{a\in A}1_{Q_{r-f(a)}}(h-a)=1
\qquad\text{for every }(h,r).
\]
These count the actual original representations and correctly retain the coupling between \(f\) and different \(Q\)-fibers. Separate common-complement statements for the \(Q_r\) do not replace these equations.

### Anchor separation is valid throughout the listed families

The lower exponent bounds imply \(H>14\), so the displayed head coordinates do not collapse modulo \(H\).

For the other coordinate:

- \(p=3\): \(55\mid R\), so \(R\ge55\);
- \(p=5\): \(33\mid R\), so \(R\ge33\);
- \(p=11\): \(15\mid R\), so \(R\ge15\).

Thus all five actual tail integers \(0,1,7,13,14\) occupy distinct \(R\)-fibers. The original head anchors impose
\[
f(0)=0,\quad f(3)=3,\quad f(8)=8,\quad f(11)=11\pmod R,
\]
and each actual tail anchor belongs to its stated fiber with its first coordinate interpreted modulo \(H\).

### A projected pairing is not an actual two-point factor

If a proposed pairing in \(A\) has fixed difference \(\delta_H\), lifting it to one fixed original difference additionally requires
\[
f(a+\delta_H)-f(a)=\delta_R
\]
with the same \(\delta_R\) throughout that pairing.

Neither the anchor memberships nor the individual fiber tilings proves this condition. Moreover, even a successful lift must have its **original cyclic** difference checked against the small-gcd hypothesis. A CRT-coordinate difference alone does not establish that gcd.

The candidate identifies this missing bridge correctly and does not claim to have supplied it.

## 6. Scope, documentary correction, and assurance

### Exact supported progress

The new theorem uniformly excludes the structural subclass of actual anchored tilings whose actual head has a two-point direct factor with original gcd at most fourteen. Because its proof has no cardinality-allocation hypothesis, it applies within the listed higher-power and mixed-odd-head scopes.

It does not establish that every remaining head belongs to that subclass.

### Matters left unproved

This review grants no conclusion of:

- unrestricted anchored cyclic-tiling nonexistence;
- existence or feasibility of any residual allocation;
- a globally audited historical frontier;
- an actual anchored witness;
- unconditional RSS applicability or original-source verification;
- finite-maximal-completion nonexistence;
- novelty or worldwide priority.

The S2 finite-run narrative and literal-code claims were completely read as packet content, but no new replay, finite verification, or separate acceptance of those matters is claimed here.

### F569 control-count correction

S1 LF 63 expressly withdraws the earlier “11 controls” count and reports that all twelve controls had been read before the ACK. This is presented as a count-only correction, not a late completion of a missing read. I did not access the underlying F569 transcript, so this gate does not independently certify its earlier access chronology or clocks. No mathematical premise depends on that count.

For this F590 assignment, all twelve listed controls were read before my direct pre-body ACK.

### Final finding counts

- **Mathematical FATAL:** 0.
- **Mathematical MAJOR:** 0.
- **Mathematical MINOR:** 0.
- **New reviewer process deviation observed in this assignment:** none.

**Assurance ceiling:** independent same-harness written reconstruction at the frozen scope. No independent-family, human, formal/kernel, executed finite-check, source-equivalence, or novelty assurance is asserted.

**Overall correctness: correct.** The actual-set reduction, all fourteen gcd exclusions, and the multiplicity-preserving contradictions are supported. The later CRT consumer is supported using the specifically named adopted dilation lemma, and the candidate correctly leaves the missing global factor/lift step and unrestricted problems unproved.

**Confidence: 0.98.**