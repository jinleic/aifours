# Unrestricted twelve-symbol square-root/phase representation v1

Clock observed before creation: **2026-10-23T15:44:17-0700**. Status **CANDIDATE / WRITTEN ONLY / PARTIAL / NOVELTY_UNCLEAR**. This is a new global representation, not a larger radius of the closed Etzion neighborhood, and no scientific execution or new assay is proposed here.

The full target remains an arbitrary Tuscan-2 square of order11. The representation below retains the noncircular target and all possible second/penultimate multiplicities. A known ordinary directed-six-cycle decomposition is used only as a new primary comparison/input; it is not silently equated to a Tuscan-2 construction.

## 1. New primary input and its exact limitation

Andrea Burgess and Mateja Šajna, *On the directed Oberwolfach Problem with equal cycle lengths*, Electronic Journal of Combinatorics21(1)(2014),#P1.15, [primary PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i1p15/pdf), Lemma18, explicitly constructs a resolvable directed6-cycle decomposition of `K12*`.

Retained source: `sources/burgess-sajna2014.pdf`, SHA-256 **`4986ba81a7632f328da1046e6b8508c43d78f90e55ec54e7b9c15ba534d98eab`**. The actual p7andp8 images were opened for all11 displayed classes and the orientation of class4; the definitions, Theorem3 and Lemma18 body were read. This is not a recent open statement: it is a **solved classical component**, and no discovery of its existence is claimed.

Each of its11 resolution classes is a permutation Q_j with two disjoint directed6-cycles. It does NOT follow that one can choose Hamilton12-cycle square roots P_j whose arcs also decompose `K12*`. That simultaneous root condition is the missing ingredient. The published input itself fails it by the exact two-pair certificate in §5 below.

## 2. Exact unrestricted representation, not only the perfect-circular subcase

Let Ω be a12-symbol set. Any Tuscan-2(11) array, after adjoining the extra root t and closing rows, gives11 Hamilton successor permutations P_j such that every ordered distinct arc occurs once. Put

`Q_j=P_j²`.

Each Q_j has exactly two directed6-cycles. The sum of its directed-arc multiplicities is the circular distance2 multiplicity array μ. Its two-path centers depend on the selected P_j, not merely on μ: if `Q_j(a)=b`, the center is `P_j(a)`.

Conversely, choose **any**11 permutations Q_j of cycle type6+6, choose a Hamilton12-cycle square root P_j of each, require that the P_j cover all ordered distinct arcs exactly once, and require a root t to belong to the exact fault intersection in `unrestricted-defect-orbit-candidate-v1.md` (with its operative endpoint addendum). Cutting at t then gives the full unrestricted T2(11) array.

Thus this is an exact representation of the primary target. **The Q_j are NOT required to be arc-disjoint or to form a resolvable design.** In the general target, repeated Q-arcs are permitted precisely subject to the good-root fault condition; their centers must be retained.

The special case in which the Q_j themselves cover every arc once has no circular distance2 fault and gives every root good. For a cut T2 array this is exactly M=E, not a condition one may impose without loss of generality. The new Burgess–Šajna input concerns only this stronger sufficient subcase.

## 3. All Hamilton square roots of a6+6 factor

Fix oriented cycles

`U=(u_0,...,u_5)`, `V=(v_0,...,v_5)`

of Q, so `Q(u_i)=u_(i+1)` and `Q(v_i)=v_(i+1)`, indices modulo6.

**Lemma1.** The Hamilton12-cycle square roots of Q are EXACTLY the following six permutations, parameterized by `s∈Z6`:

`P_s(u_i)=v_(i+s)`,

`P_s(v_j)=u_(j−s+1)`.

*Proof.* Every square root P commutes with Q. A Hamilton P cannot preserve each of the two Q-orbits, so it interchanges them. If `P(u_0)=v_s`, commutation forces `P(u_i)=v_(i+s)`. The equation `P²(u_i)=u_(i+1)` forces the second formula. Conversely those formulas square to Q and give the single interleaving cycle

`u_0,v_s,u_1,v_(s+1),...,u_5,v_(s+5)`.

They exhaust all possibilities; reversing one Q-cycle is not an additional allowed root of the same oriented Q. ∎

This converts each factor to one phase choice, but does not make the global condition automatic. Even at this fixed N, independently selecting six possibilities per class is not evidence of a globally compatible selection.

## 4. Necessary constraints on ALL unrestricted factor families

Let A_j,B_j be the two6-element Q_j-orbits. Every P_j alternates between them. Hence an arc u→v is available in classj only if u and v lie in different blocks.

**Lemma2 (scarce-pair condition).** Every unordered pair `{u,v}` must be separated by at least two of the11 partitions `{A_j,B_j}`.

*Proof.* Both directed arcs u→v and v→u must be covered. A single Hamilton P_j cannot contain both because that would be a2-cycle. Classes in which the endpoints share a Q-orbit supply neither. ∎

