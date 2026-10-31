# Reverse physical-row matching and exact CRT implication

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 19:17:58 PDT 2026. This is a **WRITTEN conditional soundness argument** for a new independent d4 identity implementation, not a claim that its currently running computation has succeeded. Any actual result requires a complete later receipt. The original physical lift, Gram/equality validity and saved-multiplier PSD remain separate prerequisites.

## 1. Repeated-letter assignments do not change a source orbit sum

For a used physical Gram row pair, both the original and new `reverse_rule` construct the same family f and the same multisets of unconjugated/conjugated physical factors. The owner assigns the **first** unused source slot with a matching letter; the new rule chooses the **last**. Thus the ket assignment and bra assignment differ only by permutations sigma,tau in the family letter stabilizer H_f.

For the local permutation-entry convention `V_p[k;l]=1` iff `k[p(j)]=l[j]` for all j, put `k'_s=k_(sigma(s))`, `l'_s=l_(tau(s))`. Then

`V_p[k';l']=V_(sigma p tau^−1)[k;l]`.

The same sigma,tau apply at **every** physical site and the auxiliary factor because they come from the same complete-replica physical row pair. Their simultaneous action maps every actual source-word orbit to itself, bijectively. Consequently replacing first-match with reverse-match leaves the sum of that row-pair functional over every actual orbit **exactly unchanged**, although individual word coefficients can change. No independence of source words or source-family moments is assumed.

The independently constructed canonical orbit representative in `frontier-20261028-d4-canonical-orbit-source-audit-v1.md`, SHA256 `91e4ec3fc4a135da325d4918162c63a4aa460f9a75b0d2aee8f9f4ab07923fe3`, covers independent left/right H_f actions, the three-site permutations and simultaneous inversion on all source words.

## 2. Fresh bound sufficient for exact rational zero

Let D be the positive least common multiple of `2^31`, every actual corrected multiplier-entry denominator and every corrected lambda denominator. For an orbit o write

`R_o = D[c(o)−Σ_t Tr(Z_t K_t†M_t(o)K_t)−Σ_e lambda_e E_e(o)]`.

All local maps and fixed compression entries are integral, so R_o is an integer. Let `Zmax=max|D Z_t[a,b]|`, `Lmax=max|D lambda_e|`, and let Wmax, Amax and Emax be the actual global maxima of the integer joint-compression, independently generated Gram-local and independently generated equality-local entries. For type t let k_t be its Gram row count, r_t its multiplier dimension and n_t its local joint-compression dimension. Define

`Cblock=Σ_t k_t² r_t² n_t²`,
`Ceq=Σ_e (number of signed parts in e's equality group)`,
`Cobj=(max_p|2·4^cycles(p)−4^cycles(tau p)|)^3
       ·max_p 2^cycles(tau p)`, where tau=(0 3).

One word's block contribution contains at most the stated k²r²n² products per type and each product is bounded by `Zmax Wmax² Amax⁴`. Each equality coordinate contributes no more than its number of signed parts times `Lmax Emax⁴`. The objective numerator is at most Cobj and its denominator is `2^31`. Every orbit contains at most `N=24⁴` words. Thus the actual source integer residual obeys

`|R_o| <= B := N [Cblock Zmax Wmax² Amax⁴
                  + Ceq Lmax Emax⁴ + Cobj (D/2^31)]`.                   (3)

This is a deliberate overestimate, with all maxima and counts taken over the actual corrected bytes and all independently generated source local maps. Reverse matching merely permutes each map's 24 source permutation arguments by stabilizers, and the new implementation also recomputes its **own** maxima directly; no unverified assumption that two local arrays are entrywise equal is used.

If distinct primes p_i avoid all denominators, every computed rational orbit residual being zero modulo every p_i implies their product P divides every R_o. With (3), the **actual exact comparison** `P>2B` forces every R_o=0. Agreement modulo one or a few primes is not enough. Reverse-axis tensor contractions are legitimate because the four local-mode maps act on distinct axes; each intermediate must be reduced modulo p and its int64 width/product bound checked.

## 3. Actual prospective verifier and precise nonclaims

`frontier-20261028-d4-reverse-independent-crt-check.py`, SHA256 `423e58d82a5be68486b8940199335b677f3d69cbb3ba33a37065e1bded42ebbc`, was written after Main actually read the earlier cadence self-stop and gave explicit prospective resumption. It is designed to use direct-canonical orbit labels, opposite equal-letter matching, independently authored literal local/equality maps, cycle-count objective, reverse-axis contraction, a freshly recomputed height bound, and the pinned prior prime list. It writes actual partial progress only after completing a real prime. At the time of this note, **no outcome of its running job is asserted**.

If that job later returns all-prime PASS and `P>2B`, the above argument gives an exact d4 orbit identity conditional on its code, data and arithmetic correctness; it is not by itself the source physical PSD/equality/lift proof, all-d theorem, human/other-model-family or formal-kernel review, physical operational implication or novelty. A stop, mismatch or partial run must be reported as such. The previous disclosed cadence gaps remain in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; no retrospective cure or continuous-supervision inference follows.
