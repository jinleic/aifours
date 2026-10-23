# Theorem ASSEMBLY-P: the word-level D_(2p) assembly on o_F <= p, conditional on ONE-SHORT-LS and ROT-SING (written assembly), v2

Owner OlsonAssemblyP. v2 written after /bin/date 2026-10-19T11:41:40-0700. It supersedes v1 (proof-ASSEMBLY-P-v1.md, sha256
2f6e8468c060448b05b51bffc8a435cc8e04f224f1484652cacd905b33293b4d, written after 11:37:00, preserved, never sent) by the
author's own audit: (i) row LED quotes the accepted single-bound domain and the accepted multi-condition precedents and states
that (B0) re-runs the written case analysis with explicit membership checks; (ii) Sec. 8 attributes EGZ/Davenport to the
normal form, DAV and RGR-LONG (not to the ledger); (iii) Sec. 8 adds the S1-sharp verdict's non-premise probe record;
(iv) Sec. 9.1 states why o_F = F = p forces k = p for every admissible normal form. No statement, case split or mathematical
step changes. Status: CANDIDATE_UNVERIFIED written assembly of
parent-accepted interfaces and of two PENDING candidates that enter ONLY as explicitly labelled conditional premises.
Scopes frozen BEFORE this derivation: ASSEMBLY-P-scope-v1.md, sha256
5a4d9064b05e7dfbc9ac478ba3df95e89de00b573be379c3ce968ec848c2f64f (11:30:13), and ASSEMBLY-P-scope-v1-addendum-1.md, sha256
d75211261e4108eff5ec9ada3f702d8408fbf235b8b0ff6570a2106f5727a2d9 (11:35:16; Corollary ASSEMBLY-P0).
Pending premises: [ONE-SHORT-LS] = continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md (sha256
c544aad2ab0cadc4c76870dc97382b6a749bbdda85f96596bdb128efe9b19ffc) and [ROT-SING] =
continuations/terminal-p-singletons/proof-ROT-SING-v2.md (sha256 ae5feaa1cd99aad9d2c0c35d1521ec27c3a1e5516225b102b4cb4bb793a4b1f1)
read with the parent commentary erratum review/olson-ROT-SING-parent-erratum-v1.md (sha256
aad62a162f1fb25cc786ea0b96f1ceaeacf8cad8532bd16a36c15058d612d25b). Neither is accepted at this writing; neither is used as an
accepted result. ROT-SING+ is not used. Lev 2022 Theorem 2 (arXiv:2110.01081v3, statement level, proof not replayed) enters
exactly where Sec. 8 records it. No computation, model call, novelty, priority, Lean or human-review claim.

## 0. Statements

Conventions (Sec. 1) are those of the accepted ASSEMBLY-LS proof: an avoider has no 2p letters, in increasing original index
order, whose ordered product is the identity; o_F counts the ODD blocks of the maximal cyclic constant reflection-block
decomposition; kappa(w) := p - 1 - (F - o_F)/2; INV*: all rotation letters lie in one set {rho_c, rho_-c} with c != 0, and
every maximal cyclic reflection run is constant.

**Theorem ASSEMBLY-P (conditional on [ONE-SHORT-LS] and [ROT-SING]).** Let p >= 7 be prime.
(A) Every avoider of length 4p-2 over D_(2p) with o_F <= p satisfies INV*.
(B) Every word of length 4p-1 over D_(2p) with o_F <= p has an identity 2p-subword in increasing original index order.

**Proposition ROT-P (terminal k = p).** Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p). If SOME admissible
normal form of w has terminal k = p, then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0. There is no
hypothesis on o_F(w). Premises by the kappa^ of the invoked normal form: [ROT-SING] only at kappa^ = p-1; [ONE-SHORT-LS] only
at kappa^ in U(p) (Proposition DEP); every other kappa^ uses accepted interfaces only.

**Proposition DEP (dependency refinement).** Let p >= 7 be prime and
  U(p) := {kappa : floor(2p/3)+1 <= kappa <= p-3, p < 10(p-kappa)-13, and not (p = 1 (mod 3) and kappa = (2p+1)/3)}.
Let kappa be an integer with floor(2p/3)+1 <= kappa <= p-2 and kappa not in U(p). Every sequence Y of odd elements of C_(2p)
with |Y| = p+2kappa and (ZP_kappa) satisfies (S1_kappa), by the accepted LS+2 (kappa = p-2), the accepted LS+ linear band
(e := p-kappa >= 3 and p >= 10e-13) or the accepted BASE1+ (p = 1 (mod 3), kappa = (2p+1)/3). U(7) is empty. (Remark, Sec. 4:
U(p) is nonempty for every prime p >= 11.)

**Corollary ASSEMBLY-P0 (no pending premise).** Let p >= 7 be prime. Call a word w over D_(2p) P0-admissible if o_F(w) <= p-1,
or o_F(w) = p and kappa(w) is not in U(p) u {p-1}.
(A0) Every P0-admissible avoider of length 4p-2 satisfies INV*.
(B0) Every P0-admissible word of length 4p-1 has an identity 2p-subword in increasing original index order.
At p = 7 (U(7) empty) the P0-admissible words with o_F <= 7 are exactly those with NOT (o_F = 7 and F = 7); and (A), (B) at
p = 7 use [ROT-SING] only (no [ONE-SHORT-LS]) and no Lev input.

**Remark P5 (not claimed).** p = 5 is NOT claimed. ROT-LS, ROT-KP+ (through ROT-FB), [ONE-SHORT-LS] and [ROT-SING] are stated
for p >= 7 only. The accepted p5-lift verdict (row P5; computer-assisted finite input C5) covers o_F <= 4 at p = 5; the cell
o_F = 5 at p = 5 is not covered by any interface used here (ROT-KP covers k = p = 5 only for kappa^ <= 1). No p = 5 union is
stated.

