# review-v1.md — f326 actor transport

**Status: UNREVIEWED AUTHOR CANDIDATE.** The statements below are universal written derivations at the supplied \(T(B,D)\) model. They are not peer acceptance, an original embedding theorem, or a literature claim.

**Result.** A genuinely sufficient actor-transport condition is obtained: the actor map of the given embedding must admit an **idempotent-pure homomorphic extension to the whole host actor**. This condition is also necessary for an actor-respecting embedding of the whole host. The proof constructs the new group action and an actual embedding, retaining row/column information in a rectangular-band factor.

For a possibly nonpure actor extension, a second construction gives an exact action-descent and source-fibre criterion within the specified quotient/gauge transport family.

## 1. Inputs and notation

The mathematical inputs are the source definition and explicit host convention in packet **S1|9 and S1|16**, together with the unresolved obligation in **S1|20**. Nothing from Fact1, canonical-host definitions, the Horn criterion, or source-match is used; their unverified status in **S1|22** is retained.

Write the arbitrary host actor and prescribed source actor as
\[
A=M[H;J,\Omega;P],\qquad
D=M[G;I,\Lambda;Q].
\]
Thus the packet’s sandwich matrix for \(D\) is renamed \(Q\).

Let \(B\) be a nonempty band on which \(H\) acts by automorphisms. In the supplied convention,
\[
(b,(j,h,\mu))(c,(k,t,\nu))
=
\bigl(b\,((hP_{\mu k})\cdot c),
      (j,hP_{\mu k}t,\nu)\bigr).
\]

Suppose a host embedding is already given:
\[
f:S\hookrightarrow T(B,A),\qquad
f(s)=(b_s,r(s)),\qquad
r(s)=(j_s,h_s,\mu_s),
\]
and \(q:S\to D\) is the prescribed onto idempotent-pure homomorphism. Existence of \(f\) is a hypothesis, not a conclusion.

All indices and group elements below are arbitrary variables. No particular semigroup or selected instance is examined.

## 2. A preliminary purity calculation

For \(x=(j,h,\mu)\in A\),
\[
x^2=x
\iff hP_{\mu j}=1.
\]
When this holds, the twisting coefficient in \((b,x)^2\) is \(1\), so
\[
(b,x)^2=(b^2,x)=(b,x).
\]
Conversely, an idempotent \((b,x)\) has idempotent actor \(x\). Consequently,
\[
\pi_A^{-1}(E(A))=E(T(B,A)).
\tag{1}
\]
The same calculation applies to every target \(T(C,D)\).

Thus the host projections are idempotent-pure directly from the supplied definitions.

**Claim A1: SUPPORTED by the displayed calculation.**

## 3. Universal sufficient condition, with a stronger equivalence

### Proposition A — pure actor extension gives full transport

A sufficient condition for transporting the given source embedding to actor \(q\) is the existence of an idempotent-pure homomorphism
\[
\phi:A\longrightarrow D,\qquad \phi r=q.
\tag{2}
\]

More precisely, the following are equivalent:

1. There are a \(G\)-band \(C\), an embedding
   \[
   F:T(B,A)\hookrightarrow T(C,D),
   \]
   and an actor homomorphism \(\phi:A\to D\), such that
   \[
   \pi_DF=\phi\pi_A,\qquad \phi r=q.
   \tag{3}
   \]
2. There is an idempotent-pure homomorphism \(\phi\) satisfying (2).
3. There are maps
   \[
   \alpha:J\to I,\qquad \beta:\Omega\to\Lambda,
   \]
   elements \(u_j,v_\mu\in G\), and a **group isomorphism**
   \[
   \eta:H\overset{\cong}{\longrightarrow}G
   \]
   satisfying
   \[
   \eta(P_{\mu k})
   =
   v_\mu Q_{\beta(\mu),\alpha(k)}u_k
   \quad(\mu\in\Omega,\ k\in J),
   \tag{4}
   \]
   and
   \[
   q(s)=
   \bigl(\alpha(j_s),u_{j_s}\eta(h_s)v_{\mu_s},
                    \beta(\mu_s)\bigr)
   \quad(s\in S).
   \tag{5}
   \]

Condition 1 is a **stronger full-host transport**, not a definition imposed on every possible source-only transport. Its construction is therefore sufficient for the requested source transport.

### Proof: necessity of purity

Assume condition 1. Since \(q=\phi r\) is onto, \(\phi\) is onto.

If \(\phi(a)\) is idempotent, then \(F(b,a)\) has idempotent actor for every \(b\in B\). By (1), \(F(b,a)\) is idempotent. Injectivity and multiplicativity of \(F\) imply
\[
(b,a)^2=(b,a),
\]
so \(a\) is idempotent. Hence \(\phi\) is idempotent-pure.

