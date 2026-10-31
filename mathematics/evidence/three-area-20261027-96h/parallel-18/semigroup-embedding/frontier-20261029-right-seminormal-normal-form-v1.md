# A complete recursive word model for free right-seminormal bands

**Status: NEW AUTHOR WRITTEN UNIVERSAL NORMAL-FORM PROOF plus exact finite controls; UNREVIEWED / UNADOPTED.** Likely related to classical band word algorithms; no novelty is asserted. This provides an explicit smaller free-band representation for the matching one-sided source/canonical problem, not a proof that its quotient relations separate the source.

## 1. Signature and representative

For a nonempty word w, let h(w) be its first letter; let c(w) be the letter whose LAST occurrence occurs EARLIEST among the last occurrences of all letters of w; and let t(w) be the suffix strictly after that occurrence of c(w). Thus `content(t(w))=content(w)\{c(w)}`. Define recursively

`R(empty)=empty`, `R(w)=(h(w),c(w),R(t(w)))`.

**Theorem.** Two nonempty words are equal in every band satisfying `abc=acabc` iff their R-signatures agree. A canonical representative is

`N(h,c,T) = h c N(T)`, with adjacent duplicate letters contracted,

and N(empty)=empty. Every k-letter-content representative has length at most2k−1. In the free right-seminormal band, the number of elements with any fixed k-letter content is `(k!)²`, and the free n-generator size is

`R(n)=Σ_(k=1)^n binom(n,k)(k!)²`.

## 2. Universal prefix absorption and normal reduction

Use the classical ALL-band content identity: `XYZ=XZ` whenever `content(X)=content(Z)` and `content(Y)` is a subset of that content. Its Green–Rees rectangular-D-class proof and correct R-row rationale are explicitly stated in `frontier-20261028-local-one-sided-seminormal-identities-v1.md`, SHA `f94f7c43086fd9d8dac727779d4f06384f380a0c030b090f9b9f75260bd26539`; this is a named classical input.

In a right-seminormal band, if a nonempty word u has all its letters in another nonempty word v, then

`u v = h(u) v`.                                           (P)

Write u=hr with r possibly empty. If r is empty, this is tautological. Otherwise the right-seminormal identity on the words `(a,b,c)=(h,r,v)` gives `hrv=hvh rv`. Since h occurs in v and content(r)⊆content(v), apply the content identity to `X=hv`, `Y=hr`, `Z=v`: `hvh rv=hvv=hv`. This proves (P) without assuming commutativity or an identity element in the band.

Now write w=u c(w) t(w), where u is the prefix before the last occurrence of c(w). The suffix `c(w)t(w)` contains EVERY letter of w. If u is nonempty, (P) gives `w=h(w)c(w)t(w)`; if u is empty, h(w)=c(w) and the same expression reduces to w by the band square law. By induction on the number of letters, reduce t(w) recursively to N(R(t(w))). Hence every right-seminormal band satisfies `w=N(R(w))`. Equal signatures therefore imply equality of words in the whole variety.

## 3. A separating signature algebra

The R-signature product is explicit and depends only on the two signatures A=R(u), B=R(v). Let C_A,C_B be their recursively recovered content sets.

* If `C_A⊆C_B`, then every last occurrence in uv occurs inside v. Its first letter is h(u), and its critical letter/suffix are those of v, so
  `A·B=(h(A),c(B),tail(B))`.
* Otherwise set M=C_A\C_B. Follow the tail chain of A until the first critical letter c lies in M; let that signature node be `(h',c,T)`. This c is the earliest last occurrence among letters missing from v; all letters occurring in v have later last occurrences. The suffix after c is represented by T followed by v. Thus
  `A·B=(h(A),c,T·B)`.

This recursive computation strictly decreases the first signature's content in its recursive case and exactly computes R(uv). It proves concatenation signatures are independent of the chosen word representatives. Therefore the signature multiplication is associative (both bracketings compute R(uvw)), and is idempotent because w² has the same first letter and last-occurrence/suffix data as w.

For arbitrary nonempty words u,v,w, the right-seminormal identity compares `uvw` and `uwuvw`. The inserted prefix uw has all its letters in the FINAL suffix uvw, so every last occurrence occurs in that final suffix, with the same relative order and same suffixes as in uvw; both whole words begin with h(u). Thus their R-signatures agree. The signature algebra is a right-seminormal band. Distinct signatures are distinct elements in this algebra, so distinct signatures cannot be an identity of the variety. Combined with §2, this proves the theorem and freeness.

## 4. Exact counting

For a fixed nonempty content set A of size k, a signature freely chooses its first letter h∈A and its critical letter c∈A, then a full-content signature on A\{c}. Every such choice is realized by h c N(T): c has no later occurrence, all other letters do, and the head is h. Thus fixed-content counts satisfy `r₁=1`, `r_k=k² r_(k−1)`, giving `r_k=(k!)²`. The representative length is at most2k−1 because the base k=1 contributes one letter and each recursion adds at most two. The binomial sum follows by choosing the content subset.

## 5. Exact finite implementation control and limits

`frontier-20261028-seminormal-signature-checker-v1.py`, SHA `2e9aef1b644b8e389243e7462a4418713c87e4692fc1419305743cd5956afec8`, ran in the Python eval kernel before Thu Oct29 00:11:24 PDT2026. It constructs every state by generator closure for n=1,2,3,4, obtaining sizes1,6,51,748; verifies every product against concatenated representative signatures, each representative's signature and length bound, and all associativity/rightSN substitutions for n≤3. It separately builds the correlated pair of left/right signatures, giving1,6,159,21340 states for n≤4; interpreting that paired object as the free SN band requires the separate subdirect theorem and is NOT inferred solely from these counts.

All word arithmetic is exact. A finite cross-check of all representative term functions in B5 for n≤4 found pairwise distinct signatures, but the complete proof is §§2–4, not that bounded check. The normal form does not prove a canonical source relation quotient remains faithful. Matching one-sided source R/L separation, published convention/interface, formal proof, novelty and independent review remain open.
