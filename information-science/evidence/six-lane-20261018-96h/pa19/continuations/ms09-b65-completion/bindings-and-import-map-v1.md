# b65 source bindings, premise map and review interface v1

Written after host clock 2026-10-19T17:02:50-0700. Main claim: proof-v1.md, SHA256 80241121fe3e97e46e446e96cd7ca83c90fd80001f67fd444749718e107b43f0 (20414 bytes, 274 lines), a candidate whole fixed-skeleton exclusion, not accepted or runtime-qualified. Scope: scope-v1.md, SHA256 edda4fc49fe722ae1e26cb36f095ac00d6d3f1b9ad996f2c30d920a577db77f5.

## 1. Sources and exact raw excerpts

S = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json; SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0.

E = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/code/vendor/encode_skel_b.py; SHA256 d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5.

V = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v10.json; SHA256 29c7cbe8e22cdad3bb1d196f9df12d9336652cb4942dc9538ac6d22225ebd90a.

All byte ranges below are ZERO-based half-open; all line ranges are ONE-based inclusive. Excerpt files are exact raw byte copies, with no line prefixes or whitespace compression. S has one physical line, no LF: its byte selector is the precise identity, not a claim that a one-line excerpt is the whole source.

| excerpt file | source; selector | source byte range | bytes | SHA256 |
|---|---|---|---|---|
| source-S-header-v1.txt | S; partial line 1 | [0,433) | 433 | 1d14c68a539a0fc5011edeb4fff7050cf3f6a6f616195c1bc023f8964ca229eb |
| source-S-b65-v1.txt | S; partial line 1 | [4421,4503) | 82 | 010b2b819f60b937e449a6af5ab88b711709fcae840ff226bb14af0895b28818 |
| source-E-row-order-v1.txt | E; lines 3-8 | [114,507) | 393 | d2badacac8e8224914d82ed27f64ee212b0ec1d9d99ed4c3d4ed8488e28f9790 |
| source-E-membership-v1.txt | E; lines 77-99 | [3404,4286) | 882 | 92f988ec1c8e36fbf50616e84c94847ca6ffd439c642bbaaba7bd891b7e94fe7 |
| source-V-b65-v1.txt | V; lines 4788-4835 | [66999,67656) | 657 | e12ea6fde5df9aaeb790a8eb2bf7fe3f55710a21efc23bffab2f63ec3af384a8 |
| source-V-counts-v1.txt | V; lines 4956-4962 | [69362,69793) | 431 | a1341e1410a87247f7af368f07615eebee1d452c655dced969d0cce976d9a400 |

S's header gives multiset 9, the exact eight profiles, c0=5, L=0, 71 skeletons. Its b65 entry gives precisely the seven types and seven empty rows stated by the theorem. E's two excerpts explain that each listed type is one row, followed by 4-deg(c) private rows for each c and then empty rows, and fix P0 symbol-0 membership. Each b65 degree is 3, giving one p_c per index and 7+5+7=19 distinct rows. The theorem is about this explicit array class: no certification of every encoder clause, its caller, a generated CNF, any historical run, the placement lists or skeleton enumeration is assumed.

V binds this explicit class to a current unresolved b_index 65 entry. Its skeleton_types and skeleton_empty are the same displayed content as S's byte entry; this is semantic content equality, not byte equality of differently formatted JSON. The s_tag/contract_mapped_tag ms09_s00052 is merely historical. The list n=2655, raw=59830, aut=12, interval count 27 and ext.json pin in that entry are not proof premises. The snapshot V predates this candidate, has ms06=70, ms09=59, total=129, and is not conflated with historical v9's 132 or lane-original 151. No worker edit changes V or any count.

## 2. Exact premise and consequence map

Every mathematical input is the theorem's four explicit assumptions and elementary integer counting; all other facts used are proved in proof-v1 itself.

