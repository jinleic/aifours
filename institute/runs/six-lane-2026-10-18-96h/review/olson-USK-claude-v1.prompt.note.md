# Hostile written review: Theorem USK v1

This review used only the pasted text: no tools, files, code, computation or enumeration. Pins, hashes and sizes were not checked here; the parent checked them.

Abbreviations:
- **PRF**: proof-USK-v1.md
- **PKG**: review package
- **SCP / ADD**: scope and addendum 1
- **PL**: proof-LOWER-v1.md, LF40–129
- **LER**: LOWER parent erratum
- **FB**: proof-FB-v1.md, LF9–24
- **BAL**: balfull verdict, LF26–34
- **SC0**: index-one record
- **NF**: ROT-few-E v4, LF28–43
- **K3E**: K3 parent erratum

## Counts
**FATAL 0 · MAJOR 0 · MINOR 1.** The MINOR is about import routing and has no mathematical consequence. There are also three editorial notes, which are not counted.

## Overall verdict
Theorem USK (PRF LF14–18) is **mathematically correct relative to its accepted interfaces**:
- NF (NF LF37–43)
- GRX if-direction (GRX LF18–19)
- SC0 (SC0 LF9–11)
- ZSTRUCT/FB in (S′) (FB LF11–19; FB verdict LF9; BAL LF33)
- PL Secs. 2, 4–7 (K1 verdict LF5, read with LER)

I re-derived every load-bearing step below. No unaccepted load-bearing dependency remains.

## Claim-wise verdicts

### Frame (PRF LF33–78)

**(SR), LF39–40: ACCEPT.**
- Derivation: GRX LF18–19 via PL LF48–50.
- All lᵢ are odd, so δ = N−Φ and C_max = Φ+2H, with Φ = 2m.
- So n = 2p−C ranges over [2κ+2−2m, 2p−2m] ∩ [0,R].
- The target is −Σ_{i∉P}τᵢ = Σ_{i∈P}τᵢ.
- It uses the LER LF7 convention for m (PRF LF36–37).

**Lemma W, LF42–46: ACCEPT.** With R = p−1+2κ:
- R ≤ 2p−2 ⇔ 2κ ≤ p−1.
- R ≤ 2p−2κ ⇔ p ≥ 4κ−1.
- R ≤ 2p−2κ−2 ⇔ p ≥ 4κ+1.
- R ≤ 2p−2m ⇔ 2m ≤ p+1−2κ.
- So at p = 4κ+1, only m = κ+1 has window [0,R].

**IF\*(a), LF48–49: ACCEPT.** Pigeonhole on the p+1 block values gives the arc P₀, and m(P₀) = 1.

**IF\*(b), LF50–52: ACCEPT. This is the direct bound; S1(a) is not used.**
- A zero-sum of Y of length n is n letters of X^(P₀) summing to 0 = T(P₀), with n even.
- (SR) at m = 1 excludes every even n in [2κ,R], and every zero-sum has n ≤ |Y| = R.
- So every zero-sum has length ≤ 2κ−2.
- This is the K3E LF6 argument at general κ.
- It also rules out the case where every rotation is the identity: Y = (1,0)^R would contain a zero-sum of length 2κ.

**IF\*(c), LF53–56: ACCEPT relative to SC0.**
- The zero-sum-free form follows from SC0 LF9: Y′·(−σ(Y′)) is a minimal zero-sum of length ≥ p+2 = ⌊2p/2⌋+2.
- Its basis element has order equal to the coefficient sum, which is ≥ p+2, so the order is 2p.
- The coefficients on Y′ therefore sum to ≤ 2p−1.
- Every term is odd, so g = (1,γ) with γ ≠ 0, and every aᵢ is odd.

**IF\*(d), LF57–62: ACCEPT relative to ZSTRUCT/FB.** Every clause of (S′) in FB LF12–15 holds at (k′,κ′) = (p−1, κ−1):
- κ′ ≥ 2.
- 2p+2κ′−k′ = R.
- (S1) at κ′ is exactly (b).
- t ≤ κ′.
- L ≥ p+1 = 2p−k′.

Consequences:
- n₋ ≤ Σsⱼ = n₊, so n₋ ≤ t ≤ κ−1.
- sⱼ ≤ 2κ−3.
- W+n₊ ≤ 2p−1. When t = 0 this needs only SC0.

