# author-candidate-v1.md — Initial hosts for inverse sources and a finite obstruction to arbitrary-host actor extension

**Wave:** f399-semigroup-initial-host-or-transport-complete-frontier  
**Status:** **UNREVIEWED AUTHOR CANDIDATE.** Complete written proofs and explicit finite multiplication tables are supplied below. No independent review, finite-machine replay, parent adoption, formal verification or novelty certification is claimed.

**Delivery:** Full body returned for Main materialization. No repository file was written.

## 1. Results and relation to the actual target

This manuscript establishes two distinct results.

1. **Complete inverse-source class.** For every nonempty inverse semigroup \(S\) and every prescribed onto idempotent-pure homomorphism
   \[
   q:S\longrightarrow D=M[G;I,\Lambda;Q],
   \]
   an initial embedding into the actual displayed physical host is constructed:
   \[
   F:S\hookrightarrow T(C,D),\qquad \pi_DF=q,
   \]
   where \(C\) is a semilattice with a \(G\)-action by automorphisms. No pre-existing source embedding is assumed. In fact, for inverse sources and onto \(q\), idempotent purity is necessary and sufficient for such an embedding.

2. **Arbitrary initial hosts do not universally admit matching actor extensions.** For group sources embedded as subgroups of group actors, matching extensions are characterized by subgroup retractions, and matching **pure** extensions exist exactly when the subgroup is the entire actor. The explicit finite example
   \[
   S=\{0,2\}\leq \mathbb Z/4\mathbb Z,\qquad
   q(0)=0,\quad q(2)=1\in\mathbb Z/2\mathbb Z
   \]
   admits no matching actor homomorphism at all, despite satisfying the initial-host, regularity, surjectivity, purity and kernel-inclusion hypotheses.

These address the actual obligations in frozen S1 LF7–17 and LF25, and S2 LF396–413. The first result pays initial-host existence and prescribed-\(q\) source embedding for a complete class. The second disproves an unrestricted matching-extension premise for arbitrary supplied initial hosts.

Neither result proves the original theorem for all regular sources. In particular, failure of whole-host extension is **not** treated as failure of an unrelated source-only embedding.

## 2. Exact physical host convention

For a nonempty band \(C\), a \(G\)-action on \(C\) by automorphisms, and
\[
D=M[G;I,\Lambda;Q],
\]
the host in this manuscript is precisely
\[
T(C,D)=C\times D
\]
with multiplication
\[
(c,(i,h,\lambda))(d,(j,k,\mu))
=
\left(c\,((hQ_{\lambda j})\cdot d),
      (i,hQ_{\lambda j}k,\mu)\right).
\tag{2.1}
\]

The actor projection is \(\pi_D(c,a)=a\).

An element \(a=(i,h,\lambda)\) is idempotent exactly when
\[
hQ_{\lambda i}=1.
\]
Consequently, if the actor is idempotent, the twisting coefficient in the square is \(1\), and
\[
(c,a)^2=(c^2,a)=(c,a).
\]
The converse follows by applying the actor projection. Thus
\[
\pi_D^{-1}(E(D))=E(T(C,D)).
\tag{2.2}
\]

In particular, any embedding over a prescribed \(q\) forces \(q\) to be idempotent-pure. Indeed, if \(q(s)\) is idempotent, then \(F(s)\) is idempotent by (2.2), so
\[
F(s^2)=F(s),
\]
and injectivity gives \(s^2=s\).

This is a necessary condition for arbitrary source embeddings, not merely for the earlier quotient/gauge family.

## 3. Complete initial-host theorem for inverse sources

### Theorem 3.1

Let \(S\) be any nonempty inverse semigroup. Let
\[
D=M[G;I,\Lambda;Q]
\]
be any completely simple Rees matrix semigroup with nonempty index sets, and let
\[
q:S\longrightarrow D
\]
be an onto homomorphism.

The following are equivalent:

1. \(q\) is idempotent-pure.
2. There exist a nonempty semilattice \(C\), a \(G\)-action on \(C\) by automorphisms, and an embedding
   \[
   F:S\hookrightarrow T(C,D)
   \]
   satisfying
   \[
   \pi_DF=q.
   \]

Under these equivalent conditions, both \(I\) and \(\Lambda\) are singletons. Writing their unique sandwich entry as \(p\in G\), the construction below uses
\[
C=\mathcal P(G\times E(S))
\]
with intersection as multiplication.

