# v71-A — complete written reconstruction of the unrestricted Tuscan boundary-turn interface

Actual returned `/bin/date` before writing: **Sun Oct 25 09:58:53 PDT 2026**. Reviewer MathResearch96h-2, mathematics reviewing InfoRecursiveMDS18-2. Strict WRITTEN reconstruction; source/date/hash metadata only. No scientific interpreter/eval/program/enumeration/symbolic program/replay/solver, external-model CLI or nested agent. V9 FIRST and v10 immediately SECOND were read completely before assignment/body; all earlier errata/HOLD remain binding.

## 1. Binding, full coverage, exposure and verdict

Exposure ACK `peer-review-tuscan-turn-coupling-ack-v1.json` preceded the proof body; v68-B had already been returned. Read ALL413 LF of the sole part `peer-review-wave-v71-v71-A-part1-v1.md`, including complete S1/v9 LF1–35,S2/v10 LF1–31,S3/NEW LF1–191,S4/asymmetry LF1–100 and S5/parent LF1–28. No source truncation was reported. Fresh metadata hashes match:

- Part: `2ac0cca6c4dfb1e9111dc7dee9920fd9066dcb53367a9eb216fd9ac624d61655`.
- NEW `unrestricted-boundary-turn-coupling-v1.md`: `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`.
- Asymmetry context: `ac898bee2bb750d48b171f364c10a3e356f06c3d0105bf613dfb726f336235e7`.
- Parent context: `bc6a819ef0ba0586aebd6ffcc0dd0a140bd1880a168e40a824198604d93ccf76`.

LF references below mean ORIGINAL NEW source LFs. The asymmetry paper is read for declared coverage ONLY: it remains an UNREVIEWED candidate context, and none of its automorphism/canonicalization claims is a premise or promoted by this return. The unrelated NL242 parent context is likewise not newly certified by a Tuscan review.

**Overall verdict:0 FATAL /0 MAJOR /0 MINOR at the entire191-LF boundary-turn theorem/interface scope. New load-bearing obligations NOT_RECONSTRUCTED: NONE.** Endpoint data, multiplicity-sensitive matrix coupling, direct n4 control, full arc periods/sign, odd-order involution obstruction and both directions of the construction interface reconstruct below.

This is a same-harness cross-domain supplied-proof written return, not parent disposition itself, executed finite certificate, formal/kernel, configured-family/cross-vendor/human or novelty acceptance. No literal11-by11 table, noninvolutive-case exclusion or unrestricted Tuscan-2(11) solution is supplied.

## 2. B0 — endpoint bijection, arbitrary boundary functions and actual center permutations

LF9–41.

At a symbol a, its n row occurrences have outgoing adjacency events except exactly those at row ends. Since each of its n-1 possible distinct outgoing arcs occurs once, n-e(a)=n-1, giving e(a)=1. The incoming argument gives one row start at every symbol. Indexing rows by starts is therefore DERIVED, not an imposed Latin first column. Their ends give a bijection tau. A row permutation cannot have equal first and last symbols, so tau has no fixed point.

The second symbol f(v) of the row starting v and penultimate symbol p(v) of the row ending v are both different from v. They are functions and are NOT required to be bijections; no argument below replaces their incidence counts by1.

Fix v. There is one row starting v and a DIFFERENT row ending v. The other n-2 occurrences are internal triples a,v,b. Their predecessors a are distinct because incoming arcs(a,v) are covered once, and their successors b are distinct by outgoing coverage. The missing predecessor is exactly p(v), and missing successor exactly f(v). Thus these actual triples are a bijection from X\{v,p(v)} onto X\{v,f(v)}.

Adding p(v)→f(v) and v→v supplies a genuine permutation K_v: the added domains/outputs are precisely the missing ones and are disjoint from each other. If p(v)=f(v), that added arrow is one EXTRA fixed point, not a duplicate diagonal of the same matching. Every other off-v arrow comes from an internal a,v,b with a≠b, because an actual row never repeats a symbol. Hence the only possible off-v fixed point is exactly that boundary p=f case. This proves Lemma1 WITHOUT using Tuscan-2 distance-two uniqueness.

The added arrow is a turn from the row ending at v to the row STARTING v. It is not a wraparound distance-two event inside one row.

## 3. B1 — exact I+Gamma+GF coupling, multiplicities and all deficits

