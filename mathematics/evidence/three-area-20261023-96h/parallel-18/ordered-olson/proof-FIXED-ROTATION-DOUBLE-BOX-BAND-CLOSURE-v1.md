# Fixed rotations and two Boolean boxes: candidate closure of the entire R=p+1 band

Actual returned clock before scope freeze and this manuscript: **Sun Oct 25 04:21:14 PDT 2026**. Owner MathOlson-2, slot math-2. **AUTHOR-WRITTEN CANDIDATE; fresh independent reconstruction and parent disposition NOT PERFORMED.** This is not formal/kernel verification, a novelty clearance or an accepted round result. The exact scope, exposure and pre-freeze reasoning are in `selection-fixed-rotation-double-box-v1.json`.

No scientific arithmetic, interpreter, enumeration, symbolic computation, solver or replay was used to check this argument. The six earlier exploratory kernel calls are preserved, with no verification credit, in `arithmetic-authority-correction-addendum-v1.json`; none evaluated this argument. After Main withdrew the blanket eval exception, work has been written mathematics and metadata only. All pinned predecessors remain unchanged.

## 1. Full theorem and relationship to L_RES

Fix any prime p>=7. Work in

    D_(2p)={(v,e):v in F_p, e in {+1,-1}},
    (v,e)(v',e')=(v+e*v', e*e'),
    rho_x=(x,+1), sigma_y=(y,-1).

**Theorem DB (candidate).** Every actual word w with exactly

    R=p+1 rotation occurrences,
    F=3p-2 reflection occurrences,
    N=R+F=4p-1

has an identity selection of exactly 2p original positions in their original increasing order.

All values, including zero rotation values, all type orders and all rotation-gap lengths are included. There is no raw-matching assumption, no one-endpoint condition, no all-odd-block or normal-form assumption, and no old-caller exclusion in this theorem.

Consequently, if the proof is correct, every member of the ENTIRE actual lower residual in `consolidated-lower-band-v1.md`, with all retained OLD/REF/SEL/IPGEN/GS/DS3 failures, has the required identity2p selection. This proves the **identity-selection version of L_RES by a separately proved actual selector**, and closes the whole lower raw-matching branch <=p-3. It does **not** assert that the identity lies in a maximum-matching packet family. The stronger L_MAX remains false, and the packet-only residual statement is unnecessary and is not proved here.

This still does not address the remaining other R bands, unrestricted prime-dihedral ordered Olson, or the book's all-finite-group question.

## 2. Elementary signed-box facts

All polynomial coefficients and sums below are over F_p. Boolean points are still the actual integers 0 and 1, viewed in the field when evaluated.

**Lemma B1.** If H in d variables has total degree <d, then

    sum_(a in {0,1}^d) (-1)^(a_1+...+a_d) H(a)=0.

**Proof.** Each monomial of total degree <d omits a variable. Pair the two Boolean points that differ only in that variable. The monomial values agree and the signs are opposite. Linearity proves the assertion. QED.

**Lemma B2.** If H in d variables has total degree <=d, then

    sum_(a in {0,1}^d) (-1)^(a_1+...+a_d) H(a)
      =(-1)^d [u_1 ... u_d] H.

Here the bracket denotes the coefficient of the displayed squarefree monomial in the ordinary polynomial, before any Boolean reduction.

**Proof.** A monomial omitting any variable cancels as in B1. A monomial containing every variable and having total degree <=d must have each exponent exactly one. Its Boolean signed sum is (-1)^d, since its value vanishes except at the all-one point. QED.

Both lemmas hold in F_p directly. No counting theorem or unproved inverse result is imported.

## 3. Actual cyclic word and reflection-colour parametrization

Choose one named actual rotation occurrence r_0. Make a cyclic cut just after a reflection preceding its rotation gap. List the cut word as

    X_1 f_1 X_2 f_2 ... X_F f_F,
    f_t=sigma_(y_t),

where X_t is the actual list of rotations between f_(t-1) and f_t, and r_0 belongs to X_1. Gaps may be empty or contain several rotations. This cut changes no occurrence, value or relative cyclic order. Section 9 restores the same selected positions to original linear order.

Let the other p named rotation occurrences be r_1,...,r_p, with respective values x_1,...,x_p. Let x_0 be the value of r_0. For each rotation r, let g(r) be its actual gap index in {1,...,F}. Thus g(r_0)=1. Several rotations are allowed to have the same g(r).

Introduce the F-1 Boolean variables

    u_2,...,u_F,  with u_1=u_(F+1)=0.

For a fixed subset K of ACTUAL rotation occurrences, select all rotations in K, no other rotations, and select reflection f_t exactly when

    u_t != u_(t+1).

