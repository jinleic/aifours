# A failed unrestricted lower-branch lemma: every maximum-matching packet family can miss identity

Actual returned clock before exclusive creation: **2026-10-24T05:07:26-0700 PDT**. Author MathOlson-2, math-2. This is a COMPLETE WRITTEN ROUTE-FAILURE ARGUMENT, not a lower-residual solution, an Olson counterexample, a novelty claim or a newly accepted candidate. No program, arithmetic interpreter, finite search, enumeration, solver, compilation, scientific checker, old job, CLI or nested agent was used. It has not received a separate fresh review or parent acceptance.

The exact route, informal-before-freeze chronology, stronger trial lemma and retained actual residual are frozen in `selection-lower-matching-packet-lift-v1.md`. The actual parent v16 disposition was read at independently observed SHA256 `0189f2186aa54e486736db167235eb78ca3ee184e6d1628f8ecb25a0ce57aa8c`. Its critical matching>=p-2 theorem is WRITTEN_SUPPORTED ONLY; the entire lower branch<=p-3 stays open. The present manuscript does not repeat that theorem or replace the actual remainder by a necessary normal form.

## 1. Exactly the global lemma that fails

The attempted stronger lifting lemma L_MAX was:

> Every actual zero-free singleton-gap word in D_(2p), with N=4p-1, R=p+1 rotations, F=3p-2 reflections and raw possible-switch matching number at most p-3, has an identity2p selection in a family built from SOME MAXIMUM raw matching E: choose exactly one reflection endpoint from EVERY edge of E; choose or omit its actual internal rotation independently; choose any free rotations; and choose any actual unmatched reflection filler set giving total2p.

All internal statuses, including a status with a zero switch, are allowed. All rotation counts and every filler choice are quantified. No midpoint factor is an actual selected occurrence. Selecting one endpoint from every maximum-matching edge is an additional restriction, not an equivalent reformulation of every possible identity subword.

L_MAX is stronger than its version restricted to the actual OLD/REF/GS/DS3-avoiding residual. If true it would give a lower-branch selector without using those failures. **The construction below disproves L_MAX for every prime p>=11**, even with a UNIQUE maximum matching. Thus changing the maximum matching, an activation tuple, the rotation count, the filler or the cyclic cut cannot repair THIS stronger mechanism.

This does NOT disprove the residual-only variant, because these particular words have explicit reflection-only solutions. That distinction is part of the conclusion, not a caveat to be removed later.

## 2. Literal group, actual word and all counts

Use

    D_(2p)={(y,e):y in F_p,e in{+1,-1}},
    (y,e)(y',e')=(y+e*y',e*e'),
    rho_x=(x,+1), sigma_y=(y,-1).

Fix ANY prime p>=11 and ANY v in F_p with v!=0. Put

    t=p-3,  n=p+4.

In particular t is even and t>=8. Every displayed occurrence below is an actual word position. Define actual three-letter blocks

    E1 = sigma0 rho_v sigma0,
    E2 = sigma0 rho_(-v) sigma_(2v),
    E3 = sigma0 rho_v sigma0,
    E4 = sigma_v rho_v sigma_v,
    Ei = sigma0 rho_v sigma0,       5<=i<=t.

Set, by CONCATENATION in the shown order,

    w = E1 rho_(-v) E2 rho_v E3 rho_(-v) E4 rho_v E5 E6 ... Et
          sigma0^n.                                      (1)

No commutative product is meant by this display. There are exactly t internal rotations and four further rotations, so

    R=t+4=p+1.

There are2t block reflections and n final reflections, so

    F=2t+n=3p-2,
    N=3t+4+n=4p-1.

Every actual rotation has value v or−v and is nonzero. Every rotation sits in its own reflection gap: each block has one internal rotation and the four further rotations occupy four different gaps between consecutive blocks. All other actual reflection gaps, including the cyclic boundary, are empty. Thus (1) is a genuine zero-free singleton-gap word at the correct target length, not the old one-short4p-2 diagnostic.

The opposite-pair rotation alphabet here is a permissible concrete witness for falsifying a universally quantified stronger lemma. It is NOT imposed as a model of all words in the actual lower residual.

## 3. Actual raw graph: one P10, isolated P2 components and n isolates

The raw possible-switch graph has the ACTUAL reflection occurrences as cyclically ordered vertices. An adjacent edge is present iff its reflection values differ OR the actual intervening gap contains a nonzero rotation.

Among the first ten reflection vertices, namely those of E1,...,E5, EVERY consecutive edge is present:

* the five internal block gaps contain nonzero rotations;
* the four interblock gaps E1–E2, E2–E3, E3–E4, E4–E5 contain the four additional nonzero rotations.

