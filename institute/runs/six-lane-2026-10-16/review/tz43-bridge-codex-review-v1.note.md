DISPOSITION: ACCEPT

## FATAL

none.

## MAJOR

**MAJ-1 — LANE — Unidentified external input in the unused Lemma R proof.**

`lane/README.md:LF92–93` invokes “TD(4,6), none exists” without identifying this as an imported theorem or supplying its proof. A TD(4,6) is equivalent to two orthogonal Latin squares of order 6: two groups supply row and column coordinates, and the other two supply the two entries. Its nonexistence is a substantive external result, not a consequence of the adjacent divisibility calculations.

This does **not** make Lemma R false, and neither consequence under review uses Lemma R.

**Minimal correction:** eliminate this unnecessary import. Every gcDCQS(\(m^k:2\)) ingredient requires a stem KF(\(m^k\)). If a frame has \(C\) classes and \(c_i\) miss group \(i\), point degrees give
\[
C-c_i=\frac{m(k-1)}2,\qquad C=\sum_i c_i,
\]
hence \(C=mk/2\) and \(c_i=m/2\). Thus \(m\) must be even. This directly excludes the odd-\(m\) cases \(m=1,3,9\) in `lane/README.md:LF91–94`, without either TD nonexistence assertion. Alternatively, explicitly identify and cite the TD(4,6) theorem. Keep “needs a direct construction” at `lane/README.md:LF99–100` scoped to the enumerated source constructions.

## MINOR

**MIN-1 — LANE — Incorrect multiplier fixed sets; the exclusion remains valid.**

`lane/README.md:LF192` says \(u=13,37,61\) have a fixed set comprising “a whole pair of groups.” On \(\mathbb Z_{72}\),
\[
\operatorname{Fix}(\mu_u)=\{a:(u-1)a=0\pmod{72}\}.
\]
For \(u=13,61\), \(\gcd(u-1,72)=12\), so the fixed set is \(6\mathbb Z_{72}\): six points in each of groups 0 and 2. Only \(u=37\), with gcd 36, fixes both entire groups.

**Minimal correction:** distinguish \(6\mathbb Z_{72}\) for \(13,61\) from \(2\mathbb Z_{72}\) for 37. All three exclusions still follow: a fixed triple consisting of a stem point and fixed points from groups 0 and 2 would require a fixed fourth point in a third group, which does not exist.

**MIN-2 — LANE — Inconsistent dihedral notation.**

`lane/README.md:LF187` writes \(D_{g/2}=C_g\rtimes\langle-1\rangle\). For \(g=18\), that semidirect product has \(18\cdot2=36\) elements, whereas `lane/sources/tz43-feasibility-and-bridge-v1.md:LF49–51` uses \(D_9\) among the order-18 groups.

**Minimal correction:** retain the unambiguous notation \(C_g\rtimes\langle-1\rangle\), state its order \(2g\), and remove or correct the dihedral subscript. This changes neither the regular-action lemma nor either bridge.

**MIN-3 — LANE — The FDH naming equivalence is unverified in this snapshot.**

`lane/evidence/fdgdd18-d15-inflated/construction-note.md:LF6–7` and `run/screening/math-1-tz43-contract.json:LF13` assert equivalence with Chang–Zheng–Zhou’s FDH(5,18,4,3) “by definition.” The supplied Tan–Zhou text defines FDGDD at `lane/sources/tz/tan-zhou-2503.11934.txt:LF241–247`; it supplies only the bibliographic entry for the frame-derived H-design paper at LF1125–1126, not that paper’s definition.

**Minimal correction:** supply the external FDH definition and compare it, or omit the secondary naming claim. This is an unverified nomenclature import, **not** a missing hypothesis: both constructions use Tan–Zhou’s FDGDD definition directly.

**Severity counts:** FATAL **0**; MAJOR **1**; MINOR **3**. The major finding concerns an unused auxiliary proof. There is no fatal or major defect in the mathematical bridge itself, and no SOURCE defect identified for this instance.

All **13 manifest-listed files** match their recorded SHA-256 hashes and byte counts. The snapshot contains precisely those files plus `manifest.json`. I also performed the permitted in-memory SXK check; no raw lane certificate or claimant code was executed.

## (a) Exact objects

