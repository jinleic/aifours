# Theorem ASSEMBLY-LS: the word-level D_(2p) consequence of LS-ALL on o_F <= p-1 (written assembly), v1

Owner OlsonAssemblyLS. Written after /bin/date 2026-10-19T10:02:51-0700. Status: CANDIDATE_UNVERIFIED written assembly of
parent-accepted interfaces. Scope frozen BEFORE this derivation: ASSEMBLY-LS-scope-v1.md, sha256
53be77405c8b1369dfbde986a090350829a00cf2a83c3749fb7e87ff09c172a1 (frozen 09:53:20). CONDITIONAL exactly as inherited from
G-LS: for p >= 11 the theorem rests on the statement-level external Lev 2022 Theorem 2 (arXiv:2110.01081v3) through the G-LS
cells with e = p - kappa >= 3; p = 7 uses no Lev input. No computation, model call, novelty, priority, Lean or human-review
claim. No pending (unaccepted) candidate is a premise.

## 0. Statements

Conventions (Sec. 1): an avoider has no 2p letters, in increasing original index order, whose ordered product is the
identity. o_F counts the ODD blocks of the maximal cyclic constant reflection-block decomposition (every maximal cyclic
reflection run is cut at each change of value). INV*: all rotation letters lie in one set {rho_c, rho_-c} with c != 0, and
every maximal cyclic reflection run is constant.

**Theorem ASSEMBLY-LS.** Let p >= 7 be prime.
(A) Every avoider of length 4p-2 over D_(2p) with o_F <= p-1 satisfies INV*.
(B) Every word of length 4p-1 over D_(2p) with o_F <= p-1 has an identity 2p-subword in increasing original index order.

**Proposition ROT-LS (terminal form).** Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p). If SOME admissible
normal form of w has terminal 1 <= k <= p-1, then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0.
There is no hypothesis on o_F(w).

**Remark P5 (citation union, not an LS consequence).** At p = 5, (A) and (B) with o_F <= 4 = p-1 are verbatim items 1-2 of
the accepted p5-lift verdict (row P5); its o_F = 4 piece rests on the computer-assisted finite input C5. ROT-FB is accepted
only for p >= 7, so the LS route of Sec. 3 is NOT claimed at p = 5. "(A) and (B) for every prime p >= 5" therefore holds only
as the UNION of Theorem ASSEMBLY-LS (p >= 7, written) with that verdict (p = 5, computer-assisted), trust classes kept apart.

Trust summary. Written assembly relative to the parent-accepted interfaces of Sec. 2 at their original scopes and mandatory
overlays, with the classical imports they carry (index-one theorem of Savchev-Chen/Yuan, EGZ, Davenport constants including
D(C_p + C_2p) = 3p-1). G-LS cells with e >= 3 also rest on Lev 2022 Theorem 2 (statement read by the parent, proof not
replayed). The accepting verdicts record no computation as a premise of any p >= 7 interface used here (Sec. 6, item 9);
this is a reading of their recorded trust boundaries, not a new audit of every transitive proof body.

## 1. Conventions and the admissible normal form

1.1 Group law (v,e)(v',e') = (v+ev', ee'), rho_x = (x,+1), sigma_y = (y,-1); identity selections contain an even number of
reflections [row GRX]. F, R: numbers of reflection and rotation letters. kappa(w) := p - 1 - (F - o_F)/2.

1.2 Rotation sequence. Y(x) := (1,x) in C_2 x C_p = C_(2p); these are exactly the odd elements of C_(2p). A sub-multiset of the
values Y(x) is zero-sum iff it has even size and value sum = 0 (mod p). For an integer kappa >= 0:
(ZP_kappa) no zero-sum of length in [2kappa+2, 2p]; (S1_kappa) every zero-sum has length <= 2kappa. Sequences are occurrence
sequences throughout [rows LS, GRX].

