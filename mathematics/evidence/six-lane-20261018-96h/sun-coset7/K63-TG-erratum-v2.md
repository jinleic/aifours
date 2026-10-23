# K63-TG-erratum-v2: Theorem K63-CLIQUE needs the full C-clique hypothesis (statement correction)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:03:18-0700.
- **Overlays:** `K63-TG-v1.md` (sha256 3e6a7cf604027a60f5e0b055c5d203cc0c167e08ca59ac81c36fc3a943ebc071) and `K63-TG-erratum-v1.md` (sha256 1dbcac91c17af170c752efd569a5bdbc37047cab852819a832029aa574fe0bdf); both frozen.
- **Source of the finding:** parent full read (MAJOR, hypothesis gap), received by IRC before this file was created.

## E3: hypothesis of Theorem K63-CLIQUE
**Defect.** The statement (also as corrected by E1) assumes only the star condition alpha_vc = alpha*_vc = 3 for
c in C \ {v}, but section 2 (i) applies Lemma TG to every triple {a, b, c} in C \ {v} using alpha_xy = 3 on the
edges *inside* the triple: it computes I_xy = 18 r_x r_y and derives 3 | tau and tau <= 9 from those values. These
are not implied by the star condition; with other inner values tau could be larger, divisible by 5 (relevant when v
carries the 5-marker) or by a prime of w_v, and the bound 1/6 would fail.

**Corrected statement (replaces Theorem K63-CLIQUE and its E1 form).** *There is no K6.3 configuration in which
alpha_ab = alpha*_ab = 3 for all distinct a, b in C. Proof: choose v in C \ {i*} (any C-vertex if no C-vertex
has e >= 2); then gcd(r_v, 6) = 1 whenever the 3-marker is not on v, and since at most one vertex carries the
3-marker and |C| = 6, such a v exists; apply section 2 (i)-(v) at v.* With the full clique hypothesis every edge
used in (i) has alpha = 3, so the computation there is valid as written (including triples containing i* or a
5-marked vertex: tau in {3, 6, 9} and gcd(n_v, L tau) = 6 because r_v is prime to 6, to tau and to the other
cofactors). Steps (ii)-(v) use only the row of v and are unchanged.

This still excludes all three canonical patterns of `evidence/probe-v14-exact-K63-r1` (all C-C entries are 3 in
alpha and alpha*). Lemma TG itself (section 1) is unchanged. No stronger star statement is claimed.