Trust summary. Written assembly relative to the parent-accepted interfaces of Sec. 2 at their original scopes and mandatory
overlays, with the classical imports they carry; S(p) enters through ROT-KP+ at its secondary-statement trust level; Lev
enters only through accepted ROT-LS (k <= p-1 cells) and through [ONE-SHORT-LS] (kappa^ in U(p)); the two pending premises
are conditions, not imports. The accepting verdicts and both pending texts record no computation as a premise (Sec. 8).

## 1. Conventions and the normal form at k = p

1.1-1.4 are verbatim the accepted ASSEMBLY-LS conventions (proof-ASSEMBLY-LS-v2.md lines 41-62; rows NF, GRX): group law
(v,e)(v',e') = (v+ev', ee'), rho_x = (x,+1), sigma_y = (y,-1); identity selections contain an even number of reflections; F, R
count reflection and rotation letters. Y(x) := (1,x) in C_2 x C_p = C_(2p) are exactly the odd elements; a sub-multiset of the
Y(x) is zero-sum iff it has even size and value sum = 0 (mod p). (ZP_kappa): no zero-sum of length in [2kappa+2, 2p];
(S1_kappa): every zero-sum has length <= 2kappa. Sequences are occurrence sequences. Under (ZP_kappa) a zero-sum of length
> 2kappa has even length >= 2kappa+2 outside [2kappa+2, 2p], i.e. length >= 2p+2 (LONG); so for Y with (ZP_kappa),
(S1_kappa) fails iff Y contains a long zero-sum.
Normal form [row NF]: every avoider w of length 4p-2 has an admissible normal form w^ (a terminal word of the PM*/fusion
process); w^ is an avoider of length 4p-2 with the same F and the same rotation multiset as w, a cyclic constant-block
representation R_1 S_1 ... R_k S_k with 1 <= k <= o_F(w), k = o_F(w) (mod 2), all k blocks odd, every empty run separating
blocks of different values (the even-block ending is impossible). Criteria are existential and residual statements quantify
over ALL admissible normal forms (ZX overlay 2). For k >= 2: H^ := (F-k)/2 and kappa^ := p-1-H^ are integers,
R = 2p+2kappa^-k and kappa^ = kappa(w) - (o_F(w)-k)/2.
1.5 (k = p). F = p (mod 2), H^ = (F-p)/2, R = 4p-2-F = p+2kappa^, so the rotation sequence Y of w^ has |Y| = p+2kappa^, exactly
ONE below the LS threshold p+2kappa^+1 (LS-ALL is not used anywhere at k = p). o_F(w) >= k = p; if o_F(w) = p then
kappa^ = kappa(w).

## 2. Interface table

Abbreviations. R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/ ;
R18 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/ ;
ROT = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/ ;
REF = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/ ;
EV = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/ ;
SR2 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/ ;
CON = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/ .
Line ranges are inclusive; every sha256 is of the WHOLE file, re-computed at this writing (11:24-11:37), and equals the pin
of the accepting verdict where one is given. Rows NF, GRX, DAV, REFL, LED, RGR, P5 are the accepted ASSEMBLY-LS rows
(CON/assembly-ls/proof-ASSEMBLY-LS-v2.md lines 77-79, 85-88), restated with the new "how met" entries.

