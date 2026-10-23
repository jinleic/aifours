# Case-A working notes v5 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:08:27-0700. Unchecked scratch; no computation.

## Lemma 2F3S (sketch)
Apex a in W of C (C^alpha or C^alpha*), count masses m_j = (alpha* of C)_aj / 6. Suppose that on W cup {t} \ {a} the
masses are exactly 4/6, 4/6 (vertices g1, g2) and 2/6, 2/6, 2/6 (vertices s1, s2, s3), with z of mass 3/6 (local
indices: entry * r_j). A coset holding g1, g2, t or z holds at most one two ({g, s, s'}, {z, s, s'}, {t, s, s'} have
all gcds 2); a coset with none of them holds at most two twos. With Q := cosets meeting g1, g2 or z and P2 := pure two-two
cosets: 1 = two-mass <= mu(Q) + 2 mu(P2), mu(Q) >= 4/6, so mu(union) >= (1 + mu(Q))/2 >= 5/6. FG at a (union <= 5/6)
forces mu(Q) = 4/6, mu(P2) = 1/6, D_g1 = D_g2 = Q. Hence **if some s_i has D_si cap D_gj = empty, contradiction**
(s_i's 2/6 would need P2 >= 2/6).

## Structure (2,2,1), shape F-i: DEAD (sketch)
At apex A1 in C^alpha*: masses = alpha-row of A1 = (A2 4, t 4 | C 2, B1 2, B2 2 | z 3) (no W-ones: no twins possible;
alpha_tA1 = 4 since A1 is single-four). B1 is a single alpha*-four vertex with alpha*-four A1, so L*_A1 = L*_t at B1 and
Lemma TC gives D*_t cap D*_B1 = empty at A1. Lemma 2F3S: contradiction.

## Remaining
(2,2,1) shape F-ii (F = path A1 - x - y - z' - A2 through B1, B2, C) with its N-pairings; structures with (1,3)/(3,1)
vertices; t-row cases. Also re-check S1 (notes v3) with 2F3S where possible.
