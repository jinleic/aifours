overall_correctness: correct

explanation: The literal collision derivation is valid at the stated universal-band presentation: the two branches contain 14 and 66 primitive replacements, respectively. The source relations are used only as explicitly tagged identities of source-element names; the derivation does not establish source separation or an all-host negative witness. Scientific execution was prohibited by my inherited shell role, so the fresh checker below is NOT RUN and this return is not an executed FINITE gate.

confidence: 0.97

Findings: none.

# F608 — Full FINITE return

## 1. Read and execution account

Before opening the mathematical packet, I read the complete manifest, freeze receipt, and all 13 controls, in their declared order and through their endings, using raw ranges of at most 20 lines. I also read the complete parent metadata supply. Main received my direct prebody acknowledgement before the first packet read.

The control lengths, in manifest order, were 15, 14, 23, 11, 9, 8, 49, 23, 16, 20, 22, 22, and 23 LF.

After that acknowledgement, I read the entire packet, lines 1–980, in consecutive raw ranges of at most 20 lines, including:

- S1: F588 lines 1–429;
- S2: F588 lines 732–759, including its conclusion;
- S3: F492 lines 1–521, including its conclusion.

I did not open F588’s excluded implementation, any F586 mathematical body, or any held consumer. All 13 controls were used only for permission/status boundaries.

Pins supplied by Main:

- Manifest SHA256: `117f3ea81e27e0d27f5304b70aad044f800f28043e98b455650ae4595374601a`
- Receipt SHA256: `7fbd13afc7317eeb990f01c67d64f9f26e5e5e7c549bd355ed704a9c11e00650`
- Packet SHA256: `ffcb5a7067eee81c17a5a15180ba79d66d61e12859c94e442f52deecbd1c3c04`

These are parent-supplied observations, not child-recomputed hashes or child-native timestamps.

The only shell call was read-only `git diff` scoped to this wave’s manifest, receipt, and packet; it returned no output. That observation is not a mathematical verification.

**Scientific executions: 0. Executed primitive checks: 0. Executed mutation controls: 0.**

My inherited role permits read-only review shell commands, not scientific execution. I did not bypass it with another runner or tool. The complete fresh checker in §7 is therefore **NOT RUN**. Its expected counts below are written deductions, not measured output.

No working-tree file was written. This is the full body for Main’s materialization.

## 2. Exact target and notation

The source remains the specified \(S=S_0/\theta\), with exactly the four declared congruence pairs:

\[
\begin{aligned}
\mathrm{R1}:&\quad eaa'=e,\\
\mathrm{R2}:&\quad ebb'=e,\\
\mathrm{R3}:&\quad a'afg=fg,\\
\mathrm{R4}:&\quad b'bfa'eafg=fa'eafg.
\end{aligned}
\]

The prescribed quotient has

\[
q(a)=q(a')=q(b)=q(b')=1,\qquad q(e)=q(f)=q(g)=0.
\]

The actual source words are

\[
U=eafg,\qquad V=ebfa'eafg.
\]

Both have grade 1.

Write `[h,w]` for the universal generator \((h,[w]_S)\). Concatenated bracketed expressions are words in the universal alphabet, **not an assertion that their arrows compose**.

There are only two primitive replacement types:

- `E` / `C`: expansion / contraction of
  \[
  [h,st]\longleftrightarrow[h,s][h+q(s),t].
  \]
- `I+` / `I−`: expansion / contraction of a nonempty word square.

Every locus below is zero-based in the complete **before** word.

`N(Ri@p)` denotes a separate, zero-primitive-step change between the two expressly declared names in Ri, at token position \(p\). It is not an additional defining relation of \(C_q\), an arbitrary source-word equality test, or an extra primitive replacement.

## 3. All 80 primitive replacements

The following displays all 80 replacements, with complete typed before/after words. They are organized into the two branches for readability.

The ordered endpoint-to-endpoint certificate is:

\[
U01,\ldots,U14,\quad
V66^{-1},V65^{-1},\ldots,V01^{-1}.
\]

For an inverse row, swap its displayed before/after words, invert `E/C` or `I+/I−`, and reverse any adjacent zero-step name change. The displayed locus remains the same. Thus this specifies the entire ordered chain from `[0,eafg]` to `[0,ebfa'eafg]`, not merely its endpoints or a macro hash.

### 3.1 U branch: 14 primitive replacements

U01 — E@0  
`[0,eafg] → [0,eaf][1,g]`

U02 — E@0  
`[0,eaf][1,g] → [0,ea][1,f][1,g]`

U03 — E@0  
`[0,ea][1,f][1,g] → [0,e][0,a][1,f][1,g]`

U04 — C@2  
`[0,e][0,a][1,f][1,g] → [0,e][0,a][1,fg]`  
Then `N(R3@2): [1,fg] → [1,a'afg]`.

U05 — E@2  
`[0,e][0,a][1,a'afg] → [0,e][0,a][1,a'af][1,g]`

U06 — E@2  
`[0,e][0,a][1,a'af][1,g] → [0,e][0,a][1,a'a][1,f][1,g]`

U07 — E@2  
`[0,e][0,a][1,a'a][1,f][1,g] → [0,e][0,a][1,a'][0,a][1,f][1,g]`

U08 — I+@2, block `[1,a']`  
`[0,e][0,a][1,a'][0,a][1,f][1,g] → [0,e][0,a][1,a'][1,a'][0,a][1,f][1,g]`

