#!/usr/bin/env python3
"""Bind a single exact star primal to independently checked extra cut scans.

This is receipt/evidence binding; the pinned exact branch verifiers and
source-family scanners perform the mathematical row checks separately.
"""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
E110=('frontier-20261028-full-source-lp-optimum-v1-erratum-1.md','c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9')
CORE=('frontier-20261028-crossbranch-threefamilies-combined-check-result.json','e9f004685bb2a7eee151d5803e347a954bdcb451eb2a9a41b05076d491145ddf')
L2A=('frontier-20261028-second-cross-cut-round3-scan-result.json','f1e18d8b08077d13e84a6b39792cc1ee705cfce8a52a2ef3d2737cb396a48ee5')
L2B=('frontier-20261028-second-cross-cut-round3-independent-result.json','bc08ec912010a3e28ba34014db188ee329c11c4a4ac8f5bfc333655dfbd46965')
L3E=('frontier-20261028-third-cross-cut-independent-label-erratum-v1.json','e6b01fe0362c99ad0a35dff4aea4a16bda7f0586a38144d1110c152913f7ed7a')
L3A=('frontier-20261028-third-cross-cut-scan-result.json','59d9cf7b33fdd972b4325667c286f60defad22ce1d80cc229a7a86ccfe56c600')
L3B=('frontier-20261028-third-cross-cut-independent-result.json','c11773bfc9e3106ace76b8553fd13d308875951848e9198f5d460f332665a76c')
P1=('frontier-20261028-fivevar-original-all-blocks-scan-result.json','ee7ba6ae9a27526ac7559780a2c054ef07c49c5695adbb5af898fe71f7181108')
P2=('frontier-20261028-fivevar-original-all-blocks-independent-result.json','f5d7da891b0dc6268e33fe71de98dacf24345d37b4426d526cdcd4247ee7800d')
PX1=('frontier-20261028-psi5-cross-copy-round3-scan-result.json','b5e5f2748a279d0b1e050a0270a605545ae248094f56ca9ff81f65e6179b27e5')
PX2=('frontier-20261028-psi5-cross-copy-round3-independent-result.json','ecad42eb005f40f2e08387627b82e786ccc99558ac76aea61288e88e05fba64a')
C1=('frontier-20261028-conditioned-five-variable-full-scan-result.json','f2bbd6793dd6c0772c6832f2463c56d7aa90e61218b4e26ad7aca20c377c85bb')
C2=('frontier-20261028-conditioned-five-variable-independent-result.json','77c7f21e5ed3759360bbde9ff03abe9fd4038397a408407604a15a2bf5e64acd')
OUT=ROOT/'frontier-20261028-threefamily-extended-binding-result.json'
BASE='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
C12='1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739'
C13='e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474'
PSI='def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392'


def pin(item,as_json=True):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw) if as_json else raw.decode('utf-8')


