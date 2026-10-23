All 13 SHA-256 hashes and byte counts match. Only static snapshot reads, comparisons, and hashes were used. Here \(o_F\) counts odd blocks in the **maximal cyclic constant reflection-block decomposition**, not reflection runs.

| Claim | Disposition |
|---|---|
| Generalized Lemma ZS under (G) | **ACCEPT-WITH-FIXES** |
| ROT-ZS / INV*-ZS | **ACCEPT-WITH-FIXES** |
| OLSON-ZS | **ACCEPT-WITH-FIXES** |
| HALF deduction without an additional \(F\) hypothesis | **ACCEPT-WITH-FIXES** |

**0 FATAL, 0 MAJOR.** The mathematical implications pass. The required repairs below concern proof wording, an explicit one-block case, citations, and claims about the remaining scope.

**Generalized ZS — SOURCE00:LF37–123.** All five consequences of (G) are valid:

- G1 follows from
  \[
  \kappa\le\min(k-1,p-k)\le (p-1)/2,
  \]
  giving \(4\kappa\le2p-2\).
- G2 is \(3(k-1)+2=3k-1\le2p\).
- G3 follows from \((2p+1)/3\le p-2\) for \(p\ge7\). At \(p=5\), integrality gives \(k\le3=p-2\).
- G4 weakens the stated \(3k\le2p+1\).
- G5 is precisely twice \(\kappa\le p-k\).

None imports \(k\le(p+1)/2\).

In Step 1, every minimal zero-sum has even length at most \(2p\), hence at most \(2\kappa\). At the first cumulative length reaching \(2\kappa+2\), the preceding even length is at most \(2\kappa\); adding the next minimal zero-sum gives length at most \(4\kappa\le2p-2\), contradicting ZP. For \(\kappa=0\), the minimal-zero-sum argument immediately excludes every nonempty zero-sum.

