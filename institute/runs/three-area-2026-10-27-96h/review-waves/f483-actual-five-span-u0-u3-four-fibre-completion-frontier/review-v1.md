# F483 GENERAL AUTHOR candidate: exact four-fibre completion constraints for the canonical five-span branch

**Status: AUTHOR / WRITTEN PROOF CANDIDATE; no automatic adoption.** No actual balanced NL242 witness or exclusion of the whole five-span branch is claimed.

The results below are:

1. A written reconstruction of the f468 graph/bent/lift statements and mathematical census.
2. A complete local parametrization at the displayed \(H=0,\ G_3=1\) necessary-count scope.
3. A new common-phase parity/XOR obstruction for the remaining \(U_0\) fibre.
4. An exact reduction of the remaining even-half and complementary odd-half obligations.

In particular, the entire eight-two-point-zero-block lift construction in S1 is excluded from this named \(G_3=1\) caller. This does **not** declare S1 erroneous: S1 expressly labels those constructions local, not original-target witnesses.

## 1. Read chronology, authority and execution status

All 130 manifest LF, the complete receipt, parent metadata/dispatch records, and all ten `controls_before_body`, including endings, were read before the pre-body acknowledgment at `local://f483-prebody-ack-v1.md`. Only afterward was the literal packet read completely, in order, in exact raw windows LF1–20,21–40,…,281–300,301–314. Mathematics followed that complete read.

No sibling return, linked source body, held payload, author program, external source, or external model was opened. No scientific executable, selected numerical probe, test/build/lint/formatter, or repository mutation was run. The derivations below are written all-parameter arguments, not experimental results. **Optional calculation status: NOTRUN.**

Identity/clock attribution is to the parent-supplied metadata, not child-native hashing or timing:

- Manifest SHA256: `f78bde09d329d1e9b0741b45224eb34c467919dd87f877791e930b1106943a9d`.
- Freeze-receipt SHA256: `7fb9ae1490b94f07060792c625f10eb0f230474182c6cf6c37d6da9ce9d3d96b`.
- Literal-packet SHA256: `fb9a7bcaf50588c3b07e6213fb486f3e92e9b1948e3e3c998fb0138945e129d0`, 314 LF.

The parent’s recorded pre-creation clock is `2026-10-30T12:13:16-0700 PDT`; it is not my acknowledgment time, completion time, or an execution-duration measurement. All historical HELD episodes and their consumers remain status-only/NONINPUT.

Inputs are exactly:

- S1 LF1–76: f468 unreviewed parent candidate.
- S2 LF1–37: adopted actual dichotomy.
- S3 LF1–37: adopted affine-support exclusion/interface.
- S4 LF1–162: f263 full original-caller review.

S1’s execution/control reports are not independently replayed here. Its mathematical census is instead reconstructed below. Neither this reconstruction nor an author return is a parent disposition or an independent-family review.

Complete body also retained at `local://f483-author-candidate-v1.md`.

## 2. Fixed coordinates and exact target

Use unnormalized Walsh transforms throughout. Write
\[
R=\mathbb F_2^6,\qquad c=(h,d),\qquad h=(l,j)\in\mathbb F_2\times\mathbb F_2^2,\quad d\in\mathbb F_2^3,
\]
and \(Q=\mathbb F_2^2\), with characters \(\chi_1,\chi_2,\chi_3=\chi_1\chi_2\). For an actual ternary block function \(u\), define
\[
U_s(c)=\sum_wu(c,w)\chi_s(w),\qquad a=U_1/3,\qquad g=U_2.
\]

Work only in the normalized **five-span** branch imported from S2. Its data are:

- \(d_b=1+3b_0+5b_1\), \(b\in\mathbb F_2^2\), with addition interpreted as binary-vector XOR.
- \(\rho_b=(-1)^{1+b_0b_1}\), hence \(\rho=(-1,-1,-1,+1)\).
- \(E=\{d=0\}\), \(F=\{(h,d)=(0,0),(1,0)\}\), and \(B=\{d=1,2,4,7\}\).
- \(S=\operatorname{supp}(a)\) has four points in each \(B\)-coset and no point in \(E\).
- \(g(h,0)=-2+6\mathbf1_{\{0,1\}}(h)\).
- \(g(h,d_b)=\rho_b(-2+3\mathbf1_S(h,d_b))\), with \(g=0\) on the remaining 24 blocks.
- \(|\widehat a|=4\); \(\widehat g\) has four \(+4\) coefficients at the named \(A_2=\{0,1,2,4\}\) in the dual \(d\)-coordinate and magnitude 12 elsewhere.

