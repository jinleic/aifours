# Checkpoint 004 — both co-Choi signs have a uniform gap on the 32 extremal-charge dimensions

Before-creation clock observed: **2026-10-23T14:23:42-07:00**. Physics-1 / W4. Status: **CANDIDATE written proof**, no scientific execution. This continues the single two-pair angular obligation; it is not an additional problem or a full GS result.

## 1. Exact result

For `eta_t=Omega_A+t Omega_B`, t>=0, let A={0,1}, B={2,3}. On the16-dimensional sector

`E_+=span{|a,b,c,d>:a,c in A; b,d in B}`,

and its16-dimensional physical-interchange sector E_-,

**`(C_B-S_eta)|_(E_+ direct_sum E_-) >= I/8`,**

**`(C_B+S_eta)|_(E_+ direct_sum E_-) >= I/8`.**

Thus these entire32 dimensions are never an angular obstruction. The result is uniform in t, not a finite parameter check.

Together with checkpoint002's complete eight-dimensional fixed block, this leaves216 nontrivial-complement dimensions requiring analysis. Its invariant minus sign is already closed by checkpoint003, but its invariant plus sign still requires its exact interval; neither closure is silently extended to the full space.

## 2. Why these are exact reducing sectors

Let the first physical ququart transform by `U_A direct_sum U_B` and the second by its coefficientwise conjugate. Eta_t is invariant. On the co-Choi space this representation acts simultaneously on input/output copies. The independent central phases count the number of A labels in positive slots1,3 minus the number in negative slots2,4. E_+ and E_- have charges+2 and-2, respectively, with no other possible label patterns of those charges. Thus each is an exact reducing sector for C_B and S_eta. No matrix entry was discarded by threshold or numerical sparsity.

Let F_A swap positions1,3 and F_B swap positions2,4. On E_+ these are commuting self-adjoint involutions. The fixed physical co-Choi matrix is

`C_B=(I-F_A/2)(I-F_B/2)`.

## 3. Full reference inverse and disappearance of only the rank-one correction

Use s=t^2 and

`a=1+2s`, `b=2+s`, `k=1/a`, `l=s/b`, `L=k+l`.

The full reference compression has

`A_eta=D+|eta><eta|/4`,

where D is a on A⊗A, b on B⊗B and `3(1+s)/2` on mixed pairs. With H=D^-1 eta,

`A_eta^-1=D^-1-|H><H|/[4+2L]`.

Here H has coefficients1/a on the A diagonal and t/b on the B diagonal; `<eta,H>=2L`.

For a in A,b in B,

`L_ab=-(t E_ab⊗I+I⊗E_ba)/2+|ab><eta|/4`.

A direct application to H gives

`L_ab H=[<eta,H>/4-(k+l)/2]|ab>=0`.

Therefore the rank-one inverse correction contributes zero to every co-Choi entry whose input pair is mixed A⊗B, including the entire E_+ sector. This is an **exact cancellation**, not replacing A_eta^-1 by a truncated inverse on a chosen coordinate subspace.

## 4. The complete sector operator S_eta

For a,c in A and b,d in B,

`L_ab†|cd>=-(t/2)delta_(ac)|bd>-(1/2)delta_(bd)|ca>`

`                +(1/4)delta_(ac)delta_(bd)eta`.

Use this expression in the reversed co-Choi contraction

`S_((ab,cd),(ef,gh))=<L_ef†cd,A_eta^-1 L_ab†gh>`.

The rank-one correction vanishes by Section3. The D-inverse contractions group as follows:

| Product class | Operator contribution |
|---|---|
| B⊗B negative term with itself | `(l/4)F_A` |
| A⊗A negative term with itself | `(k/4)F_B` |
| Negative terms with eta, both orders | `-(k+l)F_A F_B/4` |
| eta with itself, using `<eta,D^-1eta>=2L` | `+L F_A F_B/8` |

The cross product between A⊗A and B⊗B is zero because D^-1 is diagonal across the groups. Consequently the **entire**16-dimensional sector operator is

**`S_eta=(l/4)F_A+(k/4)F_B-(L/8)F_A F_B`.**

There are no additional terms. At t=1 this reduces to `(F_A+F_B-F_A F_B)/12`, consistently with the full uniform-reference identity, but that point is not used to prove the family formula.

## 5. Uniform spectral bounds in all four swap sectors

The pair parameters satisfy k,l>=0 and

`L=k+l=1-3kl<=1`.

For joint swap eigenvalues epsilon_A,epsilon_B in{+1,-1}, the C_B and S_eta scalars are

`C=(1-epsilon_A/2)(1-epsilon_B/2)`,

`S=(l/4)epsilon_A+(k/4)epsilon_B-(L/8)epsilon_A epsilon_B`.

Thus:

- (++): C=1/4, S=L/8 in[0,1/8]; both signs are at least1/8.
- (+-): C=3/4, S=(3l-k)/8 has absolute value at most3/8; both signs are at least3/8.
- (-+): C=3/4, S=(3k-l)/8 likewise has absolute value at most3/8; both signs are at least3/8.
- (--): C=9/4, S=-3L/8; both signs are at least15/8.

The multiplicities are9,3,3,1 because a two-dimensional pair has symmetric/antisymmetric dimensions3,1. They exhaust all16 dimensions of E_+. Interchanging the two physical factors gives E_- and exchanges k,l, leaving the same lower bounds. This proves the stated32-dimensional conclusion.

## 6. Exact remaining global obligation

The central charges have dimensions16,64,96,64,16 for charges2,1,0,-1,-2. This follows by choosing A-label occupancy independently in the two positive and two negative slots, each selected group assignment contributing16 coordinate states. The eight-dimensional fixed subspace of checkpoint002 lies in charge zero. Removing it and the two extremal-charge sectors leaves

`64+64+(96-8)=216`

dimensions, with their matrix blocks still to be reconstructed and controlled. The fixed-block plus sign is also still unresolved over the whole t interval. The principal quartic is only necessary and is not promoted to sufficiency by this sector result.

All work here is written algebra on the physical model. No exact program, solver, root search, finite matrix test or new scientific GO was used. W4 and the complete angular criterion remain open.
