# CURRENT P44 CONSOLIDATION v9 — PART7/7: two finite auxiliary-PPT extension cones force physical decomposability

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 20:38:34 PDT 2026**. Exact WRITTEN/source/metadata only. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Original October27 cutoff11:05:38/deadline12:35:38 unchanged.

## Z0. Complete current union and exact assurance

The complete current v9 requires ALL original LF/endings of prior parts1–6(2124LF157313bytes total) AND ENTIRE this NEW Part7, as pinned by its author union manifest. Each source part is below90000bytes. Older headers/end labels remain immutable historical source bytes, not backdated v9 labels. No older frozen scope is restarted and no part alone is the entire-current gate. NEW C25 does not inherit any old Bose/C18/state-certificate verdict.

All mandatory overlays remain: old26-not27 metadata MINOR, C12 AT_MOST zero-mixture allocation precision MINOR and its unused positive residual, cp071 additive row identity correction, all owner exactness/ACK-order/cadence/admission/N4UNKNOWN/oldexit/old21 findings, parent/reviewer/root/freeze/clock/read corrections, and HOLD. No clean thought/runtime/history census or process cure by later exact algebra. This is author-WRITTEN pending fresh complete reconstruction, not executable/formal/human/family/novelty acceptance.

**Theorem C25:** at EVERY finite auxiliary dimension k>=2 and level N>=1, TWO specified weaker extension cones can certify only PHYSICALLY DECOMPOSABLE witnesses W: (A) actual Bose support with PPT ONLY on the global extended-Alice/all-Bob cut; (B) permutation-INVARIANCE without Bose support, even with ALL partial-transpose cuts, for the UNCOMPRESSED/permutation-averaged objective. Both receive explicit feasible negative controls from ANY physical PPT input of negative W expectation.

This DOES NOT exclude the genuinely stronger cone with BOTH actual Bose support AND PPT on proper nonempty Bob subsets. It is NOT an unrestricted all4x4 PPT=>SN2 theorem. The exact distinction between objectives/support/cuts is load-bearing below.

## Z1. Physical spaces, normalized auxiliary Bell factor and the TWO objectives

Let physical A,B have dimension d>=1. Auxiliary A0 and every Bj0 have dimension k>=2; every physical Bj has dimension d. The fixed tensor grouping is

`(A0,A):(B10,B1):...:(BN0,BN)`.

For arbitrary Hermitian physical W define

```
phi_k=(1/sqrtk)sum_(r=0)^(k-1)|r>_A0|r>_B10,
Phi_k=P(phi_k),
K_N(W)=Phi_k(A0,B10) tensorW(A,B1) tensorI_spectators.
```

Let P_N be the orthogonal projector onto symmetry of the COMPLETE paired Bob systems `(Bj0,Bj)`. Put

`Q_N(W)=P_N K_N(W)P_N`.

- In class A, states are ACTUALLY supported on `H_A0A tensor Sym^N(C^k tensorC^d)`. Q_N and K_N then have the same expectation. We impose PSD, trace1 and ONLY the partial transpose on all extended Alice A0A; the equivalent global-all-Bob cut adds nothing because total transpose preserves PSD.
- In class B, states are only invariant under conjugation by complete-pair Bob permutations, NOT required to be Bose-supported. The objective is K_N, or its permutation average `Kbar_N=(1/N)sum_j Phi_k(A0,Bj0) tensorW(A,Bj)` with spectator identities. These objectives agree on invariant states. **It is NOT Q_N**: inserting the Bose projector would change this second theorem. Impose PSD, trace1 and PPT on ALL subsets of the elementary party factors (in particular all complete-pair cuts).

These are precise mathematical cones, not claims about an unsubmitted solver encoding or the unknown historical N4 run.

## Z2. Class A: explicit Bose isometry for ANY physical PPT rho

Take ANY nonzero physical PPT rho>=0 and choose a unit physical vector v in C^d. Use two orthogonal auxiliary labels0,1, which exist because k>=2. Define

```
V_N:C^d -> Sym^N(C^k tensorC^d),
V_N b=(1/sqrtN)sum_(j=1)^N |0,b>_j
                       tensor_(l!=j)|1,v>_l.           (Z2.1)
```

