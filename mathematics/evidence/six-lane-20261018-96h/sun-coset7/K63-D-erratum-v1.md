# K63-D-erratum-v1: repair of one compatibility clause in K63-D-v1 section 2 (b4) (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:07:41-0700.
- **Overlays:** `K63-D-v1.md`, sha256 f4027779f19a4733614f543d56a4cf596af9383f04510fbc725a5a7a3ebed255 (frozen, unchanged).
- **Source of the finding:** parent full read (IRC at about 01:35 PDT); not yet a CLI review.

## H1: section 2 (b4), branches (1,2,0) and (0,3,0), last sub-case

Replace "If alpha_pt is odd and t is compatible with i* (3 | alpha_pi*)" by: **"If alpha_pt is odd and t is compatible
with i* (gcd(lambda_t, lambda_i*) >= 2, which for odd alpha_pt happens exactly when 3 | alpha_pi* or alpha_pt =
alpha_pi* = 5)"**. The weights are unchanged: y_t = y_i* = 1/2. Feasibility: {two, i*} has sum 1 (lambda_i* is even);
{i*, t} has sum 1; {two, i*, t} is not allowed because gcd(lambda_two, lambda_t) = 1 (t's label 3^F w_t alpha_pt is odd).
Value: 3 + (alpha_pi* + alpha_pt)/2 >= 3 + (3 + 1)/2 = 5 in the 3-case and 3 + (5 + 5)/2 = 8 in the 5-case; both >= 4.
Nothing else in K63-D changes.
