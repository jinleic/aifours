# K63-TG-erratum-v3: step (v) when no C-vertex has an even cofactor (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:15:17-0700.
- **Overlays:** `K63-TG-v1.md` (sha256 3e6a7cf604027a60f5e0b055c5d203cc0c167e08ca59ac81c36fc3a943ebc071), `K63-TG-erratum-v1.md` (sha256 1dbcac91c17af170c752efd569a5bdbc37047cab852819a832029aa574fe0bdf), `K63-TG-erratum-v2.md`
  (sha256 22ccda2faff32b04b8aaa72646fc84038dc0a3942dc39fd59641e49beced8ec3); all frozen.
- **Source:** parent read (minor), received by IRC before this file was created.

## E4: no i*
The corrected Theorem K63-CLIQUE (erratum v2) also covers configurations in which no C-vertex has e >= 2, i.e. every
C-cofactor r_c is odd; then "i*" and D_(i*) in section 2 (iii) and (v) are undefined. In that case all labels
lambda*_c = 3 r_c (c in C \ {v}) are odd, so gcd(lambda*_d, lambda*_c) is 3 (f_d >= 2) or at most 1 (f_d = 1), and no
pair has gcd >= 4. Hence no allowed S_R contains d together with three elements of C (a 4-set needs a pair with
gcd >= 4), so D_d is disjoint from the union of the D_c, each of whose cosets carries three C-elements by (iv). Then
the union of all D_j has measure >= 5/6 + alpha*_vd / 3 >= 5/6 + 1/3 > 1, contradicting (V4). If i* exists, it lies in
C \ {v} (v is chosen with gcd(r_v, 6) = 1) and section 2 (v) applies as written.
