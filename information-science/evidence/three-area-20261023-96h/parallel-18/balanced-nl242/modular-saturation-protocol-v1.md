# Exact unrestricted modular-saturation criterion and candidate protocol

Author: InfoBalancedNL242, slot info-6. **WRITTEN CANDIDATE / NOT EXECUTED.** This file proves an exact finite criterion and freezes how a future candidate would be verified. It supplies no satisfying assignment, truth table, UNSAT proof or executed checker. No native scientific run is authorized from this launch.

## 1. An exact all-type criterion

Let `H=H_8` be the unnormalized256-point Sylvester transform. The following conditions on two integer arrays `p,w:F_2^8 -> Z` are equivalent to existence of a balanced nine-variable Boolean function with Walsh peak<=28:

1. For every a, `p(a) in {-3,-2,-1,0,1,2,3}`, `w(a) in {-7,-5,-3,-1,1,3,5,7}`, and

   `w(a)=1+2p(a) (mod4)`.

   There are exactly28 local pairs: seven p choices, four w choices for each.

2. `p(0)=0`.

3. At every x in F_2^8,

   `H p(x)=0 (mod64)`,

   `H(w+2p)(x)=128 (mod256)`.

4. The integer energy satisfies

   `E(p,w):=sum_a (w(a)^2+4p(a)^2) <=16384`.

There is no fixed half, residue type, zero set, symmetry, neighborhood or corpus restriction. The energy inequality is necessarily equality. Conditions1–4 are not merely a relaxation: the saturation proof below forces full Boolean realizability.

## 2. Sufficiency: integrality plus one energy bound forces every sign

Define integers

`A(x)=H p(x)/64`,

`B(x)=H w(x)/128`.

The second congruence in condition3 and the first imply that B is integral and `A(x)+B(x)` is odd. Therefore

`A(x)^2+B(x)^2 >=1` at every x.                            (5)

Parseval gives exactly

`E(p,w)=64 sum_x (A(x)^2+B(x)^2)`.

There are256 x, so (5) implies `E>=16384`. The upper bound in condition4 forces equality at every x, hence

`(A(x),B(x)) in {(1,0),(-1,0),(0,1),(0,-1)}`.              (6)

Set `K_0=2w+4p`, `K_1=2w-4p`. Their transforms are

`H K_0=256(B+A)`, `H K_1=256(B-A)`.

By (6), both factors on the right are exactly±1. Thus there are genuine Boolean functions `g,h:F_2^8 -> F_2`, recovered without a solver, for which

`(-1)^g(x)=B(x)+A(x)`, `(-1)^h(x)=B(x)-A(x)`,

and `W_g=K_0`, `W_h=K_1`.

Define the complete nine-variable function by

`f(x,0)=g(x)`, `f(x,1)=1-h(x)`.

Its Walsh coefficients are exactly

`W_f(a,0)=K_0(a)-K_1(a)=8p(a)`,

`W_f(a,1)=K_0(a)+K_1(a)=4w(a)`.

Condition1 bounds the first sector by24 and the second by28, while condition2 makes `W_f(0,0)=0`. This is the required balanced function. Reconstructing all512 bits is part of any actual acceptance.

**Important logical point:** divisibility alone would allow zero, ±2 and larger normalized inverse values. The oddness condition together with the exact minimum energy is what eliminates them. No coordinatewise±1 condition is assumed or checked only on a sample.

## 3. Necessity and unrestricted coverage

The elementary balanced target reduction gives a nonzero support XOR s and a linear normal v with `v.s=1`. Split on `ker(v)` with complementary coset origin s and explicit basis B. The two restrictions `g_*,h_*` have odd weight, equal support XOR in the eight coordinates, and opposite canonical phases because `wt(g_*)+wt(h_*)=256`.

For completeness, nonzero s does not require the new unrestricted covering-radius claim. Balance gives `W_f(a)=4(a.s) mod8`. If s=0, all coefficients are multiples of8 and, under the cap28, belong to0,±8,±16,±24. The Walsh residue `q=W_f/8 mod2` has degree<=2 by the elementary integer character expansion. Since q(0)=0, the nonzero quadratic1+q has weight at least128. Thus at least128 coefficients have magnitude<=16, and Parseval would give

`sum W_f^2 <=128*16^2+384*24^2=253952 <262144`,

impossible. The minimum-weight fact follows by choosing a highest-degree monomial: every assignment of the remaining variables leaves a nonzero polynomial, so a nonzero degree<=2 polynomial on nine variables has at least2^7 nonzero points.

Let `K_g,K_h` be the canonically normalized eight-variable spectra. Canonical normalization multiplies an actual Walsh spectrum by an affine sign character; it corresponds to translating/complementing the input Boolean function and therefore preserves full inverse signs. It is not an arbitrary independent choice of Walsh signs.

Set `S=K_g+K_h`, `R=K_g-K_h`, `w=S/4`, `p=R/8`. The opposite canonical phases and original balance give `p(0)=0`. The cap gives `|w|<=7`, `|p|<=3`. Since `K_g,K_h=2 mod8`, we have `w=1+2p mod4`, which also makes w odd. This is condition1.

