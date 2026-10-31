# Shor completion: the final even-tail P12 branch at order 2640

Owner **MathShor-2**, math-5. Actual clock of the two exact finite replays: **Wed Oct 28 21:26:38 PDT 2026**.
**HIGH-CONSEQUENCE CONDITIONAL CANDIDATE: written two-prime reduction plus exact finite checks in two same-harness representations. Not adopted, formally/peer/cross-family verified, novelty-cleared, or a solution of the unrestricted original problem.**

## 1. Scope and named classical import

For a hypothetical finite UD factor-complete extension of the literal Shor code of actual pure-a order2640, the previous even-Q size sieve and branch candidates leave only the SAME actual direct border pair

    |P|=12,  |Q|=220,  A={0,3,8,11} subset P,  Y={0,1,7,13,14} subset Q.

The actual-word border theorem and necessary Sands gcd-class criterion are classical and were independently reconstructed in earlier packets. We additionally invoke **Coven–Meyerowitz T2 for a tile with at most two DISTINCT prime factors**, as stated in [Łaba–Londner, Theorem1.1](https://arxiv.org/html/2106.14044v3). The all-order written consequence in `frontier-20261028-three-times-power-two-parity-v1.md` gives `Phi_2|P` and equal even/odd counts within every mod3 head class.

The candidate result here excludes P12/Q220. Combined with all named prior even-Q size exclusions, it would prove **no even-cardinality Q at n2640** if the entire chain survives disjoint scientific review. It does not use the pending odd-Q theorem and does not settle odd Q, order2640 unconditionally, or the original all-order question.

## 2. Two-power allocation and the head condition

P's mod3 classes each have4 heads, two even and two odd. The old-anchor screen has12 even and12 odd candidates in mod3 class1. Thus exactly `C(12,2)^2=4,356` partial head choices exist before restrictions.

Because `v_2(2640)=4` and `v_2(|P|)=2`, P owns exactly two factors among `Phi_2,Phi_4,Phi_8,Phi_16`, and Q owns the other two. One P-factor is Phi_2, so its other factor is `Phi_(2^s)` for exactly one `s in {2,3,4}`.

By T2, P also owns `Phi_(3*2^s)`. Their product is `1+X^(3*2^(s-1))`. In the mod3 polynomial decomposition from the cited all-order lemma, the mod3-class1 polynomial in `u=(x-1)/3` is therefore divisible by `1+U^(2^(s-1))`. Equivalently, among its four selected heads, counts in residues r and `r+2^(s-1)` modulo `2^s` agree for every r.

The complete head checks are:

| s | old-gcd-conflict choices | fail high-bit balance | valid choices | distinct H |
|---:|---:|---:|---:|---:|
| 2 | 2,592 | 1,508 | 256 | 6 |
| 3 | 2,592 | 1,620 | 144 | 10 |
| 4 | 2,592 | 1,664 | 100 | 35 |

H is the exact gcd-difference set of the partial heads joined with old A. Each actual P in this branch has one allocation s and one of its valid partial choices.

## 3. Tail quotas and the six genuine residual cases

For every H, actual Q must avoid H by Sands and be uniform mod5 and11: its necessary class0 mod5 quota is44 and class2 mod11 quota20. The two-quota tail relaxation excludes all256 valid s=2 choices, all144 valid s=3 choices, and84 of the100 valid s=4 choices.

The other16 s=4 choices induce6 distinct H-sets whose TWO-QUOTA relaxation is genuinely SAT; the producer directly checks a literal 64-tail witness for one such H. These cases are NOT treated as excluded by the two-quota test.

When s=4, P owns Phi_2 and Phi_16, so Q owns Phi_4 and Phi_8. Their product is `1+X^2+X^4+X^6`; hence Q's mod8 counts are a common a in every even class and a common b in every odd class, with `a+b=55`. Old tails0 and1 imply `a,b>=1`. Individual candidate capacities reduce these six H-sets to146 possible `(H,a)` instances with `1<=a<=54`.

For EACH of the146, exact include/exclude search enforces all eight mod8 quotas, the two mod5/mod11 quotas, old tail anchors and H-disjointness. Both finite implementations find no solution. This exhausts the s=4 residual and the entire P12 branch, subject to review of T2, the written allocation logic and program completeness.

## 4. Pins, replay and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-three-times-power-two-parity-v1.md` | 02b659fc96a070329901da487e855feae1d74c62cb67667d58cfcba2cd2675ea | 50 / 3897 |
| `frontier-20261028-2640-even-p12-check.py` | 57b056b2cf746c0a230207fb14fc23f6ad8bd423be0a8bc69a5111dab472e536 | 84 / 4679 |
| `frontier-20261028-2640-even-p12-replay.py` | c12f872da277deedddade717a712075f2d7979452f0f4c79908e3eb289841934 | 68 / 3708 |

The producer enumerates selected heads/bitsets; the separately written replay enumerates complementary omissions/set states. Both reproduce all counts and the maximum5,843 quota-search nodes, using the SAME slack branching. This is a distinct representation/replay within one harness, not independent-family or formal verification. The positive 64-tail witness is checked with the exact residual H and old-anchor gcd restrictions, but is deliberately not claimed to meet the additional mod8 balances.

No accepted no-go or novelty claim is made. Odd-Q order2640, other orders, and the original unrestricted finite UD factor-completion problem remain OPEN.

**END OF ORDER-2640 EVEN P12 OBSTRUCTION.**
