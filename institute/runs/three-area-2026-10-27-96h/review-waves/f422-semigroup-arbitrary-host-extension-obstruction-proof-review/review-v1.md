# f422 WRITTEN review — arbitrary-host matching-extension obstruction

**Delivery:** Complete review text for parent materialization; no repository file written.  
**Scope:** The frozen subgroup-host criterion, the actual \(C_2\le C_4\) obstruction, the whole cyclic family, the nonpure negative control, and the source-embedding/whole-host-extension distinction. The inverse-source construction in the complete packet is also reconstructed below.  
**Disposition boundary:** This is a written review, not parent acceptance. The candidate remains **UNREVIEWED pending separate parent disposition**.

## 1. Evidence, read order, and execution boundary

Before reading the mathematical packet, I read the complete manifest, freeze receipt, all seven required status-only controls through their endings, and the supplied parent live-metadata record. I then sent Main an administrative pre-body ACK.

After that ACK, I read **packet LF1–747 completely and in order**, in raw windows of at most 20 LF, including:

- S1 LF1–720, the complete author candidate, including its final status;
- S2 LF1–25, the complete prior parent disposition, including its scope exclusions.

The following integrity observations are **parent-supplied**, not independently executed hashes or native reviewer timestamps:

| Item | Frozen SHA256 |
|---|---|
| Manifest | `987c9c34bde75d4a131d0896d5e54f0856f8657cb654be113ec452e57562aa73` |
| Freeze receipt | `869a7d504ae9c734dd4472da04c69b02a421f8551d207155d7d544ba84115749` |
| Literal packet | `3b18b56ed32a2fe84e87bb0ec58b11fedbfb6f291c0c3ef5b90d2a8b24c64cfd` |
| S1 author candidate | `a9e535a45a44c7638c4db80d4ae2a4c422e13d15fd030d65768f6b4ab143d850` |
| S2 prior disposition | `a2525384fd90acfb80a944df557cd0d9bfd287e732843d93354a66edb5da77fa` |

The parent metadata observation is **2026-10-30T10:56:06-0700 PDT**. It is not my native start or completion time.

All held episodes and their mathematical, selection, planning, and confidence consumers were treated as **NONINPUT**. I did not follow excluded links or read current sibling outputs, author code, or unassigned predecessor bodies.

**No scientific execution occurred in this review:** no interpreter, CAS, solver, enumeration, selected-instance probe, code replay, build, test, lint, or formatter. The finite verification below is written reasoning from the expressly assigned tables and relations. No external-model CLI or paid computation was used.

## 2. Claimwise verdicts

| Claim | Verdict | Frozen location |
|---|---|---|
| A physical-host embedding over \(q\) forces idempotent purity of \(q\) | **SUPPORTED** | S1 LF35–74 |
| For every group \(H\), subgroup \(K\le H\), and isomorphism \(q:K\to G\), a matching extension exists iff \(K\) is a retract of \(H\) | **SUPPORTED** | S1 LF419–447 |
| A matching extension in that class can be idempotent-pure iff \(K=H\) | **SUPPORTED** | S1 LF438–455 |
| An actor-respecting embedding of the entire singleton-band initial host over \(q\) exists iff \(K=H\) | **SUPPORTED** | S1 LF439–457 |
| The displayed \(C_2\le C_4\) data satisfy the stated source, host, quotient, purity, and kernel hypotheses | **SUPPORTED** | S1 LF463–542 |
| That actual example has no matching actor homomorphism, pure or nonpure | **SUPPORTED** | S1 LF545–570 |
| Every supplied initial host admits a matching actor extension under those hypotheses | **REFUTED** by the displayed example | S1 LF568–570 |
| The same example nevertheless has a source-only embedding over \(q\) | **SUPPORTED** | S1 LF574–583 |
| For \(m\ge2,n\ge1\), the cyclic family has a matching extension iff \(\gcd(n,m)=1\), and a pure matching extension iff \(n=1\) | **SUPPORTED** | S1 LF585–616 |
| The assigned trivial-quotient negative control is nonpure and admits no source embedding over that quotient | **SUPPORTED** | S1 LF620–630 |
| The complete inverse-source construction preserves the prescribed \(q\) exactly | **SUPPORTED** as written mathematics | S1 LF80–413 |
| Failure of a canonical-host theorem, failure of arbitrary source embeddings, or closure of the general regular-source target | **INCONCLUSIVE / not established** | S1 LF31, 572, 647–661; S2 LF25 |

