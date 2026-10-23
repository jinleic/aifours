# k63-residue checkpoint 001 (Sun63Successor)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:16:51-0700. Previous file: `SCOPE-v1.md`
  (sha256 ec574356d6ef7074c268ad8d6ee8efa58d90d245ec748c2b3eba1d442255c2c5, written 02:33:10).
- **Deviation:** this checkpoint is late. The gap from the scope file (02:33:10) to this file exceeds the 30-minute
  cadence (reading and derivation without an intermediate write). Recorded as an actual deviation.
- **New input since scope:** parent verdict `RUN/review/sun7-K62A-TG-parent-verdict-v1.md` sha256
  c792dc68884a0c99632f218fd03833f60b80b89fd2c194137331d35fb4f3fc61 (recorded 02:39:50): TG (general, finite core) and
  K63-CLIQUE (full clique only) are now CORRECTNESS-ACCEPTED premises; K62-A accepted.

## Written progress (not yet frozen as a candidate; no computation run)
1. Lemma S (draft): in the K6.3 residue, every triangle's T-quotient tau is {2,3,5}-smooth (C-triangles:
   tau = k tau_min with k <= second-smallest edge value <= 5; d-triangles: tau <= 8 and tau != 7 since tau_min is even).
   Applies verbatim to the conjugated family g_jU_jg_j^-1 (alpha*).
2. Lemma FG (draft): for v in O = C minus i* with h_v = 0, gcd(n_v, [G : intersection of U_j over all j != v]) divides 6
   (induction adding unmarked O-vertices; each step multiplies by an integer <= 5). Hence the union of the VFC sets
   D_j and the union of the LFC sets g_jU_jU_v each have measure <= 5/6 (not just < 1).
3. Row Lemma (draft): at such v, the LFC/VFC bound 5/6 excludes every row with x_vd = 1 (x = alpha or alpha*), in
   every 5-marker placement. With INV (alpha_vd + alpha*_vd <= 3) this would exclude the whole K6.3 residue.
4. Status: the above is being written up as a candidate with full case coverage; it is unreviewed. Full Sun(7) OPEN.

## Resources
No process launched; no GO requested or held by this worker.
