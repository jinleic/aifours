# Independent all-graph occupancy reconstruction, 2+2 physical obstruction, and correction to F747 §3

**Status: NONBLIND GENERAL-AUTHOR WRITTEN CANDIDATE; NOT ADOPTED, NOT INDEPENDENTLY CHECKED.** The frozen F747 candidate remains unchanged and unadopted. Its §3 argument has the concrete error displayed in §3 below. I give a different uniform parity argument and an independently written reconstruction of the four non-1111 all-graph cases, with the requested detailed physical 2+2 proof. These are claims for separate disjoint checking, not a parent disposition. In particular, no conclusion about `d_E >= 1` is adopted here. The 1111 theorem is an explicit, separately adopted **import**, not proved anew by this return; composition requires a check that that import and every new case apply at the same actual interface. Nothing here rules out any `d_E=1,2,3,4` case or establishes an original Boolean/NL242 result.

Native clock observed before this exclusive creation: `2026-10-30T17:52:35-0700 PDT`. This is an observation before writing, not an asserted exact write time.

## 1. Precise domain and local identities

Work at the literal S4–S6 actual imports, with one common five-span rank-two object, its physical `f,R,a,g,x=U0,y=U3`, local `H_loc=0`, the actual original-DC transport `t`, the named graph/bent assumptions, and physical counts `D0=4, D3=18, Z2=6, Z4=1, Z0=17`, `sum x^2=56`, `sum y^2=128`. Require all 64 U0 coefficients divisible by 8 and capped by 8, the *specified* `xhat(t)=0`, `J=1`, and all 64 U3 coefficients capped by 12. Use the imported same-X seven simultaneous profiles, the general-g residue, and the graph/bent interfaces only at their stated actual scopes. In the proof restrict explicitly to `d_E=0`: all four D0 sites are among the sixteen graph mates. Thus the six E-row blocks are D3; both F blocks and the six E blocks have `X=0` at ell=0, b=0, while their Y values are respectively zero and `+/-2`. The six Z2 and unique Z4 lie at ell=0, b!=0. No three-cell pattern is assumed. The separate 1111 import has its own stated all-graph premise.

Put `I=B=F_2^2`, write vectors and covectors as bit pairs, identify them by the usual dot product, and let `Q(a0,a1)=(a1,a0)`. Let `chi_alpha(b)=(-1)^(alpha.b)`. The common radical coordinates are `(ell,h,i,b)`, with i,b in F_2^2, graph h=`F_i`, actual physical mate h=`1+F_i`, and `sum_i F_i=1`. Physical b is unchanged. Set `X(c)=(-1)^(t.c)x(c)`, `Y(c)=(-1)^(t.c)y(c)`; this is a common spectral translation, not a new choice of t or a modulation of the fixed a or g.

For graph row i let `D_i` be its actual D0 mate sites, `k_i=|D_i|`, `S_i(b)=X(1,F_i,i,b)` and `Dsgn_i(b)=X(1,1+F_i,i,b)/2`. Thus S is always a sign, while Dsgn is a sign on D_i and zero elsewhere. Define

`Z_(ell,i)(s,alpha)=(1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha.b)`.

The zero column `Z(0,0)` is identically zero. Each of the other seven columns, simultaneously for the same X, is either a single `+/-2` or four `+/-1` on one affine 2-flat of the 3-bit quotient `(ell,i)`, with product of its four signs `-1`. Hence, in *each* profile, the number of odd entries on ell=1 is even: the affine functional ell is either constant or balanced on a flat; a singleton has no odd entries. Also, for each ell=0 row and each s,

`sum_alpha Z_(0,i)(s,alpha)=0`,                                                (1.1)

because X vanishes at its physical b=0 sites. Its row zero implies every occupied ell=0 row has an even number of Z2 sites, so at most three ell=0 rows are occupied. The parity of `Z_(0,i)(0,alpha)+Z_(0,i)(1,alpha)` is independent of alpha and equals `Z_(0,i)(1,0) mod 2`.

The graph row transform and its row-zero relation are

`Z_(1,i)(s,alpha)=(-1)^(s F_i) [Shat_i(alpha)+2(-1)^s Dsgnhat_i(alpha)]/4`,
`Shat_i(0)+2 Dsgnhat_i(0)=0`.                                                (1.2)

