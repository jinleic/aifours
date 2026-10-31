# author-candidate-v1.md

**Wave:** f403-ame-t24-4445-simultaneous-profile-frontier  
**Role:** GENERAL AUTHOR  
**Status:** **AUTHOR CANDIDATE — UNREVIEWED; NOT ADOPTED.**  
**Result:** A complete written exclusion of the **entire actual residual-alphabet profile \(4445\)** at support \(48\), \(t=24\), for arbitrary complex amplitudes.  
**Dependency:** The proof does **not** require no-distance-one, no-OLS(6), or the earlier \(4444\) normal form.  
**Execution:** No scientific executable or finite checker was run. No working-tree file was written. This is the complete manuscript for parent materialization.

**Additive metadata:** The subsequently received parent clock is recorded in §12. It does not change the scientific body, proof, scope or acceptance status.

## 1. Exact theorem

Work in a fixed product basis.

**Theorem — whole-profile \(4445\) exclusion.**  
Let \(\psi\in(\mathbb C^6)^{\otimes4}\) be normalized, and set \(U=6\psi\). Suppose all three balanced flattenings
\[
U^{12\mid34},\qquad U^{13\mid24},\qquad U^{14\mid23}
\]
are unitary. Suppose \(U\) has exactly \(48\) nonzero entries, exactly \(24\) of modulus one. Define the same sets of tensor words
\[
P=\{w:|U_w|=1\},\qquad
E=\{w:0<|U_w|<1\}.
\]
If the four residual alphabets of \(E\) have sizes \(4,4,4,5\), these hypotheses are contradictory.

The theorem covers every support and every nonzero complex amplitude satisfying these hypotheses. There is no real-phase, equal-modulus, independent-pair-gauge, or support-normal-form restriction.

The proof establishes a stronger combinatorial obstruction: the necessary shared-\(P\), exact-two-extension support interface itself is impossible for \(4445\). Thus no phase or modulus construction is needed to close this class.

This is **not** a universal \(t=24\) exclusion, a support-\(48\) exclusion, an \(N\ge49\) theorem, a physical witness, a novelty claim, or an adoption.

## 2. Access, bindings and chronology

Before reading the mathematical packet, I read the complete manifest, freeze receipt, dispatch receipt, parent live metadata, and all eight named permission/status controls. I then read the complete ordered literal packet through its ending:

- S1: assigned logical lines 1–345;
- S2: complete assigned body, logical lines 1–461;
- S3: complete body, logical lines 1–28;
- S4: complete body, logical lines 1–374.

The packet was read in contiguous raw windows covering packet lines 1–1210. After mathematical derivation and two substantive messages to the parent, I reread packet lines 1005–1070 to compare the exact inherited histogram and degree formulas.

Assigned bindings:

| Artifact | SHA256 |
|---|---|
| Manifest | `a2d5d537858324e2fd63e335d45bbbd6e1b41db68c6f70ae0dcde6abd7260455` |
| Freeze receipt | `83b7f40fd4629193c2e34b92d719b24ee4b651a3c07c0c4db49d77b01cc733fd` |
| Literal packet | `61926d558e5918c1cb68b9dfb1b48d676ca31c6e0895e57070298ad00136bea2` |

Matching hashes, byte counts and LF counts are **parent-supplied observations**, not child-executed hash checks. The observation **2026-10-30T10:39:50-0700 PDT** is likewise attributed to the parent; it is not represented as my native start, derivation time or completion time.

This was a GENERAL AUTHOR assignment. No separate pre-body written-review ACK is claimed.

The quarantine controls were used for status and boundaries only. No held scientific payload, held \(t=28\) phase/compression route, PH registration/report consumer, or outside sibling outcome was followed or used. No public webpage or paper was opened. The prior public-source statements inside the supplied packet remain attributed packet content, not newly inspected sources.

All calculations below are written counting and finite algebra. No interpreter, solver, CAS, scientific enumeration, build, test, lint or formatter was run. There are no executable outputs to report. These access statements describe the actual tool chronology; they are not a cognitive-isolation certificate.

## 3. The actual same-tensor support interface

Permute the parties so that parties \(1,2,3\) have four residual symbols and party \(4\) has five. Write
\[
A_i=\pi_i(E),\qquad
|A_1|=|A_2|=|A_3|=4,\qquad |A_4|=5.
\]

Every entry of a unitary matrix has modulus at most one. Thus \(|P|=|E|=24\).

In every balanced flattening, a unit-modulus entry exhausts its row and column. The \(24\) entries of \(P\) consequently occupy distinct rows and distinct columns, with no other nonzero entry in those lines.

