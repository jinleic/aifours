# Locally regular bands and seminormal bands coincide

**NEW AUTHOR WRITTEN CANDIDATE with exact same-author replay; UNREVIEWED and UNADOPTED.** Native check-start observation **Wed Oct 28 20:51:51 PDT 2026**. This pays the previously open band-variety identity direction using two explicit local regular-band substitutions. It is NOT by itself a proof that every original source embeds, an adoption of any historical STOPped material, or a resolution of all D1–D4 printed-product interfaces. The elementary band-content lemma below uses the explicitly named classical Green–Rees free-band/D-class fact.

## 1. Exact statement

For any nonempty band B, the following are equivalent:

1. Every local monoid eBe is a regular band (`xyxzx=xyzx`).
2. B is seminormal in Billhardt's 1998 convention:

   `a b c d a = a b c a c d a` for all a,b,c,d∈B.         (SN)

Thus the registered locally-regular band variety V and the printed seminormal band variety SN are the SAME variety, at the exact ordinary band-identity definitions. The other source-class, actor, product-convention and printed-question interfaces are not asserted here.

**2⇒1:** in any local monoid eBe, substitute e for c in (SN); it becomes `a b d a=a b a d a`, the regular-band identity.

The remaining direction is given explicitly in §§2–4.

## 2. A named elementary band-content lemma

For words X,Y,Z in letters of a band, if `content(Y)⊆content(X)=content(Z)`, then

`X Y Z = X Z`.                                             (C)

Here equality is an identity in ALL bands. A standard proof uses the Green–Rees theorem: in a free band, D-classes are determined by content, and every D-class is a rectangular band. X, XY and Z have the same content, hence lie in one rectangular D-class. There `X(XY)X=X`, so X and XY have the same R-coordinate, and `(XY)Z=XZ`. The free universal property transfers the word identity to every band. The Green–Rees characterization is stated in [Cirpons, *Computing in Free Bands*](https://www-users.york.ac.uk/~varg1/2023_11_08_York_Semigroups_Computing_in_Free_Bands-corrected.pdf), slides10–11; it is a named classical input, not inferred from the finite control.

The identities `WW=W` and (C) are the only band equalities used in the reduction traces below. No global regular-band identity, commutativity or cancellation is assumed.

## 3. Two local-regular substitutions

Write, for any band words e,A,B,C,

`X=e A e`, `Y=e B e`, `Z=e C e`,
`L(e,A,B,C)=X Y X Z X`, `R(e,A,B,C)=X Y Z X`.

Every word e is idempotent, so X,Y,Z are actual elements of eBe. If B is locally regular then `L=R`. We apply it TWICE:

| Instance | e | A | B | C | common left context | common right context |
|---|---|---|---|---|---|---|
| I | c | a | b | da | ab | da |
| II | bc | a | ac | d | a | da |

Only associative concatenation is used for the contexts. The four exact reductions, detailed in §4, are

`ab L(c,a,b,da) da  =  abcacda`,
`ab R(c,a,b,da) da  =  abcacbcda`,
`a L(bc,a,ac,d) da   =  abcda`,
`a R(bc,a,ac,d) da   =  abcacbcda`.

The two local equalities therefore give `abcacda=abcacbcda=abcda`, which is (SN). No case distinction, selected small example or target-equivalence premise is used.

## 4. Literal rewrite traces

Each arrow marked implicitly below is deletion of a displayed consecutive square WW, except the TWO explicitly labeled (C) steps. The source and target strings are literal; all contexts are included.

**I, left:**

```text
abcaccbccaccdaccacda
→ abcacbccaccdaccacda
→ abcacbccacdaccacda
→ abcacbccacda
→ abcacbcacda
→ abcacda
```

**I, right:**

```text
abcaccbccdaccacda
→ abcacbccdaccacda
→ abcacbcdaccacda
→ abcacbcdacacda
→ abcacbcdacda
→ abcacbcda
```

**II, left:**

```text
abcabcbcacbcbcabcbcdbcbcabcda
→ abcabcbcacbcabcbcdbcbcabcda
→ abcabcbcabcbcdbcbcabcda
→ abcabcbcabcdbcbcabcda
→ abcabcbcabcda
→ abcabcda
→ abcda
```

**II, right:**

```text
abcabcbcacbcbcdbcbcabcda
→ abcbcacbcbcdbcbcabcda
→ abcacbcbcdbcbcabcda
→ abcacbcdbcbcabcda
→ abcacbcdbcabcda
→ abcacbcdcabcda       (C)
→ abcacbcdabcda        (C)
→ abcacbcda
```

For the first (C) step, the replaced factor is `X Y Z` with `X=abcacbcd`, `Y=b`, `Z=cabcd`, followed by context a. For the second, `X=abcacbcd`, `Y=c`, `Z=abcd`, again followed by a. In each, X and Z contain exactly {a,b,c,d}, and Y's content is a subset. The final step deletes the square `(bcda)(bcda)`.

## 5. Exact replay, consequence and limits

`frontier-20261028-local-seminormal-proof-replay-v1.py`, SHA `29a4157f635a6576dee7ee3ea1f422704981bd25b6463eb13c192f29dc600bc4`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 20:51:51 PDT 2026**, exit0. It independently reconstructs both local substitutions and contexts, validates every trace transition as a square contraction or a valid (C) application, and compares Green–Rees free-band signatures at each step:

```text
PASS two local-regular identity instances with exact contexts, four band-rewrite traces
square contractions=21 content absorptions=2
CONTROL target words are distinct in the unrestricted free band; bad rewrite rejected
```

The bounded C++ congruence search `frontier-20261028-local-seminormal-congruence-search-v1.cpp`, SHA `08631a33bf942c0d8bd23dcb68bea408199626ae097511378c85889db8f6efab`, generated the candidate; a shorter-substitution-only search was inconclusive. The replay above does NOT trust the search's union-find or trace construction. Both programs are same-author artifacts; neither is an independent proof review or formal/kernel certificate.

If reviewed and accepted, this equality removes the specific **band-variety** uncertainty in `frontier-20261028-seminormal-original-variety-barrier-v1.md`, SHA `59570e93d39ec4e9905b50b2c087516f0d3e21533a711a175d979358060e1a7a`: a locally regular nonseminormal BAND counterexample cannot exist. It also means any separately established locally-regular-band physical host is automatically seminormal at the named identity. It does NOT establish any unconstructed host, canonical SEP/R/L, the complete printed/registered equivalence, the attributed Billhardt–Szendrei embedding assertion, or a general solution of Q1/Q2. Independent written replay and source/priority review are required before adoption.
