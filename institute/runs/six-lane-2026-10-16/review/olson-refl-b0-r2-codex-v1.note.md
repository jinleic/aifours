**ACCEPT-WITH-FIXES — 0 FATAL, 0 MAJOR, 2 MINOR**, relative to the supplied parent-accepted imports. All ten SHA256 hashes match. This review used only static snapshot reads and hashes.

The new preservation and composition argument is valid. Two statements need correction:

- **MINOR — SOURCE00:L38–39.** PM0 need not append its even block to an **odd** block: the receiving block may also be even. Replace “an odd one” with “the next constant block, of either parity.” The displayed floor identity holds for either parity, so the preservation claim survives.
- **MINOR — SOURCE00:L60–61.** P3 preserves \(R,\kappa,B\); its donor remains nonempty, and filling the genuine empty run changes no reflection block. P4 changes these parameters. Replace the sentence with: “For mixed rotations, P3 and P4 can occur; P4 changes \(R,B,\kappa\), so this fixed-\(R\) composition does not apply.” Precisely, P4 decreases \(R\) by two, \(B\) by one, and \(\kappa\) by one, with one further decrease only if two odd blocks fuse.

The following checks support acceptance of the mathematics.

Normalization at **SOURCE00:L33–34** is legitimate. Since \(x\ne0\), the group automorphism
\[
\rho_v\mapsto\rho_{x^{-1}v},\qquad
\sigma_y\mapsto\sigma_{x^{-1}y}
\]
makes every rotation \(\rho_1\). It preserves block lengths, equality and inequality of reflection values, genuine empty gaps, \(R,H,\kappa\), and avoidance. Thus \(A=R,B=0\) without a subsequent sign swap. Cyclic cuts also respect the finite-word requirement: moving a selected prefix past the cut conjugates the selected product. An identity product therefore remains identity in increasing index order after the corresponding cyclic shift. The accepted SPEC/H0 move arguments concern ordered selections, so no unordered-product assumption enters.

For **SOURCE00:L35–39**, \(B=0\) is invariant. FUS recolors reflections; PM0 merges rotation runs and moves an even reflection block. Neither introduces a negative rotation. P3 requires both rotation signs in a donor, and P4 requires a \((1,1)\)-run, so neither can ever become available. Both remaining moves preserve \(R\), \(F\), and total length.

The FUS bookkeeping covers all parities. A single fusion joins an even block to an arbitrary block and leaves \(H\) unchanged. A double fusion replaces
\[
\sigma_u^a\,[]\,\sigma_v^b\,[]\,\sigma_u^c,\qquad b\ \text{even},
\]
by one block, and
\[
\Delta H=
\left\lfloor\frac{a+b+c}{2}\right\rfloor
-\left\lfloor\frac a2\right\rfloor-\frac b2
-\left\lfloor\frac c2\right\rfloor
=[a,c\text{ both odd}].
\]
Thus even–even, even–odd, and odd–even outer parities preserve \(\kappa\); odd–odd lowers it by one. Maximality prevents a further cascade beyond these two neighboring fusions: any unchanged block across an additional empty gap already differed from the surviving value. The exceptional all-reflection cycle is excluded before using this bookkeeping.