This proves \(1\Rightarrow2\). In particular, a nonpure extension cannot support an actor-respecting embedding of the **whole** host.

### Proof: coordinate form, without importing a Rees-homomorphism theorem

The coordinate form needed here follows from the definitions.

In a completely simple Rees matrix semigroup, \(\mathcal R\)-classes are determined by row and \(\mathcal L\)-classes by column, as follows by solving the group-coordinate equations for multiplication witnesses. A homomorphism preserves those witnesses. Therefore the row and column of \(\phi(j,h,\mu)\) depend only on \(j\) and \(\mu\); denote them by \(\alpha(j)\) and \(\beta(\mu)\).

Fix arbitrary reference indices \(j_0,\mu_0\), and put
\[
p_0=P_{\mu_0j_0}.
\]
The map
\[
\tau(h)=(j_0,p_0^{-1}h,\mu_0)
\]
identifies \(H\) with the maximal subgroup at
\((j_0,p_0^{-1},\mu_0)\). Its image under \(\phi\) is a group at the image idempotent. Writing
\[
q_0=Q_{\beta(\mu_0),\alpha(j_0)},
\]
there is a group homomorphism \(\eta:H\to G\) such that
\[
\phi(\tau(h))
=
\bigl(\alpha(j_0),q_0^{-1}\eta(h),\beta(\mu_0)\bigr).
\]

Every actor element has the symbolic decomposition
\[
(j,h,\mu)
=
(j,1,\mu_0)\,\tau(h)\,(j_0,p_0^{-1},\mu).
\]
Applying \(\phi\) gives elements \(u_j,v_\mu\in G\) with
\[
\phi(j,h,\mu)
=
\bigl(\alpha(j),u_j\eta(h)v_\mu,\beta(\mu)\bigr).
\tag{6}
\]
Comparing \(\phi(xy)\) and \(\phi(x)\phi(y)\), and cancelling group factors, gives exactly (4).

Two additional facts are needed:

**Purity.** From (4) and (6),
\[
\phi(j,h,\mu)\in E(D)
\iff
\eta(hP_{\mu j})=1.
\tag{7}
\]
The original element is idempotent exactly when \(hP_{\mu j}=1\). Since \(hP_{\mu j}\) ranges over all of \(H\), (7) shows
\[
\phi\text{ is idempotent-pure}
\iff
\eta\text{ is injective}.
\tag{8}
\]

**Surjectivity.** If \(\phi\) is onto, then \(\eta\) is onto. To see this, put \(K=\eta(H)\). Equation (4) implies
\[
\alpha(j)=\alpha(k)\ \Longrightarrow\ u_j^{-1}u_k\in K,
\]
and
\[
\beta(\mu)=\beta(\nu)\ \Longrightarrow\ v_\nu v_\mu^{-1}\in K.
\]
Thus all preimages of the target row \(\alpha(j_0)\) and column \(\beta(\mu_0)\) have group coordinates in the single set
\[
u_{j_0}K v_{\mu_0}.
\]
Onto-ness of \(\phi\) forces this set to equal \(G\), and therefore \(K=G\).

Consequently an onto, idempotent-pure \(\phi\) yields an isomorphism \(\eta\), proving \(2\Rightarrow3\). Conversely, (4) defines a homomorphism by (6), and an isomorphism \(\eta\) makes it pure by (7).

### Proof: explicit action, band and embedding

Assume condition 3. Relabel the original action using \(\eta\):
\[
g\star b=\eta^{-1}(g)\cdot b.
\]
This is a \(G\)-action by band automorphisms.

Let
\[
R=J\times\Omega,\qquad
(j,\mu)(k,\nu)=(j,\nu),
\]
be the rectangular band, and put
\[
C=B\times R.
\]
Let \(G\) act by
\[
g\star(b,(j,\mu))=(g\star b,(j,\mu)).
\]

Define
\[
F(b,(j,h,\mu))
=
\left(
  (u_j\star b,(j,\mu)),
  (\alpha(j),u_j\eta(h)v_\mu,\beta(\mu))
\right).
\tag{9}
\]

The row and column labels in \(R\) are essential information retained by this construction; they are not discarded by actor factorization.

For \(x=(j,h,\mu)\) and \(y=(k,t,\nu)\), the target twisting coefficient is
\[
\begin{aligned}
w_D(\phi(x),\phi(y))
&=u_j\eta(h)v_\mu
          Q_{\beta(\mu),\alpha(k)}\\
&=u_j\eta(hP_{\mu k})u_k^{-1},
\end{aligned}
\tag{10}
\]
using (4). Therefore the \(B\)-coordinate of \(F(b,x)F(c,y)\) is
\[
\begin{aligned}
&(u_j\star b)\,
 \Bigl(
 [u_j\eta(hP_{\mu k})u_k^{-1}]
       \star(u_k\star c)
 \Bigr)\\
&\qquad
=u_j\star\bigl(b\,((hP_{\mu k})\cdot c)\bigr).
\end{aligned}
\]
Its rectangular coordinate is \((j,\nu)\), and its actor is \(\phi(xy)\). These are precisely the coordinates of \(F((b,x)(c,y))\). Thus \(F\) is a homomorphism.

