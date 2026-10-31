# Exact Tietze certificate for the 68-source's universal CS group

**Status: SAME-AUTHOR WRITTEN-checked finite group-presentation certificate; UNREVIEWED / UNADOPTED.** This exercises `frontier-20261028-universal-cs-group-presentation-v1.md`, SHA `22f600563e2edf428ed122050c2cf95472078edb70a265c468d89535a005f16c`, without assuming the resulting universal group in advance. Its interpretation as the least CS quotient still depends on that written theorem.

For the pinned source table S68 and its computed finest source rows/columns (two rows, three columns), normalize the base row/column of the universal Rees matrix. Its group presentation has 70 generators: 68 source letters x₀,…,x₆₇ and the two non-base matrix entries p_(C₁,R₁), p_(C₂,R₁). The 4,624 source equations are `x_(st)=x_s p_(C_s,R_t) x_t`.

`frontier-20261028-quotient68-universal-group-trace-v1.json`, SHA `d0bcb92f8ba5b42e35374034f6dbe1f6d33df35db32f9c200ff7e6bd8426fab7`, records 69 exact Tietze generator eliminations. Each eliminates a generator appearing exactly once (positive or negative) in a current relator, solves for it in the other generators, and substitutes through the remaining presentation. Freely cancelling, conjugating cyclically and inverting relators preserves the presented group. The final presentation is

`<t | t²=1, t⁴=1>`.

The second relator is redundant, and the literal refined actor's group-bit map satisfies every original equation while sending t nontrivially to C₂. Hence the presented group is **exactly C₂**, not a proper quotient of it.

The trace producer is `frontier-20261028-quotient68-universal-group-tietze-v1.py`, SHA `5ccd2f44cf3cca13b261a11ab5d43c368ce70e28fccb63d43c8385447ab5dd75`. Its first development run reached the correct two final relators but failed an overly strict assertion expecting only t²; the assertion was repaired to retain t⁴ explicitly as redundant, and the final run passed. No source/proof byte was changed after pinning.

The separate literal trace replayer `frontier-20261028-quotient68-universal-group-replay-v1.py`, SHA `bb69603f67c672ad50cc82d87fedb6d744fae6143ce690d01394356c0a4e9339`, completed in the Python eval kernel before Wed Oct 28 23:06:51 PDT 2026. It reconstructs every source relator, checks that each cited relator is present, validates its one-occurrence elimination and solved replacement, substitutes/reduces all relators, checks the active generator set and final presentation, and checks the nontrivial C₂ map. It does not import Z3 or a group solver. It shares the author's source/table assumptions and basic free-group implementation concepts; independent proof/certificate review remains required.

Together with the two-row/three-column result, the general universal-Rees theorem would identify the least CS quotient as the 12-element refined actor. The certificate does not by itself prove that universal theorem, host injectivity, novelty, or any all-source Q1 result.
