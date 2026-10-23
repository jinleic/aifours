# K7-D23-RICH-erratum-v1: NO5 (a) last branch without Sun(6) or propagation (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T05:26:21-0700.
- **Overlays:** `K7-D23-RICH-v1.md`, sha256 ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3, frozen byte-identical.
- **Source:** parent full read (IRC), import-accounting finding: the branch "e = 5 and all four W-entries 5, c != 3" of
  Lemma NO5 (a) used y = 1/5 on six labels with pairwise gcd 5, i.e. a direct Sun(6) instance, contrary to section 0,
  which allows Sun(5)/Sun(6) only inside the imported ROW-U class analysis.
- **Status:** written overlay; no statement of the file changes. No computation.

## R-1: replacement of the last branch of Lemma NO5 (a)

In Lemma NO5 (a), case "Bz >= 1 (so Bt = 0)", replace the text from "If e = 5 and all four W-entries are 5:" to the end of
that case ("... contradicting LFC (d) for the inverted configuration.") by:

**"If e = 5 and all four W-entries of u are 5, then INV (b) (alpha + alpha* <= 6, alpha* >= 1) gives alpha*_uv = 1 for the
four v in W \ {u} and alpha*_ut = 1, while c* := alpha*_uz lies in {1, 2, 3} (D23-MIX for alpha*). At u in the inverted
configuration (INV (a), E6) the labels are w_v (four W-neighbours), lambda*_t = 3^A w_t (Bt = 0) and
lambda*_z = 2^E 5^Bz c* w_z. The four labels w_v are coprime to every other label, and gcd(lambda*_t, lambda*_z) is 3 if
c* = 3 and 1 otherwise. If c* = 3, put y = 1 on the four W-neighbours and on z (y_t = 0): val = 4 + 3 = 7. If c* in
{1, 2}, all six labels are pairwise coprime; put y = 1 on all six: val = 4 + 1 + c* >= 6. Every allowed set is a
singleton or {z, t} (the latter only when c* = 3, and then y_t = 0), so y is feasible, and both values contradict
LFC (d) for the inverted configuration."**

This argument is local to u, uses only LFC (d) for the inverted configuration and Sun(2) (through LFC (c)), and covers
every c in {1, 2, 3}; the former sub-cases "c != 3" (with its Sun(6) instance) and "c = 3" (with the propagation to the
other vertices of W) are withdrawn and are not needed.

## R-2: import accounting confirmed

After R-1 the new arguments of the file use Sun(2), Sun(3) and Sun(4) only (through LFC (c) and VFC (V3)); Sun(5) and
Sun(6) enter only inside the imported ROW-U class analysis (E8 standard weights), exactly as section 0 states. No other
step of the file uses a set of five or six pieces directly: NO5 (b), Lemma R3, Lemma CC and Lemma LZ bound allowed sets
by Sun(4) (four pieces of pairwise gcd 3), Sun(3) (three pieces of pairwise gcd 2) and Sun(2).

## Unchanged

Lemma NO5 and every other statement of `K7-D23-RICH-v1.md` (FG7, Corollary 5/6, R3, TR, CC, Theorem K7-D23-RICH, TZ, LZ,
the residue description of section 9) are unchanged. (a2) and the (a1) rows without a W-three remain OPEN.
