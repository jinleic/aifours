# Shor completion: an all-order eight-tail border obstruction

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:53:53 PDT 2026**.
**WRITTEN same-code all-order necessary theorem with exact symbolic checks; not an unrestricted completion/no-go, formal proof, peer acceptance or novelty claim.**

## 1. The complementary theorem

For any finite UD factor-complete extension D of the literal Shor code, its actual pure-a atom `a^n` and actual multi-b-permitting border sets satisfy

    P={i mod n:a^i b^k in D, k>=1},
    Q={j mod n:b^l a^j in D, l>=1},
    P+Q is a direct tiling of Z_n,  n>=26,
    {0,3,8,11} subset P,  Y={0,1,7,13,14} subset Q.

The independent actual-word reconstruction and the previous elementary `|Q|>=6` proof are in `frontier-20261028-six-head-border-factorization-v1.md`. **The new all-order assertion is `|Q|>=8`: both the six-tail and seven-tail alternatives are impossible.** There are no valuation restrictions. Combined with `frontier-20261028-eight-head-border-obstruction-v1.md`, every completion would have BOTH `|P|>=8` and `|Q|>=8`.

The direct-tiling result is known prior literature; this particular anchor deduction is not novelty-cleared. Both borders below come from the same D.

## 2. Table convention

For target `t`, a source column `s in Q` corresponds to the candidate `t-s` for membership in P. An entry `K/(q,q')` certifies

    (t-s)+q = K+q',    K in P,    q,q' in Q,    q!=q'.          (1)

Directness forbids that candidate from P. `*` marks a survivor. If all but one source are forbidden, coverage forces its candidate into P; if none survives, coverage fails. The equalities are valid for all cyclic specializations because the listed Q-elements are distinct under the size hypothesis.

## 3. Six tails are impossible

Suppose `Q=Y union {V}`. Covering `V+7` forces `D=V+6` into P. With that forced P-element, the target `V+12` has no representation:

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=V |
|---|---|---|---|---|---|---|
| V+7 | 8/(1,V) | * | 0/(0,V) | 8/(14,V) | 0/(7,V) | 0/(0,7) |
| V+12 | D/(1,7) | 11/(0,V) | D/(1,0) | 0/(1,V) | 11/(13,V) | 0/(1,13) |

Therefore `|Q|!=6`.

## 4. Seven tails are impossible

Suppose `Q=Y union {U,V}`. At target `V+1`, only two candidates survive: `B=V-12` (source13), or `B=V-U+1` (source U).

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V |
|---|---|---|---|---|---|---|---|
| V+1 | 8/(7,V) | 0/(0,V) | 8/(14,V) | * | 0/(13,V) | * | 0/(0,1) |

**Case I: `B=V-12 in P`.** The next two rows force `D=U-V+2` and `E=U-V+1` into P:

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V |
|---|---|---|---|---|---|---|---|
| U+2 | 3/(1,U) | 8/(7,U) | 8/(13,U) | 3/(14,U) | B/(V,U) | 3/(1,0) | * |
| U+1 | 8/(7,U) | 0/(0,U) | 8/(14,U) | B/(V,U) | 0/(13,U) | 0/(0,1) | * |

Now `D+0=E+1` is a collision using two distinct Q-elements, contradiction.

**Case II: `B=V-U+1 in P`.** The target `V+2` has no representation:

| target t | s=0 | s=1 | s=7 | s=13 | s=14 | s=U | s=V |
|---|---|---|---|---|---|---|---|
| V+2 | 3/(1,V) | 8/(7,V) | 8/(13,V) | 3/(14,V) | B/(13,U) | B/(0,1) | 3/(1,0) |

Thus `|Q|!=7` and the theorem follows.

## 5. A dual actual multi-b tradeoff

Let `N_Y` count actual one-b atoms whose tail residue lies outside `Y={0,1,7,13,14}`; the six original atoms in rows3 and8 with tails2,4,6 are included in this count. Let `M_Q` count actual border atoms `b^l a^j` with `l>=2`. Padding on the left with the actual atom b and on the right with `a^n` shows that two distinct such border atoms cannot share a tail residue, and none can use an old Y-residue already occupied by `b a^j`.

Let `r_0` be the number of distinct one-b tail residues among atoms with head residue0. The actual one-b atoms `b a^j` representing the one-b portion of Q are included in this row even though the row may additionally contain atoms with positive head exponents divisible by n. Thus `r_0>=|Q|-M_Q`. Direct packing of each column against this row gives `N_Y>=n-5 floor(n/r_0)`. The new `|Q|>=8` therefore gives

| Assumption | Necessary lower bound for N_Y |
|---|---|
| M_Q=0 | n-5 floor(n/8) |
| M_Q<=1 | n-5 floor(n/7) |
| M_Q<=2 | n-5 floor(n/6) |

All counts concern the same actual D; these conditions do not construct one.

## 6. Actual check and limits

`frontier-20261028-eight-tail-certificate.py`, SHA256 `dad8a3c95996b337bafd0a0d46007d3c86d7e00d20dff81d618743fa8c8f99f7` (55 LF, 2104 bytes), checks every displayed table entry using exact integer coefficient triples, verifies all source columns and both branches, and prints `PASS`. It checks the symbolic identities and finite proof certificate, not formal/kernel verification. No independent-family, human, peer or novelty gate is claimed. The original finite UD factor-completion problem remains OPEN.

**END OF EIGHT-TAIL BORDER OBSTRUCTION.**
