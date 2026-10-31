#!/usr/bin/env python3
"""Measured local FIFO replay of pinned ASCII DRUP via binary conversion.

This is owner-local evidence, not a parent replay or review. All byte feeds,
EOFs, child ownership, final empty clause, output and controls are recorded.
"""
import argparse,datetime,fcntl,hashlib,json,os,pathlib,re,resource,shutil,signal,struct,subprocess,termios,threading,time
H=pathlib.Path(__file__).parent
CNF='frontier-20261028-q2-nonmax35-symmetry-v1.cnf';CSHA='b62e5ce8c2cd6e15567315fcf9dc0f172af19cfbd90d4f13c472168df8e2b47c'
PROOF='frontier-20261028-q2-nonmax35-symmetry-proof-v1.drup';PSHA='cd1b58bd32c5aa2affbaeaf9be692fc43710261c12899fa18b8cd0be529f8ee4'
CHECKER='/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/drat-trim';DSHA='a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
FLOOR=2*1024**3

def sha(b):return hashlib.sha256(b).hexdigest()
def pinned(path,pin):
 b=pathlib.Path(path).read_bytes()
 if sha(b)!=pin:raise ValueError('input hash '+str(path))
 return b

def parse_ascii(data,maxvar):
 if not data.endswith(b'\n'):raise ValueError('unterminated ASCII proof')
 out=[]
 for line in data.decode('ascii').splitlines():
  v=line.split()
  if not v:raise ValueError('blank proof line')
  d=v[0]=='d';v=v[1:] if d else v
  z=[int(q) for q in v]
  if not z or z[-1]!=0 or 0 in z[:-1] or any(abs(q)>maxvar for q in z[:-1]):raise ValueError('bad ASCII proof')
  out.append((d,tuple(z[:-1])))
 if not out or out[-1]!=(False,()):raise ValueError('final empty absent')
 return out

def encode(steps):
 out=bytearray()
 for deletion,clause in steps:
  out.append(ord('d') if deletion else ord('a'))
  for lit in (*clause,0):
   v=(abs(lit)<<1)|(lit<0)
   while v>127:out.append(128+(v&127));v>>=7
   out.append(v)
 return bytes(out)

def decode(data):
 out=[];i=0
 while i<len(data):
  kind=data[i];i+=1
  if kind not in (ord('a'),ord('d')):raise ValueError('binary marker')
  clause=[]
  while True:
   v=0;shift=0
   while True:
    if i>=len(data):raise ValueError('truncated varint')
    z=data[i];i+=1;v|=(z&127)<<shift;shift+=7
    if z<128:break
    if shift>35:raise ValueError('oversize varint')
   if v==0:break
   if v==1:raise ValueError('negative zero')
   lit=v>>1;clause.append(-lit if v&1 else lit)
  out.append((kind==ord('d'),tuple(clause)))
 return out

def feed(fd,data,state,stop):
 state.update({'bytes':0,'sha256':None,'error':None,'closed':False})
 h=hashlib.sha256()
 try:
  os.set_blocking(fd,False)
  while state['bytes']<len(data) and not stop.is_set():
   try:
    p=state['bytes'];n=os.write(fd,data[p:min(p+65536,len(data))])
    if n<=0:raise OSError('zero write')
    h.update(data[p:p+n]);state['bytes']+=n
   except BlockingIOError:time.sleep(.002)
  if state['bytes']!=len(data):state['error']='feed_interrupted'
 except BaseException as e:state['error']=repr(e)
 finally:
  state['sha256']=h.hexdigest()
  try:os.close(fd);state['closed']=True
  except BaseException as e:state['error']=state['error'] or repr(e)

