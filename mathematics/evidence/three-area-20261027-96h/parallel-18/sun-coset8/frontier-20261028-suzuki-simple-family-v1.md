# Suzuki simple groups: Sun8 via odd-index structure and Sun5

**NEW FAMILY CANDIDATE at NAMED IMPORTS — WRITTEN plus a bounded exact Sz(8) matrix experiment; not yet peer-reviewed/adopted/novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:44:36 PDT 2026**. The proof applies to actual left cosets of EVERY actual subgroup, not only a normalizer list, a private-index pattern, or a fixed numerical group.

## 1. Exact theorem and named dependencies

For any group X, let `Sun_k(X)` mean: every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups have a pair of subgroup indices with gcd at least k.

**Theorem.** For EVERY integer m>=1, let `q=2^(2m+1)` and G be the finite simple Suzuki group `Sz(q) = ^2B_2(q)`. If `Sun_5(G)` and the Suzuki order/maximal-subgroup statements below hold, then `Sun_6(G)`, `Sun_7(G)` and `Sun_8(G)` hold. In particular, at the previously internally accepted arbitrary-group Sun5 STATEMENT and the named Suzuki subgroup-classification import, no simple Suzuki group supports a direct P7/Sun8 counterconfiguration.

The two non-elementary inputs are explicitly separate:

