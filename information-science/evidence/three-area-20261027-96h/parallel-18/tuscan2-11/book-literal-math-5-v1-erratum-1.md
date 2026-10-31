# B5 — literal transcription erratum 1

Transcriber: **InfoRecursiveMDS18-2**, info-4. Actual native prewrite clock: **Wed Oct 28 09:56:08 PDT 2026**. The pinned v1 is unchanged; this file is additive.

- v1: `book-literal-math-5-v1.md`, SHA256 `52c10cef1e2f65a551f5a5ea8b11db381e4b55e192c8c725cf94dded8878ac08`.
- Comparison: `book-literal-math-5-comparison-v1.md`, SHA256 `188b750c398f75139eb2ebed427637c27e114472df3ceea3e25d60c15574fd25`.
- High-resolution gate addendum: SHA256 `ff7ea3920b3707f04070df25c16d2b64a9f1f9d7cc3c3a03a2621b12501a28d2`.
- Printed p.64/PDF p.80 images: `source-math-0080.png`, SHA256 `e2c67ba6010edeefb71e104b056d203f64060ba5fd059da273c918091ab5ed8f`; `source-math-0080-r300.png`, SHA256 `40929ee1f4f5dcad370c4b25ce404e3e448688b43295cba3c1260e9dda880803`.
- Printed p.65/PDF p.81 images: `source-math-0081.png`, SHA256 `0bad7cfb52328592848919db2173184c5147339ca553600cb22362af688b61fc`; `source-math-0081-r300.png`, SHA256 `0cdd9fda3b34a6c0716bb67cd92aa175b3db7c7b9f82616913955bf0e5c98d9`.
- Inspection: the listed full-page images and in-memory magnified crops of the same 300-dpi images were visually displayed. The crops were displayed with a Python/PIL image viewer; no crop file, OCR text, scientific calculation or additional page was produced.

## 1. M1 / U1 — contextual reference clause

**V1 Chinese, LF38:**

> 在 M.P.Schutzenberger 于1955开创的“变长度码理论”中[1]，除了“码交换等价于前缀码”的猜测及其局限于“有限极大”情形的猜测外（见文献[2]，[3]，也可参看我们⟦U1⟧于这里的一个有关的专门介绍），另一个主要的公开问题就是“有限码具有有限完备化的判定问题”. 这一问题的背景是，许多有关“编码过程优化”的问题都涉及码的一些极端性质，诸如“极大性”，“完备性”等；另外，这一问题与“有限极大码交换等价于有限极大前缀码”的猜测[3]也有密切的联系.

**V1 English, LF185:**

> **[E64-P1.s1 ↔ C64-P1, sentence 1]** In the “variable-length code theory” initiated by M.P.Schutzenberger in1955[1], besides the conjecture that “codes are exchange-equivalent to prefix codes” and the conjecture restricted to the “finite maximal” case (see references[2],[3]; one may also consult our ⟦U1: unclear printed glyph⟧ here, a related special introduction), another main open question is “the decision problem for a finite code having a finite completion”.

**V1 uncertainty, LF269:**

> | U1 | source-math-0080.png, printed64, C64-P1, third text line around y476, immediately after “我们” and before “于这里” | One glyph is not reliably resolved between a 刊-/行-shaped reading. It is left as `⟦U1⟧`, not supplied from another text. The corresponding English clause retains the same gap. |

**Corrected printed Chinese:** printed p.64, first body paragraph, third printed line, displayed-preview y≈476; the 300-dpi page's in-memory view of original pixel rectangle (285,875)–(1840,1135) shows:

> 也可参看我们平行于这里的一个有关的专门介绍

The omitted span after “我们” is **平行**, two printed glyphs. Replace `我们⟦U1⟧于这里` by `我们平行于这里` in LF38. **RESOLVED** from the image.

**Corrected literal English for the same clause:**

> one may also consult a related specialized introduction of ours parallel to here

The phrase “平行于这里” is **AMBIGUOUS**; the rendering retains its literal wording without resolving its referent. The corrected LF185 sentence is:

> **[E64-P1.s1 ↔ C64-P1, sentence 1]** In the “variable-length code theory” initiated by M.P.Schutzenberger in1955[1], besides the conjecture that “codes are exchange-equivalent to prefix codes” and the conjecture restricted to the “finite maximal” case (see references[2],[3]; one may also consult a related specialized introduction of ours parallel to here), another main open question is “the decision problem for a finite code having a finite completion”.

**Inventory:** the quoted conjecture strings in v1 LF261 do not contain this contextual reference clause; no inventory entry is changed for M1.

## 2. M2 / U4 — printed reference [2]

**V1 reference, LF152–153:**

> [2] Perrin D, Schutzenberger M P. Un probleme elementaire de la theorie de l'information.  
> Colloques intern⟦U4⟧t. CNRS 276, Cachan 1977, 249-260

**V1 uncertainty, LF272:**

> | U4 | source-math-0081.png, printed65, C65-R2 second line around y820, `Colloques intern…t.` | One letter appears a-/e-shaped. It is left as `⟦U4⟧`; the word is not normalized to a presumed bibliographic spelling. |

**Corrected printed reference:** printed p.65, bibliography [2], displayed-preview y≈787–832; 300-dpi original pixel view (285,1590)–(1840,1910), with the author spelling also displayed in crop (365,1730)–(720,1815):