The refuted statement is the explicitly identified unrestricted extension premise, **not an assertion endorsed by the candidate**.

## 3. Physical-host projection purity

The displayed product is
\[
(c,(i,h,\lambda))(d,(j,k,\mu))
=
\left(c((hQ_{\lambda j})\cdot d),
(i,hQ_{\lambda j}k,\mu)\right).
\]

For \(a=(i,h,\lambda)\), the Rees multiplication gives
\[
a^2=a
\quad\Longleftrightarrow\quad
hQ_{\lambda i}=1.
\]
If \(a\) is idempotent, the twisting coefficient in \((c,a)^2\) is therefore the identity. Since \(C\) is a band,
\[
(c,a)^2=(c^2,a)=(c,a).
\]
Conversely, an idempotent of the host projects to an idempotent of the actor. Hence
\[
\pi_D^{-1}(E(D))=E(T(C,D)).
\]

Consequently, for any injective homomorphism \(F:S\to T(C,D)\) with \(\pi_DF=q\),
\[
q(s)\in E(D)
\ \Longrightarrow\
F(s)^2=F(s)
\ \Longrightarrow\
F(s^2)=F(s)
\ \Longrightarrow\
s^2=s.
\]
This establishes the necessary purity condition without requiring regularity of \(S\), surjectivity of \(q\), or a particular gauge construction.

This also verifies the consuming-side step needed later: a whole-host embedding cannot conceal a nonidempotent element inside a fibre over an idempotent actor by choosing a different target band coordinate.

## 4. Complete subgroup-host criterion

### 4.1 Exact quantified hypotheses

Let:

- \(H\) be **any group**, finite or infinite;
- \(K\le H\) be **any subgroup**;
- \(q:K\overset{\cong}{\longrightarrow}G\) be **any group isomorphism**;
- the initial physical host be \(T(\{*\},H)\), with singleton band and trivial action;
- the source \(S=K\) be embedded by \(k\mapsto(*,k)\).

No normality of \(K\), finiteness, actor saturation, or canonical-host property is assumed.

A matching extension means a homomorphism
\[
\phi:H\longrightarrow G
\quad\text{such that}\quad
\phi(k)=q(k)\quad(k\in K).
\]

### 4.2 Matching extension iff retraction

Given a matching extension, define
\[
\rho=q^{-1}\phi:H\longrightarrow K.
\]
It is a homomorphism and
\[
\rho(k)=q^{-1}(q(k))=k
\quad(k\in K).
\]
Thus \(\rho\) is a retraction onto the actual subgroup \(K\).

Conversely, if \(\rho:H\to K\) satisfies \(\rho|_K=\operatorname{id}_K\), then
\[
\phi=q\rho
\]
is a matching homomorphism.

This is an exact equivalence for the entire stated class. It neither assumes nor implies that \(K\) is normal or that \(H\) is a direct product.

### 4.3 Pure matching extension iff \(K=H\)

For a group homomorphism,
\[
\phi^{-1}(E(G))=\phi^{-1}(\{1_G\})=\ker\phi,
\qquad E(H)=\{1_H\}.
\]
Therefore idempotent purity is equivalent to trivial kernel, hence injectivity.

Every matching extension is already surjective because
\[
\phi(K)=q(K)=G.
\]
Suppose it is also injective. For any \(h\in H\), surjectivity of \(q\) supplies \(k\in K\) such that
\[
q(k)=\phi(h).
\]
Then \(\phi(k)=\phi(h)\), so \(k=h\). Thus every \(h\) belongs to \(K\), proving \(H=K\).

Conversely, if \(H=K\), the isomorphism \(q\) itself is a pure matching extension.

Importantly, this is **not a finite-cardinality argument**. It remains valid for infinite \(H\) and \(K\), even when they are abstractly isomorphic but \(K\) is a proper subgroup of the supplied \(H\).

### 4.4 Entire-host embedding iff \(K=H\)