Deleting those rows and columns leaves a \(12\times12\) unitary containing exactly the \(24\) residual entries. Every remaining row and column has at least two nonzeros: a singleton would have modulus one and would belong to \(P\). Therefore every remaining row and column has **exactly two** nonzeros.

The three cuts cover all six coordinate-pair systems. For every pair \(ij\), define
\[
R_{ij}=\pi_{ij}(E).
\]
Then:

1. \(|R_{ij}|=12\);
2. each value of \(R_{ij}\) has exactly two extensions in \(E\);
3. \(\pi_{ij}\) is injective on \(P\);
4. for the **same** \(P,E\),
   \[
   \pi_{ij}(P)=[6]^2\setminus R_{ij}. \tag{1}
   \]

Although full \(2\times2\) block closure also follows from actual orthogonality, the new contradiction below needs only this exact support interface.

For \(a\in A_i\), let
\[
p_i(a)=|\{w\in P:w_i=a\}|,\qquad
r_i(a)=|\{b:(a,b)\in R_{ij}\}|.
\]
Injectivity and (1) give
\[
r_i(a)=6-p_i(a), \tag{2}
\]
so the degree is independent of the partner party \(j\). Also,
\[
|\{w\in E:w_i=a\}|=2r_i(a),\qquad
\sum_{a\in A_i}r_i(a)=12. \tag{3}
\]

A used symbol cannot have degree one. Otherwise precisely two residual words would contain it, and the unique neighbor at every other party would force those words to coincide. Hence
\[
r_i(a)\ge2. \tag{4}
\]

No no-distance-one assertion has been used.

## 4. Exact maximal-word counts and degrees

Call a coordinate of \(w\in P\) **internal** when its symbol lies in the corresponding \(A_i\). Put
\[
k(w)=|\{i:w_i\in A_i\}|,\qquad
n_s=|\{w\in P:k(w)=s\}|.
\]

Because \(\sum_i|A_i|=17\), equations (2)–(3) give
\[
\sum_{w\in P}k(w)=6\cdot17-48=54. \tag{5}
\]

For each pair \(ij\), exactly \(|A_i||A_j|-12\) maximal words are internal at both positions. Thus
\[
\sum_{w\in P}\binom{k(w)}2
=3\cdot16+3\cdot20-72
=36. \tag{6}
\]

For \(k=0,1,2,3,4\), the values of
\[
\binom{k}{2}-2k+3
\]
are respectively \(3,1,0,0,1\). Summing and using (5)–(6) gives
\[
3n_0+n_1+n_4=36-2\cdot54+3\cdot24=0.
\]
Consequently all maximal words have two or three internal coordinates, and
\[
n_2=18,\qquad n_3=6. \tag{7}
\]

For \(a\in A_i\), let \(\tau_i(a)\) count the three-internal-coordinate maximal words containing \(a\). Counting other internal coordinates in the maximal words containing \(a\) gives
\[
p_i(a)+\tau_i(a)
=\sum_{j\ne i}\bigl(|A_j|-r_i(a)\bigr).
\]
Using (2),
\[
\tau_i(a)=17-|A_i|-6-2r_i(a). \tag{8}
\]

### 4.1 Four-symbol parties

For \(i\in\{1,2,3\}\),
\[
\tau_i(a)=7-2r_i(a)\ge0,
\]
so \(r_i(a)\le3\). The four degrees sum to twelve, hence
\[
r_i(a)=3,\qquad p_i(a)=3,\qquad \tau_i(a)=1 \tag{9}
\]
for every symbol of every four-symbol party.

Thus **each of the twelve four-party symbols occurs in exactly one maximal triple**.

### 4.2 Five-symbol party

At party \(4\),
\[
\tau_4(a)=6-2r_4(a)\ge0.
\]
Together with (3)–(4), the degree multiset is
\[
(3,3,2,2,2). \tag{10}
\]

Call the degree-three symbols \(H\), with \(|H|=2\), and the degree-two symbols \(L\), with \(|L|=3\). Equation (8) gives
\[
\tau_4(h)=0\quad(h\in H),\qquad
\tau_4(\ell)=2\quad(\ell\in L). \tag{11}
\]

The total number of maximal triples containing party \(4\) is therefore six. By (7), these are **all** maximal triples.

Hence every maximal triple contains:

- party \(4\), using a symbol of \(L\);
- exactly two of parties \(1,2,3\).

Each \(\ell\in L\) occurs in exactly two such triples.

