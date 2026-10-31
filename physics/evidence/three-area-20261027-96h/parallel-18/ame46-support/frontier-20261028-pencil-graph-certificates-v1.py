#!/usr/bin/env python3
"""Verify compact bipartite support-graph certificates for all 72 pencils."""
import argparse
import collections
import importlib.util
import json
from pathlib import Path
import sys


class GraphCertificateError(ValueError):
    pass


def certify(tensor):
    results = []
    for spectator in range(4):
        active = [a for a in range(4) if a != spectator]
        for level in range(6):
            for pencil in active:
                row_axis, col_axis = [a for a in active if a != pencil]
                edges = {}
                graph = collections.defaultdict(set)
                for coord, coeff in tensor.items():
                    if coord[spectator] != level:
                        continue
                    r, c, owner = coord[row_axis], coord[col_axis], coord[pencil]
                    if (r, c) in edges or coeff == (0, 0):
                        raise GraphCertificateError("overlapping cells or zero coefficient")
                    edges[(r, c)] = owner
                    rv, cv = ("r", r), ("c", c)
                    graph[rv].add(cv)
                    graph[cv].add(rv)
                unseen = set(graph)
                components = []
                while unseen:
                    node = unseen.pop()
                    todo, nodes = [node], {node}
                    while todo:
                        for neighbor in graph[todo.pop()]:
                            if neighbor in unseen:
                                unseen.remove(neighbor)
                                nodes.add(neighbor)
                                todo.append(neighbor)
                    comp_edges = sorted((r, c, owner) for (r, c), owner in edges.items()
                                        if ("r", r) in nodes and ("c", c) in nodes)
                    degrees = sorted(len(graph[v]) for v in nodes)
                    components.append({"vertices": len(nodes), "degrees": degrees, "edges_row_col_owner": comp_edges})
                components.sort(key=lambda x: (x["vertices"], x["edges_row_col_owner"]))
                sizes = [c["vertices"] for c in components]
                label_counts = collections.Counter(edges.values())
                if set(label_counts) != set(range(6)):
                    raise GraphCertificateError("missing pencil parameter")
                for owner in range(6):
                    owned = [(r, c) for (r, c), j in edges.items() if j == owner]
                    if len({r for r, c in owned}) != len(owned) or len({c for r, c in owned}) != len(owned):
                        raise GraphCertificateError("pencil parameter is not a matching")
                if len(edges) == 12:
                    if sizes != [12] or components[0]["degrees"] != [2] * 12 or sorted(label_counts.values()) != [2] * 6:
                        raise GraphCertificateError("12-entry graph is not a single 12-cycle with six two-edge parameters")
                    rank_one_subspace_dim = 0
                elif len(edges) == 9:
                    if sizes != [2, 2, 2, 6] or any(c["degrees"] != [1, 1] for c in components[:3]) or components[3]["degrees"] != [2] * 6:
                        raise GraphCertificateError("9-entry graph is not a 6-cycle plus three isolated edges")
                    isolated = {c["edges_row_col_owner"][0][2] for c in components[:3]}
                    cycle_counts = collections.Counter(e[2] for e in components[3]["edges_row_col_owner"])
                    if len(isolated) != 3 or isolated.intersection(cycle_counts) or sorted(cycle_counts.values()) != [2, 2, 2]:
                        raise GraphCertificateError("9-entry parameter grouping is not 3 singleton and 3 matching pairs")
                    rank_one_subspace_dim = 3
                else:
                    raise GraphCertificateError("unexpected slice support")
                results.append({"spectator": spectator, "level": level, "pencil": pencil,
                                "row_axis": row_axis, "col_axis": col_axis,
                                "support": len(edges), "rank_one_subspace_dim_upper": rank_one_subspace_dim,
                                "basis_rank_sum_lower": 12 - rank_one_subspace_dim,
                                "components": components})
    if len(results) != 72:
        raise GraphCertificateError("incomplete pencil set")
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("verifier", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("dense_verifier", args.verifier)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    tensor, table_sha = mod.load_table(args.table)
    records = certify(tensor)
    changed = dict(tensor)
    changed.pop(min(changed))
    try:
        certify(changed)
    except GraphCertificateError as exc:
        control = str(exc)
    else:
        raise GraphCertificateError("deleted-coordinate mutation incorrectly accepted")
    histogram = collections.Counter((r["support"], r["rank_one_subspace_dim_upper"]) for r in records)
    result = {"table_sha256": table_sha, "records": records,
              "classification": [{"slice_support": k[0], "rank_one_subspace_dim_upper": k[1], "pencils": v} for k, v in sorted(histogram.items())],
              "deletion_control": control,
              "scope": "Support-graph structure only; written argument translates graph structure to rank and orbit-support lower bound."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump({k: result[k] for k in ("table_sha256", "classification", "deletion_control", "scope")}, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