These ten vertices form one path P10. The following gap after E5 is empty between sigma0 and sigma0, so it is absent. For every i>=6 the two endpoints of Ei are joined by its internal nonzero rotation gap, giving a P2 component. Every gap between these later blocks is empty with equal endpoint values0 and is absent.

The final n copies of sigma0 are all isolated vertices. Their mutual gaps, the gap from Et to the first such vertex, and the cyclic gap from the last such vertex to the first vertex of E1 are empty and have equal endpoint value0. There is no extra cyclic connecting edge. Consequently the COMPLETE raw graph is

    P10  disjoint union (t-5) copies of P2
         disjoint union n isolated vertices.             (2)

A path on an even number2a of vertices has matching number a and a UNIQUE perfect matching: its endpoint must be matched with its only neighbor, after which the same argument inducts on the remaining even path. Each P2 has the same property. Therefore (2) has matching number

    5+(t-5)=t=p-3,

and its UNIQUE maximum matching is precisely the t named internal reflection pairs E1,...,Et. Every global maximum matching must be maximum on each independent component, so none is hidden by a different distribution among components.

This verifies an actual entire lower raw-matching instance. It is not a scalar matching-number system being asserted realizable without a word.

## 4. Every actual maximum-matching packet selection

Because the maximum matching is unique, consider ALL families based on E={E1,...,Et}. Each block supplies exactly ONE of its two ACTUAL reflection endpoints, and its actual internal rotation is selected or not.

Call E2 the special block. Let

    e in{0,1} be the special internal-rotation status,
    j in{0,...,t-1} be the number of selected normal internal rotations,
    c=j+e be the selected internal-rotation count.

Choose ANY subset A of the four actual free rotations, with a=|A| in{0,1,2,3,4}. Choose ANY subset Q of the n final unmatched sigma0 occurrences, with q=|Q|. A target-length selection has

    k=c+a actual rotations,
    t+q actual reflections,
    t+k+q=2p,

so necessarily

    q=2p-t-k=p+3-k.                                      (3)

Since0<=k<=t+4=p+1, all even k give2<=q<=p+3<n+1, and such actual fillers exist. If k is odd, t+q=2p-k is odd, so the product is a reflection and cannot be identity. It remains to check EVERY even k, not merely a preferred all-rotation or two-rotation branch. For even k, q is even because p+3 is even.

The positions in Q are all after every block and every free rotation; choosing different positions in Q never changes the order of any selected earlier occurrence. All count and parity statements refer to actual selected positions, not formal identity insertions.

## 5. Local ordered products and their virtual midpoints

For a normal block sigma_h rho_v sigma_h, let eta denote its internal-rotation status. Choosing its left or right actual endpoint gives the ACTUAL local selected products

    sigma_h rho_(eta*v)=sigma_(h-eta*v),
    rho_(eta*v) sigma_h=sigma_(h+eta*v).                   (4)

With eta0 both products are sigma_h; with eta1 they are sigma_(h-v) and sigma_(h+v). Each option always selects one reflection and eta rotations. Grouping factors inside this block is legitimate; no outside selected factors are permuted.

For E2=sigma0 rho_(-v) sigma_(2v), the two actual local products are

    sigma0 rho_(-e*v)=sigma_(e*v),
    rho_(-e*v) sigma_(2v)=sigma_(2v-e*v).                  (5)

Their midpoint is v. With e0 the centered offsets are−v,+v; with e1 BOTH local products equal sigma_v and the switch vanishes, although the rotation remains an ACTUAL selected occurrence. Thus the total number of nonzero centered switches, INCLUDING all zero-status possibilities correctly, is

    s=j+(1-e).                                          (6)

Every nonzero centered switch contributes either−v or+v to its local reflection label. Its external reflection-prefix sign may reverse that choice pair, but the SET{−v,+v} is unchanged. The choices for different blocks are independent because their spans and actual positions are disjoint.

The midpoint labels of E1,...,Et are

    h1=0, h2=v, h3=0, h4=v, h5=...=ht=0.

Their ordered even reflection product has coordinate

    h1-h2+h3-h4+...-ht = -2v.                            (7)

This midpoint product is only an algebraic center of the actual option set. It is never called an actual selected subword or transported as an identity witness.

## 6. Every free contribution and the COMPLETE actual option set

The free rotation after Ei, for i=1,2,3,4, has value(-1)^i v in (1). Exactly i block reflections precede it in EVERY packet choice, and no Q occurrence precedes it. Therefore its actual coordinate contribution is

    (-1)^i * [(-1)^i v] = v.                             (8)

This is derived by the displayed semidirect group law and the actual prefix parity. It is NOT commuting a rotation through selected reflections. Any a chosen free rotations contribute exactly a*v.

