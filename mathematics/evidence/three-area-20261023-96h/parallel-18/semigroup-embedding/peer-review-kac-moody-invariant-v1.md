# Bounded peer reconstruction — Kac–Moody invariant bridge

Reviewer: MathSemigroup (math-4), assigned by `peer-review-wave-eighteen-v1.json`. Clock actually observed immediately before writing: **2026-10-23T14:18:58-0700**.

## Verdict and exact pin

**No FATAL, MAJOR or MINOR mathematical defect found at the explicitly stated scoped theorem and import boundary.** The invariant bridge is suitable for parent written consideration, not automatically accepted by this review. The full all-r,s level-four band, arbitrary-level Serre conjecture, novelty, formal verification and literature priority are NOT established.

Reviewed **the complete body, lines1–219**, of

`mathematics/evidence/three-area-20261023-96h/parallel-18/kac-moody/invariant-bridge-v1.md`

at actually observed SHA-256

`26485dba4591ca16c8d5dfa66b5793bae5f28635c54be2938e7f50ab6f343a2c`.

This matches the parent's required pin. Also read the exact current selection and relevant original definitions/presentation proofs. No author file was changed. No executable mathematical calculation, solver, enumeration, compilation, build/test/lint/formatter, nested agent or model CLI was run. The computations below are written symbolic reconstructions, not software/kernel evidence.

## 1. Source and hypothesis boundary reconstructed

The theorem is injectivity of D3 on the **invariant part** of the actual S4 for A(r,s), every positive integer r,s. It does not assert injectivity on all Levi-lowest spaces. The full Cartan realization remains; Levi weight(0,0) at level4 means full multidegree(4,4,4), not full Cartan degree zero.

I read `proof.md` §§1–4,7–8 for the actual realization, lowering sign/row convention, stability and radical recurrence; `evidence/round2-coefficient-two.md` §§3.1,4.2–4.5 for elimination, V=ad(sl3), the explicit exterior-square decomposition and original-row lowering; historical STRUCTURAL/degree3 notes for the exact conditional alpha3<=3 dependency. The historical height-seven receipt was read only at its scope fields and pinned; its large certificates were NOT replayed.

Observed dependency hashes match every corresponding source pin in author lines207–212:

- `proof.md`: `5f7c3e3d98d4b3c521cb21b0ff76a91d939ec1d2d0fd76f55a6e5f7c1b1e4b5f`
- coefficient-two note: `82630f6bc98b8b9d1bfcc3d8882cafee8e62264a0a4defa6aaf174185e180473`
- STRUCTURAL: `94b8b1fe14dea85f06ed27dc3f7aff07dbb9b5d8d2296f8302d143223e659694`
- degree3 notes: `b2b416ff9a4f34ed27bea0eb01a3907e85bc6c55a45fb2dfddd6262b89b56696`
- height-seven parent receipt: `7275abb3ecfc9b8c0efc4c437274229cec6be4245ae5674d69ef79df7b48c44d`
- historical level-four check: `4aa35babdd8dc7641c560b036de9ab8ffea5d40da613931cda839533f5027172`

The last historical level-four determinant is not used to accept the new invariant proof. Classical finite-Levi semisimplicity, sl3 classification/dimensions and graded PBW/Witt remain explicit mathematical imports. The new proof does not assume irreducibility of an unknown nonsymmetrizable whole algebra.

## 2. Exact small-row ideals and quotient-lowest lifting

Author lines25–50 are correct through the specified levels. With v=E31, u=-E32 and w=E21, the relation (ad v)^q(E_jv) has level q+1; its tensor term v^q(E_jv) has coefficient1 and cannot cancel. F_j E_jv=v and F_iE_jv=0 for i!=j, so lowering the displayed relation leaves (ad v)^q v=0. It is a genuine lowest vector, not a free-space label.

For j=1 its weight is q(-1,-1)+(1,-2)=(1-q,-q-2). Applying the A2 longest Weyl element gives highest weight(q+2,q-1); the Weyl dimension formula is q(q+3)(2q+3)/2, giving10,35,81 for q=1,2,3. The j=2 summands are dual. Finite-dimensional complete reducibility makes each cyclic lowest module the appropriate simple module.

Through level4 an ideal generated in levels2,3,4 has exactly

    T2=Q2,
    T3=[V,Q2]+Q3,
    T4=[V,[V,Q2]]+[V,Q3]+Q4.

The potentially omitted [L2,Q2] term is already included by Jacobi; so are [Q2,Q2] terms. Levi stability adds no separate homogeneous generators. Positive generation cannot lower level. These are both source AND target ideals for the original row, not ranks in the unchanged free L4.

The quotient-lowest identity at author lines54–58 is valid because a Levi-stable complement of T gives a direct-sum quotient. Simultaneous F1/F2 kernels then descend summand by summand, weight by weight. This uses no false assertion that D3 itself is Levi-equivariant.

## 3. Invariant line, nonzero bracket and actual source survival

I reconstructed the invariant character argument in author lines64–84. The decomposition

    V tensor V=1 + 2V + 10 + 10* + 27

gives invariant multiplicity8 in V^tensor4. For R=V tensor V, the invariant flip trace on R tensor R is4:1 from the trivial summand,2 from the multiplicity-two adjoint block,1 from27, and0 from the exchanged10/10* blocks. Each self-dual irreducible here has a symmetric invariant form. Thus the PBW/Witt character formula gives (8-4)/4=1 for L4's invariant multiplicity.

