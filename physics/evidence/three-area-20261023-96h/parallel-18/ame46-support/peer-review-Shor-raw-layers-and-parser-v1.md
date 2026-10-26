# Peer reconstruction — Shor raw2/3-a layers, free-end parser, four-a table and endpoint

Reviewer: PhysicsAME46, primary slot physics-6 retained. Actual clocks observed: review startup `2026-10-23T15:08:18-0700`; immediately before this output `2026-10-23T15:11:31-0700`. Assignment: `peer-review-wave-eighteen-v2.json`, PhysicsAME46 entry and common contract. Only this new review file is written. No author/shared edits, scientific executable, arithmetic program, enumeration, solver, compilation, tests, CLI or nested agent.

## 1. Pins, exposure and complete read coverage

The three assigned source SHA256 values were observed with shasum and match exactly:

| Source in sibling mathematics `parallel-18/shor-completion/` | Observed SHA256 | Coverage |
|---|---|---|
| `proof-RAW-TWO-THREE-A-LAYERS-v1.md` | `0614a8e399f789397cdfaf4c6c6adb3d514f884264f6bc5fbd9e22cd71465ba2` | Complete188 lines |
| `proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md` | `adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb` | Complete163 lines |
| `proof-RAW-TAIL-ENDPOINT-COROLLARY-v1.md` | `4dca62723aa4f87aeb078d5fde1899e3c74c0c9dbffdeb4fa3025708404fb75c` | Complete98 lines |

All required dependency bodies were also read completely and their identities observed:

- `selection-v1.md`,60 lines: `d7ac86b0c69dc96b82361d16c17145593e47b6c3d8dce7c99a539bf34be00ba3`.
- `raw-realization-protocol-v1.md`,144 lines: `544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578`.
- `proof-BERNOULLI-TAIL-REALIZATION-v1.md`,161 lines: `3918ca67108d0dc98620760209474cc306750110d910dbdb2fd167d7eea48de3`.
- Actual dossier `mathematics/shor-code-finite-completion/evidence/raw-instance.json`: `6eb38f63bfee602369a09b22be26a0c598111f33b8202d44349786903f63ecf4`.
- Actual book transcription `mathematics/shor-code-finite-completion/source/problem.zh.txt`,30 lines: `642b818093ac231cbc44006dc324d73492c6ad9a9b71c469a327cbb4307a75c8`.

The literal16 pairs agree between the selection, raw-instance record and book transcription. They are the five i=0 pairs j=0,1,7,13,14; the four i=3 and four i=8 pairs j=0,2,4,6; and the three i=11 pairs j=0,1,2. The book's completeness quantifier is actual factor completeness: every binary w is a factor of some word of M*, not prefix completeness or residue membership.

Exposure: before this assignment I had the shared roster/memory's broad unresolved-Shor context and the parent's packet descriptions; these are not a blind input. I had not previously reviewed these three proof bodies. This is a supplied-proof same-harness reconstruction by another problem owner, not cross-vendor, human, formal/kernel or novelty certification.

## 2. Verdict and precise scope

**0 FATAL / 0 MAJOR / 0 MINOR findings. No substantive defect found at the stated quantified scopes.**

The first source's raw two-/three-a conclusions apply to EVERY hypothetical finite UD factor-complete M containing the exact C, without a homogeneous-tail, maximum-length or residue-realization assumption. The GP equivalence applies to every finite raw M containing b and no other pure-b word. Its automaton certificate is only a criterion for an actually supplied candidate. The endpoint result is correctly restricted to M=C∪T_n with all extra words of length n and n≥5.

None of these conclusions supplies a UD complete extension, proves unrestricted noncompletion, imposes a new pure-a order bound, or upgrades a Bernoulli-saturated ambiguous raw set into a code. The paper/source-status and novelty gates are not assessed by this mathematical review.

## 3. Reconstruction of the all-completion layer argument

### 3.1 Bernoulli mass equality from UD and factor completeness

Layers LF35–68 is self-contained and sound. For positive letter probabilities x,1−x, distinct lists of q codewords produce distinct words of lengths q through qD, so f(x)^q≤qD−q+1. This establishes f≤1 without a prefix-code hypothesis. Under f<1, UD permits the exact geometric sum over M*: each concatenation has one list, including the empty list, giving total mass1/(1−f).

Factor completeness lets one choose an occurrence of ANY word w in a product and trim whole codewords on its two sides. The remaining prefix/suffix lengths are each at most D−1. For each resulting z and pair of lengths the middle word is determined, and its mass is bounded by min(x,1−x)^(−2D+2) times the mass of z. Summing over at most D² end-length choices bounds the mass of all binary words by a finite number, contradicting mass1 at every length. The argument needs no injective choice of z across all w; bounded multiplicity per(z,end lengths) is sufficient and is exactly what is proved.

Thus f(x)=1 for every0<x<1 and, since M is finite, polynomial coefficient comparison at0 is justified. UD with b rules out every other pure-b codeword. The x coefficient gives one one-a word, necessarily ba. The b and ba contributions are1−x². The x² coefficient forces exactly one two-a word; if it has v b's, its x³ coefficient is−v and the three-a count must be v. These are identities, not sampled derivative values.

