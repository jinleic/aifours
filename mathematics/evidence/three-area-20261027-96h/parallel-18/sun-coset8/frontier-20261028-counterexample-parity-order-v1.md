# Parity refinement of the conditional simple-factor order bound

**Status: WRITTEN-checked-in-kernel, CONDITIONAL and UNREVIEWED.** At exactly the input scope of `frontier-20261028-counterexample-prime-complexity-v1.md` SHA `f69767d6edfab0c0fe7e0925ffb0197c8777e9c4fce542b07f3a818ba61f11a8`, failure of arbitrary-group Sun8 would supply an actual-P7 finite nonabelian simple composition factor S satisfying the stronger necessary bound

\[|S|\ge135{,}795{,}660.\]

If v_7(|S|)=1, the stronger bound is |S|≥446,185,740. These are conditional necessary conditions, not constructions, simple-group classifications, Sun8 proofs, priority or adoption claims. In particular the case v_7(|S|)≥2 remains allowed.

The input explicitly assumes the prior all-group Sun7 written-composition interface, prior R8/finite-core/normal-section descent, and the unreviewed Jones-based simple prime-support/exception criterion; none of these sources or proofs is newly adopted or independently replayed. The R8 and normal-section steps are prior work, not new discoveries. Read the earlier pre-source overlays in order `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` → `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` → `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` before affected bodies. No historical hold or old finding is modified.

## 1. An elementary even-order observation

For any finite nonabelian simple group S, if 2 divides |S| then 4 divides |S|. Otherwise Cauchy's theorem gives an involution t and |S|/2 is odd. In the left regular action of S on itself, t is a product of |S|/2 transpositions and hence is odd. The sign of that regular permutation action is a nontrivial homomorphism S→C2, impossible for a nonabelian simple group. This argument does not assume the odd-order theorem: groups of odd order are retained as a separate case below.

## 2. Distinct-prime products

The input gives 7 dividing |S| and at least eight distinct prime divisors of |S|/7. If S has even order, the preceding observation supplies an extra factor 2 beyond the first factor in the cofactor's distinct-prime product. The least possible such product is

\[2^2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19=19{,}399{,}380,\]

and multiplying by 7 gives 135,795,660. If S has odd order, the least product of eight distinct odd primes is

\[3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot23=111{,}546{,}435,\]

and multiplying by 7 gives 780,825,045, which is larger. Thus the first bound holds without excluding odd order by an imported theorem.

If v_7(|S|)=1, the cofactor |S|/7 has no factor 7. In the even-order case its least allowed product is

\[2^2\cdot3\cdot5\cdot11\cdot13\cdot17\cdot19\cdot23=63{,}740{,}820,\]

which gives 446,185,740 after multiplying by 7. In the odd-order case the least eight-prime product excluding 7 is

\[3\cdot5\cdot11\cdot13\cdot17\cdot19\cdot23\cdot29=462{,}120{,}945,\]

which gives 3,234,846,615 after multiplying by 7. The four products were checked using exact integers in the author's eval kernel; no simple group or coset configuration is claimed to achieve any bound.

## 3. Scope and review

A disjoint reviewer should check the Cayley-action parity argument, the ω/cofactor input and all four prime-product minima. For the original group the simple-section direction remains necessary only, not a converse lift. No mathematical review, novelty, public proof, formal/kernel or all-simple/global result is implied by this additive arithmetic refinement.
