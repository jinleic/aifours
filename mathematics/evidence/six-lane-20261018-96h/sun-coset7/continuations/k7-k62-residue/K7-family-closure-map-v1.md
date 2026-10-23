# K7 family closure map v1: dependency DAG for the 2-marker != 3-marker K7 family (CONDITIONAL; no closure claim)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:56:51-0700.
- **Owner:** Sun7K62Successor. Navigation and bookkeeping only: no new mathematics beyond the elementary exhaustion
  argument of section 2; no computation. Every edge below is labelled with its file, sha256, status and covering review.
  **No closure is claimed**: the map only records that, IF every pending edge is accepted, no configuration of the family
  remains.

Reviews: **[A]** accepted (verdict cited); **(1)** A1/A2 overlay repair verdict (pending); **(2)** dual review of
`review-package-CASEA-CELL-v1.md` (e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583); **(3)** dual review of `review-package-A2-ZT5-v1.md`
(75146e9faf7db2be4b337a5b8ec75e01a43f0a61c09facefe7cd274a47280157), declared conditional on (2).

## 1. The family

Class K7 (README of the 2026-10-16 lane, sha256 2a6d6d6e...3fd1; accepted): seven pairwise disjoint cosets with indices
n_i = 6 r_i, the r_i pairwise coprime, r_i = m_i w_i with m_i the {2,3,5}-part and the w_i pairwise coprime and prime to 30.
By pairwise coprimality each of 2, 3, 5 divides at most one r_i; the vertex with 2 | r_z (resp. 3 | r_t, 5 | r_p) is the
2-marker z (3-marker t, 5-marker p). **F** := the K7 configurations having a 2-marker z and a 3-marker t with z != t.
"Inverse" = the inverted configuration (INV (a), E6: same labelled indices and markers, alpha <-> alpha*); "mirror" =
the case obtained by exchanging the roles of (alpha, T) and (alpha*, T*), which is the inverse of the original case.

## 2. Exhaustion (proof)

Let C be in F. (i) If there is no 5-marker, or it is z or t, then r_z = 2^E 5^Bz w_z, r_t = 3^A 5^Bt w_t with Bz Bt = 0
(z has no factor 3 and t no factor 2, by coprimality) and the other five vertices are unmarked: C is in **(a1)**.
(ii) Otherwise the 5-marker is a third vertex p, r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p, W' := V \ {z,t,p} is
unmarked: C is in **(a2)**. (iii) In (a2), put **(a2-zt5)** := some orientation has z-t entry 5; **(a2-o5)** := not
(a2-zt5), but some entry of alpha or alpha* equals 5; **(a2-no5)** := no entry of alpha, alpha* equals 5. These three
cases are exhaustive and pairwise disjoint by definition, and each is inversion-stable (E6 keeps the markers and swaps
alpha, alpha*). (iv) In (a2-zt5), alpha_zt + alpha*_zt <= 6 with both >= 1 (INV (b), E7), so exactly one orientation
carries the five; by (iv) and inversion it may be called alpha. Hence **F = (a1) cup (a2-zt5) cup (a2-o5) cup (a2-no5)**,
a disjoint union of inversion-stable classes, and (a2-o5) is empty by Lemma F (edge E-a2-1). QED

## 3. Edges

