# F595 — Fresh original-input written review of the finite regular pure-\(C_2\) source

**Disposition: SUPPORTED at the explicitly partial source-construction scope. The finite all-host negative witness remains NOT PROVED.**

**Findings:** 0 FATAL / 0 MAJOR / 0 MINOR. The expressly unpaid SEP and COLL obligations are not counted as defects or silently treated as established.

This is the complete review body for Main to materialize. No working-tree review file was written under this read-only role.

## 1. Input, read order and exclusions

Before reading the mathematical packet, I read the manifest and freeze receipt through their endings, every listed status-only control through its ending, and both parent metadata/dispatch records through their endings. I then sent a direct administrative pre-body ACK to `agent://Main`.

Only afterward did I read the entire literal packet, in consecutive raw windows of at most 20 lines, through its ending at packet LF 564. This included all of S1 through LF 521 and all of S2 through LF 41. Mathematical reconstruction began after that complete read.

The bindings below are **parent-supplied metadata**, not child-recomputed hashes:

- Manifest: `af0189ba086fcc95da340a0d6d87722c19ad94408b241e015fcc4a548d24fce2`.
- Freeze receipt: `af7a871a15bd0f42f4d999c8496ff598e10b57527a07045a22edc54e66974ea3`.
- Literal packet: `785f011b9559ffb878d1e668129a3236699348a189077623b208b5eba939954f`.
- S1, original F492 candidate: `7cc82e10967198b7a28f44fb314ead28108c60d556c76766f40dad1d225ad3f9`.
- S2, adopted actor-rigidity/universal-band disposition: `62babb5bd3bfccd57154373d1df082388747602f1f421b84310679ec8b3e80e4`.

The entire F586 episode and every held proof, method, selection, planning, verification, reporting and confidence consumer were NONINPUT. I did not open their bodies or histories, follow excluded references, or salvage mathematical fragments from them.

**Scientific execution: NOTRUN.** No scientific code, CAS, interpreter, solver, enumeration, replay, build, test, linter, formatter, new selected instance or private probe was used. No public-source link was followed. The reconstruction below uses general quantified arguments and the literal objects already specified in S1/S2. This is an access/use account, not a cognitive-isolation certificate.

## 2. Claim-by-claim disposition

| Claim | Status | Evidence and boundary |
|---|---|---|
| Local finiteness and the representative-length bound for free bands | **SUPPORTED at the named classical import** | S1 LF 176–204. Imports the band \(\mathcal D\)-semilattice/rectangular-class theorem; the ensuing deduction is reconstructed below. |
| The ten-letter ambient band, involution and multiplication specify a finite associative semigroup | **SUPPORTED** | S1 LF 206–242. |
| The generated subsemigroup \(S_0\) is regular, with inverses inside \(S_0\) | **SUPPORTED** | S1 LF 244–270. The wordwise star retains the actual \(C_2\) twist. |
| The four-relation quotient \(S=S_0/\theta\) is finite, regular and idempotent-pure over \(C_2\) | **SUPPORTED** | S1 LF 272–306. The congruence is on \(S_0\), not on the whole ambient host. |
| The quotient is genuinely noninverse | **SUPPORTED** | S1 LF 308–333. The displayed left-zero map separates \(ef\) and \(fe\). |
| The displayed source words, group values and twisted coordinate expansions are correct | **SUPPORTED** | S1 LF 339–366 and 399–409. |
| Equal prescribed-group values imply equality in the least group quotient | **SUPPORTED** | S1 LF 376; S2 LF 7–9. |
| The universal presentation and its evaluation maps detect every embedding over \(q\) | **SUPPORTED** | S1 LF 62–88; S2 LF 15–25. |
| The universal construction has the displayed finite-host bound | **SUPPORTED at the same band-theory import** | S1 LF 466–485. |
| The externally reported quasiidentity (N) is an authenticated theorem | **INCONCLUSIVE in this review** | S1 LF 139–162. The external source was not followed; its theorem status is not independently certified here. |
| \(U\ne V\) after quotienting by \(\theta\) — SEP | **INCONCLUSIVE / UNPROVED** | Expressly unpaid at S1 LF 368–380 and 506–517. |
| A finite typed universal-band chain proves COLL | **INCONCLUSIVE / UNPROVED** | Expressly unpaid at S1 LF 384–416 and 506–517. |
| This candidate is a finite all-host nonembedding witness | **NOT PROVED** | Both source separation and the required collision certificate remain absent. |