| Row | Interface as used here | Source (path:lines, sha256) | Accepting verdict (path:lines, sha256, item) | Original domain | How each hypothesis is met |
|---|---|---|---|---|---|
| NF | Normal form: existence; same length, F, rotation multiset; avoidance; 1<=k<=o_F, k=o_F mod 2; all terminal blocks odd; even ending impossible; empty runs separate different values | ROT/proof-ROT-few-E-v4.md:28-43, ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16/olson-fewodd-parent-verdict-v1-addendum-1.md:12, 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a; R16/olson-zx-s1c-parent-verdict-v1.md:51-53 (overlays 1-3), 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af; R16/olson-rotation-lowodd-parent-verdict-v2.md:8,29,32 (PM*, M1, M4), 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 | Every avoider of length 4p-2, p>=5 prime; any cyclic constant-block representation, empty runs allowed | w and every length-(4p-2) deletion in Sec. 6 are avoiders of length 4p-2, p>=7 |
| GRX | Exact criterion; all-plus pattern gives kappa^>=0 and (ZP_kappa^) for k>=2 | ROT/notes-GRX-v1.md:7-20, afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; ROT/proof-SHgen-v3.md:28-33,37, fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e | R16/olson-rotation-lowodd-parent-verdict-v2.md:7 (item 1), 0853f4ac...ba29; R16/olson-zx-s1c-parent-verdict-v1.md:53 (overlay 3); R16/olson-k01-parent-verdict-v1.md:53 (m4), e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4 | Every word over D_(2p), p odd prime, every cyclic constant-block representation, every sign pattern | w^ with k=p odd blocks, all-plus pattern: Phi=0, delta=p, C_max=2H^, T=0 (Sec. 3, Step 1) |
| DAV | kappa^<=k-1 (R+H^<=3p-2) | ROT/proof-ROT-o3-v4.md:50-57, 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf; ROT/proof-ROT-few-E-v4.md:42-43 | Davenport-alpha with erratum m4: R16/olson-runs-parent-verdict-v1.md:57, 82adbdddd87dff5af0ef8e0e1ceb82b2a20257213966ae45789811a91a859237; as import for k>=2: R16/olson-zx-s1c-parent-verdict-v1.md:53,55; R16/olson-rotkp-parent-verdict-v1.md:59, dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3 | Word of length N<=4p-1, F>=2, any constant-block representation (frame at a run gap) | N=4p-2, F>=k=p>=2; authority as in the ASSEMBLY-LS row (RUNS m4 plus import lists; o3-v4 quoted as written instance only) |
| ROT-LS | Proposition ROT-LS: SOME admissible normal form with 1<=k<=p-1 => one nonzero pair; no o_F hypothesis | CON/assembly-ls/proof-ASSEMBLY-LS-v2.md:24-26 (statement), 101-140 (proof), ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3; mandatory R18/olson-ASSEMBLY-LS-parent-erratum-v1.md, 572308b87c62237f77dab554afb29152b568b11c027dc8825c5923895b93f8f7; R18/olson-ASSEMBLY-LS-parent-erratum-v2.md:5-15 (N1), 38458a8521f692e07b695a1c4553bb41bfaf6be9f93481b5d16f9c3e92d7c588 | R18/olson-ASSEMBLY-LS-parent-verdict-v1.md:9,11,15 (item 1), 249e07658762e7e3efe346063851b243369f14dadf6fbaedf121944a18db6a22 | p>=7 prime; avoider of length 4p-2; any o_F; Lev (statement level) for p>=11 when the invoked normal form has floor(2p/3)+1<=kappa^<=p-3 | Invoked only for a normal form with k<=p-1 (Secs. 5-6) |
| ALS | Theorem ASSEMBLY-LS (A)/(B): o_F<=p-1 | same proof, lines 20-22, 142-182 | same verdict, lines 12-13, 15 (items 2-3) | p>=7 prime; o_F<=p-1; Lev as ROT-LS | Corollary ASSEMBLY-P0, case o_F<=p-1 (Secs. 5-6) |
| KP | Theorem ROT-KP: SOME admissible normal form with k=p and kappa^ in {0,1} => one nonzero pair | ROT/proof-ROT-KP-v1.md:113-115 (statement), 40-110 (Parts A, B), 472e43cf6c2652ecbc68704dea99fc84263ea241ef3a3147feb51902c43a800e | R16/olson-rotkp-parent-verdict-v1.md:15,17 (item 1), 47-55 (mandatory overlay m1-m9), 59 (imports), dfb2fd0b...bcf3 | p>=5 prime; avoider of length 4p-2; any o_F (SHgen-E base words at k=p inside restricted REFL, m5) | kappa^ in {0,1} at k=p (Sec. 3, Step 2) |
| S1S | Lemma S1-sharp: (ZP_kappa) => (S1_kappa), NO length hypothesis | EV/proof-S1-sharp-v1.md:9-15, 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c (+ erratum 1, bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507, no statement change) | R18/olson-s1sharp-parent-verdict-v1.md:3,9 (item 1), bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41 | Prime p>=5, integer 0<=kappa<=floor(2p/3), any sequence of odd elements of Z_(2p) | Y of w^, kappa=kappa^ in [2,floor(2p/3)], (ZP) from GRX (Sec. 3, Step 3) |
| KP+ | Theorem ROT-KP+: p>=7, admissible normal form with k=p, kappa^>=1 and (S1) at kappa^ => one nonzero pair | EV/proof-KPS-v4.md:38-40 (statement), 105-130 (proof), 68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170; mandatory EV/proof-KPS-v4-erratum-1-v2.md:11-14 (M-1), 24-30 (M-6), 3ef936f19d2dc9eabadc8684ea842e19a92df2534fb582b11bb302b8375aa80b | R18/olson-KPS-SLZ-parent-verdict-v1.md:8 (item 1, S(p)), 10 (item 3), 14-15, 24, 23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612 | p>=7 prime; avoider of length 4p-2; k=p; kappa^>=1 with no upper bound; (S1_kappa^) for the rotation sequence of that normal form; any o_F; relative to S(p) at secondary-statement trust level | kappa^ in [2,p-2], (S1_kappa^) from S1S, [ONE-SHORT-LS] or row DEP (Sec. 3, Steps 3-4) |
| OSL | [PENDING] ONE-SHORT-LS: |Y|=p+2kappa EXACTLY and (ZP_kappa) => (S1_kappa) | CON/one-short-ls/proof-ONE-SHORT-LS-v2.md:16-17 (statement), 249-252 (trust: Lev in case (I), every e>=2), c544aad2ab0cadc4c76870dc97382b6a749bbdda85f96596bdb128efe9b19ffc | NONE (pending). Codex R18/olson-ONE-SHORT-LS-codex-v1.prompt.stdout.txt, dd2ec5570d1be85fbff8e6fe710b3a4d61e14caccbf3ca400ea0a2be1d5b7220: ACCEPT, 0 findings; second family not returned at this writing | p>=7 prime; integer floor(2p/3)+1<=kappa<=p-2; odd Y in C_(2p); |Y|=p+2kappa exactly; Lev-conditional | CONDITIONAL premise: Y of w^, |Y|=R=p+2kappa^ (1.5), (ZP_kappa^) from GRX, kappa^ in its range (Sec. 3, Step 4); needed only at kappa^ in U(p) |
| SING | [PENDING] ROT-SING: SOME admissible normal form with k=p and kappa^=p-1 => rotation multiset rho_c^(2p-1) rho_-c^(p-1), c!=0 | CON/terminal-p-singletons/proof-ROT-SING-v2.md:14-16 (statement), 41-44 (shape), ae5feaa1cd99aad9d2c0c35d1521ec27c3a1e5516225b102b4cb4bb793a4b1f1; overlay R18/olson-ROT-SING-parent-erratum-v1.md (commentary only), aad62a162f1fb25cc786ea0b96f1ceaeacf8cad8532bd16a36c15058d612d25b | NONE (pending). Codex R18/olson-ROT-SING-codex-v1.prompt.stdout.txt, e6fc106e0d2a7fbfcff1e5b0c73e5e3352b7dc1d1e22ee111d30026272a3383e (1 commentary MINOR, disposed by the parent erratum); second family not returned at this writing | p>=7 prime; avoider of length 4p-2; any o_F | CONDITIONAL premise: kappa^=p-1 at k=p (Sec. 3, Step 5) |
| LS+2 | Theorem LS+2: kappa=p-2, odd (ZP_kappa) sequence with a long zero-sum has length <=3p-5 | SR2/proof-LSplus-e2-v1.md:21-23, 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 | R18/olson-STAB-delta-parent-verdict-v1.md:9 (definitions), 21 (item 4), ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 | p>=7 prime, kappa=p-2, any length | DEP (i): |Y|=3p-4>3p-5 (Sec. 4) |
| LS+lin | LS+ linear band: floor(2p/3)+1<=kappa<=p-2, e=p-kappa, (e=2, p>=7) or (e>=3, p>=10e-13): odd (ZP_kappa) Y with a long zero-sum has |Y|<=3kappa+1 | SR2/proof-LSplus-lin-v1.md:18-20, 1372a691022cfef9a75c0fceec73054563e2b3d411e12c739ef27970587667cf, read through governing SR2/erratum-1-lsplus-chain-consolidated-v3.md, f1573d6c8b1ac00afe3ce438ff5ebca64cce1e4c2682aaf3ef01e18831a608c0 | R18/olson-LSplus-chain-parent-verdict-v1.md:9-11 (statement), 24 (undecided cells), 29, 4005007f4e073386236016b62949cba925cb5cde12ba13c24ce27b2a2c351b55 | Prime p, the stated (kappa,e) band, any length | DEP (ii): |Y|=3kappa^+e>=3kappa^+3 (Sec. 4) |
| BASE1+ | Corollary BASE1+: p=1 mod 3, p>=7, kappa=(2p+1)/3: odd (ZP_kappa) sequence with a long zero-sum has length <=2p+2 | SR2/proof-STAB-base-p1mod3-v1.md:12,15, 8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985 | R18/olson-STAB-delta-parent-verdict-v1.md:17-20 (item 3), ac8ead13...c5 | p=1 (mod 3), p>=7 prime, kappa=(2p+1)/3, any length | DEP (iii): |Y|=(7p+2)/3>2p+2 (Sec. 4) |
| REFL | Corollary REFL-few-odd: rotations in one {rho_x,rho_-x}, x!=0, avoider, o_F<=p => every maximal cyclic reflection run constant | REF/proof-REFL-fewodd-r4.md:13-25, 35-37, 1e447754e8c7238c2a1918254f674cfb9a4889015a845517e3170087f932861d | R16/olson-refl-fewodd-parent-verdict-v1.md:6, 14-16 (boundaries; caller obligations), 16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca | p>=5 prime; avoider of length 4p-2; no INV*, RGR, kappa, k condition | Pair from ROT-LS or ROT-P; o_F(w)<=p; applied directly to w, not through SHgen-E (Sec. 5) |
| LED | Ordered deletion ledger: Case 1 (R<=2) needs o_F<=2p-3; Case 2 (odd block of length>=3) -> (o-1,F-1); Case 3 (R>=3, two rotation deletions) -> (o or o-2,F); reconstruction of the pair and of constant runs | ROT/proof-OLSON-few-v3.md:26-47, ae151f9b38af60ba3a16b954f470b53976317fede4efddc8181fb98ce18cd66a | R16/olson-fewodd-parent-verdict-v1.md:7,15, 375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8; R16/olson-zx-s1c-parent-verdict-v1.md:58 (overlay 8); R16/olson-k01-parent-verdict-v1.md:38,59 (m10); R16/olson-p5-few-lift-parent-verdict-v1.md:37 (overlay 4), c2d06e1478f9aae7354505c81dae3fc7a782c4591a41c3bc288d380d85136d7b; multi-condition uses: R16/olson-rotkp-parent-verdict-v1.md:43, R18/olson-FB-parent-verdict-v1.md:29, 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a | Accepted form: any bound B<=2p-3 such that every length-(4p-2) avoider with o_F<=B is RGR; accepted multi-condition uses add an F-o_F inequality that Cases 2-3 preserve (K01 line 38, ROT-KP line 43, FB line 29); no even-block deletion | (B): B=p<=2p-3, class o_F<=p is (A), verbatim. (B0): the class P0 is not of either accepted form; Sec. 6 re-runs the written case analysis of (B) and checks P0-membership of every deletion explicitly |
| RGR | RGR-LONG(p): every word of length 4p-1 with rotations in one {rho_x,rho_-x}, x!=0, and constant maximal cyclic reflection runs has an identity 2p-subword | R16/olson-runs-assembly-proof-v4.md:39-40, 72, 204-205, 06579ba5d23f194cf4cf61241fbbc6eebdaa6fb991d004f1642f43277bb3b104 | R16/olson-runs-parent-verdict-v1.md:3,7, 82adbddd...9237 | p>=5 prime; any such word of length 4p-1 | w is RGR after ledger Case 2 or 3 (Sec. 6) |
| P5 | p=5, o_F<=4: INV* and OLSON-FEW | ROT/proof-FEW-p5-lift-v3.md, aa2fb35092e8eb7621772428925898f5f000584cd9ff069004afc8e353bcb9cb | R16/olson-p5-few-lift-parent-verdict-v1.md:5,10-11 (items 1-2), c2d06e14...6d7b | p=5, o_F<=4; computer-assisted C5 | Remark P5 only (not a premise) |

