# mcDSQS(74): Construction 2.1 with a two-point stem

Written after the host-clock reading 2026-10-17 19:14:08 PDT. This is a finite-construction explanation, not a
formal proof of the source's general construction and not a novelty/priority claim. The 74-point output is
checked directly by both mcDSQS checkers; their acceptance does not depend on the explanation or on symmetry.

## Source and inputs

Tan–Zhou arXiv:2503.11934v1, pinned text `sources/tz/tan-zhou-2503.11934.txt`, SHA-256
`df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164`. Definitions: gcDSQS(v,h), LF 227–236;
gcDCQS, LF 281–288; Construction 2.1, LF 292–335 (the 2 mod 6 branch).

1. gcDCQS(18⁴:2), raw file `evidence/gcdcqs18-z8z3z3/gcdcqs18_4_2_z8z3z3.txt`, SHA-256
   `1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e`.
2. mcDSQS(20), Shi–Xia–Krotov arXiv:2212.00048v2, proof of Proposition 3 (printed p.15):
   `sources/sxk/sxk_prop3_transcription.json`, SHA-256
   `3610b32c75738348751c4f58dd9243358e66c2b72d2a15d80bf91e0f49a0d057`, copied byte-for-byte from the gcdcqs20
   lane. The earlier primary PDF/text remain there read-only (PDF SHA `5474c9fb…53c4`, text `619909f8…77a1`,
   LF 667–684). The present builder independently develops all 16 base blocks under Z20 and checks all 1140
   triples once (285 blocks), and at every a ∈ Z20 checks the ten translated cells partition the derived STS(19)
   into partial parallel classes.

## Why the same mcDSQS(20) is a gcDSQS(20,2)

Designate any two points as a hole S={α,β}. There is no triple inside a two-point set, so the SQS condition is
unchanged. At x∉S the derived STS(19) is minimum colourable by the supplied ten classes. At x=α the incomplete
STS(19,1), hole {β}, is the same triple system: β has degree 9 and the ten classes are partial parallel classes,
so β belongs to exactly nine classes and is missed by exactly one. This is precisely the good-colouring
parameter s=χ′(19)−(19−1)/2=10−9=1. The same argument applies at β. The builder explicitly checks the 9/1 split
at both stem points of each local copy. Thus the gcDSQS(20,2) hypothesis is met, not merely assumed.

## Labels, blocks and class merge

For each original group G_k in the certificate's GROUPS order, send local label j<18 to the j-th listed point
of G_k, and labels 18,19 to stem points 72,73. The four local SQS(20)s use distinct groups and share only two
points, hence no local quadruple is duplicated. Add their blocks to the gcDCQS blocks:
15066+4·285=16206=C(74,3)/4.

At a group point x∈G_k, merge the ten local derived classes with the ten gcDCQS classes avoiding
(G_k∪S)∖{x}, both in listed order; retain the other 27 classes. The merge is point-disjoint because the two
summands lie in disjoint sets.

At stem point α, for each k pair its nine KF classes missing G_k with the nine local derived classes on
G_k∪S that contain the other stem β (listed order). The frame part avoids G_k∪S, so these merges are
point-disjoint. The one remaining local class of each group avoids β and lies wholly in G_k; unite the four
such classes to obtain the last class. This gives 4·9+1=37 classes at each stem point.

## Direct finite result and limits

Output `evidence/mcdsqs74-c21/mcdsqs74_c21.txt`, SHA-256
`eaff77fc63cc408756f72b6f6213eb7449a13e1efc5ba0c40401fc51d4f216c3`. Both definition-first checkers PASS:
all C(74,3)=64824 triples occur once, and all 74 derived STS(73)s are partitioned into 37 partial parallel
classes. A class on 73 points has at most 24 triples; 36·24=864<876, so 37 colours are minimal without using
any external chromatic-index theorem.

This closes only the finite order-74 consequence of the gcDCQS object. The frozen §4(3) target still requires
FDGDD(3,4,5{18}) or RDGDD(3,4,5{18}); the infinite-family bridge is not established by this order-74 witness
alone. No Lean result, priority finding or breakthrough-gate claim is made here.
