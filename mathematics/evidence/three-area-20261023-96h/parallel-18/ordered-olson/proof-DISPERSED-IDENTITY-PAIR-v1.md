# Two dispersed identity rotations close the lower-band zero branch

Observed before exclusive creation: **2026-10-23T14:47:52-0700 PDT**. MathOlson-2, math-2. **CANDIDATE written actual-word selection theorem.** This is not another single-profile classification: it directly constructs a nonempty selection through a complete Boolean-box proof and removes a named whole-word branch. No scientific execution. It does not solve the remaining nonzero/concentrated or lower-matching classes.

## 1. Exact theorem and baseline comparison

**Theorem Z2.** Let p>=7 be ANY prime. Let w be an ACTUAL word over D_(2p), with original length N<=4p-1, at least F>=3p-2 reflection occurrences, and at least TWO ACTUAL identity-valued rotation occurrences rho_0. Then w has EXACTLY2p positions in increasing ORIGINAL index order whose ordered product is the identity.

The two identity rotations need not be adjacent, in one rotation gap, in one constant block, or near equal reflections. All other rotation and reflection values/interleavings are arbitrary. There is no paired alphabet, all-odd block, normal-form or nonzero assumption.

At the assigned lower band R=p+1,F=3p-2,N=4p-1, this gives the direct necessary survivor bound

    v_0<=1,                                               (1)

where v_0 is the ACTUAL multiplicity of rho_0 among rotations. Zero-containing words are not silently discarded: words with two zeros are removed by a proved actual-word selection, while the entire zero-free AND exactly-one-zero remainder stays in scope.

**Baseline and priority:** this reuses the signed Boolean-box/linear-product/quadratic-size mechanism of the old complete Theorem P proof, read with both operative errata. P's printed sufficient statement pairs rotations WITHIN individual gaps; it does not explicitly license a pair of dispersed identities. The previous current `proof-UNIFORM-RESIDUAL-PARTIAL-v1.md` IDPAIR criterion required2p-2 identity rotations when F>=p+1. That different all-count criterion is retained, not misquoted as needing only two. A targeted source-tree search did not locate the exact dispersed-two-identity statement; that search is NOT a novelty or complete-provider certificate. The complete new specialization is proved below without importing P itself, S(p), Lev, EGZ, Davenport, index-one or a scientific computation.

## 2. Parametrization by actual occurrences

Use the actual group law

    (v,e)(v',e')=(v+ev',ee'),
    rho_x=(x,+1), sigma_y=(y,-1).

Cyclically cut the ACTUAL word just after a reflection, so it ends at a reflection and has the representation

    X_1 f_1 X_2 f_2 ... X_F f_F,

where f_t=sigma_(y_t), and X_t is the actual rotation gap preceding f_t. This is only a cut, not a rearrangement. Fix two distinct actual rho_0 occurrences z_1,z_2, wherever their gaps lie. All rotations other than these two will be unselected in this proof.

Introduce Boolean variables

    u_2,...,u_F, m;  u_1=u_(F+1)=0.

There are

    M=(F-1)+1=F>=3p-2                                    (2)

independent Boolean variables. For a parameter point define an ACTUAL selection:

* f_t is selected iff u_t!=u_(t+1);
* BOTH z_1,z_2 are selected iff m=1; neither is selected if m=0;
* every other rotation occurrence is unselected.

The selection is in the word's actual cut order. Its selected reflection count is even, since it counts color changes around the cycle u_1,...,u_F,u_1. Its total selected count is also even because the identity pair contributes2m.

The map from parameters to actual selected occurrence sets is injective. Given the selected reflection indicators, recover u_(t+1)=u_t XOR[f_t selected] recursively from u_1=0, recovering ALL u_t. Whether the two fixed identity positions were selected recovers m. In particular the EMPTY selection occurs ONLY at the all-zero parameter point.

These statements do not require the selected identity positions to be adjacent. Identity elements have no product effect at ANY of their actual positions.

## 3. The product coordinate is still LINEAR

On Boolean points put c_t=(-1)^(u_t). Before f_t the number of selected reflections has parity u_t, because u_1=0 and each selected prior reflection toggles the color. Identity rotations do not affect product or parity. The selected product has parity+1 and coordinate

    V=sum_(t:f_t selected)c_t y_t.

For Boolean u,

    c_t [u_t!=u_(t+1)]=u_(t+1)-u_t.

This can be checked in the four Boolean cases; it is an exact F_p identity. Therefore, by telescoping with u_1=u_(F+1)=0,

    V(u,m)=sum_(t=1)^F (u_(t+1)-u_t)y_t
          =sum_(t=2)^F (y_(t-1)-y_t)u_t.                  (3)

Thus V is a polynomial of degree AT MOST1, possibly identically zero, and is independent of m. An actual selection has identity product exactly when V=0, since its reflection parity is even.

No noncommuting selected terms were reordered: the signs came from their actual selected-reflection prefixes; the selected rho_0 terms are literally identities.

## 4. The selected size is QUADRATIC and bounded

The integer polynomial

    Z(u,m)=sum_(t=1)^F
             (u_t+u_(t+1)-2u_tu_(t+1))+2m                (4)

equals the selected cardinality on Boolean points. It has degree at most2, is always EVEN there, and is at most the actual N<=4p-1. Its value0 as an integer means the empty selection, already uniquely identified above. We will use its reduction modulo p only in the next finite-field argument.

