# author-candidate-v1.md

## F492 — Finite regular pure-group sources: explicit candidate construction and exact collision frontier

**Status: AUTHOR_WRITTEN_PARTIAL / NEGATIVE WITNESS NOT ESTABLISHED.**

This return supplies:

1. A completely specified finite, regular, noninverse semigroup with a prescribed pure quotient onto \(C_2\), defined by an explicit multiplication construction and four quotient relations.
2. An exact pair of same-quotient elements whose separation would be relevant to the recovered nonembedding condition.
3. A finite certificate format for the required collision in the universal band presentation.
4. A finite-host bound for the universal construction.
5. Public-source findings that go beyond the original survey citation, while explicitly stopping short of recovering the complete 1998 proof.

**Neither separation of the proposed source elements nor their collision in the universal band has been proved here. Consequently, no all-host nonembedding witness is claimed.** The construction below is a candidate for the assigned negative direction, not a replacement positive theorem counted as solving that direction.

No working-tree artifact was written. This is the complete body for Main to materialize.

---

## 1. Input and execution chronology

Before opening the scientific packet, I completely read:

- `manifest-v1.json`, LF 1–117;
- `freeze-receipt-v1.json`, LF 1–60;
- all ten specified permission/status controls through their endings.

Those complete reads used raw ranges of at most 20 LF. Earlier nonraw manifest, receipt and parent-metadata reads preceded the complete raw reads; no scientific packet body had been opened at that point.

I then sent a direct prebodyACK to Main. Only afterward did I read the entire ordered `literal-packet-v1.md`, LF 1–81, in consecutive raw ranges of at most 20 LF, including the ending of S3.

The supplied pins are:

- Manifest: `dbca358a8de9aecdcbb8b89186acd31c8d6074422b28e6ab5a909f72a39549ce`
- Receipt: `f1868ba404c5fabadf20c2f5c37027dfe5475061bb38e6809c84e7cc0adb6050`
- Packet: `9fe75e7d72430f5f9bc886be07ee387bf97af36b6616357dd4a247576c22196b`

These are **parent-supplied observations**, corroborated by the supplied metadata record, not child-recomputed hashes. The parent’s clock is not a child-native start or execution timestamp.

After the packet read, I undertook public-source reading and fresh written algebra. The fresh construction in §4 was developed after encountering the four-premise necessary condition in Hartmann’s dissertation. It is therefore **source-informed, not independently blind**, and is not identified with the original Szendrei construction.

All held episodes and their consumers remained NONINPUT. References appearing inside the permitted packet were not followed into held scientific payloads. This is an access/use account, not a cognitive-isolation certificate.

**Scientific execution: NOTRUN.** The runtime’s read-only shell restriction was not bypassed. No scientific program, solver, build, test, formatter, installation, external-model CLI or mutation was run. All derivations below are written exact algebra; no measured computational output is asserted.

---

## 2. The original target and its precise certificate

Let \(S\) be a nonempty regular semigroup and let
\[
q:S\twoheadrightarrow G
\]
be a prescribed group homomorphism satisfying
\[
q^{-1}(1)=E(S).
\]

The assigned negative direction asks for an explicit finite such source and an obstruction to **every** embedding into a semidirect product of a band by a group—not just failure in one chosen host.

Use the adopted universal band
\[
C_q=
\left\langle
(g,s)\ (g\in G,\ s\in S)
\ \middle|\
ww=w,\quad
(g,st)=(g,s)(gq(s),t)
\right\rangle_{\mathrm{semigroup}},
\]
where the square relations range over **every nonempty word**, not merely individual generators.

Translation of the group index defines a \(G\)-action. Writing \(c_s=[(1,s)]\), the canonical homomorphism is
\[
\eta_q(s)=(c_s,q(s))\in C_q\rtimes G.
\]

The exact target certificate is:

- distinct \(s,t\in S\);
- \(q(s)=q(t)\);
- a finite defining-relation derivation
  \[
  (1,s)\equiv_q(1,t).
  \]

Such a derivation defeats every embedding over the prescribed \(q\), by the universal evaluation map. The adopted regular-source actor-rigidity result then defeats every group actor, not only \(G\).

**No such completed certificate is supplied in this return.**

---

## 3. What the public-source search actually recovered

### 3.1 Billhardt’s original article: identifier recovered, full proof not recovered

The original article is:

