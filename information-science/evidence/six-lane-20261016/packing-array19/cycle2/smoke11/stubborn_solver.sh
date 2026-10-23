#!/bin/sh
trap '' TERM
exec 3>"$2"
sleep 12
exit 0
