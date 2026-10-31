# f219 — independent same-harness review of the T2-free single-small-prime exclusion

**Disposition: 0F / 0M / 0m; 3 INCONCLUSIVE items (I1–I3 below).** The written argument for the frozen cyclic-tiling theorem and its stated order-family corollary reconstructs from elementary arithmetic. This is support for that scoped argument, not a claim about any larger head family or unrestricted completion. The actual-word code caller is conditional on its named external border theorem.

## Frozen inputs, measurements and sequence

The first research artifact opened was `manifest-v1.json`. Its measured SHA-256 was `48a2bbf009ffe1374e31ebbe94a6b989d96c27d411e1f97cc68c015dc3a7d870`, matching the required prefix `48a2bbf009ff`. It measured 3,064 bytes and 30 LF. **Before either input body was read**, both declared inputs were measured and all three quantities matched the manifest:

| Manifest order | Input | Measured SHA-256 | Bytes | LF |
|---|---|---|---:|---:|
| 1 | `institute/runs/three-area-2026-10-27-96h/dispositions/math-5-shor-single-small-shared-prime-head-exclusion-conditional-parent-v1.md` | `c1c4c95dc4f399fbcb9cc3356b0d415778f8a496e9417c9e8828c3ecf27ea8aa` | 3,637 | 13 |
| 2 | `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-single-small-shared-prime-T2-free-v1.md` | `5aa6c71dbe3fb5d40d999821055ba7787d6757e0ab8926697fe71619dc863f83` | 12,293 | 123 |

Paths in this table are relative to `/Users/jinleic/repos/aifours/`. Both input bodies were displayed completely, in the manifest order, before mathematical reconstruction or controls, in these actual raw windows:

- Input 1: `1–13`.
- Input 2: `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–105`, `106–120`, `121–123`.

The input-1 disposition adopts its earlier tiling result only **conditionally** on an LL/T2 statement, records the coset observation without adopting a new T2-free result, and states a same-code border consequence at its frozen scope. I did not use its conditional T2 route, its linked bodies, or its claimed controls as premises. The target's route is reconstructed below from the literal tiling and anchor assumptions. The author's stated reviewer-guided provenance is retained; neither the observation nor its origin is a substitute for a proof.

Native `/bin/date` observed immediately before writing this review: `2026-10-29T13:42:39-0700 PDT`. This is a pre-write observation, not an asserted file-creation time.

## Per-claim dispositions

`0F/0M/0m` means no fatal, major, or minor finding on the claim as scoped; an INCONCLUSIVE entry is not a pass on the indicated outside premise or provenance.

| Claim | Verdict | Basis and limit |
|---|---|---|
| Group-ring coprime dilation, including injectivity and iteration | 0F/0M/0m | Nonnegative integer coefficient sum upgrades the mod-ell congruence to a unique tiling; §1. |
| CRT unit lifting and equal-gcd exclusion | 0F/0M/0m | A unit matching the two differences exists for every prime-power allocation; §2. |
| R1: `330 | n` | 0F/0M/0m | Actual anchor differences `8`, `3`, `5`, `11` versus `1`; §3. |
| R2: `3·5·11 | |Q|`, parameterization and `v≥2` | 0F/0M/0m | Dilation of Q supplies a direct duplicate representation if any small prime is absent from its size; §3. |
| R3: odd Q-difference divisible by q1 or q2 must be divisible by p² | 0F/0M/0m | Both p-adic cases yield an admissible odd multiplier and equal-gcd collision; §3. |
| R-dilated quotient, every fibre's size and unconditional nonconstancy mod p² | 0F/0M/0m | Each fibre is nonempty; constant residue would force the noninteger coset count `2^a/p`; §4. No parity or T2 premise. |
| Single-parity fibres and one crossing-edge contradiction | 0F/0M/0m | Universal cross-pair congruence makes a mixed fibre or a crossing fibre constant; connectedness suffices; §5. |
| `n>14`, `|P|=p·2^a`, p in `{3,5,11}` exclusion | 0F/0M/0m | The preceding steps compose for arbitrary other odd factors and exponents; §5. |
| `n=165·p^s·2^K` corollary, including j=0 and j=1 | 0F/0M/0m | The explicit j=0 odd-difference argument is reconstructed in §6; no j≥2 exclusion is inferred. |
| Literal code anchors and conditional actual-word border caller | 0F/0M/0m conditional; **I1** | The words visibly give the claimed anchors; the external border theorem's exact statement, attribution and validity are not independently verified under this contract; §7. |
| Import disclosure | 0F/0M/0m | No Sands, Tijdeman, LL or T2 theorem is invoked as a premise for the cyclic theorem. The only direct non-elementary premise of the code caller is the stated actual-word border theorem; §7. |
| Historical provenance and author's computations | **I2** | Reported exposure and author controls are not independently checked and are not evidence for the theorem. |
| Unrestricted status, novelty and outside-scope families | **I3** | Not determined: in particular no claim is checked for other head primes, multiple odd head primes, or `j≥2`. |

