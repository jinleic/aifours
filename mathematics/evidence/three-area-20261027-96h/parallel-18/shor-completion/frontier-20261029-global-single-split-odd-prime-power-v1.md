# Shor completion: a global obstruction to one split odd prime in the head border

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 09:31:10 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE, with bounded integer-only controls.** This is a global necessary condition, not a proof of unrestricted noncompletion. Its imports are the actual-word border theorem (reconstructed below), Sands' divisor exclusion, and Tijdeman's dilation theorem. No T2 or other tiling-structure theorem is used. The original unrestricted finite-completion problem remains **OPEN**.

## 0. Provenance, separation and arithmetic correction

Main authorized continuation of the literal open bridge or a genuinely global witness/no-go. This packet instead proves a stronger uniform obstruction, with the full residual stated in §1. It does not substitute a restricted problem for the original target. The parent must assess the new proof and its exact scope separately.

This is same-author work. The owner had read and considered earlier unreviewed fibre-related sources before developing the preceding 165-family route, as disclosed to Main on 2026-10-29 shortly after 00:02:01 PDT:

> "Provenance correction to my pending freeze question: by 'independent' I meant no dependency on the pending Q55 theorem or a fibre packet as a mathematical premise. It is SAME-AUTHOR work, not a disjoint exposure: I had read and considered my prior unreviewed fibre-related sources before developing this route."

The present argument was developed after the separately submitted 2310-family packet. It uses its elementary approach as a same-author starting point, but every mathematical premise and every proof step needed here is restated. There is no blindness, clean-cognition, independent-author, or old-verdict-transfer claim.

**Non-premises:** the 165-family all-tail packet `20169ac9…` and its erratum `54329f3e…`; the 2310-family complete packet `2d6b48f8…` (separately frozen as f189); the seven-divides-head packet `564956bf…`; the four earlier 2310-family odd-tail packets and f169; f128/Q55, f157, f174 and all fibre/cofactor packets; every order-660/1320/1980/2640 packet; all historical HELD/ZERO/NONINPUT material. Parent notices of dispositions are status only. No outcome from those files is a mathematical premise here.

**Arithmetic disclosure.** The narrower, unsubmitted `frontier-20261029-165p-family-no-go-check.py` (SHA256 `2e4101b615e9846f5c1398f8117a02a36b29b3e2a91cfaa2e6df7925a10f9512`) used a floating-point square-root bound in its prime enumeration despite its integer-only header. Its observed PASS is not integer-only evidence and is **not used**. The error and the earlier checkpoint's overbroad description were disclosed in `owner-20261029-092233-prime-checker-arithmetic-disclosure-v1.json` (SHA256 `9f17a24fc1001f2ac6ceaff630918e3facbd8738dc6f6552754ac10ae5a5271d`). The old bytes remain unchanged. Section 8 uses only the new checker, which computes its own prime list with `math.isqrt` and cross-checks that list against an integer sieve. No old output is read.

Checkpoint-cadence breaches remain disclosed in `owner-20261029-checkpoint-2310-bridge-tijdeman-v1.json` and `owner-20261029-092113-single-prime-power-generalization-checkpoint-v1.json`. Mathematical progress does not waive them. No historical quarantine or process finding is cleared by this packet.

## 1. Statements and exact residual

Write A={0,3,8,11} and Y={0,1,7,13,14}. An **anchored tiling** means P,Q ⊆ Z_n, A⊆P, Y⊆Q, and P⊕Q=Z_n: every residue has exactly one expression p+q.

> **Theorem A (global candidate).** Let n>14 and suppose an anchored tiling exists. Then:
> 1. 330 divides n; each of 3,5,11 divides |Q|.
> 2. |P| is not a power of 2.
> 3. If the odd part of |P| is p^e for one odd prime p and e≥1, then p divides |Q| as well.
>
> Equivalently: every anchored tiling has either two distinct odd primes dividing |P|, or an odd prime dividing both |P| and |Q|.

The central new result is the following fully quantified, stronger-than-2310 proposition.