1.3 Admissible normal form [row NF]. Let w be an avoider of length 4p-2. Then F >= 1 (F = 0 would give 4p-2 >= 3p-1
rotations and EGZ twice an identity 2p-subword). Cut every maximal cyclic reflection run into its maximal constant
sub-blocks (empty rotation runs between them); o := o_F(w) counts the odd ones. Apply PM* across every even block and read two
equal-valued blocks separated by an empty run as one block, repeating; each step lowers the odd-block count by 0 or 2 and the
block count by at least 1, so the process terminates. Any terminal word w^ of this (in general non-unique) process is an
ADMISSIBLE normal form; by ZX overlay 2 every criterion below is existential ("some admissible normal form") and every residual
statement must quantify over ALL admissible normal forms. w^ is an avoider (PM* preserves avoidance from original to reduced),
has length 4p-2, the same F and the same rotation multiset as w, and is EITHER a cyclic constant-block representation with
1 <= k <= o odd blocks, k = o (mod 2), every empty run separating blocks of different values, OR one even block. The even-block
ending is impossible for an avoider (Proposition K1 forces F = 2p-1, odd; lowodd overlay M4). Hence every avoider of length
4p-2 has at least one admissible normal form, and every admissible normal form has terminal 1 <= k <= o_F(w).

1.4 For w^ with k >= 2: all k blocks are odd, so F = k (mod 2), H^ := (F-k)/2 = sum (l_i - 1)/2 and kappa^ := p - 1 - H^ are
integers, R = 4p - 2 - F = 2p + 2kappa^ - k, and kappa^ = kappa(w) - (o_F(w) - k)/2 [rows NF, GRX].

## 2. Interface table

Abbreviations. R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/ ;
R18 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/ ;
ROT = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/ ;
REF = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/ ;
EV = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/ ;
SR2 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/ .
Line ranges are inclusive; every sha256 is of the WHOLE file and was re-computed at this writing and equals the pin in the
accepting verdict where one is given.

