# Shor completion: seven forced actual atoms in the 12-tail branch

Owner **MathShor-2**, math-5. Native clock of exact synthetic controls: **Wed Oct 28 21:44:10 PDT 2026**.
**ALL-ORDER WRITTEN successor, conditional on the explicitly named common-prime T2 fibre theorem. No full completion/noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Strengthened actual-word conclusion

For any `a>=1`, suppose a finite UD factor-complete extension D of the literal Shor code has the SAME actual direct border factors

    n=165*2^(a+2),     |P|=55*2^a,     |Q|=12.

Q is EVEN. Then Q has exactly ONE actual tail in each of the twelve residue classes modulo24

    {0,1,2,6,7,8,12,13,14,18,19,20}.                         (1)

Consequently D must contain at least SEVEN distinct ACTUAL atoms `b^l a^j`, `l>=1`, whose tail residues modulo24 are

    {2,6,8,12,18,19,20}.                                       (2)

None of these seven is an old b-run tail anchor in the literal Shor code. This strengthens the separately pinned one-atom result; it does not construct any code or rule out the branch.

## 2. Why all three four-tail fibres are saturated

The named classical actual-border and Sands criteria and the [Łaba–Londner common-prime T2 corollary](https://arxiv.org/html/2106.14042v1) are the explicit imports in `frontier-20261028-even-tail-unified-fibres-v1.md`. That all-order predecessor gives 165 same-D fibre factorizations `P_i+Q_j=Z_(2^(a+2))`, where `i mod55`, `j mod3`, `|P_i|=2^a`, and every Q_j has four elements and the SAME allocated two-power cyclotomic spectrum.

The prior `frontier-20261028-even-tail-twelve-forced-atom-v1.md` proves from the old tails1,7,13 that this spectrum is exactly `Phi_4,Phi_8` and that ALL three Q_j fibres have even normalized residues. Each mask is therefore divisible by

    Phi_4(X) Phi_8(X) = 1+X^2+X^4+X^6.

After folding modulo `X^8-1`, an even polynomial of total weight4 divisible by this degree6 polynomial is exactly the displayed polynomial. So each Q_j contains precisely one normalized residue in each of `{0,2,4,6} mod8`. Mapping back by `q=j+3v` gives exactly (1); the three mod3 classes are disjoint and |Q|=12. Removing old tail residues `{0,1,7,13,14}` leaves exactly the seven distinct actual words in (2).

## 3. Additional head-fibre constraint

For any fixed i, Q_1 contains differences2 and4 in its normalized `Z_(2^(a+2))` fibre. Sands applied to the SAME direct fibre tiling makes P_i avoid difference gcd2 and gcd4. Thus its normalized even elements all occupy a single residue mod8, and its normalized odd elements all occupy a single residue mod8: two distinct residues of the same parity would differ with gcd2 or4. The common spectrum also puts Phi_2 in P_i, so P_i has `2^(a-1)` elements of EACH parity.

For each old head `i in {0,3,8,11}` (all distinct modulo55), normalized0 is present. Therefore the even half of that head fibre is specifically `0 mod8`, or actual heads `p==i mod440`; the odd half occupies one as-yet-unspecified odd normalized class mod8. No claim is made that the odd choices agree across different fibres or that the complete code exists.

## 4. Controls and limits

`frontier-20261028-even-tail-twelve-saturation-check.py`, SHA256 `df63a592af2cd3ed104d129bf7f1ba9f86c2cdb02ccd698706075a5bfae2d09f` (12 LF, 638 bytes), checks the 12-class formula and direct synthetic two-power fibre tilings for k=3,...,8. These are controls, NOT Shor completions. The all-order argument is §§2–3, conditional on the named classical imports and written predecessor proofs; none has received independent scientific, human, formal, model-family or novelty acceptance.

The original unrestricted finite UD factor-completion/noncompletion problem remains OPEN.

**END OF TWELVE-TAIL SATURATION REFINEMENT.**
