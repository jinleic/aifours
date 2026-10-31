# F675 independent q=7 actual-coset author candidate

**Status:** unadopted, nonblind GENERAL FINITE SOURCEAUTHOR reconstruction. The written argument below proves the stated q=7 result *conditional on the imported q=7 maximal-subgroup classification*, subject to independent mathematical review. The accompanying independent finite source is **NOT RUN and NOT TESTED**; it supplies no observed enumeration, passing control, or execution result. No parent GO or parent disposition is implied. This note does not alter the already adopted conditional f≥2 theorem.

## Exact claim and inputs

For a group X, B7(X)≤r means that every r+1 pairwise-disjoint **actual left cosets** of finite-index subgroups contain two subgroup indices with gcd at least 8. J7(X)≤s makes that conclusion for every s+1 proper subgroup **labels**, allowing repetition and not requiring disjointness. My q=7 conclusion is **B7(PSL₂(F7))=7 and no finite J7 bound holds**. In particular this is not a conclusion about arbitrary quotient shadows, a multiset of index labels standing in for cosets, all prime powers, a normal-extension theorem, or unrestricted Sun8.

The non-elementary import is only the q=7 consequence of the classification rendered in frozen packet S3: there are two conjugacy classes of maximal S4 subgroups of index 7 and a class of projective-line stabilizers of index 8, with no other maximal types. See the literal excerpt of Giudici, Theorems 2.1–2.2, <https://arxiv.org/pdf/math/0703685v1>, and Beltrán–Viudez, Theorem 3.2, <https://arxiv.org/html/2607.09144v2#S3.Thmtheorem2>. I did **not** follow those links, authenticate the extraction, or prove their classification. In particular the equality-looking inequality glyphs in the PDF extraction are not used as equalities; the HTML excerpt states the relevant restrictions. The actual finite checker below does not assume the group isomorphism name S4 for its enumeration and would independently check the q=7 maximal counts if it were successfully run and its source and result independently reviewed; it cannot authenticate the general classification.

The frozen S1 is the nonblind F668 proposal, including its new q=7 argument; S2 is the f≥2 parent disposition and explicitly leaves that q=7 extension unadopted. This body reconstructs the relevant assertions afresh from these original assigned inputs, not from stopped reviews or their consumers.

## 1. Matrix group and elementary facts

Let G=SL₂(F7)/{±I}. A nonzero first column has 48 choices, and the determinant-one equation gives 7 choices for the second, so |SL₂(F7)|=336 and |G|=168. The center of SL₂(F7) is {±I}: commuting with both upper and lower unipotents forces a scalar, and determinant one makes its square 1. Let

`U(s)=[[1,s],[0,1]]`, `V(s)=[[1,0],[s,1]]`, and `D=diag(2,4)`.

Upper and lower unipotents generate SL₂(F7) by row elimination, and U(1), V(1) generate each unipotent family by taking powers. Moreover D U(s) D⁻¹=U(4s) and D V(s) D⁻¹=V(2s), so their commutators with D give U(3s) and V(s). Because 3 is invertible, G is perfect. Consequently a nontrivial image of G cannot be solvable. In particular G has no proper index 2, 3 or 4 subgroup, since a transitive coset action of such a degree would give a nontrivial image in a solvable symmetric group.

For finite subgroups A,B≤G of coprime indices m,n, the map `G/(A∩B) → G/A × G/B`, `g(A∩B) ↦ (gA,gB)`, is injective. Its domain size is divisible by both m and n and at most mn; hence it is mn, the map is onto, and **every actual left A-coset meets every actual left B-coset**. If a coset `xU` is contained in `yH`, then U≤H and `y⁻¹xU` is an actual left U-coset inside H: indeed y⁻¹x∈H and `(y⁻¹x)U⊆H`.

For the projective-line action, `P={U(s):s∈F7}` has order 7 and fixes exactly one point. Any normalizer of P must fix that point, and its stabilizer is the upper-triangular Borel of order 21. Thus N_G(P) is this Borel. Its quotient by P acts on the six nonidentity translations by the squares `{1,2,4}`, giving two orbits of size 3 which are negatives of one another.

## 2. Both degree-seven actions and their actual incidence

The classification gives fourteen index-7 subgroups, in two conjugacy classes. Every such subgroup H has order 24 and is maximal: any overgroup index divides 7. Its normalizer is H, because a larger normalizer would equal G, making G/H a nontrivial solvable group of order 7. Hence each class consists of exactly seven distinct subgroups.

Consider the action on G/H. P is regular on these seven points: no nonidentity element of order 7 can lie in a conjugate of H, so no such element fixes a point. N_G(P) has order 21 and is transitive; its stabilizer of a selected point has order 3. In P-coordinates that stabilizer has the two 3-orbits above on the six other points. The G-point-stabilizer can therefore have either one suborbit of length 6 or two of length 3. In the latter case a 3-suborbit cannot be self-paired under reversal: it would give an undirected 3-regular graph on 7 vertices, impossible by the handshake lemma. Its reverse is the other 3-suborbit, so it defines a G-invariant tournament. The nontrivial transitive image of G is perfect. If it had odd order, its order would divide 21; every group of order dividing 21 is solvable, since its Sylow-7 subgroup is normal when present and the quotient is cyclic. Thus the image has even order and contains an involution. As a nonidentity permutation it swaps two vertices, reversing their tournament edge, a contradiction. The action is therefore **2-transitive**. This proof applies to both index-7 classes.

