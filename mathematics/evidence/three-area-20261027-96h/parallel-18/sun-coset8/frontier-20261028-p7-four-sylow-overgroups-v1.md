# Direct P7 forces four Sylow maximal overgroups

**Status: WRITTEN, UNREVIEWED.** Let G be finite with no proper subgroup of index below 8. If G admits eight pairwise disjoint left cosets whose subgroup indices have all pairwise gcd exactly 7 (the prior direct P7 condition), then for every prime p>7 dividing |G|, **every Sylow p-subgroup is contained in at least four distinct maximal proper subgroups**. If in addition p divides none of the eight indices, the lower bound is five. Consequently, if some Sylow p-subgroup for p>7 has at most three actual maximal proper overgroups, direct P7 is impossible.

For a finite nonabelian simple group, the minimum-index condition is automatic when p>7: every proper coset action is faithful, so each proper index is at least p. These are actual subgroup and Sylow assertions, not a count of maximal-subgroup conjugacy classes and not an integer-only relaxation. This result does not assert unrestricted Sun8 without an additional Sun7/R8 import, classify all simple groups, claim novelty, or represent review/adoption/formal verification.

## 1. Exact relation to previous work

This is a stronger prospective source-free direct-P7 successor to `frontier-20261028-common-sylow-triple-p7-sun8-v1.md` SHA `4ce24ffd341338433de4d7ae57a706893f50dfea5c9d13c1eb917a0d846dcf9d`, which obtained three overgroups for p>42. The **separate** unrestricted Sun8 criterion at p>42 and at most two overgroups in `frontier-20261028-common-sylow-two-overgroups-sun8-v1.md` SHA `5ca3941781212d47f8408c4a30b01ab622d994c0227b19991f3ffdaaab15b472` is not replaced or strengthened here. Earlier unique-overgroup arguments and the prior R8/P7 definition remain credited; no priority is claimed.

Read in order the complete earlier overlays `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. Direct P7 here is the eight-disjoint-coset definition in §3 of `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md` SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`. No Sun7/R8 implication, CFSG, source classification, historical-hold change or clean-cognition claim is imported.

## 2. A common Sylow for all 30-free, p-free vertices

Write the eight indices as m_i=7a_i, where the a_i are positive and pairwise coprime. Units may repeat; no distinctness assumption is used. Fix any prime p>7 dividing |G|. At most one a_i is divisible by p, and for each of 2,3,5 at most one a_i is divisible by that prime. Therefore at least four indices i satisfy both p∤a_i and gcd(a_i,30)=1; if p divides no index there are at least five. Let J be **all** such vertices.

We prove that p does not divide [G:⋂_{i∈J}H_i]. Order J arbitrarily. For the first t vertices let A_t be the product of their a_i and let I_t be the index of the intersection of their subgroups. Inductively,

\[I_t=7A_t c_t,\qquad c_t\text{ has no prime divisor outside }\{2,3,5\}.\tag{1}\]

For t=1, c_1=1. Assume (1) and let H be the next subgroup with index 7a. Pairwise coprimality and gcd(a,30)=1 give gcd(A_t c_t,a)=1, so

\[\gcd(I_t,7a)=7,\qquad \operatorname{lcm}(I_t,7a)=7A_t a c_t.\]

The next coset is disjoint from an earlier coset. Thus the corresponding subgroup product H_iH is not all of G for that earlier i. Since ⋂_{j≤t}H_j⊆H_i, also (⋂_{j≤t}H_j)H≠G. The product-set size formula therefore gives I_(t+1)<I_t·7a. As I_(t+1) is a multiple of both I_t and 7a, it equals their lcm times an integer c' with 1≤c'<7. Thus

\[I_{t+1}=7A_t a\,(c_t c'),\qquad c'\in\{1,2,3,4,5,6\},\]

and the induction continues. Every c' is 5-smooth, every selected a_i is p-free, and p>7; hence p∤I_|J|. By Sylow's theorem the intersection contains one full Sylow p-subgroup of G shared by **all** vertices in J. This does not claim a common Sylow for vertices outside J or a simultaneous common choice for different primes.

## 3. Distinct maximal overgroups

All eight subgroup vertices are proper. Any pair H_i,H_j generates G: their generated subgroup has index dividing gcd(m_i,m_j)=7, and no proper subgroup has index 1 through 7. For the common Sylow P in §2, choose one maximal proper subgroup M_i containing each H_i with i∈J. Every M_i contains P, and the M_i are pairwise distinct because any two H_i generate G. Hence |M(P)|≥|J|≥4, or ≥5 when p divides no index. All Sylow p-subgroups are conjugate, so the conclusion holds for every Sylow p-subgroup. The case P=G cannot occur in the assumed configuration because the selected proper subgroups contain P.

This proves the theorem and the direct-P7 exclusion when the actual maximal-overgroup count is at most three. Counting only at most three **conjugacy classes** does not suffice. A hypothetical global Sun8 counterexample need not have all gcds equal 7 unless an independently named Sun7/R8 implication is assumed; this packet does not silently make that assumption.

## 4. Review boundary

A disjoint reviewer should reconstruct the selection count allowing repeated unit cofactors and one higher-7 cofactor, the iterative lcm/index coefficient and strict product-set step, the 5-smooth induction, and actual pair-generation/maximal-overgroup count. There is no formal proof, source-family classification, human/cross-model review, novelty or historic-hold rehabilitation in this report.
