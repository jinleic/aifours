import json, hashlib
from pathlib import Path
spr_repo = Path('/Users/jinleic/repos/aifours')
spr_own = 'information-science/evidence/three-area-20261023-96h/parallel-18/robust-spr7/'
spr_run = 'institute/runs/three-area-2026-10-23-96h/'
spr_manifest_names = [
 'current-reciprocal-successor-v11-v20-manifest-and-claim-DAG-v1.json',
 'current-reciprocal-successor-v11-v29-entire-union-manifest-and-claim-DAG-v2.json',
 'current-reciprocal-successor-v11-v36-entire-union-manifest-and-claim-DAG-v3.json',
 'current-reciprocal-successor-v11-v38-entire-union-manifest-and-claim-DAG-v4.json',
 'current-reciprocal-successor-v11-v40-entire-union-manifest-and-claim-DAG-v5.json'
]
spr_manifests = []
spr_manifest_pins = []
for number, name in enumerate(spr_manifest_names, 1):
    raw = (spr_repo / spr_own / name).read_bytes()
    spr_manifests.append(json.loads(raw))
    spr_manifest_pins.append({'id': 'M' + str(number), 'path': spr_own + name, 'sha256': hashlib.sha256(raw).hexdigest(), 'LF': raw.count(b'\n'), 'bytes': len(raw), 'included_ranges': [[1, raw.count(b'\n')]], 'role': 'ENTIRE immutable claim/source-index metadata; every declared mathematical body must separately be supplied in full; not proof or acceptance'})
spr_source_fields = [
 (0, 'new_sources'), (0, 'operative_antecedents_and_mathematical_errata'), (0, 'mandatory_process_sources'),
 (1, 'later_sources_all_full'), (1, 'additional_mandatory_process_sources'),
 (2, 'later_sources_ALL_full'), (3, 'additional_sources_ALL_full'), (4, 'additional_sources_ALL_full')
]
spr_source_map = {}
for manifest_index, field in spr_source_fields:
    for original in spr_manifests[manifest_index][field]:
        entry = dict(original)
        entry['declared_at'] = spr_manifest_pins[manifest_index]['id'] + '.' + field
        old = spr_source_map.get(entry['path'])
        if old is not None and old['sha256'] != entry['sha256']:
            raise ValueError('Conflicting immutable metadata pins: ' + entry['path'])
        if old is None:
            spr_source_map[entry['path']] = entry
