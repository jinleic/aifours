# math-p0039: bounded research result

**Outcome: partial. The all-orders conjecture is not solved or refuted. Novelty is unknown.**

## General finite computational result

Assuming the declared imported theorems, one production computation excluded every
candidate in **200000000000 <= n < 10341223092224**, with n=8 (mod 24).
The last unbroken audited block boundary is **N=10341223092224**, exclusive.
The computation covered 422,550,962,176 class members in
50,372 complete blocks: 364,818,361,313 proper-factor
sieve rejections and 57,732,600,863 exact base-two tests. Every block
satisfies sieved+tested=its exact arithmetic-class count. There are no unresolved
survivors.

Together with the imported Thas–Zagier below-200000000000 exclusion, this gives
the **conditional computational bound: no non-Desarguesian flag-transitive
projective plane has order n<N**. Independent arbitrary-precision checks covered
only the explicitly stated subsets below. The complete production interval has
NOT been independently certified. This finite range is a sub-question, not a
solution of the universal question. The planned stop 20000000000000 is not a
reported bound.

A separate exact result excludes only power-of-two orders 2^a for 3<a<59049;
it does not extend the general bound N to 2^59049.

## Question fidelity and imported premises

The target is the finite flag-transitive-plane conjecture, with its special-prime
difference-set reformulation. The book's literal graph assertions are defective:
reflection-generated dihedral Cayley graphs are bipartite, each part has p
vertices, and degree n+1<p leaves opposite-part nonneighbors, making diameter
two impossible. Also an unspecified set of reflections does not give the stated
equivalence with non-Desarguesian planes: classical Singer difference sets yield
diameter-three incidence Cayley graphs too. The staged book-page image was
visually checked. No result here relies on that printed equivalence.

The detailed ledger is [PREMISES.md](evidence/PREMISES.md):

* Kantor (1987), via Thas–Zagier Section 1: the non-Desarguesian alternative has
  even n, prime p=n²+n+1 and a Frobenius/sharply flag-transitive action. This
  reduction relies on the classification of finite simple groups.
* Thas–Zagier Proposition 2.1/Theorem 2.4 identify the remaining case with
  D=mu_(n+1) being an additive planar difference set. Only n=2,8 give classical
  planes in this special construction. Their appendix gives the base-two
  necessary condition and the published computational baseline.
* Feit's VALID necessary conditions: 8|n and d^(n+1)=1 mod p for every positive
  divisor d of n. Feit's purported power-of-two exclusion and Ott's purported
  prime-power-order proof are not used; the staged paper identifies errors.
* Derived here: n³=1 mod p and n is not 1 mod p, so ord_p(n)=3. Taking d=n
  gives 3|(n+1); together with 8|n this gives n=8 mod 24.
* The base-two condition also has a short proof: the unique x with x,x+1 in D
  is fixed by inversion. Thus x=±1, with −1 impossible, so x=1 and 2 is in D.

Only staged local materials were available. The Thas–Zagier source is a
reader-converted text, whose SHA-256 matches SOURCES.json; its original PDF and
later papers were not available for a fresh literature check. Section 1,
Proposition 2.1, Theorem 2.4 and the appendix were rechecked before production.
The below-2×10^11 computation is imported, not independently rerun here.

## Controls, cheap falsification and arithmetic

The FULL published even-n interval [2,5000000000) was rerun without a sieve:
2,499,999,999 values, 299 blocks, 248.323 seconds,
exactly the seven published exceptions. This reproduces the full list, not just
isolated positive checks. Python independently recomputed 3991 recorded full
residues, not the whole 2.5-billion-value control run.

| n | p | exact status |
|---:|---:|---|
| 2 | 7 | D planar, all differences checked (classical control) |
| 8 | 73 | D planar, all differences checked (classical control) |
| 24 | 601 | [1, 256] and [8, 263] have the same nonzero difference 346 |
| 90 | 8191 | [1, 7474] and [4, 7477] have the same nonzero difference 718 |
| 512 | 262657 | [1, 89785] and [4, 89788] have the same nonzero difference 172873 |
| 134217728 | 18014398643699713 | proper factor 2593; cofactor 6947319183841 |
| 297474474 | 88491062979051151 | n mod 24 = 18; d=n has residue 297474474, not 1 |


For each n=24,90,512 collision, the four elements are verified members of D and
the ordered pairs are distinct. Thus passing base two is not sufficient.

The full even-n range [2,20000) was also checked both with and without a
B=1000000 sieve. All 9999 residues and every actual smallest proper sieve
factor were independently recomputed. In particular the controls whose prime
p lies below B (7,73,601,8191,262657) were retained: the sieve never uses q=p
as a rejection. Two further 1024-member arithmetic windows, one at the main
lower boundary and one near n=2^60, matched Python completely.

The producing [scan.c](code/scan.c) uses full 256-bit intermediate products for
128-bit Montgomery reduction. Inputs satisfy n<2^60, hence odd p<2^127.
The proof of the arithmetic bounds is in PREMISES.md. Audit records contain
complete ordinary residues after Montgomery conversion, not pass/fail flags.
The source and binary were frozen before controls and production; their hashes
and the compiler command are in [build.json](evidence/build.json). Replay commands never execute that
binary.

