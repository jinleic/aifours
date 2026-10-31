# Balanced NL242 (3,112), L=16, s=12, d=5: direct distinct-inactivity (a4) exclusion

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:43:30-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** A shorter same-author route to v19, not an independent review. It uses the zero-slice pair/circuit geometry and v30, not v14's moment proof or v12's 30-coset energy count. No scientific program, selected-state probe, whole-type exclusion, witness, formal/kernel or novelty claim.

## 1. Both single-carrier slices force m=24

Let p,p′ be the two outside balanced cosets, with distinct inactive slices and δ=p+p′∈W\{0}. In the slice where p is the only active outside coset, all twelve Σ-points are active. The single-carrier formula gives υ(p)=ε_p(3m−64), and the twelve-point τ=0 parity/Parseval congruence gives m≡0 (mod 3). The balanced p T-row in its two active slices has magnitudes either {2,2} or {4,8}. Among these magnitudes, |3m−64| with m≡0 (mod 3) can only be 8, at m=24. The same reasoning applies to the p′-only slice.

By the author-only v30, each m=24 slice splits the six canonical r-pairs into positive and negative triples and has Ψ²=4+32·1_N, where N consists of its eight |Ψ|=6 classes. For v≠0, its transform F of the 24 nondivisible classes equals the negative autocorrelation of its signed Σ-set:

    F(v)=−Σ_{x∈W}g(x)g(x+v).                                    (1)

The six quotient labels form an affine six-point circuit. For a difference between labels in the same triple, exactly those two r-pairs overlap and (1) has magnitude 4; for labels in opposite triples it vanishes, as it does at r. Thus F has support consisting of both lifts of the six same-triple quotient differences, and only values 0 or ±4 off 0.

At the other outside balanced coset, inactive in this slice, the T-row gives υ∈{0,±6}. Since the single-carrier formula gives υ=3ε_pF(δ) and F(δ)∈{0,±4}, F(δ)=0. This is true in both single-carrier slices.

## 2. Shifted support obstruction

Let A₁,A₂ be the six same-triple differences in Q=W/⟨r⟩, and d=δ mod r. Then d∉A₁∪A₂. At a pure outside coset, a nonzero single-carrier value has magnitude 12, so the pure-coset slice lemma makes every other nonzero slice zero. The two carriers are shifted by δ, giving

    A₁∩(d+A₂)=∅.                                                 (2)

For d=0 this is impossible: among any three labels in one first-slice triple, two share a second-slice triple.

For d≠0, the circuit property represents d by a unique pair i,j. Since d belongs to neither A-set, i,j are in opposite triples in both splits. Orient both splits with i on one side and j on the other. For any other label k, adding d swaps the differences i+k and j+k. If k changes sides between the splits, one of these differences lies in A₁∩(d+A₂), contrary to (2). Hence the splits coincide. The four other labels then form two same-side pairs {a,b} and {c,e}; the six-point sum is zero, so d+(a+b)=c+e. Both pair differences belong to the common A-set, again violating (2). ∎

## Exact scope and dependencies

This excludes distinct-inactivity (a4) only conditionally at author-candidate level. It imports v11/v12's original cases and single-carrier/T-row formulas, the τ=0 m≡0 (mod 3) statement in `rank6-112-L14-s12-exclusion-v3.md` SHA-256 `3a29e8171f3b8eb7b2fc8f51ace4ae0df92d8f9c80b04f49c381fe2dbda2d62b`, and `rank6-112-L16-s12-d5-m24-pair-rigidity-v30.md` SHA-256 `1444e3e3ab5dce4d43888dae0984c241e11c54adc04987496c7200059dbc280d`, 35 LF. It retains the admitted cuts and all errata in those sources. No independent review, accepted floor, whole-type exclusion, original witness, unrestricted exclusion, (24,24,2) closure or novelty follows. Earlier process findings, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding.