spr_pm2 = dict(spr_manifests[1]['new_current_parent_qualification_source'])
spr_pm2['declared_at'] = 'M2.new_current_parent_qualification_source'
spr_source_map[spr_pm2['path']] = spr_pm2
spr_extra_inputs = [
 ('B2', spr_own + 'reciprocal-invariant-box-four-curve-duality-consolidated-v2.md', 'ENTIRE original reciprocal v2 whole-cone branch root; qualified by PM1/PM2; B5 reproduces operative arguments; no new proof read or old-verdict transfer'),
 ('B3', spr_own + 'reciprocal-first-critical-four-orbits-and-endpoint-quintic-v3.md', 'ENTIRE original first-critical/four-orbit antecedent; B5 reproduces operative proof; contextual whole branch root, not imported by headline'),
 ('B4', spr_own + 'reciprocal-full-critical-inverse-consolidated-v4.md', 'ENTIRE original inverse antecedent; B5 reproduces operative proof; contextual whole branch root, not imported by headline'),
 ('SEL', spr_own + 'selection-v1.md', 'ENTIRE frozen original statement/model selection; source scope only, not fresh printed-book authentication'),
 ('SEL2', spr_own + 'selection-addendum-v2-even-anchor.md', 'ENTIRE frozen source-selection/anchor qualification; preserve original target and actual model'),
 ('OX6', spr_own + 'owner-written-exact-arithmetic-erratum-v6.json', 'Permanent SIXTH primary symbolic-scope finding; ENTIRE excluded branch and consuming guidance ZERO, do not copy/replay prohibited values'),
 ('P78', spr_run + 'SPR-sixth-parameter-trial-parent-next-review-direction-v78.json', 'Standing original source/proof/rehearsal/method STOP; no clearance by metadata identity or review RETURN'),
 ('R142INV', spr_own + 'peer-review-v142-B-specific-prior-Sun-exposure-finding-v1.json', 'Permanent specific prior-body inventory finding; exposure only, no false-blindness or verdict transfer'),
 ('R142SCOPE', spr_own + 'peer-review-v142-B-private-small-parameter-review-scope-finding-v1.json', 'Permanent remembered small-parameter scope finding; all excluded judgments/guidance ZERO'),
 ('R142FORMAT', spr_own + 'peer-review-v142-B-source-fraction-format-exactness-finding-v1.json', 'Permanent source-fraction FORMAT finding; all excluded judgments/guidance ZERO'),
 ('R142ORDER', spr_own + 'peer-review-v142-B-required-direction-first-order-finding-v1.json', 'Permanent required-direction-FIRST order finding; no later-read cure'),
 ('P90', spr_run + 'post-v89-new-stops-cadence-and-qualified-review-directions-v90.json', 'ENTIRE additive process/authority qualification; no primary resumption or clean-history credit'),
 ('P93', spr_run + 'SPR-v142-source-fraction-format-parent-direction-v93.json', 'ENTIRE additive review FORMAT qualification and historical same-scope direction; no original-primary permission'),
 ('P97', spr_run + 'SPR-v142-direction-first-order-parent-direction-v97.json', 'ENTIRE additive complete-direction-FIRST order qualification; no original-primary permission'),
 ('P121', spr_run + 'SPR-v153-stage1-cadence-qualified-entire-review-admission-v121.json', 'ENTIRE prior153 admission qualification; retains distinct136 FULL30m22 cadence'),
 ('CP136', spr_own + 'resume-checkpoint-v136-v153-A-whole-primary-and-cadence-finding-v1.json', 'ENTIRE whole pre153 primary and distinct FULL30m22 cadence finding; no source-proof clearance'),
 ('ACK153', spr_own + 'peer-review-v153-A-opaque-ack-v1.json', 'ENTIRE specific serial/nonblind exposure inventory and findings; semigroup/Sun/etc contacts context only, not SPR proof premises'),
 ('CP139', spr_own + 'resume-checkpoint-v139-v153-A-complete-before-actual-return-v1.json', 'ENTIRE actual153 completion/source-contact metadata; not exact RETURN clock or SPR result'),
 ('POST153ACK', spr_own + 'primary-post-v153-RETURN-WHOLE-ACK-WAIT-metadata-only-v1.json', 'ENTIRE required NEW whole ACK and NEW FULL2h16m00 cadence finding; all prior leads/contacts/STOP retained'),
 ('P108', spr_run + 'semigroup-post-v96-control-withdrawn171-parent-direction-v108.json', 'ENTIRE later author-control/withdrawn171 process-only qualification; no semigroup mathematical input to SPR gate'),
 ('AUTHOR108', 'mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/primary-post-v96-frozen-band-control-scope-self-stop-v1.json', 'ENTIRE actual author-control finding; ENTIRE171 and excluded guidance ZERO; process context only, no withdrawn proof included'),
 ('P138', spr_run + 'parent-checkpoint103-104-105-two-cadence-findings-v138.json', 'ENTIRE TWO distinct Main cadence findings FULL30m02 and31m10; actual observation spans, not native-write/continuous-work clocks'),
 ('P157', spr_run + 'NL-SPR-new-postreturn-cadences-qualified-entire-metadata-authority-v157.json', 'ENTIRE CURRENT explicit metadata-only authority after complete whole ACK read; original78 STOP retained; no mathematical permission')
]
for source_id, path, role in spr_extra_inputs:
    spr_source_map[path] = {'id': source_id, 'path': path, 'role': role, 'declared_at': 'CURRENT metadata-only field map under P157; no new mathematical derivation'}
