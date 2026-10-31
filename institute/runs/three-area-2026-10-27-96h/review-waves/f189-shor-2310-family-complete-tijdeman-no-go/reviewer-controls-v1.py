#!/usr/bin/env python3
"""Finite, definition-based diagnostics; never imports or executes author code."""
import collections
import hashlib
import itertools
import json
import math
import sys


class ControlFailure(Exception):
    def __init__(self, code, detail=""):
        super().__init__(code + (": " + str(detail) if detail else ""))
        self.code = code
        self.detail = detail


def need(condition, code, detail=""):
    if not condition:
        raise ControlFailure(code, detail)


def reject(name, fn, intended):
    try:
        fn()
    except ControlFailure as exc:
        need(exc.code == intended, "WRONG_NEGATIVE_REASON", [name, intended, exc.code])
        negatives.append({"name": name, "intended": intended, "observed": exc.code,
                          "detail": exc.detail})
    else:
        raise ControlFailure("NEGATIVE_ACCEPTED", name)


def divs(xs, n):
    return {math.gcd(x - y, n) for x in xs for y in xs}


def tile(xs, ys, n):
    if len(xs) * len(ys) != n:
        return False
    return len({(x + y) % n for x in xs for y in ys}) == n


def validate_tile(xs, ys, n):
    need(len(set(xs)) == len(xs) and len(set(ys)) == len(ys), "REPEATED_INPUT")
    need(len(xs) * len(ys) == n, "CARDINALITY")
    seen = set()
    for x in xs:
        for y in ys:
            z = (x + y) % n
            need(z not in seen, "DUPLICATE_REPRESENTATION", z)
            seen.add(z)
    need(len(seen) == n, "COVERAGE")


def validate_dilation(xs, ys, n, r):
    need(math.gcd(r, len(xs)) == 1, "MULTIPLIER_NOT_COPRIME_TO_MOVED_FACTOR")
    rx = sorted({(r * x) % n for x in xs})
    need(len(rx) == len(xs), "DILATION_COLLAPSED")
    validate_tile(rx, ys, n)


def uniquely_decipherable(words):
    # Sardinas-Patterson on finite strings, with equality checked before residuals.
    current = {v[len(u):] for u in words for v in words
               if u != v and v.startswith(u)}
    previous = set()
    while current:
        frozen = frozenset(current)
        if frozen in previous:
            return True
        previous.add(frozen)
        following = set()
        for suffix in current:
            for word in words:
                if suffix == word:
                    return False
                if suffix.startswith(word):
                    following.add(suffix[len(word):])
                if word.startswith(suffix):
                    following.add(word[len(suffix):])
        current = following
    return True


def factor_complete(words):
    # NFA for words*: strict codeword prefixes are states, and a completed
    # codeword resets to the empty prefix. All states are accessible/coaccessible.
    # A word is a factor of words* iff some path labeled by it exists. Explore
    # the powerset from ALL states; emptiness is an exact missing-factor witness.
    prefixes = {w[:j] for w in words for j in range(len(w))}
    all_states = frozenset(prefixes)
    seen = {all_states}
    queue = collections.deque([(all_states, "")])
    while queue:
        states, label = queue.popleft()
        for letter in "ab":
            nxt = set()
            for state in states:
                word = state + letter
                if word in prefixes:
                    nxt.add(word)
                if word in words:
                    nxt.add("")
            label2 = label + letter
            if not nxt:
                return False, label2, len(seen)
            frozen = frozenset(nxt)
            if frozen not in seen:
                seen.add(frozen)
                queue.append((frozen, label2))
    return True, "", len(seen)


def validate_actual_border(words, n):
    need("b" in words and "a" * n in words, "MISSING_ACTUAL_ATOMS")
    need(uniquely_decipherable(words), "NOT_UNIQUELY_DECIPHERABLE")
    complete, witness, states = factor_complete(words)
    need(complete, "NOT_FACTOR_COMPLETE", witness)
    p, q = set(), set()
    for word in words:
        j = word.find("b")
        if j >= 0 and word == "a" * j + "b" * (len(word) - j):
            p.add(j % n)
        j = len(word) - len(word.lstrip("b"))
        if j and word == "b" * j + "a" * (len(word) - j):
            q.add((len(word) - j) % n)
    validate_tile(sorted(p), sorted(q), n)
    return sorted(p), sorted(q), states


def odd_rep(r):
    return r if r % 2 else r + 1155


def first_identity(x, n):
    need(math.gcd(7*x, n) == 7*math.gcd(x, 165), "CROSS_GCD_FIRST")


def second_identity(y, h, n):
    need(math.gcd(h*y, n) == 7*h, "CROSS_GCD_SECOND")


def final_identity(value, p0, n):
    need(math.gcd(value-p0, n) == 1, "FINAL_GCD_NOT_ONE",
         math.gcd(value-p0, n))


def neighbors(primes, minimum_shared):
    ans = []
    for x in range(165):
        bits = 0
        for y in range(165):
            if x != y and sum((x-y) % p == 0 for p in primes) >= minimum_shared:
                bits |= 1 << y
        ans.append(bits)
    return ans