## Production method, benchmark and coverage

Candidates are n=200000000000+24i. An Eratosthenes sieve generates trial primes
q<=1000000. The roots of n²+n+1 mod q are computed exactly; q=3 is handled
separately. Every sieve rejection is by a proper divisor 1<q<p. The fast path
first proves B<p at the block's smallest n, hence for the whole block; the
small-n path checks q<p at every proposed mark. Descending marking retains the
smallest sieve prime as the recorded witness.

All unsieved candidates receive an exact 2^(n+1) mod p test. A residue other
than 1 eliminates a proved necessary condition without requiring a primality
test. A residue of 1 must be resolved by an exact witness; probable primality
never eliminates one.

Three 100-million-member benchmarks gave 2.461 s (B=100000, large blocks),
2.113 s (B=1000000, large blocks), and 2.028 s (B=1000000, small blocks).
Large blocks (8388608 members) were selected to limit evidence volume and audit
memory. The two B=1000000 benchmarks agreed on all aggregate counts.

Production used 3 CPU threads with one CPU reserved for independent Python
work. Its hard compute cap was 9000 seconds, completing only already assigned
blocks after the cap. Actual production wall time: 9000.533
seconds. All block IDs are consecutive from 0; starts, exclusive endpoints,
class counts, branch counts and every survivor list are structurally checked.
See [production-plan.json](evidence/production-plan.json) and [main.blocks.jsonl](logs/main.blocks.jsonl). No install, network, delegation,
credentials, outside-directory reads, or git commits were used.

## Survivor/elimination table

| production base-two survivors after sieving | exact eliminations needed | unresolved |
|---:|---:|---:|
| 0 | 0 | 0 |


The machine-readable table is [survivors.json](evidence/survivors.json). Its independent checker compares
the table with EVERY logged survivor, verifies proper factors or valid divisor
congruence failures, and rejects unresolved cases. It does not accept any
probable-prime elimination.

## Exactly what was independently checked

* **A second complete computation of a smaller contiguous prefix:** the
  separate Python scanner processed ALL 9,986,637,824 class
  members in [200000000000,439679307776), using
  8,622,783,470 proper-factor rejections and
  1,363,854,354 arbitrary-precision powers, with no survivors.
  It uses Tonelli–Shanks roots of −3 and bytearray slices, imports no producing
  C code, and ran for 6000.498 s on one CPU. Every one of
  1,190 fully overlapping C blocks agrees with
  its aggregate counts. That agreement is an aggregate control, not an
  entrywise residue hash of all n. The separate computation repeats its
  entire stated prefix, which is SMALLER than the general production range.
  Its own 47,748 audit records received independent
  full-power/trial-factor checks. Parameters/source hash are in
  independent-plan.json, counts in python-main.blocks.jsonl, checks in
  python-main.audit.json and scans.comparison.json.
* **Production audit records:** 251,526 records, including
  217,011 factor decisions and
  34,515 unsieved decisions. Python recomputes the
  COMPLETE power for each, and uses independent trial division to verify the
  actual smallest sieve factor. Records include the first/last two members of
  every completed block and 197 contiguous
  256-member windows at the first block and every 256th block. Every member in
  each window is hashed as n, decision, factor, full residue, including sieved
  members. Exact window endpoints and hashes are in [main.audit.json](evidence/main.audit.json).
* **Separated exhaustive Python windows:** 100 predetermined windows of
  1048576 members each, 104,857,600 full powers total.
  Window j starts at 200000000000+24·8388608·512·j, for 0<=j<100. Every n,
  decision and full residue contributes to its hash, including composite
  moduli. 99 of these windows lie wholly inside the final main
  interval. All are listed individually in [python-windows.jsonl](logs/python-windows.jsonl); any outside
  the main endpoint do not enlarge the gap-free general bound.
* **A third arithmetic control:** an independent manual binary-exponentiation
  checker rechecked only windows 0 and 99 (2,097,152 members)
  and matched their full hashes. It did not recheck all 100 windows. A separate
  replay with built-in pow reran all 100 windows (104,857,600
  full powers) and matched every hash; its output is
  python-windows.full-replay.json.
* **Exhaustive boundaries:** Python pow checked every one of the first
  1000000 class members [200000000000,200024000000), and every one of the last
  1000000 class members [10341199092224,10341223092224). No base-two hits remained.
* **Controls:** the small full-range comparisons and the 3991 full published-
  control samples described above. Known positive controls were included.

These are implementations using Python arbitrary-precision integers that do
not import or execute the producing C code. Their scope is precisely these
subsets, including the explicitly smaller complete Python prefix. Neither
sampling nor hashes independently certify the entire
production scan. File hashes establish integrity only. The general bound is
reported as one production computation with declared subset checks.

## A separate power-of-two-order result and analytical limitations

