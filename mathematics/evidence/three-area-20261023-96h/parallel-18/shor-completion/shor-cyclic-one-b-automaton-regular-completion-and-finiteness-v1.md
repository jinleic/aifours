# Shor — explicit cyclic one-b automaton: complete regular extension and exact finiteness test

Owner MathShor / MathShor-2. Actual `/bin/date` before writing: **Sun Oct 25 16:02:58 PDT 2026**. WRITTEN CANDIDATE, unreviewed. No scientific program/interpreter/arithmetic execution/enumeration/replay/solver/CLI/nested agent/new GO. No actual Shor completion witness is claimed.

## 0. Exact purpose and inputs

This gives an ACTUAL graph/code construction from an arbitrary fixed one-b border candidate, not a placeholder for a raw realization theorem. It characterizes finiteness of THIS explicit construction exactly. It does NOT characterize every possible finite completion or every possible automaton extension.

Use fixed n,A,B,Y with0inA,B, A+B=Z_n direct, and the ALL-t border bijections for the ACTUAL arbitrary Y. The previous successor proves an exact fixed-candidate finite linear criterion for that hypothesis without imposing a row normal form:

`shor-actual-Y-complement-automaton-and-finite-linear-border-test-v1.md`, SHA256 `ebf60e3d3db9450bad5d8274adb39fe307930dad24bdf78465c8a07ba641ac96`.

For the original Shor application Y contains all sixteen C residue pairs and n>14, so their canonical lifts are the actual C words. Let

    M0={a^n} union{a^i b a^j:(i,j)inY,0<=i,j<n}.

No unknown rows, endpoint tiles, wraps or other Y pairs are removed in §§1–3. The special common-mate row normal form appears ONLY in §4 and is clearly separated.

## 1. The full explicit graph and its first-return code

Construct a finite labelled graph G on vertices Z_n with distinguished base0:

- for EVERY v, put the a-edge v->v+1 modn;
- for EVERY(i,j)inY, put the b-edge i->−j modn.

Different Y pairs give different b-edges; canonical j uniquely determines its endpoint. There are no epsilon edges. Let X be the SET of labels of nonempty paths0->0 having no internal visit to0. This is a regular language, described exactly by this finite graph with initial/final copies of0 and all internal0-visits forbidden. No scientific program is needed to define it.

Each a^n is a first return. Each a^i b a^j from Y is a first return: before its b the path advances from0 to i without returning; after its b it advances from−j to0 for the first time after j steps. The cases i=0 or j=0 cause no problem. Thus M0subsetX, and in particular CsubsetX when Y contains the literal seeds.

### 1.1 Unambiguity and unique decipherability

Suppose TWO graph paths0->0 have the SAME word label. If that label has t b's, write its actual a-run lengths as l0,...,lt. A path is specified by its t b-edges, hence by a tuple(i1,j1),...,(it,jt)inY. It necessarily satisfies

    i1=l0 modn,
    j_s+i_(s+1)=l_s modn,
    jt=lt modn.

These are the BT outputs with initial B marker0 and terminal A marker0. Injectivity of the t-border map therefore forces the SAME Y tuple. All a-edges are deterministic, so the graph paths themselves agree. For t=0 the a-cycle is deterministic directly.

Every loop at0 has a UNIQUE decomposition at its successive visits to0 into first-return paths. If two lists of words of X had the same concatenated label, their graph loops would be the same by the preceding unambiguity argument, and the intermediate0 visits force the same first-return cuts and same word list. Thus X is a RAW UD code, even when it is infinite. No residue cancellation is being asserted as an actual word identity.

### 1.2 Factor completeness

Take ANY binary word w with t b's and actual a-run lengths l0,...,lt. Border surjectivity supplies d inB,s inA and Y pairs with

    d+i1=l0, j1+i2=l1,...,jt+s=lt modn.

The graph therefore has a path labelled w from vertex−d to vertex s: each a-run advances modulo n, and the b-edges have exactly the required endpoints. Prefix this path by a suitable a-run from0 to−d and suffix it by one from s to0. This creates a graph loop at0 whose label contains w as a literal factor. Every such loop label is in X* by its0-return decomposition. Pure-a words are handled by the a-cycle alone.

Therefore X is factor-complete on the FULL binary alphabet. It is an explicit complete REGULAR UD extension of M0. This conclusion is conditional on the actual border candidate; no such candidate containing the Shor seeds has been found here.

## 2. Exact finiteness criterion for THIS graph construction

The following are equivalent:

1. X is finite.
2. The induced graph on nonbase vertices{1,...,n−1} has NO directed cycle.
3. EVERY canonical Y pair satisfies i+j<n.

**2=>1.** A first-return path can visit each nonbase vertex at most once in a finite acyclic graph. Hence its length is at most n; there are finitely many such paths/labels. Thus this is a genuine finite code construction when the criterion holds.

**1=>2.** If a nonbase directed cycle exists, reach one of its vertices from0 along the a-cycle without visiting0 internally, repeat that directed cycle m times, then continue along a-edges to0 without an earlier0. These are first-return paths for every m, and their word lengths strictly increase with m. X is infinite.

**3=>2.** All nonbase a-edges strictly increase the canonical vertex index. If i,j are nonzero and i+j<n, the b-edge target n−j is STRICTLY greater than i. Edges with i=0 or j=0 do not lie in the induced nonbase graph. Consequently every remaining edge strictly increases the index, so a nonbase cycle is impossible.

