# F587 — Written review of the finite regular pure-\(C_2\) source and universal collision frontier

**Role:** WRITTEN  
**Disposition:** SUPPORTED at the explicitly partial written scope described below.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR at that partial scope.**  
**Negative witness:** NOT PROVED.  
**SEP:** UNPROVED.  
**COLL:** UNPROVED.

The construction does specify a finite regular noninverse semigroup with an idempotent-pure quotient onto the prescribed \(C_2\). Its coordinate calculations, least-group-congruence claim and finite universal-host bound are supported by the written reconstruction below. It does **not** establish that its proposed pair is distinct after the source quotient, that the pair collides in the universal band, or that this source fails to embed in every band-by-group host.

## 1. Read boundary, chronology and attribution

Before reading any mathematical packet body, I completely read:

- `manifest-v1.json`, LF 1–119;
- `freeze-receipt-v1.json`, LF 1–47;
- `parent-dispatch-receipt-v1.json`, through its ending;
- `parent-live-metadata-supply-v1.json`, through its ending;
- every control listed in the manifest, through its ending:
  - owner frontier-first direction;
  - L1 selected-diagnostic quarantine;
  - written-duty execution/reporting deviations;
  - held PH registration/report-consumer quarantine;
  - F439, F444, F448, F508 and F513 selected-diagnostic quarantines;
  - AME held-claim-consumer quarantine;
  - CORE-GRAM auxiliary-operator quarantine;
  - privacy auxiliary-parameter quarantine.

These controls were used only as permission/status and exclusion records. I did not follow their links into held mathematical material.

I then sent the required direct administrative pre-body ACK to `agent://Main`. Only afterward did I read `literal-packet-v1.md` in consecutive, ordered raw windows of at most 20 LF, covering **LF 1–564 without a gap**, including the terminal S1 and S2 lines. The packet contains S1 logical lines 1–521 and S2 lines 1–41.

The following are **parent-supplied live metadata**, not hashes or clock observations executed by me:

- Manifest SHA256: `00ce68f8ec3fd98dfbfa12139c313b4aaadb77d6f9d368155680cc2f8d478207`
- Freeze-receipt SHA256: `3ea6da71cc2302abbde1800d5ad9e72d4c3ca81bbf89f0c040f18bb84ea2c4db`
- Packet SHA256: `785f011b9559ffb878d1e668129a3236699348a189077623b208b5eba939954f`
- Parent observation: `2026-10-30T13:56:13-0700 PDT`

That parent clock is not a child-native start, completion or execution timestamp.

**Scientific execution: NOTRUN.** No scientific code, interpreter, CAS, solver, enumeration, replay, build, test, lint or formatter was run. No new selected mathematical instance or private diagnostic was introduced. I did not follow public-source links, author-code links, prior-review links or sibling-return links. The written work below reconstructs the frozen general arguments and the explicitly supplied construction and left-zero map; it does not add a new finite model.

This complete body is returned for parent materialization. I did not write a repository artifact.

## 2. Exact import and review scope

The mathematical import boundary is the elementary band fact stated in **S1 LF 178–204**:

> In a band, Green’s \(\mathcal D\) is a semilattice congruence, and each \(\mathcal D\)-class is a rectangular band.

The free-band universal property and elementary semigroup-congruence constructions are used in their usual meanings. The local-finiteness bound, source regularity, quotient purity, noninverseness, least-group-congruence equality and universal-host implications are reconstructed below.

For S2, the relevant inputs are the actor-rigidity statement in **LF 7–9** and the universal construction in **LF 15–25**. Their needed arguments are reconstructed here rather than accepted from the linked prior reviews.

The separate Green-coordinate separation statement, unit-regular classification, illustrative examples and historical finite-run results in S2 are not newly certified by this review. In particular, the finite-run counts in **S2 LF 41** are not my execution evidence and are not used to prove anything about the present source quotient.

The reported necessary condition **(N)** in **S1 LF 141–156** is an **external theorem import**, not an established theorem of this review. Its application is therefore conditional.

## 3. Finite band and ambient semigroup

