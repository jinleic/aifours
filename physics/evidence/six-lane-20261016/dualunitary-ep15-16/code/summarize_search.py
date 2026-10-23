"""Aggregate float search outputs (evidence/search/*.jsonl) into evidence/search_summary.json (candidates only)."""
import collections
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(HERE, "..", "evidence")


def main():
    summ = {"files": {}, "strata_counts": collections.Counter(), "max_ep_non_O9_converged": 0.0,
            "non_O9_points_with_rank_UG_gt_6": [], "ascent_maxima": collections.Counter()}
    for path in sorted(glob.glob(os.path.join(EV, "search", "*.jsonl"))):
        name = os.path.basename(path)
        n = 0
        for line in open(path):
            r = json.loads(line)
            n += 1
            infos = []
            if "start_info" in r:
                infos = [("start", r["start_info"]), ("max", r["max_info"])]
                b = r["max_info"]
                summ["ascent_maxima"][f"tangent{b['tangent_dim']}-rank{b['rank_UG']}-ep{round(b['ep'], 6)}"] += 1
            elif "rank_UG" in r and "ep" in r and r.get("res", 0) < 1e-11:
                infos = [("point", {"tangent_dim": r.get("tangent_dim"), "rank_UG": r["rank_UG"], "ep": r["ep"]})]
            for tag, inf in infos:
                summ["strata_counts"][f"{tag}:tangent{inf.get('tangent_dim')}-rank{inf['rank_UG']}"] += 1
                if inf["ep"] < 1 - 1e-9:
                    summ["max_ep_non_O9_converged"] = max(summ["max_ep_non_O9_converged"], inf["ep"])
                    if inf["rank_UG"] > 6:
                        summ["non_O9_points_with_rank_UG_gt_6"].append(
                            {"file": name, "seed": r.get("seed"), "t": r.get("t", r.get("run")), "tag": tag,
                             "ep": inf["ep"], "tangent_dim": inf.get("tangent_dim"),
                             "note": "see LOG: near-singular, within 3e-7 of rank-4 dual points" })
        summ["files"][name] = n
    summ["strata_counts"] = dict(summ["strata_counts"])
    summ["ascent_maxima"] = dict(summ["ascent_maxima"])
    with open(os.path.join(EV, "search_summary.json"), "w") as f:
        json.dump(summ, f, indent=1)
    print(json.dumps({k: v for k, v in summ.items() if k != "files"}, indent=1))


if __name__ == "__main__":
    main()
