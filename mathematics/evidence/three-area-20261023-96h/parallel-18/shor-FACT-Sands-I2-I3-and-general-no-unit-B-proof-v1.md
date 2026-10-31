# Shor FACT: complete I2/I3 reconstruction and the GENERAL no-unit-seed prime-power theorem

Owner MathShor-2. Actual `/bin/date` immediately before this NEW manuscript write: **Mon Oct 26 12:02:14 PDT 2026** (precreation observation).

**NEW ADDITIVE WRITTEN CANDIDATE, UNREVIEWED.** This fills the specifically named I3 proof prerequisite of the GENERAL Theorem B in `shor-FACT-prime-power-side-exclusion-v1.md`, including its previously unproved no-unit-seed application, and gives a self-contained proof of the I2 divisor criterion. It does NOT claim a new FACT size restriction, a three-prime theorem for |A|, an I4 proof, a finite completion, noncompletion or raw stabilization. Original unrestricted Shor completion remains **NOT_PROVED in either direction**.

## 0. Prospective authority, source exposure and exact import boundary

Actual v141-A222LF RETURN preceded NEW whole61/ACK, SHA256 `10dbe970a23132c0f3140a257453d80cb0343b23505833d9c424e50d69b48446`; Main actually read it through END and issued explicit future-only original-primary direction v89. That ENTIRE direction was read FIRST before the current primary source work. ALL six own findings and THREE separate provenance blockers remain; neither source timing nor this new proof supplies a clean-provenance/process cure.

The source question was the named cyclic-group I3/I4 dependency retained in the qualified FACT frontier, not a raw coefficient/Taylor/parser consequence. This manuscript uses only normalized DIRECT CYCLIC GROUP factorizations, elementary finite group-ring arithmetic and CRT fibers. It does not consume, repair, universalize or backconvert the quarantined coefficient/Taylor/control/selected-DeFelice/later-raw-parser lines, their source-selection directions or conclusions. This is a bounded statement of the explicit mathematical proof inputs, not a global hidden-cognition/provenance assertion. All earlier597LF candidate bodies keep their own gate states.

Primary source actually read: A. D. Sands, **On Keller's conjecture for certain cyclic groups**, *Proc. Edinburgh Math. Soc.*22(1979),17–21, DOI <https://doi.org/10.1017/S0013091500027747>. The static reader yielded no proof text and flagged ALL five scanned pages incomplete. Under Main's explicit SOURCE-READING-ONLY browser permission, ALL five pages were actually viewed as raster screenshots, including source Theorems2/3/4 and their proofs on printed20 and the final references/address on21. Exact ten browser cells, printed outputs, screenshot hashes, actual clock bounds and source coverage are characterized in `shor-Sands1979-source-browser-cells-and-coverage-v1.json`; viewer was closed. No formula was evaluated in JS or another scientific interpreter.

Source Theorem4 has **GROUP ORDER** p^e q^f, not arbitrary-n **CARDINALITY** |A|=p^alpha q^beta. The source's Theorem2 proof cites Rédei's Hilfssatz6; earlier source results use de Bruijn. Those original transitive proofs were NOT read. The complete proof below instead derives the automorphism/divisor step from the independently displayed elementary multiplier proof, so neither unread Hilfssatz6 nor de Bruijn is a premise of THIS manuscript.

**Required scope distinction:** Cordero2301.13566v1 Lemma5.2 literally states the CARDINALITY-form result and attributes it to Szabó–Sands2009 Theorem5.5. Its original proof remains **NAMED_NOT_RECONSTRUCTED (I4)**. Sands1979's group-order theorem does not discharge it. The current result discharges only I2/I3 and GENERAL Theorem B as a NEW written candidate, not the old frozen file or all its numerical wording. Older660/1320/R2LF58/H* qualifications remain unchanged.

## 1. Set-up and the full elementary multiplier lemma

