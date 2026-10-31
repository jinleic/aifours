# Every PPT rank-two test projector is separable

**Status: WRITTEN, UNREVIEWED.** The projector classification below is proved directly, without importing a rank-two PPT theorem. Its application to the original T2 inequality depends on the separately UNREVIEWED `frontier-20261029-d4-t2-separable-projector-complete-consolidated-v2.md` (SHA-256 12a2a6f4cc832a5070e414eaf5be145ca16ef41f8004672267707b7ade3859ec). There is no numerical/physical-q instance, program, external source, false f198 estimate, held/ZERO input or novelty claim.

## 1. Claim and original-target consequence

For every rank-two orthogonal projector `P` on `C4⊗C4`,

**`P^Γ⪰0` iff `P/2` is separable**,  (1.1)

where `Γ` denotes partial transpose in either local factor. The reverse implication is immediate: the partial transpose of a product projector is a product projector.

The named separable-projector proof consequently pays the full original T2 dual gap for **every PPT rank-two P** and arbitrary traceless complex `A,B`. If both local factors are nonnormal, that proof gives strict gap. Hence any unrestricted T2 failure would require an **NPT rank-two test projector**. This is a necessary condition on the test projector, not an assertion that an NPT projector, a physical state, or a counterexample exists. The NPT interior, f274 optimized-certificate comparison, T2/T3/Z2/q3 and novelty remain open.

## 2. A PPT kernel identity and local support rank

Write the rank-two projector as `P=|ψ1⟩⟨ψ1|+|ψ2⟩⟨ψ2|` with orthonormal `ψ1,ψ2`. Suppose `P^Γ⪰0`. For `x,z` in the first local space and `y,w` in the second, expansion in a product basis gives

`⟨x⊗conjugate(y), P^Γ(z⊗conjugate(w))⟩`

`= Σ_{k=1}² ⟨x⊗w,ψ_k⟩ conjugate(⟨z⊗y,ψ_k⟩)`.  (2.1)

If `x⊗y∈ker P`, then the diagonal value on the left with `z=x,w=y` is zero. Positivity of `P^Γ` implies `x⊗conjugate(y)∈ker P^Γ`; hence the right side of (2.1) vanishes for all `z,w`.

For each `x`, put `u_k(x)=(⟨x|⊗I)ψ_k` in the second local space. If there is an `x` for which `u1(x),u2(x)` are linearly independent, choose any `y` orthogonal to both. Then `x⊗y∈ker P`, and varying `w` in (2.1) isolates the two coefficients. Thus `⟨z⊗y,ψ_k⟩=0` for both `k` and every `z`. Since this holds for every `y⊥span{u1(x),u2(x)}`, the **entire** second-local support of both `ψ1,ψ2` lies in that two-dimensional span.

If instead `u1(x),u2(x)` are dependent for **every** `x`, regard them as two linear maps of `conjugate(x)`. The following elementary fact applies: if linear maps `S,T` have `Sx,Tx` dependent for all `x`, then either `T=λS`, or their combined ranges are one-dimensional. Indeed, when `rank S≥2`, compare `x,y,x+y` with independent `Sx,Sy`, and then compare arbitrary vectors and `ker S`, to obtain one common scalar; when `rank S=1`, compare `x0+t z` with `z∈ker S` to force `T` into the same one-dimensional range. The proportional alternative contradicts linear independence of `ψ1,ψ2`; hence both share one second-local factor and `P` is separable.

Partial transposition in the *other* local factor is also positive, since it is the full transpose of `P^Γ`. Repeating the argument with factors exchanged shows: unless `P` is already a common-factor product projector, both local supports have dimension at most two. Restrict to those supports and identify them with `C2⊗C2`; the inherited partial transpose remains positive.

## 3. Completion in 2×2

Let `S=range P` be a two-dimensional subspace of `C2⊗C2`. Identify its vectors with 2×2 coefficient matrices `U,V`. The homogeneous quadratic `det(sU+tV)` either vanishes identically or has one or two projective roots over `C`. Its roots are precisely the product rays in `S`.

If it vanishes identically, every vector in `S` is product. Two independent product vectors must then share a local factor, since otherwise their sum has Schmidt rank two. Thus `P` is a common-factor separable projector.

Suppose there is exactly one product ray. It must be a double root. Local unitaries take it to `|00⟩`; choose a unit `w∈S` orthogonal to `|00⟩`. Write `w=a|01⟩+b|10⟩+c|11⟩`. The determinant polynomial is `st c−t²ab`; a unique double root at `t=0` forces `c=0` and `ab≠0`. As `P=|00⟩⟨00|+|w⟩⟨w|`, the partial transpose has on `span{|00⟩,|11⟩}` the principal block

`[[1, a conjugate(b)],[conjugate(a)b,0]]`,

whose determinant is `−|ab|²<0`, contradicting positivity. Thus the one-ray case is impossible.

Finally suppose there are two product rays. If their first or second local factors are parallel, the span has a common local factor and is separable. Otherwise the two local pairs are independent. Invertible local filters map the rays to `|00⟩` and `|11⟩`. The filtered positive operator has support in their span and so is

`α|00⟩⟨00|+β|11⟩⟨11|+γ|00⟩⟨11|+conjugate(γ)|11⟩⟨00|`.

PPT is preserved by local filtering: `[(F_A⊗F_B)P(F_A⊗F_B)†]^Γ=(F_A⊗conjugate(F_B))P^Γ(F_A⊗conjugate(F_B))†`. In the filtered partial transpose, the principal block on `|01⟩,|10⟩` is `[[0,γ],[conjugate(γ),0]]`. Positivity forces `γ=0`. The filtered operator is a positive sum of two product projectors, and the inverse local filters preserve separability. This completes `P^Γ⪰0 ⇒ P/2` separable and hence proves (1.1).

## 4. T2 boundary and nonclaims

Under the named UNREVIEWED all-separable-projector theorem, (1.1) immediately proves the full original dual bound for every PPT rank-two test projector, strictly whenever both local factors are nonnormal. The only unpaid test-projector domain in this reduction is NPT `P`.

No statement is made that an NPT projector produces a T2 failure, that a physical quantum state is distillable, that any optimized f274 `η>2L` exists, or that unrestricted T2/T3/Z2/q3, source correctness, execution, formal/kernel, stronger-family/human review or novelty is settled. Disjoint written review should check the PPT kernel identity, two-linear-map lemma, 2×2 double-root and filtering cases, and the separately frozen separable-projector prerequisite. Earlier packet bytes, review scopes, and STOP/HOLD/ZERO restrictions remain unchanged.
