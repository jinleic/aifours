# F589 — Independent WRITTEN review

**Verdict: SUPPORTED at the stated conditional structural scope.**  
**Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The candidate proves that, for actual sets
\[
P\oplus Q=\mathbb Z_n,\qquad
\{0,3,8,11\}\subseteq P,\qquad
\{0,1,7,13,14\}\subseteq Q,
\]
an actual two-point direct factor
\[
P=\{u,u+d\}\oplus C,\qquad d\not\equiv0\pmod n,
\]
must satisfy \(\gcd(d,n)\ge15\). The proof preserves the original factorization, correctly normalizes its orientation, and uses weighted projected coefficients rather than an unweighted quotient tiling. All fourteen stated cases reconstruct.

This is **not** a proof of unrestricted anchored nonexistence or of the existence of a suitable two-point factor in every head.

## 1. Reviewed material and process

Frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f589-anchored-two-point-factor-periodic-reduction-small-gcd-written-review/`

Parent-supplied pins:

- Manifest SHA-256: `ac03d037e3e6a8ab53184b4d32dfd6856a2ee3d17f2b570740551281d06566b9`.
- Freeze-receipt SHA-256: `36ad4954c951e15c01a666a16aa4a1f17838c57f4669523be61e487b6011f1f9`.
- Literal-packet SHA-256: `6270a7c45f80820cae59dabe8c512e091ea9410924e092a749a8361cd4abecbc`.

These hashes, byte/LF measurements, and the supplied observation `2026-10-30T13:57:02-0700 PDT` are **parent observations**, not reviewer-native executions or an observed reviewer start time. I did not independently execute hashing or a native clock command.

Before mathematical packet reading, I completely read the manifest, freeze receipt, parent metadata supply, and all **twelve** status-only controls:

1. Owner frontier-first direction.
2. L1 selected-diagnostic release quarantine.
3. Written-duty execution/reporting deviations.
4. Held PH registration/report-consumer quarantine.
5. F439 quarantine.
6. F444 quarantine.
7. F448 quarantine.
8. F508 quarantine.
9. F513 quarantine.
10. AME held-consumer quarantine.
11. CORE-GRAM auxiliary-operator quarantine.
12. Privacy auxiliary-parameter quarantine.

I then delivered the direct administrative pre-body ACK to Main. Only afterward did I read the entire literal packet consecutively in raw windows of at most twenty LF, covering packet LF1–727 through both endings:

- **S1:** complete author candidate, logical labels 1–694; source SHA-256 `63a833c5c54b369d072208a0543d15a9b1e4b51e90b4c6b8622cb75a3d333909`.
- **S2:** complete prior disposition, labels 1–31; source SHA-256 `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`.

The S1 metadata count of 693 LF delimiters and its 694 rendered logical labels are distinguished; its final conclusion was read. No displayed packet elision required recovery.

The F569 ACK’s earlier “11 controls” statement is explicitly withdrawn by S1:63 and corrected to twelve. I do not reuse the withdrawn count or infer an additional omitted-control event.

This review used written reconstruction of the author’s fourteen cases and stated support identities. **No scientific execution, interpreter, CAS, solver, scientific code, new selected numerical instance, source-link follow, author-code read, sibling-review read, or held scientific payload was used.** No repository file was edited. This complete body is returned for parent materialization.

## 2. Claim: actual-factor reduction and periodic quotient — SUPPORTED

**Evidence:** S1:69–143.

After absorbing \(u\) into the second factor, write
\[
P=\{0,d\}\oplus C.
\]
The two actual direct sums combine to give
\[
\{0,d\}\oplus C\oplus Q=\mathbb Z_n.
\]

In particular, \(C\oplus Q\) is direct: a collision between two \(C,Q\) pairs would already give a collision between two \(P,Q\) representations using the zero branch of \(\{0,d\}\). Set
\[
T=C\oplus Q.
\]
Then
\[
\{0,d\}\oplus T=\mathbb Z_n
\]
as an actual direct factorization. Thus, with \(t=1_T\),
\[
t(x)+t(x-d)=1,\qquad t(x)=t(x-2d).
\]

Let \(g=\gcd(d,n)\). Each \(d\)-cycle has length \(n/g\); its alternating zero-one values close only if \(n/g\) is even. Writing \(d=ge\), \(n=gm\), we have \(m\) even and \(\gcd(e,m)=1\), so \(e\) is odd and
\[
\gcd(2d,n)=2g.
\]
Therefore \(2g\mid n\), and invariance under \(2d\) means that \(T\) is a union of complete fibers modulo \(2g\).

Moreover \(d\equiv g\pmod{2g}\). The projected occupied set \(V\subseteq\mathbb Z_{2g}\) consequently satisfies
\[
V\sqcup(V+g)=\mathbb Z_{2g},\qquad |V|=g.
\]

This establishes the needed consuming interface for the projected proof: \(V\) records complete fibers of the **actual** set \(T\), not a replacement complement.

## 3. Claim: orientation and actual-anchor consumers — SUPPORTED

**Evidence:** S1:145–173.

The normalization is valid without translating the actual head or tail.

Since \(0\in P=\{0,d\}\oplus C\), either \(0\in C\) or \(-d\in C\). In the latter case, put
\[
d'=-d,\qquad C'=C+d.
\]
Then
\[
\{0,d'\}\oplus C'
=\{0,-d\}\oplus(C+d)
=P,
\]
and \(0\in C'\). The original \(P,Q\) and all their anchors remain unchanged, while \(\gcd(d',n)=g\). The associated \(T\) and \(V\) are translated consistently. Both signs of the difference project to \(g\) modulo \(2g\).

Thus the proof may assume \(c_0>0\), and the actual tail anchors imply
\[
S_g=\{0,1,7,13,14\}\bmod2g\subseteq V.
\]
For every projected \(C\)-support residue \(c\),
\[
S_g+c\subseteq V.
\]
Every original head anchor \(a\) requires projected \(C\)-support at \(a\) or \(a-g\). These requirements follow from actual membership in \(P=C\sqcup(C+d)\); no quotient-head factorization is assumed.

## 4. Claim: exact weighted projection — SUPPORTED

**Evidence:** S1:175–196.

For
\[
c_i=\#\{c\in C:c\equiv i\pmod{2g}\},\qquad
q_j=\#\{q\in Q:q\equiv j\pmod{2g}\},
\]
the convolution coefficient
\[
\sum_i c_iq_{s-i}
\]
counts actual ordered \(C,Q\) pairs whose sum projects to \(s\).

Because \(C\oplus Q=T\) is direct, this equals the number of actual elements of \(T\) in that fiber. Complete-fiber periodicity gives
\[
\sum_i c_iq_{s-i}=L\,1_V(s),\qquad L=\frac n{2g}>0.
\]

Projection collisions have therefore been counted, not discarded. Nothing in the subsequent argument assumes that nonzero \(c_i\) or \(q_j\) equals one.

## 5. Claim: the eight antipodal exclusions — SUPPORTED

**Evidence:** S1:198–218.

The displayed actual-tail differences give precisely the required congruences:

| \(g\) | Tail difference | Difference modulo \(2g\) |
|---:|---:|---:|
| 1 | \(1-0\) | 1 |
| 2 | \(14-0\) | 2 |
| 4 | \(13-1\) | 4 |
| 6 | \(7-1\) | 6 |
| 7 | \(7-0\) | 7 |
| 12 | \(13-1\) | 12 |
| 13 | \(13-0\) | 13 |
| 14 | \(14-0\) | 14 |

Each places an antipodal pair in \(S_g\subseteq V\), contradicting \(V\cap(V+g)=\varnothing\). Together these exclude exactly the eight stated cases.

## 6. Claim: \(g=3,5\) — SUPPORTED

**Evidence:** S1:221–265.

For \(g=3\),
\[
S_3=\{0,1,2\}\subseteq\mathbb Z_6.
\]
For \(g=5\),
\[
S_5=\{0,1,3,4,7\}\subseteq\mathbb Z_{10}.
\]
In each case \(|S_g|=g=|V|\), so \(V=S_g\).

Every \(C\)-support residue must then stabilize \(S_g\), since its translate of \(S_g\) is contained in another set of the same cardinality. In either case, a nontrivial translation stabilizer would have order \(g\): its order divides both \(2g\) and \(|S_g|=g\). The set would therefore be one parity coset. Both displayed sets contain 0 and 1, so this is impossible.

Consequently \(C\) projects only to zero. The projected head is supported in \(\{0,g\}\). For \(g=3\), the actual anchor \(8\equiv2\pmod6\) is excluded; for \(g=5\), the actual anchor 3 is excluded.

## 7. Claim: \(g=8\) — SUPPORTED

**Evidence:** S1:267–337.

Work modulo 16. The head anchor 3 requires \(C\)-support at 3 or 11. The latter would place
\[
11+13\equiv8\pmod{16}
\]
in \(V\), antipodal to its mandatory zero. Thus \(c_0,c_3>0\), and
\[
V=S\cup(S+3)=\{0,1,3,4,7,10,13,14\}.
\]

I reconstructed the complete support restrictions through intersections. Define
\[
K=\bigcap_{s\in S}(V-s).
\]
Starting with \(V\), intersection successively with \(V-1,V-7,V-13,V-14\) gives
\[
\{0,3,13\},\quad
\{0,3,13\},\quad
\{0,3,13\},\quad
\{0,3\}.
\]
Hence \(\operatorname{supp}(C\bmod16)\subseteq\{0,3\}\). Since both residues occur,
\[
\operatorname{supp}(Q\bmod16)
\subseteq V\cap(V-3)
=\{0,1,4,7,10,13,14\}.
\]

The weighted coefficients at \(3,14,0,1\) consequently are
\[
\begin{aligned}
L&=c_3q_0,\\
L&=c_0q_{14},\\
L&=c_0q_0+c_3q_{13}>c_0q_0,\\
L&=c_0q_1+c_3q_{14}>c_3q_{14}.
\end{aligned}
\]
The actual tail anchors ensure \(q_0,q_1,q_{13},q_{14}>0\). The first and third equations imply \(c_3>c_0\); the second and fourth imply \(c_0>c_3\). This contradiction is valid for arbitrary positive multiplicities.

## 8. Claim: \(g=9\) — SUPPORTED

**Evidence:** S1:339–369.

Modulo 18, head anchor 3 requires support at 3 or 12. Residue 3 would put \(3+7=10\) opposite mandatory residue 1, so 12 occurs.

Head anchor 8 requires support at 8 or 17. Residue 8 would put \(8+1=9\) opposite mandatory residue 0, so 17 occurs.

The resulting support includes
\[
12+14\equiv8,\qquad17+0=17\pmod{18}.
\]
These are antipodal. Both forced choices and the final incompatibility consume the actual head and tail memberships correctly.

## 9. Claim: \(g=10\) — SUPPORTED

**Evidence:** S1:371–448.

Modulo 20, the three stated head-anchor alternatives force
\[
D=\{0,1,8,13\}\subseteq\operatorname{supp}(C\bmod20):
\]

- Support at 3 is impossible because \(3+7=10\) is opposite 0; hence 13 occurs.
- Support at 18 is impossible because \(18+13\equiv11\) is opposite 1; hence 8 occurs.
- Support at 11 is itself opposite 1; hence 1 occurs.

The union of the mandatory translates is
\[
S+D=\{0,1,2,6,7,8,9,13,14,15\}.
\]
Its cardinality is ten, so it equals \(V\).

For \(K=\bigcap_{s\in S}(V-s)\), the successive intersections after shifts \(1,7,13,14\) are
\[
\begin{aligned}
&\{0,1,6,7,8,13,14\},\\
&\{0,1,6,7,8,13,14\},\\
&\{0,1,7,8,13,14\},\\
&\{0,1,7,8,13,14\}.
\end{aligned}
\]
This verifies the asserted \(C\)-support restriction.

For \(Q\), intersection with the mandatory \(C\)-translates gives
\[
\begin{aligned}
V\cap(V-1)&=\{0,1,6,7,8,13,14\},\\
V\cap(V-1)\cap(V-8)&=\{0,1,6,7,13,14\},\\
\bigcap_{c\in D}(V-c)&=\{0,1,7,13,14\}=S.
\end{aligned}
\]

At residues 6 and 9, the support restrictions leave exactly
\[
L=c_{13}q_{13},\qquad L=c_8q_1.
\]
At residue 1, the contribution \(c_8q_{13}\) is accompanied by the strictly positive \(c_0q_1\), so
\[
L>c_8q_{13}.
\]
At residue 14, the contribution \(c_{13}q_1\) is accompanied by strictly positive \(c_0q_{14}\), so
\[
L>c_{13}q_1.
\]
Other possible contributions are nonnegative and do not weaken either inequality. Since \(q_{13},q_1>0\), comparison gives both \(c_{13}>c_8\) and \(c_8>c_{13}\).

## 10. Claim: \(g=11\) — SUPPORTED

**Evidence:** S1:450–517.

Modulo 22, head anchor 3 requires support at 3 or 14. The former is opposite the mandatory tail residue 14, so 14 occurs.

Head anchor 8 requires support at 8 or 19. The latter would put \(19+14\equiv11\) opposite mandatory zero, so 8 occurs.

Thus \(c_0,c_8,c_{14}>0\), and the mandatory translates force
\[
V=S+\{0,8,14\}
=\{0,1,5,6,7,8,9,13,14,15,21\}.
\]

For \(K=\bigcap_{s\in S}(V-s)\), successive intersections after shifts \(1,7,13,14\) give
\[
\begin{aligned}
&\{0,5,6,7,8,13,14,21\},\\
&\{0,6,7,8,14,21\},\\
&\{0,8,14\},\\
&\{0,8,14\}.
\end{aligned}
\]
Hence only the three mandatory \(C\)-support residues remain.

The corresponding \(Q\)-support intersections are
\[
V\cap(V-8)=\{0,1,5,6,7,13,14,15,21\},
\]
and
\[
V\cap(V-8)\cap(V-14)
=\{0,1,7,13,14,15,21\}.
\]

The exact weighted equations therefore reduce to
\[
\begin{aligned}
L&=c_{14}q_{14} &&\text{at residue }6,\\
L&=c_8q_0 &&\text{at residue }8,\\
L&=c_0q_0+c_8q_{14}>c_8q_{14} &&\text{at residue }0,\\
L&=c_0q_{14}+c_{14}q_0>c_{14}q_0 &&\text{at residue }14.
\end{aligned}
\]
Actual tail anchors give \(q_0,q_{14}>0\). The equations imply \(c_{14}>c_8\) and \(c_8>c_{14}\), completing the contradiction.

The eight immediate exclusions and these six remaining cases exhaust every positive integer \(g\le14\).

## 11. Claim: original-versus-projected factor boundary — SUPPORTED

**Evidence:** S1:32–36, 519–539, 611–623, 656–658.

The proved hypothesis is an **actual global** two-point direct factor of the original head \(P\). The candidate does not derive that hypothesis merely from the four head anchors, a quotient support, or a replacement tile.

In particular, an actual factor of difference \(3,5,8,\) or \(11\) is excluded because its original cyclic gcd is at most that positive difference and hence below fifteen. A factor in another coordinate system does not qualify without checking its lift and original gcd.

The stated unpaid step is accurate: establish a qualifying actual factor, or handle heads without one by another argument. No full numerical allocation is closed merely by this structural subclass theorem.

## 12. Claim: CRT consumer and residual parameter scope — SUPPORTED at its stated scope

**Evidence:** S1:541–658; exact adopted dilation import in S2:11.

For the stated families,
\[
n=HR,\qquad
H=2^{a+b}p^{j+t},\qquad
|P|=2^ap^j,\qquad
\gcd(R,2p)=1.
\]
The CRT choice \(k\equiv1\pmod H\), \(k\equiv0\pmod R\) is coprime to \(|P|\). The adopted dilation lemma applies at exactly that cardinality-coprimality scope; it does not require \(k\) to be a unit modulo \(n\).

Under CRT, multiplication by \(k\) sends \((h,r)\) to \((h,0)\). Its injectivity on \(P\) therefore makes the first-coordinate projection injective, yielding
\[
P=\{(a,f(a)):a\in A\}.
\]
The dilated tiling gives
\[
A\oplus Q_r=\mathbb Z_H,\qquad |Q_r|=2^bp^t
\]
for every \(r\).

The original tiling still requires the stronger coupled equations
\[
\sum_{a\in A}1_{Q_{r-f(a)}}(h-a)=1.
\]
This is the correct consuming-side equation: the graph’s second coordinate shifts which tail fiber participates. It is not discarded by the common-complement statement.

The head and tail anchor equations follow directly under CRT. The stated parameter bounds ensure \(H>14\) and \(R\ge15\), so the displayed anchor coordinates have the claimed noncollapse and distinct-fiber properties.

A projected pairing also needs a common increment in \(f\) to lift to a fixed original difference. The candidate correctly leaves that condition unproved.

The listed \(p=3,5,11\) residual scopes are consistent with the imported necessary conditions. In particular, the extra \(a+b\ge3\) restriction for \(p=5,11\) follows from S2’s alternative \(3\mid|P|\) or \(8\mid n\). They are stated as this argument’s remaining scopes, not as existence assertions or a globally audited frontier.

## 13. Import and assurance limits

The new small-gcd obstruction is self-contained from the actual-factor assumptions. Its fourteen-case proof does not use an external structure theorem, an RSS conclusion, or an earlier machine result.

The CRT discussion uses only the adopted dilation statement at the explicit scope recorded in S2:11. I did not follow S2’s evidence links or reclassify its historical finite results as fresh execution.

The public references listed in S1:660–672 were not followed in this review. Accordingly:

- Original RSS verification remains outside this result.
- The additional pure-letter-order fact remains unverified here.
- No unconditional finite-maximal-completion conclusion follows.
- No current literature, novelty, worldwide-priority, source-equivalence, independent-family, human, or formal/kernel assurance is supplied.

## 14. Findings and final disposition

**Mathematical findings:** 0 FATAL / 0 MAJOR / 0 MINOR.

All load-bearing claims of the conditional small-gcd theorem were reconstructed, including the complete support restrictions and strict weighted comparisons. The orientation change preserves the actual anchored head, and every projected object is consumed through justified support or multiplicity equations.

**Overall correctness:** correct.

**Explanation:** The candidate establishes the stated obstruction for actual two-point direct factors of the actual anchored head, and its stated CRT consequences preserve the original-factor boundary. It does not establish unrestricted anchored nonexistence, the missing global factor/lift premise, or finite-maximal-completion nonexistence.

**Confidence:** 0.97.

This is one completed same-harness WRITTEN review, not parent adoption or a substitute for the separate written and finite gates.