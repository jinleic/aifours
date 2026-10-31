# A local-r upper bound for a natural generalized Fact 2 target

**NEW AUTHOR WRITTEN NECESSARY CONDITION with exact finite control; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 21:01:27 PDT 2026**. This considers a SPECIFIC natural generalization of printed Fact2: replace the semilattice-by-group product with the explicit seminormal-band-by-CS physical product, while retaining an idempotent-separating homomorphic image. It does not say the print intended exactly this replacement, prove that every locally r-orthodox source embeds, or solve open-ended Q2.

## 1. Exact theorem

Let `H=P(B,D)` be the physical Rees-action product of a seminormal band B by a completely simple D, let `π:H→U` be an onto homomorphism that is injective on E(H), and let S be ANY regular subsemigroup of U. Then S is locally r-orthodox.

Consequently, under this particular generalized Fact2 target, the class of locally r-orthodox regular semigroups is an UPPER BOUND on the regular sources that can embed. It is not claimed sufficient. The earlier literal semilattice-by-group target has the much smaller inverse-semigroup boundary recorded in `frontier-20261028-literal-fact2-regular-boundary-v1.md`, SHA `a0c19e81d70be449946c0fc612b5f4ffc380457933131e1d9e47cd959cd7b3a8`.

## 2. The full physical product is regular and locally r-orthodox

Write D=M[G;I,Λ;P] and the physical product

`(b,(i,g,λ))(c,(j,h,μ))=(b α_(gP_(λ,j))(c),(i,gP_(λ,j)h,μ))`.

For x=`(b,(i,g,λ))`, choose ANY j,μ and put `p=P_(λ,j)`, `r=P_(μ,i)`, `h=p^(-1)g^(-1)r^(-1)`, `c=α_((gp)^(-1))(b)`. The resulting y=`(c,(j,h,μ))` satisfies xyx=x and yxy=y by direct Rees/group cancellation and b²=b; the action weights in the last factors are identities. Thus H is regular.

A seminormal band is locally regular: in its defining identity substitute the identity of a local corner for its third variable. Let e=`(b,d)` be an idempotent of H. The local actor dDd is a group with identity d. Every idempotent in eHe has actor d, and its band coefficient lies in bBb; conversely each c∈bBb gives an idempotent `(c,d)∈eHe`. Hence

`E(eHe) ≅ bBb` as bands,

with ordinary band multiplication because d's self-weight is the group identity. Therefore each local idempotent band is regular, and H is locally r-orthodox.

## 3. Idempotent-separating quotients retain each local idempotent band

U is regular as a homomorphic image of H. Given e∈E(U), choose an idempotent e0∈H with π(e0)=e; this standard lift can be constructed by taking a preimage x and an inverse z of x², then xzx is idempotent and maps to e.

For any f∈E(eUe), choose y∈H with π(y)=f and set x=e0 y e0. Then x lies in the regular local monoid e0He0 and π(x)=f. Taking an inverse z of x² INSIDE that local monoid gives an idempotent xzx∈e0He0 mapping to f. Thus π maps `E(e0He0)` onto `E(eUe)`. Its restriction is injective by idempotent separation, and both sides are bands, so this is a band isomorphism. In particular E(eUe) satisfies the regular-band law.

Finally, for e∈E(S), `E(eSe)⊂E(eUe)`. Products of its members remain in eSe and are idempotent because E(eUe) is a band; the regular-band identity is inherited. Every eSe is regular because S is regular. Therefore S is locally r-orthodox.

## 4. Exact finite control and nonconclusions

`frontier-20261028-generalized-fact2-upper-checker-v1.py`, SHA `70a2f4ae7ebb59bcec3f6999ae58d6baa6facaa206ed83f02600307e6efcdbe8`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 21:01:27 PDT 2026**, exit0. It constructs an8-element physical product of a2-element right-zero band by C2×C2 and its NONINJECTIVE4-element group-factor quotient. The quotient is idempotent-separating, has noncommuting idempotents and has regular local idempotent bands. It also checks the six-element band monoid from the Billhardt-scope note is regular as a semigroup but fails the local regular-band condition at its identity, and hence lies outside the stated upper bound.

Any source already embedded in a suitable seminormal-band-by-CS physical product is a trivial positive instance of this generalized target by taking π to be the identity. This does NOT prove that every locally r-orthodox regular semigroup has such an embedding or such a quotient; that sufficiency is open at this record's scope. The exact printed Q2 extension and product convention remain a separate interpretive obligation. No general Q2, formal/kernel/independent review or novelty conclusion is claimed.
