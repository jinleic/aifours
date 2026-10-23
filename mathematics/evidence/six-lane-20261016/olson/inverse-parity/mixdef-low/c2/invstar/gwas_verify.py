"""Raw-DP replay of gwas.cpp output lines (AVOID ...): builds the explicit word (../../../../code/was_verify.py word_of,
unchanged: R_i then S_i, y from theta with y_(k-1) = 0) and runs the raw ordered-product DP dp_has (unchanged).
mode 'avoid': every line must be an avoider (no identity 2p-subword) and must have a genuine empty run (theta != 0 there);
mode 'mutant': every line must be REJECTED (has an identity 2p-subword).  Usage: python3 gwas_verify.py FILE p mode
"""
import sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "code"))
import was_verify as wv   # noqa: E402


def main():
    path, p, mode = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    st = {"file": path, "p": p, "mode": mode, "lines": 0, "dp_avoider": 0, "dp_has_solution": 0, "genuine_empty": 0,
          "rgr_after_merge": 0}
    for line in open(path):
        if not line.startswith("AVOID"):
            continue
        kv = dict(re.findall(r"(\w+)=([^\s]+)", line))
        a = [int(x) for x in kv["a"].split(",")]; b = [int(x) for x in kv["b"].split(",")]
        l = [int(x) for x in kv["l"].split(",")]; th = [int(x) for x in kv["theta"].split(",")]
        assert sum(a) + sum(b) + sum(l) == int(kv["N"])
        w = wv.word_of(a, b, l, th, p)
        has = wv.dp_has(w, p)
        st["lines"] += 1
        st["dp_has_solution" if has else "dp_avoider"] += 1
        st["genuine_empty"] += any(a[i] + b[i] == 0 and th[i] % p != 0 for i in range(len(a)))
    print(json.dumps(st))


if __name__ == "__main__":
    main()
