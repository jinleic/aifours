# Finite rank replacement for the four-replica source-span import at d=4

**PhysicsResearch96h-2 / physics-1.** Actual native clock before writing: **Wed Oct 28 17:29:51 PDT 2026**. This is a **computer-assisted finite-dimensional proof candidate**, with exact modular rank witnesses and two replay algorithms described below. It removes the need to assume a general Schur–Weyl theorem for the local dimensions actually used by the d4 certificate, subject to the finite arithmetic/software evidence and the explicit elementary matrix-derivative argument. It is not a new representation-theoretic discovery, not a general-d theorem, and not human/formal/Lean/configured-family or parent adoption.

## 1. Exact claim needed by the original certificate

For each `n` in `{2,4}`, let `W_n=(C^n)^tensor4`. For a permutation p∈S4, let V_p permute the four tensor factors of W_n. Then

**`{A∈End(W_n): A U^tensor4=U^tensor4 A for ALL U∈U(n)}
   = span_C{V_p:p∈S4}`.**                                      (C_n)

The `n=4` case is used at each of the three physical sites of `(C^4)^tensor3`; `n=2` is the auxiliary Q factor for the original rank-two lift. These are the only local dimensions in the actual d4 moment certificate. This statement is about the full unitary commutant, not a restriction of physical C, a selected state or a claim for all n.

## 2. Finite integer constraint system from unitary invariance

Index the tensor basis of W_n by all four-letter words x=(x1,x2,x3,x4) with letters in `{0,…,n−1}`. Write `wt(x)` for the n-tuple of occurrence counts of its letters. Commutation with all diagonal unitaries gives

`A_(x,y)=0 unless wt(x)=wt(y)`.

Indeed a matrix element acquires the character `exp(i (wt(x)−wt(y))·theta)` under arbitrary diagonal phase angles; invariance for ALL angles forces any coefficient with unequal weights to vanish. Let the remaining same-weight entries be N_n complex unknowns.

For i≠j let `E_ij` be the n-by-n matrix unit and let `rho(E_ij)` be the sum of E_ij acting in each of the four replica positions. If A commutes with U^tensor4 for ALL U∈U(n), differentiating at the identity along the skew-Hermitian generators `E_ij−E_ji` and `i(E_ij+E_ji)`, then taking their complex linear combinations, gives `[A,rho(E_ij)]=0`. Only standard finite-dimensional matrix exponential differentiation is used.

Explicitly, for every word y with at least one j and every word x with

`wt(x)=wt(y)+e_i−e_j`,

one integer-coefficient row of this system is

`Σ_(t:y_t=j) A_(x,y[t←i])
 −Σ_(t:x_t=i) A_(x[t←j],y)=0`.                              (R)

All occurrences and all rows are defined on the ACTUAL four-replica basis; no abstract representation is substituted. The finite calculation uses an independent subset of these rows only; they are necessary for every unitary commutant element.

Every V_p preserves weights and commutes with every rho(E_ij), because the latter is the sum of the SAME local operator over all replica positions. Thus the 24 permutation matrices lie in the kernel of **every** integer row (R) and in the actual U(n) commutant. This inclusion is a universal algebraic argument, not a data assumption.

## 3. Rank sandwich: why finite-field witnesses prove characteristic-zero equality

Let K_n be the integer matrix of all constraints (R) on the N_n same-weight unknowns, and let P_n be the N_n-by-24 integer matrix whose columns are the entries of the permutation operators V_p. For any prime p,

`rank_C K_n >= rank_Fp K_n`,
`rank_C P_n >= rank_Fp P_n`,

because a nonzero minor modulo p is a nonzero integer minor. The universal permutation inclusion gives `K_n P_n=0` over the integers. Therefore

`rank_C K_n + rank_C P_n <= N_n`.

If a finite-field computation supplies ranks at least N_n−r and r respectively, the inequality forces equality throughout: `dim_C ker K_n=r=dim_C span{V_p}`. Every unitary-commutant element lies in ker K_n by §2, while every V_p lies in the unitary commutant. The inclusions and equal dimensions prove (C_n).

This argument uses **lower bounds** on two integer-matrix ranks. It does not assume that a modular rank upper bound is automatically valid over C, and it does not need every constraint row once a full minor of the required size has been exhibited.

## 4. Actual exact finite witnesses and independent replays

Prime **65521** was checked by exact trial division through its integer square root in the independent verifier. The physical values n=4 and n=2 are fixed by the source target and auxiliary space, not chosen hypothetical examples.

| Local n | Full W_n dimension | Same-weight unknowns N_n | Rank of 24 permutation columns mod p | Independent commutator-row minor mod p |
|---|---:|---:|---:|---:|
| 2 | 16 | 70 | 14 | 56 |
| 4 | 256 | 2716 | 24 | 2692 |

Thus both lower bounds sum exactly to N_n. The unknown counts follow by summing squared weight-block sizes, `Σ_(a1+…+an=4)(4!/(a1!…an!))²`; the witness programs reconstruct these blocks directly from the complete basis, not from a rank assumption.

### Actual generator and witness

`frontier-20261028-local-commutant-rank-witness.py`, SHA256 `cc70da54065d71d824b9d796f1f439000f170b5b5685c83b0b35eb2104ea6d83`, generated selected independent constraint-row labels and pivot columns from (R), using exact sparse field elimination. The resulting concrete witness is `frontier-20261028-local-commutant-pivot-rows.json`, SHA256 `1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4`. Generator result `frontier-20261028-local-commutant-rank-witness-results.json`, SHA256 `91c48f2c8244d72b51b0b954ffa72c2ac54c1e3773298bbc5c4aea69e21c4517`.