All hats on b alone are unnormalized. The row-zero relation makes S balanced/constant for even k and a 3:1 sign for odd k. More precisely:

* k=0: `S=epsilon chi_xi`, xi nonzero; at alpha=xi both extensions have one odd entry, and otherwise neither does. Its lambda entry is zero.
* k=1: `S=epsilon(2*1_(b=gamma)-1)`, the D0 sign is epsilon at its site u. At each nonzero alpha precisely one graph entry is odd, at `s=alpha.(gamma+u)`; the lambda entry is `+/-1`.
* k=3: the same form of S holds; u is the *omitted* mate and v the minority-sign D0 site. The D0 signs are two epsilon and one `-epsilon`, and for nonzero alpha `Dsgnhat=-epsilon chi_alpha(u)-2epsilon chi_alpha(v)`. Again one main odd entry is at `s=alpha.(gamma+u)`. In the opposite extension there is additionally a singleton `+/-2` precisely at the unique nonzero `alpha=Q(u+v)`; no other extra entry occurs. Its lambda entry is `+/-1`.
* k=2: put actual pair `{u,v}`, `Delta=u+v !=0`, `a=Q Delta`. If D0 signs are equal, row zero forces S constant, xi=0 and lambda is `+/-2`; call this **active**. Its odd graph entries occur in both extensions only at alpha=a. If D0 signs are opposite, S is a nonconstant character and lambda is zero. If xi=a (**N**), both extensions are odd at every nonzero alpha. If xi!=a (**O**), alpha=xi has one `+/-2` singleton in one extension, alpha=a has zero in both, and alpha=xi+a has one odd entry in each. The other extension at the singleton is zero in this row.
* k=4: Dsgn has sum 0 or `+/-2`. In the latter case S is constant, lambda is `+/-2`, and this row has one odd entry in each extension at all three nonzero alpha. In the former, S and Dsgn are nonconstant signed characters with covectors xi and a. Equality xi=a would give a forbidden magnitude 3 in (1.2), so xi!=a. At alpha=a this graph row is a `+/-2` singleton in **both** extensions, at xi it has one odd entry in each, and at xi+a it is zero.

These statements include both signs and all possible alpha collisions. For the k=2 rows the pair-transform support is obtained from `chi_alpha(u) +/- chi_alpha(v)`; no one-D0 exception formula is used there.

The common graph phase has affine row-linear parts `lambda_i` forming an affine bijection, so `sum_i lambda_i=0`. An even-k graph Y row is bent,

`G_i(b)=sigma_i (-1)^(b0 b1+theta_i.b)`, `theta_i=lambda_i+xi_i`;

an odd-k graph Y row is a character with covector

`kappa_i=lambda_i+(1,1)+Q gamma_i`.                                         (1.3)

These are consequences of the same graph relation `Y=-agX`, not independent choices of spectra.

## 2. Separate uniform parity proof, including all 2+2 types

**This is a new repair, not a statement that the frozen F747 proof made a valid inference. It requires independent review.** Define `B_D=sum_i sum_(b in D_i) b`. I claim, for each of `(4)`, `(3+1)`, `(2+2)`, `(2+1+1)`, that the simultaneous profiles imply

`sum_(even i) theta_i + sum_(odd i) kappa_i = Q B_D`.                       (2.1)

All sums are XORs. Use the elementary identity `sum_(alpha!=0) alpha * (alpha.w) = Qw` in F_2^2: for nonzero w the two covectors evaluating to one differ by Qw; for zero w the sum is zero. The only profile fact used for graph odd support is the evenness proved above, including singleton columns.

**4.** If its k=4 row is active, each nonzero alpha has one paired odd graph row from it; the three k=0 covectors must occur with odd multiplicity at each alpha, so their XOR is the XOR of all three nonzero covectors, namely zero. The active row has xi=0. If it is inactive, at alpha=a its two singleton extensions prohibit every other graph odd entry. Elsewhere graph-odd parity says the parity of the three k=0 occurrences at alpha is `1_(alpha=xi)`. Their XOR is xi, so all four xi XOR to zero. The XOR of all four D0 b sites is zero, proving (2.1).