Write G=Z_n additively, n>1. A direct factorization A⊕B=G means every g has exactly one representation a+b. Both factors are finite/nonempty and |A||B|=n. A normalized factorization has0 in both factors. For a set S let f_S be its integer indicator, with convolution on G.

**Lemma M.** If A⊕B=G and d is a positive integer with gcd(d,|A|)=1, then multiplication by d is injective on A and dA⊕B=G. d need not be a unit modulo n.

*Complete proof.* First let r be prime and r not divide |A|. In the commutative group ring over F_r, Frobenius gives `f_A^{*r}=T_r f_A`, where T_r pushes multiplicities forward under x↦rx. Therefore

`(T_r f_A)*f_B = f_A^{*(r−1)}*(f_A*f_B) = |A|^{r−1}*1 = 1 (mod r)`.

The middle equality uses the actual integral identity f_A*f_B=1; the last uses the nonzero residue of |A| and Fermat. The left side has nonnegative INTEGER values, each congruent1 mod r, so each is at least1. Its sum over G is |A||B|=n. Hence every value is EXACTLY1.

If two distinct a,a' had ra=ra', then fixing any b in B would give contribution at least2 at ra+b, contradiction. Thus T_r f_A is the indicator of rA, with unchanged size, and rA⊕B=G. Factor d into primes and iterate, retaining |rA|=|A| at every step. This proves M without a Fourier/native/CAS computation. In particular M applies to EVERY automorphism multiplier t with gcd(t,n)=1, because |A| divides n. ∎

## 2. Exact unit-orbit proof of I2, including both directions

For S⊂Z_n define

`Div_n(S)={gcd(s−s',n):s,s' in S}`.

Representatives do not matter. n is included by taking s=s'.

**Lemma UO.** Two nonzero elements u,v of Z_n with the same gcd d with n are carried to each other by a UNIT multiplier t modulo n.

*Proof.* Put N=n/d, u=d u', v=d v', where u',v' are units modulo N. Prescribe `t=v'*(u')^{-1} (mod N)`. This residue is nonzero modulo each prime dividing N. For each prime power ell^e exactly dividing n with ell not dividing N, additionally prescribe `t=1 (mod ell^e)`. CRT supplies a positive t satisfying these compatible prescriptions. It is coprime to every prime of n, and `t u=v (mod n)`. No enumeration or chosen finite control is used. ∎

**Theorem I2.** For sets A,B⊂Z_n,

`A⊕B=Z_n iff |A||B|=n and Div_n(A) intersect Div_n(B)={n}`.

*Necessity.* Cardinality is immediate. Suppose a nontrivial common gcd d<n came from u=a−a' and v=b−b'. UO supplies a unit t with tu=v. By M, tA⊕B=G, but

`ta+b' = ta'+b`.

Here a≠a' and t is injective, so these are distinct representations. Contradiction. Thus only n is common.

*Sufficiency.* Suppose cardinality and divisor exclusion hold. An actual collision a+b=a'+b' with either pair distinct would give the SAME nonzero difference a−a'=b'−b and hence a common gcd d<n. Therefore all |A||B| sums are distinct. There are n of them in a group of n elements, proving complete coverage. This direction needs no unproved character identity. ∎

This is the same divisor/orbit criterion as Sands1979 Theorem3, reconstructed here from M and elementary CRT. It is valid for arbitrary n; it is not a Shor/three-mate sufficiency assertion.

## 3. Complete GROUP-ORDER two-prime subgroup theorem I3

**Lemma GD.** Let n have at most TWO distinct prime divisors and n>1. If S⊂Z_n contains0 and generates Z_n, then S−S contains a unit of Z_n.

*Proof.* For n=p^v, generation means some s is not divisible by p, so s−0 is a unit. For n=p^v q^w with distinct p,q and v,w>=1, generation gives s not divisible by p and t not divisible by q. If either is already a unit, use its difference with0. Otherwise s is divisible by q but not p, and t is divisible by p but not q. Then s−t is divisible by neither p nor q, hence is a unit. This exhausts the cases; no unit ELEMENT of S was assumed. ∎