| Row | Interface as used here | Source (path:lines, sha256) | Accepting verdict (path:lines, sha256, item) | Original domain | How each hypothesis is met |
|---|---|---|---|---|---|
| NF | Normal form: existence; same length, F, rotation multiset; avoidance; 1<=k<=o_F, k=o_F mod 2; even ending impossible; k=1 -> K1 | ROT/proof-ROT-few-E-v4.md:28-43, ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16/olson-fewodd-parent-verdict-v1-addendum-1.md:12 (ROT-FEW-E v4 in the accepted chain), 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a; R16/olson-zx-s1c-parent-verdict-v1.md:51-53 (overlays 1-3), 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af; R16/olson-rotation-lowodd-parent-verdict-v2.md:8,29,32 (PM*, M1, M4), 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 | Every avoider of length 4p-2, p>=5 prime; any cyclic constant-block representation, empty runs allowed | w (and each deletion in Sec. 5) is an avoider of length 4p-2, p>=7 |
| GRX | Exact criterion; all-plus pattern gives (ZP_kappa^) and kappa^>=0 for k>=2 | ROT/notes-GRX-v1.md:7-20, afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; ROT/proof-SHgen-v3.md:28-33,37, fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e | R16/olson-rotation-lowodd-parent-verdict-v2.md:7 (item 1), 0853f4ac...ba29; R16/olson-zx-s1c-parent-verdict-v1.md:53 (overlay 3, kappa^>=0); R16/olson-k01-parent-verdict-v1.md:53 (m4), e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4 | Every word over D_(2p), p odd prime, every cyclic constant-block representation, empty runs allowed | Applied to w^ with all k blocks odd: Phi=0, delta=k, C_max=2H^, T=0 (Sec. 3, Step 2) |
| DAV | kappa^<=k-1 (R+H^<=3p-2) | ROT/proof-ROT-o3-v4.md:50-57, 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf; ROT/proof-ROT-few-E-v4.md:42-43 | Davenport-alpha with erratum m4: R16/olson-runs-parent-verdict-v1.md:57, 82adbdddd87dff5af0ef8e0e1ceb82b2a20257213966ae45789811a91a859237; DAV as accepted import for k>=2: R16/olson-zx-s1c-parent-verdict-v1.md:53,55; R16/olson-rotkp-parent-verdict-v1.md:59, dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3 | Word of length N<=4p-1, F>=2, any constant-block representation (frame at a run gap outside I) | N=4p-2; F>=k>=2; w^'s boundary gaps exist. The o3-v4 inline text is quoted as the written instance only; per R16/olson-p5-few-lift-parent-verdict-v1.md:34 the o3o4 verdict does not pin v4, so authority is the RUNS m4 plus the ZX/ROT-KP import lists |
| K1 | One block: F=R=2p-1, rotations c^(2p-1), c!=0 | ROT/proof-ROT-lowodd-v1.md:43-61, 8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785 | R16/olson-rotation-lowodd-parent-verdict-v2.md:9 (item 3), 29 (M1), 32 (M4); R16/olson-zx-s1c-parent-verdict-v1.md:53; R16/olson-k01-parent-verdict-v1.md:51 (m2) | p>=5 prime; avoider of length 4p-2 with one constant block, any representation | w^ with k=1 is such a word; rotation multiset of w^ = that of w |
| LS | Corollary LS-ALL: (ZP_kappa) => (S1_kappa) for odd Y with |Y|>=p+2kappa+1; blocks S1-sharp (kappa<=floor(2p/3), no length hypothesis) and G-LS | Definition EV/LS-scope-v1.md:9-12, 80ae8041118d68f4c1417a67a2891ceaceeba181a375b29dfd73820957cfddfa; S1-sharp EV/proof-S1-sharp-v1.md:9-15, 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c (+ erratum 1 bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507, no statement change); G-LS SR2/proof-general-LS-Lev-v1.md:10-28, bc4f4c7035353bf904a202bd41811684a76cb5e9401905a2860e20222fec06dc (+ m3 overlay at its lines 184,187) | R18/olson-general-LS-parent-verdict-v1.md:5,9-10 (items 1-2), 811e5807541f4adb27bf308456358de87cbbd444382103a3f98cda595c10f25b; R18/olson-s1sharp-parent-verdict-v1.md:9 (item 1), bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41 | Prime p>=5, INTEGER 0<=kappa<=p-2, Y odd in C_(2p), |Y|>=p+2kappa+1; G-LS block p>=7, floor(2p/3)+1<=kappa<=p-2, Lev-conditional for e=p-kappa>=3 | Y = rotation sequence of w^, kappa=kappa^ integral in [0,p-2] (Step 2), |Y|=2p+2kappa^-k>=p+2kappa^+1 iff k<=p-1, (ZP_kappa^) from GRX |
| K01 | ROT-K01: some admissible normal form with 2<=k<=p-1, kappa^ in {0,1} => nonzero pair | ROT/proof-ROT-K01-v1.md:61-74, b3ecdb4e09d2eae964322b96e0cddb3c48c91bcea258bebbd4324d16c59eb378 | R16/olson-k01-parent-verdict-v1.md:18 (item 3), 53-54, 57 (m4, m5, m8), e11144f6...0df4 | p>=5 prime; avoider of length 4p-2 | Used for kappa^=0 with 2<=k<=p-1 (Step 4); K01 itself supplies (S1) at kappa^ in {0,1} via S1+ |
| FB | Theorem ROT-FB(a): p>=7, some admissible normal form with kappa^>=1, 2<=k<=p-1 and (S1) at kappa^ => nonzero pair | EV/proof-FB-v1.md:11-17 (S'), 26-30 (statement), 84-107 (proof), 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b; mandatory EV/proof-FB-v1-erratum-1.md:9-27, 44-46 (R1, R2, O4), 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 | R18/olson-FB-parent-verdict-v1.md:5,11-12, 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a; (S') objects via R18/olson-balfull-rotzb-parent-verdict-v1.md:31 (overlay 5), 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 | p>=7 prime; avoider of length 4p-2; NO 3k<=2p+1, NO F or o_F(w) condition; (S1) at kappa^ is a hypothesis when kappa^>floor(2p/3) | kappa^>=1, 2<=k<=p-1 (Step 5); (S1_kappa^) from row LS |
| ZX | Terminal ROT-ZX (3k<=2p+1 and (S1)) | ROT/proof-ROT-ZX-v1.md, ad2460b251b54e93611a7f632349671ce0727cb2a1a812da6ca48d84d1b6815b | R16/olson-zx-s1c-parent-verdict-v1.md:20 (item 3) | 3k<=2p+1 | NOT USED. Row FB covers every 2<=k<=p-1 (Sec. 6, item 4) |
| REFL | Corollary REFL-few-odd: rotations in one {rho_x,rho_-x}, x!=0, avoider, o_F<=p => every maximal cyclic reflection run constant | REF/proof-REFL-fewodd-r4.md:13-25, 35-37, 1e447754e8c7238c2a1918254f674cfb9a4889015a845517e3170087f932861d | R16/olson-refl-fewodd-parent-verdict-v1.md:6, 16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca | p>=5 prime; avoider of length 4p-2; no INV*, RGR, kappa, k condition | Rotation pair from ROT-LS; o_F(w)<=p-1<=p (Sec. 4) |
| LED | Ordered deletion ledger: Case 1 (R<=2) needs o_F<=2p-3; Case 2 (odd block of length>=3) -> (o-1,F-1); Case 3 (R>=3, two rotation deletions) -> (o or o-2,F); reconstruction of the pair and of constant runs | ROT/proof-OLSON-few-v3.md:26-47, ae151f9b38af60ba3a16b954f470b53976317fede4efddc8181fb98ce18cd66a | R16/olson-fewodd-parent-verdict-v1.md:7,15, 375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8; R16/olson-zx-s1c-parent-verdict-v1.md:58 (overlay 8); R16/olson-k01-parent-verdict-v1.md:38,59 (m10); R16/olson-p5-few-lift-parent-verdict-v1.md:37 (overlay 4), c2d06e1478f9aae7354505c81dae3fc7a782c4591a41c3bc288d380d85136d7b | Any bound B<=2p-3 such that every length-(4p-2) avoider with o_F<=B is RGR; no even-block deletion | B=p-1<=2p-3; the class hypothesis is (A) (Sec. 5) |
| RGR | RGR-LONG(p): every word of length 4p-1 with rotations in one {rho_x,rho_-x}, x!=0, and constant maximal cyclic reflection runs has an identity 2p-subword | R16/olson-runs-assembly-proof-v4.md:39-40, 72, 204-205, 06579ba5d23f194cf4cf61241fbbc6eebdaa6fb991d004f1642f43277bb3b104 | R16/olson-runs-parent-verdict-v1.md:3,7, 82adbddd...9237 | p>=5 prime; any such word of length 4p-1 | w is RGR after ledger Case 2 or 3 (Sec. 5) |
| P5 | p=5, o_F<=4: INV* and OLSON-FEW | ROT/proof-FEW-p5-lift-v3.md, aa2fb35092e8eb7621772428925898f5f000584cd9ff069004afc8e353bcb9cb | R16/olson-p5-few-lift-parent-verdict-v1.md:5,10-11 (items 1-2), c2d06e14...6d7b | p>=5 prime, o_F<=4; o_F=4 at p=5 via computer-assisted C5 | Remark P5 only |

