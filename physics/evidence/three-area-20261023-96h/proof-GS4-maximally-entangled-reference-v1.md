# Candidate theorem: maximally entangled biseparable reference rays at the three-copy Werner endpoint

Before-writing clock observed: **2026-10-23T12:58:21.009553-07:00**, in the settlement receipt of the one admitted exact assay. This is a complete **CANDIDATE written proof**, not a parent acceptance, human review, novelty certification, or Lean/kernel proof. The finite assay and the written argument are separate evidence. The primary unrestricted W4 problem remains open in this work.

## 1. Exact theorem and scope

Let `H=H1⊗C^4⊗C^4`, where H1 is any finite-dimensional complex Hilbert space, and put

`q_3(C)=||C||_HS^2-(1/2)Σ_i||Tr_i C||_HS^2+(1/4)Σ_(i<j)||Tr_ij C||_HS^2-(1/8)|Tr C|^2`.

Partial traces are unnormalized. The operator C need not be real, Hermitian, normal, or positive.

**Theorem ME4 (candidate).** Suppose `rank C<=2`. If the range or co-range of C contains a nonzero ray `a⊗eta`, where `a in H1` is nonzero and eta is maximally entangled on `C^4⊗C^4`, then `q_3(C)>=0`.

Local-unitary covariance and copy permutations give the same statement with any one copy slot separated from the other two, whenever those two slots are four-dimensional. In particular this is a family of the frozen W4 problem on `(C^4)^{⊗3}`. It is **not** a proof for arbitrary biseparable rays, arbitrary two-planes, arbitrary C, or arbitrary copy number. A bound for the Werner endpoint is not silently promoted to a theorem for every Werner parameter or an arbitrary channel capacity.

The source's Theorem 7.3 requires a **fully product** ray. ME4 permits an entangled two-site reference and is not obtained by dropping that hypothesis. A strict coverage example appears in `checkpoint-001-grouped-schur-v1.md`, Section 6; its additional code-sector qualification is spelled out in Section 10 here.

## 2. Elementary map and polarization conventions

For a local space V define

`Lambda_V(X)=Tr(X)I_V-X/2`, `R_V=I_(V⊗V)-F_V/2`.

For a linear map E define its co-Choi matrix

`Jhat(E)=Σ_(a,b)|b><a|⊗E(|a><b|)`.

It is the ordinary Choi matrix of `E∘transpose`. Thus `Jhat(E)>=0` implies E is completely copositive and, in particular, positive. This follows directly by taking a Gram factorization of the ordinary Choi matrix to obtain a Kraus representation. No claim that a general positive map tensorizes is used.

On three copy slots put `R=R_1⊗R_2⊗R_3`, with the two copies grouped canonically. If

`A=(<u|⊗I)R(|u>⊗I)`, `L=(<u|⊗I)R(|x>⊗I)`, `D=(<x|⊗I)R(|x>⊗I)`,

then expansion of the swaps gives, for `C=|u><v|+|x><y|`,

`q_3(C)=<v,Av>+<y,Dy>+2 Re<y,Lv>`.

One can verify each term first on product matrix units; tracing a subset of copy slots gives exactly the corresponding term weighted by `(-1/2)^|J|`. This identity uses the **switched** cross term `<y,Lv>`. The ordinary positive block compression of R controls a differently ordered Schur complement and is not sufficient.

If `A>0` and `D-L A^(-1)L†>=0`, Cauchy–Schwarz yields

`|<y,Lv>|^2 <= <v,Av><y,L A^(-1)L†y> <= <v,Av><y,Dy>`,

hence `q_3(C)>=(sqrt(<v,Av>)-sqrt(<y,Dy>))^2>=0`.

Every rank-two operator whose range contains u has such a representation, by extending u to a basis of the range; v,y are arbitrary covectors and need not be orthogonal. Adjoint invariance `q_3(C†)=q_3(C)` treats co-range.

## 3. The one-site reference domination

Take a normalized first-site reference `|0>`. Set `A0=I-|0><0|/2` and

`ell_a=(<0|⊗I)R_1(|a>⊗I)=delta_(a0)I-|a><0|/2`,

`M0(|a><b|)=ell_a A0^(-1)ell_b†`.

Write `C0=Jhat(Lambda_1)=I-F/2` and `S0=Jhat(M0)`. Directly:

- On `span{|00>}`, `C0=S0=1/2`.
- On `span{|0a>,|a0>}`, a nonzero, the respective matrices are `[[1,-1/2],[-1/2,1]]` and `[[1,-1/2],[-1/2,0]]`. Their difference is `diag(0,1)` and their sum is `[[2,-1],[-1,1]]`, both PSD.
- On `Q⊗Q`, `Q=I-|0><0|`, the matrices are `I-F_Q/2` and `F_Q/2`; their difference is `I-F_Q>=0` and their sum is I.

