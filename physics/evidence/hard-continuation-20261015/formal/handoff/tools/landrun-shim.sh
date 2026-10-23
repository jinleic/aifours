#!/bin/sh
# FAKE LANDRUN: macOS has no landrun. This shim drops the sandbox options and runs the
# command unsandboxed, so Comparator's sandbox guarantee does NOT hold on this machine.
echo "THIS IS NOT REAL LANDRUN (unsandboxed shim)" >&2
while [ $# -gt 0 ]; do
  case "$1" in
    --best-effort) shift ;;
    --rox|--ro|--rw|--rwx|--env|--rwo) shift 2 ;;
    *) break ;;
  esac
done
exec "$@"
