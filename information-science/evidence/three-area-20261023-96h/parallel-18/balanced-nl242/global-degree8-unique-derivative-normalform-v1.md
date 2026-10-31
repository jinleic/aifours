# Global balanced-NL242 representation: degree8, one exceptional derivative direction, and a literal high-ANF normal form

Owner InfoBalancedNL242-2. Actual `/bin/date` observation before this write: **Mon Oct 26 05:17:25 PDT 2026**. Original balanced nine-variable problem, not just rank2. **WRITTEN CANDIDATE**, no parent/reviewer acceptance, formal/kernel/finite replay or novelty claim. Exact symbols/fractions/integer products only; no scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/CLI/nested agent or GO.

This is an additive NEW all-residue representation, not a count-table update or a claimed global exclusion. It preserves one actual Boolean function throughout. The already supported CASE32/unpruned U2 result remains CONDITIONAL at FULL J_U2/E116/etc and is consumed only in the separately labelled optional consequence §6. It does not become an all-residue pruning theorem.

## 1. Target, existing inputs and new conclusion

Let f:F2^9->F2 be balanced, weight256, with EVERY Walsh coefficient bounded by28. Walsh is unnormalized. Let s be the XOR of its support, as an INPUT vector. Existing elementary balanced/Parseval reasoning gives s!=0. The canonical odd-half residue theorem gives positive polar rank for the intrinsic quadratic on s-perp; a direct reminder appears in §5.

The NEW written bridge proves:

1. f has algebraic degree EXACTLY8. Its nine degree8 ANF coefficients are precisely the coordinates of s.
2. There is EXACTLY ONE nonzero direction with derivative degree at most6, namely s. Its derivative has degree EXACTLY6. Every other nonzero direction has derivative degree EXACTLY7.
3. After actual invertible affine INPUT changes, f has the literal form

```text
f(x,t)=P8(x)+t C_r(x)+rho(x,t),   degree(rho)<=6,
P8(x)=x1 x2 ... x8,
C_r(x)=sum_(j=1)^r product_(i notin{2j-1,2j}) xi,
1<=r<=4.                                                (NF)
```

Here2r is EXACTLY the polar rank of the intrinsic quadratic. Its affine part/weight remains coupled to the SAME rho; those data are not chosen independently. No output operation that might destroy balance and no preselected truth-table half are used.

Every choice of binary ANF coefficients rho defines ALL512 Boolean bits literally. This removes the 'independent realizable spectra later glued together' pitfall, but does NOT assert existence of a rho meeting balance and the512 Walsh inequalities. That lower-degree feasibility/structure is the residual, not an executed search.

## 2. Degree8 coefficients ARE the support-XOR vector

Write f's unique multilinear ANF. The degree9 coefficient is the XOR of all truth values, which is0 since weight256 is even. For each coordinate i the coefficient of the degree8 monomial missing i is

```text
sum_(x_i=0) f(x) mod2
 = wt(f)+sum_x x_i f(x) mod2
 = s_i.                                                  (1)
```

This is the ANF coefficient formula on the coordinate hyperplane, not a fit to a spectrum. Thus s!=0 forces degree8 EXACTLY. It also specifies its entire top homogeneous part, not just a degree lower bound.

Choose an actual linear input basis with s=e_t and x in F2^8. Formula(1), recomputed in this basis, gives

```text
f(x,t)=g(x)+t h(x),
g(x)=P8(x)+g_le7(x),    degree(h)<=6.                      (2)
```

All other degree8 terms contain t and vanish because their corresponding s-coordinate is0. The t-dependent term has degree at most7 globally. The derivative along s is exactly h; no truth-table slice has been fixed in advance.

## 3. Intrinsic quadratic polar = the dual degree6 derivative tensor

Use the SAME g,h in(2) and define the actual ternary function

```text
e(x)=(-1)^g(x) (1-h(x)),
R(a)=W_f(a,0)=2 H8 e(a).
```

Here h is its actual0/1 Boolean value, not an unrelated sign stream. Balance gives sum e=0. Mod2, e=1+h. Since degree(h)<=6, the sum of `(1+h)x_i` over all8 input bits is even (its degree is at most7). Therefore each integer moment M_i=sum e(x)x_i is even.

Expanding the actual character as product_i(1-2a_i x_i) gives

```text
H8 e(a) = sum e -2 sum_i a_i M_i
          +4 sum_(i<j) a_i a_j M_ij + multiples of8,
M_ij=sum_x e(x)x_i x_j.
```

Hence H8 e is divisible by4 for EVERY a, and

