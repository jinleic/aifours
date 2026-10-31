# Shor completion: an all-order eight-head border obstruction

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:44:58 PDT 2026**.
**WRITTEN proof with an exact symbolic collision-certificate checker; no unrestricted completion/no-go, formal proof, peer acceptance, independent-family review or novelty clearance is claimed.**

## 1. Theorem

Let D be ANY finite UD factor-complete extension of the literal Shor code, with actual pure-a atom `a^n`. Define from actual atoms, allowing several consecutive b's,

    P={i mod n : a^i b^k in D for some k>=1},
    Q={j mod n : b^l a^j in D for some l>=1}.

The actual-word border reconstruction in `frontier-20261028-six-head-border-factorization-v1.md` gives `n>=26`, the direct tiling `P+Q=Z_n`, and anchors

    A={0,3,8,11} subset P,     {0,1,7,13,14} subset Q.

The prior packet `frontier-20261028-seven-head-border-obstruction-v1.md` independently proves `|P|>=7`. **The additional all-order conclusion here is `|P|!=7`, and therefore `|P|>=8`.** There is no restriction on n's prime valuations. The direct-tiling theorem itself is prior, as acknowledged in that predecessor; priority of this particular anchor deduction has not been searched.

## 2. Collision-table proof protocol

Suppose for contradiction `P={0,3,8,11,U,V,W}`, seven distinct group elements. Work throughout modulo n. A collision certificate `K/(p,p')` at target `t` and **source column** `s in P` means

    (t-s)+p = K+p',     K in Q,     p,p' in P and p!=p'.        (1)

Directness then forbids `t-s` from Q. If every column but one is forbidden, coverage of t forces the sole remaining `t-s` into Q. If every column is forbidden, coverage fails. An asterisk `*` denotes a surviving source column; every displayed certificate has the exact form (1). Since P's members are distinct, these implications remain valid even when other symbolic expressions coincide after substituting concrete group residues.

Set `E=U-V+4` and `F=W-U+4`. The old Q elements 1,7,14 are available. In the first row below the only survivors are sources V and W. Relabel V,W if necessary and assume `E in Q`. The second row then forces `F in Q`; the third reduces to exactly two cases.

| target t | s=0 | s=3 | s=8 | s=11 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|
| U+4 | 7/(3,U) | 1/(0,U) | 7/(11,U) | 1/(8,U) | 1/(0,3) | * | * |
| W+4 | 7/(3,W) | 1/(0,W) | 7/(11,W) | 1/(8,W) | * | E/(U,W) | 1/(0,3) |
| W+9 | * | 14/(8,W) | 1/(0,W) | 1/(3,W) | F/(3,8) | * | 1/(0,8) |

Thus the cases are `W+9 in Q` and `W-V+9 in Q`. The relabeling is legitimate even in a specialized cyclic group because the two original surviving Q-elements differ exactly when V and W differ.

## 3. Case I: `B=W+9 in Q`

Use the following tables in order. The first forces `C=U-W+9` into Q, the second forces `D=U+12`, and the third forces `H=W-2V+12`. The last target has no possible representation.

| target t | s=0 | s=3 | s=8 | s=11 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|
| U+9 | B/(W,U) | 14/(8,U) | 1/(0,U) | 1/(3,U) | 1/(0,8) | E/(3,8) | * |
| U+12 | * | B/(W,U) | 7/(3,U) | 1/(0,U) | 1/(0,11) | E/(0,8) | C/(0,3) |
| W-V+12 | B/(V,3) | B/(V,0) | E/(U,W) | 1/(V,W) | F/(V,8) | * | 1/(V,11) |
| U-V+W+12 | D/(V,W) | B/(V,U) | E/(0,W) | E/(3,W) | B/(V,3) | H/(0,U) | E/(0,8) |

## 4. Case II: `B=W-V+9 in Q`

The first row forces `D=W+12`, the second forces `H=U-2V+W+12`, and the third forces `I=W-2V+15`.

| target t | s=0 | s=3 | s=8 | s=11 | s=U | s=V | s=W |
|---|---|---|---|---|---|---|---|
| W+12 | * | B/(0,V) | 7/(3,W) | 1/(0,W) | F/(0,8) | B/(0,3) | 1/(0,11) |
| U-V+W+12 | D/(V,U) | B/(0,U) | E/(0,W) | E/(3,W) | B/(0,3) | * | E/(0,8) |
| W-V+15 | D/(V,3) | B/(0,3) | 7/(V,W) | E/(U,W) | F/(V,11) | * | 7/(V,8) |

But `H+3=I+U`, with distinct P-elements3,U and hence distinct Q-elements H,I. This is a directness contradiction. Both possible cases fail, so `|P|=7` is impossible. Together with the seven-head predecessor, `|P|>=8`.

## 5. Consequences and precise limits

The actual-code multi-b escape theorem in `frontier-20261028-zero-column-multib-escape-v1.md` now yields the sharper same-D alternative: either

    N_out >= n-4 floor(n/5),

or D contains at least **four** actual atoms `a^i b^k` with `k>=2` and pairwise distinct head residues outside `{0,3,8,11}`. Here `N_out` counts actual one-b atoms with heads outside that old four-head set. At n=1320, fewer than264 outside-head one-b atoms would force at least four such multi-b border atoms. No existence is asserted.

The seven-head predecessor's separate elementary `v_2(n)=3` Fourier filter excludes `|P|=8`, so for that valuation `|P|>=9`. At n=1320 this gives `|P|>=10` because9 does not divide1320. The 18 remaining divisor choices listed there are unchanged:7 was already not a divisor of1320. These are necessary arithmetic filters, not a proof that n=1320 is impossible.

## 6. Actual symbolic check and assurance

`frontier-20261028-eight-head-certificate.py`, SHA256 `6e629ecf8906ad4dc7b3d3e4b87dd44a8ffaa12c59b7ce3e908f15ec36a9eeb6` (91 LF, 4036 bytes), checks every entry of the tables as an exact identity in the free integer coefficients of `1,U,V,W`; checks every column is either certified or explicitly survives; checks both forced branches and the final collision; and verifies that each certificate uses two distinct symbolic P-elements and a previously established Q-element. Its actual output was `PASS` for both seven-head branches and root/forced/collision identities. The finite identity check is not itself a formal proof or an independent model-family review; the universal argument is the written direct-tiling reasoning and table.

This does not construct D, exclude all orders, establish novelty, or adopt a larger border size as feasible. The original finite UD factor-completion problem remains OPEN.

**END OF EIGHT-HEAD BORDER OBSTRUCTION.**
