# Reciprocal W_I — automatic orientations, the r/s criterion and an exact coefficient window

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:27:15 PDT 2026**. InfoSPR7/info-2. **NEW WRITTEN LEMMA CANDIDATE** about the W_I chart of `reciprocal-class-exact-three-word-reduction-v10.md` (SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`). It must be read with that file's erratum-1 (SHA256 `cd14290a4ab5aacc8452b79966beb2e8c87dbdecb2140100c53cf4d2c0bc93e1`). Both are unchanged. It also uses the zone table `general-n7-contact-zone-table-v1.md` (SHA256 `a05d332de4fac12f2416a4758c34f4e2fb380163e76fa7f17eb6313fadf4fce1`).

All variables are symbolic and every identity is written out. No numeric instance is used. The instance withdrawn in owner erratum v4 is not used. No interpreter, eval, program, CAS or GO. This does not decide W_I.

## Chart recap (v10 §4)

The parameters satisfy `0<r<s<1<w`, `0<c<1` and h>0. Put d0=1/w, β=(rsw)^-2 and u=rsw, so β=u^-2. Then:

- `P2=(t-r)²(t-s)²(t-w)²(t+β)`;
- `P3=(1+t)H_c²((t-1)²+ht)` with `H_c=t²-(c+1/c)t+1`;
- `F=(P2-P3)/t=E_B·Δrev`.

Here Δrev=2(w1t²+w3t+w2) has positive width coefficients, and E_B has roots x1<x2<x3 with x1x3<1<x2x3 and x2<1.

## Lemma 1 — two of the four orientations are automatic

- **d0 leads.** d0<x1 places it in cell 1, and the zone table admits only C4 lead there.
- **c lags.** c∈(x2,1) lies in cell 4. The C3 lead zone in that cell is (oL2,eL3), and in the reciprocal class 1<oL2 (v10 §1). So c<1 cannot lead.

Neither orientation is an extra filter.

## Lemma 2 — the r/s criterion

Both r and s lie in the C2 cell (y1,x2), where E_B<0 and O_B<0. At a C2 contact, y=−E_{C2}/(ωO_B), so sign(y)=sign(Eplus). Hence:

- r lags ⇔ Eplus(r)<0;
- s leads ⇔ Eplus(s)>0.

The C2 lag zone (eU1,oU1) lies below the C2 lead zone (eL2,oL2). So the order "r leads, s lags" is impossible, and the cases that remain are (lag,lag), (lag,lead) and (lead,lead).

Word I needs (lag,lead). By the alternation of v10 §3, with d0 leading and c lagging, (lag,lead) is exactly the alternating case. Equivalently: P2>0 on (r,s), so arg(C2/B) stays in (−π/2,π/2) there, and it must run from −π/2 at r to +π/2 at s. In other words, the curve C2/B on the imaginary axis crosses the POSITIVE real axis inside (r,s). This is the only orientation condition W_I adds beyond the cell chain.

## Lemma 3 — the exact coefficient window

**Coefficients of P2.** P2(0)=r²s²w²β=1. Since P2'(0)/P2(0) is the sum of 1/(0−ρ) over the roots ρ of P2:

- `[t]P2=1/β−2(1/r+1/s+1/w)`;
- `[t⁶]P2=β−2(r+s+w)`, since the sum of the roots is 2r+2s+2w−β.

**Coefficients of P3.** P3 is monic and palindromic with P3(0)=1. Summing the subleading coefficients of its monic factors gives

`[t⁶]P3=[t]P3=H3:=h−1−2(c+1/c)`.

**Conditions.** The positive width coefficients give F(0)=2w2>0. The leading coefficient of F is −2Aw1<0, with A=1/(x1x2x3), as in v10. Together:

`β−2(r+s+w)+1+2(c+1/c) < h < 1/β−2(1/r+1/s+1/w)+1+2(c+1/c)`. (WIN)

**Consequence A: the h-free form.** Put φ(x)=x−1/x and use u^-2−u²=−φ(u)(u+1/u). A nonempty (WIN) requires

`φ(u)(u+1/u)+2[φ(r)+φ(s)+φ(w)]>0`.

**Consequence B: the C4 contact is tiny.** Because h>0, the right side of (WIN) is positive. Using s<c<1, so that 2/c<2/s and 2c<2, gives u²>2/r+2/w−3. Then s<1 gives u<rw, so r²w²>2/r−3. Hence, when r<2/3,

`d0=1/w < r^{3/2}(2−3r)^{-1/2}`,

and when r≥2/3 no new bound follows. So the leading C4 contact sits at a scale no larger than r^{3/2}, below the first C2 contact.

These are necessary conditions only. The middle-width condition w3>0, the P1≥0 condition on (x1,y1), Lemma 2, and conditions 4–5 remain separate.

## Scope

This file neither decides W_I nor gives a point or emptiness, and it supplies no counterexample. The named ordinary inputs are Hermite–Biehler, the band facts of v10 §1, and the zone table with its phase rule. All of these are written candidates awaiting gates. This is not formal, kernel, human, family, cross-vendor, executable or novelty acceptance, not a GO, and not an edit of any frozen source. All permanent owner and parent findings remain, and the cutoff and deadline are unchanged.