### 3.2 Raw padding and the unique adjacent two-a word

Layers LF70–113 is sound. Two distinct codewords with the same internal a-core yield genuinely different lists after leading/trailing b-padding to common maxima; b supplies every padding symbol. For completeness forcing, a2D margin prevents a codeword meeting an a of the displayed core from reaching an outside a, because its entire length is at most D. The a-positions are therefore partitioned by actual smaller-layer words or covered by one word with that exact core.

The core a² cannot split into two one-a words: ba would need a b immediately before the second a, where the first a actually sits. The unique two-a word is therefore b^r a² b^t. The three displayed collisions correctly eliminate all zero-delay cases:

- a² itself would factor the literal a⁸b as(a²)^4 b;
- for r=0,t≥1, ba·a²b^t=b·a³b·b^(t−1);
- for t=0,r≥1, b^r a²·a¹¹b=b^(r−1)·ba¹³·b.

All participating fixed words are in C and the lists are distinct. Hence r,t≥1 and N3=r+t.

### 3.3 Exhaustion and every delay inequality

For1≤s<r, the core a b^s a² has no proper lower-layer parse: its terminal adjacent pair must be W, whose leading delay requires s≥r. Three ba words fail at the adjacent pair; the other2+1 placement cannot match W's internal zero gap. Thus one U_s is forced. Likewise a²b^s a for1≤s≤t would require W followed by ba with boundary gap at least t+1, forcing one V_s. The literal a³b supplies the all-adjacent core. Outer padding gives uniqueness of every core, and1+(r−1)+t=r+t exhausts N3. This excludes all other three-a words, including three separated a's; no ansatz has been substituted for arbitrary M.

The three raw ambiguity identities in LF141–159 were reconstructed literally. They give beta_s≥1 for all U_s, alpha_1≥1 when r≥2, and gamma_s≥1 only for s≥2. At s=2 the last collision has zero intervening b's and remains valid; at s=1 it would require a negative exponent and is correctly NOT used. Empty U ranges and zero outer delays elsewhere remain allowed.

The homogeneous equations r+t=n−2 and alpha_s+beta_s=gamma_s+delta_s=n−3−s are applied only where the corresponding word is extra and length n. C has no two-a word and its only three-a word is a³b. The conditional r=1 exclusion for n≥5 correctly uses t=n−3≥2 and the already-proved gamma_t≥1.

## 4. Reconstruction of GP and the finite certificate interface

### 4.1 Both directions, empty list and zero gaps

Parser LF9–36 is an exact equivalence. A finite gap list of length ell represents q=ell+1 a-positions; thus the EMPTY gap list means one a-position, not the zero-a word. Its unique parse requires exactly one one-a codeword. Pure-b words, including the empty concatenation, are separately handled by the sole pure-b word b.

Completeness provides a padded realization and hence at least one parse. Two different labelled parses can be padded to a common leading/trailing b-length exceeding both first/last delays. Surplus b's at each boundary are uniquely determined. The raw M-lists then differ in their a-containing words or a-block boundaries, contradicting UD. This argument does not identify words merely because their gap lists coincide.

Conversely two M-factorizations induce parses of the same actual gap list. A unique labelled parse determines every a-containing word and block boundary; the remaining b counts at boundaries and ends are determined by the actual word, so the M-lists coincide. A parse for any a-core can be padded enough at the two free ends to produce an element of M*, proving precisely factor completeness. All zero gaps are allowed: a boundary at gap0 is valid iff beta_u+alpha_v=0. No epsilon transition or prohibited reordering is being suppressed.

### 4.2 Rational invariant-subspace witness is a criterion only

Parser LF38–61 caps each gap above B, where B dominates every internal equality value and every boundary threshold. Infinity can never be an internal equality and always passes a boundary inequality, so it preserves parses in both directions. States(w,j) keep the full raw word label; a path consumes one gap per transition. For k=1 the state is both initial and final, correctly counting the empty list.

For B_c=diag(A_c,1), lambda=(I,−1) and nu=(F;1), the stated rational identities nu=Vz, B_cV=VT_c and lambda V=0 put every B_word nu in a lambda-annihilated invariant space. Thus every acceptance count is exactly1. Conversely the rational span of the actual vectors B_word nu is invariant, has dimension at most the state count plus1, and is annihilated by lambda if all counts equal1; a finite rational basis gives the displayed certificate. This is a finite all-order criterion once M is supplied, NOT a supplied Shor witness or a bounded-length testing claim.

## 5. Crossing condition and exhaustive four-a table

I reconstructed all seven proper compositions of4 using parts1,2,3. With A=ba, W delays(r,t), P=a³b delays(0,1), U_s gaps(s,0), V_s gaps(0,s), the boundary tests are exactly:

