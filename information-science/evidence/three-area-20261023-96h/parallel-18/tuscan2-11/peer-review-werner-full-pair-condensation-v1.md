# v31-D — written review of full-spectrum pair/four-row condensation

Observed `/bin/date` before creation: **Sun Oct 25 04:38:00 PDT 2026**. Reviewer `InfoRecursiveMDS18-2` (information science), author `PhysicsResearch96h` (physics).

## 1. Verdict and exact boundary

**WRITTEN RECONSTRUCTED AT THE NAMED IMPORTS for the new full-spectrum coordinate identities and condensation P1–P10.** I find **0 FATAL / 0 MAJOR / 0 MINOR mathematical defects at this reformulation scope**.

This is **not** a proof of P11, generic Z_up>=0, E_full>=0, the other three uniform signs, or W4. The author explicitly leaves those open. Positivity of the principal blocks and intermediate metrics is not positivity of the coupled block.

The new formulas P1–P10 are reconstructed algebraically below, not accepted from author instance checks. No additional finite numerical identity remains NOT_RECONSTRUCTED within those new formulas. Explicit imports remain imports: I do not re-prove the prior p-Hodge theorem, the complete Qraw-minus-R0 coefficient certificate, or the original physical co-Choi reduction. The distinction is essential to this verdict.

**No scientific eval/interpreter, arithmetic program, symbolic program, enumeration, certificate replay, solver, CLI delegate or nested agent was used.** Only metadata SHA-256, clocks and ordinary source reading were performed. All computations displayed below are written algebra. Parent erratum v7 is binding; no historical unadmitted arithmetic has verification credit.

## 2. Source pins, full coverage and exposure

Frozen assignment v31-D, manifest SHA-256 independently observed: `73cf8654ddca55870d137b3e447355274c54a733451fa9aa3d1d6a1dc3dcf5d8`.

The single mandatory literal part was read in full, packet LF1–340, using raw ranges1–170 and171–340. These contain every declared source line:

|Label below|Source|Complete source LF|Observed SHA-256|
|---|---|---|---|
|P|`full-spectrum-pair-condensation-v1.md`|1–267|`1a814168eec30b5a8698b669fceae33145862f58c1b380d0f6b679caecf8fe98`|
|D|`resumption-arithmetic-authority-addendum-v1.json`|1–59|`82f64cf6ff936b2de9f0adcefbf0441de4674e32c78b6d7d55009484e4dc98b4`|

Literal part SHA-256 observed: `aefd9eeeb3e648890c974a0d3fd3c76f1146cc31a96636c9e0213d87e4525d0d`, matching the manifest. Raw reads exposed no truncated source lines.

Before packet reading I had only the assignment and round summaries of earlier Werner operator results. No author supplemental calculation, correctness verdict, or other review of this packet was supplied. This is a cross-domain same-harness supplied-proof reconstruction, not blind, cross-vendor, human, formal or novelty acceptance.

Additional targeted source reading, performed to check actual normalizations rather than import a prior verdict:

- `generic-upper-zero-operator-checkpoint-001-v1.md`: LF20–96,175–230, including G1–G4 and G9–G11.
- `generic-upper-zero-operator-checkpoint-001-ADDENDUM-2.md`: LF14–103, full F1–F5 normalization and resolvent-correction argument.
- `all-reference-four-residuals-v1.md`: LF219–257, physical q block and R5–R7.
- `all-reference-reduction-checkpoint-017-v1.md`: LF86–118,169–190, p-filter scope and strict-interior conclusion.

Their metadata hashes match the pins quoted in P13–17. The addendum1 hash was also checked, but its entire body was not reread. These targeted reads are not a claim to reconstruct all bodies of the imported source chain.

The operative imports are: actual filtered p/q identities G1/G9–G11; full physical raw q-plus matrix/R5–R7; Qraw>=R0 and the full S_c correction; and strict positivity of the p-principal quotient in the interior. Neither G13 nor the bare dual lift nor an arbitrary-spectrum stronger R0 comparison is imported.

## 3. The full interior charts preserve every test direction

Let x_i=c_i^2>0, sum x_i=1. Then d_i=1-x_i>0, d_ij>0, r>0 and W=e3(d)>0.