| id | from -> to | claim used | file(s) and sha256 | status | review |
|---|---|---|---|---|---|
| E-0 | F -> (a1), (a2) | exhaustion (section 2) | this map | elementary | - |
| E-a1-1 | (a1) -> 3-type z-rows in both orientations; T, T* >= 3 | D23-MIX | `K7-D23-NO4-v1.md` a3b47626...189d + erratum 594c28aa...ba69 | accepted | [A] d3453de1...e37db |
| E-a1-2 | (a1) -> T = W or T* = W | RICH TZ (iii), NO5, R3, TR, CC | `K7-D23-RICH-v1.md` ba32d282...f2bb3 + 8261831b...0ba69 + 55cb66ca...4d428 | accepted | [A] 1167bc4f...aec0 |
| E-a1-3 | (a1) -> Case A (T = T* = W), Case B (T = W != T*), Case B' (T* = W != T) = inverse of Case B | E-a1-2 + definitions | - | elementary | - |
| E-a1-4 | Case A, Case B -> entries in {1,2,4}, Lemma B, Corollary L, CASEB data | Cor W3, E3, PFG-t, Cor L, Lemma B, Thm CASEB | `K7-A1-STRUCT-v1.md` c8a16f14...e3ccf via overlay 0e477743...7e54e | pending | (1) |
| E-a1-5 | Case A -> all-(2,2) structure excluded | Thm K7-TC-A22 (uses R1 at E = 1) | `K7-TC-A22-v1.md` 9ebec279...1b46b41; `K7-TC-v1.md` cc48340d...e117 via overlay | pending | (1) |
| E-a1-6 | Case A (not all-(2,2)) -> K_{2,3} family or its inverse | Thm K7-CASEA-K23 (rows, K3, K2, CL, S, (S-a)-(S-f)) | `K7-CASEA-K23-v1.md` f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3 | pending | (2) |
| E-a1-7 | K_{2,3} family (and inverse) -> empty | Thm K7-CELL-A (EQ, SUB, IN, CELL) | `K7-CELL-v1.md` d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae + erratum 56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132 | pending | (2) |
| E-a1-8 | Case B -> alpha*_v1v2 = 2, alpha* = 2 on T* | Thm K7-TC-B (uses Lemma FG-V) | `K7-TC-v1.md` via overlay (TC.7-TC.10) | pending | (1) |
| E-a1-9 | Case B -> alpha_ta = 2, alpha*_ta = 4 for all a | Prop K7-CASEB-T | `K7-CASEA-K23-v1.md` f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3 | pending | (2) |
| E-a1-10 | Case B (and Case B' by inversion) -> empty | Thm K7-CELL-B (C.4 correction) | `K7-CELL-v1.md` + erratum | pending | (2) |
| E-a2-0 | (a2) -> both z-rows of type (b') | Thm K7-D23P | `K7-D23P-v1.md` 89739dc2...37880 | accepted | [A] 1167bc4f...aec0 |
| E-a2-1 | (a2-o5) -> empty | Lemma F (F1)-(F7) | `K7-A2-FIVE-v1.md` 93fd95d7...8dfc via overlay | pending | (1) |
| E-a2-2 | (a2-no5) -> (a1)-type data with W = W' cup p | Thm K7-A2-BRIDGE (enumerated claims), FG-a2, D23-a2 | `K7-A2-FIVE-v1.md` via overlay (A2.10-A2.16) | pending | (1) |
| E-a2-3 | (a2-no5) -> A1-package claims | Cor K7-A2-TRANSFER (named claims) | `K7-A2-FIVE-v1.md` via overlay (A2.17) | pending | (1) |
| E-a2-4 | (a2-no5) -> empty | Cor K7-CC-A2 (transfer of CASEA-K23 and CELL) | `K7-CASEA-CELL-A2-TRANSFER-v1.md` 84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6 | pending | (3) |
| E-a2-5 | (a2-zt5) -> normalised orientation, z-row (3,3,3,3,3 | t 5), E >= 2 | Lemma F, Prop K7-A2-ZT5 | `K7-A2-FIVE-v1.md` via overlay | pending | (1) |
| E-a2-6 | (a2-zt5) -> T* = W or |T*| = 3 (with O*-data) | Lemma FG-zf, Lemma ZS | `K7-A2-ZT5-A-v1.md` 4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919 | pending | (3) |
| E-a2-7 | (a2-zt5), T* = W -> empty | Thm K7-ZT5-A | `K7-A2-ZT5-A-v1.md` | pending | (3) |
| E-a2-8 | (a2-zt5), |T*| = 3 -> empty | Thm K7-ZT5-B | `K7-A2-ZT5-B-v1.md` f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8 | pending | (3) |

Common accepted foundations of every edge: LFC/INV (`K7-LFC-INV-v1.md` 45be9162...726c + 7af9acf0...75bd5, verdict
8621e744...ca18), rules-k7 L0.1-L0.3/L1/VFC (77b9afec...cee, verdict 73a25ba6...3f9d), R0, Sun(2), Sun(3); transitive
computer-assisted Sun(5)/Sun(6) records 2cf02436...5301 and efe1d849...1e29.

## 4. Conditional reading

If every edge marked pending is accepted at its stated scope, then (a1), (a2-o5), (a2-no5) and (a2-zt5) are empty, and by
section 2 so is F (including mirrors and inverses, each class being inversion-stable and every case having been treated in
both orientations or reduced by inversion). This is a conditional dependency statement only; **no closure of F, of K7 or
of Sun(7) is claimed**. Outside F (other K7 classes, K6.2*) nothing is asserted here.
