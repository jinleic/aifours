# Erratum v1 to b63-reduction-v1.md (timestamp deviation)

Recorded after host clock 2026-10-19T17:49:54-0700 by ContinuePA19d.

b63-reduction-v1.md (SHA256 6be58b9a82078ac9ed8df4fa4dc80d86ea91038b65885416087b05ef3a5c2aa9, 6835 bytes) states in its first line "Written after host clock 2026-10-19T18:03:00-0700". That value was NOT read from /bin/date; it was an unverified estimate written by the author, in violation of the read-/bin/date-before-every-timestamp rule. Observed facts: the last /bin/date reading before creation was 2026-10-19T17:43:22-0700 (checkpoint-002); the file modification time is 2026-10-19T17:49:11-0700; the next /bin/date reading was 2026-10-19T17:49:43-0700. Read the header as "written between 17:43:22 and 17:49:11 PDT". No mathematical content, hash or other file changes; the original bytes remain immutable. Process deviation retained.