1. **Sun5 statement only:** every five disjoint finite-index left cosets in an arbitrary group have a pair of indices with gcd>=5. The actual 2026-10-19 written-composition parent verdict `institute/runs/six-lane-2026-10-18-96h/review/sun56-S56W-parent-verdict-v1.md`, SHA256 `63baa72b107e0f809c26a5057f10b6fd31f8ae2f09cffb527873bec11a8107ee`, states this at its named Sun3/Sun4 and written-core dependencies. I read the literal verdict, not its entire transitive proof DAG. **NR-SUN5-INDEPENDENT-PROOF:** no new proof, human/kernel acceptance or priority inference.
2. **Suzuki order and maximal-subgroup classification:** the published article Héthelyi–Horváth–Petényi, [*The depth of subgroups of Suzuki groups*, arXiv:1404.1523v1](https://arxiv.org/html/1404.1523v1), §2 and Theorems3.1/4.1, states `|Sz(q)|=q²(q²+1)(q−1)` and gives every maximal subgroup, up to conjugacy, as the Sylow2 normalizer B of order `q²(q−1)`; a dihedral group of order `2(q−1)`; either torus normalizer of order `4(q±2^(m+1)+1)`; or a proper subfield Suzuki group `Sz(s)` where `q=s^t`, t>1, s>=8. Its §3 explicitly attributes subgroup facts to earlier Suzuki/Huppert–Blackburn sources. I read the source's displayed order, Theorem3.1 orders and Theorem4.1 maximality list, and independently checked their application below; **NR-SUZUKI-CLASSIFICATION-PROOF:** the original classification proof, original Suzuki1962 publication and its full transitive source ancestry were NOT read or rederived. The 2014 paper is a source for the stated import, not a claim that this new coset theorem appears there.

The case m=0, `Sz(2)` of order20, is not a finite nonabelian simple Suzuki group and is NOT included in this stated family. No CFSG-wide classification, Sun7, prior P7/simple descent, NC7 or finite-group database is imported by the proof below. No historical held result is treated as proof or retrospectively validated.

## 2. General parity-to-odd-index lemma

**Lemma.** Let G be any finite group with 3 not dividing |G|, satisfying `Sun_5(G)`. Suppose there is an integer D>=8 such that EVERY proper subgroup of ODD index in G has index divisible by D. Then `Sun_k(G)` holds for k=6,7,8.

**Proof.** Fix k in {6,7,8} and suppose k actual disjoint left cosets have subgroup indices n_i with every pair gcd<k, hence at most7. Each subgroup is proper: an index-one coset is all G and cannot be disjoint from any other nonempty coset.

If there were five even indices, their five actual disjoint cosets would invoke `Sun_5(G)`. But 3 does not divide |G| and every index divides |G| by Lagrange, so the gcd of ANY two even indices is even, at most7 and not divisible by3. Its only possibilities are2 or4, both <5. This contradicts Sun5. Thus at most four of the k indices are even.

Since k>=6, at least TWO indices are odd. Both correspond to actual proper odd-index subgroups, so the stated index property makes D divide both. Their gcd is at least D>=8>=k, contradicting the counterconfiguration. This pays all k=6,7,8 and equality D=8, without assuming any seven-divisible index, P7, projection, subgroup normality, cover or solvability. □

The classification task is now solely to establish the actual odd-index divisor D for Sz(q); the lemma does NOT assume a Sylow normalizer contains all subgroups without proof.

## 3. Every proper odd-index subgroup of Sz(q) has index divisible by q²+1

Fix m>=1, so q>=8, and put `theta=2^(m+1)`. From the named Suzuki order input,

    |G|=q²(q²+1)(q−1),        |G|_2=q².

Let H<G be ANY proper subgroup of ODD index. Then |H| has the SAME full 2-part q². A Sylow2 subgroup of H therefore has order q² and is a Sylow2 subgroup of G. Since G is finite, H is contained in at least one maximal proper subgroup M. We compare the 2-parts of EVERY type in the named exhaustive classification:

- B=N_G(P) has order `q²(q−1)` and 2-part q².
- The dihedral maximal subgroup has order `2(q−1)` and 2-part2 because q−1 is odd.
- Each of the two torus normalizers has order `4(q±theta+1)` and 2-part4 because q and theta are even.
- A proper subfield subgroup Sz(s), where s>=8 and q=s^t with t>1, has order `s²(s²+1)(s−1)` and 2-part s²<q².

Since q²>=64>4, no maximal subgroup except a Sylow2 normalizer has enough 2-part to contain H's Sylow2 subgroup. Hence M is conjugate to B. For every such M,

    [G:M] = q²+1,
    [G:H] = [G:M][M:H],

so q²+1 divides the actual subgroup index [G:H]. This is valid for EVERY actual proper odd-index H; the containing maximal subgroup can depend on H. It neither assumes that the odd-index subgroups or their Sylow2 subgroups are identical nor that their cosets meet a common fiber.

For the general parity lemma, D=q²+1>=65. Also 3 does not divide |G|: `2^(2m+1)≡−1 (mod 3)`, so q²≡1, q−1≡1 and q²+1≡2 modulo3. The named order formula and elementary modular arithmetic therefore give `3∤|G|` for EVERY m>=1.

Applying Section2 yields `Sun_6(G)`, `Sun_7(G)` and `Sun_8(G)` at the named Sun5 and Suzuki-structure inputs. □

## 4. Exact bounded independent Sz(8) model check

To check the q=8 group/order/normalizer INTERFACE, not to replace the all-q classification, I wrote and ran the standard-library exact matrix program `frontier-20261028-suzuki8-matrix-check.py`, SHA256 `2d58134ab45dcf2e27c9d76c3c9252dbf71465b0df81fee0e4c570040f0d2398`,126LF/4133B. It uses GF(8)=F2[x]/(x³+x+1), direct 4x4 matrix products, the source's matrices S(a,b), C(lambda), T, and integer/set operations only. Four source generators are closed by BFS with a35,000-element cap; the root set is independently checked for closure; conjugation by generated group generators builds the entire orbit of that root subgroup and computes its actual normalizer size by orbit-stabilizer. Actual output from the bounded30-second run:

```text
GF8_polynomial: x^3+x+1
root_subgroup_size: 64
generated_B_size: 448
generated_G_size: 29120
root_conjugacy_orbit_size: 65
normalizer_size_from_orbit: 448
PASS: exact Sz(8) model, Sylow root and normalizer cardinalities
```

The source-code hash and native clock were observed immediately afterward at **Wed Oct 28 17:43:44 PDT 2026**. These match q²=64, q²(q−1)=448 and q²+1=65 for this one model. Given the cited source's group definition and order, the generated subgroup of size29120 equals that model. The experiment does NOT enumerate all Sz(8) subgroups, establish the all-q maximal classification, verify Sun5, or give a finite eight-coset search/witness. Its one implementation is not a formal/human/cross-family check.

## 5. Progress, previous scope and remaining obligations

The earlier 2026-10-23 round's final math-6 summary explicitly supports all-field SL/PSL and symplectic families at their named gates, while later unitary/orthogonal/Ree/Cayley leads were not generally adopted there. A targeted search of the prior math-6 parent dispositions did not identify a separate Suzuki `^2B_2(q)` family gate; this is a preliminary ancestry observation, NOT an exhaustive literature, source-history or novelty search. The candidate supplies a complete algebraic coset implication for an infinite nonsolvable finite-simple family, at an explicit externally sourced subgroup-classification statement and internal Sun5, rather than merely one finite simple order or an index tuple.

The original arbitrary-group Sun8 remains OPEN. Even if this family proof is accepted, it excludes only finite simple Suzuki groups, not all finite simple groups, arbitrary groups, Ree groups, all exceptional types, or the remaining direct-P7 simple factors. The full Sun5 composition and original Suzuki classification source/proofs remain named imports; neither has been independently proof-audited here. Parent and a disjoint reviewer must read the exact source statement and the complete candidate before any adoption. No novelty, priority, human/kernel/independent-family or publication acceptance is asserted.
