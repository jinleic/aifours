DISPOSITION: ACCEPT-WITH-FIXES
T1 DISPOSITION: ACCEPT
T2 DISPOSITION: ACCEPT
T3 DISPOSITION: ACCEPT-WITH-FIXES

All three target hashes match. The ten mathematical import files checked also match the manifest. Only snapshot file reads, SHA-256 checks, and hand reasoning were used; no mathematical code, network, writes, or delegation.

Below, `P = inverse-run-count/mixdef-high`. References use the requested LF numbering.

## FATAL

none

## MAJOR

none

## MINOR

**M1 — T3 should state its dependency status explicitly.**  
`P/c6/proof-A0.md:5`, `P/c6/proof-A0.md:40`, `P/c6/proof-A0.md:66`.

The count-free argument checks out relative to Lemma C0W, but the theorem and corollary should carry that dependency explicitly rather than leaving “under review” only in the dependencies paragraph.

The evidence supports a precision fix: both earlier reviews found DF/C0W correct, with no requested change to either lemma. Moreover, the concatenated DF/C0W passages at `P/c6/proof-C0WB.md:27` and `:33`, and their r1 counterparts at `P/c6/proof-C0WB-r1.md:39` and `:45`, have identical SHA-256:
`ead66341ed2bc728f08cbf4afb1f4443df4189b9938f4d8d35d47024d7365175`.
The repair revision as a whole remains independently unreviewed. I also checked the unchanged argument directly below.

**Corrected theorem wording:**

> **Theorem C0-all, conditional on Lemma C0W.** Assuming Lemma C0W of `c6/proof-C0WB.md` in its stated NMH setting, for every NMH word with \(R\le2p-3\), the integer system (L) has no solution.

**Corrected corollary wording:**

> Let \(w\) be an NMH word with \(R\le2p-3\). An empty intersection of configuration-derived GS(a) bounds for some actual run excludes avoidance directly. Otherwise, conditional on Lemma C0W, \(w\) has an identity \(2p\)-subword if either every run has a quality seed, or every run has a nonempty seed satisfying (QS*) and the entire seed family satisfies (P2) and (PIN). Use SCW-G/SL from `proof-SEEDG-r2.md`, or the repaired SCW-G* from `proof-SEEDGstar-r1.md`.

No false mathematical inequality or numerical counterexample is asserted in this finding.

**Optional MINOR remark, not an error or counted finding — T2’s parity rule is unnecessary.**  
`P/c6/proof-S2wide.md:30`, `P/c6/proof-S2wide.md:35`.

Taking \(c=1\) throughout also works. Then
\[
j_2=q+1,\qquad j_1=B+[h\text{ odd}]-1,
\]
and the footprint excess is \(5-\Delta-q\). The exceptional families reduce to
\[
(\Delta,h)=(3,0),(3,2),(4,1).
\]
For example, at \((p,g,B)=(11,6,2)\), the original default has footprint \(12>n-B-4=11\); choosing \(c=1\) gives \(j_2=3,j_1=1\), footprint \(11\), and the same valid genericity argument. The existing five-family proof remains correct.

## T1: RZ-wide hand audit

**T1.1 — Parameters.**  
`P/c6/proof-RZwide.md:17`.

Since \(B\ge g+1\),
\[
m=\left\lceil\frac{g+B}{2}\right\rceil\ge g+1,\qquad r=m-g\ge1.
\]
The selected \(c\) is the least positive integer of \(r\)’s parity, so \(r-c\ge0\) is even. Consequently
\[
i=(r-c)/2\ge0,\qquad j=i+g+c\ge0,
\]
and \(i+j=m,\ j-i=y\). All are integers.

**T1.2 — Realisability, including small \(B\).**  
`P/c6/proof-RZwide.md:24`.

For \(\kappa=3\), necessarily \((g,B)=(1,2)\); then \(m=2,c=1,i=0,j=2\). The proof correctly treats this separately: \(2i\le B-3\) would be false here.

For \(\kappa\ge4\),
\[
m\le\kappa-2,\qquad
2i=m-g-c\le\kappa-2-g-1=B-3.
\]
Also
\[
2m\le\kappa+1\le p-2\le n-3,\qquad
2m+2\le\kappa+3\le p<k.
\]