> **Proposition B (single split prime power).** Let K,e≥1, let p be an odd prime outside {3,5,11}, put ρ=p^e, and let R be any odd positive integer with 165|R and gcd(p,R)=1. Put n=2^KρR. No anchored tiling has
>
>     |P| = ρ·2^a,    |Q| = R·2^b,    a,b≥0,    a+b=K.
>
> R need not be squarefree. It may have arbitrary prime powers, including higher powers of 3,5,11, and any additional primes other than p.

> **Corollary C (order families).** If K≥1 and p is an odd prime outside {3,5,11}, there is no anchored tiling at n=165·p·2^K. More generally, at n=165·p^s·2^K, s≥1, any anchored tiling would have |P|=p^j·2^a with 1≤j≤s−1. Thus p would divide both border cardinalities. At n=165·2^K there is no anchored tiling either.

> **Corollary D (squarefree odd part).** If n=2^KM, K≥1, M odd and squarefree, and an anchored tiling exists, then the odd part of |P| has at least two distinct prime factors, all outside {3,5,11}. In particular, M must contain at least two primes in addition to 3,5,11.

These are necessary-condition results for the **same** actual border of the **same** hypothetical completion. They do not construct a code or a border, and do not say that any residual order is feasible.

**Literal residual:** the proof does not exclude (i) an odd prime shared between |P| and |Q|, or (ii) an odd part of |P| containing at least two distinct primes. These are genuine remaining alternatives, not bounded ranges or presumed constructions. No numerical lower bound on the completion order, all-order conclusion, priority, novelty, or original-problem solution is asserted.

## 2. Original-code caller: the actual border

The literal code, with `1` denoting the empty word, is

    S = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2}.

Let D be any finite UD, factor-complete code containing S. UD means concatenation is injective on finite atom lists; factor-complete means every word over {a,b} is a factor of some word of D*. A pure-a atom exists: if L is the largest atom length, embed a^(2L+1) in D*; some atom strictly inside that run is pure-a. Two different pure-a atoms a^u,a^v would give the distinct lists (a^u,a^v) and (a^v,a^u) for the same word. Thus there is exactly one, a^n. Since b∈D, no b^k with k≥2 is an atom.

Define, from actual D-atoms,

    P = {i mod n : a^i b^k ∈ D, k≥1},    Q = {j mod n : b^l a^j ∈ D, l≥1}.

Then A⊆P, Y⊆Q. The classical border theorem is Restivo–Salemi–Sportelli, as stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1). Here is the direct reconstruction needed for its use.

- **Injectivity of border sums:** if two residue pairs i_t+j_t have the same sum mod n, choose actual border atoms a^(i_t)b^(k_t), b^(l_t)a^(j_t), choose G>i_t+j_t in that common residue class, and H,K sufficiently large. The two atom lists consisting of H−l_t copies of b, the left atom b^(l_t)a^(j_t), (G−i_t−j_t)/n copies of a^n, the right atom a^(i_t)b^(k_t), and K−k_t copies of b both spell b^H a^G b^K. The positive central a-run identifies the two border atoms (or their absence of a, in which case the atom is b). Distinct residue pairs give distinct lists, forbidden by UD.
- **Coverage:** embed b^L a^g b^L with g>L in any prescribed residue class mod n. The atom containing the last left b starts inside the left guard and cannot reach the right guard; it is b^l a^j. The corresponding right atom is a^i b^k. The intervening atoms are all a^n, so g≡i+j (mod n).

Hence P⊕Q=Z_n. The results of §1 therefore apply to any actual completion whose n>14. They are not a converse: an anchored tiling alone would not construct a finite UD factor-complete extension. We do not use or establish any smaller-order exclusion here.

## 3. Classical inputs and elementary tools

For X⊆Z_M, define Div_M(X)={gcd(x−x′,M):x,x′∈X}, including the value M from zero differences.

**Sands (import).** P⊕Q=Z_M iff |P||Q|=M and Div_M(P)∩Div_M(Q)={M}. Only the necessity is used. Source: Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3).