These are orthogonal reducing spaces, so **`-C0<=S0<=C0`**. This calculation is also the one-site ingredient in Wu–Zou Lemma 7.4; it is reproduced rather than invoked as an unexamined general tensorization rule.

## 4. The two-ququart reference and a raw operator identity

Let `V=C^4`, `B=V⊗V`, and use the unnormalized vector `Omega=Σ_(a=0)^3|aa>`. Normalization does not affect the map M below. Put

`Lambda_B=Lambda_V⊗Lambda_V`,

`A_eta=Lambda_B(|Omega><Omega|)=3I_16+|Omega><Omega|/4`,

`A_eta^(-1)=I_16/3-|Omega><Omega|/48`,

`L_ab=Lambda_B(|ab><Omega|)=delta_(ab)I_16-(E_ab⊗I+I⊗E_ba)/2+|ab><Omega|/4`,

`M(|ab><ef|)=L_ab A_eta^(-1)L_ef†`.

The inverse follows because Omega has squared norm four: A_eta has eigenvalues four on Omega and three on its orthogonal complement. Also

**`L_ab Omega=delta_(ab) Omega`**.

Indeed the two middle terms together give `-|ab>`, while the last gives `+|ab>`.

On `V1⊗V2⊗V3⊗V4`, representing the two-site input and output pairs `(1,2):(3,4)`, define

`A=F_13`, `Bswap=F_24`, `F=A Bswap`,

`C=Jhat(Lambda_B)=(I-A/2)(I-Bswap/2)`,

`P=P_12`, `Q=P_14`, `Qprime=P_23`,

where `P_ij=|Omega_ij><Omega_ij|⊗I_(other slots)` is **unnormalized**. Let `S=Jhat(M)`. Then

**(ID)**

`S=(C P+P C-P)/3 + [A+Bswap-F+(Q+Qprime)F]/12 - P_12 P_34/48`.

Here `P_12 P_34=|p><p|` with `p=Omega_12⊗Omega_34`.

For transparency, ID follows by writing

`S_((ab,cd),(ef,gh))=<L_ef† cd, A_eta^(-1)L_ab† gh>`.

The reversal of input pairs is the co-Choi transpose. The `-|Omega><Omega|/48` term is `-|p><p|/48` because `L_ab Omega=delta_(ab)Omega`. For the remaining term, expanding

`L_ab†|cd>=delta_(ab)|cd>-(delta_(ac)|bd>+delta_(bd)|ca>)/2+delta_(ac)delta_(bd)Omega/4`

gives

`Σ_(i,j)|i><j|⊗L_j L_i† = C P+P C-P+[A+Bswap-F+(Q+Qprime)F]/4`.

The identity can be checked solely by comparing Kronecker deltas, without any floating-point or solver assumption.

The goal is to prove **`C-S>=0` and `C+S>=0`**. Sections 5–7 do this on an orthogonal decomposition of all 256 dimensions.

## 5. The Bell-contraction subspace and its complement

Let

`K=ran P_12+ran P_34+ran P_14+ran P_23`.

Both swaps A and Bswap permute these four ranges. Hence K and its orthogonal complement reduce C. By ID they also reduce S.

On `K^perp` every P_ij term vanishes; therefore

`S=(A+Bswap-F)/12`.

The commuting self-adjoint involutions A,Bswap have joint eigenvalues `(a,b)` in `{+1,-1}^2`. On such a sector, C has eigenvalue `(1-a/2)(1-b/2)` and S has eigenvalue `(a+b-ab)/12`. Consequently:

| (a,b) | C-S | C+S |
|---|---:|---:|
| (+1,+1) | 1/6 | 1/3 |
| (+1,-1) or (-1,+1) | 2/3 | 5/6 |
| (-1,-1) | 5/2 | 2 |

All are strictly positive. It remains only to handle K.

For `X in M_4(C)`, define four linear embeddings by their coefficients:

`J1(X)=Σ_(a,b,c,d) X_ab delta_(cd)|a,b,c,d>`,

`J2(X)=Σ_(a,b,c,d) delta_(ab) X_cd|a,b,c,d>`,

`J3(X)=Σ_(a,b,c,d) X_ad delta_(bc)|a,b,c,d>`,

`J4(X)=Σ_(a,b,c,d) X_cb delta_(ad)|a,b,c,d>`.