Suppose an embedding
\[
\Psi:T(\{*\},H)\hookrightarrow T(C,G)
\]
has actor homomorphism \(\phi\) with \(\phi|_K=q\).

If \(\phi(h)=1_G\), projection purity makes \(\Psi(*,h)\) idempotent. Injectivity of \(\Psi\) then forces \((*,h)\) to be idempotent, so \(h=1_H\). Thus \(\phi\) is pure, and §4.3 forces \(K=H\).

If \(K=H\), a singleton target band suffices:
\[
(*,h)\longmapsto(*,q(h)).
\]
This is an injective homomorphism with the required actor.

The necessity does not depend on an unexamined representation theorem: it follows directly at the consuming host projection. The sufficiency is an explicit map.

### 4.5 Edge cases

The argument includes trivial groups and subgroups. For trivial \(K\), \(G\) is trivial; a matching homomorphism always exists, while purity and an entire-host embedding require \(H\) itself to be trivial. No nontriviality assumption has silently entered Proposition 4.1.

Thus all three parts of the proposition are supported at their actual quantifiers.

## 5. Written reconstruction of the actual \(C_2\)-in-\(C_4\) obstruction

### 5.1 Complete supplied multiplication data

The initial actor is \(A=C_4\), written additively:

| \(+\) | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| **0** | 0 | 1 | 2 | 3 |
| **1** | 1 | 2 | 3 | 0 |
| **2** | 2 | 3 | 0 | 1 |
| **3** | 3 | 0 | 1 | 2 |

The source subgroup is \(S=\{0,2\}\):

| \(+\) | 0 | 2 |
|---|---:|---:|
| **0** | 0 | 2 |
| **2** | 2 | 0 |

The prescribed target is \(D=C_2\):

| \(+\) | 0 | 1 |
|---|---:|---:|
| **0** | 0 | 1 |
| **1** | 1 | 0 |

The band is \(B=\{*\}\), with \(**=*\), and the action is trivial. With the normalized singleton Rees indices and additive sandwich entry \(0\), the physical-host product is exactly
\[
(*,a)(*,b)=(*,a+b).
\]

These are the assigned tables, not executable output or a newly selected example.

### 5.2 All antecedents hold

Both \(S\) and \(A\) are groups. In particular, \(S\) is a regular inverse semigroup. Each displayed group has only its identity \(0\) as an idempotent.

Define
\[
q(0)=0,\qquad q(2)=1.
\]
The source relation \(2+2=0\) maps to \(1+1=0\), and the remaining products involve the identity. Thus \(q\) is a homomorphism. Its two images are distinct and exhaust \(D\), so it is an isomorphism and in particular an onto idempotent-pure homomorphism:
\[
q^{-1}(E(D))=\{0\}=E(S).
\]

The initial embedding
\[
f(s)=(*,s)
\]
is multiplicative by the displayed host product and injective by its second coordinate. Its actor map is the subgroup inclusion \(r(s)=s\). Therefore, as kernel congruences,
\[
\ker r=\ker q=\Delta_S.
\]
In particular, the required kernel inclusion holds.

What does **not** hold is saturation:
\[
r(S)=\{0,2\}\ne C_4.
\]
This is not a failed antecedent of the arbitrary-host premise under review; it is precisely the boundary distinguished in S2 LF11.

### 5.3 No matching homomorphism exists

Suppose
\[
\phi:C_4\to C_2,\qquad \phi r=q.
\]
The actual relation \(2=1+1\) in \(C_4\) gives
\[
\phi(2)=\phi(1)+\phi(1)=0,
\]
because every element of \(C_2\) doubles to \(0\).

Matching \(q\) instead gives
\[
\phi(2)=q(2)=1.
\]
This is a contradiction.

The argument excludes **every** matching homomorphism. It therefore excludes matching pure extensions and matching nonpure extensions alike; it is not merely a failure of an attempted choice of \(\phi\).

Every entire-host map into a physical host over \(D\) would, on composing with the actor projection, produce such a matching homomorphism. Consequently the claimed actor-respecting entire-host embedding is also impossible.

### 5.4 The source-only embedding is explicit

