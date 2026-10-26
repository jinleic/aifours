# Exact finite raw-word realization protocol for the Shor target

Observed before creation: **2026-10-23T14:10:16-0700 PDT**. Status: **written certificate protocol and bridge analysis**, not a produced Shor completion, executable verifier, admitted search, or novelty claim. No scientific execution occurred.

The parent requested that continuation use the raw-word realization interface, not another collection of necessary order conditions. This file specifies a certificate whose successful instance really would change the existence answer, proves its sufficiency directly, and exhibits a finite positive-control code showing why residue realization is not the same certificate.

## 1. The exact unresolved bridge

The inherited all-t residue data and the Cordero n-cbc framework are necessary conditions. The following are distinct obligations:

1. R,L actually form a cyclic factorization and Y has n points.
2. Y is an n-cbc, with its required stable compatibility/border.
3. Y occurs as C_M(ω) for an actual **finite maximal** M and some word ω.
4. The exact sixteen **literal short words** in the book belong to a finite UD complete M over {a,b}.

No inspected theorem makes 1 or 2 imply 4. Cordero 2023, immediately after Definition 1.5, explicitly leaves the general realization in 3 unknown. Even 3 does not literally assert 4: ω need not be b, residue representatives need not be the short words, and membership of a long padded representative in M* cannot simply be cancelled inside an arbitrary free submonoid.

The missing constructive ingredient is therefore a **finite raw-word realization**, not a different permissible value of n. The protocol below is fully sufficient for 4 and introduces no bound on n, the number of b's in codewords, cardinality, symmetry, or maximum length.

## 2. A concrete raw-representative negative control

This example is not Shor's code and is not evidence for either answer to the Shor problem. It isolates an actual logical failure that a realization certificate must avoid.

Let

    P=aa,    B=b,    X=aba,    Y=abb.

The set K={P,B,X,Y} is a finite complete prefix code: b is one branch, and under a the leaves are aa, aba, abb. Over the four-symbol abstract alphabet {P,B,X,Y}, the set

    N={P,B,Y,PX,BX,YX,XX}

is a finite complete suffix code. Indeed its reversal is the prefix code whose leaves are P,B,Y and XP,XB,XY,XX. Substitution of the four words of K is injective on every abstract string because K is a prefix code. Consequently the following substituted set M0 is UD:

    M0={aa, b, abb, aaaba, baba, abbaba, abaaba}.

It is complete. Its exact binary Kraft sum is

    1/4 + 1/2 + 1/8 + 1/32 + 1/16 + 1/64 + 1/64 = 1,

and the sufficiency proof in section 4 below is independent of any prefix assumption on M0.

The unique pure-a codeword is a^2. The only one-b codewords are b and aaaba=a^3 b a. Thus the canonical residue data C_M0(b) at n=2 are

    {(0,0),(1,1)},

which include the short representative aba. Nevertheless **aba∉M0***. A nonempty product yielding aba must begin with a word of M0 that is a prefix of aba. None is: aa mismatches the second letter, abb the third, b the first, and all other codewords are too long.

Hence “the canonical point (1,1) is in C_M(b)” does **not** imply “aba is in M*”, even with an actual finite UD complete M and b,a^n∈M. No converse realization theorem is refuted by this control; it refutes only the unsupported cancellation/representative inference. In particular it is not a counterexample to finite completability of the canonical two-point bayonet code.

## 3. A useful exact short-word bridge

**Lemma.** Let M be any UD code over {a,b} with a^n∈M, n>0. If 0≤i,j<n and a^i b a^j∈M*, then a^i b a^j∈M.

**Proof.** UD implies that a^n is the only pure-a codeword: distinct powers a^n and a^m would give two factorizations of a^(mn). A factorization of a^i b a^j has exactly one codeword containing b, since the total number of b's is one. Every other codeword is the pure-a word a^n and lies before or after that one codeword. Since each outer a-run is shorter than n, there can be no such pure-a codeword. The factorization has length one. QED.

For the exact Shor C, all left and right exponents are ≤14. Therefore, for any UD M with pure-a order n>14, it is enough for a producer to certify literal **M*** membership of each short Shor word: the lemma upgrades all sixteen to actual M membership. This does not apply to residue membership alone. The negative control above has the canonical representative absent from M0*, exactly where the lemma's hypothesis fails.

This bridge is elementary and not claimed as new prior art. Its role is to make the certificate interface exact when a producer supplies an accepting automaton for M* instead of directly asserting which short words are primitive codewords.

## 4. Sufficient certificate, with no code-theoretic theorem import

A positive certificate consists of a finite, duplicate-free set of nonempty literal words M⊆{a,b}*, together with a finite set S⊆{a,b}^+ of residual words. Every word is stored literally or by a **lossless maximal-run encoding**, not merely by its Parikh vector or residue pair. Let D=max{|x|:x∈M}.

The following four conditions suffice:

**A. Literal target binding.** Each of the sixteen exact Shor words is a member of M. Alternatively use the lemma in section 3 with a verified a^n∈M, n>14, and sixteen literal M* factorization lists. No residue-only assertion is accepted.

**B. Initial residual coverage.** For every distinct x,y∈M, if y=xr or x=yr with r nonempty, then r∈S.

**C. Residual closure and empty exclusion.** For every r∈S and every x∈M:

- if r=xv, then v∈S;
- if x=rv, then v∈S;