Different summands have different single-zero auxiliary label strings and are orthogonal. Thus V_N*V_N=I_d for arbitrary COMPLEX b/v. A permutation of complete Bob pairs merely permutes the summands; V_N is actually Bose-supported, not just invariant as a mixed density.

With tensor order restored, define

`tau_N=|0><0|_A0 tensor(I_A tensorV_N)rho(I_A tensorV_N*)`. (Z2.2)

It is PSD, has traceTr rho and is fixed on both sides by P_N. Since V_N acts on Bob ALL copies and Alice auxiliary is a real product label,

```
tau_N^Gamma_A0A
 =|0><0|_A0 tensor(I_A tensorV_N)rho^Gamma_A(I_A tensorV_N*)>=0.       (Z2.3)
```

Thus normalizing by Tr rho makes an ACTUAL feasible class-A state for every finite N. No assumption that rho's hidden modes/Schmidt number are known, no product-vector sample and no scientific run is used.

Contract the normalized auxiliary Bell bra on A0,B10. Only the j=1 term in (Z2.1) has that pair00 and survives; all other j have pair01 and vanish. The surviving amplitude is EXACTLY1/sqrt(kN), with the physical rho on A,B1 and spectator `|1,v>` products. Consequently

```
Tr(Q_N(W)tau_N)=Tr(K_N(W)tau_N)
                         =(1/(kN))Tr(Wrho).             (Z2.4)
```

The formula includes N1, when the spectator product is the scalar1, and d1, when any physical PPT density is just a scalar. Norms are controlled by the literal isometry, not numerical diagonalization.

## Z3. Class-A certificate consequence: W must be decomposable

If the class-A minimum of Q_N(W) is nonnegative, apply (Z2.4) to EVERY trace-one physical PPT rho. It follows `Tr(Wrho)>=0` for every such rho. In particular any dual sufficient certificate

`Q_N(W)=P+R^Gamma_A0A`, P,R>=0 on the Bose-supported space,

has that same consequence. Partial transpose on Alice commutes with the Bob Bose projector, so this is a genuine bipartite positive-cone statement on extended Alice versus SymBob, with no subspace/PT mismatch.

The physical decomposable cone is `DEC={P0+Q0^Gamma_B:P0,Q0>=0}`. It is closed: for a convergent represented sequence, `TrP0+TrQ0=TrW` bounds both PSD traces/norms, so a subsequence converges to a positive representation of the limit. Its dual is PPT by PSD self-duality and trace self-adjointness of Gamma. Finite-dimensional bipolarity therefore gives `PPT*=DEC`.

Hence every W admitted by the class-A positivity condition is physically DECOMPOSABLE. No assumption that W was already two-positive is required. Contrapositively, if W is not decomposable, separation supplies a physical PPT rho with Tr(Wrho)<0, and (Z2.2) gives an explicit feasible negative class-A control at EVERY finite N, with expectation scaled by1/(kN).

This is a NECESSARY condition, not an iff: we do NOT claim every physical decomposable W passes this auxiliary lift, or that an arbitrary decomposable but not two-positive map is thereby valid. It is enough to rule out using this finite cone to certify any W that strictly detects a physical PPT density.

## Z4. Class B: a different, ALL-PPT permutation-invariant control

Drop actual Bose support, retain only invariance under complete-pair permutations, and use objective K_N/Kbar_N as specified in Z1. Define the CLASSICAL mixture

```
tauhat_N=(1/N)sum_(j=1)^N
  [|0><0|_A0 tensor|0><0|_Bj0
           tensor_(l!=j)|1><1|_Bl0]
       tensor rho_(A,Bj) tensor_(l!=j)P(v)_Bl.            (Z4.1)
```

All factors are placed in the fixed party order. It is PSD with traceTr rho. Complete Bob-pair permutations simply relabel j, so it is invariant.

It is PPT on EVERY allowed subset of elementary party factors. Each term has a product auxiliary state. On the only nontrivial physical factor rho_ABj, a subset cut transposes neither factor, one factor, or both: these give respectively rho, rho^Gamma (PSD by PPT), or rho^T (PSD). Spectator physical rank-one factors transpose to positive rank-one factors. Thus every transposed summand and their sum are PSD. This covers more cuts than the complete-pair/Alice cuts needed for the theorem, not an assumption of positivity of an unobserved matrix.