Let
\[
D=(E\cup B)\setminus(F\cup S),\qquad |D|=22,
\]
so \(|g|=2\) on \(D\). Let
\[
Z=R\setminus(E\cup B),\qquad |Z|=24.
\]
Let \(e=(h=1,d=0)\) be the **primal** direction joining the full-block pair. It is not the dual normal \(\nu=(0,7)\) of \(B\).

The named actual-caller obligations in S4 include:

- \(|\operatorname{supp}(u)|=116\).
- \(\sum U_0^2=56\), \(\sum U_3^2=128\).
- \(H=0\), with \(H\) explicitly the number of \(U_1=0\) blocks having a single \(|U_0|=4\) peak.
- \(\#\{U_3=0\}=23\) at \(G_3=1\).
- Globally, \(\widehat U_0\in\{0,\pm8\}\), with eight zeros.
- Globally, \(\widehat U_3\in\{\pm4,\pm12\}\), with eight magnitude-four positions.

Balance is an **original-coordinate** condition, treated in §7. No undisplayed historical class convention is silently identified with these explicit local/count statements.

## 3. Written reconstruction of f468

### 3.1 The transversal and bent equivalences

For nonzero \(h\)-frequency \(y\) satisfying \(y\cdot1=0\), the \(E\)-row transform is 12. All eight full coefficients \(\widehat g(y,z)\) have magnitude 12 and average 12 over \(z\). Therefore all equal \(+12\). Inverting the \(d\)-transform shows that every other \(d\)-row has zero transform at these three nonzero \(y\).

On \(B\), the constant \(-2\) term has zero transform at nonzero \(y\). Thus the three nontrivial quotient transforms of the support slice vanish. Each slice has four points. Fourier inversion on \(h/\langle1\rangle\) says every pair \(\{2j,2j+1\}\) contains exactly one support point. Consequently one common function \(f:\mathbb F_2^4\to\mathbb F_2\) parametrizes \(S\):
\[
S=\{(h,d)=(2j+f(j,b),d_b):j,b\in\mathbb F_2^2\}.
\]

For \(y=1+2v\), the \(E\)-contribution vanishes. Set
\[
q(b)=1+b_0b_1,\qquad w(z)=(z\cdot3,z\cdot5).
\]
Direct substitution gives
\[
\widehat g(1+2v,z)
=3(-1)^{z\cdot1}W_{f+q}(v,w(z)).
\]
The map \(z\mapsto w(z)\) is onto, twice onto each value.

At \(y=0\), the row sums are \(-4\) on \(E\) and \(-4\rho_b\) on \(B\), giving \(+4\) for \(d\)-frequency weights zero/one and \(-12\) for weights two/three. The other even \(y\)-rows already equal \(+12\). Therefore the **complete** required \(g\)-spectrum is equivalent to \(f+q\) being bent on four variables.

Write
\[
a(2j+f(j,b),d_b)=(-1)^{r(j,b)}.
\]
The same calculation gives
\[
\widehat a(2v,z)=(-1)^{z\cdot1}W_r(v,w(z)),
\]
\[
\widehat a(1+2v,z)=(-1)^{z\cdot1}W_{r+f}(v,w(z)).
\]
Hence
\[
|\widehat a|\equiv4
\quad\Longleftrightarrow\quad
r\text{ and }r+f\text{ are both bent}.
\]
These are common-object equivalences, not independently chosen spectra.

### 3.2 The mathematical census, without executing a census

A four-variable bent Boolean function has degree at most two. Its total weight is 6 or 10. On every affine hyperplane, the sign sum is half a sum/difference of two \(\pm4\) Walsh coefficients, hence \(0\) or \(\pm4\); its weight is therefore \(2,4,\) or \(6\), always even. The ANF quartic coefficient is the parity of the total weight, and each cubic coefficient is the parity on a coordinate three-face. All vanish.

For a quadratic function, flat Walsh magnitude four is equivalent to its alternating polar form being nonsingular: the autocorrelation at a shift \(t\) is a character sum of its polar linear form, zero exactly when \(t\) is outside the radical. Thus all nonzero shifts have zero autocorrelation exactly when the radical is zero.

For an alternating four-by-four form \(M\), put
\[
\operatorname{Pf}(M)
=M_{12}M_{34}+M_{13}M_{24}+M_{14}M_{23}.
\]
It is nonsingular iff \(\operatorname{Pf}(M)=1\). The triple \((M_{12},M_{13},M_{14})\) must be nonzero; there are four complementary triples giving dot product one. Thus there are \(7\cdot4=28\) nonsingular forms. Each polar form has \(2^5=32\) affine offsets, giving \(896\) bent functions.

The polar form \(Q\) of \(q\) has rank two. In a basis with \(Q_{12}=1\) and other coefficients zero,
\[
\operatorname{Pf}(F+Q)=\operatorname{Pf}(F)+F_{34}.
\]
For \(\operatorname{Pf}(F+Q)=1\):

- Rank-two \(F\): \(F_{34}=1\), \(\operatorname{Pf}(F)=0\). The other four cross coefficients are free and \(F_{12}\) is determined, giving 16 forms.
- Rank-four \(F\): \(F_{34}=0\), and
  \[
  F_{13}F_{24}+F_{14}F_{23}=1.
  \]
  Six invertible two-by-two cross matrices and two choices of \(F_{12}\) give 12 forms.

Thus there are \(16\cdot32=512\) rank-two graphs and \(12\cdot32=384\) rank-four graphs: \(896\) in total.

No affine \(f\) is allowed, because \(f+q\) would still have rank-two polar form and would not be bent. Its graph therefore spans dimension exactly five: it lies in the known affine five-flat \(B\), while a four-flat graph over all sixteen \((j,b)\) would make \(f\) affine.

For fixed admissible \(F\), the two bent conditions on \(r,r+f\) require polar forms \(M,M+F\) both nonsingular.

- For rank-two \(F\), normalize \(F_{12}=1\). The conditions are \(M_{34}=0\) and cross determinant one, giving \(2\cdot6=12\) forms.
- For rank-four \(F\), normalize \(F_{12}=F_{34}=1\). The conditions are \(M_{12}+M_{34}=1\) and the same cross determinant one, again giving \(2\cdot6=12\) forms.

These basis choices count abstract polar forms; they do not assert a balance-preserving transformation of an actual caller. Every form admits all 32 affine offsets of \(r\). Thus every admissible \(f\) has exactly \(384\) common phases, and there are
\[
896\cdot384=344064
\]
pairs.

This proves the mathematical census asserted in S1 independently of its program output. It does not audit that program, its elapsed time, selected diagnostic, or mutation controls.

### 3.3 The stated local lifts really are local lifts

On \(S\), a block with \(U_1=3a\), \(a=\pm1\), has exactly three aligned nonzeros. If \(\alpha=U_0=\pm1\), necessarily
\[
U_3=-ag\alpha.
\]
The omitted point \(w_0\) is uniquely specified by
\[
\chi_1(w_0)=-a\alpha,\qquad \chi_2(w_0)=g\alpha.
\]
Conversely these choices give exactly that block. Equivalently S1’s condition
\[
\chi_1(w_0)\chi_2(w_0)=-g/a
\]
leaves exactly two omitted-point choices.

On \(F\), the block is \((g/4)\chi_2\). On \(D\), one may put the second \(\pm2\) transform in slot 0 or slot 3. On \(Z\), two equal signs at opposite diagonal points give \(U_1=g=0\) and \(|U_0|=|U_3|=2\).

These verify S1’s block formulas, support count
\[
48+8+44+16=116
\]
and \(H=0\). They do **not** establish the original global caller. The next section gives a uniform obstruction to precisely that proposed eight-pair subfamily.

## 4. All local lifts at the actual necessary-count scope

Every physical lift with fixed \(a,g\) and \(H=0\) has this complete block parametrization. Write \(x=U_0,\ y=U_3\).

- On \(S\): \(x=\alpha\in\{\pm1\}\), \(y=-ag\alpha\).
- On \(F\): \(x=y=0\).
- Partition \(D=D_0\sqcup D_3\):
  - On \(D_0\): \(x=2\varepsilon,\ y=0\).
  - On \(D_3\): \(x=0,\ y=2\zeta\).
- Partition \(Z=Z_0\sqcup Z_2\sqcup Z_4\):
  - On \(Z_0\): \(x=y=0\).
  - On \(Z_2\): \(x=2\varepsilon,\ y=2\delta\varepsilon\).
  - On \(Z_4\): \(x=0,\ y=4\kappa\).

Here \(\varepsilon,\zeta,\delta,\kappa\) are signs.

There is no omitted block type: when \(U_1=0\), the actual four-point spectrum is zero, two \(\pm2\) entries, or one \(\pm4\) entry; \(H=0\) removes the \(U_0\)-peak option. The fixed \(g\) leaves exactly the displayed choices.

In every case the common inverse is
\[
u(c,w)=\frac{x(c)+3a(c)\chi_1(w)+g(c)\chi_2(w)+y(c)\chi_3(w)}4.
\]
It is genuinely ternary. On \(D_0,D_3,Z_2,Z_4\), respectively, it equals
\[
\frac{\varepsilon+(g/2)\chi_2}{2},\quad
\frac{\chi_2((g/2)+\zeta\chi_1)}2,\quad
\frac{\varepsilon(1+\delta\chi_3)}2,\quad
\kappa\chi_3.
\]

Put \(d=|D_0|,\ p=|Z_2|,\ t=|Z_4|\). Support 116 and \(U_0\)-energy 56 give
\[
p+2t=8,\qquad d+p=10.
\]
The number of \(U_3\)-zeros is
\[
2+d+(24-p-t)=20+3t.
\]
At the displayed \(G_3=1\) count it equals 23, so necessarily
\[
\boxed{
|D_0|=4,\quad |D_3|=18,\quad
|Z_2|=6,\quad |Z_4|=1,\quad |Z_0|=17.
}
\tag{L}
\]

Conversely, these counts give support 116,
\[
\sum U_0^2=16+16+24=56,\qquad
\sum U_3^2=16+72+24+16=128,
\]
\(H=0\), and exactly 23 \(U_3\)-zeros. They meet the explicit local/count obligations, not an undisplayed historical class table.

**Whole-subfamily exclusion.** Every S1 lift using eight two-point \(Z\)-blocks and no four-point \(Z\)-block has \(t=0\) and no \(|U_3|=4\) peak. If it also meets the required \(U_0\)-energy, then \(d=2\) and its \(U_3\)-zero count is 20, not 23. Thus **none** of those lifts belongs to the named \(G_3=1\) caller.

This does not exclude corrected lifts with counts (L), another actual branch, or \(G_3=0\) callers.

## 5. New common-phase parity/XOR obstruction for \(U_0\)

Use counts (L). Put
\[
W=D_0\cup Z_2,\qquad |W|=10.
\]
Define
\[
P=\{c\in S:\alpha(c)=-1\},\qquad
N=\{c\in W:\varepsilon(c)=-1\},
\]
\[
p=|P|,\quad n=|N|,\quad
X_P=\bigoplus_{c\in P}c,\quad
X_W=\bigoplus_{c\in W}c.
\]

Let \(\gamma=0\) for rank-two polar \(f\), and \(\gamma=1\) for rank-four polar \(f\). Equivalently,
\[
\gamma=\operatorname{wt}(f)/2\pmod2.
\]

The graph-indicator transform has even \(y\)-rows \(0\) or \(\pm16\), and odd \(y\)-rows equal, up to sign, to \(W_f\). A rank-two quadratic four-variable function has Walsh values \(0,\pm8\); a rank-four one has \(\pm4\). Therefore
\[
\widehat{\mathbf1_S}(\xi)\equiv4\gamma(\xi\cdot e)\pmod8
\quad\text{for every }\xi\in R^*.
\tag{G}
\]

The remaining phase obeys the following **exact equivalence**:
\[
\widehat x(\xi)\in8\mathbb Z\text{ for every }\xi
\]
if and only if
\[
\boxed{
p\text{ is even},\qquad
p/2+n\text{ is odd},\qquad
X_P+X_W=\gamma e.
}
\tag{C}
\]

**Proof.** The physical phase representation is
\[
x=\mathbf1_S-2\mathbf1_P+2\mathbf1_W-4\mathbf1_N.
\]
Since \(|W|=10\), reduction modulo four first forces \(p\) even. For any finite set \(A\),
\[
\widehat{\mathbf1_A}(\xi)
\equiv |A|-2\left(\xi\cdot\bigoplus A\right)\pmod4.
\]
Using this identity, (G), and \(p\) even yields
\[
\widehat x(\xi)\equiv
4\left[1-p/2-n+\xi\cdot(\gamma e+X_P+X_W)\right]\pmod8.
\]
This vanishes for every \(\xi\) exactly when its constant and linear parts vanish, which is (C). No amplitude assumption enters this equivalence.

Consequently:

- A rank-two graph requires \(X_P=X_W\).
- A rank-four graph requires \(X_P+X_W=e\).

Any support/phase selection violating any part of (C) cannot be an actual caller, regardless of its \(U_3\)-completion or proposed \(V\). This couples locations and phases of **one common physical \(u\)**; it is not a separate-spectrum condition. The first condition also forces the product of the sixteen \(S\)-values of \(U_0\) to be \(+1\).

## 6. A common-block dual link and an exact even-half reduction

Let \(F_s(\xi)=\widehat U_s(\xi)\). The fixed fibres satisfy
\[
F_1,F_2\equiv4\pmod8.
\]
At \(w=0\), the physical inverse gives
\[
F_0(\xi)+F_1(\xi)+F_2(\xi)+F_3(\xi)
=4\sum_cu(c,0)\chi_\xi(c).
\]

Let
\[
J=\#\{c:u(c,0)\ne0\}\pmod2.
\]
The sum on the right has parity \(J\), independently of \(\xi\). Once (C) holds,
\[
\boxed{F_3(\xi)\equiv4J\pmod8\quad\text{for every }\xi.}
\tag{D}
\]
Thus the entire third-fibre congruence \(F_3\equiv4\pmod8\) is equivalent to **one physical column-parity condition**, \(J=1\). It is not obtained by choosing an independent \(\sigma_3\).

For fixed \(f,r\) and physical choices (L), the explicit remaining even-half spectrum therefore reduces exactly to:

1. The three common-phase conditions (C).
2. \(J=1\).
3. \(|F_0(\xi)|\le8\) and \(|F_3(\xi)|\le12\) for every \(\xi\).
4. The original-coordinate balance zero in §7.

Indeed, \(\sum x^2=56\), divisibility by eight, and the first cap force \(F_0\in\{0,\pm8\}\). Parseval then gives exactly 56 nonzero coefficients and eight zeros.

Similarly, \(\sum y^2=128\), (D), \(J=1\), and the second cap force \(F_3\in\{\pm4,\pm12\}\). If \(e_3\) counts magnitude-four positions, then
\[
16e_3+144(64-e_3)=64\cdot128,
\]
so \(e_3=8\). No third-fibre zero is possible. Thus the even half has exactly eight Walsh zeros in total.

With \(k(r,s)=F_s(r)/2\),
\[
k(r,s)/2\bmod2=
\begin{cases}
0,&s=0,\\
1,&s\ne0.
\end{cases}
\]
This is the anisotropic quadratic \(s_1+s_2+s_1s_2\), of polar rank two and radical \(R\), with \(q^{-1}(0)=R\).

Local \(H\) and the displayed \(G_3=1\) zero count were established in (L). These statements do not resolve a separate historical-label identity.

At the full S4 scope, the resulting \(A_3\) must additionally obey its adopted necessary atom consequences: affine rank six with the stated four-atom relation, \(\operatorname{XOR}(A_3)=\operatorname{XOR}(A_2)=\nu\), equal small-sign product \(+1\), all-translation overlap at most two, and all-translation sign-mismatch restrictions. They are not presumed to hold for arbitrary choices satisfying only (C), nor substituted for the actual \(F_3\)-cap.

No existence of choices meeting items 1–4 is asserted here.

## 7. Balance: retain the original zero, not an arbitrary modulation

For the common-\(R\) gauge used in this normalization, write
\[
u_N(c,w)=\eta\chi_t(c)u_O(Mc+b,w),
\]
with \(M\) invertible. Then
\[
F_{s,N}(\xi)=
\eta(-1)^{[M^{-T}(\xi+t)]\cdot b}
F_{s,O}(M^{-T}(\xi+t)).
\]
Original balance \(F_{0,O}(0)=0\) is therefore precisely
\[
\boxed{
F_{0,N}(t)=
\sum_{c\in S}\alpha(c)\chi_t(c)
+2\sum_{c\in W}\varepsilon(c)\chi_t(c)=0.
}
\tag{B}
\]

It is **not** automatically \(F_{0,N}(0)=0\). A zero at an unrelated normalized frequency does not verify balance for a particular fixed original-coordinate gauge. If additional coordinate operations are used, their full dual image of the original zero must likewise be carried explicitly.

The reduction retains (B); it never calls arbitrary modulation balance-preserving.

## 8. Complementary \(V\): one parity condition plus the unpaid cap

Let \(Y=R\times Q\), so \(|Y|=256\), and
\[
C=\{y:u(y)=0\},\qquad |C|=140.
\]
All four even-half transforms are divisible by four under §6. For every frequency \(\lambda\),
\[
\widehat u(\lambda)-\widehat u(0)
=-2\sum_{y:\lambda\cdot y=1}u(y).
\]
Divisibility by four implies every indicated half contains an even number of support points. Therefore
\[
\bigoplus\operatorname{supp}(u)=0,
\qquad
\bigoplus C=0.
\]

An actual complementary \(v\) must equal a sign \(\beta(y)\) on \(C\), and zero elsewhere. Let \(n_-\) be the number of negative \(\beta\)-signs. Since \(\bigoplus C=0\), for every \(\lambda\),
\[
\widehat v(\lambda)\equiv140-2n_-\equiv2n_-\pmod4.
\]
Thus **all 256 odd-half congruences** \(\widehat v\equiv2\pmod4\) are equivalent to the single condition
\[
n_-\text{ is odd}.
\]

Given this parity, the original odd-half Walsh requirement is exactly
\[
\boxed{
\left|\sum_{y\in C}\beta(y)\chi_\lambda(y)\right|\le14
\quad\text{for all 256 }\lambda.
}
\tag{V}
\]
The allowed values are then \(\pm2,\pm6,\pm10,\pm14\), not zero or arbitrary even numbers. This is an exact simplification, **not a construction of \(\beta\)**.

These conditions also enforce the actual selected \(T\), rather than only a formal two-half placement. In original balanced coordinates, \(u\) has 58 negative nonzero pairs. The f263 XOR identity gives
\[
\operatorname{XOR}\{x:f(x)=1\}
=
\left(\bigoplus C\right)
+\left(58+\#\{y:v(y)=1\}\pmod2\right)T.
\]
Here \(\bigoplus C=0\), and \(\#\{v=1\}=140-n_-\) is odd, so the result is \(T\). Thus \(T\ne0\) is genuinely the selected pair direction if such a complementary \(v\) is found.

Physical complementarity also enforces the full common-caller convolutions. With \(\mathcal U=\widehat u\) and \(\mathcal V=\widehat v\), for every \(\omega\),
\[
\sum_\lambda\mathcal U(\lambda)\mathcal V(\lambda+\omega)=0,
\]
\[
\sum_\lambda\left[
\mathcal U(\lambda)\mathcal U(\lambda+\omega)
+\mathcal V(\lambda)\mathcal V(\lambda+\omega)
\right]
=256^2\mathbf1_{\omega=0}.
\]
These follow from \(uv=0\) and \(u^2+v^2=1\), not independently designed spectra.

If (V), its odd parity, §6, and (B) were actually satisfied, then
\[
s(y)=u(y)+v(y),\qquad s(y+T)=u(y)-v(y)
\]
would be a genuine balanced Boolean sign function with full Walsh cap 28. **No such data are supplied or claimed in this candidate.**

## 9. Exact frontier and assurance ceiling

**Established here as author-written results:**

- The f468 transversal/bent equivalences, mathematical census, and local-lift validity.
- Complete block parametrization and forced counts (L).
- Uniform exclusion of S1’s eight-pair/no-peak lifts from the displayed \(G_3=1\) caller.
- The new exact parity/XOR criterion (C).
- The common-column dual congruence (D).
- The even-half reduction with explicit original-coordinate balance.
- The complementary odd-congruence/sign-parity reduction.

**First unproved step:** produce, or exclude uniformly, a common \(f,r\) and physical choices (L) satisfying (C), \(J=1\), **both amplitude caps**, and the carried balance zero (B). The algebraic census does not settle these coupled caps.

Even a successful even half would still leave the physical 140-support sign assignment with odd sign parity and every cap (V) unpaid. Neither stage’s feasibility follows from these reductions.

The aligned five-span actual branch remains **OPEN**. The two six-span branches, other m116/m114 callers, and the full balanced NL242 problem are not closed.

No public-source novelty, full original-book equivalence, historical \(H/G_3\) table equivalence, human/independent-family review, formal/kernel proof, fresh finite assay, or parent adoption is claimed. No held result is used. Repository materialization is left to Main; this full body is returned without a working-tree write bypass.