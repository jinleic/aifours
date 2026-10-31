# f194: global single-split odd-prime-power review

Clock observed before writing: `2026-10-29T09:52:11-0700 PDT` from `/bin/date`. This is one same-harness review, not a human, independent-model-family, formal/kernel, priority, or novelty review.

## Disposition and exact scope

**Theorem A, including the global disjunction: RECONSTRUCTED conditional on the expressly identified Sands and Tijdeman imports.** No fatal or major mathematical defect found. For every anchored tiling with `n > 14`, the reconstructed result is `330 | n`, `3,5,11 | |Q|`, `|P|` is not a power of two, and if the odd part of `|P|` is `p^e`, then `p | |Q|`. Hence **an odd prime divides both cardinalities OR at least two distinct odd primes divide `|P|`**. The alternatives are not asserted to be disjoint, feasible, or sufficient.

**Proposition B: RECONSTRUCTED conditional on those imports**, for every odd prime `p` outside `{3,5,11}`, every `e,K >= 1`, every odd `R` with `165 | R` and `gcd(p,R)=1`, and every `a,b >= 0` with `a+b=K`; `R` may contain arbitrary additional prime powers, including powers of 3, 5 and 11. Under the stated cardinalities no anchored tiling exists. No fatal or major mathematical defect found.

**Exact residual:** tilings with an odd prime shared by `|P|` and `|Q|`, or with at least two different odd primes in `|P|`, remain outside this obstruction; overlap of those alternatives is allowed. There is **no unrestricted no-go, numerical floor, construction, or original-problem solution** here. Corollaries C and D are reconstructed only at their stated family and squarefree-order scopes.

| Claim | F/M/m/INCONCLUSIVE disposition |
|---|---|
| Actual finite-code border caller | F=0, M=0, m=0; reconstructed directly for finite UD, factor-complete codes containing the displayed `S`, not from a converse. |
| Sands divisor exclusion | F=0, M=0, m=0; imported exactly at the stated set/cardinality hypotheses. |
| Tijdeman same-complement dilation | F=0, M=0, **m=1**: the cited page states positive scalars; the packet's unrestricted integer phrasing does not spell out the elementary zero/negative extension. All its applications use positive scalars. The extension is supplied below; no effect on B or A. |
| Reductions, P1–P6, G1, G2, Proposition B | F=0, M=0, m=0 at the quantified scope stated above. |
| Theorem A and Corollaries C,D | F=0, M=0, m=0 at their stated scopes and subject to the same imports. |
| Author's checker output and previously reported counts | **INCONCLUSIVE as independently exercised evidence:** its entire source was read but never executed or imported. Its claimed PASS is not a premise. |
| Original unrestricted completion; independent-family and formal acceptance | **INCONCLUSIVE / not performed.** |

The equivalence to the disjunction concerns the prime-factor conclusions after the separately derived `330 | n` and `3,5,11 | |Q|` facts; the bare disjunction by itself does not encode those additional facts.

## Frozen inputs, actual read order, and imports

