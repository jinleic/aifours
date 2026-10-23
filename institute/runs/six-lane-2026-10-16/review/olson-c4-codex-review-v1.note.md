VERDICT: ACCEPT-WITH-FIXES

All four SHA-256 hashes match.

| File, under `inverse-run-count/mixdef-high/c4/` | Verdict |
|---|---|
| `proof-NOBCplus-r3.md` | ACCEPT |
| `proof-KB0-r1.md` | ACCEPT-WITH-FIXES |
| `proof-IND-r1.md` | ACCEPT-WITH-FIXES |
| `proof-INDstar-r1.md` | ACCEPT |

FATAL: none. MAJOR: none.

- **MINOR — `proof-KB0-r1.md:15`:** cites the unfrozen, superseded `proof-NOBCplus-r2.md`, absent from S. Replace with `proof-NOBCplus-r3.md`.
- **MINOR — `proof-IND-r1.md:132`:** exceeding the corollary’s upper bound does **not** imply \(j_1>\delta\). At \((p,k_B)=(17,9)\), \(j_1=7<8=\delta\), although \(9>(3p-7)/5\). Replace the opening with: “In the regime \(j_1>\delta\), the seed is \(s=j_1\)…”. The theorem and corollary are unaffected.

## What is established

- **NOBC+:** the false universal DOB(p) lifting obstruction is explicitly withdrawn. Lemma D’s equivalence holds throughout its stated domain, including the small-prime boundaries: beyond W-ALL, aligned pairs certify exactly when \(p\equiv1\pmod6\) and \(k_B=(p+5)/3\). On DOB*, singleton extension and the specified extended certification produce no larger patterns. The resulting singleton-only lifted system admits \(x=0\); this is a feasibility witness for that system.
- **KB0:** every \(W(p,(p+5)/3)\) is excluded for primes \(p\equiv1\pmod6,\ p\ge13\). The anti triples, size induction, complementary pin \(P,P^c\), and exceptional defect cases all work uniformly. No uncertified anti pair is used. The pin gives \(X_{[k]}=p\).
- **IND:** Steps 1–4 establish the theorem under its stated arithmetic hypotheses. The corollary holds for every prime \(p\ge11\) and integer
  \[
  \frac{3p+1}{7}\le k_B\le\frac{3p-7}{5}.
  \]
  The difference seed, induction over subsets of \(T\), balanced-profile reduction, and contradiction at sizes \(\delta\) and \(j_1\) are valid.
- **IND\*:** the stated certificate applies to NMH words with \(R\le2p-3\), arbitrary anti positions and excess, and an available independent set \(T\). Its failure alternatives and joint hypotheses are sufficient. The r1 uniqueness fix works: the singleton lambda sum is actually at least \(4\), making the canonical interval shorter than \(p\). No hidden (H) hypothesis is used.

Independent in-memory checks confirmed all KB0 certification types through \(p=199\), the complete W(13,6) certification calculation, every corollary-band hypothesis through \(p=401\), and the reported IND* parameter counts \(2623/3221\) and \(3947/7264\).

## Imported/unchecked

Corrected Lemma H, the BC Claim, Lemma L, and accepted c3 results remain imports. Their foundational WAS/GR/reduction proofs were not re-refereed. Historical random replays and c3 sample-coverage claims were not independently replayed.

Nothing here proves NMH(p), MIX_DEF_HIGH(p), RUNS(p), INV, or ordered Olson for \(D_{2p}\).