If \(S\) is finite, this gives a finite host, with
\[
|C|=2^{\,|G|\,|E(S)|}.
\]
No efficiency or minimality claim is made for this bound.

### Proof

The implication \(2\Rightarrow1\) was proved in §2. Assume henceforth that \(q\) is idempotent-pure.

#### Step 1: the prescribed completely simple quotient is a group

Let \(a,b\in E(D)\). Surjectivity supplies \(s,t\in S\) with
\[
q(s)=a,\qquad q(t)=b.
\]
Purity makes \(s,t\) idempotent. Idempotents in an inverse semigroup commute, so
\[
ab=q(st)=q(ts)=ba.
\]
Thus all idempotents of \(D\) commute.

For arbitrary \(i,j\in I\) and \(\lambda,\mu\in\Lambda\), consider the idempotents
\[
e=(i,Q_{\lambda i}^{-1},\lambda),\qquad
f=(j,Q_{\mu j}^{-1},\mu).
\]
The product \(ef\) has row \(i\) and column \(\mu\), whereas \(fe\) has row \(j\) and column \(\lambda\). Their equality forces
\[
i=j,\qquad \mu=\lambda.
\]
Since the indices were arbitrary, \(I\) and \(\Lambda\) are singletons.

Denote them by \(i_0,\lambda_0\), and put
\[
p=Q_{\lambda_0 i_0}.
\]
The map
\[
\rho:D\longrightarrow G,\qquad
\rho(i_0,h,\lambda_0)=hp
\tag{3.1}
\]
is a group isomorphism, because
\[
\rho\bigl((i_0,h,\lambda_0)(i_0,k,\lambda_0)\bigr)
=(hpk)p=(hp)(kp).
\]

Set
\[
\bar q=\rho q:S\longrightarrow G.
\]
Then \(\bar q\) is onto and
\[
\bar q^{-1}(1)=E(S).
\tag{3.2}
\]
Also,
\[
\bar q(s^{-1})=\bar q(s)^{-1}.
\tag{3.3}
\]

The singleton-index conclusion is derived, not imposed as a narrowing of the prescribed quotient.

#### Step 2: an injective coordinate map for the source set

Let
\[
X=G\times E(S)
\]
and define
\[
\iota:S\longrightarrow X,\qquad
\iota(x)=\bigl(\bar q(x),x^{-1}x\bigr).
\tag{3.4}
\]

We first prove that \(\iota\) is injective.

Suppose
\[
\bar q(x)=\bar q(y),\qquad x^{-1}x=y^{-1}y=e.
\]
Put \(u=xy^{-1}\). Its group image is \(1\), so (3.2) makes \(u\) idempotent. Therefore
\[
u=u^{-1}=yx^{-1}.
\]
It follows that
\[
uy=xy^{-1}y=xe=x,
\qquad
ux=yx^{-1}x=ye=y.
\]
Using \(u^2=u\),
\[
x=uy=u^2y=u(uy)=ux=y.
\]
This proves injectivity.

Let \(G\) act on \(X\) by left translation in the first coordinate:
\[
g\cdot(h,e)=(gh,e).
\tag{3.5}
\]

Whenever
\[
s^{-1}s\,x=x,
\]
we have
\[
(sx)^{-1}(sx)=x^{-1}s^{-1}sx=x^{-1}x.
\]
Consequently,
\[
\iota(sx)=\bar q(s)\cdot\iota(x)
\quad\text{if }s^{-1}s\,x=x.
\tag{3.6}
\]

This identity concerns multiplication on its actual inverse-semigroup domain. It does not claim that left multiplication by \(s\) is a permutation of all of \(S\).

#### Step 3: the band and the source band coordinates

Take
\[
C=\mathcal P(X),
\qquad UV=U\cap V.
\]
This is a nonempty semilattice. The action (3.5) induces a \(G\)-action on \(C\):
\[
g\cdot U=\{g\cdot x:x\in U\}.
\tag{3.7}
\]
Each such map is a semilattice automorphism, with inverse induced by \(g^{-1}\).

For \(s\in S\), write
\[
e_s=ss^{-1},
\]
and define
\[
R_s=\iota(e_sS)
=\{\iota(x):e_sx=x\}.
\tag{3.8}
\]

Here, for an idempotent \(e\),
\[
eS=\{x\in S:ex=x\}.
\]
In particular, \(R_s\) is nonempty because \(e_s\in e_sS\).

