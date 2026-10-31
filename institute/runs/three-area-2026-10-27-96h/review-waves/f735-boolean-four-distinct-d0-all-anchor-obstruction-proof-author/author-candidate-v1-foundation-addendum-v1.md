# Prospective foundation addendum: the normalized g pattern and local H

**GENERAL-AUTHOR WRITTEN ADDENDUM; NOT A PARENT DISPOSITION.** This is new work after the separate frozen f735-s1 supplement was dispatched and completely read. The original f735 candidate and its then-correct missing-display boundary remain unchanged and are not backdated. The supplement now supplies a general normalized five-span g source and the explicit local-H definition. At their exact imported scope, the g normalization needed for the original residue bridge is recovered, and the local H for the two stated local examples is checkable. No child scientific execution was run.

To avoid confusing symbols, call the scalar counting invariant `H_loc` and reserve `H_rad` for the radical-lift plane in the four-distinct-D0 argument.

## 1. Precise local-H definition and block reconstruction

Supplement S3, selected original f483 LF74, defines `H_loc` as **the number of blocks with U1=0 having a single |U0|=4 peak**. It is not a dimension, not the radical plane, and not an unspecified historical class-table label. Its vanishing is an actual-caller/local-form hypothesis, not an implication from the words `rank two` or from a Fourier cap alone.

For completeness, the local classification in supplement S4 LF193–243 follows directly at the specified ternary interface. At a block with `U1=0`, write the four ternary entries of u in the two pairs on which `chi_1` is respectively +1 and -1. The pair sums are equal. A support of size 1 or 3 is impossible: in one pair the sum of two nonzero signs is even, while in the other the sum of one sign is odd. For support 0 the Walsh spectrum is zero. For support 2, character orthogonality gives exactly two nonzero Fourier entries, each of magnitude 2. For support 4, the four signs `u chi_1` sum to zero and therefore form a nonconstant character up to sign on `F_2^2`; u itself is a character up to sign. Its spectrum is a single magnitude-4 peak at U0, U2, or U3, not U1. Thus H_loc=0 excludes precisely the U0 peak.

At the common fixed a,g of supplement S2/S3, this gives the following actual possibilities, with all signs independently understood as the one chosen physical block:

* On S, `U1=3a` with `a=+/-1`, `g=+/-1`. Since U1 has magnitude 3, u has three nonzeros, each equal to `a chi_1`, and one zero at w*. Hence `x=U0=-a chi_1(w*)` is a sign, `g=x chi_2(w*)`, and `y=U3=-a g x`.
* On the two F blocks, `g=+4`, so `x=y=0` and `u=chi_2`.
* On D, `|g|=2`: the second nonzero Fourier coordinate is either U0 or U3. Thus `D0: (x,y)=(+/-2,0)` or `D3: (x,y)=(0,+/-2)`.
* On Z, `g=0`: the block is `Z0: (0,0)`, `Z2: (+/-2,+/-2)`, or `Z4: (0,+/-4)`. The two Z2 signs may be written `(2 epsilon,2 delta epsilon)` with signs epsilon,delta. A `(x,y)=(+/-4,0)` block would instead be counted by H_loc and is forbidden.

The common inverse `4u=x+3a chi_1+g chi_2+y chi_3` realizes exactly these patterns. For example, on D0 and D3 it gives, respectively, `(epsilon+(g/2)chi_2)/2` and `chi_2((g/2)+zeta chi_1)/2`; on Z2 and Z4 it gives `epsilon(1+delta chi_3)/2` and `kappa chi_3`. These are ternary. Thus this is a local classification, not an assertion that independently chosen global spectra belong to one u.

Let `d=|D0|`, `p=|Z2|`, and `z=|Z4|`. There are 16 graph blocks, 2 F blocks, 22 D blocks, and 24 Z blocks. Their actual support sizes yield `116=16*3+2*4+22*2+2p+4z=100+2p+4z`, i.e. `p+2z=8`. The U0 energy gives `56=16+4d+4p`, i.e. `d+p=10`. The U3-zero count is `2+d+(24-p-z)=20+3z` after these equations. Requiring 23 zeros gives exactly

    D0=4, D3=18, Z2=6, Z4=1, Z0=17.

