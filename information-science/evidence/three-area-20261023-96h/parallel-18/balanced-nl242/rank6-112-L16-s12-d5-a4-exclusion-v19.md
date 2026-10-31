# Balanced NL242 (3,112), L=16, s=12, d=5: distinct-inactivity (a4) excluded

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:10:44-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This excludes the remaining distinct-inactivity (a4) variant, conditional on the source-separated v205 author chain through v16. Together with v11/v12/v17/v18, it is an author-only exclusion of s=12,d=5 at L=16, not an exclusion of L=16, a residue type, or the original problem. No independent review, formal/kernel check, novelty or witness is claimed. The proof is exact all-variable hand reasoning; no scientific program or selected numerical probe was used.

## 1. Two shifted support conditions

In distinct-inactivity (a4), p,p′ are the two outside balanced cosets and δ=p+p′∈W\{0}. In each single-carrier slice, its inside active set is Σ and its m is 24 (v12); v14 gives negative slice-sign product. By v15/v16, Σ is six r-pairs whose quotient labels form a six-point affine circuit in Q=W/⟨r⟩, and in each slice its six pair products split into two groups of three.

Let A₁,A₂ be the sets of six nonzero differences of same-group quotient labels in the first and second splits. The 15 pairwise differences are all distinct and exhaust Q\{0}. For either slice, v15's autocorrelation identity and the circuit property show that its class transform F(v) is nonzero exactly when v mod ⟨r⟩ belongs to the corresponding A: at such v, exactly two pairs overlap and their equal pair products make |C(v)|=4; r itself gives C(r)=0. Thus the support is invariant under v↦v+r and has both lifts of each element of A.

In the slice where p is the single active carrier, the inactive p′ row gives F₁(δ)=0, as derived in v15; similarly F₂(δ)=0 when p′ is the single active carrier. Put d=δ mod ⟨r⟩. Hence d∉A₁∪A₂ (also true when d=0).

Every outside coset other than p,p′ is pure and has k=2 by v12, so at most one of the three slices is nonzero. Since the second carrier is p′, not p, this gives the **shifted** necessary condition

    A₁ ∩ (d+A₂) = ∅.                                             (1)

Indeed, any e in the intersection has a lift v with F₁(v)≠0 and F₂(v+δ)≠0; its coset p+v is pure because e≠0,d. The two single-carrier formulas would make both slice values nonzero there.

## 2. Contradiction in the quotient

If d=0, two 3+3 splits of six labels have a same-group pair in common: take any triple in the first split; two of its labels must also share a group in the second. Their difference is in A₁∩A₂, contrary to (1).

Now let d≠0. By the circuit property, d is the difference of a unique pair of labels, say i,j. Because d belongs to neither A₁ nor A₂, i and j lie in different groups in both splits. Orient each split so i is on the first side and j on the second.

For each of the other four labels k, exactly one of the edges {i,k},{j,k} is same-group in each split. Adding d interchanges their differences:

    d+(i+k)=j+k.

If k changes side between the splits, the difference of its same-group edge in split 1 lies in A₁ and also in d+A₂. Hence (1) forces every k to have the same side in both splits; the two splits coincide.

Each side then consists of i or j and two of the other four labels. Call those two pairs {a,b} and {c,e}. The sum of all six quotient labels is zero, so

    d+(a+b)=c+e.

Both {a,b} and {c,e} are same-group edges in the common split. Thus a+b∈A₁∩(d+A₂), again contrary to (1). ∎

## Exact status

Conditional on all preceding unreviewed candidates, **distinct-inactivity (a4) is excluded**. With the earlier author-only exclusions of (a1), (b), (c), equal-inactivity (a4), (a2), (a3), and d=4/6, the author chain claims that s=12 at (3,112), L=16 is excluded. The remaining L=16 cases s=15 and s=16 are OPEN. No whole residue type, witness, unrestricted exclusion, (24,24,2) closure, review acceptance, kernel/formal status or novelty follows.

Dependencies: `rank6-112-L16-s12-d5-variants-v12.md` SHA-256 `7aac4fe052ed17aea9b3b41ce4354115f6f17edface0be1ac93bdff720890b7f`, 55 LF; `rank6-112-L16-s12-d5-m24-sign-sublemma-v14.md` SHA-256 `7b5425d179cec99b8690dae641cf4e009c65722d2c49fd1eebe30003a1ca0fd7`, 62 LF; `rank6-112-L16-s12-d5-antipodal-pairs-sublemma-v15.md` SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`, 49 LF; `rank6-112-L16-s12-d5-pair-circuit-and-a2-sublemma-v16.md` SHA-256 `664f9ef3d9237c0862ca493f16b0b54550e188d29d6fcc29072047dfd4ffbfab`, 47 LF; and the stated v205 admitted cuts. Earlier errata, pre-pin corrections, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and all HELD/ZERO/NONINPUT restrictions remain binding. Novelty UNCLEARED.