Call the seven conjugate stabilizers in the first class points, and let K be a subgroup in the other class. K fixes no point, for then K≤a point stabilizer and equality of their orders would make their classes the same. Its orbit sizes divide 24. An orbit of size 2 would make an index-2 subgroup of K, of order 12, fix both points individually, but a two-point stabilizer has order `168/(7·6)=4`. No orbit has size 1, 2 or 7; therefore the point orbits have sizes 3 and 4. Call the 3-orbit the line associated to K, and use all seven conjugates of K as line labels.

Point 2-transitivity makes the number λ of lines through a pair of points constant. Counting incidences of point pairs and line labels gives `λ·C(7,2)=7·C(3,2)`, so λ=1. In particular the seven line subsets are distinct. Transitivity and incidence counting give three lines through each point. Every two lines meet exactly once: each line meets the other six through its three points, and two lines cannot share two points. The line action is also 2-transitive. The two K-orbits of sizes 3 and 4 show that the G action is transitive on the 21 incident point-line flags and on the 28 nonincident flags separately. No pre-existing Fano-plane coordinate table or GL₃(2) isomorphism is needed.

For points write `P(x,y)={g∈G:g(x)=y}` and for lines `L(a,b)={g∈G:g(a)=b}`. Because the relevant stabilizer is exactly the corresponding index-7 subgroup, each transporter is an **actual left coset**. There are 49 of each type, all 98 sets distinct: a nonempty coset determines its stabilizer by translating any of its elements to the identity. Within one type distinct cells are disjoint exactly if they share a source or share a target; otherwise 2-transitivity gives an intersection of size 4. Across types, flag and antiflag transitivity give

`P(x,y) ∩ L(a,b) = ∅  ⇔  (x incident with a) ≠ (y incident with b)`.

If both flags are incident the intersection has size 168/21=8; if both are nonincident it has size 168/28=6. Thus, over unordered distinct same-type pairs, the disjoint/intersection-4 counts are 588/1764. Over the 49×49 cross-type pairs, the intersection-size 0/6/8 counts are 1176/784/441. These are written consequences of the conditional argument, **not observed checker output**.

## 3. All six-coset completions and the eight-coset consumer

At least three pairwise-disjoint cells of one type share one row or one column: after two cells share a row with different targets, a third disjoint from both must share that row. The same argument continues inductively. Inversion preserves the disjoint family and sends `P(x,y)` to `P(y,x)` (and likewise for L); although an inverse of an arbitrary left coset is generally a right coset, here the inverted transporter is explicitly an actual **left** coset of the target stabilizer. Point/line interchange is also legitimate because the incidence structure has the proved symmetric pair properties.

Take six pairwise-disjoint index-7 cells. If all have one type they lie in one row or column; its omitted seventh cell is their complement. Otherwise, after interchange and possibly inversion, at least three point cells are `P(x,y)` for y in a set Y, with |Y|≥3. If |Y|≥5, a disjoint line cell would require Y to lie in either a 3-point line or its 4-point complement, impossible.

* If |Y|=4, every line cell disjoint from the point cells has source line through x and target the unique line b whose complement is Y. The two chosen source lines through x are distinct; the third source line through x mapped to b supplies the seventh cell.
* If |Y|=3 and Y is a line b, any disjoint line cell has target b and source not through x. Of the four such source lines, the one not used by the three line cells supplies the seventh.
* If |Y|=3 and Y is noncollinear, exactly one line b is disjoint from Y: the three pair-lines are distinct and the seven lines meeting Y number `3·3−3=6`. All three line cells have target b and source through x, using all three such lines. The unique point y₀ outside `Y∪b` gives the seventh cell `P(x,y₀)`.

In every case the seven actual sets are disjoint and each has size 24, so the seventh is exactly the complement of the six. This is the all-six-cliques statement, not merely an assertion about their subgroup labels.

The same proof counts all such six-cliques. The two one-type cases give 98 each. For four point and two line cells, choose a source point, a target line, two of its three admissible source lines, and row/column orientation: `7·7·3·2=294`; the dual case also gives 294. For three and three, collinear Y gives `7·7·C(4,3)·2=392`, and noncollinear Y gives `7·28·2=392`. Thus there are **1568 six-cliques**, completing to **224 seven-coset partitions** because each partition contributes exactly seven six-subsets. These too are authored arithmetic, not observed execution.

Now let an actual disjoint family have all pairwise index gcd at most 7. A subgroup of index 1 contributes G and excludes any other member, so suppose all subgroups proper. Every proper index is divisible by 7 or 8 by the stated classification. If an index-7 cell occurs, every subgroup of index not divisible by 7 has order divisible by 7; an element of order 7 acts as a seven-cycle on both degree-seven actions, so every one of its actual left cosets meets every index-7 transporter. Hence every other index is 7m. If the index is greater than 7, then m>1 and m divides 24. Two such labels must have coprime relative indices, and at most two such m can be pairwise coprime because their only possible prime factors are 2 and 3, including when subgroup labels repeat.