No mathematical claim was refuted in the reviewed partial construction.

## 3. Band-theory import and the finite bound

**Evidence:** S1 LF 176–204.

The precise imported classical fact is:

> In every band, Green’s \(\mathcal D\) is a semilattice congruence, and each \(\mathcal D\)-class is a rectangular band.

This review does not supply a new proof or external authentication of that theorem. Its use is not restricted to commutative bands.

Let \(w\) be any nonempty word with \(k\) distinct letters. Its shortest full-content prefix and suffix have the displayed forms
\[
p=s\sigma,\qquad r=\varepsilon t.
\]
The contents of \(s\) and \(t\) each have \(k-1\) letters.

Because the \(\mathcal D\)-quotient is a semilattice, the evaluations of \(p,w,r\) have the same image there. They therefore belong to one rectangular \(\mathcal D\)-class. Prefix and suffix factorization, together with idempotence, give
\[
pw=w,\qquad wr=w.
\]
Consequently,
\[
w=pwr=pr=s\sigma\varepsilon t.
\]

The rectangular-band identity is applied to \(p,w,r\), which have already been shown to lie in the same class. It is not applied indiscriminately to factors of different contents.

Recursively replacing \(s\) and \(t\) gives
\[
L_0=0,\qquad L_k=2L_{k-1}+2=2^{k+1}-2.
\]
Empty \(s\) or \(t\) is harmless: it means omission of a factor in the word concatenation, not insertion of an identity element into the semigroup. Thus the argument does not silently pass from the free band semigroup to a free band monoid.

Every element of the free band on \(k\) letters has a nonempty representative of length at most \(L_k\), whence
\[
|F_k|\le \sum_{j=1}^{L_k}k^j.
\]
The bound is crude but valid at the stated import boundary.

## 4. Ambient construction and regularity inside \(S_0\)

**Evidence:** S1 LF 206–270.

The alphabet is exactly
\[
\{a_0,a_1,b_0,b_1,e_0,e_1,f_0,f_1,g_0,g_1\}.
\]
The subscript exchange extends to an automorphism \(\tau\) of the free band \(F\), with \(\tau^2=1\). Hence
\[
(u,h)(v,k)=\bigl(u\tau^h(v),h+k\bigr)
\]
is associative. The generated \(S_0\) is finite, with
\[
|S_0|\le 2|F|
\le 2\sum_{j=1}^{2046}10^j.
\]

The regularity argument genuinely supplies inverses **inside the generated subsemigroup**. It does not infer that an arbitrary subsemigroup of a regular host is regular.

For a general generator word \(W=x_1\cdots x_n\), write the generator coordinates as \((\ell_i,h_i)\). Its natural first-coordinate word is
\[
w=\ell_1\,\tau^{h_1}(\ell_2)\cdots
\tau^{h_1+\cdots+h_{n-1}}(\ell_n),
\qquad h=h_1+\cdots+h_n.
\]
For every displayed generator, the named star has coordinates
\[
x_i^*=\bigl(\tau^{h_i}(\ell_i),h_i\bigr).
\]
Expanding the reversed starred generator word therefore yields
\[
W^*=\bigl(\tau^h(\operatorname{rev}w),h\bigr).
\]
The suffix parity in the expansion of \(W^*\) equals the total parity plus the corresponding prefix parity in \(W\), because the actor is \(C_2\).

Reversal also respects the free-band relations: reversing a word-square relation gives another word-square relation. Thus use of \(\operatorname{rev}w\) is compatible with the band quotient.

The evaluations of \(w\) and \(\operatorname{rev}w\) have identical content and lie in the same rectangular \(\mathcal D\)-class. Therefore
\[
w\,\operatorname{rev}w\,w=w,\qquad
\operatorname{rev}w\,w\,\operatorname{rev}w=\operatorname{rev}w.
\]
Consuming the actual twist in the ambient multiplication gives
\[
WW^*W=W,\qquad W^*WW^*=W^*.
\]
Since \(W^*\) remains a word in the seven allowed generators, these are inverse witnesses in \(S_0\). No well-defined unary star operation on quotient elements is needed for this existential regularity proof.

