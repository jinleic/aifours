# Genuinely non-completely-regular original sources with exact all-actor band size

**Status: NEW AUTHOR WRITTEN constructive family theorem; one full 544-element finite homomorphism certificate rechecked in the exact eval kernel. UNREVIEWED / UNADOPTED.** Original universalQ1/Q2 remain OPEN. S68 itself is completely regular; the new sources below are NOT, and that distinction is essential.

## 1. An arbitrary semilattice-action factor, without unitizing S68

Let Y be a finite semilattice with zero and H a finite group acting on Y by automorphisms. Define `T=Y⋊H`, `(y,h)(z,k)=(y∧h(z),hk)`. It is an inverse semigroup: the unique inverse of `(y,h)` is `(h⁻¹(y),h⁻¹)`. Uniqueness follows because any inverse has actor h⁻¹ and the two inverse equations force its semilattice coordinate to equal h⁻¹(y). Its idempotents are exactly `(y,1)`, so projection onto H is idempotent-pure. It is WEU because any idempotent below an element has the same group actor as that element, forcing actor1. All idempotent corners have semilattice idempotents. If some h moves y, then `(y,h)` is NOT completely regular, since its unique inverse has `ss⁻¹=(y,1)` and `s⁻¹s=(h⁻¹(y),1)` different.

For a,b≥0, d=a+b≥1, let

`S(a,b;Y,H)=S68^a × (S68^op)^b × (Y⋊H)`.

Finite products preserve regularity, FULL-order WEU and local-r, by taking coordinates of inverses/order witnesses/corners. Thus this is in the ORIGINAL source class. It is nonorthodox and nonlocallyinverse because its S68 factor is; fixing idempotents in all other coordinates embeds that factor, and also embeds its noncommuting-idempotent corner. It is non-completely-regular whenever the H-action on Y is nontrivial, as shown by the T-factor element above. There is no added identity on S68 and no invalid monoid reduction.

## 2. Explicit optimal host over arbitrary actors

Import the pinned S68 host: band B8, actor D12, faithful map `S68→P(B8,D12)`, with B8 RIGHTSN and |B8|=8. Its opposite has the corresponding LEFTSN host with the same sizes, using the exact opposite/gauge identity in `frontier-20261029-SN-minimal-universal-band-variety-v1.md`, SHA `7ac1c34e5f599fc96a7e9658b7fc3d66777792eda07aabd520d25793beee97a6`.

Products of physical hosts are physical hosts over the product CS actor, with product band and coordinatewise group action; the physical multiplication identity is literally coordinatewise. Thus S(a,b;Y,H) has an explicit faithful SN host with

`band C=B8^a × (B8^op)^b × Y`, `|C|=8^d|Y|`,

`actor D=D12^a × (D12^op)^b × H`, `|D|=12^d|H|`,

`|source|=68^d|Y||H|`, `|whole host|=96^d|Y||H|`.

This band size is SHARP over **ALL** CS actors/actions, not just this actor. In S68 the eight distinct idempotents `F={0,8,16,24,36,44,52,60}` lie above source0. The same holds in its opposite. In T all |Y| idempotents lie above `(0_Y,1)`. Consequently the product contains `8^d|Y|` distinct idempotents all above ONE idempotent. Every CS homomorphism sends these to a single actor, because idempotent comparability in a CS semigroup is equality. Any faithful physical host must therefore give these source idempotents distinct band coordinates. Hence `|band|≥8^d|Y|`, attained above.

If a,b>0, neither a RIGHTSN-only band nor a LEFTSN-only band can host this source under ANY actor/action: restriction to its embedded opposite-S68 or S68 slice respectively contradicts the universal one-sided exclusions of `frontier-20261029-mixed-source-essential-SN-v1.md`, SHA `69346bc21b4eb1346a69b716b79e6c59f76fa85d89192054b8711071a760c45c`. Full SN is genuinely needed for this mixed family. The stated whole-host sizes are constructive UPPER bounds, not claimed whole-host optima.

## 3. Small literal non-CR instance and exact recheck

Take Y=P({1,2}), represented by bitmasks0,1,2,3 with intersection, and H=C₂ swapping the atoms. Then T has eight elements, and `(1,1)` has inverse `(2,1)` and is not completely regular. For a=1,b=0 the original source has544 elements, optimal band32, actor24, and host768.

`frontier-20261029-nonCR-original-product-checker-v1.py`, SHA `ece967974dfbad5b97ab494d12bccfc13ad713ba458ef947dd7301536157c42d`, completed before ThuOct29 01:43:49 PDT2026. It freshly checks S68 regularity and FULL two-idempotent-witness WEU, EVERY local idempotent corner is right regular, an explicit nonorthodox pair0,7, and noncommuting local witness(e,x,y)=(59,43,67). It verifies B8 associativity/RIGHTSN, all512 T-associativity equations and T-regularity, the explicit non-CR T-element and lack of any commuting inverse. It checks ALL295936 products of the544 source elements against the literal product-host formula and all544 image coordinates are distinct, plus all32 common-lower-bounded idempotents. It does not enumerate544³ associativity equations; product associativity is the written proof above using its factors.

The checker pins original source data SHA `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf` and B8/refined-actor data SHA `72bb328439b4f24919788e7379a20ea61f01ecc58dcd74f80da3f5d8ff848c40`. The mandatory FULL-order correction `frontier-20261028-natural-order-weu-audit-erratum-v1.md`, SHA `801f699bb640bd1e58eed095779c05b882e7d9eddd0ea1c470b522ecbc345c28`, remains binding; the weaker old simultaneous-witness check is NOT used.

For arbitrary finite nonabelian H one can take Y=P(H) with left-translation action, which is faithful and nontrivial. Then the same written construction gives genuinely non-CR, nonorthodox, nonlocallyinverse original sources with faithful nonabelian action and exact band size `8^d2^|H|`. That general statement is a symbolic proof, not a claimed finite replay of the large sources. No novelty, independent proof, formal kernel verification, or universal originalSEP closure is inferred.
