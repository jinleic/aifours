# K62-STATUS-v1: exact state of the remaining K6.2* classes after this follow-on (navigation + obstruction facts)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T04:08:43-0700.
- **Author:** Sun63Successor. No computation. Labels: CANDIDATE (unreviewed) unless a parent verdict is cited.
  Nothing here is promoted by the K63-RES verdict (sha256 5ac595295727218cd86d0888720213972fe0520f64cea8d93a5c50ef18ed7bac),
  which accepts FG / Corollary 5/6 at the exact K6.3 setting only.

## 1. Candidates in this directory (for the parent's later review)
| file | sha256 | content |
|---|---|---|
| `SETTING-v1.md` | 3bff4e6618cb6591683f7adcc1fbd52fbd3dd16e306b024be6181c332f42bb8d | frozen setting, import boundary |
| `K62-FG-v1.md` | d47e3747ce16ffc21aa818229e79a2028923ec8722aaaae14031e079b4cad083 | Lemma D, Lemma OO, Lemma FG-62, Theorem R2-11, R1 obstruction |
| `K62-FG-erratum-v1.md` | debcb0331cc474f3d5833cd1e5b791ccf209a2f8da7a8414b55685bc6ef05500 | Lemma OO five case, softened remark |
| `K62-FG-erratum-v2.md` | 8365eab65757e944d7e1d2bdcfbbe05d869028647a07b919c7dfec1660cad2ae | attribution overlay (L0.1 + Lagrange, 73a25ba6, Phi, Sun list) |
| `K62-R2-v1.md` | 527ea6682edf4a1ed8e50fc32b75ccb422e227db2ce53b28ce6d4d0038743665 | R2 with e* <= 3 excluded |

If all are accepted: K6.2* with e_d = 2 and e* <= 3 is excluded (with the accepted K62-A).

## 2. Exact remaining K6.2* gap
- **(G-R1)** e_d >= 3 (then e* = 2): every sub-case (3-marker on i*, on t in O, or absent; any 5-marker).
- **(G-R2)** e_d = 2, 3-marker on t in O, **e* >= 4**, and {alpha_(d i*), alpha*_(d i*)} = {1, 3}.

## 3. Obstruction facts (each proved by an explicit dual certificate; they show which single-vertex tools are
## insufficient, not that configurations exist)
For a vertex u and an orientation, "val <= B for every feasible y" is certified by weights u_S >= 0 on ALLOWED sets S
covering every load (sum over S containing j of u_S >= load_j); then val <= sum of u_S.
1. **R1, unmarked v in O, both orientations with the 5/6-bound** (`K62-FG-v1.md` section 5): joint row
   (4,4,2,2 | x_(v i*) = 1) / (2,2,4,4 | 1); certificate value 5.
2. **R1, the five O-vertices together:** the pattern "alpha = 4 on a 5-cycle of O and 2 on its complement, alpha*
   reversed" puts the row of item 1 at every vertex of O, satisfies INV, Lemma OO and the count at d
   (sum over the ten O-pairs of 2^-(1 + v2(alpha_ab)) = 5/8 + 5/4 <= 19/8, the maximum allowed by the d-fibre count with
   all O-edges tight there). So local tests at O-vertices and at d do not exclude it; the i*-row must be used.
3. **R1 at i* with e_d >= 4** (d's label 2^(e_d - 2) * 5^(h_d) w_d, four-like, load 3/2): the i*-row (2,2,2,4,4)
   passes the bound 11/12 available at i* (gcd(n_(i*), [G : intersection over j != i* of U_j]) = 12 when f* = 1):
   allowed maximal sets {F1, F2, d, z_k} (k = 1, 2, 3) and the three pairs {z_i, z_j}; weights 4/3 on each 4-set and 1/3
   on each pair cover all loads (F: 4, d: 4 >= 3/2, z: 4/3 + 2/3 = 2); value 5 <= 11/2.
   (With e_d = 3, d is two-like at i* and every i*-row with entries in {1, 2, 4} and at most two 4s has
   val >= 5 + 3/4 > 11/2 under the weights 1, 1/2, 1/4 and y_d = 1/2; i*-rows with an entry 3 are not covered by this.)
4. **G-R2 (e* >= 4), unmarked v, alpha-orientation with the 5/6-bound:** row u1, u2, u3 unmarked fours, t with
   alpha_vt = 4, alpha_(v i*) = 3, no 5-marker. Types 4, 4, 4, 3^F * 4, 2^(e* - 1) * 3 (four-like, gcd 12 with t),
   d = 2 (load 3). Maximal allowed sets: M1 = {u1, u2, u3, t, i*}; M2_k = {d, t, i*} cup ({u1, u2, u3} minus u_k);
   M3 = {d, u1, u2, u3}. Weights 1 on M1, 1 on each M2_k, 1 on M3 cover all loads (u: 1 + 2 + 1 = 4; t: 1 + 3 = 4;
   i*: 4 >= 3; d: 3 + 1 = 4 >= 3); value 5. So the alpha-row (4,4,4,4 | 3) survives at v; in this sub-case the
   alpha*-orientation at v has only the plain bound, and the 23/24 bound at i* (Step B of K62-R2) is not available.

## 4. What a closure of G-R1 / G-R2 seems to need (navigation, not a claim)
Constraints coupling the i*-row with the O-rows (x_(v i*) = x_(i* v)), for example: at i*, threes in the row force,
at the corresponding unmarked O-vertex v, the row (4,4,4,2 | 3) (the only R1 survivor with x_(v i*) = 3 when t is not a
neighbour, by the 5/6-bound); combined with INV on the i*-edges this restricts the i*-row strongly. No finite
certificate architecture is proposed here; the parent asked for written work and no LP is admitted.
