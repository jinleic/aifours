# Elementary six-index-seven completion and Sun8 for GL(3,2)

**NEW WRITTEN PROOF CANDIDATE, not reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:30:58 PDT 2026**. This is a **proof-dependency improvement**, not a claim of a new group family: the earlier parent A1/A2 union already supported Sun8 for GL/SL/PSL3(2) at its named NC7/A7/Eisenstein boundaries. The new argument below proves the concrete GL(3,2) six-coset complement AND its Sun8 consequence using only elementary F2 linear algebra, finite group/index facts and the written arguments here. It imports neither Sun7 nor the earlier NC7 theorem nor an A7/Eisenstein theorem. No PSL2(7)-to-GL3(2) isomorphism is used or certified here.

## 1. Claims

Let G=GL(3,F2). Then:

1. Every SIX pairwise-disjoint actual left cosets of index-seven subgroups of G have an actual seventh index-seven left coset as their EXACT complement in G.
2. Every EIGHT pairwise-disjoint actual left cosets of arbitrary subgroups of G have a pair whose subgroup indices have gcd>=8: `Sun_8(G)`.

There is no covering assumption on the initial six or eight cosets. Statements are for this exact group only, not an unrestricted Sun8 or a normal-extension/composition-factor theorem.

## 2. Elementary group facts and absence of subgroup indices 2–6

Let V=F2^3. An invertible matrix is an ordered basis of V: the three columns can be chosen in `7*6*4=168` ways. Thus |G|=168. There are seven nonzero vectors and seven 2-dimensional planes (each plane is the kernel of one unique nonzero covector). G acts transitively on nonzero vectors and on planes by basis extension; point and plane stabilizers therefore have order24 and index7.

G is perfect. Elementary transvections `I+E_ij` generate G by Gaussian elimination: over F2 the only nonzero scaling is1 and row swaps are products of three row additions. For distinct i,j,k, direct multiplication gives

    [I+E_ik, I+E_kj] = I+E_ij.

Thus every generator is a commutator and G=[G,G].

Every finite group J whose order divides24 is solvable. For completeness: if 3 does not divide |J|, J is a 2-group and is solvable by the class-equation centre induction. Otherwise a Sylow3-subgroup has number 1 or4, since its number divides a power of2 at most8 and is 1 modulo3. If the number is1, it is normal and the quotient is a 2-group. If it is4, the conjugation action on the four Sylow3-subgroups has image in solvable S4 and kernel contained in a Sylow3 normalizer of order `|J|/4<=6`; groups of order dividing6 are solvable. In both cases J is an extension of solvable groups. S4 is solvable via `1<V4<A4<S4`. These are elementary finite-group facts, not a subgroup classification of G.

If H<G had index d with 2<=d<=6, the transitive left-coset action G->S_d would have image order dividing both168 and d!, hence dividing `gcd(168,6!)=24`. That image would be simultaneously a quotient of perfect G and a solvable group, hence trivial; a trivial action cannot be transitive on d>1 points. Therefore G has NO subgroup indices2,3,4,5,6.

## 3. Every index-seven subgroup is a point or plane stabilizer

Let H have index7, so |H|=24. Consider its action on the seven nonzero vectors of V. All H-orbit sizes divide24. If H fixes a nonzero vector, it equals that vector's order24 stabilizer.

Suppose H has no fixed nonzero vector. An H-orbit of size2, say {u,v}, would make u+v a nonzero fixed vector, since H permutes u,v; this is impossible. Orbit sizes are therefore among3,4,6, and their sum is7, so the orbit decomposition is3+4.

Let {u,v,w} be the 3-orbit. Its sum u+v+w is H-fixed. As H has no nonzero fixed vector, the sum is0. Thus w=u+v and the orbit is exactly the three nonzero vectors in the plane L=span(u,v). H stabilizes L and, by equal order24, is the full plane stabilizer. This proves the list completely without importing a catalogue or simplicity of G.

## 4. Actual coset incidence model

For each nonzero vector p and target vector a define

    P(p,a)={T in G:T p=a}.

It is an actual left coset of the stabilizer of p: choose T0 with T0 p=a; then P(p,a)=T0 Stab(p). For nonzero covectors alpha,beta define

    L(alpha,beta)={T in G:alpha T=beta}.