Not used: LS-ALL / G-LS (k = p lies one below their length threshold), ROT-K01 (stated for 2 <= k <= p-1), ROT-FB(a) directly
(it enters only inside ROT-LS and ROT-KP+), ROT-SING+, the ZX terminal criterion. Residual-only references (Sec. 9): RED/K0*
R16/olson-reflection-K0star-RED-parent-verdict-v1.md (879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a);
small-k R16/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8);
ROT-SING+ CON/terminal-pplus1-singletons/proof-ROT-SINGPLUS-v1.md (68865d55311128167ead7e3e966e92545520eb5224e4b44458ab469af67a8d9d, pending).

## 3. Proof of Proposition ROT-P

Let p >= 7 be prime, w an avoider of length 4p-2, w^ an admissible normal form of w with terminal k = p, and Y the rotation
sequence of w^ (equal, as a multiset, to that of w; row NF).

Step 1 (parameters). By 1.5, kappa^ is an integer and |Y| = R = p+2kappa^. GRX on w^ with the all-plus pattern z: every
f_i = 0, so Phi = 0; every l_i is odd, so delta = #{i : l_i odd} = p and C_max = F - p = 2H^; T(z) = sum of all theta_i = 0
(cyclic telescoping). Hence w^ has an identity 2p-subword as soon as, for some even C with 0 <= C <= 2H^ and
0 <= 2p-C <= R, some 2p-C rotation values sum to 0 (mod p).
(i) If H^ >= p, C = 2p with the empty rotation selection qualifies; avoidance gives H^ <= p-1, i.e. kappa^ >= 0.
(ii) For even m = 2p-C in [2kappa^+2, 2p] (then C in [0, 2H^]) with m <= R, no m rotation values sum to 0 (mod p); lengths
m > R are vacuous. By 1.1 this is (ZP_kappa^) for Y.
DAV on w^ (N = 4p-2, F >= k = p >= 2, frame at a run gap): R + H^ <= 3p-2. As R + H^ = (p+2kappa^) + (p-1-kappa^) =
2p-1+kappa^, this is kappa^ <= p-1. So kappa^ is an integer in [0, p-1].
The four ranges below are disjoint and cover [0, p-1]: floor(2p/3) >= 4 >= 2 and floor(2p/3)+1 <= p-2 for p >= 7.

