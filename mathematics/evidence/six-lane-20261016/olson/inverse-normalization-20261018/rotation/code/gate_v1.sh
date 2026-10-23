#!/bin/bash
# Usage: gate_v1.sh PROJECTED_BYTES cmd args...   Refuses to run cmd unless statvfs free >= 12.2e9 + PROJECTED_BYTES.
need=$((12200000000 + $1)); shift
free=$(python3 -B -c "import os; s=os.statvfs('.'); print(s.f_bavail*s.f_frsize)")
if [ "$free" -lt "$need" ]; then echo "GATE-FAIL free=$free need=$need $(date '+%H:%M:%S')"; exit 97; fi
echo "GATE-OK free=$free need=$need $(date '+%H:%M:%S')"
exec "$@"
