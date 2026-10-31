# author-candidate-v1.md

**Wave:** f361-ame48-t24-original-tensor-frontier  
**Status:** NEW AUTHOR CANDIDATE — UNREVIEWED; not an adopted result.

## 1. Result and exact target relation

For the **same normalized complex AME(4,6) tensor**, with exactly 48 nonzero coefficients and exactly 24 coefficients of modulus \(1/6\), the following new restrictions hold.

1. **No residual alphabet profile can contain both a three-symbol party and a four-symbol party.** Up to party permutations, this excludes the entire classes
   \[
   (3,4,4,4),\qquad(3,4,4,5),\qquad(3,4,5,5).
   \]
   These exclusions concern actual tensors, including every choice of nonzero complex amplitudes, not merely a failed numerical search.

2. Composed with the frozen no-distance-one/alphabet theorem, the residual alphabet profiles not excluded here are only
   \[
   \boxed{(3,5,5,5),\ (4,4,4,4),\ (4,4,4,5),\
   (4,4,5,5),\ (4,5,5,5),\ (5,5,5,5).}
   \]
   This is a list of **remaining necessary cases**, not an existence assertion.

3. The first three remaining profiles have forced residual symbol degrees:
   - \(3555\): the three-symbol party has degrees \((4,4,4)\); each five-symbol party has degrees \((3,3,2,2,2)\).
   - \(4444\): every party has degrees \((3,3,3,3)\).
   - \(4445\): every four-symbol party has degrees \((3,3,3,3)\), and the five-symbol party has degrees \((3,3,2,2,2)\).

4. There is an additional **actual complex-phase obstruction**: a residual degree-two symbol cannot have a paired-block partner internal to its two-symbol neighbor alphabet. Such an internal partner forces an isolated eight-word binary parity tensor whose simultaneous complex unitarity is algebraically impossible. This also gives a further necessary matching rule for the surviving \(3555\) class.

The composition retains the frozen **no-OLS(6) provenance** of the inherited no-distance-one/alphabet result. Nothing here backdates or removes that import.

No universal \(t=24\) exclusion, support-48 exclusion, or physically valid support-48 tensor is claimed.

## 2. Inputs, chronology, and methods

I read the complete manifest, freeze receipt, dispatch receipt, and parent metadata; then all seven listed status/permission controls; then the complete literal packet in its prescribed order **S1 → S2 → S3, including their endings**, before mathematical derivation.

The assigned manifest and receipt pins were:

- Manifest: `220c5f043f510c47ee2a197da37299dee3f5fcbe3db4b9810bcf549f6c01cc19`
- Receipt: `66d7a2d8a411b3ab225ff6390e8554d3b225eb7fc813896d103f1b207cee5187`

Matching hash/byte/LF observations are **parent-supplied metadata**, not child-executed checks. The supplied clock observations, including 09:13:58 and 09:21:28 PDT, are likewise parent observations; neither is asserted as my exact derivation or completion time.

Scientific imports:

- **S1:** inherited no-distance-one and residual alphabet sizes \(3,4,5\), at its stated no-OLS(6) provenance.
- **S2:** the actual same-tensor \(t=24\) residual setting. The elementary degree-two structure needed below is also reconstructed here.
- **S3:** read completely; its \(t=27\) exclusion is **not used** to infer any \(t=24\) conclusion.

The quarantine records were used only for status and permissions. No held f337/f340 or parent-claim-consumer scientific payload was accessed or used. No \(t=28\) argument is developed.

After initial algebraic work I consulted the public primary source cited in §8. All calculations below are written finite counting or algebra. **No scientific executable, numerical optimization, support enumeration, or solver was run.** Consequently there is no execution log or program output to claim. This complete body is returned inline for Main materialization; no working-tree file write is claimed.

## 3. Same-tensor residual structure

Let
\[
U=6\psi,\qquad
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\}.
\]
Thus \(|P|=|E|=24\).

Each of the three balanced flattenings of \(U\) is a \(36\times36\) unitary matrix. A unit-modulus entry exhausts its row and column. Therefore:

- \(P\) projects injectively onto each of the six coordinate-pair systems.
- No pair value used by \(P\) is used by \(E\).
- Removing the 24 singleton rows and columns leaves a \(12\times12\) unitary with 24 nonzeros.
- Every remaining row and column has degree at least two, since a singleton would have modulus one. Hence every remaining line has degree **exactly two**.

