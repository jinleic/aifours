# Nonzero-support-XOR NL242 search in rich symmetric classes

**Scope:** a new intermediate construction target, separate from the completed252 fixed-half exclusions in the parent evidence directory. Seek any nine-variable Boolean function with Walsh peak at most28 and nonzero support XOR `s`, then try to obtain an actual Walsh zero. No balanced NL242 witness or symmetry-class nonexistence claim is supplied merely by a non-find or proof cap. The book problem remains open.

## Mod-eight type and literature

For even weight `w` and support XOR `s`,

`W_f(a)=-2w+4(a.s) mod8`.

If `s=0,w=2 mod4`, every Walsh coefficient is four modulo eight and no coefficient can vanish. If `s!=0`, exactly256 coefficients are zero modulo eight, but they need not be zero as integers. Nonzero `s` is exactly the degree-eight case among even-weight functions. This type is preserved under extended-affine equivalence, so affine transforms of the known degree-seven examples cannot enter it.

The residue observation is **prior art**, not a new mechanism. Lou–Xu–Wang, [arXiv:2610.17897v1](https://arxiv.org/html/2610.17897v1#Thmproposition1), Proposition1's proof explicitly uses the support sum to derive the stronger normalized `W_g(a,c)=4c+8Q(a) mod16` in its eight-variable balanced setting. Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/abs/2610.17871), Lemma2 and Proposition1, contain the general integer expansion/affine low bit. Neither preprint's claimed covering-radius result is imported as a premise. Kavut–Yücel, [arXiv:0808.0684v1](https://arxiv.org/abs/0808.0684), Sections2–4, supplies the symmetry classes, orbit matrices and five published tables.

`classification.md` gives a self-contained derivation and exact encoding correspondence. `sources/literature.json` records read scope; `sources/lxw-proposition1-excerpt.txt` preserves the primary-source excerpt. The checker evaluates all five actual tables by direct character sums and FWHT and checks their common `s=0,w=2 mod4,W=4 mod8` type.

## Bounded heuristic experiments

`code/orbit_search.cpp` is a seeded KY-style sampled steepest-neighbour/tabu search over independent orbit bits, with random/published-seed perturbed restarts. It is not represented as the unpublished original KY algorithm. It minimizes full-spectrum peak-excess energy, using exact orbit character matrices. Moves preserve **even weight, not balance**; the targeted runs enforce nonzero `s` throughout. This is not the old fixed-weight balanced-swap search.

The3-rotation action has176 orbits; adding nine-coordinate reversal gives104. The unrestricted run has512 singleton orbits. The independent checker reconstructs every orbit and all512 character rows, then checks each retained best table directly and by FWHT.

| Run | Seed | Wall cap | Producer-reported best peak / NL | Outcome |
|---|---:|---:|---|---|
| 3-DSBF104 | 20261015040301 | 180s | 32 /240 | NON_FIND |
| 3-RSBF176 | 20261015040302 | 180s | 32 /240 | NON_FIND |
| Unrestricted512 | 20261015040303 | 180s | 36 /238 | NON_FIND |

The unrestricted heuristic did worse than an explicit planted peak32 control; it is not evidence of a better bound. The three runs made, respectively, 1,164,584,308;709,924,103;244,518,838 sampled proposals. A perturbed published-seed recovery control found a genuine peak28 function in0.071s with `s=0`. It shows the implementation can recover the known type, not that the targeted type is absent.

No targeted peak28 table was reported by these bounded runs, so no candidate triggered the requested local-balancing stage. Any later positive table must explicitly expose a zero or be locally balanced, and then pass weight256 plus all512 direct/FWHT bounds with its character shift recorded.

## Exact feasibility attempts

### Full FWHT circuit

`code/exact_cnf.py` models all104 independent3-DSBF orbit bits, **both weight parities**, peak<=28, and `s!=0`. It contains213706 variables and854618 clauses. Harmless output complementation normalizes `f(0)=0`. The complete signed11-bit FWHT is wired on all512 inputs; every intermediate value lies within[-512,512], so no wraparound affects the Walsh inequalities. Range checks at104 frequency representatives cover all512 coefficients by the audited symmetry identity.

CaDiCaL3.0.1 ran with a300s time cap and a256MiB compressed-proof cap. It stopped after129.766s at the proof cap, returning **UNKNOWN**, not UNSAT. The268763136-byte partial LRAT output is retained in the original evidence root with its SHA-256 in `results/exact-run.json`. It is not an empty-clause certificate and is excluded from the compact handoff. It must not support a negative claim.

The universal circuit audit imports no producer code and checks:

- every gate against all8 assignments to its input/output variables;
- every full-adder bit identity and all9 FWHT wiring layers;
- every comparator against all2048 input words;
- every support-XOR expression as an exact binary linear form;
- every target clause, with no extra hidden restrictions.

Positive/discriminating controls use actual full truth tables: a published peak28 model fails **only** `s!=0`; flipping both fixed inputs0 and511, followed by output complementation, supplies an explicit `s=511`, peak32 table that satisfies every clause of the relaxed bound32 circuit. The latter is not a target witness.

### Native weighted-PB formulation

`code/native_pb.py` exercises a materially smaller formulation:104 primary Booleans and208 weighted constraints. For a character row `C_j`, set `L=sum|C_j|`, and let `b_j=f_j` for positive coefficients and `b_j=1-f_j` for negative coefficients. Then the exact symbolic identity

`W=L-2*sum_j |C_j| b_j`

turns the peak constraint into two weighted thresholds. The same nonzero-XOR condition and harmless complement normalization apply. This run has a120s solver cap; its actual outcome is in `results/native-pb-run.json` and `result.json`. A solver-only UNSAT result from this formulation would still be **uncertified**, not a class exclusion.

## Final replay, pins and compact delivery

The final machine-readable receipt is `result.json`; `results/check.json` contains the independent direct/universal audit. Verification is:

```sh
python3 code/check.py
```

Discriminating negative controls, each required to exit1 for its intended assertion:

```sh
python3 code/check.py --corrupt-spectrum
python3 code/check.py --corrupt-encoding
```

`code/final_verify.py` runs that one final evidence pass and records actual commands, return codes, elapsed times and hashes. No old snapshot, record, generated index or shared navigation is changed. `inputs/orbits.json.gz` contains all indexed seed tables, explicit orbits, character matrices and hashes of the C++ matrix inputs. All bit tables use `bits[x]=f(x)`, `x_i=(x>>i)&1`; published hex is decoded left-to-right, MSB-first within each nibble.

For research regeneration, the exact commands and original output metadata are retained in the receipt. The bounded heuristic is compiled with `c++ -O3 -std=c++17 code/orbit_search.cpp -o code/orbit_search`; no third-party dependency is needed for independent replay. Z3 is needed only for the optional native-PB experiment; CaDiCaL only for the optional exact solver run.

`handoff/` stages only load-bearing compressed inputs/circuits, sources, compact results, proof and literature context. It excludes the incomplete268MB trace, raw CNF caches and executable binary. All originals remain preserved here.

## FRONTIER

**PROOF-OBLIGATION / NONZERO-TYPE-CONSTRUCTION.** The bounded searches provide no new impossibility theorem. Do not repeat the same seeds/objective or relabel the proof-capped exact run. A useful continuation requires a genuinely stronger representation—such as structurally decomposing the104-bit weighted-PB problem by the nonzero support type and known quadratic Walsh residues, with proof output planned from the start—or an independently new degree-eight construction. Any discovered nonzero-type NL242 function still needs a Walsh zero before it becomes a balanced242 solution. The completed252 fixed-half exclusions remain unchanged.
