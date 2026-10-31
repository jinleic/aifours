# F635 — Written review of source-image obstructions and graded purity

**Materialization:** This is the complete review body for parent materialization as `review-v1.md`. No repository file was created, and no filesystem-write workaround was attempted.

## 1. Scope, reading record, and process boundary

I read the following before sending the direct administrative pre-body ACK to Main:

- `manifest-v1.json`, LF 1–150;
- `freeze-receipt-v1.json`, LF 1–60;
- `parent-live-metadata-supply-v1.json`, through its closing line;
- the actual `dispatch-receipt-v1.json`, through its closing line;
- all fifteen manifest-listed status/permission controls, through their endings.

The manifest and freeze-receipt bindings were respectively:

- `e8d419361da0cba819a1a38078104891db42107ea90b1c6c259f61a55c83b10b`;
- `b5f137986126dab25fdcaf43c7b5066b0e553f6376eff958d0abb2a6a5d1848c`.

After delivery of that ACK, I read the entire literal packet in consecutive, ordered RAW windows of at most twenty LF: 1–20, 21–40, …, 241–260, and the final LF 261. All source endings were included. No elision or truncation marker appeared in those packet displays. Mathematical reconstruction began only after that complete read.

The packet binding is `3fdabf9907190c8653881ae90c765cba4f76b0e2e9bf5fa993b4fab8383c7473`, 261 LF. Hash, byte-count, source-stability, and freeze-order statements are attributed to the supplied parent metadata; I did not independently recompute them.

The mathematical inputs were exclusively the packet’s:

- **S1:** complete F628 author candidate, LF 1–161, SHA `800b1e704cae989bb1d189976829e0b4263be933b857423c481ef680ba6f5973`;
- **S2:** adopted source/COLL disposition, LF 1–57, SHA `7734d9f05396fc1e47f4d92bfa0ef82f4372eb9189b49fb76bd2406918aa0314`;
- **S3:** adopted regular-source actor disposition, LF 1–41, SHA `62babb5bd3bfccd57154373d1df082388747602f1f421b84310679ec8b3e80e4`.

I did not follow their links or access external papers, sibling reviews, author code, or held scientific payloads. Every held episode and **all** its consumers remained NONINPUT. No new selected mathematical instance was introduced. No scientific code, interpreter, CAS, solver, enumeration, replay, build, test, formatter, external-model CLI, installation, Git operation, or scientific network run was performed.

The historical access and execution account in S1 LF 7–11 remains author-reported provenance. Reading that account is not independent authentication of those historical events or a cognition certificate.

## 2. Claim dispositions

| Claim | Disposition | Evidence and qualification |
|---|---|---|
| The candidate uses exactly the frozen \(S=S_0/\theta\), with a semigroup congruence on \(S_0\), not an ambient-band replacement | **SUPPORTED** | S1 LF 15–35; S2 LF 7–19. Both new maps are constructed before factoring through \(\theta\). |
| The displayed six transformations form the stated associative six-element band | **SUPPORTED** | S1 LF 39–63; reconstructed below using the stated right-action convention. |
| The first map is onto the full twelve-element \(B\times C_2\), respects R1–R4, and preserves the pure grade | **SUPPORTED** | S1 LF 63–70. |
| \(E(S)\) satisfies the regular-band identity | **REFUTED** | The supplied source words \(efege\) and \(efge\) have distinct images \(A\) and \(Z\); S1 LF 60–78. |
| The free-band-with-zero construction gives an actual finite source image with \(a^3\ne a\) | **SUPPORTED** | S1 LF 88–101; no surjectivity onto the entire ambient semidirect product is needed or inferred. |
| \(S\) is completely regular | **REFUTED** | Every square in \(S\) is idempotent, whereas the second image distinguishes \(a^3\) from \(a\). |
| Every actual image \(T=\phi(S)\) is regular, has idempotent squares, and has \(E(T)=\phi(E(S))\) | **SUPPORTED** | S1 LF 35; square-lifting and regular inverses reconstructed below. |
| The grade-enriched image \(R\) has pure onto grade \(p\), \(E(R)\cong E(T)\), and least group quotient \(p\) | **SUPPORTED** | S1 LF 113–127. |
| A separating image must have a non-regular idempotent band | **SUPPORTED CONDITIONALLY** | S1 LF 111–129, conditional on the explicitly quoted Szendrei 1987 theorem and adopted COLL. |
| A separating image has at least three idempotents, and its enriched \(R\) has at least five elements | **SUPPORTED CONDITIONALLY** | S1 LF 131, with the same theorem-import dependency. The five-element bound is for \(R\), not automatically for ungraded \(T\). |
| No completely regular image with \(\mathcal H\) a congruence separates \(U,V\) | **SUPPORTED** | S1 LF 135–153, using adopted COLL and standard Green-class facts, without the 1987 theorem. |
| Either new source image separates \(U,V\) | **REFUTED** | The first identifies both with \((Z,1)\); the second identifies both with \((0,1)\). |
| SEP, or alternatively \(U=V\), in the original \(S_0/\theta\) | **INCONCLUSIVE / UNPAID** | Neither construction decides the designated pair in the original source. |
| Independent reconstruction of the full Szendrei 1987 proof or the eighty-primitive COLL certificate | **NOT RECONSTRUCTED** | These full proofs are not in this packet. Their exact imported interfaces are distinguished below. |