LF43–70.

Use the stated row-tail/column-head convention. Since F_vb indicates f(v)=b and G_av indicates p(v)=a,

`(GF)_ab=sum_v 1_(p(v)=a)1_(f(v)=b)`.

Thus GF counts EXACTLY the n added boundary arrows, including diagonal and repeated entries. F has one1 per ROW and G one1 per COLUMN; neither is assumed a permutation matrix.

Summing all actual K_v counts three disjoint types of EVENT: n artificial diagonal arrows giving I, actual internal turns giving Gamma, and the n boundary events giving GF. Entrywise values add with multiplicity even if different types land on the SAME matrix entry. Therefore

`sum K_v=I+Gamma+GF`

holds for every Tuscan-1 array before any distance-two noncollision is imposed. In particular Gamma may have entries greater than1; replacing it by a zero-one matrix prematurely would be wrong.

Under Tuscan-2, Gamma has zero diagonal and distinct off-diagonal entries, total n(n-2), so M=J-I-Gamma is its actual missing-pair matrix, with exactly n ones. Rearranging yields precisely M=J+GF-sum K_v; this does not imply GF=M.

Every K_v has each row/column sum1. GF's row-a sum is #{v:p(v)=a}, because F has row sums1. Its column-b sum is #{v:f(v)=b}, because G has column sums1. Taking row/column sums in the actual matrix identity therefore gives the printed missing outdegree/indegree formulas, with total n in both. They are not separately imposed degree-feasible surrogate graphs.

As an independent event interpretation, distance-two outgoing events from a omit its unique final occurrence and its penultimate occurrences, so the deficit is exactly the penultimate count. The incoming argument similarly omits the unique start and the second-position counts. This agrees with the full matrix derivation without assuming either f or p bijective.

## 4. B2 — complete n4 calibration and rejection of GF=M

LF72–99. The rows are0123,1302,2031,3210. Their adjacency list is

`01,12,23; 13,30,02; 20,03,31; 32,21,10`.

For each first symbol0,1,2,3 this contains each of its three different targets exactly once, hence all twelve ordered distinct arcs. Their LINEAR distance-two list is

`02,13; 10,32; 23,01; 31,20`.

All eight are distinct. Complementing within the twelve distinct ordered pairs leaves03,30,12,21, exactly the stated M. There is no wraparound event in either list.

Reading actual row boundaries gives f=(1,3,0,2), p=(1,3,0,2). The four boundary pairs(p(v),f(v)) are(1,1),(3,3),(0,0),(2,2), so GF=I entrywise. It is manifestly not the off-diagonal missing matrix M.

The actual centered INTERNAL arrows are:

- v=0:3→2 and2→3, with added fixed points0,1;
- v=1:0→2 and2→0, with added fixed points1,3;
- v=2:1→3 and3→1, with added fixed points2,0;
- v=3:1→0 and0→1, with added fixed points3,2.

Thus K0=(2 3),K1=(0 2),K2=(1 3),K3=(0 1). Their diagonal entries sum to2 at every symbol; their eight nonzero off-diagonals are exactly the eight distance-two pairs above, each once. All other off-diagonals are M's four missing pairs and sum to0. This checks EVERY entry of sum K_v=J+I-M, not a checksum or a cited program output.

Consequently GF=M is a FALSE general necessity and would discard an actual Tuscan-2 array. The completed center table is not required to be a convenient idempotent Latin object.

## 5. B3 — arc permutation, actual row-splice cycles and determinant/traces

LF101–121.

On ordered distinct arcs, T(a,v)=(v,K_v(a)) remains a distinct arc because a≠v and K_v fixes v. Its inverse at(v,b) is(K_v^(-1)(b),v), so T is a bijection. At an internal incoming arc it follows the actual row successor. At the unique terminal arc(p(v),v), it moves to(v,f(v)), the FIRST arc of the row beginning at v.

Thus a row starting s, consisting of n-1 distinct arcs, is followed as a whole and then spliced to the row starting tau(s). All arcs are used by exactly one actual row. A first arc of another row cannot equal an internal arc, by adjacency uniqueness. Hence no T-cycle closes at an intermediate cut; every tau-cycle of length ell gives ONE T-cycle of length(n-1)ell, and every T-cycle is obtained this way. Starting from an arbitrary arc also eventually encounters its row boundary, so there is no extra T-cycle avoiding all starts.

