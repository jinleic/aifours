# A nonorthodox finite-envelope extension via idempotent products

**NEW AUTHOR WRITTEN REDUCTION with exact finite control; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 21:04:11 PDT 2026**. This extends the orthodox finite-envelope reduction to a nonorthodox class. It does not prove that all original sources satisfy the hypothesis or that any finite canonical obligations are universally paid.

## 1. Exact envelope theorem

Let S be a locally finite regular semigroup satisfying

`(P2G)  every product ef of two idempotents of S lies in a subgroup of S`.

Then every finite subset of S is contained in a finite regular subsemigroup. In particular the condition holds when S is E-solid, meaning its idempotent-generated core C(S) is completely regular. P2G is stated directly because the proof needs only idempotent PAIRS; no claim is made that it is strictly weaker than E-solidity.

If, additionally, S is weakly E-unitary and locally r-orthodox, each such regular subsemigroup is again weakly E-unitary and locally r-orthodox. Thus for an original source with an onto pure CS actor and locally finite maximal actor group, the local-to-global q-host criterion reduces to finite **regular original-class** subsemigroups whenever P2G holds. Brown's theorem supplies local finiteness, and the precise compactness/actor assumptions are those of `frontier-20261028-locally-finite-local-global-host-v1.md`, SHA `073d175108116583b1d91906436ce53dd53fdcac5961b97766516574789b5057`.

This strictly relaxes the PROVED assumption of the earlier orthodox envelope note: it does not require E(S) to be globally closed. Whether it exhausts all original sources is NOT claimed.

## 2. Construct the finite regular envelope

Take a finite subset A⊂S and choose one mutual inverse a' of each a∈A. Local finiteness makes `F=⟨A∪A'⟩` finite. We show every product of elements whose inverses already lie in F again has an inverse in F.

Let a,a' and b,b' be mutual inverse pairs in F, and put

`e=a'a`, `f=bb'`, `u=ef`.

Both e,f are idempotents. By P2G, u belongs to a group. Since S is locally finite, the cyclic semigroup of u is finite, so the group inverse v of u is a POSITIVE power of u (when u is its group identity take v=u). Thus v∈F. Define `y=b' v a'`. Direct multiplication, using `ae=a`, `fb=b`, `u v u=u` and `v u v=v`, gives

`(ab)y(ab)=a f v e b=a e f v e f b=a e f b=ab`,

`y(ab)y=b' v e f v a'=b' v a'=y`.

Hence y is a mutual inverse of ab in F. Induct on words in the finite generators and their chosen inverses; each generator has an inverse in that same set, so F is regular. No reversal law for inverses and no global closure of E(S) is used.

For e∈E(F), the local monoid eFe is regular. Its idempotents lie in the regular band E(eSe); their products stay in eFe and remain idempotent, so E(eFe) is a subband of E(eSe) and inherits the regular-band identity. Weak E-unitarity is hereditary for a regular subsemigroup. Thus F has the original class hypotheses whenever S does.

## 3. The actual-q finite-to-global implication

Suppose S also has an onto pure CS actor q and is locally r/weak E, and its actor maximal group is locally finite. Brown's theorem applied to q's idempotent fibres makes S locally finite. Every finite subsemigroup F0⊂S lies inside a finite regular original-class F by §2. If every such F admits a physical host over its own actual q_F, the pure onto actor pullback and subgroup restriction gauges in `frontier-20261028-orthodox-finite-original-reduction-v1.md`, SHA `d208670ba3ceddf6f680c51198209b9e56b23421c4067e2cc166b1e69c11924f`, supply the required host for F0 over q(F0). The prior coinduction/first-order compactness theorem then gives a global host over exactly q. The converse follows by host restriction and actual-actor pushforward.

Accordingly this is an iff REDUCTION to finite original subsemigroups, conditional on the named actor/compactness inputs; it is not a proof that any of those finite obligations universally hold. It covers orthodox sources because there ef is itself idempotent, and can also cover nonorthodox sources. The 45-source from the earlier nonorthodox boundary has idempotent-generated core equal to the whole non-completely-regular source, so it is NOT E-solid; `frontier-20261028-non-E-solid-45-checker-v1.py`, SHA `63634a1727f2b9131de37d0d90382081d8aab271f8938e01aebe4b169802fb1a`, directly checked the core and witness at21:05:05. This note does not extend the regular-envelope proof to that source merely by renaming the hypothesis.

## 4. Exact nonorthodox, non-completely-regular control

`frontier-20261028-E-solid-finite-envelope-checker-v1.py`, SHA `81d8dc2187811accc4cdf658a1dff2d8a0d3580b509d1dbb3c71ae3698db5447`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 21:04:11 PDT 2026**, exit0. Its source is the direct product of a non-completely-regular finite inverse semilattice-by-C2 semigroup and an8-element nonorthodox completely simple Rees semigroup. It has64 elements, 16 idempotents, actual pure CS actor16, and idempotent-generated core32. The code exhausts source regularity, weak E, local-r, actual syntactic contexts, nonclosure of E, non-complete-regularity, and a commuting group inverse for EVERY core element. The selected inverse-generator envelope has56 elements and is regular, locally-r and nonorthodox.

```text
ambient=64 E=16 core=32 actual_actor=16
PASS regular/WEU/local-r, nonorthodox, non-completely-regular, core completely regular
finite inverse-generator envelope=56 regular, locally-r and nonorthodox
PASS actor purity and full 65^2 contexts/source
```

This finite sample does not prove a strict hierarchy between P2G and E-solid or the general theorem; those are separately scoped above. No independent witness/scientific review, cross-vendor/human/formal proof, novelty or full-original-source closure is claimed.