**IF\*(e),(f), LF63–66: ACCEPT.**
- E ≤ (2p−1−n₊)−(R−n₊−n₋) = p−2κ+n₋ ≤ p−κ−1.
- So every aᵢ ≤ p−κ.
- Each odd aᵢ > 1 adds at least 2 to E, so m₁ ≥ (p+κ+3)/2.

**Normalisation, LT and light-side exchange, LF67–73: ACCEPT.**
- Exchanging the sides replaces (Y, Z, g) by (−Y, −Z, −g), with identical labels, n± and sⱼ.
- The frame quantifier at LF77–78 is correct, and a frame always exists.

### Lemma D\*, LF80–87: ACCEPT
- **s-labels:** sⱼ ≤ 2κ−3 ≤ (p+κ+5)/2 ⇔ 3κ ≤ p+11, which holds.
- **a-labels:** a_max−1 ≤ E−2(r−1) ≤ m₁ ⇔ E ≤ L+r−2. This holds since E < p ≤ L+r−2.
- **Covering:** the prefix-sum covering argument is valid.
- **Equality:** B*−R = E+n₊−n₋ ≥ 0, with equality iff every |c| = 1.
- It uses neither the Setting fact nor FB-E.

### Cited PL lemmas SS, U, A, C (LF89–96): ACCEPT as re-derived (see MINOR-1)
- **SS:** follows from D\* by PL's bijection (PL LF97–98).
- **U:** the integers of one parity in [−ν₀, 2p−1−ν₀] form a complete residue system mod p. Fullness therefore forces B* ≤ 2p−2 and U ∈ [Π₀+1, 2p−1−ν₀].
- **A:** D ∈ [2Π₀+3+ν₀−2p, 4p−3−2ν₀−Π₀] and D ≡ 0 mod 2p, so D = 2p.
- **C:** the window has length 4p−4−2B*, which is < 2p because B* ≥ R > p−2.

### Lemma N, LF101–134: ACCEPT for general t and κ
- The list of negative types is exhaustive: a letter is negative iff it is in P₀ with b > 0 or in C₀ with b < 0.

**(a)**
- ν₀ ≤ q₁ + (3/2)Σ(B_k−1) + n₊ ≤ q₁ + 3E/2 + n₊.
- Then 2Π₀+3+ν₀−2p = 4κ+1+2E+2n₊−2n₋−ν₀ ≥ 2κ+2+E/2.
- The last step uses q₁ ≤ κ, n₊ ≥ n₋ and n₋ ≤ κ−1.

**(b)**
- u₊ ≥ m₁+n₊−q₁.
- The C₀ a-labels ≥ 3 number at most (E−Σ(B_k−1))/2.
- E ≤ 2p−1−n₊−L, and 3L+3n₊ = 3R−3n₋.
- These give the displayed bound, which is ≥ (5κ+2)/2.
- The degenerate case t = 0 is correct.

**(c)**
- **(\*)** is a genuine forbidden integer zero-sum: it is disjoint from the +1 letters, its size is even and lies in W₀, and its target is T(∅) = 0.
- **(c1):** u₊ ≥ (p−2+κ+B)/2 ≥ B, and B+1 ≤ p−κ+1 ≤ R.
- **(c2):** κ+1 ≤ (5κ+2)/2.
- **(c3):**
  - X_{j\*−1} ≤ 2κ because X is even, so X_{j\*} ≤ 4κ ≤ R.
  - w(S) ≤ 2κ+B−k₁.
  - Type (ii) needs p−5+2κ−3n₋ ≥ B, and the left side is ≥ 3κ−1 ≥ B.
  - Type (iii): sⱼ ≤ 2κ−1−2n₋, and p ≥ 4κ+1 gives the needed 2B bound.
- Conclusion: **|A₋|+ν₀ ≤ 2κ**.
- The lift margin at LF108 is ≥ 2κ+2 and uses only (b), (\*) and D\*. It is genuinely independent of (a).

### Lemma F, LF136–179: ACCEPT

**(F1), full window:** W_{κ+1} = [0,R]. SS gives a set J with |J| ≡ v ≡ 0 and |J| ≤ R, so every P in the family is full.

**(F2), θ via full pairs: complies with LER LF6.**
- The full pair is explicit: Qᵢ and Qᵢ ∪ {i}.
  - The wrap gap has N−2κ−1 ≥ 2κ+1 runs.
  - i−1 ∉ Qᵢ.
  - The separator has N−2κ−2 ≥ 2κ runs.
- Any full pair gives the same difference d, because:
  - d ≡ hᵢ (mod p) and d ≡ σ({i}) (mod 2);
  - |d| ≤ p−1−2κ;
  - so two such differences differ by at most 2p−2−4κ < 2p.

