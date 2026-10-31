# f212: independent same-harness review of the all-powers-of-three head obstruction

**Disposition: 0 F / 0 M / 0 m.** The written three-class theorem and the stated `55·3^v·2^K` consequence are supported by the reconstructions below. **INCONCLUSIVE:** the author’s historical execution/provenance statements, external citation accuracy and unrestricted-problem status were not independently checked; a full manifest digest comparison against an independently supplied 64-hex value is unavailable because the assignment supplied only the 12-hex prefix. These inconclusives are not mathematical counterexamples or affirmative verifications of those matters.

Native `/bin/date` observed immediately before writing this review: `2026-10-29T13:18:04-0700 PDT`. This is an observation before writing, not an asserted file creation time.

## Frozen inputs and actual sequence

1. The first research artifact opened was `manifest-v1.json` in this wave. Its measured SHA-256 was `0e2ff99e17baac8061523c331c6a1cfb87c8beaf6b6eba96eaa625129d387ec4`, which matches the **entire supplied prefix** `0e2ff99e17ba`. No full expected manifest digest was supplied, so I do not claim an independently pinned full-digest match.
2. Before opening either declared input body, `shasum -a 256` and `wc -c -l` measured **both**. In manifest order:
   - `dispositions/math-5-shor-165-powers-two-all-tail-conditional-parent-v1.md`: SHA-256 `059616d47a482b46fa647722646df69482de71d87cfda54ad67c95801667a47a`; **6,184 bytes, 34 LF**. All three agree with the manifest.
   - `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-all-powers-three-head-obstruction-v1.md`: SHA-256 `7146bd0f6b5c8e00d3221d173b8610f3c494f4faba6ad994f864132e231f8ca7`; **11,691 bytes, 116 LF**. All three agree with the manifest.
3. I displayed all of the first body in raw windows **1–12, 13–24, 25–34**, then all of the second in raw windows **1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–116**. Thus both final lines were displayed; no body was read before the integrity measurements. Mathematical reconstruction and controls followed the complete ordered reads.
4. Workspace memory summary and the independent-snapshot-review skill were read only as process guidance, not as mathematical evidence. The skill’s external-model workflow was not invoked. No linked body, author checker, sibling review, web source, other model/API, author communication, or held material was opened or used as evidence.

## Per-claim verdicts

| Claim / boundary | Verdict | Basis and limitations |
|---|---|---|
| `n>14`, anchored tiling, and head `3^e·2^a`, `e≥1` imply `330|n`, `3,5,11` divide `|Q|`, hence `990|n` | **0F/0M/0m** | Independently derived below, including nonzero-difference and scalar-injectivity checks. |
| Universal `Q` coverage mod 55 and opposite-parity rules U and V | **0F/0M/0m** | Derived for arbitrary remaining prime powers; no transversal or same-parity rule assumed. |
| The three-class contradiction for 3, 25 and 45 | **0F/0M/0m** | Each parity and mod-9 step is reconstructed below; exact projection and intended-reason negatives independently controlled. |
| The theorem for every `e≥1`, `a≥0` and every `n>14` in its hypotheses | **0F/0M/0m** | Follows from the universal argument, not the finite scan; no T2 or parent family theorem used. |
| `n=55·3^v·2^K`, `K,v≥1`, including the `e=0` case | **0F/0M/0m** | Squarefree allocation and the separate pure-two-head contradiction are shown; all claimed orders, no larger family. |
| Actual finite-UD factor-complete code caller, with the stated code and actual borders | **0F/0M/0m** | Independently reconstructed with finite guards and one actual code, conditional on the stipulated definitions of UD and factor-completeness. The cited external theorem’s bibliography is not checked. |
| Stated finite projection, the three literal domains and bounded generic multiplier count | **0F/0M/0m** for the mathematical quantities | Independently recomputed by a reviewer-authored control. This does not establish that the author’s separate program ran or had the reported bytes/output. |
| Author-run `PASS`, historical provenance, exploratory process and non-premise assertions | **INCONCLUSIVE** | No author program, historical record, linked packet or author communication was examined. None is a premise of this review. |
| Exact bibliographic wording of external cited theorems; novelty and present unrestricted-problem status | **INCONCLUSIVE** | No literature/source expansion or status search permitted. The narrower mathematical argument does not establish novelty or worldwide open status. |
| Full expected manifest SHA-256 | **INCONCLUSIVE** beyond the supplied prefix | Measured complete digest and the supplied 12-character prefix are recorded above. |

