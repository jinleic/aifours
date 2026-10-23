# Parent derivation: rotation rigidity with at most two odd constant reflection blocks

Recorded 2026-10-18T02:58:11-07:00. Candidate inputs `proof-ROT-lowodd-v1.md` SHA `8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785` and `notes-GRX-v1.md` SHA `afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30`, in the [review snapshot](../olson-rotation-lowodd-review-v1/manifest.json). This is independent parent verification of the written subclass argument, not acceptance of full ROT, INV* or ordered Olson.

## GRX and merging

For each selected reflection count c_i, the sign before the next rotation block changes iff c_i is odd. Thus c_i=f_i mod2, with independently available counts f_i,f_i+2,...,l_i-[(l_i-f_i) odd]. Sums of integer intervals give every even C between Phi and C_max; this is not a subset-sum approximation. The signed rotations contribute a submultiset sum of X^z. Reflection contribution telescopes to -T(z), since sum theta_i=0. Hence identity and total length2p are exactly the GRX condition. Normalize z_1=+1 when asserting the literal product coordinate; for the other global sign the coordinate is its negative and the zero condition is unchanged. Empty rotation blocks and nonmaximal equal adjacent pieces do not change this proof. Cyclically rotating an ordered selection conjugates its product, preserving identity.

Merging an even reflection block sets the two adjacent zone signs equal. Its removal does not change delta/Phi; its even length transferred to the next constant block preserves parity and total F. The two associated theta terms telescope into the new one. Every reduced GRX witness therefore lifts to an original one; avoidance descends, not conversely. Repeatedly remove even blocks while retaining the displayed representation even if it stops being maximal. Finish at o odd blocks, or one even block if o=0.

## Elementary sequence lemmas

In a zero-sum-free sequence of length n-1 over C_n, every ordering has exactly all n-1 nonzero partial sums. Swapping positions1 and2 changes only the first partial sum, so the two terms coincide. Arbitrary occurrences can be placed there: all terms equal a generator. For length2p-2 with all terms in {1}×C_p, the p-1 even-indexed partial sums exhaust the nonzero parity-zero subgroup elements. Swapping positions2 and3 changes only the even partial sum at2, so the two terms coincide. All terms equal g=(1,c); c=0 would give a zero pair, hence c≠0. Primality makes g a generator. This is not a generic inverse theorem for arbitrary length2p-2 sequences.

## K1

With one constant reflection block, F≤2p-1 and the two-EGZ argument gives R≤3p-2. Write R=2p-1+s,0≤s≤p-1. GRX's sole normalized sign pattern forbids zero-sums of even lengths in[s+1,2p]. For s>0 pack disjoint zero-sums of length≤s until total length s: while the total is≤s-1, at least2p terms remain; the next available zero-sum has length≤s, and the union has length≤2s-1<2p, so the exclusion prevents overshooting s. If s is odd, parity already contradicts this. Otherwise the2p-1-term remainder is zero-sum-free and equals g^(2p-1).

Each term h in the packed s-term block has odd coefficient a_h in[1,2p-1] relative to g. It can be cancelled with e_h=2p-a_h available g's, so b_h=1+e_h is even and≤s. Accumulate these lengths until first crossing s. The resulting forbidden zero-sum has length at most2s≤2p-2 and uses fewer than2p-1 g's. Hence s>0 is impossible. For s=0, the inverse lemma gives all R=2p-1 rotations equal a nonzero c, and F=2p-1. These known extremal words do avoid an identity2p-selection.

## K2

For two odd constant blocks, H=(F-2)/2≤p-1 and the EGZ bound imply even F in[p+1,2p]. Set t=(2p-F)/2,0≤t≤(p-1)/2. The all-plus GRX pattern forbids even zero-sums in[2t+2,2p]. Pack a zero-sum of length2t; as in K1, strict even growth and the upper bound4t-2≤2p-4 force exact termination. The remaining2p-2 terms are zero-sum-free, so equal g by the parity-restricted inverse lemma. At t=0 the packing loop is empty and this conclusion holds directly.

At most one packed term equals g, else2p copies yield the forbidden zero-sum. For every other h, its cancelling g-count e_h satisfies1≤e_h≤2t-1; all copies exist in the2p-2 remainder. For t=1, e_h=1, so h=-g. For t≥2, at least2t-1 such terms have total cancellation-length at least4t-2≥2t+2. The first even crossing of2t+2 has length≤4t≤2p-2 and uses at most4t-2<2p-2 copies of g. This contradicts the forbidden interval. Thus all rotation values lie in one nonzero±pair.

The final implication concerns **at most two odd maximal constant reflection blocks**, not at most two arbitrary reflection runs. PM* preserves the rotation multiset; K1 rules out o=0 and classifies o=1; K2 proves the o=2 claim. None of this forces constant reflection runs or handles o≥3.

## Independent finite aid

[RESULT.json](RESULT.json), SHA `09095f7736b18f97cbf949db22c3638fff0a40805724af20a481f5a0e7fba04f`:1,176 checks passed from pre-pinned parent source `grx_smoke_v1.py` (`f66b2e83a889d3d375408cf69b2883ff346542bcc1eaa2b364e8b92d76fe4f56`). A raw ordered-product dynamic program was compared with independently implemented GRX on1,152 deterministic random words,9 known-family words,9 cyclic shifts and6 nonmaximal-block representations. No worker code or native child. Tests at p=3 concern GRX only; the candidate ROT theorem starts at p=5. This finite aid is not a universal proof premise.

Codex's independent review has returned ACCEPT (`6fba60f7…8f12`). Claude's review remains pending at this note's creation. No full ROT or gate is inferred.