For i!=j set T_ij=t_ij and T_ii=-sum_(j!=i)x_j t_ij/x_i. Since Z_ij=c_i c_j T_ij,

`(Zc)_i=c_i sum_j x_j T_ij=0`.

Conversely, every Zc=0 determines all twelve t_ij uniquely by dividing its off-diagonal entries by c_i c_j; its diagonal is then forced by that row equation. Thus the chart is a complex-linear isomorphism onto the full p12 quotient. It does not impose transpose symmetry or real test vectors.

Similarly U_ij=sqrt(2)c_i c_j v_ij, i<j, with U_ji=U_ij and zero diagonal, parametrizes every complex transpose-symmetric zero-diagonal U. Its physical normalized q-plus coefficients are

`q_ij=d_ij U_ij=sqrt(2)c_i c_j d_ij v_ij`.

This last sqrt(2) must remain in both the cross block and the raw q congruence.

## 4. Direct reconstruction of every H and B entry

Write `s_i=sum_(j!=i)x_j t_ij`. The imported row-variance and swap identities give

`<Z,rho'Z>=sum_(i!=j)d_i^2 x_i x_j |t_ij|^2`
`             +sum_i(r-d_i x_i)|s_i|^2`
`             +r sum_(i!=j)x_i x_j conj(t_ij)t_ji`.

The last sum is real because reverse ordered terms are conjugate pairs; it is not assumed nonnegative. Reading the coefficient matrix yields:

- diagonal: `d_i^2 x_i x_j+(r-d_i x_i)x_j^2`;
- distinct slots in one directed row: `(r-d_i x_i)x_j x_t`;
- reversed directed edge: `r x_i x_j`;
- no other entries.

Thus H is exactly P58–61, retaining the skew/swap contribution and all row cross terms.

For the cross block, the old variable z is `z=sqrt(2)v`. G11 therefore becomes

`-2 Re Gamma(T,v)-Re sum_(i<j)x_i x_j conj(d_i t_ij+d_j t_ji)v_ij`.

The row variance bilinear is

`2Gamma(T,v)=sum_i d_i x_i [d_i sum_(j!=i)x_j conj(t_ij)v_ij`
`                              -conj(s_i)sum_(t!=i)x_t v_it]`.

Remembering that the joint form is `2Re(t^dagger Bv)` gives, from the Gamma term,

- same edge: `-d_i^2 x_i x_j/2+d_i x_i x_j^2/2`;
- another edge {i,t}: `d_i x_i x_j x_t/2`.

The remaining edge term adds `-d_i x_i x_j/2` to the same edge. Summing gives

`B_(ij,{i,j})=-d_i x_i x_j(1+d_i-x_j)/2`,

`B_(ij,{i,t})=d_i x_i x_j x_t/2`,

and zero for edges not incident to i. This derives the factor1/2 and sign of every entry in P66–68 for arbitrary complex tests.

## 5. Full A, all raw corrections, and the Stieltjes assertion

Put `D_qphys=(5/4)I-Tq` to distinguish this imported physical raw block from the later D_q. The physical coefficient vector is `q=sqrt(2)W_e v`, where `(W_e)_ij=c_i c_j d_ij`. Hence

`A=2W_e D_qphys W_e`.

Its physical diagonal is `3/2-d_ij d_kl/W`. Its shared-edge entry is `-c_j c_t/(4d_jt)`. Direct multiplication gives exactly

`A_(ij,ij)=x_i x_j d_ij^2(3-2d_ij d_kl/W)`,

`A_(ij,it)=-x_i x_j x_t d_ij d_it/(2d_jt)`.

Disjoint-edge entries vanish. Every shared-edge coupling is retained, including all cross terms that would be lost by replacing S_c with its diagonal.

The old compatible-square coordinates used `U_ij=c_i c_j z_ij`, with q pivot `(1/2)z^dagger[M+C^dagger C+2S_c]z`. Substituting z=sqrt(2)v gives

`A=M+C^dagger C+2S_c`,

precisely the new normalization. Thus the factor2 in front of S_c is correct and the full raw correction, not R0 alone, is used.

