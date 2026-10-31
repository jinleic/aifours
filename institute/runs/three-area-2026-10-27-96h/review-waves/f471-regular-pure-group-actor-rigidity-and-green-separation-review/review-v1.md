# f471 WRITTEN review — Pure group-actor rigidity and Green-coordinate separation

**Result:** **SUPPORTED at the stated mathematical scopes.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR** affecting those conclusions.  
**Acceptance status:** Reviewer support only; parent disposition remains required. This return does not close the original general regular-source, canonical-host, printed-source, SN/RIGHTSN or Q1 target.

## 1. Inputs, coverage and execution boundary

The frozen wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f471-regular-pure-group-actor-rigidity-and-green-separation-review/`

The following metadata is **parent-supplied**, not an independently executed child hash or clock check:

- Manifest SHA256: `c78d48a252e1747119e035778fe2149d0a3bdca99a92be02e9303f59325f619a`
- Freeze-receipt SHA256: `f22749c0fcd5fb2a4b9239e33cd6289c1991c2e0e60f88d84460c1824d4bcbd3`
- Literal-packet SHA256: `710861a140b145a61addebce757850fd0fee580387d27a064a39e6c3de6ecbea`
- Parent observation: `2026-10-30T12:05:56-0700 PDT`
- Parent reports that the assigned pins, bytes and LF counts match.

Before reading the mathematical packet, I read the manifest, freeze receipt, parent-live metadata supply and all ten named controls through their endings. Those controls were used only for their permission, status and exclusion boundaries. I sent the administrative pre-body ACK to Main before opening the mathematical packet.

I then read the complete literal packet in consecutive raw windows:

- `1–20`, `21–40`, continuing consecutively through `701–720`;
- final window `721–722`.

Every window contained at most twenty requested lines. The observed source endings were **S1:676**, **S2:31** and **S3:13**. No omitted mathematical packet section remains.

Source labels below refer to the frozen packet:

- **S1:** f462 author candidate, SHA256 `320d839ce753b7291e94ecd0cc36eb9c89263e5e9b46eb2bd50a477969d9f58e`.
- **S2:** inverse-source parent disposition, SHA256 `7ccee47da6fd66773c7da5e054eef2fa9df872bf066366cf40b77e483d4b50db`.
- **S3:** arbitrary-host extension disposition, SHA256 `7a327b17dbe39aa652ef9ea9f0a79812e75791700246968f33062b2a8a359a46`.

This was a written reconstruction using the frozen formal parameters and explicit author instances. No scientific program, interpreter, CAS, solver, enumeration, replay, build, test, lint or formatter was executed. No new concrete diagnostic instance, external mathematical source, sibling review, author code or held scientific payload was used. No external-model CLI was invoked.

No child-native start clock, independent hash computation, finite execution or machine-checked result is claimed. Under the active read-only restriction, no repository write was attempted; this is the complete body for parent materialization.

## 2. Claim-by-claim disposition

| Claim | Frozen location | Disposition |
|---|---|---|
| The physical projection of a band semidirect product onto its group actor is idempotent-pure | S1:71–82 | **SUPPORTED** |
| Identifying all idempotents of a nonempty regular semigroup produces its least group quotient | S1:88–116 | **SUPPORTED** |
| Every pure onto group quotient of that source has this same kernel | S1:118–141 | **SUPPORTED** |
| An actual embedding with any group actor can be transported to the exact prescribed pure onto actor | S1:147–207 | **SUPPORTED** |
| This transport does not require an extension from the unused part of the original actor group | S1:209–213; S3:5–13 | **SUPPORTED** |
| The prescribed group image together with the actual Green \(\mathcal R\)- and \(\mathcal L\)-classes separates the source | S1:219–272 | **SUPPORTED** |
| The presented \(C_q\) has a genuine action and the stated conditional universal embedding criterion | S1:276–404 | **SUPPORTED**, without automatic injectivity |
| The unit-regular monoid theorem gives the displayed full physical-host isomorphism | S1:416–495 | **SUPPORTED** |
| The six-element example and proper-embedding boundary control have the stated properties | S1:499–557 | **SUPPORTED** by their displayed definitions |
| The one-row Rees normalization uses \(hp\) at the consuming twist and preserves literal \(q\) | S1:561–593 | **SUPPORTED** |
| The public-source reading history and exact literature comparisons are independently authenticated by this review | S1:599–613 | **INCONCLUSIVE**; those external texts were not assigned as literal inputs |
| An unconditional general regular-source host, a self-contained all-host counterexample, or original-target closure has been established | S1:626–637,676 | **NOT ESTABLISHED**, consistently with the author’s exclusions |

No mathematical claim is classified **REFUTED** in this return.

## 3. Physical projection and the intrinsic group quotient

### 3.1 Physical purity

For a band \(B\) acted on by a group \(H\),

\[
(b,h)(c,k)=\bigl(b(h\cdot c),hk\bigr).
\]

If \((b,h)\) is idempotent, its actor coordinate satisfies \(h^2=h\), hence \(h=1\). Conversely,

\[
(b,1)^2=(b^2,1)=(b,1).
\]

Thus

\[
E(B\rtimes H)=B\times\{1\}.
\]

For an **injective** homomorphism \(j:S\to B\rtimes H\), write \(r=\pi_Hj\). If \(r(s)=1\), then \(j(s)\) is idempotent, so

\[
j(s^2)=j(s)^2=j(s).
\]

Injectivity gives \(s^2=s\). Every idempotent of \(S\) also maps to \(1\) under the group-valued \(r\). Consequently,

\[
r^{-1}(1)=E(S).
\]

This establishes the precise purity assertion used later. It does not assume that \(r\) is onto \(H\).

### 3.2 The quotient by all idempotent pairs is a group

Let \(S\) be nonempty and regular, and let \(\sigma\) be the congruence generated by every pair of idempotents.

Regularity supplies, for each \(s\), an inverse \(s'\) satisfying

\[
ss's=s,\qquad s'ss'=s'.
\]

Both \(ss'\) and \(s's\) are idempotent. In particular, idempotents exist, and they have a common \(\sigma\)-class \(\varepsilon\).

In the quotient,

\[
[s][s']=[ss']=\varepsilon=[s's]=[s'][s].
\]

The identity calculations are

\[
\varepsilon[s]=[ss'][s]=[ss's]=[s],
\]

and

\[
[s]\varepsilon=[s][s's]=[ss's]=[s].
\]

Therefore \(\varepsilon\) is a two-sided identity and every quotient element has a two-sided inverse. Hence \(S/\sigma\) is a group.

Any homomorphism from \(S\) to a group sends every idempotent to that group’s identity. Its kernel congruence therefore contains all the generating pairs of \(\sigma\), and hence contains \(\sigma\). This proves leastness, not merely existence of a group quotient.

### 3.3 Purity forces equality of kernels

For the prescribed onto pure map \(q:S\twoheadrightarrow G\), leastness gives a well-defined surjective group homomorphism

\[
\bar q:S/\sigma\twoheadrightarrow G,\qquad \bar q([s])=q(s).
\]

If \(\bar q([s])=1\), then \(q(s)=1\). Purity gives \(s\in E(S)\), so \([s]=\varepsilon\). Thus \(\bar q\) has trivial group kernel and is an isomorphism. Consequently,

\[
\ker q=\sigma.
\]

For two pure onto quotients \(q_1,q_2\), equality of their kernel congruences makes

\[
\theta(q_1(s))=q_2(s)
\]

well-defined. It is multiplicative and bijective, and surjectivity of \(q_1\) gives uniqueness. No inverse uniqueness, finite cardinality argument or commutativity of source idempotents is used.

## 4. Transport of an actual source embedding

Assume an actual embedding

\[
j:S\hookrightarrow B\rtimes H,\qquad j(s)=(b_s,r(s)).
\]

The preceding physical-projection argument proves purity of \(r\).

### 4.1 The actor image is a subgroup

Set \(K=r(S)\). Multiplicative closure follows from the homomorphism property.

For an inverse \(s'\) of \(s\), applying \(r\) to \(ss's=s\) and cancelling in \(H\) gives

\[
r(s')=r(s)^{-1}.
\]

Also \(r(ss')=1\). Nonemptiness and regularity therefore ensure that \(K\) contains the identity and inverses of all its elements. It is a subgroup of \(H\), not merely a subsemigroup.

Viewed as a map onto \(K\), \(r\) is pure and onto. The intrinsic quotient theorem gives

\[
\ker r=\sigma=\ker q.
\]

Thus there is a unique isomorphism

\[
\theta:G\overset{\cong}{\longrightarrow}K,
\qquad
\theta(q(s))=r(s).
\]

### 4.2 The transported action is consumed correctly

Restrict the original \(H\)-action on \(B\) to \(K\), and define

\[
g\star b=\theta(g)\cdot_H b.
\]

Because \(\theta\) is a group homomorphism and the original action is by band automorphisms, this is a \(G\)-action by band automorphisms.

Define

\[
F(s)=(b_s,q(s)).
\]

The actual target multiplication receives the new action through

\[
\begin{aligned}
F(s)F(t)
&=\bigl(b_s(q(s)\star b_t),q(s)q(t)\bigr)\\
&=\bigl(b_s(\theta(q(s))\cdot_H b_t),q(st)\bigr)\\
&=\bigl(b_s(r(s)\cdot_H b_t),q(st)\bigr)\\
&=(b_{st},q(st))\\
&=F(st).
\end{aligned}
\]

The fourth equality is exactly the band-coordinate equality supplied by the original homomorphism \(j\).

If \(F(s)=F(t)\), then \(b_s=b_t\) and \(q(s)=q(t)\). Applying \(\theta\) gives \(r(s)=r(t)\), hence \(j(s)=j(t)\). Injectivity of \(j\) gives \(s=t\).

Thus the construction preserves:

- the original band \(B\);
- every existing band coordinate \(b_s\);
- actual source multiplication;
- source injectivity;
- the literal prescribed actor projection \(\pi_GF=q\).

It does **not** preserve or extend all of the original host \(B\rtimes H\). Its relevant intermediate host is \(B\rtimes K\).

## 5. Why this does not contradict the whole-host obstruction

The distinction in S3 is substantive.

For a group \(H\), subgroup \(K\le H\) and isomorphism \(q:K\to G\), a homomorphism \(\phi:H\to G\) extending \(q\) corresponds exactly to a retraction

\[
q^{-1}\phi:H\to K.
\]

Conversely, composing a retraction \(H\to K\) with \(q\) gives such an extension.

If this extension is pure, it is injective, because a group has only its identity as an idempotent. It is also onto, since it extends the onto map \(q\). For any \(h\in H\), choose \(k\in K\) with \(q(k)=\phi(h)\). Then

\[
\phi(h)=\phi(k),
\]

so injectivity forces \(h=k\). Therefore purity of an extension forces \(K=H\). The converse is immediate.

The explicit frozen \(C_4\) example has

\[
K=\{0,2\},\qquad q(0)=0,\qquad q(2)=1\in C_2.
\]

For a homomorphism \(\phi:C_4\to C_2\),

\[
\phi(2)=2\phi(1)=0,
\]

so it cannot extend \(q\). Nevertheless the source itself embeds over \(q\) into the singleton-band host with actor \(C_2\).

The new transport theorem does precisely the latter kind of source construction: it restricts to the image actor and transports its action. It never asks for the impossible extension \(\phi:C_4\to C_2\).

Likewise, in the frozen cyclic family, writing \(\phi(1)=a\) makes the extension condition

\[
na=1\pmod m.
\]

This is solvable exactly when \(\gcd(n,m)=1\). Purity additionally forces \(K=H\), equivalently \(n=1\). These are whole-host extension conclusions, not all-host source-embedding obstructions.

## 6. Green-coordinate separation

Assume

\[
s\mathrel{\mathcal R}t,\qquad
s\mathrel{\mathcal L}t,\qquad
q(s)=q(t).
\]

Choose an arbitrary inverse \(s'\) of \(s\), and set

\[
e=s's,\qquad a=s't.
\]

The group images satisfy

\[
q(s')=q(s)^{-1},
\]

so

\[
q(a)=q(s)^{-1}q(t)=1.
\]

Purity gives \(a^2=a\).

The actual Green relations supply \(u,v,w\in S^1\) such that

\[
t=su,\qquad s=tv,\qquad t=ws.
\]

No evaluation of \(q\) on these \(S^1\)-multipliers is required.

First,

\[
av=s'tv=s's=e.
\]

Second, \(se=ss's=s\), so the left Green relation gives

\[
te=wse=ws=t.
\]

Consequently,

\[
ae=s'te=s't=a.
\]

But \(e=av\) and \(a^2=a\) also give

\[
ae=a(av)=a^2v=av=e.
\]

Thus \(a=e\).

Finally, the right Green relation gives the needed left-identity calculation:

\[
ss't=ss'su=su=t.
\]

It follows that

\[
t=ss't=sa=se=s.
\]

The proof therefore establishes injectivity of

\[
s\longmapsto\bigl(q(s),[s]_{\mathcal R},[s]_{\mathcal L}\bigr)
\]

for the entire stated regular-source class.

The identity orientations matter and are correct:

- \(e=s's\) is used as a **right** identity for \(s\);
- \(s\mathrel{\mathcal L}t\) transports that right-identity property to \(t\);
- \(ss'\) is used as a **left** identity for \(t\), through \(s\mathrel{\mathcal R}t\).

Nothing requires \(es=s\), a unique inverse, commuting idempotents, cancellation in \(S\), or an identity in \(S\).

This remains a separation theorem. It does not equip the Green-class coordinates with the required global band multiplication and group action.

## 7. The universal band construction is genuinely conditional

The presentation in S1:276–404 is mathematically well-defined.

The quotient of nonempty words over \(G\times S\) by all relations \(ww\equiv_q w\) is a nonempty band. Imposing the additional cocycle relations does not change that conclusion.

Left translation

\[
(g,s)\longmapsto(hg,s)
\]

preserves the word-square relations and sends a cocycle relation to

\[
(hg,st)\equiv_q(hg,s)(hgq(s),t).
\]

It therefore induces an automorphism of the quotient, with inverse induced by translation by \(h^{-1}\). Composition has the asserted order \(L_hL_k=L_{hk}\).

For \(c_s=[(1,s)]\), the defining relation yields

\[
c_{st}=c_s\bigl(q(s)\cdot c_t\bigr).
\]

Thus \(\eta_q(s)=(c_s,q(s))\) really is a homomorphism into the physical semidirect product.

For another homomorphism \(H(s)=(b_s,q(s))\), evaluation of a letter by

\[
(g,s)\longmapsto g\cdot b_s
\]

respects word-square relations because the target is a band. It respects the cocycle relations because

\[
g\cdot b_{st}
=(g\cdot b_s)\bigl(gq(s)\cdot b_t\bigr).
\]

This proves the factorization and equivariance. Uniqueness follows because the translated \(c_s\) generate the quotient.

Consequently, condition (6.6) is exactly injectivity of \(\eta_q\), and every embedding over \(q\) forces that condition through the universal factorization.

A finite same-\(q\) generator collision would obstruct every such band host. The transport theorem would then extend that obstruction to every group actor for the regular source. However, no collision is produced here, and no automatic injectivity is established.

In particular, the Green separation theorem does not discharge condition (6.6). The missing connection must not be silently supplied.

## 8. Unit-regular theorem and the explicit author examples

### 8.1 Full unit-regular realization

For the monoid theorem, an element of \(\ker(q|_{U(M)})\) is both a unit and an idempotent, hence is \(1_M\). Thus the restriction is injective.

If \(q(U(M))=G\), its inverse \(g\mapsto u_g\) satisfies

\[
u_gu_h=u_{gh}.
\]

For \(g=q(s)\), purity gives

\[
e_s=su_g^{-1}\in E(M),
\qquad
s=e_su_g.
\]

Conversely, \(M=E(M)U(M)\) and surjectivity of \(q\) imply \(q(U(M))=G\).

The equivalence with unit-regularity is also explicit:

\[
s=eu \quad\Longrightarrow\quad su^{-1}s=s,
\]

while

\[
svs=s,\quad v\in U(M)
\quad\Longrightarrow\quad
(sv)^2=sv,\quad s=(sv)v^{-1}.
\]

Purity makes \(E(M)\) a band. Conjugation by \(u_g\) preserves its multiplication and has the stated inverse, producing the action \(\alpha_g\).

Writing \(s=e_su_g\) and \(t=e_tu_h\),

\[
st=e_s\alpha_g(e_t)u_{gh}.
\]

Therefore

\[
F(s)F(t)
=\bigl(e_s\alpha_g(e_t),gh\bigr)
=F(st).
\]

The displayed inverse \((e,g)\mapsto eu_g\) verifies bijectivity and exact preservation of \(q\). This proves the stated unit-regular class theorem without commuting-idempotent assumptions.

### 8.2 Six-element example

The explicit action on the author’s band fixes \(\mathbf1\) and swaps \(a,b\). It preserves the left-zero multiplication on \(\{a,b\}\) and the identity, so the semidirect product is associative.

The complete displayed table follows from two rules:

- a left factor whose band coordinate is \(a\) or \(b\) retains that band coordinate;
- a left factor with band coordinate \(\mathbf1\) applies its group action to the right band coordinate.

Together with addition of the \(C_2\)-coordinate, these give all six printed rows.

The zero actor fibre consists exactly of \(I,a,b\), which are exactly the idempotents. The stated inverse choices establish regularity. The equations \(xyx=x\), \(yxy=y\) and \(x^3=x\) give distinct inverses of \(x\), so inverse uniqueness fails.

The displayed equation

\[
tat^{-1}=b\ne a
\]

shows a nontrivial action. It also rules out an isomorphism to a band–group direct product: in such a monoid direct product every unit commutes with every idempotent, whereas this conjugation does not fix \(a\).

For the explicit submonoid \(N\) with trivial action, the four elements with band coordinate in \(\{a,b\}\) form a proper ideal. They cannot be units. Projection is nevertheless pure and onto, and the displayed inclusion already supplies the proper source embedding. Thus failure of unit surjectivity is not a general source-embedding obstruction.

These are checks of the author’s explicit instances, not a new selected finite experiment.

## 9. Literal one-row Rees normalization

For

\[
D=M[G;\{i_0\},\{\lambda_0\};p],
\]

the actor product is

\[
(i_0,h,\lambda_0)(i_0,k,\lambda_0)
=(i_0,hpk,\lambda_0).
\]

The selected normalization

\[
\rho(i_0,h,\lambda_0)=hp
\]

satisfies

\[
\rho(hpk)=hpkp=(hp)(kp),
\]

so it is a group isomorphism.

More importantly, it is exactly the normalization received by the supplied physical multiplication. If

\[
q(s)=(i_0,h_s,\lambda_0),
\]

then the consuming twist is

\[
h_sp=\bar q(s).
\]

Returning the actor coordinate as the original \(q(s)\), rather than replacing it by \(\bar q(s)\), therefore gives

\[
F_D(s)F_D(t)
=\bigl(c_s(\bar q(s)\cdot c_t),q(st)\bigr)
=F_D(st).
\]

No exchange of \(p\) with another group element occurs. Noncentral sandwich entries do not invalidate the calculation.

This is a one-row, one-column conclusion. Neither the group-actor transport theorem nor this normalization replaces a genuinely multirow or multicolumn completely simple actor. The singleton-index conclusion in the inverse-source disposition uses commuting source idempotents; that premise is not available for arbitrary regular sources.

## 10. Imports and remaining obligations

The least-group-quotient, actor-transport and Green-separation arguments above are self-contained. They do not import the reported Billhardt nonembedding theorem, a canonical free-band theorem, a regular-band representation theorem or any unread external proof.

The public-source section remains an author-attributed reading and literature report. This role did not independently access those sources, and the report must not be upgraded here to an independently authenticated theorem identification or a reconstructed negative witness.

The following remain unpaid:

1. Proving injectivity of the universal \(\eta_q\) for the full regular class.
2. Alternatively, supplying an explicit regular pure-\(q\) source and a proved distinct same-\(q\) generator collision.
3. Constructing a host for every regular source outside the proved classes.
4. Extending an embedding from an entire arbitrary supplied host.
5. Handling genuinely multirow or multicolumn prescribed completely simple actors by the group-actor argument.
6. Establishing any additional canonical-host, SN, RIGHTSN, Horn or admissibility requirement.
7. Printed-source/Fact1 authentication, Q1 closure, novelty, independent-family or human review, and formal/kernel verification.

No actual finite gate was executed by this WRITTEN role. The separate finite duty is neither replaced nor certified by the displayed hand reconstructions.

## Verdict

**Overall correctness: correct at the audited written scopes.**

The intrinsic pure group quotient, exact actor transport and Green-coordinate separation are supported by the complete frozen proofs, including their consuming multiplication and identity orientations. The conditional universal criterion, unit-regular realization and explicit author examples are also consistent with their stated boundaries; none establishes unconditional general regular-source host existence or original-target closure.

**Confidence: 0.98.**