| proof location | obligation / output | dependencies |
|---|---|---|
| Theorem and fixed case | Exact labelled b65 class; Q_0,...,Q_4 | S-header, S-b65, E row-order/membership definition bridge |
| 1.1 | Every pair agrees exactly once; T-disjointness and block-intersection rule | Four theorem assumptions; 5*21+3*22=C(19,2) |
| 1.2 | All row patterns; empty rows in two P1 quads/one triple/no pair | 1.1; partner-count identity |
| 1.3 | Exhaustive one-excess occupancy categories | 1.1-1.2; balancing and explicit sum/square identities |
| 1.4 | I(r)=7 and the two possible private rescue blocks | 1.1-1.3 |
| 2.1 | g's two pairs, partners p3,p4; H_C with three empties; g's two occupancy-2 P0 triples | 1.2-1.4 and exact type list |
| 2.2 | Q1; L_C={p0,p3,p4,e0}; L_A,L_B occupancy 2; high quads occupancy 3; C-triples occupancy 1 | 2.1, private rescue, explicit S3 normalization |
| 2.3 | {i,j}={1,2}, pi in L_A, pj in L_B; all P0 triples of p3,p4,pi,pj occupancy 1 | 1.2,1.4,2.2; no choice of i versus j omitted |
| 3 | Forced actual-empty quad table; exact missing-pair graph M and g matching (G) | 1.1-1.3,2.1-2.3; explicit 3<->4/A<->B symmetry; actual-row matching obstruction |
| 4.1 | f(w)=5-deg_M(w); P0 empty-partner sets S and J | 2.3,3; exact pair cover |
| 4.2 | Seven O triples, with exactly one carrying each actual empty row | 4.1; p3,p4 already agree in L_C |
| 4.3 | Column-4 p3-pi triple; shared pi-pj-e0 triple; c_j=v'; {w3,w4}={u,u'} | 4.1-4.2, exact nonempty partner lists and no repeated agreement |
| 4.4 | All full completions contradicted in P0 column 4 | (G),4.2-4.3, partitioning the seven actual empty rows |

The decisive new obligation is fully discharged as a written candidate: every completion of the joint P0/P1/empty-row problem would give the Section 3 table and the O-to-E bijection; column 4 would then contain two H_C empty rows together. This is a contradiction for every actual-row filling, not merely for an occupancy or nonempty projection. There is no surviving full-array branch claimed by this proof. This sentence records the candidate's scope, not independent acceptance.

## 3. Prior candidates and erratum interface

The earlier e7 dossier (manifest 8773ac590e8456b132fcbcf70c7b9558142328891f74d02d8af13111286d88ba) is context only. Its pair-exactness, row patterns, five categories, I(r), rescue and b65 high/low normal-form facts are independently re-derived in Sections 1-2 here. Its actual-empty graph/matching ideas are independently re-derived in Section 3. No unreviewed e7 implication is imported as a premise.

The e7 Codex PASS, structural Theorems A/B, AT2 and its equality clause, Petersen girth, C-pair orbits/path cases, high-quad zero-triple relation, and the earlier displayed P0-incompatible branch are NOT USED. In particular the new closure does not rely on either family having accepted e7. The proof even avoids needing AT2 to separate pi and pj in C: the unique O triple carrying e0 separates them.

Parent e7 erratum /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-e7-excess-parent-erratum-v1.md (SHA256 fc48075bd3ce91a72a3b039695c54705705cb3cb77b5cc942c6433fd39d5abd2) is included as reference context, not a theorem premise. Its three wording repairs are explicitly respected:
- An empty edge determines its missing column only; any particular triple is further data. Section 3 states exactly this, and later triple identities follow from the occupancy-one/bijection/partition arguments.
- The exact 3<->4/A<->B automorphism and its row map are written out. No unstated orbit reduction is used.
- v9 is historical; V=v10 is the pre-result 129 snapshot. Candidate count or acceptance is parent-owned.

## 4. Symmetry ledger and review boundary

1. Name the three equal-profile P1 columns A,B,C using g's two distinct pair partners. This is column naming, not a first-column placement restriction.
2. A permutation of {0,1,2} maps P0 Q_k and a_k,b_k,p_k by the same permutation, fixes g,p3,p4, and preserves every profile. It places the extra private row of L_C at p0. The remaining p1,p2 are retained as arbitrary pi,pj.
3. Simultaneously swap P0 indices 3,4, rows a_k,b_k, private rows p3,p4 and P1 columns A,B. The pair normalization and L_C remain invariant. This places e0 in H_A and preserves the preceding choice p0.
4. Remaining empty labels u,u',u'',v,v',v'' name positions proved forced by exact row identities and degrees. They are not interchangeable slots after assignment.

The review package includes scope, the FULL current proof, this FULL map, raw definition/status excerpts, the full slot authority and the parent e7 erratum. It is self-contained for the written theorem. External execution provenance, finite controls, runtime admission, skeleton-list/global PA19 completeness and novelty are outside the proof. Parent must independently read/check it and obtain both-family hostile review before ledger acceptance. Prior runtime HOLDs and UNKNOWNs are unchanged. No build, import, scientific computation or test was performed.

Process deviations: scope discloses the pre-freeze in-session sketch; checkpoint-001 discloses the earlier wait checkpoint gap. These disclosures remain immutable and are not erased by a candidate theorem. Files were exclusive-created only in this assigned continuation directory.