## 5. Complete signed Boolean-box proof

For any polynomial Q over F_p in M variables with total degree<M,

    sum_(b in{0,1}^M)(-1)^(wt(b))Q(b)=0 in F_p.          (5)

**Proof of (5).** Every monomial of total degree<M omits some variable. Summing first over that variable pairs identical monomial values with opposite signs and cancels. Linearity proves the polynomial identity. No executable enumeration, prime-parameter test or stronger Chevalley-Warning theorem is being imported.

Apply (5) to

    Q=(1-V^(p-1))(1-Z^(p-1)).

By (2)-(4),

    deg Q<=3(p-1)=3p-3<M.

Fermat's little theorem on each Boolean point gives Q(b)=1 exactly when BOTH V(b)=0 and Z(b)=0 modulo p, and Q(b)=0 otherwise. Hence

    sum_(b:V(b)=Z(b)=0 modp)(-1)^(wt(b))=0 in F_p.        (6)

The all-zero parameter point contributes+1. Thus another parameter point must have V=Z=0 modulo p; otherwise (6) would say1=0. Injectivity/unique emptiness makes its actual selected word NONEMPTY. Its actual selected size is a positive EVEN integer, is divisible by the ODD prime p and is below4p. The only possibility is EXACTLY2p. Its even-reflection product has coordinate V=0, hence is identity. This proves the cut-word claim for ACTUAL positions.

Restore original order: write the original word AB and the cut word BA. If P_A,P_B are the selected products of the two original portions, then P_B P_A=1 implies P_A P_B=P_B^(-1)(P_B P_A)P_B=1. The same actual selected2p positions therefore have identity product in increasing ORIGINAL order. QED.

## 6. Consequences for the ACTUAL current frontier

### 6.1 All-zero-free critical branch is removed, not assumed away

The critical cross-K paper `proof-CRITICAL-MATCHING-FREE-ROTATION-RIGIDITY-v1.md`, pin **19c8063b37d160d798a89e4e1ace14075a31c6046bd3eaadd9266979b745879e**, has at least THREE actual free rotations at any p-2 raw matching. Its first alternative was that all those free rotations have value0. That gives at least three actual identity rotations, so Z2 supplies a complete actual identity2p selection. Thus that alternative is CLOSED by this theorem, whether or not its profile obeys other local constraints.

This consequence uses the earlier paper only to identify the named branch and its actual count. Z2 itself is self-contained and does not import an unreviewed rigidity theorem as a proof premise.

### 6.2 Sharpened flat-gap bookkeeping, with exactly-one-zero retained

The two-free-controls paper derives on the actual residual

    2kappa+e_F<=p-4+Z_0,

where kappa=p-1-sum floor(ell_i/2) and e_F count ACTUAL constant reflection blocks, not terminal-NF data, and Z_0 counts ACTUAL identity rotations flanked by equal reflections. Since Z2 gives Z_0<=v_0<=1, surviving words obey

    2kappa+e_F<=p-3.                                    (7)

If no rho_0 occurs, retain the sharper old right side p-4. If one occurs but is not flanked by equal reflections, Z_0=0 also. The exactly-one-zero/equal-neighbor case is retained with Z_0=1; it is NOT silently made zero-free.

At p=7 and the separately stated old-trust odd-block floor o_F>=p+2 (hence actual kappa>=1), the zero-free or Z_0=0 residual is kappa=1,e_F<=1; the Z_0=1 residual is kappa=1,e_F<=2 OR kappa=2,e_F=0. These are only necessary actual count possibilities at their explicit import trust, not feasible/avoiding classifications or a full D_14 result. No parameter enumeration was executed; the inequalities are direct two-case integer consequences of (7).

### 6.3 A reflection-only disjunction, not a stronger unsupported theorem

For any reflection-only word of length3p-2, insert two actual identity rotations, apply Z2 at total length3p<=4p-1, and remove them from the selected product if used. The resulting original reflection word has an identity selection of length EITHER2p OR2p-2. This disjunction is a valid written consequence. It does NOT assert that length2p-2 alone always occurs. The current band additionally removes REF, so in its no-reflection-only case the Z2 proof necessarily uses both identity rotations and supplies exactly2p-2 actual selected reflections.

## 7. Exact residual and verification boundary

Keep ALL the current actual lower-band residual data and provider tests. After removing the proved Z2 class, v_0<=1 is DERIVED. For raw matching p-2, only the nonzero free-pair/one-arc alternative remains from the queued rigidity packet, still carrying every activation, filler, cut and exact offset constraint. Lower raw matching<=p-3 also remains, with arbitrary nonzero rotation values and the exactly-one-identity case fully retained.

No length4p-1 counterexample, nonempty residual, full-band theorem, unrestricted prime-dihedral or all-finite-group Olson result is claimed. This proof closes the actual TWO-IDENTITY-ROTATION class and one named zero branch, not the remaining entire MIX obligation. It is a direct extension of the old P mechanism, not a new probability/algebra theorem or a novelty certificate.

This is a complete frozen written argument. Its new dispersed-pair use needs an actual separate reconstruction and parent check; earlier peer returns on gauge/deeper-switch do not certify this snapshot. No scientific program, enumeration, solver, compilation, old native job/checker, Lean/kernel or model CLI was run. Metadata hashes are byte identities only. Historical S(p)/Lev/classical/source/process limitations remain unchanged wherever earlier residual comparisons use them.
