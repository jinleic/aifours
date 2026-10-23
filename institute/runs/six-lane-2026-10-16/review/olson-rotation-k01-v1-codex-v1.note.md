All eight SHA256 hashes match. **No FATAL or MAJOR defect was found in the stated mathematical claims.** Two MINOR corrections are required.

| Claim | Verdict |
|---|---|
| KETA | **ACCEPT** |
| New sequence Lemma K1, \(\kappa=1\) | **ACCEPT** |
| ROT-K01 | **AWF** |
| Uniform INV*-K01 | **AWF** |
| Uniform ordered OLSON-K01 | **AWF** |

AWF means accept with the citation and scope corrections below; no stated hypothesis or conclusion needs weakening.

This audit independently checks KETA, the new sequence argument, the changed theorem estimates, expansion callers, deletion bookkeeping, and boundary examples. SC0 and the recorded classical index-one theorem are imports, as are PM*, DAV, GRX, S1+, the accepted **one-block** K1, SHgen/SHgen-E, restricted REFL, and RGR-LONG. Their original proofs are not newly certified. No K0 file, residual note, finite experiment, or model suggestion was used. Only snapshot reads and hashes were performed.

**KETA is correct using the actual SHgen definitions.** SOURCE03:39–42 makes every heavy absolute weight odd and at least \(3\), including weight \(p\) for a zero rotation. For \(\eta\ge1\), select a maximum-weight occurrence. Then
\[
E\ge(a_{\max}-1)+2(\eta-1)
 =a_{\max}+2\eta-3
 \ge a_{\max}+\eta-2.
\]
Consequently,
\[
2p-\eta-a_{\max}-1
 \ge2p-E-3
 \ge2p-k-2
 \ge k
\]
when \(E\le k-1\) and \(k\le p-1\). This directly establishes SHgen(K).

For \(\eta=0\), \(a_{\max}\) is undefined under those definitions. Neither KETA nor SHgen should be invoked: \(E=0\), and every rotation is already light. This supplies the implicit trivial branch in SOURCE00:70–73.

**The new sequence lemma survives the occurrence-level audit.** Odd residues cannot give singleton zero-sums. Under its hypothesis, every nonempty zero-sum is therefore an inverse pair. Two disjoint pairs would produce a forbidden length-four zero-sum.

Fix a pair of distinct occurrences \(\{u,v\}\). If neither endpoint deletion is zero-sum-free, there are pairs
\[
P'=\{v,x\},\qquad P''=\{u,y\}.
\]
Here \(x,y\) lie outside \(\{u,v\}\). Because the two pairs must intersect, their only possible common occurrence is \(x=y\). Their value equations give \(u=v=-x\), while \(u+v=0\). Thus all three occurrences have the unique order-two value, \(pg\), written \((1,0)\) in the source.

This also controls every other possible pair. A fourth occurrence adjacent to this triple would itself be the involution, yielding two disjoint pairs. A pair wholly outside the triple would be disjoint from \(\{u,v\}\). Hence the pair graph consists precisely of that triangle and isolated vertices.

Deleting occurrences \(u,v\) leaves a zero-sum-free sequence of length
\[
2p-k\ge p+1
\]
that still contains occurrence \(x\). SC0 assigns \(x\) coefficient \(p\) relative to any resulting generator, so its total positive weight is at least
\[
p+(2p-k-1)=3p-k-1\ge2p,
\]
contradicting SC0. Thus an endpoint deletion \(Y_0=Y-\{u\}\) really is zero-sum-free.

Its length is \(L=2p+1-k\ge p+2\), and SC0 gives
\[
W\le2p-1,\qquad W-L\le k-2.
\]
An involution endpoint would leave its partner in \(Y_0\), forcing
\[
W\ge p+(L-1)=3p-k>2p-1.
\]
That endpoint is excluded.

For the surviving partner \(v=ag\), suppose \(a\ge3\). With \(h\) nonunit occurrences and \(m=L-h\) unit occurrences,
\[
W-L\ge(a-1)+2(h-1),
\]
hence
\[
a\le k+1-2h,\qquad
m-a\ge2p-2k+h\ge3.
\]
Therefore \(Y_0\) contains at least \(a\) **distinct unit occurrences**. They are distinct from \(v\), whose coefficient is at least \(3\), and from deleted occurrence \(u\). Together with \(u=-ag\), they give a zero-sum of length \(a+1\ge4\). Thus \(v=g\) and \(u=-g\).

All remaining positive coefficients satisfy
\[
a_i\le1+(W-L)\le k-1\le p-2.
\]
They are therefore the intended positive signed coefficients. The deleted occurrence contributes coefficient \(-1\), giving
\[
E=W-L\le k-2,\qquad N=1,\qquad
\operatorname{cost}_g(Y)=E+1\le k-1.
\]
Since \(Y_0\) is zero-sum-free, every pair in the original sequence contains the deleted occurrence; no additional pair configuration was overlooked.

The no-pair branch is also sound: SC0 gives excess at most \(k-3\), \(N=0\), and coefficients at most \(k-2\). Its small-\(k\) consequences must be read as impossibilities:

- At \(k=1,2\), the no-pair sequence would have length at least \(2p\), contradicting \(W\le2p-1\).
- At \(k=1\), the pair branch also has \(L=2p\), so the entire hypothesis is impossible.
- At \(k=2\), the pair branch is possible and forces \(Y=g^{2p-1}(-g)\). It has \(E=0,N=1\).

