The intended integer-parameter mathematics passes. **0 FATAL, 0 MAJOR, 2 MINOR findings.** All 13 snapshot SHA-256 hashes match.

| Claim | Verdict |
|---|---|
| Lemma ZX | **ACCEPT** |
| Lemma S1(a) | **ACCEPT-WITH-FIXES** |
| Lemma S1(b) | **ACCEPT-WITH-FIXES** |
| ROT-ZX terminal | **ACCEPT-WITH-FIXES** |
| ROT-ZX uniform | **ACCEPT** |
| INV*-ZX | **ACCEPT** |
| OLSON-ZX | **ACCEPT** |

The fixes concern explicit domains and normal-form quantifiers; the integer-domain conclusions require no weakening.

1. **MINOR — SOURCE00:68–72: explicitly require integer κ.** Write “Let \(p\ge5\) be prime and \(\kappa\in\mathbb Z_{\ge0}\).” Without integrality, both S1 statements are false: in \(\mathbb Z_{10}\), take
   \[
   Y=(1,9),\qquad \kappa=\tfrac12.
   \]
   Its only nonempty zero-sum has length \(2\). Thus (ZP), whose window is \([3,10]\), holds, and both displayed numerical hypotheses hold, but (S1) fails. S1(b)’s asserted interval becomes \([11,1]\). All downstream applications already have integer \(\widehat\kappa\).

2. **MINOR — SOURCE00:203–206, 300–303: carry the existential normal-form quantifier consistently.** Adopt SOURCE01:76–81’s **“SOME normal form produced by the process”** in the main statement. No uniqueness theorem is supplied or needed. Likewise, failure of \(3k\le2p+1\) for a selected normal form does not by itself establish that the original word is uncovered: the residual must quantify over all admissible normal forms, as SOURCE01:96–99 does.