The second projection is onto \(C_2\). Every element of parity zero is idempotent, while an element of parity one cannot be idempotent because squaring changes its group coordinate to zero. Hence
\[
q_0^{-1}(0)=E(S_0).
\]

## 5. The four-relation quotient and its consumers

**Evidence:** S1 LF 272–333.

Each side of each defining pair has parity zero. Thus every generating pair for \(\theta\) belongs to \(\ker q_0\), and minimality of the generated semigroup congruence gives
\[
\theta\subseteq\ker q_0.
\]
The group projection consequently descends to an onto map
\[
q:S_0/\theta\longrightarrow C_2.
\]

Associativity and regularity pass through the quotient. If \(q([x])=0\), then \(q_0(x)=0\), so \(x\) itself is idempotent and therefore so is \([x]\). Conversely, an idempotent class has idempotent group image, necessarily zero. Consequently
\[
q^{-1}(0)=E(S).
\]
The idempotents form a subsemigroup because their \(q\)-values are zero, so the quotient is orthodox.

This reasoning uses **the congruence generated on \(S_0\)**. It neither replaces \(\theta\) by an ambient band congruence nor permits substitution in contexts that are not available in \(S_0\).

The noninverse witness also survives the quotient. The displayed map from the ten letters to the two-element left-zero band is \(\tau\)-invariant. It therefore defines a homomorphism
\[
F\rtimes C_2\longrightarrow L\times C_2.
\]
Under this homomorphism:

- R1 and R2 have first coordinate \(E\) on both sides.
- R3 and R4 have first coordinate \(F\) on both sides.
- Every side has group coordinate zero.

The restriction to \(S_0\) therefore annihilates \(\theta\), so it factors through \(S\). The literal elements \(ef\) and \(fe\) have different images,
\[
(E,0)\ne(F,0).
\]
Thus the idempotents of \(S\) do not commute, and the regular semigroup \(S\) is not inverse.

This proves only the claimed noninverseness. The same map sends both \(U\) and \(V\) to \((E,1)\), so it is not a separation certificate for the target pair.

## 6. Literal coordinate and typing reconstruction

**Evidence:** S1 LF 339–374 and 393–409.

The displayed pair is
\[
U=eafg,\qquad V=ebfa'eafg.
\]
Their group values are both one.

Successive use of the accumulated parity gives exactly
\[
U:\quad e_0a_0f_1g_1,
\]
and
\[
V:\quad e_0b_0f_1a_0e_0a_0f_1g_1.
\]

The four relation pairs likewise have the stated ambient first coordinates:
\[
e_0a_0=e_0,\qquad e_0b_0=e_0,
\]
\[
a_1f_0g_0=f_0g_0,
\]
and
\[
b_1f_0a_1e_1a_1f_0g_0
=
f_0a_1e_1a_1f_0g_0.
\]
In the last pair, the occurrence of \(e_1\), rather than \(e_0\), is required by the parity accumulated before consuming \(e\). These calculations agree with the stated semidirect multiplication, rather than a direct-product substitution.