The reflection selection has even cardinality: it is the number of colour changes around a cycle whose initial and final colour are both zero. The reflection selection determines all u_t uniquely by successive recovery from u_1=0. In particular, no reflections are selected iff all variables are zero. This is a parametrization of actual selected occurrences, not a virtual word or an insertion of fictitious identity letters.

We will use only even-cardinality K. The total selected size is then even.

## 4. Exact product and size for fixed K

Write k=|K| and define the integer polynomial

    Z_K(u)=k+sum_(t=1)^F (u_t+u_(t+1)-2u_t*u_(t+1)).       (1)

At every Boolean point this is exactly the actual selected size. Its degree is at most two, and its homogeneous degree-two part is

    Z_2(u)=-2 sum_(t=2)^(F-1) u_t*u_(t+1).                 (2)

In particular Z_2 is independent of K, k, the rotation values and gap multiplicities.

The number of selected reflections before any occurrence in gap t, or before f_t, has parity u_t. Therefore each selected rotation in X_t contributes (1-2u_t)*x to the product coordinate. The reflection f_t contributes y_t times

    (u_(t+1)-u_t),

because this is zero if f_t is omitted and equals (-1)^u_t if f_t is selected. Summing and using the two boundary zero colours gives

    sum_(t=1)^F (u_(t+1)-u_t)*y_t
      =sum_(t=2)^F (y_(t-1)-y_t)*u_t.

Thus the actual selected ordered product is the rotation rho_(V_K(u)), where

    V_K(u)=sum_(r in K) x_r
            +sum_(t=2)^F (y_(t-1)-y_t)*u_t
            -2 sum_(r in K) x_r*u_(g(r)).                (3)

The convention u_1=0 applies to every rotation in X_1. This formula follows directly from the displayed group law and selected-reflection prefix parity. Selected rotations do not change that parity. No selected factors have been commuted through reflections.

Let the homogeneous degree-one part in u be

    L_K(u)=sum_(t=2)^F (y_(t-1)-y_t)*u_t
             -2 sum_(r in K) x_r*u_(g(r)).               (4)

Adding or removing the named rotation r_0 changes the constant term of V_K, and changes k in Z_K, but changes NEITHER L_K NOR Z_2, because g(r_0)=1 and u_1=0. This precise highest-colour independence is the parity bridge needed below. It does not assert that actual selected products or sizes are unchanged by that addition.

## 5. The first box at its exact degree boundary

Put

    M=F-1=3p-3=3(p-1),
    Q_K(u)=(1-V_K(u)^(p-1))*(1-Z_K(u)^(p-1)).             (5)

Fermat's identity says that at a Boolean point Q_K is exactly the indicator of

    V_K(u)=0,  Z_K(u)=0 mod p.

Also deg_u Q_K<=3(p-1)=M. Only its term V_K^(p-1)*Z_K^(p-1) can contribute homogeneous u-degree M. The degree-one and degree-two parts in (4) and (2) give the exact equality

    [u_2 ... u_F] Q_K
      =[u_2 ... u_F] L_K^(p-1)*Z_2^(p-1).                (6)

Every use of a constant term of V_K, or a term of degree below two from Z_K, lowers total u-degree below M. The remaining two terms in the expansion of Q_K have degrees at most p-1 and 2p-2, also below M. Thus no dependence on k or the constant contribution of r_0 is hidden in (6).

By B2 and the fact that M is even,

    sum_(u in {0,1}^M) (-1)^(sum u_t) Q_K(u)
      =[u_2 ... u_F] L_K^(p-1)*Z_2^(p-1).                (7)

This equality is at the boundary deg=M, NOT an unjustified strict-degree cancellation. That distinction is why the second box is necessary.

## 6. Consequences of hypothetical failure of the entire actual word

Suppose, for contradiction, that w has no original-order identity2p selection. By the cyclic-conjugation bridge in section 9, its chosen cut word has none either.

For any even K, every selection in sections 3-4 has even size between 0 and N=4p-1. A positive such size divisible by the odd prime p must be exactly 2p: the possible multiples p and 3p are odd, and 4p exceeds N. Its product is already a rotation. Hence the conditions indicated by Q_K give an actual identity2p selection unless the selected size is zero.

If K is nonempty and even, its selected size is at least two. Under the contradiction hypothesis,

    Q_K(u)=0 for every Boolean u,  for every nonempty even K.   (8)

If K is empty, no reflections are selected only at u=0. At that point both V and Z are zero. Every other indicated point would give the forbidden identity2p. Therefore

    Q_empty(0)=1,
    Q_empty(u)=0 for every other Boolean u.                   (9)

Consequently the left side of (7) is zero for every nonempty even K and is one for K empty. There is no comparison with an odd-cardinality K or an odd selected word in this argument.