Step 2 correctly yields
\[
L=2p+2\kappa-k-|Z|,\qquad
e=k-1-2\kappa+|Z|,\qquad 0\le e\le k-1.
\]
Maximal length ensures that the complement \(Y'\) is zero-sum-free. Inclusion-maximality would also suffice.

MULT’s actual prerequisite is satisfied:
\[
3e+2\le3k-1\le2p.
\]
SOURCE06:LF63–81 consequently supplies \(m\ge\max(2,e+1)\), a generator \(g\), and positive odd weights with excess \(e'\le e\). MULT remains an essential import.

COMP is valid: each added weight satisfies \(d_j\le e'+1\le m\), so subset weights fill the entire integer interval. A weight-\(2p\) subsequence would contradict zero-sum-freeness, proving \(W'\le2p-1\). G3 then ensures that these positive weights are the prescribed signed representatives. Step 4 completes \(U\subseteq Z\) using terms entirely in \(Y'\), so its disjointness and length inequalities are justified.

**Step 5 — SOURCE00:LF91–96.** Both endpoints of the forbidden middle interval are excluded. If
\[
k\le\tau(U)\le2p-k,
\]
then \(\tau(U^c)=2p-\tau(U)\) lies in the same interval, and both are at most \(W'\). The two separate completions give
\[
|Z|+2p-2e'\le4\kappa.
\]
Substituting \(e'\le k-1-2\kappa+|Z|\) forces
\[
|Z|\ge2p-2k+2.
\]
But Step 1 and G5 give
\[
|Z|\le2\kappa\le2p-2k.
\]
The contradiction retains a two-unit gap even at \(\kappa=p-k\). The completion subsequences may overlap: only their separate numerical inequalities are added.

**Revised Step 6 — SOURCE00:LF98–105.** The wrap correction works. Singleton applications of Step 5 give \(|b|\le k-1<p\) on \(Z\). A first positive partial sum crossing \(k\) lands in
\[
k\le S_j\le2k-2<2p.
\]
Its signed representative is \(S_j\) when \(S_j\le p\), and \(S_j-2p\) otherwise. Thus its magnitude is at least
\[
\min(k,\,2p-2k+2)\ge k,
\]
because \(3k\le2p+2\). This contradicts Step 5, including when \(S_j=p\) or \(S_j>p\). Applying the same magnitude argument to negative terms bounds \(\sigma_-\). Finally,
\[
|\sigma_+-\sigma_-|\le k-1<2p
\]
and congruence to zero force equality as integers. The old non-wrapping bound \(2k-2\le p-1\) is unnecessary.

**Steps 7–9 — SOURCE00:LF107–123.** If \(W'\ge2p-\sigma\), completion of \(Z_+\) gives
\[
2p+1\le \sigma+k+|Z_-|
       \le2\sigma+k
       \le3k-2
       \le2p,
\]
a contradiction by G4. Therefore the strict inequality becomes the correct integer bound
\[
W'\le2p-1-\sigma.
\]
For Step 8, \(\sigma\le k-1\le m\) permits completion by exactly \(\sigma\) copies of \(g\), yielding \(|Z_-|+\sigma\le2\kappa\). The case \(\sigma=0\) is immediate.

The final count is exact:
\[
\begin{aligned}
\operatorname{cost}(Y)
&=e'+2\sigma-|Z_+|\\
&\le e+\sigma-|Z_+|\\
&=k-1-2\kappa+|Z_-|+\sigma\\
&\le k-1.
\end{aligned}
\]
Negative terms pay their full \(|b|\); their surcharge is not lost. Hence \(\operatorname{cost}=E+N\).

The endpoints also pass: \(k=1\) forces \(\kappa=0\) and \(Y=g^{2p-1}\); general \(\kappa=0\) gives \(Z=\varnothing\). MULT remains applicable at equality \(3e+2=2p\), including \(p=7,k=5,e=4\). The order-two element is excluded from \(Y'\) by C1 and from \(Z\) by the singleton bound.

**ROT-ZS / INV*-ZS — SOURCE00:LF149–181.** Normalization has the required bookkeeping. PM* preserves length, \(F\), the rotation multiset, and avoidance in the accepted direction. Equal-valued fusions lower the odd count by zero or two. Thus
\[
k\le o,\quad k\equiv o\pmod2,\quad
H_{\rm terminal}=\frac{F-k}{2},
\]
and
\[
\kappa_{\rm terminal}
=\kappa_{\rm original}-\frac{o-k}{2}.
\]
One must recompute \(H\) after fusions; it is not preserved by an odd-plus-odd fusion.

The normal-form exclusions handle the one-even-block ending; K1 handles \(k=1\). For \(k\ge2\), DAV gives \(\kappa\le k-1\). If \(H\ge p\), GRX’s all-plus pattern with zero selected rotations already solves the word, so avoidance gives \(\kappa\ge0\), also with empty runs. The original \(F\) condition supplies
\[
\kappa\le p-o-\frac{o-k}{2}\le p-k.
\]
Together with \(3k\le3o\le2p+1\), every G bound holds after possible fusions.

After stating \(|b|\le k\le p-2\), the identification with SHgen’s weights is valid and excludes \(\rho_0\). If \(E>0\),
\[
2H\ge2k-2\ge k-1\ge E.
\]
Also \(\eta\le E/2\le(k-1)/2\) and \(a_{\max}\le k\), so K follows from
\[
5k\le\frac{10p+5}{3}\le4p-1
\]
for \(p\ge4\). The old \(5k\le2p+4\) is unused.

The supplied normal-form and SHgen-E proofs support their independent lemma hypotheses; their former placement inside a narrower theorem does not impose that theorem’s range. Expansions preserve \(k\), block values, odd nonempty blocks, and genuine empty runs. Every restricted REFL call therefore has
\[
o_F(u^\circ)\le k\le(2p+1)/3\le p.
\]
H and K persist under induction. G need not be re-established for expanded descendants.

For INV*, restricted REFL is applied to the **original** word after ROT supplies its nonzero rotation pair. Reflection constancy is not transported backwards through PM*.

**HALF deduction — SOURCE00:LF171–174.** The automatic \(F\) condition follows from avoidance. For terminal \(k\ge2\), V gives
\[
\kappa_{\rm original}
=\kappa+\frac{o-k}{2}
\le\frac{o+k-2}{2}
\le o-1
\le p-o.
\]
Thus \(F\ge3o-2\), and \(3o\le(3p+3)/2\le2p+1\). For \(k=1\), K1 supplies \(F=2p-1\), hence terminal \(\kappa=0=k-1\), validating the same calculation. The normal-form exclusions cover \(o=0\). No additional \(F\) assumption is needed.

**OLSON-ZS — SOURCE00:LF183–196.** Assume the length-\((4p-1)\) word avoids; every deletion word then avoids in increasing inherited order.

For \(R\le2\), \(F\ge4p-3\) and \(o\le(2p+1)/3\le2p-3\) give
\[
(F-o)/2\ge p.
\]
SOURCE10:LF31–36 chooses a frame preventing a constant block from wrapping, and selects \(p\) equal-reflection pairs. Their ordered product is identity. Returning to original index order cyclically shifts the selected product, preserving identity by conjugation. The all-equal, rotations-free case is immediate.

Deleting from an odd reflection block of length at least three leaves that block present and gives exactly
\[
(o',F')=(o-1,F-1).
\]
In the high-\(o\) branch,
\[
F'\ge3o-3\ge3o'-2.
\]
In the low branch, \(o'\le(p+1)/2\), and the preceding V calculation applies to this deletion avoider. Both branches satisfy \(3o'\le2p+1\).

For rotation deletion, \(F_i=F\) and \(o_i\in\{o,o-2\}\). A newly empty run either leaves different-valued blocks separate or permits one fusion; the parity calculation gives exactly those changes. The high branch retains \(F_i\ge3o_i-2\); the low branch again obtains that inequality from avoidance and V.

Each of the two words deletes **one distinct rotation occurrence**. A third surviving rotation is nonzero and identifies their two rotation pairs. Every original rotation occurs in at least one deletion word. Adjacent unequal reflections in the original remain adjacent after rotation deletion, so deletion-word rigidity forces the original maximal cyclic reflection runs to be constant. Restoring the reflection in Case 2 likewise preserves RGR.

Thus the reconstructed original word meets SOURCE12:LF7 exactly, and RGR-LONG supplies the ordered identity selection. No even-reflection deletion or unrestricted INV* is used.

The following **MINOR repairs are mandatory**:

1. **SOURCE00:LF5, LF10–11:** replace “complete in-file proof” with “complete modulo MULT and \(D(\mathbb Z_{2p})=2p\).” Say the *parent-accepted v1 statements, with SOURCE03’s overlay*, remain true.

2. **SOURCE00:LF155–161:** spell out the \(H\ge p\), all-plus, zero-rotation argument for \(\kappa\ge0\). Move \(|b|\le k\le p-2\) before identifying SHgen’s weights. State that the independent normal-form/DAV/SHgen-E hypotheses are the ones being used.

3. **SOURCE00:LF173–174:** explicitly dispose of terminal \(k=1\) using K1 as above, or derive the needed inequality directly from DAV on the original representation. This also makes the automatic-\(F\) assertion used for deletion avoiders explicit.

4. **SOURCE00:LF24–26, LF186–195:** replace the absent deletion-ledger premise with SOURCE10:LF31–46 and the displayed deletion calculations. Cite the V argument in the HALF proof for low-\(o\) deletion avoiders.

5. **SOURCE00:LF144, LF208:** restrict the obstruction to \((k,\kappa)=(p,p-1)\). The example satisfies ZP and V and defeats the cost conclusion there; it establishes no interval “near \(p\).” Additional avoidance information, such as nonconstant-sign GRX patterns, is a possible input—not a necessity theorem about all proofs.

6. **SOURCE00:LF205:** label KAPPA01 an **unaccepted auxiliary candidate**, excluded from accepted coverage and dependencies.

7. **SOURCE00:LF8–9, LF204, LF206–208:** describe the residual as parameters not covered by these uniform sufficient hypotheses. Failure of \(3o\le2p+1\) does not make MULT unavailable: actual terminal \(k\) or defect \(e\) may still satisfy its conditions. Preserve the separately accepted four-block union, including \(p=5,o=4\). Limit “nothing is new at \(p=7\)” to the HALF comparison: generalized ZS allows \(p=7,o=5,F\ge13\).

**Audited/imported boundary:** Audited here are G1–G5, ZS’s nine steps and COMP, normalization bookkeeping, SHgen caller inequalities, restricted REFL scopes, the HALF deduction, and every ordered deletion/reconstruction step. Imported at their stated accepted scopes are Davenport/EGZ, MULT, GRX, PM*, K1, DAV, SHgen/SHgen-E, restricted REFL, and RGR-LONG. No finite experiment is a premise; no unrestricted ROT, INV*, or Olson claim is accepted.