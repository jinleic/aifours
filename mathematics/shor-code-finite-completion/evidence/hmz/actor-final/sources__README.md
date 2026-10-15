# Source evidence

All files here were generated inside the authorized scratch repository.
The original book and workspace files were read without modification.

- `manifest.json` identifies the five downloaded primary PDFs, their source
  URLs, sizes, and SHA-256 digests. Corresponding `.txt` files are Poppler
  layout extractions.
- `book-pages64-65.txt` and `book-080.png`, `book-081.png` were extracted
  from the local original book path recorded in `../proof.md`. PDF pages
  80–81 correspond to printed pages 64–65. Both renderings were inspected.
- `cordero-2019-page8.png` was rendered from the downloaded 2019 paper and
  inspected to audit its Section 2.2 table and displayed arithmetic.
- `rss-1989-page144.png` renders printed page 144 (PDF page 11), including
  the formula in RSS Conjecture 2 omitted from the text extraction.
- `rss-later-work.txt` retains the primary-source chronology, URLs,
  retrieval time, mathematical scope of Szabó (2006) Theorem 7, and the
  publisher-provided Sands (2007) preview's refutation statement. It records
  that Sands's construction pages were not retrieved.
- `szabo-2006-theorem7-excerpt.txt` retains verbatim parsed hypothesis and
  conclusion fragments from printed page 453 (PDF page 5), with the
  primary PDF URL and retrieval time. An explicitly labelled mathematical
  paraphrase explains the parser's prime and divisibility glyph artifacts.
- `szabo-sands-2009-index.html` is the public reader page served by the
  indexed book URL in `../novelty.md`. Its `.txt` extraction is a reader
  shell, not the full book. The indexed book statement remains unaudited
  as a book citation. The same condition was independently located in the
  primary article Szabó (2006), Theorem 7. Its divisibility condition is
  incomparable with 1320 dividing n; only its stated lower bound is larger.
- The 2008 Zhang–Shum draft was accessible as parsed PDF text through the
  web tool, including its definitions and pages 11–13. Direct download
  returned HTTP 403; no local PDF is claimed. Selected parsed mathematical
  text and scope fragments from pages 4 and 11–13 are retained in
  `zhang-shum-2008-excerpt.txt`, with URL, retrieval time and page labels.
  The hypotheses, the derived infinite code Y, and the asserted formula are
  audited in `../proof.md` Section 6.

No downloaded file is an acceptance certificate. No bounded enumeration of
completion orders or candidates was performed. `../research-checks.json`
records only small exact arithmetic checks supporting the written arguments.
