# Even a relative MIDDLE identity completion forces GLOBAL regularity

**Status: NEW AUTHOR WRITTEN self-contained band theorem with a small exact control; UNREVIEWED / UNADOPTED.** This is a sharp obstruction to a particular completion step, NOT to the original fullSN physical host problem. It does not assume a source semigroup is orthodox or declare an originalQ1/Q2 closure.

## 1. Principal ONE-sided ideals of an SN band are GLOBALREG

Let C be a band satisfying `abcda=abcacda` and p∈C. The sets Cp and pC are subbands. In Cp, p is a RIGHT identity. Substitute c=p in SN for a,b,d∈Cp:

`a b p d a = a b p a p d a` reduces to `a b d a = a b a d a`.

Thus Cp is a GLOBALREG band. The same substitution for a,b,d∈pC, using p as a LEFT identity, gives the same global regular identity. Hence BOTH principal one-sided ideals are GLOBALREG, not merely their intersections pCp. This is a direct equational derivation; it does not import the earlier localREG↔SN proof.

## 2. Exact relative-mididentity completion theorem

For ANY band B, the following are equivalent:

- B embeds as a subband in an SN band C containing p such that `b p c=b c` for EVERY b,c in the embedded B (a single RELATIVE MIDDLE identity).
- B embeds in an SN band with a single relative LEFT identity, or with a single relative RIGHT identity.
- B is GLOBALREG.

To prove the first condition implies the third, identify B with its image. Define

`Φ:B→Cp×pC`, `Φ(b)=(bp,pb)`.

This is a homomorphism: `(bp)(cp)=bpcp=(bc)p` and `(pb)(pc)=pbpc=p(bc)`. It is INJECTIVE: if bp=cp and pb=pc, then

`b=bpb=(bp)b=(cp)b=c(pb)=c(pc)=cpc=c`.

Both factors are GLOBALREG by §1, so their subband Φ(B) is GLOBALREG. A relative left or right identity is a relative middle identity, giving its necessity too. Conversely, if B is GLOBALREG, its ordinary fresh unitization B^1 remains GLOBALREG: substituting1 for any of x,y,z in `xyxzx=xyzx` gives the same product on both sides. GLOBALREG directly implies SN by the substitution `x=a,y=bc,z=cd`, since `a(bc)a(cd)a=a(bc)(cd)a` reduces to SN. Thus B^1 is the required SN completion with p=1, proving ALL implications.

This rules out even arbitrary larger SN ambient bands and arbitrarily many auxiliary elements if the construction retains B as a genuine subband and demands ONE relative middle identity. It is strictly more general than checking whether B^1 itself is SN. No Green–Rees theorem, inverse-semigroup embedding theorem, actor transport, finiteness or unexplained model import is needed for this proof.

## 3. Exact finite control and scope limitation

`frontier-20261029-SN-relative-mididentity-checker-v1.py`, SHA `3198600ae4a40bc855feecdd59c5ec5c4cb16d7e79ce5753da170ca8bc21e2be`, completed before ThuOct29 03:30:14 PDT2026. For the five-band B5={x,u0,u1,v0,v1}, it checks all625SN substitutions, ALL ten principal one-sided ideals are closed and GLOBALREG, and the Φ-map is an injective homomorphism on each tested pC. Whole B5 is not GLOBALREG at(u0,x,u1), and no EXISTING element is its relative middle identity. The impossibility of ANY external SN relative-middle-identity completion comes from the universal written proof, not a bounded search.

B5 itself is a perfectly valid positive SN host band, and the existing nonorthodox S45/S68 SN hosts remain positive. The excluded maneuver is ONLY a completion which preserves an already chosen nonGLOBALREG band as a subband and adds one globally usable left/right/middle unit. It does NOT exclude different coefficient maps, ideal-dependent partial units, row/column-dependent frames, multiple twisted sandwich elements, or a genuine fullSN source globalization. Those alternatives remain scientifically open. No novelty, independent review or formal proof is claimed.
