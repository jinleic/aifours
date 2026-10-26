# A written endpoint parametrization of every projective Hamilton row

Observed `/bin/date` before creation: **Sun Oct 25 04:13:05 PDT 2026**. Owner `InfoRecursiveMDS18`, slot info-4. Status **WRITTEN / CANDIDATE / PARTIAL FOR UNRESTRICTED TUSCAN-2(11)**. This argument was developed after the parent withdrew the eval-kernel admission exception. **No scientific interpreter, enumeration, symbolic calculation, certificate replay or solver was launched for this note.** The displayed modular arithmetic is part of the written proof, not a machine-check claim.

Mandatory authority qualification: [kernel-admission-correction-addendum-v1.md](kernel-admission-correction-addendum-v1.md). Earlier enumerations remain preserved, unadmitted scientific computations under the parent's withdrawn permission. They are not premises of this proof.

## 1. Claim and elementary imports

Let Omega be the projective line F11 union {infinity}. A projective transformation is the action of an invertible two-by-two matrix, modulo nonzero scalar, on Omega. Cut a transformation that is one Hamilton 12-cycle at infinity, giving its eleven successive finite values as a row.

We prove in writing, without enumerating transformations:

1. There are exactly **two** such rows for each ordered pair of distinct finite starting/ending symbols (s,e).
2. Thus there are exactly **220** such rows in total.
3. A hypothetical eleven-row square entirely in this family is specified by a derangement of its endpoints and one of two exact rational recurrences for each row.

Imports are elementary linear algebra over a field: eigenvalues in a splitting field, Cayley-Hamilton, and the fact that a nonidentity projective transformation fixes at most two points. No PGL conjugacy classification or design-existence theorem is needed.

## 2. The eigenvalue-ratio condition

Let M represent a Hamilton 12-cycle T. The action of projective matrices on the projective line is faithful, since fixing three distinct points forces a scalar matrix. Hence the projective order of M is exactly twelve.

M cannot have repeated eigenvalues. If it did, either it would be scalar, or, after scaling over a splitting field, it would be I+N with N nonzero and N^2=0. In characteristic eleven, (I+N)^11=I, giving order eleven, not twelve.

Let alpha,beta be its distinct nonzero eigenvalues and put rho=alpha/beta. The projective order is the multiplicative order of rho, so rho has order twelve. Since rho^6=-1 and rho^2!=-1, the factorization

`x^6+1=(x^2+1)(x^4-x^2+1)`

implies

`rho^4-rho^2+1=0`, and therefore `rho^2+rho^(-2)=1`.

Writing

`lambda=(tr M)^2/det M=2+rho+rho^(-1)`

gives

`(lambda-2)^2=3`.

In F11 the two square roots of 3 are 5 and -5. Consequently

`lambda in {7,8}`.

Conversely, suppose an invertible matrix has lambda in {7,8}, has distinct eigenvalues, and has no eigenline defined over F11. Its eigenvalue ratio satisfies rho^4-rho^2+1=0. This gives rho^6=-1 and rho^12=1. It cannot have order dividing six. It cannot have order four, since substituting rho^2=-1 gives 3=0, false in characteristic eleven. Therefore it has order twelve.

For 1<=k<12 the eigenvalues of M^k remain distinct, because rho^k!=1, and its eigenlines are the same two non-rational lines. Thus T^k fixes no point of Omega. Every orbit has length twelve, so on the twelve-point projective line T is one Hamilton cycle.

## 3. Exact endpoint formula

A Hamilton transformation does not fix infinity, so normalize its lower-left matrix entry to 1. If its row starts at s and ends at e, then

`T(infinity)=s` and `T(e)=infinity`.

Hence it has the form

`T(x)=s+k/(x-e)`

for a nonzero k. Its matrix may be written

`M=[[s, k-s*e],[1,-e]]`.

Then

`tr M=s-e`, `det M=-k`, and `lambda=-(s-e)^2/k`.

The start and end cannot agree: s=e would put infinity in the two-cycle infinity->s->infinity. Thus s!=e. The only possible choices are

`k=-(s-e)^2/7` or `k=-(s-e)^2/8`.  (E)

Both choices really are Hamilton. The discriminant of M is

`Delta=(s-e)^2+4k=(s-e)^2*(1-4/lambda)`.

For lambda=7 the last factor is 2; for lambda=8 it is 6. Both are nonsquares in F11: their fifth powers equal -1. In particular the discriminant is nonzero, and the two eigenlines are not defined over F11. Section2 now proves the Hamilton property.

This proves **exactly two transformations for every s!=e**, not merely an upper bound. Distinct transformations give distinct cut rows because a row determines the full successor permutation after adjoining infinity. Therefore the exact number is

`11*10*2=220`.

This census has a written proof independent of the earlier 1,320-transformation enumeration.

## 4. First/last-two-symbol relations

Let t be the second symbol and u the penultimate symbol. Substituting x=s and solving T(u)=e give

`t=s-(s-e)/lambda`,

`u=e+(s-e)/lambda`.

Thus the two cases are:

|lambda|second symbol t|penultimate symbol u|
|---|---|---|
|7|4s+8e|8s+4e|
|8|5s+7e|7s+5e|

All expressions are in F11. In either case

`t+u=s+e`.

The normalized row starting (0,1) has 1=e/lambda, hence e=lambda. Its matrix is `(0,3,1,3)` when lambda=8 and `(0,4,1,4)` when lambda=7, recovering the two representatives without a ten-case orbit-length computation.

## 5. Endpoint-permutation representation of the whole family problem

In any actual Tuscan-1 square, each symbol starts exactly one row and ends exactly one row. Index rows by their starts. The map E sending s to the end e of its row is therefore a permutation, and E(s)!=s.

If every row is projective, the complete array is determined by:

- a derangement E of F11;
- a choice lambda_s in {7,8} for each s;
- the recurrence `T_s(x)=s-(s-E(s))^2/(lambda_s*(x-E(s)))`.

The row starting s is obtained by successive applications to infinity, omitting the final return. Conversely, each of these choices gives eleven actual row permutations; their pair coverage/noncollision must still be checked. This is an exact representation of the projective-family completion problem, not a sufficient condition for Tuscan-2.

No Latin-column property is imposed. The two endpoint choices constrain the second and penultimate symbols, but do not make either of those columns a permutation. In particular, the relations above must not be substituted for unrestricted defect identities outside this projective family.

## 6. What this adds, and what remains

The 220-row census, two affine-normalized representatives, and an explicit two-choice-per-endpoint parametrization now have a self-contained written derivation. They no longer require accepting the unadmitted enumeration as evidence for these particular facts. This does **not** retroactively admit that enumeration or the color-certificate replay.

The earlier projective coloring still requires a permissible complete written reconstruction or other parent-approved verification; this note does not silently certify its 32/34 neighborhoods or proper colorings. The general rainbow-insertion obstruction remains a different written result.

Most importantly, an unrestricted Tuscan-2(11) need not have any projective row after the first row's arbitrary global normalization. There is no claim that this representation covers all row permutations. **No unrestricted eleven-by-eleven witness or all-family impossibility proof is supplied.** The correct constructive frontier remains a genuinely nonregular/nonprojective row mechanism, or an unrestricted argument that does not impose these family restrictions.
