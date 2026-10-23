# Sources (saved 2026-10-16 22:10-22:12 PDT, host clock)

| file | SHA-256 | bytes | origin |
|---|---|---|---|
| `hetman-baicheva-topalova-2026-jacodesmath-389.pdf` | `47c017e42cc14bcf478b388f30788149cad2c4c4470c5074176e0a0a34b4a149` | 669519 | https://jacodesmath.com/index.php/jacodesmath/article/download/389/267 (curl). I. Hetman, T. Baicheva, S. Topalova, "Construction of (v,k,1) cyclic difference families with small parameters", J. Algebra Comb. Discrete Appl. 13(1) (2026) 111-119, DOI 10.13069/jacodesmath.v13i1.389. Open-status quote on p. 4 (PDF page 4, Section 1): "A (20t + 1,5,1) CDF exists for 1 <= t <= 50 except possibly for t = 16,25,31,34,40,45 [2]". Stretch target quote, same paragraph: "(q,7,1) CDF exists for any prime power q = 1 (mod 42) except for q = 43, possibly for q = 127 (nonexistence proved in [5]), 211, 31^6, ...". |
| `abel-costa-finizio-2004-academia-107955257.reader.txt` | `9ec3d7ff73559cf73aafb0ea3fbb6be864a1f7804037d01c8a0e4d52cf5c82f3` | 70861 | Reader-tool text extraction of https://www.academia.edu/107955257/ (R.J.R. Abel, S. Costa, N.J. Finizio, Discrete Appl. Math. 143 (2004) 43-53, DOI 10.1016/j.dam.2003.12.005). A direct curl returned a Cloudflare challenge page, retained as `archive/academia-cloudflare-challenge-not-paper.html`. The extraction renders the exclusion sign of Theorem 14 as "∈"; the sense is "v not in {321,...,901}". |
| `acf2004-section3-excerpt.txt` | `3ff52111bc65a047b38eab2aadf5de7b601a485ac8e58432b92ab218e686f476` | 10459 | Lines 440-610 of the reader text: Section 3 (explicit families transcribed into `code/build_controls.py`) and Theorem 14. One OCR artefact read by hand: "(0:12; 33; 74; 78)" in the v = 161 list is (0,12,33,74,78); the transcribed family passes the verifier. |

Not obtained: Handbook of Combinatorial Designs (2nd ed.) difference-family tables; Baicheva-Topalova data page
(http://www.moi.math.bas.bg/~tsonka/MainCDF.htm). The priority audit is parent-owned (review/cdf-k5-priority-audit.md).