## 5. Simultaneous missing-matchings structure from the common \(P\)

For \(i,j\in\{1,2,3\}\), define
\[
M_{ij}=(A_i\times A_j)\setminus R_{ij}.
\]
By (9), this is a perfect matching between the two four-symbol sets.

The four edges of \(M_{ij}\) are precisely the internal \(ij\)-projections of four maximal words. Split these edges into:

- \(T_{ij}\): those supplied by maximal triples, which also contain party \(4\) internally;
- \(F_{ij}\): those supplied by maximal words whose only internal coordinates are \(i,j\).

These are actual projections of the same \(P\), not independent choices of pair matchings.

Let \(x_{ij}=|T_{ij}|\). Each four-symbol party has four symbols, each in exactly one maximal triple. Therefore
\[
x_{12}+x_{13}=4,\qquad
x_{12}+x_{23}=4,\qquad
x_{13}+x_{23}=4,
\]
so
\[
|T_{12}|=|T_{13}|=|T_{23}|=2. \tag{12}
\]
Consequently
\[
|F_{12}|=|F_{13}|=|F_{23}|=2. \tag{13}
\]

On the disjoint union \(A_1\sqcup A_2\sqcup A_3\), set
\[
T=T_{12}\cup T_{13}\cup T_{23},\qquad
F=F_{12}\cup F_{13}\cup F_{23}.
\]

Equation (9) says that \(T\) is a perfect matching on all twelve vertices. Each vertex has one missing-matching edge toward each of the other two parties, exactly one of which belongs to \(T\). Thus \(F\) is also a perfect matching, and
\[
M_{12}\cup M_{13}\cup M_{23}=T\sqcup F. \tag{14}
\]

This is the simultaneous compatibility forced by the common maximal-word set.

As an additional necessary classification, every component of (14) is an alternating cycle. Its party colors repeat \(1,2,3\), so its length is divisible by three; alternation makes it even. With twelve vertices, the only possibilities are
\[
C_{12}\qquad\text{or}\qquad C_6\sqcup C_6. \tag{15}
\]
Neither possibility is asserted to be sufficient for a common packing or a tensor.

### 5.1 Complete maximal-word type counts

All \(24\) maximal words are accounted for as follows:

| Internal positions | Count |
|---|---:|
| \(ij4\), for each pair \(ij\subset\{1,2,3\}\) | \(2\) |
| \(ij\), for each pair \(ij\subset\{1,2,3\}\) | \(2\) |
| \(i4\), for each \(i\in\{1,2,3\}\) | \(4\) |

The first two rows contribute six words each; the last contributes twelve.

For the last row, fix a four-party symbol. It occurs in three maximal words: one \(T\)-word, one \(F\)-word, and therefore one word whose internal positions are that party and party \(4\).

The missing graph between \(A_i\) and \(A_4\) has degree two at each \(A_i\)-symbol, degree one at each \(h\in H\), and degree two at each \(\ell\in L\). Every incidence here still comes from the same \(P\).

## 6. The actual four-word slice lemma

Fix any degree-two symbol \(\ell\in L\). For \(i\in\{1,2,3\}\), let
\[
N_i=\{a\in A_i:(a,\ell)\in R_{i4}\},\qquad
S_i=A_i\setminus N_i.
\]
Since \(r_4(\ell)=2\),
\[
|N_i|=|S_i|=2. \tag{16}
\]

The actual residual slice
\[
E_\ell=\{w\in E:w_4=\ell\}
\]
contains four distinct words. At every other party, its two neighbor symbols occur twice each.

**Four-word slice lemma.** Among the three pair projections of \(E_\ell\) onto parties \(1,2,3\), at most one fails to contain the entire corresponding product \(N_i\times N_j\).

**Proof.** Index the four distinct words by a four-element set \(V\). At each party, its two symbols partition \(V\) into two sets of size two.

There are exactly three unordered \(2+2\) partitions of a four-element set. Two distinct such partitions intersect in four singleton cells; the corresponding coordinate-pair projection therefore contains all four symbol pairs.

If all three coordinate partitions were equal, the words would have only two distinct coordinate triples: each of the two partition classes would consist of duplicate words. This contradicts distinct support words.

Thus either:

1. all three partitions are distinct, and all three pair projections are full; or
2. exactly two partitions coincide, and only their coordinate pair can be non-full.

This proves the lemma. \(\square\)

This argument includes the distance-one possibility. In case 2, the coincident-coordinate pair takes two values twice each, while each pair involving the remaining coordinate takes all four values once. No inherited no-distance-one restriction has been imposed.

