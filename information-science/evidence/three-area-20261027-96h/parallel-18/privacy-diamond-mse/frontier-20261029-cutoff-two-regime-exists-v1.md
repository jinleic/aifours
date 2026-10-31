# The cutoff-2 regime exists: a certified explicit interval

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 20:12:00 PDT 2026`.

**AUTHOR-WRITTEN, UNREVIEWED.** This answers Main's open-surface item (b) — whether `1/2<V<=2` occurs at all — in the affirmative, at all-variable scope: no selected ε, no numeric instance; the only constants are exact rationals and symbolic endpoints. Items (a) (corner/kink normal-cone envelope) and (c) (scalar-pair uniqueness) are NOT addressed and remain open.

## 0. Statement

Let b=e^(-ε), D the full closed l1 unit ball, F_b the all-Borel every-shift class, V=inf J. Let m_L be the unique positive root of

    p(m)=16m³+16m²-1,

and write the value bounds

    V >= L(m),  L(m)=(m+8m²+8m³)/(1+2m),  m=b/(1-b);      V <= 4/ε².   (1)

**Theorem.** For every ε with

    √2 <= ε <= log(123/23),                                              (2)

one has `1/2 < V <= 2`. Hence `ceil(sqrt(2V))=2`: the f261 finite-prefix problem is exactly the N=2 problem on the whole interval (2), and the f273-adopted reduction `V=min_(a>=0,c>=a+1/2) rho(a,c)` applies verbatim there. The interval (2) is nonempty. This is the first certified non-one-core-triggering region: on it no one-core trial can certify V<=1/2 is irrelevant — the certified V>1/2 shows the N=1 theorem's hypothesis fails, so the optimum is governed only by the two-scalar problem (whether its minimizer lies on the diagonal c=a+1 or in the interior remains open).

## 1. The two bounds, both at all-variable scope

**Upper bound.** The product-Laplace law `(ε²/4)e^(-ε||x||_1)` is feasible for every shift by the triangle inequality and has cost exactly 4/ε²; this is the f261-adopted witness. For ε>=√2, `4/ε²<=2`.

**Lower bound (re-derived; ancestry: the f245 disposition used it for m>=2).** Project any feasible law to one coordinate X; the marginal inherits `P(A)<=b^(-1)P(A+h)` for every interval shift |h|<=1, by pulling back Borel sets. For A=(-1/2,1/2), the integer translates A+k are pairwise disjoint and privacy gives `P(X∈A+k)>=b^|k| P(X∈A)`; summing,

    P(X∈A) <= (1-b)/(1+b),  hence p(1/2):=P(|X|>=1/2) >= 2b/(1+b).

For r>0 the two disjoint half-lines give `p(r+1)>=b p(r)`. With the layer-cake identity EX²=∫₀^∞ 2r p(r) dr, integrating over [0,1/2] and the disjoint shells [k-1/2,k+1/2], k>=1:

    EX² >= [2b/(1+b)]·[1/4+2Σ_(k>=1) k b^k] = [2b/(1+b)]·[1/4+2b/(1-b)²].

Adding the two coordinates (no independence used) and converting with m=b/(1-b):

    V >= L(m)=(m+8m²+8m³)/(1+2m).                                        (3)

Every step is elementary and valid for ALL b∈(0,1).

## 2. Where L exceeds 1/2

    L(m)>1/2  ⟺  2(m+8m²+8m³) > 1+2m  ⟺  p(m)=16m³+16m²-1>0.

p(0)=-1<0, p is strictly increasing on m>0 (p'=48m²+32m>0), so p has a unique positive root m_L. Exact signs:

    p(11/50) = -863/15625 < 0,     p(23/100) = 2567/62500 > 0,

hence `11/50 < m_L < 23/100`. Since m=1/(e^ε−1) strictly decreases in ε:

    ε <= log(123/23)  ⟹  m >= 23/100  ⟹  p(m) >= p(23/100) > 0  ⟹  L(m) > 1/2  ⟹  V > 1/2.

## 3. Nonemptiness of (2), exactly

It suffices to certify `e^√2 < 123/23`. Since `(1415/1000)² = 2002225/1000000 > 2`, we have √2 < 1415/1000. For x=1415/1000, the truncated exponential series through degree 13 with the geometric remainder bound gives

    e^x <= Σ_(k<=13) x^k/k! + [x¹⁴/14!]·1/(1−x/14) < 123/23 = 5+8/23,

an exact rational comparison (all terms rational; the inequality was checked by exact Fraction arithmetic; the derivation of the remainder bound is the standard geometric majorization for x<14). Hence √2 < log(123/23) and the interval (2) is nonempty.

## 4. Conclusion and boundary

Combining: on (2), `1/2 < V <= 2`, so `1 < sqrt(2V) <= 2` and the f261 cutoff is exactly 2. This settles existence of the N=2 regime affirmatively at all-variable scope. What this does NOT do: it does not locate the minimizer of rho(a,c) (items a/c open); it does not show V>1/2 fails anywhere else; it does not touch 0<ε<... questions beyond the stated interval; no uniqueness, no closed form, no source/book or novelty claim.

## 5. Owner controls and diagnostics

Exact Fraction script `n1-extension-exact-certifications-v1.py`, SHA-256 `e55d94e7a5cb7b8f2f0a20a53aa717d8a812bc44436916346d9665f401162d02`, run log `...-run3.log`, SHA-256 `03f63c94046050029a1df3504255173ae56c42c4341bc0bac552f3d5fb1a6f73`, executed 20:06:08 PDT 2026, exit 0, printing PASS A (p signs) and PASS E (the exponential comparison of §3), among others. These are owner controls, non-evidence; the written proofs above stand alone. Two earlier runs of earlier script versions failed (assertion at Δ(737/10000); lost loop-state update after edits) with logs `93d1cac4…`/`be6a3dc5…` retained as failed diagnostics; intermediate script hashes `a844aaa0…`, `8fa7ecaa…` are superseded.

**Disclosed in-flight state:** the same script had been prepared for the previously released N=1 diamond-trial extension (rational sign certifications λ_g(743/10000)<1/2<λ_g(3/40), m0∈(742/10000,743/10000)); that manuscript was NOT completed under the newest no-numeric-instance instruction and is not claimed. A separate all-variable observation is recorded in checkpoint 018: the numerator `N(g,m)=∂_mM4·M2−M4·∂_mM2` of ∂_m J(P_g;m) has ALL 17 monomial coefficients strictly positive (g⁵:2, g⁴:5+20m, g³:4+48m+88m², g²:1+28m+156m²+192m³, g:44m²+192m³+192m⁴, const:12m²+72m³+144m⁴+96m⁵), so every J(P_g;m) is strictly increasing in m and λ_g(m)=min_g J(P_g;m) is strictly increasing; unreviewed, available for a future released extension.

## 6. Premises and noninputs

Premises: the f261-adopted Laplace witness bound; the f273-adopted item-5 reduction (cited at its exact conditional scope). The lower bound (3) is re-derived here in full and needs no disposition. Same continuing author; no held/withdrawn/ZERO body, MDA26 source text, f161/f162 or protected v214 material used; no independent-authorship claim.
