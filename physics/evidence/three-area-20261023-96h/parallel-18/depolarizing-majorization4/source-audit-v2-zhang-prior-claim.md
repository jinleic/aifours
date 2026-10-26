# Additive source audit v2 — matched public n=4 uniform-weight claim

Observed audit clock: **2026-10-23T14:42:21-0700**. This qualifies, without editing, `selection-v1.md`, `source-audit-v1.md`, the earlier checkpoint and the new central-index candidate. Current prior-claim status: **STRONG METHOD/SCOPED-RESULT OVERLAP; precise uniform-weight support and full-target settlement not certified**.

## 1. Newly located primary material and exact pin

After freezing `proof-unrestricted-central-indices-v1.md`, a new targeted search for four-qubit spin alignment located:

- Yuxuan Zhang, [Song–Chen Conjecture 2 at n=4 — the uniform case](https://yuxuanzhang1995.github.io/agentic-research/songchen-n4/), author-hosted article;
- its [complete three-page manuscript PDF](https://yuxuanzhang1995.github.io/assets/pdf/agentic/songchen-n4.pdf);
- the author's [research index](https://yuxuanzhang1995.github.io/agentic-research/), which labels this entry **20 June 2026, partially solved**.

All three were actually read, including the complete PDF and the raw article HTML to inspect its proof/artifact links. The PDF title page is dated 20 June 2026. That is an **author-displayed manuscript date**, not an independently authenticated first-publication timestamp or a priority certificate.

The downloaded exact PDF is retained solely in the owned slot as `source-zhang-songchen-n4-v1.pdf`, SHA-256:

`35eb892ead8c957c85bf136365765d8fe24da302e8d82f38dd03cf0226b09ccc`.

The author explicitly says the note is AI-assisted and unrefereed. Those qualifications do not make the claim ignorable; they also do not establish correctness or novelty clearance.

## 2. What it actually claims

The article and PDF claim n=4, Q=I/2 compatible-marginal majorization at every spectral index for **uniform mu**, and leave general weights open. The described load-bearing mechanism is:

- a sixteen-value spectrum `d(x)=1+<epsilon(x),u>`, with `u_i in[0,1/2]`;
- complementary values summing to two;
- clipped pair minima `(1-a_p)_+` and pair maxima `1+a_p`;
- a piecewise-linear sign/clip/box arrangement said to have seventeen vertices;
- six tail inequalities said to be exactly verified, with zero slack at an endpoint.

The paper reports numerical searches and exact reproduction of the vertex enumeration. Those are **the author's reported checks**, not checks exercised or independently accepted here.

## 3. Exact overlap with our central proof

Our candidate `proof-unrestricted-central-indices-v1.md`, SHA-256 `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`, obtains the same useful scalar lower spectrum from `X_2>=X_1-I`:

`d=1+(1/2)sum_i epsilon_i t_i`, where `t_i` is the local Bloch length.

The substitution `u_i=t_i/2` matches the displayed range and spectrum exactly. If `a_p^ours` denotes our nonnegative signed sum, then `a_p^Zhang=a_p^ours/2`, so the clipped minima are also identical:

`(1-a_p^Zhang)_+=(1-a_p^ours/2)_+`.

Our four-sign lemma `sum min(a_p^ours,2)<=10` is equivalently `sum min(a_p^Zhang,1)<=5`, forcing the eight clipped minima to sum to at least three. That controls the five central tails; it also gives the adjacent k=5 tail by adding three pair-maxima. This is strongly consistent with the note's **six** reported tail inequalities. It is not credible to claim that complementary pairing/clipping is a newly discovered mechanism of this round.

Our proof supplies an explicit closed-form pair-variable argument rather than a vertex enumeration. That may have expository/certification value; bypassing an asserted need for enumeration is not by itself proof of original scientific priority.

## 4. Precise ambiguities and missing displayed evidence

Neither the author article nor the three-page PDF explicitly supplies:

1. the operator formula H with the precise **support of uniform mu** and its values;
2. the exact reference spectrum T and six target tail thresholds;
3. the operator-to-d lower-bound derivation;
4. the seventeen rational vertices, their complete coverage argument, their evaluated tail slacks, or an exact verifier/certificate artifact.

The primary page's only full-result link is the three-page PDF; its raw HTML has no linked source archive or vertex data. The research index links the same PDF for this entry, without an associated Zenodo/source-package link. A bounded follow-up search returned the same page; the other indexed GitHub issues inspected concerned graph-LU and stabilizer-code claims, not this proof. No source code was run, external contact attempted, or scientific computation launched.

Thus the public material is a serious **matched claim**, but its advertised exhaustive verification cannot be reconstructed from the material actually exposed there. This is not a finding that the claim is false or that no further artifact exists elsewhere.

## 5. Two possible uniform-weight readings and the assigned target

- If uniform means **all sixteen subsets**, `mu_I=1/16` in the source Conjecture-2 convention, then H is exactly the four-qubit depolarizing output at replacement p=1/2. That would claim the whole p=1/2 instance, including the low-noise spectral indices left open here. It would still not, without an additional argument, settle **every** physical p.
- If uniform means the **six two-element subsets**, then H is X_2/24. That would claim precisely the full U_2 majorization, overlapping the new central proof and the inherited U_2 indices. It still does not by itself prove the missing U_3(2,3,4) or all low-noise channel inequalities.

The displayed scalar tail mechanism points strongly toward the two-body reading, but this remains an **inference**, not a literal definition recovered from the paper. Neither reading is silently substituted for the author's text.

## 6. Operative disposition

- **Mathematics:** the central-index candidate remains eligible for its own separate pinned reconstruction. Its correctness does not depend on importing the unshown vertex enumeration.
- **Priority:** no novelty/first/global-record claim. There is a dated public claim with an essentially matching complementary-tail mechanism; the full priority comparison is **UNCLEAR**, not a clean search miss.
- **Full target:** no checked source currently certifies the entire all-state, all-physical-p target solved. The slot therefore remains the same primary problem; no replacement is justified on this ambiguous claim alone. Parent controls any eventual collision-checked replacement.
- **Preservation:** earlier source screens were bounded and missed this public entry. They remain unchanged historical evidence, with this later additive qualification governing future summaries.
- **Execution:** only source retrieval, PDF preservation and SHA metadata were performed. The public note's claimed scientific checks were not replayed and must not be counted as ours.