Conversely, within the displayed local patterns these counts give support 116, `sum x^2=56`, `sum y^2=128`, 23 y-zeros and H_loc=0. This is the explicit count converse, not a converse for original balance, amplitude caps, rank/eight-zero, or undisplayed historical atom conditions.

The original f735 packet's explicit x_* and sheared x' have graph values +/-1, four mate values +/-2, six Z2 values +/-2, and all remaining x values zero. For either one, modulation by the **given** t changes signs only. Thus neither contains a magnitude-4 U0 value anywhere, and in particular neither has a U1=0 block with a |U0|=4 peak: `H_loc=0` by the recovered definition. This is a new written identification from their stated local arrays; it does not retroactively claim that any f710/f719/f727 finite run tested H_loc, nor does it turn either exhibited y into an all-U3-capped witness or a full original caller.

## 2. General physical g normalization, not a selected fixture

Supplement S2 LF7–16 states the following as a **necessary normalized interface for every caller in its named five-span scope**, not just for an illustrative choice of f or r. Write `h=(h_0,j)`, with `h_0 in F_2`, `j in F_2^2`, and `d=(d_0,d_1,d_2)`. Its E plane is d=0, the full blocks are h=0,1, and the four B-cosets are `d_b=1 XOR 3b_0 XOR 5b_1`, with `rho_b=(-1)^{1+b_0b_1}`. The general local data are

    g(h,0) = 4 on h=0,1, and -2 for the other six h;
    g(h,d_b)=rho_b(-2+3*1_S(h,d_b));
    g=0 on the other 24 blocks.                                  (1)

Set `ell=d_0+d_1+d_2` and identify the physical `b=(d_1,d_2)`. The four d_b are exactly the four ell=1 values, one for each b. On ell=0, b=0 is exactly d=0; since h=0,1 means j=0 with either h_0, the six remaining E blocks have j!=0. The other three ell=0 d-cosets have b!=0 and g=0. The admitted graph in S2 is `h_0=f(j,b)` and there is exactly one graph point in each physical h-mate pair. Therefore (1) is precisely the general formula used in the original candidate:

    g(1,f(j,b),j,b)=rho_b,
    g(1,1+f(j,b),j,b)=-2 rho_b,
    g(0,h_0,j,b)=1_{b=0}(4*1_{j=0}-2*1_{j!=0}).               (2)

No value here is inferred from the selected f725 fixture. The source gives the normalization at its named conditional interface; it does not assert that the original-coordinate balance remains at zero after its gauge changes. The carried t remains the specific transformed original-DC covector.

## 3. Full residue derivation and exact physical scope

For a physical frequency `(nu,s,beta,alpha)` in the original `(ell,h_0,j,b)` coordinates, (2) gives

    ghat(nu,s,beta,alpha)
      = (-1)^nu [1-2(-1)^s]
            sum_{j,b} (-1)^{q(b)+s f(j,b)+beta(j)+alpha(b)}
        + 1_{s=0}(12-16*1_{beta=0}),                           (3)

where `q(b)=1+b_0b_1`. The E term follows explicitly from

    sum_{h_0}(-1)^{s h_0}[4-2 sum_{j!=0}(-1)^{beta(j)}].

For s=0, the first term is a multiple of 8 because its j sum is zero or 4 and each two-bit Walsh coefficient of `(-1)^q` is +/-2; the E term is 4 modulo 8. For s=1 the E term is zero and the bent `f+q` condition gives the first term +/-12, also 4 modulo 8. Thus `ghat=4 (mod 8)` at all 64 frequencies. Since a is supported on the graph with values `(-1)^r`, bentness of the common r and r+f gives `ahat=+/-4`; hence `3 ahat+ghat=0 (mod 8)`. Supplement S5 LF31 independently states the same normalized four-fibre parity interface, but the computation here uses the explicit g pattern rather than its historical finite checks.

For the same physical inverse, at w=0 all three nontrivial characters are +1. If `J=#{c:u(c,0)!=0} mod 2`, ternarity gives `uhat(xi,0)=J (mod 2)` at every xi. Transforming the inverse and using the actual all-frequency U0 divisibility then yields

    yhat(xi) = 4J (mod 8)  for every xi.                         (4)

