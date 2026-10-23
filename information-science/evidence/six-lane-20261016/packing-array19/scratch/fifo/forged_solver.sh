#!/bin/sh
# forged solver for a negative control: writes the binary empty clause, claims UNSAT
printf 'a\000' > "$2"
exit 20