## Independent reconstruction of the needed finite-tiling tools

These arguments establish the two named tiling tools in the particular finite cyclic setting needed here, rather than extending the pinned 165-family disposition by inference. Let `G=Z_n`, with a direct tiling `P⊕Q=G`. Its pair map is bijective, so `|P||Q|=n`.

**Dilation, including injectivity.** For a prime `p` not dividing `|P|`, work in the group algebra over `F_p`. With masks `A=Σ_(u∈P) X^u`, `B=Σ_(v∈Q) X^v` and `J=Σ_(g∈G) X^g`, the tiling is `AB=J`. Frobenius gives `A(X^p)=A(X)^p`; also `AJ=|P|J`. Therefore

`A(X^p)B = A(X)^(p−1)J = |P|^(p−1)J = J` in characteristic `p`, by Fermat’s congruence.

The integer coefficient at each residue in `A(X^p)B` counts pairs and is nonnegative and congruent to 1 modulo `p`; hence it is at least 1. Their total is `|P||Q|=n`, so every coefficient is exactly 1. Thus `pP⊕Q=G`, and `p` is injective on `P` (otherwise any fixed `q∈Q` gives two pairs at one residue). Iterating prime factors gives the same for every positive `t` coprime to `|P|`. An arbitrary integer `t` has a positive representative modulo `n` with the same gcd with `|P|`, because `|P|` divides `n`; this gives the stated scalar version. Interchanging the two factors is symmetric.

**Divisor exclusion.** Suppose nonzero differences `p1−p2` and `q1−q2` have the same gcd `g<n` with `n`. Write `d=n/g`, `p1−p2=gA`, and `q1−q2=gB`; both `A,B` are units modulo `d`. Choose `u≡B A^(−1) (mod d)`. By CRT, additionally choose `u` nonzero modulo each prime dividing `n` but not `d`. Then `gcd(u,n)=1`, so `gcd(u,|P|)=1`, and `u(p1−p2)≡q1−q2 (mod n)`. In the dilated tiling `uP⊕Q`, the distinct pairs `(up1,q2)` and `(up2,q1)` have the same sum, a contradiction. This proves precisely the Sands-form exclusion used below. CRT, elementary finite-field/Fermat arithmetic and the definition of a finite direct tiling are the only elementary inputs to these two reconstructions.

**Coset fact.** If `X⊕Z=G` and `X` is contained in a subgroup `H`, then a representation of any element in a coset `u+H` uses a `Z`-element in that same coset. Thus `Z` meets every coset. This does not say that there is only one such `Z`-element.

## Universal reductions and rules

Assume a hypothetical anchored tiling with `n>14`, `A={0,3,8,11}⊆P`, `Y={0,1,7,13,14}⊆Q`, and `|P|=3^e2^a`, `e≥1`, `a≥0`.