There is nevertheless an embedding
\[
F_0:S\hookrightarrow T(\{*\},D),
\qquad
F_0(s)=(*,q(s)).
\]
It is multiplicative because \(q\) is, and injective because \(q\) is an isomorphism. Its actor is exactly the prescribed \(q\).

Thus the same frozen data simultaneously establish:

1. a valid initial host and source embedding;
2. failure of matching extension from that supplied entire actor;
3. existence of a source-only embedding over \(q\).

This prevents converting the arbitrary-preselected-host obstruction into an arbitrary-source-embedding obstruction.

## 6. Whole cyclic family, including the stated boundary cases

Let
\[
m\ge2,\qquad n\ge1,
\]
and set
\[
H=\mathbb Z/(mn)\mathbb Z,\qquad
K=n\mathbb Z/(mn)\mathbb Z.
\]

The map
\[
\mathbb Z/m\mathbb Z\longrightarrow K,\qquad [k]_m\longmapsto[nk]_{mn}
\]
is well defined and bijective: equality of the target residues is equivalent to \(mn\mid n(k-\ell)\), hence to \(m\mid k-\ell\). It preserves addition. Its inverse is the prescribed isomorphism
\[
q([nk]_{mn})=[k]_m.
\]

Any homomorphism \(H\to C_m\) is determined by
\[
a=\phi([1]_{mn}),
\qquad
\phi([x]_{mn})=[xa]_m.
\]
Every \(a\in C_m\) defines such a homomorphism, since \((mn)a=0\) in \(C_m\).

Matching on \(K\) requires, and is implied by,
\[
na=1\pmod m.
\]
Necessity follows by evaluating at the subgroup generator \([n]_{mn}\); sufficiency follows by multiplying that congruence by every \(k\).

This congruence is solvable exactly when \(\gcd(n,m)=1\):

- If it is solvable, every common divisor of \(n,m\) divides \(na\) and \(m\), and hence divides \(1\).
- If \(\gcd(n,m)=1\), a Bézout identity supplies an inverse of \(n\) modulo \(m\).

For purity, §4 applies directly. The subgroup has \(m\) elements and \(H\) has \(mn\) elements, so
\[
K=H\quad\Longleftrightarrow\quad n=1.
\]
Equivalently, whenever \(n>1\) and a matching extension exists, the nonzero element \([m]_{mn}\) is in its kernel:
\[
\phi([m]_{mn})=[ma]_m=0.
\]
It is nonzero because \(0<m<mn\), and hence is not an idempotent of the source group.

The three stated cases are therefore exhaustive:

- **\(n=1\):** \(K=H\), and the prescribed \(q\) is a pure matching extension.
- **\(n>1\), \(\gcd(n,m)=1\):** matching extensions exist, but none is pure.
- **\(\gcd(n,m)>1\):** no matching extension exists.

The restriction \(m\ge2\) is retained. No unstated assumption \(n>1\) was used in deriving the extension criterion. The assigned \(m=n=2\) member is exactly the displayed \(C_2\le C_4\) obstruction.

## 7. Nonpure trivial-quotient negative control

Use the assigned source \(S=\{0,2\}\), but the prescribed quotient
\[
q_{\mathrm{triv}}:S\to\{0\},
\qquad
q_{\mathrm{triv}}(0)=q_{\mathrm{triv}}(2)=0.
\]
It is onto. It is not idempotent-pure, since \(2\) is nonidempotent while its image is idempotent.

A physical host over the trivial actor is a band. If an injective homomorphism \(F\) over this quotient existed, then
\[
F(2+2)=F(2)^2=F(2).
\]
The left-hand side is \(F(0)\), contradicting injectivity because \(0\ne2\).

This correctly demonstrates that the purity hypothesis cannot simply be dropped. It does not contradict the subgroup-host proposition: that proposition assumes \(q\) is an isomorphism, whereas this control is not.

The reported failure of the inverse-source coordinate map is also correct. In this source, both elements have the same domain idempotent \(0\); after replacing the group coordinate by the trivial quotient, their two coordinates coincide.

## 8. Reconstruction of the complete inverse-source construction

This part is included because the full candidate is an assigned input. The direct source-only embedding in §5.4 does not depend on it.

### 8.1 Quantifiers and quotient reduction

