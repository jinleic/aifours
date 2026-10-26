# Addendum 4 — exact nonuniform compensation; quasiuniform projections have at least72 values

Observed immediately before writing: `2026-10-23T14:55:55-0700`.

**CANDIDATE — separate reconstruction pending; no execution.** This is the requested low-cost written continuation after the parent accepted parking. It does not lift either scientific-execution HOLD. It strengthens the earlier support>=16 claim and exposes an exact identity valid for nonuniform laws too. The full guessing-number interval remains20/3..1847/276, with novelty UNCLEAR.

## 1. Unrestricted finite-law identity

Let X=(X_v) be **any** finite joint distribution satisfying all ten FDs on the frozen R-minus graph. No uniformity or group representation is assumed.

Choose one of the eight listed diamonds, write its vertices as `(U,V;P,Q)`, and let Z be its six-vertex complement. All four conditional FDs are available from the actual sight graph:

`H(U,V | P,Q,Z)=0`, `H(P | U,V,Q,Z)=0`, `H(Q | U,V,P,Z)=0`.

Thus, if T=H(U,V,P,Q|Z),

`T=H(P,Q|Z)=H(U,V,Q|Z)=H(U,V,P|Z)`.

Define the projection deficit

`Phi_Z=2 sum_{z in Z} H(X_z)-3H(X_Z)`

and the local nonnegative slack

`L_D = I(P;Q|Z) + 2I(U;V|Z) + I(U,V;P|Z) + I(U,V;Q|Z)`.

Then the following **exact identity** holds:

`Phi(X) = Phi_Z + 2 sum_{v in {U,V,P,Q}} I(X_v;X_Z) + L_D`.       (1)

Proof. The three subadditivity slacks

`H(P|Z)+H(Q|Z)-T`,

`H(U|Z)+H(V|Z)+H(Q|Z)-T`,

`H(U|Z)+H(V|Z)+H(P|Z)-T`

sum to `2 sum_{v in D} H(X_v|Z)-3T`. Expanding the second and third as total correlations shows that this sum is exactly L_D. Substitute `H(X_V)=H(X_Z)+T` and `H(X_v)=H(X_v|Z)+I(X_v;X_Z)` for v in D. This yields (1). QED.

Every term after Phi_Z is nonnegative. Consequently, for **every finite law**, a strict counterexample Phi<0 must satisfy, for every diamond complement,

`3H(X_Z)-2 sum_{z in Z} H(X_z)`

`> 2 sum_{v in D} I(X_v;X_Z) + L_D >= 0`.                      (2)

This is a precise nonuniform constraint, not a support-cardinality assertion for arbitrary laws. Any proposed small/nonuniform projection must supply enough negative projection deficit to pay for both its cross-information with the four omitted variables and the displayed local slack. A projection with Phi_Z>=0 excludes Phi<0 immediately.

**Trust boundary:** identity (1) and implication (2) use only the literal graph FDs, entropy chain rules and Shannon nonnegativity. They do **not** import either the old nine-vertex rational certificates, the diamond non-Shannon certificates, or any finite-group classification.

## 2. Quasiuniform consequence: support>=72, not merely16

Now assume X is quasiuniform and Phi<0. The previous packet's elementary binary-first-pair lemma plus entropy import I2 gives at least three values at each peripheral coordinate. Import I1 excludes constant coordinates and gives, for every v,

`sum_{u!=v} I(X_u;X_v)<H(X_v)/2`.                              (3)

These are exactly the same explicit import boundaries as in Addendum2; no new import is introduced.

Fix one complement Z. It contains five peripherals and one hub. Write

`m=|support(X_Z)|`, `n_z=|support(X_z)|`.

Quasiuniformity gives H(X_Z)=log m and H(X_z)=log n_z. Equation (2) implies

`m^3 > product_{z in Z} n_z^2`.                                (4)

The five peripheral n_z are at least3 and the hub n_z is at least2. Therefore

`m^3 > 3^10 * 2^2 = 236196 > 61^3 = 226981`.

So m>=62.

Suppose m<=71. If any peripheral n_z were at least4, the right side of (4) would be at least

`4^2 * 3^8 * 2^2 = 419904 > 71^3 = 357911`,

impossible. If the hub had at least3 values, the right side would be at least

`3^12=531441>71^3`,

also impossible. Thus all five peripherals have exactly3 values and the hub exactly2 values.

Uniformity of X_Z and its marginals now implies6 divides m. With62<=m<=71 the only possibility is m=66. For any two peripherals z,w, their pair cardinality n_zw divides66, is a multiple of3, is at most9, and exceeds3 because no one coordinate determines another under (3). Therefore n_zw=6. It follows that

`I(X_z;X_w)=log(9/6)=log(3/2)`.

For a fixed peripheral, its other four peripheral companions contribute at least4log(3/2), which is strictly larger than half its entropy `(1/2)log3` since `3^8>3*2^8`. This contradicts (3).

Hence

`|support(X_Z)|>=72`

for **every** one of the eight complements. QED.

This proof subsumes the long8..15 case analysis for the cardinality conclusion. The old snapshots remain valid weaker statements; they are not edited or promoted as separate discoveries.

## 3. Updated group consequence

For a Phi-negative full uniform coset law, `m=[G:L_Z]`. The original candidate's localization makes L_Z an Ingleton violator. Importing the same prior computer-assisted minimum offender order120 yields

`|G|=[G:L_Z]*|L_Z| >= 72*120 = 8640`.

Quotienting by core_G(K), K=intersection_v H_v, preserves every coset cardinality, FD and entropy, so the sharpened statement is

`|G/core_G(K)|>=8640`.

This bound is not asserted tight, and does not say that the number of codewords is at least8640. The previously stated1920 and960 barriers are superseded by this stronger necessary effective-order condition, within the same finite computational import boundary.

The separate all-prime PSL2/PGL2 uniform-coset exclusion is unchanged and does not depend on this group-order argument.

## 4. What does not extend to arbitrary nonuniform laws

The support>=72 proof uses H=log(support size), uniform-fiber divisibilities, and the binary quasiuniform-pair lemma. These equalities do not hold for an arbitrary distribution on a winning set. They must not be silently applied to general nonuniform laws.

For such a law, the exact valid output is (1)–(2). A low-support projection by itself can have negative Phi_Z with very small pairwise mutual informations: for example, six rare mutually exclusive indicator coordinates on seven atoms have that behavior as the rare masses tend to zero. Such a projection is **not** a full R-minus counterexample: the omitted four coordinates still must satisfy the FDs and pay the nonnegative compensation in (2). This example explains why removing the compensation or replacing entropies by bare support logarithms would be an invalid shortcut.

No full nonuniform support exclusion, new numeric guessing-number bound, formal/kernel proof, or novelty claim follows from this addendum. The nonuniform compensation identity and the stronger quasiuniform bound are one coherent continuation of the same primary problem.