> [2] Perrrin D, Schutzenberger M P. Un probleme elementaire de la theorie de linformation.  
> Colloques internet. CNRS 276, Cachan 1977, 249-260

The observed missing letter is **e**, yielding `internet.` The enlarged printed reference also shows **Perrrin** with three consecutive `r` characters and **linformation** without an apostrophe; they are copied as observed in the same listed reference, not normalized. **U4 RESOLVED** from the image.

**Corrected literal English:**

> [2] Perrrin D, Schutzenberger M P. An elementary problem of the theory of information. Colloques internet. CNRS 276, Cachan 1977, 249-260.

The printed title/venue string is retained verbatim immediately above; no alternative bibliographic spelling is supplied. **Inventory:** no v1 printed-definition inventory entry quotes reference [2], so none is affected.

## 3. m1 — 元素 in the definition and inventory

**V1 Chinese, LF42:**

> 令 \(X\) 是一有限集，\(X^*\) 是由 \(X\) 生成的自由幺半群. 称 \(X^*\) 的元（子集）为 \(X\) 上的（半群）字（语言）；称自由幺半群 \(X^*\) 的幺元1为 \(X\) 上的空字；称 \(X\) 上一非空语言 \(C\) 为 \(X\) 上一（代数）码，如果

**V1 inventory, LF244:**

> | D2 / C64-P2 | “称 X* 的元（子集）为 X 上的（半群）字（语言）” |

**Corrected printed Chinese:** printed p.64, second body paragraph, displayed-preview y≈584–659:

> 称 \(X^*\) 的元素（子集）为 \(X\) 上的（半群）字（语言）

Insert the printed character **素** after **元** in LF42.

**Corrected literal English:**

> The elements (subsets) of \(X^*\) are called (semigroup) words (languages) over \(X\).

This is the same wording already present in v1 LF191; it is included here as the aligned rendering.

**Corrected inventory entry replacing LF244:**

> | D2 / C64-P2 | “称 X* 的元素（子集）为 X 上的（半群）字（语言）” |

## 4. U2 — final glyph in the completeness display

**V1 formula, LF80:**

> \forall w\in X^*,\quad X^*wX^*\cap C^*\ne\Phi.

**V1 qualifier, LF83:**

> The final printed glyph in C64-F5 is provisionally copied as \(\Phi\); see **U2**.

**V1 inventory, LF253:**

> | D11 / C64-P6/F5 | “称 X 上一码 C 是完备的，如果”; `∀w∈X*, X*wX*∩C*≠Φ` (final glyph U2). |

**V1 uncertainty, LF270:**

> | U2 | source-math-0080.png, printed64, C64-F5, final glyph around y1078 | The glyph is Φ-shaped; the exact typeform is uncertain. It is provisionally copied as `\Phi`. No meaning or alternate notation is assigned. |

**Printed Chinese and display:** printed p.64, body y≈1027–1051 and display y≈1078; enlarged original pixel view (520,2250)–(1450,2460):

> 称 \(X\) 上一码 \(C\) 是完备的，如果  
> \(\forall w\in X^*,\quad X^*wX^*\cap C^*\ne\Phi.\)

The displayed glyph is the **capital Φ-shaped glyph**, copied as `\Phi`. **RESOLVED** as that observed typeform; no alternative symbol or interpretation is substituted.

**Corrected literal English, replacing the provisional qualifier in v1 LF203:**

> A code C over X is called complete if, for all w in X*, X*wX*∩C*≠Φ.

**Corrected inventory entry replacing LF253:**

> | D11 / C64-P6/F5 | “称 X 上一码 C 是完备的，如果”; `∀w∈X*, X*wX*∩C*≠Φ`. |

## 5. U3 — visible reference letterforms and diacritics

**V1 reference [1], LF147–148:**

> [1] Schutzenberger M P. Une theorie algebrique du codage, Seminaire Dubreil-Pisot 1955-  
> 56. expose No. 15 (1955)

**V1 reference [2], LF152–153:** quoted in item 2 above.

**V1 uncertainty, LF271:**

> | U3 | source-math-0081.png, printed65, C65-R1/R2, y740–821 | Fine Latin diacritics in the author/French strings are not reliably resolved at the displayed scale. Visible base letters are copied, without silently supplying/correcting accents from bibliographic knowledge. |

**Observed printed strings:** printed p.65 references [1]–[2], displayed-preview y≈734–832; 300-dpi original pixel views (285,1590)–(1840,1910) and (360,1620)–(1850,1815). No diacritic marks are visible on the named author/French letterforms in these enlarged views. Reference [1] is the base-letter string already quoted above. Reference [2] is the corrected printed string in item 2, including the observed spelling and absence of an apostrophe in `linformation`. **U3 RESOLVED AS OBSERVED AT THE SUPPLIED IMAGE RESOLUTION**; no unprinted accents are added.

**Literal English of reference [1]'s title:** “An algebraic theory of coding.” Reference [2]'s literal English is in item 2. **Inventory:** the quoted printed-definition inventory contains neither bibliography entry, so no inventory entry is affected.

## Item disposition

**Corrected/resolved: 5 distinct items** — M1/U1, M2/U4, m1, U2 and U3. **DISPUTED: 0.** The original v1 remains immutable; these replacements apply only at the stated lines and source positions. This is source-only transcription correction; all existing controls remain.