**2=>3.** If i+j>=n, canonical i,j must both be nonzero. The b-edge i->n−j has target<=i. Follow a-edges from n−j to i and then this b-edge back; this is a directed nonbase cycle, including the equality self-loop case. Thus no such pair exists if the induced graph is acyclic.

We therefore have an explicit sufficient POSITIVE route for the original problem: find actual n,A,B,Y satisfying the full border condition and all i+j<n; the first-return code X above is then a finite RAW UD factor-complete superset of C with word lengths<=n. This is a fully defined conditional construction, not a supplied witness, and not an asserted characterization of all possible positive solutions.

## 3. A concrete control: infinity here does NOT exclude finite completion

At n=2 take A={0,1},B={0},Y={(0,0),(1,1)}. For every t the border equations determine the successive one-b rows uniquely: the first output determines the row, each later input determines the next row, and the last output determines the final A marker. Thus this Y satisfies ALL-t BT.

Its M0 is{aa,b,aba}. Its cyclic graph has a-edges0->1->0 and b-loops at BOTH0 and1. The first-return code is

    X={b,aa} union{a b^k a:k>=1},

which is infinite by the nonbase b-loop.

Nevertheless the finite set

    P={b,aa,aba,abb}

is a RAW factor-complete UD extension of M0. It is prefix: at the root b is a leaf, after a the aa leaf is separated from the ab branch, and that branch has leaves aba/abb. Every nonleaf has both binary children, so parsing an arbitrary word and extending its last incomplete prefix reaches a leaf; hence every word is a prefix, and therefore a factor, of a P-product. Prefix parsing is unique. This is a direct written proof, not a generated finite-witness/triple-checker claim.

The example is a METHOD CONTROL, not a substitute Shor instance. It proves that a cycle/infinite first-return language in THIS cyclic automaton is NOT a nonexistence theorem for finite completion. A different finite graph can split histories/add transitions; it need not be a carry-preserving cover of G. The n=2 control has no Shor seeds and does not repair or verify the original target.

## 4. The particular common-mate row construction ALWAYS falls in the infinite side

Now assume the SAME-A common mates B,D2,D3 and the special normal form

    row0=B,row3=row8=D2,row11=D3,
    every other row i inA is B.

I prove its explicit cyclic graph necessarily has a nonbase cycle at EVERY unknown order. This is a statement about that construction, not the actual arbitrary Y of every hypothetical finite original completion.

### 4.1 The original seed tile has a forced wrapped sum at residue2

A cannot contain1, since0+1=1+0 would collide using B0/1. A cannot contain2, since3+0=2+1 would collide using A3 and B0/1. B cannot contain2, since8+2=3+7 would collide using A8/3 and B7.

Thus integer2 has NO unwrapped representation from A+B: the only possibilities are(0,2),(1,1),(2,0). But A+B tiles Z_n. Its unique cyclic representation of2 therefore has actual canonical sum n+2. In particular

    max(A)+max(B)>=n+2.                                  (4)

This retains ALL unknown endpoint positions and uses only literal seed collisions, not a bound on their size.

### 4.2 A has some element greater than11

Within{0,...,11}, no point outside I can belong to A. Values1/2 are excluded by mate differences1/2; 4/5 differ by1/2 from A3; 6/7 are forbidden B-seed differences; 9/10 differ by1/2 from A8. The mate differences1 and2 are supplied by D3 and D2 respectively. Thus A intersect{0,...,11}=I.

Also A cannot equal I. If it did, write I={0,3}+{0,8}, a direct sum. Then U=B+{0,8} is a SET and U+{0,3}=Z_n direct. Its membership function alternates on every +3 orbit: exactly one of x,x−3 is in U. But U contains0 through B0 and9 through B1+8. Those two points are three +3 steps apart, so their simultaneous presence contradicts alternation. This argument also covers an odd +3 orbit, where no such alternating tiling exists at all.

Consequently max(A)>11. At that maximum row the chosen normal form uses B. It therefore includes the actual pair(max(A),max(B)), whose canonical degree is>=n+2 by(4). Section2 gives a directed nonbase cycle and an INFINITE X for this whole normal-form family.

Thus the most immediate explicit regular completion of the common-mate normal form never itself provides a finite completion. The reason is an actual wrapped pair forced by the original seeds, not merely a guessed failure of an algorithm. Section3 proves why this does NOT exclude finite completion by a different graph or a different actual Y.

## 5. Exact original residual, dependencies, and assurance

The new positive-realization criterion in §2 is sufficient, not necessary, for the original problem. The new negative result in §4 closes ONLY the unsplit cyclic-automaton route for the selected common-mate normal form. Neither result may be silently substituted for all finite raw UD factor-complete extensions.

The original remaining alternatives are still: construct an ACTUAL finite completion containing C (possibly using another Y and genuine multib history structure), or prove a uniform obstruction for EVERY actual finite PR-saturated raw prefix, arbitrary orders/lengths/b-counts/heterogeneous delays/bridge arities, and raw STAB. No common-mate witness, winning finite graph, or such uniform obstruction is supplied.

Imports are the explicitly stated all-t border interface and elementary finite graph/path facts. All model-specific unambiguity, completeness, finiteness, wrapped-pair and toy-control arguments are supplied above. The proof uses no current-status literature claim, H*, exhaustive known-construction assertion or unseen realization converse. H* stays WITHDRAWN. Original FACT/full-code order distinctions, k7/Phi_n and all larger-trade residuals remain.

All claims are WRITTEN only, not formal/kernel/executable/finite-triple-checker/configured-family/human/independent-review/SOTA/novelty/publication acceptance. No actual graph was executed or enumerated. The original cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 are unchanged. This is not round closeout.