For even k the q final selected reflections are all sigma0 and q is even, so their ordered product is identity. Combining (4)–(8), the COMPLETE coordinate set for all endpoint choices at the fixed statuses/A/Q is exactly

    -2v + a*v + sum_(l=1)^s {-v,+v}
       = {v*(a-2-s+2r): r=0,...,s}.                     (9)

No possible endpoint combination is omitted: r counts how many independent centered choices contribute+v after their fixed prefix sign is absorbed. Conversely every r in that interval is realizable by choosing that many of the actual nonzero-switch endpoints. Zero switches introduce duplicate products, not new coordinates or extra selected positions.

The endpoint identity question is therefore settled exactly, not by a necessary sign condition alone.

## 7. The parity/range obstruction holds for ALL statuses and counts

Because k=c+a=j+e+a is even,

    a == c (mod2).

Equation(6) gives s-c=1-2e, an odd integer. Thus for EVERY r the ordinary integer

    L=a-2-s+2r

is ODD. In particular L is not the integer0. Also0<=a<=4 and0<=s<=t, so

    |L| <= |a-2|+|-s+2r| <= 2+s <= 2+t=p-1 < p.

A nonzero ordinary integer of absolute value less than p is nonzero modulo p. Since v!=0 in F_p, every coordinate in(9) is nonzero. Therefore no even-k packet selection is identity. Odd-k selections already failed the reflection-parity requirement.

This proves failure for ALL activation tuples, including those that deactivate normal switches or collapse the special switch; ALL four-free-rotation subsets; ALL actual filler subsets of the target size; and ALL internal endpoint choices. The maximum matching itself is unique. Hence **NO maximum-matching packet family supplies identity2p in(1)**.

Allowing an actual cyclic cut does not repair this result. Family membership is a condition on the same named actual occurrences. A cyclic cut only cyclically permutes their ordered selected factors, and a product is identity after such a cut iff the original selected product is identity, by conjugation. No arbitrary nonidentity products are asserted equal under that operation.

## 8. The word nevertheless has an explicit actual identity2p selection

The actual number of sigma0 occurrences in(1) is

    2 from E1 +1 from E2 +2 from E3 +0 from E4
      +2(t-4) from E5,...,Et +n
       =2t+p+1=3p-5.

For p>=11 this exceeds2p. Select the first2p ACTUAL sigma0 occurrences in their ORIGINAL increasing order and no rotations or other reflections. The selected product is sigma0^(2p)=1. These are exactly2p genuine positions. In particular the word is explicitly REF-covered.

This witness does not belong to a one-endpoint-from-E family: E4 has no sigma0 endpoint at all, so that witness selects ZERO endpoints of E4. The failed constraint is therefore substantive. It cannot be removed by regarding the midpoint as an actual selected endpoint.

The construction is **NOT an Olson counterexample** and **NOT a realization of the actual residual**, which retains REF failure and other old-caller failures. No converse to any old normal-form or scalar necessary system has been used.

## 9. Exact failed bridge and requested PARK

**L_MAX is false as a whole-word universal mechanism.** The counterexample quantifies over the entire maximum-matching family at all mixed counts and uses an actual correct-length word with a unique matching, rather than an abstract center/exception-set model. It explains precisely why the critical singleton-missing-coordinate coherence proof cannot simply be advertised as unrestricted lower-branch packet coverage.

For a general matching t=p-2-d, the exact centered set T_E may miss up to d+1 coordinates. At d=1, already two omitted coordinates can accommodate all permitted cardinality offsets; equations(6)–(9) give an actual realization of this obstruction, including the zero-switch statuses. This is a route obstruction, not a proof that all broader packet methods fail.

**The actual residual-only global bridge L_RES remains UNPROVED:** for EVERY actual lower-branch word satisfying ALL inherited OLD/REF/SEL/IPGEN/GS/DS3 failures, show that some maximum-matching family has identity, or supply a separately proved actual selector allowed to omit/both-select matched endpoints. The word(1) does not refute L_RES, because it fails its REF-avoidance antecedent. No actual residual witness, emptiness/nonemptiness proof or full lower-branch solution is claimed.

I therefore PARK this ONE bounded lower-branch mechanism under Main's explicit instruction to name its exact failed global lemma rather than issue another necessary-profile manuscript. The previously accepted critical theorem remains unchanged. The full lower branch, full R=p+1 band, unrestricted prime-dihedral theorem and all-finite-group Olson problem remain open at their exact source/trust boundaries. No scientific execution or permission to restart held jobs follows. The present route-failure argument itself is author-written and awaits any actual parent/fresh-review disposition; it is not already an accepted scientific result or discovery.