Let \(S\) be any nonempty inverse semigroup and
\[
q:S\to D=M[G;I,\Lambda;Q]
\]
an onto homomorphism, with nonempty Rees index sets.

Necessity of purity for an embedding over \(q\) was proved in §3.

Assume \(q\) is pure. Every idempotent of \(D\) has an idempotent preimage by surjectivity and purity. Since idempotents in \(S\) commute, all idempotents in \(D\) commute.

For arbitrary indices, the idempotents
\[
(i,Q_{\lambda i}^{-1},\lambda),
\qquad
(j,Q_{\mu j}^{-1},\mu)
\]
have products with respective row-column pairs \((i,\mu)\) and \((j,\lambda)\). Equality forces \(i=j\) and \(\mu=\lambda\). Thus \(I,\Lambda\) are singletons.

Writing their sandwich entry as \(p\), the map
\[
\rho(i_0,h,\lambda_0)=hp
\]
is an isomorphism \(D\to G\), because
\[
(hpk)p=(hp)(kp).
\]
Therefore \(\bar q=\rho q\) is onto and
\[
\bar q^{-1}(1)=E(S),\qquad
\bar q(s^{-1})=\bar q(s)^{-1}.
\]

The group-quotient conclusion is derived from the hypotheses; it is not a substitution of a narrower prescribed target.

### 8.2 Injective source coordinates

Define
\[
X=G\times E(S),
\qquad
\iota(x)=(\bar q(x),x^{-1}x).
\]
Suppose \(\iota(x)=\iota(y)\), and put
\[
e=x^{-1}x=y^{-1}y,\qquad u=xy^{-1}.
\]
Then \(\bar q(u)=1\), so \(u\) is idempotent. Its inverse is \(yx^{-1}\), hence \(u=yx^{-1}\). Consequently
\[
uy=xe=x,\qquad ux=ye=y.
\]
Using \(u^2=u\),
\[
x=uy=u^2y=u(uy)=ux=y.
\]
Thus \(\iota\) is injective.

Let \(G\) act on \(X\) by left translation of the first coordinate. Whenever \(s^{-1}sx=x\),
\[
(sx)^{-1}(sx)=x^{-1}s^{-1}sx=x^{-1}x,
\]
so
\[
\iota(sx)=\bar q(s)\cdot\iota(x).
\]
This is asserted only on the actual domain of left multiplication by \(s\); no global permutation action of \(S\) is assumed.

### 8.3 Band coordinates and multiplication identity

Take
\[
C=\mathcal P(X)
\]
with intersection. Translation acts by semilattice automorphisms.

Put \(e_s=ss^{-1}\) and
\[
R_s=\iota(e_sS).
\]
For an idempotent \(e\), the equality
\[
eS=\{x:ex=x\}
\]
does not require an identity in \(S\). Also \(R_s\ne\varnothing\), since \(e_s\in e_sS\).

The required identity is
\[
R_{st}=R_s\cap\bar q(s)R_t.
\]

For the forward inclusion, take \(z\in e_{st}S\), and write
\[
f=tt^{-1},\qquad d=s^{-1}s,\qquad w=s^{-1}z.
\]
Since \(e_{st}=sfs^{-1}\le e_s\), one has \(e_sz=z\), hence \(sw=z\) and \(dw=w\). Moreover,
\[
w=dfw.
\]
Commutativity of the idempotents \(d,f\) gives \(fw=w\), so \(w\in e_tS\). The domain identity above then gives
\[
\iota(z)=\bar q(s)\iota(w),
\]
and \(z\in e_sS\), proving membership in the intersection.

Conversely, suppose
\[
\iota(z)=\bar q(s)\iota(x),
\qquad z\in e_sS,\quad x\in e_tS.
\]
Applying the domain identity to \(s^{-1},z\) gives
\[
\iota(s^{-1}z)=\iota(x).
\]
Injectivity gives \(s^{-1}z=x\), and therefore
\[
e_{st}z
=se_ts^{-1}z
=se_tx
=sx
=ss^{-1}z
=z.
\]
This proves the reverse inclusion.

### 8.4 Consuming host multiplication and separation

