# A parity/3 collision among saturated length-seven windows

**Status: WRITTEN necessary-condition candidate, conditional on the unreviewed t=41 saturation/quotient inputs; not an A_(r+41) P7 exclusion.** Under the hypothetical t=41 direct-P7 pattern of `frontier-20261028-alternating-saturated-seven-frontier-v1.md` SHA `82cb25f5f1ab52d928f3fc3ee6fba73ac2147b7aa0c00833aee1b1618dc91fee`, at most **four** of the six distinguished r-free seven-cell windows can have length exactly 7. In particular the five-length-7 7-local model in that packet cannot extend to a P7 pattern, even before using any primes greater than 3. It remains a valid **7-local** model, not a claimed subgroup realization.

The public A_r classification, exact c|u! quotient and general factorial incompatibility used to reach saturation remain named, unreviewed inputs in the cited frontier. The writer's nonblind cross-topic exposure is recorded there; no such excerpt is used and no historical hold is modified. No full t=41 conclusion or historical novelty is claimed.

## Proof

All seven hypothetical subgroup indices are divisible by 7 and at most one is even. For a distinguished length-7 window ending at j, its full binomial factor is B_j=C(r+j,7) and divides the corresponding index. The endpoints of distinct labels are distinct and lie in {7,…,41}.

In characteristic 2, (1+X)^8=1+X^8. Therefore C(n,7) is odd exactly when n≡7 mod 8. Consequently every odd length-7 binomial in the pattern has endpoint j≡7−r mod 8.

In characteristic 3, (1+X)^9=1+X^9. Hence C(n,7) is not divisible by 3 exactly when n mod 9 is 7 or 8: for residues 0,…,6 the coefficient is zero, while C(7,7)=1 and C(8,7)=8≡2.

Suppose at least five distinguished windows have length 7. At least four of their indices are odd, so their B_j are odd. Their four endpoints are distinct and congruent modulo 8. Any nonzero difference between them is a multiple of 8 of magnitude at most 34, hence cannot be divisible by 9. The four numbers r+j have distinct residues modulo 9. Only two residues allow B_j to be 3-free, so at least two of these four binomials are divisible by 3. Their subgroup indices are both divisible by 3 and 7, giving gcd≥21, contradiction. Thus at most four distinguished windows have length 7.

The six distinguished windows are still disjoint, their lengths are in 1,…,13, at least one has length≤6, and at most one index may have 7-valuation≥2. The remaining configurations with at least two lengths different from 7 require further work; this lemma does not assert they are impossible.

## Actual control

`frontier-20261028-alternating-length7-check.py`, SHA-256 `67c76eaeadd681f041397fc3d59cb5fb8f3bcef5b60e2adc5740366213e11706`, 21 LF / 732 bytes, ran at 19:42:10 PDT on 2026-10-28. It used exact integers to check 480 mod-72/endpoint cases, including 48 all-odd cases, and confirmed the stated 3-collision. This finite control is not a proof of the source, saturation, quotient, actual subgroup existence, or an independent review. Review must check the mod-8/mod-9 coefficient identities and the endpoint-difference bound.
