#!/usr/bin/env python3
"""Independent exact reconstruction and finite Shannon-separator controls.

Reads only the f122 manifest and its three inputs. Never imports author code.
Creates only the three finite-* JSON receipts, and refuses any overwrite.
"""

from collections import Counter
from copy import deepcopy
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest-v1.json"
MANIFEST_SHA = "b8bdc86c7281c3c8e1d0c6a2abdc980848e620650a8df95906cae854a6524907"
NAMES = "BCRHPQ"
FULL = (1 << len(NAMES)) - 1
OUT_ROWS = ROOT / "finite-rows-v1.json"
OUT_CONTROLS = ROOT / "finite-controls-v1.json"
OUT_RESULT = ROOT / "finite-result-v1.json"


class ReviewError(Exception):
    def __init__(self, code, detail=None):
        super().__init__(code)
        self.code = code
        self.detail = detail


def require(condition, code, detail=None):
    if not condition:
        raise ReviewError(code, detail)


def digest(data):
    return sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "JSON_DUPLICATE_KEY", key)
        result[key] = value
    return result


def reject_constant(value):
    raise ReviewError("JSON_NONFINITE_CONSTANT", value)


def strict_json(raw):
    try:
        return json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ReviewError("JSON_SYNTAX", str(exc)) from exc


def read_inputs():
    manifest_raw = MANIFEST.read_bytes()
    require(digest(manifest_raw) == MANIFEST_SHA, "MANIFEST_SHA")
    manifest = strict_json(manifest_raw)
    inputs = manifest["inputs_in_read_order"]
    require(len(inputs) == 3, "INPUT_COUNT")
    expected_roles = ["Self-contained inequality and gluing proof", "Standalone 64-coordinate exact witness", "Author independent witness checker, read not executed"]
    require([item["role"] for item in inputs] == expected_roles, "INPUT_ORDER")
    records = [{"role": "manifest", "path": str(MANIFEST), "sha256": digest(manifest_raw), "bytes": len(manifest_raw), "LF": manifest_raw.count(b"\n")}]
    contents = []
    for item in inputs:
        raw = Path(item["path"]).read_bytes()
        measured = {"role": item["role"], "path": item["path"], "sha256": digest(raw), "bytes": len(raw), "LF": raw.count(b"\n")}
        for key in ("sha256", "bytes", "LF"):
            require(measured[key] == item[key], "INPUT_PIN", {"path": item["path"], "field": key, "actual": measured[key], "expected": item[key]})
        raw.decode("utf-8", errors="strict")
        records.append(measured)
        contents.append(raw)
    return records, contents


def extract_table(manuscript):
    parts = manuscript.split("```")
    require(len(parts) == 3, "TABLE_FENCE_COUNT", len(parts) - 1)
    require(parts[1].startswith("\n") and parts[1].endswith("\n"), "TABLE_FENCE_LAYOUT")
    return parts[1][1:-1]


def parse_table(block):
    lines = block.splitlines()
    require(len(lines) == 8, "TABLE_ROW_COUNT", len(lines))
    values = []
    for row, line in enumerate(lines):
        match = re.fullmatch(r"\s*([0-9]+)–([0-9]+):[ \t]+(.+?)\s*", line)
        require(match is not None, "TABLE_ROW_SYNTAX", {"row": row, "line": line})
        first, last = int(match.group(1)), int(match.group(2))
        require((first, last) == (8 * row, 8 * row + 7), "TABLE_MASK_ORDER", {"row": row, "range": [first, last]})
        tokens = match.group(3).split()
        require(len(tokens) == 8 and all(re.fullmatch(r"0|[1-9][0-9]*", token) for token in tokens), "TABLE_ROW_VALUES", {"row": row, "tokens": tokens})
        values.extend(int(token) for token in tokens)
    return values


def manuscript_scale(manuscript):
    matches = re.findall(r"divided by `([0-9][0-9,]*)`", manuscript)
    require(len(matches) == 1 and re.fullmatch(r"[1-9][0-9]{0,2}(?:,[0-9]{3})*", matches[0]) is not None, "TABLE_SCALE_SYNTAX", matches)
    require("Order the variable bits `B,C,R,H,P,Q` from least to most significant" in manuscript, "MANUSCRIPT_VARIABLE_ORDER")
    return int(matches[0].replace(",", ""))