After deleting \(t\) and its neighbours, independently of their signs,
\[
\alpha\ge n-3\ge2m,\qquad \beta\ge B-3.
\]
If \(i>0\), the anti intervals supply
\[
\sum \lceil L/2\rceil\ge\beta/2\ge i
\]
independent anti positions. Removing their aligned neighbours loses at most \(2i\) aligned positions. Thus the remaining aligned intervals supply at least
\[
\frac{\alpha-2i}{2}\ge m-i=j
\]
independent aligned positions.

For \(B=2\), only the separately treated \((g,B)=(1,2)\) occurs. For \(B=3\), the displayed bound forces \(i=0\). No positive anti capacity is assumed in either case. Anti targets or neighbours only improve the aligned count.

The deleted triple separates the path ends in the original cycle. Both neighbours of \(t\) remain omitted, so \(Q,Q+t\) are proper; adding \(t\) creates exactly one block. Finally \(D_Q=j-i=y\). No placement assumption is hidden.

**T1.3 — Formulas and every genericity comparison.**  
`P/c6/proof-RZwide.md:38`; compare `P/c6/proof-SEEDG-r2.md:51`, `:93`.

Here \(A=p+g\), \(A-\kappa=p-B\), and
\[
p-\left(\left\lfloor\frac{A-v}{2}\right\rfloor+1\right)
=\left\lceil\frac{p-g+v}{2}\right\rceil-1.
\]
Thus both displayed formulas are correct. “Generic” requires both \(\lambda(P)\) and \(\lambda(P^c)\) to attain their floor terms, exactly as GS(b) requires.

Put \(p=2s+1\). Then \(m\le s-1\), \(\kappa\le2m\). For \(Q\):
\[
\left\lfloor\frac{\kappa+c}{2}\right\rfloor+1
\le m+\lfloor c/2\rfloor+1\le m+c,
\]
while \(p-m+1\ge m+4\).

For \(Q+t\), put \(z=c+d\in\{0,1,2,3\}\):
\[
\left\lfloor\frac{\kappa+z}{2}\right\rfloor+1
\le m+\lfloor z/2\rfloor+1
\le m+z+1,
\]
and the third term is at most \(m+2<p-m\).

The ceiling values and competing middle-term bounds are:

| Argument | \(C(z)=\lceil(p+z)/2\rceil-1\) | Upper bound for middle term of \(U(Q+t)\) |
|---|---:|---:|
| \(z=0\) | \(s\) | \(s-2\) |
| \(z=1\) | \(s\) | \(s-1\) |
| \(z=2\) | \(s+1\) | \(s\) |
| \(z=3\) | \(s+1\) | \(s+1\) |

For \(Q\), its middle term is at most \(m+c\le s-1+c=C(c)\). The first \(U\)-terms are respectively \(m-1\le s-2\) and \(m\le s-1\).

The \(z=3\) tie is valid. For example, \(p=11,g=2,B=6,m=4,c=2,d=1\) gives \(v=5,b=5\):
\[
\lambda=\min(7,8,6)=6,\qquad U=\max(4,6,6)=6.
\]
There is no off-by-one error.

**T1.4 — Assembly and empty intervals.**  
`P/c6/proof-RZwide.md:61`; `P/c6/proof-SEEDG-r2.md:74`, `:89`, `:167`.

The configurations are actual proper patterns, so GS(b), NW and GS(a) apply. Intersecting the derived bounds with the canonical singleton interval either gives a nonempty quality seed or an actually inconsistent configuration-derived interval. This uses the repaired actual-empty interpretation, not emptiness of an abstract QS window.

Every aligned rotation run has length one, hence \(n_{\rm ev,al}=0\). C0+(i) and every remaining SEED-G hypothesis hold. The argument covers every anti-position layout.

**T1.5 — \(\kappa=3\), including \(p=7\).**  
`P/c6/proof-RZwide.md:25`, `:39`.

For \((g,B)=(1,2)\), let \(s=(p-1)/2\). Direct substitution gives:

| Pattern | \(\lambda\) | \(\lambda(\text{complement})\) | \(U\) |
|---|---:|---:|---:|
| \(Q:(2,2)\) | \(3\) | \(s+1\) | \(s\) |
| \(Q+t_+:(3,3)\) | \(3\) | \(s\) | \(s+1\) |
| \(Q+t_-:(1,3)\) | \(2\) | \(s+1\) | \(s\) |

