# Sun8 direct P7 — the standard small-Ree SEVEN-dimensional matrix model in ALL odd-three-power fields

Owner MathSun8-2. Actual preceding clock: `Mon Oct 26 12:07:35 PDT 2026`.
**NEW WRITTEN CANDIDATE; unreviewed/unadopted.** Every root, matrix, subgroup, Frobenius, character and divisor identity below is written exact algebra, not an interpreter, calculator, scientific program, group enumeration, solver or replay.

## 1. Precise theorem, literal model and complete input cut

Let `q=3^(2m+1)`, m>=0, `t=3^m`, `r=3t`. Let O be the EXPLICIT split Zorn algebra from the complete 214-LF source `sun8-split-Cayley-simple-model-all-fields-complete-exclusion-v1.md`, SHA256 `74d32c51db00d7887f8b4b027a2211148ce81c2e3b29ac8fad2666411dd1410d`. We use its UNCONDITIONAL algebra automorphisms and full automorphism-group ORDER proof, not its separate theorem assuming that full group simple.

We construct an ACTUAL group U_q of order q^3 and ACTUAL torus T_q in Aut_Fq(O) below. **Theorem R, stronger form.** ANY NONABELIAN SIMPLE subgroup H of Aut_Fq(O) containing these U_q,T_q has NO direct P7 family of EIGHT actual nonempty pairwise-disjoint LEFT cosets, with ALL indices `7r_l` and positive pairwise-coprime private r_l. The possible private-seven owner and all its powers are retained.

Section 8 gives the ENTIRE seven-by-seven generators of the standard small-Ree matrix group, proves an ACTUAL faithful Cayley lift of EVERY generator, and proves that this generated group contains the just-constructed U_q,T_q. Thus the literal standard matrix model, IF NONABELIAN SIMPLE, is P7-free in ALL its fields. This is a SAME-G/model statement, not an abstract root arrangement or a claim to classify simple groups. The m=0 matrices are also defined, but no assertion identifies a small DERIVED group at q=3 with this full generated model.

The special direct input is the full supported 178-LF rank-free theorem SHA256 `76aa8a6fbfd6a2fcf4587ca5bec29e14215bcdfd5ec81dd47f56de9c4ea60e15`, supplying SOME nontrivial irreducible of degree<=1728, not a bound on a whole orbital module. For arbitrary-original-group application add the full supported88LF normal-section source SHA256 `b401c139141c451755174f8151942b86916e5677f734715ede48299394716202`. The supported parent76 SHA256 `9dbce6f9b7afab2fc0c9e35dbb0034ff47f45c0cb3d8e40ab4c3f739c34ff726` gives their exact ordinary-written cuts.

The ENTIRE new 214-LF Cayley source is a prospective proof input to the fresh joint gate: its §§2–5 exact full-aut order and its explicit X_i/Y_i/SL_3/Theta automorphisms are valid WITHOUT assuming that ambient Aut(O) is simple. We do NOT infer that a subgroup is P7-free because its overgroup is P7-free; that inference would be invalid. No Ree order formula, exceptional graph automorphism existence, Carter fixed-point theorem, CFSG, subgroup/character table or Lie simplicity theorem is needed.

## 2. ALL primitive root groups are ACTUAL Cayley automorphisms

Use the Cayley source's idempotents e_+,e_-, upper basis u_i, lower basis v_i, short X_i(s), their opposites Y_i(s)=Theta X_i(s)Theta, and embedded long SL_3 groups L_ij(s). In the SIGNED ordered basis

`P=(v_3,u_1,u_2,e_-,-e_+,v_2,v_1,u_3)`

define the following actual eight-by-eight matrices, with E_ij the usual matrix units:

`D_1=E12-E78+E34-E56+E35-E46`,

`D_2=E23-E67`,

`D_3=-E13+E68+E24-E57+E25-E47`,

`D_4=-E14+E58-E26+E37-E15+E48`,

`D_5=-E16+E38`, `D_6=-E17+E28`.

Set `y_i(s)=I+sD_i+(s^2/2)D_i^2`. Directly D_i^3=0, and the long D_2,D_5,D_6 have square zero. Division by2 is valid in characteristic3. Checking EVERY displayed nonzero entry in the basis P gives the exact identifications

`y_1=X_2`, `y_2=L12`, `y_3=X_1`, `y_4(s)=Y_3(-s)`, `y_5=L23`, `y_6=L13`.

