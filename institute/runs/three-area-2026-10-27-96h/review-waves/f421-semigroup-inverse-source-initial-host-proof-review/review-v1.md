# review-v1.md — F421 inverse-source initial-host written review

**Disposition: SUPPORTED at the complete assigned inverse-source scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR mathematical defects.**

This is a same-harness written reconstruction, not parent acceptance, independent-model-family review, human review, kernel verification, or novelty certification. The complete review body is returned for parent materialization; no own-wave file was created.

## 1. Exact scope and claimwise verdicts

Let \(S\) be any nonempty inverse semigroup, let
\[
D=M[G;I,\Lambda;Q]
\]
be a completely simple Rees matrix semigroup with nonempty index sets, and let \(q:S\to D\) be an onto homomorphism. The assigned theorem is:

> \(q\) is idempotent-pure if and only if there exist a nonempty semilattice \(C\), a \(G\)-action on \(C\) by automorphisms, and an embedding
> \[
> F:S\hookrightarrow T(C,D)
> \]
> whose actor projection is exactly \(q\), using the displayed physical-host multiplication.

The quantifiers include arbitrary infinite \(S\), arbitrary nonempty Rees index sets before their derived collapse, and an arbitrary sandwich entry—not an assumed identity entry.

References below use **this wave’s packet source labels and source-line numbers**.

| Assigned claim | Verdict | Source anchors |
|---|---|---|
| Physical-host associativity and actor-projection purity for any band and nonempty Rees indices | SUPPORTED | S1 35–74; interface S2 7, S3 26–78 |
| Onto pure inverse-source quotient has singleton row and column sets | SUPPORTED | S1 120–139 |
| \(\rho(i_0,h,\lambda_0)=hp\) is the correct group isomorphism and preserves the actual twisting convention | SUPPORTED | S1 141–172, 337–353 |
| \(\iota(x)=(\bar q(x),x^{-1}x)\) is injective, with covariance on the actual multiplication domain | SUPPORTED | S1 176–230 |
| \(R_{st}=R_s\cap\bar q(s)R_t\), with both inclusions and correct domain/range handling | SUPPORTED | S1 246–324 |
| \(F(s)=(R_s,q(s))\) is multiplicative and injective | SUPPORTED | S1 328–401 |
| Powerset semilattice, automorphism action, semilattice corners, and finite construction when \(S\) is finite | SUPPORTED | S1 102–112, 234–261, 408–413 |
| Original arbitrary-regular-source, canonical-host, SN/RIGHTSN, Horn, Fact1/source-authentication and Q1 conclusions | INCONCLUSIVE / unpaid | S1 647–661; S2 25; S3 433–449 |

S1’s subgroup-host extension results and finite witness were read as required by complete-packet coverage. They are **not independently adjudicated by this inverse-source gate and are not premises of the proof below**.

## 2. Foundational inverse identities

The reconstruction uses the standard meaning of inverse semigroup: every element has a unique inverse. The required identities can be justified directly, without importing a representation theorem.

For \(s\in S\),
\[
ss^{-1}s=s,\qquad s^{-1}ss^{-1}=s^{-1}.
\]
Consequently,
\[
e_s=ss^{-1},\qquad d_s=s^{-1}s
\]
are idempotents. Symmetry of the inverse equations and uniqueness give
\[
(s^{-1})^{-1}=s.
\]
An idempotent is its own inverse.

For completeness, uniqueness also yields commutativity of idempotents. Given idempotents \(e,f\), let \(x\) be the inverse of \(ef\). The element \(fxe\) is another inverse of \(ef\), since
\[
(ef)(fxe)(ef)=(ef)x(ef)=ef
\]
and
\[
(fxe)(ef)(fxe)=f\bigl(x(ef)x\bigr)e=fxe.
\]
Thus \(x=fxe\), and
\[
x^2=fxefxe=f\bigl(x(ef)x\bigr)e=fxe=x.
\]
Since \(ef\) is an inverse of the idempotent \(x\), uniqueness gives \(ef=x\). Hence \(ef\) is idempotent. Interchanging \(e,f\) shows that \(fe\) is idempotent as well. Now
\[
(ef)(fe)(ef)=(ef)^2=ef,\qquad
(fe)(ef)(fe)=(fe)^2=fe.
\]
Therefore \(fe\) is an inverse of the idempotent \(ef\), so \(fe=ef\).

