# Deletion obstruction addendum v1 — D12 excluded, Dic3 sharpened

Clock observed before creation: **2026-10-23T14:35:57-0700**. Read with immutable `deletion-obstruction-candidate-v1.md`, SHA-256 `a7ce2e0dd4bb7ddd6b3a0c573496e0340f58a44c3cc4f654b4863ad7edb041b7`. This is an additive sharpening, not an edit or withdrawal of the original proof. Status **CANDIDATE / WRITTEN ONLY / PARTIAL / NOVELTY_UNCLEAR**. No executable arithmetic or enumeration occurred.

## 1. Shared exact normalized setting

Use the source manuscript's group-developed Tuscan-2 square and delete the first symbol of the identity-indexed starter row, normalized to

`a_0=1`, `a_(m−2)=u=v²`, `a_(m−1)=v`, `ord(v)>2`.

Its distinct adjacent right quotients are `d_i=a_i^(−1)a_(i+1)`, `0≤i≤m−2`, enumerating `G\{1}`. The last quotient is

`d_(m−2)=(v²)^(−1)v=v^(−1)`.

The exact necessary adjacent-pair matching from Lemma4 is

`{(d_i^(−1),d_(i+1)):0≤i≤m−3}`

`= {(a_j,a_(j+1)):1≤j≤m−2}`.  (E)

All these are actual ordered pairs of group elements, not merely equalities of quotient sets.

## 2. Endpoint order3 is impossible

**Lemma A.** In this setting `ord(v)≠3`.

*Proof.* The retained starter path contains the adjacent pair `(u,v)=(v²,v)`. Therefore (E) supplies an index `0≤i≤m−3` such that

`d_i^(−1)=v²`, `d_(i+1)=v`.

Thus `d_i=v^(−2)`. If v has order3, `v^(−2)=v`, so two consecutive adjacent quotients are both v. This contradicts that all d_i are distinct. The matching index really is before the last quotient: it is supplied by (E); alternatively, `v^(−2)≠v^(−1)` for every v≠1. ∎

Combined with Lemma4, a possible endpoint has order at least4. This is not a statement about all Tuscan-2 squares; it is a condition on this exact deletion construction.

**Corollary B (D12 source class excluded).** No one-row/one-symbol deletion of ANY D12-developed Tuscan-2 square yields even a Tuscan-1 square of order11.

*Proof.* The original Theorem3 excludes interior deletion. Its abelianization calculation for `D12=<r,s | r^6=s²=1, srs=r^(−1)>` puts the normalized endpoint in `<r²>`. The endpoint cannot be1 or an involution, so it must be r² or r⁴, both of order3. LemmaA excludes both. Reversal accounts for deletion of the other endpoint. ∎

Thus the original residual D12 route is now closed **as a construction family**, not by a failed search and not by unrestricted Tuscan11 nonexistence. The original two-group scientific request is on HOLD and must not be executed.

## 3. Further exact first-entry filters

Put `w=a_1`. The source criterion gives `d_0=w`.

**Lemma C.** `ord(w)>2`.

*Proof.* Suppose `w²=1`. The bridge for i=0 in(E) is `(w,d_1)`. The retained starter path's unique edge beginning at w is `(w,a_2)`, so `d_1=a_2`. But `d_1=w^(−1)a_2=w a_2`, forcing w=1, whereas a_0=1 and a is an ordering. ∎

**Lemma D.** `w≠v^(−2)`.

*Proof.* If `w=v^(−2)`, the unique bridge in(E) beginning at u=v² has i=0, since `d_0^(−1)=v²`. Its right endpoint must be v, so `d_1=v`. Hence `a_2=a_1d_1=v^(−1)`. The i=1 bridge in(E) then begins at `d_1^(−1)=a_2` and ends at d_2. The actual retained path's edge beginning at a_2 ends at a_3, so `d_2=a_3`. But `d_2=a_2^(−1)a_3=v a_3`, forcing v=1. Contradiction. The index i=1 is available since m≥4; in the applications m=12. ∎

A further useful quotient-set consequence is that the unique nonidentity quotient omitted by the source distance2 quotient list is w: all new bridge quotients are exactly that list, whereas the removed finite path's quotients are `d_1,...,d_(m−2)=G\{1,w}`. In particular, the consecutive pair `v^(−2),v` identified above has product `v^(−1)`, so `w≠v^(−1)` as well. This last filter is additional route evidence, not needed for D12's exclusion.

## 4. Exact residual Dic3 model

For `Dic3=<a,x | a^6=1, x²=a³, xax^(−1)=a^(−1)>`, the original abelianization argument forces

`v∈{a,a⁵}`, `u=v²`.

Of the six rotation-subgroup elements,1 and v and v² cannot be w because the starter is an ordering; a³ is excluded by LemmaC; `v^(−2)` is excluded by LemmaD; and `v^(−1)` is excluded by the distance2 quotient consequence. These are all six rotations: when v=a they are `1,a,a²,a³,a⁴,a⁵`, and similarly when v=a⁵. Therefore

**w must be one of the six elements `a^r x`, `0≤r≤5`, all of order4.**

This is the only group-source deletion model proposed for the successor assay: enumerate all starters of Dic3 with first1, first nonidentity entry outside `<a>`, endpoint a or a⁵, penultimate endpoint², distinct adjacent quotients and distinct distance2 quotients. Check the full12×12 developed source and resulting literal11×11 array directly. No random starter, group-isomorphism quotient, unproved row/column symmetry, target Latin-column assumption or omitted distance2 condition is allowed.

None of these filters ensures that a starter or target exists. Conversely failure of this model still does not settle unrestricted T2(11). Any scientific program implementing it remains unexecuted until an exact successor parent GO. Parent and actual separate written reconstruction of this addendum are pending; no WRITTEN_CHECKED or novelty label is inferred from the author's algebra.
