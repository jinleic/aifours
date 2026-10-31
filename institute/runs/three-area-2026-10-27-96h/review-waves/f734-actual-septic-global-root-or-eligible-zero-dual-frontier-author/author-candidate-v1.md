# F734 author candidate: eight-atom zero dual and two-parity backtracking

**Status: AUTHOR-WRITTEN, UNADOPTED; original universal common-SPR/ROOT/DUAL problem NOT PROVED and no eligible counterexample supplied.** The substantive candidate is a universal necessary structure for a same-box zero dual: at least six distinct finite frequencies, an at-most-eight-atom compactified representation, and an oppositely directed sign reversal in each of two disjoint physical parity-uncertainty bands. A zero dual with at least four finite frequency groups can be converted, with those same groups, into an all-eight-strict-negative aggregate in any eligible constant/linear buffered enlargement. These are written claims requiring the parent's independent complete read and disposition. They do not establish that a zero dual actually exists or that the reversal constraints are impossible.

Native clock observed before composing this file: `2026-10-30T17:13:57-0700 PDT`. This observation is not a file creation timestamp or a claim about earlier cognition.

## 1. Original scope, eligibility, and imported boundary

Let
\[
 K=\{a(s)=s^7+\sum_{j=0}^6a_js^j:\ell_j\le a_j\le u_j\}
\]
be one nonempty compact **independent** real coefficient box, including degenerate intervals. For \(t=\omega^2\), write
\[
 E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\quad
 O_a(t)=a_1-a_3t+a_5t^2-t^3,
\]
\[
 r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
An **eligible** K means that every actual member is strictly Hurwitz, not merely that corners are stable. The exact eligibility import S1/S4 says: the actual center b is Hurwitz, \(\ell_0>0\), and there is no \(t>0\) for which both \(E_b(t)^2\le H_E(t)^2\) and \(O_b(t)^2\le H_O(t)^2\), with
\[
 H_E=h_0+h_2t+h_4t^2+h_6t^3,\qquad
 H_O=h_1+h_3t+h_5t^2,\qquad h_j=(u_j-\ell_j)/2.
\]
This includes equality, tangencies, and zero widths. Independence makes the actual pair at each t the complete rectangle \([E_-,E_+]\times[O_-,O_+]\), with four fixed actual corner polynomials \(C_{\sigma\tau}\), and makes each actual row a same-frequency convex combination of their rows. It does not make K the convex hull of four polynomials.

The original target asks for ONE monic stable Q for all actual members and frequencies. I import S1/S4's exact same-box equivalence between this strict common-SPR property and
\[
 0\notin \operatorname{conv}\{r_{C_{\sigma\tau}}(t)/(1+t)^7:
 \sigma,\tau\in\{-,+\},\;0\le t\le\infty\}.
\]
At zero the compactified row is \(a_0 e_0\), and at infinity it is \(e_7\). I also import, at the S3 scope, the earlier result there excluding an all-eight-strict-negative actual-member aggregate on an eligible box when it uses at most five distinct positive finite squared frequencies. This is an explicit load-bearing import, not a theorem whose original proof I inspected. The ordinary Hermite--Biehler interlacing theorem for a strictly Hurwitz real septic and elementary interpolation/separation are used below.

## 2. Main candidate: eight compactified atoms, at least six finite frequencies

**Theorem A.** For every eligible K:

1. In any finite same-box zero-dual representation
   \[
   \sum_{j=1}^{m}w_jr_{C_j}(t_j)+\lambda e_0+\mu e_7=0,
   \quad w_j,t_j>0,\quad \lambda,\mu\ge0,                 \tag{A}
   \]
   there are at least six **distinct** finite \(t_j\). Repeated physical corners at one t count as one frequency. At least one finite atom is required.
2. If a zero dual exists, one exists with
   \[
       m+\mathbf1_{\lambda>0}+\mathbf1_{\mu>0}\le8,       \tag{B}
   \]
   and hence with six, seven, or eight distinct finite frequencies. All finite atoms remain actual physical four-corner rows. This improves the nine-atom Carathéodory count stated in S1, conditional on this new proof.
3. If either the whole even or the whole odd coefficient parity is fixed, no same-box zero dual exists, so strict common-SPR holds there by the imported zero-hull alternative. This fixed-parity corollary is independently derived here only to establish the boundary of the genuinely both-parity case; prior fixed-parity results are already recorded in the packet, and no novelty is asserted.

### 2.1. Grouping and a two-coordinate steering identity

Combine all finite atoms in (A) with the same \(t=u_i\). Let their total raw weight be \(W_i>0\), and let \(a_i\in K\) be the corresponding weighted average of actual corners. Convexity of the independent box makes \(a_i\) an actual member, and linearity gives the identical raw aggregate \(\sum_iW_i r_{a_i}(u_i)\). Let there be n distinct groups.

Suppose \(n\ge4\), and choose any four of them with distinct positive nodes, denoted again by \(u_1,\ldots,u_4\), with weights \(W_i\). Set
\[
 L_i(x)=\prod_{j\ne i}\frac{x-u_j}{u_i-u_j},\qquad
 \delta a_{0,i}=-\epsilon\frac{L_i(-1)}{W_i},\qquad
 \delta a_{1,i}=-\epsilon\frac{L_i(-1)}{W_i u_i}.        \tag{C}
\]
Leave the other five coefficients and all unselected groups unchanged. Lagrange interpolation gives
\(\sum_i L_i(-1)u_i^k=(-1)^k\) for \(0\le k\le3\). Therefore, **exactly**, the eight-coordinate change in the finite raw aggregate is
\[
 (-\epsilon,-\epsilon,-\epsilon,-\epsilon,
  -\epsilon,-\epsilon,-\epsilon,-\epsilon).             \tag{D}
\]
No asymptotic or solver calculation is involved. If L is any eligible enlargement of K with a strictly positive buffer in each of the constant and linear coefficient intervals, all changes (C) lie in L for sufficiently small \(\epsilon>0\): the finitely many changes are linear in epsilon, and each original selected member belongs to K. The new finite aggregate is consequently
\[
 (-\lambda-\epsilon,-\epsilon,-\epsilon,-\epsilon,
  -\epsilon,-\epsilon,-\epsilon,-\mu-\epsilon),          \tag{E}
\]
all strictly negative, on exactly the original n finite frequencies and actual members of L. The newly selected members need not be corner members. Compactness of an eligible K and openness of strict Hurwitz stability guarantee that sufficiently small positive two-coordinate buffers exist; the assertion also applies to any such buffer already known eligible. This is a conditional implication from an actual zero dual, not a supplied obstruction.

For comparison, if the four selected grouped members already have enough independent constant and linear slack inside K, the same calculation stays inside K. Thus such a zero dual would yield a same-box strict-negative aggregate. This does **not** establish same-box weak-to-strict synthesis in general.

### 2.2. Why at least six distinct finite frequencies

For \(1\le n\le3\), no buffer or imported five-frequency result is needed. With the grouped actual members, choose a real polynomial \(F\) of degree at most three with \(F(0)=1\) and \(F(u_i)=E_{a_i}(u_i)\). Independently choose
\(G(t)=-t^3+H(t)\), with \(\deg H\le n-1\), so that \(G(u_i)=O_{a_i}(u_i)\). These are the even and odd parts of a real monic coefficient vector q, with \(q_0=q_7=1\); q is only a test vector and is not asserted Hurwitz. Pairing q with (A) yields
\[
 0=\sum_i W_i\big(E_{a_i}(u_i)^2+u_iO_{a_i}(u_i)^2\big)+\lambda+\mu>0.
\]
The strict inequality holds because every grouped \(a_i\) is an actual eligible member and cannot vanish on the imaginary axis. With no finite groups, the nonnegative endpoint terms alone cannot form a nontrivial zero combination.

For \(n=4\) or 5, choose an eligible two-coordinate buffer L. Formulae (C)--(E) give an actual-member all-eight-strict-negative aggregate in L at those same n frequencies, contradicting the **imported** S3 at-most-five-frequency no-go. Thus every representation (A), including those with endpoint atoms and those with many corner atoms at one frequency, has \(n\ge6\).

### 2.3. Why eight rather than nine compactified atoms suffice

Let S be the union of the four normalized physical corner curves, including both endpoint limits. Each curve is continuous on \([0,\infty]\); all four share the point \(e_7\) at infinity. Thus S is compact and path connected. Starting from any convex representation of 0, ordinary Carathéodory gives at most nine points in \(\mathbb R^8\). If nine are needed in that representation, take affinely independent \(p_0,\ldots,p_8\in S\) and strictly positive barycentric coefficients \(\alpha_i\).

For completeness, here is the connected-set reduction. Take a continuous path \(p(s)\in S\) from \(p_0\) to \(p_1\), and express it in the fixed affine coordinates \(p(s)=\sum_i c_i(s)p_i\), \(\sum_i c_i(s)=1\). Before the first time \(c_0\) reaches zero,
\[
 0=\frac{\alpha_0}{c_0(s)}p(s)+
 \sum_{i=1}^8\left(\alpha_i-\frac{\alpha_0c_i(s)}{c_0(s)}\right)p_i.
\]
At the start all coefficients are positive. At the first zero of \(c_0\), at least one other \(c_i\) is positive because their sum is one; just before that time its displayed coefficient is negative. By continuity, a first coefficient among \(i=1,\ldots,8\) reaches zero while all the others are nonnegative. This gives a convex representation using the path point and at most seven of \(p_1,\ldots,p_8\). If an earlier Carathéodory representation had fewer than nine points or a zero coefficient, it already satisfies the bound.

Convert any finite normalized weight \(\alpha\) to the raw weight \(\alpha/(1+t)^7\). Combine all zero-endpoint contributions into \(\lambda e_0\) and all infinity contributions into \(\mu e_7\). Since every actual constant coefficient is positive, each positive \(\lambda e_0\) is a positive multiple of an actual zero-endpoint row. This gives (A)--(B). Conversely any nontrivial (A) normalizes back to a convex representation of 0 using those actual endpoint rows. The endpoints are not discarded and no rationality of a zero-dual frequency is claimed.

In particular, if the eight-atom representation has exactly six distinct finite frequencies and \(z=\mathbf1_{\lambda>0}+\mathbf1_{\mu>0}\), then at most \(2-z\) of the six groups can contain multiple finite corner atoms. At least \(4+z\) groups are single actual-corner rows; when both endpoints occur, all six are single. This is a statement about the chosen sparse representation, not about every original witness.

### 2.4. Fixed-parity exclusion, directly from the zero dual

If the odd parity is fixed, \(O_a=O_b\) for all a. Test (A) with the coefficient vector having even part zero and odd part \(G=O_b\). Every finite pairing is \(tO_b^2\ge0\); the infinity pairing is 1 and the zero-endpoint pairing is 0. Equality forces \(\mu=0\) and every finite group to satisfy \(O_b(u_i)=0\). At such a node eligibility and the full parity rectangle force the entire actual E interval to avoid zero, with the same sign as \(E_b\). Testing instead with even part \(F=E_b\), odd part zero, gives strictly positive finite pairings \(E_bE_{a_i}\), plus the nonnegative endpoint term \(\lambda b_0\), a contradiction.

If the even parity is fixed, first use the test \(F=E_b,G=0\). Its finite pairings are \(E_b^2\ge0\), its zero-endpoint pairing is \(b_0>0\), and its infinity pairing is 0. Equality forces \(\lambda=0\) and \(E_b(u_i)=0\) at every finite group. Eligibility forces every actual O value there to have the nonzero sign of \(O_b\). The test \(F=0,G=O_b\) then gives strictly positive \(u_i O_bO_{a_i}\) at every finite group and a nonnegative infinity term, contradiction. These tests are not required to be stable or coefficientwise nonnegative.

## 3. Main candidate: necessary backtracking in BOTH physical parities

A zero-dual eligible K must have at least one nondegenerate even and one nondegenerate odd coefficient interval, by Section 2.4. Consequently \(H_E(t),H_O(t)>0\) for every \(t>0\). There are three closed actual even-uncertainty bands \(I^E_1,I^E_2,I^E_3\), where \(E_-\le0\le E_+\), and three analogous odd bands \(I^O_1,I^O_2,I^O_3\), where \(O_-\le0\le O_+\). Their endpoints are roots of the **actual** envelope polynomials, not arbitrary chosen markers.

The Hermite--Biehler theorem applied to the eligible center gives positive simple center roots in the order
\[
 e_1<o_1<e_2<o_2<e_3<o_3,
\]
where the e's are roots of \(E_b\) and the o's of \(O_b\). Applying the same interlacing to the two actual even-endpoint polynomials with odd coefficients fixed at the center gives exactly one zero of each even envelope in each of \((0,o_1),(o_1,o_2),(o_2,o_3)\). Since \(E_-<E_+\) at positive t, their order produces three disjoint even bands, containing \(e_1,e_2,e_3\). The analogous odd construction, also imported in S3, produces the three disjoint odd bands containing \(o_1,o_2,o_3\). If any even band met any odd band, independence would realize \(E=O=0\) at that same t, contradicting exact eligibility. Hence, as closed intervals,
\[
 I^E_1<I^O_1<I^E_2<I^O_2<I^E_3<I^O_3.              \tag{F}
\]
Here \(I<J\) means every point of I is strictly smaller than every point of J. For each parity separately, the certain signs outside its three bands run \(+,-,+,-\) as t increases. At the first and third bands the baseline change is \(+\to-\); at the second it is \(-\to+\).

**Theorem B.** Group any actual zero dual as above. Write \(E_i=E_{a_i}(u_i)\) and \(O_i=O_{a_i}(u_i)\), with the distinct nodes in increasing order. For **each** parity separately, there must be two distinct nodes \(u_i<u_j\) in one and the same actual uncertainty band with opposite signs in the *reverse* direction:

* in band 1 or 3: its parity values satisfy \(V_i<0<V_j\);
* in band 2: its parity values satisfy \(V_i>0>V_j\).

Use \(V=E\) for an even band and \(V=O\) for an odd band. By (F), the required even and odd pairs lie in disjoint bands, so they comprise at least four distinct physical frequencies. The values are those of the actual grouped member at each node; a group can mix corner atoms. No claim is made that the same two nodes work for both parities, or that either reversal is sufficient for a dual.

### 3.1. Exact signed moments and endpoint effects

Set
\[
 X_i=W_iE_i,\qquad Y_i=W_i u_i O_i.
\]
The eight coordinates of (A) give precisely
\[
 \sum_iX_i=-\lambda,\quad \sum_iX_i u_i^k=0\ (k=1,2,3);\qquad
 \sum_iY_i u_i^k=0\ (k=0,1,2),\quad
 \sum_iY_i u_i^3=\mu.                                  \tag{G}
\]
Thus the infinity atom must **not** be silently removed from the fourth odd moment, nor the zero atom from the first even moment.

Neither the X sequence nor the Y sequence is identically zero. For example, if all \(E_i=0\), each \(O_i\) has the same nonzero sign as \(O_b(u_i)\): otherwise the independent actual parity rectangle would contain the origin. The test \(F=0,G=O_b\) has strictly positive finite pairing and nonnegative infinity contribution, contradicting (A). The all-\(O_i=0\) case is symmetric using \(F=E_b,G=0\) and the zero endpoint. This argument uses actual eligibility, not corner stability.

Delete zero entries before counting sign changes. From (G), Y has at least three sign changes: with at most two, a polynomial of degree at most two, whose roots lie between successive opposite-sign blocks, makes every \(Y_i p(u_i)\) have the same strict sign, contradicting the first three Y moments. If Y has exactly three changes, take the **monic** cubic p with one positive root between each change. Its lower moments vanish, so \(\sum_iY_i p(u_i)=\mu\). The sign of this nonzero sum is the sign of the last nonzero Y entry; hence \(\mu>0\) and that last sign is positive. In particular \(\mu=0\) forces at least four changes.

The same conclusion holds for X with \(\lambda\) in place of \(\mu\). For at most two changes use \(u_iX_i\) and the vanishing moments of degrees 1--3. With exactly three changes and the same monic cubic p, whose three roots \(\xi_1,\xi_2,\xi_3\) are positive,
\[
 \sum_i X_i p(u_i)=\lambda\xi_1\xi_2\xi_3.
\]
Its sign is the sign of the last nonzero X entry. Consequently exactly three changes require \(\lambda>0\) and last sign positive; \(\lambda=0\) forces at least four changes. The weights \(W_i\) and \(u_i\) are positive, so these are also the sign sequences of the actual grouped E and O values.

### 3.2. From moment signs to two backward physical crossings

Suppose one parity has no reverse pair of the specified type. In its first and third uncertainty bands its nonzero sampled signs can then only progress from + to -, and in its second they can only progress from - to +. Outside the bands the signs are fixed. The entire sampled sign word is therefore a subsequence of the four-block word \(+,-,+,-\): it has at most three changes, and if it has exactly three its final sign is negative. This contradicts Section 3.1, which requires at least three and, in the exactly-three case, a positive final sign. Thus each parity has its own actual-band reverse pair. The proof includes zero and infinity through \(\lambda,\mu\), admits zero entries by deleting them only from the sign word, and does not choose separate boxes or replace the physical grouped members by unrelated parity data.

## 4. Exact frontier and remaining bridge

Combining Theorems A and B gives this conditional exact alternative for each original eligible K: strict common-SPR holds, or there is an actual physical four-corner zero relation (A) with at most eight finite-plus-endpoint atoms, six to eight distinct positive finite frequencies, and both parity-backtracking constraints of Section 3. Conversely, any relation (A) is genuinely a zero dual and excludes strict synthesis on the **same** K. The equations in (A), positivity of weights/frequencies, the corner choices, and the exact eligibility predicate form a finite first-order description; displaying it is not a quantifier-elimination run or a truth verdict.

If the first branch fails, the steering identity gives all-eight-strict-negative actual-member certificates in eligible two-coordinate enlargements, at the same selected finite frequencies. This respects the buffer: it does not infer strict negativity on K from a zero dual on K. The four-corner/same-Q SDP and the all-actual-R4/both-R5 ROOT interface remain the imports S1--S3, not newly solved claims. In particular, no common triple satisfying every actual R4 and both R5 orientations has been constructed here, and a negative polynomial coefficient, failed solver, synthetic example, or merely weak separator is not an eligible counterexample.

**First unpaid step:** either prove that no eligible independent parity rectangle can support an (A)--(B) relation with the two reverse physical-band pairs and moment conditions (G), or actually give one full-width eligible box and verify its zero relation exactly. Neither has been done. The reverse-pair conditions are necessary only; they have not been proved contradictory. The scoped fixed-parity corollary and a finite support reduction do not settle the arbitrary both-parity target. Rational-endpoint zero-dual real-algebraic existence is only the S4 import; no rational-frequency zero dual is claimed. No actual eligible zero dual, strict-negative witness, universal numerator, or global ROOT proof is supplied.

## 5. Input pins, process, imports, and assurance

Role: **GENERAL AUTHOR**, not a constrained-WRITTEN reviewer or independent family gate. Before mathematical body access I read the actual dispatch receipt; complete manifest, freeze receipt, final binding, and prepared metadata; and **all 23 manifest-listed controls** through their endings, then sent Main the direct PREBODY ACK. The multipart policy as stated in the manifest and freeze receipt was read; its separately referenced policy file was not separately opened. I then read the single literal packet serially in consecutive raw windows of at most 20 LF, from packet lines 1--384 through its ending, before comparison or research. No body was read in parallel. Parent metadata reports full-source roundtrip and persisted-byte equality; I did not independently rerender or authenticate the original source files.

Actual SHA-256 observations for the wave's manifest, freeze receipt, final binding, prepared metadata and packet were respectively:

* manifest `cc28c39eb0047c6d325762729ce784edc8eef6480271f17e71c55d085d57cdad`;
* freeze `97f5e67d30dd24c086e4260bfdf7bb7a256d80a472fcf4474ce1a7fe0e66c88f`;
* final binding `3b25d438a5bd067ae4a173ac3d99ba6c638a0688bc3ccc8adb0388f6dd6acc8a`;
* prepared metadata `d158c7f8539d039100ffaf14cd8017029c0b82c5d5461bef7d23db247d6b000b`;
* complete packet `78415651f9a177c91a1fe6c82e635d22fd195df633e0a218e722da4a9a1a2923`.

The packet contains the following complete bodies and source pins, as supplied by the parent freeze and directly read in the packet: S1 LF1--29 `949af8c879058b8be166086ab06dbba03d896a26adc64e1621dfbdf7a72e4d0b`; S2 LF1--40 `8fcf488e37f1415c98b48cccdcab391e6a2fa409f8c43561f73df4cd8e41f63d`; S3 LF1--46 `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`; S4 LF1--200 `ffbb995d00381931c2895e332b86e1b2ee124890d605e0dcdf415025c97c075b`; S5 LF1--47 `89d522980ae257e6f5d86181ae4c4c97c48c441e6d77735e3ffc7d8cc43325c8`. S5 reports a different, scoped small-box parent run; it is not an independent execution of this candidate and did not test the wide SDP.

Mathematical imports are exactly the S1/S4 exact eligibility and same-box zero-hull equivalence, S3's eligible at-most-five-frequency strict-negative no-go and actual odd-band interface, the classical Hermite--Biehler theorem, and elementary real interpolation, convexity and compactness. The endpoint-sensitive sign-change and connected-hull arguments above are supplied as written proofs, not imported numerical evidence. Source identity beyond the parent's packet binding, global status, literature novelty, and worldwide priority were not established.

**Separate process findings / nonactions:** No held episode, held method/history, held proof, or any held selection/planning/verification/reporting/confidence/downstream consumer was consulted; no packet outgoing source link, sibling proof, or old code was followed. No scientific code, source preparation, solver, test, build, lint, formatter, public-source fetch, external-model CLI, install, Git, paid/heavy action, or scientific child execution was performed. Hashing and the exclusive creation of this literal written return are administrative I/O, not scientific execution. No process deviation is known to this author; no private-cognition certificate is asserted. Parent full reading, independent mathematical reconstruction, and a disposition remain separate. No human, other-model-family, formal/kernel, novelty, global-solution, or actual-counterexample PASS is claimed.
