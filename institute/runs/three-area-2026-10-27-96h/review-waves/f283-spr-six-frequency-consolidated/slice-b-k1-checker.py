#!/usr/bin/env python3
"""Slice B independent K1 checker for wave f283-spr-six-frequency-consolidated.

Definition-first replay of S1's finite phase classification (S1 lines 22, 24-26,
33-38) using ONLY the written definitions; the author kernel
frontier-20261029-strict-certificate-five-node-phase-independent-kernel-v1.py
was never read/imported/executed (metadata only, per manifest-v1.json).

Predicates derived from the manuscript text:
  (alpha) S1|34 (Lemma 4): a parity sign word that does NOT contain the oriented
         subsequence (-,+,-,+) fits the four blocks +*-*+*-* and is incompatible
         with Lemma 3's four moment signs. K1 requires this for BOTH parity sign
         words (S1|38: "each parity sign word fails the four-block pattern").
         Internal control: over every sign word of length <= 7,
         contains(-,+,-,+)  <=>  NOT fits(+*-*+*-*)  (validated below).
  (beta) S1|22: for t_i < t_j: (i) q_j >= q_i - 1 always; (ii) if BOTH parity
         signs differ between the samples, q_j >= q_i + 2.
  Class sign pairs from S1|22: classes 0..6 have (E,O) sign pairs
         (++),(-+),(--),(+-),(++),(-+),(--).

Standard library only; exact integer comparisons; single core; full 7^m universes.
S2 numbers are embedded below only as AUTHOR CLAIMS, compared after computation.
"""
import sys, os, json, time, hashlib, platform, datetime
from itertools import product

T0 = time.time()
WAVE = os.path.dirname(os.path.abspath(__file__))
SELFPATH = os.path.abspath(__file__)

ESIGN = {0: 1, 1: -1, 2: -1, 3: 1, 4: 1, 5: -1, 6: -1}   # S1|22
OSIGN = {0: 1, 1: 1, 2: -1, 3: -1, 4: 1, 5: 1, 6: -1}    # S1|22
ORIENT = (-1, 1, -1, 1)   # S1|33-34
FLIP = (1, -1, 1, -1)

def contains(seq, pat):
    it = iter(seq)
    return all(any(x == n for x in it) for n in pat)

def fits_blocks(seq):
    labels = (1, -1, 1, -1); bi = 0
    for x in seq:
        if bi < 4 and x == labels[bi]:
            continue
        bi += 1
        while bi < 4 and labels[bi] != x:
            bi += 1
        if bi >= 4:
            return False
    return True

def eword(w): return tuple(ESIGN[q] for q in w)
def oword(w): return tuple(OSIGN[q] for q in w)

def alpha(w):
    return contains(eword(w), ORIENT) and contains(oword(w), ORIENT)

def alpha_E_only(w):  # mutation M5
    return contains(eword(w), ORIENT)

def alpha_flip(w):    # mutation M1
    return contains(eword(w), FLIP) and contains(oword(w), FLIP)

def both_differ(qi, qj):
    return ESIGN[qi] != ESIGN[qj] and OSIGN[qi] != OSIGN[qj]

def beta(w, ii_plus=2, use_i=True, use_ii=True, i_slack=1):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n):
            if use_i and w[j] < w[i] - i_slack:
                return False
            if use_ii and both_differ(w[i], w[j]) and w[j] < w[i] + ii_plus:
                return False
    return True

# ---------- internal control C0: subsequence/block equivalence (Lemma 4 reading)
c0_ok = True
for L in range(0, 8):
    for w in product((1, -1), repeat=L):
        if contains(w, ORIENT) == fits_blocks(w):
            c0_ok = False

# ---------- full universes m = 3, 4, 5
universe = {m: list(product(range(7), repeat=m)) for m in (3, 4, 5)}
alpha_pass = {m: [w for w in universe[m] if alpha(w)] for m in (3, 4, 5)}
retained = {m: [w for w in alpha_pass[m] if beta(w)] for m in (3, 4, 5)}

# expected m=4 alpha-passers from the WRITTEN m>=5 argument (S1|36): both parity
# words exactly (-,+,-,+) => sign pairs (--),(++),(--),(++) => classes as below.
expected16 = {(q1, q2, q3, q4) for q1 in (2, 6) for q2 in (0, 4)
              for q3 in (2, 6) for q4 in (0, 4)}
c_m4_16 = set(alpha_pass[4]) == expected16

# ---------- mutations (each labeled with intended reason; discriminating flag)
BASE = set(retained[5])
muts = {}
muts["M1_alpha_orientation_flip"] = dict(
    intended="oriented subsequence flipped to (+,-,+,-); wrong Lemma-4 orientation",
    retained=[w for w in universe[5] if alpha_flip(w) and beta(w)],
    alpha_pass=len([w for w in universe[5] if alpha_flip(w)]))
muts["M2_drop_beta_ii"] = dict(
    intended="omit ordered-phase constraint (ii) entirely",
    retained=[w for w in universe[5] if alpha(w) and beta(w, use_ii=False)],
    alpha_pass=len(alpha_pass[5]))
