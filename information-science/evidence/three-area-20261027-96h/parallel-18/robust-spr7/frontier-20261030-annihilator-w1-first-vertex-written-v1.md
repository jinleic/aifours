# First written all-variable step for the five-node annihilator ray (word W1, u4 in (b,c))

Owner InfoSPR7-2, info-2. Native clock observed before writing: **Fri Oct 30 03:34:56 PDT 2026**. WRITTEN, unreviewed; additive to the chain whose lower bound the parent adopted via f283 Slice A (disposition a4f1f48c…). Manuscript e223cb44… is untouched; its six MAJORs are acknowledged and are NOT repeated here. m=6,7,8 residuals remain in scope; no four-node bound is reused on annihilators.

## 1. Object

For a six-node certificate of word W1 = (0,2,1,3,5,4), the five-node annihilator ray has support u₁<…<u₅ (nodes t₁,…,t₅) with odd sign word exactly (+,−,+,−,+) and weights wᵢ = c/(uᵢOᵢ(uᵢ)H′(uᵢ)), H(t)=Π(t−uᵢ); H′ signs (+,−,+,−,+) make all wᵢ>0. Placement (class-forced): u₁∈(0,a); u₂,u₃∈(a,b); u₄∈(b,c) [this file] or (c,d); u₅∈(d,e). Test F(t)=−t(b−t)(e−t). Envelope/endpoint domination per node was re-derived (not inherited): every node term Kᵢ/Oᵢ is bounded below, and the worst endpoints are O₊ at u₁ when x=0 / O₋ when x=a; O₋ at u₂; O₊ at u₃; O₋ (y=b) or O₊ (y=c) at u₄; O₋ (z=d) or O₊ (z=e) at u₅.

At the vertex (x,y,z)=(a,c,d) the cancelled worst-endpoint terms are, with Dᵢ:=Π_{j≠i}|uᵢ−uⱼ|,
t₂ = (c−u₂)(b−u₂)/D₂ > 0,  |t₁| = (c−u₁)(b−u₁)/D₁,  t₃ = (u₃−a)(d−u₃)(e−u₃)/((f−u₃)D₃) > 0,  |t₄| = (u₄−a)(d−u₄)(e−u₄)/((f−u₄)D₄),  |t₅| = (u₅−c)(u₅−b)/D₅.

## 2. Lemma (P1, written proof): t₂ > |t₁| for all admissible u₁<u₂<u₃<b<u₄<c<u₅

For any u₁<u₂ and reals v,w: (v−u₂)(w−u₁) − (v−u₁)(w−u₂) = (u₂−u₁)(v−w); hence [(v−u₂)/(v−u₁)]·[(w−u₁)/(w−u₂)] > 1 iff v>w. With ψ(v):=(v−u₂)/(v−u₁),
t₂/|t₁| = ψ(c)ψ(b)/(ψ(u₃)ψ(u₄)ψ(u₅)) = [ψ(c)/ψ(u₄)]·[ψ(b)/ψ(u₃)]·[1/ψ(u₅)].
The first factor exceeds 1 because c>u₄ (gap case), the second because b>u₃, the third because ψ(u₅)<1. Hence t₂>|t₁|. ∎ (Exact-rational check: 2000/2000 random admissible samples, minimum ratio 400/273>1 in the scanned range; evidence only — the proof above is the warrant. The same pairing fails when u₄∈(c,d), since then c<u₄: the band case remains unpaid.)

## 3. Corollary (complete all-variable vertex exclusion): at vertex (a,b,e)

At (x,y,z)=(a,b,e) the terms t₃,t₄,t₅ are positive by direct sign checks and |t₁| is dominated by t₂ by §2. So the W1-gap annihilator ray has strictly positive F-pairing at vertex (a,b,e) for every admissible box, nodes and members — the first fully proven annihilator-ray exclusion vertex.

## 4. Exact unpaid premise (next target)

The remaining seven vertices reduce to: (D6) t₃ > |t₄| + |t₅| at (a,c,d), plus its per-vertex variants ((a,b,d) needs t₃>|t₅| after a (c−u₃)-rescaling; (a,c,e),(0,c,d),(0,c,e) need t₃>|t₄|; (0,b,d) needs t₃>|t₅|; (a,b,e) done; (0,b,e) trivial). Evidence: exact-rational, 126/126 random admissible samples for every vertex sum, pinned gap minimum 53/630 (bands (1,4,7,13,20,24), nodes (1/2,2,3,5,15)); band-case (u₄∈(c,d)) pinned minimum 53/2205. Negative result: the brute positive-coefficient route FAILS — M₆ := (t₃−|t₄|−|t₅|)·(f−u₃)(f−u₄)D₃D₄D₅ expands in the twelve positive gap variables to 142,731 monomials with mixed signs (70,922 positive / 71,809 negative), and M₁ (band version) is also mixed; identities verified exactly at 25/25 rational points (sign convention of H′ corrected). A sharper route is required; the t₃/|t₄| ratio factors as η(a)η(u₁)η(u₂)η(d)η(e)η(u₅)/η(f) with η(v):=(v−u₃)/(v−u₄), where the pairs (a,d),(u₁,e),(u₂,u₅) each exceed 1 by the §2 rule, leaving the single leftover inequality η(u₂)η(u₅)/η(f)>1 — proved or refuted, this decides the pairing route.

## 5. Scope and assurance

Same-host exact-rational sampling and polynomial expansion in one Eval host; all written arguments are displayed above. Not a proof of D6, not an exclusion of W1 (one vertex of eight proven), not any m=6 word beyond W1's first family, and not a step toward narrowing the m=6/7/8 residual beyond K3's corrected census (17/239/1842 annihilator-admitting words). Process ancestry: owner-incidental-held-source-search-display-v1.json (dfb30abd…), OWNER PROCESS MINOR, status only; no clean-cognition claim.
