"""Frozen runtime-package inventory checks; no scientific computation."""
import os
from pathlib import Path

class EnvironmentErrorGate(Exception): pass

def require(condition, code, detail=''):
    if not condition: raise EnvironmentErrorGate(f'{code}: {detail}')

def verify_manifest(root, manifest, read_pinned, guard):
    root=Path(root).resolve(strict=True)
    require(isinstance(manifest,dict) and set(manifest)=={'schema_version','kind','packages','files'}, 'ENV_MANIFEST_SCHEMA')
    require(type(manifest['schema_version']) is int and manifest['schema_version']==1 and manifest['kind']=='PH7_PYTHON_PACKAGE_INVENTORY_V1', 'ENV_MANIFEST_VERSION')
    packages=manifest['packages']; require(packages==['mpmath','sympy'], 'ENV_PACKAGE_SET')
    files=manifest['files']; require(isinstance(files,list) and 0<len(files)<=30000, 'ENV_FILE_COUNT')
    expected={}
    for item in files:
        require(isinstance(item,dict) and set(item)=={'path','sha256'}, 'ENV_FILE_SCHEMA')
        rel=item['path']; sha=item['sha256']
        require(isinstance(rel,str) and rel and not rel.startswith('/') and '\\' not in rel, 'ENV_RELATIVE_PATH')
        parts=rel.split('/')
        require(all(p and p not in ('.','..') for p in parts) and parts[0] in packages, 'ENV_RELATIVE_PATH', rel)
        require(rel not in expected, 'ENV_DUPLICATE_PATH', rel)
        require(isinstance(sha,str) and len(sha)==64 and all(c in '0123456789abcdef' for c in sha), 'ENV_INVALID_SHA', rel)
        expected[rel]=sha
    for package in packages:
        require(package+'/__init__.py' in expected, 'ENV_PACKAGE_INIT_MISSING', package)
    seen=set()
    for package in packages:
        p=root/package
        require(p.is_dir() and not p.is_symlink(), 'ENV_PACKAGE_MISSING_OR_SYMLINK', package)
        for current, dirs, names in os.walk(p, topdown=True, followlinks=False):
            guard(); dirs.sort(); names.sort()
            for d in dirs: require(not (Path(current)/d).is_symlink(), 'ENV_SYMLINK', str(Path(current)/d))
            for name in names:
                path=Path(current)/name
                require(not path.is_symlink() and path.is_file(), 'ENV_NONREGULAR_OR_SYMLINK', str(path))
                rel=path.relative_to(root).as_posix()
                require(rel in expected, 'ENV_UNLISTED_FILE', rel)
                seen.add(rel)
    require(True, 'ENV_INVENTORY_MISSING', '')
    for rel, sha in sorted(expected.items()):
        guard(); read_pinned(root/rel,sha,16*1024*1024)
    return {'packages':packages,'file_count':len(expected),'files_verified':True,
            'limitation':'Pre/post hashes bind observed bytes, not an OS-enforced immutable mount; freeze the dependency tree read-only for the admission window.'}