**Theorem I3 (Sands group-order form).** In a normalized direct factorization A⊕B=Z_n with n>1 having at most two distinct prime divisors, at least one of ⟨A⟩,⟨B⟩ is proper.

*Proof.* If both generated, GD would give unit differences in BOTH A−A and B−B. Then1 belongs to Div_n(A)∩Div_n(B), contradicting I2 because n>1. ∎

For the two-prime case this is precisely the hypothesis/conclusion of the original source Theorem4 actually viewed on printed20. The proof HERE is complete even in the no-unit-element case, and does not import the unread Rédei/de Bruijn proofs. The restriction n>1 avoids the trivial-group exception, where no proper subgroup exists.

## 4. The general all-n prime-power factor theorem, with NO unit seed

**Theorem B.** Let A⊕B=Z_n, n>1,0∈A∩B, |A|=p^alpha with alpha>=1 and p prime. If A generates Z_n, then **B⊂pZ_n**. No element of A is assumed to be a unit modulo n or any two-prime projection.

This is the ENTIRE general statement whose previous proof retained the no-unit I3 import. We now prove every step.

### 4.1 CRT-fiber lemma from M

Write n=p^v m with gcd(p,m)=1; v>=alpha because |A| divides n. Let N be any divisor consisting of the whole p^v component and any selection of the other FULL prime-power components, so gcd(N,n/N)=1. Choose positive d satisfying

`d=1 (mod N), d=0 (mod n/N)`.

As p does not divide d, M applies. In the CRT decomposition Z_n=Z_N×Z_(n/N), dA is precisely the set of projected points `(a mod N,0)`, with the same size as A. Thus projection mod N is injective on A. Write A_N for its image.

For EVERY z∈Z_(n/N), let

`B_z={b mod N : b∈B, b mod(n/N)=z}`.

In a representation of `(x,z)` by dA+B, the B component necessarily has this z. Therefore

`A_N⊕B_z=Z_N`, and `|B_z|=N/p^alpha`.

In particular each fiber is nonempty. Also A_N generates Z_N, since it is the homomorphic image of a generating set. This proves the complete fiber lemma without a missing positivity/projection assumption.

### 4.2 Single-p fibers are constant modulo p

Take N=p^v. For every m-coordinate y, choose any b_y in its nonempty B fiber. The normalized factorization

`A_(p^v) ⊕ (B_y−b_y)=Z_(p^v)`

has its first factor generating. I3 (or its single-prime proof) makes the second generated subgroup proper. Every proper subgroup of a cyclic p-group is contained in pZ_(p^v). Hence ALL original B elements with the same m-coordinate have the SAME residue mod p. If m=1 this already gives B⊂pZ_n because0∈B.

### 4.3 Every one-other-prime fiber is likewise constant modulo p

Suppose m>1. Fix ANY prime q dividing m, with q^w the full q component, and let W_q=m/q^w. Apply4.1 with N=p^v q^w. For EVERY W_q-coordinate z, normalize B_z by one b_z. The first factor A_N generates Z_N. The complete I3 theorem therefore makes `⟨B_z−b_z⟩` a proper subgroup of Z_N, contained in pZ_N OR qZ_N.

The q alternative is impossible. Indeed, for EVERY q-coordinate y_q,4.1 with N=p^v gives a nonempty original B fiber at the entire m-coordinate `(y_q,z)`. Thus B_z contains elements of EVERY q-coordinate; after translation they still exhaust every q-coordinate, so they cannot all be divisible by q. Consequently

`B_z−b_z ⊂ pZ_N`.

This proves that original B elements with the same W_q-coordinate have equal residue mod p. Crucially no unit element of A_N was required: I3 was proved via a UNIT DIFFERENCE, which exists by generation in the two-prime group.

### 4.4 Connect all fibers, retaining the actual complement

