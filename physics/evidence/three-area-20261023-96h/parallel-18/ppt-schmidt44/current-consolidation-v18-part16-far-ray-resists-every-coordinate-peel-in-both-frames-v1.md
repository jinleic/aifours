# CURRENT P44 CONSOLIDATION v18 — PART16/16: the far balanced ray resists every coordinate peel, in both natural frames

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 00:01:38 PDT 2026**. Exact WRITTEN mathematics. All inequalities are proved by hand (Cauchy–Schwarz and exact block entries). No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff (2026-10-27T11:05:38-07:00) and deadline.

## G0. Scope, union rule, status

NEW claim C35 is a METHOD barrier. It concerns peel compressions of the ORIGINAL chart state on its far balanced ray. It is NOT a statement that SN=3 and NOT an SN<=2 statement.

The complete current union is:
- the fifteen parts bound in `checkpoint-092-complete-current-v17-fifteen-part-manifest-v1.json` (SHA256 986f195b63528f6daf82fd0d0ced2662b29eeab0d7f47cd50578978c105a4711);
- `current-consolidation-v17-part15-ADDENDUM-1-interpolation-proof-and-source-identity-erratum-v1.md` (SHA256 2f001f2e6ba538bcb473e695eee042cb36d36525083016266f2b825b278b9b50);
- THIS part;
- every mandatory overlay.

Parts 9–16 are LATER UNREVIEWED; nothing is inherited.

Notation is as in Part15 Q1: a,b,c,d_x,e,f,g,j,h_x and R_x. A **peel** is a compression by 1-|φ><φ| on one side. By Lemma L (Part15 Q2), a separable peel compression certifies SN<=2. The **coordinate peels** are the eight peels with φ a computational basis vector of Alice or Bob.

## G1. Statement

**Theorem C35.**
1. *(Original frame.)* For real s > 6(1+√2) (about 14.49), every one of the eight coordinate peel compressions of R_(s,s,s,s) is entangled.
2. *(Involution frame.)* For 0<|ζ|<1/(6√2), every coordinate peel compression of R_(1,1,-1,ζ), and the adapted Bob peel along |0>+ζ|3>, is entangled. This is Part15 C34.4, restated for completeness.

By the Part6 involution R_(s,s,s,s) ~ R_(1,1,-1,1/s), so for every s>6(1+√2) BOTH representatives defeat all coordinate peels. No Lemma-L certificate through a coordinate direction exists in either frame.

## G2. The six peels already excluded by Part15 at (s,s,s,s)

At x=(s,s,s,s) we have u=v=w=z=s!=0. Part15 C34.3 excludes:
- **Bob-0, by (e):** with V=|v|^2=s^2 and W=|w|^2=s^2, 12-6W-4V-9W^2-6VW = 12-10s^2-15s^4 < 0 for s>=1.
- **Bob-2 and Alice-2, by (b):** z,v!=0.
- **Alice-0, by (c):** z!=0 and v!=0.
- **Alice-3 and Bob-3, by (d):** always.

Part15 (a) only gives the NECESSARY condition |z|>=1/(6sqrt(1+|w|^2)) for Alice-1 and Bob-1, which holds at (s,s,s,s). These two peels are settled below.

## G3. The Bob-1 peel at (s,s,s,s) is entangled for s>6(1+√2)

**Reduction.** Removing Bob |1| sends:
- b→|12> and c→|10>, products on Alice |1>;
- a→|00>+|22>;
- d→|02>+s|3>⊗y and h→s|0>⊗y, with y=|0>+|2>+|3> (Bob);
- e,f,g,j unchanged.

Write A=Alice|0>, B=Alice|2>, C=Alice|3>, and a,b,c=Bob|0>,|2>,|3>. The compression is P(|12>)+P(|10>)+Q(s), with

`Q(s) = P(Aa+Bb) + 3P(Ab+sCy) + 3P(Ba+Cc) + 3P(Ca) + 3P(Cb) + 3P(Bc) + 3s^2 P(Ay)`.

It is separable iff Q(s) is, by compressing Alice onto {A,B,C}. Apply the invertible Alice filter A→A/s, C→C/s, which preserves separability. With ε=1/s this gives

```
Q' = P(Bb+εAa) + 3P(Cy+εAb) + 3P(Ba+εCc) + 3ε^2P(Ca) + 3ε^2P(Cb) + 3P(Bc) + 3P(Ay).   (G3.1)
```

The seven vectors in (G3.1) are linearly independent. The coordinates Bb, Ba, Bc and Ac occur only in the first, third, sixth and seventh vectors, so those coefficients vanish in any dependency. The Ab coordinate then isolates Cy+εAb, after which Ca and Cb are independent. So every decomposition Q'=Σ_i ψ_iψ_i* into range vectors has coefficient Gram exactly diag(1,3,3,3ε^2,3ε^2,3,3).

