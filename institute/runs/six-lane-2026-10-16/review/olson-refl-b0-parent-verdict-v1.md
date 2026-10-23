# Olson: equal-rotation reflection rigidity in a numerical range, parent verdict v1

Recorded at 2026-10-18T12:34:15-07:00.

**CORRECTNESS-ACCEPTED, written partial theorem, with the overlay below.** No imposed hypothesis o_F≤p, but this is **not** every equal-rotation avoider and not full REFL(p), INV*(p), ordered Olson or a new gate. No novelty or Lean claim.

## Exact statement

For every prime p≥5, let w be an avoider of length4p−2 over D_(2p), with all rotation letters equal to one nonidentity rotation ρ_x. Let R count its rotations and let κ=p−1−Σ_i floor(l_i/2), computed on its **maximal cyclic constant reflection blocks**. If

**R≥4κ−4, 2κ≤p−1, and 5R≥4p+6κ−10,**

then every maximal cyclic reflection run of w is constant.

The original disjunction [R≥p+κ−2 OR5R≥4p+6κ−10] is equivalent here: the first alternative implies the second since κ<p. Dropping that redundant alternative changes no covered word. At length4p−2, o_F=2p−R+2κ; it is not arbitrarily large at fixedp,R,κ. No o_F≤p restriction is imposed. Mixed ρ_x/ρ_−x rotation words are not covered by this corollary.

## Text and reviews

- Text of record: [REFL-B0 r3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-REFL-B0-r3.md), SHA256 `c05eb38386e8e1a239f6abf51875f3fcc02c1ce2304cf14063be9d95bd412272`, plus this overlay.
- Both reviews examined the unchanged mathematical proof in [r2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-REFL-B0-r2.md), SHA256 `32671067ff7a6b355da0882d85416a2a472599e31a171aac6a2e7e7ef00c475b`. The parent read the exact [r2→r3 diff](olson-refl-b0-r2-to-r3-parent.diff): only title/scope/identity/example wording changed, no theorem hypothesis or proof step. No duplicate scientific run was performed.
- [Codex review](olson-refl-b0-r2-codex-v1.note.md), `9733a6220dad80f4ab16a8850ae8f85c2689e8a2f9bb600a9361360753de0c10`: ACCEPT-WITH-FIXES,0FATAL/MAJOR,2MINOR.
- [Claude review](olson-refl-b0-r2-claude-v1.note.md), `edc448e69f0e1948cadc3ee791ba8827d6a512524f33dfe7adf70c33bf3fb0f8`: ACCEPT-WITH-FIXES,0FATAL/MAJOR,7MINOR.

## Mandatory overlay

1. **Scope/title** (Claude m1,m6): use the numerical range above and “no imposed o_F≤p”. At p31,κ7,R32, the identity gives o_F44>31. A terminal word is hypothetical; no existence of avoiders with those parameters is assumed.
2. **Redundant branch** (m2): R≥p+κ−2 is subsumed by the5R condition. Keep it only as an alternative proof route, not as additional coverage.
3. **Degenerate cases** (m3): κ<0 makes H≥p, giving p disjoint equal-reflection pairs. κ0 is K0*. κ1 cannot produce the terminal κ′≥2. R0 is excluded by the accepted all-reflection EGZ argument; F0 is vacuous and equal rotations already give an identity selection. In the nonvacuous contradiction proof retainR,F≥1.
4. **Terminal invocation** (m4): RED is invoked only after assuming failure of reflection rigidity. Its g=0 exit is excluded through accepted (I2),(I3),K0*: the last fusion must merge odd–even–odd to an even block, while the terminal κ0RGR statement requires odd blocks. K0*/K1* exclude terminalκ′≤1. This B0 argument does not use P3/P4, TII,SING,QQ or (I1)/(I4).
5. **P1/P2 parity and maximal reread** (Codex1; m5): PM0 appends an even block to the next constant block **of either parity**. The floor identity preservesH for either parity. Its merged rotation run stays nonempty, so it introduces no extra fusion. In FUS only the recolored even block can merge with its two neighbours; a double fusion raisesH by1 exactly when the two outer blocks are odd, otherwise by0. Maximality prevents further equal-value fusion across an unchanged genuine gap. Thus R stays fixed andκ never increases on the actual maximal decomposition, not only on a temporary representation.
6. **Mixed-sign remark** (Codex2; m7): P3 preservesR,κ,B. P4 lowersR by2 andB by1 and lowersκ by1 (by2 if an additional odd–odd fusion occurs). They cannot occur whileB0, so the present fixedR composition makes no mixed-sign claim.
7. **CJ import** (m7): use the full accepted B0 setting—length4p−2,R,F≥1,maximal odd blocks,genuine empty runs—and the corrected [CJ parent overlay](olson-cj-cjx-parent-verdict-v1.md). k≥p+1 is only the branch used, not an extra hypothesis of CJ tripleprime. The accepted smallk argument remains a redundant second route.

## Parent derivation and acceptance boundary

The parent read the candidate and its r3 wording delta, both reviews, and the corrected CJ statement/interface. The new part is a preservation/composition argument:

- Normalize x to1 by the group automorphism multiplying rotation and reflection exponents byx^−1. This preserves equality, block lengths and increasing-index identity selections. B0 then holds throughout.
- P3 needs both signs in a donor run; P4 needs a(1,1)run. P1/P2 introduce no negative rotation, so neither becomes available. They preserveR,F,length. For a doubleFUS, ΔH=floor((a+b+c)/2)−floor(a/2)−b/2−floor(c/2), with b even; this is1 iff a,c odd. PM0 uses floor((a+b)/2)=floor(a/2)+b/2. Henceκ′≤κ.
- RED/K0*/K1* yield a genuine residual avoider withB0,alloddblocks,κ′≥2, sameR, if the initial word violated rigidity. The initially arbitrary o_F never needs a bound. If k′≤p, the accepted B0S result excludes it.
- Otherwise k′=2p−R+2κ′ and Δ′=p+κ′−1−R. The monotone inequalitiesR≥4κ−4≥4κ′−4 and2κ′≤p−1 discharge the strengthenedCJ hypotheses. Its correctedCor2 forcesΔ′≥2 andp<κ′+5Δ′−5. These implyR≤p+κ−3 and5R<4p+6κ−10 respectively, contradicting the stated alternatives.

[Exact parity smoke](olson-refl-b0-parent-parity-smoke-v1.json):15,376 finite length triples confirm the written floor identities; this is an aid, not a premise. The proof uses the algebraic identities for all lengths. Earlier p7 census cells, stopped jobs and numerical searches are not premises.

**Imports at accepted scopes:** RED's avoidance-preserving moves/termination, K0*/K1*, the RGR exit statements(I2)/(I3), B0S and strengthenedCJ+correctedCor2. The parent did not independently re-prove every imported page. Model-family written audits, not formal kernel checks, support those interfaces.

**Remaining open:** cells outside these numerical conditions, mixed rotations beyond existing restrictedREFL scopes, and full INV*/Olson. The [EDGE candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-B0Sedge-r2.md) claims the extra2κ≤p−1 hypothesis can be dropped, but is under separate reviews and is **not** accepted by this verdict. The [reflection CPU-limit deviation record](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/census-receipts-r1.md) is retained; affected attempts remainUNKNOWN and carry no proof weight.