1. If `n` is odd, the nonzero `P`-difference `8` and `Q`-difference `1` each have gcd 1 with `n`, contradicting divisor exclusion. If one of `3,5,11` is absent from `n`, use respectively the nonzero `P`-difference `3−0`, `8−3`, or `11−0`, and again the `Q`-difference `1−0`: both gcds are 1. The assumption `n>14` ensures all of these displayed differences are nonzero modulo `n`. Hence `330|n`.
2. If `ℓ∈{3,5,11}` failed to divide `|Q|`, dilation gives `P⊕ℓQ`; the `P`-difference `ℓ` and the dilated `Q`-difference `ℓ(1−0)` are the same nonzero residue, contradicting divisor exclusion. Thus all three divide `|Q|`. In particular 3 divides both cardinalities, so `9|n`. Write `n=2^K3^vT`, where `K≥1`, `v≥e+1`, `gcd(T,6)=1`, and `55|T`; consequently `990|n`.
3. `gcd(T,|P|)=1`, so `TP⊕Q=Z_n`. Since `T|n`, `TP` lies in the subgroup `TZ_n`, whose cosets are the residue classes modulo `T`. The coset fact makes `Q` meet **every** class modulo `T`, and therefore every class modulo 55, regardless of tail multiplicities.

For any odd difference `x=q−q'` of actual `Q`-elements, `g=gcd(x,n)` is odd and `g<n`, since `n` is even. The difference is nonzero modulo `n`. All congruences and parities used below are well-defined on `Z_n` because `990|n`.

- **U:** If `3|x` but `9∤x`, then `v_3(g)=1`. The positive scalar `t=g/3` is odd and not divisible by 3, hence coprime to `3^e2^a`. In `tP⊕Q`, the scaled anchor difference `t(3−0)=g` has gcd `g` with `n`, as does `x`, contradicting divisor exclusion. Thus `3|x ⇒ 9|x`.
- **V:** If `5|x` or `11|x` and `3|x`, U gives `9|x`. Otherwise take a dividing `ℓ∈{5,11}`. Then `t=g/ℓ` is an integer, odd, and not divisible by 3; it is coprime to `|P|`. The scaled `P`-difference `ℓt=g` collides in gcd with `x`, a contradiction. Hence `5|x` or `11|x` also implies `9|x`.

No inference is made from U or V for a same-parity pair. Extra prime powers only change `g`; the required coprimality still follows from its oddness and its 3-adic valuation.

## Written three-class contradiction

The actual odd anchors `1,7,13` are all `1 (mod 3)` but are respectively `1,7,4 (mod 9)`. If an even `q∈Q` were `1 (mod 3)`, each difference `q−1`, `q−7`, `q−13` would be odd and divisible by 3. U would require `q` to equal all three distinct residues modulo 9. Therefore **no even `Q`-element is 1 modulo 3**.

By coverage choose actual elements `x3,x25,x45∈Q` in classes 3, 25, 45 modulo 55. The classes are distinct from one another and from the named anchors; representatives are arbitrary, not the finite representatives used in the control.

1. If `x3` were even, `x3−13` would be odd and divisible by 5, so V would give `x3≡13≡4 (mod 9)`, contrary to the preceding observation. Thus `x3` is odd. Now `x3−14` is odd and divisible by 11, so V gives `x3≡14≡5 (mod 9)`.
2. If `x45` were even, `x45−1` would be odd and divisible by 11, so V would give `x45≡1 (mod 9)`, again impossible. Thus `x45` is odd. Its difference from the even anchor 0 is divisible by 5, so V gives `x45≡0 (mod 9)`.
3. If `x25` were odd, comparison with the even anchors 0 and 14 would use divisibility by 5 and 11 respectively, forcing both `x25≡0` and `x25≡5 (mod 9)`. Therefore `x25` is even.
4. `x25−x3` is odd and divisible by 11 because the class difference is 22, so V forces `x25≡5 (mod 9)`. But `x25−x45` is odd and divisible by 5 because the class difference is −20, so V forces `x25≡0 (mod 9)`. Contradiction.

This proves the claimed universal head-cardinality theorem. The finite modulus-990 control below is only a check on this written argument, not the quantifier step.

## All orders `55·3^v·2^K` and the actual-code caller