Step 2 (kappa^ in {0, 1}). w^ is an admissible normal form of the avoider w with terminal k = p and kappa^ in {0, 1}; ROT-KP
(p >= 5) gives one nonzero pair for the rotation letters of w. (For kappa^ = 1 ROT-KP+ would also apply; its own proof routes
kappa^ = 1 to ROT-KP, EV/proof-KPS-v4.md line 108; routing to ROT-KP avoids S(p).)

Step 3 (2 <= kappa^ <= floor(2p/3)). Y is a sequence of odd elements of C_(2p) with (ZP_kappa^) (Step 1), p >= 5 is prime and
kappa^ is an integer in [0, floor(2p/3)]: S1-sharp (no length hypothesis) gives (S1_kappa^). Then p >= 7, w avoids, and w^ has
k = p, kappa^ >= 1 and (S1) at kappa^: ROT-KP+ gives one nonzero pair.

Step 4 (floor(2p/3)+1 <= kappa^ <= p-2). Y consists of odd elements of C_(2p), |Y| = p+2kappa^ EXACTLY (1.5), (ZP_kappa^)
holds (Step 1), p >= 7 is prime and kappa^ is an integer in [floor(2p/3)+1, p-2]: these are exactly the hypotheses of
[ONE-SHORT-LS], which (CONDITIONALLY) gives (S1_kappa^). By Proposition DEP, if kappa^ is not in U(p) the same (S1_kappa^)
follows from the accepted LS+2, LS+ linear band or BASE1+ instead, so [ONE-SHORT-LS] is needed only for kappa^ in U(p).
Then ROT-KP+ (k = p, kappa^ >= 1, (S1) at kappa^, p >= 7) gives one nonzero pair.

Step 5 (kappa^ = p-1). w is an avoider of length 4p-2 and w^ is an admissible normal form with k = p and kappa^ = p-1 (H^ = 0,
F = p, all blocks singletons, R = 3p-2): [ROT-SING] (CONDITIONALLY) gives the rotation multiset rho_c^(2p-1) rho_-c^(p-1),
c != 0; in particular one nonzero pair. (Here (S1_(p-1)) can fail at sequence level, e.g. Y = g^(2p-1)(3g)^(p-1) (ZS v2 V6);
ROT-KP+ is not invoked.)

By Step 1 the cases are exhaustive. No step uses o_F(w). []

Interface checks. ROT-KP+ carries no o_F, F or kappa^ upper-bound hypothesis (KPS-SLZ verdict line 10; source lines 38-40);
its SHgen/SHgen-E calls at k = p are discharged inside it through the ROT-KP caller scope (erratum M-6, lines 24-30; ROT-KP
overlay m5: base words keep k = p and o_F(u°) <= p inside restricted REFL). [ONE-SHORT-LS] is sequence level and is applied at
its exact length p+2kappa; it is never applied at kappa = p-1, where its statement is false (scope remark, its line 19).
[ROT-SING] has no o_F hypothesis and uses no (S1), Lev or REFL.

## 4. Proof of Proposition DEP (and the size of U(p))

Let floor(2p/3)+1 <= kappa <= p-2, kappa not in U(p), and Y odd with |Y| = p+2kappa and (ZP_kappa). Suppose (S1_kappa) fails;
by 1.1, Y contains a long zero-sum. Since kappa is not in U(p), one of the following holds.
(i) kappa = p-2. LS+2 (p >= 7, kappa = p-2): |Y| <= 3p-5. But |Y| = p+2(p-2) = 3p-4. Contradiction.
(ii) e := p-kappa >= 3 and p >= 10e-13 (and floor(2p/3)+1 <= kappa <= p-2 as required by the band): the LS+ linear band gives
     |Y| <= 3kappa+1. But |Y| = p+2kappa = 3kappa+e >= 3kappa+3. Contradiction.
