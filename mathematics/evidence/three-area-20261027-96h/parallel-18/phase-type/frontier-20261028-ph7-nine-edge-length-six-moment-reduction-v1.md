# A five-variable exact reduction for the remaining length-six connector cases

Status: **WRITTEN, with the independent coefficient identity explicitly checked in the owner's SymPy kernel; not yet independently reviewed**. This is a necessary semialgebraic system, not a claim that the system is empty. It replaces an unconstrained nine-rate spectral search by a smaller, exact all-rate task. The degree-two coefficient identity below was checked by symbolic expansion of the full directed-cycle determinant; no selected PH state or optimizer result is used as proof.

## Graph and variables

Consider the graph of `frontier-20261028-ph7-nine-edge-omitted-rate-obstruction-v1.md`, but suppose its connector cycle has length **six**. Its two disjoint directed triangles have positive diagonal rates `alpha_1,alpha_2,alpha_3` and `beta_1,beta_2,beta_3`; the singleton has rate `x>0`. Scale the repeated eigenvalue to `-1 +/- i*sqrt(8/9)`. Define

`A=alpha_1+alpha_2+alpha_3`, `B=beta_1+beta_2+beta_3`,

`a2=alpha_1*alpha_2+alpha_1*alpha_3+alpha_2*alpha_3`, `b2=beta_1*beta_2+beta_1*beta_3+beta_2*beta_3`,

`a3=alpha_1*alpha_2*alpha_3`, `b3=beta_1*beta_2*beta_3`.

Let the triangle transition products be `w_A,w_B>0`. The row-generator property gives `w_A<a3`, `w_B<b3`. Put `r_A=a3-w_A>0`, `r_B=b3-w_B>0`. We may exchange the names of the two triangles when deriving these coefficient conditions and suppose `A<=B`.

The characteristic polynomial has the form

`det(yI-G)=D(y)*(y^2+p*y+q)`,

`D(y)=y*((y+1)^2+8/9)^2`,

where `p,q>0`: irreducibility gives the unique simple zero eigenvalue and all other eigenvalues have negative real parts. This factorization is spectral only; PH input/exit matching is an additional condition not used here.

Define the following expressions in `A,B,x,a2,b2`:

`p=A+B+x-4`,

`q=a2+b2+A*B+x*(A+B)-4*(A+B+x)+74/9`,

`J=a2*B+A*b2+x*(a2+b2+A*B)-4*(a2+b2+A*B+x*(A+B))+(74/9)*(A+B+x)-28/3`,

`K=a2*b2+x*(a2*B+A*b2)-(70/9)*(a2+b2+A*B+x*(A+B))+(212/9)*(A+B+x)-1007/27`,

`T=(289/81)*p+(68/9)*q`.

Then the three exact necessary equalities are

`J=-r_A-r_B`,

`K=-r_A*(B+x)-r_B*(A+x)`,

`T=r_A*(b2+x*B)+r_B*(a2+x*A)+x*a2*b2`.

The first two follow from the `y^4` and `y^3` coefficients. The third is the `y^2` coefficient. The connector 6-cycle contributes only in degrees `y^1,y^0`; the product of the two disjoint triangle cycles contributes `w_A*w_B*(y+x)` and likewise has no `y^2` contribution. This distinction is essential. The check expanded

`prod_v(y+u_v)-w_A*(y+x)*prod_{v in B}(y+u_v)-w_B*(y+x)*prod_{v in A}(y+u_v)+w_A*w_B*(y+x)`

and verified its `y^2` coefficient equals the right side above identically after substituting `r_A=a3-w_A`, `r_B=b3-w_B`. The omitted 6-cycle term cannot alter this coefficient.

## Five-variable necessary system when A<B

Let `t=B-A>0`, and set

`R_A=-K+J*(A+x)`, `R_B=K-J*(B+x)`.

The first two equalities force `R_A=t*r_A>0`, `R_B=t*r_B>0`. Since for three positive rates `(a2)^2 >= 3*A*a3` and `(b2)^2 >= 3*B*b3`, their positive triangle weights further imply the **strict** inequalities

`P=a2^2*t-3*A*R_A>0`, `Q=b2^2*t-3*B*R_B>0`.

The `y^2` equality becomes the single polynomial equation

`L=t*(T-x*a2*b2)-R_A*(b2+x*B)-R_B*(a2+x*A)=0`.

Thus every graph realization must satisfy `p,q,R_A,R_B,P,Q>0` and `L=0`, together with

`A>0`, `B>A`, `x>0`, `0<a2<=A^2/3`, `0<b2<=B^2/3`.

Equivalently use five variables `A,t,x,xi,eta`, with `B=A+t`, `a2=A^2*xi/3`, `b2=B^2*eta/3`, `0<xi,eta<=1`. This relaxation loses the full three-rate product-discriminant constraints, the connector-cycle coefficient, and PH numerator matching; infeasibility of this system would exclude the length-six graph, but feasibility would not construct it. The optional separately written supported-five-path result would also impose its stronger positive lower bound on `p`; it is not needed for the equalities above.

When `A=B`, division by `t` is invalid. The first two equalities instead require `K=J*(A+x)` and `J=-(r_A+r_B)<0`; the `y^2` equality remains as displayed, with `0<r_A<a2^2/(3A)` and `0<r_B<b2^2/(3A)`. This branch is not covered by the five-variable `A<B` equations and must be analyzed separately.

The reduction is necessary, not sufficient; no global infeasibility, 8/9 decision, novelty, executable-certificate replay, independent audit, or theorem adoption is asserted. The critical PH7 caller additionally depends on the separate nine-edge graph-template manuscript and its pending capacity/overlap-budget inputs.
