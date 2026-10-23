VERDICT: ACCEPT

**Scope.** I reviewed `PriorFormal.lean:1–47`, all of `Generic.lean`, and `gen_data.py`. Several things are outside this snapshot and rest on your pipeline: `PriorFormal.lean:48+`, the generated data modules, the two certificate modules, and the exported root statements. Later declarations cannot change the meaning of lines 1–47, and any axiom they add would show up in `#print axioms` if used. I found no logical or semantic defect. The generator findings below are hardening items, not defects in the claimed result. Because the root statements are not in the snapshot, the report-level claim also needs check R1 at the end.

## Logical errors: none

**(1) The semantic definitions are faithful.**

| Intended condition | Frozen clause |
|---|---|
| Blocks are unordered 3-subsets of v labelled points | `Triple v = {s : Finset (Fin v) // s.card = 3}` (`PriorFormal.lean:18–21`). Subtype equality is equality of the underlying finsets, so `Disjoint` and `⋃` act on genuine 3-sets. |
| STS: every pair lies in exactly one block | `IsSTS` `:24–25`, using `∃!` over blocks containing the pair |
| A parallel class partitions all v points | `IsParallelClass` `:28–29`, `∃!` per point. With card-3 blocks this forces a partition into v/3 blocks. |
| Exactly (v−1)/2 classes partitioning the blocks | `IsResolution` `:32–35`: indexed by `Fin ((v-1)/2)`, each class parallel, pairwise disjoint (hence distinct, since nonempty), union = B |
| KTS = STS with a resolution | `IsKTS` `:37–38`. The resolution is existentially quantified, which is the standard reading for existence. |
| v−2 constituents, pairwise block-disjoint, union = all triples | `IsLKTS` `:41–43`: `Fintype.card I = v-2`, and coverage is a stated conjunct, not derived |

Natural-number truncation is inert at both instances: 55/85, 28/43, 19/29. No condition is missing or vacuous. The two finite claims are exactly `FullGoal`'s body at t = 9 and t = 14.

**(2) The bridge cannot pass an invalid object.** Any trick would have to produce a kernel proof of the frozen `Kirkman.IsLKTS`, so the worst it could do is cause a false rejection. Each attack route is also closed inside the argument itself:

- **Dummy defaults.** The `getD` defaults in `rowAt` (`Generic.lean:100–101`) are unreachable. `hlen`, `s.length == (v-1)/2` (`:78`) and `cls.length == v/3` (`:71`) are exact, and `blocksOf`/`classesOf` (`:104–110`) only index those `Fin` ranges. The default `(0,0,0)` would fail `rowOK` anyway.
- **Truncation and rank collisions.** `rank` (`:82`) is only a bit position.
  - `rankFold_sound` (`:199–217`) needs only "equal rows ⇒ equal rank", so a collision makes the fold return `none` and fail closed.
  - The pair encoding `v*x+y` is injective given `y < v` (`base_eq`, `:270–277`).
  - `2^v − 1` is exact.
- **Class-pair OR masking.** `classPairs` (`:74`) cannot detect a pair repeated inside one class. No such pair can exist, because the rows of a class are point-disjoint (`accOK … ptMask`, `:71`); the proof's `pt_unique` step relies on exactly this. Across classes, `accOK` gives pairwise disjointness and an exact union equal to `fullPairs`.
- **Omitted triples.** Coverage follows from three facts:
  - the map `F` on `Fin (v-2) × Fin ((v-1)/2) × Fin (v/3)` is injective;
  - `Fintype.card_finset_len` gives the codomain size;
  - `hcard` matches the counts: 55·28·19 = 29260 = C(57,3) and 85·43·29 = 105995 = C(87,3), which I checked by hand.

  The `⋃ = univ` conjunct is then proved via `F_surj`, not assumed.
- **Duplicates.**
  - The same row twice within a class makes the `ptMask`s overlap.
  - The same row in two classes makes the class pair masks overlap.
  - The same row in two systems violates `allRows` `Nodup`.

  `rowOK` forces sorted rows, so `row_eq_of_rowSet_eq` (`:303–324`) makes row-distinctness the same as triple-distinctness.
- **Hidden hypotheses and cardinality tricks.** There is no `variable` and no axiom, and all four hypotheses are explicit (`:339–343`). `card I = v−2` is discharged by `Fintype.card_fin`.

**(3) The obligations are executable checks.** The four hypotheses are closed, decidable facts about literals:
- a list length;
- Bool checks;
- `Nodup`, obtained via `nodup_of_rankFold` and `rankFold_append`;
- a numeral identity.

None of them mentions `IsSTS`, `IsLKTS`, sets or uniqueness. The intermediate rank-fold accumulators in the certificate source are untrusted: segments must chain end-to-start, so a wrong value simply fails. `decide +kernel` yields a proof that the kernel re-evaluates by unfolding definitions. It introduces no `Lean.ofReduceBool` or `trustCompiler`; those come only from `+native`/`native_decide`.

## Data-binding problems: none blocking; three hardening items