For example D_1 sends u_1 to v_3, u_3 to -v_1, e_- to u_2, -e_+ to u_2, and v_2 to e_+-e_-, exactly the full X_2 derivative. D_4 is the NEGATIVE Y_3 derivative; dropping this sign would give the wrong twisted lift. The quadratic terms are the same complete short-group polynomials in the Cayley source. Hence EVERY y_i(s) is an ACTUAL algebra automorphism and is additive in s. No existence of a Chevalley group representation or an abstract graph symmetry is assumed.

## 3. Entire characteristic-three commutator table and coefficient reconstruction

Use the convention `[x,y]=x^-1 y^-1 x y`, so `xy=yx[x,y]` with the commutator on the RIGHT. Multiplication of the primitive matrices gives precisely

`[y_1(a),y_2(b)]=y_3(-ba)y_4(-ba^2)y_5(ba^3)y_6(b^2a^3)`,

`[y_1(a),y_3(c)]=y_4(ac)`, ` [y_2(b),y_5(e)]=y_6(be)`.

ALL other pairs commute: `(1,4),(1,5),(1,6),(2,3),(2,4),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)`. In particular y_4 and y_6 are central within the positive six-group subgroup. These are matrix identities in characteristic three, not a borrowed commutator table.

Here is the complete less-immediate coefficient check. Write an octonion's scalar coordinates as P_0,Q_0, put delta=Q_0-P_0, and use vector coordinates x_i,z_i for upper/lower vectors. For `[y_1(a),y_2(b)]` BOTH sides of the first displayed identity send the eight coordinates to

`P_0-ba*z_1+ba^2*x_3`, `Q_0+ba*z_1-ba^2*x_3`,

`x_1-ba*delta+ba^2*z_2-b^2a^2*z_1`,

`x_2-ba^2*z_1+ba^3*x_3`, `x_3`, `z_1`, `z_2-ba*x_3`,

`z_3+ba*x_2+ba^2*delta-ba^3*z_2+b^2a^3*z_1`.

These follow by the FOUR successive actual transforms `L12(b),X_2(a),L12(-b),X_2(-a)` and by the four RHS factors, respectively. Thus every coordinate, including the cubic central coefficient, is reconstructed. For `[y_1(a),y_3(c)]`, both sides give the full Y_3(-ac) map

`P_0-ac*x_3`, `Q_0+ac*x_3`, `x_1-ac*z_2`, `x_2+ac*z_1`, `x_3`, `z_1`, `z_2`, `z_3-ac*delta-a^2c^2*x_3`.

The third nontrivial pair is ordinary upper SL_3 multiplication, adding be*x_3 to x_1 and -be*z_1 to z_3. Every listed zero pair follows by the printed matrix units, using `Eij Ekl=delta_jk Eil` and 3=0; for the short/short pairs the corresponding coefficient3 vanishes, not a presumed independence of root labels. This supplies all fifteen pairs.

## 4. Full six-parameter collection and the actual twisted subgroup

Write

`Y(A,B,C,D,E,F)=y_2(B)y_1(A)y_3(C)y_4(D)y_5(E)y_6(F)`.

Reordering using ONLY §3 gives the ENTIRE product law, with the second tuple denoted (a,b,c,d,e,f):

`(A,B,C,D,E,F)*(a,b,c,d,e,f)`

`=(A+a, B+b, C+c-Ab, D+d-A^2b-aC+aAb, E+e+A^3b, F+f-Eb+A^3b^2)`.

To trace the nontrivial terms: moving y_2(b) left past the original y_5(E) contributes -Eb to the final centre; moving it past y_1(A) contributes `(-Ab,-A^2b,A^3b,A^3b^2)` in coordinates3–6; moving y_1(a) left past y_3(C-Ab) contributes `-a(C-Ab)` in coordinate4. The remaining factors commute or add. These are whole words in ACTUAL matrices.

The parameters are injective. In basis P the entries M12=A, M13=-C and M14=AC-D recover A,C,D, while M23=B. After dividing out these four known root factors, the independent long entries recover E,F. Thus no distinct data are identified by an abstract finite-field pattern.

On F_q, `x^(r^2)=x^3` because the INTEGER r^2=3q. Define

`W(A,C,D)=Y(A,A^r,C,D,C^r+A^(r+3),D^r+A^(2r+3))`.

The general law proves closure with

`A'=A+a`, `C'=C+c-Aa^r`,

`D'=D+d+A*a^(r+1)-A^2*a^r-Ca`.