Moreover `H p in {0,±64}` and `H(w+2p)=H(K_g/2) in {±128}`, proving both congruences. Finally the two Boolean Parseval equalities give

`sum(w^2+4p^2) = (1/16)sum(S^2+R^2)=16384`.

This proves necessity. Every balanced target has a representative here; no preselected truth-table half has been imposed. The result uses only classical character orthogonality, canonical normalization, the elementary low-bit expansion and Parseval. These mechanisms are prior art; novelty of this specific optimization form is not claimed.

## 4. What a future exact attack could certify

A finite-domain minimum-energy question with conditions1–3 and `p(0)=0` is now exact:

- a feasible assignment with energy<=16384 reconstructs a full balanced target;
- a **checked, complete** proof that no such assignment exists proves unrestricted exclusion;
- a minimum above16384 would also suffice only with a certified global lower bound;
- sampled assignments, LP/count relaxations, unchecked UNSAT, UNKNOWN and a search non-find settle none of these.

The sparse-defect theorem in `sparse-defect-proof-v1.md`, if separately accepted, may add the universally valid cut `#{a:|w(a)| in {1,3}}>=4`. It must not be used as a trusted search cut before its proof gate closes. The seven old residue-type conditions are optional additional proven filters, not the coverage mechanism.

This exact model is a representation/protocol contribution, **not** a claim that28^256 choices are feasible to enumerate or that a new solver run is justified. No runtime framework, encoding implementation or search has been launched.

## 5. Immutable candidate package

If p,w or a truth table is found, create new immutable files in this owned root:

- Literal truth table: exactly512 ASCII0/1 characters plus one newline, index `x=0,...,511`, `x_i=(x>>i)&1`.
- If hexadecimal is additionally supplied: exactly128 digits expanded most-significant bit first *within each digit*, in the same truth-table order. Do not reinterpret the whole hex integer as a reversed bit array.
- Candidate record: exact SHA-256 of the truth-table bytes, p,w bytes if supplied, construction inputs and any producer; source/import ledger; observed clock; full512 Walsh coefficient list and histogram after admitted checks.
- If generated from p,w: record x=(y,t), integer index `y+256t`, the reconstruction formulas in §2, all256 A,B values and both congruence residue arrays.

A candidate object is not promoted merely because its producer prints “242”. Raw bits, not a solver's spectral counts or objective value, are the load-bearing witness.

## 6. Definition-level independent verification gate

**No part of this gate has been executed in this launch.** Each executable check needs an exact parent GO binding source/input hashes, command, positive/negative controls, resources and settlement; a GO for an old job does not transfer.

After admission and pinning:

1. A strict parser rejects wrong length, nonbinary characters, extra records or an unexpected byte hash. Confirm `sum bits=256` directly.
2. One independently authored integer FWHT computes all512 coefficients from the sign table, and checks origin0, peak<=28, NL=256-peak/2 and Parseval262144. No floating point.
3. A separately authored implementation imports no producer/checker helpers and computes all512 direct character sums from the raw truth table. Require exact equality of every coefficient, not just the maximum/histogram.
4. A third independently authored definition-level verifier computes distances to all1024 affine Boolean functions and checks the minimum>=242. This is not another solver on the same encoding. Ordinary in-harness review may be requested through the parent; independent-model CLI remains unauthorized.
5. For a p,w producer, independently verify conditions1–4, derive A,B and (6), reconstruct raw bits, and compare the resulting512 coefficients with the direct table check. This is additional provenance, not a substitute for steps1–4.

Meaningful controls to freeze alongside any checker:

- Positive balanced240 control: `f(x,t)=x_0x_1+x_2x_3+x_4x_5+x_6x_7+t`; its balance and peak32 follow symbolically from an eight-variable bent quadratic. A relaxed threshold32 checker must accept it, and threshold28 must reject it specifically for the Walsh cap.
- Positive unbalanced242 control: a precisely pinned Kavut–Yücel printed table. Its nonlinearity-only mode must accept, while target mode must reject specifically for balance, using its actual independently computed weight.
- Strict parser controls: truncate/duplicate a bit, insert an invalid character, wrong expected hash and wrong expansion convention.
- On any genuine target: flip one bit; reject specifically for balance, not merely an unrelated parser exception. A balanced two-bit swap is not automatically invalid and must not be designated a guaranteed rejection without checking its actual spectrum.
- Do not claim a synthetic p,w count vector is a positive Boolean control. A hypothetical target is not a currently available positive target fixture.

For an exclusion, a checked DRAT/LRAT-style proof or a genuinely complete written argument must be accompanied by the exact unrestricted mathematical-to-encoding map, all constraint families and symmetry proofs. Agreement of two solvers on one encoding is weaker and is not a universal certificate by itself.

## 7. Actual status

No 512-bit balanced242 table or global exclusion exists in this packet. The completed deliverables are this exact written criterion/protocol and the separate all-type sparse-defect necessary-condition candidate. Correctness review, finite verification, formal acceptance, priority and scientific significance remain separate. No scientific script, solver, enumeration, compilation, Walsh replay, test suite or CLI delegation was run. Parent alone integrates and may authorize verification after reviewing the pinned candidate.
