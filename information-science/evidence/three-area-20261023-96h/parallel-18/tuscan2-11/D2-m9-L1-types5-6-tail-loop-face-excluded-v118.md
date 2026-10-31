# Original Tuscan-2(11), entire m = 9 distance-two branch, part 7: L1 types 5 and 6 (tail face = T Λ T⁻) excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-face-types-segments-and-universal-constraints-v117.md` (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`). Notation is that of v117. Lemma OL (v115 §1) and the L2 k = 1 tail-face arguments of v95 §4–§5 (SHA256 `5f818d37…`, read whole at intake) are used with the labels of the leaf and the loop branch exchanged.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. Set-up

**The tail face.** In types 5 and 6, F1 = S_T P+ is the walk ℓ, T, b6, Λ (out by Λ+, back by Λ−), b6, T, ℓ (v117 §2). Index Λ from its Λ+ end. The F1 positions are:
- b6 at t;
- Λ[k] at t + k;
- b6 at t + λ;
- ℓ at 10r1 = 2t + λ.

So λ = 10r1 − 2t, where r1 = r(F1).

**Arms.**
- R_out = ℓ, T_int, b6, Λ[1..u] and R_in = Λ[λ−u..λ−1], b6, T_int, ℓ.
- Each arm carries S, with |S| = u.
- The F1 cuts on Λ sit at Λ[u + 10k], for k = 0..r1 − 2.

**Counts.** Let m be the number of W's on Λ, and let ε = 1 if v's cut lies in F1. Applying the face identity to w (whose cut ℓ lies in F1) and to v gives:
- r1 = 2 + m, so r1 ∈ {2, 3, 4, 5};
- the number of V's on Λ is nΛ = m − ε.

The middle rows of F1 lie inside Λ. Each needs exactly one v and one w from Λ. No W lies on a cut, since w's cut is ℓ.

**The other pass.** The second pass P− of Λ is a single contiguous stretch of another face. In that face it is preceded and followed by b6, and after Λ+ the walk continues along σ(Λ+) = t1. So the two rows of that face which meet the ends of the stretch both contain b6.

## 2. The four values of r1

**r1 = 5.** Here λ = 2u + 30 ≥ 32 > 26. This contradicts Lemma OL.

**r1 = 4.** Here λ = 2u + 20 ∈ {22, 24, 26} (since λ ≤ 26), and the forward cuts of Λ sit at indices ≡ u. For every ρ, some window of v115 §1 contains s = u:

| ρ | Window | Contains u because |
|---|---|---|
| 1, 2, 3 | [1−ρ, L−11] | L − 11 = 2u + 9 |
| 4 | [−3, 2u−1] (B-chain) | u ≤ 2u − 1 |
| 5 | [1, 2u+4] (C-chain) | u ≤ 2u + 4 |
| 6 | [1, 2u+3] (C-chain) | u ≤ 2u + 3 |
| 7, 8, 9 | [1, 2u+19−ρ] | 2u + 19 − ρ ≥ u |
| 0 | — | Λ[u] would carry two cut passages |

The difference paths stay apart:
- Inside Λ they are disjoint.
- Beyond the Λ+ end they run, in F1, into T and, in the other face, into t1.
- Beyond the Λ− end they run into the thread preceding P−: t3 in type 5 and t2 in type 6.

So Λ is impossible.

**r1 = 2.** Here m = 0, so ε = 0 and nΛ = 0. Also λ = 2u, and R_out ∪ R_in covers Λ, with Λ[u] common to both. Hence L(Λ[1..u−1]) = L(Λ[u+1..2u−1]).

This is v95 §4 verbatim:
- If u ≥ 2, the equal-label pairs force cuts of the other face inside Λ, at indices c′ ≤ u − 1 and c ≥ u + 1. The cut cannot sit at Λ[u], since that label's cut is already in F1. Then c − c′ < 20 forces c = c′ + 10, so a full row lies inside Λ. That row contains no v (there is no V on Λ). Contradiction.
- If u = 1, then Λ[1] would need a cut in both faces. Contradiction.

**r1 = 3.** Here m = 1. If ε were 1, then nΛ = 0, so Λ carries no V and the middle row M1 = Λ[u..u+10] would contain no v. So ε = 0, and Λ carries exactly one V and one W, both inside M1int = Λ[u+1..u+9].

Write c1 = L(Λ[u]) and c2 = L(Λ[u+10]). By the face identity:
- every T_int label has exactly one Λ-vertex, and it lies in M1int;
- every x ∈ S ∖ {c1, c2} has exactly three Λ-vertices, i1 < u < i2 < u+10 < i3, with i2 in M1int.

The argument is now v95 §5 with v and w exchanged.

*At most two cuts on the pass.* Every row of the other face lying inside Λ needs a w from Λ. The single loop-W is not on a cut, because w's cut is ℓ. So at most one such row exists, and that face has at most two cuts on Λ.

*u ≥ 3.* Some x forces two consecutive cuts γ and γ + 10, and Φ = Λ[γ..γ+10] is a full row. Its eleven labels force M1int ⊆ Φ, so γ ∈ {u−1, u+1}:
- γ = u − 1 makes Λ[u−1] carry c2 on a cut. Contradiction.
- γ = u + 1 makes Λ[u+11] carry c1 on a cut. Contradiction.

*u = 1.* Both arms are single cut vertices carrying the one label of S, so one label has two cuts. Contradiction.

*u = 2.* The pairs force exactly one cut γ on the pass. The two rows meeting at Λ[γ] both contain b6, and the loop-V lies in M1int, inside one of them. That row then contains v twice. Contradiction.

## 3. Result

**WRITTEN, (R1)–(R2) only: L1 types 5 and 6 are impossible.**

**Open:**
- L1 types 1–4 and 7–12, with the exact gap as in v117 §4, restricted to those types;
- the L2 (k = 3) residual of v116 §4.

L4-B is closed (v113). The v143 ceiling is unchanged:
- no support-9 statement is made;
- every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
