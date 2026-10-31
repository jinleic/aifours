# Exact optimum after all nine single-auxiliary cross-pair systems

**Status: WRITTEN with independently checked exact rational primal and matching publisher dual; scientific admission of the added universal inequalities remains pending.** This is a separately scoped successor to `frontier-20261028-threefamily-extended-optimum-v1.md` (SHA-256 `3b917e24eba4a299d0122675837a3016cb34e5ac928e5c3c0c5c7895e20e6fbb`). It does not edit f110 or its frozen review inputs, prove an actual entropy law, or improve the original R-minus numerical bound.

## LP scope

Let `X` be the ten original variables, `U=b'0`, `V=(d'1,e'1,g'2)` and `W=(f'3,g'3,h'4)`. Begin with the two 14-variable star Shannon/copy systems `(X,U,V)` and `(X,U,W)`, their common 11-variable `(X,U)` entropy profile, original FDs/caps/symmetry and the explicitly enumerated entropy-cut families in the predecessor.

For **each of the nine pairs** `v in V`, `w in W`, add a separate full 12-variable Shannon system `(X,v,w)` and impose `I(v;w|X)=0`. The pair systems share their existing `(X,v)` and `(X,w)` marginals with the star primal. A real original law admits these conditional independences by sampling the source auxiliary branches independently given `X`; thus the new requirements are legitimate existential extension constraints.

Each pair contributes `2^10=1,024` previously absent entropy coordinates containing both of its two auxiliaries. Distinct pairs share no new mixed coordinate and agree on their already fixed single-auxiliary/base intersections. The resulting LP has `30,719+9*1,024=39,935` nonempty coordinates. It includes `9*67,596=608,364` checked elemental rows in the nine pair systems, in addition to the `745,500` checked elemental rows in the two star systems. The source copy equalities and the star's 14 independence equalities are retained; nine more pair independence equalities are imposed.

This is **not** the full 17-variable Shannon/copy LP. In particular, it omits mixed Shannon inequalities and entropy coordinates containing two auxiliaries from one of `V,W` together with an auxiliary from the other; it also does not impose the tuple-level `I(V;W|X)=0` as a single all-auxiliary equality. The nine consistent pairwise systems do not by themselves define a full joint polymatroid or a probability distribution.

## Matching exact primal and dual

The two pinned exact star candidates have the same original profile with all singleton entropies equal to 1 and `h(X)=1847/276`. For each of the nine cross pairs, the producer constructed 1,024 rational cross-entropy coordinates while fixing both whole single-auxiliary marginals; the independent checker binds each file hash, rebuilds all `67,596` pairwise elemental inequalities, checks `I(v;w|X)=0` exactly, and rejects changed-full-entropy and missing-coordinate controls. All nine checks pass.

The combined binder merges these pair coordinates with the star primal, independently rechecks all nine conditional-independence equalities and all `1,920` publisher source rows, and revalidates the source signed dual. Thus an exact feasible primal attains the published dual upper `1847/276`: **the optimum of this specified pair-augmented LP remains exactly `1847/276`**. All previously enumerated `F_n`, pinned 2026 disjoint source families, three tested gluing families, and listed `Psi` instances remain satisfied because they depend only on the unchanged star/base marginals. The exact finite bounds and coverage are listed in the predecessor packet and its receipt.

The previously exhibited fixed-star nonentropic points are not resurrected: the current third-family star primal has different auxiliary values and is not claimed entropic or almost-entropic. Conversely, the nine pairwise extensions do not establish that it is non-entropic either. The 1,023-coordinate original profile with alternate copies remains unexcluded.

## Source-order and evidence

* Read `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9` before its frozen publisher-LP source: cross-branch exclusion is Remark **5.4**, not 3.8.
* Read `frontier-20261028-third-cross-cut-independent-label-erratum-v1.json` SHA-256 `e6b01fe0362c99ad0a35dff4aea4a16bda7f0586a38144d1110c152913f7ed7a` before the affected third-cut replay receipt; its metadata label is corrected from “second” to “third.”
* Producer `frontier-20261028-crossbranch23-pairs-round4.py` SHA-256 `a3d29bb4cad4ffdaa01fec81fb9af4ec871689e01be6eb1fef5abfb27af979fb`; its summary SHA-256 `d2883058aa5cf663d0539e41e2f6712c3bec3155220e588eb8e93edaa2f76516` lists all nine candidate filenames and exact hashes. Floating solver statuses were only proposals, not the proof.
* Independent pair checker `frontier-20261028-crossbranch23-pairs-round4-independent.py` SHA-256 `f34fe9895233be6206ea857f73ca0d89d88644d92c3a0790217f8c1e93647151`; receipt SHA-256 `143db08d3ce5caf8e2f764473d0eb2fe5ce4f14a760e95df33b47903a4fc4540`. It checks all nine exact 12-variable systems and two mutations per pair.
* Combined binder `frontier-20261028-pair-augmented-lp-binding.py` SHA-256 `7d1ceebe0e00588cee54fe64ab3a800e1be9a83a25a42ce05dcfb04459a18b55`; receipt SHA-256 `f42c65d0e0c41e5df086d11ff17e347547e57bab4f3756153e62db33af5b66cc`. It reads both required corrections first, binds the common star and all nine pair witnesses, merges all 39,935 coordinates, rechecks pair independence and all source rows, and rejects two combined-point mutations.

No cross-model review, proof-assistant formalization, or novelty clearance has been performed for this successor. All-variable cross-branch constraints, other non-Shannon inequalities and the original scientific target remain open.
