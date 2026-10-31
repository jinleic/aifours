# Additive author erratum 1 to author-candidate-v1.md

**Same author, same harness; additive clarification, not a review or acceptance.** `author-candidate-v1.md` remains unchanged. After writing it, I reread its full raw text. I found no false mathematical step. The items below correct presentation and scope wording, make two terse steps explicit, add an equivalent closing route, and qualify the process record. None weakens a quantifier or adds an import.

## 1. Exact hypothesis equals “full no-F” under the surplus hypothesis

The theorem hypothesis assumes that each party has **exactly** two E symbols of surplus two, both of degree three, and two E symbols of surplus zero. Their degree two then follows from `Σd=10`. Under this surplus hypothesis, a physical pair system has a multiplicity-four E value if and only if it is F, meaning two multiplicity-four values and eight multiplicity-two values.

Proof: by candidate (2), a multiplicity-four line `(x,y)` consumes the full surplus two of both endpoints. Thus both endpoints are high, and every other line at y has multiplicity two. The other high symbol `x'` at the first party must put both surplus units on high lines. Low symbols have surplus zero and y is exhausted, so both units go to the other high symbol `y'`, giving multiplicity four there too. All remaining lines have multiplicity two, so the counts are `2·4+8·2=24`. The converse is immediate. The candidate's condition, “no multiplicity-four value in each of the six systems,” is therefore exactly the assigned full no-F premise together with high surplus two and degree three.

## 2. Import wording in §7

Replace “The f860 §§2–4 argument for that premise” with: “The packet S2 (f860) argument for that premise, namely §1's cut interface and lemma (2), §§2–4, and the degree assignment in the first paragraph of §5…”. The import itself is unchanged: this document does not establish no-F, the (2,2,0,0) surplus profile, or the degree-three highs.

## 3. Twin-pair disjointness written in full (§2)

Suppose distinct degree-two rows `r_1,r_2` had high twin pairs `{p,q}` and `{p,q'}` with `q≠q'`. Then q, p and q' would have one common row neighborhood. It contains `r_1`, so `r_1` would meet q, p and q', contradicting degree two. Together with the written exclusion of an identical shared pair, this proves that distinct high twin pairs are disjoint.

## 4. A third closing route in §5

Under the §5 hypotheses, the six-pair table's forced words are 8 Ω, 4 L, 4 M, 4 `Z^{BD}` and 4 `Z^{CD}` words. Their coordinate patterns are pairwise different: all high; high/low/low/high; high/high/high/low; low/high/low/high; low/low/high/high. Hence they are 24 distinct E words, exactly all of E. Every word in this list has D high or D=`δ`. Therefore the other low D symbol `δ'` occurs in no E word, contradicting `s_D(δ')=4`. This uses the same forced lines as the candidate's low-D/BC argument, and its separate shortcut `β_0=β_1, γ_0=γ_1 ⇒ s_0=s_1` gives another route. No route uses a phase or component choice beyond those enumerated there.

## 5. Corrected rendering of the §6 table

Raw Markdown in the first column of the §6 table encloses a pipe in backticks, such as AB, a code-span pipe, then CD. GitHub-flavored renderers may still treat that pipe as a cell separator, misaligning rows and hiding the consequence column. The raw text is unchanged and unambiguous. The intended table is:

| Pair system (cut) | Its actual two low rows | Consequence |
|---|---|---|
| AB (cut AB/CD) | `{α}×H_B` | Chosen without loss of generality. |
| AC (cut AC/BD) | `{α}×H_C` | Forced by (12), same four α words. |
| AD (cut AD/BC) | `{α}×H_D` | Forced by (12), same four α words. |
| BC (cut BC/AD) | `{β}×H_C` or `H_B×{γ}` | First forces AB rows `H_A×{β}`; second forces AC rows `H_A×{γ}`; both conflict. |
| BD (cut BD/AC) | `{β}×H_D` or `H_B×{η}` | First forces AB rows `H_A×{β}`; second forces AD rows `H_A×{η}`; both conflict. |
| CD (cut CD/AB) | `{γ}×H_D` or `H_C×{η}` | First forces AC rows `H_A×{γ}`; second forces AD rows `H_A×{η}`; both conflict. |

## 6. Notation and grammar

In §5, `s_a` names the low BC column of the a-component, while `s_A(a)=8` is the occurrence count from §1. In §§5–6 the letter d also names a high D bit, while `d_i(x)` is a degree. In §2, “Each high row's first two entries is” should read “Each high row's first two entries form.” These overloads and wording changes alter no deduction.

## 7. Process qualifications

* The candidate's statement that every packet window was below 30,000 bytes was **not byte-measured**. Each of the 22 raw windows of at most 20 LF was displayed completely, with no truncation notice. The bound is inferred from that complete visible content and the 74,792-byte packet total. No byte-count command was run, so no subprocess was used.
* Under the prospective GENERAL AUTHOR status recorded in the scope-restoration control, §2 adds one fresh illustrative example, the order-four antisymmetric conference matrix. It also gives a general local parameterization (3). Neither is a premise of the theorem. The example's six row inner products were checked by hand in writing only; no execution occurred. This is disclosed here because §8 did not list it separately.
* This erratum was written after the reread; no packet, source, control, sibling output or held content was reopened for it. No network, execution, subprocess, test, compilation, Git, deletion or verifier preparation occurred. There is still no prepared code hash.
