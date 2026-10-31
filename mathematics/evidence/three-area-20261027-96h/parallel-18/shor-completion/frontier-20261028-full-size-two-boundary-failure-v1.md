# Full-size Shor one-b layers: two-boundary uniqueness still does not imply UD

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 17:35:47 PDT 2026**.
**Exact explicit counterfamily to a relaxation, independently checked at bounded orders; not a finite completion or global Shor noncompletion.**

## 1. Exact conclusion

For EVERY positive integer m and n=32m, there is an explicit n-pair one-b residue set B_n that contains all16 literal Shor pairs and has NO repeated endpoint/internal-residue triple among its ordered two-atom paths. Nevertheless the corresponding actual words are NOT uniquely decipherable: three old/new one-b atoms give two different parses of the same raw word, with no pure-a padding.

Thus the following three necessary tests, even TOGETHER, are not sufficient for a Shor one-b layer to be UD:

1. all original Shor pairs are present;
2. its cardinality equals the compulsory pure-a exponent n;
3. all ordered two-one-b paths have distinct `(first head, internal seam, final tail)` residues.

This counterfamily covers arbitrarily large n, including n=5280, a multiple of660. That arithmetic compatibility is not a claim that any such n is realizable by a completion. Critically, this particular family FAILS the stronger actual-completion requirement of exactly n paths at EVERY fixed seam: it must NOT be presented as a counterexample to that conservation law.

## 2. Explicit base set and elementary two-boundary certificate

Let W_32 be the following 32 pairs (i,j), denoting actual words a^i b a^j:

    i=0:  j in {0,1,7,13,14,20,26};
    i=1:  j in {5,11,15,17,24,30,31};
    i=2:  j in {3,9,10};
    i=3:  j in {0,2,4,6};
    i=4:  j in {18};
    i=6:  j in {8,22};
    i=8:  j in {0,2,4,6};
    i=11: j in {0,1,2};
    i=13: j in {3}.

This includes the complete literal original set S, in its four original rows0,3,8,11. Every listed pair is distinct.

For a set W of unique endpoint pairs, let Δrow consist of all NONZERO differences of tails in one same row, and Δcol all NONZERO differences of heads in one same column, modulo n. The two-boundary triples `(i,j+k,l)` are unique iff Δrow and Δcol are disjoint: two paths with matching outer rows/columns and seam have equal respective nonzero differences, and conversely such a common difference gives two different paths.

A direct exact count for W_32 gives

    Δcol={3,5,8,11,21,24,27,29}
         = ±{3,5,8,11} mod32,
    Δrow=Z_32 minus ({0} union Δcol).

The sets are disjoint, so all 32²=1024 original two-atom triples are different. The verifier in §5 checks this directly rather than relying solely on the difference-set summary.

## 3. Universal lift preserves the full pair count and two-boundary uniqueness

For n=32m define

    W_n={(i+32k,j) : (i,j) in W_32, 0<=k<m}.

All heads lie in [0,n−1], tails in [0,31], and every pair is distinct, so `|W_n|=32m=n`. All16 original pairs occur at k=0.

Suppose two ordered two-atom paths in W_n have equal first head, internal seam and final tail modulo n. Reducing those equalities modulo32 gives equal base-path triples. The W_32 property forces the two FIRST base pairs and the two SECOND base pairs to agree. Equality of their first lifted heads fixes the first block index, while equality of the internal seam now reduces to `32(k−k')==0 mod32m`, fixing the second block index. Hence the lifted paths themselves coincide. This proves TWO-boundary uniqueness for EVERY m, not just the checked values.

For a fixed seam gamma modulo n, the number of W_n paths equals m times the number for the base seam gamma mod32: a base path with that residue has one second block index for each of m first-block choices. In particular the base seam0 has44 paths, so the lifted seam0 has44m, NOT n=32m. The true all-list/conservation theorem therefore excludes these layers even before noticing the explicit three-word ambiguity. This observation is a limitation of the counterexample, not a reason to overlook its direct falsification of the weaker tests.

## 4. Raw three-atom ambiguity for every lifted order

All six words below are in the lifted set because the required pairs occur in W_32:

    (a^11 b)(a^3 b)(a^11 b)
      = (a^11 b a)(a^2 b a^3)(a^8 b)
      = a^11 b a^3 b a^11 b.

The two lists are different and have exactly the same actual word. Therefore ANY code containing these atoms, whether or not it also contains a^n, is not UD. A positive answer for the original Shor question would require a DIFFERENT set of added atoms, full all-list UD and factor-completeness.

## 5. Actual bounded computations and independent validation

A bounded Z3 run `python3 -B frontier-20261028-bayonet-layer-sat.py 32 15000` returned SAT and supplied the explicit base set. Its propositional model imposed old-pair inclusion, cardinality32 and disjoint same-row/same-column differences. This is a generator only; SAT is not proof that a complete code exists.

The NEW standalone `frontier-20261028-layer32-independent-check.py` then read the saved model without importing the solver/producer. Actual command:

    python3 -B frontier-20261028-layer32-independent-check.py frontier-20261028-layer32-model-v1.json

It checked all1024 actual base two-atom triples, confirmed the original pairs and the raw three-atom equality, and checked lifts m=1,2,3,5, i.e. n=32,64,96,160, with1024,4096,9216,25600 distinct two-path keys. Base seam counts had minimum7, maximum62 and seam0 count44; the lifted min/max were respectively doubled/tripled/quintupled. Three deliberate defects were rejected for their intended distinct reasons: `DUPLICATE_PAIR`, `OLD_PAIR_MISSING`, `TWO_BOUNDARY_COLLISION`.

The verifier's pair enumeration and the explicit difference sets certify the finite W_32 facts; §3's written argument supplies every m, not just the checked lifts. No external-model or formal prover acceptance is claimed.

| Artifact | Native SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-layer32-model-v1.json` | ed7cf4b9864981840d72cf819a277e910487eb06983e6ffd0f08fe81bf102a00 |10 /525 |
| `frontier-20261028-layer32-independent-check.py` | 05ef89827dac5815b1832cebfde1d16e725857de64bd5f756627b01c807e1213 |96 /3254 |
| `frontier-20261028-bayonet-layer-sat.py` | ae34c24df45a2a2ccaf297fff685444233616374ac1c3bb0c4b216d30b116afc |59 /2509 |

Native artifact pin observation: Wed Oct28 17:35:47 PDT.

## 6. Actual remaining gap

The stronger necessary system for a genuine finite completion includes SAME-layer all-length zero-one path products and exactly n paths for EVERY internal residue word, plus all raw multi-b UD and factor-completeness. The present false layer violates those conditions; no counterexample to them or finite completion is claimed. Its role is to expose why cardinality plus pairwise uniqueness, even for a layer of the full target size and at arbitrarily large arithmetically compatible orders, cannot replace the actual all-list bridge. No novelty/priority or stronger assurance follows.

**END OF FULL-SIZE TWO-BOUNDARY FAILURE COUNTERFAMILY.**
