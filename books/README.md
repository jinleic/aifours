# Source volumes

The three source books are third-party, copyrighted PDFs. They stay local: the repository
`.gitignore` excludes every `*.pdf`. Each copy here was byte-identical to the owner's original in
`/Users/jinleic/Documents/中文pdf/` on 2026-10-14.

| Volume | Science Press edition | PDF pages | PDF page from book page |
|---|---|---|---|
| 信息科学卷 (information science) | 2011, ISBN 978-7-03-031911-1 | 1139 | book + 21 |
| 数学卷 (mathematics) | 2009, ISBN 978-7-03-024267-9 | 568 | book + 16 |
| 物理学卷 (physics) | 2009, ISBN 978-7-03-024269-3 | 876 | book + 33 for pp. 183–579; book + 35 for pp. 580–704 |

SHA-256 identities, as checked by `shasum -a 256 books/*.pdf` from the repository root:

```text
9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db  books/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf
3c69cf2c023a37fdb9e2c7e8ccbe9b163e067884f257003c9df64ac62d092901  books/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf
a4524a2fb26903b13dc76b0fc8edabefe0a3d822b8a400d6149658317631193f  books/10000个科学难题·物理学卷(10000个科学难题物理编委会).pdf
```

To restore a missing copy, copy it from `/Users/jinleic/Documents/中文pdf/` under the same file
name and recheck the hash. The workspace research-institute explorer reads these paths for
table-of-contents extraction.
