# F615 — fresh independent finite author, deficit-six mixed selector

**Status: AUTHOR SOURCE DESIGN; SCIENTIFIC EXECUTION NOT RUN.** The accompanying new standard-library source is `independent-finite-author-checker-v1.py`. This is a prospective finite checker, not a finite PASS, an independent-family review, or an adoption of the original all-prime word theorem. Its source and every claimed planned check are unexecuted by this author.

## Chronology, inputs, and quarantine

I read the complete f615 manifest, freeze receipt, dispatch receipt, all 15 named permission/status controls, and the parent metadata supply. I sent Main a direct PREBODYACK before opening the literal packet. I then read the packet in consecutive raw windows of at most 20 lines, from line 1 through line 680; the two source endings were `S1|631` and `S2|47`. Only after that read did I derive selected cases and independently write the checker. Main reported a launch/request-history interruption; my actual observed packet sequence consisted of the complete windows just described. No inference about an unobserved prior process is made.

The parent supplied the manifest SHA-256 `2631b3b726eb7ca65a001cbcffc70169c5ba8f017f29132b899049b641b801dc`, freeze-receipt SHA-256 `faf17f9d0218967abce095ad29c930726ebef07ff4e002239af5a68e92b7b89a`, and packet SHA-256 `36446ee7c1b43780d5f7dec616fd9d85075ba88b665eb77050b547fcaf6a2949`. These and its recorded clock are **parent observations**, not my own hash or clock observations. I did not obtain a SHA-256 for the newly authored source; the parent must do so before its own run.

The entire held f602 and f586 scientific episodes and their method, confidence, proof, selection, and other consumers were NONINPUT. Their status controls alone were read. I did not open another checker, author code, sibling scientific return, external source, or held mathematical payload. This access chronology is not a cognitive-isolation certificate.

## Original target and finite scope

For an actual linear word in \(D_{2p}\), the original author candidate concerns \(p\ge7\), \(3p-2\) reflections, at least \(p+1\) rotations, at most one rotation in each cyclic reflection gap, and cyclic reflection projection odd-run count \(3p-8\). The candidate seeks an original-order identity subsequence of exactly \(2p\) letters. Its selector uses two rotations, except for the single-six-run arithmetic-progression branch, for which a zero-rotation selector is supplied. The universal candidate remains **UNADOPTED**.

The proposed checker designs 79 actual words: 27 for p=7 and 26 each for p=11 and p=13. For every one of the ten listed deficit-six run types and every p, it constructs two generic variants with different labels/gap placements, one of which cuts through a long run. Additional cases include both endpoint choices r=0 and s=0 for the seven-run single-rich/AP mechanism and for the 5+3 exceptional two-direction mechanism; and 5+3 exceptional words with a=b at both endpoint choices. Rotation placements have exactly p+1 distinct physical occurrences and at most one per original cyclic gap. These counts are source-design counts, **not observed execution results**.

The optional exhaustive binary p=7 \(2^{19}\) projection scan is deliberately omitted: no claim of exhausting that scan, all p-ary labels, all placements, all rotation labels, or all primes is made.

## Exact finite construction and checking design

* The script constructs the group internally as \((x,e)(y,b)=(x+(-1)^e y,e+b)\), stores each actual linear occurrence separately, and independently parses every original cyclic gap. It partitions by omitting each physical reflection occurrence in turn. The union of actual consecutive reflection triples seen over all omissions must equal the set of all actual cyclic triple starts, for each word and hence for all ten types.
* The general subsequence DP keeps every dihedral product and every rotation count for exact length \(2p\); it does not assume an abelian reflection product. The separate selector code explicitly computes chronological pair products, the first/second interior rotation signs, safe/unsafe physical gaps, boundary rotations on both sides of the omission, and the bound \(B+2h\). It searches actual omissions and protected rich/AP blocks, with at most one selected interior rotation per block.
* For a selector certificate it computes each actual local product set, checks protected sets are unchanged and all constant blocks remain nonempty, performs sumset extraction, reconstructs one physical \(2p\)-position selector for **every** field exponent, and compares each actual product against the independent DP. The two-rotation DP must contain all field exponents for such a certificate. The zero-rotation AP selector is separately reconstructed and checked against the zero-rotation DP.
* Each reconstructed selected word is checked at every physical cut using the actual prefix conjugation identity. It does **not** assume a nonidentity product is unchanged under cyclic rotation. Identity must remain identity at each cut.
* For the selected fields the code plans exhaustive \((d,e)\) field checks of \(|D_d+D_e|=4\) for \(d\ne\pm e\), and both orientations of the rich-plus-AP exception criterion. It separately plans every \((a,u)\) constant-block/interior-gap combination. It explicitly checks the source's six-/seven-run and exceptional 5+3 phase shapes using physical occurrence indices.
* A small 16-letter auxiliary word, not a theorem input, is designed for an independently enumerated all-\(\binom{16}{14}\)-subword comparison to the general p=7 group DP. This checks the DP recurrence at that finite auxiliary input; it is not claimed as a proof of the recurrence or of the all-prime theorem.