**2+2.** Denote the two actual pair covectors by `a_A=Q Delta_A`, `a_B=Q Delta_B`, and the two k=0 covectors by `xi_C,xi_D`. For each nonzero alpha, let `r_alpha` be the number, modulo 2, of graph rows contributing odd entries in both extensions. It is zero by the affine-flat graph parity. The weighted XOR contribution of a k=0 row is xi; of an active pair is a; of an N pair is the XOR of all three nonzero covectors, zero; and of an O pair is xi+a. Therefore

`0=sum_(alpha!=0) alpha r_alpha = sum_(all four i) xi_i + a_A+a_B`.

For this equality use xi=0 for an active pair and xi=a for an N pair; it covers every active/N/O combination, singleton-extension sign, coincident covector and actual pair placement without assuming either pair is active or preselecting ell=0 signs. Since `B_D=Delta_A+Delta_B`, (2.1) follows. A graph singleton cannot share its extension with any other nonzero entry; that additional constraint is used later but is not needed for this identity.

**3+1.** Let A have k=3, B have k=1, and let their main-extension offsets be `t_A=gamma_A+u_A`, `t_B=gamma_B+u_B`, with u_A omitted and u_B the actual singleton D0 site. Set `w=t_A+t_B`; let C,D be the k=0 rows. At A's special alpha, its singleton forces B's odd entry into A's other extension, and forbids both paired k=0 entries; thus `alpha.w=0` and the k=0 occurrence parity is zero there. At any other nonzero alpha, graph-flat parity in each extension says

`1_(alpha=xi_C)+1_(alpha=xi_D) = alpha.w (mod 2)`.

It also holds at the special alpha. Weight by alpha and XOR: `xi_C+xi_D=Qw`. Since `gamma_A+gamma_B=w+u_A+u_B` and the three sites in A XOR to the omitted u_A, the left side of (2.1) is `Qw+Q(gamma_A+gamma_B)=Q(u_A+u_B)=QB_D`. No equality of offsets is required.

**2+1+1.** The two odd rows already consume two units of lambda-column energy; hence the k=2 row cannot be active. Write its pair covector a, its graph covector xi, and the k=0 covector d. Let w be the XOR of the two odd-row offsets. Away from a possible O singleton, graph-flat parity gives `r_alpha=alpha.w`, where r counts the paired contributions of the k=2 and k=0 rows. At an O singleton, both odd-row entries must be in the other extension and the paired k=0 row is forbidden, so the same equation holds there. In the N case the weighted XOR of r is d (the three nonzero alpha sum to zero); in the O case it is `(xi+a)+d`. Consequently in both cases `xi+d=a+Qw`. The two odd graph character covectors contribute `Q(gamma_1+gamma_2)` beyond their lambda parts, and `gamma_1+gamma_2=w+u_1+u_2`. Thus the total is `a+Q(u_1+u_2)=QB_D`. This includes N, O, all zero/collision cases and both alpha-extension choices.

## 3. Exact counterexample to F747's offset subclaim, not to its final theorem

F747 §3 asserts the two odd-row offsets must agree and, in `(3+1)`, that the two k=0 covectors must agree. This does **not** follow from the simultaneous seven profiles. The following explicit signed-X configuration realizes the physical D0/Z2 locations and all seven profiles, with unequal offsets. It does not claim a common capped Y or original caller.

Use i labels A=00, B=01, C=10, D=11; `F_A=1`, the other F values 0. The ell=1 graph signs, D0 sites and Dsgn signs are:

| row | graph S(b) | D0 mate b : Dsgn |
|---|---|---|
| A | `2*1_(b=10)-1` | `01:+1, 10:-1, 11:+1` |
| B | `2*1_(b=00)-1` | `00:+1` |
| C | `chi_10(b)` | none |
| D | `-chi_11(b)` | none |

All other graph-mate X values are zero; a listed Dsgn means X is twice that sign at the actual mate h=`1+F_i`. On ell=0 put precisely these six nonzero X values, all others zero:

* U=00: `(h,b)=(0,10):+2`, `(1,11):-2`;
* V=01: `(0,10):+2`, `(1,01):-2`;
* W=10: `(0,01):+2`, `(0,11):-2`.

This leaves the physical b=0 F/E X values zero; the unique Z4 may be designated at the otherwise X-zero ell=0 site `(h,i,b)=(0,11,01)` and all remaining such X-zero sites Z0. The X data themselves do not supply Y or prove full physical inverse/caller admissibility. Each displayed row has zero sum. With `gA` denoting quotient `(ell=1,i=A)` and `eU` `(ell=0,i=U)`, its seven nonzero profiles are **exactly**:

| `(s,alpha)` | complete nonzero `Z` entries |
|---|---|
| `(1,00)` | `gA:+1, gB:-1, eU:+1, eV:+1` |
| `(0,01)` | `gA:-1, gB:+1, eU:+1, eV:+1` |
| `(1,01)` | `gA:-2` |
| `(0,10)` | `gB:+1, gC:+1, eV:-1, eW:+1` |
| `(1,10)` | `gA:+1, gC:+1, eU:-1, eW:+1` |
| `(0,11)` | `gB:+1, gD:-1, eU:-1, eW:-1` |
| `(1,11)` | `gA:+1, gD:-1, eV:-1, eW:-1` |

Every listed four-support has XOR zero in `(ell,i)` and is therefore an affine 2-flat, with product `-1`; the singleton has magnitude 2. Thus these are all seven required profiles for one X, not a lambda-only example. Direct quotient Fourier inversion gives the corresponding carried U0 spectrum values 0 or `+/-8`: the four-sign odd-product transform has magnitude 2 and the singleton transform magnitude 2, with the factor 4 in the definition of Z. This establishes only the stated X/profile boundary. The omitted A mate and B's D0 mate are both 00, while `gamma_A=10`, `gamma_B=00`, so the offsets are respectively 10 and 00. Also `xi_C=10`, `xi_D=11`. Their XOR is 01=`Q(10)`, exactly compensating the unequal offsets in (2.1). Nothing here verifies J, the U3 residue/cap, a common full Y, V, selected T, or the original caller. It is **not** a counterexample to the asserted all-graph no-go.

## 4. Common U3 parity and the twelve actual mate signs

For the four occupancy types, define the ell-partial Y transforms

`A_ell(s,alpha,beta)=sum_(h,i,b)Y(ell,h,i,b)(-1)^(s h+alpha.b+beta.i)`.

Write n for the number of negative signs among the twelve actual nonzero graph mates, and m_alpha for the number of odd-row graph characters equal to alpha. From (2.1), every `A_1/4` is integral and

`A_1/4 = n+c+s+m_alpha+alpha.(B_D+Q sum_even theta_i) (mod 2)`              (4.1)

for a constant c independent of s, alpha, beta. To see this, an even graph Walsh value is twice a sign with normalized dual `sigma_i (-1)^((alpha+theta_i)_0(alpha+theta_i)_1)`; each actual mate contributes twice a sign. The product of the relevant signs gives n, the indicated b exponent, and s exponent `sum_even F_i+sum_odd(1+F_i)=1`; the beta exponent is `sum_i i=0`. There are 0 or 2 odd graph rows, whose Walsh values add `m_alpha` modulo two after division by 4. Their constants and the even number of dual quadratic terms are absorbed into c.

Put `v=B_D+Q sum_even theta_i`. Equation (2.1) says the XOR of the odd kappa values is Qv. With no odd rows v=0. With two equal kappa, again v=0 and m_alpha is always even. With two distinct kappa, they form one full level set of alpha.v because `(Qv).v=0`; hence `m_alpha+alpha.v` is constant. Therefore one single slice `s_*` has all `A_1/4` even and the other `s'=s_*+1` has all odd, simultaneously for all 16 alpha,beta.

The general-g/J=1 residue gives all full Y coefficients congruent to 4 modulo 8. Their cap and energy 128 give exactly eight coefficients of magnitude 4 and 56 of magnitude 12. Since `A_0 +/- A_1` are the paired full coefficients, both partial values are multiples of 4, their quotients have opposite parity, and `|A_0|+|A_1|<=12`.

Let E count the 16 positions at s_* where `|A_1|=8`, and O count those at s' where `|A_1|=4`. Every such position consumes at least one of the eight distinct magnitude-4 full coefficients, so `E+O<=8`. The ell=1 energy is `16+12*4=64`; Parseval yields `O=2+E/2`. If `e_i(b)` is the actual mate sign, put `C=sum_(12 actual mates) G_i(b)e_i(b)`. The b,i Parseval identity at s_* gives `E=16+(-1)^s_* C>=4`. Hence `E=O=4`, and equality in `|C|<=12` gives, at **every actual non-D0 graph mate**,

`e_i(b)=-(-1)^s_* G_i(b)`.                                                  (4.2)