def normalize_expression(body, suffix):
    body = body.replace("\\\\", "").replace("&", "")
    body = re.sub(r"\s+", "", body)
    require(body.endswith(suffix), "EXPRESSION_SUFFIX", body[-30:])
    return body[:-len(suffix)]


def extract_expressions(manuscript):
    blocks = re.findall(r"\\Phi=\{\}&(.*?)\\end\{aligned\}", manuscript, flags=re.DOTALL)
    require(len(blocks) == 2, "EXPRESSION_BLOCK_COUNT", len(blocks))
    return normalize_expression(blocks[0], r"\ge0."), normalize_expression(blocks[1], ".")


def mask_for(word):
    require(word and all(c in NAMES for c in word), "VARIABLE_SYNTAX", word)
    indices = [NAMES.index(c) for c in word]
    require(len(indices) == len(set(indices)) and indices == sorted(indices), "VARIABLE_ORDER_OR_DUPLICATE", word)
    return sum(1 << i for i in indices)


def signed_tokens(text, pattern, error):
    if text and text[0] not in "+-":
        text = "+" + text
    result = []
    pos = 0
    while pos < len(text):
        match = pattern.match(text, pos)
        require(match is not None, error, {"offset": pos, "remainder": text[pos:]})
        result.append(match.groups())
        pos = match.end()
    return result


def parse_entropy_expression(text):
    pattern = re.compile(r"([+-])([1-9][0-9]*)?H\(([BCRHPQ]+)\)")
    tokens = signed_tokens(text, pattern, "ENTROPY_EXPRESSION_SYNTAX")
    require(len(tokens) == 16, "MANUSCRIPT_TERM_COUNT", len(tokens))
    result = {}
    for sign, number, word in tokens:
        mask = mask_for(word)
        require(mask not in result, "MANUSCRIPT_DUPLICATE_MASK", mask)
        result[mask] = (1 if sign == "+" else -1) * (int(number) if number else 1)
    return result


def parse_cmi_expression(text):
    pattern = re.compile(r"([+-])([1-9][0-9]*)?I\(([BCRHPQ]);([BCRHPQ])\\mid([BCRHPQ](?:,[BCRHPQ])*)\)")
    tokens = signed_tokens(text, pattern, "CMI_EXPRESSION_SYNTAX")
    require(len(tokens) == 9, "CMI_TERM_COUNT", len(tokens))
    rows = []
    for sign, number, x, y, cond in tokens:
        a, b = mask_for(x), mask_for(y)
        z = mask_for(cond.replace(",", ""))
        require(a != b and (a | b) & z == 0, "CMI_OVERLAP", {"x": x, "y": y, "condition": cond})
        weight = (1 if sign == "+" else -1) * (int(number) if number else 1)
        rows.append((a, b, z, weight))
    require(len(set(rows)) == 9, "CMI_DUPLICATE_ROW")
    require(sorted(row[3] for row in rows) == [-2] + [1] * 8, "CMI_WEIGHTS", [row[3] for row in rows])
    require((16, 32, 15, -2) in rows, "CMI_NEGATIVE_GLUE_ROW")
    return rows


def expand_cmis(rows):
    coefficients = Counter()
    for x, y, z, weight in rows:
        for mask, sign in ((x | z, 1), (y | z, 1), (z, -1), (x | y | z, -1)):
            coefficients[mask] += sign * weight
    return {mask: value for mask, value in coefficients.items() if value != 0}


def differences(left, right):
    return {str(mask): {"left": left.get(mask, 0), "right": right.get(mask, 0)} for mask in sorted(set(left) | set(right)) if left.get(mask, 0) != right.get(mask, 0)}


