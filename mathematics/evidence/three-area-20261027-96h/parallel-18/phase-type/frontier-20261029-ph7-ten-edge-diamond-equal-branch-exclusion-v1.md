# Equal diamond branch escape rates are impossible for the critical support

Status: **WRITTEN-checked in the owner's SymPy kernel**, pending independent mathematical review and parent disposition. This is an exact all-rate exclusion of a codimension-one slice of the still-open ten-edge graph/support in `frontier-20261029-ph7-ten-edge-diamond-support-factorization-v1.md` (SHA256 `d6a4ec797a1be76ab2afe0e0d67d0d72bf9694dedabb4e31cee4f151f4a56c8f`). It does not exclude unequal branch rates, other supports, or PH7 at `8/9`.

## 1. Statement

For the ten-edge graph specified in that source, let input be supported at vertex 1 and exit on vertices `{4,5}`, with the target transfer of relative degree five and `z>1/2`. Its edge rates are `e_0,...,e_9>0` in the same order as the source. Then necessarily

`e_5 != e_8+e_9`,

so the diagonal escape rates of the two diamond branch vertices 3 and 6 cannot be equal. This conclusion applies in particular at `z=8/9`.

The proof imports the standalone **six-state Metzler spectral lemma** from §4 of `frontier-20261028-ph7-global-irreducibility-v1.md` (SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`), previously independently reconstructed in parent review f61. It is not a new unrestricted PH6 theorem.

## 2. Equal branch rates force a second rate equality

Assume `e_5=e_8+e_9=:t>0`. The topology-fixed hidden decay rate in `frontier-20261029-ph7-ten-edge-diamond-hidden-root-v1.md` (SHA256 `6553f0ddb1dadcbcb30f52d8ddabd353df43b664034ebe8e331051f46e52195d`) then equals `t`, so the actual seven-state characteristic polynomial `P(y)=det(yI-G)` must satisfy `P(-t)=0`. Direct determinant expansion gives the exact identity

`P(-t) = -e_1*e_4*t*e_6*e_7*e_8*(e_3-t)`

under `e_5=t=e_8+e_9`. Every factor outside the last is strictly positive, hence `e_3=t`. This is a spectral divisibility requirement from the same actual numerator, not a selected optimizer result.

## 3. A positive six-state quotient

When `e_3=e_5=e_8+e_9=t`, define the full-rank nonnegative `6 x 7` matrix `W` whose first five rows are the coordinate row vectors of states `0,2,4,5,6` and whose last row is `e_0*e_1^T+e_1*e_3^T`, where `e_i^T` here denotes the coordinate row vector of state `i` (not the similarly named edge rate). Set

`H = [[-e0-e1-e2, 0, 0, 0, e2, 1],
      [e4, -e4, 0, 0, 0, 0],
      [0, 0, -e6, e6, 0, 0],
      [0, 0, 0, -e7, e7, 0],
      [0, e8, e9, 0, -t, 0],
      [0, e0*t, e1*t, 0, 0, -t]]`.

Here the last two diagonal row sums use `e8+e9=t`. Direct multiplication gives

`W*G=H*W`, and `H*(W*1)=0` with `W*1=(1,1,1,1,1,e0+e1)^T>0`.

All off-diagonal entries of `H` are nonnegative, so the positive diagonal similarity defined by `W*1` makes `H` a row-conservative Metzler generator. Its spectrum is therefore in the closed left half-plane and contains zero. The kernel of `W` is one-dimensional and spanned by `-e1*e_1+e0*e_3` (coordinate column vectors). The intertwining and `Gv=-t*v` imply the exact characteristic factorization

`det(yI-G)=(y+t)*det(yI-H)`.

This factorization, the intertwining, and `H*(W*1)=0` were checked as symbolic identities in the owner's SymPy kernel. The displayed matrices and one-dimensional kernel permit independent written verification; no formal proof-assistant or independent scientific review is claimed.

Because the target's `-1 +/- i sqrt(z)` pair is nonreal, division by the real factor `y+t` preserves its full double multiplicity in `H`. The sixth remaining eigenvalue is real and nonpositive, since `H` is real and has spectral bound zero. After rescaling `d`, its six-state spectrum is exactly the forbidden `0,-u,-1 +/- i sqrt(z)` (the pair twice) with `u>=0`, `z>1/2`. The imported six-state spectral lemma gives a contradiction. □

The condition is only necessary for the specifically named graph and support. Unequal branch rates, different input/exit supports, graphs with two-cycles, all ten-or-more-transition families, actual PH7 existence/exclusion, novelty, and parent adoption remain open.
