# RQLS10 v51 — tenth-root parity theorem and ENTIRE Fourier/permutation character family: duplicate rays OR NO quantum transversal

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 11:41:40 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact root-of-unity/parity/projective-class/permutation proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

This is a genuinely DIFFERENT tenth-root character model, not a Gaussian fifth-root parameter retry. A necessary parity theorem applies to ANY flat tenth-root10-ray ONB; its application closes EVERY Fourier/permutation Hadamard pairing with arbitrary full resolution, not merely cyclic transversals.

## 1. Exact family theorem, including a literal100-ray positive QLS

Let omega=exp(2pi*i/10) and let mu be ANY permutation of Z10. Define

    q_(x,y)(t)=omega^[x*t+y*mu(t)]/sqrt10,
    x,y,t inZ10.                                 (CHAR)

Every row and column is an ONB by elementary character orthogonality, irrespective of mu. This is the complete literal array, not an unprinted finite search result.

**Theorem.** No CHAR array is a MAXIMAL1-RQLS10. If mu preserves or reverses the input's parity up to a constant, distinct cells already repeat rays. Otherwise the array has NO quantum transversal AT ALL, including completely noncyclic/noncovariant choices. This dichotomy covers ALL mu, with no enumeration or group-complete-mapping WLOG.

The arbitrary independent monomial-equivalence pair family of the Fourier matrix F10 reduces to CHAR: row phases/permutations only rephase/relabel cells, independent column phases give a common coordinate unitary, common column permutations are harmless, and all relative column permutations remain as mu. Thus the ENTIRE F10/F10 monomial pair family is covered.

There is a positive maximal-cardinality QLS example: choose mu swapping0 and1 and fixing2..9. Its100 rays are all distinct by section6, but it has no quantum transversal and is NOT an original1-RQLS witness.

## 2. Exact parity of ANY vanishing sum of TEN tenth roots

Let zeta=omega^2. Then omega=-zeta^3. A vanishing sum of ten tenth roots can therefore be written

    sum_(r=0)^4 [E_r-O_r]*zeta^r=0,

where E_r counts EVEN exponents and O_r ODD exponents, grouped by the bijective residue3e modulo5. Primitive Phi5 forces all five integer signed counts equal:

    E_r-O_r=c for EVERY r.

Since the total number of terms is10,5|c|<=10, and parity of that total equals parity of5c. Thus c isEVEN and c in{-2,0,+2}.

- c0 gives E_r=O_r for every r, so exactlyFIVE exponents even andFIVE odd.
- c2 uses all ten terms at the minimal possible count: E_r2,O_r0 for each r, so ALLten exponents even.
- c-2 similarly makes ALLten odd.

Hence in ANY zero ten-term tenth-root inner product the binary exponent difference has Hamming weight0,5or10. This is a necessary root-count theorem, not an approximate complex cancellation or a claim that parity alone is sufficient for orthogonality.

## 3. ANY flat tenth-root ONB has at mostTWO projective binary parity classes

For a phase word f inZ10^10 reduce its exponents modulo2. Global tenth-root ray phases add either0 or the all-ones binary word, so use parity classes in

    F2^10/<1>.

A proportionality scalar between tenth-root phase vectors must itself be a tenth root (compare one coordinate), so this is a well-defined ray invariant at the phase-family scope. Hamming-weight PARITY is unchanged by complement because length10 isEVEN.

Two orthogonal rays in DISTINCT binary classes have parity difference neither0 nor1, so section2 forces weightFIVE. Their binary weight parities are therefore OPPOSITE. Three different classes cannot be pairwise opposite in one binary invariant. Thus an actual ONB has at mostTWO distinct parity classes.

If it has two, they occur EXACTLYFIVE rays each. To prove this full refinement, normalize the first binary class to0 by common coordinate phases and choose row phases so the second class has a fixed representative w of weight5. The basis matrix's binary rows are0 orw. Pick one physical column with w_s0 and one with w_t1. Their binary difference is the indicator of the second-class rows, whose size m is between1 and9. Columns also are an actual tenth-root ONB, so section2 forces m5. No arbitrary binary clique is called a complex basis.

This parity-class theorem is UNRESTRICTED within ALL flat tenth-root ONBs, not specific to Fourier/Gaussian/A5 matrices.

## 4. The four parity blocks of CHAR

Let

    a(t)=t mod2,       b(t)=mu(t) mod2.

