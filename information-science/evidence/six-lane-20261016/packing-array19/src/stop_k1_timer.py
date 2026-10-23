#!/usr/bin/env python3
"""Parent-approved end-of-day admission stop: at 17:20:00 PDT create cycle2/STOP-K1 (creation-only), a registry
RESOURCE_STOP that refuses every NEW v6 admission; in-flight items (worst case ~34 min) end by ~17:55.
Lane-local sleeping process, not cron/launchd. Never deletes; refuses if the marker already exists.
"""
import datetime
import json
import os
import time
from pathlib import Path

L = Path(__file__).resolve().parent.parent
TARGET = datetime.datetime.fromisoformat('2026-10-18T17:20:00-07:00').timestamp()


def main():
    while True:
        remaining = TARGET-time.time()
        if remaining <= 0: break
        time.sleep(min(remaining,30))
    marker = L/'cycle2/STOP-K1'
    note = {'created_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'reason':'parent end-of-day rule: no new v6 admissions after 17:20; native work ends <=17:55',
            'class':'resource-stop (registry)','pid':os.getpid()}
    fd = os.open(marker,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o644)
    try: os.write(fd,(json.dumps(note)+'\n').encode())
    finally: os.close(fd)
    print('STOP-K1 created',note['created_host_clock'],flush=True)


if __name__ == '__main__':
    main()
