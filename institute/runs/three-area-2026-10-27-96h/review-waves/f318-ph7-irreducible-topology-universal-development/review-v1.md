# UNREVIEWED AUTHOR CANDIDATE — PH7 all-shift cubic resolvent obstruction

**Wave:** f318-ph7-irreducible-topology-universal-development  
**Observed completion checkpoint:** 2026-10-30T14:52:37Z  
**Status:** Written necessary-condition candidate, not an independent review or adopted result. No seven-state existence, seven-state exclusion, improved endpoint, or original-target completion is claimed.

## 1. Administrative acknowledgement and exact inputs

The administrative PRE-BODY ACK was delivered before opening the mathematical packet, following the observed clock 2026-10-30T14:42:47Z.

Before that ACK, I read the complete manifest, complete freeze receipt, and all six declared status-only controls, including their endings. Live metadata hashes matched:

- Manifest: `95cb0954514894e332fb0beb7bc05e90a2cffb12949ac6358ea93c0463f1b322`.
- Freeze receipt: `0aa26ffd3c8a6ba26c43f4f32d32668a0f302e097503590394ffe1b79443b69e`.
- Literal packet: `fd999e13d90467ab54a8f3170dd87250de2ab9fc12f137ccfbf80dec1114823a`.
- All six control pins.

After the ACK, I read the complete ordered literal packet in raw windows LF1–20, LF21–40, and LF41–50, including the ending. No packet truncation remained.

The only scientific source inputs are:

1. **S1, complete LF1–17:** original transform and actual PH representation definition, particularly LF5–10. Source SHA-256: `a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85`.
2. **S2, complete LF1–31:** the adopted, conditional every-actual-seven-state irreducibility/eight-edge theorem, particularly LF7–11 and LF19–23. Source SHA-256: `42ae3d996ffb7f46cc5ad72a0d18f3eae665290f8d7901e994ac7776a6b4d281`.

Both source hashes were also checked directly as metadata. Linked older manuscripts, reviewer bodies, held payloads, and computational controls were not opened or replayed. Historical computational statements inside S2 are provenance, not newly executed evidence.

The status-only controls supply no mathematical premises. GLOBAL NO GO and inherited consumer restrictions remain unchanged.

## 2. Candidate statement

Let
\[
d=a-c>0,\qquad z=\frac{b^2}{d^2}>\frac12,
\]
and suppose an **actual** representation of
\[
H(s)=\frac{c(a^2+b^2)^2}
{(s+c)((s+a)^2+b^2)^2}
\]
uses at most seven states, with all original requirements:
\[
T\text{ real Hurwitz Metzler},\quad T\mathbf1\le0,\quad
\alpha\ge0,\quad \alpha\mathbf1=1,
\]
and
\[
\alpha(sI-T)^{-1}(-T\mathbf1)=H(s).
\]

By the exact adopted S2 scope, it has seven states and a strongly connected generator graph, with at least eight positive off-diagonal entries.

Put
\[
G=\frac{T+cI}{d}.
\]
There exist real numbers \(\sigma>0,\pi>0\) such that
\[
p(x):=\det(xI-G)
=x\bigl((x+1)^2+z\bigr)^2
  (x^2+\sigma x+\pi).
\]

For **every** real \(x>0\), define
\[
w=x+1,\qquad A=w^2+z,\qquad B=x^2+\sigma x+\pi,
\]
and
\[
L=\frac1x+\frac{4w}{A}+\frac{2x+\sigma}{B},
\]
\[
V=\frac1{x^2}
+\frac{4(w^2-z)}{A^2}
+\frac{(2x+\sigma)^2-2B}{B^2},
\]
\[
W=\frac1{x^3}
+\frac{4w(w^2-3z)}{A^3}
+\frac{(2x+\sigma)((2x+\sigma)^2-3B)}{B^3}.
\]
Finally put
\[
Q=V-\frac{L^2}{7},
\qquad
R=W-\frac{3LV}{7}+\frac{2L^3}{49}.
\]

The proposed necessary spectral condition is
\[
\boxed{\quad
Q(x)>0,\qquad
R(x)+\frac5{\sqrt{42}}\,Q(x)^{3/2}>0
\quad\text{for every }x>0.
\quad} \tag{★}
\]

This is an all-variable condition. No topology, rate pattern, value of \(z\), or diagnostic resolvent shift has been selected.

## 3. Proof

### 3.1 Actual representation and normalized spectrum

The visible poles force characteristic roots \(-c\) and \(-a\pm ib\), with each nonreal root having algebraic multiplicity at least two. This uses actual transfer equality, not a proposed spectral realization.

For completeness, the Perron root of the irreducible \(T\) is exactly \(-c\). Let \(r=-T\mathbf1\). It is nonnegative and nonzero: otherwise \(T\mathbf1=0\), contrary to Hurwitz stability. If \(v,w_T\) are positive right and left Perron vectors, then
\[
(\alpha v)(w_T^{\mathsf T}r)>0.
\]
Thus the Perron mode occurs with positive coefficient in the actual density \(\alpha e^{tT}r\).