### 3.1 Local finiteness and the stated bound — SUPPORTED

**Evidence:** S1 LF 178–204.

Let \(w\) have \(k\) distinct letters. Let \(p=s\sigma\) be its shortest prefix containing all those letters, and let \(r=\varepsilon t\) be its shortest suffix containing all those letters.

Because \(p\) is a prefix of \(w\), writing \(w=pv\) gives
\[
pw=p(pv)=p^2v=pv=w.
\]
Likewise \(wr=w\). The words \(p,w,r\) have the same content, so their evaluations are in the same rectangular \(\mathcal D\)-class. Hence
\[
w=pwr=pr=s\sigma\varepsilon t.
\]

Each of \(s,t\) has at most \(k-1\) distinct letters. Empty \(s\) or \(t\) denotes omission of a factor in the resulting word, not an assumed identity element in the band. Thus the representative-length recurrence
\[
L_0=0,\qquad L_k=2L_{k-1}+2
\]
is valid, giving
\[
L_k=2^{k+1}-2.
\]

Every element of the free band on \(k\) letters therefore has a nonempty representative of length at most \(L_k\), and
\[
|F_k|\le \sum_{j=1}^{L_k}k^j.
\]

Consequently the ten-letter band \(F\) is finite and the supplied bound \(L_{10}=2046\) is valid. This is a mathematical finiteness argument, not a claim of feasible enumeration.

### 3.2 Ambient multiplication — SUPPORTED

**Evidence:** S1 LF 208–238.

The alphabet permutation \(\tau\), exchanging subscripts \(0\) and \(1\), preserves band identities and induces an automorphism of \(F\) with \(\tau^2=1\).

Therefore
\[
(u,h)(v,k)=\bigl(u\,\tau^h(v),h+k\bigr)
\]
defines the stated associative semidirect product \(F\rtimes C_2\), with group coordinates interpreted additively.

The seven named generators specify a definite subsemigroup \(S_0\), and
\[
|S_0|\le 2|F|\le 2\sum_{j=1}^{2046}10^j.
\]
No multiplication table has been enumerated, but the finite carrier and multiplication are mathematically specified by this construction.

## 4. Regularity and purity inside \(S_0\)

### 4.1 The reverse-star argument — SUPPORTED

**Evidence:** S1 LF 242–270.

For each supplied generator \(x=(\ell_x,h_x)\), its named star has coordinates
\[
x^*=\bigl(\tau^{h_x}(\ell_x),h_x\bigr).
\]
For \(e,f,g\), this fixes the generator; for \(a,a'\) and \(b,b'\), it exchanges the displayed names.

Let \(W=x_1\cdots x_n\) evaluate to \((u,h)\), with first-coordinate word
\[
w=\ell_{x_1}\,
\tau^{h_{x_1}}(\ell_{x_2})\cdots
\tau^{h_{x_1}+\cdots+h_{x_{n-1}}}(\ell_{x_n}).
\]
Expanding the reversed starred word gives
\[
W^*=\bigl(\tau^h(\operatorname{rev}w),h\bigr).
\]
The total group coordinate remains \(h\), since it lies in \(C_2\). Reversal is compatible with the band presentation: reversing a word-square relation again produces a word-square relation.

The evaluations of \(w\) and \(\operatorname{rev}w\) have the same content, hence lie in the same rectangular \(\mathcal D\)-class. Thus
\[
w\,\operatorname{rev}w\,w=w,\qquad
\operatorname{rev}w\,w\,\operatorname{rev}w=\operatorname{rev}w.
\]
With the actual \(\tau^h\)-twists included, these give
\[
WW^*W=W,\qquad W^*WW^*=W^*.
\]

Crucially, \(W^*\) is a word in the same seven generators. This proves regularity **inside \(S_0\)**, not just regularity of the ambient host. It does not require choosing a unique word representative or asserting that the named star supplies unique inverses.

### 4.2 The pure quotient \(q_0\) — SUPPORTED

**Evidence:** S1 LF 265–270.