Thus no negative cost is being asserted for an existing sequence.

**ROT-K01 has the required interfaces throughout its stated range.** Terminal \(\widehat\kappa\) is integral because \(F\equiv k\pmod2\). For an avoider with \(k\ge2\), GRX also forces \(\widehat\kappa\ge0\): if \(H\ge p\), the all-plus pattern with no selected rotations already supplies an identity selection. GRX gives (ZP), and accepted S1+ applies at \(\widehat\kappa=0,1\).

For \(\widehat\kappa=0\), S1 makes \(Y\) zero-sum-free of length \(2p-k\ge p+1\). Directly from SC0,
\[
E=W-(2p-k)\le k-1,\qquad N=0,\qquad a_i\le k.
\]
The coefficients are odd; since \(k\le p-1\), they are actually at most \(p-2\). This independently proves the needed branch without importing K0.

For \(\widehat\kappa=1\), the new sequence lemma supplies stronger bounds. A generator of \(C_{2p}\), expressed as \(Y(c)\), has \(c\ne0\). Thus both branches produce exactly the SHgen signed weights, with no zero rotation. Moreover,
\[
2H=2p-2-2\widehat\kappa\ge2p-4\ge k-1\ge E,
\]
and KETA supplies (K) whenever a heavy exists.

The SHgen-E caller is valid at **every** induction base. SOURCE04:52–70 preserves length \(4p-2\), the same \(k\) positive odd blocks, their values, and every empty run between different values. Consequently every base expansion has maximal constant-block count
\[
o_F=k\le p-1\le p.
\]
Once all rotations are light, restricted REFL applies. Any surviving empty run joins differently valued reflection blocks, contradicting the constant-run conclusion for an avoider. This uses precisely the accepted restricted interface, without assuming unrestricted REFL.

**Both uniform consequences follow.** Normal-form existence and exclusion of the one-even-block endpoint are supplied by SOURCE04:30–43. For every admissible normal form,
\[
k\le o_F,\qquad
\widehat\kappa=\kappa(w)-(o_F-k)/2\le\kappa(w)\le1.
\]
For \(k\ge2\), GRX supplies the missing lower bound \(0\); hence \(\widehat\kappa\in\{0,1\}\). The \(k=1\) branch uses the accepted one-block proposition, including its nonzero-pair conclusion. Restricted REFL then applies to the **original** word because its \(o_F\le p-1\). This proves INV*.

For ordered Olson, the accepted deletion ledger preserves both uniform inequalities:

- If \(R\le2\), then \(F\ge4p-3\). Since \(o_F\le p-1\le2p-3\), there are at least \(p\) disjoint equal reflection pairs. SOURCE07:31–36 supplies the cyclic frame and conjugation argument returning an increasing-original-index identity selection.
- Deleting a reflection from an odd block of length at least three gives \((o',F')=(o-1,F-1)\), preserving \(F-o\).
- Deleting either of two distinct rotation occurrences, separately, gives \(F'=F\) and \(o'=o\) or \(o-2\). Thus \(F'-o'\ge F-o\).

The resulting avoiders satisfy uniform INV*. In the rotation-deletion branch, a third rotation occurs in both words and identifies their nonzero pairs. Original unequal reflection adjacencies would survive deletion, so the original reflection runs are constant. RGR-LONG then gives the required ordered identity subword.

**Hand checks support the exact boundary estimates.** For every permitted prime, the sequence
\[
Y=g^{p+1}\bigl((p-2)g\bigr)(-g),\qquad k=p-1,
\]
has only inverse-pair zero-sums and attains \(E=k-2\), cost \(k-1\), and \(m-a=3\). At \(p=5,7,11\), its heavy coefficients are respectively \(3,5,9\). These verify sharp sequence bounds; they assert no dihedral realization.

The uniform examples are correct: \(p=7,o_F=6,F\ge16\); \(p=11,o_F=9,F\ge27\), or \(o_F=10,F\ge28\). At \(p=5\), the resulting \(o_F=4\) uniform class already lies in the separately accepted finite case recorded in SOURCE05:27. Line 95 describes this route’s scope, not failure of outside words or exclusion of other normal forms.

The required corrections are:

1. **MINOR — [SOURCE00:13,74,81](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-k01-v1-review-v1/snapshot/00-K01-v1.md:74): ambiguous K1 references.** Rename §2 “Sequence K1 (\(\kappa=1\))”; explicitly write “accepted one-block Proposition K1” at the imported and \(k=1\) references. The new sequence lemma is vacuous at sequence parameter \(k=1\) and cannot replace that proposition.

2. **MINOR — [SOURCE00:94](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-k01-v1-review-v1/snapshot/00-K01-v1.md:94): incorrect boundary explanation.** SC0 already covers \(Y_0\) of length \(p+1\). Replace the \(\widehat\kappa=1\) clause with: “At \(k=p\), the endpoint-deletion argument fails in the involution-triple branch: its residual has length \(p\), and its weight lower bound is only \(2p-1\).” Indeed,
\[
Y=(pg)^3g^{p-1}
\]
has length \(p+2\) and only length-two zero-sums, but every endpoint deletion retains an involution pair. Its involution coefficient has absolute value \(p>k-1\). This is an obstruction at the **excluded sequence boundary**; retain the theorem’s \(k\le p-1\) scope.