**Conclusion: for these parameters, Formats S and D certify exactly the required Tan–Zhou objects; the FDH alias is unnecessary and externally unverified.**

The source defines an STS(\(v,h\)) as a GDD(2,3,\(v\)) of type \(1^{v-h}h^1\). A good colouring partitions its blocks into
\[
r=\chi'(v),\qquad a=r-\frac{v-h}{2}
\]
PPCs, with \(a\) PPCs avoiding the hole. I write \(a\) here because the source overloads \(s\), also used for stem size. Its displayed formulas are
\[
(r,a)=
\begin{cases}
((v-1)/2,(h-1)/2),&v\equiv3\pmod6,\\
((v+1)/2,(h+1)/2),&v\equiv1\pmod6,\ v\notin\{7,13\}.
\end{cases}
\]
See `lane/sources/tz/tan-zhou-2503.11934.txt:LF211–220`.

An SQS(\(v,h\)) covers every triple outside its hole exactly once and covers no triple contained in the hole. Its gcDSQS condition requires minimum-colourable derived STSs outside the hole and good-colourable incomplete derived STSs at hole points. See `lane/sources/tz/tan-zhou-2503.11934.txt:LF227–236`.

For the required gcDCQS,
\[
X=S\sqcup G_0\sqcup G_1\sqcup G_2\sqcup G_3,\qquad
|S|=2,\quad |G_i|=18,\quad |X|=74.
\]
The CQS condition is exactly coverage once of triples not contained in any \(S\cup G_i\), with no forbidden triple covered. This is the source’s CS/CQS definition, not a transverse-GDD condition on its quadruples. See `lane/sources/tz/tan-zhou-2503.11934.txt:LF256–266`.

The forbidden triples number
\[
4\binom{20}{3}=4\cdot1140=4560:
\]
different \(S\cup G_i\) intersect only in the two-point stem, so no triple is double-counted. Thus
\[
\binom{74}{3}-4560=64824-4560=60264
\]
triples are covered, giving \(60264/4=15066\) blocks.

A block cannot contain both stem points. A block containing one stem point has its other three points in three distinct groups. The nonstem block patterns are precisely \(2+2\), \(2+1+1\), and \(1+1+1+1\), as stated at `lane/README.md:LF14–19`.

At a group point \(x\in G_i\), the derived design is
\[
\operatorname{STS}(73,19),\qquad H_x=(G_i\cup S)\setminus\{x\}.
\]
In particular, the hole contains the **other 17 group points and both stem points**. It is not merely the other group points.