spr_pin_errors = []
for entry in spr_source_map.values():
    raw = (spr_repo / entry['path']).read_bytes()
    actual = {'sha256': hashlib.sha256(raw).hexdigest(), 'LF': raw.count(b'\n'), 'bytes': len(raw)}
    if entry.get('sha256', actual['sha256']) != actual['sha256'] or entry.get('LF', actual['LF']) != actual['LF']:
        spr_pin_errors.append({'path': entry['path'], 'expected_sha256': entry.get('sha256'), 'expected_LF': entry.get('LF'), 'actual': actual})
    entry.update(actual)
    entry['included_ranges'] = [[1, actual['LF']]]
    entry['coverage'] = 'REQUIRED_COMPLETE_LITERAL_BODY; current byte metadata is NOT a proof-body read'
if spr_pin_errors:
    raise ValueError(json.dumps(spr_pin_errors, ensure_ascii=False))
spr_claim_fields = [(0, 'claim_nodes', 'claim_DAG_topological_order'), (1, 'later_claim_nodes', 'later_claim_DAG_topological_order'), (2, 'later_claim_nodes', 'later_claim_DAG_topological_order'), (3, 'new_claim_nodes', 'new_claim_DAG_topological_order'), (4, 'new_claim_nodes', 'new_claim_DAG_topological_order')]
spr_claim_index = []
spr_claim_roots = []
for manifest_index, field, order_field in spr_claim_fields:
    manifest_id = spr_manifest_pins[manifest_index]['id']
    nodes = spr_manifests[manifest_index][field]
    spr_claim_roots.append({'manifest': manifest_id, 'all_claims_field': field, 'topological_order_field': order_field, 'claim_count': len(nodes), 'claim_ids_in_existing_order': spr_manifests[manifest_index][order_field], 'full_quantifiers_conclusions_relationships': 'Read EVERY original object in the pinned field; descriptions are not rewritten or adopted by this metadata map'})
    for node in nodes:
        spr_claim_index.append({'id': node['id'], 'source_id': node['source'], 'requires': node['requires'], 'literal_claim_field': manifest_id + '.' + field + '[id=' + node['id'] + ']', 'role': 'ENTIRE original quantified claim AND dependency/application; not a selected headline gate'})
if len({node['id'] for node in spr_claim_index}) != len(spr_claim_index):
    raise ValueError('Duplicate claim ID in frozen metadata fields')
