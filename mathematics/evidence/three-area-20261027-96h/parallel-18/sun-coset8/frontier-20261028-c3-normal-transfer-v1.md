# Sun8 transfers through an index-three normal extension, conditional on Sun7

**NEW WRITTEN CANDIDATE, not reviewed/adopted/novelty-cleared.** Actual native prewrite clock: **Wed Oct 28 17:02:41 PDT 2026**. The normal-extension proof below is self-contained apart from the two explicit group properties in its hypothesis; the universal Sun7 statement is a separately identified statement-only import in the corollary. An independent bounded finite prime-support checker was run and is supplementary, not a replacement for the written proof or an actual-group counterexample search.

## 1. Definitions and precise theorem

For a group X and k=7 or8, `Sun_k(X)` means: for **every** k pairwise-disjoint actual LEFT cosets of finite-index subgroups of X, two of their subgroup indices have gcd at least k. Subgroups/cosets may repeat as objects where disjointness permits; X need not be finite and the cosets need not cover X.

**Theorem.** For every group G and every normal subgroup N of index3, if `Sun_8(N)` and `Sun_7(G)`, then `Sun_8(G)`.

**Corollary, conditional on the licensed statement-only arbitrary-group Sun7 import.** If every group satisfies `Sun_7`, then every index-three extension of a `Sun_8` group again satisfies `Sun_8`. Consequently, by successive index-three normal steps, the same holds when G/N is a finite 3-group and N satisfies `Sun_8`. The last finite-3-group step uses the elementary existence of a normal series with prime-order quotients, established in Section6. No splitting, finiteness of G/N beyond the stated cases, normality of the original subgroups, covering condition or symmetry of subgroup indices is assumed.

The imported Sun7 STATEMENT is the one named in the already reviewed v3 packet: every seven disjoint finite-index cosets in an arbitrary group have some pair of indices with gcd>=7. Its proof is NOT reconstructed or newly authenticated here. Without this import, the theorem remains a valid conditional implication with the explicit `Sun_7(G)` hypothesis; an unconditional corollary would not follow solely from this packet.

## 2. Actual fibres and two necessary facts

Assume, for contradiction, that actual disjoint G-cosets `g_i U_i`, `i=1,...,8`, have finite indices `n_i` satisfying `gcd(n_i,n_j)<=7` for every distinct pair. Let `pi:G->G/N`, and put

    b_i=[N:N∩U_i],   a_i=[G/N:pi(U_i)],   n_i=a_i b_i.

The index formula follows from `N U_i/U_i ≅ N/(N∩U_i)` as coset sets and `[G:U_i]=[G:NU_i][NU_i:U_i]`. The quotient has prime order3; therefore `a_i` is either1 or3. A label with `a_i=3` is **proper-image**, and its actual image coset is one quotient point. A label with `a_i=1` is **full-image**, and its actual image coset is all of G/N.

For a quotient point q contained in `pi(g_i U_i)`, choose one representative `t` of q. Then `t^{-1}(g_i U_i∩tN)` is an ACTUAL left coset in N of `N∩U_i`, of index b_i: choose one member `t x` in the intersection, and write the intersection as `t x (N∩U_i)`. Fibres of two disjoint original cosets are disjoint. Consequently any two labels whose actual quotient-image cosets meet have

    gcd(b_i,b_j)>=2.                                            (2.1)

For completeness, (2.1) follows because two finite-index left cosets with coprime indices in any group must intersect: the diagonal map from the cosets of the intersection subgroup into the product of the two coset sets is injective; the intersection index is divisible by both coprime indices and at most their product, hence equals the product, making the diagonal map surjective. This uses actual left cosets, not an assumed independent selection of fibre representatives.

If there are zero or one proper-image labels, all eight image cosets share a quotient point. The corresponding eight disjoint N-cosets then invoke the **actual kernel hypothesis** `Sun_8(N)`, producing a pair with `gcd(b_i,b_j)>=8`, hence also `gcd(n_i,n_j)>=8`. Thus a counterconfiguration has at least two proper-image labels.

For ANY two proper-image labels i,j, `n_i=3b_i` and `n_j=3b_j`, so

    gcd(b_i,b_j)<=2.                                            (2.2)

