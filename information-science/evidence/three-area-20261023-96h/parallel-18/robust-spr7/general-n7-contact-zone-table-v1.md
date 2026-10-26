# SPR7 general boxes — exact contact-zone table and the complete strict-degree-7 critical word list

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 21:53:23 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN STRUCTURAL THEOREM** for the GENERAL independent monic degree-7 box. A fresh gate is required. Only symbolic sign and order reasoning is used: no numeric trial, calculator, interpreter, eval, program, CAS, enumeration program, solver or replay. The word count below was obtained by hand with a stated combinatorial argument.

All three of my written-exactness majors remain permanent, as do every older finding and HOLD. Probes get zero credit. This is a structural refinement only. It does NOT exclude any general critical configuration, does not settle the book problem, and does not use any reciprocal hypothesis outside §5.

## 0. Statement

Let K be an ORIGINAL independent monic degree-7 box with every member strictly Hurwitz and with varying intervals in both parity blocks. Let b be a weak common numerator of EXACT degree 7. Weak means every pairing is ≥0, with b Hurwitz and b(0)>0. Suppose a positive annihilation in the full eight-coefficient space uses exactly eight positive-frequency contact nodes and no infinity node. Theorem J's alternative (A) with b(0)>0 is of this form. Its first-critical construction is in `information-science/robust-spr-interval-synthesis/work/theory.md`, which is historical ancestry and is not re-accepted here; the alternation rule actually used is derived in §3.

Then:

1. **Zone table.** Each positive weak contact lies in an explicit open interval between ACTUAL band endpoints. That interval is fixed by its minimizing corner and its lead/lag orientation, as listed in §2.
2. **Cell structure.** Number b's seven cells 1..7. Cell 1 admits only a LEAD contact, and cell 7 only a LAG contact. In each middle cell the lag zone lies entirely below the lead zone. Under the alternation of §3, each middle cell therefore carries at most one lag followed by at most one lead.
3. **Word list.** With alternating orientation, every eight-node configuration is an alternating 8-subsequence of the 12-letter string `+ - + - + - + - + - + -`. The 12 positions carry fixed (cell, corner, orientation) labels. There are exactly 54 such subsequences. Exactly 11 put four contacts on corner C1, which exceeds that corner's degree bound. **Exactly 43 words remain.**
4. **Reciprocal specialization.** For the reciprocal class with a palindromic target, take v10's four distinct orbits with no ω=1 contact. The reversal-symmetric choices compatible with the palindromic-corner bound are then EXACTLY the three words I, II, III of `reciprocal-class-exact-three-word-reduction-v10.md` (SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`, read together with its erratum-1, SHA256 `cd14290a4ab5aacc8452b79966beb2e8c87dbdecb2140100c53cf4d2c0bc93e1`). This is a second derivation of that classification from the general table, by the same author; it is not an independent review.

No word is shown empty or realized. Weak numerators of degree 6 (b(0)=0, or degree 6 with an infinity node) have different cells and are NOT treated here.

## 1. Bands, corner roots and target cells

The ACTUAL root bands strictly alternate. Independence of the blocks makes the member that pairs the extreme even and odd corner parts a box member; it is Hurwitz, so Hermite–Biehler gives, for example, eU1<oL1 and oU1<eL2:

`I_E1=[eL1,eU1]<I_O1=[oL1,oU1]<I_E2<I_O2<I_E3<I_O3`.

The extreme components for t>0 are attained at four ACTUAL Kharitonov-type corners. Their positive roots sit at band endpoints, because each extreme stays on its side of every member on each sign interval:

- `Eplus`: eU1, eL2, eU3;
- `Eminus`: eL1, eU2, eL3;
- `Oplus`: oU1, oL2, oU3;
- `Ominus`: oL1, oU2, oL3.

The corners are C1=(Eplus,Ominus), C2=(Eplus,Oplus), C3=(Eminus,Oplus), C4=(Eminus,Ominus).

For the strict target, write E_b(t) and O_b(t), where b(iω)=E_b+iωO_b and t=ω². Hermite–Biehler gives interlacing roots `x1<y1<x2<y2<x3<y3`, with E_b(0)>0 and O_b(0)>0. The seven open cells and their UNIQUE minimizers, with target quadrant index q, are:

| cell | interval | sign(E_b,O_b) | minimizer | q |
|---|---|---|---|---|
|1|(0,x1)|(+,+)|C4|0|
|2|(x1,y1)|(-,+)|C1|1|
|3|(y1,x2)|(-,-)|C2|2|
|4|(x2,y2)|(+,-)|C3|3|
|5|(y2,x3)|(+,+)|C4|4|
|6|(x3,y3)|(-,+)|C1|5|
|7|(y3,∞)|(-,-)|C2|6|