```text
Q(a)=R(a)/8 mod2
    =sum_i ell_i a_i +sum_(i<j) m_ij a_i a_j,
ell_i=-(M_i/2) mod2,   m_ij=M_ij mod2,   Q(0)=0.           (3)
```

The linear coefficients are actual SIGNED integer half-moments, not free offsets.

For the quadratic coefficients, e mod2=1+h and the full-cube x_i x_j sum is even. Thus

```text
m_ij=sum_x h(x)x_i x_j mod2
    = ANF_coefficient_(product_(k notin{i,j}) x_k) h.       (4)
```

To justify the last equality without a computational moment table: summing a Boolean polynomial over8 variables extracts its degree8 coefficient. In h*x_i*x_j, with degree(h)<=6, the ONLY monomial that can cover all8 variables is the degree6 monomial missing exactly i,j. All lower monomials miss a coordinate. Equations(3)–(4) prove the literal polar/derivative correspondence.

The Q here is precisely the intrinsic `W_f/8 mod2` on s-perp. Multiplying R by the canonical affine sign does not change this parity. Thus its polar alternating matrix has rank2r and is exactly the coefficient tensor dual to h's degree6 part. This is a direct source-level Boolean bridge, not an import of any finite corpus or older classification table.

## 4. Canonical top ANF and the UNIQUE exceptional derivative direction

An alternating form over F2 admits a symplectic basis. Make the corresponding invertible LINEAR input change on x (contragredient to the frequency basis). Equation(4) then puts h's top degree6 part into C_r in(NF). P8 is still the unique degree8 monomial with coefficient1; the linear change may create lower-degree terms, which are retained.

Write the resulting degree7 part of g as

```text
g_7(x)=sum_i c_i product_(j!=i) x_j.
```

Translate x by the actual vector c. In P8(x+c) the degree7 coefficients are precisely c_i; the degree7 part of g_7 is unchanged by translation. They cancel overF2. Lower terms remain lower. This translation does not change h's degree6 part, nor balance or Walsh magnitudes. Thus

```text
g=P8+g_le6,   h=C_r+h_le5,
f=P8+t C_r+[g_le6+t h_le5],
```

which is exactly(NF). Input translations preserve s because wt(f) is even. We have not independently normalized two halves or removed Q's coupled affine part. The same actual polynomial defines every bit.

Now let v=(u,v_t) be a nonzero input direction. If u!=0, the degree7 part of the Boolean derivative D_v f is

```text
sum_i u_i product_(j!=i) x_j,
```

which is nonzero because these degree7 monomials are independent. All derivatives of the degree<=7 remaining part have degree<=6. Hence degree(D_v f)=7 for EVERY v not in span(s).

For v=s, D_s f=h=C_r+h_le5. As soon as r>0, C_r is nonzero, so degree(D_s f)=6. Since the only nonzero vector in span(s) is s, this proves the unique-direction theorem. It does not claim that any other directional derivative has small Walsh peak or that a degree profile alone excludes f.

## 5. Why r>0: retain the actual paired-capacity proof boundary

This is existing canonical-residue mathematics, not a new novelty claim. Both actual halves in the s-adapted split have odd weight. Canonically sign their spectra K1,K2, retaining their actual affine phases, and set S=K1+K2,Rc=K1-K2,D=J1+J2. Canonical phases identify D with the Q in(3). Let d=wt(D), chi=(-1)^D and Gamma=sum chi*S.

The exact pointwise canonical possibilities give T=chi*S in{-28,-12,4,20}, so T²+8T<=560. Also Rc²<=256+320D. The two genuine Boolean Parseval identities therefore give

```text
Gamma<=40d-6656.
```

If the polar rank were0, chi is an affine character and the genuine transform of S has values0,+512,-512, hence |Gamma|<=512. An affine D has weight0,128 or256. The first two violate the displayed bound (at128 the right side is-1536); the last would be constant1, contradicting Q(0)=0. Thus r>0. No old signed-eight support enumeration is used for this particular positive-rank implication.

More generally the same published/named ordinary quadratic normal form gives `|Gamma|<=512*2^r` and the familiar bound `40d>=6656-512*2^r`. The full roster and all transitive assurance qualifications remain those of the actual canonical proof; this manuscript does not pretend to newly settle other residue types or remove older ledger imports from an accepted union.

For completeness s!=0 also has an elementary independent route. If s0, all balanced Walsh coefficients are divisible by8. Their next parity W_f/8 mod2 is quadratic by the support-moment expansion. Its value at0 is0, so the nonzero quadratic1+q has at least128 ones. At those coefficients the cap forces magnitude<=16, elsewhere<=24, giving Parseval upper bound253952<262144. This is the original standard obstruction, not the unrestricted covering-radius preprint imported as a theorem.