Bernd Billhardt, *On Embeddability into a Semidirect Product of a Band by a Group*, **Journal of Algebra 206** (1998), 40–50, DOI [10.1006/jabr.1997.7390](https://doi.org/10.1006/jabr.1997.7390).

The following were accessible:

- [Crossref metadata](https://api.crossref.org/works/10.1006/jabr.1997.7390);
- [OpenAlex record](https://api.openalex.org/works/W1967329499);
- [zbMATH review](https://zbmath.org/0920.20048);
- [MaRDI reproduction of the review](https://portal.mardi4nfdi.de/wiki/On_embeddability_into_a_semidirect_product_of_a_band_by_a_group).

The review reports a negative solution and a canonical algebraic embedding construction. It is a review, not the original proof.

Actual full-text access outcomes:

- ScienceDirect article and PDF routes: HTTP 403.
- Publisher XML route: metadata only, without the mathematical article body.
- Publisher FULL view: HTTP 401.
- Publisher PDF API request: HTTP 406.
- OpenAlex content PDF: HTTP 401.
- Publisher linking resolver: redirect-only text.
- Semantic Scholar API attempts: reader extraction rejected the URL format; no article text obtained.

Thus an index’s “open access” or “has fulltext” flag was **not** treated as successful proof access.

### 3.2 A specific finite Szendrei article is authenticated bibliographically

Szendrei’s own [publication list, item 37](https://www.math.u-szeged.hu/tagok/bszendre/papers.html) identifies:

Mária B. Szendrei, *A finite non-embeddable E-unitary regular semigroup*, in *Semigroups and Applications* (St Andrews, 1997), World Scientific, Singapore, 1998, pp. 202–214.

This confirms a specific finite-construction article, distinct from Billhardt’s journal article. The publication-list entry does **not** provide its proof.

The existing survey attributes a finite example to Billhardt; the dissertation discussed next explicitly attributes a finite graph-semigroup construction to Szendrei. These are not grounds for silently identifying the two constructions or transferring one article’s proof to the other.

### 3.3 Hartmann’s dissertation contains a concrete mathematical lead

I accessed the full publicly served dissertation PDF:

Miklós Hartmann, *Ortodox félcsoportok és szemidirekt szorzatok*, Szeged, 2007, [repository record](https://doktori.bibl.u-szeged.hu/id/eprint/1183/) and [PDF](https://doktori.bibl.u-szeged.hu/id/eprint/1183/1/HM_dissz.pdf).

The relevant extracted passage is PDF page 20, numbered mathematical page 18, Theorem 3.4 and Statements 3.5–3.6. I read the relevant passage and its surrounding construction; I did not read the entire dissertation through its ending.

Theorem 3.4, attributed there to Billhardt, reports the following necessary condition for an embeddable E-unitary regular semigroup. With
\[
a\,\sigma\,b,\quad a'\in V(a),\quad b'\in V(b),\quad e,f,g\in E(S),
\]
assume
\[
eaa'=e,\qquad ebb'=e,
\]
\[
a'afg=fg,\qquad
b'bfa'eafg=fa'eafg.
\]
Then
\[
eafg=ebfa'eafg. \tag{N}
\]

The dissertation next specifies a \(C_2\)-based graph construction and attributes the needed inequivalence of two paths to Szendrei’s 1998 article. Crucially, that load-bearing inequivalence is **stated**, not proved in the passage. Later arguments use that statement rather than supplying its missing proof.

The extracted graph-presentation line is typographically damaged. I therefore do not offer an OCR reconstruction of it as an exact authenticated original presentation.

This is a substantive improvement in the source frontier: a definite seven-element configuration and four exact algebraic premises are now available. It is **not** recovery of the complete primary countercertificate.

### 3.4 A separate accessible paper is not a nonembedding proof

Hartmann and Szendrei’s [*E-unitary almost factorizable orthodox semigroups*](https://www.math.u-szeged.hu/~bszendre/e-un_fact.pdf) was also accessible. Its counterexample concerns failure to be **isomorphic to a whole semidirect product**. That is not failure to embed into an arbitrary larger semidirect product.

I do not use that counterexample as evidence for the assigned all-host negative claim.

---

## 4. A fresh, completely specified finite regular pure-\(C_2\) source

The following construction is fresh written work informed by the configuration above. **Its source properties are proved below; its nonembeddability is not.**

### 4.1 Band background and an explicit finiteness bound

Use the elementary band-decomposition fact:

> In a band, Green’s \(\mathcal D\) is a semilattice congruence, and each \(\mathcal D\)-class is a rectangular band.

This is standard band theory, not a novelty claim. In particular, evaluations of words with the same set of letters are \(\mathcal D\)-related, and in one rectangular class \(xyz=xz\).

For completeness, the needed local-finiteness deduction is short. Given a nonempty word \(w\) with \(k\) distinct letters, let:

- \(p=s\sigma\) be its shortest prefix containing all \(k\) letters;
- \(r=\varepsilon t\) be its shortest suffix containing all \(k\) letters.

The words \(s,t\) each omit one of those letters. In any band, the evaluations of \(p,w,r\) lie in the same rectangular \(\mathcal D\)-class. Also \(pw=w\) and \(wr=w\), since \(p\) is a prefix and \(r\) a suffix. Consequently
\[
w=pwr=pr=s\sigma\varepsilon t.
\]

Recursing yields a representative-length bound
\[
L_0=0,\qquad L_k=2L_{k-1}+2=2^{k+1}-2.
\]

Therefore the free band on \(k\) letters is finite, with the deliberately crude bound
\[
|F_k|\le \sum_{j=1}^{L_k}k^j.
\]

This deduction uses the stated elementary band-decomposition fact as its import boundary; it is not presented as a new proof of that classical fact.

### 4.2 Alphabet, involution and ambient multiplication

Let
\[
\mathcal A=
\{a_0,a_1,b_0,b_1,e_0,e_1,f_0,f_1,g_0,g_1\},
\]
and let \(F\) be the free band on \(\mathcal A\).

Let \(\tau\) exchange subscripts 0 and 1. It induces an automorphism of \(F\) with \(\tau^2=1\).

Take the ambient semidirect product
\[
F\rtimes C_2,\qquad
(u,h)(v,k)=\bigl(u\,\tau^h(v),h+k\bigr),
\]
with group coordinates added modulo 2.

Let \(S_0\) be the subsemigroup generated by
\[
a=(a_0,1),\quad a'=(a_1,1),\quad
b=(b_0,1),\quad b'=(b_1,1),
\]
\[
e=(e_0,0),\quad f=(f_0,0),\quad g=(g_0,0).
\]

This completely specifies its multiplication. It is finite: \(L_{10}=2046\), so
\[
|S_0|\le 2|F|
\le 2\sum_{j=1}^{2046}10^j.
\]
This is a mathematical bound, not a feasible 55-second enumeration proposal.

### 4.3 Associativity, regularity and purity of \(S_0\)

Associativity follows from the displayed semidirect-product multiplication.

Define a star on generator names by exchanging \(a,a'\), exchanging \(b,b'\), and fixing \(e,f,g\). For a generator word \(W=x_1\cdots x_n\), put
\[
W^*=x_n^*\cdots x_1^*.
\]

If \(W\) evaluates to \((u,h)\), and \(u\) is represented by the band word \(w\), then direct expansion of the multiplication gives
\[
W^*=\bigl(\tau^h(\operatorname{rev}w),h\bigr).
\]

The evaluations of \(w\) and \(\operatorname{rev}w\) have the same content, hence lie in one rectangular \(\mathcal D\)-class. Thus
\[
w\,\operatorname{rev}w\,w=w,\qquad
\operatorname{rev}w\,w\,\operatorname{rev}w=\operatorname{rev}w.
\]
It follows that
\[
WW^*W=W,\qquad W^*WW^*=W^*.
\]
Because \(W^*\) is again a generator word, this proves regularity inside \(S_0\), not merely in the larger host.

The second projection \(q_0:S_0\to C_2\) is onto. Every element above 0 is idempotent because its first coordinate belongs to a band. No element above 1 can be idempotent, since an idempotent’s group coordinate must be 0. Therefore
\[
q_0^{-1}(0)=E(S_0).
\]

In particular \(a'\in V(a)\), \(b'\in V(b)\), and \(e,f,g\) are idempotent.

### 4.4 Impose exactly the four source relations

Let \(\theta\) be the least **semigroup congruence on \(S_0\)** containing
\[
eaa'=e,\qquad ebb'=e, \tag{R1–R2}
\]
\[
a'afg=fg, \tag{R3}
\]
\[
b'bfa'eafg=fa'eafg. \tag{R4}
\]

Define
\[
S=S_0/\theta.
\]

Each defining pair has group coordinate 0, so
\[
\theta\subseteq\ker q_0.
\]
Consequently \(q_0\) induces an onto homomorphism
\[
q:S\to C_2.
\]

The quotient is associative and regular. If \(q(x\theta)=0\), then \(q_0(x)=0\), hence \(x^2=x\), so \(x\theta\) is idempotent. The converse follows from its group image. Thus
\[
q^{-1}(0)=E(S).
\]

This proves that \(S\) is a finite regular orthodox semigroup with the required pure onto group quotient.

**Important boundary:** \(\theta\) is a congruence on \(S_0\). It is not defined by closing the four relations arbitrarily in the whole ambient band or ambient semidirect product. Replacing it by that larger closure would change the candidate.

### 4.5 The quotient remains genuinely noninverse

Let \(L=\{E,F\}\) be the two-element left-zero band, \(xy=x\), with trivial \(C_2\)-action.

Map \(e_0,e_1\) to \(E\), and every other letter of \(\mathcal A\) to \(F\). This band homomorphism is \(\tau\)-invariant, so it induces a homomorphism
\[
F\rtimes C_2\longrightarrow L\times C_2.
\]

On the seven generators its values are
\[
e\mapsto(E,0),\qquad f,g\mapsto(F,0),
\]
\[
a,a',b,b'\mapsto(F,1).
\]

All four relations hold under this map: the first two have first coordinate \(E\) on both sides, and the last two have first coordinate \(F\) on both sides; all have group coordinate 0. Hence the map factors through \(S\).

But
\[
ef\mapsto(E,0),\qquad fe\mapsto(F,0).
\]
Therefore \(ef\ne fe\) in \(S\). Its idempotents do not commute, so \(S\) is not inverse.

This also checks that the quotient construction has not merely collapsed to an inverse-source positive class.

---

## 5. The exact unresolved same-\(q\) pair

In \(S\), define
\[
U=eafg,\qquad V=ebfa'eafg.
\]
Both have \(q\)-value 1.

Before taking the quotient, their ambient first coordinates are
\[
U:\quad e_0a_0f_1g_1,
\]
\[
V:\quad e_0b_0f_1a_0e_0a_0f_1g_1.
\]

For comparison, the four defining source pairs have ambient first coordinates
\[
e_0a_0=e_0,\qquad e_0b_0=e_0,
\]
\[
a_1f_0g_0=f_0g_0,
\]
\[
b_1f_0a_1e_1a_1f_0g_0
=
f_0a_1e_1a_1f_0g_0.
\]

These coordinates are obtained by the actual consuming twist \(\tau^h\), not by treating the source as a direct product.

The required separation is
\[
U\ne V\quad\text{in }S_0/\theta. \tag{SEP}
\]
**SEP is unproved.** Different ambient words before imposing \(\theta\) do not prove it.

The left-zero quotient used above does not separate this pair: both map to \((E,1)\). It proves noninverseness, not nonembedding.

For connection to the reported condition (N), \(a\,\sigma\,b\) does hold. Indeed, for any regular pure group quotient, \(\ker q=\sigma\): after all idempotents are identified, regular inverses make the quotient a group; if \(q(s)=q(t)\), then for an inverse \(s'\), the product \(s't\) is idempotent, forcing \([s]^{-1}[t]=1\). Thus equal \(q\)-values give equal least-group-quotient values.

Accordingly, all premises of the reported condition (N) hold in this candidate. **If (N) is imported as a theorem**, SEP would imply nonembedding into every band-by-group semidirect product.

That is a conditional reduction only. Neither SEP nor an independent proof of (N) is supplied here.

---

## 6. The missing universal-band derivation, stated explicitly

For the candidate just defined, the desired universal-band relation is
\[
(0,U)\equiv_q(0,V)\quad\text{in }C_q. \tag{COLL}
\]

Here the identity of \(C_2\) is written additively as 0.

The source relations must be consumed through
\[
(g,st)=(g,s)(g+q(s),t).
\]
One cannot remove the shifted indices or apply a source relation at an arbitrary untyped position.

For example, writing \(c_x=[(0,x)]\) and letting \(\alpha\) denote the nontrivial \(C_2\)-action, the source products expand as
\[
c_U=c_e\,c_a\,\alpha(c_f)\,\alpha(c_g),
\]
\[
c_V=
c_e\,c_b\,\alpha(c_f)\,\alpha(c_{a'})
\,c_e\,c_a\,\alpha(c_f)\,\alpha(c_g).
\]

These expansions are valid identities in the universal band, but **their equality has not been derived**.

A successful negative certificate for this candidate therefore still needs both:

1. SEP in the finite source quotient;
2. a finite chain proving COLL, using only the universal defining relations.

The dissertation’s reported necessary condition supplies a focused lead for the second obligation. It is not a substitute for displaying the chain required by this assignment.

---

## 7. Exact finite certificate format

A checkable completed certificate should contain the following finite data.

### Source data

- A finite carrier and complete multiplication table.
- A finite group table, identity and inverses.
- The complete map \(q\).
- For every \(s\), an inverse witness \(s'\).
- Distinct named elements \(U,V\) with \(q(U)=q(V)\).

The checks are:

\[
(st)u=s(tu)\quad\text{for every source triple},
\]
\[
q(st)=q(s)q(t)\quad\text{for every source pair},
\]
\[
ss's=s,\qquad s'ss'=s',
\]
\[
q(s)=1\iff s^2=s,
\]
and surjectivity.

### Relation-chain data

A finite list of words
\[
W_0=(1,U),\ W_1,\ldots,W_m=(1,V).
\]

Every adjacent pair must be one explicitly located contextual replacement of either:

- \(ww\leftrightarrow w\), with \(w\) nonempty; or
- \((g,st)\leftrightarrow(g,s)(gq(s),t)\),

with the unchanged left and right contexts displayed or mechanically identified.

Only a successful check of this full chain, together with \(U\ne V\) in the source, certifies the all-host obstruction. No such completed data object is asserted to exist in this return.

---

## 8. A finite-host bound at the universal criterion

For finite \(S,G\), the universal alphabet has
\[
k=|G||S|
\]
letters. The band \(C_q\) is a quotient of the free band on those letters. The bound in §4.1 therefore gives
\[
|C_q|\le
\sum_{j=1}^{2^{k+1}-2}k^j.
\]

Consequently, if any band host embeds \(S\) over \(q\), the canonical finite host \(C_q\rtimes G\) does so, with
\[
|C_q\rtimes G|
\le
|G|\sum_{j=1}^{2^{k+1}-2}k^j.
\]

This is a finite-versus-infinite frontier statement. It does not provide an efficient procedure, a completed congruence computation, or permission to enumerate this bound under the modest local-check allowance. No such enumeration was attempted.

---

## 9. Disposition and exact unpaid steps

### Established in this written return

At the explicitly stated elementary-band-theory import boundary:

- The construction \(S=S_0/\theta\) is finite, associative and regular.
- Its displayed quotient \(q:S\twoheadrightarrow C_2\) is idempotent-pure.
- Its idempotents do not commute, so it is genuinely noninverse.
- Its chosen \(a,a',b,b',e,f,g\) satisfy the four recovered premises.
- The exact candidate pair \(U,V\), their group values and their coordinate expansions are specified.
- The universal construction has the stated finite-host bound.

These are **author-written claims**, not parent-adopted or independently reviewed results.

### Not established

- \(U\ne V\) after taking the source congruence.
- \((0,U)\equiv_q(0,V)\) by a displayed finite derivation.
- Nonembedding of this candidate into all band-by-group hosts.
- Identity of this candidate with either 1998 construction.
- Recovery of the complete Billhardt or Szendrei primary proof.
- Applicability to unspecified printed-source, canonical-host, SN/RIGHTSN/Horn or other additional conditions.

### The exact remaining scientific obligations

The first unresolved source step is **SEP**, not associativity, regularity or purity. It needs an exact separating invariant/model or a fully checked finite quotient computation.

The second unresolved step is **COLL**, requiring the actual universal-band derivation. Importing the reported quasiidentity without reconstructing its proof would leave this assignment’s certificate requirement unpaid.

Alternatively, obtaining Szendrei’s pp. 202–214 or Billhardt’s pp. 40–50 in full would permit reconstruction of their exact construction and proof. The public documents reached here do not supply the missing load-bearing separation proof.

**Final scientific verdict: strongest explicit frontier returned; finite all-host negative witness NOT PROVED.** No numerical, novelty, independent-family, human, formal/kernel or automatic-adoption credit is claimed.