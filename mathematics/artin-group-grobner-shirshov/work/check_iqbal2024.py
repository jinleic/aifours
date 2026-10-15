"""Independent check of Theorem 2.3 of Iqbal-Munir-Ayub-Nizami, 'Complete
presentation and Hilbert series of the mixed braid monoid MB_{1,3}',
Rev. Un. Mat. Argentina 67(2) (2024) 503-516 (sources/iqbal-et-al-2024-type-b3-monoid.*).

MB_{1,3} = <z1,z2,z3 | z3z1=z1z3, z3z2z3=z2z3z2, z2z1z2z1=z1z2z1z2> is the Artin
monoid of type B3 (4 between z1,z2).  Order z1<z2<z3, length-lex.  In our
coxeter.py labelling (Bourbaki s1-s2=4=s3): z1=s3, z2=s2, z3=s1, i.e. order
[2,1,0]; letters a=z1, b=z2, c=z3.

Interpretation of the families (stated in the paper with n,n1,... in N): we test
exponents >= 1, and for R9-R11 the bracket '(z2^n z1^n1 z2^n2 ...)' as an
alternating product of positive powers whose tail after the first two powers
is any (possibly empty) word over {z1,z2} beginning with z2.  We check
 (1) validity of every instance up to length L (Garside normal form), and
 (2) coverage: every minimal non-lexmin word of the monoid (the leading words
     of the reduced GS basis, computed independently) of length <= L is a
     leading word of the paper's list -- necessary for a GS basis (Lemma 1).
Usage: python3 work/check_iqbal2024.py [L] [--corrected]
  --corrected: R3, R6, R9 with z2^(n+1) instead of z2^n on the left (as printed
  they are length-inconsistent: |LHS| = |RHS| - 1 for every n).
"""
import itertools
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from coxeter import build  # noqa: E402
from gs_oracle import enumerate_basis  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 12
CORR = "--corrected" in sys.argv
K = 1 if CORR else 0  # extra z2 on the left of R3, R6, R9
G = build("B", 3, 0, [2, 1, 0])
a, b, c = "a", "b", "c"


def tails(maxlen):
    """words over {a,b} that are empty or begin with b, length <= maxlen"""
    out = [""]
    for n in range(1, maxlen + 1):
        for w in itertools.product("ab", repeat=n):
            if w[0] == "b":
                out.append("".join(w))
    return out


def fams(L):
    R = []
    E = range(1, L + 1)
    R.append(("R0", "ca", "ac"))
    R.append(("Rbr1", "cbc", "bcb"))
    R.append(("Rbr2", "baba", "abab"))
    for n in range(0, L):
        R.append(("R1", "b" + "a" * (n + 1) + "bab", "ababb" + "a" * n))
    for n in E:
        R.append(("R2", "cb" + "a" * n + "c", "bcb" + "a" * n))
        R.append(("R3", "c" + "b" * (n + K) + "cb", "bcbb" + "c" * n))
        R.append(("R5", "cbab" + "b" * (n - 1) + "cb", "bcbab" + "c" * n))
        for n1 in E:
            R.append(("R4", "cb" + "a" * n + "b" * n1 + "cb", "bcb" + "a" * n + "b" + "c" * n1))
            R.append(("R6", "c" + "b" * (n + K) + "a" * n1 + "cbab", "bcbba" + "c" * n + "ba" + "a" * (n1 - 1)))
            R.append(("R8", "cba" + "b" * n + "a" * n1 + "cbab", "bacbab" + "c" * n + "b" + "a" * n1))
            for n2 in E:
                R.append(("R7", "cb" + "a" * n + "b" * n1 + "a" * n2 + "cbab",
                          "bcb" + "a" * n + "ba" + "c" * n1 + "b" + "a" * n2))
    for n in E:
        for n1 in E:
            for t in tails(L):
                if 1 + n + K + n1 + len(t) + 5 > L:
                    continue
                R.append(("R9", "c" + "b" * (n + K) + "a" * n1 + t + "cbabc",
                          "bcbba" + "c" * n + "b" + "a" * n1 + "c" + t))
            for t in tails(L):
                if 3 + n + n1 + len(t) + 5 > L:
                    continue
                R.append(("R11", "cba" + "b" * n + "a" * n1 + t + "cbabc",
                          "bacbab" + "c" * n + "b" + "a" * n1 + "c" + t))
    # R10: c b (a^n b^n1 a^n2 b^n3 ...) c b a b c = b c b a^n b a c^n1 b a^n2 c (b^n3 ...)
    for n in E:
        for n1 in E:
            for n2 in E:
                for t in tails(L):
                    if 2 + n + n1 + n2 + len(t) + 5 > L:
                        continue
                    R.append(("R10", "cb" + "a" * n + "b" * n1 + "a" * n2 + t + "cbabc",
                              "bcb" + "a" * n + "ba" + "c" * n1 + "b" + "a" * n2 + "c" + t))
    return [(nm, l, r) for nm, l, r in R if len(l) <= L]


def lexmin_word(w):
    return G.lexmin(G.normalize([G.W.gen[ord(x) - 97] for x in w]))


rules = fams(L)
bad_valid = [(nm, l, r) for nm, l, r in rules if lexmin_word(l) != lexmin_word(r)]
from collections import Counter  # noqa: E402
lead = {}
for nm, l, r in rules:
    lead.setdefault(l, []).append(nm)
oracle, _ = enumerate_basis(G, L, monoid=True)
minred = [u for u, _ in oracle]
uncovered = [u for u in minred if u not in lead]
print(json.dumps({"L": L, "corrected_R3_R6_R9": CORR, "paper_instances": len(rules),
                  "instances_by_family": Counter(nm for nm, _, _ in rules),
                  "invalid_instances": len(bad_valid),
                  "invalid_by_family": Counter(nm for nm, _, _ in bad_valid),
                  "invalid_examples": bad_valid[:10], "oracle_minred": len(minred),
                  "uncovered_minred": len(uncovered), "uncovered_examples": uncovered[:15]}, indent=1))