The bracket map Lambda2(Lambda2V) --> L4(V) is genuinely injective: in the tensor algebra it is the ordinary block antisymmetrization p tensor q - q tensor p; concatenation of two degree-two tensor blocks is injective. The canonical nonzero pairing tensor between the two dual10 modules therefore has a nonzero bracket X. It spans the unique invariant line.

If r=1 or s=1, one10-module is in Q2; hence [M1,M2] lies in T4 and the invariant is killed. If r,s>=2, Q2=0. The remaining T4 is an equivariant image of V tensor Q3 plus81-dimensional simple summands; none can contain a trivial summand because Hom_g(V*,35)=0 and81 is nontrivial. Invariants are exact in these finite-dimensional modules. Therefore the source invariant dimension is exactly0 or1 as claimed. No higher relation is ignored in this source-survival argument.

## 4. Independent reconstruction of the two-adjoint noncancellation step

I derived the author lines119–137 directly from matrix brackets, not a saved certificate. For a=E31,b=E21,c=E32,d=E12,e=E23,h=H1,k=H2, the required lowering brackets are

    [b,c]=-a, [b,d]=-h, [b,h]=2b, [b,k]=-b,
    [c,b]=a, [c,e]=-k, [c,h]=-c, [c,k]=2c,

with [b,a]=[c,a]=[b,e]=[c,d]=0. Derivation on the five exterior basis vectors gives

    F1 A=a wedge b wedge h+2a wedge b wedge k,
    F1 B=a wedge b wedge h,  F1 C=0,
    F1 D=a wedge b wedge h,  F1 E=a wedge b wedge k;

    F2 A=-2a wedge c wedge h-a wedge c wedge k,
    F2 B=0, F2 C=a wedge c wedge k,
    F2 D=a wedge c wedge h, F2 E=a wedge c wedge k.

Their common kernel is exactly A-3B+3C+2D-2E. The listed five vectors exhaust this weight space: one a with two Cartan vectors, a with either opposite-root pair, and b wedge c with either Cartan vector. A joint lowest vector at weight(-1,-1) generates an adjoint module, so its multiplicity is one.

For delta0=(id tensor matrix-bracket)j I independently obtain

    delta0 A=-h tensor a+k tensor a,
    delta0 B=a tensor h+b tensor c,
    delta0 C=a tensor k-c tensor b,
    delta0 D=-b tensor c-2c tensor b-h tensor a,
    delta0 E=2b tensor c+c tensor b-k tensor a.

Hence

    delta0 Z=-3(h tensor a+a tensor h)
              +3(k tensor a+a tensor k)
              -9(b tensor c+c tensor b),

which is nonzero in the actual tensor product. This proves that the unique adjoint in the Jacobi-kernel Lambda3V has a nonzero M0 projection. No nonzero adjoint-kernel vector can consequently be supported solely in V tensor(M1+M2). Since each of V tensor Mi has one adjoint copy, their bracket images are injective and independent. This verifies the key noncancellation bridge at full representation multiplicity, not just at one tensor coordinate.

## 5. Original-row D3 and target quotient

With the fixed sign convention, Dv=-h3, Du=-r e1, Dw=-s e2. Since h3 acts on u with weight2-r,

    D[v,u]=-(2-r)u+r u=2(r-1)u,

and the dual calculation gives2(s-1)w. D commutes with both Levi raisings, so its restrictions to the cyclic Mi have the respective factors r-1,s-1 uniformly, not at sampled parameters. Taking Levi translates of f3 extends these to the equivariant W tensor Mi maps, with W the dual adjoint level-minus-one module.

Contraction against a perfect M1/M2 pairing is faithful. Each nonzero bracket map W tensor Mi --> V therefore produces a nonzero adjoint tensor map into V tensor M_(3-i). Section4's bracket injectivity makes both resulting A,B nonzero. Their images lie in the two independent adjoint modules just reconstructed; no relation between r,s can cancel these terms when their coefficients are nonzero. For r,s>=2 this proves DX!=0.

The **actual** T3 in that regime is Q3 and has only35-dimensional simple constituents. It intersects the two8-dimensional adjoint images trivially, so the nonzero detection survives in S3. For min(r,s)=1 the source invariant is zero, not a falsely detected surviving free vector. This verifies the exact quotient, not a free-space rank surrogate.

## 6. Residual scope, findings and handoff

Conditional on the explicitly retained lower-level and coefficient-one imports, a first level4 defect has a,b>=2 and2a-b<=4,2b-a<=4. Solving gives a,b<=4; an entry4 forces the pair(4,4), whose Levi-zero lowest vector is invariant and has just been excluded. The four remaining degrees listed at author line197 are exactly(2,2,4),(3,2,4),(2,3,4),(3,3,4). They remain unresolved by this packet; no all-four-cell or all-level conclusion is licensed.

**Findings:** FATAL0; MAJOR0; MINOR0, at this declared scope. Source trusts and historical certificate dependencies remain unrefreshed beyond the reads/pins stated above; that limitation is preserved rather than recorded as a defect in the author's explicitly qualified theorem. This was an ordinary in-harness supplied-proof reconstruction, not blind, cross-vendor, human, formal or novelty review. Parent must still read/compose its own verdict.

Returning to my ONE primary semigroup problem after this assigned bounded reconstruction.
