"""Replica a prévia validada, sem recompilar nem alterar o catálogo estável."""
import hashlib
import json
import os
import subprocess
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

VERSION = '1.1.3-rc.7'
TAG = 'v' + VERSION
EXPECTED = {f'SistemaPescador-Setup-{VERSION}.exe',
            f'SistemaPescador-Atualizacao-{VERSION}.exe',
            'SHA256SUMS.txt', 'unified-manifest.json', 'PESQBRASIL-AUTOMACAO.md'}
manifest = json.loads(Path('transferencia-pesqbrasil-previa.json').read_text())
assert manifest['source'] == 'j4xmine/sistema-pescador-frontend'
assert manifest['tag'] == TAG
assets = manifest['assets']
assert len(assets) == len(EXPECTED) and {a['name'] for a in assets} == EXPECTED
out = Path('preview-out')
out.mkdir(exist_ok=True)
for a in assets:
    url = urlparse(a['url'])
    assert url.scheme == 'https' and url.hostname == 'release-assets.githubusercontent.com'
    assert len(a['sha256']) == 64 and all(c in '0123456789abcdef' for c in a['sha256'])
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(a['url'], timeout=60) as source, (out / a['name']).open('wb') as dest:
        while data := source.read(1024 * 1024):
            digest.update(data)
            size += len(data)
            dest.write(data)
    assert size == a['size'] and digest.hexdigest() == a['sha256'], a['name']
    print('VERIFICADO=' + a['name'])
front = json.loads((out / 'unified-manifest.json').read_text(encoding='utf-8-sig'))
assert front['version'] == VERSION and front['updateSequence'] == 7007
assert front['frontendCommit'] == manifest['frontendCommit']
assert front['backendUpdateRequired'] is False
for line in (out / 'SHA256SUMS.txt').read_text().splitlines():
    if not line.strip():
        continue
    digest, name = line.split(None, 1)
    name = name.strip().lstrip('*')
    assert name in EXPECTED and hashlib.sha256((out / name).read_bytes()).hexdigest() == digest.lower()
assert (out / f'SistemaPescador-Setup-{VERSION}.exe').read_bytes() == (out / f'SistemaPescador-Atualizacao-{VERSION}.exe').read_bytes()
repo = os.environ['GITHUB_REPOSITORY']
assert repo == 'j4xmine/sistema-pescador-download'
def releases():
    return json.loads(subprocess.check_output(['gh', 'api', f'repos/{repo}/releases?per_page=100']))
existing = [r for r in releases() if r['tag_name'] == TAG]
assert len(existing) <= 1
if not existing:
    subprocess.run(['gh', 'release', 'create', TAG, '--repo', repo,
                    '--target', os.environ['GITHUB_SHA'], '--draft', '--prerelease', '--latest=false',
                    '--title', 'Marlin 1.1.3-rc.7 — teste da automação PesqBrasil',
                    '--notes-file', str(out / 'PESQBRASIL-AUTOMACAO.md'),
                    *[str(out / name) for name in sorted(EXPECTED)]], check=True)
    existing = [r for r in releases() if r['tag_name'] == TAG]
assert len(existing) == 1
release = existing[0]
assert release['prerelease'] and {a['name'] for a in release['assets']} == EXPECTED
for a in release['assets']:
    source = next(v for v in assets if v['name'] == a['name'])
    assert a['digest'] == 'sha256:' + source['sha256'] and a['size'] == source['size']
if release['draft']:
    subprocess.run(['gh', 'api', f"repos/{repo}/releases/{release['id']}", '--method', 'PATCH', '--input', '-'],
                   input=json.dumps({'draft': False, 'prerelease': True, 'make_latest': 'false'}).encode(),
                   stdout=subprocess.DEVNULL, check=True)
latest = json.loads(subprocess.check_output(['gh', 'api', f'repos/{repo}/releases/latest']))
assert latest['tag_name'] == 'v1.1.2'
print('PREVIA_PUBLICADA=' + release['html_url'])
