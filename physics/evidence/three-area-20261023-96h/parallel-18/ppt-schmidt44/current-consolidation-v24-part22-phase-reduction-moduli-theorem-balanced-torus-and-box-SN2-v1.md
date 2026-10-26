# CURRENT P44 CONSOLIDATION v24 — PART22/22: a two-phase symmetry of the chart, a moduli-only two-block theorem, the whole balanced torus |u|=|v|=|w|=|z|>0 and an explicit 4-moduli box are SN2

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 01:16:01 PDT 2026**. Exact WRITTEN mathematics; every identity and inequality is displayed and checked by hand. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## T0. Scope and union

The NEW claims C44–C46 sit on the ORIGINAL chart. The complete current union is the twenty-one parts plus Part15 ADDENDUM-1 bound in `checkpoint-104-complete-current-v23-twenty-one-part-manifest-v1.json` (SHA256 d6286e08ce0193283bd23dab45d9d6f6d7c08f8062944b963b50a774fb73f9b3), THIS part, and all mandatory overlays. Parts 9–22 are LATER UNREVIEWED.

Imports:
- Part10 H1.1/H1.2 and the H5 involution;
- Part20 (B1.1), B3, (B-P), C39 and C41;
- Part21 R1–R5, here extended to arbitrary phases;
- Part15 Q6.

Moduli are written p_u=|u|, p_v=|v|, p_w=|w|, p_z=|z|.

## T1. Lemma C44.0 (two-phase symmetry)

For unit complex numbers λ, μ, R_x is locally unitarily equivalent to R_x'' with

`x'' = (μλ^2 u, μλ v, μ w, λ^4 z).`

*Proof.* Take U=diag(α0..α3) on Alice and V=diag(β0..β3) on Bob. Every generator must be mapped to a unit multiple of itself or of the new d, h:
- **a.** α0β0=α1β1=α2β2=:c.
- **b.** α0β1=α1β2. **c.** α1β0=α2β1. Both reduce to β1^2=cβ2 (with α0=1, α_i=c/β_i for i=0,1,2).
- **e.** α2β0=α3β3, i.e. α3=c^2/(β2β3).
- **f, g, j** are single kets, so P(·) is invariant.