## 1. Independent reconstruction: dilation

Write the cyclic group additively and let `P⊕Q=Z_n` mean that every residue has exactly one ordered representation. In the commutative group algebra over `F_ell`, let `u=Σ_(x∈P)[x]`, `v=Σ_(y∈Q)[y]`, and `G=Σ_(z∈Z_n)[z]`. The tiling gives `uv=G`, and `uG=|P|G`. For prime `ell` not dividing `|P|`, the freshman's dream yields

`u^ell = Σ_(x∈P)[ell x]`, and hence

`u^ell v = u^(ell−1)G = |P|^(ell−1)G = G` in `F_ell[Z_n]`.

The last equality is Fermat's little theorem. Take the same expression in the integer group algebra, retaining the **multiplicity** of each scaled element. Every resulting coefficient is a nonnegative integer congruent to 1 mod `ell`, hence at least 1. Their sum is `|P||Q|=n`, so all n coefficients are exactly 1. Because Q is nonempty, a repeated value of `ell x` would produce a coefficient at least 2. Thus scaling is injective on P and `ell P⊕Q=Z_n`.

For a positive integer t coprime to `|P|`, apply this argument successively to every prime factor of t with multiplicity. Every stage retains the same factor size and tiles, establishing `tP⊕Q` and injectivity. The multiplier need not be a unit modulo n. The same argument applies with P and Q interchanged.

## 2. Equal-gcd exclusion by a CRT unit

Suppose nonzero differences `d_P∈P−P`, `d_Q∈Q−Q` have the same gcd `g` with n. Since they are nonzero residues, `g<n`; put `m=n/g` and write `d_P=gu`, `d_Q=gv` with u and v units modulo m. Choose `w≡v u^(−1) (mod m)`. For every prime dividing n but not m, additionally require `w≡1` modulo that prime. These additional moduli are mutually coprime and coprime to m, so CRT gives a positive w satisfying them all. At primes dividing m, w is already a unit; at the remaining primes dividing n it is 1. Thus `gcd(w,n)=1` and `w d_P≡d_Q (mod n)`.

Because `|P|` divides n, `gcd(w,|P|)=1`, so §1 gives `wP⊕Q`. If `d_P=x−x'` and `d_Q=y−y'`, then `wx+y'=wx'+y`. The two P entries remain distinct because w is a unit, and this contradicts uniqueness. Therefore the gcds cannot agree. This derivation uses only CRT and the proven dilation lemma, not a Sands or Tijdeman theorem.

For later use, the elementary coset count is: if `X⊕Z=G` and `X⊆H≤G`, then each `u+H` is tiled by X and `Z∩(u+H)`, because in a representation `y=x+z` the terms y and x force z into that coset. Consequently each such intersection has cardinality `|H|/|X|`, necessarily an integer.

## 3. R1–R3