The crucial identity is
\[
\boxed{R_{st}=R_s\cap\bigl(\bar q(s)\cdot R_t\bigr).}
\tag{3.9}
\]

We prove both inclusions explicitly.

**Forward inclusion.** Let \(z\in e_{st}S\). Put
\[
f=tt^{-1},\qquad d=s^{-1}s,\qquad w=s^{-1}z.
\]
Since
\[
e_{st}=sfs^{-1},\qquad e_se_{st}=e_{st},
\]
we have \(e_sz=z\), and hence
\[
sw=z,\qquad dw=w.
\]
Moreover,
\[
w=s^{-1}z=s^{-1}sfs^{-1}z=dfw.
\]
The idempotents \(d,f\) commute, so
\[
fw=fdfw=dfw=w.
\]
Thus \(w\in fS=e_tS\). By (3.6),
\[
\iota(z)=\bar q(s)\cdot\iota(w).
\]
Together with \(z\in e_sS\), this proves
\[
\iota(z)\in R_s\cap\bigl(\bar q(s)\cdot R_t\bigr).
\]

**Reverse inclusion.** Suppose
\[
\iota(z)=\bar q(s)\cdot\iota(x),
\qquad z\in e_sS,\quad x\in e_tS.
\]
Apply (3.6) to \(s^{-1}\) and \(z\), using \(e_sz=z\):
\[
\iota(s^{-1}z)
=\bar q(s)^{-1}\cdot\iota(z)
=\iota(x).
\]
Injectivity of \(\iota\) gives
\[
s^{-1}z=x.
\]
Therefore
\[
e_{st}z
=se_ts^{-1}z
=se_tx
=sx
=ss^{-1}z
=z.
\]
Hence \(z\in e_{st}S\), proving (3.9).

#### Step 4: the actual physical-host map

Define
\[
F:S\longrightarrow T(C,D),\qquad
F(s)=(R_s,q(s)).
\tag{3.10}
\]

This retains the prescribed actor **exactly**, not merely up to an unnamed isomorphism.

To check multiplication at the consuming host product, write
\[
q(s)=(i_0,h_s,\lambda_0).
\]
The twisting coefficient in (2.1) is
\[
h_sp=\rho(q(s))=\bar q(s).
\]
Thus (3.9) gives
\[
\begin{aligned}
F(s)F(t)
&=\left(R_s\cap(\bar q(s)\cdot R_t),q(s)q(t)\right)\\
&=(R_{st},q(st))\\
&=F(st).
\end{aligned}
\]
Therefore \(F\) is a homomorphism, and
\[
\pi_DF=q.
\]

Under the normalization (3.1), the entire host multiplication is
\[
(U,g)(V,h)=(U\cap gV,gh).
\tag{3.11}
\]
Associativity is also immediate directly:
\[
(U\cap gV)\cap ghW
=
U\cap g(V\cap hW).
\]

#### Step 5: source separation

Suppose \(F(s)=F(t)\). Then
\[
\bar q(s)=\bar q(t),\qquad R_s=R_t.
\]

Because \(\iota(e_s)\in R_s=R_t\), there is \(x\in e_tS\) with
\[
\iota(x)=\iota(e_s).
\]
Injectivity of \(\iota\) gives \(x=e_s\), so
\[
e_te_s=e_s.
\]
Interchanging \(s,t\) gives
\[
e_se_t=e_t.
\]
The idempotents commute; hence \(e_s=e_t\).

Finally,
\[
\iota(s^{-1})
=\bigl(\bar q(s)^{-1},e_s\bigr)
=\bigl(\bar q(t)^{-1},e_t\bigr)
=\iota(t^{-1}).
\]
Injectivity gives \(s^{-1}=t^{-1}\), and therefore \(s=t\).

This completes the embedding proof. ∎

### Consequences and scope

- The construction starts from \(S,q\), not from an assumed \(f:S\hookrightarrow T(B,A)\).
- It works for **every** prescribed onto pure \(q\) in the inverse-source class.
- If an unrelated initial embedding was already supplied, this construction still provides a source-only embedding over \(q\). It does not promise a map extending that supplied whole host.
- Every corner of \(C\) is a semilattice:
  \[
  UCU=\{V\cap U:V\subseteq X\}=\mathcal P(U).
  \]
  Thus local left-regular and local right-regular band identities hold.
- No undefined canonical, SN, RIGHTSN, free-band or Horn requirement is inferred from these explicit properties.

