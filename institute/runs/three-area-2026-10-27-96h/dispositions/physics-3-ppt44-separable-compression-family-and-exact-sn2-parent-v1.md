# PPT4x4: exact Schmidt-number-two intermediate and separable-compression family

**Disposition: scoped same-harness written support; the general peel-off mechanism and intermediate-state SN2 conclusion are PRIOR published results reconstructed here.** Native observation before composition: 2026-10-30T09:59:08-0700 PDT. f367 reports **0 FATAL / 0 MAJOR / 0 MINOR**. No unrestricted 4x4 PPT/SN<=2 theorem or target SN>=3 state is obtained.

## Actual state, not the earlier 4x5 witness

Use Bob-second coordinate4i+j and [v]=|v><v|. Set A=|00>+|11>+|22>, B=|01>+|12>, D=|10>−|21>, E=|20>+|33>, and

R=[A]+[B]+[D]+3([02]+[E]+[23]+[30]+[32]).

Its eight disjoint-support projector vectors give rank8 and trace25. Direct Bob partial transpose has an explicit PSD decomposition:

R^Gamma=[01+10]+[12+21]+[02+11−20]+2[02+20]
        +3[23+30]+[00]+[22]+3[33]+3[32],

with block rank9. Thus R/25 is an actual4x4 PPT state.

For each fourth root z of unity, v_z=B+zA−z²D+z^−1|02> is the sum of the two product vectors

(0+z1+z²2) tensor(1+z^−1 2) +(z0−z²1) tensor0.

Here digits inside factors denote computational basis kets. Four-root averaging gives (1/4)sum[v_z]=[A]+[B]+[D]+[02], so adding 2[02]+3[E]+3[23]+3[30]+3[32] decomposesR entirely into Schmidt-rank<=2 positive terms. Its 3x3 local compression has range matrices [[a,b,c],[d,a,b],[e,−d,a]]; rank1 forces a²−bd=a²+bd=0, hence a=0. A separable positive decomposition would then have zero00diagonal, contrary to its value1. Therefore SN(R/25)=2 exactly, not3, and no2-block-positive detector has negative pairing with this state. Parent reconstructed the exact PT/root-average/range-minor identities in writing; no finite scan is substituted for them.

## Every coherent completion of a separable codimension-one core

For ANY PSD block operator rho=[[C,Z],[Z†,D]] obtained by retaining all but one Bob coordinate, positivity gives rangeZ subsetrangeC and D−Z†C+Z>=0. If C=sum[a_j tensor b_j] is separable, lift each vector to (a_j tensor b_j, Z†C+(a_j tensor b_j)). The added component has one Bob coordinate, so each lift has Schmidt rank<=2, and the remaining Schur block is separable. Thus SN(rho)<=2. Singular/zeroC and arbitrary complex coherentZ,D are included. This is the separable-core case of [Krebs–Gachechiladze, Theorem2](https://arxiv.org/html/2509.07086v1#Thmobservation2), not a new general theorem.

For the displayed R, deleting Bob0 gives a separable core C0 by the explicitly supplied four-root product decomposition. Every PSD4x4 completion with core tC0, t>=0, therefore has SN<=2. More generally, if a PPT state's Bob-delete0 core is block diagonal on (Alice012 tensor Bob12), (Alice012 tensor Bob3) and (Alice3 tensor Bob123), its first block is3x2 PPT and hence separable by the exact [Horodecki Theorem3](https://arxiv.org/html/quant-ph/9605038v2#Thmtheorem3); the other blocks each have one local dimension. The core is separable and every such completion has SN<=2. Arbitrary4x4 PPT states are NOT shown to admit this block form.

## Source and assurance

The [published SupplementE](https://arxiv.org/html/2509.07086v1#A5) already identifies the one-extension intermediate as SN2. The explicit state/decomposition and completion-family application reconstruct that known obstruction. Its source list includes30after deletingBob0, but that ket is removed by the projection; the exact C0 certificate correctly omits it. No paper-wide falsity, novelty or new4x4no-go is inferred.

Parent displayed full502-logical-line f362 author and full349-line f367 review plus the exact frozen primary excerpts; all live source pins match. [Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f362-ppt44-actual-witness-or-global-obstruction-frontier/review-v1.md) · [Review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f367-ppt44-compression-and-exact-intermediate-proof-review/review-v1.md) · [Manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f367-ppt44-compression-and-exact-intermediate-proof-review/manifest-v1.json). Reviewer used parent-supplied hashes/clocks, not independent metadata execution; its later parent clock is recorded additively, not backdated. This review does not adjudicate f362's separate Eq6 theorem. Same-harness written evidence is not human, independent-family, formal/kernel, exhaustive source-status or novelty verification. The original4x4PPT/SN>=3 question remains unpaid.
