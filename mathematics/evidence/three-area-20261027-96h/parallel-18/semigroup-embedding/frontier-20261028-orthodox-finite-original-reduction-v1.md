# Orthodox locally-finite-actor sources reduce to finite original sources

**NEW AUTHOR WRITTEN CANDIDATE with exact finite control; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:23:09 PDT 2026**. This is a scoped strengthening of `frontier-20261028-locally-finite-local-global-host-v1.md`, SHA `073d175108116583b1d91906436ce53dd53fdcac5961b97766516574789b5057`. Unlike the general local-to-global theorem, it permits finite **regular original-class** witnesses, but only when the ambient source is globally orthodox. It does not establish the finite obligations or solve the nonorthodox original problem.

## 1. Exact theorem

Let S be a regular, weakly E-unitary, locally r-orthodox semigroup with globally closed idempotents E(S) (that is, S is orthodox). Let its actual syntactic map `q:S→D` be onto and pure with D completely simple; as elsewhere, the assertion that the original hypotheses imply these q properties is the named SQ-E input. Assume a maximal subgroup G of D is locally finite.

Then S embeds in a locally regular-band-by-D physical host over EXACTLY q **iff** every finite subsemigroup F⊂S that itself is regular, weakly E-unitary and locally r-orthodox has a faithful physical host over its own actual syntactic q_F (equivalently, its canonical κ_(q_F) is injective, using the fixed-actor universal property).

In particular, conditional on the named finite-actor restriction and pure-CS actor pushforward, a theorem for ALL finite original-class sources would imply the original physical-host assertion for this entire orthodox locally-finite-actor subclass. It would NOT by this argument imply the nonorthodox case, non-locally-finite actor groups, or either printed question beyond the explicitly named scope.

## 2. Every finite subset has a finite regular original-class envelope

Brown's locally finite extension theorem and Green–Rees band local finiteness, at the precise scope written in the predecessor §5, imply S is locally finite because q is pure and G locally finite.

Let A be any finite subset of S. Choose one mutual inverse a' for every a∈A, and let

`F=⟨ A ∪ {a':a∈A} ⟩`.

F is finite by local finiteness. We show it is regular and remains original-class.

First, in an orthodox semigroup the product of chosen inverses in reverse order is an inverse of a product. For mutual inverse pairs a,a' and b,b', put e=a'a and f=bb'; both lie in E(S), and ef and fe are idempotent because E(S) is a band. Then

`(ab)(b'a')(ab)=a f e b = a e f e f b = a e f b=ab`,

using `ae=a`, `fb=b`, and `(ef)²=ef`. Dually,

`(b'a')(ab)(b'a')=b' e f a' = b' f e f e a' = b' f e a'=b'a'`,

using `b'f=b'`, `ea'=a'`, and `(fe)²=fe`. Induction gives an inverse in F for every word over A and A', by reversing the word and exchanging each a with a'. Hence F is regular.

E(F)=F∩E(S) is closed because both F and E(S) are subsemigroups, so F is orthodox. Weak E-unitarity is hereditary: any idempotent natural-order witness inside F is the same witness in S. For e∈E(F), E(eFe) is a subband of E(eSe), and the latter satisfies the regular-band identity by S's local-r hypothesis. Thus F is locally r-orthodox. This proves the envelope assertion, with no assertion that the ORIGINAL finite subsemigroup ⟨A⟩ was regular.

## 3. From an actual finite actor to the restricted global actor

For such a finite F, its actor image T=q(F) is a finite CS subsemigroup of D, and q|_F is onto and pure. Idempotence-context lifting gives the actual source quotient `q_F=f∘q|_F`, where `f:T→T/τ_T` is pure and onto; its local group map h is an isomorphism. These are the exact finite-image and pure-quotient inputs recorded in the predecessor and in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`.

A faithful q_F model can be pulled BACK to the restricted actor T without enlarging its band. In Rees coordinates write

`f(i,g,λ)=(a(i),u_i h(g) v_λ,b(λ))`,
`v_λ Q'_(b(λ),a(j)) u_j=h(Q_(λ,j))`.

If γ is the q_F-group action and c'_s the q_F-band coefficient, set `c_s=γ_(u_i^(-1))(c'_s)` and `α_g=γ_(h(g))`, where i is the T row of q(s). The q_F action weight is `u_i h(w_T)u_j^(-1)`, so the displayed row gauge gives `c_(st)=c_s α_(w_T)c_t`. If T actors and c values agree, the row gauges and q_F actors agree, hence the q_F model's faithfulness gives equality in F. Thus the model is faithful over q|_F, even if f collapses rows or columns.

For any smaller finite subsemigroup F0⊂F (possibly nonregular), restrict the F host to F0 and its finite CS actor image q(F0), again by the occupied-row gauge. Hence a host for the finite original envelope pays the nonregular finite obligations in the predecessor local-to-global theorem.

## 4. Both implications and limits

If S has a faithful q-host, restricting to each finite regular original-class subsemigroup F and pushing its pure actor image to q_F gives a faithful q_F model. Conversely, suppose every finite regular original-class F⊂S has a faithful q_F model. Every finite subset lies in such an F by §2, and §3 supplies the required host over the restricted global actor for every smaller finite subsemigroup. The first-order compactness/coinduction theorem of the predecessor then gives a faithful global model over q. This proves the stated equivalence.

The result uses global orthodoxy exactly to make reversed inverses stay inside finite generated envelopes. For general locally r-orthodox but globally nonorthodox S that step has not been established. Nor has any uniform or effective enumeration of all finite envelopes been proved; this is an infinitary criterion, not a terminating decision procedure for an arbitrary infinite S.

## 5. Exact nontrivial finite control

`frontier-20261028-orthodox-finite-closure-checker-v1.py`, SHA `a31de978c7657085cf1ba6ac8e93a3db75f80c6faf5f0af67e6e03662d68aeb2`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:23:09 PDT 2026**, exit0. It takes B to be the product of the pinned5-element locally regular but globally nonregular band and a4-element powerset semilattice, with C2 acting nontrivially on both factors. The40-element source B⋊C2 is orthodox, and its20 idempotents form a locally regular but NOT globally regular band.

```text
ambient orthodox source=40 idempotents=20 E locally regular but NOT globally regular
monogenic finite F=3 nonregular; inverse-closed finite Fprime=8 regular/WEU/local-r
PASS all inverse choices reversed, all Fprime products and local corners
```

The code checks the nonregular3-element subsemigroup, its8-element inverse-generated regular envelope, every relevant inverse reversal, WEU and local-r identities. This illustrates that the envelope theorem is not merely the special case in which every finite subsemigroup is already regular, and that its ambient E need not be globally regular. The finite check is same-author, not a proof of Brown/compactness or an independent witness review.

No finite-source universal theorem has been asserted here. No full-original, printed-Q1/Q2, human/cross-model/formal proof or novelty claim is made.
