# B4r literal packet — additive erratum 1

- Immutable v1 `book-literal-math-4-v1.md`: SHA256 `8627f8902cc9b89254997ede7f161225568ff77d25e6f33abe787e4520aeee2f`, **272 LF / 18211 bytes**.
- Complete comparison `book-literal-math-4-comparison-v1.md`: SHA256 `1152dc0a7e35048616aa116d62e171ffef98a7b6fac291911af077bc3b15b383`, **52 LF / 7016 bytes**.
- Mandatory comparer addenda: `book-literal-math-4-comparison-erratum-1-v1.md`, SHA256 `c09ce484ffd25211d22ebf73ce2d22f201d9c0e1274e840cdef1499035bb914f`, **33 LF / 4612 bytes**; `book-literal-math-4-comparison-erratum-2-v1.md`, SHA256 `85484c4c6a621e2b2b22693286466e2fc667859b7ddc3b2f8f5135b775b93d2d`, **23 LF / 2522 bytes**.
- Pre-body ACK `book-literal-math-4-erratum-1-prebody-ack-v1.json`: SHA256 `21c3cbbbcb7b164a7ad3d844b735ee5419aca5bdb013268632549b63789a1788`, **12 LF / 2177 bytes**, native prewrite clock **Wed Oct 28 09:47:13 PDT 2026**.
- Erratum release SHA256 `8318bb69872393654711cb5f82341cd95742763278c0c09c3bd1710cd51c14e9` initially had an empty image list. The separately frozen additive image list SHA256 `b835a547f53e9687ba7eba0a0d52f1e1fe0aec11972a7985bef9e9b97fac1ef7` supplied the two original images; Main gave explicit PROCEED. I did not open either image between the ACK and that permission.
- The further frozen high-resolution addendum SHA256 `d7d8b1b100d961750292a5d4bb9cd2299062f7aaa6cc2b0264d3a99450b485ef` expressly permits visual crops of listed images; no OCR.
- PDF p82 / printed p66: 150-dpi image SHA256 `d70fd92ab92e65b252e7088cdb2e4f76b940c96d76a98dc79832bab073e5c127`; 300-dpi image SHA256 `fab15892312320695cf11e9a5fc6b541352bfa35977ce05624874fa3a20591f4`.
- PDF p83 / printed p67: 150-dpi image SHA256 `7b6ddcf090999f397e504181378d16759921438fc3f25028d9cffbec73abf70a`; 300-dpi image SHA256 `a80aaeb9f8c098fa65d9732d81feac27c00b3e221de668c83ee3842e354c32e9`.
- Native clock immediately before writing this erratum: **Wed Oct 28 09:49:48 PDT 2026**.

**Result: 0 corrected occurrences; 5 DISPUTED occurrences.** The comparer grouped these five occurrences as one repeated-word observation. On the permitted 300-dpi crops I observe **关于**, as already written in v1, at all five locations; the comparer instead reported **对于**. The differing printed glyphs are given for each occurrence below. No mathematical meaning or severity disposition is inferred. V1 stays immutable.

The five documentary crops below are generated directly from `source-math-0082-r300.png` with native `sips --cropToHeightWidth 180 1100 --cropOffset Y X`; pixel origin is the upper-left of that 300-dpi input. Crop image paths are in the same transcriber root, not additional source pages. Each visual crop displays approximately 1222×200; the source pixels used are the 1100×180 rectangle stated.

| Location | Crop file | SHA256 | Source crop offset (Y, X) |
|---|---|---|---|
| 1 | `book-literal-math-4-erratum-glyph-1-v1.png` | `36f573112c0ae53d50da678449400115f72df436b7510e5c1297a056634174ea` | (1150, 650) |
| 2 | `book-literal-math-4-erratum-glyph-2-v1.png` | `a85a34583ca17a25af5d9d23df3974687d2a08f6b5656715c2a69825d85e6f13` | (1825, 300) |
| 3 | `book-literal-math-4-erratum-glyph-3-v1.png` | `66b72acd36ca06c8985c0da026c076bfa85d1f20874e97f01a03558934555c2b` | (1960, 300) |
| 4 | `book-literal-math-4-erratum-glyph-4-v1.png` | `a799cd6a8a2d6af81ed319545739fc8ac25adea1f6fe7fa42f7347ac42e0c483` | (2185, 750) |
| 5 | `book-literal-math-4-erratum-glyph-5-v1.png` | `0ace8e60503941941b5e3caba44a4c4dfe31916d7def55c6211fb76375fa8a1e` | (2410, 450) |

## 1. Regular/inverse condition — DISPUTED

**Printed p66, body B06**, crop 1: I observe **“如果关于任意”**; the comparer reported **“如果对于任意”**. The v1 wording below is retained, not replaced.

**V1 LF41, as written:**

> 令 $S$ 是一半群, $a\in S$. 称 $S$ 是一幺半群, 如果 $S$ 含恒等元; 称 $a$ 是 $S$ 的一个正则元, 如果 $S$ 的子集 $V(a)$ 非空, 其中, $V(a)=\{x\in S\mid axa=a,xax=x\}$, $V(a)$ 中的元素称为 $a$ 的逆元; 称 $S$ 是一正则 (逆) 半群, 如果关于任意 $a\in S$, $V(a)$ 非空 ($V(a)$ 是一单元集). $S$ 的所有幂等元形成的子集用 $E(S)$ 表示. 称 $E(S)$ 是一带, 如果 $E(S)$ 是 $S$ 的一个子半群; 称 $S$ 是一纯正半群, 如果 $E(S)$ 是一带; 称带 $E(S)$ 是一半格 (交换带)、正则带、正规带、半正规带, 如果它们分别满足