## 7. Transferring slice fullness through the simultaneous matchings

For a perfect matching \(M_{ij}\), the two-by-two partitions
\[
A_i=N_i\sqcup S_i,\qquad A_j=N_j\sqcup S_j
\]
satisfy
\[
|M_{ij}\cap(N_i\times N_j)|
=
|M_{ij}\cap(S_i\times S_j)|. \tag{17}
\]

Indeed, if the left side is \(x\), the two matching edges leaving \(N_i\) include \(2-x\) edges toward \(S_j\), and the two matching edges entering \(N_j\) include \(2-x\) edges from \(S_i\). The remaining \(x\) edges join \(S_i\) to \(S_j\).

If the slice projection onto \(ij\) is full, then every value of \(N_i\times N_j\) lies in \(R_{ij}\), so no edge of \(M_{ij}\) lies there. Equation (17) yields
\[
M_{ij}\cap(S_i\times S_j)=\varnothing. \tag{18}
\]

The four-word slice lemma therefore implies:

> Among \(M_{12},M_{13},M_{23}\), edges joining the corresponding \(S\)-sets can occur in at most one party pair.

Now consider the two maximal triples containing \(\ell\). Their other symbols lie in the corresponding \(S\)-sets, because their pairs with \(\ell\) are used by \(P\), and hence are excluded from \(R_{i4}\).

These two triples supply two \(T\)-edges joining \(S\)-sets. Consequently there must be an exceptional pair \(ij\), and **both triples containing \(\ell\) use that same pair \(ij\)**.

They are disjoint edges because \(T\) is a perfect matching. By (16), they exhaust \(S_i,S_j\). Hence
\[
T_{ij}\text{ joins }S_i\text{ bijectively to }S_j. \tag{19}
\]

Let \(k\) be the third party among \(1,2,3\). Since every vertex has exactly one \(T\)-edge, and each \(T\)-pair has two edges, equation (19) forces
\[
T_{ik}\text{ to exhaust }N_i,\qquad
T_{jk}\text{ to exhaust }N_j. \tag{20}
\]

These are consequences of the global common-\(P\) incidence, not independently adjusted matchings.

## 8. Final contradiction in the remaining slice case

The set \(S_k\) has two symbols. Choose \(a\in S_k\).

Its unique \(T\)-edge goes to either party \(i\) or party \(j\). Without loss of generality, suppose it goes to party \(i\).

The other missing-matching edge incident to \(a\), namely its edge in \(M_{kj}\), then belongs to \(F_{kj}\), not \(T_{kj}\).

By (20), the two edges of \(T_{kj}\) exhaust \(N_j\). Since \(M_{kj}\) is a perfect matching, its remaining two edges \(F_{kj}\) end in \(S_j\). Therefore the \(M_{kj}\)-edge incident to \(a\) joins
\[
a\in S_k
\quad\text{to a symbol in }S_j.
\]

But \(kj\ne ij\), so \(kj\) is a nonexceptional pair. Equation (18) forbids exactly such an \(S_k\)-to-\(S_j\) edge.

This contradiction excludes the remaining slice case.

Every degree-two symbol \(\ell\in L\) would produce this contradiction. Such symbols are forced by (10), so the entire \(4445\) class is impossible. \(\square\)

## 9. Explicit coverage of the possible triple-color incidences

The proof above already covers the entire class. The following separates the previously possible incidence families.

Color a \(T\)-edge by its party-\(4\) symbol \(\ell\in L\). Each color occurs twice, and each party pair contains two \(T\)-edges.

Equivalently, the \(3\times3\) incidence matrix, with rows indexed by the three low symbols and columns by the three party pairs, has nonnegative integer entries and every row and column sum equal to two.

Up to row and column permutations, its possibilities are:

1. three rows concentrated in single columns: \(2I_3\);
2. one concentrated row and two rows split across the other two columns;
3. every row split across two columns: \(J_3-I_3\).

There are no other possibilities: an entry two removes its row and column; if no entry is two, every row and column has exactly one zero.

A split row places the two triples of one low symbol in different party pairs. Sections 6–7 exclude this immediately: its slice allows \(S\)-to-\(S\) missing edges in at most one pair.

Thus families 2 and 3 are excluded at that step. Family 1 is precisely the same-pair case closed in §8.

There is therefore **no remaining \(4445\) incidence family** in this author candidate. This is not a claim that the three binary-shadow matrices were physical supports.

## 10. Dependency and source-alignment audit

### 10.1 Exact logical relation

