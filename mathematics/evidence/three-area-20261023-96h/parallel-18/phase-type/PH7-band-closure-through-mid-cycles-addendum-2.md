# Addendum 2: z_star and z_new both lie below 4/5

The actual `/bin/date` returned before this addendum was **Sun Oct 25 23:05:41 PDT 2026**. Owner: MathResearch96h-2. This addendum adds a family-membership statement; the base file and Addendum 1 are unchanged. Everything here is exact written comparison of displayed matrices. No machine was used.

## 1. Which constructions belong to the family

Both packets below build their matrix from the same blocks: J_u (diagonal −u, superdiagonal 1), a middle state with diagonal −w, and J_1. So their holdings are exactly (u,u,u,w,1,1,1).

| Packet | SHA256 | Value of u | Endpoint |
|---|---|---|---|
| `PH7-u-deformation-actual-family-v1.md` (lines 72–80, read now) | `9f9b048bd4113b5008bdebf56f1e5d903e06e0b6ffe1f8eed78dbcd7ebb1a01e` | u0, with 1 < u0 < 3/2 (its §4–5) | z_new |
| `PH7-rational-uniform-band-seven-ninths-v1.md` (§2) | `ef6df980b2fbb5545a42ed7f3c72f17cea6f26f7148065670c104838f9a0c0f7` | u = 29/20 | z_star |

In both packets the only back edges are:

- D1, D2, D3: from states 5, 6, 7 back to state 1. These close the cycles [1..5], [1..6] and [1..7].
- φ: from state 7 back to state 4. This closes the cycle [4..7].

Every one of these cycles contains the middle state 4. Also u > 1 in both, so delta = u − 1 > 0.

The u-deformation packet says that at u = 3/2 its formulas reduce to "Chart II" of the older `proof-seven-state-nonuniform-dominator-band-v1.md` (SHA256 `4e490052336693f7f65b1978820aafa600636c421f91a217015d05aeb4928a05`). The other charts of that older packet were NOT re-read here, so they are not claimed to be members.

## 2. Consequence

Addendum 1 shows the following for every z ≥ 4/5 and every u ≥ 1, even after adding arbitrary back edges that close cycles through state 4: the holding pattern (u,u,u,w,1,1,1) does not realize the PH7 spectrum. The two families above are members of that set, so:

    z_new < 4/5   and   z_star < 4/5.

This bounds the union max(z_new, z_star) by 4/5. It does NOT say which of z_new and z_star is larger. To go past 4/5, a construction has to leave the band mechanism: it needs u < 1, holdings that differ within a block, a cycle that avoids state 4, or a different topology.

## 3. Limits

This is still a restricted-family result, and it rests on the written proofs of the base file and Addendum 1. The unrestricted question at 8/9 is still open: the minimum there is in {7,8}.

No machine check, formal proof, review or novelty claim is made. HOLD, root, cutoff and deadline are unchanged.