**(F3), toggle connectivity:**
- (a) Trimming the right end of an interval keeps the number of intervals.
- (b) If gⱼ ≥ 2, then v_{j+1}−1 is non-adjacent to vⱼ, and v_{j+2}−(v_{j+1}−1) = g_{j+1}+2.
- (c) Σ_{j≤κ} gⱼ strictly decreases, ending at gaps (1,…,1,G) with G = N−2κ−1 ≥ 2κ+1.
- (d) The donors are G ≥ 2 and then 2. At the endpoint, G = 2κ+1.

**(F4), disjoint additive-constant patterns:**
- P₁ = {0,3,…,3κ} and P₂ = {1,4,…,3κ+1} are independent (wrap gap N−3κ−1 ≥ κ+1) and disjoint.
- P₁ ∪ P₂ has κ+1 intervals {3j, 3j+1}. The last separator has N−3κ−2 ≥ κ runs.
- Lemma A with N(a) gives f₀ = 0.
- At the endpoint, 3κ+1 = N−1−κ exactly, and the construction still works.

**(F5), complement:** Q₀ is independent and Q₀ᶜ has κ+1 intervals. Lemma C then gives Θ(all) = B*−2ν₀−2p.

### Lemma RIG, LF183–196: ACCEPT
- S_ev and S_od are independent, and M = (p+1)/2 ≥ 2κ+1.
- **Top-(κ+1) bound:** the top κ+1 values form a set in the family, so their sum is U′ ≤ −1−ν₀.
  - Hence θ₍κ+1₎ ≤ −1, which gives (R1).
- **Rigidity:** adding (R1) over S_ev and S_od and using (F5) gives B* ≤ R, so B* = R and every |c| = 1.
- **Tight θ excess:** both instances of (R1) are tight, so every tail entry equals −1.
  - Since M ≥ κ+2, θ₍κ+1₎ = −1.
  - Every eᵢ ≥ 0, and Σeᵢ = κ−ν₀.

### Sec. 5, LF200–228: ACCEPT

**(T):** θᵢ ≡ hᵢ (mod p) and θᵢ ≡ σ({i}) ≡ rᵢ (mod 2), because every label is odd.

**Run facts:**
- **(E1)** θᵢ = −1 ⇒ rᵢ is odd, so run i is nonempty.
- **(E2)** An empty run has Xᵢ = 0, so τᵢ ≡ θᵢ (mod p). Then θᵢ = 0 would mean yᵢ = y_{i−1}, which violates the NF empty-run rule.

**Selection:**
- |O| ≥ f+κ+1.
- Each P(O′) has m = κ and window W_κ = [2,R].
- Θ(P) = −ν₀, because P contains the excess support Z_S.
- T(P) ≡ −ν(P), and ν(P) is even.

**KEY:** if ν(P) ≥ 2, the ν(P) letters of value −1 have even size in [2,R] and sum to T(P). This contradicts (SR). If instead ν(P) = 0, the letter set of P is exactly A₋.

**Case (i), free slot (f ≥ 1):**
- The run o is nonempty by (E1) and is not in P(O′₂).
- So the two patterns have different **letter** sets, however many other runs are empty.
- At most one of them equals A₋, so the other has ν ≥ 2.
- This case covers every ν₀ ≥ 1.

**Case (ii), no free slot (f = 0):**
- Then ν₀ = 0, A₋ = ∅, and θ = 0 on Z_S.
- (E2) makes these runs nonempty, so ν(P) ≥ 2.
- This is the only place the genuine empty-run rule is load-bearing.

**By-ν₀ line, LF224–226:** consistent. The phrase "also by N(c)" holds because after RIG, |A₋| = ν₀.

### Sec. 6, LF230–256: ACCEPT
- **Endpoint p = 4κ+1:** every value is a substitution into the general formulas: N = 4κ+2, R = 6κ, W_{κ+1} = [0,6κ], W_{κ+2} = [0,6κ−2], E ≤ 3κ, m₁ ≥ (5κ+4)/2, G = 2κ+1, and a separator of κ runs.
- **(κ,p) = (3,13):**
  - Windows W₀…W₇ are as listed.
  - m₁ ≥ 10, u₊ ≥ 9 and |A₋|+ν₀ ≤ 6.
  - P₁ = {0,3,6,9} and P₂ = {1,4,7,10}.
  - Q₀ᶜ = {1},{3},{5},{7..13}.
- No enumeration was used.

