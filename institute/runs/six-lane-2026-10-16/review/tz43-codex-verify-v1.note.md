RESULT: VALID
gcDCQS(18^4:2): VALID
FDGDD(3,4,5{18}): VALID
mcDSQS(74) ASCII: VALID

FATAL: none  
MAJOR: none  
MINOR: none

All three SHA-256 hashes and byte lengths match the supplied pins and manifest. The definition excerpt also matches its manifest pin. No discrepancy was found in the working restatement.

References below use physical LF numbers in the pinned files. Applied definitions:

- GDD, type, STS/SQS, PPC/PC: `tz43-definitions-formats-excerpt.txt:12–30` ([B] LF 48–72); derived designs: `:34–35` ([B] LF 78–79).
- Colouring, chromatic index, (1.1), mcSTS/mcDSQS: `tz43-definitions-formats-excerpt.txt:39–79` ([B] LF 90–130). Recomputed χ′(73) = 37.
- gcSTS: `tz43-definitions-formats-excerpt.txt:87–96` ([B] LF 211–220); KF: `:113–116` ([B] LF 237–240).
- FDGDD: `tz43-definitions-formats-excerpt.txt:117–123` ([B] LF 241–247); CQS: `:132–142` ([B] LF 256–266); gcDCQS: `:157–164` ([B] LF 281–288).
- Formats S/D: `tz43-definitions-formats-excerpt.txt:174–191` ([C] LF 114–131).

Strict ASCII, LF termination, canonical decimal records, distinct points, section structure and complete record consumption passed. Noncomment records consumed: **78,151 / 76,238 / 83,845**, respectively.

Profiles below mean **triple count : number of classes**, per point.

| Certificate evidence | Exhaustive verification |
|---|---|
| `gcdcqs18_4_2_z8z3z3.txt:2–12`, `:15079`, `:76783` | Header **74,4,18,2**; four 18-point groups and two-point stem partition X. **15,066 distinct blocks**. Of **64,824 triples**, **60,264 occur once**, and **4,560 forbidden triples occur zero times**. Every one of 72 group points has exactly **819 derived triples**, with **2,457 allowed pairs once / 171 hole pairs absent**. Each has **37 consecutive nonempty PPCs**, exactly **10 hole-avoiding**; every hole point has degree **27**. Profile: **16:1, 17:4, 18:5, 23:3, 24:24**. Both stem points have **648 derived triples**, with **1,944 cross-group pairs once / 612 within-group pairs absent**; **36 FRAME PCs**, each covering the prescribed 54 points with **18 triples**, **nine per missed group**. |
| `fdgdd_5_18_inflated_D15.txt:1–8`, `:14589` | Header **GDD34 FDGDD 5 18**; five 18-point groups partition **90 points**. **14,580 distinct transverse blocks**. All **58,320 transverse triples occur once**; all **59,160 other triples are absent**. Every point has exactly **648 derived triples**, satisfying the 72-point GDD pair condition (**1,944 once / 612 absent**). Each has **36 FRAME PCs**, profile **18:36**, covering the prescribed 54 points, with **nine per allowed label** and no own-group label. |
| `mcdsqs74_c21_ascii.txt:3–5`, `:16212` | Header **MCDSQS 74**, **COLOURS 37**. **16,206 distinct blocks**; all **64,824 triples occur exactly once**. All 74 ordered point sections partition exactly **876 derived triples**, with all **2,628 pairs once**, into **37 consecutive nonempty PPCs**. Profiles: **72 points: 21:1, 22:2, 23:5, 24:29**; **two points: 22:4, 23:4, 24:29**. PPC capacity is **24**; **⌈876/24⌉ = 37**. |

Nine controls were constructed as corrupted byte strings in memory, reparsed, and checked by the same verifier. References identify original input LF anchors.

| Control | Intended invariant → observed rejection |
|---|---|
| gcDCQS: move triple `gcdcqs18_4_2_z8z3z3.txt:15273` between classes at `:15264` and `:15080` | Hole-avoiding count → **HOLE_AVOIDING_COUNT: 9 instead of 10**. Explicitly confirmed every class remains a PPC and the triple partition is unchanged. |
| gcDCQS: move `gcdcqs18_4_2_z8z3z3.txt:15289` into another CLASS | PPC disjointness → **CLASS_PPC_COLLISION**, repeated points **{1,27,50}**. Triple partition preserved. |
| gcDCQS: exchange points 9↔10 in blocks `gcdcqs18_4_2_z8z3z3.txt:13–14` | Triple coverage → **GLOBAL_TRIPLE_MULTIPLICITY**, triple **(0,9,45)** occurs twice; second occurrence at `:253`. Block distinctness, point degrees and forbidden-triple exclusion preserved. |
| FDGDD: exchange same-group points 36↔37 in `fdgdd_5_18_inflated_D15.txt:9–10` | Triple coverage → **GLOBAL_TRIPLE_MULTIPLICITY**, triple **(0,36,62)** occurs twice, detected at `:36`. Transversality and block distinctness preserved. |
| FDGDD: move `fdgdd_5_18_inflated_D15.txt:14591` between two FRAME 1 classes | Parallel-class coverage → **FRAME_PC_DOMAIN**, source has **17 triples**, missing **{36,54,72}**. Triple partition and label counts preserved. |
| FDGDD: relabel `fdgdd_5_18_inflated_D15.txt:14590`, FRAME 1→2 | Labelled PC domain → **FRAME_PC_DOMAIN**, missing **18–35**, extra **36–53**. Triples and disjointness preserved. |
| mcDSQS: exchange points 2↔42 in `mcdsqs74_c21_ascii.txt:6–7` | Triple coverage → **GLOBAL_TRIPLE_MULTIPLICITY**, triple **(0,2,3)** occurs twice, detected at `:42`. Block distinctness and point degrees preserved. |
| mcDSQS: change `mcdsqs74_c21_ascii.txt:4` to COLOURS 38 | Required colour count → **COLOURS_CHI**, **38 instead of 37**. |
| mcDSQS: move `mcdsqs74_c21_ascii.txt:16237` into another CLASS | PPC disjointness → **CLASS_PPC_COLLISION**, repeated points **{1,3,42}**. Triple partition preserved. |

After all controls, the original files were reread, their pins rechecked, and the complete verification repeated: **all passed with identical results**.

Measured verifier run: **11.81 s wall**, **11.80 s CPU**, **127.44 MiB peak RSS**; one sequential Python process, no threads created. No files were written. External sources and construction/provenance assertions in comments were not checked.