In particular J=1 supplies all 64 residues 4 modulo 8, not an amplitude bound. Multiplying the same x and y by the carried character t translates their spectra and leaves the fixed physical a,g unmodulated; it preserves (4), magnitudes, and the graph relation. The global linear radical coordinates used in the original candidate preserve all frequencies together and the physical b coordinate. At b=0 their radical lift and linear h-shift vanish, so the E formula is unchanged there; the actual h-mate direction is still carried. The original signed-array obstruction therefore applies to the actual four-distinct-D0 consumer **at its full named imports**, including H_loc=0, the adopted same-x location result, the actual normalized g interface, ternarity, all U0 divisibilities/caps, the specific balance t, J=1 and all U3 caps. This is a prospective source-foundation reconstruction, not a parent adoption of the theorem.

## 4. What is and is not closed

The supplement closes the earlier **display gap at this normalized source interface**: general g is now a complete-body adopted necessary normalization, and H_loc has an explicit selected-source definition. The earlier candidate accurately said those items were not displayed in its original frozen packet; that historical observation remains true. I do not derive the broader named caller's equivalence to the printed original problem, prove omitted atom/class-table statements, claim all normalizations preserve DC balance, or establish global five-span/six-span exclusion, a complementary V, an NL242 solution, novelty, or human/external-family/kernel verification. The signed-array theorem still has its own self-contained assumptions and does not require H_loc. The actual-caller theorem retains its same-object and imported-location boundaries and awaits parent independent disposition.

## 5. Supplement reading and pins

The original f735 packet was completely read and the original return was written before this separately frozen supplement. Before this supplement packet, I read its complete manifest, freeze receipt, final binding, prepared metadata, actual dispatch and all **22** listed controls through their endings, then delivered a direct SUPPLEMENT PREBODY ACK. The sole supplement packet was then read serially in raw windows of at most 20 LF through LF 219 and its ending, before research or comparison. Its actual coverage is complete S1 LF1–13, complete S2 LF1–38, **only** f483 original S3 LF39–80 and S4 LF191–243, and complete S5 LF1–51. No claim is made to have read the rest of f483. The parent-supplied whole-source SHA256 pins are:

    S1 a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef
    S2 443d0a1a94384e237076cb7974b49845e6fa52edf3ca83f161259e79a369de1e
    S3/S4 whole source a87070e93236c417f0b6d9c04ad6d9ebefd90342f6ce9a6e87a54d4e5d3dca36
    S3 selected bytes bb5c8ce088d9f0c67999079ad6abf4a69c040ebffb757888cd69bdfcdb2e9de2
    S4 selected bytes 4a7f7267c1605decc029d3694d46d20f18e07017d3cb52e427629986d0fd11e8
    S5 fc7169410a6540a6d63ea033720a90207fd49e89e4cc048d9eb208639eb65e5c

After the complete packet read, I directly hashed the supplement packet and metadata. SHA256: packet `52831db2b5af020c8b38bc50e2d8662b8f6b11e293d5c4bd8255d62bcc16d8ff`; manifest `80041d0505c186532ea50c8acbab72f39ac7a4e18dd243cc79b2cbab84c73265`; freeze `05310c3ad8065cac69efb34e74b0417e7a6ec908b5fbb5a7cd1de3443796f5dd`; final binding `f45552511f467ebdd9cebdfc370552872b50dc0cc0b709f79070115d1d80403b`; prepared metadata `b10100ffc8ff573d7c7f49c47e0ebb6f4b73e7f3a7bc2c6ce2bfeb694f605627`; actual dispatch `8e2262b66a59b5353f5e5d6af91b399d0eec5939e7786750df541f6109cdc466`. The observed native clock before this exclusive write was `2026-10-30T17:16:37-0700 PDT`, not a claimed file-creation timestamp.

The original source paths were not opened separately; whole-source and selected-byte pins above are parent-supplied, whereas the packet/metadata hashes are direct. No held episode or any of its proof/method/selection/planning/verification/reporting/confidence/downstream consumers, no old code, no unspecified sibling artifact, and no outgoing source link was used. No solver, scientific executable, CAS, test, build, lint, formatter, finite program or search was run. Metadata hashing and writing this addendum are not scientific verification; no sampled finite run is a proof.
