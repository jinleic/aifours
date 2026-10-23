# ERRATUM to binding-result.json (2026-10-17T15:44:09-07:00, host clock)

binding-result.json (sha256 25aea392…243b) is superseded by binding-result.v2.json. Two assembly errors, no change to
any verdict, count or hash:
1. the `controls` section was built but omitted from the written receipt; v2 contains it;
2. `commands[0]`/`commands[1]` named the guard logs ../K5.log and ../K4.log; the actual logs are K5.bind.log and K4.bind.log.
All other fields of v2 are identical to binding-result.json. Files are written once (mode x), hence a new file.
