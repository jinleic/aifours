"""Read-only syntax check: creates no interpreter cache outside the workspace."""
from pathlib import Path
files=sorted(Path('code').glob('*.py'))
for path in files:
    compile(path.read_text(),str(path),'exec')
print('PASS in-memory syntax checks:',len(files),'Python files')
