# info-6: dense active peaks sharply restrict every potential exchange direction

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Native `/bin/date` observed before this write: **2026-10-27T16:24:01-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** The statements quantify over all directions and all original Boolean objects; no swap, numeric state, peak half or control is selected or tested. They do not construct a witness, give an unrestricted no-go, select an original polar rank, improve the numerical nonlinearity bound or claim novelty/formal/kernel review.

## Claim

Let f be any actual balanced peak≤28 object. Let T be its nonzero one-support XOR, H={a:a·T=1} its odd affine 8-half, and S={a:|W_f(a)|=28}. For any d∉{0,T}, write

    H_d={a:a·T=1, a·d=1},    S_d=S∩H_d.

Then H_d is an affine 7-flat. Define X_d as the set of source points satisfying the exact peak-phase equations of `walsh-universal-exchange-rigidity-v1.md`.

1. If |S_d|>64, then X_d is either empty or an affine **two-point** set with direction T+d. Thus no such d has more than two possible source points for a balanced peak-preserving exchange.
2. If |S_d|>96 and X_d is nonempty, the one global mod-4 bilinear form 𝔅 vanishes on J:=T^⊥∩d^⊥. Equivalently, on K:=T^⊥ it factors as

       𝔅(u,v)=(u·d)L(v)+(v·d)L(u)                                 (2)

   for some linear L:K→F₂. This is a conditional algebraic consequence, not a choice or classification of an original polar rank.

These are necessary restrictions only; neither density condition nor any actual exchange is asserted to occur.

## Proof

Because d is neither 0 nor T, the two linear functionals a↦a·T and a↦a·d are independent, so H_d has affine dimension 7. Any proper affine subspace of H_d has at most 64 points. Thus if |S_d|>64, its affine span is all H_d. Its linear span has dimension 8; its orthogonal complement is precisely ⟨T+d⟩, since both a·T and a·d equal 1 on H_d. The consistent phase system X_d is therefore a coset of ⟨T+d⟩, or is empty. This proves 1, including every possibility for the actual truth values at its two points.

Suppose |S_d|>96 and X_d is nonempty. For any solution x∈X_d, the actual peak sign condition says the common odd-half quadratic phase Q agrees with the affine character a↦a·x on all of S_d. Their difference is a Boolean polynomial of degree at most 2 on H_d. A nonzero such polynomial on seven variables has weight at least 2^{7−2}=32 by the elementary induction in `walsh-support-xor-obstruction-v1.md`, so it cannot vanish at more than 96 of the 128 points. Hence it vanishes identically. Its second differences are 𝔅, so 𝔅 vanishes on J.

To prove (2) without a rank classification, let λ(u)=u·d on K, choose any w∈K with λ(w)=1, and set L(v)=𝔅(w,v). Because 𝔅 is alternating on K and vanishes on ker λ=J, write each u=u₀+λ(u)w and v=v₀+λ(v)w with u₀,v₀∈J. Bilinearity gives exactly (2). All choices in the proof are arbitrary quantified witnesses to the implications, not generated or tested controls. ∎

## Inputs and limits

Inputs are S1's original definitions and the current-release files `walsh-universal-exchange-rigidity-v1.md` SHA-256 `7666453ec08368b66511dbb0afa25df3b4d995354686038c17695a61ad39873d`, 40 LF, `walsh-odd-half-quadratic-sign-v1.md` SHA-256 `be6421feeb80f076373e09aaccb4a6ed1401591db892e82fe77c64831aa215e7`, 35 LF, and `walsh-support-xor-obstruction-v1.md` SHA-256 `380655caaa06ea27e4236070ff66e070be63963960efebfabef2e730d2091fc4`, 49 LF, with mandatory `walsh-support-xor-coupled-count-erratum-v1.md` SHA-256 `810e3e55c52288f252b335a776a134752702df33d70d8d689fb009aac127273c`, 30 LF. The peak-XOR premise is parent-notified same-harness written-supported; the exchange, odd-half phase and this new implication remain unreviewed. All four source pins were measured before this write.

The theorem does not show an exchange exists, show either density condition holds, construct a witness or exclude every original object. All rank/weight alternatives and `(24,24,2)` remain open. No old Gate-I/candidate/HELD source, stopped half-split/canonical or global truth-degree/ANF method, or selection guide is an input. Book-source equivalence is only at the separate internal bridge; full-scope review of this theorem, human, formal/kernel, executable and novelty gates remain unperformed. Prior exposure, metadata-poll and source-pin MINORs, all S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
