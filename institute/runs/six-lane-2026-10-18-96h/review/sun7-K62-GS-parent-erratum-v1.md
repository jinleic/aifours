# K62-GS parent citation and wording erratum v1

Recorded at 2026-10-19T11:22:46-0700. Read after immutable [K62-GS-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/K62-GS-v1.md) `020fdc7aacf105c224842990dbd434ecd49a86e39e2e70ca0f6ced41b57b4627`. Disposes Claude review `1a5527de67ea298ab153864b5b98db9aee69774eac46dfc459395a931845ddd9` m1, m2, m4, m5 and m6; Codex `fecc0372b94a9bacebeae22387a3fd3d50852f495584d588e462a969ac9d882c` had no findings. No theorem statement, case split, inequality or proof step changes. Each Old span occurs exactly once in the immutable file.

## m1 provenance of the P1 value set (table row)

Old:
````text
| E3-a | same verdict; K62-E3 C2 sub-claim (a) (erratum v2 Z11) | every O-O value of alpha and alpha* lies in {1, 2, 4} |
````

New:
````text
| E3-a | same verdict; K62-E3 C2 PROOF sub-claim (a) (erratum v2 Z11), reviewed by both families only inside the accepted C2 proof and not an accepted standalone statement; its orientation hypotheses hold in G for both families (both distinguished entries 1, E3-L1) | every O-O value of alpha and alpha* lies in {1, 2, 4} |
````

## m1 provenance of the P1 value set (section heading)

Old:
````text
## 2. Basic facts (each proved here; the accepted sources are cited for cross-checking)
````

New:
````text
## 2. Basic facts (P2-P5 derived here from the section 1 imports; P1's value set is the E3 C2 proof sub-claim (a); the accepted sources are cited for cross-checking)
````

## m5 both-family authority for P2

Old:
````text
| APEX, DG-3 | CAP-DT verdict `84061c6f…34a0` item 5 (DT-A §1 table, both families, admissible only); SH-DG verdict `cae455c3…ddda` item 3 (DG-3, erratum G3) | P2 (also re-derived) |
````

New:
````text
| APEX, DG-3 | CAP-DT verdict `84061c6f…34a0` item 5 (DT-A §1 table, admissible only); SH-DG verdict `cae455c3…ddda` item 3 (DG-3, erratum G3, accepted for the alpha*-family) | cross-reference only: P2 is re-derived for the actual x-configuration; its both-family authority is L1 + INV (a)/E6, as in CAP-DT erratum-v2 V11 |
````

## m4 setting of Lemma EQ

Old:
````text
**P5 = Lemma EQ.** Let v, a, b be distinct vertices of O and x a family with
````

New:
````text
**P5 = Lemma EQ.** In G (so v is unmarked, both distinguished entries are 1 and n_a = 6w_a, n_b = 6w_b), let v, a, b be distinct vertices of O and x a family with
````

## m2 Lemma TRI wording

Old:
````text
most two triangles, and two of its triangles share an edge (so it then contains a diamond, i.e. K4 minus an edge).
````

New:
````text
most two triangles, and any two distinct triangles share an edge (so a graph with two triangles contains a diamond, i.e. K4 minus an edge).
````

## m6 depth notion

Old:
````text
(a positive integer, Lagrange); the **type** of R is its sorted x-values; R is **deep** if delta(R) >= 4.
````

New:
````text
(a positive integer, Lagrange); the **type** of R is its sorted x-values; R is **deep** if delta(R) >= 4 (as e_d >= 4, this coincides with DG's capped depth min(e_d, delta(R)) >= 4).
````

## m6 dependency bookkeeping

Old:
````text
FB (uses P3, P4, T16, ONE, DEG; not DG) -> DEEP (DG + FB + T16)
````

New:
````text
FB (uses P1, P2, P3, P4, T16, ONE, DEG; not DG) -> DEEP (DG + FB + T16 + P2)
````


## Supplementary note to m1 (not load-bearing)
Claude also offered an in-G derivation of P1's value set: x <= g-1 = 5 by INV E1; value 3 is excluded by accepted E3 Lemma 2; value 5 by Lemma 2 when h_d >= 1; if h_d = 0 and x_vu = 5, lambda_u = 5w_u and lambda_d = 2^(e_d-1)w_d are coprime, so y_u = y_d = 1 is feasible and val = 5+3 = 8 >= 6 contradicts LFC (d); for alpha* apply this to the inverse via INV (a)/E6. This alternative was reviewed by one family only and is recorded as a cross-check. The verdict relies on the E3 C2 proof sub-claim at its orientation scope.

## No change needed
- m3: P2's forward reference to P4 is not circular; P4 uses only the definition of tau, lcm = 6w_aw_bw_c and L0.1.
- Observation: in FB (v), the set equality from P3's equality clause carries no load, since mu(Phi_bW_(R_b)) = k_b/6 = 2/6 already follows from k = 6mu.
- "EQ -> BUD -> DEG" in section 7 is a listing order, not a dependency chain; the corrected dependency graph is acyclic.