def symbolic_comparison(entropy_text, cmi_text):
    manuscript_coeff = parse_entropy_expression(entropy_text)
    cmi_rows = parse_cmi_expression(cmi_text)
    expanded = expand_cmis(cmi_rows)
    require(expanded == manuscript_coeff, "MANUSCRIPT_CMI_MISMATCH", differences(manuscript_coeff, expanded))
    require(len(expanded) == 16 and 0 not in expanded, "EXPANDED_TERM_COUNT", len(expanded))
    require(all(not (mask & 16 and mask & 32) for mask in expanded), "MIXED_PQ_COEFFICIENT")
    return manuscript_coeff, cmi_rows, expanded


def validate_doc(doc):
    keys = {"origin_receipt_sha256", "variable_order", "scale", "values_by_subset_mask", "inequality_coefficients_by_mask", "scaled_inequality_value", "scope"}
    require(type(doc) is dict and set(doc) == keys, "JSON_SCHEMA_KEYS")
    require(type(doc["origin_receipt_sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", doc["origin_receipt_sha256"]) is not None, "JSON_ORIGIN_SHA")
    require(doc["variable_order"] == list(NAMES), "JSON_VARIABLE_ORDER")
    require(type(doc["scale"]) is int and doc["scale"] > 0, "JSON_SCALE")
    require(type(doc["scaled_inequality_value"]) is int and type(doc["scope"]) is str, "JSON_VALUE_OR_SCOPE")
    validate_vector(doc["values_by_subset_mask"])


def validate_vector(values):
    require(type(values) is list and len(values) == 64 and all(type(v) is int and v >= 0 for v in values), "VECTOR_FORMAT")
    require(values[0] == 0, "VECTOR_ORIGIN", values[0])


def json_coefficients(doc):
    pairs = doc["inequality_coefficients_by_mask"]
    require(type(pairs) is list and len(pairs) == 16, "JSON_COEFFICIENT_COUNT")
    result = {}
    previous = 0
    for pair in pairs:
        require(type(pair) is list and len(pair) == 2 and all(type(v) is int for v in pair), "JSON_COEFFICIENT_FORMAT", pair)
        mask, value = pair
        require(1 <= mask <= 63 and value != 0, "JSON_COEFFICIENT_RANGE", pair)
        require(mask not in result, "JSON_COEFFICIENT_DUPLICATE", mask)
        require(mask > previous, "JSON_COEFFICIENT_ORDER", pair)
        result[mask] = value
        previous = mask
    return result


def compare_json_coefficients(doc, expanded):
    coefficients = json_coefficients(doc)
    require(coefficients == expanded, "JSON_CMI_MISMATCH", differences(coefficients, expanded))
    return coefficients


def compare_table_json(table_values, scale, doc):
    validate_doc(doc)
    require(scale == doc["scale"], "SCALE_MISMATCH", [scale, doc["scale"]])
    mismatches = [i for i in range(64) if table_values[i] != doc["values_by_subset_mask"][i]]
    require(not mismatches, "TABLE_JSON_MISMATCH", mismatches)


def summary(rows):
    values = [row[-1] for row in rows]
    smallest = min(values)
    positives = [value for value in values if value > 0]
    return {"count": len(values), "minimum": smallest, "minimum_row": rows[values.index(smallest)], "zero_count": values.count(0), "positive_count": len(positives), "minimum_positive": min(positives) if positives else None}


def elemental_rows(h):
    rows = []
    for i in range(6):
        given = FULL ^ (1 << i)
        rows.append(["H", i, given, h[FULL] - h[given]])
    for i in range(6):
        for j in range(i + 1, 6):
            x, y = 1 << i, 1 << j
            for given in range(64):
                if given & (x | y) == 0:
                    slack = h[given | x] + h[given | y] - h[given] - h[given | x | y]
                    rows.append(["I", i, j, given, slack])
    require(len(rows) == 246, "ELEMENTAL_COUNT", len(rows))
    data = summary(rows)
    require(data["minimum"] >= 0, "ELEMENTAL_NEGATIVE", data["minimum_row"])
    return rows, data


def comparable_rows(h):
    rows = [[a, b, h[b] - h[a]] for a in range(64) for b in range(64) if a & b == a]
    require(len(rows) == 729, "COMPARABLE_COUNT", len(rows))
    data = summary(rows)
    require(data["minimum"] >= 0, "MONOTONICITY_NEGATIVE", data["minimum_row"])
    return rows, data


def submodular_rows(h):
    rows = [[a, b, h[a] + h[b] - h[a | b] - h[a & b]] for a in range(64) for b in range(64)]
    require(len(rows) == 4096, "SUBMODULARITY_COUNT", len(rows))
    data = summary(rows)
    require(data["minimum"] >= 0, "SUBMODULARITY_NEGATIVE", data["minimum_row"])
    return rows, data


def dot(coefficients, h):
    return sum(coefficient * h[mask] for mask, coefficient in coefficients.items())


def exact_claim(manuscript, h, scale, coefficients, doc):
    actual = dot(coefficients, h)
    matches = re.findall(r"\\Phi\(r\)=\\frac\{(-?[0-9]+)\}\{([0-9]+)\}=-\\frac\{([0-9]+)\}\{([0-9]+)\}<0", manuscript)
    require(len(matches) == 1, "EXACT_VALUE_SYNTAX", matches)
    numerator, denominator, reduced_num, reduced_den = map(int, matches[0])
    require(actual == doc["scaled_inequality_value"] == numerator and scale == denominator, "EXACT_VALUE_MISMATCH", {"computed": actual, "json": doc["scaled_inequality_value"], "manuscript": numerator, "scale": scale, "manuscript_denominator": denominator})
    value = Fraction(actual, scale)
    require(value == Fraction(-reduced_num, reduced_den) and value < 0, "EXACT_VALUE_REDUCTION", str(value))
    return actual, str(value)


def project(law, mask):
    result = {}
    for outcome, probability in law.items():
        key = tuple(outcome[i] for i in range(6) if mask & (1 << i))
        result[key] = result.get(key, Fraction(0)) + probability
    return result


def exact_binary_entropy_vector(law):
    require(sum(law.values(), Fraction(0)) == 1, "LAW_NOT_NORMALIZED")
    vector = []
    for mask in range(64):
        marginal = project(law, mask)
        n = len(marginal)
        require(n > 0 and n & (n - 1) == 0, "LAW_NON_POWER_TWO_SUPPORT", mask)
        require(all(p == Fraction(1, n) for p in marginal.values()), "LAW_NONUNIFORM_MARGINAL", mask)
        vector.append(n.bit_length() - 1)
    return vector


def cmi_value(h, row):
    x, y, z, _ = row
    return h[x | z] + h[y | z] - h[z] - h[x | y | z]


def finite_gluing_control(coefficients, cmi_rows):
    original = {}
    glued = {}
    for u, v, w, s in product(range(2), repeat=4):
        outcome = (u, v, w, u ^ w, s ^ u, s ^ v)
        original[outcome] = original.get(outcome, Fraction(0)) + Fraction(1, 16)
    for u, v, w, s, t in product(range(2), repeat=5):
        outcome = (u, v, w, u ^ w, s ^ u, t ^ v)
        glued[outcome] = glued.get(outcome, Fraction(0)) + Fraction(1, 32)
    for mask in (15, 31, 47):
        require(project(original, mask) == project(glued, mask), "GLUING_MARGINAL", mask)
    y = project(glued, 15)
    yp = project(glued, 31)
    yq = project(glued, 47)
    for state, py in y.items():
        for p, q in product(range(2), repeat=2):
            joint = glued.get(state + (p, q), Fraction(0))
            require(joint * py == yp.get(state + (p,), Fraction(0)) * yq.get(state + (q,), Fraction(0)), "GLUING_CONDITIONAL_PRODUCT", [state, p, q])
    orig_h = exact_binary_entropy_vector(original)
    glued_h = exact_binary_entropy_vector(glued)
    preserved_masks = [mask for mask in range(64) if not (mask & 16 and mask & 32)]
    require(len(preserved_masks) == 48 and all(orig_h[m] == glued_h[m] for m in preserved_masks), "GLUING_ENTROPIES")
    orig_cmi = [cmi_value(orig_h, row) for row in cmi_rows]
    glued_cmi = [cmi_value(glued_h, row) for row in cmi_rows]
    require(all(v >= 0 for v in orig_cmi + glued_cmi), "LAW_NEGATIVE_CMI")
    negative_index = cmi_rows.index((16, 32, 15, -2))
    require(orig_cmi[negative_index] == 1 and glued_cmi[negative_index] == 0, "GLUING_DEPENDENCE_CONTROL", [orig_cmi[negative_index], glued_cmi[negative_index]])
    orig_phi = dot(coefficients, orig_h)
    glued_phi = dot(coefficients, glued_h)
    require(orig_phi == glued_phi == 1, "GLUING_PHI", [orig_phi, glued_phi])
    require(sum(row[3] * value for row, value in zip(cmi_rows, orig_cmi)) == orig_phi, "LAW_ORIGINAL_IDENTITY")
    require(sum(row[3] * value for row, value in zip(cmi_rows, glued_cmi)) == glued_phi, "LAW_GLUED_IDENTITY")
    elemental_rows(orig_h)
    comparable_rows(orig_h)
    submodular_rows(orig_h)
    elemental_rows(glued_h)
    comparable_rows(glued_h)
    submodular_rows(glued_h)
    return {"law": "independent uniform bits U,V,W,S,T; B=U,C=V,R=W,H=U xor W,P=S xor U; Q=S xor V before gluing and T xor V after", "original_atoms": len(original), "glued_atoms": len(glued), "marginals_Y_YP_YQ_equal": True, "conditional_product_all_states": True, "preserved_nonmixed_masks": preserved_masks, "original_entropy_bits": orig_h, "glued_entropy_bits": glued_h, "original_CMI_bits_in_written_order": orig_cmi, "glued_CMI_bits_in_written_order": glued_cmi, "original_I_P_Q_given_Y_bits": orig_cmi[negative_index], "glued_I_P_Q_given_Y_bits": glued_cmi[negative_index], "original_phi_bits": orig_phi, "glued_phi_bits": glued_phi}


def main():
    started = datetime.now().astimezone().isoformat(timespec="microseconds")
    for output in (OUT_ROWS, OUT_CONTROLS, OUT_RESULT):
        require(not output.exists(), "OUTPUT_EXISTS", str(output))
    script_raw = Path(__file__).resolve().read_bytes()
    inputs, contents = read_inputs()
    manuscript = contents[0].decode("utf-8")
    witness_raw = contents[1]
    doc = strict_json(witness_raw)
    validate_doc(doc)
    table = extract_table(manuscript)
    table_values = parse_table(table)
    scale = manuscript_scale(manuscript)
    compare_table_json(table_values, scale, doc)
    entropy_text, cmi_text = extract_expressions(manuscript)
    manuscript_coeff, cmi_rows, expanded = symbolic_comparison(entropy_text, cmi_text)
    json_coeff = compare_json_coefficients(doc, expanded)
    h = doc["values_by_subset_mask"]
    numerator, reduced = exact_claim(manuscript, h, scale, expanded, doc)
    elementary, elementary_summary = elemental_rows(h)
    comparable, comparable_summary = comparable_rows(h)
    submodular, submodular_summary = submodular_rows(h)

    controls = []
    def rejected(name, payload, expected, callback):
        try:
            callback()
        except ReviewError as exc:
            require(exc.code == expected, "CONTROL_WRONG_REASON", {"name": name, "expected": expected, "actual": exc.code, "detail": exc.detail})
            encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
            controls.append({"name": name, "payload": payload, "payload_canonical_json_sha256": digest(encoded), "expected_error": expected, "observed_error": exc.code, "detail": exc.detail})
        else:
            raise ReviewError("CONTROL_ACCEPTED", name)

    bad_range = table.replace("0–7:", "1–7:", 1)
    require(bad_range != table, "CONTROL_SETUP_RANGE")
    rejected("table_range_out_of_order", bad_range, "TABLE_MASK_ORDER", lambda: parse_table(bad_range))
    table_lines = table.splitlines()
    table_lines[0] += " 9"
    bad_count = "\n".join(table_lines)
    rejected("table_extra_number", bad_count, "TABLE_ROW_VALUES", lambda: parse_table(bad_count))
    bad_table = table.replace("3875000", "3875001", 1)
    require(bad_table != table, "CONTROL_SETUP_TABLE")
    rejected("table_coordinate_vs_json", bad_table, "TABLE_JSON_MISMATCH", lambda: compare_table_json(parse_table(bad_table), scale, doc))
    bad_scale = deepcopy(doc)
    bad_scale["scale"] += 1
    rejected("wrong_scale", bad_scale, "SCALE_MISMATCH", lambda: compare_table_json(table_values, scale, bad_scale))
    duplicate_json = witness_raw.decode("utf-8").replace('"scale": 6900000,', '"scale": 6900000,\n  "scale": 6900000,', 1)
    require(duplicate_json.encode("utf-8") != witness_raw, "CONTROL_SETUP_DUPLICATE_JSON")
    rejected("duplicate_json_key", duplicate_json, "JSON_DUPLICATE_KEY", lambda: strict_json(duplicate_json))
    bad_origin = list(h)
    bad_origin[0] = 1
    rejected("nonzero_empty_set", bad_origin, "VECTOR_ORIGIN", lambda: validate_vector(bad_origin))
    duplicate_coeff = deepcopy(doc)
    duplicate_coeff["inequality_coefficients_by_mask"][1] = list(duplicate_coeff["inequality_coefficients_by_mask"][0])
    rejected("duplicate_json_coefficient_mask", duplicate_coeff, "JSON_COEFFICIENT_DUPLICATE", lambda: json_coefficients(duplicate_coeff))
    wrong_coeff = deepcopy(doc)
    wrong_coeff["inequality_coefficients_by_mask"][0][1] *= -1
    rejected("flipped_json_coefficient", wrong_coeff, "JSON_CMI_MISMATCH", lambda: compare_json_coefficients(wrong_coeff, expanded))
    overlap_cmi = cmi_text.replace(r"I(B;R\midC,H,P,Q)", r"I(B;R\midB,C,H,P,Q)", 1)
    require(overlap_cmi != cmi_text, "CONTROL_SETUP_CMI_OVERLAP")
    rejected("condition_overlaps_target", overlap_cmi, "CMI_OVERLAP", lambda: parse_cmi_expression(overlap_cmi))
    changed_cmi = cmi_text.replace(r"I(B;R\midC,H,P,Q)", r"I(B;R\midC,H,P)", 1)
    require(changed_cmi != cmi_text, "CONTROL_SETUP_CMI")
    rejected("changed_cmi_condition", changed_cmi, "MANUSCRIPT_CMI_MISMATCH", lambda: symbolic_comparison(entropy_text, changed_cmi))
    changed_entropy = entropy_text.replace("-H(BC)", "+H(BC)", 1)
    require(changed_entropy != entropy_text, "CONTROL_SETUP_ENTROPY")
    rejected("flipped_manuscript_entropy_term", changed_entropy, "MANUSCRIPT_CMI_MISMATCH", lambda: symbolic_comparison(changed_entropy, cmi_text))
    bad_terminal = list(h)
    bad_terminal[63] = 0
    rejected("full_set_monotonicity_elemental", bad_terminal, "ELEMENTAL_NEGATIVE", lambda: elemental_rows(bad_terminal))
    rejected("full_set_monotonicity_all_comparable", bad_terminal, "MONOTONICITY_NEGATIVE", lambda: comparable_rows(bad_terminal))
    bad_submod = list(h)
    bad_submod[3] = h[1] + h[2] + 1
    rejected("pair_submodularity_elemental", bad_submod, "ELEMENTAL_NEGATIVE", lambda: elemental_rows(bad_submod))
    rejected("pair_submodularity_all_pairs", bad_submod, "SUBMODULARITY_NEGATIVE", lambda: submodular_rows(bad_submod))

    positives = []
    for name, vector in (("weighted_modular", [scale * sum(weight for i, weight in enumerate((2, 3, 5, 7, 11, 13)) if mask & (1 << i)) for mask in range(64)]), ("uniform_rank_two", [scale * min(mask.bit_count(), 2) for mask in range(64)])):
        validate_vector(vector)
        _, es = elemental_rows(vector)
        _, ms = comparable_rows(vector)
        _, ss = submodular_rows(vector)
        val = dot(expanded, vector)
        require(val >= 0, "POSITIVE_CONTROL_PHI", {"name": name, "numerator": val})
        positives.append({"name": name, "values_by_mask": vector, "elementals": es, "comparable": ms, "submodular": ss, "phi_numerator": val, "phi": str(Fraction(val, scale))})
    gluing = finite_gluing_control(expanded, cmi_rows)
    coefficient_rows = [{"mask": mask, "variables": "".join(NAMES[i] for i in range(6) if mask & (1 << i)), "manuscript": manuscript_coeff[mask], "CMI_expansion": expanded[mask], "JSON": json_coeff[mask]} for mask in sorted(expanded)]
    mixed_masks = [{"mask": mask, "CMI_expansion": expanded.get(mask, 0), "manuscript": manuscript_coeff.get(mask, 0), "JSON": json_coeff.get(mask, 0)} for mask in range(64) if mask & 16 and mask & 32]
    require(all(all(row[key] == 0 for key in ("CMI_expansion", "manuscript", "JSON")) for row in mixed_masks), "MIXED_MASK_COMPARISON")

    rows_receipt = {"format": {"elementals": "[H, variable_index, conditioning_mask, slack] or [I, first_index, second_index, conditioning_mask, slack]", "comparable": "[subset_mask, superset_mask, slack] including equality", "submodular": "[first_mask, second_mask, slack] for all ordered pairs", "all_slacks": "integer numerators with common denominator scale"}, "scale": scale, "elementals": elementary, "comparable": comparable, "submodular": submodular}
    controls_receipt = {"fixture_hash_rule": "SHA256 of UTF-8 json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'))", "negative_controls": controls, "positive_controls": positives, "exact_gluing_law": gluing}
    rows_raw = json_bytes(rows_receipt)
    controls_raw = json_bytes(controls_receipt)
    completed = datetime.now().astimezone().isoformat(timespec="microseconds")
    result = {"status": "FINITE_CHECKS_PASS", "started_local": started, "computation_completed_local": completed, "script_path": str(Path(__file__).resolve()), "script_sha256": digest(script_raw), "inputs_in_read_order": inputs, "table_rows": 8, "table_coordinates": len(table_values), "scale": scale, "coefficient_comparison": coefficient_rows, "mixed_PQ_mask_comparison": mixed_masks, "written_CMI_rows": [{"x_mask": x, "y_mask": y, "condition_mask": z, "weight": weight} for x, y, z, weight in cmi_rows], "elemental": elementary_summary, "comparable_monotonicity": comparable_summary, "all_ordered_submodular_pairs": submodular_summary, "scaled_phi_numerator": numerator, "phi": reduced, "negative_control_count": len(controls), "positive_control_count": len(positives), "finite_gluing_control": {"phi_bits": gluing["glued_phi_bits"], "original_conditional_MI_bits": gluing["original_I_P_Q_given_Y_bits"], "glued_conditional_MI_bits": gluing["glued_I_P_Q_given_Y_bits"]}, "artifacts": {"finite-rows-v1.json": {"sha256": digest(rows_raw), "bytes": len(rows_raw)}, "finite-controls-v1.json": {"sha256": digest(controls_raw), "bytes": len(controls_raw)}}, "scope_limit": "Finite Shannon-cone separation only; one exact law is a control, not a proof of universality or closure. No novelty, independent-model-family, human or formal/kernel clearance."}
    result_raw = json_bytes(result)
    for path, raw in ((OUT_ROWS, rows_raw), (OUT_CONTROLS, controls_raw), (OUT_RESULT, result_raw)):
        with path.open("xb") as stream:
            stream.write(raw)
    print(json.dumps({"status": result["status"], "script_sha256": result["script_sha256"], "result_sha256": digest(result_raw), "rows_sha256": digest(rows_raw), "controls_sha256": digest(controls_raw), "scaled_phi_numerator": numerator, "phi": reduced, "elemental": elementary_summary, "comparable": comparable_summary, "submodular": submodular_summary, "negative_controls": len(controls), "positive_controls": len(positives), "gluing": result["finite_gluing_control"], "started_local": started, "computation_completed_local": completed}, indent=2))


if __name__ == "__main__":
    main()