Every O position has `|A_0|=8`: if it had A_0=0 it would use two small full coefficients, exceeding the exact total after E and the other O positions are counted. At s' the contribution of graph row i is therefore

`(-1)^(s' F_i) sum_b G_i(b) chi_alpha(b) [3-2*1_(b in D_i)]`.             (4.3)

For any three distinct i in F_2^2, an actual beta can align any specified three real nonzero row signs, because those three points are affinely independent. This is one common physical frequency, not a frequencywise assembly of unrelated arrays.

## 5. Three other all-graph partitions, pending independent review

These short consequences are included so the conditional composition boundary is explicit; they use §2's new parity proof, not F747's invalid intermediate offset claim.

* `(4)`: at any alpha, the k=4 row has magnitude 2 and the other three bent rows have magnitude 6 in (4.3). Align the three sixes: at least `18-2=16`, violating the cap.
* `(3+1)`: at the k=1 graph character, its row has magnitude 10, the two k=0 bent rows each 6, and the k=3 character row at most 6. Align the first three: at least 16. The k=3 bound follows since its row magnitude is 6 at its own character and 2 at the other alpha.
* `(2+1+1)`: a k=2 bent row in (4.3) has magnitude 2 or 6, as proved in §6. A k=1 character row has magnitude 10 at its character and 2 elsewhere. If the two characters differ, choose one and align its 10, the k=0 row's 6 and the k=2 row's at-least-2, subtracting the other 2: at least 16. If they coincide, align the two 10s and the k=0 6, subtracting at most 6: at least 20.

All three contradict the same cap `|A_1|<=12`. The general 2+2 case is handled below, without importing a location theorem from the one-D0-per-row case.

## 6. Complete 2+2 reconstruction: pair matching to the physical Z2 contradiction

Let A,B be the k=2 rows, with actual D0 pairs `{u_i,v_i}`, `Delta_i=u_i+v_i !=0` and `P_i=G_i(u_i)G_i(v_i)`. In (4.3), put the deleted signed summands `d_u=G_i(u_i)chi_alpha(u_i)`, `d_v=G_i(v_i)chi_alpha(v_i)`. A bent four-point sign row has product `-1` and Walsh value `2d`, d a sign. If `d_u=d_v`, the other two summands are opposite and d=`d_u`; the modified row is `2d`. If `d_u=-d_v`, the deleted sum is zero and the modified row is `6d`. Thus its magnitude is 2 iff

`P_i chi_alpha(Delta_i)=+1`; otherwise it is 6.                              (6.1)

The two k=0 rows always have magnitude 6. If the pair-row magnitudes differ at any alpha, aligning the three sixes gives at least 16 even after the remaining two is subtracted. Therefore their predicates agree for every alpha. At alpha=0 this gives `P_A=P_B=P`; varying all alpha then gives

`Delta_A=Delta_B=Delta !=0`.                                                 (6.2)

Let `a=Q Delta`. Now `B_D=Delta_A+Delta_B=0`, so §2 yields `sum_i theta_i=0`. The product of all sixteen graph signs is +1 (each bent row has product -1); removing the four D0 signs has product `P_A P_B=1`. By (4.2), the product of all twelve actual mate signs is also +1, so n is even. The product of the four normalized bent dual signs is a constant in alpha, say `(-1)^c`. For four even rows (4.1) is `A_1/4=n+c+s mod 2`, so `c=s_* mod 2`. The product of the four signed row-dual signs at s' is consequently `(-1)^(s'+c)=-1`, using `sum F_i=1`. The signs of the modified 2/6 rows agree with their bent duals by the preceding calculation.

For the two alpha with `chi_alpha(Delta)=P`, the four row magnitudes are `(2,2,6,6)` and their sign product is -1. As beta runs over its four values, the absolute sums are exactly `4,4,12,12`: when the two sixes have the same sign the twos have opposite signs, and vice versa; each situation occurs twice. At the other two alpha all four magnitudes are 6 and odd sign product gives four absolute sums of 12. Thus (4.3) has exactly four magnitude-4 positions, precisely as §4 requires.

Define the **one physical** ell=0 h-combination

`B_i(b)=Y(0,0,i,b)+(-1)^s' Y(0,1,i,b)`.