Two degree-two rows that intersect must have the same two columns: a one-column intersection cannot be orthogonal when both entries are nonzero. Column degree two then makes every connected residual block a full \(2\times2\) block.

For every pair \(ij\), write
\[
R_{ij}=\pi_{ij}(E).
\]
Then
\[
|R_{ij}|=12,
\]
each value in \(R_{ij}\) has exactly two extensions in \(E\), and
\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}. \tag{1}
\]

Equation (1) uses the **same \(P\) and \(E\) in every pair system**. It does not independently choose a different maximal-word packing for each cut.

Let \(A_i\) be the residual alphabet at party \(i\), and \(q_i=|A_i|\). Define
\[
p_i(a)=|\{w\in P:w_i=a\}|,\qquad
r_i(a)=|\{b:(a,b)\in R_{ij}\}|.
\]
From (1),
\[
r_i(a)=6-p_i(a), \tag{2}
\]
independently of \(j\). Moreover,
\[
|\{w\in E:w_i=a\}|=2r_i(a),\qquad
\sum_{a\in A_i}r_i(a)=12. \tag{3}
\]

A used symbol cannot have \(r_i(a)=1\). Otherwise exactly two residual words contain \(a\), and multiplicity two in every pair \(ij\) forces those words to agree at every other coordinate, contradicting distinct support words. Thus
\[
2\le r_i(a)\le\min_{j\ne i}q_j. \tag{4}
\]

## 4. Alphabet-shadow theorem

For a maximal word \(w\in P\), let
\[
k(w)=|\{i:w_i\in A_i\}|,
\qquad Q=\sum_iq_i.
\]

### Exact first moment

At party \(i\), equations (2)–(3) give
\[
\sum_{a\in A_i}p_i(a)=6q_i-12.
\]
Therefore
\[
C:=\sum_{w\in P}k(w)=6Q-48. \tag{5}
\]

### Exact second moment

All 12 residual pair values lie in \(A_i\times A_j\). By (1), exactly
\[
q_iq_j-12
\]
maximal words have both coordinates \(i,j\) in the residual alphabets. Consequently
\[
M:=\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}q_iq_j-72. \tag{6}
\]

These are exact identities, not upper bounds.

For integer \(k\in\{0,1,2,3,4\}\),
\[
\binom{k}{2}\ge k-1,\qquad
\binom{k}{2}\ge2k-3.
\]
Summing over the 24 maximal words gives
\[
M\ge C-24,\qquad M\ge2C-72. \tag{7}
\]

### Entire alphabet classes excluded

There cannot be two three-symbol parties, because \(R_{ij}\) would require 12 distinct values inside a \(3\times3\) product.

For the three remaining profiles containing both 3 and 4, equations (5)–(7) give:

| Sorted profile | \(C\) | Actual required \(M\) | Necessary lower bound for \(M\) |
|---|---:|---:|---:|
| \(3444\) | 42 | 12 | 18 |
| \(3445\) | 48 | 23 | 24 |
| \(3455\) | 54 | 35 | 36 |

Each is contradictory.

**Therefore every actual tensor in these three entire alphabet classes is excluded.** No assumption about real phases, equal residual moduli, or selected support examples enters this proof.

## 5. Forced structure in the remaining cases

Put
\[
n_s=|\{w\in P:k(w)=s\}|,\qquad 0\le s\le4.
\]
Besides \(\sum n_s=24\), equations (5)–(6) imply
\[
3n_0+n_1+n_4=M-2C+72. \tag{8}
\]

For \(3555,4444,4445\), the right side is zero. Hence all maximal words have \(k=2\) or \(3\), with:

| Profile | \((n_0,n_1,n_2,n_3,n_4)\) |
|---|---|
| \(3555\) | \((0,0,12,12,0)\) |
| \(4444\) | \((0,0,24,0,0)\) |
| \(4445\) | \((0,0,18,6,0)\) |

For a residual symbol \(a\in A_i\), let \(n_3(i,a)\) count maximal words containing it and having \(k=3\). Counting the other residual-alphabet coordinates of those words gives
\[
n_3(i,a)=Q-q_i-6-2r_i(a). \tag{9}
\]

Indeed, the count by partner parties is
\[
\sum_{j\ne i}(q_j-r_i(a))=Q-q_i-3r_i(a),
\]
whereas each containing maximal word contributes one or two, according as \(k=2\) or \(3\). Subtracting their number \(p_i(a)=6-r_i(a)\) proves (9).

