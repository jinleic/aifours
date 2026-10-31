# info-6 frontier: sharpness and equality structure for the rank≤4 Z₈ bound

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T20:44:45-0700 PDT**. Additive to the unreviewed `frontier-20261028-four-zero-radical-reduction-v1.md` (SHA-256 `89ca5480f9c4375cc0a82b313fd66c554941bfc7856bdea3e326935a94eeb229`, 63 LF). This is **not** an NL242 witness or a novelty claim.

## Exact equality case

For the no-peak-bound statement in the predecessor, if a balanced f has T≠0, rank(B_q)≤4 and `|Z₈|=8`, then Z₈ is a **linear 3-plane**. Indeed the predecessor proves its indicator has degree≤5 on K. A derivative has degree≤4 and hence is either zero or has weight at least `2^(8−4)=16`; its weight is at most 16. Any difference of two support points produces overlapping supports and hence a zero derivative. Thus the eight support points form one coset of the period subspace; since 0∈Z₈, it is a linear 3-plane. This equality statement does not assert that the plane is generally contained in the radical.

## An actual balanced sharpness example

The pinned candidate is an actual 512-bit Boolean truth table, independently checked by direct 512×512 Walsh character sums, FWHT, inverse and Parseval. It has

- weight 256, T=141 and even-half polar rank 2;
- `Z₈={0,34,157,191,336,370,461,495}`, a linear 3-plane of exactly eight frequencies;
- three actual Walsh-zero coefficients, peak **80**, and nonlinearity **216**.

The example attains the predecessor's rank≤4 lower bound |Z₈|≥8 **without a peak bound**. In this example only, Z₈ is contained in the polar radical. Its peak is far above 28, so it does not attain, approach as a certificate, or decide the balanced NL242 target. The no-peak-bound sharpness example does not prove that a peak≤28 target can attain equality.

## Pinned evidence

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-z8-anneal-a-candidate.json` | `49e16feb05671b8fa422da520899f796f71bb928d95b42a1b4c30ddb13a5d2e5` | 8 |
| `frontier-20261028-z8-anneal-a-audit.json` | `1809b585aad66732fc62a6386f3113846d56aa63cb2afd0d07c55c18af5b0ee4` | 565 |
| `frontier-20261028-z8-sharpness-check.py` | `a0d7d9a3f066c63de621e87bf98b090d4a7d1751d4a40b50cc2d2c389c6ce47e` | 60 |
| `frontier-20261028-z8-sharpness-check-result.json` | `a7f68f9e693a913261eab10338fcfbb6729866de618a85b4386539cf3368e94c` | 30 |
| `frontier-20261028-z8-anneal.cpp` | `dd122965cb4e73c571c10f4ee481a1c1cf38a6bf7c163db34161d34f6e957554` | 45 |

The equality proof and earlier rank-reduction theorem remain author-owned and unreviewed; the executable controls do not replace disjoint review. **END.**