The second projection is onto because the supplied generators include both group coordinates. Every \((u,0)\in S_0\) satisfies
\[
(u,0)^2=(u^2,0)=(u,0).
\]
An idempotent cannot have group coordinate \(1\), because its image in \(C_2\) must be the identity \(0\).

Therefore
\[
q_0^{-1}(0)=E(S_0).
\]
In particular, the displayed \(a'\) and \(b'\) are regular inverses of \(a\) and \(b\), respectively.

## 5. The precise source quotient and its coordinate semantics

### 5.1 The four relations preserve the prescribed quotient — SUPPORTED

**Evidence:** S1 LF 274–306.

Each side of R1–R4 has group coordinate \(0\). Hence the kernel congruence of \(q_0\) contains all four defining pairs. By minimality of the **semigroup congruence on \(S_0\)** generated by those pairs,
\[
\theta\subseteq\ker q_0.
\]

Thus \(q_0\) induces a well-defined onto homomorphism
\[
q:S_0/\theta\longrightarrow C_2.
\]

The quotient \(S=S_0/\theta\) is finite and associative. Regularity passes to it using the images of the inverse witnesses already constructed in \(S_0\).

If \(q(x\theta)=0\), then \(q_0(x)=0\), so \(x^2=x\) already in \(S_0\); consequently \(x\theta\) is idempotent. Conversely, an idempotent has identity group image. Therefore
\[
q^{-1}(0)=E(S).
\]
Its idempotents form a subsemigroup because they are exactly this identity fibre. The asserted finite, regular, orthodox and pure-onto-\(C_2\) properties follow.

### 5.2 Consuming the twists in R1–R4 — SUPPORTED

**Evidence:** S1 LF 353–366.

Expanding with the displayed semidirect multiplication gives the following first-coordinate pairs, each with total group coordinate \(0\):
\[
\begin{aligned}
\mathrm{R1}:&\quad e_0a_0=e_0,\\
\mathrm{R2}:&\quad e_0b_0=e_0,\\
\mathrm{R3}:&\quad a_1f_0g_0=f_0g_0,\\
\mathrm{R4}:&\quad
b_1f_0a_1e_1a_1f_0g_0
=f_0a_1e_1a_1f_0g_0.
\end{aligned}
\]
The repeated adjacent letters arising in the expansion have been reduced using band idempotence. The subscript changes in R3 and R4 agree with the accumulated \(C_2\) coordinate.

These are coordinate descriptions of the **specific defining pairs in \(S_0\)**. They do not authorize arbitrary contextual rewriting in the ambient free band. Closing these equations under all ambient band or ambient semidirect-product contexts could produce a larger congruence and a different quotient. The author explicitly excludes that change in **S1 LF 306**, and the later source claims do not require making it.

## 6. Noninverseness and the proposed pair

### 6.1 The supplied left-zero image proves noninverseness — SUPPORTED

**Evidence:** S1 LF 310–333.

The prescribed letter map to the two-element left-zero band \(L=\{E,F\}\) is \(\tau\)-invariant. It therefore induces the displayed homomorphism to \(L\times C_2\), and restriction to \(S_0\) is legitimate.

Under that map, R1 and R2 have first coordinate \(E\) on both sides; R3 and R4 have first coordinate \(F\) on both sides. All have group coordinate \(0\). Its kernel therefore contains \(\theta\), so the homomorphism factors through the **actual** source quotient \(S\).

The images of \(ef\) and \(fe\) are respectively \((E,0)\) and \((F,0)\). Consequently \(ef\ne fe\) in \(S\). Both are products of idempotents, and the idempotents of \(S\) do not commute. Thus \(S\) is not inverse.

This establishes only the claimed noninverse property.

### 6.2 The source pair and its coordinates — SUPPORTED

**Evidence:** S1 LF 339–374.

For
\[
U=eafg,\qquad V=ebfa'eafg,
\]
the accumulated group coordinate is \(1\) in each case.

