# K62-E3-erratum-v1: three wording repairs from my own re-read (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T04:32:18-0700.
- **Overlays:** `K62-E3-v1.md`, sha256 70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372 (frozen, unchanged).

## F1: Corollary (C2), first sentence
"The fibres containing (U*_c cap U*_c')U_d number at least ..." reads: "The fibres **contained in**
(U*_c cap U*_c')U_d (a union of left U_d-cosets) number at least n_d / gcd(n_d, [G : U*_c cap U*_c']) =
n_d / 2^(1 + v2(alpha*_cc')), and each of them has B(F) containing {c, c'} (step 3 with Q = {c, c'})."

## F2: Lemma 2, item (ii)
Item (iii)'s argument (four 1-entries in the other orientation) applies whenever F5 = O minus {v}, whatever
x_(v i*) is; item (ii) is therefore redundant. It is correct as written and is kept; no case depends on it.

## F3: Lemma 3, the sentence on h_d >= 1
"so the pair factor alpha*_(c_1 c_2) and every k <= alpha*_ej <= 4 are prime to 5" reads: "then no O-vertex is
5-marked, so p does not exist and the order starts with t (if t exists) or with any vertex; T_1 = n_(c_1) has no
factor 5 and every later k satisfies k <= alpha*_ej <= 4, hence is prime to 5."

Nothing else changes.