Again only j=1 has auxiliary pair00 at A0,B10. Therefore

`Tr(K_N(W)tauhat_N)=Tr(Kbar_N(W)tauhat_N)=Tr(Wrho)/(kN)`. (Z4.2)

In general tauhat_N is NOT Bose-supported. For instance its distinct auxiliary label strings are mixed rather than coherently symmetrized; a complete Bob permutation need not act trivially on each vector in its range. Thus (Z4.1) cannot be inserted into the stronger Bose/full-PPT problem.

The same physical PPT duality as Z3 proves: any nonnegative certificate for the class-B all-PPT invariant-state minimum forces W physically decomposable. This holds at EVERY finite N,k,d. Adding more finite copies without imposing actual Bose support cannot rescue a physical PPT-negative separator under this objective.

## Z5. Exactly which stronger cone is NOT ruled out

The two negative controls satisfy DIFFERENT sets of constraints:

- tau_N is Bose-supported and PPT on extended Alice versus ALL Bob, but its coherent single-excitation Bob isometry need NOT preserve PPT on a proper Bob subset.
- tauhat_N is PPT on ALL cuts and permutation invariant, but is generally NOT Bose-supported and is only a control for K_N/Kbar_N, not the Bose-compressed objective Q_N.

Therefore the cone that imposes BOTH actual Bose support AND relevant proper-nonempty-Bob-subset PPT constraints is NOT excluded by either proof. There is no assertion that either control is feasible there. That stricter full-PPT Bose cone remains a distinct mathematical obligation and could in principle be a nontrivial certificate class. No finite level, candidate witness, exact dual decomposition or native program for it is supplied/admitted here.

This distinction is also why the old bare-Bose result `Q_N(W)>=0 iffW>=0` does NOT already prove C25. The old123-LF source was read COMPLETE including its ending and explicitly excluded PPT strengthenings from its theorem. The NEW controls above establish only the TWO precisely specified weaker-PPT obstructions, without editing that source or silently broadening it to allPPT extensions.

The1/(kN) negative scaling is compatible with limiting separability hierarchies whose auxiliary-lifted separable minimum is0: values can stay strictly negative at every finite level and approach0 from below. No source limiting theorem or symmetry reduction is called false. An equivalent objective-preserving auxiliary twirl preserves a feasible control's expectation/PSD/PPT/support, but no non-equivalent twirl or relaxed support condition is assumed.

## Z6. Operational and original-problem residual

This is an unrestricted-in-W/rho/k/d/N certificate-cone barrier, NOT an unrestricted statement about physical4x4 PPT Schmidt number. Neither class A nor class B can supply the requested physical PPT/SN3 negative pair at ANY finite level. To evade both while retaining this auxiliary lift requires the genuine Bose-plus-proper-Bob-PPT strengthening, not merely a larger N, a new target state, or a permutation-invariant relaxation mislabeled Bose.

The historical N4 outcome remains UNKNOWN/incomplete with unestablished child exit/resource history; it is not rerun, repaired or certified by this theorem. Old21, withdrawn arithmetic, process/cadence and root/source/freeze corrections remain. No input/program/checker was launched and no new GO or resource admission follows.

**Original P44 remains UNMET:** no explicit rational4x4 PPT/SN>=3 state with an actual universally complex-SR2-nonnegative STRICT negative separator; no truly unrestricted all4x4 PPT=>SN2 theorem. C18 closes only its proper source witness formula, C23 only its state domain, C24 only its linear-range certificate mechanism, and C25 only the two weak finite extension cones. General inside-range/moment witnesses and genuinely stronger full-PPT Bose certificates are not classified by these barriers.

All proof imports are ordinary finite complex PSD/rank/isometry algebra, tensor trace/Bell contraction, local partial transpose and closed-cone duality, with every specialized control supplied inline. No old native output, solver tolerance, certificate replay, product sample, source hash or external quantum theorem is an opaque premise. Formal/kernel/executable/triple/human/configured-family/novelty/SOTA/publication acceptance remains separate and unperformed. Whole new gates require all actual parts/overlays/endings; no source hash substitutes for reading. Original18/cutoff/deadline unchanged; not a terminal park or round closeout.

**END OF COMPLETE CURRENT v9 PART7/7.**
