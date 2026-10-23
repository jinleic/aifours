# Frozen scope addendum 1 to ASSEMBLY-P-scope-v1.md: the accepted-interfaces-only part (Corollary ASSEMBLY-P0)

Owner OlsonAssemblyP. Frozen after /bin/date 2026-10-19T11:35:16-0700, BEFORE any written derivation of the statement below.
Applies after ASSEMBLY-P-scope-v1.md (sha256 5a4d9064b05e7dfbc9ac478ba3df95e89de00b573be379c3ce968ec848c2f64f, frozen 11:30:13),
which is unchanged. Status: CANDIDATE_UNVERIFIED target, not a proof and not a verdict. Written research only.

## Added candidate statement
U(p) is exactly as defined in Proposition DEP of the scope v1. Call a word w over D_(2p) P0-ADMISSIBLE if o_F(w) <= p-1, or
o_F(w) = p and kappa(w) is not in U(p) u {p-1} (kappa(w) = p - 1 - (F - o_F)/2 as in the scope v1).

**Corollary ASSEMBLY-P0 (no pending premise).** Let p >= 7 be prime.
(A0) Every P0-admissible avoider of length 4p-2 over D_(2p) satisfies INV*.
(B0) Every P0-admissible word of length 4p-1 over D_(2p) has an identity 2p-subword in increasing original index order.
Neither [ONE-SHORT-LS] nor [ROT-SING] nor any other pending candidate is a premise. Trust: the accepted interfaces only,
including Lev 2022 Theorem 2 exactly where the accepted ASSEMBLY-LS/ROT-LS verdict records it (p >= 11) and S(p) through ROT-KP+.

## Route to be checked (not assumed)
1. o_F(w) <= p-1: accepted ASSEMBLY-LS (A)/(B) verbatim.
2. o_F(w) = p, some admissible normal form with k <= p-1: accepted ROT-LS. All normal forms with k = p: kappa^ = kappa(w)
   (o_F = k), so the k = p routing of the scope v1 never reaches [ONE-SHORT-LS] (kappa^ in U(p)) or [ROT-SING] (kappa^ = p-1).
3. (B0): the accepted ledger's case analysis with class preservation checked case by case: Case 2 deletion has o_F <= p-1;
   a Case 3 deletion has o_F <= p-2 or (o_F = p, same F, same kappa); Case 1 needs only o_F <= 2p-3. Identify the accepted
   precedent for using the ledger with a class that is not of the pure form o_F <= B, or isolate the gap.

## Not claimed
As in the scope v1; in particular no statement for o_F = p with kappa(w) in U(p) u {p-1} without the pending premises.
