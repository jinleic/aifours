# One isolated nonloop-duplication excursion cannot collapse a source path

MathSemigroup, math-4. Observed immediately before writing: **2026-10-23T14:34:28-0700**.

**CANDIDATE / PARTIAL / NOVELTY_UNCLEAR.** This advances exactly the path-completion part of the canonical fibre-separation construction from `path-separation-attack-v1.md`, SHA-256 `60d967621f44e20f36f25c4ce402446ff4d4bd6f5f7dbf4c6a0fe68a4451ff4d`. It is confined to the same orthodox group-graded branch. It does not cover arbitrary overlapping/untyped derivations or the general nonorthodox Rees case. No execution was performed.

## 1. Exact new claim

Keep S, sigma:S→G and the absolute-object-labelled arrow alphabet from that file. Suppose U and V are path words from a to b, a≠b. Consider a derivation

    U --> UU ~~ ... ~~ VV --> V,                  (1)

where the first and last steps are the indicated band idempotency expansion/contraction, and every interior step uses only:

- an actual typed composition relation M_G, in either direction; or
- the displayed local regular-band generating identity LR_P, in either direction and arbitrary nonempty substitutions.

Assume **every interior word has exactly ONE incompatible adjacency** between consecutive arrows. This is an exact restricted hypothesis, not an asserted normal form for arbitrary derivations.

Then U and V have the same value in S.

The same is true when this excursion is performed in a fixed left/right word context and every interior rewrite stays wholly inside the selected core, never crossing either context boundary. Remove the fixed context and apply the core statement. Thus a derivation assembled from typed rewrites and such context-isolated single excursions cannot identify distinct source paths of the same endpoints.

## 2. Bridge-value invariant on one-gap words

A word with exactly one incompatible adjacency splits uniquely as

    L | R,

where L and R are nonempty path words. Let end(L)=b and start(R)=a. Inserting any arrow X_(b,t) with sigma(t)=b^(-1)a completes this word to a path. For each such t, define its completed value as

    F_t(L|R)=value(L) t value(R).                 (2)

The next assertions concern all such t simultaneously; no endpoint-only bridge satisfying an inner-inverse law for every source element is assumed.

### Actual multiplication steps

A composition relation M_G can only be applied to a compatible adjacent pair. It cannot straddle the one incompatible adjacency. Contracting or expanding elsewhere preserves the endpoints adjacent to the gap and preserves the corresponding S-product. Thus it preserves the ordered gap pair(b,a) and every value F_t.

### Local regular-band steps

Recall the two block words

    P Z P X P Z P Y P Z P,
    P Z P X P Y P Z P.                            (LR_P)

The block P occurs at least four times and Z at least twice on either side. Therefore, in a one-gap word, an incompatible adjacency cannot lie **inside** a substituted P or Z: it would recur in each copy and give at least two gaps. Likewise the boundary pairs PZ and ZP occur at least twice on either side, so neither can be incompatible in a one-gap word.

The only remaining possibilities are:

- the unique gap lies outside the rewritten substring;
- it lies inside the single-occurrence block X or Y;
- it lies at one of the single-occurrence boundaries PX, XP, PY or YP.

In the first case, the LR substring is an actual path, so the typed local-corner lemma from the preceding packet preserves its S-value, and therefore F_t.

In the second case, insert the bridge t inside that same X or Y block. In the third case, absorb the bridge into the appropriate end of X or Y. The resulting completed LR relation is path-typed on both sides. The local-corner lemma applies to **every** choice of t of the specified grade, and gives equal completed values. Removing the bookkeeping bridge leaves exactly one gap of the same ordered type(b,a) in the new word. Hence every F_t is preserved here too.

This proves the one-gap bridge-value invariant under every allowed interior step of(1). It is a symbolic argument about all substitutions and all bridge values, not a finite point test.

## 3. Recovering the original source values

Put s=value(U), v=value(V), and h=a^(-1)b. Both have grade h. The gap between the two copies in UU and VV is(b,a). Invariance of(2) along the interior derivation therefore gives

    s t s = v t v
    for every t with sigma(t)=h^(-1).             (3)

Choose s' in V_S(s) and v' in V_S(v). Their grades are h^(-1). Substituting t=s' into(3) yields

    s=v s' v.

Both v s' and s' v have grade1, so they are idempotents by E-unitarity/purity. Consequently this equality witnesses s<=v in the **exact** book natural order:

    s=(v s')v=v(s' v).

Substituting t=v' gives v=s v' s, with s v' and v' s idempotent, so v<=s. Antisymmetry of the natural order of a regular semigroup gives s=v. This completes the proof.

No compatibility of the natural order with multiplication was used. That would be false in this class and cannot be inserted when handling changing contexts. The fixed-context version follows instead by equality of the core values before multiplying the fixed context, so it avoids that error as well.

## 4. Exact unresolved extension, not a normal-form assumption

The lemma excludes a genuine set of potential collapse derivations, but does NOT show that every congruence derivation decomposes into these excursions. In a general derivation:

- another nonloop idempotency expansion can create a second gap before the first closes;
- local-regularity rewrites can then duplicate or merge gap occurrences, defeating the unique-gap argument;
- multiplication/identity rewrites can cross the originally selected core boundary, changing the surrounding source contexts.

Those are the remaining coherent-repair obligations in this route. In particular, a derivation that collapses distinct source idempotents must resist decomposition into typed segments and the context-isolated one-gap excursions just proved harmless. A proof of the needed decomposition or an actual source-preserving multiple-gap counterexample has not been obtained.

The key advance over merely observing that typed paths are harmless is the universal bridge-polynomial identity(3): arbitrary fixed bridges were previously inadequate, but varying t and then testing actual inverse choices eliminates one complete untyped excursion without requiring a common inverse for an entire group-grade fibre. This is still a restricted construction lemma, not the full mixed-relation separation theorem, a full embedding, or a new counted problem.