## 3. Exact source and import boundaries

The source is the subsemigroup \(S_0\) of \(F\rtimes C_2\) generated by the seven displayed elements, followed by the least **semigroup congruence on \(S_0\)** generated by exactly R1–R4. The named pair remains

\[
U=eafg,\qquad V=ebfa'eafg,\qquad q(U)=q(V)=1.
\]

No ambient-band contextual closure is substituted for that congruence.

I use the following frozen interfaces:

1. **Source interface — S2 LF 7–19.** The specified source is finite, regular, and has pure onto \(q:S\to C_2\). Its grade-zero elements are exactly its idempotents. The source inverse construction and free-band finiteness argument are imported at their stated scope.
2. **COLL interface — S2 LF 23–37.** Every homomorphism from this exact \(S\) into a band-by-\(C_2\) semidirect product **over \(q\)** identifies \(U,V\). The packet supplies the adopted disposition, not the complete eighty-primitive certificate; I do not claim a new replay of that certificate.
3. **Actor interface — S3 LF 7–9.** For a regular source with pure onto prescribed group quotient, an existing band-by-group embedding can be transported to the prescribed actor. The relevant transport argument is reconstructed below.
4. **External theorem interface — S1 LF 11 and 129.** The Szendrei 1987 statement is imported only as quoted from its **primary abstract**: an E-unitary regular semigroup whose idempotents form a regular band embeds into a band-by-group semidirect product. Neither its full proof nor a theorem page was independently read here. The secondary corroboration described by the author does not raise this assurance level.

The remaining material in S2/S3 is not given blanket new acceptance merely because those complete disposition bodies were read.

## 4. Six transformations, the twelve-element quotient, and source band failure

### 4.1 Multiplication convention and complete table

Use precisely the stated convention: \(xy\) means apply \(x\) first and \(y\) second.

Write \(P=\{p_0,p_E,p_F\}\). All six transformations fix `acc` and `rej`.

- \(I\) is the identity.
- \(E,F\) collapse \(P\) to \(p_E,p_F\), respectively.
- \(G\) sends \(p_E\) to `acc` and the other members of \(P\) to `rej`.
- \(A,Z\) collapse \(P\) to `acc`,`rej`, respectively.

The row rules reconstruct the entire supplied table:

- \(I\) acts as identity on either side.
- After \(E\), applying \(E,F,G,A,Z\) produces \(E,F,A,A,Z\).
- After \(F\), applying \(E,F,G,A,Z\) produces \(E,F,Z,A,Z\).
- The ranges of \(G,A,Z\) lie in \(\{\mathrm{acc},\mathrm{rej}\}\), which every displayed transformation fixes. Their rows are therefore constant at \(G,A,Z\), respectively.

Thus the table is closed and agrees with the actual transformations. Associativity follows from transformation composition, not from an unchecked table assertion. Each diagonal entry is its row label, so all six elements are idempotent. The transformation descriptions distinguish all six maps. Consequently \(B\) is the stated six-element band with identity.

In particular,

\[
EFEGE=FEGE=EGE=AE=A,
\]
whereas
\[
EFGE=FGE=ZE=Z.
\]

Since \(A\ne Z\), this is a genuine failure of \(xyxzx=xyzx\).

Here “non-regular band” means failure of the **regular-band variety identity**. It does not mean that the band’s elements fail semigroup regularity.

### 4.2 Genuine factorization through the source

