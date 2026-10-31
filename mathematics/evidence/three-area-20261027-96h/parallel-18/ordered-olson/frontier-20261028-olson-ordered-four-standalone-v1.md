# Standalone ordered-four field-sequence candidate

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 19:54:16 PDT 2026**. This is a NEW standalone written statement for a NEW disjoint scientific review. It makes NO actual-reflection-block, odd-run, raw-graph, floor, L_RES or Olson application.

The same mathematical statement appeared in the earlier source `frontier-20261028-olson-ordered-four-odd-boundary-v1.md`; that ENTIRE candidate's actual-block lift and parent f111 disposition were withdrawn/held after the fatal block/projection error. This new packet does NOT transfer or salvage its prior review verdict, and does not claim blind or independent prior exposure. It supplies the complete field-sequence argument separately, to be judged afresh.

## 1. Statement

Let p be ANY odd prime and let `z_1,...,z_(p+2)` be a sequence of elements of F_p with `z_i!=z_(i+1)` for every consecutive linear pair. Then there are original sequence indices `i<j<k<l` for which

`z_i−z_j+z_k−z_l=0`.  (1)

No full-support or pairwise-distinct hypothesis is imposed.

## 2. Full-support auxiliary argument

Suppose the entire field F_p occurs in an adjacent-distinct sequence of length p+2, but no (1) exists. For every consecutive triple let `t=z_i−z_(i+1)+z_(i+2)`. Some sequence occurrence has value t. If it is before the triple, or after it, it and that triple give an ordered zero quadruple. Thus all its occurrences lie inside the triple. Since adjacent values differ, t is neither first nor last, so it is the middle. This forces `z_(i+1)−z_i=z_(i+2)−z_(i+1)` for every triple. The entire sequence is an arithmetic progression of nonzero step d. Positions `1,2,3,p+2` then have alternating sum `−p d=0`, contradiction.

## 3. Multiplicities and crossing pairs

Assume no (1).

If some value occurs at least four times, choose four occurrences. If one value a occurs at least three times and a different value b at least twice, consider the three a occurrences relative to the interval between two b occurrences. If two a's are both before, both inside, or both after that interval, their pair and the b pair are disjoint or nested and have alternating sum0. If one a lies in each of the three regions, their order is `a,b,a,b,a`; the outer a occurrences and both b occurrences give `a−b+b−a=0`. Therefore, if any value occurs three times, it is the only repeated value and occurs exactly three times. A length-p+2 sequence with that multiplicity pattern has p distinct values, hence full support, contrary to §2.

Thus every value occurs at most twice. Let s be the number of doubled values. Since support has size `p+2−s<=p`, s>=2. Any two different doubled values must have crossing occurrence intervals: disjoint intervals produce `a,a,b,b`, nested intervals produce `a,b,b,a`, and either has alternating sum0.

## 4. The absent affine extensions

Fix any doubled value a and another doubled value b. Their occurrences cross, in one of the orders `a_1<b_1<a_2<b_2` or `b_1<a_1<b_2<a_2`. Put `x=2a−b`. Since p is odd and a!=b, x differs from both a and b.

If `a_1<b_1<a_2<b_2`, any occurrence of x gives one of the following actual ordered quadruples:

* x before a_1: `x,a_1,b_1,a_2`;
* x between a_1 and a_2: `a_1,x,a_2,b_2`;
* x after a_2: `a_1,b_1,a_2,x`.

If `b_1<a_1<b_2<a_2`, use instead

* x before a_1: `x,a_1,b_2,a_2`;
* x between a_1 and a_2: `b_1,a_1,x,a_2`;
* x after a_2: `a_1,b_2,a_2,x`.

The before/after sums are `x−a+b−a` and `a−b+a−x`. The middle sum is `a−x+a−b` in the first ordering and `b−a+x−a` in the second. All are zero because x=2a−b. Thus `2a−b` is ABSENT from the sequence for every doubled b!=a.

These s−1 absent field values are distinct as b varies. Yet the sequence's support has size p+2−s, so only s−2 values of F_p are absent. This contradiction proves (1).

## 5. Fresh bounded checks and scope

New local `frontier-20261028-olson-ordered-four-standalone-checker-v1.py`, SHA256 `d85a76b3f6630b3c220a5347d7dd3fda0257ad6cfcc0211354a35b7782a1eeb4`, returned `PASS_STANDALONE_ORDERED_FOUR_FINITE_CHECK` in `frontier-20261028-olson-ordered-four-standalone-check-results-v1.json`, SHA256 `59a9d32b3a4e004a3f00d29bcc9cad6b68dbb11371d822e1f4efcc1007ff5ce1`. It directly found original-index quadruples for all 16/4,096 normalized adjacent-distinct sequences at p=3/5, for 2,000 seeded samples each at p=7/11/13, and for all 60/200/420 crossing-extension insertion cases at p=3/5/7. Wrong-length, adjacent-equality and out-of-range controls were rejected for their intended reasons.

This finite check is not the all-prime proof, a disjoint reviewer, a formal/kernel proof, a cross-model-family review or novelty clearance. The standalone candidate must receive a NEW disjoint full-source review before adoption. It does not assert any repaired actual-block scope or resurrect the held f111 disposition.

**END — standalone field-sequence candidate only.**