Let \(H_{4445}\) mean exactly the hypotheses of §1, including the fixed-basis support and modulus counts.

The argument establishes
\[
H_{4445}
\Longrightarrow
\text{shared-\(P\) exact-two-extension interface}
\Longrightarrow
\text{the simultaneous \(T/F\) structure}
\Longrightarrow
\bot.
\]

Every implication is reconstructed above.

In fact, the contradiction uses only the following combinatorial interface:

- \(24\) maximal words with injective projections onto every coordinate pair;
- \(24\) distinct residual words;
- complementary maximal and residual pair projections;
- exactly two residual extensions per residual pair value;
- residual alphabet sizes \(4445\).

The actual tensor hypotheses imply this interface. Proving that this necessary interface is impossible excludes the actual tensor class; it does not substitute a relaxed feasibility claim for physical feasibility.

### 10.2 No-distance-one is not needed

The slice lemma explicitly retains both possibilities for four balanced words:

- all three coordinate partitions distinct;
- exactly two coordinate partitions equal.

The second is the distance-one alternative relevant here. It is excluded using the common-\(P\) matchings, not discarded by an inherited theorem.

Thus this proof does not assume no-distance-one or infer it from the earlier \(4444\) result.

### 10.3 No-OLS(6) is not needed for this theorem

The proof does not import:

- a restriction that all possible residual alphabets belong to \(\{3,4,5\}\);
- an external-partner theorem;
- no-distance-one;
- no-OLS(6).

The alphabet sizes \(4445\) are explicit hypotheses of the theorem, and their necessary degrees are rederived.

This does **not** remove the no-OLS provenance of older results that used it. If the new theorem is eventually combined with an earlier necessary-profile list, that list retains its own assumptions and source dependencies.

### 10.4 Relation to the frozen sources

- **S1 and S2:** Their \(4444\) normal form and written review were read but are not premises of this proof. No \(4444\) canonical labels, parity gauges, or forced-word table were transferred to \(4445\).
- **S3:** Supplies the adopted contextual interface and reporting boundary. The necessary support interface and \(4445\) degrees used here are also reconstructed independently in §§3–4.
- **S4:** Its \(4445\) histogram and degree formulas agree with §§4–5. Its external-partner lemma and inherited no-distance-one hypothesis are not used.

No unspecified historical convention about “maximal,” “residual,” \(t\), normalization, or phases is silently imported: all are defined in §1.

No printed-book equivalence or broader original-source equivalence was newly investigated. The source alignment established here is with the **explicit same-tensor \(4445\) caller in the frozen packet**, not an unexamined historical or public formulation.

## 11. Results, negative findings and verification boundary

### Supplied result

A complete written author proof excludes every actual complex tensor in the exact \(4445\) class of §1. The contradiction already occurs at the shared support interface.

### What was not supplied or claimed

- No physical tensor witness.
- No numerical optimization or failed-search argument.
- No exhaustive support enumeration.
- No executed finite checker.
- No independent-family, human or formal/kernel verification.
- No public-source priority or novelty assessment.
- No exclusion of the other residual profiles.
- No universal \(t=24\), support-\(48\), or \(N\ge49\) conclusion.
- No rehabilitation of any held output or consumer.

### Remaining acceptance work

The mathematical proof is returned as a complete **author candidate**, not self-adopted evidence. The separate acceptance obligations are:

1. A disjoint reconstruction, particularly of the four-word partition lemma, the equality in (17), and the final \(T/F\) incidence argument.
2. Parent materialization, pinning and disposition of this complete body.
3. Any separately assigned finite gate, clearly distinguished from this unexecuted written derivation.
4. Public-source novelty screening before any novelty claim.

No proper subfamily is being presented as the whole class: both split-color and concentrated-color triple families are explicitly resolved above. The unresolved boundary is acceptance and the other scientific classes, not an omitted \(4445\) support or complex-phase case.

## 12. Additive parent-clock attribution

After the earlier complete manuscript return, the parent supplied the actual `/bin/date` observation:

**2026-10-30T10:47:18-0700 PDT.**

This is **parent-only metadata**. It is not my native start, private derivation time, completion time, or an independently executed child observation. Its receipt did not authorize or cause additional scientific execution, alter the frozen role, or change any mathematical statement above.

The earlier return remains a historical complete-body return; this addition does not backdate its creation or any derivation. If that body has already been materialized, its bytes should remain preserved and this clock attribution treated additively.

**Final status: COMPLETE WHOLE-\(4445\) WRITTEN AUTHOR CANDIDATE; UNREVIEWED; NOT ADOPTED.**