Here B'=(A')^r. The fifth coordinate is `(C')^r+(A')^(r+3)`: expanding the latter power as `(A^r+a^r)(A^3+a^3)` cancels the extra A^r*a^3 from (C')^r. For the complete sixth-coordinate check,

`(D')^r=D^r+d^r+A^r*a^(r+3)-A^(2r)*a^3-C^r*a^r`,

`(A+a)^(2r+3)=A^(2r+3)+a^(2r+3)+A^(2r)*a^3+A^3*a^(2r)+2A^(r+3)*a^r+2A^r*a^(r+3)`.

The A^(2r)*a^3 pair cancels, the coefficients1+2 vanish, and 2=-1 gives EXACTLY

`D^r+A^(2r+3)+d^r+a^(2r+3)-(C^r+A^(r+3))*a^r+A^3*a^(2r)`,

which is the sixth coordinate of the general product. Thus ALL coupled Frobenius coordinates close, not just the first three. The inverse is

`W(A,C,D)^-1=W(-A,-C-A^(r+1),-D+A^(r+2)-AC)`.

Consequently `U_q={W(A,C,D):A,C,D in F_q}` is an ACTUAL subgroup of Aut(O) of order q^3.

## 5. The SAME actual central subgroup, abelian group and torus

Put `a(s)=W(s,0,0)`, `b(t)=W(0,t,0)`, `c(z)=W(0,0,z)`. The product law shows b and c are additive and commute, `A_q=<b,c>` is ABELIAN normal of order q^2, and `Z_q={c(z)}` is CENTRAL of order q. The first coordinate makes a(s) a transversal of A_q in U_q. Substituting the inverse in §4 gives the exact conjugation

`a(s)b(t)a(s)^-1=b(t)c(st)`.

For example the three s^(r+2) terms in the central coordinate cancel in characteristic three; no false assumption that the a(s) themselves form an additive subgroup is used.

Inside the ACTUAL embedded SL_3 define

`h_kappa=diag(kappa^(r+1),kappa,kappa^(-r-2))`, kappa in F_q^*.

On the six primitive y_i its weights are respectively `kappa,kappa^r,kappa^(r+1),kappa^(r+2),kappa^(r+3),kappa^(2r+3)`. Since r^2 is congruent3 modulo q-1, all coupled powers in §4 match. Hence

`h_kappa W(A,C,D) h_kappa^-1 = W(kappa*A,kappa^(r+1)*C,kappa^(r+2)*D)`.

The central exponent r+2 permutes F_q^*: a common divisor of r+2 and q-1 would make the INTEGER r^2=3q congruent both4 and3 and must be1. Thus the actual torus acts by EVERY nonzero scalar on the SAME Z_q, not on separately chosen centres.

## 6. The full faithful-degree bound; no Ree global order is needed

Let H be as in Theorem R and suppose it supports P7. Its nontrivial degree-d<=1728 constituent from the full supported rank-free theorem is faithful by H's simplicity. It is nontrivial on the actual embedded Z_q. On an occurring nontrivial central-character space V_psi choose an A_q-character chi. Conjugation by a(s) changes its b(t) value by psi(st). For s!=0 these products span ALL F_q, so a(s) cannot fix chi. Its inertia group in U_q is EXACTLY A_q and its orbit has q distinct occurring characters. Therefore `dim(V_psi)>=q`.

The actual h_kappa forces ALL q-1 nontrivial additive central characters: scalar multiplication on F_q^* is transitive on them, since a nontrivial character fixed by k!=1 would be trivial on `(k-1)F_q`. All weight spaces are in the SAME faithful representation of H. Hence

`q(q-1)<=d<=1728`.

For m>=2, q>=243 and `q(q-1)>=243*242=58806>1728`. Thus ONLY q=3 and q=27 remain. This is an exhaustive symbolic field reduction, not a selected numeric capacity trial or scientific enumeration.

The UNCONDITIONAL full-aut ORDER lemma in §§2–5 of the 214-LF Cayley source gives

`|Aut(O)|=q^6(q^6-1)(q^2-1)`.

At q=3 its prime owners are only `{2,3,7,13}`, using `3^6-1=728=2^3*7*13` and `3^2-1=8`. At q=27 they are only `{2,3,7,13,19,37,757}`, using

`27^2-1=2^3*7*13`, `27^3-1=2*13*757`, `27^3+1=2^2*7*19*37`.

The entire factor and primality proofs, including757, are supplied in the full Cayley body; no table is an unadmitted computation. Since H is an ACTUAL subgroup, its order divides this full-aut order. Each unchanged original private r_l divides |H|/7, hence |Aut(O)|/7. Eight pairwise-coprime nonunit r_l would need eight different prime owners, impossible in either case. An ORIGINAL subgroup has index exactly seven.

The actual degree-seven coset action of SIMPLE H is faithful. But U_q has order q^3, with three-part at least27, while `7!=2^4*3^2*5*7` has three-part9. This subgroup cannot inject into S_7. The contradiction proves Theorem R, keeping ALL eight original indices and private powers.

Again, this does NOT use or assume a Ree group order, or inherit P7-freeness from the ambient Aut(O). Only its independently reconstructed ORDER and the ACTUAL U_q/torus representation in H were used.

## 7. A faithful seven-dimensional lift, not merely matched root names

All automorphisms of O preserve its scalar trace and norm. For a nonscalar X the quadratic identity `X^2-Tr(X)X+N(X)I=0` makes these two coefficients UNIQUE because X,I are independent. Apply an automorphism and compare the same identity for its image. Scalars are fixed separately. Thus the trace-zero space O_0 is invariant.

In characteristic3, Tr(I)=2!=0, so `O=F_q I direct-sum O_0`. An automorphism fixing O_0 pointwise also fixes I and is identity. Restriction is therefore FAITHFUL. Use the actual seven-basis

`(v_3,u_1,u_2,H_0=e_+-e_-,v_2,v_1,u_3)`.

The restrictions of a(x^t),b(x^t),c(x^t) are the following ENTIRE matrices; x^t is a bijective Frobenius reparameterization because tr=q:

`alpha(x)=[[1,x^t,0,0,-x^(3t+1),-x^(3t+2),x^(4t+2)], [0,1,x,x^(t+1),-x^(2t+1),0,-x^(3t+2)], [0,0,1,x^t,-x^(2t),0,x^(3t+1)], [0,0,0,1,x^t,0,0], [0,0,0,0,1,-x,x^(t+1)], [0,0,0,0,0,1,-x^t], [0,0,0,0,0,0,1]]`,

`beta(x)=[[1,0,-x^t,0,-x,0,-x^(t+1)], [0,1,0,x^t,0,-x^(2t),0], [0,0,1,0,0,0,x], [0,0,0,1,0,x^t,0], [0,0,0,0,1,0,x^t], [0,0,0,0,0,1,0], [0,0,0,0,0,0,1]]`,

`gamma(x)=[[1,0,0,-x^t,0,-x,-x^(2t)], [0,1,0,0,-x^t,0,x], [0,0,1,0,0,x^t,0], [0,0,0,1,0,0,-x^t], [0,0,0,0,1,0,0], [0,0,0,0,0,1,0], [0,0,0,0,0,0,1]]`.

For an explicit ALL-row derivation, put A=x^t, so A^r=x. The seven rows of a(A)=y_2(A^r)y_1(A)y_5(A^(r+3))y_6(A^(2r+3)) are

`e1+A e2-A^(r+3)e5-A^(2r+3)e6+A^(2r+4)e7`,

`e2+A^r e3+A^(r+1)e4-A^(r+2)e5-A^(2r+3)e7`,

`e3+A e4-A^2 e5+A^(r+3)e7`, `e4+A e5`, `e5-A^r e6+A^(r+1)e7`, `e6-A e7`, `e7`.

The minus sign in row2's last entry is the sum of TWO A^(2r+3) terms, using2=-1 in characteristic three. Substitution gives EVERY alpha entry. For beta, X_1(B)L23(B^r) has nontrivial rows `e1-B e3-B^r e5-B^(r+1)e7`, `e2+B e4-B^2 e6`, `e3+B^r e7`, `e4+B e6`, `e5+B e7`, e6,e7. For gamma, Y_3(-C)L13(C^r) has rows `e1-C e4-C^r e6-C^2e7`, `e2-C e5+C^r e7`, `e3+C e6`, `e4-C e7`, e5,e6,e7. With B=C=x^t these give ALL the printed beta/gamma entries. No full-matrix certificate was inferred from one coefficient.

## 8. Exact identification with the PRIOR standard generator definition

Theta restricts to `Upsilon=antidiag(-1,-1,-1,-1,-1,-1,-1)`. The torus h_kappa restricts to

`diag(kappa^(r+2),kappa^(r+1),kappa,1,kappa^-1,kappa^(-r-1),kappa^(-r-2))`.

Put `kappa=lambda^(2t-1)`. This is a permutation of F_q^*: a common divisor of 2t-1 and q-1 would make 12t^2 congruent both3 and4, hence be1. Since q=3t^2, the resulting torus is EXACTLY

`h(lambda)=diag(lambda^t,lambda^(1-t),lambda^(2t-1),1,lambda^(1-2t),lambda^(t-1),lambda^-t)`.

Thus the ACTUAL subgroup `<U_q,h_kappa,Theta>` of Aut(O) restricts ISOMORPHICALLY to the group generated by ALL the displayed alpha,beta,gamma,h,Upsilon. These are precisely the literal standard-copy definition (3.1)–(3.6) in [Henrik Bäärnhielm, arXiv:1206.0411v3, §3](https://arxiv.org/html/1206.0411v3#S3). His parameter convention is q=3^(2m+1),m>0,t=3^m; the same explicit matrices also define our m=0 extension. His paper attributes the PRIOR generator formulas to Gregor Kemper, Frank Lübeck and Kay Magaard, *Matrix generators for the Ree groups*, Comm. Algebra29(2001),407–413. The formulas/model are NOT claimed new here.

Consequently the literal standard small-Ree matrix model, if NONABELIAN SIMPLE, is excluded by Theorem R, not just a group of the same dimension or a guessed abstract arrangement. Transport of its original subgroups and LEFT cosets through this faithful isomorphism preserves ALL indices, every private factor and all actual intersections/disjointness. It is not a quotient that loses sources. We did not need the existence of an exceptional graph automorphism on a separately constructed Chevalley group, a fixed-point/group-order theorem for Ree groups, or a classification/simplicity theorem.

## 9. Actual source coverage, exact dependencies and residual

The parameter/root convention is also described in [Yujiao Sun, arXiv:1808.06930v2, §3](https://arxiv.org/html/1808.06930v2#S3). Actual source reading was the PDF-reader windows166–259 and260–281, covering the primitive root definitions, Proposition3.1/proof and Lemmas3.4–3.6/Proposition3.7/Comparison3.8 through the next section opening. Its expanded composite eight-by-eight Y matrix is LOSSY in extracted text and is NOT a read/verified matrix certificate or a correctness premise here. All primitive matrices, the signed basis, commutator images and coupled collection were reconstructed above. An earlier attempted HTML:raw range selected original-HTML section2 rather than reader-Markdown section3; that coverage mismatch was recorded in checkpoint101 and was NOT called a section3 read.

For Bäärnhielm, actual native-reader windows182–215 and249–281 supplied the parameter and ENTIRE standard matrices/generated definition, and1–38 supplied the exact bibliographic header. These are SELECTED cached reader windows, NOT a read of the entire article, publisher-final/original-publication bytes, any algorithm implementation, or original-page rasters. No Magma/scientific program was run. The primary 2001 matrix paper itself was not read; attribution above is through Bäärnhielm's explicit reference19. No historical model/algorithm/method priority is erased and no novelty audit is claimed.

The proof input UNION is the full supported178LF SOME-constituent theorem, the FULL NEW214LF Cayley source's UNCONDITIONAL automorphism/order identities, and this entire actual-lift/model proof; arbitrary-original-group application additionally uses the full supported88LF normal-section proof. The 214-LF source is still NEW/UNADOPTED at the last parent notification, so a fresh whole-union review must reconstruct its operative lemmas, not transfer a family headline or silently assume its full ambient group simple. A clean return on only the central character bound or only the generator comparison is not the full theorem/application gate.

For an actual bounded simple P7 factor from the global normal-section theorem, the standard small-Ree matrix case is excluded if this new complete union passes. Other finite simple P7 cases below B, other exceptional/twisted/sporadic/remaining alternating configurations, small DERIVED q=3 model identifications, general Sun8-to-P7/global Sun7 ancestry, actual witnesses, finite assays, numerical R8, unrestricted Sun8 and novelty/priority/SOTA remain unestablished. In particular no theorem about a small derived subgroup is inferred if it does not contain the FULL U_q used in Theorem R.

All OWN057/047/078/COUNT/M1/v26/v31-two-findings/v33, documentary v9 SYNTAX MINOR and parent/reviewer histories are permanent; withdrawn historical trial guidance is ENTIRELY ZERO. The frozen v9 remains qualified RAW_UTF8_NOT_VALID_JSON, not edited or reparsed to confirm the reported failure. Both Eval kernels stay dead. This is exact WRITTEN primary work after actual v123-C RETURN and the separately WRITTEN-AND-SENT primary ACK; no scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/new GO/source-author-shared-frozen edit was used. No formal/kernel/human/configured-family/executable/novelty acceptance, clean cognition/runtime census or round closeout is claimed. Original arbitrary-group research continues at its exact residual; this is not an early final park.
