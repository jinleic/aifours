# F755 — exact U3 census and local lambda/Fourier source preparation

**Status: NONBLIND GENERAL AUTHOR; both source versions NOT RUN, NOT COMPILED, NOT TESTED.** The operative proposal is `independent-boolean-u3-local-profile-v2.py`, SHA-256 `34a540a694551ddd3766232ad5ca2792b5419831fecc80b7fb73bf4cc19925c5`, 28,110 bytes, 644 LF. Before any execution, Main must independently read the entire exact source, decide whether its scope and controls are suitable, and issue a separate bounded GO. The source proposes a 42 s cooperative deadline, signal-to-INCOMPLETE handling, and JSON on stdout, with no input, file reads/writes, network, subprocess, deletion, third-party package, or hidden solver. A parent external bound, if a GO is granted, is at most 55 s; no run, outcome, duration, memory bound, test pass, or parent acceptance is asserted here.

## Actual correction and exposure

I first created `independent-boolean-u3-local-profile-v1.py`, SHA-256 `9609201adbd8d7744f4ff5443966b6070cf921d99fe87a89a7986bc49b721299`, 28,128 bytes, 648 LF. Before any execution I recognized that its heavy-row extension bookkeeping retained only one light-row occupancy completion, potentially omitting another allowed E-occupancy shape from its shape-indexed counts. I informed Main immediately. V1 is preserved unchanged, NEVER RUN, SUPERSEDED, and must not receive GO. V2 is a complete newly exclusive-created file; for each heavy row it considers all E-occupancy count combinations for the three other actual light rows and records each reachable shape, so its counts by shape can overlap. This is a pre-run **source-coverage design fault**, not an observed failure or evidence of mathematical falsity. Its repair is untested and requires the parent's full independent source review.

The additive f749 correction in packet S3 remains operative: graph `0000` has graph lambda energy **exactly zero**, not generically 0 or 4. No f749 source was opened or reused.

## Independently derived U3 integer domain

Retain one same-object normalized `Y`, the 32 physical ell-pairs `(A0+A1,A0-A1)`, all 64 residues `4 mod 8`, the cap 12, full spatial Y-energy 128, and graph/ell1 partial spatial energy `64+4d`, `d=0,1,2,3,4`. These imply each full coefficient is one of `-12,-4,4,12`. Full Parseval gives exactly eight magnitude-4 coefficients. Independently enumerate the ordered pair values, not a freely selected spatial Y: `A1` has magnitude 0,4,8,12, with counts `Z,O,E,P`. For `O`, `H` counts `A0=0`; for `Z`, `Z4` counts `|A0|=4`. All six counts are nonnegative integers, with `E+O+P+Z=32`, `H<=O`, `Z4<=Z`,

`E+O+H+2 Z4 = 8`, and `O+4E+9P = 128+8d`.

The six actual ordered-pair signature types are `(E,one small, A1²=64)`, `(O,A0 nonzero,one small,16)`, `(O,A0=0,two small,16)`, `(P,no small,144)`, `(Z,|A0|=12,no small,0)`, `(Z,|A0|=4,two small,0)`. Their multiplicities give the exact following **written arithmetic** table; `(H,Z4)` lists every permitted pair for that displayed `(E,O,P,Z)`. This table is not an executed checker result, and no entry asserts a realizable spatial Y or common physical object.

| d | (E,O,P,Z) | all (H,Z4) |
|---|---|---|
|0|(0,2,14,16)|(0,3),(2,2)|
|0|(1,7,13,11)|(0,0)|
|0|(2,3,13,14)|(1,1),(3,0)|
|0|(4,4,12,12)|(0,0)|
|0|(7,1,11,13)|(0,0)|
|1|(0,1,15,16)|(1,3)|
|1|(1,6,14,11)|(1,0)|
|1|(2,2,14,14)|(0,2),(2,1)|
|1|(4,3,13,12)|(1,0)|
|2|(0,0,16,16)|(0,4)|
|2|(1,5,15,11)|(0,1),(2,0)|
|2|(2,1,15,14)|(1,2)|
|2|(4,2,14,12)|(0,1),(2,0)|
|3|(0,8,16,8)|(0,0)|
|3|(1,4,16,11)|(1,1),(3,0)|
|3|(2,0,16,14)|(0,3)|
|3|(3,5,15,9)|(0,0)|
|3|(4,1,15,12)|(1,1)|
|3|(6,2,14,10)|(0,0)|
|4|(0,7,17,8)|(1,0)|
|4|(1,3,17,11)|(0,2),(2,1)|
|4|(3,4,16,9)|(1,0)|
|4|(4,0,16,12)|(0,2)|
|4|(6,1,15,10)|(1,0)|

