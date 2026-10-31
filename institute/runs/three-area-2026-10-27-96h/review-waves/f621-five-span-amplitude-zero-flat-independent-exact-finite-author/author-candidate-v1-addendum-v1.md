# Addendum to f621 author-candidate-v1: positive identity and coordinate-label clarification

**AUTHOR, UNADOPTED; scientific code NOT RUN.** This is an additive clarification, not a modification or execution of the retained candidate. The same acceptance and excluded-source boundaries apply.

## Written derivation of the explicitly specified positive array

Let `c=(a,b)` with `a=(c0,c1,c2)` and `b=(c3,c4,c5)`, and let `Q(c)=a·b` over `F2`. Define `s(c)=(-1)^Q(c)`, `A={c:a=(1,0,0)}`, and `x=s(1-1_A)`. Let `K={(a,0):a in F2^3}`, `t=(0,(1,0,0))`, and `Z=t+K`. For any frequency `xi=(u,v)`, summing first over `a` gives `W(s)(xi)=8(-1)^(u·v)`. On `A`, `s(c)=(-1)^b0`, so directly

`W(s 1_A)(u,v)=8(-1)^u0 1_{v=(1,0,0)}=8(-1)^Q(xi) 1_Z(xi)`.

Hence `W(x)=8z` with `z(xi)=(-1)^Q(xi)(1-1_Z(xi))`. Walsh-squaring gives `W(z)=8x`. Both x and z are explicit integer ternary arrays: x has eight zeros and 56 entries of magnitude one, so `sum x²=56`, but its 56 odd entries violate the actual graph-support count 16. This is a legitimate positive identity control, not an actual original caller.

The dual zero-flat direction is `K`, its primal annihilator is `L=K^perp={(0,b):b in F2^3}`, and `t=8` is a zero. From `W(A_x)=W(x)^2=64(1-1_Z)` and `W(1_Z)(c)=8(-1)^(t·c)1_L(c)`, inversion gives `A_x(c)=64 delta_0(c)-8(-1)^(t·c)1_L(c)`. This written argument is separate from, and not an observed execution of, the candidate checker.

## Output interpretation and runtime prerequisite

The JSON field named `physical_coordinate_S_mask_hex` in the retained source represents the **actual graph support expressed in the `(ell,h0,j0,j1,b0,b1)` basis** specified in the candidate, not the integer-index mask in the old `(h,d)` coordinate order. The checker explicitly converts and compares the two support sets, but does not output the old-order mask. Do not interpret the field name as evidence that it outputs old `(h,d)` mask bytes. The `L` mask is likewise in the stated six-bit basis.

`int.bit_count()` requires Python 3.10 or later. Parent execution therefore needs a suitable already-installed `python3` (no installation is authorized), static source review, resource admission and a one-shot GO. The source's 55-second budget remains unmeasured; the present written proof is not a timing or passing-test receipt.
