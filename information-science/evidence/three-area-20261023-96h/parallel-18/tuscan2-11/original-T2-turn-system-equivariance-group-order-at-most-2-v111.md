# Original Tuscan-2(11): the turn system of every eligible array has equivariance group of order at most 2

Actual `/bin/date` before this body: **Mon Oct 26 16:02:08 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE on the unrestricted eligible family. It is not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, chosen row or chosen control.

**Uses.** (R1)–(R3) of `selection-v1.md` lines 7–11. The distance-two condition (R3) enters in §4.

**Imports.**
- v1 (SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`): Lemma 1, Theorem 2.
- v110 (SHA256 `6bf459e45faf661b5de6523ec80e4b70ecf09968a8ab0b15b6957aa1ecc89db6`): Theorem 3.1.

## 1. Definition and statement

The turn system {K_x} is **G-equivariant**, for a group G of symbol permutations, if K_(gx)(ga) = g·K_x(a) for all g, x, a. Let Eq be the largest such group. Neither the boundary data p, f nor the square need be invariant. A G-invariant square is already impossible by `unrestricted-prime-order-asymmetry-v1.md`; here only the turns are assumed symmetric.

**Theorem.** For every eligible Tuscan-2(11) array, |Eq| ≤ 2, and a non-identity element of Eq has cycle type 2^5·1.

In particular, no eligible array has a turn system with a symmetry of order 3, 4, 5, 7 or 11. This covers every multiplicative or affine turn mechanism on Z_11, Latin case or not.

## 2. A non-identity equivariance fixes at most one symbol (T1)

Let g ∈ Eq, g ≠ id, and suppose g fixes two symbols a ≠ x.
- The arc (a,x) is g-fixed. Since T commutes with g, the whole T-cycle through (a,x) consists of g-fixed arcs.
- Every symbol on that face is therefore g-fixed. But each of its rows contains all 11 symbols, so g = id. Contradiction.

**Consequences.**
- A prime order q ∈ Eq must satisfy 11 ≡ 0 or 1 (mod q), with at most one fixed point. Hence q ∈ {2, 5, 11}, with cycle types 2^5·1, 5^2·1 and 11.
- An element of order 4 would square to an involution fixing 2b+1 ≥ 3 points, unless b = 0, which would give 4a = 10. So there are no elements of order 4.
- Elements of order 6, 10, 15, … have powers of order 3 or 5, so they reduce to those cases.

## 3. Order 11 (T1)

An element of order 11 is an 11-cycle. After relabelling it is x ↦ x+1, and v110 Theorem 3.1 excludes it.

## 4. Order 5 (uses (R3))

After relabelling, g is x ↦ 3x, generating the squares S = {1,3,4,5,9} of Z_11.

### 4.1 Types and faces

S acts freely on the 110 arcs, since a fixed arc would need a = x = 0. Its 22 orbits ("types") are:
- 18 types of arcs with both ends non-zero;
- 2 types of II-arcs (y,0), for y a square or a non-square;
- 2 types of III-arcs (0,z).

T permutes the types; call this permutation σ.

**Each σ-cycle contains II and III types.**
- Every face contains the symbol 0, so every σ-cycle contains a II or a III type.
- T(y,0) = (0, K_0(y)) is a III-arc, and the T-preimage of a III-arc is a II-arc.
- So every σ-cycle contains both a II and a III type, and there are at most two σ-cycles.

**Lifting σ-cycles to faces.** Over a σ-cycle of length λ, T^λ acts as one element s ∈ S, by equivariance and commutativity. So its faces have length λ·ord(s), with ord(s) ∈ {1,5}.

**ord(s) = 1 is impossible.**
- ord(s) = 1 gives five faces of length λ. This forces λ = 20 (all 22 types in one cycle would give length 22).
- The other σ-cycle would then have length 2, i.e. (II, III). That needs K_z(0) = 0 for a whole S-orbit of z. So p(z) = f(z) = 0 for five z, and 0 would sit in column 9 of five rows and column 1 of five rows, plus columns 0 and 10. That is 12 > 11 rows. Contradiction.

**So every face is S-invariant.** S acts on a face of length L = 10r by the subgroup ⟨L/5⟩ of Z_L. Writing ℓ = 2r, some g_0 ∈ S satisfies s_(i+kℓ) = g_0^k·s_i for all i and k.

### 4.2 Window relations when 5 ∤ r

Rows of the face are R_m = (s_(p+j))_(j=0..10) with p = φ + 10m. If 5 ∤ r there are integers k, k′ with kℓ ≡ 2 and k′ℓ ≡ 8 (mod 10).

**Claim 1.** {R_m[0], R_m[1]} = {R_(m+1)[1], R_(m+1)[2]}.

Proof. The segment [p+2, p+12] equals g_0^k applied to the window starting at p − kℓ + 2, which is a window start. So it carries all 11 symbols. Comparing it with R_m = [p, p+10] gives the claim.

**Claim 2.** {R_m[8], R_m[9]} = {R_(m+1)[9], R_(m+1)[10]}, in the same way via k′.

**Resolving the claims.**
- In Claim 1, the alternative R_(m+1)[1] = R_m[0], R_(m+1)[2] = R_m[1] repeats the adjacency (R_m[0], R_m[1]), contradicting (R2). So R_(m+1)[1] = R_m[1] =: c and R_(m+1)[2] = R_m[0] = v_m.
- Likewise Claim 2 gives R_(m+1)[9] = R_m[9] =: d and R_(m+1)[10] = R_m[8], i.e. R_m[8] = v_(m+2).

So every row of the face reads (v_m, c, v_(m−1), …, v_(m+2), d, v_(m+1)).
- If r ≥ 3, the distance-two event (v_(m+1), v_m) occurs in row m+1 (middle c) and in row m−1 (middle d). This contradicts (R3).
- If r = 2, row m+1 contains v_(m+1) twice. This contradicts (R1).

### 4.3 Conclusion for order 5

Either there is one face with r = 11, or two faces with r_1 + r_2 = 11. In the second case 5 | r_i forces the other to be 6 or 1, and a face needs at least 2 rows. So some face has 5 ∤ r, and §4.2 applies. Order 5 is impossible.

In the one-face case (r = 11) all eleven symbols are cuts of that face, so §4.2 gives c = f(v) for every v, including v = c. The row starting at c then repeats c. So this case needs (R1)–(R2) only.

## 5. Order 2 and the bound

By §§2–4, every non-identity element of Eq is an involution of type 2^5·1, so Eq is elementary abelian. A Klein four-group whose three involutions each fix exactly one of 11 points would have (11+1+1+1)/4 orbits, which is not an integer (Burnside). Hence |Eq| ≤ 2. ∎

**Open.** Whether the involution case occurs is not decided here. For an involution-invariant face with r odd, the relation −R_m = (R_(m+h)[5..10], R_(m+h+1)[1..5]) (h = (r−1)/2, after relabelling g to x ↦ −x) is self-consistent under (R1)–(R3) as far as checked.

## 6. Result

- **WRITTEN:** the Theorem. The turn system of any eligible Tuscan-2(11) array has equivariance group of order ≤ 2, with any non-identity element of type 2^5·1.
- The order-11 and one-face order-5 cases use (R1)–(R2) only. The two-face order-5 case uses (R3).
- This strengthens v110 Theorem 3 and the square-level asymmetry theorem to the level of turn systems.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