At a positive weak contact both components of b are nonzero, by the classical parity-variation derivative argument for boxes with varying intervals in both blocks. So contacts lie inside cells, where the minimizer is unique.

## 2. The zone table

At a contact, `a(iω)/b(iω)=iy` with y real and nonzero, and

`y=ωO_a/E_b=-E_a/(ωO_b)`.

y>0 is called LEAD (a ahead of b by π/2); y<0 is LAG. In each cell the signs of E_b and O_b turn the orientation into sign conditions on the corner components:

- C4: lead ⇔ Eminus<0 and Ominus>0; lag ⇔ Eminus>0 and Ominus<0.
- C1: lead ⇔ Eplus<0 and Ominus<0; lag ⇔ Eplus>0 and Ominus>0.
- C2: lead ⇔ Eplus>0 and Oplus<0; lag ⇔ Eplus<0 and Oplus>0.
- C3: lead ⇔ Eminus>0 and Oplus>0; lag ⇔ Eminus<0 and Oplus<0.

Intersect these with the sign intervals of §1. Then use the phase relation: the corner's own quadrant index is k=q+1 for a lead and k=q-1 for a lag. Here k is the number of the corner's component roots below t, and q is the target cell index. This assigns each zone to a unique cell:

| zone | corner, orientation | corner k | cell forced |
|---|---|---|---|
|(0,eL1)|C3 lead|0|q=-1: IMPOSSIBLE|
|(0,eU1)|C1 lag|0|2|
|(eL1,oL1)|C4 lead|1|1|
|(eU1,oU1)|C2 lag|1|3|
|(oL1,eL2)|C1 lead|2|2|
|(oU1,eU2)|C3 lag|2|4|
|(eL2,oL2)|C2 lead|3|3|
|(eU2,oU2)|C4 lag|3|5|
|(oL2,eL3)|C3 lead|4|4|
|(oU2,eU3)|C1 lag|4|6|
|(eL3,oL3)|C4 lead|5|5|
|(eU3,oU3)|C2 lag|5|7|
|(oL3,∞)|C1 lead|6|6|
|(oU3,∞)|C3 lag|6|q=7: IMPOSSIBLE|

Each intersection is a direct consequence of the strict band order. For example, C4 lead requires Eminus<0 on `(eL1,eU2)∪(eL3,∞)` and Ominus>0 on `(0,oL1)∪(oU2,oL3)`; the intersection is `(eL1,oL1)∪(eL3,oL3)`. Every other row is computed the same way. The phase relation holds because, for Hurwitz a and b, the continuous arg(a/b) stays in [-π/2,π/2] (weak positivity) and equals exactly ±π/2 at a contact. So the quadrant indices satisfy k=q±1 exactly; no residue is taken mod 4.

## 3. Cell consequences

Reading the table by cell:

- **cell1:** only C4 lead, zone (eL1,oL1);
- **cell2:** C1 lag in (0,eU1) BELOW C1 lead in (oL1,eL2);
- **cell3:** C2 lag in (eU1,oU1) BELOW C2 lead in (eL2,oL2);
- **cell4:** C3 lag in (oU1,eU2) BELOW C3 lead in (oL2,eL3);
- **cell5:** C4 lag in (eU2,oU2) BELOW C4 lead in (eL3,oL3);
- **cell6:** C1 lag in (oU2,eU3) BELOW C1 lead in (oL3,∞);
- **cell7:** only C2 lag, zone (eU3,oU3).

**Alternation, derived here.** Let mu_i>0 be the weights at nodes t_1<...<t_8 with minimizing members a_i. The functional c ↦ Σ mu_i P_{a_i,c}(t_i) vanishes for every real c of degree ≤7. Using even-only and odd-only c separately gives Σ mu_i E_{a_i}(t_i)p(t_i)=0 and Σ mu_i t_i O_{a_i}(t_i)p(t_i)=0 for every p of degree ≤3.

With eta_i=1/∏_{j≠i}(t_i−t_j), the divided-difference identity Σ eta_i r(t_i)=0 for deg r≤6 shows that the vectors (eta_i g(t_i)), deg g≤3, fill this 4-dimensional solution space. Hence mu_i E_{a_i}(t_i)=eta_i g(t_i) and mu_i t_i O_{a_i}(t_i)=eta_i h(t_i). The eight contacts give E_b g+O_b h=0 at eight nodes; this polynomial has degree ≤6, so E_b g=−O_b h identically. E_b and O_b are coprime of exact degree 3, so g=κO_b and h=−κE_b with real κ≠0.

