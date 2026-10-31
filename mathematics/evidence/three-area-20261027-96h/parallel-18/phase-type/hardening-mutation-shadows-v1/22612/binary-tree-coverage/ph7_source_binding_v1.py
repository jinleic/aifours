"""Fixed source-order/pin binding for the prospective PH7 global checker."""
from pathlib import Path

class SourceBindingError(Exception): pass

def require(condition, code, detail=''):
    if not condition: raise SourceBindingError(f'{code}: {detail}')

def expected_sources(owner_root, run_root):
    owner=Path(owner_root); run=Path(run_root)
    return [
      ('parent_closed_endpoint_erratum', run/'dispositions/math-1-ph7-supremum-bracket-closed-endpoint-erratum-v1.json','a1589a464fccc010cf2ad13cd61c430e9a6032cb80407019b2d38edbc603ce97'),
      ('owner_closed_endpoint_erratum', owner/'frontier-20261029-ph7-closed-endpoint-and-f50-erratum-v1.md','a1cfbd816d04e03655b7461850e95df91e13b0e6fb081801f306bc1b4a719d8c'),
      ('owner_f159_f160_minor_overlay', owner/'frontier-20261029-ph7-f159-f160-minor-fixes-addendum-v1.md','a447c10752b9c876b8eaa9754ce5246bda11e40778f26bf98fa5c4fd345ac4d1'),
      ('f50_erratum', owner/'frontier-20261028-ph7-two-cycle-endpoint-v4-erratum-v1.md','b5526a1556a61786c5cc382e924087a318b31b6640b35d30a41fe9d3fe22cc30'),
      ('f50_manuscript', owner/'frontier-20261028-ph7-two-cycle-endpoint-v4.md','4f63347198b12ce6dfefb5c7c94adf95fcc262234d29ce055e6f789bff27e191'),
      ('f50_root_certificate', owner/'frontier-20261028-ph7-two-cycle-interval-certificate.json','2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88'),
      ('f50_disposition', run/'dispositions/math-1-ph7-algebraic-endpoint-closed-band-parent-v1.md','307b3823d9af55a171fa911373ae96cd9df22a019b3f4f65fa94d70e9de5cbeb'),
      ('caller_disposition', run/'dispositions/math-1-ph7-global-irreducibility-eight-edges-parent-v1.md','42ae3d996ffb7f46cc5ad72a0d18f3eae665290f8d7901e994ac7776a6b4d281'),
      ('f159_f160_disposition', run/'dispositions/math-1-ph7-no-seven-states-at-eight-ninths-and-above-0p85-parent-v1.md','4997bb2e2572190a378e843d2504629cd5e9254d0c5e3ae68ee24703792e08ec'),
      ('f180_disposition', run/'dispositions/math-1-ph7-no-seven-states-above-83over100-parent-v1.md','7935d4f5ce796c9efd4a7c015066f03120a0ae8cec89d62e9231197f3da64b3a'),
      ('f203_parent_no_go', run/'review-waves/f203-ph7-local-to-global-schur-bridge-robustness-review/parent-no-go-and-caller-availability-v1.json','f0afb377ad352ef05a4a9249e8762eadd2737152ee0000348924350f45bd3108'),
      ('f203_review_disclosed_context', run/'review-waves/f203-ph7-local-to-global-schur-bridge-robustness-review/review-v1.md','bb0ede9cdfc46866dc3cda04a97411e13a618c77118095f56e59bfd67f023b1f'),
      ('caller_and_face_addendum', owner/'frontier-20261029-ph7-global-caller-face-obligations-addendum-v1.md','e9fdf9f05350032281c7e885adc537b52328520bf9a59384e8cf79eeede82d90'),
      ('joint_lemma', owner/'frontier-20261029-ph7-joint-interlacing-y1-v1.md','0221e6c73440f921f127db0130038f8ab733fae65d5585f4227ba06b9fef8310'),
      ('candidate', owner/'frontier-20261029-ph7-local-to-global-supremum-candidate-v1.md','b2b7770d8b024782c5d0c1cfbd8f6e01368892801d1f3882e7b3279b59059ca5'),
      ('local_source', owner/'frontier-20261029-ph7-local-global-dual-check.py','cb2b9ede94c117ea44b6c100ee7dbfa4cb46d38531aea9de1bd3582892e085d8'),
      ('local_engine', owner/'frontier-20261029-ph7-v4-local-spectral-optimality-check.py','6eed9b486726dcb79a8ad8d57c4106aa312c354df7cc7989c5887dd7a121813b'),
      ('local_certificate', owner/'frontier-20261029-ph7-local-global-local-certificate-v1.json','8f5f9b85b1211c36114500fc61c1a35b23646e9e1cb65e6697fd0663d1b15fce'),
    ]

def verify_manifest(manifest, expected, read_pinned, guard):
    require(isinstance(manifest,dict) and set(manifest)=={'schema_version','kind','sources'}, 'SOURCE_MANIFEST_SCHEMA')
    require(manifest['schema_version']==1 and manifest['kind']=='PH7_ORDERED_SOURCE_MANIFEST_V1', 'SOURCE_MANIFEST_VERSION')
    sources=manifest['sources']; require(isinstance(sources,list) and len(sources)==len(expected), 'SOURCE_MANIFEST_COUNT')
    out={}; seen=set()
    for record,(role,path,sha) in zip(sources,expected):
        guard()
        require(isinstance(record,dict) and set(record)=={'role','path','sha256'}, 'SOURCE_ENTRY_SCHEMA')
        require(record=={'role':role,'path':str(path),'sha256':sha}, 'SOURCE_ORDER_OR_PIN_MISMATCH',role)
        require(str(path) not in seen, 'SOURCE_DUPLICATE_PATH',str(path));seen.add(str(path))
        out[role]=read_pinned(path,sha,16*1024*1024)
    return out