Take arbitrary b,b'∈B and list the distinct primes of m as q_1,...,q_s. Starting at b, change its q_1-coordinate to that of b', keeping all OTHER m-coordinates fixed. Such a B element exists by4.1's nonempty fiber at every full m-coordinate; both elements are in one W_(q_1) fiber and so have the SAME residue mod p by4.3. Repeat for q_2,...,q_s.

At the end there is b*∈B with b*_m=b'_m and b* congruent b mod p. By4.2, b* and b' have equal residue mod p. Hence b and b' do too. Since b,b' were arbitrary and0∈B, every B element is divisible by p. This proves Theorem B for ALL n with NO unit seed. ∎

The complement B was never replaced by a different tiling complement in this argument. Auxiliary multiplier factorizations use the SAME B; normalized fibers are explicitly connected back to that B. A period reduction that merely produces some new complement would not suffice for the theorem stated here.

## 5. Exact effect on the original frontier and what is STILL not proved

The new candidate proof dependency graph is elementary convolution/Fermat/CRT -> M -> UO/I2 -> GD/I3 -> all four complete steps of GENERAL B. Every specialized proof input in this graph is displayed; no imported theorem remains at the former no-unit I3 boundary. Parent adoption or a joint existing-source gate is NOT automatic: the frozen old prime-power packet remains byte-identical and must be read with its existing660/1320 wording qualifications.

For Shor FACT, |A| is even, its prime-power cases were ALREADY excluded by the admitted unit-seed argument. Therefore this manuscript **does not claim a newly eliminated FACT cardinality or new science bound**. Its substantive contribution is a complete all-n no-unit proof and discharge candidate for the named Sands I2/I3 dependency, rather than a repeated1320/small-period calculation, solver miss or finite instance enumeration. Known source proofs are not claimed novel.

The stronger I4 assertion about arbitrary-n factorizations with |A|=p^alpha q^beta remains **NAMED_NOT_RECONSTRUCTED**. Nothing here replaces |G| by |A| in I3. In particular there is NO unconditional three-prime-cardinality conclusion from this manuscript. All general two-prime-size residuals and sizes with more primes stay at their exact existing boundaries. H* stays FALSE/WITHDRAWN; R2 LF58's universal two28-coset shape remains NOT_RECONSTRUCTED; bare FACT gives660|n and n>=1320, NOT1320 divisibility. No literal Shor source is changed.

The original unrestricted RAW positive gap is still an actual finite UD complete extension (or finite positive-reset certificate with EVERY raw coefficient nonnegative and all literal C inclusions); the negative gap is a uniform obstruction across all finite lengths/counts/arity/delay/memory or all necessary FACT data. No raw SP/Kraft witness, short-gap realization, STAB/GP bridge, concrete factorization or finite-code counterexample is supplied. The five597LF all-word-memory/integer-necessity candidates keep their separate unreviewed/parent-gate status and are not promoted by this source work.

All SIX own process majors and THREE separate provenance blockers, all ZERO-credit controls/glosses/Taylor/coefficient/selected-source/later-parser consumers, historical unknown execution boundaries and all parent/owner/reviewer findings remain. This proof gives no timeline-based unaffectedness, clean-process/cognition/runtime census, or process cure. The ten authorized browser source-only cells are expressly characterized, not hidden as no-Eval history.

WRITTEN exact symbols/fractions/integer products only, including private reasoning. **No scientific identity was machine-checked.** No scientific interpreter/calculator/CAS/program/enumeration/solver/replay/build/test/modelCLI/nested agent/newGO or chosen numeric/state/control/boundary/limit/magnitude/decimal viability probe. Exclusive OWN outputs; frozen bytes unchanged; no Git/deletion/publication. Same18/HOLD/actual substantive checkpoints<=30min/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 unchanged. Ordinary same-harness writing is not formal/kernel/configured-family/human/executable/novelty acceptance. This is incremental ACTIVE original research, not an early final-park or96-hour closeout.