U09 — C@0  
`[0,e][0,a][1,a'][1,a'][0,a][1,f][1,g] → [0,ea][1,a'][1,a'][0,a][1,f][1,g]`

U10 — C@0  
`[0,ea][1,a'][1,a'][0,a][1,f][1,g] → [0,eaa'][1,a'][0,a][1,f][1,g]`  
Then `N(R1@0): [0,eaa'] → [0,e]`.

U11 — C@1  
`[0,e][1,a'][0,a][1,f][1,g] → [0,e][1,a'a][1,f][1,g]`

U12 — C@1  
`[0,e][1,a'a][1,f][1,g] → [0,e][1,a'af][1,g]`

U13 — C@1  
`[0,e][1,a'af][1,g] → [0,e][1,a'afg]`  
Then `N(R3@1): [1,a'afg] → [1,fg]`.

U14 — E@1  
`[0,e][1,fg] → [0,e][1,f][1,g]`

The common terminal word is `[0,e][1,f][1,g]`.

### 3.2 V branch: 66 primitive replacements

V01 — E@0  
`[0,ebfa'eafg] → [0,ebfa'eaf][1,g]`

V02 — E@0  
`[0,ebfa'eaf][1,g] → [0,ebfa'ea][1,f][1,g]`

V03 — E@0  
`[0,ebfa'ea][1,f][1,g] → [0,ebfa'e][0,a][1,f][1,g]`

V04 — E@0  
`[0,ebfa'e][0,a][1,f][1,g] → [0,ebfa'][0,e][0,a][1,f][1,g]`

V05 — E@0  
`[0,ebfa'][0,e][0,a][1,f][1,g] → [0,ebf][1,a'][0,e][0,a][1,f][1,g]`

V06 — E@0  
`[0,ebf][1,a'][0,e][0,a][1,f][1,g] → [0,eb][1,f][1,a'][0,e][0,a][1,f][1,g]`

V07 — E@0  
`[0,eb][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,f][1,a'][0,e][0,a][1,f][1,g]`

V08 — C@2  
`[0,e][0,b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,fa'][0,e][0,a][1,f][1,g]`

V09 — C@2  
`[0,e][0,b][1,fa'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,fa'e][0,a][1,f][1,g]`

V10 — C@2  
`[0,e][0,b][1,fa'e][0,a][1,f][1,g] → [0,e][0,b][1,fa'ea][1,f][1,g]`

V11 — C@2  
`[0,e][0,b][1,fa'ea][1,f][1,g] → [0,e][0,b][1,fa'eaf][1,g]`

V12 — C@2  
`[0,e][0,b][1,fa'eaf][1,g] → [0,e][0,b][1,fa'eafg]`  
Then `N(R4@2): [1,fa'eafg] → [1,b'bfa'eafg]`.

V13 — E@2  
`[0,e][0,b][1,b'bfa'eafg] → [0,e][0,b][1,b'bfa'eaf][1,g]`

V14 — E@2  
`[0,e][0,b][1,b'bfa'eaf][1,g] → [0,e][0,b][1,b'bfa'ea][1,f][1,g]`

V15 — E@2  
`[0,e][0,b][1,b'bfa'ea][1,f][1,g] → [0,e][0,b][1,b'bfa'e][0,a][1,f][1,g]`

V16 — E@2  
`[0,e][0,b][1,b'bfa'e][0,a][1,f][1,g] → [0,e][0,b][1,b'bfa'][0,e][0,a][1,f][1,g]`

V17 — E@2  
`[0,e][0,b][1,b'bfa'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,b'bf][1,a'][0,e][0,a][1,f][1,g]`

V18 — E@2  
`[0,e][0,b][1,b'bf][1,a'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,b'b][1,f][1,a'][0,e][0,a][1,f][1,g]`

V19 — E@2  
`[0,e][0,b][1,b'b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g]`

V20 — I+@2, block `[1,b']`  
`[0,e][0,b][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][0,b][1,b'][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g]`

V21 — C@0  
`[0,e][0,b][1,b'][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,eb][1,b'][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g]`

V22 — C@0  
`[0,eb][1,b'][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,ebb'][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g]`  
Then `N(R2@0): [0,ebb'] → [0,e]`.

V23 — C@1  
`[0,e][1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][1,b'b][1,f][1,a'][0,e][0,a][1,f][1,g]`

V24 — C@1  
`[0,e][1,b'b][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][1,b'bf][1,a'][0,e][0,a][1,f][1,g]`

V25 — C@1  
`[0,e][1,b'bf][1,a'][0,e][0,a][1,f][1,g] → [0,e][1,b'bfa'][0,e][0,a][1,f][1,g]`

V26 — C@1  
`[0,e][1,b'bfa'][0,e][0,a][1,f][1,g] → [0,e][1,b'bfa'e][0,a][1,f][1,g]`

V27 — C@1  
`[0,e][1,b'bfa'e][0,a][1,f][1,g] → [0,e][1,b'bfa'ea][1,f][1,g]`

V28 — C@1  
`[0,e][1,b'bfa'ea][1,f][1,g] → [0,e][1,b'bfa'eaf][1,g]`

V29 — C@1  
`[0,e][1,b'bfa'eaf][1,g] → [0,e][1,b'bfa'eafg]`  
Then `N(R4@1): [1,b'bfa'eafg] → [1,fa'eafg]`.