- A,A,A,A: all three gaps≥1;
- W,A,A: first gap0, second≥t+1, third≥1;
- A,W,A: middle gap0, first≥r, last≥t+1;
- A,A,W: last gap0, first≥1, middle≥r;
- W,W: first/last gaps0, middle≥r+t;
- P,A / U_s,A / V_s,A: each triple's exact internal gaps and final boundary≥its beta+1;
- A,P / A,U_s / A,V_s: each triple's exact internal gaps and first boundary≥its alpha.

These exhaust all proper parses. On gaps(a,0,c), the U_a,A and A,V_c parses coexist exactly when beta_a<c AND gamma_c≤a, within1≤a<r,1≤c≤t. Hence(C4) is necessary for every completion, and an added four-a word cannot repair an existing lower-layer ambiguity.

The complete table is correct at all endpoints:

| Gap zero pattern | Missing proper parse / forced four-a core |
|---|---|
| (a,b,c),all positive | Never; four A's parse it |
| (0,b,c) | Exactly b≤t and c≤delta_b; otherwise W,A,A or V_b,A |
| (a,0,c) | Exactly when none of the three displayed A,W,A / U_a,A / A,V_c conditions holds |
| (a,b,0) | Exactly b<r and a<alpha_b |
| (0,0,c) | Only c=1 with gamma_1≥1; P,A covers c≥2 and A,V_1 covers c=1 iff gamma_1=0 |
| (0,b,0) | Exactly b<r+t except b<r with alpha_b=0 |
| (a,0,0),including a=0 | Never; A,P is allowed even at boundary0 |

In particular V_b,A cannot parse(0,b,0) because its last threshold is delta_b+1>0. The r+t endpoint belongs to W,W, the r endpoint of(a,b,0) belongs to A,A,W, and the t+1 endpoint of(0,b,c) belongs to W,A,A; none is incorrectly forced. The finite rectangle bound for(a,0,c) follows by eliminating the northeast A,W,A region and the two remaining U/V tails. The statement assumes actual lower-layer uniqueness, not that(C4) alone solves every future parsing constraint.

When a proper parse is absent, GP forces a SINGLE four-a word of that core; when present, another such codeword would create a second parse. This justifies both directions of the exact table, not just necessary examples. C contains no four-a word, so the homogeneous-tail length budget alpha_g+beta_g=n−4−sum(g) is correctly applied only to these new words.

## 6. Endpoint corollary reconstruction

Endpoint LF40–92 is noncircular and valid for the sufficient homogeneous-tail ansatz:

1. First r=1 is excluded using the unrestricted gamma_t≥1 at t=n−3≥2. Thus r≥2 and every V_c has total outer delay n−3−c≥r−1≥1.
2. If gamma_c=0, set the positive last gap to delta_c. The core(0,c,delta_c) has neither possible proper parse and already has length4+c+delta_c=n+1. It cannot be in C or the length-n tail. Thus gamma_c≥1 also for c=1.
3. At c=t, gamma_t≤r−1. Crossing with a=r−1 forces beta_(r−1)≥t, while its total outer-delay budget equals t. Hence alpha_(r−1)=0,beta_(r−1)=t. For r=2 this contradicts alpha_1≥1, so r≥3.
4. If an earlier alpha_a vanished, beta_a=r+t−1−a≥t+1. The core(a,0,beta_a) defeats all three proper-parse conditions and has length n+1, impossible. Therefore every earlier alpha_a is positive.

The earlier raw-layer exhaustion then makes U_(r−1) the unique EXTRA three-a word starting with a. The fixed a³b is properly excluded from that count. No statement transfers r≥3 or homogeneous endpoint shapes to arbitrary mixed-length completions.

## 7. Dependency and significance calibration

The raw certificate protocol's actual-word binding, nonempty residual closure and exact binary Kraft equality are sufficient by the written Sardinas–Patterson cancellation argument plus the finite-mass contradiction for an avoided factor. Its necessity argument retains all reachable nonempty proper-suffix residuals, a finite universe. No residue-membership converse or unread Szabó/Rédei result is used by the reviewed layers/parser.

The Bernoulli-tail dependency was read completely. Its literal polynomial, positive homogenized coefficients and binomial capacities construct finite raw SETS; its displayed W_n=(ba)^2 b^(n−4) is also factorizable as ba,ba followed by n−4 copies of b. The source expressly chooses an ambiguous control, not a completion. The layer/endpoint proofs consume only its C∪T_n length interface and raw-selector boundary; no unproved UD assertion or n-cbc converse enters. The coarse246002 construction threshold is not a necessary bound on an arbitrary finite completion.

The exact missing positive input is still a finite actual M (or a valid homogeneous-tail selector) with the raw residual closure/Kraft certificate, equivalently the all-gap GP/Q certificate. A negative answer still requires an all-order obstruction covering every finite mixed-length realization. These reviewed structural constraints and optional finite certificate language do not provide either input.

## Return

No repair is requested at the stated scopes. This review can unblock the author's SINGLE consolidation of these same completion-shape results, but it does not accept that consolidation before its own frozen bytes exist. It does not confer novelty, human/kernel review or parent acceptance. I will message MathShor directly with this exact output pin and copy Main, then return to the already accepted AME review pause unless its parent gate becomes actionable.