On the transform side, the slowest pole is the simple pole \(-c\), with positive residue
\[
\frac{c(a^2+b^2)^2}{(d^2+b^2)^2}.
\]
All other density terms decay as a polynomial times \(e^{-at}\), with \(a>c\). Perron asymptotics therefore give \(s(T)=-c\).

Consequently \(G\) is irreducible Metzler with simple Perron root zero, and every other eigenvalue has strictly negative real part. Its prescribed roots are
\[
-1\pm i\sqrt z,
\]
each at least twice.

The two remaining characteristic roots can be written \(-u,-v\). They are either both negative real roots, or a conjugate pair with negative real part; equivalently, \(u,v\) are positive real numbers or conjugates with positive real part. Hence
\[
\sigma=u+v>0,\qquad \pi=uv>0.
\]

This gives the stated factorization of \(p\). It also allows hidden roots to coincide with prescribed nonreal roots. No diagonalizability or distinct-hidden-root assumption is made.

### 3.2 Every positive-shift resolvent is entrywise positive

For every \(x>0\),
\[
N=(xI-G)^{-1}
=\int_0^\infty e^{-xt}e^{tG}\,dt.
\]
The integral converges because \(s(G)=0\). Irreducible Metzler semigroup positivity gives
\[
e^{tG}>0\qquad(t>0),
\]
so
\[
N_{ij}>0
\]
for every pair of indices.

This positivity applies to the actual generator’s resolvent. No replacement realization has been introduced.

The characteristic factorization gives
\[
L=\operatorname{tr}N,\qquad
V=\operatorname{tr}N^2,\qquad
W=\operatorname{tr}N^3.
\]
The displayed formulas follow by summing reciprocal eigenvalue powers, with algebraic multiplicity. These trace identities remain valid for Jordan blocks.

### 3.3 Centering and reciprocal-edge symmetrization

Set
\[
X=N-\frac{L}{7}I.
\]
Then
\[
\operatorname{tr}X=0,\qquad
\operatorname{tr}X^2=Q,\qquad
\operatorname{tr}X^3=R.
\]

Define the real symmetric matrix \(S\) by
\[
S_{ii}=X_{ii},\qquad
S_{ij}=\sqrt{N_{ij}N_{ji}}\quad(i\ne j).
\]
Every off-diagonal entry of \(S\) is strictly positive. Direct trace expansion gives
\[
\operatorname{tr}S=0,\qquad
\operatorname{tr}S^2=\operatorname{tr}X^2=Q.
\]
In particular, \(Q>0\).

The diagonal and reciprocal-two-edge contributions to the cubic traces agree. For each unordered triple \(i,j,k\), the remaining difference is
\[
3\left(
N_{ij}N_{jk}N_{ki}
+N_{ik}N_{kj}N_{ji}
-2\sqrt{
N_{ij}N_{ji}N_{jk}N_{kj}N_{ik}N_{ki}}
\right)\ge0
\]
by AM–GM. Therefore
\[
R=\operatorname{tr}X^3\ge\operatorname{tr}S^3. \tag{1}
\]

This sums over all triples. It assumes no particular directed cycle or graph topology.

### 3.4 Seven-dimensional symmetric cubic bound

For real numbers \(\mu_1,\ldots,\mu_7\) satisfying
\[
\sum_i\mu_i=0,\qquad \sum_i\mu_i^2=Q>0,
\]
compactness and Lagrange multipliers show that an extremizer of \(\sum_i\mu_i^3\) has at most two distinct values.

At an extremizer, let \(k\) values be negative and \(7-k\) positive. The constraints determine its cubic sum as
\[
Q^{3/2}\frac{2k-7}{\sqrt{7k(7-k)}}.
\]
The coefficient is increasing for real \(0<k<7\): differentiating
\[
\frac{2k-7}{\sqrt{k(7-k)}}
\]
gives a strictly positive derivative. Its minimum over admissible integer multiplicities is therefore attained at \(k=1\). Thus
\[
\sum_i\mu_i^3\ge-\frac5{\sqrt{42}}Q^{3/2}. \tag{2}
\]

Equality requires one negative eigenvalue and six equal positive eigenvalues.

For the present \(S\), equality is impossible. Its strictly positive off-diagonal entries make it an irreducible Metzler matrix, whose largest eigenvalue is simple by Perron theory. The equality spectrum in (2) would instead have its largest eigenvalue with multiplicity six. Hence
\[
\operatorname{tr}S^3>
-\frac5{\sqrt{42}}Q^{3/2}. \tag{3}
\]

Combining (1) and (3) proves (★).

Importantly, strictness does **not** require strict AM–GM on a particular triangle. It follows from the complete off-diagonal positivity of the resolvent symmetrization.