Observed generator: dimension2 rank56 after81 rows; dimension4 rank2692 after20161 rows. Actual total **5.845s**, maximum resident set **22,511,616 bytes**. Reaching the rank threshold is sufficient by §3; it is not a claim that only those rows are valid or that later rows were individually examined.

### Independent replay of actual witness rows

`frontier-20261028-independent-local-commutant-witness-check.py`, SHA256 `5a9a0e017900e4a978e6824e4b0d4510634726c4d397f0f7c33f1deff85e8a1f`, read the pinned witness, reconstructed its rows from the displayed formula and its pivot columns from the full basis, verified the prime by trial division, and used a separately written **reverse-order/max-pivot** sparse modular elimination. It also built the 24 permutation columns afresh and computed their rank with FLINT nmod arithmetic; every selected constraint row annihilated every permutation column modulo p.

Actual result `frontier-20261028-independent-local-commutant-witness-check-results.json`, SHA256 `f32f88be65afcdc47f55ce9e647aab49b42f6e295c9cd353de7b8a2448aa1b97`: **PASS**, with the exact ranks in the table; elapsed **0.871s**. A deliberate duplicate-row control in the n=2 witness reduced the square rank to55 instead of56, and was detected. This is a checker fault control, not a physical counterexample.

### Third rank engine

`frontier-20261028-dense-local-commutant-witness-check.py`, SHA256 `e70562d5b8be87d82746a33e3867bfe6d6a6b4dddf9a968094094eb66b5fa643`, rebuilt the selected square matrices and used **dense FLINT nmod rank**, not either sparse rank algorithm. Result `frontier-20261028-dense-local-commutant-witness-check-results.json`, SHA256 `9fb2adaf6863ec0dd6a42ddd667e469e114d05af46d9645b0b0c5f9225950925`: full ranks56 and2692, duplicate-row control55 for n2, prime check PASS; total **2.101s**. This third rank engine shares the second checker's row-reconstruction helper; it is not a third independent developer/model family or a formal kernel.

By the explicit rank sandwich, the two actual local commutant claims (C_2),(C_4) follow **conditional on the specified exact finite-checker/runtime correctness**. No known theorem about commutants in unspecified dimensions is imported.

## 5. Actual four-local-factor source span

Regroup `(H⊗Q)^tensor4` by local factors as `(C⁴)^tensor4 ⊗ (C⁴)^tensor4 ⊗ (C⁴)^tensor4 ⊗ (C²)^tensor4`. The local group is `U(4)^3×U(2)`, acting independently on these four factors. Finite-dimensional vector-space decompositions give

`End(total)^(U(4)^3×U(2))
 = End((C⁴)^tensor4)^(U(4))^tensor3
   ⊗ End((C²)^tensor4)^(U(2))`.

For example, expand an operator in a basis of the other factors; invariance under the first independent group forces every coefficient in that basis into the first invariant subspace, and repeat. Equivalently use vector-space complements to see the intersections of the four factorwise invariant subspaces equal the displayed tensor product. No independence of the later word operators is assumed.

Applying (C_4) and (C_2) yields the span of all **four-component permutation words** `V_(p1)⊗V_(p2)⊗V_(p3)⊗V_(pQ)` for the actual source at d4. The physical twirl additionally has, for each letter family, the two-sided replica stabilizer invariances, site-permutation invariance, and real/symmetric inversion invariance described in the certificate bridge. Averaging any word representation over these finite actions yields a real orbit-sum representation. Word dependencies in the Q=2 factor do not matter: spanning is enough.

The separately run independent orbit checker established all corresponding word partitions and counts1142/2391/1142. Therefore the source-span step needed by the actual original q3 certificate has a concrete finite-rank route: no application to arbitrary d, and no appeal to a separately verified broad Schur–Weyl theorem, is required.

## 6. Exact implications and remaining assurance

Combine §5's source span with the already independently checked 4675-orbit corrected identity and 1237 corrected PSD multipliers, and with the explicit actual rank<=2 lift/Gram/equality/q3 objective bridge in `frontier-20261028-d4-certificate-bridge-and-independent-identity-v1.md`, SHA256 `cc9a354a16b9d3abf6ac1ef8ff6fcc6e2041a88d435216b9d9b326a85f348a66` plus `frontier-20261028-d4-certificate-verification-addendum-v1.md`, SHA256 `176eac7dcf96c9819c5d73488787b18a201be0a0b5a46061b26ac83f67a14340`.

The resulting **computer-assisted d4 proof candidate** is conditional on correctness of the pinned finite rank/identity/PSD implementations, exact arithmetic libraries, and written elementary bridge. This is not numerical agreement or a no-defect report presented as final acceptance. Parent/independent scientific review, human or separate model-family review and formal/Lean verification remain unperformed. The public source already claims the target; no novelty is claimed. No unrestricted all-d theorem, physical distillability criterion, new physical witness or original-target redefinition follows.

All scientific runs were local, bounded and single-process; no paid/external model, nested agent, deletion, Git push/publication, secret access or infrastructure mutation occurred. Existing historical held outcomes are not premises or retroactively validated.
