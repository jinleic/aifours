# A sharp limitation of globally idempotent-separating trivial-action invariants

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation: **Wed Oct 28 17:11:49 PDT 2026**. The exact bounded check in §5 is NOT a proof of the infinite statements. No novelty or original full-target solution is claimed.

## 1. The general falsified premise

The preceding candidate `frontier-20261028-cryptogroup-band-retraction-v1.md` establishes a powerful canonical-band invariant whenever an actual idempotent-separating source homomorphism into a seminormal band exists. A tempting universal completion would be: **every original source admits such a homomorphism, so the canonical host's group action may be taken trivial**. This is false even for original-class inverse monoids.

More generally, for ANY orthodox regular semigroup S (idempotents closed), if a homomorphism `ρ:S→D` into ANY band D is injective on E(S), then S must be completely regular and H must be a congruence. The proof is entirely elementary (§2). Conversely, for a completely regular H-congruence source, the natural band quotient is idempotent-separating; under the original local-r hypothesis it lies in V, as proved in the preceding candidate. Thus for **orthodox original-class sources**, existence of a globally idempotent-separating trivial-action V-band invariant is equivalent to S being a cryptogroup.

This equivalence concerns a particular **stronger invariant**, not existence of an arbitrary host. For a concrete original-class noncryptogroup, §§3–4 construct a nontrivial-action invariant that works. Therefore the failure of trivial action cannot be promoted to a nonembedding result.

## 2. Idempotent-separating band homomorphism forces group membership

Let s∈S, and let t be any mutual inverse: sts=s and tst=t. Put

`e=st`, `f=ts`, `p=ef`.

Both e,f are source idempotents; because S is orthodox, p is idempotent too. Set a=ρ(s), b=ρ(t). The band relations include `aba=a`, `bab=b`, and

`ρ(e)=ab`, `ρ(f)=ba`, `ρ(p)=(ab)(ba)=aba=a`.

The four following identities compare **actual source idempotents**; each therefore follows from injectivity of ρ on E(S):

`ρ(pe)=a(ab)=ab=ρ(e)`  ⇒  `pe=e`;
`ρ(ep)=(ab)a=a=ρ(p)`  ⇒  `ep=p`;
`ρ(fp)=(ba)a=ba=ρ(f)`  ⇒  `fp=f`;
`ρ(pf)=a(ba)=a=ρ(p)`  ⇒  `pf=p`.

As es=s=sf, these imply `ps=(pe)s=es=s` and `sp=s(fp)=sf=s`. The element `v=p t p` satisfies

`s v = s p t p = s t p = e p = p`,
`v s = p t p s = p t s = p f = p`.

Thus s is a unit of the monoid pSp with identity p. Every source element belongs to a subgroup, so S is completely regular. No selection of one inverse for different products or assumption that arbitrary idempotents commute is used.

For any completely regular S and band homomorphism ρ, its restriction to any subgroup is constant, because an idempotent group element must be the group identity. Writing e_s for s's group identity, ρ(s)=ρ(e_s). If ρ separates source idempotents, `ρ(s)=ρ(t)` iff `e_s=e_t`, equivalently s H t. Therefore `H=ker ρ` is a congruence. This proves the claimed necessary condition, and the converse at the exact locally-r-orthodox source scope is the explicit S/H construction in the preceding candidate.

**Diagnostic consequence:** any proof of universal idempotent separation that uses only a *trivial-action* homomorphic V-band image and is silent about completely regular/H-congruence is missing an essential hypothesis. This says nothing negative about an action-dependent B_q invariant.

## 3. Concrete infinite original-class source where trivial action fails

Define the bicyclic monoid explicitly as the set `N_0×N_0`, with

`(i,j)(k,ℓ)=(i+(k-j)_+, ℓ+(j-k)_+)`.                      (1)

One self-contained associativity proof represents `(i,j)` by the partial bijection on N_0 with domain `{n≥j}` and value `n↦n-j+i`. The functions are distinct by their domains and images, composition gives exactly (1), and partial-map composition is associative. The identity is `(0,0)` and `(i,j)` has inverse `(j,i)`; the idempotents are exactly `(n,n)`, whose multiplication is `(max(n,m),max(n,m))`. Hence the source is an inverse monoid with a semilattice of idempotents and all local corners inverse, in particular locally r-orthodox.