## 4. Exact extension criterion for the complete subgroup-host family

### Proposition 4.1

Let \(H\) be any group, \(K\leq H\) any subgroup, and
\[
q:K\overset{\cong}{\longrightarrow}G
\]
any group isomorphism.

Use the actual initial host
\[
T(\{*\},H)\cong H
\]
with the trivial action on the singleton band, and embed \(S=K\) by subgroup inclusion.

Then:

1. A homomorphism
   \[
   \phi:H\longrightarrow G,\qquad \phi|_K=q
   \]
   exists if and only if \(K\) is a retract of \(H\).
2. Such a matching extension can be idempotent-pure if and only if \(K=H\).
3. An actor-respecting embedding of this entire initial host over \(q\) exists if and only if \(K=H\).

### Proof

A matching extension gives a retraction
\[
\rho=q^{-1}\phi:H\longrightarrow K,\qquad \rho|_K=\operatorname{id}_K.
\]
Conversely, a retraction \(\rho\) gives the matching extension \(q\rho\). This proves part 1.

For group homomorphisms, idempotent purity is equivalent to trivial kernel, hence injectivity. A matching extension is onto because its restriction to \(K\) already maps onto \(G\). If it is also injective, then for any \(h\in H\), choose \(k\in K\) with
\[
q(k)=\phi(h).
\]
Since \(\phi(k)=q(k)\), injectivity gives \(h=k\). Thus \(H=K\).

Conversely, when \(H=K\), the map \(q\) itself is a pure extension. This proves part 2.

For part 3, an actor-respecting whole-host embedding forces its actor extension to be pure by projection purity and injectivity, as in §2. Part 2 then forces \(K=H\). When \(K=H\), the isomorphism \(q\) gives the required whole-host embedding using a singleton target band. ∎

This is an extension obstruction for a complete family, not another formulation of saturation/kernel inclusion. A proper subgroup can admit a nonpure extension when it is a retract, or no extension when it is not a retract. Neither possibility prevents embedding the source group \(K\) itself over its isomorphism \(q\).

## 5. Explicit finite counterexample: \(C_2\) inside \(C_4\)

All multiplication data are given here. Additive notation is used.

### 5.1 Initial actor

Let
\[
A=\mathbb Z/4\mathbb Z=\{0,1,2,3\}
\]
with multiplication given by addition modulo \(4\):

| \(+\) | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| **0** | 0 | 1 | 2 | 3 |
| **1** | 1 | 2 | 3 | 0 |
| **2** | 2 | 3 | 0 | 1 |
| **3** | 3 | 0 | 1 | 2 |

Inverses are \(0,3,2,1\), respectively. Its only idempotent is \(0\), since \(a+a=a\) implies \(a=0\).

Take the singleton band
\[
B=\{*\},\qquad **=*,
\]
with trivial \(A\)-action. The actor is the normalized one-row, one-column Rees matrix over \(C_4\), with sandwich entry \(0\) in additive notation. The physical product is exactly
\[
(*,a)(*,b)=(*,a+b).
\]

### 5.2 Source, prescribed quotient and initial embedding

Let
\[
S=\{0,2\}\subseteq A
\]
with inherited multiplication:

| \(+\) | 0 | 2 |
|---|---:|---:|
| **0** | 0 | 2 |
| **2** | 2 | 0 |

This is a group, hence a regular inverse semigroup. Its only idempotent is \(0\).

Let
\[
D=\mathbb Z/2\mathbb Z=\{0,1\}
\]
with table:

| \(+\) | 0 | 1 |
|---|---:|---:|
| **0** | 0 | 1 |
| **1** | 1 | 0 |

Its only idempotent is \(0\). Define
\[
q(0)=0,\qquad q(2)=1.
\]
The tables show that \(q\) is an onto homomorphism; it is an isomorphism. In particular,
\[
q^{-1}(E(D))=\{0\}=E(S),
\]
so it is idempotent-pure.

The actual initial embedding is
\[
f:S\hookrightarrow T(B,A),\qquad f(s)=(*,s).
\]
It is multiplicative and injective. Its actor map is
\[
r:S\hookrightarrow A,\qquad r(s)=s.
\]

Here,
\[
\ker r=\ker q=\Delta_S,
\]
so even equality of these kernels holds. However,
\[
r(S)=\{0,2\}\ne A.
\]

### 5.3 No matching actor extension exists