Assume the target hypotheses. Since `n>14`, all displayed anchor differences are nonzero in `Z_n`.

**R1.** If n were odd, the P difference `8−0=8` and Q difference `1−0=1` would both have gcd 1 with n. If `ell∈{3,5,11}` did not divide n, the respective P differences `3−0`, `8−3`, `11−0` and Q difference 1 would again have equal gcd 1. Section 2 therefore forces `330|n`.

**R2.** If `ell∈{3,5,11}` did not divide `|Q|`, §1 would give `P⊕ell Q`. The latter Q factor contains both 0 and ell, since 0 and 1 are in Q; P has a pair differing by ell. These provide two distinct representations of the same residue, contradiction. Thus each of 3, 5, and 11 divides `|Q|`.

Write the other two primes as `q1,q2` and factor

`n=2^K p^v R`, `|P|=p·2^a`, `|Q|=p^(v−1) R 2^b`,

where `K≥1`, `v≥2`, `a,b≥0`, `a+b=K`, R is odd, `gcd(R,p)=1`, and `q1q2|R`. Here `v≥2` uses the p in **both** factor cardinalities, not an assumption that p is unshared. R may have arbitrary further odd prime powers.

**R3.** Let `x=q−q'` be an odd Q-difference divisible by q1 or q2. Set `g=gcd(x,n)`. The representative-independent parity follows from even n; g is odd and `g<n`. If p does not divide x, select a small prime `ell∈{q1,q2}` dividing x. It divides g, and `t=g/ell` is odd and coprime to p, so `gcd(t,|P|)=1`. The actual P difference ell dilates to g in `tP`, whose gcd with n is g, matching the Q difference x. Section 2 gives a contradiction.

If p divides x but p² does not, `v≥2` ensures that p divides g exactly once. Now `t=g/p` is odd and coprime to `p2^a`; dilating the actual P difference p again gives gcd g, contradicting §2. These are the only cases in which p² fails to divide x, so R3 follows. The proof does not assert the same rule for even differences.

## 4. Every fibre is nonconstant modulo p²

For each `r∈Z_R`, let `Q_r={q∈Q:q≡r (mod R)}`. Since `gcd(R,p2^a)=1`, dilation gives `RP⊕Q=Z_n`, with `RP⊆H=RZ_n`. Its injective factor has size `p2^a`, so the coset count gives, for **every** r,

`|Q_r|=(n/R)/(p2^a)=p^(v−1)2^b>0`.

Let `N=n/R=p^v2^K`, identify H with `Z_N` by `z↦Rz`, and choose an integer representative r for the coset. Restricting `RP⊕Q` to that coset and translating by `−r` gives the direct tiling

`Pbar⊕V_r=Z_N`, where `Pbar={x mod N:x∈P}` and `V_r={(q−r)/R mod N:q∈Q_r}`.

The scaled-factor injectivity proves `|Pbar|=p2^a`; the quotient map on the fibre is also injective, so `|V_r|=p^(v−1)2^b`. All of these statements are independent of fibre parity.

Suppose `Q_r` were constant modulo p². Because p does not divide R, every element of `V_r` has the same residue modulo p². Translate `V_r` by one of its elements into `H'=p²Z_N`; this translation preserves the tiling. The coset count applied with X equal to the translated `V_r` would force each Pbar intersection with a coset of H' to have the integer cardinality

`|H'|/|V_r| = (p^(v−2)2^K)/(p^(v−1)2^b) = 2^a/p`.

This is not an integer because p is odd. Thus **every** fibre has at least two residues modulo p². No T2, cyclotomic assignment, parity hypothesis, or result from the previous disposition was used.

## 5. Single parity and the crossing edge

If some `Q_r` contained both parities, every even–odd pair from it would have an odd difference divisible by R and hence by q1. R3 would make each pair congruent modulo p². Fixing one element of each parity then makes all elements of both parity classes congruent to the same residue modulo p², contrary to §4. Therefore each nonempty fibre has a single parity.

