# CURRENT P44 CONSOLIDATION v25 — PART23/23: on the slice z=0, every point with |w|^2 >= |v|^2 + 1/3 is SN2, for every u and arbitrarily large norm, by a zero-mean Laurent h-absorption circle family

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 01:29:01 PDT 2026**. Exact WRITTEN mathematics; every identity is displayed and checked by hand. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## W0. Scope and union

The NEW claim C47 sits on the ORIGINAL chart. The complete current union is everything bound in `checkpoint-106-complete-current-v24-twenty-two-parts-plus-two-addenda-manifest-v1.json` (SHA256 6cc81ebb30e4a0b6e5156b241c528129ed95a8ac012307ef456260adef86cd48), THIS part, and all mandatory overlays. Parts 9–23 are LATER UNREVIEWED.

Imports:
- Part10 H1.1/H1.2;
- Part15 Q6;
- the closedness of the SN<=2 cone, used for one circle average exactly as in Part13 X4 and Part11 (absolutely convergent Laurent series with Fourier orthogonality and Parseval).

## W1. Theorem C47

**C47.** Let x=(u,v,w,0) with u arbitrary and |w|^2 >= |v|^2 + 1/3. Then SN(R_x)=2.

The region contains points of arbitrarily large norm with all of u, v, w comparable, for example (V, V, 2V, 0) for every V>=1/3 and every u. These lie in Part11 V3's "u, v, w all comparable" open core and outside C40 once |v|^2+1.5|w|^2>3.

## W2. Proof

Let r be uniform on the unit circle, and put

`λ_r = r^2/(w - r v),   ψ_r = a + r b - r̄ c + λ_r h_x.`

Since |w|>|v|, the denominator never vanishes.

**Rank two.** By H1.2 with α=1, β=r, γ=-r̄, λ=λ_r and every other coefficient 0 (in particular z=0):
- row0 = [1+λu, r+λv, λw, 0];
- row1 = [-r̄, 1, r, 0];
- row2 = [0, r̄, 1, 0];
- row3 = 0.

The defining relation λ(w-rv)=r^2 says exactly that λw = r(r+λv). Hence

`ψ_r = ((r+λv)|0> + |1> + r̄|2>) ⊗ (|1> + r|2>) + ((1+λu)|0> - r̄|1>) ⊗ |0>,`

and SR(ψ_r)<=2. Check entrywise:
- row0: (1+λu, r+λv, (r+λv)r, 0), and (r+λv)r = λw;
- row1: (-r̄, 1, r, 0);
- row2: (0, r̄, r̄r, 0) = (0, r̄, 1, 0).

**Moments.** Write ν=v/w, so |ν|<1, and expand λ_r = (r^2/w)Σ_{k>=0} ν^k r^k, which converges absolutely and uniformly on |r|=1. Using E[r^m]=0 for m!=0:
- E[λ] = Σ_k (ν^k/w) E[r^{k+2}] = 0;
- E[r λ̄] = Σ_k (ν̄^k/w̄) E[r^{1-(k+2)}] = Σ_k (ν̄^k/w̄) E[r̄^{k+1}] = 0;
- E[(-r̄) λ̄] = -Σ_k (ν̄^k/w̄) E[r̄^{k+3}] = 0;
- E[r·conj(-r̄)] = -E[r^2] = 0, and E[r] = E[r̄] = 0;
- E|λ|^2 = Σ_k |ν|^{2k}/|w|^2 = 1/(|w|^2-|v|^2), by Parseval.

The coefficient vector is (c_a,c_b,c_c,c_h)=(1,r,-r̄,λ_r), so every cross-moment vanishes and

`E P(ψ_r) = P(a) + P(b) + P(c) + P(h_x)/(|w|^2-|v|^2).                         (W2.1)`

**Remainder.** By H1.1,

`R_x - E P(ψ_r) = 3[P(d_x)+P(e)+P(f)+P(g)+P(j)] + (3 - 1/(|w|^2-|v|^2)) P(h_x).`

The bracket is nonnegative iff |w|^2-|v|^2 >= 1/3. The vectors involved are d_x=02+|3>x, which has Alice support {0,3}; e=20+33, which has SR 2; and the products f, g, j, h_x. So every term is a nonnegative multiple of a projector onto an SR<=2 vector.

The circle average lies in the closed SN<=2 cone; Carathéodory gives a finite decomposition if desired. Hence SN<=2, and Q6 gives SN=2. ∎

## W3. Why this needs w-dominance, and what stays open

The mean of λ_r over the circle equals the residue of r/(w-rv) at r=w/v. That pole lies inside the unit circle iff |v|>|w|, and then E[λ] = -w/v^2 != 0. This is exactly Part11 V3's recorded leading λ-mean -w/v^2, so C47 is the w-dominant half of that obstruction, resolved.

For z!=0 the entry λz in row0, column 3 cannot be matched while rows 1–2 keep Bob support {0,1,2}. The j-corrected variants written down so far either have nonzero κ-mean or an e/f cost of order |w|/|z|. No z!=0 claim is made.

**Still OPEN at z=0:** |v|>=|w| with |v|^2+1.5|w|^2>3 and outside Theorems C and D, for example (0,V,V,0) or (V,V,V,0) at large V.

**Original physics-3/P44 remains UNMET.** This is an author-WRITTEN candidate pending fresh reconstruction. It is not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v25 PART23/23.**