1. Read `manifest-v1.json` first among wave/source records; 3,503 bytes / 30 LF; SHA-256 `dfe646ed684a42ca9be0cef0d031db9e48f5f8cf3d131e931eec687914c0194e`, exactly the assigned hash.
2. The manifest contains no separate frozen task-file path. The assignment text was transcribed verbatim as visible, with one terminating LF, into `reviewer-assignment.txt`: 956 bytes / 8 LF, SHA-256 `55642e3499e04e6473b55d119a6f1372c3c5ff48a3d66c33030fa9d89e26dc98`. This is a reviewer-created transcription, **not** a claim of a separately parent-frozen task file or of a hash of an unavailable raw chat transport.
3. Hashed and read every line 1–207, in consecutive short raw windows through the explicit end, of `mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-global-single-split-odd-prime-power-v1.md`: 22,671 bytes / 207 LF; SHA-256 `e7ea40e4988de0e6227e3ff62d1d02632c72ac163c58de71c8d8213b649041ca`.
4. Then hashed and read every line 1–217, in consecutive short raw windows through its ending, of the similarly located `frontier-20261029-global-single-split-odd-prime-power-check-v1.py`: 7,943 bytes / 217 LF; SHA-256 `4dead88fa441d1f21246b9f20978164511c582ffa180d7075223ff6445e30d86`. Only after both complete reads did mathematical assessment and direct named-source reads begin. Neither listed input was modified, executed, or imported.
5. Directly read only the candidate-named source statements: Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1), and Łaba–Londner, [arXiv:2106.14042v3, pp. 3 and 10](https://arxiv.org/pdf/2106.14042v3), with its p. 26 application inspected only for the dilation citation. The source reader first returned the opening 300 rendered lines of each paper, which included text beyond the requested statements; the specific statements were subsequently reread in raw windows. No extra source files or links were opened, and no T2 claim was used. The retrieved **text renderings, not the PDF bytes**, have SHA-256 respectively `0d80aa60d0ee5177da3240f73526f48f67e6d92b65e1755467a491beae5789af` (`artifact://62469`) and `08eafabc57f01bed02c5a7e5d0cb697d9e4d161186ec9f74c0089930b3b0f3f9` (`artifact://62468`). These arXiv papers report the older theorems; the original historical papers were not separately inspected.

No f189, f176, Q55, fibre, T2 or other earlier disposition/result is a premise. No discarded floating checker, held/f161/f162 payload, sibling review, author contact, web search, external model/API, Git operation, or author-code execution was used. The candidate's same-author exposure, prior cadence disclosures, and floating-square-root correction remain historical disclosures, not cleared process findings or inherited mathematical evidence.

## Import fidelity and actual code border

For finite sets in `Z_M`, Sands says `U ⊕ V = Z_M` exactly when `|U||V|=M` and `Div_M(U) ∩ Div_M(V)={M}`, where zero differences give `M`. Only the necessity of divisor exclusion is needed for the proof. The named source states this for sets, with no squarefreeness or prime-count restriction.

The named Tijdeman source states: a finite integer tile `U` with a fixed complement remains a tile with **the same complement** after multiplication by a positive integer `t` coprime to `|U|`. Lift a cyclic complement to `V+M Z`, apply that statement, and reduce modulo `M`; uniqueness forces the `t`-dilation to be injective on `U` even if `gcd(t,M)>1`. Thus `tU ⊕ V=Z_M`. Applying this twice is legitimate when `gcd(t,|U|)=gcd(s,|V|)=1`, since the first dilation preserves cardinality. For the minor wording issue: if `t<0`, apply the positive case to `-t`, then use Sands and `Div_M(-(-t)U)=Div_M((-t)U)` with unchanged cardinality; if `t=0`, coprimality forces `|U|=1`, so `V=Z_M` and the assertion is immediate. Every actual dilation in the packet is positive.

For the border, let `L` be the maximum atom length of a finite UD factor-complete extension `D` containing `S`. An embedded run `a^(2L+1)` has an atom strictly inside it, hence a pure-`a` atom. Two different pure-`a` atoms would commute as distinct atom lists, so exactly one, `a^n`, exists. Since `b` is an atom, no `b^k`, `k>1`, can be another atom. Define `P,Q` from actual atoms `a^i b^k` and `b^l a^j` modulo `n`, with `k,l>=1`. The displayed `S` supplies `A={0,3,8,11} ⊆ P` and `Y={0,1,7,13,14} ⊆ Q`; `n>14` keeps these literal anchors distinct.

For injectivity, suppose two distinct residue pairs give the same sum. Choose actual exponent representatives and a common positive `G` in that residue class exceeding both sums. For large `H,K`, the lists consisting of copies of `b`, the selected `b^l a^j` atom, `(G-i-j)/n` copies of `a^n`, the selected `a^i b^k` atom, and copies of `b` all spell `b^H a^G b^K`. The positive central run identifies any non-`b` boundary atoms. If `i=0` or `j=0`, the relevant pure-`b` atom is exactly `b`, so that boundary residue is zero; distinct pairs still give distinct atom lists. UD forbids the coincidence.

For coverage choose `g>L` in any desired class modulo `n` and embed `b^L a^g b^L` in `D*`. The atom meeting the last left `b` begins inside the left guard and cannot reach the right guard; it is `b^l a^j`. The atom meeting the first right `b` is `a^i b^k`. They are distinct because `g>L`; intervening atoms lie entirely in the `a` run and are `a^n`. Hence `g ≡ i+j (mod n)`. This proves the actual-residue tiling `P⊕Q=Z_n`, without needing to identify factor-completeness with maximality. The cited Cordero statement instead has the explicit finite maximal-code hypothesis; no unproved converse is used.

## Universal reconstruction

Write `Div_n(X)={gcd(x-x',n):x,x'∈X}`. Throughout, differences can be represented by arbitrary integers; parity is well-defined since the eventual order is even.

### Elementary reductions

* If `n` is odd, `gcd(8,n)=1` from the `P` difference `8-0`, matching `gcd(1,n)=1` from `Q`. Likewise, if any `ell∈{3,5,11}` is absent from `n`, a `P` difference of length `ell` has gcd 1. Divisor exclusion contradicts each case. Thus `330 | n`.
* If such `ell` did not divide `|Q|`, dilate `Q` by `ell`. The fixed `P` difference of length `ell` and the scaled `Q` difference `ell(1-0)` both have gcd `ell<n`, a contradiction. Thus all three small primes divide `|Q|`.
* For an odd `Q` difference `x` divisible by one of those `ell`, put `g=gcd(x,n)`. If `g/ell` is coprime to `|P|`, dilate `P` by `g/ell`; its length-`ell` difference has gcd `g`, matching the `Q` difference. Since `g` is odd and `n` even, `g<n`. This is the exact L2 hypothesis, including repeated prime powers.
* If `|P|=2^a`, let `T` be the odd part of `n`. Since `gcd(T,|P|)=1`, `TP⊕Q` tiles and, as `TP` lies in `T Z_n`, the coset argument gives at least one `q∈Q` in each class mod `T`. Select `q≡6 (mod 165)`. For odd `q`, `q-0` is an odd multiple of 3; for even `q`, `q-1` is an odd multiple of 5. The L2 multiplier is odd and therefore coprime to `2^a` in either case. Both cases contradict L2. This includes `a=0`.

The coset argument used here and below is direct: in a tiling `X⊕Z=G` with `X⊆H`, every `u+H` is tiled uniquely by `X` and `Z∩(u+H)`; hence every such intersection has size `|H|/|X|`.

### Fibres and parity

Assume B and put `rho=p^e`, `n=2^K rho R`, `|P|=rho 2^a`, `|Q|=R2^b`. If an odd `x∈Q-Q` is divisible by 3, 5, or 11 but not by `p`, then `gcd(x,n)/ell` is odd and coprime to `p`, hence coprime to `|P|`; L2 rules it out. Thus every such difference is divisible by `p` (P1).

Since `gcd(R,|P|)=1`, `RP⊕Q` tiles and `|Q_u|=2^b` in every class `u mod R`. Since `gcd(rho,|Q|)=1`, `P⊕rho Q` tiles and `|P_gamma|=2^a` in every class `gamma mod rho`. These are genuine nonempty fibres.

For each fixed `u`, identify the subgroup `R Z_n` with `Z_N`, `N=rho 2^K`. The restricted tiling is `V⊕Pbar=Z_N`, where `V=(Q_u-u)/R` and `Pbar=P mod N`. The dilation `RP` is injective, so the projection of `P` to `Pbar` has unchanged cardinality. Since `|V|=2^b`, dilate `V` by `rho`. Restrict to a `gamma mod rho` coset and use CRT to reduce it bijectively modulo `2^K`; this is a genuine tiling of `Z_(2^K)`. Its two factors have odd differences exactly when `P_gamma` and `Q_u`, respectively, are mixed parity. Both cannot have odd differences by divisor exclusion, and neither can both lack them because their sums then have one parity. Consequently for **every** `(gamma,u)` exactly one is mixed, yielding the two global alternatives.

If all `Q_u` are mixed, any even–odd pair within one fibre has difference divisible by `R`, hence by 3, so P1 puts the entire fibre in one class modulo `p`. Even–odd pairs between fibres indexed by `u` and `u+3` or `u+5` do the same; steps 3 and 5 generate `Z_R`. Thus all of `Q` has one residue mod `p`, contradicting `0,1∈Q`. Therefore every `Q_u` has one parity and every `P_gamma` is mixed. Define the nonempty proper partition `E ⊔ O=Z_R` by that single fibre parity; `0∈E` and `1∈O`.

### Nonsquarefree separation and stabilizer

The identity used is valid with arbitrary valuations: if `g0=gcd(y,R)` and `g0|h|R`, write `y=g0 z`; then `gcd(z,R/g0)=1`, so `gcd((h/g0)y,R)=h`. It includes `y=0`, although the odd-difference applications here have `y≠0` as an integer representative.

Take an odd difference `y` of two elements of the same `P_gamma`, so `rho|y`, and put `g0=gcd(y,R)`. Suppose an `E` and an `O` fibre agree mod `g0`; select `q,q'` from them, let `x=q-q'` and `h=gcd(x,R)`. Then `x` is odd and `g0|h|R`. Set `t=h/g0`, `s=rho`. The first is an odd divisor of `R` and hence coprime to `|P|`; the second is coprime to `|Q|`. In `tP⊕rho Q`, transport and truncation at the **full** `rho` factor of `n` give

`gcd(t y,n)=rho h=gcd(rho x,n)<n`.

The equality remains true when `x` is divisible by any power of `p`, or `y/rho` itself has extra `p` factors, because `n` has exactly `p^e` and `p∤R`. This contradicts Sands. Every mod-`g0` class therefore has a single colour, so `E` is invariant under addition of `g0`.

The stabilizer of `E` in cyclic `Z_R` is `pi Z_R` for one divisor `pi|R`; because `E` is nonempty proper, `pi>1`. Each separation gives `pi|g0`. Thus each mixed `P_gamma` has all its elements congruent mod `pi`: opposite parities compare directly and equal parities compare through an element of the other parity. No assumption that `R` is squarefree or that `pi=R` is made.

### G1 and `165 | pi`

Suppose one `ell∈{3,5,11}` does not divide `pi`. Remove **the full power** `ell^c || R`, set `M=R/ell^c`, and use `pi|M` and `gcd(ell^c,M)=1`. Each colour is the full `ell^c` coordinate times a nonempty colour class on `Z_M`. A fixed full-coordinate layer is complete bipartite under agreement mod `ell`. With the two other small-prime coordinates `q1,q2`, choose one `E'` vertex and one `O'` vertex; CRT supplies a `z` agreeing with the first mod `q1` and the second mod `q2`. Whichever colour `z` has, it forms an opposite-colour pair agreeing on one of these coordinates. Lifting that pair to arbitrary full-`ell^c` layers links every pair of layers; the graph is connected. The proof permits `pi` to be a proper divisor of `M` and permits arbitrary other prime powers.

For each graph edge, any selected elements of its opposite-parity `Q` fibres have odd difference divisible by one of the three primes; P1 puts all their elements in one class mod `p`. Connectivity would force all of `Q` into one class, contrary to `0,1∈Q`. Thus no small prime is absent from `pi`, i.e. `165|pi`.

### The `w` edge and CRT-layer G2

As `P_0` is mixed and contains 0, choose odd `v0∈P_0`. The stabilizer argument makes `pi|v0`; the fibre definition gives `rho|v0`. Put `y*=8-v0` and `w=gcd(y*,R)`. The difference is odd, `y*≡8 (mod pi)` and `y*≡8 (mod rho)`. Since `pi` and `p` are odd, `gcd(w,pi)=1` and `gcd(y*,p)=1` even if `y*` is negative.

If an odd `Q` difference `x` is divisible by `w` but not by `p`, put `h=gcd(x,R)` and `t=h/w`. Then `t` is odd and supported on `R`, so it is coprime to `|P|`. Transport gives `gcd(t y*,n)=h`, while oddness and `p∤x` give `gcd(x,n)=h`. This proper common divisor contradicts Sands after dilating `P`. Therefore every odd `Q` difference divisible by `w` is divisible by `p`. When `w=1`, the difference `1-0` already contradicts this rule.

For the general graph proof, `pi|R`, `w|R`, and `gcd(pi,w)=1` imply `pi w|R`, not necessarily equality. Every layer `u≡j (mod w)` contains both colours by CRT: lift any chosen opposite-coloured classes modulo `pi` into that layer. Its induced graph is complete bipartite through agreement mod `w`. Within `Z_pi`, choose `e∈E` and `o∈O`; if they agree mod 3 or 5 they are a bridge, and otherwise choose `z≡e (mod 3)`, `z≡o (mod 5)`. Its colour gives an opposite-coloured pair agreeing on one of those primes. CRT lifts the pair to any two `w`-layers; the extra factor `R/(pi w)` is unrestricted. Hence the combined graph with agreement mod 3, 5, 11, or `w` is connected. The case `w=1` is a single complete bipartite layer. Prime edges invoke P1; `w`-edges invoke the new tail rule. Every edge propagates a common `p` residue to all elements in both nonempty fibres, so connectivity contradicts `0,1∈Q`. This proves B.

### Global callers and limits

If `|P|` has only one odd prime `p`, say odd part `p^e`, and `p∤|Q|`, the small-prime allocation forces `p∉{3,5,11}`. Because `|P||Q|=n`, the entire `p`-power of `n` is `p^e` and the odd part of `|Q|` is a coprime `R` divisible by 165. Thus B applies. Together with L3 this is exactly the announced disjunction.

At `n=165 p^s 2^K`, the first powers of 3, 5 and 11 all lie in `|Q|`; L3 excludes `p^0` in `|P|`, and B excludes `p^s`, leaving `1≤j≤s-1`. This interval is empty at `s=1`; with no `p` present, L3 excludes the remaining cardinality. For squarefree odd `n`, the two odd cardinalities are coprime, and L1 assigns 3, 5 and 11 to `|Q|`; A consequently requires at least two other distinct odd primes in `|P|`.

Boundary audit: `K=0` cannot occur after the initial odd-order exclusion; B explicitly requires `K≥1`. `e=0` is outside B and is handled by L3; `p=2` is outside the odd-prime case; `p∈{3,5,11}` cannot satisfy `gcd(p,R)=1` when `165|R`. At `a=0`, each `P_gamma` is a singleton so only the mixed-`Q` branch is possible and it is contradicted; at `b=0`, each `Q_u` is a singleton and the other branch applies. `K=1`, `w=1`, `pi=R`, repeated powers in `R`, and arbitrary higher `e` do not require a separate unproved step. Limits are universal written arguments, not extrapolations from finite controls.

## Reviewer-owned bounded controls and audit trail

The control source imports no author code. The first one-shot run was **FAIL**, exit 1, at `/bin/date` `2026-10-29T09:50:38-0700 PDT`: my control mistakenly required every internal prefix-tree child to be a completed atom, rather than a prefix. Its source was preserved unchanged as `reviewer-controls-initial.py`; its stderr and receipt remain. This was a control-fixture implementation error, not an observed defect in the candidate. I corrected that one check and used separately named output/receipt files; neither failure nor its artifacts was erased.

The corrected run used a 100-second wall cap (a timeout is `UNKNOWN`, never exclusion), `/bin/date` start and end both `2026-10-29T09:51:23-0700 PDT`, exit `0`, stderr empty, result `PASS`. It used exact integer arithmetic; no float, solver, CAS, or author data/code execution. It establishes only the finite cases below:

* A real complete prefix-code border control `D={aa,ab,b}` gives `P={0,1},Q={0}` mod 2. Adding `ba` makes `b·ab=ba·b` and is rejected specifically as `BORDER_DUPLICATE_SUM`.
* Exhaustive Sands equivalence among all set pairs of cardinality product `n` at `n=1,2,4,6,8` checked respectively `1,4,44,612,3936` pairs. A common proper divisor is rejected by `SANDS_COMMON_NONTRIVIAL_DIVISOR`. At `n=60`, scalar 2 is coprime to `|P|=3` but not a unit mod 60, and the original complement remains valid; scalar 3 fails the stated coprimality and the direct tiling.
* 485 transport identities include zero/negative `y` and nonsquarefree `R`. For `R=495,y=9,h=45`, the correct result is 45; replacing 9 by 3 loses a prime power and gives 15. Invalid `h` is rejected specifically for not dividing `R` or not being divisible by `g0`. The P5 collision `rho=49,R=495,K=2,y=441,x=15435` has `g0=9,h=45,t=5`, both gcds 2205, even though `p^3|x`. Omitting `rho|y` produces 45 versus 2205; the intended missing-hypothesis rejection is recorded.
* Twenty actual, **unanchored** constructed cyclic tilings exercise `R=165,495`, `rho=7,49`, `K=1,2`, every `0≤a≤K`, both parity branches and `a=0`/`b=0`. Every `P_gamma,Q_u` fibre was checked; quotient and CRT tilings were checked for `u=0,1,R-1` and every `gamma`. These are sanity controls, not witnesses for the target.
* G1 exact graph controls removed the full powers `3²`, `5²`, and `11²` in `(R,pi)=(3465,385),(2475,99),(9075,75)`; each graph had one component. With `R=165,pi=165,E={0}`, removing the free-coordinate hypothesis yields 81 components. Attempting CRT after removing only one 3 from `495` is rejected as noncoprime.
* G2 has a one-component positive at `(R,pi,w)=(32175,165,13)` with `R/(pi w)=15`, and at `w=1`. The coprimality-negative `(165,165,3), E={0}` has 81 components. A separate stabilizer example has `R=45,pi=9` and periods `{0,9,18,27,36}`; a mixed residue class mod 3 is rejected for that exact reason.
* The tail control uses `p=7,e=2,K=2,R=32175,pi=165,v0=40425`, giving `y*=-40417,w=13`, and both relevant gcds 13 for `x=13`. Negative controls reject even `x` and `p|x` for those respective hypotheses; with `x=91` the unscaled gcd is 91, not 13.

Artifacts and SHA-256 (all in this wave directory):

| Artifact | SHA-256 |
|---|---|
| `reviewer-controls-input.json` | `e8675ac97ca6fcfffc6814287768bf2491f051d1add63be87edfee0fa3228cf0` |
| `reviewer-controls-initial.py` | `a2bbd26b245623d8181a2977ed748e36a1a0c7103595973fcb04fdf659c58c78` |
| `reviewer-controls.py` corrected source | `9aeb965fa29b0d76a7b509728d9a26b165f1aea749259ff37ffedc05148cb54d` |
| `reviewer-run-controls.py` first runner | `d8c106ccbb8b67ddc437c7acf1eb98e0e70e5a2b4b76213272b3e17b81084f94` |
| `reviewer-run-controls-v2.py` corrected-run runner | `c24ca4a337373166ab88054a5db51c2c161083405acb1a9984d08be5384d5ad3` |
| `reviewer-controls-output.json` first, empty | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `reviewer-controls-stderr.txt` first failure | `00f61cbb42d83f5ce5c690d8cee7fc20832d765c224cbfd0336e166bb3cfbf58` |
| `reviewer-controls-receipt.json` first failure | `f35edfe0d901998aac87a08475a28ddee0387068e2f062a362ce7f7152149638` |
| `reviewer-controls-output-v2.json` | `f066ca34611d8e44bcc436846926cd1e113dece35b8055ef884063646f0bb669` |
| `reviewer-controls-stderr-v2.txt` empty | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `reviewer-controls-receipt-v2.json` | `bd6735a691bc6375b5790da9ff29633da655a83d1072c639e25e0128da0f72e5` |

The report's own hash is recorded separately in `reviewer-review-sha256.txt` to avoid a self-referential hash. These controls do not prove universal B, settle its literal residual, verify source novelty, or substitute for independent-family/formal acceptance.