**Forced form.** Suppose Q' is separable, Q'=Σ_i w_i π_iπ_i* with product π_i. The coordinate Bb occurs only in the first vector. Every product with a nonzero Bb-component therefore has first coefficient α!=0; normalize α=1, absorbing |α|^2 into w. Its rows (Alice A,B,C; Bob a,b,c) are:
- Row_B = (e',1,κ);
- Row_A = (ε+η, εδ+η, η);
- Row_C = (δ+φ', δ+γ', δ+εe').

Here δ,e',φ',γ',κ,η are the range coefficients. Being a product, Row_A=p·Row_B and Row_C=t·Row_B for scalars p,t. Hence

```
(R1) ε+η=p e',  (R2) εδ+η=p,  (R3) η=pκ,  (R4) δ+εe'=tκ.
```

R1 with R3 gives p(e'-κ)=ε, so e'!=κ. R2 with R3 gives εδ=p(1-κ). Therefore **1-κ = δ(e'-κ) = (tκ-εe')(e'-κ)**, using R4 in the last step.

**Exact constraints from Q'.** Sums run over the products with a Bb-component.
- (Q1) Σw=1. The (Bb,Bb) entry of Q' is 1, and only these products touch Bb.
- (Q2) Σwκ=0. The (Bc,Bb) entry is 0, since no vector of (G3.1) contains both.
- (Q3) Σw|e'|^2<=3 and Σw|κ|^2<=3, from the (Ba,Ba) and (Bc,Bc) entries. Also Σw|δ|^2<=3, from the coefficient Gram.
- (Q4) The C-block of Q' is 3P(y)+3ε^2 I. For z=a-b and z'=b-c, both orthogonal to y, <Cz|Q'|Cz> = <Cz'|Q'|Cz'> = 6ε^2. A product contributes |t|^2|e'-1|^2 and |t|^2|1-κ|^2 there. Hence Σw|t|^2|e'-1|^2<=6ε^2 and Σw|t|^2|1-κ|^2<=6ε^2.

**Contradiction.** By (Q1),(Q2), Σw(1-κ)=1. Insert the identity above:

`1 = Σ w tκ(e'-1) + Σ w tκ(1-κ) - ε Σ w e'(e'-κ).`

Cauchy–Schwarz with (Q3),(Q4) bounds the three terms:
- |Σ w tκ(e'-1)| <= sqrt(6ε^2)·sqrt(3) = 3√2 ε;
- |Σ w tκ(1-κ)| <= 3√2 ε;
- ε|Σ w e'(e'-κ)| <= ε·sqrt(3)·sqrt(2·3+2·3) = 6ε.

So 1 <= (6+6√2)ε. **For ε<1/(6+6√2), i.e. s>6(1+√2), Q' is entangled and so is the Bob-1 compression.** ∎

## G4. The Alice-1 peel at (s,s,s,s) is entangled for s>6(1+√2)

Removing Alice |1> sends a→|00>+|22>, b→|01> and c→-|21>, and leaves the rest. Use Alice A=|0>, B=|2>, C=|3> and the full Bob basis 0,1,2,3, with Y=|0>+|1>+|2>+|3>. After the same filter A→A/s, C→C/s the compression is

`P(B2+εA0) + 3P(CY+εA2) + 3P(B0+εC3) + 3ε^2P(C0) + 3ε^2P(C2) + 3P(B3) + 3P(AY) + ε^2P(A1) + P(B1)`.

Products carrying B⊗|2> have Row_B=(e',μ,1,κ), Row_A=p·Row_B and Row_C=t·Row_B. They give the same relations: p(e'-κ)=ε, εδ=p(1-κ) and δ+εe'=tκ, together with δ=tμ.

The constraints are the same as in G3:
- Σw=1, from the (B2,B2) entry 1.
- Σwκ=0, from the (B3,B2) entry 0.
- Σw|e'|^2<=3 and Σw|κ|^2<=3, from (B0,B0) and (B3,B3).
- Σw|δ|^2<=3, since the nine vectors are independent.
- The C-block is 3P(Y)+3ε^2(P(0)+P(2)+P(3)). The vectors |0>-|2> and |2>-|3> are orthogonal to Y and have C-block value 6ε^2. Hence Σw|t|^2|e'-1|^2<=6ε^2 and Σw|t|^2|1-κ|^2<=6ε^2.

The same three Cauchy–Schwarz bounds give 1<=(6+6√2)ε. ∎

## G5. Consequences and interpretation

1. **Combined with G2,** for s>6(1+√2) all eight coordinate peels of R_(s,s,s,s) fail. In the involution frame (1,1,-1,1/s), all eight coordinate peels and the adapted peel fail as soon as 1/s<1/(6√2) (Part15 C34.4). Both thresholds hold together for s>6(1+√2).
2. **Necessary-condition evidence only.** Lemma L is one sufficient mechanism; its failure for coordinate directions does NOT imply SN=3. Other mechanisms remain possible: non-coordinate peels, Part13/14 phase families, or general SR2 decompositions. So does SN=3. The far ray is now the sharpest known candidate region of this chart for P44. No SN3 claim is made.
3. **Contrast with x0.** At the limit point x0 the Bob-0 peel succeeds (Part15 C34.1). Along the far ray every coordinate peel fails in both frames, so the SN2 certificate of the limit does not propagate by peeling.
4. **The mechanism of G3/G4 is new:** a linear identity forced on the Bb-carrying products, 1-κ=(tκ-εe')(e'-κ), played against near-rank-one blocks. It is recorded so that any future far-ray SN2 construction must route its α-budget through non-product compressed vectors.

## G6. Original gap

Original physics-3/P44 remains UNMET. Missing:
- an explicit rational 4x4 PPT state with SN>=3 and a universal complex SR2-nonnegative strict negative separator; or
- an unrestricted all-state theorem.

In this chart the far balanced ray (s>6(1+√2) proved peel-resistant; 5<s<=6(1+√2) unexamined beyond the C34.3 maps) and the z!=0 comparable core remain OPEN. N4 is historical UNKNOWN/exit-unestablished and old21 is NOT_RECONSTRUCTED. All process findings are retained.

These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v18 PART16/16.**