If two values of (9) are equal, the rectangular coordinates first give
\[
j=k,\qquad \mu=\nu.
\]
Actor equality then gives \(\eta(h)=\eta(t)\), hence \(h=t\). Equality of the band coordinates gives \(b=c\), since the \(u_j\)-action is invertible. Thus \(F\) is injective.

Finally,
\[
\pi_DFf=\phi r=q.
\]
This proves \(3\Rightarrow1\) and establishes Proposition A.

The source’s purity is retained because its actor map is exactly \(q\); the target projection is independently pure by (1). This is an actual embedding, not just a factorization of actor maps.

**Claim A2: SUPPORTED by the complete construction and proof above.**

### Local-band preservation

The added rectangular factor does not change local-monoid types. For
\(e=(b,(j,\mu))\in C\),
\[
eCe
=
\{(bxb,(j,\mu)):x\in B\}
\cong bBb.
\tag{11}
\]
Hence any host restriction expressed solely by the relevant local-monoid properties is preserved. In particular, locally left-regular or locally right-regular band conditions are preserved.

This does **not** certify undefined additional SN/RIGHTSN or canonical-host requirements.

## 4. An important sufficient corollary: actor-saturated hosts

Assume additionally that
\[
r(S)=A.
\tag{12}
\]

Then
\[
\ker r\subseteq\ker q
\tag{13}
\]
is equivalent to the existence of the full-host transport in Proposition A.

Indeed, (13) defines the unique onto homomorphism
\[
\phi(r(s))=q(s).
\]
It is pure: if \(\phi(a)\) is idempotent, choose \(s\) with \(r(s)=a\). Then \(q(s)\) is idempotent, so purity of \(q\) gives \(s^2=s\), and therefore \(a^2=a\). Proposition A now supplies the action, sandwich compatibility and embedding. Necessity of (13) follows from \(q=\phi r\).

Thus kernel inclusion becomes sufficient **under actor saturation and after the full construction**, not merely by naming an actor factorization.

**Claim A3: SUPPORTED at the additional hypothesis (12).** Actor saturation is not supplied by the frozen packet and is not assumed for its arbitrary host.

## 5. Source-only transport through a possibly nonpure extension

The preceding condition is sufficient, but not asserted necessary for an embedding of \(S\) alone. The following gives an exact alternative within a specified compatible transport family.

Suppose a homomorphism \(\phi:A\to D\) satisfying \(\phi r=q\) is supplied, without assuming it pure. Its coordinate data still satisfy (4) and (6), and \(\eta\) is onto because \(\phi\) is onto.

Set
\[
N=\ker\eta.
\]
Let \(\theta\) be the least \(H\)-invariant band congruence on \(B\) containing
\[
(b,n\cdot b)\qquad(b\in B,\ n\in N).
\tag{14}
\]
The quotient \(\overline B=B/\theta\) carries a well-defined \(G\)-action:
\[
\eta(h)\star[b]=[h\cdot b].
\tag{15}
\]
For two lifts of the same element of \(G\), their difference lies in \(N\); (14) and \(H\)-invariance make their values in (15) equal. Each induced map is a band automorphism.

Put
\[
C_\theta=\overline B\times R.
\]
The same calculation as (10) proves that
\[
F_\theta(b,(j,h,\mu))
=
\left(
 (u_j\star[b],(j,\mu)),
 \phi(j,h,\mu)
\right)
\tag{16}
\]
is a homomorphism.

Its restriction to the source is injective **if and only if**
\[
\boxed{
\begin{gathered}
q(s)=q(t),\qquad j_s=j_t,\qquad \mu_s=\mu_t,\\
b_s\mathrel{\theta}b_t
\quad\Longrightarrow\quad s=t.
\end{gathered}}
\tag{17}
\]
This follows by comparing the three coordinates of (16); when \(j_s=j_t\), the common \(u_j\)-action is invertible.

Condition (17) is an explicit source-fibre condition on the canonical action-collapse congruence. Purity of \(q\) does not by itself establish it.

### Why this is a genuine obstruction for the specified family