## 6. Conditional use of the completed proper-type result — NO global promotion

At r1 the ordinary paired-capacity bound and quadratic weight list force d192. The already delivered unpruned rank2 U2 proof therefore excludes r1 **ONLY CONDITIONALLY at FULL J_U2**, with mandatory M1/M2, E116/graph/canonical/pruning/Boolean and historical named boundaries retained. No new smaller dependency union is asserted because(NF) gives a direct ANF description.

This leaves r2/r3/r4 as the genuine next normal-form classes in THIS representation, not a claim that every other original proof gap has been accepted. Weight/Arf/radical-linear distinctions of Q still belong to its SAME rho via(3). I do not infer any global numerical NL bound, another residue-type elimination, or unconditional original solution from the conditional r1 gate.

The old `(4,128)` exclusion and any other old computation/reviewer claims are NOT newly consumed or authenticated here merely because selection-v1 cites them. All current assertions are limited to the fully displayed ANF bridge and named paired-capacity premise. No old finite table or unadmitted arithmetic output is a new correctness input.

## 7. Concrete residual and continuing attack, not an early park

(NF) is a COMPLETE high-degree normalization for ANY original target, and conversely every binary coefficient array rho defines one literal Boolean function in that form. It is not a satisfying assignment. The remaining task is to prove a uniform obstruction or find an actual rho with:

```text
sum_(x,t) (-1)^[P8(x)+t C_r(x)+rho(x,t)] =0,
|sum_(x,t) (-1)^[P8(x)+t C_r(x)+rho(x,t)+a.x+b t]|<=28
for EVERY a,b.
```

All balance, common-coordinate and both-half Boolean conditions remain. There is no independent spectrum or count model whose pointwise pieces are silently declared compatible. The affine part of Q, its allowed weights, actual zero set and all phase constraints must be obtained from this same rho.

The NEXT unproved structural step is a useful uniform constraint on the degree<=6 correction relative to the canonical degree6 derivative tensor C_r for r2/3/4. A coefficient count, a claim of generic emptiness, another already-covered sparse-defect profile, or a solver non-find is not that step. No coefficient enumeration, program or assay is authorized. Original research continues under the same deadline; this source is a parkable incremental representation, NOT terminal completion.

## 8. Source pins, process and assurance

Actually read before this manuscript: original selection, the complete paired-distance proofs, remaining-type round2 source, own modular-saturation representation and relevant sparse-defect/composition bodies. The finite archived computations mentioned in those sources were not replayed or re-credited.

- selection-v1.md: `26b94d67d87778c8630b04bfe2b86ce105377517c7c72b449eb5539eac49d84b`.
- modular-saturation-protocol-v1.md: `d485c6da50c7c4c19b86ad198c7d0b6018c95334ac6a0164784b763e7091e032`.
- hard-continuation-20261015/quadratic-distance/PROOF.md: `caf7db55c93a6b3fc73d461fd4dc018f387ec510adf29417605ee4e3e71730b5`.
- hard-continuation-20261015/quadratic-distance/SHARPER.md: `bfd1cea494b42f7c016cbf174772940dff4afaf2460735779e299ab095f44601`.
- Later NONESSENTIAL canonical-odd-J2-written-interface-addendum-v1.md: `ec1d0b56b5b626d957f872d29bb9c4d98a050adb6dd7ee2429ea0d86d5cad3fb`; not silently inserted into an older freeze or assigned inherited acceptance.

The original target is exactly the balanced512-bit problem in selection; no hidden fixed half, affine-frequency zero relocation, corpse/corpus restriction or all-state pruning is imposed. Ordinary ANF Möbius coefficients, finite character expansion, symplectic basis and canonical paired-capacity facts retain ordinary WRITTEN status. Novelty/priority is UNCLEAR; no historical-source/full-DAG/kernel/human/family/finite-triple gate follows.

Whole primary resumption ACK027 was ACTUALLY SENT before these new source reads/reasoning. Own v112 private-written exactness MAJOR/entire withdrawn scout ZERO guidance, separate15->14 count qualification, older cadence/v105 false quotation and all parent/owner process/admission findings remain permanent. The RQLS scout is not an input or guidance to this unrelated Boolean representation. No approximate private magnitude annotations or scientific execution occurred for the current ANF derivation. No global clean-cognition/runtime/history census. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early round/owner closeout.