and ε∉S. In particular r=x is forbidden: it would require ε∈S. These clauses include all comparable pairs and are checked against the raw words. S may be a superset of the reachable residuals; it need not be a producer's claimed traversal trace.

**D. Exact Kraft equality.** If c_l is the number of raw words of M of length l, verify the length profile against M itself and then verify the integer equality

    Σ_(l=1)^D c_l · 2^(D-l) = 2^D.

There is no floating-point tolerance. A length-profile file without raw-word binding is not a certificate.

### Why B–C imply UD

Suppose distinct finite lists from M have the same concatenation. Remove their common initial codewords, so the first remaining codewords are distinct and prefix-comparable. B puts the nonempty excess suffix in S. Repeatedly compare this residual with the next codeword on the shorter side; prefix cancellation and C keep every nonempty residual in S. Because the two finite concatenations eventually end together, the process eventually reaches an empty residual. C forbids that. Thus no two different lists have the same concatenation. This is the classical Sardinas–Patterson mechanism, with its soundness proved here rather than imported from a checker output.

### Why UD and D imply the book's factor completeness

Let f=Σ_(x∈M)2^(-|x|)=1. UD makes the map from all finite lists to M* injective, hence the nonnegative series satisfies

    Σ_(z∈M*) 2^(-|z|) = Σ_(t≥0) f^t = ∞.

If a nonempty word w of length h were a factor of no word in M*, all words of M* would avoid w. An avoiding word of length kh+r, 0≤r<h, must avoid w in each of its k disjoint length-h blocks. There are at most

    (2^h-1)^k · 2^r

such words. Their total normalized mass is therefore at most

    Σ_(r=0)^(h-1) Σ_(k≥0) (1-2^(-h))^k = h·2^h < ∞,

contradicting the preceding divergence. Thus every nonempty w occurs as a factor of some z∈M*. The empty word occurs automatically. This is exactly the book's completeness quantifier, without an appeal to a cyclic-factorization converse. QED.

## 5. Completeness of the protocol as a witness language

The protocol is not an ansatz: **every** actual finite UD complete M containing C admits such an S and satisfies D.

For S take all residuals reachable from the initial proper-prefix residuals by the transitions in C. Every residual is a nonempty proper suffix of a word in M, so the universe is finite. If ε were reachable, reversing the same prefix-cancellation steps gives two distinct lists with equal concatenation, contrary to UD. Thus B–C hold.

For completeness of condition D, first show f≤1 for every finite UD M. Concatenations of exactly t codewords have lengths between t and tD and are distinct. At each length L there are at most 2^L words; hence

    f^t ≤ tD-t+1.

If f>1 the left side grows exponentially and violates this linear bound. Therefore f≤1.

Now suppose M is also complete but f<1. Then

    Σ_(z∈M*)2^(-|z|)=1/(1-f)<∞.

Every word w occurs as a factor of some product from M. Remove whole codewords lying strictly before and after this occurrence. This leaves z=u w v∈M* with |u|,|v|≤D-1. For each fixed z and each such pair of end lengths there is at most one w, and its normalized weight obeys

    2^(-|w|) = 2^(|u|+|v|) · 2^(-|z|)
             ≤ 2^(2D-2) · 2^(-|z|).

Summing over all possible end lengths bounds the total normalized mass of **all** binary words by

    D^2 · 2^(2D-2) · Σ_(z∈M*)2^(-|z|) < ∞.

But all binary words have infinite normalized mass (each length contributes 1). Contradiction. Hence f=1, exactly D. This proof supplies the needed necessity too; no unauthenticated Szabó theorem, Reutenauer factorization, or conjectural positivity assumption is used.

Thus existence of finite raw M,S satisfying A–D is equivalent to a positive answer to the original book question. This is a certificate characterization, **not a decision algorithm for unbounded M**, a new existence proof, or a claim that such M,S have been found.

## 6. What would actually change the existence conclusion

A successful candidate must supply actual finite bytes for M and S, not just n,R,L,Y or a plan to produce them. Independent definition-level verification of A–D would prove a positive answer. The producer, parent checker and a separate reconstruction must use the same pinned M bytes, with raw parser/length-profile binding, and targeted controls must reject at the intended boundary.

Required controls include: the explicit finite M0 above (positive UD/complete control but a negative literal-aba/residue-lifting control); an ambiguous set such as {a,b,ab} (Kraft/UD boundaries kept separate); an incomplete UD set such as {aa,b}; removal of a Shor word; a changed run length; omitted residual transition; a residual equal to a codeword, forcing ε; and a forged length profile. No such executable checks have been run here.

Failure to find a certificate, rejection of a particular certificate, or exhaustion of any finite length/order bound does not prove a negative answer. A negative answer still needs an all-order obstruction that reaches **every** finite raw realization. The multiplier-separator result only closes one forced-data obstruction route; it does not supply this missing theorem.

## 7. Process boundary

There is no witness producer ready for an admitted run, and this protocol is not a request to spend compute. A scientific launch would first need an exact frozen producer/checker, source/input hashes, bounded resources, positive and intended-reason negative controls, deadline and named parent GO. No script or runtime framework was created as a substitute for the missing construction.

Correctness of the written arguments, classical priority of Sardinas–Patterson/Kraft, source trust, target scope and significance remain separate. A successful verifier of a future instance would establish a finite witness, not automatically novelty, formal/kernel proof or human acceptance.