### Profile \(3555\)

For the three-symbol party, (9) gives
\[
n_3(i,a)=9-2r_i(a)\ge0.
\]
Thus each degree is at most four, and their sum is twelve; all three degrees are four.

Every five-symbol party has degrees between two and three by (4), summing to twelve. Its degree multiset is therefore
\[
(3,3,2,2,2).
\]

Label the three-symbol party \(0\). For each other party \(j\),
\[
R_{0j}=(A_0\times A_j)
\setminus\{(a,\ell_j(a)):a\in A_0\}, \tag{10}
\]
where \(\ell_j:A_0\to A_j\) is injective. Each row misses one value because its degree is four. Each column misses at most one because its residual degree is at least two. Thus the three missing pairs form an injective matching.

### Profile \(4444\)

All maximal words have \(k=2\), so (9) yields
\[
0=6-2r_i(a).
\]
Every residual symbol has degree three. Every \(R_{ij}\) is therefore \(K_{4,4}\) with a perfect matching removed.

This does **not** prove that the six missing matchings can be simultaneously relabelled to one common equality relation.

### Profile \(4445\)

At a four-symbol party, (9) gives \(r_i(a)\le3\). Sum twelve over four symbols forces every degree to be three.

At the five-symbol party, (9) also gives \(r_i(a)\le3\); with (4), its degree multiset is \((3,3,2,2,2)\).

### Further exact maximal-word shadow restrictions

Solving the five nonnegative integer counts using (5), (6), and (8), then applying pairwise injectivity of \(P\), leaves only these necessary histograms:

| Profile | Possible \((n_0,n_1,n_2,n_3,n_4)\) |
|---|---|
| \(4455\) | \((0,1,10,13,0)\); \((0,0,13,10,1)\) |
| \(4555\) | \((0,0,9,12,3)\); \((0,1,6,15,2)\); \((0,2,3,18,1)\); \((1,0,3,20,0)\) |
| \(5555\) | \((0,0,6,12,6)\); \((0,1,3,15,5)\); \((1,0,0,20,3)\) |

For completeness, the additional injectivity eliminations are:

- For \(5555\), each outside-residual alphabet is a singleton. Two \(k=1\) words would each use outside symbols at three parties; those triples intersect in at least two parties, repeating a pair value. Hence \(n_1\le1\).
- For \(4555\), suppose three \(k=1\) words existed. If one uses all three singleton outside alphabets of the five-symbol parties, it repeats an outside pair with either other word. Otherwise all three use an outside symbol at the four-symbol party and two singleton outside symbols elsewhere. Two use the same one of its two outside symbols; their two-party subsets among the other three parties intersect, again repeating a pair. Hence \(n_1\le2\).

These are exhaustive restrictions on the **five-count binary shadow**, not an enumeration or existence proof for tensor supports.

## 6. A complex-phase obstruction for degree-two symbols

### External-partner lemma

Assume the inherited no-distance-one condition. If \(r_i(a)=2\), then for each \(j\ne i\), let \(B_j(a)\) be the two symbols occurring at party \(j\) among residual words with \(w_i=a\).