spr_union_meta = {
 'schema_version': 1,
 'owner': 'InfoSPR7-2',
 'status': 'ONE_CURRENT_IMMUTABLE_EXISTING_SOURCE_IDENTITY_AND_FIELD_MAP_ONLY; NO_NEW_MATHEMATICS_OR_DISPATCH',
 'permission': {'record': spr_run + 'NL-SPR-new-postreturn-cadences-qualified-entire-metadata-authority-v157.json', 'observed_permission_clock': '2026-10-26T16:45:37-0700 PDT', 'actual_preEval_metadata_clock': 'Mon Oct 26 16:46:55 PDT 2026', 'read_order': 'Complete157 FIRST then complete138 in separate returned calls BEFORE this byte/field-only cell; prior wholeACK written/sent and completely Main-read'},
 'identity_rule': 'M5 is the EXISTING comprehensive root. Recursively expand M5->M4->M3->M2->M1 and ALL declared full bodies. This artifact pins/maps those existing fields, not a duplicate proof or fresh scientific theorem. Later mathematical successors require a separate future manifest; none is silently merged.',
 'existing_manifest_identity': spr_manifest_pins[-1],
 'all_manifest_inputs_FULL': spr_manifest_pins,
 'per_input_path_hash_FULL_LF_range_role_map': list(spr_source_map.values()),
 'metadata_counts': {'manifest_inputs': len(spr_manifest_pins), 'distinct_source_process_statement_inputs': len(spr_source_map), 'individual_claim_nodes': len(spr_claim_index), 'whole_claim_field_roots': len(spr_claim_roots), 'live_pin_discrepancies': spr_pin_errors},
 'ALL_individual_claim_field_index': spr_claim_index,
 'ALL_whole_claim_field_roots': spr_claim_roots,
 'whole_branch_roots': [
  {'id': 'ORIGINAL_ALL_MONIC_SEPTIC', 'fields': ['M5.original_target_unchanged', 'M5.exact_remaining_gap', 'M3.exact_current_residual'], 'scope': 'Original unrestricted source-box/plant-segment intersection remains unexhibited/open; reciprocal INPUT subclass never replaces all original boxes'},
  {'id': 'RECIPROCAL_ORIGINAL_EXHAUSTIVE_CONE', 'inputs': ['B2', 'B3', 'B4', 'B5', 'B9', 'B10', 'E10', 'RT', 'ERT', 'PM1', 'PM2'], 'fields': ['M1.operative_ancestry_not_extra_hidden_imports', 'M1.scope_and_notation_errata_in_force'], 'scope': 'ENTIRE original-model reciprocal first-failure/inverse/duality and weak-quadratic exclusion; v2/v5 actual-box restriction and all typing/sign/admission qualifiers'},
  {'id': 'W_I_ENTIRE', 'inputs': ['B5', 'B9', 'B10', 'E10', 'W1', 'ZT', 'N37', 'N38'], 'fields': ['M4.new_claim_nodes', 'M4.current_strengthening_and_residual'], 'scope': 'Entire WI actual-model branch and pre-scaled FIXED-PHASE UNBOUNDED-depth necessary model, all rates/weak source/zero amplitude/ALL-zero cases; no finite-WI emptiness or global compact closure'},
  {'id': 'W_II_STRICTQ_ENTIRE', 'inputs': ['N11', 'N12', 'N13', 'N14', 'N21', 'N22', 'N23', 'N28', 'N29', 'N39'], 'fields': ['M1.claim_nodes', 'M2.later_claim_nodes', 'M5.new_claim_nodes'], 'scope': 'ENTIRE WII plus SAME-point boundary-to-WI coverage, strict-Q independent contribution, source walls/ALL selected-extra-coincident zeros; original finite plant-segment intersection unresolved'},
  {'id': 'W_III_ENTIRE', 'inputs': ['N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N19', 'N20', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N38', 'N39'], 'fields': ['M1.claim_nodes', 'M2.later_claim_nodes', 'M3.later_claim_nodes', 'M4.new_claim_nodes', 'M5.new_claim_nodes'], 'scope': 'EVERY whole target/phase, full finite system, ALL source/positive-zero guards, pre-scaled fixed-phase UNBOUNDED-depth argument and all weak-model cases; source/target/phase-boundary finite-depth physical feasibility NOT inferred'},
  {'id': 'CONDITIONAL_RATIONALITY_AND_BOUNDARY_TRANSFER', 'inputs': ['N18', 'N35', 'N36', 'N40'], 'fields': ['M1.claim_nodes[id=C18_RATIONAL_DUAL]', 'M3.later_claim_nodes[id=C35_CONDITIONAL_GERM]', 'M3.later_claim_nodes[id=C36_ROUTE_DISPOSITION]', 'M5.new_claim_nodes'], 'scope': 'Separate conditional results and their exact unexhibited/vacuous antecedents; no actual tuple, rational atoms, closed-width point, feasibility, attainment or original all-seven-width witness'}
 ],
 'mandatory_field_map': [
  {'topic': 'OPERATIVE_V2_V5_V9_V10', 'fields': ['M1.operative_antecedents_and_mathematical_errata', 'M1.operative_ancestry_not_extra_hidden_imports', 'M1.scope_and_notation_errata_in_force', 'M2.new_current_parent_qualification_source'], 'inputs': ['B2', 'B3', 'B4', 'B5', 'B9', 'B10', 'E10', 'PM1', 'PM2'], 'qualifiers': 'Original reciprocal INPUT restriction only; actual P difference2J vs real phi difference2Z after inverse; d0<x1 IMPOSED; odd leading -1/rational gain qualification; whole weak-quadratic strict transfer; explicit orientation referent'},
  {'topic': 'PM2_FOUR_DISTINCT', 'fields': ['M2.new_current_parent_qualification_source.four_separate_qualifications', 'M5.whole_inherited_union_REQUIRED.mandatory_qualifiers'], 'inputs': ['PM2'], 'qualifiers': 'False optional STRICT-window converse; degree6 pre-cancellation SIX not5; intrinsic5D/smoothness/constant-rank NOT_RECONSTRUCTED; old C4 lag referent wrong, C4 LEADS B/B LAGS C4. General43/13/8 only at stated node/weaktarget conditions; old wholeTheoremJ NR; no old formal middle compactness credit'},
  {'topic': 'ALL_SOURCE_ZEROS_PAL_NONPAL_WHOLE_BOX_BEFORE_DUAL', 'fields': ['M1.whole_positive_zero_Hurwitz_amplitude_admission_contract', 'M2.whole_admission_order_current', 'M3.whole_current_admission_and_boundary_order', 'M5.whole_positive_zero_source_admission_contract'], 'inputs': ['N11', 'N12', 'N13', 'N14', 'N17', 'N21', 'N22', 'N23', 'N25', 'N26', 'N27', 'N28', 'N29', 'N39', 'N40'], 'qualifiers': 'ALL pal/nonpal selected-extra-coincident-higher/unweighted zeros, source amplitudes and actual source/Hurwitz/width/target/global positivity guards; N40 closed-width sufficiency is a separately CONDITIONAL guard-preserving transfer, not old-chart widening'},
  {'topic': 'PRESCALED_FIXED_PHASE_UNBOUNDED_DEPTH', 'fields': ['M3.later_claim_nodes[id=C31_EXPLICIT_OPPOSITE_TAIL]', 'M3.later_claim_nodes[id=C32_ALLPHASE_LINEAR_GROWTH]', 'M3.later_claim_nodes[id=C33_FULL_BOUNDED_RESCALING]', 'M3.later_claim_nodes[id=C34_ENTIRE_INNER_MODEL]', 'M3.later_claim_nodes[id=C36_ALLWEAKMODEL_EMPTY]', 'M4.new_claim_nodes'], 'inputs': ['N30', 'N31', 'N32', 'N33', 'N34', 'N36', 'N37', 'N38'], 'qualifiers': 'Full actual pre-limit source/coefficients/contact bounds and EVERY phase/rate/weak-limit/zero-amplitude derivative case; no isolated contact-only replacement or generic-rank assumption'},
  {'topic': 'V35_CONDITIONAL_GERM_VACUITY', 'fields': ['M3.later_claim_nodes[id=C35_CONDITIONAL_GERM]', 'M3.later_claim_nodes[id=C36_ROUTE_DISPOSITION]', 'M3.current_strengthening_independence_status', 'M4.current_strengthening_and_residual', 'M5.current_frontier_and_nonpromotion'], 'inputs': ['N35', 'N36'], 'qualifiers': 'Conditional implication retained at complete hypotheses, later leading antecedent excluded by N36; no actual family or germ/witness. Preserve pointwise/nonuniform whole-phase vs separately proved compact-interior-phase uniformity'},
  {'topic': 'UNIFORMITY_NOT_GLOBAL_COMPACTNESS', 'fields': ['M3.later_claim_nodes[id=C36_FIXEDPHASE_DEPTH_BOUNDED]', 'M4.new_claim_nodes[id=C38_JOINT_COMPACTPHASE_UNIFORMITY]', 'M4.new_claim_nodes[id=C38_PHASE_ESCAPE_RESIDUAL]', 'M5.new_claim_nodes[id=C39_COMPACT_STRICT_TARGET_UNIFORMITY]', 'M5.current_frontier_and_nonpromotion'], 'inputs': ['N36', 'N38', 'N39'], 'qualifiers': 'Fixed phase bound is not uniform over entire phase chart; N38 separately asserts compact INTERIOR-phase delta uniformity only. N39 compact STRICT-target coordinate guards do not give admissible closure, attainment, point or feasibility'},
  {'topic': 'CONDITIONAL_RATIONALITY_SEPARATE', 'fields': ['M1.claim_nodes[id=C18_RATIONAL_DUAL]', 'M1.whole_positive_zero_Hurwitz_amplitude_admission_contract.finite_rationality', 'M5.new_claim_nodes[id=C40_ALL7_WIDTH_TRANSFER]'], 'inputs': ['N18', 'N40'], 'qualifiers': 'Unexhibited ACTUAL original-class physical obstruction precedes rationality or all-width transfer; no finite certificate/data or numerical trial instantiated'},
  {'topic': 'ORIGINAL_OPEN_PLANT_SEGMENT_INTERSECTION', 'fields': ['M5.original_target_unchanged', 'M5.exact_remaining_gap', 'M5.current_frontier_and_nonpromotion', 'M4.current_strengthening_and_residual.exact_missing'], 'qualifiers': 'Actual guarded finite-depth WI/WII_strict/WIII source-box/plant-segment intersection remains unexhibited; original general nonreciprocal/universal problem OPEN. Representation, partial exclusion, bounds and conditional bridges not full emptiness/attainment/feasibility'}
 ],
 'completed_later_source_boundary': {'actual_filename_check': 'Specialized glob of own *v[4-9][0-9].md and *v[1-9][0-9][0-9].md returned ONLY v40; no completed post-v40 primary body found at this bounded filename check, and none was authored/delivered after the standing78 STOP. Review outputs are not primary successors.', 'unpublished_quarantined': 'ENTIRE post-v5 unpublished scouting branch and all consuming guidance ZERO; no new field serialization/repair/reconstruction of it. No completed later math silently added; future authorized math requires separate future manifest.'},
 'current_process_overlay_rule': 'Original M5 historical FIVE finding/active-primary wording is preserved immutable, not current authority. OX6/P78/FOUR142/CP136/POST153ACK/P121/P138/P157 supersede its process-state implication PROSPECTIVELY ONLY. ALL original v1-v40 sources remain individual author/parent-qualified statuses, not independently proven unaffected by time or hashes.',
 'current_pause': 'Original source/proof/rehearsal/method STOP78 unchanged. Only existing-byte/field metadata mapping authorized; no new mathematics, chosen controls, scientific execution/GO, stronger verification or early round closeout.',
 'full_gate_requirement': 'ONE complete current union: ALL individual claims AND ALL whole branch roots with EVERY operative antecedent/erratum/full source ending and all process qualifications. Every reviewer receives every expanded full body; two verdicts per claim (mathematics AND dependency/application/trust/noncircularity). Missing specialized proof NAMED_NOT_RECONSTRUCTED, never PASS by hash/headline/old verdict. This artifact is NOT a dispatched gate, parent adoption, proof read, rank/root calculation or source-provenance clearance.',
 'limits': 'Same18/exclusiveOWN/HOLD/N4UNKNOWNhistoricalexitunestablished/aux214STOP/originalOct27cutoff11:05:38/deadline12:35:38/substantive30min INCLUDINGblocked/noearlypark. ALL six primary/four142/two later own cadence findings and Main138 BOTH parent cadence findings remain. No scientific interpreter/Eval/CAS/calculator/program/arithmetic/control calculation/enumeration/solver/replay/CLI/nestedagent/newGO/withdrawn guide/novelty/formal-human-family-executable acceptance/global cognition-runtime-clean-provenance census.'
}
spr_union_meta_json = json.dumps(spr_union_meta, ensure_ascii=False, indent=2) + '\n'
print(json.dumps({'operation': 'BYTE_FIELD_ONLY_METADATA; no source-proof text interpreted', 'manifest_inputs': spr_union_meta['metadata_counts']['manifest_inputs'], 'distinct_source_process_statement_inputs': spr_union_meta['metadata_counts']['distinct_source_process_statement_inputs'], 'individual_claim_nodes': spr_union_meta['metadata_counts']['individual_claim_nodes'], 'whole_claim_field_roots': spr_union_meta['metadata_counts']['whole_claim_field_roots'], 'branch_root_count': len(spr_union_meta['whole_branch_roots']), 'metadata_pin_errors': spr_pin_errors, 'output_sha256': hashlib.sha256(spr_union_meta_json.encode()).hexdigest(), 'output_LF': spr_union_meta_json.count('\n'), 'output_bytes': len(spr_union_meta_json.encode()), 'writes': 'NONE in this cell'}, ensure_ascii=False, indent=2))