For the special AP constructions, the exact source input uses \(r+s=p-4\), \(L=3r+2\), \(M=3s+2\), \(d=1\), \(e=-L/M\pmod p\), at r=0 and s=0. A seven-run word uses the actual chain of L increments d followed by M increments e, bracketed by the seven equal-label occurrences. The 5+3 construction uses those two physical AP chains between the five- and three-runs. The a=b exceptional tests are separate generated words; the report does not conflate them with the no-rich AP cases.

## Explicit p=7 zero-rotation case — written construction, not a machine result

Using \(\sigma_a=(a,1)\) and \(\rho_u=(u,0)\), the actual original-order word, with one-based positions, is:

```text
 1 σ0   2 σ0   3 σ0   4 ρ2   5 σ0   6 σ0   7 ρ1
 8 σ1   9 σ2  10 ρ0  11 σ3  12 σ4  13 ρ6  14 σ5
15 σ6  16 ρ5  17 σ0  18 σ1  19 ρ4  20 σ2  21 σ3
22 ρ3  23 σ4  24 σ5  25 ρ2  26 σ6  27 σ0
```

Its cyclic projection is a six-run of label 0 followed by the singleton chain \(1,2,3,4,5,6,0,1,2,3,4,5,6\), with the physical cut through the six-run. The planned zero-rotation positions are

```text
6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26
```

Their ordered reflection labels are \(0,1,2,3,4,5,6,0,1,2,3,4,5,6\). Their alternating exponent is \(-7\equiv0\pmod7\), so this is a written, literal 14-reflection identity construction. The code is designed to reconstruct these physical positions and check all cuts. Its DP will report whether a two-rotation identity also exists for this selected word; **no assertion that two rotations are impossible is made**. No machine check has been performed.

## Intended controls and actual result

The source plans intended-reason negative controls for a mutated group-DP state; each wrong interior sign; both reversed safety predicates; a double-rotation gap; dropping an omitted-reflection boundary rotation; two interior rotations in one block; a protected interior; an unsafe interior; a duplicated position; wrong selector length; wrong rotation count; incompatible block-pair choices; an incomplete sumset; a nonidentity product; false nonidentity cut equality; and missing type coverage. The controls mutate concrete data or an actual state checked by the same production validator; an arbitrary exception is not counted as the intended rejection. The tiny exhaustive DP comparison and each correctly formed construction are intended positive controls.

**Observed results:** no scientific source execution, no program stdout/stderr, no exit status, no elapsed runtime, no finite PASS/FAIL, and no control outcome. The program uses a 52-second cooperative deadline and aborts with a nonzero status and `TIME_BOUND` if it reaches that deadline before completion; an actual \(<55\) second runtime is not established without the parent's run. The checker performs no file, network, or child-process I/O; its only intended output is JSON on standard output.

## Parent one-shot and remaining gates

After independently pinning and inspecting the source bytes and arranging a fresh captured receipt, the parent may execute once under its own frozen authority:

```text
python3 -B /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f615-fresh-original-input-deficit-six-independent-finite-replacement/independent-finite-author-checker-v1.py
```

Record the parent-observed source SHA-256, exact argv, start/end times, exit status, complete stdout/stderr, and whether all planned cases and intended-reason controls actually completed. A timeout, exception, failed control, source change, or incomplete receipt is **not** a PASS. Parent review and disposition remain necessary. The source is not an independent-family, human, kernel, novelty, global-Olson, or all-prime proof; the original written theorem and all broader targets remain unadopted here.
