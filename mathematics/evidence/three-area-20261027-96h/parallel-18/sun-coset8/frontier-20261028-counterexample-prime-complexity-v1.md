# Conditional prime complexity of an arbitrary-group Sun8 counterexample

**Status: WRITTEN-checked-in-kernel, CONDITIONAL, UNREVIEWED.** Assume the named all-group Sun7 statement, the prior finite-core/R8/normal-section reduction, the Jones k=0 statement and the unreviewed written A7 and GL3(2) exceptional-case arguments specified below. If arbitrary-group Sun8 fails, a finite nonabelian simple composition factor S of a finite quotient of a counterexample has actual eight-coset P7 data and satisfies

\[7\mid |S|,\qquad \omega(|S|/7)\ge8,\qquad |S|\ge67{,}897{,}830.\]

If in addition 7 divides |S| exactly once, then |S|≥223,092,870. Here ω counts distinct prime divisors. This is a **necessary** condition on one actual finite simple section, not a counterexample, a classification of all simple groups, a proof of Sun8, an infinitude/novelty result or a claim that either order is attainable.

## 1. Named inputs and prior work

Before earlier affected candidates and successors, read the complete overlays in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The A7 no-seven-index assertion is false; it is not used.

- The all-group Sun7 statement is imported only at the written-composition/errata scope of `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md`, SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`. Its full proof DAG is not independently replayed here.
- The finite-core, R8 and actual-P7 normal-section descent are **prior work**, recorded in `institute/runs/three-area-2026-10-23-96h/sun8-normal-section-parent-v1.md`, SHA `8a8480e2d66f0098fc80ae2960bafcdab36a9976e80b671ddee01c5048fec475`, §§1–3, and the older R8 source SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`. The parent record reports same-harness written support, not a human, Lean or full Sun7-DAG replay. In particular it states a necessary composition-factor direction for a fixed original group; we do not infer a converse lift back to that fixed group or claim discovery of the descent.
- The prime-support exclusion for every finite nonabelian simple S with 7∤|S| or ω(|S|/7)≤7 is the **unreviewed** candidate `frontier-20261028-simple-seven-prime-support-v1.md` SHA `815c9e2374a96858f7bfd609aca9f592f293fb14a1822e774333dc41c4eb2faf`. It uses Jones Theorem 1.2(k=0), the separately unreviewed written GL3(2) Fano proof and the A7 proof within that packet. Jones's classification proof is not replayed and its source states CFSG dependence. The simple P7 criterion is not presumed adopted.

No old hold or process finding is rehabilitated. The author is nonblind, including separately disclosed incidental cross-topic display, and claims no novel R8 or simple-reduction credit.

## 2. The conditional composition

Assume Sun8 fails for some group. The prior finite-core construction maps an eight-coset counterconfiguration to a finite quotient without changing its subgroup indices or disjointness. The inherited all-group Sun7 statement and prior R8 reduction make its eight index gcds all exactly 7. The named normal-section descent then supplies an actual P7 configuration in a finite nonabelian simple composition factor S of that quotient. In particular 7 divides |S|.

If ω(|S|/7) were at most 7, the named unreviewed simple-family criterion would exclude that very actual P7 configuration, contradiction. Hence ω(|S|/7)≥8. No assumption of distinct cofactor values equal to 1 is made; the A7 and GL3(2) index-7 exceptions are treated in the named criterion, not silently excluded.

## 3. Absolute arithmetic bounds

The least product of eight distinct primes is

\[2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19=9{,}699{,}690.\]

Thus |S|/7 is at least this product and |S|≥67,897,830. If v_7(|S|)=1, then 7 is not among the prime divisors of |S|/7; the least product of eight distinct primes excluding 7 is

\[2\cdot3\cdot5\cdot11\cdot13\cdot17\cdot19\cdot23=31{,}870{,}410,\]

so |S|≥223,092,870. The two integer products and multiplications by 7 were checked exactly in the author's eval kernel; no group of either order was constructed or tested.

## 4. Review boundary

A disjoint reviewer must independently verify the exact hypotheses and nonretroactive scope of the old Sun7/R8/descent chain, the named source-dependent simple P7 exclusion including repeated index-7 vertices, and both prime-product inequalities. This packet does not accept any constituent proof, alter earlier reviews, imply a quotient converse for the original group, settle larger prime-support families, or establish formal/human/priority clearance.
