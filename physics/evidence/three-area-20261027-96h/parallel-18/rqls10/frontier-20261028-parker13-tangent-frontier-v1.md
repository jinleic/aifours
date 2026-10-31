# Parker 13-ray array — first exact tangent-rank bounds

**Interim scientific record, not a proof of an additional deformation.** Native `/bin/date` before writing: **Wed Oct 28 17:14:33 PDT 2026**. Array certificate `frontier-20261028-parker-13ray-result-v1.json`, SHA256 **0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5**, was independently checked at the original vector definition by `frontier-20261028-partial-qls-exact-check-v1.py`, SHA256 **40f201ed11f598afada8091ac59b7fe5865b7d75acd5bf5764b4024550a4ed47**: 100 unit vectors, all30 required orthonormal bases, valid resolution, exactly13 distinct rays,387 parallel pairs. It is NOT a maximal-cardinality witness.

The actual real array has integer numerator vectors over denominator3. Linearizing all100 normalization equations and all1350 complex within-block off-diagonal equations yields independent real and imaginary sectors with1000 real variables each. Matrix generator `frontier-20261028-tangent-matrix-v1.py`, SHA256 **3ac0f54ae7df9ff157f75a67dc960e2b194ff20864b070803426bdae3b52db39**, produces exact sparse integer matrices:

- real:1450×1000,3304 nonzeros, `frontier-20261028-parker13-tangent-real-v2.txt`, SHA256 **3ed6d188c5fd5ea8d6416df79d7cc86e88f19da0b3198ed5a430ff15946598a7**;
- imaginary:1350×1000,3186 nonzeros, `frontier-20261028-parker13-tangent-imag-v2.txt`, SHA256 **543b7bbd3712745cec53720ca01024dcaa619f46968262b2bb6ee722b2012459**.

Independent modular-rank implementation `frontier-20261028-modrank-v1.cpp`, SHA256 **fa00474116b15173eba0228f37c367f3dc4fc97e7544c372ff24f8416283**, compiled with `clang++ -O3 -std=c++17`. Actual bounded output over prime65521:

```text
real rows 1450 columns 1000 nonzeros 3304
imag rows 1350 columns 1000 nonzeros 3186
file frontier-20261028-parker13-tangent-real-v2.txt rows 1450 columns 1000 prime 65521 rank 952 nullity 48
file frontier-20261028-parker13-tangent-imag-v2.txt rows 1350 columns 1000 prime 65521 rank 852 nullity 148
```

The modulus was separately checked prime by exact trial division through its integer square root. Since the integer matrix has a nonzero minor modulo this prime, rational rank is at least the modular rank. Thus characteristic-zero tangent nullity is at most48 real plus148 imaginary =196; modular nullity alone DOES NOT prove that these upper bounds are attained over the rationals or that any extra directions exist/integrate.

At least192 real gauge directions exist: `U(10)` plus100 per-cell phases has dimension200; its stabilizer has dimension8 because the seven standard rays outside the embedded3-space have independent phases, whereas the original and Householder-rotated three bases inside that3-space force one common phase there. More specifically the visible real orthogonal directions have dimension45 and the imaginary common-unitary/phase directions have dimension147. Hence the ORIGINAL tangent dimension lies in **[192,196]**, with at most3 extra real and1 extra imaginary directions. This is an exact upper/lower bound conditional on the supplied independent finite-rank checker; it is not a claim that the four candidate directions exist or integrate to new arrays. Independent replay/code review remains needed.

A first generator version accidentally wrote column count100 instead of1000; the rank checker correctly rejected it with `invalid sparse entry` and produced NO rank. The erroneous v1 matrix bytes were retained; the generator was corrected and wrote NEW v2 matrix filenames. The rank values above are exclusively the corrected v2 output; no hidden successful pre-correction run is claimed.

Current next task is the assigned disjoint f8 review. The original 100-ray/10-ray-cardinality gap remains open; no new theorem of global existence or obstruction follows.