Partition `Z_R` into the even-fibre indices E and odd-fibre indices O. Both are nonempty: the fibre of 0 is even, the fibre of 1 is odd, and `R≥q1q2>1` makes the indices distinct. The undirected graph with steps `±q1` and `±q2` is connected because `gcd(q1,q2)=1`, so an integer combination of the steps equals 1. Any path from 0 to 1 contains an E–O crossing edge.

For one such edge, its endpoint difference is `±q_i mod R` for i=1 or 2. Since `q_i|R`, every pair of Q-elements from the two endpoint fibres has difference divisible by q_i; the difference is odd because the fibres have opposite parities. R3 therefore says **every** cross pair is congruent modulo p². Fixing an element in either nonempty fibre makes the other fibre constant modulo p², contradicting §4. This one edge is enough; no connectedness of the subgraph of crossing edges is assumed. The contradiction excludes the target tiling for every stated p and n.

## 6. The stated order-family corollary

Take `n=165·p^s·2^K` with `K,s≥1`. The two primes q1,q2 different from p each occur once in n and, by R2, occur in `|Q|`, not `|P|`. Also p divides `|Q|`, while its exponent in n is `s+1`. Thus `|P|=p^j2^a` with `0≤j≤s`. Section 5 excludes j=1.

For j=0, write `M=165p^s`, so `n=M2^K` and `|P|=2^a`. Since M is odd, `MP⊕Q` by dilation, and `MP⊆MZ_n`. The coset count therefore makes Q meet every class modulo M, including 6. Choose `q∈Q` with `q≡6 (mod M)`, hence modulo 165. If q is odd, let `x=q−0` and `ell=3`; if q is even, let `x=q−1` and `ell=5`. In either case x is odd, is divisible by ell, is an actual Q-difference, and is nonzero modulo even n. Set `g=gcd(x,n)` and `t=g/ell`. Then `g<n`, t is odd, and `gcd(t,2^a)=1`. The A-difference ell scaled by t has gcd g with n, matching x, which §2 forbids. Hence j=0 is impossible as well, leaving `2≤j≤s`; in particular this order family has no such tiling when `s=1`. No conclusion about j≥2 follows.

## 7. Explicit imports and remaining gaps

**T2 / Sands / Tijdeman / LL:** none is directly imported into the cyclic-tiling theorem or the elementary corollary. The proof above uses only elementary finite group algebra, Fermat's little theorem, integer divisibility, CRT/Bezout, and the proved coset count. The earlier disposition's T2-conditional result is not used as a theorem premise.

**Actual-word caller, I1:** the candidate names a Restivo–Salemi–Sportelli actual-word border theorem, as stated in its cited Cordero source, as a premise for a finite uniquely decipherable, factor-complete D containing the literal Shor code S and a pure-a atom `a^n`. Conditional on that stated theorem giving the displayed actual-word border sets P and Q and their direct cyclic tiling, the anchor inclusions are immediate: S contains `b`, `a³b`, `a⁸b`, `a¹¹b` and `b`, `ba`, `ba⁷`, `ba¹³`, `ba¹⁴`. For `n>14`, §5 then excludes `|P|=p2^a`. This is not a construction of a code from an arbitrary tiling. The frozen disposition expressly records a same-code caller at its conditional scope; it is not independent verification of the candidate's exact external source wording. External source inspection is forbidden here, so the border theorem's precise formulation, attribution, validity, and any transitive dependencies remain unverified. No stronger assertion about those dependencies is made.

**I2:** the author's descriptions of earlier exposure, provenance, and finite controls are not independently established in this review. The input explicitly discloses reviewer-guided provenance. No author code, script, PASS, receipt, solver result, or floating search was used as evidence.

**I3:** the claim of an unrestricted problem remaining open, novelty, and the status of unreviewed higher-powers/other-primes/multiple-odd-prime families are not established by these inputs and are outside this review. The proof's finite cases do not settle them.