V30 — E@1  
`[0,e][1,fa'eafg] → [0,e][1,fa'eaf][1,g]`

V31 — E@1  
`[0,e][1,fa'eaf][1,g] → [0,e][1,fa'ea][1,f][1,g]`

V32 — E@1  
`[0,e][1,fa'ea][1,f][1,g] → [0,e][1,fa'e][0,a][1,f][1,g]`

V33 — E@1  
`[0,e][1,fa'e][0,a][1,f][1,g] → [0,e][1,fa'][0,e][0,a][1,f][1,g]`

V34 — E@1  
`[0,e][1,fa'][0,e][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,e][0,a][1,f][1,g]`

V35 — C@5  
`[0,e][1,f][1,a'][0,e][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,e][0,a][1,fg]`  
Then `N(R3@5): [1,fg] → [1,a'afg]`.

V36 — E@5  
`[0,e][1,f][1,a'][0,e][0,a][1,a'afg] → [0,e][1,f][1,a'][0,e][0,a][1,a'af][1,g]`

V37 — E@5  
`[0,e][1,f][1,a'][0,e][0,a][1,a'af][1,g] → [0,e][1,f][1,a'][0,e][0,a][1,a'a][1,f][1,g]`

V38 — E@5  
`[0,e][1,f][1,a'][0,e][0,a][1,a'a][1,f][1,g] → [0,e][1,f][1,a'][0,e][0,a][1,a'][0,a][1,f][1,g]`

V39 — I+@5, block `[1,a']`  
`[0,e][1,f][1,a'][0,e][0,a][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,e][0,a][1,a'][1,a'][0,a][1,f][1,g]`

V40 — C@3  
`[0,e][1,f][1,a'][0,e][0,a][1,a'][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,ea][1,a'][1,a'][0,a][1,f][1,g]`

V41 — C@3  
`[0,e][1,f][1,a'][0,ea][1,a'][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,eaa'][1,a'][0,a][1,f][1,g]`  
Then `N(R1@3): [0,eaa'] → [0,e]`.

V42 — C@4  
`[0,e][1,f][1,a'][0,e][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,a'a][1,f][1,g]`

V43 — C@4  
`[0,e][1,f][1,a'][0,e][1,a'a][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,a'af][1,g]`

V44 — C@4  
`[0,e][1,f][1,a'][0,e][1,a'af][1,g] → [0,e][1,f][1,a'][0,e][1,a'afg]`  
Then `N(R3@4): [1,a'afg] → [1,fg]`.

V45 — E@4  
`[0,e][1,f][1,a'][0,e][1,fg] → [0,e][1,f][1,a'][0,e][1,f][1,g]`

V46 — I+@4, block `[1,f]`  
`[0,e][1,f][1,a'][0,e][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,f][1,g]`

V47 — C@5  
`[0,e][1,f][1,a'][0,e][1,f][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,fg]`  
Then `N(R3@5): [1,fg] → [1,a'afg]`.

V48 — E@5  
`[0,e][1,f][1,a'][0,e][1,f][1,a'afg] → [0,e][1,f][1,a'][0,e][1,f][1,a'af][1,g]`

V49 — E@5  
`[0,e][1,f][1,a'][0,e][1,f][1,a'af][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,a'a][1,f][1,g]`

V50 — E@5  
`[0,e][1,f][1,a'][0,e][1,f][1,a'a][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,a'][0,a][1,f][1,g]`

V51 — I+@5, block `[1,a']`  
`[0,e][1,f][1,a'][0,e][1,f][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'][0,a][1,f][1,g]`

V52 — C@6  
`[0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'a][1,f][1,g]`

V53 — C@6  
`[0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'a][1,f][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'af][1,g]`

V54 — C@6  
`[0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'af][1,g] → [0,e][1,f][1,a'][0,e][1,f][1,a'][1,a'afg]`  
Then `N(R3@6): [1,a'afg] → [1,fg]`.

V55 — E@6  
`[0,e][1,f][1,a'][0,e][1,f][1,a'][1,fg] → [0,e][1,f][1,a'][0,e][1,f][1,a'][1,f][1,g]`

V56 — I−@0, block `[0,e][1,f][1,a']`  
`[0,e][1,f][1,a'][0,e][1,f][1,a'][1,f][1,g] → [0,e][1,f][1,a'][1,f][1,g]`

V57 — C@3  
`[0,e][1,f][1,a'][1,f][1,g] → [0,e][1,f][1,a'][1,fg]`  
Then `N(R3@3): [1,fg] → [1,a'afg]`.

V58 — E@3  
`[0,e][1,f][1,a'][1,a'afg] → [0,e][1,f][1,a'][1,a'af][1,g]`

V59 — E@3  
`[0,e][1,f][1,a'][1,a'af][1,g] → [0,e][1,f][1,a'][1,a'a][1,f][1,g]`

V60 — E@3  
`[0,e][1,f][1,a'][1,a'a][1,f][1,g] → [0,e][1,f][1,a'][1,a'][0,a][1,f][1,g]`

V61 — I−@2, block `[1,a']`  
`[0,e][1,f][1,a'][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'][0,a][1,f][1,g]`

V62 — C@2  
`[0,e][1,f][1,a'][0,a][1,f][1,g] → [0,e][1,f][1,a'a][1,f][1,g]`

