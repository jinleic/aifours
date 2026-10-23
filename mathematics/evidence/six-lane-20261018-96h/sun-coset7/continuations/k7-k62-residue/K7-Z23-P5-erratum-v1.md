# K7-Z23-P5-erratum-v1: imports, transfer hypotheses, one omitted pair, case split, notation, inverse dictionary (no theorem change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:51:55-0700.
- **Overlays:** `K7-Z23-P5-v1.md`, sha256 632550329619f441868f38c3435d4a42559e599e20c1c2db100945dff9ff8e04, frozen byte-identical.
- **Responds to (read in full):** Codex `RUN/review/sun7-Z23P5-codex-v1.prompt.stdout.txt` (sha256 48075068be4025a2c70e9c44cf5d50267fd92bedcd7b3a05d6313989b6fb4169; ACCEPT, 0 FATAL /
  0 MAJOR / 0 MINOR) and Claude `RUN/review/sun7-Z23P5-claude-v1.prompt.note.md` (sha256 72448243718468e64a46499f07988394dc4c3cc826453579dac3a2b812d8fa7b; ACCEPT-WITH-FIXES,
  0 FATAL / 0 MAJOR / 6 MINOR m1-m6). RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Status:** written overlay. Theorem Z23-P5 keeps its exact statement and scope (2- and 3-markers together on z,
  5-marker on p != z, E,A,B >= 1 unbounded; arbitrary groups via R0). No new premise, no computation.

## P-1 (Claude m1): imports named exactly

Add to the import list of section 0:
- **`K7-LFC-INV-erratum-v1.md` E2** (Sun(2): two pieces with coprime local indices never share a fibre / right coset)
  and **E6** (the inverted configuration has the same labelled index tuple, hence the same vertices z, p, the same
  marker products and the same hypotheses of section 0; inversion is an involution, alpha** = alpha).
- **VFC (V2) and (V3)** of `rules-k7-v1.md`: LT1 and LT2 of section 2 are (V3) applied with the (V2) local indices
  d_j = q_j n_j / 6 = alpha*_zj r_j (q = alpha* by INV (b)).
- **Primary acceptance of L1 (T1)-(T3), VFC (V1)-(V4) and F7** (the forced condition of addendum A1): the written verdict
  `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` sha256
  73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35. The Z2 parent verdict (sha256 0f6b9aa3...5b19c) is
  confirmation of their K7 use; application of L1 and F7 to the inverted configuration is as in `K7-Z2-erratum-v1.md` G5
  (sha256 3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9).

## P-2 (Claude m2): the degree transfer at z, clause by clause

In section 1 replace "This is precisely the accepted ROW-1 degree transfer (five unmarked labels, one odd {3,5}-smooth
label; no condition on the apex's own cofactor)." by:

**"ROW-1-deg holds at z (`K7-Z2-erratum-v1.md` G2): (i) g_zj = 6 for all six neighbours (K7); (ii) the five labels
lambda_u = w_u alpha_zu (u in W) have the w_u pairwise coprime and prime to 30; (iii) the sixth label is
lambda_p = m w_p alpha_zp with m = 5^B odd and {3,5}-smooth, with the actual exponent B as in `K7-M1-erratum-v1.md` F2,
and w_p prime to 30 and to every w_u; (iv) LFC (d) holds at z. The apex's own cofactor 2^E 3^A w_z enters only through
the bound 1 - 1/n_z. Renaming: ROW-1's apex v becomes z and ROW-1's marked neighbour becomes p."**

## P-3 (Claude m3): the omitted allowed pair {two, z} in section 4.3

In the feasibility paragraph of section 4.3, insert after "For k=2 remainder twos, c=3, each two only partners z, and
their triple with z has all gcds2 and is forbidden;":

**"A remainder two always partners z (gcd(2 w_u, 2^(E+2) 3^A w_z) = 2) and partners p only for c in {2, 4}. The pair
{two, z} weighs 1/2 + 1/3 = 5/6 in the k = 2 rows and 2/3 + 1/3 = 1 in the k = 3 rows with c in {1, 2, 3, 5}; in the
k = 3, c = 4 row the two has weight 0. The block {z} cup {remainder twos} has all pair gcds 2, so it has no allowed
triple (Sun(3))."**

This completes the list of allowed sets; every certificate weight and every total of the table is unchanged.

## P-4 (Claude m4): split of the s*_b = 1 exclusion in section 5

Replace the paragraph "We next show s*_b=2 for every b in F. ..." up to "Therefore all s*_b=2, and each D_b (b in F)
has measure1/3." by:

