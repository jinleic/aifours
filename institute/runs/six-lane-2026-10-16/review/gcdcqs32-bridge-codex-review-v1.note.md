BRIDGE-HOLDS

- **FATAL:** None found.
- **MAJOR:** None in the mathematical bridge.
- **MINOR:** `check_ingredients.py` checks I1 and I3, but has no I2 mode. The builder’s header and class-count assertions do not establish I2’s validity. I independently checked the pinned I2 in memory and resolved this verification boundary. Checker lines 113–120; builder lines 39–40, 71–80.

References below: [TZ](/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt), [checker](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups/code/check_ingredients.py), [builder](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups/code/build_c23.py), [note](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups/evidence/gcdcqs32-c23/construction-2.3-hypotheses.md). All references use actual file line numbers.

**1. Construction 2.3 applies.**

Its hypotheses specialize as follows. Both named code hashes, all three ingredient hashes, and the primary-source hash match their supplied pins.

| Hypothesis | Audit |
|---|---|
| \(m=8,g=n=4,s=0,\ K_1=\{4\},K=\{5\}\) | \(mgn+s=128\equiv2\pmod6\), \(mk_1+s=32\equiv2\pmod6\). This is precisely the proved \(2\bmod6\) case. TZ 444–450. |
| I1: \(1\)-FG\((3,(\{4\},\{5\}),16)\), type \(4^4\) | Checker verifies the group partition, block sizes, valid subsets, unique pair coverage by \(\mathcal G\cup\mathcal B\), and unique triple coverage by \(\mathcal G\cup\mathcal B\cup\mathcal T\). It passes: 16 B-blocks and 48 T-blocks. TZ 248–255; checker 27–44. |
| I2: gcDCQS\((8^4:0)\) | Independent check passes: 1,184 quadruples; all 4,736 admissible triples covered uniquely; all 32 derived designs partitioned into 16 PPCs, exactly four avoiding the seven-point hole. Class profile is \(10^{12}7^4\) at every point. TZ 211–220, 281–288. |
| I3: FDGDD\((3,4,5\{8\})\) | Checker verifies a transverse GDD, unique coverage of every transverse triple, and a complete Kirkman-frame decomposition at every point. It passes: 1,280 quadruples and 16 frame classes at each of 40 points. These conditions establish the FDGDD required by TZ, independently of the FDH label. TZ 237–247; checker 76–110. |

The builder’s assumption that each B meets every original group once follows from I1’s **pair** axiom: two points in one group already have their unique covering member of \(\mathcal G\cup\mathcal B\). A four-point B therefore meets all four groups. No affine-geometric assertion is needed. Builder 46–49.

The frame multiplicities are checked **implicitly**, despite `miss` being collected without a histogram assertion at checker 98–109. A derived frame is a GDD of type \(8^4\), so every point occurs in \(24/2=12\) triples. Let \(c\) be its number of classes and \(c_H\) the number omitting group \(H\). Since every class is a full PC off its omitted group,
\[
c-c_H=12,\qquad \sum_Hc_H=c.
\]
Thus \(c=16\) and every \(c_H=4\), exactly the multiplicity required at TZ 473–476. Direct inspection also gives \((4,4,4,4)\) at all 40 points. **There is no missing multiplicity hypothesis.**

**Arbitrary assignment works**, provided it is a bijection between the 12 nonavoiding local classes and
\[
(B\setminus\{x\})\times\{1,2,3,4\}.
\]
No additional relation between a class’s contents and its assigned \(y\) is required. Builder 71–80; note 35; TZ 456–461.

Here is the disjointness argument behind TZ 498–531:

- For \(y\notin G(x)\), pair uniqueness supplies the unique \(B_1\supset\{x,y\}\). Distinct T-blocks containing \(x,y\) cannot share another point \(z\), because that would cover \(\{x,y,z\}\) twice. Such a T also cannot share another point with \(B_1\). Consequently the FDH class supports \((T\setminus\{x,y\})\times I_8\) are mutually disjoint and disjoint from the **entire** local \(B_1\)-support. Any assigned local PPC can therefore be added.
- For \(y\in G(x)\setminus\{x\}\), no T containing \(x,y\) contains another point of \(G(x)\): that triple is already covered by the group. Its frame supports are mutually disjoint and avoid the enlarged hole.
- Distinct B-blocks through \(x\) intersect only at \(x\), by pair uniqueness. Their avoiding classes omit the whole \(x\)-fibre, so their unions are disjoint and hole-free.

Every local derived triple enters exactly one global class because the local resolutions are partitions and their class assignments are bijections.

The quadruple union also follows from coverage, independently of execution. A lifted triple projecting to two base points uses their unique B-block; a triple projecting to three distinct base points uses its unique B- or T-block. Triples inside an enlarged group are forbidden: B is transverse, and T cannot contain three points of an original group. These same uniqueness arguments prevent duplicate coverage between ingredients. TZ 453–483.

