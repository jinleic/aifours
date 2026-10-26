# At most three arbitrary ME4 ray terms: nonorthogonality does not escape the scalar-completion obstruction

Actual `/bin/date` before writing: **Sun Oct 25 07:27:40 PDT 2026**. Owner PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE, based on an explicitly supplied parent lead; independent reconstruction and parent disposition pending.** No scientific eval/interpreter/arithmetic program/enumeration/certificate replay/solver was used. Metadata hashes/clocks only. Parent erratum v9 and HOLD v2 remain binding.

## 1. Exposure and successor scope

Read parent evidence erratum v9 FIRST, then ALL38LF of the parent-supplied `ppt-three-ME-nonorthogonal-written-lead-v1.md`, observed SHA-256 `fa727f533812e42495f54c5f0cbaad9ccb93310934ca6dc219e65e4363e945ae`. The preceding exposure ACK is `three-ME-nonorthogonal-lead-ack-v1.json`.

The closest-eigenphase-pair argument, principal-Gram estimate and proposed positive partial-transpose margin were supplied by the parent. This manuscript reconstructs that chain rather than claiming independent discovery, blind review, preregistration or acceptance from parent confidence. The older orthogonal packet and every earlier review/disposition stay frozen at their actual narrower scopes; this is not a retrospective expansion of their acceptance.

**Reconstruction outcome:** the proposed chain is valid, including nonorthogonal, repeated and linearly dependent rays. The full-complex Gram iff requires no independence or orthogonality. The new phase-gap argument replaces the old trace-zero assumption rather than quietly retaining it.

## 2. Exact theorem and normalization

Let0<=m<=3, let U_r be arbitrary4 by4 unitaries, and define

```
Phi_r=vec(U_r)/2,
p_r>=0,
Q=sum_(r=1)^m p_r P(Phi_r),
W=lambda I16-Q, lambda real.                            (1)
```

No Hilbert–Schmidt orthogonality, pairwise distinctness, linear independence or commutation is assumed. The coefficient-matrix/vectorization convention is

```
<Phi_r,vec(C)>=(1/2)Tr(U_r* C),
||Phi_r||^2=Tr(U_r*U_r)/4=1.                             (2)
```

Thus Q is PSD and Tr(Q)=sum p_r, even if several projectors coincide. In particular Q=0 iff all weights are zero. The p_r are **given conic weights**, not asserted eigenvalues of a nonorthogonal sum. The actual rank of Q or negative spectral part of W need not equal m.

**Theorem.** If W is nonnegative on EVERY complex Schmidt-rank-at-most-two vector, then W^Gamma>=0. If Q is nonzero, W^Gamma is in fact bounded below by a strictly positive scalar multiple of I16:

- if exactly one weight p1 is positive, `W^Gamma >= (p1/4)I16`;
- if at least two are positive, order p1>=p2>=p3>=0, taking p3=0 when needed. Then

```
W^Gamma >= delta I16,
delta=[sqrt(p1^2+p2^2)-p3]/4>0.                          (3)
```

Consequently no such scalar completion detects any4 by4 PPT state. Maximal entanglement, scalar completion and at most THREE contributing ray terms remain essential hypotheses.

## 3. Complete complex Gram criterion without an orthogonal-ray assumption

First, two-block-positivity implies lambda>=0: for any normalized product ket u, its expectation is `lambda-<u,Qu>` and Q>=0. So allowing lambda real in(1) creates no missing negative-lambda branch.

For any complex4 by2 isometry S, put P=S S* and define

```
H_rs(P)=sqrt(p_rp_s)/4 Tr(U_r* P U_s).                   (4)
```

The exact criterion is

```
W is two-block-positive
 iff lambda>=0 AND H(P)<=lambda I_m
     for EVERY complex rank-two orthogonal projector P. (5)
```

For m=0 the Gram condition is empty and the explicit lambda>=0 is necessary; it is not silently dropped.

Proof. Every complex coefficient matrix C of rank at most two has C=SZ, by extending its column space to a two-plane. Let z_j be the columns of Z, and let V_j have columns

```
v_jr=sqrt(p_r)/2 S* U_r e_j.
```

Then