Let \(C'\) be any \(G\)-band and
\(\gamma:B\to C'\) any band homomorphism satisfying
\[
\gamma(h\cdot b)=\eta(h)\cdot\gamma(b).
\tag{18}
\]
For \(n\in N\), equation (18) gives
\(\gamma(n\cdot b)=\gamma(b)\). Moreover \(\ker\gamma\) is \(H\)-invariant. Hence
\[
\theta\subseteq\ker\gamma,
\]
and \(\gamma\) factors uniquely through a \(G\)-equivariant band homomorphism
\[
\overline\gamma:\overline B\to C'.
\]

Consequently every transport of the compatible form
\[
(b,(j,h,\mu))
\longmapsto
\left(
 (u_j\cdot\gamma(b),(j,\mu)),
 \phi(j,h,\mu)
\right)
\tag{19}
\]
factors through (16). If distinct source elements violate (17), every map (19) identifies them. Conversely, if (17) holds, (16) supplies the required source embedding.

Thus (17) is necessary and sufficient within this entire equivariant band-map, row/column-memory, prescribed-\(\phi\) transport family. It is **not** an impossibility result for unrelated constructions or for embeddings not induced by this family.

**Claim A4: SUPPORTED at this explicitly bounded scope.**

## 6. Exact remaining obligation for the frozen M1

For a general nonsaturated host, kernel inclusion only defines
\[
r(S)\longrightarrow D,\qquad r(s)\longmapsto q(s).
\]
It does not establish an extension to all of \(A\).

The missing inputs are now explicit:

- **Full-host route:** an idempotent-pure homomorphism
  \(\phi:A\to D\) with \(\phi r=q\). Proposition A proves this condition is both necessary and sufficient for the stronger actor-respecting full-host transport.
- **Prescribed nonpure-extension route:** a homomorphism \(\phi\) matching \(q\), followed by the action-descent quotient (14) and the source-fibre separation condition (17). These are sufficient, and exact within family (19).
- Any additional host-admissibility condition not specified by the supplied \(T(B,D)\) model remains a separate obligation. Equation (11) pays local-monoid preservation for Proposition A; it does not verify unnamed canonical or Horn conditions.

**Claim A5: INCONCLUSIVE for unconditional M1.** The packet does not establish either missing route for every arbitrary host. Treating the original canonical-actor equivalence as proved would still have a **MAJOR load-bearing gap** at **S1|20**. No FATAL finding or mathematical refutation of the adopted structural reductions is asserted.

The deliverable is the proved conditional bridge and exact bounded obstruction above. Fact1 and original source-match remain nonpremises.

---

# reviewer-process-v1.md — full process return

- **Observed native checkpoints:**  
  2026-10-30T07:48:00-0700 PDT;  
  2026-10-30T07:56:56-0700 PDT;  
  2026-10-30T07:58:47-0700 PDT;  
  2026-10-30T08:00:50-0700 PDT.  
  These are actual `/bin/date` observations, not reconstructed creation or event times.

- **Pre-body order:** Read manifest LF1–64, freeze receipt LF1–34, and all five status-only controls completely in raw windows of at most 20 LF. Attempted own-wave `reviewer-prebody-ack-v1.md`; the filesystem write was refused. Immediately sent the administrative PRE-BODY ACK directly to `agent://Main`; the tool returned **“Delivered to Main.”** Mathematical packet reads occurred only afterward.

- **Pinned metadata:** Live hashes matched:
  - Manifest: `2f5122ee9f5ae599672a8510c44ba472167b721b3db8912e4f0aa3cfe06fa132`
  - Freeze receipt: `0664b5616494a196ce75f83fbb9118f048dc8bd3dc644222ea3bbcfe16eccd46`
  - Literal packet: `2ffa7cfbdd97f43cc59a7a065b1455c1e9756b99e17cc5fa32b00827068748b4`
  - Whole source: `63546947083781f1b7743eb656026f0c8bf2e94c4e3bfdbd7b6849d6bcd764f8`
  - All five status-control hashes matched the manifest.

- **Mathematical read coverage:** Complete packet LF1–24, read raw as LF1–20 and LF21–24, including its ending. This supplied S1 LF1–22. No elision was observed. Source LF23–34 was not accessed; whole-source hashing was metadata only.

- **Exposure and execution:** No excluded link, held payload, prior reviewer body, sibling mathematical output, or literature source was followed. Memory summary and relevant protocol skills were read for process only. No selected mathematical instance, scientific code, CAS, solver, enumeration, replay, test, build, lint, formatter, external-model CLI, or paid/heavy work was used. Shell activity was confined to native clock and hash metadata commands.

- **Publication status:** The attempted own-wave process-file write was also refused by the xd/local-only transport. No alternate-path or shell-write bypass was attempted. No own-wave file was created by these attempts. The complete candidate and process texts are returned above for parent materialization. The refusal is administrative transport status, not scientific disqualification.

- **Acceptance status:** UNREVIEWED AUTHOR CANDIDATE only. No independent written gate, peer acceptance, Fact1 verification, source-match verification, or original-target closure is claimed.