Its triple count is
\[
\frac{\binom{73}{2}-\binom{19}{2}}3
=\frac{2628-171}{3}=819.
\]
Each hole point has degree \((73-19)/2=27\), while each nonhole point has degree \((73-1)/2=36\). Hence
\[
19\cdot27=513
\]
triples meet the hole, and \(819-513=306\) avoid it. Since \(\chi'(73)=37\), the prescribed number of avoiding classes is
\[
37-\frac{73-19}{2}=10.
\]
These are exactly the requirements at `lane/sources/tz/tan-zhou-2503.11934.txt:LF281–288` and `lane/README.md:LF20–23`.

“Exactly ten” does not silently strengthen “there are ten.” A hole point occurs in 27 distinct classes, so among 37 classes at most ten can avoid the hole. If ten avoiding classes exist, all remaining 27 classes contain **every** hole point exactly once.

Nor does requiring 37 **nonempty** classes introduce a material restriction here. Each nonavoiding class contains 19 hole triples, using 38 nonhole points, and therefore at most five additional triples. Each avoiding class has at most 18 triples. If one avoiding class were empty, capacity would be at most
\[
27\cdot24+9\cdot18=810<819.
\]
The nonavoiding classes are already nonempty. Thus empty padding cannot occur.

At a stem point \(\alpha\), the derived design is on \(X\setminus S\), with groups \(G_i\), and is automatically a GDD(2,3,72) of type \(18^4\). It has
\[
\frac{\binom42\,18^2}{3}=648
\]
triples. Its required KF condition is precisely a partition into PCs of
\[
(X\setminus S)\setminus G_i=X\setminus(S\cup G_i).
\]
Each class therefore has \(54/3=18\) triples. If \(C\) is the class count and \(c_i\) counts classes missing \(G_i\), point degree gives \(C-c_i=27\). Summing yields \(C=36\) and \(c_i=9\). This matches the KF definition at `lane/sources/tz/tan-zhou-2503.11934.txt:LF237–240`, its use at LF288, and `lane/README.md:LF24–27`.

Consequently there are \(2\cdot648=1296\) stem-containing blocks and \(15066-1296=13770\) nonstem blocks.

For FDGDD(3,4,5{18}), the underlying design has **90 points in five groups of 18**. Its blocks are transverse quadruples, and it covers
\[
\binom53\,18^3=10\cdot5832=58320
\]
transverse triples, giving \(58320/4=14580\) blocks. At **every** point \(x\), the derived design is a KF(\(18^4\)) on the other 72 points, namely \(X\setminus G_x\). It has 648 triples, 36 frame classes of 18 triples, and nine classes missing each other group. This is exactly `lane/sources/tz/tan-zhou-2503.11934.txt:LF241–247`.

For comparison, RDGDD requires instead 27 full PCs, each of \(72/3=24\) triples. RDTD(3,4,\(m\)) is the four-group special case of RDGDD, not FDGDD.

The derived GDD properties need no additional checker hypothesis:

- At a group point of the CQS, pair coverage follows by adjoining that point to each eligible pair; pairs inside \(H_x\) are forbidden.
- At a stem point, adjoining the stem point covers every cross-group pair once; same-group pairs are forbidden.
- At a point of the transverse GDD, adjoining it covers every pair from two other groups once.

Thus the coverage and exact derived-class partitions in `lane/README.md:LF114–131` imply all underlying derived-design axioms. Ordered labels and class numbering are serialization choices. No symmetry or class-size profile is imposed.

## (b) Scope of §4(3)

**Conclusion: gcDCQS(18⁴:2) together with FDGDD(3,4,5{18}) answers exactly the positive construction request, under the stipulated certificate assumptions.**

The request at `lane/sources/tz/tan-zhou-2503.11934.txt:LF1114–1116` is
\[
A\ \land\ (\mathrm{FDGDD}\ \lor\ \mathrm{RDGDD}).
\]
It does not require both B alternatives. Four groups in A and five groups in B are the stated parameters, not inconsistent conventions. Neither the two-point stem nor the group size 18 is an added restriction.

The exponent’s positive range is supplied by Lemma 3.8’s “any positive integer \(n\)” at `lane/sources/tz/tan-zhou-2503.11934.txt:LF1070–1071`. Renaming that exponent \(t\) and writing \(t\ge1\) changes no quantifier. The family note handles \(t=1\) separately and uses the fan construction for \(t\ge2\).

The current statements remain appropriately qualified: `lane/README.md:LF43–64` identifies worker-passing candidates and keeps parent verification and other reviews separate; `lane/sources/tz43-family-consequence-v1.md:LF67–70` expressly conditions the family on the finite inputs and imported results.

The contract’s nonexistence exit is an additional research-policy alternative, not a positive construction. Logically, disproving only the FDGDD alternative would leave RDGDD open. No such exit is invoked here.

## (c) Order 74

**Conclusion: Construction 2.1 applies correctly, and the stipulated direct order-74 checks independently establish mcDSQS(74) from the definitions.**

Here \(g=18,n=4,s=2\), so
\[
gn+s=74=6\cdot12+2.
\]
The three hypotheses of `lane/sources/tz/tan-zhou-2503.11934.txt:LF292–293` are met:

1. The assumed Format-S certificate supplies gcDCQS(\(18^4:2\)).
2. The SXK transcription supplies mcDSQS(20).
3. The same design, with any designated pair as hole, supplies gcDSQS(20,2).

For the third assertion, an SQS(20,2) is simply an SQS(20) with a designated two-point hole: a two-point set contains no triple. At a hole point \(\alpha\), the derived STS(19,1), with hole \(\{\beta\}\), is still the full STS(19). In every ten-colouring of an STS(19), \(\beta\) has degree nine and occurs at most once per class. It therefore occurs in exactly nine classes and is absent from exactly one:
\[
\chi'(19)-\frac{19-1}{2}=10-9=1.
\]
This is automatic for **every** such ten-colouring. The argument at `lane/evidence/mcdsqs74-c21/construction-2.1-hypotheses.md:LF23–30` is correct.

The permitted independent transcription check passed: the 16 bases at `lane/sources/sxk/sxk_prop3_transcription.json:LF10–12` develop to 285 distinct blocks covering all 1140 triples once. The cells at LF15–25 are disjoint PPCs partitioning the 57 derived triples at 0; their sizes are eight sixes, one five, and one four. Cyclic translation supplies every other point. Since \(9\cdot6=54<57\), ten colours attain the global minimum.

The lane’s merges match the source’s formulas at `lane/sources/tz/tan-zhou-2503.11934.txt:LF321–335`:

- At \(x\in G_i\), pair the ten local classes on \((G_i\cup S)\setminus\{x\}\) with the ten CQS classes avoiding that entire set, retaining the other 27 classes.
- At a stem point \(\alpha\), pair the nine frame classes missing \(G_i\) with the nine local classes containing \(\beta\).
- Each remaining local class avoids \(\beta\), hence lies wholly in its own \(G_i\). Their union is a PPC because the four groups are disjoint.

The distinguished \(G_0\) copy in the source proof causes no exception: the degree-nine argument also supplies its one \(\beta\)-avoiding class. Thus the lane obtains \(4\cdot9+1=37\) stem classes exactly as claimed at `lane/evidence/mcdsqs74-c21/construction-2.1-hypotheses.md:LF32–46`.

The block count is
\[
15066+4\cdot285=16206=\binom{74}{3}/4.
\]
At a group point the derived count is \(819+57=876\); at a stem point it is \(648+4\cdot57=876\).

For the direct certificate, an STS(73) has
\[
73\cdot72/6=876
\]
triples, while a PPC contains at most 24. Hence
\[
36\cdot24=864<876.
\]
This is a lower bound for **every** STS(73). Any checked derived 37-colouring supplies an upper bound for the minimum over all STS(73)s. Consequently \(\chi'(73)=37\), and all 74 checked derived designs attain the source’s global minimum. No external chromatic-index theorem is needed for this finite conclusion. See `lane/evidence/mcdsqs74-c21/receipt-v1.json:LF15–21`.

The two raw versions remain distinct:

- UTF-8-comment version: `eaff77fc…16c3`, identified at `lane/evidence/mcdsqs74-c21/receipt-v1.json:LF10–18`.
- ASCII version: `1122f1f4…eb4c`, identified at `lane/evidence/mcdsqs74-c21-ascii-v2/receipt-v2.json:LF5–21`.

The newer receipt expressly preserves separate parent dispositions at LF33, as does `lane/README.md:LF54–58`. Older documents naming only the older version are not claims that the newer raw bytes had already been accepted.

## (d) Family

**Conclusion: the written FDGDD → Construction 2.3 → Construction 2.1 route is valid for every \(t\ge2\); the direct order-74 witness supplies \(t=1\).**

Put \(M=4^t\). Lemma 3.8 supplies an RDS(3,5,\(M+1\)). Delete \(\infty\), and define
\[
\mathcal B=\{A\setminus\{\infty\}:\infty\in A\},\qquad
\mathcal T=\{A:\infty\notin A\}.
\]
Every pair in the remaining \(M\) points extends with \(\infty\) to exactly one original block, so \(\mathcal B\) is an S(2,4,\(M\)). Every remaining triple belongs either to a block obtained by deleting \(\infty\), or to a block in \(\mathcal T\), exclusively. Taking singleton groups therefore gives exactly the 1-FG of type \(1^M\) defined at `lane/sources/tz/tan-zhou-2503.11934.txt:LF248–255`. The same deletion is explicitly stated at LF343–345.

**Only the underlying S(3,5,\(M+1\)) is needed for this fan.** Resolvability is additional structure supplied by the imported RDS theorem. The lane says this correctly at `lane/sources/tz43-family-consequence-v1.md:LF28–35`.

Construction 2.3 permits \(g=1\): its statement at `lane/sources/tz/tan-zhou-2503.11934.txt:LF444–447` imposes no contrary restriction, and the preceding definition explicitly discusses singleton-group fans.

The complete substitution is
\[
(m,g,n,s)=(18,1,M,2),\qquad K_1=\{4\},\quad K=\{5\}.
\]
Therefore
\[
mgn+s=18M+2\equiv2\pmod6,\qquad mk_1+s=74\equiv2\pmod6.
\]
Its required ingredients are precisely the supplied gcDCQS(\(18^4:2\)) and FDGDD(3,4,5{18}), and its output is gcDCQS(\(18^M:2\)). The substitution at `lane/sources/tz43-family-consequence-v1.md:LF37–47` is correct.

There is no hidden compatibility requirement in the shared-stem construction:

- At a local group point, the 27 nonavoiding classes may be labelled arbitrarily by \((y,j)\), with \(y\) in the other three local groups and \(1\le j\le9\). This is a bijection between two 27-element sets; the source does not require these classes to miss group \(y\).
- The 36 local stem-frame classes have exactly nine classes missing each group, by the degree count in (a), so their \((y,j)\) labels are automatic.
- Each FDGDD derived frame likewise has nine classes per missed group.

These are precisely the local labels used at `lane/sources/tz/tan-zhou-2503.11934.txt:LF456–476`.

For a fixed pair \(x,y\) of fan points, its unique \(\mathcal B\)-block and the \(\mathcal T\)-blocks containing that pair partition the other fan points through their remaining points. The FDGDD frame pieces indexed by \(y\) omit both \(x\)’s and \(y\)’s fibres. Consequently their supports are disjoint from each other and from the selected local CQS piece. This justifies the unions at `lane/sources/tz/tan-zhou-2503.11934.txt:LF498–521`.

The ten avoiding classes are united across the \(\mathcal B\)-blocks through \(x\). Those blocks intersect only in \(x\), and the selected classes avoid \(x\)’s fibre and the stem. The resulting colouring has
\[
9(M-1)+10=9M+1
\]
classes, ten avoiding the global hole of size 19.

At a stem point, for fixed \(y,j\), unite the local frame classes missing \(y\). The sets \(B\setminus\{y\}\), over \(\mathcal B\)-blocks containing \(y\), partition the other fan points. The union is therefore a PC missing exactly \(y\)’s fibre. There are \(9M\) such classes, nine per final group, as required by the source’s formulas at LF532–539.

Thus arbitrary separate copies of the certified ingredient suffice. No synchronization of colour labels between different derived points, stem points, or fan blocks is needed.

Construction 2.1 then uses the same mcDSQS(20)/gcDSQS(20,2) filling. Its derived colour count is \(9M+1\). This also attains the universal lower bound: write \(18M+1=6k+1\), where \(k=3M\). An STS(\(6k+1\)) has \(k(6k+1)\) triples and each PPC has at most \(2k\), so \(3k\) colours cannot suffice. The required minimum is therefore \(3k+1=9M+1\).

The FD/RD choice is correct. **FDGDD is used in Construction 2.3; RDGDD would be needed for Construction 2.2.** The lane expressly distinguishes them at `lane/sources/tz43-family-consequence-v1.md:LF54–56`. Neither Theorem 2.5’s sufficient RDTD criterion nor Corollary 2.6 is used.

For \(t=1\), the original S(3,5,5) consists of one block; deletion gives one four-block and \(\mathcal T=\varnothing\). The lane avoids any empty block-size-set convention by using the direct order-74 result instead, at `lane/sources/tz43-family-consequence-v1.md:LF58–70`.

The orders are
\[
74,\quad290,\quad1154,\quad4610,\ldots
\]
The lane explicitly identifies higher orders as recursive mathematical consequences, not supplied certificates or generated formal proofs.

The other tuple \((18,4,4,2)\) outputs gcDCQS(\(72^4:2\)), on 290 points, rather than gcDCQS(\(18^4:2\)). Its fan description is valid:

- Deleting a point from S(3,5,17) gives 20 four-blocks, since \(\binom{16}{2}/\binom42=20\).
- There are \(68-20=48\) five-blocks, since \(\binom{17}{3}/\binom53=68\).
- Choose a PC of four derived four-blocks as the four groups, leaving 16 blocks in \(\mathcal B\).
- Both unions \(\mathcal G\cup\mathcal B\) and \(\mathcal G\cup\mathcal B\cup\mathcal T\) are unchanged, so their Steiner coverage identities persist.

A five-block on four groups necessarily meets some group twice. This is permitted: the fan definition does **not** impose GDD transversality on \(\mathcal T\). It prohibits three points in a group, because that triple is already covered by the group. Thus `lane/sources/tz43-feasibility-and-bridge-v1.md:LF68–73` is mathematically correct.

The Remark at source LF542–543 is unnecessary here: \(K_1=\{4\}\), so “some” versus “every” block size introduces no distinction.

## (e) Lane overclaims and auxiliary lemmas

**Conclusion: the current consequence statements preserve conditionality; the auxiliary mathematical statements are sound apart from the identified proof-provenance and precision defects.**

The 19:16 feasibility note’s “B still missing” statements are historical: its timestamp is at `lane/sources/tz43-feasibility-and-bridge-v1.md:LF3`, while B’s later pin is recorded at `lane/README.md:LF43–52`. The later construction deliberately uses a bare size-6 H-design followed by newly found size-18 frames; it does not claim to have produced an FDGDD size-6 seed. See `lane/evidence/fdgdd18-d15-inflated/construction-note.md:LF20–26` and LF39–52.

The current uses of “complete” and “accepted” are qualified as worker certificate/checking statements. They do not claim completed parent acceptance or a completed gate. Higher-order certificates and formal proofs are expressly excluded from the result’s stated scope.

The requested lemma audit is:

- **Lemma N — correct.** The degree argument in (a) forces all 19 hole points into every nonavoiding class. Such a class has 19 hole triples and \(m\le5\) free triples, missing \(16-3m\) nonhole points. An avoiding class has \(k\le18\) triples. Therefore
  \[
  \sum(5-m)+\sum(18-k)=27\cdot5+10\cdot18-306=9.
  \]
  Nonhole degree 36 means each is missed once. The comparison slacks are also correct: for \(20^4:0\), \(30\cdot7+10\cdot20-400=10\); for \(32^4:0\), \(48\cdot11+16\cdot32-1024=16\). See `lane/README.md:LF74–78`.

- **Lemma K — correct.** A stem-derived triple meets three distinct groups. A regular diagonal action has trivial stabilizer on it, and development visits every coordinate exactly once in each of those groups. Its 18 translates are therefore a PC missing the fourth group. See `lane/README.md:LF80–84`.

- **Lemma R — correct conclusion, with MAJ-1 in the written proof.** Odd ingredient sizes can be excluded directly by stem-frame parity. For \(m=2,g=9\), triple-block pair coverage would require degree \(27/2\), impossible. For \(m=18,g=1\), usable four-block ingredients are circular. The remaining \(m=6,g=3\) argument also checks out: each point has
  \[
  \binom{11}{2}-\binom22-3\binom32=55-1-9=45
  \]
  triples left for \(\mathcal T\). A T-block has size at most eight because it cannot contain three points of a group, and at least five because its FDGDD ingredient needs at least four derived frame groups. Thus
  \[
  45=21a+15b+10c+6d
  \]
  gives exactly the four listed patterns. If \(n_8\) counts points of pattern \(8\cdot5^4\), block incidences require \(8\mid n_8\) and \(5\mid4n_8\); since \(n_8\le12\), \(n_8=0\). Heptad incidences then give \(7b_7=12+2n_2\), so \(n_2=1\) or 8. The former requires three heptads through a point when only two exist. The latter gives four heptads with total pairwise intersection 24, although six pairs of distinct Steiner 3-system blocks could total at most 12. This is a valid contradiction. See `lane/README.md:LF86–100`.

- **Lemma W — correct for positive odd weights.** For fixed \(\alpha,c\), the coordinate maps \(\beta,\beta+c,-\alpha-2\beta-c\) are permutations because 2 is invertible modulo the weight. Their triples therefore form PCs over each master PPC. Every zero-sum derived triple determines \(\beta\) and \(c\) uniquely. This proves both frame and resolvable lifting claims. The explicit weight-three ingredient is not invalidated by Theorem 2.5’s merely sufficient criterion. The separate H(5,2,4,3) nonexistence statement is expressly labelled an import and is not proved in the snapshot. See `lane/README.md:LF102–110`.

- **Lemma I — correct in the stated four-group action.** The unique block through \(\{\alpha,y,z\}\) is invariant when \(\alpha\) is fixed and \(y,z\) are exchanged. Its fourth point is fixed and belongs to a third group. A double transposition of all four groups has no such fixed point. An \(A_4\)-action cannot evade this by swapping the stem pair: every homomorphism \(A_4\to S_2\) is trivial. See `lane/README.md:LF187` and `lane/sources/tz43-feasibility-and-bridge-v1.md:LF28–31`.

- **Lemma 3.1 cyclic-model remarks — correct model and obstruction, with MIN-1’s fixed-set error.** The published group is exactly the 32-cycle together with a stem swap, at `lane/sources/tz/tan-zhou-2503.11934.txt:LF871–876`. The subgroup generated by \(\rho^4\) acts regularly within each group and fixes the stems, so Lemma K applies. All listed multiplier exclusions remain valid after correcting their fixed sets. See `lane/README.md:LF192`.

- **Lemma F′ — correct.** The fixed derived STS(25,7) has
  \[
  [\binom{25}{2}-\binom72]/3=93
  \]
  triples: \(7\cdot9=63\) meeting its hole and 30 avoiding it. A fixed nonhole point has degree 12. An invariant class containing a fixed point must use an entirely fixed triple, since an order-three action has no nontrivial two-point orbit. This forces nine invariant nonavoiding classes and a total of 12 or 13 invariant classes. Twelve would accommodate at most \(9\cdot1+3\cdot6=27<30\) hole-free fixed triples. Hence there are 13, including exactly four avoiding ones. The forced orbit specification and good restriction follow. See `lane/README.md:LF207`.

- **Lemma C8 — correct for the stated Singer action and invariant-colouring models.** The fixed derived STS(9,3) has
  \[
  [\binom92-\binom32]/3=11
  \]
  triples; each fixed hole point lies in three. An invariant nonavoiding class uses all six fixed nonhole points in its three fixed hole triples. Its two nonfixed hole orbits consume four of the six nonhole orbits of size eight, leaving only two, insufficient for another disjoint triple orbit. Thus it has no hole-free triples. Exactly three such classes are forced by the fixed stem, contributing deficit \(3\cdot5=15>9\), a contradiction. This proves the symmetric-colouring obstruction, not unrestricted nonexistence. For the smaller cyclic Singer stabilizers, the later \(-I\) exclusion is also justified by the stem anchor: a \(-I\)-invariant stem triple must lie in the fixed subdesign, forcing its containing nonavoiding class to be invariant under the full stabilizer. The three fixed triples through \((4,0,0)\) already occupy those classes. See `lane/README.md:LF214`.

The empirical claims about particular rejected samples, solver runs, and diagnostics were not independently checked here.

## HYPOTHESIS TABLE

“CERTIFIED-OBJECT” below means worker-checked with independent parent verification pending, except that the small SXK transcription was additionally checked in memory during this review.

| Hypothesis | How it is met | Status |
|---|---|---|
| \(t\ge2\), \(M=4^t\), \(q=4\) a prime power | \(4=2^2\); parameter substitution | DEFINITIONAL |
| S(3,5,\(M+1\)) | Supplied with additional resolvability by Lemma 3.8 | IMPORT |
| 1-FG(3,({4},{5}),\(M\)) of type \(1^M\) | Delete one point; pair/triple coverage proves the fan identities | DEFINITIONAL |
| Construction 2.3 permits \(g=1\) | Its statement and the explicit singleton-type fan definition | DEFINITIONAL |
| \(mgn+s\equiv mk_1+s\equiv2\pmod6\) | \(m=18,g=1,n=M,s=2,k_1=4\) | DEFINITIONAL |
| gcDCQS(\(18^4:2\)) | Format-S certificate `1382d572…282e` | CERTIFIED-OBJECT |
| FDGDD(3,4,5{18}) | Format-D certificate `3e22f502…a998` | CERTIFIED-OBJECT |
| Local class labels/shared stem | Arbitrary bijections for 27 classes; nine frame classes per missed group; fan support disjointness | DEFINITIONAL |
| Construction 2.3, \(2\bmod6\) branch | Tan–Zhou LF444–541; applicable proof audited above | IMPORT |
| Output type \(18^M:2\) | \((mg)^n:s=18^M:2\) | DEFINITIONAL |
| mcDSQS(20) | Finite cyclic transcription and ten cells | CERTIFIED-OBJECT |
| gcDSQS(20,2) | Designate any pair; degree nine forces one avoiding class | DEFINITIONAL |
| Construction 2.1 | Tan–Zhou LF292–335; filling merge audited above | IMPORT |
| Required minimum colour count | Source (1.1); alternatively the universal capacity bound plus the constructed colourings | IMPORT / DEFINITIONAL |
| \(t=1\) | Direct order-74 certificate, with 37 classes at every point | CERTIFIED-OBJECT |

There is **no GAP in the required family route** under the stated assumptions. The unused FDH name and Lemma R are not hypotheses.

## IMPORTS

1. **Lemma 3.8 / Witt [20] / Zhou–Chang [25].** Needed: an S(3,5,\(4^t+1\)) for every \(t\ge2\). The cited lemma supplies the stronger RDS statement. Source: `lane/sources/tz/tan-zhou-2503.11934.txt:LF1070–1071`, references LF1178–1179 and LF1194. The lane explicitly identifies this import and the absence of a re-proof at `lane/sources/tz43-family-consequence-v1.md:LF28–35`.

2. **Construction 2.3, \(2\bmod6\) branch.** Needed: the certified four-group gcDCQS and five-group FDGDD, together with the singleton fan, produce gcDCQS(\(18^{4^t}:2\)). Source: `lane/sources/tz/tan-zhou-2503.11934.txt:LF444–541`. The lane explicitly invokes it at `lane/sources/tz43-family-consequence-v1.md:LF37–47`. The relevant proof is supplied by Tan–Zhou; the citation to Chang–Zhou [3] at LF449 concerns the other, \(4\bmod6\), branch.

3. **Construction 2.1, \(2\bmod6\) branch.** Needed: filling the CQS with mcDSQS(20)/gcDSQS(20,2) gives the claimed mcDSQS. Source: `lane/sources/tz/tan-zhou-2503.11934.txt:LF292–335`. Explicitly invoked at `lane/sources/tz43-family-consequence-v1.md:LF49–50` and LF67–70. Again, the needed proof is in Tan–Zhou; its [3] citation concerns the other congruence branch. The direct order-74 checks bypass this theorem.

4. **mcDSQS(20): Lemma 3.4 / Shi–Xia–Krotov [16], using the cyclic SQS from Phelps [14].** Source: `lane/sources/tz/tan-zhou-2503.11934.txt:LF903–906`, references LF1161 and LF1166–1167. The lane explicitly identifies the SXK input at `lane/evidence/mcdsqs74-c21/construction-2.1-hypotheses.md:LF15–21`. The supplied transcription independently establishes the needed finite existence; matching it to the original publication remains a provenance question.

5. **Equation (1.1) / [19].** Needed in the lane’s numerical identification of \(\chi'(19)\), \(\chi'(73)\), and family colour counts. Source: `lane/sources/tz/tan-zhou-2503.11934.txt:LF110–130`, reference LF1175–1176. The lane names (1.1) at `lane/README.md:LF22–23` and LF119. For these consequences, universal capacity bounds plus the exhibited colourings independently establish the required global minima.

6. **Auxiliary, unused imports.** Lemma R invokes TD(4,6) nonexistence without a source; MAJ-1 gives an elementary replacement. Lemma W expressly imports H(5,2,4,3) nonexistence from an unavailable screen at `lane/README.md:LF108–110`. The external FDH naming assertion is covered by MIN-3. None is needed by the accepted bridge.

The fan deletion identities, two-point-hole identification, class-label bijections, and frame multiplicities are elementary deductions, not additional existence imports.

## UNKNOWN

- The raw A, B, and order-74 certificates are absent from this snapshot. Their actual contents, checker implementations, replay claims, and raw-file hashes were therefore not independently verified here; the review uses the stipulated certificate assumptions.
- The original Witt, Zhou–Chang, SXK, and Chang–Zheng–Zhou papers are absent. Applicability of the supplied Tan–Zhou statements was checked, but those external proofs and the FDH terminology were not independently audited.
- The asserted noncomment-byte identity of the two order-74 raw versions is supported by their supplied receipt, not by a comparison performed here.
- The underlying sample files, CNFs, nonframe diagnostic, and solver logs are absent. Their empirical claims remain unverified and are unnecessary for this bridge.
- No explicit certificate or formal proof for \(t\ge2\) was supplied or checked. The accepted higher-order claim is the stated conditional mathematical consequence of the finite objects and identified imports.