A permutation cycle of length m has characteristic polynomial z^m-1. For each tau-cycle the right side det(z^(n-1)I-tau) contributes exactly(z^(n-1))^ell-1, the SAME factor. Multiplying proves the full determinant identity, with matching degree n(n-1) and no omitted scalar factor.

For n11, tau has no1-cycles, so T-cycle lengths are multiples of10 and at least20. Trace of a permutation power counts fixed arcs; none can occur for1≤k≤19. For a10k power a T-cycle10ell contributes10ell exactly when ell divides k, while the corresponding tau-cycle contributes ell. Therefore tr(T^(10k))=10tr(tau^k) for all positive integers k. Period data alone do NOT imply that the n-1-arc segments are Hamilton; the converse below retains that condition explicitly.

## 6. B4 — complete sign-product relation

LF123–129.

As FUNCTIONS, arc reversal alpha(a,v)=(v,a) followed by sigma(v,a)=(v,K_v(a)) gives T=sigma∘alpha. A row-transition-matrix convention reverses the written matrix order, but sign multiplication and all cycle invariants are unchanged. No GF/FG convention is altered by this observation.

Alpha consists of n(n-1)/2 transpositions, so its sign is(-1)^(n(n-1)/2). Sigma acts independently on the n first-coordinate fibers; fixing v means the sign of its restriction to X\{v} equals sign(K_v). Hence sign(sigma)=product sign(K_v).

Let N=n(n-1),c=c(tau). Section5 gives sign(T)=(-1)^(N-c), while sign(tau)=(-1)^(n-c). Dividing these signs and using the EVEN integer N shows

`product sign(K_v)=(-1)^(N/2-n) sign(tau)`

`=(-1)^(n(n-3)/2) sign(tau)`.

At n11 the exponent44 is even. This is an exact endpoint/turn coupling, with no global symbol automorphism, regular development or row-reversal assumption.

## 7. B5 — Theorem3 at EVERY odd order, including both split-component types

LF131–156. Assume all K_v are involutions. Split each original vertex v into one copy for each cycle of K_v on X\{v}. The original unordered edge{a,b} joins the a-copy containing b to the b-copy containing a. Different original endpoints preclude loops. Two edges joining the same two copies would have to be the SAME original unordered{a,b}, which occurs only once; thus there are no parallel edges.

A2-cycle copy has degree2 and a fixed-point copy degree1; no copy has degree0. Every component is therefore a path with at least one edge or a cycle. Mapping an ordered original arc to its oriented split edge is bijective. At a degree2 copy, K_v sends the incoming neighbour to the OTHER incident neighbour, so T continues without reflecting. At a degree1 copy it sends that neighbour to itself, so T reverses along the same edge. This proves the walk correspondence even when a split component contains several copies of one original symbol; the oriented EDGES, not just original vertex labels, distinguish arcs.

A cycle component with m edges consequently gives TWO opposite T-cycles of length m. By Section5, m is divisible by n-1, and these two cycles contain2m/(n-1) actual rows, an EVEN number.

A path with m edges gives ONE T-cycle of length2m: traverse to the far leaf, reflect, traverse back and reflect. Every leaf is an off-v fixed point of K_v, which Lemma1 says can occur ONLY at the designated boundary p(v)=f(v). It cannot be an internal a,v,a turn of a Hamilton row. Thus BOTH reflections are actual row boundaries. Their terminal-arc positions in that T-cycle are exactly m T-steps apart. Row-boundary positions are spaced by n-1 steps throughout the spliced actual rows. Hence m, not just2m, is divisible by n-1. The path contributes2m/(n-1) rows, again EVEN.

Local turns remain within their split copies, so no row or T-cycle straddles two split components. All oriented arcs, all T-cycles and therefore ALL n actual rows have been accounted for. Summing the even contributions makes n even, contradiction. This uses Tuscan-1 adjacency coverage and row permutations ONLY; no Tuscan-2 uniqueness or asymmetry theorem is needed.

For the four-symbol consequence, v itself is fixed and cannot belong to a long cycle. In an off-v cycle of length≥3, at most ONE arrow is the added p(v)→f(v). If present remove it; at least two consecutive actual arrows remain. If absent choose any two consecutive arrows. Their outer symbols a,b,c are distinct and different from v. Thus actual triples a,v,b and b,v,c occur. They must be in different rows because a row has only one occurrence of center v. The pattern is necessary, not itself excluded. The n4 calibration has even row count and all involutive K_v, so it does not contradict the parity boundary.