Residual-only rows (Sec. 7; no step of Secs. 3-5 uses them): ROT-KP R16/olson-rotkp-parent-verdict-v1.md:17 (dfb2fd0b...);
ROT-KP+ R18/olson-KPS-SLZ-parent-verdict-v1.md:10 (23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612),
EV/proof-KPS-v4.md:38-40 (68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170) with
EV/proof-KPS-v4-erratum-1-v2.md (3ef936f19d2dc9eabadc8684ea842e19a92df2534fb582b11bb302b8375aa80b) M-1; ROT-FB(b) row FB;
ZS v2 overlay V6 R16/olson-zs-v2-parent-verdict-v1.md:29 (2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734);
RED/K0* R16/olson-reflection-K0star-RED-parent-verdict-v1.md (879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a);
small-k R16/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8);
REFL-HI v5 R18/olson-REFLHI-v5-parent-verdict-v1.md (13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547);
RP-LIFT R18/olson-RP-LIFT-parent-verdict-v1.md (e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652);
RP-2NE R18/olson-RP2NE-parent-verdict-v1.md (320d817a4b24d2c39f04806ce84ab1977fd68f5869b8c7be0da5184d166d2eab).

## 3. Proof of Proposition ROT-LS

Let p >= 7 be prime, w an avoider of length 4p-2, w^ an admissible normal form of w with terminal 1 <= k <= p-1, and Y the
rotation sequence of w^ (equal, as a multiset, to that of w; row NF).

Step 1 (k = 1). w^ is an avoider of length 4p-2 consisting of one constant block (any representation; lowodd M1), so by
Proposition K1 its rotation letters are rho_c^(2p-1) with c != 0. They are the rotation letters of w.