The resulting counts are
\[
15\cdot4+4=64,\qquad 3\cdot4+4=16
\]
classes and hole-free classes. Pair/triple coverage gives four T-blocks through every base pair and four B-blocks through every base point, explaining the reported profile:
\[
(10+4\cdot8)^{48}(4\cdot8)^{12}(4\cdot7)^4
=42^{48}32^{12}28^4.
\]

**2. Corollary 2.6 yields the stated infinite family, with a separate argument for 128.**

For its \(m=32\):
\[
32\equiv8\pmod{12},\quad
\gcd(32,4)=4\ne2,\quad
\gcd(32,18)=2\ne3.
\]
For every integer \(t\ge2\), put \(v=4^t\). Then \(v\equiv4\pmod{12}\), \(4m=128\equiv2\pmod6\), and \(mv\equiv2\pmod6\). All arithmetic conditions of Construction 2.4 and Theorem 2.5 hold. TZ 568–572, 680–688.

The imported existence results have these exact scopes:

- **Theorem 2.5(1), citing Xu–Bao–Ji [21, Corollary 3.2]:** \(2\)-RSQS\(^*(4^t)\) for every \(t\ge2\), not arbitrary admissible orders.
- **Theorem 2.5(2), citing [9,21]:** RDTD\((3,4,m)\) for positive \(m\) satisfying both stated gcd exclusions; this supplies \(m=32\).
- **Lemma 3.4:** mcDSQS\((32)\), among the specific orders \(20,26,32\). TZ 903–907. I additionally checked its Appendix B construction: 40 cyclic base blocks develop to 1,240 quadruples, and the derived design at zero has 155 triples partitioned into 16 PPCs. Translation supplies every other point. TZ 1321–1372.
- **Equation (1.1), citing Vanstone et al. [19]:** the global minimum STS colouring value for orders \(1\bmod6\), excluding 7 and 13. TZ 110–125.

The first two are used as published existence theorems reported in the pinned source; their original papers were not read. No general FDH existence theorem from the inaccessible journal body is needed.

Construction 2.4 supplies gcDCQS\((32^{\,4^t}:0)\), and Construction 2.1 fills it using mcDSQS\((32)\). The nominal additional input gcDSQS\((32,0)\) is the same mcDSQS\((32)\): an empty hole imposes no additional condition. TZ 227–236, 292–293, 684–693.

Now
\[
32\cdot4^t=2^{2t+5}=2^{2n+1},
\qquad n=t+2.
\]
Thus \(t\ge2\) gives **every \(n\ge4\)**, beginning at 512. This agrees exactly with TZ 1111–1113.

**mcDSQS(128) follows separately:** apply Construction 2.1 directly to the accepted gcDCQS\((32^4:0)\). Fill all four groups with the published mcDSQS\((32)\). At each point, pair the filler’s 16 derived PPCs with the 16 exterior hole-free PPCs; retain the other 48 classes. The completed design has 85,344 quadruples and 64 colours at every derived STS(127). This is optimal because
\[
\left\lceil\frac{127\cdot126/6}{\lfloor127/3\rfloor}\right\rceil
=\left\lceil\frac{2667}{42}\right\rceil=64.
\]
TZ 299–326. Corollary 2.6 itself starts at 512.

**3. The accepted finite predicate matches the source definition.**

At \(x\), the derived ground set has 127 points and hole \(G(x)\setminus\{x\}\) of size 31. Therefore TZ 211–220 requires
\[
r=\chi'(127)=64,\qquad s_{\rm gc}=64-\frac{127-31}{2}=16.
\]
With empty stem, the stem-frame condition is vacuous. TZ 281–288.

Crucially, the 16 avoiding classes need only be **PPCs**, not PCs. The four size-28 classes therefore cause no mismatch. TZ 69–70, 213–226.

**Unsupported stronger statement:** the certificate does not establish that the *incomplete* STS\((127,31)\) itself has chromatic index 64. The definition uses \(\chi'(127)\), the minimum for complete STS(127)s. Minimum colouring of the completed STS(127)s is established by the filling argument above.

A fully checked labelled certificate proves unrestricted existence even if symmetry constrained its search. No symmetry restriction survives as a qualification on that existential conclusion.

**4. Exact defensible result and significance.**

The accepted raw witness establishes gcDCQS\((32^4:0)\). Together with the published mcDSQS(32), it gives mcDSQS(128); together with the stated published recursion inputs, it gives mcDSQS\((2^{2n+1})\) for every \(n\ge4\).

Its specialist significance is that it supplies precisely the \(v=32\) auxiliary object requested in §4(2) of the pinned version and activates that paper’s recursion. Novelty and priority remain unassessed. No new general method or Lean formalization of the infinite family is established.