## Reviewer-owned exact control receipts

These are finite diagnostic checks, not proofs of the universal theorem. Both scripts are reviewer-owned, inside this wave, use integer arithmetic and Python's standard library, and do not load author artifacts. Each run had a 120-second tool deadline; neither completed run hit it.

1. `reviewer-exact-controls.py`, final measured SHA-256 `32224c4f917e9984d1fa2f29dbf07fc0fc0d5b3120d283595a1fe6aa05b48f33`; `/usr/bin/python3`; native `/bin/date` start `2026-10-29T13:40:53-0700 PDT`, end `2026-10-29T13:40:54-0700 PDT`; exit **0**. It enumerated 1,254 normalized tilings for `2≤n≤16`, checked 10,160 coprime multipliers including 1,678 nonunits modulo n, and checked 4,979 prime congruences. Unit orbits checked 126,454 equal-gcd ordered pairs for `2≤n≤90`. Arithmetic checks covered 1,243 odd-order R1 witnesses, 5,905 missing-prime witnesses, 36 simple equal-difference collisions, 2,268 R3 forbidden-gcd witnesses, and 324 noninteger coset ratios. It checked 261,121 pairs of nonempty residue subsets for the all-cross-pairs implication, nine connected graph instances, all 32,766 nontrivial partitions of `Z_15`, and two synthetic j=0 parity branches.

   Intended-reason negatives: a noncoprime multiplier repeats P in `Z_8`; an ambient nonunit may nevertheless be valid in `Z_12`; unequal gcds 2 and 3 in `Z_12` have no connecting unit; in `n=990,p=3,a=1`, gcd 45 has the permitted p² factor and even gcd 10 is outside R3; an unanchored `Z_18` tiling with `|P|=3²` has `Q={0,9}` constant mod 9; one equal cross pair need not make either set constant; step 3 alone is disconnected on `Z_15`; and the j=0 synthetic tilings lack the required P-anchor even though the illustrated Q difference exists.

   **Disclosure of initial failed run:** the first version had SHA-256 `7d70cd94f32283073bf45f0f283b1840a08964b05a646492f0187f253271d48a`, ran from `2026-10-29T13:39:59-0700 PDT` to `2026-10-29T13:39:59-0700 PDT`, and exited **1** at `int.bit_count`, unavailable in the invoked Python. It stopped before completing the parity/graph/j=0 controls. I changed that one singleton-bit check to `e & (e−1)==0` and ran the final script above. The partial failed run is not counted as a completed control; the initial version was not retained as a separate file.

2. `reviewer-quotient-controls.py`, measured SHA-256 `124ead5f41ba94b8b53753418a11e11c46ce9a50d20a53e3f35e08be53f1099a`; `/usr/bin/python3`; native start and end `2026-10-29T13:41:59-0700 PDT`; exit **0**. Six synthetic unanchored tilings for the three p values and `a∈{0,1}` gave 206 fibres. Every fibre was checked for its exact cardinality, direct quotient tiling, and nonconstancy mod p². In the a=0 controls, mixed-parity fibres exhibit odd q1-divisible differences not divisible by p² because the needed anchors are absent; in the a=1 controls all Q-elements are even, so the Q-anchor 1 is absent. A separate `n=18,R=3,|P|=3` negative gives fibre counts `6,0,0` and a failed scaled tiling when the necessary coprimality is removed.

The finite controls do not establish an all-n claim and none of their unanchored examples is asserted to satisfy the theorem's full hypotheses.

## Contract deviations and assurance

No deviation from the frozen-input/read-order/evidence restrictions is claimed. The initial reviewer-script runtime failure and repair are disclosed above; it is not treated as a result about the author candidate. No author code was executed, no input was edited, and no external source, sibling review, author contact, f161/f162/held payload, or solver outcome was used. Controls and this review are the only written artifacts owned here.

**Same-harness review is not human, independent-model-family, formal/kernel, or novelty verification.**
