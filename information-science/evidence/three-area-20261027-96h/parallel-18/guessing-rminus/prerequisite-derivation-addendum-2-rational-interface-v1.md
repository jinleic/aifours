# Addendum 2 — exact rational strict-gain certificate interface and empty-graph erratum

InfoGuessingRminus-2. Actual preceding native clock: **Tue Oct 27 15:00:32 PDT 2026**. AUTHOR-WRITTEN UNREVIEWED, no computation or numeric probe. Frozen v1 and Addendum 1 remain unchanged. This arithmetic reformulation is an assurance interface, **not another claimed scientific advance or original bound improvement**.

## 1. Explicit degenerate-graph erratum to v1

The phrases "EVERY finite loopless digraph" in v1's max-marginal formulas require **a nonempty vertex set**. If V is empty, max_v H(X_v) is undefined. Handle that separate case directly: there is one empty word and its guessing number is zero at every alphabet. No max-marginal ratio is asserted in that case. All statements for R-minus (ten vertices) and all proofs for nonempty finite loopless digraphs are unchanged.

## 2. All-integer certificate at any positive rational threshold

Let G be any fixed nonempty finite loopless digraph with its original neighbourhoods. Let a>=0 and b>=1 be integers. Let S be any finite nonempty FD-consistent support, and give each s in S a positive integer weight k_s. Set

`D=sum_s k_s`,
`m_{v,z}=sum_{s:s_v=z} k_s`.

The law P(s)=k_s/D satisfies the same original FDs. Zero marginal counts may be omitted; use the empty-product and 0^0=1 conventions if they are retained. Its entropies are

`D H(P)=D log D - sum_s k_s log k_s`,
`D H(P_v)=D log D - sum_z m_{v,z} log m_{v,z}`.

Therefore `bH(P)>a max_v H(P_v)` is equivalent to the following EXACT POSITIVE-INTEGER comparison for EVERY vertex v:

`D^(bD) product_z m_{v,z}^{a m_{v,z}} > D^(aD) product_s k_s^{b k_s}`.   (C_v)

This follows by taking the logarithm of the ratio of the two positive sides; it is precisely D[bH(P)-aH(P_v)]. No rounded logarithm or floating comparison is a premise. Both sides are finite integers. No k_s, D or product value is selected or evaluated here.

## 3. Original actual-word caller and converse

If (C_v) holds for all v and a>0, the strict homogeneous gap is positive and h=max_v H(P_v)>0: otherwise all coordinates are constant and H(P)=0. The type-class construction of v1 then supplies an actual finite common alphabet q and original full-domain decoders with

`|W|^b > q^a`.

The exact integer products certify the entropy gap; they do NOT by themselves print the finite decoder table. v1 supplies its existential construction and a sufficient blocklength condition. Execution, table generation and independent finite-certificate replay still require their separate gates and are not authorized here.

Conversely, suppose an actual original q-alphabet strategy has `|W|^b>q^a`. Its W is nonempty and FD-consistent. Give each s in W weight one. Then H(P)=log|W| and every H(P_v)<=log q, so `bH(P)>aH(P_v)` for every v. Thus all (C_v) hold.

A general finite FD law with a strict real entropy gap can first be approximated by a rational law on the SAME support, using continuity as proved in v1. Clearing its probability denominators gives the positive integer weights above. Hence, at each positive rational threshold a/b, existence of an original strict-gain code, existence of a finite FD law with the strict homogeneous entropy gap, and existence of this all-vertex integer certificate are equivalent.

In particular, the literal original lower-target exponents may be substituted without choosing a diagnostic parameter. This is the target statement itself, not a numerical test. No such support or weights are supplied in this work.

## 4. Exact limitation for the proposed upper-bound line

The equivalent universal upper assertion is that EVERY finite original-FD support and EVERY positive integer weighting fails the strict system (C_v). Proving failure only for a chosen support, a fixed alphabet, bounded denominator or a field/quasigroup/architecture family does not establish that universal assertion.

Thus eliminating numerical entropy evaluation is not a new upper bound. The still-missing ingredient is a genuinely unrestricted original-FD inequality, or an actual finite support/weight certificate with strict gain. The old undefined Phi-to-gain implication remains NONINPUT/NR; no old source or candidate is revived by these formulas.

Inputs: released definitions, v1's explicitly proved coupling lemmas and ordinary finite entropy/log identities. No excluded guide, external theorem, selected example or scientific program. Source-scope deviation MINOR on the prior read remains recorded and its over-displayed fragments unused/unrecovered.
