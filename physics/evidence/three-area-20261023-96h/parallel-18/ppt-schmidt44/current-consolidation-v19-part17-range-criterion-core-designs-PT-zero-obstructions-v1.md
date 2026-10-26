# CURRENT P44 CONSOLIDATION v19 — PART17/17: range-criterion certificates with a Schmidt-rank-four core in 4x4: normal form, a partial-transpose kernel lemma, and impossibility for three natural design families

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 00:26:26 PDT 2026**. Exact WRITTEN linear algebra with one named import (KCKL Lemma 5, already quoted in Part12 L1/I5). No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## K0. Why this route, scope, union

The only known SN3 PPT certificate in small dimension, for the 4x5 state of 2509.07086 (Theorem 5), is the **range criterion**: every Schmidt-rank<=2 vector of the range lies in a hyperplane (the coefficient psi00 vanishes), while the range is not contained in it. Part17 asks whether the same mechanism can certify a 4x4 PPT state. It gives:
- a normal form;
- a new obstruction lemma;
- impossibility for three natural families.

It does NOT prove that the range criterion never works in 4x4 and does NOT solve P44.

The complete current union is the sixteen parts plus ADDENDUM-1 bound in `checkpoint-096-complete-current-v18-sixteen-part-manifest-v1.json` (SHA256 1221cdb1ab35ff2098e806ba2bf2f346db8cea2ba6560e9044dc2c61fda90631), THIS part, and all mandatory overlays. Parts 9–17 are LATER UNREVIEWED.

Notation. Ω=Σ_k|kk> (unnormalized). Every vector of C^4⊗C^4 is (A⊗1)Ω for a unique 4x4 matrix A, and its Schmidt rank is rank(A). E_ij are matrix units. For a range R we write R=span{(A⊗1)Ω : A in V} with V a space of matrices.

## K1. Normal form

**Lemma K1.** Let R be the range of a 4x4 state ρ. Suppose all SR<=2 vectors of R lie in a hyperplane H of R, and some vector of R outside H has Schmidt rank 4. Then, after an invertible local filter (which preserves PPT and SN), the following hold.
1. R = C·Ω ⊕ {(B⊗1)Ω : B in N} for a subspace N.
2. N has **property (P)**: no B in N has a nonzero eigenvalue of geometric multiplicity >=2.
3. Conversely, if N has (P), every SR<=2 vector of C·Ω⊕N lies in N. Any state with exactly this range then has SN>=3, by the range criterion: a Schmidt-rank-<=2 decomposition would place its range inside N.

*Proof.* Let v0 ∉ H have Schmidt rank 4, so v0=(A0⊗1)Ω with A0 invertible. The local filter A0^{-1}⊗1 maps v0 to Ω, and R=C·v0⊕H maps to C·Ω⊕N. For c0!=0, (c0·1+B)⊗1 Ω ∉ N has Schmidt rank rank(c0+B)>=3 by hypothesis. That is exactly (P), since rank(B-λ)<=2 for some λ!=0 means geometric multiplicity >=2. The converse reverses this. ∎

By Part12 C31 a PPT witness needs rank(ρ)>=6, so dim N>=5. Property (P) is non-generic. For a generic 5-dimensional N, the projectivization P(N)=P^4 meets the 12-dimensional closure of {B : ∃λ, rank(B-λ)<=2} (inside P^15) in at least a curve. It meets the 11-dimensional rank-<=2 locus in only finitely many points. So (P) requires special structure.

## K2. The partial-transpose kernel lemma

**Lemma K2.** Let ρ be PPT and x,y unit vectors in C^4 with x⊗conj(y) ∈ ker ρ. Then

`(1⊗<conj y|) ρ (|x>⊗1) = 0,  i.e.  <x'⊗conj(y)|ρ|x⊗z> = 0 for all x', z.`

In particular, if x⊥y, then <x⊗conj(x)|ρ|y⊗conj(y)> = 0.

*Proof.* By KCKL Lemma 5 (Part12 I5), x⊗y ∈ ker ρ^Γ. In the computational Bob basis, <a⊗b|ρ^Γ|c⊗d> = <a⊗conj(d)|ρ|c⊗conj(b)>. Hence 0 = <x'⊗y'|ρ^Γ|x⊗y> = <x'⊗conj(y)|ρ|x⊗conj(y')> for all x',y'. Take x'=y and y'=x for the special case, after a Hermitian conjugation. ∎

For R=C·Ω⊕N, the vector x⊗conj(y) is orthogonal to R iff <x|y>=0 and <x|B|y>=0 for all B in N, since <x⊗conj y|(A⊗1)Ω> = <x|A|y>.