The raw seed windows are
\[
[3-s,s-2]\quad(+),\qquad [2-s,s-3]\quad(-).
\]
The canonical singleton ranges are \([1,s]\) and \([-1,s-1]\); their intersections are \([1,s-2]\) and \([-1,s-3]\).

At \(p=7\), the four lambda values for the positive construction are \((3,4,3,3)\), and for the negative construction \((3,4,2,4)\). Explicitly:
\[
\begin{aligned}
\lambda(Q)&=\min(6,3,3)=3,&U(Q)&=\max(1,2,3)=3,\\
\lambda(Q+t_+)&=\min(5,5,3)=3,&U(Q+t_+)&=\max(2,2,4)=4,\\
\lambda(Q+t_-)&=\min(5,3,2)=2,&U(Q+t_-)&=\max(2,0,3)=3.
\end{aligned}
\]
Raw windows: \([0,1]\), \([-1,0]\). Canonically clipped seeds: \([1,1]\), \([-1,0]\).

## T2: S2-wide hand audit

**T2.1 — Packing.**  
`P/c6/proof-S2wide.md:19`.

The deletion leaves at most \(B+1\) aligned intervals. An interval of length \(l\) accommodates a specified list of singleton/pair blocks precisely when
\[
\sum(s_e+1)\le l+1.
\]
Pairs here are blocks of **two adjacent aligned rotation runs**.

Writing \(r\) for the number of aligned intervals,
\[
\sum\left\lfloor\frac{l+1}{3}\right\rfloor
\ge\frac{\alpha-r}{3}.
\]
The hypothesis implies
\[
3j_2+2j_1\le n-B-4\le\alpha-r.
\]
Hence enough pair capacity exists. Allocate pair counts to intervals and then pack the combined block lists there. The residual algebraic capacities satisfy
\[
\sum C_l=\alpha+r-3j_2,\qquad
\sum\lfloor C_l/2\rfloor\ge\frac{\alpha-3j_2}{2}\ge j_1.
\]
One unused position separates blocks within an interval; an anti run separates distinct intervals. The deleted triple prevents wrap and adjacency to \(t\). The resulting mass and block count are \(2j_2+j_1\) and \(j_2+j_1\), and adding \(t\) adds one block.

**T2.2 — Default recipe and exceptional split.**  
`P/c6/proof-S2wide.md:30`.

Since \(m-g=-q\), the stated equivalent parity rule is correct. Directly:
\[
j_2=q+c\ge1,\qquad j_1=B+[h\text{ odd}]-c\ge0,
\]
and
\[
3j_2+2j_1=m+y,\qquad
(m+y)-(n-B-4)=c+4-\Delta-q.
\]

Using \(h+\Delta\) odd:

| \(\Delta\) | Required parity of \(h\) | Values giving positive excess |
|---|---|---|
| \(3\) | even | \(q=0,1,2\), hence \(h=0,2,4\) |
| \(4\) | odd | \(q=0\), hence \(h=1\) |
| \(5\) | even | \(q=0\), hence \(h=0\) |
| \(\ge6\) | either permitted parity | none |

Thus the five families are exactly correct. The optional \(c=1\) simplification was recorded above.

**T2.3 — Genericity.**  
`P/c6/proof-S2wide.md:44`.

The calculation is identical to T1.3. A two-run aligned block contributes mass two but remains one block, exactly as the formulas require. Genericity depends on \((v,b)\), not on blocks all being singletons. Both target signs are covered.

**T2.4 — Every exceptional table entry.**  
`P/c6/proof-S2wide.md:55`.

For the four rows with \(m=y=g\), subtracting \(g\) from each of the three terms gives
\[
\begin{aligned}
L_0&=\min(\Delta-h+1,0,1-\lceil h/2\rceil),\\
U_0&=\max(-1,-h,(\Delta-h-1)/2),\\
L_+&=\min(\Delta-h,2,1-\lfloor h/2\rfloor),\\
U_+&=\max(0,-h,(\Delta-h-1)/2),\\
L_-&=\min(\Delta-h,0,-\lfloor h/2\rfloor),\\
U_-&=\max(0,-h-2,(\Delta-h-3)/2).
\end{aligned}
\]
These evaluate to the following complete table. Arc pairs mean \((\lambda-g,U-g)\); seed endpoints are ordinary, unshifted endpoints.

