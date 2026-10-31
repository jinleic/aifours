# Small Ree simple groups: Sun8 from a full-Sylow3 subgroup barrier

**NEW FAMILY CANDIDATE at NAMED IMPORTS — WRITTEN plus bounded exact subgroup-order arithmetic; not yet reviewed/adopted/novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:47:01 PDT 2026**. This is a direct original-coset statement for an infinite finite-simple family, not a conditional order bound or an alleged complete solution of arbitrary-group Sun8.

## 1. Exact theorem and imports

For a group X, `Sun_k(X)` means every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups have a pair of original indices with gcd>=k.

**Theorem.** For EVERY integer m>=1, put `q=3^(2m+1)` and let `G=^2G_2(q)` be the simple SMALL Ree group. If `Sun_7(G)` and the named Ree order/maximal-subgroup classification statements below hold, then `Sun_8(G)`.

The earlier 2026-10-20 parent verdict `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md`, SHA256 `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`, supports the arbitrary-group Sun7 STATEMENT at its full written-composition dependency boundary. I have not independently replayed/reproved that full DAG, so **NR-SUN7-INDEPENDENT-PROOF** remains. The mathematical theorem here is fully explicit with only the LOCAL hypothesis `Sun_7(G)`.

The named Ree structure import consists of the exact order and maximal-subgroup list in [E. Pierro, *The Möbius function of the small Ree groups*, arXiv:1410.8702v2](https://arxiv.org/html/1410.8702v2), §2.1–2.2, plus the explicit group order independently stated in [Alavi–Daneshkhah–Mosaed, *On quantitative structure of small Ree groups*, arXiv:1606.00049v1](https://arxiv.org/html/1606.00049), §2. Their maximal classification is attributed to Levchuk–Nuzhin and Kleidman. I read the source statements and reconstruct EVERY order/index comparison below, but did NOT read/reprove the original classification proofs: **NR-REE-CLASSIFICATION-PROOF / NR-REE-PRIMARY-ANCESTRY** remain. The list is an explicit classical group-structure IMPORT, not a claimed consequence of the local arithmetic checker.

Scope is q>=27, exactly m>=1. The exceptional group `^2G_2(3)` is not simple and is NOT included here. No Sun8 result for the large Ree groups `^2F_4(q)` is claimed. No held historical candidate is adopted or retrospectively validated.

## 2. General p-free-index criterion

**Lemma.** Let p∈{2,3,5}. Let G be finite and satisfy `Sun_7(G)`. Suppose there is an integer D>=8 such that EVERY proper subgroup of G whose index is not divisible by p has index divisible by D. Then `Sun_8(G)`.

**Proof.** Suppose eight actual disjoint left cosets have original subgroup indices with every pair gcd<=7. If seven of these indices were divisible by p, the Sun7 property applied to those SAME seven cosets would give an index gcd>=7. But a positive multiple of p that is <=7 can only be:

- p=2: 2,4,6;
- p=3: 3,6;
- p=5: 5.

Each is <7, contradiction. Thus at most six indices are divisible by p, and at least TWO are prime to p. Their subgroups are proper because an index-one coset is all G and cannot be disjoint from any other nonempty coset. The hypothesis makes D divide both original indices, so their gcd is at least D>=8, contrary to the counterconfiguration. □

This uses only one seven-coset subfamily and works at any p of the displayed set; p=7 is deliberately excluded because gcd7 would not contradict Sun7. It does not require all eight original indices to be divisible by7 or an assumed P7/simple-group reduction.

## 3. Actual 3-parts of EVERY maximal-subgroup type

Fix q=3^(2m+1), m>=1. The source group-order statement is

    |G|=q³(q³+1)(q−1),       |G|_3=q³.

The latter follows because q³+1≡1 and q−1≡−1 modulo3. Let H be ANY proper subgroup with 3-free index `[G:H]`. Then |H| has full 3-part q³, so a Sylow3 subgroup of H is a Sylow3 subgroup of G. H is contained in some maximal proper subgroup M. Its 3-part must be at least q³ and in fact equals q³. We examine ALL listed maximal types:

1. **Parabolic** `P=q^(1+1+1):(q−1)` has order `q³(q−1)` and 3-part q³.
2. **Involution centralizer** `2×PSL2(q)` has order `q(q²−1)` for odd q, using `|PSL2(q)|=q(q²−1)/2`; its 3-part is only q.
3. **Four-group normalizer** `(2²×D_{(q+1)/2}):3` has order `6(q+1)` under the source's dihedral-order convention; its 3-part is3 because q+1≡1 mod3.
4. **Two Hall normalizers** have orders `6(q−sqrt(3q)+1)` and `6(q+sqrt(3q)+1)`. Here `sqrt(3q)=3^(m+1)`, so each bracket is1 mod3 and each 3-part is3.
5. **Proper subfield subgroup** `^2G_2(q0)` has q=q0^t with t>1 and q0 an odd power of3. Its 3-part is q0³<q³ from the same order formula. The q0=3 exceptional subfield, when present, has order1512 and 3-part27=q0³; it is not falsely treated as a simple group.

Since q>=27, q³ is strictly larger than q and3, and q0³<q³. Therefore the ONLY listed maximal type capable of containing a FULL Sylow3 subgroup is the parabolic P. Thus every actual H as above lies in some conjugate of P, and

    [G:H]=[G:P][P:H],       [G:P]=q³+1.

Hence D=q³+1 divides every proper 3-free original subgroup index, and D>=8. Applying Section2 with p=3 proves Sun8(G). □

No statement that different H contain the SAME Sylow3 subgroup, share a conjugate parabolic, or form a covering is needed; the common divisor is the index of the respective conjugate parabolic.

## 4. Source-order discrepancy and why it is not hidden

The displayed order in §2.2 of [Busch–Pengitore–Schillewaert–Van Maldeghem, arXiv:2510.06479v1](https://arxiv.org/html/2510.06479v1) was returned by the web reader as `q³(q+1)(q−1)`. The SAME document describes a natural action of degree `q³+1` and a Sylow3 normalizer of order `q³(q−1)`, so orbit-stabilizer yields `q³(q³+1)(q−1)`, not the shorter displayed formula. The exact 2016 source's order formula agrees with that action and with Pierro's 2014 §2. We do NOT use the shorter expression, silently reconcile it as a proof, or assert the PDF/author's intended text was separately checked. The actual needed complete maximal-subgroup theorem is taken from the explicitly named 2014 source, not inferred from the 2025 introduction.

## 5. Bounded exact arithmetic check

Executed `/opt/homebrew/bin/python3 frontier-20261028-ree-maximal-3part-check.py` with a10-second deadline. Source SHA256 `355bd7e338d2432d7954d827d9562fa5883dfc7c0a45eadf96bec4d6cd00312a`; it uses exact integers only. For m=1,...,6 it checks the exact group order, parabolic index, divisibility and 3-parts of every listed other maximal ORDER and each proper subfield order. Actual output:

```text
m=1, q=27, v3_group=9, v3_B=9, max_v3_other=3, index_B=19684
m=2, q=243, v3_group=15, v3_B=15, max_v3_other=5, index_B=14348908
m=3, q=2187, v3_group=21, v3_B=21, max_v3_other=7, index_B=10460353204
m=4, q=19683, v3_group=27, v3_B=27, max_v3_other=9, index_B=7625597484988
m=5, q=177147, v3_group=33, v3_B=33, max_v3_other=11, index_B=5559060566555524
m=6, q=1594323, v3_group=39, v3_B=39, max_v3_other=13, index_B=4052555153018976268
PASS: six q cases match stated 3-part and index comparisons
Wed Oct 28 17:46:46 PDT 2026
```

The source also checks the algebraic identity `q³+1=(q+1)(q²−q+1)` underlying the discrepancy in Section4 for these values. This finite sample is NOT an actual-group construction, subgroup enumeration, Sun7 proof or verification that the imported maximal list is complete; the all-m arithmetic in Section3 is the written proof of the needed valuations.

## 6. Prior scope and residual

The previous round final math-6 summary expressly lists full SL/PSL and symplectic families as written-supported; its later Ree leads were not generally adopted and retain their own exact historical statuses. Thus this is a prospective full small-Ree-family proof CANDIDATE at the explicitly named classification and Sun7 statements, NOT an assertion that older held Ree material has been validated, reused as proof, or superseded. A publication/priority search is not complete; no novelty claim is made.

This excludes only the SMALL Ree simple family if the named inputs and this proof pass review. Arbitrary finite nonabelian simple groups, large Ree, remaining exceptional types, unrestricted Sun8, original proofs of the imports, human/kernel/independent-family review and publication/priority are not settled. Parent must review the complete proof and exact source statements before adoption.