At the universal-band boundary, the receiving relation is
\[
(g,st)=(g,s)(g+q(s),t).
\]
It retains the same accumulated group index. Accordingly,
\[
c_U=c_e c_a\alpha(c_f)\alpha(c_g),
\]
and
\[
c_V=c_e c_b\alpha(c_f)\alpha(c_{a'})
c_e c_a\alpha(c_f)\alpha(c_g)
\]
are correct.

These expansions establish the two individually typed expressions. They do **not** establish their equality. No unshifted or untyped replacement is justified by these formulas.

## 7. Universal evaluation, actor rigidity and the finite host

**Evidence:** S1 LF 62–88, 376 and 466–485; S2 LF 7–25.

All nonempty word-square relations make \(C_q\) a band. Left translation of every group index preserves both the square relations and the cocycle relations, hence defines the stated group action.

For an embedding over \(q\), write
\[
H(s)=(b_s,q(s)).
\]
Its homomorphism law says
\[
b_{st}=b_s\bigl(q(s)\cdot b_t\bigr).
\]
The proposed evaluation
\[
(g,s)\longmapsto g\cdot b_s
\]
therefore sends the two sides of a cocycle relation to the same value:
\[
g\cdot b_{st}
=
(g\cdot b_s)\bigl((gq(s))\cdot b_t\bigr).
\]
It also respects every word-square relation because its target is a band. Thus it descends to the required equivariant band homomorphism. This is the consuming-side verification needed for the all-host criterion.

Consequently, a collision between distinct same-\(q\) source generators defeats every embedding over \(q\). Conversely, when no such collision occurs, the canonical \(\eta_q\) is injective and supplies a host itself.

For the regular-source actor change, let \(\sigma\) identify all idempotents. Regular inverses make \(S/\sigma\) a group, and every group homomorphism identifies the source idempotents. Thus \(\sigma\) is the least group congruence. If \(q(s)=q(t)\), an inverse \(s'\) satisfies \(q(s't)=0\), so purity makes \(s't\) idempotent. In \(S/\sigma\),
\[
[s'] [t]=1=[s'] [s],
\]
which implies \([s]=[t]\). Therefore \(\ker q=\sigma\).

For an arbitrary embedding into \(B\rtimes H\), the induced actor map is pure: an element whose actor coordinate is the identity has an idempotent image, and injectivity then makes the source element idempotent. Regularity makes the actor image a subgroup. Its kernel is the same \(\sigma\), so this subgroup is isomorphic to the prescribed \(G\), and its restricted action transports to an embedding over the literal \(q\).

This does not require a map from all of \(H\) to \(G\), nor an extension to the entire original host.

Finally, for finite \(S,G\), the universal alphabet has \(k=|G||S|\) letters. The already reconstructed free-band bound yields
\[
|C_q|\le\sum_{j=1}^{2^{k+1}-2}k^j
\]
and hence
\[
|C_q\rtimes G|
\le |G|\sum_{j=1}^{2^{k+1}-2}k^j.
\]
If any host embeds \(S\) over \(q\), the universal criterion makes this canonical finite host an embedding host. This is an existence bound, not an exercised enumeration, a feasible computational proposal or a completed congruence calculation.

## 8. External theorem and exact residual

**Evidence:** S1 LF 139–168, 368–416 and 504–521.

The theorem labelled (N) is present only as the author’s report of an external dissertation passage. This review did not authenticate that passage, its translation, its hypotheses or its attribution. The bibliography and historical access outcomes likewise remain author-reported, not independently re-exercised observations.

The conditional reduction is nevertheless correctly stated: the constructed source has the displayed regular inverse pairs and four source relations, and \(a\,\sigma\,b\) follows from their equal \(q\)-values. **If** the reported necessary condition (N) is imported as a valid theorem, then SEP would contradict that necessary condition and exclude an embedding. This conditional implication does not discharge either the external theorem import or the assignment’s displayed-chain requirement.

The remaining obligations are exactly:

1. **SEP:** establish \(U\ne V\) in the particular quotient \(S_0/\theta\). Different ambient expressions do not suffice, and the existing left-zero map does not separate them.
2. **COLL:** supply the finite contextual derivation
   \[
   (0,U)\equiv_q(0,V),
   \]
   retaining the group indices at every cocycle replacement and allowing square relations for arbitrary nonempty words.
3. Combine that source separation and checked chain to obtain the requested all-host negative certificate.

Neither obligation is supplied by the present packet. The source does not disguise this gap: its opening, collision discussion and final disposition all explicitly withhold the all-host witness.

## 9. Final verdict and scope

**Overall correctness: correct.** The finite associative regular noninverse source, its pure onto \(C_2\)-quotient, the literal twisted coordinates and the universal finite-host bound are supported by the written reconstruction at the explicitly named classical band-theory import. SEP, COLL and the finite all-host negative witness remain unproved; the review does not upgrade them through the secondary-source theorem or historical review labels.

**Written-review confidence: 0.96**, limited to that partial scope.

No novelty, original-source authentication, independent-family, human, kernel, numerical-execution or automatic-adoption credit is claimed.