# Shor completion: graded outside-head versus multi-b border tradeoff

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:47:30 PDT 2026**.
**WRITTEN same-code all-order necessary bounds and finite synthetic controls. No completion, unrestricted noncompletion, formal verification or novelty claim.**

## 1. Definitions and main bound

Let D be any finite UD factor-complete extension of the literal Shor code, with actual atom `a^n`, and set `A={0,3,8,11}`. Let B be its actual one-b atoms and let `N_out` count those with heads outside A modulo n. Define the actual border

    P={i mod n : a^i b^k in D for some k>=1}

and let M be the **number of actual atoms** `a^i b^k in D` with `k>=2`. Every such atom has a head residue outside A, and distinct such atoms have distinct head residues, by the proof below.

For any proved lower bound `|P|>=L` and any integer `m` satisfying `0<=m<L-4`,

    M <= m  ==>  N_out >= n - 4 floor(n/(L-m)).                (1)

The exact same D supplies every quantity in (1). In particular the predecessor `frontier-20261028-eight-head-border-obstruction-v1.md` gives `L=8` for **every feasible n**, yielding

| Assumption | Necessary lower bound for N_out |
|---|---|
| M=0 | n-4 floor(n/8) |
| M<=1 | n-4 floor(n/7) |
| M<=2 | n-4 floor(n/6) |
| M<=3 | n-4 floor(n/5) |

Contrapositively, e.g. if `N_out<n-4 floor(n/6)` then at least three actual multi-b border atoms with distinct new head residues are necessary. This refines the earlier two-way small-outside/four-atom alternative, without claiming either branch exists.

## 2. Proof: actual border atoms cannot repeat a head residue

Suppose two DISTINCT actual atoms `a^i b^k` and `a^h b^l` have `i==h mod n`. The literal b is an atom of D, and so is `a^n`. Prefix each of the two atoms by enough copies of `a^n` to make the initial a-exponents agree, and suffix each by enough copies of the atom b to make the lengths of the b-runs agree. The two raw words are identical. Their actual atom lists differ: they contain the two distinct named border atoms, except for the possible border atom b itself, which likewise differs from any other such atom. This contradicts UD. Hence **each element of P is realized by exactly one actual `a^*b^+` atom**.

In particular the four actual old atoms `b,a^3b,a^8b,a^11b` occupy all four A-residues, so every multi-b border atom has a head outside A. Let `P_1` consist of residues realized by actual one-b atoms literally of the form `a^i b` (tail exponent exactly zero). Uniqueness gives

    |P_1|=|P|-M.

The one-b residue column `I_0` from the zero-column predecessor includes all of P_1, and might include additional one-b atoms whose tail exponent is a positive multiple of n. Hence, **without identifying `I_0` and P_1**,

    c_0=|I_0| >= |P_1| = |P|-M >= L-m.

The predecessor's exact packing inequality `N_out >= n-4 floor(n/c_0)` then gives (1). It uses the directness of each one-b row against the actual zero-tail residue column and `|B|=n`; no multib atom is treated as a one-b residue pair.

## 3. Stronger numerical thresholds at n=1320

At n=1320 the same border theorem plus the `v_2(n)=3` prime-power filter and the divisibility `|P| divides 1320` force `|P|>=10`; this does NOT itself exclude that order. Taking L=10 in (1):

| Assumption | Necessary N_out |
|---|---:|
| M=0 | >=792 |
| M<=1 | >=736 |
| M<=2 | >=660 |
| M<=3 | >=568 |
| M<=4 | >=440 |
| M<=5 | >=264 |

For instance, a hypothetical completion with `N_out<264` must contain at least **six** actual multi-b border atoms with distinct head residues outside A. The stronger thresholds rely on the same unreviewed border theorem and Fourier argument, and are conditional on an actual n=1320 completion.

## 4. Checks and status

`frontier-20261028-border-atom-uniqueness-check.py`, SHA256 `07e0698022202f3560c9c643c7b394a63c68702c3f12098b1fa4cf737d7e8aac` (20 LF, 926 bytes), independently enumerated synthetic codes `{a^n,b,u,v}` with `u,v` ranging over distinct actual words `a^i b^k`, `0<=i<2n`, `1<=k<=3`. It uses the Sardinas–Patterson function from the pinned zero-column control and found:

| n | codes | UD | repeated-border-head codes, all rejected |
|---|---:|---:|---:|
| 2 | 55 | 0 | 55 |
| 3 | 136 | 36 | 100 |
| 4 | 253 | 108 | 145 |
| 5 | 406 | 216 | 190 |
| 6 | 595 | 360 | 235 |

These finite checks do not involve a Shor completion or establish the all-order bound. Arithmetic in the 1320 table was checked exactly with integers. The border factorization is prior literature; these deductions have not received novelty, peer, formal/kernel or independent-family review. The original finite UD factor-completion/noncompletion problem remains OPEN.

**END OF GRADED MULTI-B BORDER TRADEOFF.**