It is an actual left coset of the stabilizer of beta: choose T0 with alpha T0=beta; then L(alpha,beta)=T0 Stab(beta). A nonzero covector and its kernel uniquely identify each plane over F2. By Section3 these 49+49 labelled families include ALL index7 cosets. Point and covector stabilizers are distinct: a point stabilizer acts transitively on the six other nonzero vectors and hence cannot fix any plane; so the two label types do not represent the same coset.

The following pair-intersection rules are elementary consequences of extending independent vectors/covectors to bases:

- Two distinct P(p,a),P(p',a') are disjoint iff either `p=p'` and `a≠a'`, or `p≠p'` and `a=a'`. If both source and target pairs are distinct, they are pairs of independent nonzero F2 vectors and some invertible map sends one pair to the other.
- Two distinct L(alpha,beta),L(alpha',beta') obey the SAME rule for their two covector labels, by applying the preceding basis argument to the dual action.
- P(p,a) and L(alpha,beta) intersect iff `beta(p)=alpha(a)`. Necessity is evaluation of alpha T=beta at p. Conversely, when this equality is0, map ker(beta) isomorphically to ker(alpha), taking p to a, and map a complement to a complement. When it is1, map p to a and choose any isomorphism ker(beta)->ker(alpha). In either case the resulting invertible T satisfies both constraints.

All three rules concern actual group elements and actual left cosets; they are not a numerical intersection heuristic.

## 5. A Fano-incidence bound

Let A be a nonempty set of m distinct nonzero vectors and B a nonempty set of n distinct nonzero covectors of V, and suppose `beta(a)=e` for EVERY a∈A,beta∈B, with fixed e∈F2.

- If e=0, when m=1 there are only three nonzero covectors annihilating its member, so n<=3. When m>=2, the two distinct nonzero F2 vectors are independent, so their common annihilator has at most one nonzero covector; then n<=1 and m<=3. Hence m+n<=4.
- If e=1 and m,n>=2, two distinct vectors are independent, so at most two covectors take value1 on both; symmetrically at most two vectors give1 for two distinct covectors. Hence m,n<=2 and m+n<=4. If m=1 then n<=4; if n=1 then m<=4. Thus m+n<=5.

This covers every nonempty pair of incidence sets, including repeated-value and rank boundaries; the labels within A,B themselves are distinct.

## 6. Every six disjoint index-seven cosets have a seventh complement

By the same-type rule of Section4, a pairwise-disjoint family of point cosets with at least two members has either ONE common source p and distinct targets a, or ONE common target a and distinct sources p. Indeed after choosing two, a third with a different source and a different target from the fixed pattern cannot be disjoint from both. The identical row/column statement holds for covector cosets. A singleton may be placed in either mode.

Take six pairwise-disjoint index7 cosets; suppose m are point type and n=6−m are covector type.

If m=0 or n=0, the six same-type cosets share one coordinate and have six distinct values of the other. Choose the missing seventh nonzero value; the resulting index7 coset is disjoint from all six.

Now suppose m,n>0. A singleton may be assigned either orientation, so choose modes consistently with the following exhaustive analysis.

**Matched modes.** If all point sources are one p and all covector first labels are one alpha, the cross-disjointness condition `beta_j(p) != alpha(a_i)` for all i,j forces a common c∈F2 with

    alpha(a_i)=c for all i,      beta_j(p)=1−c for all j.

There are respectively 3 and4 possible nonzero values when c=0, and 4 and3 when c=1. The two capacities sum to7. Since m+n=6, at least one side has an unused allowable label; adding its point or covector coset preserves ALL same-type and cross disjointness.

The other matched case, all point targets one a and all covector second labels one beta, is identical with `beta(p_i)=c` and `alpha_j(a)=1−c`: again capacities are3 and4, and an unused label supplies the seventh coset.

**Crossed modes.** If point sources are one p while covector second labels are one beta, cross disjointness says `alpha_j(a_i)=1−beta(p)` for every pair. Section5 bounds m+n<=5. The case of common point target a and common covector first label alpha similarly gives `beta_j(p_i)=1−alpha(a)` for every pair and the same bound. Neither crossed mode can contain six cosets.

The cases exhaust all families; if one side is a singleton it may be assigned the appropriate matched orientation. Hence a seventh actual index7 coset always exists and is disjoint from the initial six. Each such coset has |G|/7=24 elements, so seven disjoint ones have total size168=|G|. The seventh is therefore the EXACT complement, proving Claim1. □

## 7. Sun8(G) without the Sun7 import

