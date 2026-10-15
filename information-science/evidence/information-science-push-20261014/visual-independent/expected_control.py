"""Construct a small exact expected-count-only scheme for case 5, m=7."""
import itertools,json,time
from pathlib import Path
from verify import distribution

ROOT=Path(__file__).resolve().parent


def run():
    started=time.monotonic()
    leaf_pairs=[(1<<i)|(1<<j) for i,j in itertools.combinations(range(1,5),2)]
    white=[{'orbit':[0,0]+[1|p]*5,'probability':'1/10'} for p in leaf_pairs]
    white.extend([{'orbit':[0,0]+[31]*5,'probability':'1/10'},{'orbit':[0,0]+[30]*5,'probability':'3/10'}])
    black=[{'orbit':[0]+[1]*6,'probability':'1/4'},{'orbit':[0]+[31]*6,'probability':'1/4'},{'orbit':sorted(leaf_pairs+[31]),'probability':'1/2'}]
    witness={'white':white,'black':black}
    checked=distribution(5,7,witness,full=False)
    assert checked['full_security_violations']
    out={'case':5,'m':7,'verdict':'YES','model':'expected projected column counts; unchanged all-support contrast','method':'explicit rational 8-white/3-black orbit construction','witness':witness,'verification':checked,'simple_security_violation':{'forbidden':1,'event':'all seven entries of participant 1 are white','white_probability':'3/10','black_probability':'0'},'seconds':time.monotonic()-started}
    (ROOT/'expected_count_control.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='witness'}),flush=True)
    return out

if __name__=='__main__':run()
