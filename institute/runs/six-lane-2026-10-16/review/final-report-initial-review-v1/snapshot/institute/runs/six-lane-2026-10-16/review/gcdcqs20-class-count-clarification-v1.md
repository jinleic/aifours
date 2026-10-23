# gcDCQS(20^4:0)/mcDSQS(80): class-count wording clarification

Recorded at 2026-10-18T14:10:30-07:00.

The [parent verdict](gcdcqs20-parent-verdict.md), line41, says “This gives40classes of1027triples.” Read this as **1,027 triples in total, partitioned into40 colour classes**, not1,027 triples in each class.

The same verdict's actual checker receipt/profile already establishes the intended counts: profile26^37,25,24,16 has37+1+1+1=40classes and37·26+25+24+16=1,027triples. An STS(79) has79·78/6=1,027triples, and each colour class has at mostfloor(79/3)=26triples, so at leastceil(1,027/26)=40classes are necessary. The verified40-colouring therefore attains the minimum. No source, certificate, checker, acceptance decision or theorem is changed; this corrects only that sentence.

Historical statuses in the old verdict (“no Lean yet”, v=32open) are also superseded at their exact scopes by the [Lean verdict](gcdcqs20-lean-parent-verdict.md) and [gcDCQS32 verdict](gcdcqs32-parent-verdict.md). The imported recursion and its parameter range remain as stated in those verdicts. This is not a new construction or gate.