The ten-letter map sends both members of each swapped pair to the same element of \(B\). It is therefore equivariant for the trivial involution on \(B\), and induces a homomorphism

\[
F\rtimes C_2\longrightarrow B\times C_2.
\]

Restrict it to the actual \(S_0\) before considering \(\theta\). Its generator images are those in S1 LF 70.

All four source relations lie in its kernel:

- R1 and R2 have first-coordinate equality \(E=E\).
- R3 has first-coordinate equality \(FG=FG\).
- R4 has first-coordinate equality \(FEFG=FEFG\).

Each pair has grade zero. Therefore the kernel contains the least four-pair semigroup congruence on \(S_0\), giving a well-defined map from exactly \(S\). No extra ambient-band congruence has been imposed.

The map is onto the whole \(B\times C_2\):

- \(a^2\) supplies \((I,0)\), and \(a\) supplies \((I,1)\);
- \(e,f,g\) supply the grade-zero copies of \(E,F,G\);
- \(eg,fg\) supply the grade-zero copies of \(A,Z\);
- multiplication by \((I,1)\) supplies the corresponding grade-one elements.

For every \((x,h)\in B\times C_2\),

\[
(x,h)^2=(x,0),\qquad (x,h)^3=(x,h).
\]

Thus each element is its own regular inverse. The grade projection is onto and is idempotent-pure, because \((x,h)\) is idempotent exactly when \(h=0\).

### 4.3 What this proves, and what it does not

The source elements \(e,f,g\) are idempotents. Their displayed words map to the distinct grade-zero elements \((A,0)\) and \((Z,0)\). Hence

\[
efege\ne efge\quad\text{in the original }S.
\]

This proves \(E(S)\) is not a regular band, independently of SEP and independently of the external embedding theorem.

For the designated pair,

\[
\phi(U)=(EFG,1)=(Z,1),
\]
and
\[
\phi(V)=(EFEFG,1)=(Z,1).
\]

**This twelve-element source image is NONSEPARATING.** Its source-band obstruction is valid, but it does not prove either equality or inequality of \(U,V\) in the original source.

## 5. Free-band-with-zero image and failure of complete regularity

The second model uses the free band on \(x,y\), with a distinct absorbing zero adjoined. The frozen free-band finiteness argument, including the stated representative bound \(L_2=6\), makes this a finite band. Swapping \(x,y\) and fixing zero gives the required involution.

The ten-letter assignment is equivariant. It therefore induces a homomorphism from \(F\rtimes C_2\), which is restricted to \(S_0\). Every side of R1–R4 contains a letter mapped to zero. Since the involution fixes zero and zero is absorbing, both first coordinates in every pair are zero; their grades are zero. The map consequently factors through the actual \(S\).

This does **not** require the image to equal the entire ambient \(D\rtimes C_2\). I make no such surjectivity claim.

For the supplied element \(a\),

\[
\phi(a)=(x,1),\qquad
\phi(a^2)=(xy,0),\qquad
\phi(a^3)=(xyx,1).
\]

Free-band square insertion/removal preserves letter content, including in context. The words \(xyx\) and \(x\) have different content, so they represent distinct elements. Adjoining a new zero does not identify them. Therefore \(a^3\ne a\) in the original \(S\).

Because \(q(s^2)=0\) and \(q\) is pure, every square in \(S\) is idempotent. If \(a\) belonged to a subgroup, its idempotent square would be that subgroup’s identity, forcing \(a^3=a\). Thus \(S\) cannot be a union of groups: it is not completely regular.

This does not contradict the imported **regularity** of \(S\); regularity and complete regularity are different properties.

Both \(U,V\) contain zero-mapped letters and retain grade one, so

\[
\phi(U)=\phi(V)=(0,1).
\]

**This second finite source image is also NONSEPARATING.**

## 6. Arbitrary source images and the grade-enriched image

Let \(T=\phi(S)\), replacing any ambient codomain by the actual image.

### 6.1 Regularity, idempotent squares, and square-lifting

A regular inverse of \(s\) maps to a regular inverse of \(\phi(s)\), so \(T\) is regular.

Every \(t=\phi(s)\) has idempotent square because \(s^2\) is idempotent. In particular, if \(t\) itself is idempotent, then

\[
t=t^2=\phi(s^2),
\]

with \(s^2\in E(S)\). This proves the nontrivial inclusion in

\[
E(T)=\phi(E(S)).
\]

The reverse inclusion follows from preservation of idempotence. Since \(E(S)\) is a band, its image is a band. Thus \(T\) is orthodox.

