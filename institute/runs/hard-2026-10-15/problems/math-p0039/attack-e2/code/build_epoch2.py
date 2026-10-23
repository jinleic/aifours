#!/usr/bin/env python3
"""Build production-only executables; never used by claim replay commands.

The 128-bit variant is explicitly derived from the inherited scan.c. It adds
ordinary residues and a digest of every decision; its arithmetic is unchanged.
scan32.c is separately implemented and includes none of scan.c.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    s = Path('code/scan.c').read_text()
    s = s.replace('#include <assert.h>', '#include <assert.h>\n#include <CommonCrypto/CommonDigest.h>')
    s = s.replace('static inline u128 power_two(u64 n, bool full_residue) {\n    u128 p = (u128)n * n + n + 1, inv = 1;',
                  'static inline u128 generic_power(u64 e, u128 p, bool full_residue) {\n    u128 inv = 1;')
    s = s.replace('    u64 e = n + 1;\n', '')
    at = '\nstatic u64 pow_small('
    assert at in s
    s = s.replace(at, '\nstatic inline u128 power_two(u64 n, bool full_residue) { return generic_power(n+1,(u128)n*n+n+1,full_residue); }\n'+at)
    helper = '''
static void hash_record(CC_SHA256_CTX *h,u64 n,u32 q,u128 residue) {
    unsigned char b[32]; u32 tag=q?1:(residue==1?3:2);
    for(int i=0;i<8;i++){b[i]=(unsigned char)n;n>>=8;}
    for(int i=0;i<4;i++){b[8+i]=(unsigned char)q;q>>=8;b[12+i]=(unsigned char)tag;tag>>=8;}
    for(int i=0;i<16;i++){b[16+i]=(unsigned char)residue;residue>>=8;}
    CC_SHA256_Update(h,b,32);
}
'''
    s = s.replace('static void *worker(void *unused) {',helper+'\nstatic void *worker(void *unused) {')
    s = s.replace('        u64 sieved = 0, tested = 0, hits = 0;',
                  '        CC_SHA256_CTX hctx; CC_SHA256_Init(&hctx);\n        u64 sieved = 0, tested = 0, hits = 0;')
    s = s.replace('residue = power_two(n, audit);','residue = power_two(n, true);')
    s = s.replace('            if (audit || hit) audit_record',
                  '            hash_record(&hctx,n,(u32)q,q?0:residue);\n            if (audit || hit) audit_record')
    s = s.replace('        if (sieved + tested != len) fail("coverage count mismatch");',
                  '        if (sieved + tested != len) fail("coverage count mismatch");\n        unsigned char raw_digest[32]; char digest_hex[65];\n        CC_SHA256_Final(raw_digest,&hctx);\n        for(int v=0;v<32;v++)sprintf(digest_hex+2*v,"%02x",raw_digest[v]);\n        digest_hex[64]=0;')
    old = r'",\"seconds\":%.6f,\"survivors\":["'
    new = r'",\"decision_sha256\":\"%s\",\"seconds\":%.6f,\"survivors\":["'
    assert old in s
    s = s.replace(old,new)
    s = s.replace('len, sieved, tested, hits, now() - t0);','len, sieved, tested, hits, digest_hex, now() - t0);')
    s = s.replace('    if (argc != 12)', '''    if(argc==5 && !strcmp(argv[1],"power")) {
        u64 e=parse_u64(argv[2]);u128 p=0;
        for(const char*t=argv[3];*t;t++){if(*t<'0'||*t>'9')fail("modulus");p=p*10+*t-'0';}
        if(!e||p<3||!(p&1)||p>=((u128)1<<127))fail("power bounds");
        char out[48];printf("%s\\n",dec128(generic_power(e,p,true),out));return 0;
    }
    if (argc != 13)''')
    old = r'",\"window_len\":%" PRIu64 "}\n",'
    new = r'",\"window_len\":%" PRIu64 ",\"binary_sha256\":\"%s\",\"backend\":\"radix64-two-limb-cuberoot\",\"digest_protocol\":\"le64-n-le32-factor-le32-tag-le128-residue; factor residue zero=uncomputed\"}\n",'
    assert old in s
    s=s.replace(old,new)
    s=s.replace('threads, cap, window_every, window_len);','threads, cap, window_every, window_len, argv[12]);')
    Path('code/scan128_digest.c').write_text(s)
    Path('.tmp').mkdir(exist_ok=True)
    env=dict(os.environ,TMPDIR=str(Path('.tmp').resolve()))
    records=[]
    for stem in ('scan128_digest','scan32'):
        command=['clang','-O3','-mcpu=native','-std=c11','-Wall','-Wextra',
                 '-Wno-deprecated-declarations','-pthread','code/'+stem+'.c','-o','code/'+stem]
        result=subprocess.run(command,env=env,capture_output=True,text=True,check=True)
        records.append(dict(command=command,source_sha256=sha('code/'+stem+'.c'),
                            binary_sha256=sha('code/'+stem),stdout=result.stdout,stderr=result.stderr))
    Path('evidence/epoch2/build.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(records,indent=2))


if __name__=='__main__':main()