Step 2 (k >= 2; parameters). Use 1.4. GRX on w^ with the all-plus pattern z: Phi = 0, every f_i = 0, every l_i odd, so
delta = k, C_max = F - k = 2H^, and T(z) = sum theta_i = 0. Hence w^ has an identity 2p-subword as soon as, for some even C with
0 <= C <= 2H^ and 0 <= 2p - C <= R, some 2p - C rotation values sum to 0 (mod p).
(i) If H^ >= p, C = 2p and the empty rotation selection qualify; so avoidance gives H^ <= p-1, i.e. kappa^ >= 0.
(ii) For even m = 2p - C in [2kappa^+2, 2p] (automatically C in [0, 2H^]) and m <= R, no m rotation values sum to 0 (mod p);
lengths m > R are vacuous. By 1.2 this is exactly (ZP_kappa^) for Y.
DAV on w^ (N = 4p-2 <= 4p-1, F >= k >= 2, frame at a run gap): R + H^ <= 3p-2. Since R + H^ = (2p+2kappa^-k) + (p-1-kappa^) =
3p-1+kappa^-k, this is kappa^ <= k-1. With k <= p-1: kappa^ is an integer and 0 <= kappa^ <= k-1 <= p-2.

Step 3 ((S1) at kappa^ for k <= p-1). |Y| = R = 2p+2kappa^-k >= p+2kappa^+1 because k <= p-1. Y consists of odd elements of
C_(2p) (1.2), satisfies (ZP_kappa^) (Step 2), p >= 7 >= 5 is prime and kappa^ is an integer in [0, p-2]. These are exactly the
hypotheses of LS(p, kappa^) in its original definition (EV/LS-scope-v1.md:10-12), which Corollary LS-ALL proves on that whole
domain. Hence Y satisfies (S1_kappa^). Block actually used: kappa^ <= floor(2p/3): S1-sharp (no length hypothesis);
floor(2p/3)+1 <= kappa^ <= p-2: G-LS (p >= 7), Lev-free when kappa^ = p-2 (e = 2) and conditional on Lev 2022 Theorem 2 when
kappa^ <= p-3 (e >= 3). The latter range is empty at p = 7 (floor(14/3)+1 = 5 = p-2) and nonempty for every p >= 11.

Step 4 (kappa^ = 0). w^ is an admissible normal form with 2 <= k <= p-1 and kappa^ in {0, 1}: ROT-K01 (p >= 5) gives one
nonzero pair for the rotations of w. (Step 3 is not needed here; K01 obtains (S1) at kappa^ in {0,1} from S1+.)