**(4) The generator preserves rows.**
- Rows are emitted verbatim in raw order, with no sorting, deduplication or repair (`gen_data.py:64–80`).
- Each row line must have exactly 3 tokens (`:38`).
- `KTS`/`CLASS` labels must be consecutive (`:30`, `:34`), and the header must be exactly `LKTS v`, once (`:26`).
- Structural extras or omissions become length failures in Lean. Unsorted or out-of-range rows fail `rowOK`.
- The SHA-256 is computed over the same bytes that are parsed, in a single read (`:94–98`).
- The `Iff.rfl` specification theorem only restates `blocksOf` (`Generic.lean:104–105`). That is correct, but it adds no assurance by itself.

Hardening items:

- **D1 – unsanitized interpolation into Lean source.**
  - `--label` is placed inside a block comment (`:50`); `--name` is placed in a comment (`:52`) and in declaration names (`:61`, `:67`, `:75–76`).
  - A label containing `-/` closes the comment, and the rest compiles as Lean commands. Lean 4 block comments also nest on `/-`.
  - Byte-identical regeneration with the worker's arguments reproduces any injection, so it is no defence.
  - **Fix:** require `name` to fullmatch `[A-Za-z][A-Za-z0-9_]*`, and reject labels containing `/-`, `-/` or control characters. Alternatively, inspect the generated header.
  - R1 plus the axiom audit bound the impact.
- **D2 – lenient tokens.**
  - Python `int()` (`:30`, `:34`, `:40`) accepts `+5`, `05` and `5_0` (read as 50). `str.split()` (`:22`) treats `\v`, `\f` and `\x1c`–`\x1f` as whitespace.
  - The Lean data come out canonical. But for a non-canonical raw file, the claim "the bytes with this SHA encode this object" would depend on which parser reads them.
  - **Fix:** require every data token to fullmatch `0|[1-9][0-9]*`, or run that regex once over the two pinned raw files.
- **D3 – encoding versus reported hash.**
  - `write_text` (`:100`) uses the locale encoding, while the printed `out_sha256` (`:103`) hashes the UTF-8 bytes. The output contains the non-ASCII `×` (`:67`, `:75`).
  - This is moot under a UTF-8 macOS locale.
  - **Fix:** hash the files on disk with an independent tool, or write the bytes explicitly as UTF-8.

The Lean constant `…RawSha256` (`:61`) is an uninterpreted string; nothing in the kernel ties it to the data.

## Reporting limits

**(5)** The minimum the report should state:

1. **Exact claim.** Two closed theorems, `∃ B : Fin (v−2) → Kirkman.Blocks v, Kirkman.IsLKTS B` for v ∈ {57, 87}, over PriorFormal SHA `a39613c9…`, with the root theorems named. That these definitions mean "LKTS(v)" is a human review judgment (this report), not something the kernel checked.
2. **Trust base.**
   - **Kernel:** a single implementation, Lean 4.34.1, including its GMP-backed `Nat` operations. Those do all the heavy work: pair masks up to bit 7481, rank accumulators around 10⁵ bits.
   - **Axioms:** `propext`, `Classical.choice`, `Quot.sound`.
   - **Mathlib d13f23b7:** fixes the meaning of `Finset`, `Fintype.card`, `Set`, `Disjoint`, `Pairwise` and `∃!`.
   - **Replay:** `leanchecker --fresh` re-checks the import closure through the same kernel code. It guards against elaborator, olean and environment faults, not kernel bugs.
   - **Not used:** a second kernel or Comparator.
3. **Binding to the raw files happens outside the kernel.** The kernel never sees the raw files. The statement "the file with SHA `09a9d8ca…`/`65ab29ae…` is an LKTS(v)" also rests on `gen_data.py` (give its SHA) and the regeneration comparison. The bare existence claim does not.
4. **Scope.** No other v, no `FullGoal`, no novelty or priority. Nothing about how the data were constructed, the seed development in PriorFormal, automorphisms, or isomorphism classes.
5. **The existential hides the resolution.** The raw `CLASS` partitions serve as the resolutions inside the proof, but no exported theorem says so. Claim that only after exporting `∀ i, IsResolution (blocksOf v d i) (classesOf v d i)`.
6. **Independence.** The Lean check is independent in method from the three earlier verifiers, but all four examined the same bytes. That agreement partly offsets the single-kernel limit.

**R1 (required, cheap) – statement audit for modules outside the snapshot.** Elaborate the target in a file that imports only PriorFormal, so nothing defined in the data or certificate modules can affect how it is read:

```lean
import LktsKernel.PriorFormal
def Kirkman.Audit.Target (v : ℕ) : Prop := ∃ B : Fin (v - 2) → Kirkman.Blocks v, Kirkman.IsLKTS B
```

Then, in a file that also imports the certificate roots:

```lean
theorem audit57 : Kirkman.Audit.Target 57 := <root57>
theorem audit87 : Kirkman.Audit.Target 87 := <root87>
#print axioms audit57
#print axioms audit87
```

Run `leanchecker --fresh` on that file. This confirms that each root's type is definitionally the target, with no leftover hypotheses, and that only the three standard axioms are used.