## 7. The second box: p rotation statuses but degree at most p-1

Introduce p new formal variables z_1,...,z_p and define

    L(z;u)=sum_(t=2)^F (y_(t-1)-y_t)*u_t
              -2 sum_(i=1)^p z_i*x_i*u_(g(r_i)),

    G(z)=[u_2 ... u_F] L(z;u)^(p-1)*Z_2(u)^(p-1).       (10)

This is an ordinary polynomial over F_p with

    deg_z G<=p-1.                                          (11)

Taking a coefficient in u does not increase total degree in z. Repeated gap indices and zero x_i do not invalidate (11); they can only remove dependencies. No multilinearity assumption is needed.

For an ACTUAL subset A of {r_1,...,r_p}, choose the even actual rotation subset

    K(A)=A                         if |A| is even,
    K(A)=A union {r_0}              if |A| is odd.          (12)

Then K(A) is empty exactly when A is empty; otherwise it is nonempty and even. The largest possible size is p+1, so all these are legitimate actual occurrence selections.

Let 1_A be the Boolean status vector of A. Because r_0 lies in the fixed zero-colour gap, equation (4) gives

    L_(K(A))(u)=L(1_A;u).                                  (13)

Its contribution to the CONSTANT part of V and to the CONSTANT size k is deliberately ignored ONLY after the exact highest-u coefficient calculation (6). There is no substitution of a nonlinear parity function into a low-degree polynomial.

Combining (7)-(10) with (12)-(13), the hypothetical failure of w forces

    G(0,...,0)=1,
    G(1_A)=0 for EVERY nonempty A subset {r_1,...,r_p}.     (14)

But by B1 applied to the p z-variables and degree bound (11),

    sum_(z in {0,1}^p) (-1)^(z_1+...+z_p) G(z)=0.         (15)

The values in (14) make that same sum equal to one. Thus 0=1 in F_p, a contradiction.

This proves existence of an actual identity2p selection in the cut word. No packet endpoints, virtual midpoint or necessary-only inverse profile have entered the argument.

## 8. What the existence argument actually selects

The contradiction establishes that for at least one even actual K, some actual Boolean reflection-colour point u has V_K(u)=0 and Z_K(u)=2p. Its selected rotations are precisely K, and its selected reflections are precisely the colour-change occurrences f_t. They are distinct original word positions, and equation (3) is their product in the actual order.

On a REF-avoiding residual word K cannot be empty. It is therefore a genuine mixed identity2p selection, with some even rotation count between 2 and p+1. The proof is not a claim that the two-rotation branch alone always works, or that a maximum-matching packet family contains this selection. It supplies the separate actual selector allowed in the recorded identity-selection L_RES obligation.

No execution or search is required for the existence theorem. A computational extraction procedure, a formal proof and a complexity claim are not supplied or asserted.

## 9. Restoration to original linear order

Write the original word as AB and the selected cut word as BA. Let P_A and P_B be the products of the selected named occurrences in their respective original portions. Identity on the cut means

    P_B*P_A=1.

Then

    P_A*P_B=P_B^(-1)*(P_B*P_A)*P_B=1.

The same named occurrence subset therefore has identity product in increasing ORIGINAL index order. Its cardinality is unchanged and remains exactly2p. This completes Theorem DB.

## 10. Source credit, independence and remaining gates

The first colour parametrization, the summation-by-parts coordinate and the Fermat/signed-box mechanism are explicitly adapted from the old `mathematics/evidence/six-lane-20261016/olson/proof-theoremP.md`, freshly observed SHA256 `58a85ebeba8208e2f89b39a691235d2d1374656d8888ea905fe96aa75e1dafc2`. They are re-derived here rather than importing its historical computation, sharpness remarks or prime-power extensions.

The change is to FIX an arbitrary even actual rotation subset instead of dropping all singleton rotations, retain the EXACT highest-colour coefficient when F=3p-2, and use one actual initial-gap rotation to close the parity of the other p statuses. This gives a second strict-degree box cancellation. It is not the dead maximum-matching packet-lift route.

No S(p), Lev, EGZ, Davenport constant, index-one, inverse normal form, grammar completeness or historical scientific output is a premise. The direct theorem includes all band words and therefore implies the original residual conclusion without needing to accept the old exclusions as facts about every word. The old residual remains unchanged as a definition and no strict provider-difference, nonempty residual or novelty claim is made.

The earlier six kernel diagnostics do not check (6), (13) or the double-box contradiction and supply NO verification credit to this packet. Required next gate: a fresh written reconstruction of the entire proof, especially actual parity/size, the top-degree equality (6), the r_0 independence used in (13), and the two different box identities. Parent acceptance has not been obtained merely by creating this manuscript.
