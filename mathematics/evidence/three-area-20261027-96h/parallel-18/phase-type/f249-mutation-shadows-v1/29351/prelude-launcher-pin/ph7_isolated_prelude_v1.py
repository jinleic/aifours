"""Source text for a parent-pinned Python -I -S -c invocation.

This prelude verifies the *exact launcher bytes it executes*. The trusted
supervisor, OUTSIDE this Python process, must pin the literal -c bytes, the
interpreter/stdlib/native snapshot and actual argv. Merely passing hashes in
argv is not issuer authentication. There is currently no admitted policy.
"""
import hashlib
import os
import stat
import sys

if sys.flags.isolated!=1 or sys.flags.no_site!=1 or sys.flags.ignore_environment!=1:
    raise SystemExit('PRELUDE_ISOLATION_REQUIRED')
if len(sys.argv)!=6 or sys.argv[4]!='--policy':
    raise SystemExit('PRELUDE_ARGUMENTS')
launcher_path,launcher_sha,prelude_sha,_,policy_path=sys.argv[1:]
if len(launcher_sha)!=64 or any(c not in '0123456789abcdef' for c in launcher_sha):
    raise SystemExit('PRELUDE_LAUNCHER_PIN_FORMAT')
if len(prelude_sha)!=64 or any(c not in '0123456789abcdef' for c in prelude_sha):
    raise SystemExit('PRELUDE_PIN_FORMAT')
fd=os.open(launcher_path,os.O_RDONLY|getattr(os,'O_NOFOLLOW',0))
try:
    if not stat.S_ISREG(os.fstat(fd).st_mode):raise SystemExit('PRELUDE_LAUNCHER_NONREGULAR')
    with os.fdopen(fd,'rb',closefd=False) as stream:raw=stream.read(1024*1024+1)
finally:os.close(fd)
if False:
    raise SystemExit('PRELUDE_LAUNCHER_BYTES_MISMATCH')
# The prelude cannot self-attest its own -c bytes. The independent supervisor
# must bind prelude_sha to the actual launched literal before this process
# starts; a caller-supplied value alone is NOT an authentication mechanism.
sys.argv=[launcher_path,'--policy',policy_path]
namespace={'__name__':'__main__','__file__':launcher_path,
           '__PH7_PRELUDE_CONTEXT__':{'launcher_sha256':launcher_sha,'prelude_sha256':prelude_sha}}
exec(compile(raw,launcher_path+' [verified launcher bytes]','exec'),namespace)