### Imports claimed unused: VERIFIED
- **CJ‴:** not cited anywhere load-bearing.
  - In the all-equal case, RIG forces ν₀ = 0, which is closed by Sec. 5 case (i) or (ii).
  - The case where every rotation is the identity is already excluded at IF\*(b).
  - SCP LF36–38 allowed CJ‴; the proof only narrows the inputs.
- **Other unused inputs:** S1(a), the Setting fact, FB-E, Theorem P, PL THETA, PL Secs. 8–9 and CR/(H-ALT) are all unused. The one exception is the literal Setting-fact path described in MINOR-1.
- **K2 and K3:** no lemma is imported.
  - The proof agrees with the K3 verdict at p ≥ 13, since ⌊(p−1)/4⌋ ≥ 3 ⇔ p ≥ 13.
  - K3-11 (p = 11) is outside the range (LF271–274).
- **No residual, middle-range or full-Olson closure is claimed** (LF271–278; PKG LF66–70).
- **Sec. 7 remarks (R1)–(R3) are not claims.** The "(2/3)κ+4" figure in (R1) is unverified and not load-bearing.

## Finding

**MINOR-1: SS is cited "as stated" through an ancestor that uses the Setting fact.**

- **Step.**
  - PRF LF89–91 cites PL Lemma SS "as stated".
  - PL's proof of SS (PL LF97) applies PL Lemma D.
  - PL Lemma D bounds sⱼ "by ZSTRUCT and the Setting fact" (PL LF89–90).
  - Yet PRF LF295 and PKG LF35 declare the Setting fact unused.
  - PKG LF33–34 and PRF LF288 also list "the covering step of D" as an accepted input, although D\* re-proves it.
- **Consequence.**
  - There is no mathematical consequence. SS needs only density on [0,B*], which D\* proves without the Setting fact; I re-derived SS that way.
  - However, U, A, C, F, RIG and Sec. 5 all inherit SS.
  - So the stated input hygiene is literally inaccurate as written. Someone auditing the dependency graph would record a Setting-fact ancestor.
- **Repair.**
  - At LF89, add: "SS follows from Lemma D\* by PL's bijection J ↦ (J∩Pos(P)) ∪ (Neg(P)∖J) and term parity (PL LF97–98); PL Lemma D is not used."
  - Remove "covering step of D" from the list of inputs.

## Editorial notes (not counted)
1. LF215 says "By (SR) this is an identity 2p-subword". (SR) only says such a sum does not exist. Better: "this contradicts (SR); equivalently, the GRX if-direction gives an identity 2p-subword."
2. LF67–73 shows normalisation before the light-side swap. After the swap, γ ↦ −γ, and normalisation and c := ±b must be reapplied to the chosen light side. "Verbatim" implies this; saying it once would help.
3. Several symbols are overloaded: F, H, W, E and N. Context disambiguates every use.

## Governing errata applied
- **LER LF5:** CR and (H-ALT) are unused (LF269–270).
- **LER LF6:** θ is defined only through an explicit full pair; (F2) complies.
- **LER LF7:** the m(P) convention is used throughout.
- **FB erratum 1:** it changes no statement.
- **BAL overlay 5:** ZSTRUCT holds in (S′) for every index-<1 generator, which IF\*(d) needs.
- **K3E:** its MINOR-2 direct-bound pattern is matched by IF\*(b). Its MINOR-1 frame quantifier is respected: the proof uses no hypothesis that depends on the frame, so no H11-type residual arises.

## Separation of verdict types
- **Correctness:** Theorem USK and Lemmas W, IF\*, D\*, N, F and RIG are correct at 3 ≤ κ ≤ ⌊(p−1)/4⌋ under the full antecedent. This is relative to the accepted imports listed above. There is no flaw beyond MINOR-1.
- **Completeness:**
  - Complete for the frozen target (SCP LF14–21).
  - It is a scoped partial of ordered Olson. Outside this range:
    - κ̂ ≤ 2 is accepted separately.
    - κ̂ > (p−1)/4, including p = 11 with κ̂ = 3, is open; K3-11 stays conditional.
    - κ̂ = 0, p = 7, other cells and full ordered Olson are open.
- **Process:** timestamps, freeze order, hashes, sizes and the "no computation" declarations cannot be verified from the text and were not used.
- **Priority and novelty:** none is claimed by the author and none here. "[NEW]" means "proved in this text".
- **Computation:** none here.

This judges only the scoped mathematical claim. It does not approve the research target, ordered Olson, or any runtime or process step.
