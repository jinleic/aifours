# Physics-2 checkpoint059 - outside-F slice: exact Weyl-sparse system frozen; U-invariant case derived

Actual `/bin/date` before this write: 2026-10-19T21:42:14-0700. Previous checkpoint058 21:27:03 (15m11s).
Next target 22:02:14, binding 22:12:14. No execution, import, test, enumeration or numerical/symbolic script.

## Frozen
continuations/outside-F-flatplanes/01-weyl-sparse-system-v1.md
SHA-256 6be70323c501401f6e9687215844e28de4ac19c1f7b38211d15cfe9e1711b09a: flat planes <-> Hermitian idempotents
P = (1/5) sum y_z W_z whose Weyl coefficients vanish on the three forbidden lines; explicit system of 6 forbidden + 6
allowed complex quadratic equations + trace in (alpha_k, beta_k), k = 1,2,3 (coefficient table -phi / 1/phi);
support lemma: one nonzero allowed line <=> the 30 MUB-pair planes, two nonzero lines impossible. Known slip to be
recorded in an erratum file (no result change): the distinctness sentence for the 30 MUB-pair planes should argue via
diagonals (a MUB-pair plane of B_k has constant diagonal 2/5 in B_k', k' != k), not via non-orthogonality.

## Derived in working form (being written as note 02)
U W_z U^* = W_(Mz) with M(a,c) = (c, -a-c) (no phase); U-invariant flat planes reduce to (a, b) in C^2; exact solution:
Re a = Re b = -1/(2phi), (Im a)^2 + (Im b)^2 = phi/2, (Im b)^2 - (Im a)^2 = 4 phi^2 (Im a)(Im b): EXACTLY FOUR, of any
eigen-type (the other branch Re a + Re b = 3/(2phi) is excluded by 28phi + 16 != 0). Parent message (21:4x): E1
Proposition 9 accepted at literal scope (RUN/review/rqls10-E1-nonMUB-parent-verdict-v1.md ad790caa...e872); citing it,
the four are exactly P_tau, and their 100 WH translates are distinct (count proved in y-coordinates).

Next: note 02; then Pi-type, antiunitary-involution and full-group stabiliser cases; then Q3 or exact GAP.
Global runtime HOLD unchanged; full W8 and 1-RQLS(10) OPEN / UNKNOWN.