The map `q(i,j)=i-j` is a homomorphism onto Z and is idempotent pure: q=0 iff i=j. If e≤s in the printed natural order, e=fs for a source idempotent f, so q(e)=q(f)+q(s) forces q(s)=0 and s is idempotent. Thus the source is weakly E-unitary and satisfies every named original-class hypothesis. By the pure-group/syntactic-kernel argument in the global-regular-band candidate, q is also the ACTUAL syntactic quotient up to its canonical isomorphism to Z; alternatively, identical q gives identical idempotence in every context, and the reverse follows by applying the context of a mutual inverse.

Let `p0=(0,1)`, `q0=(1,0)` and 1=(0,0). Then p0 q0=1, while q0 p0=(1,1)≠1 and both latter elements are idempotent. For any band homomorphism ρ, write a=ρ(p0), b=ρ(q0), d=ρ(1). The element d acts as identity on the image and ab=d. Since a,b are idempotent,

`a=a d=a(ab)=a²b=ab=d`,
`b=d b=(ab)b=ab²=ab=d`.

Hence `ρ(q0p0)=ba=d=ρ(1)`. Every such homomorphism identifies distinct source idempotents. The inverse monoid is not completely regular; e.g. the general conclusion follows from §2 and the exhibited nonseparable idempotents. No unsupported claim that a finite truncation of (1) is closed is made.

## 4. The ACTUAL canonical host still separates the source

Let D be the semilattice of all integer upper tails

`A_k={n∈Z:n≥k}`,    `A_i A_j=A_i∩A_j=A_max(i,j)`.

Z acts on D by translations α_u(A_k)=A_(u+k). Define β(i,j)=A_i and keep the actual group actor q(i,j)=i-j. For all source elements and u∈Z,

`α_u β(i,j) · α_(u+q(i,j)) β(k,ℓ)`
`= A_(u+i) ∩ A_(u+i-j+k)`
`= A_(u+i+max(0,k-j))`
`= α_u β((i,j)(k,ℓ))`.

Thus the assignment `X_(u,(i,j))↦A_(u+i)` respects EVERY canonical mixed relation. A semilattice is in V, so every band identity/substitution/context is also respected; this is an honest equivariant homomorphism from B_q, not just a word-prefix statistic. For distinct idempotents `(n,n)`, β gives distinct tails A_n. The physical map

`(i,j) ↦ (A_i,i-j) ∈ D⋊Z`

is injective, since the tail determines i and the group coordinate then determines j. Its multiplication is (1) by the displayed equation. Thus this actual original-class source embeds in a **nontrivial shift-action** host, while every trivial-action globally idempotent-separating band projection fails. There are no distinct R/L-related idempotents in this inverse example; it calibrates the all-idempotent invariant, not a new nonvacuous R/L instance.

The actor/group action in this construction is explicit and source-matched, not an imported O'Carroll or McAlister existence theorem. It does not generalize automatically to the whole inverse or locally r-orthodox class. Standard partial-bijection facts used here are defined and checked in the first paragraph; the infinite algebra is fully symbolic.

## 5. Bounded exact check and limitation

Checker `frontier-20261028-bicyclic-shift-checker-v1.py`, SHA256 `e1a234df955ae4dca6bf940c9dd95fe88610b8f3251d527a78048db65c25cf68`, executed with `/opt/homebrew/bin/python3` at **Wed Oct 28 17:11:46 PDT 2026**, timeout30s, returned exit0:

```text
bounded_source_labels=25 shifts=7
PASS exact unit, associativity, inverse, quotient purity, canonical relations, host injection
PASS five distinct idempotent tails; p*q=1 and q*p=(1,1)!=1
CONTROL wrong-shift-direction mismatches=2555
```

The program compares exact integer labels and uses no floating point. Products of bounded input labels are not truncated. Its invalid-action control intentionally reverses the actor shift and is detected by the claimed relation. This is a bounded check of the implementation/formulas and does NOT establish the infinite result, which is separately proved above. No third-party independent verification, source-priority review or proof assistant was performed.

## 6. Exact scientific gap and provenance

The concrete false premise is that a globally idempotent-separating **trivial-action** V-band source image is universally available. The action-dependent invariant closes this one source but does not resolve the general noncryptogroup original target or a nonvacuous R/L collapse. The previous global-regular-E theorem handles this source only by its named SZ87 import; the present direct host does not use that import.

An all-host obstruction still needs a genuine distinct original-class pair collapsed in the full canonical V-band; failure of the trivial-action test is not such a collapse. An unrestricted embedding proof still needs to preserve source information through arbitrary local V-band substitutions and the ACTUAL completely-simple actor. The literal book target/presentation interface remains independently qualified. Prior quarantine/failure records remain historical, not accepted premises; all results here are prospective author work subject to full independent review.