Suppose eight actual disjoint G-cosets have indices n_i with `gcd(n_i,n_j)<=7`. Each n_i divides168 and n_i>=7 by Section2; an index1 coset is the whole group and cannot be disjoint from another.

If no n_i equals7, at most TWO indices are not divisible by7: such an index divides24 and is at least7, so it lies in `{8,12,24}`; two occurrences of8, two of12, or an occurrence of24 with either8 or12 have gcd>=8. At most TWO indices ARE divisible by7: they are `7d_i`, where d_i>1 divides24, and the gcd bound makes the d_i pairwise coprime. Since every d_i>1 has prime2 or3, at most one d_i can contain2 and at most one can contain3. Altogether there could be at most four labels, contradicting eight. Hence some original coset has index7.

Every other original index must be divisible by7: its disjoint coset and the index7 coset have index gcd>=2 (coprime-index cosets always intersect). Write all eight as n_i=7d_i, with d_i|24 and d_i pairwise coprime. At most two d_i exceed1, so at least SIX original cosets have index7.

By Claim1, these six have an index7 coset xH as their exact complement. The remaining two original nonempty cosets are disjoint from the six and are thus contained in xH. Pick a representative y_i in each; since y_i H=xH and y_i U_i⊂y_i H, each U_i is a subgroup of H. Translating both cosets into H gives two disjoint actual H-cosets with subgroup indices

    [H:U_i]=[G:U_i]/[G:H]=d_i.

These d_i are coprime. But two actual finite-index cosets of coprime index always intersect: the diagonal map H/(U_1∩U_2)->H/U_1×H/U_2 is injective and its domain index is a common multiple of the two coprime indices no larger than their product, so it is onto. Contradiction. Therefore `Sun_8(GL(3,2))`. □

## 8. Two bounded exact computational checks

These are evidence for the finite identities, not substitutes for the proof and not independent-family/formal acceptance.

1. Actual group/subgroup/coset enumeration: `frontier-20261028-gl32-coset-search.py`, SHA256 `92998acba482388c32f5d5f22aa04010c020fbfeed36156845428622f371290e`, generated all168 invertible matrices and their finite-generated subgroups, checked closure and all actual left-coset partitions, then searched the exact disjointness/gcd graph. Output: 179 subgroups, 6746 actual left cosets, 5200 clique-search nodes, no eight-coset counterconfiguration; bounded run wall time9.23 seconds. Its graph search is not independently formally checked.
2. Six-complement verification using the same matrix/subgroup enumeration: `frontier-20261028-gl32-index7-six-cover-check.py`, SHA256 `1dda7d01784b480e41165a2c738c9e7e6439bf9e64ad4994ccd4017c9cda6bc4`. Actual output: 98 index7 cosets, 1568 disjoint unordered six-sets, 0 whose complement is not an index7 coset, PASS; observed Wed Oct28 17:28:53 PDT 2026. It reuses checker1's enumerator, so is not a second independent group enumeration.
3. Separately written Fano point/covector incidence checker: `frontier-20261028-gl32-fano-incidence-check.py`, SHA256 `8bcd9d8b46079fb0627d72cd0e773b80a37b9f123c40853456343829f259875a`. It constructs only the 98 point/covector labels and Section4 intersection relations, not checker1's matrices/subgroups. Actual output: 98 labels, six-set completion counts `{1: 1568}`, PASS; observed Wed Oct28 17:30:11 PDT 2026. Its connection to ALL actual index7 subgroups is established by Sections3–4, not by the finite label calculation alone.

The two six-set checks are independent representations but do not satisfy a three-checker/cross-family/human/formal verification gate.

## 9. Prior scope and remaining obligations

The parent disposition `sun-A1-A2-entire-all-fields-parent-v1.md` already supports the broader finite-field PSL/SL/PGL families, including the168-order q=2 A2 base, and identifies NC7 with an A7/Eisenstein dependency. This packet does NOT claim first discovery, full-family progress or that older imports are thereby retroactively removed; rather, if independently reviewed, it supplies a new elementary substitute for the concrete GL(3,2) six-coset complement and verifies Sun8 of this group directly. The prior parent report and evidence remain frozen. Full isomorphism/transport to other named presentations requires its own proof or named import.

No unrestricted Sun8, arbitrary perfect-group extension, finite-simple classification, source-priority/novelty, independent-family/human/kernel or publication acceptance follows. Parent and reviewers must read the entire proof and compare its explicit scope with the prior source before adoption. Previously held outputs are not used as premises or retrospectively validated.