At each of the two selected alpha, A_0 is nonzero at exactly two beta and equals `+/-8`; at every other alpha,beta it is zero. Invert the beta transform: for each selected alpha, `Bhat_i(alpha)` is 0 or `+/-4`, nonzero at exactly two i. The selected covectors are `gamma` and `gamma+a`. Inverting b at b=0 gives `|B_i(0)|<=2`. But physical F blocks give B_0(0)=0 and each E pair gives B_i(0) in `{0,+/-4}`. Hence all `B_i(0)=0`. Consequently `Bhat_i(gamma+a)=-Bhat_i(gamma)` for each i; the same two rows, U,V, are the only nonzero B rows. In fact

`B_i(b+Delta)=P B_i(b)`, and `B_i(0)=B_i(Delta)=0`.

Let p,q be the other two nonzero physical b values; `p+q=Delta`. The inverse transform gives `|B_i(p)|=|B_i(q)|=2` in each of U,V and zero elsewhere. This handles either P sign and either selected alpha level, including a level containing alpha=0.

Now derive, rather than assume, the physical Z4/Z2 placements. A Z4 at a zero B site cannot cancel: its opposite-h site is at most a single Z2, so `+/-4` plus 0 or `+/-2` is nonzero. Hence the unique Z4 is at one of the four `(U or V,p or q)` sites and has a Z2 in the opposite h slot. At each other one of these four sites there is exactly one Z2, because two `+/-2` contributions sum to 0 or `+/-4`, never `+/-2`. These use four Z2. The remaining two Z2 must be an opposite-h cancelling pair at one other physical site: a lone Z2 at a B-zero site is impossible, and no supporting site has a spare slot compatible with its required magnitude. It cannot be at b=0, which consists of the actual F/E blocks. If it occupied a third i-row, that row would contain exactly this pair; its zero-profile row sum forces opposite X signs and hence its lambda entry would have magnitude 1.

The lambda column is a **singleton**, not a four-plane. Indeed, two active k=2 rows would already exceed energy 4; if one is active it supplies the singleton. If neither is active, the graph lambda entries all vanish; an ell=0 four-plane would need four occupied ell=0 rows, but there are at most three. Therefore a lambda magnitude-1 entry is impossible, and the cancelling pair lies in U or V. Rename its row U. Its b must be Delta, since p and q already carry their required support contributions and b=0 is F/E. The other row V has just its two Z2 at p,q. Its zero row sum makes their X signs opposite. If their h values differed, V's lambda would have magnitude 1, so both have the same h, say h_V.

In row U the cancelling pair occupies both h slots over Delta, and the remaining Z2 sites are one each over p,q. The zero row sum and singleton lambda rule give lambda_U either 0 or `+/-2`. They force the p and q Z2 into opposite h slots: otherwise one h contains only its Delta sign and cannot have the required zero or extremal sum. When lambda_U=0 the two X signs in each h are opposite; when lambda_U=`+/-2` they are equal within each h.

For either of the two nonzero alpha other than a, `alpha.Delta=1` and the characters of p,q are opposite. The preceding explicit X signs imply that `Z_(0,U)(0,alpha)` and `Z_(0,U)(1,alpha)` are both `+/-1`, with their ratio flipping between those two alpha. At alpha=a, if lambda_U=0 exactly one extension is `+/-2` and the other zero; if lambda_U=`+/-2`, both are zero. For V, its p,q X signs are opposite and its h is common, so at both alpha other than a it has two `+/-1` entries with fixed extension ratio `(-1)^h_V`; at alpha=a it is zero.

An O pair row has a graph singleton at xi!=a; either such singleton conflicts with the nonzero U entry in the same extension. Hence every inactive pair is N. If one pair were active, lambda is the graph singleton and lambda_U=0; at alpha=a the active and the N graph rows are nonzero in both extensions, conflicting with U's singleton in one of them. Two active rows were already excluded. Thus **both pairs are N**, and lambda_U is `+/-2`.

For every nonzero alpha the two N rows contribute one graph odd entry each per extension. The two k=0 covectors must coincide by even graph-support parity. If their common covector eta were not a, at eta all four graph rows would be odd in both extensions while U is also odd, impossible for an energy-4 profile. Thus eta=a. At each of the other two alpha, in each extension the same four quotient points `(1,A),(1,B),(0,U),(0,V)` are odd, and their profile signs have product -1. On each graph N row the extension ratio is `(-1)^(F_i+1)`, independent of alpha, because the signed D0-pair transform alone contributes. V's ratio is also alpha-independent, whereas U's flips. Therefore the ratio between the two extension sign products changes between the two alpha, although both products are required to equal -1. This contradiction excludes 2+2 under the exact imports, subject to independent checking.