For PM0, the identity in SOURCE00 is correct for every receiving length \(l\):
\[
\left\lfloor(l+l')/2\right\rfloor
=\lfloor l/2\rfloor+l'/2,\qquad l'\text{ even}.
\]
Both neighboring rotation runs are nonempty, so their merger remains nonempty and cannot expose another reflection fusion. Other gaps retain their neighboring values and genuineness. The receiving block retains its parity. Consequently \(H\), hence \(\kappa\), is unchanged **after rereading the maximal decomposition**, not merely in an auxiliary representation. This establishes the claimed new monotonicity independently of Claim MON.

The reduction invocation at **SOURCE00:L40–41** is justified, with an important quantifier: RED sends an arbitrary **counterexample to reflection rigidity** into the residual class. It does not send every equal-rotation avoider there. An initial word with constant reflection runs already satisfies the conclusion. Under the contradiction assumption, however, there is a genuine empty run and RED applies.

The accessible exits can be checked more economically than the general RED proof. With \(B=0\), P3 cannot produce an exit, and P2 preserves empty gaps. Therefore \(g=0\) can arise only through P1. At that exit, the resulting RGR avoider has \(\kappa_{\rm end}=0\) by imported (I2), **SOURCE01:L27–31**. Before the move, \(g\ge1\) implies \(\kappa_{\rm pre}\ge1\) by K0* and the pair bound. Since FUS lowers \(\kappa\) by at most one, this must be an odd–even–odd double fusion with \(\kappa_{\rm pre}=1\). Its merged block is even. Imported (I3), **SOURCE01:L32–35**, says that an RGR avoider with \(\kappa=0\) has all reflection blocks odd: contradiction.

These RGR imports are applied only to the produced \(g=0\) word. Their use imposes no RGR hypothesis on the original word. In particular, (I3)’s internal \(o_F\le p\) justification is derived at its RGR, \(\kappa=0\) scope; it is not inherited from \(w_0\).

Termination follows from the decreasing integer triple \((\kappa,g,k)\). At a terminal state with \(g\ge1\), an even block would either touch an empty gap, enabling P1, or have two nonempty neighboring runs, enabling P2. Hence all blocks are odd. Every run is already pure or empty because \(B=0\). K0* gives \(\kappa'\ge1\), and K1*, **SOURCE01:L91–98**, excludes \(\kappa'=1\). K1* does not assume \(o_F\le p\): it derives \(g\le2\), \(k\le p+2\), and \(R\ge p\) from P0 and the run count. Therefore the terminal word really has
\[
B=0,\quad g\ge1,\quad \kappa'\ge2,\quad
R'=R,\quad\kappa'\le\kappa,
\]
with all maximal blocks odd and all empty gaps genuine.

The original edge cases are covered by the imported proof, though SOURCE00 could usefully make them explicit. If \(\kappa<0\), then \(H\ge p\), and selecting \(p\) disjoint equal-reflection pairs gives an ordered identity \(2p\)-subword. If \(\kappa=0\), K0* already gives the conclusion. If \(R=0\), pair consecutive reflections into \(2p-1\) rotation products; EGZ selects \(p\) pair products summing to zero, giving an increasing-index identity \(2p\)-subword. This is the supplied AR argument. With no reflections the conclusion is vacuous, and \(2p\) equal rotations also certify solvability. Thus no added \(R\ge1\) assumption is required.

For the composition at **SOURCE00:L41–46**, fixed length and terminal oddness give
\[
k'=2p-R+2\kappa',\qquad
\Delta'=p+\kappa'-1-R.
\]
If \(k'\le p\), the B0S scope in **SOURCE06:L7–15** applies directly. Its terminal odd-block count condition does not become an assumption on the initial word.

If \(k'\ge p+1\), all CJ triple-prime hypotheses in **SOURCE05:L7–17** hold, including
\[
R\ge4\kappa'-4,\qquad 2\kappa'\le p-1.
\]
The corrected corollary forces \(\Delta'\ge2\) and \(p<\kappa'+5\Delta'-5\). The first yields
\[
R\le p+\kappa'-3\le p+\kappa-3,
\]
contradicting the first numerical alternative. The second yields
\[
5R<4p+6\kappa'-10\le4p+6\kappa-10,
\]
contradicting the second. Both boundary equalities are handled correctly. Neither the unavailable stronger shortcut nor the original \(p\le23\) conclusion is imported.

The examples at **SOURCE00:L51–58** are arithmetically correct. P0 gives \(R+o_R\ge2p\), and \(o_R\le R\) gives \(R\ge p\), without an odd-block cap. Equal rotations give \(R\le2p-1\). For \(p=31,\kappa=7\), the thresholds are \(24,36,156/5\), giving exactly \(32\le R\le61\); only \(R=31\) remains outside this numerical corollary. For \(p=7\), \(\kappa=2\) requires \(R\ge6\), hence covers every possible avoider value \(7\le R\le13\); \(\kappa=3\) requires \(R\ge8\); \(\kappa\ge4\) violates the stated bound.

Finally,
\[
o_F(w_0)=2p-R+2\kappa
\]
is an exact identity. At \((31,7,32)\), \(o_F=44\), while \(k'\le44\). REFL-fewodd’s cap corresponds to \(R\ge p+2\kappa=45\), so \(32\le R\le44\) adds parameter coverage in the equal-rotation slice. “Unbounded” should mean **no imposed hypothesis \(o_F\le p\)**. It cannot mean arbitrarily large at fixed parameters. These examples assert no existence of avoiders; indeed, for positive \(\kappa\), the new conclusion combined with (I2) excludes such avoiders altogether. Acceptance concerns this preservation/composition proof and its scoped imports, with no broader rigidity or novelty claim.