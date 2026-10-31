# Canonical row/column idempotent-band obstructions for generalized Q2

**Status: NEW AUTHOR WRITTEN universal necessary theorem with exact finite applications; UNREVIEWED / UNADOPTED.** It applies to embeddings in idempotent-separating images of physical products. It does NOT characterize the largest regular class, prove originalQ1, or exclude the original fullSN band scope.

## 1. Rows and columns DO descend through an idempotent-separating image

Let `π:H=P(B,D)→U` be onto idempotent-separating, `D=M[G;I,Λ;P]`, with group action α. H is regular: for `x=(b,(i,g,λ))`, put p=P_(λ,i), w=gp and

`x*=(α_(w⁻¹)(b),(i,p⁻¹g⁻¹p⁻¹,λ))`.

Then xx*=(b,(i,p⁻¹,λ)) and x*x=(α_(w⁻¹)(b),(i,p⁻¹,λ)); multiplying once more gives xx*x=x and x*xx*=x*. The sole named structural import below is the standard fact that an idempotent-separating congruence on a regular semigroup is over groups, stated explicitly in Szendrei's 2019 survey §2, <https://arxiv.org/html/1909.05280v1>.

If π(x)=π(y), choose u inverse to x. The elements xu and ux are idempotent. Since π(yu)=π(xu), yu lies in the GROUP congruence class with identity xu. Its actor therefore lies in the same CS cell as the actor of xu. CS multiplication preserves left rows, so `row(y)=row(yu)=row(xu)=row(x)`. Applying the same argument to uy and ux gives `col(y)=col(x)`. Thus the host row/column homomorphisms induce homomorphisms `U→LZ_I`, `U→RZ_Λ`. The WHOLE GROUP COORDINATE need not descend; that stronger assertion is neither used nor true.

For ANY semigroup S embedded in U, define canonical source relations

`R=equiv{(s,st):s,t∈S}`, `C=equiv{(t,st):s,t∈S}`.

S/R is leftzero and S/C rightzero; the source maps are universal for such homomorphisms. Their pair `ρ_rect:S→(S/R)×(S/C)` is onto the full rectangular band, because the product of any representative of a chosen row with any representative of a chosen column realizes that cell. Hence all source elements in one canonical R-class have ONE actual host row, and similarly for C. This construction uses ALL source products, not just idempotent comparability.

## 2. Exact necessary source bands and gauges

Let B belong to a band variety V and let S be as above. Idempotents have unique idempotent lifts: existence by xzx with z inverse to x², uniqueness by idempotent separation. Write an idempotent lift as `(b_e,(i_e,P_(λ_e,i_e)⁻¹,λ_e))`.

- For a fixed canonical R-class, all i_e equal some i. Products of two lifts have identity group weight, actor equal to the RIGHT factor's actor, and coefficient b_e b_f. Thus its ENTIRE source idempotent set is a band embedded by `e↦(b_e,λ_e)` in `B×RZ_Λ`. It belongs to `V∨RZ`.
- For a fixed canonical C-class, all λ_e equal some λ. Put p_i=P_(λ,i). The normalized coefficient `c_e=α_(p_(i_e))(b_e)` gives `c_(ef)=c_e c_f`, since the original weight is `p_(i_e)⁻¹p_(i_f)`. The actor row is retained from the LEFT factor. Thus its entire source idempotent set embeds by `e↦(i_e,c_e)` in `LZ_I×B`, and belongs to `LZ∨V`.
- In a canonical RECTANGULAR cell, both actual actor row and column are fixed, hence the idempotent actor itself is fixed. The coefficient map directly embeds the entire idempotent cell into B, so that cell is a band in V.

Each image is injective because equal displayed coordinates recover the whole idempotent actor and band coordinate upstairs; distinct source idempotents cannot have the same lift. Closure of each source E-set follows because the relevant two-lift product is idempotent and has the required retained row/column. No regularity assumption on S is required.

For V=SN, and also for V=GLOBALREG, V contains both zero-band varieties, so EVERY canonical row and column E-set must itself lie in V. For V=SL, the row bands must be right normal (`xyz=yxz`), column bands left normal (`xyz=xzy`), and cell bands semilattices. This does not assert that mere cellwise tests or any of these necessary conditions suffice.

## 3. Strict improvement beyond BOTH local-corner and upper-cone GLOBALREG tests

Let B5={x,u0,u1,v0,v1}, with a·x=x, x·u_i=x·v_i=v_i, u_i u_j=u_i, u_i v_j=v_j, v_i u_j=v_i, v_i v_j=v_j. It is SN and all elements are idempotent, hence it is an original regular WEU/local-r source. EVERY lower corner and EVERY upper idempotent cone is GLOBALREG. But B5 itself is not GLOBALREG: at (a,b,c)=(u0,x,u1), `abaca=v0` while `abca=v1` (equivalently `xyxzx≠xyzx`).

Because a·x=x for every a, EVERY source-to-leftzero homomorphism is constant. There is only one canonical row, whose E-set is all B5. Section2 would embed it in a GLOBALREG band times RZ, which is GLOBALREG—a contradiction. Therefore B5 has NO embedding into ANY idempotent-separating image of a GLOBALREG-band-by-CS physical host, arbitrary actors/actions and infinite targets included. It DOES have its own positive fullSN host (actor trivial). This is a strict insufficiency result for the COMBINED local-corner and upper-cone tests at the explicitly NARROWER GLOBALREG target, not a counterexample at the originalSN target.

`frontier-20261029-B5-cones-globalREG-checker-v1.py`, SHA `3dd3198690000fccd71f3136c8a42372cfc28e9b6fc4ba94b6fdb1da25ddb7fe`, checks all125 associativity,625SN, every upper/lower cone's closure and GLOBALREG identity, and the literal globalREG failure3≠4. It completed before ThuOct29 02:43:33 PDT2026.

`frontier-20261029-Q2-row-column-band-checker-v1.py`, SHA `dcaff37dcf000ddfdb6b09243cb4e8d04903ae79251f1d9d9cfb406f76281177`, computes canonical classes from all S68 products (pinned source SHA `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf`). Its two row E-bands have17,17 elements, column E-bands4,14,16, all checked closed andSN. GLOBALREG fails in row/column at(24,8,52) and the second row at(28,12,56). Thus S68 likewise cannot even embed in the GLOBALREG target's idempotent-separating images. This is also an APPLICATION of the older V-upper-cone theorem, since24,8,52 lie in its common-lower-bounded cone; it is not double-counted as an independent obstruction. The original fullSN image/host class is untouched. No sufficiency, formal/independent verification, novelty or largest-class answer is claimed.
