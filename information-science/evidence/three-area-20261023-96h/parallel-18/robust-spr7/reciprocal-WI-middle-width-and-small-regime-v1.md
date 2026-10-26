# Reciprocal W_I — exact middle-width identity, an exact x1 localization, and a FORMAL small-contact regime computation

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:33:31 PDT 2026**. InfoSPR7/info-2. **NEW WRITTEN CANDIDATE**, additive to `reciprocal-WI-orientation-and-window-v1.md` (SHA256 `1e02dd4812713f45bfbd805c0b21b54629110c83423da6132cf4f0a15a4f63d9`). It works in the chart and notation of v10 §4 (SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`, read with erratum-1 `cd14290a…93e1`). No source is edited.

Variables are symbolic throughout. §1 and §2 are exact. **§3 is FORMAL leading-order asymptotics: it is labelled as such and is NOT a proof.** No numeric instance, interpreter, eval, program, CAS or GO is used.

Notation: C=c+1/c, H3=h−1−2C, u=rsw=β^{-1/2}, d0=1/w. Write S1=1/r+1/s+1/w, S2 for the sum of pairwise products of 1/r, 1/s, 1/w, and S3=1/(rsw). Let x1<x2<x3 be the positive roots of F, and e1=1/x1+1/x2+1/x3.

## 1. Exact middle-width identity

From F=E_B·Δrev with E_B(0)=1, E_B=1−e1t+…, and Δrev=2(w1t²+w3t+w2), comparing coefficients gives

`2w2=F(0)`, `2w3=F'(0)+e1·F(0)`.

In chart terms the inputs are as follows. Since P2=(1+u²t)·Q(t) with Q=∏_{ρ∈{r,s,w}}(1−t/ρ)² (because βr²s²w²=1),

- `F(0)=u²−2S1−H3`;
- `F'(0)=[t²]P2−M1`, where `[t²]P2=S1²+2S2−2S1u²`;
- `M1:=[t²]P3=(C+1)²+h(1−2C)`, obtained by multiplying (1+t), H_c²=1−2Ct+(C²+2)t²+… and 1+(h−2)t+t² through t².

**So the third width w3>0 is EXACTLY `[t²]P2−M1+e1·F(0)>0`.** This is the one width condition left unrestricted by the window lemma.

## 2. Exact localization of x1 and y1

Because P3 is palindromic and P4(t)=t⁷P2(1/t),

`F(1/t)=t^{-6}(P4(t)−P3(t))`,

identically. Since F<0 on (x3,∞), it follows that **P4<P3 on (0,y1)**, where y1=1/x3.

On 0<t<min(c,1):

- P4(t)=(1−wt)²(1−rt)²(1−st)²(1+βt) ≥ (1−wt)²(1−t)⁴, since r,s<1;
- P3(t) ≤ (1+t)(1+ht+t²), since H_c(t)∈(0,1) there.

**Lemma.** Suppose 3d0<min(c,1) and

`4(1−3d0)⁴ > (1+3d0)(1+3hd0+9d0²)`.

Then P4(3d0)>P3(3d0), so y1≤3d0 and **d0<x1<y1≤3d0**.

The upper bound uses x1x3<1. The lower bound is the imposed C4-cell condition from erratum-1. This lemma is exact.

## 3. FORMAL leading order: the small-contact regime makes w3<0

**Not a proof.** The following is formal leading-order bookkeeping: remainders are dropped and labelled O(·), with no explicit bound attached.

Take r,s→0 with c and h bounded, and put a=1/r>b=1/s. Window consequence B forces w→∞, and §2 then gives x1=O(d0).

- The leading order of F(0)>0 forces u²≈2S1, so f1:=F'(0)≈−(3S1²−2S2)<0.
- Also f2:=[t³](P2−P3)≈2S1³+2S1S2−2S3.
- From F(x1)=0, f0/x1=−f1−f2x1+O(x1²).

Hence

`2w3≈x1·(|f1|(1/x2+1/x3)−f2)`.

With x2>s, so that 1/x2<b, and with x3 large,

`f2−|f1|/x2 > (a+b)²(2a−b)+2a²b+4ab² > 0`

at leading order, since S1≈a+b, S2≈ab and S3≈0.

So, FORMALLY, **w3<0 in this whole regime**.

The same conclusion follows independently from the large-scale root sum. The two remaining roots of F have sum −p with p≈x1+x2−2(r+s)+β. Here x2<2s at leading order and β≈rs/(2(r+s))<r/2, so p<0.

Both computations point the same way. Making them rigorous needs explicit remainder bounds for degree-7 polynomials with explicit coefficients. That is feasible in writing, but it is NOT done here.

## 4. Status and exact next step

- **Exact here:** the middle-width identity; the identity F(1/t)=t^{-6}(P4−P3); and the localization lemma d0<x1<y1≤3d0 under its stated smallness condition.
- **Formal only:** w3<0 when r,s are small.
- **No W_I emptiness or point is claimed.**
- **Next step:** turn §3 into an exact inequality chain. Bound f0/x1 from above with a convexity or Taylor certificate of F on (0,3d0), using exact coefficient bounds. Then show `[t²]P2−M1+e1F(0)<0` on the regime {r,s≤ρ*} for an explicit ρ*. The bounded-r regime remains separate.

Assurance: this is a written candidate only. It is not formal, kernel, human, family, cross-vendor, executable or novelty acceptance, and not a GO. All four owner process majors and all parent findings remain; probes receive zero credit; the cutoff and deadline are unchanged.