Their prequotient ambient first coordinates are exactly
\[
e_0a_0f_1g_1
\]
and
\[
e_0b_0f_1a_0e_0a_0f_1g_1.
\]
In the second expression, the action before \(a'\) sends \(a_1\) to \(a_0\); after that factor the accumulated coordinate returns to \(0\), accounting for the next \(e_0,a_0\). The final \(f,g\) again occur at index \(1\).

These calculations identify representatives of \(U,V\); they do not establish inequality in \(S_0/\theta\).

### 6.3 SEP — INCONCLUSIVE / UNPROVED

**Evidence:** S1 LF 368–374, 506 and 515.

No invariant or model separating \(U\) from \(V\) in the specified quotient is supplied. Distinct written ambient representatives do not establish distinct quotient elements.

The supplied left-zero map sends **both** to \((E,1)\), exactly as the author states. Its noninverseness argument cannot be repurposed as a proof of SEP.

Thus
\[
U\ne V\quad\text{in }S
\]
remains **UNPROVED**. This is a missing negative-certificate obligation, not a defect concealed by the partial status.

## 7. Least group congruence and actor rigidity

### 7.1 The claim \(\ker q=\sigma\) — SUPPORTED

**Evidence:** S1 LF 376; S2 LF 7.

Here use multiplicative group notation, with identity \(1\), and let \(S\) be any nonempty regular semigroup with a pure onto group homomorphism \(q\). Let \(\sigma\) be the congruence generated by identifying all idempotents.

Write \(\epsilon\) for their common class. Given \(s\in S\), choose a regular inverse \(s'\). Then
\[
[s][s']=[ss']=\epsilon,\qquad
[s'][s]=[s's]=\epsilon.
\]
Moreover
\[
\epsilon[s]=[ss's]=[s],\qquad
[s]\epsilon=[ss's]=[s].
\]
Thus \(S/\sigma\) is a group, with identity \(\epsilon\) and inverse \([s']\) for \([s]\).

Every homomorphism to a group identifies all idempotents. Hence \(\sigma\) is the least group congruence and
\[
\sigma\subseteq\ker q.
\]

For the reverse inclusion, suppose \(q(s)=q(t)\). The inverse equations imply \(q(s')=q(s)^{-1}\), so
\[
q(s't)=1.
\]
Purity makes \(s't\) idempotent. In \(S/\sigma\),
\[
[s]^{-1}[t]=[s'][t]=[s't]=\epsilon,
\]
and therefore \([s]=[t]\). This proves
\[
\boxed{\ker q=\sigma}.
\]

The proof needs neither commuting idempotents nor unique inverses. Applied to the present source, it gives \(a\,\sigma\,b\).

### 7.2 Transfer from an arbitrary group actor to the prescribed actor — SUPPORTED

**Evidence:** S2 LF 9; use in S1 LF 88.

Suppose \(j:S\hookrightarrow B\rtimes H\) is an embedding and let \(r:S\to H\) be its group projection.

An idempotent maps to the group identity. Conversely, if \(r(s)=1\), then \(j(s)=(b_s,1)\) is idempotent because \(B\) is a band; injectivity gives \(s^2=s\). Thus \(r\) is pure.

Regular inverse witnesses show that \(K=r(S)\) is a subgroup of \(H\). Both onto pure group maps \(q:S\to G\) and \(r:S\to K\) have kernel \(\sigma\), so
\[
\psi:G\longrightarrow K,\qquad \psi(q(s))=r(s)
\]
is a well-defined group isomorphism.

Restrict the original action to \(K\) and transport it through \(\psi\). Then
\[
s\longmapsto (b_s,q(s))
\]
is an embedding into a band semidirect product with exactly the prescribed actor \(G\).

This transfers the **source embedding**. It does not assert a homomorphism \(H\to G\) or an embedding of the entire original host into the new host.

## 8. Universal-band routing and the missing collision

### 8.1 The universal presentation and its consumer — SUPPORTED

**Evidence:** S1 LF 62–88, 393–409; S2 LF 15–25.

The presentation imposes square relations on **all nonempty words**, not just generators. Hence \(C_q\) is a band.

For general multiplicative \(G\), left translation of indices preserves each cocycle relation:
\[
(g,st)=(g,s)(gq(s),t)
\]
becomes
\[
(hg,st)=(hg,s)(hgq(s),t).
\]
It therefore gives genuine band automorphisms and a \(G\)-action.

With \(c_s=[(1,s)]\), the cocycle relation at index \(1\) gives
\[
c_{st}=c_s\,\alpha_{q(s)}(c_t),
\]
so \(\eta_q(s)=(c_s,q(s))\) is a homomorphism.

For any homomorphism \(s\mapsto(b_s,q(s))\) into \(B\rtimes G\), the assignment
\[
(g,s)\longmapsto \alpha_g(b_s)
\]
respects the source relation because
\[
\alpha_g(b_{st})
=\alpha_g(b_s)\,\alpha_{gq(s)}(b_t).
\]
It also respects every word-square relation because \(B\) is a band. Thus it descends to the required equivariant band homomorphism.

Consequently, equality of \(c_s,c_t\) together with equality of their \(q\)-values forces equality of their images in **every** host over \(q\). Conversely, injectivity of \(\eta_q\) itself supplies such a host. With the regular-source actor argument above, a genuine distinct same-\(q\) collision would obstruct every group actor.

The indices \(gq(s)\) are essential to this consumption of the defining relation.

### 8.2 The displayed expansions of \(c_U,c_V\) — SUPPORTED

**Evidence:** S1 LF 399–409.

For the additive \(C_2\) convention, let \(c_x=[(0,x)]\) and let \(\alpha\) be the nontrivial action. The accumulated source group coordinates give
\[
c_U=c_e\,c_a\,\alpha(c_f)\,\alpha(c_g)
\]
and
\[
c_V=
c_e\,c_b\,\alpha(c_f)\,\alpha(c_{a'})
\,c_e\,c_a\,\alpha(c_f)\,\alpha(c_g).
\]
In particular, the group coordinate returns to \(0\) after \(a'\) in the second expression, so the subsequent \(c_e,c_a\) are unshifted.

These are correctly typed expansions of source-element generators of \(C_q\). They are not an equality between the two products.

### 8.3 COLL — INCONCLUSIVE / UNPROVED

**Evidence:** S1 LF 384–416, 448–462, 507 and 517.

No finite defining-relation chain establishes
\[
(0,U)\equiv_q(0,V).
\]
The proposed chain format correctly requires contextual instances of word-square relations or the typed source cocycle relations. However, a certificate format is not a certificate.

Thus **COLL remains UNPROVED**. Nothing in the coordinate expansions, the left-zero image or the source regularity argument pays this obligation.

## 9. The external necessary condition and source reports

### 9.1 Conditional use of (N) — SUPPORTED only as a conditional reduction

**Evidence:** S1 LF 141–162 and 376–380.

The supplied source satisfies the algebraic premises written before (N):

- \(a\,\sigma\,b\), by the proved kernel equality;
- \(a'\in V(a)\) and \(b'\in V(b)\);
- \(e,f,g\in E(S)\);
- R1–R4, by the definition of \(\theta\).

Therefore, **if** the reported necessary condition is imported as a valid theorem for the stated embeddable regular-source class, it gives the conditional implication
\[
\mathrm{SEP}\Longrightarrow
\text{nonembedding into every band-by-group semidirect product}.
\]

Its theorem status is not established by those premise checks. The frozen packet reports the secondary-source statement but supplies neither its proof nor the missing primary separation proof. I did not follow the external links.

Accordingly:

- the premise verification is **SUPPORTED**;
- (N) as an independently verified external theorem is **INCONCLUSIVE in this review**;
- a self-contained all-host negative conclusion is **NOT PROVED**;
- (N) is not counted as a displayed universal-band relation chain.

### 9.2 Bibliographic and access reports — not independently reauthenticated

The author distinguishes bibliographic identification, secondary reports, partial source access and recovery of a complete original proof. The report expressly does **not** claim the latter.

I did not independently repeat the reported access attempts or authenticate the external documents. Their contents therefore remain source reports at their stated scope, not independent evidence generated by this review. Failed transport establishes neither mathematical truth nor mathematical falsehood.

No identification of this fresh source with either 1998 construction follows.

## 10. Finite universal-host bound

**Status: SUPPORTED. Evidence:** S1 LF 466–485.

For finite \(S,G\), the universal alphabet has
\[
k=|G||S|
\]
letters. The band \(C_q\) is a quotient of the free band on those letters, so the established representative-length argument yields
\[
|C_q|\le \sum_{j=1}^{2^{k+1}-2}k^j.
\]
Consequently
\[
|C_q\rtimes G|
\le |G|\sum_{j=1}^{2^{k+1}-2}k^j.
\]

If a host embeds \(S\) over \(q\), the universal criterion makes \(\eta_q\) injective, and this finite canonical host embeds it. For the present regular source, actor rigidity also explains why an embedding with another group actor would reduce to the prescribed actor.

This is an existence and size bound. It does not assert efficient construction, completed congruence computation, measured runtime, or feasibility within a bounded finite-check allowance. No such computation was performed.

## 11. Claim-by-claim disposition

| Claim | Disposition |
|---|---|
| \(S_0\) is mathematically specified, finite and associative | **SUPPORTED**, at the declared elementary-band-theory import boundary |
| Reverse-star witnesses prove regularity inside \(S_0\) | **SUPPORTED** |
| \(q_0^{-1}(0)=E(S_0)\) | **SUPPORTED** |
| \(\theta\) is the specified congruence on \(S_0\), with \(\theta\subseteq\ker q_0\) | **SUPPORTED** |
| \(S=S_0/\theta\) is finite, regular, orthodox and pure onto \(C_2\) | **SUPPORTED** |
| The supplied left-zero map factors through \(S\) and proves noninverseness | **SUPPORTED** |
| That left-zero map separates \(U,V\) | **REFUTED as an inference**; both images are \((E,1)\), and the author expressly does not make that claim |
| R1–R4 and \(U,V\) have the stated twisted coordinates | **SUPPORTED** |
| \(q(U)=q(V)=1\) in additive \(C_2\) notation | **SUPPORTED** |
| Every regular pure onto group quotient has kernel equal to the least group congruence | **SUPPORTED**, by the full general proof above |
| The universal construction has the stated action, homomorphism and all-host factorization | **SUPPORTED** |
| The displayed \(c_U,c_V\) expansions have correctly routed indices | **SUPPORTED** |
| SEP: \(U\ne V\) in the actual quotient | **INCONCLUSIVE / UNPROVED** |
| COLL: a finite universal-band derivation equates their generators | **INCONCLUSIVE / UNPROVED** |
| The source satisfies the written premises of reported (N) | **SUPPORTED** |
| Reported (N) is independently established by this review | **INCONCLUSIVE; external import not proved here** |
| The finite universal-host bound | **SUPPORTED**, not a computational result |
| This source is an established all-host nonembedding witness | **NOT PROVED** |
| Complete recovery/authentication of either 1998 construction and proof | **NOT ESTABLISHED** |

The refuted left-zero inference is not an author defect: the author explicitly warns against it in S1 LF 374. No mathematical finding is raised on that basis.

## 12. Final verdict

**Overall correctness: correct at the declared partial written scope.**

The frozen candidate consistently separates established source properties from its two unpaid certificate obligations. The written reconstruction supports the finite regular pure-\(C_2\), genuinely noninverse source, the exact quotient semantics and coordinate routing, the least-group-congruence equality, the universal criterion and the finite-host bound. No FATAL, MAJOR or MINOR defect was identified within that scope.

**SEP and COLL both remain UNPROVED.** There is no completed all-host negative witness and no basis here for promoting the candidate to one. The secondary condition (N), the historical source reports and earlier finite-run statements receive no unearned proof or execution credit.

This is one same-harness written review. It is not parent adoption, independent-family review, human review, kernel verification, novelty certification or authorization to consume held material.

**Confidence:** 0.97 for the stated partial-scope assessment.