The `d=0,2,4` four-count projections agree by this written calculation with the unadopted f748 table S2 LF102–108. For example, the formal d=0 candidate `(5,0,12,15)` meets the partial-energy equation but cannot reach eight small coefficients: it would need `2 Z4=3`. Odd-d rows above describe the U3-only arithmetic relaxation; they are **not** physical odd-d witnesses. The graph zero-eta/parity and E-side physical support constraints are additional; under the named imports they separately force even d. The proposed program independently generates all six pair signatures from the 16 ordered full-value pairs, enumerates all six-count tuples at all five d, and reports exact set differences for each declared even-d table. Its named controls separately mutate residue, cap, total energy, partial energy, pair count, `H`/`Z4` bounds, small census and a declared table. No control has been executed.

## Omitted lambda singleton and a concrete local discriminator

The profile import S8 LF15 allows either a single `+/-2` **or** four `+/-1` on an affine two-flat with odd sign product. In f748 S2 LF49 the stated reason for discarding graph-lambda-zero at `d=0` treats only four E-side `+/-1` entries: these indeed require at least eight nonzero E-side x sites. It does not eliminate the allowed one-E-side `+/-2` profile, which needs only four such sites. The same missing alternative occurs in the lambda-only arguments at S2 LF52 and LF54. Thus those arguments are incomplete as written; the heavy-row analysis is conditional unless the singleton is excluded by some additional shown hypothesis. This is **not** a counterexample to f748's full simultaneous seven-profile/common-U3 physical hypotheses and does not automatically invalidate the odd-d parity result.

A completely specified local site-pattern discriminator shows why this is not merely a phrase about formal profiles. Take the packet's odd graph-height table `F=(0,0,0,1)`, identify b with `0,1,2,3` using the two bit coordinates, and let every graph row have sign character `g(b)=(-1)^b0`. For graph occupancy `4000`, take the four D0 mates of row i=0 as `2(-1)^b1` and all other graph mates zero. For `2200`, instead take both i=0 and i=1 mates as `(2,-2,0,0)` in b order and the other mates zero. Both choices have zero row sum, even total graph negative-sign parity, graph lambda zero, integral local eta values and local magnitude at most two. On ell0 choose i=0, h=0 x-values `+2` at b=1,2 and h=1 values `-2` at the same two sites. At i=1 put `+2,-2` at b=1,2 in h=0 and put zero on every other ell0 site. The two full i=0,b=0 sites remain zero; the six nonzero ell0 sites are actual Z2 positions, no E D0 occurs, and every ell0 row has zero eta, integral local transforms and local magnitude at most two. The lambda vector, in the order four ell0 rows then four graph rows, is `(2,0,0,0;0,0,0,0)`, an allowed singleton. The 18 remaining zero-x Z sites leave places for the one Z4, but no Z4, Y, u, V, remaining six global columns, original carried t, or full caller is constructed here. These are local x/site patterns, **not** asserted full physical fixtures.

The proposed source independently enumerates graph signs `+/-1` and each same-b mate in `{0,+2,-2}` for both h bits, all five local k values, the zero-eta equation and every local eta entry; it checks `p=k mod 2` and the signed lambda identity. It then enumerates actual ell0 F/E/Z site domains with six Z2, `d` E D0, zero eta and per-row local bounds, combines them with **all 128** allowed signed lambda profiles and all 70 labeled `(k0,k1,k2,k3,d)` placements, and records actual row-pattern witnesses. A dedicated positive control requires singleton examples for both `4000` and `2200`, and another reason control checks that a four-entry ell0 profile requires eight rather than six nonzero sites. The source samples `F=(0,0,0,1)` for the assembled local examples, while separately checking both individual graph h bits. It does **not** claim simultaneous full-column profiles, arbitrary f/R assembly, all-kappa character behavior, or Y feasibility.

## Physical heavy-row Fourier check

