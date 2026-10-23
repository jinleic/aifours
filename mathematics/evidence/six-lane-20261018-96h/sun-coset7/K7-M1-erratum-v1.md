# K7-M1-erratum-v1: wording/import overlay on K7-M1-v1 (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T00:32:43-0700.
- **Overlays:** `K7-M1-v1.md`, sha256 6e9b2d09aa5c55698dd96d95266243701ca077c98ec615aa57b648ebf3f95d63 (frozen, unchanged).
- **Responds to:** Claude review `RUN/review/sun7-m1-claude-v1.prompt.note.md` (sha256 98f9fac0fb13964d0bcf55eae9cb226b806cd795c676a975d3362b738be6b4af; ACCEPT-WITH-FIXES,
  0 FATAL/0 MAJOR/8 MINOR) and Codex review `RUN/review/sun7-m1-codex-v1.prompt.stdout.txt` (sha256 ccdf820ed6f2b2eebe509017763a94a102d39485de70ebe584641b3ac51c658c;
  ACCEPT-WITH-FIXES, 0/0/1 MINOR). RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Status:** overlay only; Lemma ROW-1 and Theorem K7-M1 are unchanged in statement and scope.

## F1 (Claude 1): imports

Add to the import list: **R0** (README section 1; used in the statement of Theorem K7-M1), **LFC (a)** (label formula
lambda_j = n_j alpha_vj / g_vj) and **LFC (c)** (the hereditary allowed-set condition), and erratum **E2** (Sun(2)) and
**E6** (the inverted configuration has the same labelled index tuple, hence the same class and the same marked vertex
with the same markers) of `K7-LFC-INV-erratum-v1.md`.

## F2 (Claude 2, Codex): the marker product of z

Replace in section 1 "m_z = 3^a 5^b with a, b in {0,1} after capping" by: "**m_z = 3^A 5^B with A, B >= 0 and A + B > 0**
(the actual exponents, unbounded; e_z = 1). The indices and labels use the actual m_z. Every alpha is <= 5, so a label
gcd involving lambda_z = m_z w_z alpha_vz depends on m_z only through the two indicators [3 | m_z] and [5 | m_z]; only in
such gcd calculations may a positive exponent be replaced by 1." Nothing else about m_z enters the proof.

## F3 (Claude 3): what ROW-1 (c) uses

ROW-U's *statement* assumes all six neighbours unmarked, which fails at v in W (z is marked). ROW-1 (c) uses ROW-U's
*proof*, which needs only the abstract hypothesis **ROW-U-deg**: "g_vj = 6 for every neighbour, every alpha_vj <= 5,
and every gcd of two neighbour labels equals the gcd of the corresponding alphas". Under ROW-U-deg the class split,
the allowed sets inside each class, the standard weights and the value bound min(N, 4) (erratum E8) are verbatim the
same, so conclusions (i)-(iii) hold. This is the same transfer the parent verdict (sha256 8621e744...ca18, item 3)
checked for ROW-U (the gcd reduction is independent of whether v is marked). ROW-1 (c) verifies ROW-U-deg: the five
other entries are powers of 2 and m_z w_z is odd, so gcd(lambda_z, lambda_u) = gcd(alpha_vz, alpha_vu).

## F4 (Claude 4): garbled weight

In ROW-1 (b), first case, read "(y = 1/k3 = 1/min(3, k3))".

## F5 (Claude 5): feasibility sentence in ROW-1 (b), last case

Replace "with twos (label 2) the only pairs have gcd <= 2 and with 3-elements the gcd is 3" by "with a two (label
2 w_u) the gcd is at most 2, and with a three (label 3 w_u) the gcd is **at most 3, equal to 3 iff 3 | m_z alpha_vz**".
The list of sets containing z ({z}, {z, x}, {z, 3, 3}) is therefore a superset of the true allowed sets containing z,
so the stated weights remain feasible; the value 5 + alpha_vz / 3 >= 6 is unchanged.

## F6 (Claude 6): step (3) of the theorem

Replace "Steps (1)-(3) apply verbatim to the inverted configuration (same z, same markers), giving |A4*(v)| >= 3 for
all v" by: "Steps (0)-(2), and ROW-1 (c) as in step (3), applied to the inverted configuration (alpha-matrix alpha*;
inverting twice returns the original configuration by INV (a), so the inverted configuration's F, F* are our F*, F)
give |A4*(v)| >= 3 for every v in W, and step (0) gives |A4*(z)| = |F*| = 3."

## F7 (Claude 7): notation

Rename the vertex set U := V \ {z} of K7-M1 to **W** throughout (and U3 to W3), to avoid collision with the subgroups U_v.

## F8 (Claude 8): exploratory parenthesis in section 4

Replace the parenthesis by: "(Exploratory probes, never premises, observed **in the probed range of capped profile
tuples** that LFC + INV alone left no joint (alpha, alpha*) solution for K7 with markers 3 and 5 on two different vertices,
and that every probed configuration with a 2-marker survived LFC + INV + T + Ppair and was removed after adding RPLP
evaluated at the true q = alpha*; these are observations of a bounded search, not claims.)"

## Non-defect remarks recorded

Claude notes that step (0)'s sentence "for u in F*, alpha_zu in {1,2}" is not used, that step (2) needs only |F| >= 3,
and that INV is load-bearing only in steps (1) and (3). Accepted as remarks; no change.
