import os,runpy,sys
def retain(*a,**k): raise RuntimeError("Replay forbids evidence deletion")
os.remove=retain;os.unlink=retain
sys.path.insert(0,os.path.dirname(sys.argv[1]))
sys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name="__main__")