V63 — C@2  
`[0,e][1,f][1,a'a][1,f][1,g] → [0,e][1,f][1,a'af][1,g]`

V64 — C@2  
`[0,e][1,f][1,a'af][1,g] → [0,e][1,f][1,a'afg]`  
Then `N(R3@2): [1,a'afg] → [1,fg]`.

V65 — E@2  
`[0,e][1,f][1,fg] → [0,e][1,f][1,f][1,g]`

V66 — I−@1, block `[1,f]`  
`[0,e][1,f][1,f][1,g] → [0,e][1,f][1,g]`

### 3.3 Written counts

These are **written counts, not executed checker output**.

| Chain | C | E | I+ | I− | Primitive total | Zero-step names |
|---|---:|---:|---:|---:|---:|---:|
| U branch | 6 | 7 | 1 | 0 | 14 | 3 |
| V branch | 28 | 31 | 4 | 3 | 66 | 10 |
| U followed by reversed V | 37 | 35 | 4 | 4 | **80** | **13** |

The 13 source-name changes use R1 twice, R2 once, R3 eight times, and R4 twice. They are not included in the primitive total.

In particular, the composite square at V56 is essential to this certificate. A checker restricted to generator squares cannot verify it.

## 4. Typed consumers and the source-equality boundary

The H3 chain begins at index 1:

\[
[1,a'][0,a][1,f][1,g]
\to[1,a'a][1,f][1,g]
\to[1,a'af][1,g]
\to[1,a'afg]
=_{\mathrm{R3}}[1,fg]
\to[1,f][1,g].
\]

The H4 chain also begins at index 1. Its token indices are exactly

\[
[1,b'][0,b][1,f][1,a'][0,e][0,a][1,f][1,g],
\]

and its right side is

\[
[1,f][1,a'][0,e][0,a][1,f][1,g].
\]

Thus the producing source relations reach their actual consuming cocycle positions with the required shifts; neither H3 nor H4 is silently treated as an index-0 identity.

The first loss of source-path composability is U08. In U07, `[1,a']` goes from 1 to 0. Its duplicated successor `[1,a']` starts at 1, so the adjacent copies do not compose. U08 is nevertheless a valid nonempty word-square replacement in the universal band.

Consequently, this certificate proves COLL but is not a source-congruence derivation of \(U=V\). Conversely, its failure to remain composable does not prove \(U\ne V\).

## 5. Actual four-element positive-control image

Let

\[
T=\{E_0,E_1,F_0,F_1\},\qquad
L_iM_j=L_{i+j\pmod2}.
\]

This is the direct product of the two-element left-zero band with \(C_2\), with trivial action.

Its complete multiplication table is:

| · | E₀ | E₁ | F₀ | F₁ |
|---|---|---|---|---|
| E₀ | E₀ | E₁ | E₀ | E₁ |
| E₁ | E₁ | E₀ | E₁ | E₀ |
| F₀ | F₀ | F₁ | F₀ | F₁ |
| F₁ | F₁ | F₀ | F₁ | F₀ |

The quotient table is

\[
q_T(E_0)=q_T(F_0)=0,\qquad
q_T(E_1)=q_T(F_1)=1.
\]

For every three elements, both associations equal the first element’s left-zero coordinate with the sum of all three grades. This verifies associativity for all 64 triples by the displayed multiplication formula. For all 16 pairs, grade addition gives the homomorphism law.

Every element is its own regular inverse: \(xxx=x\). The idempotents are exactly \(E_0,F_0\), precisely the grade-0 fibre. The quotient is onto.

The seven-generator map is

\[
e\mapsto E_0,\quad f,g\mapsto F_0,\quad
a,a',b,b'\mapsto F_1.
\]

It is induced from the ambient construction by sending both \(e_0,e_1\) to \(E\) and every other free-band letter to \(F\). That band map is invariant under \(\tau\), so this is a homomorphism from the actual ambient semidirect product, not merely a seven-symbol assignment satisfying selected equations.

The four source pairs evaluate as follows:

| Relation | Left image | Right image |
|---|---|---|
| R1 | E₀ | E₀ |
| R2 | E₀ | E₀ |
| R3 | F₀ | F₀ |
| R4 | F₀ | F₀ |

It therefore factors through the specified \(S_0/\theta\). Its generated image is all four elements: \(E_1\) is the image of \(ea\).

Furthermore,

\[
ef\mapsto E_0\ne F_0\mapsfrom fe,
\qquad
U,V\mapsto E_1.
\]

This checks noncommuting source idempotents through a genuine image. **It does not separate U and V. The four-element image is not being substituted for the original source.**

These are exact written checks. The exhaustive table loops in the source below remain NOT RUN.

## 6. Required weakened/mutated controls

The supplied checker implements the following controls, with invariant-specific rejections. None has been executed here.

| Control | Intended rejection |
|---|---|
| H3 constructed with start index 0 | `MACRO_MATCH` |
| H4 constructed with start index 0 | `MACRO_MATCH` |
| Omitted shift on the first U endpoint expansion | `COCYCLE_TARGET` |
| Generator-only square checker applied to the full certificate | `GENERATOR_ONLY_SQUARE` |
| H3 reverse applied at U’s position 1 instead of 2 | `MACRO_MATCH` |
| Claim that the duplicated-D U word is a source path | `NOT_SOURCE_PATH` |
| Empty “xk” square block | `SQUARE_NONEMPTY` |
| Incorrect V12 macro word `XPDXPPQ` | `V12_LITERAL` |
| R4 removed from the admitted source-name pairs | `RELATION_MISSING` |
| COLL plus unknown SEP promoted to a negative witness | `SEP_UNPROVED` |

The last item is only a **scope-guard control**, not evidence for a mathematical theorem or a substitute for SEP.

The correct V12 macro word is `XPDXPDPQ`, i.e.

\[
[0,e][1,f][1,a'][0,e][1,f][1,a'][1,f][1,g].
\]

## 7. Fresh standalone checker — NOT RUN

This source uses only the Python standard library. Its inputs are literal constants, and it performs no filesystem reads/writes, networking, subprocesses, installations, or external-model calls. Its only output is standard output. It includes a cooperative 55-second ceiling.

For a lossless materialization, remove the leading `SRC|` from every source line. The first character after that prefix is the first character of the Python line. Uppercase source letters `A` and `B` mean \(a'\) and \(b'\); the output formatter prints the primes explicitly.

**Execution status: NOT RUN. No stdout, elapsed time, checker hash, or passing-control result is claimed.**

SRC|from collections import Counter
SRC|from itertools import product
SRC|from time import monotonic
SRC|
SRC|class Rejected(Exception):
SRC|    pass
SRC|
SRC|def need(condition, reason):
SRC|    if not condition:
SRC|        raise Rejected(reason)
SRC|
SRC|LIMIT = None
SRC|
SRC|def tick():
SRC|    if LIMIT is not None:
SRC|        need(monotonic() < LIMIT, "DEADLINE")
SRC|
SRC|Q = dict(a=1, A=1, b=1, B=1, e=0, f=0, g=0)
SRC|R = {
SRC|    1: ("eaA", "e"),
SRC|    2: ("ebB", "e"),
SRC|    3: ("Aafg", "fg"),
SRC|    4: ("BbfAeafg", "fAeafg"),
SRC|}
SRC|ALL = frozenset(R)
SRC|U = "eafg"
SRC|V = "ebfAeafg"
SRC|SYMBOL = {
SRC|    "X": (0, "e"), "A": (0, "a"), "D": (1, "A"),
SRC|    "B": (0, "b"), "J": (1, "B"),
SRC|    "P": (1, "f"), "Q": (1, "g"),
SRC|}
SRC|
SRC|def parity(s):
SRC|    need(type(s) is str and bool(s), "SOURCE_NONEMPTY")
SRC|    need(all(c in Q for c in s), "SOURCE_ALPHABET")
SRC|    return sum(Q[c] for c in s) % 2
SRC|
SRC|def validate_word(w):
SRC|    need(type(w) is tuple and bool(w), "UNIVERSAL_NONEMPTY")
SRC|    for token in w:
SRC|        need(type(token) is tuple and len(token) == 2, "TOKEN")
SRC|        h, s = token
SRC|        need(type(h) is int and h in (0, 1), "GROUP_INDEX")
SRC|        parity(s)
SRC|
SRC|def spelled(h, s):
SRC|    parity(s)
SRC|    out = []
SRC|    for c in s:
SRC|        out.append((h, c))
SRC|        h ^= Q[c]
SRC|    return tuple(out)
SRC|
SRC|def symbols(s):
SRC|    return tuple(SYMBOL[c] for c in s)
SRC|
SRC|def transition(kind, at, n, w, allowed=ALL, singles_only=False):
SRC|    tick()
SRC|    validate_word(w)
SRC|    need(type(at) is int and 0 <= at < len(w), "LOCUS")
SRC|    h, s = w[at]
SRC|    if kind == "E":
SRC|        need(type(n) is int and 0 < n < len(s), "SPLIT_NONEMPTY")
SRC|        left, right = s[:n], s[n:]
SRC|        middle = ((h, left), (h ^ parity(left), right))
SRC|        return w[:at] + middle + w[at + 1:]
SRC|    if kind == "C":
SRC|        need(at + 1 < len(w), "COCYCLE_PAIR")
SRC|        k, t = w[at + 1]
SRC|        need(k == (h ^ parity(s)), "COCYCLE_SHIFT")
SRC|        need(n == len(s), "CONTRACTION_SPLIT")
SRC|        return w[:at] + ((h, s + t),) + w[at + 2:]
SRC|    if kind == "N":
SRC|        need(n in allowed and n in R, "RELATION_MISSING")
SRC|        left, right = R[n]
SRC|        need(parity(left) == parity(right), "RELATION_GRADE")
SRC|        need(s == left or s == right, "RELATION_SOURCE_NAME")
SRC|        target = right if s == left else left
SRC|        return w[:at] + ((h, target),) + w[at + 1:]
SRC|    need(kind in ("I+", "I-"), "PRIMITIVE_KIND")
SRC|    need(type(n) is int and n > 0, "SQUARE_NONEMPTY")
SRC|    if singles_only:
SRC|        need(n == 1, "GENERATOR_ONLY_SQUARE")
SRC|    need(at + n <= len(w), "SQUARE_BLOCK")
SRC|    block = w[at:at + n]
SRC|    if kind == "I+":
SRC|        return w[:at] + block + block + w[at + n:]
SRC|    need(at + 2 * n <= len(w), "SQUARE_PAIR")
SRC|    need(w[at + n:at + 2 * n] == block, "SQUARE_EQUAL_HALVES")
SRC|    return w[:at] + block + w[at + 2 * n:]
SRC|
SRC|TARGET_REASON = {
SRC|    "E": "COCYCLE_TARGET", "C": "COCYCLE_TARGET",
SRC|    "N": "ALIAS_TARGET",
SRC|    "I+": "SQUARE_TARGET", "I-": "SQUARE_TARGET",
SRC|}
SRC|
SRC|def verify_event(event, allowed=ALL, singles_only=False):
SRC|    kind, at, n, before, after = event
SRC|    validate_word(after)
SRC|    expected = transition(kind, at, n, before, allowed, singles_only)
SRC|    need(expected == after, TARGET_REASON[kind])
SRC|
SRC|def step(log, w, kind, at, n):
SRC|    after = transition(kind, at, n, w)
SRC|    event = (kind, at, n, w, after)
SRC|    verify_event(event)
SRC|    log.append(event)
SRC|    return after
SRC|
SRC|def inverted(log):
SRC|    inverse_kind = {"E": "C", "C": "E", "N": "N",
SRC|                    "I+": "I-", "I-": "I+"}
SRC|    return [(inverse_kind[k], p, n, after, before)
SRC|            for k, p, n, before, after in reversed(log)]
SRC|
SRC|def macro_template(rid, override_start=None):
SRC|    h = {1: 0, 2: 0, 3: 1, 4: 1}[rid]
SRC|    if override_start is not None:
SRC|        h = override_start
SRC|    left, right = R[rid]
SRC|    w = spelled(h, left)
SRC|    log = []
SRC|    for unused in range(len(left) - 1):
SRC|        w = step(log, w, "C", 0, len(w[0][1]))
SRC|    w = step(log, w, "N", 0, rid)
SRC|    for cut in range(len(right) - 1, 0, -1):
SRC|        w = step(log, w, "E", 0, cut)
SRC|    need(w == spelled(h, right), "MACRO_TEMPLATE_END")
SRC|    return log
SRC|
SRC|def use_macro(log, w, rid, at, reverse=False, override_start=None):
SRC|    template = macro_template(rid, override_start)
SRC|    if reverse:
SRC|        template = inverted(template)
SRC|    first = template[0][3]
SRC|    need(0 <= at and w[at:at + len(first)] == first, "MACRO_MATCH")
SRC|    prefix, suffix = w[:at], w[at + len(first):]
SRC|    for kind, local, n, before, after in template:
SRC|        need(w == prefix + before + suffix, "MACRO_CONTEXT")
SRC|        event = (kind, at + local, n, w, prefix + after + suffix)
SRC|        verify_event(event)
SRC|        log.append(event)
SRC|        w = event[4]
SRC|    return w
SRC|
SRC|U_PLAN = [
SRC|    ("H", 3, 2, True), ("I+", 2, 1),
SRC|    ("H", 1, 0, False), ("H", 3, 1, False),
SRC|]
SRC|U_WORDS = ["XAPQ", "XADAPQ", "XADDAPQ", "XDAPQ", "XPQ"]
SRC|V_PLAN = [
SRC|    ("H", 4, 2, True), ("I+", 2, 1),
SRC|    ("H", 2, 0, False), ("H", 4, 1, False),
SRC|    ("H", 3, 5, True), ("I+", 5, 1),
SRC|    ("H", 1, 3, False), ("H", 3, 4, False),
SRC|    ("I+", 4, 1), ("H", 3, 5, True), ("I+", 5, 1),
SRC|    ("H", 3, 6, False), ("I-", 0, 3),
SRC|    ("H", 3, 3, True), ("I-", 2, 1),
SRC|    ("H", 3, 2, False), ("I-", 1, 1),
SRC|]
SRC|V_WORDS = [
SRC|    "XBPDXAPQ", "XBJBPDXAPQ", "XBJJBPDXAPQ", "XJBPDXAPQ",
SRC|    "XPDXAPQ", "XPDXADAPQ", "XPDXADDAPQ", "XPDXDAPQ",
SRC|    "XPDXPQ", "XPDXPPQ", "XPDXPDAPQ", "XPDXPDDAPQ",
SRC|    "XPDXPDPQ", "XPDPQ", "XPDDAPQ", "XPDAPQ", "XPPQ", "XPQ",
SRC|]
SRC|
SRC|def branch(source, plan, expected_words):
SRC|    need(len(expected_words) == len(plan) + 1, "PLAN_LENGTH")
SRC|    w = ((0, source),)
SRC|    log = []
SRC|    for cut in range(len(source) - 1, 0, -1):
SRC|        w = step(log, w, "E", 0, cut)
SRC|    need(w == symbols(expected_words[0]), "ENDPOINT_EXPANSION")
SRC|    snapshots = [w]
SRC|    for instruction, expected in zip(plan, expected_words[1:]):
SRC|        if instruction[0] == "H":
SRC|            unused, rid, at, reverse = instruction
SRC|            w = use_macro(log, w, rid, at, reverse)
SRC|        else:
SRC|            kind, at, n = instruction
SRC|            w = step(log, w, kind, at, n)
SRC|        need(w == symbols(expected), "NAMED_MACRO_WORD")
SRC|        snapshots.append(w)
SRC|    return log, snapshots
SRC|
SRC|def replay(log, start, end, allowed=ALL, singles_only=False):
SRC|    w = start
SRC|    counts = Counter()
SRC|    for event in log:
SRC|        need(event[3] == w, "CHAIN_CONTINUITY")
SRC|        verify_event(event, allowed, singles_only)
SRC|        counts[event[0]] += 1
SRC|        w = event[4]
SRC|    need(w == end, "CHAIN_ENDPOINT")
SRC|    return counts
SRC|
SRC|def require_path(w):
SRC|    validate_word(w)
SRC|    for (h, s), (k, unused) in zip(w, w[1:]):
SRC|        need(k == (h ^ parity(s)), "NOT_SOURCE_PATH")
SRC|
SRC|def conclusion_guard(coll, sep, negative_witness):
SRC|    if negative_witness:
SRC|        need(coll is True and sep is True, "SEP_UNPROVED")
SRC|    return "COLL_ONLY" if coll and sep is not True else "SCOPED"
SRC|
SRC|def reject(label, expected_reason, action):
SRC|    try:
SRC|        action()
SRC|    except Rejected as error:
SRC|        need(str(error) == expected_reason, "WRONG_REJECTION:" + label)
SRC|        print("CONTROL", label, "REJECTED", expected_reason)
SRC|        return
SRC|    raise Rejected("MUTANT_ACCEPTED:" + label)
SRC|
SRC|def controls(ulog, us, vs, chain):
SRC|    reject("H3_WRONG_START", "MACRO_MATCH",
SRC|           lambda: use_macro([], us[0], 3, 2, True, 0))
SRC|    reject("H4_WRONG_START", "MACRO_MATCH",
SRC|           lambda: use_macro([], vs[0], 4, 2, True, 0))
SRC|    kind, at, n, before, after = ulog[0]
SRC|    wrong_after = after[:1] + ((0, after[1][1]),) + after[2:]
SRC|    wrong_shift = (kind, at, n, before, wrong_after)
SRC|    reject("OMITTED_Q_SHIFT", "COCYCLE_TARGET",
SRC|           lambda: verify_event(wrong_shift))
SRC|    reject("GENERATOR_ONLY_SQUARES", "GENERATOR_ONLY_SQUARE",
SRC|           lambda: replay(chain, ((0, U),), ((0, V),),
SRC|                          singles_only=True))
SRC|    reject("WRONG_MACRO_POSITION", "MACRO_MATCH",
SRC|           lambda: use_macro([], us[0], 3, 1, True))
SRC|    require_path(us[1])
SRC|    reject("DD_SOURCE_COMPOSABLE", "NOT_SOURCE_PATH",
SRC|           lambda: require_path(us[2]))
SRC|    empty_square = ("I+", 0, 0, ((0, U),), ((0, U),))
SRC|    reject("EMPTY_XK", "SQUARE_NONEMPTY",
SRC|           lambda: verify_event(empty_square))
SRC|    need(vs[12] == symbols("XPDXPDPQ"), "CORRECT_V12")
SRC|    reject("WRONG_V12_WORD", "V12_LITERAL",
SRC|           lambda: need(vs[12] == symbols("XPDXPPQ"), "V12_LITERAL"))
SRC|    reject("MISSING_R4", "RELATION_MISSING",
SRC|           lambda: replay(chain, ((0, U),), ((0, V),),
SRC|                          allowed=frozenset((1, 2, 3))))
SRC|    need(conclusion_guard(True, None, False) == "COLL_ONLY", "SCOPE")
SRC|    reject("COLL_AS_NEGATIVE_WITNESS_SCOPE_GUARD", "SEP_UNPROVED",
SRC|           lambda: conclusion_guard(True, None, True))
SRC|
SRC|def finite_image():
SRC|    carrier = ((0, 0), (0, 1), (1, 0), (1, 1))
SRC|    index = {x: i for i, x in enumerate(carrier)}
SRC|    def mul(i, j):
SRC|        left, h = carrier[i]
SRC|        unused, k = carrier[j]
SRC|        return index[(left, h ^ k)]
SRC|    table = tuple(tuple(mul(i, j) for j in range(4))
SRC|                  for i in range(4))
SRC|    expected = ((0, 1, 0, 1), (1, 0, 1, 0),
SRC|                (2, 3, 2, 3), (3, 2, 3, 2))
SRC|    need(table == expected, "IMAGE_TABLE")
SRC|    grades = tuple(h for unused, h in carrier)
SRC|    for i, j, k in product(range(4), repeat=3):
SRC|        tick()
SRC|        need(mul(mul(i, j), k) == mul(i, mul(j, k)), "IMAGE_ASSOC")
SRC|    for i, j in product(range(4), repeat=2):
SRC|        need(grades[mul(i, j)] == (grades[i] ^ grades[j]), "IMAGE_Q")
SRC|    for i in range(4):
SRC|        inverse = i
SRC|        need(mul(mul(i, inverse), i) == i, "IMAGE_INVERSE_LEFT")
SRC|        need(mul(mul(inverse, i), inverse) == inverse,
SRC|             "IMAGE_INVERSE_RIGHT")
SRC|        need((mul(i, i) == i) == (grades[i] == 0), "IMAGE_PURITY")
SRC|    need(set(grades) == {0, 1}, "IMAGE_ONTO")
SRC|    for h, k, l in product(range(2), repeat=3):
SRC|        need(((h ^ k) ^ l) == (h ^ (k ^ l)), "GROUP_ASSOC")
SRC|    for h in range(2):
SRC|        need((h ^ 0) == h and (0 ^ h) == h and (h ^ h) == 0,
SRC|             "GROUP_IDENTITY_INVERSE")
SRC|    gen = dict(a=3, A=3, b=3, B=3, e=0, f=2, g=2)
SRC|    for c in Q:
SRC|        need(grades[gen[c]] == Q[c], "GENERATOR_GRADE")
SRC|    def evaluate(s):
SRC|        parity(s)
SRC|        result = gen[s[0]]
SRC|        for c in s[1:]:
SRC|            result = mul(result, gen[c])
SRC|        return result
SRC|    relation_images = []
SRC|    for rid, (left, right) in R.items():
SRC|        a, b = evaluate(left), evaluate(right)
SRC|        need(a == b, "IMAGE_R" + str(rid))
SRC|        relation_images.append((rid, a, b))
SRC|    generated = set(gen.values())
SRC|    while True:
SRC|        expanded = generated | {mul(i, j) for i in generated
SRC|                                 for j in generated}
SRC|        if expanded == generated:
SRC|            break
SRC|        generated = expanded
SRC|    need(generated == set(range(4)), "IMAGE_GENERATED_CARRIER")
SRC|    need(evaluate("ef") != evaluate("fe"), "IMAGE_NONCOMMUTING")
SRC|    need(evaluate(U) == evaluate(V) == 1, "IMAGE_UV_EQUAL")
SRC|    print("IMAGE_TABLE", table)
SRC|    print("IMAGE_Q", grades, "INVERSES", tuple(range(4)))
SRC|    print("IMAGE_RELATIONS", relation_images)
SRC|    print("IMAGE_CHECKS", "64 associativity; 16 q; 4 inverse; 4 purity")
SRC|    print("IMAGE_EF_FE", evaluate("ef"), evaluate("fe"))
SRC|    print("IMAGE_U_V", evaluate(U), evaluate(V), "NOT_SOURCE_SEP")
SRC|
SRC|def show_source(s):
SRC|    return "".join({"A": "a'", "B": "b'"}.get(c, c) for c in s)
SRC|
SRC|def show_word(w):
SRC|    return " ".join("(%d,%s)" % (h, show_source(s)) for h, s in w)
SRC|
SRC|def print_chain(chain):
SRC|    primitive = 0
SRC|    for kind, at, n, before, after in chain:
SRC|        if kind == "N":
SRC|            label = "NAME R%d (zero primitive steps)" % n
SRC|        else:
SRC|            primitive += 1
SRC|            label = "STEP %02d %s parameter=%d" % (primitive, kind, n)
SRC|        print(label, "LOCUS", at)
SRC|        print("BEFORE", show_word(before))
SRC|        print("AFTER ", show_word(after))
SRC|    need(primitive == 80, "PRINTED_PRIMITIVE_COUNT")
SRC|
SRC|def main():
SRC|    global LIMIT
SRC|    LIMIT = monotonic() + 55.0
SRC|    ulog, us = branch(U, U_PLAN, U_WORDS)
SRC|    vlog, vs = branch(V, V_PLAN, V_WORDS)
SRC|    common = symbols("XPQ")
SRC|    uc = replay(ulog, ((0, U),), common)
SRC|    vc = replay(vlog, ((0, V),), common)
SRC|    need(uc == Counter({"C": 6, "E": 7, "I+": 1, "N": 3}),
SRC|         "U_COUNTS")
SRC|    need(vc == Counter({"C": 28, "E": 31, "I+": 4, "I-": 3, "N": 10}),
SRC|         "V_COUNTS")
SRC|    chain = ulog + inverted(vlog)
SRC|    counts = replay(chain, ((0, U),), ((0, V),))
SRC|    need(counts == Counter({"C": 37, "E": 35, "I+": 4, "I-": 4, "N": 13}),
SRC|         "FULL_COUNTS")
SRC|    controls(ulog, us, vs, chain)
SRC|    finite_image()
SRC|    print_chain(chain)
SRC|    tick()
SRC|    print("COUNTS_U", dict(uc))
SRC|    print("COUNTS_V", dict(vc))
SRC|    print("COUNTS_FULL", dict(counts))
SRC|    print("RESULT COLL_FINITE_WORD_REPLAY; SEP_UNKNOWN; NO_NEGATIVE_WITNESS")
SRC|
SRC|if __name__ == "__main__":
SRC|    main()

## 8. Exact disposition

**Written result:** the literal 80-primitive chain proves

\[
(0,U)\equiv_q(0,V)
\]

in the actual universal presentation, using all required shifted indices, eight nonempty word-square replacements, and only R1–R4 for the 13 expressly identified source-name changes.

**Execution result:** NOT RUN. No computational PASS or executed FINITE-gate credit is available from this return.

**Source result:** the explicit four-element image supports the noncommuting-idempotent positive control and respects all four source relations. It identifies U and V and supplies no separation evidence.

**Unpaid scientific step:** SEP for the original \(S_0/\theta\). Neither \(U\ne V\) nor \(U=V\) in that source is established here.

**Original all-host negative witness:** NOT PROVED.

This is a same-harness written reconstruction with fresh, unexecuted checker source—not an independent-family, human, kernel, novelty, or automatic-adoption certificate.