The d=4 heavy-row exercise is conditional on the four-E-side-`+/-1` lambda branch, not a proof that the singleton branch is impossible. For a physical 3-site h-cell let its signed `X/2` values be `c(-1)^{alpha*(b)}` on the three sites and let `q` be the missing b point. Zero row sum makes the one physical site in the other h-cell have sign `c(-1)^{alpha*(q)}`. The triple sum is `+/-1`, so `alpha*` is nonzero. Set `p_i,q_i` as the h=0/h=1 actual or virtual coordinates exactly as in f748 (the missing point is virtual), and `a_i` as the h=0 sign sum. For `alpha != alpha*`, orthogonality of the completed character gives

`Z_i(s,alpha) = (a_i/2) [(-1)^alpha(p_i) - (-1)^s (-1)^alpha(q_i)]`.

The omitted term's sign is essential; for `alpha=alpha*` the triple contributes three aligned terms, and the two actual normalized magnitudes are 1 and 2, not the generic formula. V2 proposes to exhaust both heavy orientations, all physical missing/single coordinates and all zero-mean triple signs, rule out the actual two full sites, and retain a heavy pattern for **every** reachable d=4 E occupancy `2+2` or `2+1+1`. It checks both corresponding light-row formulas and exact six-Z2/four-E-site extendability. Its named controls flip the actual heavy missing sign and the formula's minus sign. Different shape counts can overlap when the same heavy row has more than one type of light-row extension. No run or combined seven-profile assertion is made.

The sole displayed fixture whose X bytes are reconstructed by the program is the explicit d=4 X-component of packet S4 LF29: the program proposes to calculate its actual X Walsh flags and the singleton lambda. It does not invent unspecified Y signs, a Z4 site, ternary u or an original physical caller. Flags, should they be produced, concern that literal X component only.

## Coverage, assurance and frontier

After actual dispatch, I read the manifest, freeze receipt, final binding, prepared metadata and all 22 controls through their endings, then directly delivered the PREBODY ACK to Main. Only afterward I serially read the one complete packet part, all 761 LF in raw windows of at most 20 LF, including its ending, before mathematical comparison or research. All eight source blocks are complete, totaling 727 source LF. Metadata pins: manifest `626d4666879c2613af0f96ededa8a274309e2a93c3b135501eb0e7002f30a637`; freeze receipt `2157b3db7db2872bbb7cb85cbf6fd0fba8a497c5152c7a4c7431eeb84bd5be8a`; final binding `f78d6b20c0b3948c6c5ee0b59cae96a28b6582fd11ca61a10355dc26e88c9cbb`; prepared metadata `ffb5c502d0931f74279e76a3bca980d2aa0fedb53f291a4a4611e77bde06be60`; actual dispatch `90975dae886e437c6940cc49734e4c0e6e005c6b42ac888e5762135411a37909`; packet `b20d2dcb228e52740495f5353adaf911155363b940e861bd86c3c055e2dbda64`. These metadata hashes do not constitute independent source-identity or scientific verification. The parent-supplied complete-body source pins are S1 `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c`; S2 `09b37a6329453627d4d6c633c7363d8e54b7c84bb13f43fe54372b745036be55`; S3 `4e02d9a0a277fb830db497552d2e52e61f02e6c2a029e7b6fb71d47dc06cd17a`; S4 `3a1899e8000395700de08015f06ae397288164c3c092fc2e799751594ed7bcb5`; S5 `44fc6d7c1f177a22eba29d295889220761f540a427bb84a7b7f9d9912cc52bf9`; S6 `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928`; S7 `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef`; S8 `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`.

No held payload/history, held consumer, old checker code, unspecified sibling proof, outgoing link, solver, scientific program, CAS, compile, test, lint, formatter or external-model CLI was used. All genuinely held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. The imported f749 parent-run receipt is evidence only at its expressly local/lambda scope, not a simultaneous-profile witness. Open frontiers are all seven full profiles of one actual x, complete physical ternary inverse and same Y with its 64 caps, actual J and carried t, complementary V and original rank/source caller. This work supplies no family, human, kernel, formal, novelty, original-source-identity, global theorem or parent-adoption assurance. Observed native clock before this report's creation: `2026-10-30T17:47:30-0700 PDT`; it is a lower bound on creation, not a backdated creation timestamp.