## 4. Explicit hidden-spectrum consequence

The same necessary condition supplies a simple quantitative restriction on the two hidden roots.

The large-\(x\) resolvent expansion gives
\[
\lim_{x\to\infty}x^4Q(x)
=\operatorname{tr}G^2-\frac{(\operatorname{tr}G)^2}{7}
\ge0.
\]
Here
\[
\operatorname{tr}G=-4-\sigma,
\]
and
\[
\operatorname{tr}G^2=4(1-z)+\sigma^2-2\pi.
\]
Consequently
\[
\boxed{\quad
7\pi+14z\le3\sigma^2-4\sigma+6.
\quad} \tag{4}
\]

Since \(\pi>0\) and \(z>1/2\), this further implies
\[
\boxed{\quad
\sigma>\frac{2+\sqrt{42z-14}}{3}.
\quad} \tag{5}
\]
Indeed, the quadratic
\[
3\sigma^2-4\sigma+6-14z
\]
must be strictly positive; its lower root is negative throughout the stipulated \(z\)-range.

These are hidden-spectrum constraints, not assumptions that the hidden roots are real. The full finite-\(x\) condition (★), rather than only its large-\(x\) consequence, is the principal candidate.

## 5. Actual source versus relaxation

The argument starts with an actual \((\alpha,T)\), including its initial distribution, exit-vector tie, and exact numerator. Those conditions justify the actual-spectrum extraction and positive Perron visibility.

After that extraction, the candidate retains only necessary spectral and Metzler consequences. In particular, it does **not** retain enough information to reconstruct:

- a Metzler generator with the proposed characteristic polynomial;
- the required Jordan visibility of both second-order nonreal poles;
- an initial distribution and the tied exit vector realizing the exact numerator.

Thus satisfying (★) is not sufficient for an actual PH representation. No spectral realization is silently promoted to a PH realization.

The new content relative to the supplied structural theorem is an explicit scalar positivity obstruction involving \(z,\sigma,\pi\) at **every** resolvent shift, not merely a restatement of strong connectivity or the eight-edge count. It does not establish an improved \(z\)-only bound in this return. Novelty outside the supplied packet has not been assessed.

## 6. Exact unpaid analytic implication

To obtain an exclusion on any specified parameter interval \(J\subset(1/2,\infty)\) using this relaxation, one would still need to prove
\[
\forall z\in J\ \forall\sigma>0\ \forall\pi>0\
\exists x>0:
\]
\[
Q(x)\le0
\quad\text{or}\quad
\left(
Q(x)>0\ \text{and}\
R(x)+\frac5{\sqrt{42}}Q(x)^{3/2}\le0
\right).
\]

That quantified analytic implication is **not proved here**. No nonempty interval \(J\) is asserted to satisfy it.

Conversely, finding \(\sigma,\pi\) that pass every inequality would establish only feasibility of this necessary relaxation, not seven-state existence.

Therefore:

- No seven-state representation has been constructed.
- No seven-state exclusion has been established.
- No failure of this route has been proved.
- No universal impossibility follows from an unpaid elimination step.
- GLOBAL NO GO remains unchanged.

## 7. Claim and severity accounting

“SUPPORTED” below means an author-written derivation is supplied, not independent acceptance.

| Claim | Status | Evidence/import boundary |
|---|---|---|
| Conditional seven-state size, reachability, strong connectivity and eight-edge minimum | **SUPPORTED as an exact adopted import** | S2 LF7–13, LF19–23; not independently re-reviewed here |
| Normalized characteristic factorization with \(\sigma,\pi>0\) | **SUPPORTED** | S1 LF5–10; S2 LF11, LF19–23; §3.1 above |
| All-shift strict cubic resolvent condition (★) | **SUPPORTED** | Independent written derivation in §§3.2–3.4 |
| Hidden-spectrum restrictions (4)–(5) | **SUPPORTED** | §4 |
| Improved parameter endpoint, seven-state existence/exclusion, exact minimum-order function | **INCONCLUSIVE** | Unpaid implication stated in §6 |

**Author-identified findings:** 0 FATAL / 0 MAJOR / 0 MINOR. This is not an independent-review verdict, a source acceptance gate, or a correctness certificate. The unresolved parameter projection is explicitly outside the proved claim.

## 8. Execution and delivery record

Observed checkpoints were 2026-10-30T14:41:46Z, 14:42:47Z, 14:50:13Z, and 14:52:37Z. This duty remained within the required checkpoint cadence.

Only source/control reads, metadata hashing, native clock observations, and the refused administrative-file write were performed. No selected mathematical instance, scientific executable, interpreter calculation, CAS, solver, enumeration, replay, verifier, external-model CLI, build, lint, test, or formatter was used.

The filesystem write refusal was not bypassed. This full text is returned for parent materialization.

**Final disposition: UNREVIEWED AUTHOR CANDIDATE.**