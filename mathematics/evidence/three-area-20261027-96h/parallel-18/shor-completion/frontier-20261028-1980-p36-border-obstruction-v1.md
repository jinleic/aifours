# Shor completion: exclusion of the 36-head border branch at order 1980

Owner **MathShor-2**, math-5. Actual clock of independent finite replay: **Wed Oct 28 19:40:28 PDT 2026**.
**Conditional written reduction plus two independently implemented exact finite checks; this does NOT exclude n=1980 or solve the original all-order problem. No formal, peer, cross-family or novelty acceptance is claimed.**

## 1. Statement and prime-power forcing

Let D be a hypothetical finite UD factor-complete extension of the literal Shor code with actual pure-a atom `a^1980`. The actual border sets P,Q, including multi-b words, form a direct cyclic tiling with old anchors

    A={0,3,8,11} subset P,     Y={0,1,7,13,14} subset Q.

This is the same classical border theorem independently reconstructed in the previous packets. The classical Sands gcd-class disjointness condition also applies.

**Claim:** the specific cardinality branch `|P|=36, |Q|=55` is impossible. No other order-1980 border branch is excluded by this packet.

Because `1980=2^2*3^2*5*11` and |Q|=55 is coprime to3, both `Phi_3` and `Phi_9` must divide the P-mask. Their product `1+X+...+X^8` forces P to be uniform modulo9, exactly4 in each class. Consequently P has exactly12 elements congruent1 modulo3.

## 2. A unique saturated set of twelve heads

Old anchor differences give `G_A={3,4,5,11}` and `G_Y={1,2,6,12}` as gcd classes at order1980. The old-anchor head candidate screen contains exactly18 residues congruent1 modulo3. Directness/Sands requires any two selected heads to have gcd-difference outside G_Y.

Exact enumeration of all `C(18,12)=18,564` 12-subsets finds exactly ONE compatible set:

    {88,253,418,583,748,913,1078,1243,1408,1573,1738,1903}.

The independent replay enumerates the complementary six-subsets instead. In particular P contains `88,253,418,583,748,1078`; their differences from88 force the five gcd classes

    H={165,330,495,660,990}.

Thus Q must avoid H as well as G_A.

## 3. Four tail quotas contradict those gcd exclusions

Since |Q|=55 and |P|=36 is coprime to5 and11, Q is uniform modulo5 and11. Therefore it has exactly11 elements in each mod5 class and5 in each mod11 class.

Retain only screened Q-candidates in mod5 classes0,4 OR mod11 classes0,3, while enforcing compatibility with all five old Q-anchors and forbidding gcd differences in `G_A union H`. There are170 such core candidates. A putative Q must select old anchors0,14 and satisfy the four exact quotas `(11,11,5,5)` in these classes. Dropping every other Q element and constraint is a relaxation; if the relaxed instance is impossible then the actual border tiling is impossible.

The bitset include/exclude search checks this instance in393 nodes, with166 quota prunes, and finds no solution. An independently written set-based search with a different branch ordering checks541 nodes, with271 quota prunes, and also finds no solution. Each search performs only exhaustive branching plus exact quota and gcd rejection.

A literal 22-residue control satisfies the four quotas and the old-anchor compatibility after **only gcd660 is removed** from the exclusion set; it contains gcd660 collisions. The first checker verifies this control directly. It demonstrates that the relaxed contradiction is not vacuous.

## 4. Pins and original gap

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-1980-p36-quota-check.py` | 1ebc077254161d228d624ffc60bcf4d32f8ec10deb4c4ce6df4076d15c6b0083 | 54 / 2887 |
| `frontier-20261028-1980-p36-quota-replay.py` | d558e970fcd85cf33512619f8b47ff5a340b1b42ef92385f1cf78791b941dd5a | 43 / 2063 |

The candidate `n>=1980` floor from the separate order660/1320 candidates is not required here and remains unreviewed. The n1980 branches `|P|=12` and15 yielded bounded Z3 UNKNOWN at25 seconds; these timeouts are not exclusions. The many other cardinalities remain open, and no finite completion is constructed.

**END OF ORDER-1980 P36 BORDER OBSTRUCTION.**