Step 5 (kappa^ >= 1). p >= 7 is prime, w is an avoider of length 4p-2, and its admissible normal form w^ has kappa^ >= 1,
2 <= k <= p-1, and (S1) at kappa^ for its rotation sequence (Step 3): this is hypothesis (a) of Theorem ROT-FB. Hence every
rotation letter of w lies in one {rho_c, rho_-c}, c != 0. ROT-FB(a) carries no 3k <= 2p+1, F or o_F(w) condition; its internal
objects live in (S') (1 <= k <= p-1, integer 1 <= kappa < p, |Y| = 2p+2kappa-k, (S1) at kappa), which kappa = kappa^ meets
since 1 <= kappa^ <= k-1 < p; its SHgen-E caller (o_F(u°) <= k <= p-1) is discharged inside the accepted ROT-FB.

By Step 2, kappa^ >= 0, so Steps 1, 4 and 5 are exhaustive. []

Remark. The only input not available before LS-ALL is (S1_kappa^) for floor(2p/3)+1 <= kappa^ <= p-2 with k <= p-1: exactly
the open boundary recorded at R18/olson-FB-parent-verdict-v1.md:39 ("Within terminal k<=p-1, the remaining rotation cases have
kappa^>floor(2p/3) and (S1) failing") and anticipated at EV/LS-scope-v1.md:16-17. For kappa^ >= 1 the scope's sentence there
("ROT-FB (a) ... for every terminal 2 <= k <= p-1") is used as written; kappa^ = 0 is routed to ROT-K01 because ROT-FB requires
kappa^ >= 1.

## 4. Proof of Theorem ASSEMBLY-LS (A)

Let p >= 7 and w an avoider of length 4p-2 with o_F(w) <= p-1. By 1.3, w has an admissible normal form, and every admissible
normal form of w has terminal 1 <= k <= o_F(w) <= p-1. Proposition ROT-LS puts all rotation letters of w in one
{rho_c, rho_-c}, c != 0. Corollary REFL-few-odd applies to w itself: p >= 5 prime, length 4p-2, (i) that rotation pair,
(ii) w avoids, (iii) o_F(w) <= p-1 <= p. So every maximal cyclic reflection run of w is constant, and w satisfies INV*. []

Quantifier. Every admissible normal form of such a w meets the hypothesis of ROT-LS, so the existential criteria apply
whichever normal form the process produces; no avoider with o_F <= p-1 can be residual in the sense of ZX overlay 2.
No condition on F is needed: the FB uniform consequence (R18/olson-FB-parent-verdict-v1.md:15) imposed
F - o_F >= 2(p-1-floor(2p/3)) only to force kappa^ <= kappa(w) <= floor(2p/3), where S1-sharp supplies (S1)
(EV/proof-FB-v1.md:113-121); Step 3 supplies (S1) for every kappa^ <= p-2 when k <= p-1.

## 5. Proof of Theorem ASSEMBLY-LS (B)

Let p >= 7 and w a word of length 4p-1 over D_(2p) with o_F(w) <= p-1. Suppose w has no identity 2p-subword in increasing
index order; then every subword avoids. Apply the accepted ordered deletion ledger with B := p-1. Its class hypothesis,
"every avoider of length 4p-2 with o_F <= B is RGR", is (A) (INV* is RGR: rotations in one nonzero pair, constant maximal
cyclic reflection runs). Its only global requirement B <= 2p-3 holds (p >= 2).
- Case 1 (R <= 2). F >= 4p-3 and F - o_F(w) >= 4p-3-(p-1) = 3p-2 >= 2p. If R = 0 and all reflections are equal, any 2p of them
  multiply to 1. Otherwise read w in the cyclic frame starting at a rotation (R >= 1) or at a change of reflection value
  (R = 0); no block wraps, the blocks contain (F - o_F(w))/2 >= p disjoint adjacent equal pairs, p of them form an identity
  2p-subword of the framed word, and conjugating back gives one of w (RUNS verdict m6). Contradiction.
- Case 2 (some odd block has length >= 3). Deleting one of its letters gives an avoider w' of length 4p-2 with
  o_F(w') = o_F(w) - 1 <= p-2 (that block becomes even and stays nonempty; nothing else changes). By (A), w' is RGR; w has the
  same rotation letters and its reflection runs differ from those of w' by one more copy of a letter inside a constant block,
  so w is RGR.
- Case 3 (R >= 3). Delete two different rotation letters x1, x2: each w_i := w - x_i is an avoider of length 4p-2 with
  o_F(w_i) <= o_F(w) <= p-1 (if the run of x_i becomes empty, the two neighbouring blocks keep their identity or fuse, and
  odd+odd -> even, odd+even -> odd, even+even -> even never raises the odd count). By (A) both are RGR, with pairs
  {±c1}, {±c2}. A third rotation x3 lies in both; its value t != 0 forces {±c1} = {±t} = {±c2} (p5-lift overlay 4); every
  rotation of w lies in w_1 or w_2, hence in that pair. Deleting a rotation only creates new adjacencies between reflections,
  so two adjacent reflections of different values in w would stay adjacent in w_1; hence every maximal cyclic reflection run
  of w is constant, and w is RGR.
In Cases 2 and 3, w lies in RGR_(4p-1)(p), and RGR-LONG(p) (p >= 5) gives w an identity 2p-subword in increasing original
index order: contradiction. []

Preservation check. In (B), (A) is applied only to w' (o_F = o_F(w) - 1) and to w_1, w_2 (o_F <= o_F(w)); none exceeds p-1.
The normal form of Sec. 1.3 is applied only inside (A), to each of these length-(4p-2) avoiders separately. No deletion from
an even block occurs. Because the class has no F condition, the ledger's F - o_F bookkeeping (needed by earlier uniform
corollaries) plays no role.

## 6. Answers to the frozen route items (each at the interface's original scope)

1. Normal form and kappa^ (rows NF, GRX, DAV): existence, 1 <= k <= o_F, k = o_F (mod 2), F and rotation multiset preserved;
   for k >= 2, kappa^ is an integer with 0 <= kappa^ <= k-1 (GRX all-plus pattern; DAV with N = 4p-2, F >= 2). Hence
   0 <= kappa^ <= k-1 <= o_F - 1 <= p-2 under o_F <= p-1.
2. Length: R = 2p+2kappa^-k >= p+2kappa^+1 iff k <= p-1; then LS-ALL gives (S1_kappa^) (row LS), every hypothesis of its
   original definition being met (Step 3).
3. kappa^ = 0 is NOT isolated: ROT-K01 covers it for every 2 <= k <= p-1 and every prime p >= 5. k = 1 is K1.
4. ZX terminal criterion: not used. The S1-sharp verdict's dihedral chain (R18/olson-s1sharp-parent-verdict-v1.md:31) invoked
   it because it needed 3k <= 2p+1; ROT-FB(a) (R18/olson-FB-parent-verdict-v1.md:11-12) covers all 2 <= k <= p-1 without it,
   as EV/proof-FB-v1.md:129-130 and erratum O4 record. The only remaining restriction on k anywhere in Secs. 3-5 is
   k <= p-1, imposed simultaneously by ROT-FB's setting (L >= 2p-k >= p+1), by ROT-K01's range and by the LS threshold; it is
   automatic from k <= o_F <= p-1. Other global conditions: restricted REFL needs o_F <= p; ledger Case 1 needs o_F <= 2p-3.
5. Restricted REFL is applied to the original length-(4p-2) word, with o_F <= p-1 <= p.
6. The ledger and normalization preserve o_F <= p-1 from length 4p-1 to every length-(4p-2) word used (Sec. 5, preservation
   check); RGR-LONG(p) then finishes (B).
7. Quantifier: every admissible normal form is covered, so the existential criteria apply; residual statements (Sec. 7) are
   universal over all admissible normal forms.
8. p = 5: Remark P5 (citation union only).
9. Transitive trust. Classical: index-one theorem (via SC0, S1-sharp, ROT-FB), EGZ, Davenport/D(C_n) = n, D(C_p + C_2p) = 3p-1
   (Davenport-alpha), Cauchy-Davenport (inside G-LS). External statement-level: Lev 2022 Theorem 2 (G-LS, e >= 3; p >= 11 only).
   Computer-assisted: none recorded as a premise of the p >= 7 chain (R16/olson-runs-parent-verdict-v1.md:3 "No finite census is
   a proof premise"; R18/olson-FB-parent-verdict-v1.md:5 "No computation is a premise"; R16/olson-k01-parent-verdict-v1.md:63;
   R18/olson-general-LS-parent-verdict-v1.md:50; R16/olson-rotkp-parent-verdict-v1.md:61); the p = 5 union cell rests on the
   computer-assisted finite C5 (R16/olson-p5-few-lift-parent-verdict-v1.md:5). This assembly re-reads verdict trust statements;
   it does not re-audit every transitive proof body.

## 7. Residual description (NOT a claim; quantified over ALL admissible normal forms)

7.1 o_F(w) = p, length 4p-2 avoiders, p >= 7.
- Restricted REFL applies (o_F = p <= p), so INV* for w is equivalent to rotation rigidity; only the rotation half remains.
- Every admissible normal form has odd terminal k <= p. If SOME has k <= p-2, Proposition ROT-LS applies verbatim (it has no
  o_F hypothesis); with restricted REFL such w satisfy INV* (an immediate consequence of the candidate ROT-LS, hence also
  CANDIDATE_UNVERIFIED; not separately frozen as a theorem).
- If an admissible normal form has k = p, then kappa^ = kappa(w) (o_F = k) and |Y| = R = p+2kappa^, ONE below the LS threshold
  p+2kappa^+1, so LS-ALL does not apply. Accepted coverage there: ROT-KP (kappa^ in {0,1}); ROT-KP+ (p >= 7, kappa^ >= 1, (S1)
  at kappa^; relative to the classical import S(p) at its recorded secondary-statement trust level, KPS erratum M-1); the
  ROT-FB(b) hypothesis (every zero-sum of Y of length <= 2kappa^-2) implies (S1) and is contained in ROT-KP+'s. (S1) at kappa^ is
  automatic for kappa^ <= floor(2p/3) (S1-sharp).
- Residual cell: avoiders with o_F = p ALL of whose admissible normal forms have terminal k = p (no fusion step lowers the odd
  count), with floor(2p/3)+1 <= kappa(w) <= p-1 (kappa(w) <= o_F - 1 by DAV), whose rotation sequence (length p+2kappa(w),
  (ZP_kappa(w)) by GRX) has a zero-sum of length >= 2p+2. Exact blocking hypothesis: (S1) at kappa^ for |Y| = p+2kappa^ (the
  ROT-KP+ / ROT-FB(b) input at k = p).
- Smallest missing sequence lemma (one-short LS): for prime p >= 7 and floor(2p/3)+1 <= kappa <= p-2, every odd Y in C_(2p) with
  |Y| = p+2kappa and (ZP_kappa) satisfies (S1_kappa). Not attempted here. Remarks only: a counterexample needs a long zero-sum T
  with 2p+2 <= |T| <= p+2kappa (possible in size since kappa >= (p+2)/2 throughout this range); at kappa = p-1 (outside the
  original LS domain) the sequence version FAILS: Y = g^(2p-1)(3g)^(p-1) (ZS v2 overlay V6) has length 3p-2 = p+2(p-1),
  satisfies (ZP_(p-1)) (a zero-sum of length 2p would need a + b = 2p and a + 3b = 0 mod 2p, so b = 0 mod p, b = 0 and
  a = 2p > 2p-1), and contains the zero-sum g^(p+3)(3g)^(p-1) of length 2p+2 (coefficient sum 4p). So the cell
  (k, kappa^) = (p, p-1), i.e. F = p, all blocks singletons, R = 3p-2, needs word-level input beyond (ZP) (for example
  non-constant GRX sign patterns, as the ZS v2 and half-range verdicts note). No group word realizing that Y is known or claimed.
- Word level (length 4p-1, o_F = p), residual-map observation only (not frozen as a candidate statement): ledger Case 1 applies
  (o_F = p <= 2p-3); a Case 2 deletion has o_F = p-1, inside (A); Case 3 deletions have o_F in {p-2, p}. So for these words the
  ledger can stall only when no odd block has length >= 3 and a Case 3 deletion with o_F = p lies in the residual cell above.

7.2 o_F(w) >= p+1.
- Rotation half: ROT-LS covers every avoider having SOME admissible normal form with k <= p-1 (any o_F); ROT-KP/ROT-KP+ cover
  k = p with kappa^ <= 1 or (S1) at kappa^. Residual rotation cells: every admissible normal form has terminal k >= p+1, or k = p
  with (S1) failing at some kappa^ >= floor(2p/3)+1. For k >= p+1: |Y| = 2p+2kappa^-k <= p+2kappa^-1 (below every LS
  threshold); ROT-FB's setting fails (L >= 2p-k no longer gives L >= p+1, so SC0/index-one is unavailable); and the SHgen-E
  caller would need REFL for o_F up to k >= p+1, outside restricted REFL. Missing inputs: a sequence lemma for zero-sum-free
  complements of length <= p, and REFL beyond o_F <= p.
- Reflection half (the binding obstruction even when rotations are rigid): restricted REFL needs o_F <= p. By RED, REFL(p) is
  equivalent to "no avoider in RES_<(p) with kappa >= 2"; the small-k verdict excludes RES_<(p) with k <= p; RES_<(p) with
  k >= p+1 (B = 0 and 1 <= B < kappa) is open. Accepted partial exclusions in the all-odd one-pair setting (REFL-HI v5 R = p and
  R = p+delta bands, RP-LIFT, RP-2NE) keep their own scopes and are not assembled here. REFL(p), REFL-HI(p), RES-HI(p) are OPEN.
- Word level: ledger Case 1 still needs o_F <= 2p-3; Case 2/3 deletions have o_F >= p-1 and may fall in the residual above.

7.3 Unrestricted INV*(p), ordered Olson for D_(2p) and the all-groups ordered Olson target remain OPEN.

## 8. Coverage comparison (internal, not literature) and limits

Avoiders satisfy kappa(w) <= o_F - 1 (rows NF, DAV, K1: kappa(w) = kappa^ + (o_F - k)/2 <= (o_F + k)/2 - 1). Within
o_F <= p-1 the accepted uniform classes already covered 3o_F <= 2p+1 (S1-sharp, any F) and kappa(w) <= floor(2p/3) (FB);
FB's own residual statement is EV/proof-FB-v1.md:139-140 ({kappa(w) >= floor(2p/3)+1 and o_F >= floor(2p/3)+2}). Theorem
ASSEMBLY-LS removes that residual: the new uniform cells are o_F <= p-1 with kappa(w) >= floor(2p/3)+1. Examples (with
F = o_F + 2(p-1-kappa(w))): p = 7, (o_F, F) = (6, 8); p = 11, (o_F, F) in {(9,13), (10,14), (10,12)}. These are sufficient
classes only; no existence of avoiders with these parameters is asserted. The theorem is a composition of accepted
statements; no new sequence or word lemma is proved here. Written mathematics only: no Lean, no human review, no novelty or
priority assessment, no claim at o_F >= p.