Equivalently `K_full=2D_qphys` has the entries in P109: nonpositive shared-edge off-diagonals and zero disjoint-edge entries. To check its lower bound without a Hilbert-Schmidt factor error, let F=L_D U. Its off-diagonal edge vector is `F_edge=sqrt(2)W_e v`, while the symmetric Hilbert-Schmidt norm doubles the edge sum. Consequently

`R0(U)=<F,K_c F>_HS/4=v^dagger W_e K_c W_e v`.

The imported Qraw>=R0 therefore implies `K_full>=K_c>=I` by congruence with invertible W_e. So A>0 and K_full is positive Stieltjes.

For completeness, inverse entrywise nonnegativity needs no scientific computation: if K is a real positive-definite Z-matrix, choose s at least its largest eigenvalue and write K=sI-C, C entrywise nonnegative. Every eigenvalue of C/s lies in[0,1), and

`K^(-1)=(1/s)sum_(m>=0)(C/s)^m`

is entrywise nonnegative. This proves the claimed inverse sign. It does **not** compare K_full^(-1) and K_c^(-1) entrywise; no such claim is made in the source.

## 6. Positive elementary edge pivots and exact signed update

For each pair i,j, the two-by-two block has positive diagonal and determinant

`(x_i x_j)^2(d_i^2 d_j^2-r^2)`.

Because the other two positive terms remain in sum_k1/d_k,

`r<d_i d_j/(d_i+d_j)`.

Also `d_i+d_j=2-x_i-x_j>1`, so `r<d_i d_j`. Thus every Delta_ij>0. The usual two-by-two inverse is exactly P138, including its negative off-diagonal entries. This is uniform over the strictly positive simplex.

With V_(ij,k)=delta_ik x_j, the ordered-row diagonal of `V S_row V^dagger` is `(r-d_i x_i)x_j^2`; its off-diagonal entries within the same directed row are `(r-d_i x_i)x_j x_t`. It has no reversed-edge contribution. E_0 supplies exactly the remaining diagonal and reversed-edge terms. Therefore

`H=E_0+V S_row V^dagger`.

For B, `(V K_row R)_(ij,{i,j})=d_i x_i x_j^2/2`, and its other incident entries are `d_i x_i x_j x_t/2`. Subtracting L_0 gives the diagonal edge entry derived in section4. Hence

`B=-L_0+V K_row R`.

The update S_row is signed. None of this establishes S_row>=0, and removing it would change the target.

## 7. G and N_row: positivity uses only the p-principal import

The four columns of V have disjoint nonempty supports and hence are independent. Since E_0>0,

`G=V^dagger E_0^(-1)V>0`.

Reading its entries from the elementary inverse gives

`G_ii=sum_(j!=i)x_j d_j^2/(x_i Delta_ij)`,

`G_ij=-r/Delta_ij`.

Thus G is also positive Stieltjes. The inverse-sign argument above applies. This assertion is independent of the coupled target sign.

Here is the constrained-minimum proof in full. For any u, let

`t_u=E_0^(-1)V G^(-1)u`.

Then V^dagger t_u=u. Every other feasible t has t=t_u+z, V^dagger z=0, and `z^dagger E_0 t_u=z^dagger V G^(-1)u=0`. Thus

`min_(V^dagger t=u)t^dagger E_0t=u^dagger G^(-1)u`.

The signed update has constant value u^dagger S_row u on that constraint, so

`min_(V^dagger t=u)t^dagger Ht=u^dagger(G^(-1)+S_row)u`.

The separately imported p-Hodge result is H>0 on the full p12 interior chart. For nonzero u the feasible minimizer t_u is nonzero. Its H energy is strictly positive, giving N_row>0. This proof does not assume joint PSD, A-B^dagger H^(-1)B>=0, or S_row>=0. N_row is not claimed to be Stieltjes, nor is any entrywise inverse sign assigned to it.

## 8. Full constrained condensation, including the forcing sign

Using u=V^dagger t, write the entire joint form as

`t^dagger E_0t-2Re(t^dagger L_0v)+u^dagger S_row u`
` +2Re(u^dagger K_row Rv)+v^dagger Av`.

Shift t by `t_0=E_0^(-1)L_0v`. Then V^dagger t_0=Yv and completing the E_0 square gives