| \((\Delta,h)\) | \((m,y)\) | \(Q\) | \(Q+t_+\) | \(Q+t_-\) | Seed \(+\) | Seed \(-\) | Smallest admissible \((p,g,B)\) |
|---|---|---|---|---|---|---|---|
| \((3,0)\) | \((g,g)\) | \((0,1)\) | \((1,1)\) | \((0,0)\) | \([0,1]\) | \([-1,0]\) | \((7,2,2)\) |
| \((3,2)\) | \((g,g)\) | \((0,0)\) | \((0,0)\) | \((-1,0)\) | \([0,0]\) | \([-1,0]\) | \((11,5,3)\) |
| \((3,4)\) | \((g-1,g)\) | \((-1,-1)\) | \((-1,-1)\) | \((-2,-1)\) | \([0,0]\) | \([-1,0]\) | \((11,6,2)\) |
| \((4,1)\) | \((g,g)\) | \((0,1)\) | \((1,1)\) | \((0,0)\) | \([0,1]\) | \([-1,0]\) | \((11,4,3)\) |
| \((5,0)\) | \((g,g)\) | \((0,2)\) | \((1,2)\) | \((0,1)\) | \([-1,2]\) | \([-2,1]\) | \((11,3,3)\) |

For the special \((3,4)\) row, the normalized triples are explicitly
\[
\begin{array}{c|cc}
&\lambda\text{ terms}&U\text{ terms}\\ \hline
Q&(1,-1,-1)&(-2,-3,-1)\\
Q+t_+&(0,1,-1)&(-1,-3,-1)\\
Q+t_-&(0,-1,-2)&(-1,-5,-2).
\end{array}
\]
Taking minima/maxima reproduces every special-row entry.

For \(\Delta_0=\Delta\), the integer QS windows are:

| \(\Delta\) | Positive target | Negative target |
|---|---|---|
| \(3\) | \([0,1]\) | \([-1,0]\) |
| \(4\) | \([0,1]\) | \([-1,0]\) |
| \(5\) | \([-1,2]\) | \([-2,1]\) |

Every table seed lies inside its required window.

Availability also checks:
\[
g\le p-B-3\le p-5\quad\Longrightarrow\quad2g\le n-3.
\]
For \((3,4)\), \(g=B+4\ge6,\ p=2g-1\), and
\[
3+2(g-2)=2g-1=n-B-4.
\]
Thus the packing lemma applies at equality. NW supplies no wrap; GS(a) supplies the canonical intersection or an actual contradiction.

The “smallest” triples account for primality: the \(B=2\) candidates in families \((3,2),(4,1),(5,0)\) have \(p=9\), so their first admissible prime is \(11\).

**T2.5 — Assembly and small primes.**  
`P/c6/proof-S2wide.md:78`, `:84`.

Each run gets a quality seed or an actual-empty interval. Since \(n_{\rm ev,al}=0\), SEED-G applies.

For \(B=1\), \(k=p+g+1\) and
\[
H=p-1-\kappa=p-g-2.
\]
After rotating the unique anti run to position zero, these are exactly W(p,g), including its reflection-excess condition; see `P/c3/proof-WALL.md:15`.

The bounds \(3g\le p+4\) and \(3g\ge p+5\) exhaust integer \(3g\). W-ALL applies for \(p\ge5\); SEED is used only for \(p\ge11\), as required by `P/c6/c5-fixes/proof-SEED-r3.md:165`.

At \(p=5\), only \(g=B=1\) is possible. At \(p=7,B=1\), \(1\le g\le3\), and \(3g\le9<11=p+4\). For \(B\ge2\), \(\kappa\ge3\) forces \(p\ge7\), and the integer alternatives \(B\ge g+1\) or \(g\ge B\) are exhaustive.

The corollary is correctly assembled, including the smallest \(\kappa\). It needs no finite or computer-assisted exclusion, and no unreviewed LB result.

## T3: A0 and C0-all hand audit

**T3.1 — Setting and Kill equivalence.**  
`P/c6/proof-A0.md:10`; `P/c3/proof-C-r1.md:19`, `:43`.

