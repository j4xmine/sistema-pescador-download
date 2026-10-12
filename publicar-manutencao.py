"""Publica exclusivamente os binários já verificados, sem recompilar."""
import hashlib,json,os,subprocess,urllib.request
from pathlib import Path
from urllib.parse import urlparse
manifest=json.loads(Path('transferencia-manutencao.json').read_text())
assert manifest['tag']=='v1.1.2-rc.3'
expected={'SistemaPescador-Setup-1.1.2-rc.3.exe','SistemaPescador-Atualizacao-1.1.2-rc.3.exe','SHA256SUMS.txt','unified-manifest.json','MANUTENCAO-PESQBRASIL.md','sistema-pescador-backend-manutencao.jar','instalar-manutencao.py','backend-manifest.json','SHA256SUMS-backend.txt','MANUTENCAO-SERVIDOR.md'}
assets=manifest['assets'];assert len(assets)==len(expected) and {a['name'] for a in assets}==expected
out=Path('release-out');out.mkdir(exist_ok=True)
for a in assets:
    assert urlparse(a['url']).scheme=='https' and urlparse(a['url']).hostname=='release-assets.githubusercontent.com'
    assert len(a['sha256'])==64 and all(c in '0123456789abcdef' for c in a['sha256'])
    p=out/a['name']
    h=hashlib.sha256();n=0
    with urllib.request.urlopen(a['url'],timeout=60) as source,p.open('wb') as dest:
        while data:=source.read(1024*1024):h.update(data);n+=len(data);dest.write(data)
    assert n==a['size'] and h.hexdigest()==a['sha256'],a['name']
    print('VERIFICADO='+a['name'])
front=json.loads((out/'unified-manifest.json').read_text());back=json.loads((out/'backend-manifest.json').read_text())
assert back['version']=='1.1.2-rc.3-manutencao' and back['commit']==manifest['backendCommit']
assert front['version']=='1.1.2-rc.3' and front['backendUpdateRequired'] is True
assert front['frontendCommit']==manifest['frontendCommit'] and front['updateSequence']==6902
for filename in ['SHA256SUMS.txt','SHA256SUMS-backend.txt']:
    for line in (out/filename).read_text().splitlines():
        if not line.strip():continue
        digest,name=line.split(None,1);name=name.strip().lstrip('*')
        assert name in expected and hashlib.sha256((out/name).read_bytes()).hexdigest()==digest.lower()
setup=hashlib.sha256((out/'SistemaPescador-Setup-1.1.2-rc.3.exe').read_bytes()).hexdigest()
assert setup==hashlib.sha256((out/'SistemaPescador-Atualizacao-1.1.2-rc.3.exe').read_bytes()).hexdigest()
repo=os.environ['GITHUB_REPOSITORY'];tag=manifest['tag']
assert repo=='j4xmine/sistema-pescador-download'
# Draft somente passa a ser visível após upload e conferência de todos os assets.
releases=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases?per_page=100']))
existing=[r for r in releases if r['tag_name']==tag]
assert len(existing)<=1
if not existing:
    subprocess.run(['gh','release','create',tag,'--repo',repo,'--target',os.environ['GITHUB_SHA'],'--draft','--prerelease','--latest=false','--title','Marlin 1.1.2-rc.3 — perfis da entidade','--notes-file','NOTAS-MANUTENCAO.md',*[str(out/a) for a in sorted(expected)]],check=True)
    releases=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases?per_page=100']))
    existing=[r for r in releases if r['tag_name']==tag]
assert len(existing)==1
r=existing[0]
assert r['prerelease']
assert {a['name'] for a in r['assets']}==expected
for a in r['assets']:
    source=next(v for v in assets if v['name']==a['name']);assert a['digest']=='sha256:'+source['sha256'] and a['size']==source['size']
if r['draft']:
    subprocess.run(['gh','api',f"repos/{repo}/releases/{r['id']}",'--method','PATCH','--input','-'],input=json.dumps({'draft':False,'prerelease':True,'make_latest':'false'}).encode(),stdout=subprocess.DEVNULL,check=True)
print('RELEASE_PUBLICADA='+r['html_url'])
