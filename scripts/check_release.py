#!/usr/bin/env python3
"""Check public-package boundaries, recipe IDs, and local documentation links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {
    'README.md', 'START_HERE.md', 'COMMANDS.md', 'AGENTS.md', 'SKILL.md',
    'RECIPES.md', 'LICENSE', 'NOTICE.md', 'CONTRIBUTING.md', 'SECURITY.md',
    'CHANGELOG.md', '.gitignore',
}
PUBLIC_DIRS = {'adapters', 'docs', 'templates', 'recipes', 'examples', 'scripts', 'tests', '.github'}
SKIP_DIRS = {'.git', '__pycache__', '.pytest_cache', '.venv'}
PRIVATE_NAMES = {'USER.md', 'MEMORY.md', 'SOUL.md', 'IDENTITY.md', 'DREAMS.md'}


def visible_text(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def anchors(text):
    text = visible_text(text)
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        heading = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading)
        base = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        n = counts.get(base, 0)
        result.add(base if n == 0 else f'{base}-{n}')
        counts[base] = n + 1
    return result


def check():
    errors = []
    files = []
    for path in ROOT.rglob('*'):
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts) or path.name == '.DS_Store':
            continue
        if path.is_symlink():
            errors.append(f'{relative}: symlinks are excluded from the public package')
            continue
        if not path.is_file():
            continue
        files.append(path)
        if len(relative.parts) == 1 and path.name not in ROOT_FILES:
            errors.append(f'{relative}: unexpected root file; review before adding to the release')
        if len(relative.parts) > 1 and relative.parts[0] not in PUBLIC_DIRS:
            errors.append(f'{relative}: outside the public package directories')
        if path.name in PRIVATE_NAMES or path.name.startswith('.env') or '.migrated' in path.name:
            errors.append(f'{relative}: private or runtime artifact')
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            errors.append(f'{relative}: unexpected binary file')
            continue
        # This catches accidental account and document material, not every possible secret.
        if re.search(r'https://docs\.google\.com/(?:document|spreadsheets)/d/[A-Za-z0-9_-]{20,}', text):
            errors.append(f'{relative}: private Google document reference')
        if re.search(r'(?:mcp_token|access_token|refresh_token)=\S+', text):
            errors.append(f'{relative}: access token in a URL')
        if re.search(r'/Users/[A-Za-z0-9_.-]+/', text):
            errors.append(f'{relative}: personal absolute file path')
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^\s)]+)\)', visible_text(text)):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                try:
                    destination.relative_to(ROOT)
                except ValueError:
                    errors.append(f'{relative}: link escapes the public package: {target}')
                    continue
                if not destination.exists():
                    errors.append(f'{relative}: missing local link: {target}')
                elif parsed.fragment and destination.is_file() and destination.suffix == '.md':
                    if unquote(parsed.fragment) not in anchors(destination.read_text()):
                        errors.append(f'{relative}: missing anchor: {target}')

    for name in ('RECIPES.md', 'recipes/STARTER_RECIPES.md'):
        path = ROOT / name
        if not path.exists():
            errors.append(f'{name}: missing recipe collection')
            continue
        text = path.read_text()
        ids = re.findall(r'<a id="([^"]+)"></a>', text)
        if not ids or len(ids) != len(set(ids)):
            errors.append(f'{name}: empty or duplicate recipe IDs')
        for block in re.split(r'<a id="[^"]+"></a>', text)[1:]:
            for field in ('**ID:**', '**Servings:**', '**Time:**', '**Review:**', '#### Ingredients', '#### Method', '#### Source'):
                if field not in block:
                    errors.append(f'{name}: recipe missing {field}')

    commands_path = ROOT / 'COMMANDS.md'
    if commands_path.exists():
        commands = re.findall(r'^## (/\S+)$', commands_path.read_text(), re.M)
        if commands != ['/help', '/plan', '/preferences', '/recipe-add']:
            errors.append('COMMANDS.md: expected exactly the four documented commands')
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f'Public-package boundaries and documentation checks passed for {len(files)} files.')
    print('Run a dedicated secret scanner as well before publishing a release.')
    return 0


if __name__ == '__main__':
    sys.exit(check())