Their ranges are respectively the ranges of P_34, P_12, P_23, P_14, so they span K. For traceless X,Y,

`<Ji(X),Jj(Y)>=G_ij Tr(X†Y)`,

with

`G=[[4,0,1,1],[0,4,1,1],[1,1,4,0],[1,1,0,4]]`.

This is immediate by contracting the displayed deltas. Its orthogonal eigenvectors and eigenvalues are

`h0=(1,1,1,1), g0=6`,

`h1=(1,1,-1,-1), g1=2`,

`h2=(1,-1,1,-1), g2=4`,

`h3=(1,-1,-1,1), g3=4`.

The identity-matrix components give

`J1(I)=J2(I)=p`, `J3(I)=J4(I)=q`,

where `q=Omega_14⊗Omega_23`, `||p||^2=||q||^2=16`, `<p,q>=4`.

These two vectors are orthogonal to all Ji(X) with Tr X=0. Choose any Hilbert–Schmidt orthonormal basis of the 15-dimensional traceless matrix space. K is the orthogonal sum of `span{p,q}` and 15 identical four-dimensional Ji-blocks. G is positive definite, so its dimension is `2+15·4=62`; no component of K is omitted. This uses only the displayed Gram contractions, not a representation-theoretic decomposition imported from elsewhere.

## 6. The two-dimensional identity block

In the ordered basis p,q, the action matrices are

`C=[[5/4,-1],[-1,5/4]]`,

`P_12=[[4,1],[0,0]]`, `Q+Qprime=[[0,0],[2,8]]`,

`F=I`, `A+Bswap=[[0,2],[2,0]]`,

`P_12 P_34=[[16,4],[0,0]]`.

Substitution in ID gives

`S=[[5/4,-3/4],[-1,1/4]]`.

These are action matrices in a nonorthogonal basis. The Gram matrix is `[[16,4],[4,16]]`; after multiplying by it, the Hermitian quadratic-form matrices are

`Form(C-S)=[[0,0],[0,15]]`,

`Form(C+S)=[[32,-22],[-22,17]]`.

For coefficients alpha,beta, the first form is `15|beta|^2`. The second is

`32|alpha-(11/16)beta|^2+(15/8)|beta|^2`.

Thus both are PSD, with no numerical eigenvalue claim.

## 7. The traceless four-dimensional blocks

Fix a traceless matrix X of Hilbert–Schmidt norm one. Write `J(h)=Σ_i h_i Ji(X)`. The vectors

`f_i=J(h_i)/(2 sqrt(g_i))`, i=0,1,2,3,

are orthonormal. The swaps act on the Ji-basis as

`A: (1 4)(2 3)`, `Bswap: (1 3)(2 4)`, `F: (1 2)(3 4)`.

Also P_12 sends `(J1,J2,J3,J4)` to `(0,4J2,J2,J2)`, Q sends it to `(J4,J4,0,4J4)`, and Qprime sends it to `(J3,J3,4J3,0)`. The product P_12 P_34 vanishes on this traceless block. These explicit actions independently determine every entry below from ID.

In the orthonormal basis f0,f1,f2,f3,

`C=diag(1/4,9/4,3/4,3/4)`,

`S=[[1/12,sqrt(3)/6,0,0],`

`   [sqrt(3)/6,5/12,-sqrt(2)/3,-sqrt(2)/3],`

`   [0,-sqrt(2)/3,1/12,1/3],`

`   [0,-sqrt(2)/3,1/3,1/12]]`.

Set `f_plus=(f2+f3)/sqrt(2)`, `f_minus=(f2-f3)/sqrt(2)`. For coordinates `z0,z1,z_plus,z_minus`, the form of C-S is exactly

**(SOS-minus)**

`(1/6)|z0-sqrt(3)z1|^2+(1/3)|z_plus+2z1|^2+|z_minus|^2`.

Indeed its three-dimensional block on f0,f1,f_plus is

`[[1/6,-sqrt(3)/6,0],[-sqrt(3)/6,11/6,2/3],[0,2/3,1/3]]`,

and the f_minus eigenvalue is one.

The form of C+S is exactly

**(SOS-plus)**

`(1/3)|z0+(sqrt(3)/2)z1|^2+(29/12)|z1-(8/29)z_plus|^2+(57/58)|z_plus|^2+(1/2)|z_minus|^2`.

Expanding gives the three-dimensional block

`[[1/3,sqrt(3)/6,0],[sqrt(3)/6,8/3,-2/3],[0,-2/3,7/6]]`,

