# f477 — Written review of local multiplicities and the S/five-party refinement

**Overall correctness: correct at the scoped necessary-condition level.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence: 0.99.**

The local integer parameterization in S2 §5 is complete for its stated count equations. The new exclusion is supported at **each** four-symbol party: in S with the singleton internal at a five-symbol party, neither four-symbol party can have residual-degree profile \((4,4,2,2)\). This is not a whole-4455 exclusion, a common-\(P,E\) construction, or a physical-tensor existence result.

## 1. Frozen bindings and actual access

The following are **parent-supplied metadata observations**, not reviewer-executed hashes or native clock measurements:

| Artifact | SHA-256 |
|---|---|
| f477 manifest | `bfa82af4e48a478293b0c5dda3eeec0e232a6708d3d9ca3afd16af50da4ca5b6` |
| f477 freeze receipt | `145f17654e89026c937d272976f60a6cc7467ee7af4a51858eba42af23016094` |
| f477 literal packet | `4f6ccd6696ed75b9fb8f0e670291e787fc6fccf321a7403d9feca1658510f5a6` |
| S1 adopted disposition | `60448959ee1043506210ebec876ede3fc2b91d233781a06d6513942129837632` |
| S2 f460 report | `4de63ccedc86491423bdc1a9feae114850d1571eb260b088e7ecc32cf9d30879` |

The parent metadata supply records its observation at **2026-10-30T12:13:16-0700 PDT**. I do not attribute that clock to my own start, completion, or hash execution.

Actual access sequence:

1. Read the required memory summary and relevant review skills.
2. Read the complete f477 manifest, freeze receipt, all ten declared status-only controls through their endings, and the parent dispatch/metadata records.
3. Delivered the required administrative **PREBODY_ACK** to Main before reading the mathematical packet.
4. Read the complete literal packet in consecutive, ordered raw windows of at most 20 LF, covering packet LF **1–266**, including the ending `S2|226|`.
5. Only afterward performed the written reconstruction below.

Source coverage is **S1 LF1–38, complete**, and **S2 LF1–226, selected range only**. I did not open S2 beyond LF226, author/checker source, sibling reviews, excluded links, held mathematical payloads, or external sources. No scientific program, CAS, interpreter, solver, enumeration, replay, or newly selected mathematical instance was used. No repository file was edited; this is the complete review body for parent materialization.

The quarantine controls were used only for status and permissions. This access account is not a cognitive-isolation certificate.

## 2. Exact hypotheses and imports

The mathematical interface is S1 LF7–9 and S2 LF57–82:

- One and the same tensor \(U\), with three unitary balanced flattenings, has 48 nonzero entries and 24 modulus-one entries.
- \(P\) and \(E\) are its respective 24-word maximal and residual supports.
- For every pair \(ij\), \(R_{ij}=\pi_{ij}(E)\) has 12 pairs, each with two residual extensions.
- Projection on \(P\) is injective, and
  \[
  \pi_{ij}(P)=[6]^2\setminus R_{ij}.
  \]
- The residual alphabet sizes are \(q=(4,4,5,5)\), with outside counts \(b=(2,2,1,1)\).
- For a residual symbol,
  \[
  p_i(a)=6-r_i(a),\qquad r_i(a)\ge2,\qquad
  \sum_{a\in A_i}r_i(a)=12.
  \]

These remain hypotheses/consequences of a **common actual support**, not independent pairwise fixtures. No no-OLS or no-distance-one assumption enters the reconstruction.

The previously adopted low-slice, defect, and regular-matching conclusions in S1 LF24–32 are not needed to prove the new local classification or the S/five-party exclusion. They receive no new whole-scope review from this gate.

## 3. Global word counts — SUPPORTED

**References:** S1 LF13–16; S2 LF84–113.

Pair injectivity and the residual-pair complements give
\[
\sum_s n_s=24,\qquad
\sum_s s\,n_s=60,\qquad
\sum_s \binom{s}{2}n_s=49.
\]
Consequently,
\[
\sum_s\left[\binom{s}{2}-2s+3\right]n_s
=3n_0+n_1+n_4=1.
\]
Nonnegativity therefore gives precisely the displayed alternatives:
\[
F:(0,0,13,10,1),\qquad
S:(0,1,10,13,0).
\]

The type-specific counts also follow from the same \(P\). Every outside-coordinate value occurs in six maximal words, and each outside pair occurs once. In F, these give
\[
t_i=b_i^2,\qquad d_{ij}=b_kb_l.
\]
In S, the unique singleton is internal at \(h\). It contributes to an outside pair exactly when neither member of that pair is \(h\), yielding
\[
d_{ij}=b_kb_l-\mathbf1_{h\in\{i,j\}},
\qquad
t_i=b_i^2+\mathbf1_{i\ne h}.
\]

These are global counts of actual words in the same \(P\), not totals assembled from unrelated projections.

## 4. Local equations — SUPPORTED

**References:** S2 LF115–144.