Suppose a homomorphism
\[
\phi:C_4\longrightarrow C_2
\]
satisfied \(\phi r=q\). Then
\[
\phi(2)=\phi(1+1)=\phi(1)+\phi(1)=0
\]
in \(C_2\). Matching \(q\) instead requires
\[
\phi(2)=q(2)=1.
\]
This is a contradiction.

Therefore:

- the well-defined pure homomorphism \(r(S)\to D\) does **not** extend to \(A\);
- no matching pure extension exists;
- no matching nonpure extension exists;
- no actor-respecting whole-host embedding over \(q\) exists.

This refutes the precise unrestricted premise:

> For every supplied initial physical-host embedding and every prescribed onto pure \(q\), the induced actor map on the source image extends to the entire initial actor.

It does **not** refute a separately defined canonical-actor theorem whose additional hypotheses have not been supplied.

### 5.4 Source-only embedding still exists

There is nevertheless the explicit embedding
\[
F_0:S\hookrightarrow T(\{*\},D),\qquad
F_0(s)=(*,q(s)).
\]
It is injective because \(q\) is an isomorphism, and its actor is exactly \(q\).

Thus this example does not convert an extension obstruction into an arbitrary-embedding no-go.

### 5.5 A whole cyclic family

For every pair of integers
\[
m\geq2,\qquad n\geq1,
\]
let
\[
H=\mathbb Z/(mn)\mathbb Z,\qquad
K=\{nk:k\in\mathbb Z/m\mathbb Z\},
\qquad
q(nk)=k.
\]
Multiplication in each group is addition modulo its stated modulus. The map \(q:K\to C_m\) is an isomorphism.

An extension \(\phi:H\to C_m\) is determined by \(a=\phi(1)\). Matching \(q\) is equivalent to
\[
na=1\pmod m.
\]
Hence a matching extension exists exactly when
\[
\gcd(n,m)=1.
\]
By Proposition 4.1, a matching pure extension exists exactly when \(n=1\).

This separates three cases:

- \(n=1\): a matching pure extension exists;
- \(n>1\) and \(\gcd(n,m)=1\): matching extensions exist but are nonpure;
- \(\gcd(n,m)>1\): no matching extension exists.

The fully tabulated \(C_4,C_2\) example is \(m=n=2\).

## 6. Negative controls and precise residual obligations

### 6.1 Purity cannot be omitted

Use the same two-element source group \(S=\{0,2\}\), but map it onto the trivial group:
\[
q_{\mathrm{triv}}(0)=q_{\mathrm{triv}}(2)=0.
\]
The target multiplication is the single equation \(0+0=0\).

This map is onto but not pure: the nonidempotent \(2\) maps to an idempotent. A physical host over the trivial group is just its band. An embedding of \(S\) over \(q_{\mathrm{triv}}\) would make the image of \(2\) idempotent, forcing \(2\) itself to be idempotent by injectivity. This contradicts the source table.

Correspondingly, the coordinate map (3.4) is no longer injective: both source elements have the same trivial group coordinate and the same domain idempotent.

### 6.2 An extension obstruction is not an embedding obstruction

Section 5.4 supplies an actual source-only embedding for the very example in which actor extension fails. No necessity claim about arbitrary embeddings is inferred from the earlier prescribed quotient/gauge family.

### 6.3 What is paid

At the displayed physical-host convention, the manuscript supplies written proofs of:

- initial-host existence for every inverse source admitting the prescribed onto pure \(q\);
- exact preservation of that prescribed actor map;
- the source-separation argument;
- a semilattice band, hence both local left-regular and local right-regular band identities;
- an exact matching-extension criterion for subgroup sources in singleton-band group hosts;
- an explicit finite counterexample to unrestricted actor extension from an arbitrary initial host.

### 6.4 What remains unpaid

1. **General regular sources.** The initial-host construction relies on inverse-semigroup structure. In particular, it uses the well-defined inverse \(x^{-1}\), commuting idempotents and the injectivity of (3.4). No substitute has been established for arbitrary regular sources.

2. **Non-group completely simple quotients of general regular sources.** Their row/column structure is not covered by Theorem 3.1. For inverse sources, the prescribed onto pure quotient was proved to be a group; this does not address the genuinely multirow/multicolumn regular-source case.

3. **Canonical or otherwise restricted initial actors.** The \(C_4\) example concerns a supplied arbitrary actual host. It does not establish failure of an undefined canonical construction.

