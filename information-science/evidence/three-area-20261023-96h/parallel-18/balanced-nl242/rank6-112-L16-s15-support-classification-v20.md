# Balanced NL242 (3,112), L=16, s=15: support is a union of complementary 3-spaces

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:14:37-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** Under the source-separated v205 L16 premises, this proves a necessary support classification for the previously open s=15 case. It does not yet exclude s=15, L=16 or a residue type. Handwritten exact algebra only; no scientific program, selected numerical probe, independent review, formal/kernel or novelty claim.

## Claim

Under v6's L16 hyperplane restrictions and dim aff(Σ)=6, after an affine translation

    Σ = F ∪ G,      F,G ≤ F₂⁶,    dim F=dim G=3,    F∩G={0}.

The translation is the old sum τ=Σ_{x∈Σ}x, which belongs to Σ as a consequence, not an assumption. No statement about the signs g is made here.

## 1. Hyperplane spectrum

Translate by τ, so the new sum of the 15 points is zero. For ω, set W(ω)=Σ_{x∈Σ}(−1)^{ω·x}. Since every negative side has even size, W≡15≡3 (mod 4). v6 Lemma H forbids nonempty sides of sizes 1,2,3,5; hence, for ω≠0, W∈{7,3,−1}. Write their multiplicities a,b,c. Affine spanning excludes W=15 off zero. Parseval gives

    a+b+c=63,       6a+b=84.

Character orthogonality gives Σ_ω W(ω)=64·1_{0∈Σ}=288−16a. If 0∉Σ, a=18 and b<0; therefore 0∈Σ, a=14, b=0, c=49.

Each of the fourteen 4-point negative sides is an affine 2-plane by Lemma H. Let A be the 14 corresponding dual vectors. For ω≠0, W(ω)=−1+8·1_A(ω). Fourier inversion at any x∈Σ\{0} gives Σ_{ω∈A}(−1)^{ω·x}=6, so exactly four of these 14 planes contain x.

## 2. The two disjoint simplex codes

Form the binary length-14 code C of all evaluation words (ω·x)_{x∈Σ\{0}}. Its dimension is 6 and its nonzero weights are fourteen 4s and forty-nine 8s. It is self-orthogonal: wt(u),wt(v),wt(u+v) are divisible by 4, so 2|supp(u)∩supp(v)|=wt(u)+wt(v)−wt(u+v) is divisible by 4.

Fix a weight-4 word u with support T. Every point of T lies in four weight-4 supports, so the other supports have total intersection size 4·3=12 with T. By self-orthogonality each distinct intersection has size 0 or 2. Thus exactly six other weight-4 words meet T, and seven are disjoint from T.

The four distinct nonzero columns at T form a plane and have rank three: their sum is zero, while a three-point dependence would force the fourth column to be zero. Restriction C→F₂^T has rank 3, so its kernel C₀ has dimension 3. Its seven nonzero words are precisely the seven weight-4 words disjoint from T.

The union B of their supports has size 7: every active coordinate in a 3-dimensional code is 1 in four codewords, so 4|B|=7·4. On B the seven nonzero coordinate functionals of C₀ are all distinct: for every nonzero message, four coordinates are 1, so Fourier inversion gives multiplicity one for each nonzero functional. In particular any vector orthogonal to C₀ has either zero or at least three coordinates in B.

The other seven weight-4 words, namely u and the six meeting T, have at least two coordinates in T and therefore at most two in B, which is disjoint from T. Since C is self-orthogonal, all seven vanish on B. Their sum, if nonzero, is a C-word supported in the seven coordinates outside B and hence has weight 4 rather than 8. So these seven words together with zero form a 3-dimensional subcode C₁ supported outside B. C=C₀⊕C₁; the same support-count/Fourier argument shows C₁ uses its seven coordinates as the seven distinct nonzero 3-bit functionals.

In a dual basis adapted to C₀⊕C₁, the 14 columns Σ\{0} are exactly the seven nonzero vectors of one 3-space and the seven nonzero vectors of a complementary 3-space. Together with 0 this is F∪G, as claimed. ∎

## Dependencies and residual

This uses `rank6-112-L16-reduction-v6.md` SHA-256 `450cd2ac6328e5c1c1b2a4eaad4a9d7144ac21be4582b67894ac7a35431b283d`, particularly Lemma H and the L16 setting; `rank6-lifted-floors-consolidated-proof-v1.md` SHA-256 `6c5ce361f12e0335c5dbfc49f783bb5f926a7575e04bfd929a851d6aaf55b929` for dim aff(P)=6; and their exact admitted cuts. When s=15 the L16 budget leaves no P\Σ coset, so aff(P)=aff(Σ). All preceding new conclusions are unreviewed author candidates.

s=15 remains open pending its slice-zero signs; s=16 remains open. Original witness-or-unrestricted-exclusion and (24,24,2) gaps remain open. HOLD, all findings and HELD/ZERO/NONINPUT restrictions remain binding; novelty UNCLEARED.