Let `n=55·3^v·2^K`, `K,v≥1`, and suppose an anchored tiling exists. The reduction above puts 5 and 11 in `|Q|`; they occur only to the first power in `n`, so neither divides `|P|`. Also 3 divides `|Q|`. Hence `|P|=3^e2^a` with `0≤e≤v−1`. The theorem excludes `e≥1`.

For `e=0`, put `|P|=2^a` and let the odd part `T=55·3^v`. It is coprime to `|P|`; dilation and the coset fact show that `Q` meets every class modulo `T`. Since `165|T`, choose `q∈Q` with `q≡6 (mod 165)`.

For an odd `Q`-difference `x` divisible by `ℓ∈{3,5,11}`, `g=gcd(x,n)` is odd, divisible by `ℓ`, and smaller than even `n`. Then `t=g/ℓ` is odd and coprime to `2^a`; the `P`-difference `ℓ`, after dilation by `t`, has the same gcd `g` as `x`, impossible. If the chosen `q` is odd, `q−0` is an odd difference divisible by 3; if it is even, `q−1` is an odd difference divisible by 5. Both cases contradict the preceding sentence. Thus no anchored tiling exists in this family. Writing `v=s+1` gives exactly `165·3^s·2^K` for `s≥0`, `K≥1`; this is not an unrestricted order exclusion.

For the literal code in the candidate, the first block contains `b` and the actual tails `ba^j`, `j∈Y`; the other two blocks contain `a^i b`, `i∈A` (including `i=0` via `b`). Here is an independent reconstruction of the same-code bridge.

Let a hypothetical extension `D` be finite, uniquely decipherable and factor-complete, and let `L` be its maximum codeword length. If no codeword were a pure positive power of `a`, an `a`-run in a word of `D*` could cross at most one codeword boundary and would have length at most `2L`; factor-completeness supplies arbitrarily long `a`-runs, a contradiction. Two distinct pure-`a` codewords `a^r,a^s` would violate unique decipherability via `(a^r)^s=(a^s)^r`. Thus there is a unique actual pure-`a` atom `a^n`.

Define `P,Q` exactly as in the candidate from actual codewords `a^i b^k` and `b^ℓ a^j`. To prove coverage, take `b^H a^G b^K` as a factor of a word in `D*`, with `H,K>L` and `G>L`. The atom containing the last left `b` is wholly inside the guard and has form `b^ℓ a^j`; the distinct atom containing the first right `b` has form `a^i b^k`; every atom strictly between them is the unique pure-`a` atom. Therefore `G=j+mn+i`, so `G mod n∈P+Q`. Choosing sufficiently large `G` in any desired residue class proves coverage.

For directness, if two actual pairs `(i,j)` and `(i',j')` have the same sum modulo `n`, choose a common sufficiently large `G=i+j+mn=i'+j'+m'n`, and take guards `H,K` larger than `L` and all indicated `b` exponents. Each pair constructs a factorization of the same word `b^H a^G b^K`: repeat the actual codeword `b`, then use the corresponding `b^ℓ a^j`, `m` copies of `a^n`, the corresponding `a^i b^k`, and finally repeat `b`. Unique decipherability makes the two codeword sequences identical. Since `G>L`, the atom containing the last left `b` and the distinct atom containing the first right `b` are determined by that sequence, forcing the same `j` and `i`, hence the same residues. Thus `P⊕Q=Z_n`, with the displayed anchors in the same actual code. Applying the theorem and order consequence rules out the stated actual head sizes and pure-`a` orders; no arbitrary cyclic tiling is asserted to construct a completion. The universal head theorem is stated only for `n>14`; no smaller-order claim is made.

## Reviewer-authored exact controls and receipts