Then (U⊗V)d_x = β2 · d_x'' and (U⊗V)h_x = h_x''' with x'''_k = β_k x_k and x''_k = (α3/β2)β_k x_k. Since α3/β2 is a unit, P(h_x''') = P(h_x''). Put λ=c/β1 and μ=c^3/(β1^2β3); β1 and β3 are free, so λ and μ are free. The multipliers α3β_k/β2 for k=0,1,2,3 are c^5/(β1^4β3)=μλ^2, c^4/(β1^3β3)=μλ, μ and (c/β1)^4=λ^4. ∎

Checks:
- λ=1, μ=-1 gives R_x ~ R_(-u,-v,-w,z).
- Choosing λ^4=conj(z)/|z| makes z''=|z|>0 without changing any modulus.

## T2. The moduli-only core theorem C44

Assume by T1 that z=p_z>=0 is real. Fix κ>0 with p_zκ^2<1, put ρ=(1-p_zκ^2)/(κ(1+p_z)), and use the Part21 R1 ensemble (δ=±iκ, β,χ in {±γ} or {±γ̄}, γ^2=-iρ), now with

`ψ = a + βb + χc + δd - p_zδ e + δ(vχ-u) f + δ(vβ-w) g.`

**Rank.** Row3 of H1.2 is [δu+δ(vχ-u), δv, δw+δ(vβ-w), p_zδ-p_zδ] = δv·[χ,1,β,0] = δv·row1. Column 3 is 0, and rows 0–2 are as in Part21 with s replaced by p_z, so det=1-δ(p_zβ^2+χ^2)+p_zδ^2=0. Hence SR<=2.

**Moments.** By sign independence, every cross-moment pairing a, b or c with d, e, f, g vanishes. For example:
- b–g: v̄ρE[δ̄]-w̄E[βδ̄] = 0;
- c–f: v̄ρE[δ̄] = 0.

On (d,e,f,g), E[cc^†] = κ^2ωω^† + κ^2p_v^2ρ(E_ff+E_gg) with ω=(1,-p_z,-u,-w). For example E|δ(vχ-u)|^2 = κ^2(p_v^2ρ+p_u^2), and E[δ(vχ-u)conj(δ(vβ-w))] = κ^2 u w̄. Hence

`R_x - E P(ψ) = (1-ρ)[P(b)+P(c)] + F M F^†,   M = 3I - κ^2ωω^† - κ^2p_v^2ρ(E_ff+E_gg)`

on (d,e,f,g,h,j), with h and j diagonals equal to 3.

**Rephasing.** Let Λ multiply the f and g coefficients by ū/p_u and w̄/p_w (by 1 if p_u or p_w is 0). This means using the unit multiples of the generators f, g, which have the same support. Then ΛMΛ^† is real, with:
- d: 3-κ^2; e: 3-κ^2p_z^2; f: 3-κ^2(p_u^2+p_v^2ρ); g: 3-κ^2(p_w^2+p_v^2ρ);
- (d,e)=κ^2p_z; (d,f)=κ^2p_u; (d,g)=κ^2p_w;
- (e,f)=-κ^2p_zp_u; (e,g)=-κ^2p_zp_w; (f,g)=-κ^2p_up_w.

**Cancelling (d,e).** Subtract the Part20 B3 family (any x) with A C̄ = a0c0 = κ^2p_z. If p_z=0 it is omitted.

**Theorem C44.** Suppose there are κ, a0, c0, b0, ν0 >0 such that:
- (a) p_zκ^2<1 and ρ<=1;
- (b) a0c0=κ^2p_z, b0^2<=3 and c0^2<=3ν0^2;
- (c) D:=3-κ^2-a0^2>0 and Ee:=3-κ^2p_z^2-c0^2>0;
- (d) N := [[Fd, -κ^2p_up_w],[-κ^2p_up_w, Gd]] - τ êê^T is PSD.

Here Fd=3-κ^2(p_u^2+p_v^2ρ)-ν0^2c0^2, Gd=3-κ^2(p_w^2+p_v^2ρ)-a0^4/b0^2, τ=κ^4(p_u^2+p_w^2)(1/D+p_z^2/Ee), and ê=(p_u,p_w)/√(p_u^2+p_w^2), with τ=0 if p_u=p_w=0. Then SN(R_x)=2.

*Proof.* Let r=√(p_u^2+p_w^2). The (d;f,g) coupling is m=κ^2rê, and the (e;f,g) coupling is n'=-κ^2p_z rê. Set:
- Φ2 = [[D, m^T],[m, (κ^4r^2/D)êê^T + N]] on (d,f,g). Its Schur complement is N>=0.
- Φ1 = [[Ee, n'^T],[n', (κ^4p_z^2r^2/Ee)êê^T]] on (e,f,g). Its Schur complement is 0.

Their (f,g) blocks add to τêê^T+N, which is the (f,g) block of the remainder. The remaining diagonals 3-b0^2 (h), 3-c0^2/ν0^2 (j) and 1-ρ (b, c) are nonnegative. Φ2 lives on Alice{0,3} and Φ1 on Alice{2,3}, so (B-P) applies. Every term is in the SN<=2 cone, and Q6 gives SN>=2. ∎

For p_u=p_w=p_v=p_z=s, (d) reduces exactly to Part21 (R4.1): along (1,1)/√2 the condition is G-n-τ>=0, and along (1,-1) it is G+n>=0.

## T3. Corollary C45 (the whole balanced torus)

**C45.** Every chart point with |u|=|v|=|w|=|z|=s>0, with arbitrary phases, has SN(R_x)=2.

*Proof.* Each range of s uses a result that depends only on moduli:
- s in [2/3,3/2]: C44 with Part21's parameters (κ=1/2, a0=c0=√s/2, b0^2=3, ν0^2=s/12). After T1 and the rephasing, every number is the ray number, so Part21 R5 applies verbatim.
- s^2<=4/5: Part20 C39 depends only on (p_v,p_w,p_z) and is uniform in u, so the C41(b) numbers apply.
- s>=3/2: the involution x'=(w/z,v/z,-u/z,1/z) has moduli (1,1,1,1/s). C39 applied there with the C41(a) numbers (t^2=2/5, |z'|^2<=4/9) concludes. ∎

The literal input, the whole Part21 ray, its negative-z partner (s,s,s,-s), and every phase variant are covered.

## T4. Corollary C46 (explicit 4-moduli box) and its involution image

**C46.** If p_z in [2/3,3/2] and p_u, p_v, p_w <= 3/2, then SN(R_x)=2.

*Proof.* Use C44 with κ=1/2, a0=c0=√p_z/2, b0^2=3, ν0^2=p_z/12. Then:
- f and g costs are both p_z^2/48;
- the h and j leftovers are 0;
- ρ=(4-p_z)/(2(1+p_z))<=1 iff p_z>=2/3;
- D=(11-p_z)/4 >= 19/8;
- Ee=(12-p_z-p_z^2)/4 >= 33/16, which is decreasing in p_z;
- p_z^2/Ee <= (9/4)(16/33) = 12/11.

With P=3/2:
- τ <= (1/16)(2P^2)(8/19+12/11) = P^2·316/1672 = 79P^2/418;
- Fd, Gd >= 3-P^2/4-P^2/4-3/64, using ρ<=1 and p_z^2/48<=3/64;
- |X| = p_up_w/4 <= P^2/4.

Since τêê^T <= τI and a symmetric 2x2 [[A,X],[X,B]] with A,B>=|X| is PSD, it suffices that 189/64 >= P^2(3/4+79/418) = P^2·785/836. At P^2=9/4 the right side is 7065/3344, and 189·3344 = 632016 > 7065·64 = 452160. ∎

**C46′.** If p_z in [2/3,3/2] and p_u, p_v, p_w <= (3/2)p_z, then SN(R_x)=2.

*Proof.* The involution source has moduli (p_w/p_z, p_v/p_z, p_u/p_z, 1/p_z), which lie in the C46 box. ∎

## T5. Map, gaps and status

**Currently proved SN2**, each by an explicit certificate:
- Part6 ball;
- Part10 Theorems A and C, and H5.1;
- Part11 D and D′;
- Part13;
- Part15 E0/E;
- Part18 C36;
- Part19 C37/C37′;
- Part20 C39–C41;
- Part21 C42/C43;
- here C45, C46 and C46′.

**Still OPEN in this chart.** Mainly large comparable moduli with p_z away from them, for example (V,V,V,1) for large V: there ρ<=1 forces κ>=~1/(1+p_z), so the f and g costs scale like V^2. Also v-dominant points with u, z!=0 outside Theorem D. No member of the chart is known to be SN3.

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v24 PART22/22.**