## 7. Scope of any composition and remaining frontier

The five partitions of four graph D0 are 4, 31, 22, 211, 1111. Sections 2 and 4–6 offer a fresh written candidate for the first four; S4 separately states the adopted 1111 exclusion at its explicit normalization/physical-count/graph scope. **Only if** independent scrutiny verifies the new arguments, and the prior 1111 theorem is confirmed applicable with all the same actual imports, can their logical union imply the necessary condition `d_E>=1`. This file does not certify that verification or adopt the union. It cannot remove d_E=1,2,3,4 or infer any U3/V/full-caller witness. S7 reports only a prior parent-run local/lambda-scope enumeration; it is not a proof of simultaneous seven profiles or U3, and was not used as such. The F748 singleton warning is a warning, not an imported classification.

## 8. Coverage, bindings, corrections, and NOTTESTED

Before the direct PREBODYACK to Main I read actual dispatch, the complete manifest, freeze receipt, final binding, prepared metadata and all 22 listed controls through their endings, as permissions/status only. Then I read the single literal packet **serially as RAW LF 1–728 in contiguous calls of at most 20 LF**, through its ending, before comparison or mathematical work. No outgoing links, held history/payload/consumers, unspecified sibling proof or old code were read for science. The complete packet S1–S7 covers all 22? No: the packet contains exactly **seven scientific/source blocks** and the separately read controls number **22**. Parent-supplied source bindings and their complete original ranges are:

* S1 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json`, LF 1–11, SHA256 `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c`.
* S2 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md`, LF 1–7, SHA256 `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca`.
* S3 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f747-boolean-general-d0-occupancy-profile-frontier-author/author-candidate-v1.md`, LF 1–143, SHA256 `27fcb901518fdf2208f55553d647f5ef5d17960fc0c606f3f6fe3a02d33b7f85`.
* S4 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-entire-four-distinct-d0-rank2-same-object-obstruction-parent-v1.md`, LF 1–31, SHA256 `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928`.
* S5 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-recovered-local-H-definition-and-general-g-foundation-v1.md`, LF 1–13, SHA256 `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef`.
* S6 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-actual-rank2-seven-profile-and-four-distinct-d0-cross-fibre-parent-v1.md`, LF 1–37, SHA256 `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`.
* S7 `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f749-boolean-d0-occupancy-local-profile-exact-finite-author/parent-d0-occupancy-local-profile-v2-run-v1-receipt.json`, LF 1–456, SHA256 `44fc6d7c1f177a22eba29d295889220761f540a427bb84a7b7f9d9912cc52bf9`.

These source SHA values are the frozen parent bindings; I did not separately open or rehash those source paths. I independently observed metadata hashes: manifest `4009719b08d3ea9673308d51eb3f87ad3c9d010aceafbc89f16df7ddbaa33d85`; freeze `93bc545ef842dcae6d020a1a7ed152ed5b53f5a21849fd3c339c4eadff3492b0`; final binding `257a64f28153cd809bee964fe7b38b4cb14632d55de543717155f95ec92e56e6`; prepared metadata `ea64d77e26516f38b5bf468a8244769c060dcac82e5d39aae9575779b8ef2a59`; actual dispatch `bd0e871d112efd448f8b32b71cdd469e452a6f5ef7cf82ad134c4e249ed14ecc`; complete packet `b00c3a145d4337ee744046eb921e7ad1d91be878130f9eb238ea748340b2f95d`. The PREBODYACK reported the first five observations and exact part count/LF before the packet read; the packet hash observation was after complete reading.

The specific correction is §3's counterconfiguration and §2's replacement parity proof; no frozen source was modified. The written example is not a computational check. **CHILD SCIENTIFIC EXECUTION NOT RUN:** no finite source was created or run, and no program, solver, CAS, test, build, linter, formatter, external-model CLI, installation or parent GO was used. This is not independent-model-family, human, kernel/formal, original-source-identity, novelty, global completion or parent-adoption evidence. Any later correction must use a new additive artifact, not an overwrite.
