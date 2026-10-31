# S1 addendum 1 — LOC conserves every coherent source value, including nonidempotent E-blocks

**Owner:** MathSemigroup-2, math-4. **Actual prewrite clock:** Tue Oct 27 14:39:21 PDT 2026 (`/bin/date`).

**AUTHOR-WRITTEN / UNREVIEWED.** Additive continuation of `prerequisite-derivation-v1.md`, SHA `e3f8451d6a41bd5350105055dd10d47893e7c1bddd9391e825985c0802076111`. Its bytes remain unchanged.

This closes the exact local equation case left NR there. It does **not** close the idempotency-expansion failure, R/L separation, or the original embedding problem.

## 1. Inputs, provenance and scope

Same S1 narrow authority, same exact seven-source packet (`5a671de2533ed5c1dd241695bde1cb03f2833f0467a67f0c7440b0f7f5eddf4e`), all read through LF880 as recorded in v1.

New proof inputs are just:

- original source regularity, with a mutual inverse of any actual source element (S2:15–21);
- original local r-orthodoxy: E(fSf) is a regular band for each actual idempotent f (S4:43–47; the literal LOC law is S3:15–19);
- purity of actual q (S2:80–104);
- the literal position identities (S4:49–57).

No Rees/RH factorization or PR/RP transfer is used to prove the source lemma. Any eventual original-reading consequence still retains those named U5/PRRP boundaries. Main's current six-body reading is not asserted. All three mandatory corrections remain in force; the false grid equality, incomplete identity-image formula and overbroad kernel heuristic are not inputs.

This proof is a direct calculation with an actual mutual inverse and actual local idempotents from the original hypotheses. It is **not** a completion/globalization theorem or an import of any old corner/homogeneity/representation guide. No source/action is enlarged, no common identity for unrelated source elements is adjoined, and no excluded prior outline is invoked. Same-author exposure is disclosed, not claimed absent.

## 2. Source lemma with no idempotency assumption on e

**Lemma L-SUPPORT.** Let S be regular with E(fSf) a regular band at every actual source idempotent f. For arbitrary e,a,b,c in S, suppose ea, eb and ec are idempotents. Then

e a e b e a e c e a e = e a e b e c e a e.                  (L)

No hypothesis that e itself is idempotent is required.

**Proof.** Choose a mutual inverse r of e, and put f=er. Regularity gives f²=f and fe=e. Write

p=ea,  q0=eb,  t=ec.

By hypothesis p,q0,t are idempotents, and fp=p, fq0=q0, ft=t, because fe=e. Set

x=pf,  y=q0f,  z=tf.

All three lie in the **same actual local monoid** fSf. For x, both fx=x and xf=x hold, and

x²=p f p f=p²f=pf=x.

The same calculation makes y,z idempotents. Thus x,y,z belong to the regular band E(fSf). Its regular-band identity is

x y x z x = x y z x.

Multiply this equality on the right by the actual e. Since fp=p, fq0=q0, ft=t and fe=e,

x y x z x e = p q0 p t p e,
x y z x e = p q0 t p e.

Expanding p=ea, q0=eb and t=ec gives exactly (L). This uses associativity only after the local identity. No equality such as eae=e, no cancellation, and no common support for unrelated source elements was assumed. ∎

**Degeneracies.** Repeated variables, coinciding idempotents, trivial local bands, e idempotent or nonidempotent, and arbitrary cardinality are all included. The proof makes one regularity choice for the actual e; it never chooses an idempotent unit for arbitrary a,b,c or assumes they lie in fSf.

## 3. Every coherent LOC substitution satisfies the source hypotheses

Use the notation of v1: substitute arbitrary nonempty coherent words for E,A,B,C, with source products e,a,b,c and start positions v_E,v_A,v_B,v_C.

Coherence of the repeated E-A-E segment gives

v_A=v_E w(e,a),
v_E=v_A w(a,e).

Since positions lie in G, cancellation of the common **group position** v_E (not source cancellation) gives

w(e,a)w(a,e)=1_G.

But

w(e,a)w(a,e)=g_(ea) p_(lambda_a,i_e).

The actor q(ea) has row i_e and column lambda_a, so this is precisely the criterion that q(ea) is idempotent. Purity therefore gives (ea)²=ea. Identical calculations for E-B-E and E-C-E give eb and ec idempotent.

These subpatterns occur on **both** LOC sides. L-SUPPORT applies whether or not q(e), or e, is idempotent.

Therefore the NR-LOC-NONIDEMPOTENT-BLOCK in v1 is discharged at AUTHOR-WRITTEN level for **coherent** substitutions. Nothing is claimed about a nonexistent source value on an incoherent word.

## 4. Substitution, both directions, and every word context

- **All nonempty substituted words:** the argument concerns their actual products e,a,b,c, not just generator substitutions. Repeated variables carry the same actual placed word each time.
- **Coherence of both sides:** each side consists of the same adjacent block-type pairs E-A/A-E, E-B/B-E and E-C/C-E, all with their fixed repeated origins. Thus if one side is coherent, all the join equations for the other side hold. Internal block coherence is inherited.
- **Outer left context:** both sides begin with the same E-block at the same position. The preceding join is unchanged.
- **Outer right context:** both end with that same E-block and its same last placed letter. The following join is unchanged.
- **Source equality in context:** L-SUPPORT gives equality of the two source products before inserting the arbitrary left/right source context, so associativity preserves equality afterwards. An absent context means simply omit it, not adjoin a source identity.
- **Reverse LOC:** all coherence/equality statements above are equivalences or symmetric equalities. They cover expansion and contraction, not just one preferred reduction.

Hence **every coherent LOC application in every coherent one-hole context conserves Eval**, in both directions.

## 5. Exact generating-step classification after this addendum

On the coherent-word domain, the generating presentation steps now have a complete classification:

| Step | Domain / value behavior |
|---|---|
| Associativity | Always preserves the domain and value. |
| Either direction of any M relation | Preserves the domain and value, including arbitrary outer contexts. |
| Either direction of LOC, under arbitrary nonempty word substitution | Preserves the domain and value whenever one side is coherent, including all nonidempotent E-block cases. |
| U² -> U from a coherent word | Forces the source product of U idempotent, so preserves value. |
| U -> U² with idempotent source product | Preserves domain and value. |
| U -> U² with nonidempotent source product | Leaves the coherent domain; the uniformly reachable failure from v1 persists. |
| A step on already incoherent words | Eval is undefined; no value assertion is made. |

**Conclusion.** The exact first failure of this partial invariant is isolated to arbitrary band-idempotency expansion of a coherent block with nonidempotent source product. There is no unpaid coherent LOC case remaining. An all-derivation proof still must interpret those new incoherent terms and their later equations; restricting to the coherent subderivations is not permitted as a substitute.

## 6. Original-target caller and next premise

The original full finite/infinite source quantifiers and the distinct R/L obligations remain. None of these relation checks supplies a pair-separating host or an identification of distinct original source idempotents.

The admitted next question is whether an interpretation on **all** presentation terms can incorporate the incoherent idempotency expansions without discarding the noncommutative information needed inside a rectangular fibre. A semilattice-only interpretation provably loses that information (v1 §6). No such total interpretation is asserted here.

All S0/S1 restrictions, scientific HOLD, N4 UNKNOWN/historical child exit unestablished, auxiliary214 STOP, exclusions and permanent process findings persist. No interpreter, arithmetic program, enumeration, solver, replay, selected probe, CLI, nested agent, Git mutation, deletion or external contact was used. This is not formal/kernel/executable/independent-model/novelty acceptance. Research deadline remains 2026-10-31T21:23:27.000Z.
