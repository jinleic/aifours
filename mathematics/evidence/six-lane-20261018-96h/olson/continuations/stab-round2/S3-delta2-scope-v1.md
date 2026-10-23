# S3 delta'=2 short-core step: frozen statement before written derivation, v1

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T08:45:23-0700. Parent authorized written short-core work after packaging
proof-S3-lowdefect-core-v1.md (3847ade3f32e9d9edd11a7cbbd246b68b1a63c8e16beda796250d7c9d64c662a), which remains UNREVIEWED / CONDITIONAL. No computation.

## Exact statement under test
Q2: In the same BASE2 threshold-counterexample CF setting p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h=2m-2, g=g0, d=delta0<=h-1,
Z0 inclusion-maximal mod-p zero-sum, U'=U-Z0 and delta'=d-|Z0|, the alternative delta'=2 is impossible. This is the first short
core obstruction at p=29,m=5 (then |U'|=14 and |U'(-sigma(U'))|=15<floor(29/2)+2=16, so index one is unavailable).

## Visible new approach (not assumed)
F' at delta'=2 still forbids ALL nonempty subset sums of U' in[0,h]. Its length is now2m+4, so |A'|>=2m+5, A':={0}unionSigma(U').
For each z in nonempty Z0, the complementary occurrence subset Z0-{z} has size d-3 and residue-z, hence F* forbids all
z+[2,h] from A'. A tailT=[h+1,p-1] of size4m with an (h-1)-interval removed has size2m+3; with0 added at most2m+4<|A'|.
Thus the middle residues of Z0 should again be excluded; the endpoints now permit residue-1 as well as small positives. A
signed balance/first-crossing argument (plus a large core of sumsets near a forbidden interval, if necessary) must finish the
step or leave an exact obstruction. Do not assume signed balance modulo p is integer equality without a range check.
Empty Z0 (d=2) will use P2 only CONDITIONALLY while its review runs, or the already re-proved packing step with accepted L1.
No universal LS/BASE2, LS+ or STAB result is sought by this step; no inaccessible inverse theorem is imported.