Equivalently, encoding each vertex by its0/1 side in the11 balanced partitions gives twelve binary column words of length11 with pairwise Hamming distance at least2. This is only necessary; arbitrary such binary words do not supply cycle orientations or phases.

More generally, for every nonempty proper S⊂Ω put `a_j=|S∩A_j|`, `b_j=|S∩B_j|`.

**Lemma3 (unrestricted subset capacity).** Any phase-compatible arc cover must satisfy

`sum_j min(|S|−1, 2 min(a_j,b_j)) ≥ |S|(|S|−1)`.

*Proof.* Each internal selected arc crosses the two blocks, so at most min(a_j,b_j) go in each direction. Also a Hamilton12-cycle has no directed cycle wholly inside a proper S, so its internal arcs form disjoint paths and number at most |S|−1. Sum these bounds over the11 P_j, whose internal arcs must cover all |S|(|S|−1) ordered pairs. ∎

At |S|=2 this recovers Lemma2. At |S|=3 it says at least three class partitions must split the triple. These constraints apply to the **entire unrestricted factor representation**, whether the Q-arcs repeat or not; they do not inherit a group/Latin-column assumption.

A second constraint is phase consistency. If a pair is available in exactly two classes, each of those classes must supply one of its orientations. Therefore the phase of either class must belong to the two offsets that realize one of these orientations. Several scarce pairs incident to one class can have incompatible phase requirements even though all pair and subset counts look feasible.

## 5. Exact phase-conflict certificate for the published Lemma18 input

The source labels vertices `x_0,...,x_5,y_0,...,y_5` and classes `R_1,...,R_11`. Only its two6-cycle block memberships are needed to establish the following complete availability table:

|Class|x1 andx4|x2 andx3|
|---:|---|---|
|1|same block|same block|
|2|same block|same block|
|3|same block|same block|
|4|opposite blocks|opposite blocks|
|5|same block|same block|
|6|opposite blocks|same block|
|7|same block|same block|
|8|same block|same block|
|9|same block|opposite blocks|
|10|same block|same block|
|11|same block|same block|

This was read directly from all11 source classes on the opened p7/p8 images; no computer-generated availability census is claimed. In particular:

- the only classes able to cover x1↔x4 are4and6;
- the only classes able to cover x2↔x3 are4and9.

A Hamilton root in one class cannot cover both directions of either pair. Thus **class4 must cover one orientation of BOTH pairs**.

The exact source orientation of class4 is

`U=(x0,y5,x1,y3,x2,y4)`,

`V=(y0,x5,y1,x3,y2,x4)`.

Use the phase convention of Lemma1.

For x1=u2 and x4=v5:

- `P_s(x1)=x4` requires `2+s=5 mod6`, so s=3;
- `P_s(x4)=x1` requires `5−s+1=2 mod6`, so s=4.

Hence the first scarce pair forces **s∈{3,4}**.

For x2=u4 and x3=v3:

- `P_s(x2)=x3` requires `4+s=3 mod6`, so s=5;
- `P_s(x3)=x2` requires `3−s+1=4 mod6`, so s=0.

Hence the second forces **s∈{5,0}**. The two phase sets are disjoint. There is no simultaneous Hamilton square-root arc cover of the published11-factor decomposition. ∎

This is a two-pair symbolic contradiction covering all six class4 phases and therefore all choices in the other ten classes. It is not a failed6^11 search, an executable enumeration or an assertion that the source's ordinary directed6-cycle decomposition does not exist.

As a positive calibration of the root formula itself, phase0 gives the explicit Hamilton interleaving `u0,v0,u1,v1,...,u5,v5`, whose square is exactly the displayed class4. The obstruction arises only from the two simultaneous global coverage demands, not from a bogus claim that an individual factor has no square root.

## 6. Exact delta and remaining scientific obligation

The ordinary resolvable directed6-cycle component at12 is already solved. This packet supplies an exact phase-compatibility layer that a Tuscan construction must satisfy and an explicit certificate that the first accessible published component cannot simply be square-rooted into a construction. The global subset-capacity and scarce-phase constraints are necessary for arbitrary factor families, not only this input.

Neither the representation nor this one input obstruction settles T2(11). A positive still needs compatible Q factors, their actual Hamilton roots and a nonempty good-root intersection (or an ordinary Q arc cover as a stronger sufficient case). A negative still needs an obstruction for EVERY allowed factor family, including those with Q-arc repetitions compatible with one good root. No convenience restriction M=E may be silently adopted.

This is the lane's new unrestricted mathematical line, not a radius increment of the old source. All earlier scripts remain unexecuted; the closed deletion/radius1 requests are supersededHOLD, the encoder is PREPARE/not admitted, and this packet proposes no new scientific run. Its written claims require actual separate and parent reconstruction. Novelty and significance remain unestablished; no theorem/discovery count is asserted.