4. **Additional host-admissibility definitions.** Explicit semilattice and corner properties are proved. Unspecified SN, RIGHTSN, canonical, Horn or free-band conditions are not certified.

5. **Book-source identity and Fact1.** No printed-problem authentication, Fact1 reconstruction or Q1 closure is claimed.

6. **Acceptance.** The proofs and finite tables require their separately assigned review and parent disposition before adoption. No machine replay was performed here.

The exact next general-source mathematical obligation is therefore an actual replacement for the inverse-source separation construction, or an actual counterexample to source embedding itself. A universal extension theorem for arbitrary preselected hosts cannot be used without additional hypotheses, because §5 disproves it.

## 7. Public attribution, execution status and chronology

### 7.1 Public prior context

No novelty claim is made. This inverse-source construction belongs in the classical setting of E-unitary inverse-semigroup representations.

The following primary publisher records were read:

- D. B. McAlister, **“E-unitary inverse semigroups over semilattices,”** *Glasgow Mathematical Journal* **19** (1978), 1–12, [DOI 10.1017/S0017089500003311](https://doi.org/10.1017/S0017089500003311). The publisher’s abstract describes the classical representation using a group acting on a partially ordered set with an ideal subsemilattice.
- D. B. McAlister and N. R. Reilly, **“E-unitary covers for inverse semigroups,”** *Pacific Journal of Mathematics* **68** (1977), 161–174, [publisher record and abstract](https://msp.org/pjm/1977/68-1/p18.xhtml), [DOI 10.2140/pjm.1977.68.161](https://doi.org/10.2140/pjm.1977.68.161). Its abstract discusses E-unitary covers, group images and the associated embedding problem.

These records support the historical attribution, not a claim that a particular theorem number or identical powerset formula was checked in their full proofs. PDF extraction did not expose the substantive proof pages. A separate attempted Margolis-paper fetch timed out. Search snippets and inaccessible proof pages are not mathematical premises.

Theorem 3.1 and Proposition 4.1 have therefore been proved in full above rather than imported through an unverified literature identification.

### 7.2 Proof versus experiment

All results in this return are **written mathematical derivations**. The finite tables are explicit mathematical inputs, not claimed executable output.

- No scientific code, interpreter, CAS, enumeration, solver or numerical calculation was executed.
- No tests, builds, lint, formatter or smoke run was performed.
- No experimental output or finite-machine verification is claimed.
- No external-model CLI, paid/heavy/remote calculation, installation, deletion, credential change, commit, push or publication occurred.

There is consequently no executed script, invocation or observed scientific stdout to report.

### 7.3 Actual read and derivation order

Before reading the scientific packet, I read:

- the required advisory memory summary and relevant procedural skills;
- the complete wave manifest and freeze receipt;
- the parent dispatch receipt and live-metadata supply;
- all seven named status/permission controls, through their endings.

The scientific packet was then read completely and in order in raw windows:

\[
1\!-\!270,\quad271\!-\!540,\quad541\!-\!805,\quad806\!-\!1028.
\]

This covered all of assigned S1, S2 and S3, including their endings. Mathematical development followed that complete-packet read. Public searches and primary publisher-record reads occurred afterward.

No excluded held scientific payload or linked out-of-scope predecessor body was followed. Assigned S3 was read because the manifest expressly included it.

### 7.4 Metadata attribution and delivery boundary

The manifest, receipt and packet pins are those reported in the supplied parent metadata:

- Manifest: `6e05e4591d8d003c129626d4367dd1b49aadf8ee216b3ba20334365baed42bd9`
- Receipt: `9854ed03ce660a2a2a1e2f7ef369aa4f519e4f06136581c9b275f757620eefb5`
- Packet: `25cd20096d8d1996bd02a668c9fb5d32ccba6d653e70dc7014dcac3bd50e9eab`

Their live hash/byte/LF agreement and the clock `2026-10-30T10:37:10-0700 PDT` are **parent observations**, not my own execution or native start measurement. No independent child hash or native timestamp is claimed.

The active tool-role restriction prohibited repository edits and scientific shell execution. No write bypass was attempted. This complete body is returned for Main materialization and later separate review.

**Final author status:** A complete initial-host theorem for the inverse-source class, an exact whole-family subgroup-host extension criterion, and a fully specified finite nonextension witness are supplied. The general regular-source target remains open; no original-target closure or acceptance is asserted.