Therefore y_i=−E_{a_i}(t_i)/(ω_i O_b(t_i))=−κ eta_i/(mu_i ω_i), whose sign is −sign(κ)(−1)^{8−i}. Orientation alternates in frequency order. This is the J1 rule, derived rather than imported; v10 §3 gives its own proof in the reciprocal case.

Contacts within one cell are consecutive in the full sequence, so each cell contributes at most "−+", at most "+" (cell 1) or at most "−" (cell 7). In particular C4's first-cell contact must LEAD and C2's last-cell contact must LAG. These are the first and last phase rules, now derived from the table rather than assumed.

## 4. The complete strict-degree-7 eight-node word list

Concatenate the maximal per-cell blocks:

`+ | − + | − + | − + | − + | − + | −`, with positions 1 to 12.

The labels are:

- position 1: C4 lead in cell 1;
- positions 2 and 3: C1 lag and C1 lead in cell 2;
- positions 4 and 5: C2 lag and C2 lead in cell 3;
- positions 6 and 7: C3 lag and C3 lead in cell 4;
- positions 8 and 9: C4 lag and C4 lead in cell 5;
- positions 10 and 11: C1 lag and C1 lead in cell 6;
- position 12: C2 lag in cell 7.

Any alternating eight-node configuration is an 8-subset whose consecutive chosen positions have ODD gaps.

**Count.** Drop four of the twelve positions. A drop pattern keeps alternation iff every interior run of dropped positions has EVEN length; runs at the two ends are unrestricted. The cases are:

- only end runs: 5 patterns;
- one interior run of length 2 and end runs summing to 2: 7·3=21;
- interior runs summing to 4 (one of length 4 in 7 places, or two of length 2 in C(7,2)=21 ways): 28.

**Total: 54.**

**Corner bound.** Each corner pairing has degree 7, with leading coefficient equal to b's positive leading coefficient and positive constant term b(0)a(0). Since it is ≥0, it has at most THREE positive double roots. C4 can occur only at {1,8,9}, C2 only at {4,5,12} and C3 only at {6,7}, so none of these can exceed its bound. C1 occupies {2,3,10,11}, and an 8-set containing all four violates the bound.

Count those sets. The chosen positions between 3 and 10 form a chain with an EVEN number j of intermediate points, because j+1 odd gaps sum to 7. Their total is j+[1 chosen]+[12 chosen]=4.

- j=4: there are 5 compositions of 7 into five odd parts.
- j=2 with both 1 and 12 chosen: there are 6 compositions of 7 into three odd parts.

That gives 11 excluded sets, so **43 admissible words remain.** No further general word is excluded here.

## 5. Reciprocal specialization — second proof of exactly three words

For the reciprocal class (A7=1, paired intervals) with a palindromic strict target, import v10's counting inputs: four distinct orbits and no ω=1 contact, via the 341LF interface. Reversal maps position p to 13−p and flips orientation. This matches the table: C4 at t corresponds to C2 at 1/t, C1 and C3 are fixed, cells are mapped j↔8−j, and cell 4 is self-paired with its lag at t and its lead at 1/t. So eight-node configurations are unions of four of the six pairs

`(1,12),(2,11),(3,10),(4,9),(5,8),(6,7)`.

The palindromic corner C1 has at most ONE contact orbit, because its real form is a monic cubic in V. This excludes any union using both (2,11) and (3,10). Checking all fifteen 4-pair unions for odd gaps leaves:

- `{1,4,5,6,7,8,9,12}` = word I (C4, C2 lag, C2 lead, C3);
- `{3,4,5,6,7,8,9,10}` = word II (C1 lead, C2 lag, C2 lead, C3);
- `{1,2,5,6,7,8,11,12}` = word III (C4, C1 lag, C2 lead, C3).

The three other alternating unions all use both C1 orbits. This rederives v10's three-word classification from the general table. It is a same-author consistency check, not an independent review.

## 6. Scope and assurance

These are necessary zone and order conditions on critical contacts. No general word is shown empty, no reciprocal word is decided, and no realization is supplied. Not covered, and each needing its own cell table: degree-6 weak numerators, Theorem J's alternative (B), and weak b with imaginary-axis roots or b(0)=0.

The ordinary named inputs are:

- degree-7 Hermite–Biehler;
- Kharitonov corner extremality and the fact that its roots sit at band endpoints;
- monotone continuous phase of Hurwitz polynomials;
- the weak-positive-real phase interval;
- elementary composition counting.

Every specialized step is written above. Old Lemma L and its census are not re-accepted; this table refines them by using corner-specific band endpoints.

This is not formal, kernel, human, configured-family, cross-vendor, executable, triple-finite, novelty, SOTA or publication acceptance. It is not a universal SPR7 verdict, a new GO, an edit of any shared or frozen source, a deadline reset or a round closeout. Every process finding remains.