In the cut \(ij\mid kl\), consider either row \((a,b)\), \(b\in B_j(a)\), and its other row \((a',b')\) in the same full \(2\times2\) block. Then
\[
\boxed{b'\notin B_j(a).} \tag{11}
\]

### Proof

There are four residual words with coordinate \(i=a\). At each other party exactly two symbols occur twice. No two words share an additional coordinate pair, because that would be a distance-one pair.

After relabelling the other three parties, these four words must be
\[
(a,0,0,0),\quad(a,0,1,1),\quad
(a,1,0,1),\quad(a,1,1,0). \tag{12}
\]

Suppose an internal partner exists. Relabelling the two symbols if necessary, the row \((a,0)\) in cut \(12\mid34\) has partner \((a',1)\). Its two entries are forced to be
\[
(a',1,0,0),\qquad(a',1,1,1). \tag{13}
\]
Here \(a'\ne a\).

In cut \(14\mid23\), the first word of (13) shares a column with \((a,1,0,1)\). Degree-two block closure forces
\[
(a',0,1,0).
\]
The second word of (13), paired with the block containing \((a,1,1,0)\), forces
\[
(a',0,0,1).
\]

Thus eight words are present: after labelling \(a=0,a'=1\), exactly
\[
0000,\ 0011,\ 0101,\ 0110,\
1001,\ 1010,\ 1100,\ 1111. \tag{14}
\]
Every binary pair value already has its two residual extensions within (14). These words therefore form an isolated binary block in all three cuts.

It remains essential to check **complex unitarity**, rather than treating (14) as a physical tensor.

Let \(\theta_w\) be the phase of each nonzero entry, and set
\[
\begin{aligned}
A&=\theta_{0000}+\theta_{1111},&
B&=\theta_{0011}+\theta_{1100},\\
C&=\theta_{0101}+\theta_{1010},&
D&=\theta_{0110}+\theta_{1001}.
\end{aligned}
\]
A full nonzero \(2\times2\) unitary block requires its diagonal phase sum minus its off-diagonal phase sum to equal \(\pi\) modulo \(2\pi\).

The cuts \(12\mid34\), \(13\mid24\), and \(14\mid23\) respectively require, among their block equations,
\[
A-B\equiv\pi,\qquad A-C\equiv\pi,\qquad B-C\equiv\pi
\pmod{2\pi}.
\]
The first two imply \(B-C\equiv0\), contradicting the third.

This excludes arbitrary nonzero complex amplitudes on the forced block; it is not a real-sign-only argument or numerical failure. Therefore the internal partner cannot exist. ∎

### Consequence for \(3555\)

Use notation (10). The low-degree symbol \(\ell_j(a)\) has precisely the two neighbors \(A_0\setminus\{a\}\).

Consequently, in the cut \(0j\mid kl\), the other row paired with
\[
(c,\ell_j(a)),\qquad c\ne a,
\]
must have the form
\[
(a,x). \tag{15}
\]
The first coordinate must be the unique symbol outside those two neighbors, by (11).

Thus the six residual \(2\times2\) blocks in each such cut must obey (15). This is an additional necessary restriction on the actual surviving three-symbol branch, beyond its degree sequence.

## 7. What has and has not been established

**Established in this candidate:**

- Entire alphabet classes \(3444,3445,3455\) are excluded by exact same-tensor maximal-word counting.
- Several additional maximal-word occupancy classes are excluded.
- The profiles \(3555,4444,4445\) have the forced degree sequences proved above.
- The internal-partner support class in §6 is excluded by a simultaneous complex-phase contradiction.
- The surviving \(3555\) branch obeys the matching constraint (15).

**Not established:**

- Existence or impossibility of all supports in any of the six remaining alphabet profiles.
- Compatibility of every remaining residual support with a single maximal-word set \(P\).
- Simultaneous complex phase solvability on those remaining supports.
- Positive, strictly subunit residual moduli satisfying every block equation.
- A normalized physical witness.

For a candidate support, the distinction remains exact. In every residual block, writing its squared moduli as \(x_{rc}>0\), actual unitarity requires
\[
x_{rc}=x_{r'c'},\quad
x_{rc'}=x_{r'c},\quad
x_{rc}+x_{rc'}=1,
\]
and
\[
\theta_{rc}-\theta_{rc'}-\theta_{r'c}+\theta_{r'c'}
\equiv\pi\pmod{2\pi},
\]
**simultaneously across all three cuts of the same entries**. Residual values must also remain strictly below one. A support graph or a maximal-word shadow alone satisfies neither requirement.

If those conditions and the singleton blocks were actually satisfied, \(U/6\) would have all balanced marginals \(I_{36}/36\). No such remaining construction is supplied here.

## 8. Public source and verification boundary

Public primary source consulted:

- Palash Pandya, *Euler’s thirty-six officers need not all be entangled: real AME(4,6), families and classification*, arXiv:2610.16673v1, especially **§III, Lemma 1 and equation (2)**:  
  https://arxiv.org/html/2610.16673v1#Thmlemma1

That lemma states the separation of positive squared-modulus equations and phase congruences for simultaneous \(1\times1/2\times2\) block supports. The particular obstruction in §6 is proved explicitly above, not inferred from the paper’s constructions or numerical results.

**Verification status:** written author derivation only. No independent-family, human, formal/kernel, executable, exhaustive-support-search, or novelty verification has occurred. The original universal \(t=24\) question remains open, but the three complete alphabet classes containing both 3 and 4 are eliminated by this candidate.