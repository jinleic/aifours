# An explicit finite zero-resolution act for the two-J-class fixed-q problem

**NEW AUTHOR WRITTEN construction/criterion, UNREVIEWED / UNADOPTED.** This replaces an unspecified globalization by a finite right-act congruence in a restricted two-layer host form. It does NOT prove that the congruence preserves real points in every RRL source. It does not repair f164's arbitrary-actor transport, invoke Fact1, establish canonical freeness, or close Q1/Q2.

## 1. Input and the upper skeleton

Let S=T ⊔ K be finite regular with T its maximal J-class and K a completely simple ideal. T need not be closed. Let q:S→D=M[G;I,Λ;P] be specified, onto and idempotent pure. Use the directly constructed normal-band skeleton A^0 of `frontier-20261029-maximal-J-fixed-q-skeleton-v1.md` (SHA 5a5f854daefe67c9b2c520007616353ee6ed297f16060962b1063a86eb666571). Its nonzero part A is a disjoint union of rectangular components A_γ=R_γ×C_γ. Products within one component are rectangular; products between components are the zero being resolved. Write c_A(x) for the column of x and γ(x) for its component. The specified upper coefficient is b(t)∈A for t∈T. It obeys the source coefficient equation whenever st∈T, and the twisted upper factors have different components exactly when st∈K.

The real points are W=G×ColK, with K-columns and action c·t as in the closed-CS-top theorem. Put κ(k)=(g_k,c_K(k)). G acts on W by left multiplication of its group label.

## 2. A finite RIGHTSN band before any source relations

Define a disjoint bottom set Ω0 containing:

- real points w∈W;
- formal acted points F(w,x) for w∈W,x∈A;
- reset points C(ξ,y) for ξ∈C_γ, y∈A_δ with γ≠δ.

The right action of a top element x on these points is:

`w·x=F(w,x)`;

`F(w,z)·x=F(w,zx)` if γ(z)=γ(x), and `C(c_A(z),x)` otherwise;

`C(ξ,z)·x=C(ξ,zx)` if γ(z)=γ(x), and `C(c_A(z),x)` otherwise.

Here zx in the same-component branches is the rectangular product in A. Set B0=A ⊔ Ω0. Make Ω0 right zero and set xπ=π for top x and bottom π. For x,y∈A define their product to be the rectangular product if they have the same component, and C(c_A(x),y) otherwise.

**Associativity.** For three top factors, if adjacent component labels both agree, use rectangular associativity. If only the first junction changes, both bracketings give C(c_A(x),yz); if the second junction changes, both give C(c_A(y),z), using c_A(xy)=c_A(y) when the first junction stays in one component. For a bottom point π followed by x,y in one component, the displayed action rules give (πx)y=π(xy). When x,y have different components, the action rules reset (πx)y to C(c_A(x),y), independently of π, exactly π(xy). All other cases follow from right-zero multiplication and top-left absorption.

Every element is idempotent. For x∈A, xB0x consists of x and bottom points fixed on the right by x, a right-zero band with identity x adjoined. For π∈Ω0, πB0π={π}. Thus B0 is RIGHTSN. The G-action on W and A extends to F(w,x) and C(ξ,y) coordinatewise, giving band automorphisms.

The reset point forgets the first factor's row for a necessary algebraic reason: if x,x′ have the same top column and y is in another component, choose z in their component with zx′=x. In any right-zero-bottom extension, xy=(zx′)y=z(x′y)=x′y. No such forgetting of the second factor's row was made.

## 3. The source relations are an explicit act congruence

Let θ be the least equivalence on Ω0 closed under right multiplication by A and the G-action, containing the following relations.

**K–T relations.** For w=(m,c), t∈T put a=m p_(μ(c),i_t). Impose

`F(w,^a b(t))  θ  (a g_t,c·t)`.

**T–T drops.** For s,t∈T with st∈K, and every a∈G, put

`x=^a b(s)`, `y=^(a w(s,t)) b(t)`.

These have different components by the skeleton lemma. Impose

`C(c_A(x),y)  θ  ^a κ(st)`.

Because Ω0 is right zero, top elements absorb it on the left and bottom multiplication on the right returns the right factor, an equivalence on Ω0 closed under the stated right actions is exactly what is needed for a band congruence that leaves the top untouched. G-closure makes the quotient action well defined. Thus B=B0/θ is RIGHTSN.

Define β(t)=b(t) for t∈T and β(k)=[κ(k)] for k∈K. Every source coefficient equation holds:

- T–T products staying in T use the upper skeleton;
- T–T products dropping to K are imposed above;
- K–T products are imposed above;
- S–K products are automatic because the bottom is right zero, left multiplication preserves a K-column, and g_(sk)=w(s,k)g_k.

Therefore s↦(β(s),q(s)) is always a homomorphism into the explicit same-q physical product. It separates the maximal T-layer. **If W→Ω0/θ is injective**, it also separates every same-fibre R-related idempotent pair in K, since distinct such idempotents have different K-columns. This is a sufficient exact criterion, not an assertion that injectivity always holds.

For finite input, the construction is finite:

`|Ω0|=|W|+|W||A|+sum_(γ≠δ) |C_γ||A_δ|`.

One computes θ by union-find closure under the finitely many right actions and G-generators. No SAT solver or scientific optimization is needed.

This construction is universal only among right-zero-bottom extensions of this prescribed upper skeleton with the prescribed real-point/source relations: send F(w,x) to the product wx and C(c_A(x),y) to xy. It is not identified with an unrestricted canonical RIGHTSN host. A collision would invalidate this restricted construction's separation; it is not automatically a no-host certificate for the original problem.

## 4. Exact S45 reconstruction

`frontier-20261029-two-layer-zero-resolution-checker-v1.py`, SHA 5cfcf964b92a2ed053c364bd542997c6e8ad125e97c7b3a8cc7a161f4b677782, ran with python3.14 at Thu Oct 29 09:46:24 PDT 2026, exit 0.

For S45 over its natural actor the upper A has 18 elements, W has 12 distinct real points, and Ω0 has 282 formal points. The act congruence performs 234 identifications and leaves 48 bottom classes. No two real points merge. The resulting band has 66 elements and separates all nine same-fibre R-idempotent pairs. The checker exhausts its associativity and RIGHTSN identity, the C2 automorphism and every source-host equation.

It additionally constructs a literal equivariant quotient map from the stored 306-element band onto this 66-element band, checks all 93,636 products, all action equations and all source coordinates, and checks surjectivity. This uses only the stored tables, not their claimed canonical freeness. The bottom-column count 48 agrees with the earlier analysis of that stored band's minimal rectangular class; the new quotient removes its row multiplicity.

The remaining two-layer gap is now explicit: prove W-injectivity for θ under suitable source hypotheses (in particular the RRL hypothesis), or exhibit a collision and determine whether it reflects only the prescribed skeleton/right-zero restriction. No all-source W-injectivity proof is supplied here.