```
h_r=sqrt(p_r)/2 Tr(U_r* C),
h=sum_j V_j* z_j,
||C||_F^2=||Z||_F^2,
sum_j V_j*V_j=H(P).                                    (6)
```

Even for nonorthogonal or repeated rays, `<vec(C),Qvec(C)>=sum_r|h_r|^2` because Q is DEFINED as that projector sum. No basis decomposition of Q is needed. The linear map L:Z->h has Gram L L*=H, so its exact squared norm is lambda_max(H). Thus H<=lambda I gives all required nonnegative expectations.

Conversely, if Hv=gv for a unit vector v and g>lambda>=0, choose z_j=V_jv. Then `||Z||_F^2=g`, h=gv and the witness expectation is `g(lambda-g)<0` on the actual nonzero rank-at-most-two matrix C=SZ. This proves necessity. Zero weights or dependencies may make H singular, but no inverse or independent-column hypothesis occurs anywhere. Changing S within the same plane leaves(4) unchanged.

Its diagonal is always

```
H_rr=(p_r/4)Tr(U_r* P U_r)=p_r/2.                        (7)
```

This uses only Tr(P)=2 and unitary invariance of trace, not orthogonality of different U_r.

## 4. Local-unitary and relative-unitary conventions

Suppose p2>0. A left unitary change C->U1* C sends each ray matrix U_r to U1*U_r, so the first becomes I and the second becomes

```
V=U1*U2.
```

This is a physical local unitary on Alice. Diagonalize V=S0 diag(eta1,...,eta4)S0*. The simultaneous coefficient change `C->S0* C S0` sends ray matrices in the same way, keeps the first at I and diagonalizes the second. It is implemented by the local unitary `S0* tensor S0^T`; both factors are unitary. Ranks, Frobenius norms and the full quantifier over complex two-planes are preserved. All other ray matrices remain arbitrary unitaries: no simultaneous diagonalization of the third ray is asserted.

One can alternatively avoid changing coordinates. Cyclicity gives

```
Tr(U1* P U2)=Tr(P U2 U1*).
```

Thus in the ORIGINAL Alice coordinates the corresponding eigenplane is an eigenplane of U2U1*, whereas AFTER the left reduction it is an eigenplane of U1*U2. These relative unitaries are unitarily similar. This distinction prevents an unnoticed projector-orientation error; the parent's proposed reduction is valid.

Local unitary conjugation also preserves partial-transpose eigenvalue bounds: if W'=(A tensor B)W(A tensor B)*, then `W'^Gamma=(A tensor conjugate(B))W^Gamma(A tensor conjugate(B))*`. A scalar lower margin proved after reduction therefore transfers unchanged to the original operator.

## 5. The closest cyclic eigenphase pair, including repeated eigenvalues

The unitary V has an orthonormal eigenbasis and four unit-modulus eigenvalues, counted with multiplicity. Choose phases

```
0<=theta1<=theta2<=theta3<=theta4<2pi,
eta_j=exp(i theta_j).
```

The four NONNEGATIVE cyclic gaps are

```
theta2-theta1, theta3-theta2, theta4-theta3,
theta1+2pi-theta4.
```

Their sum is2pi, so one gap d is at most pi/2. The two corresponding spectral indices are distinct, including the wraparound pair4,1. Even when their eigenvalues agree, the associated eigenvectors can be chosen orthonormal; repeated phases give d=0, not a failure of rank two.

Let P project onto these two eigenvectors in the reduced coordinates. Then

```
|Tr(PV)|^2=|eta_i+eta_j|^2
          =2+2cos d>=2,
|Tr(PV)|>=sqrt2.                                       (8)
```

The same identity applies to the wraparound gap modulo2pi. No trace-zero, orthogonality of the original ME rays, distinct-phase or eigenvalue-separation hypothesis is used. This is the precise replacement for the older six-pair trace-zero argument.

## 6. Principal Gram eigenvalue and the strengthened necessary threshold

At this actual complex rank-two projector P, the principal Gram block for the first two ray TERMS is

```
G2=[ p1/2, sqrt(p1p2)Tr(PV)/4;
     sqrt(p1p2)conj(Tr(PV))/4, p2/2 ].                  (9)
