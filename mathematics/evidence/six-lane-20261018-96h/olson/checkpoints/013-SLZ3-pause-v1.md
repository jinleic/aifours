# Checkpoint 013: Theorem SLZ3 (candidate); LS residue sharpened; state at pause

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:28:37-0700.  Continues checkpoint 012 (e5679ad2c1ce895efd6376528e74316b28107c2dfd0230d4de73b9c649ee6477).

## Actual result since 012
- CANDIDATE (unreviewed): evidence/proof-SLZ3-v1.md 0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c: for floor(2p/3) + 1 <= kappa <= p - 1, under (ZP_kappa) every
  shortest long zero-sum has length <= 3kappa + 1 (induction on kappa from S1-sharp; S1-sharp's Steps 1-9 with N >= 3kappa + 2
  replacing p >= 3delta - 1; Step 3 via SLZ3 at kappa - 1).  Sharp at kappa = (2p + 1)/3 (F1).  Improves SLZ.
- Minimum-transversal observation (written here, not frozen elsewhere): in an LS counterexample let D be a minimum transversal
  of the long zero-sums (tau = |D| >= 2 by PAIR (a)); adding back any d in D to Y - D creates a long zero-sum, so EXT' fails for
  Y - D: t0(Y - D) >= min(kappa + 2 - tau, kappa - (tau - 1)/2).  For tau = 2: Y - D (length p + 2kappa - 1) is (S1) with a
  2kappa-zero-sum whose complement has length p - 1, below the range of SC0 and of S(p) (non-SC zero-sum-free odd sequences
  of length p - 1 exist).

## Exact blocker
LS: the residue of PAIR (no term meets all long zero-sums; no two terms meet all 2kappa-zero-sums); in the tau = 2 sub-case the
relevant complements have length p - 1.  LS+: sequences with terms outside every shortest long zero-sum (SLZ3 covers the
rest).

## Pending with the parent
Review packet: proof-KPS-v4.md 68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170, import-Sp-XiaYuan-v1.md d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7, proof-SLZ-EXT-v2.md 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751;
new candidate proof-SLZ3-v1.md 0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c; notes-LS-propagation-v1.md be14d640f97f47e119f31d2e9b4bc5d7ef8c4f33129346e953435c6334c0de5d (context).

## Next bounded action (on wake)
Errata for any review findings; then LS+ beyond SLZ3: the extension step 'a (ZP_kappa), not-(S1) sequence of length 3kappa + 1
admits no further odd term' using SLZ3's two-atom structure when N is large and the extremal family h^a (3h)^b as the target.