def connected(e, adjacent):
    universe = (1 << 165) - 1
    seen = 1
    frontier = 1
    while frontier:
        lsb = frontier & -frontier
        frontier ^= lsb
        v = lsb.bit_length() - 1
        opposite = (universe ^ e) if ((e >> v) & 1) else e
        new = adjacent[v] & opposite & ~seen
        seen |= new
        frontier |= new
    return seen == universe


def validate_connected(e, adjacent):
    need(connected(e, adjacent), "H_DISCONNECTED")


def enumerate_small(moduli):
    result = {}
    for n in moduli:
        variants = {}
        for d in range(1, n+1):
            if n % d == 0:
                variants[d] = [(0,) + s for s in itertools.combinations(range(1, n), d-1)]
        processed = nt = dilations = 0
        for d, left in variants.items():
            right = variants[n//d]
            dl = [(x, divs(x,n)) for x in left]
            dr = [(x, divs(x,n)) for x in right]
            for x, dx in dl:
                for y, dy in dr:
                    processed += 1
                    is_tile = tile(x,y,n)
                    need(is_tile == (dx & dy == {n}), "SANDS_DISAGREEMENT", [n,x,y])
                    if is_tile:
                        nt += 1
                        for r in range(1,n+1):
                            if math.gcd(r,len(x)) == 1:
                                validate_dilation(x,y,n,r)
                                dilations += 1
        result[str(n)] = {"pairs": processed, "tilings": nt, "dilations": dilations}
    return result


def family_instances(Ks):
    result = {"tilings": 0, "projected_pairs": 0, "q_both_branch": 0,
              "p_both_branch": 0, "unanchored_splits": 0}
    for K in Ks:
        n = 1155 * 2**K
        for a in range(K+1):
            b = K-a
            for odd in (1,7):
                size = odd * 2**a
                P = list(range(size))
                Q = [size*j for j in range(n//size)]
                validate_tile(P,Q,n)
                result["unanchored_splits"] += 1
                if odd != 7:
                    continue
                result["tilings"] += 1
                NP = n//165
                PP = {(165*p) % n for p in P}
                need(len(PP) == len(P), "165P_COLLAPSED")
                validate_tile(sorted(PP), Q, n)
                need(len({p % NP for p in P}) == len(P), "PROJECTION_COLLAPSED")
                qr = [[] for _ in range(165)]
                pg = [[] for _ in range(7)]
                for q in Q:
                    qr[q % 165].append(q)
                for p in P:
                    pg[p % 7].append(p)
                need(all(len(q)==2**b for q in qr), "FIBER_SIZE")
                need(all(len(p)==2**a for p in pg), "P_FIBER_SIZE")
                qmix = [len({q % 2 for q in group}) == 2 for group in qr]
                pmix = [len({p % 2 for p in group}) == 2 for group in pg]
                for r in range(165):
                    V = {((q-r)//165) % NP for q in qr[r]}
                    W = {(7*v) % 2**K for v in V}
                    need(len(W) == len(V), "SEVEN_V_COLLAPSED")
                    for gamma in range(7):
                        X = {p % 2**K for p in pg[gamma]}
                        need(len(X) == len(pg[gamma]), "GAMMA_PROJECTION_COLLAPSED")
                        validate_tile(sorted(X),sorted(W),2**K)
                        need(pmix[gamma] != qmix[r], "PARITY_DICHOTOMY")
                        result["projected_pairs"] += 1
                if all(qmix):
                    need(not any(pmix), "MIXED_GLOBAL_BRANCH")
                    result["q_both_branch"] += 1
                else:
                    need(not any(qmix) and all(pmix), "MIXED_GLOBAL_BRANCH")
                    result["p_both_branch"] += 1
    return result


def arithmetic(config):
    checks = {"odd_residues": 0, "second_gcd_cases": 0, "final_instances": 0}
    A,Y = config["A"],config["Y"]
    need({abs(x-y) for x in A for y in A if (x-y)%2} == {3,5,11}, "A_DIFFERENCES")
    need(0 in Y and 1 in Y and math.gcd(8,1155)==1, "ANCHORS")
    ds = [d for d in range(1,166) if 165%d == 0]
    for K in config["gcd_K"]:
        n = 1155*2**K
        for r in range(1155):
            x = odd_rep(r)
            g = math.gcd(x,n)
            h = math.gcd(x,165)
            first_identity(x,n)
            if h > 1 and x%7:
                prime = next(p for p in (3,5,11) if x%p == 0)
                need(g % prime == 0 and math.gcd(g//prime, 7*2**K)==1,
                     "TAIL_RULE_MULTIPLIER")
            if h > 1 and x%7 == 0:
                for p in (3,5,11):
                    if x%p == 0:
                        need(math.gcd(g//p,7*2**K) != 1, "TAIL_RULE_LOST_SEVEN")
            if x%7 == 0:
                for hh in ds:
                    if hh%h == 0:
                        second_identity(x,hh,n)
                        checks["second_gcd_cases"] += 1
            checks["odd_residues"] += 1
        for j in range(12):
            q = 6+165*j
            value = q if q%2 else q-1
            need(value%2 == 1 and math.gcd(value,165) > 1, "CLASS_SIX")
    for K in range(1,config["final_K_max"]+1):
        n=1155*2**K
        for j in range(1,2**min(K,7),2):
            p0=1155*j
            final_identity(8,p0,n)
            checks["final_instances"] += 1
    return checks


def graph_controls(seed_count, m15):
    primes=(3,5,11)
    n1=neighbors(primes,1)
    n2=neighbors(primes,2)
    samples=0
    for ell in primes:
        m=165//ell
        masks=[1, (1<<m)-2, sum(1<<i for i in range(0,m,2))]
        for seed in range(seed_count):
            value=int.from_bytes(hashlib.sha256((str(ell)+":"+str(seed)).encode()).digest(), "big")
            mask=value & ((1<<m)-1)
            if mask and mask != (1<<m)-1:
                masks.append(mask)
        for mask in masks:
            E=sum(1<<r for r in range(165) if (mask>>(r%m))&1)
            validate_connected(E,n1)
            samples += 1
    need(m15 == 15, "UNEXPECTED_EXHAUSTIVE_MODULUS")
    local=[sum(1<<v for v in range(m15)
               if u!=v and ((u-v)%3 == 0 or (u-v)%5 == 0)) for u in range(m15)]
    full=(1<<m15)-1
    count=0
    for mask in range(1,full):
        other=full^mask
        remaining=mask
        found=False
        while remaining:
            bit=remaining & -remaining
            remaining ^= bit
            if local[bit.bit_length()-1] & other:
                found=True
                break
        need(found, "CRT_CROSS_EDGE_MISSING", mask)
        count += 1
    reject("extend H to full period E={0}", lambda: validate_connected(1,n1), "H_DISCONNECTED")
    E=sum(1<<r for r in range(165) if r%5 == 0)
    reject("require two common prime coordinates", lambda: validate_connected(E,n2), "H_DISCONNECTED")
    return {"periodic_full_165_graph_samples": samples,
            "exhaustive_cross_cut_partitions_Z15": count}


with open(sys.argv[1], "r", encoding="utf-8") as f:
    cfg=json.load(f)
negatives=[]
out={"scope": "finite diagnostics only; never an all-k proof"}
n=cfg["border_positive_n"]
ps=cfg["border_positive_P"]
qs=cfg["border_positive_Q"]
words={"a"*n} | {"a"*p+"b"+"a"*q for p in ps for q in qs}
actual_p,actual_q,states=validate_actual_border(words,n)
need(actual_p==ps and actual_q==qs, "ACTUAL_BORDER_WRONG")
out["actual_word_border"]={"n": n, "words": sorted(words), "P": actual_p,
                            "Q": actual_q, "factor_automaton_subset_states": states}
reject("add a^2 to code containing a^6", lambda: validate_actual_border(words | {"aa"},n),
       "NOT_UNIQUELY_DECIPHERABLE")
reject("delete completion atoms", lambda: validate_actual_border({"a"*n,"b","ab"},n),
       "NOT_FACTOR_COMPLETE")
validate_tile(ps,qs,n)
reject("overlapping same-size factors", lambda: validate_tile([0,2],qs,n), "DUPLICATE_REPRESENTATION")
reject("omit size hypothesis", lambda: validate_tile([0],qs,n), "CARDINALITY")
need(divs([0],n) & divs(qs,n) == {n}, "SIZE_MUTATION_SETUP")
validate_dilation(ps,qs,n,3)
need(math.gcd(3,n)>1 and math.gcd(3,len(ps))==1, "NONUNIT_DILATION_SETUP")
reject("use multiplier coprime only to complement", lambda: validate_dilation(ps,qs,n,2),
       "MULTIPLIER_NOT_COPRIME_TO_MOVED_FACTOR")
reject("actual bad multiplier creates collision", lambda: validate_tile([0,2],qs,n),
       "DUPLICATE_REPRESENTATION")
out["small_group_exhaustion"]=enumerate_small(cfg["small_moduli"])
out["family_instances"]=family_instances(cfg["family_K"])
out["arithmetic"]=arithmetic(cfg)
reject("introduce a second factor of seven into n", lambda: first_identity(7,2310*7), "CROSS_GCD_FIRST")
reject("omit h0 divides h", lambda: second_identity(21,5,2310), "CROSS_GCD_SECOND")
reject("replace anchor 8 by 6", lambda: final_identity(6,1155,2310), "FINAL_GCD_NOT_ONE")
out["lemma_H"]=graph_controls(cfg["lemma_H_seed_count_per_prime"],cfg["exhaustive_crt_modulus"])
out["negative_controls"]=negatives
out["result"]="PASS"
print(json.dumps(out, indent=2, sort_keys=True))
