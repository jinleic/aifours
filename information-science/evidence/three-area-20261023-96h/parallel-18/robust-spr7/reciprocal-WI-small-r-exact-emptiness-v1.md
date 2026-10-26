# Reciprocal W_I — EXACT emptiness in the small-first-contact region (explicit threshold)

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:38:46 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN THEOREM CANDIDATE**; a fresh gate is required. This file makes the FORMAL §3 of `reciprocal-WI-middle-width-and-small-regime-v1.md` (SHA256 `5d921b5c14a5989fd24e0cdb6cd6d61eca1da0a2f92c982b64afc0a1f0f66bec`) exact, with explicit constants.

Its chart and definitions are from `reciprocal-class-exact-three-word-reduction-v10.md` (SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`), read with erratum-1 `cd14290a4ab5aacc8452b79966beb2e8c87dbdecb2140100c53cf4d2c0bc93e1`. It also uses the window lemma `reciprocal-WI-orientation-and-window-v1.md` (SHA256 `1e02dd4812713f45bfbd805c0b21b54629110c83423da6132cf4f0a15a4f63d9`). None of these is edited.

Variables stay symbolic. The only numbers are explicit rational proof constants. There is no numeric instance, interpreter, eval, program, CAS or GO.

## Theorem

Fix L≥2 and put C=c+1/c. **W_I contains no point with**

`h≤L`, `C≤L`, `r≤10^{-8}L^{-3}`.

This is an exact partial emptiness result. It does not decide W_I, W_II or W_III elsewhere, and it does not settle the reciprocal class or universal SPR7.

## Notation

Put a=1/r and b=1/s, so 1<b<a, and d0=1/w. Let σ1=1/r+1/s+1/w, σ2 be the sum of pairwise products of 1/r, 1/s, 1/w, and σ3=1/(rsw)=1/u, where u=rsw.

Since βr²s²w²=1, P2=(1+u²t)·Q(t), with Q=(1−σ1t+σ2t²−σ3t³)²=Σq_k t^k. The coefficients are

`q1=−2σ1`, `q2=σ1²+2σ2`, `q3=−2σ3−2σ1σ2`, `q4=σ2²+2σ1σ3`, `q5=−2σ2σ3`, `q6=σ3²`.

P3 is palindromic. In the notation of the middle-width file:

- `[t]P3=[t⁶]P3=H3=h−1−2C`;
- `[t²]P3=[t⁵]P3=M1=(C+1)²+h(1−2C)`;
- `[t³]P3=[t⁴]P3=N3=(C²−2C+2)(h−1)+1−2C`.

N3 comes from (1+t)H_c²=1+(1−2C)t+(C²−2C+2)t²+(C²−2C+2)t³+… times 1+(h−2)t+t².

Write F=Σ_{k=0}^5 f_k t^k. Then:

- `f0=u²−2σ1−H3`;
- `f1=q2+u²q1−M1`;
- `f2=q3+u²q2−N3`;
- `f3=q4+u²q3−N3`;
- `f4=q5+u²q4−M1`;
- `f5=q6+u²q5−H3`.

Put η=H3+f0, so that u²=2σ1+η.

## Step 0 — size bounds

Assume r≤10^{-8}L^{-3}, so a≥10^8L³.

**Bound on d0.** Window consequence B gives r²w²>2/r−3. Since r≤1/3, 2/r−3≥1/r, so w²>a³ and **d0<a^{-3/2}**.

**Parameter bounds.** Since b<a and d0≤1:

- σ1∈(a,3a];
- ab≤σ2≤2a²;
- σ3=ab·d0≤a^{1/2};
- σ2≤σ1²/3.

Also |H3|≤h+1+2C≤4L, |M1|≤(L+1)²+2L²≤5L², and |N3|≤L²(L+1)+2L≤2L³.

## Step 1 — exact localization

Since 3d0<3a^{-3/2}<1/a=r<s<c≤1 and Ld0≤L·a^{-3/2} is tiny, the inequality

`4(1−3d0)⁴≥4−48d0>(1+3d0)(1+3hd0+9d0²)`

holds. The exact lemma of the middle-width file (§2) then gives **d0<x1<y1≤3d0**.

The chart also forces s<x2 and 1/c≤x3, since F(s)<0, F(1/c)≥0 and s<1<1/c. Hence `E':=1/x2+1/x3<b+1`.

## Step 2 — exact reduction to a single coefficient inequality

The middle-width identity is 2w3=f1+e1f0. By Taylor's theorem on [0,x1] with F(x1)=0, some ξ∈(0,x1) satisfies

`f0=−x1f1−(x1²/2)F''(ξ)`, and hence `2w3=−(x1/2)F''(ξ)+f0E'`.

Suppose F''≥0 on [0,3d0]:

- If f1≥0, then f0≤0, which contradicts f0=2w2>0.
- If f1<0, then f0≤x1|f1|, so `2w3≤x1(|f1|E'−F''(ξ)/2)`.

So it suffices to prove `F''(t)≥2(b+1)|f1|` on [0,3d0], with f1<0. That forces w3≤0, contradicting the positive middle width.

On [0,3d0],

`F''(t)=2f2+6f3t+12f4t²+20f5t³≥2f2−Err`, where `Err:=18d0|f3|+108d0²|f4|+540d0³|f5|`.

Define `Φ(f0):=2f2−Err−2(b+1)(−f1)`, viewing every coefficient as a function of f0≥0 with r, s, w, c and h fixed. It suffices to show Φ>0 and −f1>0.

## Step 3 — sign of f1

From −f1=3σ1²−2σ2+2ησ1+M1 and σ2≤σ1²/3,

`−f1≥(7/3)a²−24La−5L²+2σ1f0>0`.

This holds for every f0≥0, because a≥10^8L³ and the f0 term only adds.

## Step 4 — Φ is increasing in f0

Each f_k is affine in f0, with slope q_{k−1}. Hence:

`dΦ/df0 ≥ 2q2 − 4(b+1)σ1 − 18d0|q3| − 108d0²q4 − 540d0³|q5|`.

**The positive part.** We have 2q2−4(b+1)σ1=2[σ1²+2σ2−2(b+1)σ1].

- (σ1)(σ1−2b−2)≥(a+b)(a−b−2), because the d0 terms add d0(2a−2+d0)≥0.
- 2σ2≥2ab.
- Together, the bracket is at least a²+b(2a−b)−2a−2b ≥ a²−2a+b(a−2) ≥ a²/2.

So the positive part is at least a².

**The error part.** Using |q3|≤2a^{1/2}+12a³≤13a³, q4≤4a⁴+6a^{3/2}≤5a⁴ and |q5|≤4a^{5/2}, it is at most 234a^{3/2}+540a+1.

Therefore dΦ/df0≥a²−234a^{3/2}−540a−1>0, and so **Φ(f0)≥Φ(0)**.

## Step 5 — Φ(0)>0

At f0=0 we have η=H3 and u²=2σ1+H3∈(0,7a].

**Main term.** Main:=4σ1³+4σ1σ2−6(b+1)σ1²+4(b+1)σ2.

- It increases in σ1, because its σ1-derivative is 12σ1(σ1−b−1)+4σ2>0.
- It increases in σ2, because that coefficient is 4σ1+4(b+1)>0.
- So Main≥(a+b)²(4a−2b−6)+4ab(a+2b+1)≥(a+b)²(2a−6)≥a³.

**Remaining terms.**

- −4σ3≥−4a^{1/2}.
- 2H3[σ1²+2σ2−2(b+1)σ1]≥−2·4L·13a²=−104La². Step 4 shows the bracket is positive, and it is at most σ1²+2σ2≤13a².
- −2N3≥−4L³.
- −2(b+1)M1≥−20L²a.

**Error.** This uses |f3|≤5a⁴+7a·13a³+2L³≤97a⁴, |f4|≤4a^{5/2}+7a·5a⁴+5L²≤36a⁵ and |f5|≤a+7a·4a^{5/2}+4L≤29a^{7/2}. Then:

`Err≤1746a^{5/2}+3888a²+1`.

**Combination.** Hence

`Φ(0)≥a³−1746a^{5/2}−(104L+3888)a²−20L²a−4L³−4a^{1/2}−1`.

Since a≥10^8L³, we have a^{1/2}≥10^4L^{3/2}, so 1746/a^{1/2}≤1746/10^4·L^{-3/2}<0.18, and every other ratio to a³ is below 10^{-4}. So Φ(0)≥(4/5)a³>0.

## Conclusion

Steps 2–5 show F''≥2(b+1)|f1|≥0 on [0,3d0] with f1<0. Hence w3≤0. This contradicts the positive middle width that W_I requires through Δrev. No such point exists. ∎

## Scope and assurance

**Exact here.** The theorem is exact at its stated imports: v10's chart and definitions with erratum-1, the window consequence B, and the middle-width identity and localization lemma, all written candidates. The proof constants are deliberately crude.

**Not covered.** W_I with larger r, or with h or C unbounded relative to r, remains undecided. So do W_II, W_III, the reciprocal class and universal SPR7.

This is not formal, kernel, human, family, cross-vendor, executable or novelty acceptance, and not a GO. All four owner process majors and all parent findings remain; probes receive zero credit; the cutoff and deadline are unchanged.