In particular they cannot both have b divisible by any odd prime. For ANY full-image label j, `n_j=b_j`, and its quotient image meets every other image coset. Thus its b has gcd>=2 with every other label's b, by (2.1).

## 3. Three seven-divisible original indices

`Sun_7(G)` applied to each seven-label subfamily of the eight actual disjoint cosets yields a pair with gcd>=7. Under the counterconfiguration assumption that pair has gcd exactly7, so both its indices are divisible by7. If fewer than three of the eight indices were divisible by7, deleting one of at most two such labels would leave a seven-label subfamily with at most one, a contradiction. Hence at least THREE original indices are divisible by7.

At most one proper-image label is seven-divisible: two would have original indices divisible by `3*7`, contradicting the <=7 pairwise gcd bound. Thus at least two seven-divisible labels are full-image. Any two distinct seven-divisible full labels V,W have gcd exactly7. In particular, they cannot both be even and cannot share any prime other than7.

## 4. No proper-image label is seven-divisible: contradiction

There are at least two proper-image labels, call them A and B. In this case neither b_A nor b_B is divisible by7. Choose two seven-divisible full labels V,W, and choose V odd; such a choice exists because at most one of V,W is even.

Full V meets both proper-image fibres. By (2.1), each of `gcd(b_A,n_V)` and `gcd(b_B,n_V)` is at least2. Each divides the corresponding original G-index gcd and is therefore at most7. Since V is odd and neither proper b is divisible by7, each such gcd has a prime divisor in `{3,5}`.

By (2.2), b_A and b_B cannot share either3 or5. Therefore, after interchanging A and B if needed, `3|b_A`, `5|b_B`, and BOTH `3|n_V` and `5|n_V`. But `n_B=3b_B` is divisible by15, and n_V is also divisible by15. This gives `gcd(n_B,n_V)>=15`, contradicting the original <=7 bound. Thus this entire case is impossible. No selected subgroup, quotient point or numeric index tuple was assumed.

## 5. Exactly one proper-image label is seven-divisible: contradiction

Let A be the proper-image seven-divisible label. There are at least two full seven-divisible labels; select V,W so that V is odd. Because `21|n_A`, no full seven-divisible original index can be divisible by3: otherwise its gcd with n_A would be at least21.

There is at least one other proper-image label. For ANY such label B, b_B is not divisible by7. The same actual-fibre argument as above shows `gcd(b_B,n_V)>=2`, and this gcd divides `gcd(n_B,n_V)<=7`. Since V is odd, not divisible by3, and b_B is not divisible by7, the common prime must be5. Hence

    5|b_B  and  5|n_V.                                          (5.1)

If there were two distinct labels B with this property, their b indices would have gcd at least5, contradicting (2.2). Therefore A and B are the **only** proper-image labels and the other six labels are full-image.

Since `gcd(n_V,n_W)=7`, W is not divisible by5. It is also not divisible by3. Its fibre meets B's, so (2.1), the bound <=7 and `7∤b_B` force their common prime to be2. Thus

    2|n_W,  2|b_B,  5|b_B.                                     (5.2)

As `7|b_A` and `14|n_W`, the original <=7 pair bound forces b_A odd. Combining this with (2.2) gives `gcd(b_A,b_B)=1`. In particular `5∤b_A`.

There are six full labels, so choose a full label F distinct from V and W. It CANNOT be seven-divisible. Indeed, if it were, its pairwise gcds with seven-divisible W and V force F to be odd and not divisible by5, while the preceding paragraph shows no full seven-label is divisible by3. Its fibre must meet B's; because `7∤b_B` and `gcd(b_B,n_F)<=7`, it would need a common prime among2,3,5,7, none of which is possible. Thus `7∤n_F`.

Now F meets A's fibre, so `gcd(b_A,n_F)>=2` and this gcd is at most7. Because b_A is odd, `5∤b_A`, and `7∤n_F`, the only possible common prime is3. Hence `3|b_A` and `3|n_F`. The coprimality `gcd(b_A,b_B)=1` gives `3∤b_B`; nevertheless `n_B=3b_B` is divisible by3 and by5.