Define
\[
F(s)=(R_s,q(s)).
\]
If \(q(s)=(i_0,h_s,\lambda_0)\), the actual twisting coefficient in the displayed physical host is
\[
h_sp=\bar q(s).
\]
Thus the consuming product is exactly
\[
F(s)F(t)
=
\left(R_s\cap\bar q(s)R_t,\ q(s)q(t)\right)
=
(R_{st},q(st))
=
F(st).
\]
In particular, the prescribed actor is preserved **as \(q\)**, not replaced by \(\bar q\).

For injectivity, \(F(s)=F(t)\) gives equal group coordinates and \(R_s=R_t\). Because \(\iota\) is injective, membership of \(\iota(e_s)\) in \(R_t\) gives \(e_te_s=e_s\); the reverse membership gives \(e_se_t=e_t\). Commutativity yields \(e_s=e_t\).

Then
\[
\iota(s^{-1})
=(\bar q(s)^{-1},e_s)
=(\bar q(t)^{-1},e_t)
=\iota(t^{-1}),
\]
so \(s=t\).

The normalized host product is
\[
(U,g)(V,h)=(U\cap gV,gh),
\]
and associativity follows from
\[
(U\cap gV)\cap ghW=U\cap g(V\cap hW).
\]
Thus the construction produces an actual associative physical host and an embedding into it.

### 8.5 Remaining construction details

Nonemptiness is accounted for: a nonempty inverse semigroup has idempotents, and the powerset band is nonempty. No finiteness or identity of \(S\) is required.

For finite \(S\), surjectivity makes \(G\) finite, so the stated band size
\[
|C|=2^{|G||E(S)|}
\]
is correct.

Every corner is
\[
UCU=\mathcal P(U)
\]
under intersection, including the empty-set corner. Hence the stated local left-regular and right-regular band identities follow. This does not establish unspecified non-equational or canonical admissibility conditions.

I found no missing implication in this inverse-source construction.

## 9. Exact imports and unpaid gates

### Imports used

1. **S1 LF35–74:** the displayed physical multiplication and projection-purity calculation, reconstructed above.
2. **S1 LF80–413:** the explicit inverse-source definitions and construction, reconstructed above rather than imported from an unverified literature theorem.
3. **S1 LF419–630:** the subgroup-host proposition, actual finite data, cyclic family, and negative control.
4. **S2 LF7–11:** the meaning of whole-host actor transport and the distinction between saturated actors and mere kernel inclusion.
5. **S2 LF13–17, 25:** the limitation of the fixed-extension quotient/gauge family and the exclusion of arbitrary-source no-go conclusions.

For the subgroup-host result, the needed whole-host necessity was proved directly, so it does not depend on importing the unassigned Rees-gauge proof behind S2. No predecessor linked from S2 LF23 was followed.

The bibliography in S1 LF667–676 is not a load-bearing mathematical import here. I did not independently verify the author's historical reading, execution chronology, publisher descriptions, or a theorem-level literature identification.

### Unpaid or excluded conclusions

This review does **not** establish:

- an initial-host construction for every regular, non-inverse source;
- the multirow or multicolumn completely simple quotient case for general regular sources;
- failure of a separately specified canonical-host construction;
- an obstruction to unrelated source-only embeddings from the arbitrary-host counterexample;
- SN, RIGHTSN, Horn, free-band, or other unnamed admissibility conditions;
- printed-problem identity, Fact1, Q1, or original-target closure;
- novelty or publishability;
- finite-machine replay, kernel/formal verification, human review, or independent-model-family acceptance.

The arbitrary-host counterexample invalidates an unrestricted extension premise. It does not settle the larger source-embedding target in either direction.

## 10. Findings and verdict

**FATAL: 0.**  
**MAJOR: 0.**  
**MINOR: 0.**

No mathematical defect requiring correction was found in the assigned claims. In particular, the subgroup criterion retains its full quantifiers, the supplied counterexample satisfies its actual antecedents, the cyclic criterion includes \(n=1\), and the source-only/entire-host distinction is maintained.

**Overall correctness:** correct.

**Explanation:** The assigned matching-extension criterion, actual \(C_2\le C_4\) obstruction, cyclic family, and negative control withstand written reconstruction. The complete inverse-source construction also checks at the displayed physical-host convention; none of these results supplies general regular-source closure or parent acceptance.

**Confidence:** 0.98.