**Relevant literal English, v1 LF161, unchanged:**

> **[Z03b]** S is called a monoid if S contains an identity element; a is called a regular element of S if the subset $V(a)$ of S is nonempty, where $V(a)=\{x\in S\mid axa=a,xax=x\}$, and the elements of $V(a)$ are called inverses of a; S is called a regular (inverse) semigroup if, for every $a\in S$, $V(a)$ is nonempty ($V(a)$ is a singleton set).

**V1 inventory LF234, unchanged:**

> | Regular/inverse semigroup and quantifier | “称 $S$ 是一正则 (逆) 半群, 如果关于任意 $a\in S$, $V(a)$ 非空 ($V(a)$ 是一单元集)” | Z03; p66 B06–B07 |

## 2. Primitive idempotent — DISPUTED

**Printed p66, body B11**, crop 2: I observe **“如果关于任意非零幂等元”**; the comparer reported **“如果对于任意非零幂等元”**.

**V1 LF56, as written:**

> 众所周知, 逆半群恰是 $E(S)$ 为半格的半群, 因此逆半群是纯正的; 称 $S$ 的非零幂等元 $f$ 是本原的, 如果关于任意非零幂等元 $e$, $ef=fe=e\to e=f$.

**Relevant literal English, v1 LF178, unchanged:**

> **[Z05b]** a nonzero idempotent f of S is called primitive if, for every nonzero idempotent e, $ef=fe=e\to e=f$.

**V1 inventory LF244, unchanged:**

> | Nonzero primitive idempotent and quantifier | “称 $S$ 的非零幂等元 $f$ 是本原的, 如果关于任意非零幂等元 $e$, $ef=fe=e\to e=f$” | Z05; p66 B10–B11 |

## 3. Locally inverse condition — DISPUTED

**Printed p66, body B13**, crop 3: I observe **“如果关于任意幂等元”**; the comparer reported **“如果对于任意幂等元”**.

**V1 LF60, as written:**

> 一正则半群称为完全单的, 如果它不含真理想, 而且含一本原幂等元; 称半群 $S$ 是局部逆的, 如果关于任意幂等元 $e$, $eSe$ 是逆子半群; 称正则半群 $S$ 是弱 $E$-酉的, 如果

**Relevant literal English, v1 LF180, unchanged:**

> **[Z06a]** A regular semigroup is called completely simple if it has no proper ideal and contains a primitive idempotent; a semigroup S is called locally inverse if, for every idempotent e, $eSe$ is an inverse subsemigroup; a regular semigroup S is called weakly $E$-unitary if

**V1 inventory LF246, unchanged:**

> | Locally inverse | “称半群 $S$ 是局部逆的, 如果关于任意幂等元 $e$, $eSe$ 是逆子半群” | Z06; p66 B12–B13 |

## 4. Natural-order sentence — DISPUTED

**Printed p66, body B15**, crop 4: I observe **“定义如下: 关于任意”**; the comparer reported **“定义如下: 对于任意”**.

**V1 LF70, as written:**

> 其中, “$\le$” 是正则半群 $S$ 上的自然偏序, 定义如下: 关于任意 $a,b\in S$,

**Relevant literal English, v1 LF188, unchanged:**

> **[Z08 + Z09]** Here “$\le$” is the natural partial order on the regular semigroup S, defined as follows: for every $a,b\in S$,

**V1 inventory LF248, unchanged:**

> | Natural partial order and both quantifiers | “其中, ‘$\le$’ 是正则半群 $S$ 上的自然偏序, 定义如下: 关于任意 $a,b\in S$” | Z08; p66 B15 |

## 5. Locally r-orthodox condition — DISPUTED

**Printed p66, body B16**, crop 5: I observe **“如果关于任意”**; the comparer reported **“如果对于任意”**.

**V1 LF80, as written:**

> 称一正则半群 $S$ 是局部 $r$-纯正的, 如果关于任意 $e\in E(S)$, $eSe$ 是以 $E(eSe)$ 为正则带的纯正 (幺) 半群. 称半群 $S$ 到半群 $T$ 的同态 $\phi$ 是幂等元分离的, 如果

**Relevant literal English, v1 LF194, unchanged:**

> **[Z10a]** A regular semigroup S is called locally $r$-orthodox if, for every $e\in E(S)$, $eSe$ is an orthodox (monoid) semigroup whose $E(eSe)$ is a regular band.

**V1 inventory LF250, unchanged:**

> | Locally $r$-orthodox | “称一正则半群 $S$ 是局部 $r$-纯正的, 如果关于任意 $e\in E(S)$, $eSe$ 是以 $E(eSe)$ 为正则带的纯正 (幺) 半群” | Z10; p66 B16–B17 |

## Withdrawn apparent findings

The mandatory comparer addenda withdraw the apparent fourth-condition punctuation and grouped-locator findings; the original comparison's band-list and Question 2 sections themselves assign no discrepancy. No correction is made for those sections. The comparer also withdrew its previous definite severity label for the repeated-word observation pending parent classification. No additional source claim follows from these withdrawals.

**END OF ADDITIVE B4r ERRATUM 1.**