Both binary words have weight5. Their projective classes are nonzero. The cell(x,y) has parity class

    (x mod2)*[a]+(y mod2)*[b].

If [a]=[b], then a+b is a constant word (0or1). For EVERY cell,

    q_(x+5,y+5)(t)=(-1)^[t+mu(t)] q_(x,y)(t),

and that sign is CONSTANT across t. The cells are distinct but their rays coincide. Hence the array is NOT maximal. This covers both parity-preserving and parity-reversing mu, without asserting they exhaust all other possible collision mechanisms.

Otherwise [a],[b] are independent and the four classes

    0, [a], [b], [a+b]

are distinct. Their binary weight parities are even,odd,odd,even respectively. The OPPOSITE class pairs(0,[a+b]) and([a],[b]) therefore CANNOT contain orthogonal rays: their parity difference is even and is neither constant word, while section2 would require weight5.

The other four class pairs may pass this necessary parity test; no sufficiency claim is made. Every original row and column uses two adjacent classes, consistent with its proved ONB property.

## 5. EVERY possible transversal fails in the independent-parity case

A candidate row-and-column transversal is y=f(x), where f is an ARBITRARY permutation of Z10. It uses five even/five odd row indices and five even/five odd column indices. Its2x2 parity-block counts must be

    even/even:s,        even/odd:5-s,
    odd/even:5-s,       odd/odd:s,

for some integer0<=s<=5.

If1<=s<=4, allFOUR binary parity classes occur, contradicting section3's at-mostTWO-class theorem for an actual ONB.

If s5, the two classes are0 and[a+b], an incompatible opposite pair. If s0, the two classes are[a] and[b], also an incompatible opposite pair. Therefore NO candidate permutation f can be a quantum transversal. This closes ALL resolutions at once, not just a selected cyclic/group-table family.

Together with section4's repeated-ray case, this proves the whole family theorem for EVERY mu. Even an independent-parity array that happens to have other ray collisions still has no quantum transversal; maximality was not assumed for this branch.

## 6. Literal100-ray example is genuinely distinct, not just a census

Let mu=(0 1) and fix every other residue. Suppose two cell rays in CHAR are proportional. Then some A,B inZ10 make

    A*t+B*mu(t)=constant for EVERY t.

For t2..9, mu(t)=t. Comparing consecutive values2,3 gives A+B0 modulo10, and then the constant is0. At t0, mu(0)=1 forces B0. At t1, mu(1)=0 forces A0. Thus the two original cell indices are identical and ALL100 rays are distinct.

For this mu, a+b has ones only at0,1, so it is not constant. The no-transversal branch applies. We have a complete exact100-distinct-ray QLS, but its original full-resolution requirement is PROVEDimpossible. No independent executable witness gate has been performed.

## 7. Relation to newer character constructions and exact remaining problem

The character viewpoint was prompted by actually reading the definition/construction sections of Lv–Zhang–Cao, *Orthogonal Quantum Latin Squares with Maximal Cardinality from Full-Rank Factorizations*, arXiv2609.29070v1, https://arxiv.org/html/2609.29070v1 . Its displayed large-order existence theorem concerns BOTH members maximal and does NOT settle the original order10/one-classical-mate question. None of its factorization or existence claims is an operative premise here; CHAR's row/column/distinctness/parity proofs are fully printed.

This theorem does NOT exclude all cyclic-resolution quantum Latin arrays, all tenth-root phase arrays, all abelian/nonabelian nice-error-basis orbits, or the Weyl/dihedral systems ofv7/v8. Those are different models. It excludes the precise all-Fourier/permutation character construction above and its stated monomial orbit. No group covariance or Fourier form was shown WLOG for the original problem.

An entire gate must reconstruct ALLseven sections/endings: integer signed-count parity lemma; projective binary complement invariant; at-mosttwo classes and five/five refinement; binary-dependent repeated-cell proof; ALLfour independent blocks; EVERY transversal contingency case; literal positive100 distinct example; full monomial/application limits. A classical complete-mapping obstruction or one permutation check is not the result.

All computations are exact WRITTEN, not machine-checked. No scientific execution/private approximate scout/finite enumeration/independent finite-witness checker/control/vendor/priority gate used or called passed. No100-ray1-RQLS witness/unrestrictedno-go/formal/kernel/family/human/current-openness/novelty promotion. All unrestricted originalintrinsic10/4+6/5+5 branches remain OPEN. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary leaves this closed character family for genuinely different original geometry, no early pending-review park.
