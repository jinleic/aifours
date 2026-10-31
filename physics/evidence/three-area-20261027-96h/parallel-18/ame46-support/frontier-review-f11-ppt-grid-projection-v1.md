# f11 — full scientific review of the 4×5 grid-state projection claims

Reviewer **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:20:18 PDT 2026`**; not an exact creation/completion/runtime clock. **Same-harness written reconstruction plus independently implemented exact checks; not formal/kernel, independent-model-family or novelty acceptance.**

## 1. Exact verdict, source warning and inputs

**Candidate verdict: NO SUBSTANTIVE DEFECT AT THE EXACT PROJECTED-RANGE SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR against the two candidates.** The arbitrary complex 5→4 projection, the well-defined inherited functional, explicit rank-two construction in all parameter cases, and spanning consequence reconstruct below.

**Separate SOURCE-WARNING S1:** the cited published arXiv v1 contains an incorrect displayed polynomial identity in its proof of the original 4×5 range criterion. I independently checked the printed generators and found an explicit corrected identity. The candidates do NOT rely on the erroneous identity for their universal projected-range construction; the original source's *pointwise rank≤2 consequence* still follows from the corrected identity. This source issue is reported in §7, not hidden inside the 0/0/0 candidate count, and is NOT a counterexample to the source theorem or a new 4×4 witness.

Complete assignment was read FIRST, SHA256 `878a7543f96ac632f64ce1bd0dab8384fcc66d81ac53a60a1d6df1677ae4487d`; both candidate files read completely and hashes observed:

- `frontier-20261028-grid-projection-full-span-v1.json`, **34 LF**, SHA256 `3cebc491cbdb653506dbb138c3b3b417988ae17396ef14bc636b187e84526213` — cited as **F**.
- `frontier-20261028-grid-projection-obstruction-v1.json`, **37 LF**, SHA256 `8d72e6ecdf0eb6a01fcddfb0c75eda3272847883f575c1dbd31bee5b40942c84` — cited as **O**.

I read the registered target `written-releases/physics-3-ppt-sn3-definitions-v1.md` SHA256 `eecd40e6e864ac0e13212543ffb2916a9799f7457dc9cd7c35b6537316ceaceb`, and the cited primary source [Krebs–Gachechiladze, arXiv:2509.07086v1, Eq. (11), Eq. (12), Theorem 5](https://arxiv.org/html/2509.07086v1) directly. The later source mentioned at O LF13 is not a load-bearing premise; I did NOT independently establish its status/novelty implication. The authors' finite search/code results are not imported as my check.

Prior exposure: I have earlier cross-domain PPT/review contacts and my own ongoing AME work; this is not a blind or independent-family certificate. Historical quarantined outcomes are not premises. No author was contacted; no held proof, external-model/paid API, nested agent, Git, deletion or publication was used.

## 2. Published actual range and physical projection caller

The source's Eq. (11) gives the SAME 4×5 coefficient-matrix range

`M(a,b,c,d,e,f,g,i,h) = [[a,b,c,0,h], [d,a,b,0,0], [e,-d,a,f,0], [g,0,i,e,c]]`.

These nine coordinates are independent: each can be read from an explicitly occupied matrix entry. The Schmidt rank of the associated complex bipartite vector is the ordinary matrix rank. The paper declares this matrix family to be the actual range of its published 4×5 PSD state; the source-range identification, not a newly reconstructed full grid-state density matrix, is the named primary-source input.

For an arbitrary complex local linear map `K:C^5→C^4` of rank4, the coefficient convention gives `M→M K^T`; set `P=K^T∈C^(5×4)`. Its image H is a 4-dimensional subspace, so there exists a nonzero COMPLEX **row covector** `s=(u,v,w,x,y)` with `H=ker(s)`. No conjugation of s is assumed; the physical adjoints in the PSD state are separate from this algebraic right multiplication.

For PSD `rho`, write `rho=R R*` with `range(R)=range(rho)`. Then `range(A rho A*)=range((A R)(A R)*)=range(A R)=A range(rho)` for `A=I⊗K`. Thus `S P` is exactly the projected state's actual range, not merely a relaxation. A rank-four K and the constructed nonzero projected vector below make the projected state nonzero; it can be normalized. The source state is PPT, and the local filter preserves PPT by conjugation of the partial transpose with the conjugate local operator. None of this determines its projected Schmidt number.

## 3. The inherited diagonal functional is well-defined

Suppose `M P=M' P`; put `D=M-M'∈S`. Every row of D annihilates H, hence is a scalar multiple of s. Therefore `rank(D)≤1` even if D=0. Denote its first five parameters again by `a,b,c,d,e`. Its two 2×2 minors are

`det D[{0,1},{0,1}]=a²-bd`,

`det D[{1,2},{1,2}]=a²+bd`.

Both vanish, hence `2a²=0`, so `a=0` over C. Therefore

`L_H(MP):=a(M)`

is a well-defined LINEAR functional on the entire projected range, independent of the chosen preimage. It is not claimed to be literally the same coordinate entry after arbitrary P. In the original range the paper's `|e*> = |00>+|11>+|22>` has overlap `3a`, so the `a` functional is its diagonal range functional up to a nonzero scalar.

## 4. Universal rank-two vector, first three covector coordinates nonzero

Assume `(u,v,w)≠(0,0,0)`. Choose nonzero `α,β,γ` with

`α w − γ u = β(v−β)`.                                                                  (A)

Existence over ALL complex parameters is explicit:

- If `(u,w)≠(0,0)`, choose `β≠0,v`. The right side is nonzero. If only u or only w is nonzero, solve for γ or α respectively and choose the other freely nonzero. If both are nonzero, solving the linear equation leaves a free parameter; avoid the finitely many values making α or γ zero.
- If `u=w=0`, then v≠0. Choose `β=v`, `α=γ=1`; (A) holds.

Set

`a=1`, `b=(w−γ)/β`, `d=(u−α)/β`, `f=x/γ`, `h=y/α`, `c=e=g=i=0`.

The nonzero rows are

`r0=(1,b,0,0,h)`, `r1=(d,1,b,0,0)`, `r2=(0,−d,1,f,0)`.

Their leading 3×3 determinant is `(1+bd)−bd=1`, so M has rank3. Direct componentwise substitution gives

`α r0+β r1+γ r2 = (u, αb+β−γd, βb+γ, γf, αh) = (u,v,w,x,y)=s`.

The middle equality uses (A); no selected normal, realness or generic denominator was assumed. The restriction map from rowspace(M) to H has one-dimensional kernel `span(s)` because s is in it. Consequently `rank(MP)=3−1=2` and `L_H(MP)=a=1`. This reconstructs F LF11–12 and O LF17–22.

## 5. Universal rank-two vector when only the last two covector coordinates remain

Assume `u=v=w=0`, so `(x,y)≠(0,0)`. Set `a=1,c=y,e=x,f=g=i=h=0`.

- If `x≠0`, choose `d=0` and any complex square root `b²=(xy−1)/x`.
- If `x=0`, then y≠0; choose `b=0` and a complex square root `d²=1/y`.

The first three rows have support in columns0–2 and leading determinant

`1+b² x−y d²−x y=0`.

The leading 2×2 minor is `1−bd=1` in EITHER branch, so those rows have rank exactly2, including zero-root boundary cases. The fourth row is `s=(0,0,0,x,y)`, nonzero and supported entirely on columns3–4, hence independent of the first three. Thus `rank(M)=3`, s lies in its rowspace, and the same restriction argument gives `rank(MP)=2`, with `L_H(MP)=1`. This reconstructs F LF13 and O LF23–27 for arbitrary complex normals, not just the finite controls.

## 6. Entire projected range is spanned by its own rank≤2 vectors

Let B_a,…,B_h be the nine source coordinate matrices, with i treated as the named parameter, not the imaginary unit. Direct inspection gives

`rank(B_a)=3`; `rank(B_b)=rank(B_c)=rank(B_d)=rank(B_e)=2`; and `rank(B_f)=rank(B_g)=rank(B_i)=rank(B_h)=1`.

Right multiplication by P cannot increase rank. For the constructed M0 with `a=1`, every source matrix decomposes exactly as

`M = a(M) M0 + sum_(j≠a) [parameter_j(M)−a(M) parameter_j(M0)] B_j`.

After multiplying by P, the spanning list consists of the projected M0, rank exactly2, plus the eight projected B_j, each rank≤2 (including possible zero vectors). All nine are in the same actual projected range. Thus **every vector in SP is a complex linear combination of rank≤2 vectors in SP**, for EVERY rank4 complex P. This reconstructs F LF10–14 independently.

As a result, no linear functional on SP can vanish on all its rank≤2 vectors while being nonzero somewhere on SP: vanishing on a spanning set forces it to vanish on all of SP. In particular the inherited `L_H` is nonzero on M0P, directly refuting the original diagonal-functional range argument after every such projection. This is the precise sense of “no range-annihilator certificate.”

**Important non-converse:** a range being linearly spanned by SR≤2 vectors does NOT itself provide a positive decomposition of the projected density operator into SR≤2 projectors. No SN≤2 assertion, 4×4 PPT/SN≥3 witness, global no-go, or obstruction to all OTHER inequality separators follows.

## 7. SOURCE-WARNING S1 — published Eq. (12) identity, with an explicit repair

The source gives five 3×3 minors (write `a=psi00,b=psi01,c=psi02,d=psi10,e=psi20`):

`g1=e(a²−bd)`, `g2=c(a²+bd)`, `g3=e(b²−ac)`, `g4=−c(d²+ae)`,

`g5=a³+b²e−d²c−ace`.

The paper's displayed prose at [arXiv v1, immediately after Eq. (12)](https://arxiv.org/html/2509.07086v1) says

`a(g5−g3−g4)−c g1+e g2 = a⁴`.

Direct exact polynomial expansion instead gives

`[a(g5−g3−g4)−c g1+e g2]−a⁴ = c e (a²+2bd)`.

The all-ones algebraic control has LHS4, RHS1. It does NOT satisfy all g_i=0 and is NOT a rank≤2 counterexample. The error is in the printed polynomial identity, not an inferred failure of the source's range claim.

An exact integer-polynomial replacement is

`2a(g5−g3−g4)−c g1−e g2 = 2a⁴`.                                                   (B)

Its residual is identically zero over `Z[a,b,c,d,e]`. Each g_i is indeed a 3×3 minor of the displayed M: respectively row/column sets `(013,013)`, `(123,124)`, `(013,123)`, `(123,014)`, `(012,012)`, with zero-based labels. Thus rank(M)≤2 makes all five vanish, and (B) gives `a=0` over C. This independently pays the cited source's operative diagonal-functional conclusion WITHOUT relying on its false printed identity or on the Nullstellensatz.

The same conclusion can also be obtained pointwise: for a≠0, if c=e=0 then g5=a³≠0; if only e is nonzero then g3 forces b=0 and g1≠0; if only c is nonzero then g4 forces d=0 and g2≠0; if both are nonzero then g1,g2 force bd=a² and bd=−a², impossible over C. This covers every complex case. Neither reconstruction claims the entire paper, its global source status, or novelty has been audited.

## 8. Checks actually performed

1. Independent reviewer-written `frontier-20261028-f11-independent-check-v1.py`, SHA256 `3fd90068f914ee39ba094c115e8bf5cce25200610aac04b610278779f8a41114`, executed as `python3 -B frontier-20261028-f11-independent-check-v1.py frontier-20261028-f11-independent-check-v1.json`. Receipt SHA256 `d5a59b0ac6a3ef654aab65f563b3d7bbaa690efa0dcc657b4fb793f58fddc67b`. Exact `Fraction`-component Q(i) elimination checked the nine basis ranks `(3,2,2,2,2,1,1,1,1)` and NINE projection normals, including both zero-coordinate branches, genuinely complex normals and a complex square-root case. For each: P rank4, M0 rank3, M0P rank2, the eight images rank≤2, and constructed span dimension equals full projected-range dimension. Observed range dimensions were8 or9 in those controls. The finite samples do not prove the universal claim; §§3–6 give its written argument.
2. `frontier-20261028-f11-source-identity-check-v1.py`, SHA256 `716d838331718bd140c70c44da5679250d9128b73a6a72bfd81cc8667aedf190`, executed with new output `frontier-20261028-f11-source-identity-check-v1.json`, SHA256 `1a55e8a6f54bb54af053bc307aab4878b99bd3db27f581d2017122821d41e1f3`. Exact integer-polynomial expansion returned residual `ce(a²+2bd)` and the 4-versus-1 control above.
3. `frontier-20261028-f11-source-corrected-identity-v1.py`, SHA256 `0cb6902dd03be3a0e05bf84ac1653018f691cad72101d60d025d79f0a4c63458`, executed using the prior polynomial-ring implementation and new output `frontier-20261028-f11-source-corrected-identity-v1.json`, SHA256 `7d4f387f18e13a252cf123b38912d71bfa45e8629659d727859a7324c25c73d1`. The replacement identity's integer-polynomial residual was empty/zero. These two symbolic checks share the same simple polynomial-ring operations; they are not two independent formal verifiers.

The author's bounded search counts at F LF15–31 and O LF29–35 are author-reported and NOT rerun or independently certified here. Their absence is not a mathematical gap in the universal written construction above. The test controls and source warning do not settle 4×4 Schmidt number or source priority.

## 9. Final scope

Supported here: the exact **universal projected-range span** and **inherited-functional obstruction** for this one published 4×5 grid-state range, for every rank-four complex map on its five-dimensional local factor. The source's printed identity needs the explicit correction in §7; the repaired pointwise implication is independently demonstrated.

Not shown: any 4×4 SN≥3 PPT state, any globally valid SR2-positive separating operator for such a state, SN≤2 of the projected state, the impossibility of every other 4×4 construction, global all-PPT SN≤2, source-wide novelty or a peer-reviewed/formal/kernel/cross-family certificate. Prior historical quarantine findings remain historical; none was used as a validated mathematical premise. The reviewer will resume the original AME research after returning this duty.
