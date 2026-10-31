# The 68-conflict triangle-code trade bound is sharp

**Status: WRITTEN corollary, conditional on the pinned exact neighbor-fiber counts; scientific review pending.** The lower bound in `frontier-20261028-triangle-code-trade-barrier-v1.md` SHA-256 `34b647fe99c3b03bb15553074e44c7154716ec40d0368f5078aab2dda4856e8b` is attained. Take any q=8 word whose only nonzero triangle syndrome is factor 1, the triangle `123`. It conflicts with **exactly 68** old codewords.

The previous packet proves that its three disjoint neighbor fibers at vertices `1,2,3` contribute `4+32+32=68` conflicts. There are no conflicts at another vertex `v`: all triangle parities incident with `v` are zero in the new word, so any old codeword matching it on `N(v)` must match its three factor bits at `v` as well. Hence those three fibers are the entire conflict neighborhood in `W0`.

The syndrome vector with only bit 1 set is attainable, for example by flipping the factor-1 bit at vertex 1 of the all-zero ambient word. The exact generator/projection receipt SHA-256 `09165f77dc480be2463290cb532da5d8fed04a366404f86a3edb6327af1156a7` and independent factorwise receipt SHA-256 `9000c1afc5dc4c9cb0986b15596d23ff8120b56edb0831709be663757e950e5f` pin the 4/32/32 fiber sizes. This sharpness concerns a **single new word's** conflicts; it does not construct a larger fixed-point set or a strict entropy-gap law.