def run(tag,cnf,proof,cnf_bound,proof_bound):
 fifo=H/('frontier-20261028-q2-sym35-measured-'+tag+'-v1.fifo')
 if fifo.exists():raise ValueError('FIFO already exists '+str(fifo))
 os.mkfifo(fifo,0o600);dummy=os.open(fifo,os.O_RDONLY|os.O_NONBLOCK)
 # Retain a writer until all supplied CNF bytes have been observed drained;
 # otherwise a tiny feed can close before the checker opens its read side.
 held=os.open(fifo,os.O_WRONLY|os.O_NONBLOCK)
 stop=threading.Event();cs={};ps={};child=None;threads=[];pending=set();reason=None;sent=None;held_closed_after_drain=False
 stamp=datetime.datetime.now().astimezone().isoformat();started=time.monotonic()
 try:
  if shutil.disk_usage(H).free<FLOOR or sha(pathlib.Path(CHECKER).read_bytes())!=DSHA:raise ValueError('pre-spawn gate')
  child=subprocess.Popen([CHECKER,str(fifo),'-i','-U','-p','-W','-t','30'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
  pid=child.pid
  cfd=os.open(fifo,os.O_WRONLY|os.O_NONBLOCK);pending.add(cfd)
  pfd=os.dup(child.stdin.fileno());pending.add(pfd);child.stdin.close()
  for fd,payload,state in ((cfd,cnf,cs),(pfd,proof,ps)):
   th=threading.Thread(target=feed,args=(fd,payload,state,stop))
   th.start();pending.remove(fd);threads.append(th)
  while child.poll() is None:
   if held is not None and cs.get('closed') and cs.get('bytes')==len(cnf):
    available=struct.unpack('I',fcntl.ioctl(dummy,termios.FIONREAD,struct.pack('I',0)))[0]
    if available==0:os.close(held);held=None;held_closed_after_drain=True
   if time.monotonic()-started>35:reason='wall_limit';break
   if shutil.disk_usage(H).free<FLOOR:reason='disk_floor';break
   time.sleep(.01)
  if reason is not None and child.poll() is None:
   try:os.killpg(child.pid,signal.SIGTERM);sent='SIGTERM'
   except ProcessLookupError:sent='already_exited'
  # Retain ownership; no SIGKILL or subprocess timeout is used.
  if reason is not None:stop.set()
  child.wait();rc=child.returncode;stop.set()
  for th in threads:th.join(5)
  if any(th.is_alive() for th in threads):raise RuntimeError('feed thread unsettled')
  stdout=child.stdout.read().decode('utf-8','replace');stderr=child.stderr.read().decode('utf-8','replace');child.stdout.close();child.stderr.close();child=None
  remaining=struct.unpack('I',fcntl.ioctl(dummy,termios.FIONREAD,struct.pack('I',0)))[0]
 finally:
  if held is not None:os.close(held);held=None
  stop.set()
  for fd in pending:
   try:os.close(fd)
   except OSError:pass
  if child is not None:
   if child.poll() is None:
    try:os.killpg(child.pid,signal.SIGTERM)
    except ProcessLookupError:pass
   child.wait()
  for th in threads:
   if th.is_alive():th.join(5)
  os.close(dummy)
 if sha(pathlib.Path(CHECKER).read_bytes())!=DSHA:raise ValueError('post-checker hash')
 out_lines=[clean for line in stdout.split('\n') if (clean:=line.replace('\r','')).startswith('s ')]
 count=re.search(r'finished parsing, read (\d+) bytes from proof file',stdout)
 hdr=re.search(r'parsing input formula with (\d+) variables and (\d+) clauses',stdout)
 header=cnf_bound.decode('ascii').splitlines()[0].split()
 if len(header)!=4 or header[:2]!=['p','cnf']:raise ValueError('bound formula header')
 observed_count=int(count.group(1)) if count else None
 transport=(cs.get('bytes')==len(cnf_bound) and cs.get('sha256')==sha(cnf_bound) and cs.get('closed') and not cs.get('error') and remaining==0 and
            ps.get('bytes')==len(proof_bound) and ps.get('sha256')==sha(proof_bound) and ps.get('closed') and not ps.get('error') and observed_count==len(proof_bound))
 clean=(rc==0 and out_lines==['s VERIFIED'] and not stderr and reason is None and hdr is not None and
        (int(hdr.group(1)),int(hdr.group(2)))==(int(header[2]),int(header[3])) and
        not any(z in stdout for z in ('WARNING','TIMEOUT','NOT VERIFIED','early EOF','clauses less than expected','formula contains empty clause')))
 out={'tag':tag,'start':stamp,'end':datetime.datetime.now().astimezone().isoformat(),'pid':pid,'returncode':rc,
         'held_writer_closed_after_observed_drain_while_child_running':held_closed_after_drain,
         'stop_reason':reason,'signal':sent,'cnf_feed':cs,'proof_feed':ps,'cnf_fifo_remaining_bytes':remaining,
         'checker_reported_proof_bytes':observed_count,'checker_stdout':stdout,'checker_stderr':stderr,
         'status_lines':out_lines,'bound_formula_sha256':sha(cnf_bound),'bound_formula_bytes':len(cnf_bound),
         'bound_binary_proof_sha256':sha(proof_bound),'bound_binary_proof_bytes':len(proof_bound),
         'transport_exact':bool(transport),'checker_clean_verified':bool(clean),'strict_pass':bool(transport and clean),
         'wall_seconds':time.monotonic()-started,'fifo_retained':str(fifo)}
 record=H/('frontier-20261028-q2-sym35-measured-'+tag+'-v1-receipt.json')
 with record.open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 cnf=pinned(H/CNF,CSHA);ascii_proof=pinned(H/PROOF,PSHA);pinned(CHECKER,DSHA)
 steps=parse_ascii(ascii_proof,13440);binary=encode(steps)
 if decode(binary)!=steps:raise ValueError('ASCII/binary proof roundtrip mismatch')
 pc=b'p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n';pp=encode([(False,(2,)),(False,())])
 nc=b'p cnf 1 1\n1 0\n';np=encode([(False,())])
 ctl_good=run('control-positive',pc,pp,pc,pp)
 if not ctl_good['strict_pass']:raise ValueError('positive control failed')
 ctl_bad=run('control-sat-empty',nc,np,nc,np)
 if ctl_bad['returncode']!=1 or ctl_bad['status_lines']!=['s NOT VERIFIED'] or not ctl_bad['transport_exact']:raise ValueError('SAT negative control not rejected')
 ctl_wrong=run('control-wrong-formula',b'p cnf 2 1\n1 0\n',pp,b'p cnf 2 1\n1 0\n',pp)
 if ctl_wrong['strict_pass'] or ctl_wrong['status_lines']!=['s NOT VERIFIED']:raise ValueError('wrong formula control')
 ctl_trunc_cnf=run('control-truncated-cnf',pc[:-7],pp,pc,pp)
 if ctl_trunc_cnf['strict_pass'] or ctl_trunc_cnf['transport_exact']:raise ValueError('truncated CNF not rejected')
 ctl_trunc_proof=run('control-truncated-proof',pc,pp[:-2],pc,pp)
 if ctl_trunc_proof['strict_pass'] or ctl_trunc_proof['transport_exact']:raise ValueError('truncated proof not rejected')
 actual=run('actual',cnf,binary,cnf,binary)
 after={'cnf_sha256':sha((H/CNF).read_bytes()),'ascii_proof_sha256':sha((H/PROOF).read_bytes()),'checker_sha256':sha(pathlib.Path(CHECKER).read_bytes())}
 if after!={'cnf_sha256':CSHA,'ascii_proof_sha256':PSHA,'checker_sha256':DSHA}:raise ValueError('post-input hash')
 report={'result':'OWNER_LOCAL_MEASURED_FIFO_PASS' if actual['strict_pass'] else 'OWNER_LOCAL_MEASURED_FIFO_NOT_PASS',
         'source_sha256':sha(pathlib.Path(__file__).read_bytes()),'cnf_sha256':CSHA,'ascii_proof_sha256':PSHA,'checker_sha256':DSHA,
         'ascii_steps':len(steps),'binary_proof_sha256':sha(binary),'binary_proof_bytes':len(binary),
         'ascii_binary_roundtrip':'PASS','final_ascii_step':'empty clause',
         'controls':{'positive':ctl_good,'sat_empty':ctl_bad,'wrong_formula':ctl_wrong,'truncated_cnf':ctl_trunc_cnf,'truncated_proof':ctl_trunc_proof},
         'actual':actual,'after_hashes':after,'elapsed_seconds':time.monotonic()-start,
         'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'limits':'Owner-local replay, not parent-independent replay or proof of physical-to-CNF reduction. FIFO nodes deliberately retained.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ('controls','actual')},indent=2))
 print('actual_summary',actual['returncode'],actual['status_lines'],actual['transport_exact'],actual['checker_clean_verified'],actual['checker_reported_proof_bytes'],actual['cnf_fifo_remaining_bytes'])
if __name__=='__main__':main()