Fix a residual symbol \(a\) at party \(i\), and use the author’s variables \(\sigma,f,\tau,\delta,x_j,y_j\). The special-word indicators satisfy
\[
\sigma,f\in\{0,1\},\qquad \sigma f=0,
\]
because F and S are mutually exclusive.

The multiplicity equation is
\[
6-r=\sigma+\tau+\delta+f.
\]

For every other party \(j\), exactly \(b_j\) maximal words pair \(a\) with an outside \(j\)-symbol. Counting those words by type gives
\[
b_j=\sigma+x_j+\delta-y_j.
\]

There are \(q_j-r\) maximal words pairing \(a\) with an internal \(j\)-symbol. Summing this over the other three parties gives
\[
2\tau+\delta+3f=\sum_{j\ne i}(q_j-r)
=18-q_i-3r.
\]
Subtracting the multiplicity equation yields
\[
\tau+2f-\sigma=12-q_i-2r.
\]

Equivalently,
\[
\tau=12-q_i-2r+\sigma-2f,\qquad
\delta=q_i-6+r-2\sigma+f,
\]
and
\[
x_j=b_j-\sigma-\delta+y_j.
\]

Nonnegativity and \(\sum_jy_j=\delta\) then determine the displayed local rows. The remaining sum condition is consistent automatically: since \(\sum_{j\ne i}b_j=q_i\),
\[
\sum_jx_j=q_i-3\sigma-2\delta=\tau.
\]

Thus no additional independent \(\sum x_j=\tau\) constraint has been lost in the parameterization.

## 5. Complete local integer rows — SUPPORTED

**References:** S2 LF146–178.

### Four-symbol party

Here the outside-count vector of the other parties is \((2,1,1)\), and
\[
\tau=8-2r+\sigma-2f,\qquad
\delta=r-2-2\sigma+f.
\]

- **Ordinary symbol:** nonnegativity permits exactly \(r=2,3,4\).
  - \(r=2\): \(\delta=0\), hence \(y=0\) and \(x=(2,1,1)\).
  - \(r=3\): \(\delta=1\), hence \(y=e_a\) and \(x=(1,0,0)+e_a\).
  - \(r=4\): \(\delta=2\). Nonnegative \(x\) requires \(y\ge(0,1,1)\); its prescribed sum forces \(y=(0,1,1)\), with \(x=0\).

- **Four-internal-word symbol:** nonnegativity permits exactly \(r=2,3\). The respective \((\tau,\delta)\) values are \((2,1)\) and \((0,2)\), giving the two displayed rows.

- **Singleton symbol:** \(\delta=r-4\ge0\) and \(\tau=9-2r\ge0\) force \(r=4\). Then \(\delta=0\), \(\tau=1\), and \(x=(1,0,0)\).

This verifies all six rows, including the conclusion that a singleton internal at a four-symbol party uses a degree-four symbol whose unique other maximal word is a triple containing both five-symbol parties.

### Five-symbol party

Here the outside-count vector is \((2,2,1)\), with last position \(l\), and
\[
\tau=7-2r+\sigma-2f,\qquad
\delta=r-1-2\sigma+f.
\]

- **Ordinary symbol:** exactly \(r=2,3\).
  - \(r=2\): \(y=e_a\), \(x=(1,1,0)+e_a\).
  - \(r=3\): nonnegative \(x\) requires \(y_l\ge1\). Since \(\sum y=2\), this is exactly \(y=e_l+e_a\), with \(x=e_a\).

- **Four-internal-word symbol:** exactly \(r=2\), with \(\tau=1,\delta=2\) and the same \(y=e_l+e_a,\ x=e_a\) parameterization.

- **Singleton symbol:** exactly \(r=3,4\).
  - \(r=3\): \(\tau=2,\delta=0,\ x=(1,1,0)\).
  - \(r=4\): \(\tau=0,\delta=1\), forcing \(y=e_l,\ x=0\).

In the unit-vector rows, the index ranges over all three displayed positions, including \(a=l\) where applicable.

These are complete solutions of the stated **local integer count constraints**. They are not a sufficiency theorem for assigning actual symbols, constructing common \(P,E\), or obtaining simultaneous unitary phases.

### Degree-profile consequences

Combining the rows with the residual-degree sum gives:

- Four-symbol parties:
  \[
  (3,3,3,3),\quad(4,3,3,2),\quad(4,4,2,2).
  \]
- A five-symbol party without the singleton:
  \[
  (3,3,2,2,2).
  \]
- The singleton’s five-symbol party can instead have
  \[
  (4,2,2,2,2).
  \]

Only the singleton’s party can have the exceptional five-symbol profile. A five-symbol coordinate of the four-internal word has degree two, and a degree-two five-symbol symbol cannot be the singleton symbol.

## 6. New S/five-party exclusion — SUPPORTED at both four-symbol parties

**References:** S2 LF180–190; S1 LF22 and LF38.

### Missing-graph proof

In S with \(h\in\{3,4\}\), the unique maximal word containing both outside five-party symbols must be double-internal at parties 1 and 2. Its internal pair gives an edge \(v\) of \(M_{12}\).

