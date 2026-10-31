# Source-bound original definitions — math-5

Literal book excerpt (Guo–Liu, pp.64-65), /Users/jinleic/repos/aifours/mathematics/shor-code-finite-completion/source/problem.zh.txt SHA256 642b818093ac231cbc44006dc324d73492c6ad9a9b71c469a327cbb4307a75c8, LF1-30:

1| Source: 10000个科学难题·数学卷, 科学出版社, 2009.
2| ISBN: 978-7-03-024267-9.
3| Chapter: 关于有限码具有有限完备化的判定问题.
4| Authors: 郭聿琦、刘云（西南大学）.
5| Book pages: 64–65. PDF pages: 80–81.
6| Source PDF: /Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf
7| The excerpt below was checked against the page images, not only extracted text. Mathematical superscripts are transcribed with ^.
8| 
9| 称 X 上一码 C 是完备的，如果
10| 
11| ∀w ∈ X*，X*wX* ∩ C* ≠ Φ.
12| 
13| 称 X 上一有限码 C 具有有限完备化，如果它能被嵌入一有限完备码.
14| 
15| 事实[1] 正则码（特别地，有限码）是完备的当且仅当它是极大的.
16| 
17| 推翻“码交换等价于前缀码”猜测的那个非极大有限码的反例是 {a,b} 上的有限码[3,5]
18| 
19| C = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2}.
20| 
21| 问题 1[3] 上面的有限码 C 具有有限完备化（据事实 1，即有限极大化）吗？
22| 
23| 这一问题与“有限极大码交换等价于有限极大前缀码”的猜测的联系在于，如果问题 1 的回答是正面的，那么“有限极大码交换等价于有限极大前缀码”的猜测就是错的.
24| 
25| 问题 2[3] 有限码具有有限完备化是可判定的吗？
26| 
27| [3] Bruyere V, Latteux M. Variable-Length Maximal Codes. Automata, Languages and Programming (paderborn, 1996). Berlin: Springer-Verlag, 1996, 24–47.
28| [5] Shor P. A counterexample to the triangle conjecture. J Combin Theor Ser A, 1983, 38: 110–112.
29| 
30| Editorial note (not source text): the book prints 1983 for [5]. The author's publication list and the journal volume identify the publication year as 1985; the source quotation above preserves the book's year.

Original target: does Shor's16-word code C over {a,b} have a finite completion (a finite complete, equivalently finite maximal, code containing C)? Prove one exists (exhibit it with all UD and completeness obligations proved in writing) or prove none exists for ALL finite extensions.

## Provenance and limits

The excerpt is the 2026-10-14 dossier transcription checked against page images (book prints1983 for [5]; editorial note preserved). Main asserts no result.