Single control script: `reviewer-f212-control-v1.py` in this wave; SHA-256 `474d4511654f95e0b4010b388476e494ed7e2ec114ab99464b4e70df06604d5e`. It uses Python integer arithmetic and standard-library operations only, is independently authored, and neither reads nor executes author code. The one run used `/usr/bin/python3 -B`; native `/bin/date` reported start `2026-10-29T13:16:29-0700 PDT`, end `2026-10-29T13:16:30-0700 PDT`; **exit 0**, with a 120-second execution limit. There was no cap or timeout. A capped or timed-out run would be UNKNOWN, not an exclusion.

- Independently checked all **980,100 ordered pairs** modulo 990: the U/V test agrees there with excluding odd-difference gcds `{3,5,11,15,33,55,165}`. This finite equivalence is not claimed to be the full gcd list for arbitrary larger `n`.
- Filtering all 990 types against the five anchors left **257**; none was even and `1 (mod 3)`. The respective literal representatives modulo 990 were `x3={113}`, `x25={80,300,410,630,740,960}`, `x45={45}`. Their `(parity, mod 9)` domains are exactly `{(1,5)}`, `{(0,0),(0,2),(0,3),(0,5),(0,6),(0,8)}`, and `{(1,0)}`. All **six** triples failed the two final edges jointly.
- Intended-reason negatives: dropping only edge `(3,25)` permits `(113,630,45)`, whose sole failed omitted edge is `(3,25)`; dropping only `(25,45)` permits `(113,410,45)`, whose sole failed omitted edge is `(25,45)`. Dropping U permits `(58,80,100)` and dropping V permits `(113,25,45)` under the corresponding weakened rules; each violates the original full rules. Removing anchor 14 permits `(113,135,45)` with the remaining four anchors, but reintroducing 14 makes the pair with 135 violate V. These are local relaxation witnesses, not tilings.
- **25,600** independently generated multiplier checks used `e=1,…,4`, `K=1,…,4`, `v=e+1,e+2`, `T∈{55,275,605,715}` and the relevant odd `1≤x<990`. In each, the constructed `t` was coprime to `3^e2^K` and its scaled anchor difference had gcd `g`; this is stronger than needed for every `a≤K`. Separately **1,200** pure-two-case checks covered `v,K=1,…,4`, all `q≡6 (mod 165)` within the sampled orders, both parities, and all `a≤K`.
- Admissibility negatives: at `n=990,x=15,ℓ=5`, the illicit shortcut gives `g=15,t=3`, not coprime to a head divisible by 3; this is why the V branch first handles `3|x` with U. At `n=990,x=10,ℓ=5`, the even-difference shortcut gives `g=10,t=2`, not coprime to head 6; this illustrates why the odd/opposite-parity hypothesis matters.

The grid, negative examples and script success are bounded controls only. The all-exponent result rests on the written gcd/dilation and three-class reconstruction, not on enumeration, author PASS, a search failure, or a timeout.

## Import boundary, gaps and deviations

The pinned parent disposition expressly states its own `165·2^t` family and names classical imports; its linked bodies, historical reviews, T2 result and earlier family conclusion are **not** premises here. The candidate names actual-border, Sands and Tijdeman imports; their finite-cyclic statements needed for this assignment are independently reconstructed above from the explicitly stated elementary arithmetic/group-algebra facts and the definition of the coding hypotheses. This does not verify the precise wording or attribution of the candidate’s external citations. Those elementary facts and the ordinary definitions of UD, factor-completeness and cyclic tiling remain explicit background assumptions, not a formal proof certificate.

No unrestricted completion/noncompletion claim, new order floor, novelty claim, current literature-status certification, or stronger prime-family claim follows. Actual author checker execution and provenance were not verified. The full manifest digest was measured but only its supplied 12-hex prefix could be independently compared. Apart from that limitation of the supplied manifest pin, there were no deviations from the scoped reading, evidence, ownership or control contract; no input or infrastructure was edited, no author code was run, and no Git/build/lint/test/formatter or external-model workflow was invoked.

This is **same-harness** review, not human review, independent-model-family review, formal/kernel verification, or novelty verification.