F also meets B's fibre, so `gcd(b_B,n_F)>=2`. As `3∤b_B` and `7∤n_F`, a common prime at most7 is2 or5. If 5 divided n_F, then both n_F and n_B would be divisible by15, contradicting their <=7 original-index gcd. Therefore `5∤n_F` and the common prime is2.

Finally F and V are both FULL-image labels, so their actual quotient cosets meet and (2.1) requires `gcd(n_F,n_V)>=2`. But n_F is not divisible by5 or7, while n_V is not divisible by2 or3; any common prime <=7 is impossible. A common prime >7 would itself violate the <=7 original-index gcd bound. Thus their gcd is1, a contradiction. The contradiction uses the SAME actual F,V,A,B cosets and the SAME kernel indices throughout, including the pair of full fibres.

Both possibilities have been exhausted. Therefore the assumed counterconfiguration does not exist and `Sun_8(G)` holds. □

## 6. Finite 3-group corollary and all hypotheses

If Q is a finite nontrivial 3-group, its centre has a nonidentity element: conjugacy-class sizes are powers of3, so the class equation shows the centre has size divisible by3. A central element of order3 exists by taking an appropriate power of a nonidentity element of 3-power order. Induct on |Q|: the quotient by that central subgroup is a smaller 3-group with a series of normal subgroups whose factors have order3; pulling this series back through the quotient and appending the central subgroup gives such a series in Q. Each subgroup in the series is normal in the next. The trivial quotient is the zero-step case.

For Q=G/N, take inverse images of that series in G. Starting from N and applying the theorem to each successive index-three extension gives `Sun_8(G)`, PROVIDED the stated Sun7 property holds for each intermediate group. The licensed arbitrary-group Sun7 statement supplies those hypotheses; otherwise write them explicitly. This is a conditional 3-group extension corollary, not an unconditional assertion for an arbitrary kernel.

## 7. Exact bounded independent finite support check

Executed `/opt/homebrew/bin/python3 frontier-20261028-c3-support-obstruction-check.py` with a 30-second command deadline. Source SHA256 **`d53e7c5e14e3a5f18b36ae20cb09423cc43cc5c53dd40bfb16aab1b5ff392160`**. Actual output and observed clock:

```text
no_proper_seven: partial_counts=[1, 24, 180, 588, 0, 0]; terminal_models=0
one_proper_seven: partial_counts=[1, 24, 180, 235, 80, 0]; terminal_models=0
PASS: no abstract model for either C3 obstruction scenario
Wed Oct 28 17:02:17 PDT 2026
```

The checker enumerates all48 signatures `2^e2 3^e3 5^e5 7^e7` with `0<=e2<=3`, `0<=e3<=2`, `0<=e5,e7<=1`. These are divisors of any actual b with the corresponding truncated valuations. If an actual original pair gcd is <=7, the checker’s projected gcd is <=7. If two actual fibre cosets are disjoint and their original gcd is <=7, a shared prime must be among2,3,5,7, so the checker retains their nontrivial projected gcd. Ignoring larger primes and higher powers of5/7 makes an OVERAPPROXIMATION, not a hidden finite-group enumeration. For no proper seven-label it seeks two non-seven proper labels and three seven full labels; for one proper seven-label it seeks that label, another proper label, two seven full labels and any additional full label. Zero models is consistent with the two written contradictions. The program does not authenticate Sun7, establish actual coset existence, check every mathematical inference, or constitute formal proof.

## 8. Exact scope and provenance

This is a NEW argument for the actual quotient of order3, beyond the previously parent-supported quotient5/7 and prime>7 transfers. The exact original definitions were reread from the39LF bound packet and the valid normal-fibre/previous v2–v3 arguments were inspected; this proof independently supplies the necessary fibre and seven-divisibility steps. The previously held post-v3 episode is not treated as a proven premise or retroactively validated. No clean-cognition or novelty claim is made; current owner direction prospectively permits independent calculations and new reasoning.

The theorem does NOT prove unrestricted Sun8: the `Sun_8(N)` premise and `Sun_7(G)` are explicit, and extensions involving quotient2, arbitrary mixed composition factors, and remaining finite simple groups are not resolved here. This also does not independently certify the statement-only Sun7 import, source/book equivalence, a human/kernel/independent-family proof, or publication priority. Parent must review the entire argument and its dependencies before any adoption.