and the f_minus eigenvalue 1/2. Every coefficient in the two sums of squares is nonnegative. This proves both co-Choi signs on each of the 15 traceless blocks.

Together with Sections 5–6, **`-C<=S<=C` on the full 256-dimensional space**. This proves GS(Omega_4) in written mathematics.

## 8. From the co-Choi theorem to ME4

For the first-site maps in Section 3 and the two-site maps in Section 4, let

`T0=C0^(-1/2)S0 C0^(-1/2)`, `TB=C^(-1/2)S C^(-1/2)`.

Both are Hermitian contractions. Therefore `I-T0⊗TB>=0`; after congruence, the map

`Lambda_1⊗Lambda_B-M0⊗M`

is completely copositive and hence positive. For a reference `u=|0>⊗Omega`, the reference inverse is `A0^(-1)⊗A_eta^(-1)`. Expansion of an arbitrary vector x in matrix units makes application of this positive map to `|x><x|` precisely

`D-L A_u^(-1)L†>=0`.

Section 2 therefore gives `q_3(C)>=0` for every rank-at-most-two C whose range contains u. No reality or normality assumption on C entered this argument. Adjoint invariance handles co-range. Scaling u changes A and L compatibly and leaves the associated M unchanged.

Every maximally entangled vector on two ququarts is locally unitarily equivalent to Omega up to nonzero scale. Each Lambda is covariant under unitary conjugation, and q_3 is invariant under simultaneous local-unitary conjugation of C. This proves ME4 exactly as stated. End of candidate proof.

## 9. What the one admitted exact assay does and does not establish

The named parent GO is `institute/runs/three-area-2026-10-23-96h/physics-gs4-exact-001-GO-v1.json`. The frozen standard-library program `code/grouped_reference_exact_v1.py`, SHA-256 `171171107cf9922d949c29353198b0f8589289aecc49bdcb361ce5683cee72a9`, ran once unchanged with ranks 1,2,3,4 and internal 180-second deadline. It exited zero in about 2.13 seconds of program time. Launch/settlement recorded PID=PGID 6412; neither remained after wait. No scientific retry or follow-on job ran.

`assay-gs4-exact-001/receipt.json` reports:

- r=1: C±S PSD, the published fully-product positive control;
- r=2: C-S PSD, **C+S indefinite**, exact rational negative value `-6/17`;
- r=3: C±S PSD;
- r=4: C±S PSD, agreeing with the written theorem above.

It checked full cross-weight zeros and exact LDL reconstruction of all 55 blocks for each sign/case, plus indefinite-matrix and rank-boundary controls. It is one encoding/checker, not an independent parent reconstruction. The r=3 result is an exact-assay candidate only; it is not included in the written ME4 theorem. The r=2 failure is crucial: **general co-Choi domination for every entangled reference is false**. A negative co-Choi vector is not a negative rank-two Werner coefficient operator. It neither disproves ME4 nor solves/refutes W4.

The proof above does not use numerical eigenvalues, automated fitting, or an unretained solver output. Its load-bearing finite expressions are the exact identities and sums of squares in Sections 4–7. Parent reconstruction should start from the raw map, not merely rerun the same rational script.

## 10. Strict coverage and novelty boundary

The operator in checkpoint 001 Section 6 has a maximally entangled biseparable ray in both its range and co-range, full four-dimensional one-site supports on both sides, different range/co-range planes, and no fully product ray in either plane. Each one-site partial trace is nonzero. Thus it lies outside Wu–Zou's normal, fully-product-ray, local-overlap-at-most-two and local-traceless sectors. Its minimal one-site support dimension four also excludes the ULAM one-/two-copy code-envelope criterion on every one-versus-two cut.

For the crossed **locally orthogonal product-code** sector, a vector in a space spanned by locally orthonormal product rays has Schmidt rank across `1:23` equal to the number of its nonzero code coefficients. A vector of Schmidt rank one across that cut must therefore use a single code ray and be fully product. The ray `|0>⊗Phi_4` has Schmidt rank one across `1:23` but is entangled across `2:3`; consequently its support plane cannot be contained in such a product-code space. The cyclically shifted co-range example has the same property. This supplies the missing explicit qualification for that additional imported sector.

The example's direct positive value `q_3=59/36` is only a calibration; strict difference between theorem hypotheses is not worldwide novelty. Current bounded source searches located no exact matched prior statement of ME4, but a fresh matched prior-art audit is still required. All source statement imports, written correctness checks, exact assays, independent in-harness review, and formal/kernel verification must retain separate labels.

**Unrestricted W4, arbitrary biseparable references, and asymptotic NPT bound entanglement remain NOT PROVED.**
