# SPR7 general boxes — exact width monotonicity at contacts (companion to the 43/13/8 word lists)

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:47:30 PDT 2026**. InfoSPR7/info-2. **NEW WRITTEN LEMMA CANDIDATE.** It generalizes the reciprocal file `reciprocal-width-monotonicity-contact-values-v1.md` (SHA256 `7a56acab43ac77e8eac5386aba6b6f9297f2100ad9e3f8b7758672c579a12ab3`) to every ORIGINAL independent monic degree-7 box. It is a tool for the word lists of `general-n7-contact-zone-table-v1.md` (SHA256 `a05d332de4fac12f2416a4758c34f4e2fb380163e76fa7f17eb6313fadf4fce1`) and `general-n7-degree-six-zone-words-v1.md` (SHA256 `376484d242d7cce67e16f7a29ed2fe7f17f4d765461aaae7df2c4b8c3b033472`). Neither file is edited.

The work is symbolic and exact. No numeric instance, interpreter, eval, program, CAS or GO is used.

## 1. Width polynomials

Write E_a(t)=a7−a5t+a3t²−a1t³ and O_a(t)=a6−a4t+a2t²−t³, with intervals [l_k,u_k] and widths δ_k=u_k−l_k≥0. Then

- `ΔE:=Eplus−Eminus=δ7+δ5t+δ3t²+δ1t³`;
- `ΔO:=Oplus−Ominus=δ6+δ4t+δ2t²`.

Both have nonnegative coefficients. The hypothesis "both blocks vary" means each has at least one positive coefficient.

## 2. Exact pairing relations

For a numerator b, write P_j=P_{C_j,b}, with C1=(Eplus,Ominus), C2=(Eplus,Oplus), C3=(Eminus,Oplus) and C4=(Eminus,Ominus). Then

- `P2−P3=P1−P4=ΔE·E_b`;
- `P2−P1=P3−P4=tΔO·O_b`;
- `P1+P3=P2+P4`.

Each identity is a direct expansion of the pairing P=E_aE_b+tO_aO_b in the two corner blocks.

## 3. Contact values

Let τ>0 be a contact of corner j inside one of its own cells, so E_b(τ)O_b(τ)≠0. Then:

| corner at τ | ΔE(τ) | ΔO(τ) |
|---|---|---|
| C1 (P1=0) | −P4/E_b | P2/(τO_b) |
| C2 (P2=0) | −P3/E_b | −P1/(τO_b) |
| C3 (P3=0) | P2/E_b | −P4/(τO_b) |
| C4 (P4=0) | P1/E_b | P3/(τO_b) |

Every entry is ≥0, consistent with the cell signs of (E_b,O_b) from the zone table. For example, C2 cells have E_b<0 and O_b<0.

## 4. Lemma — the two monotonicity windows

Let 0<p<q. Since ΔE has nonnegative coefficients and degree ≤3, and ΔO has nonnegative coefficients and degree ≤2:

`ΔE(p) ≤ ΔE(q) ≤ (q/p)³ΔE(p)`,

`ΔO(p) ≤ ΔO(q) ≤ (q/p)²ΔO(p)`.

The inequalities are strict whenever the relevant polynomial has two or more positive coefficients. Both windows also hold with p=0 on their left sides, where ΔE(0)=δ7 and ΔO(0)=δ6.

*Proof.* A polynomial with nonnegative coefficients is nondecreasing on [0,∞). Dividing it by t^(deg) gives a nonincreasing function on (0,∞). ∎

## 5. Use

Any two contacts of a word, at any corners, give four explicit exact inequalities via the table in §3. All of them are NECESSARY for a first-critical configuration on a box with nonnegative widths.

In the reciprocal class, ΔE=tΔrev and δ7=0. This recovers the reciprocal file, whose window exponent is 2 because ΔE/t is quadratic.

No general word is decided here; this is a tool. This is not formal, kernel, human, family, cross-vendor, executable or novelty acceptance, not a GO, and not a universal verdict. All permanent owner and parent findings remain; the cutoff and deadline are unchanged.