With at most five index-7 cosets, there are at most seven family members. With six, the complement is an actual index-7 left coset `zH`. Two further actual cosets inside `zH` would translate to disjoint actual H-cosets whose relative indices m,n are coprime, contradicting the elementary coprime-index lemma. Seven index-7 cosets fill G. If there is no index-7 coset, there are at most two indices divisible by 7 and at most one remaining index, since all remaining indices are divisible by 8. Thus no bad family has eight members.

Conversely the seven distinct left cosets of any fixed index-7 subgroup partition G, and each pair has gcd(7,7)=7. This is a positive packing of **seven**, not eight; it proves B7(G)≥7 and hence B7(G)=7. Repeating the same index-7 *label* arbitrarily often proves that no finite J7 bound holds, but those repeated labels are not arbitrarily many disjoint actual cosets.

## 4. Full census and intersections: written predictions, not execution output

The following census is an additional conditional written derivation. Every proper subgroup lies in one of the stated S4 or order-21 Borels, so only the displayed proper orders are possible. The 8 order-7 subgroups are the unipotent groups attached to the 8 projective points; each has its order-21 Borel as normalizer. An order-3 subgroup is conjugate to the diagonal subgroup generated by diag(2,4). Its centralizer has order 3 and its normalizer, adding the Weyl involution, has order 6, yielding 28 such subgroups. Every order-6 subgroup normalizes its normal Sylow-3 subgroup and is that normalizer, so there are 28.

A projective involution has a trace-zero determinant-one lift. The 42 such lifts are obtained by writing `[[a,b],[c,−a]]` with `bc=−1−a²`; the right side is never zero in F7, giving 6 choices of b for each a. Quotienting ± gives 21 involutions. All are conjugate to the projective class of `J=[[0,−1],[1,0]]`: its characteristic polynomial is irreducible, and the determinant of a GL₂ conjugator can be adjusted using the surjective F49/F7 norm. Its projective centralizer has order 8: the determinant-one commuting and anticommuting matrices correspond to the norm equations `a²+b²=1` and `a²+b²=−1`, each with 8 solutions, divided by ±. It is D8, with the involution central, one cyclic subgroup of order 4, and two Klein four subgroups containing that involution. Hence there are 21 cyclic order-4 subgroups, `21·2/3=14` Klein fours, and 21 order-8 subgroups. For the last statement, every order-8 subgroup is a Sylow-2 subgroup and is conjugate to a D8 Sylow subgroup of S4; it is the centralizer of its central involution.

Each S4 has one A4, and its normalizer in G is that S4: a larger normalizer is G, which would give a nontrivial solvable quotient of order 14. Consequently the 14 S4's give 14 distinct order-12 subgroups, and every order-12 subgroup occurs this way. Together with the identity and whole group, the census is:

| subgroup order | subgroups | index | actual proper left cosets |
|---:|---:|---:|---:|
| 1 | 1 | 168 | 168 |
| 2 | 21 | 84 | 1764 |
| 3 | 28 | 56 | 1568 |
| 4 | 35 | 42 | 1470 |
| 6 | 28 | 28 | 784 |
| 7 | 8 | 24 | 192 |
| 8 | 21 | 21 | 441 |
| 12 | 14 | 14 | 196 |
| 21 | 8 | 8 | 64 |
| 24 | 14 | 7 | 98 |
| 168 | 1 | 1 | not proper |

The table totals **179 subgroups and 6745 actual proper left cosets**. In particular 256 actual cosets have index not divisible by 7: 64 of index 8 and 192 of index 24. Their indices are coprime to 7. Every actual index-7 coset meets each, with intersection size 3 for index 8 and 1 for index 24. Across all 98 index-7 cosets this predicts 6272 size-3 and 18816 size-1 intersections, 25088 in total.

For the high-index argument, actual subgroup labels give relative values `m∈{2,3,4,6,8,12,24}`; the only unordered coprime pairs among these values are `(2,3)`, `(3,4)`, `(3,8)`. Inside each index-7 stabilizer, the S4 subgroup counts for relative indices 2,3,4,8 are respectively 1,3,4,4. Hence there are 27 unordered proper-subgroup-label pairs of these coprime relative types, and `3·(2·3)+12·(3·4)+12·(3·8)=450` pairs of actual internal left cosets; all meet by the coprime-index lemma. Over 14 stabilizers these become 378 label pairs and 6300 actual internal coset pairs. This is exactly the derived-label check needed for the completion consumer, **not** an exhaustive assertion about arbitrary S4 coset families or all-group Sun8.

## 5. Proposed finite assay, inputs, controls and unpaid execution