**Tijdeman (import).** If P⊕Q=Z_M and gcd(t,|P|)=1, then tP⊕Q=Z_M; in particular multiplication by t is injective on P. Source: Łaba–Londner, [same paper, p. 3 and the proof of Corollary 6.2 on p. 26](https://arxiv.org/pdf/2106.14042v3), citing Tijdeman [47, Theorem 1] and Coven–Meyerowitz [2, Lemma 2.2]. The integer statement preserves the same tiling complement; the cyclic version follows by lifting Q to Q+MZ. We import that statement, not Corollary 6.2 or T2.

**Dilation tool.** If gcd(t,|P|)=gcd(s,|Q|)=1, then tP⊕sQ=Z_M, by applying Tijdeman twice. Thus Div_M(tP)∩Div_M(sQ)={M}.

**Coset tool.** If X⊕Z=G and X lies in a subgroup H, then X⊕(Z∩(u+H))=u+H for every coset. Indeed the unique representation of a point y∈u+H has z=y−x∈u+H. In particular |Z∩(u+H)|=|H|/|X|.

**Gcd transport identity.** If g₀=gcd(y,R) and g₀|h|R, then

    gcd((h/g₀)y, R) = h.                                      (T)

Proof: write y=g₀z. Then gcd(z,R/g₀)=1, hence also gcd(z,R/h)=1, and gcd(hz,R)=h. This identity, rather than a squarefree-prime argument, is essential when R is not squarefree.

## 4. General elementary reductions

If n>14 is an anchored tiling order, then 2,3,5,11 all divide n. If n is odd, gcd(8,n)=1 lies in Div_n(P), as does gcd(1,n)=1 in Div_n(Q), against Sands. If one of 3,5,11 does not divide n, the A-difference equal to that prime has gcd 1 with n, giving the same contradiction. Thus 330|n.

Fix such an n.

**L1.** Each ℓ∈{3,5,11} divides |Q|. Otherwise P⊕ℓQ is a tiling by Tijdeman. Its divisor sets both contain ℓ: from the A-difference ℓ and from the scaled Y-difference ℓ(1−0). Since ℓ<n, this contradicts Sands.

**L2.** Let x=q−q′ be odd, g=gcd(x,n). If ℓ∈{3,5,11} divides x and gcd(g/ℓ,|P|)=1, then no such difference is possible. Indeed t=g/ℓ is an integer, tP⊕Q tiles by Tijdeman, and the scaled A-difference tℓ=g has gcd g with n, matching the Q-difference. Since n is even and g is odd, g≠n.

**L3.** |P| cannot be a power of 2. Suppose |P|=2^a and let T be the odd part of n. The tiling TP⊕Q and the coset tool show that Q meets every residue class mod T. Since 165|T, choose q∈Q with q≡6 (mod 165). L2 says every odd Q-difference is coprime to 165, because g/ℓ is odd, hence coprime to 2^a. If q is odd, q−0 is odd and divisible by 3. If q is even, q−1 is odd and divisible by 5. Both are impossible.

## 5. Parity and separation for Proposition B

Assume for contradiction the hypotheses and cardinalities of Proposition B. The only primes in |P| are 2 and p. For each u∈Z_R and γ∈Z_ρ define

    Q_u = {q∈Q:q≡u (mod R)},    P_γ = {v∈P:v≡γ (mod ρ)}.

**P1 (tail congruence).** If x∈Q−Q is odd and gcd(x,165)>1, then p|x. Otherwise g=gcd(x,n) is odd and coprime to p, so g/ℓ is coprime to |P| for a prime ℓ∈{3,5,11} dividing x. This contradicts L2. No squarefreeness of R is used.

**P2 (nonempty fibres).** RP⊕Q tiles because gcd(R,|P|)=1. Each coset mod R has |Q_u|=(n/R)/|P|=2^b elements. Similarly P⊕ρQ tiles and each P_γ has 2^a elements.

**P3 (dichotomy).** Either every Q_u has both parities and every P_γ is single-parity, or every P_γ has both parities and every Q_u is single-parity.

Proof with the quotient and parity maps explicit:

1. Fix u. Restriction of RP⊕Q gives (Q_u−u)⊕RP=RZ_n. The isomorphism Rz↦z mod N, N=n/R=ρ2^K, gives V⊕P̄=Z_N, with V=(Q_u−u)/R, |V|=2^b, and P̄={v mod N:v∈P} of unchanged cardinality.
2. Since gcd(ρ,2^b)=1, Tijdeman gives ρV⊕P̄=Z_N. Restrict to a coset γ mod ρ and reduce it mod 2^K. CRT makes that reduction bijective, so

       (P̄_γ mod 2^K) ⊕ (ρV mod 2^K) = Z_(2^K).

3. The first factor has an odd difference exactly when P_γ has both parities. The second does exactly when Q_u has both parities: R and ρ are odd, and q−u=Rz implies z≡q−u (mod 2).
4. In a tiling of Z_(2^K), K≥1, both factors cannot have odd differences, since their divisor sets would both contain 1. Neither can lack an odd difference simultaneously, since every sum would have a single parity. Thus for every pair (γ,u) exactly one fibre is mixed. Fixing either index proves the stated global dichotomy.

**P4.** The first alternative is impossible. Within a mixed Q_u, every even–odd difference is an odd multiple of R, hence divisible by 3, so P1 forces all of Q_u into one residue mod p. Comparing even elements of Q_u with odd elements of Q_(u+3), and similarly Q_(u+5), equates their residues mod p by P1. The steps 3 and 5 generate Z_R (2·3−5=1), so all of Q has one residue mod p. But 0,1∈Q.

We are therefore in the second alternative. Let E⊔O=Z_R be the indices of the even and odd Q-fibres. Both are nonempty: 0∈E and 1∈O. Every P_γ has both parities.

**P5 (separation).** Let y=v−v′ be odd with v,v′∈P_γ, and g₀=gcd(y,R). Then E and O cannot meet the same residue class mod g₀.

Suppose instead u∈E, u′∈O and g₀|u−u′. Take q∈Q_u and q′∈Q_(u′). The difference x=q−q′ is odd and g₀|x. Put h=gcd(x,R), t=h/g₀, s=ρ. Since g₀|h, t is an odd divisor of R, so gcd(t,|P|)=1; also gcd(ρ,|Q|)=1. Hence tP⊕ρQ tiles. By (T), and using ρ|y, we have

    gcd(ty,n) = ρh = gcd(ρx,n).

Both differences are odd and ρh<n. This contradicts Sands. Thus E is a union of residue classes mod g₀.

**P6 (the common period).** The stabilizer {s∈Z_R:E+s=E} is a subgroup of Z_R, hence πZ_R for a unique divisor π of R. Since E is nonempty and proper, π>1. Membership in E depends only on u mod π. P5 gives π|g₀ for every such odd pair in every P_γ. Therefore all elements of a given P_γ are congruent mod π: every even–odd pair is, and same-parity elements can be compared through an element of the other parity.

## 6. Two connectivity lemmas and the final contradiction

An **agreement graph** below is bipartite, with parts E and O. Only opposite-coloured vertices are joined. All vertices are residue classes, not selected Q-elements.

**G1 (three prime coordinates).** Suppose 165|R, E⊔O=Z_R is nonempty on both sides, membership depends only on u mod π with π|R, and some ℓ∈{3,5,11} does not divide π. The graph joining u∈E, v∈O whenever they agree mod 3, mod 5 or mod 11 is connected.

Proof. Let ℓ^c be the full power of ℓ dividing R and M=R/ℓ^c. Since ℓ∤π, π|M. Under CRT, E=Z_(ℓ^c)×E′ and O=Z_(ℓ^c)×O′, with E′,O′ nonempty and partitioning Z_M. Every layer with fixed ℓ^c-coordinate is complete bipartite, because its vertices agree mod ℓ. There are e′∈E′ and o′∈O′ agreeing on one of the other two prime coordinates q₁,q₂. Otherwise choose a residue z∈Z_M agreeing with some e′ mod q₁ and some o′ mod q₂; CRT permits this. If z∈E′ it forms an agreeing cross-pair with o′; if z∈O′ it forms one with e′, a contradiction. Such an agreeing pair gives an edge between every pair of ℓ^c-layers. Therefore the graph is connected. This proof explicitly allows c>1 and other prime powers in M. ∎

Apply G1 to the period π of P6. An edge joins an even and an odd fibre index and has difference divisible by a prime of 165. For **every** q∈Q_u and q′∈Q_v, the difference is odd and P1 forces q≡q′ (mod p). Since the fibres are nonempty, the whole union Q_u∪Q_v has a single residue mod p. A connected graph would force all of Q into one residue mod p, contradicting 0,1∈Q. Consequently

    165 | π.                                                   (6.1)

Choose an odd v₀∈P_0. Since 0∈P_0, P6 gives π|v₀; also ρ|v₀ by definition of P_0. Put

    y* = 8−v₀,    w = gcd(y*,R).

Then y*∈P−P is odd, y*≡8 (mod π) and y*≡8 (mod ρ). As π and ρ are odd,

    gcd(y*,p)=1,    gcd(w,π)=1.                                 (6.2)

**Extra tail rule.** Every odd Q-difference x divisible by w must also be divisible by p. If not, h=gcd(x,R) is a multiple of w. Set t=h/w. Then t is supported on R and is coprime to |P|. Identity (T), applied to y* with gcd(y*,R)=w, gives

    gcd(ty*,n)=h=gcd(x,n),

because x,y*,t are odd and coprime to p. This contradicts Sands for the tiling tP⊕Q. In particular w=1 is already impossible using x=1−0. We may keep it in the next lemma as a harmless case.

**G2 (a free agreement modulus).** Suppose π|R, 165|π, w|R, gcd(π,w)=1, and a nonempty proper E⊂Z_R depends only on u mod π. The graph joining opposite colours when they agree mod 3, mod 5, mod 11 **or mod w** is connected.

Proof. Each layer L_j={u:u≡j (mod w)} contains both colours: choose any E-residue and O-residue mod π and lift each with j by CRT, since πw|R. Within L_j every opposite-coloured pair agrees mod w, so L_j is connected. There are opposite-coloured residues c,d mod π agreeing mod 3 or mod 5. Indeed take any E-residue e and O-residue o; if they do not already agree, choose z≡e (mod 3), z≡o (mod 5). Whichever colour z has gives an agreeing cross-pair. Lift c into any layer L_j and d into any L_(j′) by CRT. Agreement on the chosen prime is preserved because that prime divides π. Thus an edge links every pair of layers. For w=1 there is just one complete bipartite layer. ∎

Conditions (6.1)–(6.2) give all hypotheses of G2. Every prime-coordinate edge forces all cross-fibre elements to agree mod p by P1. Every w-edge forces it by the extra tail rule. Both endpoints have opposite parities and every fibre is nonempty, so connectivity again forces all of Q to share one residue mod p. This contradicts 0,1∈Q and proves Proposition B.

## 7. Deducing the global alternatives and family statements

For Theorem A, §4 proves 330|n, L1 and L3. Suppose the odd part of |P| is a single prime power p^e and p∤|Q|. L1 implies p∉{3,5,11}. Write n=2^Kp^eR; since p∤|Q|, the full p-power of n is p^e. Thus R is odd, divisible by 165 and coprime to p, and the two cardinalities have exactly the form of Proposition B. The contradiction proves Theorem A(3).

For Corollary C, the primes 3,5,11 occur to the first power in n, so L1 assigns all of them to |Q|. At n=165p^s2^K, the odd part of |P| is p^j for 0≤j≤s. L3 excludes j=0, and Proposition B excludes j=s. This leaves exactly 1≤j≤s−1. For s=1 that interval is empty. When p is absent from n, |P| is a power of 2, also impossible by L3.

For Corollary D, squarefreeness makes the odd parts of |P| and |Q| coprime. Theorem A then requires at least two distinct odd primes in |P|, and L1 excludes 3,5,11 from that set. Nothing in this deduction excludes an odd part containing two or more additional primes, or the shared-prime alternatives at nonsquarefree orders.

## 8. Integer-only finite controls and verification boundary

New checker: `frontier-20261029-global-single-split-odd-prime-power-check-v1.py`, SHA256 `4dead88fa441d1f21246b9f20978164511c582ffa180d7075223ff6445e30d86`, 217 LF / 7,943 bytes. The owner executed exactly these bytes in a fresh namespace of the retained eval kernel after the arithmetic disclosure. All assertions passed and the actual output ended with `"result": "PASS"`. This is **WRITTEN-checked-in-kernel at the listed finite scope**, not formal proof or independent-model verification. No float, solver, CAS, network, or prior checker data is used by this script.

The finite controls are:

- `math.isqrt` trial-division primes through 200 agree with a separately constructed integer sieve.
- Identity (T): 141,969 exact cases over all residues of R∈{45,105,165,225,315,495,825,1155,1815,2145,5445}, including nonsquarefree R. R not divisible by 165 is used only to test the universal gcd identity, not as an original-target order.
- Cyclic stabilizer: 33,438 nonempty proper subsets over Z_3,Z_5,Z_7,Z_9,Z_15; the minimal period divides R and divides exactly the invariant divisor-shifts.
- G1 on exhaustive **small analogues**, with prime coordinates {2,3,5}: 32,766 partitions for (R,free full prime power)=(30,2); 1,022 for (30,3); 62 for (30,5); 32,766 for (60,4). The last case exercises a nontrivial prime power. The two-coordinate negative control is disconnected, as intended.
- G2 on exhaustive small analogues: 62 partitions each for (π,w,R)=(6,5,30) and (6,5,60); 32,766 for (15,7,105). A negative control dropping gcd(π,w)=1 is disconnected at π=15,w=3,E={0}.
- P5 collision arithmetic with R∈{165,495,825,1815,2145}, p∈{7,13,17} coprime to R, e∈{1,2}, K∈{1,3}: 528,984 exact gcd identities, with all odd multiples of ρ in the stated finite ranges.
- The coprimality step (6.2): 300 bounded cases with the same R,p,e and every π|R divisible by 165.
- P3 small-model tilings: a fresh exhaustive exact-cover enumeration of all tilings V⊕P̄ of Z_14 and Z_28 with 0 in both factors and |V| a power of 2. It found 71 and 13,161 ordered pairs respectively. In every pair the dilation by 7, the coset/CRT reduction, unchanged cardinalities, and exactly-one-mixed-parity property all hold.

These controls do **not** exhaust the hypotheses of Proposition B or either connectivity lemma. The all-R, all-prime, all-exponent assertions rest on the written proofs above. The classical imports, the actual-code caller, novelty, priority, and formal/kernel/human/configured-family acceptance are not checked by the script.

## 9. Review scope and handoff

A complete review must reconstruct, at the stated universal quantifiers:

1. The actual-code border caller in §2, or explicitly retain it as an imported theorem.
2. Sands and Tijdeman statement fidelity and applicability, including each coprimality and injectivity use.
3. The all-order reductions L1–L3, the parity quotient P3, and the mixed-fibre contradiction P4.
4. P5 using the nonsquarefree transport identity (T), then the cyclic stabilizer step P6.
5. G1 with the **full** ℓ-power removed, including arbitrary extra prime powers in R.
6. The choice v₀, coprimalities (6.2), the extra tail rule, and G2 with πw possibly a proper divisor of R.
7. Theorem A and Corollaries C,D as callers, without promoting either residual alternative to feasibility or impossibility.
8. All non-premise and process/arithmetic disclosures in §0; no inherited verdict.

This packet is returned as a separately reviewable candidate. It changes no frozen packet, ledger, parent disposition or prior review scope. No original full witness/no-go has been delivered.

**END OF GLOBAL SINGLE-SPLIT-ODD-PRIME-POWER CANDIDATE.**