muts["M3_drop_beta_i"] = dict(
    intended="omit ordered-phase constraint (i) entirely",
    retained=[w for w in universe[5] if alpha(w) and beta(w, use_i=False)],
    alpha_pass=len(alpha_pass[5]))
muts["M4_ii_advance_plus1"] = dict(
    intended="weaken (ii) advance bound from +2 to +1",
    retained=[w for w in universe[5] if alpha(w) and beta(w, ii_plus=1)],
    alpha_pass=len(alpha_pass[5]))
muts["M5_alpha_E_word_only"] = dict(
    intended="apply Lemma 4 to the even word only (odd word unchecked)",
    retained=[w for w in universe[5] if alpha_E_only(w) and beta(w)],
    alpha_pass=len([w for w in universe[5] if alpha_E_only(w)]))
muts["M6_i_slack_2"] = dict(
    intended="weaken (i) slack from -1 to -2",
    retained=[w for w in universe[5] if alpha(w) and beta(w, i_slack=2)],
    alpha_pass=len(alpha_pass[5]))
for k, v in muts.items():
    s = set(v["retained"])
    v["count"] = len(s)
    v["differs_from_baseline"] = (s != BASE)
    v["superset_of_baseline"] = (BASE <= s)
    v["discriminating"] = (s != BASE)
    v["retained_sorted"] = sorted(s)

# ---------- author claims (S2 receipt, packet S2|6-13); compared AFTER computation
S2_CLAIM = {"ordered_m4_sequences": 0, "ordered_m5_sequences": 3,
            "phase_order_removed_m4_sequences": 16,
            "phase_order_removed_m5_sequences": 676,
            "cases": [[2, 1, 3, 2, 4], [2, 1, 3, 5, 4], [2, 4, 3, 5, 4]]}
comparison = {
    "alpha_pass_m4_equals_S2_16": len(alpha_pass[4]) == S2_CLAIM["phase_order_removed_m4_sequences"],
    "alpha_pass_m5_equals_S2_676": len(alpha_pass[5]) == S2_CLAIM["phase_order_removed_m5_sequences"],
    "retained_m4_empty_equals_S2_0": len(retained[4]) == S2_CLAIM["ordered_m4_sequences"],
    "retained_m5_equals_S2_cases": set(retained[5]) == {tuple(c) for c in S2_CLAIM["cases"]},
    "retained_m5_count_equals_S2_3": len(retained[5]) == S2_CLAIM["ordered_m5_sequences"],
}

receipt = {
    "kind": "slice-B independent K1 finite classification receipt",
    "wave": "f283-spr-six-frequency-consolidated",
    "source": os.path.basename(SELFPATH),
    "checker_sha256_at_run": hashlib.sha256(open(SELFPATH, "rb").read()).hexdigest(),
    "python": platform.python_version(),
    "platform": platform.platform(),
    "argv": sys.argv,
    "clock_start_utc": datetime.datetime.fromtimestamp(T0, datetime.timezone.utc).isoformat(),
    "definitions_used": {
        "class_sign_pairs_S1_L22": {"E": {str(k): v for k, v in ESIGN.items()},
                                     "O": {str(k): v for k, v in OSIGN.items()}},
        "alpha": "both parity sign words contain oriented subsequence (-,+,-,+), equivalently fail +*-*+*-* (S1|34,38)",
        "beta": "for all i<j: q_j>=q_i-1; if both parity signs differ then q_j>=q_i+2 (S1|22)",
    },
    "internal_control_C0_subseq_block_equivalence_all_sign_words_len0_7": c0_ok,
    "universes": {str(m): len(universe[m]) for m in (3, 4, 5)},
    "alpha_pass_counts": {str(m): len(alpha_pass[m]) for m in (3, 4, 5)},
    "retained_counts": {str(m): len(retained[m]) for m in (3, 4, 5)},
    "m4_alpha_set_equals_written_expected16": c_m4_16,
    "m4_alpha_pass_sorted": sorted(alpha_pass[4]),
    "m5_retained_sorted": sorted(retained[5]),
    "m5_alpha_pass_sorted": sorted(alpha_pass[5]),
    "S2_author_claim_comparison": comparison,
    "mutations": muts,
    "author_kernel_read_or_executed": False,
    "slice_A_or_other_review_read": False,
    "clock_end_utc": datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).isoformat(),
    "wall_seconds": round(time.time() - T0, 3),
}
out = os.path.join(WAVE, "slice-b-k1-receipt.json")
with open(out, "w") as f:
    json.dump(receipt, f, indent=1)
ok = (c0_ok and c_m4_16 and all(comparison.values()))
print("K1 core: alpha m3/m4/m5 = %d/%d/%d ; retained m3/m4/m5 = %d/%d/%d ; retained m5 = %s"
      % (len(alpha_pass[3]), len(alpha_pass[4]), len(alpha_pass[5]),
         len(retained[3]), len(retained[4]), len(retained[5]), sorted(retained[5])))
print("C0 equivalence:", c0_ok, "| m4 alpha==expected16:", c_m4_16, "| S2 comparison:", comparison)
for k, v in muts.items():
    print("MUT %s: count=%d differs=%s discriminating=%s" % (k, v["count"], v["differs_from_baseline"], v["discriminating"]))
print("receipt:", out)
sys.exit(0 if ok else 1)