The standalone source is `q7-actual-cosets-v1.py`, SHA-256 `539ba3dfc53839ab33d540a6b0a4400a0a0346c5bece6df08ed362ff1e2914bb`. Its complete literal body is appended below. Its only mathematical input is F7 and determinant one; canonical matrix representatives identify A with −A. It constructs the multiplication table, unit and inverses, separately checks U(1),V(1) generation, and generates the whole subgroup lattice by adjoining one representative per `gH`. The reduction is exact because `<H,gh>=<H,g>`; exploring every new H-coset under right multiplication by all h·g generates precisely `<H,g>`, and every subgroup is reachable by adjoining its elements. It materializes every proper actual left coset as a bitset of group-element ids, reconstructs the two subgroup-conjugacy actions and their actual 3+4 incidence, and checks every same/cross cell pair and every six-clique. It then checks every actual non-7-index coset against all 98 cells, plus all actual coprime relative coset pairs in every index-7 subgroup. Its bounded JSON would include the complete subgroup membership inventory, element-id/matrix map, orders, all counts, and actual members of a seven-coset positive packing; it does not print giant pair-by-pair logs.

The proposed named negative controls deliberately reject malformed matrices/projective-center separation, mixing left with right cosets, wrong incidence, a false or overlapping six-cell completion, a transposed source-stabilizer map, and mixing the two source classes. Separate logical guards distinguish repeated labels from disjoint cosets and refuse q≠7 as a model claim. The source checks a monotonic 52-second cooperative deadline; the parent must impose a 55-second outer deadline and use Python 3.10 or later with `-B -I` to suppress bytecode writes and isolate import paths. The program has no network, file-writing or child-process operation; its bounded result is written to stdout. An exception, deadline, missing output or lack of execution is **not** a pass.

**Observed checker execution and controls: NOT RUN / NOT TESTED.** No subgroup inventory, algorithmic census, six-clique result, internal-pair count or negative-control outcome has been obtained from the program. The counts above are independent written predictions, not fabricated machine results. Before any parent execution: full static read of the entire candidate and exact source, verify this binding, then a prospective named one-shot GO and the parent deadline; afterward the actual full output, exit status, stderr and elapsed time require separate review. No implicit GO is requested or granted by this candidate.

## 6. Exposure and chronological boundaries

Before body exposure I read the entire manifest, freeze receipt, parent-prepared metadata, actual dispatch receipt and all 20 status/permission controls through their endings, then sent Main a direct PREBODYACK. The manifest, freeze and packet hashes observed locally were respectively `5ea707f43050dbdafd2b70354ddbcdd474599928be9b40308decdc15ff436cb4`, `718f8bc890e14080a13c8f655cb37519f7670ee928072f0fa73f54abd9b3b54b`, and `9f2f95d93c426af4aac5d43aa161a090fb9417c8fecbddc4dfdfc42284733fb6`. After the ACK I read packet LF 1–265 entirely in strictly ordered raw windows of at most 20 LF, including the ending, before mathematical derivation or source design. Source and named controls above were created prospectively after the packet; q=7 itself was specified by the assignment. At the metadata observation `2026-10-30T15:53:20-0700 PDT` the source hash was the one stated above. No exact private derivation/completion timestamp or cognitive-isolation certificate is claimed.

No scientific executable, CAS, test, build, lint, formatter, external model, package installation or source-following was run. Only dates and file fingerprints were observed as metadata. No sibling code/proof, held scientific payload, stopped history or method/selection/confidence/consumer was read; the actual stopped episodes and all their consumers remain HELD/ZERO/NONINPUT. This author role is not a no-selected-case written reviewer and does not retroactively change any stopped gate.

**Paid in this body:** the complete conditional q=7 geometry, actual-coset disjointness and completion argument, its actual packing consumer, written census/intersection predictions, and the full unexecuted finite source. **Unpaid:** source-classification authentication, independent checking of every load-bearing written step and census, parent static review and GO, any actual execution and control results, independent-family/human/kernel review, novelty or priority, adoption of this extension, all-field classification, the original normal-extension 6+2 obstruction, and unrestricted Sun8. The established f≥2 disposition remains exactly at its prior conditional scope.

## 7. Literal standalone source (unrun)

The following is the complete source supplied for the proposed one-shot; the text is not itself an executed result.