(iii) p = 1 (mod 3) and kappa = (2p+1)/3 (then p >= 7 and kappa = floor(2p/3)+1 <= p-2): BASE1+ gives |Y| <= 2p+2. But
     |Y| = p+(4p+2)/3 = (7p+2)/3 > 2p+2 since p > 4. Contradiction.
That (i)-(iii) are the only alternatives: kappa not in U(p) means kappa = p-2, or p >= 10(p-kappa)-13, or (p = 1 (mod 3) and
kappa = (2p+1)/3) (the first condition of U(p) holds for kappa <= p-3 by assumption). Hence (S1_kappa). []
U(7) = {}: floor(14/3)+1 = 5 > 4 = p-3. At p = 7 the only Step 4 value is kappa^ = 5 = p-2 (cell (i); also cell (iii), 7 = 1
(mod 3), (2*7+1)/3 = 5).
Remark (U(p) nonempty for p >= 11). Let E := floor((p-1)/3) >= 3, so kappa_E := p-E = floor(2p/3)+1 <= p-3. If p = 2 (mod 3),
E = (p-2)/3 and 10E-13 = (10p-59)/3 > p (p >= 9), so kappa_E is in U(p). If p = 1 (mod 3) (p >= 13), kappa_E is the BASE1+ cell;
then E-1 = (p-4)/3 >= 3 and 10(E-1)-13 = (10p-79)/3 > p (p >= 12), so kappa_E+1 <= p-3 is in U(p). This agrees with the
undecided-cell list of the LS+ verdict (line 24: (11,8), (13,10), (17,12-13), (19,14-15), (23,16-19), ...).

## 5. Proof of (A) and (A0)

(A). Let p >= 7 and w an avoider of length 4p-2 with o_F(w) <= p. By 1.1 (row NF), w has an admissible normal form, and every
admissible normal form w^ of w has terminal 1 <= k <= o_F(w) <= p. If k <= p-1, Proposition ROT-LS (accepted, no o_F
hypothesis) puts all rotation letters of w in one {rho_c, rho_-c}, c != 0. If k = p, Proposition ROT-P does (conditionally).
Corollary REFL-few-odd applies to w itself: p >= 5 prime, length 4p-2, (i) that rotation pair, (ii) w avoids,
(iii) o_F(w) <= p. So every maximal cyclic reflection run of w is constant: w satisfies INV*. []
Quantifier. Every admissible normal form of such a w has k <= p and is covered by ROT-LS or ROT-P, so the existential criteria
apply to whichever normal form the process produces. If k = p occurs then o_F(w) = p and kappa^ = kappa(w) (1.5).
REFL caller obligations (R16/olson-refl-fewodd-parent-verdict-v1.md:16) bind only callers that rebase Lemma SHgen-E on REFL;
here REFL is applied directly to the original w with o_F(w) <= p. The SHgen-E calls inside the imported theorems are
discharged in their own verdicts: ROT-FB(a) inside ROT-LS (o_F(u°) <= k <= p-1, ROT-ZR discharge), ROT-KP Part B and ROT-KP+
at k = p (ROT-KP overlay m5; KPS erratum M-6). [ONE-SHORT-LS] and [ROT-SING] use no REFL.

(A0). Let w be a P0-admissible avoider of length 4p-2. If o_F(w) <= p-1, ASSEMBLY-LS (A) (accepted, row ALS) gives INV*. If
o_F(w) = p, take any admissible normal form w^. If k <= p-1, ROT-LS applies. If k = p, then kappa^ = kappa(w) (1.5), which is
not in U(p) u {p-1}; so Step 5 of Sec. 3 is not reached, and in Step 4 Proposition DEP replaces [ONE-SHORT-LS]. Hence the
rotation pair follows from accepted interfaces only, and REFL-few-odd (o_F(w) = p) gives INV*. []

## 6. Proof of (B) and (B0)

(B). Let p >= 7 and w a word of length 4p-1 over D_(2p) with o_F(w) <= p. Suppose w has no identity 2p-subword in increasing
index order; then every subword avoids. Apply the accepted ordered deletion ledger with B := p. Its class hypothesis, "every
avoider of length 4p-2 with o_F <= B is RGR", is (A) (INV* is RGR). Its only global requirement B <= 2p-3 holds (p >= 3).
- Case 1 (R <= 2). F >= 4p-3 and F - o_F(w) >= 4p-3-p = 3p-3 >= 2p. If R = 0 and all reflections are equal, any 2p of them
  multiply to 1. Otherwise read w in the cyclic frame starting at a rotation (R >= 1) or at a change of reflection value
  (R = 0); no block wraps, the blocks contain (F - o_F(w))/2 >= p disjoint adjacent equal pairs, p of them form an identity
  2p-subword of the framed word, and conjugating back gives one of w (RUNS verdict m6). Contradiction.
