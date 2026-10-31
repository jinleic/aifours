# Addendum: the complex-hidden formal spectrum passes shifted Newton tests

Status: **WRITTEN-checked-in-kernel with exact rational arithmetic**, not a matrix realization or PH witness. This is an immutable addendum to `frontier-20261029-ph7-complex-hidden-moment-limit-v1.md` (SHA256 `52e935bf28b522ecd4526088296edb69dfb81aca84d0c94af4be3075a2922393`).

For the formal characteristic polynomial

`P(y)=y*((y+1)^2+8/9)^2*((y+11/4)^2+3/4)`,

all coefficients of `P(y+2)` are strictly positive. In ascending powers of `y` they are

`2954533/648`, `12533069/1296`, `708451/81`, `2839571/648`, `94643/72`, `33997/144`, `47/2`, `1`.

Normalize each coefficient by the corresponding binomial coefficient `binom(7,k)`. The six consecutive normalized Newton differences `b_k^2-b_(k-1)*b_(k+1)`, in ascending order `k=1,...,6`, are exactly

`2369679398491/246903552`, `920950956049/1851776640`, `17172104881/514382400`, `1009585811/342921600`, `14085629/45722880`, `593/21168`,

all strictly positive. These exact values were checked by rational polynomial expansion in the owner's SymPy kernel.

Consequently this formal complex-hidden spectrum passes both the centered trace-two/three necessary tests in the parent and the six ordinary shifted coefficient Newton tests at shift 2. This remains only a **method-limit example**: it does not assert that any Metzler generator has diagonal escape rates bounded by 2, that the full nonnegative inverse spectral problem or all higher JLL tests pass, that Jordan/PH input-output conditions hold, or that an actual PH7 realization exists. No uniqueness, novelty, disjoint scientific review, formal proof or parent adoption is claimed.