def validate(d):
    core=d['core'];l2a=d['l2a'];l2b=d['l2b'];l3a=d['l3a'];l3b=d['l3b'];p1=d['p1'];p2=d['p2'];px1=d['px1'];px2=d['px2'];c1=d['c1'];c2=d['c2']
    if core['base_sha256']!=BASE or core['cross12_candidate_sha256']!=C12 or core['cross13_candidate_sha256']!=C13 or core['primal_objective']!='1847/276':raise ValueError('CORE')
    row=l2a['scans'][1];r=l2b['new_point_exact_scan']
    if l2a['new_threefamilies_sha256']!=C13 or l2b['new_star_sha256']!=C13 or row['cuts_checked']!=272160 or row['negative_count'] or r['checked']!=272160 or r['negative_count'] or Fraction(row['minimum'])<0 or Fraction(r['minimum'])<0:raise ValueError('L2_SCAN')
    row=l3a['scans']['new_threefamily'];r=l3b['new_point_exact_scan']
    if l3a['new_star_sha256']!=C13 or l3b['new_star_sha256']!=C13 or row['checked']!=5443200 or row['negative_count'] or r['checked']!=5443200 or r['negative_count'] or Fraction(row['minimum_exact'])<0 or Fraction(r['minimum'])<0:raise ValueError('L3_SCAN')
    if p1['profile_sha256']!=BASE or p1['inequality_witness_sha256']!=PSI or p1['substitutions_checked']!=67609080 or p1['violations'] or Fraction(p1['minimum_exact_slack'])<0:raise ValueError('PSI_ORIG1')
    if p2['profile_sha256']!=BASE or p2['witness_sha256']!=PSI or p2['substitutions_checked']!=67609080 or p2['first_violation'] is not None or Fraction(p2['minimum_exact_slack'])<0:raise ValueError('PSI_ORIG2')
    for r in (px1,px2):
        if r['base_sha256']!=BASE or r['cross12_sha256']!=C12 or r['cross13_sha256']!=C13 or r['psi_sha256']!=PSI or r['substitutions_checked']!=7870500 or Fraction(r['minimum_exact_slack'])<0:raise ValueError('PSI_CROSS')
    if px1['violations'] or px2['first_violation'] is not None:raise ValueError('PSI_CROSS_VIOLATION')
    if c1['point_sha256']!=BASE or c1['substitutions_mod_AB_swap_checked']!=47534520 or c1['family1_exact_violation'] is not None or c1['family1_range_blocker'] is not None or c1['family2_exact_violation'] is not None:raise ValueError('SOURCE_2026_1')
    if c2['point_sha256']!=BASE or c2['disjoint_substitutions_mod_AB_swap']!=47534520 or c2['family1_minimum_over_all_finite_staircases_scaled']<0 or not c2['family2_both_AB_orders_all_positive_k_pass'] or c2['family2_min_twice_scaled']<0:raise ValueError('SOURCE_2026_2')


def main():
    # Binding source-order corrections are read before their affected receipts.
    f110err=pin(E110,False)
    if 'REQUIRED BEFORE SOURCE' not in f110err or 'Remark 5.4' not in f110err:raise ValueError('F110_ERRATUM')
    l3err=pin(L3E)
    if l3err['status']!='ADDITIVE REQUIRED BEFORE SOURCE' or l3err['receipt_sha256']!=L3B[1]:raise ValueError('L3_ERRATUM')
    d={'core':pin(CORE),'l2a':pin(L2A),'l2b':pin(L2B),'l3a':pin(L3A),'l3b':pin(L3B),
       'p1':pin(P1),'p2':pin(P2),'px1':pin(PX1),'px2':pin(PX2),'c1':pin(C1),'c2':pin(C2)}
    validate(d);controls={}
    def reject(tag,mut):
        x=deepcopy(d);mut(x)
        try:validate(x)
        except (ValueError,KeyError,TypeError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    reject('wrong_primal_hash',lambda x:x['core'].__setitem__('cross13_candidate_sha256','bad'))
    reject('missing_L3_coverage',lambda x:x['l3b']['new_point_exact_scan'].__setitem__('checked',1))
    reject('negative_Psi_slack',lambda x:x['p2'].__setitem__('minimum_exact_slack','-1'))
    reject('source_family_violation',lambda x:x['c2'].__setitem__('family2_both_AB_orders_all_positive_k_pass',False))
    out={'base_sha256':BASE,'cross12_sha256':C12,'cross13_sha256':C13,
         'f110_erratum_sha256':E110[1],'third_scan_label_erratum_sha256':L3E[1],
         'exact_primal_dual_core_receipt':CORE[1],'optimum':'1847/276','nonempty_LP_coordinates':30719,
         'first_gluing_instances':45360,'second_gluing_instances':272160,'third_gluing_instances':5443200,
         'Psi_original_disjoint_substitutions':67609080,'Psi_cross_complement_substitutions':7870500,
         'source_2026_disjoint_substitutions_mod_AB_swap':47534520,
         'F_n_disjoint_substitutions_mod_AB_swap':13729980,'all_parameters':'as specified by the pinned exact receipts',
         'minimum_slacks':{'L2':'0','L3':'1697/1725000','Psi_original':'0','Psi_cross':'0'},
         'mutation_controls':controls,'all_bound':True,
         'limits':'Exact no-improvement only for the stated star LP plus enumerated named cuts. Universal inequality/source theorem proofs require independent scientific review. Other substitutions, cross-branch Shannon and entropic realization remain open.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