- Case 2 (some odd block has length >= 3). Deleting one of its letters gives an avoider w' of length 4p-2 with
  o_F(w') = o_F(w) - 1 <= p-1 (that block becomes even and stays nonempty; nothing else changes). By (A), w' is RGR; w has the
  same rotation letters and its reflection runs differ from those of w' by one more copy of a letter inside a constant block,
  so w is RGR.
- Case 3 (R >= 3). Delete two different rotation letters x1, x2: each w_i := w - x_i is an avoider of length 4p-2 with
  o_F(w_i) <= o_F(w) <= p (if the run of x_i becomes empty, the two neighbouring blocks keep their identity or fuse, and
  odd+odd -> even, odd+even -> odd, even+even -> even never raises the odd count). By (A) both are RGR, with pairs {+-c1},
  {+-c2}. A third rotation x3 lies in both; its value t != 0 forces {+-c1} = {+-t} = {+-c2} (p5-lift overlay 4); every rotation
  of w lies in w_1 or w_2, hence in that pair. Deleting a rotation only creates new adjacencies between reflections, so two
  adjacent reflections of different values in w would stay adjacent in w_1; hence every maximal cyclic reflection run of w is
  constant, and w is RGR.
In Cases 2 and 3, w lies in RGR_(4p-1)(p), and RGR-LONG(p) (p >= 5) gives w an identity 2p-subword in increasing original index
order: contradiction. []
Preservation check. (A) is applied only to w' (o_F = o_F(w)-1 <= p-1) and to w_1, w_2 (o_F <= o_F(w) <= p); no F condition is
needed, so the F - o_F bookkeeping of the earlier uniform corollaries plays no role. No deletion from an even block occurs. The
same ledger at B = p is already used, with an additional F - o_F condition, in the accepted OLSON-KP
(R16/olson-rotkp-parent-verdict-v1.md:43) and in the KPS-SLZ uniform corollary (item 3).

(B0). Let w be a P0-admissible word of length 4p-1, assumed to have no identity 2p-subword. Run the same three cases with the
class "P0-admissible avoiders of length 4p-2", all RGR by (A0). Case 1 needs only o_F(w) <= p <= 2p-3. Case 2: o_F(w') =
o_F(w) - 1 <= p-1, so w' is P0-admissible. Case 3: F(w_i) = F(w) and o_F(w_i) is o_F(w) or o_F(w) - 2. If o_F(w_i) <= p-1, w_i is
P0-admissible. Otherwise o_F(w_i) = p, hence o_F(w) = p and o_F(w_i) = o_F(w), so kappa(w_i) = p-1-(F(w)-p)/2 = kappa(w), which
is not in U(p) u {p-1}: w_i is P0-admissible. The reconstruction steps of Cases 2-3 and RGR-LONG(p) are unchanged; the ledger
is used with a class that is not of the pure form o_F <= B, exactly as the accepted multi-condition uses (rows LED: K01 verdict
line 38, ROT-KP verdict line 43, FB verdict line 29), and here every deletion's membership is checked explicitly. []

## 7. Answers to the frozen route items (scope v1 items 1-6, addendum items 1-3)

1. Normal form (rows NF, GRX, DAV): every avoider of length 4p-2 has an admissible normal form; every one has
   1 <= k <= o_F <= p (Sec. 5).
2. k <= p-1: accepted ROT-LS, no o_F hypothesis; Lev cells as recorded in its verdict (Sec. 8).
3. k = p: kappa^ integral, 0 <= kappa^ <= p-1 (GRX, DAV), |Y| = p+2kappa^ (Sec. 3, Step 1).
   - kappa^ = 0 (and 1): the accepted interface is ROT-KP item 1 (R16/olson-rotkp-parent-verdict-v1.md:15,17; p >= 5, k = p,
     kappa^ in {0,1}). ROT-K01 does NOT cover k = p (its range is 2 <= k <= p-1). Nothing is isolated.
   - 2 <= kappa^ <= floor(2p/3): S1-sharp + ROT-KP+.
   - floor(2p/3)+1 <= kappa^ <= p-2: (ZP) at |Y| = p+2kappa^ exactly; [ONE-SHORT-LS], or for kappa^ not in U(p) the accepted
     LS+2 / LS+ linear band / BASE1+ (Proposition DEP); then ROT-KP+.
   - kappa^ = p-1: [ROT-SING].
4. (A): restricted REFL on the original w (o_F <= p); caller obligations as in Sec. 5.
5. (B): ledger with B = p <= 2p-3; Case 1 F - o_F >= 3p-3 >= 2p; Case 2 o_F-1; Case 3 <= o_F; class o_F <= p preserved without
   an F condition; RGR-LONG(p).
6. Quantifier: every admissible normal form of every avoider with o_F <= p is covered (Sec. 5).
Addendum 1-3: Sec. 5 (A0) and Sec. 6 (B0); the precedent for multi-condition ledger classes is identified (row LED); no gap.

## 8. Trust classes and dependency map

Cell table (by the invoked admissible normal form; all cells require p >= 7 prime; REFL, the ledger and RGR-LONG are added at
word level):

| Invoked normal form | Interfaces | Pending premise | Lev 2022 Thm 2 | S(p) |
|---|---|---|---|---|
| k = 1 | ROT-LS (K1) | none | no | no |
| 2 <= k <= p-1, kappa^ = 0 | ROT-LS (K01) | none | no | no |
| 2 <= k <= p-1, 1 <= kappa^ <= floor(2p/3) | ROT-LS (S1-sharp, ROT-FB(a)) | none | no | no |
| 2 <= k <= p-1, floor(2p/3)+1 <= kappa^ <= p-3 | ROT-LS (G-LS e >= 3, ROT-FB(a)) | none | YES (p >= 11 only) | no |
| 2 <= k <= p-1, kappa^ = p-2 (forces k = p-1) | ROT-LS (G-LS e = 2, ROT-FB(a)) | none | no | no |
| k = p, kappa^ in {0,1} | ROT-KP | none | no | no |
| k = p, 2 <= kappa^ <= floor(2p/3) | S1-sharp, ROT-KP+ | none | no | YES |
| k = p, floor(2p/3)+1 <= kappa^ <= p-2, kappa^ not in U(p) | LS+2 / LS+lin / BASE1+, ROT-KP+ | none | no | YES |
| k = p, kappa^ in U(p) (empty for p = 7) | ROT-KP+ | [ONE-SHORT-LS] | YES (through ONE-SHORT-LS) | YES |
| k = p, kappa^ = p-1 | none accepted | [ROT-SING] | no | no |

- Lev 2022 Theorem 2 (statement level, proof not replayed): through accepted ROT-LS exactly as its verdict records (p >= 11,
  invoked k <= p-1 normal form with floor(2p/3)+1 <= kappa^ <= p-3) and through [ONE-SHORT-LS] at k = p, kappa^ in U(p) (its
  Sec. 11: case (I) for every e >= 2). p = 7 is Lev-free.
- S(p): classical corollary imported at the secondary-statement trust level of KPS-SLZ verdict item 1 with erratum M-1
  (Xia-Yuan 2010 via Peng-Sun; primary proof unread); through ROT-KP+ at k = p, kappa^ >= 2.
- Classical: the index-one theorem of Savchev-Chen/Yuan (inside S1-sharp, ROT-FB, SC0/ROT-KP Part B, ROT-KP+, LS+2, LS+ band,
  BASE1+), EGZ and Davenport constants including D(C_p + C_2p) = 3p-1 (normal form, DAV, RGR-LONG), Cauchy-Davenport
  (inside G-LS, LS+2/LS+ band via CT/RS, [ONE-SHORT-LS] via CT/ROW/RS, and directly in [ROT-SING] Step 3).
- Computer-assisted: none as a premise for p >= 7. Recorded boundaries: ASSEMBLY-LS verdict line 5 ("No computation is a
  premise for p >= 7"); R16/olson-rotkp-parent-verdict-v1.md:61; KPS-SLZ verdict line 24 (finite S(p) controls are consistency
  checks only); R18/olson-s1sharp-parent-verdict-v1.md:37 (probes are finite aids, not premises); STAB-delta verdict line 5;
  LS+ chain verdict line 5; [ONE-SHORT-LS] Sec. 11 and [ROT-SING] Sec. 4 (no
  computation, no computer-assisted cited input). The only computer-assisted item in sight is the p = 5 input C5 (row P5),
  which is not used. This is a reading of recorded trust boundaries, not a new audit of every transitive proof body.
- p = 5: not claimed (Remark P5).

## 9. Residual description (NOT a claim; quantified over ALL admissible normal forms)

9.1 o_F <= p. Conditional on the two premises, nothing remains. Without [ONE-SHORT-LS]: avoiders with o_F = p ALL of whose
admissible normal forms have k = p and kappa(w) in U(p) whose rotation sequence has a long zero-sum (empty at p = 7). Without
[ROT-SING]: avoiders with o_F = p = F. (F = o_F means every constant block is a singleton; with no even block PM* never acts,
and two blocks separated by an empty run lie in one maximal reflection run and differ in value, so no fusion occurs: the block
decomposition itself is the only terminal word, with k = p and kappa^ = p-1.) Word level of length 4p-1: by (B0), only words
with o_F = p and kappa(w) in U(p) u {p-1} need a premise.
9.2 o_F >= p+1 (p >= 7).
- Rotation half: ROT-LS (accepted) and ROT-P (conditional) have no o_F hypothesis, so they cover every avoider having SOME
  admissible normal form with k <= p. Residual rotation cells: EVERY admissible normal form has terminal k >= p+1. There
  |Y| = 2p+2kappa^-k <= p+2kappa^-1 (at least two below the LS length threshold); ROT-FB(a), ROT-KP+ and ROT-P are outside
  their stated k-domains. These are obstacles to these routes, not proof that such avoiders exist. ROT-SING+ (pending) states
  the cell k = p+1, kappa^ = p-1.
- Reflection half: restricted REFL needs o_F <= p. By RED, REFL(p) is equivalent to "no avoider in RES_<(p) with kappa >= 2";
  the small-k verdict excludes RES_<(p) with k <= p; RES_<(p) with k >= p+1 is open. REFL(p) is OPEN.
- Word level (length 4p-1). Ledger Case 1 applies for o_F <= 2p-3. For o_F(w) = p+1, a Case 2 deletion has o_F = p, inside (A)
  (so such words with an odd block of length >= 3 have an identity 2p-subword, conditionally on the premises; an immediate
  consequence of (A) via the ledger's Case 2, NOT separately frozen as a theorem). Case 3 deletions have o_F in {p-1, p+1}; the
  ledger stalls only when no odd block has length >= 3 and fewer than two rotation deletions lower o_F.
9.3 Unrestricted INV*(p), ordered Olson for D_(2p) and the all-groups ordered Olson target remain OPEN.

## 10. Coverage comparison (internal, not literature) and limits

Before this assembly, accepted coverage at o_F = p was: INV*-KP / OLSON-KP (F - o_F >= 2p-4, i.e. kappa(w) <= 1); the KPS-SLZ
uniform corollary (kappa(w) <= floor(2p/3) for INV*, F - o_F >= 2(p-1-floor(2p/3)) at length 4p-1); and, existentially, ROT-LS
for avoiders having some admissible normal form with k <= p-1. ASSEMBLY-LS covered o_F <= p-1. New cells at o_F = p (avoiders,
F = p + 2(p-1-kappa(w))): kappa(w) in [floor(2p/3)+1, p-2] \ U(p) with no pending premise (Corollary ASSEMBLY-P0; e.g.
p = 7: (o_F, F) = (7, 9); p = 11: (11, 13); p = 13: (13, 19) and (13, 15)), kappa(w) in U(p) conditional on [ONE-SHORT-LS]
(e.g. p = 11: (11, 15); p = 13: (13, 17)), and kappa(w) = p-1, i.e. F = p, conditional on [ROT-SING]. These are sufficient
classes only; no existence of avoiders with these parameters is asserted. The theorem is a composition of accepted statements
and two pending candidates; the only new arguments are the case routing, Proposition DEP's length comparisons and the P0 class
bookkeeping. Written mathematics only: no Lean, no human review, no novelty or priority assessment, no claim at o_F >= p+1,
no claim at p = 5.
