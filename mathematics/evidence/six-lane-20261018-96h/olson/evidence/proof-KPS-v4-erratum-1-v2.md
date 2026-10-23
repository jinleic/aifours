# Erratum 1 to evidence/proof-KPS-v4.md (sha256 68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170), version 2

(v2 after /bin/date 2026-10-19T03:46:44-0700 supersedes erratum-1 v1 5bf0b4e7...37cc, never sent: one sentence on KETA in M-5 made precise.)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:46:30-0700.
Reviews answered: run review/olson-kps-slz-codex-v1.prompt.stdout.txt (sha256 6ce69cb0eb1a2e23b9edff9d85868e17278adfbb1dd4943e9388380cef102408; 0 FATAL / 0 MAJOR / 3 MINOR, all
on SLZ-EXT) and run review/olson-kps-slz-claude-v1.prompt.note.md (sha256 c98dc2f491e739d374329d2489218a81837512e03b979714cdb57287f1bda3bd; 0 FATAL / 0 MAJOR / 8 required MINOR
M-1..M-8 + 2 editorial E-1, E-2 + optional O-1..O-5).  One coordinated round: this file and its two siblings
(import note, KPS v4, SLZ-EXT v2).  The frozen texts are not edited; no proof strategy or theorem statement changes.

## M-1 (proviso carried)
Every 'relative to Import S(p)' in the header, Sec. 0 and Sec. 6 reads 'relative to Import S(p) at the trust level of
evidence/import-Sp-XiaYuan-v1.md as amended by its erratum 1 (df1c5ac2dba4f088b6aa402a1e1c1e9037063230a37776d8f50b704997c87269)'; the n-range is covered for every p >= 5
at that secondary-statement trust level (the Theorem and Corollary use p >= 7).
## M-5 (definitions of eta and a_max; the eta >= 2 bound)
Sec. 4 (K) cites: proof-SHgen-v3.md (fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e) Sec. 0, L39-42: relative to c, rho_c and rho_-c are LIGHT; every other rotation
is HEAVY with signed weight b (odd, |b| <= p - 2, b_0 := p); eta := number of heavies (BOTH signs); a_j := |b| of heavy j;
a_max := max_j a_j; E := sum_j (a_j - 1).  Derivation used for eta >= 2: the heavy with |b| = a_max contributes a_max - 1 to E
and each of the other eta - 1 heavies contributes |b| - 1 >= 2, so E >= a_max - 1 + 2(eta - 1), i.e. eta + a_max <= E + 3 - eta
<= E + 1.  (In case (N) the heavies are exactly the terms a_i g with a_i >= 3 and -s_i g with s_i >= 3, so 'eta >= 1 iff E >= 1'
and 's_1 is the only heavy' are statements about this eta.)  KETA's k-free inequality eta + a_max <= E + 2 (ROT-ZR verdict
6d8bb6c94f6263834c39130c6d39a2ab54e557740eb45f904732664e879dde73, L45) is not needed in KPS: for eta = 1, eta + a_max = E + 2 holds by definition (E = a_max - 1);
for eta >= 2 the derivation above gives the stronger eta + a_max <= E + 1.
## M-6 (caller scopes in Sec. 1)
Sec. 1's import line 'SHgen/SHgen-E with the ROT-ZR caller discharge and restricted REFL for o_F(u°) <= k <= p' is replaced by:
'SHgen/SHgen-E with (a) for 2 <= k <= p - 1 (inside the Corollary, through ROT-FB (a)) the ROT-ZR verdict's discharge
(o_F(u°) <= k <= p - 1; verdict 6d8bb6c94f6263834c39130c6d39a2ab54e557740eb45f904732664e879dde73, L45); (b) for k = p the ROT-KP verdict's caller scope (verdict dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3: m5, m6;
SHgen has no hidden k <= p - 1 restriction, SHgen-E base words keep k = p and o_F(u°) <= p inside restricted REFL-few-odd,
(K) equality allowed) with ZX overlay 4 / generalized ZS v2 overlay V3 (verdicts 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af, 2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734), extended to
kappa^ >= 2 by the FB verdict's closure of R1 (run review/olson-FB-parent-verdict-v1.md, 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a)', as Sec. 4 already states.
## Optional (adopted as editorial)
- O-2: in FB-p (R), the n = 1 case has a_(h) = p; the unified bound for 1 <= n <= p - 1 is W >= p + n(p - n).
- O-3: in FB-p (B), y < m uses m >= slack + 1 + h (L = p), not FB's m >= slack + 3; the argument is a re-derivation (FB's
  scope needs L >= p + 1).
- O-4: in ARC0, R = a + b = p + 2kappa^, so k = p is implicit; m <= R holds automatically (m counts letters of w^).