```

The full H may contain arbitrary correlations with a third, possibly dependent ray. Nevertheless its largest eigenvalue is at least that of G2: extend any two-component unit vector by a zero third component in the Rayleigh quotient. This needs no independence assumption and makes no assertion about signs of the third correlations.

The exact larger eigenvalue of(9) is

```
[p1+p2+sqrt((p1-p2)^2+p1p2|Tr(PV)|^2)]/4.
```

By(8) and the universal condition(5),

```
lambda >= [p1+p2+sqrt(p1^2+p2^2)]/4.                    (10)
```

The factor inside the root comes from TWO times p1p2: `(p1-p2)^2+2p1p2=p1^2+p2^2`. This checks the normalization and factor of four in the supplied lead. It is a necessary lower threshold; it is NOT asserted to be the exact positivity threshold for all triples.

## 7. All-PPT bound and every zero-weight case

For every unitary U, with F the swap operator,

```
P(vec(U)/2)^Gamma=(U tensor I)F(U* tensor I)/4<=I16/4.
```

Therefore, with no orthogonality or independence,

```
Q^Gamma<=(p1+p2+p3)I16/4,
W^Gamma>=[lambda-(p1+p2+p3)/4]I16.                       (11)
```

For p2>0, insert(10) to obtain exactly(3). Ordering gives `sqrt(p1^2+p2^2)>p2>=p3`, since p1>0, hence the margin is strictly positive. Repeated identical rays cause no cancellation: Q is a sum of PSD terms and its trace is the sum of the weights. Singular full Gram matrices likewise do not affect the principal-block argument.

If p2=0 but p1>0, all other weights are zero. A maximally entangled unit ray has four Schmidt coefficients1/2. Keeping any two Schmidt terms and normalizing produces a rank-two unit vector with squared overlap1/2. Two-block-positivity gives `lambda>=p1/2`; (11) yields `W^Gamma>=p1 I16/4>0`, as stated.

If every weight is zero, Q=0 and W=lambda I16. Two-block-positivity is exactly lambda>=0, so W^Gamma>=0; strict positivity is not asserted at lambda=0. This also covers m=0. These cases include a missing third ray, weights equal to zero, repeated rays, and arbitrary linear dependence without introducing an artificial positive-weight term.

For any PPT density matrix rho,

```
Tr(Wrho)=Tr(W^Gamma rho^Gamma)>=0,
```

and is at least the positive margin when Q is nonzero. Thus there is no PPT-negative target once the sound universal rank-two condition is imposed.

## 8. Scope correction, history and the genuine remaining escape

The full supplied chain is reconstructed; no failed implication was found. This successor removes orthogonality ENTIRELY and strengthens the uniform margin. For three unit weights the necessary threshold is `(2+sqrt2)/4` and the lower partial-transpose margin is `(sqrt2-1)/4`, uniformly over all triples. The exact threshold may be higher; for coincident rays the bound need not be sharp.

This does not change the historical scope of the older orthogonal manuscript, its reviews or parent dispositions. The broader theorem is a NEW supplied-lead WRITTEN candidate until separately reconstructed. The parent lead is not itself acceptance, and this is not a blind or independently discovered proof.

**Nonorthogonality alone is NOT an escape.** A subtracted Q admitting a conic representation by at most THREE normalized ME4 ray projectors cannot produce PPT detection under a scalar positive completion if the resulting W is universally rank-two nonnegative. The statement is about the number of contributing ray TERMS, not necessarily the rank of Q or the number of its spectral negative eigenvalues.

Possible next mechanisms must leave at least one of these remaining hypotheses: at least FOUR contributing ME ray terms, nonmaximally entangled rays, or a non-scalar/anisotropic positive completion. None of those possibilities is asserted viable or solved. Four dependent terms may still span a low-dimensional space; this theorem must not be inflated into a rule that negative spectral rank must be at least four.

Unrestricted P44 remains unanswered. The earlier x1111 SN=2, single-Bell D-type and two-Bell cyclic results retain only their own v8/v9-qualified histories; old21table remains unreconstructed, N4 remains UNKNOWN/incomplete with historical exit unestablished, no retry. They are not proof premises here.

Correctness: author-WRITTEN reconstruction of a supplied lead, cross-domain review and parent disposition pending. No scientific execution, proof-assistant/kernel, cross-vendor/human or novelty acceptance is claimed. No new GO is requested; the scientific HOLD remains binding.