**"We show s*_b = 2 for every b in F = P cup {p}. Suppose s*_b = 1.
- Case b = p. Take any v in W3. The inverse triangle {z, v, p} has alpha*-values (alpha*_zv, alpha*_zp, alpha*_vp) =
  (4, 1, x*_vp). Its compulsory term 4/gcd(4, ell_p) = 4 (ell_p = 5^B w_p odd), so tau*_min >= 4, while
  tau*_max = min(x*_vp, 4 min(1, x*_vp), min(4, x*_vp)) = min(x*_vp, 4). Hence x*_vp >= 4; x*_vp = 5 would give
  tau*_min divisible by 20 (r_z has no factor 5), so x*_vp = 4. But alpha_vp = 3 (section 4.2, k = 2), and
  3 + 4 > 6 contradicts INV.
- Case b in P. Take any v in W3. The original triangle {z, v, b} has x_vb = 2 and s_v = 2 (shown above), tau_min = 4,
  and F7 at apex z gives X_v subset X_b (4 * 6 >= 6 * 2 * 2). Hence D_b subset Y_b subset Y_v = D_v (zv tight). The
  local indices d_b = alpha*_zb w_b = w_b and d_v = 4 w_v are coprime, so by LT2 the nonempty D_b (measure 1/6) cannot
  lie in D_v. Contradiction. (No inverse-triangle computation is used in this case.)
Therefore all s*_b = 2, and each D_b (b in F) has measure 1/3."**

## P-5 (Claude m5): notation and one precise value

- In sections 5 and 7 rename the edge values x := alpha_vu (section 5) and x := alpha_ab (section 7) to **x_vu** and
  **x_ab**, and their inverse counterparts to **x*_vu**, **x*_ab** (the letter x is used by L1 for vertices).
- In section 5 replace "Thus tau_min=4 (the third term x/gcd(x,r_z) divides2)" by **"Thus tau_min = 4: the third term
  x_vu / gcd(x_vu, r_z) equals 1, since x_vu in {1, 2} and 2 | r_z (E >= 1)."** (In section 7, for x_ab in {1, 2, 4},
  the third term divides 4, as written there; for E = 1 and x_ab = 4 it equals 2.)

## P-6 (Claude m6): explicit inverse dictionary

Add at the end of section 5, and read every "inverse" step of sections 1, 3, 4, 6 and 7 with this dictionary.
**The inverted configuration C* (alpha-matrix alpha*, VFC vector q = alpha, the same z, p and markers by E6) satisfies
sections 1, 3, 4 with alpha and alpha* exchanged; its own F, F* are our F*, F, and its s, s* are our s*, s. In the
repetition of section 5 for C*:**
- **W3* := {v in W : alpha*_vu = 3 for some u in W}. Section 4.3 in C* gives alpha*_vz in {1, 2} for v in W3*, so W3*
  avoids our F* and lies in our F. Since |W3*| >= 3 = |our F|, W3* equals our F; hence p lies in our F*, and
  P* := (our F*) cap W has size 2;**
- **the tight edges are zv for v in our F (alpha_zv + alpha*_zv = 4 + 2 = 6 after s*_v = 2 is forced);**
- **the value excluded is s_a = alpha_za = 1 for a in our F*. For a = p the case uses the original triangle {z, v, p}
  with values (4, 1, x_vp), forcing x_vp = 4, against alpha*_vp = 3 (section 4.2 in C*), contradicting INV. For
  a in P* the case uses F7 in C* and LT2* (local indices alpha_za w_a = w_a and alpha_zv w_v = 4 w_v are coprime);**
- **the light sets are D*_a (a in our F*), of measure alpha_za / 6 = 1/3, and LT1*-LT3* of section 2 apply.**
This yields the contradiction for C* exactly as for C. In section 7, the case "only a0 exists" is the case "only b0
exists" of C* under the same dictionary (our a0 plays the role of C*'s b0), as in `K7-Z2-erratum-v1.md` G9.

## Non-defect remarks recorded (no change)

Claude: the section 8 frontier sentence is conditional and not a premise; with A = 0 the section 4.3 certificates would
only improve (out of scope). Codex: all sections ACCEPT with full tables re-derived (including the exact objectives of
section 4.3) and no finding.

## Unchanged

Theorem Z23-P5, all certificates, tables, totals, the arbitrary-exponent audit and the R0 lift are unchanged. The
different-vertex family (2- and 3-markers on different vertices; 5-marker absent, on one of them or on a third vertex)
remains OPEN. No novelty, Lean or human-review claim.
