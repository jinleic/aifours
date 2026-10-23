# Checkpoint 001 (Sun7K62Successor, continuation k7-k62-residue)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:54:54-0700. Work started 2026-10-19T02:32:05-0700.
- **Status:** written work only; no computation of any kind run in this continuation; no process left running.

## Candidates sent
| file | sha256 | scope | status |
|---|---|---|---|
| `K7-U1-v1.md` | d4e6cdc9e11320bee2456e589459c2b0e961bec466e1b7c05e7ff4003e751965 | no K7 configuration with exactly one marked vertex (any m_z; new part 6 / m_z) | parent read, no gap found (IRC ~02:5x); CLI reviews parent-owned, running. Parent wording note: section 1 (b) remainder pairs use custom weights (four with weight 1 beside an isolated one; half weights on the two-element sets (4,2)/(4,4)), not the literal standard formula; to be clarified in a later erratum if reviewers ask; no theorem change. |

## Parent news received
K62-A + TG + corrected full-C-clique PARENT-ACCEPTED (`RUN/review/sun7-K62A-TG-parent-verdict-v1.md`, sha256
c792dc68884a0c99632f218fd03833f60b80b89fd2c194137331d35fb4f3fc61); use exact scopes. Directive: continue K7 with 2- and 3-markers on different vertices.

## Working notes on K7 with z (2-marker) != t (3-marker) (NOT claims; to be frozen in a candidate)
1. Centre-Z: if both rows of z (alpha, alpha*) are 4-type (entries {1,2,4}, <= one 1, >= three 4s), the K7-Z2/K7-U1
   CROSS/LIGHT/T1-T4 argument applies at z: ell_z = 2^E (5^B) w_z has no factor 3, so x = 3 dies by tau_min = 12;
   x = 5 dies as in Z2; all neighbour cofactors of z are odd, so LIGHT's gcd reduction holds. Needs a written transfer.
2. Row dichotomy at z (p absent/on z/on t: ROW-1 at z via the accepted G2 transfer; k5 = 5 killed by inversion):
   each z-row is 4-type or 3-type (k3 >= 3 unmarked threes, other unmarked in {1,2}, alpha_zt in {1,2}).
3. Mixed rows killed: alpha-row 3-type with alpha*-row 4-type forces |T_z| = 3, F*_z = (W \ T_z) + t; inverted CROSS
   table + triangle {z,a,v} (alpha_av in {3,4}) force alpha*_za = 2 and X*_a subset X*_v; inverted VFC at z then
   puts D*_a (1/2) and D*_v1, D*_v2 (disjoint, coprime local indices) inside Y*_a (2/3): contradiction.
4. Open residue of this route: both z-rows 3-type (and, when the 5-marker is a third vertex, the k3 = 3 sub-case of
   item 3 and the k3 = 2 rows of ROW-2 at z).