```python
#!/usr/bin/env python3
"""Unrun prospective exact PSL(2,7) actual-subgroup/coset assay.

No input, network, child processes, or filesystem writes.  Parent must fully
read this source, separately authorize one run, and impose a 55-second outer
limit.  The internal monotonic deadline is 52 seconds.  A traceback, timeout,
or absent run is not a pass.  This checker addresses q=7 only.
"""
import itertools
import json
import math
import time
from collections import Counter

START = time.monotonic()
DEADLINE = START + 52.0


def guard():
    if time.monotonic() >= DEADLINE:
        raise TimeoutError("cooperative 52-second deadline reached; no verdict")


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def checked_matrix(a):
    if (not isinstance(a, tuple) or len(a) != 4 or
            any(type(x) is not int or not 0 <= x < 7 for x in a)):
        raise ValueError("matrix must be a 4-tuple of residues 0..6")
    if (a[0] * a[3] - a[1] * a[2]) % 7 != 1:
        raise ValueError("matrix determinant is not 1")
    return a


def canonical(a):
    a = checked_matrix(a)
    return min(a, tuple((-x) % 7 for x in a))


def matrix_product(a, b):
    return ((a[0]*b[0] + a[1]*b[2]) % 7,
            (a[0]*b[1] + a[1]*b[3]) % 7,
            (a[2]*b[0] + a[3]*b[2]) % 7,
            (a[2]*b[1] + a[3]*b[3]) % 7)


def rejects_matrix(a):
    try:
        canonical(a)
        return False
    except ValueError:
        return True


def indices(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


# Enumerate determinant-one matrices directly, then quotient by the actual
# center {I,-I}; integer ids refer to the sorted canonical representatives.
elements = sorted({canonical((a, b, c, d))
                   for a in range(7) for b in range(7)
                   for c in range(7) for d in range(7)
                   if (a*d - b*c) % 7 == 1})
need(len(elements) == 168, "projective group order")
N = len(elements)
BIT = [1 << i for i in range(N)]
FULL = (1 << N) - 1
id_of = {a: i for i, a in enumerate(elements)}
unit = id_of[canonical((1, 0, 0, 1))]
minus_unit = (6, 0, 0, 6)
need(canonical(minus_unit) == elements[unit], "projective center")
need(rejects_matrix((1, 0, 0, 2)) and rejects_matrix((1, 0, 0))
     and rejects_matrix((8, 0, 0, 1)), "malformed matrix refusal")
guard()

product = []
for a in elements:
    product.append([id_of[canonical(matrix_product(a, b))] for b in elements])
    guard()
inverse = [id_of[canonical((a[3], (-a[1]) % 7,
                              (-a[2]) % 7, a[0]))] for a in elements]
for a in range(N):
    need(len(set(product[a])) == N, "product row permutation")
    need(product[a][unit] == a and product[unit][a] == a, "unit")
    need(product[a][inverse[a]] == unit and
         product[inverse[a]][a] == unit, "inverse")

# This is an independent reachability check against the determinant enumeration.
upper = id_of[canonical((1, 1, 0, 1))]
lower = id_of[canonical((1, 0, 1, 1))]
generated = {unit}
frontier = [unit]
while frontier:
    x = frontier.pop()
    for s in (upper, lower):
        y = product[x][s]
        if y not in generated:
            generated.add(y)
            frontier.append(y)
    guard()
need(len(generated) == N, "unipotents do not generate the group")


def left_coset(g, subgroup_members):
    return sum(BIT[product[g][h]] for h in subgroup_members)


def right_coset(g, subgroup_members):
    return sum(BIT[product[h][g]] for h in subgroup_members)


def is_left_coset(coset, subgroup):
    if not coset:
        return False
    g = next(indices(coset))
    return coset == left_coset(g, list(indices(subgroup)))


def adjoin(subgroup, members, generator):
    # Explore right multiplication by h*generator from every left H-coset.
    # Each new point brings in its entire left H-coset.  Since all elements
    # have finite order, the resulting finite monoid is <H,g>.
    seen = subgroup
    representatives = [unit]
    pos = 0
    while pos < len(representatives):
        x = representatives[pos]
        pos += 1
        for h in members:
            y = product[product[x][h]][generator]
            if not (seen & BIT[y]):
                new_coset = left_coset(y, members)
                need(not (seen & new_coset), "adjoin coset overlap")
                seen |= new_coset
                representatives.append(y)
        guard()
    return seen


# For fixed H, one representative g of each left H-coset gH suffices:
# <H,gh>=<H,g> for every h in H.  Every subgroup is reachable by repeatedly
# adjoining elements of it, so the queue covers the complete subgroup lattice.
known = {BIT[unit]}
queue = [BIT[unit]]
position = 0
while position < len(queue):
    H = queue[position]
    position += 1
    members = list(indices(H))
    covered = 0
    for g in range(N):
        if covered & BIT[g]:
            continue
        block = left_coset(g, members)
        need(not (covered & block), "left cosets must partition")
        covered |= block
        if H & BIT[g]:
            continue
        K = adjoin(H, members, g)
        if K not in known:
            known.add(K)
            queue.append(K)
    need(covered == FULL, "subgroup coset enumeration incomplete")
    guard()

subgroups = sorted(known, key=lambda H: (H.bit_count(), H))
subgroup_id = {H: i for i, H in enumerate(subgroups)}
need(FULL in known, "entire group missing")
for H in subgroups:
    members = list(indices(H))
    need(H & BIT[unit] and N % len(members) == 0, "subgroup unit/order")
    for a in members:
        need(H & BIT[inverse[a]], "subgroup inverse closure")
        for b in members:
            need(H & BIT[product[a][b]], "subgroup product closure")
    guard()

proper = [H for H in subgroups if H != FULL]
maximal = [H for H in proper
           if not any(H != K and (H & K) == H for K in proper)]
maximal_indices = Counter(N // H.bit_count() for H in maximal)
need(maximal_indices == Counter({7: 14, 8: 8}), "maximal index/count")

# Materialize every proper actual left coset, not just subgroup labels.
# A coset determines its subgroup, since x^{-1}C is independent of x in C.
cosets_by_subgroup = {}
all_cosets = []
by_mask = {}
for H in proper:
    members = list(indices(H))
    covered = 0
    blocks = []
    for g in range(N):
        if covered & BIT[g]:
            continue
        C = left_coset(g, members)
        need(not (covered & C), "coset partition overlap")
        need(C not in by_mask, "distinct subgroup/coset sets duplicated")
        covered |= C
        blocks.append((g, C))
        record = (H, g, C)
        by_mask[C] = record
        all_cosets.append(record)
    need(covered == FULL and len(blocks) == N // len(members),
         "actual coset enumeration incomplete")
    cosets_by_subgroup[H] = blocks
    guard()


def conjugate(g, H):
    return sum(BIT[product[product[g][h]][inverse[g]]] for h in indices(H))


index7 = sorted(H for H in maximal if N // H.bit_count() == 7)
for H in maximal:
    normalizer = [g for g in range(N) if conjugate(g, H) == H]
    need(set(normalizer) == set(indices(H)), "maximal self-normalizer")
    guard()
remaining = set(index7)
classes = []
while remaining:
    H = min(remaining)
    orbit = {conjugate(g, H) for g in range(N)}
    need(orbit <= remaining and len(orbit) == 7, "index-7 conjugacy class")
    classes.append(sorted(orbit))
    remaining -= orbit
need(len(classes) == 2, "two index-7 classes")
classes.sort(key=lambda row: tuple(row))
points, lines = classes


def class_action(cls):
    lookup = {H: j for j, H in enumerate(cls)}
    action = []
    for g in range(N):
        image = [lookup[conjugate(g, H)] for H in cls]
        need(sorted(image) == list(range(7)), "class action permutation")
        action.append(image)
        guard()
    for a in range(N):
        for b in range(N):
            ab = product[a][b]
            for x in range(7):
                need(action[ab][x] == action[a][action[b][x]],
                     "conjugation action orientation")
        guard()
    for x, H in enumerate(cls):
        stabilizer = sum(BIT[g] for g in range(N) if action[g][x] == x)
        need(stabilizer == H, "actual point stabilizer")
    orbit = {(action[g][0], action[g][1]) for g in range(N)}
    need(len(orbit) == 42 and all(x != y for x, y in orbit),
         "degree-seven action not 2-transitive")
    return action


point_action = class_action(points)
line_action = class_action(lines)

# Incidence is reconstructed from actual K-orbits on the point class: the
# 3-orbit of each line stabilizer K is its line; no Fano table is imported.
incidence = [[False] * 7 for _ in range(7)]  # [point][line]
for a, K in enumerate(lines):
    unseen = set(range(7))
    orbits = []
    while unseen:
        x = min(unseen)
        orbit = {point_action[k][x] for k in indices(K)}
        need(orbit <= unseen, "point orbits overlap")
        unseen -= orbit
        orbits.append(orbit)
    need(sorted(map(len, orbits)) == [3, 4], "line 3+4 orbit")
    for x in next(o for o in orbits if len(o) == 3):
        incidence[x][a] = True
need(all(sum(incidence[x][a] for x in range(7)) == 3 for a in range(7)),
     "three points per line")
need(all(sum(incidence[x]) == 3 for x in range(7)), "three lines per point")
for x, y in itertools.combinations(range(7), 2):
    need(sum(incidence[x][a] and incidence[y][a] for a in range(7)) == 1,
         "point pair incidence")
for a, b in itertools.combinations(range(7), 2):
    need(sum(incidence[x][a] and incidence[x][b] for x in range(7)) == 1,
         "line pair incidence")
for expected in (False, True):
    all_flags = {(x, a) for x in range(7) for a in range(7)
                 if incidence[x][a] == expected}
    x, a = min(all_flags)
    flag_orbit = {(point_action[g][x], line_action[g][a]) for g in range(N)}
    need(flag_orbit == all_flags, "flag or antiflag action")
guard()

# Each cell is the full set of group elements mapping its source to target.
# Compare this actual bitset against the independently materialized cosets.
cells = []
cell_at = {}
for kind, cls, action in (("P", points, point_action),
                           ("L", lines, line_action)):
    for x, H in enumerate(cls):
        for y in range(7):
            C = sum(BIT[g] for g in range(N) if action[g][x] == y)
            need(C.bit_count() == 24 and C in by_mask and by_mask[C][0] == H,
                 "transporter is not its claimed actual left coset")
            cell_at[(kind, x, y)] = len(cells)
            cells.append((kind, x, y, H, C))
actual_index7 = {C for H, _, C in all_cosets if N // H.bit_count() == 7}
need(len(cells) == 98 and len(actual_index7) == 98 and
     {cell[4] for cell in cells} == actual_index7, "98 actual index-7 cosets")
cell_by_mask = {cell[4]: i for i, cell in enumerate(cells)}

same_hist = Counter()
cross_hist = Counter()
adjacency = [0] * len(cells)  # only larger-numbered neighbours
for i, first in enumerate(cells):
    kind, x, y, _, C = first
    for j in range(i + 1, len(cells)):
        kind2, a, b, _, D = cells[j]
        overlap = (C & D).bit_count()
        if kind == kind2:
            same_hist[overlap] += 1
            need((overlap == 0) == (x == a or y == b),
                 "same-class disjointness")
            need(overlap in (0, 4), "same-class intersection size")
        else:
            # All P cells were appended before all L cells.
            cross_hist[overlap] += 1
            left_flag = incidence[x][a]
            right_flag = incidence[y][b]
            need((overlap == 0) == (left_flag != right_flag),
                 "cross-class incidence criterion")
            if overlap:
                need(overlap == (8 if left_flag else 6),
                     "cross-class intersection size")
        if not overlap:
            adjacency[i] |= 1 << j
    guard()
need(same_hist == Counter({0: 588, 4: 1764}), "same-class pair counts")
need(cross_hist == Counter({0: 1176, 6: 784, 8: 441}),
     "cross-class pair counts")


def completion(six, proposed=None):
    if len(six) != 6 or len(set(six)) != 6:
        return None
    union = 0
    for i in six:
        if not 0 <= i < len(cells) or union & cells[i][4]:
            return None
        union |= cells[i][4]
    rest = FULL ^ union
    if proposed is not None and rest != proposed:
        return None
    return cell_by_mask.get(rest)


clique_counts = Counter()
partitions = set()
first_six = None
nodes = 0


def visit(chosen, candidates):
    global nodes, first_six
    nodes += 1
    if nodes % 1024 == 0:
        guard()
    if len(chosen) == 6:
        complement = completion(chosen)
        need(complement is not None, "six-clique has no actual coset complement")
        p = sum(cells[i][0] == "P" for i in chosen)
        clique_counts[f"{p},{6-p}"] += 1
        partitions.add(tuple(sorted((*chosen, complement))))
        if first_six is None:
            first_six = tuple(chosen)
        return
    needed = 6 - len(chosen)
    while candidates.bit_count() >= needed:
        low = candidates & -candidates
        i = low.bit_length() - 1
        candidates ^= low
        visit((*chosen, i), candidates & adjacency[i])


visit((), (1 << len(cells)) - 1)
need(clique_counts == Counter({"6,0": 98, "0,6": 98,
                               "4,2": 294, "2,4": 294, "3,3": 784}),
     "six-clique composition counts")
need(len(partitions) == 224, "seven-coset partition count")
guard()

# Check every actual proper coset whose index is not divisible by 7 against
# every actual index-7 coset; classify real intersection sizes by index.
other_cosets = [(H, g, C) for H, g, C in all_cosets
                if (N // H.bit_count()) % 7]
intersection_hist = Counter()
for cell in cells:
    C = cell[4]
    for H, _, D in other_cosets:
        index = N // H.bit_count()
        amount = (C & D).bit_count()
        need(amount > 0 and math.gcd(7, index) == 1,
             "non-7 index actual coset failed to intersect")
        need(amount == N // (7 * index), "coprime intersection cardinality")
        intersection_hist[f"{index}:{amount}"] += 1
    guard()

# Only the high relative indices derived from 7m | 168 are used here.
high = [(H, (N // H.bit_count()) // 7) for H in proper
        if (N // H.bit_count()) % 7 == 0 and N // H.bit_count() > 7]
high_values = sorted({m for _, m in high})
need(all(m > 1 and 24 % m == 0 for m in high_values), "relative divisors")
for a, b, c in itertools.combinations_with_replacement(high_values, 3):
    need(not (math.gcd(a, b) == math.gcd(a, c) == math.gcd(b, c) == 1),
         "three pairwise coprime high relative indices")
high_coprime = sorted({tuple(sorted((a, b))) for a in high_values
                       for b in high_values if math.gcd(a, b) == 1})
need(set(high_coprime) <= {(2, 3), (3, 4), (3, 8)},
     "unexpected relative coprime indices")

# Independently inspect actual relative cosets inside every order-24 index-7
# subgroup.  No isomorphism label or all-group Sun8 claim is used.
internal = []
for K in points + lines:
    local = [H for H in proper if H != K and (H & K) == H]
    local_cosets = {}
    for H in local:
        local_cosets[H] = [C for _, C in cosets_by_subgroup[H] if (C & K) == C]
        need(len(local_cosets[H]) == K.bit_count() // H.bit_count(),
             "internal actual left cosets")
    labels = 0
    pairs = 0
    pair_types = Counter()
    for A, B in itertools.combinations_with_replacement(local, 2):
        m, n = K.bit_count() // A.bit_count(), K.bit_count() // B.bit_count()
        if math.gcd(m, n) != 1:
            continue
        need(tuple(sorted((m, n))) in {(2, 3), (3, 4), (3, 8)},
             "internal relative index outside derived pairs")
        labels += 1
        pair_types[str(tuple(sorted((m, n))))] += 1
        for C in local_cosets[A]:
            for D in local_cosets[B]:
                need(C & D, "disjoint coprime-index internal cosets")
                pairs += 1
    internal.append({"ambient_subgroup_id": subgroup_id[K],
                     "proper_internal_subgroups": len(local),
                     "coprime_label_pairs": labels,
                     "actual_coset_pairs": pairs,
                     "relative_index_pair_counts": dict(pair_types)})
    guard()

# Named negative controls use deliberately malformed inputs/consumers.  They
# are assertions about refusal, not additional scientific executions.
H = points[0]
Hm = list(indices(H))
g = next(g for g in range(N) if left_coset(g, Hm) != right_coset(g, Hm))
need(not is_left_coset(right_coset(g, Hm), H), "left/right mix accepted")
need(is_left_coset(left_coset(g, Hm), H), "valid left coset rejected")

bad_incidence = [row[:] for row in incidence]
bad_incidence[0][0] = not bad_incidence[0][0]
wrong_incidence_mismatches = 0
for x, y, a, b in itertools.product(range(7), repeat=4):
    C = cells[cell_at[("P", x, y)]][4]
    D = cells[cell_at[("L", a, b)]][4]
    wrong = bad_incidence[x][a] != bad_incidence[y][b]
    wrong_incidence_mismatches += (wrong != (not (C & D)))
need(wrong_incidence_mismatches > 0, "wrong incidence not rejected")

valid_six = [cell_at[("P", 0, y)] for y in range(6)]
wrong_completion = cells[cell_at[("P", 1, 6)]][4]
need(completion(valid_six) is not None and
     completion(valid_six, wrong_completion) is None,
     "false complement accepted")
nonclique = [cell_at[("P", 0, y)] for y in range(5)] + [cell_at[("P", 1, 1)]]
need(completion(nonclique) is None, "overlapping six falsely completed")

for kind, x, y, _, C in cells:
    inverted = sum(BIT[inverse[z]] for z in indices(C))
    need(inverted == cells[cell_at[(kind, y, x)]][4], "inverse transporter")
transposed = cells[cell_at[("P", 1, 0)]][4]
need(not is_left_coset(transposed, points[0]), "transposed source accepted")
need(not is_left_coset(points[0], lines[0]), "source class mix accepted")

packing = [cells[cell_at[("P", 0, y)]][4] for y in range(7)]
union = 0
for C in packing:
    need(not (union & C), "positive packing is not disjoint")
    union |= C
need(union == FULL and len(packing) == 7, "seven-coset packing")
need(math.gcd(7, 7) == 7 and len(cosets_by_subgroup[points[0]]) == 7,
     "label repetition versus seven actual cosets")
need(len({packing[0] for _ in range(8)}) == 1,
     "repeated labels incorrectly treated as eight disjoint cosets")


def model_for_q(q):
    if q != 7:
        raise ValueError("this finite model covers q=7 only")
    return N


try:
    model_for_q(8)
    raise AssertionError("out-of-scope field accepted")
except ValueError:
    pass
need(model_for_q(7) == N, "q=7 scope guard")
guard()

counts_by_order = Counter(H.bit_count() for H in subgroups)
cosets_by_index = Counter(N // H.bit_count() for H, _, _ in all_cosets)
maximal_set = set(maximal)
result = {
    "status": "PASS_BOUNDED_Q7_ASSAY_ONLY",
    "elapsed_before_encoding_seconds": round(time.monotonic() - START, 6),
    "scope": {"field": 7, "objects": "actual left cosets of actual subgroups",
              "all_fields": False, "all_group_sun8": False,
              "classification_source_authenticated": False},
    "group": {"order": N, "identity_id": unit,
              "upper_generator_id": upper, "lower_generator_id": lower,
              "canonical_matrix_representatives_by_id": elements},
    "subgroup_enumeration": {
        "method": "complete adjoin-closure, one representative per gH",
        "total": len(subgroups), "counts_by_order": dict(counts_by_order),
        "proper_cosets_total": len(all_cosets),
        "proper_cosets_by_index": dict(cosets_by_index),
        "maximal_counts_by_index": dict(maximal_indices),
        "inventory": [{"id": subgroup_id[H], "order": H.bit_count(),
                       "members": list(indices(H)), "maximal": H in maximal_set}
                      for H in subgroups]},
    "geometry": {
        "point_stabilizer_ids": [subgroup_id[H] for H in points],
        "line_stabilizer_ids": [subgroup_id[H] for H in lines],
        "lines_as_point_numbers": [[x for x in range(7) if incidence[x][a]]
                                    for a in range(7)],
        "actual_index7_cosets": len(cells),
        "same_class_intersections": dict(same_hist),
        "cross_class_intersections": dict(cross_hist),
        "six_cliques_by_point_line_count": dict(clique_counts),
        "seven_coset_partitions": len(partitions),
        "first_six_cells": [list(cells[i][:3]) for i in first_six],
        "first_six_complement": list(cells[completion(first_six)][:3])},
    "nondivisible_by_7": {"cosets": len(other_cosets),
                          "index_and_intersection_size_counts": dict(intersection_hist)},
    "high_relative_indices": {"values": high_values,
                              "coprime_pairs": high_coprime,
                              "subgroup_label_count": len(high)},
    "internal_actual_coprime_checks": internal,
    "positive_seven_packing": {"subgroup_id": subgroup_id[points[0]],
                               "coset_members": [list(indices(C)) for C in packing]},
    "named_controls": {"malformed_matrix": "REJECTED",
                       "unquotiented_projective_center": "REJECTED",
                       "left_right_mix": "REJECTED",
                       "wrong_incidence": "REJECTED",
                       "false_completion_and_nonclique": "REJECTED",
                       "transposed_source_map": "REJECTED",
                       "source_class_mix": "REJECTED",
                       "logical_scope_label_vs_coset_and_other_q": "GUARDED"},
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":"))
need(len(payload.encode("utf-8")) <= 200000, "bounded output size")
guard()
print(payload)

```
