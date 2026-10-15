# Mixed-parity bilinear all-N soliton construction

This is a precise subproblem of Lou Senyue and Li Jinhua's higher-dimensional integrability conjecture, *10000 Selected Problems in Sciences: Physics* (2009), book pp. **350–351**. For `P=D_t+c1 D_x+c2 D_x^2+c3 D_x^3`, `c2 != 0`, the target is a finite exponential tau formula proving `P F.G=0`, `D_y P F.G=0` for **every N and every generic F/G seed pattern**, including the quadratic branch `c3=0`. This is a second scoped parity branch of the same chapter as the sibling odd-cubic project, not a different book problem. It does not settle the full polynomial/operator conjecture or equate the Hirota property with all meanings of integrability.

## Verdict — 2026-10-14 PT

**SOLVED for the precise all-N construction statement by a complete written algebraic proof.** Independent hostile Codex review returned **CORRECT**, with no remaining mathematical gap; one minor notation clarification was applied. FRONTIER: **DELIVERY-READY** for correctness and **NOVELTY-UNCLEAR** for priority. Evidence label: **Certification**, not Discovery. No claim of a new integrable model, scientific priority, or Lean/kernel certification is made.

The operator with `c3 != 0` is gauge-equivalent to the known odd-cubic system, but simply completing the cube would change the normalized background and would not prove the requested seed family. The construction explicitly handles that background, projects a unique charge coefficient of the bilinear identities, normalizes all F/G seeds, and cancels the apparent singularity at `c3=0` for every subset cardinality.

### Precise result

For arbitrary finite N, independent active amplitudes, and generic independent wave numbers `(k_i,l_i)`:

- F-only seeds have `(F_i,G_i)=(A_i,0)`, `w_i=-p(k_i)`.
- G-only seeds have `(F_i,G_i)=(0,A_i)`, `w_i=p(-k_i)`.
- `F_empty=G_empty=1`; no functional relation between k and l is imposed.
- A closed Pfaffian-subset formula rational in `lambda=3*c3/(2*c2)` solves both equations for all type patterns.
- The formula is directly defined at `lambda=0`, and its all-N proof extends to that point by a removable rational limit.
- Specializing `l_i=k_i` and then restricting `y=0` gives the `D_x P` reduction.

All parameter denominators and the generic-recursion uniqueness conditions are explicit in RESULTS.md. Singular limits not covered by these formulas, global regularity of derived physical fields, higher-degree P, and other extension operators remain outside scope.

## Reproduction

From this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py
```

This verifies **local scientific controls**, not a formal proof kernel: symbolic pair and gauge identities; the arbitrary-cardinality cancellation formula; 12 independent ordinary-polynomial differentiation cases; 444 exact cases through N=7, with every type pattern through N=5; and two negative controls. Every finite case agrees coefficient-by-coefficient with the sibling's read-only shared recursion and has zero residuals. The **all-N proof is §§3–7 of RESULTS.md**, not extrapolation from these checks.

The shared verifier `../phys-bilinear-higher-dim-integrability/code/hirota_ns.py` is imported read-only, never copied or changed; its hash is recorded in the verification output. The same shared Python environment is used without installation or modification.

## Frozen contract and file map

The target, coefficient class, seed types, genericity, inclusion of `c3=0`, and requirement for an actual all-N proof were fixed before deriving the candidate. The starting project baseline was a complete three-soliton calculation and finite N=4,5 controls, **not** a certified global novelty claim. No random optimizer or larger search was substituted for the proof obligation.

- [STATUS.md](STATUS.md): book bridge, primary Li–Lou/Hietarinta/Peng comparison, literature-access limitations and novelty boundary.
- [RESULTS.md](RESULTS.md): explicit formula, complete Pfaffian/gauge/charge/limit proof, observed controls and independent-review dispositions.
- `source/problem.zh.txt`: unedited book excerpt; `source/manifest.json`: pinned accessible primary artifacts.
- `code/tau_formula.py`: uniform mixed-quadratic/cubic coefficients.
- `code/verify.py`: shared-recursion comparison and independent direct differentiation controls.
- `results/verification.json`: fixed parameters, all 444 cases, symbolic checks and shared-verifier hash.
- `review/`: hostile independent review prompt, report and invocation record.

The most valuable remaining action is a primary-source comparison with the full Peng et al. (2008) Wronskian family. Correctness of this self-contained proof does not establish its novelty. The full book conjecture remains open outside this scoped class.