Write ρ=Σ_k r_k r_k* with {r_k} spanning R. The form Q(L,L')=Σ_k L(r_k)conj(L'(r_k)) is then **positive definite** on linear functionals restricted to R. Lemma K2 becomes the statement Q(L_{x'⊗conj y}, L_{x⊗z}) = 0 for all x', z, where L_w(r)=<w|r>.

**Corollary K3 (diagonal pair).** Suppose x⊥y with <x|B|y> = <x|B|x> = <y|B|y> = 0 for all B in N. Then no PPT state has range C·Ω⊕N.

*Proof.* Lemma K2 gives Q(L_{xx̄}, L_{yȳ}) = 0. On R these functionals read L_{xx̄}((c0+B)⊗1Ω) = c0 + <x|B|x> = c0, and likewise L_{yȳ} = c0. So Q(c0,c0) = 0, contradicting positive definiteness, because c0 (the Ω-coordinate) is nonzero on R. ∎

## K3. Three design families with property (P), all impossible for PPT states

**Family F1: a nilpotent 3x3 compression.** Suppose some 3-dimensional W has P_W N P_W simultaneously strictly upper-triangular in an orthonormal basis w1,w2,w3 of W.
- **(P) holds.** For λ!=0, the compression P_W(B-λ)P_W = (P_W B P_W) - λ·1_W is invertible on W, so rank(B-λ)>=3.
- **No PPT state.** x=w3, y=w2 is a diagonal pair: <w3|B|w2> is a strictly-lower entry and <w2|B|w2>=<w3|B|w3> are diagonal entries, all zero. Corollary K3 applies.

F1 contains three subfamilies:
- every strictly upper-triangular N, up to U⊗conj(U), which fixes Ω;
- the 10-dimensional N10={B : the {1,2,3}-block of B is strictly upper-triangular};
- its 5-dimensional non-nilpotent, non-triangularizable member N5=span{E00,E01,E12,E23,E30}. As a check, it gives R=span{|11>+|22>+|33>, |00>,|01>,|12>,|23>,|30>}, where <21|ρ|21>=0 forces <22|ρ|11>=G_11=0.

**Family F2: Weyl "diagonal plus diagonal-times-shift".** Take Z=diag(1,i,-1,-i), X|n>=|n+1> (mod 4) and N_W={aZ+DX : a in C, D diagonal}=span{Z,X,ZX,Z^2X,Z^3X}. This is 5-dimensional, so R=span of six Weyl Bell states Ω_(a,b)=(Z^aX^b⊗1)Ω with (a,b) in {(0,0),(1,0),(0,1),(1,1),(2,1),(3,1)}.

**(P) holds.** The matrix B-λ = (aZ-λ) + DX is diagonal plus diagonal-times-cyclic-shift. In the permutation expansion only the identity and the 4-cycle survive, so det(B-λ) = Π_m(aω^m-λ) - Π_m D_m = λ^4 - a^4 - Π_m D_m. Every nonzero eigenvalue is a simple fourth root. So for any state with this range, SN>=3 follows from the range criterion. **This family has NO diagonal pair:**
- The diagonal conditions <x|DX|x>=0 for all D force x to have no two cyclically adjacent nonzero entries; with <x|Z|x>=0 this gives x ∝ |0>+e^{iα}|2> or |1>+e^{iα}|3>. The same holds for y.
- If x,y have the same support type, orthogonality forces y=Zx up to a scalar, so <x|Z|y>!=0.
- If they have different types, some conj(x_{n+1})y_n!=0.

So Corollary K3 does not apply, and the full Lemma K2 is needed.

**F2 has no PPT state.**
- *Support.* Every r in R is supported on |ii> (coefficient u_i(r)=(c0+c1ω^i)/2) and on |i+1,i> (coefficient v_{i+1}(r)). For each m and j in {m+1,m+2}, |m⊗j> is orthogonal to R, since Alice-Bob ≡ -1 or -2 is not in the support.
- *Lemma K2 with x=|m>, conj(y)=|j>.* It gives Q(L_{a,j}, L_{m,b})=0 for all a,b. The nonzero functionals involved are L_{j,j}=u_j and L_{j+1,j}=v_{j+1} on the left, and L_{m,m}=u_m and L_{m,m-1}=v_m on the right. Hence u_m ⊥_Q u_{m+1} and u_m ⊥_Q u_{m+2} for every m.
- *Contradiction.* All four u_i are pairwise Q-orthogonal and nonzero. But they lie in the 2-dimensional span of the coordinate functionals c0,c1, which is impossible for a positive definite Q. ∎

In particular no Bell-diagonal state with this support is PPT. A direct check agrees: the t=1 partial-transpose block has zero diagonal at x=0 but entry p00+p10ω^{-1}!=0.

## K4. What is and is not established

**Established, author-WRITTEN:**
- the normal form K1;
- the kernel lemma K2 and Corollary K3;
- impossibility of PPT states for the whole family F1, including all triangular-nilpotent and N10-type cores, and for the Weyl family F2.

So the 4x5 mechanism does not transfer to 4x4 through any of these natural cores, nor through the simplest Z4 Bell-diagonal six-state support with property (P).

**NOT established:**
- that every 4x4 property-(P) core of dimension >=5 is PPT-infeasible (stated here only as an OPEN question);
- range certificates whose outside vectors all have Schmidt rank 3 (singular-space ranges, which reduce to 3x4/4x3 supports);
- anything about SN3 states not certified by the range criterion.

No novelty or priority claim. The KCKL import is used at its quoted statement only.

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v19 PART17/17.**
