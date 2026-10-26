# Paw subtype count erratum v1

PhysicsRQLS10. Mandatory overlay on `axial-negative-paw-fourth-order-v1.md`, section4; source snapshot unchanged. No execution, no invented clock.

The phrase “The negative paw has8 raw matching embeddings …384 literal …” is too broad. Those numbers refer only to the **parallel-leaf paw subtype whose unique heavy edge is opposite the hub**. The entire paw support class has16 raw embeddings and768 literal cores, because it also includes the heavy-edge-incident-to-hub subtype.

The exact old written geometry is `rook-three-pairs-closure-v1.md`, lines36–45: for one horizontal/two vertical pairs, r has2 choices, a has2, and u∈{0,r} has2. Coordinate transposition doubles these8 to16. The u=r branch (and its transpose) has two parallel vertical leaves and its heavy edge opposite the hub:8 raw embeddings,384 literal cores. The u=0 branch has its heavy edge incident to the diagonal hub: another8 raw embeddings,384 literal cores.

The new P residual already requires **heavy opposite hub**, by `axial-leading-class-reduction-v1.md` section4. The heavy-incident-to-hub case is an earlier first-order path4 closure and is not part of the fourth-order calculation. Therefore the subsequent384→96→48→16 calculation is correct on its actual parallel-leaf subtype and the claimed16 residual does not change. All uses of “negative paw” as a global count must carry this subtype qualification. No all-paw exclusion or new execution is implied.