Finally,
\[
(ab)^{-1}=b^{-1}a^{-1}.
\]
Indeed, commuting the idempotents \(bb^{-1}\) and \(a^{-1}a\) gives
\[
(ab)(b^{-1}a^{-1})(ab)
=a(bb^{-1})(a^{-1}a)b
=a(a^{-1}a)(bb^{-1})b
=ab.
\]
The reverse inverse equation follows similarly:
\[
(b^{-1}a^{-1})(ab)(b^{-1}a^{-1})
=b^{-1}(a^{-1}a)(bb^{-1})a^{-1}
=b^{-1}a^{-1}.
\]
Uniqueness proves the formula. These facts supply the inverse identities used in all subsequent steps.

## 3. Actual physical-host multiplication and necessary purity

Use precisely
\[
(c,(i,h,\lambda))(d,(j,k,\mu))
=
\left(c\,((hQ_{\lambda j})\cdot d),
(i,hQ_{\lambda j}k,\mu)\right).
\]

This is associative for any band \(C\) with a \(G\)-action by automorphisms. For actor elements
\[
a=(i,h,\lambda),\quad b=(j,k,\mu),\quad
a'=(\ell,m,\nu),
\]
write \(w(a,b)=hQ_{\lambda j}\). Then
\[
w(ab,a')=hQ_{\lambda j}kQ_{\mu\ell}
=w(a,b)w(b,a').
\]
Thus, for band coordinates \(c,d,v\), the left-associated product has band coordinate
\[
\bigl(c(w(a,b)\cdot d)\bigr)
\bigl((w(a,b)w(b,a'))\cdot v\bigr).
\]
The right-associated product has band coordinate
\[
c\left(w(a,b)\cdot
\bigl(d(w(b,a')\cdot v)\bigr)\right),
\]
which is equal to the preceding expression by the automorphism action and associativity of \(C\). The actor coordinates agree by Rees multiplication.

The actor projection is a homomorphism. Moreover,
\[
(i,h,\lambda)^2=(i,h,\lambda)
\iff hQ_{\lambda i}=1.
\]
When this holds, the twisting coefficient in the square of a host element is \(1\), so
\[
(c,(i,h,\lambda))^2
=(c^2,(i,h,\lambda))
=(c,(i,h,\lambda)).
\]
Conversely, an idempotent host element has idempotent actor. Therefore
\[
\pi_D^{-1}(E(D))=E(T(C,D)).
\]

Consequently, **any** embedding \(F:S\hookrightarrow T(C,D)\) with \(\pi_DF=q\) forces \(q\) to be idempotent-pure: if \(q(s)\) is idempotent, so is \(F(s)\), and
\[
F(s^2)=F(s)
\]
implies \(s^2=s\).

This necessity does not assume that the source is inverse, that \(q\) is onto, or that the band is a semilattice. It therefore proves the necessary direction of the assigned equivalence at its full stated scope.

## 4. Reduction of the prescribed actor, including arbitrary sandwich entry

Assume now that \(S\) is inverse and \(q\) is onto and idempotent-pure.

For any \(a,b\in E(D)\), surjectivity gives \(s,t\in S\) with \(q(s)=a\), \(q(t)=b\). Purity makes \(s,t\) idempotent, so
\[
ab=q(st)=q(ts)=ba.
\]
Thus the idempotents of \(D\) commute.

For arbitrary \(i,j\in I\) and \(\lambda,\mu\in\Lambda\), the elements
\[
a=(i,Q_{\lambda i}^{-1},\lambda),\qquad
b=(j,Q_{\mu j}^{-1},\mu)
\]
are idempotents. The product \(ab\) has row \(i\) and column \(\mu\), while \(ba\) has row \(j\) and column \(\lambda\). Equality forces
\[
i=j,\qquad \mu=\lambda.
\]
Because the indices were arbitrary and their sets are nonempty, both index sets are singletons.

Write their unique elements as \(i_0,\lambda_0\), and set
\[
p=Q_{\lambda_0 i_0}.
\]
No normalization or centrality of \(p\) is assumed. Define
\[
\rho:D\to G,\qquad
\rho(i_0,h,\lambda_0)=hp.
\]
Its inverse is
\[
g\longmapsto(i_0,gp^{-1},\lambda_0),
\]
and
\[
\rho(i_0,hpk,\lambda_0)=hpkp=(hp)(kp).
\]
Thus \(\rho\) is a group isomorphism. In particular, the identity of \(D\) is \((i_0,p^{-1},\lambda_0)\).

Set
\[
\bar q=\rho q,\qquad g_s=\bar q(s).
\]
Then \(\bar q\) is onto, and
\[
\bar q^{-1}(1)=E(S).
\]
Indeed, \(\rho^{-1}(1)\) is the unique idempotent of the group \(D\), and the equivalence follows from purity and the automatic preservation of idempotents.

Also,
\[
g_s\,\bar q(s^{-1})=\bar q(ss^{-1})=1,
\]
so
\[
\bar q(s^{-1})=g_s^{-1}.
\]

The collapse to a group is therefore a conclusion from the original hypotheses, not a restriction imposed on the prescribed quotient.

## 5. Injective source coordinates and the exact partial-action domain

Let
\[
X=G\times E(S),\qquad
\iota(x)=\bigl(\bar q(x),x^{-1}x\bigr).
\]

### 5.1 Injectivity

Suppose
\[
\bar q(x)=\bar q(y),\qquad
x^{-1}x=y^{-1}y=e.
\]
Put \(u=xy^{-1}\). Then
\[
\bar q(u)=1,
\]
so purity makes \(u\) idempotent. Using the inverse identities established above,
\[
u=u^{-1}=yx^{-1}.
\]
Consequently,
\[
uy=xy^{-1}y=xe=x,\qquad
ux=yx^{-1}x=ye=y.
\]
Since \(u^2=u\),
\[
x=uy=u^2y=u(uy)=ux=y.
\]
Thus \(\iota\) is injective.

In particular, the argument does not assume that equality of group images alone separates source elements. The domain-idempotent coordinate and purity are both used.

### 5.2 Covariance only on its valid domain

Let \(G\) act on \(X\) by
\[
g\cdot(h,e)=(gh,e).
\]
If \(d_sx=x\), then
\[
(sx)^{-1}(sx)=x^{-1}s^{-1}sx=x^{-1}x,
\]
and hence
\[
\iota(sx)=g_s\cdot\iota(x).
\]

The relevant source map is the partial bijection
\[
d_sS\longrightarrow e_sS,\qquad x\longmapsto sx,
\]
whose inverse is \(z\mapsto s^{-1}z\). The equations
\[
s^{-1}(sx)=d_sx=x,\qquad
s(s^{-1}z)=e_sz=z
\]
hold on precisely those respective domains.

For any idempotent \(e\), the notation is valid without a source identity:
\[
eS=\{x\in S:ex=x\}.
\]
The two descriptions agree because \(e(ey)=ey\), and \(ex=x\) expresses \(x\) as an element of \(eS\).

Nothing here asserts that left multiplication by \(s\) permutes all of \(S\), or that translation by \(g_s\) preserves all of \(\iota(S)\).

## 6. Powerset semilattice and both inclusions in the range identity

Take
\[
C=\mathcal P(X)
\]
with intersection as multiplication. It is a nonempty semilattice. The translations on \(X\) induce
\[
gU=\{g\cdot x:x\in U\}.
\]
Each translation is bijective with inverse \(g^{-1}\), so
\[
g(U\cap V)=gU\cap gV.
\]
These maps form a \(G\)-action by semilattice automorphisms.

For \(s\in S\), define
\[
R_s=\iota(e_sS).
\]
This set is nonempty because \(e_s\in e_sS\).

The necessary multiplication identity is
\[
R_{st}=R_s\cap g_sR_t.
\]

### 6.1 Forward inclusion

Let \(z\in e_{st}S\), and put
\[
f=e_t=tt^{-1},\qquad d=d_s=s^{-1}s,\qquad
w=s^{-1}z.
\]
The inverse-product identity gives
\[
e_{st}=st(st)^{-1}=sfs^{-1}.
\]
Also,
\[
e_se_{st}=e_{st},
\]
so \(e_sz=z\). Therefore
\[
sw=z,\qquad dw=w.
\]

Since \(z=e_{st}z\),
\[
w=s^{-1}z=s^{-1}sfs^{-1}z=dfw.
\]
The idempotents \(d,f\) commute, and thus
\[
fw=fdfw=dfw=w.
\]
Hence \(w\in e_tS\). Applying covariance on its valid domain \(dw=w\),
\[
\iota(z)=\iota(sw)=g_s\iota(w)\in g_sR_t.
\]
At the same time, \(z\in e_sS\), so \(\iota(z)\in R_s\). This proves
\[
R_{st}\subseteq R_s\cap g_sR_t.
\]

### 6.2 Reverse inclusion

An arbitrary point of \(R_s\cap g_sR_t\) has the form
\[
\iota(z)=g_s\iota(x),
\qquad z\in e_sS,\quad x\in e_tS.
\]
The covariance identity for \(s^{-1}\) is applicable to \(z\), because its domain condition is exactly
\[
(s^{-1})^{-1}s^{-1}z=ss^{-1}z=e_sz=z.
\]
Therefore
\[
\iota(s^{-1}z)
=g_s^{-1}\iota(z)
=\iota(x).
\]
Injectivity of \(\iota\) gives \(s^{-1}z=x\). Consequently,
\[
e_{st}z
=se_ts^{-1}z
=se_tx
=sx
=ss^{-1}z
=z.
\]
Thus \(z\in e_{st}S\), proving
\[
R_s\cap g_sR_t\subseteq R_{st}.
\]

Both inclusions are therefore established. In particular, the reverse direction uses the range condition on \(z\) before applying multiplication by \(s^{-1}\); it does not silently extend a partial source action to a total action.

## 7. The actual consuming host product and source separation

Define
\[
F(s)=(R_s,q(s)).
\]
Write
\[
q(s)=(i_0,h_s,\lambda_0).
\]
The twisting coefficient in the **actual displayed host multiplication** is
\[
h_sQ_{\lambda_0 i_0}=h_sp=\rho(q(s))=g_s.
\]
Thus
\[
\begin{aligned}
F(s)F(t)
&=\left(R_s\cap g_sR_t,\ q(s)q(t)\right)\\
&=(R_{st},q(st))\\
&=F(st).
\end{aligned}
\]
The map is multiplicative at the consuming product, not merely after an unnamed replacement of the actor. Its actor remains exactly
\[
\pi_DF=q.
\]

For injectivity, suppose \(F(s)=F(t)\). Then
\[
g_s=g_t,\qquad R_s=R_t.
\]
Since \(\iota(e_s)\in R_s=R_t\), some \(x\in e_tS\) satisfies
\[
\iota(x)=\iota(e_s).
\]
Injectivity of \(\iota\) gives \(x=e_s\), hence
\[
e_te_s=e_s.
\]
Interchanging \(s,t\) gives
\[
e_se_t=e_t.
\]
The idempotents commute, so \(e_s=e_t\). Finally,
\[
\iota(s^{-1})
=\bigl(g_s^{-1},ss^{-1}\bigr)
=\bigl(g_t^{-1},tt^{-1}\bigr)
=\iota(t^{-1}).
\]
Injectivity yields \(s^{-1}=t^{-1}\), and taking inverses yields \(s=t\).

This completes the sufficient direction and therefore the full assigned equivalence.

## 8. Corners, finiteness, and edge conditions

For every \(U\subseteq X\),
\[
UCU=\{U\cap V\cap U:V\subseteq X\}=\mathcal P(U).
\]
Indeed, every displayed intersection is contained in \(U\), and every subset \(W\subseteq U\) is obtained by taking \(V=W\). Each corner is consequently a semilattice. In particular, both local left-regular and local right-regular band identities hold.

If \(S\) is finite, then \(E(S)\) is finite, and surjectivity onto \(D\cong G\) makes \(G\) finite. Hence
\[
|C|=2^{\,|G|\,|E(S)|},
\qquad
|T(C,D)|=|G|\;2^{\,|G|\,|E(S)|}.
\]
This is a construction bound, not an efficiency or minimality claim. No finite-host conclusion is asserted merely from the unrestricted infinite-source theorem.

The proof also resolves the relevant edge conditions:

- No identity of \(S\) is required; every use of \(eS\) was justified without adjoining one.
- No finiteness, finite generation, or cancellation in \(S\) is required.
- The argument does not assume any nontriviality beyond the stated nonempty sets.
- The sandwich entry \(p\) may be nonidentity and noncentral. Its multiplication order is retained in both \(\rho(h)=hp\) and the host twist \(h_sp\).
- Empty subsets are legitimate elements of \(C\); they do not affect the nonemptiness of each constructed \(R_s\).
- The construction uses no global choice of preimages under \(q\). Surjectivity supplies local existential witnesses in the quotient-reduction proof, not a chosen section. All of \(X,\iota,C,R_s,F\) are explicitly defined from the given data.
- If \(q\) is not pure, the necessary direction rules out an embedding over that \(q\) into any host of the displayed band form. Thus the equivalence does not leave the nonpure case unaddressed.

## 9. Exact imports and unpaid gates

### Mathematical imports

The physical-host convention is the one displayed in S1 35–50 and in the expressly assigned interface S2 7 / S3 26–37. Its associativity and projection purity were reconstructed above.

S1’s inverse-source statements were treated as candidate claims to be checked, not accepted premises. The reconstruction does **not** require the earlier actor-extension equivalence, its Rees gauge theorem, action descent, or a pre-existing source embedding.

S3 was expressly assigned as a complete read for the earlier host/gauge interface. It is an earlier review body; no claim of blindness to that assigned text is made. No linked predecessor or other review body was followed.

No McAlister representation theorem, paper theorem number, or purported literature identification is imported. S1 667–676 is author-attributed historical context only; this wave did not independently audit those publisher records or establish novelty.

### What this gate pays

At written-proof level, it supplies:

1. Initial-host existence for every nonempty inverse source with the prescribed onto pure \(q\).
2. Exact preservation of that prescribed actor map.
3. A semilattice target band with an explicit automorphism action.
4. Full source separation, including the range-idempotent and inverse-coordinate steps.
5. Explicit corner properties and a finite construction when the source is finite.

### What remains unpaid

- **General regular sources:** the proof depends on unique inverses, commuting idempotents, and the injectivity of \(\iota\). No replacement is proved for arbitrary regular sources.
- **Genuinely multirow or multicolumn quotients of general regular sources:** the inverse-source quotient collapse does not resolve those cases.
- **Extension from an arbitrary supplied initial host:** the constructed \(F\) is a new source embedding. It does not produce a matching actor homomorphism from every other initial actor, or a map extending every pre-existing whole-host embedding.
- **Arbitrary-embedding obstruction:** failure of a whole-host extension route is not, by itself, failure of an unrelated source-only embedding.
- **Additional admissibility definitions:** semilattice and corner properties do not certify undefined SN, RIGHTSN, canonical, free-band, or Horn requirements.
- **Original-source identification:** printed-problem authentication, Fact1 reconstruction, model compatibility, and Q1 closure remain unpaid.
- **Acceptance and verification families:** a separate parent disposition is required. No finite-machine replay, independent-model-family, human, formal/kernel, or novelty acceptance is supplied by this review.

## 10. Process, coverage, and metadata attribution

### Administrative order

Before any mathematical packet read, I read:

- The required memory summary and relevant procedural skills.
- The complete manifest and freeze receipt.
- The parent dispatch receipt and complete live-metadata supply.
- All seven named status-only controls through their endings.

The control read coverage was:

| Status-only control | Complete line coverage |
|---|---:|
| Owner frontier-first addendum | 1–14 |
| L1 selected-diagnostic quarantine | 1–23 |
| Written-duty execution/reporting deviations | 1–28 |
| Held PH registration/report-consumer quarantine | 1–49 |
| AME held-claim consumer quarantine | 1–8 |
| Auxiliary-operator diagnostic quarantine | 1–9 |
| Privacy auxiliary-parameter diagnostic quarantine | 1–11 |

These supplied exclusions and process status only. No held mathematical payload or excluded link was followed.

I then sent a direct **PRE-BODY ACK** to `agent://Main`; the tool reported **“Delivered to Main.”** The first mathematical packet read occurred afterward.

### Complete packet coverage

The packet was read in ordered raw windows
\[
[20k+1,20k+20]\quad(k=0,\ldots,64),
\]
followed by the final window \(1301\)–\(1307\). Thus every read window contained at most 20 LF, and their union covered the complete packet from line 1 through line 1307. No elision was observed.

This included:

- S1: all source-line labels 1–720, including its final status.
- S2: all source-line labels 1–25, including its scope ending.
- S3: all source-line labels 1–560, including its final publication-status ending.

The source-line labels include final unterminated lines where present; they are distinguished here from the parent-reported counts of LF bytes. Mathematical reconstruction began only after the complete-packet read. Subsequent rereads of proof anchors also used raw windows of at most 20 LF.

### Frozen bindings

The following pins and byte/LF counts are **parent-observed metadata**, not independently executed child measurements:

| Item | SHA256 | Bytes | LF |
|---|---|---:|---:|
| Manifest | `388d739527b0d01bbf3eeee9320fd9052d721c152fff2dd95e41ee87b978f3d5` | 6,310 | 102 |
| Freeze receipt | `8f3c69d2ebbbd988b296f2b65afbd57f53997b34cdd2018c0ddf4407a170b186` | 2,391 | 60 |
| Literal packet | `16810534ecdaba2b69f1a91691a9e9120e17b2f53feb1adf637612827bdc4adc` | 61,013 | 1,307 |
| S1 candidate | `a9e535a45a44c7638c4db80d4ae2a4c422e13d15fd030d65768f6b4ab143d850` | 22,897 | 719 |
| S2 disposition/interface | `a2525384fd90acfb80a944df557cd0d9bfd287e732843d93354a66edb5da77fa` | 4,162 | 25 |
| S3 assigned earlier review/interface | `f8f702eb94ec8389051fd022664a18c7aaee4f40ef4a9da6e7b4669392b2fd1c` | 25,035 | 559 |

The parent supplied a live-match observation at **2026-10-30T10:56:06-0700 PDT**, and later a fresh parent clock observation at **2026-10-30T11:01:01-0700 PDT** immediately before sending its reply. Neither is claimed as my native start, completion, or elapsed-time measurement.

### Actual methods and delivery boundary

All mathematics in this review is universal written reasoning. No new selected instance, scientific executable, interpreter, CAS, solver, enumeration, finite replay, or test was used. No author code, current sibling output, extra reviewer body, external scientific search, or external-model CLI was used.

No build, lint, formatter, installation, deletion, credential action, commit, push, or publication was performed. No executable deliverable is assigned to this WRITTEN gate.

The available write transport does not authorize working-tree writes. No own-wave file creation or shell-write bypass was attempted. This complete body is supplied for parent materialization and separate disposition.

## Final verdict

**overall_correctness:** correct

**explanation:** The complete inverse-source theorem is supported by the written reconstruction, including arbitrary prescribed sandwich entry, both range-set inclusions, the actual consuming host multiplication, and source injectivity without finiteness or hidden choice. The original general-regular-source and canonical/source-authentication obligations remain unpaid; this review neither adopts them nor converts whole-host extension questions into arbitrary source-embedding obstructions.

**confidence:** 0.99