For n=2^a, primality of p forces a=3^t: if a has a prime divisor l!=3, then
2^(2a/l)+2^(a/l)+1 is an explicit proper divisor of p. For a=3^t the order of
2 mod a hypothetical prime p is exactly 3^(t+1), which divides n+1. Thus
all base-two AND divisor-multiplier conditions automatically pass. The proof
is in [POWER-TWO-LEMMA.md](evidence/POWER-TWO-LEMMA.md); no invalid Feit power-of-two argument is imported.
In fact for every t this congruence statement holds even when p is composite,
and every prime factor of that p is 1 mod (6·3^t). Consequently any FIXED
finite prime sieve plus these power conditions admits infinitely many integer
survivors at larger orders. This is a limitation of the filter, not a claim
that the associated p is prime or that any counterexample plane exists.

At a=9, n=512 is eliminated by the direct D collision above. All subsequent
exceptional exponents below 59049 have these exact proper factors:

| a | proper factor of 2^(2a)+2^a+1 |
|---:|---:|
| 27 | 2593 |
| 81 | 487 |
| 243 | 80191 |
| 729 | 39367 |
| 2187 | 209953 |
| 6561 | 141560137 |
| 19683 | 472393 |


This is a gap-free factor chain for 3^t, 3<=t<=9. It proves the restricted
exclusion for every exponent 3<a<59049, not only the displayed seven exponents:
the algebraic lemma excludes all non-powers of three. check_family.py verifies
each factor by manual small-modulus exponentiation and verifies the n=512
collision; a separate full-integer factor check also passed. The first unhandled
exceptional exponent is a=59049. Failure to find a factor below 10^11 does not
prove this p prime or resolve that case. See [POWER-TWO-RANGE.md](evidence/POWER-TWO-RANGE.md).

Multiplicative closure also gives gcd(n,3·5·7·17·31)=1 under the valid
divisor-multiplier premise ([CLOSURE-LEMMA.md](evidence/CLOSURE-LEMMA.md)). This corollary leaves substantial
families open and was NOT used by the production sieve. No novelty is claimed
for either elementary lemma or the factor chain.

The Gaussian-period/Fermat-curve reformulations in the staged paper were
considered, but no uniform rationality obstruction or difference collision was
derived. The elementary subgroup argument only excludes some factor patterns;
it leaves powers of two and other factor sets. A finite scan cannot fill this
all-orders gap.

## Replay commands and negative controls

All commands run from this directory using python3; no attack-built executable
is invoked. Fast structural replay (not a full recomputation):

    python3 code/verify_result.py
    python3 code/check.py schema
    python3 code/check_family.py
    python3 code/check_controls.py
    python3 code/compare_scans.py
    python3 code/seal.py check

Recompute ALL stored production arithmetic samples (still only a subset of n):

    python3 code/check.py records logs/main --allow-partial

Recompute the selected manual-control windows, or every separated window:

    python3 code/check_windows.py --indices 0,99 --backend manual
    python3 code/check_windows.py --all --backend pow

Slow complete Python reexecution of the entire general range is available but
was NOT performed; it can require far more time than this visit's budget:

    python3 code/replay.py --start 200000000000 --stop 10341223092224 --step 24

Each of the following deliberate corruptions must return nonzero: a changed
full residue, a q=p self-factor, a broken block count, a changed window hash,
a changed family factor, and a changed reported endpoint:

    python3 code/check.py single evidence/negative-residue.json --bound 1000000
    python3 code/check.py single evidence/negative-self-factor.json --bound 1000000
    python3 code/check.py metadata evidence/negative-coverage
    python3 code/check_windows.py evidence/negative-window.jsonl --indices 0 --backend pow
    python3 code/check_family.py evidence/power-two-family-broken.json
    python3 code/verify_result.py --result evidence/result-broken.json

## Final validation

All positive checks passed. All seven deliberately corrupted cases returned
nonzero with the intended mathematical or coverage failure reason. Exact
commands, return codes and outputs are in
[fast-checks.json](evidence/fast-checks.json). The final claims file passes
claims.schema.json. Every claims.json replay command uses python3 and no
attack-built executable.

## Remaining gap and best next step

No non-Desarguesian plane has been constructed, and no argument excludes every
remaining order. Orders n>=N outside the restricted power-of-two result remain
unhandled. Even within that family, a>=59049 is not excluded by its theorem.
The imported baseline and classification are not independently reproved, and
the complete new general interval has only one production implementation.
The separate Python computation repeated only the smaller prefix stated above.

The best verification next step is an independently engineered COMPLETE exact
replay of the reported interval, followed by checking later literature before
any best-bound or novelty statement. The universal conjecture requires an
additional mathematical obstruction, not interpretation of this finite scan
as a universal proof. No automatic continuation or extra visit is scheduled.

Finalized UTC: 2026-10-15T14:15:23.722684+00:00. Session deadlines are in [session.json](evidence/session.json); production
began at the time in [production-plan.json](evidence/production-plan.json). Evidence file hashes are in
[manifest.json](evidence/manifest.json) and certify file integrity only.