This argument is specific and sufficient; it does not assume unrestricted idempotent lifting for arbitrary semigroup quotients.

### 6.2 Why the grade must be retained explicitly

The map \(q\) need not descend to the ungraded image \(T\). The candidate correctly uses

\[
\lambda:S\to T\times C_2,\qquad
\lambda(s)=(\phi(s),q(s)),
\]
and sets \(R=\lambda(S)\).

It is an actual semigroup image, hence regular. Its projection \(p:R\to C_2\) is onto.

A grade-zero member has a grade-zero source representative, which is idempotent. Conversely an idempotent in \(R\) must have grade zero. Hence \(p\) is pure.

Furthermore,

\[
E(R)=\{(t,0):t\in E(T)\}.
\]

For the reverse inclusion, the square-lifting argument provides a representative \(s^2\) mapping to each idempotent \(t\), with grade zero. The identification \(t\mapsto(t,0)\) preserves multiplication and is a band isomorphism.

### 6.3 Least group quotient

Let \(\alpha:R\to H\) be any homomorphism to a group. Suppose \(p(r)=p(t)\), and choose a regular inverse \(r'\) of \(r\).

The inverse equations give

\[
p(r')=p(r)^{-1},\qquad
\alpha(r')=\alpha(r)^{-1}.
\]

Thus \(p(r't)=0\), so purity makes \(r't\) idempotent. Its group image is the identity:

\[
1=\alpha(r't)=\alpha(r)^{-1}\alpha(t).
\]

Therefore \(\alpha(r)=\alpha(t)\). Every group homomorphism factors through \(p\); because \(p\) is itself an onto group homomorphism, its kernel is exactly the least group congruence.

Consequently the canonical least group quotient is pure. This supplies the E-unitary condition in the least-group-quotient convention used by the imported theorem.

## 7. Actor transport, COLL consumption, and the conditional regular-band exclusion

Suppose \(E(T)\) satisfies the regular-band identity. The preceding band isomorphism makes \(E(R)\) a regular band.

**Conditional on the quoted Szendrei 1987 theorem**, there is an embedding

\[
j:R\hookrightarrow K\rtimes H.
\]

Its group projection \(\alpha\) factors as \(\beta p\) by the least-group result. The factor \(\beta:C_2\to H\) cannot be trivial: otherwise \(j(R)\) would lie entirely in the band \(K\times\{1\}\), forcing every element of \(R\) to be idempotent, contrary to its onto pure grade.

A nontrivial homomorphism from \(C_2\) is injective. Restricting the action to \(\beta(C_2)\) and identifying that subgroup with \(C_2\) therefore transports this embedding to a band-by-\(C_2\) embedding over exactly \(p\). Composing with \(\lambda\) gives a homomorphism out of the original \(S\) over exactly \(q\).

This is the consuming interface required by COLL. In particular, for a host map \(H(s)=(k_s,q(s))\), the evaluation

\[
(h,s)\longmapsto h\cdot k_s
\]

respects the typed cocycle relation because the host multiplication gives

\[
k_{st}=k_s\bigl(q(s)\cdot k_t\bigr).
\]

It respects all nonempty word-square relations because the receiving first-coordinate semigroup is a band. Thus the adopted universal collision applies to the composed map and identifies the images of \(U,V\).

Injectivity of \(j\) then forces

\[
(\phi(U),1)=(\phi(V),1).
\]

Therefore a separating \(\phi\) cannot have regular-band \(E(T)\), subject to the stated external theorem import.

This transport only restricts the acting subgroup and changes its identification. It does not require or construct an extension \(H\to C_2\) on the entire original host group.

### Bounds and degenerate cases

The regular-band law holds whenever two of its three variables coincide:

- if \(y=x\), both sides reduce to \(xzx\);
- if \(z=x\), both reduce to \(xyx\);
- if \(z=y\), the left side is \((xy)^2x=xyx\), and the right side is \(xy^2x=xyx\).

Hence a failure requires three distinct idempotents. A separating \(T\) therefore has at least three idempotents, conditionally on the exclusion just proved.

The corresponding \(R\) contains their three distinct grade-zero copies and the two distinct grade-one elements \((\phi(U),1),(\phi(V),1)\). Thus \(|R|\ge5\).

These are necessary bounds, not existence or feasibility claims. In particular, the argument does not establish \(|T|\ge5\), because the ungraded first-coordinate image can forget grade distinctions.

## 8. Direct exclusion of completely regular images with congruence \(\mathcal H\)

This proof does not use the 1987 embedding theorem.

Assume \(T=\phi(S)\) is completely regular and its Green relation \(\mathcal H\) is a semigroup congruence.

Every \(t^2\) is idempotent. In the subgroup containing \(t\), it is therefore the identity, and \(t^3=t\). In particular \(t\mathrel{\mathcal H}t^2\).

For \(t,u\in T\), congruence compatibility gives

\[
tu\mathrel{\mathcal H}t^2u^2.
\]

The latter element is idempotent because \(E(T)\) is a band. Complete regularity puts \((tu)^2\) in the same \(\mathcal H\)-class as \(tu\), and it too is idempotent. The standard uniqueness of an idempotent in an \(\mathcal H\)-class gives

\[
(tu)^2=t^2u^2.
\]

Consequently

\[
\Psi:R\to E(T)\times C_2,\qquad
\Psi(t,h)=(t^2,h)
\]

is a homomorphism over \(p\).

It is injective:

- Different grades are distinguished by the second coordinate.
- At grade zero, purity makes \(t\) idempotent, so \(t^2=t\).
- At grade one, suppose \(t^2=u^2=e\). Complete regularity puts \(t,u\) in the same maximal subgroup with identity \(e\). Since \((tu,0)\in R\), purity makes \(tu\) idempotent. Within that subgroup, \(tu=e\). Using \(t^2=e\),
  \[
  u=t^2u=t(tu)=te=t.
  \]

This covers the same-grade fibers without inverse uniqueness in the whole semigroup or commuting idempotents.

The composite \(\Psi\lambda\) is a homomorphism from the original \(S\) into a band-by-\(C_2\) direct product over \(q\). COLL identifies its values on \(U,V\); injectivity of \(\Psi\) then yields \(\phi(U)=\phi(V)\).

The stated rectangular-group and Clifford-semigroup cases fall within this exclusion: their maximal-group \(\mathcal H\)-classes form a congruence, with rectangular-band and semilattice quotients respectively. The proof does **not** silently remove the \(\mathcal H\)-congruence hypothesis or claim the same argument for every completely regular orthodox image.

## 9. Acceptance boundary and remaining obligation

The following are supported at this review’s reconstructed scope:

1. The exact original source has the displayed regular-band identity failure in its idempotent band.
2. The exact original source satisfies \(a^3\ne a\), and therefore is not completely regular.
3. Every actual homomorphic image is regular and orthodox, with idempotent squares and the stated square-lifting property.
4. The grade-enriched construction, its pure least group quotient, and the required actor transport are valid.
5. The regular-band separator exclusion and its bounds follow **conditionally** on the explicitly imported 1987 theorem and adopted COLL.
6. The completely-regular-plus-\(\mathcal H\)-congruence exclusion follows from adopted COLL and the stated standard Green-class facts, without the 1987 theorem.

**Both newly constructed source images are NONSEPARATING.** Neither supplies SEP, and their identification of the pair does not prove \(U=V\) in the original source.

The exact unpaid obligation remains to decide the pair in **this** \(S_0/\theta\): either a genuine separating homomorphism/invariant or a valid source-congruence derivation of equality. A proposed finite separator must preserve the source-first, semigroup-congruence construction and establish the actual carrier, multiplication, relations, grade, regular inverses, and separated pair. Necessary search filters do not replace that obligation.

No partial **D8** data are promoted to a whole-band certificate; no such certificate is supplied or reconstructed here. No unreviewed **deficit-six** result is imported, relied upon, or implicitly adopted.

This review does not establish original-target closure, an all-host nonembedding witness, identity with either published 1998 construction, novelty, independent-family or human acceptance, or formal/kernel verification. Parent adoption is separate.

## 10. Findings and verdict

**Findings:** None at the reconstructed scope.

**FATAL: 0. MAJOR: 0. MINOR: 0.**

The unreconstructed external proof and adopted-certificate boundaries are explicit limitations, not defects concealed by an unconditional acceptance.

**Overall correctness:** correct

**Explanation:** The two source maps, image/grade arguments, conditional regular-band exclusion, and direct completely-regular-\(\mathcal H\)-congruence exclusion are valid at the candidate’s stated import boundaries. Both new images identify \(U,V\), so SEP and the broader original target remain unresolved.

**Confidence:** 0.97