## 8. B6 — FULL converse conditions1–4, with all omitted-realization dangers handled

LF158–175.

Necessity follows from the actual-row constructions above. For sufficiency, begin with the four PRINTED conditions, not merely the endpoint polynomial or marginal degrees.

K_v permutations fixing v make T a bijection on distinct arcs. B={(v,f(v))} has n distinct arcs since f(v)≠v and tails are distinct, irrespective of injectivity of f. Condition2 says B,T B,...,T^(n-2)B are disjoint and cover the entire arc set. Apply the bijection T: T B,...,T^(n-1)B are another disjoint cover. The shared middle layers1,...,n-2 leave the unique complement B, so

`T^(n-1)B=B`.

Thus T^(n-1) bijects the n first arcs and induces an endpoint permutation. Because every T step glues the head to the next tail, the n-1-arc segment beginning at(s,f(s)) is one walk starting at s. Condition3, which is NOT deduced from the arc conditions, makes its n vertices all distinct; it is a Hamilton row on X and its endpoint differs from s.

For each v, the unique preimage of(v,f(v)) is(p(v),v), by K_v(p(v))=f(v) and injectivity of K_v. Moreover the set of last arcs is T^(n-2)B=T^(-1)B. Therefore the prescribed p(v) really is the penultimate vertex of the unique row ending at v, and f(v) really its start-successor. These are actual boundary functions, not independently chosen data surviving an invalid realization step.

Every other nonboundary turn occurs between consecutive arcs inside exactly one distinguished Hamilton segment. Summing K_v counts all these actual internal turns, the n artificial v diagonals and the n boundary turns GF, precisely as in Section3. Hence the PRINTED integer Gamma=sum K_v-I-GF is the ACTUAL distance-two event-count matrix.

Condition4's ENTRYWISE0≤Gamma≤J-I is exactly noncollision of those linear distance-two events: no diagonal pair and at most one of each ordered distinct outer pair. Its total is automatically n²-n-n=n(n-2), because sum K_v has total n²,I has n and GF has n. Thus these are exactly the required n(n-2) distinct distance-two events. The same layer cover gives every adjacency arc once. We have constructed n actual row permutations satisfying Tuscan-2, proving the FULL converse.

In particular Hamilton segments are not supplied merely by arc periods or a degree-feasible M. The separate condition3 prevents repeated original vertices in an arc trail, and cannot be silently dropped. Neither f/p bijectivity, regular M, Latin middle columns, source-group symmetry, independent row reversal nor a finite search cap was used.

## 9. Exact disposition, context exclusions and remaining primary gap

**New load-bearing identities NOT_RECONSTRUCTED: NONE.** Every191-LF theorem component in the assignment has a written reconstruction above: no-fixed-point endpoint bijection, genuine K_v completion and p=f boundary, multiplicity-aware matrix identity, full marginal degrees, all n4 events and K_v entries, complete T-cycle/determinant/trace correspondence, exact sign exponent, both split-graph component types, actual four-symbol pattern and the four-condition iff.

This is a structural/obstruction INTERFACE, not a tuple satisfying it at n11. No eleven-by-eleven table or contradiction covering noninvolutive local permutations is provided. At n11 a genuine solution must simultaneously realize the exact boundary coupling, arc layers, Hamilton11 segments, distance-two noncollisions and at least one noninvolutive K_v. Theorem3 does not exclude that required regime.

The S4 asymmetry/canonicalization manuscript remains UNREVIEWED candidate context and was not used as a premise. Its22-form or automorphism statements are not promoted by this gate. The source's bounded Anderson/source-status observations and novelty history are likewise not independently authenticated by this combinatorial reconstruction. Unrelated NL242 parent assertions were read for packet coverage only.

The registered unrestricted Tuscan-2(11) target remains OPEN at its actual source/import boundary. Parent full-body disposition and stronger formal/kernel/human/cross-vendor/configured-family/executable/novelty gates stay separate. Original v9/v10/HOLD, cutoff/deadline and all immutable histories remain unchanged; no scientific GO, execution, full-target acceptance or new primary cutover follows.
