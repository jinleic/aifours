# A seminormal-band family with arbitrary permutation-group actions

**Status: NEW AUTHOR WRITTEN MODEL FAMILY and exact finite controls; UNREVIEWED / UNADOPTED.** This provides a noncommutative, non-globally-regular band representation for testing original physical-host kernels beyond C₂. It does not embed an arbitrary source or prove universal comparable/R/L separation.

## 1. Definition and exact structure

For any nonempty set I let `B_I={x} ⊔ {u_i:i∈I} ⊔ {v_i:i∈I}` with multiplication

`a x=x` for every a;
`x u_i=v_i`, `x v_i=v_i`;
`u_i u_j=u_i`, `u_i v_j=v_j`;
`v_i u_j=v_i`, `v_i v_j=v_j`.

Every element is idempotent. The product of a nonempty word is described exactly as follows: if its final letter is x, the result is x; otherwise take the suffix after its last x, or the whole word when x is absent. If this suffix contains any v-letter, the result is its last v-letter. If it contains only u-letters, the result is its first u-letter when the whole word has no x, and the corresponding v-letter when a last x is present. These rules follow directly from the multiplication table and also show associativity: evaluating any prefix before multiplying the remaining suffix preserves precisely this last-x/last-v/first-u data. Equivalently, a case split on the middle factor's type verifies all 3³ structural associativity cases.

The local corners are

`xB_Ix={x}`, `v_iB_Iv_i={v_i}`, `u_iB_Iu_i={u_i}∪{v_j:j∈I}`.

The latter is a right-zero band with an identity u_i; it is a regular band. Thus B_I is locally regular. It satisfies the seminormal identity `abcda=abcacda` directly from the word rule: if a=x both sides end in x; if a is a v-letter both sides equal that final letter. If a is a u-letter and one of b,c,d is v-type, the rightmost such v has the same index on both sides. With no v-type among b,c,d, the last x and the first u after it have the same type/index on both sides (the repeated c only moves a possible last x to an identical c before d,a); if there is no x, both sides retain the first u=a. Thus the identity holds for arbitrary I, independently of the earlier unreviewed local-regular/SN equivalence.

If |I|≥2, B_I is not globally regular: for i≠j, `u_i x u_i u_j u_i=v_i` whereas `u_i x u_j u_i=v_j`. These are the regular identity's `xyxzx` and `xyzx` with `(x,y,z)=(u_i,x,u_j)`.

## 2. Full automorphism group and arbitrary groups

Every permutation σ of I defines an automorphism by `u_i↦u_(σ(i))`, `v_i↦v_(σ(i))`, x↦x. Conversely an automorphism preserves the u-type elements, since precisely those have a nonsingleton local corner. Among the remaining right-zero elements, x is the unique element moved by right multiplication by some u; every v_i is fixed by all u. Hence x is fixed, u_i are permuted, and `v_i=xu_i` forces the same index permutation on v_i. Therefore

`Aut(B_I)≅Sym(I)`.

In particular any group G acts faithfully on B_G through its left-regular permutation action on I=G. Thus arbitrary nonabelian groups can act on locally regular/SN bands which are not globally regular as soon as |G|≥2. This is an action carrier, not an arbitrary-source faithful-host construction.

## 3. Exact controls and targeted original-source attack

`frontier-20261028-symmetric-local-band-checker-v1.py`, SHA `3bc8655f0b319be83512758ad006fcda7f0104d7f6c2a036a2dbb65d07c77c8c`, checked sizes |I|=1,2,3,4 in the Python eval kernel before Wed Oct 28 23:23:44 PDT 2026: all products-of-three, every seminormal substitution, all local corners/regular identities, all index-permutation automorphisms and the displayed global-regular counterexample. It checks the listed automorphisms, not a separate exhaustive permutation search over all (2|I|+1)! maps; the full Aut claim is the written argument.

The separate bounded source attack `frontier-20261028-nonabelian-sevenband-horn-attack-v1.py`, SHA `8da5d7a1a81d428468b96ed51aac32eec38f7c6028637e1b45e3cf3dd7a03caa`, uses B_(3) with its S₃ action and a24-element twisted Rees S₃ actor. It forms the 168-element physical host and every single-pair actor-compatible congruence generated in an idempotent actor fibre. These yield12 distinct source quotient partitions, with source sizes36,48,108,120. The canonical Horn comparable test found no collapsed pair in this family; the actual observed search completed in1.222s with no timeout. This is a **negative finite search outcome**, not a theorem for all S₃ sources or proof of the original comparable-separation condition. The programs are same-author and all mathematics/source assumptions await independent review.