The parameter identities give
\[
k=p+g+B-E/2,\qquad
k\ge2g+2B+3,\qquad
g+B+E/2\le p-3.
\]
Also \(E\) is even, \(d_t\le E+1\), and
\[
\sum bh_t=2p-D=k-2g.
\]
This sum is positive and strictly less than \(k\). Therefore \(Z\) is proper, and integrality excludes \(Z=\varnothing\).

“Proper” means nonempty and different from \([k]\); see `inverse-parity/proof-PAR-K0.md:13`. For such patterns, all reflection runs odd gives \(\beta=0\), so
\[
\lambda(Q)=\min(p-m+1,D_Q+m-g,\lfloor(D_Q+B)/2\rfloor+1).
\]
For integer \(X_Q\), being strictly below each term is respectively equivalent to
\[
X_Q+m\le p,\qquad
\Phi(Q)\ge g+1,\qquad
bh(Q)\le B.
\]
Thus the Kill equivalence is exact.

**T3.2 — A0.**  
`P/c6/proof-A0.md:24`.

The endpoint \(Z\) meets the threshold, while the empty prefix has \(\Phi=0\); hence a first nonempty crossing exists even if \(\Phi\) is nonmonotone. Integrality gives \(\Phi(P')\le g\). Since \(P'\subseteq Z\),
\[
X_{P'}+m(P')=\Phi(P')+bh(P')\le g.
\]
Adding one vertex changes the block count by at most \(1\), including when it joins or merges blocks. On a defect,
\[
x_t\le\lfloor d_t/2\rfloor
\le\lfloor(E+1)/2\rfloor=E/2.
\]
Therefore
\[
X_P+m(P)\le g+E/2+1\le p-B-2<p.
\]
The other Kill conditions follow from \(\Phi(P)\ge g+1\) and \(bh(P)\le0\). The set is nonempty and proper because it lies in proper \(Z\).

A0 uses only scalar NMH identities, integer coordinates, \(\sum x=p\), and the violated proper-pattern inequality in (L). It needs no avoidance assumption, seed bound, count condition, or (A*).

**T3.3 — Case B and the partition.**  
`P/c6/proof-A0.md:42`.

The imported identity
\[
\Delta=-f(Z)-m(Z)-n_{\rm ev}/2-\mathrm{sur}
\]
uses no count hypothesis. Its signs are correct:
\[
f_{\rm aligned}\ge0,\qquad f_{\rm pair}=-1,\qquad
f_{\rm anti}=-\lceil(b+1)/2\rceil.
\]
Dropping aligned contributions and extending pair/anti sums gives
\[
n_{\rm ev}/2
\le n_{\rm pr}+\frac{B-n_{\rm pr}+n_{\rm an}+n_{\rm ev,an}}2-1.
\]
Using \(n_{\rm ev}=n_{\rm pr}+n_{\rm ev,an}+n_{\rm ev,al}\) yields exactly
\[
n_{\rm ev,al}\le B+n_{\rm an}-2.
\]

The intermediate B1+ bound
\[
|X_o|\ge2\Delta+s_0
\]
is unconditional; its final rounding under count assumptions is a separate step. B2+ needs the established bound \(|X_o|\ge2\Delta+1\), the NMH identities and (L), with no count hypothesis or \(2g\le p\) assumption. See `P/c6/c5-fixes/proof-Cplus-r2.md:75`, `:80`.

For case (i),
\[
s_0\ge k-g-3B+1+n_{\rm pr}
\ge g-B+4+n_{\rm pr}\ge4.
\]
The target’s weaker \(\ge1\) is valid.

For case (iii),
\[
2g+1\le g+B\le p-3\quad\Longrightarrow\quad2g\le p-4.
\]
Also \(2g+B\ge3g+1>p\), hence \(2g+B\ge p+1\), and
\[
E\le2p-2g-2B-6\le p-B-7.
\]
Consequently
\[
2E\le2p-2B-14\le2p-2B-1.
\]
Since \(k-g-2B=p-B-E/2\), this is sufficient for
\[
E\le2(k-g-2B)-1.
\]
Together with \(n_{\rm ev,al}\le E\),
\[
s_0\ge(k-g-2B)-E/2\ge\tfrac12.
\]
Integer \(|X_o|\) and \(\Delta\) then give \(|X_o|\ge2\Delta+1\).

Cases (i)–(iii) exhaust integer \(B,g\). No arithmetic slip was found.

**T3.4 — C0W and dependency.**  
`P/c6/proof-A0.md:56`; `P/c6/proof-C0WB.md:27`, `:33`.

Case (ii) has exactly C0W’s hypotheses. Its proof uses only (L) and scalar NMH facts:

- DF forces \(c_t\le g-1\) when \(bh_t\le1\), because \(x_t\) is below the singleton minimum’s first and third terms.
- Cheap weights \(w_t=c_t+1\) satisfy \(1\le w_t\le g\).
- Their total satisfies
  \[
  W(\mathrm{cheap})\ge p+2g-A/2\ge2g+\tfrac12,
  \]
  hence is at least \(2g+1\).
- Heavier alternating classes of the cheap paths produce an independent set of weight at least \(g+1\). The all-cheap case is handled by deleting one run first.
- The first crossing produces a nonempty proper independent pattern with
  \[
  g+1\le\Phi(P)\le2g,\quad bh(P)\le g+1\le B,
  \quad X_P+m(P)\le3g+1\le p.
  \]

The final violated lower bound contradicts (L). No low-run \(k\le p\) hypothesis enters. The review-status correction is M1 above.

**T3.5 — Complete certification and quantifiers.**  
`P/c6/proof-A0.md:66`.

Both routes supply **all** of (L) before the finisher:

1. **Quality seeds:** P0/ARC give canonical lifts and singleton bounds; SCW-G proves certification; SL gives every proper-pattern lower bound; the pin gives \(\sum x=p\). These steps precede C0+ in `P/c6/proof-SEEDG-r2.md:66`, `:103`, `:152`, `:170`.

2. **Relaxed seeds:** use the corrected argument at `P/c6/proof-SEEDGstar-r1.md:62`:
   \[
   \min_i U_i+\min_j T_j
   =\min_{i,j}(U_i+T_j)\ge\min_{i,j}B_{ij}=L_A(d).
   \]
   Integrality gives the ceiling bound; similarly for \(L_B\). P2 supplies the two-run base case. The pin supplies \(\sum x=p\), and canonical lifts supply singletons.

   The r0 phrase “at least each” at `P/c6/proof-SEEDGstar.md:42` must not be inherited. PIN is in fact automatic for genuine seeds:
   \[
   b_a-\lambda(\{a\})
   \le p-\lambda(\{a\}^c)-\lambda(\{a\})\le p-1.
   \]
   Retaining it as an extra hypothesis is harmless.

The corollary’s global actual-empty alternative avoids star-r0’s per-run quantifier defect. “As in” imports the requirement of seeds for every run; the explicit wording in M1 makes this unambiguous. An actual-empty intersection for **one actual run** suffices. An empty abstract QS/QS* window alone does not.

Thus, conditional on C0W, the corollary removes the count restriction from the **seed-certified implications** of SEED-G and SEED-G*. It does not establish universal seed existence. This is consistent with the reviewed certification proofs.

**T3.6 — Integer counterexample.**

None was found. The hand argument excludes every integer solution of (L), conditional on the stated C0W import. No relaxed-window solution or group counterexample is asserted.

## Dependency and scope checks

No imported mathematical statement is used outside its needed hypotheses. In particular, T3 uses the unconditional intermediate B1+ estimate and B2+ construction, rather than applying the entire count-restricted C+ theorem without its assumptions.

T1 and T2 independently supply their packing arguments; neither silently relies on unreviewed LB Lemmas RZ/RZ2. Their LB references identify provenance or separate controls.

No [F] receipt is used as a premise. Receipt statistics were not independently reproduced. The scope sentences at `P/c6/proof-RZwide.md:65`, `P/c6/proof-S2wide.md:90`, and `P/c6/proof-A0.md:71` do not claim NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, or an ordered-Olson theorem.

Per-target counts **(FATAL/MAJOR/MINOR)**:

- **T1: 0/0/0**
- **T2: 0/0/0**, plus one optional MINOR remark
- **T3: 0/0/1**

**Correctness:** the mathematical chains check out, with T3’s dependency qualification made explicit. **Novelty:** no external novelty or priority assessment was performed. **Significance:** T1/T2 give uniform coverage of the all-single-letter NMH subcase; A0 and C0-all remove count restrictions from the lifted-system finisher, while seed existence for general words with excess remains an independent obligation.