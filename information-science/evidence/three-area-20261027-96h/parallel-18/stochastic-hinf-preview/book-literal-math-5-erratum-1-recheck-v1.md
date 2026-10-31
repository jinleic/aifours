# B5 erratum 1 — documentary recheck against the pinned page images

**Verdict: EXACT_WITH_ERRATUM** for the five items below and the deviations/uncertainties in my prior comparison, at the supplied image resolution. No deviation from those prior comparison findings remains after applying the additive erratum. This is a same-harness documentary-fidelity finding, not a mathematical or lane-input acceptance.

**Actual native prewrite clock:** Wed Oct 28 10:03:32 PDT 2026.

## Frozen inputs and actual coverage

- Entire recheck release read through its closing brace, SHA-256 `245972c9f7c5980ddfd37575282d6aeda690a543475dd36c8bc1aae4d931474d`; no new pre-body ACK required by its explicit order.
- Entire `book-literal-math-5-v1-erratum-1.md` read in raw windows 1–55, 56–110, 111–144 through its ending; SHA-256 `bbdff72096e293cf1c759e1ed62fb6898b3b6ae9feabf71adb983991db5266b1`, 144 LF / 9930 bytes.
- Entire prior comparison read through its ending, SHA-256 `188b750c398f75139eb2ebed427637c27e114472df3ceea3e25d60c15574fd25`. The erratum-return receipt was read as metadata only, SHA-256 `acb413e1315e4cad72304fa4c1c0555dff7e1f88995d4af4a1340fb6fdaf80de`.
- All four listed image hashes matched before recheck. Visually opened BOTH entire 300-dpi pages and in-memory crops of those SAME two pinned images: printed p.64/PDF80 `source-math-0080-r300.png`, SHA `40929ee1f4f5dcad370c4b25ce404e3e448688b43295cba3c1260e9dda880803`; printed p.65/PDF81 `source-math-0081-r300.png`, SHA `0cdd9fda3b34a6c0716bbf67cd92aa175b3db7c7b9f82616913955bf0e5c98d9`. The corresponding 150-dpi pins `e2c67ba6010edeefb71e104b056d203f64060ba5fd059da273c918091ab5ed8f` and `0bad7cfb52328592848919db2173184c5147339ca553600cb22362af688b61fc` also matched; those whole pages had been viewed in the original comparison. No unlisted image or page was opened.

## Item-by-item verdict

| Erratum item | Verdict | Actual visual comparison |
|---|---|---|
| **1. M1/U1: p.64 contextual reference clause and aligned English** | **CONFIRMED** | The first body paragraph's third printed line in the 300-dpi crop reads `也可参看我们平行于这里的一个有关的专门介绍`. The span after `我们` is the two glyphs `平行`, as the erratum states. The English rendering retains “parallel to here” as a literal, explicitly **AMBIGUOUS** phrase; no referent is resolved. This replaces the previous unresolved `⟦U1⟧` in the stated Chinese/English lines. |
| **2. M2/U4: p.65 printed reference [2]** | **CONFIRMED** | The 300-dpi reference crops show the venue word `internet.` and the printed string `Perrrin D, Schutzenberger M P. Un probleme elementaire de la theorie de linformation.` The three consecutive `r` characters and absence of an apostrophe in `linformation` are as printed in the supplied image; neither was normalized to an outside bibliography. This replaces the unresolved `⟦U4⟧` and the two newly noticed v1 spelling/punctuation differences in that same reference. |
| **3. m1: p.64 definition and inventory `元素`** | **CONFIRMED** | The enlarged second body paragraph visibly says `称 X* 的元素（子集）为 …`. Adding `素` after `元` in both the body and D2 inventory matches the printed wording. The aligned English `elements (subsets)` remains as stated. |
| **4. U2: p.64 completeness display final glyph** | **CONFIRMED** | The enlarged display ends with the capital **Φ-shaped printed glyph**, rendered `\Phi` in the erratum. The original provisional typeform is thus confirmed as the observed glyph; no different symbol or interpretation is assigned. |
| **5. U3: p.65 reference [1]–[2] visible diacritics** | **CONFIRMED AT SUPPLIED RESOLUTION** | In the enlarged 300-dpi reference crops, no diacritic marks are visible on the named author/French letterforms. The base-letter reference [1] and the corrected printed reference [2] match what is visible; no unprinted accents or bibliographic spelling are inferred. This confirms what the admitted images show, not an external bibliographic record. |

## Effect on the original comparison

With erratum 1 applied at its stated lines, both previous MAJOR gaps (**M1/U1** and **M2/U4**) and the MINOR omission **m1** are resolved by the displayed source. The prior provisional **U2** typeform and **U3** fine-letterform qualifications are confirmed at the stated image resolution. Reference [2]'s additional `Perrrin`/`linformation` corrections are also visibly correct and must be carried together with the `internet.` correction; the old packet and previous comparison are unchanged. The sentence's referent in `平行于这里` remains **AMBIGUOUS** by design, not a purportedly solved interpretation.

My original comparison confirmed **TRUNCATED: NO** for the two displayed pages. This focused erratum recheck does not broaden that two-page coverage, claim exactness of a different edition or independently authenticate the whole PDF. The original comparison was not a claim that every fine typographic mark was exact; this verdict is limited to the five corrected items and its identified deviations/uncertainties, not a new source-wide audit.

## Method and continuing limits

The previous ACK `book-literal-math-5-comparison-prebody-ack-v1.json`, SHA `f97090fd7782cf5f4adf5bfd24cd029b8ea9998ac0e64e5871390f4da950b50a`, was retained without a new ACK as the frozen recheck release directs. The original and erratum files remain immutable.

For THIS recheck, Python/PIL through the Eval tool was used **only as an in-memory documentary image viewer** to display crops of the two explicitly admitted 300-dpi pages; no crop or other file was written, and no OCR, mathematical/scientific calculation, selected diagnostic, solver or data extraction was performed. This use is disclosed rather than being described as “no Eval”; the earlier no-Eval/no-scientific-execution statement in the original comparison concerns that earlier comparison. The return receipt likewise records the transcriber's separately disclosed image-only viewer use. All other action/source restrictions persist.

No author or lane owner was contacted, no bibliography or other source followed, and no lane proof, held/withdrawn/ZERO material or mathematical interpretation was consulted. The parent pre-gate display MINOR, all STOP/HOLD/ZERO controls, local copyright boundary, scientific HOLDv2, N4 UNKNOWN historical child exit and auxiliary214 STOP remain. This report does not release the packet to the lane, assess current status/priority, verify mathematics or confer formal/human/configured-family/novelty acceptance.
