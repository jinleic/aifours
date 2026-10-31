# Shor completion: the only possible odd tail border over a 165 cofactor

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 20:26:08 PDT 2026**.
**ALL-ORDER WRITTEN necessary classification, conditional on the separately pinned universal 55-tail proof; no full no-go, formal/peer/cross-family acceptance or novelty claim.**

## 1. Statement

Let `k>=2` and `n=165*2^k`. For any direct cyclic border factorization with the literal Shor anchors

    {0,3,8,11} subset P,     {0,1,7,13,14} subset Q,

if |Q| is odd, then necessarily

    k>=4,       |Q|=165,       |P|=2^k,

and P contains exactly one residue in each class modulo `2^k`. In particular, for n660 and n1320 an odd-cardinality tail border is impossible. This does NOT exclude even-cardinality Q or prove any completion/noncompletion.

## 2. Proof

Set `m=2^k`. The direct tiling gives `|P||Q|=165m`. If |Q| is odd, then `|P|=m*d` and `|Q|=165/d`, where d is a positive divisor of165. The usual prime-power root argument puts all `Phi_2,...,Phi_m` in P, so P has exactly d elements in each residue class modulo m.

The independent CRT anchor-screen lemma proved in `frontier-20261028-universal-55-tail-obstruction-v1.md` says the residue class `1 mod m` has exactly THREE individually compatible head residues. Thus `d<=3`. The only positive divisors of165 at most3 are1 and3.

If d=3, then |Q|=55, excluded for every k>=2 by the separately pinned all-order 55-tail theorem. Hence d=1, |Q|=165 and P has exactly one residue per mod-m class.

For k=2, old heads0 and8 coincide modulo4; for k=3, they coincide modulo8. These are two distinct actual P-elements and contradict one-per-class. Thus k>=4. The old heads are distinct modulo m for k>=4; this observation does NOT establish that a tiling or code exists.

## 3. Source and boundary

The CRT lemma and all-k |Q|55 exclusion are in `frontier-20261028-universal-55-tail-obstruction-v1.md`, SHA256 `d6c9929c1a6a2a69f79f4951e76443b752764f035f1d80af9760876aba1c6673`. Its independent bounded check covers k=2..10. Classical Sands and actual-border factorization are explicitly reconstructed and named there and in its predecessors. The finite checks do not replace the written all-order proof.

The conclusion is a necessary branch classification for the SAME P,Q tiling. The remaining odd-Q branch when k>=4 and all even-Q branches are open, as is the original unrestricted finite UD factor-completion problem. Independent scientific review and novelty screening remain outstanding.

**END OF ODD-TAIL COFACTOR CLASSIFICATION.**
