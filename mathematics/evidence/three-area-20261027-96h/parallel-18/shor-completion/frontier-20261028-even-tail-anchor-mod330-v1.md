# Shor completion: anchored tail fibres sharpen to mod330

Owner **MathShor-2**, math-5. Native clock of exact residue controls: **Wed Oct 28 21:34:36 PDT 2026**.
**ALL-ORDER WRITTEN necessary refinement, conditional on the explicitly imported common-prime T2 fibre theorem; no completion/noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Exact same-code conclusion

Under the SAME hypotheses as `frontier-20261028-even-tail-two-power-fibres-v1.md`, namely

    n=165*2^k,   k>=2,   |P|=3*2^a,   |Q|=55*2^(k-a),   1<=a<k,

and the literal Shor old anchors, write a Q-tail in one of the old mod55 classes as

    q = j + 110t  (mod n),   j in {0,1,7,13,14}.

The cited common-prime T2 fibre theorem proves that this representation is necessary for each such actual Q-tail. The new refinement is

    j in {1,7,13}:   t==0 mod3,  hence q==j mod330;
    j=0:             t!=2 mod3;
    j=14:            t!=1 mod3.                                (1)

All residues and factorization data belong to the SAME actual D. No statement is made about other mod55 fibres or the existence of a completion.

## 2. Proof by old-head gcd3

The old heads0 and3 give a P-difference with gcd3 against `n=165*2^k`. Thus the classical Sands gcd-disjointness criterion prohibits any two Q-elements whose difference has gcd3 with n. The only prime divisors of n are2,3,5,11.

Take an odd old anchor `j in {1,7,13}`. The fibre condition makes `q=j+110t` odd. Compare q to the actual old even tails0 and14. In BOTH comparisons the difference is odd and is nonzero modulo5 and11. For q versus0 it is divisible by3 exactly when `t==1 mod3`; for q versus14 it is divisible by3 exactly when `t==2 mod3`. Either event would give forbidden gcd3. Therefore only `t==0 mod3` is possible, proving the first line of (1).

For j=0, compare `q=110t` against any of the old odd tails1,7,13. The difference is odd, nonzero mod5 and11, and divisible by3 when `t==2 mod3`; this value is forbidden. For j=14, the same comparison gives forbidden `t==1 mod3`. This proves all of (1).

## 3. Evidence and explicit imports

The prerequisite `frontier-20261028-even-tail-two-power-fibres-v1.md`, SHA256 `f2a5655a3ea65a9150298ada9b7e7c17b1cec02e2ae040e522416897fc2c3706`, explicitly imports [Łaba–Londner, Corollary6.2](https://arxiv.org/html/2106.14042v1) for common-prime T2, together with the classical actual-border and Sands criteria. Its 165 simultaneous fibre factorizations are not re-proved or silently upgraded here.

`frontier-20261028-even-tail-anchor-mod330-check.py`, SHA256 `9e1051d508a6658568cd84f450a80d39fe93cda8161af50656bdac6c591e7f2d` (17 LF, 709 bytes), verifies the six odd-anchor and six even-anchor gcd3 identities at n2640. Those are bounded controls; the prime/divisibility reasoning above proves (1) for every stated k.

This refinement does not eliminate the cardinality family, determine t for the two even fibres, or establish unrestricted Shor noncompletion. The original finite UD factor-completion problem remains OPEN; no scientific review, formal verification, independent-family review or novelty clearance is claimed.

**END OF ANCHORED-TAIL MOD330 REFINEMENT.**
