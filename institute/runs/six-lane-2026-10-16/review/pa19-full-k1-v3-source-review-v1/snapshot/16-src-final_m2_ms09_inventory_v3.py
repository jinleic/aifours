#!/usr/bin/env python3
"""Fail-closed ms09 component inventory; measured-v2 transport only for final counted inputs.
--verify-formulas is mandatory for FINAL. All14 historical/calibration inputs require new measured validation;
the withdrawn parent-reuse CLI has been removed, and old originals remain immutable and separately classified.
This is NOT a global M1/M2/PA19 verdict; the final independent parent reader is separate.
"""
import argparse
import json
import time

import m2_ms09_contract_v3 as C
import m2_supervised_runtime_v3 as R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('contract')
    ap.add_argument('sha256')
    ap.add_argument('--verify-formulas',action='store_true')
    args = ap.parse_args()
    c = C.load(args.contract,args.sha256)
    out = C.inventory(c,args.sha256,args.verify_formulas)
    out.update(host_clock=time.strftime('%Y-%m-%dT%H:%M:%S%z'),production_contract_sha256=args.sha256,
               schema='PA19-MS09-FINAL-INVENTORY-v3')
    dest = C.LANE/'cycle2'/('m2-ms09-inventory-%s-%d.json' % (time.strftime('%Y%m%dT%H%M%S'),time.time_ns()))
    h = C.publish_json(dest,out,C.LANE/'scratch'/'m2k1-publish'/('inventory-'+str(time.time_ns())))
    print(dest)
    print('sha256',h)
    print(json.dumps({k:v for k,v in out.items() if k != 'rows'},indent=1))


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        main()