For **ZX Step A and COMP** (SOURCE00:81–108), all prerequisites hold. A nonempty zero-sum in \(Y'\) would enlarge \(Z\); hence \(Y'\) is zero-sum-free. Davenport and (S1) give
\[
2p-k\le L\le2p-1,\qquad
e=2p-1-L=k-1-2\kappa+|Z|\in[0,k-1].
\]
In particular \(Y'\) is nonempty, so a multiplicity maximizer exists. Moreover,
\[
3e+2\le3k-1\le2p,\qquad
3e\le3k-3\le2p-2.
\]
These discharge MULT(iii), followed by MULT(ii), for **any** multiplicity-maximizing value \(g\).

The deductions
\[
e'\ge2q,\quad m=L-q\ge L-e'/2,\quad
d_j\le e'+1\le e+1\le m
\]
are valid. The range gives \(k\le p-2\), including \(p=5\), so \(d_j\) really is its signed coefficient. Adding each weight to the existing interval proves every integer in \([0,W']\) is represented. If \(W'\ge2p\), weight \(2p\) supplies a nonempty zero-sum in \(Y'\). Thus
\[
p+2\le L\le W'\le2p-1.
\]
The cardinality estimate \(|Q|\ge w(Q)-e'\) also holds.

For **EX** (SOURCE00:110–113), occurrences are disjoint because \(Q\le Y'\) and \(U\le Z\). Therefore \((Z-U)Q\le Y\), and its sum is zero under the stated congruence. Longest-length maximality gives \(|Q|\le|U|\) for **every** admissible \(Q\). If the replacement is empty, that inequality is immediate. Empty \(U\) or \(Q\) causes no exception. Oddness makes congruent sums have congruent cardinality parity automatically.

For **C–D** (SOURCE00:115–127), a positive coefficient \(b\ge3\), including \(b=p\), lies below \(W'\). Its completion has at least two terms: use \(g^b\) when \(b\le m\); otherwise every singleton has weight at most \(m\). EX contradicts the singleton \(U\). Thus every positive term of \(Z\) equals \(g\).

For a negative coefficient \(-\beta\), the target \(2p-\beta\ge p+2\) likewise cannot have an admissible completion of cardinality at most one. Consequently
\[
2p-\beta>W'=2p-1-e+e',
\]
which, by integrality, gives \(\beta\le e-e'\).

For **E** (SOURCE00:129–145), \(r<2p\) and \(\sigma\ge0\) justify
\[
\sigma=r+2pt,\qquad t\ge0.
\]
If \(t\ge1\), put \(\Delta=e-e'\ge1\). The interval calculation is correct:
\[
|I|=2m-2p+1
 \ge2p-1-2e-e'
 \ge e-e'=\Delta.
\]
Also \(I=[2p-m,m]\subset[1,2p-1]\). The increasing **integer**, unreduced prefix sums have increments at most \(\Delta\); the least crossing of \(2p-m\) therefore lands at or below \(m\). There is no modular wrap issue at this crossing.

Both \(g^{2p-S_j}\) and \(g^{S_j}\) are available separately in \(Y'\). EX applied to \(U\) and \(Z-U\) yields
\[
2p-S_j\le j,\qquad S_j\le|Z|-j,
\]
hence \(2p\le|Z|<2p\). The two completion multisets need not be disjoint from each other. If \(\sigma=0\), the congruence and \(r<2p\) already force \(r=0\). Empty \(Z\) is covered.

For **F–G** (SOURCE00:147–160), the hypothetical completion of weight \(2p-r\) and EX with \(T\) give
\[
2p\le |Z|+e'\le2\kappa+e\le3(k-1)\le2p-2.
\]
Thus \(W'\le2p-1-r\), and
\[
\operatorname{cost}_g(Y)=e'+\sigma=e'+r\le e\le k-1.
\]
The coefficient bounds and \(E+N=\operatorname{cost}\) follow exactly as stated.

The edge cases survive: \(\kappa=0\) forces \(Z=\varnothing\); \(k=1\) forces \(e=e'=0\) and \(Y=g^{2p-1}\). At \(3k=2p+1\), MULT still permits equality, while the contradiction bounds retain \(3(k-1)=2p-2<2p\).

For **S1(a)** (SOURCE00:183–188), with integer κ, minimal zero-sums have even length at most \(2p\), hence at most \(2\kappa\) by (ZP). Decomposing a longer zero-sum into minimal pieces and stopping at the least cumulative length exceeding \(2\kappa\) produces a forbidden length in
\[
[2\kappa+2,4\kappa]\subseteq[2\kappa+2,2p-2].
\]
For \(\kappa=0\), the existence of any minimal zero-sum already contradicts (ZP).

For **S1(b)** (SOURCE00:189–199), the proof is valid. If at most one minimal piece is long, place it at the beginning. The cumulative crossing then adds a nonlong piece of length at most \(2p-2\kappa\), producing a forbidden total at most \(2p\). Hence two disjoint pieces are long; parity strengthens their lower bound to \(2p-2\kappa+2\). Their union has length at least
\[
4p-4\kappa+4\ge2\kappa+2,
\]
using \(6\kappa\le4p+2\), and (ZP) forces its length to be at least \(2p+2\). The upper bounds give \(4\kappa\ge2p+2\).

Such a pair conversely violates (S1), since the displayed numerical hypothesis ensures \(\kappa<p\). Thus the introductory “exactly” is justified within that hypothesis. **S1(b) is unnecessary for ZX, ROT, INV*, and OLSON; it supports the residual description only.**

For **ROT-ZX terminal** (SOURCE00:203–234), the imported normal-form interface preserves length, \(F\), and the rotation multiset, with \(k\le o\), \(k\equiv o\pmod2\), and
\[
\widehat\kappa=\kappa(w)-(o-k)/2.
\]
The \(k=1\) branch is covered by K1, including the nonzero common rotation value, \(F=2p-1\), and \(\widehat\kappa=0\). For \(k\ge2\), GRX with all-plus signs and zero selected rotations excludes \(H\ge p\); hence \(\widehat\kappa\ge0\). DAV gives \(\widehat\kappa\le k-1\), and GRX supplies (ZP).

The order of weight identification is correct: ZX establishes \(|b|\le k\le p-2\) before identifying \(b\) with the SHgen weight. This excludes \(\rho_0\). No condition \(\widehat\kappa\le p-k\) is used.

For \(E>0\), SHgen’s hypotheses follow from
\[
2H\ge2p-2k\ge k-1\ge E
\]
and
\[
\eta\le E/2,\quad a_{\max}\le E+1\le k,\quad
2p-\eta-a_{\max}-1\ge k,
\]
the last inequality following from \(5k\le4p-1\). That bound follows from \(3k\le2p+1\) and \(p\ge5\).

SHgen-E’s caller obligations hold: expansions preserve \(k\), odd nonempty blocks, block values, and genuine empty runs. Each base expansion has length \(4p-2\), rotations in one nonzero pair, and \(o_F\le k\le p\). Restricted REFL therefore suffices.

For **uniform ROT-ZX** (SOURCE00:236–243), either
\[
\widehat\kappa\le k-1\le o-1\le(p-1)/2,
\]
or
\[
\widehat\kappa\le\kappa(w)\le(p-1)/2.
\]
Thus S1(a) supplies (S1). The equivalence with \(F\ge o+p-1\) is correct.

For **INV*-ZX** (SOURCE00:247–251; SOURCE01:87–90), restricted REFL must apply to the **original word**. Its separate \(o_F(w)\le p\) hypothesis is correctly retained in the terminal form. Uniformly, \(3o\le2p+1\) implies it. The conclusion is precisely the nonzero rotation pair plus constant maximal cyclic reflection runs.

For **OLSON-ZX** (SOURCE00:253–266), the SOURCE09:28–47 case structure applies:

- If \(R\le2\), then \(F\ge4p-3\) and \(o\le2p-3\), so \((F-o)/2\ge p\). SOURCE09’s cyclic framing supplies the adjacent equal pairs; the constant all-reflection case is immediate. Conjugating the cyclic selection back preserves identity.
- Deleting within an odd block of length at least three gives exactly \((o',F')=(o-1,F-1)\). The block remains nonempty, and \(F'-o'=F-o\).
- Deleting a rotation gives \((o_i,F_i)=(o,F)\) or \((o-2,F)\). A fusion lowers the odd count by two only when both fused blocks are odd.

Both sufficient branches survive these deletions. In Case 2, reinserting the equal reflection preserves RGR. In Case 3, a third rotation position identifies the two deletion words’ nonzero pairs; differing adjacent reflections would persist after rotation deletion. RGR-LONG then applies.

The coverage arithmetic is correct: \(p=7,o=5\) adds \(F=11\) before the previous threshold \(13\); \(p=13,o=8\) adds \(F=20\), and \(o=9\) adds \(F=21,23\). The listed terminal pairs are correct. These are sufficient parameter ranges, without an assertion that corresponding avoiders exist. High κ alone does not exclude terminal coverage when (S1) holds. The single \((p,p-1)\) obstruction remains confined to that pair, and KAPPA01 is not used.

I audited ZX A–G, both S1 arguments, parameter arithmetic, quantifiers, and deletion/reconstruction arguments. I imported Davenport, MULT, GRX/PM*/K1, normal form/DAV, SHgen/SHgen-E, restricted REFL, and RGR-LONG at their supplied accepted scopes. SOURCE02 was read subject to SOURCE03’s mandatory V1–V9 overlay. No computational experiment was run.

Operational deviation: I issued one initial `pwd` in the supplied review directory. All file reads and hashes were within the snapshot; no interpreter, writes, network, or delegation was used.