There is exactly one such double-internal word. The other three \(M_{12}\) edges come from triples missing one of the two five-symbol parties. A triple missing a five-symbol party uses that party’s unique outside symbol, also used by \(v\). If its edge shared either endpoint with \(v\), two maximal words would repeat the corresponding four-party/five-party pair, contradicting pair injectivity on \(P\). Thus \(v\) is isolated.

At **each endpoint** of this isolated edge, missing degree is one. Since
\[
\deg_{M_{12}}(a)=4-r_i(a),
\]
each of the two four-symbol parties has a residual-degree-three symbol. The profile \((4,4,2,2)\) has no such symbol. It is therefore excluded separately at each four-symbol party, leaving
\[
(3,3,3,3)\quad\text{or}\quad(4,3,3,2).
\]

### Independent local-to-global count proof

Fix either four-symbol party \(i\), and retain \(h\) as the singleton’s five-symbol party. All symbols at \(i\) are ordinary. The ordinary degree-four row requires one double-internal word at the pair \((i,h)\) for every degree-four symbol at \(i\).

The profile \((4,4,2,2)\) would therefore require at least two such words. But the global S count is
\[
d_{ih}=b_jb_l-1=2\cdot1-1=1,
\]
where \(j\) is the other four-symbol party and \(l\) the other five-symbol party. This is a contradiction.

The local-row output is thus compatible with—and genuinely constrained by—the consuming global \(d_{ih}\) count. Neither proof uses a no-OLS or no-distance-one premise.

The exclusion is restricted to **S with the singleton internal at a five-symbol party**. It is not extended to F or to S with the singleton internal at a four-symbol party.

## 7. Selected missing-graph classification and counts — SUPPORTED as weak graph statements

**References:** S2 LF194–223.

Four edges and maximum degree two leave precisely
\[
4P_2,\quad P_3\sqcup2P_2,\quad 2P_3,\quad
P_4\sqcup P_2,\quad P_5,\quad C_4,
\]
after removing isolated vertices.

The labeled counts admit direct written counting:

| Class | Written count | Total |
|---|---|---:|
| \(4P_2\) | \(4!\) | 24 |
| \(P_3\sqcup2P_2\) | \(2\cdot4\binom42\binom32\,2!\) | 288 |
| \(2P_3\) | \(36+36+144\), by center-side orientations | 216 |
| \(P_4\sqcup P_2\) | \(\binom42^2\cdot4\cdot4\) | 576 |
| \(P_5\) | \(2\binom43\binom42\cdot6\) | 288 |
| \(C_4\) | \(\binom42^2\) | 36 |

They total 1428. The complementary inadmissible graphs consist of eight four-edge stars and
\[
8\binom43\cdot12=384
\]
graphs with a degree-three vertex. Such a degree-three vertex is unique in a four-edge graph, so this count does not double-count. Together these account for the stated 1820 graphs.

The maximum matching numbers in the table are also correct.

For the marking columns:

- **F:** \(v\) must be disjoint from two distinct triple edges. Every listed forest permits this; \(C_4\) does not. The total is \(1392\).
- **S, singleton at a five-symbol party:** an isolated edge is required. Exactly \(4P_2\), \(P_3\sqcup2P_2\), and \(P_4\sqcup P_2\) qualify, totaling \(888\).
- **S, singleton at party 1:** all six classes permit the bare two-matching coloring. Requiring an isolated party-1 vertex gives the displayed counts \(0,144,180,576,288,36\), totaling \(1224\). In particular, the \(2P_3\) contribution consists of the party-1-center orientation and the opposite-center orientation, not the orientation using all four party-1 vertices.

These are graph-relaxation statements. The counts do not establish that any counted graph extends to complete common \(P,E\), residual block closure, or physical phases.

## 8. Unassessed claims and explicit exclusions

**INCONCLUSIVE / not assessed by this review:**

- Claims about checker implementation, aggregation, canonical-form computation, or runtime behavior in S2 LF113, LF192, and LF225.
- Scientific source and report content beyond S2 LF226.
- The historical computational execution and mutation-control claims summarized in S1 LF36.
- Independent reconstruction of the low-slice, defect, and regular-matching results outside this refinement.
- Literature priority, novelty, independent-family agreement, human review, or kernel verification.

The graph counts above have written support independent of any claimed program run. No implementation correctness or computational PASS is inferred from that written support.

## 9. Disposition

**SUPPORTED:** the complete local count parameterization; its displayed degree consequences; the exclusion of \((4,4,2,2)\) at **either** four-symbol party in S with a five-party singleton; and the selected four-edge graph classification/counts at their necessary, weak-relaxation scope.

**REFUTED:** none.

**FATAL / MAJOR / MINOR:** **0 / 0 / 0** within the reviewed scope.

The new refinement is mathematically supported for parent disposition, with no automatic adoption. It does not resolve whole-4455 compatibility, construct a physical tensor, or change the open global AME minimum.