`v^dagger D_qv+(t-t_0)^dagger E_0(t-t_0)`
` +u^dagger S_row u+2Re(u^dagger K_row Rv)`.

The constraint on the shifted variable is `V^dagger(t-t_0)=u-Yv`. Section7 gives exactly the first constrained minimum displayed at P205–209, with unique minimizer

`t=t_0+E_0^(-1)V G^(-1)(u-Yv)`.

Expanding its u-dependent part yields

`u^dagger N_row u-2Re(u^dagger Fv)`
` +v^dagger(D_q+Y^dagger G^(-1)Y)v`,

where `F=G^(-1)Y-K_row R`. In particular the cross sign is minus; minimizing gives `u=N_row^(-1)Fv`. Its value is

`v^dagger[D_q+Y^dagger G^(-1)Y-F^dagger N_row^(-1)F]v`.

On the other hand, direct minimization of the same original joint form in all twelve t directions, using H>0, gives

`v^dagger[A-B^dagger H^(-1)B]v`.

Equality for every complex v proves P9 as a Hermitian-matrix identity. The constructive first expression uses only the six elementary edge inverses and the two positive four-by-four inverses. No inverse of signed S_row is introduced. No q direction or raw cross term is dropped.

## 9. Actual Schur equivalence and physical factor2

Because A>0, minimizing the original joint form over all v gives its p-side residual `H-BA^(-1)B^dagger`. By the imported full-Qraw definition and the bijective q chart, this is exactly the condition `E_full,c(Z)>=0 for every Zc=0`.

Because H>0, positivity of that same joint form is also equivalent to `A-B^dagger H^(-1)B>=0`. Together with P9 this proves both equivalences in P10. This uses positivity of pivots only to justify the equivalences; it does not prove either residual positive.

For the physical normalization, let J_p denote the invertible interior p parametrization **including the pre-existing real local p filter**. It is important not to identify rho' with the unfiltered physical rho. An invertible p-only congruence leaves the q Schur form unchanged. The q change is exactly `q=sqrt(2)W_e v`. Thus the q Schur form transforms as

`Z_hat=(sqrt(2)W_e)^dagger Z_up(sqrt(2)W_e)=2W_e Z_up W_e`.

The canonical R7 uses rho_reg=rho+Pref; the addition does not affect this subtraction because the physical upper cross columns are reference-perpendicular. This is precisely the imported R5–R7 scope. No q coefficient rescaling or p-filter omission remains hidden in P240.

## 10. Scope audit, authority disclosure and unresolved target

P247–255 correctly identifies the first unproved sign as

`D_q+Y^dagger G^(-1)Y >= F^dagger N_row^(-1)F`

for every strictly positive spectrum. This is the coupled residual, not a consequence of positive E_0, G, N_row and A. As a purely logical illustration, positive pivots H=A=I do not stop an off-diagonal block B=2I from producing a negative Schur residual; principal positivity alone cannot close a coupled sign.

The source does not label D_q positive, invert a signed S_row, apply inverse-order monotonicity across it, discard S_c cross terms, revive G13, or reuse the false bare dual lift. It does not substitute a selected-spectrum or stronger-R0 theorem for the full target. These potential major failure modes are avoided.

D1–59 is a disclosure of earlier computations and parent-caused admission error, not a scientific proof premise. I read the entire disclosure but did not replay, independently validate, or attest exit/resource metadata for any listed call. No booleans or positive pivots from that history enter this review's derivation.

**Exact residual obligations:** P11 remains NOT_PROVED here; so do generic Z_up, E_full, F_up, F_low, Z_low, the full asymmetric co-Choi route and unrestricted rank<=2 W4. No negative spectrum or physical Werner witness is supplied. These are explicitly unproved targets, not incomplete finite identities being silently called PASS.

All charts/inverses above are strictly interior. This review supplies no sparse-boundary inverse, pseudoinverse-continuity result, or new endpoint theorem. A future uniform physical joint-PSD proof could use the already named physical-continuity interface; the present reformulation alone cannot do so.

**Final disposition:** the entire new P1–P10 reformulation is reconstructed in writing at the enumerated prior imports, with no substantive defect found. This supports only that scoped written identity result, not the final target sign, independent computational verification, formal acceptance or novelty.
