# Erratum 1 to evidence/proof-FB-v1.md (sha256 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:15:50-0700.  Responds to the two hostile reviews launched by the parent:
run review/olson-fb-codex-v1.prompt.stdout.txt (sha256 1c585d1f8a7dcb105cf8f3ed69714ad7642479f8d9500c36ae2ff1ca3e0477e1; ACCEPT on all four items incl. k = p, 0 required findings)
and run review/olson-fb-claude-v1.prompt.note.md (sha256 0521132c5d97c2a1e6db46df22f07f9db71fb7b12da5183cf497769f691d9997; Lemma FB, Corollary FB-E, Corollary ACCEPT; Theorem
ROT-FB ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR, required MINOR R1, R2, optional O1-O5).  The v1 text is not edited.  No
statement of Lemma FB, Corollary FB-E, Theorem ROT-FB (a)/(b) or the Corollary changes.

## R1 (required): k = p caller citation for Theorem ROT-FB (b)
Sec. 4's SHgen/SHgen-E step for case (b) (k = p) is cited to the accepted ROT-KP verdict (run of 2026-10-16,
review/olson-rotkp-parent-verdict-v1.md, sha256 dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3): its Codex referee checked that Theorem SHgen has no hidden
k <= p - 1 restriction and that the SHgen-E caller uses restricted REFL at o_F = p; its derivation records 'Empty runs route
through SHgen-E, whose base words keep k = p and o_F = p <= p, inside restricted REFL-few-odd', with overlay m5 ('o_F(u°) <=
k = p; k = p and REFL condition (d) are checked at each base word') and m6 (the (K) equality case k = 2p - eta - a_max - 1
reaches SHgen Lemma Ua's KB branch).  Together with ZX overlay 4 (review/olson-zx-s1c-parent-verdict-v1.md, sha256
2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af: expansions preserve k and the block/empty-run representation; cite the generalized ZS v2 overlay V3,
review/olson-zs-v2-parent-verdict-v1.md, sha256 2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734), this is the caller scope for k = p.  The ROT-ZR verdict's
discharge (o_F(u°) <= k <= p - 1) is cited only for case (a).  In case (b) the (K) inequality may hold with equality
(eta + a_max = p - 1 = 2p - 1 - k is allowed, as in ROT-KP).

## R2 (required): inline content instead of 'ROUTE-ALL(T)'
The header sentence 'Within that scope this text proves ROUTE-ALL(T)' and the Sec. 4 Remark are replaced by the content:
'In (S') with 2 <= k <= p - 1, for any longest zero-sum Z and any index-<1 generator g = Y(c) of Y - Z, the SHgen
quantities relative to c satisfy E_c <= 2H = 2p - 2 - 2kappa, and either E_c = 0 or eta_c + a_max,c <= 2p - 1 - k.  In
particular this holds when the longest zero-sum has length exactly 2kappa (then (S1) at kappa is automatic, and
2kappa + k >= 2p is allowed), so no sequence-level obstruction of that kind exists.'  The phrase '(S1) assumed when
kappa > floor(2p/3)' in the Remark is deleted as redundant.

## O1 (optional, adopted): integer form of the y + r step
In Sec. 2 the convexity line is replaced by: with x := r - 1 >= 1, x s_(r) <= S_(r-1) <= delta - 1 and
(x - 1)(s_(r) - 1) >= 0 give x + s_(r) <= x s_(r) + 1 <= delta, so y + r <= s_(r) + x <= delta; equality forces
S_(r-1) = delta - 1, s_(1) = ... = s_(r), and x = 1 or s_(r) = 1.

## O2 (optional, adopted): statement of (b)
Theorem ROT-FB (b) reads: 'k = p and every zero-sum of Y has length <= 2kappa^ - 2' ((S1) at kappa^ is implied).  For
kappa^ <= floor(2p/3) this is equivalent to: Y has no zero-sum of length exactly 2kappa^ (by (ZP) and S1-sharp).

## O3 (optional): ROOM wording
Sec. 2 Remark (ii) stands as written: the earlier ROOM (proof-ROT-ZB-v2.md Sec. 3) proves W <= 2p - 1 - n+ using L >= 2t
(from 2kappa + k <= 2p and t <= kappa) but NOT balance, and BAL-forall needs L >= 2t + 1; Lemma FB obtains balance and the
W-bound with no relation between L and t.  The compressed wording 'ROOM's W-bound uses only longestness' (BAL-full parent
derivation) is read as 'uses longestness and L >= 2t, not balance' (parent IRC clarification).

## O4 (optional, adopted): residual and containment wording
Sec. 6: residual (ii) at k = p excludes kappa^ <= 1 (accepted ROT-KP).  'Contains the ZX terminal criterion with S1-sharp'
applies to k >= 2 and kappa^ >= 1; kappa^ = 0 goes to K01 (and k = 1 to K1).

## O5 (optional, adopted): canonical E
Corollary FB-E additionally states: with c defined by g = Y(c), the representatives b = a_i, 1, -s_i (|b| <= p - 2) are
SHgen's canonical signed weights, so E equals SHgen's E_c; moreover t <= n+ <= k - 1 for t >= 1 (n+ = S(N) >= n- = 2t - n+).

## Dependents
evidence/proof-KPS-cond-v2.md (46bf6ecac2b3a2dad778c3dffb76e4b35306c116d00dee8e07c50cd54ca98798, candidate, conditional on
S(p)) cites ROT-FB (b) and reads it through R1 and O2; its own k = p SHgen step is cited to the same ROT-KP verdict scope.
